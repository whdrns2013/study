
## Flavor  

![](/images/flavor.png)  

### 정의  

> MLflow에서 다양한 모델을 다루는 일관된 규격(Wrapper)  

Flavor는 MLflow에서 어떤 머신러닝 모델을 다루는 방법을 표준화해주는 틀 또는 규격(Wrapper) 라고 이해할 수 있다.  

다시 말해, 어떤 머신러닝 라이브러리로 모델을 만들었든 상관 없이, MLflow 환경에서는 똑같은 방식으로 저장하고, 불러오고, 배포할 수 있도록 하는 **표준화된 포장지(Wrapper)**인 것이다.  

### 역할  

> MLflow에서 여러 유형의 모델을 "일관된 방법"으로 다룰 수 있게 해주는 역할  

예를 들어 `Spark ML` 라이브러리로 모델을 만든다고 해보자. `Pipeline` 모델, `로지스틱 회귀` 모델 등 여러 종류의 모이 존재한다. 이 모델들은 내부 구조가 제각각이라, 배포할 때마다 다르게 처리해야 하는 복잡함이 생길 수 있다.  

이 때 MLflow에서는, 이 모든 모델을 단순히 **Spark ML Flavor**라는 하나의 우산 아래에 넣고 관리한다. 즉, 추상화를 하는 것이다. 이러한 추상화 덕분에 모델 내부 구조나 유형에 상관 없이 모델을 저장하고, 불러오고, 배포할 수 있는 것이다.  


### 표준화  

> Flavor의 역할을 한 단어로 정의한다면 "표준화" 일 것이다.  

표준화란, "모두가 따르는 규칙을 정의하는 것"으로 풀어 말할 수 있다. Flavor는 각 라이브러리가 모델을 저장하고 불러오는 고유한 방식(직렬화와 역직렬화)를 알아서 처리해준다. 사용자(개발자)는 이 복잡한 과정을 하나 하나 알 필요 없이, Flavor를 통해 모델 저장/로드 과정을 매우 간단하게 처리할 수 있다.  

### Flavor의 종류  

| Flavor | 설명 |
| :--- | :--- |
| `mlflow.pyfunc` | Python 함수 모델의 일반적인 형태.<br>다른 플레이버가 범용 Python 환경에서 로드될 수 있도록 지원하는 가장 유연하고 핵심적인 플레이버 |
| `mlflow.sklearn` | Scikit-learn 모델용 플레이버.<br>로깅, 로드 및 배포 지원 |
| `mlflow.pytorch` | PyTorch 모델용 플레이버<br> PyTorch의 모델 및 상태를 저장하고 로드 가능 |
| `mlflow.tensorflow` | TensorFlow 및 Keras 모델용 플레이버.<br>SavedModel 형식을 포함한 TensorFlow의 모델 관리 지원 |
| `mlflow.xgboost` | XGBoost 모델용 플레이버.<br>XGBoost 모델의 구조와 가중치를 효율적으로 관리 |
| `mlflow.lightgbm` | LightGBM 모델용 플레이버.<br>LightGBM 모델 객체의 로깅 및 로드 지원 |
| `mlflow.statsmodels` | Statsmodels 라이브러리의 통계 모델용 플레이버 |
| `mlflow.prophet` | Prophet (Facebook) 시계열 예측 모델용 플레이버 |
| `mlflow.h2o` | H2O.ai 플랫폼의 모델용 플레이버 |
| `mlflow.spark` | Apache Spark MLlib의 모델용 플레이버 |
| `mlflow.openai` | OpenAI LLM 및 API를 사용하는 모델 및 애플리케이션 추적 및 로깅 지원 |
| `mlflow.transformers` | Hugging Face Transformers 모델용 플레이버.<br>대규모 언어 모델(LLM) 로깅에 유용 |
| `mlflow.langchain` | LangChain 에이전트 및 애플리케이션의 로깅 및 관리 지원 |
| `mlflow.dspy` | DSPy 프레임워크로 구축된 LLM 파이프라인의 로깅 지원 |
| `mlflow.llama_index` | LlamaIndex 애플리케이션의 로깅 지원 |
| `mlflow.fastai` | FastAI 모델용 플레이버 |
| `mlflow.spacy` | spaCy NLP 모델용 플레이버 |
| `mlflow.catboost` | CatBoost 모델용 플레이버 |
| `mlflow.gluon` | Gluon 모델용 플레이버 |
| `mlflow.onnx` | ONNX (Open Neural Network Exchange) 형식으로 내보낸 모델용 플레이버 |
| `mlflow.pmdarima` | PMDARIMA (Auto-ARIMA) 시계열 모델용 플레이버 |
| `mlflow.keras` | (TensorFlow에 포함) Keras 모델의 관리 지원 |
| `mlflow.diviner` | Diviner (Uber) 시계열 모델용 플레이버 |

### Named Flavor  

Named Flavor (명명된 Flavor) 는 MLflow에서 특정 머신러닝 라이브러리나 프레임워크를 위해 미리 정의된 표준 포장(wrapper) 형식이다.  


### 코드 상에서 flavor  

- 이 모델을 어떤 방식으로 로드할 수 있는지를 정의한 딕셔너리 형태의 데이터.  
- MLflow 모델은 보통 여러 flavor를 동시에 포함할 수 있다.  
- 필수 요건 (1) JSON 직렬화가 가능해야 한다. -> MLmodel 파일로 저장되기 때문  
- 필수 요건 (2) `loader_module` 필드가 존재해야 함 : 해당 flavor를 로드하는 Python 모듈  

```json
// flavor 예시 1 : pyfunc (범용 API)
{
  "python_function": { // flavor 이름
    "loader_module": "mlflow.pyfunc", // 모델을 로드할 모듈 이름
    "python_version": "3.9.0", // 모델을 실행시킬 수 있는 파이썬 버전
    "data": "model.pkl", // 모델이 저장될 때 파일 이름
    "env": "conda.yaml" // 모델을 실행시킬 수 있는 가상환경이 명세된 파일 이름
  }
}
```

```json
// flavor 예시 2 : sklearn
{
  "sklearn": {
    "sklearn_version": "1.2.2", // scikit-learn 라이브러리 버전
    "serialization_format": "cloudpickle", // 직렬화 형태
    "data": "model.pkl",
    "loader_module": "mlflow.sklearn"
  }
}
```

```json
// flavor 예시 3 : pytorch
{
  "pytorch": {
    "pytorch_version": "2.0.0",
    "data": "model.pth",
    "loader_module": "mlflow.pytorch",
    "code": null
  }
}
```

```json
// flavor 예시 4 : 사용자 정의 모델
{
  "my_custom_flavor": {
    "loader_module": "my_project.custom_loader",
    "my_field_1": "value",
    "my_field_2": 123
  }
}

```


## Reference  

[https://mlflow.org/docs/latest/ml/traditional-ml/tutorials/creating-custom-pyfunc/part1-named-flavors/](https://mlflow.org/docs/latest/ml/traditional-ml/tutorials/creating-custom-pyfunc/part1-named-flavors/)  
[https://mlflow.org/docs/latest/ml/model/#models_built-in-model-flavors](https://mlflow.org/docs/latest/ml/model/#models_built-in-model-flavors)  


