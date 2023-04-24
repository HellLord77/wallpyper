from __future__ import annotations

from typing import Callable as _Callable

from . import ObjectArray as _ObjectArray
from . import StructuredQueryCondition as _StructuredQueryCondition
from . import Unknwnbase as _Unknwnbase
from . import comcat as _comcat
from . import commoncontrols as _commoncontrols
from . import oaidl as _oaidl
from . import objidl as _objidl
from . import objidlbase as _objidlbase
from . import oleidl as _oleidl
from . import propsys as _propsys
from . import servprov as _servprov
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IContextMenu(_Unknwnbase.IUnknown):
    QueryContextMenu: _Callable[[_type.HMENU,  # hmenu
                                 _type.UINT,  # indexMenu
                                 _type.UINT,  # idCmdFirst
                                 _type.UINT,  # idCmdLast
                                 _type.UINT],  # uFlags
                                _type.HRESULT]
    InvokeCommand: _Callable[[_Pointer[_struct.CMINVOKECOMMANDINFO]],  # pici
                             _type.HRESULT]
    GetCommandString: _Callable[[_type.UINT_PTR,  # idCmd
                                 _type.UINT,  # uType
                                 _Pointer[_type.UINT],  # pReserved
                                 _Pointer[_type.CHAR],  # pszName
                                 _type.UINT],  # cchMax
                                _type.HRESULT]


class IContextMenu2(IContextMenu):
    HandleMenuMsg: _Callable[[_type.UINT,  # uMsg
                              _type.WPARAM,  # wParam
                              _type.LPARAM],  # lParam
                             _type.HRESULT]


class IContextMenu3(IContextMenu2):
    HandleMenuMsg2: _Callable[[_type.UINT,  # uMsg
                               _type.WPARAM,  # wParam
                               _type.LPARAM,  # lParam
                               _Pointer[_type.LRESULT]],  # plResult
                              _type.HRESULT]


class IExecuteCommand(_Unknwnbase.IUnknown):
    SetKeyState: _Callable[[_type.DWORD],  # grfKeyState
                           _type.HRESULT]
    SetParameters: _Callable[[_type.LPCWSTR],  # pszParameters
                             _type.HRESULT]
    SetPosition: _Callable[[_struct.POINT],  # pt
                           _type.HRESULT]
    SetShowWindow: _Callable[[_type.c_int],  # nShow
                             _type.HRESULT]
    SetNoShowUI: _Callable[[_type.BOOL],  # fNoShowUI
                           _type.HRESULT]
    SetDirectory: _Callable[[_type.LPCWSTR],  # pszDirectory
                            _type.HRESULT]
    Execute: _Callable[[],
                       _type.HRESULT]


class IPersistFolder(_objidl.IPersist):
    Initialize: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidl
                          _type.HRESULT]


class IRunnableTask(_Unknwnbase.IUnknown):
    Run: _Callable[[],
                   _type.HRESULT]
    Kill: _Callable[[_type.BOOL],  # bWait
                    _type.HRESULT]
    Suspend: _Callable[[],
                       _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    IsRunning: _Callable[[],
                         _type.ULONG]


class IShellTaskScheduler(_Unknwnbase.IUnknown):
    AddTask: _Callable[[IRunnableTask,  # prt
                        _Pointer[_struct.TASKOWNERID],  # rtoid
                        _type.DWORD_PTR,  # lParam
                        _type.DWORD],  # dwPriority
                       _type.HRESULT]
    RemoveTasks: _Callable[[_Pointer[_struct.TASKOWNERID],  # rtoid
                            _type.DWORD_PTR,  # lParam
                            _type.BOOL],  # bWaitIfRunning
                           _type.HRESULT]
    CountTasks: _Callable[[_Pointer[_struct.TASKOWNERID]],  # rtoid
                          _type.UINT]
    Status: _Callable[[_type.DWORD,  # dwReleaseStatus
                       _type.DWORD],  # dwThreadTimeout
                      _type.HRESULT]


class IPersistFolder2(IPersistFolder):
    GetCurFolder: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                            _type.HRESULT]


class IPersistFolder3(IPersistFolder2):
    InitializeEx: _Callable[[_objidl.IBindCtx,  # pbc
                             _Pointer[_struct.ITEMIDLIST],  # pidlRoot
                             _Pointer[_struct.PERSIST_FOLDER_TARGET_INFO]],  # ppfti
                            _type.HRESULT]
    GetFolderTargetInfo: _Callable[[_Pointer[_struct.PERSIST_FOLDER_TARGET_INFO]],  # ppfti
                                   _type.HRESULT]


class IPersistIDList(_objidl.IPersist):
    SetIDList: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidl
                         _type.HRESULT]
    GetIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                         _type.HRESULT]


class IEnumIDList(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_Pointer[_struct.ITEMIDLIST]],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumIDList]],  # ppenum
                     _type.HRESULT]


class IEnumFullIDList(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_Pointer[_struct.ITEMIDLIST]],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumFullIDList]],  # ppenum
                     _type.HRESULT]


class IFileSyncMergeHandler(_Unknwnbase.IUnknown):
    Merge: _Callable[[_type.LPCWSTR,  # localFilePath
                      _type.LPCWSTR,  # serverFilePath
                      _Pointer[_enum.MERGE_UPDATE_STATUS]],  # updateStatus
                     _type.HRESULT]
    ShowResolveConflictUIAsync: _Callable[[_type.LPCWSTR,  # localFilePath
                                           _type.HMONITOR],  # monitorToDisplayOn
                                          _type.HRESULT]


class IObjectWithFolderEnumMode(_Unknwnbase.IUnknown):
    SetMode: _Callable[[_enum.FOLDER_ENUM_MODE],  # feMode
                       _type.HRESULT]
    GetMode: _Callable[[_Pointer[_enum.FOLDER_ENUM_MODE]],  # pfeMode
                       _type.HRESULT]


class IParseAndCreateItem(_Unknwnbase.IUnknown):
    SetItem: _Callable[[IShellItem],  # psi
                       _type.HRESULT]
    GetItem: _Callable[[_Pointer[_struct.IID],  # riid
                        _type.c_void_p],  # ppv
                       _type.HRESULT]


class IShellFolder(_Unknwnbase.IUnknown):
    ParseDisplayName: _Callable[[_type.HWND,  # hwnd
                                 _objidl.IBindCtx,  # pbc
                                 _type.LPWSTR,  # pszDisplayName
                                 _Pointer[_type.ULONG],  # pchEaten
                                 _Pointer[_Pointer[_struct.ITEMIDLIST]],  # ppidl
                                 _Pointer[_type.ULONG]],  # pdwAttributes
                                _type.HRESULT]
    EnumObjects: _Callable[[_type.HWND,  # hwnd
                            _type.SHCONTF,  # grfFlags
                            _Pointer[IEnumIDList]],  # ppenumIDList
                           _type.HRESULT]
    BindToObject: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                             _objidl.IBindCtx,  # pbc
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]
    BindToStorage: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                              _objidl.IBindCtx,  # pbc
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppv
                             _type.HRESULT]
    CompareIDs: _Callable[[_type.LPARAM,  # lParam
                           _Pointer[_struct.ITEMIDLIST],  # pidl1
                           _Pointer[_struct.ITEMIDLIST]],  # pidl2
                          _type.HRESULT]
    CreateViewObject: _Callable[[_type.HWND,  # hwndOwner
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppv
                                _type.HRESULT]
    GetAttributesOf: _Callable[[_type.UINT,  # cidl
                                _Pointer[_Pointer[_struct.ITEMIDLIST]],  # apidl
                                _Pointer[_type.SFGAOF]],  # rgfInOut
                               _type.HRESULT]
    GetUIObjectOf: _Callable[[_type.HWND,  # hwndOwner
                              _type.UINT,  # cidl
                              _Pointer[_Pointer[_struct.ITEMIDLIST]],  # apidl
                              _Pointer[_struct.IID],  # riid
                              _Pointer[_type.UINT],  # rgfReserved
                              _type.c_void_p],  # ppv
                             _type.HRESULT]
    GetDisplayNameOf: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                 _type.SHGDNF,  # uFlags
                                 _Pointer[_struct.STRRET]],  # pName
                                _type.HRESULT]
    SetNameOf: _Callable[[_type.HWND,  # hwnd
                          _Pointer[_struct.ITEMIDLIST],  # pidl
                          _type.LPCWSTR,  # pszName
                          _type.SHGDNF,  # uFlags
                          _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidlOut
                         _type.HRESULT]


class IEnumExtraSearch(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.EXTRASEARCH],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumExtraSearch]],  # ppenum
                     _type.HRESULT]


class IShellFolder2(IShellFolder):
    GetDefaultSearchGUID: _Callable[[_Pointer[_struct.GUID]],  # pguid
                                    _type.HRESULT]
    EnumSearches: _Callable[[_Pointer[IEnumExtraSearch]],  # ppenum
                            _type.HRESULT]
    GetDefaultColumn: _Callable[[_type.DWORD,  # dwRes
                                 _Pointer[_type.ULONG],  # pSort
                                 _Pointer[_type.ULONG]],  # pDisplay
                                _type.HRESULT]
    GetDefaultColumnState: _Callable[[_type.UINT,  # iColumn
                                      _Pointer[_type.SHCOLSTATEF]],  # pcsFlags
                                     _type.HRESULT]
    GetDetailsEx: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                             _Pointer[_struct.SHCOLUMNID],  # pscid
                             _Pointer[_struct.VARIANT]],  # pv
                            _type.HRESULT]
    GetDetailsOf: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                             _type.UINT,  # iColumn
                             _Pointer[_struct.SHELLDETAILS]],  # psd
                            _type.HRESULT]
    MapColumnToSCID: _Callable[[_type.UINT,  # iColumn
                                _Pointer[_struct.SHCOLUMNID]],  # pscid
                               _type.HRESULT]


class IShellView(_oleidl.IOleWindow):
    TranslateAcceleratorA: _Callable[[_Pointer[_struct.MSG]],  # pmsg
                                     _type.HRESULT]
    EnableModeless: _Callable[[_type.BOOL],  # fEnable
                              _type.HRESULT]
    UIActivate: _Callable[[_type.UINT],  # uState
                          _type.HRESULT]
    Refresh: _Callable[[],
                       _type.HRESULT]
    CreateViewWindow: _Callable[[IShellView,  # psvPrevious
                                 _Pointer[_struct.FOLDERSETTINGS],  # pfs
                                 IShellBrowser,  # psb
                                 _Pointer[_struct.RECT],  # prcView
                                 _Pointer[_type.HWND]],  # phWnd
                                _type.HRESULT]
    DestroyViewWindow: _Callable[[],
                                 _type.HRESULT]
    GetCurrentInfo: _Callable[[_Pointer[_struct.FOLDERSETTINGS]],  # pfs
                              _type.HRESULT]
    AddPropertySheetPages: _Callable
    SaveViewState: _Callable[[],
                             _type.HRESULT]
    SelectItem: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlItem
                           _type.SVSIF],  # uFlags
                          _type.HRESULT]
    GetItemObject: _Callable[[_type.UINT,  # uItem
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppv
                             _type.HRESULT]


class IShellView2(IShellView):
    GetView: _Callable[[_Pointer[_struct.SHELLVIEWID],  # pvid
                        _type.ULONG],  # uView
                       _type.HRESULT]
    CreateViewWindow2: _Callable[[_Pointer[_struct.SV2CVW2_PARAMS]],  # lpParams
                                 _type.HRESULT]
    HandleRename: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidlNew
                            _type.HRESULT]
    SelectAndPositionItem: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlItem
                                      _type.UINT,  # uFlags
                                      _Pointer[_struct.POINT]],  # ppt
                                     _type.HRESULT]


class IFolderView(_Unknwnbase.IUnknown):
    GetCurrentViewMode: _Callable[[_Pointer[_type.UINT]],  # pViewMode
                                  _type.HRESULT]
    SetCurrentViewMode: _Callable[[_type.UINT],  # ViewMode
                                  _type.HRESULT]
    GetFolder: _Callable[[_Pointer[_struct.IID],  # riid
                          _type.c_void_p],  # ppv
                         _type.HRESULT]
    Item: _Callable[[_type.c_int,  # iItemIndex
                     _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                    _type.HRESULT]
    ItemCount: _Callable[[_type.UINT,  # uFlags
                          _Pointer[_type.c_int]],  # pcItems
                         _type.HRESULT]
    Items: _Callable[[_type.UINT,  # uFlags
                      _Pointer[_struct.IID],  # riid
                      _type.c_void_p],  # ppv
                     _type.HRESULT]
    GetSelectionMarkedItem: _Callable[[_Pointer[_type.c_int]],  # piItem
                                      _type.HRESULT]
    GetFocusedItem: _Callable[[_Pointer[_type.c_int]],  # piItem
                              _type.HRESULT]
    GetItemPosition: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                _Pointer[_struct.POINT]],  # ppt
                               _type.HRESULT]
    GetSpacing: _Callable[[_Pointer[_struct.POINT]],  # ppt
                          _type.HRESULT]
    GetDefaultSpacing: _Callable[[_Pointer[_struct.POINT]],  # ppt
                                 _type.HRESULT]
    GetAutoArrange: _Callable[[],
                              _type.HRESULT]
    SelectItem: _Callable[[_type.c_int,  # iItem
                           _type.DWORD],  # dwFlags
                          _type.HRESULT]
    SelectAndPositionItems: _Callable[[_type.UINT,  # cidl
                                       _Pointer[_Pointer[_struct.ITEMIDLIST]],  # apidl
                                       _Pointer[_struct.POINT],  # apt
                                       _type.DWORD],  # dwFlags
                                      _type.HRESULT]


class IFolderView2(IFolderView):
    SetGroupBy: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                           _type.BOOL],  # fAscending
                          _type.HRESULT]
    GetGroupBy: _Callable[[_Pointer[_struct.PROPERTYKEY],  # pkey
                           _Pointer[_type.BOOL]],  # pfAscending
                          _type.HRESULT]
    SetViewProperty: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                _Pointer[_struct.PROPERTYKEY],  # propkey
                                _Pointer[_struct.PROPVARIANT]],  # propvar
                               _type.HRESULT]
    GetViewProperty: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                _Pointer[_struct.PROPERTYKEY],  # propkey
                                _Pointer[_struct.PROPVARIANT]],  # ppropvar
                               _type.HRESULT]
    SetTileViewProperties: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                      _type.LPCWSTR],  # pszPropList
                                     _type.HRESULT]
    SetExtendedTileViewProperties: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                              _type.LPCWSTR],  # pszPropList
                                             _type.HRESULT]
    SetText: _Callable[[_enum.FVTEXTTYPE,  # iType
                        _type.LPCWSTR],  # pwszText
                       _type.HRESULT]
    SetCurrentFolderFlags: _Callable[[_type.DWORD,  # dwMask
                                      _type.DWORD],  # dwFlags
                                     _type.HRESULT]
    GetCurrentFolderFlags: _Callable[[_Pointer[_type.DWORD]],  # pdwFlags
                                     _type.HRESULT]
    GetSortColumnCount: _Callable[[_Pointer[_type.c_int]],  # pcColumns
                                  _type.HRESULT]
    SetSortColumns: _Callable[[_Pointer[_struct.SORTCOLUMN],  # rgSortColumns
                               _type.c_int],  # cColumns
                              _type.HRESULT]
    GetSortColumns: _Callable[[_Pointer[_struct.SORTCOLUMN],  # rgSortColumns
                               _type.c_int],  # cColumns
                              _type.HRESULT]
    GetItem: _Callable[[_type.c_int,  # iItem
                        _Pointer[_struct.IID],  # riid
                        _type.c_void_p],  # ppv
                       _type.HRESULT]
    GetVisibleItem: _Callable[[_type.c_int,  # iStart
                               _type.BOOL,  # fPrevious
                               _Pointer[_type.c_int]],  # piItem
                              _type.HRESULT]
    GetSelectedItem: _Callable[[_type.c_int,  # iStart
                                _Pointer[_type.c_int]],  # piItem
                               _type.HRESULT]
    GetSelection: _Callable[[_type.BOOL,  # fNoneImpliesFolder
                             _Pointer[IShellItemArray]],  # ppsia
                            _type.HRESULT]
    GetSelectionState: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                  _Pointer[_type.DWORD]],  # pdwFlags
                                 _type.HRESULT]
    InvokeVerbOnSelection: _Callable[[_type.LPCSTR],  # pszVerb
                                     _type.HRESULT]
    SetViewModeAndIconSize: _Callable[[_enum.FOLDERVIEWMODE,  # uViewMode
                                       _type.c_int],  # iImageSize
                                      _type.HRESULT]
    GetViewModeAndIconSize: _Callable[[_Pointer[_enum.FOLDERVIEWMODE],  # puViewMode
                                       _Pointer[_type.c_int]],  # piImageSize
                                      _type.HRESULT]
    SetGroupSubsetCount: _Callable[[_type.UINT],  # cVisibleRows
                                   _type.HRESULT]
    GetGroupSubsetCount: _Callable[[_Pointer[_type.UINT]],  # pcVisibleRows
                                   _type.HRESULT]
    SetRedraw: _Callable[[_type.BOOL],  # fRedrawOn
                         _type.HRESULT]
    IsMoveInSameFolder: _Callable[[],
                                  _type.HRESULT]
    DoRename: _Callable[[],
                        _type.HRESULT]


