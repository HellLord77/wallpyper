from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _const
from . import _func
from . import _struct
from . import _type
from .__head__ import _Globals
from .__head__ import _Pointer
from .__head__ import _addressof
from .__head__ import _byref
from .__head__ import _get_doc
from .__head__ import _not_internal
from .__head__ import _resolve_type

_ASSIGNED = ('__CLSID__', '__RuntimeClass__',
             *(assigned for assigned in _functools.WRAPPER_ASSIGNMENTS if assigned != '__doc__'))


class _IUnknown(_type.c_void_p):
    __CLSID__ = ''
    __RuntimeClass__ = ''
    QueryInterface: _Callable[[_Pointer[_struct.IID],
                               _type.c_void_p],
                              _type.HRESULT]
    AddRef: _Callable[[],
                      _type.ULONG]
    Release: _Callable[[],
                       _type.ULONG]


class IShellItem(_IUnknown):
    BindToHandler: _Callable[[_Pointer[IBindCtx],
                              _Pointer[_struct.GUID],
                              _Pointer[_struct.IID],
                              _type.c_void_p],
                             _type.HRESULT]
    GetParent: _Callable[[_Pointer[_type.IShellItem]],
                         _type.HRESULT]
    GetDisplayName: _Callable[[_type.SIGDN,
                               _Pointer[_type.LPWSTR]],
                              _type.HRESULT]
    GetAttributes: _Callable[[_type.SFGAOF,
                              _Pointer[_type.SFGAOF]],
                             _type.HRESULT]
    Compare: _Callable[[_Pointer[_type.IShellItem],
                        _type.SICHINTF,
                        _Pointer[_type.c_int]],
                       _type.HRESULT]


class IShellItemArray(_IUnknown):
    BindToHandler: _Callable
    GetPropertyStore: _Callable[[_type.GETPROPERTYSTOREFLAGS,
                                 _Pointer[_struct.IID],
                                 _Pointer[IPropertyStore]],
                                _type.HRESULT]
    GetPropertyDescriptionList: _Callable
    GetAttributes: _Callable
    GetCount: _Callable[[_Pointer[_type.DWORD]],
                        _type.HRESULT]
    GetItemAt: _Callable[[_type.DWORD,
                          _Pointer[_Pointer[IShellItem]]],
                         _type.HRESULT]
    EnumItems: _Callable


class IActiveDesktop(_IUnknown):
    __CLSID__ = _const.CLSID_ActiveDesktop
    ApplyChanges: _Callable[[_type.DWORD],
                            _type.HRESULT]
    GetWallpaper: _Callable[[_type.PWSTR,
                             _type.UINT,
                             _type.DWORD],
                            _type.HRESULT]
    SetWallpaper: _Callable[[_type.PCWSTR,
                             _type.DWORD],
                            _type.HRESULT]
    GetWallpaperOptions: _Callable[[_Pointer[_struct.WALLPAPEROPT],
                                    _type.DWORD],
                                   _type.HRESULT]
    SetWallpaperOptions: _Callable[[_Pointer[_struct.WALLPAPEROPT],
                                    _type.DWORD],
                                   _type.HRESULT]
    GetPattern: _Callable[[_type.PWSTR,
                           _type.UINT,
                           _type.DWORD],
                          _type.HRESULT]
    SetPattern: _Callable[[_type.PCWSTR,
                           _type.DWORD],
                          _type.HRESULT]
    GetDesktopItemOptions: _Callable
    SetDesktopItemOptions: _Callable
    AddDesktopItem: _Callable
    AddDesktopItemWithUI: _Callable
    ModifyDesktopItem: _Callable
    RemoveDesktopItem: _Callable
    GetDesktopItemCount: _Callable[[_Pointer[_type.c_int],
                                    _type.DWORD],
                                   _type.HRESULT]
    GetDesktopItem: _Callable
    GetDesktopItemByID: _Callable
    GenerateDesktopItemHtml: _Callable
    AddUrl: _Callable
    GetDesktopItemBySource: _Callable


