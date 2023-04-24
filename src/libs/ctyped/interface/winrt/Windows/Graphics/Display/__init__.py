from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IDisplayPropertiesEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable],  # sender
                      _type.HRESULT]


class IDisplayPropertiesEventHandler(_IDisplayPropertiesEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDisplayPropertiesEventHandler_impl(_IDisplayPropertiesEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAdvancedColorInfo(_inspectable.IInspectable):
    get_CurrentAdvancedColorKind: _Callable[[_Pointer[_enum.Windows.Graphics.Display.AdvancedColorKind]],  # value
                                            _type.HRESULT]
    get_RedPrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    get_GreenPrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                _type.HRESULT]
    get_BluePrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                               _type.HRESULT]
    get_WhitePoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    get_MaxLuminanceInNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_MinLuminanceInNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_MaxAverageFullFrameLuminanceInNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                      _type.HRESULT]
    get_SdrWhiteLevelInNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                                       _type.HRESULT]
    IsHdrMetadataFormatCurrentlySupported: _Callable[[_enum.Windows.Graphics.Display.HdrMetadataFormat,  # format
                                                      _Pointer[_type.boolean]],  # result
                                                     _type.HRESULT]
    IsAdvancedColorKindAvailable: _Callable[[_enum.Windows.Graphics.Display.AdvancedColorKind,  # kind
                                             _Pointer[_type.boolean]],  # result
                                            _type.HRESULT]


class IBrightnessOverride(_inspectable.IInspectable):
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsOverrideActive: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_BrightnessLevel: _Callable[[_Pointer[_type.DOUBLE]],  # level
                                   _type.HRESULT]
    SetBrightnessLevel: _Callable[[_type.DOUBLE,  # brightnessLevel
                                   _enum.Windows.Graphics.Display.DisplayBrightnessOverrideOptions],  # options
                                  _type.HRESULT]
    SetBrightnessScenario: _Callable[[_enum.Windows.Graphics.Display.DisplayBrightnessScenario,  # scenario
                                      _enum.Windows.Graphics.Display.DisplayBrightnessOverrideOptions],  # options
                                     _type.HRESULT]
    GetLevelForScenario: _Callable[[_enum.Windows.Graphics.Display.DisplayBrightnessScenario,  # scenario
                                    _Pointer[_type.DOUBLE]],  # brightnessLevel
                                   _type.HRESULT]
    StartOverride: _Callable[[],
                             _type.HRESULT]
    StopOverride: _Callable[[],
                            _type.HRESULT]
    add_IsSupportedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBrightnessOverride, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_IsSupportedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_IsOverrideActiveChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBrightnessOverride, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_IsOverrideActiveChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_BrightnessLevelChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IBrightnessOverride, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_BrightnessLevelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IBrightnessOverrideSettings(_inspectable.IInspectable):
    get_DesiredLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_DesiredNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]


class IBrightnessOverrideSettingsStatics(_inspectable.IInspectable):
    CreateFromLevel: _Callable[[_type.DOUBLE,  # level
                                _Pointer[IBrightnessOverrideSettings]],  # result
                               _type.HRESULT]
    CreateFromNits: _Callable[[_type.FLOAT,  # nits
                               _Pointer[IBrightnessOverrideSettings]],  # result
                              _type.HRESULT]
    CreateFromDisplayBrightnessOverrideScenario: _Callable[[_enum.Windows.Graphics.Display.DisplayBrightnessOverrideScenario,  # overrideScenario
                                                            _Pointer[IBrightnessOverrideSettings]],  # result
                                                           _type.HRESULT]

    _factory = True


class IBrightnessOverrideStatics(_inspectable.IInspectable):
    GetDefaultForSystem: _Callable[[_Pointer[IBrightnessOverride]],  # value
                                   _type.HRESULT]
    GetForCurrentView: _Callable[[_Pointer[IBrightnessOverride]],  # value
                                 _type.HRESULT]
    SaveForSystemAsync: _Callable[[IBrightnessOverride,  # value
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                  _type.HRESULT]

    _factory = True


class IColorOverrideSettings(_inspectable.IInspectable):
    get_DesiredDisplayColorOverrideScenario: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayColorOverrideScenario]],  # value
                                                       _type.HRESULT]


class IColorOverrideSettingsStatics(_inspectable.IInspectable):
    CreateFromDisplayColorOverrideScenario: _Callable[[_enum.Windows.Graphics.Display.DisplayColorOverrideScenario,  # overrideScenario
                                                       _Pointer[IColorOverrideSettings]],  # result
                                                      _type.HRESULT]

    _factory = True