class IFolderViewSettings(_Unknwnbase.IUnknown):
    GetColumnPropertyList: _Callable[[_Pointer[_struct.IID],  # riid
                                      _type.c_void_p],  # ppv
                                     _type.HRESULT]
    GetGroupByProperty: _Callable[[_Pointer[_struct.PROPERTYKEY],  # pkey
                                   _Pointer[_type.BOOL]],  # pfGroupAscending
                                  _type.HRESULT]
    GetViewMode: _Callable[[_Pointer[_enum.FOLDERLOGICALVIEWMODE]],  # plvm
                           _type.HRESULT]
    GetIconSize: _Callable[[_Pointer[_type.UINT]],  # puIconSize
                           _type.HRESULT]
    GetFolderFlags: _Callable[[_Pointer[_enum.FOLDERFLAGS],  # pfolderMask
                               _Pointer[_enum.FOLDERFLAGS]],  # pfolderFlags
                              _type.HRESULT]
    GetSortColumns: _Callable[[_Pointer[_struct.SORTCOLUMN],  # rgSortColumns
                               _type.UINT,  # cColumnsIn
                               _Pointer[_type.UINT]],  # pcColumnsOut
                              _type.HRESULT]
    GetGroupSubsetCount: _Callable[[_Pointer[_type.UINT]],  # pcVisibleRows
                                   _type.HRESULT]


class IInitializeNetworkFolder(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                           _Pointer[_struct.ITEMIDLIST],  # pidlTarget
                           _type.UINT,  # uDisplayType
                           _type.LPCWSTR,  # pszResName
                           _type.LPCWSTR],  # pszProvider
                          _type.HRESULT]


class INetworkFolderInternal(_Unknwnbase.IUnknown):
    GetResourceDisplayType: _Callable[[_Pointer[_type.UINT]],  # displayType
                                      _type.HRESULT]
    GetIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # idList
                         _type.HRESULT]
    GetProvider: _Callable[[_type.UINT,  # itemIdCount
                            _Pointer[_Pointer[_struct.ITEMIDLIST]],  # itemIds
                            _type.UINT,  # providerMaxLength
                            _type.LPWSTR],  # provider
                           _type.HRESULT]


class IPreviewHandlerVisuals(_Unknwnbase.IUnknown):
    SetBackgroundColor: _Callable[[_type.COLORREF],  # color
                                  _type.HRESULT]
    SetFont: _Callable[[_Pointer[_struct.LOGFONTW]],  # plf
                       _type.HRESULT]
    SetTextColor: _Callable[[_type.COLORREF],  # color
                            _type.HRESULT]


class ICommDlgBrowser(_Unknwnbase.IUnknown):
    OnDefaultCommand: _Callable[[IShellView],  # ppshv
                                _type.HRESULT]
    OnStateChange: _Callable[[IShellView,  # ppshv
                              _type.ULONG],  # uChange
                             _type.HRESULT]
    IncludeObject: _Callable[[IShellView,  # ppshv
                              _Pointer[_struct.ITEMIDLIST]],  # pidl
                             _type.HRESULT]


class ICommDlgBrowser2(ICommDlgBrowser):
    Notify: _Callable[[IShellView,  # ppshv
                       _type.DWORD],  # dwNotifyType
                      _type.HRESULT]
    GetDefaultMenuText: _Callable[[IShellView,  # ppshv
                                   _type.LPWSTR,  # pszText
                                   _type.c_int],  # cchMax
                                  _type.HRESULT]
    GetViewFlags: _Callable[[_Pointer[_type.DWORD]],  # pdwFlags
                            _type.HRESULT]


class IColumnManager(_Unknwnbase.IUnknown):
    SetColumnInfo: _Callable[[_Pointer[_struct.PROPERTYKEY],  # propkey
                              _Pointer[_struct.CM_COLUMNINFO]],  # pcmci
                             _type.HRESULT]
    GetColumnInfo: _Callable[[_Pointer[_struct.PROPERTYKEY],  # propkey
                              _Pointer[_struct.CM_COLUMNINFO]],  # pcmci
                             _type.HRESULT]
    GetColumnCount: _Callable[[_enum.CM_ENUM_FLAGS,  # dwFlags
                               _Pointer[_type.UINT]],  # puCount
                              _type.HRESULT]
    GetColumns: _Callable[[_enum.CM_ENUM_FLAGS,  # dwFlags
                           _Pointer[_struct.PROPERTYKEY],  # rgkeyOrder
                           _type.UINT],  # cColumns
                          _type.HRESULT]
    SetColumns: _Callable[[_Pointer[_struct.PROPERTYKEY],  # rgkeyOrder
                           _type.UINT],  # cVisible
                          _type.HRESULT]


class IFolderFilterSite(_Unknwnbase.IUnknown):
    SetFilter: _Callable[[_Unknwnbase.IUnknown],  # punk
                         _type.HRESULT]


class IFolderFilter(_Unknwnbase.IUnknown):
    ShouldShow: _Callable[[IShellFolder,  # psf
                           _Pointer[_struct.ITEMIDLIST],  # pidlFolder
                           _Pointer[_struct.ITEMIDLIST]],  # pidlItem
                          _type.HRESULT]
    GetEnumFlags: _Callable[[IShellFolder,  # psf
                             _Pointer[_struct.ITEMIDLIST],  # pidlFolder
                             _Pointer[_type.HWND],  # phwnd
                             _Pointer[_type.DWORD]],  # pgrfFlags
                            _type.HRESULT]


class IInputObjectSite(_Unknwnbase.IUnknown):
    OnFocusChangeIS: _Callable[[_Unknwnbase.IUnknown,  # punkObj
                                _type.BOOL],  # fSetFocus
                               _type.HRESULT]


class IInputObject(_Unknwnbase.IUnknown):
    UIActivateIO: _Callable[[_type.BOOL,  # fActivate
                             _Pointer[_struct.MSG]],  # pMsg
                            _type.HRESULT]
    HasFocusIO: _Callable[[],
                          _type.HRESULT]
    TranslateAcceleratorIO: _Callable[[_Pointer[_struct.MSG]],  # pMsg
                                      _type.HRESULT]


class IInputObject2(IInputObject):
    TranslateAcceleratorGlobal: _Callable[[_Pointer[_struct.MSG]],  # pMsg
                                          _type.HRESULT]


class IShellIcon(_Unknwnbase.IUnknown):
    GetIconOf: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                          _type.UINT,  # flags
                          _Pointer[_type.c_int]],  # pIconIndex
                         _type.HRESULT]


class IShellBrowser(_oleidl.IOleWindow):
    InsertMenusSB: _Callable[[_type.HMENU,  # hmenuShared
                              _Pointer[_struct.OLEMENUGROUPWIDTHS]],  # lpMenuWidths
                             _type.HRESULT]
    SetMenuSB: _Callable[[_type.HMENU,  # hmenuShared
                          _type.HOLEMENU,  # holemenuRes
                          _type.HWND],  # hwndActiveObject
                         _type.HRESULT]
    RemoveMenusSB: _Callable[[_type.HMENU],  # hmenuShared
                             _type.HRESULT]
    SetStatusTextSB: _Callable[[_type.LPCWSTR],  # pszStatusText
                               _type.HRESULT]
    EnableModelessSB: _Callable[[_type.BOOL],  # fEnable
                                _type.HRESULT]
    TranslateAcceleratorSB: _Callable[[_Pointer[_struct.MSG],  # pmsg
                                       _type.WORD],  # wID
                                      _type.HRESULT]
    BrowseObject: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                             _type.UINT],  # wFlags
                            _type.HRESULT]
    GetViewStateStream: _Callable[[_type.DWORD,  # grfMode
                                   _Pointer[_objidlbase.IStream]],  # ppStrm
                                  _type.HRESULT]
    GetControlWindow: _Callable[[_type.UINT,  # id
                                 _Pointer[_type.HWND]],  # phwnd
                                _type.HRESULT]
    SendControlMsg: _Callable[[_type.UINT,  # id
                               _type.UINT,  # uMsg
                               _type.WPARAM,  # wParam
                               _type.LPARAM,  # lParam
                               _Pointer[_type.LRESULT]],  # pret
                              _type.HRESULT]
    QueryActiveShellView: _Callable[[_Pointer[IShellView]],  # ppshv
                                    _type.HRESULT]
    OnViewWindowActive: _Callable[[IShellView],  # pshv
                                  _type.HRESULT]
    SetToolbarItems: _Callable[[_Pointer[_struct.TBBUTTON],  # lpButtons
                                _type.UINT,  # nButtons
                                _type.UINT],  # uFlags
                               _type.HRESULT]


class IProfferService(_Unknwnbase.IUnknown):
    ProfferService: _Callable[[_Pointer[_struct.GUID],  # serviceId
                               _servprov.IServiceProvider,  # serviceProvider
                               _Pointer[_type.DWORD]],  # cookie
                              _type.HRESULT]
    RevokeService: _Callable[[_type.DWORD],  # cookie
                             _type.HRESULT]


class IGetServiceIds(_Unknwnbase.IUnknown):
    GetServiceIds: _Callable[[_Pointer[_type.ULONG],  # serviceIdCount
                              _Pointer[_Pointer[_struct.GUID]]],  # serviceIds
                             _type.HRESULT]


class IShellItem(_Unknwnbase.IUnknown):
    BindToHandler: _Callable[[_objidl.IBindCtx,  # pbc
                              _Pointer[_struct.GUID],  # bhid
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppv
                             _type.HRESULT]
    GetParent: _Callable[[_Pointer[IShellItem]],  # ppsi
                         _type.HRESULT]
    GetDisplayName: _Callable[[_enum.SIGDN,  # sigdnName
                               _Pointer[_type.LPWSTR]],  # ppszName
                              _type.HRESULT]
    GetAttributes: _Callable[[_type.SFGAOF,  # sfgaoMask
                              _Pointer[_type.SFGAOF]],  # psfgaoAttribs
                             _type.HRESULT]
    Compare: _Callable[[IShellItem,  # psi
                        _type.SICHINTF,  # hint
                        _Pointer[_type.c_int]],  # piOrder
                       _type.HRESULT]


class IShellItem2(IShellItem):
    GetPropertyStore: _Callable[[_enum.GETPROPERTYSTOREFLAGS,  # flags
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppv
                                _type.HRESULT]
    GetPropertyStoreWithCreateObject: _Callable[[_enum.GETPROPERTYSTOREFLAGS,  # flags
                                                 _Unknwnbase.IUnknown,  # punkCreateObject
                                                 _Pointer[_struct.IID],  # riid
                                                 _type.c_void_p],  # ppv
                                                _type.HRESULT]
    GetPropertyStoreForKeys: _Callable[[_Pointer[_struct.PROPERTYKEY],  # rgKeys
                                        _type.UINT,  # cKeys
                                        _enum.GETPROPERTYSTOREFLAGS,  # flags
                                        _Pointer[_struct.IID],  # riid
                                        _type.c_void_p],  # ppv
                                       _type.HRESULT]
    GetPropertyDescriptionList: _Callable[[_Pointer[_struct.PROPERTYKEY],  # keyType
                                           _Pointer[_struct.IID],  # riid
                                           _type.c_void_p],  # ppv
                                          _type.HRESULT]
    Update: _Callable[[_objidl.IBindCtx],  # pbc
                      _type.HRESULT]
    GetProperty: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                            _Pointer[_struct.PROPVARIANT]],  # ppropvar
                           _type.HRESULT]
    GetCLSID: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                         _Pointer[_struct.CLSID]],  # pclsid
                        _type.HRESULT]
    GetFileTime: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                            _Pointer[_struct.FILETIME]],  # pft
                           _type.HRESULT]
    GetInt32: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                         _Pointer[_type.c_int]],  # pi
                        _type.HRESULT]
    GetString: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                          _Pointer[_type.LPWSTR]],  # ppsz
                         _type.HRESULT]
    GetUInt32: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                          _Pointer[_type.ULONG]],  # pui
                         _type.HRESULT]
    GetUInt64: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                          _Pointer[_type.ULONGLONG]],  # pull
                         _type.HRESULT]
    GetBool: _Callable[[_Pointer[_struct.PROPERTYKEY],  # key
                        _Pointer[_type.BOOL]],  # pf
                       _type.HRESULT]


class IShellItemImageFactory(_Unknwnbase.IUnknown):
    GetImage: _Callable[[_struct.SIZE,  # size
                         _type.SIIGBF,  # flags
                         _Pointer[_type.HBITMAP]],  # phbm
                        _type.HRESULT]


class IEnumShellItems(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[IShellItem],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumShellItems]],  # ppenum
                     _type.HRESULT]


class ITransferAdviseSink(_Unknwnbase.IUnknown):
    UpdateProgress: _Callable[[_type.ULONGLONG,  # ullSizeCurrent
                               _type.ULONGLONG,  # ullSizeTotal
                               _type.c_int,  # nFilesCurrent
                               _type.c_int,  # nFilesTotal
                               _type.c_int,  # nFoldersCurrent
                               _type.c_int],  # nFoldersTotal
                              _type.HRESULT]
    UpdateTransferState: _Callable[[_type.TRANSFER_ADVISE_STATE],  # ts
                                   _type.HRESULT]
    ConfirmOverwrite: _Callable[[IShellItem,  # psiSource
                                 IShellItem,  # psiDestParent
                                 _type.LPCWSTR],  # pszName
                                _type.HRESULT]
    ConfirmEncryptionLoss: _Callable[[IShellItem],  # psiSource
                                     _type.HRESULT]
    FileFailure: _Callable[[IShellItem,  # psi
                            _type.LPCWSTR,  # pszItem
                            _type.HRESULT,  # hrError
                            _type.LPWSTR,  # pszRename
                            _type.ULONG],  # cchRename
                           _type.HRESULT]
    SubStreamFailure: _Callable[[IShellItem,  # psi
                                 _type.LPCWSTR,  # pszStreamName
                                 _type.HRESULT],  # hrError
                                _type.HRESULT]
    PropertyFailure: _Callable[[IShellItem,  # psi
                                _Pointer[_struct.PROPERTYKEY],  # pkey
                                _type.HRESULT],  # hrError
                               _type.HRESULT]


class ITransferSource(_Unknwnbase.IUnknown):
    Advise: _Callable[[ITransferAdviseSink,  # psink
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]
    SetProperties: _Callable[[_propsys.IPropertyChangeArray],  # pproparray
                             _type.HRESULT]
    OpenItem: _Callable[[IShellItem,  # psi
                         _type.TRANSFER_SOURCE_FLAGS,  # flags
                         _Pointer[_struct.IID],  # riid
                         _type.c_void_p],  # ppv
                        _type.HRESULT]
    MoveItem: _Callable[[IShellItem,  # psi
                         IShellItem,  # psiParentDst
                         _type.LPCWSTR,  # pszNameDst
                         _type.TRANSFER_SOURCE_FLAGS,  # flags
                         _Pointer[IShellItem]],  # ppsiNew
                        _type.HRESULT]
    RecycleItem: _Callable[[IShellItem,  # psiSource
                            IShellItem,  # psiParentDest
                            _type.TRANSFER_SOURCE_FLAGS,  # flags
                            _Pointer[IShellItem]],  # ppsiNewDest
                           _type.HRESULT]
    RemoveItem: _Callable[[IShellItem,  # psiSource
                           _type.TRANSFER_SOURCE_FLAGS],  # flags
                          _type.HRESULT]
    RenameItem: _Callable[[IShellItem,  # psiSource
                           _type.LPCWSTR,  # pszNewName
                           _type.TRANSFER_SOURCE_FLAGS,  # flags
                           _Pointer[IShellItem]],  # ppsiNewDest
                          _type.HRESULT]
    LinkItem: _Callable[[IShellItem,  # psiSource
                         IShellItem,  # psiParentDest
                         _type.LPCWSTR,  # pszNewName
                         _type.TRANSFER_SOURCE_FLAGS,  # flags
                         _Pointer[IShellItem]],  # ppsiNewDest
                        _type.HRESULT]
    ApplyPropertiesToItem: _Callable[[IShellItem,  # psiSource
                                      _Pointer[IShellItem]],  # ppsiNew
                                     _type.HRESULT]
    GetDefaultDestinationName: _Callable[[IShellItem,  # psiSource
                                          IShellItem,  # psiParentDest
                                          _Pointer[_type.LPWSTR]],  # ppszDestinationName
                                         _type.HRESULT]
    EnterFolder: _Callable[[IShellItem],  # psiChildFolderDest
                           _type.HRESULT]
    LeaveFolder: _Callable[[IShellItem],  # psiChildFolderDest
                           _type.HRESULT]


class IEnumResources(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.SHELL_ITEM_RESOURCE],  # psir
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumResources]],  # ppenumr
                     _type.HRESULT]


