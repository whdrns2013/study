from mlflow_mng.connect import MlflowConnection
from mlflow_mng.experiment import MlflowExperiment
from configparser import ConfigParser

config = ConfigParser()
config.read('core/config.ini')

def process():
    
    # connect
    connection = MlflowConnection()
    server_url = config['mlflow']['protocol.server'] + '://' + config['mlflow']['ip.server'] + ':' + config['mlflow']['port.server']
    mlflow = connection.connect(server_url = server_url)
    
    # create experiment
    experiment = MlflowExperiment(mlflow)
    experiment_id, experiment_name = experiment.create_experiment('create_experiment_test')
    print(experiment_id, experiment_name)
    mlflow = experiment.set_experiment(experiment_name)
    