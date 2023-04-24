from __future__ import annotations

from typing import Callable as _Callable

from ... import Storage as _Windows_Storage
from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IApplicationDataManager(_inspectable.IInspectable):
    pass


class IApplicationDataManagerStatics(_inspectable.IInspectable):
    CreateForPackageFamily: _Callable[[_type.HSTRING,  # packageFamilyName
                                       _Pointer[_Windows_Storage.IApplicationData]],  # applicationData
                                      _type.HRESULT]

    _factory = True
