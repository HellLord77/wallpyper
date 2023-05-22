from __future__ import annotations

from typing import Callable as _Callable

from .... import Xaml as _Windows_UI_Xaml
from ..... import Foundation as _Windows_Foundation
from .....Devices import Geolocation as _Windows_Devices_Geolocation
from .....Foundation import Collections as _Windows_Foundation_Collections
from .....Services import Maps as _Windows_Services_Maps
from .....Services.Maps import LocalSearch as _Windows_Services_Maps_LocalSearch
from .....Storage import Streams as _Windows_Storage_Streams
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class ICustomMapTileDataSource(_inspectable.IInspectable):
    add_BitmapRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICustomMapTileDataSource, IMapTileBitmapRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_BitmapRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class ICustomMapTileDataSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ICustomMapTileDataSource]],  # value
                              _type.HRESULT]


class IHttpMapTileDataSource(_inspectable.IInspectable):
    get_UriFormatString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_UriFormatString: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_AdditionalRequestHeaders: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                                            _type.HRESULT]
    get_AllowCaching: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_AllowCaching: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    add_UriRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IHttpMapTileDataSource, IMapTileUriRequestedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_UriRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IHttpMapTileDataSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IHttpMapTileDataSource]],  # value
                              _type.HRESULT]
    CreateInstanceWithUriFormatString: _Callable[[_type.HSTRING,  # uriFormatString
                                                  _inspectable.IInspectable,  # baseInterface
                                                  _Pointer[_inspectable.IInspectable],  # innerInterface
                                                  _Pointer[IHttpMapTileDataSource]],  # value
                                                 _type.HRESULT]


class ILocalMapTileDataSource(_inspectable.IInspectable):
    get_UriFormatString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_UriFormatString: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    add_UriRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ILocalMapTileDataSource, IMapTileUriRequestedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_UriRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class ILocalMapTileDataSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ILocalMapTileDataSource]],  # value
                              _type.HRESULT]
    CreateInstanceWithUriFormatString: _Callable[[_type.HSTRING,  # uriFormatString
                                                  _inspectable.IInspectable,  # baseInterface
                                                  _Pointer[_inspectable.IInspectable],  # innerInterface
                                                  _Pointer[ILocalMapTileDataSource]],  # value
                                                 _type.HRESULT]


class IMapActualCameraChangedEventArgs(_inspectable.IInspectable):
    get_Camera: _Callable[[_Pointer[IMapCamera]],  # value
                          _type.HRESULT]


class IMapActualCameraChangedEventArgs2(_inspectable.IInspectable):
    get_ChangeReason: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason]],  # value
                                _type.HRESULT]


class IMapActualCameraChangingEventArgs(_inspectable.IInspectable):
    get_Camera: _Callable[[_Pointer[IMapCamera]],  # value
                          _type.HRESULT]


class IMapActualCameraChangingEventArgs2(_inspectable.IInspectable):
    get_ChangeReason: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason]],  # value
                                _type.HRESULT]


class IMapBillboard(_inspectable.IInspectable):
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    put_Location: _Callable[[_Windows_Devices_Geolocation.IGeopoint],  # value
                            _type.HRESULT]
    get_NormalizedAnchorPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                         _type.HRESULT]
    put_NormalizedAnchorPoint: _Callable[[_struct.Windows.Foundation.Point],  # value
                                         _type.HRESULT]
    get_Image: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                         _type.HRESULT]
    put_Image: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                         _type.HRESULT]
    get_CollisionBehaviorDesired: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior]],  # value
                                            _type.HRESULT]
    put_CollisionBehaviorDesired: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior],  # value
                                            _type.HRESULT]
    get_ReferenceCamera: _Callable[[_Pointer[IMapCamera]],  # value
                                   _type.HRESULT]


class IMapBillboardFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceFromCamera: _Callable[[IMapCamera,  # camera
                                         _Pointer[IMapBillboard]],  # value
                                        _type.HRESULT]


class IMapBillboardStatics(_inspectable.IInspectable, factory=True):
    get_LocationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_NormalizedAnchorPointProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_CollisionBehaviorDesiredProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]


class IMapCamera(_inspectable.IInspectable):
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    put_Location: _Callable[[_Windows_Devices_Geolocation.IGeopoint],  # value
                            _type.HRESULT]
    get_Heading: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Heading: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Pitch: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Pitch: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_Roll: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    put_Roll: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]
    get_FieldOfView: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_FieldOfView: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]


class IMapCameraFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithLocation: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                           _Pointer[IMapCamera]],  # value
                                          _type.HRESULT]
    CreateInstanceWithLocationAndHeading: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                                     _type.DOUBLE,  # headingInDegrees
                                                     _Pointer[IMapCamera]],  # value
                                                    _type.HRESULT]
    CreateInstanceWithLocationHeadingAndPitch: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                                          _type.DOUBLE,  # headingInDegrees
                                                          _type.DOUBLE,  # pitchInDegrees
                                                          _Pointer[IMapCamera]],  # value
                                                         _type.HRESULT]
    CreateInstanceWithLocationHeadingPitchRollAndFieldOfView: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                                                         _type.DOUBLE,  # headingInDegrees
                                                                         _type.DOUBLE,  # pitchInDegrees
                                                                         _type.DOUBLE,  # rollInDegrees
                                                                         _type.DOUBLE,  # fieldOfViewInDegrees
                                                                         _Pointer[IMapCamera]],  # value
                                                                        _type.HRESULT]


class IMapContextRequestedEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMapElement]]],  # value
                               _type.HRESULT]


class IMapControl(_inspectable.IInspectable):
    get_Center: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                          _type.HRESULT]
    put_Center: _Callable[[_Windows_Devices_Geolocation.IGeopoint],  # value
                          _type.HRESULT]
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IDependencyObject]]],  # value
                            _type.HRESULT]
    get_ColorScheme: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapColorScheme]],  # value
                               _type.HRESULT]
    put_ColorScheme: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapColorScheme],  # value
                               _type.HRESULT]
    get_DesiredPitch: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_DesiredPitch: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_Heading: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Heading: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_LandmarksVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_LandmarksVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_LoadingStatus: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapLoadingStatus]],  # value
                                 _type.HRESULT]
    get_MapServiceToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_MapServiceToken: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_MaxZoomLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_MinZoomLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_PedestrianFeaturesVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_PedestrianFeaturesVisible: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_Pitch: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    get_Style: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapStyle]],  # value
                         _type.HRESULT]
    put_Style: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapStyle],  # value
                         _type.HRESULT]
    get_TrafficFlowVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_TrafficFlowVisible: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_TransformOrigin: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                   _type.HRESULT]
    put_TransformOrigin: _Callable[[_struct.Windows.Foundation.Point],  # value
                                   _type.HRESULT]
    get_WatermarkMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapWatermarkMode]],  # value
                                 _type.HRESULT]
    put_WatermarkMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapWatermarkMode],  # value
                                 _type.HRESULT]
    get_ZoomLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_ZoomLevel: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_MapElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMapElement]]],  # value
                               _type.HRESULT]
    get_Routes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMapRouteView]]],  # value
                          _type.HRESULT]
    get_TileSources: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMapTileSource]]],  # value
                               _type.HRESULT]
    add_CenterChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_CenterChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_HeadingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_HeadingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_LoadingStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_LoadingStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_MapDoubleTapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapInputEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_MapDoubleTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_MapHolding: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapInputEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_MapHolding: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_MapTapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapInputEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_MapTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_PitchChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PitchChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_TransformOriginChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_TransformOriginChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_ZoomLevelChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ZoomLevelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    FindMapElementsAtOffset: _Callable[[_struct.Windows.Foundation.Point,  # offset
                                        _Pointer[_Windows_Foundation_Collections.IVectorView[IMapElement]]],  # result
                                       _type.HRESULT]
    GetLocationFromOffset: _Callable[[_struct.Windows.Foundation.Point,  # offset
                                      _Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # location
                                     _type.HRESULT]
    GetOffsetFromLocation: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                      _Pointer[_struct.Windows.Foundation.Point]],  # offset
                                     _type.HRESULT]
    IsLocationInView: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                 _Pointer[_type.boolean]],  # isInView
                                _type.HRESULT]
    TrySetViewBoundsAsync: _Callable[[_Windows_Devices_Geolocation.IGeoboundingBox,  # bounds
                                      _Windows_Foundation.IReference[_struct.Windows.UI.Xaml.Thickness],  # margin
                                      _enum.Windows.UI.Xaml.Controls.Maps.MapAnimationKind,  # animation
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    TrySetViewWithCenterAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # center
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    TrySetViewWithCenterAndZoomAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # center
                                                 _Windows_Foundation.IReference[_type.DOUBLE],  # zoomLevel
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                _type.HRESULT]
    TrySetViewWithCenterZoomHeadingAndPitchAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # center
                                                             _Windows_Foundation.IReference[_type.DOUBLE],  # zoomLevel
                                                             _Windows_Foundation.IReference[_type.DOUBLE],  # heading
                                                             _Windows_Foundation.IReference[_type.DOUBLE],  # desiredPitch
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                            _type.HRESULT]
    TrySetViewWithCenterZoomHeadingPitchAndAnimationAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # center
                                                                      _Windows_Foundation.IReference[_type.DOUBLE],  # zoomLevel
                                                                      _Windows_Foundation.IReference[_type.DOUBLE],  # heading
                                                                      _Windows_Foundation.IReference[_type.DOUBLE],  # desiredPitch
                                                                      _enum.Windows.UI.Xaml.Controls.Maps.MapAnimationKind,  # animation
                                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                                     _type.HRESULT]


