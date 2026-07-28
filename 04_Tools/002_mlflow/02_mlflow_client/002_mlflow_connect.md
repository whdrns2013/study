
## MLflow 서버에 연결하기  

- MLflow 서버에 연결하는 방법은 두 가지가 있다.  

### 1. 환경변수 mlflow tracking uri 등록하기  

- 환경변수에 mlflow tracking uri를 등록해놓으면, 자동으로 해당 mlflow server에 연결된다.  
- tracking uri는 `도메인 주소` 혹은 `서버ip:포트` 여야 한다.  

```python
import os
os.environ["MLFLOW_TRACKING_URI"] = "http://<mlflow-server>" # 또는 OS환경변수에 등록
print(f"MLflow Tracking URI without server url def: {mlflow.get_tracking_uri()}")
```

### 2. 명시적으로 mlflow tracking uri 부여하기  

- 명시적으로 mlflow tracking uri를 부여할 수도 있다.  
- tracking uri는 `도메인 주소` 혹은 `서버ip:포트` 여야 한다.  

```python
server_uri = "http://<mlflow-server>"
mlflow.set_tracking_uri(server_uri)
print(f"MLflow Tracking URI with server url def: {mlflow.get_tracking_uri()}")
```

### tracking uri가 제대로 세팅되었는지 체크하기  

- `get_experiment` 와 같은 메서드로 실험을 가져오는 등의 검증 작업을 거치면 된다.  
- 잘 세팅이 되었다면, 실험 정보를 가져오거나, 실험이 없는 경우 None 을 반환한다.  
- 하지만 잘못 세팅이 되어있다면, 무한 대기를 하거나 오류가 나게 된다.  

```python
experiments = client.get_experiment_by_name("default")
print(f"Experiments List : {experiments}")
>> Experiments List : None
```