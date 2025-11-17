https://mlflow.org/docs/latest/ml/model/signatures/#understanding-model-signatures

## 모델 시그니처  

### 정의  

- 모델의 입력, 출력 및 매개변수에 대한 형식을 정의한다.  
- 모델이 추론할 때 어떤 input을 기대하고, 무엇을 return 할지를 정확하게 명시하는 계약에 해당한다.  

### 목적  

- 아래와 같은 이점을 얻기 위해 시그니처라는 개념이 생겨났고, 사용됨  

|이점|설명|
|---|---|
|Consistency<br>일관성|모든 모델의 상호작용이 일관적인 데이터 형식을 따르도록 보장한다.|
|Validation<br>유효성 검증|데이터 형식 오류가 모델에 도달하기 전에 미리 포착할 수 있다.|
|Documentation<br>문서화|모델 사용법에 대한 살아있는 문서 역할을 한다.|
|Deployment Safety<br>안전한 배포|MLflow 배포 도구가 요청(추론 요청)을 자동으로 검증할 수 있도록 하는 근거를 제시한다.|
|UI Integration<br>UI 통합|MLflow UI에서 모델의 요구사항으로 명확하게 표시할 수 있는 근거를 제시한다.|

## 시그니처 추가하기  

### 시그니처 추가 방법의 종류  

- 입력 및 출력 데이터 포맷  

|No|방법|설명|
|---|---|---|
|1|input_example을 통한 자동 추론|입력 예시 데이터를 제공해 mlflow가 입출력 스키마를 자동으로 추론하게 한다.<br>개발자는 `input_example` 매개변수에 알맞은 데이터 샘플만 전달하면 된다.| 
|2|명시적 시그니처 객체 생성|개발자가 직접 `signature` 객체를 만들어 전달한다.<br>데이터 구조가 복잡하거나, 자동 추론이 어려운 경우에 적합하다.|
|3|PyFunc 모델의 타입 힌트|`mlflow.pyfunc.PythonModel`을 사용하면서 `predict` 메서드 인수에 타입 힌트를 포함시킴|

### input_example을 통한 자동 추론  

- 방법 : 모델을 기록하는 `log_model` 메서드를 실행시킬 때, `input_example` 인수에 입력 데이터 샘플을 전달한다.  
- 입력된 데이터 샘플을 통해 MLflow가 자동으로 입력 데이터의 유형과 구조를 추론하고, 예시 predict 를 수행해 자동으로 출력 데이터의 유형과 구조 또한 추론한다.  
- 장점 : 코드의 간결성, 명시적으로 복잡한 스키마 객체 작성 필요 없음  
- 장점2 : 모델을 실제로 한 번 실행해서 얻은 결과를 기반으로 output 스키마를 추론(가능한 경우)   
- 장점3 : MLflow는 REST API 엔드포인트에서 사용될 수 있는 형식인 `serving_input_example.json` 파일을 **자동으로 생성**하여 배포 편의성을 높인다.  

```python
import mlflow
# ... model_fit 코드 ...

with mlflow.start_run():
    mlflow.sklearn.log_model(
        model,
        artifact_path="my_model",
        input_example=X_train.iloc[[0]]  # 유효한 입력 데이터(DataFrame)의 한 행을 전달
    )
```

### 명시적 시그니처 객체 생성  

- 방법 : 개발자가 직접 시그니처 객체를 생성해 `log_model` 메서드에 넘겨준다.  
- 여기에서 두 가지 방법이 있다.  

|방법|설명|
|---|---|
|`infer_signature` 함수 사용|`mlflow.models.infer_signature` 함수를 사용해 반자동화 객체 생성|
|`ModelSignature`객체 직접 생성|`Schema`, `ColSpec`, `TensorSpec` 등의 객체를 직접 생성하고 조합해 Signature 객체 생성|

#### infer_signature 함수 사용 방법  

- 방법 : mlflow.models.infer_signature(model_input, model_output) 함수를 사용  
- 장점 : 다음에 나올 직접 스키마 작성 방법보다는 간편하지만, `ModelSignature` 객체를 반환받는 다는 것은 동일함  

