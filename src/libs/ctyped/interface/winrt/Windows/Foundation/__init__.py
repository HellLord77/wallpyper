from __future__ import annotations

from typing import Callable as _Callable, Generic as _Generic

from ... import inspectable as _inspectable
from .... import _T, _TArgs, _TProgress, _TResult, _TSender, _Template
from ....um import Unknwnbase as _Unknwnbase
from ..... import enum as _enum
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class _IAsyncOperationProgressHandler(_Template):
    Invoke: _Callable[[IAsyncOperationWithProgress[_TResult, _TProgress],  # asyncInfo
                       _TProgress],  # progressInfo
                      _type.HRESULT]


class IAsyncOperationProgressHandler(_IAsyncOperationProgressHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncOperationProgressHandler_impl(_IAsyncOperationProgressHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown_impl):
    pass


class _IAsyncOperationWithProgressCompletedHandler(_Template):
    Invoke: _Callable[[IAsyncOperationWithProgress[_TResult, _TProgress],  # asyncInfo
                       _enum.Windows.Foundation.AsyncStatus],  # status
                      _type.HRESULT]


class IAsyncOperationWithProgressCompletedHandler(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncOperationWithProgressCompletedHandler_impl(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown_impl):
    pass


class _IAsyncOperationCompletedHandler(_Template):
    Invoke: _Callable[[IAsyncOperation[_TResult],  # asyncInfo
                       _enum.Windows.Foundation.AsyncStatus],  # status
                      _type.HRESULT]


class IAsyncOperationCompletedHandler(_IAsyncOperationCompletedHandler, _Generic[_TResult], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncOperationCompletedHandler_impl(_IAsyncOperationCompletedHandler, _Generic[_TResult], _Unknwnbase.IUnknown_impl):
    pass


class IAsyncOperationWithProgress(_Template, _Generic[_TResult, _TProgress], _inspectable.IInspectable):
    put_Progress: _Callable[[IAsyncOperationProgressHandler[_TResult, _TProgress]],  # handler
                            _type.HRESULT]
    get_Progress: _Callable[[_Pointer[IAsyncOperationProgressHandler[_TResult, _TProgress]]],  # handler
                            _type.HRESULT]
    put_Completed: _Callable[[IAsyncOperationWithProgressCompletedHandler[_TResult, _TProgress]],  # handler
                             _type.HRESULT]
    get_Completed: _Callable[[_Pointer[IAsyncOperationWithProgressCompletedHandler[_TResult, _TProgress]]],  # handler
                             _type.HRESULT]
    GetResults: _Callable[[_Pointer[_TResult]],  # results
                          _type.HRESULT]


class IAsyncActionWithProgress(_Template, _Generic[_TProgress], _inspectable.IInspectable):
    put_Progress: _Callable[[IAsyncActionProgressHandler[_TProgress]],  # handler
                            _type.HRESULT]
    get_Progress: _Callable[[_Pointer[IAsyncActionProgressHandler[_TProgress]]],  # handler
                            _type.HRESULT]
    put_Completed: _Callable[[IAsyncActionWithProgressCompletedHandler[_TProgress]],  # handler
                             _type.HRESULT]
    get_Completed: _Callable[[_Pointer[IAsyncActionWithProgressCompletedHandler[_TProgress]]],  # handler
                             _type.HRESULT]
    GetResults: _Callable[[],
                          _type.HRESULT]


class IAsyncOperation(_Template, _Generic[_TResult], _inspectable.IInspectable):
    put_Completed: _Callable[[IAsyncOperationCompletedHandler[_TResult]],  # handler
                             _type.HRESULT]
    get_Completed: _Callable[[_Pointer[IAsyncOperationCompletedHandler[_TResult]]],  # handler
                             _type.HRESULT]
    GetResults: _Callable[[_Pointer[_TResult]],  # results
                          _type.HRESULT]


class _IAsyncActionProgressHandler(_Template):
    Invoke: _Callable[[IAsyncActionWithProgress[_TProgress],  # asyncInfo
                       _TProgress],  # progressInfo
                      _type.HRESULT]


class IAsyncActionProgressHandler(_IAsyncActionProgressHandler, _Generic[_TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncActionProgressHandler_impl(_IAsyncActionProgressHandler, _Generic[_TProgress], _Unknwnbase.IUnknown_impl):
    pass


class _IAsyncActionWithProgressCompletedHandler(_Template):
    Invoke: _Callable[[IAsyncActionWithProgress[_TProgress],  # asyncInfo
                       _enum.Windows.Foundation.AsyncStatus],  # status
                      _type.HRESULT]


class IAsyncActionWithProgressCompletedHandler(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncActionWithProgressCompletedHandler_impl(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], _Unknwnbase.IUnknown_impl):
    pass


class IReference(_Template, _Generic[_T], _inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_T]],  # value
                         _type.HRESULT]


class IReferenceArray(_Template, _Generic[_T], _inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.UINT32],  # length
                          _Pointer[_Pointer[_T]]],  # value
                         _type.HRESULT]


class _IEventHandler(_Template):
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _T],  # args
                      _type.HRESULT]


