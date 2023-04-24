from __future__ import annotations

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IDesktopWindowTarget(_inspectable.IInspectable):
    get_IsTopmost: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