```python
from mlflow.models import infer_signature

# 모델 예측을 수행할 입력 및 출력 예시
input_data = X_train.iloc[[0]]
output_data = model.predict(input_data)

# 시그니처 객체 생성
signature = infer_signature(inputs=input_data, outputs=output_data)

with mlflow.start_run():
    mlflow.sklearn.log_model(
        model,
        artifact_path="my_model",
        signature=signature  # 생성된 시그니처 객체를 전달
    )
```

#### ModelSignature 객체 직접 생성 방법  

- 방법 : `Schema`, `ColSpec`, `TensorSpec` 등의 객체를 직접 생성하여 입력, 출력, 매개변수 스키마를 완전 수동으로 정의하고 이를 조합해 `ModelSignature` 객체를 구성  
- 장점 : 가장 유연함. 마음대로 구성할 수 있음.  
- 단점 : 복잡함  

- `ModelSignature` 객체의 주요 구성 요소  

|구성 요소|용도|설명|
|---|---|---|
|`ModelSignature`|시그니처의 최종 객체|아래 구성 요소를 통해 생성한 `inputs`, `outputs`, `params` 스키마를 묶는다.|
|`Schema`|데이터의 논리적 구조 정의|`Colspec` 또는 `TensorSpec` **객체의 리스트**를 포함한다.|
|`ColSpec`|열(Column) 기반 스키마|테이블 형식 데이터(DataFrame)의 열 이름과 유형 세트|
|`TensorSpec`|텐서(Tensor) 기반 스키마|Numpy 배열 등의 데이터 유형과 모양(shape)을 정의한 세트|
|`ParamSchema`|추론 매개변수 정의|추론 시 선택적으로 전달될 매개변수(`temperature`)를 정의|


```python
# 일반적인 머신 러닝 모델 : ColSpec 기반 스키마 작성
from mlflow.models import ModelSignature
from mlflow.types.schema import Schema, ColSpec
from mlflow.types.entities import DataType

# ... 모델(model) 생성 코드는 생략

# 1. 입력 스키마 정의 (ColSpec 사용)
input_schema_ml = Schema([
    ColSpec(DataType.double, "feature_A"),  # 'feature_A'는 실수형 (double)
    ColSpec(DataType.string, "category_B"), # 'category_B'는 문자열형 (string)
    ColSpec(DataType.long, "optional_C", required=False), # 'optional_C'는 정수형 (long)이며 필수가 아님 (required=False)
])

# 2. 출력 스키마 정의 (ColSpec 사용)
output_schema_ml = Schema([
    ColSpec(DataType.double, "prediction") # 'prediction'은 실수형 (double)
])

# 3. ModelSignature 객체 생성
signature_ml = ModelSignature(inputs=input_schema_ml, outputs=output_schema_ml)

with mlflow.start_run():
    mlflow.sklearn.log_model(
        model,
        artifact_path="my_model",
        signature=signature_ml  # 생성된 시그니처 객체를 전달
    )
```

```python
# Tensor 를 사용하는 딥러닝 모델 : TensorSpec 기반 스키마 작성
from mlflow.models import ModelSignature
from mlflow.types.schema import Schema, TensorSpec
import numpy as np
from mlflow.types.entities import DataType

# ... 모델(model) 생성 코드는 생략

# 1. 입력 스키마 정의 (TensorSpec 사용)
input_schema_tensor = Schema([
    TensorSpec(
        dtype=DataType.float32, # 데이터 타입: 32비트 실수 (np.float32)
        shape=(-1, 64, 64, 3),  # 모양 (Shape): [배치 크기, 높이, 너비, 채널] 예시 :: (-1은 배치(Batch) 크기로, '가변적'임을 의미함)
        name="input_image_tensor"
    )
])

# 2. 출력 스키마 정의 (TensorSpec 사용)
output_schema_tensor = Schema([
    TensorSpec(
        dtype=DataType.float32,  # 데이터 타입: 32비트 실수
        shape=(-1, 10), # 모양 (Shape): [배치 크기, 클래스 개수(10)]
        name="output_probabilities"
    )
])

# 3. ModelSignature 객체 생성
signature_tensor = ModelSignature(inputs=input_schema_tensor, outputs=output_schema_tensor)

with mlflow.start_run():
    mlflow.tensorflow.log_model(
        model,
        artifact_path="my_model",
        signature=signature_tensor  # 생성된 시그니처 객체를 전달
    )
```

