from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Composition as _Microsoft_UI_Composition
from .. import Dispatching as _Microsoft_UI_Dispatching
from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from ....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IContentCoordinateConverter(_inspectable.IInspectable):
    ConvertLocalToScreenWithPoint: _Callable[[_struct.Windows.Foundation.Point,  # localPoint
                                              _Pointer[_struct.Windows.Graphics.PointInt32]],  # result
                                             _type.HRESULT]
    ConvertLocalToScreenWithPoints: _Callable[[_type.UINT32,  # __localPointsSize
                                               _Pointer[_struct.Windows.Foundation.Point],  # localPoints
                                               _Pointer[_type.UINT32],  # __resultSize
                                               _Pointer[_Pointer[_struct.Windows.Graphics.PointInt32]]],  # result
                                              _type.HRESULT]
    ConvertLocalToScreenWithPointsAndRoundingMode: _Callable[[_type.UINT32,  # __localPointsSize
                                                              _Pointer[_struct.Windows.Foundation.Point],  # localPoints
                                                              _enum.Microsoft.UI.Content.ContentCoordinateRoundingMode,  # roundingMode
                                                              _Pointer[_type.UINT32],  # __resultSize
                                                              _Pointer[_Pointer[_struct.Windows.Graphics.PointInt32]]],  # result
                                                             _type.HRESULT]
    ConvertLocalToScreenWithRect: _Callable[[_struct.Windows.Foundation.Rect,  # localRect
                                             _Pointer[_struct.Windows.Graphics.RectInt32]],  # result
                                            _type.HRESULT]
    ConvertScreenToLocalWithPoint: _Callable[[_struct.Windows.Graphics.PointInt32,  # screenPoint
                                              _Pointer[_struct.Windows.Foundation.Point]],  # result
                                             _type.HRESULT]
    ConvertScreenToLocalWithPoints: _Callable[[_type.UINT32,  # __screenPointsSize
                                               _Pointer[_struct.Windows.Graphics.PointInt32],  # screenPoints
                                               _Pointer[_type.UINT32],  # __resultSize
                                               _Pointer[_Pointer[_struct.Windows.Foundation.Point]]],  # result
                                              _type.HRESULT]
    ConvertScreenToLocalWithRect: _Callable[[_struct.Windows.Graphics.RectInt32,  # screenRect
                                             _Pointer[_struct.Windows.Foundation.Rect]],  # result
                                            _type.HRESULT]


class IContentCoordinateConverterFactory(_inspectable.IInspectable):
    pass


class IContentCoordinateConverterStatics(_inspectable.IInspectable, factory=True):
    CreateForWindowId: _Callable[[_struct.Microsoft.UI.WindowId,  # windowId
                                  _Pointer[IContentCoordinateConverter]],  # result
                                 _type.HRESULT]


class IContentDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IContentEnvironmentSettingChangedEventArgs(_inspectable.IInspectable):
    get_SettingName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IContentEnvironmentStateChangedEventArgs(_inspectable.IInspectable):
    get_DidAppWindowIdChange: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_DidDisplayIdChange: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IContentIsland(_inspectable.IInspectable):
    get_ActualSize: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                              _type.HRESULT]
    get_AppData: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]
    put_AppData: _Callable[[_inspectable.IInspectable],  # value
                           _type.HRESULT]
    get_CoordinateConverter: _Callable[[_Pointer[IContentCoordinateConverter]],  # value
                                       _type.HRESULT]
    get_CustomProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                    _type.HRESULT]
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    get_Environment: _Callable[[_Pointer[IContentIslandEnvironment]],  # value
                               _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT64]],  # value
                      _type.HRESULT]
    get_IsConnected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsHitTestVisibleWhenTransparent: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_IsHitTestVisibleWhenTransparent: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_IsIslandEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsIslandEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsIslandVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsIslandVisible: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsSiteEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsSiteVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_LayoutDirection: _Callable[[_Pointer[_enum.Microsoft.UI.Content.ContentLayoutDirection]],  # value
                                   _type.HRESULT]
    get_RasterizationScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    GetAutomationHostProvider: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                                         _type.HRESULT]
    GetStateChangeDeferral: _Callable[[_Pointer[IContentDeferral]],  # result
                                      _type.HRESULT]
    RequestSize: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # size
                           _type.HRESULT]
    add_AutomationProviderRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentIsland, IContentIslandAutomationProviderRequestedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_AutomationProviderRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentIsland, IContentIslandStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IContentIslandAutomationProviderRequestedEventArgs(_inspectable.IInspectable):
    get_AutomationProvider: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                      _type.HRESULT]
    put_AutomationProvider: _Callable[[_inspectable.IInspectable],  # value
                                      _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IContentIslandEnvironment(_inspectable.IInspectable):
    get_AppWindowId: _Callable[[_Pointer[_struct.Microsoft.UI.WindowId]],  # value
                               _type.HRESULT]
    get_DisplayId: _Callable[[_Pointer[_struct.Microsoft.UI.DisplayId]],  # value
                             _type.HRESULT]
    add_SettingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentIslandEnvironment, IContentEnvironmentSettingChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_SettingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentIslandEnvironment, IContentEnvironmentStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IContentIslandEnvironmentFactory(_inspectable.IInspectable):
    pass


class IContentIslandFactory(_inspectable.IInspectable):
    pass


class IContentIslandStateChangedEventArgs(_inspectable.IInspectable):
    get_DidActualSizeChange: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_DidSiteEnabledChange: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_DidSiteVisibleChange: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_DidLayoutDirectionChange: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_DidRasterizationScaleChange: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IContentIslandStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.IVisual,  # Root
                       _Pointer[IContentIsland]],  # result
                      _type.HRESULT]
    FindAllForCompositor: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                                     _Pointer[_type.UINT32],  # __resultSize
                                     _Pointer[_Pointer[IContentIsland]]],  # result
                                    _type.HRESULT]
    FindAllForCurrentThread: _Callable[[_Pointer[_type.UINT32],  # __resultSize
                                        _Pointer[_Pointer[IContentIsland]]],  # result
                                       _type.HRESULT]
    GetByVisual: _Callable[[_Microsoft_UI_Composition.IVisual,  # child
                            _Pointer[IContentIsland]],  # result
                           _type.HRESULT]
    GetFromId: _Callable[[_type.UINT64,  # id
                          _Pointer[IContentIsland]],  # result
                         _type.HRESULT]


class IContentSite(_inspectable.IInspectable):
    get_ActualSize: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                              _type.HRESULT]
    put_ActualSize: _Callable[[_struct.Windows.Foundation.Numerics.Vector2],  # value
                              _type.HRESULT]
    get_ClientSize: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                              _type.HRESULT]
    put_ClientSize: _Callable[[_struct.Windows.Graphics.SizeInt32],  # value
                              _type.HRESULT]
    get_CoordinateConverter: _Callable[[_Pointer[IContentCoordinateConverter]],  # value
                                       _type.HRESULT]
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    get_Environment: _Callable[[_Pointer[IContentSiteEnvironment]],  # value
                               _type.HRESULT]
    get_IsConnected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsSiteEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsSiteEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsSiteVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsSiteVisible: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_LayoutDirection: _Callable[[_Pointer[_enum.Microsoft.UI.Content.ContentLayoutDirection]],  # value
                                   _type.HRESULT]
    put_LayoutDirection: _Callable[[_enum.Microsoft.UI.Content.ContentLayoutDirection],  # value
                                   _type.HRESULT]
    get_OverrideScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_OverrideScale: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_ParentScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_ParentScale: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_RasterizationScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_RequestedSize: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                 _type.HRESULT]
    get_ShouldApplyRasterizationScale: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_ShouldApplyRasterizationScale: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_View: _Callable[[_Pointer[IContentSiteView]],  # value
                        _type.HRESULT]
    GetIslandStateChangeDeferral: _Callable[[_Pointer[IContentDeferral]],  # result
                                            _type.HRESULT]
    add_RequestedStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IContentSite, IContentSiteRequestedStateChangedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_RequestedStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class IContentSiteBridge(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    get_LayoutDirectionOverride: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Microsoft.UI.Content.ContentLayoutDirection]]],  # value
                                           _type.HRESULT]
    put_LayoutDirectionOverride: _Callable[[_Windows_Foundation.IReference[_enum.Microsoft.UI.Content.ContentLayoutDirection]],  # value
                                           _type.HRESULT]
    get_OverrideScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_OverrideScale: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]


