from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Spatial as _Windows_Perception_Spatial
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISpatialGraphInteropFrameOfReferencePreview(_inspectable.IInspectable):
    get_CoordinateSystem: _Callable[[_Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]
    get_NodeId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_CoordinateSystemToNodeTransform: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix4x4]],  # value
                                                   _type.HRESULT]


class ISpatialGraphInteropPreviewStatics(_inspectable.IInspectable):
    CreateCoordinateSystemForNode: _Callable[[_struct.GUID,  # nodeId
                                              _Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # result
                                             _type.HRESULT]
    CreateCoordinateSystemForNodeWithPosition: _Callable[[_struct.GUID,  # nodeId
                                                          _struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                          _Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # result
                                                         _type.HRESULT]
    CreateCoordinateSystemForNodeWithPositionAndOrientation: _Callable[[_struct.GUID,  # nodeId
                                                                        _struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                        _struct.Windows.Foundation.Numerics.Quaternion,  # relativeOrientation
                                                                        _Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # result
                                                                       _type.HRESULT]
    CreateLocatorForNode: _Callable[[_struct.GUID,  # nodeId
                                     _Pointer[_Windows_Perception_Spatial.ISpatialLocator]],  # result
                                    _type.HRESULT]

    _factory = True


class ISpatialGraphInteropPreviewStatics2(_inspectable.IInspectable):
    TryCreateFrameOfReference: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                          _Pointer[ISpatialGraphInteropFrameOfReferencePreview]],  # result
                                         _type.HRESULT]
    TryCreateFrameOfReferenceWithPosition: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                                      _struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                      _Pointer[ISpatialGraphInteropFrameOfReferencePreview]],  # result
                                                     _type.HRESULT]
    TryCreateFrameOfReferenceWithPositionAndOrientation: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                                                    _struct.Windows.Foundation.Numerics.Vector3,  # relativePosition
                                                                    _struct.Windows.Foundation.Numerics.Quaternion,  # relativeOrientation
                                                                    _Pointer[ISpatialGraphInteropFrameOfReferencePreview]],  # result
                                                                   _type.HRESULT]

    _factory = True
