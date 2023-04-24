from __future__ import annotations

from typing import Callable as _Callable

from . import ShObjIdl_core as _ShObjIdl_core
from . import Unknwnbase as _Unknwnbase
from . import msxml as _msxml
from . import objidl as _objidl
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IQueryCodePage(_Unknwnbase.IUnknown):
    GetCodePage: _Callable[[_Pointer[_type.UINT]],  # puiCodePage
                           _type.HRESULT]
    SetCodePage: _Callable[[_type.UINT],  # uiCodePage
                           _type.HRESULT]


class IFolderViewOptions(_Unknwnbase.IUnknown):
    SetFolderViewOptions: _Callable[[_enum.FOLDERVIEWOPTIONS,  # fvoMask
                                     _enum.FOLDERVIEWOPTIONS],  # fvoFlags
                                    _type.HRESULT]
    GetFolderViewOptions: _Callable[[_Pointer[_enum.FOLDERVIEWOPTIONS]],  # pfvoFlags
                                    _type.HRESULT]


class IShellView3(_ShObjIdl_core.IShellView2):
    CreateViewWindow3: _Callable[[_ShObjIdl_core.IShellBrowser,  # psbOwner
                                  _ShObjIdl_core.IShellView,  # psvPrev
                                  _type.SV3CVW3_FLAGS,  # dwViewFlags
                                  _enum.FOLDERFLAGS,  # dwMask
                                  _enum.FOLDERFLAGS,  # dwFlags
                                  _enum.FOLDERVIEWMODE,  # fvMode
                                  _Pointer[_struct.SHELLVIEWID],  # pvid
                                  _Pointer[_struct.RECT],  # prcView
                                  _Pointer[_type.HWND]],  # phwndView
                                 _type.HRESULT]


class ISearchBoxInfo(_Unknwnbase.IUnknown):
    GetCondition: _Callable[[_Pointer[_struct.IID],  # riid
                             _type.c_void_p],  # ppv
                            _type.HRESULT]
    GetText: _Callable[[_Pointer[_type.LPWSTR]],  # ppsz
                       _type.HRESULT]


class IVisualProperties(_Unknwnbase.IUnknown):
    SetWatermark: _Callable[[_type.HBITMAP,  # hbmp
                             _enum.VPWATERMARKFLAGS],  # vpwf
                            _type.HRESULT]
    SetColor: _Callable[[_enum.VPCOLORFLAGS,  # vpcf
                         _type.COLORREF],  # cr
                        _type.HRESULT]
    GetColor: _Callable[[_enum.VPCOLORFLAGS,  # vpcf
                         _Pointer[_type.COLORREF]],  # pcr
                        _type.HRESULT]
    SetItemHeight: _Callable[[_type.c_int],  # cyItemInPixels
                             _type.HRESULT]
    GetItemHeight: _Callable[[_Pointer[_type.c_int]],  # cyItemInPixels
                             _type.HRESULT]
    SetFont: _Callable[[_Pointer[_struct.LOGFONTW],  # plf
                        _type.BOOL],  # bRedraw
                       _type.HRESULT]
    GetFont: _Callable[[_Pointer[_struct.LOGFONTW]],  # plf
                       _type.HRESULT]
    SetTheme: _Callable[[_type.LPCWSTR,  # pszSubAppName
                         _type.LPCWSTR],  # pszSubIdList
                        _type.HRESULT]


class ICommDlgBrowser3(_ShObjIdl_core.ICommDlgBrowser2):
    OnColumnClicked: _Callable[[_ShObjIdl_core.IShellView,  # ppshv
                                _type.c_int],  # iColumn
                               _type.HRESULT]
    GetCurrentFilter: _Callable[[_type.LPWSTR,  # pszFileSpec
                                 _type.c_int],  # cchFileSpec
                                _type.HRESULT]
    OnPreViewCreated: _Callable[[_ShObjIdl_core.IShellView],  # ppshv
                                _type.HRESULT]


class IUserAccountChangeCallback(_Unknwnbase.IUnknown):
    OnPictureChange: _Callable[[_type.LPCWSTR],  # pszUserName
                               _type.HRESULT]


