# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task_controller/gen/task_controller.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='task_controller/gen/task_controller.proto',
  package='TaskController',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n)task_controller/gen/task_controller.proto\x12\x0eTaskController\"H\n\x17\x41\x64\x64\x43ustomLogCallbackReq\x12-\n\ncustom_log\x18\x01 \x01(\x0b\x32\x19.TaskController.CustomLog\"B\n\x18\x41\x64\x64\x43ustomLogCallbackResp\x12&\n\x04resp\x18\x01 \x01(\x0b\x32\x18.TaskController.Response\";\n\tCustomLog\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\"0\n\nAddTaskReq\x12\"\n\x04task\x18\x01 \x01(\x0b\x32\x14.TaskController.Task\"5\n\x0b\x41\x64\x64TaskResp\x12&\n\x04resp\x18\x01 \x01(\x0b\x32\x18.TaskController.Response\"\x1e\n\x0bStopTaskReq\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\"6\n\x0cStopTaskResp\x12&\n\x04resp\x18\x01 \x01(\x0b\x32\x18.TaskController.Response\"\x10\n\x0eGetAllTasksReq\"9\n\x0fGetAllTasksResp\x12&\n\x04resp\x18\x01 \x01(\x0b\x32\x18.TaskController.Response\"!\n\x0eGetTaskInfoReq\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\"]\n\x0fGetTaskInfoResp\x12&\n\x04resp\x18\x01 \x01(\x0b\x32\x18.TaskController.Response\x12\"\n\x04task\x18\x02 \x01(\x0b\x32\x14.TaskController.Task\"3\n\rUpdateTaskReq\x12\"\n\x04task\x18\x01 \x01(\x0b\x32\x14.TaskController.Task\"8\n\x0eUpdateTaskResp\x12&\n\x04resp\x18\x01 \x01(\x0b\x32\x18.TaskController.Response\"\x84\x01\n\x04Task\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\x05\x12\x12\n\nstart_time\x18\x04 \x01(\x05\x12\x13\n\x0bunion_train\x18\x05 \x01(\x05\x12\x11\n\tedgenodes\x18\x06 \x01(\t\x12\x0c\n\x04\x66ile\x18\x07 \x01(\t\")\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2\xff\x03\n\x0eTaskController\x12\x44\n\x07\x41\x64\x64Task\x12\x1a.TaskController.AddTaskReq\x1a\x1b.TaskController.AddTaskResp\"\x00\x12G\n\x08StopTask\x12\x1b.TaskController.StopTaskReq\x1a\x1c.TaskController.StopTaskResp\"\x00\x12P\n\x0bGetAllTasks\x12\x1e.TaskController.GetAllTasksReq\x1a\x1f.TaskController.GetAllTasksResp\"\x00\x12P\n\x0bGetTaskInfo\x12\x1e.TaskController.GetTaskInfoReq\x1a\x1f.TaskController.GetTaskInfoResp\"\x00\x12M\n\nUpdateTask\x12\x1d.TaskController.UpdateTaskReq\x1a\x1e.TaskController.UpdateTaskResp\"\x00\x12k\n\x14\x41\x64\x64\x43ustomLogCallback\x12\'.TaskController.AddCustomLogCallbackReq\x1a(.TaskController.AddCustomLogCallbackResp\"\x00\x62\x06proto3'
)




_ADDCUSTOMLOGCALLBACKREQ = _descriptor.Descriptor(
  name='AddCustomLogCallbackReq',
  full_name='TaskController.AddCustomLogCallbackReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='custom_log', full_name='TaskController.AddCustomLogCallbackReq.custom_log', index=0,
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
  serialized_start=61,
  serialized_end=133,
)


_ADDCUSTOMLOGCALLBACKRESP = _descriptor.Descriptor(
  name='AddCustomLogCallbackResp',
  full_name='TaskController.AddCustomLogCallbackResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='TaskController.AddCustomLogCallbackResp.resp', index=0,
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
  serialized_start=135,
  serialized_end=201,
)


_CUSTOMLOG = _descriptor.Descriptor(
  name='CustomLog',
  full_name='TaskController.CustomLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='TaskController.CustomLog.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='TaskController.CustomLog.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='TaskController.CustomLog.time', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_end=262,
)


_ADDTASKREQ = _descriptor.Descriptor(
  name='AddTaskReq',
  full_name='TaskController.AddTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='TaskController.AddTaskReq.task', index=0,
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
  serialized_start=264,
  serialized_end=312,
)


_ADDTASKRESP = _descriptor.Descriptor(
  name='AddTaskResp',
  full_name='TaskController.AddTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='TaskController.AddTaskResp.resp', index=0,
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
  serialized_start=314,
  serialized_end=367,
)


