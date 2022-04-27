from __future__ import annotations as _

import ctypes as _ctypes
import types as _types
import typing as _typing
from typing import Callable as _Callable, Optional as _Optional

from . import const as _const, enum as _enum, interface_impl as _interface_impl, struct as _struct, type as _type
from ._utils import _format_annotations, _get_func_doc, _Pointer, _resolve_type


def _method_type(types: _Callable) -> list:
    types = _resolve_type(types)
    types.insert(1, _type.c_void_p)
    return types


class _Interface(_type.c_void_p):
    _struct = _ctypes.Structure

    def __new__(cls):
        if cls._struct.__name__ != cls.__name__:
            cls._struct = type(cls.__name__, (_ctypes.Structure,), {'_fields_': tuple((name, _ctypes.WINFUNCTYPE(
                *_method_type(types))) for name, types in _typing.get_type_hints(cls).items())})
            annots = {}
            for base in cls.mro():
                try:
                    annots.update(base.__annotations__)
                except AttributeError:
                    break
            # noinspection PyProtectedMember,PyUnresolvedReferences
            cls.__doc__ = '\n\n'.join(_get_func_doc(name, types._restype_, types._argtypes_[1:], _format_annotations(
                annots[name])) for name, types in cls._struct._fields_)
        return super().__new__(cls)

    def __getattr__(self, name: str):
        # noinspection PyProtectedMember,PyUnresolvedReferences
        for name_, _ in self._struct._fields_:
            if name == name_:
                if self.value is None:
                    raise MemoryError(f"interface '{type(self).__name__}' has not been initialized yet")
                # noinspection PyUnresolvedReferences
                funcs = self._struct.from_address(_type.c_void_p.from_address(self.value).value)
                # noinspection PyProtectedMember,PyUnresolvedReferences
                for name__, types in self._struct._fields_:
                    method = getattr(funcs, name__)
                    method.__name__ = name__
                    method.__doc__ = '\n'.join(
                        doc for doc in self.__doc__.split('\n') if doc.startswith(f'{name__}('))
                    setattr(self, name__, _types.MethodType(method, self))
                break
        return super().__getattribute__(name)


class IUnknown(_Interface):
    _CLSID_ = ''
    QueryInterface: _Callable[[_Pointer[_struct.IID],
                               _type.c_void_p],
                              _type.HRESULT]
    AddRef: _Callable[[],
                      _type.ULONG]
    Release: _Callable[[],
                       _type.ULONG]


class IInspectable(IUnknown):
    _RuntimeClass_ = ''
    GetIids: _Callable
    GetRuntimeClassName: _Callable[[_Pointer[_type.HSTRING]],
                                   _type.HRESULT]
    GetTrustLevel: _Callable[[_Pointer[_enum.TrustLevel]],
                             _type.HRESULT]


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
    _CLSID_ = _const.CLSID_ActiveDesktop
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
    GetDesktopItemOptions: _Callable[[_Pointer[_struct.COMPONENTSOPT],
                                      _type.DWORD],
                                     _type.HRESULT]
    SetDesktopItemOptions: _Callable[[_Pointer[_struct.COMPONENTSOPT],
                                      _type.DWORD],
                                     _type.HRESULT]
    AddDesktopItem: _Callable[[_Pointer[_struct.COMPONENT],
                               _type.DWORD],
                              _type.HRESULT]
    AddDesktopItemWithUI: _Callable[[_Optional[_type.HWND],
                                     _Pointer[_struct.COMPONENT],
                                     _type.DWORD],
                                    _type.HRESULT]
    ModifyDesktopItem: _Callable[[_Pointer[_struct.COMPONENT],
                                  _type.DWORD],
                                 _type.HRESULT]
    RemoveDesktopItem: _Callable[[_Pointer[_struct.COMPONENT],
                                  _type.DWORD],
                                 _type.HRESULT]
    GetDesktopItemCount: _Callable[[_Pointer[_type.c_int],
                                    _type.DWORD],
                                   _type.HRESULT]
    GetDesktopItem: _Callable[[_type.c_int,
                               _Pointer[_struct.COMPONENT],
                               _type.DWORD],
                              _type.HRESULT]
    GetDesktopItemByID: _Callable[[_type.ULONG_PTR,
                                   _Pointer[_struct.COMPONENT],
                                   _type.DWORD],
                                  _type.HRESULT]
    GenerateDesktopItemHtml: _Callable[[_type.PCWSTR,
                                        _Pointer[_struct.COMPONENT],
                                        _type.DWORD],
                                       _type.HRESULT]
    AddUrl: _Callable[[_Optional[_type.HWND],
                       _type.PCWSTR,
                       _Pointer[_struct.COMPONENT],
                       _type.DWORD],
                      _type.HRESULT]
    GetDesktopItemBySource: _Callable[[_type.PCWSTR,
                                       _Pointer[_struct.COMPONENT],
                                       _type.DWORD],
                                      _type.HRESULT]


class IDesktopWallpaper(IUnknown):
    _CLSID_ = _const.CLSID_DesktopWallpaper
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
    _CLSID_ = _const.CLSID_FileOpenDialog
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


class IUserNotification(IUnknown):
    _CLSID_ = _const.CLSID_UserNotification
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
    Show: _Callable[[_Optional[_interface_impl.IQueryContinue],
                     _type.DWORD],
                    _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR],
                         _type.HRESULT]


