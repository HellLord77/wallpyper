from __future__ import annotations as _

from typing import Callable as _Callable

from . import inspectable as _inspectable
from ... import type as _type
from ..._utils import _Pointer


class IActivationFactory(_inspectable.IInspectable):
    ActivateInstance: _Callable[[_Pointer[_inspectable.IInspectable]],  # instance
                                _type.HRESULT]
