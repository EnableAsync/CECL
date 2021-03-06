from concurrent import futures
import time
import os
from threading import Thread

from services_manager import register
from task_runtime.logic import git_clone
from task_runtime.util.get_file_path import get_config_path, get_script_path, get_script_work_path, \
    get_docker_compose_yml_path, is_git_files
from conf import TASK_RUNTIME_SERVER
from common.task import Task
from task_runtime.logic.task_runner import start_task, stop_task
from task_runtime.gen.task_runtime_pb2 import UploadTaskReq
from data_manager.gen.data_manger_client import DataManager

from common.custom_log import CustomLog

import grpc

from task_runtime.gen import task_runtime_pb2, task_runtime_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TaskRuntime(task_runtime_pb2_grpc.TaskRuntimeServicer):
    def __init__(self):
        self.tasks: dict = {}
        self.db = DataManager()

    def AddTaskByGit(self, request, context):
        request_task: Task = request.task
        upload_path = get_script_work_path(request_task)

        if request_task.task_id not in self.tasks:
            self.tasks[request_task.task_id] = request_task

        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        try:
            # clone and response can be parallel
            print(f"clone to {upload_path}")

            # start clone
            url = request_task.file
            path = upload_path
            clone = Thread(target=git_clone.clone_from_url, args=(url, path, request_task))
            clone.start()

            return task_runtime_pb2.AddTaskByGitResp(
                resp=task_runtime_pb2.Response(code=0, message="starting clone"))
        except Exception as e:
            return task_runtime_pb2.AddTaskByGitResp(
                resp=task_runtime_pb2.Response(code=10002, message=str(e)))

    # async def clone_and_response(self, url, path):
    #     tasks = [
    #         asyncio.create_task(git_clone.clone_from_url(url=url, path=path)),
    #         asyncio.create_task(self.response_to_grpc_client())
    #     ]
    #     done, pending = await asyncio.wait(tasks, timeout=0.1)
    #     print(done)

    # @staticmethod
    # async def response_to_grpc_client():
    #     await task_runtime_pb2.AddTaskByGitResp(
    #         resp=task_runtime_pb2.Response(code=0, message="starting clone"))

    def AddTaskByHTTP(self, request, context):
        return super().AddTaskByHTTP(request, context)

    def UploadTask(self, request: UploadTaskReq, context):
        request_task = request.task

        print(type(request_task))
        task: Task = Task(
            task_id=request_task.task_id,
            name=request_task.name,
            create_time=request_task.create_time,
            start_time=request_task.start_time,
            end_time=request_task.end_time,
            union_train=request_task.union_train,
            edge_nodes=request_task.edge_nodes,
            file=request_task.file,
            status=0
        )
        script = request.script
        config = request.config

        if request_task.task_id == 0:
            return task_runtime_pb2.UploadTaskResp(
                resp=task_runtime_pb2.Response(code=10001, message="task id can't be empty"))

        # upload_path = '{}/{}'.format(TASK_RUNTIME_UPLOAD_PATH, request_task.task_id)
        upload_path = get_script_work_path(task)
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)

        script_path = get_script_path(request_task)
        print("save file to: " + script_path)
        script_file = open(script_path, 'wb')
        script_file.write(script)
        script_file.close()
        print("save file finish")

        config_path = get_config_path(request_task)
        config_file = open(config_path, 'wb')
        config_file.write(config)
        config_file.close()

        if task.task_id not in self.tasks:
            self.tasks[request_task.task_id] = task

        return task_runtime_pb2.UploadTaskResp(resp=task_runtime_pb2.Response(code=0, message="success"))

    def StartTask(self, request, context):
        task_id: int = request.task_id
        if task_id not in self.tasks:
            return task_runtime_pb2.StartTaskResp(
                resp=task_runtime_pb2.Response(code=10000, message="Task not found"))

        task: Task = self.tasks[task_id]
        print(task)

        # uploaded file
        if is_git_files(task):
            docker_compose_path = get_docker_compose_yml_path(task)
            print(docker_compose_path)
            if not os.path.exists(docker_compose_path):
                return task_runtime_pb2.StartTaskResp(
                    resp=task_runtime_pb2.Response(code=10000, message="Docker compose file not uploaded"))
        else:
            script_path = get_script_path(task)
            print("start file: " + script_path)
            if not os.path.exists(script_path):
                return task_runtime_pb2.StartTaskResp(
                    resp=task_runtime_pb2.Response(code=10000, message="Script not uploaded"))

        start_task(task)
        return task_runtime_pb2.StartTaskResp(
            resp=task_runtime_pb2.Response(code=0, message="success"))

    def StopTask(self, request, context):
        task_id: int = request.task_id
        if task_id not in self.tasks:
            return task_runtime_pb2.StartTaskResp(
                resp=task_runtime_pb2.Response(code=10000, message="Task not found"))
        if stop_task(self.tasks[task_id]):
            return task_runtime_pb2.StopTaskResp(
                resp=task_runtime_pb2.Response(code=0, message="success"))

    def GetTaskInfo(self, request, context):
        return super().GetTaskInfo(request, context)

    def GetTaskFile(self, request, context):
        request_task = request.task
        task: Task = Task(
            task_id=request_task.task_id,
            name=request_task.name,
            create_time=request_task.create_time,
            start_time=request_task.start_time,
            end_time=request_task.end_time,
            union_train=request_task.union_train,
            edge_nodes=request_task.edge_nodes,
            file=request_task.file,
            status=0
        )
        if request_task.task_id == 0:
            return task_runtime_pb2.GetTaskFileResp(
                resp=task_runtime_pb2.Response(code=10001, message="task id can't be empty"),
                script=b'',
                config=b''
            )
        file_path = get_script_path(task)
        if not os.path.exists(file_path):
            return task_runtime_pb2.GetTaskFileResp(
                resp=task_runtime_pb2.Response(code=10001, message="file is not exists"),
                script=b'',
                config=b''
            )
        file = open(file_path, 'rb')
        file_bytes = file.read()
        file.close()
        print("get file:{}".format(file_path))
        return task_runtime_pb2.GetTaskFileResp(
            resp=task_runtime_pb2.Response(code=0, message='success'),
            script=file_bytes,
            config=b''
        )

    # def SayHello(self, request, context):
    #     print(request)
    #     date_array = datetime.datetime.utcfromtimestamp(request.date)
    #     other_style_time = date_array.strftime("%Y-%m-%d %H:%M:%S")
    #     print(other_style_time)
    #     return hello_pb2.HelloReply(message='Hello, %s!' % request.name, date=other_style_time)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', 10 * 1024 * 1024),
        ('grpc.max_receive_message_length', 10 * 1024 * 1024),
    ])
    task_runtime_pb2_grpc.add_TaskRuntimeServicer_to_server(TaskRuntime(), server)
    server.add_insecure_port(f"{TASK_RUNTIME_SERVER['ip']}:{TASK_RUNTIME_SERVER['port']}")
    register.register(TASK_RUNTIME_SERVER['name'],
                      TASK_RUNTIME_SERVER['ip'],
                      int(TASK_RUNTIME_SERVER['port']))
    server.start()  # start() will not block
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        register.register(TASK_RUNTIME_SERVER['name'],
                          TASK_RUNTIME_SERVER['ip'],
                          int(TASK_RUNTIME_SERVER['port']))
        server.stop(0)


if __name__ == '__main__':
    serve()