class IShellItemResources(_Unknwnbase.IUnknown):
    GetAttributes: _Callable[[_Pointer[_type.DWORD]],  # pdwAttributes
                             _type.HRESULT]
    GetSize: _Callable[[_Pointer[_type.ULONGLONG]],  # pullSize
                       _type.HRESULT]
    GetTimes: _Callable[[_Pointer[_struct.FILETIME],  # pftCreation
                         _Pointer[_struct.FILETIME],  # pftWrite
                         _Pointer[_struct.FILETIME]],  # pftAccess
                        _type.HRESULT]
    SetTimes: _Callable[[_Pointer[_struct.FILETIME],  # pftCreation
                         _Pointer[_struct.FILETIME],  # pftWrite
                         _Pointer[_struct.FILETIME]],  # pftAccess
                        _type.HRESULT]
    GetResourceDescription: _Callable[[_Pointer[_struct.SHELL_ITEM_RESOURCE],  # pcsir
                                       _Pointer[_type.LPWSTR]],  # ppszDescription
                                      _type.HRESULT]
    EnumResources: _Callable[[_Pointer[IEnumResources]],  # ppenumr
                             _type.HRESULT]
    SupportsResource: _Callable[[_Pointer[_struct.SHELL_ITEM_RESOURCE]],  # pcsir
                                _type.HRESULT]
    OpenResource: _Callable[[_Pointer[_struct.SHELL_ITEM_RESOURCE],  # pcsir
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]
    CreateResource: _Callable[[_Pointer[_struct.SHELL_ITEM_RESOURCE],  # pcsir
                               _Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]
    MarkForDelete: _Callable[[],
                             _type.HRESULT]


class ITransferDestination(_Unknwnbase.IUnknown):
    Advise: _Callable[[ITransferAdviseSink,  # psink
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]
    CreateItem: _Callable[[_type.LPCWSTR,  # pszName
                           _type.DWORD,  # dwAttributes
                           _type.ULONGLONG,  # ullSize
                           _type.TRANSFER_SOURCE_FLAGS,  # flags
                           _Pointer[_struct.IID],  # riidItem
                           _type.c_void_p,  # ppvItem
                           _Pointer[_struct.IID],  # riidResources
                           _type.c_void_p],  # ppvResources
                          _type.HRESULT]


class IFileOperationProgressSink(_Unknwnbase.IUnknown):
    StartOperations: _Callable[[],
                               _type.HRESULT]
    FinishOperations: _Callable[[_type.HRESULT],  # hrResult
                                _type.HRESULT]
    PreRenameItem: _Callable[[_type.DWORD,  # dwFlags
                              IShellItem,  # psiItem
                              _type.LPCWSTR],  # pszNewName
                             _type.HRESULT]
    PostRenameItem: _Callable[[_type.DWORD,  # dwFlags
                               IShellItem,  # psiItem
                               _type.LPCWSTR,  # pszNewName
                               _type.HRESULT,  # hrRename
                               IShellItem],  # psiNewlyCreated
                              _type.HRESULT]
    PreMoveItem: _Callable[[_type.DWORD,  # dwFlags
                            IShellItem,  # psiItem
                            IShellItem,  # psiDestinationFolder
                            _type.LPCWSTR],  # pszNewName
                           _type.HRESULT]
    PostMoveItem: _Callable[[_type.DWORD,  # dwFlags
                             IShellItem,  # psiItem
                             IShellItem,  # psiDestinationFolder
                             _type.LPCWSTR,  # pszNewName
                             _type.HRESULT,  # hrMove
                             IShellItem],  # psiNewlyCreated
                            _type.HRESULT]
    PreCopyItem: _Callable[[_type.DWORD,  # dwFlags
                            IShellItem,  # psiItem
                            IShellItem,  # psiDestinationFolder
                            _type.LPCWSTR],  # pszNewName
                           _type.HRESULT]
    PostCopyItem: _Callable[[_type.DWORD,  # dwFlags
                             IShellItem,  # psiItem
                             IShellItem,  # psiDestinationFolder
                             _type.LPCWSTR,  # pszNewName
                             _type.HRESULT,  # hrCopy
                             IShellItem],  # psiNewlyCreated
                            _type.HRESULT]
    PreDeleteItem: _Callable[[_type.DWORD,  # dwFlags
                              IShellItem],  # psiItem
                             _type.HRESULT]
    PostDeleteItem: _Callable[[_type.DWORD,  # dwFlags
                               IShellItem,  # psiItem
                               _type.HRESULT,  # hrDelete
                               IShellItem],  # psiNewlyCreated
                              _type.HRESULT]
    PreNewItem: _Callable[[_type.DWORD,  # dwFlags
                           IShellItem,  # psiDestinationFolder
                           _type.LPCWSTR],  # pszNewName
                          _type.HRESULT]
    PostNewItem: _Callable[[_type.DWORD,  # dwFlags
                            IShellItem,  # psiDestinationFolder
                            _type.LPCWSTR,  # pszNewName
                            _type.LPCWSTR,  # pszTemplateName
                            _type.DWORD,  # dwFileAttributes
                            _type.HRESULT,  # hrNew
                            IShellItem],  # psiNewItem
                           _type.HRESULT]
    UpdateProgress: _Callable[[_type.UINT,  # iWorkTotal
                               _type.UINT],  # iWorkSoFar
                              _type.HRESULT]
    ResetTimer: _Callable[[],
                          _type.HRESULT]
    PauseTimer: _Callable[[],
                          _type.HRESULT]
    ResumeTimer: _Callable[[],
                           _type.HRESULT]


class IShellItemArray(_Unknwnbase.IUnknown):
    BindToHandler: _Callable[[_objidl.IBindCtx,  # pbc
                              _Pointer[_struct.GUID],  # bhid
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppvOut
                             _type.HRESULT]
    GetPropertyStore: _Callable[[_enum.GETPROPERTYSTOREFLAGS,  # flags
                                 _Pointer[_struct.IID],  # riid
                                 _type.c_void_p],  # ppv
                                _type.HRESULT]
    GetPropertyDescriptionList: _Callable[[_Pointer[_struct.PROPERTYKEY],  # keyType
                                           _Pointer[_struct.IID],  # riid
                                           _type.c_void_p],  # ppv
                                          _type.HRESULT]
    GetAttributes: _Callable[[_enum.SIATTRIBFLAGS,  # AttribFlags
                              _type.SFGAOF,  # sfgaoMask
                              _Pointer[_type.SFGAOF]],  # psfgaoAttribs
                             _type.HRESULT]
    GetCount: _Callable[[_Pointer[_type.DWORD]],  # pdwNumItems
                        _type.HRESULT]
    GetItemAt: _Callable[[_type.DWORD,  # dwIndex
                          _Pointer[IShellItem]],  # ppsi
                         _type.HRESULT]
    EnumItems: _Callable[[_Pointer[IEnumShellItems]],  # ppenumShellItems
                         _type.HRESULT]


class IInitializeWithItem(_Unknwnbase.IUnknown):
    Initialize: _Callable[[IShellItem,  # psi
                           _type.DWORD],  # grfMode
                          _type.HRESULT]


class IObjectWithSelection(_Unknwnbase.IUnknown):
    SetSelection: _Callable[[IShellItemArray],  # psia
                            _type.HRESULT]
    GetSelection: _Callable[[_Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]


class IObjectWithBackReferences(_Unknwnbase.IUnknown):
    RemoveBackReferences: _Callable[[],
                                    _type.HRESULT]


class IPropertyUI(_Unknwnbase.IUnknown):
    ParsePropertyName: _Callable[[_type.LPCWSTR,  # pszName
                                  _Pointer[_struct.FMTID],  # pfmtid
                                  _Pointer[_type.PROPID],  # ppid
                                  _Pointer[_type.ULONG]],  # pchEaten
                                 _type.HRESULT]
    GetCannonicalName: _Callable[[_Pointer[_struct.IID],  # fmtid
                                  _type.PROPID,  # pid
                                  _type.LPWSTR,  # pwszText
                                  _type.DWORD],  # cchText
                                 _type.HRESULT]
    GetDisplayName: _Callable[[_Pointer[_struct.IID],  # fmtid
                               _type.PROPID,  # pid
                               _type.PROPERTYUI_NAME_FLAGS,  # flags
                               _type.LPWSTR,  # pwszText
                               _type.DWORD],  # cchText
                              _type.HRESULT]
    GetPropertyDescription: _Callable[[_Pointer[_struct.IID],  # fmtid
                                       _type.PROPID,  # pid
                                       _type.LPWSTR,  # pwszText
                                       _type.DWORD],  # cchText
                                      _type.HRESULT]
    GetDefaultWidth: _Callable[[_Pointer[_struct.IID],  # fmtid
                                _type.PROPID,  # pid
                                _Pointer[_type.ULONG]],  # pcxChars
                               _type.HRESULT]
    GetFlags: _Callable[[_Pointer[_struct.IID],  # fmtid
                         _type.PROPID,  # pid
                         _Pointer[_type.PROPERTYUI_FLAGS]],  # pflags
                        _type.HRESULT]
    FormatForDisplay: _Callable[[_Pointer[_struct.IID],  # fmtid
                                 _type.PROPID,  # pid
                                 _Pointer[_struct.PROPVARIANT],  # ppropvar
                                 _type.PROPERTYUI_FORMAT_FLAGS,  # puiff
                                 _type.LPWSTR,  # pwszText
                                 _type.DWORD],  # cchText
                                _type.HRESULT]
    GetHelpInfo: _Callable[[_Pointer[_struct.IID],  # fmtid
                            _type.PROPID,  # pid
                            _type.LPWSTR,  # pwszHelpFile
                            _type.DWORD,  # cch
                            _Pointer[_type.UINT]],  # puHelpID
                           _type.HRESULT]


class ICategoryProvider(_Unknwnbase.IUnknown):
    CanCategorizeOnSCID: _Callable[[_Pointer[_struct.SHCOLUMNID]],  # pscid
                                   _type.HRESULT]
    GetDefaultCategory: _Callable[[_Pointer[_struct.GUID],  # pguid
                                   _Pointer[_struct.SHCOLUMNID]],  # pscid
                                  _type.HRESULT]
    GetCategoryForSCID: _Callable[[_Pointer[_struct.SHCOLUMNID],  # pscid
                                   _Pointer[_struct.GUID]],  # pguid
                                  _type.HRESULT]
    EnumCategories: _Callable[[_Pointer[_comcat.IEnumGUID]],  # penum
                              _type.HRESULT]
    GetCategoryName: _Callable[[_Pointer[_struct.GUID],  # pguid
                                _type.LPWSTR,  # pszName
                                _type.UINT],  # cch
                               _type.HRESULT]
    CreateCategory: _Callable[[_Pointer[_struct.GUID],  # pguid
                               _Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]


class ICategorizer(_Unknwnbase.IUnknown):
    GetDescription: _Callable[[_type.LPWSTR,  # pszDesc
                               _type.UINT],  # cch
                              _type.HRESULT]
    GetCategory: _Callable[[_type.UINT,  # cidl
                            _Pointer[_Pointer[_struct.ITEMIDLIST]],  # apidl
                            _Pointer[_type.DWORD]],  # rgCategoryIds
                           _type.HRESULT]
    GetCategoryInfo: _Callable[[_type.DWORD,  # dwCategoryId
                                _Pointer[_struct.CATEGORY_INFO]],  # pci
                               _type.HRESULT]
    CompareCategory: _Callable[[_enum.CATSORT_FLAGS,  # csfFlags
                                _type.DWORD,  # dwCategoryId1
                                _type.DWORD],  # dwCategoryId2
                               _type.HRESULT]


class IDropTargetHelper(_Unknwnbase.IUnknown):
    DragEnter: _Callable[[_type.HWND,  # hwndTarget
                          _objidl.IDataObject,  # pDataObject
                          _Pointer[_struct.POINT],  # ppt
                          _type.DWORD],  # dwEffect
                         _type.HRESULT]
    DragLeave: _Callable[[],
                         _type.HRESULT]
    DragOver: _Callable[[_Pointer[_struct.POINT],  # ppt
                         _type.DWORD],  # dwEffect
                        _type.HRESULT]
    Drop: _Callable[[_objidl.IDataObject,  # pDataObject
                     _Pointer[_struct.POINT],  # ppt
                     _type.DWORD],  # dwEffect
                    _type.HRESULT]
    Show: _Callable[[_type.BOOL],  # fShow
                    _type.HRESULT]


class IDragSourceHelper(_Unknwnbase.IUnknown):
    InitializeFromBitmap: _Callable[[_Pointer[_struct.SHDRAGIMAGE],  # pshdi
                                     _objidl.IDataObject],  # pDataObject
                                    _type.HRESULT]
    InitializeFromWindow: _Callable[[_type.HWND,  # hwnd
                                     _Pointer[_struct.POINT],  # ppt
                                     _objidl.IDataObject],  # pDataObject
                                    _type.HRESULT]


class IShellLinkA(_Unknwnbase.IUnknown):
    GetPath: _Callable[[_type.LPSTR,  # pszFile
                        _type.c_int,  # cch
                        _Pointer[_struct.WIN32_FIND_DATAA],  # pfd
                        _type.DWORD],  # fFlags
                       _type.HRESULT]
    GetIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                         _type.HRESULT]
    SetIDList: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidl
                         _type.HRESULT]
    GetDescription: _Callable[[_type.LPSTR,  # pszName
                               _type.c_int],  # cch
                              _type.HRESULT]
    SetDescription: _Callable[[_type.LPCSTR],  # pszName
                              _type.HRESULT]
    GetWorkingDirectory: _Callable[[_type.LPSTR,  # pszDir
                                    _type.c_int],  # cch
                                   _type.HRESULT]
    SetWorkingDirectory: _Callable[[_type.LPCSTR],  # pszDir
                                   _type.HRESULT]
    GetArguments: _Callable[[_type.LPSTR,  # pszArgs
                             _type.c_int],  # cch
                            _type.HRESULT]
    SetArguments: _Callable[[_type.LPCSTR],  # pszArgs
                            _type.HRESULT]
    GetHotkey: _Callable[[_Pointer[_type.WORD]],  # pwHotkey
                         _type.HRESULT]
    SetHotkey: _Callable[[_type.WORD],  # wHotkey
                         _type.HRESULT]
    GetShowCmd: _Callable[[_Pointer[_type.c_int]],  # piShowCmd
                          _type.HRESULT]
    SetShowCmd: _Callable[[_type.c_int],  # iShowCmd
                          _type.HRESULT]
    GetIconLocation: _Callable[[_type.LPSTR,  # pszIconPath
                                _type.c_int,  # cch
                                _Pointer[_type.c_int]],  # piIcon
                               _type.HRESULT]
    SetIconLocation: _Callable[[_type.LPCSTR,  # pszIconPath
                                _type.c_int],  # iIcon
                               _type.HRESULT]
    SetRelativePath: _Callable[[_type.LPCSTR,  # pszPathRel
                                _type.DWORD],  # dwReserved
                               _type.HRESULT]
    Resolve: _Callable[[_type.HWND,  # hwnd
                        _type.DWORD],  # fFlags
                       _type.HRESULT]
    SetPath: _Callable[[_type.LPCSTR],  # pszFile
                       _type.HRESULT]


class IShellLinkW(_Unknwnbase.IUnknown):
    GetPath: _Callable[[_type.LPWSTR,  # pszFile
                        _type.c_int,  # cch
                        _Pointer[_struct.WIN32_FIND_DATAW],  # pfd
                        _type.DWORD],  # fFlags
                       _type.HRESULT]
    GetIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                         _type.HRESULT]
    SetIDList: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidl
                         _type.HRESULT]
    GetDescription: _Callable[[_type.LPWSTR,  # pszName
                               _type.c_int],  # cch
                              _type.HRESULT]
    SetDescription: _Callable[[_type.LPCWSTR],  # pszName
                              _type.HRESULT]
    GetWorkingDirectory: _Callable[[_type.LPWSTR,  # pszDir
                                    _type.c_int],  # cch
                                   _type.HRESULT]
    SetWorkingDirectory: _Callable[[_type.LPCWSTR],  # pszDir
                                   _type.HRESULT]
    GetArguments: _Callable[[_type.LPWSTR,  # pszArgs
                             _type.c_int],  # cch
                            _type.HRESULT]
    SetArguments: _Callable[[_type.LPCWSTR],  # pszArgs
                            _type.HRESULT]
    GetHotkey: _Callable[[_Pointer[_type.WORD]],  # pwHotkey
                         _type.HRESULT]
    SetHotkey: _Callable[[_type.WORD],  # wHotkey
                         _type.HRESULT]
    GetShowCmd: _Callable[[_Pointer[_type.c_int]],  # piShowCmd
                          _type.HRESULT]
    SetShowCmd: _Callable[[_type.c_int],  # iShowCmd
                          _type.HRESULT]
    GetIconLocation: _Callable[[_type.LPWSTR,  # pszIconPath
                                _type.c_int,  # cch
                                _Pointer[_type.c_int]],  # piIcon
                               _type.HRESULT]
    SetIconLocation: _Callable[[_type.LPCWSTR,  # pszIconPath
                                _type.c_int],  # iIcon
                               _type.HRESULT]
    SetRelativePath: _Callable[[_type.LPCWSTR,  # pszPathRel
                                _type.DWORD],  # dwReserved
                               _type.HRESULT]
    Resolve: _Callable[[_type.HWND,  # hwnd
                        _type.DWORD],  # fFlags
                       _type.HRESULT]
    SetPath: _Callable[[_type.LPCWSTR],  # pszFile
                       _type.HRESULT]


class IShellLinkDataList(_Unknwnbase.IUnknown):
    AddDataBlock: _Callable[[_type.c_void_p],  # pDataBlock
                            _type.HRESULT]
    CopyDataBlock: _Callable[[_type.DWORD,  # dwSig
                              _type.c_void_p],  # ppDataBlock
                             _type.HRESULT]
    RemoveDataBlock: _Callable[[_type.DWORD],  # dwSig
                               _type.HRESULT]
    GetFlags: _Callable[[_Pointer[_type.DWORD]],  # pdwFlags
                        _type.HRESULT]
    SetFlags: _Callable[[_type.DWORD],  # dwFlags
                        _type.HRESULT]


class IResolveShellLink(_Unknwnbase.IUnknown):
    ResolveShellLink: _Callable[[_Unknwnbase.IUnknown,  # punkLink
                                 _type.HWND,  # hwnd
                                 _type.DWORD],  # fFlags
                                _type.HRESULT]


class IActionProgressDialog(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.SPINITF,  # flags
                           _type.LPCWSTR,  # pszTitle
                           _type.LPCWSTR],  # pszCancel
                          _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IActionProgress(_Unknwnbase.IUnknown):
    Begin: _Callable[[_enum.SPACTION,  # action
                      _type.SPBEGINF],  # flags
                     _type.HRESULT]
    UpdateProgress: _Callable[[_type.ULONGLONG,  # ulCompleted
                               _type.ULONGLONG],  # ulTotal
                              _type.HRESULT]
    UpdateText: _Callable[[_enum.SPTEXT,  # sptext
                           _type.LPCWSTR,  # pszText
                           _type.BOOL],  # fMayCompact
                          _type.HRESULT]
    QueryCancel: _Callable[[_Pointer[_type.BOOL]],  # pfCancelled
                           _type.HRESULT]
    ResetCancel: _Callable[[],
                           _type.HRESULT]
    End: _Callable[[],
                   _type.HRESULT]


class IShellExtInit(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlFolder
                           _objidl.IDataObject,  # pdtobj
                           _type.HKEY],  # hkeyProgID
                          _type.HRESULT]


class IShellPropSheetExt(_Unknwnbase.IUnknown):
    AddPages: _Callable
    ReplacePage: _Callable


class IRemoteComputer(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.LPCWSTR,  # pszMachine
                           _type.BOOL],  # bEnumerating
                          _type.HRESULT]


