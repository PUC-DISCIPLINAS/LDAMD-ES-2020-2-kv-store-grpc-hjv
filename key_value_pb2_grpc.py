import grpc

import kv_pb2 as kv__pb2


class ClientStub(object):
  """The client service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/kv.Client/Get',
        request_serializer=kv__pb2.GetKey.SerializeToString,
        response_deserializer=kv__pb2.GetReply.FromString,
        )
    self.Set = channel.unary_unary(
        '/kv.Client/Set',
        request_serializer=kv__pb2.SetKey.SerializeToString,
        response_deserializer=kv__pb2.SetReply.FromString,
        )
    self.List = channel.unary_unary(
        '/kv.Client/List',
        request_serializer=kv__pb2.Void.SerializeToString,
        response_deserializer=kv__pb2.StoreReply.FromString,
        )
    self.RegisterWithPeer = channel.unary_unary(
        '/kv.Client/RegisterWithPeer',
        request_serializer=kv__pb2.IP.SerializeToString,
        response_deserializer=kv__pb2.StoreReply.FromString,
        )


class ClientServicer(object):
  """The client service definition.
  """

  def Get(self, request, context):
    """Retrieves a key from a server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Set(self, request, context):
    """Set a key on a server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """List all the keys defined on a server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RegisterWithPeer(self, request, context):
    """Registers a new server with a peer.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClientServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=kv__pb2.GetKey.FromString,
          response_serializer=kv__pb2.GetReply.SerializeToString,
      ),
      'Set': grpc.unary_unary_rpc_method_handler(
          servicer.Set,
          request_deserializer=kv__pb2.SetKey.FromString,
          response_serializer=kv__pb2.SetReply.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=kv__pb2.Void.FromString,
          response_serializer=kv__pb2.StoreReply.SerializeToString,
      ),
      'RegisterWithPeer': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterWithPeer,
          request_deserializer=kv__pb2.IP.FromString,
          response_serializer=kv__pb2.StoreReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kv.Client', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))