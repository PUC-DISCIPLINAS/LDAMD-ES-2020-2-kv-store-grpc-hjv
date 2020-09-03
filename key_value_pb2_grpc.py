import grpc

import key_value_pb2


class ClientStub(object):

  def __init__(self, channel):
    self.Get = channel.unary_unary(
        '/kv.Client/Get',
        request_serializer=key_value_pb2.GetKey.SerializeToString,
        response_deserializer=key_value_pb2.GetReply.FromString,
        )
    self.Set = channel.unary_unary(
        '/kv.Client/Put',
        request_serializer=key_value_pb2.PutKey.SerializeToString,
        response_deserializer=key_value_pb2.PutReply.FromString,
        )
    self.List = channel.unary_unary(
        '/kv.Client/List',
        request_serializer=key_value_pb2.Void.SerializeToString,
        response_deserializer=key_value_pb2.StoreReply.FromString,
        )
    self.RegisterWithPeer = channel.unary_unary(
        '/kv.Client/RegisterWithPeer',
        request_serializer=key_value_pb2.IP.SerializeToString,
        response_deserializer=key_value_pb2.StoreReply.FromString,
        )


class ClientServicer(object):

  def Get(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Set(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterWithPeer(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClientServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=key_value_pb2.GetKey.FromString,
          response_serializer=key_value_pb2.GetReply.SerializeToString,
      ),
      'Put': grpc.unary_unary_rpc_method_handler(
          servicer.Set,
          request_deserializer=key_value_pb2.PutKey.FromString,
          response_serializer=key_value_pb2.PutReply.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=key_value_pb2.Void.FromString,
          response_serializer=key_value_pb2.StoreReply.SerializeToString,
      ),
      'RegisterWithPeer': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterWithPeer,
          request_deserializer=key_value_pb2.IP.FromString,
          response_serializer=key_value_pb2.StoreReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kv.Client', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
