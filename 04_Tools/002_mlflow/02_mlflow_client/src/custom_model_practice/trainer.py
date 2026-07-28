from typing import Any
from custom_model_practice.settings import settings
from custom_model_practice.dto import TrainArtifacts, Metric, PreprocessedData

class Trainer:
    def __init__(self):
        self.artifacts: TrainArtifacts = TrainArtifacts()
        self.metric: Metric = Metric() 
        
    def train(self,
              train_data:PreprocessedData,
              train_parameter:dict[str, Any]=settings.train_parameter) -> TrainArtifacts:
        """
        TODO : 구현 - 모델 학습 로직
        """
        pass
    
    def save_artifacts(self,
                       artifacts:Any) -> None:
        """
        TODO: 구현 - 아티팩트 저장 로직
        """
        pass