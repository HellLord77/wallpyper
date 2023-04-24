from __future__ import annotations

from typing import Callable as _Callable

from . import d3d11 as _d3d11
from . import d3d11_1 as _d3d11_1
from . import d3d11_2 as _d3d11_2
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D11Texture2D1(_d3d11.ID3D11Texture2D):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_TEXTURE2D_DESC1]],  # pDesc
                        _type.c_void]


class ID3D11Texture3D1(_d3d11.ID3D11Texture3D):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_TEXTURE3D_DESC1]],  # pDesc
                        _type.c_void]


class ID3D11RasterizerState2(_d3d11_1.ID3D11RasterizerState1):
    GetDesc2: _Callable[[_Pointer[_struct.D3D11_RASTERIZER_DESC2]],  # pDesc
                        _type.c_void]


class ID3D11ShaderResourceView1(_d3d11.ID3D11ShaderResourceView):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_SHADER_RESOURCE_VIEW_DESC1]],  # pDesc1
                        _type.c_void]


class ID3D11RenderTargetView1(_d3d11.ID3D11RenderTargetView):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_RENDER_TARGET_VIEW_DESC1]],  # pDesc1
                        _type.c_void]


class ID3D11UnorderedAccessView1(_d3d11.ID3D11UnorderedAccessView):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_UNORDERED_ACCESS_VIEW_DESC1]],  # pDesc1
                        _type.c_void]


class ID3D11Query1(_d3d11.ID3D11Query):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_QUERY_DESC1]],  # pDesc1
                        _type.c_void]


class ID3D11DeviceContext3(_d3d11_2.ID3D11DeviceContext2):
    Flush1: _Callable[[_enum.D3D11_CONTEXT_TYPE,  # ContextType
                       _type.HANDLE],  # hEvent
                      _type.c_void]
    SetHardwareProtectionState: _Callable[[_type.BOOL],  # HwProtectionEnable
                                          _type.c_void]
    GetHardwareProtectionState: _Callable[[_Pointer[_type.BOOL]],  # pHwProtectionEnable
                                          _type.c_void]


class ID3D11Fence(_d3d11.ID3D11DeviceChild):
    CreateSharedHandle: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # pAttributes
                                   _type.DWORD,  # dwAccess
                                   _type.LPCWSTR,  # lpName
                                   _Pointer[_type.HANDLE]],  # pHandle
                                  _type.HRESULT]
    GetCompletedValue: _Callable[[],
                                 _type.UINT64]
    SetEventOnCompletion: _Callable[[_type.UINT64,  # Value
                                     _type.HANDLE],  # hEvent
                                    _type.HRESULT]


class ID3D11DeviceContext4(ID3D11DeviceContext3):
    Signal: _Callable[[ID3D11Fence,  # pFence
                       _type.UINT64],  # Value
                      _type.HRESULT]
    Wait: _Callable[[ID3D11Fence,  # pFence
                     _type.UINT64],  # Value
                    _type.HRESULT]


class ID3D11Device3(_d3d11_2.ID3D11Device2):
    CreateTexture2D1: _Callable[[_Pointer[_struct.D3D11_TEXTURE2D_DESC1],  # pDesc1
                                 _Pointer[_struct.D3D11_SUBRESOURCE_DATA],  # pInitialData
                                 _Pointer[ID3D11Texture2D1]],  # ppTexture2D
                                _type.HRESULT]
    CreateTexture3D1: _Callable[[_Pointer[_struct.D3D11_TEXTURE3D_DESC1],  # pDesc1
                                 _Pointer[_struct.D3D11_SUBRESOURCE_DATA],  # pInitialData
                                 _Pointer[ID3D11Texture3D1]],  # ppTexture3D
                                _type.HRESULT]
    CreateRasterizerState2: _Callable[[_Pointer[_struct.D3D11_RASTERIZER_DESC2],  # pRasterizerDesc
                                       _Pointer[ID3D11RasterizerState2]],  # ppRasterizerState
                                      _type.HRESULT]
    CreateShaderResourceView1: _Callable[[_d3d11.ID3D11Resource,  # pResource
                                          _Pointer[_struct.D3D11_SHADER_RESOURCE_VIEW_DESC1],  # pDesc1
                                          _Pointer[ID3D11ShaderResourceView1]],  # ppSRView1
                                         _type.HRESULT]
    CreateUnorderedAccessView1: _Callable[[_d3d11.ID3D11Resource,  # pResource
                                           _Pointer[_struct.D3D11_UNORDERED_ACCESS_VIEW_DESC1],  # pDesc1
                                           _Pointer[ID3D11UnorderedAccessView1]],  # ppUAView1
                                          _type.HRESULT]
    CreateRenderTargetView1: _Callable[[_d3d11.ID3D11Resource,  # pResource
                                        _Pointer[_struct.D3D11_RENDER_TARGET_VIEW_DESC1],  # pDesc1
                                        _Pointer[ID3D11RenderTargetView1]],  # ppRTView1
                                       _type.HRESULT]
    CreateQuery1: _Callable[[_Pointer[_struct.D3D11_QUERY_DESC1],  # pQueryDesc1
                             _Pointer[ID3D11Query1]],  # ppQuery1
                            _type.HRESULT]
    GetImmediateContext3: _Callable[[_Pointer[ID3D11DeviceContext3]],  # ppImmediateContext
                                    _type.c_void]
    CreateDeferredContext3: _Callable[[_type.UINT,  # ContextFlags
                                       _Pointer[ID3D11DeviceContext3]],  # ppDeferredContext
                                      _type.HRESULT]
    WriteToSubresource: _Callable[[_d3d11.ID3D11Resource,  # pDstResource
                                   _type.UINT,  # DstSubresource
                                   _Pointer[_struct.D3D11_BOX],  # pDstBox
                                   _type.c_void_p,  # pSrcData
                                   _type.UINT,  # SrcRowPitch
                                   _type.UINT],  # SrcDepthPitch
                                  _type.c_void]
    ReadFromSubresource: _Callable[[_type.c_void_p,  # pDstData
                                    _type.UINT,  # DstRowPitch
                                    _type.UINT,  # DstDepthPitch
                                    _d3d11.ID3D11Resource,  # pSrcResource
                                    _type.UINT,  # SrcSubresource
                                    _Pointer[_struct.D3D11_BOX]],  # pSrcBox
                                   _type.c_void]
