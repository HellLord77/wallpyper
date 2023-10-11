from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# rometadata
MetaDataGetDispenser: _Callable[[_Pointer[_struct.IID],  # rclsid
                                 _Pointer[_struct.IID],  # riid
                                 _type.LPVOID],  # ppv
                                _type.HRESULT]
"""
Creates dispenser class - interfaces IMetaDataDispenser or IMetaDataDispenserEx.
Arguments: rclsid - Only CLSID_CorMetaDataDispenser supported. riid - Interfaces
supported: IID_IMetaDataDispenser, IID_IMetaDataDispenserEx.
"""

_WinLib(__name__)
