from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IWebBrowser(_oaidl.IDispatch):
    GoBack: _Callable[[],
                      _type.HRESULT]
    GoForward: _Callable[[],
                         _type.HRESULT]
    GoHome: _Callable[[],
                      _type.HRESULT]
    GoSearch: _Callable[[],
                        _type.HRESULT]
    Navigate: _Callable[[_type.BSTR,  # URL
                         _Pointer[_struct.VARIANT],  # Flags
                         _Pointer[_struct.VARIANT],  # TargetFrameName
                         _Pointer[_struct.VARIANT],  # PostData
                         _Pointer[_struct.VARIANT]],  # Headers
                        _type.HRESULT]
    Refresh: _Callable[[],
                       _type.HRESULT]
    Refresh2: _Callable[[_Pointer[_struct.VARIANT]],  # Level
                        _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    get_Application: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDisp
                               _type.HRESULT]
    get_Parent: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDisp
                          _type.HRESULT]
    get_Container: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDisp
                             _type.HRESULT]
    get_Document: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppDisp
                            _type.HRESULT]
    get_TopLevelContainer: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pBool
                                     _type.HRESULT]
    get_Type: _Callable[[_Pointer[_type.BSTR]],  # Type
                        _type.HRESULT]
    get_Left: _Callable[[_Pointer[_type.c_long]],  # pl
                        _type.HRESULT]
    put_Left: _Callable[[_type.c_long],  # Left
                        _type.HRESULT]
    get_Top: _Callable[[_Pointer[_type.c_long]],  # pl
                       _type.HRESULT]
    put_Top: _Callable[[_type.c_long],  # Top
                       _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.c_long]],  # pl
                         _type.HRESULT]
    put_Width: _Callable[[_type.c_long],  # Width
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.c_long]],  # pl
                          _type.HRESULT]
    put_Height: _Callable[[_type.c_long],  # Height
                          _type.HRESULT]
    get_LocationName: _Callable[[_Pointer[_type.BSTR]],  # LocationName
                                _type.HRESULT]
    get_LocationURL: _Callable[[_Pointer[_type.BSTR]],  # LocationURL
                               _type.HRESULT]
    get_Busy: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pBool
                        _type.HRESULT]


class DWebBrowserEvents(_oaidl.IDispatch):
    pass


class IWebBrowserApp(IWebBrowser):
    Quit: _Callable[[],
                    _type.HRESULT]
    ClientToWindow: _Callable[[_Pointer[_type.c_int],  # pcx
                               _Pointer[_type.c_int]],  # pcy
                              _type.HRESULT]
    PutProperty: _Callable[[_type.BSTR,  # Property
                            _struct.VARIANT],  # vtValue
                           _type.HRESULT]
    GetProperty: _Callable[[_type.BSTR,  # Property
                            _Pointer[_struct.VARIANT]],  # pvtValue
                           _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.BSTR]],  # Name
                        _type.HRESULT]
    get_HWND: _Callable[[_Pointer[_type.SHANDLE_PTR]],  # pHWND
                        _type.HRESULT]
    get_FullName: _Callable[[_Pointer[_type.BSTR]],  # FullName
                            _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.BSTR]],  # Path
                        _type.HRESULT]
    get_Visible: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pBool
                           _type.HRESULT]
    put_Visible: _Callable[[_type.VARIANT_BOOL],  # Value
                           _type.HRESULT]
    get_StatusBar: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pBool
                             _type.HRESULT]
    put_StatusBar: _Callable[[_type.VARIANT_BOOL],  # Value
                             _type.HRESULT]
    get_StatusText: _Callable[[_Pointer[_type.BSTR]],  # StatusText
                              _type.HRESULT]
    put_StatusText: _Callable[[_type.BSTR],  # StatusText
                              _type.HRESULT]
    get_ToolBar: _Callable[[_Pointer[_type.c_int]],  # Value
                           _type.HRESULT]
    put_ToolBar: _Callable[[_type.c_int],  # Value
                           _type.HRESULT]
    get_MenuBar: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # Value
                           _type.HRESULT]
    put_MenuBar: _Callable[[_type.VARIANT_BOOL],  # Value
                           _type.HRESULT]
    get_FullScreen: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbFullScreen
                              _type.HRESULT]
    put_FullScreen: _Callable[[_type.VARIANT_BOOL],  # bFullScreen
                              _type.HRESULT]


