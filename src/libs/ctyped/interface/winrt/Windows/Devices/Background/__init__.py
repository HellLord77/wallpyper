from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDeviceServicingDetails(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ExpectedDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                    _type.HRESULT]


class IDeviceUseDetails(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
