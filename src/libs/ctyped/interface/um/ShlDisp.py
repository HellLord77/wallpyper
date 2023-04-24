from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from . import objidl as _objidl
from . import objidlbase as _objidlbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IFolderViewOC(_oaidl.IDispatch):
    SetFolderView: _Callable[[_oaidl.IDispatch],  # pdisp
                             _type.HRESULT]


class DShellFolderViewEvents(_oaidl.IDispatch):
    pass


class DFConstraint(_oaidl.IDispatch):
    get_Name: _Callable[[_Pointer[_type.BSTR]],  # pbs
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_struct.VARIANT]],  # pv
                         _type.HRESULT]


class FolderItem(_oaidl.IDispatch):
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                          _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.BSTR]],  # pbs
                        _type.HRESULT]
    put_Name: _Callable[[_type.BSTR],  # bs
                        _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.BSTR]],  # pbs
                        _type.HRESULT]
    get_GetLink: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                           _type.HRESULT]
    get_GetFolder: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                             _type.HRESULT]
    get_IsLink: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pb
                          _type.HRESULT]
    get_IsFolder: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pb
                            _type.HRESULT]
    get_IsFileSystem: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pb
                                _type.HRESULT]
    get_IsBrowsable: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pb
                               _type.HRESULT]
    get_ModifyDate: _Callable[[_Pointer[_type.DATE]],  # pdt
                              _type.HRESULT]
    put_ModifyDate: _Callable[[_type.DATE],  # dt
                              _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.LONG]],  # pul
                        _type.HRESULT]
    get_Type: _Callable[[_Pointer[_type.BSTR]],  # pbs
                        _type.HRESULT]
    Verbs: _Callable[[_Pointer[FolderItemVerbs]],  # ppfic
                     _type.HRESULT]
    InvokeVerb: _Callable[[_struct.VARIANT],  # vVerb
                          _type.HRESULT]


class FolderItems(_oaidl.IDispatch):
    get_Count: _Callable[[_Pointer[_type.c_long]],  # plCount
                         _type.HRESULT]
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                          _type.HRESULT]
    Item: _Callable[[_struct.VARIANT,  # index
                     _Pointer[FolderItem]],  # ppid
                    _type.HRESULT]
    _NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppunk
                        _type.HRESULT]


class FolderItemVerb(_oaidl.IDispatch):
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                          _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.BSTR]],  # pbs
                        _type.HRESULT]
    DoIt: _Callable[[],
                    _type.HRESULT]


class FolderItemVerbs(_oaidl.IDispatch):
    get_Count: _Callable[[_Pointer[_type.c_long]],  # plCount
                         _type.HRESULT]
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                          _type.HRESULT]
    Item: _Callable[[_struct.VARIANT,  # index
                     _Pointer[FolderItemVerb]],  # ppid
                    _type.HRESULT]
    _NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppunk
                        _type.HRESULT]


class Folder(_oaidl.IDispatch):
    get_Title: _Callable[[_Pointer[_type.BSTR]],  # pbs
                         _type.HRESULT]
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                          _type.HRESULT]
    get_ParentFolder: _Callable[[_Pointer[Folder]],  # ppsf
                                _type.HRESULT]
    Items: _Callable[[_Pointer[FolderItems]],  # ppid
                     _type.HRESULT]
    ParseName: _Callable[[_type.BSTR,  # bName
                          _Pointer[FolderItem]],  # ppid
                         _type.HRESULT]
    NewFolder: _Callable[[_type.BSTR,  # bName
                          _struct.VARIANT],  # vOptions
                         _type.HRESULT]
    MoveHere: _Callable[[_struct.VARIANT,  # vItem
                         _struct.VARIANT],  # vOptions
                        _type.HRESULT]
    CopyHere: _Callable[[_struct.VARIANT,  # vItem
                         _struct.VARIANT],  # vOptions
                        _type.HRESULT]
    GetDetailsOf: _Callable[[_struct.VARIANT,  # vItem
                             _type.c_int,  # iColumn
                             _Pointer[_type.BSTR]],  # pbs
                            _type.HRESULT]


