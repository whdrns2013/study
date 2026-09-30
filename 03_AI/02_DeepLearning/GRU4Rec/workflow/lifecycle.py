"""외부에서 주입한 단계와 순서로 worker 내부 워크플로를 구성한다."""

from collections.abc import Iterable, Mapping, Set
from .workflow import Step, Workflow

class Stage(Step):
    def __init__(self, name, task):
        '''외부에서 이름과 작업을 주입받아 하나의 단계로 묶는다.'''
        if not isinstance(name, str) or not name.strip():
            raise ValueError('Stage name must be a nonempty string')
        if isinstance(task, Workflow):
            steps = list(task.steps)
        elif isinstance(task, Step):
            steps = [task]
        elif callable(task):
            steps = [Step(task)]
        else:
            if not isinstance(task, Iterable) or isinstance(task, (str, bytes, Mapping, Set)):
                raise TypeError('Stage tasks must be a callable, Step, Workflow, or ordered iterable')
            steps = list(task)
            if not all(isinstance(step, Step) or callable(step) for step in steps):
                raise TypeError('Stage subtasks must be Step instances or callables')
            steps = [step if isinstance(step, Step) else Step(step) for step in steps]
        if not all(isinstance(step, Step) for step in steps):
            raise TypeError('Workflow subtasks must be Step instances')
        self.workflow = Workflow(steps)
        super().__init__(self._run, name=name)

    def _run(self, state, config):
        '''같은 컨텍스트로 소단위 스텝을 실행하고 단계의 상태를 반환한다.'''
        return self.workflow.run(state, config, copy_state=False)


def build_worker_workflow(stage_tasks: Mapping | Iterable[Step]) -> Workflow:
    '''주입된 mapping 또는 스텝 목록의 구성과 순서를 그대로 적용한다.'''
    if isinstance(stage_tasks, Mapping):
        return Workflow([Stage(name, task) for name, task in stage_tasks.items()])
    if not isinstance(stage_tasks, Iterable) or isinstance(stage_tasks, (str, bytes, Set)):
        raise TypeError('Workflow tasks must be a mapping or ordered iterable of Steps')
    steps = list(stage_tasks)
    if not all(isinstance(step, Step) for step in steps):
        raise TypeError('Workflow tasks must be Step or Stage instances')
    return Workflow(steps)
