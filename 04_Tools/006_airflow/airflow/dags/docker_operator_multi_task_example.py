# docker_operator_multi_task_examply.py
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id="multi_task_docker_operator",
    start_date=datetime(2026,1,1),
    schedule=None,
    catchup=False
) as dag:

    first_job = DockerOperator(
        task_id="first_job",
        image="python:3.11-slim",
        command="python -c \"print('hello from container')\"",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        auto_remove="success",
    )

    second_job = DockerOperator(
        task_id="second_job",
        image="python:3.11-slim",
        command="python -c \"print('2nd job is here!')\"",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        auto_remove="success",
    )