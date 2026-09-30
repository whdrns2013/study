# GRU4Rec 확장 예제

일반 함수는 필요한 입력을 명시적으로 받고 결과를 직접 반환합니다. workflow의 state/config 처리와 갱신 dict 포장은 같은 파일의 XXX_step 래퍼에서만 수행합니다.

| 파일 | 일반 함수 | 예제 동작 | workflow 래퍼 |
| --- | --- | --- | --- |
| load_data.py | load_data(csv_path, *, user_col, item_col) | 원천 CSV를 DataFrame으로 로딩 | load_data_step |
| preprocessing.py | data_preprocessing(raw_data, *, user_col, item_col, time_col, session_gap_minutes) | 사용자 클릭을 세션별 학습 이벤트로 변환 | preprocessing_step |
| train.py | train(events, *, 모델·학습 인자) | 표준 GRU4Rec 학습을 재사용 | train_step |
| predict.py | predict(model, item_sequence, item2idx, *, 예측 인자) | 표준 예측을 재사용 | predict_step |
| evaluation.py | evaluation(model, events, item2idx, *, top_k) | 모델·이벤트 규모를 요약한 더미 보고서 | evaluation_step |
| artifacts.py | artifacts(model, item2idx, output_dir, *, evaluation_report) | 가중치·모델 구조·매핑·보고서를 파일로 저장 | artifacts_step |
| registration.py | registration(model_uri, model_name, *, registry_path) | 로컬 JSON에 더미 등록 기록 추가 | registration_step |

evaluation은 성능 평가를 구현한 것이 아닙니다. 실제 Recall/MRR 등의 값은 만들지 않으며 metrics는 빈 dict입니다. registration은 외부 모델 레지스트리에 연결하지 않고 dummy_registered 상태를 가진 로컬 기록을 남깁니다. artifacts는 실제 파일을 저장합니다.

## 일반 함수 사용

```python
from gru4rec_standard.examples.load_data import load_data
from gru4rec_standard.examples.preprocessing import data_preprocessing
from gru4rec_standard.examples.train import train
from gru4rec_standard.examples.predict import predict
from gru4rec_standard.examples.evaluation import evaluation
from gru4rec_standard.examples.artifacts import artifacts
from gru4rec_standard.examples.registration import registration

raw_data = load_data('gru4rec_standard/examples/data/clicks.csv')
events = data_preprocessing(raw_data, session_gap_minutes=30)
trained = train(events, loss='bpr', num_negatives=3, epochs=2, device='cpu')
recommendations = predict(trained['model'], ['A', 'B'], trained['item2idx'])
report = evaluation(trained['model'], events, trained['item2idx'], top_k=10)
manifest = artifacts(trained['model'], trained['item2idx'], 'output', evaluation_report=report)
record = registration(manifest['model_uri'], 'clickstream-gru4rec', registry_path='output/registrations.json')
```

학습 입력은 SessionId/ItemId/Time 이벤트 표이고 예측 입력은 실제 아이템 ID를 순서대로 나열한 한 세션 이력입니다. train의 모델·학습 옵션은 함수 시그니처에 명시했습니다. loss='label_smoothed'는 예제 손실 함수를 표준 train에 주입합니다.

## 수치 특성과 사용자 윈도우로 확장

전처리는 UserId, GapMinutes, SequencePosition도 생성합니다. GapMinutes는 같은 세션의 직전 클릭과의 시간 간격이며 세션 시작은 0입니다. SequencePosition은 세션 안에서 현재까지의 이벤트 위치입니다. 두 특성은 미래를 집계하지 않으며 기본 설정의 feature_cols=[]에서는 사용하지 않습니다. 이 예제는 스케일러를 학습하지 않습니다. 실제 데이터의 특성 생성과 스케일링은 케이스별 전처리에서 수행해야 합니다.

```python
feature_cols = ['GapMinutes', 'SequencePosition']
catalog = events['ItemId'].drop_duplicates().tolist() + ['NEW_ITEM']
trained = train(
    events, sequence_col='UserId', training_mode='window', max_seq_len=20,
    bptt_steps=None, use_padding=True, feature_cols=feature_cols,
    item_catalog=catalog, loss='bpr', epochs=2,
)
history = events.loc[events['SessionId'].eq(events['SessionId'].iloc[0])].sort_values('Time')
recommendations = predict(
    trained['model'], history['ItemId'].tolist(), trained['item2idx'],
    numeric_features=history[feature_cols],
)
```