class IWebBrowser2(IWebBrowserApp):
    Navigate2: _Callable[[_Pointer[_struct.VARIANT],  # URL
                          _Pointer[_struct.VARIANT],  # Flags
                          _Pointer[_struct.VARIANT],  # TargetFrameName
                          _Pointer[_struct.VARIANT],  # PostData
                          _Pointer[_struct.VARIANT]],  # Headers
                         _type.HRESULT]
    QueryStatusWB: _Callable[[_enum.OLECMDID,  # cmdID
                              _Pointer[_enum.OLECMDF]],  # pcmdf
                             _type.HRESULT]
    ExecWB: _Callable[[_enum.OLECMDID,  # cmdID
                       _enum.OLECMDEXECOPT,  # cmdexecopt
                       _Pointer[_struct.VARIANT],  # pvaIn
                       _Pointer[_struct.VARIANT]],  # pvaOut
                      _type.HRESULT]
    ShowBrowserBar: _Callable[[_Pointer[_struct.VARIANT],  # pvaClsid
                               _Pointer[_struct.VARIANT],  # pvarShow
                               _Pointer[_struct.VARIANT]],  # pvarSize
                              _type.HRESULT]
    get_ReadyState: _Callable[[_Pointer[_enum.READYSTATE]],  # plReadyState
                              _type.HRESULT]
    get_Offline: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbOffline
                           _type.HRESULT]
    put_Offline: _Callable[[_type.VARIANT_BOOL],  # bOffline
                           _type.HRESULT]
    get_Silent: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbSilent
                          _type.HRESULT]
    put_Silent: _Callable[[_type.VARIANT_BOOL],  # bSilent
                          _type.HRESULT]
    get_RegisterAsBrowser: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbRegister
                                     _type.HRESULT]
    put_RegisterAsBrowser: _Callable[[_type.VARIANT_BOOL],  # bRegister
                                     _type.HRESULT]
    get_RegisterAsDropTarget: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbRegister
                                        _type.HRESULT]
    put_RegisterAsDropTarget: _Callable[[_type.VARIANT_BOOL],  # bRegister
                                        _type.HRESULT]
    get_TheaterMode: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pbRegister
                               _type.HRESULT]
    put_TheaterMode: _Callable[[_type.VARIANT_BOOL],  # bRegister
                               _type.HRESULT]
    get_AddressBar: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # Value
                              _type.HRESULT]
    put_AddressBar: _Callable[[_type.VARIANT_BOOL],  # Value
                              _type.HRESULT]
    get_Resizable: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # Value
                             _type.HRESULT]
    put_Resizable: _Callable[[_type.VARIANT_BOOL],  # Value
                             _type.HRESULT]


class DWebBrowserEvents2(_oaidl.IDispatch):
    pass


class DShellWindowsEvents(_oaidl.IDispatch):
    pass


class IShellWindows(_oaidl.IDispatch):
    get_Count: _Callable[[_Pointer[_type.c_long]],  # Count
                         _type.HRESULT]
    Item: _Callable[[_struct.VARIANT,  # index
                     _Pointer[_oaidl.IDispatch]],  # Folder
                    _type.HRESULT]
    _NewEnum: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppunk
                        _type.HRESULT]
    Register: _Callable[[_oaidl.IDispatch,  # pid
                         _type.c_long,  # hwnd
                         _type.c_int,  # swClass
                         _Pointer[_type.c_long]],  # plCookie
                        _type.HRESULT]
    RegisterPending: _Callable[[_type.c_long,  # lThreadId
                                _Pointer[_struct.VARIANT],  # pvarloc
                                _Pointer[_struct.VARIANT],  # pvarlocRoot
                                _type.c_int,  # swClass
                                _Pointer[_type.c_long]],  # plCookie
                               _type.HRESULT]
    Revoke: _Callable[[_type.c_long],  # lCookie
                      _type.HRESULT]
    OnNavigate: _Callable[[_type.c_long,  # lCookie
                           _Pointer[_struct.VARIANT]],  # pvarLoc
                          _type.HRESULT]
    OnActivated: _Callable[[_type.c_long,  # lCookie
                            _type.VARIANT_BOOL],  # fActive
                           _type.HRESULT]
    FindWindowSW: _Callable[[_Pointer[_struct.VARIANT],  # pvarLoc
                             _Pointer[_struct.VARIANT],  # pvarLocRoot
                             _type.c_int,  # swClass
                             _Pointer[_type.c_long],  # phwnd
                             _type.c_int,  # swfwOptions
                             _Pointer[_oaidl.IDispatch]],  # ppdispOut
                            _type.HRESULT]
    OnCreated: _Callable[[_type.c_long,  # lCookie
                          _Unknwnbase.IUnknown],  # punk
                         _type.HRESULT]
    ProcessAttachDetach: _Callable[[_type.VARIANT_BOOL],  # fAttach
                                   _type.HRESULT]


