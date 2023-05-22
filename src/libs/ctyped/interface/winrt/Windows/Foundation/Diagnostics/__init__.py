from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAsyncCausalityTracerStatics(_inspectable.IInspectable, factory=True):
    TraceOperationCreation: _Callable[[_enum.Windows.Foundation.Diagnostics.CausalityTraceLevel,  # traceLevel
                                       _enum.Windows.Foundation.Diagnostics.CausalitySource,  # source
                                       _struct.GUID,  # platformId
                                       _type.UINT64,  # operationId
                                       _type.HSTRING,  # operationName
                                       _type.UINT64],  # relatedContext
                                      _type.HRESULT]
    TraceOperationCompletion: _Callable[[_enum.Windows.Foundation.Diagnostics.CausalityTraceLevel,  # traceLevel
                                         _enum.Windows.Foundation.Diagnostics.CausalitySource,  # source
                                         _struct.GUID,  # platformId
                                         _type.UINT64,  # operationId
                                         _enum.Windows.Foundation.AsyncStatus],  # status
                                        _type.HRESULT]
    TraceOperationRelation: _Callable[[_enum.Windows.Foundation.Diagnostics.CausalityTraceLevel,  # traceLevel
                                       _enum.Windows.Foundation.Diagnostics.CausalitySource,  # source
                                       _struct.GUID,  # platformId
                                       _type.UINT64,  # operationId
                                       _enum.Windows.Foundation.Diagnostics.CausalityRelation],  # relation
                                      _type.HRESULT]
    TraceSynchronousWorkStart: _Callable[[_enum.Windows.Foundation.Diagnostics.CausalityTraceLevel,  # traceLevel
                                          _enum.Windows.Foundation.Diagnostics.CausalitySource,  # source
                                          _struct.GUID,  # platformId
                                          _type.UINT64,  # operationId
                                          _enum.Windows.Foundation.Diagnostics.CausalitySynchronousWork],  # work
                                         _type.HRESULT]
    TraceSynchronousWorkCompletion: _Callable[[_enum.Windows.Foundation.Diagnostics.CausalityTraceLevel,  # traceLevel
                                               _enum.Windows.Foundation.Diagnostics.CausalitySource,  # source
                                               _enum.Windows.Foundation.Diagnostics.CausalitySynchronousWork],  # work
                                              _type.HRESULT]
    add_TracingStatusChanged: _Callable[[_Windows_Foundation.IEventHandler[ITracingStatusChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # cookie
                                        _type.HRESULT]
    remove_TracingStatusChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                           _type.HRESULT]


class IErrorDetails(_inspectable.IInspectable):
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_LongDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_HelpUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]


class IErrorDetailsStatics(_inspectable.IInspectable, factory=True):
    CreateFromHResultAsync: _Callable[[_type.INT32,  # errorCode
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IErrorDetails]]],  # operation
                                      _type.HRESULT]


class IErrorReportingSettings(_inspectable.IInspectable):
    SetErrorOptions: _Callable[[_enum.Windows.Foundation.Diagnostics.ErrorOptions],  # value
                               _type.HRESULT]
    GetErrorOptions: _Callable[[_Pointer[_enum.Windows.Foundation.Diagnostics.ErrorOptions]],  # value
                               _type.HRESULT]


class IFileLoggingSession(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    AddLoggingChannel: _Callable[[ILoggingChannel],  # loggingChannel
                                 _type.HRESULT]
    AddLoggingChannelWithLevel: _Callable[[ILoggingChannel,  # loggingChannel
                                           _enum.Windows.Foundation.Diagnostics.LoggingLevel],  # maxLevel
                                          _type.HRESULT]
    RemoveLoggingChannel: _Callable[[ILoggingChannel],  # loggingChannel
                                    _type.HRESULT]
    CloseAndSaveToFileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                       _type.HRESULT]
    add_LogFileGenerated: _Callable[[_Windows_Foundation.ITypedEventHandler[IFileLoggingSession, ILogFileGeneratedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_LogFileGenerated: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IFileLoggingSessionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # name
                       _Pointer[IFileLoggingSession]],  # result
                      _type.HRESULT]


class ILogFileGeneratedEventArgs(_inspectable.IInspectable):
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]


class ILoggingActivity(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]


