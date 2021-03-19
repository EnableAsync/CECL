import grpc

from message_hub.gen import message_hub_pb2, message_hub_pb2_grpc
from conf import MESSAGE_HUB_SERVER
from common.task import Task
from services_manager import resolver


class MessageHub:
    def __init__(self):
        ip, port = resolver.get_service(MESSAGE_HUB_SERVER['name'])
        print(f"Remote server: {ip}:{port}")
        channel = grpc.insecure_channel(f"{ip}:{port}")
        self.stub = message_hub_pb2_grpc.MessageHubStub(channel)
        # self.handler = {}

    def send_message_to_edge(self, msg):
        return self.stub.SendMessageToEdge(message_hub_pb2.SendMessageToEdgeReq(
            message=msg
        ))

    def send_message_to_cloud(self, msg):
        return self.stub.SendMessageToCloud(message_hub_pb2.SendMessageToCloudReq(
            message=msg
        ))

    def send_file(self, task: Task, script):
        return self.stub.SendFile(message_hub_pb2.SendFileReq(
            task=message_hub_pb2.Task(
                task_id=task.task_id
            ),
            script=script
        ))

    # def register_receive(self, identify, function):
    #     self.handler[identify] = function
    #
    # def send_task(self, t: Task):
    #     return self.stub.SendTask(message_hub_pb2.SendTaskReq(
    #         task=message_hub_pb2.Task(
    #             task_id=t.task_id,
    #             name=t.name,
    #             create_time=t.create_time,
    #             start_time=0,
    #             end_time=0,
    #             union_train=t.union_train,
    #             edge_nodes=t.edge_nodes,
    #             file=t.file,
    #         )
    #     ))


if __name__ == '__main__':
    mh = MessageHub()
    mh.send_message("test")
