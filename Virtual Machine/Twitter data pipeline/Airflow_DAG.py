# Import timedelta for working with time intervals
from datetime import timedelta

# Import DAG for defining DAGs in Airflow
from airflow import DAG

# Import PythonOperator for defining Python tasks in DAGs
from airflow.operators.python_operator import PythonOperator

# Import days_ago for working with dates in Airflow
from airflow.utils.dates import days_ago

# Import datetime for working with dates and times
from datetime import datetime

# Import the ETL_Datapipeline function for running the Twitter ETL process
from ETL import ETL_Datapipeline

# Define default arguments for the DAG
default_args = {
    'owner': 'AJAY',
    'depends_on_past': False,
    'start_date': datetime(2022, 4, 8),
    'email': ['junioralexio607@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the DAG
dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='First DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=ETL_Datapipeline,
    dag=dag, 
)

run_etl
