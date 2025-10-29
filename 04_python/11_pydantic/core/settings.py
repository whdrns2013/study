from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class ServiceSettings(BaseModel):
    timeout:str = "60"                # .env 파일에서는 대문자로 선언했더라도, pydantic은 소문자로 바꿔서 인식할 것임.
    multiprocessor_num:str = "10"
    
class DirPathSettings(BaseModel):
    data_path:str = "data"
    artifact_path:str = "artifacts"
    log_path:str = "logs"

class LoggingSettings(BaseModel):
    expire_day: str = "90"
    log_level:str = "DEBUG"
    
class Settings(BaseSettings):       # 세팅 클래스는 pydantic_settings의 BaseSettings 를 상속받아야 함.
    service: ServiceSettings        # pydantic-settings가 .env 파일의 SERVICE__... 같은 접두사를 인식하게 하려면, Settings 클래스 안의 속성 이름이 그 접두사(의 소문자 버전)와 정확히 일치해야 함
    dirpath: DirPathSettings              # 타입 힌트만 적어주면 됨
    logging: LoggingSettings
    
    # .env 파일의 위치를 명시적으로 지정 (파일 이름, 인코딩)
    model_config = SettingsConfigDict(
        env_file="core/.env", 
        env_file_encoding='utf-8',
        env_nested_delimiter='__'   # __ 로 구분
    )
    
settings = Settings() # 이렇게 선언해놓으면 다른 어떤곳에서 import를 하더라도 동일한 setting 값을 가질 수 있다. (변수가 생성된 타이밍 동일, 동일한 객체임)



# pydantic_settings.exceptions.SettingsError: error parsing value for field "path" from source "EnvSettingsSource"
# pydantic-settings가 Settings 클래스의 path: PathSettings 필드를 채우려고 할 때, .env 파일의 PATH__... 변수들보다 **운영체제(Windows)의 기본 환경 변수인 PATH**를 먼저 발견했기 때문일 가능성이 높음
# https://gemini.google.com/app/c6feb8741c961192?hl=ko