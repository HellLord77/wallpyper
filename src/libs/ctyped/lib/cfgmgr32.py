from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# Cfgmgr32
CM_Get_DevNode_PropertyW: _Callable[[_type.DEVINST,
                                     _Pointer[_struct.DEVPROPKEY],
                                     _Pointer[_type.DEVPROPTYPE],
                                     _Optional[_type.PBYTE],
                                     _Pointer[_type.ULONG],
                                     _type.ULONG],
                                    _type.CONFIGRET]
CM_Get_Device_Interface_PropertyW: _Callable[[_type.LPCWSTR,
                                              _Pointer[_struct.DEVPROPKEY],
                                              _Pointer[_type.DEVPROPTYPE],
                                              _Optional[_type.PBYTE],
                                              _Pointer[_type.ULONG],
                                              _type.ULONG],
                                             _type.CONFIGRET]
CM_Locate_DevNodeA: _Callable[[_Pointer[_type.DEVINST],
                               _type.PBYTE,
                               _type.ULONG],
                              _type.CONFIGRET]
CM_Locate_DevNodeW: _Callable[[_Pointer[_type.DEVINST],
                               _type.PWSTR,
                               _type.ULONG],
                              _type.CONFIGRET]

_WinLib(__name__)
