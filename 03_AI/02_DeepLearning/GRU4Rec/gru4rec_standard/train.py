from numbers import Integral

import numpy as np
import pandas as pd
import torch
from torch.nn import functional as F

from .model import GRU4Rec


def _sample_negatives(targets, num_items, num_negatives):
    '''정답을 제외한 실제 출력 클래스에서 음성 아이템을 균등 추출한다.'''
    draws = torch.randint(0, num_items - 1, (len(targets), num_negatives), device=targets.device)
    return draws + draws.ge(targets[:, None]).long()


def _compute_loss(logits, targets, loss, num_negatives, negative_sampler):
    '''패딩을 포함하지 않는 실제 아이템 점수로 선택한 손실을 계산한다.'''
    if callable(loss):
        result = loss(logits, targets)
    elif loss == 'cross_entropy':
        result = F.cross_entropy(logits, targets)
    else:
        negatives = negative_sampler(targets, logits.shape[1], num_negatives)
        if not isinstance(negatives, torch.Tensor) or negatives.shape != (len(targets), num_negatives):
            raise ValueError('negative_sampler must return a [batch_size, num_negatives] tensor')
        if negatives.dtype != torch.long or negatives.device != logits.device:
            raise ValueError('Negative indices must be torch.long on the logits device')
        if ((negatives < 0) | (negatives >= logits.shape[1]) | negatives.eq(targets[:, None])).any():
            raise ValueError('Negative indices must be valid classes distinct from the target')
        result = F.softplus(logits.gather(1, negatives) - logits.gather(1, targets[:, None])).mean()
    if not isinstance(result, torch.Tensor) or result.ndim != 0 or not torch.isfinite(result):
        raise ValueError('The loss must return a finite scalar Tensor')
    return result


def _build_optimizer(model, optimizer, learning_rate, optimizer_kwargs):
    '''이름 또는 생성 함수와 추가 인자로 optimizer를 구성한다.'''
    choices = {'adam': torch.optim.Adam, 'adamw': torch.optim.AdamW,
               'sgd': torch.optim.SGD, 'adagrad': torch.optim.Adagrad}
    if isinstance(optimizer, str):
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


def _update_model(model, optimizer, total_loss, count, clip_grad_norm):
    '''묶인 시점 또는 윈도우의 평균 손실로 모델을 한 번 갱신한다.'''
    (total_loss / count).backward()
    if clip_grad_norm is not None:
        torch.nn.utils.clip_grad_norm_(model.parameters(), clip_grad_norm)
    optimizer.step()
    optimizer.zero_grad()


def _session_batches(sequences, batch_size, order):
    '''이력별 입력 아이템·수치 특성·정답과 슬롯 교체 여부를 생성한다.'''
    pending = iter(order)
    active = [None] * batch_size
    positions = np.zeros(batch_size, dtype=np.int64)
    while True:
        slots, inputs, features, targets, resets = [], [], [], [], []
        for slot in range(batch_size):
            reset = active[slot] is None
            if reset:
                sequence_index = next(pending, None)
                if sequence_index is None:
                    continue
                active[slot] = sequences[sequence_index]
                positions[slot] = 0
            items, numeric = active[slot]
            position = positions[slot]
            slots.append(slot)
            inputs.append(items[position])
            features.append(numeric[position])
            targets.append(items[position + 1])
            resets.append(reset)
            positions[slot] += 1
            if positions[slot] == len(items) - 1:
                active[slot] = None
        if not slots:
            return
        yield slots, inputs, np.asarray(features, dtype=np.float32), targets, resets


def _window_batches(sequences, batch_size, max_seq_len, use_padding, shuffle, rng):
    '''최근 이력 윈도우를 패딩하거나 길이별로 묶어 학습 배치를 생성한다.'''
    buckets = {}
    for sequence_index, (items, _) in enumerate(sequences):
        for end in range(1, len(items)):
            length = min(end, max_seq_len)
            key = 0 if use_padding else length
            buckets.setdefault(key, []).append((sequence_index, end))
    keys = list(buckets)
    if shuffle:
        rng.shuffle(keys)
    for key in keys:
        samples = buckets[key]
        if shuffle:
            rng.shuffle(samples)
        for start in range(0, len(samples), batch_size):
            batch = samples[start:start + batch_size]
            lengths = np.array([min(end, max_seq_len) for _, end in batch], dtype=np.int64)
            width = int(lengths.max())
            feature_dim = sequences[0][1].shape[1]
            inputs = np.zeros((len(batch), width), dtype=np.int64)
            features = np.zeros((len(batch), width, feature_dim), dtype=np.float32)
            targets = np.empty(len(batch), dtype=np.int64)
            for row, (sequence_index, end) in enumerate(batch):
                items, numeric = sequences[sequence_index]
                length = lengths[row]
                inputs[row, :length] = items[end - length:end]
                features[row, :length] = numeric[end - length:end]
                targets[row] = items[end]
            yield inputs, features, lengths, targets


