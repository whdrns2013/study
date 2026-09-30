# GRU4Rec 표준 구현

표준 모델·학습·예측은 필요한 값을 명시적인 인자로 받으며 workflow, State, JSON에 의존하지 않습니다. 예제에서만 XXX_step 래퍼로 workflow에 연결합니다. 원본 대학 모델에 실제 적용하는 리팩터링은 별도 작업입니다.

## 구성

- model.py: 아이템 임베딩, 선택적 수치 특성 결합, GRU, 실제 아이템 점수 출력.
- train.py: 입력 검증, 선택적 카탈로그 매핑, 세션 병렬 또는 윈도우 학습.
- predict.py: 아이템 이력과 선택적 수치 특성을 이용한 추천.
- load_data.py/preprocessing.py/evaluation.py/artifacts.py/registration.py: 케이스별 구현용 껍데기.
- examples/: 구체적인 로딩·전처리·학습·예측, 더미 평가·등록, 파일 저장 및 workflow 예시.

## 학습 입력

`train(events, *, sequence_col='SessionId', item_col='ItemId', time_col='Time', feature_cols=None, ...)`

events는 pandas DataFrame이며 한 행은 한 이벤트입니다. sequence_col은 이력을 묶을 키로 세션 ID 또는 사용자 ID 컬럼을 지정합니다. item_col은 실제 아이템 ID, time_col은 이력 안에서 정렬 가능한 시간입니다. 필수 컬럼에 결측값을 허용하지 않습니다. 같은 시간의 이벤트는 입력 순서를 유지합니다. 날짜 문자열은 호출자가 datetime 또는 숫자로 변환합니다. 이전 session_col 인자는 호환용 별칭이며 함께 지정한 sequence_col과 충돌하면 오류입니다.

feature_cols에는 모델에 전달할 수치 특성의 컬럼명 목록을 순서대로 지정합니다. None 또는 빈 목록이면 아이템만 사용합니다. 특성은 외부 전처리에서 생성·결측값 처리·스케일링하고 유한한 수치로 전달합니다. 표준은 특성을 생성하거나 스케일러를 학습하지 않습니다. 모델은 각 입력 시점의 특성과 아이템 임베딩을 결합합니다. 미래 이벤트 및 평가 정답 정보가 특성에 들어가지 않도록 호출자가 분리해야 합니다.

## 학습 방식과 역전파

| 인자 | 의미 |
| --- | --- |
| training_mode='session_parallel' | 각 배치 슬롯에서 이력을 한 시점씩 처리하고 hidden state를 이어받음 |
| training_mode='window' | 각 다음 아이템 정답에 대해 최근 이력 윈도우를 구성하고 초기 hidden state에서 처리 |
| bptt_steps | 세션 병렬에서 optimizer 갱신과 계산 그래프 분리 사이의 배치 시점 수; None이면 1 |
| max_seq_len | 윈도우의 최대 입력 길이; 세션 병렬에서는 이력을 자르지 않음 |
| use_padding | 패딩용 입력 인덱스 예약 및 윈도우 배치 패딩 여부 |

세션 병렬에서 bptt_steps=1은 hidden 값만 이어받고 gradient는 이전 배치로 보내지 않습니다. N이면 최대 N개 배치 시점의 손실을 묶어 역전파합니다. 교체된 이력의 hidden state는 0으로 초기화하므로 이력 경계를 넘어 gradient가 전달되지 않습니다. 각 묶음과 epoch 마지막의 잔여 시점까지 학습합니다. 모든 슬롯은 같은 갱신 경계를 공유하므로 교체 시점에 따라 한 이력의 실제 역전파 길이는 N보다 짧을 수 있습니다.

윈도우는 입력 윈도우 전체를 역전파하며 별도 bptt_steps는 지원하지 않습니다. 반드시 None으로 둡니다. 윈도우마다 초기 hidden state에서 시작하며 최대 길이를 초과한 과거는 제외합니다. use_padding=False이면 같은 실제 길이의 윈도우끼리 배치를 구성합니다. True이면 서로 다른 길이를 오른쪽 패딩으로 묶고 pack_padded_sequence로 패딩을 GRU 계산에서 제외합니다.

use_padding=True인 세션 병렬도 지원하지만 한 시점씩 처리하므로 배치 입력에 채울 패딩은 없습니다. 이 경우에도 인덱스 규칙은 패딩용 0을 예약합니다.

## 인덱스와 카탈로그

item_catalog=None이면 전체 입력 events에서 아이템 목록을 만들고, 지정하면 그 목록으로 매핑합니다. 카탈로그는 item_col을 가진 DataFrame 또는 아이템 ID 목록입니다. 중복·결측값을 허용하지 않으며 이벤트에 등장한 모든 아이템을 포함해야 합니다. 카탈로그에는 최소 2개 아이템이 필요합니다. 길이 1의 이력은 학습 샘플에서는 제외되지만 이벤트에서 만든 매핑에는 해당 아이템이 포함됩니다.

- use_padding=False: 실제 입력 아이템 인덱스는 0부터 N-1.
- use_padding=True: 입력 인덱스 0은 패딩 전용이며 실제 아이템은 1부터 N.
- 두 경우 모두 모델의 출력 클래스는 실제 아이템 N개이며 0부터 N-1.

