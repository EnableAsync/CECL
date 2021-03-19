from __future__ import print_function

import time
from conf import TASK_RUNTIME_SERVER
from common.task import Task

import grpc

from services_manager import resolver
from task_runtime.gen import task_runtime_pb2, task_runtime_pb2_grpc


class TaskRuntime:
    def __init__(self):
        ip, port = resolver.get_service(TASK_RUNTIME_SERVER['name'])
        print(f"Remote server: {ip}:{port}")
        channel = grpc.insecure_channel(f"{ip}:{port}", options=[
            ('grpc.max_send_message_length', 10 * 1024 * 1024),
            ('grpc.max_receive_message_length', 10 * 1024 * 1024),
        ])
        self.stub = task_runtime_pb2_grpc.TaskRuntimeStub(channel)

    def add_task_by_git(self, t: Task):
        return self.stub.AddTaskByGit(task_runtime_pb2.AddTaskByGitReq(
            task=task_runtime_pb2.Task(
                task_id=t.task_id,
                name=t.name,
                create_time=t.create_time,
                start_time=0,
                end_time=0,
                union_train=t.union_train,
                edge_nodes=t.edge_nodes,
                file=t.file),
        ))

    def upload_task(self, t: Task, script: bytes, config: bytes):
        return self.stub.UploadTask(task_runtime_pb2.UploadTaskReq(
            task=task_runtime_pb2.Task(
                task_id=t.task_id,
                name=t.name,
                create_time=t.create_time,
                start_time=0,
                end_time=0,
                union_train=t.union_train,
                edge_nodes=t.edge_nodes,
                file=t.file),
            script=script,
            config=config,
        ))

    def start_task(self, task_id: int):
        return self.stub.StartTask(task_runtime_pb2.StartTaskReq(
            task_id=task_id
        ))

    def stop_task(self, task_id: int):
        return self.stub.StopTask(task_runtime_pb2.StopTaskReq(
            task_id=task_id
        ))

    def get_file(self, t: Task):
        return self.stub.GetTaskFile(task_runtime_pb2.GetTaskFileReq(
            task=task_runtime_pb2.Task(
                task_id=t.task_id,
                name=t.name,
                create_time=t.create_time,
                start_time=0,
                end_time=0,
                union_train=t.union_train,
                edge_nodes=t.edge_nodes,
                file=t.file),
        ))


if __name__ == '__main__':
    tr = TaskRuntime()
    task = Task(
        task_id=1,
        name="test_task",
        create_time=int(time.time()),
        union_train=0,
        edge_nodes='nodes',
        file='train.py'
    )
    file = open('./test/99.55%.py', 'rb')
    tr.upload_task(task, file.read(), b'')
    print(tr.start_task(1).resp.message)
