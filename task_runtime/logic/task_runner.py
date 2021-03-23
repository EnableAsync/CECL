from common.custom_log import CustomLog
from common.task import Task
from task_controller.gen.task_controller_client import TaskController
from data_manager.gen.data_manger_client import DataManager
from task_runtime.util.get_file_path import get_script_path, get_script_work_path, is_git_files
import subprocess
import time

tasks = {}


def exist_task(task: Task):
    return tasks.get(task) is not None


def start_task(task: Task):
    print('start_task')
    print(task.task_id)
    tc = TaskController()
    dm = DataManager()
    try:
        print('script path:' + get_script_path(task))
        # codes from git which contain docker-compose.yml
        if is_git_files(task):
            sub = subprocess.Popen(
                ['docker-compose', 'up'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                cwd=get_script_work_path(task), bufsize=1)
        # uploaded codes
        else:
            sub = subprocess.Popen(
                ['python3.6', get_script_path(task)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                cwd=get_script_work_path(task), bufsize=1)

        for line in iter(sub.stdout.readline, b''):
            if line:
                print(line)
                dm.add_custom_log(CustomLog(
                    task_id=task.task_id,
                    content=line,
                    time=int(time.time())
                ))
        sub.stdout.close()

        if sub.returncode == 0:
            print('Subprogram success')
            tc.finish_task(task.task_id)
        else:
            print('Subprogram failed')
            tc.add_custom_log_callback(CustomLog(
                task_id=task.task_id,
                content=sub.stdout.read().decode('utf8'),
                time=int(time.time())
            ))
            tc.stop_task(task.task_id)
    except Exception as e:
        print('[error]' + str(e))
        tc.add_custom_log_callback(CustomLog(
            task_id=task.task_id,
            content=str(e),
            time=int(time.time())
        ))


def stop_task(task: Task) -> bool:
    if not exist_task(task):
        return False

    sub: subprocess.Popen = tasks[task]
    sub.kill()
    tc = TaskController()
    tc.add_custom_log_callback(CustomLog(
        task_id=task.task_id,
        content='[stop]',
        time=int(time.time())
    ))
    return True
