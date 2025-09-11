import mlflow
from configparser import ConfigParser

def process():
    config = ConfigParser()
    config.read('core/config.ini')
    server_url = config['mlflow']['protocol.server'] + '://' + config['mlflow']['ip.server'] + ':' + config['mlflow']['port.server']
    mlflow.set_tracking_uri(server_url)
    print(f"MLflow Tracking URI: {mlflow.get_tracking_uri()}")