class IMapControl2(_inspectable.IInspectable):
    get_BusinessLandmarksVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_BusinessLandmarksVisible: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_TransitFeaturesVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_TransitFeaturesVisible: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_PanInteractionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode]],  # value
                                      _type.HRESULT]
    put_PanInteractionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapPanInteractionMode],  # value
                                      _type.HRESULT]
    get_RotateInteractionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapInteractionMode]],  # value
                                         _type.HRESULT]
    put_RotateInteractionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapInteractionMode],  # value
                                         _type.HRESULT]
    get_TiltInteractionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapInteractionMode]],  # value
                                       _type.HRESULT]
    put_TiltInteractionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapInteractionMode],  # value
                                       _type.HRESULT]
    get_ZoomInteractionMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapInteractionMode]],  # value
                                       _type.HRESULT]
    put_ZoomInteractionMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapInteractionMode],  # value
                                       _type.HRESULT]
    get_Is3DSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsStreetsideSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_Scene: _Callable[[_Pointer[IMapScene]],  # value
                         _type.HRESULT]
    put_Scene: _Callable[[IMapScene],  # value
                         _type.HRESULT]
    get_ActualCamera: _Callable[[_Pointer[IMapCamera]],  # value
                                _type.HRESULT]
    get_TargetCamera: _Callable[[_Pointer[IMapCamera]],  # value
                                _type.HRESULT]
    get_CustomExperience: _Callable[[_Pointer[IMapCustomExperience]],  # value
                                    _type.HRESULT]
    put_CustomExperience: _Callable[[IMapCustomExperience],  # value
                                    _type.HRESULT]
    add_MapElementClick: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapElementClickEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_MapElementClick: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_MapElementPointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapElementPointerEnteredEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_MapElementPointerEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_MapElementPointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapElementPointerExitedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_MapElementPointerExited: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_ActualCameraChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapActualCameraChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ActualCameraChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ActualCameraChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapActualCameraChangingEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ActualCameraChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_TargetCameraChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapTargetCameraChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_TargetCameraChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_CustomExperienceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapCustomExperienceChangedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_CustomExperienceChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    StartContinuousRotate: _Callable[[_type.DOUBLE],  # rateInDegreesPerSecond
                                     _type.HRESULT]
    StopContinuousRotate: _Callable[[],
                                    _type.HRESULT]
    StartContinuousTilt: _Callable[[_type.DOUBLE],  # rateInDegreesPerSecond
                                   _type.HRESULT]
    StopContinuousTilt: _Callable[[],
                                  _type.HRESULT]
    StartContinuousZoom: _Callable[[_type.DOUBLE],  # rateOfChangePerSecond
                                   _type.HRESULT]
    StopContinuousZoom: _Callable[[],
                                  _type.HRESULT]
    TryRotateAsync: _Callable[[_type.DOUBLE,  # degrees
                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    TryRotateToAsync: _Callable[[_type.DOUBLE,  # angleInDegrees
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                _type.HRESULT]
    TryTiltAsync: _Callable[[_type.DOUBLE,  # degrees
                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                            _type.HRESULT]
    TryTiltToAsync: _Callable[[_type.DOUBLE,  # angleInDegrees
                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    TryZoomInAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    TryZoomOutAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                               _type.HRESULT]
    TryZoomToAsync: _Callable[[_type.DOUBLE,  # zoomLevel
                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    TrySetSceneAsync: _Callable[[IMapScene,  # scene
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                _type.HRESULT]
    TrySetSceneWithAnimationAsync: _Callable[[IMapScene,  # scene
                                              _enum.Windows.UI.Xaml.Controls.Maps.MapAnimationKind,  # animationKind
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                             _type.HRESULT]


class IMapControl3(_inspectable.IInspectable):
    add_MapRightTapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapRightTappedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_MapRightTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IMapControl4(_inspectable.IInspectable):
    get_BusinessLandmarksEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_BusinessLandmarksEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_TransitFeaturesEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_TransitFeaturesEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    GetVisibleRegion: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapVisibleRegionKind,  # region
                                 _Pointer[_Windows_Devices_Geolocation.IGeopath]],  # result
                                _type.HRESULT]


class IMapControl5(_inspectable.IInspectable):
    get_MapProjection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapProjection]],  # value
                                 _type.HRESULT]
    put_MapProjection: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapProjection],  # value
                                 _type.HRESULT]
    get_StyleSheet: _Callable[[_Pointer[IMapStyleSheet]],  # value
                              _type.HRESULT]
    put_StyleSheet: _Callable[[IMapStyleSheet],  # value
                              _type.HRESULT]
    get_ViewPadding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],  # value
                               _type.HRESULT]
    put_ViewPadding: _Callable[[_struct.Windows.UI.Xaml.Thickness],  # value
                               _type.HRESULT]
    add_MapContextRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapContextRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_MapContextRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    FindMapElementsAtOffsetWithRadius: _Callable[[_struct.Windows.Foundation.Point,  # offset
                                                  _type.DOUBLE,  # radius
                                                  _Pointer[_Windows_Foundation_Collections.IVectorView[IMapElement]]],  # result
                                                 _type.HRESULT]
    GetLocationFromOffsetWithReferenceSystem: _Callable[[_struct.Windows.Foundation.Point,  # offset
                                                         _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # desiredReferenceSystem
                                                         _Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # location
                                                        _type.HRESULT]
    StartContinuousPan: _Callable[[_type.DOUBLE,  # horizontalPixelsPerSecond
                                   _type.DOUBLE],  # verticalPixelsPerSecond
                                  _type.HRESULT]
    StopContinuousPan: _Callable[[],
                                 _type.HRESULT]
    TryPanAsync: _Callable[[_type.DOUBLE,  # horizontalPixels
                            _type.DOUBLE,  # verticalPixels
                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                           _type.HRESULT]
    TryPanToAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                             _type.HRESULT]


class IMapControl6(_inspectable.IInspectable):
    get_Layers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMapLayer]]],  # value
                          _type.HRESULT]
    put_Layers: _Callable[[_Windows_Foundation_Collections.IVector[IMapLayer]],  # value
                          _type.HRESULT]
    TryGetLocationFromOffset: _Callable[[_struct.Windows.Foundation.Point,  # offset
                                         _Pointer[_Windows_Devices_Geolocation.IGeopoint],  # location
                                         _Pointer[_type.boolean]],  # returnValue
                                        _type.HRESULT]
    TryGetLocationFromOffsetWithReferenceSystem: _Callable[[_struct.Windows.Foundation.Point,  # offset
                                                            _enum.Windows.Devices.Geolocation.AltitudeReferenceSystem,  # desiredReferenceSystem
                                                            _Pointer[_Windows_Devices_Geolocation.IGeopoint],  # location
                                                            _Pointer[_type.boolean]],  # returnValue
                                                           _type.HRESULT]


