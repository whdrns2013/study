from ml.intent_classifier.intent_classifier import IntentClassifier
from typing import List, Union
from configparser import ConfigParser
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from tqdm import tqdm
import ast
import joblib

class KNNIntentClassifier(IntentClassifier):
    
    def __init__(self):
        self.config = ConfigParser()
        self.config.read("core/config.ini")
        self.model = None
    
    def train(self, question_embeddings:List[List[float]], intent:List[str]):
        
        # train model
        model = KNeighborsClassifier(n_neighbors=5, weights="distance", metric="euclidean", n_jobs=-1)
        model.fit(question_embeddings, intent)
        print('model train success')
        self.model = model

        # save model
        MODEL_PATH = self.config['trained_model_path']['knn']
        joblib.dump(model, MODEL_PATH)
        
        # save embedding
        embedding_results_str = list()
        for emb in tqdm(question_embeddings):
            emb_str = np.asarray(emb, dtype=np.float32).ravel().tolist()
            embedding_results_str.append(emb_str)
        embedding_result_df = pd.DataFrame({'vector':embedding_results_str, 'intent':intent})
        EMBEDDING_SAVE_PATH = self.config['filepath']['data.embedding.knn']
        embedding_result_df.to_csv(EMBEDDING_SAVE_PATH, index=False)
            
        return model

    def predict(self, question_embedding):
        
        # load model
        try:
            if self.model is not None:
                model = self.model
            else:
                MODEL_PATH = self.config['trained_model_path']['knn']
                try:
                    model = joblib.load(MODEL_PATH)
                    self.model = model
                except:
                    raise RuntimeError('Cant loads model')
        except:
            raise RuntimeError('There is no model')
        
        # question embedding reshape
        if question_embedding.ndim == 1:
            question_embedding = question_embedding.reshape(1, -1)  # (1, D)
        
        # predict
        if model:
            pred = model.predict(question_embedding)[0]
            return pred
        