class IShellUIHelper(_oaidl.IDispatch):
    ResetFirstBootMode: _Callable[[],
                                  _type.HRESULT]
    ResetSafeMode: _Callable[[],
                             _type.HRESULT]
    RefreshOfflineDesktop: _Callable[[],
                                     _type.HRESULT]
    AddFavorite: _Callable[[_type.BSTR,  # URL
                            _Pointer[_struct.VARIANT]],  # Title
                           _type.HRESULT]
    AddChannel: _Callable[[_type.BSTR],  # URL
                          _type.HRESULT]
    AddDesktopComponent: _Callable[[_type.BSTR,  # URL
                                    _type.BSTR,  # Type
                                    _Pointer[_struct.VARIANT],  # Left
                                    _Pointer[_struct.VARIANT],  # Top
                                    _Pointer[_struct.VARIANT],  # Width
                                    _Pointer[_struct.VARIANT]],  # Height
                                   _type.HRESULT]
    IsSubscribed: _Callable[[_type.BSTR,  # URL
                             _Pointer[_type.VARIANT_BOOL]],  # pBool
                            _type.HRESULT]
    NavigateAndFind: _Callable[[_type.BSTR,  # URL
                                _type.BSTR,  # strQuery
                                _Pointer[_struct.VARIANT]],  # varTargetFrame
                               _type.HRESULT]
    ImportExportFavorites: _Callable[[_type.VARIANT_BOOL,  # fImport
                                      _type.BSTR],  # strImpExpPath
                                     _type.HRESULT]
    AutoCompleteSaveForm: _Callable[[_Pointer[_struct.VARIANT]],  # Form
                                    _type.HRESULT]
    AutoScan: _Callable[[_type.BSTR,  # strSearch
                         _type.BSTR,  # strFailureUrl
                         _Pointer[_struct.VARIANT]],  # pvarTargetFrame
                        _type.HRESULT]
    AutoCompleteAttach: _Callable[[_Pointer[_struct.VARIANT]],  # Reserved
                                  _type.HRESULT]
    ShowBrowserUI: _Callable[[_type.BSTR,  # bstrName
                              _Pointer[_struct.VARIANT],  # pvarIn
                              _Pointer[_struct.VARIANT]],  # pvarOut
                             _type.HRESULT]


class IShellUIHelper2(IShellUIHelper):
    AddSearchProvider: _Callable[[_type.BSTR],  # URL
                                 _type.HRESULT]
    RunOnceShown: _Callable[[],
                            _type.HRESULT]
    SkipRunOnce: _Callable[[],
                           _type.HRESULT]
    CustomizeSettings: _Callable[[_type.VARIANT_BOOL,  # fSQM
                                  _type.VARIANT_BOOL,  # fPhishing
                                  _type.BSTR],  # bstrLocale
                                 _type.HRESULT]
    SqmEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfEnabled
                          _type.HRESULT]
    PhishingEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfEnabled
                               _type.HRESULT]
    BrandImageUri: _Callable[[_Pointer[_type.BSTR]],  # pbstrUri
                             _type.HRESULT]
    SkipTabsWelcome: _Callable[[],
                               _type.HRESULT]
    DiagnoseConnection: _Callable[[],
                                  _type.HRESULT]
    CustomizeClearType: _Callable[[_type.VARIANT_BOOL],  # fSet
                                  _type.HRESULT]
    IsSearchProviderInstalled: _Callable[[_type.BSTR,  # URL
                                          _Pointer[_type.DWORD]],  # pdwResult
                                         _type.HRESULT]
    IsSearchMigrated: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfMigrated
                                _type.HRESULT]
    DefaultSearchProvider: _Callable[[_Pointer[_type.BSTR]],  # pbstrName
                                     _type.HRESULT]
    RunOnceRequiredSettingsComplete: _Callable[[_type.VARIANT_BOOL],  # fComplete
                                               _type.HRESULT]
    RunOnceHasShown: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfShown
                               _type.HRESULT]
    SearchGuideUrl: _Callable[[_Pointer[_type.BSTR]],  # pbstrUrl
                              _type.HRESULT]


