import mlflow
from typing import List, Dict, Union
from mlflow.tracking import MlflowClient

class MlflowDeployment:
    
    def __init__(self, mlflow_connection:mlflow):
        self.mlflow = mlflow_connection
    
    def stage(self, model_name, model_version, new_stage, archive:bool=True):
        '''
        [stage]
        None : 새로운 모델 버전의 초기 상태. 모델이 등록은 되었지만, 아직 검토되거나 역할이 부여되지 않은 단계.
        Staging : 초기 테스트를 통과하고, 실제 서비스에 투입되기 전 통합 테스트나 A/B 테스트 같은 조금 더 본격적인 검증을 준비하는 모델을 위한 단계.
        Production : 현재 실제 사용자들에게 서비스를 제공하고 있는 모델 버전을 위한 단계
        Archived : 오래되거나 성능이 낮은 모델을 보관하는 단계
        
        [archive]
        archive_existing_versions : 새로운 버전을 'Production'으로 올릴 때 기존에 'Production' 딱지를 달고 있던 버전은 자동으로 'Archived'(보관됨) 스테이지로 옮긴다.
        '''
        mlflow = self.mlflow
        client = MlflowClient()
        client.transition_model_version_stage(
            name = model_name,
            version = model_version,
            stage = new_stage,
            archive_existing_versions=archive
        )
        return 0
    
    def make_docker_image(self, model_uri, docker_image_name):
        self.mlflow.models.build_docker(
            model_uri = model_uri,
            name = docker_image_name
        )