def _train_session_epoch(model, sequences, optimizer, order, batch_size, bptt_steps,
                         loss, num_negatives, sampler, clip_grad_norm):
    '''이력의 hidden state를 이어받고 지정한 시점 수마다 역전파한다.'''
    device = next(model.parameters()).device
    width = min(batch_size, len(sequences))
    hidden = model.initial_hidden(width)
    optimizer.zero_grad()
    accumulated_loss, accumulated_count, steps = None, 0, 0
    total_loss, total_count = 0.0, 0
    for slots, inputs, features, targets, resets in _session_batches(sequences, width, order):
        indices = torch.tensor(slots, dtype=torch.long, device=device)
        items = torch.tensor(inputs, dtype=torch.long, device=device).unsqueeze(1)
        numeric = torch.as_tensor(features, device=device).unsqueeze(1)
        labels = torch.tensor(targets, dtype=torch.long, device=device) - model.index_offset
        reset_mask = torch.tensor(resets, dtype=torch.bool, device=device)
        selected = hidden.index_select(1, indices) * (~reset_mask)[None, :, None]
        logits, next_hidden = model(items, selected, numeric_features=numeric)
        batch_loss = _compute_loss(logits[:, 0], labels, loss, num_negatives, sampler)
        weighted = batch_loss * len(slots)
        accumulated_loss = weighted if accumulated_loss is None else accumulated_loss + weighted
        accumulated_count += len(slots)
        total_loss += batch_loss.detach().item() * len(slots)
        total_count += len(slots)
        hidden = hidden.index_copy(1, indices, next_hidden)
        steps += 1
        if steps == bptt_steps:
            _update_model(model, optimizer, accumulated_loss, accumulated_count, clip_grad_norm)
            hidden = hidden.detach()
            accumulated_loss, accumulated_count, steps = None, 0, 0
    if accumulated_loss is not None:
        _update_model(model, optimizer, accumulated_loss, accumulated_count, clip_grad_norm)
    return total_loss / total_count


def _train_window_epoch(model, sequences, optimizer, batch_size, max_seq_len, shuffle, rng,
                        loss, num_negatives, sampler, clip_grad_norm):
    '''초기 hidden state에서 각 윈도우 전체를 역전파하여 학습한다.'''
    device = next(model.parameters()).device
    total_loss, total_count = 0.0, 0
    optimizer.zero_grad()
    for inputs, features, lengths, targets in _window_batches(
        sequences, batch_size, max_seq_len, model.use_padding, shuffle, rng,
    ):
        items = torch.as_tensor(inputs, device=device)
        numeric = torch.as_tensor(features, device=device)
        labels = torch.as_tensor(targets, device=device) - model.index_offset
        logits, _ = model(items, numeric_features=numeric, lengths=lengths)
        rows = torch.arange(len(targets), device=device)
        last_positions = torch.as_tensor(lengths - 1, device=device)
        batch_loss = _compute_loss(logits[rows, last_positions], labels, loss, num_negatives, sampler)
        _update_model(model, optimizer, batch_loss * len(targets), len(targets), clip_grad_norm)
        total_loss += batch_loss.detach().item() * len(targets)
        total_count += len(targets)
    return total_loss / total_count