class ILoggingActivity2(_inspectable.IInspectable):
    get_Channel: _Callable[[_Pointer[ILoggingChannel]],  # value
                           _type.HRESULT]
    StopActivity: _Callable[[_type.HSTRING],  # stopEventName
                            _type.HRESULT]
    StopActivityWithFields: _Callable[[_type.HSTRING,  # stopEventName
                                       ILoggingFields],  # fields
                                      _type.HRESULT]
    StopActivityWithFieldsAndOptions: _Callable[[_type.HSTRING,  # stopEventName
                                                 ILoggingFields,  # fields
                                                 ILoggingOptions],  # options
                                                _type.HRESULT]


class ILoggingActivityFactory(_inspectable.IInspectable, factory=True):
    CreateLoggingActivity: _Callable[[_type.HSTRING,  # activityName
                                      ILoggingChannel,  # loggingChannel
                                      _Pointer[ILoggingActivity]],  # loggingActivity
                                     _type.HRESULT]
    CreateLoggingActivityWithLevel: _Callable[[_type.HSTRING,  # activityName
                                               ILoggingChannel,  # loggingChannel
                                               _enum.Windows.Foundation.Diagnostics.LoggingLevel,  # level
                                               _Pointer[ILoggingActivity]],  # loggingActivity
                                              _type.HRESULT]


class ILoggingChannel(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Level: _Callable[[_Pointer[_enum.Windows.Foundation.Diagnostics.LoggingLevel]],  # value
                         _type.HRESULT]
    LogMessage: _Callable[[_type.HSTRING],  # eventString
                          _type.HRESULT]
    LogMessageWithLevel: _Callable[[_type.HSTRING,  # eventString
                                    _enum.Windows.Foundation.Diagnostics.LoggingLevel],  # level
                                   _type.HRESULT]
    LogValuePair: _Callable[[_type.HSTRING,  # value1
                             _type.INT32],  # value2
                            _type.HRESULT]
    LogValuePairWithLevel: _Callable[[_type.HSTRING,  # value1
                                      _type.INT32,  # value2
                                      _enum.Windows.Foundation.Diagnostics.LoggingLevel],  # level
                                     _type.HRESULT]
    add_LoggingEnabled: _Callable[[_Windows_Foundation.ITypedEventHandler[ILoggingChannel, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_LoggingEnabled: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class ILoggingChannel2(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]


class ILoggingChannelFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # name
                       _Pointer[ILoggingChannel]],  # result
                      _type.HRESULT]


class ILoggingChannelFactory2(_inspectable.IInspectable, factory=True):
    CreateWithOptions: _Callable[[_type.HSTRING,  # name
                                  ILoggingChannelOptions,  # options
                                  _Pointer[ILoggingChannel]],  # result
                                 _type.HRESULT]
    CreateWithOptionsAndId: _Callable[[_type.HSTRING,  # name
                                       ILoggingChannelOptions,  # options
                                       _struct.GUID,  # id
                                       _Pointer[ILoggingChannel]],  # result
                                      _type.HRESULT]


class ILoggingChannelOptions(_inspectable.IInspectable):
    get_Group: _Callable[[_Pointer[_struct.GUID]],  # value
                         _type.HRESULT]
    put_Group: _Callable[[_struct.GUID],  # value
                         _type.HRESULT]


class ILoggingChannelOptionsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_struct.GUID,  # group
                       _Pointer[ILoggingChannelOptions]],  # result
                      _type.HRESULT]


