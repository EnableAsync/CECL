# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from message_hub.gen import message_hub_pb2 as message__hub_dot_gen_dot_message__hub__pb2


class MessageHubStub(object):
    """The message hub service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendFile = channel.unary_unary(
                '/MessageHub.MessageHub/SendFile',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendFileReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendFileResp.FromString,
                )
        self.SendTask = channel.unary_unary(
                '/MessageHub.MessageHub/SendTask',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskResp.FromString,
                )
        self.StopTask = channel.unary_unary(
                '/MessageHub.MessageHub/StopTask',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskResp.FromString,
                )
        self.SendMessageToCloud = channel.unary_unary(
                '/MessageHub.MessageHub/SendMessageToCloud',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToCloudReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToCloudResp.FromString,
                )
        self.SendMessageToEdge = channel.unary_unary(
                '/MessageHub.MessageHub/SendMessageToEdge',
                request_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToEdgeReq.SerializeToString,
                response_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToEdgeResp.FromString,
                )


class MessageHubServicer(object):
    """The message hub service definition.
    """

    def SendFile(self, request, context):
        """Send file to edges
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendTask(self, request, context):
        """Send and run a new task to edges.
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

    def SendMessageToCloud(self, request, context):
        """Send message to cloud
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessageToEdge(self, request, context):
        """Send message to edge
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageHubServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SendFile,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendFileReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendFileResp.SerializeToString,
            ),
            'SendTask': grpc.unary_unary_rpc_method_handler(
                    servicer.SendTask,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendTaskResp.SerializeToString,
            ),
            'StopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTask,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.StopTaskResp.SerializeToString,
            ),
            'SendMessageToCloud': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToCloud,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToCloudReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToCloudResp.SerializeToString,
            ),
            'SendMessageToEdge': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessageToEdge,
                    request_deserializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToEdgeReq.FromString,
                    response_serializer=message__hub_dot_gen_dot_message__hub__pb2.SendMessageToEdgeResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MessageHub.MessageHub', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MessageHub(object):
    """The message hub service definition.
    """

    @staticmethod
    def SendFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageHub.MessageHub/SendFile',
            message__hub_dot_gen_dot_message__hub__pb2.SendFileReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.SendFileResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageHub.MessageHub/SendTask',
            message__hub_dot_gen_dot_message__hub__pb2.SendTaskReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.SendTaskResp.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/MessageHub.MessageHub/StopTask',
            message__hub_dot_gen_dot_message__hub__pb2.StopTaskReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.StopTaskResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageToCloud(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageHub.MessageHub/SendMessageToCloud',
            message__hub_dot_gen_dot_message__hub__pb2.SendMessageToCloudReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.SendMessageToCloudResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessageToEdge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MessageHub.MessageHub/SendMessageToEdge',
            message__hub_dot_gen_dot_message__hub__pb2.SendMessageToEdgeReq.SerializeToString,
            message__hub_dot_gen_dot_message__hub__pb2.SendMessageToEdgeResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