class IDesktopWallpaper(_IUnknown):
    __CLSID__ = _const.CLSID_DesktopWallpaper
    SetWallpaper: _Callable[[_Optional[_type.LPCWSTR],
                             _type.LPCWSTR],
                            _type.HRESULT]
    GetWallpaper: _Callable[[_Optional[_type.LPCWSTR],
                             _Pointer[_type.LPWSTR]],
                            _type.HRESULT]
    GetMonitorDevicePathAt: _Callable[[_type.UINT,
                                       _Pointer[_type.LPWSTR]],
                                      _type.HRESULT]
    GetMonitorDevicePathCount: _Callable[[_Pointer[_type.UINT]],
                                         _type.HRESULT]
    GetMonitorRECT: _Callable[[_type.LPCWSTR,
                               _Pointer[_struct.RECT]],
                              _type.HRESULT]
    SetBackgroundColor: _Callable[[_type.COLORREF],
                                  _type.HRESULT]
    GetBackgroundColor: _Callable[[_Pointer[_type.COLORREF]],
                                  _type.HRESULT]
    SetPosition: _Callable[[_type.DESKTOP_WALLPAPER_POSITION],
                           _type.HRESULT]
    GetPosition: _Callable[[_Pointer[_type.DESKTOP_WALLPAPER_POSITION]],
                           _type.HRESULT]
    SetSlideshow: _Callable[[IShellItemArray],
                            _type.HRESULT]
    GetSlideshow: _Callable
    SetSlideshowOptions: _Callable[[_type.DESKTOP_SLIDESHOW_OPTIONS,
                                    _type.UINT],
                                   _type.HRESULT]
    GetSlideshowOptions: _Callable[[_Pointer[_type.DESKTOP_SLIDESHOW_OPTIONS],
                                    _Pointer[_type.UINT]],
                                   _type.HRESULT]
    AdvanceSlideshow: _Callable[[_type.LPCWSTR,
                                 _type.DESKTOP_SLIDESHOW_DIRECTION],
                                _type.HRESULT]
    GetStatus: _Callable[[_Pointer[_type.DESKTOP_SLIDESHOW_STATE]],
                         _type.HRESULT]
    Enable: _Callable[[_type.BOOL],
                      _type.HRESULT]


class IModalWindow(_IUnknown):
    __CLSID__ = _const.CLSID_FileOpenDialog
    Show: _Callable[[_type.HWND],
                    _type.HRESULT]


class IFileDialog(IModalWindow):
    SetFileTypes: _Callable
    SetFileTypeIndex: _Callable[[_type.UINT],
                                _type.HRESULT]
    GetFileTypeIndex: _Callable[[_type.UINT],
                                _type.HRESULT]
    Advise: _Callable
    Unadvise: _Callable
    SetOptions: _Callable[[_type.FILEOPENDIALOGOPTIONS],
                          _type.HRESULT]
    GetOptions: _Callable[[_Pointer[_type.FILEOPENDIALOGOPTIONS]],
                          _type.HRESULT]
    SetDefaultFolder: _Callable[[_Pointer[IShellItem]],
                                _type.HRESULT]
    SetFolder: _Callable[[IShellItem],
                         _type.HRESULT]
    GetFolder: _Callable
    GetCurrentSelection: _Callable
    SetFileName: _Callable[[_type.LPCWSTR],
                           _type.HRESULT]
    GetFileName: _Callable[[_type.LPWSTR],
                           _type.HRESULT]
    SetTitle: _Callable[[_type.LPCWSTR],
                        _type.HRESULT]
    SetOkButtonLabel: _Callable[[_type.LPCWSTR],
                                _type.HRESULT]
    SetFileNameLabel: _Callable[[_type.LPCWSTR],
                                _type.HRESULT]
    GetResult: _Callable[[_Pointer[IShellItem]],
                         _type.HRESULT]
    AddPlace: _Callable
    SetDefaultExtension: _Callable[[_type.LPCWSTR],
                                   _type.HRESULT]
    Close: _Callable[[_type.HRESULT],
                     _type.HRESULT]
    SetClientGuid: _Callable[[_Pointer[_struct.GUID]],
                             _type.HRESULT]
    ClearClientData: _Callable[[],
                               _type.HRESULT]
    SetFilter: _Callable


class IFileOpenDialog(IFileDialog):
    GetResults: _Callable
    GetSelectedItems: _Callable


class IInspectable(_IUnknown):
    GetIids: _Callable
    GetRuntimeClassName: _Callable[[_Pointer[_type.HSTRING]], _type.HRESULT]
    GetTrustLevel: _Callable[[_Pointer[_type.TrustLevel]], _type.HRESULT]