class IStreamAsync(_objidlbase.IStream):
    ReadAsync: _Callable[[_type.c_void_p,  # pv
                          _type.DWORD,  # cb
                          _Pointer[_type.DWORD],  # pcbRead
                          _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                         _type.HRESULT]
    WriteAsync: _Callable[[_type.c_void_p,  # lpBuffer
                           _type.DWORD,  # cb
                           _Pointer[_type.DWORD],  # pcbWritten
                           _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                          _type.HRESULT]
    OverlappedResult: _Callable[[_Pointer[_struct.OVERLAPPED],  # lpOverlapped
                                 _Pointer[_type.DWORD],  # lpNumberOfBytesTransferred
                                 _type.BOOL],  # bWait
                                _type.HRESULT]
    CancelIo: _Callable[[],
                        _type.HRESULT]


class IStreamUnbufferedInfo(_Unknwnbase.IUnknown):
    GetSectorSize: _Callable[[_Pointer[_type.ULONG]],  # pcbSectorSize
                             _type.HRESULT]


class IDragSourceHelper2(_ShObjIdl_core.IDragSourceHelper):
    SetFlags: _Callable[[_type.DWORD],  # dwFlags
                        _type.HRESULT]


class IHWEventHandler(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.LPCWSTR],  # pszParams
                          _type.HRESULT]
    HandleEvent: _Callable[[_type.LPCWSTR,  # pszDeviceID
                            _type.LPCWSTR,  # pszAltDeviceID
                            _type.LPCWSTR],  # pszEventType
                           _type.HRESULT]
    HandleEventWithContent: _Callable[[_type.LPCWSTR,  # pszDeviceID
                                       _type.LPCWSTR,  # pszAltDeviceID
                                       _type.LPCWSTR,  # pszEventType
                                       _type.LPCWSTR,  # pszContentTypeHandler
                                       _objidl.IDataObject],  # pdataobject
                                      _type.HRESULT]


class IHWEventHandler2(IHWEventHandler):
    HandleEventWithHWND: _Callable[[_type.LPCWSTR,  # pszDeviceID
                                    _type.LPCWSTR,  # pszAltDeviceID
                                    _type.LPCWSTR,  # pszEventType
                                    _type.HWND],  # hwndOwner
                                   _type.HRESULT]


class IQueryCancelAutoPlay(_Unknwnbase.IUnknown):
    AllowAutoPlay: _Callable[[_type.LPCWSTR,  # pszPath
                              _type.DWORD,  # dwContentType
                              _type.LPCWSTR,  # pszLabel
                              _type.DWORD],  # dwSerialNumber
                             _type.HRESULT]


class IDynamicHWHandler(_Unknwnbase.IUnknown):
    GetDynamicInfo: _Callable[[_type.LPCWSTR,  # pszDeviceID
                               _type.DWORD,  # dwContentType
                               _Pointer[_type.LPWSTR]],  # ppszAction
                              _type.HRESULT]


class IUserNotificationCallback(_Unknwnbase.IUnknown):
    OnBalloonUserClick: _Callable[[_Pointer[_struct.POINT]],  # pt
                                  _type.HRESULT]
    OnLeftClick: _Callable[[_Pointer[_struct.POINT]],  # pt
                           _type.HRESULT]
    OnContextMenu: _Callable[[_Pointer[_struct.POINT]],  # pt
                             _type.HRESULT]


class IUserNotification2(_Unknwnbase.IUnknown):
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
    Show: _Callable[[_ShObjIdl_core.IQueryContinue,  # pqc
                     _type.DWORD,  # dwContinuePollInterval
                     IUserNotificationCallback],  # pSink
                    _type.HRESULT]
    PlaySoundW: _Callable[[_type.LPCWSTR],  # pszSoundName
                          _type.HRESULT]


class IDeskBand2(_ShObjIdl_core.IDeskBand):
    CanRenderComposited: _Callable[[_Pointer[_type.BOOL]],  # pfCanRenderComposited
                                   _type.HRESULT]
    SetCompositionState: _Callable[[_type.BOOL],  # fCompositionEnabled
                                   _type.HRESULT]
    GetCompositionState: _Callable[[_Pointer[_type.BOOL]],  # pfCompositionEnabled
                                   _type.HRESULT]


class IStartMenuPinnedList(_Unknwnbase.IUnknown):
    RemoveFromList: _Callable[[_ShObjIdl_core.IShellItem],  # pitem
                              _type.HRESULT]


class ICDBurn(_Unknwnbase.IUnknown):
    GetRecorderDriveLetter: _Callable[[_type.LPWSTR,  # pszDrive
                                       _type.UINT],  # cch
                                      _type.HRESULT]
    Burn: _Callable[[_type.HWND],  # hwnd
                    _type.HRESULT]
    HasRecordableDrive: _Callable[[_Pointer[_type.BOOL]],  # pfHasRecorder
                                  _type.HRESULT]


class IWizardSite(_Unknwnbase.IUnknown):
    GetPreviousPage: _Callable
    GetNextPage: _Callable
    GetCancelledPage: _Callable


class IWizardExtension(_Unknwnbase.IUnknown):
    AddPages: _Callable
    GetFirstPage: _Callable
    GetLastPage: _Callable


class IWebWizardExtension(IWizardExtension):
    SetInitialURL: _Callable[[_type.LPCWSTR],  # pszURL
                             _type.HRESULT]
    SetErrorURL: _Callable[[_type.LPCWSTR],  # pszErrorURL
                           _type.HRESULT]


class IPublishingWizard(IWizardExtension):
    Initialize: _Callable[[_objidl.IDataObject,  # pdo
                           _type.DWORD,  # dwOptions
                           _type.LPCWSTR],  # pszServiceScope
                          _type.HRESULT]
    GetTransferManifest: _Callable[[_Pointer[_type.HRESULT],  # phrFromTransfer
                                    _Pointer[_msxml.IXMLDOMDocument]],  # pdocManifest
                                   _type.HRESULT]


class IFolderViewHost(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_type.HWND,  # hwndParent
                           _objidl.IDataObject,  # pdo
                           _Pointer[_struct.RECT]],  # prc
                          _type.HRESULT]


