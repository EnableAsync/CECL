from concurrent import futures
import time
from common.task import Task
from common.custom_log import CustomLog
from conf import TASK_CONTROLLER_SERVER
from services_manager import register
from data_manager.gen.data_manger_client import DataManager
from task_runtime.gen.task_runtime_client import TaskRuntime
# from grpc_reflection.v1alpha import reflection

import grpc

from task_controller.gen import task_controller_pb2, task_controller_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TaskController(task_controller_pb2_grpc.TaskControllerServicer):

    def __init__(self):
        self.db = DataManager()
        self.runtime = TaskRuntime()
        self.tasks = []

    def AddCustomLogCallback(self, request, context):
        log: CustomLog = request.custom_log
        resp = self.db.add_custom_log(log).resp
        return task_controller_pb2.AddCustomLogCallbackResp(resp=task_controller_pb2.Response(
            code=resp.code,
            message=resp.message,
        ))

    def AddTask(self, request, context):
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
        self.tasks.append(task)
        resp = self.db.add_task(task).resp
        print("add task:" + resp.message)
        return task_controller_pb2.AddTaskResp(resp=task_controller_pb2.Response(
            code=resp.code,
            message=resp.message,
        ))

        # if resp.code != 0:
        #     return task_controller_pb2.AddTaskResp(resp=task_controller_pb2.Response(
        #         code=resp.code,
        #         message=resp.message,
        #     ))
        # resp = self.runtime.start_task(request_task.task_id).resp
        # return task_controller_pb2.AddTaskResp(resp=task_controller_pb2.Response(
        #     code=resp.code,
        #     message=resp.message,
        # ))

    def StartTask(self, request, context):
        task_id: int = request.task_id
        print("start task task id:" + str(task_id))
        resp = self.db.start_task(task_id, int(time.time())).resp
        resp = self.runtime.start_task(task_id).resp
        print("start task runtime code:" + str(resp.code))
        if resp.code != 0:
            return task_controller_pb2.StartTaskResp(resp=task_controller_pb2.Response(
                code=resp.code,
                message=resp.message
            ))
        return task_controller_pb2.StartTaskResp(resp=task_controller_pb2.Response(
            code=resp.code,
            message=resp.message
        ))

    def StopTask(self, request, context):
        task_id: int = request.task_id
        resp = self.runtime.stop_task(task_id).resp
        if resp.code != 0:
            return task_controller_pb2.StopTaskReq(resp=task_controller_pb2.Response(
                code=resp.code,
                message=resp.message
            ))
        resp = self.db.stop_task(task_id, int(time.time()))
        return task_controller_pb2.StopTaskReq(resp=task_controller_pb2.Response(
            code=resp.code,
            message=resp.message
        ))

    def FinishTask(self, request, context):
        task_id: int = request.task_id
        resp = self.db.finish_task(task_id, int(time.time())).resp
        return task_controller_pb2.FinishTaskResp(resp=task_controller_pb2.Response(
            code=resp.code,
            message=resp.message
        ))

    def GetAllTasks(self, request, context):
        return super().GetAllTasks(request, context)

    def GetTaskInfo(self, request, context):
        return super().GetTaskInfo(request, context)

    def UpdateTask(self, request, context):
        return super().UpdateTask(request, context)

    def SendMessage(self, request, context):
        print("get message: " + request.message)
        return task_controller_pb2.SendMessageResp(resp=task_controller_pb2.Response(
            code=0,
            message="success"
        ))

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
    task_controller_pb2_grpc.add_TaskControllerServicer_to_server(TaskController(), server)

    # SERVICE_NAMES = (
    #     task_controller_pb2.DESCRIPTOR.services_by_name['TaskController'].full_name,
    #     reflection.SERVICE_NAME
    # )
    # reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(TASK_CONTROLLER_SERVER["port"])
    register.register(TASK_CONTROLLER_SERVER['name'],
                      TASK_CONTROLLER_SERVER['ip'],
                      int(TASK_CONTROLLER_SERVER['port']))
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        register.register(TASK_CONTROLLER_SERVER['name'],
                          TASK_CONTROLLER_SERVER['ip'],
                          int(TASK_CONTROLLER_SERVER['port']))
        server.stop(0)


if __name__ == '__main__':
    serve()
