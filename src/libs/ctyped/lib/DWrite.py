from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.um import Unknwnbase as _Unknwnbase

# dwrite
DWriteCreateFactory: _Callable[[_enum.DWRITE_FACTORY_TYPE,  # factoryType
                                _Pointer[_struct.IID],  # iid
                                _Pointer[_Unknwnbase.IUnknown]],  # factory
                               _type.HRESULT]

_WinLib(__name__)
