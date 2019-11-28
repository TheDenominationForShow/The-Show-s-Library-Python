# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ShowLibInterface.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ShowLibInterface.proto',
  package='ShowLibInterface',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16ShowLibInterface.proto\x12\x10ShowLibInterface\"Q\n\tMsgHeader\x12\x0f\n\x07localid\x18\x01 \x01(\t\x12\x0e\n\x06peerid\x18\x02 \x01(\t\x12\x12\n\nsenssionid\x18\x03 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\x05\"G\n\nCommandMsg\x12+\n\x06header\x18\x01 \x01(\x0b\x32\x1b.ShowLibInterface.MsgHeader\x12\x0c\n\x04hash\x18\x02 \x03(\t\"8\n\x0cRCHashRecord\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\t\"l\n\rRCHashRecords\x12+\n\x06header\x18\x01 \x01(\x0b\x32\x1b.ShowLibInterface.MsgHeader\x12.\n\x06record\x18\x02 \x03(\x0b\x32\x1e.ShowLibInterface.RCHashRecord\"I\n\x0bRecordCount\x12+\n\x06header\x18\x01 \x01(\x0b\x32\x1b.ShowLibInterface.MsgHeader\x12\r\n\x05\x43ount\x18\x02 \x01(\x05\"o\n\tFileBlock\x12*\n\x05hader\x18\x01 \x01(\x0b\x32\x1b.ShowLibInterface.MsgHeader\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12(\n\x06rcByte\x18\x03 \x01(\x0b\x32\x18.ShowLibInterface.RCByte\"(\n\x06RCByte\x12\x0f\n\x07\x62lockid\x18\x01 \x01(\t\x12\r\n\x05\x62lock\x18\x02 \x01(\x0c\x32\x9d\x05\n\tshowlibif\x12G\n\x07\x63ommand\x12\x1c.ShowLibInterface.CommandMsg\x1a\x1c.ShowLibInterface.CommandMsg\"\x00\x12Y\n\x13InsertRCHashRecords\x12\x1e.ShowLibInterface.RCHashRecord\x1a\x1c.ShowLibInterface.CommandMsg\"\x00(\x01\x30\x01\x12R\n\x11PulishRCHashCount\x12\x1d.ShowLibInterface.RecordCount\x1a\x1c.ShowLibInterface.CommandMsg\"\x00\x12X\n\x13PulishRCHashRecords\x12\x1f.ShowLibInterface.RCHashRecords\x1a\x1c.ShowLibInterface.CommandMsg\"\x00(\x01\x12O\n\x0eGetRCHashCount\x12\x1c.ShowLibInterface.CommandMsg\x1a\x1d.ShowLibInterface.RecordCount\"\x00\x12U\n\x10GetRCHashRecords\x12\x1c.ShowLibInterface.CommandMsg\x1a\x1f.ShowLibInterface.RCHashRecords\"\x00\x30\x01\x12K\n\nDownLoadRC\x12\x1c.ShowLibInterface.CommandMsg\x1a\x1b.ShowLibInterface.FileBlock\"\x00\x30\x01\x12I\n\x08UpLoadRC\x12\x1b.ShowLibInterface.FileBlock\x1a\x1c.ShowLibInterface.CommandMsg\"\x00(\x01\x62\x06proto3')
)




_MSGHEADER = _descriptor.Descriptor(
  name='MsgHeader',
  full_name='ShowLibInterface.MsgHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='localid', full_name='ShowLibInterface.MsgHeader.localid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peerid', full_name='ShowLibInterface.MsgHeader.peerid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='senssionid', full_name='ShowLibInterface.MsgHeader.senssionid', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='command', full_name='ShowLibInterface.MsgHeader.command', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=44,
  serialized_end=125,
)


_COMMANDMSG = _descriptor.Descriptor(
  name='CommandMsg',
  full_name='ShowLibInterface.CommandMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='ShowLibInterface.CommandMsg.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ShowLibInterface.CommandMsg.hash', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=127,
  serialized_end=198,
)


_RCHASHRECORD = _descriptor.Descriptor(
  name='RCHashRecord',
  full_name='ShowLibInterface.RCHashRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ShowLibInterface.RCHashRecord.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ShowLibInterface.RCHashRecord.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='ShowLibInterface.RCHashRecord.size', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=200,
  serialized_end=256,
)


_RCHASHRECORDS = _descriptor.Descriptor(
  name='RCHashRecords',
  full_name='ShowLibInterface.RCHashRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='ShowLibInterface.RCHashRecords.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='ShowLibInterface.RCHashRecords.record', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=258,
  serialized_end=366,
)


_RECORDCOUNT = _descriptor.Descriptor(
  name='RecordCount',
  full_name='ShowLibInterface.RecordCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='ShowLibInterface.RecordCount.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Count', full_name='ShowLibInterface.RecordCount.Count', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=368,
  serialized_end=441,
)


_FILEBLOCK = _descriptor.Descriptor(
  name='FileBlock',
  full_name='ShowLibInterface.FileBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hader', full_name='ShowLibInterface.FileBlock.hader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ShowLibInterface.FileBlock.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rcByte', full_name='ShowLibInterface.FileBlock.rcByte', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=443,
  serialized_end=554,
)