class IEventHandler(_IEventHandler, _Generic[_T], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IEventHandler_impl(_IEventHandler, _Generic[_T], _Unknwnbase.IUnknown_impl):
    pass


class _ITypedEventHandler(_Template):
    Invoke: _Callable[[_TSender,  # sender
                       _TArgs],  # args
                      _type.HRESULT]


class ITypedEventHandler(_ITypedEventHandler, _Generic[_TSender, _TArgs], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITypedEventHandler_impl(_ITypedEventHandler, _Generic[_TSender, _TArgs], _Unknwnbase.IUnknown_impl):
    pass


class _IAsyncActionCompletedHandler:
    Invoke: _Callable[[IAsyncAction,  # asyncInfo
                       _enum.Windows.Foundation.AsyncStatus],  # asyncStatus
                      _type.HRESULT]


class IAsyncActionCompletedHandler(_IAsyncActionCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncActionCompletedHandler_impl(_IAsyncActionCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDeferralCompletedHandler:
    Invoke: _Callable[[],
                      _type.HRESULT]


class IDeferralCompletedHandler(_IDeferralCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDeferralCompletedHandler_impl(_IDeferralCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAsyncAction(_inspectable.IInspectable):
    put_Completed: _Callable[[IAsyncActionCompletedHandler],  # handler
                             _type.HRESULT]
    get_Completed: _Callable[[_Pointer[IAsyncActionCompletedHandler]],  # handler
                             _type.HRESULT]
    GetResults: _Callable[[],
                          _type.HRESULT]


class IClosable(_inspectable.IInspectable):
    Close: _Callable[[],
                     _type.HRESULT]


class IDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IDeferralFactory(_inspectable.IInspectable):
    Create: _Callable[[IDeferralCompletedHandler,  # handler
                       _Pointer[IDeferral]],  # result
                      _type.HRESULT]

    _factory = True


class IGetActivationFactory(_inspectable.IInspectable):
    GetActivationFactory: _Callable[[_type.HSTRING,  # activatableClassId
                                     _Pointer[_inspectable.IInspectable]],  # factory
                                    _type.HRESULT]


class IGuidHelperStatics(_inspectable.IInspectable):
    CreateNewGuid: _Callable[[_Pointer[_struct.GUID]],  # result
                             _type.HRESULT]
    get_Empty: _Callable[[_Pointer[_struct.GUID]],  # value
                         _type.HRESULT]
    Equals: _Callable[[_Pointer[_struct.GUID],  # target
                       _Pointer[_struct.GUID],  # value
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]

    _factory = True


class IMemoryBuffer(_inspectable.IInspectable):
    CreateReference: _Callable[[_Pointer[IMemoryBufferReference]],  # reference
                               _type.HRESULT]


class IMemoryBufferFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # capacity
                       _Pointer[IMemoryBuffer]],  # value
                      _type.HRESULT]

    _factory = True


class IMemoryBufferReference(_inspectable.IInspectable):
    get_Capacity: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    add_Closed: _Callable[[ITypedEventHandler[IMemoryBufferReference, _inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # cookie
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # cookie
                             _type.HRESULT]


class IPropertyValue(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Foundation.PropertyType]],  # value
                        _type.HRESULT]
    get_IsNumericScalar: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    GetUInt8: _Callable[[_Pointer[_type.BYTE]],  # value
                        _type.HRESULT]
    GetInt16: _Callable[[_Pointer[_type.INT16]],  # value
                        _type.HRESULT]
    GetUInt16: _Callable[[_Pointer[_type.UINT16]],  # value
                         _type.HRESULT]
    GetInt32: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    GetUInt32: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    GetInt64: _Callable[[_Pointer[_type.INT64]],  # value
                        _type.HRESULT]
    GetUInt64: _Callable[[_Pointer[_type.UINT64]],  # value
                         _type.HRESULT]
    GetSingle: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    GetDouble: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    GetChar16: _Callable[[_Pointer[_type.WCHAR]],  # value
                         _type.HRESULT]
    GetBoolean: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    GetString: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    GetGuid: _Callable[[_Pointer[_struct.GUID]],  # value
                       _type.HRESULT]
    GetDateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    GetTimeSpan: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]
    GetPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                        _type.HRESULT]
    GetSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                       _type.HRESULT]
    GetRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                       _type.HRESULT]
    GetUInt8Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                              _Pointer[_Pointer[_type.BYTE]]],  # value
                             _type.HRESULT]
    GetInt16Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                              _Pointer[_Pointer[_type.INT16]]],  # value
                             _type.HRESULT]
    GetUInt16Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.UINT16]]],  # value
                              _type.HRESULT]
    GetInt32Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                              _Pointer[_Pointer[_type.INT32]]],  # value
                             _type.HRESULT]
    GetUInt32Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.UINT32]]],  # value
                              _type.HRESULT]
    GetInt64Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                              _Pointer[_Pointer[_type.INT64]]],  # value
                             _type.HRESULT]
    GetUInt64Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.UINT64]]],  # value
                              _type.HRESULT]
    GetSingleArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.FLOAT]]],  # value
                              _type.HRESULT]
    GetDoubleArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.DOUBLE]]],  # value
                              _type.HRESULT]
    GetChar16Array: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.WCHAR]]],  # value
                              _type.HRESULT]
    GetBooleanArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                _Pointer[_Pointer[_type.boolean]]],  # value
                               _type.HRESULT]
    GetStringArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                               _Pointer[_Pointer[_type.HSTRING]]],  # value
                              _type.HRESULT]
    GetInspectableArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                    _Pointer[_Pointer[_inspectable.IInspectable]]],  # value
                                   _type.HRESULT]
    GetGuidArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                             _Pointer[_Pointer[_struct.GUID]]],  # value
                            _type.HRESULT]
    GetDateTimeArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                 _Pointer[_Pointer[_struct.Windows.Foundation.DateTime]]],  # value
                                _type.HRESULT]
    GetTimeSpanArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                 _Pointer[_Pointer[_struct.Windows.Foundation.TimeSpan]]],  # value
                                _type.HRESULT]
    GetPointArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                              _Pointer[_Pointer[_struct.Windows.Foundation.Point]]],  # value
                             _type.HRESULT]
    GetSizeArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                             _Pointer[_Pointer[_struct.Windows.Foundation.Size]]],  # value
                            _type.HRESULT]
    GetRectArray: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                             _Pointer[_Pointer[_struct.Windows.Foundation.Rect]]],  # value
                            _type.HRESULT]


