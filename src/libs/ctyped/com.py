from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import types as _types
from typing import Callable as _Callable, Optional as _Optional

from . import com_impl as _com_impl, const as _const, enum as _enum, struct as _struct, type as _type
from ._head import _format_annotations, _get_func_doc, _Globals, _Pointer, _resolve_type

_ASSIGNED = ('__CLSID__', '__RuntimeClass__',
             *(assigned for assigned in _functools.WRAPPER_ASSIGNMENTS if assigned != '__doc__'))


class IUnknown(_type.c_void_p):
    __CLSID__ = ''
    __RuntimeClass__ = ''
    QueryInterface: _Callable[[_Pointer[_struct.IID],
                               _type.c_void_p],
                              _type.HRESULT]
    AddRef: _Callable[[],
                      _type.ULONG]
    Release: _Callable[[],
                       _type.ULONG]


class IShellItem(IUnknown):
    BindToHandler: _Callable[[_Pointer[IBindCtx],
                              _Pointer[_struct.GUID],
                              _Pointer[_struct.IID],
                              _type.c_void_p],
                             _type.HRESULT]
    GetParent: _Callable[[_Pointer[IShellItem]],
                         _type.HRESULT]
    GetDisplayName: _Callable[[_enum.SIGDN,
                               _Pointer[_type.LPWSTR]],
                              _type.HRESULT]
    GetAttributes: _Callable[[_type.SFGAOF,
                              _Pointer[_type.SFGAOF]],
                             _type.HRESULT]
    Compare: _Callable[[_Pointer[IShellItem],
                        _type.SICHINTF,
                        _Pointer[_type.c_int]],
                       _type.HRESULT]


class IShellItemArray(IUnknown):
    BindToHandler: _Callable
    GetPropertyStore: _Callable[[_enum.GETPROPERTYSTOREFLAGS,
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


class IActiveDesktop(IUnknown):
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


class IDesktopWallpaper(IUnknown):
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
    SetPosition: _Callable[[_enum.DESKTOP_WALLPAPER_POSITION],
                           _type.HRESULT]
    GetPosition: _Callable[[_Pointer[_enum.DESKTOP_WALLPAPER_POSITION]],
                           _type.HRESULT]
    SetSlideshow: _Callable[[IShellItemArray],
                            _type.HRESULT]
    GetSlideshow: _Callable
    SetSlideshowOptions: _Callable[[_enum.DESKTOP_SLIDESHOW_OPTIONS,
                                    _type.UINT],
                                   _type.HRESULT]
    GetSlideshowOptions: _Callable[[_Pointer[_enum.DESKTOP_SLIDESHOW_OPTIONS],
                                    _Pointer[_type.UINT]],
                                   _type.HRESULT]
    AdvanceSlideshow: _Callable[[_type.LPCWSTR,
                                 _enum.DESKTOP_SLIDESHOW_DIRECTION],
                                _type.HRESULT]
    GetStatus: _Callable[[_Pointer[_enum.DESKTOP_SLIDESHOW_STATE]],
                         _type.HRESULT]
    Enable: _Callable[[_type.BOOL],
                      _type.HRESULT]


class IModalWindow(IUnknown):
    __CLSID__ = _const.CLSID_FileOpenDialog
    Show: _Callable[[_Optional[_type.HWND]],
                    _type.HRESULT]


class IFileDialog(IModalWindow):
    SetFileTypes: _Callable
    SetFileTypeIndex: _Callable[[_type.UINT],
                                _type.HRESULT]
    GetFileTypeIndex: _Callable[[_type.UINT],
                                _type.HRESULT]
    Advise: _Callable
    Unadvise: _Callable
    SetOptions: _Callable[[_enum.FILEOPENDIALOGOPTIONS],
                          _type.HRESULT]
    GetOptions: _Callable[[_Pointer[_enum.FILEOPENDIALOGOPTIONS]],
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


class IInspectable(IUnknown):
    GetIids: _Callable
    GetRuntimeClassName: _Callable[[_Pointer[_type.HSTRING]], _type.HRESULT]
    GetTrustLevel: _Callable[[_Pointer[_enum.TrustLevel]], _type.HRESULT]


class IUserNotification(IUnknown):
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
    Show: _Callable[[_Optional[_com_impl.IQueryContinue],
                     _type.DWORD],
                    _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR],
                         _type.HRESULT]


class IUserNotification2(IUnknown):
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
    Show: _Callable[[_Optional[_Pointer[_com_impl.IQueryContinue]],
                     _type.DWORD,
                     _Optional[_Pointer[_com_impl.IUserNotificationCallback]]],
                    _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR],
                         _type.HRESULT]


class IPropertyStore(IUnknown):
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


class ISequentialStream(IUnknown):
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


class IPersist(IUnknown):
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
                              _Optional[_Pointer[IMoniker]],
                              _Pointer[_struct.IID],
                              _Pointer[IMoniker]],
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


