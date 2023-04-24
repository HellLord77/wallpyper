from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...ApplicationModel import Core as _Windows_ApplicationModel_Core
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IJumpList(_inspectable.IInspectable):
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IJumpListItem]]],  # value
                         _type.HRESULT]
    get_SystemGroupKind: _Callable[[_Pointer[_enum.Windows.UI.StartScreen.JumpListSystemGroupKind]],  # value
                                   _type.HRESULT]
    put_SystemGroupKind: _Callable[[_enum.Windows.UI.StartScreen.JumpListSystemGroupKind],  # value
                                   _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                         _type.HRESULT]


class IJumpListItem(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.StartScreen.JumpListItemKind]],  # value
                        _type.HRESULT]
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_RemovedByUser: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_GroupName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_GroupName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                        _type.HRESULT]
    put_Logo: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                        _type.HRESULT]


class IJumpListItemStatics(_inspectable.IInspectable):
    CreateWithArguments: _Callable[[_type.HSTRING,  # arguments
                                    _type.HSTRING,  # displayName
                                    _Pointer[IJumpListItem]],  # result
                                   _type.HRESULT]
    CreateSeparator: _Callable[[_Pointer[IJumpListItem]],  # result
                               _type.HRESULT]

    _factory = True


class IJumpListStatics(_inspectable.IInspectable):
    LoadCurrentAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IJumpList]]],  # result
                                _type.HRESULT]
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]

    _factory = True


class ISecondaryTile(_inspectable.IInspectable):
    put_TileId: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_TileId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Arguments: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    ShortName: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                    _type.HRESULT]
    SmallLogo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                         _type.HRESULT]
    WideLogo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                        _type.HRESULT]
    put_LockScreenBadgeLogo: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                       _type.HRESULT]
    get_LockScreenBadgeLogo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                       _type.HRESULT]
    put_LockScreenDisplayBadgeAndTileText: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_LockScreenDisplayBadgeAndTileText: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    TileOptions: _Callable[[_Pointer[_enum.Windows.UI.StartScreen.TileOptions]],  # value
                           _type.HRESULT]
    ForegroundText: _Callable[[_Pointer[_enum.Windows.UI.StartScreen.ForegroundText]],  # value
                              _type.HRESULT]
    BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    RequestCreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                  _type.HRESULT]
    RequestCreateAsyncWithPoint: _Callable[[_struct.Windows.Foundation.Point,  # invocationPoint
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]
    RequestCreateAsyncWithRect: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    RequestCreateAsyncWithRectAndPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                                       _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                      _type.HRESULT]
    RequestDeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                  _type.HRESULT]
    RequestDeleteAsyncWithPoint: _Callable[[_struct.Windows.Foundation.Point,  # invocationPoint
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]
    RequestDeleteAsyncWithRect: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    RequestDeleteAsyncWithRectAndPlacement: _Callable[[_struct.Windows.Foundation.Rect,  # selection
                                                       _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                      _type.HRESULT]
    UpdateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]


class ISecondaryTile2(_inspectable.IInspectable):
    put_PhoneticName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_PhoneticName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_VisualElements: _Callable[[_Pointer[ISecondaryTileVisualElements]],  # value
                                  _type.HRESULT]
    put_RoamingEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_RoamingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    add_VisualElementsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ISecondaryTile, IVisualElementsRequestedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_VisualElementsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class ISecondaryTileFactory(_inspectable.IInspectable):
    CreateTile: _Callable[[_type.HSTRING,  # tileId
                           _type.HSTRING,  # shortName
                           _type.HSTRING,  # displayName
                           _type.HSTRING,  # arguments
                           _enum.Windows.UI.StartScreen.TileOptions,  # tileOptions
                           _Windows_Foundation.IUriRuntimeClass,  # logoReference
                           _Pointer[ISecondaryTile]],  # value
                          _type.HRESULT]
    CreateWideTile: _Callable[[_type.HSTRING,  # tileId
                               _type.HSTRING,  # shortName
                               _type.HSTRING,  # displayName
                               _type.HSTRING,  # arguments
                               _enum.Windows.UI.StartScreen.TileOptions,  # tileOptions
                               _Windows_Foundation.IUriRuntimeClass,  # logoReference
                               _Windows_Foundation.IUriRuntimeClass,  # wideLogoReference
                               _Pointer[ISecondaryTile]],  # value
                              _type.HRESULT]
    CreateWithId: _Callable[[_type.HSTRING,  # tileId
                             _Pointer[ISecondaryTile]],  # value
                            _type.HRESULT]


class ISecondaryTileFactory2(_inspectable.IInspectable):
    CreateMinimalTile: _Callable[[_type.HSTRING,  # tileId
                                  _type.HSTRING,  # displayName
                                  _type.HSTRING,  # arguments
                                  _Windows_Foundation.IUriRuntimeClass,  # square150x150Logo
                                  _enum.Windows.UI.StartScreen.TileSize,  # desiredSize
                                  _Pointer[ISecondaryTile]],  # value
                                 _type.HRESULT]

    _factory = True


class ISecondaryTileStatics(_inspectable.IInspectable):
    Exists: _Callable[[_type.HSTRING,  # tileId
                       _Pointer[_type.boolean]],  # exists
                      _type.HRESULT]
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISecondaryTile]]]],  # operation
                            _type.HRESULT]
    FindAllForApplicationAsync: _Callable[[_type.HSTRING,  # applicationId
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISecondaryTile]]]],  # operation
                                          _type.HRESULT]
    FindAllForPackageAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ISecondaryTile]]]],  # operation
                                      _type.HRESULT]

    _factory = True


