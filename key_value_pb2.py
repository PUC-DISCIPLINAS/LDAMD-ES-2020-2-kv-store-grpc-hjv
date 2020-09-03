# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: .proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x06.proto\"\x15\n\x06GetKey\x12\x0b\n\x03key\x18\x01 \x01(\t\"*\n\x08GetReply\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65\x66ined\x18\x02 \x01(\x08\"7\n\x06PutKey\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\tbroadcast\x18\x03 \x01(\x08\"\x19\n\x08PutReply\x12\r\n\x05value\x18\x01 \x01(\t\"\x06\n\x04Void\"\x10\n\x02IP\x12\n\n\x02ip\x18\x01 \x01(\t\"a\n\nStoreReply\x12%\n\x05store\x18\x01 \x03(\x0b\x32\x16.StoreReply.StoreEntry\x1a,\n\nStoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x8f\x01\n\rKeyValueStore\x12\x1b\n\x03Get\x12\x07.GetKey\x1a\t.GetReply\"\x00\x12\x1b\n\x03Put\x12\x07.PutKey\x1a\t.PutReply\"\x00\x12\x1c\n\x04List\x12\x05.Void\x1a\x0b.StoreReply\"\x00\x12&\n\x10RegisterWithPeer\x12\x03.IP\x1a\x0b.StoreReply\"\x00\x62\x06proto3'
)




_GETKEY = _descriptor.Descriptor(
  name='GetKey',
  full_name='GetKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='GetKey.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10,
  serialized_end=31,
)


_GETREPLY = _descriptor.Descriptor(
  name='GetReply',
  full_name='GetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='GetReply.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='defined', full_name='GetReply.defined', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=75,
)


_PUTKEY = _descriptor.Descriptor(
  name='PutKey',
  full_name='PutKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PutKey.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='PutKey.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='broadcast', full_name='PutKey.broadcast', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=132,
)


_PUTREPLY = _descriptor.Descriptor(
  name='PutReply',
  full_name='PutReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PutReply.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=159,
)


_VOID = _descriptor.Descriptor(
  name='Void',
  full_name='Void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=167,
)


_IP = _descriptor.Descriptor(
  name='IP',
  full_name='IP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='IP.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=185,
)


_STOREREPLY_STOREENTRY = _descriptor.Descriptor(
  name='StoreEntry',
  full_name='StoreReply.StoreEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='StoreReply.StoreEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='StoreReply.StoreEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=284,
)

_STOREREPLY = _descriptor.Descriptor(
  name='StoreReply',
  full_name='StoreReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='store', full_name='StoreReply.store', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_STOREREPLY_STOREENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=284,
)

_STOREREPLY_STOREENTRY.containing_type = _STOREREPLY
_STOREREPLY.fields_by_name['store'].message_type = _STOREREPLY_STOREENTRY
DESCRIPTOR.message_types_by_name['GetKey'] = _GETKEY
DESCRIPTOR.message_types_by_name['GetReply'] = _GETREPLY
DESCRIPTOR.message_types_by_name['PutKey'] = _PUTKEY
DESCRIPTOR.message_types_by_name['PutReply'] = _PUTREPLY
DESCRIPTOR.message_types_by_name['Void'] = _VOID
DESCRIPTOR.message_types_by_name['IP'] = _IP
DESCRIPTOR.message_types_by_name['StoreReply'] = _STOREREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetKey = _reflection.GeneratedProtocolMessageType('GetKey', (_message.Message,), {
  'DESCRIPTOR' : _GETKEY,
  '__module__' : '_pb2'
  # @@protoc_insertion_point(class_scope:GetKey)
  })
_sym_db.RegisterMessage(GetKey)

GetReply = _reflection.GeneratedProtocolMessageType('GetReply', (_message.Message,), {
  'DESCRIPTOR' : _GETREPLY,
  '__module__' : '_pb2'
  # @@protoc_insertion_point(class_scope:GetReply)
  })
_sym_db.RegisterMessage(GetReply)

PutKey = _reflection.GeneratedProtocolMessageType('PutKey', (_message.Message,), {
  'DESCRIPTOR' : _PUTKEY,
  '__module__' : '_pb2'
  # @@protoc_insertion_point(class_scope:PutKey)
  })
_sym_db.RegisterMessage(PutKey)

PutReply = _reflection.GeneratedProtocolMessageType('PutReply', (_message.Message,), {
  'DESCRIPTOR' : _PUTREPLY,
  '__module__' : '_pb2'
  # @@protoc_insertion_point(class_scope:PutReply)
  })
_sym_db.RegisterMessage(PutReply)

Void = _reflection.GeneratedProtocolMessageType('Void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : '_pb2'
  # @@protoc_insertion_point(class_scope:Void)
  })
_sym_db.RegisterMessage(Void)

IP = _reflection.GeneratedProtocolMessageType('IP', (_message.Message,), {
  'DESCRIPTOR' : _IP,
  '__module__' : '_pb2'
  # @@protoc_insertion_point(class_scope:IP)
  })
_sym_db.RegisterMessage(IP)

StoreReply = _reflection.GeneratedProtocolMessageType('StoreReply', (_message.Message,), {

  'StoreEntry' : _reflection.GeneratedProtocolMessageType('StoreEntry', (_message.Message,), {
    'DESCRIPTOR' : _STOREREPLY_STOREENTRY,
    '__module__' : '_pb2'
    # @@protoc_insertion_point(class_scope:StoreReply.StoreEntry)
    })
  ,
  'DESCRIPTOR' : _STOREREPLY,
  '__module__' : '_pb2'
  # @@protoc_insertion_point(class_scope:StoreReply)
  })
_sym_db.RegisterMessage(StoreReply)
_sym_db.RegisterMessage(StoreReply.StoreEntry)


_STOREREPLY_STOREENTRY._options = None

_KEYVALUESTORE = _descriptor.ServiceDescriptor(
  name='KeyValueStore',
  full_name='KeyValueStore',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=287,
  serialized_end=430,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='KeyValueStore.Get',
    index=0,
    containing_service=None,
    input_type=_GETKEY,
    output_type=_GETREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Put',
    full_name='KeyValueStore.Put',
    index=1,
    containing_service=None,
    input_type=_PUTKEY,
    output_type=_PUTREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='KeyValueStore.List',
    index=2,
    containing_service=None,
    input_type=_VOID,
    output_type=_STOREREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterWithPeer',
    full_name='KeyValueStore.RegisterWithPeer',
    index=3,
    containing_service=None,
    input_type=_IP,
    output_type=_STOREREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYVALUESTORE)

DESCRIPTOR.services_by_name['KeyValueStore'] = _KEYVALUESTORE

# @@protoc_insertion_point(module_scope)