class Folder2(Folder):
    get_Self: _Callable[[_Pointer[FolderItem]],  # ppfi
                        _type.HRESULT]
    get_OfflineStatus: _Callable[[_Pointer[_type.LONG]],  # pul
                                 _type.HRESULT]
    Synchronize: _Callable[[],
                           _type.HRESULT]
    get_HaveToShowWebViewBarricade: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbHaveToShowWebViewBarricade
                                              _type.HRESULT]
    DismissedWebViewBarricade: _Callable[[],
                                         _type.HRESULT]


class Folder3(Folder2):
    get_ShowWebViewBarricade: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbShowWebViewBarricade
                                        _type.HRESULT]
    put_ShowWebViewBarricade: _Callable[[_type.VARIANT_BOOL],  # bShowWebViewBarricade
                                        _type.HRESULT]


class FolderItem2(FolderItem):
    InvokeVerbEx: _Callable[[_struct.VARIANT,  # vVerb
                             _struct.VARIANT],  # vArgs
                            _type.HRESULT]
    ExtendedProperty: _Callable[[_type.BSTR,  # bstrPropName
                                 _Pointer[_struct.VARIANT]],  # pvRet
                                _type.HRESULT]


class FolderItems2(FolderItems):
    InvokeVerbEx: _Callable[[_struct.VARIANT,  # vVerb
                             _struct.VARIANT],  # vArgs
                            _type.HRESULT]


class FolderItems3(FolderItems2):
    Filter: _Callable[[_type.c_long,  # grfFlags
                       _type.BSTR],  # bstrFileSpec
                      _type.HRESULT]
    get_Verbs: _Callable[[_Pointer[FolderItemVerbs]],  # ppfic
                         _type.HRESULT]


class IShellLinkDual(_oaidl.IDispatch):
    get_Path: _Callable[[_Pointer[_type.BSTR]],  # pbs
                        _type.HRESULT]
    put_Path: _Callable[[_type.BSTR],  # bs
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.BSTR]],  # pbs
                               _type.HRESULT]
    put_Description: _Callable[[_type.BSTR],  # bs
                               _type.HRESULT]
    get_WorkingDirectory: _Callable[[_Pointer[_type.BSTR]],  # pbs
                                    _type.HRESULT]
    put_WorkingDirectory: _Callable[[_type.BSTR],  # bs
                                    _type.HRESULT]
    get_Arguments: _Callable[[_Pointer[_type.BSTR]],  # pbs
                             _type.HRESULT]
    put_Arguments: _Callable[[_type.BSTR],  # bs
                             _type.HRESULT]
    get_Hotkey: _Callable[[_Pointer[_type.c_int]],  # piHK
                          _type.HRESULT]
    put_Hotkey: _Callable[[_type.c_int],  # iHK
                          _type.HRESULT]
    get_ShowCommand: _Callable[[_Pointer[_type.c_int]],  # piShowCommand
                               _type.HRESULT]
    put_ShowCommand: _Callable[[_type.c_int],  # iShowCommand
                               _type.HRESULT]
    Resolve: _Callable[[_type.c_int],  # fFlags
                       _type.HRESULT]
    GetIconLocation: _Callable[[_Pointer[_type.BSTR],  # pbs
                                _Pointer[_type.c_int]],  # piIcon
                               _type.HRESULT]
    SetIconLocation: _Callable[[_type.BSTR,  # bs
                                _type.c_int],  # iIcon
                               _type.HRESULT]
    Save: _Callable[[_struct.VARIANT],  # vWhere
                    _type.HRESULT]


class IShellLinkDual2(IShellLinkDual):
    get_Target: _Callable[[_Pointer[FolderItem]],  # ppfi
                          _type.HRESULT]