_STOPTASKREQ = _descriptor.Descriptor(
  name='StopTaskReq',
  full_name='TaskController.StopTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='TaskController.StopTaskReq.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=369,
  serialized_end=399,
)


_STOPTASKRESP = _descriptor.Descriptor(
  name='StopTaskResp',
  full_name='TaskController.StopTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='TaskController.StopTaskResp.resp', index=0,
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
  serialized_start=401,
  serialized_end=455,
)


_GETALLTASKSREQ = _descriptor.Descriptor(
  name='GetAllTasksReq',
  full_name='TaskController.GetAllTasksReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=457,
  serialized_end=473,
)


_GETALLTASKSRESP = _descriptor.Descriptor(
  name='GetAllTasksResp',
  full_name='TaskController.GetAllTasksResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='TaskController.GetAllTasksResp.resp', index=0,
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
  serialized_start=475,
  serialized_end=532,
)


_GETTASKINFOREQ = _descriptor.Descriptor(
  name='GetTaskInfoReq',
  full_name='TaskController.GetTaskInfoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='TaskController.GetTaskInfoReq.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=534,
  serialized_end=567,
)


_GETTASKINFORESP = _descriptor.Descriptor(
  name='GetTaskInfoResp',
  full_name='TaskController.GetTaskInfoResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='TaskController.GetTaskInfoResp.resp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task', full_name='TaskController.GetTaskInfoResp.task', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=569,
  serialized_end=662,
)


_UPDATETASKREQ = _descriptor.Descriptor(
  name='UpdateTaskReq',
  full_name='TaskController.UpdateTaskReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='TaskController.UpdateTaskReq.task', index=0,
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
  serialized_start=664,
  serialized_end=715,
)


_UPDATETASKRESP = _descriptor.Descriptor(
  name='UpdateTaskResp',
  full_name='TaskController.UpdateTaskResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resp', full_name='TaskController.UpdateTaskResp.resp', index=0,
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
  serialized_start=717,
  serialized_end=773,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='TaskController.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='TaskController.Task.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='TaskController.Task.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='TaskController.Task.create_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='TaskController.Task.start_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='union_train', full_name='TaskController.Task.union_train', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edgenodes', full_name='TaskController.Task.edgenodes', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file', full_name='TaskController.Task.file', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=776,
  serialized_end=908,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='TaskController.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='TaskController.Response.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='TaskController.Response.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=910,
  serialized_end=951,
)

_ADDCUSTOMLOGCALLBACKREQ.fields_by_name['custom_log'].message_type = _CUSTOMLOG
_ADDCUSTOMLOGCALLBACKRESP.fields_by_name['resp'].message_type = _RESPONSE
_ADDTASKREQ.fields_by_name['task'].message_type = _TASK
_ADDTASKRESP.fields_by_name['resp'].message_type = _RESPONSE
_STOPTASKRESP.fields_by_name['resp'].message_type = _RESPONSE
_GETALLTASKSRESP.fields_by_name['resp'].message_type = _RESPONSE
_GETTASKINFORESP.fields_by_name['resp'].message_type = _RESPONSE
_GETTASKINFORESP.fields_by_name['task'].message_type = _TASK
_UPDATETASKREQ.fields_by_name['task'].message_type = _TASK
_UPDATETASKRESP.fields_by_name['resp'].message_type = _RESPONSE
DESCRIPTOR.message_types_by_name['AddCustomLogCallbackReq'] = _ADDCUSTOMLOGCALLBACKREQ
DESCRIPTOR.message_types_by_name['AddCustomLogCallbackResp'] = _ADDCUSTOMLOGCALLBACKRESP
DESCRIPTOR.message_types_by_name['CustomLog'] = _CUSTOMLOG
DESCRIPTOR.message_types_by_name['AddTaskReq'] = _ADDTASKREQ
DESCRIPTOR.message_types_by_name['AddTaskResp'] = _ADDTASKRESP
DESCRIPTOR.message_types_by_name['StopTaskReq'] = _STOPTASKREQ
DESCRIPTOR.message_types_by_name['StopTaskResp'] = _STOPTASKRESP
DESCRIPTOR.message_types_by_name['GetAllTasksReq'] = _GETALLTASKSREQ
DESCRIPTOR.message_types_by_name['GetAllTasksResp'] = _GETALLTASKSRESP
DESCRIPTOR.message_types_by_name['GetTaskInfoReq'] = _GETTASKINFOREQ
DESCRIPTOR.message_types_by_name['GetTaskInfoResp'] = _GETTASKINFORESP
DESCRIPTOR.message_types_by_name['UpdateTaskReq'] = _UPDATETASKREQ
DESCRIPTOR.message_types_by_name['UpdateTaskResp'] = _UPDATETASKRESP
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddCustomLogCallbackReq = _reflection.GeneratedProtocolMessageType('AddCustomLogCallbackReq', (_message.Message,), {
  'DESCRIPTOR' : _ADDCUSTOMLOGCALLBACKREQ,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.AddCustomLogCallbackReq)
  })