class IAccessibleObject(_Unknwnbase.IUnknown):
    SetAccessibleName: _Callable[[_type.LPCWSTR],  # pszName
                                 _type.HRESULT]


class IResultsFolder(_Unknwnbase.IUnknown):
    AddItem: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                       _type.HRESULT]
    AddIDList: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                          _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidlAdded
                         _type.HRESULT]
    RemoveItem: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                          _type.HRESULT]
    RemoveIDList: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidl
                            _type.HRESULT]
    RemoveAll: _Callable[[],
                         _type.HRESULT]


class IAutoCompleteDropDown(_Unknwnbase.IUnknown):
    GetDropDownStatus: _Callable[[_Pointer[_type.DWORD],  # pdwFlags
                                  _Pointer[_type.LPWSTR]],  # ppwszString
                                 _type.HRESULT]
    ResetEnumerator: _Callable[[],
                               _type.HRESULT]


class ICDBurnExt(_Unknwnbase.IUnknown):
    GetSupportedActionTypes: _Callable[[_Pointer[_type.CDBE_ACTIONS]],  # pdwActions
                                       _type.HRESULT]


class IEnumReadyCallback(_Unknwnbase.IUnknown):
    EnumReady: _Callable[[],
                         _type.HRESULT]


class IEnumerableView(_Unknwnbase.IUnknown):
    SetEnumReadyCallback: _Callable[[IEnumReadyCallback],  # percb
                                    _type.HRESULT]
    CreateEnumIDListFromContents: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidlFolder
                                             _type.DWORD,  # dwEnumFlags
                                             _Pointer[_ShObjIdl_core.IEnumIDList]],  # ppEnumIDList
                                            _type.HRESULT]


class IInsertItem(_Unknwnbase.IUnknown):
    InsertItem: _Callable[[_Pointer[_struct.ITEMIDLIST]],  # pidl
                          _type.HRESULT]


class IFolderBandPriv(_Unknwnbase.IUnknown):
    SetCascade: _Callable[[_type.BOOL],  # fCascade
                          _type.HRESULT]
    SetAccelerators: _Callable[[_type.BOOL],  # fAccelerators
                               _type.HRESULT]
    SetNoIcons: _Callable[[_type.BOOL],  # fNoIcons
                          _type.HRESULT]
    SetNoText: _Callable[[_type.BOOL],  # fNoText
                         _type.HRESULT]


