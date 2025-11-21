from schema.dto import OriginData, PreprocessedData, Data
from core.settings import settings
import pandas as pd
import pickle
from konlpy.tag import Okt

class TrainDataHandler:
    def load_data(self, data_path:str) -> OriginData:
        data = pd.read_csv(data_path)
        origin_data = OriginData(data = data)
        return origin_data
    
    def preprocess(self, origin_data: OriginData = None) -> PreprocessedData:
        data = origin_data.data
        utterances = tokenizing_pos(data["utterance"].tolist())
        intents = data["intent"].tolist()
        preprocessedData = PreprocessedData(data = (utterances, intents))
        return preprocessedData
    
    def save_data(self,
                  data: Data,
                  save_path:str | dict[str, str]) -> None:
        with open(save_path, "wb") as f:
            pickle.dump(data, f)
            
# 전처리 옵션 1
def tokenizing_nouns(utterances):
    okt = Okt()
    return [okt.nouns(word) for word in utterances]

# 전처리 옵션 2
def tokenizing_pos(utterances):
    okt = Okt()
    return [[word for word, pos in okt.pos(sentence, stem=True) if pos in ["Noun", "Verb", "Adjective"]] for sentence in utterances]

# 전처리 옵션 3
def tokenizing_phrase(utterances):
    okt = Okt()
    return [okt.phrases(sentence) for sentence in utterances]