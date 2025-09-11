from abc import ABC, abstractmethod

class IntentClassifier(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def train(self, model_save_path):
        pass
    
    @abstractmethod
    def predict(self):
        pass
    
    