class IQueryContinue(_Unknwnbase.IUnknown):
    QueryContinue: _Callable[[],
                             _type.HRESULT]


class IObjectWithCancelEvent(_Unknwnbase.IUnknown):
    GetCancelEvent: _Callable[[_Pointer[_type.HANDLE]],  # phEvent
                              _type.HRESULT]


class IUserNotification(_Unknwnbase.IUnknown):
    SetBalloonInfo: _Callable[[_type.LPCWSTR,  # pszTitle
                               _type.LPCWSTR,  # pszText
                               _type.DWORD],  # dwInfoFlags
                              _type.HRESULT]
    SetBalloonRetry: _Callable[[_type.DWORD,  # dwShowTime
                                _type.DWORD,  # dwInterval
                                _type.UINT],  # cRetryCount
                               _type.HRESULT]
    SetIconInfo: _Callable[[_type.HICON,  # hIcon
                            _type.LPCWSTR],  # pszToolTip
                           _type.HRESULT]
    Show: _Callable[[IQueryContinue,  # pqc
                     _type.DWORD],  # dwContinuePollInterval
                    _type.HRESULT]
    PlaySoundA: _Callable[[_type.LPCWSTR],  # pszSoundName
                          _type.HRESULT]


class IItemNameLimits(_Unknwnbase.IUnknown):
    GetValidCharacters: _Callable[[_Pointer[_type.LPWSTR],  # ppwszValidChars
                                   _Pointer[_type.LPWSTR]],  # ppwszInvalidChars
                                  _type.HRESULT]
    GetMaxLength: _Callable[[_type.LPCWSTR,  # pszName
                             _Pointer[_type.c_int]],  # piMaxNameLen
                            _type.HRESULT]


class ISearchFolderItemFactory(_Unknwnbase.IUnknown):
    SetDisplayName: _Callable[[_type.LPCWSTR],  # pszDisplayName
                              _type.HRESULT]
    SetFolderTypeID: _Callable[[_struct.FOLDERTYPEID],  # ftid
                               _type.HRESULT]
    SetFolderLogicalViewMode: _Callable[[_enum.FOLDERLOGICALVIEWMODE],  # flvm
                                        _type.HRESULT]
    SetIconSize: _Callable[[_type.c_int],  # iIconSize
                           _type.HRESULT]
    SetVisibleColumns: _Callable[[_type.UINT,  # cVisibleColumns
                                  _Pointer[_struct.PROPERTYKEY]],  # rgKey
                                 _type.HRESULT]
    SetSortColumns: _Callable[[_type.UINT,  # cSortColumns
                               _Pointer[_struct.SORTCOLUMN]],  # rgSortColumns
                              _type.HRESULT]
    SetGroupColumn: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # keyGroup
                              _type.HRESULT]
    SetStacks: _Callable[[_type.UINT,  # cStackKeys
                          _Pointer[_struct.PROPERTYKEY]],  # rgStackKeys
                         _type.HRESULT]
    SetScope: _Callable[[IShellItemArray],  # psiaScope
                        _type.HRESULT]
    SetCondition: _Callable[[_StructuredQueryCondition.ICondition],  # pCondition
                            _type.HRESULT]
    GetShellItem: _Callable[[_Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]
    GetIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                         _type.HRESULT]


class IExtractImage(_Unknwnbase.IUnknown):
    GetLocation: _Callable[[_type.LPWSTR,  # pszPathBuffer
                            _type.DWORD,  # cch
                            _Pointer[_type.DWORD],  # pdwPriority
                            _Pointer[_struct.SIZE],  # prgSize
                            _type.DWORD,  # dwRecClrDepth
                            _Pointer[_type.DWORD]],  # pdwFlags
                           _type.HRESULT]
    Extract: _Callable[[_Pointer[_type.HBITMAP]],  # phBmpThumbnail
                       _type.HRESULT]


class IExtractImage2(IExtractImage):
    GetDateStamp: _Callable[[_Pointer[_struct.FILETIME]],  # pDateStamp
                            _type.HRESULT]


class IThumbnailHandlerFactory(_Unknwnbase.IUnknown):
    GetThumbnailHandler: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlChild
                                    _objidl.IBindCtx,  # pbc
                                    _Pointer[_struct.IID],  # riid
                                    _type.c_void_p],  # ppv
                                   _type.HRESULT]


class IParentAndItem(_Unknwnbase.IUnknown):
    SetParentAndItem: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlParent
                                 IShellFolder,  # psf
                                 _Pointer[_struct.ITEMIDLIST]],  # pidlChild
                                _type.HRESULT]
    GetParentAndItem: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]],  # ppidlParent
                                 _Pointer[IShellFolder],  # ppsf
                                 _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidlChild
                                _type.HRESULT]


class IDockingWindow(_oleidl.IOleWindow):
    ShowDW: _Callable[[_type.BOOL],  # fShow
                      _type.HRESULT]
    CloseDW: _Callable[[_type.DWORD],  # dwReserved
                       _type.HRESULT]
    ResizeBorderDW: _Callable[[_Pointer[_struct.RECT],  # prcBorder
                               _Unknwnbase.IUnknown,  # punkToolbarSite
                               _type.BOOL],  # fReserved
                              _type.HRESULT]


class IDeskBand(IDockingWindow):
    GetBandInfo: _Callable[[_type.DWORD,  # dwBandID
                            _type.DWORD,  # dwViewMode
                            _Pointer[_struct.DESKBANDINFO]],  # pdbi
                           _type.HRESULT]


class IDeskBandInfo(_Unknwnbase.IUnknown):
    GetDefaultBandWidth: _Callable[[_type.DWORD,  # dwBandID
                                    _type.DWORD,  # dwViewMode
                                    _Pointer[_type.c_int]],  # pnWidth
                                   _type.HRESULT]


class ITaskbarList(_Unknwnbase.IUnknown):
    HrInit: _Callable[[],
                      _type.HRESULT]
    AddTab: _Callable[[_type.HWND],  # hwnd
                      _type.HRESULT]
    DeleteTab: _Callable[[_type.HWND],  # hwnd
                         _type.HRESULT]
    ActivateTab: _Callable[[_type.HWND],  # hwnd
                           _type.HRESULT]
    SetActiveAlt: _Callable[[_type.HWND],  # hwnd
                            _type.HRESULT]


class ITaskbarList2(ITaskbarList):
    MarkFullscreenWindow: _Callable[[_type.HWND,  # hwnd
                                     _type.BOOL],  # fFullscreen
                                    _type.HRESULT]


class ITaskbarList3(ITaskbarList2):
    SetProgressValue: _Callable[[_type.HWND,  # hwnd
                                 _type.ULONGLONG,  # ullCompleted
                                 _type.ULONGLONG],  # ullTotal
                                _type.HRESULT]
    SetProgressState: _Callable[[_type.HWND,  # hwnd
                                 _enum.TBPFLAG],  # tbpFlags
                                _type.HRESULT]
    RegisterTab: _Callable[[_type.HWND,  # hwndTab
                            _type.HWND],  # hwndMDI
                           _type.HRESULT]
    UnregisterTab: _Callable[[_type.HWND],  # hwndTab
                             _type.HRESULT]
    SetTabOrder: _Callable[[_type.HWND,  # hwndTab
                            _type.HWND],  # hwndInsertBefore
                           _type.HRESULT]
    SetTabActive: _Callable[[_type.HWND,  # hwndTab
                             _type.HWND,  # hwndMDI
                             _type.DWORD],  # dwReserved
                            _type.HRESULT]
    ThumbBarAddButtons: _Callable[[_type.HWND,  # hwnd
                                   _type.UINT,  # cButtons
                                   _Pointer[_struct.THUMBBUTTON]],  # pButton
                                  _type.HRESULT]
    ThumbBarUpdateButtons: _Callable[[_type.HWND,  # hwnd
                                      _type.UINT,  # cButtons
                                      _Pointer[_struct.THUMBBUTTON]],  # pButton
                                     _type.HRESULT]
    ThumbBarSetImageList: _Callable[[_type.HWND,  # hwnd
                                     _commoncontrols.IImageList],  # himl
                                    _type.HRESULT]
    SetOverlayIcon: _Callable[[_type.HWND,  # hwnd
                               _type.HICON,  # hIcon
                               _type.LPCWSTR],  # pszDescription
                              _type.HRESULT]
    SetThumbnailTooltip: _Callable[[_type.HWND,  # hwnd
                                    _type.LPCWSTR],  # pszTip
                                   _type.HRESULT]
    SetThumbnailClip: _Callable[[_type.HWND,  # hwnd
                                 _Pointer[_struct.RECT]],  # prcClip
                                _type.HRESULT]


class ITaskbarList4(ITaskbarList3):
    SetTabProperties: _Callable[[_type.HWND,  # hwndTab
                                 _enum.STPFLAG],  # stpFlags
                                _type.HRESULT]


class IExplorerBrowserEvents(_Unknwnbase.IUnknown):
    OnNavigationPending: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidlFolder
                                   _type.HRESULT]
    OnViewCreated: _Callable[[IShellView],  # psv
                             _type.HRESULT]
    OnNavigationComplete: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidlFolder
                                    _type.HRESULT]
    OnNavigationFailed: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidlFolder
                                  _type.HRESULT]


class IExplorerBrowser(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.HWND,  # hwndParent
                           _Pointer[_struct.RECT],  # prc
                           _Pointer[_struct.FOLDERSETTINGS]],  # pfs
                          _type.HRESULT]
    Destroy: _Callable[[],
                       _type.HRESULT]
    SetRect: _Callable[[_Pointer[_type.HDWP],  # phdwp
                        _struct.RECT],  # rcBrowser
                       _type.HRESULT]
    SetPropertyBag: _Callable[[_type.LPCWSTR],  # pszPropertyBag
                              _type.HRESULT]
    SetEmptyText: _Callable[[_type.LPCWSTR],  # pszEmptyText
                            _type.HRESULT]
    SetFolderSettings: _Callable[[_Pointer[_struct.FOLDERSETTINGS]],  # pfs
                                 _type.HRESULT]
    Advise: _Callable[[IExplorerBrowserEvents,  # psbe
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]
    SetOptions: _Callable[[_enum.EXPLORER_BROWSER_OPTIONS],  # dwFlag
                          _type.HRESULT]
    GetOptions: _Callable[[_Pointer[_enum.EXPLORER_BROWSER_OPTIONS]],  # pdwFlag
                          _type.HRESULT]
    BrowseToIDList: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                               _type.UINT],  # uFlags
                              _type.HRESULT]
    BrowseToObject: _Callable[[_Unknwnbase.IUnknown,  # punk
                               _type.UINT],  # uFlags
                              _type.HRESULT]
    FillFromObject: _Callable[[_Unknwnbase.IUnknown,  # punk
                               _enum.EXPLORER_BROWSER_FILL_FLAGS],  # dwFlags
                              _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]
    GetCurrentView: _Callable[[_Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]


class IEnumObjects(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.IID],  # riid
                     _type.c_void_p,  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumObjects]],  # ppenum
                     _type.HRESULT]


class IOperationsProgressDialog(_Unknwnbase.IUnknown):
    StartProgressDialog: _Callable[[_type.HWND,  # hwndOwner
                                    _type.OPPROGDLGF],  # flags
                                   _type.HRESULT]
    StopProgressDialog: _Callable[[],
                                  _type.HRESULT]
    SetOperation: _Callable[[_enum.SPACTION],  # action
                            _type.HRESULT]
    SetMode: _Callable[[_type.PDMODE],  # mode
                       _type.HRESULT]
    UpdateProgress: _Callable[[_type.ULONGLONG,  # ullPointsCurrent
                               _type.ULONGLONG,  # ullPointsTotal
                               _type.ULONGLONG,  # ullSizeCurrent
                               _type.ULONGLONG,  # ullSizeTotal
                               _type.ULONGLONG,  # ullItemsCurrent
                               _type.ULONGLONG],  # ullItemsTotal
                              _type.HRESULT]
    UpdateLocations: _Callable[[IShellItem,  # psiSource
                                IShellItem,  # psiTarget
                                IShellItem],  # psiItem
                               _type.HRESULT]
    ResetTimer: _Callable[[],
                          _type.HRESULT]
    PauseTimer: _Callable[[],
                          _type.HRESULT]
    ResumeTimer: _Callable[[],
                           _type.HRESULT]
    GetMilliseconds: _Callable[[_Pointer[_type.ULONGLONG],  # pullElapsed
                                _Pointer[_type.ULONGLONG]],  # pullRemaining
                               _type.HRESULT]
    GetOperationStatus: _Callable[[_Pointer[_enum.PDOPSTATUS]],  # popstatus
                                  _type.HRESULT]


class IIOCancelInformation(_Unknwnbase.IUnknown):
    SetCancelInformation: _Callable[[_type.DWORD,  # dwThreadID
                                     _type.UINT],  # uMsgCancel
                                    _type.HRESULT]
    GetCancelInformation: _Callable[[_Pointer[_type.DWORD],  # pdwThreadID
                                     _Pointer[_type.UINT]],  # puMsgCancel
                                    _type.HRESULT]