class IUserNotification(_IUnknown):
    __CLSID__ = _const.CLSID_UserNotification
    SetBalloonInfo: _Callable[[_type.LPCWSTR,
                               _type.LPCWSTR,
                               _type.DWORD],
                              _type.HRESULT]
    SetBalloonRetry: _Callable[[_type.DWORD,
                                _type.DWORD,
                                _type.UINT],
                               _type.HRESULT]
    SetIconInfo: _Callable[[_type.HICON,
                            _type.LPCWSTR],
                           _type.HRESULT]
    Show: _Callable[[_Optional[IQueryContinue],
                     _type.DWORD],
                    _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR],
                         _type.HRESULT]


class IUserNotification2(_IUnknown):
    __CLSID__ = _const.CLSID_UserNotification
    SetBalloonInfo: _Callable[[_type.LPCWSTR,
                               _type.LPCWSTR,
                               _type.DWORD],
                              _type.HRESULT]
    SetBalloonRetry: _Callable[[_type.DWORD,
                                _type.DWORD,
                                _type.UINT],
                               _type.HRESULT]
    SetIconInfo: _Callable[[_type.HICON,
                            _type.LPCWSTR],
                           _type.HRESULT]
    Show: _Callable[[_Optional[_Pointer[IQueryContinue]],
                     _type.DWORD,
                     _Optional[_Pointer[IUserNotificationCallback]]],
                    _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR],
                         _type.HRESULT]


class IPropertyStore(_IUnknown):
    GetCount: _Callable[[_Pointer[_type.DWORD]],
                        _type.HRESULT]
    GetAt: _Callable[[_type.DWORD,
                      _Pointer[_struct.PROPERTYKEY]],
                     _type.HRESULT]
    GetValue: _Callable[[_Pointer[_struct.PROPERTYKEY],
                         _Pointer[_struct.PROPVARIANT]],
                        _type.HRESULT]
    SetValue: _Callable[[_Pointer[_struct.PROPERTYKEY],
                         _Pointer[_struct.PROPVARIANT]],
                        _type.HRESULT]
    Commit: _Callable[[],
                      _type.HRESULT]


class ISequentialStream(_IUnknown):
    Read: _Callable
    Write: _Callable


class IStream(ISequentialStream):
    Seek: _Callable
    SetSize: _Callable
    CopyTo: _Callable
    Commit: _Callable
    Revert: _Callable
    LockRegion: _Callable
    UnlockRegion: _Callable
    Stat: _Callable
    Clone: _Callable


class IPersist(_IUnknown):
    GetClassID: _Callable[[_Pointer[_struct.CLSID]],
                          _type.HRESULT]


class IPersistFile(IPersist):
    IsDirty: _Callable[[],
                       _type.HRESULT]
    Load: _Callable[[_type.LPCOLESTR,
                     _type.DWORD],
                    _type.HRESULT]
    Save: _Callable[[_type.LPCOLESTR,
                     _type.BOOL],
                    _type.HRESULT]
    SaveCompleted: _Callable[[_type.LPCOLESTR],
                             _type.HRESULT]
    GetCurFile: _Callable[[_type.LPOLESTR],
                          _type.HRESULT]


class IPersistStream(IPersist):
    IsDirty: _Callable
    Load: _Callable
    Save: _Callable
    GetSizeMax: _Callable


class IMoniker(IPersistStream):
    BindToObject: _Callable
    BindToStorage: _Callable[[_Optional[_Pointer[IBindCtx]],
                              _Optional[_Pointer[_type.IMoniker]],
                              _Pointer[_struct.IID],
                              _Pointer[_type.IMoniker]],
                             _type.HRESULT]
    Reduce: _Callable
    ComposeWith: _Callable
    Enum: _Callable
    IsEqual: _Callable
    Hash: _Callable
    IsRunning: _Callable
    GetTimeOfLastChange: _Callable
    Inverse: _Callable
    CommonPrefixWith: _Callable
    RelativePathTo: _Callable
    GetDisplayName: _Callable
    ParseDisplayName: _Callable
    IsSystemMoniker: _Callable


