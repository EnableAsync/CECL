from __future__ import print_function

import grpc
import time
from task_controller.gen import task_controller_pb2, task_controller_pb2_grpc
from task_controller.model.task import Task
from task_controller.model.custom_log import CustomLog
from conf import TASK_CONTROLLER_SERVER


class TaskController:
    def __init__(self):
        channel = grpc.insecure_channel(TASK_CONTROLLER_SERVER)
        self.stub = task_controller_pb2_grpc.TaskControllerStub(channel)

    def add_custom_log_callback(self, custom_log: CustomLog):
        return self.stub.AddCustomLogCallback(task_controller_pb2.AddCustomLogCallbackReq(
            custom_log=task_controller_pb2.CustomLog(
                task_id=custom_log.task_id,
                content=custom_log.content,
                time=custom_log.time,
            )
        ))

    def add_task(self, t: Task, script: bytes, config: bytes):
        return self.stub.AddTask(task_controller_pb2.AddTaskReq(
            task=task_controller_pb2.Task(
                task_id=t.task_id,
                name=t.name,
                create_time=t.create_time,
                start_time=0,
                end_time=0,
                union_train=t.union_train,
                edgenodes=t.edgenodes,
                file=t.file
            )
        ))



if __name__ == '__main__':
    tc = TaskController()
    # task = Task(
    #     task_id=1,
    #     name="test_task",
    #     create_time=int(time.time()),
    #     union_train=0,
    #     edgenodes='nodes',
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
