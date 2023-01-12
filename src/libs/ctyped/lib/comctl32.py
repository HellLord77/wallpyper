from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.um import commoncontrols as _commoncontrols
from ..interface.um import objidlbase as _objidlbase

DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                         _type.HRESULT]
# CommCtrl
InitCommonControls: _Callable[[],
                              _type.c_void]
InitCommonControlsEx: _Callable[[_Pointer[_struct.INITCOMMONCONTROLSEX]],  # picce
                                _type.BOOL]
ImageList_Create: _Callable[[_type.c_int,  # cx
                             _type.c_int,  # cy
                             _type.UINT,  # flags
                             _type.c_int,  # cInitial
                             _type.c_int],  # cGrow
                            _commoncontrols.IImageList]
ImageList_Destroy: _Callable[[_commoncontrols.IImageList],  # himl
                             _type.BOOL]
ImageList_GetImageCount: _Callable[[_commoncontrols.IImageList],  # himl
                                   _type.c_int]
ImageList_SetImageCount: _Callable[[_commoncontrols.IImageList,  # himl
                                    _type.UINT],  # uNewCount
                                   _type.BOOL]
ImageList_Add: _Callable[[_commoncontrols.IImageList,  # himl
                          _type.HBITMAP,  # hbmImage
                          _type.HBITMAP],  # hbmMask
                         _type.c_int]
ImageList_ReplaceIcon: _Callable[[_commoncontrols.IImageList,  # himl
                                  _type.c_int,  # i
                                  _type.HICON],  # hicon
                                 _type.c_int]
ImageList_SetBkColor: _Callable[[_commoncontrols.IImageList,  # himl
                                 _type.COLORREF],  # clrBk
                                _type.COLORREF]
ImageList_GetBkColor: _Callable[[_commoncontrols.IImageList],  # himl
                                _type.COLORREF]
ImageList_SetOverlayImage: _Callable[[_commoncontrols.IImageList,  # himl
                                      _type.c_int,  # iImage
                                      _type.c_int],  # iOverlay
                                     _type.BOOL]
ImageList_Draw: _Callable[[_commoncontrols.IImageList,  # himl
                           _type.c_int,  # i
                           _type.HDC,  # hdcDst
                           _type.c_int,  # x
                           _type.c_int,  # y
                           _type.UINT],  # fStyle
                          _type.BOOL]
ImageList_Replace: _Callable[[_commoncontrols.IImageList,  # himl
                              _type.c_int,  # i
                              _type.HBITMAP,  # hbmImage
                              _type.HBITMAP],  # hbmMask
                             _type.BOOL]
ImageList_AddMasked: _Callable[[_commoncontrols.IImageList,  # himl
                                _type.HBITMAP,  # hbmImage
                                _type.COLORREF],  # crMask
                               _type.c_int]
ImageList_DrawEx: _Callable[[_commoncontrols.IImageList,  # himl
                             _type.c_int,  # i
                             _type.HDC,  # hdcDst
                             _type.c_int,  # x
                             _type.c_int,  # y
                             _type.c_int,  # dx
                             _type.c_int,  # dy
                             _type.COLORREF,  # rgbBk
                             _type.COLORREF,  # rgbFg
                             _type.UINT],  # fStyle
                            _type.BOOL]
ImageList_DrawIndirect: _Callable[[_Pointer[_struct.IMAGELISTDRAWPARAMS]],  # pimldp
                                  _type.BOOL]
ImageList_Remove: _Callable[[_commoncontrols.IImageList,  # himl
                             _type.c_int],  # i
                            _type.BOOL]
ImageList_GetIcon: _Callable[[_commoncontrols.IImageList,  # himl
                              _type.c_int,  # i
                              _type.UINT],  # flags
                             _type.HICON]
ImageList_LoadImageA: _Callable[[_type.HINSTANCE,  # hi
                                 _type.LPCSTR,  # lpbmp
                                 _type.c_int,  # cx
                                 _type.c_int,  # cGrow
                                 _type.COLORREF,  # crMask
                                 _type.UINT,  # uType
                                 _type.UINT],  # uFlags
                                _commoncontrols.IImageList]
ImageList_LoadImageW: _Callable[[_type.HINSTANCE,  # hi
                                 _type.LPCWSTR,  # lpbmp
                                 _type.c_int,  # cx
                                 _type.c_int,  # cGrow
                                 _type.COLORREF,  # crMask
                                 _type.UINT,  # uType
                                 _type.UINT],  # uFlags
                                _commoncontrols.IImageList]
