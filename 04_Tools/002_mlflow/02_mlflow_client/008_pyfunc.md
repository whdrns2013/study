## MLflow PyFunc  

### 정의  

> 모든 Flavor 들의 부모 클래스, 인터페이스이자  
> Custom Flavor를 만들 수 있게 해주는 인터페이스  

![](/images/model_save_and_load.png)  

MLflow는 TensorFlow나 Scikit-learn 같은 특정 모델을 저장하고 관리하는 Flavor 라는 기능(Named Flavors)이 있다. 하지만 **만약 MLflow가 지원하지 않는 독특한 모델**이나, 모델에 복잡한 전처리/후처리 로직을 추가하고 싶다면 어떻게 해야 할까?  

이때 필요한 것이 바로 **PyFunc (Python Function)**다. PyFunc는 모델을 **표준화된 Python 클래스** 형태로 감싸서, 어떤 복잡한 로직이나 프레임워크로 만들어진 모델이라도 MLflow 안에서 하나의 **통일된 모델처럼 작동하게 만드는** 만능 인터페이스다.  

다시 정리하면 모든 Flavor들이 어떻게 구성되고, 어떻게 행동해야 하는지를 정의한 **가장 기본적으고 표준적인 Flavor이자 Flavor 인터페이스** 이다.  

### 역할  

#### 공통된 인터페이스    

PyFunc는 **모든 MLflow Python 모델이 따르는 공통된 인터페이스 역할**을 한다. MLflow가 내장 지원하는 모든 라이브러리 모델(예: Scikit-learn, H2O, ONNX)을 저장할 때, MLflow는 자동으로 이 모델에 PyFunc (python_function) Flavor를 추가한다.  

이를 통해 어떤 복잡한 라이브러리로 모델을 만들었든지 상관없이, 배포 환경에서는 `mlflow.pyfunc.load_model()` 함수를 사용해 해당 모델을 단순한 Python 함수처럼 불러와서 일관되게 예측을 수행할 수 있는 것이다.  

#### 커스텀 Flavor   

PyFunc는 단순히 기존 모델을 감싸는 역할뿐 아니라, **MLflow가 공식적으로 지원하지 않는 라이브러리의 모델을 통합할 때**나, **모델에 사용자 정의 코드(예: 예측 전 데이터 전처리 또는 후처리)를 추가**할 때에도 사용할 수 있다. PyFunc가 Flavor의 인터페이스이기 때문이다. (즉, 이러한 경우는 `PyFunc` 를 상속받아 Custom Flavor를 만든다고 생각하면 된다.)  


### 사용하는 이유  

#### 유연성 (Flexibility)  

MLflow가 기본 지원하지 않는 새로운 프레임워크나 모델, 혹은 개발자가 직접 만든 모델에도 적용할 수 있다.  

#### 통일된 인터페이스 (Unified Interface)  

PyFunc를 사용하면 일관된 API를 얻을 수 있다. 모델이 이 인터페이스를 준수하면, 환경에 대한 걱정 없이 MLflow의 모든 배포 도구를 활용할 수 있다. (=통일된 방식으로 사용할 수 있다.)  

#### 커스텀 로직 추가 (Custom Logic)  

PyFunc 는 모델 그 자체를 넘어서, 전처리와 후처리리 등 복잡한 비즈니스 로직을 자유롭게 추가할 수 있다.  


### PyFunc 의 구성 요소  

#### 1. Python Function Flavor  

MLflow Python 모델의 기본 모델 인터페이스다. 모든 MLflow Python 모델이 일관된 API를 사용하여 로드되고 상호 작용할 수 있도록 보장한다.  

#### 2. Filesystem Format  

필요한 모든 데이터, 코드 및 구성을 포함하는 구조화된 디렉토리로, 캡슐화된 모델과 그 종속성이 자체 포함되고 재현 가능하도록 보장한다.  

#### 3. MLModel Configuration  

필수적인 설명자인 `MLmodel` 파일은 로더 모듈, 코드, 데이터 및 환경을 포함하여 모델에 대한 세부 정보를 제공한다.  

#### 4. Custom Pyfunc Models  

Named Flavor를 넘어서는 강력한 기능으로, 커스텀 로직, 데이터 변환 등을 가진 모델 생성을 허용한다.  

