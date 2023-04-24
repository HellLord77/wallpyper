from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D10DeviceChild(_Unknwnbase.IUnknown):
    GetDevice: _Callable[[_Pointer[ID3D10Device]],  # ppDevice
                         _type.c_void]
    GetPrivateData: _Callable[[_Pointer[_struct.GUID],  # guid
                               _Pointer[_type.UINT],  # pDataSize
                               _type.c_void_p],  # pData
                              _type.HRESULT]
    SetPrivateData: _Callable[[_Pointer[_struct.GUID],  # guid
                               _type.UINT,  # DataSize
                               _type.c_void_p],  # pData
                              _type.HRESULT]
    SetPrivateDataInterface: _Callable[[_Pointer[_struct.GUID],  # guid
                                        _Unknwnbase.IUnknown],  # pData
                                       _type.HRESULT]


class ID3D10DepthStencilState(ID3D10DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_DEPTH_STENCIL_DESC]],  # pDesc
                       _type.c_void]


class ID3D10BlendState(ID3D10DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_BLEND_DESC]],  # pDesc
                       _type.c_void]


class ID3D10RasterizerState(ID3D10DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_RASTERIZER_DESC]],  # pDesc
                       _type.c_void]


class ID3D10Resource(ID3D10DeviceChild):
    GetType: _Callable[[_Pointer[_enum.D3D10_RESOURCE_DIMENSION]],  # rType
                       _type.c_void]
    SetEvictionPriority: _Callable[[_type.UINT],  # EvictionPriority
                                   _type.c_void]
    GetEvictionPriority: _Callable[[],
                                   _type.UINT]


class ID3D10Buffer(ID3D10Resource):
    Map: _Callable[[_enum.D3D10_MAP,  # MapType
                    _type.UINT,  # MapFlags
                    _type.c_void_p],  # ppData
                   _type.HRESULT]
    Unmap: _Callable[[],
                     _type.c_void]
    GetDesc: _Callable[[_Pointer[_struct.D3D10_BUFFER_DESC]],  # pDesc
                       _type.c_void]


class ID3D10Texture1D(ID3D10Resource):
    Map: _Callable[[_type.UINT,  # Subresource
                    _enum.D3D10_MAP,  # MapType
                    _type.UINT,  # MapFlags
                    _type.c_void_p],  # ppData
                   _type.HRESULT]
    Unmap: _Callable[[_type.UINT],  # Subresource
                     _type.c_void]
    GetDesc: _Callable[[_Pointer[_struct.D3D10_TEXTURE1D_DESC]],  # pDesc
                       _type.c_void]


class ID3D10Texture2D(ID3D10Resource):
    Map: _Callable[[_type.UINT,  # Subresource
                    _enum.D3D10_MAP,  # MapType
                    _type.UINT,  # MapFlags
                    _Pointer[_struct.D3D10_MAPPED_TEXTURE2D]],  # pMappedTex2D
                   _type.HRESULT]
    Unmap: _Callable[[_type.UINT],  # Subresource
                     _type.c_void]
    GetDesc: _Callable[[_Pointer[_struct.D3D10_TEXTURE2D_DESC]],  # pDesc
                       _type.c_void]


class ID3D10Texture3D(ID3D10Resource):
    Map: _Callable[[_type.UINT,  # Subresource
                    _enum.D3D10_MAP,  # MapType
                    _type.UINT,  # MapFlags
                    _Pointer[_struct.D3D10_MAPPED_TEXTURE3D]],  # pMappedTex3D
                   _type.HRESULT]
    Unmap: _Callable[[_type.UINT],  # Subresource
                     _type.c_void]
    GetDesc: _Callable[[_Pointer[_struct.D3D10_TEXTURE3D_DESC]],  # pDesc
                       _type.c_void]


class ID3D10View(ID3D10DeviceChild):
    GetResource: _Callable[[_Pointer[ID3D10Resource]],  # ppResource
                           _type.c_void]


