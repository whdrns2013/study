
## MLflow Client  

### 1. MLflow Client란  

MLflow를 사용하는 시스템은 크게 **Server Side**와 **Client Side**로 나누어 볼 수 있다. 지난 포스팅까지는 이 중 Server Side를 살펴보았다. MLflow Server는 Tracking API를 제공하고, 실험 및 모델 정보를 Backend Store에 저장하며, Artifact Store와 연결하여 아티팩트를 관리한다. 또한 사용자가 실험과 모델 정보를 조회할 수 있도록 Web UI를 제공한다.

이번 포스팅부터는 **Client Side**를 살펴본다. Client Side에서는 모델을 학습하거나 평가하는 과정에서 발생한 파라미터, 메트릭, 태그, 아티팩트 등을 MLflow Server에 기록한다.

Client Side에서는 MLflow Server와 통신하기 위한 기능이 주로 필요하며, Server 자체를 구동하기 위한 Web UI나 SQL 저장소 등의 기능은 필요하지 않다. 따라서 Client Side에서 전체 MLflow 기능과 의존성을 모두 설치하는 것은 불필요할 수 있다.  

MLflow는 이러한 Client 환경에서 보다 가볍게 사용할 수 있도록 mlflow-skinny 패키지를 제공한다. mlflow-skinny는 전체 기능을 포함하는 mlflow에서 Server, UI, SQL 저장소 및 일부 데이터 사이언스 관련 의존성을 제외한 경량 패키지이다.  


### 2. MLflow 선택적 설치  

|라이브러리|주요 기능|설치 방법|설치 용량(의존성 포함)|
|---|---|---|---|
|mlflow|모델 로깅, 실험 관리, 모델 레지스트리, 모델 서빙 등 MLflow의 모든 기능을 포함한 표준 패키지|`pip install mlflow`|약 484 MB|
|mlflow-tracing|LLM/GenAI 애플리케이션의 트레이싱(관찰/모니터링)만을 위한 초경량 패키지<br>모델 로깅, 실험 관리, 모델 레지스트리 등은 지원하지 않음|`pip install mlflow-tracing`|약 48 MB|
|mlflow-skinny|서버, UI, 데이터사이언스 관련 의존성을 제외한 경량 패키지<br>기본적인 트래킹(파라미터/메트릭/아티팩트 로깅)과 모델 레지스트리, 프로젝트 실행 등은 가능|`pip install mlflow-skinny`|약 63 MB|

> 용량은 MLflow 3.16.1, macOS 환경에서 각 패키지를 빈 가상환경에 설치한 후 의존성을 포함하여 측정하였다. 설치 용량은 Python 버전과 운영체제 등에 따라 달라질 수 있으므로 패키지 간 상대적인 크기를 비교하는 용도로만 참고하길 바란다.  

### 3. 설치 방법

Client Side에서 원격 MLflow Tracking Server를 사용한다면 다음과 같이 mlflow-skinny를 설치할 수 있다.

```bash
pip install mlflow-skinny
```

설치 후 Client가 요청을 전송할 MLflow Tracking Server를 지정한다.

```python
import mlflow
mlflow.set_tracking_uri("http://mlflow-server:5000")
```

또는 환경변수로 지정할 수도 있다.

```bash
export MLFLOW_TRACKING_URI="http://mlflow-server:5000"
```

## Reference  

[https://pypi.org/project/mlflow-skinny/3.16.1/?utm_source=chatgpt.com](https://pypi.org/project/mlflow-skinny/3.16.1)  