class IContentSiteEnvironment(_inspectable.IInspectable):
    get_AppWindowId: _Callable[[_Pointer[_struct.Microsoft.UI.WindowId]],  # value
                               _type.HRESULT]
    put_AppWindowId: _Callable[[_struct.Microsoft.UI.WindowId],  # value
                               _type.HRESULT]
    get_DisplayId: _Callable[[_Pointer[_struct.Microsoft.UI.DisplayId]],  # value
                             _type.HRESULT]
    put_DisplayId: _Callable[[_struct.Microsoft.UI.DisplayId],  # value
                             _type.HRESULT]
    get_View: _Callable[[_Pointer[IContentSiteEnvironmentView]],  # value
                        _type.HRESULT]
    NotifySettingChanged: _Callable[[_type.HSTRING],  # setting
                                    _type.HRESULT]


class IContentSiteEnvironmentFactory(_inspectable.IInspectable):
    pass


class IContentSiteEnvironmentView(_inspectable.IInspectable):
    get_AppWindowId: _Callable[[_Pointer[_struct.Microsoft.UI.WindowId]],  # value
                               _type.HRESULT]
    get_DisplayId: _Callable[[_Pointer[_struct.Microsoft.UI.DisplayId]],  # value
                             _type.HRESULT]


class IContentSiteEnvironmentViewFactory(_inspectable.IInspectable):
    pass


class IContentSiteFactory(_inspectable.IInspectable):
    pass


class IContentSiteRequestedStateChangedEventArgs(_inspectable.IInspectable):
    get_DidRequestedSizeChange: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IContentSiteView(_inspectable.IInspectable):
    get_ActualSize: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                              _type.HRESULT]
    get_ClientSize: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                              _type.HRESULT]
    get_CoordinateConverter: _Callable[[_Pointer[IContentCoordinateConverter]],  # value
                                       _type.HRESULT]
    get_DispatcherQueue: _Callable[[_Pointer[_Microsoft_UI_Dispatching.IDispatcherQueue]],  # value
                                   _type.HRESULT]
    get_EnvironmentView: _Callable[[_Pointer[IContentSiteEnvironmentView]],  # value
                                   _type.HRESULT]
    get_IsConnected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsSiteEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsSiteVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_LayoutDirection: _Callable[[_Pointer[_enum.Microsoft.UI.Content.ContentLayoutDirection]],  # value
                                   _type.HRESULT]
    get_OverrideScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    get_ParentScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    get_RasterizationScale: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_RequestedSize: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector2]],  # value
                                 _type.HRESULT]
    get_ShouldApplyRasterizationScale: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]


class IContentSiteViewFactory(_inspectable.IInspectable):
    pass


class IDesktopChildSiteBridge(_inspectable.IInspectable):
    get_ResizePolicy: _Callable[[_Pointer[_enum.Microsoft.UI.Content.ContentSizePolicy]],  # value
                                _type.HRESULT]
    put_ResizePolicy: _Callable[[_enum.Microsoft.UI.Content.ContentSizePolicy],  # value
                                _type.HRESULT]
    get_SiteView: _Callable[[_Pointer[IContentSiteView]],  # value
                            _type.HRESULT]


class IDesktopChildSiteBridgeStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Microsoft_UI_Composition.ICompositor,  # compositor
                       _struct.Microsoft.UI.WindowId,  # parentWindowId
                       _Pointer[IDesktopChildSiteBridge]],  # result
                      _type.HRESULT]


class IDesktopSiteBridge(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_WindowId: _Callable[[_Pointer[_struct.Microsoft.UI.WindowId]],  # value
                            _type.HRESULT]
    Connect: _Callable[[IContentIsland],  # content
                       _type.HRESULT]
    Disable: _Callable[[],
                       _type.HRESULT]
    Enable: _Callable[[],
                      _type.HRESULT]
    Hide: _Callable[[],
                    _type.HRESULT]
    MoveAndResize: _Callable[[_struct.Windows.Graphics.RectInt32],  # rect
                             _type.HRESULT]
    MoveInZOrderAtBottom: _Callable[[],
                                    _type.HRESULT]
    MoveInZOrderAtTop: _Callable[[],
                                 _type.HRESULT]
    MoveInZOrderBelow: _Callable[[_struct.Microsoft.UI.WindowId],  # windowId
                                 _type.HRESULT]
    Show: _Callable[[],
                    _type.HRESULT]


class IDesktopSiteBridgeFactory(_inspectable.IInspectable):
    pass


class IDesktopSiteBridgeStatics(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