class IShellLinkA(IUnknown):
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


class IShellLinkW(IUnknown):
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


class IStartMenuPinnedList(IUnknown):
    __CLSID__ = _const.CLSID_StartMenuPin
    RemoveFromList: _Callable[[IShellItem],
                              _type.HRESULT]


class IBindCtx(IUnknown):
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


class IPicture(IUnknown):
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


class IDispatch(IUnknown):
    GetTypeInfoCount: _Callable[[_Pointer[_type.UINT]],
                                _type.HRESULT]
    GetTypeInfo: _Callable
    GetIDsOfNames: _Callable
    Invoke: _Callable


class IPictureDisp(IDispatch):
    pass


class ICreateDevEnum(IUnknown):
    __CLSID__ = _const.CLSID_SystemDeviceEnum
    CreateClassEnumerator: _Callable[[_Pointer[_struct.CLSID],
                                      _Pointer[IEnumMoniker],
                                      _type.DWORD],
                                     _type.DWORD]


class IEnumMoniker(IUnknown):
    Next: _Callable[[_type.ULONG,
                     _Pointer[IMoniker],
                     _type.ULONG],
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable


class IErrorLog(IUnknown):
    AddError: _Callable


class IPropertyBag(IUnknown):
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
    get_Status: _Callable[[_Pointer[_enum.AsyncStatus]],
                          _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],
                             _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class IAsyncAction(IInspectable):
    put_Completed: _Callable[[_com_impl.IAsyncActionCompletedHandler],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[],
                          _type.HRESULT]


class IAsyncActionWithProgress(IInspectable):
    put_Progress: _Callable[[_com_impl.IAsyncActionProgressHandler],
                            _type.HRESULT]
    get_Progress: _Callable
    put_Completed: _Callable[[_com_impl.IAsyncActionWithProgressCompletedHandler],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[],
                          _type.HRESULT]


class IAsyncOperation(IInspectable):
    put_Completed: _Callable[[_com_impl.IAsyncOperationCompletedHandler],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[_Pointer[_type.c_void_p]],
                          _type.HRESULT]


class IAsyncOperationWithProgress(IInspectable):  # TODO parameterize for progress & result type / overload in child (?)
    put_Progress: _Callable[[_com_impl.IAsyncOperationProgressHandler],
                            _type.HRESULT]
    get_Progress: _Callable
    put_Completed: _Callable[[_com_impl.IAsyncOperationWithProgressCompletedHandler],
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
                                _enum.CreationCollisionOption,
                                _Pointer[IAsyncOperation]],
                               _type.HRESULT]
    CreateFolderAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                        _Pointer[IAsyncOperation]],
                                                       _type.HSTRING]
    CreateFolderAsync: _Callable[[_type.HSTRING,
                                  _enum.CreationCollisionOption,
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
    OpenAsync: _Callable[[_enum.FileAccessMode,
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
                             _enum.NameCollisionOption,
                             _Pointer[IAsyncOperation]],
                            _type.HRESULT]
    CopyAndReplaceAsync: _Callable[[IStorageFile,
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
                             _enum.NameCollisionOption,
                             _Pointer[IAsyncAction]],
                            _type.HRESULT]
    MoveAndReplaceAsync: _Callable[[IStorageFile,
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
                          _enum.InputStreamOptions,
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
    CloneStream: _Callable[[_Pointer[IRandomAccessStream]],
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


class ILauncherOptions(IInspectable):
    __RuntimeClass__ = _const.RuntimeClass_Windows_System_LauncherOptions
    get_TreatAsUntrusted: _Callable[[_Pointer[_type.boolean]],
                                    _type.HRESULT]
    put_TreatAsUntrusted: _Callable[[_type.boolean],
                                    _type.HRESULT]
    get_DisplayApplicationPicker: _Callable[[_Pointer[_type.boolean]],
                                            _type.HRESULT]
    put_DisplayApplicationPicker: _Callable[[_type.boolean],
                                            _type.HRESULT]
    get_UI: _Callable
    get_PreferredApplicationPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],
                                                         _type.HRESULT]
    put_PreferredApplicationPackageFamilyName: _Callable[[_type.HSTRING],
                                                         _type.HRESULT]
    get_PreferredApplicationDisplayName: _Callable[[_Pointer[_type.HSTRING]],
                                                   _type.HRESULT]
    put_PreferredApplicationDisplayName: _Callable[[_type.HSTRING],
                                                   _type.HRESULT]
    get_FallbackUri: _Callable[[_Pointer[IUriRuntimeClass]],
                               _type.HRESULT]
    put_FallbackUri: _Callable[[IUriRuntimeClass],
                               _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],
                               _type.HRESULT]
    put_ContentType: _Callable[[_type.HSTRING],
                               _type.HRESULT]


class ILauncherStatics(IInspectable):
    __RuntimeClass__ = _const.RuntimeClass_Windows_System_Launcher
    LaunchFileAsync: _Callable[[IStorageFile,
                                _Pointer[IAsyncOperation]],
                               _type.HRESULT]
    LaunchFileWithOptionsAsync: _Callable[[IStorageFile,
                                           ILauncherOptions,
                                           _Pointer[IAsyncOperation]],
                                          _type.HRESULT]
    LaunchUriAsync: _Callable[[IUriRuntimeClass,
                               _Pointer[IAsyncOperation]],
                              _type.HRESULT]
    LaunchUriWithOptionsAsync: _Callable[[IUriRuntimeClass,
                                          ILauncherOptions,
                                          _Pointer[IAsyncOperation]],
                                         _type.HRESULT]


def _method_type(types: _Callable) -> list:
    types = _resolve_type(types)
    types.insert(1, _type.c_void_p)
    return types


def _init(item: str) -> type[_type.c_void_p]:
    _globals.check_item(item)

    class Com(_type.c_void_p):
        def __getattr__(self, name: str):
            # noinspection PyProtectedMember
            for name_, _ in self._struct._fields_:
                if name == name_:
                    if self.value is None:
                        raise MemoryError(f"com '{type(self).__name__}' has not been initialized yet")
                    funcs = self._struct.from_address(_type.c_void_p.from_address(self.value).value)
                    # noinspection PyProtectedMember
                    for name__, types in self._struct._fields_:
                        method = getattr(funcs, name__)
                        method.__name__ = name__
                        method.__doc__ = '\n'.join(doc for doc in self.__doc__.split('\n')
                                                   if doc.startswith(f'{name__}('))
                        setattr(self, name__, _types.MethodType(method, self))
                    break
            return super().__getattribute__(name)

    dict.__setitem__(_globals, item, _functools.update_wrapper(Com, _globals.vars_[item], _ASSIGNED, ()))
    # noinspection PyTypeChecker,PyTypeHints
    Com._struct: _ctypes.Structure = type(item, (_ctypes.Structure,), {'_fields_': tuple(
        (name, _ctypes.WINFUNCTYPE(*_method_type(types))) for name, types in _globals.get_type_hints(item))})
    annots = {}
    for base in _globals.vars_[item].mro():
        try:
            annots.update(base.__annotations__)
        except AttributeError:
            break
    # noinspection PyProtectedMember
    Com.__doc__ = '\n\n'.join(_get_func_doc(name, types._restype_, types._argtypes_[1:],
                                            _format_annotations(annots[name])) for name, types in Com._struct._fields_)
    return _globals.pop(item)


_globals = _Globals()
