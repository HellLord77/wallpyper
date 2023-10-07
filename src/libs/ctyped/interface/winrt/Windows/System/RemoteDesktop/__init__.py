from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IInteractiveSessionStatics(_inspectable.IInspectable, factory=True):
    get_IsRemote: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