class IShellFolderViewDual(_oaidl.IDispatch):
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                          _type.HRESULT]
    get_Folder: _Callable[[_Pointer[Folder]],  # ppid
                          _type.HRESULT]
    SelectedItems: _Callable[[_Pointer[FolderItems]],  # ppid
                             _type.HRESULT]
    get_FocusedItem: _Callable[[_Pointer[FolderItem]],  # ppid
                               _type.HRESULT]
    SelectItem: _Callable[[_Pointer[_struct.VARIANT],  # pvfi
                           _type.c_int],  # dwFlags
                          _type.HRESULT]
    PopupItemMenu: _Callable[[FolderItem,  # pfi
                              _struct.VARIANT,  # vx
                              _struct.VARIANT,  # vy
                              _Pointer[_type.BSTR]],  # pbs
                             _type.HRESULT]
    get_Script: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDisp
                          _type.HRESULT]
    get_ViewOptions: _Callable[[_Pointer[_type.c_long]],  # plViewOptions
                               _type.HRESULT]


class IShellFolderViewDual2(IShellFolderViewDual):
    get_CurrentViewMode: _Callable[[_Pointer[_type.UINT]],  # pViewMode
                                   _type.HRESULT]
    put_CurrentViewMode: _Callable[[_type.UINT],  # ViewMode
                                   _type.HRESULT]
    SelectItemRelative: _Callable[[_type.c_int],  # iRelative
                                  _type.HRESULT]


class IShellFolderViewDual3(IShellFolderViewDual2):
    get_GroupBy: _Callable[[_Pointer[_type.BSTR]],  # pbstrGroupBy
                           _type.HRESULT]
    put_GroupBy: _Callable[[_type.BSTR],  # bstrGroupBy
                           _type.HRESULT]
    get_FolderFlags: _Callable[[_Pointer[_type.DWORD]],  # pdwFlags
                               _type.HRESULT]
    put_FolderFlags: _Callable[[_type.DWORD],  # dwFlags
                               _type.HRESULT]
    get_SortColumns: _Callable[[_Pointer[_type.BSTR]],  # pbstrSortColumns
                               _type.HRESULT]
    put_SortColumns: _Callable[[_type.BSTR],  # bstrSortColumns
                               _type.HRESULT]
    put_IconSize: _Callable[[_type.c_int],  # iIconSize
                            _type.HRESULT]
    get_IconSize: _Callable[[_Pointer[_type.c_int]],  # piIconSize
                            _type.HRESULT]
    FilterView: _Callable[[_type.BSTR],  # bstrFilterText
                          _type.HRESULT]


class IShellDispatch(_oaidl.IDispatch):
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                          _type.HRESULT]
    NameSpace: _Callable[[_struct.VARIANT,  # vDir
                          _Pointer[Folder]],  # ppsdf
                         _type.HRESULT]
    BrowseForFolder: _Callable[[_type.c_long,  # Hwnd
                                _type.BSTR,  # Title
                                _type.c_long,  # Options
                                _struct.VARIANT,  # RootFolder
                                _Pointer[Folder]],  # ppsdf
                               _type.HRESULT]
    Windows: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                       _type.HRESULT]
    Open: _Callable[[_struct.VARIANT],  # vDir
                    _type.HRESULT]
    Explore: _Callable[[_struct.VARIANT],  # vDir
                       _type.HRESULT]
    MinimizeAll: _Callable[[],
                           _type.HRESULT]
    UndoMinimizeALL: _Callable[[],
                               _type.HRESULT]
    FileRun: _Callable[[],
                       _type.HRESULT]
    CascadeWindows: _Callable[[],
                              _type.HRESULT]
    TileVertically: _Callable[[],
                              _type.HRESULT]
    TileHorizontally: _Callable[[],
                                _type.HRESULT]
    ShutdownWindows: _Callable[[],
                               _type.HRESULT]
    Suspend: _Callable[[],
                       _type.HRESULT]
    EjectPC: _Callable[[],
                       _type.HRESULT]
    SetTime: _Callable[[],
                       _type.HRESULT]
    TrayProperties: _Callable[[],
                              _type.HRESULT]
    Help: _Callable[[],
                    _type.HRESULT]
    FindFiles: _Callable[[],
                         _type.HRESULT]
    FindComputer: _Callable[[],
                            _type.HRESULT]
    RefreshMenu: _Callable[[],
                           _type.HRESULT]
    ControlPanelItem: _Callable[[_type.BSTR],  # bstrDir
                                _type.HRESULT]