class ID3D10ShaderResourceView(ID3D10View):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_SHADER_RESOURCE_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D10RenderTargetView(ID3D10View):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_RENDER_TARGET_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D10DepthStencilView(ID3D10View):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_DEPTH_STENCIL_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D10VertexShader(ID3D10DeviceChild):
    pass


class ID3D10GeometryShader(ID3D10DeviceChild):
    pass


class ID3D10PixelShader(ID3D10DeviceChild):
    pass


class ID3D10InputLayout(ID3D10DeviceChild):
    pass


class ID3D10SamplerState(ID3D10DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_SAMPLER_DESC]],  # pDesc
                       _type.c_void]


class ID3D10Asynchronous(ID3D10DeviceChild):
    Begin: _Callable[[],
                     _type.c_void]
    End: _Callable[[],
                   _type.c_void]
    GetData: _Callable[[_type.c_void_p,  # pData
                        _type.UINT,  # DataSize
                        _type.UINT],  # GetDataFlags
                       _type.HRESULT]
    GetDataSize: _Callable[[],
                           _type.UINT]


class ID3D10Query(ID3D10Asynchronous):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_QUERY_DESC]],  # pDesc
                       _type.c_void]


class ID3D10Predicate(ID3D10Query):
    pass


class ID3D10Counter(ID3D10Asynchronous):
    GetDesc: _Callable[[_Pointer[_struct.D3D10_COUNTER_DESC]],  # pDesc
                       _type.c_void]