class IPropertyValueStatics(_inspectable.IInspectable):
    CreateEmpty: _Callable[[_Pointer[_inspectable.IInspectable]],  # propertyValue
                           _type.HRESULT]
    CreateUInt8: _Callable[[_type.BYTE,  # value
                            _Pointer[_inspectable.IInspectable]],  # propertyValue
                           _type.HRESULT]
    CreateInt16: _Callable[[_type.INT16,  # value
                            _Pointer[_inspectable.IInspectable]],  # propertyValue
                           _type.HRESULT]
    CreateUInt16: _Callable[[_type.UINT16,  # value
                             _Pointer[_inspectable.IInspectable]],  # propertyValue
                            _type.HRESULT]
    CreateInt32: _Callable[[_type.INT32,  # value
                            _Pointer[_inspectable.IInspectable]],  # propertyValue
                           _type.HRESULT]
    CreateUInt32: _Callable[[_type.UINT32,  # value
                             _Pointer[_inspectable.IInspectable]],  # propertyValue
                            _type.HRESULT]
    CreateInt64: _Callable[[_type.INT64,  # value
                            _Pointer[_inspectable.IInspectable]],  # propertyValue
                           _type.HRESULT]
    CreateUInt64: _Callable[[_type.UINT64,  # value
                             _Pointer[_inspectable.IInspectable]],  # propertyValue
                            _type.HRESULT]
    CreateSingle: _Callable[[_type.FLOAT,  # value
                             _Pointer[_inspectable.IInspectable]],  # propertyValue
                            _type.HRESULT]
    CreateDouble: _Callable[[_type.DOUBLE,  # value
                             _Pointer[_inspectable.IInspectable]],  # propertyValue
                            _type.HRESULT]
    CreateChar16: _Callable[[_type.WCHAR,  # value
                             _Pointer[_inspectable.IInspectable]],  # propertyValue
                            _type.HRESULT]
    CreateBoolean: _Callable[[_type.boolean,  # value
                              _Pointer[_inspectable.IInspectable]],  # propertyValue
                             _type.HRESULT]
    CreateString: _Callable[[_type.HSTRING,  # value
                             _Pointer[_inspectable.IInspectable]],  # propertyValue
                            _type.HRESULT]
    CreateInspectable: _Callable[[_inspectable.IInspectable,  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateGuid: _Callable[[_struct.GUID,  # value
                           _Pointer[_inspectable.IInspectable]],  # propertyValue
                          _type.HRESULT]
    CreateDateTime: _Callable[[_struct.Windows.Foundation.DateTime,  # value
                               _Pointer[_inspectable.IInspectable]],  # propertyValue
                              _type.HRESULT]
    CreateTimeSpan: _Callable[[_struct.Windows.Foundation.TimeSpan,  # value
                               _Pointer[_inspectable.IInspectable]],  # propertyValue
                              _type.HRESULT]
    CreatePoint: _Callable[[_struct.Windows.Foundation.Point,  # value
                            _Pointer[_inspectable.IInspectable]],  # propertyValue
                           _type.HRESULT]
    CreateSize: _Callable[[_struct.Windows.Foundation.Size,  # value
                           _Pointer[_inspectable.IInspectable]],  # propertyValue
                          _type.HRESULT]
    CreateRect: _Callable[[_struct.Windows.Foundation.Rect,  # value
                           _Pointer[_inspectable.IInspectable]],  # propertyValue
                          _type.HRESULT]
    CreateUInt8Array: _Callable[[_type.UINT32,  # __valueSize
                                 _Pointer[_type.BYTE],  # value
                                 _Pointer[_inspectable.IInspectable]],  # propertyValue
                                _type.HRESULT]
    CreateInt16Array: _Callable[[_type.UINT32,  # __valueSize
                                 _Pointer[_type.INT16],  # value
                                 _Pointer[_inspectable.IInspectable]],  # propertyValue
                                _type.HRESULT]
    CreateUInt16Array: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.UINT16],  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateInt32Array: _Callable[[_type.UINT32,  # __valueSize
                                 _Pointer[_type.INT32],  # value
                                 _Pointer[_inspectable.IInspectable]],  # propertyValue
                                _type.HRESULT]
    CreateUInt32Array: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.UINT32],  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateInt64Array: _Callable[[_type.UINT32,  # __valueSize
                                 _Pointer[_type.INT64],  # value
                                 _Pointer[_inspectable.IInspectable]],  # propertyValue
                                _type.HRESULT]
    CreateUInt64Array: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.UINT64],  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateSingleArray: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.FLOAT],  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateDoubleArray: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.DOUBLE],  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateChar16Array: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.WCHAR],  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateBooleanArray: _Callable[[_type.UINT32,  # __valueSize
                                   _Pointer[_type.boolean],  # value
                                   _Pointer[_inspectable.IInspectable]],  # propertyValue
                                  _type.HRESULT]
    CreateStringArray: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.HSTRING],  # value
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]
    CreateInspectableArray: _Callable[[_type.UINT32,  # __valueSize
                                       _Pointer[_inspectable.IInspectable],  # value
                                       _Pointer[_inspectable.IInspectable]],  # propertyValue
                                      _type.HRESULT]
    CreateGuidArray: _Callable[[_type.UINT32,  # __valueSize
                                _Pointer[_struct.GUID],  # value
                                _Pointer[_inspectable.IInspectable]],  # propertyValue
                               _type.HRESULT]
    CreateDateTimeArray: _Callable[[_type.UINT32,  # __valueSize
                                    _Pointer[_struct.Windows.Foundation.DateTime],  # value
                                    _Pointer[_inspectable.IInspectable]],  # propertyValue
                                   _type.HRESULT]
    CreateTimeSpanArray: _Callable[[_type.UINT32,  # __valueSize
                                    _Pointer[_struct.Windows.Foundation.TimeSpan],  # value
                                    _Pointer[_inspectable.IInspectable]],  # propertyValue
                                   _type.HRESULT]
    CreatePointArray: _Callable[[_type.UINT32,  # __valueSize
                                 _Pointer[_struct.Windows.Foundation.Point],  # value
                                 _Pointer[_inspectable.IInspectable]],  # propertyValue
                                _type.HRESULT]
    CreateSizeArray: _Callable[[_type.UINT32,  # __valueSize
                                _Pointer[_struct.Windows.Foundation.Size],  # value
                                _Pointer[_inspectable.IInspectable]],  # propertyValue
                               _type.HRESULT]
    CreateRectArray: _Callable[[_type.UINT32,  # __valueSize
                                _Pointer[_struct.Windows.Foundation.Rect],  # value
                                _Pointer[_inspectable.IInspectable]],  # propertyValue
                               _type.HRESULT]

    _factory = True


