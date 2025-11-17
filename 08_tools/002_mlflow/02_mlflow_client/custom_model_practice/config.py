from abc import ABC, abstractmethod
from pydantic import BaseModel

class Settings(BaseModel):
    # 필요한 세팅 정의
    pass

class CustomSettings(Settings):
    # Data Handler
    train_data_path:str

settings = CustomSettings() # 필요한 세팅값 정의