ImageList_Copy: _Callable[[_commoncontrols.IImageList,  # himlDst
                           _type.c_int,  # iDst
                           _commoncontrols.IImageList,  # himlSrc
                           _type.c_int,  # iSrc
                           _type.UINT],  # uFlags
                          _type.BOOL]
ImageList_BeginDrag: _Callable[[_commoncontrols.IImageList,  # himlTrack
                                _type.c_int,  # iTrack
                                _type.c_int,  # dxHotspot
                                _type.c_int],  # dyHotspot
                               _type.BOOL]
ImageList_EndDrag: _Callable[[],
                             _type.c_void]
ImageList_DragEnter: _Callable[[_type.HWND,  # hwndLock
                                _type.c_int,  # x
                                _type.c_int],  # y
                               _type.BOOL]
ImageList_DragLeave: _Callable[[_type.HWND],  # hwndLock
                               _type.BOOL]
ImageList_DragMove: _Callable[[_type.c_int,  # x
                               _type.c_int],  # y
                              _type.BOOL]
ImageList_SetDragCursorImage: _Callable[[_commoncontrols.IImageList,  # himlDrag
                                         _type.c_int,  # iDrag
                                         _type.c_int,  # dxHotspot
                                         _type.c_int],  # dyHotspot
                                        _type.BOOL]
ImageList_DragShowNolock: _Callable[[_type.BOOL],  # fShow
                                    _type.BOOL]
ImageList_GetDragImage: _Callable[[_Pointer[_struct.POINT],  # ppt
                                   _Pointer[_struct.POINT]],  # pptHotspot
                                  _commoncontrols.IImageList]
ImageList_Read: _Callable[[_objidlbase.IStream],  # pstm
                          _commoncontrols.IImageList]
ImageList_Write: _Callable[[_commoncontrols.IImageList,  # himl
                            _objidlbase.IStream],  # pstm
                           _type.BOOL]
ImageList_ReadEx: _Callable[[_type.DWORD,  # dwFlags
                             _objidlbase.IStream,  # pstm
                             _Pointer[_struct.IID],  # riid
                             _Pointer[_type.PVOID]],  # ppv
                            _type.HRESULT]
ImageList_WriteEx: _Callable[[_commoncontrols.IImageList,  # himl
                              _type.DWORD,  # dwFlags
                              _objidlbase.IStream],  # pstm
                             _type.HRESULT]
ImageList_GetIconSize: _Callable[[_commoncontrols.IImageList,  # himl
                                  _Pointer[_type.c_int],  # cx
                                  _Pointer[_type.c_int]],  # cy
                                 _type.BOOL]
ImageList_SetIconSize: _Callable[[_commoncontrols.IImageList,  # himl
                                  _type.c_int,  # cx
                                  _type.c_int],  # cy
                                 _type.BOOL]
ImageList_GetImageInfo: _Callable[[_commoncontrols.IImageList,  # himl
                                   _type.c_int,  # i
                                   _Pointer[_struct.IMAGEINFO]],  # pImageInfo
                                  _type.BOOL]
ImageList_Merge: _Callable[[_commoncontrols.IImageList,  # himl1
                            _type.c_int,  # i1
                            _commoncontrols.IImageList,  # himl2
                            _type.c_int,  # i2
                            _type.c_int,  # dx
                            _type.c_int],  # dy
                           _commoncontrols.IImageList]
ImageList_Duplicate: _Callable[[_commoncontrols.IImageList],  # himl
                               _commoncontrols.IImageList]
HIMAGELIST_QueryInterface: _Callable[[_commoncontrols.IImageList,  # himl
                                      _Pointer[_struct.IID],  # riid
                                      _type.c_void_p],  # ppv
                                     _type.HRESULT]
CreateToolbarEx: _Callable[[_type.HWND,  # hwnd
                            _type.DWORD,  # ws
                            _type.UINT,  # wID
                            _type.c_int,  # nBitmaps
                            _type.HINSTANCE,  # hBMInst
                            _type.UINT_PTR,  # wBMID
                            _Pointer[_struct.TBBUTTON],  # lpButtons
                            _type.c_int,  # iNumButtons
                            _type.c_int,  # dxButton
                            _type.c_int,  # dyButton
                            _type.c_int,  # dxBitmap
                            _type.c_int,  # dyBitmap
                            _type.UINT],  # uStructSize
                           _type.HWND]
