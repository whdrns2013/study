from ml.intent_classifier.knn_intent_classifier import KNNIntentClassifier

class IntentClassifierFactory():
    
    def __new__(cls, classifier_name:str):
        if classifier_name == 'knn':
            return KNNIntentClassifier()