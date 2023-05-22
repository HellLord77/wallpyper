from __future__ import annotations

from typing import Callable as _Callable

from .. import Custom as _Windows_Gaming_Input_Custom
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IGameControllerProviderInfoStatics(_inspectable.IInspectable, factory=True):
    GetParentProviderId: _Callable[[_Windows_Gaming_Input_Custom.IGameControllerProvider,  # provider
                                    _Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    GetProviderId: _Callable[[_Windows_Gaming_Input_Custom.IGameControllerProvider,  # provider
                              _Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
