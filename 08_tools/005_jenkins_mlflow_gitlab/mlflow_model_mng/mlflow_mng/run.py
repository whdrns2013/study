import mlflow
from typing import Dict, Any, List
from mlflow_mng import common_classes

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
    
    def log_params(self, parameters:List[common_classes.TrainParam]):
        for param_set in parameters:
            self.mlflow.log_param(param_set.param_name, param_set.param_value)
        return self.mlflow
    
    def log_metrics(self, metrics:List[common_classes.Metric]):
        for metric in metrics:
            self.mlflow.log_metric(metric.metric, metric.score)
        return self.mlflow
    
    def end_run(self):
        self.mlflow.end_run()
        return self.mlflow