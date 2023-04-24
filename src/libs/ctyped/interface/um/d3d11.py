from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D11DeviceChild(_Unknwnbase.IUnknown):
    GetDevice: _Callable[[_Pointer[ID3D11Device]],  # ppDevice
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


class ID3D11DepthStencilState(ID3D11DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_DEPTH_STENCIL_DESC]],  # pDesc
                       _type.c_void]


class ID3D11BlendState(ID3D11DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_BLEND_DESC]],  # pDesc
                       _type.c_void]


class ID3D11RasterizerState(ID3D11DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_RASTERIZER_DESC]],  # pDesc
                       _type.c_void]


class ID3D11Resource(ID3D11DeviceChild):
    GetType: _Callable[[_Pointer[_enum.D3D11_RESOURCE_DIMENSION]],  # pResourceDimension
                       _type.c_void]
    SetEvictionPriority: _Callable[[_type.UINT],  # EvictionPriority
                                   _type.c_void]
    GetEvictionPriority: _Callable[[],
                                   _type.UINT]


class ID3D11Buffer(ID3D11Resource):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_BUFFER_DESC]],  # pDesc
                       _type.c_void]


class ID3D11Texture1D(ID3D11Resource):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_TEXTURE1D_DESC]],  # pDesc
                       _type.c_void]


class ID3D11Texture2D(ID3D11Resource):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_TEXTURE2D_DESC]],  # pDesc
                       _type.c_void]


class ID3D11Texture3D(ID3D11Resource):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_TEXTURE3D_DESC]],  # pDesc
                       _type.c_void]


class ID3D11View(ID3D11DeviceChild):
    GetResource: _Callable[[_Pointer[ID3D11Resource]],  # ppResource
                           _type.c_void]


class ID3D11ShaderResourceView(ID3D11View):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_SHADER_RESOURCE_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D11RenderTargetView(ID3D11View):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_RENDER_TARGET_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D11DepthStencilView(ID3D11View):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_DEPTH_STENCIL_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D11UnorderedAccessView(ID3D11View):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_UNORDERED_ACCESS_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D11VertexShader(ID3D11DeviceChild):
    pass


class ID3D11HullShader(ID3D11DeviceChild):
    pass


class ID3D11DomainShader(ID3D11DeviceChild):
    pass


class ID3D11GeometryShader(ID3D11DeviceChild):
    pass


class ID3D11PixelShader(ID3D11DeviceChild):
    pass


class ID3D11ComputeShader(ID3D11DeviceChild):
    pass


class ID3D11InputLayout(ID3D11DeviceChild):
    pass


class ID3D11SamplerState(ID3D11DeviceChild):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_SAMPLER_DESC]],  # pDesc
                       _type.c_void]


class ID3D11Asynchronous(ID3D11DeviceChild):
    GetDataSize: _Callable[[],
                           _type.UINT]


class ID3D11Query(ID3D11Asynchronous):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_QUERY_DESC]],  # pDesc
                       _type.c_void]


class ID3D11Predicate(ID3D11Query):
    pass


class ID3D11Counter(ID3D11Asynchronous):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_COUNTER_DESC]],  # pDesc
                       _type.c_void]


class ID3D11ClassInstance(ID3D11DeviceChild):
    GetClassLinkage: _Callable[[_Pointer[ID3D11ClassLinkage]],  # ppLinkage
                               _type.c_void]
    GetDesc: _Callable[[_Pointer[_struct.D3D11_CLASS_INSTANCE_DESC]],  # pDesc
                       _type.c_void]
    GetInstanceName: _Callable[[_type.LPSTR,  # pInstanceName
                                _Pointer[_type.SIZE_T]],  # pBufferLength
                               _type.c_void]
    GetTypeName: _Callable[[_type.LPSTR,  # pTypeName
                            _Pointer[_type.SIZE_T]],  # pBufferLength
                           _type.c_void]


class ID3D11ClassLinkage(ID3D11DeviceChild):
    GetClassInstance: _Callable[[_type.LPCSTR,  # pClassInstanceName
                                 _type.UINT,  # InstanceIndex
                                 _Pointer[ID3D11ClassInstance]],  # ppInstance
                                _type.HRESULT]
    CreateClassInstance: _Callable[[_type.LPCSTR,  # pClassTypeName
                                    _type.UINT,  # ConstantBufferOffset
                                    _type.UINT,  # ConstantVectorOffset
                                    _type.UINT,  # TextureOffset
                                    _type.UINT,  # SamplerOffset
                                    _Pointer[ID3D11ClassInstance]],  # ppInstance
                                   _type.HRESULT]


class ID3D11CommandList(ID3D11DeviceChild):
    GetContextFlags: _Callable[[],
                               _type.UINT]


