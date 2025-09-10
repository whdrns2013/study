from ml.intent_classifier.intent_classifier_factory import IntentClassifierFactory
from configparser import ConfigParser
import pandas as pd
import numpy as np
import ast

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
    classifier.train(X, y)
