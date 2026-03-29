




## Model 클래스  

```python
# mlflow.models.model

class Model:
    """
    An MLflow Model that can support multiple model flavors. Provides APIs for implementing
    new Model flavors.
    """
    def __init__(
        self,
        artifact_path=None,
        run_id=None,
        utc_time_created=None,
        flavors=None,
        signature=None,  # ModelSignature
        saved_input_example_info: dict[str, Any] | None = None,
        model_uuid: str | Callable[[], str] | None = lambda: uuid.uuid4().hex,
        mlflow_version: str | None = mlflow.version.VERSION,
        metadata: dict[str, Any] | None = None,
        model_size_bytes: int | None = None,
        resources: str | list[Resource] | None = None,
        env_vars: list[str] | None = None,
        auth_policy: AuthPolicy | None = None,
        model_id: str | None = None,
        prompts: list[str] | None = None,
        **kwargs,
    ):
```

`mlflow.models.model.Model`  

- MLflow에서 정의하는 머신러닝 모델의 표준적은 구조를 추상화한 클래스 (mlflow : "우리는 모델을 이렇게 정의하고 있어!")  
- sklearn, pytorch, tensorflow 등 다양한 프레임워크의 모델과 그와 관련된 메타데이터, 아티팩트, 시그니처 정보를 받아 MLflow에서 다루는 표준 모델 구조로 통합하는 역할을 한다.  
- mlflow 에서 모델을 다룰 때 내부적으로 이 "Model" 클래스의 인스턴스를 만든다.  
- 이렇게 생성된 Model 의 인스턴스는 `mlflow.log_model()`을 통해 MLflow Server에 모델을 기록하거나, 모델 배포에 필요한 `MLmodel 메타데이터 파일`을 생성하는 등 모델과 관련된 여러 부분에 핵심 요소로 사용된다.  

|속성|설명|
|---|---|
|artifact_path|모델이 저장될 Artifact Store 내부의 논리적(상대) 경로<br>실제 물리적 저장 위치는 MLflow가 사용하는 artifact store(S3, 로컬, GCS 등)에 따라 결정됨|
|run_id|이 모델이 속한 MLflow Run의 ID.<br>같은 Run 안의 다른 아티팩트 및 로그와 연결하는 키 역할|
|utc_time_created|모델이 생성된 UTC 시간. 모델 버전 및 생성 이력을 추적할 때 사용.|
|flavors|이 모델을 어떤 방식으로 로드할 수 있는지를 정의한 딕셔너리 형태의 데이터.|
|signature|입력/출력 스키마(컬럼명, dtype, shape) 정보. 모델 예측 시 형식을 보장하기 위함.<br>`ModelSignature` 객체이다.|
|saved_input_example_info|입력 예시 데이터를 저장한 경우 그 메타데이터(파일 경로, 컬럼 정보 등).<br>모델 사용자가 입력 형식을 쉽게 이해하도록 도움.|
|model_uuid|모델 객체에 부여되는 고유 ID(UUID).|
|mlflow_version|이 모델이 저장될 때 사용된 MLflow 버전.<br>모델 호환성 문제를 디버깅할 때 유용|
|metadata|사용자가 추가로 넣는 자유 형식의 메타데이터 딕셔너리.<br>실험 정보, 태그, 커스텀 옵션 등을 포함 가능.|
|model_size_bytes|모델 파일의 실제 크기(바이트).<br>스토리지 관리, 전송, 배포 시 용량 정보를 알고 싶을 때 활용.|
|resources|모델 실행에 필요한 리소스 요구사항.<br>예: GPU, CPU 개수, 메모리 등. Model Serving 환경에서 사용 가능.|
|env_vars|모델 실행 시 필요한 환경 변수 목록.<br>환경 재현성 및 Serving 시 필요한 설정을 전달할 때 사용.|
|auth_policy|모델 접근 제어(Authorization 정책).<br>MLflow 모델에 대한 보안 정책이나 인증 규칙을 지정.|
|model_id|MLflow Model Registry에서 관리되는 모델 ID.<br>등록된 모델의 고유 식별자. 버전 관리와 연결됨.|
|prompts|LLM 관련 기능에서 사용되는 프롬프트 리스트.<br>모델이 프롬프트 기반 동작을 제공할 때 저장됨.|
|kwargs|위 속성 외에 확장 기능을 위한 추가 키워드 파라미터들.<br>플러그인, 커스텀 메타데이터 확장 시 활용.|

#### model_uuid 와 model_id  

|구분|설명|
|---|---|
|model_uuid|Model 객체 자체의 내부 고유 ID<br>Model 객체를 생성할 때 자동으로 만들어진다.<br>Model 인스턴스를 구분하기 위한 내부 식별자이다.|
|model_id|MLflow Model Registry에 모델을 "등록"했을 때 주어지는 공식 ID<br>Registry 내 모델을 식별하고 버전을 관리하기 위한 ID|

## Reference  

[https://mlflow.org/docs/latest/api_reference/python_api/mlflow.models.html#mlflow.models.Model](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.models.html#mlflow.models.Model)  