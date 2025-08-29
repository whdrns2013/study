import pandas as pd
from configparser import ConfigParser
from ml.knn.sentence_transformer_process import sentence_transformers_processing
from tqdm import tqdm
import numpy as np

config = ConfigParser()
config.read("ml/knn/config.ini")

def train():

    # 1) 데이터 로드 (컬럼명: question, intent)
    CSV_PATH = config['filepath']['dataset.train.knn']
    df = pd.read_csv(CSV_PATH)

    X = df["question"].astype(str).values
    y = df["intent"].astype(str).values

    # 2) sentence transformer
    EMBEDDING_SAVE_PATH = config['filepath']['data.embedding.knn']
    embedding_results = []
    for sentence in tqdm(X):
        embedding_result = sentence_transformers_processing(sentence)
        embedding_result = np.asarray(embedding_result, dtype=np.float32).ravel().tolist()
        embedding_results.append(embedding_result)
    embedding_result_df = pd.DataFrame({'vector':embedding_results, 'intent':y})
    embedding_result_df.to_csv(EMBEDDING_SAVE_PATH, index=False)
    
    return 0