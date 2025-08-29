from ml.knn.knn_trainer import train
from ml.knn.knn_predictor import predict
from configparser import ConfigParser
import os

config = ConfigParser()
config.read('ml/knn/config.ini')

def main():
    
    question = '안녕! 오늘 날씨가 정말 맑네.'
    MODEL_PATH = config['filepath']['data.embedding.knn']
    if os.path.exists(MODEL_PATH) != True:
        train()
    intent = predict(question)
    print(intent)

if __name__ == "__main__":
    main()
