from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import type as _type
from .._utils import _Pointer

# ShellScalingApi
GetDpiForMonitor: _Callable[[_type.HMONITOR,
                             _enum.MONITOR_DPI_TYPE,
                             _Pointer[_type.UINT],
                             _Pointer[_type.UINT]],
                            _type.HRESULT]
GetProcessDpiAwareness: _Callable[[_type.HANDLE,
                                   _Pointer[_enum.PROCESS_DPI_AWARENESS]],
                                  _type.HRESULT]
SetProcessDpiAwareness: _Callable[[_enum.PROCESS_DPI_AWARENESS],
                                  _type.HRESULT]

_WinLib(__name__)
