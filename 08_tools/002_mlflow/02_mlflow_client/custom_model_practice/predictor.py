from mlflow.pyfunc import PythonModel, PythonModelContext
from mlflow.models import ModelSignature
from mlflow.types.schema import Schema, ColSpec, DataType
from typing import Any
from custom_model_practice.settings import settings

class Predictor:
    def __init__(self,
                 artifacts:dict[str,str]=settings.artifacts,
                 model_config:dict[str,Any]|None=settings.model_config):
        
        self.artifacts =  artifacts
        self.model_config =  model_config
    
    def set_signature(self) -> ModelSignature:
        """
        TODO: 정의
        Signature : 모델 추론의 input, output 데이터 스키마를 정의하고 반환함
        Example:
            input_schema = Schema([
                ColSpec(DataType.string, "stdud_no"),
                ColSpec(DataType.integer, "grade")
            ])
            output_schema = Schema([
                ColSpec(DataType.string, "subj_no"),
                ColSpec(DataType.float, "score")
            ])
        """
        input_schema = None  # TODO: 정의
        output_schema = None # TODO: 정의
        self.signature = ModelSignature(inputs=input_schema, outputs=output_schema)
        return self.signature
    
    def predict(self, model_input:Any) -> Any:
        # TODO: predict 로직 구현
        pass

class MLflowModelWrapper(PythonModel):
    
    def load_context(self, context:PythonModelContext) -> None:
        """
        MLflow 가 모델을 로드할 때 호출하는 코드입니다.
        모델 설정값이나 아티팩트 등을 정의해줍니다.
        """
        artifacts = context.artifacts
        model_config = context.model_config
        self.model = Predictor(artifacts=artifacts, model_config=model_config)
    
    def predict(self, context: PythonModelContext, model_input) -> Any:
        """
        MLflow 가 예측을 수행할 때 호출되는 코드입니다.
        실제 예측 수행은 Predictor 객체에 위임합니다.
        """
        return self.model.predict(model_input)
