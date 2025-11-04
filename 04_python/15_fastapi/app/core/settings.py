from pydantic_settings import BaseSettings, SettingsConfigDict

class ServiceSettings(BaseSettings):
    PORT:int = 8080
    BIND:str = "0.0.0.0"
    TIMEOUT:int = 10
    
class EndpointSettings(BaseSettings):
    HEALTHCHECK:str = "/health_check"
    PREFIX:str = "/api/v1"
    
class AppSettings(BaseSettings):
    SERVICE:ServiceSettings
    ENDPOINT:EndpointSettings
    model_config = SettingsConfigDict(
        env_file="app/core/.env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__"
    )

settings = AppSettings()