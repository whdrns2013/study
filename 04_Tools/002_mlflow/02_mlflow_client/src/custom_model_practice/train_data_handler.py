from custom_model_practice.dto import TrainData, PreprocessedData
from custom_model_practice.settings import settings

class TrainDataHandler:
    def load_data(self,
                  data_path:str | dict[str, str] = settings.origin_data_path
                  ) -> TrainData:
        """
        TODO : 구현
        Example:
            self.train_data = pd.read_csv(self.train_data_path)
            return self.train_data
        """
        pass
    
    def preprocess(self,
                   origin_data: TrainData = None
                   ) -> PreprocessedData:
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
                  save_path:str | dict[str, str] = settings.preprocessed_data_path) -> None:
        """
        TODO: 구현
        """
        pass