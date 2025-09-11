from mlflow_mng.connect import MlflowConnection
from mlflow_mng.experiment import MlflowExperiment
from mlflow_mng.run import MlflowRun
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
    
    # create run
    run = MlflowRun(mlflow)
    run.start_run()
    
    # log parameters
    parameters = {
        'n_neighbors' : 5,
        'weights' : 'distance',
        'metric' : 'euclidean', 
        'n_jobs' : -1
    }
    run.log_params(parameters)
    
    # log metrics
    metrics = {
        'accuracy' : 0.98,
        'recall' : 0.95,
        'precision' : 0.99
    }
    run.log_metrics(metrics)
    
    # end run
    run.end_run()