from concurrent import futures
import time
import json
from task_controller.model.task import Task
from task_controller.model.custom_log import CustomLog
from conf import TASK_CONTROLLER_SERVER

import grpc

from task_controller.gen import task_controller_pb2, task_controller_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TaskController(task_controller_pb2_grpc.TaskControllerServicer):

    def __init__(self):
        pass

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
    task_controller_pb2_grpc.add_TaskControllerServicer_to_server(TaskController(), server)
    server.add_insecure_port(TASK_CONTROLLER_SERVER)
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
