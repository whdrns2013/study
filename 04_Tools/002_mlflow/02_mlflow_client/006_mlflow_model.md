
## MLflow Models  

### 개념  

MLflow Models 는 머신러닝 모델을 패키징하기 위한 표준 형식이다. 쉽게 말해, 머신러닝 모델을 위한 표준 포장 상자이다.  

이러한 MLflow Models 형식의 핵심은, 모델을 Flavor로 저장하는 규칙을 정의해서, 여러 환경에서 각 배포 도구가 모델을 문제 없이 이해하고 사용할 수 있도록 하는 것이다.  

쉽게 말해 개발자가 학습시킨 모델을 누군가가 사용할 때, 그 모델이 `scikit-learn` 으로 만들어졌는지, `PyTorch`로 만들어졌는지 신경 쓸 필요 없이, 어디서든 쉽게 꺼내 쓸 수 있는 표준 형식으로 묶어주는 것이다.  

### 저장 구조(Storage Format)  

각 MLflow Model은 디렉터리로 저장된다. 그리고 이 디렉터리의 루트에는 YAML 형식의 `MLModel` 파일이 존재하며, 그 외 기타 여러 파일들이 존재할 수 있다. `MLModel` 파일은 다음 단락에서 다루기로 한다.  

`MLModel` 파일 외로는 모델 바이너리 파일(학습된 모델 파일, e.g. `model.pkl`) 및 기타 지원 파일(추론에 필요한 파일 등), 종속성 및 환경 파일, 인풋 샘플, 시그니처, 환경변수 등을 포함할 수 있다.  

```bash
# 저장 구조 예시
model/
├── MLmodel     # MLmodel 파일
├── model.pkl   # 모델 바이너리 파일 (학습된 모델 파일)
├── conda.yaml          # 종속성
├── python_env.yaml     # 종속성
├── requirements.txt    # 종속성
├── input_example.json (optional)           # predict 메서드로 추론할 때 기대하는 입력 형식
├── serving_input_example.json (optional)   # REST API 페이로드 예시
├── environment_variables.txt (optional)    # 환경변수
└── ... 추가파일 # 전처리, 유틸 등 추가 코드
```

### MLmodel 파일  

MLmodel 파일은 모델이 지원하는 모든 Flavor를 YAML 형식으로 정의한 파일이다.  

|필드|설명|
|---|---|
|`flavors`|flavor 에 대한 명세|
|`time_created`|모델이 생성된 날짜와 시간|
|`run_id`|모델을 생성한 Run의 고유 식별자|
|`signature`|JSON 형식의 시그니처<br>(입력/출력 스키마(컬럼명, dtype, shape) 정보)|
|`input_example`|predict 입력 예제를 포함하는 아티팩트에 대한 참조 ㄸ도는 아티팩트의 경로|
|`databricks_runtime`|모델이 Databricks 노트북이나 작업에서 학습된 경우<br>Databricks 런타임 버전 및 유형 정보|
|`mlflow_version`|모델을 기록(log)하는 데 사용된 MLflow의 버전|

```yaml
# 예시 (검증 필요)
time_created: 2018-05-25T17:28:53.35

flavors:
  sklearn:
    sklearn_version: 0.19.1
    pickled_model: model.pkl
  python_function:
    loader_module: mlflow.sklearn
    python_version: 3.10.0
    env: conda.yaml

run_id: 1a2b3c4d5e6f7g8h9i0j1k2l
mlflow_version: 2.9.2
artifact_path: model
```

### Signature 와 Input Example    

#### Signature  

모델의 입력, 출력 및 매개변수에 대해 예상되는 형식을 정의한 것이다. 모델이 정확히 어떤 데이터를 예상하고 무엇을 반환할지 명시하는 일종의 계약(Contract) 역할을 한다.

#### Input Example  

유효한 모델 입력의 구체적인 예시이다. 이는 개발자가 필요한 데이터 형식을 이해하는 데 도움을 주며, 모델이 올바르게 작동하는지 확인하는 데 사용될 수 있다.  

#### 중요한 이유  

| 항목 | 설명 |
| :--- | :--- |
| 일관성 (Consistency) | 모든 모델 상호 작용이 동일한 데이터 형식을 따르도록 보장한다. |
| 유효성 검사 (Validation) | 모델에 도달하기 전에 데이터 형식 오류를 사전에 포착한다. |
| 문서화 (Documentation) | 모델 사용법에 대한 살아있는 문서 (Living Documentation) 역할을 한다. |
| 배포 안전성 (Deployment Safety) | MLflow 배포 도구가 들어오는 요청을 자동으로 검증할 수 있도록 한다. |
| UI 통합 (UI Integration) | MLflow UI에 모델의 명확한 요구 사항을 표시할 수 있도록 한다. |

#### 자세한 내용  

자세한 내용은 별도 문서에서 소개하도록 한다.  


### 실행 환경 재현(종속성)  

MLflow는 환경 재현을 위해 모델이 로깅될 때마다 자동으로 환경을 기록한다. 기록은 `conda.yaml`, `python_env.yaml` 및 파일 또는 `requirements.txt`를 사용하며, 모델을 가져다 사용할 때, 종속성을 재현하는 데 활용된다.

#### python_env.yaml  

```yaml
python: 3.9.8
build_dependencies:
  - pip==23.3.2
  - setuptools==69.0.3
  - wheel==0.42.0
dependencies:
  - -r requirements.txt
```

#### conda.yaml  

```yaml
name: mlflow-env
channels:
  - conda-forge
dependencies:
  - python=3.9.8
  - pip
  - pip:
      - mlflow==2.9.2
      - scikit-learn==1.3.2
      - cloudpickle==3.0.0
```

#### requirements.txt  

```yaml
mlflow==2.9.2
scikit-learn==1.3.2
cloudpickle==3.0.0
```

#### 종속성 추가  

MLflow 는 모델 플레이버를 기반으로 필요한 종속성을 추론한다. 하지만 모델 외적으로 필요한 전처리 등 다른 라이브러리가 필요한 경우는 직접 종속성을 추가해줘야 한다.  

```python
import mlflow

mlflow.pyfunc.log_model(
    python_model=CustomModel(),
    name="model",
    extra_pip_requirements=["pandas==2.0.3"], # 종속성 추가
    input_example=input_data,
)
```

#### 종속성을 처음부터 정의  

```python
import mlflow

mlflow.sklearn.log_model(
    sk_model=model,
    name="model",
    pip_requirements=[
        "mlflow-skinny==2.9.2",
        "cloudpickle==2.5.8",
        "scikit-learn==1.3.1",
    ],
)
```

### 추가 파일  

MLflow에서는 train, predict 외로 개발자가 지정한 코드파일을 저장하는 기능도 지원한다. 이러한 코드파일은 전처리나 특정한 유틸 등을 포함할 수 있다. 이를 위해 모델 로깅시 `code_path`를 지정해줘야 한다.  

```python
import mlflow

with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        python_model=MyModel(),
        name="model",
        input_example=input_data,
        code_paths=["utils.py"], # 파일 추가
    )
```


## Reference  

[https://mlflow.org/docs/latest/ml/model/](https://mlflow.org/docs/latest/ml/model/)  
[https://mlflow.org/docs/latest/ml/model/dependencies/#how-mlflow-records-dependencies](https://mlflow.org/docs/latest/ml/model/dependencies/#how-mlflow-records-dependencies)  