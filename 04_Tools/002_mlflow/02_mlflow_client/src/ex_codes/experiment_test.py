import mlflow
from mlflow.entities import ViewType
from pathlib import Path

# 실험 생성
artifact_location = Path.cwd().joinpath("mlruns").as_uri()

mlflow.create_experiment(
    name= "실험 이름",                      # 필수
    artifact_location= artifact_location,  # 옵션
    tags= {"key1":"value1"})               # 옵션

# 실험 정보 가져오기
mlflow.get_experiment(experiment_id="실험 id")
mlflow.get_experiment_by_name(name="실험 이름")

# 다양한 조건으로 Experiment를 검색
mlflow.search_experiments(
    view_type= ViewType.ACTIVE_ONLY | ViewType.DELETED_ONLY | ViewType.ALL, # mlflow.entities.ViewType 에 정의된 뷰타입 Enum 중 하나
    max_results= 20, # 검색 결과 개수
    filter_string= "name = 'my_experiment'", # 문자열로 검색. 여러 방법이 있음 (공식문서 참고)
    order_by= ["last_update_time DESC"] # 와 같이 experiment 속성 + [ASC | DESC]
)

# 실험 삭제
mlflow.delete_experiment(experiment_id="실험 id")


# 현재 mlflow connection 에 실험 세팅
mlflow.set_experiment(experiment_name="실험 이름")

# 태그 관리
mlflow.set_experiment_tag(key="key", value="value")
mlflow.set_experiment_tags(tags={"key1" : "value1", "key2" : "value2"})
mlflow.delete_experiment_tag(key="key")

