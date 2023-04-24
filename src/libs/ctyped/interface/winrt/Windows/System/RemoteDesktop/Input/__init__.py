from __future__ import annotations

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _IRemoteTextConnectionDataHandler:
    Invoke: _Callable[[_type.UINT32,  # __pduDataSize
                       _Pointer[_type.BYTE],  # pduData
                       _Pointer[_type.boolean]],  # result
                      _type.HRESULT]


class IRemoteTextConnectionDataHandler(_IRemoteTextConnectionDataHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRemoteTextConnectionDataHandler_impl(_IRemoteTextConnectionDataHandler, _Unknwnbase.IUnknown_impl):
    pass


class IRemoteTextConnection(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    RegisterThread: _Callable[[_type.UINT32],  # threadId
                              _type.HRESULT]
    UnregisterThread: _Callable[[_type.UINT32],  # threadId
                                _type.HRESULT]
    ReportDataReceived: _Callable[[_type.UINT32,  # __pduDataSize
                                   _Pointer[_type.BYTE]],  # pduData
                                  _type.HRESULT]


class IRemoteTextConnectionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_struct.GUID,  # connectionId
                               IRemoteTextConnectionDataHandler,  # pduForwarder
                               _Pointer[IRemoteTextConnection]],  # value
                              _type.HRESULT]

    _factory = True
