from concurrent import futures

import grpc
import time
import json

from message_hub.gen import message_hub_pb2, message_hub_pb2_grpc
from conf import MESSAGE_HUB_SERVER
from common.task import Task

import message_hub.client.deploy_runtime_client
import message_hub.client.deploy_controller_client
import message_hub.client.task_controller_client

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class MessageHub(message_hub_pb2_grpc.MessageHubServicer):
    def __init__(self):
        self.dr = message_hub.client.deploy_runtime_client.TaskRuntime()
        self.dc = message_hub.client.deploy_controller_client.TaskController()
        self.tc = message_hub.client.task_controller_client.TaskController()

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
    server.add_insecure_port(MESSAGE_HUB_SERVER)
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
