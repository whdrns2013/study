from schema.dto import OriginData, PreprocessedData, Data
from core.settings import settings
from utils.tokenizer import TokenizingMethod, TokenizerFactory, TokenizerContext
import pandas as pd
import pickle

class TrainDataHandler:
    def load_data(self, data_path:str) -> OriginData:
        data = pd.read_csv(data_path)
        origin_data = OriginData(data = data)
        return origin_data
    
    def preprocess(self, origin_data: OriginData = None) -> PreprocessedData:
        data = origin_data.data
        
        # tokenizing
        tokenizer_name = settings.TEXTPREPROCESSING.TOKENIZER_NAME
        tokenizer = TokenizerFactory.create(tokenizer_name)
        tokenizer_context = TokenizerContext(tokenizer, TokenizingMethod[settings.TEXTPREPROCESSING.TOKENIZING_METHOD])
        utterances = tokenizer_context(data["utterance"].tolist())
        
        intents = data["intent"].tolist()
        preprocessedData = PreprocessedData(data = (utterances, intents))
        return preprocessedData
    
    def save_data(self,
                  data: Data,
                  save_path:str | dict[str, str]) -> None:
        with open(save_path, "wb") as f:
            pickle.dump(data, f)
            