class IDisplayEnhancementOverride(_inspectable.IInspectable):
    get_ColorOverrideSettings: _Callable[[_Pointer[IColorOverrideSettings]],  # value
                                         _type.HRESULT]
    put_ColorOverrideSettings: _Callable[[IColorOverrideSettings],  # value
                                         _type.HRESULT]
    get_BrightnessOverrideSettings: _Callable[[_Pointer[IBrightnessOverrideSettings]],  # value
                                              _type.HRESULT]
    put_BrightnessOverrideSettings: _Callable[[IBrightnessOverrideSettings],  # value
                                              _type.HRESULT]
    get_CanOverride: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsOverrideActive: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    GetCurrentDisplayEnhancementOverrideCapabilities: _Callable[[_Pointer[IDisplayEnhancementOverrideCapabilities]],  # value
                                                                _type.HRESULT]
    RequestOverride: _Callable[[],
                               _type.HRESULT]
    StopOverride: _Callable[[],
                            _type.HRESULT]
    add_CanOverrideChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayEnhancementOverride, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CanOverrideChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_IsOverrideActiveChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayEnhancementOverride, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_IsOverrideActiveChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_DisplayEnhancementOverrideCapabilitiesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayEnhancementOverride, IDisplayEnhancementOverrideCapabilitiesChangedEventArgs],  # handler
                                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                                 _type.HRESULT]
    remove_DisplayEnhancementOverrideCapabilitiesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                                    _type.HRESULT]


class IDisplayEnhancementOverrideCapabilities(_inspectable.IInspectable):
    get_IsBrightnessControlSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_IsBrightnessNitsControlSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
    GetSupportedNitRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Graphics.Display.NitRange]]],  # result
                                     _type.HRESULT]


class IDisplayEnhancementOverrideCapabilitiesChangedEventArgs(_inspectable.IInspectable):
    get_Capabilities: _Callable[[_Pointer[IDisplayEnhancementOverrideCapabilities]],  # value
                                _type.HRESULT]


class IDisplayEnhancementOverrideStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IDisplayEnhancementOverride]],  # result
                                 _type.HRESULT]

    _factory = True


class IDisplayInformation(_inspectable.IInspectable):
    get_CurrentOrientation: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                      _type.HRESULT]
    get_NativeOrientation: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                     _type.HRESULT]
    add_OrientationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_OrientationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    get_ResolutionScale: _Callable[[_Pointer[_enum.Windows.Graphics.Display.ResolutionScale]],  # value
                                   _type.HRESULT]
    get_LogicalDpi: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    get_RawDpiX: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    get_RawDpiY: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    add_DpiChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_DpiChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    get_StereoEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    add_StereoEnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_StereoEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    GetColorProfileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # asyncInfo
                                    _type.HRESULT]
    add_ColorProfileChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ColorProfileChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IDisplayInformation2(_inspectable.IInspectable):
    get_RawPixelsPerViewPixel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]


class IDisplayInformation3(_inspectable.IInspectable):
    get_DiagonalSizeInInches: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                        _type.HRESULT]


class IDisplayInformation4(_inspectable.IInspectable):
    get_ScreenWidthInRawPixels: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_ScreenHeightInRawPixels: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]


class IDisplayInformation5(_inspectable.IInspectable):
    GetAdvancedColorInfo: _Callable[[_Pointer[IAdvancedColorInfo]],  # value
                                    _type.HRESULT]
    add_AdvancedColorInfoChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_AdvancedColorInfoChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]


class IDisplayInformationStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IDisplayInformation]],  # current
                                 _type.HRESULT]
    get_AutoRotationPreferences: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                           _type.HRESULT]
    put_AutoRotationPreferences: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                           _type.HRESULT]
    add_DisplayContentsInvalidated: _Callable[[_Windows_Foundation.ITypedEventHandler[IDisplayInformation, _inspectable.IInspectable],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_DisplayContentsInvalidated: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]

    _factory = True


class IDisplayPropertiesStatics(_inspectable.IInspectable):
    CurrentOrientation: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                  _type.HRESULT]
    NativeOrientation: _Callable[[_Pointer[_enum.Windows.Graphics.Display.DisplayOrientations]],  # value
                                 _type.HRESULT]
    AutoRotationPreferences: _Callable[[_enum.Windows.Graphics.Display.DisplayOrientations],  # value
                                       _type.HRESULT]
    OrientationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    ResolutionScale: _Callable[[_Pointer[_enum.Windows.Graphics.Display.ResolutionScale]],  # value
                               _type.HRESULT]
    LogicalDpi: _Callable[[_Pointer[_type.FLOAT]],  # value
                          _type.HRESULT]
    LogicalDpiChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    StereoEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    StereoEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    GetColorProfileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # asyncInfo
                                    _type.HRESULT]
    ColorProfileChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    DisplayContentsInvalidated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]

    _factory = True


class IDisplayServices(_inspectable.IInspectable):
    pass


class IDisplayServicesStatics(_inspectable.IInspectable):
    FindAll: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                        _Pointer[_Pointer[_struct.Windows.Graphics.DisplayId]]],  # result
                       _type.HRESULT]

    _factory = True
