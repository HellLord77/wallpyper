from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.shared import dxgi as _dxgi
from ..interface.um import d2d1_1 as _d2d1_1

# d2d1
D2D1CreateFactory: _Callable[[_enum.D2D1_FACTORY_TYPE,  # factoryType
                              _Pointer[_struct.IID],  # riid
                              _Optional[_Pointer[_struct.D2D1_FACTORY_OPTIONS]],  # pFactoryOptions
                              _type.c_void_p],  # ppIFactory
                             _type.HRESULT]
D2D1MakeRotateMatrix: _Callable[[_type.FLOAT,  # angle
                                 _struct.D2D1_POINT_2F,  # center
                                 _Pointer[_struct.D2D1_POINT_2F]],  # matrix
                                _type.c_void]
D2D1MakeSkewMatrix: _Callable[[_type.FLOAT,  # angleX
                               _type.FLOAT,  # angleY
                               _struct.D2D1_POINT_2F,  # center
                               _Pointer[_struct.D2D1_MATRIX_3X2_F]],  # matrix
                              _type.c_void]
D2D1IsMatrixInvertible: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # matrix
                                  _type.BOOL]
D2D1InvertMatrix: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # matrix
                            _type.BOOL]
# d2d1_1
D2D1CreateDeviceContext: _Callable[[_dxgi.IDXGISurface,  # dxgiSurface
                                    _Optional[_Pointer[_struct.D2D1_CREATION_PROPERTIES]],  # creationProperties
                                    _Pointer[_d2d1_1.ID2D1DeviceContext]],  # d2dDeviceContext
                                   _type.HRESULT]
D2D1SinCos: _Callable[[_type.FLOAT,  # angle
                       _Pointer[_type.FLOAT],  # s
                       _Pointer[_type.FLOAT]],  # c
                      _type.c_void]
D2D1Tan: _Callable[[_type.FLOAT],  # angle
                   _type.FLOAT]
D2D1Vec3Length: _Callable[[_type.FLOAT,  # x
                           _type.FLOAT,  # y
                           _type.FLOAT],  # z
                          _type.FLOAT]

_WinLib(__name__)
