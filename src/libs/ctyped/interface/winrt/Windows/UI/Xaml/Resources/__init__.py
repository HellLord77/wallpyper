from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class ICustomXamlResourceLoader(_inspectable.IInspectable):
    pass


class ICustomXamlResourceLoaderFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICustomXamlResourceLoader]],  # value
                              _type.HRESULT]


class ICustomXamlResourceLoaderOverrides(_inspectable.IInspectable):
    GetResource: _Callable[[_type.HSTRING,  # resourceId
                            _type.HSTRING,  # objectType
                            _type.HSTRING,  # propertyName
                            _type.HSTRING,  # propertyType
                            _Pointer[_inspectable.IInspectable]],  # result
                           _type.HRESULT]


class ICustomXamlResourceLoaderStatics(_inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[ICustomXamlResourceLoader]],  # value
                           _type.HRESULT]
    put_Current: _Callable[[ICustomXamlResourceLoader],  # value
                           _type.HRESULT]

    _factory = True