_RCBYTE = _descriptor.Descriptor(
  name='RCByte',
  full_name='ShowLibInterface.RCByte',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='blockid', full_name='ShowLibInterface.RCByte.blockid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='ShowLibInterface.RCByte.block', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=556,
  serialized_end=596,
)

_COMMANDMSG.fields_by_name['header'].message_type = _MSGHEADER
_RCHASHRECORDS.fields_by_name['header'].message_type = _MSGHEADER
_RCHASHRECORDS.fields_by_name['record'].message_type = _RCHASHRECORD
_RECORDCOUNT.fields_by_name['header'].message_type = _MSGHEADER
_FILEBLOCK.fields_by_name['hader'].message_type = _MSGHEADER
_FILEBLOCK.fields_by_name['rcByte'].message_type = _RCBYTE
DESCRIPTOR.message_types_by_name['MsgHeader'] = _MSGHEADER
DESCRIPTOR.message_types_by_name['CommandMsg'] = _COMMANDMSG
DESCRIPTOR.message_types_by_name['RCHashRecord'] = _RCHASHRECORD
DESCRIPTOR.message_types_by_name['RCHashRecords'] = _RCHASHRECORDS
DESCRIPTOR.message_types_by_name['RecordCount'] = _RECORDCOUNT
DESCRIPTOR.message_types_by_name['FileBlock'] = _FILEBLOCK
DESCRIPTOR.message_types_by_name['RCByte'] = _RCBYTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgHeader = _reflection.GeneratedProtocolMessageType('MsgHeader', (_message.Message,), {
  'DESCRIPTOR' : _MSGHEADER,
  '__module__' : 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.MsgHeader)
  })
_sym_db.RegisterMessage(MsgHeader)

CommandMsg = _reflection.GeneratedProtocolMessageType('CommandMsg', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDMSG,
  '__module__' : 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.CommandMsg)
  })
_sym_db.RegisterMessage(CommandMsg)

RCHashRecord = _reflection.GeneratedProtocolMessageType('RCHashRecord', (_message.Message,), {
  'DESCRIPTOR' : _RCHASHRECORD,
  '__module__' : 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.RCHashRecord)
  })
_sym_db.RegisterMessage(RCHashRecord)

RCHashRecords = _reflection.GeneratedProtocolMessageType('RCHashRecords', (_message.Message,), {
  'DESCRIPTOR' : _RCHASHRECORDS,
  '__module__' : 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.RCHashRecords)
  })
_sym_db.RegisterMessage(RCHashRecords)

RecordCount = _reflection.GeneratedProtocolMessageType('RecordCount', (_message.Message,), {
  'DESCRIPTOR' : _RECORDCOUNT,
  '__module__' : 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.RecordCount)
  })
_sym_db.RegisterMessage(RecordCount)

FileBlock = _reflection.GeneratedProtocolMessageType('FileBlock', (_message.Message,), {
  'DESCRIPTOR' : _FILEBLOCK,
  '__module__' : 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.FileBlock)
  })
_sym_db.RegisterMessage(FileBlock)

RCByte = _reflection.GeneratedProtocolMessageType('RCByte', (_message.Message,), {
  'DESCRIPTOR' : _RCBYTE,
  '__module__' : 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.RCByte)
  })
_sym_db.RegisterMessage(RCByte)



_SHOWLIBIF = _descriptor.ServiceDescriptor(
  name='showlibif',
  full_name='ShowLibInterface.showlibif',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=599,
  serialized_end=1268,
  methods=[
  _descriptor.MethodDescriptor(
    name='command',
    full_name='ShowLibInterface.showlibif.command',
    index=0,
    containing_service=None,
    input_type=_COMMANDMSG,
    output_type=_COMMANDMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InsertRCHashRecords',
    full_name='ShowLibInterface.showlibif.InsertRCHashRecords',
    index=1,
    containing_service=None,
    input_type=_RCHASHRECORD,
    output_type=_COMMANDMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PulishRCHashCount',
    full_name='ShowLibInterface.showlibif.PulishRCHashCount',
    index=2,
    containing_service=None,
    input_type=_RECORDCOUNT,
    output_type=_COMMANDMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PulishRCHashRecords',
    full_name='ShowLibInterface.showlibif.PulishRCHashRecords',
    index=3,
    containing_service=None,
    input_type=_RCHASHRECORDS,
    output_type=_COMMANDMSG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRCHashCount',
    full_name='ShowLibInterface.showlibif.GetRCHashCount',
    index=4,
    containing_service=None,
    input_type=_COMMANDMSG,
    output_type=_RECORDCOUNT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRCHashRecords',
    full_name='ShowLibInterface.showlibif.GetRCHashRecords',
    index=5,
    containing_service=None,
    input_type=_COMMANDMSG,
    output_type=_RCHASHRECORDS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DownLoadRC',
    full_name='ShowLibInterface.showlibif.DownLoadRC',
    index=6,
    containing_service=None,
    input_type=_COMMANDMSG,
    output_type=_FILEBLOCK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpLoadRC',
    full_name='ShowLibInterface.showlibif.UpLoadRC',
    index=7,
    containing_service=None,
    input_type=_FILEBLOCK,
    output_type=_COMMANDMSG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHOWLIBIF)

DESCRIPTOR.services_by_name['showlibif'] = _SHOWLIBIF

# @@protoc_insertion_point(module_scope)