class IFileOperation(_Unknwnbase.IUnknown):
    Advise: _Callable[[IFileOperationProgressSink,  # pfops
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]
    SetOperationFlags: _Callable[[_type.DWORD],  # dwOperationFlags
                                 _type.HRESULT]
    SetProgressMessage: _Callable[[_type.LPCWSTR],  # pszMessage
                                  _type.HRESULT]
    SetProgressDialog: _Callable[[IOperationsProgressDialog],  # popd
                                 _type.HRESULT]
    SetProperties: _Callable[[_propsys.IPropertyChangeArray],  # pproparray
                             _type.HRESULT]
    SetOwnerWindow: _Callable[[_type.HWND],  # hwndOwner
                              _type.HRESULT]
    ApplyPropertiesToItem: _Callable[[IShellItem],  # psiItem
                                     _type.HRESULT]
    ApplyPropertiesToItems: _Callable[[_Unknwnbase.IUnknown],  # punkItems
                                      _type.HRESULT]
    RenameItem: _Callable[[IShellItem,  # psiItem
                           _type.LPCWSTR,  # pszNewName
                           IFileOperationProgressSink],  # pfopsItem
                          _type.HRESULT]
    RenameItems: _Callable[[_Unknwnbase.IUnknown,  # pUnkItems
                            _type.LPCWSTR],  # pszNewName
                           _type.HRESULT]
    MoveItem: _Callable[[IShellItem,  # psiItem
                         IShellItem,  # psiDestinationFolder
                         _type.LPCWSTR,  # pszNewName
                         IFileOperationProgressSink],  # pfopsItem
                        _type.HRESULT]
    MoveItems: _Callable[[_Unknwnbase.IUnknown,  # punkItems
                          IShellItem],  # psiDestinationFolder
                         _type.HRESULT]
    CopyItem: _Callable[[IShellItem,  # psiItem
                         IShellItem,  # psiDestinationFolder
                         _type.LPCWSTR,  # pszCopyName
                         IFileOperationProgressSink],  # pfopsItem
                        _type.HRESULT]
    CopyItems: _Callable[[_Unknwnbase.IUnknown,  # punkItems
                          IShellItem],  # psiDestinationFolder
                         _type.HRESULT]
    DeleteItem: _Callable[[IShellItem,  # psiItem
                           IFileOperationProgressSink],  # pfopsItem
                          _type.HRESULT]
    DeleteItems: _Callable[[_Unknwnbase.IUnknown],  # punkItems
                           _type.HRESULT]
    NewItem: _Callable[[IShellItem,  # psiDestinationFolder
                        _type.DWORD,  # dwFileAttributes
                        _type.LPCWSTR,  # pszName
                        _type.LPCWSTR,  # pszTemplateName
                        IFileOperationProgressSink],  # pfopsItem
                       _type.HRESULT]
    PerformOperations: _Callable[[],
                                 _type.HRESULT]
    GetAnyOperationsAborted: _Callable[[_Pointer[_type.BOOL]],  # pfAnyOperationsAborted
                                       _type.HRESULT]


class IFileOperation2(IFileOperation):
    SetOperationFlags2: _Callable[[_enum.FILE_OPERATION_FLAGS2],  # operationFlags2
                                  _type.HRESULT]


class IObjectProvider(_Unknwnbase.IUnknown):
    QueryObject: _Callable[[_Pointer[_struct.GUID],  # guidObject
                            _Pointer[_struct.IID],  # riid
                            _type.c_void_p],  # ppvOut
                           _type.HRESULT]


class INamespaceWalkCB(_Unknwnbase.IUnknown):
    FoundItem: _Callable[[IShellFolder,  # psf
                          _Pointer[_struct.ITEMIDLIST]],  # pidl
                         _type.HRESULT]
    EnterFolder: _Callable[[IShellFolder,  # psf
                            _Pointer[_struct.ITEMIDLIST]],  # pidl
                           _type.HRESULT]
    LeaveFolder: _Callable[[IShellFolder,  # psf
                            _Pointer[_struct.ITEMIDLIST]],  # pidl
                           _type.HRESULT]
    InitializeProgressDialog: _Callable[[_Pointer[_type.LPWSTR],  # ppszTitle
                                         _Pointer[_type.LPWSTR]],  # ppszCancel
                                        _type.HRESULT]


class INamespaceWalkCB2(INamespaceWalkCB):
    WalkComplete: _Callable[[_type.HRESULT],  # hr
                            _type.HRESULT]


class INamespaceWalk(_Unknwnbase.IUnknown):
    Walk: _Callable[[_Unknwnbase.IUnknown,  # punkToWalk
                     _type.DWORD,  # dwFlags
                     _type.c_int,  # cDepth
                     INamespaceWalkCB],  # pnswcb
                    _type.HRESULT]
    GetIDArrayResult: _Callable[[_Pointer[_type.UINT],  # pcItems
                                 _Pointer[_Pointer[_Pointer[_struct.ITEMIDLIST]]]],  # prgpidl
                                _type.HRESULT]


class IBandSite(_Unknwnbase.IUnknown):
    AddBand: _Callable[[_Unknwnbase.IUnknown],  # punk
                       _type.HRESULT]
    EnumBands: _Callable[[_type.UINT,  # uBand
                          _Pointer[_type.DWORD]],  # pdwBandID
                         _type.HRESULT]
    QueryBand: _Callable[[_type.DWORD,  # dwBandID
                          _Pointer[IDeskBand],  # ppstb
                          _Pointer[_type.DWORD],  # pdwState
                          _type.LPWSTR,  # pszName
                          _type.c_int],  # cchName
                         _type.HRESULT]
    SetBandState: _Callable[[_type.DWORD,  # dwBandID
                             _type.DWORD,  # dwMask
                             _type.DWORD],  # dwState
                            _type.HRESULT]
    RemoveBand: _Callable[[_type.DWORD],  # dwBandID
                          _type.HRESULT]
    GetBandObject: _Callable[[_type.DWORD,  # dwBandID
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppv
                             _type.HRESULT]
    SetBandSiteInfo: _Callable[[_Pointer[_struct.BANDSITEINFO]],  # pbsinfo
                               _type.HRESULT]
    GetBandSiteInfo: _Callable[[_Pointer[_struct.BANDSITEINFO]],  # pbsinfo
                               _type.HRESULT]


class IModalWindow(_Unknwnbase.IUnknown):
    Show: _Callable[[_type.HWND],  # hwndOwner
                    _type.HRESULT]


class IContextMenuSite(_Unknwnbase.IUnknown):
    DoContextMenuPopup: _Callable[[_Unknwnbase.IUnknown,  # punkContextMenu
                                   _type.UINT,  # fFlags
                                   _struct.POINT],  # pt
                                  _type.HRESULT]


class IMenuBand(_Unknwnbase.IUnknown):
    IsMenuMessage: _Callable[[_Pointer[_struct.MSG]],  # pmsg
                             _type.HRESULT]
    TranslateMenuMessage: _Callable[[_Pointer[_struct.MSG],  # pmsg
                                     _Pointer[_type.LRESULT]],  # plRet
                                    _type.HRESULT]


class IRegTreeItem(_Unknwnbase.IUnknown):
    GetCheckState: _Callable[[_Pointer[_type.BOOL]],  # pbCheck
                             _type.HRESULT]
    SetCheckState: _Callable[[_type.BOOL],  # bCheck
                             _type.HRESULT]


class IDeskBar(_oleidl.IOleWindow):
    SetClient: _Callable[[_Unknwnbase.IUnknown],  # punkClient
                         _type.HRESULT]
    GetClient: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppunkClient
                         _type.HRESULT]
    OnPosRectChangeDB: _Callable[[_Pointer[_struct.RECT]],  # prc
                                 _type.HRESULT]


class IMenuPopup(IDeskBar):
    Popup: _Callable[[_Pointer[_struct.POINTL],  # ppt
                      _Pointer[_struct.RECTL],  # prcExclude
                      _type.MP_POPUPFLAGS],  # dwFlags
                     _type.HRESULT]
    OnSelect: _Callable[[_type.DWORD],  # dwSelectType
                        _type.HRESULT]
    SetSubMenu: _Callable[[IMenuPopup,  # pmp
                           _type.BOOL],  # fSet
                          _type.HRESULT]


class IFileIsInUse(_Unknwnbase.IUnknown):
    GetAppName: _Callable[[_Pointer[_type.LPWSTR]],  # ppszName
                          _type.HRESULT]
    GetUsage: _Callable[[_Pointer[_enum.FILE_USAGE_TYPE]],  # pfut
                        _type.HRESULT]
    GetCapabilities: _Callable[[_Pointer[_type.DWORD]],  # pdwCapFlags
                               _type.HRESULT]
    GetSwitchToHWND: _Callable[[_Pointer[_type.HWND]],  # phwnd
                               _type.HRESULT]
    CloseFile: _Callable[[],
                         _type.HRESULT]


class IFileDialogEvents(_Unknwnbase.IUnknown):
    OnFileOk: _Callable[[IFileDialog],  # pfd
                        _type.HRESULT]
    OnFolderChanging: _Callable[[IFileDialog,  # pfd
                                 IShellItem],  # psiFolder
                                _type.HRESULT]
    OnFolderChange: _Callable[[IFileDialog],  # pfd
                              _type.HRESULT]
    OnSelectionChange: _Callable[[IFileDialog],  # pfd
                                 _type.HRESULT]
    OnShareViolation: _Callable[[IFileDialog,  # pfd
                                 IShellItem,  # psi
                                 _Pointer[_enum.FDE_SHAREVIOLATION_RESPONSE]],  # pResponse
                                _type.HRESULT]
    OnTypeChange: _Callable[[IFileDialog],  # pfd
                            _type.HRESULT]
    OnOverwrite: _Callable[[IFileDialog,  # pfd
                            IShellItem,  # psi
                            _Pointer[_enum.FDE_OVERWRITE_RESPONSE]],  # pResponse
                           _type.HRESULT]


class IFileDialog(IModalWindow):
    SetFileTypes: _Callable[[_type.UINT,  # cFileTypes
                             _Pointer[_struct.COMDLG_FILTERSPEC]],  # rgFilterSpec
                            _type.HRESULT]
    SetFileTypeIndex: _Callable[[_type.UINT],  # iFileType
                                _type.HRESULT]
    GetFileTypeIndex: _Callable[[_Pointer[_type.UINT]],  # piFileType
                                _type.HRESULT]
    Advise: _Callable[[IFileDialogEvents,  # pfde
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]
    SetOptions: _Callable[[_type.FILEOPENDIALOGOPTIONS],  # fos
                          _type.HRESULT]
    GetOptions: _Callable[[_Pointer[_type.FILEOPENDIALOGOPTIONS]],  # pfos
                          _type.HRESULT]
    SetDefaultFolder: _Callable[[IShellItem],  # psi
                                _type.HRESULT]
    SetFolder: _Callable[[IShellItem],  # psi
                         _type.HRESULT]
    GetFolder: _Callable[[_Pointer[IShellItem]],  # ppsi
                         _type.HRESULT]
    GetCurrentSelection: _Callable[[_Pointer[IShellItem]],  # ppsi
                                   _type.HRESULT]
    SetFileName: _Callable[[_type.LPCWSTR],  # pszName
                           _type.HRESULT]
    GetFileName: _Callable[[_Pointer[_type.LPWSTR]],  # pszName
                           _type.HRESULT]
    SetTitle: _Callable[[_type.LPCWSTR],  # pszTitle
                        _type.HRESULT]
    SetOkButtonLabel: _Callable[[_type.LPCWSTR],  # pszText
                                _type.HRESULT]
    SetFileNameLabel: _Callable[[_type.LPCWSTR],  # pszLabel
                                _type.HRESULT]
    GetResult: _Callable[[_Pointer[IShellItem]],  # ppsi
                         _type.HRESULT]
    AddPlace: _Callable[[IShellItem,  # psi
                         _enum.FDAP],  # fdap
                        _type.HRESULT]
    SetDefaultExtension: _Callable[[_type.LPCWSTR],  # pszDefaultExtension
                                   _type.HRESULT]
    Close: _Callable[[_type.HRESULT],  # hr
                     _type.HRESULT]
    SetClientGuid: _Callable[[_Pointer[_struct.GUID]],  # guid
                             _type.HRESULT]
    ClearClientData: _Callable[[],
                               _type.HRESULT]
    SetFilter: _Callable[[IShellItemFilter],  # pFilter
                         _type.HRESULT]


class IFileSaveDialog(IFileDialog):
    SetSaveAsItem: _Callable[[IShellItem],  # psi
                             _type.HRESULT]
    SetProperties: _Callable[[_propsys.IPropertyStore],  # pStore
                             _type.HRESULT]
    SetCollectedProperties: _Callable[[_propsys.IPropertyDescriptionList,  # pList
                                       _type.BOOL],  # fAppendDefault
                                      _type.HRESULT]
    GetProperties: _Callable[[_Pointer[_propsys.IPropertyStore]],  # ppStore
                             _type.HRESULT]
    ApplyProperties: _Callable[[IShellItem,  # psi
                                _propsys.IPropertyStore,  # pStore
                                _type.HWND,  # hwnd
                                IFileOperationProgressSink],  # pSink
                               _type.HRESULT]


class IFileOpenDialog(IFileDialog):
    GetResults: _Callable[[_Pointer[IShellItemArray]],  # ppenum
                          _type.HRESULT]
    GetSelectedItems: _Callable[[_Pointer[IShellItemArray]],  # ppsai
                                _type.HRESULT]


class IFileDialogCustomize(_Unknwnbase.IUnknown):
    EnableOpenDropDown: _Callable[[_type.DWORD],  # dwIDCtl
                                  _type.HRESULT]
    AddMenu: _Callable[[_type.DWORD,  # dwIDCtl
                        _type.LPCWSTR],  # pszLabel
                       _type.HRESULT]
    AddPushButton: _Callable[[_type.DWORD,  # dwIDCtl
                              _type.LPCWSTR],  # pszLabel
                             _type.HRESULT]
    AddComboBox: _Callable[[_type.DWORD],  # dwIDCtl
                           _type.HRESULT]
    AddRadioButtonList: _Callable[[_type.DWORD],  # dwIDCtl
                                  _type.HRESULT]
    AddCheckButton: _Callable[[_type.DWORD,  # dwIDCtl
                               _type.LPCWSTR,  # pszLabel
                               _type.BOOL],  # bChecked
                              _type.HRESULT]
    AddEditBox: _Callable[[_type.DWORD,  # dwIDCtl
                           _type.LPCWSTR],  # pszText
                          _type.HRESULT]
    AddSeparator: _Callable[[_type.DWORD],  # dwIDCtl
                            _type.HRESULT]
    AddText: _Callable[[_type.DWORD,  # dwIDCtl
                        _type.LPCWSTR],  # pszText
                       _type.HRESULT]
    SetControlLabel: _Callable[[_type.DWORD,  # dwIDCtl
                                _type.LPCWSTR],  # pszLabel
                               _type.HRESULT]
    GetControlState: _Callable[[_type.DWORD,  # dwIDCtl
                                _Pointer[_enum.CDCONTROLSTATEF]],  # pdwState
                               _type.HRESULT]
    SetControlState: _Callable[[_type.DWORD,  # dwIDCtl
                                _enum.CDCONTROLSTATEF],  # dwState
                               _type.HRESULT]
    GetEditBoxText: _Callable[[_type.DWORD,  # dwIDCtl
                               _Pointer[_Pointer[_type.WCHAR]]],  # ppszText
                              _type.HRESULT]
    SetEditBoxText: _Callable[[_type.DWORD,  # dwIDCtl
                               _type.LPCWSTR],  # pszText
                              _type.HRESULT]
    GetCheckButtonState: _Callable[[_type.DWORD,  # dwIDCtl
                                    _Pointer[_type.BOOL]],  # pbChecked
                                   _type.HRESULT]
    SetCheckButtonState: _Callable[[_type.DWORD,  # dwIDCtl
                                    _type.BOOL],  # bChecked
                                   _type.HRESULT]
    AddControlItem: _Callable[[_type.DWORD,  # dwIDCtl
                               _type.DWORD,  # dwIDItem
                               _type.LPCWSTR],  # pszLabel
                              _type.HRESULT]
    RemoveControlItem: _Callable[[_type.DWORD,  # dwIDCtl
                                  _type.DWORD],  # dwIDItem
                                 _type.HRESULT]
    RemoveAllControlItems: _Callable[[_type.DWORD],  # dwIDCtl
                                     _type.HRESULT]
    GetControlItemState: _Callable[[_type.DWORD,  # dwIDCtl
                                    _type.DWORD,  # dwIDItem
                                    _Pointer[_enum.CDCONTROLSTATEF]],  # pdwState
                                   _type.HRESULT]
    SetControlItemState: _Callable[[_type.DWORD,  # dwIDCtl
                                    _type.DWORD,  # dwIDItem
                                    _enum.CDCONTROLSTATEF],  # dwState
                                   _type.HRESULT]
    GetSelectedControlItem: _Callable[[_type.DWORD,  # dwIDCtl
                                       _Pointer[_type.DWORD]],  # pdwIDItem
                                      _type.HRESULT]
    SetSelectedControlItem: _Callable[[_type.DWORD,  # dwIDCtl
                                       _type.DWORD],  # dwIDItem
                                      _type.HRESULT]
    StartVisualGroup: _Callable[[_type.DWORD,  # dwIDCtl
                                 _type.LPCWSTR],  # pszLabel
                                _type.HRESULT]
    EndVisualGroup: _Callable[[],
                              _type.HRESULT]
    MakeProminent: _Callable[[_type.DWORD],  # dwIDCtl
                             _type.HRESULT]
    SetControlItemText: _Callable[[_type.DWORD,  # dwIDCtl
                                   _type.DWORD,  # dwIDItem
                                   _type.LPCWSTR],  # pszLabel
                                  _type.HRESULT]


class IApplicationAssociationRegistration(_Unknwnbase.IUnknown):
    QueryCurrentDefault: _Callable[[_type.LPCWSTR,  # pszQuery
                                    _enum.ASSOCIATIONTYPE,  # atQueryType
                                    _enum.ASSOCIATIONLEVEL,  # alQueryLevel
                                    _Pointer[_type.LPWSTR]],  # ppszAssociation
                                   _type.HRESULT]
    QueryAppIsDefault: _Callable[[_type.LPCWSTR,  # pszQuery
                                  _enum.ASSOCIATIONTYPE,  # atQueryType
                                  _enum.ASSOCIATIONLEVEL,  # alQueryLevel
                                  _type.LPCWSTR,  # pszAppRegistryName
                                  _Pointer[_type.BOOL]],  # pfDefault
                                 _type.HRESULT]
    QueryAppIsDefaultAll: _Callable[[_enum.ASSOCIATIONLEVEL,  # alQueryLevel
                                     _type.LPCWSTR,  # pszAppRegistryName
                                     _Pointer[_type.BOOL]],  # pfDefault
                                    _type.HRESULT]
    SetAppAsDefault: _Callable[[_type.LPCWSTR,  # pszAppRegistryName
                                _type.LPCWSTR,  # pszSet
                                _enum.ASSOCIATIONTYPE],  # atSetType
                               _type.HRESULT]
    SetAppAsDefaultAll: _Callable[[_type.LPCWSTR],  # pszAppRegistryName
                                  _type.HRESULT]
    ClearUserAssociations: _Callable[[],
                                     _type.HRESULT]


class IDelegateFolder(_Unknwnbase.IUnknown):
    SetItemAlloc: _Callable[[_objidlbase.IMalloc],  # pmalloc
                            _type.HRESULT]


class IBrowserFrameOptions(_Unknwnbase.IUnknown):
    GetFrameOptions: _Callable[[_type.BROWSERFRAMEOPTIONS,  # dwMask
                                _Pointer[_type.BROWSERFRAMEOPTIONS]],  # pdwOptions
                               _type.HRESULT]


class INewWindowManager(_Unknwnbase.IUnknown):
    EvaluateNewWindow: _Callable[[_type.LPCWSTR,  # pszUrl
                                  _type.LPCWSTR,  # pszName
                                  _type.LPCWSTR,  # pszUrlContext
                                  _type.LPCWSTR,  # pszFeatures
                                  _type.BOOL,  # fReplace
                                  _type.DWORD,  # dwFlags
                                  _type.DWORD],  # dwUserActionTime
                                 _type.HRESULT]


class IAttachmentExecute(_Unknwnbase.IUnknown):
    SetClientTitle: _Callable[[_type.LPCWSTR],  # pszTitle
                              _type.HRESULT]
    SetClientGuid: _Callable[[_Pointer[_struct.GUID]],  # guid
                             _type.HRESULT]
    SetLocalPath: _Callable[[_type.LPCWSTR],  # pszLocalPath
                            _type.HRESULT]
    SetFileName: _Callable[[_type.LPCWSTR],  # pszFileName
                           _type.HRESULT]
    SetSource: _Callable[[_type.LPCWSTR],  # pszSource
                         _type.HRESULT]
    SetReferrer: _Callable[[_type.LPCWSTR],  # pszReferrer
                           _type.HRESULT]
    CheckPolicy: _Callable[[],
                           _type.HRESULT]
    Prompt: _Callable[[_type.HWND,  # hwnd
                       _enum.ATTACHMENT_PROMPT,  # prompt
                       _Pointer[_enum.ATTACHMENT_ACTION]],  # paction
                      _type.HRESULT]
    Save: _Callable[[],
                    _type.HRESULT]
    Execute: _Callable[[_type.HWND,  # hwnd
                        _type.LPCWSTR,  # pszVerb
                        _Pointer[_type.HANDLE]],  # phProcess
                       _type.HRESULT]
    SaveWithUI: _Callable[[_type.HWND],  # hwnd
                          _type.HRESULT]
    ClearClientState: _Callable[[],
                                _type.HRESULT]


class IShellMenuCallback(_Unknwnbase.IUnknown):
    CallbackSM: _Callable[[_Pointer[_struct.SMDATA],  # psmd
                           _type.UINT,  # uMsg
                           _type.WPARAM,  # wParam
                           _type.LPARAM],  # lParam
                          _type.HRESULT]


class IShellMenu(_Unknwnbase.IUnknown):
    Initialize: _Callable[[IShellMenuCallback,  # psmc
                           _type.UINT,  # uId
                           _type.UINT,  # uIdAncestor
                           _type.DWORD],  # dwFlags
                          _type.HRESULT]
    GetMenuInfo: _Callable[[_Pointer[IShellMenuCallback],  # ppsmc
                            _Pointer[_type.UINT],  # puId
                            _Pointer[_type.UINT],  # puIdAncestor
                            _Pointer[_type.DWORD]],  # pdwFlags
                           _type.HRESULT]
    SetShellFolder: _Callable[[IShellFolder,  # psf
                               _Pointer[_struct.ITEMIDLIST],  # pidlFolder
                               _type.HKEY,  # hKey
                               _type.DWORD],  # dwFlags
                              _type.HRESULT]
    GetShellFolder: _Callable[[_Pointer[_type.DWORD],  # pdwFlags
                               _Pointer[_Pointer[_struct.ITEMIDLIST]],  # ppidl
                               _Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppv
                              _type.HRESULT]
    SetMenu: _Callable[[_type.HMENU,  # hmenu
                        _type.HWND,  # hwnd
                        _type.DWORD],  # dwFlags
                       _type.HRESULT]
    GetMenu: _Callable[[_Pointer[_type.HMENU],  # phmenu
                        _Pointer[_type.HWND],  # phwnd
                        _Pointer[_type.DWORD]],  # pdwFlags
                       _type.HRESULT]
    InvalidateItem: _Callable[[_Pointer[_struct.SMDATA],  # psmd
                               _type.DWORD],  # dwFlags
                              _type.HRESULT]
    GetState: _Callable[[_Pointer[_struct.SMDATA]],  # psmd
                        _type.HRESULT]
    SetMenuToolbar: _Callable[[_Unknwnbase.IUnknown,  # punk
                               _type.DWORD],  # dwFlags
                              _type.HRESULT]


class IKnownFolder(_Unknwnbase.IUnknown):
    GetId: _Callable[[_Pointer[_struct.KNOWNFOLDERID]],  # pkfid
                     _type.HRESULT]
    GetCategory: _Callable[[_Pointer[_enum.KF_CATEGORY]],  # pCategory
                           _type.HRESULT]
    GetShellItem: _Callable[[_type.DWORD,  # dwFlags
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]
    GetPath: _Callable[[_type.DWORD,  # dwFlags
                        _Pointer[_type.LPWSTR]],  # ppszPath
                       _type.HRESULT]
    SetPath: _Callable[[_type.DWORD,  # dwFlags
                        _type.LPCWSTR],  # pszPath
                       _type.HRESULT]
    GetIDList: _Callable[[_type.DWORD,  # dwFlags
                          _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                         _type.HRESULT]
    GetFolderType: _Callable[[_Pointer[_struct.FOLDERTYPEID]],  # pftid
                             _type.HRESULT]
    GetRedirectionCapabilities: _Callable[[_Pointer[_type.KF_REDIRECTION_CAPABILITIES]],  # pCapabilities
                                          _type.HRESULT]
    GetFolderDefinition: _Callable[[_Pointer[_struct.KNOWNFOLDER_DEFINITION]],  # pKFD
                                   _type.HRESULT]


class IKnownFolderManager(_Unknwnbase.IUnknown):
    FolderIdFromCsidl: _Callable[[_type.c_int,  # nCsidl
                                  _Pointer[_struct.KNOWNFOLDERID]],  # pfid
                                 _type.HRESULT]
    FolderIdToCsidl: _Callable[[_Pointer[_struct.KNOWNFOLDERID],  # rfid
                                _Pointer[_type.c_int]],  # pnCsidl
                               _type.HRESULT]
    GetFolderIds: _Callable[[_Pointer[_Pointer[_struct.KNOWNFOLDERID]],  # ppKFId
                             _Pointer[_type.UINT]],  # pCount
                            _type.HRESULT]
    GetFolder: _Callable[[_Pointer[_struct.KNOWNFOLDERID],  # rfid
                          _Pointer[IKnownFolder]],  # ppkf
                         _type.HRESULT]
    GetFolderByName: _Callable[[_type.LPCWSTR,  # pszCanonicalName
                                _Pointer[IKnownFolder]],  # ppkf
                               _type.HRESULT]
    RegisterFolder: _Callable[[_Pointer[_struct.KNOWNFOLDERID],  # rfid
                               _Pointer[_struct.KNOWNFOLDER_DEFINITION]],  # pKFD
                              _type.HRESULT]
    UnregisterFolder: _Callable[[_Pointer[_struct.KNOWNFOLDERID]],  # rfid
                                _type.HRESULT]
    FindFolderFromPath: _Callable[[_type.LPCWSTR,  # pszPath
                                   _enum.FFFP_MODE,  # mode
                                   _Pointer[IKnownFolder]],  # ppkf
                                  _type.HRESULT]
    FindFolderFromIDList: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                     _Pointer[IKnownFolder]],  # ppkf
                                    _type.HRESULT]
    Redirect: _Callable[[_Pointer[_struct.KNOWNFOLDERID],  # rfid
                         _type.HWND,  # hwnd
                         _type.KF_REDIRECT_FLAGS,  # flags
                         _type.LPCWSTR,  # pszTargetPath
                         _type.UINT,  # cFolders
                         _Pointer[_struct.KNOWNFOLDERID],  # pExclusion
                         _Pointer[_type.LPWSTR]],  # ppszError
                        _type.HRESULT]


class ISharingConfigurationManager(_Unknwnbase.IUnknown):
    CreateShare: _Callable[[_enum.DEF_SHARE_ID,  # dsid
                            _enum.SHARE_ROLE],  # role
                           _type.HRESULT]
    DeleteShare: _Callable[[_enum.DEF_SHARE_ID],  # dsid
                           _type.HRESULT]
    ShareExists: _Callable[[_enum.DEF_SHARE_ID],  # dsid
                           _type.HRESULT]
    GetSharePermissions: _Callable[[_enum.DEF_SHARE_ID,  # dsid
                                    _Pointer[_enum.SHARE_ROLE]],  # pRole
                                   _type.HRESULT]
    SharePrinters: _Callable[[],
                             _type.HRESULT]
    StopSharingPrinters: _Callable[[],
                                   _type.HRESULT]
    ArePrintersShared: _Callable[[],
                                 _type.HRESULT]


class IRelatedItem(_Unknwnbase.IUnknown):
    GetItemIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                             _type.HRESULT]
    GetItem: _Callable[[_Pointer[IShellItem]],  # ppsi
                       _type.HRESULT]


class IIdentityName(IRelatedItem):
    pass


class IDelegateItem(IRelatedItem):
    pass


class ICurrentItem(IRelatedItem):
    pass


class ITransferMediumItem(IRelatedItem):
    pass


class IDisplayItem(IRelatedItem):
    pass


class IViewStateIdentityItem(IRelatedItem):
    pass


class IPreviewItem(IRelatedItem):
    pass


class IDestinationStreamFactory(_Unknwnbase.IUnknown):
    GetDestinationStream: _Callable[[_Pointer[_objidlbase.IStream]],  # ppstm
                                    _type.HRESULT]


class ICreateProcessInputs(_Unknwnbase.IUnknown):
    GetCreateFlags: _Callable[[_Pointer[_type.DWORD]],  # pdwCreationFlags
                              _type.HRESULT]
    SetCreateFlags: _Callable[[_type.DWORD],  # dwCreationFlags
                              _type.HRESULT]
    AddCreateFlags: _Callable[[_type.DWORD],  # dwCreationFlags
                              _type.HRESULT]
    SetHotKey: _Callable[[_type.WORD],  # wHotKey
                         _type.HRESULT]
    AddStartupFlags: _Callable[[_type.DWORD],  # dwStartupInfoFlags
                               _type.HRESULT]
    SetTitle: _Callable[[_type.LPCWSTR],  # pszTitle
                        _type.HRESULT]
    SetEnvironmentVariableA: _Callable[[_type.LPCWSTR,  # pszName
                                        _type.LPCWSTR],  # pszValue
                                       _type.HRESULT]


class ICreatingProcess(_Unknwnbase.IUnknown):
    OnCreating: _Callable[[ICreateProcessInputs],  # pcpi
                          _type.HRESULT]


class ILaunchUIContext(_Unknwnbase.IUnknown):
    SetAssociatedWindow: _Callable[[_type.HWND],  # value
                                   _type.HRESULT]
    SetTabGroupingPreference: _Callable[[_type.DWORD],  # value
                                        _type.HRESULT]


class ILaunchUIContextProvider(_Unknwnbase.IUnknown):
    UpdateContext: _Callable[[ILaunchUIContext],  # context
                             _type.HRESULT]


class INewMenuClient(_Unknwnbase.IUnknown):
    IncludeItems: _Callable[[_Pointer[_type.NMCII_FLAGS]],  # pflags
                            _type.HRESULT]
    SelectAndEditItem: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlItem
                                  _type.NMCSAEI_FLAGS],  # flags
                                 _type.HRESULT]


