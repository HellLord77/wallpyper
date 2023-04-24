from __future__ import annotations

from typing import Callable as _Callable

from . import dxgi1_2 as _dxgi1_2
from . import dxgi1_3 as _dxgi1_3
from ..um import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDXGISwapChain3(_dxgi1_3.IDXGISwapChain2):
    GetCurrentBackBufferIndex: _Callable[[],
                                         _type.UINT]
    CheckColorSpaceSupport: _Callable[[_enum.DXGI_COLOR_SPACE_TYPE,  # ColorSpace
                                       _Pointer[_type.UINT]],  # pColorSpaceSupport
                                      _type.HRESULT]
    SetColorSpace1: _Callable[[_enum.DXGI_COLOR_SPACE_TYPE],  # ColorSpace
                              _type.HRESULT]
    ResizeBuffers1: _Callable[[_type.UINT,  # BufferCount
                               _type.UINT,  # Width
                               _type.UINT,  # Height
                               _enum.DXGI_FORMAT,  # Format
                               _type.UINT,  # SwapChainFlags
                               _Pointer[_type.UINT],  # pCreationNodeMask
                               _Pointer[_Unknwnbase.IUnknown]],  # ppPresentQueue
                              _type.HRESULT]


class IDXGIOutput4(_dxgi1_3.IDXGIOutput3):
    CheckOverlayColorSpaceSupport: _Callable[[_enum.DXGI_FORMAT,  # Format
                                              _enum.DXGI_COLOR_SPACE_TYPE,  # ColorSpace
                                              _Unknwnbase.IUnknown,  # pConcernedDevice
                                              _Pointer[_type.UINT]],  # pFlags
                                             _type.HRESULT]


class IDXGIFactory4(_dxgi1_3.IDXGIFactory3):
    EnumAdapterByLuid: _Callable[[_struct.LUID,  # AdapterLuid
                                  _Pointer[_struct.IID],  # riid
                                  _type.c_void_p],  # ppvAdapter
                                 _type.HRESULT]
    EnumWarpAdapter: _Callable[[_Pointer[_struct.IID],  # riid
                                _type.c_void_p],  # ppvAdapter
                               _type.HRESULT]


class IDXGIAdapter3(_dxgi1_2.IDXGIAdapter2):
    RegisterHardwareContentProtectionTeardownStatusEvent: _Callable[[_type.HANDLE,  # hEvent
                                                                     _Pointer[_type.DWORD]],  # pdwCookie
                                                                    _type.HRESULT]
    UnregisterHardwareContentProtectionTeardownStatus: _Callable[[_type.DWORD],  # dwCookie
                                                                 _type.c_void]
    QueryVideoMemoryInfo: _Callable[[_type.UINT,  # NodeIndex
                                     _enum.DXGI_MEMORY_SEGMENT_GROUP,  # MemorySegmentGroup
                                     _Pointer[_struct.DXGI_QUERY_VIDEO_MEMORY_INFO]],  # pVideoMemoryInfo
                                    _type.HRESULT]
    SetVideoMemoryReservation: _Callable[[_type.UINT,  # NodeIndex
                                          _enum.DXGI_MEMORY_SEGMENT_GROUP,  # MemorySegmentGroup
                                          _type.UINT64],  # Reservation
                                         _type.HRESULT]
    RegisterVideoMemoryBudgetChangeNotificationEvent: _Callable[[_type.HANDLE,  # hEvent
                                                                 _Pointer[_type.DWORD]],  # pdwCookie
                                                                _type.HRESULT]
    UnregisterVideoMemoryBudgetChangeNotification: _Callable[[_type.DWORD],  # dwCookie
                                                             _type.c_void]
