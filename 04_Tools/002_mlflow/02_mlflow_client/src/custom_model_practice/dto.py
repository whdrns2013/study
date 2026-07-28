from typing import Any
from custom_model_practice.settings import settings

class TrainData:
    def __init__(self, data:Any):
        self.schema: Any # 여기서 직접 정의 (처음 보는 사람 모델 이해도 위함)
        self.data = data

class PreprocessedData:
    def __init__(self, data:Any):
        self.schema: Any # 여기서 직접 정의 (처음 보는 사람 모델 이해도 위함)
        self.data = data

class TrainArtifacts:
    """
    학습 결과 아티팩트 종류와 경로를 관리하는 데이터 클래스
    settings 의 artifacts에 Dictionary 형태로 정의해주세요.
    model_path 는 필수적으로 넣어주시기 바랍니다.
    """
    def __init__(self):
        for key, value in settings.artifacts.items():
            setattr(self, key, value)
    
    def asdict(self):
        return self.__dict__

class Metric:
    # 추후 구현
    pass