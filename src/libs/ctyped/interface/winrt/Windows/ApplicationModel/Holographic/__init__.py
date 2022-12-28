from __future__ import annotations as _

from typing import Callable as _Callable

from ...Perception import Spatial as _Windows_Perception_Spatial
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IHolographicKeyboard(_inspectable.IInspectable):
    SetPlacementOverride: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                     _struct.Windows.Foundation.Numerics.Vector3,  # topCenterPosition
                                     _struct.Windows.Foundation.Numerics.Quaternion],  # orientation
                                    _type.HRESULT]
    SetPlacementOverrideWithMaxSize: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                                _struct.Windows.Foundation.Numerics.Vector3,  # topCenterPosition
                                                _struct.Windows.Foundation.Numerics.Quaternion,  # orientation
                                                _struct.Windows.Foundation.Numerics.Vector2],  # maxSize
                                               _type.HRESULT]
    ResetPlacementOverride: _Callable[[],
                                      _type.HRESULT]


class IHolographicKeyboardStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IHolographicKeyboard]],  # result
                          _type.HRESULT]

    _factory = True