class ID3D11DeviceContext(ID3D11DeviceChild):
    VSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    PSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    PSSetShader: _Callable[[ID3D11PixelShader,  # pPixelShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _type.UINT],  # NumClassInstances
                           _type.c_void]
    PSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    VSSetShader: _Callable[[ID3D11VertexShader,  # pVertexShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _type.UINT],  # NumClassInstances
                           _type.c_void]
    DrawIndexed: _Callable[[_type.UINT,  # IndexCount
                            _type.UINT,  # StartIndexLocation
                            _type.INT],  # BaseVertexLocation
                           _type.c_void]
    Draw: _Callable[[_type.UINT,  # VertexCount
                     _type.UINT],  # StartVertexLocation
                    _type.c_void]
    Map: _Callable[[ID3D11Resource,  # pResource
                    _type.UINT,  # Subresource
                    _enum.D3D11_MAP,  # MapType
                    _type.UINT,  # MapFlags
                    _Pointer[_struct.D3D11_MAPPED_SUBRESOURCE]],  # pMappedResource
                   _type.HRESULT]
    Unmap: _Callable[[ID3D11Resource,  # pResource
                      _type.UINT],  # Subresource
                     _type.c_void]
    PSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    IASetInputLayout: _Callable[[ID3D11InputLayout],  # pInputLayout
                                _type.c_void]
    IASetVertexBuffers: _Callable[[_type.UINT,  # StartSlot
                                   _type.UINT,  # NumBuffers
                                   _Pointer[ID3D11Buffer],  # ppVertexBuffers
                                   _Pointer[_type.UINT],  # pStrides
                                   _Pointer[_type.UINT]],  # pOffsets
                                  _type.c_void]
    IASetIndexBuffer: _Callable[[ID3D11Buffer,  # pIndexBuffer
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
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    GSSetShader: _Callable[[ID3D11GeometryShader,  # pShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _type.UINT],  # NumClassInstances
                           _type.c_void]
    IASetPrimitiveTopology: _Callable[[_enum.D3D11_PRIMITIVE_TOPOLOGY],  # Topology
                                      _type.c_void]
    VSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    VSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    Begin: _Callable[[ID3D11Asynchronous],  # pAsync
                     _type.c_void]
    End: _Callable[[ID3D11Asynchronous],  # pAsync
                   _type.c_void]
    GetData: _Callable[[ID3D11Asynchronous,  # pAsync
                        _type.c_void_p,  # pData
                        _type.UINT,  # DataSize
                        _type.UINT],  # GetDataFlags
                       _type.HRESULT]
    SetPredication: _Callable[[ID3D11Predicate,  # pPredicate
                               _type.BOOL],  # PredicateValue
                              _type.c_void]
    GSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    GSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    OMSetRenderTargets: _Callable[[_type.UINT,  # NumViews
                                   _Pointer[ID3D11RenderTargetView],  # ppRenderTargetViews
                                   ID3D11DepthStencilView],  # pDepthStencilView
                                  _type.c_void]
    OMSetRenderTargetsAndUnorderedAccessViews: _Callable[[_type.UINT,  # NumRTVs
                                                          _Pointer[ID3D11RenderTargetView],  # ppRenderTargetViews
                                                          ID3D11DepthStencilView,  # pDepthStencilView
                                                          _type.UINT,  # UAVStartSlot
                                                          _type.UINT,  # NumUAVs
                                                          _Pointer[ID3D11UnorderedAccessView],  # ppUnorderedAccessViews
                                                          _Pointer[_type.UINT]],  # pUAVInitialCounts
                                                         _type.c_void]
    OMSetBlendState: _Callable[[ID3D11BlendState,  # pBlendState
                                _Pointer[_type.FLOAT],  # BlendFactor
                                _type.UINT],  # SampleMask
                               _type.c_void]
    OMSetDepthStencilState: _Callable[[ID3D11DepthStencilState,  # pDepthStencilState
                                       _type.UINT],  # StencilRef
                                      _type.c_void]
    SOSetTargets: _Callable[[_type.UINT,  # NumBuffers
                             _Pointer[ID3D11Buffer],  # ppSOTargets
                             _Pointer[_type.UINT]],  # pOffsets
                            _type.c_void]
    DrawAuto: _Callable[[],
                        _type.c_void]
    DrawIndexedInstancedIndirect: _Callable[[ID3D11Buffer,  # pBufferForArgs
                                             _type.UINT],  # AlignedByteOffsetForArgs
                                            _type.c_void]
    DrawInstancedIndirect: _Callable[[ID3D11Buffer,  # pBufferForArgs
                                      _type.UINT],  # AlignedByteOffsetForArgs
                                     _type.c_void]
    Dispatch: _Callable[[_type.UINT,  # ThreadGroupCountX
                         _type.UINT,  # ThreadGroupCountY
                         _type.UINT],  # ThreadGroupCountZ
                        _type.c_void]
    DispatchIndirect: _Callable[[ID3D11Buffer,  # pBufferForArgs
                                 _type.UINT],  # AlignedByteOffsetForArgs
                                _type.c_void]
    RSSetState: _Callable[[ID3D11RasterizerState],  # pRasterizerState
                          _type.c_void]
    RSSetViewports: _Callable[[_type.UINT,  # NumViewports
                               _Pointer[_struct.D3D11_VIEWPORT]],  # pViewports
                              _type.c_void]
    RSSetScissorRects: _Callable[[_type.UINT,  # NumRects
                                  _Pointer[_struct.D3D11_RECT]],  # pRects
                                 _type.c_void]
    CopySubresourceRegion: _Callable[[ID3D11Resource,  # pDstResource
                                      _type.UINT,  # DstSubresource
                                      _type.UINT,  # DstX
                                      _type.UINT,  # DstY
                                      _type.UINT,  # DstZ
                                      ID3D11Resource,  # pSrcResource
                                      _type.UINT,  # SrcSubresource
                                      _Pointer[_struct.D3D11_BOX]],  # pSrcBox
                                     _type.c_void]
    CopyResource: _Callable[[ID3D11Resource,  # pDstResource
                             ID3D11Resource],  # pSrcResource
                            _type.c_void]
    UpdateSubresource: _Callable[[ID3D11Resource,  # pDstResource
                                  _type.UINT,  # DstSubresource
                                  _Pointer[_struct.D3D11_BOX],  # pDstBox
                                  _type.c_void_p,  # pSrcData
                                  _type.UINT,  # SrcRowPitch
                                  _type.UINT],  # SrcDepthPitch
                                 _type.c_void]
    CopyStructureCount: _Callable[[ID3D11Buffer,  # pDstBuffer
                                   _type.UINT,  # DstAlignedByteOffset
                                   ID3D11UnorderedAccessView],  # pSrcView
                                  _type.c_void]
    ClearRenderTargetView: _Callable[[ID3D11RenderTargetView,  # pRenderTargetView
                                      _Pointer[_type.FLOAT]],  # ColorRGBA
                                     _type.c_void]
    ClearUnorderedAccessViewUint: _Callable[[ID3D11UnorderedAccessView,  # pUnorderedAccessView
                                             _Pointer[_type.UINT]],  # Values
                                            _type.c_void]
    ClearUnorderedAccessViewFloat: _Callable[[ID3D11UnorderedAccessView,  # pUnorderedAccessView
                                              _Pointer[_type.FLOAT]],  # Values
                                             _type.c_void]
    ClearDepthStencilView: _Callable[[ID3D11DepthStencilView,  # pDepthStencilView
                                      _type.UINT,  # ClearFlags
                                      _type.FLOAT,  # Depth
                                      _type.UINT8],  # Stencil
                                     _type.c_void]
    GenerateMips: _Callable[[ID3D11ShaderResourceView],  # pShaderResourceView
                            _type.c_void]
    SetResourceMinLOD: _Callable[[ID3D11Resource,  # pResource
                                  _type.FLOAT],  # MinLOD
                                 _type.c_void]
    GetResourceMinLOD: _Callable[[ID3D11Resource],  # pResource
                                 _type.FLOAT]
    ResolveSubresource: _Callable[[ID3D11Resource,  # pDstResource
                                   _type.UINT,  # DstSubresource
                                   ID3D11Resource,  # pSrcResource
                                   _type.UINT,  # SrcSubresource
                                   _enum.DXGI_FORMAT],  # Format
                                  _type.c_void]
    ExecuteCommandList: _Callable[[ID3D11CommandList,  # pCommandList
                                   _type.BOOL],  # RestoreContextState
                                  _type.c_void]
    HSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    HSSetShader: _Callable[[ID3D11HullShader,  # pHullShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _type.UINT],  # NumClassInstances
                           _type.c_void]
    HSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    HSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    DSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    DSSetShader: _Callable[[ID3D11DomainShader,  # pDomainShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _type.UINT],  # NumClassInstances
                           _type.c_void]
    DSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    DSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    CSSetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    CSSetUnorderedAccessViews: _Callable[[_type.UINT,  # StartSlot
                                          _type.UINT,  # NumUAVs
                                          _Pointer[ID3D11UnorderedAccessView],  # ppUnorderedAccessViews
                                          _Pointer[_type.UINT]],  # pUAVInitialCounts
                                         _type.c_void]
    CSSetShader: _Callable[[ID3D11ComputeShader,  # pComputeShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _type.UINT],  # NumClassInstances
                           _type.c_void]
    CSSetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    CSSetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    VSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    PSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    PSGetShader: _Callable[[_Pointer[ID3D11PixelShader],  # ppPixelShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _Pointer[_type.UINT]],  # pNumClassInstances
                           _type.c_void]
    PSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    VSGetShader: _Callable[[_Pointer[ID3D11VertexShader],  # ppVertexShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _Pointer[_type.UINT]],  # pNumClassInstances
                           _type.c_void]
    PSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    IAGetInputLayout: _Callable[[_Pointer[ID3D11InputLayout]],  # ppInputLayout
                                _type.c_void]
    IAGetVertexBuffers: _Callable[[_type.UINT,  # StartSlot
                                   _type.UINT,  # NumBuffers
                                   _Pointer[ID3D11Buffer],  # ppVertexBuffers
                                   _Pointer[_type.UINT],  # pStrides
                                   _Pointer[_type.UINT]],  # pOffsets
                                  _type.c_void]
    IAGetIndexBuffer: _Callable[[_Pointer[ID3D11Buffer],  # pIndexBuffer
                                 _Pointer[_enum.DXGI_FORMAT],  # Format
                                 _Pointer[_type.UINT]],  # Offset
                                _type.c_void]
    GSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    GSGetShader: _Callable[[_Pointer[ID3D11GeometryShader],  # ppGeometryShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _Pointer[_type.UINT]],  # pNumClassInstances
                           _type.c_void]
    IAGetPrimitiveTopology: _Callable[[_Pointer[_enum.D3D11_PRIMITIVE_TOPOLOGY]],  # pTopology
                                      _type.c_void]
    VSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    VSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    GetPredication: _Callable[[_Pointer[ID3D11Predicate],  # ppPredicate
                               _Pointer[_type.BOOL]],  # pPredicateValue
                              _type.c_void]
    GSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    GSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    OMGetRenderTargets: _Callable[[_type.UINT,  # NumViews
                                   _Pointer[ID3D11RenderTargetView],  # ppRenderTargetViews
                                   _Pointer[ID3D11DepthStencilView]],  # ppDepthStencilView
                                  _type.c_void]
    OMGetRenderTargetsAndUnorderedAccessViews: _Callable[[_type.UINT,  # NumRTVs
                                                          _Pointer[ID3D11RenderTargetView],  # ppRenderTargetViews
                                                          _Pointer[ID3D11DepthStencilView],  # ppDepthStencilView
                                                          _type.UINT,  # UAVStartSlot
                                                          _type.UINT,  # NumUAVs
                                                          _Pointer[ID3D11UnorderedAccessView]],  # ppUnorderedAccessViews
                                                         _type.c_void]
    OMGetBlendState: _Callable[[_Pointer[ID3D11BlendState],  # ppBlendState
                                _Pointer[_type.FLOAT],  # BlendFactor
                                _Pointer[_type.UINT]],  # pSampleMask
                               _type.c_void]
    OMGetDepthStencilState: _Callable[[_Pointer[ID3D11DepthStencilState],  # ppDepthStencilState
                                       _Pointer[_type.UINT]],  # pStencilRef
                                      _type.c_void]
    SOGetTargets: _Callable[[_type.UINT,  # NumBuffers
                             _Pointer[ID3D11Buffer]],  # ppSOTargets
                            _type.c_void]
    RSGetState: _Callable[[_Pointer[ID3D11RasterizerState]],  # ppRasterizerState
                          _type.c_void]
    RSGetViewports: _Callable[[_Pointer[_type.UINT],  # pNumViewports
                               _Pointer[_struct.D3D11_VIEWPORT]],  # pViewports
                              _type.c_void]
    RSGetScissorRects: _Callable[[_Pointer[_type.UINT],  # pNumRects
                                  _Pointer[_struct.D3D11_RECT]],  # pRects
                                 _type.c_void]
    HSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    HSGetShader: _Callable[[_Pointer[ID3D11HullShader],  # ppHullShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _Pointer[_type.UINT]],  # pNumClassInstances
                           _type.c_void]
    HSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    HSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    DSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    DSGetShader: _Callable[[_Pointer[ID3D11DomainShader],  # ppDomainShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _Pointer[_type.UINT]],  # pNumClassInstances
                           _type.c_void]
    DSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    DSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    CSGetShaderResources: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumViews
                                     _Pointer[ID3D11ShaderResourceView]],  # ppShaderResourceViews
                                    _type.c_void]
    CSGetUnorderedAccessViews: _Callable[[_type.UINT,  # StartSlot
                                          _type.UINT,  # NumUAVs
                                          _Pointer[ID3D11UnorderedAccessView]],  # ppUnorderedAccessViews
                                         _type.c_void]
    CSGetShader: _Callable[[_Pointer[ID3D11ComputeShader],  # ppComputeShader
                            _Pointer[ID3D11ClassInstance],  # ppClassInstances
                            _Pointer[_type.UINT]],  # pNumClassInstances
                           _type.c_void]
    CSGetSamplers: _Callable[[_type.UINT,  # StartSlot
                              _type.UINT,  # NumSamplers
                              _Pointer[ID3D11SamplerState]],  # ppSamplers
                             _type.c_void]
    CSGetConstantBuffers: _Callable[[_type.UINT,  # StartSlot
                                     _type.UINT,  # NumBuffers
                                     _Pointer[ID3D11Buffer]],  # ppConstantBuffers
                                    _type.c_void]
    ClearState: _Callable[[],
                          _type.c_void]
    Flush: _Callable[[],
                     _type.c_void]
    GetType: _Callable[[],
                       _enum.D3D11_DEVICE_CONTEXT_TYPE]
    GetContextFlags: _Callable[[],
                               _type.UINT]
    FinishCommandList: _Callable[[_type.BOOL,  # RestoreDeferredContextState
                                  _Pointer[ID3D11CommandList]],  # ppCommandList
                                 _type.HRESULT]


class ID3D11VideoDecoder(ID3D11DeviceChild):
    GetCreationParameters: _Callable[[_Pointer[_struct.D3D11_VIDEO_DECODER_DESC],  # pVideoDesc
                                      _Pointer[_struct.D3D11_VIDEO_DECODER_CONFIG]],  # pConfig
                                     _type.HRESULT]
    GetDriverHandle: _Callable[[_Pointer[_type.HANDLE]],  # pDriverHandle
                               _type.HRESULT]


class ID3D11VideoProcessorEnumerator(ID3D11DeviceChild):
    GetVideoProcessorContentDesc: _Callable[[_Pointer[_struct.D3D11_VIDEO_PROCESSOR_CONTENT_DESC]],  # pContentDesc
                                            _type.HRESULT]
    CheckVideoProcessorFormat: _Callable[[_enum.DXGI_FORMAT,  # Format
                                          _Pointer[_type.UINT]],  # pFlags
                                         _type.HRESULT]
    GetVideoProcessorCaps: _Callable[[_Pointer[_struct.D3D11_VIDEO_PROCESSOR_CAPS]],  # pCaps
                                     _type.HRESULT]
    GetVideoProcessorRateConversionCaps: _Callable[[_type.UINT,  # TypeIndex
                                                    _Pointer[_struct.D3D11_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS]],  # pCaps
                                                   _type.HRESULT]
    GetVideoProcessorCustomRate: _Callable[[_type.UINT,  # TypeIndex
                                            _type.UINT,  # CustomRateIndex
                                            _Pointer[_struct.D3D11_VIDEO_PROCESSOR_CUSTOM_RATE]],  # pRate
                                           _type.HRESULT]
    GetVideoProcessorFilterRange: _Callable[[_enum.D3D11_VIDEO_PROCESSOR_FILTER,  # Filter
                                             _Pointer[_struct.D3D11_VIDEO_PROCESSOR_FILTER_RANGE]],  # pRange
                                            _type.HRESULT]


class ID3D11VideoProcessor(ID3D11DeviceChild):
    GetContentDesc: _Callable[[_Pointer[_struct.D3D11_VIDEO_PROCESSOR_CONTENT_DESC]],  # pDesc
                              _type.c_void]
    GetRateConversionCaps: _Callable[[_Pointer[_struct.D3D11_VIDEO_PROCESSOR_RATE_CONVERSION_CAPS]],  # pCaps
                                     _type.c_void]


class ID3D11AuthenticatedChannel(ID3D11DeviceChild):
    GetCertificateSize: _Callable[[_Pointer[_type.UINT]],  # pCertificateSize
                                  _type.HRESULT]
    GetCertificate: _Callable[[_type.UINT,  # CertificateSize
                               _Pointer[_type.BYTE]],  # pCertificate
                              _type.HRESULT]
    GetChannelHandle: _Callable[[_Pointer[_type.HANDLE]],  # pChannelHandle
                                _type.c_void]


class ID3D11CryptoSession(ID3D11DeviceChild):
    GetCryptoType: _Callable[[_Pointer[_struct.GUID]],  # pCryptoType
                             _type.c_void]
    GetDecoderProfile: _Callable[[_Pointer[_struct.GUID]],  # pDecoderProfile
                                 _type.c_void]
    GetCertificateSize: _Callable[[_Pointer[_type.UINT]],  # pCertificateSize
                                  _type.HRESULT]
    GetCertificate: _Callable[[_type.UINT,  # CertificateSize
                               _Pointer[_type.BYTE]],  # pCertificate
                              _type.HRESULT]
    GetCryptoSessionHandle: _Callable[[_Pointer[_type.HANDLE]],  # pCryptoSessionHandle
                                      _type.c_void]


class ID3D11VideoDecoderOutputView(ID3D11View):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D11VideoProcessorInputView(ID3D11View):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D11VideoProcessorOutputView(ID3D11View):
    GetDesc: _Callable[[_Pointer[_struct.D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC]],  # pDesc
                       _type.c_void]


class ID3D11VideoContext(ID3D11DeviceChild):
    GetDecoderBuffer: _Callable[[ID3D11VideoDecoder,  # pDecoder
                                 _enum.D3D11_VIDEO_DECODER_BUFFER_TYPE,  # Type
                                 _Pointer[_type.UINT],  # pBufferSize
                                 _type.c_void_p],  # ppBuffer
                                _type.HRESULT]
    ReleaseDecoderBuffer: _Callable[[ID3D11VideoDecoder,  # pDecoder
                                     _enum.D3D11_VIDEO_DECODER_BUFFER_TYPE],  # Type
                                    _type.HRESULT]
    DecoderBeginFrame: _Callable[[ID3D11VideoDecoder,  # pDecoder
                                  ID3D11VideoDecoderOutputView,  # pView
                                  _type.UINT,  # ContentKeySize
                                  _type.c_void_p],  # pContentKey
                                 _type.HRESULT]
    DecoderEndFrame: _Callable[[ID3D11VideoDecoder],  # pDecoder
                               _type.HRESULT]
    SubmitDecoderBuffers: _Callable[[ID3D11VideoDecoder,  # pDecoder
                                     _type.UINT,  # NumBuffers
                                     _Pointer[_struct.D3D11_VIDEO_DECODER_BUFFER_DESC]],  # pBufferDesc
                                    _type.HRESULT]
    DecoderExtension: _Callable[[ID3D11VideoDecoder,  # pDecoder
                                 _Pointer[_struct.D3D11_VIDEO_DECODER_EXTENSION]],  # pExtensionData
                                _type.APP_DEPRECATED_HRESULT]
    VideoProcessorSetOutputTargetRect: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.BOOL,  # Enable
                                                  _Pointer[_struct.RECT]],  # pRect
                                                 _type.c_void]
    VideoProcessorSetOutputBackgroundColor: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                       _type.BOOL,  # YCbCr
                                                       _Pointer[_struct.D3D11_VIDEO_COLOR]],  # pColor
                                                      _type.c_void]
    VideoProcessorSetOutputColorSpace: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _Pointer[_struct.D3D11_VIDEO_PROCESSOR_COLOR_SPACE]],  # pColorSpace
                                                 _type.c_void]
    VideoProcessorSetOutputAlphaFillMode: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                     _enum.D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE,  # AlphaFillMode
                                                     _type.UINT],  # StreamIndex
                                                    _type.c_void]
    VideoProcessorSetOutputConstriction: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                    _type.BOOL,  # Enable
                                                    _struct.SIZE],  # Size
                                                   _type.c_void]
    VideoProcessorSetOutputStereoMode: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.BOOL],  # Enable
                                                 _type.c_void]
    VideoProcessorSetOutputExtension: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                 _Pointer[_struct.GUID],  # pExtensionGuid
                                                 _type.UINT,  # DataSize
                                                 _type.c_void_p],  # pData
                                                _type.APP_DEPRECATED_HRESULT]
    VideoProcessorGetOutputTargetRect: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _Pointer[_type.BOOL],  # Enabled
                                                  _Pointer[_struct.RECT]],  # pRect
                                                 _type.c_void]
    VideoProcessorGetOutputBackgroundColor: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                       _Pointer[_type.BOOL],  # pYCbCr
                                                       _Pointer[_struct.D3D11_VIDEO_COLOR]],  # pColor
                                                      _type.c_void]
    VideoProcessorGetOutputColorSpace: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _Pointer[_struct.D3D11_VIDEO_PROCESSOR_COLOR_SPACE]],  # pColorSpace
                                                 _type.c_void]
    VideoProcessorGetOutputAlphaFillMode: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                     _Pointer[_enum.D3D11_VIDEO_PROCESSOR_ALPHA_FILL_MODE],  # pAlphaFillMode
                                                     _Pointer[_type.UINT]],  # pStreamIndex
                                                    _type.c_void]
    VideoProcessorGetOutputConstriction: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                    _Pointer[_type.BOOL],  # pEnabled
                                                    _Pointer[_struct.SIZE]],  # pSize
                                                   _type.c_void]
    VideoProcessorGetOutputStereoMode: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _Pointer[_type.BOOL]],  # pEnabled
                                                 _type.c_void]
    VideoProcessorGetOutputExtension: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                 _Pointer[_struct.GUID],  # pExtensionGuid
                                                 _type.UINT,  # DataSize
                                                 _type.c_void_p],  # pData
                                                _type.APP_DEPRECATED_HRESULT]
    VideoProcessorSetStreamFrameFormat: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                   _type.UINT,  # StreamIndex
                                                   _enum.D3D11_VIDEO_FRAME_FORMAT],  # FrameFormat
                                                  _type.c_void]
    VideoProcessorSetStreamColorSpace: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.UINT,  # StreamIndex
                                                  _Pointer[_struct.D3D11_VIDEO_PROCESSOR_COLOR_SPACE]],  # pColorSpace
                                                 _type.c_void]
    VideoProcessorSetStreamOutputRate: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.UINT,  # StreamIndex
                                                  _enum.D3D11_VIDEO_PROCESSOR_OUTPUT_RATE,  # OutputRate
                                                  _type.BOOL,  # RepeatFrame
                                                  _Pointer[_struct.DXGI_RATIONAL]],  # pCustomRate
                                                 _type.c_void]
    VideoProcessorSetStreamSourceRect: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.UINT,  # StreamIndex
                                                  _type.BOOL,  # Enable
                                                  _Pointer[_struct.RECT]],  # pRect
                                                 _type.c_void]
    VideoProcessorSetStreamDestRect: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                _type.UINT,  # StreamIndex
                                                _type.BOOL,  # Enable
                                                _Pointer[_struct.RECT]],  # pRect
                                               _type.c_void]
    VideoProcessorSetStreamAlpha: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                             _type.UINT,  # StreamIndex
                                             _type.BOOL,  # Enable
                                             _type.FLOAT],  # Alpha
                                            _type.c_void]
    VideoProcessorSetStreamPalette: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                               _type.UINT,  # StreamIndex
                                               _type.UINT,  # Count
                                               _Pointer[_type.UINT]],  # pEntries
                                              _type.c_void]
    VideoProcessorSetStreamPixelAspectRatio: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                        _type.UINT,  # StreamIndex
                                                        _type.BOOL,  # Enable
                                                        _Pointer[_struct.DXGI_RATIONAL],  # pSourceAspectRatio
                                                        _Pointer[_struct.DXGI_RATIONAL]],  # pDestinationAspectRatio
                                                       _type.c_void]
    VideoProcessorSetStreamLumaKey: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                               _type.UINT,  # StreamIndex
                                               _type.BOOL,  # Enable
                                               _type.FLOAT,  # Lower
                                               _type.FLOAT],  # Upper
                                              _type.c_void]
    VideoProcessorSetStreamStereoFormat: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                    _type.UINT,  # StreamIndex
                                                    _type.BOOL,  # Enable
                                                    _enum.D3D11_VIDEO_PROCESSOR_STEREO_FORMAT,  # Format
                                                    _type.BOOL,  # LeftViewFrame0
                                                    _type.BOOL,  # BaseViewFrame0
                                                    _enum.D3D11_VIDEO_PROCESSOR_STEREO_FLIP_MODE,  # FlipMode
                                                    _type.c_int],  # MonoOffset
                                                   _type.c_void]
    VideoProcessorSetStreamAutoProcessingMode: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                          _type.UINT,  # StreamIndex
                                                          _type.BOOL],  # Enable
                                                         _type.c_void]
    VideoProcessorSetStreamFilter: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                              _type.UINT,  # StreamIndex
                                              _enum.D3D11_VIDEO_PROCESSOR_FILTER,  # Filter
                                              _type.BOOL,  # Enable
                                              _type.c_int],  # Level
                                             _type.c_void]
    VideoProcessorSetStreamExtension: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                 _type.UINT,  # StreamIndex
                                                 _Pointer[_struct.GUID],  # pExtensionGuid
                                                 _type.UINT,  # DataSize
                                                 _type.c_void_p],  # pData
                                                _type.APP_DEPRECATED_HRESULT]
    VideoProcessorGetStreamFrameFormat: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                   _type.UINT,  # StreamIndex
                                                   _Pointer[_enum.D3D11_VIDEO_FRAME_FORMAT]],  # pFrameFormat
                                                  _type.c_void]
    VideoProcessorGetStreamColorSpace: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.UINT,  # StreamIndex
                                                  _Pointer[_struct.D3D11_VIDEO_PROCESSOR_COLOR_SPACE]],  # pColorSpace
                                                 _type.c_void]
    VideoProcessorGetStreamOutputRate: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.UINT,  # StreamIndex
                                                  _Pointer[_enum.D3D11_VIDEO_PROCESSOR_OUTPUT_RATE],  # pOutputRate
                                                  _Pointer[_type.BOOL],  # pRepeatFrame
                                                  _Pointer[_struct.DXGI_RATIONAL]],  # pCustomRate
                                                 _type.c_void]
    VideoProcessorGetStreamSourceRect: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                  _type.UINT,  # StreamIndex
                                                  _Pointer[_type.BOOL],  # pEnabled
                                                  _Pointer[_struct.RECT]],  # pRect
                                                 _type.c_void]
    VideoProcessorGetStreamDestRect: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                _type.UINT,  # StreamIndex
                                                _Pointer[_type.BOOL],  # pEnabled
                                                _Pointer[_struct.RECT]],  # pRect
                                               _type.c_void]
    VideoProcessorGetStreamAlpha: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                             _type.UINT,  # StreamIndex
                                             _Pointer[_type.BOOL],  # pEnabled
                                             _Pointer[_type.FLOAT]],  # pAlpha
                                            _type.c_void]
    VideoProcessorGetStreamPalette: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                               _type.UINT,  # StreamIndex
                                               _type.UINT,  # Count
                                               _Pointer[_type.UINT]],  # pEntries
                                              _type.c_void]
    VideoProcessorGetStreamPixelAspectRatio: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                        _type.UINT,  # StreamIndex
                                                        _Pointer[_type.BOOL],  # pEnabled
                                                        _Pointer[_struct.DXGI_RATIONAL],  # pSourceAspectRatio
                                                        _Pointer[_struct.DXGI_RATIONAL]],  # pDestinationAspectRatio
                                                       _type.c_void]
    VideoProcessorGetStreamLumaKey: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                               _type.UINT,  # StreamIndex
                                               _Pointer[_type.BOOL],  # pEnabled
                                               _Pointer[_type.FLOAT],  # pLower
                                               _Pointer[_type.FLOAT]],  # pUpper
                                              _type.c_void]
    VideoProcessorGetStreamStereoFormat: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                    _type.UINT,  # StreamIndex
                                                    _Pointer[_type.BOOL],  # pEnable
                                                    _Pointer[_enum.D3D11_VIDEO_PROCESSOR_STEREO_FORMAT],  # pFormat
                                                    _Pointer[_type.BOOL],  # pLeftViewFrame0
                                                    _Pointer[_type.BOOL],  # pBaseViewFrame0
                                                    _Pointer[_enum.D3D11_VIDEO_PROCESSOR_STEREO_FLIP_MODE],  # pFlipMode
                                                    _Pointer[_type.c_int]],  # MonoOffset
                                                   _type.c_void]
    VideoProcessorGetStreamAutoProcessingMode: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                          _type.UINT,  # StreamIndex
                                                          _Pointer[_type.BOOL]],  # pEnabled
                                                         _type.c_void]
    VideoProcessorGetStreamFilter: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                              _type.UINT,  # StreamIndex
                                              _enum.D3D11_VIDEO_PROCESSOR_FILTER,  # Filter
                                              _Pointer[_type.BOOL],  # pEnabled
                                              _Pointer[_type.c_int]],  # pLevel
                                             _type.c_void]
    VideoProcessorGetStreamExtension: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                 _type.UINT,  # StreamIndex
                                                 _Pointer[_struct.GUID],  # pExtensionGuid
                                                 _type.UINT,  # DataSize
                                                 _type.c_void_p],  # pData
                                                _type.APP_DEPRECATED_HRESULT]
    VideoProcessorBlt: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                  ID3D11VideoProcessorOutputView,  # pView
                                  _type.UINT,  # OutputFrame
                                  _type.UINT,  # StreamCount
                                  _Pointer[_struct.D3D11_VIDEO_PROCESSOR_STREAM]],  # pStreams
                                 _type.HRESULT]
    NegotiateCryptoSessionKeyExchange: _Callable[[ID3D11CryptoSession,  # pCryptoSession
                                                  _type.UINT,  # DataSize
                                                  _type.c_void_p],  # pData
                                                 _type.HRESULT]
    EncryptionBlt: _Callable[[ID3D11CryptoSession,  # pCryptoSession
                              ID3D11Texture2D,  # pSrcSurface
                              ID3D11Texture2D,  # pDstSurface
                              _type.UINT,  # IVSize
                              _type.c_void_p],  # pIV
                             _type.c_void]
    DecryptionBlt: _Callable[[ID3D11CryptoSession,  # pCryptoSession
                              ID3D11Texture2D,  # pSrcSurface
                              ID3D11Texture2D,  # pDstSurface
                              _Pointer[_struct.D3D11_ENCRYPTED_BLOCK_INFO],  # pEncryptedBlockInfo
                              _type.UINT,  # ContentKeySize
                              _type.c_void_p,  # pContentKey
                              _type.UINT,  # IVSize
                              _type.c_void_p],  # pIV
                             _type.c_void]
    StartSessionKeyRefresh: _Callable[[ID3D11CryptoSession,  # pCryptoSession
                                       _type.UINT,  # RandomNumberSize
                                       _type.c_void_p],  # pRandomNumber
                                      _type.c_void]
    FinishSessionKeyRefresh: _Callable[[ID3D11CryptoSession],  # pCryptoSession
                                       _type.c_void]
    GetEncryptionBltKey: _Callable[[ID3D11CryptoSession,  # pCryptoSession
                                    _type.UINT,  # KeySize
                                    _type.c_void_p],  # pReadbackKey
                                   _type.HRESULT]
    NegotiateAuthenticatedChannelKeyExchange: _Callable[[ID3D11AuthenticatedChannel,  # pChannel
                                                         _type.UINT,  # DataSize
                                                         _type.c_void_p],  # pData
                                                        _type.HRESULT]
    QueryAuthenticatedChannel: _Callable[[ID3D11AuthenticatedChannel,  # pChannel
                                          _type.UINT,  # InputSize
                                          _type.c_void_p,  # pInput
                                          _type.UINT,  # OutputSize
                                          _type.c_void_p],  # pOutput
                                         _type.HRESULT]
    ConfigureAuthenticatedChannel: _Callable[[ID3D11AuthenticatedChannel,  # pChannel
                                              _type.UINT,  # InputSize
                                              _type.c_void_p,  # pInput
                                              _Pointer[_struct.D3D11_AUTHENTICATED_CONFIGURE_OUTPUT]],  # pOutput
                                             _type.HRESULT]
    VideoProcessorSetStreamRotation: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                _type.UINT,  # StreamIndex
                                                _type.BOOL,  # Enable
                                                _enum.D3D11_VIDEO_PROCESSOR_ROTATION],  # Rotation
                                               _type.c_void]
    VideoProcessorGetStreamRotation: _Callable[[ID3D11VideoProcessor,  # pVideoProcessor
                                                _type.UINT,  # StreamIndex
                                                _Pointer[_type.BOOL],  # pEnable
                                                _Pointer[_enum.D3D11_VIDEO_PROCESSOR_ROTATION]],  # pRotation
                                               _type.c_void]


