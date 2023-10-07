from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Perception as _Windows_Perception
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from ...System import RemoteSystems as _Windows_System_RemoteSystems
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ISpatialAnchor(_inspectable.IInspectable):
    get_CoordinateSystem: _Callable[[_Pointer[ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]
    get_RawCoordinateSystem: _Callable[[_Pointer[ISpatialCoordinateSystem]],  # value
                                       _type.HRESULT]
    add_RawCoordinateSystemAdjusted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialAnchor, ISpatialAnchorRawCoordinateSystemAdjustedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                                               _type.HRESULT]
    remove_RawCoordinateSystemAdjusted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                  _type.HRESULT]


class ISpatialAnchor2(_inspectable.IInspectable):
    get_RemovedByUser: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class ISpatialAnchorExportSufficiency(_inspectable.IInspectable):
    get_IsMinimallySufficient: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_SufficiencyLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_RecommendedSufficiencyLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                               _type.HRESULT]


class ISpatialAnchorExporter(_inspectable.IInspectable):
    GetAnchorExportSufficiencyAsync: _Callable[[ISpatialAnchor,  # anchor
                                                _enum.Windows.Perception.Spatial.SpatialAnchorExportPurpose,  # purpose
                                                _Pointer[_Windows_Foundation.IAsyncOperation[ISpatialAnchorExportSufficiency]]],  # operation
                                               _type.HRESULT]
    TryExportAnchorAsync: _Callable[[ISpatialAnchor,  # anchor
                                     _enum.Windows.Perception.Spatial.SpatialAnchorExportPurpose,  # purpose
                                     _Windows_Storage_Streams.IOutputStream,  # stream
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                    _type.HRESULT]


class ISpatialAnchorExporterStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[ISpatialAnchorExporter]],  # value
                          _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]]],  # result
                                  _type.HRESULT]


class ISpatialAnchorManagerStatics(_inspectable.IInspectable, factory=True):
    RequestStoreAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISpatialAnchorStore]]],  # value
                                 _type.HRESULT]


class ISpatialAnchorRawCoordinateSystemAdjustedEventArgs(_inspectable.IInspectable):
    get_OldRawCoordinateSystemToNewRawCoordinateSystemTransform: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4]],  # value
                                                                           _type.HRESULT]


class ISpatialAnchorStatics(_inspectable.IInspectable, factory=True):
    TryCreateRelativeTo: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                                    _Pointer[ISpatialAnchor]],  # value
                                   _type.HRESULT]
    TryCreateWithPositionRelativeTo: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                                                _struct.Windows.Foundation.Numerics.Vector3,  # position
                                                _Pointer[ISpatialAnchor]],  # value
                                               _type.HRESULT]
    TryCreateWithPositionAndOrientationRelativeTo: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                                                              _struct.Windows.Foundation.Numerics.Vector3,  # position
                                                              _struct.Windows.Foundation.Numerics.Quaternion,  # orientation
                                                              _Pointer[ISpatialAnchor]],  # value
                                                             _type.HRESULT]


class ISpatialAnchorStore(_inspectable.IInspectable):
    GetAllSavedAnchors: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, ISpatialAnchor]]],  # value
                                  _type.HRESULT]
    TrySave: _Callable[[_type.HSTRING,  # id
                        ISpatialAnchor,  # anchor
                        _Pointer[_type.boolean]],  # succeeded
                       _type.HRESULT]
    Remove: _Callable[[_type.HSTRING],  # id
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class ISpatialAnchorTransferManagerStatics(_inspectable.IInspectable, factory=True):
    TryImportAnchorsAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # stream
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.HSTRING, ISpatialAnchor]]]],  # operation
                                     _type.HRESULT]
    TryExportAnchorsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, ISpatialAnchor]],  # anchors
                                      _Windows_Storage_Streams.IOutputStream,  # stream
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]]],  # result
                                  _type.HRESULT]


class ISpatialBoundingVolume(_inspectable.IInspectable):
    pass


class ISpatialBoundingVolumeStatics(_inspectable.IInspectable, factory=True):
    FromBox: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                        _struct.Windows.Perception.Spatial.SpatialBoundingBox,  # box
                        _Pointer[ISpatialBoundingVolume]],  # value
                       _type.HRESULT]
    FromOrientedBox: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                                _struct.Windows.Perception.Spatial.SpatialBoundingOrientedBox,  # box
                                _Pointer[ISpatialBoundingVolume]],  # value
                               _type.HRESULT]
    FromSphere: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                           _struct.Windows.Perception.Spatial.SpatialBoundingSphere,  # sphere
                           _Pointer[ISpatialBoundingVolume]],  # value
                          _type.HRESULT]
    FromFrustum: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                            _struct.Windows.Perception.Spatial.SpatialBoundingFrustum,  # frustum
                            _Pointer[ISpatialBoundingVolume]],  # value
                           _type.HRESULT]