CreateMappedBitmap: _Callable[[_type.HINSTANCE,  # hInstance
                               _type.INT_PTR,  # idBitmap
                               _type.UINT,  # wFlags
                               _Pointer[_struct.COLORMAP],  # lpColorMap
                               _type.c_int],  # iNumMaps
                              _type.HBITMAP]
DrawStatusTextA: _Callable[[_type.HDC,  # hDC
                            _Pointer[_struct.RECT],  # lprc
                            _type.LPCSTR,  # pszText
                            _type.UINT],  # uFlags
                           _type.c_void]
DrawStatusTextW: _Callable[[_type.HDC,  # hDC
                            _Pointer[_struct.RECT],  # lprc
                            _type.LPCWSTR,  # pszText
                            _type.UINT],  # uFlags
                           _type.c_void]
CreateStatusWindowA: _Callable[[_type.LONG,  # style
                                _type.LPCSTR,  # lpszText
                                _type.HWND,  # hwndParent
                                _type.UINT],  # wID
                               _type.HWND]
CreateStatusWindowW: _Callable[[_type.LONG,  # style
                                _type.LPCWSTR,  # lpszText
                                _type.HWND,  # hwndParent
                                _type.UINT],  # wID
                               _type.HWND]
MenuHelp: _Callable[[_type.UINT,  # uMsg
                     _type.WPARAM,  # wParam
                     _type.LPARAM,  # lParam
                     _type.HMENU,  # hMainMenu
                     _type.HINSTANCE,  # hInst
                     _type.HWND,  # hwndStatus
                     _Pointer[_type.UINT]],  # lpwIDs
                    _type.c_void]
ShowHideMenuCtl: _Callable[[_type.HWND,  # hWnd
                            _type.UINT_PTR,  # uFlags
                            _Pointer[_type.INT]],  # lpInfo
                           _type.BOOL]
GetEffectiveClientRect: _Callable[[_type.HWND,  # hWnd
                                   _Pointer[_struct.RECT],  # lprc
                                   _Pointer[_type.INT]],  # lpInfo
                                  _type.c_void]
MakeDragList: _Callable[[_type.HWND],  # hLB
                        _type.BOOL]
DrawInsert: _Callable[[_type.HWND,  # handParent
                       _type.HWND,  # hLB
                       _type.c_int],  # nItem
                      _type.c_void]
LBItemFromPt: _Callable[[_type.HWND,  # hLB
                         _struct.POINT,  # pt
                         _type.BOOL],  # bAutoScroll
                        _type.c_int]
CreateUpDownControl: _Callable[[_type.DWORD,  # dwStyle
                                _type.c_int,  # x
                                _type.c_int,  # y
                                _type.c_int,  # cx
                                _type.c_int,  # cy
                                _type.HWND,  # hParent
                                _type.c_int,  # nID
                                _type.HINSTANCE,  # hInst
                                _type.HWND,  # hBuddy
                                _type.c_int,  # nUpper
                                _type.c_int,  # nLower
                                _type.c_int],  # nPos
                               _type.HWND]
TaskDialogIndirect: _Callable[[_Pointer[_struct.TASKDIALOGCONFIG],  # pTaskConfig
                               _Pointer[_type.c_int],  # pnButton
                               _Pointer[_type.c_int],  # pnRadioButton
                               _Pointer[_type.BOOL]],  # pfVerificationFlagChecked
                              _type.HRESULT]
TaskDialog: _Callable[[_type.HWND,  # hwndOwner
                       _type.HINSTANCE,  # hInstance
                       _type.PCWSTR,  # pszWindowTitle
                       _type.PCWSTR,  # pszMainInstruction
                       _type.PCWSTR,  # pszContent
                       _enum.TASKDIALOG_COMMON_BUTTON_FLAGS,  # dwCommonButtons
                       _type.PCWSTR,  # pszIcon
                       _Pointer[_type.c_int]],  # pnButton
                      _type.HRESULT]
InitMUILanguage: _Callable[[_type.LANGID],  # uiLang
                           _type.c_void]
GetMUILanguage: _Callable[[],
                          _type.LANGID]
_TrackMouseEvent: _Callable[[_Pointer[_struct.TRACKMOUSEEVENT]],  # lpEventTrack
                            _type.BOOL]
