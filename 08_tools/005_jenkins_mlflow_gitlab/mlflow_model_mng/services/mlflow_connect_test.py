import mlflow
from configparser import ConfigParser
import os

def process():
    
    # 1. 환경변수에 연결할 server_url 을 등록해놓으면 자동으로 가져와서 연결함
    os.environ['MLFLOW_TRACKING_URI'] = 'http://mock_mlflow'
    print(f"MLflow Tracking URI without server url def: {mlflow.get_tracking_uri()}")
    
    # 2. 명시적으로 server_url 을 부여하기
    config = ConfigParser()
    config.read('core/config.ini')
    server_url = config['mlflow']['protocol.server'] + '://' + config['mlflow']['ip.server'] + ':' + config['mlflow']['port.server']
    mlflow.set_tracking_uri(server_url)
    print(f"MLflow Tracking URI with server url def: {mlflow.get_tracking_uri()}")