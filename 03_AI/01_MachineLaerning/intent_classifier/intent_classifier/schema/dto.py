from typing import Any
from core.settings import settings
import pandas as pd

class Data:
    def __init__(self, data:Any):
        self.schema: Any
        self.data = data

class OriginData(Data):
    """_summary_
    OriginData.scheam : 데이터 타입과 스키마를 정의해주세요. e.g. self.schema : tuple[list[str]] = ([])
    OriginData.data : 실제 데이터입니다. 인스턴스 생성시 넣어주시면 됩니다.
    """
    def __init__(self, data:pd.DataFrame):
        self.schema:pd.DataFrame = pd.DataFrame({
                                        "utterance" : pd.Series(dtype="string"), # 사용자의 발화 문장
                                        "intent" : pd.Series(dtype="string")     # 의도(클래스)
                                    })
        self.data = data

class PreprocessedData(Data):
    """_summary_
    OriginData.scheam : 데이터 타입과 스키마를 정의해주세요. e.g. self.schema : tuple[list[str]] = ([])
    OriginData.data : 실제 데이터입니다. 인스턴스 생성시 넣어주시면 됩니다.
    """
    def __init__(self, data:tuple[list[str], list[str]]):
        self.schema: tuple[list[str], list[str]] = (
                                                    [], # 사용자의 발화 문장
                                                    []  # 의도(클래스)
                                                   )
        self.data = data

class TrainArtifacts:
    """_summary_
    학습 결과 아티팩트 종류와 경로를 관리하는 데이터 클래스입니다.
    settings 의 artifacts에 dictionary 형태로 정의하거나, 이곳에 바로 정의해주세요.
    model_path 는 필수적으로 넣어주시기 바랍니다.
    """
    def __init__(self):
        for key, value in settings.MODEL.ARTIFACTS.items():
            setattr(self, key, value)
    
    def asdict(self):
        return self.__dict__

class Metric:
    # 추후 구현
    pass