from __future__ import annotations as _

from typing import Callable as _Callable

from ...... import Unknwnbase as _Unknwnbase
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IDesktopWindowXamlSourceNative(_Unknwnbase.IUnknown):
    AttachToWindow: _Callable[[_type.HWND],  # parentWnd
                              _type.HRESULT]
    get_WindowHandle: _Callable[[_Pointer[_type.HWND]],  # hWnd
                                _type.HRESULT]


class IDesktopWindowXamlSourceNative2(IDesktopWindowXamlSourceNative):
    PreTranslateMessage: _Callable[[_Pointer[_struct.MSG],  # message
                                    _Pointer[_type.BOOL]],  # result
                                   _type.HRESULT]
