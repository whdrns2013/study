from typing import TypedDict, Annotated
from copy import deepcopy
from collections.abc import Mapping

###############################################
# 핵심 도메인
###############################################
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
        '''주어진 데이터와 설정으로 객체를 초기화한다.
        function : Step에서 수행할 작업이 정의된 함수
        requires : Step이 작업 수행할 때 필요한 input state의 key 목록 (tuple)
        provides : Step이 작업 수행 후 반환할 output state의 key 목록 (tuple)
        '''
        self.function = function
        self.name = name or getattr(function, "__name__", type(function).__name__)
        self.requires = tuple(requires)
        self.provides = tuple(provides)
        self.validate()

    def validate(self):
        if not callable(self.function):
            raise TypeError("Step function must be callable")

    def run(self, state: State, config: Config):
        '''스텝의 입출력 계약을 검증하고 상태 갱신값을 반환한다.'''

        # input 요구사항 충족 확인
        missing = set(self.requires) - state.keys()  
        if missing:
            raise KeyError(f"Step {self.name}: missing state keys {sorted(missing)}")

        # 작업 수행
        update = self.function(state, config)  
        
        # 리턴값 dict 여부 확인
        if not isinstance(update, Mapping):
            raise TypeError(f"Step {self.name} must return a mapping")

        # output 요구사항 충족 확인
        missing = set(self.provides) - update.keys()  
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


###############################################
# 외부 요청 관리
###############################################

class StateDefinition(TypedDict):
    '''외부에서 주입되는 State 정의. key-value 형태'''
    pass

class ConfigDefinition(TypedDict):
    '''외부에서 주입되는 Config 정의. key-value 형태'''
    pass

class StepDefinition(TypedDict):
    '''외부에서 주입되는 Step Input'''
    step_name     :Annotated[str, "스텝의 명칭"]
    function_name :Annotated[str, "스텝이 수행할 작업이 정의된 함수 이름"]
    file_name     :Annotated[str, "function이 포함된 파일 이름"]
    sequence      :Annotated[int, "스텝의 수행 순서"]
    requires      :Annotated[list[str], "필요로 하는 state의 key 집합"]
    provides      :Annotated[list[str], "반환하는 state의 key 집합"]

class RuntimeContext(TypedDict):
    '''요청 컨텍스트 정보'''
    execution_id           : str
    requester_base_url     : str
    log_endpoint           : str
    status_update_endpoint : str
    record_result_endpoint : str


###############################################
# 외부 요청 해석 및 워크플로 수행
###############################################

import io
import contextlib
from urllib.request import Request, urlopen
from urllib.parse import urlencode, urljoin
from typing import Any
import json
import importlib.util
from pathlib import Path
import sys
from uuid import uuid4

class ExecutionReporter:
    '''요청자(요청 서버)에게 진행 상황과 결과를 리포팅'''
    
    def __init__(self, runtime_context:RuntimeContext):
        '''요청 컨텍스트 필요'''
        self.runtime_context = runtime_context
        
    def log(self, message:str):
        '''요청자(요청 서버)에 로깅'''
        rc = self.runtime_context
        url = urljoin(base=rc.get("requester_base_url"), url=rc.get("log_endpoint"))
        data = urlencode({"execution_id":rc.get("execution_id"), "log":message}).encode("utf-8")
        try:
            request = Request(url, data=data, method="POST")
            with urlopen(request, timeout=10) as response:
                response.read()
        except Exception as e:
            print(e)
    
    def update_status(self, status:str):
        '''요청자(요청 서버)에 현재 작업(Execution) 상태 업데이트'''
        rc = self.runtime_context
        url = urljoin(base=rc.get("requester_base_url"), url=rc.get("status_update_endpoint"))
        data = urlencode({"execution_id":rc.get("execution_id"), "status":status}).encode("utf-8")
        try:
            request = Request(url, data=data, method="POST")
            with urlopen(request, timeout=10) as response:
                response.read()
        except Exception as e:
            self.log(f"update status failed. {e}")
    
    def record_result(self, result:Any):
        '''요청자(요청 서버)에 작업 결과를 기록 (직렬화 가능한 데이터만 기록하길 권장)'''
        rc = self.runtime_context
        url = urljoin(base=rc.get("requester_base_url"), url=rc.get("record_result_endpoint"))
        try:
            result = json.dumps(result) if isinstance(result, dict) or isinstance(result, list) else result
            data = urlencode({"execution_id":rc.get("execution_id"), "result":result}).encode("utf-8")
            request = Request(url, data=data, method="POST")
            with urlopen(request, timeout=10) as response:
                response.read()
        except Exception as e:
            self.log(f"record result failed. {e}")