FlatSB_EnableScrollBar: _Callable[[_type.HWND,
                                   _type.c_int,
                                   _type.UINT],
                                  _type.BOOL]
FlatSB_ShowScrollBar: _Callable[[_type.HWND,
                                 _type.c_int,  # code
                                 _type.BOOL],
                                _type.BOOL]
FlatSB_GetScrollRange: _Callable[[_type.HWND,
                                  _type.c_int,  # code
                                  _Pointer[_type.c_int],
                                  _Pointer[_type.c_int]],
                                 _type.BOOL]
FlatSB_GetScrollInfo: _Callable[[_type.HWND,
                                 _type.c_int,  # code
                                 _Pointer[_struct.SCROLLINFO]],
                                _type.BOOL]
FlatSB_GetScrollPos: _Callable[[_type.HWND,
                                _type.c_int],  # code
                               _type.c_int]
FlatSB_GetScrollProp: _Callable[[_type.HWND,
                                 _type.c_int,  # propIndex
                                 _Pointer[_type.INT]],
                                _type.BOOL]
FlatSB_GetScrollPropPtr: _Callable[[_type.HWND,
                                    _type.c_int,  # propIndex
                                    _Pointer[_type.INT_PTR]],
                                   _type.BOOL]
FlatSB_SetScrollPos: _Callable[[_type.HWND,
                                _type.c_int,  # code
                                _type.c_int,  # pos
                                _type.BOOL],  # fRedraw
                               _type.c_int]
FlatSB_SetScrollInfo: _Callable[[_type.HWND,
                                 _type.c_int,  # code
                                 _Pointer[_struct.SCROLLINFO],  # psi
                                 _type.BOOL],  # fRedraw
                                _type.c_int]
FlatSB_SetScrollRange: _Callable[[_type.HWND,
                                  _type.c_int,  # code
                                  _type.c_int,  # min
                                  _type.c_int,  # max
                                  _type.BOOL],  # fRedraw
                                 _type.c_int]
FlatSB_SetScrollProp: _Callable[[_type.HWND,
                                 _type.UINT,  # index
                                 _type.INT_PTR,  # newValue
                                 _type.BOOL],
                                _type.BOOL]
InitializeFlatSB: _Callable[[_type.HWND],
                            _type.BOOL]
UninitializeFlatSB: _Callable[[_type.HWND],
                              _type.HRESULT]
SetWindowSubclass: _Callable[[_type.HWND,  # hWnd
                              _type.SUBCLASSPROC,  # pfnSubclass
                              _type.UINT_PTR,  # uIdSubclass
                              _type.DWORD_PTR],  # dwRefData
                             _type.BOOL]
GetWindowSubclass: _Callable[[_type.HWND,  # hWnd
                              _type.SUBCLASSPROC,  # pfnSubclass
                              _type.UINT_PTR,  # uIdSubclass
                              _Pointer[_type.DWORD_PTR]],  # pdwRefData
                             _type.BOOL]
RemoveWindowSubclass: _Callable[[_type.HWND,  # hWnd
                                 _type.SUBCLASSPROC,  # pfnSubclass
                                 _type.UINT_PTR],  # uIdSubclass
                                _type.BOOL]
DefSubclassProc: _Callable[[_type.HWND,  # hWnd
                            _type.UINT,  # uMsg
                            _type.WPARAM,  # wParam
                            _type.LPARAM],  # lParam
                           _type.LRESULT]
LoadIconMetric: _Callable[[_type.HINSTANCE,  # hinst
                           _type.PCWSTR,  # pszName
                           _type.c_int,  # lims
                           _Pointer[_type.HICON]],  # phico
                          _type.HRESULT]
LoadIconWithScaleDown: _Callable[[_type.HINSTANCE,  # hinst
                                  _type.PCWSTR,  # pszName
                                  _type.c_int,  # cx
                                  _type.c_int,  # cy
                                  _Pointer[_type.HICON]],  # phico
                                 _type.HRESULT]
DrawShadowText: _Callable[[_type.HDC,  # hdc
                           _type.LPCWSTR,  # pszText
                           _type.UINT,  # cch
                           _Pointer[_struct.RECT],  # prc
                           _type.DWORD,  # dwFlags
                           _type.COLORREF,  # crText
                           _type.COLORREF,  # crShadow
                           _type.c_int,  # ixOffset
                           _type.c_int],  # iyOffset
                          _type.c_int]

_WinLib(__name__)