class ILoggingFields(_inspectable.IInspectable):
    Clear: _Callable[[],
                     _type.HRESULT]
    BeginStruct: _Callable[[_type.HSTRING],  # name
                           _type.HRESULT]
    BeginStructWithTags: _Callable[[_type.HSTRING,  # name
                                    _type.INT32],  # tags
                                   _type.HRESULT]
    EndStruct: _Callable[[],
                         _type.HRESULT]
    AddEmpty: _Callable[[_type.HSTRING],  # name
                        _type.HRESULT]
    AddEmptyWithFormat: _Callable[[_type.HSTRING,  # name
                                   _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                  _type.HRESULT]
    AddEmptyWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                          _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                          _type.INT32],  # tags
                                         _type.HRESULT]
    AddUInt8: _Callable[[_type.HSTRING,  # name
                         _type.BYTE],  # value
                        _type.HRESULT]
    AddUInt8WithFormat: _Callable[[_type.HSTRING,  # name
                                   _type.BYTE,  # value
                                   _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                  _type.HRESULT]
    AddUInt8WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                          _type.BYTE,  # value
                                          _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                          _type.INT32],  # tags
                                         _type.HRESULT]
    AddUInt8Array: _Callable[[_type.HSTRING,  # name
                              _type.UINT32,  # __valueSize
                              _Pointer[_type.BYTE]],  # value
                             _type.HRESULT]
    AddUInt8ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                        _type.UINT32,  # __valueSize
                                        _Pointer[_type.BYTE],  # value
                                        _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                       _type.HRESULT]
    AddUInt8ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                               _type.UINT32,  # __valueSize
                                               _Pointer[_type.BYTE],  # value
                                               _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                               _type.INT32],  # tags
                                              _type.HRESULT]
    AddInt16: _Callable[[_type.HSTRING,  # name
                         _type.INT16],  # value
                        _type.HRESULT]
    AddInt16WithFormat: _Callable[[_type.HSTRING,  # name
                                   _type.INT16,  # value
                                   _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                  _type.HRESULT]
    AddInt16WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                          _type.INT16,  # value
                                          _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                          _type.INT32],  # tags
                                         _type.HRESULT]
    AddInt16Array: _Callable[[_type.HSTRING,  # name
                              _type.UINT32,  # __valueSize
                              _Pointer[_type.INT16]],  # value
                             _type.HRESULT]
    AddInt16ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                        _type.UINT32,  # __valueSize
                                        _Pointer[_type.INT16],  # value
                                        _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                       _type.HRESULT]
    AddInt16ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                               _type.UINT32,  # __valueSize
                                               _Pointer[_type.INT16],  # value
                                               _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                               _type.INT32],  # tags
                                              _type.HRESULT]
    AddUInt16: _Callable[[_type.HSTRING,  # name
                          _type.UINT16],  # value
                         _type.HRESULT]
    AddUInt16WithFormat: _Callable[[_type.HSTRING,  # name
                                    _type.UINT16,  # value
                                    _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                   _type.HRESULT]
    AddUInt16WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                           _type.UINT16,  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                           _type.INT32],  # tags
                                          _type.HRESULT]
    AddUInt16Array: _Callable[[_type.HSTRING,  # name
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.UINT16]],  # value
                              _type.HRESULT]
    AddUInt16ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                         _type.UINT32,  # __valueSize
                                         _Pointer[_type.UINT16],  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                        _type.HRESULT]
    AddUInt16ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                _type.UINT32,  # __valueSize
                                                _Pointer[_type.UINT16],  # value
                                                _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                _type.INT32],  # tags
                                               _type.HRESULT]
    AddInt32: _Callable[[_type.HSTRING,  # name
                         _type.INT32],  # value
                        _type.HRESULT]
    AddInt32WithFormat: _Callable[[_type.HSTRING,  # name
                                   _type.INT32,  # value
                                   _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                  _type.HRESULT]
    AddInt32WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                          _type.INT32,  # value
                                          _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                          _type.INT32],  # tags
                                         _type.HRESULT]
    AddInt32Array: _Callable[[_type.HSTRING,  # name
                              _type.UINT32,  # __valueSize
                              _Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    AddInt32ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                        _type.UINT32,  # __valueSize
                                        _Pointer[_type.INT32],  # value
                                        _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                       _type.HRESULT]
    AddInt32ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                               _type.UINT32,  # __valueSize
                                               _Pointer[_type.INT32],  # value
                                               _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                               _type.INT32],  # tags
                                              _type.HRESULT]
    AddUInt32: _Callable[[_type.HSTRING,  # name
                          _type.UINT32],  # value
                         _type.HRESULT]
    AddUInt32WithFormat: _Callable[[_type.HSTRING,  # name
                                    _type.UINT32,  # value
                                    _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                   _type.HRESULT]
    AddUInt32WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                           _type.UINT32,  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                           _type.INT32],  # tags
                                          _type.HRESULT]
    AddUInt32Array: _Callable[[_type.HSTRING,  # name
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    AddUInt32ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                         _type.UINT32,  # __valueSize
                                         _Pointer[_type.UINT32],  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                        _type.HRESULT]
    AddUInt32ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                _type.UINT32,  # __valueSize
                                                _Pointer[_type.UINT32],  # value
                                                _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                _type.INT32],  # tags
                                               _type.HRESULT]
    AddInt64: _Callable[[_type.HSTRING,  # name
                         _type.INT64],  # value
                        _type.HRESULT]
    AddInt64WithFormat: _Callable[[_type.HSTRING,  # name
                                   _type.INT64,  # value
                                   _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                  _type.HRESULT]
    AddInt64WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                          _type.INT64,  # value
                                          _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                          _type.INT32],  # tags
                                         _type.HRESULT]
    AddInt64Array: _Callable[[_type.HSTRING,  # name
                              _type.UINT32,  # __valueSize
                              _Pointer[_type.INT64]],  # value
                             _type.HRESULT]
    AddInt64ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                        _type.UINT32,  # __valueSize
                                        _Pointer[_type.INT64],  # value
                                        _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                       _type.HRESULT]
    AddInt64ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                               _type.UINT32,  # __valueSize
                                               _Pointer[_type.INT64],  # value
                                               _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                               _type.INT32],  # tags
                                              _type.HRESULT]
    AddUInt64: _Callable[[_type.HSTRING,  # name
                          _type.UINT64],  # value
                         _type.HRESULT]
    AddUInt64WithFormat: _Callable[[_type.HSTRING,  # name
                                    _type.UINT64,  # value
                                    _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                   _type.HRESULT]
    AddUInt64WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                           _type.UINT64,  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                           _type.INT32],  # tags
                                          _type.HRESULT]
    AddUInt64Array: _Callable[[_type.HSTRING,  # name
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.UINT64]],  # value
                              _type.HRESULT]
    AddUInt64ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                         _type.UINT32,  # __valueSize
                                         _Pointer[_type.UINT64],  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                        _type.HRESULT]
    AddUInt64ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                _type.UINT32,  # __valueSize
                                                _Pointer[_type.UINT64],  # value
                                                _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                _type.INT32],  # tags
                                               _type.HRESULT]
    AddSingle: _Callable[[_type.HSTRING,  # name
                          _type.FLOAT],  # value
                         _type.HRESULT]
    AddSingleWithFormat: _Callable[[_type.HSTRING,  # name
                                    _type.FLOAT,  # value
                                    _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                   _type.HRESULT]
    AddSingleWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                           _type.FLOAT,  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                           _type.INT32],  # tags
                                          _type.HRESULT]
    AddSingleArray: _Callable[[_type.HSTRING,  # name
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    AddSingleArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                         _type.UINT32,  # __valueSize
                                         _Pointer[_type.FLOAT],  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                        _type.HRESULT]
    AddSingleArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                _type.UINT32,  # __valueSize
                                                _Pointer[_type.FLOAT],  # value
                                                _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                _type.INT32],  # tags
                                               _type.HRESULT]
    AddDouble: _Callable[[_type.HSTRING,  # name
                          _type.DOUBLE],  # value
                         _type.HRESULT]
    AddDoubleWithFormat: _Callable[[_type.HSTRING,  # name
                                    _type.DOUBLE,  # value
                                    _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                   _type.HRESULT]
    AddDoubleWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                           _type.DOUBLE,  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                           _type.INT32],  # tags
                                          _type.HRESULT]
    AddDoubleArray: _Callable[[_type.HSTRING,  # name
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    AddDoubleArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                         _type.UINT32,  # __valueSize
                                         _Pointer[_type.DOUBLE],  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                        _type.HRESULT]
    AddDoubleArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                _type.UINT32,  # __valueSize
                                                _Pointer[_type.DOUBLE],  # value
                                                _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                _type.INT32],  # tags
                                               _type.HRESULT]
    AddChar16: _Callable[[_type.HSTRING,  # name
                          _type.WCHAR],  # value
                         _type.HRESULT]
    AddChar16WithFormat: _Callable[[_type.HSTRING,  # name
                                    _type.WCHAR,  # value
                                    _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                   _type.HRESULT]
    AddChar16WithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                           _type.WCHAR,  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                           _type.INT32],  # tags
                                          _type.HRESULT]
    AddChar16Array: _Callable[[_type.HSTRING,  # name
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.WCHAR]],  # value
                              _type.HRESULT]
    AddChar16ArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                         _type.UINT32,  # __valueSize
                                         _Pointer[_type.WCHAR],  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                        _type.HRESULT]
    AddChar16ArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                _type.UINT32,  # __valueSize
                                                _Pointer[_type.WCHAR],  # value
                                                _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                _type.INT32],  # tags
                                               _type.HRESULT]
    AddBoolean: _Callable[[_type.HSTRING,  # name
                           _type.boolean],  # value
                          _type.HRESULT]
    AddBooleanWithFormat: _Callable[[_type.HSTRING,  # name
                                     _type.boolean,  # value
                                     _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                    _type.HRESULT]
    AddBooleanWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                            _type.boolean,  # value
                                            _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                            _type.INT32],  # tags
                                           _type.HRESULT]
    AddBooleanArray: _Callable[[_type.HSTRING,  # name
                                _type.UINT32,  # __valueSize
                                _Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    AddBooleanArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                          _type.UINT32,  # __valueSize
                                          _Pointer[_type.boolean],  # value
                                          _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                         _type.HRESULT]
    AddBooleanArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                 _type.UINT32,  # __valueSize
                                                 _Pointer[_type.boolean],  # value
                                                 _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                 _type.INT32],  # tags
                                                _type.HRESULT]
    AddString: _Callable[[_type.HSTRING,  # name
                          _type.HSTRING],  # value
                         _type.HRESULT]
    AddStringWithFormat: _Callable[[_type.HSTRING,  # name
                                    _type.HSTRING,  # value
                                    _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                   _type.HRESULT]
    AddStringWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                           _type.HSTRING,  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                           _type.INT32],  # tags
                                          _type.HRESULT]
    AddStringArray: _Callable[[_type.HSTRING,  # name
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    AddStringArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                         _type.UINT32,  # __valueSize
                                         _Pointer[_type.HSTRING],  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                        _type.HRESULT]
    AddStringArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                _type.UINT32,  # __valueSize
                                                _Pointer[_type.HSTRING],  # value
                                                _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                _type.INT32],  # tags
                                               _type.HRESULT]
    AddGuid: _Callable[[_type.HSTRING,  # name
                        _struct.GUID],  # value
                       _type.HRESULT]
    AddGuidWithFormat: _Callable[[_type.HSTRING,  # name
                                  _struct.GUID,  # value
                                  _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                 _type.HRESULT]
    AddGuidWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                         _struct.GUID,  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                         _type.INT32],  # tags
                                        _type.HRESULT]
    AddGuidArray: _Callable[[_type.HSTRING,  # name
                             _type.UINT32,  # __valueSize
                             _Pointer[_struct.GUID]],  # value
                            _type.HRESULT]
    AddGuidArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                       _type.UINT32,  # __valueSize
                                       _Pointer[_struct.GUID],  # value
                                       _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                      _type.HRESULT]
    AddGuidArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                              _type.UINT32,  # __valueSize
                                              _Pointer[_struct.GUID],  # value
                                              _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                              _type.INT32],  # tags
                                             _type.HRESULT]
    AddDateTime: _Callable[[_type.HSTRING,  # name
                            _struct.Windows.Foundation.DateTime],  # value
                           _type.HRESULT]
    AddDateTimeWithFormat: _Callable[[_type.HSTRING,  # name
                                      _struct.Windows.Foundation.DateTime,  # value
                                      _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                     _type.HRESULT]
    AddDateTimeWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                             _struct.Windows.Foundation.DateTime,  # value
                                             _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                             _type.INT32],  # tags
                                            _type.HRESULT]
    AddDateTimeArray: _Callable[[_type.HSTRING,  # name
                                 _type.UINT32,  # __valueSize
                                 _Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    AddDateTimeArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                           _type.UINT32,  # __valueSize
                                           _Pointer[_struct.Windows.Foundation.DateTime],  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                          _type.HRESULT]
    AddDateTimeArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                  _type.UINT32,  # __valueSize
                                                  _Pointer[_struct.Windows.Foundation.DateTime],  # value
                                                  _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                  _type.INT32],  # tags
                                                 _type.HRESULT]
    AddTimeSpan: _Callable[[_type.HSTRING,  # name
                            _struct.Windows.Foundation.TimeSpan],  # value
                           _type.HRESULT]
    AddTimeSpanWithFormat: _Callable[[_type.HSTRING,  # name
                                      _struct.Windows.Foundation.TimeSpan,  # value
                                      _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                     _type.HRESULT]
    AddTimeSpanWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                             _struct.Windows.Foundation.TimeSpan,  # value
                                             _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                             _type.INT32],  # tags
                                            _type.HRESULT]
    AddTimeSpanArray: _Callable[[_type.HSTRING,  # name
                                 _type.UINT32,  # __valueSize
                                 _Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    AddTimeSpanArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                           _type.UINT32,  # __valueSize
                                           _Pointer[_struct.Windows.Foundation.TimeSpan],  # value
                                           _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                          _type.HRESULT]
    AddTimeSpanArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                                  _type.UINT32,  # __valueSize
                                                  _Pointer[_struct.Windows.Foundation.TimeSpan],  # value
                                                  _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                                  _type.INT32],  # tags
                                                 _type.HRESULT]
    AddPoint: _Callable[[_type.HSTRING,  # name
                         _struct.Windows.Foundation.Point],  # value
                        _type.HRESULT]
    AddPointWithFormat: _Callable[[_type.HSTRING,  # name
                                   _struct.Windows.Foundation.Point,  # value
                                   _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                  _type.HRESULT]
    AddPointWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                          _struct.Windows.Foundation.Point,  # value
                                          _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                          _type.INT32],  # tags
                                         _type.HRESULT]
    AddPointArray: _Callable[[_type.HSTRING,  # name
                              _type.UINT32,  # __valueSize
                              _Pointer[_struct.Windows.Foundation.Point]],  # value
                             _type.HRESULT]
    AddPointArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                        _type.UINT32,  # __valueSize
                                        _Pointer[_struct.Windows.Foundation.Point],  # value
                                        _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                       _type.HRESULT]
    AddPointArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                               _type.UINT32,  # __valueSize
                                               _Pointer[_struct.Windows.Foundation.Point],  # value
                                               _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                               _type.INT32],  # tags
                                              _type.HRESULT]
    AddSize: _Callable[[_type.HSTRING,  # name
                        _struct.Windows.Foundation.Size],  # value
                       _type.HRESULT]
    AddSizeWithFormat: _Callable[[_type.HSTRING,  # name
                                  _struct.Windows.Foundation.Size,  # value
                                  _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                 _type.HRESULT]
    AddSizeWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                         _struct.Windows.Foundation.Size,  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                         _type.INT32],  # tags
                                        _type.HRESULT]
    AddSizeArray: _Callable[[_type.HSTRING,  # name
                             _type.UINT32,  # __valueSize
                             _Pointer[_struct.Windows.Foundation.Size]],  # value
                            _type.HRESULT]
    AddSizeArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                       _type.UINT32,  # __valueSize
                                       _Pointer[_struct.Windows.Foundation.Size],  # value
                                       _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                      _type.HRESULT]
    AddSizeArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                              _type.UINT32,  # __valueSize
                                              _Pointer[_struct.Windows.Foundation.Size],  # value
                                              _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                              _type.INT32],  # tags
                                             _type.HRESULT]
    AddRect: _Callable[[_type.HSTRING,  # name
                        _struct.Windows.Foundation.Rect],  # value
                       _type.HRESULT]
    AddRectWithFormat: _Callable[[_type.HSTRING,  # name
                                  _struct.Windows.Foundation.Rect,  # value
                                  _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                 _type.HRESULT]
    AddRectWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                         _struct.Windows.Foundation.Rect,  # value
                                         _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                         _type.INT32],  # tags
                                        _type.HRESULT]
    AddRectArray: _Callable[[_type.HSTRING,  # name
                             _type.UINT32,  # __valueSize
                             _Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    AddRectArrayWithFormat: _Callable[[_type.HSTRING,  # name
                                       _type.UINT32,  # __valueSize
                                       _Pointer[_struct.Windows.Foundation.Rect],  # value
                                       _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat],  # format
                                      _type.HRESULT]
    AddRectArrayWithFormatAndTags: _Callable[[_type.HSTRING,  # name
                                              _type.UINT32,  # __valueSize
                                              _Pointer[_struct.Windows.Foundation.Rect],  # value
                                              _enum.Windows.Foundation.Diagnostics.LoggingFieldFormat,  # format
                                              _type.INT32],  # tags
                                             _type.HRESULT]


class ILoggingOptions(_inspectable.IInspectable):
    get_Keywords: _Callable[[_Pointer[_type.INT64]],  # value
                            _type.HRESULT]
    put_Keywords: _Callable[[_type.INT64],  # value
                            _type.HRESULT]
    get_Tags: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    put_Tags: _Callable[[_type.INT32],  # value
                        _type.HRESULT]
    get_Task: _Callable[[_Pointer[_type.INT16]],  # value
                        _type.HRESULT]
    put_Task: _Callable[[_type.INT16],  # value
                        _type.HRESULT]
    get_Opcode: _Callable[[_Pointer[_enum.Windows.Foundation.Diagnostics.LoggingOpcode]],  # value
                          _type.HRESULT]
    put_Opcode: _Callable[[_enum.Windows.Foundation.Diagnostics.LoggingOpcode],  # value
                          _type.HRESULT]
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    put_ActivityId: _Callable[[_struct.GUID],  # value
                              _type.HRESULT]
    get_RelatedActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                                     _type.HRESULT]
    put_RelatedActivityId: _Callable[[_struct.GUID],  # value
                                     _type.HRESULT]


class ILoggingOptionsFactory(_inspectable.IInspectable, factory=True):
    CreateWithKeywords: _Callable[[_type.INT64,  # keywords
                                   _Pointer[ILoggingOptions]],  # result
                                  _type.HRESULT]


class ILoggingSession(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    SaveToFileAsync: _Callable[[_Windows_Storage.IStorageFolder,  # folder
                                _type.HSTRING,  # fileName
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                               _type.HRESULT]
    AddLoggingChannel: _Callable[[ILoggingChannel],  # loggingChannel
                                 _type.HRESULT]
    AddLoggingChannelWithLevel: _Callable[[ILoggingChannel,  # loggingChannel
                                           _enum.Windows.Foundation.Diagnostics.LoggingLevel],  # maxLevel
                                          _type.HRESULT]
    RemoveLoggingChannel: _Callable[[ILoggingChannel],  # loggingChannel
                                    _type.HRESULT]


class ILoggingSessionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # name
                       _Pointer[ILoggingSession]],  # result
                      _type.HRESULT]


class ILoggingTarget(_inspectable.IInspectable):
    IsEnabled: _Callable[[_Pointer[_type.boolean]],  # result
                         _type.HRESULT]
    IsEnabledWithLevel: _Callable[[_enum.Windows.Foundation.Diagnostics.LoggingLevel,  # level
                                   _Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    IsEnabledWithLevelAndKeywords: _Callable[[_enum.Windows.Foundation.Diagnostics.LoggingLevel,  # level
                                              _type.INT64,  # keywords
                                              _Pointer[_type.boolean]],  # result
                                             _type.HRESULT]
    LogEvent: _Callable[[_type.HSTRING],  # eventName
                        _type.HRESULT]
    LogEventWithFields: _Callable[[_type.HSTRING,  # eventName
                                   ILoggingFields],  # fields
                                  _type.HRESULT]
    LogEventWithFieldsAndLevel: _Callable[[_type.HSTRING,  # eventName
                                           ILoggingFields,  # fields
                                           _enum.Windows.Foundation.Diagnostics.LoggingLevel],  # level
                                          _type.HRESULT]
    LogEventWithFieldsAndOptions: _Callable[[_type.HSTRING,  # eventName
                                             ILoggingFields,  # fields
                                             _enum.Windows.Foundation.Diagnostics.LoggingLevel,  # level
                                             ILoggingOptions],  # options
                                            _type.HRESULT]
    StartActivity: _Callable[[_type.HSTRING,  # startEventName
                              _Pointer[ILoggingActivity]],  # result
                             _type.HRESULT]
    StartActivityWithFields: _Callable[[_type.HSTRING,  # startEventName
                                        ILoggingFields,  # fields
                                        _Pointer[ILoggingActivity]],  # result
                                       _type.HRESULT]
    StartActivityWithFieldsAndLevel: _Callable[[_type.HSTRING,  # startEventName
                                                ILoggingFields,  # fields
                                                _enum.Windows.Foundation.Diagnostics.LoggingLevel,  # level
                                                _Pointer[ILoggingActivity]],  # result
                                               _type.HRESULT]
    StartActivityWithFieldsAndOptions: _Callable[[_type.HSTRING,  # startEventName
                                                  ILoggingFields,  # fields
                                                  _enum.Windows.Foundation.Diagnostics.LoggingLevel,  # level
                                                  ILoggingOptions,  # options
                                                  _Pointer[ILoggingActivity]],  # result
                                                 _type.HRESULT]


class ITracingStatusChangedEventArgs(_inspectable.IInspectable):
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # enabled
                           _type.HRESULT]
    get_TraceLevel: _Callable[[_Pointer[_enum.Windows.Foundation.Diagnostics.CausalityTraceLevel]],  # value
                              _type.HRESULT]