def train(
    events: pd.DataFrame,
    *,
    sequence_col: str = 'SessionId',
    session_col: str | None = None,
    item_col: str = 'ItemId',
    time_col: str = 'Time',
    feature_cols=None,
    training_mode: str = 'session_parallel',
    bptt_steps: int | None = None,
    max_seq_len: int = 20,
    use_padding: bool = False,
    item_catalog=None,
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
    '''선택한 이력·수치 특성·학습 방식으로 GRU4Rec과 매핑을 생성한다.'''
    if session_col is not None:
        if sequence_col != 'SessionId' and sequence_col != session_col:
            raise ValueError('sequence_col and the legacy session_col must agree')
        sequence_col = session_col
    if not isinstance(events, pd.DataFrame):
        raise TypeError('events must be a pandas DataFrame')
    if isinstance(feature_cols, str):
        raise TypeError('feature_cols must be a list of column names, not a string')
    features = list(feature_cols or ())
    columns = [sequence_col, item_col, time_col, *features]
    if len(set(columns)) != len(columns):
        raise ValueError('Sequence, item, time and feature columns must be distinct')
    if not events.columns.is_unique:
        raise ValueError('events must have unique column names')
    missing = [column for column in columns if column not in events.columns]
    if missing:
        raise ValueError(f'Missing event columns: {missing}')
    frame = events[columns].copy()
    if frame.empty or frame.isna().any().any():
        raise ValueError('events must be nonempty and required columns must not contain nulls')
    if features:
        numeric = frame[features].to_numpy(dtype=np.float32)
        if not np.isfinite(numeric).all():
            raise ValueError('Numeric features must be finite and preprocessed before training')
    for name, value in (
        ('embedding_dim', embedding_dim), ('hidden_size', hidden_size), ('num_layers', num_layers),
        ('epochs', epochs), ('batch_size', batch_size), ('num_negatives', num_negatives),
        ('max_seq_len', max_seq_len),
    ):
        if isinstance(value, bool) or not isinstance(value, Integral) or value < 1:
            raise ValueError(f'{name} must be a positive integer')
    if training_mode not in ('session_parallel', 'window'):
        raise ValueError('training_mode must be session_parallel or window')
    if bptt_steps is not None and (isinstance(bptt_steps, bool) or not isinstance(bptt_steps, Integral) or bptt_steps < 1):
        raise ValueError('bptt_steps must be None or a positive integer')
    if training_mode == 'window' and bptt_steps is not None:
        raise ValueError('Window training backpropagates the whole window; leave bptt_steps=None')
    if not isinstance(use_padding, bool) or not isinstance(shuffle_sessions, bool):
        raise TypeError('use_padding and shuffle_sessions must be bools')
    if not 0 <= dropout < 1:
        raise ValueError('dropout must be in [0, 1)')
    if not np.isfinite(learning_rate) or learning_rate <= 0:
        raise ValueError('learning_rate must be finite and positive')
    if clip_grad_norm is not None and (not np.isfinite(clip_grad_norm) or clip_grad_norm <= 0):
        raise ValueError('clip_grad_norm must be None or finite and positive')
    if not callable(loss) and loss not in ('cross_entropy', 'bpr'):
        raise ValueError('loss must be cross_entropy, bpr, or a callable(logits, targets)')
    if negative_sampler is not None and not callable(negative_sampler):
        raise TypeError('negative_sampler must be a callable or None')

    if item_catalog is None:
        item_ids = frame[item_col].unique().tolist()
    else:
        catalog = item_catalog[item_col] if isinstance(item_catalog, pd.DataFrame) else item_catalog
        if isinstance(catalog, (str, bytes)):
            raise TypeError('item_catalog must be a DataFrame or a collection of item IDs')
        catalog = pd.Series(list(catalog))
        if catalog.empty or catalog.isna().any() or catalog.duplicated().any():
            raise ValueError('item_catalog must contain unique non-null item IDs')
        item_ids = catalog.tolist()
    if len(item_ids) < 2:
        raise ValueError('At least two catalog items are required')
    offset = int(use_padding)
    item2idx = {item: index + offset for index, item in enumerate(item_ids)}
    idx2item = {index: item for item, index in item2idx.items()}
    unknown = frame.loc[~frame[item_col].isin(item_ids), item_col].unique().tolist()
    if unknown:
        raise ValueError(f'Event items absent from item_catalog: {unknown}')
    sequences = []
    for _, group in frame.groupby(sequence_col, sort=False, observed=True):
        if len(group) < 2:
            continue
        ordered = group.sort_values(time_col, kind='stable')
        sequences.append((ordered[item_col].map(item2idx).to_numpy(dtype=np.int64),
                          ordered[features].to_numpy(dtype=np.float32)))
    if not sequences:
        raise ValueError('At least one sequence with two events is required')

    torch.manual_seed(random_state)
    rng = np.random.default_rng(random_state)
    target_device = torch.device(device or ('cuda' if torch.cuda.is_available() else 'cpu'))
    model = GRU4Rec(
        len(item_ids), embedding_dim, hidden_size, num_layers, dropout,
        numeric_feature_dim=len(features), use_padding=use_padding, feature_cols=features,
    ).to(target_device)
    model.training_mode = training_mode
    model.max_seq_len = max_seq_len if training_mode == 'window' else None
    model.bptt_steps = (bptt_steps or 1) if training_mode == 'session_parallel' else None
    trainer = _build_optimizer(model, optimizer, learning_rate, optimizer_kwargs)
    sampler = _sample_negatives if negative_sampler is None else negative_sampler
    loss_history = []
    model.train()
    for _ in range(epochs):
        if training_mode == 'session_parallel':
            order = rng.permutation(len(sequences)) if shuffle_sessions else range(len(sequences))
            epoch_loss = _train_session_epoch(
                model, sequences, trainer, order, batch_size, model.bptt_steps,
                loss, num_negatives, sampler, clip_grad_norm,
            )
        else:
            epoch_loss = _train_window_epoch(
                model, sequences, trainer, batch_size, max_seq_len, shuffle_sessions, rng,
                loss, num_negatives, sampler, clip_grad_norm,
            )
        loss_history.append(epoch_loss)
    model.eval()
    return {'model': model, 'item2idx': item2idx, 'idx2item': idx2item,
            'loss_history': loss_history, 'feature_cols': features}