class IShellDispatch2(IShellDispatch):
    IsRestricted: _Callable[[_type.BSTR,  # Group
                             _type.BSTR,  # Restriction
                             _Pointer[_type.c_long]],  # plRestrictValue
                            _type.HRESULT]
    ShellExecute: _Callable[[_type.BSTR,  # File
                             _struct.VARIANT,  # vArgs
                             _struct.VARIANT,  # vDir
                             _struct.VARIANT,  # vOperation
                             _struct.VARIANT],  # vShow
                            _type.HRESULT]
    FindPrinter: _Callable[[_type.BSTR,  # name
                            _type.BSTR,  # location
                            _type.BSTR],  # model
                           _type.HRESULT]
    GetSystemInformation: _Callable[[_type.BSTR,  # name
                                     _Pointer[_struct.VARIANT]],  # pv
                                    _type.HRESULT]
    ServiceStart: _Callable[[_type.BSTR,  # ServiceName
                             _struct.VARIANT,  # Persistent
                             _Pointer[_struct.VARIANT]],  # pSuccess
                            _type.HRESULT]
    ServiceStop: _Callable[[_type.BSTR,  # ServiceName
                            _struct.VARIANT,  # Persistent
                            _Pointer[_struct.VARIANT]],  # pSuccess
                           _type.HRESULT]
    IsServiceRunning: _Callable[[_type.BSTR,  # ServiceName
                                 _Pointer[_struct.VARIANT]],  # pRunning
                                _type.HRESULT]
    CanStartStopService: _Callable[[_type.BSTR,  # ServiceName
                                    _Pointer[_struct.VARIANT]],  # pCanStartStop
                                   _type.HRESULT]
    ShowBrowserBar: _Callable[[_type.BSTR,  # bstrClsid
                               _struct.VARIANT,  # bShow
                               _Pointer[_struct.VARIANT]],  # pSuccess
                              _type.HRESULT]


class IShellDispatch3(IShellDispatch2):
    AddToRecent: _Callable[[_struct.VARIANT,  # varFile
                            _type.BSTR],  # bstrCategory
                           _type.HRESULT]


class IShellDispatch4(IShellDispatch3):
    WindowsSecurity: _Callable[[],
                               _type.HRESULT]
    ToggleDesktop: _Callable[[],
                             _type.HRESULT]
    ExplorerPolicy: _Callable[[_type.BSTR,  # bstrPolicyName
                               _Pointer[_struct.VARIANT]],  # pValue
                              _type.HRESULT]
    GetSetting: _Callable[[_type.c_long,  # lSetting
                           _Pointer[_type.VARIANT_BOOL]],  # pResult
                          _type.HRESULT]


class IShellDispatch5(IShellDispatch4):
    WindowSwitcher: _Callable[[],
                              _type.HRESULT]


class IShellDispatch6(IShellDispatch5):
    SearchCommand: _Callable[[],
                             _type.HRESULT]


class IFileSearchBand(_oaidl.IDispatch):
    SetFocus: _Callable[[],
                        _type.HRESULT]
    SetSearchParameters: _Callable[[_Pointer[_type.BSTR],  # pbstrSearchID
                                    _type.VARIANT_BOOL,  # bNavToResults
                                    _Pointer[_struct.VARIANT],  # pvarScope
                                    _Pointer[_struct.VARIANT]],  # pvarQueryFile
                                   _type.HRESULT]
    get_SearchID: _Callable[[_Pointer[_type.BSTR]],  # pbstrSearchID
                            _type.HRESULT]
    get_Scope: _Callable[[_Pointer[_struct.VARIANT]],  # pvarScope
                         _type.HRESULT]
    get_QueryFile: _Callable[[_Pointer[_struct.VARIANT]],  # pvarFile
                             _type.HRESULT]