class IShellLinkA(_IUnknown):
    __CLSID__ = _const.CLSID_ShellLink
    GetPath: _Callable[[_type.LPWSTR,
                        _type.c_int,
                        _Optional[_Pointer[_struct.WIN32_FIND_DATAA]],
                        _type.DWORD],
                       _type.HRESULT]
    GetIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],
                         _type.HRESULT]
    SetIDList: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                         _type.HRESULT]
    GetDescription: _Callable[[_type.LPSTR,
                               _type.c_int],
                              _type.HRESULT]
    SetDescription: _Callable[[_type.LPCSTR],
                              _type.HRESULT]
    GetWorkingDirectory: _Callable[[_type.LPSTR,
                                    _type.c_int],
                                   _type.HRESULT]
    SetWorkingDirectory: _Callable[[_type.LPCSTR],
                                   _type.HRESULT]
    GetArguments: _Callable[[_type.LPSTR,
                             _type.c_int],
                            _type.HRESULT]
    SetArguments: _Callable[[_type.LPCSTR],
                            _type.HRESULT]
    GetHotkey: _Callable[[_Pointer[_type.WORD]],
                         _type.HRESULT]
    SetHotkey: _Callable[[_type.WORD],
                         _type.HRESULT]
    GetShowCmd: _Callable[[_Pointer[_type.c_int]],
                          _type.HRESULT]
    SetShowCmd: _Callable[[_type.c_int],
                          _type.HRESULT]
    GetIconLocation: _Callable[[_type.LPSTR,
                                _type.c_int,
                                _Pointer[_type.c_int]],
                               _type.HRESULT]
    SetIconLocation: _Callable[[_type.LPCSTR,
                                _type.c_int],
                               _type.HRESULT]
    SetRelativePath: _Callable[[_type.LPCSTR,
                                _type.DWORD],
                               _type.HRESULT]
    Resolve: _Callable[[_type.HWND,
                        _type.DWORD],
                       _type.HRESULT]
    SetPath: _Callable[[_type.LPCSTR],
                       _type.HRESULT]


class IShellLinkW(_IUnknown):
    __CLSID__ = _const.CLSID_ShellLink
    GetPath: _Callable[[_type.LPWSTR,
                        _type.c_int,
                        _Optional[_Pointer[_struct.WIN32_FIND_DATAW]],
                        _type.DWORD],
                       _type.HRESULT]
    GetIDList: _Callable[[_Pointer[_Pointer[_struct.ITEMIDLIST]]],
                         _type.HRESULT]
    SetIDList: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                         _type.HRESULT]
    GetDescription: _Callable[[_type.LPWSTR,
                               _type.c_int],
                              _type.HRESULT]
    SetDescription: _Callable[[_type.LPCWSTR],
                              _type.HRESULT]
    GetWorkingDirectory: _Callable[[_type.LPWSTR,
                                    _type.c_int],
                                   _type.HRESULT]
    SetWorkingDirectory: _Callable[[_type.LPCWSTR],
                                   _type.HRESULT]
    GetArguments: _Callable[[_type.LPWSTR,
                             _type.c_int],
                            _type.HRESULT]
    SetArguments: _Callable[[_type.LPCWSTR],
                            _type.HRESULT]
    GetHotkey: _Callable[[_Pointer[_type.WORD]],
                         _type.HRESULT]
    SetHotkey: _Callable[[_type.WORD],
                         _type.HRESULT]
    GetShowCmd: _Callable[[_Pointer[_type.c_int]],
                          _type.HRESULT]
    SetShowCmd: _Callable[[_type.c_int],
                          _type.HRESULT]
    GetIconLocation: _Callable[[_type.LPWSTR,
                                _type.c_int,
                                _Pointer[_type.c_int]],
                               _type.HRESULT]
    SetIconLocation: _Callable[[_type.LPCWSTR,
                                _type.c_int],
                               _type.HRESULT]
    SetRelativePath: _Callable[[_type.LPCWSTR,
                                _type.DWORD],
                               _type.HRESULT]
    Resolve: _Callable[[_type.HWND,
                        _type.DWORD],
                       _type.HRESULT]
    SetPath: _Callable[[_type.LPCWSTR],
                       _type.HRESULT]


class IStartMenuPinnedList(_IUnknown):
    __CLSID__ = _const.CLSID_StartMenuPin
    RemoveFromList: _Callable[[IShellItem],
                              _type.HRESULT]


class IBindCtx(_IUnknown):
    RegisterObjectBound: _Callable
    RevokeObjectBound: _Callable
    ReleaseBoundObjects: _Callable
    SetBindOptions: _Callable
    GetBindOptions: _Callable
    GetRunningObjectTable: _Callable
    RegisterObjectParam: _Callable
    GetObjectParam: _Callable
    EnumObjectParam: _Callable
    RevokeObjectParam: _Callable