```python
# 파라미터가 필요한 모델의 경우 (LLM 등) - ParamSchema 추가 사용 필요
from mlflow.models import ModelSignature
from mlflow.types.schema import Schema, ColSpec, ParamSchema, ParamSpec
from mlflow.types.entities import DataType

# ... 모델(model) 생성 코드는 생략

# 1. 입력 스키마 정의
input_schema_llm = Schema([
    ColSpec(DataType.string, "prompt_text") # (단순 텍스트 입력 가정)
])

# 2. 출력 스키마 정의
output_schema_llm = Schema([
    ColSpec(DataType.string, "generated_text") # (단순 텍스트 출력 가정)
])

# --- 3. 매개변수 스키마 (Parameters Schema) 정의 ---
params_schema_llm = ParamSchema([
    ParamSpec("temperature", DataType.double, 0.7), # 'temperature': 실수형, 기본값은 0.7
    ParamSpec("max_tokens", DataType.long, 100),    # 'max_tokens': 정수형, 기본값은 100
    ParamSpec(name="stop_sequences",
              dtype=DataType.string,
              default=[],
              shape=[-1]),    # 'stop_sequences': 문자열 리스트 형태, 기본값은 빈 리스트
])

# 4. ModelSignature 객체 생성 (inputs, outputs, params 모두 전달)
signature_llm = ModelSignature(
    inputs=input_schema_llm, 
    outputs=output_schema_llm, 
    params=params_schema_llm
)

with mlflow.start_run():
    mlflow.openai.log_model(
        model,
        artifact_path="my_model",
        signature=signature_llm  # 생성된 시그니처 객체를 전달
    )
```

### PyFunc 모델의 타입 힌트  

- 방법 : `predict` 함수의 인수에 `typing 모듈`이나 `Pydantic 모델`을 사용  
- 장점 : 코드가 Pythonic 해짐, MLflow 가 타입 힌트를 기반으로 시그니처를 자동 추론, 서빙시 자동으로 입력 데이터 유효성 검사  
- LLM 등에서 복잡하고 중첩된 JSON/딕셔너리 구조를 다룰 때 강력함  

|방법|설명|
|---|---|
|`Pydantic` 모델 사용|Pydantic 을 이용해 스키마 객체를 선언 (권장)|
|`typing` 모듈 사용|파이썬 내장 모듈인 typing 모듈을 이용해 스키마 객체를 선언|

#### Pydantic 모델 사용시  

```python
# 전통적인 머신러닝 모델인 경우 예시
import mlflow.pyfunc
from typing import List
import pydantic

# 1. 모델이 기대하는 정확한 입력 구조 정의
class InputSchema(pydantic.BaseModel):
    name: str
    age: int
    income: int

# 2. 출력 구조도 정의 가능
class OutputSchema(pydantic.BaseModel):
    score: float

# 3. 모델과 predict 정의
# MLflow는 predict 메서드의 인수 타입 힌트 + input_example 을 조합해서 스키마를 추정, 확정한다.
class FinancialModel(mlflow.pyfunc.PythonModel):
    # 입력 힌트: InputSchema 객체의 리스트를 받음 (PyFunc는 항상 배치(Batch) 입력을 기대함)
    def predict(self, context, model_input: List[InputSchema]) -> List[OutputSchema]: # (여기에 실제 모델 추론 로직)
        results = []
        for person in model_input: # Pydantic 덕분에 필드 이름(name, age, income)과 유형이 보장됨
            prediction_score = person.age * 0.1 + person.income * 0.05 
            results.append(OutputSchema(score=prediction_score)) # 출력 힌트: OutputSchema 객체의 리스트를 반환함
        return results

# 4. 모델 로깅
with mlflow.start_run() as run:
    model_info = mlflow.pyfunc.log_model(
        python_model=FinancialModel(),
        artifact_path="financial_scorer",
        input_example=[ # 유형 힌트 기반으로 시그니처가 자동 추론되지만, input_example은 데이터 유효성 검증 및 문서화에 사용됨
            {"name": "Alice", "age": 30, "income": 50000},
            {"name": "Bob", "age": 45, "income": 75000}
        ]
    )
```