class IMapControl7(_inspectable.IInspectable):
    get_Region: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Region: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]


class IMapControl8(_inspectable.IInspectable):
    get_CanTiltDown: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_CanTiltUp: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanZoomIn: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanZoomOut: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IMapControlBusinessLandmarkClickEventArgs(_inspectable.IInspectable):
    get_LocalLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Services_Maps_LocalSearch.ILocalLocation]]],  # value
                                  _type.HRESULT]


class IMapControlBusinessLandmarkPointerEnteredEventArgs(_inspectable.IInspectable):
    get_LocalLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Services_Maps_LocalSearch.ILocalLocation]]],  # value
                                  _type.HRESULT]


class IMapControlBusinessLandmarkPointerExitedEventArgs(_inspectable.IInspectable):
    get_LocalLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Services_Maps_LocalSearch.ILocalLocation]]],  # value
                                  _type.HRESULT]


class IMapControlBusinessLandmarkRightTappedEventArgs(_inspectable.IInspectable):
    get_LocalLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Services_Maps_LocalSearch.ILocalLocation]]],  # value
                                  _type.HRESULT]


class IMapControlDataHelper(_inspectable.IInspectable):
    add_BusinessLandmarkClick: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlBusinessLandmarkClickEventArgs],  # value
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_BusinessLandmarkClick: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_TransitFeatureClick: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlTransitFeatureClickEventArgs],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_TransitFeatureClick: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_BusinessLandmarkRightTapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlBusinessLandmarkRightTappedEventArgs],  # value
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_BusinessLandmarkRightTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_TransitFeatureRightTapped: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlTransitFeatureRightTappedEventArgs],  # value
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_TransitFeatureRightTapped: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]


class IMapControlDataHelper2(_inspectable.IInspectable):
    add_BusinessLandmarkPointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlBusinessLandmarkPointerEnteredEventArgs],  # value
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_BusinessLandmarkPointerEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_TransitFeaturePointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlTransitFeaturePointerEnteredEventArgs],  # value
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_TransitFeaturePointerEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    add_BusinessLandmarkPointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlBusinessLandmarkPointerExitedEventArgs],  # value
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_BusinessLandmarkPointerExited: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_TransitFeaturePointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapControl, IMapControlTransitFeaturePointerExitedEventArgs],  # value
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_TransitFeaturePointerExited: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IMapControlDataHelperFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[IMapControl,  # map
                               _Pointer[IMapControlDataHelper]],  # instance
                              _type.HRESULT]


class IMapControlDataHelperStatics(_inspectable.IInspectable, factory=True):
    CreateMapControl: _Callable[[_type.boolean,  # rasterRenderMode
                                 _Pointer[IMapControl]],  # returnValue
                                _type.HRESULT]


class IMapControlStatics(_inspectable.IInspectable, factory=True):
    get_CenterProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_ChildrenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_ColorSchemeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_DesiredPitchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_HeadingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_LandmarksVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_LoadingStatusProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_MapServiceTokenProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_PedestrianFeaturesVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                     _type.HRESULT]
    get_PitchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_StyleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_TrafficFlowVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_TransformOriginProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_WatermarkModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_ZoomLevelProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_MapElementsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_RoutesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_TileSourcesProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_LocationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetLocation: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # result
                           _type.HRESULT]
    SetLocation: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                            _Windows_Devices_Geolocation.IGeopoint],  # value
                           _type.HRESULT]
    get_NormalizedAnchorPointProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    GetNormalizedAnchorPoint: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _Pointer[_struct.Windows.Foundation.Point]],  # result
                                        _type.HRESULT]
    SetNormalizedAnchorPoint: _Callable[[_Windows_UI_Xaml.IDependencyObject,  # element
                                         _struct.Windows.Foundation.Point],  # value
                                        _type.HRESULT]


class IMapControlStatics2(_inspectable.IInspectable, factory=True):
    get_BusinessLandmarksVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_TransitFeaturesVisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_PanInteractionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_RotateInteractionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_TiltInteractionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_ZoomInteractionModeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_Is3DSupportedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IsStreetsideSupportedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_SceneProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]


class IMapControlStatics4(_inspectable.IInspectable, factory=True):
    get_BusinessLandmarksEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_TransitFeaturesEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]


class IMapControlStatics5(_inspectable.IInspectable, factory=True):
    get_MapProjectionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_StyleSheetProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_ViewPaddingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]


class IMapControlStatics6(_inspectable.IInspectable, factory=True):
    get_LayersProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IMapControlStatics7(_inspectable.IInspectable, factory=True):
    get_RegionProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IMapControlStatics8(_inspectable.IInspectable, factory=True):
    get_CanTiltDownProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CanTiltUpProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CanZoomInProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_CanZoomOutProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class IMapControlTransitFeatureClickEventArgs(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_TransitProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                                     _type.HRESULT]


class IMapControlTransitFeaturePointerEnteredEventArgs(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_TransitProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                                     _type.HRESULT]


class IMapControlTransitFeaturePointerExitedEventArgs(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_TransitProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                                     _type.HRESULT]


class IMapControlTransitFeatureRightTappedEventArgs(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_TransitProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                                     _type.HRESULT]


class IMapCustomExperience(_inspectable.IInspectable):
    pass


