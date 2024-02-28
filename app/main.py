import schedule
import sys
import time
from models.task import Task


def print_sth(sth="code"):
    print("I'm working...", sth)


def foo():
    print("foo")


scheduler = schedule.Scheduler()


def exec_to_tasks() -> list[Task]:
    tasks: list[Task] = []
    if sys.argv[0] == "main.py":
        list_argv = sys.argv[1:]

        is_params = False

        for argv in list_argv:
            if argv == "-p":
                is_params = True
                continue

            if is_params:
                equal_index = argv.find("=")
                if equal_index == -1:
                    tasks[-1].args.append(argv)
                    is_params = False
                    continue

                split_kwargs = argv.split("=")
                assert len(split_kwargs) == 2
                tasks[-1].kwargs.update({split_kwargs[0]: split_kwargs[1]})
                is_params = False
                continue

            task = Task(func_name=argv)
            tasks.append(task)
    return tasks


if __name__ == "__main__":
    list_task = exec_to_tasks()
    print(list_task)
    for job in list_task:
        scheduler.every(2).seconds.do(globals()[job.func_name], *job.args, **job.kwargs)

    while True:
        scheduler.run_pending()
        time.sleep(1)
