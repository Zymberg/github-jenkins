from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello, World!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )
