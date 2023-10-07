from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IHdmiDisplayInformation(_inspectable.IInspectable):
    GetSupportedDisplayModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHdmiDisplayMode]]],  # result
                                        _type.HRESULT]
    GetCurrentDisplayMode: _Callable[[_Pointer[IHdmiDisplayMode]],  # result
                                     _type.HRESULT]
    SetDefaultDisplayModeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                          _type.HRESULT]
    RequestSetCurrentDisplayModeAsync: _Callable[[IHdmiDisplayMode,  # mode
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                 _type.HRESULT]
    RequestSetCurrentDisplayModeWithHdrAsync: _Callable[[IHdmiDisplayMode,  # mode
                                                         _enum.Windows.Graphics.Display.Core.HdmiDisplayHdrOption,  # hdrOption
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                        _type.HRESULT]
    RequestSetCurrentDisplayModeWithHdrAndMetadataAsync: _Callable[[IHdmiDisplayMode,  # mode
                                                                    _enum.Windows.Graphics.Display.Core.HdmiDisplayHdrOption,  # hdrOption
                                                                    _struct.Windows.Graphics.Display.Core.HdmiDisplayHdr2086Metadata,  # hdrMetadata
                                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                                   _type.HRESULT]
    add_DisplayModesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IHdmiDisplayInformation, _inspectable.IInspectable],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_DisplayModesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IHdmiDisplayInformationStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IHdmiDisplayInformation]],  # result
                                 _type.HRESULT]


class IHdmiDisplayMode(_inspectable.IInspectable):
    get_ResolutionWidthInRawPixels: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]
    get_ResolutionHeightInRawPixels: _Callable[[_Pointer[_type.UINT32]],  # value
                                               _type.HRESULT]
    get_RefreshRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    get_StereoEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_BitsPerPixel: _Callable[[_Pointer[_type.UINT16]],  # value
                                _type.HRESULT]
    IsEqual: _Callable[[IHdmiDisplayMode,  # mode
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    get_ColorSpace: _Callable[[_Pointer[_enum.Windows.Graphics.Display.Core.HdmiDisplayColorSpace]],  # value
                              _type.HRESULT]
    get_PixelEncoding: _Callable[[_Pointer[_enum.Windows.Graphics.Display.Core.HdmiDisplayPixelEncoding]],  # value
                                 _type.HRESULT]
    get_IsSdrLuminanceSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_IsSmpte2084Supported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_Is2086MetadataSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class IHdmiDisplayMode2(_inspectable.IInspectable):
    get_IsDolbyVisionLowLatencySupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