class ISpatialCoordinateSystem(_inspectable.IInspectable):
    TryGetTransformTo: _Callable[[ISpatialCoordinateSystem,  # target
                                  _Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Numerics.Matrix4x4]]],  # value
                                 _type.HRESULT]


class ISpatialEntity(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Anchor: _Callable[[_Pointer[ISpatialAnchor]],  # value
                          _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class ISpatialEntityAddedEventArgs(_inspectable.IInspectable):
    get_Entity: _Callable[[_Pointer[ISpatialEntity]],  # value
                          _type.HRESULT]


class ISpatialEntityFactory(_inspectable.IInspectable, factory=True):
    CreateWithSpatialAnchor: _Callable[[ISpatialAnchor,  # spatialAnchor
                                        _Pointer[ISpatialEntity]],  # value
                                       _type.HRESULT]
    CreateWithSpatialAnchorAndProperties: _Callable[[ISpatialAnchor,  # spatialAnchor
                                                     _Windows_Foundation_Collections.IPropertySet,  # propertySet
                                                     _Pointer[ISpatialEntity]],  # value
                                                    _type.HRESULT]


class ISpatialEntityRemovedEventArgs(_inspectable.IInspectable):
    get_Entity: _Callable[[_Pointer[ISpatialEntity]],  # value
                          _type.HRESULT]


class ISpatialEntityStore(_inspectable.IInspectable):
    SaveAsync: _Callable[[ISpatialEntity,  # entity
                          _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                         _type.HRESULT]
    RemoveAsync: _Callable[[ISpatialEntity,  # entity
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                           _type.HRESULT]
    CreateEntityWatcher: _Callable[[_Pointer[ISpatialEntityWatcher]],  # value
                                   _type.HRESULT]


class ISpatialEntityStoreStatics(_inspectable.IInspectable, factory=True):
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    TryGetForRemoteSystemSession: _Callable[[_Windows_System_RemoteSystems.IRemoteSystemSession,  # session
                                             _Pointer[ISpatialEntityStore]],  # value
                                            _type.HRESULT]


class ISpatialEntityUpdatedEventArgs(_inspectable.IInspectable):
    get_Entity: _Callable[[_Pointer[ISpatialEntity]],  # value
                          _type.HRESULT]


class ISpatialEntityWatcher(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Perception.Spatial.SpatialEntityWatcherStatus]],  # value
                          _type.HRESULT]
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialEntityWatcher, ISpatialEntityAddedEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialEntityWatcher, ISpatialEntityUpdatedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialEntityWatcher, ISpatialEntityRemovedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialEntityWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class ISpatialLocation(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                               _type.HRESULT]
    get_AbsoluteLinearVelocity: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                          _type.HRESULT]
    get_AbsoluteLinearAcceleration: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                              _type.HRESULT]
    AbsoluteAngularVelocity: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                                       _type.HRESULT]
    AbsoluteAngularAcceleration: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                                           _type.HRESULT]


class ISpatialLocation2(_inspectable.IInspectable):
    get_AbsoluteAngularVelocityAxisAngle: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                                    _type.HRESULT]
    get_AbsoluteAngularAccelerationAxisAngle: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                                        _type.HRESULT]


