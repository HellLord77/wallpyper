from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import type as _type
from ..._utils import _Pointer


class IImageBytes(_Unknwnbase.IUnknown):
    CountBytes: _Callable[[_Pointer[_type.UINT]],  # pcb
                          _type.HRESULT]
    LockBytes: _Callable[[_type.UINT,  # cb
                          _type.ULONG,  # ulOffset
                          _Pointer[_Pointer[_type.VOID]]],  # ppvBytes
                         _type.HRESULT]
    UnlockBytes: _Callable[[_Pointer[_type.VOID],  # pvBytes
                            _type.UINT,  # cb
                            _type.ULONG],  # ulOffset
                           _type.HRESULT]
