from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Storage as _Windows_Storage
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IServiceDeviceStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_enum.Windows.Devices.Portable.ServiceDeviceType,  # serviceType
                                  _Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]
    GetDeviceSelectorFromServiceId: _Callable[[_struct.GUID,  # serviceId
                                               _Pointer[_type.HSTRING]],  # selector
                                              _type.HRESULT]


class IStorageDeviceStatics(_inspectable.IInspectable, factory=True):
    FromId: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[_Windows_Storage.IStorageFolder]],  # deviceRoot
                      _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]
