from __future__ import annotations as _

from typing import Callable as _Callable

from .......winrt import inspectable as _inspectable
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class ICoreFrameworkInputViewInterop(_inspectable.IInspectable):
    GetForWindow: _Callable[[_type.HWND,  # appWindow
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # coreFrameworkInputView
                            _type.HRESULT]
