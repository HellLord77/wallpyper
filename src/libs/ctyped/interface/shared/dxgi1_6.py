from __future__ import annotations as _

from typing import Callable as _Callable

from . import dxgi1_4 as _dxgi1_4
from . import dxgi1_5 as _dxgi1_5
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDXGIAdapter4(_dxgi1_4.IDXGIAdapter3):
    GetDesc3: _Callable[[_Pointer[_struct.DXGI_ADAPTER_DESC3]],  # pDesc
                        _type.HRESULT]


class IDXGIOutput6(_dxgi1_5.IDXGIOutput5):
    GetDesc1: _Callable[[_Pointer[_struct.DXGI_OUTPUT_DESC1]],  # pDesc
                        _type.HRESULT]
    CheckHardwareCompositionSupport: _Callable[[_Pointer[_type.UINT]],  # pFlags
                                               _type.HRESULT]


class IDXGIFactory6(_dxgi1_5.IDXGIFactory5):
    EnumAdapterByGpuPreference: _Callable[[_type.UINT,  # Adapter
                                           _enum.DXGI_GPU_PREFERENCE,  # GpuPreference
                                           _Pointer[_struct.IID],  # riid
                                           _type.c_void_p],  # ppvAdapter
                                          _type.HRESULT]


class IDXGIFactory7(IDXGIFactory6):
    RegisterAdaptersChangedEvent: _Callable[[_type.HANDLE,  # hEvent
                                             _Pointer[_type.DWORD]],  # pdwCookie
                                            _type.HRESULT]
    UnregisterAdaptersChangedEvent: _Callable[[_type.DWORD],  # dwCookie
                                              _type.HRESULT]