class ISecondaryTileVisualElements(_inspectable.IInspectable):
    Square30x30Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    Square70x70Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_Square150x150Logo: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                     _type.HRESULT]
    get_Square150x150Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                     _type.HRESULT]
    put_Wide310x150Logo: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                   _type.HRESULT]
    get_Wide310x150Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]
    put_Square310x310Logo: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                     _type.HRESULT]
    get_Square310x310Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                     _type.HRESULT]
    put_ForegroundText: _Callable[[_enum.Windows.UI.StartScreen.ForegroundText],  # value
                                  _type.HRESULT]
    get_ForegroundText: _Callable[[_Pointer[_enum.Windows.UI.StartScreen.ForegroundText]],  # value
                                  _type.HRESULT]
    put_BackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_ShowNameOnSquare150x150Logo: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_ShowNameOnSquare150x150Logo: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_ShowNameOnWide310x150Logo: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_ShowNameOnWide310x150Logo: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_ShowNameOnSquare310x310Logo: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_ShowNameOnSquare310x310Logo: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class ISecondaryTileVisualElements2(_inspectable.IInspectable):
    put_Square71x71Logo: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                   _type.HRESULT]
    get_Square71x71Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]


class ISecondaryTileVisualElements3(_inspectable.IInspectable):
    put_Square44x44Logo: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                   _type.HRESULT]
    get_Square44x44Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]


class ISecondaryTileVisualElements4(_inspectable.IInspectable):
    get_MixedRealityModel: _Callable[[_Pointer[ITileMixedRealityModel]],  # value
                                     _type.HRESULT]


class IStartScreenManager(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    SupportsAppListEntry: _Callable[[_Windows_ApplicationModel_Core.IAppListEntry,  # appListEntry
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    ContainsAppListEntryAsync: _Callable[[_Windows_ApplicationModel_Core.IAppListEntry,  # appListEntry
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    RequestAddAppListEntryAsync: _Callable[[_Windows_ApplicationModel_Core.IAppListEntry,  # appListEntry
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]


class IStartScreenManager2(_inspectable.IInspectable):
    ContainsSecondaryTileAsync: _Callable[[_type.HSTRING,  # tileId
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    TryRemoveSecondaryTileAsync: _Callable[[_type.HSTRING,  # tileId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]


class IStartScreenManagerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IStartScreenManager]],  # value
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IStartScreenManager]],  # result
                          _type.HRESULT]

    _factory = True


class ITileMixedRealityModel(_inspectable.IInspectable):
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_BoundingBox: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Perception.Spatial.SpatialBoundingBox]],  # value
                               _type.HRESULT]
    get_BoundingBox: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Perception.Spatial.SpatialBoundingBox]]],  # value
                               _type.HRESULT]


class ITileMixedRealityModel2(_inspectable.IInspectable):
    put_ActivationBehavior: _Callable[[_enum.Windows.UI.StartScreen.TileMixedRealityModelActivationBehavior],  # value
                                      _type.HRESULT]
    get_ActivationBehavior: _Callable[[_Pointer[_enum.Windows.UI.StartScreen.TileMixedRealityModelActivationBehavior]],  # value
                                      _type.HRESULT]


class IVisualElementsRequest(_inspectable.IInspectable):
    get_VisualElements: _Callable[[_Pointer[ISecondaryTileVisualElements]],  # value
                                  _type.HRESULT]
    get_AlternateVisualElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ISecondaryTileVisualElements]]],  # value
                                           _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IVisualElementsRequestDeferral]],  # deferral
                           _type.HRESULT]


class IVisualElementsRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IVisualElementsRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IVisualElementsRequest]],  # value
                           _type.HRESULT]
