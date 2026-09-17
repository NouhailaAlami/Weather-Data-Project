from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import sys 

sys.path.append('/opt/airflow/api_request')
# tasks functions
def main_callable():
    from insert_records import main
    return main()
default_args ={
    'description':'a DAG to orchestrate weather data',
    'start_date': datetime(2026,9,17),
    'catchup': False,
    
}

dag =DAG(
    dag_id='weather-api-orchestrator',
    default_args = default_args,
    schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id ='example_task',
        python_callable=main_callable
    )
