from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

dag = DAG('example1', schedule_interval='* * * * *', start_date=datetime(2018, 1, 1))

task_1 = DummyOperator(task_id='tasK_1', retries=3)
task_2 = DummyOperator(task_id='task_2', retries=3)

dag >> task_1 >> task_2