class Orchestrator:
    '''외부 요청을 해석해 워크플로를 구성하고, 일련의 작업을 수행케 하는 클래스'''
    
    def __init__(
        self,
        state_definition: StateDefinition | None = None,
        config_definition: ConfigDefinition | None = None,
        steps_definition: list[StepDefinition] | None = None,
        runtime_context: RuntimeContext | None = None,
        copy_state=True
    ):
        '''초기화'''
        self.validate(state_definition, config_definition, steps_definition, runtime_context)
        
        self.state           = self.build_state(state_definition)
        self.config          = self.build_config(config_definition)
        self.workflow        = self.build_workflow(steps_definition)
        self.runtime_context = self.build_runtime_context(runtime_context)
        self.reporter        = ExecutionReporter(self.runtime_context)
        self.copy_state      = copy_state
    
    def validate(self, state:StateDefinition, config:ConfigDefinition, steps:list[StepDefinition], runtime_context:RuntimeContext):
        '''유효성 판별'''
        missings = []
        missings.append("state") if state is None else None
        missings.append("config") if config is None else None
        missings.append("steps") if steps is None else None
        missings.append("runtime_context") if runtime_context is None else None
            
        if missings:
            raise ValueError(f"Missing fields : {'.'.join(missings)}")

    def build_state(self, state_def:StateDefinition) -> State:
        '''주입된 값을 유지하면서 초기 상태 dict를 만들어 반환한다.'''
        return dict(state_def)

    def build_config(self, config_def:ConfigDefinition) -> Config:
        '''외부에서 주입된 JSON-Like Config를 Config 인스턴스로 생성 후 self.config에 등록'''
        return dict(config_def)

    def build_workflow(self, steps_def:list[StepDefinition]) -> Workflow:
        '''파일에서 진입점 함수를 로드하고, sequence 순으로 Step을 배치하여 워크플로를 구성한다.'''
        steps = []
        modules = {}
        for definition in sorted(steps_def, key=lambda step: step["sequence"]):
            path = Path(definition["file_name"]).resolve(strict=True)
            if path not in modules:
                module_name = f"_workflow_step_{uuid4().hex}"
                spec = importlib.util.spec_from_file_location(module_name, path)
                if spec is None or spec.loader is None:
                    raise ImportError(f"Cannot load step file: {path}")
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                try:
                    spec.loader.exec_module(module)
                except BaseException:
                    sys.modules.pop(module_name, None)
                    raise
                modules[path] = module
            function = getattr(modules[path], definition["function_name"])
            steps.append(Step(
                function,
                name=definition["step_name"],
                requires=definition["requires"],
                provides=definition["provides"],
            ))
        return Workflow(steps)
    
    def build_runtime_context(self, runtime_context_def:RuntimeContext) -> RuntimeContext:
        '''요청자에 대한 정보 등을 포함하는 요청 컨텍스트를 알맞게 등록'''
        return dict(runtime_context_def)
    
    def run(self) -> State:
        '''주입된 워크플로를 실행하고 최종 상태를 반환한다.'''
        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer):
                self.state = self.workflow.run(
                    self.state, self.config, copy_state=self.copy_state
                )
            output = buffer.getvalue()
            self.reporter.log(output)
            self.reporter.update_status("SUCCESS")
            self.reporter.record_result(self.state)
        except Exception as e:
            output = buffer.getvalue()
            self.reporter.log(output)
            self.reporter.update_status("FAIL")
            self.reporter.record_result(e)
        return self.state
