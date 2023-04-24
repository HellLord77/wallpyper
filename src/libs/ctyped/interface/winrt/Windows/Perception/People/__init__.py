from __future__ import annotations

from typing import Callable as _Callable

from .. import Spatial as _Windows_Perception_Spatial
from ... import Foundation as _Windows_Foundation
from ... import Perception as _Windows_Perception
from ...UI.Input import Spatial as _Windows_UI_Input_Spatial
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IEyesPose(_inspectable.IInspectable):
    get_IsCalibrationValid: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_Gaze: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Perception.Spatial.SpatialRay]]],  # value
                        _type.HRESULT]
    get_UpdateTimestamp: _Callable[[_Pointer[_Windows_Perception.IPerceptionTimestamp]],  # value
                                   _type.HRESULT]


class IEyesPoseStatics(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.UI.Input.GazeInputAccessStatus]]],  # operation
                                  _type.HRESULT]

    _factory = True


class IHandMeshObserver(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_Windows_UI_Input_Spatial.ISpatialInteractionSource]],  # value
                          _type.HRESULT]
    get_TriangleIndexCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    get_VertexCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    GetTriangleIndices: _Callable[[_type.UINT32,  # __indicesSize
                                   _Pointer[_type.UINT16]],  # indices
                                  _type.HRESULT]
    GetVertexStateForPose: _Callable[[IHandPose,  # handPose
                                      _Pointer[IHandMeshVertexState]],  # result
                                     _type.HRESULT]
    get_NeutralPose: _Callable[[_Pointer[IHandPose]],  # value
                               _type.HRESULT]
    get_NeutralPoseVersion: _Callable[[_Pointer[_type.INT32]],  # value
                                      _type.HRESULT]
    get_ModelId: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]


class IHandMeshVertexState(_inspectable.IInspectable):
    get_CoordinateSystem: _Callable[[_Pointer[_Windows_Perception_Spatial.ISpatialCoordinateSystem]],  # value
                                    _type.HRESULT]
    GetVertices: _Callable[[_type.UINT32,  # __verticesSize
                            _Pointer[_struct.Windows.Perception.People.HandMeshVertex]],  # vertices
                           _type.HRESULT]
    get_UpdateTimestamp: _Callable[[_Pointer[_Windows_Perception.IPerceptionTimestamp]],  # value
                                   _type.HRESULT]


class IHandPose(_inspectable.IInspectable):
    TryGetJoint: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                            _enum.Windows.Perception.People.HandJointKind,  # joint
                            _Pointer[_struct.Windows.Perception.People.JointPose],  # jointPose
                            _Pointer[_type.boolean]],  # result
                           _type.HRESULT]
    TryGetJoints: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                             _type.UINT32,  # __jointsSize
                             _Pointer[_enum.Windows.Perception.People.HandJointKind],  # joints
                             _type.UINT32,  # __jointPosesSize
                             _Pointer[_struct.Windows.Perception.People.JointPose],  # jointPoses
                             _Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    GetRelativeJoint: _Callable[[_enum.Windows.Perception.People.HandJointKind,  # joint
                                 _enum.Windows.Perception.People.HandJointKind,  # referenceJoint
                                 _Pointer[_struct.Windows.Perception.People.JointPose]],  # result
                                _type.HRESULT]
    GetRelativeJoints: _Callable[[_type.UINT32,  # __jointsSize
                                  _Pointer[_enum.Windows.Perception.People.HandJointKind],  # joints
                                  _type.UINT32,  # __referenceJointsSize
                                  _Pointer[_enum.Windows.Perception.People.HandJointKind],  # referenceJoints
                                  _type.UINT32,  # __jointPosesSize
                                  _Pointer[_struct.Windows.Perception.People.JointPose]],  # jointPoses
                                 _type.HRESULT]


class IHeadPose(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    get_ForwardDirection: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                    _type.HRESULT]
    get_UpDirection: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
