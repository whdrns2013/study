# GRU4Rec 기본 구현

세션 기반 다음 아이템 추천을 위한 독립적인 PyTorch 구현입니다. 모델 코드는 workflow, State, JSON을 참조하지 않습니다. 윤경애 수석 모델 코드에 적용하는 작업은 별도로 진행합니다.

## 파일

- model.py: 아이템 임베딩, GRU, 아이템 점수 출력.
- train.py: 입력 확인, 아이템 매핑, 세션 병렬 학습.
- predict.py: 한 세션 이력으로 다음 아이템 순위 예측.
- load_data.py: 데이터 로딩 더미 함수 load_data.
- preprocessing.py: 전처리 더미 함수 data_preprocessing.
- evaluation.py: 평가 더미 함수 evaluation.
- artifacts.py: 아티팩트 더미 함수 artifacts.
- registration.py: 등록 더미 함수 registration.
- examples/: workflow 연결 함수 및 config_definition/state_definition JSON 예시.

## 학습 입력

`train(events, *, session_col='SessionId', item_col='ItemId', time_col='Time', ...)`

events는 아래 세 컬럼을 가진 pandas DataFrame입니다. 컬럼명은 함수 인자로 변경할 수 있습니다. 추가 컬럼은 사용하지 않습니다.

| 컬럼 | 의미 | 조건 |
| --- | --- | --- |
| SessionId | 독립된 세션 식별자 | 결측값이 없고 그룹화 가능한 값 |
| ItemId | 실제 아이템 ID | 결측값이 없고 해시 가능한 값 |
| Time | 세션 안에서 이벤트 순서를 정하는 시간 | 결측값이 없고 정렬 가능한 값 |

한 행은 한 이벤트입니다. 사용자 ID는 필요하지 않습니다. 세션 구분은 호출자가 결정합니다. 날짜 문자열은 전처리에서 datetime 또는 숫자로 변환해야 합니다. 시간값이 같은 이벤트는 입력 행 순서를 유지합니다. 사용자 이력을 하나의 세션으로 취급하려면 호출자가 명시적으로 해당 세션 ID를 부여합니다.

길이 1인 세션은 학습에서 제외됩니다. 길이 2 이상인 세션이 하나 이상 있어야 하며, 해당 세션들에 서로 다른 아이템이 2개 이상 있어야 합니다. 아이템 매핑은 학습 코드가 0부터 생성합니다. 패딩을 사용하지 않으므로 인덱스 0도 실제 아이템입니다.

나머지 인자는 모델 구조(embedding_dim/hidden_size/num_layers/dropout), 학습 설정(epochs/batch_size/learning_rate/clip_grad_norm), 시드(random_state), 장치(device)입니다. 기본값과 타입은 train.py의 시그니처에 명시합니다.

반환값은 model/item2idx/idx2item/loss_history를 가진 dict입니다. JSON이나 State 클래스 없이 직접 사용할 수 있습니다.

```python
import pandas as pd
from gru4rec_standard import train, predict

events = pd.DataFrame({
    'SessionId': [1, 1, 1, 2, 2],
    'ItemId': ['A', 'B', 'C', 'B', 'A'],
    'Time': [1, 2, 3, 1, 2],
})
result = train(events, epochs=10, batch_size=128)
recommendations = predict(
    result['model'], ['A', 'B'], result['item2idx'], top_k=10,
)
```

## 예측 입력

`predict(model, item_sequence, item2idx, *, top_k=10, exclude_seen=False, score_transform='raw', candidate_items=None)`

item_sequence는 하나의 세션에 속한 실제 아이템 ID를 시간순으로 나열한 비어 있지 않은 이력입니다. model과 item2idx는 같은 학습 결과에서 가져옵니다. 학습하지 않은 아이템은 오류로 처리합니다. 매 호출마다 초기 hidden state에서 시작합니다.

