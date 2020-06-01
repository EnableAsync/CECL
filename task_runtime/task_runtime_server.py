from concurrent import futures
import time
import os
from conf import TASK_RUNTIME_SERVER, TASK_RUNTIME_UPLOAD_PATH
from task_runtime.model.task import Task

import grpc

from task_runtime.gen import task_runtime_pb2, task_runtime_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TaskRuntime(task_runtime_pb2_grpc.TaskRuntimeServicer):

    def UploadTask(self, request, context):
        task: Task = request.task
        script = request.script
        config = request.config

        os.makedirs('{}/{}'.format(TASK_RUNTIME_UPLOAD_PATH, task.task_id))

        script_path = '{}/{}/{}'.format(TASK_RUNTIME_UPLOAD_PATH, task.task_id, task.file)
        script_file = open(script_path, 'wb')
        script_file.write(script)
        script_file.close()

        config_path = '{}/{}/{}'.format(TASK_RUNTIME_UPLOAD_PATH, task.task_id, 'config.json')
        config_file = open(config_path, 'wb')
        config_file.write(config)
        config_file.close()

        return task_runtime_pb2.UploadTaskResp(resp=task_runtime_pb2.Response(code=0, message="success"))

    def StartTask(self, request, context):
        return super().StartTask(request, context)

    def StopTask(self, request, context):
        return super().StopTask(request, context)

    def GetTaskInfo(self, request, context):
        return super().GetTaskInfo(request, context)

    # # 工作函数
    # def SayHello(self, request, context):
    #     print(request)
    #     date_array = datetime.datetime.utcfromtimestamp(request.date)
    #     other_style_time = date_array.strftime("%Y-%m-%d %H:%M:%S")
    #     print(other_style_time)
    #     return hello_pb2.HelloReply(message='Hello, %s!' % request.name, date=other_style_time)


def serve():
    # gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
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