class IPicture(_IUnknown):
    get_Handle: _Callable
    get_hPal: _Callable
    get_Type: _Callable
    get_Width: _Callable
    get_Height: _Callable
    Render: _Callable
    set_hPal: _Callable
    get_CurDC: _Callable
    SelectPicture: _Callable
    get_KeepOriginalFormat: _Callable
    put_KeepOriginalFormat: _Callable
    PictureChanged: _Callable
    SaveAsFile: _Callable
    get_Attributes: _Callable


class IDispatch(_IUnknown):
    GetTypeInfoCount: _Callable[[_Pointer[_type.UINT]],
                                _type.HRESULT]
    GetTypeInfo: _Callable
    GetIDsOfNames: _Callable
    Invoke: _Callable


class IPictureDisp(IDispatch):
    pass


class ICreateDevEnum(_IUnknown):
    __CLSID__ = _const.CLSID_SystemDeviceEnum
    CreateClassEnumerator: _Callable[[_Pointer[_struct.CLSID],
                                      _Pointer[IEnumMoniker],
                                      _type.DWORD],
                                     _type.DWORD]


class IEnumMoniker(_IUnknown):
    Next: _Callable[[_type.ULONG,
                     _Pointer[IMoniker],
                     _type.ULONG],
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable


class IErrorLog(_IUnknown):
    AddError: _Callable


class IPropertyBag(_IUnknown):
    Read: _Callable[[_type.LPCOLESTR,
                     _Pointer[_struct.VARIANT],
                     _Optional[_Pointer[IErrorLog]]],
                    _type.HRESULT]
    Write: _Callable[[_type.LPCOLESTR,
                      _Pointer[_struct.VARIANT]],
                     _type.HRESULT]


class IAsyncInfo(IInspectable):
    get_Id: _Callable[[_Pointer[_type.c_uint32]],
                      _type.HRESULT]
    get_Status: _Callable[[_Pointer[_type.AsyncStatus]],
                          _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],
                             _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class IAsyncAction(IInspectable):
    put_Completed: _Callable[[_Pointer[IAsyncActionCompletedHandler]],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[],
                          _type.HRESULT]


class IAsyncOperation(IInspectable):
    put_Completed: _Callable[[_Pointer[IAsyncOperationCompletedHandler]],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[_Pointer[_type.c_void_p]],
                          _type.HRESULT]


class IAsyncOperationWithProgress(IInspectable):  # TODO parameterize for progress & result type / overload in child (?)
    put_Progress: _Callable
    get_Progress: _Callable[[_Pointer[_type.c_void_p]],
                            _type.HRESULT]
    put_Completed: _Callable[[_Pointer[IAsyncOperationWithProgressCompletedHandler]],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[_Pointer[_type.c_void_p]],
                          _type.HRESULT]


class IActivationFactory(IInspectable):
    ActivateInstance: _Callable[[_Pointer[IInspectable]],
                                _type.HRESULT]


class IStorageFolderStatics(IInspectable):
    __RuntimeClass__ = _const.RuntimeClass_Windows_Storage_StorageFolder
    GetFolderFromPathAsync: _Callable[[_type.HSTRING,
                                       _Pointer[IAsyncOperation]],
                                      _type.HRESULT]


class IStorageFolder(IInspectable):
    CreateFileAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                      _Pointer[IAsyncOperation]],
                                                     _type.HSTRING]
    CreateFileAsync: _Callable[[_type.HSTRING,
                                _type.CreationCollisionOption,
                                _Pointer[IAsyncOperation]],
                               _type.HRESULT]
    CreateFolderAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                        _Pointer[IAsyncOperation]],
                                                       _type.HSTRING]
    CreateFolderAsync: _Callable[[_type.HSTRING,
                                  _type.CreationCollisionOption,
                                  _Pointer[IAsyncOperation]],
                                 _type.HRESULT]
    GetFileAsync: _Callable[[_type.HSTRING,
                             _Pointer[IAsyncOperation]],
                            _type.HSTRING]
    GetFolderAsync: _Callable[[_type.HSTRING,
                               _Pointer[IAsyncOperation]],
                              _type.HSTRING]
    GetItemAsync: _Callable[[_type.HSTRING,
                             _Pointer[IAsyncOperation]],
                            _type.HSTRING]
    GetFilesAsyncOverloadDefaultOptionsStartAndCount: _Callable[[_Pointer[IAsyncOperation]],
                                                                _type.HSTRING]
    GetFoldersAsyncOverloadDefaultOptionsStartAndCount: _Callable[[_Pointer[IAsyncOperation]],
                                                                  _type.HSTRING]
    GetItemsAsyncOverloadDefaultStartAndCount: _Callable[[_Pointer[IAsyncOperation]],
                                                         _type.HSTRING]


