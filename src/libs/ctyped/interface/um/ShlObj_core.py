from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from . import objidl as _objidl
from . import oleidl as _oleidl
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IExtractIconA(_Unknwnbase.IUnknown):
    GetIconLocation: _Callable[[_type.UINT,  # uFlags
                                _type.PSTR,  # pszIconFile
                                _type.UINT,  # cchMax
                                _Pointer[_type.c_int],  # piIndex
                                _Pointer[_type.UINT]],  # pwFlags
                               _type.HRESULT]
    Extract: _Callable[[_type.PCSTR,  # pszFile
                        _type.UINT,  # nIconIndex
                        _Pointer[_type.HICON],  # phiconLarge
                        _Pointer[_type.HICON],  # phiconSmall
                        _type.UINT],  # nIconSize
                       _type.HRESULT]


class IExtractIconW(_Unknwnbase.IUnknown):
    GetIconLocation: _Callable[[_type.UINT,  # uFlags
                                _type.PWSTR,  # pszIconFile
                                _type.UINT,  # cchMax
                                _Pointer[_type.c_int],  # piIndex
                                _Pointer[_type.UINT]],  # pwFlags
                               _type.HRESULT]
    Extract: _Callable[[_type.PCWSTR,  # pszFile
                        _type.UINT,  # nIconIndex
                        _Pointer[_type.HICON],  # phiconLarge
                        _Pointer[_type.HICON],  # phiconSmall
                        _type.UINT],  # nIconSize
                       _type.HRESULT]


class IShellIconOverlayManager(_Unknwnbase.IUnknown):
    GetFileOverlayInfo: _Callable[[_type.PCWSTR,  # pwszPath
                                   _type.DWORD,  # dwAttrib
                                   _Pointer[_type.c_int],  # pIndex
                                   _type.DWORD],  # dwflags
                                  _type.HRESULT]
    GetReservedOverlayInfo: _Callable[[_type.PCWSTR,  # pwszPath
                                       _type.DWORD,  # dwAttrib
                                       _Pointer[_type.c_int],  # pIndex
                                       _type.DWORD,  # dwflags
                                       _type.c_int],  # iReservedID
                                      _type.HRESULT]
    RefreshOverlayImages: _Callable[[_type.DWORD],  # dwFlags
                                    _type.HRESULT]
    LoadNonloadedOverlayIdentifiers: _Callable[[],
                                               _type.HRESULT]
    OverlayIndexFromImageIndex: _Callable[[_type.c_int,  # iImage
                                           _Pointer[_type.c_int],  # piIndex
                                           _type.BOOL],  # fAdd
                                          _type.HRESULT]


class IShellIconOverlay(_Unknwnbase.IUnknown):
    GetOverlayIndex: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                _Pointer[_type.c_int]],  # pIndex
                               _type.HRESULT]
    GetOverlayIconIndex: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                    _Pointer[_type.c_int]],  # pIconIndex
                                   _type.HRESULT]


class IShellExecuteHookA(_Unknwnbase.IUnknown):
    Execute: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOA]],  # pei
                       _type.HRESULT]


class IShellExecuteHookW(_Unknwnbase.IUnknown):
    Execute: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOW]],  # pei
                       _type.HRESULT]


class IURLSearchHook(_Unknwnbase.IUnknown):
    Translate: _Callable[[_type.PWSTR,  # pwszSearchURL
                          _type.DWORD],  # cchBufferSize
                         _type.HRESULT]


class ISearchContext(_Unknwnbase.IUnknown):
    GetSearchUrl: _Callable[[_Pointer[_type.BSTR]],  # pbstrSearchUrl
                            _type.HRESULT]
    GetSearchText: _Callable[[_Pointer[_type.BSTR]],  # pbstrSearchText
                             _type.HRESULT]
    GetSearchStyle: _Callable[[_Pointer[_type.DWORD]],  # pdwSearchStyle
                              _type.HRESULT]


class IURLSearchHook2(IURLSearchHook):
    TranslateWithSearchContext: _Callable[[_type.PWSTR,  # pwszSearchURL
                                           _type.DWORD,  # cchBufferSize
                                           ISearchContext],  # pSearchContext
                                          _type.HRESULT]


