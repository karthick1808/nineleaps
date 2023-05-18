from airflow import DAG
from datetime import datetime
with DAG('user_processing',start_date=datetime(2023,5,18),
         schedule_interval='@daily',catchup=False) as dag:
    None