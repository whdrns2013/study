import mlflow

class MlflowExperiment():
    
    def __init__(self, mlflow_connection:mlflow):
        self.mlflow = mlflow_connection
    
    # 실험 존재 여부 체크
    def is_exist(self, experiment_name):
        experiment = self.mlflow.get_experiment_by_name(experiment_name)
        return experiment
    
    # 실험 생성
    def create_experiment(self, experiment_name):
        experiment = self.is_exist(experiment_name)
        if experiment is None:
            experiment_id = self.mlflow.create_experiment(experiment_name)
            print(f"'{experiment_name}' 실험을 새로 만들었습니다. (ID: {experiment_id})")
        else:
            experiment_id = experiment.experiment_id
            print(f"'{experiment_name}' 실험이 이미 존재합니다. (ID: {experiment_id})")
        return experiment_id, experiment_name
    
    # 현재 mlflow connection 에 실험 세팅
    def set_experiment(self, experiment_name):
        self.mlflow.set_experiment(experiment_name)
        return self.mlflow