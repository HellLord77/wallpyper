from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import d3d11 as _d3d11
from . import d3d11_1 as _d3d11_1
from . import d3d11_3 as _d3d11_3
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D11Device4(_d3d11_3.ID3D11Device3):
    RegisterDeviceRemovedEvent: _Callable[[_type.HANDLE,  # hEvent
                                           _Pointer[_type.DWORD]],  # pdwCookie
                                          _type.HRESULT]
    UnregisterDeviceRemoved: _Callable[[_type.DWORD],  # dwCookie
                                       _type.c_void]


class ID3D11Device5(ID3D11Device4):
    OpenSharedFence: _Callable[[_type.HANDLE,  # hFence
                                _Pointer[_struct.IID],  # ReturnedInterface
                                _type.c_void_p],  # ppFence
                               _type.HRESULT]
    CreateFence: _Callable[[_type.UINT64,  # InitialValue
                            _enum.D3D11_FENCE_FLAG,  # Flags
                            _Pointer[_struct.IID],  # ReturnedInterface
                            _type.c_void_p],  # ppFence
                           _type.HRESULT]


class ID3D11Multithread(_Unknwnbase.IUnknown):
    Enter: _Callable[[],
                     _type.c_void]
    Leave: _Callable[[],
                     _type.c_void]
    SetMultithreadProtected: _Callable[[_type.BOOL],  # bMTProtect
                                       _type.BOOL]
    GetMultithreadProtected: _Callable[[],
                                       _type.BOOL]


class ID3D11VideoContext2(_d3d11_1.ID3D11VideoContext1):
    VideoProcessorSetOutputHDRMetaData: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _enum.DXGI_HDR_METADATA_TYPE,  # Type
                                                   _type.UINT,  # Size
                                                   _type.c_void_p],  # pHDRMetaData
                                                  _type.c_void]
    VideoProcessorGetOutputHDRMetaData: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _Pointer[_enum.DXGI_HDR_METADATA_TYPE],  # pType
                                                   _type.UINT,  # Size
                                                   _type.c_void_p],  # pMetaData
                                                  _type.c_void]
    VideoProcessorSetStreamHDRMetaData: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _type.UINT,  # StreamIndex
                                                   _enum.DXGI_HDR_METADATA_TYPE,  # Type
                                                   _type.UINT,  # Size
                                                   _type.c_void_p],  # pHDRMetaData
                                                  _type.c_void]
    VideoProcessorGetStreamHDRMetaData: _Callable[[_d3d11.ID3D11VideoProcessor,  # pVideoProcessor
                                                   _type.UINT,  # StreamIndex
                                                   _Pointer[_enum.DXGI_HDR_METADATA_TYPE],  # pType
                                                   _type.UINT,  # Size
                                                   _type.c_void_p],  # pMetaData
                                                  _type.c_void]


class ID3D11VideoDevice2(_d3d11_1.ID3D11VideoDevice1):
    CheckFeatureSupport: _Callable[[_enum.D3D11_FEATURE_VIDEO,  # Feature
                                    _type.c_void_p,  # pFeatureSupportData
                                    _type.UINT],  # FeatureSupportDataSize
                                   _type.HRESULT]
    NegotiateCryptoSessionKeyExchangeMT: _Callable[[_d3d11.ID3D11CryptoSession,  # pCryptoSession
                                                    _enum.D3D11_CRYPTO_SESSION_KEY_EXCHANGE_FLAGS,  # flags
                                                    _type.UINT,  # DataSize
                                                    _type.c_void_p],  # pData
                                                   _type.HRESULT]


class ID3D11VideoContext3(ID3D11VideoContext2):
    DecoderBeginFrame1: _Callable[[_d3d11.ID3D11VideoDecoder,  # pDecoder
                                   _d3d11.ID3D11VideoDecoderOutputView,  # pView
                                   _type.UINT,  # ContentKeySize
                                   _type.c_void_p,  # pContentKey
                                   _type.UINT,  # NumComponentHistograms
                                   _Pointer[_type.UINT],  # pHistogramOffsets
                                   _Pointer[_d3d11.ID3D11Buffer]],  # ppHistogramBuffers
                                  _type.HRESULT]
    SubmitDecoderBuffers2: _Callable[[_d3d11.ID3D11VideoDecoder,  # pDecoder
                                      _type.UINT,  # NumBuffers
                                      _Pointer[_struct.D3D11_VIDEO_DECODER_BUFFER_DESC2]],  # pBufferDesc
                                     _type.HRESULT]
