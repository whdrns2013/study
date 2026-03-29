
## Tracking 이란  

### Trainking?  

- 이전 connect 코드를 보면 `set_tracking_uri` 라는 메서드를 사용하는 것을 볼 수 있다.  
- tracking_uri 즉, 트래킹이란 것의 URI를 뜻하는데 이게 뭘까?  

### 개념  

- Tracking은 머신러닝 "실험"의 파라미터, 메트릭, 코드 버전, 아티팩트(모델, 이미지 등)와 같은 정보를 기록하고 관리하는 기능이다.  
- 이를 통해 실험 결과를 체계적으로 저장하고, 여러 실험을 비교하거나 재현할 수 있다.  
- 또한 나중에 UI를 통해  실험 결과를 시각화하거나, 검색하거나, 비교할 수도 있다.  
- 실험을 기록하는 방법은 두 가지로, API를 통한 기록과, UI를 통한 기록이 있다.  
- 이번 study에서는 "API"를 통한 기록만을 다룰 것이다.  

### set_tracking_uri  

- Tracking 서버 URI를 설정한다.  
- uri는 빈 문자열 또는 로컬 파일 경로, 혹은 HTTP URI, Batabricks 작업공간이나 pathlib.Path일 수 있다.  
- 나의 경우 보통 HTTP URI를 사용할 것이다.  

```python
mlflow.config.set_tracking_uri(uri)
# e.g. mlflow.config.set_tracking_uri("http://10.200.0.77:8082")
```

## Runs  

### 개념  

- **코드 한 번의 실행, 즉 한 번의 프로세스**를 의미한다.  
- MLflow 에서 중심이 되는, 그리고 가장 기본의 단위.  
- 예를 들어, 학습 코드 실행 한 번, 평가 코드 실행 한 번... 등을 의미한다.  
- 각각의 Run은 아래의 요소들을 포함한다.  

|포함 요소|설명|
|---|---|
|파라미터<br>Parameter|**추후 추가**|
|메트릭<br>Metric|**추후 추가**|
|아티팩트<br>Artifact|**추후 추가**|
|태그<br>Tag|**추후 추가**|
|시작시간|**추후 추가**|
|종료시간|**추후 추가**|

## Models  

### 개념  

- `runs` 도중 생산된 "학습된 머신 러닝 아티팩트"를 가리킨다.  
- 기록된 모델(logged model) 은 자체 메타데이터와 아티팩트를 포함한다.  


## Experiment  

### 개념  

- Experiment는 특정한 목적이나 작업을 위한 여러 개의 runs를 묶은 그룹이다.  
- 쉽게 말하면, 관련된 다수의 runs들을 그룹화하는 것, 또는 그 그룹을 의미하는 것이다.  
- 일반적으로는 특정 문제나 프로젝트에 대한 일련의 시도를 묶는 데 사용된다.  
- e.g. A 라는 모델의 성능 개선을 위한 여러 번의 Run 묶음  
- e.g. 집갑 예측을 위한 선형 회귀 모델 학습 Run, 랜덤 포레스트 학습 Run .. 등을 묶은 것  



## Reference  

https://mlflow.org/docs/latest/ml/tracking/  
https://mlflow.org/docs/latest/api_reference/python_api/mlflow.config.html#mlflow.config.set_tracking_uri  