import mlflow
import mlflow.pyfunc
from typing import List, Dict
from mlflow_mng import common_classes

class MlflowModel():
    
    def __init__(self, mlflow_connection:mlflow):
        self.mlflow = mlflow_connection
    
    def log_custom_model(self, model=None, artifact_path:str=None, model_name:str=None, artifacts:List[common_classes.Artifact]=None):
        # model 은 joblib 파일을 읽어들여 송신해도 된다.
        model_info = dict()
        if model is not None:
            model_info.update({'python_model' : model})
        if artifact_path is not None:
            model_info.update({'artifact_path' : artifact_path,})
        if model_name is not None:
            model_info.update({'registered_model_name' : model_name})
        if artifacts is not None:
            model_info.update({'artifacts'})
            
            def log_artifact(self, artifacts:):
        for artifact in artifacts:
            self.mlflow
        pass
        # 모델 등록
        self.mlflow.log_model(**model_info)