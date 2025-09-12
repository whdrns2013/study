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
    latest_version = mlflow_model.get_latest_version(model_name)
    
    # staging
    ## production
    mlflow_deployment = MlflowDeployment(mlflow)
    new_stage = 'Production'
    mlflow_deployment.stage(model_name = model_name, model_version = 16, new_stage = new_stage)
    ## staging
    new_stage = 'Staging'
    mlflow_deployment.stage(model_name = model_name, model_version = 15, new_stage = new_stage)
    
    
    # get latest version of staging model / production model / archived model
    staging_model_uri = mlflow_model.get_staged_latest_version_uri(model_name = model_name)
    production_model_uri = mlflow_model.get_production_latest_version_uri(model_name = model_name)
    archived_model_uri = mlflow_model.get_archived_latest_version_uri(model_name = model_name)
    print(f'staging_model_uri : {staging_model_uri}')
    print(f'production_model_uri : {production_model_uri}')
    print(f'archived_model_uri : {archived_model_uri}')