class IStorageFileStatics(IInspectable):
    __RuntimeClass__ = _const.RuntimeClass_Windows_Storage_StorageFile
    GetFileFromPathAsync: _Callable[[_type.HSTRING,
                                     _Pointer[IAsyncOperation]],
                                    _type.HRESULT]
    GetFileFromApplicationUriAsync: _Callable
    CreateStreamedFileAsync: _Callable
    ReplaceWithStreamedFileAsync: _Callable
    CreateStreamedFileFromUriAsync: _Callable
    ReplaceWithStreamedFileFromUriAsync: _Callable


class IStorageFile(IInspectable):
    get_FileType: _Callable[[_Pointer[_type.HSTRING]],
                            _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],
                               _type.HRESULT]
    OpenAsync: _Callable[[_type.FileAccessMode,
                          _Pointer[IAsyncOperation]],
                         _type.HRESULT]
    OpenTransactedWriteAsync: _Callable[[_Pointer[IAsyncOperation]],
                                        _type.HRESULT]
    CopyOverloadDefaultNameAndOptions: _Callable[[IStorageFolder,
                                                  _Pointer[IAsyncOperation]],
                                                 _type.HRESULT]
    CopyOverloadDefaultOptions: _Callable[[IStorageFolder,
                                           _type.HSTRING,
                                           _Pointer[IAsyncOperation]],
                                          _type.HRESULT]
    CopyOverload: _Callable[[IStorageFolder,
                             _type.HSTRING,
                             _type.NameCollisionOption,
                             _Pointer[IAsyncOperation]],
                            _type.HRESULT]
    CopyAndReplaceAsync: _Callable[[_type.IStorageFile,
                                    _Pointer[IAsyncAction]],
                                   _type.HRESULT]
    MoveOverloadDefaultNameAndOptions: _Callable[[IStorageFolder,
                                                  _Pointer[IAsyncAction]],
                                                 _type.HRESULT]
    MoveOverloadDefaultOptions: _Callable[[IStorageFolder,
                                           _type.HSTRING,
                                           _Pointer[IAsyncAction]],
                                          _type.HRESULT]
    MoveOverload: _Callable[[IStorageFolder,
                             _type.HSTRING,
                             _type.NameCollisionOption,
                             _Pointer[IAsyncAction]],
                            _type.HRESULT]
    MoveAndReplaceAsync: _Callable[[_type.IStorageFile,
                                    _Pointer[IAsyncAction]],
                                   _type.HRESULT]


class IUriRuntimeClass(IInspectable):
    get_AbsoluteUri: _Callable[[_Pointer[_type.HSTRING]],
                               _type.HRESULT]
    get_DisplayUri: _Callable[[_Pointer[_type.HSTRING]],
                              _type.HRESULT]
    get_Domain: _Callable[[_Pointer[_type.HSTRING]],
                          _type.HRESULT]
    get_Extension: _Callable[[_Pointer[_type.HSTRING]],
                             _type.HRESULT]
    get_Fragment: _Callable[[_Pointer[_type.HSTRING]],
                            _type.HRESULT]
    get_Host: _Callable[[_Pointer[_type.HSTRING]],
                        _type.HRESULT]
    get_Password: _Callable[[_Pointer[_type.HSTRING]],
                            _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],
                        _type.HRESULT]
    get_Query: _Callable[[_Pointer[_type.HSTRING]],
                         _type.HRESULT]
    get_QueryParsed: _Callable
    get_RawUri: _Callable[[_Pointer[_type.HSTRING]],
                          _type.HRESULT]
    get_SchemeName: _Callable[[_Pointer[_type.HSTRING]],
                              _type.HRESULT]
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],
                            _type.HRESULT]
    get_Port: _Callable[[_Pointer[_type.INT32]],
                        _type.HRESULT]
    get_Suspicious: _Callable[[_Pointer[_type.boolean]],
                              _type.HRESULT]
    Equals: _Callable
    CombineUri: _Callable


