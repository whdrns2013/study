from pydantic import BaseModel
from typing import Any

class Artifact(BaseModel):
    name:str
    local_path:str
    
class Metric(BaseModel):
    metric: str
    score: Any

class Param(BaseModel):
    param_name:str
    param_value:Any