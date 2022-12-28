from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import UI as _Windows_UI
from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IResourceLoader(_inspectable.IInspectable):
    GetString: _Callable[[_type.HSTRING,  # resource
                          _Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IResourceLoader2(_inspectable.IInspectable):
    GetStringForUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                _Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IResourceLoaderFactory(_inspectable.IInspectable):
    CreateResourceLoaderByName: _Callable[[_type.HSTRING,  # name
                                           _Pointer[IResourceLoader]],  # loader
                                          _type.HRESULT]

    _factory = True


class IResourceLoaderStatics(_inspectable.IInspectable):
    GetStringForReference: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                      _Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]

    _factory = True


class IResourceLoaderStatics2(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IResourceLoader]],  # loader
                                 _type.HRESULT]
    GetForCurrentViewWithName: _Callable[[_type.HSTRING,  # name
                                          _Pointer[IResourceLoader]],  # loader
                                         _type.HRESULT]
    GetForViewIndependentUse: _Callable[[_Pointer[IResourceLoader]],  # loader
                                        _type.HRESULT]
    GetForViewIndependentUseWithName: _Callable[[_type.HSTRING,  # name
                                                 _Pointer[IResourceLoader]],  # loader
                                                _type.HRESULT]

    _factory = True


class IResourceLoaderStatics3(_inspectable.IInspectable):
    GetForUIContext: _Callable[[_Windows_UI.IUIContext,  # context
                                _Pointer[IResourceLoader]],  # result
                               _type.HRESULT]

    _factory = True


class IResourceLoaderStatics4(_inspectable.IInspectable):
    GetDefaultPriPath: _Callable[[_type.HSTRING,  # packageFullName
                                  _Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]

    _factory = True
