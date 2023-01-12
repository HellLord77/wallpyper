from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.shared import dxgi as _dxgi
from ..interface.um import d3d11 as _d3d11

# d3d11
D3D11CalcSubresource: _Callable[[_type.UINT,  # MipSlice
                                 _type.UINT,  # ArraySlice
                                 _type.UINT],  # MipLevels
                                _type.UINT]
D3D11CreateDevice: _Callable[[_dxgi.IDXGIAdapter,  # pAdapter
                              _enum.D3D_DRIVER_TYPE,  # DriverType
                              _type.HMODULE,  # Software
                              _type.UINT,  # Flags
                              _Pointer[_enum.D3D_FEATURE_LEVEL],  # pFeatureLevels
                              _type.UINT,  # FeatureLevels
                              _type.UINT,  # SDKVersion
                              _Pointer[_d3d11.ID3D11Device],  # ppDevice
                              _Pointer[_enum.D3D_FEATURE_LEVEL],  # pFeatureLevel
                              _Pointer[_d3d11.ID3D11DeviceContext]],  # ppImmediateContext
                             _type.HRESULT]
D3D11CreateDeviceAndSwapChain: _Callable[[_dxgi.IDXGIAdapter,  # pAdapter
                                          _enum.D3D_DRIVER_TYPE,  # DriverType
                                          _type.HMODULE,  # Software
                                          _type.UINT,  # Flags
                                          _Pointer[_enum.D3D_FEATURE_LEVEL],  # pFeatureLevels
                                          _type.UINT,  # FeatureLevels
                                          _type.UINT,  # SDKVersion
                                          _Pointer[_struct.DXGI_SWAP_CHAIN_DESC],  # pSwapChainDesc
                                          _Pointer[_dxgi.IDXGISwapChain],  # ppSwapChain
                                          _Pointer[_d3d11.ID3D11Device],  # ppDevice
                                          _Pointer[_enum.D3D_FEATURE_LEVEL],  # pFeatureLevel
                                          _Pointer[_d3d11.ID3D11DeviceContext]],  # ppImmediateContext
                                         _type.HRESULT]

_WinLib(__name__)