class IStringable(_inspectable.IInspectable):
    ToString: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IUriEscapeStatics(_inspectable.IInspectable):
    UnescapeComponent: _Callable[[_type.HSTRING,  # toUnescape
                                  _Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    EscapeComponent: _Callable[[_type.HSTRING,  # toEscape
                                _Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]

    _factory = True


class IUriRuntimeClass(_inspectable.IInspectable):
    get_AbsoluteUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DisplayUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Domain: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Extension: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Fragment: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Host: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Password: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Query: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_QueryParsed: _Callable[[_Pointer[IWwwFormUrlDecoderRuntimeClass]],  # ppWwwFormUrlDecoder
                               _type.HRESULT]
    get_RawUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_SchemeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Port: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    get_Suspicious: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    Equals: _Callable[[IUriRuntimeClass,  # pUri
                       _Pointer[_type.boolean]],  # value
                      _type.HRESULT]
    CombineUri: _Callable[[_type.HSTRING,  # relativeUri
                           _Pointer[IUriRuntimeClass]],  # instance
                          _type.HRESULT]


class IUriRuntimeClassFactory(_inspectable.IInspectable):
    CreateUri: _Callable[[_type.HSTRING,  # uri
                          _Pointer[IUriRuntimeClass]],  # instance
                         _type.HRESULT]
    CreateWithRelativeUri: _Callable[[_type.HSTRING,  # baseUri
                                      _type.HSTRING,  # relativeUri
                                      _Pointer[IUriRuntimeClass]],  # instance
                                     _type.HRESULT]

    _factory = True


class IUriRuntimeClassWithAbsoluteCanonicalUri(_inspectable.IInspectable):
    get_AbsoluteCanonicalUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_DisplayIri: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IWwwFormUrlDecoderEntry(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IWwwFormUrlDecoderRuntimeClass(_inspectable.IInspectable):
    GetFirstValueByName: _Callable[[_type.HSTRING,  # name
                                    _Pointer[_type.HSTRING]],  # phstrValue
                                   _type.HRESULT]


class IWwwFormUrlDecoderRuntimeClassFactory(_inspectable.IInspectable):
    CreateWwwFormUrlDecoder: _Callable[[_type.HSTRING,  # query
                                        _Pointer[IWwwFormUrlDecoderRuntimeClass]],  # instance
                                       _type.HRESULT]

    _factory = True