class IShellUIHelper3(IShellUIHelper2):
    AddService: _Callable[[_type.BSTR],  # URL
                          _type.HRESULT]
    IsServiceInstalled: _Callable[[_type.BSTR,  # URL
                                   _type.BSTR,  # Verb
                                   _Pointer[_type.DWORD]],  # pdwResult
                                  _type.HRESULT]
    InPrivateFilteringEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfEnabled
                                         _type.HRESULT]
    AddToFavoritesBar: _Callable[[_type.BSTR,  # URL
                                  _type.BSTR,  # Title
                                  _Pointer[_struct.VARIANT]],  # Type
                                 _type.HRESULT]
    BuildNewTabPage: _Callable[[],
                               _type.HRESULT]
    SetRecentlyClosedVisible: _Callable[[_type.VARIANT_BOOL],  # fVisible
                                        _type.HRESULT]
    SetActivitiesVisible: _Callable[[_type.VARIANT_BOOL],  # fVisible
                                    _type.HRESULT]
    ContentDiscoveryReset: _Callable[[],
                                     _type.HRESULT]
    IsSuggestedSitesEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfEnabled
                                       _type.HRESULT]
    EnableSuggestedSites: _Callable[[_type.VARIANT_BOOL],  # fEnable
                                    _type.HRESULT]
    NavigateToSuggestedSites: _Callable[[_type.BSTR],  # bstrRelativeUrl
                                        _type.HRESULT]
    ShowTabsHelp: _Callable[[],
                            _type.HRESULT]
    ShowInPrivateHelp: _Callable[[],
                                 _type.HRESULT]


class IShellUIHelper4(IShellUIHelper3):
    msIsSiteMode: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfSiteMode
                            _type.HRESULT]
    msSiteModeShowThumbBar: _Callable[[],
                                      _type.HRESULT]
    msSiteModeAddThumbBarButton: _Callable[[_type.BSTR,  # bstrIconURL
                                            _type.BSTR,  # bstrTooltip
                                            _Pointer[_struct.VARIANT]],  # pvarButtonID
                                           _type.HRESULT]
    msSiteModeUpdateThumbBarButton: _Callable[[_struct.VARIANT,  # ButtonID
                                               _type.VARIANT_BOOL,  # fEnabled
                                               _type.VARIANT_BOOL],  # fVisible
                                              _type.HRESULT]
    msSiteModeSetIconOverlay: _Callable[[_type.BSTR,  # IconUrl
                                         _Pointer[_struct.VARIANT]],  # pvarDescription
                                        _type.HRESULT]
    msSiteModeClearIconOverlay: _Callable[[],
                                          _type.HRESULT]
    msAddSiteMode: _Callable[[],
                             _type.HRESULT]
    msSiteModeCreateJumpList: _Callable[[_type.BSTR],  # bstrHeader
                                        _type.HRESULT]
    msSiteModeAddJumpListItem: _Callable[[_type.BSTR,  # bstrName
                                          _type.BSTR,  # bstrActionUri
                                          _type.BSTR,  # bstrIconUri
                                          _Pointer[_struct.VARIANT]],  # pvarWindowType
                                         _type.HRESULT]
    msSiteModeClearJumpList: _Callable[[],
                                       _type.HRESULT]
    msSiteModeShowJumpList: _Callable[[],
                                      _type.HRESULT]
    msSiteModeAddButtonStyle: _Callable[[_struct.VARIANT,  # uiButtonID
                                         _type.BSTR,  # bstrIconUrl
                                         _type.BSTR,  # bstrTooltip
                                         _Pointer[_struct.VARIANT]],  # pvarStyleID
                                        _type.HRESULT]
    msSiteModeShowButtonStyle: _Callable[[_struct.VARIANT,  # uiButtonID
                                          _struct.VARIANT],  # uiStyleID
                                         _type.HRESULT]
    msSiteModeActivate: _Callable[[],
                                  _type.HRESULT]
    msIsSiteModeFirstRun: _Callable[[_type.VARIANT_BOOL,  # fPreserveState
                                     _Pointer[_struct.VARIANT]],  # puiFirstRun
                                    _type.HRESULT]
    msAddTrackingProtectionList: _Callable[[_type.BSTR,  # URL
                                            _type.BSTR],  # bstrFilterName
                                           _type.HRESULT]
    msTrackingProtectionEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfEnabled
                                           _type.HRESULT]
    msActiveXFilteringEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pfEnabled
                                         _type.HRESULT]


