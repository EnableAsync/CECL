from __future__ import print_function

import grpc
import logging

from data_manager.gen import data_manager_pb2, data_manager_pb2_grpc
from common.task import Task
from common.custom_log import CustomLog
from conf import DATA_MANAGER_SERVER
from services_manager import resolver


class DataManager:
    def __init__(self):
        ip, port = resolver.get_service(DATA_MANAGER_SERVER['name'])
        logging.info(f"Remote server: {ip}:{port}")
        print(f"Remote server: {ip}:{port}")
        channel = grpc.insecure_channel(f"{ip}:{port}")
        self.stub = data_manager_pb2_grpc.DataManagerStub(channel)

    def add_task(self, task: Task):
        return self.stub.AddTask(data_manager_pb2.AddTaskReq(
            task=data_manager_pb2.Task(
                task_id=task.task_id,
                name=task.name,
                create_time=task.create_time,
                start_time=0,
                end_time=0,
                union_train=task.union_train,
                edge_nodes=task.edge_nodes,
                file=task.file,
            )
        ))

    def stop_task(self, task_id, stop_time):
        return self.stub.StopTask(data_manager_pb2.StopTaskReq(
            task_id=task_id,
            stop_time=stop_time,
        ))

    def start_task(self, task_id, start_time):
        return self.stub.StartTask(data_manager_pb2.StartTaskReq(
            task_id=task_id,
            start_time=start_time,
        ))

    def finish_task(self, task_id, finish_time):
        return self.stub.FinishTask(data_manager_pb2.FinishTaskReq(
            task_id=task_id,
            finish_time=finish_time,
        ))

    def get_all_tasks(self):
        return self.stub.GetAllTasks(data_manager_pb2.GetAllTasksReq())

    def update_task(self, task: Task):
        return self.stub.UpdateTask(data_manager_pb2.UpdateTaskReq(
            task=data_manager_pb2.Task(
                task_id=task.task_id,
                name=task.name,
                create_time=0,
                start_time=0,
                end_time=0,
                union_train=task.union_train,
                edge_nodes=task.edge_nodes,
                file=task.file,
            )
        ))

    def add_custom_log(self, task_log: CustomLog):
        return self.stub.AddCustomLog(data_manager_pb2.AddCustomLogReq(
            custom_log=data_manager_pb2.CustomLog(
                task_id=task_log.task_id,
                content=task_log.content,
                time=task_log.time,
            )
        ))

    def get_task_log(self, task_id):
        return self.stub.GetTaskLog(data_manager_pb2.GetTaskReq(
            task_id=task_id
        ))


if __name__ == '__main__':
    dm = DataManager()
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

    # log = CustomLog(
    #     task_id=1,
    #     content='Test!!',
    #     time=int(time.time())
    # )
    # dm.add_custom_log(log)
    dm.get_all_tasks()
