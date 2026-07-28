
## MLflow Client  

### MLflow Client란  

- MLflow 는 `extras` 기능을 제공하여, 필요한 구성 요소만 선택적으로 설치할 수 있다.  
- MLflow 를 포함한 시스템을 생각해보자.  
- MLflow 서버에는 UI도 있어야 하고, 저장소도 있어야 하고, 로그 기록도 해야 한다. 따라서 라이브러리 용량이 커질 수밖에 없다.  
- 하지만 모델을 학습시키고, 이를 MLflow 서버에 전송하는 사이드는, UI도 필요 없고, 저장소도 필요 없다. 오직 MLflow Tracking API만을 사용할 수 있으면 된다.  
- MLdlow 2.0 버전 이상부터는 `mlflow-client`라는 별도의 경량 패키지가 제공되며, 이는 MLflow Tracking API를 사용하는 데 필요한 최소한의 의존성만 포함하고 있다.  

### MLflow 선택적 설치  

|라이브러리|주요 기능|설치 방법|크기|의존성 포함|
|---|---|---|---|---|
|mlflow|모델 로깅, 실험 관리, 모델 레지스트리, 모델 서빙 등 MLflow의 모든 기능을 포함한 표준 패키지|`pip install mlflow`|32.0 MB|465 MB|
|mlflow-tracing|LLM/GenAI 애플리케이션의 트레이싱(관찰/모니터링)만을 위한 초경량 패키지<br>모델 로깅, 실험 관리, 모델 레지스트리 등은 지원하지 않음|`pip install mlflow-tracing`|6.2 MB|27.1 MB|
|mlflow-skinny|서버, UI, 데이터사이언스 관련 의존성을 제외한 경량 패키지<br>기본적인 트래킹(파라미터/메트릭/아티팩트 로깅)과 모델 레지스트리, 프로젝트 실행 등은 가능|`pip install mlflow-skinny`|10.7 MB|36.2 MB|

- 용량은 2025-11-13 기준, 의존성 패키지 제외, 직접적인 mlflow 라이브러리만.  
- 의존성 패키지들을 포함하면 더 큰 차이가 있을 것임.  

### 설치 방법  

```bash
pip install mlflow-skinny
```

