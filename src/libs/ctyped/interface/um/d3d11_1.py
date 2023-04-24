from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import d3d11 as _d3d11
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D11BlendState1(_d3d11.ID3D11BlendState):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_BLEND_DESC1]],  # pDesc
                        _type.c_void]


class ID3D11RasterizerState1(_d3d11.ID3D11RasterizerState):
    GetDesc1: _Callable[[_Pointer[_struct.D3D11_RASTERIZER_DESC1]],  # pDesc
                        _type.c_void]


class ID3DDeviceContextState(_d3d11.ID3D11DeviceChild):
    pass


class ID3D11DeviceContext1(_d3d11.ID3D11DeviceContext):
    CopySubresourceRegion1: _Callable[[_d3d11.ID3D11Resource,  # pDstResource
                                       _type.UINT,  # DstSubresource
                                       _type.UINT,  # DstX
                                       _type.UINT,  # DstY
                                       _type.UINT,  # DstZ
                                       _d3d11.ID3D11Resource,  # pSrcResource
                                       _type.UINT,  # SrcSubresource
                                       _Pointer[_struct.D3D11_BOX],  # pSrcBox
                                       _type.UINT],  # CopyFlags
                                      _type.c_void]
    UpdateSubresource1: _Callable[[_d3d11.ID3D11Resource,  # pDstResource
                                   _type.UINT,  # DstSubresource
                                   _Pointer[_struct.D3D11_BOX],  # pDstBox
                                   _type.c_void_p,  # pSrcData
                                   _type.UINT,  # SrcRowPitch
                                   _type.UINT,  # SrcDepthPitch
                                   _type.UINT],  # CopyFlags
                                  _type.c_void]
    DiscardResource: _Callable[[_d3d11.ID3D11Resource],  # pResource
                               _type.c_void]
    DiscardView: _Callable[[_d3d11.ID3D11View],  # pResourceView
                           _type.c_void]
    VSSetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    HSSetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    DSSetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    GSSetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    PSSetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    CSSetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    VSGetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    HSGetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    DSGetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    GSGetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    PSGetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    CSGetConstantBuffers1: _Callable[[_type.UINT,  # StartSlot
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_d3d11.ID3D11Buffer],  # ppConstantBuffers
                                      _Pointer[_type.UINT],  # pFirstConstant
                                      _Pointer[_type.UINT]],  # pNumConstants
                                     _type.c_void]
    SwapDeviceContextState: _Callable[[ID3DDeviceContextState,  # pState
                                       _Pointer[ID3DDeviceContextState]],  # ppPreviousState
                                      _type.c_void]
    ClearView: _Callable[[_d3d11.ID3D11View,  # pView
                          _Pointer[_type.FLOAT],  # Color
                          _Pointer[_struct.D3D11_RECT],  # pRect
                          _type.UINT],  # NumRects
                         _type.c_void]
    DiscardView1: _Callable[[_d3d11.ID3D11View,  # pResourceView
                             _Pointer[_struct.D3D11_RECT],  # pRects
                             _type.UINT],  # NumRects
                            _type.c_void]


