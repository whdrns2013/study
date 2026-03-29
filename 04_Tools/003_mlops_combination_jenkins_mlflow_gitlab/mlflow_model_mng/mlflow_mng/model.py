import mlflow
from mlflow.tracking import MlflowClient
from typing import List, Dict, Union
from mlflow_mng import common_classes

class MlflowModel():
    
    def __init__(self, mlflow_connection:mlflow):
        self.mlflow = mlflow_connection
    
    def log_custom_model(self, model=None, name:str=None, model_name:str=None,
                         artifacts:Union[List[common_classes.Artifact], common_classes.Artifact]=None,
                         signature=None):
        '''doc
        model : 모델을 사용하는 방법에 대해 정의된 클래스
        name : ???
        model_name : 모델 이름
        artifacts : 실제 파일들. 모델, 추론에 필요한 데이터 등이 해당된다. {'아티팩트이름':'로컬의 아티팩트 경로'} 로 구성된다.
        signature : 모델의 입출력 스키마
        '''
        # model 은 joblib 파일을 읽어들여 송신해도 된다.
        model_info = dict()
        if model is not None:
            model_info.update({'python_model' : model})
        if name is not None:
            model_info.update({'name' : name,})
        if model_name is not None:
            model_info.update({'registered_model_name' : model_name})
        if artifacts is not None:
            if isinstance(artifacts, List):
                artifacts_dict = { artifact.name : artifact.local_path for artifact in artifacts}
            elif isinstance(artifacts, common_classes.Artifact):
                artifacts_dict = {artifacts.name : artifacts.local_path}
            model_info.update({'artifacts' : artifacts_dict})
        if signature is not None:
            model_info.update({'signature' : signature})
        # 모델 등록
        self.mlflow.pyfunc.log_model(**model_info)
    
    def infer_signature(self, dataset, input_cols:List[str], output_cols:List[str]):
        input_data = dataset[input_cols]
        output_data = dataset[output_cols]
        signature = self.mlflow.models.infer_signature(input_data, output_data)
        return signature
    
    def load_model(self, model_uri:str):
        try:
            model = self.mlflow.pyfunc.load_model(model_uri)
            return model
        except Exception as e:
            print(e)
            raise RuntimeError(f'cant load model : {e}')
        
    def get_model_name_list(self):
        mlflow = self.mlflow
        client = MlflowClient()
        model_list = client.search_registered_models()
        model_name_list = [ model.name for model in model_list ]
        return model_name_list
    
    def get_latest_version(self, model_name:str):
        mlflow = self.mlflow
        client = MlflowClient()
        latest_version = client.get_latest_versions(model_name)[0].version
        return latest_version
    
    def get_latest_version_uri(self, model_name:str):
        mlflow = self.mlflow
        client = MlflowClient()
        model_uri = client.get_latest_versions(model_name)[0].source
        return model_uri
    
    def get_staged_latest_version_uri(self, model_name:str):
        mlflow = self.mlflow
        client = MlflowClient()
        model_uri = client.get_latest_versions(model_name, stages=['Staging'])[0].source
        return model_uri
    
    def get_production_latest_version_uri(self, model_name:str):
        mlflow = self.mlflow
        client = MlflowClient()
        model_uri = client.get_latest_versions(model_name, stages=['Production'])[0].source
        return model_uri
    
    def get_archived_latest_version_uri(self, model_name:str):
        mlflow = self.mlflow
        client = MlflowClient()
        model_uri = client.get_latest_versions(model_name, stages=['Archived'])[0].source
        return model_uri