class IImageRecompress(_Unknwnbase.IUnknown):
    RecompressImage: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                _type.c_int,  # cx
                                _type.c_int,  # cy
                                _type.c_int,  # iQuality
                                _objidl.IStorage,  # pstg
                                _Pointer[_objidlbase.IStream]],  # ppstrmOut
                               _type.HRESULT]


class IFileDialogControlEvents(_Unknwnbase.IUnknown):
    OnItemSelected: _Callable[[_ShObjIdl_core.IFileDialogCustomize,  # pfdc
                               _type.DWORD,  # dwIDCtl
                               _type.DWORD],  # dwIDItem
                              _type.HRESULT]
    OnButtonClicked: _Callable[[_ShObjIdl_core.IFileDialogCustomize,  # pfdc
                                _type.DWORD],  # dwIDCtl
                               _type.HRESULT]
    OnCheckButtonToggled: _Callable[[_ShObjIdl_core.IFileDialogCustomize,  # pfdc
                                     _type.DWORD,  # dwIDCtl
                                     _type.BOOL],  # bChecked
                                    _type.HRESULT]
    OnControlActivating: _Callable[[_ShObjIdl_core.IFileDialogCustomize,  # pfdc
                                    _type.DWORD],  # dwIDCtl
                                   _type.HRESULT]


class IFileDialog2(_ShObjIdl_core.IFileDialog):
    SetCancelButtonLabel: _Callable[[_type.LPCWSTR],  # pszLabel
                                    _type.HRESULT]
    SetNavigationRoot: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                                 _type.HRESULT]


class IApplicationAssociationRegistrationUI(_Unknwnbase.IUnknown):
    LaunchAdvancedAssociationUI: _Callable[[_type.LPCWSTR],  # pszAppRegistryName
                                           _type.HRESULT]


class IShellRunDll(_Unknwnbase.IUnknown):
    Run: _Callable[[_type.LPCWSTR],  # pszArgs
                   _type.HRESULT]


class IPreviousVersionsInfo(_Unknwnbase.IUnknown):
    AreSnapshotsAvailable: _Callable[[_type.LPCWSTR,  # pszPath
                                      _type.BOOL,  # fOkToBeSlow
                                      _Pointer[_type.BOOL]],  # pfAvailable
                                     _type.HRESULT]


class IUseToBrowseItem(_ShObjIdl_core.IRelatedItem):
    pass


class INameSpaceTreeControl2(_ShObjIdl_core.INameSpaceTreeControl):
    SetControlStyle: _Callable[[_type.NSTCSTYLE,  # nstcsMask
                                _type.NSTCSTYLE],  # nstcsStyle
                               _type.HRESULT]
    GetControlStyle: _Callable[[_type.NSTCSTYLE,  # nstcsMask
                                _Pointer[_type.NSTCSTYLE]],  # pnstcsStyle
                               _type.HRESULT]
    SetControlStyle2: _Callable[[_enum.NSTCSTYLE2,  # nstcsMask
                                 _enum.NSTCSTYLE2],  # nstcsStyle
                                _type.HRESULT]
    GetControlStyle2: _Callable[[_enum.NSTCSTYLE2,  # nstcsMask
                                 _Pointer[_enum.NSTCSTYLE2]],  # pnstcsStyle
                                _type.HRESULT]


