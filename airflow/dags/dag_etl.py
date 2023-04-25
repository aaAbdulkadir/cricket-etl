from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.etl.extract import *
from src.etl.transform import *
from src.etl.load import *

default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    default_args=default_args,
    dag_id='cricket-etl-1',
    description='get cricket data',
    start_date=datetime.today()-timedelta(days=2), #testing
    schedule_interval='0 9 * * *' # 9am everyday
) as dag:
    extract = PythonOperator(
        task_id='Extract',
        python_callable=extract
    )
    transform = PythonOperator(
        task_id='Transform',
        python_callable=transform
    )
    load = PythonOperator(
        task_id='Load',
        python_callable=load
    )
    extract >> transform >> load