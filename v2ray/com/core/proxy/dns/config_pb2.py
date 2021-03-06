# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/proxy/dns/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.net import destination_pb2 as v2ray_dot_com_dot_core_dot_common_dot_net_dot_destination__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/proxy/dns/config.proto',
  package='v2ray.core.proxy.dns',
  syntax='proto3',
  serialized_options=_b('\n\030com.v2ray.core.proxy.dnsP\001Z\003dns\252\002\024V2Ray.Core.Proxy.Dns'),
  serialized_pb=_b('\n%v2ray.com/core/proxy/dns/config.proto\x12\x14v2ray.core.proxy.dns\x1a+v2ray.com/core/common/net/destination.proto\"9\n\x06\x43onfig\x12/\n\x06server\x18\x01 \x01(\x0b\x32\x1f.v2ray.core.common.net.EndpointB8\n\x18\x63om.v2ray.core.proxy.dnsP\x01Z\x03\x64ns\xaa\x02\x14V2Ray.Core.Proxy.Dnsb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_net_dot_destination__pb2.DESCRIPTOR,])




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.proxy.dns.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='v2ray.core.proxy.dns.Config.server', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=108,
  serialized_end=165,
)

_CONFIG.fields_by_name['server'].message_type = v2ray_dot_com_dot_core_dot_common_dot_net_dot_destination__pb2._ENDPOINT
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'v2ray.com.core.proxy.dns.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.dns.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