class IMapCustomExperienceChangedEventArgs(_inspectable.IInspectable):
    pass


class IMapCustomExperienceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMapCustomExperience]],  # value
                              _type.HRESULT]


class IMapElement(_inspectable.IInspectable):
    get_ZIndex: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_ZIndex: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Visible: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IMapElement2(_inspectable.IInspectable):
    get_MapTabIndex: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_MapTabIndex: _Callable[[_type.INT32],  # value
                               _type.HRESULT]


class IMapElement3(_inspectable.IInspectable):
    get_MapStyleSheetEntry: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_MapStyleSheetEntry: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_MapStyleSheetEntryState: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    put_MapStyleSheetEntryState: _Callable[[_type.HSTRING],  # value
                                           _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                       _type.HRESULT]
    put_Tag: _Callable[[_inspectable.IInspectable],  # value
                       _type.HRESULT]


class IMapElement3D(_inspectable.IInspectable):
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    put_Location: _Callable[[_Windows_Devices_Geolocation.IGeopoint],  # value
                            _type.HRESULT]
    get_Model: _Callable[[_Pointer[IMapModel3D]],  # value
                         _type.HRESULT]
    put_Model: _Callable[[IMapModel3D],  # value
                         _type.HRESULT]
    get_Heading: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Heading: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Pitch: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Pitch: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_Roll: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    put_Roll: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                         _type.HRESULT]


class IMapElement3DStatics(_inspectable.IInspectable, factory=True):
    get_LocationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_HeadingProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_PitchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_RollProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_ScaleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]


class IMapElement4(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class IMapElementClickEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMapElement]]],  # value
                               _type.HRESULT]


class IMapElementFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMapElement]],  # value
                              _type.HRESULT]


class IMapElementPointerEnteredEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElement: _Callable[[_Pointer[IMapElement]],  # value
                              _type.HRESULT]


class IMapElementPointerExitedEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElement: _Callable[[_Pointer[IMapElement]],  # value
                              _type.HRESULT]


class IMapElementStatics(_inspectable.IInspectable, factory=True):
    get_ZIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_VisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]


class IMapElementStatics2(_inspectable.IInspectable, factory=True):
    get_MapTabIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]


class IMapElementStatics3(_inspectable.IInspectable, factory=True):
    get_MapStyleSheetEntryProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_MapStyleSheetEntryStateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_TagProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                               _type.HRESULT]


class IMapElementStatics4(_inspectable.IInspectable, factory=True):
    get_IsEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]


class IMapElementsLayer(_inspectable.IInspectable):
    get_MapElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMapElement]]],  # value
                               _type.HRESULT]
    put_MapElements: _Callable[[_Windows_Foundation_Collections.IVector[IMapElement]],  # value
                               _type.HRESULT]
    add_MapElementClick: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapElementsLayer, IMapElementsLayerClickEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_MapElementClick: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_MapElementPointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapElementsLayer, IMapElementsLayerPointerEnteredEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_MapElementPointerEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_MapElementPointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapElementsLayer, IMapElementsLayerPointerExitedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_MapElementPointerExited: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_MapContextRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapElementsLayer, IMapElementsLayerContextRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_MapContextRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IMapElementsLayerClickEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMapElement]]],  # value
                               _type.HRESULT]


class IMapElementsLayerContextRequestedEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMapElement]]],  # value
                               _type.HRESULT]


class IMapElementsLayerPointerEnteredEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElement: _Callable[[_Pointer[IMapElement]],  # value
                              _type.HRESULT]


class IMapElementsLayerPointerExitedEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    get_MapElement: _Callable[[_Pointer[IMapElement]],  # value
                              _type.HRESULT]


class IMapElementsLayerStatics(_inspectable.IInspectable, factory=True):
    get_MapElementsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]


class IMapIcon(_inspectable.IInspectable):
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]
    put_Location: _Callable[[_Windows_Devices_Geolocation.IGeopoint],  # value
                            _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_NormalizedAnchorPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                         _type.HRESULT]
    put_NormalizedAnchorPoint: _Callable[[_struct.Windows.Foundation.Point],  # value
                                         _type.HRESULT]
    get_Image: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                         _type.HRESULT]
    put_Image: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                         _type.HRESULT]


class IMapIcon2(_inspectable.IInspectable):
    get_CollisionBehaviorDesired: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior]],  # value
                                            _type.HRESULT]
    put_CollisionBehaviorDesired: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapElementCollisionBehavior],  # value
                                            _type.HRESULT]


class IMapIconStatics(_inspectable.IInspectable, factory=True):
    get_LocationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_TitleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_NormalizedAnchorPointProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]


class IMapIconStatics2(_inspectable.IInspectable, factory=True):
    get_CollisionBehaviorDesiredProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]


class IMapInputEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]


class IMapItemsControl(_inspectable.IInspectable):
    get_ItemsSource: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                               _type.HRESULT]
    put_ItemsSource: _Callable[[_inspectable.IInspectable],  # value
                               _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Xaml.IDependencyObject]]],  # value
                         _type.HRESULT]
    get_ItemTemplate: _Callable[[_Pointer[_Windows_UI_Xaml.IDataTemplate]],  # value
                                _type.HRESULT]
    put_ItemTemplate: _Callable[[_Windows_UI_Xaml.IDataTemplate],  # value
                                _type.HRESULT]


class IMapItemsControlStatics(_inspectable.IInspectable, factory=True):
    get_ItemsSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ItemsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_ItemTemplateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]


