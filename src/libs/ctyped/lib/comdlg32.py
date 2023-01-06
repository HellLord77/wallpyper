from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# commdlg
ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]],
                        _type.BOOL]
ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]],
                        _type.BOOL]

_WinLib(__name__)
