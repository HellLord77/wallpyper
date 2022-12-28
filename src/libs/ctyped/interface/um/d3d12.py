from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import d3dcommon as _d3dcommon
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D12Object(_Unknwnbase.IUnknown):
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
    SetName: _Callable[[_type.LPCWSTR],  # Name
                       _type.HRESULT]


class ID3D12DeviceChild(ID3D12Object):
    GetDevice: _Callable[[_Pointer[_struct.IID],  # riid
                          _type.c_void_p],  # ppvDevice
                         _type.HRESULT]


class ID3D12RootSignature(ID3D12DeviceChild):
    pass


class ID3D12RootSignatureDeserializer(_Unknwnbase.IUnknown):
    GetRootSignatureDesc: _Callable[[],
                                    _Pointer[_struct.D3D12_ROOT_SIGNATURE_DESC]]


class ID3D12VersionedRootSignatureDeserializer(_Unknwnbase.IUnknown):
    GetRootSignatureDescAtVersion: _Callable[[_enum.D3D_ROOT_SIGNATURE_VERSION,  # convertToVersion
                                              _Pointer[_Pointer[_struct.D3D12_VERSIONED_ROOT_SIGNATURE_DESC]]],  # ppDesc
                                             _type.HRESULT]
    GetUnconvertedRootSignatureDesc: _Callable[[],
                                               _Pointer[_struct.D3D12_VERSIONED_ROOT_SIGNATURE_DESC]]


class ID3D12Pageable(ID3D12DeviceChild):
    pass


class ID3D12Heap(ID3D12Pageable):
    GetDesc: _Callable[[],
                       _struct.D3D12_HEAP_DESC]


class ID3D12Resource(ID3D12Pageable):
    Map: _Callable[[_type.UINT,  # Subresource
                    _Pointer[_struct.D3D12_RANGE],  # pReadRange
                    _type.c_void_p],  # ppData
                   _type.HRESULT]
    Unmap: _Callable[[_type.UINT,  # Subresource
                      _Pointer[_struct.D3D12_RANGE]],  # pWrittenRange
                     _type.c_void]
    GetDesc: _Callable[[],
                       _struct.D3D12_RESOURCE_DESC]
    GetGPUVirtualAddress: _Callable[[],
                                    _type.D3D12_GPU_VIRTUAL_ADDRESS]
    WriteToSubresource: _Callable[[_type.UINT,  # DstSubresource
                                   _Pointer[_struct.D3D12_BOX],  # pDstBox
                                   _type.c_void_p,  # pSrcData
                                   _type.UINT,  # SrcRowPitch
                                   _type.UINT],  # SrcDepthPitch
                                  _type.HRESULT]
    ReadFromSubresource: _Callable[[_type.c_void_p,  # pDstData
                                    _type.UINT,  # DstRowPitch
                                    _type.UINT,  # DstDepthPitch
                                    _type.UINT,  # SrcSubresource
                                    _Pointer[_struct.D3D12_BOX]],  # pSrcBox
                                   _type.HRESULT]
    GetHeapProperties: _Callable[[_Pointer[_struct.D3D12_HEAP_PROPERTIES],  # pHeapProperties
                                  _Pointer[_enum.D3D12_HEAP_FLAGS]],  # pHeapFlags
                                 _type.HRESULT]


class ID3D12CommandAllocator(ID3D12Pageable):
    Reset: _Callable[[],
                     _type.HRESULT]


class ID3D12Fence(ID3D12Pageable):
    GetCompletedValue: _Callable[[],
                                 _type.UINT64]
    SetEventOnCompletion: _Callable[[_type.UINT64,  # Value
                                     _type.HANDLE],  # hEvent
                                    _type.HRESULT]
    Signal: _Callable[[_type.UINT64],  # Value
                      _type.HRESULT]


class ID3D12Fence1(ID3D12Fence):
    GetCreationFlags: _Callable[[],
                                _enum.D3D12_FENCE_FLAGS]


class ID3D12PipelineState(ID3D12Pageable):
    GetCachedBlob: _Callable[[_Pointer[_d3dcommon.ID3DBlob]],  # ppBlob
                             _type.HRESULT]


class ID3D12DescriptorHeap(ID3D12Pageable):
    GetDesc: _Callable[[],
                       _struct.D3D12_DESCRIPTOR_HEAP_DESC]
    GetCPUDescriptorHandleForHeapStart: _Callable[[],
                                                  _struct.D3D12_CPU_DESCRIPTOR_HANDLE]
    GetGPUDescriptorHandleForHeapStart: _Callable[[],
                                                  _struct.D3D12_GPU_DESCRIPTOR_HANDLE]


class ID3D12QueryHeap(ID3D12Pageable):
    pass


class ID3D12CommandSignature(ID3D12Pageable):
    pass


class ID3D12CommandList(ID3D12DeviceChild):
    GetType: _Callable[[],
                       _enum.D3D12_COMMAND_LIST_TYPE]


