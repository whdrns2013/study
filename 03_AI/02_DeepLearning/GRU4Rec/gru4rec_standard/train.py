from numbers import Integral

import numpy as np
import pandas as pd
import torch
from torch.nn import functional as F

from .model import GRU4Rec


def _sample_negatives(targets, num_items, num_negatives):
    '''정답을 제외한 아이템을 균등 분포에서 복원 추출한다.'''
    draws = torch.randint(0, num_items - 1, (len(targets), num_negatives), device=targets.device)
    return draws + draws.ge(targets[:, None]).long()


def _compute_loss(logits, targets, loss, num_negatives, negative_sampler):
    '''선택한 손실 함수로 아이템 점수와 정답의 학습 손실을 계산한다.'''
    if callable(loss):
        return loss(logits, targets)
    if loss == 'cross_entropy':
        return F.cross_entropy(logits, targets)
    negatives = negative_sampler(targets, logits.shape[1], num_negatives)
    if not isinstance(negatives, torch.Tensor) or negatives.shape != (len(targets), num_negatives):
        raise ValueError('negative_sampler must return a [batch_size, num_negatives] tensor')
    if negatives.dtype != torch.long or negatives.device != logits.device:
        raise ValueError('Negative indices must be torch.long on the logits device')
    if ((negatives < 0) | (negatives >= logits.shape[1]) | negatives.eq(targets[:, None])).any():
        raise ValueError('Negative indices must be valid items distinct from the target')
    positives = logits.gather(1, targets[:, None])
    negative_scores = logits.gather(1, negatives)
    return F.softplus(negative_scores - positives).mean()


def _build_optimizer(model, optimizer, learning_rate, optimizer_kwargs):
    '''지정한 이름 또는 생성 함수로 optimizer를 생성한다.'''
    if isinstance(optimizer, str):
        choices = {'adam': torch.optim.Adam, 'adamw': torch.optim.AdamW,
                   'sgd': torch.optim.SGD, 'adagrad': torch.optim.Adagrad}
        if optimizer not in choices:
            raise ValueError(f'Unsupported optimizer: {optimizer}')
        factory = choices[optimizer]
    elif callable(optimizer):
        factory = optimizer
    else:
        raise TypeError('optimizer must be a supported name or a factory')
    options = dict(optimizer_kwargs or {})
    if 'lr' in options:
        raise ValueError('Use learning_rate instead of optimizer_kwargs["lr"]')
    return factory(model.parameters(), lr=learning_rate, **options)


