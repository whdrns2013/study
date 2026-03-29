from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id="run_process_via_host_docker",
    start_date=datetime(2026,1,1),
    schedule=None,
    catchup=False
) as dag:

    run_job = DockerOperator(
        task_id="run_job",
        image="python:3.11-slim",
        command="python -c \"print('hello from container')\"",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        auto_remove="success",
    )