class IInitializeWithBindCtx(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_objidl.IBindCtx],  # pbc
                          _type.HRESULT]


class IShellItemFilter(_Unknwnbase.IUnknown):
    IncludeItem: _Callable[[IShellItem],  # psi
                           _type.HRESULT]
    GetEnumFlagsForItem: _Callable[[IShellItem,  # psi
                                    _Pointer[_type.SHCONTF]],  # pgrfFlags
                                   _type.HRESULT]


class INameSpaceTreeControl(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.HWND,  # hwndParent
                           _Pointer[_struct.RECT],  # prc
                           _type.NSTCSTYLE],  # nsctsFlags
                          _type.HRESULT]
    TreeAdvise: _Callable[[_Unknwnbase.IUnknown,  # punk
                           _Pointer[_type.DWORD]],  # pdwCookie
                          _type.HRESULT]
    TreeUnadvise: _Callable[[_type.DWORD],  # dwCookie
                            _type.HRESULT]
    AppendRoot: _Callable[[IShellItem,  # psiRoot
                           _type.SHCONTF,  # grfEnumFlags
                           _type.NSTCROOTSTYLE,  # grfRootStyle
                           IShellItemFilter],  # pif
                          _type.HRESULT]
    InsertRoot: _Callable[[_type.c_int,  # iIndex
                           IShellItem,  # psiRoot
                           _type.SHCONTF,  # grfEnumFlags
                           _type.NSTCROOTSTYLE,  # grfRootStyle
                           IShellItemFilter],  # pif
                          _type.HRESULT]
    RemoveRoot: _Callable[[IShellItem],  # psiRoot
                          _type.HRESULT]
    RemoveAllRoots: _Callable[[],
                              _type.HRESULT]
    GetRootItems: _Callable[[_Pointer[IShellItemArray]],  # ppsiaRootItems
                            _type.HRESULT]
    SetItemState: _Callable[[IShellItem,  # psi
                             _type.NSTCITEMSTATE,  # nstcisMask
                             _type.NSTCITEMSTATE],  # nstcisFlags
                            _type.HRESULT]
    GetItemState: _Callable[[IShellItem,  # psi
                             _type.NSTCITEMSTATE,  # nstcisMask
                             _Pointer[_type.NSTCITEMSTATE]],  # pnstcisFlags
                            _type.HRESULT]
    GetSelectedItems: _Callable[[_Pointer[IShellItemArray]],  # psiaItems
                                _type.HRESULT]
    GetItemCustomState: _Callable[[IShellItem,  # psi
                                   _Pointer[_type.c_int]],  # piStateNumber
                                  _type.HRESULT]
    SetItemCustomState: _Callable[[IShellItem,  # psi
                                   _type.c_int],  # iStateNumber
                                  _type.HRESULT]
    EnsureItemVisible: _Callable[[IShellItem],  # psi
                                 _type.HRESULT]
    SetTheme: _Callable[[_type.LPCWSTR],  # pszTheme
                        _type.HRESULT]
    GetNextItem: _Callable[[IShellItem,  # psi
                            _enum.NSTCGNI,  # nstcgi
                            _Pointer[IShellItem]],  # ppsiNext
                           _type.HRESULT]
    HitTest: _Callable[[_Pointer[_struct.POINT],  # ppt
                        _Pointer[IShellItem]],  # ppsiOut
                       _type.HRESULT]
    GetItemRect: _Callable[[IShellItem,  # psi
                            _Pointer[_struct.RECT]],  # prect
                           _type.HRESULT]
    CollapseAll: _Callable[[],
                           _type.HRESULT]


class INameSpaceTreeControlFolderCapabilities(_Unknwnbase.IUnknown):
    GetFolderCapabilities: _Callable[[_enum.NSTCFOLDERCAPABILITIES,  # nfcMask
                                      _Pointer[_enum.NSTCFOLDERCAPABILITIES]],  # pnfcValue
                                     _type.HRESULT]


