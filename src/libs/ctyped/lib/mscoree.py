from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# cor
CoEEShutDownCOM: _Callable[[],
                           _type.c_void]
CoInitializeCor: _Callable[[_type.DWORD],
                           _type.HRESULT]
CoInitializeEE: _Callable[[_enum.COINITIEE],
                          _type.HRESULT]
CoUninitializeCor: _Callable[[],
                             _type.c_void]
CoUninitializeEE: _Callable[[_type.BOOL],
                            _type.c_void]
# mscoree
CorBindToCurrentRuntime: _Callable[[_Optional[_type.LPCWSTR],
                                    _Pointer[_struct.CLSID],
                                    _Pointer[_struct.IID],
                                    _type.LPVOID],
                                   _type.HRESULT]
CorBindToRuntimeEx: _Callable[[_Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR],
                               _enum.STARTUP_FLAGS,
                               _Pointer[_struct.CLSID],
                               _Pointer[_struct.IID],
                               _type.LPVOID],
                              _type.HRESULT]
# rometadata
MetaDataGetDispenser: _Callable[[_Pointer[_struct.IID],  # rclsid
                                 _Pointer[_struct.IID],  # riid
                                 _type.LPVOID],  # ppv
                                _type.HRESULT]

_WinLib(__name__)
