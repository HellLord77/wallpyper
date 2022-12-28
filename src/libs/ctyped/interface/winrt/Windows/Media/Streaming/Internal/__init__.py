from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Streaming as _Windows_Media_Streaming
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IMediaRendererBrokerStatics(_inspectable.IInspectable):
    CreateMediaRendererAsync: _Callable[[_type.HSTRING,  # deviceIdentifier
                                         _inspectable.IInspectable,  # mediaSessionFactoryMF
                                         _type.HSTRING,  # applicationUserModelId
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Streaming.IMediaRenderer]]],  # value
                                        _type.HRESULT]
    CreateMediaRendererFromBasicDeviceAsync: _Callable[[_Windows_Media_Streaming.IBasicDevice,  # basicDevice
                                                        _inspectable.IInspectable,  # mediaSessionFactoryMF
                                                        _type.HSTRING,  # applicationUserModelId
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Streaming.IMediaRenderer]]],  # value
                                                       _type.HRESULT]

    _factory = True