class IMapLayer(_inspectable.IInspectable):
    get_MapTabIndex: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_MapTabIndex: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Visible: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_ZIndex: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_ZIndex: _Callable[[_type.INT32],  # value
                          _type.HRESULT]


class IMapLayerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMapLayer]],  # value
                              _type.HRESULT]


class IMapLayerStatics(_inspectable.IInspectable, factory=True):
    get_MapTabIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_VisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_ZIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IMapModel3D(_inspectable.IInspectable):
    pass


class IMapModel3DFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMapModel3D]],  # value
                              _type.HRESULT]


class IMapModel3DStatics(_inspectable.IInspectable, factory=True):
    CreateFrom3MFAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # source
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IMapModel3D]]],  # operation
                                  _type.HRESULT]
    CreateFrom3MFWithShadingOptionAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # source
                                                    _enum.Windows.UI.Xaml.Controls.Maps.MapModel3DShadingOption,  # shadingOption
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IMapModel3D]]],  # operation
                                                   _type.HRESULT]


class IMapPolygon(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopath]],  # value
                        _type.HRESULT]
    put_Path: _Callable[[_Windows_Devices_Geolocation.IGeopath],  # value
                        _type.HRESULT]
    get_StrokeColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    put_StrokeColor: _Callable[[_struct.Windows.UI.Color],  # value
                               _type.HRESULT]
    get_StrokeThickness: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_StrokeThickness: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_StrokeDashed: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_StrokeDashed: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_FillColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    put_FillColor: _Callable[[_struct.Windows.UI.Color],  # value
                             _type.HRESULT]


class IMapPolygon2(_inspectable.IInspectable):
    get_Paths: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Devices_Geolocation.IGeopath]]],  # value
                         _type.HRESULT]


class IMapPolygonStatics(_inspectable.IInspectable, factory=True):
    get_PathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_StrokeThicknessProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_StrokeDashedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]


class IMapPolyline(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopath]],  # value
                        _type.HRESULT]
    put_Path: _Callable[[_Windows_Devices_Geolocation.IGeopath],  # value
                        _type.HRESULT]
    get_StrokeColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    put_StrokeColor: _Callable[[_struct.Windows.UI.Color],  # value
                               _type.HRESULT]
    get_StrokeThickness: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_StrokeThickness: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_StrokeDashed: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_StrokeDashed: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IMapPolylineStatics(_inspectable.IInspectable, factory=True):
    get_PathProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_StrokeDashedProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]


class IMapRightTappedEventArgs(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]


class IMapRouteView(_inspectable.IInspectable):
    get_RouteColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    put_RouteColor: _Callable[[_struct.Windows.UI.Color],  # value
                              _type.HRESULT]
    get_OutlineColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    put_OutlineColor: _Callable[[_struct.Windows.UI.Color],  # value
                                _type.HRESULT]
    get_Route: _Callable[[_Pointer[_Windows_Services_Maps.IMapRoute]],  # value
                         _type.HRESULT]


class IMapRouteViewFactory(_inspectable.IInspectable):
    CreateInstanceWithMapRoute: _Callable[[_Windows_Services_Maps.IMapRoute,  # route
                                           _inspectable.IInspectable,  # baseInterface
                                           _Pointer[_inspectable.IInspectable],  # innerInterface
                                           _Pointer[IMapRouteView]],  # value
                                          _type.HRESULT]


class IMapScene(_inspectable.IInspectable):
    get_TargetCamera: _Callable[[_Pointer[IMapCamera]],  # value
                                _type.HRESULT]
    add_TargetCameraChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMapScene, IMapTargetCameraChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_TargetCameraChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IMapSceneStatics(_inspectable.IInspectable, factory=True):
    CreateFromBoundingBox: _Callable[[_Windows_Devices_Geolocation.IGeoboundingBox,  # bounds
                                      _Pointer[IMapScene]],  # result
                                     _type.HRESULT]
    CreateFromBoundingBoxWithHeadingAndPitch: _Callable[[_Windows_Devices_Geolocation.IGeoboundingBox,  # bounds
                                                         _type.DOUBLE,  # headingInDegrees
                                                         _type.DOUBLE,  # pitchInDegrees
                                                         _Pointer[IMapScene]],  # result
                                                        _type.HRESULT]
    CreateFromCamera: _Callable[[IMapCamera,  # camera
                                 _Pointer[IMapScene]],  # result
                                _type.HRESULT]
    CreateFromLocation: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                   _Pointer[IMapScene]],  # result
                                  _type.HRESULT]
    CreateFromLocationWithHeadingAndPitch: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                                      _type.DOUBLE,  # headingInDegrees
                                                      _type.DOUBLE,  # pitchInDegrees
                                                      _Pointer[IMapScene]],  # result
                                                     _type.HRESULT]
    CreateFromLocationAndRadius: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                            _type.DOUBLE,  # radiusInMeters
                                            _Pointer[IMapScene]],  # result
                                           _type.HRESULT]
    CreateFromLocationAndRadiusWithHeadingAndPitch: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                                               _type.DOUBLE,  # radiusInMeters
                                                               _type.DOUBLE,  # headingInDegrees
                                                               _type.DOUBLE,  # pitchInDegrees
                                                               _Pointer[IMapScene]],  # result
                                                              _type.HRESULT]
    CreateFromLocations: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Devices_Geolocation.IGeopoint],  # locations
                                    _Pointer[IMapScene]],  # result
                                   _type.HRESULT]
    CreateFromLocationsWithHeadingAndPitch: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Devices_Geolocation.IGeopoint],  # locations
                                                       _type.DOUBLE,  # headingInDegrees
                                                       _type.DOUBLE,  # pitchInDegrees
                                                       _Pointer[IMapScene]],  # result
                                                      _type.HRESULT]


