from __future__ import annotations

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IHtmlUtilities(_inspectable.IInspectable):
    ConvertToText: _Callable[[_type.HSTRING,  # html
                              _Pointer[_type.HSTRING]],  # text
                             _type.HRESULT]

    _factory = True