class IShellUIHelper5(IShellUIHelper4):
    msProvisionNetworks: _Callable[[_type.BSTR,  # bstrProvisioningXml
                                    _Pointer[_struct.VARIANT]],  # puiResult
                                   _type.HRESULT]
    msReportSafeUrl: _Callable[[],
                               _type.HRESULT]
    msSiteModeRefreshBadge: _Callable[[],
                                      _type.HRESULT]
    msSiteModeClearBadge: _Callable[[],
                                    _type.HRESULT]
    msDiagnoseConnectionUILess: _Callable[[],
                                          _type.HRESULT]
    msLaunchNetworkClientHelp: _Callable[[],
                                         _type.HRESULT]
    msChangeDefaultBrowser: _Callable[[_type.VARIANT_BOOL],  # fChange
                                      _type.HRESULT]


class IShellUIHelper6(IShellUIHelper5):
    msStopPeriodicTileUpdate: _Callable[[],
                                        _type.HRESULT]
    msStartPeriodicTileUpdate: _Callable[[_struct.VARIANT,  # pollingUris
                                          _struct.VARIANT,  # startTime
                                          _struct.VARIANT],  # uiUpdateRecurrence
                                         _type.HRESULT]
    msStartPeriodicTileUpdateBatch: _Callable[[_struct.VARIANT,  # pollingUris
                                               _struct.VARIANT,  # startTime
                                               _struct.VARIANT],  # uiUpdateRecurrence
                                              _type.HRESULT]
    msClearTile: _Callable[[],
                           _type.HRESULT]
    msEnableTileNotificationQueue: _Callable[[_type.VARIANT_BOOL],  # fChange
                                             _type.HRESULT]
    msPinnedSiteState: _Callable[[_Pointer[_struct.VARIANT]],  # pvarSiteState
                                 _type.HRESULT]
    msEnableTileNotificationQueueForSquare150x150: _Callable[[_type.VARIANT_BOOL],  # fChange
                                                             _type.HRESULT]
    msEnableTileNotificationQueueForWide310x150: _Callable[[_type.VARIANT_BOOL],  # fChange
                                                           _type.HRESULT]
    msEnableTileNotificationQueueForSquare310x310: _Callable[[_type.VARIANT_BOOL],  # fChange
                                                             _type.HRESULT]
    msScheduledTileNotification: _Callable[[_type.BSTR,  # bstrNotificationXml
                                            _type.BSTR,  # bstrNotificationId
                                            _type.BSTR,  # bstrNotificationTag
                                            _struct.VARIANT,  # startTime
                                            _struct.VARIANT],  # expirationTime
                                           _type.HRESULT]
    msRemoveScheduledTileNotification: _Callable[[_type.BSTR],  # bstrNotificationId
                                                 _type.HRESULT]
    msStartPeriodicBadgeUpdate: _Callable[[_type.BSTR,  # pollingUri
                                           _struct.VARIANT,  # startTime
                                           _struct.VARIANT],  # uiUpdateRecurrence
                                          _type.HRESULT]
    msStopPeriodicBadgeUpdate: _Callable[[],
                                         _type.HRESULT]
    msLaunchInternetOptions: _Callable[[],
                                       _type.HRESULT]


