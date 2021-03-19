from concurrent import futures
import time
import os
from task_runtime.util.get_file_path import get_config_path, get_script_path, get_script_work_path
from conf import TASK_RUNTIME_SERVER
from common.task import Task
from task_runtime.logic.task_runner import start_task, stop_task
from task_runtime.gen.task_runtime_pb2 import UploadTaskReq

import grpc

from task_runtime.gen import task_runtime_pb2, task_runtime_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TaskRuntime(task_runtime_pb2_grpc.TaskRuntimeServicer):
    def __init__(self):
        self.tasks: dict = {}

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
        # script_path = '{}/{}/{}'.format(TASK_RUNTIME_UPLOAD_PATH, task.task_id, task.file)
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

    # # 工作函数
    # def SayHello(self, request, context):
    #     print(request)
    #     date_array = datetime.datetime.utcfromtimestamp(request.date)
    #     other_style_time = date_array.strftime("%Y-%m-%d %H:%M:%S")
    #     print(other_style_time)
    #     return hello_pb2.HelloReply(message='Hello, %s!' % request.name, date=other_style_time)


def serve():
    # gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', 10 * 1024 * 1024),
        ('grpc.max_receive_message_length', 10 * 1024 * 1024),
    ])
    task_runtime_pb2_grpc.add_TaskRuntimeServicer_to_server(TaskRuntime(), server)
    server.add_insecure_port(TASK_RUNTIME_SERVER)
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
