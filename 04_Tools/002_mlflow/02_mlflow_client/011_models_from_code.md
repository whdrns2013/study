
## 코드 기반 모델 (Models From Code)  

### 코드 기반 모델의 정의  

- MLflow에서 모델 로직을 이진 파일이 아닌, 읽기 쉬운 Python 스크립트(.py) 형태로 저장하고 관리하는 기능  

### 코드 기반 모델의 장점  

|특징|레거시 방식|코드 기반 모델|
|---|---|---|
|투명성 및 가독성|낮음<br>(모델이 이진파일이기 때문)|높음<br>(모델이 읽을 수 있는 코드 텍스트로 저장됨)|
|디버깅 단순화|낮음<br>(모델이 이진파일이기 때문)|높음<br>(직렬화로 인한 에러 걱정이 줄어듦)|
|더 나은 호환성|낮음<br>(pickle/cloudpickle 등에 종속)|높음<br>(pickle/cloudpickle의 제한을 피함)|
|강화된 보안|낮음<br>(이진 파일이라 사람이 읽고 검증하기 어려움)|향상됨<br>(사람이 읽을 수 있어 검증이 용이함)|

### 코드 기반 모델을 사용하기 위한 핵심 요구사항

#### 1. 스크립트 실행  

- 모델 스크립트는 로그(log) 하는 동안 유효성을 검사함  
- 따라서, 로깅 환경에 외부 종속성이나 인증을 제대로 설정해야 함  

#### 2. Import 관리  

- 상단의 Import 는 실제 사용하는 것만 포함하는 것이 좋음  
- 미사용 Import 가 있는 경우, MLflow가 requirements.txt 에 포함시켜버림  
- 이로 인한 불필요한 종속성 증가는 비효율성을 일으킴  

#### 3. 외부 의존성  

- pip로 설치되지 않는 패키지나 스크립트는 `code_path` 인자를 사용해 명시해야 함.  

#### 4. 보안  

- 코드가 텍스트로 저장되므로, API 키나 비밀번호 등 민감정보는 스크립트에 포함하지 말 것  
- 대신 환경변수 등을 사용하는 것을 권장함  



## Models From Code 작성  

### 권장 프로젝트 디렉터리 구조  

```bash
my_project/
|-- model.py # Defines the custom pyfunc model
|── train.py # Trains and logs the model
|── core/    # Required modules for prediction
|   |── preprocessing.py
|   └── ...
└── helper/  # Other helper modules used for training, evaluation
    |── evaluation.py
    └── ...
```

### 예시  

- 1. 모델 정의  

```python
# basic.py
import pandas as pd
from typing import List, Dict
from mlflow.pyfunc import PythonModel
from mlflow.models import set_model

class BasicModel(PythonModel):
    def exponential(self, numbers):
        return {f"{x}": 2**x for x in numbers}

    def predict(self, context, model_input) -> Dict[str, float]:
        if isinstance(model_input, pd.DataFrame):
            model_input = list(model_input.iloc[0].values())
        return self.exponential(model_input)

set_model(BasicModel())
```

- 2. 모델 로깅  

```python
import mlflow

mlflow.set_experiment("Basic Model From Code")
model_info = mlflow.pyfunc.log_model(
    python_model="basic.py",  # 스크립트 경로
    name="arithmetic_model",
    input_example=[42.0, 24.0],
    infer_code_paths= True,         # 의존 코드파일 자동 추가 옵션
    code_paths=["abc.py", "bcd.py"] # 선택적, 외부 의존성이 있는 경우
)
```

- 3. 모델 로드 및 사용  

```python
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
result = loaded_model.predict([2.2, 3.1, 4.7])
print(result)
```


[https://mlflow.org/docs/latest/ml/model/models-from-code/](https://mlflow.org/docs/latest/ml/model/models-from-code/)