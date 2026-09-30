from numbers import Integral

import pandas as pd
import torch

from .model import GRU4Rec


def predict(
    model: GRU4Rec,
    item_sequence,
    item2idx: dict,
    *,
    top_k: int | None = 10,
    exclude_seen: bool = False,
    score_transform: str = 'raw',
    candidate_items=None,
):
    '''하나의 세션 이력으로 다음 아이템의 추천 순위와 점수를 반환한다.'''
    sequence = list(item_sequence)
    if score_transform not in ('raw', 'softmax', 'sigmoid'):
        raise ValueError('score_transform must be raw, softmax, or sigmoid')
    if not sequence:
        raise ValueError('item_sequence must contain at least one item')
    if top_k is not None and (isinstance(top_k, bool) or not isinstance(top_k, Integral) or top_k < 1):
        raise ValueError('top_k must be a positive integer or None')
    if any(isinstance(index, bool) or not isinstance(index, Integral) for index in item2idx.values()):
        raise ValueError('item2idx values must be integer indices')
    if len(item2idx) != model.num_items or set(item2idx.values()) != set(range(model.num_items)):
        raise ValueError('item2idx must cover all model indices from 0 to num_items - 1')
    unknown = [item for item in sequence if item not in item2idx]
    if unknown:
        raise ValueError(f'Unknown items in item_sequence: {unknown}')
    candidates = list(item2idx) if candidate_items is None else list(dict.fromkeys(candidate_items))
    unknown_candidates = [item for item in candidates if item not in item2idx]
    if unknown_candidates:
        raise ValueError(f'Unknown candidate items: {unknown_candidates}')
    indices = [item2idx[item] for item in sequence]
    device = next(model.parameters()).device
    items = torch.tensor([indices], dtype=torch.long, device=device)
    was_training = model.training
    model.eval()
    try:
        with torch.no_grad():
            logits, _ = model(items)
            values = logits[0, -1]
            if score_transform == 'softmax':
                values = values.softmax(dim=-1)
            elif score_transform == 'sigmoid':
                values = values.sigmoid()
            scores = values.cpu().tolist()
    finally:
        model.train(was_training)
    seen = set(indices) if exclude_seen else set()
    ranked = [(item, scores[item2idx[item]]) for item in candidates if item2idx[item] not in seen]
    result = pd.DataFrame(ranked, columns=['item_id', 'score']).sort_values(
        'score', ascending=False, kind='stable',
    )
    return (result if top_k is None else result.head(top_k)).reset_index(drop=True)
