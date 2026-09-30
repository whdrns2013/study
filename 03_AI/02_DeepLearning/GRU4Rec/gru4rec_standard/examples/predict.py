from gru4rec_standard import predict as standard_predict
from gru4rec_standard.model import GRU4Rec


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
    '''모델·세션 이력·아이템 매핑을 받아 추천 결과 표를 반환한다.'''
    return standard_predict(
        model, item_sequence, item2idx, top_k=top_k, exclude_seen=exclude_seen,
        score_transform=score_transform, candidate_items=candidate_items,
    )


def predict_step(state, config):
    '''workflow 모델과 이력을 일반 예측 함수에 전달하고 결과를 감싼다.'''
    return {'predictions': predict(
        state['model'], state['item_sequence'], state['item2idx'], **config['predict'],
    )}
