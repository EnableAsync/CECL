from git import Repo
from data_manager.gen.data_manger_client import DataManager
from common.task import Task
from common.custom_log import CustomLog

import time

db = DataManager()


def clone_from_url(url, path, task: Task):
    try:
        Repo.clone_from(url, path)
        clone_finished(task)
    except Exception as e:
        clone_error(task, e)


def clone_error(request_task, error):
    # add pulling log
    db.add_pulling_log(
        task_log=CustomLog(task_id=request_task.task_id, content=str(error), time=int(time.time())))

    # update status
    request_task.status = Task.PULL_FAILURE
    db.update_task(task=request_task)


def clone_finished(request_task):
    # update status
    request_task.status = Task.READY
    db.update_task(task=request_task)

    # add log
    db.add_pulling_log(
        task_log=CustomLog(task_id=request_task.task_id, content=f"clone {request_task.file} finished.",
                           time=int(time.time())))
