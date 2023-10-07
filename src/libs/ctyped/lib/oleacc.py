from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import type as _type

GetProcessHandleFromHwnd: _Callable[[_type.HWND],
                                    _type.HANDLE]
# oleacc
GetRoleTextA: _Callable[[_type.DWORD,
                         _Optional[_type.LPSTR],
                         _type.UINT],
                        _type.UINT]
GetRoleTextW: _Callable[[_type.DWORD,
                         _Optional[_type.LPWSTR],
                         _type.UINT],
                        _type.UINT]
GetStateTextA: _Callable[[_type.DWORD,
                          _Optional[_type.LPSTR],
                          _type.UINT],
                         _type.UINT]
GetStateTextW: _Callable[[_type.DWORD,
                          _Optional[_type.LPWSTR],
                          _type.UINT],
                         _type.UINT]

_WinLib(__name__)