class ID3D11VideoDevice(_Unknwnbase.IUnknown):
    CreateVideoDecoder: _Callable[[_Pointer[_struct.D3D11_VIDEO_DECODER_DESC],  # pVideoDesc
                                   _Pointer[_struct.D3D11_VIDEO_DECODER_CONFIG],  # pConfig
                                   _Pointer[ID3D11VideoDecoder]],  # ppDecoder
                                  _type.HRESULT]
    CreateVideoProcessor: _Callable[[ID3D11VideoProcessorEnumerator,  # pEnum
                                     _type.UINT,  # RateConversionIndex
                                     _Pointer[ID3D11VideoProcessor]],  # ppVideoProcessor
                                    _type.HRESULT]
    CreateAuthenticatedChannel: _Callable[[_enum.D3D11_AUTHENTICATED_CHANNEL_TYPE,  # ChannelType
                                           _Pointer[ID3D11AuthenticatedChannel]],  # ppAuthenticatedChannel
                                          _type.HRESULT]
    CreateCryptoSession: _Callable[[_Pointer[_struct.GUID],  # pCryptoType
                                    _Pointer[_struct.GUID],  # pDecoderProfile
                                    _Pointer[_struct.GUID],  # pKeyExchangeType
                                    _Pointer[ID3D11CryptoSession]],  # ppCryptoSession
                                   _type.HRESULT]
    CreateVideoDecoderOutputView: _Callable[[ID3D11Resource,  # pResource
                                             _Pointer[_struct.D3D11_VIDEO_DECODER_OUTPUT_VIEW_DESC],  # pDesc
                                             _Pointer[ID3D11VideoDecoderOutputView]],  # ppVDOVView
                                            _type.HRESULT]
    CreateVideoProcessorInputView: _Callable[[ID3D11Resource,  # pResource
                                              ID3D11VideoProcessorEnumerator,  # pEnum
                                              _Pointer[_struct.D3D11_VIDEO_PROCESSOR_INPUT_VIEW_DESC],  # pDesc
                                              _Pointer[ID3D11VideoProcessorInputView]],  # ppVPIView
                                             _type.HRESULT]
    CreateVideoProcessorOutputView: _Callable[[ID3D11Resource,  # pResource
                                               ID3D11VideoProcessorEnumerator,  # pEnum
                                               _Pointer[_struct.D3D11_VIDEO_PROCESSOR_OUTPUT_VIEW_DESC],  # pDesc
                                               _Pointer[ID3D11VideoProcessorOutputView]],  # ppVPOView
                                              _type.HRESULT]
    CreateVideoProcessorEnumerator: _Callable[[_Pointer[_struct.D3D11_VIDEO_PROCESSOR_CONTENT_DESC],  # pDesc
                                               _Pointer[ID3D11VideoProcessorEnumerator]],  # ppEnum
                                              _type.HRESULT]
    GetVideoDecoderProfileCount: _Callable[[],
                                           _type.UINT]
    GetVideoDecoderProfile: _Callable[[_type.UINT,  # Index
                                       _Pointer[_struct.GUID]],  # pDecoderProfile
                                      _type.HRESULT]
    CheckVideoDecoderFormat: _Callable[[_Pointer[_struct.GUID],  # pDecoderProfile
                                        _enum.DXGI_FORMAT,  # Format
                                        _Pointer[_type.BOOL]],  # pSupported
                                       _type.HRESULT]
    GetVideoDecoderConfigCount: _Callable[[_Pointer[_struct.D3D11_VIDEO_DECODER_DESC],  # pDesc
                                           _Pointer[_type.UINT]],  # pCount
                                          _type.HRESULT]
    GetVideoDecoderConfig: _Callable[[_Pointer[_struct.D3D11_VIDEO_DECODER_DESC],  # pDesc
                                      _type.UINT,  # Index
                                      _Pointer[_struct.D3D11_VIDEO_DECODER_CONFIG]],  # pConfig
                                     _type.HRESULT]
    GetContentProtectionCaps: _Callable[[_Pointer[_struct.GUID],  # pCryptoType
                                         _Pointer[_struct.GUID],  # pDecoderProfile
                                         _Pointer[_struct.D3D11_VIDEO_CONTENT_PROTECTION_CAPS]],  # pCaps
                                        _type.HRESULT]
    CheckCryptoKeyExchange: _Callable[[_Pointer[_struct.GUID],  # pCryptoType
                                       _Pointer[_struct.GUID],  # pDecoderProfile
                                       _type.UINT,  # Index
                                       _Pointer[_struct.GUID]],  # pKeyExchangeType
                                      _type.HRESULT]
    SetPrivateData: _Callable[[_Pointer[_struct.GUID],  # guid
                               _type.UINT,  # DataSize
                               _type.c_void_p],  # pData
                              _type.HRESULT]
    SetPrivateDataInterface: _Callable[[_Pointer[_struct.GUID],  # guid
                                        _Unknwnbase.IUnknown],  # pData
                                       _type.HRESULT]


