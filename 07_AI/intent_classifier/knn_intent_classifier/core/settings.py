from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, Any

class DirPathSettings(BaseSettings):
    DATA_PATH:str = "data/"
    ARTIFACT_PATH:str = "artifacts/"

class DataSettings(BaseSettings):
    TRAIN_DATA:str = "train_data.txt"
    
class ModelSettings(BaseSettings):
    """TODO: 설정값을 기재하거나 env 파일에 설정해주세요."""
    ARTIFACTS               :str = "abc"

class AppSettings(BaseSettings):
    DIRPATH: DirPathSettings
    DATA: DataSettings
    MODEL: ModelSettings
    
    model_config = SettingsConfigDict(
        env_file="core/.env", 
        env_file_encoding='utf-8',
        env_nested_delimiter='__',
        case_sensitive=True
    )
    
settings = AppSettings()