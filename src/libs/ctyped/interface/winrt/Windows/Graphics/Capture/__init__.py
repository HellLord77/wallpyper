from __future__ import annotations

from typing import Callable as _Callable

from ..DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...UI import Composition as _Windows_UI_Composition
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDirect3D11CaptureFrame(_inspectable.IInspectable):
    get_Surface: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]],  # value
                           _type.HRESULT]
    get_SystemRelativeTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    get_ContentSize: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                               _type.HRESULT]


class IDirect3D11CaptureFramePool(_inspectable.IInspectable):
    Recreate: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice,  # device
                         _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                         _type.INT32,  # numberOfBuffers
                         _struct.Windows.Graphics.SizeInt32],  # size
                        _type.HRESULT]
    TryGetNextFrame: _Callable[[_Pointer[IDirect3D11CaptureFrame]],  # result
                               _type.HRESULT]
    add_FrameArrived: _Callable[[_Windows_Foundation.ITypedEventHandler[IDirect3D11CaptureFramePool, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    CreateCaptureSession: _Callable[[IGraphicsCaptureItem,  # item
                                     _Pointer[IGraphicsCaptureSession]],  # result
                                    _type.HRESULT]
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]


class IDirect3D11CaptureFramePoolStatics(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice,  # device
                       _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                       _type.INT32,  # numberOfBuffers
                       _struct.Windows.Graphics.SizeInt32,  # size
                       _Pointer[IDirect3D11CaptureFramePool]],  # result
                      _type.HRESULT]

    _factory = True


class IDirect3D11CaptureFramePoolStatics2(_inspectable.IInspectable):
    CreateFreeThreaded: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice,  # device
                                   _enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # pixelFormat
                                   _type.INT32,  # numberOfBuffers
                                   _struct.Windows.Graphics.SizeInt32,  # size
                                   _Pointer[IDirect3D11CaptureFramePool]],  # result
                                  _type.HRESULT]

    _factory = True


class IGraphicsCaptureAccessStatics(_inspectable.IInspectable):
    RequestAccessAsync: _Callable[[_enum.Windows.Graphics.Capture.GraphicsCaptureAccessKind,  # request
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.Authorization.AppCapabilityAccess.AppCapabilityAccessStatus]]],  # operation
                                  _type.HRESULT]

    _factory = True


class IGraphicsCaptureItem(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                        _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IGraphicsCaptureItem, _inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IGraphicsCaptureItemStatics(_inspectable.IInspectable):
    CreateFromVisual: _Callable[[_Windows_UI_Composition.IVisual,  # visual
                                 _Pointer[IGraphicsCaptureItem]],  # result
                                _type.HRESULT]

    _factory = True


class IGraphicsCaptureItemStatics2(_inspectable.IInspectable):
    TryCreateFromWindowId: _Callable[[_struct.Windows.UI.WindowId,  # windowId
                                      _Pointer[IGraphicsCaptureItem]],  # result
                                     _type.HRESULT]
    TryCreateFromDisplayId: _Callable[[_struct.Windows.Graphics.DisplayId,  # displayId
                                       _Pointer[IGraphicsCaptureItem]],  # result
                                      _type.HRESULT]

    _factory = True


class IGraphicsCapturePicker(_inspectable.IInspectable):
    PickSingleItemAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGraphicsCaptureItem]]],  # operation
                                   _type.HRESULT]


class IGraphicsCaptureSession(_inspectable.IInspectable):
    StartCapture: _Callable[[],
                            _type.HRESULT]


class IGraphicsCaptureSession2(_inspectable.IInspectable):
    get_IsCursorCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsCursorCaptureEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class IGraphicsCaptureSession3(_inspectable.IInspectable):
    get_IsBorderRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsBorderRequired: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IGraphicsCaptureSessionStatics(_inspectable.IInspectable):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]

    _factory = True
