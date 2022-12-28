from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import type as _type


class IDisplayRequest(_inspectable.IInspectable):
    RequestActive: _Callable[[],
                             _type.HRESULT]
    RequestRelease: _Callable[[],
                              _type.HRESULT]
