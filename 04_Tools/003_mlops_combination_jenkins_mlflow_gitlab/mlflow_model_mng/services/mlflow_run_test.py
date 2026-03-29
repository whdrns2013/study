from mlflow_mng.connect import MlflowConnection
from mlflow_mng.experiment import MlflowExperiment
from mlflow_mng.run import MlflowRun
from configparser import ConfigParser
from mlflow_mng import common_classes
import pandas as pd

config = ConfigParser()
config.read('core/config.ini')

def process():
    
    # connect
    connection = MlflowConnection()
    server_url = config['mlflow']['protocol.server'] + '://' + config['mlflow']['ip.server'] + ':' + config['mlflow']['port.server']
    mlflow = connection.connect(server_url = server_url)
    
    # create experiment
    experiment = MlflowExperiment(mlflow)
    experiment_id, experiment_name = experiment.create_experiment('create_run_test_jh')
    print(experiment_id, experiment_name)
    mlflow = experiment.set_experiment(experiment_name)
    
    # create run
    run = MlflowRun(mlflow)
    run.start_run(run_name= 'create_run_test_run_jh')
    
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
    
    # dataset
    dataset = pd.read_csv('_sample_model/knn_intent_train_dataset_ko.csv')
    run.log_dataset(dataset)
    
    # end run
    run.end_run()