class IBuffer(IInspectable):
    get_Capacity: _Callable[[_Pointer[_type.UINT32]],
                            _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],
                          _type.HRESULT]
    put_Length: _Callable[[_type.UINT32],
                          _type.HRESULT]


class IInputStream(IInspectable):
    ReadAsync: _Callable[[IBuffer,
                          _type.UINT32,
                          _type.InputStreamOptions,
                          _Pointer[IAsyncOperationWithProgress]],
                         _type.HRESULT]


class IOutputStream(IInspectable):
    WriteAsync: _Callable
    FlushAsync: _Callable


class IRandomAccessStreamStatics(IInspectable):
    __RuntimeClass__ = _const.RuntimeClass_Windows_Storage_Streams_RandomAccessStream
    CopyAsync: _Callable[[IInputStream,
                          IOutputStream,
                          _Pointer[IAsyncOperationWithProgress]],
                         _type.HRESULT]
    CopySizeAsync: _Callable[[IInputStream,
                              IOutputStream,
                              _type.UINT64,
                              _Pointer[IAsyncOperationWithProgress]],
                             _type.HRESULT]
    CopyAndCloseAsync: _Callable[[IInputStream,
                                  IOutputStream,
                                  _Pointer[IAsyncOperationWithProgress]],
                                 _type.HRESULT]


class IRandomAccessStream(IInspectable):
    get_Size: _Callable[[_Pointer[_type.UINT64]],
                        _type.HRESULT]
    put_Size: _Callable[[_type.UINT64],
                        _type.HRESULT]
    GetInputStreamAt: _Callable[[_type.UINT64,
                                 _Pointer[IInputStream]],
                                _type.HRESULT]
    GetOutputStreamAt: _Callable[[_type.UINT64,
                                  _Pointer[IOutputStream]],
                                 _type.HRESULT]
    get_Position: _Callable[[_Pointer[_type.UINT64]],
                            _type.HRESULT]
    Seek: _Callable[[_type.UINT64],
                    _type.HRESULT]
    CloneStream: _Callable[[_Pointer[_type.IRandomAccessStream]],
                           _type.HRESULT]
    get_CanRead: _Callable[[_Pointer[_type.boolean]],
                           _type.HRESULT]
    get_CanWrite: _Callable[[_Pointer[_type.boolean]],
                            _type.HRESULT]


class ILockScreenStatics(IInspectable):
    __RuntimeClass__ = _const.RuntimeClass_Windows_System_UserProfile_LockScreen
    get_OriginalImageFile: _Callable[[_Pointer[IUriRuntimeClass]],
                                     _type.HRESULT]
    GetImageStream: _Callable[[_Pointer[IRandomAccessStream]],
                              _type.HRESULT]
    SetImageFileAsync: _Callable[[IStorageFile,
                                  _Pointer[IAsyncAction]],
                                 _type.HRESULT]
    SetImageStreamAsync: _Callable[[IRandomAccessStream,
                                    _Pointer[IAsyncAction]],
                                   _type.HRESULT]


def _method_type(types: _Callable) -> list:
    types = _resolve_type(types)
    types.insert(1, _type.c_void_p)
    return types


def _init(name: str) -> type[_type.c_void_p]:
    _globals.check_item(name)

    class Wrapper(_type.c_void_p):
        _struct: _ctypes.Structure = type(name, (_ctypes.Structure,), {'_fields_': tuple((name_, _ctypes.WINFUNCTYPE(
            *_method_type(types))) for name_, types in _globals.get_type_hints(name))})
        # noinspection PyProtectedMember
        __doc__ = '\n'.join(_get_doc(name_, types._restype_, types._argtypes_) for name_, types in _struct._fields_)

        def __getattr__(self, name_: str):
            if _not_internal(name_) and name_ in dir(self._struct):
                if self.value is None:
                    raise MemoryError(f"com '{type(self).__name__}' has not been initialized yet")
                funcs = self._struct.from_address(_type.c_void_p.from_address(self.value).value)
                # noinspection PyProtectedMember
                for name__, types in self._struct._fields_:
                    method = getattr(funcs, name__)
                    method.__name__ = name__
                    # noinspection PyProtectedMember
                    method.__doc__ = _get_doc(name__, types._restype_, types._argtypes_)
                    setattr(self, name__, _types.MethodType(method, self))
            return super().__getattribute__(name_)

    return _functools.update_wrapper(Wrapper, _globals.vars_[name], _ASSIGNED, ())


