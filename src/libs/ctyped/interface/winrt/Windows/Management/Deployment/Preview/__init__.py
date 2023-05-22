from __future__ import annotations

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IClassicAppManagerStatics(_inspectable.IInspectable, factory=True):
    FindInstalledApp: _Callable[[_type.HSTRING,  # appUninstallKey
                                 _Pointer[IInstalledClassicAppInfo]],  # result
                                _type.HRESULT]


class IInstalledClassicAppInfo(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DisplayVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
