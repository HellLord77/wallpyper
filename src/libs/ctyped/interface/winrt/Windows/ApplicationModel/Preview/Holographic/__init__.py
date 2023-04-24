from __future__ import annotations

from typing import Callable as _Callable

from ... import Activation as _Windows_ApplicationModel_Activation
from ....Perception import Spatial as _Windows_Perception_Spatial
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IHolographicApplicationPreviewStatics(_inspectable.IInspectable):
    IsCurrentViewPresentedOnHolographicDisplay: _Callable[[_Pointer[_type.boolean]],  # result
                                                          _type.HRESULT]
    IsHolographicActivation: _Callable[[_Windows_ApplicationModel_Activation.IActivatedEventArgs,  # activatedEventArgs
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]

    _factory = True


class IHolographicKeyboardPlacementOverridePreview(_inspectable.IInspectable):
    SetPlacementOverride: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                     _struct.Windows.Foundation.Numerics.Vector3,  # topCenterPosition
                                     _struct.Windows.Foundation.Numerics.Vector3],  # normal
                                    _type.HRESULT]
    SetPlacementOverrideWithMaxSize: _Callable[[_Windows_Perception_Spatial.ISpatialCoordinateSystem,  # coordinateSystem
                                                _struct.Windows.Foundation.Numerics.Vector3,  # topCenterPosition
                                                _struct.Windows.Foundation.Numerics.Vector3,  # normal
                                                _struct.Windows.Foundation.Numerics.Vector2],  # maxSize
                                               _type.HRESULT]
    ResetPlacementOverride: _Callable[[],
                                      _type.HRESULT]


class IHolographicKeyboardPlacementOverridePreviewStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[IHolographicKeyboardPlacementOverridePreview]],  # result
                                 _type.HRESULT]

    _factory = True