class IWebWizardHost(_oaidl.IDispatch):
    FinalBack: _Callable[[],
                         _type.HRESULT]
    FinalNext: _Callable[[],
                         _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    put_Caption: _Callable[[_type.BSTR],  # bstrCaption
                           _type.HRESULT]
    get_Caption: _Callable[[_Pointer[_type.BSTR]],  # pbstrCaption
                           _type.HRESULT]
    put_Property: _Callable[[_type.BSTR,  # bstrPropertyName
                             _Pointer[_struct.VARIANT]],  # pvProperty
                            _type.HRESULT]
    get_Property: _Callable[[_type.BSTR,  # bstrPropertyName
                             _Pointer[_struct.VARIANT]],  # pvProperty
                            _type.HRESULT]
    SetWizardButtons: _Callable[[_type.VARIANT_BOOL,  # vfEnableBack
                                 _type.VARIANT_BOOL,  # vfEnableNext
                                 _type.VARIANT_BOOL],  # vfLastPage
                                _type.HRESULT]
    SetHeaderText: _Callable[[_type.BSTR,  # bstrHeaderTitle
                              _type.BSTR],  # bstrHeaderSubtitle
                             _type.HRESULT]


class IWebWizardHost2(IWebWizardHost):
    SignString: _Callable[[_type.BSTR,  # value
                           _Pointer[_type.BSTR]],  # signedValue
                          _type.HRESULT]


class INewWDEvents(IWebWizardHost):
    PassportAuthenticate: _Callable[[_type.BSTR,  # bstrSignInUrl
                                     _Pointer[_type.VARIANT_BOOL]],  # pvfAuthenitcated
                                    _type.HRESULT]


class IAutoComplete(_Unknwnbase.IUnknown):
    Init: _Callable[[_type.HWND,  # hwndEdit
                     _Unknwnbase.IUnknown,  # punkACL
                     _type.LPCWSTR,  # pwszRegKeyPath
                     _type.LPCWSTR],  # pwszQuickComplete
                    _type.HRESULT]
    Enable: _Callable[[_type.BOOL],  # fEnable
                      _type.HRESULT]


class IAutoComplete2(IAutoComplete):
    SetOptions: _Callable[[_type.DWORD],  # dwFlag
                          _type.HRESULT]
    GetOptions: _Callable[[_Pointer[_type.DWORD]],  # pdwFlag
                          _type.HRESULT]


class IEnumACString(_objidlbase.IEnumString):
    NextItem: _Callable[[_type.LPWSTR,  # pszUrl
                         _type.ULONG,  # cchMax
                         _Pointer[_type.ULONG]],  # pulSortIndex
                        _type.HRESULT]
    SetEnumOptions: _Callable[[_type.DWORD],  # dwOptions
                              _type.HRESULT]
    GetEnumOptions: _Callable[[_Pointer[_type.DWORD]],  # pdwOptions
                              _type.HRESULT]


class IDataObjectAsyncCapability(_Unknwnbase.IUnknown):
    SetAsyncMode: _Callable[[_type.BOOL],  # fDoOpAsync
                            _type.HRESULT]
    GetAsyncMode: _Callable[[_Pointer[_type.BOOL]],  # pfIsOpAsync
                            _type.HRESULT]
    StartOperation: _Callable[[_objidl.IBindCtx],  # pbcReserved
                              _type.HRESULT]
    InOperation: _Callable[[_Pointer[_type.BOOL]],  # pfInAsyncOp
                           _type.HRESULT]
    EndOperation: _Callable[[_type.HRESULT,  # hResult
                             _objidl.IBindCtx,  # pbcReserved
                             _type.DWORD],  # dwEffects
                            _type.HRESULT]
