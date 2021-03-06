from conf import TASK_RUNTIME_UPLOAD_PATH
from common.task import Task
import os.path


def get_upload_path() -> str:
    return os.path.abspath(TASK_RUNTIME_UPLOAD_PATH)


def get_script_work_path(task: Task) -> str:
    return '{}/{}'.format(get_upload_path(), task.task_id)


def get_script_path(task: Task) -> str:
    return '{}/{}'.format(get_script_work_path(task), task.file)


def is_git_files(task: Task) -> bool:
    return task.file.endswith('.git') or task.file.startswith('https://github.com')


def get_docker_compose_yml_path(task: Task) -> str:
    return '{}/{}'.format(get_script_work_path(task), 'docker-compose.yml')


def get_config_path(task: Task) -> str:
    return '{}/{}'.format(get_script_work_path(task), 'config.json')


if __name__ == '__main__':
    print(get_script_path(Task(
        task_id=65,
        file='CNN.py'
    )))
