from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPhoneCallOrigin(_inspectable.IInspectable):
    Category: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    CategoryDescription: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    Location: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IPhoneCallOrigin2(_inspectable.IInspectable):
    DisplayName: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]


class IPhoneCallOrigin3(_inspectable.IInspectable):
    DisplayPicture: _Callable[[_Windows_Storage.IStorageFile],  # value
                              _type.HRESULT]


class IPhoneCallOriginManagerStatics(_inspectable.IInspectable):
    IsCurrentAppActiveCallOriginApp: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    ShowPhoneCallOriginSettingsUI: _Callable[[],
                                             _type.HRESULT]
    SetCallOrigin: _Callable[[_struct.GUID,  # requestId
                              IPhoneCallOrigin],  # callOrigin
                             _type.HRESULT]

    _factory = True


class IPhoneCallOriginManagerStatics2(_inspectable.IInspectable):
    RequestSetAsActiveCallOriginAppAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                    _type.HRESULT]

    _factory = True


class IPhoneCallOriginManagerStatics3(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]

    _factory = True
