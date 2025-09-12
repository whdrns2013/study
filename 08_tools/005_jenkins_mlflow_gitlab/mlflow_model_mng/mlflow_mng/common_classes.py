from pydantic import BaseModel
from typing import Any

class Artifact(BaseModel):
    mlflow_path:str
    local_path:str
    
class Metric(BaseModel):
    metric: str
    score: Any

class TrainParam(BaseModel):
    param_name:str
    param_value:Any