class IShellDetails(_Unknwnbase.IUnknown):
    GetDetailsOf: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                             _type.UINT,  # iColumn
                             _Pointer[_struct.SHELLDETAILS]],  # pDetails
                            _type.HRESULT]
    ColumnClick: _Callable[[_type.UINT],  # iColumn
                           _type.HRESULT]


class IObjMgr(_Unknwnbase.IUnknown):
    Append: _Callable[[_Unknwnbase.IUnknown],  # punk
                      _type.HRESULT]
    Remove: _Callable[[_Unknwnbase.IUnknown],  # punk
                      _type.HRESULT]


class IACList(_Unknwnbase.IUnknown):
    Expand: _Callable[[_type.PCWSTR],  # pszExpand
                      _type.HRESULT]


class IACList2(IACList):
    SetOptions: _Callable[[_type.DWORD],  # dwFlag
                          _type.HRESULT]
    GetOptions: _Callable[[_Pointer[_type.DWORD]],  # pdwFlag
                          _type.HRESULT]


class IProgressDialog(_Unknwnbase.IUnknown):
    StartProgressDialog: _Callable[[_type.HWND,  # hwndParent
                                    _Unknwnbase.IUnknown,  # punkEnableModless
                                    _type.DWORD,  # dwFlags
                                    _type.LPCVOID],  # pvResevered
                                   _type.HRESULT]
    StopProgressDialog: _Callable[[],
                                  _type.HRESULT]
    SetTitle: _Callable[[_type.PCWSTR],  # pwzTitle
                        _type.HRESULT]
    SetAnimation: _Callable[[_type.HINSTANCE,  # hInstAnimation
                             _type.UINT],  # idAnimation
                            _type.HRESULT]
    HasUserCancelled: _Callable[[],
                                _type.BOOL]
    SetProgress: _Callable[[_type.DWORD,  # dwCompleted
                            _type.DWORD],  # dwTotal
                           _type.HRESULT]
    SetProgress64: _Callable[[_type.ULONGLONG,  # ullCompleted
                              _type.ULONGLONG],  # ullTotal
                             _type.HRESULT]
    SetLine: _Callable[[_type.DWORD,  # dwLineNum
                        _type.PCWSTR,  # pwzString
                        _type.BOOL,  # fCompactPath
                        _type.LPCVOID],  # pvResevered
                       _type.HRESULT]
    SetCancelMsg: _Callable[[_type.PCWSTR,  # pwzCancelMsg
                             _type.LPCVOID],  # pvResevered
                            _type.HRESULT]
    Timer: _Callable[[_type.DWORD,  # dwTimerAction
                      _type.LPCVOID],  # pvResevered
                     _type.HRESULT]


class IDockingWindowSite(_oleidl.IOleWindow):
    GetBorderDW: _Callable[[_Unknwnbase.IUnknown,  # punkObj
                            _Pointer[_struct.RECT]],  # prcBorder
                           _type.HRESULT]
    RequestBorderSpaceDW: _Callable[[_Unknwnbase.IUnknown,  # punkObj
                                     _Pointer[_struct.RECT]],  # pbw
                                    _type.HRESULT]
    SetBorderSpaceDW: _Callable[[_Unknwnbase.IUnknown,  # punkObj
                                 _Pointer[_struct.RECT]],  # pbw
                                _type.HRESULT]


