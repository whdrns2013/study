
## MLflow 서버에 연결하기  

MLflow Client에서 원격 MLflow Tracking Server를 사용하려면 Tracking URI를 설정해야 한다. Tracking URI를 설정하는 방법은 크게 두 가지가 있다.  

### 1. 환경변수 mlflow tracking uri 등록하기  

- 환경변수에 MLFLOW_TRACKING_URI를 등록해놓으면 MLflow Client가 해당 주소를 Tracking URI로 사용한다.  
- 원격 MLflow Server에 연결하는 경우, `http://<도메인>:<포트>` 혹은 `http://<서버ip>:<포트>` 형태의 주소를 사용할 수 있다.  

```python
import os
os.environ["MLFLOW_TRACKING_URI"] = "http://<mlflow-server>" 
print(f"MLflow Tracking URI without server url def: {mlflow.get_tracking_uri()}")
```

OS 환경변수에 직접 등록할 수도 있으며, 이 경우 Python 코드에서 별도로 Tracking URI를 지정하지 않아도 해당 서버를 사용한다.  

```bash
export MLFLOW_TRACKING_URI="http://<mlflow-server>"
```

### 2. 코드에서 명시적으로 mlflow tracking uri 부여하기  

- `mlflow.set_tracking_uri()`를 사용하여 코드에서 Tracking URI를 직접 지정할 수도 있다.  

```python
server_uri = "http://<mlflow-server>"
mlflow.set_tracking_uri(server_uri)
print(f"MLflow Tracking URI with server url def: {mlflow.get_tracking_uri()}")
```

### 3. 주의사항  

#### (1) Tracking Server 연결 확인하기  

mlflow.get_tracking_uri()는 현재 설정된 Tracking URI를 반환할 뿐, 실제 MLflow Server와 정상적으로 통신할 수 있는지를 확인하지는 않는다.

따라서 실제 연결 상태를 확인하려면 MlflowClient를 통해 Experiment 조회와 같이 서버에 요청을 보내는 API를 호출해보는 방법이 있다.  

```python
from mlflow import MlflowClient

client = MlflowClient()
experiment = client.get_experiment_by_name("Default")
print(experiment)
```

- 잘 세팅이 되었다면, 실험 정보를 가져오거나, 실험이 없는 경우 None 을 반환한다.  
- 하지만 잘못 세팅이 되어있다면, 무한 대기를 하거나 오류가 나게 된다.  