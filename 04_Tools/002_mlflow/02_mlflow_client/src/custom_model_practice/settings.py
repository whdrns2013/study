from pydantic import BaseModel
from typing import Any

# TODO: 모델에 맞게 설정값을 채워주세요.
# TODO: 이 부분은 추후 env + pydantic.BaseSettings 조합으로 변경할 예정

class ModelSettings(BaseModel):
    """전역 설정값. TODO: 알맞은 값으로 설정해주세요."""
    origin_data_path        :str | dict[str, str] = "data/origin_data.csv"
    preprocessed_data_path  :str | dict[str, str] = "data/train_data.csv"
    train_parameter         :dict[str,Any] | None = None
    artifacts               :dict[str,str] = {"model_path" : "artifacts/model.pickle"}
    model_config            :dict[str,Any] | None = None
    extra_pip_requirements  :list[str] | None = None   # e.g. ["pydantic==1.0.0", ...]
    model_name              :str = "model_name"

settings = ModelSettings() # 필요한 세팅값 정의