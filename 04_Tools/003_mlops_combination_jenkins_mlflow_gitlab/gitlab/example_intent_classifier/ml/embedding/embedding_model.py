from abc import ABC, abstractmethod


class EmbeddingModel(ABC):
    
    def __init__(self):
        pass
    
    @abstractmethod
    def init_model(self):
        pass
    
    @abstractmethod
    def embedding(self):
        pass