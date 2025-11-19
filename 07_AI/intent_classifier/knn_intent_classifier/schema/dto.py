from typing import Any
from core.settings import settings

class TrainData:
    def __init__(self, data:Any):
        self.schema = [{"utterance":"사용자의 발화 문장.", "intent":"의도"}]
        self.data = data

class PreprocessedData:
    def __init__(self, data:Any):
        self.schema: Any
        self.data = data
