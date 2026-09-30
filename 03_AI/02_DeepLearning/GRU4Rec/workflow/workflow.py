from typing import TypedDict
from copy import deepcopy
from collections.abc import Mapping

# Step Function : input is State, output is Dict


class State(TypedDict):
    """Workflow 전체에서 공유하는 작업 Context. Dict 형태이며, 각 Step의 return dict를 부분 업데이트한다."""
    pass


class Config(TypedDict):
    """외부에서 주입받는 설정값 Dict"""
    pass


class Step:
    """Workflow를 구성하는 작은 작업 단위. State와 Config를 받아와서, 작업 결과를 State에 업데이트할 수 있도록 Dict 형태로 반환한다."""

    def __init__(self, function, *, name=None, requires=(), provides=()):
        '''주어진 데이터와 설정으로 객체를 초기화한다.'''
        if not callable(function):
            raise TypeError("Step function must be callable")
        self.function = function
        self.name = name or getattr(function, "__name__", type(function).__name__)
        self.requires = tuple(requires)
        self.provides = tuple(provides)

    def run(self, state: State, config: Config):
        '''스텝의 입출력 계약을 검증하고 상태 갱신값을 반환한다.'''

        missing = set(self.requires) - state.keys()  # input 요구사항 충족 확인
        if missing:
            raise KeyError(f"Step {self.name}: missing state keys {sorted(missing)}")

        update = self.function(state, config)  # 리턴값 dict 여부 확인
        if not isinstance(update, Mapping):
            raise TypeError(f"Step {self.name} must return a mapping")

        missing = set(self.provides) - update.keys()  # output 요구사항 충족 확인
        if missing:
            raise KeyError(f"Step {self.name}: missing output keys {sorted(missing)}")

        return update


class Workflow:
    """하나의 흐름을 가진 작업 묶음. Step들을 가진다."""

    def __init__(self, steps: list[Step]):
        '''순서대로 실행할 소단위 스텝 목록을 저장한다.'''
        self.steps = steps

    def run(self, state: State, config: Config, *, copy_state=True):
        '''스텝을 순차 실행하여 상태 갱신값을 공유 컨텍스트에 병합한다.'''
        # Models and tensors may not support deepcopy. Callers can share their
        # values while keeping the input dictionary isolated.
        state = deepcopy(state) if copy_state else dict(state)
        for step in self.steps:
            update_state = step.run(state, config)
            state.update(update_state)
        return state


class WorkflowExecutor:
    def __init__(
        self, workflow: Workflow, state: State, config: Config, *, copy_state=True
    ):
        '''외부에서 주입한 워크플로/상태/설정을 읽어들여 실행할 수 있는 워크플로를 구성한다.'''
        self.workflow = workflow
        self.state = state
        self.config = config
        self.copy_state = copy_state

    def run(self):
        '''주입된 워크플로를 실행하고 최종 상태를 반환한다.'''
        self.state = self.workflow.run(
            self.state, self.config, copy_state=self.copy_state
        )
        return self.state
