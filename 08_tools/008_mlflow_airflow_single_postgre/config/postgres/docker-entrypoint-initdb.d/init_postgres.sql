-- 
-- ###################################################################
--                 ⚠️  SECURITY ALERT: PASSWORD UPDATE ⚠️
-- ###################################################################
-- 
-- [필수 조치 사항]
-- Airflow 및 MLflow의 데이터베이스 접속 비밀번호를 강력한 보안값으로 즉시 변경해 주십시오.
-- 변경 시, 아래 두 위치의 비밀번호가 반드시 일치해야 합니다.
-- 
-- 1. 이 SQL 파일 내: 
--    - Airflow DB 사용자 생성의 USER 및 PASSWORD
--    - MLflow DB 사용자 생성의 USER 및 PASSWORD
--
-- 2. .env 환경 파일 내:
--    - AIRFLOW_DB_USER_NAME
--    - AIRFLOW_DB_USER_PASSWORD
--    - MLFLOW_DB_USER_NAME
--    - MLFLOW_DB_USER_PASSWORD
--    - POSTGRES_MASTER_USER
--    - POSTGRES_MASTER_PASSWORD
--
-- ###################################################################
--

-- Airflow 데이터베이스 및 사용자 생성
CREATE USER airflow WITH PASSWORD 'airflow';
CREATE DATABASE airflow OWNER airflow;

-- MLflow 데이터베이스 및 사용자 생성
CREATE USER mlflow WITH PASSWORD 'mlflow';
CREATE DATABASE mlflow OWNER mlflow;