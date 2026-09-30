import importlib.util
import json
from pathlib import Path

from workflow import Step, Workflow


def main():
    '''예시 정의 파일의 스텝과 실행 순서로 workflow를 구성하고 실행한다.'''
    directory = Path(__file__).resolve().parent
    project_root = directory.parent.parent
    config = json.loads((directory / 'config_definition.json').read_text(encoding='utf-8'))
    state = json.loads((directory / 'state_definition.json').read_text(encoding='utf-8'))
    definitions = json.loads((directory / 'steps_definition.json').read_text(encoding='utf-8'))

    for section, key in [('load_data', 'csv_path'), ('artifacts', 'output_dir'),
                         ('registration', 'registry_path')]:
        path = Path(config[section][key])
        config[section][key] = str(path if path.is_absolute() else directory / path)

    steps = []
    for definition in sorted(definitions, key=lambda entry: entry['sequence']):
        path = Path(definition['file_name'])
        path = path if path.is_absolute() else project_root / path
        spec = importlib.util.spec_from_file_location(definition['step_name'], path)
        if spec is None or spec.loader is None:
            raise ImportError(f'Cannot load step file: {path}')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        function = getattr(module, definition['function_name'])
        steps.append(Step(
            function,
            name=definition['step_name'],
            requires=definition['requires'],
            provides=definition['provides'],
        ))

    result = Workflow(steps).run(state, config, copy_state=False)
    print(result['predictions'].to_string(index=False))
    print(json.dumps(result['evaluation_report'], indent=2))
    print(json.dumps(result['artifact_manifest'], indent=2))
    print(json.dumps(result['registration'], indent=2))


if __name__ == '__main__':
    main()