def _session_batches(sessions, batch_size, order):
    '''세션별 순서를 유지하며 입력·정답·교체 여부를 병렬 배치로 생성한다.'''
    pending = iter(order)
    active = [None] * batch_size
    positions = np.zeros(batch_size, dtype=np.int64)
    while True:
        slots, inputs, targets, resets = [], [], [], []
        for slot in range(batch_size):
            reset = active[slot] is None
            if reset:
                session_index = next(pending, None)
                if session_index is None:
                    continue
                active[slot] = sessions[session_index]
                positions[slot] = 0
            sequence = active[slot]
            position = positions[slot]
            slots.append(slot)
            inputs.append(sequence[position])
            targets.append(sequence[position + 1])
            resets.append(reset)
            positions[slot] += 1
            if positions[slot] == len(sequence) - 1:
                active[slot] = None
        if not slots:
            return
        yield slots, inputs, targets, resets


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
    '''세션 이벤트를 병렬로 학습하여 모델·아이템 매핑·손실 이력을 반환한다.'''
    if not isinstance(events, pd.DataFrame):
        raise TypeError('events must be a pandas DataFrame')
    columns = [session_col, item_col, time_col]
    if len(set(columns)) != 3:
        raise ValueError('session_col, item_col and time_col must be distinct')
    if not events.columns.is_unique:
        raise ValueError('events must have unique column names')
    missing = [column for column in columns if column not in events.columns]
    if missing:
        raise ValueError(f'Missing event columns: {missing}')
    frame = events[columns].copy()
    if frame.empty or frame.isna().any().any():
        raise ValueError('events must be nonempty and required columns must not contain nulls')
    for name, value in (
        ('embedding_dim', embedding_dim), ('hidden_size', hidden_size),
        ('num_layers', num_layers), ('epochs', epochs), ('batch_size', batch_size),
    ):
        if isinstance(value, bool) or not isinstance(value, Integral) or value < 1:
            raise ValueError(f'{name} must be a positive integer')
    if not 0 <= dropout < 1:
        raise ValueError('dropout must be in [0, 1)')
    if not np.isfinite(learning_rate) or learning_rate <= 0:
        raise ValueError('learning_rate must be finite and positive')
    if clip_grad_norm is not None and (not np.isfinite(clip_grad_norm) or clip_grad_norm <= 0):
        raise ValueError('clip_grad_norm must be None or finite and positive')
    if not callable(loss) and loss not in ('cross_entropy', 'bpr'):
        raise ValueError('loss must be cross_entropy, bpr, or a callable(logits, targets)')
    if isinstance(num_negatives, bool) or not isinstance(num_negatives, Integral) or num_negatives < 1:
        raise ValueError('num_negatives must be a positive integer')
    if negative_sampler is not None and not callable(negative_sampler):
        raise TypeError('negative_sampler must be a callable or None')
    if not isinstance(shuffle_sessions, bool):
        raise TypeError('shuffle_sessions must be a bool')
    sampler = _sample_negatives if negative_sampler is None else negative_sampler

    # One-event sessions have no next-item training target.
    lengths = frame.groupby(session_col, sort=False, observed=True)[item_col].transform('size')
    frame = frame.loc[lengths.ge(2)]
    if frame.empty:
        raise ValueError('At least one session with two events is required')
    item_ids = frame[item_col].unique().tolist()
    if len(item_ids) < 2:
        raise ValueError('At least two distinct training items are required')
    item2idx = {item: index for index, item in enumerate(item_ids)}
    idx2item = dict(enumerate(item_ids))
    sessions = [
        group.sort_values(time_col, kind='stable')[item_col].map(item2idx).to_numpy(dtype=np.int64)
        for _, group in frame.groupby(session_col, sort=False, observed=True)
    ]
    torch.manual_seed(random_state)
    rng = np.random.default_rng(random_state)
    target_device = torch.device(device or ('cuda' if torch.cuda.is_available() else 'cpu'))
    model = GRU4Rec(len(item_ids), embedding_dim, hidden_size, num_layers, dropout).to(target_device)
    trainer = _build_optimizer(model, optimizer, learning_rate, optimizer_kwargs)
    loss_history = []
    width = min(batch_size, len(sessions))
    model.train()
    for _ in range(epochs):
        hidden = model.initial_hidden(width)
        total_loss, total_examples = 0.0, 0
        order = rng.permutation(len(sessions)) if shuffle_sessions else range(len(sessions))
        for slots, inputs, targets, resets in _session_batches(sessions, width, order):
            slot_tensor = torch.tensor(slots, dtype=torch.long, device=target_device)
            items = torch.tensor(inputs, dtype=torch.long, device=target_device).unsqueeze(1)
            labels = torch.tensor(targets, dtype=torch.long, device=target_device)
            reset_mask = torch.tensor(resets, dtype=torch.bool, device=target_device)
            selected_hidden = hidden[:, slot_tensor].detach().clone()
            selected_hidden[:, reset_mask] = 0
            trainer.zero_grad()
            logits, next_hidden = model(items, selected_hidden)
            batch_loss = _compute_loss(logits[:, 0], labels, loss, num_negatives, sampler)
            batch_loss.backward()
            if clip_grad_norm is not None:
                torch.nn.utils.clip_grad_norm_(model.parameters(), clip_grad_norm)
            trainer.step()
            hidden = hidden.detach().index_copy(1, slot_tensor, next_hidden.detach())
            total_loss += batch_loss.item() * len(slots)
            total_examples += len(slots)
        loss_history.append(total_loss / total_examples)
    model.eval()
    return {
        'model': model,
        'item2idx': item2idx,
        'idx2item': idx2item,
        'loss_history': loss_history,
    }
