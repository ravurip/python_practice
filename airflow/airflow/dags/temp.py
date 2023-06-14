import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from temputils import conf_prep

dag = DAG(
    dag_id='an-example-dag',
    start_date=pendulum.datetime(2023, 5, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['example', 'example2'],
    params={"example_key": "example_value"},
)

init = PythonOperator(task_id="ConfigPrep", dag=dag,
                      python_callable=conf_prep,
                      op_args=[1, 2, 3, 4])

task = BashOperator(task_id="UserBash0", dag=dag, bash_command="sleep 30", cwd="/opt/airflow/logs/")

bash = BashOperator(task_id="UserBash", dag=dag, bash_command="ls -lR", cwd="/opt/airflow/logs/")

init >> task >> bash