class IMapStyleSheet(_inspectable.IInspectable):
    pass


class IMapStyleSheetEntriesStatics(_inspectable.IInspectable, factory=True):
    get_Area: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Airport: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Cemetery: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Continent: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Education: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_IndigenousPeoplesReserve: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    get_Island: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Medical: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Military: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Nautical: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Neighborhood: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Runway: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Sand: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_ShoppingCenter: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Stadium: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Vegetation: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Forest: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_GolfCourse: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Park: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_PlayingField: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Reserve: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Point: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_NaturalPoint: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Peak: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_VolcanicPeak: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_WaterPoint: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_PointOfInterest: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Business: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_FoodPoint: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_PopulatedPlace: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Capital: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_AdminDistrictCapital: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_CountryRegionCapital: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_RoadShield: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_RoadExit: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Transit: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Political: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_CountryRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_AdminDistrict: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_District: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Structure: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Building: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_EducationBuilding: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_MedicalBuilding: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_TransitBuilding: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Transportation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Road: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_ControlledAccessHighway: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    get_HighSpeedRamp: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Highway: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_MajorRoad: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ArterialRoad: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Street: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Ramp: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_UnpavedStreet: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_TollRoad: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Railway: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Trail: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_WaterRoute: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Water: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_River: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_RouteLine: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_WalkingRoute: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_DrivingRoute: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IMapStyleSheetEntryStatesStatics(_inspectable.IInspectable, factory=True):
    get_Disabled: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Hover: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Selected: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IMapStyleSheetStatics(_inspectable.IInspectable, factory=True):
    Aerial: _Callable[[_Pointer[IMapStyleSheet]],  # result
                      _type.HRESULT]
    AerialWithOverlay: _Callable[[_Pointer[IMapStyleSheet]],  # result
                                 _type.HRESULT]
    RoadLight: _Callable[[_Pointer[IMapStyleSheet]],  # result
                         _type.HRESULT]
    RoadDark: _Callable[[_Pointer[IMapStyleSheet]],  # result
                        _type.HRESULT]
    RoadHighContrastLight: _Callable[[_Pointer[IMapStyleSheet]],  # result
                                     _type.HRESULT]
    RoadHighContrastDark: _Callable[[_Pointer[IMapStyleSheet]],  # result
                                    _type.HRESULT]
    Combine: _Callable[[_Windows_Foundation_Collections.IIterable[IMapStyleSheet],  # styleSheets
                        _Pointer[IMapStyleSheet]],  # result
                       _type.HRESULT]
    ParseFromJson: _Callable[[_type.HSTRING,  # styleAsJson
                              _Pointer[IMapStyleSheet]],  # result
                             _type.HRESULT]
    TryParseFromJson: _Callable[[_type.HSTRING,  # styleAsJson
                                 _Pointer[IMapStyleSheet],  # styleSheet
                                 _Pointer[_type.boolean]],  # returnValue
                                _type.HRESULT]


class IMapTargetCameraChangedEventArgs(_inspectable.IInspectable):
    get_Camera: _Callable[[_Pointer[IMapCamera]],  # value
                          _type.HRESULT]


class IMapTargetCameraChangedEventArgs2(_inspectable.IInspectable):
    get_ChangeReason: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapCameraChangeReason]],  # value
                                _type.HRESULT]


class IMapTileBitmapRequest(_inspectable.IInspectable):
    get_PixelData: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    put_PixelData: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IMapTileBitmapRequestDeferral]],  # result
                           _type.HRESULT]


class IMapTileBitmapRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IMapTileBitmapRequestedEventArgs(_inspectable.IInspectable):
    get_X: _Callable[[_Pointer[_type.INT32]],  # value
                     _type.HRESULT]
    get_Y: _Callable[[_Pointer[_type.INT32]],  # value
                     _type.HRESULT]
    get_ZoomLevel: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Request: _Callable[[_Pointer[IMapTileBitmapRequest]],  # value
                           _type.HRESULT]


class IMapTileBitmapRequestedEventArgs2(_inspectable.IInspectable):
    get_FrameIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]


class IMapTileDataSource(_inspectable.IInspectable):
    pass


class IMapTileDataSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMapTileDataSource]],  # value
                              _type.HRESULT]


