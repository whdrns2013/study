import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from configparser import ConfigParser
from ml.embedding.sentence_transformer_model import sentence_transformers_processing
import numpy as np
import ast

# config
config = ConfigParser()
config.read("core/config.ini")

def predict(sentence:str)->str:
    
    # load_model_file
    MODEL_PATH = config['filepath']['data.embedding.knn']
    embedding_df = pd.read_csv(MODEL_PATH)
    
    # 1) embedding
    embedding = sentence_transformers_processing(sentence)
    
    # 2) load embedding
    X = embedding_df["vector"].tolist()
    X = np.vstack([np.asarray(ast.literal_eval(v), dtype=np.float32) for v in X])  # (N, D)
    y = embedding_df["intent"].astype(str).values
    
    # 3) embedding reshape
    embedding = np.asarray(embedding, dtype=np.float32)
    if embedding.ndim == 1:
        embedding = embedding.reshape(1, -1)  # (1, D)
    
    # 4) knn
    knn = KNeighborsClassifier(n_neighbors=5, weights="distance", metric="euclidean", n_jobs=-1)
    knn.fit(X, y)
    
    # 5) pred
    pred = knn.predict(embedding)[0]
    return pred

import pandas as pd
from configparser import ConfigParser
from ml.embedding.sentence_transformer_model import sentence_transformers_processing
from tqdm import tqdm
import numpy as np

config = ConfigParser()
config.read("core/config.ini")

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