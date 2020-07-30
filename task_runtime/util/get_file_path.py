from conf import TASK_RUNTIME_UPLOAD_PATH
from task_runtime.model.task import Task


def get_script_path(task: Task) -> str:
    return '{}/{}/{}'.format(TASK_RUNTIME_UPLOAD_PATH, task.task_id, task.file)


def get_config_path(task: Task) -> str:
    return '{}/{}/{}'.format(TASK_RUNTIME_UPLOAD_PATH, task.task_id, 'config.json')