class ISpatialLocator(_inspectable.IInspectable):
    get_Locatability: _Callable[[_Pointer[_enum.Windows.Perception.Spatial.SpatialLocatability]],  # value
                                _type.HRESULT]
    add_LocatabilityChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialLocator, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_LocatabilityChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]
    add_PositionalTrackingDeactivating: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialLocator, ISpatialLocatorPositionalTrackingDeactivatingEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                                  _type.HRESULT]
    remove_PositionalTrackingDeactivating: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                     _type.HRESULT]
    TryLocateAtTimestamp: _Callable[[_Windows_Perception.IPerceptionTimestamp,  # timestamp
                                     ISpatialCoordinateSystem,  # coordinateSystem
                                     _Pointer[ISpatialLocation]],  # value
                                    _type.HRESULT]
    CreateAttachedFrameOfReferenceAtCurrentHeading: _Callable[[_Pointer[ISpatialLocatorAttachedFrameOfReference]],  # value
                                                              _type.HRESULT]
    CreateAttachedFrameOfReferenceAtCurrentHeadingWithPosition: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                           _Pointer[ISpatialLocatorAttachedFrameOfReference]],  # value
                                                                          _type.HRESULT]
    CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientation: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                                         _struct.Windows.Foundation.Numerics.Quaternion,  # relativeOrientation
                                                                                         _Pointer[ISpatialLocatorAttachedFrameOfReference]],  # value
                                                                                        _type.HRESULT]
    CreateAttachedFrameOfReferenceAtCurrentHeadingWithPositionAndOrientationAndRelativeHeading: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                                                           _struct.Windows.Foundation.Numerics.Quaternion,  # relativeOrientation
                                                                                                           _type.DOUBLE,  # relativeHeadingInRadians
                                                                                                           _Pointer[ISpatialLocatorAttachedFrameOfReference]],  # value
                                                                                                          _type.HRESULT]
    CreateStationaryFrameOfReferenceAtCurrentLocation: _Callable[[_Pointer[ISpatialStationaryFrameOfReference]],  # value
                                                                 _type.HRESULT]
    CreateStationaryFrameOfReferenceAtCurrentLocationWithPosition: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                              _Pointer[ISpatialStationaryFrameOfReference]],  # value
                                                                             _type.HRESULT]
    CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientation: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                                            _struct.Windows.Foundation.Numerics.Quaternion,  # relativeOrientation
                                                                                            _Pointer[ISpatialStationaryFrameOfReference]],  # value
                                                                                           _type.HRESULT]
    CreateStationaryFrameOfReferenceAtCurrentLocationWithPositionAndOrientationAndRelativeHeading: _Callable[[_struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                                                              _struct.Windows.Foundation.Numerics.Quaternion,  # relativeOrientation
                                                                                                              _type.DOUBLE,  # relativeHeadingInRadians
                                                                                                              _Pointer[ISpatialStationaryFrameOfReference]],  # value
                                                                                                             _type.HRESULT]


class ISpatialLocatorAttachedFrameOfReference(_inspectable.IInspectable):
    get_RelativePosition: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                    _type.HRESULT]
    put_RelativePosition: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                    _type.HRESULT]
    get_RelativeOrientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                                       _type.HRESULT]
    put_RelativeOrientation: _Callable[[_struct.Windows.Foundation.Numerics.Quaternion],  # value
                                       _type.HRESULT]
    AdjustHeading: _Callable[[_type.DOUBLE],  # headingOffsetInRadians
                             _type.HRESULT]
    GetStationaryCoordinateSystemAtTimestamp: _Callable[[_Windows_Perception.IPerceptionTimestamp,  # timestamp
                                                         _Pointer[ISpatialCoordinateSystem]],  # value
                                                        _type.HRESULT]
    TryGetRelativeHeadingAtTimestamp: _Callable[[_Windows_Perception.IPerceptionTimestamp,  # timestamp
                                                 _Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                _type.HRESULT]


class ISpatialLocatorPositionalTrackingDeactivatingEventArgs(_inspectable.IInspectable):
    get_Canceled: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_Canceled: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class ISpatialLocatorStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[ISpatialLocator]],  # value
                          _type.HRESULT]


class ISpatialStageFrameOfReference(_inspectable.IInspectable):
    get_CoordinateSystem: _Callable[[_Pointer[ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]
    get_MovementRange: _Callable[[_Pointer[_enum.Windows.Perception.Spatial.SpatialMovementRange]],  # value
                                 _type.HRESULT]
    get_LookDirectionRange: _Callable[[_Pointer[_enum.Windows.Perception.Spatial.SpatialLookDirectionRange]],  # value
                                      _type.HRESULT]
    GetCoordinateSystemAtCurrentLocation: _Callable[[ISpatialLocator,  # locator
                                                     _Pointer[ISpatialCoordinateSystem]],  # result
                                                    _type.HRESULT]
    TryGetMovementBounds: _Callable[[ISpatialCoordinateSystem,  # coordinateSystem
                                     _Pointer[_type.UINT32],  # __valueSize
                                     _Pointer[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]]],  # value
                                    _type.HRESULT]


class ISpatialStageFrameOfReferenceStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[ISpatialStageFrameOfReference]],  # value
                           _type.HRESULT]
    add_CurrentChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_CurrentChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    RequestNewStageAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISpatialStageFrameOfReference]]],  # result
                                    _type.HRESULT]


class ISpatialStationaryFrameOfReference(_inspectable.IInspectable):
    get_CoordinateSystem: _Callable[[_Pointer[ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]