학습·예측 코드가 입력 인덱스와 출력 클래스 사이의 오프셋을 처리합니다. 패딩은 손실·음성 샘플·추천 후보에 포함하지 않습니다. 사용자 정의 손실과 음성 샘플러는 입력 매핑 인덱스가 아닌 실제 출력 클래스 인덱스 0부터 N-1을 사용합니다. 전체 카탈로그를 매핑해도 미관측 아이템의 선호를 학습하거나 신규 아이템 추천을 해결한 것은 아닙니다.

반환값은 model/item2idx/idx2item/loss_history/feature_cols dict입니다. 모델과 매핑은 학습 후 변경하지 않고 함께 재사용합니다.

## 사용 예

```python
from gru4rec_standard import train, predict

# 기본 GRU4Rec: 세션 병렬, 한 시점 역전파, 수치 특성·패딩 없음
trained = train(events, sequence_col='SessionId', loss='cross_entropy')
recommendations = predict(trained['model'], ['A', 'B'], trained['item2idx'])

# 사용자 이력 윈도우: 수치 특성, 패딩, 별도 아이템 카탈로그
trained = train(
    user_events, sequence_col='USER_ID', item_col='ITEM_ID', time_col='event_time',
    feature_cols=['interest_interval', 'user_count'],
    training_mode='window', max_seq_len=20, bptt_steps=None,
    use_padding=True, item_catalog=items['ITEM_ID'].tolist(), loss='bpr',
)
recommendations = predict(
    trained['model'], history['ITEM_ID'].tolist(), trained['item2idx'],
    numeric_features=history[['interest_interval', 'user_count']],
)
```

위의 사용자 윈도우 구성은 원본 방식의 표현을 지원하지만 원본과 수치적 결과가 동일하다는 보장은 아닙니다. 패딩 계산 제외, 음성 샘플링과 dropout 처리 등의 차이가 있습니다. 실제 원본 리팩터링에서 구체적인 보존 범위를 확정해야 합니다.

## 손실과 optimizer

loss는 cross_entropy, bpr 또는 callable(logits, targets)를 지원합니다. 사용자 손실은 유한한 스칼라 Tensor를 반환해야 합니다. BPR은 softplus(음성 점수 - 양성 점수)의 평균으로 계산하며 BPR-max와 다릅니다. num_negatives로 음성 샘플 수를 지정합니다. negative_sampler(targets, num_items, num_negatives)는 정답과 다른 실제 출력 클래스 인덱스를 [배치 크기, num_negatives] 형태의 long Tensor로 반환해야 합니다. 기본은 균등 복원 추출입니다.

optimizer는 adam/adamw/sgd/adagrad 또는 생성 함수를 지원합니다. optimizer_kwargs로 추가 인자를 전달하고 학습률은 learning_rate로 지정합니다. clip_grad_norm=None이면 clipping을 끕니다. shuffle_sessions는 이력 또는 윈도우 순서를 섞을지 지정합니다.

## 예측 입력

`predict(model, item_sequence, item2idx, *, numeric_features=None, max_seq_len=None, ...)`

item_sequence는 실제 아이템 ID를 시간순으로 나열한 비어 있지 않은 이력입니다. 미등록 아이템은 오류입니다. feature_cols를 사용해 학습했다면 각 이벤트에 대한 numeric_features도 필요합니다. [이력 길이, 수치 특성 개수] 배열 또는 학습과 동일한 컬럼명·순서의 DataFrame을 전달합니다. 학습과 동일한 변환을 적용하고 아이템 이력과 행을 정렬해야 합니다.

윈도우 모델은 저장된 max_seq_len만큼 최근 이력을 사용합니다. 세션 병렬 모델은 기본적으로 전체 전달 이력을 사용합니다. 예측의 max_seq_len으로 길이를 명시할 수 있습니다. 이미 본 아이템 제외는 잘린 이력뿐 아니라 호출자가 전달한 전체 이력을 기준으로 합니다. 각 예측 호출은 초기 hidden state에서 시작합니다.

top_k는 추천 개수이며 None이면 전체 후보를 반환합니다. candidate_items로 후보를 제한할 수 있습니다. score_transform은 raw/softmax/sigmoid입니다. softmax는 전체 실제 카탈로그에 대해 계산하며 후보 제한 후 재정규화하지 않습니다. BPR의 점수를 보정된 확률로 해석하지 않습니다. 반환값은 item_id/score DataFrame입니다.

예제 아티팩트는 모델 생성 인자와 특성 순서 및 학습 메타데이터를 저장합니다. 복원 시 model_parameters로 모델을 생성하고 state_dict를 로딩한 뒤 training_metadata의 max_seq_len 등을 모델에 다시 설정해야 합니다.

이 구현은 간결한 공통 코드이며 공식 GRU4Rec의 전체 최적화 옵션을 재현하지 않습니다. 모든 아이템의 점수를 계산하므로 큰 카탈로그에서는 연산과 메모리 비용이 증가합니다. [확장 예제](examples/README.md)에 실행 방법을 정리했습니다. 별도 요청 전까지 테스트와 학습은 실행하지 않습니다.
