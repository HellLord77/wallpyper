from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Http as _Windows_Web_Http
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....System import Diagnostics as _Windows_System_Diagnostics
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IHttpDiagnosticProvider(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_RequestSent: _Callable[[_Windows_Foundation.ITypedEventHandler[IHttpDiagnosticProvider, IHttpDiagnosticProviderRequestSentEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_RequestSent: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_ResponseReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IHttpDiagnosticProvider, IHttpDiagnosticProviderResponseReceivedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ResponseReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_RequestResponseCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IHttpDiagnosticProvider, IHttpDiagnosticProviderRequestResponseCompletedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_RequestResponseCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]


class IHttpDiagnosticProviderRequestResponseCompletedEventArgs(_inspectable.IInspectable):
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Timestamps: _Callable[[_Pointer[IHttpDiagnosticProviderRequestResponseTimestamps]],  # value
                              _type.HRESULT]
    get_RequestedUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                _type.HRESULT]
    get_ProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_ThreadId: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Initiator: _Callable[[_Pointer[_enum.Windows.Web.Http.Diagnostics.HttpDiagnosticRequestInitiator]],  # value
                             _type.HRESULT]
    get_SourceLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHttpDiagnosticSourceLocation]]],  # value
                                   _type.HRESULT]


class IHttpDiagnosticProviderRequestResponseTimestamps(_inspectable.IInspectable):
    get_CacheCheckedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                         _type.HRESULT]
    get_ConnectionInitiatedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    get_NameResolvedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                         _type.HRESULT]
    get_SslNegotiatedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                          _type.HRESULT]
    get_ConnectionCompletedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    get_RequestSentTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                        _type.HRESULT]
    get_RequestCompletedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                             _type.HRESULT]
    get_ResponseReceivedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                             _type.HRESULT]
    get_ResponseCompletedTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                              _type.HRESULT]


class IHttpDiagnosticProviderRequestSentEventArgs(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Message: _Callable[[_Pointer[_Windows_Web_Http.IHttpRequestMessage]],  # value
                           _type.HRESULT]
    get_ProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_ThreadId: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Initiator: _Callable[[_Pointer[_enum.Windows.Web.Http.Diagnostics.HttpDiagnosticRequestInitiator]],  # value
                             _type.HRESULT]
    get_SourceLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHttpDiagnosticSourceLocation]]],  # value
                                   _type.HRESULT]


class IHttpDiagnosticProviderResponseReceivedEventArgs(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Message: _Callable[[_Pointer[_Windows_Web_Http.IHttpResponseMessage]],  # value
                           _type.HRESULT]


class IHttpDiagnosticProviderStatics(_inspectable.IInspectable, factory=True):
    CreateFromProcessDiagnosticInfo: _Callable[[_Windows_System_Diagnostics.IProcessDiagnosticInfo,  # processDiagnosticInfo
                                                _Pointer[IHttpDiagnosticProvider]],  # value
                                               _type.HRESULT]


class IHttpDiagnosticSourceLocation(_inspectable.IInspectable):
    get_SourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    get_LineNumber: _Callable[[_Pointer[_type.UINT64]],  # value
                              _type.HRESULT]
    get_ColumnNumber: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]
