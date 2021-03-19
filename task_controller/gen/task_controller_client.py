from __future__ import print_function

import grpc
import time

from services_manager import resolver
from task_controller.gen import task_controller_pb2, task_controller_pb2_grpc
from common.task import Task
from common.custom_log import CustomLog
from conf import TASK_CONTROLLER_SERVER


class TaskController:
    def __init__(self):
        ip, port = resolver.get_service(TASK_CONTROLLER_SERVER['name'])
        print(f"Remote server: {ip}:{port}")
        channel = grpc.insecure_channel(f"{ip}:{port}")
        self.stub = task_controller_pb2_grpc.TaskControllerStub(channel)

    def add_custom_log_callback(self, custom_log: CustomLog):
        return self.stub.AddCustomLogCallback(task_controller_pb2.AddCustomLogCallbackReq(
            custom_log=task_controller_pb2.CustomLog(
                task_id=custom_log.task_id,
                content=custom_log.content,
                time=custom_log.time,
            )
        ))

    def add_task(self, t: Task):
        return self.stub.AddTask(task_controller_pb2.AddTaskReq(
            task=task_controller_pb2.Task(
                task_id=t.task_id,
                name=t.name,
                create_time=t.create_time,
                start_time=0,
                end_time=0,
                union_train=t.union_train,
                edge_nodes=t.edge_nodes,
                file=t.file
            )
        ))

    def add_task_by_git(self, t: Task):
        return self.stub.AddTaskByGit(task_controller_pb2.AddTaskByGitReq(
            task=task_controller_pb2.Task(
                task_id=t.task_id,
                name=t.name,
                create_time=t.create_time,
                start_time=0,
                end_time=0,
                union_train=t.union_train,
                edge_nodes=t.edge_nodes,
                file=t.file
            )
        ))

    def stop_task(self, task_id: int):
        return self.stub.StopTask(task_controller_pb2.StopTaskReq(
            task_id=task_id,
            stop_time=int(time.time())
        ))

    def start_task(self, task_id: int):
        return self.stub.StartTask(task_controller_pb2.StartTaskReq(
            task_id=task_id,
            start_time=int(time.time())
        ))

    def finish_task(self, task_id: int):
        return self.stub.FinishTask(task_controller_pb2.FinishTaskReq(
            task_id=task_id
        ))

    def send_message(self, msg):
        return self.stub.SendMessage(task_controller_pb2.SendMessageReq(
            message=msg
        ))


if __name__ == '__main__':
    tc = TaskController()
    # task = Task(
    #     task_id=1,
    #     name="test_task",
    #     create_time=int(time.time()),
    #     union_train=0,
    #     edge_nodes='nodes',
    #     file='train.py'
    # )
    # dm.add_task(task)
    # dm.start_task(2, int(time.time()))
    # dm.stop_task(2, int(time.time()))
    # dm.finish_task(2, int(time.time()))
    # ret = dm.get_all_tasks()
    # print(ret.resp)

    log = CustomLog(
        task_id=1,
        content='Test!!',
        time=int(time.time())
    )
    tc.add_custom_log_callback(log)
