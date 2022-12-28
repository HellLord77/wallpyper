from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IInstalledDesktopApp(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Publisher: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_DisplayVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IInstalledDesktopAppStatics(_inspectable.IInspectable):
    GetInventoryAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IInstalledDesktopApp]]]],  # operation
                                 _type.HRESULT]

    _factory = True