class IPreviewHandler(_Unknwnbase.IUnknown):
    SetWindow: _Callable[[_type.HWND,  # hwnd
                          _Pointer[_struct.RECT]],  # prc
                         _type.HRESULT]
    SetRect: _Callable[[_Pointer[_struct.RECT]],  # prc
                       _type.HRESULT]
    DoPreview: _Callable[[],
                         _type.HRESULT]
    Unload: _Callable[[],
                      _type.HRESULT]
    SetFocus: _Callable[[],
                        _type.HRESULT]
    QueryFocus: _Callable[[_Pointer[_type.HWND]],  # phwnd
                          _type.HRESULT]
    TranslateAcceleratorA: _Callable[[_Pointer[_struct.MSG]],  # pmsg
                                     _type.HRESULT]


class IPreviewHandlerFrame(_Unknwnbase.IUnknown):
    GetWindowContext: _Callable[[_Pointer[_struct.PREVIEWHANDLERFRAMEINFO]],  # pinfo
                                _type.HRESULT]
    TranslateAcceleratorA: _Callable[[_Pointer[_struct.MSG]],  # pmsg
                                     _type.HRESULT]


class IExplorerPaneVisibility(_Unknwnbase.IUnknown):
    GetPaneState: _Callable[[_Pointer[_struct.EXPLORERPANE],  # ep
                             _Pointer[_type.EXPLORERPANESTATE]],  # peps
                            _type.HRESULT]


class IContextMenuCB(_Unknwnbase.IUnknown):
    CallBack: _Callable[[IShellFolder,  # psf
                         _type.HWND,  # hwndOwner
                         _objidl.IDataObject,  # pdtobj
                         _type.UINT,  # uMsg
                         _type.WPARAM,  # wParam
                         _type.LPARAM],  # lParam
                        _type.HRESULT]


class IDefaultExtractIconInit(_Unknwnbase.IUnknown):
    SetFlags: _Callable[[_type.UINT],  # uFlags
                        _type.HRESULT]
    SetKey: _Callable[[_type.HKEY],  # hkey
                      _type.HRESULT]
    SetNormalIcon: _Callable[[_type.LPCWSTR,  # pszFile
                              _type.c_int],  # iIcon
                             _type.HRESULT]
    SetOpenIcon: _Callable[[_type.LPCWSTR,  # pszFile
                            _type.c_int],  # iIcon
                           _type.HRESULT]
    SetShortcutIcon: _Callable[[_type.LPCWSTR,  # pszFile
                                _type.c_int],  # iIcon
                               _type.HRESULT]
    SetDefaultIcon: _Callable[[_type.LPCWSTR,  # pszFile
                               _type.c_int],  # iIcon
                              _type.HRESULT]


class IExplorerCommand(_Unknwnbase.IUnknown):
    GetTitle: _Callable[[IShellItemArray,  # psiItemArray
                         _Pointer[_type.LPWSTR]],  # ppszName
                        _type.HRESULT]
    GetIcon: _Callable[[IShellItemArray,  # psiItemArray
                        _Pointer[_type.LPWSTR]],  # ppszIcon
                       _type.HRESULT]
    GetToolTip: _Callable[[IShellItemArray,  # psiItemArray
                           _Pointer[_type.LPWSTR]],  # ppszInfotip
                          _type.HRESULT]
    GetCanonicalName: _Callable[[_Pointer[_struct.GUID]],  # pguidCommandName
                                _type.HRESULT]
    GetState: _Callable[[IShellItemArray,  # psiItemArray
                         _type.BOOL,  # fOkToBeSlow
                         _Pointer[_type.EXPCMDSTATE]],  # pCmdState
                        _type.HRESULT]
    Invoke: _Callable[[IShellItemArray,  # psiItemArray
                       _objidl.IBindCtx],  # pbc
                      _type.HRESULT]
    GetFlags: _Callable[[_Pointer[_type.EXPCMDFLAGS]],  # pFlags
                        _type.HRESULT]
    EnumSubCommands: _Callable[[_Pointer[IEnumExplorerCommand]],  # ppEnum
                               _type.HRESULT]


class IExplorerCommandState(_Unknwnbase.IUnknown):
    GetState: _Callable[[IShellItemArray,  # psiItemArray
                         _type.BOOL,  # fOkToBeSlow
                         _Pointer[_type.EXPCMDSTATE]],  # pCmdState
                        _type.HRESULT]


class IInitializeCommand(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.LPCWSTR,  # pszCommandName
                           _oaidl.IPropertyBag],  # ppb
                          _type.HRESULT]


class IEnumExplorerCommand(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[IExplorerCommand],  # pUICommand
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IEnumExplorerCommand]],  # ppenum
                     _type.HRESULT]


class IExplorerCommandProvider(_Unknwnbase.IUnknown):
    GetCommands: _Callable[[_Unknwnbase.IUnknown,  # punkSite
                            _Pointer[_struct.IID],  # riid
                            _type.c_void_p],  # ppv
                           _type.HRESULT]
    GetCommand: _Callable[[_Pointer[_struct.GUID],  # rguidCommandId
                           _Pointer[_struct.IID],  # riid
                           _type.c_void_p],  # ppv
                          _type.HRESULT]


class IOpenControlPanel(_Unknwnbase.IUnknown):
    Open: _Callable[[_type.LPCWSTR,  # pszName
                     _type.LPCWSTR,  # pszPage
                     _Unknwnbase.IUnknown],  # punkSite
                    _type.HRESULT]
    GetPath: _Callable[[_type.LPCWSTR,  # pszName
                        _type.LPWSTR,  # pszPath
                        _type.UINT],  # cchPath
                       _type.HRESULT]
    GetCurrentView: _Callable[[_Pointer[_enum.CPVIEW]],  # pView
                              _type.HRESULT]


class IFileSystemBindData(_Unknwnbase.IUnknown):
    SetFindData: _Callable[[_Pointer[_struct.WIN32_FIND_DATAW]],  # pfd
                           _type.HRESULT]
    GetFindData: _Callable[[_Pointer[_struct.WIN32_FIND_DATAW]],  # pfd
                           _type.HRESULT]


class IFileSystemBindData2(IFileSystemBindData):
    SetFileID: _Callable[[_union.LARGE_INTEGER],  # liFileID
                         _type.HRESULT]
    GetFileID: _Callable[[_Pointer[_union.LARGE_INTEGER]],  # pliFileID
                         _type.HRESULT]
    SetJunctionCLSID: _Callable[[_Pointer[_struct.IID]],  # clsid
                                _type.HRESULT]
    GetJunctionCLSID: _Callable[[_Pointer[_struct.CLSID]],  # pclsid
                                _type.HRESULT]


class ICustomDestinationList(_Unknwnbase.IUnknown):
    SetAppID: _Callable[[_type.LPCWSTR],  # pszAppID
                        _type.HRESULT]
    BeginList: _Callable[[_Pointer[_type.UINT],  # pcMinSlots
                          _Pointer[_struct.IID],  # riid
                          _type.c_void_p],  # ppv
                         _type.HRESULT]
    AppendCategory: _Callable[[_type.LPCWSTR,  # pszCategory
                               _ObjectArray.IObjectArray],  # poa
                              _type.HRESULT]
    AppendKnownCategory: _Callable[[_enum.KNOWNDESTCATEGORY],  # category
                                   _type.HRESULT]
    AddUserTasks: _Callable[[_ObjectArray.IObjectArray],  # poa
                            _type.HRESULT]
    CommitList: _Callable[[],
                          _type.HRESULT]
    GetRemovedDestinations: _Callable[[_Pointer[_struct.IID],  # riid
                                       _type.c_void_p],  # ppv
                                      _type.HRESULT]
    DeleteList: _Callable[[_type.LPCWSTR],  # pszAppID
                          _type.HRESULT]
    AbortList: _Callable[[],
                         _type.HRESULT]


class IApplicationDestinations(_Unknwnbase.IUnknown):
    SetAppID: _Callable[[_type.LPCWSTR],  # pszAppID
                        _type.HRESULT]
    RemoveDestination: _Callable[[_Unknwnbase.IUnknown],  # punk
                                 _type.HRESULT]
    RemoveAllDestinations: _Callable[[],
                                     _type.HRESULT]


class IApplicationDocumentLists(_Unknwnbase.IUnknown):
    SetAppID: _Callable[[_type.LPCWSTR],  # pszAppID
                        _type.HRESULT]
    GetList: _Callable[[_enum.APPDOCLISTTYPE,  # listtype
                        _type.UINT,  # cItemsDesired
                        _Pointer[_struct.IID],  # riid
                        _type.c_void_p],  # ppv
                       _type.HRESULT]


class IObjectWithAppUserModelID(_Unknwnbase.IUnknown):
    SetAppID: _Callable[[_type.LPCWSTR],  # pszAppID
                        _type.HRESULT]
    GetAppID: _Callable[[_Pointer[_type.LPWSTR]],  # ppszAppID
                        _type.HRESULT]


class IObjectWithProgID(_Unknwnbase.IUnknown):
    SetProgID: _Callable[[_type.LPCWSTR],  # pszProgID
                         _type.HRESULT]
    GetProgID: _Callable[[_Pointer[_type.LPWSTR]],  # ppszProgID
                         _type.HRESULT]


class IUpdateIDList(_Unknwnbase.IUnknown):
    Update: _Callable[[_objidl.IBindCtx,  # pbc
                       _Pointer[_struct.ITEMIDLIST],  # pidlIn
                       _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidlOut
                      _type.HRESULT]


class IDesktopWallpaper(_Unknwnbase.IUnknown):
    SetWallpaper: _Callable[[_type.LPCWSTR,  # monitorID
                             _type.LPCWSTR],  # wallpaper
                            _type.HRESULT]
    GetWallpaper: _Callable[[_type.LPCWSTR,  # monitorID
                             _Pointer[_type.LPWSTR]],  # wallpaper
                            _type.HRESULT]
    GetMonitorDevicePathAt: _Callable[[_type.UINT,  # monitorIndex
                                       _Pointer[_type.LPWSTR]],  # monitorID
                                      _type.HRESULT]
    GetMonitorDevicePathCount: _Callable[[_Pointer[_type.UINT]],  # count
                                         _type.HRESULT]
    GetMonitorRECT: _Callable[[_type.LPCWSTR,  # monitorID
                               _Pointer[_struct.RECT]],  # displayRect
                              _type.HRESULT]
    SetBackgroundColor: _Callable[[_type.COLORREF],  # color
                                  _type.HRESULT]
    GetBackgroundColor: _Callable[[_Pointer[_type.COLORREF]],  # color
                                  _type.HRESULT]
    SetPosition: _Callable[[_enum.DESKTOP_WALLPAPER_POSITION],  # position
                           _type.HRESULT]
    GetPosition: _Callable[[_Pointer[_enum.DESKTOP_WALLPAPER_POSITION]],  # position
                           _type.HRESULT]
    SetSlideshow: _Callable[[IShellItemArray],  # items
                            _type.HRESULT]
    GetSlideshow: _Callable[[_Pointer[IShellItemArray]],  # items
                            _type.HRESULT]
    SetSlideshowOptions: _Callable[[_enum.DESKTOP_SLIDESHOW_OPTIONS,  # options
                                    _type.UINT],  # slideshowTick
                                   _type.HRESULT]
    GetSlideshowOptions: _Callable[[_Pointer[_enum.DESKTOP_SLIDESHOW_OPTIONS],  # options
                                    _Pointer[_type.UINT]],  # slideshowTick
                                   _type.HRESULT]
    AdvanceSlideshow: _Callable[[_type.LPCWSTR,  # monitorID
                                 _enum.DESKTOP_SLIDESHOW_DIRECTION],  # direction
                                _type.HRESULT]
    GetStatus: _Callable[[_Pointer[_enum.DESKTOP_SLIDESHOW_STATE]],  # state
                         _type.HRESULT]
    Enable: _Callable[[_type.BOOL],  # enable
                      _type.HRESULT]


class IHomeGroup(_Unknwnbase.IUnknown):
    IsMember: _Callable[[_Pointer[_type.BOOL]],  # member
                        _type.HRESULT]
    ShowSharingWizard: _Callable[[_type.HWND,  # owner
                                  _Pointer[_enum.HOMEGROUPSHARINGCHOICES]],  # sharingchoices
                                 _type.HRESULT]


class IInitializeWithPropertyStore(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_propsys.IPropertyStore],  # pps
                          _type.HRESULT]


class IOpenSearchSource(_Unknwnbase.IUnknown):
    GetResults: _Callable[[_type.HWND,  # hwnd
                           _type.LPCWSTR,  # pszQuery
                           _type.DWORD,  # dwStartIndex
                           _type.DWORD,  # dwCount
                           _Pointer[_struct.IID],  # riid
                           _type.c_void_p],  # ppv
                          _type.HRESULT]


class IShellLibrary(_Unknwnbase.IUnknown):
    LoadLibraryFromItem: _Callable[[IShellItem,  # psiLibrary
                                    _type.DWORD],  # grfMode
                                   _type.HRESULT]
    LoadLibraryFromKnownFolder: _Callable[[_Pointer[_struct.KNOWNFOLDERID],  # kfidLibrary
                                           _type.DWORD],  # grfMode
                                          _type.HRESULT]
    AddFolder: _Callable[[IShellItem],  # psiLocation
                         _type.HRESULT]
    RemoveFolder: _Callable[[IShellItem],  # psiLocation
                            _type.HRESULT]
    GetFolders: _Callable[[_enum.LIBRARYFOLDERFILTER,  # lff
                           _Pointer[_struct.IID],  # riid
                           _type.c_void_p],  # ppv
                          _type.HRESULT]
    ResolveFolder: _Callable[[IShellItem,  # psiFolderToResolve
                              _type.DWORD,  # dwTimeout
                              _Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppv
                             _type.HRESULT]
    GetDefaultSaveFolder: _Callable[[_enum.DEFAULTSAVEFOLDERTYPE,  # dsft
                                     _Pointer[_struct.IID],  # riid
                                     _type.c_void_p],  # ppv
                                    _type.HRESULT]
    SetDefaultSaveFolder: _Callable[[_enum.DEFAULTSAVEFOLDERTYPE,  # dsft
                                     IShellItem],  # psi
                                    _type.HRESULT]
    GetOptions: _Callable[[_Pointer[_enum.LIBRARYOPTIONFLAGS]],  # plofOptions
                          _type.HRESULT]
    SetOptions: _Callable[[_enum.LIBRARYOPTIONFLAGS,  # lofMask
                           _enum.LIBRARYOPTIONFLAGS],  # lofOptions
                          _type.HRESULT]
    GetFolderType: _Callable[[_Pointer[_struct.FOLDERTYPEID]],  # pftid
                             _type.HRESULT]
    SetFolderType: _Callable[[_Pointer[_struct.FOLDERTYPEID]],  # ftid
                             _type.HRESULT]
    GetIcon: _Callable[[_Pointer[_type.LPWSTR]],  # ppszIcon
                       _type.HRESULT]
    SetIcon: _Callable[[_type.LPCWSTR],  # pszIcon
                       _type.HRESULT]
    Commit: _Callable[[],
                      _type.HRESULT]
    Save: _Callable[[IShellItem,  # psiFolderToSaveIn
                     _type.LPCWSTR,  # pszLibraryName
                     _enum.LIBRARYSAVEFLAGS,  # lsf
                     _Pointer[IShellItem]],  # ppsiSavedTo
                    _type.HRESULT]
    SaveInKnownFolder: _Callable[[_Pointer[_struct.KNOWNFOLDERID],  # kfidToSaveIn
                                  _type.LPCWSTR,  # pszLibraryName
                                  _enum.LIBRARYSAVEFLAGS,  # lsf
                                  _Pointer[IShellItem]],  # ppsiSavedTo
                                 _type.HRESULT]


class IDefaultFolderMenuInitialize(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.HWND,  # hwnd
                           IContextMenuCB,  # pcmcb
                           _Pointer[_struct.ITEMIDLIST],  # pidlFolder
                           IShellFolder,  # psf
                           _type.UINT,  # cidl
                           _Pointer[_Pointer[_struct.ITEMIDLIST]],  # apidl
                           _Unknwnbase.IUnknown,  # punkAssociation
                           _type.UINT,  # cKeys
                           _Pointer[_type.HKEY]],  # aKeys
                          _type.HRESULT]
    SetMenuRestrictions: _Callable[[_enum.DEFAULT_FOLDER_MENU_RESTRICTIONS],  # dfmrValues
                                   _type.HRESULT]
    GetMenuRestrictions: _Callable[[_enum.DEFAULT_FOLDER_MENU_RESTRICTIONS,  # dfmrMask
                                    _Pointer[_enum.DEFAULT_FOLDER_MENU_RESTRICTIONS]],  # pdfmrValues
                                   _type.HRESULT]
    SetHandlerClsid: _Callable[[_Pointer[_struct.IID]],  # rclsid
                               _type.HRESULT]