NEW_ITEM은 매핑만 추가한 미관측 아이템이며 이 설정만으로 선호를 학습하지 않습니다. 패딩이 켜지면 입력 인덱스는 1부터, 꺼지면 0부터입니다. 출력 점수에는 항상 실제 아이템만 포함합니다.

workflow에서 같은 구성을 사용하려면 config의 train에 sequence_col/training_mode/use_padding/feature_cols를 지정하고, window 모드에서는 bptt_steps를 null로 바꿉니다. item_catalog는 config의 train에 목록으로 지정하거나 state에 런타임 표 또는 목록을 주입합니다. predict_step은 state의 numeric_features를 전달하므로 수치 특성을 사용할 때는 item_sequence와 행·컬럼 순서가 일치하는 행렬을 함께 주입해야 합니다. 예를 들어 item_sequence=["A", "B"]에 feature_cols=["GapMinutes", "SequencePosition"]이라면 numeric_features=[[0, 0], [3, 1]]처럼 실제 이력의 값을 전달합니다. 해당 수치 특성 모델에서 이 입력을 생략하면 오류입니다.

세션 병렬에서 bptt_steps=N은 N개 배치 시점의 손실을 묶어 역전파합니다. 모델과 매핑의 인덱스 규칙을 학습 후 변경하지 않습니다. 아티팩트에는 수치 특성 차원·컬럼 순서·패딩 여부와 윈도우 길이 등도 저장합니다.

## 예제 실행

프로젝트 루트에서 실행합니다.

```powershell
.venv/Scripts/python.exe -m gru4rec_standard.examples.run_example
```

run_example.py에는 main() 진입점만 있습니다. direct/workflow 모드와 CLI 옵션은 제거했습니다. main은 config_definition.json/state_definition.json/steps_definition.json을 읽고, 명세의 file_name/function_name으로 함수를 로드하여 sequence 순서대로 Workflow를 실행합니다. 함수 선택용 레지스트리는 두지 않습니다. 현재 Orchestrator의 build_* 메서드는 수정하지 않았습니다.

예시 순서는 로딩 → 전처리 → 학습 → 예측 → 평가 → 아티팩트 → 등록입니다. 이 목록은 steps_definition.json에 있으며 runner에 고정하지 않았습니다. 순서나 구성 변경 시 각 스텝의 입력 의존성을 충족하도록 상태를 준비해야 합니다.

각 스텝 명세의 requires에는 실행 전에 필요한 최상위 state 키를, provides에는 해당 스텝의 반환 dict가 포함해야 하는 키를 명시합니다. config 키는 이 목록에 넣지 않습니다. runner가 두 목록을 Step에 전달하므로 기존 Step.run이 실행 전 입력 키와 실행 후 반환 키를 검증합니다. 예를 들어 predict는 초기 상태의 item_sequence와 학습 결과의 model/item2idx를 요구하고 predictions를 반환합니다.

데이터·출력 경로의 상대 경로는 examples 디렉터리를 기준으로, 스텝 파일의 상대 경로는 프로젝트 루트를 기준으로 해석합니다. 이 규칙은 예제 runner에만 적용합니다. 모델 파일과 평가 보고서는 examples/output/model.pt와 examples/output/evaluation.json에 저장되고 재실행하면 덮어씁니다. 등록 기록은 examples/output/registrations.json에 추가됩니다. 이 폴더는 gitignore에 포함했습니다.

손실·optimizer 등의 변경은 config_definition.json의 train 항목에서 수행합니다. 기본 학습은 CPU, 2 epoch입니다. 일반 함수는 JSON을 참조하지 않으며 래퍼가 읽은 설정을 인자로 전달합니다.

## 데이터

가상 로그에는 사용자 300명, 세션 3,000개, 아이템 100개, 이벤트 34,143건이 있습니다. 사용자 선호와 반복 클릭, 세션별 3~20개 이벤트를 포함합니다. 아이템은 A/B/C/D와 P005부터 P100까지입니다. 기본 전처리는 사용자 변경 또는 직전 클릭과 30분을 초과하는 간격을 새 세션으로 처리합니다.

데이터 재생성 스크립트는 학습 없이 사용할 수 있습니다.

```powershell
python gru4rec_standard/examples/generate_data.py
python gru4rec_standard/examples/generate_data.py --users 1000 --sessions-per-user 20 --items 200
```

이번 변경에서는 예제 실행·학습·테스트를 수행하지 않았습니다.
