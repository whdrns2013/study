from schema.dto import OriginData, PreprocessedData, Data
from core.settings import settings
from utils.tokenizer import TokenizingMethod, TokenizerFactory, TokenizerContext
from utils.text_normalizer import Pipe, CaseLowerNormalizer, SpecialCharNormalizer, WhitespaceNormalizer
import pandas as pd
import pickle

class TrainDataHandler:
    def load_data(self, data_path:str) -> OriginData:
        data = pd.read_csv(data_path)
        origin_data = OriginData(data = data)
        return origin_data
    
    def preprocess(self, origin_data: OriginData = None) -> PreprocessedData:
        data = origin_data.data
        utterances = data["utterance"].tolist()
        
        # text normalize
        text_normalizer = Pipe()
        text_normalizer.add_filters([CaseLowerNormalizer(), SpecialCharNormalizer(), WhitespaceNormalizer()])
        utterances = [text_normalizer.run_pipeline(text) for text in utterances]
        
        # tokenizing
        tokenizer_name = settings.TEXT_PREPROCESSING.TOKENIZER_NAME
        tokenizer = TokenizerFactory.create(tokenizer_name)
        tokenizer_context = TokenizerContext(tokenizer, TokenizingMethod[settings.TEXT_PREPROCESSING.TOKENIZING_METHOD].value)
        utterances = tokenizer_context.tokenize(utterances)
        
        intents = data["intent"].tolist()
        preprocessedData = PreprocessedData(data = (utterances, intents))
        return preprocessedData
    
    def save_data(self,
                  data: Data,
                  save_path:str | dict[str, str]) -> None:
        with open(save_path, "wb") as f:
            pickle.dump(data, f)
            