class ID3D11Device(_Unknwnbase.IUnknown):
    CreateBuffer: _Callable[[_Pointer[_struct.D3D11_BUFFER_DESC],  # pDesc
                             _Pointer[_struct.D3D11_SUBRESOURCE_DATA],  # pInitialData
                             _Pointer[ID3D11Buffer]],  # ppBuffer
                            _type.HRESULT]
    CreateTexture1D: _Callable[[_Pointer[_struct.D3D11_TEXTURE1D_DESC],  # pDesc
                                _Pointer[_struct.D3D11_SUBRESOURCE_DATA],  # pInitialData
                                _Pointer[ID3D11Texture1D]],  # ppTexture1D
                               _type.HRESULT]
    CreateTexture2D: _Callable[[_Pointer[_struct.D3D11_TEXTURE2D_DESC],  # pDesc
                                _Pointer[_struct.D3D11_SUBRESOURCE_DATA],  # pInitialData
                                _Pointer[ID3D11Texture2D]],  # ppTexture2D
                               _type.HRESULT]
    CreateTexture3D: _Callable[[_Pointer[_struct.D3D11_TEXTURE3D_DESC],  # pDesc
                                _Pointer[_struct.D3D11_SUBRESOURCE_DATA],  # pInitialData
                                _Pointer[ID3D11Texture3D]],  # ppTexture3D
                               _type.HRESULT]
    CreateShaderResourceView: _Callable[[ID3D11Resource,  # pResource
                                         _Pointer[_struct.D3D11_SHADER_RESOURCE_VIEW_DESC],  # pDesc
                                         _Pointer[ID3D11ShaderResourceView]],  # ppSRView
                                        _type.HRESULT]
    CreateUnorderedAccessView: _Callable[[ID3D11Resource,  # pResource
                                          _Pointer[_struct.D3D11_UNORDERED_ACCESS_VIEW_DESC],  # pDesc
                                          _Pointer[ID3D11UnorderedAccessView]],  # ppUAView
                                         _type.HRESULT]
    CreateRenderTargetView: _Callable[[ID3D11Resource,  # pResource
                                       _Pointer[_struct.D3D11_RENDER_TARGET_VIEW_DESC],  # pDesc
                                       _Pointer[ID3D11RenderTargetView]],  # ppRTView
                                      _type.HRESULT]
    CreateDepthStencilView: _Callable[[ID3D11Resource,  # pResource
                                       _Pointer[_struct.D3D11_DEPTH_STENCIL_VIEW_DESC],  # pDesc
                                       _Pointer[ID3D11DepthStencilView]],  # ppDepthStencilView
                                      _type.HRESULT]
    CreateInputLayout: _Callable[[_Pointer[_struct.D3D11_INPUT_ELEMENT_DESC],  # pInputElementDescs
                                  _type.UINT,  # NumElements
                                  _type.c_void_p,  # pShaderBytecodeWithInputSignature
                                  _type.SIZE_T,  # BytecodeLength
                                  _Pointer[ID3D11InputLayout]],  # ppInputLayout
                                 _type.HRESULT]
    CreateVertexShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                   _type.SIZE_T,  # BytecodeLength
                                   ID3D11ClassLinkage,  # pClassLinkage
                                   _Pointer[ID3D11VertexShader]],  # ppVertexShader
                                  _type.HRESULT]
    CreateGeometryShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                     _type.SIZE_T,  # BytecodeLength
                                     ID3D11ClassLinkage,  # pClassLinkage
                                     _Pointer[ID3D11GeometryShader]],  # ppGeometryShader
                                    _type.HRESULT]
    CreateGeometryShaderWithStreamOutput: _Callable[[_type.c_void_p,  # pShaderBytecode
                                                     _type.SIZE_T,  # BytecodeLength
                                                     _Pointer[_struct.D3D11_SO_DECLARATION_ENTRY],  # pSODeclaration
                                                     _type.UINT,  # NumEntries
                                                     _Pointer[_type.UINT],  # pBufferStrides
                                                     _type.UINT,  # NumStrides
                                                     _type.UINT,  # RasterizedStream
                                                     ID3D11ClassLinkage,  # pClassLinkage
                                                     _Pointer[ID3D11GeometryShader]],  # ppGeometryShader
                                                    _type.HRESULT]
    CreatePixelShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                  _type.SIZE_T,  # BytecodeLength
                                  ID3D11ClassLinkage,  # pClassLinkage
                                  _Pointer[ID3D11PixelShader]],  # ppPixelShader
                                 _type.HRESULT]
    CreateHullShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                 _type.SIZE_T,  # BytecodeLength
                                 ID3D11ClassLinkage,  # pClassLinkage
                                 _Pointer[ID3D11HullShader]],  # ppHullShader
                                _type.HRESULT]
    CreateDomainShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                   _type.SIZE_T,  # BytecodeLength
                                   ID3D11ClassLinkage,  # pClassLinkage
                                   _Pointer[ID3D11DomainShader]],  # ppDomainShader
                                  _type.HRESULT]
    CreateComputeShader: _Callable[[_type.c_void_p,  # pShaderBytecode
                                    _type.SIZE_T,  # BytecodeLength
                                    ID3D11ClassLinkage,  # pClassLinkage
                                    _Pointer[ID3D11ComputeShader]],  # ppComputeShader
                                   _type.HRESULT]
    CreateClassLinkage: _Callable[[_Pointer[ID3D11ClassLinkage]],  # ppLinkage
                                  _type.HRESULT]
    CreateBlendState: _Callable[[_Pointer[_struct.D3D11_BLEND_DESC],  # pBlendStateDesc
                                 _Pointer[ID3D11BlendState]],  # ppBlendState
                                _type.HRESULT]
    CreateDepthStencilState: _Callable[[_Pointer[_struct.D3D11_DEPTH_STENCIL_DESC],  # pDepthStencilDesc
                                        _Pointer[ID3D11DepthStencilState]],  # ppDepthStencilState
                                       _type.HRESULT]
    CreateRasterizerState: _Callable[[_Pointer[_struct.D3D11_RASTERIZER_DESC],  # pRasterizerDesc
                                      _Pointer[ID3D11RasterizerState]],  # ppRasterizerState
                                     _type.HRESULT]
    CreateSamplerState: _Callable[[_Pointer[_struct.D3D11_SAMPLER_DESC],  # pSamplerDesc
                                   _Pointer[ID3D11SamplerState]],  # ppSamplerState
                                  _type.HRESULT]
    CreateQuery: _Callable[[_Pointer[_struct.D3D11_QUERY_DESC],  # pQueryDesc
                            _Pointer[ID3D11Query]],  # ppQuery
                           _type.HRESULT]
    CreatePredicate: _Callable[[_Pointer[_struct.D3D11_QUERY_DESC],  # pPredicateDesc
                                _Pointer[ID3D11Predicate]],  # ppPredicate
                               _type.HRESULT]
    CreateCounter: _Callable[[_Pointer[_struct.D3D11_COUNTER_DESC],  # pCounterDesc
                              _Pointer[ID3D11Counter]],  # ppCounter
                             _type.HRESULT]
    CreateDeferredContext: _Callable[[_type.UINT,  # ContextFlags
                                      _Pointer[ID3D11DeviceContext]],  # ppDeferredContext
                                     _type.HRESULT]
    OpenSharedResource: _Callable[[_type.HANDLE,  # hResource
                                   _Pointer[_struct.IID],  # ReturnedInterface
                                   _type.c_void_p],  # ppResource
                                  _type.HRESULT]
    CheckFormatSupport: _Callable[[_enum.DXGI_FORMAT,  # Format
                                   _Pointer[_type.UINT]],  # pFormatSupport
                                  _type.HRESULT]
    CheckMultisampleQualityLevels: _Callable[[_enum.DXGI_FORMAT,  # Format
                                              _type.UINT,  # SampleCount
                                              _Pointer[_type.UINT]],  # pNumQualityLevels
                                             _type.HRESULT]
    CheckCounterInfo: _Callable[[_Pointer[_struct.D3D11_COUNTER_INFO]],  # pCounterInfo
                                _type.c_void]
    CheckCounter: _Callable[[_Pointer[_struct.D3D11_COUNTER_DESC],  # pDesc
                             _Pointer[_enum.D3D11_COUNTER_TYPE],  # pType
                             _Pointer[_type.UINT],  # pActiveCounters
                             _type.LPSTR,  # szName
                             _Pointer[_type.UINT],  # pNameLength
                             _type.LPSTR,  # szUnits
                             _Pointer[_type.UINT],  # pUnitsLength
                             _type.LPSTR,  # szDescription
                             _Pointer[_type.UINT]],  # pDescriptionLength
                            _type.HRESULT]
    CheckFeatureSupport: _Callable[[_enum.D3D11_FEATURE,  # Feature
                                    _type.c_void_p,  # pFeatureSupportData
                                    _type.UINT],  # FeatureSupportDataSize
                                   _type.HRESULT]
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
    GetFeatureLevel: _Callable[[],
                               _enum.D3D_FEATURE_LEVEL]
    GetCreationFlags: _Callable[[],
                                _type.UINT]
    GetDeviceRemovedReason: _Callable[[],
                                      _type.HRESULT]
    GetImmediateContext: _Callable[[_Pointer[ID3D11DeviceContext]],  # ppImmediateContext
                                   _type.c_void]
    SetExceptionMode: _Callable[[_type.UINT],  # RaiseFlags
                                _type.HRESULT]
    GetExceptionMode: _Callable[[],
                                _type.UINT]
