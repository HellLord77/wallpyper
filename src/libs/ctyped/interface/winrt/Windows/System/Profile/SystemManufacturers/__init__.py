from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IOemSupportInfo(_inspectable.IInspectable):
    get_SupportLink: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_SupportAppLink: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                  _type.HRESULT]
    get_SupportProvider: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class ISmbiosInformationStatics(_inspectable.IInspectable):
    get_SerialNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]

    _factory = True


class ISystemSupportDeviceInfo(_inspectable.IInspectable):
    get_OperatingSystem: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_SystemManufacturer: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_SystemProductName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_SystemSku: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SystemHardwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_SystemFirmwareVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]


class ISystemSupportInfoStatics(_inspectable.IInspectable):
    get_LocalSystemEdition: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_OemSupportInfo: _Callable[[_Pointer[IOemSupportInfo]],  # value
                                  _type.HRESULT]

    _factory = True


class ISystemSupportInfoStatics2(_inspectable.IInspectable):
    get_LocalDeviceInfo: _Callable[[_Pointer[ISystemSupportDeviceInfo]],  # value
                                   _type.HRESULT]

    _factory = True
