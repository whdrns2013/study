from schema.dto import TrainData, PreprocessedData
from core.settings import settings
import pandas as pd

class TrainDataHandler:
    def load_data(self, data_path:str) -> TrainData:
        data = pd.read_csv(data_path)
        train_data = TrainData(data = data)
        return train_data
    
    def preprocess(self, data: TrainData = None) -> PreprocessedData:
        """
        TODO: 구현
        Example:
            train_data = self.train_data if data == None else data 
            ...preprocessing...
            self.preprocessed_data = preprocessed_data
            return preprocessed_data
        """
        pass
    
    def save_data(self,
                  data: PreprocessedData,
                  save_path:str | dict[str, str]) -> None:
        """
        TODO: 구현
        """
        pass