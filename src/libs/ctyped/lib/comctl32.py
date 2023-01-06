from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                         _type.HRESULT]
# CommCtrl
InitCommonControls: _Callable[[],
                              _type.c_void]
InitCommonControlsEx: _Callable[[_Pointer[_struct.INITCOMMONCONTROLSEX]],
                                _type.BOOL]

_WinLib(__name__)