class IActiveDesktop(_Unknwnbase.IUnknown):
    QueryInterface: _Callable[[_Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]
    AddRef: _Callable[[],
                      _type.ULONG]
    Release: _Callable[[],
                       _type.ULONG]
    ApplyChanges: _Callable[[_type.DWORD],  # dwFlags
                            _type.HRESULT]
    GetWallpaper: _Callable[[_type.PWSTR,  # pwszWallpaper
                             _type.UINT,  # cchWallpaper
                             _type.DWORD],  # dwFlags
                            _type.HRESULT]
    SetWallpaper: _Callable[[_type.PCWSTR,  # pwszWallpaper
                             _type.DWORD],  # dwReserved
                            _type.HRESULT]
    GetWallpaperOptions: _Callable[[_Pointer[_struct.WALLPAPEROPT],  # pwpo
                                    _type.DWORD],  # dwReserved
                                   _type.HRESULT]
    SetWallpaperOptions: _Callable[[_Pointer[_struct.WALLPAPEROPT],  # pwpo
                                    _type.DWORD],  # dwReserved
                                   _type.HRESULT]
    GetPattern: _Callable[[_type.PWSTR,  # pwszPattern
                           _type.UINT,  # cchPattern
                           _type.DWORD],  # dwReserved
                          _type.HRESULT]
    SetPattern: _Callable[[_type.PCWSTR,  # pwszPattern
                           _type.DWORD],  # dwReserved
                          _type.HRESULT]
    GetDesktopItemOptions: _Callable[[_Pointer[_struct.COMPONENTSOPT],  # pco
                                      _type.DWORD],  # dwReserved
                                     _type.HRESULT]
    SetDesktopItemOptions: _Callable[[_Pointer[_struct.COMPONENTSOPT],  # pco
                                      _type.DWORD],  # dwReserved
                                     _type.HRESULT]
    AddDesktopItem: _Callable[[_Pointer[_struct.COMPONENT],  # pcomp
                               _type.DWORD],  # dwReserved
                              _type.HRESULT]
    AddDesktopItemWithUI: _Callable[[_type.HWND,  # hwnd
                                     _Pointer[_struct.COMPONENT],  # pcomp
                                     _type.DWORD],  # dwReserved
                                    _type.HRESULT]
    ModifyDesktopItem: _Callable[[_Pointer[_struct.COMPONENT],  # pcomp
                                  _type.DWORD],  # dwFlags
                                 _type.HRESULT]
    RemoveDesktopItem: _Callable[[_Pointer[_struct.COMPONENT],  # pcomp
                                  _type.DWORD],  # dwReserved
                                 _type.HRESULT]
    GetDesktopItemCount: _Callable[[_Pointer[_type.c_int],  # pcItems
                                    _type.DWORD],  # dwReserved
                                   _type.HRESULT]
    GetDesktopItem: _Callable[[_type.c_int,  # nComponent
                               _Pointer[_struct.COMPONENT],  # pcomp
                               _type.DWORD],  # dwReserved
                              _type.HRESULT]
    GetDesktopItemByID: _Callable[[_type.ULONG_PTR,  # dwID
                                   _Pointer[_struct.COMPONENT],  # pcomp
                                   _type.DWORD],  # dwReserved
                                  _type.HRESULT]
    GenerateDesktopItemHtml: _Callable[[_type.PCWSTR,  # pwszFileName
                                        _Pointer[_struct.COMPONENT],  # pcomp
                                        _type.DWORD],  # dwReserved
                                       _type.HRESULT]
    AddUrl: _Callable[[_type.HWND,  # hwnd
                       _type.PCWSTR,  # pszSource
                       _Pointer[_struct.COMPONENT],  # pcomp
                       _type.DWORD],  # dwFlags
                      _type.HRESULT]
    GetDesktopItemBySource: _Callable[[_type.PCWSTR,  # pwszSource
                                       _Pointer[_struct.COMPONENT],  # pcomp
                                       _type.DWORD],  # dwReserved
                                      _type.HRESULT]


class IShellChangeNotify(_Unknwnbase.IUnknown):
    OnChange: _Callable[[_type.LONG,  # lEvent
                         _Pointer[_struct.ITEMIDLIST],  # pidl1
                         _Pointer[_struct.ITEMIDLIST]],  # pidl2
                        _type.HRESULT]


class IQueryInfo(_Unknwnbase.IUnknown):
    GetInfoTip: _Callable[[_type.DWORD,  # dwFlags
                           _Pointer[_type.PWSTR]],  # ppwszTip
                          _type.HRESULT]
    GetInfoFlags: _Callable[[_Pointer[_type.DWORD]],  # pdwFlags
                            _type.HRESULT]


class IShellFolderViewCB(_Unknwnbase.IUnknown):
    MessageSFVCB: _Callable[[_type.UINT,  # uMsg
                             _type.WPARAM,  # wParam
                             _type.LPARAM],  # lParam
                            _type.HRESULT]


class IShellFolderView(_Unknwnbase.IUnknown):
    Rearrange: _Callable[[_type.LPARAM],  # lParamSort
                         _type.HRESULT]
    GetArrangeParam: _Callable[[_Pointer[_type.LPARAM]],  # plParamSort
                               _type.HRESULT]
    ArrangeGrid: _Callable[[],
                           _type.HRESULT]
    AutoArrange: _Callable[[],
                           _type.HRESULT]
    GetAutoArrange: _Callable[[],
                              _type.HRESULT]
    AddObject: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                          _Pointer[_type.UINT]],  # puItem
                         _type.HRESULT]
    GetObject: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]],  # ppidl
                          _type.UINT],  # uItem
                         _type.HRESULT]
    RemoveObject: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                             _Pointer[_type.UINT]],  # puItem
                            _type.HRESULT]
    GetObjectCount: _Callable[[_Pointer[_type.UINT]],  # puCount
                              _type.HRESULT]
    SetObjectCount: _Callable[[_type.UINT,  # uCount
                               _type.UINT],  # dwFlags
                              _type.HRESULT]
    UpdateObject: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlOld
                             _Pointer[_struct.ITEMIDLIST],  # pidlNew
                             _Pointer[_type.UINT]],  # puItem
                            _type.HRESULT]
    RefreshObject: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                              _Pointer[_type.UINT]],  # puItem
                             _type.HRESULT]
    SetRedraw: _Callable[[_type.BOOL],  # bRedraw
                         _type.HRESULT]
    GetSelectedCount: _Callable[[_Pointer[_type.UINT]],  # puSelected
                                _type.HRESULT]
    GetSelectedObjects: _Callable[[_Pointer[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # pppidl
                                   _Pointer[_type.UINT]],  # puItems
                                  _type.HRESULT]
    IsDropOnSource: _Callable[[_oleidl.IDropTarget],  # pDropTarget
                              _type.HRESULT]
    GetDragPoint: _Callable[[_Pointer[_struct.POINT]],  # ppt
                            _type.HRESULT]
    GetDropPoint: _Callable[[_Pointer[_struct.POINT]],  # ppt
                            _type.HRESULT]
    MoveIcons: _Callable[[_objidl.IDataObject],  # pDataObject
                         _type.HRESULT]
    SetItemPos: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                           _Pointer[_struct.POINT]],  # ppt
                          _type.HRESULT]
    IsBkDropTarget: _Callable[[_oleidl.IDropTarget],  # pDropTarget
                              _type.HRESULT]
    SetClipboard: _Callable[[_type.BOOL],  # bMove
                            _type.HRESULT]
    SetPoints: _Callable[[_objidl.IDataObject],  # pDataObject
                         _type.HRESULT]
    GetItemSpacing: _Callable[[_Pointer[_struct.ITEMSPACING]],  # pSpacing
                              _type.HRESULT]
    SetCallback: _Callable[[IShellFolderViewCB,  # pNewCB
                            _Pointer[IShellFolderViewCB]],  # ppOldCB
                           _type.HRESULT]
    Select: _Callable[[_type.UINT],  # dwFlags
                      _type.HRESULT]
    QuerySupport: _Callable[[_Pointer[_type.UINT]],  # pdwSupport
                            _type.HRESULT]
    SetAutomationObject: _Callable[[_oaidl.IDispatch],  # pdisp
                                   _type.HRESULT]


class INamedPropertyBag(_Unknwnbase.IUnknown):
    ReadPropertyNPB: _Callable[[_type.PCWSTR,  # pszBagname
                                _type.PCWSTR,  # pszPropName
                                _Pointer[_struct.PROPVARIANT]],  # pVar
                               _type.HRESULT]
    WritePropertyNPB: _Callable[[_type.PCWSTR,  # pszBagname
                                 _type.PCWSTR,  # pszPropName
                                 _Pointer[_struct.PROPVARIANT]],  # pVar
                                _type.HRESULT]
    RemovePropertyNPB: _Callable[[_type.PCWSTR,  # pszBagname
                                  _type.PCWSTR],  # pszPropName
                                 _type.HRESULT]
