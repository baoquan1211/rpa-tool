from celery import Celery
from models.task import Task
from tasks.get_mail_gmail import get_mail_gmail
from tasks.get_mail_outlook import get_mail_outlook
import json
app = Celery('tasks', broker='redis://localhost:6379/0',
             backend='db+postgresql://root:2112@localhost:5432/rpa-scheduler')

@app.task
def do_task(task_json: str):
    task = json.loads(task_json)
    print(task)
    return globals()[task["func_name"]](*task["args"], **task["kwargs"])
