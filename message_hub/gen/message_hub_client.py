import grpc

from message_hub.gen import message_hub_pb2, message_hub_pb2_grpc
from conf import MESSAGE_HUB_SERVER
from message_hub.model.task import Task


class MessageHub:
    def __init__(self):
        channel = grpc.insecure_channel(MESSAGE_HUB_SERVER)
        self.stub = message_hub_pb2_grpc.MessageHubStub(channel)
        # self.handler = {}

    def send_message_to_edge(self, msg):
        return self.stub.SendMessage(message_hub_pb2.SendMessageReq(
            message=msg
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
    #             edgenodes=t.edgenodes,
    #             file=t.file,
    #         )
    #     ))


if __name__ == '__main__':
    mh = MessageHub()
    mh.send_message("test")
