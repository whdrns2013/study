import mlflow

class MlflowConnection():
    
    def __init__(self, server_url:str=None):
        self.server_url = server_url
    
    def connect(self, server_url:str=None):
        if server_url is not None:
            mlflow.set_tracking_uri(server_url)
        else:
            mlflow.set_tracking_uri(self.server_url)
        return mlflow
