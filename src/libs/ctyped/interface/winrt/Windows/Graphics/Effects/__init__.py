from __future__ import annotations

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IGraphicsEffect(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # name
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # name
                        _type.HRESULT]


class IGraphicsEffectSource(_inspectable.IInspectable):
    pass
