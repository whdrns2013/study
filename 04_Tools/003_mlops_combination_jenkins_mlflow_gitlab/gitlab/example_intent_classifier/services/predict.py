from ml.embedding.embedding_model_factory import EmbeddingModelFactory
from ml.intent_classifier.intent_classifier_factory import IntentClassifierFactory
from configparser import ConfigParser

config = ConfigParser()
config.read('core/config.ini')

def predict(question:str='안녕! 오늘 날씨가 정말 맑네.'):
    
    # embedding
    embedding_model_name = config['model']['embedding']
    embedding_model = EmbeddingModelFactory(embedding_model_name)
    question_embedded = embedding_model.embedding(question)
    
    # intent classifier
    classifier_name = config['model']['intent_classifier']
    classifier = IntentClassifierFactory(classifier_name)
    
    # predict
    intent = classifier.predict(question_embedded)
    print(intent)

if __name__ == "__main__":
    predict()
