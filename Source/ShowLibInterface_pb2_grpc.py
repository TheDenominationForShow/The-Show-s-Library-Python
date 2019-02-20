# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ShowLibInterface_pb2 as ShowLibInterface__pb2


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.InsertRCHashRecord = channel.unary_unary(
        '/ShowLibInterface.Greeter/InsertRCHashRecord',
        request_serializer=ShowLibInterface__pb2.RCHashRecord.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.Result.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def InsertRCHashRecord(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'InsertRCHashRecord': grpc.unary_unary_rpc_method_handler(
          servicer.InsertRCHashRecord,
          request_deserializer=ShowLibInterface__pb2.RCHashRecord.FromString,
          response_serializer=ShowLibInterface__pb2.Result.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ShowLibInterface.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))