class ID3D10Device(_Unknwnbase.IUnknown):
    VSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D10Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    PSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D10ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    PSSetShader: _Callable[[ID3D10PixelShader],  # pPixelShader
                           _type.c_void]
    PSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D10SamplerState]],  # ppSamplers
                             _type.c_void]
    VSSetShader: _Callable[[ID3D10VertexShader],  # pVertexShader
                           _type.c_void]
    DrawIndexed: _Callable[[_type.UINT,  # IndexCount
                            _type.UINT,  # StartIndexLocation
                            _type.INT],  # BaseVertexLocation
                           _type.c_void]
    Draw: _Callable[[_type.UINT,  # VertexCount
                     _type.UINT],  # StartVertexLocation
                    _type.c_void]
    PSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D10Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    IASetInputLayout: _Callable[[ID3D10InputLayout],  # pInputLayout
                                _type.c_void]
    IASetVertexBuffers: _Callable[[_type.UINT,  # StartSlot
                                   _type.UINT,  # NumBuffers
                                   _Pointer[ID3D10Buffer],  # ppVertexBuffers
                                   _Pointer[_type.UINT],  # pStrides
                                   _Pointer[_type.UINT]],  # pOffsets
                                  _type.c_void]
    IASetIndexBuffer: _Callable[[ID3D10Buffer,  # pIndexBuffer
                                 _enum.DXGI_FORMAT,  # Format
                                 _type.UINT],  # Offset
                                _type.c_void]
    DrawIndexedInstanced: _Callable[[_type.UINT,  # IndexCountPerInstance
                                     _type.UINT,  # InstanceCount
                                     _type.UINT,  # StartIndexLocation
                                     _type.INT,  # BaseVertexLocation
                                     _type.UINT],  # StartInstanceLocation
                                    _type.c_void]
    DrawInstanced: _Callable[[_type.UINT,  # VertexCountPerInstance
                              _type.UINT,  # InstanceCount
                              _type.UINT,  # StartVertexLocation
                              _type.UINT],  # StartInstanceLocation
                             _type.c_void]
    GSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D10Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    GSSetShader: _Callable[[ID3D10GeometryShader],  # pShader
                           _type.c_void]
    IASetPrimitiveTopology: _Callable[[_enum.D3D10_PRIMITIVE_TOPOLOGY],  # Topology
                                      _type.c_void]
    VSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D10ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    VSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D10SamplerState]],  # ppSamplers
                             _type.c_void]
    SetPredication: _Callable[[ID3D10Predicate,  # pPredicate
                               _type.BOOL],  # PredicateValue
                              _type.c_void]
    GSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D10ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    GSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D10SamplerState]],  # ppSamplers
                             _type.c_void]
    OMSetRenderTargets: _Callable[[_type.UINT,  # NumViews
                                   _Pointer[ID3D10RenderTargetView],  # ppRenderTargetViews
                                   ID3D10DepthStencilView],  # pDepthStencilView
                                  _type.c_void]
    OMSetBlendState: _Callable[[ID3D10BlendState,  # pBlendState
                                _Pointer[_type.FLOAT],  # BlendFactor
                                _type.UINT],  # SampleMask
                               _type.c_void]
    OMSetDepthStencilState: _Callable[[ID3D10DepthStencilState,  # pDepthStencilState
                                       _type.UINT],  # StencilRef
                                      _type.c_void]
    SOSetTargets: _Callable[[_type.UINT,  # NumBuffers
                             _Pointer[ID3D10Buffer],  # ppSOTargets
                             _Pointer[_type.UINT]],  # pOffsets
                            _type.c_void]
    DrawAuto: _Callable[[],
                        _type.c_void]
    RSSetState: _Callable[[ID3D10RasterizerState],  # pRasterizerState
                          _type.c_void]
    RSSetViewports: _Callable[[_type.UINT,  # NumViewports
                               _Pointer[_struct.D3D10_VIEWPORT]],  # pViewports
                              _type.c_void]
    RSSetScissorRects: _Callable[[_type.UINT,  # NumRects
                                  _Pointer[_struct.D3D10_RECT]],  # pRects
                                 _type.c_void]
    CopySubresourceRegion: _Callable[[ID3D10Resource,  # pDstResource
                                      _type.UINT,  # DstSubresource
                                      _type.UINT,  # DstX
                                      _type.UINT,  # DstY
                                      _type.UINT,  # DstZ
                                      ID3D10Resource,  # pSrcResource
                                      _type.UINT,  # SrcSubresource
                                      _Pointer[_struct.D3D10_BOX]],  # pSrcBox
                                     _type.c_void]
    CopyResource: _Callable[[ID3D10Resource,  # pDstResource
                             ID3D10Resource],  # pSrcResource
                            _type.c_void]
    UpdateSubresource: _Callable[[ID3D10Resource,  # pDstResource
                                  _type.UINT,  # DstSubresource
                                  _Pointer[_struct.D3D10_BOX],  # pDstBox
                                  _type.c_void_p,  # pSrcData
                                  _type.UINT,  # SrcRowPitch
                                  _type.UINT],  # SrcDepthPitch
                                 _type.c_void]
    ClearRenderTargetView: _Callable[[ID3D10RenderTargetView,  # pRenderTargetView
                                      _Pointer[_type.FLOAT]],  # ColorRGBA
                                     _type.c_void]
    ClearDepthStencilView: _Callable[[ID3D10DepthStencilView,  # pDepthStencilView
                                      _type.UINT,  # ClearFlags
                                      _type.FLOAT,  # Depth
                                      _type.UINT8],  # Stencil
                                     _type.c_void]
    GenerateMips: _Callable[[ID3D10ShaderResourceView],  # pShaderResourceView
                            _type.c_void]
    ResolveSubresource: _Callable[[ID3D10Resource,  # pDstResource
                                   _type.UINT,  # DstSubresource
                                   ID3D10Resource,  # pSrcResource
                                   _type.UINT,  # SrcSubresource
                                   _enum.DXGI_FORMAT],  # Format
                                  _type.c_void]
    VSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D10Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    PSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D10ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    PSGetShader: _Callable[[_Pointer[ID3D10PixelShader]],  # ppPixelShader
                           _type.c_void]
    PSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D10SamplerState]],  # ppSamplers
                             _type.c_void]
    VSGetShader: _Callable[[_Pointer[ID3D10VertexShader]],  # ppVertexShader
                           _type.c_void]
    PSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D10Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    IAGetInputLayout: _Callable[[_Pointer[ID3D10InputLayout]],  # ppInputLayout
                                _type.c_void]
    IAGetVertexBuffers: _Callable[[_type.UINT,  # StartSlot
                                   _type.UINT,  # NumBuffers
                                   _Pointer[ID3D10Buffer],  # ppVertexBuffers
                                   _Pointer[_type.UINT],  # pStrides
                                   _Pointer[_type.UINT]],  # pOffsets
                                  _type.c_void]
    IAGetIndexBuffer: _Callable[[_Pointer[ID3D10Buffer],  # pIndexBuffer
                                 _Pointer[_enum.DXGI_FORMAT],  # Format
                                 _Pointer[_type.UINT]],  # Offset
                                _type.c_void]
    GSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D10Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    GSGetShader: _Callable[[_Pointer[ID3D10GeometryShader]],  # ppGeometryShader
                           _type.c_void]
    IAGetPrimitiveTopology: _Callable[[_Pointer[_enum.D3D10_PRIMITIVE_TOPOLOGY]],  # pTopology
                                      _type.c_void]
    VSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D10ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    VSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D10SamplerState]],  # ppSamplers
                             _type.c_void]
    GetPredication: _Callable[[_Pointer[ID3D10Predicate],  # ppPredicate
                               _Pointer[_type.BOOL]],  # pPredicateValue
                              _type.c_void]
    GSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D10ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    GSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D10SamplerState]],  # ppSamplers
                             _type.c_void]
    OMGetRenderTargets: _Callable[[_type.UINT,  # NumViews
                                   _Pointer[ID3D10RenderTargetView],  # ppRenderTargetViews
                                   _Pointer[ID3D10DepthStencilView]],  # ppDepthStencilView
                                  _type.c_void]
    OMGetBlendState: _Callable[[_Pointer[ID3D10BlendState],  # ppBlendState
                                _Pointer[_type.FLOAT],  # BlendFactor
                                _Pointer[_type.UINT]],  # pSampleMask
                               _type.c_void]
    OMGetDepthStencilState: _Callable[[_Pointer[ID3D10DepthStencilState],  # ppDepthStencilState
                                       _Pointer[_type.UINT]],  # pStencilRef
                                      _type.c_void]
    SOGetTargets: _Callable[[_type.UINT,  # NumBuffers
                             _Pointer[ID3D10Buffer],  # ppSOTargets
                             _Pointer[_type.UINT]],  # pOffsets
                            _type.c_void]
    RSGetState: _Callable[[_Pointer[ID3D10RasterizerState]],  # ppRasterizerState
                          _type.c_void]
    RSGetViewports: _Callable[[_Pointer[_type.UINT],  # NumViewports
                               _Pointer[_struct.D3D10_VIEWPORT]],  # pViewports
                              _type.c_void]
    RSGetScissorRects: _Callable[[_Pointer[_type.UINT],  # NumRects
                                  _Pointer[_struct.D3D10_RECT]],  # pRects
                                 _type.c_void]
    GetDeviceRemovedReason: _Callable[[],
                                      _type.HRESULT]
    SetExceptionMode: _Callable[[_type.UINT],  # RaiseFlags
                                _type.HRESULT]
    GetExceptionMode: _Callable[[],
                                _type.UINT]
    GetPrivateData: _Callable[[_Pointer[_struct.GUID],  # guid
                               _Pointer[_type.UINT],  # pDataSize
                               _type.c_void_p],  # pData
                              _type.HRESULT]
    SetPrivateData: _Callable[[_Pointer[_struct.GUID],  # guid
                               _type.UINT,  # DataSize
                               _type.c_void_p],  # pData
                              _type.HRESULT]
    SetPrivateDataInterface: _Callable[[_Pointer[_struct.GUID],  # guid
                                        _Unknwnbase.IUnknown],  # pData
                                       _type.HRESULT]
    ClearState: _Callable[[],
                          _type.c_void]
    Flush: _Callable[[],
                     _type.c_void]
    CreateBuffer: _Callable[[_Pointer[_struct.D3D10_BUFFER_DESC],  # pDesc
                             _Pointer[_struct.D3D10_SUBRESOURCE_DATA],  # pInitialData
                             _Pointer[ID3D10Buffer]],  # ppBuffer
                            _type.HRESULT]
    CreateTexture1D: _Callable[[_Pointer[_struct.D3D10_TEXTURE1D_DESC],  # pDesc
                                _Pointer[_struct.D3D10_SUBRESOURCE_DATA],  # pInitialData
                                _Pointer[ID3D10Texture1D]],  # ppTexture1D
                               _type.HRESULT]
    CreateTexture2D: _Callable[[_Pointer[_struct.D3D10_TEXTURE2D_DESC],  # pDesc
                                _Pointer[_struct.D3D10_SUBRESOURCE_DATA],  # pInitialData
                                _Pointer[ID3D10Texture2D]],  # ppTexture2D
                               _type.HRESULT]
    CreateTexture3D: _Callable[[_Pointer[_struct.D3D10_TEXTURE3D_DESC],  # pDesc
                                _Pointer[_struct.D3D10_SUBRESOURCE_DATA],  # pInitialData
                                _Pointer[ID3D10Texture3D]],  # ppTexture3D
                               _type.HRESULT]
    CreateShaderResourceView: _Callable[[ID3D10Resource,  # pResource
                                         _Pointer[_struct.D3D10_SHADER_RESOURCE_VIEW_DESC],  # pDesc
                                         _Pointer[ID3D10ShaderResourceView]],  # ppSRView
                                        _type.HRESULT]
    CreateRenderTargetView: _Callable[[ID3D10Resource,  # pResource
                                       _Pointer[_struct.D3D10_RENDER_TARGET_VIEW_DESC],  # pDesc
                                       _Pointer[ID3D10RenderTargetView]],  # ppRTView
                                      _type.HRESULT]
    CreateDepthStencilView: _Callable[[ID3D10Resource,  # pResource
                                       _Pointer[_struct.D3D10_DEPTH_STENCIL_VIEW_DESC],  # pDesc
                                       _Pointer[ID3D10DepthStencilView]],  # ppDepthStencilView
                                      _type.HRESULT]
    CreateInputLayout: _Callable[[_Pointer[_struct.D3D10_INPUT_ELEMENT_DESC],  # pInputElementDescs
                                  _type.UINT,  # NumElements
                                  _type.c_void_p,  # pShaderBytecodeWithInputSignature
                                  _type.SIZE_T,  # BytecodeLength
                                  _Pointer[ID3D10InputLayout]],  # ppInputLayout
                                 _type.HRESULT]
    CreateVertexShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                   _type.SIZE_T,  # BytecodeLength
                                   _Pointer[ID3D10VertexShader]],  # ppVertexShader
                                  _type.HRESULT]
    CreateGeometryShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                     _type.SIZE_T,  # BytecodeLength
                                     _Pointer[ID3D10GeometryShader]],  # ppGeometryShader
                                    _type.HRESULT]
    CreateGeometryShaderWithStreamOutput: _Callable[[_type.c_void_p,  # pShaderBytecode
                                                     _type.SIZE_T,  # BytecodeLength
                                                     _Pointer[_struct.D3D10_SO_DECLARATION_ENTRY],  # pSODeclaration
                                                     _type.UINT,  # NumEntries
                                                     _type.UINT,  # OutputStreamStride
                                                     _Pointer[ID3D10GeometryShader]],  # ppGeometryShader
                                                    _type.HRESULT]
    CreatePixelShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                  _type.SIZE_T,  # BytecodeLength
                                  _Pointer[ID3D10PixelShader]],  # ppPixelShader
                                 _type.HRESULT]
    CreateBlendState: _Callable[[_Pointer[_struct.D3D10_BLEND_DESC],  # pBlendStateDesc
                                 _Pointer[ID3D10BlendState]],  # ppBlendState
                                _type.HRESULT]
    CreateDepthStencilState: _Callable[[_Pointer[_struct.D3D10_DEPTH_STENCIL_DESC],  # pDepthStencilDesc
                                        _Pointer[ID3D10DepthStencilState]],  # ppDepthStencilState
                                       _type.HRESULT]
    CreateRasterizerState: _Callable[[_Pointer[_struct.D3D10_RASTERIZER_DESC],  # pRasterizerDesc
                                      _Pointer[ID3D10RasterizerState]],  # ppRasterizerState
                                     _type.HRESULT]
    CreateSamplerState: _Callable[[_Pointer[_struct.D3D10_SAMPLER_DESC],  # pSamplerDesc
                                   _Pointer[ID3D10SamplerState]],  # ppSamplerState
                                  _type.HRESULT]
    CreateQuery: _Callable[[_Pointer[_struct.D3D10_QUERY_DESC],  # pQueryDesc
                            _Pointer[ID3D10Query]],  # ppQuery
                           _type.HRESULT]
    CreatePredicate: _Callable[[_Pointer[_struct.D3D10_QUERY_DESC],  # pPredicateDesc
                                _Pointer[ID3D10Predicate]],  # ppPredicate
                               _type.HRESULT]
    CreateCounter: _Callable[[_Pointer[_struct.D3D10_COUNTER_DESC],  # pCounterDesc
                              _Pointer[ID3D10Counter]],  # ppCounter
                             _type.HRESULT]
    CheckFormatSupport: _Callable[[_enum.DXGI_FORMAT,  # Format
                                   _Pointer[_type.UINT]],  # pFormatSupport
                                  _type.HRESULT]
    CheckMultisampleQualityLevels: _Callable[[_enum.DXGI_FORMAT,  # Format
                                              _type.UINT,  # SampleCount
                                              _Pointer[_type.UINT]],  # pNumQualityLevels
                                             _type.HRESULT]
    CheckCounterInfo: _Callable[[_Pointer[_struct.D3D10_COUNTER_INFO]],  # pCounterInfo
                                _type.c_void]
    CheckCounter: _Callable[[_Pointer[_struct.D3D10_COUNTER_DESC],  # pDesc
                             _Pointer[_enum.D3D10_COUNTER_TYPE],  # pType
                             _Pointer[_type.UINT],  # pActiveCounters
                             _type.LPSTR,  # szName
                             _Pointer[_type.UINT],  # pNameLength
                             _type.LPSTR,  # szUnits
                             _Pointer[_type.UINT],  # pUnitsLength
                             _type.LPSTR,  # szDescription
                             _Pointer[_type.UINT]],  # pDescriptionLength
                            _type.HRESULT]
    GetCreationFlags: _Callable[[],
                                _type.UINT]
    OpenSharedResource: _Callable[[_type.HANDLE,  # hResource
                                   _Pointer[_struct.IID],  # ReturnedInterface
                                   _type.c_void_p],  # ppResource
                                  _type.HRESULT]
    SetTextFilterSize: _Callable[[_type.UINT,  # Width
                                  _type.UINT],  # Height
                                 _type.c_void]
    GetTextFilterSize: _Callable[[_Pointer[_type.UINT],  # pWidth
                                  _Pointer[_type.UINT]],  # pHeight
                                 _type.c_void]


class ID3D10Multithread(_Unknwnbase.IUnknown):
    Enter: _Callable[[],
                     _type.c_void]
    Leave: _Callable[[],
                     _type.c_void]
    SetMultithreadProtected: _Callable[[_type.BOOL],  # bMTProtect
                                       _type.BOOL]
    GetMultithreadProtected: _Callable[[],
                                       _type.BOOL]
