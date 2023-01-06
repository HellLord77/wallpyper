from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# dwmapi
DwmDefWindowProc: _Callable[[_type.HWND,
                             _type.UINT,
                             _type.WPARAM,
                             _type.LPARAM,
                             _Pointer[_type.LRESULT]],
                            _type.BOOL]
DwmEnableComposition: _Callable[[_type.UINT],
                                _type.HRESULT]
DwmEnableMMCSS: _Callable[[_type.BOOL],
                          _type.HRESULT]
DwmExtendFrameIntoClientArea: _Callable[[_type.HWND,
                                         _Pointer[_struct.MARGINS]],
                                        _type.HRESULT]
DwmGetColorizationColor: _Callable[[_Pointer[_type.DWORD],
                                    _Pointer[_type.BOOL]],
                                   _type.HRESULT]
DwmGetWindowAttribute: _Callable[[_type.HWND,
                                  _type.DWORD,
                                  _type.PVOID,
                                  _type.DWORD],
                                 _type.HRESULT]
DwmIsCompositionEnabled: _Callable[[_Pointer[_type.BOOL]],
                                   _type.HRESULT]
DwmModifyPreviousDxFrameDuration: _Callable[[_type.HWND,
                                             _type.INT,
                                             _type.BOOL],
                                            _type.HRESULT]
DwmRegisterThumbnail: _Callable[[_type.HWND,
                                 _type.HWND,
                                 _Pointer[_type.HTHUMBNAIL]],
                                _type.HRESULT]
DwmSetDxFrameDuration: _Callable[[_type.HWND,
                                  _type.INT],
                                 _type.HRESULT]
DwmSetWindowAttribute: _Callable[[_type.HWND,
                                  _type.DWORD,
                                  _type.LPCVOID,
                                  _type.DWORD],
                                 _type.HRESULT]
DwmUnregisterThumbnail: _Callable[[_type.HTHUMBNAIL],
                                  _type.HRESULT]

_WinLib(__name__)
