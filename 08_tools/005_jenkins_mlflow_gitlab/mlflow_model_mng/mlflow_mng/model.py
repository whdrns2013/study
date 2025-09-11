import mlflow

class MlflowModel():
    
    def __init__(self, mlflow_connection:mlflow):
        self.mlflow = mlflow_connection
    
    def log_model(self, model=None, artifact_path:str=None, model_name:str=None):
        # model 은 joblib 파일을 읽어들여 송신해도 된다.
        model_info = dict()
        if model is not None:
            model_info.update({'model' : model})
        if artifact_path is not None:
            model_info.update({'artifact_path' : artifact_path,})
        if model_name is not None:
            model_info.update({'registered_model_name' : model_name})
        self.mlflow.log_model(**model_info)