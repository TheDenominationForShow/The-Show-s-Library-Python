# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ShowLibInterface_pb2 as ShowLibInterface__pb2


class showlibifStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.command = channel.unary_unary(
        '/ShowLibInterface.showlibif/command',
        request_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
        )
    self.InsertRCHashRecords = channel.stream_stream(
        '/ShowLibInterface.showlibif/InsertRCHashRecords',
        request_serializer=ShowLibInterface__pb2.RCHashRecord.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
        )
    self.PulishRCHashCount = channel.unary_unary(
        '/ShowLibInterface.showlibif/PulishRCHashCount',
        request_serializer=ShowLibInterface__pb2.RecordCount.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
        )
    self.PulishRCHashRecords = channel.stream_unary(
        '/ShowLibInterface.showlibif/PulishRCHashRecords',
        request_serializer=ShowLibInterface__pb2.RCHashRecords.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
        )
    self.GetRCHashCount = channel.unary_unary(
        '/ShowLibInterface.showlibif/GetRCHashCount',
        request_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.RecordCount.FromString,
        )
    self.GetRCHashRecords = channel.unary_stream(
        '/ShowLibInterface.showlibif/GetRCHashRecords',
        request_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.RCHashRecords.FromString,
        )
    self.DownLoadRC = channel.unary_stream(
        '/ShowLibInterface.showlibif/DownLoadRC',
        request_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.FileBlock.FromString,
        )
    self.UpLoadRC = channel.stream_unary(
        '/ShowLibInterface.showlibif/UpLoadRC',
        request_serializer=ShowLibInterface__pb2.FileBlock.SerializeToString,
        response_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
        )


class showlibifServicer(object):
  """The greeting service definition.
  """

  def command(self, request, context):
    """命令
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InsertRCHashRecords(self, request_iterator, context):
    """批量插入数据
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PulishRCHashCount(self, request, context):
    """发布签名数
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PulishRCHashRecords(self, request_iterator, context):
    """发布签名
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRCHashCount(self, request, context):
    """获取签名数
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRCHashRecords(self, request, context):
    """获取签名
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownLoadRC(self, request, context):
    """下载资源
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpLoadRC(self, request_iterator, context):
    """上传资源
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_showlibifServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'command': grpc.unary_unary_rpc_method_handler(
          servicer.command,
          request_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
          response_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
      ),
      'InsertRCHashRecords': grpc.stream_stream_rpc_method_handler(
          servicer.InsertRCHashRecords,
          request_deserializer=ShowLibInterface__pb2.RCHashRecord.FromString,
          response_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
      ),
      'PulishRCHashCount': grpc.unary_unary_rpc_method_handler(
          servicer.PulishRCHashCount,
          request_deserializer=ShowLibInterface__pb2.RecordCount.FromString,
          response_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
      ),
      'PulishRCHashRecords': grpc.stream_unary_rpc_method_handler(
          servicer.PulishRCHashRecords,
          request_deserializer=ShowLibInterface__pb2.RCHashRecords.FromString,
          response_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
      ),
      'GetRCHashCount': grpc.unary_unary_rpc_method_handler(
          servicer.GetRCHashCount,
          request_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
          response_serializer=ShowLibInterface__pb2.RecordCount.SerializeToString,
      ),
      'GetRCHashRecords': grpc.unary_stream_rpc_method_handler(
          servicer.GetRCHashRecords,
          request_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
          response_serializer=ShowLibInterface__pb2.RCHashRecords.SerializeToString,
      ),
      'DownLoadRC': grpc.unary_stream_rpc_method_handler(
          servicer.DownLoadRC,
          request_deserializer=ShowLibInterface__pb2.CommandMsg.FromString,
          response_serializer=ShowLibInterface__pb2.FileBlock.SerializeToString,
      ),
      'UpLoadRC': grpc.stream_unary_rpc_method_handler(
          servicer.UpLoadRC,
          request_deserializer=ShowLibInterface__pb2.FileBlock.FromString,
          response_serializer=ShowLibInterface__pb2.CommandMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ShowLibInterface.showlibif', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
