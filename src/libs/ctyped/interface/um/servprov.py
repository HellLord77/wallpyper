from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IServiceProvider(_Unknwnbase.IUnknown):
    QueryService: _Callable[[_Pointer[_struct.GUID],  # guidService
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppvObject
                            _type.HRESULT]
