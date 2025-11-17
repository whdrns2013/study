from abc import ABC, abstractmethod

class DataHandler(ABC):
    
    def __init__(self):
        train_data_path:str
    
    @abstractmethod
    def load_data(self):
        pass
    
    @abstractmethod
    def preprocess(self):
        pass