from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type

# wingdi
AlphaBlend: _Callable[[_type.HDC,  # hdcDest
                       _type.c_int,  # xoriginDest
                       _type.c_int,  # yoriginDest
                       _type.c_int,  # wDest
                       _type.c_int,  # hDest
                       _type.HDC,  # hdcSrc
                       _type.c_int,  # xoriginSrc
                       _type.c_int,  # yoriginSrc
                       _type.c_int,  # wSrc
                       _type.c_int,  # hSrc
                       _struct.BLENDFUNCTION],  # ftn
                      _type.BOOL]

_WinLib(__name__)