class IShellUIHelper7(IShellUIHelper6):
    SetExperimentalFlag: _Callable[[_type.BSTR,  # bstrFlagString
                                    _type.VARIANT_BOOL],  # vfFlag
                                   _type.HRESULT]
    GetExperimentalFlag: _Callable[[_type.BSTR,  # bstrFlagString
                                    _Pointer[_type.VARIANT_BOOL]],  # vfFlag
                                   _type.HRESULT]
    SetExperimentalValue: _Callable[[_type.BSTR,  # bstrValueString
                                     _type.DWORD],  # dwValue
                                    _type.HRESULT]
    GetExperimentalValue: _Callable[[_type.BSTR,  # bstrValueString
                                     _Pointer[_type.DWORD]],  # pdwValue
                                    _type.HRESULT]
    ResetAllExperimentalFlagsAndValues: _Callable[[],
                                                  _type.HRESULT]
    GetNeedIEAutoLaunchFlag: _Callable[[_type.BSTR,  # bstrUrl
                                        _Pointer[_type.VARIANT_BOOL]],  # flag
                                       _type.HRESULT]
    SetNeedIEAutoLaunchFlag: _Callable[[_type.BSTR,  # bstrUrl
                                        _type.VARIANT_BOOL],  # flag
                                       _type.HRESULT]
    HasNeedIEAutoLaunchFlag: _Callable[[_type.BSTR,  # bstrUrl
                                        _Pointer[_type.VARIANT_BOOL]],  # exists
                                       _type.HRESULT]
    LaunchIE: _Callable[[_type.BSTR,  # bstrUrl
                         _type.VARIANT_BOOL],  # automated
                        _type.HRESULT]


class IShellUIHelper8(IShellUIHelper7):
    GetCVListData: _Callable[[_Pointer[_type.BSTR]],  # pbstrResult
                             _type.HRESULT]
    GetCVListLocalData: _Callable[[_Pointer[_type.BSTR]],  # pbstrResult
                                  _type.HRESULT]
    GetEMIEListData: _Callable[[_Pointer[_type.BSTR]],  # pbstrResult
                               _type.HRESULT]
    GetEMIEListLocalData: _Callable[[_Pointer[_type.BSTR]],  # pbstrResult
                                    _type.HRESULT]
    OpenFavoritesPane: _Callable[[],
                                 _type.HRESULT]
    OpenFavoritesSettings: _Callable[[],
                                     _type.HRESULT]
    LaunchInHVSI: _Callable[[_type.BSTR],  # bstrUrl
                            _type.HRESULT]


class IShellUIHelper9(IShellUIHelper8):
    GetOSSku: _Callable[[_Pointer[_type.DWORD]],  # pdwResult
                        _type.HRESULT]


class DShellNameSpaceEvents(_oaidl.IDispatch):
    pass


class IShellFavoritesNameSpace(_oaidl.IDispatch):
    MoveSelectionUp: _Callable[[],
                               _type.HRESULT]
    MoveSelectionDown: _Callable[[],
                                 _type.HRESULT]
    ResetSort: _Callable[[],
                         _type.HRESULT]
    NewFolder: _Callable[[],
                         _type.HRESULT]
    Synchronize: _Callable[[],
                           _type.HRESULT]
    Import: _Callable[[],
                      _type.HRESULT]
    Export: _Callable[[],
                      _type.HRESULT]
    InvokeContextMenuCommand: _Callable[[_type.BSTR],  # strCommand
                                        _type.HRESULT]
    MoveSelectionTo: _Callable[[],
                               _type.HRESULT]
    get_SubscriptionsEnabled: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pBool
                                        _type.HRESULT]
    CreateSubscriptionForSelection: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pBool
                                              _type.HRESULT]
    DeleteSubscriptionForSelection: _Callable[[_Pointer[_type.VARIANT_BOOL]],  # pBool
                                              _type.HRESULT]
    SetRoot: _Callable[[_type.BSTR],  # bstrFullPath
                       _type.HRESULT]