_sym_db.RegisterMessage(AddCustomLogCallbackReq)

AddCustomLogCallbackResp = _reflection.GeneratedProtocolMessageType('AddCustomLogCallbackResp', (_message.Message,), {
  'DESCRIPTOR' : _ADDCUSTOMLOGCALLBACKRESP,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.AddCustomLogCallbackResp)
  })
_sym_db.RegisterMessage(AddCustomLogCallbackResp)

CustomLog = _reflection.GeneratedProtocolMessageType('CustomLog', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMLOG,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.CustomLog)
  })
_sym_db.RegisterMessage(CustomLog)

AddTaskReq = _reflection.GeneratedProtocolMessageType('AddTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _ADDTASKREQ,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.AddTaskReq)
  })
_sym_db.RegisterMessage(AddTaskReq)

AddTaskResp = _reflection.GeneratedProtocolMessageType('AddTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _ADDTASKRESP,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.AddTaskResp)
  })
_sym_db.RegisterMessage(AddTaskResp)

StopTaskReq = _reflection.GeneratedProtocolMessageType('StopTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _STOPTASKREQ,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.StopTaskReq)
  })
_sym_db.RegisterMessage(StopTaskReq)

StopTaskResp = _reflection.GeneratedProtocolMessageType('StopTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _STOPTASKRESP,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.StopTaskResp)
  })
_sym_db.RegisterMessage(StopTaskResp)

GetAllTasksReq = _reflection.GeneratedProtocolMessageType('GetAllTasksReq', (_message.Message,), {
  'DESCRIPTOR' : _GETALLTASKSREQ,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.GetAllTasksReq)
  })
_sym_db.RegisterMessage(GetAllTasksReq)

GetAllTasksResp = _reflection.GeneratedProtocolMessageType('GetAllTasksResp', (_message.Message,), {
  'DESCRIPTOR' : _GETALLTASKSRESP,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.GetAllTasksResp)
  })
_sym_db.RegisterMessage(GetAllTasksResp)

GetTaskInfoReq = _reflection.GeneratedProtocolMessageType('GetTaskInfoReq', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKINFOREQ,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.GetTaskInfoReq)
  })
_sym_db.RegisterMessage(GetTaskInfoReq)

GetTaskInfoResp = _reflection.GeneratedProtocolMessageType('GetTaskInfoResp', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKINFORESP,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.GetTaskInfoResp)
  })
_sym_db.RegisterMessage(GetTaskInfoResp)

UpdateTaskReq = _reflection.GeneratedProtocolMessageType('UpdateTaskReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETASKREQ,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.UpdateTaskReq)
  })
_sym_db.RegisterMessage(UpdateTaskReq)

UpdateTaskResp = _reflection.GeneratedProtocolMessageType('UpdateTaskResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETASKRESP,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.UpdateTaskResp)
  })
_sym_db.RegisterMessage(UpdateTaskResp)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.Task)
  })
_sym_db.RegisterMessage(Task)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'task_controller.gen.task_controller_pb2'
  # @@protoc_insertion_point(class_scope:TaskController.Response)
  })
_sym_db.RegisterMessage(Response)



_TASKCONTROLLER = _descriptor.ServiceDescriptor(
  name='TaskController',
  full_name='TaskController.TaskController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=954,
  serialized_end=1465,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddTask',
    full_name='TaskController.TaskController.AddTask',
    index=0,
    containing_service=None,
    input_type=_ADDTASKREQ,
    output_type=_ADDTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopTask',
    full_name='TaskController.TaskController.StopTask',
    index=1,
    containing_service=None,
    input_type=_STOPTASKREQ,
    output_type=_STOPTASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllTasks',
    full_name='TaskController.TaskController.GetAllTasks',
    index=2,
    containing_service=None,
    input_type=_GETALLTASKSREQ,
    output_type=_GETALLTASKSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTaskInfo',
    full_name='TaskController.TaskController.GetTaskInfo',
    index=3,
    containing_service=None,
    input_type=_GETTASKINFOREQ,
    output_type=_GETTASKINFORESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTask',
    full_name='TaskController.TaskController.UpdateTask',
    index=4,
    containing_service=None,
    input_type=_UPDATETASKREQ,
    output_type=_UPDATETASKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddCustomLogCallback',
    full_name='TaskController.TaskController.AddCustomLogCallback',
    index=5,
    containing_service=None,
    input_type=_ADDCUSTOMLOGCALLBACKREQ,
    output_type=_ADDCUSTOMLOGCALLBACKRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKCONTROLLER)

DESCRIPTOR.services_by_name['TaskController'] = _TASKCONTROLLER

# @@protoc_insertion_point(module_scope)