class IApplicationActivationManager(_Unknwnbase.IUnknown):
    ActivateApplication: _Callable[[_type.LPCWSTR,  # appUserModelId
                                    _type.LPCWSTR,  # arguments
                                    _enum.ACTIVATEOPTIONS,  # options
                                    _Pointer[_type.DWORD]],  # processId
                                   _type.HRESULT]
    ActivateForFile: _Callable[[_type.LPCWSTR,  # appUserModelId
                                IShellItemArray,  # itemArray
                                _type.LPCWSTR,  # verb
                                _Pointer[_type.DWORD]],  # processId
                               _type.HRESULT]
    ActivateForProtocol: _Callable[[_type.LPCWSTR,  # appUserModelId
                                    IShellItemArray,  # itemArray
                                    _Pointer[_type.DWORD]],  # processId
                                   _type.HRESULT]


class IVirtualDesktopManager(_Unknwnbase.IUnknown):
    IsWindowOnCurrentVirtualDesktop: _Callable[[_type.HWND,  # topLevelWindow
                                                _Pointer[_type.BOOL]],  # onCurrentDesktop
                                               _type.HRESULT]
    GetWindowDesktopId: _Callable[[_type.HWND,  # topLevelWindow
                                   _Pointer[_struct.GUID]],  # desktopId
                                  _type.HRESULT]
    MoveWindowToDesktop: _Callable[[_type.HWND,  # topLevelWindow
                                    _Pointer[_struct.GUID]],  # desktopId
                                   _type.HRESULT]


class IAssocHandlerInvoker(_Unknwnbase.IUnknown):
    SupportsSelection: _Callable[[],
                                 _type.HRESULT]
    Invoke: _Callable[[],
                      _type.HRESULT]


class IAssocHandler(_Unknwnbase.IUnknown):
    GetName: _Callable[[_Pointer[_type.LPWSTR]],  # ppsz
                       _type.HRESULT]
    GetUIName: _Callable[[_Pointer[_type.LPWSTR]],  # ppsz
                         _type.HRESULT]
    GetIconLocation: _Callable[[_Pointer[_type.LPWSTR],  # ppszPath
                                _Pointer[_type.c_int]],  # pIndex
                               _type.HRESULT]
    IsRecommended: _Callable[[],
                             _type.HRESULT]
    MakeDefault: _Callable[[_type.LPCWSTR],  # pszDescription
                           _type.HRESULT]
    Invoke: _Callable[[_objidl.IDataObject],  # pdo
                      _type.HRESULT]
    CreateInvoker: _Callable[[_objidl.IDataObject,  # pdo
                              _Pointer[IAssocHandlerInvoker]],  # ppInvoker
                             _type.HRESULT]


class IEnumAssocHandlers(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[IAssocHandler],  # rgelt
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]


class IDataObjectProvider(_Unknwnbase.IUnknown):
    GetDataObject: _Callable[[_Pointer[_objidl.IDataObject]],  # dataObject
                             _type.HRESULT]
    SetDataObject: _Callable[[_objidl.IDataObject],  # dataObject
                             _type.HRESULT]


class IDataTransferManagerInterop(_Unknwnbase.IUnknown):
    GetForWindow: _Callable[[_type.HWND,  # appWindow
                             _Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # dataTransferManager
                            _type.HRESULT]
    ShowShareUIForWindow: _Callable[[_type.HWND],  # appWindow
                                    _type.HRESULT]


class IFrameworkInputPaneHandler(_Unknwnbase.IUnknown):
    Showing: _Callable[[_Pointer[_struct.RECT],  # prcInputPaneScreenLocation
                        _type.BOOL],  # fEnsureFocusedElementInView
                       _type.HRESULT]
    Hiding: _Callable[[_type.BOOL],  # fEnsureFocusedElementInView
                      _type.HRESULT]


class IFrameworkInputPane(_Unknwnbase.IUnknown):
    Advise: _Callable[[_Unknwnbase.IUnknown,  # pWindow
                       IFrameworkInputPaneHandler,  # pHandler
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    AdviseWithHWND: _Callable[[_type.HWND,  # hwnd
                               IFrameworkInputPaneHandler,  # pHandler
                               _Pointer[_type.DWORD]],  # pdwCookie
                              _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]
    Location: _Callable[[_Pointer[_struct.RECT]],  # prcInputPaneScreenLocation
                        _type.HRESULT]


class IAppVisibilityEvents(_Unknwnbase.IUnknown):
    AppVisibilityOnMonitorChanged: _Callable[[_type.HMONITOR,  # hMonitor
                                              _enum.MONITOR_APP_VISIBILITY,  # previousMode
                                              _enum.MONITOR_APP_VISIBILITY],  # currentMode
                                             _type.HRESULT]
    LauncherVisibilityChange: _Callable[[_type.BOOL],  # currentVisibleState
                                        _type.HRESULT]


class IAppVisibility(_Unknwnbase.IUnknown):
    GetAppVisibilityOnMonitor: _Callable[[_type.HMONITOR,  # hMonitor
                                          _Pointer[_enum.MONITOR_APP_VISIBILITY]],  # pMode
                                         _type.HRESULT]
    IsLauncherVisible: _Callable[[_Pointer[_type.BOOL]],  # pfVisible
                                 _type.HRESULT]
    Advise: _Callable[[IAppVisibilityEvents,  # pCallback
                       _Pointer[_type.DWORD]],  # pdwCookie
                      _type.HRESULT]
    Unadvise: _Callable[[_type.DWORD],  # dwCookie
                        _type.HRESULT]


class IPackageExecutionStateChangeNotification(_Unknwnbase.IUnknown):
    OnStateChanged: _Callable[[_type.LPCWSTR,  # pszPackageFullName
                               _enum.PACKAGE_EXECUTION_STATE],  # pesNewState
                              _type.HRESULT]


class IPackageDebugSettings(_Unknwnbase.IUnknown):
    EnableDebugging: _Callable[[_type.LPCWSTR,  # packageFullName
                                _type.LPCWSTR,  # debuggerCommandLine
                                _Pointer[_type.WCHAR]],  # environment
                               _type.HRESULT]
    DisableDebugging: _Callable[[_type.LPCWSTR],  # packageFullName
                                _type.HRESULT]
    Suspend: _Callable[[_type.LPCWSTR],  # packageFullName
                       _type.HRESULT]
    Resume: _Callable[[_type.LPCWSTR],  # packageFullName
                      _type.HRESULT]
    TerminateAllProcesses: _Callable[[_type.LPCWSTR],  # packageFullName
                                     _type.HRESULT]
    SetTargetSessionId: _Callable[[_type.ULONG],  # sessionId
                                  _type.HRESULT]
    EnumerateBackgroundTasks: _Callable[[_type.LPCWSTR,  # packageFullName
                                         _Pointer[_type.ULONG],  # taskCount
                                         _Pointer[_Pointer[_struct.GUID]],  # taskIds
                                         _Pointer[_Pointer[_type.LPCWSTR]]],  # taskNames
                                        _type.HRESULT]
    ActivateBackgroundTask: _Callable[[_Pointer[_struct.GUID]],  # taskId
                                      _type.HRESULT]
    StartServicing: _Callable[[_type.LPCWSTR],  # packageFullName
                              _type.HRESULT]
    StopServicing: _Callable[[_type.LPCWSTR],  # packageFullName
                             _type.HRESULT]
    StartSessionRedirection: _Callable[[_type.LPCWSTR,  # packageFullName
                                        _type.ULONG],  # sessionId
                                       _type.HRESULT]
    StopSessionRedirection: _Callable[[_type.LPCWSTR],  # packageFullName
                                      _type.HRESULT]
    GetPackageExecutionState: _Callable[[_type.LPCWSTR,  # packageFullName
                                         _Pointer[_enum.PACKAGE_EXECUTION_STATE]],  # packageExecutionState
                                        _type.HRESULT]
    RegisterForPackageStateChanges: _Callable[[_type.LPCWSTR,  # packageFullName
                                               IPackageExecutionStateChangeNotification,  # pPackageExecutionStateChangeNotification
                                               _Pointer[_type.DWORD]],  # pdwCookie
                                              _type.HRESULT]
    UnregisterForPackageStateChanges: _Callable[[_type.DWORD],  # dwCookie
                                                _type.HRESULT]


class IPackageDebugSettings2(IPackageDebugSettings):
    EnumerateApps: _Callable[[_type.LPCWSTR,  # packageFullName
                              _Pointer[_type.ULONG],  # appCount
                              _Pointer[_Pointer[_type.LPWSTR]],  # appUserModelIds
                              _Pointer[_Pointer[_type.LPWSTR]]],  # appDisplayNames
                             _type.HRESULT]


class ISuspensionDependencyManager(_Unknwnbase.IUnknown):
    RegisterAsChild: _Callable[[_type.HANDLE],  # processHandle
                               _type.HRESULT]
    GroupChildWithParent: _Callable[[_type.HANDLE],  # childProcessHandle
                                    _type.HRESULT]
    UngroupChildFromParent: _Callable[[_type.HANDLE],  # childProcessHandle
                                      _type.HRESULT]


class IExecuteCommandApplicationHostEnvironment(_Unknwnbase.IUnknown):
    GetValue: _Callable[[_Pointer[_enum.AHE_TYPE]],  # pahe
                        _type.HRESULT]


class IExecuteCommandHost(_Unknwnbase.IUnknown):
    GetUIMode: _Callable[[_Pointer[_enum.EC_HOST_UI_MODE]],  # pUIMode
                         _type.HRESULT]


class IApplicationDesignModeSettings(_Unknwnbase.IUnknown):
    SetNativeDisplaySize: _Callable[[_struct.SIZE],  # nativeDisplaySizePixels
                                    _type.HRESULT]
    SetScaleFactor: _Callable[[_enum.DEVICE_SCALE_FACTOR],  # scaleFactor
                              _type.HRESULT]
    SetApplicationViewState: _Callable[[_enum.APPLICATION_VIEW_STATE],  # viewState
                                       _type.HRESULT]
    ComputeApplicationSize: _Callable[[_Pointer[_struct.SIZE]],  # applicationSizePixels
                                      _type.HRESULT]
    IsApplicationViewStateSupported: _Callable[[_enum.APPLICATION_VIEW_STATE,  # viewState
                                                _struct.SIZE,  # nativeDisplaySizePixels
                                                _enum.DEVICE_SCALE_FACTOR,  # scaleFactor
                                                _Pointer[_type.BOOL]],  # supported
                                               _type.HRESULT]
    TriggerEdgeGesture: _Callable[[_enum.EDGE_GESTURE_KIND],  # edgeGestureKind
                                  _type.HRESULT]


class IApplicationDesignModeSettings2(IApplicationDesignModeSettings):
    SetNativeDisplayOrientation: _Callable[[_enum.NATIVE_DISPLAY_ORIENTATION],  # nativeDisplayOrientation
                                           _type.HRESULT]
    SetApplicationViewOrientation: _Callable[[_enum.APPLICATION_VIEW_ORIENTATION],  # viewOrientation
                                             _type.HRESULT]
    SetAdjacentDisplayEdges: _Callable[[_enum.ADJACENT_DISPLAY_EDGES],  # adjacentDisplayEdges
                                       _type.HRESULT]
    SetIsOnLockScreen: _Callable[[_type.BOOL],  # isOnLockScreen
                                 _type.HRESULT]
    SetApplicationViewMinWidth: _Callable[[_enum.APPLICATION_VIEW_MIN_WIDTH],  # viewMinWidth
                                          _type.HRESULT]
    GetApplicationSizeBounds: _Callable[[_Pointer[_struct.SIZE],  # minApplicationSizePixels
                                         _Pointer[_struct.SIZE]],  # maxApplicationSizePixels
                                        _type.HRESULT]
    GetApplicationViewOrientation: _Callable[[_struct.SIZE,  # applicationSizePixels
                                              _Pointer[_enum.APPLICATION_VIEW_ORIENTATION]],  # viewOrientation
                                             _type.HRESULT]


class ILaunchTargetMonitor(_Unknwnbase.IUnknown):
    GetMonitor: _Callable[[_Pointer[_type.HMONITOR]],  # monitor
                          _type.HRESULT]


class ILaunchSourceViewSizePreference(_Unknwnbase.IUnknown):
    GetSourceViewToPosition: _Callable[[_Pointer[_type.HWND]],  # hwnd
                                       _type.HRESULT]
    GetSourceViewSizePreference: _Callable[[_Pointer[_enum.APPLICATION_VIEW_SIZE_PREFERENCE]],  # sourceSizeAfterLaunch
                                           _type.HRESULT]


class ILaunchTargetViewSizePreference(_Unknwnbase.IUnknown):
    GetTargetViewSizePreference: _Callable[[_Pointer[_enum.APPLICATION_VIEW_SIZE_PREFERENCE]],  # targetSizeOnLaunch
                                           _type.HRESULT]


class ILaunchSourceAppUserModelId(_Unknwnbase.IUnknown):
    GetAppUserModelId: _Callable[[_Pointer[_type.LPWSTR]],  # launchingApp
                                 _type.HRESULT]


class IInitializeWithWindow(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.HWND],  # hwnd
                          _type.HRESULT]


class IHandlerInfo(_Unknwnbase.IUnknown):
    GetApplicationDisplayName: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                         _type.HRESULT]
    GetApplicationPublisher: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                       _type.HRESULT]
    GetApplicationIconReference: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                           _type.HRESULT]


class IHandlerInfo2(IHandlerInfo):
    GetApplicationId: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                _type.HRESULT]


class IHandlerActivationHost(_Unknwnbase.IUnknown):
    BeforeCoCreateInstance: _Callable[[_Pointer[_struct.IID],  # clsidHandler
                                       IShellItemArray,  # itemsBeingActivated
                                       IHandlerInfo],  # handlerInfo
                                      _type.HRESULT]
    BeforeCreateProcess: _Callable[[_type.LPCWSTR,  # applicationPath
                                    _type.LPCWSTR,  # commandLine
                                    IHandlerInfo],  # handlerInfo
                                   _type.HRESULT]


class IAppActivationUIInfo(_Unknwnbase.IUnknown):
    GetMonitor: _Callable[[_Pointer[_type.HMONITOR]],  # value
                          _type.HRESULT]
    GetInvokePoint: _Callable[[_Pointer[_struct.POINT]],  # value
                              _type.HRESULT]
    GetShowCommand: _Callable[[_Pointer[_type.c_int]],  # value
                              _type.HRESULT]
    GetShowUI: _Callable[[_Pointer[_type.BOOL]],  # value
                         _type.HRESULT]
    GetKeyState: _Callable[[_Pointer[_type.DWORD]],  # value
                           _type.HRESULT]


class IContactManagerInterop(_Unknwnbase.IUnknown):
    ShowContactCardForWindow: _Callable[[_type.HWND,  # appWindow
                                         _Unknwnbase.IUnknown,  # contact
                                         _Pointer[_struct.RECT],  # selection
                                         _enum.FLYOUT_PLACEMENT],  # preferredPlacement
                                        _type.HRESULT]


class IShellIconOverlayIdentifier(_Unknwnbase.IUnknown):
    IsMemberOf: _Callable[[_type.LPCWSTR,  # pwszPath
                           _type.DWORD],  # dwAttrib
                          _type.HRESULT]
    GetOverlayInfo: _Callable[[_type.LPWSTR,  # pwszIconFile
                               _type.c_int,  # cchMax
                               _Pointer[_type.c_int],  # pIndex
                               _Pointer[_type.DWORD]],  # pdwFlags
                              _type.HRESULT]
    GetPriority: _Callable[[_Pointer[_type.c_int]],  # pPriority
                           _type.HRESULT]


class IBannerNotificationHandler(_Unknwnbase.IUnknown):
    OnBannerEvent: _Callable[[_Pointer[_struct.BANNER_NOTIFICATION]],  # notification
                             _type.HRESULT]


class ISortColumnArray(_Unknwnbase.IUnknown):
    GetCount: _Callable[[_Pointer[_type.UINT]],  # columnCount
                        _type.HRESULT]
    GetAt: _Callable[[_type.UINT,  # index
                      _Pointer[_struct.SORTCOLUMN]],  # sortcolumn
                     _type.HRESULT]
    GetSortType: _Callable[[_Pointer[_enum.SORT_ORDER_TYPE]],  # type
                           _type.HRESULT]


class IPropertyKeyStore(_Unknwnbase.IUnknown):
    GetKeyCount: _Callable[[_Pointer[_type.c_int]],  # keyCount
                           _type.HRESULT]
    GetKeyAt: _Callable[[_type.c_int,  # index
                         _Pointer[_struct.PROPERTYKEY]],  # pkey
                        _type.HRESULT]
    AppendKey: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # key
                         _type.HRESULT]
    DeleteKey: _Callable[[_type.c_int],  # index
                         _type.HRESULT]
    IsKeyInStore: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # key
                            _type.HRESULT]
    RemoveKey: _Callable[[_Pointer[_struct.PROPERTYKEY]],  # key
                         _type.HRESULT]
