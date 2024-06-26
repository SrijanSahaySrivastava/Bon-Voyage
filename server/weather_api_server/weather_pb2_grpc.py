# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import weather_pb2 as weather__pb2


class LatLongServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetForcasteWeather = channel.unary_unary(
                '/weather_api.LatLongService/GetForcasteWeather',
                request_serializer=weather__pb2.Forcaste_Weather_req.SerializeToString,
                response_deserializer=weather__pb2.Forcaste_Weather_res.FromString,
                )


class LatLongServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetForcasteWeather(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LatLongServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetForcasteWeather': grpc.unary_unary_rpc_method_handler(
                    servicer.GetForcasteWeather,
                    request_deserializer=weather__pb2.Forcaste_Weather_req.FromString,
                    response_serializer=weather__pb2.Forcaste_Weather_res.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weather_api.LatLongService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LatLongService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetForcasteWeather(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/weather_api.LatLongService/GetForcasteWeather',
            weather__pb2.Forcaste_Weather_req.SerializeToString,
            weather__pb2.Forcaste_Weather_res.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
