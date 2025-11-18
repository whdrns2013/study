from custom_model_practice.train_data_handler import TrainDataHandler
from custom_model_practice.trainer import Trainer, TrainArtifacts
from custom_model_practice.predictor import Predictor, MLflowModelWrapper
from custom_model_practice.dto import PreprocessedData
import mlflow
from custom_model_practice.settings import settings
from typing import Any

class ModelOrchestrator:
    
    def prepare_data_pipeline(self,
                            origin_data_path:str | dict[str, str]=settings.origin_data_path,
                            preprocessed_data_path:str | dict[str, str]=settings.preprocessed_data_path) -> PreprocessedData:
        data_handler = TrainDataHandler()
        origin_data = data_handler.load_data(data_path = origin_data_path)
        preprocessed_data = data_handler.preprocess(origin_data = origin_data)
        data_handler.save_data(data = preprocessed_data, save_path = preprocessed_data_path)
        return preprocessed_data
    
    def train_pipeline(self,
                       train_data_path:str | dict[str, str]=settings.preprocessed_data_path,
                       train_parameter:dict[str,Any]=settings.train_parameter) -> TrainArtifacts:
        trainer = Trainer()
        data_handler = TrainDataHandler()
        train_data = data_handler.load_data(data_path = train_data_path)
        artifacts = trainer.train(train_data = train_data, train_parameter = train_parameter)
        return artifacts
    
    def predict_pipeline(self,
                         model_input:Any,
                         artifacts:dict[str,str]=settings.artifacts,
                         model_config:dict[str,Any]=settings.model_config) -> Any:
        predictor = Predictor(artifacts = artifacts, model_config = model_config)
        predict_result = predictor.predict(model_input = model_input)
        return predict_result
    
    def model_regist_pipeline(self,
                              artifacts:dict[str,str]=settings.artifacts,
                              model_config:dict[str,Any]=settings.model_config) -> None:
        """mlflow 사용시, service 에서 train_pipeline -> model_regist_pipeline 로직 구현하여 사용할 수 있습니다."""
        predictor = Predictor(artifacts = artifacts, model_config = model_config)
        signature = predictor.set_signature()
        artifacts = predictor.artifacts
        extra_pip_requirements = settings.extra_pip_requirements
        mlflow.pyfunc.log_model(
            python_model=MLflowModelWrapper(),
            name=settings.model_name,
            artifacts=artifacts,
            model_config = model_config,
            signature=signature,
            extra_pip_requirements=extra_pip_requirements
        )