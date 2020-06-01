# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from task_runtime.gen import task_runtime_pb2 as task__runtime_dot_gen_dot_task__runtime__pb2


class TaskRuntimeStub(object):
    """The task runtime service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadTask = channel.unary_unary(
                '/TaskRuntime/UploadTask',
                request_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.UploadTaskReq.SerializeToString,
                response_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.UploadTaskResp.FromString,
                )
        self.StartTask = channel.unary_unary(
                '/TaskRuntime/StartTask',
                request_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.StartTaskReq.SerializeToString,
                response_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.StartTaskResp.FromString,
                )
        self.StopTask = channel.unary_unary(
                '/TaskRuntime/StopTask',
                request_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.StopTaskReq.SerializeToString,
                response_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.StopTaskResp.FromString,
                )
        self.GetTaskInfo = channel.unary_unary(
                '/TaskRuntime/GetTaskInfo',
                request_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.GetTaskInfoReq.SerializeToString,
                response_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.GetTaskInfoResp.FromString,
                )


class TaskRuntimeServicer(object):
    """The task runtime service definition.
    """

    def UploadTask(self, request, context):
        """Add task's file
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartTask(self, request, context):
        """Run a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTask(self, request, context):
        """Stop a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskInfo(self, request, context):
        """Get task information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskRuntimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadTask,
                    request_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.UploadTaskReq.FromString,
                    response_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.UploadTaskResp.SerializeToString,
            ),
            'StartTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTask,
                    request_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.StartTaskReq.FromString,
                    response_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.StartTaskResp.SerializeToString,
            ),
            'StopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTask,
                    request_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.StopTaskReq.FromString,
                    response_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.StopTaskResp.SerializeToString,
            ),
            'GetTaskInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskInfo,
                    request_deserializer=task__runtime_dot_gen_dot_task__runtime__pb2.GetTaskInfoReq.FromString,
                    response_serializer=task__runtime_dot_gen_dot_task__runtime__pb2.GetTaskInfoResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TaskRuntime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskRuntime(object):
    """The task runtime service definition.
    """

    @staticmethod
    def UploadTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskRuntime/UploadTask',
            task__runtime_dot_gen_dot_task__runtime__pb2.UploadTaskReq.SerializeToString,
            task__runtime_dot_gen_dot_task__runtime__pb2.UploadTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskRuntime/StartTask',
            task__runtime_dot_gen_dot_task__runtime__pb2.StartTaskReq.SerializeToString,
            task__runtime_dot_gen_dot_task__runtime__pb2.StartTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskRuntime/StopTask',
            task__runtime_dot_gen_dot_task__runtime__pb2.StopTaskReq.SerializeToString,
            task__runtime_dot_gen_dot_task__runtime__pb2.StopTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskRuntime/GetTaskInfo',
            task__runtime_dot_gen_dot_task__runtime__pb2.GetTaskInfoReq.SerializeToString,
            task__runtime_dot_gen_dot_task__runtime__pb2.GetTaskInfoResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
