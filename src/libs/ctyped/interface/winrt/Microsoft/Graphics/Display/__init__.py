from __future__ import annotations as _

from typing import Callable as _Callable

from ...UI import Dispatching as _Microsoft_UI_Dispatching
from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ....Windows.Storage import Streams as _Windows_Storage_Streams
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDisplayAdvancedColorInfo(_inspectable.IInspectable):
    get_CurrentAdvancedColorKind: _Callable[[_Pointer[_enum.Microsoft.Graphics.Display.DisplayAdvancedColorKind]],  # value
                                            _type.HRESULT]
    get_RedPrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    get_GreenPrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                _type.HRESULT]
    get_BluePrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                               _type.HRESULT]
    get_WhitePoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    get_MaxLuminanceInNits: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    get_MinLuminanceInNits: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    get_MaxAverageFullFrameLuminanceInNits: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                      _type.HRESULT]
    get_SdrWhiteLevelInNits: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    IsHdrMetadataFormatCurrentlySupported: _Callable[[_enum.Microsoft.Graphics.Display.DisplayHdrMetadataFormat,  # format
                                                      _Pointer[_type.boolean]],  # result
                                                     _type.HRESULT]
    IsAdvancedColorKindAvailable: _Callable[[_enum.Microsoft.Graphics.Display.DisplayAdvancedColorKind,  # kind
                                             _Pointer[_type.boolean]],  # result
                                            _type.HRESULT]


class IDisplayInformation(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    get_IsStereoEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    add_IsStereoEnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_IsStereoEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    GetColorProfileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                                    _type.HRESULT]
    GetColorProfile: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # result
                               _type.HRESULT]
    add_ColorProfileChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ColorProfileChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetAdvancedColorInfo: _Callable[[_Pointer[IDisplayAdvancedColorInfo]],  # result
                                    _type.HRESULT]
    add_AdvancedColorInfoChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_AdvancedColorInfoChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_Destroyed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Destroyed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]


class IDisplayInformationStatics(_inspectable.IInspectable, factory=True):
    CreateForWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                                  _Pointer[IDisplayInformation]],  # result
                                 _type.HRESULT]
    CreateForDisplayId: _Callable[[_struct.Microsoft.UI.DisplayId,  # displayId
                                   _Pointer[IDisplayInformation]],  # result
                                  _type.HRESULT]