class INameSpaceTreeControlEvents(_Unknwnbase.IUnknown):
    OnItemClick: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                            _type.NSTCEHITTEST,  # nstceHitTest
                            _type.NSTCECLICKTYPE],  # nstceClickType
                           _type.HRESULT]
    OnPropertyItemCommit: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                                    _type.HRESULT]
    OnItemStateChanging: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                    _type.NSTCITEMSTATE,  # nstcisMask
                                    _type.NSTCITEMSTATE],  # nstcisState
                                   _type.HRESULT]
    OnItemStateChanged: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                   _type.NSTCITEMSTATE,  # nstcisMask
                                   _type.NSTCITEMSTATE],  # nstcisState
                                  _type.HRESULT]
    OnSelectionChanged: _Callable[[_ShObjIdl_core.IShellItemArray],  # psiaSelection
                                  _type.HRESULT]
    OnKeyboardInput: _Callable[[_type.UINT,  # uMsg
                                _type.WPARAM,  # wParam
                                _type.LPARAM],  # lParam
                               _type.HRESULT]
    OnBeforeExpand: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                              _type.HRESULT]
    OnAfterExpand: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                             _type.HRESULT]
    OnBeginLabelEdit: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                                _type.HRESULT]
    OnEndLabelEdit: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                              _type.HRESULT]
    OnGetToolTip: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                             _type.LPWSTR,  # pszTip
                             _type.c_int],  # cchTip
                            _type.HRESULT]
    OnBeforeItemDelete: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                                  _type.HRESULT]
    OnItemAdded: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                            _type.BOOL],  # fIsRoot
                           _type.HRESULT]
    OnItemDeleted: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                              _type.BOOL],  # fIsRoot
                             _type.HRESULT]
    OnBeforeContextMenu: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                    _Pointer[_struct.IID],  # riid
                                    _type.c_void_p],  # ppv
                                   _type.HRESULT]
    OnAfterContextMenu: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                   _ShObjIdl_core.IContextMenu,  # pcmIn
                                   _Pointer[_struct.IID],  # riid
                                   _type.c_void_p],  # ppv
                                  _type.HRESULT]
    OnBeforeStateImageChange: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                                        _type.HRESULT]
    OnGetDefaultIconIndex: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                      _Pointer[_type.c_int],  # piDefaultIcon
                                      _Pointer[_type.c_int]],  # piOpenIcon
                                     _type.HRESULT]


class INameSpaceTreeControlDropHandler(_Unknwnbase.IUnknown):
    OnDragEnter: _Callable[[_ShObjIdl_core.IShellItem,  # psiOver
                            _ShObjIdl_core.IShellItemArray,  # psiaData
                            _type.BOOL,  # fOutsideSource
                            _type.DWORD,  # grfKeyState
                            _Pointer[_type.DWORD]],  # pdwEffect
                           _type.HRESULT]
    OnDragOver: _Callable[[_ShObjIdl_core.IShellItem,  # psiOver
                           _ShObjIdl_core.IShellItemArray,  # psiaData
                           _type.DWORD,  # grfKeyState
                           _Pointer[_type.DWORD]],  # pdwEffect
                          _type.HRESULT]
    OnDragPosition: _Callable[[_ShObjIdl_core.IShellItem,  # psiOver
                               _ShObjIdl_core.IShellItemArray,  # psiaData
                               _type.c_int,  # iNewPosition
                               _type.c_int],  # iOldPosition
                              _type.HRESULT]
    OnDrop: _Callable[[_ShObjIdl_core.IShellItem,  # psiOver
                       _ShObjIdl_core.IShellItemArray,  # psiaData
                       _type.c_int,  # iPosition
                       _type.DWORD,  # grfKeyState
                       _Pointer[_type.DWORD]],  # pdwEffect
                      _type.HRESULT]
    OnDropPosition: _Callable[[_ShObjIdl_core.IShellItem,  # psiOver
                               _ShObjIdl_core.IShellItemArray,  # psiaData
                               _type.c_int,  # iNewPosition
                               _type.c_int],  # iOldPosition
                              _type.HRESULT]
    OnDragLeave: _Callable[[_ShObjIdl_core.IShellItem],  # psiOver
                           _type.HRESULT]


class INameSpaceTreeAccessible(_Unknwnbase.IUnknown):
    OnGetDefaultAccessibilityAction: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                                _Pointer[_type.BSTR]],  # pbstrDefaultAction
                                               _type.HRESULT]
    OnDoDefaultAccessibilityAction: _Callable[[_ShObjIdl_core.IShellItem],  # psi
                                              _type.HRESULT]
    OnGetAccessibilityRole: _Callable[[_ShObjIdl_core.IShellItem,  # psi
                                       _Pointer[_struct.VARIANT]],  # pvarRole
                                      _type.HRESULT]


