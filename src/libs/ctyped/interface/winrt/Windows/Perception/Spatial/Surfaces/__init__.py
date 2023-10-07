from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Spatial as _Windows_Perception_Spatial
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISpatialSurfaceInfo(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]
    get_UpdateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                              _type.HRESULT]
    TryGetBounds: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                             _Pointer[_Windows_Foundation.IReference[_struct.Windows.Perception.Spatial.SpatialBoundingOrientedBox]]],  # value
                            _type.HRESULT]
    TryComputeLatestMeshAsync: _Callable[[_type.DOUBLE,  # maxTrianglesPerCubicMeter
                                          _Pointer[_Windows_Foundation.IAsyncOperation[ISpatialSurfaceMesh]]],  # value
                                         _type.HRESULT]
    TryComputeLatestMeshWithOptionsAsync: _Callable[[_type.DOUBLE,  # maxTrianglesPerCubicMeter
                                                     ISpatialSurfaceMeshOptions,  # options
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[ISpatialSurfaceMesh]]],  # value
                                                    _type.HRESULT]


class ISpatialSurfaceMesh(_inspectable.IInspectable):
    get_SurfaceInfo: _Callable[[_Pointer[ISpatialSurfaceInfo]],  # value
                               _type.HRESULT]
    get_CoordinateSystem: _Callable[[_Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]
    get_TriangleIndices: _Callable[[_Pointer[ISpatialSurfaceMeshBuffer]],  # value
                                   _type.HRESULT]
    get_VertexPositions: _Callable[[_Pointer[ISpatialSurfaceMeshBuffer]],  # value
                                   _type.HRESULT]
    get_VertexPositionScale: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                       _type.HRESULT]
    get_VertexNormals: _Callable[[_Pointer[ISpatialSurfaceMeshBuffer]],  # value
                                 _type.HRESULT]


class ISpatialSurfaceMeshBuffer(_inspectable.IInspectable):
    get_Format: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                          _type.HRESULT]
    get_Stride: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_ElementCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]


class ISpatialSurfaceMeshOptions(_inspectable.IInspectable):
    get_VertexPositionFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                                        _type.HRESULT]
    put_VertexPositionFormat: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPixelFormat],  # value
                                        _type.HRESULT]
    get_TriangleIndexFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                                       _type.HRESULT]
    put_TriangleIndexFormat: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPixelFormat],  # value
                                       _type.HRESULT]
    get_VertexNormalFormat: _Callable[[_Pointer[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]],  # value
                                      _type.HRESULT]
    put_VertexNormalFormat: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPixelFormat],  # value
                                      _type.HRESULT]
    get_IncludeVertexNormals: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IncludeVertexNormals: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]


class ISpatialSurfaceMeshOptionsStatics(_inspectable.IInspectable, factory=True):
    get_SupportedVertexPositionFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]]],  # value
                                                  _type.HRESULT]
    get_SupportedTriangleIndexFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]]],  # value
                                                 _type.HRESULT]
    get_SupportedVertexNormalFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.DirectX.DirectXPixelFormat]]],  # value
                                                _type.HRESULT]


class ISpatialSurfaceObserver(_inspectable.IInspectable):
    GetObservedSurfaces: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, ISpatialSurfaceInfo]]],  # value
                                   _type.HRESULT]
    SetBoundingVolume: _Callable[[_Windows_Perception_Spatial.ISpatialBoundingVolume],  # bounds
                                 _type.HRESULT]
    SetBoundingVolumes: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Perception_Spatial.ISpatialBoundingVolume]],  # bounds
                                  _type.HRESULT]
    add_ObservedSurfacesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialSurfaceObserver, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ObservedSurfacesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class ISpatialSurfaceObserverStatics(_inspectable.IInspectable, factory=True):
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Perception.Spatial.SpatialPerceptionAccessStatus]]],  # result
                                  _type.HRESULT]


class ISpatialSurfaceObserverStatics2(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
