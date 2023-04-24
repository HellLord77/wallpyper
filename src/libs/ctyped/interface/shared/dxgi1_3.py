from __future__ import annotations

from typing import Callable as _Callable

from . import dxgi as _dxgi
from . import dxgi1_2 as _dxgi1_2
from ..um import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDXGIDevice3(_dxgi1_2.IDXGIDevice2):
    Trim: _Callable[[],
                    _type.c_void]


class IDXGISwapChain2(_dxgi1_2.IDXGISwapChain1):
    SetSourceSize: _Callable[[_type.UINT,  # Width
                              _type.UINT],  # Height
                             _type.HRESULT]
    GetSourceSize: _Callable[[_Pointer[_type.UINT],  # pWidth
                              _Pointer[_type.UINT]],  # pHeight
                             _type.HRESULT]
    SetMaximumFrameLatency: _Callable[[_type.UINT],  # MaxLatency
                                      _type.HRESULT]
    GetMaximumFrameLatency: _Callable[[_Pointer[_type.UINT]],  # pMaxLatency
                                      _type.HRESULT]
    GetFrameLatencyWaitableObject: _Callable[[],
                                             _type.HANDLE]
    SetMatrixTransform: _Callable[[_Pointer[_struct.DXGI_MATRIX_3X2_F]],  # pMatrix
                                  _type.HRESULT]
    GetMatrixTransform: _Callable[[_Pointer[_struct.DXGI_MATRIX_3X2_F]],  # pMatrix
                                  _type.HRESULT]


class IDXGIOutput2(_dxgi1_2.IDXGIOutput1):
    SupportsOverlays: _Callable[[],
                                _type.BOOL]


class IDXGIFactory3(_dxgi1_2.IDXGIFactory2):
    GetCreationFlags: _Callable[[],
                                _type.UINT]


class IDXGIDecodeSwapChain(_Unknwnbase.IUnknown):
    PresentBuffer: _Callable[[_type.UINT,  # BufferToPresent
                              _type.UINT,  # SyncInterval
                              _type.UINT],  # Flags
                             _type.HRESULT]
    SetSourceRect: _Callable[[_Pointer[_struct.RECT]],  # pRect
                             _type.HRESULT]
    SetTargetRect: _Callable[[_Pointer[_struct.RECT]],  # pRect
                             _type.HRESULT]
    SetDestSize: _Callable[[_type.UINT,  # Width
                            _type.UINT],  # Height
                           _type.HRESULT]
    GetSourceRect: _Callable[[_Pointer[_struct.RECT]],  # pRect
                             _type.HRESULT]
    GetTargetRect: _Callable[[_Pointer[_struct.RECT]],  # pRect
                             _type.HRESULT]
    GetDestSize: _Callable[[_Pointer[_type.UINT],  # pWidth
                            _Pointer[_type.UINT]],  # pHeight
                           _type.HRESULT]
    SetColorSpace: _Callable[[_enum.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS],  # ColorSpace
                             _type.HRESULT]
    GetColorSpace: _Callable[[],
                             _enum.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS]


class IDXGIFactoryMedia(_Unknwnbase.IUnknown):
    CreateSwapChainForCompositionSurfaceHandle: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                                           _type.HANDLE,  # hSurface
                                                           _Pointer[_struct.DXGI_SWAP_CHAIN_DESC1],  # pDesc
                                                           _dxgi.IDXGIOutput,  # pRestrictToOutput
                                                           _Pointer[_dxgi1_2.IDXGISwapChain1]],  # ppSwapChain
                                                          _type.HRESULT]
    CreateDecodeSwapChainForCompositionSurfaceHandle: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                                                 _type.HANDLE,  # hSurface
                                                                 _Pointer[_struct.DXGI_DECODE_SWAP_CHAIN_DESC],  # pDesc
                                                                 _dxgi.IDXGIResource,  # pYuvDecodeBuffers
                                                                 _dxgi.IDXGIOutput,  # pRestrictToOutput
                                                                 _Pointer[IDXGIDecodeSwapChain]],  # ppSwapChain
                                                                _type.HRESULT]


class IDXGISwapChainMedia(_Unknwnbase.IUnknown):
    GetFrameStatisticsMedia: _Callable[[_Pointer[_struct.DXGI_FRAME_STATISTICS_MEDIA]],  # pStats
                                       _type.HRESULT]
    SetPresentDuration: _Callable[[_type.UINT],  # Duration
                                  _type.HRESULT]
    CheckPresentDurationSupport: _Callable[[_type.UINT,  # DesiredPresentDuration
                                            _Pointer[_type.UINT],  # pClosestSmallerPresentDuration
                                            _Pointer[_type.UINT]],  # pClosestLargerPresentDuration
                                           _type.HRESULT]


class IDXGIOutput3(IDXGIOutput2):
    CheckOverlaySupport: _Callable[[_enum.DXGI_FORMAT,  # EnumFormat
                                    _Unknwnbase.IUnknown,  # pConcernedDevice
                                    _Pointer[_type.UINT]],  # pFlags
                                   _type.HRESULT]
