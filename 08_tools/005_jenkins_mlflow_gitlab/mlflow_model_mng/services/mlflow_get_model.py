from mlflow_mng.connect import MlflowConnection
from mlflow_mng.experiment import MlflowExperiment
from mlflow_mng.run import MlflowRun
from mlflow_mng.model import MlflowModel
from configparser import ConfigParser
from mlflow_mng import common_classes
from custom_model.intent_classifier import IntentClassifierModel
import joblib
import pandas as pd

config = ConfigParser()
config.read('core/config.ini')

def process():
    
    # connect
    connection = MlflowConnection()
    server_url = config['mlflow']['protocol.server'] + '://' + config['mlflow']['ip.server'] + ':' + config['mlflow']['port.server']
    mlflow = connection.connect(server_url = server_url)
    
    # model name list
    mlflow_model = MlflowModel(mlflow)
    model_name_list = mlflow_model.get_model_name_list()
    print('========== model name list ==========\n', model_name_list)
    
    # uri of model's latest version
    mlflow_model = MlflowModel(mlflow)
    model_name = model_name_list[0] if model_name_list[0] == 'intent_classifier' else 'intent_classifier'
    latest_version_model_uri = mlflow_model.get_latest_version(model_name = model_name)
    print('========== models latest version uri ==========\n', latest_version_model_uri)