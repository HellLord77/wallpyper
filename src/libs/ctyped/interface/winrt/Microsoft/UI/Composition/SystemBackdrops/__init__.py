from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Composition as _Microsoft_UI_Composition
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.UI import Composition as _Windows_UI_Composition
from .....Windows.UI import Core as _Windows_UI_Core
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDesktopAcrylicController(_inspectable.IInspectable):
    get_FallbackColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    put_FallbackColor: _Callable[[_struct.Windows.UI.Color],  # value
                                 _type.HRESULT]
    get_LuminosityOpacity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                     _type.HRESULT]
    put_LuminosityOpacity: _Callable[[_type.FLOAT],  # value
                                     _type.HRESULT]
    get_TintColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    put_TintColor: _Callable[[_struct.Windows.UI.Color],  # value
                             _type.HRESULT]
    get_TintOpacity: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_TintOpacity: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]


class IDesktopAcrylicController2(_inspectable.IInspectable):
    ResetProperties: _Callable[[],
                               _type.HRESULT]


class IDesktopAcrylicController3(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicKind],  # value
                        _type.HRESULT]


class IDesktopAcrylicControllerStatics(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IMicaController(_inspectable.IInspectable):
    get_FallbackColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                 _type.HRESULT]
    put_FallbackColor: _Callable[[_struct.Windows.UI.Color],  # value
                                 _type.HRESULT]
    get_LuminosityOpacity: _Callable[[_Pointer[_type.FLOAT]],  # value
                                     _type.HRESULT]
    put_LuminosityOpacity: _Callable[[_type.FLOAT],  # value
                                     _type.HRESULT]
    get_TintColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    put_TintColor: _Callable[[_struct.Windows.UI.Color],  # value
                             _type.HRESULT]
    get_TintOpacity: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_TintOpacity: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]


class IMicaController2(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.SystemBackdrops.MicaKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Microsoft.UI.Composition.SystemBackdrops.MicaKind],  # value
                        _type.HRESULT]
    ResetProperties: _Callable[[],
                               _type.HRESULT]


class IMicaControllerStatics(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class ISystemBackdropConfiguration(_inspectable.IInspectable):
    get_HighContrastBackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                               _type.HRESULT]
    put_HighContrastBackgroundColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                               _type.HRESULT]
    get_IsHighContrast: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsHighContrast: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_IsInputActive: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsInputActive: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_Theme: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropTheme]],  # value
                         _type.HRESULT]
    put_Theme: _Callable[[_enum.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropTheme],  # value
                         _type.HRESULT]


class ISystemBackdropController(_inspectable.IInspectable):
    SetTargetWithWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                                      _Windows_UI_Composition.ICompositionTarget,  # desktopWindowTarget
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    SetTargetWithCoreWindow: _Callable[[_Windows_UI_Core.ICoreWindow,  # coreWindow
                                        _Windows_UI_Composition.ICompositionTarget,  # compositionTarget
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]


class ISystemBackdropControllerWithTargets(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropState]],  # value
                         _type.HRESULT]
    AddSystemBackdropTarget: _Callable[[_Microsoft_UI_Composition.ICompositionSupportsSystemBackdrop,  # systemBackdropTarget
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    RemoveAllSystemBackdropTargets: _Callable[[],
                                              _type.HRESULT]
    RemoveSystemBackdropTarget: _Callable[[_Microsoft_UI_Composition.ICompositionSupportsSystemBackdrop,  # systemBackdropTarget
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]
    SetSystemBackdropConfiguration: _Callable[[ISystemBackdropConfiguration],  # configuration
                                              _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemBackdropControllerWithTargets, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
