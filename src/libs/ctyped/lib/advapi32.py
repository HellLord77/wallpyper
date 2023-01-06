from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# winreg
AbortSystemShutdownA: _Callable[[_type.LPSTR],
                                _type.BOOL]
AbortSystemShutdownW: _Callable[[_type.LPWSTR],
                                _type.BOOL]
CheckForHiberboot: _Callable[[_Pointer[_type.BOOLEAN],
                              _type.BOOLEAN],
                             _type.DWORD]
InitiateShutdownA: _Callable[[_Optional[_type.LPSTR],
                              _Optional[_type.LPSTR],
                              _type.DWORD,
                              _type.DWORD,
                              _type.DWORD],
                             _type.DWORD]
InitiateShutdownW: _Callable[[_Optional[_type.LPWSTR],
                              _Optional[_type.LPWSTR],
                              _type.DWORD,
                              _type.DWORD,
                              _type.DWORD],
                             _type.DWORD]
InitiateSystemShutdownA: _Callable[[_Optional[_type.LPSTR],
                                    _Optional[_type.LPSTR],
                                    _type.DWORD,
                                    _type.BOOL,
                                    _type.BOOL],
                                   _type.BOOL]
InitiateSystemShutdownW: _Callable[[_Optional[_type.LPWSTR],
                                    _Optional[_type.LPWSTR],
                                    _type.DWORD,
                                    _type.BOOL,
                                    _type.BOOL],
                                   _type.BOOL]
InitiateSystemShutdownExA: _Callable[[_Optional[_type.LPSTR],
                                      _Optional[_type.LPSTR],
                                      _type.DWORD,
                                      _type.BOOL,
                                      _type.BOOL,
                                      _type.DWORD],
                                     _type.BOOL]
InitiateSystemShutdownExW: _Callable[[_Optional[_type.LPWSTR],
                                      _Optional[_type.LPWSTR],
                                      _type.DWORD,
                                      _type.BOOL,
                                      _type.BOOL,
                                      _type.DWORD],
                                     _type.BOOL]
RegCopyTreeA: _Callable[[_type.HKEY,
                         _Optional[_type.LPCSTR],
                         _type.HKEY],
                        _type.LSTATUS]
RegCopyTreeW: _Callable[[_type.HKEY,
                         _Optional[_type.LPCWSTR],
                         _type.HKEY],
                        _type.LSTATUS]
RegDeleteKeyValueA: _Callable[[_type.HKEY,
                               _Optional[_type.LPCSTR],
                               _Optional[_type.LPCSTR]],
                              _type.LSTATUS]
RegDeleteKeyValueW: _Callable[[_type.HKEY,
                               _Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR]],
                              _type.LSTATUS]
RegDeleteTreeA: _Callable[[_type.HKEY,
                           _Optional[_type.LPCSTR]],
                          _type.LSTATUS]
RegDeleteTreeW: _Callable[[_type.HKEY,
                           _Optional[_type.LPCWSTR]],
                          _type.LSTATUS]
RegLoadAppKeyA: _Callable[[_type.LPCSTR,
                           _Pointer[_type.HKEY],
                           _type.REGSAM,
                           _type.DWORD,
                           _type.DWORD],
                          _type.LSTATUS]
RegLoadAppKeyW: _Callable[[_type.LPCWSTR,
                           _Pointer[_type.HKEY],
                           _type.REGSAM,
                           _type.DWORD,
                           _type.DWORD],
                          _type.LSTATUS]
RegLoadMUIStringA: _Callable[[_type.HKEY,
                              _Optional[_type.LPCSTR],
                              _Optional[_type.LPSTR],
                              _type.DWORD,
                              _Optional[_Pointer[_type.DWORD]],
                              _type.DWORD,
                              _Optional[_type.LPCSTR]],
                             _type.LSTATUS]
RegLoadMUIStringW: _Callable[[_type.HKEY,
                              _Optional[_type.LPCWSTR],
                              _Optional[_type.LPWSTR],
                              _type.DWORD,
                              _Optional[_Pointer[_type.DWORD]],
                              _type.DWORD,
                              _Optional[_type.LPCWSTR]],
                             _type.LSTATUS]
RegReplaceKeyA: _Callable[[_type.HKEY,
                           _Optional[_type.LPCSTR],
                           _type.LPCSTR,
                           _type.LPCSTR],
                          _type.LSTATUS]
RegReplaceKeyW: _Callable[[_type.HKEY,
                           _Optional[_type.LPCWSTR],
                           _type.LPCWSTR,
                           _type.LPCWSTR],
                          _type.LSTATUS]
RegRestoreKeyA: _Callable[[_type.HKEY,
                           _type.LPCSTR,
                           _type.DWORD],
                          _type.LSTATUS]
RegRestoreKeyW: _Callable[[_type.HKEY,
                           _type.LPCWSTR,
                           _type.DWORD],
                          _type.LSTATUS]
RegSaveKeyExA: _Callable[[_type.HKEY,
                          _type.LPCSTR,
                          _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                          _type.DWORD],
                         _type.LSTATUS]
RegSaveKeyExW: _Callable[[_type.HKEY,
                          _type.LPCWSTR,
                          _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                          _type.DWORD],
                         _type.LSTATUS]
RegUnLoadKeyA: _Callable[[_type.HKEY,
                          _Optional[_type.LPCSTR]],
                         _type.LSTATUS]
RegUnLoadKeyW: _Callable[[_type.HKEY,
                          _Optional[_type.LPCWSTR]],
                         _type.LSTATUS]

_WinLib(__name__)