class ID3D11VideoContext1(_d3d11.ID3D11VideoContext):
    SubmitDecoderBuffers1: _Callable[[_d3d11.ID3D11VideoDecoder,  # pDecoder
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_struct.D3D11_VIDEO_DECODER_BUFFER_DESC1]],  # pBufferDesc
                                     _type.HRESULT]
    GetDataForNewHardwareKey: _Callable[[_d3d11.ID3D11CryptoSession,  # pCryptoSession
                                         _type.UINT,  # PrivateInputSize
                                         _type.c_void_p,  # pPrivatInputData
                                         _Pointer[_type.UINT64]],  # pPrivateOutputData
                                        _type.HRESULT]
    CheckCryptoSessionStatus: _Callable[[_d3d11.ID3D11CryptoSession,  # pCryptoSession
                                         _Pointer[_enum.D3D11_CRYPTO_SESSION_STATUS]],  # pStatus
                                        _type.HRESULT]
    DecoderEnableDownsampling: _Callable[[_d3d11.ID3D11VideoDecoder,  # pDecoder
                                          _enum.DXGI_COLOR_SPACE_TYPE,  # InputColorSpace
                                          _Pointer[_struct.D3D11_VIDEO_SAMPLE_DESC],  # pOutputDesc
                                          _type.UINT],  # ReferenceFrameCount
                                         _type.HRESULT]
    DecoderUpdateDownsampling: _Callable[[_d3d11.ID3D11VideoDecoder,  # pDecoder
                                          _Pointer[_struct.D3D11_VIDEO_SAMPLE_DESC]],  # pOutputDesc
                                         _type.HRESULT]
    VideoProcessorSetOutputColorSpace1: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _enum.DXGI_COLOR_SPACE_TYPE],  # ColorSpace
                                                  _type.c_void]
    VideoProcessorSetOutputShaderUsage: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _type.BOOL],  # ShaderUsage
                                                  _type.c_void]
    VideoProcessorGetOutputColorSpace1: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _Pointer[_enum.DXGI_COLOR_SPACE_TYPE]],  # pColorSpace
                                                  _type.c_void]
    VideoProcessorGetOutputShaderUsage: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _Pointer[_type.BOOL]],  # pShaderUsage
                                                  _type.c_void]
    VideoProcessorSetStreamColorSpace1: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _type.UINT,  # StreamIndex
                                                   _enum.DXGI_COLOR_SPACE_TYPE],  # ColorSpace
                                                  _type.c_void]
    VideoProcessorSetStreamMirror: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                              _type.UINT,  # StreamIndex
                                              _type.BOOL,  # Enable
                                              _type.BOOL,  # FlipHorizontal
                                              _type.BOOL],  # FlipVertical
                                             _type.c_void]
    VideoProcessorGetStreamColorSpace1: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _type.UINT,  # StreamIndex
                                                   _Pointer[_enum.DXGI_COLOR_SPACE_TYPE]],  # pColorSpace
                                                  _type.c_void]
    VideoProcessorGetStreamMirror: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                              _type.UINT,  # StreamIndex
                                              _Pointer[_type.BOOL],  # pEnable
                                              _Pointer[_type.BOOL],  # pFlipHorizontal
                                              _Pointer[_type.BOOL]],  # pFlipVertical
                                             _type.c_void]
    VideoProcessorGetBehaviorHints: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                               _type.UINT,  # OutputWidth
                                               _type.UINT,  # OutputHeight
                                               _enum.DXGI_FORMAT,  # OutputFormat
                                               _type.UINT,  # StreamCount
                                               _Pointer[_struct.D3D11_VIDEO_PROCESSOR_STREAM_BEHAVIOR_HINT],  # pStreams
                                               _Pointer[_type.UINT]],  # pBehaviorHints
                                              _type.HRESULT]


class ID3D11VideoDevice1(_d3d11.ID3D11VideoDevice):
    GetCryptoSessionPrivateDataSize: _Callable[[_Pointer[_struct.GUID],  # pCryptoType
                                                _Pointer[_struct.GUID],  # pDecoderProfile
                                                _Pointer[_struct.GUID],  # pKeyExchangeType
                                                _Pointer[_type.UINT],  # pPrivateInputSize
                                                _Pointer[_type.UINT]],  # pPrivateOutputSize
                                               _type.HRESULT]
    GetVideoDecoderCaps: _Callable[[_Pointer[_struct.GUID],  # pDecoderProfile
                                    _type.UINT,  # SampleWidth
                                    _type.UINT,  # SampleHeight
                                    _Pointer[_struct.DXGI_RATIONAL],  # pFrameRate
                                    _type.UINT,  # BitRate
                                    _Pointer[_struct.GUID],  # pCryptoType
                                    _Pointer[_type.UINT]],  # pDecoderCaps
                                   _type.HRESULT]
    CheckVideoDecoderDownsampling: _Callable[[_Pointer[_struct.D3D11_VIDEO_DECODER_DESC],  # pInputDesc
                                              _enum.DXGI_COLOR_SPACE_TYPE,  # InputColorSpace
                                              _Pointer[_struct.D3D11_VIDEO_DECODER_CONFIG],  # pInputConfig
                                              _Pointer[_struct.DXGI_RATIONAL],  # pFrameRate
                                              _Pointer[_struct.D3D11_VIDEO_SAMPLE_DESC],  # pOutputDesc
                                              _Pointer[_type.BOOL],  # pSupported
                                              _Pointer[_type.BOOL]],  # pRealTimeHint
                                             _type.HRESULT]
    RecommendVideoDecoderDownsampleParameters: _Callable[[_Pointer[_struct.D3D11_VIDEO_DECODER_DESC],  # pInputDesc
                                                          _enum.DXGI_COLOR_SPACE_TYPE,  # InputColorSpace
                                                          _Pointer[_struct.D3D11_VIDEO_DECODER_CONFIG],  # pInputConfig
                                                          _Pointer[_struct.DXGI_RATIONAL],  # pFrameRate
                                                          _Pointer[_struct.D3D11_VIDEO_SAMPLE_DESC]],  # pRecommendedOutputDesc
                                                         _type.HRESULT]


