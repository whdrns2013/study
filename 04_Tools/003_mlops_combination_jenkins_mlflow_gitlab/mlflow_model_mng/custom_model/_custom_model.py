from abc import ABC, abstractmethod
from typing import Any, Dict
import mlflow

class CustomModel(mlflow.pyfunc.PythonModel, ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_context(self, context):
        '''
        - 모델 추론 맥락을 세팅하는 메서드
        - 모델, 추론에 필요한 아티팩트 등을 로딩합니다.
        '''
        pass
    
    @abstractmethod
    def predict(self, model_input):
        '''
        - 추론을 수행하는 메서드
        '''
        pass

# TODO : artifacts 부분의 명확성이 떨어짐
class Context(ABC):
    def __init__(self, model:Any, artifacts:Dict[str, Any]):
        '''
        model : 모델 객체
        artifacts : 추론에 필요한 아티팩트들. {아티팩트이름 : 아티팩트객체}
        '''
        self.model = model
        self.artifacts = artifacts