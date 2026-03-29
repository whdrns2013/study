# docker_operator_mount_example.py
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime

with DAG(
    dag_id="docker_mount",
    start_date=datetime(2026,1,1),
    schedule=None,
    catchup=False
) as dag:

    sleeping = DockerOperator(
        task_id="sleeping",
        image="python:3.11-slim",
        command="python /workspace/src/scripts/sleeping.py",
        docker_url="unix://var/run/docker.sock",
        mounts=[
            Mount(
                source="/opt/airflow/src/scripts", # 원천데이터 : 호스트에서 접근 가능한 경로여야 함
                # source="/mnt/host/c/Users/user/Documents/추천/박종혁/airflow/airflow/src/scripts", # 원천데이터 : 호스트에서 접근 가능한 경로여야 함
                target="/workspace/src/scripts",   # 타겟 : 워커 컨테이너 내에 마운트할 경로
                type="bind",                       # 마운트 유형
            ),
            Mount(
                # source="/mnt/host/c/Users/user/Documents/추천/박종혁/airflow/airflow/src/data",
                source="/opt/airflow/src/data",
                target="/workspace/src/data",
                type="bind",
                read_only=True                     # 마운트 읽기전용 여부
            ),
        ],
        network_mode="bridge",
        working_dir="/workspace",
        auto_remove="success",
    )