class IUserNotification2(IUnknown):
    _CLSID_ = _const.CLSID_UserNotification
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
    Show: _Callable[[_Optional[_Pointer[_interface_impl.IQueryContinue]],
                     _type.DWORD,
                     _Optional[_Pointer[_interface_impl.IUserNotificationCallback]]],
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
    _CLSID_ = _const.CLSID_ShellLink
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
    _CLSID_ = _const.CLSID_ShellLink
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
    _CLSID_ = _const.CLSID_StartMenuPin
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
    _CLSID_ = _const.CLSID_SystemDeviceEnum
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


class IHostControl(IUnknown):
    GetHostManager: _Callable
    SetAppDomainManager: _Callable[[_type.DWORD,
                                    IUnknown],
                                   _type.HRESULT]


class ICLRControl(IUnknown):
    GetCLRManager: _Callable
    SetAppDomainManagerType: _Callable[[_type.LPCWSTR,
                                        _type.LPCWSTR],
                                       _type.HRESULT]


class ICLRRuntimeHost(IUnknown):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    SetHostControl: _Callable[[IHostControl],
                              _type.HRESULT]
    GetCLRControl: _Callable[[_Pointer[ICLRControl]],
                             _type.HRESULT]
    UnloadAppDomain: _Callable[[_type.DWORD,
                                _type.BOOL],
                               _type.HRESULT]
    ExecuteInAppDomain: _Callable
    GetCurrentAppDomainId: _Callable[[_Pointer[_type.DWORD]],
                                     _type.HRESULT]
    ExecuteApplication: _Callable[[_type.LPCWSTR,
                                   _type.DWORD,
                                   _Pointer[_type.LPCWSTR],
                                   _type.DWORD,
                                   _Pointer[_type.LPCWSTR],
                                   _Pointer[_type.c_int]],
                                  _type.HRESULT]
    ExecuteInDefaultAppDomain: _Callable[[_type.LPCWSTR,
                                          _type.LPCWSTR,
                                          _type.LPCWSTR,
                                          _type.LPCWSTR,
                                          _Pointer[_type.DWORD]],
                                         _type.HRESULT]


class IDesktopWindowXamlSourceNative(IUnknown):
    AttachToWindow: _Callable[[_type.HWND],
                              _type.HRESULT]
    get_WindowHandle: _Callable[[_Pointer[_type.HWND]],
                                _type.HRESULT]


class IDesktopWindowXamlSourceNative2(IDesktopWindowXamlSourceNative):
    PreTranslateMessage: _Callable[[_Pointer[_struct.MSG],
                                    _Pointer[_type.BOOL]],
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
    put_Completed: _Callable[[_interface_impl.IAsyncActionCompletedHandler],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[],
                          _type.HRESULT]


class IAsyncActionWithProgress(IInspectable):
    put_Progress: _Callable[[_interface_impl.IAsyncActionProgressHandler],
                            _type.HRESULT]
    get_Progress: _Callable
    put_Completed: _Callable[[_interface_impl.IAsyncActionWithProgressCompletedHandler],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[],
                          _type.HRESULT]


class IAsyncOperation(IInspectable):
    put_Completed: _Callable[[_interface_impl.IAsyncOperationCompletedHandler],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[_Pointer[_type.c_void_p]],
                          _type.HRESULT]


class IAsyncOperationWithProgress(IInspectable):  # TODO parameterize for progress & result type / overload in child
    put_Progress: _Callable[[_interface_impl.IAsyncOperationProgressHandler],
                            _type.HRESULT]
    get_Progress: _Callable
    put_Completed: _Callable[[_interface_impl.IAsyncOperationWithProgressCompletedHandler],
                             _type.HRESULT]
    get_Completed: _Callable
    GetResults: _Callable[[_Pointer[_type.c_void_p]],
                          _type.HRESULT]


class IActivationFactory(IInspectable):
    ActivateInstance: _Callable[[_Pointer[IInspectable]],
                                _type.HRESULT]


class Windows:
    class Data:
        class Xml:
            class Dom:
                class IXmlDocument(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_Data_Xml_Dom_XmlDocument
                    get_Doctype: _Callable
                    get_Implementation: _Callable
                    get_DocumentElement: _Callable
                    CreateElement: _Callable
                    CreateDocumentFragment: _Callable
                    CreateTextNode: _Callable
                    CreateComment: _Callable
                    CreateProcessingInstruction: _Callable
                    CreateAttribute: _Callable
                    CreateEntityReference: _Callable
                    GetElementsByTagName: _Callable
                    CreateCDataSection: _Callable
                    get_DocumentUri: _Callable
                    CreateAttributeNS: _Callable
                    CreateElementNS: _Callable
                    GetElementById: _Callable
                    ImportNode: _Callable

                class IXmlDocumentIO(IInspectable):
                    LoadXml: _Callable[[_type.HSTRING],
                                       _type.HRESULT]
                    LoadXmlWithSettings: _Callable
                    SaveToFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                                _Pointer[IAsyncAction]],
                                               _type.HRESULT]

                class IXmlDocumentIO2(IInspectable):
                    LoadXmlFromBuffer: _Callable[[Windows.Storage.Streams.IBuffer],
                                                 _type.HRESULT]
                    LoadXmlFromBufferWithSettings: _Callable

                class IXmlDocumentStatics(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_Data_Xml_Dom_XmlDocument
                    LoadFromUriAsync: _Callable[[Windows.Foundation.IUriRuntimeClass,
                                                 _Pointer[IAsyncOperation]],
                                                _type.HRESULT]
                    LoadFromUriWithSettingsAsync: _Callable
                    LoadFromFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                                  _Pointer[IAsyncOperation]],
                                                 _type.HRESULT]
                    LoadFromFileWithSettingsAsync: _Callable

                class IXmlNodeSerializer(IInspectable):
                    GetXml: _Callable[[_Pointer[_type.HSTRING]],
                                      _type.HRESULT]
                    get_InnerText: _Callable[[_Pointer[_type.HSTRING]],
                                             _type.HRESULT]
                    put_InnerText: _Callable[[_type.HSTRING],
                                             _type.HRESULT]

    class Foundation:
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

        class Collections:
            # noinspection PyPep8Naming
            class IVector_IUIElement(IInspectable):
                GetAt: _Callable[[_type.c_uint,
                                  _Pointer[Windows.UI.Xaml.IUIElement]],
                                 _type.HRESULT]
                get_Size: _Callable[[_Pointer[_type.c_uint]],
                                    _type.HRESULT]
                GetView: _Callable
                IndexOf: _Callable[[Windows.UI.Xaml.IUIElement,
                                    _Pointer[_type.c_uint],
                                    _Pointer[_type.boolean]],
                                   _type.HRESULT]
                SetAt: _Callable[[_type.c_uint,
                                  Windows.UI.Xaml.IUIElement],
                                 _type.HRESULT]
                InsertAt: _Callable[[_type.c_uint,
                                     Windows.UI.Xaml.IUIElement],
                                    _type.HRESULT]
                RemoveAt: _Callable[[_type.c_uint],
                                    _type.HRESULT]
                Append: _Callable[[Windows.UI.Xaml.IUIElement],
                                  _type.HRESULT]
                RemoveAtEnd: _Callable[[],
                                       _type.HRESULT]
                Clear: _Callable[[],
                                 _type.HRESULT]
                GetMany: _Callable[[_type.c_uint,
                                    _type.c_uint,
                                    _Pointer[Windows.UI.Xaml.IUIElement],
                                    _Pointer[_type.c_uint]],
                                   _type.HRESULT]
                ReplaceAll: _Callable[[_type.c_uint,
                                       _Pointer[Windows.UI.Xaml.IUIElement]],
                                      _type.HRESULT]

    class Storage:
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
            CopyOverloadDefaultNameAndOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                          _Pointer[IAsyncOperation]],
                                                         _type.HRESULT]
            CopyOverloadDefaultOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                   _type.HSTRING,
                                                   _Pointer[IAsyncOperation]],
                                                  _type.HRESULT]
            CopyOverload: _Callable[[Windows.Storage.IStorageFolder,
                                     _type.HSTRING,
                                     _enum.NameCollisionOption,
                                     _Pointer[IAsyncOperation]],
                                    _type.HRESULT]
            CopyAndReplaceAsync: _Callable[[Windows.Storage.IStorageFile,
                                            _Pointer[IAsyncAction]],
                                           _type.HRESULT]
            MoveOverloadDefaultNameAndOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                          _Pointer[IAsyncAction]],
                                                         _type.HRESULT]
            MoveOverloadDefaultOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                   _type.HSTRING,
                                                   _Pointer[IAsyncAction]],
                                                  _type.HRESULT]
            MoveOverload: _Callable[[Windows.Storage.IStorageFolder,
                                     _type.HSTRING,
                                     _enum.NameCollisionOption,
                                     _Pointer[IAsyncAction]],
                                    _type.HRESULT]
            MoveAndReplaceAsync: _Callable[[Windows.Storage.IStorageFile,
                                            _Pointer[IAsyncAction]],
                                           _type.HRESULT]

        class IStorageFileStatics(IInspectable):
            _RuntimeClass_ = _const.RuntimeClass_Windows_Storage_StorageFile
            GetFileFromPathAsync: _Callable[[_type.HSTRING,
                                             _Pointer[IAsyncOperation]],
                                            _type.HRESULT]
            GetFileFromApplicationUriAsync: _Callable
            CreateStreamedFileAsync: _Callable
            ReplaceWithStreamedFileAsync: _Callable
            CreateStreamedFileFromUriAsync: _Callable
            ReplaceWithStreamedFileFromUriAsync: _Callable

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

        class IStorageFolderStatics(IInspectable):
            _RuntimeClass_ = _const.RuntimeClass_Windows_Storage_StorageFolder
            GetFolderFromPathAsync: _Callable[[_type.HSTRING,
                                               _Pointer[IAsyncOperation]],
                                              _type.HRESULT]

        class Streams:
            class IBuffer(IInspectable):
                get_Capacity: _Callable[[_Pointer[_type.UINT32]],
                                        _type.HRESULT]
                get_Length: _Callable[[_Pointer[_type.UINT32]],
                                      _type.HRESULT]
                put_Length: _Callable[[_type.UINT32],
                                      _type.HRESULT]

            class IInputStream(IInspectable):
                ReadAsync: _Callable[[Windows.Storage.Streams.IBuffer,
                                      _type.UINT32,
                                      _enum.InputStreamOptions,
                                      _Pointer[IAsyncOperationWithProgress]],
                                     _type.HRESULT]

            class IOutputStream(IInspectable):
                WriteAsync: _Callable
                FlushAsync: _Callable

            class IRandomAccessStream(IInspectable):
                get_Size: _Callable[[_Pointer[_type.UINT64]],
                                    _type.HRESULT]
                put_Size: _Callable[[_type.UINT64],
                                    _type.HRESULT]
                GetInputStreamAt: _Callable[[_type.UINT64,
                                             _Pointer[Windows.Storage.Streams.IInputStream]],
                                            _type.HRESULT]
                GetOutputStreamAt: _Callable[[_type.UINT64,
                                              _Pointer[Windows.Storage.Streams.IOutputStream]],
                                             _type.HRESULT]
                get_Position: _Callable[[_Pointer[_type.UINT64]],
                                        _type.HRESULT]
                Seek: _Callable[[_type.UINT64],
                                _type.HRESULT]
                CloneStream: _Callable[[_Pointer[Windows.Storage.Streams.IRandomAccessStream]],
                                       _type.HRESULT]
                get_CanRead: _Callable[[_Pointer[_type.boolean]],
                                       _type.HRESULT]
                get_CanWrite: _Callable[[_Pointer[_type.boolean]],
                                        _type.HRESULT]

            class IRandomAccessStreamStatics(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_Storage_Streams_RandomAccessStream
                CopyAsync: _Callable[[Windows.Storage.Streams.IInputStream,
                                      Windows.Storage.Streams.IOutputStream,
                                      _Pointer[IAsyncOperationWithProgress]],
                                     _type.HRESULT]
                CopySizeAsync: _Callable[[Windows.Storage.Streams.IInputStream,
                                          Windows.Storage.Streams.IOutputStream,
                                          _type.UINT64,
                                          _Pointer[IAsyncOperationWithProgress]],
                                         _type.HRESULT]
                CopyAndCloseAsync: _Callable[[Windows.Storage.Streams.IInputStream,
                                              Windows.Storage.Streams.IOutputStream,
                                              _Pointer[IAsyncOperationWithProgress]],
                                             _type.HRESULT]

    class System:
        class ILauncherOptions(IInspectable):
            _RuntimeClass_ = _const.RuntimeClass_Windows_System_LauncherOptions
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
            get_FallbackUri: _Callable[[_Pointer[Windows.Foundation.IUriRuntimeClass]],
                                       _type.HRESULT]
            put_FallbackUri: _Callable[[Windows.Foundation.IUriRuntimeClass],
                                       _type.HRESULT]
            get_ContentType: _Callable[[_Pointer[_type.HSTRING]],
                                       _type.HRESULT]
            put_ContentType: _Callable[[_type.HSTRING],
                                       _type.HRESULT]

        class ILauncherStatics(IInspectable):
            _RuntimeClass_ = _const.RuntimeClass_Windows_System_Launcher
            LaunchFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                        _Pointer[IAsyncOperation]],
                                       _type.HRESULT]
            LaunchFileWithOptionsAsync: _Callable[[Windows.Storage.IStorageFile,
                                                   Windows.System.ILauncherOptions,
                                                   _Pointer[IAsyncOperation]],
                                                  _type.HRESULT]
            LaunchUriAsync: _Callable[[Windows.Foundation.IUriRuntimeClass,
                                       _Pointer[IAsyncOperation]],
                                      _type.HRESULT]
            LaunchUriWithOptionsAsync: _Callable[[Windows.Foundation.IUriRuntimeClass,
                                                  Windows.System.ILauncherOptions,
                                                  _Pointer[IAsyncOperation]],
                                                 _type.HRESULT]

        class UserProfile:
            class ILockScreenStatics(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_System_UserProfile_LockScreen
                get_OriginalImageFile: _Callable[[_Pointer[Windows.Foundation.IUriRuntimeClass]],
                                                 _type.HRESULT]
                GetImageStream: _Callable[[_Pointer[Windows.Storage.Streams.IRandomAccessStream]],
                                          _type.HRESULT]
                SetImageFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                              _Pointer[IAsyncAction]],
                                             _type.HRESULT]
                SetImageStreamAsync: _Callable[[Windows.Storage.Streams.IRandomAccessStream,
                                                _Pointer[IAsyncAction]],
                                               _type.HRESULT]

    class UI:
        class IColorsStatics(IInspectable):
            _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Colors
            get_AliceBlue: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_AntiqueWhite: _Callable[[_Pointer[_struct.Color]],
                                        _type.HRESULT]
            get_Aqua: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_Aquamarine: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_Azure: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_Beige: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_Bisque: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_Black: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_BlanchedAlmond: _Callable[[_Pointer[_struct.Color]],
                                          _type.HRESULT]
            get_Blue: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_BlueViolet: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_Brown: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_BurlyWood: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_CadetBlue: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Chartreuse: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_Chocolate: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Coral: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_CornflowerBlue: _Callable[[_Pointer[_struct.Color]],
                                          _type.HRESULT]
            get_Cornsilk: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_Crimson: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_Cyan: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_DarkBlue: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_DarkCyan: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_DarkGoldenrod: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_DarkGray: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_DarkGreen: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_DarkKhaki: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_DarkMagenta: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_DarkOliveGreen: _Callable[[_Pointer[_struct.Color]],
                                          _type.HRESULT]
            get_DarkOrange: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_DarkOrchid: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_DarkRed: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_DarkSalmon: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_DarkSeaGreen: _Callable[[_Pointer[_struct.Color]],
                                        _type.HRESULT]
            get_DarkSlateBlue: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_DarkSlateGray: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_DarkTurquoise: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_DarkViolet: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_DeepPink: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_DeepSkyBlue: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_DimGray: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_DodgerBlue: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_Firebrick: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_FloralWhite: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_ForestGreen: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_Fuchsia: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_Gainsboro: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_GhostWhite: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_Gold: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_Goldenrod: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Gray: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_Green: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_GreenYellow: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_Honeydew: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_HotPink: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_IndianRed: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Indigo: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_Ivory: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_Khaki: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_Lavender: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_LavenderBlush: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_LawnGreen: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_LemonChiffon: _Callable[[_Pointer[_struct.Color]],
                                        _type.HRESULT]
            get_LightBlue: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_LightCoral: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_LightCyan: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_LightGoldenrodYellow: _Callable[[_Pointer[_struct.Color]],
                                                _type.HRESULT]
            get_LightGreen: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_LightGray: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_LightPink: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_LightSalmon: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_LightSeaGreen: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_LightSkyBlue: _Callable[[_Pointer[_struct.Color]],
                                        _type.HRESULT]
            get_LightSlateGray: _Callable[[_Pointer[_struct.Color]],
                                          _type.HRESULT]
            get_LightSteelBlue: _Callable[[_Pointer[_struct.Color]],
                                          _type.HRESULT]
            get_LightYellow: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_Lime: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_LimeGreen: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Linen: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_Magenta: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_Maroon: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_MediumAquamarine: _Callable[[_Pointer[_struct.Color]],
                                            _type.HRESULT]
            get_MediumBlue: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_MediumOrchid: _Callable[[_Pointer[_struct.Color]],
                                        _type.HRESULT]
            get_MediumPurple: _Callable[[_Pointer[_struct.Color]],
                                        _type.HRESULT]
            get_MediumSeaGreen: _Callable[[_Pointer[_struct.Color]],
                                          _type.HRESULT]
            get_MediumSlateBlue: _Callable[[_Pointer[_struct.Color]],
                                           _type.HRESULT]
            get_MediumSpringGreen: _Callable[[_Pointer[_struct.Color]],
                                             _type.HRESULT]
            get_MediumTurquoise: _Callable[[_Pointer[_struct.Color]],
                                           _type.HRESULT]
            get_MediumVioletRed: _Callable[[_Pointer[_struct.Color]],
                                           _type.HRESULT]
            get_MidnightBlue: _Callable[[_Pointer[_struct.Color]],
                                        _type.HRESULT]
            get_MintCream: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_MistyRose: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Moccasin: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_NavajoWhite: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_Navy: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_OldLace: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_Olive: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_OliveDrab: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Orange: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_OrangeRed: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Orchid: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_PaleGoldenrod: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_PaleGreen: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_PaleTurquoise: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_PaleVioletRed: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
            get_PapayaWhip: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_PeachPuff: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Peru: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_Pink: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_Plum: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_PowderBlue: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_Purple: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_Red: _Callable[[_Pointer[_struct.Color]],
                               _type.HRESULT]
            get_RosyBrown: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_RoyalBlue: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_SaddleBrown: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_Salmon: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_SandyBrown: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_SeaGreen: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_SeaShell: _Callable[[_Pointer[_struct.Color]],
                                    _type.HRESULT]
            get_Sienna: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_Silver: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_SkyBlue: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_SlateBlue: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_SlateGray: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Snow: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_SpringGreen: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_SteelBlue: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Tan: _Callable[[_Pointer[_struct.Color]],
                               _type.HRESULT]
            get_Teal: _Callable[[_Pointer[_struct.Color]],
                                _type.HRESULT]
            get_Thistle: _Callable[[_Pointer[_struct.Color]],
                                   _type.HRESULT]
            get_Tomato: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_Transparent: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]
            get_Turquoise: _Callable[[_Pointer[_struct.Color]],
                                     _type.HRESULT]
            get_Violet: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_Wheat: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_White: _Callable[[_Pointer[_struct.Color]],
                                 _type.HRESULT]
            get_WhiteSmoke: _Callable[[_Pointer[_struct.Color]],
                                      _type.HRESULT]
            get_Yellow: _Callable[[_Pointer[_struct.Color]],
                                  _type.HRESULT]
            get_YellowGreen: _Callable[[_Pointer[_struct.Color]],
                                       _type.HRESULT]

        class Notifications:
            class IToastActivatedEventArgs(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastActivatedEventArgs
                get_Argument: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]

            class IToastActivatedEventArgs2(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastActivatedEventArgs
                get_UserInput: _Callable

            class IToastDismissedEventArgs(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastDismissedEventArgs
                get_Reason: _Callable[[_Pointer[_enum.ToastDismissalReason]],
                                      _type.HRESULT]

            class IToastFailedEventArgs(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastFailedEventArgs
                get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],
                                         _type.HRESULT]

            class IToastNotification(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastNotification
                get_Content: _Callable[[_Pointer[Windows.Data.Xml.Dom.IXmlDocument]],
                                       _type.HRESULT]
                put_ExpirationTime: _Callable
                get_ExpirationTime: _Callable
                add_Dismissed: _Callable[[_interface_impl.ITypedEventHandler,
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_Dismissed: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_Activated: _Callable[[_interface_impl.ITypedEventHandler,
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_Activated: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_Failed: _Callable[[_interface_impl.ITypedEventHandler,
                                       _Pointer[_struct.EventRegistrationToken]],
                                      _type.HRESULT]
                remove_Failed: _Callable[[_struct.EventRegistrationToken],
                                         _type.HRESULT]

            class IToastNotificationFactory(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastNotification
                CreateToastNotification: _Callable[[Windows.Data.Xml.Dom.IXmlDocument,
                                                    _Pointer[Windows.UI.Notifications.IToastNotification]],
                                                   _type.HRESULT]

            class IToastNotificationManagerStatics(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastNotificationManager
                CreateToastNotifier: _Callable[[_Pointer[Windows.UI.Notifications.IToastNotifier]],
                                               _type.HRESULT]
                CreateToastNotifierWithId: _Callable[[_type.HSTRING,
                                                      _Pointer[Windows.UI.Notifications.IToastNotifier]],
                                                     _type.HRESULT]
                GetTemplateContent: _Callable

            class IToastNotificationManagerStatics2(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastNotificationManager
                get_History: _Callable

            class IToastNotificationManagerStatics4(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastNotificationManager
                GetForUser: _Callable
                ConfigureNotificationMirroring: _Callable

            class IToastNotificationManagerStatics5(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastNotificationManager
                GetDefault: _Callable

            class IToastNotifier(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Notifications_ToastNotifier
                Show: _Callable[[Windows.UI.Notifications.IToastNotification],
                                _type.HRESULT]
                Hide: _Callable[[Windows.UI.Notifications.IToastNotification],
                                _type.HRESULT]
                get_Setting: _Callable[[_Pointer[_enum.NotificationSetting]],
                                       _type.HRESULT]
                AddToSchedule: _Callable
                RemoveFromSchedule: _Callable
                GetScheduledToastNotifications: _Callable

        class ViewManagement:
            class IUISettings(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_ViewManagement_UISettings
                get_HandPreference: _Callable[[_Pointer[_enum.HandPreference]],
                                              _type.HRESULT]
                get_CursorSize: _Callable[[_Pointer[_struct.SIZE]],
                                          _type.HRESULT]
                get_ScrollBarSize: _Callable[[_Pointer[_struct.SIZE]],
                                             _type.HRESULT]
                get_ScrollBarArrowSize: _Callable[[_Pointer[_struct.SIZE]],
                                                  _type.HRESULT]
                get_ScrollBarThumbBoxSize: _Callable[[_Pointer[_struct.SIZE]],
                                                     _type.HRESULT]
                get_MessageDuration: _Callable[[_Pointer[_type.UINT32]],
                                               _type.HRESULT]
                get_AnimationsEnabled: _Callable[[_Pointer[_type.boolean]],
                                                 _type.HRESULT]
                get_CaretBrowsingEnabled: _Callable[[_Pointer[_type.boolean]],
                                                    _type.HRESULT]
                get_CaretBlinkRate: _Callable[[_Pointer[_type.UINT32]],
                                              _type.HRESULT]
                get_CaretWidth: _Callable[[_Pointer[_type.UINT32]],
                                          _type.HRESULT]
                get_DoubleClickTime: _Callable[[_Pointer[_type.UINT32]],
                                               _type.HRESULT]
                get_MouseHoverTime: _Callable[[_Pointer[_type.UINT32]],
                                              _type.HRESULT]
                UIElementColor: _Callable[[_enum.UIElementType,
                                           _Pointer[_struct.Color]],
                                          _type.HRESULT]

        class Xaml:
            class IFrameworkElement(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_FrameworkElement
                get_Triggers: _Callable
                get_Resources: _Callable
                put_Resources: _Callable
                get_Tag: _Callable[[_Pointer[IInspectable]],
                                   _type.HRESULT]
                put_Tag: _Callable[[IInspectable],
                                   _type.HRESULT]
                get_Language: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]
                put_Language: _Callable[[_type.HSTRING],
                                        _type.HRESULT]
                get_ActualWidth: _Callable[[_Pointer[_type.DOUBLE]],
                                           _type.HRESULT]
                get_ActualHeight: _Callable[[_Pointer[_type.DOUBLE]],
                                            _type.HRESULT]
                get_Width: _Callable[[_Pointer[_type.DOUBLE]],
                                     _type.HRESULT]
                put_Width: _Callable[[_type.DOUBLE],
                                     _type.HRESULT]
                get_Height: _Callable[[_Pointer[_type.DOUBLE]],
                                      _type.HRESULT]
                put_Height: _Callable[[_type.DOUBLE],
                                      _type.HRESULT]
                get_MinWidth: _Callable[[_Pointer[_type.DOUBLE]],
                                        _type.HRESULT]
                put_MinWidth: _Callable[[_type.DOUBLE],
                                        _type.HRESULT]
                get_MaxWidth: _Callable[[_Pointer[_type.DOUBLE]],
                                        _type.HRESULT]
                put_MaxWidth: _Callable[[_type.DOUBLE],
                                        _type.HRESULT]
                get_MinHeight: _Callable[[_Pointer[_type.DOUBLE]],
                                         _type.HRESULT]
                put_MinHeight: _Callable[[_type.DOUBLE],
                                         _type.HRESULT]
                get_MaxHeight: _Callable[[_Pointer[_type.DOUBLE]],
                                         _type.HRESULT]
                put_MaxHeight: _Callable[[_type.DOUBLE],
                                         _type.HRESULT]
                get_HorizontalAlignment: _Callable[[_Pointer[_enum.HorizontalAlignment]],
                                                   _type.HRESULT]
                put_HorizontalAlignment: _Callable[[_enum.HorizontalAlignment],
                                                   _type.HRESULT]
                get_VerticalAlignment: _Callable[[_Pointer[_enum.VerticalAlignment]],
                                                 _type.HRESULT]
                put_VerticalAlignment: _Callable[[_enum.VerticalAlignment],
                                                 _type.HRESULT]
                get_Margin: _Callable[[_Pointer[_struct.Thickness]],
                                      _type.HRESULT]
                put_Margin: _Callable[[_struct.Thickness],
                                      _type.HRESULT]
                get_Name: _Callable[[_Pointer[_type.HSTRING]],
                                    _type.HRESULT]
                put_Name: _Callable[[_type.HSTRING],
                                    _type.HRESULT]
                get_BaseUri: _Callable[[_Pointer[Windows.Foundation.IUriRuntimeClass]],
                                       _type.HRESULT]
                get_DataContext: _Callable[[_Pointer[IInspectable]],
                                           _type.HRESULT]
                put_DataContext: _Callable[[IInspectable],
                                           _type.HRESULT]
                get_Style: _Callable
                put_Style: _Callable
                get_Parent: _Callable
                get_FlowDirection: _Callable[[_Pointer[_enum.FlowDirection]],
                                             _type.HRESULT]
                put_FlowDirection: _Callable[[_enum.FlowDirection],
                                             _type.HRESULT]
                add_Loaded: _Callable
                remove_Loaded: _Callable[[_struct.EventRegistrationToken],
                                         _type.HRESULT]
                add_Unloaded: _Callable
                remove_Unloaded: _Callable[[_struct.EventRegistrationToken],
                                           _type.HRESULT]
                add_SizeChanged: _Callable
                remove_SizeChanged: _Callable[[_struct.EventRegistrationToken],
                                              _type.HRESULT]
                add_LayoutUpdated: _Callable
                remove_LayoutUpdated: _Callable[[_struct.EventRegistrationToken],
                                                _type.HRESULT]
                FindName: _Callable[[_type.HSTRING,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
                SetBinding: _Callable

            class IUIElement(IInspectable):
                _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_UIElement
                get_DesiredSize: _Callable[[_Pointer[_struct.Size]],
                                           _type.HRESULT]
                get_AllowDrop: _Callable[[_Pointer[_type.boolean]],
                                         _type.HRESULT]
                put_AllowDrop: _Callable[[_type.boolean],
                                         _type.HRESULT]
                get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],
                                       _type.HRESULT]
                put_Opacity: _Callable[[_type.DOUBLE],
                                       _type.HRESULT]
                get_Clip: _Callable
                put_Clip: _Callable
                get_RenderTransform: _Callable
                put_RenderTransform: _Callable
                get_Projection: _Callable
                put_Projection: _Callable
                get_RenderTransformOrigin: _Callable[[_Pointer[_struct.Point]],
                                                     _type.HRESULT]
                put_RenderTransformOrigin: _Callable[[_struct.Point],
                                                     _type.HRESULT]
                get_IsHitTestVisible: _Callable[[_Pointer[_type.boolean]],
                                                _type.HRESULT]
                put_IsHitTestVisible: _Callable[[_type.boolean],
                                                _type.HRESULT]
                get_Visibility: _Callable[[_Pointer[_enum.Visibility]],
                                          _type.HRESULT]
                put_Visibility: _Callable[[_enum.Visibility],
                                          _type.HRESULT]
                get_RenderSize: _Callable[[_Pointer[_struct.Size]],
                                          _type.HRESULT]
                get_UseLayoutRounding: _Callable[[_Pointer[_type.boolean]],
                                                 _type.HRESULT]
                put_UseLayoutRounding: _Callable[[_type.boolean],
                                                 _type.HRESULT]
                get_Transitions: _Callable
                put_Transitions: _Callable
                get_CacheMode: _Callable
                put_CacheMode: _Callable
                get_IsTapEnabled: _Callable[[_Pointer[_type.boolean]],
                                            _type.HRESULT]
                put_IsTapEnabled: _Callable[[_type.boolean],
                                            _type.HRESULT]
                get_IsDoubleTapEnabled: _Callable[[_Pointer[_type.boolean]],
                                                  _type.HRESULT]
                put_IsDoubleTapEnabled: _Callable[[_type.boolean],
                                                  _type.HRESULT]
                get_IsRightTapEnabled: _Callable[[_Pointer[_type.boolean]],
                                                 _type.HRESULT]
                put_IsRightTapEnabled: _Callable[[_type.boolean],
                                                 _type.HRESULT]
                get_IsHoldingEnabled: _Callable[[_Pointer[_type.boolean]],
                                                _type.HRESULT]
                put_IsHoldingEnabled: _Callable[[_type.boolean],
                                                _type.HRESULT]
                get_ManipulationMode: _Callable[[_Pointer[_enum.ManipulationModes]],
                                                _type.HRESULT]
                put_ManipulationMode: _Callable[[_enum.ManipulationModes],
                                                _type.HRESULT]
                get_PointerCaptures: _Callable
                add_KeyUp: _Callable
                remove_KeyUp: _Callable[[_struct.EventRegistrationToken],
                                        _type.HRESULT]
                add_KeyDown: _Callable
                remove_KeyDown: _Callable[[_struct.EventRegistrationToken],
                                          _type.HRESULT]
                add_GotFocus: _Callable
                remove_GotFocus: _Callable[[_struct.EventRegistrationToken],
                                           _type.HRESULT]
                add_LostFocus: _Callable
                remove_LostFocus: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_DragEnter: _Callable
                remove_DragEnter: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_DragLeave: _Callable
                remove_DragLeave: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_DragOver: _Callable
                remove_DragOver: _Callable[[_struct.EventRegistrationToken],
                                           _type.HRESULT]
                add_Drop: _Callable
                remove_Drop: _Callable[[_struct.EventRegistrationToken],
                                       _type.HRESULT]
                add_PointerPressed: _Callable
                remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],
                                                 _type.HRESULT]
                add_PointerMoved: _Callable
                remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],
                                               _type.HRESULT]
                add_PointerReleased: _Callable
                remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],
                                                  _type.HRESULT]
                add_PointerEntered: _Callable
                remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],
                                                 _type.HRESULT]
                add_PointerExited: _Callable
                remove_PointerExited: _Callable[[_struct.EventRegistrationToken],
                                                _type.HRESULT]
                add_PointerCaptureLost: _Callable
                remove_PointerCaptureLost: _Callable[[_struct.EventRegistrationToken],
                                                     _type.HRESULT]
                add_PointerCanceled: _Callable
                remove_PointerCanceled: _Callable[[_struct.EventRegistrationToken],
                                                  _type.HRESULT]
                add_PointerWheelChanged: _Callable
                remove_PointerWheelChanged: _Callable[[_struct.EventRegistrationToken],
                                                      _type.HRESULT]
                add_Tapped: _Callable
                remove_Tapped: _Callable[[_struct.EventRegistrationToken],
                                         _type.HRESULT]
                add_DoubleTapped: _Callable
                remove_DoubleTapped: _Callable[[_struct.EventRegistrationToken],
                                               _type.HRESULT]
                add_Holding: _Callable
                remove_Holding: _Callable[[_struct.EventRegistrationToken],
                                          _type.HRESULT]
                add_RightTapped: _Callable
                remove_RightTapped: _Callable[[_struct.EventRegistrationToken],
                                              _type.HRESULT]
                add_ManipulationStarting: _Callable
                remove_ManipulationStarting: _Callable[[_struct.EventRegistrationToken],
                                                       _type.HRESULT]
                add_ManipulationInertiaStarting: _Callable
                remove_ManipulationInertiaStarting: _Callable[[_struct.EventRegistrationToken],
                                                              _type.HRESULT]
                add_ManipulationStarted: _Callable
                remove_ManipulationStarted: _Callable[[_struct.EventRegistrationToken],
                                                      _type.HRESULT]
                add_ManipulationDelta: _Callable
                remove_ManipulationDelta: _Callable[[_struct.EventRegistrationToken],
                                                    _type.HRESULT]
                add_ManipulationCompleted: _Callable
                remove_ManipulationCompleted: _Callable[[_struct.EventRegistrationToken],
                                                        _type.HRESULT]
                Measure: _Callable[[_struct.Size],
                                   _type.HRESULT]
                Arrange: _Callable[[_struct.Rect],
                                   _type.HRESULT]
                CapturePointer: _Callable
                ReleasePointerCapture: _Callable
                ReleasePointerCaptures: _Callable[[],
                                                  _type.HRESULT]
                AddHandler: _Callable
                RemoveHandler: _Callable
                TransformToVisual: _Callable
                InvalidateMeasure: _Callable[[],
                                             _type.HRESULT]
                InvalidateArrange: _Callable[[],
                                             _type.HRESULT]
                UpdateLayout: _Callable[[],
                                        _type.HRESULT]

            class Controls:
                class IPanel(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Controls_Panel
                    get_Children: _Callable[[_Pointer[Windows.Foundation.Collections.IVector_IUIElement]],
                                            _type.HRESULT]
                    get_Background: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                              _type.HRESULT]
                    put_Background: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                              _type.HRESULT]
                    get_IsItemsHost: _Callable[[_Pointer[_type.boolean]],
                                               _type.HRESULT]
                    get_ChildrenTransitions: _Callable
                    put_ChildrenTransitions: _Callable

                class IStackPanel(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Controls_StackPanel
                    get_AreScrollSnapPointsRegular: _Callable[[_Pointer[_type.boolean]],
                                                              _type.HRESULT]
                    put_AreScrollSnapPointsRegular: _Callable[[_type.boolean],
                                                              _type.HRESULT]
                    get_Orientation: _Callable[[_Pointer[_enum.Orientation]],
                                               _type.HRESULT]
                    put_Orientation: _Callable[[_enum.Orientation],
                                               _type.HRESULT]

                class IStackPanelFactory(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Controls_StackPanel
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IStackPanel]],
                                              _type.HRESULT]

                class IStackPanelStatics(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Controls_StackPanel
                    get_AreScrollSnapPointsRegularProperty: _Callable
                    get_OrientationProperty: _Callable

                class ITextBlock(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Controls_TextBlock
                    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],
                                            _type.HRESULT]
                    put_FontSize: _Callable[[_type.DOUBLE],
                                            _type.HRESULT]
                    get_FontFamily: _Callable
                    put_FontFamily: _Callable
                    get_FontWeight: _Callable
                    put_FontWeight: _Callable
                    get_FontStyle: _Callable
                    put_FontStyle: _Callable
                    get_FontStretch: _Callable
                    put_FontStretch: _Callable
                    get_CharacterSpacing: _Callable[[_Pointer[_type.INT32]],
                                                    _type.HRESULT]
                    put_CharacterSpacing: _Callable[[_type.INT32],
                                                    _type.HRESULT]
                    get_Foreground: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                              _type.HRESULT]
                    put_Foreground: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                              _type.HRESULT]
                    get_TextWrapping: _Callable[[_Pointer[_enum.TextWrapping]],
                                                _type.HRESULT]
                    put_TextWrapping: _Callable[[_enum.TextWrapping],
                                                _type.HRESULT]
                    get_TextTrimming: _Callable[[_Pointer[_enum.TextTrimming]],
                                                _type.HRESULT]
                    put_TextTrimming: _Callable[[_enum.TextTrimming],
                                                _type.HRESULT]
                    get_TextAlignment: _Callable[[_Pointer[_enum.TextAlignment]],
                                                 _type.HRESULT]
                    put_TextAlignment: _Callable[[_enum.TextAlignment],
                                                 _type.HRESULT]
                    get_Text: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]
                    put_Text: _Callable[[_type.HSTRING],
                                        _type.HRESULT]
                    get_Inlines: _Callable
                    get_Padding: _Callable[[_Pointer[_struct.Thickness]],
                                           _type.HRESULT]
                    put_Padding: _Callable[[_struct.Thickness],
                                           _type.HRESULT]
                    get_LineHeight: _Callable[[_Pointer[_type.DOUBLE]],
                                              _type.HRESULT]
                    put_LineHeight: _Callable[[_type.DOUBLE],
                                              _type.HRESULT]
                    get_LineStackingStrategy: _Callable[[_Pointer[_enum.LineStackingStrategy]],
                                                        _type.HRESULT]
                    put_LineStackingStrategy: _Callable[[_enum.LineStackingStrategy],
                                                        _type.HRESULT]
                    get_IsTextSelectionEnabled: _Callable[[_Pointer[_type.boolean]],
                                                          _type.HRESULT]
                    put_IsTextSelectionEnabled: _Callable[[_type.boolean],
                                                          _type.HRESULT]
                    get_SelectedText: _Callable[[_Pointer[_type.HSTRING]],
                                                _type.HRESULT]
                    get_ContentStart: _Callable
                    get_ContentEnd: _Callable
                    get_SelectionStart: _Callable
                    get_SelectionEnd: _Callable
                    get_BaselineOffset: _Callable[[_Pointer[_type.DOUBLE]],
                                                  _type.HRESULT]
                    add_SelectionChanged: _Callable
                    remove_SelectionChanged: _Callable[[_struct.EventRegistrationToken],
                                                       _type.HRESULT]
                    add_ContextMenuOpening: _Callable
                    remove_ContextMenuOpening: _Callable[[_struct.EventRegistrationToken],
                                                         _type.HRESULT]
                    SelectAll: _Callable[[],
                                         _type.HRESULT]
                    Select: _Callable
                    Focus: _Callable[[_enum.FocusState,
                                      _Pointer[_type.boolean]],
                                     _type.HRESULT]

                class IUIElementCollection(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Controls_UIElementCollection
                    Move: _Callable[[_type.UINT32,
                                     _type.UINT32],
                                    _type.HRESULT]

            class Hosting:
                class IDesktopWindowXamlSource(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Hosting_DesktopWindowXamlSource
                    get_Content: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                           _type.HRESULT]
                    put_Content: _Callable[[Windows.UI.Xaml.IUIElement],
                                           _type.HRESULT]
                    get_HasFocus: _Callable[[_Pointer[_type.boolean]],
                                            _type.HRESULT]
                    add_TakeFocusRequested: _Callable
                    remove_TakeFocusRequested: _Callable[[_struct.EventRegistrationToken],
                                                         _type.HRESULT]
                    add_GotFocus: _Callable
                    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],
                                               _type.HRESULT]
                    NavigateFocus: _Callable

                class IDesktopWindowXamlSourceFactory(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Hosting_DesktopWindowXamlSource
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource]],
                                              _type.HRESULT]

                class IWindowsXamlManager(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Hosting_WindowsXamlManager

                class IWindowsXamlManagerStatics(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Hosting_WindowsXamlManager
                    InitializeForCurrentThread: _Callable[[_Pointer[Windows.UI.Xaml.Hosting.IWindowsXamlManager]],
                                                          _type.HRESULT]

            class Media:
                class IBrush(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Media_Brush
                    get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],
                                           _type.HRESULT]
                    put_Opacity: _Callable[[_type.DOUBLE],
                                           _type.HRESULT]
                    get_Transform: _Callable
                    put_Transform: _Callable
                    get_RelativeTransform: _Callable
                    put_RelativeTransform: _Callable

                class ISolidColorBrush(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Media_SolidColorBrush
                    get_Color: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
                    put_Color: _Callable[[_struct.Color],
                                         _type.HRESULT]

                class ISolidColorBrushFactory(IInspectable):
                    _RuntimeClass_ = _const.RuntimeClass_Windows_UI_Xaml_Media_SolidColorBrush
                    CreateInstanceWithColor: _Callable[[_struct.Color,
                                                        _Pointer[Windows.UI.Xaml.Media.ISolidColorBrush]],
                                                       _type.HRESULT]
