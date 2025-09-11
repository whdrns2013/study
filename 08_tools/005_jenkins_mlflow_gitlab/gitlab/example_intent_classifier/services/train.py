from ml.intent_classifier.intent_classifier_factory import IntentClassifierFactory
from configparser import ConfigParser
import pandas as pd
import numpy as np
import ast
import os

config = ConfigParser()
config.read('core/config.ini')

def train():
    # train data
    MODEL_PATH = config['filepath']['data.embedding.knn']
    embedding_df = pd.read_csv(MODEL_PATH)
    X = embedding_df["vector"].tolist()
    X = np.vstack([np.asarray(ast.literal_eval(v), dtype=np.float32) for v in X])  # (N, D)
    y = embedding_df["intent"].astype(str).values
    
    # intent classifier
    classifier_name = config['model']['intent_classifier']
    classifier = IntentClassifierFactory(classifier_name)
    
    print("\n--- 디버깅 시작 ---")
    try:
        SHARED_DIR = os.environ['SHARED_DIR_MOUNT_POINT']
        print(f"[DEBUG] SHARED_DIR 환경 변수: {SHARED_DIR}")
        
        model_save_rel_path = config['dirpath']['model.save']
        print(f"[DEBUG] config.ini의 모델 저장 경로: {model_save_rel_path}")
        
        MODEL_SAVE_PATH = os.path.join(SHARED_DIR, model_save_rel_path)
        print(f"[DEBUG] 최종 모델 저장 경로: {MODEL_SAVE_PATH}")
        
        model_save_dir = os.path.dirname(MODEL_SAVE_PATH)
        print(f"[DEBUG] 모델 저장 디렉토리: {model_save_dir}")
        
        print(f"[DEBUG] 디렉토리 존재 여부 확인: {os.path.exists(model_save_dir)}")
        if not os.path.exists(model_save_dir):
            print("[DEBUG] 디렉토리가 존재하지 않아 새로 생성합니다.")
            os.makedirs(model_save_dir, exist_ok=True)
            print(f"[DEBUG] 디렉토리 생성 후 존재 여부: {os.path.exists(model_save_dir)}")
            
        print("[DEBUG] 모델 학습 및 저장을 시작합니다.")
        classifier.train(X, y, MODEL_SAVE_PATH)
        print("[DEBUG] 모델 학습 및 저장 완료.")
        
    except KeyError:
        print("[DEBUG] 오류: SHARED_DIR_MOUNT_POINT 환경 변수가 설정되지 않았습니다.")
    except Exception as e:
        print(f"[DEBUG] 예상치 못한 오류 발생: {e}")
    finally:
        print("--- 디버깅 종료 ---\n")
