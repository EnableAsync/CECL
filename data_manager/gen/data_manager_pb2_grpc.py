# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from data_manager.gen import data_manager_pb2 as data__manager_dot_gen_dot_data__manager__pb2


class DataManagerStub(object):
    """The data manager service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTask = channel.unary_unary(
                '/DataManager.DataManager/AddTask',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskResp.FromString,
                )
        self.StartTask = channel.unary_unary(
                '/DataManager.DataManager/StartTask',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.StartTaskReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.StartTaskResp.FromString,
                )
        self.StopTask = channel.unary_unary(
                '/DataManager.DataManager/StopTask',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.StopTaskReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.StopTaskResp.FromString,
                )
        self.FinishTask = channel.unary_unary(
                '/DataManager.DataManager/FinishTask',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.FinishTaskReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.FinishTaskResp.FromString,
                )
        self.GetTask = channel.unary_unary(
                '/DataManager.DataManager/GetTask',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskResp.FromString,
                )
        self.GetAllTasks = channel.unary_unary(
                '/DataManager.DataManager/GetAllTasks',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.GetAllTasksReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.GetAllTasksResp.FromString,
                )
        self.UpdateTask = channel.unary_unary(
                '/DataManager.DataManager/UpdateTask',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.UpdateTaskReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.UpdateTaskResp.FromString,
                )
        self.AddCustomLog = channel.unary_unary(
                '/DataManager.DataManager/AddCustomLog',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddCustomLogReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddCustomLogResp.FromString,
                )
        self.GetTaskLog = channel.unary_unary(
                '/DataManager.DataManager/GetTaskLog',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskLogReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskLogResp.FromString,
                )
        self.AddPullingLog = channel.unary_unary(
                '/DataManager.DataManager/AddPullingLog',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddPullingLogReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddPullingLogResp.FromString,
                )
        self.AddTaskByGit = channel.unary_unary(
                '/DataManager.DataManager/AddTaskByGit',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByGitReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByGitResp.FromString,
                )
        self.AddTaskByHTTP = channel.unary_unary(
                '/DataManager.DataManager/AddTaskByHTTP',
                request_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByHTTPReq.SerializeToString,
                response_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByHTTPResp.FromString,
                )


class DataManagerServicer(object):
    """The data manager service definition.
    """

    def AddTask(self, request, context):
        """Add a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartTask(self, request, context):
        """Start a task
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

    def FinishTask(self, request, context):
        """Will be called when a task finished
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTask(self, request, context):
        """Get task information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTasks(self, request, context):
        """Get all tasks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Update task information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCustomLog(self, request, context):
        """Add task script log
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskLog(self, request, context):
        """Get task logs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPullingLog(self, request, context):
        """Add task pulling log
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTaskByGit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTaskByHTTP(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskResp.SerializeToString,
            ),
            'StartTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTask,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.StartTaskReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.StartTaskResp.SerializeToString,
            ),
            'StopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTask,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.StopTaskReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.StopTaskResp.SerializeToString,
            ),
            'FinishTask': grpc.unary_unary_rpc_method_handler(
                    servicer.FinishTask,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.FinishTaskReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.FinishTaskResp.SerializeToString,
            ),
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskResp.SerializeToString,
            ),
            'GetAllTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTasks,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.GetAllTasksReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.GetAllTasksResp.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.UpdateTaskReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.UpdateTaskResp.SerializeToString,
            ),
            'AddCustomLog': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCustomLog,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddCustomLogReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddCustomLogResp.SerializeToString,
            ),
            'GetTaskLog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskLog,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskLogReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.GetTaskLogResp.SerializeToString,
            ),
            'AddPullingLog': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPullingLog,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddPullingLogReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddPullingLogResp.SerializeToString,
            ),
            'AddTaskByGit': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTaskByGit,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByGitReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByGitResp.SerializeToString,
            ),
            'AddTaskByHTTP': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTaskByHTTP,
                    request_deserializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByHTTPReq.FromString,
                    response_serializer=data__manager_dot_gen_dot_data__manager__pb2.AddTaskByHTTPResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataManager.DataManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataManager(object):
    """The data manager service definition.
    """

    @staticmethod
    def AddTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/AddTask',
            data__manager_dot_gen_dot_data__manager__pb2.AddTaskReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.AddTaskResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/StartTask',
            data__manager_dot_gen_dot_data__manager__pb2.StartTaskReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.StartTaskResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/StopTask',
            data__manager_dot_gen_dot_data__manager__pb2.StopTaskReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.StopTaskResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinishTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/FinishTask',
            data__manager_dot_gen_dot_data__manager__pb2.FinishTaskReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.FinishTaskResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/GetTask',
            data__manager_dot_gen_dot_data__manager__pb2.GetTaskReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.GetTaskResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/GetAllTasks',
            data__manager_dot_gen_dot_data__manager__pb2.GetAllTasksReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.GetAllTasksResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/UpdateTask',
            data__manager_dot_gen_dot_data__manager__pb2.UpdateTaskReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.UpdateTaskResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCustomLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/AddCustomLog',
            data__manager_dot_gen_dot_data__manager__pb2.AddCustomLogReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.AddCustomLogResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/GetTaskLog',
            data__manager_dot_gen_dot_data__manager__pb2.GetTaskLogReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.GetTaskLogResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPullingLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/AddPullingLog',
            data__manager_dot_gen_dot_data__manager__pb2.AddPullingLogReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.AddPullingLogResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTaskByGit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/AddTaskByGit',
            data__manager_dot_gen_dot_data__manager__pb2.AddTaskByGitReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.AddTaskByGitResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTaskByHTTP(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataManager.DataManager/AddTaskByHTTP',
            data__manager_dot_gen_dot_data__manager__pb2.AddTaskByHTTPReq.SerializeToString,
            data__manager_dot_gen_dot_data__manager__pb2.AddTaskByHTTPResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
