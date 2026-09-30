import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def registration(model_uri: str, model_name: str, *, registry_path):
    '''저장된 모델의 위치와 이름을 로컬 JSON에 더미 등록한다.'''
    if not Path(model_uri).is_file():
        raise FileNotFoundError(model_uri)
    target = Path(registry_path).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    records = json.loads(target.read_text(encoding='utf-8')) if target.exists() else []
    entry = {
        'status': 'dummy_registered',
        'registration_id': str(uuid4()),
        'model_name': model_name,
        'model_uri': model_uri,
        'registered_at': datetime.now(timezone.utc).isoformat(),
    }
    records.append(entry)
    target.write_text(json.dumps(records, indent=2), encoding='utf-8')
    return dict(entry, registry_path=str(target))


def registration_step(state, config):
    '''workflow의 모델 파일 위치를 로컬 더미 등록 함수에 전달한다.'''
    return {'registration': registration(
        state['artifact_manifest']['model_uri'], **config['registration'],
    )}
