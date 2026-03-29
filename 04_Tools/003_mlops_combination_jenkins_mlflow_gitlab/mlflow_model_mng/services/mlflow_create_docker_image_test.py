import mlflow
from configparser import ConfigParser
from mlflow_mng.model import MlflowModel
from mlflow_mng.deploy import MlflowDeployment

def process():
    config = ConfigParser()
    config.read('core/config.ini')
    server_url = config['mlflow']['protocol.server'] + '://' + config['mlflow']['ip.server'] + ':' + config['mlflow']['port.server']
    mlflow.set_tracking_uri(server_url)
    
    # get model
    mlflow_model = MlflowModel(mlflow)
    model_name_list = mlflow_model.get_model_name_list()
    model_name = model_name_list[0] if model_name_list[0] == 'intent_classifier' else 'intent_classifier'
    
    # get latest model of production version
    production_model_uri = mlflow_model.get_production_latest_version_uri(model_name = model_name)
    docker_image_name = 'intent_classifier'
    mlflow_deployment = MlflowDeployment(mlflow)
    mlflow_deployment.make_docker_image(model_uri=production_model_uri, docker_image_name=docker_image_name)