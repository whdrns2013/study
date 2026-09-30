import pandas as pd
from torch.nn import functional as F

from gru4rec_standard import train as standard_train


def label_smoothed_loss(logits, targets):
    '''라벨 스무딩을 적용한 사용자 정의 손실을 계산한다.'''
    return F.cross_entropy(logits, targets, label_smoothing=0.1)


def train(
    events: pd.DataFrame,
    *,
    session_col: str = 'SessionId',
    item_col: str = 'ItemId',
    time_col: str = 'Time',
    embedding_dim: int = 64,
    hidden_size: int = 128,
    num_layers: int = 1,
    dropout: float = 0.2,
    epochs: int = 10,
    batch_size: int = 128,
    learning_rate: float = 0.001,
    clip_grad_norm: float | None = 5.0,
    loss='cross_entropy',
    num_negatives: int = 1,
    negative_sampler=None,
    optimizer='adam',
    optimizer_kwargs: dict | None = None,
    shuffle_sessions: bool = True,
    random_state: int = 42,
    device: str | None = None,
):
    '''이벤트 표와 명시적인 학습 인자를 받아 표준 GRU4Rec을 학습한다.'''
    selected_loss = label_smoothed_loss if loss == 'label_smoothed' else loss
    return standard_train(
        events, session_col=session_col, item_col=item_col, time_col=time_col,
        embedding_dim=embedding_dim, hidden_size=hidden_size, num_layers=num_layers,
        dropout=dropout, epochs=epochs, batch_size=batch_size, learning_rate=learning_rate,
        clip_grad_norm=clip_grad_norm, loss=selected_loss, num_negatives=num_negatives,
        negative_sampler=negative_sampler, optimizer=optimizer, optimizer_kwargs=optimizer_kwargs,
        shuffle_sessions=shuffle_sessions, random_state=random_state, device=device,
    )


def train_step(state, config):
    '''workflow 이벤트와 설정을 일반 학습 함수에 전달한다.'''
    return train(state['events'], **config['train'])
