import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from configparser import ConfigParser
from ml.knn.sentence_transformer_process import sentence_transformers_processing
import numpy as np
import ast

# config
config = ConfigParser()
config.read("ml/knn/config.ini")

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