class IShellNameSpace(IShellFavoritesNameSpace):
    get_EnumOptions: _Callable[[_Pointer[_type.LONG]],  # pgrfEnumFlags
                               _type.HRESULT]
    put_EnumOptions: _Callable[[_type.LONG],  # lVal
                               _type.HRESULT]
    get_SelectedItem: _Callable[[_Pointer[_oaidl.IDispatch]],  # pItem
                                _type.HRESULT]
    put_SelectedItem: _Callable[[_oaidl.IDispatch],  # pItem
                                _type.HRESULT]
    get_Root: _Callable[[_Pointer[_struct.VARIANT]],  # pvar
                        _type.HRESULT]
    put_Root: _Callable[[_struct.VARIANT],  # var
                        _type.HRESULT]
    get_Depth: _Callable[[_Pointer[_type.c_int]],  # piDepth
                         _type.HRESULT]
    put_Depth: _Callable[[_type.c_int],  # iDepth
                         _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_type.UINT]],  # puMode
                        _type.HRESULT]
    put_Mode: _Callable[[_type.UINT],  # uMode
                        _type.HRESULT]
    get_Flags: _Callable[[_Pointer[_type.DWORD]],  # pdwFlags
                         _type.HRESULT]
    put_Flags: _Callable[[_type.DWORD],  # dwFlags
                         _type.HRESULT]
    put_TVFlags: _Callable[[_type.DWORD],  # dwFlags
                           _type.HRESULT]
    get_TVFlags: _Callable[[_Pointer[_type.DWORD]],  # dwFlags
                           _type.HRESULT]
    get_Columns: _Callable[[_Pointer[_type.BSTR]],  # bstrColumns
                           _type.HRESULT]
    put_Columns: _Callable[[_type.BSTR],  # bstrColumns
                           _type.HRESULT]
    get_CountViewTypes: _Callable[[_Pointer[_type.c_int]],  # piTypes
                                  _type.HRESULT]
    SetViewType: _Callable[[_type.c_int],  # iType
                           _type.HRESULT]
    SelectedItems: _Callable[[_Pointer[_oaidl.IDispatch]],  # ppid
                             _type.HRESULT]
    Expand: _Callable[[_struct.VARIANT,  # var
                       _type.c_int],  # iDepth
                      _type.HRESULT]
    UnselectAll: _Callable[[],
                           _type.HRESULT]


class IScriptErrorList(_oaidl.IDispatch):
    advanceError: _Callable[[],
                            _type.HRESULT]
    retreatError: _Callable[[],
                            _type.HRESULT]
    canAdvanceError: _Callable[[_Pointer[_type.BOOL]],  # pfCanAdvance
                               _type.HRESULT]
    canRetreatError: _Callable[[_Pointer[_type.BOOL]],  # pfCanRetreat
                               _type.HRESULT]
    getErrorLine: _Callable[[_Pointer[_type.LONG]],  # plLine
                            _type.HRESULT]
    getErrorChar: _Callable[[_Pointer[_type.LONG]],  # plChar
                            _type.HRESULT]
    getErrorCode: _Callable[[_Pointer[_type.LONG]],  # plCode
                            _type.HRESULT]
    getErrorMsg: _Callable[[_Pointer[_type.BSTR]],  # pstr
                           _type.HRESULT]
    getErrorUrl: _Callable[[_Pointer[_type.BSTR]],  # pstr
                           _type.HRESULT]
    getAlwaysShowLockState: _Callable[[_Pointer[_type.BOOL]],  # pfAlwaysShowLocked
                                      _type.HRESULT]
    getDetailsPaneOpen: _Callable[[_Pointer[_type.BOOL]],  # pfDetailsPaneOpen
                                  _type.HRESULT]
    setDetailsPaneOpen: _Callable[[_type.BOOL],  # fDetailsPaneOpen
                                  _type.HRESULT]
    getPerErrorDisplay: _Callable[[_Pointer[_type.BOOL]],  # pfPerErrorDisplay
                                  _type.HRESULT]
    setPerErrorDisplay: _Callable[[_type.BOOL],  # fPerErrorDisplay
                                  _type.HRESULT]
