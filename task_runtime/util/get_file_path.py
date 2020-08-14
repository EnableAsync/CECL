from conf import TASK_RUNTIME_UPLOAD_PATH
from task_runtime.model.task import Task
import os.path


def get_upload_path() -> str:
    return os.path.abspath(TASK_RUNTIME_UPLOAD_PATH)


def get_script_work_path(task: Task) -> str:
    return '{}/{}'.format(get_upload_path(), task.task_id)


def get_script_path(task: Task) -> str:
    return '{}/{}'.format(get_script_work_path(task), task.file)


def get_config_path(task: Task) -> str:
    return '{}/{}'.format(get_script_work_path(task), 'config.json')


if __name__ == '__main__':
    print(get_script_path(Task(
        task_id=65,
        file='CNN.py'
    )))
