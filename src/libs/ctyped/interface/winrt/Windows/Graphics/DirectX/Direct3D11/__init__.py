from __future__ import annotations

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDirect3DDevice(_inspectable.IInspectable):
    Trim: _Callable[[],
                    _type.HRESULT]


class IDirect3DSurface(_inspectable.IInspectable):
    get_Description: _Callable[[_Pointer[_struct.Windows.Graphics.DirectX.Direct3D11.Direct3DSurfaceDescription]],  # value
                               _type.HRESULT]
