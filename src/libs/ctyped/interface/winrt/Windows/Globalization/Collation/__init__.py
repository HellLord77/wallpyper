from __future__ import annotations

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class ICharacterGrouping(_inspectable.IInspectable):
    get_First: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class ICharacterGroupings(_inspectable.IInspectable):
    Lookup: _Callable[[_type.HSTRING,  # text
                       _Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]


class ICharacterGroupingsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # language
                       _Pointer[ICharacterGroupings]],  # result
                      _type.HRESULT]
