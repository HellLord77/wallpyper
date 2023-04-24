from __future__ import annotations

from typing import Callable as _Callable

from . import inspectable as _inspectable
from ... import enum as _enum
from ... import type as _type
from ..._utils import _Pointer


class IAsyncInfo(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.c_uint32]],  # id
                      _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Foundation.AsyncStatus]],  # status
                          _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # errorCode
                             _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
