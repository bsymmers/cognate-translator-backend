# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: languagedetect.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14languagedetect.proto\"\x1a\n\nLanRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1c\n\x08LanReply\x12\x10\n\x08response\x18\x01 \x01(\t27\n\x0eLanguageDetect\x12%\n\x0bGetLanguage\x12\x0b.LanRequest\x1a\t.LanReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'languagedetect_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LANREQUEST']._serialized_start=24
  _globals['_LANREQUEST']._serialized_end=50
  _globals['_LANREPLY']._serialized_start=52
  _globals['_LANREPLY']._serialized_end=80
  _globals['_LANGUAGEDETECT']._serialized_start=82
  _globals['_LANGUAGEDETECT']._serialized_end=137
# @@protoc_insertion_point(module_scope)