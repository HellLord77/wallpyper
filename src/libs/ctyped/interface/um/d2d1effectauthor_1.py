from __future__ import annotations as _

from typing import Callable as _Callable

from . import d2d1_3 as _d2d1_3
from . import d2d1effectauthor as _d2d1effectauthor
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID2D1EffectContext1(_d2d1effectauthor.ID2D1EffectContext):
    CreateLookupTable3D: _Callable[[_enum.D2D1_BUFFER_PRECISION,  # precision
                                    _Pointer[_type.UINT32],  # extents
                                    _Pointer[_type.BYTE],  # data
                                    _type.UINT32,  # dataCount
                                    _Pointer[_type.UINT32],  # strides
                                    _Pointer[_d2d1_3.ID2D1LookupTable3D]],  # lookupTable
                                   _type.HRESULT]


class ID2D1EffectContext2(ID2D1EffectContext1):
    CreateColorContextFromDxgiColorSpace: _Callable[[_enum.DXGI_COLOR_SPACE_TYPE,  # colorSpace
                                                     _Pointer[_d2d1_3.ID2D1ColorContext1]],  # colorContext
                                                    _type.HRESULT]
    CreateColorContextFromSimpleColorProfile: _Callable[[_Pointer[_struct.D2D1_SIMPLE_COLOR_PROFILE],  # simpleProfile
                                                         _Pointer[_d2d1_3.ID2D1ColorContext1]],  # colorContext
                                                        _type.HRESULT]
