from abc import ABC, abstractmethod

class IntentClassifier(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass
    
    
