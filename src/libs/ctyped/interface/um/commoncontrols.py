from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IImageList(_Unknwnbase.IUnknown):
    Add: _Callable[[_type.HBITMAP,  # hbmImage
                    _type.HBITMAP,  # hbmMask
                    _Pointer[_type.c_int]],  # pi
                   _type.HRESULT]
    ReplaceIcon: _Callable[[_type.c_int,  # i
                            _type.HICON,  # hicon
                            _Pointer[_type.c_int]],  # pi
                           _type.HRESULT]
    SetOverlayImage: _Callable[[_type.c_int,  # iImage
                                _type.c_int],  # iOverlay
                               _type.HRESULT]
    Replace: _Callable[[_type.c_int,  # i
                        _type.HBITMAP,  # hbmImage
                        _type.HBITMAP],  # hbmMask
                       _type.HRESULT]
    AddMasked: _Callable[[_type.HBITMAP,  # hbmImage
                          _type.COLORREF,  # crMask
                          _Pointer[_type.c_int]],  # pi
                         _type.HRESULT]
    Draw: _Callable[[_Pointer[_type.c_int]],  # pimldp
                    _type.HRESULT]
    Remove: _Callable[[_type.c_int],  # i
                      _type.HRESULT]
    GetIcon: _Callable[[_type.c_int,  # i
                        _type.UINT,  # flags
                        _Pointer[_type.HICON]],  # picon
                       _type.HRESULT]
    GetImageInfo: _Callable[[_type.c_int,  # i
                             _Pointer[_type.c_int]],  # pImageInfo
                            _type.HRESULT]
    Copy: _Callable[[_type.c_int,  # iDst
                     _Unknwnbase.IUnknown,  # punkSrc
                     _type.c_int,  # iSrc
                     _type.UINT],  # uFlags
                    _type.HRESULT]
    Merge: _Callable[[_type.c_int,  # i1
                      _Unknwnbase.IUnknown,  # punk2
                      _type.c_int,  # i2
                      _type.c_int,  # dx
                      _type.c_int,  # dy
                      _Pointer[_struct.IID],  # riid
                      _type.c_void_p],  # ppv
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[_struct.IID],  # riid
                      _type.c_void_p],  # ppv
                     _type.HRESULT]
    GetImageRect: _Callable[[_type.c_int,  # i
                             _Pointer[_struct.RECT]],  # prc
                            _type.HRESULT]
    GetIconSize: _Callable[[_Pointer[_type.c_int],  # cx
                            _Pointer[_type.c_int]],  # cy
                           _type.HRESULT]
    SetIconSize: _Callable[[_type.c_int,  # cx
                            _type.c_int],  # cy
                           _type.HRESULT]
    GetImageCount: _Callable[[_Pointer[_type.c_int]],  # pi
                             _type.HRESULT]
    SetImageCount: _Callable[[_type.UINT],  # uNewCount
                             _type.HRESULT]
    SetBkColor: _Callable[[_type.COLORREF,  # clrBk
                           _Pointer[_type.COLORREF]],  # pclr
                          _type.HRESULT]
    GetBkColor: _Callable[[_Pointer[_type.COLORREF]],  # pclr
                          _type.HRESULT]
    BeginDrag: _Callable[[_type.c_int,  # iTrack
                          _type.c_int,  # dxHotspot
                          _type.c_int],  # dyHotspot
                         _type.HRESULT]
    EndDrag: _Callable[[],
                       _type.HRESULT]
    DragEnter: _Callable[[_type.HWND,  # hwndLock
                          _type.c_int,  # x
                          _type.c_int],  # y
                         _type.HRESULT]
    DragLeave: _Callable[[_type.HWND],  # hwndLock
                         _type.HRESULT]
    DragMove: _Callable[[_type.c_int,  # x
                         _type.c_int],  # y
                        _type.HRESULT]
    SetDragCursorImage: _Callable[[_Unknwnbase.IUnknown,  # punk
                                   _type.c_int,  # iDrag
                                   _type.c_int,  # dxHotspot
                                   _type.c_int],  # dyHotspot
                                  _type.HRESULT]
    DragShowNolock: _Callable[[_type.BOOL],  # fShow
                              _type.HRESULT]
    GetDragImage: _Callable[[_Pointer[_struct.POINT],  # ppt
                             _Pointer[_struct.POINT],  # pptHotspot
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]
    GetItemFlags: _Callable[[_type.c_int,  # i
                             _Pointer[_type.DWORD]],  # dwFlags
                            _type.HRESULT]
    GetOverlayImage: _Callable[[_type.c_int,  # iOverlay
                                _Pointer[_type.c_int]],  # piIndex
                               _type.HRESULT]


class IImageList2(IImageList):
    Resize: _Callable[[_type.c_int,  # cxNewIconSize
                       _type.c_int],  # cyNewIconSize
                      _type.HRESULT]
    GetOriginalSize: _Callable[[_type.c_int,  # iImage
                                _type.DWORD,  # dwFlags
                                _Pointer[_type.c_int],  # pcx
                                _Pointer[_type.c_int]],  # pcy
                               _type.HRESULT]
    SetOriginalSize: _Callable[[_type.c_int,  # iImage
                                _type.c_int,  # cx
                                _type.c_int],  # cy
                               _type.HRESULT]
    SetCallback: _Callable[[_Unknwnbase.IUnknown],  # punk
                           _type.HRESULT]
    GetCallback: _Callable[[_Pointer[_struct.IID],  # riid
                            _type.c_void_p],  # ppv
                           _type.HRESULT]
    ForceImagePresent: _Callable[[_type.c_int,  # iImage
                                  _type.DWORD],  # dwFlags
                                 _type.HRESULT]
    DiscardImages: _Callable[[_type.c_int,  # iFirstImage
                              _type.c_int,  # iLastImage
                              _type.DWORD],  # dwFlags
                             _type.HRESULT]
    PreloadImages: _Callable[[_Pointer[_type.c_int]],  # pimldp
                             _type.HRESULT]
    GetStatistics: _Callable[[_Pointer[_struct.IMAGELISTSTATS]],  # pils
                             _type.HRESULT]
    Initialize: _Callable[[_type.c_int,  # cx
                           _type.c_int,  # cy
                           _type.UINT,  # flags
                           _type.c_int,  # cInitial
                           _type.c_int],  # cGrow
                          _type.HRESULT]
    Replace2: _Callable[[_type.c_int,  # i
                         _type.HBITMAP,  # hbmImage
                         _type.HBITMAP,  # hbmMask
                         _Unknwnbase.IUnknown,  # punk
                         _type.DWORD],  # dwFlags
                        _type.HRESULT]
    ReplaceFromImageList: _Callable[[_type.c_int,  # i
                                     IImageList,  # pil
                                     _type.c_int,  # iSrc
                                     _Unknwnbase.IUnknown,  # punk
                                     _type.DWORD],  # dwFlags
                                    _type.HRESULT]