반환값은 item_id/score 컬럼을 가진 순위순 DataFrame입니다. score_transform은 raw(원점수), softmax, sigmoid 중 선택합니다. softmax는 전체 학습 아이템을 대상으로 계산하며 후보 제한이나 기존 아이템 제외 후 재정규화하지 않습니다. BPR 점수를 확률로 해석하지 않습니다. exclude_seen은 이미 본 아이템을 제외합니다. candidate_items로 후보를 제한할 수 있고 기본값은 전체 학습 아이템입니다. top_k=None이면 모든 후보를 반환합니다.

## 선택 가능한 학습 방식

| 인자 | 선택 |
| --- | --- |
| loss | cross_entropy, bpr 또는 callable(logits, targets) |
| num_negatives | BPR의 정답당 음성 샘플 수; 기본 1 |
| negative_sampler | BPR용 callable(targets, num_items, num_negatives); 기본은 정답 제외 균등 복원 추출 |
| optimizer | adam, adamw, sgd, adagrad 또는 optimizer 생성 함수 |
| optimizer_kwargs | weight_decay, momentum 등 optimizer별 인자 |
| shuffle_sessions | 매 epoch 세션 순서를 섞을지 선택 |
| clip_grad_norm | gradient clipping 임계값; None이면 비활성화 |

사용자 손실 함수는 스칼라 Tensor를 반환해야 하며 음성 샘플링이 필요하면 함수 안에서 담당합니다. negative_sampler는 BPR에서만 사용하며 [배치 크기, num_negatives] 형태의 long Tensor를 점수와 동일한 장치에 반환해야 합니다. 음성은 유효한 인덱스이며 해당 정답과 달라야 합니다. BPR은 softplus(음성 점수 - 양성 점수)의 평균으로 계산합니다. 기존 sigmoid 차이에 대한 BPR을 수치적으로 안정되게 계산하는 방식이며 BPR-max와는 다릅니다.

optimizer 생성 함수는 parameters, lr 및 optimizer_kwargs를 받아 PyTorch optimizer를 반환해야 합니다. 함수 주입은 Python API에서 수행하고 JSON 예시에는 문자열 선택과 직렬화 가능한 인자만 넣습니다.

```python
result = train(events, loss='bpr', num_negatives=5,
               optimizer='adamw', optimizer_kwargs={'weight_decay': 0.01})
recommendations = predict(result['model'], ['A', 'B'], result['item2idx'],
                          score_transform='raw')
```

## 학습 방식과 범위

각 배치 슬롯이 한 세션을 순서대로 처리하며 세션이 끝나면 다음 세션으로 교체하고 해당 hidden state를 0으로 초기화합니다. 이벤트 사이에서는 hidden 값을 이어받고 계산 그래프는 분리하여 한 시점씩 학습합니다. 마지막에 남은 세션도 학습합니다. 기본 손실은 전체 아이템에 대한 cross-entropy이며 BPR 또는 외부 손실 함수로 교체할 수 있습니다.

이 구현은 GRU4Rec의 세션 병렬 학습을 사용하는 간결한 기본형입니다. 공식 구현의 sampled softmax, BPR-max, 추가 음성 샘플링, 최적화 옵션 전체를 재현하지 않습니다. 전체 카탈로그 점수를 계산하므로 아이템 수가 큰 데이터에서는 메모리와 연산량이 증가합니다. 수치 특성 결합은 케이스별 확장으로 남겨두었습니다.

설계 참고: [공식 GRU4Rec PyTorch 구현](https://github.com/hidasib/GRU4Rec_PyTorch_Official).

examples의 JSON은 workflow 연결 예시이며 필수 설정 파일이 아닙니다. 예제도 load_data.py/preprocessing.py/train.py/predict.py로 나누고 일반 함수는 경로·DataFrame·모델 등 필요한 입력을 명시적으로 받습니다. workflow 연결은 별도의 XXX_step(state, config) 래퍼에서만 처리합니다. 사용자 300명, 세션 3,000개, 아이템 100개, 클릭 34,143건의 가상 데이터를 포함합니다. 핵심 코드의 실행 순서는 외부에서 결정합니다. JSON 없이 직접 사용하는 방법과 workflow 연결 방법은 [확장 예제 설명](examples/README.md)에 정리했습니다.

테스트는 별도 요청 전까지 실행하지 않습니다.
