from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Input as _Microsoft_UI_Input
from ..... import inspectable as _inspectable
from .....Windows.Devices import Input as _Windows_Devices_Input
from ....... import type as _type
from ......._utils import _Pointer


class IPenDeviceInteropStatics(_inspectable.IInspectable, factory=True):
    FromPointerPoint: _Callable[[_Microsoft_UI_Input.IPointerPoint,  # pointerPoint
                                 _Pointer[_Windows_Devices_Input.IPenDevice]],  # result
                                _type.HRESULT]
