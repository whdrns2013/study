import mlflow
from typing import List, Union, Dict, Any
from mlflow_mng import common_classes
import pandas as pd

class MlflowRun():
    
    def __init__(self, mlflow:mlflow):
        self.mlflow = mlflow
        self.run = None
    
    def start_run(self, run_name:str=None):
        if run_name is not None:
            run = self.mlflow.start_run(run_name = run_name)
        else:
            run = self.mlflow.start_run()
        run_id = run.info.run_id
        self.run = run
        self.run_id = run_id
        return run_id, run
    
    def log_params(self, parameters:Union[Dict[str,Any], List[common_classes.Param]]):
        '''doc
        parameters : 직접 dict 형식으로 입력해도 되고, List 형식으로 입력해도 됨.
        '''
        if isinstance(parameters, List):
            for param_set in parameters:
                self.mlflow.log_param(param_set.param_name, param_set.param_value)
        elif isinstance(parameters, Dict):
            for parameter, value in parameters.items():
                self.mlflow.log_param(parameter, value)
        else:
            raise TypeError('type error')
        return self.mlflow
    
    def log_metrics(self, metrics:List[common_classes.Metric]):
        '''doc
        metrics : 직접 dict 형식으로 입력해도 되고, List 형식으로 입력해도 됨.
        '''
        if isinstance(metrics, List):
            for metric in metrics:
                self.mlflow.log_metric(metric.metric, metric.score)
        elif isinstance(metrics, Dict):
            for metric, score in metrics.items():
                self.mlflow.log_metric(metric, score)
        else:
            raise TypeError('type error')
        return self.mlflow
    
    def log_dataset(self, dataset:pd.DataFrame, source:str='', context:str=''):
        '''doc
        dataset : 데이터셋. 데이터셋의 형태는 판다스 데이터프레임.
        source : 데이터셋 저장 경로.
        context : 맥락. 이 데이터셋의 맥락을 의미한다. 예를 들어 학습용 / 평가용 / 검증용 등이 있다.
        '''
        dataset = mlflow.data.from_pandas(dataset, source=source)
        self.mlflow.log_input(dataset, context=context)
        return self.mlflow
    
    def end_run(self):
        self.mlflow.end_run()
        return self.mlflow