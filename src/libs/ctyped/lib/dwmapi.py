from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# dwmapi
DwmDefWindowProc: _Callable[[_type.HWND,  # hWnd
                             _type.UINT,  # msg
                             _type.WPARAM,  # wParam
                             _type.LPARAM,  # lParam
                             _Pointer[_type.LRESULT]],  # plResult
                            _type.BOOL]
DwmEnableBlurBehindWindow: _Callable[[_type.HWND,  # hWnd
                                      _Pointer[_struct.DWM_BLURBEHIND]],  # pBlurBehind
                                     _type.HRESULT]
DwmEnableComposition: _Callable[[_type.UINT],  # uCompositionAction
                                _type.HRESULT]
DwmEnableMMCSS: _Callable[[_type.BOOL],  # fEnableMMCSS
                          _type.HRESULT]
DwmExtendFrameIntoClientArea: _Callable[[_type.HWND,  # hWnd
                                         _Pointer[_struct.MARGINS]],  # pMarInset
                                        _type.HRESULT]
DwmGetColorizationColor: _Callable[[_Pointer[_type.DWORD],  # pcrColorization
                                    _Pointer[_type.BOOL]],  # pfOpaqueBlend
                                   _type.HRESULT]
DwmGetCompositionTimingInfo: _Callable[[_type.HWND,  # hwnd
                                        _Pointer[_struct.DWM_TIMING_INFO]],  # pTimingInfo
                                       _type.HRESULT]
DwmGetWindowAttribute: _Callable[[_type.HWND,  # hwnd
                                  _type.DWORD,  # dwAttribute
                                  _type.PVOID,  # pvAttribute
                                  _type.DWORD],  # cbAttribute
                                 _type.HRESULT]
DwmIsCompositionEnabled: _Callable[[_Pointer[_type.BOOL]],  # pfEnabled
                                   _type.HRESULT]
DwmModifyPreviousDxFrameDuration: _Callable[[_type.HWND,  # hwnd
                                             _type.INT,  # cRefreshes
                                             _type.BOOL],  # fRelative
                                            _type.HRESULT]
DwmQueryThumbnailSourceSize: _Callable[[_type.HTHUMBNAIL,  # hThumbnail
                                        _Pointer[_struct.SIZE]],  # pSize
                                       _type.HRESULT]
DwmRegisterThumbnail: _Callable[[_type.HWND,  # hwndDestination
                                 _type.HWND,  # hwndSource
                                 _Pointer[_type.HTHUMBNAIL]],  # phThumbnailId
                                _type.HRESULT]
DwmSetDxFrameDuration: _Callable[[_type.HWND,  # hwnd
                                  _type.INT],  # cRefreshes
                                 _type.HRESULT]
DwmSetPresentParameters: _Callable[[_type.HWND,  # hwnd
                                    _Pointer[_struct.DWM_PRESENT_PARAMETERS]],  # pPresentParams
                                   _type.HRESULT]
DwmSetWindowAttribute: _Callable[[_type.HWND,  # hwnd
                                  _type.DWORD,  # dwAttribute
                                  _type.LPCVOID,  # pvAttribute
                                  _type.DWORD],  # cbAttribute
                                 _type.HRESULT]
DwmUnregisterThumbnail: _Callable[[_type.HTHUMBNAIL],  # hThumbnailId
                                  _type.HRESULT]
DwmUpdateThumbnailProperties: _Callable[[_type.HTHUMBNAIL,  # hThumbnailId
                                         _Pointer[_struct.DWM_THUMBNAIL_PROPERTIES]],  # ptnProperties
                                        _type.HRESULT]
DwmSetIconicThumbnail: _Callable[[_type.HWND,  # hwnd
                                  _type.HBITMAP,  # hbmp
                                  _type.DWORD],  # dwSITFlags
                                 _type.HRESULT]
DwmSetIconicLivePreviewBitmap: _Callable[[_type.HWND,  # hwnd
                                          _type.HBITMAP,  # hbmp
                                          _Pointer[_struct.POINT],  # pptClient
                                          _type.DWORD],  # dwSITFlags
                                         _type.HRESULT]
DwmInvalidateIconicBitmaps: _Callable[[_type.HWND],  # hwnd
                                      _type.HRESULT]
DwmAttachMilContent: _Callable[[_type.HWND],  # hwnd
                               _type.HRESULT]
DwmDetachMilContent: _Callable[[_type.HWND],  # hwnd
                               _type.HRESULT]
DwmFlush: _Callable[[],
                    _type.HRESULT]
DwmGetGraphicsStreamTransformHint: _Callable[[_type.UINT,  # uIndex
                                              _Pointer[_struct.MilMatrix3x2D]],  # pTransform
                                             _type.HRESULT]
DwmGetGraphicsStreamClient: _Callable[[_type.UINT,  # uIndex
                                       _Pointer[_struct.UUID]],  # pClientUuid
                                      _type.HRESULT]
DwmGetTransportAttributes: _Callable[[_Pointer[_type.BOOL],  # pfIsRemoting
                                      _Pointer[_type.BOOL],  # pfIsConnected
                                      _Pointer[_type.DWORD]],  # pDwGeneration
                                     _type.HRESULT]
DwmTransitionOwnedWindow: _Callable[[_type.HWND,  # hwnd
                                     _enum.DWMTRANSITION_OWNEDWINDOW_TARGET],  # target
                                    _type.HRESULT]
DwmRenderGesture: _Callable[[_enum.GESTURE_TYPE,  # gt
                             _type.UINT,  # cContacts
                             _Pointer[_type.DWORD],  # pdwPointerID
                             _Pointer[_struct.POINT]],  # pPoints
                            _type.HRESULT]
DwmTetherContact: _Callable[[_type.DWORD,  # dwPointerID
                             _type.BOOL,  # fEnable
                             _struct.POINT],  # ptTether
                            _type.HRESULT]
DwmShowContact: _Callable[[_type.DWORD,  # dwPointerID
                           _enum.DWM_SHOWCONTACT],  # eShowContact
                          _type.HRESULT]
DwmGetUnmetTabRequirements: _Callable[[_type.HWND,  # appWindow
                                       _Pointer[_enum.DWM_TAB_WINDOW_REQUIREMENTS]],  # value
                                      _type.HRESULT]

_WinLib(__name__)
