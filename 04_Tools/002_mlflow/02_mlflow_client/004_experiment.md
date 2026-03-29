## Experiment  

### 개념  

- Experiment는 특정한 목적이나 작업을 위한 여러 개의 runs를 묶은 그룹이다.  
- 쉽게 말하면, 관련된 다수의 runs들을 그룹화하는 것, 또는 그 그룹을 의미하는 것이다.  
- 일반적으로는 특정 문제나 프로젝트에 대한 일련의 시도를 묶는 데 사용된다.  
- e.g. A 라는 모델의 성능 개선을 위한 여러 번의 Run 묶음  
- e.g. 집갑 예측을 위한 선형 회귀 모델 학습 Run, 랜덤 포레스트 학습 Run .. 등을 묶은 것  

### Experiment 클래스  

```python
# mlflow.entities.Experiment
class Experiment(_MlflowObject): # _MlflowObject 상속받음
    def __init__(self ...):
        self._experiment_id     # 실험 아이디
        self._name              # 실험 이름
        self._artifact_location # 실험에 대한 루트 아티팩트 URI
        self._lifecycle_stage   # ‘active’ or ‘deleted’
        self._tags              # 태그
        self._creation_time
        self._last_update_time
    ...
    @classmethod
    def from_proto(cls, proto):
        # Protocol Buffer 형식에서 객체를 생성
    ...
    def to_proto(self):
        # 객체를 다시 Protocol Buffer 형식으로 직렬화하는 역할
```

|속성|설명|
|---|---|
|_experiment_id|해당 실험의 **고유 식별자(ID).**|
|_name|사람이 읽을 수 있는, 해당 experiment의 이름.|
|_artifact_location|이 실험의 모든 실행(Run)들이 아티팩트를 저장하는 루트 저장소 URI.|
|_lifecycle_stage|실험의 현재 상태를 나타낸다.<br>일반적으로 'active' (활성) 또는 'deleted' (삭제됨) 값을 가짐.|
|_tags|실험에 연결된 키-값 쌍의 태그 딕셔너리.<br>주석, 프로젝트 정보 등.|
|_creation_time|실험 생성 시점 타임스탬프|
|_last_update_time|실험 마지막 업데이트 타임스탬프|

> 리뷰  
> 데이터 전송 객체 (DTO) 의 형태가 보인다. : `from_proto` - `to_proto`  
> 어떤 동작을 하기보다는 단순히 "추상화된 개념"을 나타내기 위한 클래스로 보임  

### Experiment 다루기  

#### 생성  

```python
import mlflow
from pathlib import Path

artifact_location = Path.cwd().joinpath("mlruns").as_uri()

mlflow.create_experiment(
    name= "실험 이름",                      # 필수
    artifact_location= artifact_location,  # 옵션
    tags= {"key1":"value1"})               # 옵션
```

`mlflow.create_experiment`  

|파라미터|자료형|설명|필수 여부|
|---|---|---|---|
|name|`str`|experiment 의 이름|필수|
|artifact_location|`str`|실행(Run) 아티팩트를 저장할 위치.(아티팩트 스토리지에 저장됨)<br>만약 제공하지 않으면, Tracking Server가 적절한 기본값을 선택한다.<br>기본값 : `./mlruns` 디렉터리 내<br>로컬 파일 시스템, 원격 객체 저장소(S3, 블롭스토리지 등), NFS나 SFTP 서버에 저장 가능||
|tags|`Dict[str,Any]`|experiment 관련 태그||

#### 정보 가져오기  

```python
import mlflow

mlflow.get_experiment(experiment_id="실험 id")
mlflow.get_experiment_by_name(name="실험 이름")
```

`mlflow.get_experiment`  

|파라미터|자료형|설명|필수 여부|
|---|---|---|---|
|experiment_id|`str`|정보를 가져올 experiment 의 id|필수|

`mlflow.get_experiment_by_name`  

|파라미터|자료형|설명|필수 여부|
|---|---|---|---|
|name|`str`|정보를 가져올 experiment 의 이름|필수|

#### 조건 검색  

```python
import mlflow
from mlflow.entities import ViewType

mlflow.search_experiments(
    view_type= ViewType.ACTIVE_ONLY | ViewType.DELETED_ONLY | ViewType.ALL, # mlflow.entities.ViewType 에 정의된 뷰타입 Enum 중 하나
    max_results= 20, # 검색 결과 개수
    filter_string= "name = 'my_experiment'", # 문자열로 검색. 여러 방법이 있음 (공식문서 참고)
    order_by= ["last_update_time DESC"] # 와 같이 experiment 속성 + [ASC | DESC]
)
```

`mlflow.search_experiments`  

|파라미터|자료형|설명|필수 여부|
|---|---|---|---|
|view_type|`int`|mlflow.entities.ViewType 에 정의된 뷰타입 Enum 중 하나<br>ViewType.ACTIVE_ONLY , ViewType.DELETED_ONLY , ViewType.ALL|필수|
|max_results|`int`|리턴받을 검색 결과 개수||
|filter_string|`str`|문자열로 검색. 공식문서 참고||
|order_by|`List[str]`|experiment 속성 + ASC 혹은 DESC로 정렬 규칙 정함||

#### 삭제  

```python
import mlflow

mlflow.delete_experiment(experiment_id="실험 id")
```

`mlflow.delete_experiment`  

|파라미터|자료형|설명|필수 여부|
|---|---|---|---|
|experiment_id|`str`|삭제하려는 실험 id|필수|


#### 현재 mlflow connection 에 experiment 세팅  

```python
import mlflow

mlflow.set_experiment(experiment_name="실험 이름")
```

`mlflow.set_experiment`  

|파라미터|자료형|설명|필수 여부|
|---|---|---|---|
|experiment_name|`str`|MLflow에서 현재 진행할 Run이 속할 Experiment를 지정|필수|


#### 태그 관리

```python
import mlflow

mlflow.set_experiment_tag(key="key", value="value")
mlflow.set_experiment_tags(tags={"key1" : "value1", "key2" : "value2"})
mlflow.delete_experiment_tag(key="key")
```

experiment에 대한 메타데이터 태그를 세팅하거나 삭제하는 함수들  


## Reference  

[https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=create_experiment#mlflow.create_experiment](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=create_experiment#mlflow.create_experiment)  
[https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html?highlight=experiment#mlflow.entities.Experiment](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html?highlight=experiment#mlflow.entities.Experiment)  