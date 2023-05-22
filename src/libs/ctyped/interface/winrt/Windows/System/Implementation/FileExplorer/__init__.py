from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Web import Http as _Windows_Web_Http
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISysStorageProviderEventReceivedEventArgs(_inspectable.IInspectable):
    get_Json: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ISysStorageProviderEventReceivedEventArgsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # json
                               _Pointer[ISysStorageProviderEventReceivedEventArgs]],  # value
                              _type.HRESULT]


class ISysStorageProviderEventSource(_inspectable.IInspectable):
    add_EventReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ISysStorageProviderEventSource, ISysStorageProviderEventReceivedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_EventReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class ISysStorageProviderHandlerFactory(_inspectable.IInspectable):
    GetHttpRequestProvider: _Callable[[_type.HSTRING,  # syncRootId
                                       _Pointer[ISysStorageProviderHttpRequestProvider]],  # result
                                      _type.HRESULT]
    GetEventSource: _Callable[[_type.HSTRING,  # syncRootId
                               _type.HSTRING,  # eventName
                               _Pointer[ISysStorageProviderEventSource]],  # result
                              _type.HRESULT]


class ISysStorageProviderHttpRequestProvider(_inspectable.IInspectable):
    SendRequestAsync: _Callable[[_Windows_Web_Http.IHttpRequestMessage,  # request
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Web_Http.IHttpResponseMessage]]],  # operation
                                _type.HRESULT]
