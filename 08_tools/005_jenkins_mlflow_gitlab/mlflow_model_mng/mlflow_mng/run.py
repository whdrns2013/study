import mlflow
from typing import Dict, Any

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
    
    def log_params(self, parameters:Dict[str, Any]):
        for param, value in parameters.items():
            self.mlflow.log_param(param, value)
        return self.mlflow
    
    def log_metrics(self, metrics:Dict[str, Any]):
        for metric, score in metrics.items():
            self.mlflow.log_metric(metric, score)
        return self.mlflow
    
    def end_run(self):
        self.mlflow.end_run()
        return self.mlflow