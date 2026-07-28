import mlflow
import os

# 1. 환경 변수 설정 (호스트 PC 기준 포트 사용)
# .env의 MLFLOW_PORT(5000)와 POSTGRES_PORT(15432)가 호스트에 노출되어 있어야 함
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000" # RustFS 외부 포트
os.environ["AWS_ACCESS_KEY_ID"] = "s3admin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "s3admin"

# 2. MLflow 서버 연결
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("artifact-test")

with mlflow.start_run():
    # 파라미터 및 메트릭 기록 (DB 테스트)
    mlflow.log_param("status", "testing")
    mlflow.log_metric("accuracy", 0.95)
    
    # 3. 아티팩트 생성 및 업로드 (S3/RustFS 테스트)
    with open("test_artifact.txt", "w") as f:
        f.write("MLflow Artifact Storage Test Success!")
    
    mlflow.log_artifact("test_artifact.txt")
    
    print("Run completed. Check MLflow UI at http://localhost:5000")