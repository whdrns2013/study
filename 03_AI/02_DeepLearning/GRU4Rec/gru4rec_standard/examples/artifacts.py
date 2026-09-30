import json
from pathlib import Path

import torch


def artifacts(model, item2idx: dict, output_dir, *, evaluation_report=None):
    '''모델 가중치·구조·매핑과 평가 보고서를 예제 파일로 저장한다.'''
    directory = Path(output_dir).resolve()
    directory.mkdir(parents=True, exist_ok=True)
    model_path = directory / 'model.pt'
    report_path = directory / 'evaluation.json'
    parameters = {
        'num_items': model.num_items,
        'embedding_dim': model.item_embedding.embedding_dim,
        'hidden_size': model.gru.hidden_size,
        'num_layers': model.gru.num_layers,
        'dropout': model.output_dropout.p,
        'numeric_feature_dim': model.numeric_feature_dim,
        'use_padding': model.use_padding,
        'feature_cols': list(model.feature_cols),
    }
    torch.save({
        'model_state_dict': {key: value.detach().cpu().clone() for key, value in model.state_dict().items()},
        'model_parameters': parameters,
        'item2idx': dict(item2idx),
        'training_metadata': {
            'training_mode': getattr(model, 'training_mode', None),
            'max_seq_len': getattr(model, 'max_seq_len', None),
            'bptt_steps': getattr(model, 'bptt_steps', None),
        },
    }, model_path)
    report_path.write_text(json.dumps(evaluation_report or {}, indent=2), encoding='utf-8')
    return {'model_uri': str(model_path), 'evaluation_uri': str(report_path)}


def artifacts_step(state, config):
    '''workflow의 학습 결과와 평가 보고서를 예제 아티팩트로 저장한다.'''
    return {'artifact_manifest': artifacts(
        state['model'], state['item2idx'], evaluation_report=state['evaluation_report'],
        **config['artifacts'],
    )}
