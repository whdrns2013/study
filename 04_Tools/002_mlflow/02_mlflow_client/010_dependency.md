
## Model 종속성 관리  


### 종속성 관리의 정의  

- 소프트웨어나 시스템이 올바르게 작동하기 위해 필요한 외부 라이브러리, 모듈, 패키지 및 특정 버전들을 체계적으로 식별, 구성, 설치 및 유지보수하는 프로세스  

### Model 종속성 관리의 필요성  

|필요성|설명|
|---|---|
|재현성<br>Reproducibility|코드가 작동했던 환경을 그대로 복원하여 언제, 어디서든 동일한 결과를 얻도록 보장|
|이식성<br>Portability|모델을 개발 환경에서 프로덕션 환경으로 이동(배포)할 때 문제없이 실행되도록 보장함|
|충돌 방지|프로젝트 간 라이브러리 버전 충돌 등을 방지하기 위한 격리된 환경 구성|


## MLflow 에서의 종속성 관리  

### MLflow 에서 종속성을 관리하는 방법  

- MLflow 에서 Tracking API를 사용해 MLflow 모델을 생성하면, **모델에 필요한 종속성을 자동으로 추론**해 모델 메타데이터의 일부로 기록한다.  
- 이후 기록된 모델을 불러올 때, 모델 전용의 격리된 환경을 자동으로 생성해, 필요한 종속성을 설치하고, 그 환경에서 모델을 실행할 수 있게 해준다.  
- 따라서 **일반적으로는 MLflow 모델에서 종속성 관리에 대해 신경쓸 필요가 없다**.  
- 하지만 경우에 따라 일부 종속성을 추가하거나 수정해야 할 수도 있고, 이때는 본 글을 참고하여 종속성을 관리한다.  

### MLflow 에서 종속성이 기록되는 방식  

```bash
my_model/
├── MLmodel
├── model.pkl
├── conda.yaml
├── python_env.yaml
└── requirements.txt
```

|파일|설명|
|---|---|
|requirements.txt|모델 실행에 필요한 pip 종속성 목록을 정의|
|python_env.yaml|virtualenv를 사용하여 모델 환경을 복원하는 데 필요한 정보를 포함<br>python 버전, 빌드 도구(pip, setuptools, wheel 등), requirements.txt|
|conda.yaml|모델 실행에 필요한 conda 환경을 정의|

- `python_env.yml`  

```yaml
python: 3.9.8
build_dependencies:
  - pip==23.3.2
  - setuptools==69.0.3
  - wheel==0.42.0
dependencies:
  - -r requirements.txt
```

- `requirements.txt`  

```yaml
mlflow==2.9.2
scikit-learn==1.3.2
cloudpickle==3.0.0
```

- `conda.yaml`  

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


### MLflow 모델에 추가 종속성 추가하기  

- `log_model` 메서드의 `extra_pip_requirements` 파라미터에 추가 종속성을 전달한다.  
- 이렇게 전달된 추가 종속성은 requirements.txt 파일에 추가된다.  

```python
import mlflow

class CustomModel(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input):
        # your model depends on pandas
        import pandas as pd
        ...
        return prediction

# Log the model
mlflow.pyfunc.log_model(
    python_model=CustomModel(),
    name="model",
    extra_pip_requirements=["pandas==2.0.3"], # 추가 종속성 라이브러리와 버전
    input_example=input_data,
)
```

### 모든 종속성을 직접 정의하기  

- `log_model` 메서드의 `pip_requirements` 파라미터에 종속성을 정의한다.  
- 이렇게 정의된 종속성은, MLflow가 감지한 기본 종속성을 대체한다.  

```python
import mlflow

# Log the model
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

### 종속성 py 파일 자동 저장하는 `infer_code_paths` 옵션  

- `log_model` 메서드의 `infer_code_paths` 파라미터를 True로 전환하면, 모델이 참조하는 Python 파일을 수집해 모델 안에 포함시킨다.  

- `custom_code.py`  

```python
# custom_code.py
from typing import List
iris_types = ["setosa", "versicolor", "viginica"]

def map_iris_types(predictions: int) -> List[str]:
    return [iris_types[pred] for pred in predictions]
```

- `model.py`  

```python
from typing import Any, Dict, List, Optional
from custom_code import map_iris_types  # import the external reference
import mlflow

class FlowerMapping(mlflow.pyfunc.PythonModel):
    """Custom model with an external dependency"""
    def predict(
        self, context, model_input, params: Optional[Dict[str, Any]] = None
    ) -> List[str]:
        predictions = [pred % 3 for pred in model_input]
        # Call the external function
        return map_iris_types(predictions)

with mlflow.start_run():
    model_info = mlflow.pyfunc.log_model(
        name="flowers",
        python_model=FlowerMapping(),
        infer_code_paths=True,  # True로 하면, 모델(FlowerMapping)이 참조하는 외부 코드의 종속성도 자동으로 추론한다.
    )
```

### 종속성 py 파일을 수동으로 추가하는 `code_path` 옵션  

- `log_model` 메서드의 `code_paths` 파라미터에 종속성 관리가 필요한 코드파일 목록을 정의한다.  
- 그러면 MLflow는 해당 코드파일들을 MLflow 모델 디렉터리의 `code` 디렉터리에 저장한다.  
- 제약사항 : 지정된 파일이나 디렉터리가 모델 스크립트와 같은 디렉터리에 있어야 한다.(상위 또는 하위 디렉터리에 있는 경우 의존성 전이 불가)  
- 이는 커스텀 모델을 사용할 때 특히 유용하다.  

```bash
# 모델 학습/기록(Client) 단의 파일 목록
my_project/
├── utils.py
└── train.py
```

```python
# 모델 학습/기록 코드
import mlflow

class MyModel(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input):
        from utils import my_func
        x = my_func(model_input)
        # .. your prediction logic
        return prediction

# Log the model
with mlflow.start_run() as run:
    mlflow.pyfunc.log_model(
        python_model=MyModel(),
        name="model",
        input_example=input_data,
        code_paths=["utils.py"], # 여기에 추론에 필요한 코드 목록 추가
    )
```

- 그러면 MLflow는 모델 디렉토리의 `code/` 디렉터리에 해당 코드파일들을 저장한다.  

```bash
model/
├── MLmodel
├── ...
└── code/
    └── utils.py
```

### (참고) uv 를 통한 종속성 기록  

- MLflow 2.16.0 부터 종속성을 정확한 버전으로 고정(lock) 하는 방법을 선택할 수도 있다.  
- 종속성 고정을 활성화하려면, 환경 변수 MLFLOW_LOCK_MODEL_DEPENDENCIES를 설정한다.  
- 활성화되면, MLflow 는 `uv`(설치된 경우)를 사용해 모든 종속성을 해결하고 고정한다.  
- uv 설치되어 있지 않으면 lock 기능은 자동 비활성화된다.  

```bash
export MLFLOW_LOCK_MODEL_DEPENDENCIES=true
```

- 고정된 요구 사하은 모델의 requirements.txt 파일에 저장된다.  


[https://mlflow.org/docs/latest/ml/model/dependencies/](https://mlflow.org/docs/latest/ml/model/dependencies/)