class IMapTileSource(_inspectable.IInspectable):
    get_DataSource: _Callable[[_Pointer[IMapTileDataSource]],  # value
                              _type.HRESULT]
    put_DataSource: _Callable[[IMapTileDataSource],  # value
                              _type.HRESULT]
    get_Layer: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapTileLayer]],  # value
                         _type.HRESULT]
    put_Layer: _Callable[[_enum.Windows.UI.Xaml.Controls.Maps.MapTileLayer],  # value
                         _type.HRESULT]
    get_ZoomLevelRange: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange]],  # value
                                  _type.HRESULT]
    put_ZoomLevelRange: _Callable[[_struct.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange],  # value
                                  _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeoboundingBox]],  # value
                          _type.HRESULT]
    put_Bounds: _Callable[[_Windows_Devices_Geolocation.IGeoboundingBox],  # value
                          _type.HRESULT]
    get_AllowOverstretch: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_AllowOverstretch: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsFadingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsFadingEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsTransparencyEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsTransparencyEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsRetryEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsRetryEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_ZIndex: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_ZIndex: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_TilePixelSize: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_TilePixelSize: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_Visible: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Visible: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IMapTileSource2(_inspectable.IInspectable):
    get_AnimationState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Maps.MapTileAnimationState]],  # value
                                  _type.HRESULT]
    get_AutoPlay: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_AutoPlay: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_FrameCount: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_FrameCount: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_FrameDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]
    put_FrameDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                 _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Play: _Callable[[],
                    _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IMapTileSourceFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IMapTileSource]],  # value
                              _type.HRESULT]
    CreateInstanceWithDataSource: _Callable[[IMapTileDataSource,  # dataSource
                                             _inspectable.IInspectable,  # baseInterface
                                             _Pointer[_inspectable.IInspectable],  # innerInterface
                                             _Pointer[IMapTileSource]],  # value
                                            _type.HRESULT]
    CreateInstanceWithDataSourceAndZoomRange: _Callable[[IMapTileDataSource,  # dataSource
                                                         _struct.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange,  # zoomLevelRange
                                                         _inspectable.IInspectable,  # baseInterface
                                                         _Pointer[_inspectable.IInspectable],  # innerInterface
                                                         _Pointer[IMapTileSource]],  # value
                                                        _type.HRESULT]
    CreateInstanceWithDataSourceZoomRangeAndBounds: _Callable[[IMapTileDataSource,  # dataSource
                                                               _struct.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange,  # zoomLevelRange
                                                               _Windows_Devices_Geolocation.IGeoboundingBox,  # bounds
                                                               _inspectable.IInspectable,  # baseInterface
                                                               _Pointer[_inspectable.IInspectable],  # innerInterface
                                                               _Pointer[IMapTileSource]],  # value
                                                              _type.HRESULT]
    CreateInstanceWithDataSourceZoomRangeBoundsAndTileSize: _Callable[[IMapTileDataSource,  # dataSource
                                                                       _struct.Windows.UI.Xaml.Controls.Maps.MapZoomLevelRange,  # zoomLevelRange
                                                                       _Windows_Devices_Geolocation.IGeoboundingBox,  # bounds
                                                                       _type.INT32,  # tileSizeInPixels
                                                                       _inspectable.IInspectable,  # baseInterface
                                                                       _Pointer[_inspectable.IInspectable],  # innerInterface
                                                                       _Pointer[IMapTileSource]],  # value
                                                                      _type.HRESULT]


class IMapTileSourceStatics(_inspectable.IInspectable, factory=True):
    get_DataSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_LayerProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                 _type.HRESULT]
    get_ZoomLevelRangeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_BoundsProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_AllowOverstretchProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_IsFadingEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_IsTransparencyEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]
    get_IsRetryEnabledProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_ZIndexProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]
    get_TilePixelSizeProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_VisibleProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]


class IMapTileSourceStatics2(_inspectable.IInspectable, factory=True):
    get_AnimationStateProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_AutoPlayProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FrameCountProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FrameDurationProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]


class IMapTileUriRequest(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IMapTileUriRequestDeferral]],  # result
                           _type.HRESULT]


class IMapTileUriRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IMapTileUriRequestedEventArgs(_inspectable.IInspectable):
    get_X: _Callable[[_Pointer[_type.INT32]],  # value
                     _type.HRESULT]
    get_Y: _Callable[[_Pointer[_type.INT32]],  # value
                     _type.HRESULT]
    get_ZoomLevel: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Request: _Callable[[_Pointer[IMapTileUriRequest]],  # value
                           _type.HRESULT]


class IMapTileUriRequestedEventArgs2(_inspectable.IInspectable):
    get_FrameIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]


class IStreetsideExperience(_inspectable.IInspectable):
    get_AddressTextVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_AddressTextVisible: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_CursorVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_CursorVisible: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_OverviewMapVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_OverviewMapVisible: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_StreetLabelsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_StreetLabelsVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_ExitButtonVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_ExitButtonVisible: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_ZoomButtonsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_ZoomButtonsVisible: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class IStreetsideExperienceFactory(_inspectable.IInspectable, factory=True):
    CreateInstanceWithPanorama: _Callable[[IStreetsidePanorama,  # panorama
                                           _Pointer[IStreetsideExperience]],  # value
                                          _type.HRESULT]
    CreateInstanceWithPanoramaHeadingPitchAndFieldOfView: _Callable[[IStreetsidePanorama,  # panorama
                                                                     _type.DOUBLE,  # headingInDegrees
                                                                     _type.DOUBLE,  # pitchInDegrees
                                                                     _type.DOUBLE,  # fieldOfViewInDegrees
                                                                     _Pointer[IStreetsideExperience]],  # value
                                                                    _type.HRESULT]


class IStreetsidePanorama(_inspectable.IInspectable):
    get_Location: _Callable[[_Pointer[_Windows_Devices_Geolocation.IGeopoint]],  # value
                            _type.HRESULT]


class IStreetsidePanoramaStatics(_inspectable.IInspectable, factory=True):
    FindNearbyWithLocationAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IStreetsidePanorama]]],  # operation
                                           _type.HRESULT]
    FindNearbyWithLocationAndRadiusAsync: _Callable[[_Windows_Devices_Geolocation.IGeopoint,  # location
                                                     _type.DOUBLE,  # radiusInMeters
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IStreetsidePanorama]]],  # operation
                                                    _type.HRESULT]
