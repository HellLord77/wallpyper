from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IDataProtectionProvider(_inspectable.IInspectable):
    ProtectAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # value
                            _type.HRESULT]
    UnprotectAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # value
                              _type.HRESULT]
    ProtectStreamAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # src
                                   _Windows_Storage_Streams.IOutputStream,  # dest
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                  _type.HRESULT]
    UnprotectStreamAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # src
                                     _Windows_Storage_Streams.IOutputStream,  # dest
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                    _type.HRESULT]


class IDataProtectionProviderFactory(_inspectable.IInspectable, factory=True):
    CreateOverloadExplicit: _Callable[[_type.HSTRING,  # protectionDescriptor
                                       _Pointer[IDataProtectionProvider]],  # value
                                      _type.HRESULT]