class ID3D12GraphicsCommandList(ID3D12CommandList):
    Close: _Callable[[],
                     _type.HRESULT]
    Reset: _Callable[[ID3D12CommandAllocator,  # pAllocator
                      ID3D12PipelineState],  # pInitialState
                     _type.HRESULT]
    ClearState: _Callable[[ID3D12PipelineState],  # pPipelineState
                          _type.c_void]
    DrawInstanced: _Callable[[_type.UINT,  # VertexCountPerInstance
                              _type.UINT,  # InstanceCount
                              _type.UINT,  # StartVertexLocation
                              _type.UINT],  # StartInstanceLocation
                             _type.c_void]
    DrawIndexedInstanced: _Callable[[_type.UINT,  # IndexCountPerInstance
                                     _type.UINT,  # InstanceCount
                                     _type.UINT,  # StartIndexLocation
                                     _type.INT,  # BaseVertexLocation
                                     _type.UINT],  # StartInstanceLocation
                                    _type.c_void]
    Dispatch: _Callable[[_type.UINT,  # ThreadGroupCountX
                         _type.UINT,  # ThreadGroupCountY
                         _type.UINT],  # ThreadGroupCountZ
                        _type.c_void]
    CopyBufferRegion: _Callable[[ID3D12Resource,  # pDstBuffer
                                 _type.UINT64,  # DstOffset
                                 ID3D12Resource,  # pSrcBuffer
                                 _type.UINT64,  # SrcOffset
                                 _type.UINT64],  # NumBytes
                                _type.c_void]
    CopyTextureRegion: _Callable[[_Pointer[_struct.D3D12_TEXTURE_COPY_LOCATION],  # pDst
                                  _type.UINT,  # DstX
                                  _type.UINT,  # DstY
                                  _type.UINT,  # DstZ
                                  _Pointer[_struct.D3D12_TEXTURE_COPY_LOCATION],  # pSrc
                                  _Pointer[_struct.D3D12_BOX]],  # pSrcBox
                                 _type.c_void]
    CopyResource: _Callable[[ID3D12Resource,  # pDstResource
                             ID3D12Resource],  # pSrcResource
                            _type.c_void]
    CopyTiles: _Callable[[ID3D12Resource,  # pTiledResource
                          _Pointer[_struct.D3D12_TILED_RESOURCE_COORDINATE],  # pTileRegionStartCoordinate
                          _Pointer[_struct.D3D12_TILE_REGION_SIZE],  # pTileRegionSize
                          ID3D12Resource,  # pBuffer
                          _type.UINT64,  # BufferStartOffsetInBytes
                          _enum.D3D12_TILE_COPY_FLAGS],  # Flags
                         _type.c_void]
    ResolveSubresource: _Callable[[ID3D12Resource,  # pDstResource
                                   _type.UINT,  # DstSubresource
                                   ID3D12Resource,  # pSrcResource
                                   _type.UINT,  # SrcSubresource
                                   _enum.DXGI_FORMAT],  # Format
                                  _type.c_void]
    IASetPrimitiveTopology: _Callable[[_enum.D3D12_PRIMITIVE_TOPOLOGY],  # PrimitiveTopology
                                      _type.c_void]
    RSSetViewports: _Callable[[_type.UINT,  # NumViewports
                               _Pointer[_struct.D3D12_VIEWPORT]],  # pViewports
                              _type.c_void]
    RSSetScissorRects: _Callable[[_type.UINT,  # NumRects
                                  _Pointer[_struct.D3D12_RECT]],  # pRects
                                 _type.c_void]
    OMSetBlendFactor: _Callable[[_Pointer[_type.FLOAT]],  # BlendFactor
                                _type.c_void]
    OMSetStencilRef: _Callable[[_type.UINT],  # StencilRef
                               _type.c_void]
    SetPipelineState: _Callable[[ID3D12PipelineState],  # pPipelineState
                                _type.c_void]
    ResourceBarrier: _Callable[[_type.UINT,  # NumBarriers
                                _Pointer[_struct.D3D12_RESOURCE_BARRIER]],  # pBarriers
                               _type.c_void]
    ExecuteBundle: _Callable[[ID3D12GraphicsCommandList],  # pCommandList
                             _type.c_void]
    SetDescriptorHeaps: _Callable[[_type.UINT,  # NumDescriptorHeaps
                                   _Pointer[ID3D12DescriptorHeap]],  # ppDescriptorHeaps
                                  _type.c_void]
    SetComputeRootSignature: _Callable[[ID3D12RootSignature],  # pRootSignature
                                       _type.c_void]
    SetGraphicsRootSignature: _Callable[[ID3D12RootSignature],  # pRootSignature
                                        _type.c_void]
    SetComputeRootDescriptorTable: _Callable[[_type.UINT,  # RootParameterIndex
                                              _struct.D3D12_GPU_DESCRIPTOR_HANDLE],  # BaseDescriptor
                                             _type.c_void]
    SetGraphicsRootDescriptorTable: _Callable[[_type.UINT,  # RootParameterIndex
                                               _struct.D3D12_GPU_DESCRIPTOR_HANDLE],  # BaseDescriptor
                                              _type.c_void]
    SetComputeRoot32BitConstant: _Callable[[_type.UINT,  # RootParameterIndex
                                            _type.UINT,  # SrcData
                                            _type.UINT],  # DestOffsetIn32BitValues
                                           _type.c_void]
    SetGraphicsRoot32BitConstant: _Callable[[_type.UINT,  # RootParameterIndex
                                             _type.UINT,  # SrcData
                                             _type.UINT],  # DestOffsetIn32BitValues
                                            _type.c_void]
    SetComputeRoot32BitConstants: _Callable[[_type.UINT,  # RootParameterIndex
                                             _type.UINT,  # Num32BitValuesToSet
                                             _type.c_void_p,  # pSrcData
                                             _type.UINT],  # DestOffsetIn32BitValues
                                            _type.c_void]
    SetGraphicsRoot32BitConstants: _Callable[[_type.UINT,  # RootParameterIndex
                                              _type.UINT,  # Num32BitValuesToSet
                                              _type.c_void_p,  # pSrcData
                                              _type.UINT],  # DestOffsetIn32BitValues
                                             _type.c_void]
    SetComputeRootConstantBufferView: _Callable[[_type.UINT,  # RootParameterIndex
                                                 _type.D3D12_GPU_VIRTUAL_ADDRESS],  # BufferLocation
                                                _type.c_void]
    SetGraphicsRootConstantBufferView: _Callable[[_type.UINT,  # RootParameterIndex
                                                  _type.D3D12_GPU_VIRTUAL_ADDRESS],  # BufferLocation
                                                 _type.c_void]
    SetComputeRootShaderResourceView: _Callable[[_type.UINT,  # RootParameterIndex
                                                 _type.D3D12_GPU_VIRTUAL_ADDRESS],  # BufferLocation
                                                _type.c_void]
    SetGraphicsRootShaderResourceView: _Callable[[_type.UINT,  # RootParameterIndex
                                                  _type.D3D12_GPU_VIRTUAL_ADDRESS],  # BufferLocation
                                                 _type.c_void]
    SetComputeRootUnorderedAccessView: _Callable[[_type.UINT,  # RootParameterIndex
                                                  _type.D3D12_GPU_VIRTUAL_ADDRESS],  # BufferLocation
                                                 _type.c_void]
    SetGraphicsRootUnorderedAccessView: _Callable[[_type.UINT,  # RootParameterIndex
                                                   _type.D3D12_GPU_VIRTUAL_ADDRESS],  # BufferLocation
                                                  _type.c_void]
    IASetIndexBuffer: _Callable[[_Pointer[_struct.D3D12_INDEX_BUFFER_VIEW]],  # pView
                                _type.c_void]
    IASetVertexBuffers: _Callable[[_type.UINT,  # StartSlot
                                   _type.UINT,  # NumViews
                                   _Pointer[_struct.D3D12_VERTEX_BUFFER_VIEW]],  # pViews
                                  _type.c_void]
    SOSetTargets: _Callable[[_type.UINT,  # StartSlot
                             _type.UINT,  # NumViews
                             _Pointer[_struct.D3D12_STREAM_OUTPUT_BUFFER_VIEW]],  # pViews
                            _type.c_void]
    OMSetRenderTargets: _Callable[[_type.UINT,  # NumRenderTargetDescriptors
                                   _Pointer[_struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # pRenderTargetDescriptors
                                   _type.BOOL,  # RTsSingleHandleToDescriptorRange
                                   _Pointer[_struct.D3D12_CPU_DESCRIPTOR_HANDLE]],  # pDepthStencilDescriptor
                                  _type.c_void]
    ClearDepthStencilView: _Callable[[_struct.D3D12_CPU_DESCRIPTOR_HANDLE,  # DepthStencilView
                                      _enum.D3D12_CLEAR_FLAGS,  # ClearFlags
                                      _type.FLOAT,  # Depth
                                      _type.UINT8,  # Stencil
                                      _type.UINT,  # NumRects
                                      _Pointer[_struct.D3D12_RECT]],  # pRects
                                     _type.c_void]
    ClearRenderTargetView: _Callable[[_struct.D3D12_CPU_DESCRIPTOR_HANDLE,  # RenderTargetView
                                      _Pointer[_type.FLOAT],  # ColorRGBA
                                      _type.UINT,  # NumRects
                                      _Pointer[_struct.D3D12_RECT]],  # pRects
                                     _type.c_void]
    ClearUnorderedAccessViewUint: _Callable[[_struct.D3D12_GPU_DESCRIPTOR_HANDLE,  # ViewGPUHandleInCurrentHeap
                                             _struct.D3D12_CPU_DESCRIPTOR_HANDLE,  # ViewCPUHandle
                                             ID3D12Resource,  # pResource
                                             _Pointer[_type.UINT],  # Values
                                             _type.UINT,  # NumRects
                                             _Pointer[_struct.D3D12_RECT]],  # pRects
                                            _type.c_void]
    ClearUnorderedAccessViewFloat: _Callable[[_struct.D3D12_GPU_DESCRIPTOR_HANDLE,  # ViewGPUHandleInCurrentHeap
                                              _struct.D3D12_CPU_DESCRIPTOR_HANDLE,  # ViewCPUHandle
                                              ID3D12Resource,  # pResource
                                              _Pointer[_type.FLOAT],  # Values
                                              _type.UINT,  # NumRects
                                              _Pointer[_struct.D3D12_RECT]],  # pRects
                                             _type.c_void]
    DiscardResource: _Callable[[ID3D12Resource,  # pResource
                                _Pointer[_struct.D3D12_DISCARD_REGION]],  # pRegion
                               _type.c_void]
    BeginQuery: _Callable[[ID3D12QueryHeap,  # pQueryHeap
                           _enum.D3D12_QUERY_TYPE,  # Type
                           _type.UINT],  # Index
                          _type.c_void]
    EndQuery: _Callable[[ID3D12QueryHeap,  # pQueryHeap
                         _enum.D3D12_QUERY_TYPE,  # Type
                         _type.UINT],  # Index
                        _type.c_void]
    ResolveQueryData: _Callable[[ID3D12QueryHeap,  # pQueryHeap
                                 _enum.D3D12_QUERY_TYPE,  # Type
                                 _type.UINT,  # StartIndex
                                 _type.UINT,  # NumQueries
                                 ID3D12Resource,  # pDestinationBuffer
                                 _type.UINT64],  # AlignedDestinationBufferOffset
                                _type.c_void]
    SetPredication: _Callable[[ID3D12Resource,  # pBuffer
                               _type.UINT64,  # AlignedBufferOffset
                               _enum.D3D12_PREDICATION_OP],  # Operation
                              _type.c_void]
    SetMarker: _Callable[[_type.UINT,  # Metadata
                          _type.c_void_p,  # pData
                          _type.UINT],  # Size
                         _type.c_void]
    BeginEvent: _Callable[[_type.UINT,  # Metadata
                           _type.c_void_p,  # pData
                           _type.UINT],  # Size
                          _type.c_void]
    EndEvent: _Callable[[],
                        _type.c_void]
    ExecuteIndirect: _Callable[[ID3D12CommandSignature,  # pCommandSignature
                                _type.UINT,  # MaxCommandCount
                                ID3D12Resource,  # pArgumentBuffer
                                _type.UINT64,  # ArgumentBufferOffset
                                ID3D12Resource,  # pCountBuffer
                                _type.UINT64],  # CountBufferOffset
                               _type.c_void]


class ID3D12GraphicsCommandList1(ID3D12GraphicsCommandList):
    AtomicCopyBufferUINT: _Callable[[ID3D12Resource,  # pDstBuffer
                                     _type.UINT64,  # DstOffset
                                     ID3D12Resource,  # pSrcBuffer
                                     _type.UINT64,  # SrcOffset
                                     _type.UINT,  # Dependencies
                                     _Pointer[ID3D12Resource],  # ppDependentResources
                                     _Pointer[_struct.D3D12_SUBRESOURCE_RANGE_UINT64]],  # pDependentSubresourceRanges
                                    _type.c_void]
    AtomicCopyBufferUINT64: _Callable[[ID3D12Resource,  # pDstBuffer
                                       _type.UINT64,  # DstOffset
                                       ID3D12Resource,  # pSrcBuffer
                                       _type.UINT64,  # SrcOffset
                                       _type.UINT,  # Dependencies
                                       _Pointer[ID3D12Resource],  # ppDependentResources
                                       _Pointer[_struct.D3D12_SUBRESOURCE_RANGE_UINT64]],  # pDependentSubresourceRanges
                                      _type.c_void]
    OMSetDepthBounds: _Callable[[_type.FLOAT,  # Min
                                 _type.FLOAT],  # Max
                                _type.c_void]
    SetSamplePositions: _Callable[[_type.UINT,  # NumSamplesPerPixel
                                   _type.UINT,  # NumPixels
                                   _Pointer[_struct.D3D12_SAMPLE_POSITION]],  # pSamplePositions
                                  _type.c_void]
    ResolveSubresourceRegion: _Callable[[ID3D12Resource,  # pDstResource
                                         _type.UINT,  # DstSubresource
                                         _type.UINT,  # DstX
                                         _type.UINT,  # DstY
                                         ID3D12Resource,  # pSrcResource
                                         _type.UINT,  # SrcSubresource
                                         _Pointer[_struct.D3D12_RECT],  # pSrcRect
                                         _enum.DXGI_FORMAT,  # Format
                                         _enum.D3D12_RESOLVE_MODE],  # ResolveMode
                                        _type.c_void]
    SetViewInstanceMask: _Callable[[_type.UINT],  # Mask
                                   _type.c_void]


class ID3D12GraphicsCommandList2(ID3D12GraphicsCommandList1):
    WriteBufferImmediate: _Callable[[_type.UINT,  # Count
                                     _Pointer[_struct.D3D12_WRITEBUFFERIMMEDIATE_PARAMETER],  # pParams
                                     _Pointer[_enum.D3D12_WRITEBUFFERIMMEDIATE_MODE]],  # pModes
                                    _type.c_void]


class ID3D12CommandQueue(ID3D12Pageable):
    UpdateTileMappings: _Callable[[ID3D12Resource,  # pResource
                                   _type.UINT,  # NumResourceRegions
                                   _Pointer[_struct.D3D12_TILED_RESOURCE_COORDINATE],  # pResourceRegionStartCoordinates
                                   _Pointer[_struct.D3D12_TILE_REGION_SIZE],  # pResourceRegionSizes
                                   ID3D12Heap,  # pHeap
                                   _type.UINT,  # NumRanges
                                   _Pointer[_enum.D3D12_TILE_RANGE_FLAGS],  # pRangeFlags
                                   _Pointer[_type.UINT],  # pHeapRangeStartOffsets
                                   _Pointer[_type.UINT],  # pRangeTileCounts
                                   _enum.D3D12_TILE_MAPPING_FLAGS],  # Flags
                                  _type.c_void]
    CopyTileMappings: _Callable[[ID3D12Resource,  # pDstResource
                                 _Pointer[_struct.D3D12_TILED_RESOURCE_COORDINATE],  # pDstRegionStartCoordinate
                                 ID3D12Resource,  # pSrcResource
                                 _Pointer[_struct.D3D12_TILED_RESOURCE_COORDINATE],  # pSrcRegionStartCoordinate
                                 _Pointer[_struct.D3D12_TILE_REGION_SIZE],  # pRegionSize
                                 _enum.D3D12_TILE_MAPPING_FLAGS],  # Flags
                                _type.c_void]
    ExecuteCommandLists: _Callable[[_type.UINT,  # NumCommandLists
                                    _Pointer[ID3D12CommandList]],  # ppCommandLists
                                   _type.c_void]
    SetMarker: _Callable[[_type.UINT,  # Metadata
                          _type.c_void_p,  # pData
                          _type.UINT],  # Size
                         _type.c_void]
    BeginEvent: _Callable[[_type.UINT,  # Metadata
                           _type.c_void_p,  # pData
                           _type.UINT],  # Size
                          _type.c_void]
    EndEvent: _Callable[[],
                        _type.c_void]
    Signal: _Callable[[ID3D12Fence,  # pFence
                       _type.UINT64],  # Value
                      _type.HRESULT]
    Wait: _Callable[[ID3D12Fence,  # pFence
                     _type.UINT64],  # Value
                    _type.HRESULT]
    GetTimestampFrequency: _Callable[[_Pointer[_type.UINT64]],  # pFrequency
                                     _type.HRESULT]
    GetClockCalibration: _Callable[[_Pointer[_type.UINT64],  # pGpuTimestamp
                                    _Pointer[_type.UINT64]],  # pCpuTimestamp
                                   _type.HRESULT]
    GetDesc: _Callable[[],
                       _struct.D3D12_COMMAND_QUEUE_DESC]


class ID3D12Device(ID3D12Object):
    GetNodeCount: _Callable[[],
                            _type.UINT]
    CreateCommandQueue: _Callable[[_Pointer[_struct.D3D12_COMMAND_QUEUE_DESC],  # pDesc
                                   _Pointer[_struct.IID],  # riid
                                   _type.c_void_p],  # ppCommandQueue
                                  _type.HRESULT]
    CreateCommandAllocator: _Callable[[_enum.D3D12_COMMAND_LIST_TYPE,  # type
                                       _Pointer[_struct.IID],  # riid
                                       _type.c_void_p],  # ppCommandAllocator
                                      _type.HRESULT]
    CreateGraphicsPipelineState: _Callable[[_Pointer[_struct.D3D12_GRAPHICS_PIPELINE_STATE_DESC],  # pDesc
                                            _Pointer[_struct.IID],  # riid
                                            _type.c_void_p],  # ppPipelineState
                                           _type.HRESULT]
    CreateComputePipelineState: _Callable[[_Pointer[_struct.D3D12_COMPUTE_PIPELINE_STATE_DESC],  # pDesc
                                           _Pointer[_struct.IID],  # riid
                                           _type.c_void_p],  # ppPipelineState
                                          _type.HRESULT]
    CreateCommandList: _Callable[[_type.UINT,  # nodeMask
                                  _enum.D3D12_COMMAND_LIST_TYPE,  # type
                                  ID3D12CommandAllocator,  # pCommandAllocator
                                  ID3D12PipelineState,  # pInitialState
                                  _Pointer[_struct.IID],  # riid
                                  _type.c_void_p],  # ppCommandList
                                 _type.HRESULT]
    CheckFeatureSupport: _Callable[[_enum.D3D12_FEATURE,  # Feature
                                    _type.c_void_p,  # pFeatureSupportData
                                    _type.UINT],  # FeatureSupportDataSize
                                   _type.HRESULT]
    CreateDescriptorHeap: _Callable[[_Pointer[_struct.D3D12_DESCRIPTOR_HEAP_DESC],  # pDescriptorHeapDesc
                                     _Pointer[_struct.IID],  # riid
                                     _type.c_void_p],  # ppvHeap
                                    _type.HRESULT]
    GetDescriptorHandleIncrementSize: _Callable[[_enum.D3D12_DESCRIPTOR_HEAP_TYPE],  # DescriptorHeapType
                                                _type.UINT]
    CreateRootSignature: _Callable[[_type.UINT,  # nodeMask
                                    _type.c_void_p,  # pBlobWithRootSignature
                                    _type.SIZE_T,  # blobLengthInBytes
                                    _Pointer[_struct.IID],  # riid
                                    _type.c_void_p],  # ppvRootSignature
                                   _type.HRESULT]
    CreateConstantBufferView: _Callable[[_Pointer[_struct.D3D12_CONSTANT_BUFFER_VIEW_DESC],  # pDesc
                                         _struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # DestDescriptor
                                        _type.c_void]
    CreateShaderResourceView: _Callable[[ID3D12Resource,  # pResource
                                         _Pointer[_struct.D3D12_SHADER_RESOURCE_VIEW_DESC],  # pDesc
                                         _struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # DestDescriptor
                                        _type.c_void]
    CreateUnorderedAccessView: _Callable[[ID3D12Resource,  # pResource
                                          ID3D12Resource,  # pCounterResource
                                          _Pointer[_struct.D3D12_UNORDERED_ACCESS_VIEW_DESC],  # pDesc
                                          _struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # DestDescriptor
                                         _type.c_void]
    CreateRenderTargetView: _Callable[[ID3D12Resource,  # pResource
                                       _Pointer[_struct.D3D12_RENDER_TARGET_VIEW_DESC],  # pDesc
                                       _struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # DestDescriptor
                                      _type.c_void]
    CreateDepthStencilView: _Callable[[ID3D12Resource,  # pResource
                                       _Pointer[_struct.D3D12_DEPTH_STENCIL_VIEW_DESC],  # pDesc
                                       _struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # DestDescriptor
                                      _type.c_void]
    CreateSampler: _Callable[[_Pointer[_struct.D3D12_SAMPLER_DESC],  # pDesc
                              _struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # DestDescriptor
                             _type.c_void]
    CopyDescriptors: _Callable[[_type.UINT,  # NumDestDescriptorRanges
                                _Pointer[_struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # pDestDescriptorRangeStarts
                                _Pointer[_type.UINT],  # pDestDescriptorRangeSizes
                                _type.UINT,  # NumSrcDescriptorRanges
                                _Pointer[_struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # pSrcDescriptorRangeStarts
                                _Pointer[_type.UINT],  # pSrcDescriptorRangeSizes
                                _enum.D3D12_DESCRIPTOR_HEAP_TYPE],  # DescriptorHeapsType
                               _type.c_void]
    CopyDescriptorsSimple: _Callable[[_type.UINT,  # NumDescriptors
                                      _struct.D3D12_CPU_DESCRIPTOR_HANDLE,  # DestDescriptorRangeStart
                                      _struct.D3D12_CPU_DESCRIPTOR_HANDLE,  # SrcDescriptorRangeStart
                                      _enum.D3D12_DESCRIPTOR_HEAP_TYPE],  # DescriptorHeapsType
                                     _type.c_void]
    GetResourceAllocationInfo: _Callable[[_type.UINT,  # visibleMask
                                          _type.UINT,  # numResourceDescs
                                          _Pointer[_struct.D3D12_RESOURCE_DESC]],  # pResourceDescs
                                         _struct.D3D12_RESOURCE_ALLOCATION_INFO]
    GetCustomHeapProperties: _Callable[[_type.UINT,  # nodeMask
                                        _enum.D3D12_HEAP_TYPE],  # heapType
                                       _struct.D3D12_HEAP_PROPERTIES]
    CreateCommittedResource: _Callable[[_Pointer[_struct.D3D12_HEAP_PROPERTIES],  # pHeapProperties
                                        _enum.D3D12_HEAP_FLAGS,  # HeapFlags
                                        _Pointer[_struct.D3D12_RESOURCE_DESC],  # pDesc
                                        _enum.D3D12_RESOURCE_STATES,  # InitialResourceState
                                        _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                        _Pointer[_struct.IID],  # riidResource
                                        _type.c_void_p],  # ppvResource
                                       _type.HRESULT]
    CreateHeap: _Callable[[_Pointer[_struct.D3D12_HEAP_DESC],  # pDesc
                           _Pointer[_struct.IID],  # riid
                           _type.c_void_p],  # ppvHeap
                          _type.HRESULT]
    CreatePlacedResource: _Callable[[ID3D12Heap,  # pHeap
                                     _type.UINT64,  # HeapOffset
                                     _Pointer[_struct.D3D12_RESOURCE_DESC],  # pDesc
                                     _enum.D3D12_RESOURCE_STATES,  # InitialState
                                     _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                     _Pointer[_struct.IID],  # riid
                                     _type.c_void_p],  # ppvResource
                                    _type.HRESULT]
    CreateReservedResource: _Callable[[_Pointer[_struct.D3D12_RESOURCE_DESC],  # pDesc
                                       _enum.D3D12_RESOURCE_STATES,  # InitialState
                                       _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                       _Pointer[_struct.IID],  # riid
                                       _type.c_void_p],  # ppvResource
                                      _type.HRESULT]
    CreateSharedHandle: _Callable[[ID3D12DeviceChild,  # pObject
                                   _Pointer[_struct.SECURITY_ATTRIBUTES],  # pAttributes
                                   _type.DWORD,  # Access
                                   _type.LPCWSTR,  # Name
                                   _Pointer[_type.HANDLE]],  # pHandle
                                  _type.HRESULT]
    OpenSharedHandle: _Callable[[_type.HANDLE,  # NTHandle
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppvObj
                                _type.HRESULT]
    OpenSharedHandleByName: _Callable[[_type.LPCWSTR,  # Name
                                       _type.DWORD,  # Access
                                       _Pointer[_type.HANDLE]],  # pNTHandle
                                      _type.HRESULT]
    MakeResident: _Callable[[_type.UINT,  # NumObjects
                             _Pointer[ID3D12Pageable]],  # ppObjects
                            _type.HRESULT]
    Evict: _Callable[[_type.UINT,  # NumObjects
                      _Pointer[ID3D12Pageable]],  # ppObjects
                     _type.HRESULT]
    CreateFence: _Callable[[_type.UINT64,  # InitialValue
                            _enum.D3D12_FENCE_FLAGS,  # Flags
                            _Pointer[_struct.IID],  # riid
                            _type.c_void_p],  # ppFence
                           _type.HRESULT]
    GetDeviceRemovedReason: _Callable[[],
                                      _type.HRESULT]
    GetCopyableFootprints: _Callable[[_Pointer[_struct.D3D12_RESOURCE_DESC],  # pResourceDesc
                                      _type.UINT,  # FirstSubresource
                                      _type.UINT,  # NumSubresources
                                      _type.UINT64,  # BaseOffset
                                      _Pointer[_struct.D3D12_PLACED_SUBRESOURCE_FOOTPRINT],  # pLayouts
                                      _Pointer[_type.UINT],  # pNumRows
                                      _Pointer[_type.UINT64],  # pRowSizeInBytes
                                      _Pointer[_type.UINT64]],  # pTotalBytes
                                     _type.c_void]
    CreateQueryHeap: _Callable[[_Pointer[_struct.D3D12_QUERY_HEAP_DESC],  # pDesc
                                _Pointer[_struct.IID],  # riid
                                _type.c_void_p],  # ppvHeap
                               _type.HRESULT]
    SetStablePowerState: _Callable[[_type.BOOL],  # Enable
                                   _type.HRESULT]
    CreateCommandSignature: _Callable[[_Pointer[_struct.D3D12_COMMAND_SIGNATURE_DESC],  # pDesc
                                       ID3D12RootSignature,  # pRootSignature
                                       _Pointer[_struct.IID],  # riid
                                       _type.c_void_p],  # ppvCommandSignature
                                      _type.HRESULT]
    GetResourceTiling: _Callable[[ID3D12Resource,  # pTiledResource
                                  _Pointer[_type.UINT],  # pNumTilesForEntireResource
                                  _Pointer[_struct.D3D12_PACKED_MIP_INFO],  # pPackedMipDesc
                                  _Pointer[_struct.D3D12_TILE_SHAPE],  # pStandardTileShapeForNonPackedMips
                                  _Pointer[_type.UINT],  # pNumSubresourceTilings
                                  _type.UINT,  # FirstSubresourceTilingToGet
                                  _Pointer[_struct.D3D12_SUBRESOURCE_TILING]],  # pSubresourceTilingsForNonPackedMips
                                 _type.c_void]
    GetAdapterLuid: _Callable[[],
                              _struct.LUID]


class ID3D12PipelineLibrary(ID3D12DeviceChild):
    StorePipeline: _Callable[[_type.LPCWSTR,  # pName
                              ID3D12PipelineState],  # pPipeline
                             _type.HRESULT]
    LoadGraphicsPipeline: _Callable[[_type.LPCWSTR,  # pName
                                     _Pointer[_struct.D3D12_GRAPHICS_PIPELINE_STATE_DESC],  # pDesc
                                     _Pointer[_struct.IID],  # riid
                                     _type.c_void_p],  # ppPipelineState
                                    _type.HRESULT]
    LoadComputePipeline: _Callable[[_type.LPCWSTR,  # pName
                                    _Pointer[_struct.D3D12_COMPUTE_PIPELINE_STATE_DESC],  # pDesc
                                    _Pointer[_struct.IID],  # riid
                                    _type.c_void_p],  # ppPipelineState
                                   _type.HRESULT]
    GetSerializedSize: _Callable[[],
                                 _type.SIZE_T]
    Serialize: _Callable[[_type.c_void_p,  # pData
                          _type.SIZE_T],  # DataSizeInBytes
                         _type.HRESULT]


class ID3D12PipelineLibrary1(ID3D12PipelineLibrary):
    LoadPipeline: _Callable[[_type.LPCWSTR,  # pName
                             _Pointer[_struct.D3D12_PIPELINE_STATE_STREAM_DESC],  # pDesc
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppPipelineState
                            _type.HRESULT]


class ID3D12Device1(ID3D12Device):
    CreatePipelineLibrary: _Callable[[_type.c_void_p,  # pLibraryBlob
                                      _type.SIZE_T,  # BlobLength
                                      _Pointer[_struct.IID],  # riid
                                      _type.c_void_p],  # ppPipelineLibrary
                                     _type.HRESULT]
    SetEventOnMultipleFenceCompletion: _Callable[[_Pointer[ID3D12Fence],  # ppFences
                                                  _Pointer[_type.UINT64],  # pFenceValues
                                                  _type.UINT,  # NumFences
                                                  _enum.D3D12_MULTIPLE_FENCE_WAIT_FLAGS,  # Flags
                                                  _type.HANDLE],  # hEvent
                                                 _type.HRESULT]
    SetResidencyPriority: _Callable[[_type.UINT,  # NumObjects
                                     _Pointer[ID3D12Pageable],  # ppObjects
                                     _Pointer[_enum.D3D12_RESIDENCY_PRIORITY]],  # pPriorities
                                    _type.HRESULT]


class ID3D12Device2(ID3D12Device1):
    CreatePipelineState: _Callable[[_Pointer[_struct.D3D12_PIPELINE_STATE_STREAM_DESC],  # pDesc
                                    _Pointer[_struct.IID],  # riid
                                    _type.c_void_p],  # ppPipelineState
                                   _type.HRESULT]


class ID3D12Device3(ID3D12Device2):
    OpenExistingHeapFromAddress: _Callable[[_type.c_void_p,  # pAddress
                                            _Pointer[_struct.IID],  # riid
                                            _type.c_void_p],  # ppvHeap
                                           _type.HRESULT]
    OpenExistingHeapFromFileMapping: _Callable[[_type.HANDLE,  # hFileMapping
                                                _Pointer[_struct.IID],  # riid
                                                _type.c_void_p],  # ppvHeap
                                               _type.HRESULT]
    EnqueueMakeResident: _Callable[[_enum.D3D12_RESIDENCY_FLAGS,  # Flags
                                    _type.UINT,  # NumObjects
                                    _Pointer[ID3D12Pageable],  # ppObjects
                                    ID3D12Fence,  # pFenceToSignal
                                    _type.UINT64],  # FenceValueToSignal
                                   _type.HRESULT]


class ID3D12ProtectedSession(ID3D12DeviceChild):
    GetStatusFence: _Callable[[_Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppFence
                              _type.HRESULT]
    GetSessionStatus: _Callable[[],
                                _enum.D3D12_PROTECTED_SESSION_STATUS]


class ID3D12ProtectedResourceSession(ID3D12ProtectedSession):
    GetDesc: _Callable[[],
                       _struct.D3D12_PROTECTED_RESOURCE_SESSION_DESC]


class ID3D12Device4(ID3D12Device3):
    CreateCommandList1: _Callable[[_type.UINT,  # nodeMask
                                   _enum.D3D12_COMMAND_LIST_TYPE,  # type
                                   _enum.D3D12_COMMAND_LIST_FLAGS,  # flags
                                   _Pointer[_struct.IID],  # riid
                                   _type.c_void_p],  # ppCommandList
                                  _type.HRESULT]
    CreateProtectedResourceSession: _Callable[[_Pointer[_struct.D3D12_PROTECTED_RESOURCE_SESSION_DESC],  # pDesc
                                               _Pointer[_struct.IID],  # riid
                                               _type.c_void_p],  # ppSession
                                              _type.HRESULT]
    CreateCommittedResource1: _Callable[[_Pointer[_struct.D3D12_HEAP_PROPERTIES],  # pHeapProperties
                                         _enum.D3D12_HEAP_FLAGS,  # HeapFlags
                                         _Pointer[_struct.D3D12_RESOURCE_DESC],  # pDesc
                                         _enum.D3D12_RESOURCE_STATES,  # InitialResourceState
                                         _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                         ID3D12ProtectedResourceSession,  # pProtectedSession
                                         _Pointer[_struct.IID],  # riidResource
                                         _type.c_void_p],  # ppvResource
                                        _type.HRESULT]
    CreateHeap1: _Callable[[_Pointer[_struct.D3D12_HEAP_DESC],  # pDesc
                            ID3D12ProtectedResourceSession,  # pProtectedSession
                            _Pointer[_struct.IID],  # riid
                            _type.c_void_p],  # ppvHeap
                           _type.HRESULT]
    CreateReservedResource1: _Callable[[_Pointer[_struct.D3D12_RESOURCE_DESC],  # pDesc
                                        _enum.D3D12_RESOURCE_STATES,  # InitialState
                                        _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                        ID3D12ProtectedResourceSession,  # pProtectedSession
                                        _Pointer[_struct.IID],  # riid
                                        _type.c_void_p],  # ppvResource
                                       _type.HRESULT]
    GetResourceAllocationInfo1: _Callable[[_type.UINT,  # visibleMask
                                           _type.UINT,  # numResourceDescs
                                           _Pointer[_struct.D3D12_RESOURCE_DESC],  # pResourceDescs
                                           _Pointer[_struct.D3D12_RESOURCE_ALLOCATION_INFO1]],  # pResourceAllocationInfo1
                                          _struct.D3D12_RESOURCE_ALLOCATION_INFO]


class ID3D12LifetimeOwner(_Unknwnbase.IUnknown):
    LifetimeStateUpdated: _Callable[[_enum.D3D12_LIFETIME_STATE],  # NewState
                                    _type.c_void]


class ID3D12SwapChainAssistant(_Unknwnbase.IUnknown):
    GetLUID: _Callable[[],
                       _struct.LUID]
    GetSwapChainObject: _Callable[[_Pointer[_struct.IID],  # riid
                                   _type.c_void_p],  # ppv
                                  _type.HRESULT]
    GetCurrentResourceAndCommandQueue: _Callable[[_Pointer[_struct.IID],  # riidResource
                                                  _type.c_void_p,  # ppvResource
                                                  _Pointer[_struct.IID],  # riidQueue
                                                  _type.c_void_p],  # ppvQueue
                                                 _type.HRESULT]
    InsertImplicitSync: _Callable[[],
                                  _type.HRESULT]


class ID3D12LifetimeTracker(ID3D12DeviceChild):
    DestroyOwnedObject: _Callable[[ID3D12DeviceChild],  # pObject
                                  _type.HRESULT]


class ID3D12StateObject(ID3D12Pageable):
    pass


class ID3D12StateObjectProperties(_Unknwnbase.IUnknown):
    GetShaderIdentifier: _Callable[[_type.LPCWSTR],  # pExportName
                                   _type.c_void_p]
    GetShaderStackSize: _Callable[[_type.LPCWSTR],  # pExportName
                                  _type.UINT64]
    GetPipelineStackSize: _Callable[[],
                                    _type.UINT64]
    SetPipelineStackSize: _Callable[[_type.UINT64],  # PipelineStackSizeInBytes
                                    _type.c_void]


class ID3D12Device5(ID3D12Device4):
    CreateLifetimeTracker: _Callable[[ID3D12LifetimeOwner,  # pOwner
                                      _Pointer[_struct.IID],  # riid
                                      _type.c_void_p],  # ppvTracker
                                     _type.HRESULT]
    RemoveDevice: _Callable[[],
                            _type.c_void]
    EnumerateMetaCommands: _Callable[[_Pointer[_type.UINT],  # pNumMetaCommands
                                      _Pointer[_struct.D3D12_META_COMMAND_DESC]],  # pDescs
                                     _type.HRESULT]
    EnumerateMetaCommandParameters: _Callable[[_Pointer[_struct.GUID],  # CommandId
                                               _enum.D3D12_META_COMMAND_PARAMETER_STAGE,  # Stage
                                               _Pointer[_type.UINT],  # pTotalStructureSizeInBytes
                                               _Pointer[_type.UINT],  # pParameterCount
                                               _Pointer[_struct.D3D12_META_COMMAND_PARAMETER_DESC]],  # pParameterDescs
                                              _type.HRESULT]
    CreateMetaCommand: _Callable[[_Pointer[_struct.GUID],  # CommandId
                                  _type.UINT,  # NodeMask
                                  _type.c_void_p,  # pCreationParametersData
                                  _type.SIZE_T,  # CreationParametersDataSizeInBytes
                                  _Pointer[_struct.IID],  # riid
                                  _type.c_void_p],  # ppMetaCommand
                                 _type.HRESULT]
    CreateStateObject: _Callable[[_Pointer[_struct.D3D12_STATE_OBJECT_DESC],  # pDesc
                                  _Pointer[_struct.IID],  # riid
                                  _type.c_void_p],  # ppStateObject
                                 _type.HRESULT]
    GetRaytracingAccelerationStructurePrebuildInfo: _Callable[[_Pointer[_struct.D3D12_BUILD_RAYTRACING_ACCELERATION_STRUCTURE_INPUTS],  # pDesc
                                                               _Pointer[_struct.D3D12_RAYTRACING_ACCELERATION_STRUCTURE_PREBUILD_INFO]],  # pInfo
                                                              _type.c_void]
    CheckDriverMatchingIdentifier: _Callable[[_enum.D3D12_SERIALIZED_DATA_TYPE,  # SerializedDataType
                                              _Pointer[_struct.D3D12_SERIALIZED_DATA_DRIVER_MATCHING_IDENTIFIER]],  # pIdentifierToCheck
                                             _enum.D3D12_DRIVER_MATCHING_IDENTIFIER_STATUS]


class ID3D12DeviceRemovedExtendedDataSettings(_Unknwnbase.IUnknown):
    SetAutoBreadcrumbsEnablement: _Callable[[_enum.D3D12_DRED_ENABLEMENT],  # Enablement
                                            _type.c_void]
    SetPageFaultEnablement: _Callable[[_enum.D3D12_DRED_ENABLEMENT],  # Enablement
                                      _type.c_void]
    SetWatsonDumpEnablement: _Callable[[_enum.D3D12_DRED_ENABLEMENT],  # Enablement
                                       _type.c_void]


class ID3D12DeviceRemovedExtendedDataSettings1(ID3D12DeviceRemovedExtendedDataSettings):
    SetBreadcrumbContextEnablement: _Callable[[_enum.D3D12_DRED_ENABLEMENT],  # Enablement
                                              _type.c_void]


class ID3D12DeviceRemovedExtendedData(_Unknwnbase.IUnknown):
    GetAutoBreadcrumbsOutput: _Callable[[_Pointer[_struct.D3D12_DRED_AUTO_BREADCRUMBS_OUTPUT]],  # pOutput
                                        _type.HRESULT]
    GetPageFaultAllocationOutput: _Callable[[_Pointer[_struct.D3D12_DRED_PAGE_FAULT_OUTPUT]],  # pOutput
                                            _type.HRESULT]


class ID3D12DeviceRemovedExtendedData1(ID3D12DeviceRemovedExtendedData):
    GetAutoBreadcrumbsOutput1: _Callable[[_Pointer[_struct.D3D12_DRED_AUTO_BREADCRUMBS_OUTPUT1]],  # pOutput
                                         _type.HRESULT]
    GetPageFaultAllocationOutput1: _Callable[[_Pointer[_struct.D3D12_DRED_PAGE_FAULT_OUTPUT1]],  # pOutput
                                             _type.HRESULT]


class ID3D12DeviceRemovedExtendedData2(ID3D12DeviceRemovedExtendedData1):
    GetPageFaultAllocationOutput2: _Callable[[_Pointer[_struct.D3D12_DRED_PAGE_FAULT_OUTPUT2]],  # pOutput
                                             _type.HRESULT]
    GetDeviceState: _Callable[[],
                              _enum.D3D12_DRED_DEVICE_STATE]


class ID3D12Device6(ID3D12Device5):
    SetBackgroundProcessingMode: _Callable[[_enum.D3D12_BACKGROUND_PROCESSING_MODE,  # Mode
                                            _enum.D3D12_MEASUREMENTS_ACTION,  # MeasurementsAction
                                            _type.HANDLE,  # hEventToSignalUponCompletion
                                            _Pointer[_type.BOOL]],  # pbFurtherMeasurementsDesired
                                           _type.HRESULT]


class ID3D12ProtectedResourceSession1(ID3D12ProtectedResourceSession):
    GetDesc1: _Callable[[],
                        _struct.D3D12_PROTECTED_RESOURCE_SESSION_DESC1]


class ID3D12Device7(ID3D12Device6):
    AddToStateObject: _Callable[[_Pointer[_struct.D3D12_STATE_OBJECT_DESC],  # pAddition
                                 ID3D12StateObject,  # pStateObjectToGrowFrom
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppNewStateObject
                                _type.HRESULT]
    CreateProtectedResourceSession1: _Callable[[_Pointer[_struct.D3D12_PROTECTED_RESOURCE_SESSION_DESC1],  # pDesc
                                                _Pointer[_struct.IID],  # riid
                                                _type.c_void_p],  # ppSession
                                               _type.HRESULT]


class ID3D12Device8(ID3D12Device7):
    GetResourceAllocationInfo2: _Callable[[_type.UINT,  # visibleMask
                                           _type.UINT,  # numResourceDescs
                                           _Pointer[_struct.D3D12_RESOURCE_DESC1],  # pResourceDescs
                                           _Pointer[_struct.D3D12_RESOURCE_ALLOCATION_INFO1]],  # pResourceAllocationInfo1
                                          _struct.D3D12_RESOURCE_ALLOCATION_INFO]
    CreateCommittedResource2: _Callable[[_Pointer[_struct.D3D12_HEAP_PROPERTIES],  # pHeapProperties
                                         _enum.D3D12_HEAP_FLAGS,  # HeapFlags
                                         _Pointer[_struct.D3D12_RESOURCE_DESC1],  # pDesc
                                         _enum.D3D12_RESOURCE_STATES,  # InitialResourceState
                                         _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                         ID3D12ProtectedResourceSession,  # pProtectedSession
                                         _Pointer[_struct.IID],  # riidResource
                                         _type.c_void_p],  # ppvResource
                                        _type.HRESULT]
    CreatePlacedResource1: _Callable[[ID3D12Heap,  # pHeap
                                      _type.UINT64,  # HeapOffset
                                      _Pointer[_struct.D3D12_RESOURCE_DESC1],  # pDesc
                                      _enum.D3D12_RESOURCE_STATES,  # InitialState
                                      _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                      _Pointer[_struct.IID],  # riid
                                      _type.c_void_p],  # ppvResource
                                     _type.HRESULT]
    CreateSamplerFeedbackUnorderedAccessView: _Callable[[ID3D12Resource,  # pTargetedResource
                                                         ID3D12Resource,  # pFeedbackResource
                                                         _struct.D3D12_CPU_DESCRIPTOR_HANDLE],  # DestDescriptor
                                                        _type.c_void]
    GetCopyableFootprints1: _Callable[[_Pointer[_struct.D3D12_RESOURCE_DESC1],  # pResourceDesc
                                       _type.UINT,  # FirstSubresource
                                       _type.UINT,  # NumSubresources
                                       _type.UINT64,  # BaseOffset
                                       _Pointer[_struct.D3D12_PLACED_SUBRESOURCE_FOOTPRINT],  # pLayouts
                                       _Pointer[_type.UINT],  # pNumRows
                                       _Pointer[_type.UINT64],  # pRowSizeInBytes
                                       _Pointer[_type.UINT64]],  # pTotalBytes
                                      _type.c_void]


class ID3D12Resource1(ID3D12Resource):
    GetProtectedResourceSession: _Callable[[_Pointer[_struct.IID],  # riid
                                            _type.c_void_p],  # ppProtectedSession
                                           _type.HRESULT]


class ID3D12Resource2(ID3D12Resource1):
    GetDesc1: _Callable[[],
                        _struct.D3D12_RESOURCE_DESC1]


class ID3D12Heap1(ID3D12Heap):
    GetProtectedResourceSession: _Callable[[_Pointer[_struct.IID],  # riid
                                            _type.c_void_p],  # ppProtectedSession
                                           _type.HRESULT]


class ID3D12GraphicsCommandList3(ID3D12GraphicsCommandList2):
    SetProtectedResourceSession: _Callable[[ID3D12ProtectedResourceSession],  # pProtectedResourceSession
                                           _type.c_void]


class ID3D12MetaCommand(ID3D12Pageable):
    GetRequiredParameterResourceSize: _Callable[[_enum.D3D12_META_COMMAND_PARAMETER_STAGE,  # Stage
                                                 _type.UINT],  # ParameterIndex
                                                _type.UINT64]


class ID3D12GraphicsCommandList4(ID3D12GraphicsCommandList3):
    BeginRenderPass: _Callable[[_type.UINT,  # NumRenderTargets
                                _Pointer[_struct.D3D12_RENDER_PASS_RENDER_TARGET_DESC],  # pRenderTargets
                                _Pointer[_struct.D3D12_RENDER_PASS_DEPTH_STENCIL_DESC],  # pDepthStencil
                                _enum.D3D12_RENDER_PASS_FLAGS],  # Flags
                               _type.c_void]
    EndRenderPass: _Callable[[],
                             _type.c_void]
    InitializeMetaCommand: _Callable[[ID3D12MetaCommand,  # pMetaCommand
                                      _type.c_void_p,  # pInitializationParametersData
                                      _type.SIZE_T],  # InitializationParametersDataSizeInBytes
                                     _type.c_void]
    ExecuteMetaCommand: _Callable[[ID3D12MetaCommand,  # pMetaCommand
                                   _type.c_void_p,  # pExecutionParametersData
                                   _type.SIZE_T],  # ExecutionParametersDataSizeInBytes
                                  _type.c_void]
    BuildRaytracingAccelerationStructure: _Callable[[_Pointer[_struct.D3D12_BUILD_RAYTRACING_ACCELERATION_STRUCTURE_DESC],  # pDesc
                                                     _type.UINT,  # NumPostbuildInfoDescs
                                                     _Pointer[_struct.D3D12_RAYTRACING_ACCELERATION_STRUCTURE_POSTBUILD_INFO_DESC]],  # pPostbuildInfoDescs
                                                    _type.c_void]
    EmitRaytracingAccelerationStructurePostbuildInfo: _Callable[[_Pointer[_struct.D3D12_RAYTRACING_ACCELERATION_STRUCTURE_POSTBUILD_INFO_DESC],  # pDesc
                                                                 _type.UINT,  # NumSourceAccelerationStructures
                                                                 _Pointer[_type.D3D12_GPU_VIRTUAL_ADDRESS]],  # pSourceAccelerationStructureData
                                                                _type.c_void]
    CopyRaytracingAccelerationStructure: _Callable[[_type.D3D12_GPU_VIRTUAL_ADDRESS,  # DestAccelerationStructureData
                                                    _type.D3D12_GPU_VIRTUAL_ADDRESS,  # SourceAccelerationStructureData
                                                    _enum.D3D12_RAYTRACING_ACCELERATION_STRUCTURE_COPY_MODE],  # Mode
                                                   _type.c_void]
    SetPipelineState1: _Callable[[ID3D12StateObject],  # pStateObject
                                 _type.c_void]
    DispatchRays: _Callable[[_Pointer[_struct.D3D12_DISPATCH_RAYS_DESC]],  # pDesc
                            _type.c_void]


class ID3D12ShaderCacheSession(ID3D12DeviceChild):
    FindValue: _Callable[[_type.c_void_p,  # pKey
                          _type.UINT,  # KeySize
                          _type.c_void_p,  # pValue
                          _Pointer[_type.UINT]],  # pValueSize
                         _type.HRESULT]
    StoreValue: _Callable[[_type.c_void_p,  # pKey
                           _type.UINT,  # KeySize
                           _type.c_void_p,  # pValue
                           _type.UINT],  # ValueSize
                          _type.HRESULT]
    SetDeleteOnDestroy: _Callable[[],
                                  _type.c_void]
    GetDesc: _Callable[[],
                       _struct.D3D12_SHADER_CACHE_SESSION_DESC]


class ID3D12Device9(ID3D12Device8):
    CreateShaderCacheSession: _Callable[[_Pointer[_struct.D3D12_SHADER_CACHE_SESSION_DESC],  # pDesc
                                         _Pointer[_struct.IID],  # riid
                                         _type.c_void_p],  # ppvSession
                                        _type.HRESULT]
    ShaderCacheControl: _Callable[[_enum.D3D12_SHADER_CACHE_KIND_FLAGS,  # Kinds
                                   _enum.D3D12_SHADER_CACHE_CONTROL_FLAGS],  # Control
                                  _type.HRESULT]
    CreateCommandQueue1: _Callable[[_Pointer[_struct.D3D12_COMMAND_QUEUE_DESC],  # pDesc
                                    _Pointer[_struct.IID],  # CreatorID
                                    _Pointer[_struct.IID],  # riid
                                    _type.c_void_p],  # ppCommandQueue
                                   _type.HRESULT]


class ID3D12Device10(ID3D12Device9):
    CreateCommittedResource3: _Callable[[_Pointer[_struct.D3D12_HEAP_PROPERTIES],  # pHeapProperties
                                         _enum.D3D12_HEAP_FLAGS,  # HeapFlags
                                         _Pointer[_struct.D3D12_RESOURCE_DESC1],  # pDesc
                                         _enum.D3D12_BARRIER_LAYOUT,  # InitialLayout
                                         _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                         ID3D12ProtectedResourceSession,  # pProtectedSession
                                         _type.UINT32,  # NumCastableFormats
                                         _Pointer[_enum.DXGI_FORMAT],  # pCastableFormats
                                         _Pointer[_struct.IID],  # riidResource
                                         _type.c_void_p],  # ppvResource
                                        _type.HRESULT]
    CreatePlacedResource2: _Callable[[ID3D12Heap,  # pHeap
                                      _type.UINT64,  # HeapOffset
                                      _Pointer[_struct.D3D12_RESOURCE_DESC1],  # pDesc
                                      _enum.D3D12_BARRIER_LAYOUT,  # InitialLayout
                                      _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                      _type.UINT32,  # NumCastableFormats
                                      _Pointer[_enum.DXGI_FORMAT],  # pCastableFormats
                                      _Pointer[_struct.IID],  # riid
                                      _type.c_void_p],  # ppvResource
                                     _type.HRESULT]
    CreateReservedResource2: _Callable[[_Pointer[_struct.D3D12_RESOURCE_DESC],  # pDesc
                                        _enum.D3D12_BARRIER_LAYOUT,  # InitialLayout
                                        _Pointer[_struct.D3D12_CLEAR_VALUE],  # pOptimizedClearValue
                                        ID3D12ProtectedResourceSession,  # pProtectedSession
                                        _type.UINT32,  # NumCastableFormats
                                        _Pointer[_enum.DXGI_FORMAT],  # pCastableFormats
                                        _Pointer[_struct.IID],  # riid
                                        _type.c_void_p],  # ppvResource
                                       _type.HRESULT]


class ID3D12VirtualizationGuestDevice(_Unknwnbase.IUnknown):
    ShareWithHost: _Callable[[ID3D12DeviceChild,  # pObject
                              _Pointer[_type.HANDLE]],  # pHandle
                             _type.HRESULT]
    CreateFenceFd: _Callable[[ID3D12Fence,  # pFence
                              _type.UINT64,  # FenceValue
                              _Pointer[_type.c_int]],  # pFenceFd
                             _type.HRESULT]


class ID3D12Tools(_Unknwnbase.IUnknown):
    EnableShaderInstrumentation: _Callable[[_type.BOOL],  # bEnable
                                           _type.c_void]
    ShaderInstrumentationEnabled: _Callable[[],
                                            _type.BOOL]


class ID3D12SDKConfiguration(_Unknwnbase.IUnknown):
    SetSDKVersion: _Callable[[_type.UINT,  # SDKVersion
                              _type.LPCSTR],  # SDKPath
                             _type.HRESULT]


class ID3D12GraphicsCommandList5(ID3D12GraphicsCommandList4):
    RSSetShadingRate: _Callable[[_enum.D3D12_SHADING_RATE,  # baseShadingRate
                                 _Pointer[_enum.D3D12_SHADING_RATE_COMBINER]],  # combiners
                                _type.c_void]
    RSSetShadingRateImage: _Callable[[ID3D12Resource],  # shadingRateImage
                                     _type.c_void]


class ID3D12GraphicsCommandList6(ID3D12GraphicsCommandList5):
    DispatchMesh: _Callable[[_type.UINT,  # ThreadGroupCountX
                             _type.UINT,  # ThreadGroupCountY
                             _type.UINT],  # ThreadGroupCountZ
                            _type.c_void]


class ID3D12GraphicsCommandList7(ID3D12GraphicsCommandList6):
    Barrier: _Callable[[_type.UINT32,  # NumBarrierGroups
                        _Pointer[_struct.D3D12_BARRIER_GROUP]],  # pBarrierGroups
                       _type.c_void]
