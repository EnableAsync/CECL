from __future__ import print_function

import grpc
import time
from conf import DEPLOY_RUNTIME_SERVER, TASK_RUNTIME_UPLOAD_PATH
from task_runtime.model.task import Task

import grpc

from task_runtime.gen import task_runtime_pb2, task_runtime_pb2_grpc


class TaskRuntime:
    def __init__(self):
        channel = grpc.insecure_channel(DEPLOY_RUNTIME_SERVER)
        self.stub = task_runtime_pb2_grpc.TaskRuntimeStub(channel)

    def upload_task(self, t: Task, script: bytes, config: bytes):
        return self.stub.UploadTask(task_runtime_pb2.UploadTaskReq(
            task=task_runtime_pb2.Task(
                task_id=t.task_id,
                name=t.name,
                create_time=t.create_time,
                start_time=0,
                end_time=0,
                union_train=t.union_train,
                edgenodes=t.edgenodes,
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
                edgenodes=t.edgenodes,
                file=t.file),
        ))


if __name__ == '__main__':
    tr = TaskRuntime()
    task = Task(
        task_id=1,
        name="test_task",
        create_time=int(time.time()),
        union_train=0,
        edgenodes='nodes',
        file='train.py'
    )
    file = open('./test/99.55%.py', 'rb')
    tr.upload_task(task, file.read(), b'')
    print(tr.start_task(1).resp.message)
