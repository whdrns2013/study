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
    
    # create experiment
    experiment = MlflowExperiment(mlflow)
    experiment_id, experiment_name = experiment.create_experiment('intent_classifier_artifact_test')
    print(experiment_id, experiment_name)
    mlflow = experiment.set_experiment(experiment_name)
    
    # create run
    run = MlflowRun(mlflow)
    run.start_run(run_name= 'intent_classifier_train')

    # [DEBUG] 단순 아티팩트 저장 테스트
    # print("[DEBUG] 단순 아티팩트 저장을 시도합니다...")
    # try:
    #     mlflow.log_artifact("pyproject.toml", artifact_path="debug_test")
    #     print("[DEBUG] mlflow.log_artifact() 호출 성공! 서버 UI를 확인해보세요.")
    # except Exception as e:
    #     print(f"[DEBUG] mlflow.log_artifact() 호출 실패: {e}")
    # print("\n")
    
    # train and test
    '''
    some train and test actions
    '''
    
    # log parameters
    # parameters = {
    #     'n_neighbors' : 5,
    #     'weights' : 'distance',
    #     'metric' : 'euclidean', 
    #     'n_jobs' : -1
    # }
    n_neighbors_param = common_classes.Param(param_name='n_neighbors', param_value=5)
    weights_param = common_classes.Param(param_name='weights', param_value='distance')
    metric_param = common_classes.Param(param_name='metric', param_value='euclidean')
    n_jobs_param = common_classes.Param(param_name='n_jobs', param_value=-1)
    run.log_params([n_neighbors_param, weights_param, metric_param, n_jobs_param])
    
    # log metrics
    # metrics = {
    #     'accuracy' : 0.98,
    #     'recall' : 0.95,
    #     'precision' : 0.99
    # }
    accuracy_metric = common_classes.Metric(metric='accuracy', score=0.98)
    recall_metric = common_classes.Metric(metric='recall', score=0.95)
    precision_metric = common_classes.Metric(metric='precision', score=0.99)
    run.log_metrics([accuracy_metric, recall_metric, precision_metric])
    
    # dataset
    dataset = pd.read_csv('_sample_model/knn_intent_train_dataset_ko.csv')
    run.log_dataset(dataset)
    
    # log model
    mlflow_model = MlflowModel(mlflow)
    custom_model = IntentClassifierModel()
    model_artifact = common_classes.Artifact(name='model', local_path = '_sample_model/knn.joblib')
    embedding_artifact = common_classes.Artifact(name='embedding', local_path='_sample_model/knn_intent_embeddings.csv')
    artifacts = [model_artifact, embedding_artifact]
    name = 'intent_classifier_model'
    model_name = 'intent_classifier'
    signature = mlflow_model.infer_signature(dataset=dataset, input_cols=['question'], output_cols=['intent'])
    mlflow_model.log_custom_model(
        model = custom_model,
        name = name,
        model_name = model_name,
        artifacts = artifacts,
        signature=signature
    )
    
    # end run
    run.end_run()