class ID3D11VideoProcessorEnumerator1(_d3d11.ID3D11VideoProcessorEnumerator):
    CheckVideoProcessorFormatConversion: _Callable[[_enum.DXGI_FORMAT,  # InputFormat
                                                    _enum.DXGI_COLOR_SPACE_TYPE,  # InputColorSpace
                                                    _enum.DXGI_FORMAT,  # OutputFormat
                                                    _enum.DXGI_COLOR_SPACE_TYPE,  # OutputColorSpace
                                                    _Pointer[_type.BOOL]],  # pSupported
                                                   _type.HRESULT]


class ID3D11Device1(_d3d11.ID3D11Device):
    GetImmediateContext1: _Callable[[_Pointer[ID3D11DeviceContext1]],  # ppImmediateContext
                                    _type.c_void]
    CreateDeferredContext1: _Callable[[_type.UINT,  # ContextFlags
                                       _Pointer[ID3D11DeviceContext1]],  # ppDeferredContext
                                      _type.HRESULT]
    CreateBlendState1: _Callable[[_Pointer[_struct.D3D11_BLEND_DESC1],  # pBlendStateDesc
                                  _Pointer[ID3D11BlendState1]],  # ppBlendState
                                 _type.HRESULT]
    CreateRasterizerState1: _Callable[[_Pointer[_struct.D3D11_RASTERIZER_DESC1],  # pRasterizerDesc
                                       _Pointer[ID3D11RasterizerState1]],  # ppRasterizerState
                                      _type.HRESULT]
    CreateDeviceContextState: _Callable[[_type.UINT,  # Flags
                                         _Pointer[_enum.D3D_FEATURE_LEVEL],  # pFeatureLevels
                                         _type.UINT,  # FeatureLevels
                                         _type.UINT,  # SDKVersion
                                         _Pointer[_struct.IID],  # EmulatedInterface
                                         _Pointer[_enum.D3D_FEATURE_LEVEL],  # pChosenFeatureLevel
                                         _Pointer[ID3DDeviceContextState]],  # ppContextState
                                        _type.HRESULT]
    OpenSharedResource1: _Callable[[_type.HANDLE,  # hResource
                                    _Pointer[_struct.IID],  # returnedInterface
                                    _type.c_void_p],  # ppResource
                                   _type.HRESULT]
    OpenSharedResourceByName: _Callable[[_type.LPCWSTR,  # lpName
                                         _type.DWORD,  # dwDesiredAccess
                                         _Pointer[_struct.IID],  # returnedInterface
                                         _type.c_void_p],  # ppResource
                                        _type.HRESULT]


class ID3DUserDefinedAnnotation(_Unknwnbase.IUnknown):
    BeginEvent: _Callable[[_type.LPCWSTR],  # Name
                          _type.INT]
    EndEvent: _Callable[[],
                        _type.INT]
    SetMarker: _Callable[[_type.LPCWSTR],  # Name
                         _type.c_void]
    GetStatus: _Callable[[],
                         _type.BOOL]