```python
# LLM 예시
import mlflow.pyfunc
from typing import List, Optional, Dict
import pydantic

# 1. 모델이 기대하는 정확한 입력 구조 정의
class Message(pydantic.BaseModel):
    role: str
    content: str
    metadata: Optional[Dict[str, str]] = None  # Optional인 경우 선택 필드. 기본값 = None. 입력 안와도 됨.

# 2. 모델과 predict 정의
# MLflow는 predict 메서드의 인수 타입 힌트 + input_example 을 조합해서 스키마를 추정, 확정한다.
class ChatProcessorModel(mlflow.pyfunc.PythonModel):
    # 입력 힌트: InputSchema 객체의 리스트를 받음 (PyFunc는 항상 배치(Batch) 입력을 기대함)
    def predict(self, context, model_input: List[Message]) -> List[str]:
        """
        입력으로 Message 객체의 리스트를 받아, 응답 문자열의 리스트를 반환합니다.
        """
        results = []
        for msg in model_input: # model_input : Pydantic 으로 정의한 Message 의 인스턴스가 담긴 리스트
            role = msg.role.upper()
            content = msg.content
            results.append(f"[{role}]: {content}")
        return results

# 3. 모델 로깅 (시그니처를 명시적으로 전달할 필요 없음)
#    - input_example을 제공하여 Pydantic 모델에 대한 유효성 검사를 수행할 수 있습니다.
with mlflow.start_run():
    mlflow.pyfunc.log_model(
        python_model=ChatProcessorModel(),
        artifact_path="chat_model_pyfunc",
        # 유효성 검사 및 문서화를 위한 입력 예시 (Dict 형태로 전달해도 자동으로 Pydantic으로 변환됨)
        input_example=[
            {"role": "user", "content": "오늘 날씨 어때?"},
            {"role": "system", "content": "답변 생성 시작."}
        ]
    )
```

#### typing 모듈 사용시  

```python
import mlflow
import mlflow.pyfunc
from typing import List, Dict
import pandas as pd
import os

# --- 1. PyFunc 모델 클래스 정의 ---
class TraditionalMLModel(mlflow.pyfunc.PythonModel):
    
    # [핵심] predict 메서드의 인수에 기본 유형 힌트 적용
    # 입력 힌트: Dict[str, float]의 리스트 (예: [{'f1': 1.0, 'f2': 2.0}, ...])
    # 출력 힌트: float의 리스트 (예: [0.5, 0.9, ...])
    def predict(self, context, model_input: List[Dict[str, float]]) -> List[float]:
        """
        입력 딕셔너리 리스트를 받아 예측 점수(float 리스트)를 반환합니다.
        """
        results = []
        for row_dict in model_input: # 입력 데이터는 'typing' 힌트 덕분에 딕셔너리임을 확신할 수 있음
            f1 = row_dict.get('feature_1', 0.0)
            f2 = row_dict.get('feature_2', 0.0)
            f3 = row_dict.get('feature_3', 0.0)
            prediction_score = (f1 * 1.5) + (f2 * 0.5) - (f3 * 0.1) # 예측 로직
            results.append(prediction_score)
        return results

# --- 2. MLflow 로깅 실행 ---
experiment_name = "Typing_Module_Schema_Example"
mlflow.set_experiment(experiment_name)

print(f"MLflow 실험 시작: {experiment_name}")

with mlflow.start_run() as run:
    
    model_info = mlflow.pyfunc.log_model(
        python_model=TraditionalMLModel(),
        artifact_path="traditional_scorer",
        # 유형 힌트 기반으로 시그니처가 자동 추론되며, 
        # input_example은 데이터의 구체적인 컬럼 정보를 제공하고 검증에 사용됨
        input_example=[
            {"feature_1": 10.0, "feature_2": 5.0, "feature_3": 1.0},
            {"feature_1": 12.5, "feature_2": 8.0, "feature_3": 3.0}
        ]
    )
```

[https://mlflow.org/docs/latest/ml/model/signatures/](https://mlflow.org/docs/latest/ml/model/signatures/)