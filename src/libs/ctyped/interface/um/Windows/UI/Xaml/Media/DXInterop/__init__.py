from __future__ import annotations

from typing import Callable as _Callable

from ...... import Unknwnbase as _Unknwnbase
from .......shared import dxgi as _dxgi
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class ISurfaceImageSourceNative(_Unknwnbase.IUnknown):
    SetDevice: _Callable[[_dxgi.IDXGIDevice],  # device
                         _type.HRESULT]
    BeginDraw: _Callable[[_struct.RECT,  # updateRect
                          _Pointer[_dxgi.IDXGISurface],  # surface
                          _Pointer[_struct.POINT]],  # offset
                         _type.HRESULT]
    EndDraw: _Callable[[],
                       _type.HRESULT]


class IVirtualSurfaceUpdatesCallbackNative(_Unknwnbase.IUnknown):
    UpdatesNeeded: _Callable[[],
                             _type.HRESULT]


class IVirtualSurfaceImageSourceNative(ISurfaceImageSourceNative):
    Invalidate: _Callable[[_struct.RECT],  # updateRect
                          _type.HRESULT]
    GetUpdateRectCount: _Callable[[_Pointer[_type.DWORD]],  # count
                                  _type.HRESULT]
    GetUpdateRects: _Callable[[_Pointer[_struct.RECT],  # updates
                               _type.DWORD],  # count
                              _type.HRESULT]
    GetVisibleBounds: _Callable[[_Pointer[_struct.RECT]],  # bounds
                                _type.HRESULT]
    RegisterForUpdatesNeeded: _Callable[[IVirtualSurfaceUpdatesCallbackNative],  # callback
                                        _type.HRESULT]
    Resize: _Callable[[_type.INT,  # newWidth
                       _type.INT],  # newHeight
                      _type.HRESULT]


class ISwapChainBackgroundPanelNative(_Unknwnbase.IUnknown):
    SetSwapChain: _Callable[[_dxgi.IDXGISwapChain],  # swapChain
                            _type.HRESULT]


class ISurfaceImageSourceManagerNative(_Unknwnbase.IUnknown):
    FlushAllSurfacesWithDevice: _Callable[[_Unknwnbase.IUnknown],  # device
                                          _type.HRESULT]


class ISurfaceImageSourceNativeWithD2D(_Unknwnbase.IUnknown):
    SetDevice: _Callable[[_Unknwnbase.IUnknown],  # device
                         _type.HRESULT]
    BeginDraw: _Callable[[_Pointer[_struct.RECT],  # updateRect
                          _Pointer[_struct.IID],  # iid
                          _type.c_void_p,  # updateObject
                          _Pointer[_struct.POINT]],  # offset
                         _type.HRESULT]
    EndDraw: _Callable[[],
                       _type.HRESULT]
    SuspendDraw: _Callable[[],
                           _type.HRESULT]
    ResumeDraw: _Callable[[],
                          _type.HRESULT]


class ISwapChainPanelNative(_Unknwnbase.IUnknown):
    SetSwapChain: _Callable[[_dxgi.IDXGISwapChain],  # swapChain
                            _type.HRESULT]


class ISwapChainPanelNative2(ISwapChainPanelNative):
    SetSwapChainHandle: _Callable[[_type.HANDLE],  # swapChainHandle
                                  _type.HRESULT]
