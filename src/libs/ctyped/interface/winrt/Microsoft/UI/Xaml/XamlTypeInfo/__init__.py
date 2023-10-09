from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import type as _type


class IXamlControlsXamlMetaDataProvider(_inspectable.IInspectable):
    pass


class IXamlControlsXamlMetaDataProviderStatics(_inspectable.IInspectable):
    Initialize: _Callable[[],
                          _type.HRESULT]
