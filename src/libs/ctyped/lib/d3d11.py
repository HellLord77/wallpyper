from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import type as _type
from .._utils import _Pointer
from ..interface.shared import dxgi as _dxgi
from ..interface.um import d3d11 as _d3d11

# d3d11
D3D11CreateDevice: _Callable[[_Optional[_dxgi.IDXGIAdapter],  # pAdapter
                              _enum.D3D_DRIVER_TYPE,  # DriverType
                              _type.HMODULE,  # Software
                              _type.UINT,  # Flags
                              _Optional[_Pointer[_enum.D3D_FEATURE_LEVEL]],  # pFeatureLevels
                              _type.UINT,  # FeatureLevels
                              _type.UINT,  # SDKVersion
                              _Optional[_Pointer[_d3d11.ID3D11Device]],  # ppDevice
                              _Optional[_Pointer[_enum.D3D_FEATURE_LEVEL]],  # pFeatureLevel,
                              _Optional[_Pointer[_d3d11.ID3D11DeviceContext]]],  # ppImmediateContext
                             _type.HRESULT]

_WinLib(__name__)
