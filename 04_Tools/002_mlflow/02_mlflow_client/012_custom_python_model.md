
## MLflow PythonModel Guide  

### MLflow PythonModel  

- `mlflow.pyfunc` 모듈은 `save_model()`과 `log_model()` 함수를 제공한다.  
- 이 함수들은 사용자가 지정한 코드와 파일 의존성을 포함한 `python_function` flavor 모델을 만들 때 사용된다.  
- PythonModel 은 패키징, 배포 등 **MLflow의 기능을 활용하면서 커스텀 모델 로직을 구현할 수 있게** 해준다.  
- PythonModel 정의 방식은 아래 두 가지이다.  

|PythonModel 정의 방식|설명|
|---|---|
|`mlflow.pyfunc.PythonModel` 클래스 상속||
|Callable 단일 함수 정의||

## MLflow PythonModel 작성  

### 1번 방식. mlflow.pyfunc.PythonModel 상속  

1. 모델 클래스 정의 : `mlflow.pyfunc.PythonModel` 클래스를 상속받아 자신의 클래스를 만든다.  
2. 클래스 메서드 구현 : 다음 세 가지 메서드를 구현할 수 있다.  

|메서드|설명|
|---|---|
|`predict`|모델의 예측 로직을 정의한다.|
|`predict_stream`|스트리밍 환경에서 사용 시 구현할 수 있다.|
|`load_context`|모델이 예측 전에 필요한 추가 컨텍스트를 불러오는 데 사용|

> MLflow 2.20.0 이후부터는 context 파라미터가 없어도 된다 (def predict(self, model_input, params) 같은 시그니처도 허용됨)  

```python
# 예시 : 인풋 문자/문자열을 대문자로 변환하여 반환하는 간단한 모델
import mlflow
from typing import List

class MyModel(mlflow.pyfunc.PythonModel):
    # 필요한 경우 모델 초기화 정보나 artifact를 여기서 로드
    # 예: context.artifacts를 사용해 파일을 로드 가능
    def load_context(self, context):
        pass

    # 핵심 예측 로직
    def predict(self, model_input:List[str], params=None):
        return [x.upper() for x in model_input]

```

3. `log_model` 로 모델을 기록할 때에는 `python_model` 파라미터에 모델 클래스를 넘겨준다.  

```python
with mlflow.start_run():
    model_info = mlflow.pyfunc.log_model(
        name="my_class_model",
        python_model=MyModel(),        # 클래스 인스턴스 전달
        input_example=["a", "b", "c"], # signature 자동 추론에 도움
    )
```

4. 저장 후 예측은 일반 PythonModel 과 동일하다.  

```python
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
loaded_model.predict(["hi", "mlflow"])
```


### 2번 방식. Callable 함수로 정의  

1. 함수를 하나 정의해서 `mlflow.pyfunc.log_model()` 에 호출 가능한 함수(callable)로 넘길 수 있다.  

> MLflow 2.20.0 이상에서는 `@pyfunc 데코레이터`를 사용해 타입 힌트를 기반으로 입력 데이터 유효성 검사를 활성화할 수 있다.  

```python
from mlflow.pyfunc.utils import pyfunc

@pyfunc
def predict(model_input: list[str]) -> list[str]:
    return model_input
```

2. `log_model` 로 모델을 기록할 때에는 `python_model` 파라미터에 함수를 넘겨준다.  

```python
import mlflow

with mlflow.start_run():
    model_info = mlflow.pyfunc.log_model(
        name="my_callable_model",
        python_model=predict,      # ← 함수 그대로 전달
        input_example=["a", "b"],
    )
```

3. 저장 후 예측은 일반 PythonModel 과 동일하다.  

```python
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
loaded_model.predict(["hi", "mlflow"])
```

### 모델의 시그니처 등록  

- 모델의 시그니처 등록은 009_signature.md 를 참고한다.  