_globals = _Globals()


class IUnknown(_type.c_void_p):
    __IID__ = {_const.IID_IUnknown}
    _funcs = None
    _vtbl = None

    def __new__(cls, *_, **__):
        base: type[IUnknown]
        if cls._vtbl is None:
            funcs = {}
            bases = cls.mro()
            for base in bases[bases.index(IUnknown)::-1]:
                cls.__IID__.update(base.__IID__)
                for key, value in vars(base).items():
                    if _not_internal(key) and (key in funcs or __name__ == base.__module__):
                        funcs[key] = value
            fields = []
            cls._funcs = []
            for name, func in funcs.items():
                if static := hasattr(func, '__func__'):
                    func = func.__func__
                types = list(_typing.get_type_hints(func).values())
                # noinspection PyTypeHints
                type_ = _ctypes.WINFUNCTYPE(*_resolve_type(_Callable[types, types.pop()]))
                fields.append((name, type_))
                cls._funcs.append((None, type_(func)) if static else (type_, func))
            cls._vtbl = type(cls.__name__, (_ctypes.Structure,), {'_fields_': fields})
        return super().__new__(cls)

    def __init__(self):
        self._vtbl = self._vtbl(*(func if type_ is None else type_(_types.MethodType(func, self))
                                  for type_, func in self._funcs))
        super().__init__(_addressof(self._vtbl))

    # noinspection PyPep8Naming
    def QueryInterface(self, This: _Pointer[IUnknown], riid: _Pointer[_struct.IID],
                       ppvObject: _Pointer[_type.LPVOID]) -> _type.HRESULT:
        if not ppvObject:
            return _const.E_INVALIDARG
        ppvObject.contents.value = None
        iid = _type.LPOLESTR()
        _func.ole32.StringFromIID(riid, _byref(iid))
        if iid.value in self.__IID__:
            ppvObject.contents.value = _addressof(self)
            This.contents.AddRef(This)
            return _const.NOERROR
        return _const.E_NOINTERFACE

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def AddRef(This: _Pointer[IUnknown]) -> _type.ULONG:
        return 1

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Release(This: _Pointer[IUnknown]) -> _type.ULONG:
        return 0


class IQueryContinue(IUnknown):
    __IID__ = {_const.IID_IQueryContinue}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def QueryContinue() -> _type.HRESULT:
        return _const.NOERROR


class IUserNotificationCallback(IUnknown):
    __IID__ = {_const.IID_IUserNotificationCallback}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def OnBalloonUserClick(This: _Pointer[IUserNotificationCallback],
                           pt: _Pointer[_struct.POINT]) -> _type.HRESULT:
        return _const.NOERROR

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def OnLeftClick(This: _Pointer[IUserNotificationCallback],
                    pt: _Pointer[_struct.POINT]) -> _type.HRESULT:
        return _const.NOERROR

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def OnContextMenu(This: _Pointer[IUserNotificationCallback],
                      pt: _Pointer[_struct.POINT]) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncActionCompletedHandler(IUnknown):
    __IID__ = {_const.IID_IAsyncActionCompletedHandler}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncActionCompletedHandler, asyncInfo: IAsyncAction,
               asyncStatus: _type.AsyncStatus) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncOperationCompletedHandler(IUnknown):
    __IID__ = {_const.IID_IAsyncOperationCompletedHandler_IRandomAccessStream,
               _const.IID_IAsyncOperationCompletedHandler_IStorageFile,
               _const.IID_IAsyncOperationCompletedHandler_IStorageFolder}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncOperationCompletedHandler, asyncInfo: IAsyncOperation,
               asyncStatus: _type.AsyncStatus) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncOperationWithProgressCompletedHandler(IUnknown):
    __IID__ = {_const.IID_IAsyncOperationWithProgressCompletedHandler_UINT64_UINT64}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncOperationWithProgressCompletedHandler, asyncInfo: IAsyncOperationWithProgress,
               asyncStatus: _type.AsyncStatus) -> _type.HRESULT:
        return _const.NOERROR
