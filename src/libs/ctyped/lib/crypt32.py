from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import type as _type
from .._utils import _Pointer

# wincrypt
CryptBinaryToStringA: _Callable[[_Pointer[_type.BYTE],
                                 _type.DWORD,
                                 _type.DWORD,
                                 _Optional[_Pointer[_type.LPSTR]],
                                 _Pointer[_type.DWORD]],
                                _type.BOOL]
CryptBinaryToStringW: _Callable[[_Pointer[_type.BYTE],
                                 _type.DWORD,
                                 _type.DWORD,
                                 _Optional[_Pointer[_type.LPWSTR]],
                                 _Pointer[_type.DWORD]],
                                _type.BOOL]
CryptStringToBinaryA: _Callable[[_type.LPCSTR,
                                 _type.DWORD,
                                 _type.DWORD,
                                 _Pointer[_type.BYTE],
                                 _Pointer[_type.DWORD],
                                 _Optional[_Pointer[_type.DWORD]],
                                 _Optional[_Pointer[_type.DWORD]]],
                                _type.BOOL]
CryptStringToBinaryW: _Callable[[_type.LPCWSTR,
                                 _type.DWORD,
                                 _type.DWORD,
                                 _Pointer[_type.BYTE],
                                 _Pointer[_type.DWORD],
                                 _Optional[_Pointer[_type.DWORD]],
                                 _Optional[_Pointer[_type.DWORD]]],
                                _type.BOOL]

_WinLib(__name__)
