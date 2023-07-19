# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from v1 import project_pb2 as v1_dot_project__pb2


class StudioStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/api.v1.Studio/Ping',
                request_serializer=v1_dot_project__pb2.PingRequest.SerializeToString,
                response_deserializer=v1_dot_project__pb2.PingReply.FromString,
                )
        self.CreateProject = channel.unary_unary(
                '/api.v1.Studio/CreateProject',
                request_serializer=v1_dot_project__pb2.ProjectRequest.SerializeToString,
                response_deserializer=v1_dot_project__pb2.Project.FromString,
                )
        self.Projects = channel.unary_stream(
                '/api.v1.Studio/Projects',
                request_serializer=v1_dot_project__pb2.ProjectFilter.SerializeToString,
                response_deserializer=v1_dot_project__pb2.Project.FromString,
                )


class StudioServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Projects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StudioServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=v1_dot_project__pb2.PingRequest.FromString,
                    response_serializer=v1_dot_project__pb2.PingReply.SerializeToString,
            ),
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=v1_dot_project__pb2.ProjectRequest.FromString,
                    response_serializer=v1_dot_project__pb2.Project.SerializeToString,
            ),
            'Projects': grpc.unary_stream_rpc_method_handler(
                    servicer.Projects,
                    request_deserializer=v1_dot_project__pb2.ProjectFilter.FromString,
                    response_serializer=v1_dot_project__pb2.Project.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.v1.Studio', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Studio(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.Studio/Ping',
            v1_dot_project__pb2.PingRequest.SerializeToString,
            v1_dot_project__pb2.PingReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.v1.Studio/CreateProject',
            v1_dot_project__pb2.ProjectRequest.SerializeToString,
            v1_dot_project__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Projects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.v1.Studio/Projects',
            v1_dot_project__pb2.ProjectFilter.SerializeToString,
            v1_dot_project__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)