from concurrent import futures

import grpc
import time

from message_hub.gen import message_hub_pb2, message_hub_pb2_grpc
from conf import MESSAGE_HUB_SERVER_2
from common.task import Task

import task_runtime.gen.deploy_runtime_client
import task_controller.gen.deploy_controller_client
import task_controller.gen.task_controller_client
from services_manager import register

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MessageHub(message_hub_pb2_grpc.MessageHubServicer):
    def __init__(self):
        self.dr = task_runtime.gen.deploy_runtime_client.TaskRuntime()
        self.dc = task_controller.gen.deploy_controller_client.TaskController()
        self.tc = task_controller.gen.task_controller_client.TaskController()

    def SendMessageToEdge(self, request, context):
        msg = request.message
        resp = self.dc.send_message(msg).resp
        return message_hub_pb2.SendMessageToEdgeResp(resp=message_hub_pb2.Response(
            code=resp.code,
            message=resp.message
        ))

    def SendMessageToCloud(self, request, context):
        msg = request.message
        resp = self.tc.send_message(msg).resp
        return message_hub_pb2.SendMessageToCloudResp(resp=message_hub_pb2.Response(
            code=resp.code,
            message=resp.message
        ))

    def SendFile(self, request, context):
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
        script = request.script
        config = request.config
        resp = self.dr.upload_task(task, script, config).resp
        return message_hub_pb2.SendFileResp(resp=message_hub_pb2.Response(code=resp.code, message=resp.message))


def serve():
    # gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=6), options=[
        ('grpc.max_send_message_length', 10 * 1024 * 1024),
        ('grpc.max_receive_message_length', 10 * 1024 * 1024),
    ])
    message_hub_pb2_grpc.add_MessageHubServicer_to_server(MessageHub(), server)
    server.add_insecure_port(f"{MESSAGE_HUB_SERVER_2['ip']}:50099")
    register.register(MESSAGE_HUB_SERVER_2['name'],
                      MESSAGE_HUB_SERVER_2['ip'],
                      50099)
    server.start()  # start() will not block
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        register.unregister(MESSAGE_HUB_SERVER_2['name'],
                            MESSAGE_HUB_SERVER_2['ip'],
                            50099)
        server.stop(0)


if __name__ == '__main__':
    serve()
