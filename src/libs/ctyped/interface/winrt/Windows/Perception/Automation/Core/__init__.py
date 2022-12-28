from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import type as _type


class ICorePerceptionAutomationStatics(_inspectable.IInspectable):
    SetActivationFactoryProvider: _Callable[[_Windows_Foundation.IGetActivationFactory],  # provider
                                            _type.HRESULT]

    _factory = True
