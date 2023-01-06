from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import type as _type

# Psapi
GetDeviceDriverBaseNameA: _Callable[[_type.LPVOID,  # ImageBase
                                     _type.LPSTR,  # lpFilename
                                     _type.DWORD],  # nSize
                                    _type.DWORD]
GetDeviceDriverBaseNameW: _Callable[[_type.LPVOID,  # ImageBase
                                     _type.LPWSTR,  # lpFilename
                                     _type.DWORD],  # nSize
                                    _type.DWORD]
GetDeviceDriverFileNameA: _Callable[[_type.LPVOID,  # ImageBase
                                     _type.LPSTR,  # lpFilename
                                     _type.DWORD],  # nSize
                                    _type.DWORD]
GetDeviceDriverFileNameW: _Callable[[_type.LPVOID,  # ImageBase
                                     _type.LPWSTR,  # lpFilename
                                     _type.DWORD],  # nSize
                                    _type.DWORD]
QueryWorkingSet: _Callable[[_type.HANDLE,  # hProcess
                            _type.PVOID,  # pv
                            _type.DWORD],  # cb
                           _type.BOOL]
QueryWorkingSetEx: _Callable[[_type.HANDLE,  # hProcess
                              _type.PVOID,  # pv
                              _type.DWORD],  # cb
                             _type.BOOL]
GetProcessImageFileNameA: _Callable[[_type.HANDLE,  # hProcess
                                     _type.LPSTR,  # lpImageFileName
                                     _type.DWORD],  # nSize
                                    _type.DWORD]
GetProcessImageFileNameW: _Callable[[_type.HANDLE,  # hProcess
                                     _type.LPWSTR,  # lpImageFileName
                                     _type.DWORD],  # nSize
                                    _type.DWORD]

_WinLib(__name__)