class INameSpaceTreeControlCustomDraw(_Unknwnbase.IUnknown):
    PrePaint: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.RECT],  # prc
                         _Pointer[_type.LRESULT]],  # plres
                        _type.HRESULT]
    PostPaint: _Callable[[_type.HDC,  # hdc
                          _Pointer[_struct.RECT]],  # prc
                         _type.HRESULT]
    ItemPrePaint: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.RECT],  # prc
                             _Pointer[_struct.NSTCCUSTOMDRAW],  # pnstccdItem
                             _Pointer[_type.COLORREF],  # pclrText
                             _Pointer[_type.COLORREF],  # pclrTextBk
                             _Pointer[_type.LRESULT]],  # plres
                            _type.HRESULT]
    ItemPostPaint: _Callable[[_type.HDC,  # hdc
                              _Pointer[_struct.RECT],  # prc
                              _Pointer[_struct.NSTCCUSTOMDRAW]],  # pnstccdItem
                             _type.HRESULT]


class ITrayDeskBand(_Unknwnbase.IUnknown):
    ShowDeskBand: _Callable[[_Pointer[_struct.IID]],  # clsid
                            _type.HRESULT]
    HideDeskBand: _Callable[[_Pointer[_struct.IID]],  # clsid
                            _type.HRESULT]
    IsDeskBandShown: _Callable[[_Pointer[_struct.IID]],  # clsid
                               _type.HRESULT]
    DeskBandRegistrationChanged: _Callable[[],
                                           _type.HRESULT]


class IBandHost(_Unknwnbase.IUnknown):
    CreateBand: _Callable[[_Pointer[_struct.IID],  # rclsidBand
                           _type.BOOL,  # fAvailable
                           _type.BOOL,  # fVisible
                           _Pointer[_struct.IID],  # riid
                           _type.c_void_p],  # ppv
                          _type.HRESULT]
    SetBandAvailability: _Callable[[_Pointer[_struct.IID],  # rclsidBand
                                    _type.BOOL],  # fAvailable
                                   _type.HRESULT]
    DestroyBand: _Callable[[_Pointer[_struct.IID]],  # rclsidBand
                           _type.HRESULT]


class IComputerInfoChangeNotify(_Unknwnbase.IUnknown):
    ComputerInfoChanged: _Callable[[],
                                   _type.HRESULT]


class IDesktopGadget(_Unknwnbase.IUnknown):
    RunGadget: _Callable[[_type.LPCWSTR],  # gadgetPath
                         _type.HRESULT]


class IAccessibilityDockingServiceCallback(_Unknwnbase.IUnknown):
    Undocked: _Callable[[_enum.UNDOCK_REASON],  # undockReason
                        _type.HRESULT]


class IAccessibilityDockingService(_Unknwnbase.IUnknown):
    GetAvailableSize: _Callable[[_type.HMONITOR,  # hMonitor
                                 _Pointer[_type.UINT],  # pcxFixed
                                 _Pointer[_type.UINT]],  # pcyMax
                                _type.HRESULT]
    DockWindow: _Callable[[_type.HWND,  # hwnd
                           _type.HMONITOR,  # hMonitor
                           _type.UINT,  # cyRequested
                           IAccessibilityDockingServiceCallback],  # pCallback
                          _type.HRESULT]
    UndockWindow: _Callable[[_type.HWND],  # hwnd
                            _type.HRESULT]


class IStorageProviderBanners(_Unknwnbase.IUnknown):
    SetBanner: _Callable[[_type.LPCWSTR,  # providerIdentity
                          _type.LPCWSTR,  # subscriptionId
                          _type.LPCWSTR],  # contentId
                         _type.HRESULT]
    ClearBanner: _Callable[[_type.LPCWSTR,  # providerIdentity
                            _type.LPCWSTR],  # subscriptionId
                           _type.HRESULT]
    ClearAllBanners: _Callable[[_type.LPCWSTR],  # providerIdentity
                               _type.HRESULT]
    GetBanner: _Callable[[_type.LPCWSTR,  # providerIdentity
                          _type.LPCWSTR,  # subscriptionId
                          _Pointer[_type.LPWSTR]],  # contentId
                         _type.HRESULT]


class IStorageProviderCopyHook(_Unknwnbase.IUnknown):
    CopyCallback: _Callable[[_type.HWND,  # hwnd
                             _type.UINT,  # operation
                             _type.UINT,  # flags
                             _type.LPCWSTR,  # srcFile
                             _type.DWORD,  # srcAttribs
                             _type.LPCWSTR,  # destFile
                             _type.DWORD,  # destAttribs
                             _Pointer[_type.UINT]],  # result
                            _type.HRESULT]
