import os
import mlflow
from mlflow.tracking import MlflowClient

def process():
    
    server_uri = "http://10.200.0.77:8082"
    
    os.environ["MLFLOW_TRACKING_URI"] = server_uri # 또는 OS환경변수에 등록
    client = MlflowClient()
    experiments = client.get_experiment_by_name("default")
    print(f"MLflow Tracking URI without server url def: {mlflow.get_tracking_uri()}")
    print(f"Experiments List : {experiments}")
    
    server_uri = server_uri
    mlflow.set_tracking_uri(server_uri)
    experiments = client.get_experiment_by_name("default")
    print(f"MLflow Tracking URI with server url def: {mlflow.get_tracking_uri()}")
    print(f"Experiments List : {experiments}")