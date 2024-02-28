from scheduler import do_task

from models.task import Task

test_task = Task(func_name="get_mail_outlook", kwargs={"keyword": "test_rpa", "from_date": "28/02/2024"})
do_task.delay(test_task.model_dump_json())

result = do_task.get()


