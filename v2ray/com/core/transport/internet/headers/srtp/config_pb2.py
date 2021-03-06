# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/transport/internet/headers/srtp/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/transport/internet/headers/srtp/config.proto',
  package='v2ray.core.transport.internet.headers.srtp',
  syntax='proto3',
  serialized_options=_b('\n.com.v2ray.core.transport.internet.headers.srtpP\001Z\004srtp\252\002*V2Ray.Core.Transport.Internet.Headers.Srtp'),
  serialized_pb=_b('\n;v2ray.com/core/transport/internet/headers/srtp/config.proto\x12*v2ray.core.transport.internet.headers.srtp\"w\n\x06\x43onfig\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0f\n\x07padding\x18\x02 \x01(\x08\x12\x11\n\textension\x18\x03 \x01(\x08\x12\x12\n\ncsrc_count\x18\x04 \x01(\r\x12\x0e\n\x06marker\x18\x05 \x01(\x08\x12\x14\n\x0cpayload_type\x18\x06 \x01(\rBe\n.com.v2ray.core.transport.internet.headers.srtpP\x01Z\x04srtp\xaa\x02*V2Ray.Core.Transport.Internet.Headers.Srtpb\x06proto3')
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.headers.srtp.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='v2ray.core.transport.internet.headers.srtp.Config.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='padding', full_name='v2ray.core.transport.internet.headers.srtp.Config.padding', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='v2ray.core.transport.internet.headers.srtp.Config.extension', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='csrc_count', full_name='v2ray.core.transport.internet.headers.srtp.Config.csrc_count', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marker', full_name='v2ray.core.transport.internet.headers.srtp.Config.marker', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload_type', full_name='v2ray.core.transport.internet.headers.srtp.Config.payload_type', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=107,
  serialized_end=226,
)

DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.transport.internet.headers.srtp.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.headers.srtp.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
