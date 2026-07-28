
## Backend Store  

### 개념  

- MLflow의 핵심 구성 요소로, Run, Model, Experiment에 대한 메타데이터를 저장한다.  
- 저장하는 데이터는 실행(Run)의 ID, 시작 및 종료 시각, 파라미터, 메트릭(평가지표) 등  
- 주로 구조화된 데이터들이므로 RDB 형태로 저장된다.  
- Model Registry 기능을 사용하려면 RDB 기반 저장소가 필요함  
- ※ 모델 가중치 파일과 같은 대용량 모델 아티팩트는 아티팩트 저장소에 저장됨  

| 저장되는 데이터 | 한글명 | 설명 |
| :--- | :--- | :--- |
| **Run ID** | 실행 식별자 | 각 실험 실행을 구분하는 고유한 UUID.<br>모든 메타데이터와 아티팩트의 기준점이 됨. |
| **Model ID** | 모델 식별자 | 특정 실행 내에서 저장된 모델을 가리키는 ID.<br>모델 레지스트리에 등록될 때 참조됨. |
| **Trace ID** | 추적 식별자 | LLM 추론 과정 등 복잡한 워크플로우의 흐름(Trace)을 추적하기 위한 ID. |
| **Tags** | 태그 | 실행에 부여하는 사용자 정의 키-값 쌍.<br>실험의 목적, 실행자, 환경(운영/개발) 등을 필터링할 때 사용. |
| **Start & end time** | 시작/종료 시각 | 실험이 시작된 시각과 완료된 시각.<br>실험의 소요 시간을 계산하거나 시계열로 정렬할 때 활용. |
| **Parameters** | 매개변수 | 모델 학습에 사용된 하이퍼파라미터(예: Learning Rate, Batch Size).<br>문자열 형태의 키-값 쌍으로 저장. |
| **Metrics** | 측정 기준 | 실험 결과로 도출된 숫자 지표(예: Accuracy, Loss).<br>시간에 따른 변화를 기록하여 그래프로 시각화 가능. |

### 지원되는 Backend Store  

- MLflow는 SQLAlchemy를 통해 이하의 다양한 데이터베이스를 지원한다.  

| 지원되는 Backend Store | 구분 | 설명 |
| :--- | :--- | :--- |
| **sqlite** | RDB | 가볍고 설정이 필요 없는 파일 기반 DB.<br>주로 개인 개발 및 테스트용으로 사용됨.<br>기본값.|
| **postgresql** | RDB | MLflow에서 가장 권장하는 운영용 DB.<br>확장성이 뛰어나고 대규모 트래킹에 적합함. |
| **mysql** | RDB | 널리 사용되는 오픈소스 DB.<br>안정적인 메타데이터 관리가 가능함. |
| **mssql** | RDB | 기업 환경에서 주로 사용되는 SQL Server 지원.<br>SQLAlchemy를 통해 연결됨. |
| **local file system** | file | 서버 없이 `./mlruns` 폴더 내에 JSON/YAML 형태로 저장하는 방식. |

### MLflow Tracking Server 와의 연결  

- Tracking Server에서 백엔드 스토어를 별도 지정하지 않으면 **sqlite** 가 생성되고, 이게 사용됨  
- Tracking Server를 시작할 때 `--backend-store-uri` 옵션을 통해 지정 가능  

```bash
--backend-store-uri postgresql://...
```

## Reference  

[https://mlflow.org/docs/latest/self-hosting/architecture/backend-store/](https://mlflow.org/docs/latest/self-hosting/architecture/backend-store/)  