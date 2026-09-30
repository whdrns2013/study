def evaluation(model, events, item2idx: dict, *, top_k: int = 10):
    '''예제 모델과 이벤트의 규모를 요약하는 더미 평가 보고서를 반환한다.'''
    sizes = events.groupby('SessionId', sort=False).size()
    return {
        'status': 'dummy_evaluation',
        'event_count': len(events),
        'session_count': len(sizes),
        'next_item_pairs': int((sizes - 1).clip(lower=0).sum()),
        'model_item_count': model.num_items,
        'mapping_item_count': len(item2idx),
        'top_k': top_k,
        'metrics': {},
    }


def evaluation_step(state, config):
    '''workflow의 모델과 이벤트를 더미 평가 함수에 전달한다.'''
    return {'evaluation_report': evaluation(
        state['model'], state['events'], state['item2idx'], **config['evaluation'],
    )}
