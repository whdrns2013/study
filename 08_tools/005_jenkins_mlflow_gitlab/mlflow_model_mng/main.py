from services import mlflow_connect_test, mlflow_experiment_test, mlflow_run_test, mlflow_model_regist, mlflow_get_model, predict_test, mlflow_staging_test, mlflow_create_docker_image_test

def main():
    # 아래 단계를 하나씩 테스트해보면 됩니다.
    mlflow_connect_test.process()
    # mlflow_experiment_test.process()
    # mlflow_run_test.process()
    # mlflow_model_regist.process()
    # mlflow_get_model.process()
    # predict_test.process()
    # mlflow_staging_test.process()
    # mlflow_create_docker_image_test.process() # 도커 엔진이 설치된 환경에서 실행해야 한다.

if __name__ == "__main__":
    main()