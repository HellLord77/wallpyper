from __future__ import annotations

from typing import Callable as _Callable

from . import d2d1 as _d2d1
from . import d2d1_1 as _d2d1_1
from ..shared import dxgi as _dxgi
from ... import enum as _enum
from ... import type as _type
from ..._utils import _Pointer


class ID2D1GeometryRealization(_d2d1.ID2D1Resource):
    pass


class ID2D1DeviceContext1(_d2d1_1.ID2D1DeviceContext):
    CreateFilledGeometryRealization: _Callable[[_d2d1.ID2D1Geometry,  # geometry
                                                _type.FLOAT,  # flatteningTolerance
                                                _Pointer[ID2D1GeometryRealization]],  # geometryRealization
                                               _type.HRESULT]
    CreateStrokedGeometryRealization: _Callable[[_d2d1.ID2D1Geometry,  # geometry
                                                 _type.FLOAT,  # flatteningTolerance
                                                 _type.FLOAT,  # strokeWidth
                                                 _d2d1.ID2D1StrokeStyle,  # strokeStyle
                                                 _Pointer[ID2D1GeometryRealization]],  # geometryRealization
                                                _type.HRESULT]
    DrawGeometryRealization: _Callable[[ID2D1GeometryRealization,  # geometryRealization
                                        _d2d1.ID2D1Brush],  # brush
                                       _type.c_void]


class ID2D1Device1(_d2d1_1.ID2D1Device):
    GetRenderingPriority: _Callable[[],
                                    _enum.D2D1_RENDERING_PRIORITY]
    SetRenderingPriority: _Callable[[_enum.D2D1_RENDERING_PRIORITY],  # renderingPriority
                                    _type.c_void]
    CreateDeviceContext_: _Callable[[_enum.D2D1_DEVICE_CONTEXT_OPTIONS,  # options
                                     _Pointer[ID2D1DeviceContext1]],  # deviceContext1
                                    _type.HRESULT]


class ID2D1Factory2(_d2d1_1.ID2D1Factory1):
    CreateDevice_: _Callable[[_dxgi.IDXGIDevice,  # dxgiDevice
                              _Pointer[ID2D1Device1]],  # d2dDevice1
                             _type.HRESULT]


class ID2D1CommandSink1(_d2d1_1.ID2D1CommandSink):
    SetPrimitiveBlend1: _Callable[[_enum.D2D1_PRIMITIVE_BLEND],  # primitiveBlend
                                  _type.HRESULT]
