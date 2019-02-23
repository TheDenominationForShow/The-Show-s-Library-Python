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
  serialized_pb=_b('\n\x16ShowLibInterface.proto\x12\x10ShowLibInterface\"G\n\x0cRCHashRecord\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\t\x12\r\n\x05mtime\x18\x04 \x01(\t\"T\n\rRCLabelRecord\x12\r\n\x05lable\x18\x01 \x01(\t\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0b\n\x03pro\x18\x04 \x01(\x05\x12\x0b\n\x03\x63om\x18\x05 \x01(\x05\"\x1c\n\x0bRecordCount\x12\r\n\x05\x43ount\x18\x01 \x01(\x05\"n\n\x06Result\x12\x30\n\x03RET\x18\x01 \x01(\x0e\x32#.ShowLibInterface.Result.ResultType\"2\n\nResultType\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x12\r\n\tHAS_EXIST\x10\x02\x32\xd1\x02\n\x07Greeter\x12P\n\x12InsertRCHashRecord\x12\x1e.ShowLibInterface.RCHashRecord\x1a\x18.ShowLibInterface.Result\"\x00\x12U\n\x13InsertRCHashRecords\x12\x1e.ShowLibInterface.RCHashRecord\x1a\x18.ShowLibInterface.Result\"\x00(\x01\x30\x01\x12K\n\x0eGetRCHashCount\x12\x18.ShowLibInterface.Result\x1a\x1d.ShowLibInterface.RecordCount\"\x00\x12P\n\x10GetRCHashRecords\x12\x18.ShowLibInterface.Result\x1a\x1e.ShowLibInterface.RCHashRecord\"\x00\x30\x01\x62\x06proto3')
)



_RESULT_RESULTTYPE = _descriptor.EnumDescriptor(
  name='ResultType',
  full_name='ShowLibInterface.Result.ResultType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HAS_EXIST', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=293,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_RESULT_RESULTTYPE)


_RCHASHRECORD = _descriptor.Descriptor(
  name='RCHashRecord',
  full_name='ShowLibInterface.RCHashRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='ShowLibInterface.RCHashRecord.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ShowLibInterface.RCHashRecord.name', index=1,
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
    _descriptor.FieldDescriptor(
      name='mtime', full_name='ShowLibInterface.RCHashRecord.mtime', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=44,
  serialized_end=115,
)


_RCLABELRECORD = _descriptor.Descriptor(
  name='RCLabelRecord',
  full_name='ShowLibInterface.RCLabelRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lable', full_name='ShowLibInterface.RCLabelRecord.lable', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ShowLibInterface.RCLabelRecord.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='ShowLibInterface.RCLabelRecord.desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pro', full_name='ShowLibInterface.RCLabelRecord.pro', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='com', full_name='ShowLibInterface.RCLabelRecord.com', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=117,
  serialized_end=201,
)


_RECORDCOUNT = _descriptor.Descriptor(
  name='RecordCount',
  full_name='ShowLibInterface.RecordCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Count', full_name='ShowLibInterface.RecordCount.Count', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=203,
  serialized_end=231,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='ShowLibInterface.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RET', full_name='ShowLibInterface.Result.RET', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESULT_RESULTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=343,
)

_RESULT.fields_by_name['RET'].enum_type = _RESULT_RESULTTYPE
_RESULT_RESULTTYPE.containing_type = _RESULT
DESCRIPTOR.message_types_by_name['RCHashRecord'] = _RCHASHRECORD
DESCRIPTOR.message_types_by_name['RCLabelRecord'] = _RCLABELRECORD
DESCRIPTOR.message_types_by_name['RecordCount'] = _RECORDCOUNT
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RCHashRecord = _reflection.GeneratedProtocolMessageType('RCHashRecord', (_message.Message,), dict(
  DESCRIPTOR = _RCHASHRECORD,
  __module__ = 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.RCHashRecord)
  ))
_sym_db.RegisterMessage(RCHashRecord)

RCLabelRecord = _reflection.GeneratedProtocolMessageType('RCLabelRecord', (_message.Message,), dict(
  DESCRIPTOR = _RCLABELRECORD,
  __module__ = 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.RCLabelRecord)
  ))
_sym_db.RegisterMessage(RCLabelRecord)

RecordCount = _reflection.GeneratedProtocolMessageType('RecordCount', (_message.Message,), dict(
  DESCRIPTOR = _RECORDCOUNT,
  __module__ = 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.RecordCount)
  ))
_sym_db.RegisterMessage(RecordCount)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'ShowLibInterface_pb2'
  # @@protoc_insertion_point(class_scope:ShowLibInterface.Result)
  ))
_sym_db.RegisterMessage(Result)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='ShowLibInterface.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=346,
  serialized_end=683,
  methods=[
  _descriptor.MethodDescriptor(
    name='InsertRCHashRecord',
    full_name='ShowLibInterface.Greeter.InsertRCHashRecord',
    index=0,
    containing_service=None,
    input_type=_RCHASHRECORD,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='InsertRCHashRecords',
    full_name='ShowLibInterface.Greeter.InsertRCHashRecords',
    index=1,
    containing_service=None,
    input_type=_RCHASHRECORD,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRCHashCount',
    full_name='ShowLibInterface.Greeter.GetRCHashCount',
    index=2,
    containing_service=None,
    input_type=_RESULT,
    output_type=_RECORDCOUNT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetRCHashRecords',
    full_name='ShowLibInterface.Greeter.GetRCHashRecords',
    index=3,
    containing_service=None,
    input_type=_RESULT,
    output_type=_RCHASHRECORD,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
