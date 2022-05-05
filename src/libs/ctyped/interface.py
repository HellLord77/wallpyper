from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable, Generic as _Generic, Optional as _Optional

from . import const as _const, enum as _enum, lib as _lib, macro as _macro, struct as _struct, type as _type
from ._utils import _Pointer, _addressof, _byref, _format_annotations, _func_doc, _pointer, _resolve_type

_K = _typing.TypeVar('_K')
_V = _typing.TypeVar('_V')
_T = _typing.TypeVar('_T')
_TArgs = _typing.TypeVar('_TArgs')
_TProgress = _typing.TypeVar('_TProgress')
_TResult = _typing.TypeVar('_TResult')
_TSender = _typing.TypeVar('_TSender')


class _Template:
    _args = None
    _classes = {}

    def __init_subclass__(cls):
        cls._classes = {}
        super().__init_subclass__()

    def __class_getitem__(cls, item):
        if not isinstance(item, tuple):
            item = item,
        if item not in cls._classes:
            # noinspection PyUnresolvedReferences
            args = {generic: arg for generic, arg in zip(
                cls.__parameters__, _typing.get_args(super().__class_getitem__(item)))}
            qualname = f'{cls.__qualname__}_{"_".join(type_.__name__ for type_ in args.values())}'
            cls._classes[item] = type(qualname.rsplit('.', 1)[-1], (cls,), {'__qualname__': qualname, '_args': args})
        return cls._classes[item]


class _Interface(_type.c_void_p):
    _vtbl = _ctypes.Structure
    _docs = {}

    def __new__(cls):
        if cls._vtbl.__name__ != cls.__name__:
            cls._vtbl = _get_vtbl(cls)
            # noinspection PyProtectedMember
            annots = {name: annot for base in cls.__mro__ for name, annot in getattr(base, '__annotations__', {}).items()}
            # noinspection PyProtectedMember
            cls.__doc__ = '\n\n'.join(_func_doc(name, types._restype_, types._argtypes_[1:], _format_annotations(annots[name])) for name, types in cls._vtbl._fields_)
            # noinspection PyProtectedMember
            cls._docs = {name: '\n'.join(doc for doc in cls.__doc__.split('\n') if doc.startswith(f'{name}(')) for name, _ in cls._vtbl._fields_}
        return super().__new__(cls)

    def __getattr__(self, name: str):
        # noinspection PyProtectedMember,PyUnresolvedReferences
        for name_, _ in self._vtbl._fields_:
            if name == name_:
                if not self.value:
                    raise RuntimeError(f"Interface object '{type(self).__name__}' partially initialized")
                # noinspection PyUnresolvedReferences
                funcs = self._vtbl.from_address(_type.c_void_p.from_address(self.value).value)
                # noinspection PyProtectedMember,PyUnresolvedReferences
                for name__, types in self._vtbl._fields_:
                    method = getattr(funcs, name__)
                    method.__name__ = name__
                    method.__doc__ = self._docs[name__]
                    setattr(self, name__, _types.MethodType(method, self))
                break
        return super().__getattribute__(name)


# noinspection PyPep8Naming
class _Interface_impl(_type.c_void_p):  # TODO docs
    _iid_refs = None
    _vtbl = _ctypes.Structure
    _refs = {}

    def __hash__(self):
        return self.value

    def __init__(self):
        # noinspection PyTypeChecker,PyProtectedMember
        self._ptr = _pointer(self._vtbl(*(type_(_functools.wraps(func := getattr(self, name))(lambda _, *args, _func=func: _func(*args))) for name, type_ in self._vtbl._fields_)))
        super().__init__(_addressof(self._ptr))
        self._refs[self] = 1

    def __new__(cls):
        if cls._vtbl.__name__ != cls.__name__:
            cls._iid_refs = []
            base = cls
            for base_ in cls.__mro__[cls.__mro__.index(_Interface_impl)::-1]:
                # noinspection PyProtectedMember
                if __name__ == base_.__module__ and not base_.__name__.startswith(
                        '_') and not (issubclass(base_, _Template) and base_._args is None):
                    # noinspection PyTypeChecker,PyProtectedMember
                    cls._iid_refs.append(_byref(_macro._uuidof(base_)))
                    base = base_
            cls._iid_refs = tuple(cls._iid_refs)
            cls._vtbl = _get_vtbl(base, cls.__name__)
        return super().__new__(cls)


def _get_vtbl(cls: type, name: _Optional[str] = None) -> type[_ctypes.Structure]:
    fields = []
    for name, annot in _typing.get_type_hints(cls).items():
        types = _resolve_type(annot, getattr(cls, '_args', None))
        types.insert(1, _type.c_void_p)
        fields.append((name, _ctypes.WINFUNCTYPE(*types)))
    # noinspection PyTypeChecker
    return type(cls.__name__ if name is None else name, (_ctypes.Structure,), {'_fields_': tuple(fields)})


class _IUnknown:
    QueryInterface: _Callable[[_Pointer[_struct.IID],
                               _type.LPVOID],
                              _type.HRESULT]
    AddRef: _Callable[[],
                      _type.ULONG]
    Release: _Callable[[],
                       _type.ULONG]


class IUnknown(_IUnknown, _Interface):
    _CLSID_ = ''


# noinspection PyPep8Naming
class IUnknown_impl(_IUnknown, _Interface_impl):
    # noinspection PyPep8Naming
    def QueryInterface(self, riid: _Pointer[_struct.IID], ppvObject: _type.LPVOID) -> _type.HRESULT:
        if not ppvObject:
            return _const.E_INVALIDARG
        obj_ref = _type.LPVOID.from_address(ppvObject) if isinstance(ppvObject, int) else ppvObject.contents
        obj_ref.value = None
        for iid_ref in self._iid_refs:
            if _lib.Ole32.IsEqualGUID(iid_ref, riid):
                obj_ref.value = self.value
                self.AddRef()
                return _const.NOERROR
        return _const.E_NOINTERFACE

    # noinspection PyPep8Naming
    def AddRef(self) -> _type.ULONG:
        self._refs[self] += 1
        return self._refs[self]

    # noinspection PyPep8Naming
    def Release(self) -> _type.ULONG:
        self._refs[self] -= 1
        try:
            return self._refs[self]
        finally:
            if not self._refs[self]:
                del self._refs[self]


class IInspectable(IUnknown):
    GetIids: _Callable[[_Pointer[_type.ULONG],
                        _Pointer[_Pointer[_struct.IID]]],
                       _type.HRESULT]
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
    SetBalloonInfo: _Callable[[_Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR],
                               _type.DWORD],
                              _type.HRESULT]
    SetBalloonRetry: _Callable[[_type.DWORD,
                                _type.DWORD,
                                _type.UINT],
                               _type.HRESULT]
    SetIconInfo: _Callable[[_Optional[_type.HICON],
                            _type.LPCWSTR],
                           _type.HRESULT]
    Show: _Callable[[_Optional[IQueryContinue_impl],
                     _type.DWORD],
                    _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR],
                         _type.HRESULT]


class IUserNotification2(IUnknown):
    _CLSID_ = _const.CLSID_UserNotification
    SetBalloonInfo: _Callable[[_Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR],
                               _type.DWORD],
                              _type.HRESULT]
    SetBalloonRetry: _Callable[[_type.DWORD,
                                _type.DWORD,
                                _type.UINT],
                               _type.HRESULT]
    SetIconInfo: _Callable[[_Optional[_type.HICON],
                            _Optional[_type.LPCWSTR]],
                           _type.HRESULT]
    Show: _Callable[[_Optional[_Pointer[IQueryContinue_impl]],
                     _type.DWORD,
                     _Optional[_Pointer[IUserNotificationCallback_impl]]],
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


class _IQueryContinue:
    QueryContinue: _Callable[[],
                             _type.HRESULT]


class IQueryContinue(_IQueryContinue, IUnknown):
    pass


# noinspection PyPep8Naming
class IQueryContinue_impl(_IQueryContinue, IUnknown_impl):
    pass


class _IQueryContinueWithStatus:
    SetStatusMessage: _Callable[[_type.LPCWSTR],
                                _type.HRESULT]


class IQueryContinueWithStatus(_IQueryContinueWithStatus, IQueryContinue):
    pass


# noinspection PyPep8Naming
class IQueryContinueWithStatus_impl(_IQueryContinueWithStatus, IQueryContinue_impl):
    pass


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


class _IUserNotificationCallback:
    OnBalloonUserClick: _Callable[[_Pointer[_struct.POINT]],
                                  _type.HRESULT]
    OnLeftClick: _Callable[[_Pointer[_struct.POINT]],
                           _type.HRESULT]
    OnContextMenu: _Callable[[_Pointer[_struct.POINT]],
                             _type.HRESULT]


class IUserNotificationCallback(_IUserNotificationCallback, IUnknown):
    pass


# noinspection PyPep8Naming
class IUserNotificationCallback_impl(_IUserNotificationCallback, IUnknown_impl):
    pass


class IActivationFactory(IInspectable):
    ActivateInstance: _Callable[[_Pointer[IInspectable]],
                                _type.HRESULT]


class IAsyncInfo(IInspectable):
    get_Id: _Callable[[_Pointer[_type.c_uint32]],
                      _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Foundation.AsyncStatus]],
                          _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],
                             _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class Windows:
    class ApplicationModel:
        class IAppDisplayInfo(IInspectable):
            get_DisplayName: _Callable
            get_Description: _Callable
            GetLogo: _Callable

        class IAppInfo(IInspectable):
            get_Id: _Callable
            get_AppUserModelId: _Callable
            get_DisplayInfo: _Callable
            get_PackageFamilyName: _Callable

        class IAppInfo2(IInspectable):
            get_Package: _Callable

        class IAppInfo3(IInspectable):
            get_ExecutionContext: _Callable

        class IAppInfo4(IInspectable):
            get_SupportedFileExtensions: _Callable

        class IAppInfoStatics(IInspectable):
            get_Current: _Callable
            GetFromAppUserModelId: _Callable
            GetFromAppUserModelIdForUser: _Callable

        class IAppInstallerInfo(IInspectable):
            get_Uri: _Callable

        class IAppInstallerInfo2(IInspectable):
            get_OnLaunch: _Callable
            get_HoursBetweenUpdateChecks: _Callable
            get_ShowPrompt: _Callable
            get_UpdateBlocksActivation: _Callable
            get_AutomaticBackgroundTask: _Callable
            get_ForceUpdateFromAnyVersion: _Callable
            get_IsAutoRepairEnabled: _Callable
            get_Version: _Callable
            get_LastChecked: _Callable
            get_PausedUntil: _Callable
            get_UpdateUris: _Callable
            get_RepairUris: _Callable
            get_DependencyPackageUris: _Callable
            get_OptionalPackageUris: _Callable
            get_PolicySource: _Callable

        class IAppInstance(IInspectable):
            get_Key: _Callable
            get_IsCurrentInstance: _Callable
            RedirectActivationTo: _Callable

        class IAppInstanceStatics(IInspectable):
            get_RecommendedInstance: _Callable
            GetActivatedEventArgs: _Callable
            FindOrRegisterInstanceForKey: _Callable
            Unregister: _Callable
            GetInstances: _Callable

        class IDesignModeStatics(IInspectable):
            get_DesignModeEnabled: _Callable

        class IDesignModeStatics2(IInspectable):
            get_DesignMode2Enabled: _Callable

        class IEnteredBackgroundEventArgs(IInspectable):
            GetDeferral: _Callable

        class IFullTrustProcessLaunchResult(IInspectable):
            get_LaunchResult: _Callable
            get_ExtendedError: _Callable

        class IFullTrustProcessLauncherStatics(IInspectable):
            LaunchFullTrustProcessForCurrentAppAsync: _Callable
            LaunchFullTrustProcessForCurrentAppWithParametersAsync: _Callable
            LaunchFullTrustProcessForAppAsync: _Callable
            LaunchFullTrustProcessForAppWithParametersAsync: _Callable

        class IFullTrustProcessLauncherStatics2(IInspectable):
            LaunchFullTrustProcessForCurrentAppWithArgumentsAsync: _Callable
            LaunchFullTrustProcessForAppWithArgumentsAsync: _Callable

        class ILeavingBackgroundEventArgs(IInspectable):
            GetDeferral: _Callable

        class ILimitedAccessFeatureRequestResult(IInspectable):
            get_FeatureId: _Callable
            get_Status: _Callable
            get_EstimatedRemovalDate: _Callable

        class ILimitedAccessFeaturesStatics(IInspectable):
            TryUnlockFeature: _Callable

        class IPackage(IInspectable):
            get_Id: _Callable
            get_InstalledLocation: _Callable
            get_IsFramework: _Callable
            get_Dependencies: _Callable

        class IPackage2(IInspectable):
            get_DisplayName: _Callable
            get_PublisherDisplayName: _Callable
            get_Description: _Callable
            get_Logo: _Callable
            get_IsResourcePackage: _Callable
            get_IsBundle: _Callable
            get_IsDevelopmentMode: _Callable

        class IPackage3(IInspectable):
            get_Status: _Callable
            get_InstalledDate: _Callable
            GetAppListEntriesAsync: _Callable

        class IPackage4(IInspectable):
            get_SignatureKind: _Callable
            get_IsOptional: _Callable
            VerifyContentIntegrityAsync: _Callable

        class IPackage5(IInspectable):
            GetContentGroupsAsync: _Callable
            GetContentGroupAsync: _Callable
            StageContentGroupsAsync: _Callable
            StageContentGroupsWithPriorityAsync: _Callable
            SetInUseAsync: _Callable

        class IPackage6(IInspectable):
            GetAppInstallerInfo: _Callable
            CheckUpdateAvailabilityAsync: _Callable

        class IPackage7(IInspectable):
            get_MutableLocation: _Callable
            get_EffectiveLocation: _Callable

        class IPackage8(IInspectable):
            get_EffectiveExternalLocation: _Callable
            get_MachineExternalLocation: _Callable
            get_UserExternalLocation: _Callable
            get_InstalledPath: _Callable
            get_MutablePath: _Callable
            get_EffectivePath: _Callable
            get_EffectiveExternalPath: _Callable
            get_MachineExternalPath: _Callable
            get_UserExternalPath: _Callable
            GetLogoAsRandomAccessStreamReference: _Callable
            GetAppListEntries: _Callable
            get_IsStub: _Callable

        class IPackageCatalog(IInspectable):
            add_PackageStaging: _Callable
            remove_PackageStaging: _Callable
            add_PackageInstalling: _Callable
            remove_PackageInstalling: _Callable
            add_PackageUpdating: _Callable
            remove_PackageUpdating: _Callable
            add_PackageUninstalling: _Callable
            remove_PackageUninstalling: _Callable
            add_PackageStatusChanged: _Callable
            remove_PackageStatusChanged: _Callable

        class IPackageCatalog2(IInspectable):
            add_PackageContentGroupStaging: _Callable
            remove_PackageContentGroupStaging: _Callable
            AddOptionalPackageAsync: _Callable

        class IPackageCatalog3(IInspectable):
            RemoveOptionalPackagesAsync: _Callable

        class IPackageCatalog4(IInspectable):
            AddResourcePackageAsync: _Callable
            RemoveResourcePackagesAsync: _Callable

        class IPackageCatalogAddOptionalPackageResult(IInspectable):
            get_Package: _Callable
            get_ExtendedError: _Callable

        class IPackageCatalogAddResourcePackageResult(IInspectable):
            get_Package: _Callable
            get_IsComplete: _Callable
            get_ExtendedError: _Callable

        class IPackageCatalogRemoveOptionalPackagesResult(IInspectable):
            get_PackagesRemoved: _Callable
            get_ExtendedError: _Callable

        class IPackageCatalogRemoveResourcePackagesResult(IInspectable):
            get_PackagesRemoved: _Callable
            get_ExtendedError: _Callable

        class IPackageCatalogStatics(IInspectable):
            OpenForCurrentPackage: _Callable
            OpenForCurrentUser: _Callable

        class IPackageContentGroup(IInspectable):
            get_Package: _Callable
            get_Name: _Callable
            get_State: _Callable
            get_IsRequired: _Callable

        class IPackageContentGroupStagingEventArgs(IInspectable):
            get_ActivityId: _Callable
            get_Package: _Callable
            get_Progress: _Callable
            get_IsComplete: _Callable
            get_ErrorCode: _Callable
            get_ContentGroupName: _Callable
            get_IsContentGroupRequired: _Callable

        class IPackageContentGroupStatics(IInspectable):
            get_RequiredGroupName: _Callable

        class IPackageId(IInspectable):
            get_Name: _Callable
            get_Version: _Callable
            get_Architecture: _Callable
            get_ResourceId: _Callable
            get_Publisher: _Callable
            get_PublisherId: _Callable
            get_FullName: _Callable
            get_FamilyName: _Callable

        class IPackageIdWithMetadata(IInspectable):
            get_ProductId: _Callable
            get_Author: _Callable

        class IPackageInstallingEventArgs(IInspectable):
            get_ActivityId: _Callable
            get_Package: _Callable
            get_Progress: _Callable
            get_IsComplete: _Callable
            get_ErrorCode: _Callable

        class IPackageStagingEventArgs(IInspectable):
            get_ActivityId: _Callable
            get_Package: _Callable
            get_Progress: _Callable
            get_IsComplete: _Callable
            get_ErrorCode: _Callable

        class IPackageStatics(IInspectable):
            get_Current: _Callable

        class IPackageStatus(IInspectable):
            VerifyIsOK: _Callable
            get_NotAvailable: _Callable
            get_PackageOffline: _Callable
            get_DataOffline: _Callable
            get_Disabled: _Callable
            get_NeedsRemediation: _Callable
            get_LicenseIssue: _Callable
            get_Modified: _Callable
            get_Tampered: _Callable
            get_DependencyIssue: _Callable
            get_Servicing: _Callable
            get_DeploymentInProgress: _Callable

        class IPackageStatus2(IInspectable):
            get_IsPartiallyStaged: _Callable

        class IPackageStatusChangedEventArgs(IInspectable):
            get_Package: _Callable

        class IPackageUninstallingEventArgs(IInspectable):
            get_ActivityId: _Callable
            get_Package: _Callable
            get_Progress: _Callable
            get_IsComplete: _Callable
            get_ErrorCode: _Callable

        class IPackageUpdateAvailabilityResult(IInspectable):
            get_Availability: _Callable
            get_ExtendedError: _Callable

        class IPackageUpdatingEventArgs(IInspectable):
            get_ActivityId: _Callable
            get_SourcePackage: _Callable
            get_TargetPackage: _Callable
            get_Progress: _Callable
            get_IsComplete: _Callable
            get_ErrorCode: _Callable

        class IPackageWithMetadata(IInspectable):
            get_InstallDate: _Callable
            GetThumbnailToken: _Callable
            Launch: _Callable

        class IStartupTask(IInspectable):
            RequestEnableAsync: _Callable
            Disable: _Callable
            get_State: _Callable
            get_TaskId: _Callable

        class IStartupTaskStatics(IInspectable):
            GetForCurrentPackageAsync: _Callable
            GetAsync: _Callable

        class ISuspendingDeferral(IInspectable):
            Complete: _Callable

        class ISuspendingEventArgs(IInspectable):
            get_SuspendingOperation: _Callable

        class ISuspendingOperation(IInspectable):
            GetDeferral: _Callable
            get_Deadline: _Callable

    class Data:
        class Xml:
            class Dom:
                class IDtdEntity(IInspectable):
                    get_PublicId: _Callable
                    get_SystemId: _Callable
                    get_NotationName: _Callable

                class IDtdNotation(IInspectable):
                    get_PublicId: _Callable
                    get_SystemId: _Callable

                class IXmlAttribute(IInspectable):
                    get_Name: _Callable
                    get_Specified: _Callable
                    get_Value: _Callable
                    put_Value: _Callable

                class IXmlCDataSection(IInspectable):
                    pass

                class IXmlCharacterData(IInspectable):
                    get_Data: _Callable
                    put_Data: _Callable
                    get_Length: _Callable
                    SubstringData: _Callable
                    AppendData: _Callable
                    InsertData: _Callable
                    DeleteData: _Callable
                    ReplaceData: _Callable

                class IXmlComment(IInspectable):
                    pass

                class IXmlDocument(IInspectable):
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

                class IXmlDocumentFragment(IInspectable):
                    pass

                class IXmlDocumentIO(IInspectable):
                    LoadXml: _Callable[[_type.HSTRING],
                                       _type.HRESULT]
                    LoadXmlWithSettings: _Callable
                    SaveToFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                                _Pointer[Windows.Foundation.IAsyncAction]],
                                               _type.HRESULT]

                class IXmlDocumentIO2(IInspectable):
                    LoadXmlFromBuffer: _Callable[[Windows.Storage.Streams.IBuffer],
                                                 _type.HRESULT]
                    LoadXmlFromBufferWithSettings: _Callable

                class IXmlDocumentStatics(IInspectable):
                    LoadFromUriAsync: _Callable[[Windows.Foundation.IUriRuntimeClass,
                                                 _Pointer[Windows.Foundation.IAsyncOperation[Windows.Data.Xml.Dom.IXmlDocument]]],
                                                _type.HRESULT]
                    LoadFromUriWithSettingsAsync: _Callable
                    LoadFromFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                                  _Pointer[Windows.Foundation.IAsyncOperation[Windows.Data.Xml.Dom.IXmlDocument]]],
                                                 _type.HRESULT]
                    LoadFromFileWithSettingsAsync: _Callable

                class IXmlDocumentType(IInspectable):
                    get_Name: _Callable
                    get_Entities: _Callable
                    get_Notations: _Callable

                class IXmlDomImplementation(IInspectable):
                    HasFeature: _Callable

                class IXmlElement(IInspectable):
                    get_TagName: _Callable
                    GetAttribute: _Callable
                    SetAttribute: _Callable
                    RemoveAttribute: _Callable
                    GetAttributeNode: _Callable
                    SetAttributeNode: _Callable
                    RemoveAttributeNode: _Callable
                    GetElementsByTagName: _Callable
                    SetAttributeNS: _Callable
                    GetAttributeNS: _Callable
                    RemoveAttributeNS: _Callable
                    SetAttributeNodeNS: _Callable
                    GetAttributeNodeNS: _Callable

                class IXmlEntityReference(IInspectable):
                    pass

                class IXmlLoadSettings(IInspectable):
                    get_MaxElementDepth: _Callable
                    put_MaxElementDepth: _Callable
                    get_ProhibitDtd: _Callable
                    put_ProhibitDtd: _Callable
                    get_ResolveExternals: _Callable
                    put_ResolveExternals: _Callable
                    get_ValidateOnParse: _Callable
                    put_ValidateOnParse: _Callable
                    get_ElementContentWhiteSpace: _Callable
                    put_ElementContentWhiteSpace: _Callable

                class IXmlNamedNodeMap(IInspectable):
                    get_Length: _Callable
                    Item: _Callable
                    GetNamedItem: _Callable
                    SetNamedItem: _Callable
                    RemoveNamedItem: _Callable
                    GetNamedItemNS: _Callable
                    RemoveNamedItemNS: _Callable
                    SetNamedItemNS: _Callable

                class IXmlNode(IInspectable):
                    get_NodeValue: _Callable
                    put_NodeValue: _Callable
                    get_NodeType: _Callable
                    get_NodeName: _Callable
                    get_ParentNode: _Callable
                    get_ChildNodes: _Callable
                    get_FirstChild: _Callable
                    get_LastChild: _Callable
                    get_PreviousSibling: _Callable
                    get_NextSibling: _Callable
                    get_Attributes: _Callable
                    HasChildNodes: _Callable
                    get_OwnerDocument: _Callable
                    InsertBefore: _Callable
                    ReplaceChild: _Callable
                    RemoveChild: _Callable
                    AppendChild: _Callable
                    CloneNode: _Callable
                    get_NamespaceUri: _Callable
                    get_LocalName: _Callable
                    get_Prefix: _Callable
                    Normalize: _Callable
                    put_Prefix: _Callable

                class IXmlNodeList(IInspectable):
                    get_Length: _Callable
                    Item: _Callable

                class IXmlNodeSelector(IInspectable):
                    SelectSingleNode: _Callable
                    SelectNodes: _Callable
                    SelectSingleNodeNS: _Callable
                    SelectNodesNS: _Callable

                class IXmlNodeSerializer(IInspectable):
                    GetXml: _Callable[[_Pointer[_type.HSTRING]],
                                      _type.HRESULT]
                    get_InnerText: _Callable[[_Pointer[_type.HSTRING]],
                                             _type.HRESULT]
                    put_InnerText: _Callable[[_type.HSTRING],
                                             _type.HRESULT]

                class IXmlProcessingInstruction(IInspectable):
                    get_Target: _Callable
                    get_Data: _Callable
                    put_Data: _Callable

                class IXmlText(IInspectable):
                    SplitText: _Callable

    class Foundation:
        class _IAsyncActionCompletedHandler:
            Invoke: _Callable[[Windows.Foundation.IAsyncAction,
                               _enum.Windows.Foundation.AsyncStatus],
                              _type.HRESULT]

        class IAsyncActionCompletedHandler(_IAsyncActionCompletedHandler, IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncActionCompletedHandler_impl(_IAsyncActionCompletedHandler, IUnknown_impl):
            pass

        class _IDeferralCompletedHandler:
            Invoke: _Callable[[],
                              _type.HRESULT]

        class IDeferralCompletedHandler(_IDeferralCompletedHandler, IUnknown):
            pass

        # noinspection PyPep8Naming
        class IDeferralCompletedHandler_impl(_IDeferralCompletedHandler, IUnknown_impl):
            pass

        class IAsyncAction(IInspectable):
            put_Completed: _Callable[[Windows.Foundation.IAsyncActionCompletedHandler_impl],
                                     _type.HRESULT]
            get_Completed: _Callable[[_Pointer[Windows.Foundation.IAsyncActionCompletedHandler]],
                                     _type.HRESULT]
            GetResults: _Callable[[],
                                  _type.HRESULT]

        class IClosable(IInspectable):
            Close: _Callable[[],
                             _type.HRESULT]

        class IDeferral(IInspectable):
            Complete: _Callable[[],
                                _type.HRESULT]

        class IDeferralFactory(IInspectable):
            Create: _Callable

        class IGetActivationFactory(IInspectable):
            GetActivationFactory: _Callable[[_type.HSTRING,
                                             _Pointer[IInspectable]],
                                            _type.HRESULT]

        class IGuidHelperStatics(IInspectable):
            CreateNewGuid: _Callable
            get_Empty: _Callable
            Equals: _Callable

        class IMemoryBuffer(IInspectable):
            CreateReference: _Callable

        class IMemoryBufferFactory(IInspectable):
            Create: _Callable

        class IMemoryBufferReference(IInspectable):
            get_Capacity: _Callable
            add_Closed: _Callable
            remove_Closed: _Callable

        class IPropertyValue(IInspectable):
            get_Type: _Callable
            get_IsNumericScalar: _Callable
            GetUInt8: _Callable
            GetInt16: _Callable
            GetUInt16: _Callable
            GetInt32: _Callable
            GetUInt32: _Callable
            GetInt64: _Callable
            GetUInt64: _Callable
            GetSingle: _Callable
            GetDouble: _Callable
            GetChar16: _Callable
            GetBoolean: _Callable
            GetString: _Callable
            GetGuid: _Callable
            GetDateTime: _Callable
            GetTimeSpan: _Callable
            GetPoint: _Callable
            GetSize: _Callable
            GetRect: _Callable
            GetUInt8Array: _Callable
            GetInt16Array: _Callable
            GetUInt16Array: _Callable
            GetInt32Array: _Callable
            GetUInt32Array: _Callable
            GetInt64Array: _Callable
            GetUInt64Array: _Callable
            GetSingleArray: _Callable
            GetDoubleArray: _Callable
            GetChar16Array: _Callable
            GetBooleanArray: _Callable
            GetStringArray: _Callable
            GetInspectableArray: _Callable
            GetGuidArray: _Callable
            GetDateTimeArray: _Callable
            GetTimeSpanArray: _Callable
            GetPointArray: _Callable
            GetSizeArray: _Callable
            GetRectArray: _Callable

        class IPropertyValueStatics(IInspectable):
            CreateEmpty: _Callable
            CreateUInt8: _Callable
            CreateInt16: _Callable
            CreateUInt16: _Callable
            CreateInt32: _Callable
            CreateUInt32: _Callable
            CreateInt64: _Callable
            CreateUInt64: _Callable
            CreateSingle: _Callable
            CreateDouble: _Callable
            CreateChar16: _Callable
            CreateBoolean: _Callable
            CreateString: _Callable
            CreateInspectable: _Callable
            CreateGuid: _Callable
            CreateDateTime: _Callable
            CreateTimeSpan: _Callable
            CreatePoint: _Callable
            CreateSize: _Callable
            CreateRect: _Callable
            CreateUInt8Array: _Callable
            CreateInt16Array: _Callable
            CreateUInt16Array: _Callable
            CreateInt32Array: _Callable
            CreateUInt32Array: _Callable
            CreateInt64Array: _Callable
            CreateUInt64Array: _Callable
            CreateSingleArray: _Callable
            CreateDoubleArray: _Callable
            CreateChar16Array: _Callable
            CreateBooleanArray: _Callable
            CreateStringArray: _Callable
            CreateInspectableArray: _Callable
            CreateGuidArray: _Callable
            CreateDateTimeArray: _Callable
            CreateTimeSpanArray: _Callable
            CreatePointArray: _Callable
            CreateSizeArray: _Callable
            CreateRectArray: _Callable

        class IStringable(IInspectable):
            ToString: _Callable

        class IUriEscapeStatics(IInspectable):
            UnescapeComponent: _Callable
            EscapeComponent: _Callable

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
            Equals: _Callable[[Windows.Foundation.IUriRuntimeClass,
                               _Pointer[_type.boolean]],
                              _type.HRESULT]
            CombineUri: _Callable[[_type.HSTRING,
                                   _Pointer[Windows.Foundation.IUriRuntimeClass]],
                                  _type.HRESULT]

            class IUriRuntimeClassFactory(IInspectable):
                CreateUri: _Callable[[_type.HSTRING,
                                      _Pointer[Windows.Foundation.IUriRuntimeClass]],
                                     _type.HRESULT]
                CreateWithRelativeUri: _Callable[[_type.HSTRING,
                                                  _type.HSTRING,
                                                  _Pointer[Windows.Foundation.IUriRuntimeClass]],
                                                 _type.HRESULT]

        class IUriRuntimeClassFactory(IInspectable):
            CreateUri: _Callable
            CreateWithRelativeUri: _Callable

        class IUriRuntimeClassWithAbsoluteCanonicalUri(IInspectable):
            get_AbsoluteCanonicalUri: _Callable
            get_DisplayIri: _Callable

        class IWwwFormUrlDecoderEntry(IInspectable):
            get_Name: _Callable
            get_Value: _Callable

        class IWwwFormUrlDecoderRuntimeClass(IInspectable):
            GetFirstValueByName: _Callable

        class IWwwFormUrlDecoderRuntimeClassFactory(IInspectable):
            CreateWwwFormUrlDecoder: _Callable

        class _IAsyncOperationProgressHandler(_Template):
            Invoke: _Callable[[Windows.Foundation.IAsyncOperationWithProgress[_TResult, _TProgress],
                               _TProgress],
                              _type.HRESULT]

        class IAsyncOperationProgressHandler(_IAsyncOperationProgressHandler, _Generic[_TResult, _TProgress], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncOperationProgressHandler_impl(_IAsyncOperationProgressHandler, _Generic[_TResult, _TProgress], IUnknown_impl):
            pass

        class _IAsyncOperationWithProgressCompletedHandler(_Template):
            Invoke: _Callable[[Windows.Foundation.IAsyncOperationWithProgress[_TResult, _TProgress],
                               _enum.Windows.Foundation.AsyncStatus],
                              _type.HRESULT]

        class IAsyncOperationWithProgressCompletedHandler(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncOperationWithProgressCompletedHandler_impl(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], IUnknown_impl):
            pass

        class _IAsyncOperationCompletedHandler(_Template):
            Invoke: _Callable[[Windows.Foundation.IAsyncOperation[_TResult],
                               _enum.Windows.Foundation.AsyncStatus],
                              _type.HRESULT]

        class IAsyncOperationCompletedHandler(_IAsyncOperationCompletedHandler, _Generic[_TResult], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncOperationCompletedHandler_impl(_IAsyncOperationCompletedHandler, _Generic[_TResult], IUnknown_impl):
            pass

        class IAsyncOperationWithProgress(_Template, _Generic[_TResult, _TProgress], IInspectable):
            put_Progress: _Callable[[Windows.Foundation.IAsyncOperationProgressHandler_impl[_TResult, _TProgress]],
                                    _type.HRESULT]
            get_Progress: _Callable[[_Pointer[Windows.Foundation.IAsyncOperationProgressHandler[_TResult, _TProgress]]],
                                    _type.HRESULT]
            put_Completed: _Callable[[Windows.Foundation.IAsyncOperationWithProgressCompletedHandler_impl[_TResult, _TProgress]],
                                     _type.HRESULT]
            get_Completed: _Callable[[_Pointer[Windows.Foundation.IAsyncOperationWithProgressCompletedHandler[_TResult, _TProgress]]],
                                     _type.HRESULT]
            GetResults: _Callable[[_Pointer[_TResult]],
                                  _type.HRESULT]

        class IAsyncActionWithProgress(_Template, _Generic[_TProgress], IInspectable):
            put_Progress: _Callable[[Windows.Foundation.IAsyncActionProgressHandler_impl[_TProgress]],
                                    _type.HRESULT]
            get_Progress: _Callable[[_Pointer[Windows.Foundation.IAsyncActionProgressHandler[_TProgress]]],
                                    _type.HRESULT]
            put_Completed: _Callable[[Windows.Foundation.IAsyncActionWithProgressCompletedHandler[_TProgress]],
                                     _type.HRESULT]
            get_Completed: _Callable[[_Pointer[Windows.Foundation.IAsyncActionWithProgressCompletedHandler_impl[_TProgress]]],
                                     _type.HRESULT]
            GetResults: _Callable[[],
                                  _type.HRESULT]

        class IAsyncOperation(_Template, _Generic[_TResult], IInspectable):
            put_Completed: _Callable[[Windows.Foundation.IAsyncOperationCompletedHandler_impl[_TResult]],
                                     _type.HRESULT]
            get_Completed: _Callable[[_Pointer[Windows.Foundation.IAsyncOperationCompletedHandler[_TResult]]],
                                     _type.HRESULT]
            GetResults: _Callable[[_Pointer[_TResult]],
                                  _type.HRESULT]

        class _IAsyncActionProgressHandler(_Template):
            Invoke: _Callable[[Windows.Foundation.IAsyncActionWithProgress[_TProgress],
                               _TResult],
                              _type.HRESULT]

        class IAsyncActionProgressHandler(_IAsyncActionProgressHandler, _Generic[_TProgress], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncActionProgressHandler_impl(_IAsyncActionProgressHandler, _Generic[_TProgress], IUnknown_impl):
            pass

        class _IAsyncActionWithProgressCompletedHandler(_Template):
            Invoke: _Callable[[Windows.Foundation.IAsyncActionWithProgress[_TProgress],
                               _enum.Windows.Foundation.AsyncStatus],
                              _type.HRESULT]

        class IAsyncActionWithProgressCompletedHandler(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncActionWithProgressCompletedHandler_impl(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], IUnknown_impl):
            pass

        class _IEventHandler(_Template):
            Invoke: _Callable[[IInspectable,
                               _T],
                              _type.HRESULT]

        class IEventHandler(_IEventHandler, _Generic[_T], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IEventHandler_impl(_IEventHandler, _Generic[_T], IUnknown_impl):
            pass

        class _ITypedEventHandler(_Template):
            Invoke: _Callable[[_TSender,
                               _TArgs],
                              _type.HRESULT]

        class ITypedEventHandler(_ITypedEventHandler, _Generic[_TSender, _TArgs], IUnknown):
            pass

        # noinspection PyPep8Naming
        class ITypedEventHandler_impl(_ITypedEventHandler, _Generic[_TSender, _TArgs], IUnknown_impl):
            pass

        class Collections:
            class IPropertySet(IInspectable):
                pass

            class IIterator(_Template, _Generic[_T], IInspectable):
                get_Current: _Callable[[_Pointer[_T]],
                                       _type.HRESULT]
                get_HasCurrent: _Callable[[_Pointer[_type.boolean]],
                                          _type.HRESULT]
                MoveNext: _Callable[[_Pointer[_type.boolean]],
                                    _type.HRESULT]
                GetMany: _Callable[[_type.c_uint,
                                    _Pointer[_T],
                                    _Pointer[_type.c_uint]],
                                   _type.HRESULT]

            class IVectorView(_Template, _Generic[_T], IInspectable):
                GetAt: _Callable[[_type.c_uint,
                                  _Pointer[_T]],
                                 _type.HRESULT]
                get_Size: _Callable[[_Pointer[_type.c_uint]],
                                    _type.HRESULT]
                IndexOf: _Callable[[_Optional[_T],
                                    _Pointer[_type.c_uint],
                                    _Pointer[_type.boolean]],
                                   _type.HRESULT]
                GetMany: _Callable[[_type.c_uint,
                                    _type.c_uint,
                                    _Pointer[_T],
                                    _Pointer[_type.c_uint]],
                                   _type.HRESULT]

            class IVector(_Template, _Generic[_T], IInspectable):
                GetAt: _Callable[[_Optional[_type.c_uint],
                                  _Pointer[_T]],
                                 _type.HRESULT]
                get_Size: _Callable[[_Pointer[_type.c_uint]],
                                    _type.HRESULT]
                GetView: _Callable[[_Pointer[Windows.Foundation.Collections.IVectorView[_T]]],
                                   _type.HRESULT]
                IndexOf: _Callable[[_Optional[_T],
                                    _Pointer[_type.c_uint],
                                    _Pointer[_type.boolean]],
                                   _type.HRESULT]
                SetAt: _Callable[[_type.c_uint,
                                  _T],
                                 _type.HRESULT]
                InsertAt: _Callable[[_type.c_uint,
                                     _T],
                                    _type.HRESULT]
                RemoveAt: _Callable[[_type.c_uint],
                                    _type.HRESULT]
                Append: _Callable[[_Optional[_T]],
                                  _type.HRESULT]
                RemoveAtEnd: _Callable[[],
                                       _type.HRESULT]
                Clear: _Callable[[],
                                 _type.HRESULT]
                GetMany: _Callable[[_type.c_uint,
                                    _type.c_uint,
                                    _Pointer[_T],
                                    _Pointer[_type.c_uint]],
                                   _type.HRESULT]
                ReplaceAll: _Callable[[_type.c_uint,
                                       _Pointer[_T]],
                                      _type.HRESULT]

            class IMapView(_Template, _Generic[_K, _V], IInspectable):
                Lookup: _Callable[[_Optional[_K],
                                   _Pointer[_V]],
                                  _type.HRESULT]
                get_Size: _Callable[[_Pointer[_type.c_uint]],
                                    _type.HRESULT]
                HasKey: _Callable[[_Optional[_K],
                                   _Pointer[_type.boolean]],
                                  _type.HRESULT]
                Split: _Callable[[_Pointer[Windows.Foundation.Collections.IMapView[_K, _V]],
                                  _Pointer[Windows.Foundation.Collections.IMapView[_K, _V]]],
                                 _type.HRESULT]

            class IMap(_Template, _Generic[_K, _V], IInspectable):
                Lookup: _Callable[[_Optional[_K],
                                   _Pointer[_V]],
                                  _type.HRESULT]
                get_Size: _Callable[[_Pointer[_type.c_uint]],
                                    _type.HRESULT]
                HasKey: _Callable[[_Optional[_K],
                                   _Pointer[_type.boolean]],
                                  _type.HRESULT]
                GetView: _Callable[[_Pointer[Windows.Foundation.Collections.IMapView[_K, _V]]],
                                   _type.HRESULT]
                Insert: _Callable[[_Optional[_K],
                                   _Optional[_V],
                                   _Pointer[_type.boolean]],
                                  _type.HRESULT]
                Remove: _Callable[[_Optional[_K]],
                                  _type.HRESULT]
                Clear: _Callable[[],
                                 _type.HRESULT]

    class Storage:
        class _IApplicationDataSetVersionHandler:
            Invoke: _Callable[[Windows.Storage.ISetVersionRequest],
                              _type.HRESULT]

        class IApplicationDataSetVersionHandler(_IApplicationDataSetVersionHandler, IUnknown):
            pass

        # noinspection PyPep8Naming
        class IApplicationDataSetVersionHandler_impl(_IApplicationDataSetVersionHandler, IUnknown_impl):
            pass

        class _IStreamedFileDataRequestedHandler:
            Invoke: _Callable[[Windows.Storage.Streams.IOutputStream],
                              _type.HRESULT]

        class IStreamedFileDataRequestedHandler(_IStreamedFileDataRequestedHandler, IUnknown):
            pass

        # noinspection PyPep8Naming
        class IStreamedFileDataRequestedHandler_impl(_IStreamedFileDataRequestedHandler, IUnknown_impl):
            pass

        class IAppDataPaths(IInspectable):
            get_Cookies: _Callable
            get_Desktop: _Callable
            get_Documents: _Callable
            get_Favorites: _Callable
            get_History: _Callable
            get_InternetCache: _Callable
            get_LocalAppData: _Callable
            get_ProgramData: _Callable
            get_RoamingAppData: _Callable

        class IAppDataPathsStatics(IInspectable):
            GetForUser: _Callable
            GetDefault: _Callable

        class IApplicationData(IInspectable):
            get_Version: _Callable
            SetVersionAsync: _Callable
            ClearAllAsync: _Callable
            ClearAsync: _Callable
            get_LocalSettings: _Callable
            get_RoamingSettings: _Callable
            get_LocalFolder: _Callable
            get_RoamingFolder: _Callable
            get_TemporaryFolder: _Callable
            add_DataChanged: _Callable
            remove_DataChanged: _Callable
            SignalDataChanged: _Callable
            get_RoamingStorageQuota: _Callable

        class IApplicationData2(IInspectable):
            get_LocalCacheFolder: _Callable

        class IApplicationData3(IInspectable):
            GetPublisherCacheFolder: _Callable
            ClearPublisherCacheFolderAsync: _Callable
            get_SharedLocalFolder: _Callable

        class IApplicationDataContainer(IInspectable):
            get_Name: _Callable
            get_Locality: _Callable
            get_Values: _Callable
            get_Containers: _Callable
            CreateContainer: _Callable
            DeleteContainer: _Callable

        class IApplicationDataStatics(IInspectable):
            get_Current: _Callable

        class IApplicationDataStatics2(IInspectable):
            GetForUserAsync: _Callable

        class ICachedFileManagerStatics(IInspectable):
            DeferUpdates: _Callable
            CompleteUpdatesAsync: _Callable

        class IDownloadsFolderStatics(IInspectable):
            CreateFileAsync: _Callable
            CreateFolderAsync: _Callable
            CreateFileWithCollisionOptionAsync: _Callable
            CreateFolderWithCollisionOptionAsync: _Callable

        class IDownloadsFolderStatics2(IInspectable):
            CreateFileForUserAsync: _Callable
            CreateFolderForUserAsync: _Callable
            CreateFileForUserWithCollisionOptionAsync: _Callable
            CreateFolderForUserWithCollisionOptionAsync: _Callable

        class IFileIOStatics(IInspectable):
            ReadTextAsync: _Callable
            ReadTextWithEncodingAsync: _Callable
            WriteTextAsync: _Callable
            WriteTextWithEncodingAsync: _Callable
            AppendTextAsync: _Callable
            AppendTextWithEncodingAsync: _Callable
            ReadLinesAsync: _Callable
            ReadLinesWithEncodingAsync: _Callable
            WriteLinesAsync: _Callable
            WriteLinesWithEncodingAsync: _Callable
            AppendLinesAsync: _Callable
            AppendLinesWithEncodingAsync: _Callable
            ReadBufferAsync: _Callable
            WriteBufferAsync: _Callable
            WriteBytesAsync: _Callable

        class IKnownFoldersCameraRollStatics(IInspectable):
            get_CameraRoll: _Callable

        class IKnownFoldersPlaylistsStatics(IInspectable):
            get_Playlists: _Callable

        class IKnownFoldersSavedPicturesStatics(IInspectable):
            get_SavedPictures: _Callable

        class IKnownFoldersStatics(IInspectable):
            get_MusicLibrary: _Callable
            get_PicturesLibrary: _Callable
            get_VideosLibrary: _Callable
            get_DocumentsLibrary: _Callable
            get_HomeGroup: _Callable
            get_RemovableDevices: _Callable
            get_MediaServerDevices: _Callable

        class IKnownFoldersStatics2(IInspectable):
            get_Objects3D: _Callable
            get_AppCaptures: _Callable
            get_RecordedCalls: _Callable

        class IKnownFoldersStatics3(IInspectable):
            GetFolderForUserAsync: _Callable

        class IKnownFoldersStatics4(IInspectable):
            RequestAccessAsync: _Callable
            RequestAccessForUserAsync: _Callable
            GetFolderAsync: _Callable

        class IPathIOStatics(IInspectable):
            ReadTextAsync: _Callable
            ReadTextWithEncodingAsync: _Callable
            WriteTextAsync: _Callable
            WriteTextWithEncodingAsync: _Callable
            AppendTextAsync: _Callable
            AppendTextWithEncodingAsync: _Callable
            ReadLinesAsync: _Callable
            ReadLinesWithEncodingAsync: _Callable
            WriteLinesAsync: _Callable
            WriteLinesWithEncodingAsync: _Callable
            AppendLinesAsync: _Callable
            AppendLinesWithEncodingAsync: _Callable
            ReadBufferAsync: _Callable
            WriteBufferAsync: _Callable
            WriteBytesAsync: _Callable

        class ISetVersionDeferral(IInspectable):
            Complete: _Callable

        class ISetVersionRequest(IInspectable):
            get_CurrentVersion: _Callable
            get_DesiredVersion: _Callable
            GetDeferral: _Callable

        class IStorageFile(IInspectable):
            get_FileType: _Callable[[_Pointer[_type.HSTRING]],
                                    _type.HRESULT]
            get_ContentType: _Callable[[_Pointer[_type.HSTRING]],
                                       _type.HRESULT]
            OpenAsync: _Callable[[_enum.Windows.Storage.FileAccessMode,
                                  _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStream]]],
                                 _type.HRESULT]
            OpenTransactedWriteAsync: _Callable
            CopyOverloadDefaultNameAndOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                          _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                                         _type.HRESULT]
            CopyOverloadDefaultOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                   _type.HSTRING,
                                                   _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                                  _type.HRESULT]
            CopyOverload: _Callable[[Windows.Storage.IStorageFolder,
                                     _type.HSTRING,
                                     _enum.Windows.Storage.NameCollisionOption,
                                     _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                    _type.HRESULT]
            CopyAndReplaceAsync: _Callable[[Windows.Storage.IStorageFile,
                                            _Pointer[Windows.Foundation.IAsyncAction]],
                                           _type.HRESULT]
            MoveOverloadDefaultNameAndOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                          _Pointer[Windows.Foundation.IAsyncAction]],
                                                         _type.HRESULT]
            MoveOverloadDefaultOptions: _Callable[[Windows.Storage.IStorageFolder,
                                                   _type.HSTRING,
                                                   _Pointer[Windows.Foundation.IAsyncAction]],
                                                  _type.HRESULT]
            MoveOverload: _Callable[[Windows.Storage.IStorageFolder,
                                     _type.HSTRING,
                                     _enum.Windows.Storage.NameCollisionOption,
                                     _Pointer[Windows.Foundation.IAsyncAction]],
                                    _type.HRESULT]
            MoveAndReplaceAsync: _Callable[[Windows.Storage.IStorageFile,
                                            _Pointer[Windows.Foundation.IAsyncAction]],
                                           _type.HRESULT]

        class IStorageFile2(IInspectable):
            OpenWithOptionsAsync: _Callable
            OpenTransactedWriteWithOptionsAsync: _Callable

        class IStorageFilePropertiesWithAvailability(IInspectable):
            get_IsAvailable: _Callable

        class IStorageFileStatics(IInspectable):
            GetFileFromPathAsync: _Callable[[_type.HSTRING,
                                             _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                            _type.HRESULT]
            GetFileFromApplicationUriAsync: _Callable
            CreateStreamedFileAsync: _Callable
            ReplaceWithStreamedFileAsync: _Callable
            CreateStreamedFileFromUriAsync: _Callable
            ReplaceWithStreamedFileFromUriAsync: _Callable

        class IStorageFileStatics2(IInspectable):
            GetFileFromPathForUserAsync: _Callable

        class IStorageFolder(IInspectable):
            CreateFileAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                              _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                                             _type.HSTRING]
            CreateFileAsync: _Callable[[_type.HSTRING,
                                        _enum.Windows.Storage.CreationCollisionOption,
                                        _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                       _type.HRESULT]
            CreateFolderAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                                _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFolder]]],
                                                               _type.HSTRING]
            CreateFolderAsync: _Callable[[_type.HSTRING,
                                          _enum.Windows.Storage.CreationCollisionOption,
                                          _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFolder]]],
                                         _type.HRESULT]
            GetFileAsync: _Callable[[_type.HSTRING,
                                     _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                    _type.HSTRING]
            GetFolderAsync: _Callable[[_type.HSTRING,
                                       _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFolder]]],
                                      _type.HSTRING]
            GetItemAsync: _Callable[[_type.HSTRING,
                                     _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageItem]]],
                                    _type.HSTRING]
            GetFilesAsyncOverloadDefaultOptionsStartAndCount: _Callable
            GetFoldersAsyncOverloadDefaultOptionsStartAndCount: _Callable
            GetItemsAsyncOverloadDefaultStartAndCount: _Callable

        class IStorageFolder2(IInspectable):
            TryGetItemAsync: _Callable

        class IStorageFolder3(IInspectable):
            TryGetChangeTracker: _Callable

        class IStorageFolderStatics(IInspectable):
            GetFolderFromPathAsync: _Callable[[_type.HSTRING,
                                               _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFolder]]],
                                              _type.HRESULT]

        class IStorageFolderStatics2(IInspectable):
            GetFolderFromPathForUserAsync: _Callable

        class IStorageItem(IInspectable):
            RenameAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                          _Pointer[Windows.Foundation.IAsyncAction]],
                                                         _type.HRESULT]
            RenameAsync: _Callable[[_type.HSTRING,
                                    _enum.Windows.Storage.NameCollisionOption,
                                    _Pointer[Windows.Foundation.IAsyncAction]],
                                   _type.HRESULT]
            DeleteAsyncOverloadDefaultOptions: _Callable[[_Pointer[Windows.Foundation.IAsyncAction]],
                                                         _type.HRESULT]
            DeleteAsync: _Callable[[_enum.Windows.Storage.StorageDeleteOption,
                                    _Pointer[Windows.Foundation.IAsyncAction]],
                                   _type.HRESULT]
            GetBasicPropertiesAsync: _Callable
            get_Name: _Callable[[_Pointer[_type.HSTRING]],
                                _type.HRESULT]
            get_Path: _Callable[[_Pointer[_type.HSTRING]],
                                _type.HRESULT]
            get_Attributes: _Callable
            get_DateCreated: _Callable
            IsOfType: _Callable

        class IStorageItem2(IInspectable):
            GetParentAsync: _Callable
            IsEqual: _Callable

        class IStorageItemProperties(IInspectable):
            GetThumbnailAsyncOverloadDefaultSizeDefaultOptions: _Callable
            GetThumbnailAsyncOverloadDefaultOptions: _Callable
            GetThumbnailAsync: _Callable
            get_DisplayName: _Callable
            get_DisplayType: _Callable
            get_FolderRelativeId: _Callable
            get_Properties: _Callable

        class IStorageItemProperties2(IInspectable):
            GetScaledImageAsThumbnailAsyncOverloadDefaultSizeDefaultOptions: _Callable
            GetScaledImageAsThumbnailAsyncOverloadDefaultOptions: _Callable
            GetScaledImageAsThumbnailAsync: _Callable

        class IStorageItemPropertiesWithProvider(IInspectable):
            get_Provider: _Callable

        class IStorageLibrary(IInspectable):
            RequestAddFolderAsync: _Callable
            RequestRemoveFolderAsync: _Callable
            get_Folders: _Callable
            get_SaveFolder: _Callable
            add_DefinitionChanged: _Callable
            remove_DefinitionChanged: _Callable

        class IStorageLibrary2(IInspectable):
            get_ChangeTracker: _Callable

        class IStorageLibrary3(IInspectable):
            AreFolderSuggestionsAvailableAsync: _Callable

        class IStorageLibraryChange(IInspectable):
            get_ChangeType: _Callable
            get_Path: _Callable
            get_PreviousPath: _Callable
            IsOfType: _Callable
            GetStorageItemAsync: _Callable

        class IStorageLibraryChangeReader(IInspectable):
            ReadBatchAsync: _Callable
            AcceptChangesAsync: _Callable

        class IStorageLibraryChangeReader2(IInspectable):
            GetLastChangeId: _Callable

        class IStorageLibraryChangeTracker(IInspectable):
            GetChangeReader: _Callable
            Enable: _Callable
            Reset: _Callable

        class IStorageLibraryChangeTracker2(IInspectable):
            EnableWithOptions: _Callable
            Disable: _Callable

        class IStorageLibraryChangeTrackerOptions(IInspectable):
            get_TrackChangeDetails: _Callable
            put_TrackChangeDetails: _Callable

        class IStorageLibraryLastChangeId(IInspectable):
            pass

        class IStorageLibraryLastChangeIdStatics(IInspectable):
            get_Unknown: _Callable

        class IStorageLibraryStatics(IInspectable):
            GetLibraryAsync: _Callable

        class IStorageLibraryStatics2(IInspectable):
            GetLibraryForUserAsync: _Callable

        class IStorageProvider(IInspectable):
            get_Id: _Callable
            get_DisplayName: _Callable

        class IStorageProvider2(IInspectable):
            IsPropertySupportedForPartialFileAsync: _Callable

        class IStorageStreamTransaction(IInspectable):
            get_Stream: _Callable
            CommitAsync: _Callable

        class IStreamedFileDataRequest(IInspectable):
            FailAndClose: _Callable

        class ISystemAudioProperties(IInspectable):
            get_EncodingBitrate: _Callable

        class ISystemDataPaths(IInspectable):
            get_Fonts: _Callable
            get_ProgramData: _Callable
            get_Public: _Callable
            get_PublicDesktop: _Callable
            get_PublicDocuments: _Callable
            get_PublicDownloads: _Callable
            get_PublicMusic: _Callable
            get_PublicPictures: _Callable
            get_PublicVideos: _Callable
            get_System: _Callable
            get_SystemHost: _Callable
            get_SystemX86: _Callable
            get_SystemX64: _Callable
            get_SystemArm: _Callable
            get_UserProfiles: _Callable
            get_Windows: _Callable

        class ISystemDataPathsStatics(IInspectable):
            GetDefault: _Callable

        class ISystemGPSProperties(IInspectable):
            get_LatitudeDecimal: _Callable
            get_LongitudeDecimal: _Callable

        class ISystemImageProperties(IInspectable):
            get_HorizontalSize: _Callable
            get_VerticalSize: _Callable

        class ISystemMediaProperties(IInspectable):
            get_Duration: _Callable
            get_Producer: _Callable
            get_Publisher: _Callable
            get_SubTitle: _Callable
            get_Writer: _Callable
            get_Year: _Callable

        class ISystemMusicProperties(IInspectable):
            get_AlbumArtist: _Callable
            get_AlbumTitle: _Callable
            get_Artist: _Callable
            get_Composer: _Callable
            get_Conductor: _Callable
            get_DisplayArtist: _Callable
            get_Genre: _Callable
            get_TrackNumber: _Callable

        class ISystemPhotoProperties(IInspectable):
            get_CameraManufacturer: _Callable
            get_CameraModel: _Callable
            get_DateTaken: _Callable
            get_Orientation: _Callable
            get_PeopleNames: _Callable

        class ISystemProperties(IInspectable):
            get_Author: _Callable
            get_Comment: _Callable
            get_ItemNameDisplay: _Callable
            get_Keywords: _Callable
            get_Rating: _Callable
            get_Title: _Callable
            get_Audio: _Callable
            get_GPS: _Callable
            get_Media: _Callable
            get_Music: _Callable
            get_Photo: _Callable
            get_Video: _Callable
            get_Image: _Callable

        class ISystemVideoProperties(IInspectable):
            get_Director: _Callable
            get_FrameHeight: _Callable
            get_FrameWidth: _Callable
            get_Orientation: _Callable
            get_TotalBitrate: _Callable

        class IUserDataPaths(IInspectable):
            get_CameraRoll: _Callable
            get_Cookies: _Callable
            get_Desktop: _Callable
            get_Documents: _Callable
            get_Downloads: _Callable
            get_Favorites: _Callable
            get_History: _Callable
            get_InternetCache: _Callable
            get_LocalAppData: _Callable
            get_LocalAppDataLow: _Callable
            get_Music: _Callable
            get_Pictures: _Callable
            get_Profile: _Callable
            get_Recent: _Callable
            get_RoamingAppData: _Callable
            get_SavedPictures: _Callable
            get_Screenshots: _Callable
            get_Templates: _Callable
            get_Videos: _Callable

        class IUserDataPathsStatics(IInspectable):
            GetForUser: _Callable
            GetDefault: _Callable

        class Streams:
            class IBuffer(IInspectable):
                get_Capacity: _Callable[[_Pointer[_type.UINT32]],
                                        _type.HRESULT]
                get_Length: _Callable[[_Pointer[_type.UINT32]],
                                      _type.HRESULT]
                put_Length: _Callable[[_type.UINT32],
                                      _type.HRESULT]

            class IBufferFactory(IInspectable):
                Create: _Callable

            class IBufferStatics(IInspectable):
                CreateCopyFromMemoryBuffer: _Callable
                CreateMemoryBufferOverIBuffer: _Callable

            class IContentTypeProvider(IInspectable):
                get_ContentType: _Callable

            class IDataReader(IInspectable):
                get_UnconsumedBufferLength: _Callable
                get_UnicodeEncoding: _Callable
                put_UnicodeEncoding: _Callable
                get_ByteOrder: _Callable
                put_ByteOrder: _Callable
                get_InputStreamOptions: _Callable
                put_InputStreamOptions: _Callable
                ReadByte: _Callable
                ReadBytes: _Callable
                ReadBuffer: _Callable
                ReadBoolean: _Callable
                ReadGuid: _Callable
                ReadInt16: _Callable
                ReadInt32: _Callable
                ReadInt64: _Callable
                ReadUInt16: _Callable
                ReadUInt32: _Callable
                ReadUInt64: _Callable
                ReadSingle: _Callable
                ReadDouble: _Callable
                ReadString: _Callable
                ReadDateTime: _Callable
                ReadTimeSpan: _Callable
                LoadAsync: _Callable
                DetachBuffer: _Callable
                DetachStream: _Callable

            class IDataReaderFactory(IInspectable):
                CreateDataReader: _Callable

            class IDataReaderStatics(IInspectable):
                FromBuffer: _Callable

            class IDataWriter(IInspectable):
                get_UnstoredBufferLength: _Callable
                get_UnicodeEncoding: _Callable
                put_UnicodeEncoding: _Callable
                get_ByteOrder: _Callable
                put_ByteOrder: _Callable
                WriteByte: _Callable
                WriteBytes: _Callable
                WriteBuffer: _Callable
                WriteBufferRange: _Callable
                WriteBoolean: _Callable
                WriteGuid: _Callable
                WriteInt16: _Callable
                WriteInt32: _Callable
                WriteInt64: _Callable
                WriteUInt16: _Callable
                WriteUInt32: _Callable
                WriteUInt64: _Callable
                WriteSingle: _Callable
                WriteDouble: _Callable
                WriteDateTime: _Callable
                WriteTimeSpan: _Callable
                WriteString: _Callable
                MeasureString: _Callable
                StoreAsync: _Callable
                FlushAsync: _Callable
                DetachBuffer: _Callable
                DetachStream: _Callable

            class IDataWriterFactory(IInspectable):
                CreateDataWriter: _Callable

            class IFileRandomAccessStreamStatics(IInspectable):
                OpenAsync: _Callable
                OpenWithOptionsAsync: _Callable
                OpenTransactedWriteAsync: _Callable
                OpenTransactedWriteWithOptionsAsync: _Callable
                OpenForUserAsync: _Callable
                OpenForUserWithOptionsAsync: _Callable
                OpenTransactedWriteForUserAsync: _Callable
                OpenTransactedWriteForUserWithOptionsAsync: _Callable

            class IInputStream(IInspectable):
                ReadAsync: _Callable[[Windows.Storage.Streams.IBuffer,
                                      _type.UINT32,
                                      _enum.Windows.Storage.Streams.InputStreamOptions,
                                      _Pointer[Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, _type.UINT32]]],
                                     _type.HRESULT]

            class IInputStreamReference(IInspectable):
                OpenSequentialReadAsync: _Callable

            class IOutputStream(IInspectable):
                WriteAsync: _Callable
                FlushAsync: _Callable

            class IPropertySetSerializer(IInspectable):
                Serialize: _Callable
                Deserialize: _Callable

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

            class IRandomAccessStreamReference(IInspectable):
                OpenReadAsync: _Callable

            class IRandomAccessStreamReferenceStatics(IInspectable):
                CreateFromFile: _Callable
                CreateFromUri: _Callable
                CreateFromStream: _Callable

            class IRandomAccessStreamStatics(IInspectable):
                CopyAsync: _Callable[[Windows.Storage.Streams.IInputStream,
                                      Windows.Storage.Streams.IOutputStream,
                                      _Pointer[Windows.Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],
                                     _type.HRESULT]
                CopySizeAsync: _Callable[[Windows.Storage.Streams.IInputStream,
                                          Windows.Storage.Streams.IOutputStream,
                                          _type.UINT64,
                                          _Pointer[Windows.Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],
                                         _type.HRESULT]
                CopyAndCloseAsync: _Callable[[Windows.Storage.Streams.IInputStream,
                                              Windows.Storage.Streams.IOutputStream,
                                              _Pointer[Windows.Foundation.IAsyncOperationWithProgress[_type.UINT64, _type.UINT64]]],
                                             _type.HRESULT]

            class IRandomAccessStreamWithContentType(IInspectable):
                pass

    class System:
        class _IDispatcherQueueHandler:
            Invoke: _Callable[[],
                              _type.HRESULT]

        class IDispatcherQueueHandler(_IDispatcherQueueHandler, IUnknown):
            pass

        # noinspection PyPep8Naming
        class IDispatcherQueueHandler_impl(_IDispatcherQueueHandler, IUnknown_impl):
            pass

        class IAppActivationResult(IInspectable):
            get_ExtendedError: _Callable
            get_AppResourceGroupInfo: _Callable

        class IAppDiagnosticInfo(IInspectable):
            get_AppInfo: _Callable

        class IAppDiagnosticInfo2(IInspectable):
            GetResourceGroups: _Callable
            CreateResourceGroupWatcher: _Callable

        class IAppDiagnosticInfo3(IInspectable):
            LaunchAsync: _Callable

        class IAppDiagnosticInfoStatics(IInspectable):
            RequestInfoAsync: _Callable

        class IAppDiagnosticInfoStatics2(IInspectable):
            CreateWatcher: _Callable
            RequestAccessAsync: _Callable
            RequestInfoForPackageAsync: _Callable
            RequestInfoForAppAsync: _Callable
            RequestInfoForAppUserModelId: _Callable

        class IAppDiagnosticInfoWatcher(IInspectable):
            add_Added: _Callable
            remove_Added: _Callable
            add_Removed: _Callable
            remove_Removed: _Callable
            add_EnumerationCompleted: _Callable
            remove_EnumerationCompleted: _Callable
            add_Stopped: _Callable
            remove_Stopped: _Callable
            get_Status: _Callable
            Start: _Callable
            Stop: _Callable

        class IAppDiagnosticInfoWatcherEventArgs(IInspectable):
            get_AppDiagnosticInfo: _Callable

        class IAppExecutionStateChangeResult(IInspectable):
            get_ExtendedError: _Callable

        class IAppMemoryReport(IInspectable):
            get_PrivateCommitUsage: _Callable
            get_PeakPrivateCommitUsage: _Callable
            get_TotalCommitUsage: _Callable
            get_TotalCommitLimit: _Callable

        class IAppMemoryReport2(IInspectable):
            get_ExpectedTotalCommitLimit: _Callable

        class IAppMemoryUsageLimitChangingEventArgs(IInspectable):
            get_OldLimit: _Callable
            get_NewLimit: _Callable

        class IAppResourceGroupBackgroundTaskReport(IInspectable):
            get_TaskId: _Callable
            get_Name: _Callable
            get_Trigger: _Callable
            get_EntryPoint: _Callable

        class IAppResourceGroupInfo(IInspectable):
            get_InstanceId: _Callable
            get_IsShared: _Callable
            GetBackgroundTaskReports: _Callable
            GetMemoryReport: _Callable
            GetProcessDiagnosticInfos: _Callable
            GetStateReport: _Callable

        class IAppResourceGroupInfo2(IInspectable):
            StartSuspendAsync: _Callable
            StartResumeAsync: _Callable
            StartTerminateAsync: _Callable

        class IAppResourceGroupInfoWatcher(IInspectable):
            add_Added: _Callable
            remove_Added: _Callable
            add_Removed: _Callable
            remove_Removed: _Callable
            add_EnumerationCompleted: _Callable
            remove_EnumerationCompleted: _Callable
            add_Stopped: _Callable
            remove_Stopped: _Callable
            add_ExecutionStateChanged: _Callable
            remove_ExecutionStateChanged: _Callable
            get_Status: _Callable
            Start: _Callable
            Stop: _Callable

        class IAppResourceGroupInfoWatcherEventArgs(IInspectable):
            get_AppDiagnosticInfos: _Callable
            get_AppResourceGroupInfo: _Callable

        class IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs(IInspectable):
            get_AppDiagnosticInfos: _Callable
            get_AppResourceGroupInfo: _Callable

        class IAppResourceGroupMemoryReport(IInspectable):
            get_CommitUsageLimit: _Callable
            get_CommitUsageLevel: _Callable
            get_PrivateCommitUsage: _Callable
            get_TotalCommitUsage: _Callable

        class IAppResourceGroupStateReport(IInspectable):
            get_ExecutionState: _Callable
            get_EnergyQuotaState: _Callable

        class IAppUriHandlerHost(IInspectable):
            get_Name: _Callable
            put_Name: _Callable

        class IAppUriHandlerHost2(IInspectable):
            get_IsEnabled: _Callable
            put_IsEnabled: _Callable

        class IAppUriHandlerHostFactory(IInspectable):
            CreateInstance: _Callable

        class IAppUriHandlerRegistration(IInspectable):
            get_Name: _Callable
            get_User: _Callable
            GetAppAddedHostsAsync: _Callable
            SetAppAddedHostsAsync: _Callable

        class IAppUriHandlerRegistration2(IInspectable):
            GetAllHosts: _Callable
            UpdateHosts: _Callable
            get_PackageFamilyName: _Callable

        class IAppUriHandlerRegistrationManager(IInspectable):
            get_User: _Callable
            TryGetRegistration: _Callable

        class IAppUriHandlerRegistrationManager2(IInspectable):
            get_PackageFamilyName: _Callable

        class IAppUriHandlerRegistrationManagerStatics(IInspectable):
            GetDefault: _Callable
            GetForUser: _Callable

        class IAppUriHandlerRegistrationManagerStatics2(IInspectable):
            GetForPackage: _Callable
            GetForPackageForUser: _Callable

        class IDateTimeSettingsStatics(IInspectable):
            SetSystemDateTime: _Callable

        class IDispatcherQueue(IInspectable):
            CreateTimer: _Callable
            TryEnqueue: _Callable
            TryEnqueueWithPriority: _Callable
            add_ShutdownStarting: _Callable
            remove_ShutdownStarting: _Callable
            add_ShutdownCompleted: _Callable
            remove_ShutdownCompleted: _Callable

        class IDispatcherQueue2(IInspectable):
            get_HasThreadAccess: _Callable

        class IDispatcherQueueController(IInspectable):
            get_DispatcherQueue: _Callable
            ShutdownQueueAsync: _Callable

        class IDispatcherQueueControllerStatics(IInspectable):
            CreateOnDedicatedThread: _Callable

        class IDispatcherQueueShutdownStartingEventArgs(IInspectable):
            GetDeferral: _Callable

        class IDispatcherQueueStatics(IInspectable):
            GetForCurrentThread: _Callable

        class IDispatcherQueueTimer(IInspectable):
            get_Interval: _Callable
            put_Interval: _Callable
            get_IsRunning: _Callable
            get_IsRepeating: _Callable
            put_IsRepeating: _Callable
            Start: _Callable
            Stop: _Callable
            add_Tick: _Callable
            remove_Tick: _Callable

        class IFolderLauncherOptions(IInspectable):
            get_ItemsToSelect: _Callable

        class IKnownUserPropertiesStatics(IInspectable):
            get_DisplayName: _Callable
            get_FirstName: _Callable
            get_LastName: _Callable
            get_ProviderName: _Callable
            get_AccountName: _Callable
            get_GuestHost: _Callable
            get_PrincipalName: _Callable
            get_DomainName: _Callable
            get_SessionInitiationProtocolUri: _Callable

        class IKnownUserPropertiesStatics2(IInspectable):
            get_AgeEnforcementRegion: _Callable

        class ILaunchUriResult(IInspectable):
            get_Status: _Callable
            get_Result: _Callable

        class ILauncherOptions(IInspectable):
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

        class ILauncherOptions2(IInspectable):
            get_TargetApplicationPackageFamilyName: _Callable
            put_TargetApplicationPackageFamilyName: _Callable
            get_NeighboringFilesQuery: _Callable
            put_NeighboringFilesQuery: _Callable

        class ILauncherOptions3(IInspectable):
            get_IgnoreAppUriHandlers: _Callable
            put_IgnoreAppUriHandlers: _Callable

        class ILauncherOptions4(IInspectable):
            get_LimitPickerToCurrentAppAndAppUriHandlers: _Callable
            put_LimitPickerToCurrentAppAndAppUriHandlers: _Callable

        class ILauncherStatics(IInspectable):
            LaunchFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                        _Pointer[Windows.Foundation.IAsyncOperation[_type.c_bool]]],
                                       _type.HRESULT]
            LaunchFileWithOptionsAsync: _Callable[[Windows.Storage.IStorageFile,
                                                   Windows.System.ILauncherOptions,
                                                   _Pointer[Windows.Foundation.IAsyncOperation[_type.c_bool]]],
                                                  _type.HRESULT]
            LaunchUriAsync: _Callable[[Windows.Foundation.IUriRuntimeClass,
                                       _Pointer[Windows.Foundation.IAsyncOperation[_type.c_bool]]],
                                      _type.HRESULT]
            LaunchUriWithOptionsAsync: _Callable[[Windows.Foundation.IUriRuntimeClass,
                                                  Windows.System.ILauncherOptions,
                                                  _Pointer[Windows.Foundation.IAsyncOperation[_type.c_bool]]],
                                                 _type.HRESULT]

        class ILauncherStatics2(IInspectable):
            LaunchUriForResultsAsync: _Callable
            LaunchUriForResultsWithDataAsync: _Callable
            LaunchUriWithDataAsync: _Callable
            QueryUriSupportAsync: _Callable
            QueryUriSupportWithPackageFamilyNameAsync: _Callable
            QueryFileSupportAsync: _Callable
            QueryFileSupportWithPackageFamilyNameAsync: _Callable
            FindUriSchemeHandlersAsync: _Callable
            FindUriSchemeHandlersWithLaunchUriTypeAsync: _Callable
            FindFileHandlersAsync: _Callable

        class ILauncherStatics3(IInspectable):
            LaunchFolderAsync: _Callable
            LaunchFolderWithOptionsAsync: _Callable

        class ILauncherStatics4(IInspectable):
            QueryAppUriSupportAsync: _Callable
            QueryAppUriSupportWithPackageFamilyNameAsync: _Callable
            FindAppUriHandlersAsync: _Callable
            LaunchUriForUserAsync: _Callable
            LaunchUriWithOptionsForUserAsync: _Callable
            LaunchUriWithDataForUserAsync: _Callable
            LaunchUriForResultsForUserAsync: _Callable
            LaunchUriForResultsWithDataForUserAsync: _Callable

        class ILauncherStatics5(IInspectable):
            LaunchFolderPathAsync: _Callable
            LaunchFolderPathWithOptionsAsync: _Callable
            LaunchFolderPathForUserAsync: _Callable
            LaunchFolderPathWithOptionsForUserAsync: _Callable

        class ILauncherUIOptions(IInspectable):
            get_InvocationPoint: _Callable
            put_InvocationPoint: _Callable
            get_SelectionRect: _Callable
            put_SelectionRect: _Callable
            get_PreferredPlacement: _Callable
            put_PreferredPlacement: _Callable

        class ILauncherViewOptions(IInspectable):
            get_DesiredRemainingView: _Callable
            put_DesiredRemainingView: _Callable

        class IMemoryManagerStatics(IInspectable):
            get_AppMemoryUsage: _Callable
            get_AppMemoryUsageLimit: _Callable
            get_AppMemoryUsageLevel: _Callable
            add_AppMemoryUsageIncreased: _Callable
            remove_AppMemoryUsageIncreased: _Callable
            add_AppMemoryUsageDecreased: _Callable
            remove_AppMemoryUsageDecreased: _Callable
            add_AppMemoryUsageLimitChanging: _Callable
            remove_AppMemoryUsageLimitChanging: _Callable

        class IMemoryManagerStatics2(IInspectable):
            GetAppMemoryReport: _Callable
            GetProcessMemoryReport: _Callable

        class IMemoryManagerStatics3(IInspectable):
            TrySetAppMemoryUsageLimit: _Callable

        class IMemoryManagerStatics4(IInspectable):
            get_ExpectedAppMemoryUsageLimit: _Callable

        class IProcessLauncherOptions(IInspectable):
            get_StandardInput: _Callable
            put_StandardInput: _Callable
            get_StandardOutput: _Callable
            put_StandardOutput: _Callable
            get_StandardError: _Callable
            put_StandardError: _Callable
            get_WorkingDirectory: _Callable
            put_WorkingDirectory: _Callable

        class IProcessLauncherResult(IInspectable):
            get_ExitCode: _Callable

        class IProcessLauncherStatics(IInspectable):
            RunToCompletionAsync: _Callable
            RunToCompletionAsyncWithOptions: _Callable

        class IProcessMemoryReport(IInspectable):
            get_PrivateWorkingSetUsage: _Callable
            get_TotalWorkingSetUsage: _Callable

        class IProtocolForResultsOperation(IInspectable):
            ReportCompleted: _Callable

        class IRemoteLauncherOptions(IInspectable):
            get_FallbackUri: _Callable
            put_FallbackUri: _Callable
            get_PreferredAppIds: _Callable

        class IRemoteLauncherStatics(IInspectable):
            LaunchUriAsync: _Callable
            LaunchUriWithOptionsAsync: _Callable
            LaunchUriWithDataAsync: _Callable

        class IShutdownManagerStatics(IInspectable):
            BeginShutdown: _Callable
            CancelShutdown: _Callable

        class IShutdownManagerStatics2(IInspectable):
            IsPowerStateSupported: _Callable
            EnterPowerState: _Callable
            EnterPowerStateWithTimeSpan: _Callable

        class ITimeZoneSettingsStatics(IInspectable):
            get_CurrentTimeZoneDisplayName: _Callable
            get_SupportedTimeZoneDisplayNames: _Callable
            get_CanChangeTimeZone: _Callable
            ChangeTimeZoneByDisplayName: _Callable

        class ITimeZoneSettingsStatics2(IInspectable):
            AutoUpdateTimeZoneAsync: _Callable

        class IUser(IInspectable):
            get_NonRoamableId: _Callable
            get_AuthenticationStatus: _Callable
            get_Type: _Callable
            GetPropertyAsync: _Callable
            GetPropertiesAsync: _Callable
            GetPictureAsync: _Callable

        class IUser2(IInspectable):
            CheckUserAgeConsentGroupAsync: _Callable

        class IUserAuthenticationStatusChangeDeferral(IInspectable):
            Complete: _Callable

        class IUserAuthenticationStatusChangingEventArgs(IInspectable):
            GetDeferral: _Callable
            get_User: _Callable
            get_NewStatus: _Callable
            get_CurrentStatus: _Callable

        class IUserChangedEventArgs(IInspectable):
            get_User: _Callable

        class IUserChangedEventArgs2(IInspectable):
            get_ChangedPropertyKinds: _Callable

        class IUserDeviceAssociationChangedEventArgs(IInspectable):
            get_DeviceId: _Callable
            get_NewUser: _Callable
            get_OldUser: _Callable

        class IUserDeviceAssociationStatics(IInspectable):
            FindUserFromDeviceId: _Callable
            add_UserDeviceAssociationChanged: _Callable
            remove_UserDeviceAssociationChanged: _Callable

        class IUserPicker(IInspectable):
            get_AllowGuestAccounts: _Callable
            put_AllowGuestAccounts: _Callable
            get_SuggestedSelectedUser: _Callable
            put_SuggestedSelectedUser: _Callable
            PickSingleUserAsync: _Callable

        class IUserPickerStatics(IInspectable):
            IsSupported: _Callable

        class IUserStatics(IInspectable):
            CreateWatcher: _Callable
            FindAllAsync: _Callable
            FindAllAsyncByType: _Callable
            FindAllAsyncByTypeAndStatus: _Callable
            GetFromId: _Callable

        class IUserStatics2(IInspectable):
            GetDefault: _Callable

        class IUserWatcher(IInspectable):
            get_Status: _Callable
            Start: _Callable
            Stop: _Callable
            add_Added: _Callable
            remove_Added: _Callable
            add_Removed: _Callable
            remove_Removed: _Callable
            add_Updated: _Callable
            remove_Updated: _Callable
            add_AuthenticationStatusChanged: _Callable
            remove_AuthenticationStatusChanged: _Callable
            add_AuthenticationStatusChanging: _Callable
            remove_AuthenticationStatusChanging: _Callable
            add_EnumerationCompleted: _Callable
            remove_EnumerationCompleted: _Callable
            add_Stopped: _Callable
            remove_Stopped: _Callable

        class UserProfile:
            class IAdvertisingManagerForUser(IInspectable):
                get_AdvertisingId: _Callable
                get_User: _Callable

            class IAdvertisingManagerStatics(IInspectable):
                get_AdvertisingId: _Callable

            class IAdvertisingManagerStatics2(IInspectable):
                GetForUser: _Callable

            class IAssignedAccessSettings(IInspectable):
                get_IsEnabled: _Callable
                get_IsSingleAppKioskMode: _Callable
                get_User: _Callable

            class IAssignedAccessSettingsStatics(IInspectable):
                GetDefault: _Callable
                GetForUser: _Callable

            class IDiagnosticsSettings(IInspectable):
                get_CanUseDiagnosticsToTailorExperiences: _Callable
                get_User: _Callable

            class IDiagnosticsSettingsStatics(IInspectable):
                GetDefault: _Callable
                GetForUser: _Callable

            class IFirstSignInSettings(IInspectable):
                pass

            class IFirstSignInSettingsStatics(IInspectable):
                GetDefault: _Callable

            class IGlobalizationPreferencesForUser(IInspectable):
                get_User: _Callable
                get_Calendars: _Callable
                get_Clocks: _Callable
                get_Currencies: _Callable
                get_Languages: _Callable
                get_HomeGeographicRegion: _Callable
                get_WeekStartsOn: _Callable

            class IGlobalizationPreferencesStatics(IInspectable):
                get_Calendars: _Callable
                get_Clocks: _Callable
                get_Currencies: _Callable
                get_Languages: _Callable
                get_HomeGeographicRegion: _Callable
                get_WeekStartsOn: _Callable

            class IGlobalizationPreferencesStatics2(IInspectable):
                TrySetHomeGeographicRegion: _Callable
                TrySetLanguages: _Callable

            class IGlobalizationPreferencesStatics3(IInspectable):
                GetForUser: _Callable

            class ILockScreenImageFeedStatics(IInspectable):
                RequestSetImageFeedAsync: _Callable
                TryRemoveImageFeed: _Callable

            class ILockScreenStatics(IInspectable):
                get_OriginalImageFile: _Callable[[_Pointer[Windows.Foundation.IUriRuntimeClass]],
                                                 _type.HRESULT]
                GetImageStream: _Callable[[_Pointer[Windows.Storage.Streams.IRandomAccessStream]],
                                          _type.HRESULT]
                SetImageFileAsync: _Callable[[Windows.Storage.IStorageFile,
                                              _Pointer[Windows.Foundation.IAsyncAction]],
                                             _type.HRESULT]
                SetImageStreamAsync: _Callable[[Windows.Storage.Streams.IRandomAccessStream,
                                                _Pointer[Windows.Foundation.IAsyncAction]],
                                               _type.HRESULT]

            class IUserInformationStatics(IInspectable):
                get_AccountPictureChangeEnabled: _Callable
                get_NameAccessAllowed: _Callable
                GetAccountPicture: _Callable
                SetAccountPictureAsync: _Callable
                SetAccountPicturesAsync: _Callable
                SetAccountPictureFromStreamAsync: _Callable
                SetAccountPicturesFromStreamsAsync: _Callable
                add_AccountPictureChanged: _Callable
                remove_AccountPictureChanged: _Callable
                GetDisplayNameAsync: _Callable
                GetFirstNameAsync: _Callable
                GetLastNameAsync: _Callable
                GetPrincipalNameAsync: _Callable
                GetSessionInitiationProtocolUriAsync: _Callable
                GetDomainNameAsync: _Callable

            class IUserProfilePersonalizationSettings(IInspectable):
                TrySetLockScreenImageAsync: _Callable
                TrySetWallpaperImageAsync: _Callable

            class IUserProfilePersonalizationSettingsStatics(IInspectable):
                get_Current: _Callable
                IsSupported: _Callable

    class UI:
        class IColorHelper(IInspectable):
            pass

        class IColorHelperStatics(IInspectable):
            FromArgb: _Callable

        class IColorHelperStatics2(IInspectable):
            ToDisplayName: _Callable

        class IColors(IInspectable):
            pass

        class IColorsStatics(IInspectable):
            get_AliceBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_AntiqueWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                        _type.HRESULT]
            get_Aqua: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_Aquamarine: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_Azure: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_Beige: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_Bisque: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_Black: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_BlanchedAlmond: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                          _type.HRESULT]
            get_Blue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_BlueViolet: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_Brown: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_BurlyWood: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_CadetBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Chartreuse: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_Chocolate: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Coral: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_CornflowerBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                          _type.HRESULT]
            get_Cornsilk: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_Crimson: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_Cyan: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_DarkBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_DarkCyan: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_DarkGoldenrod: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_DarkGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_DarkGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_DarkKhaki: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_DarkMagenta: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_DarkOliveGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                          _type.HRESULT]
            get_DarkOrange: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_DarkOrchid: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_DarkRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_DarkSalmon: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_DarkSeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                        _type.HRESULT]
            get_DarkSlateBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_DarkSlateGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_DarkTurquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_DarkViolet: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_DeepPink: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_DeepSkyBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_DimGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_DodgerBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_Firebrick: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_FloralWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_ForestGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_Fuchsia: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_Gainsboro: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_GhostWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_Gold: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_Goldenrod: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Gray: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_Green: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_GreenYellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_Honeydew: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_HotPink: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_IndianRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Indigo: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_Ivory: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_Khaki: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_Lavender: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_LavenderBlush: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_LawnGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_LemonChiffon: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                        _type.HRESULT]
            get_LightBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_LightCoral: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_LightCyan: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_LightGoldenrodYellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                                _type.HRESULT]
            get_LightGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_LightGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_LightPink: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_LightSalmon: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_LightSeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_LightSkyBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                        _type.HRESULT]
            get_LightSlateGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                          _type.HRESULT]
            get_LightSteelBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                          _type.HRESULT]
            get_LightYellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_Lime: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_LimeGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Linen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_Magenta: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_Maroon: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_MediumAquamarine: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                            _type.HRESULT]
            get_MediumBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_MediumOrchid: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                        _type.HRESULT]
            get_MediumPurple: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                        _type.HRESULT]
            get_MediumSeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                          _type.HRESULT]
            get_MediumSlateBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                           _type.HRESULT]
            get_MediumSpringGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                             _type.HRESULT]
            get_MediumTurquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                           _type.HRESULT]
            get_MediumVioletRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                           _type.HRESULT]
            get_MidnightBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                        _type.HRESULT]
            get_MintCream: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_MistyRose: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Moccasin: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_NavajoWhite: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_Navy: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_OldLace: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_Olive: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_OliveDrab: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Orange: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_OrangeRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Orchid: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_PaleGoldenrod: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_PaleGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_PaleTurquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_PaleVioletRed: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
            get_PapayaWhip: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_PeachPuff: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Peru: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_Pink: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_Plum: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_PowderBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_Purple: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_Red: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                               _type.HRESULT]
            get_RosyBrown: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_RoyalBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_SaddleBrown: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_Salmon: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_SandyBrown: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_SeaGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_SeaShell: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                    _type.HRESULT]
            get_Sienna: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_Silver: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_SkyBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_SlateBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_SlateGray: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Snow: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_SpringGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_SteelBlue: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Tan: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                               _type.HRESULT]
            get_Teal: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                _type.HRESULT]
            get_Thistle: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                   _type.HRESULT]
            get_Tomato: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_Transparent: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]
            get_Turquoise: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                     _type.HRESULT]
            get_Violet: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_Wheat: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_White: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                 _type.HRESULT]
            get_WhiteSmoke: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                      _type.HRESULT]
            get_Yellow: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                  _type.HRESULT]
            get_YellowGreen: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                       _type.HRESULT]

        class IUIContentRoot(IInspectable):
            get_UIContext: _Callable

        class IUIContext(IInspectable):
            pass

        class Core:
            class _IDispatchedHandler:
                Invoke: _Callable[[],
                                  _type.HRESULT]

            class IDispatchedHandler(_IDispatchedHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IDispatchedHandler_impl(_IDispatchedHandler, IUnknown_impl):
                pass

            class _IIdleDispatchedHandler:
                Invoke: _Callable[[Windows.UI.Core.IIdleDispatchedHandlerArgs],
                                  _type.HRESULT]

            class IIdleDispatchedHandler(_IIdleDispatchedHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IIdleDispatchedHandler_impl(_IIdleDispatchedHandler, IUnknown_impl):
                pass

            class IAcceleratorKeyEventArgs(IInspectable):
                get_EventType: _Callable
                get_VirtualKey: _Callable
                get_KeyStatus: _Callable

            class IAcceleratorKeyEventArgs2(IInspectable):
                get_DeviceId: _Callable

            class IAutomationProviderRequestedEventArgs(IInspectable):
                get_AutomationProvider: _Callable
                put_AutomationProvider: _Callable

            class IBackRequestedEventArgs(IInspectable):
                get_Handled: _Callable
                put_Handled: _Callable

            class ICharacterReceivedEventArgs(IInspectable):
                get_KeyCode: _Callable
                get_KeyStatus: _Callable

            class IClosestInteractiveBoundsRequestedEventArgs(IInspectable):
                get_PointerPosition: _Callable
                get_SearchBounds: _Callable
                get_ClosestInteractiveBounds: _Callable
                put_ClosestInteractiveBounds: _Callable

            class ICoreAcceleratorKeys(IInspectable):
                add_AcceleratorKeyActivated: _Callable
                remove_AcceleratorKeyActivated: _Callable

            class ICoreClosestInteractiveBoundsRequested(IInspectable):
                add_ClosestInteractiveBoundsRequested: _Callable
                remove_ClosestInteractiveBoundsRequested: _Callable

            class ICoreComponentFocusable(IInspectable):
                get_HasFocus: _Callable
                add_GotFocus: _Callable
                remove_GotFocus: _Callable
                add_LostFocus: _Callable
                remove_LostFocus: _Callable

            class ICoreCursor(IInspectable):
                get_Id: _Callable
                get_Type: _Callable

            class ICoreCursorFactory(IInspectable):
                CreateCursor: _Callable

            class ICoreDispatcher(IInspectable):
                get_HasThreadAccess: _Callable
                ProcessEvents: _Callable
                RunAsync: _Callable
                RunIdleAsync: _Callable

            class ICoreDispatcher2(IInspectable):
                TryRunAsync: _Callable
                TryRunIdleAsync: _Callable

            class ICoreDispatcherWithTaskPriority(IInspectable):
                get_CurrentPriority: _Callable
                put_CurrentPriority: _Callable
                ShouldYield: _Callable
                ShouldYieldToPriority: _Callable
                StopProcessEvents: _Callable

            class ICoreIndependentInputSourceController(IInspectable):
                get_IsTransparentForUncontrolledInput: _Callable
                put_IsTransparentForUncontrolledInput: _Callable
                get_IsPalmRejectionEnabled: _Callable
                put_IsPalmRejectionEnabled: _Callable
                get_Source: _Callable
                SetControlledInput: _Callable
                SetControlledInputWithFilters: _Callable

            class ICoreIndependentInputSourceControllerStatics(IInspectable):
                CreateForVisual: _Callable
                CreateForIVisualElement: _Callable

            class ICoreInputSourceBase(IInspectable):
                get_Dispatcher: _Callable
                get_IsInputEnabled: _Callable
                put_IsInputEnabled: _Callable
                add_InputEnabled: _Callable
                remove_InputEnabled: _Callable

            class ICoreKeyboardInputSource(IInspectable):
                GetCurrentKeyState: _Callable
                add_CharacterReceived: _Callable
                remove_CharacterReceived: _Callable
                add_KeyDown: _Callable
                remove_KeyDown: _Callable
                add_KeyUp: _Callable
                remove_KeyUp: _Callable

            class ICoreKeyboardInputSource2(IInspectable):
                GetCurrentKeyEventDeviceId: _Callable

            class ICorePointerInputSource(IInspectable):
                ReleasePointerCapture: _Callable
                SetPointerCapture: _Callable
                get_HasCapture: _Callable
                get_PointerPosition: _Callable
                get_PointerCursor: _Callable
                put_PointerCursor: _Callable
                add_PointerCaptureLost: _Callable
                remove_PointerCaptureLost: _Callable
                add_PointerEntered: _Callable
                remove_PointerEntered: _Callable
                add_PointerExited: _Callable
                remove_PointerExited: _Callable
                add_PointerMoved: _Callable
                remove_PointerMoved: _Callable
                add_PointerPressed: _Callable
                remove_PointerPressed: _Callable
                add_PointerReleased: _Callable
                remove_PointerReleased: _Callable
                add_PointerWheelChanged: _Callable
                remove_PointerWheelChanged: _Callable

            class ICorePointerInputSource2(IInspectable):
                get_DispatcherQueue: _Callable

            class ICorePointerRedirector(IInspectable):
                add_PointerRoutedAway: _Callable
                remove_PointerRoutedAway: _Callable
                add_PointerRoutedTo: _Callable
                remove_PointerRoutedTo: _Callable
                add_PointerRoutedReleased: _Callable
                remove_PointerRoutedReleased: _Callable

            class ICoreTouchHitTesting(IInspectable):
                add_TouchHitTesting: _Callable
                remove_TouchHitTesting: _Callable

            class ICoreWindow(IInspectable):
                get_AutomationHostProvider: _Callable
                get_Bounds: _Callable
                get_CustomProperties: _Callable
                get_Dispatcher: _Callable
                get_FlowDirection: _Callable
                put_FlowDirection: _Callable
                get_IsInputEnabled: _Callable
                put_IsInputEnabled: _Callable
                get_PointerCursor: _Callable
                put_PointerCursor: _Callable
                get_PointerPosition: _Callable
                get_Visible: _Callable
                Activate: _Callable
                Close: _Callable
                GetAsyncKeyState: _Callable
                GetKeyState: _Callable
                ReleasePointerCapture: _Callable
                SetPointerCapture: _Callable
                add_Activated: _Callable
                remove_Activated: _Callable
                add_AutomationProviderRequested: _Callable
                remove_AutomationProviderRequested: _Callable
                add_CharacterReceived: _Callable
                remove_CharacterReceived: _Callable
                add_Closed: _Callable
                remove_Closed: _Callable
                add_InputEnabled: _Callable
                remove_InputEnabled: _Callable
                add_KeyDown: _Callable
                remove_KeyDown: _Callable
                add_KeyUp: _Callable
                remove_KeyUp: _Callable
                add_PointerCaptureLost: _Callable
                remove_PointerCaptureLost: _Callable
                add_PointerEntered: _Callable
                remove_PointerEntered: _Callable
                add_PointerExited: _Callable
                remove_PointerExited: _Callable
                add_PointerMoved: _Callable
                remove_PointerMoved: _Callable
                add_PointerPressed: _Callable
                remove_PointerPressed: _Callable
                add_PointerReleased: _Callable
                remove_PointerReleased: _Callable
                add_TouchHitTesting: _Callable
                remove_TouchHitTesting: _Callable
                add_PointerWheelChanged: _Callable
                remove_PointerWheelChanged: _Callable
                add_SizeChanged: _Callable
                remove_SizeChanged: _Callable
                add_VisibilityChanged: _Callable
                remove_VisibilityChanged: _Callable

            class ICoreWindow2(IInspectable):
                put_PointerPosition: _Callable

            class ICoreWindow3(IInspectable):
                add_ClosestInteractiveBoundsRequested: _Callable
                remove_ClosestInteractiveBoundsRequested: _Callable
                GetCurrentKeyEventDeviceId: _Callable

            class ICoreWindow4(IInspectable):
                add_ResizeStarted: _Callable
                remove_ResizeStarted: _Callable
                add_ResizeCompleted: _Callable
                remove_ResizeCompleted: _Callable

            class ICoreWindow5(IInspectable):
                get_DispatcherQueue: _Callable
                get_ActivationMode: _Callable

            class ICoreWindowDialog(IInspectable):
                add_Showing: _Callable
                remove_Showing: _Callable
                get_MaxSize: _Callable
                get_MinSize: _Callable
                get_Title: _Callable
                put_Title: _Callable
                get_IsInteractionDelayed: _Callable
                put_IsInteractionDelayed: _Callable
                get_Commands: _Callable
                get_DefaultCommandIndex: _Callable
                put_DefaultCommandIndex: _Callable
                get_CancelCommandIndex: _Callable
                put_CancelCommandIndex: _Callable
                get_BackButtonCommand: _Callable
                put_BackButtonCommand: _Callable
                ShowAsync: _Callable

            class ICoreWindowDialogFactory(IInspectable):
                CreateWithTitle: _Callable

            class ICoreWindowEventArgs(IInspectable):
                get_Handled: _Callable
                put_Handled: _Callable

            class ICoreWindowFlyout(IInspectable):
                add_Showing: _Callable
                remove_Showing: _Callable
                get_MaxSize: _Callable
                get_MinSize: _Callable
                get_Title: _Callable
                put_Title: _Callable
                get_IsInteractionDelayed: _Callable
                put_IsInteractionDelayed: _Callable
                get_Commands: _Callable
                get_DefaultCommandIndex: _Callable
                put_DefaultCommandIndex: _Callable
                get_BackButtonCommand: _Callable
                put_BackButtonCommand: _Callable
                ShowAsync: _Callable

            class ICoreWindowFlyoutFactory(IInspectable):
                Create: _Callable
                CreateWithTitle: _Callable

            class ICoreWindowPopupShowingEventArgs(IInspectable):
                SetDesiredSize: _Callable

            class ICoreWindowResizeManager(IInspectable):
                NotifyLayoutCompleted: _Callable

            class ICoreWindowResizeManagerLayoutCapability(IInspectable):
                put_ShouldWaitForLayoutCompletion: _Callable
                get_ShouldWaitForLayoutCompletion: _Callable

            class ICoreWindowResizeManagerStatics(IInspectable):
                GetForCurrentView: _Callable

            class ICoreWindowStatic(IInspectable):
                GetForCurrentThread: _Callable

            class ICoreWindowWithContext(IInspectable):
                get_UIContext: _Callable

            class IIdleDispatchedHandlerArgs(IInspectable):
                get_IsDispatcherIdle: _Callable

            class IInitializeWithCoreWindow(IInspectable):
                Initialize: _Callable

            class IInputEnabledEventArgs(IInspectable):
                get_InputEnabled: _Callable

            class IKeyEventArgs(IInspectable):
                get_VirtualKey: _Callable
                get_KeyStatus: _Callable

            class IKeyEventArgs2(IInspectable):
                get_DeviceId: _Callable

            class IPointerEventArgs(IInspectable):
                get_CurrentPoint: _Callable
                get_KeyModifiers: _Callable
                GetIntermediatePoints: _Callable

            class ISystemNavigationManager(IInspectable):
                add_BackRequested: _Callable
                remove_BackRequested: _Callable

            class ISystemNavigationManager2(IInspectable):
                get_AppViewBackButtonVisibility: _Callable
                put_AppViewBackButtonVisibility: _Callable

            class ISystemNavigationManagerStatics(IInspectable):
                GetForCurrentView: _Callable

            class ITouchHitTestingEventArgs(IInspectable):
                get_ProximityEvaluation: _Callable
                put_ProximityEvaluation: _Callable
                get_Point: _Callable
                get_BoundingBox: _Callable
                EvaluateProximityToRect: _Callable
                EvaluateProximityToPolygon: _Callable

            class IVisibilityChangedEventArgs(IInspectable):
                get_Visible: _Callable

            class IWindowActivatedEventArgs(IInspectable):
                get_WindowActivationState: _Callable

            class IWindowSizeChangedEventArgs(IInspectable):
                get_Size: _Callable

        class Notifications:
            class IAdaptiveNotificationContent(IInspectable):
                get_Kind: _Callable
                get_Hints: _Callable

            class IAdaptiveNotificationText(IInspectable):
                get_Text: _Callable
                put_Text: _Callable
                get_Language: _Callable
                put_Language: _Callable

            class IBadgeNotification(IInspectable):
                get_Content: _Callable
                put_ExpirationTime: _Callable
                get_ExpirationTime: _Callable

            class IBadgeNotificationFactory(IInspectable):
                CreateBadgeNotification: _Callable

            class IBadgeUpdateManagerForUser(IInspectable):
                CreateBadgeUpdaterForApplication: _Callable
                CreateBadgeUpdaterForApplicationWithId: _Callable
                CreateBadgeUpdaterForSecondaryTile: _Callable
                get_User: _Callable

            class IBadgeUpdateManagerStatics(IInspectable):
                CreateBadgeUpdaterForApplication: _Callable
                CreateBadgeUpdaterForApplicationWithId: _Callable
                CreateBadgeUpdaterForSecondaryTile: _Callable
                GetTemplateContent: _Callable

            class IBadgeUpdateManagerStatics2(IInspectable):
                GetForUser: _Callable

            class IBadgeUpdater(IInspectable):
                Update: _Callable
                Clear: _Callable
                StartPeriodicUpdate: _Callable
                StartPeriodicUpdateAtTime: _Callable
                StopPeriodicUpdate: _Callable

            class IKnownAdaptiveNotificationHintsStatics(IInspectable):
                get_Style: _Callable
                get_Wrap: _Callable
                get_MaxLines: _Callable
                get_MinLines: _Callable
                get_TextStacking: _Callable
                get_Align: _Callable

            class IKnownAdaptiveNotificationTextStylesStatics(IInspectable):
                get_Caption: _Callable
                get_Body: _Callable
                get_Base: _Callable
                get_Subtitle: _Callable
                get_Title: _Callable
                get_Subheader: _Callable
                get_Header: _Callable
                get_TitleNumeral: _Callable
                get_SubheaderNumeral: _Callable
                get_HeaderNumeral: _Callable
                get_CaptionSubtle: _Callable
                get_BodySubtle: _Callable
                get_BaseSubtle: _Callable
                get_SubtitleSubtle: _Callable
                get_TitleSubtle: _Callable
                get_SubheaderSubtle: _Callable
                get_SubheaderNumeralSubtle: _Callable
                get_HeaderSubtle: _Callable
                get_HeaderNumeralSubtle: _Callable

            class IKnownNotificationBindingsStatics(IInspectable):
                get_ToastGeneric: _Callable

            class INotification(IInspectable):
                get_ExpirationTime: _Callable
                put_ExpirationTime: _Callable
                get_Visual: _Callable
                put_Visual: _Callable

            class INotificationBinding(IInspectable):
                get_Template: _Callable
                put_Template: _Callable
                get_Language: _Callable
                put_Language: _Callable
                get_Hints: _Callable
                GetTextElements: _Callable

            class INotificationData(IInspectable):
                get_Values: _Callable
                get_SequenceNumber: _Callable
                put_SequenceNumber: _Callable

            class INotificationDataFactory(IInspectable):
                CreateNotificationDataWithValuesAndSequenceNumber: _Callable
                CreateNotificationDataWithValues: _Callable

            class INotificationVisual(IInspectable):
                get_Language: _Callable
                put_Language: _Callable
                get_Bindings: _Callable
                GetBinding: _Callable

            class IScheduledTileNotification(IInspectable):
                get_Content: _Callable
                get_DeliveryTime: _Callable
                put_ExpirationTime: _Callable
                get_ExpirationTime: _Callable
                put_Tag: _Callable
                get_Tag: _Callable
                put_Id: _Callable
                get_Id: _Callable

            class IScheduledTileNotificationFactory(IInspectable):
                CreateScheduledTileNotification: _Callable

            class IScheduledToastNotification(IInspectable):
                get_Content: _Callable
                get_DeliveryTime: _Callable
                get_SnoozeInterval: _Callable
                get_MaximumSnoozeCount: _Callable
                put_Id: _Callable
                get_Id: _Callable

            class IScheduledToastNotification2(IInspectable):
                put_Tag: _Callable
                get_Tag: _Callable
                put_Group: _Callable
                get_Group: _Callable
                put_SuppressPopup: _Callable
                get_SuppressPopup: _Callable

            class IScheduledToastNotification3(IInspectable):
                get_NotificationMirroring: _Callable
                put_NotificationMirroring: _Callable
                get_RemoteId: _Callable
                put_RemoteId: _Callable

            class IScheduledToastNotification4(IInspectable):
                get_ExpirationTime: _Callable
                put_ExpirationTime: _Callable

            class IScheduledToastNotificationFactory(IInspectable):
                CreateScheduledToastNotification: _Callable
                CreateScheduledToastNotificationRecurring: _Callable

            class IScheduledToastNotificationShowingEventArgs(IInspectable):
                get_Cancel: _Callable
                put_Cancel: _Callable
                get_ScheduledToastNotification: _Callable
                GetDeferral: _Callable

            class IShownTileNotification(IInspectable):
                get_Arguments: _Callable

            class ITileFlyoutNotification(IInspectable):
                get_Content: _Callable
                put_ExpirationTime: _Callable
                get_ExpirationTime: _Callable

            class ITileFlyoutNotificationFactory(IInspectable):
                CreateTileFlyoutNotification: _Callable

            class ITileFlyoutUpdateManagerStatics(IInspectable):
                CreateTileFlyoutUpdaterForApplication: _Callable
                CreateTileFlyoutUpdaterForApplicationWithId: _Callable
                CreateTileFlyoutUpdaterForSecondaryTile: _Callable
                GetTemplateContent: _Callable

            class ITileFlyoutUpdater(IInspectable):
                Update: _Callable
                Clear: _Callable
                StartPeriodicUpdate: _Callable
                StartPeriodicUpdateAtTime: _Callable
                StopPeriodicUpdate: _Callable
                get_Setting: _Callable

            class ITileNotification(IInspectable):
                get_Content: _Callable
                put_ExpirationTime: _Callable
                get_ExpirationTime: _Callable
                put_Tag: _Callable
                get_Tag: _Callable

            class ITileNotificationFactory(IInspectable):
                CreateTileNotification: _Callable

            class ITileUpdateManagerForUser(IInspectable):
                CreateTileUpdaterForApplication: _Callable
                CreateTileUpdaterForApplicationWithId: _Callable
                CreateTileUpdaterForSecondaryTile: _Callable
                get_User: _Callable

            class ITileUpdateManagerStatics(IInspectable):
                CreateTileUpdaterForApplication: _Callable
                CreateTileUpdaterForApplicationWithId: _Callable
                CreateTileUpdaterForSecondaryTile: _Callable
                GetTemplateContent: _Callable

            class ITileUpdateManagerStatics2(IInspectable):
                GetForUser: _Callable

            class ITileUpdater(IInspectable):
                Update: _Callable
                Clear: _Callable
                EnableNotificationQueue: _Callable
                get_Setting: _Callable
                AddToSchedule: _Callable
                RemoveFromSchedule: _Callable
                GetScheduledTileNotifications: _Callable
                StartPeriodicUpdate: _Callable
                StartPeriodicUpdateAtTime: _Callable
                StopPeriodicUpdate: _Callable
                StartPeriodicUpdateBatch: _Callable
                StartPeriodicUpdateBatchAtTime: _Callable

            class ITileUpdater2(IInspectable):
                EnableNotificationQueueForSquare150x150: _Callable
                EnableNotificationQueueForWide310x150: _Callable
                EnableNotificationQueueForSquare310x310: _Callable

            class IToastActivatedEventArgs(IInspectable):
                get_Argument: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]

            class IToastActivatedEventArgs2(IInspectable):
                get_UserInput: _Callable

            class IToastCollection(IInspectable):
                get_Id: _Callable
                get_DisplayName: _Callable
                put_DisplayName: _Callable
                get_LaunchArgs: _Callable
                put_LaunchArgs: _Callable
                get_Icon: _Callable
                put_Icon: _Callable

            class IToastCollectionFactory(IInspectable):
                CreateInstance: _Callable

            class IToastCollectionManager(IInspectable):
                SaveToastCollectionAsync: _Callable
                FindAllToastCollectionsAsync: _Callable
                GetToastCollectionAsync: _Callable
                RemoveToastCollectionAsync: _Callable
                RemoveAllToastCollectionsAsync: _Callable
                get_User: _Callable
                get_AppId: _Callable

            class IToastDismissedEventArgs(IInspectable):
                get_Reason: _Callable[[_Pointer[_enum.Windows.UI.Notifications.ToastDismissalReason]],
                                      _type.HRESULT]

            class IToastFailedEventArgs(IInspectable):
                get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],
                                         _type.HRESULT]

            class IToastNotification(IInspectable):
                get_Content: _Callable[[_Pointer[Windows.Data.Xml.Dom.IXmlDocument]],
                                       _type.HRESULT]
                put_ExpirationTime: _Callable
                get_ExpirationTime: _Callable
                add_Dismissed: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Notifications.IToastNotification, Windows.UI.Notifications.IToastDismissedEventArgs],
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_Dismissed: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_Activated: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Notifications.IToastNotification, IInspectable],
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_Activated: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_Failed: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Notifications.IToastNotification, Windows.UI.Notifications.IToastFailedEventArgs],
                                       _Pointer[_struct.EventRegistrationToken]],
                                      _type.HRESULT]
                remove_Failed: _Callable[[_struct.EventRegistrationToken],
                                         _type.HRESULT]

            class IToastNotification2(IInspectable):
                put_Tag: _Callable
                get_Tag: _Callable
                put_Group: _Callable
                get_Group: _Callable
                put_SuppressPopup: _Callable
                get_SuppressPopup: _Callable

            class IToastNotification3(IInspectable):
                get_NotificationMirroring: _Callable
                put_NotificationMirroring: _Callable
                get_RemoteId: _Callable
                put_RemoteId: _Callable

            class IToastNotification4(IInspectable):
                get_Data: _Callable
                put_Data: _Callable
                get_Priority: _Callable
                put_Priority: _Callable

            class IToastNotification6(IInspectable):
                get_ExpiresOnReboot: _Callable
                put_ExpiresOnReboot: _Callable

            class IToastNotificationActionTriggerDetail(IInspectable):
                get_Argument: _Callable
                get_UserInput: _Callable

            class IToastNotificationFactory(IInspectable):
                CreateToastNotification: _Callable[[Windows.Data.Xml.Dom.IXmlDocument,
                                                    _Pointer[Windows.UI.Notifications.IToastNotification]],
                                                   _type.HRESULT]

            class IToastNotificationHistory(IInspectable):
                RemoveGroup: _Callable
                RemoveGroupWithId: _Callable
                RemoveGroupedTagWithId: _Callable
                RemoveGroupedTag: _Callable
                Remove: _Callable
                Clear: _Callable
                ClearWithId: _Callable

            class IToastNotificationHistory2(IInspectable):
                GetHistory: _Callable
                GetHistoryWithId: _Callable

            class IToastNotificationHistoryChangedTriggerDetail(IInspectable):
                get_ChangeType: _Callable

            class IToastNotificationHistoryChangedTriggerDetail2(IInspectable):
                get_CollectionId: _Callable

            class IToastNotificationManagerForUser(IInspectable):
                CreateToastNotifier: _Callable
                CreateToastNotifierWithId: _Callable
                get_History: _Callable
                get_User: _Callable

            class IToastNotificationManagerForUser2(IInspectable):
                GetToastNotifierForToastCollectionIdAsync: _Callable
                GetHistoryForToastCollectionIdAsync: _Callable
                GetToastCollectionManager: _Callable
                GetToastCollectionManagerWithAppId: _Callable

            class IToastNotificationManagerStatics(IInspectable):
                CreateToastNotifier: _Callable[[_Pointer[Windows.UI.Notifications.IToastNotifier]],
                                               _type.HRESULT]
                CreateToastNotifierWithId: _Callable[[_type.HSTRING,
                                                      _Pointer[Windows.UI.Notifications.IToastNotifier]],
                                                     _type.HRESULT]
                GetTemplateContent: _Callable

            class IToastNotificationManagerStatics2(IInspectable):
                get_History: _Callable

            class IToastNotificationManagerStatics4(IInspectable):
                GetForUser: _Callable
                ConfigureNotificationMirroring: _Callable

            class IToastNotificationManagerStatics5(IInspectable):
                GetDefault: _Callable

            class IToastNotifier(IInspectable):
                Show: _Callable[[Windows.UI.Notifications.IToastNotification],
                                _type.HRESULT]
                Hide: _Callable[[Windows.UI.Notifications.IToastNotification],
                                _type.HRESULT]
                get_Setting: _Callable[[_Pointer[_enum.Windows.UI.Notifications.NotificationSetting]],
                                       _type.HRESULT]
                AddToSchedule: _Callable
                RemoveFromSchedule: _Callable
                GetScheduledToastNotifications: _Callable

            class IToastNotifier2(IInspectable):
                UpdateWithTagAndGroup: _Callable
                UpdateWithTag: _Callable

            class IToastNotifier3(IInspectable):
                add_ScheduledToastNotificationShowing: _Callable
                remove_ScheduledToastNotificationShowing: _Callable

            class IUserNotification(IInspectable):
                get_Notification: _Callable
                get_AppInfo: _Callable
                get_Id: _Callable
                get_CreationTime: _Callable

            class IUserNotificationChangedEventArgs(IInspectable):
                get_ChangeKind: _Callable
                get_UserNotificationId: _Callable

        class ViewManagement:
            class IAccessibilitySettings(IInspectable):
                get_HighContrast: _Callable
                get_HighContrastScheme: _Callable
                add_HighContrastChanged: _Callable
                remove_HighContrastChanged: _Callable

            class IActivationViewSwitcher(IInspectable):
                ShowAsStandaloneAsync: _Callable
                ShowAsStandaloneWithSizePreferenceAsync: _Callable
                IsViewPresentedOnActivationVirtualDesktop: _Callable

            class IApplicationView(IInspectable):
                get_Orientation: _Callable
                get_AdjacentToLeftDisplayEdge: _Callable
                get_AdjacentToRightDisplayEdge: _Callable
                get_IsFullScreen: _Callable
                get_IsOnLockScreen: _Callable
                get_IsScreenCaptureEnabled: _Callable
                put_IsScreenCaptureEnabled: _Callable
                put_Title: _Callable
                get_Title: _Callable
                get_Id: _Callable
                add_Consolidated: _Callable
                remove_Consolidated: _Callable

            class IApplicationView2(IInspectable):
                get_SuppressSystemOverlays: _Callable
                put_SuppressSystemOverlays: _Callable
                get_VisibleBounds: _Callable
                add_VisibleBoundsChanged: _Callable
                remove_VisibleBoundsChanged: _Callable
                SetDesiredBoundsMode: _Callable
                get_DesiredBoundsMode: _Callable

            class IApplicationView3(IInspectable):
                get_TitleBar: _Callable
                get_FullScreenSystemOverlayMode: _Callable
                put_FullScreenSystemOverlayMode: _Callable
                get_IsFullScreenMode: _Callable
                TryEnterFullScreenMode: _Callable
                ExitFullScreenMode: _Callable
                ShowStandardSystemOverlays: _Callable
                TryResizeView: _Callable
                SetPreferredMinSize: _Callable

            class IApplicationView4(IInspectable):
                get_ViewMode: _Callable
                IsViewModeSupported: _Callable
                TryEnterViewModeAsync: _Callable
                TryEnterViewModeWithPreferencesAsync: _Callable
                TryConsolidateAsync: _Callable

            class IApplicationView7(IInspectable):
                get_PersistedStateId: _Callable
                put_PersistedStateId: _Callable

            class IApplicationView9(IInspectable):
                get_WindowingEnvironment: _Callable
                GetDisplayRegions: _Callable

            class IApplicationViewConsolidatedEventArgs(IInspectable):
                get_IsUserInitiated: _Callable

            class IApplicationViewConsolidatedEventArgs2(IInspectable):
                get_IsAppInitiated: _Callable

            class IApplicationViewFullscreenStatics(IInspectable):
                TryUnsnapToFullscreen: _Callable

            class IApplicationViewInteropStatics(IInspectable):
                GetApplicationViewIdForWindow: _Callable

            class IApplicationViewScaling(IInspectable):
                pass

            class IApplicationViewScalingStatics(IInspectable):
                get_DisableLayoutScaling: _Callable
                TrySetDisableLayoutScaling: _Callable

            class IApplicationViewStatics(IInspectable):
                get_Value: _Callable
                TryUnsnap: _Callable

            class IApplicationViewStatics2(IInspectable):
                GetForCurrentView: _Callable
                get_TerminateAppOnFinalViewClose: _Callable
                put_TerminateAppOnFinalViewClose: _Callable

            class IApplicationViewStatics3(IInspectable):
                get_PreferredLaunchWindowingMode: _Callable
                put_PreferredLaunchWindowingMode: _Callable
                get_PreferredLaunchViewSize: _Callable
                put_PreferredLaunchViewSize: _Callable

            class IApplicationViewStatics4(IInspectable):
                ClearAllPersistedState: _Callable
                ClearPersistedState: _Callable

            class IApplicationViewSwitcherStatics(IInspectable):
                DisableShowingMainViewOnActivation: _Callable
                TryShowAsStandaloneAsync: _Callable
                TryShowAsStandaloneWithSizePreferenceAsync: _Callable
                TryShowAsStandaloneWithAnchorViewAndSizePreferenceAsync: _Callable
                SwitchAsync: _Callable
                SwitchFromViewAsync: _Callable
                SwitchFromViewWithOptionsAsync: _Callable
                PrepareForCustomAnimatedSwitchAsync: _Callable

            class IApplicationViewSwitcherStatics2(IInspectable):
                DisableSystemViewActivationPolicy: _Callable

            class IApplicationViewSwitcherStatics3(IInspectable):
                TryShowAsViewModeAsync: _Callable
                TryShowAsViewModeWithPreferencesAsync: _Callable

            class IApplicationViewTitleBar(IInspectable):
                put_ForegroundColor: _Callable
                get_ForegroundColor: _Callable
                put_BackgroundColor: _Callable
                get_BackgroundColor: _Callable
                put_ButtonForegroundColor: _Callable
                get_ButtonForegroundColor: _Callable
                put_ButtonBackgroundColor: _Callable
                get_ButtonBackgroundColor: _Callable
                put_ButtonHoverForegroundColor: _Callable
                get_ButtonHoverForegroundColor: _Callable
                put_ButtonHoverBackgroundColor: _Callable
                get_ButtonHoverBackgroundColor: _Callable
                put_ButtonPressedForegroundColor: _Callable
                get_ButtonPressedForegroundColor: _Callable
                put_ButtonPressedBackgroundColor: _Callable
                get_ButtonPressedBackgroundColor: _Callable
                put_InactiveForegroundColor: _Callable
                get_InactiveForegroundColor: _Callable
                put_InactiveBackgroundColor: _Callable
                get_InactiveBackgroundColor: _Callable
                put_ButtonInactiveForegroundColor: _Callable
                get_ButtonInactiveForegroundColor: _Callable
                put_ButtonInactiveBackgroundColor: _Callable
                get_ButtonInactiveBackgroundColor: _Callable

            class IApplicationViewTransferContext(IInspectable):
                get_ViewId: _Callable
                put_ViewId: _Callable

            class IApplicationViewTransferContextStatics(IInspectable):
                get_DataPackageFormatId: _Callable

            class IApplicationViewWithContext(IInspectable):
                get_UIContext: _Callable

            class IInputPane(IInspectable):
                add_Showing: _Callable
                remove_Showing: _Callable
                add_Hiding: _Callable
                remove_Hiding: _Callable
                get_OccludedRect: _Callable

            class IInputPane2(IInspectable):
                TryShow: _Callable
                TryHide: _Callable

            class IInputPaneControl(IInspectable):
                get_Visible: _Callable
                put_Visible: _Callable

            class IInputPaneStatics(IInspectable):
                GetForCurrentView: _Callable

            class IInputPaneStatics2(IInspectable):
                GetForUIContext: _Callable

            class IInputPaneVisibilityEventArgs(IInspectable):
                get_OccludedRect: _Callable
                put_EnsuredFocusedElementInView: _Callable
                get_EnsuredFocusedElementInView: _Callable

            class IProjectionManagerStatics(IInspectable):
                StartProjectingAsync: _Callable
                SwapDisplaysForViewsAsync: _Callable
                StopProjectingAsync: _Callable
                get_ProjectionDisplayAvailable: _Callable
                add_ProjectionDisplayAvailableChanged: _Callable
                remove_ProjectionDisplayAvailableChanged: _Callable

            class IProjectionManagerStatics2(IInspectable):
                StartProjectingWithDeviceInfoAsync: _Callable
                RequestStartProjectingAsync: _Callable
                RequestStartProjectingWithPlacementAsync: _Callable
                GetDeviceSelector: _Callable

            class IStatusBar(IInspectable):
                ShowAsync: _Callable
                HideAsync: _Callable
                get_BackgroundOpacity: _Callable
                put_BackgroundOpacity: _Callable
                get_ForegroundColor: _Callable
                put_ForegroundColor: _Callable
                get_BackgroundColor: _Callable
                put_BackgroundColor: _Callable
                get_ProgressIndicator: _Callable
                get_OccludedRect: _Callable
                add_Showing: _Callable
                remove_Showing: _Callable
                add_Hiding: _Callable
                remove_Hiding: _Callable

            class IStatusBarProgressIndicator(IInspectable):
                ShowAsync: _Callable
                HideAsync: _Callable
                get_Text: _Callable
                put_Text: _Callable
                get_ProgressValue: _Callable
                put_ProgressValue: _Callable

            class IStatusBarStatics(IInspectable):
                GetForCurrentView: _Callable

            class IUISettings(IInspectable):
                get_HandPreference: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.HandPreference]],
                                              _type.HRESULT]
                get_CursorSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                          _type.HRESULT]
                get_ScrollBarSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                             _type.HRESULT]
                get_ScrollBarArrowSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                                  _type.HRESULT]
                get_ScrollBarThumbBoxSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
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
                UIElementColor: _Callable[[_enum.Windows.UI.ViewManagement.UIElementType,
                                           _Pointer[_struct.Windows.UI.Color]],
                                          _type.HRESULT]

            class IUISettings2(IInspectable):
                get_TextScaleFactor: _Callable
                add_TextScaleFactorChanged: _Callable
                remove_TextScaleFactorChanged: _Callable

            class IUISettings3(IInspectable):
                GetColorValue: _Callable
                add_ColorValuesChanged: _Callable
                remove_ColorValuesChanged: _Callable

            class IUISettings4(IInspectable):
                get_AdvancedEffectsEnabled: _Callable
                add_AdvancedEffectsEnabledChanged: _Callable
                remove_AdvancedEffectsEnabledChanged: _Callable

            class IUISettings5(IInspectable):
                get_AutoHideScrollBars: _Callable
                add_AutoHideScrollBarsChanged: _Callable
                remove_AutoHideScrollBarsChanged: _Callable

            class IUISettings6(IInspectable):
                add_AnimationsEnabledChanged: _Callable
                remove_AnimationsEnabledChanged: _Callable
                add_MessageDurationChanged: _Callable
                remove_MessageDurationChanged: _Callable

            class IUISettingsAnimationsEnabledChangedEventArgs(IInspectable):
                pass

            class IUISettingsAutoHideScrollBarsChangedEventArgs(IInspectable):
                pass

            class IUISettingsMessageDurationChangedEventArgs(IInspectable):
                pass

            class IUIViewSettings(IInspectable):
                get_UserInteractionMode: _Callable

            class IUIViewSettingsStatics(IInspectable):
                GetForCurrentView: _Callable

            class IViewModePreferences(IInspectable):
                get_ViewSizePreference: _Callable
                put_ViewSizePreference: _Callable
                get_CustomSize: _Callable
                put_CustomSize: _Callable

            class IViewModePreferencesStatics(IInspectable):
                CreateDefault: _Callable

        class Xaml:
            class _IApplicationInitializationCallback:
                Invoke: _Callable[[Windows.UI.Xaml.IApplicationInitializationCallbackParams],
                                  _type.HRESULT]

            class IApplicationInitializationCallback(_IApplicationInitializationCallback, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IApplicationInitializationCallback_impl(_IApplicationInitializationCallback, IUnknown_impl):
                pass

            class _IBindingFailedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.IBindingFailedEventArgs],
                                  _type.HRESULT]

            class IBindingFailedEventHandler(_IBindingFailedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IBindingFailedEventHandler_impl(_IBindingFailedEventHandler, IUnknown_impl):
                pass

            class _ICreateDefaultValueCallback:
                Invoke: _Callable[[_Pointer[IInspectable]],
                                  _type.HRESULT]

            class ICreateDefaultValueCallback(_ICreateDefaultValueCallback, IUnknown):
                pass

            # noinspection PyPep8Naming
            class ICreateDefaultValueCallback_impl(_ICreateDefaultValueCallback, IUnknown_impl):
                pass

            class _IDependencyPropertyChangedCallback:
                Invoke: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                   Windows.UI.Xaml.IDependencyProperty],
                                  _type.HRESULT]

            class IDependencyPropertyChangedCallback(_IDependencyPropertyChangedCallback, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IDependencyPropertyChangedCallback_impl(_IDependencyPropertyChangedCallback, IUnknown_impl):
                pass

            class _IDependencyPropertyChangedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.IDependencyPropertyChangedEventArgs],
                                  _type.HRESULT]

            class IDependencyPropertyChangedEventHandler(_IDependencyPropertyChangedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IDependencyPropertyChangedEventHandler_impl(_IDependencyPropertyChangedEventHandler, IUnknown_impl):
                pass

            class _IDragEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.IDragEventArgs],
                                  _type.HRESULT]

            class IDragEventHandler(_IDragEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IDragEventHandler_impl(_IDragEventHandler, IUnknown_impl):
                pass

            class _IEnteredBackgroundEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.ApplicationModel.IEnteredBackgroundEventArgs],
                                  _type.HRESULT]

            class IEnteredBackgroundEventHandler(_IEnteredBackgroundEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IEnteredBackgroundEventHandler_impl(_IEnteredBackgroundEventHandler, IUnknown_impl):
                pass

            class _IExceptionRoutedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.IExceptionRoutedEventArgs],
                                  _type.HRESULT]

            class IExceptionRoutedEventHandler(_IExceptionRoutedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IExceptionRoutedEventHandler_impl(_IExceptionRoutedEventHandler, IUnknown_impl):
                pass

            class _ILeavingBackgroundEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.ApplicationModel.ILeavingBackgroundEventArgs],
                                  _type.HRESULT]

            class ILeavingBackgroundEventHandler(_ILeavingBackgroundEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class ILeavingBackgroundEventHandler_impl(_ILeavingBackgroundEventHandler, IUnknown_impl):
                pass

            class _IPropertyChangedCallback:
                Invoke: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                   Windows.UI.Xaml.IDependencyPropertyChangedEventArgs],
                                  _type.HRESULT]

            class IPropertyChangedCallback(_IPropertyChangedCallback, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IPropertyChangedCallback_impl(_IPropertyChangedCallback, IUnknown_impl):
                pass

            class _IRoutedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.IRoutedEventArgs],
                                  _type.HRESULT]

            class IRoutedEventHandler(_IRoutedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IRoutedEventHandler_impl(_IRoutedEventHandler, IUnknown_impl):
                pass

            class _ISizeChangedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.ISizeChangedEventArgs],
                                  _type.HRESULT]

            class ISizeChangedEventHandler(_ISizeChangedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class ISizeChangedEventHandler_impl(_ISizeChangedEventHandler, IUnknown_impl):
                pass

            class _ISuspendingEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.ApplicationModel.ISuspendingEventArgs],
                                  _type.HRESULT]

            class ISuspendingEventHandler(_ISuspendingEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class ISuspendingEventHandler_impl(_ISuspendingEventHandler, IUnknown_impl):
                pass

            class _IUnhandledExceptionEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.IUnhandledExceptionEventArgs],
                                  _type.HRESULT]

            class IUnhandledExceptionEventHandler(_IUnhandledExceptionEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IUnhandledExceptionEventHandler_impl(_IUnhandledExceptionEventHandler, IUnknown_impl):
                pass

            class _IVisualStateChangedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Xaml.IVisualStateChangedEventArgs],
                                  _type.HRESULT]

            class IVisualStateChangedEventHandler(_IVisualStateChangedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IVisualStateChangedEventHandler_impl(_IVisualStateChangedEventHandler, IUnknown_impl):
                pass

            class _IWindowActivatedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Core.IWindowActivatedEventArgs],
                                  _type.HRESULT]

            class IWindowActivatedEventHandler(_IWindowActivatedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IWindowActivatedEventHandler_impl(_IWindowActivatedEventHandler, IUnknown_impl):
                pass

            class _IWindowClosedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Core.ICoreWindowEventArgs],
                                  _type.HRESULT]

            class IWindowClosedEventHandler(_IWindowClosedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IWindowClosedEventHandler_impl(_IWindowClosedEventHandler, IUnknown_impl):
                pass

            class _IWindowSizeChangedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Core.IWindowSizeChangedEventArgs],
                                  _type.HRESULT]

            class IWindowSizeChangedEventHandler(_IWindowSizeChangedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IWindowSizeChangedEventHandler_impl(_IWindowSizeChangedEventHandler, IUnknown_impl):
                pass

            class _IWindowVisibilityChangedEventHandler:
                Invoke: _Callable[[IInspectable,
                                   Windows.UI.Core.IVisibilityChangedEventArgs],
                                  _type.HRESULT]

            class IWindowVisibilityChangedEventHandler(_IWindowVisibilityChangedEventHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IWindowVisibilityChangedEventHandler_impl(_IWindowVisibilityChangedEventHandler, IUnknown_impl):
                pass

            class IAdaptiveTrigger(IInspectable):
                get_MinWindowWidth: _Callable
                put_MinWindowWidth: _Callable
                get_MinWindowHeight: _Callable
                put_MinWindowHeight: _Callable

            class IAdaptiveTriggerFactory(IInspectable):
                CreateInstance: _Callable

            class IAdaptiveTriggerStatics(IInspectable):
                get_MinWindowWidthProperty: _Callable
                get_MinWindowHeightProperty: _Callable

            class IApplication(IInspectable):
                get_Resources: _Callable
                put_Resources: _Callable
                get_DebugSettings: _Callable
                get_RequestedTheme: _Callable
                put_RequestedTheme: _Callable
                add_UnhandledException: _Callable
                remove_UnhandledException: _Callable
                add_Suspending: _Callable
                remove_Suspending: _Callable
                add_Resuming: _Callable
                remove_Resuming: _Callable
                Exit: _Callable

            class IApplication2(IInspectable):
                get_FocusVisualKind: _Callable
                put_FocusVisualKind: _Callable
                get_RequiresPointerMode: _Callable
                put_RequiresPointerMode: _Callable
                add_LeavingBackground: _Callable
                remove_LeavingBackground: _Callable
                add_EnteredBackground: _Callable
                remove_EnteredBackground: _Callable

            class IApplication3(IInspectable):
                get_HighContrastAdjustment: _Callable
                put_HighContrastAdjustment: _Callable

            class IApplicationFactory(IInspectable):
                CreateInstance: _Callable

            class IApplicationInitializationCallbackParams(IInspectable):
                pass

            class IApplicationOverrides(IInspectable):
                OnActivated: _Callable
                OnLaunched: _Callable
                OnFileActivated: _Callable
                OnSearchActivated: _Callable
                OnShareTargetActivated: _Callable
                OnFileOpenPickerActivated: _Callable
                OnFileSavePickerActivated: _Callable
                OnCachedFileUpdaterActivated: _Callable
                OnWindowCreated: _Callable

            class IApplicationOverrides2(IInspectable):
                OnBackgroundActivated: _Callable

            class IApplicationStatics(IInspectable):
                get_Current: _Callable
                Start: _Callable
                LoadComponent: _Callable
                LoadComponentWithResourceLocation: _Callable

            class IBindingFailedEventArgs(IInspectable):
                get_Message: _Callable

            class IBringIntoViewOptions(IInspectable):
                get_AnimationDesired: _Callable
                put_AnimationDesired: _Callable
                get_TargetRect: _Callable
                put_TargetRect: _Callable

            class IBringIntoViewOptions2(IInspectable):
                get_HorizontalAlignmentRatio: _Callable
                put_HorizontalAlignmentRatio: _Callable
                get_VerticalAlignmentRatio: _Callable
                put_VerticalAlignmentRatio: _Callable
                get_HorizontalOffset: _Callable
                put_HorizontalOffset: _Callable
                get_VerticalOffset: _Callable
                put_VerticalOffset: _Callable

            class IBringIntoViewRequestedEventArgs(IInspectable):
                get_TargetElement: _Callable
                put_TargetElement: _Callable
                get_AnimationDesired: _Callable
                put_AnimationDesired: _Callable
                get_TargetRect: _Callable
                put_TargetRect: _Callable
                get_HorizontalAlignmentRatio: _Callable
                get_VerticalAlignmentRatio: _Callable
                get_HorizontalOffset: _Callable
                put_HorizontalOffset: _Callable
                get_VerticalOffset: _Callable
                put_VerticalOffset: _Callable
                get_Handled: _Callable
                put_Handled: _Callable

            class IBrushTransition(IInspectable):
                get_Duration: _Callable
                put_Duration: _Callable

            class IBrushTransitionFactory(IInspectable):
                CreateInstance: _Callable

            class IColorPaletteResources(IInspectable):
                get_AltHigh: _Callable
                put_AltHigh: _Callable
                get_AltLow: _Callable
                put_AltLow: _Callable
                get_AltMedium: _Callable
                put_AltMedium: _Callable
                get_AltMediumHigh: _Callable
                put_AltMediumHigh: _Callable
                get_AltMediumLow: _Callable
                put_AltMediumLow: _Callable
                get_BaseHigh: _Callable
                put_BaseHigh: _Callable
                get_BaseLow: _Callable
                put_BaseLow: _Callable
                get_BaseMedium: _Callable
                put_BaseMedium: _Callable
                get_BaseMediumHigh: _Callable
                put_BaseMediumHigh: _Callable
                get_BaseMediumLow: _Callable
                put_BaseMediumLow: _Callable
                get_ChromeAltLow: _Callable
                put_ChromeAltLow: _Callable
                get_ChromeBlackHigh: _Callable
                put_ChromeBlackHigh: _Callable
                get_ChromeBlackLow: _Callable
                put_ChromeBlackLow: _Callable
                get_ChromeBlackMediumLow: _Callable
                put_ChromeBlackMediumLow: _Callable
                get_ChromeBlackMedium: _Callable
                put_ChromeBlackMedium: _Callable
                get_ChromeDisabledHigh: _Callable
                put_ChromeDisabledHigh: _Callable
                get_ChromeDisabledLow: _Callable
                put_ChromeDisabledLow: _Callable
                get_ChromeHigh: _Callable
                put_ChromeHigh: _Callable
                get_ChromeLow: _Callable
                put_ChromeLow: _Callable
                get_ChromeMedium: _Callable
                put_ChromeMedium: _Callable
                get_ChromeMediumLow: _Callable
                put_ChromeMediumLow: _Callable
                get_ChromeWhite: _Callable
                put_ChromeWhite: _Callable
                get_ChromeGray: _Callable
                put_ChromeGray: _Callable
                get_ListLow: _Callable
                put_ListLow: _Callable
                get_ListMedium: _Callable
                put_ListMedium: _Callable
                get_ErrorText: _Callable
                put_ErrorText: _Callable
                get_Accent: _Callable
                put_Accent: _Callable

            class IColorPaletteResourcesFactory(IInspectable):
                CreateInstance: _Callable

            class ICornerRadiusHelper(IInspectable):
                pass

            class ICornerRadiusHelperStatics(IInspectable):
                FromRadii: _Callable
                FromUniformRadius: _Callable

            class IDataContextChangedEventArgs(IInspectable):
                get_NewValue: _Callable
                get_Handled: _Callable
                put_Handled: _Callable

            class IDataTemplate(IInspectable):
                LoadContent: _Callable

            class IDataTemplateExtension(IInspectable):
                ResetTemplate: _Callable
                ProcessBinding: _Callable
                ProcessBindings: _Callable

            class IDataTemplateFactory(IInspectable):
                CreateInstance: _Callable

            class IDataTemplateKey(IInspectable):
                get_DataType: _Callable
                put_DataType: _Callable

            class IDataTemplateKeyFactory(IInspectable):
                CreateInstance: _Callable
                CreateInstanceWithType: _Callable

            class IDataTemplateStatics2(IInspectable):
                get_ExtensionInstanceProperty: _Callable
                GetExtensionInstance: _Callable
                SetExtensionInstance: _Callable

            class IDebugSettings(IInspectable):
                get_EnableFrameRateCounter: _Callable
                put_EnableFrameRateCounter: _Callable
                get_IsBindingTracingEnabled: _Callable
                put_IsBindingTracingEnabled: _Callable
                get_IsOverdrawHeatMapEnabled: _Callable
                put_IsOverdrawHeatMapEnabled: _Callable
                add_BindingFailed: _Callable
                remove_BindingFailed: _Callable

            class IDebugSettings2(IInspectable):
                get_EnableRedrawRegions: _Callable
                put_EnableRedrawRegions: _Callable

            class IDebugSettings3(IInspectable):
                get_IsTextPerformanceVisualizationEnabled: _Callable
                put_IsTextPerformanceVisualizationEnabled: _Callable

            class IDebugSettings4(IInspectable):
                get_FailFastOnErrors: _Callable
                put_FailFastOnErrors: _Callable

            class IDependencyObject(IInspectable):
                GetValue: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
                SetValue: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                     IInspectable],
                                    _type.HRESULT]
                ClearValue: _Callable[[Windows.UI.Xaml.IDependencyProperty],
                                      _type.HRESULT]
                ReadLocalValue: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                           _Pointer[IInspectable]],
                                          _type.HRESULT]
                GetAnimationBaseValue: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                                  _Pointer[IInspectable]],
                                                 _type.HRESULT]
                get_Dispatcher: _Callable

            class IDependencyObject2(IInspectable):
                RegisterPropertyChangedCallback: _Callable
                UnregisterPropertyChangedCallback: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                                              _type.INT64],
                                                             _type.HRESULT]

            class IDependencyObjectCollectionFactory(IInspectable):
                CreateInstance: _Callable

            class IDependencyObjectFactory(IInspectable):
                CreateInstance: _Callable[[IInspectable,
                                           _Pointer[IInspectable],
                                           _Pointer[Windows.UI.Xaml.IDependencyObject]],
                                          _type.HRESULT]

            class IDependencyProperty(IInspectable):
                GetMetadata: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName],
                                        _Pointer[Windows.UI.Xaml.IPropertyMetadata]],
                                       _type.HRESULT]

            class IDependencyPropertyChangedEventArgs(IInspectable):
                get_Property: _Callable
                get_OldValue: _Callable
                get_NewValue: _Callable

            class IDependencyPropertyStatics(IInspectable):
                get_UnsetValue: _Callable
                Register: _Callable
                RegisterAttached: _Callable

            class IDispatcherTimer(IInspectable):
                get_Interval: _Callable
                put_Interval: _Callable
                get_IsEnabled: _Callable
                add_Tick: _Callable
                remove_Tick: _Callable
                Start: _Callable
                Stop: _Callable

            class IDispatcherTimerFactory(IInspectable):
                CreateInstance: _Callable

            class IDragEventArgs(IInspectable):
                get_Handled: _Callable
                put_Handled: _Callable
                get_Data: _Callable
                put_Data: _Callable
                GetPosition: _Callable

            class IDragEventArgs2(IInspectable):
                get_DataView: _Callable
                get_DragUIOverride: _Callable
                get_Modifiers: _Callable
                get_AcceptedOperation: _Callable
                put_AcceptedOperation: _Callable
                GetDeferral: _Callable

            class IDragEventArgs3(IInspectable):
                get_AllowedOperations: _Callable

            class IDragOperationDeferral(IInspectable):
                Complete: _Callable

            class IDragStartingEventArgs(IInspectable):
                get_Cancel: _Callable
                put_Cancel: _Callable
                get_Data: _Callable
                get_DragUI: _Callable
                GetDeferral: _Callable
                GetPosition: _Callable

            class IDragStartingEventArgs2(IInspectable):
                get_AllowedOperations: _Callable
                put_AllowedOperations: _Callable

            class IDragUI(IInspectable):
                SetContentFromBitmapImage: _Callable
                SetContentFromBitmapImageWithAnchorPoint: _Callable
                SetContentFromSoftwareBitmap: _Callable
                SetContentFromSoftwareBitmapWithAnchorPoint: _Callable
                SetContentFromDataPackage: _Callable

            class IDragUIOverride(IInspectable):
                get_Caption: _Callable
                put_Caption: _Callable
                get_IsContentVisible: _Callable
                put_IsContentVisible: _Callable
                get_IsCaptionVisible: _Callable
                put_IsCaptionVisible: _Callable
                get_IsGlyphVisible: _Callable
                put_IsGlyphVisible: _Callable
                Clear: _Callable
                SetContentFromBitmapImage: _Callable
                SetContentFromBitmapImageWithAnchorPoint: _Callable
                SetContentFromSoftwareBitmap: _Callable
                SetContentFromSoftwareBitmapWithAnchorPoint: _Callable

            class IDropCompletedEventArgs(IInspectable):
                get_DropResult: _Callable

            class IDurationHelper(IInspectable):
                pass

            class IDurationHelperStatics(IInspectable):
                get_Automatic: _Callable
                get_Forever: _Callable
                Compare: _Callable
                FromTimeSpan: _Callable
                GetHasTimeSpan: _Callable
                Add: _Callable
                Equals: _Callable
                Subtract: _Callable

            class IEffectiveViewportChangedEventArgs(IInspectable):
                get_EffectiveViewport: _Callable
                get_MaxViewport: _Callable
                get_BringIntoViewDistanceX: _Callable
                get_BringIntoViewDistanceY: _Callable

            class IElementFactory(IInspectable):
                GetElement: _Callable
                RecycleElement: _Callable

            class IElementFactoryGetArgs(IInspectable):
                get_Data: _Callable
                put_Data: _Callable
                get_Parent: _Callable
                put_Parent: _Callable

            class IElementFactoryGetArgsFactory(IInspectable):
                CreateInstance: _Callable

            class IElementFactoryRecycleArgs(IInspectable):
                get_Element: _Callable
                put_Element: _Callable
                get_Parent: _Callable
                put_Parent: _Callable

            class IElementFactoryRecycleArgsFactory(IInspectable):
                CreateInstance: _Callable

            class IElementSoundPlayer(IInspectable):
                pass

            class IElementSoundPlayerStatics(IInspectable):
                get_Volume: _Callable
                put_Volume: _Callable
                get_State: _Callable
                put_State: _Callable
                Play: _Callable

            class IElementSoundPlayerStatics2(IInspectable):
                get_SpatialAudioMode: _Callable
                put_SpatialAudioMode: _Callable

            class IEventTrigger(IInspectable):
                get_RoutedEvent: _Callable
                put_RoutedEvent: _Callable
                get_Actions: _Callable

            class IExceptionRoutedEventArgs(IInspectable):
                get_ErrorMessage: _Callable

            class IExceptionRoutedEventArgsFactory(IInspectable):
                pass

            class IFrameworkElement(IInspectable):
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
                get_HorizontalAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],
                                                   _type.HRESULT]
                put_HorizontalAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],
                                                   _type.HRESULT]
                get_VerticalAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],
                                                 _type.HRESULT]
                put_VerticalAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],
                                                 _type.HRESULT]
                get_Margin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],
                                      _type.HRESULT]
                put_Margin: _Callable[[_struct.Windows.UI.Xaml.Thickness],
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
                get_Style: _Callable[[_Pointer[Windows.UI.Xaml.IStyle]],
                                     _type.HRESULT]
                put_Style: _Callable[[Windows.UI.Xaml.IStyle],
                                     _type.HRESULT]
                get_Parent: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyObject]],
                                      _type.HRESULT]
                get_FlowDirection: _Callable[[_Pointer[_enum.Windows.UI.Xaml.FlowDirection]],
                                             _type.HRESULT]
                put_FlowDirection: _Callable[[_enum.Windows.UI.Xaml.FlowDirection],
                                             _type.HRESULT]
                add_Loaded: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                       _Pointer[_struct.EventRegistrationToken]],
                                      _type.HRESULT]
                remove_Loaded: _Callable[[_struct.EventRegistrationToken],
                                         _type.HRESULT]
                add_Unloaded: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                         _Pointer[_struct.EventRegistrationToken]],
                                        _type.HRESULT]
                remove_Unloaded: _Callable[[_struct.EventRegistrationToken],
                                           _type.HRESULT]
                add_SizeChanged: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                            _Pointer[_struct.EventRegistrationToken]],
                                           _type.HRESULT]
                remove_SizeChanged: _Callable[[_struct.EventRegistrationToken],
                                              _type.HRESULT]
                add_LayoutUpdated: _Callable[[Windows.Foundation.IEventHandler_impl[IInspectable],
                                              _Pointer[_struct.EventRegistrationToken]],
                                             _type.HRESULT]
                remove_LayoutUpdated: _Callable[[_struct.EventRegistrationToken],
                                                _type.HRESULT]
                FindName: _Callable[[_type.HSTRING,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
                SetBinding: _Callable

            class IFrameworkElement2(IInspectable):
                get_RequestedTheme: _Callable
                put_RequestedTheme: _Callable
                add_DataContextChanged: _Callable
                remove_DataContextChanged: _Callable
                GetBindingExpression: _Callable

            class IFrameworkElement3(IInspectable):
                add_Loading: _Callable
                remove_Loading: _Callable

            class IFrameworkElement4(IInspectable):
                get_AllowFocusOnInteraction: _Callable
                put_AllowFocusOnInteraction: _Callable
                get_FocusVisualMargin: _Callable
                put_FocusVisualMargin: _Callable
                get_FocusVisualSecondaryThickness: _Callable
                put_FocusVisualSecondaryThickness: _Callable
                get_FocusVisualPrimaryThickness: _Callable
                put_FocusVisualPrimaryThickness: _Callable
                get_FocusVisualSecondaryBrush: _Callable
                put_FocusVisualSecondaryBrush: _Callable
                get_FocusVisualPrimaryBrush: _Callable
                put_FocusVisualPrimaryBrush: _Callable
                get_AllowFocusWhenDisabled: _Callable
                put_AllowFocusWhenDisabled: _Callable

            class IFrameworkElement6(IInspectable):
                get_ActualTheme: _Callable
                add_ActualThemeChanged: _Callable
                remove_ActualThemeChanged: _Callable

            class IFrameworkElement7(IInspectable):
                get_IsLoaded: _Callable
                add_EffectiveViewportChanged: _Callable
                remove_EffectiveViewportChanged: _Callable

            class IFrameworkElementFactory(IInspectable):
                CreateInstance: _Callable

            class IFrameworkElementOverrides(IInspectable):
                MeasureOverride: _Callable
                ArrangeOverride: _Callable
                OnApplyTemplate: _Callable

            class IFrameworkElementOverrides2(IInspectable):
                GoToElementStateCore: _Callable

            class IFrameworkElementProtected7(IInspectable):
                InvalidateViewport: _Callable

            class IFrameworkElementStatics(IInspectable):
                get_TagProperty: _Callable
                get_LanguageProperty: _Callable
                get_ActualWidthProperty: _Callable
                get_ActualHeightProperty: _Callable
                get_WidthProperty: _Callable
                get_HeightProperty: _Callable
                get_MinWidthProperty: _Callable
                get_MaxWidthProperty: _Callable
                get_MinHeightProperty: _Callable
                get_MaxHeightProperty: _Callable
                get_HorizontalAlignmentProperty: _Callable
                get_VerticalAlignmentProperty: _Callable
                get_MarginProperty: _Callable
                get_NameProperty: _Callable
                get_DataContextProperty: _Callable
                get_StyleProperty: _Callable
                get_FlowDirectionProperty: _Callable

            class IFrameworkElementStatics2(IInspectable):
                get_RequestedThemeProperty: _Callable

            class IFrameworkElementStatics4(IInspectable):
                get_AllowFocusOnInteractionProperty: _Callable
                get_FocusVisualMarginProperty: _Callable
                get_FocusVisualSecondaryThicknessProperty: _Callable
                get_FocusVisualPrimaryThicknessProperty: _Callable
                get_FocusVisualSecondaryBrushProperty: _Callable
                get_FocusVisualPrimaryBrushProperty: _Callable
                get_AllowFocusWhenDisabledProperty: _Callable

            class IFrameworkElementStatics5(IInspectable):
                DeferTree: _Callable

            class IFrameworkElementStatics6(IInspectable):
                get_ActualThemeProperty: _Callable

            class IFrameworkTemplate(IInspectable):
                pass

            class IFrameworkTemplateFactory(IInspectable):
                CreateInstance: _Callable

            class IFrameworkView(IInspectable):
                pass

            class IFrameworkViewSource(IInspectable):
                pass

            class IGridLengthHelper(IInspectable):
                pass

            class IGridLengthHelperStatics(IInspectable):
                get_Auto: _Callable
                FromPixels: _Callable
                FromValueAndType: _Callable
                GetIsAbsolute: _Callable
                GetIsAuto: _Callable
                GetIsStar: _Callable
                Equals: _Callable

            class IMediaFailedRoutedEventArgs(IInspectable):
                get_ErrorTrace: _Callable

            class IPointHelper(IInspectable):
                pass

            class IPointHelperStatics(IInspectable):
                FromCoordinates: _Callable

            class IPropertyMetadata(IInspectable):
                get_DefaultValue: _Callable[[_Pointer[IInspectable]],
                                            _type.HRESULT]
                get_CreateDefaultValueCallback: _Callable[[_Pointer[Windows.UI.Xaml.ICreateDefaultValueCallback]],
                                                          _type.HRESULT]

            class IPropertyMetadataFactory(IInspectable):
                CreateInstanceWithDefaultValue: _Callable
                CreateInstanceWithDefaultValueAndCallback: _Callable

            class IPropertyMetadataStatics(IInspectable):
                CreateWithDefaultValue: _Callable
                CreateWithDefaultValueAndCallback: _Callable
                CreateWithFactory: _Callable
                CreateWithFactoryAndCallback: _Callable

            class IPropertyPath(IInspectable):
                get_Path: _Callable[[_Pointer[_type.HSTRING]],
                                    _type.HRESULT]

            class IPropertyPathFactory(IInspectable):
                CreateInstance: _Callable[[_type.HSTRING,
                                           _Pointer[Windows.UI.Xaml.IPropertyPath]],
                                          _type.HRESULT]

            class IRectHelper(IInspectable):
                pass

            class IRectHelperStatics(IInspectable):
                get_Empty: _Callable
                FromCoordinatesAndDimensions: _Callable
                FromPoints: _Callable
                FromLocationAndSize: _Callable
                GetIsEmpty: _Callable
                GetBottom: _Callable
                GetLeft: _Callable
                GetRight: _Callable
                GetTop: _Callable
                Contains: _Callable
                Equals: _Callable
                Intersect: _Callable
                UnionWithPoint: _Callable
                UnionWithRect: _Callable

            class IResourceDictionary(IInspectable):
                get_Source: _Callable
                put_Source: _Callable
                get_MergedDictionaries: _Callable
                get_ThemeDictionaries: _Callable

            class IResourceDictionaryFactory(IInspectable):
                CreateInstance: _Callable

            class IRoutedEvent(IInspectable):
                pass

            class IRoutedEventArgs(IInspectable):
                get_OriginalSource: _Callable[[_Pointer[IInspectable]],
                                              _type.HRESULT]

            class IRoutedEventArgsFactory(IInspectable):
                CreateInstance: _Callable[[IInspectable,
                                           _Pointer[IInspectable],
                                           _Pointer[Windows.UI.Xaml.IRoutedEventArgs]],
                                          _type.HRESULT]

            class IScalarTransition(IInspectable):
                get_Duration: _Callable
                put_Duration: _Callable

            class IScalarTransitionFactory(IInspectable):
                CreateInstance: _Callable

            class ISetter(IInspectable):
                get_Property: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                        _type.HRESULT]
                put_Property: _Callable[[Windows.UI.Xaml.IDependencyProperty],
                                        _type.HRESULT]
                get_Value: _Callable[[_Pointer[IInspectable]],
                                     _type.HRESULT]
                put_Value: _Callable[[IInspectable],
                                     _type.HRESULT]

            class ISetter2(IInspectable):
                get_Target: _Callable
                put_Target: _Callable

            class ISetterBase(IInspectable):
                get_IsSealed: _Callable[[_Pointer[_type.boolean]],
                                        _type.HRESULT]

            class ISetterBaseCollection(IInspectable):
                get_IsSealed: _Callable[[_Pointer[_type.boolean]],
                                        _type.HRESULT]

            class ISetterBaseFactory(IInspectable):
                pass

            class ISetterFactory(IInspectable):
                CreateInstance: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                           IInspectable,
                                           _Pointer[Windows.UI.Xaml.ISetter]],
                                          _type.HRESULT]

            class ISizeChangedEventArgs(IInspectable):
                get_PreviousSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                            _type.HRESULT]
                get_NewSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                       _type.HRESULT]

            class ISizeHelper(IInspectable):
                pass

            class ISizeHelperStatics(IInspectable):
                get_Empty: _Callable
                FromDimensions: _Callable
                GetIsEmpty: _Callable
                Equals: _Callable

            class IStateTrigger(IInspectable):
                get_IsActive: _Callable
                put_IsActive: _Callable

            class IStateTriggerBase(IInspectable):
                pass

            class IStateTriggerBaseFactory(IInspectable):
                CreateInstance: _Callable

            class IStateTriggerBaseProtected(IInspectable):
                SetActive: _Callable

            class IStateTriggerStatics(IInspectable):
                get_IsActiveProperty: _Callable

            class IStyle(IInspectable):
                get_IsSealed: _Callable[[_Pointer[_type.boolean]],
                                        _type.HRESULT]
                get_Setters: _Callable[[_Pointer[Windows.UI.Xaml.ISetterBaseCollection]],
                                       _type.HRESULT]
                get_TargetType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],
                                          _type.HRESULT]
                put_TargetType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName],
                                          _type.HRESULT]
                get_BasedOn: _Callable[[_Pointer[Windows.UI.Xaml.IStyle]],
                                       _type.HRESULT]
                put_BasedOn: _Callable[[Windows.UI.Xaml.IStyle],
                                       _type.HRESULT]
                Seal: _Callable[[],
                                _type.HRESULT]

            class IStyleFactory(IInspectable):
                CreateInstance: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,
                                           _Pointer[Windows.UI.Xaml.IStyle]],
                                          _type.HRESULT]

            class ITargetPropertyPath(IInspectable):
                get_Path: _Callable[[_Pointer[Windows.UI.Xaml.IPropertyPath]],
                                    _type.HRESULT]
                put_Path: _Callable[[Windows.UI.Xaml.IPropertyPath],
                                    _type.HRESULT]
                get_Target: _Callable[[_Pointer[IInspectable]],
                                      _type.HRESULT]
                put_Target: _Callable[[IInspectable],
                                      _type.HRESULT]

            class ITargetPropertyPathFactory(IInspectable):
                CreateInstance: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                           _Pointer[Windows.UI.Xaml.ITargetPropertyPath]],
                                          _type.HRESULT]

            class IThicknessHelper(IInspectable):
                pass

            class IThicknessHelperStatics(IInspectable):
                FromLengths: _Callable
                FromUniformLength: _Callable

            class ITriggerAction(IInspectable):
                pass

            class ITriggerActionFactory(IInspectable):
                pass

            class ITriggerBase(IInspectable):
                pass

            class ITriggerBaseFactory(IInspectable):
                pass

            class IUIElement(IInspectable):
                get_DesiredSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                           _type.HRESULT]
                get_AllowDrop: _Callable[[_Pointer[_type.boolean]],
                                         _type.HRESULT]
                put_AllowDrop: _Callable[[_type.boolean],
                                         _type.HRESULT]
                get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],
                                       _type.HRESULT]
                put_Opacity: _Callable[[_type.DOUBLE],
                                       _type.HRESULT]
                get_Clip: _Callable[[_Pointer[Windows.UI.Xaml.Media.IRectangleGeometry]],
                                    _type.HRESULT]
                put_Clip: _Callable[[Windows.UI.Xaml.Media.IRectangleGeometry],
                                    _type.HRESULT]
                get_RenderTransform: _Callable[[_Pointer[Windows.UI.Xaml.Media.ITransform]],
                                               _type.HRESULT]
                put_RenderTransform: _Callable[[Windows.UI.Xaml.Media.ITransform],
                                               _type.HRESULT]
                get_Projection: _Callable[[_Pointer[Windows.UI.Xaml.Media.IProjection]],
                                          _type.HRESULT]
                put_Projection: _Callable[[Windows.UI.Xaml.Media.ITransform],
                                          _type.HRESULT]
                get_RenderTransformOrigin: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],
                                                     _type.HRESULT]
                put_RenderTransformOrigin: _Callable[[_struct.Windows.Foundation.Point],
                                                     _type.HRESULT]
                get_IsHitTestVisible: _Callable[[_Pointer[_type.boolean]],
                                                _type.HRESULT]
                put_IsHitTestVisible: _Callable[[_type.boolean],
                                                _type.HRESULT]
                get_Visibility: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Visibility]],
                                          _type.HRESULT]
                put_Visibility: _Callable[[_enum.Windows.UI.Xaml.Visibility],
                                          _type.HRESULT]
                get_RenderSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                          _type.HRESULT]
                get_UseLayoutRounding: _Callable[[_Pointer[_type.boolean]],
                                                 _type.HRESULT]
                put_UseLayoutRounding: _Callable[[_type.boolean],
                                                 _type.HRESULT]
                get_Transitions: _Callable[[_Pointer[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ITransition]]],
                                           _type.HRESULT]
                put_Transitions: _Callable[[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ITransition]],
                                           _type.HRESULT]
                get_CacheMode: _Callable[[_Pointer[Windows.UI.Xaml.Media.ICacheMode]],
                                         _type.HRESULT]
                put_CacheMode: _Callable[[Windows.UI.Xaml.Media.ICacheMode],
                                         _type.HRESULT]
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
                get_ManipulationMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Input.ManipulationModes]],
                                                _type.HRESULT]
                put_ManipulationMode: _Callable[[_enum.Windows.UI.Xaml.Input.ManipulationModes],
                                                _type.HRESULT]
                get_PointerCaptures: _Callable[[_Pointer[Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Input.IPointer]]],
                                               _type.HRESULT]
                add_KeyUp: _Callable[[Windows.UI.Xaml.Input.IKeyEventHandler_impl,
                                      _Pointer[_struct.EventRegistrationToken]],
                                     _type.HRESULT]
                remove_KeyUp: _Callable[[_struct.EventRegistrationToken],
                                        _type.HRESULT]
                add_KeyDown: _Callable[[Windows.UI.Xaml.Input.IKeyEventHandler_impl,
                                        _Pointer[_struct.EventRegistrationToken]],
                                       _type.HRESULT]
                remove_KeyDown: _Callable[[_struct.EventRegistrationToken],
                                          _type.HRESULT]
                add_GotFocus: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                         _Pointer[_struct.EventRegistrationToken]],
                                        _type.HRESULT]
                remove_GotFocus: _Callable[[_struct.EventRegistrationToken],
                                           _type.HRESULT]
                add_LostFocus: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_LostFocus: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_DragEnter: _Callable[[Windows.UI.Xaml.IDragEventHandler_impl,
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_DragEnter: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_DragLeave: _Callable[[Windows.UI.Xaml.IDragEventHandler_impl,
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_DragLeave: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_DragOver: _Callable[[Windows.UI.Xaml.IDragEventHandler_impl,
                                         _Pointer[_struct.EventRegistrationToken]],
                                        _type.HRESULT]
                remove_DragOver: _Callable[[_struct.EventRegistrationToken],
                                           _type.HRESULT]
                add_Drop: _Callable[[Windows.UI.Xaml.IDragEventHandler_impl,
                                     _Pointer[_struct.EventRegistrationToken]],
                                    _type.HRESULT]
                remove_Drop: _Callable[[_struct.EventRegistrationToken],
                                       _type.HRESULT]
                add_PointerPressed: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                               _Pointer[_struct.EventRegistrationToken]],
                                              _type.HRESULT]
                remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],
                                                 _type.HRESULT]
                add_PointerMoved: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                             _Pointer[_struct.EventRegistrationToken]],
                                            _type.HRESULT]
                remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],
                                               _type.HRESULT]
                add_PointerReleased: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                                _Pointer[_struct.EventRegistrationToken]],
                                               _type.HRESULT]
                remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],
                                                  _type.HRESULT]
                add_PointerEntered: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                               _Pointer[_struct.EventRegistrationToken]],
                                              _type.HRESULT]
                remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],
                                                 _type.HRESULT]
                add_PointerExited: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                              _Pointer[_struct.EventRegistrationToken]],
                                             _type.HRESULT]
                remove_PointerExited: _Callable[[_struct.EventRegistrationToken],
                                                _type.HRESULT]
                add_PointerCaptureLost: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                                   _Pointer[_struct.EventRegistrationToken]],
                                                  _type.HRESULT]
                remove_PointerCaptureLost: _Callable[[_struct.EventRegistrationToken],
                                                     _type.HRESULT]
                add_PointerCanceled: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                                _Pointer[_struct.EventRegistrationToken]],
                                               _type.HRESULT]
                remove_PointerCanceled: _Callable[[_struct.EventRegistrationToken],
                                                  _type.HRESULT]
                add_PointerWheelChanged: _Callable[[Windows.UI.Xaml.Input.IPointerEventHandler_impl,
                                                    _Pointer[_struct.EventRegistrationToken]],
                                                   _type.HRESULT]
                remove_PointerWheelChanged: _Callable[[_struct.EventRegistrationToken],
                                                      _type.HRESULT]
                add_Tapped: _Callable[[Windows.UI.Xaml.Input.ITappedEventHandler_impl,
                                       _Pointer[_struct.EventRegistrationToken]],
                                      _type.HRESULT]
                remove_Tapped: _Callable[[_struct.EventRegistrationToken],
                                         _type.HRESULT]
                add_DoubleTapped: _Callable[[Windows.UI.Xaml.Input.IDoubleTappedEventHandler_impl,
                                             _Pointer[_struct.EventRegistrationToken]],
                                            _type.HRESULT]
                remove_DoubleTapped: _Callable[[_struct.EventRegistrationToken],
                                               _type.HRESULT]
                add_Holding: _Callable[[Windows.UI.Xaml.Input.IHoldingEventHandler_impl,
                                        _Pointer[_struct.EventRegistrationToken]],
                                       _type.HRESULT]
                remove_Holding: _Callable[[_struct.EventRegistrationToken],
                                          _type.HRESULT]
                add_RightTapped: _Callable[[Windows.UI.Xaml.Input.IRightTappedEventHandler_impl,
                                            _Pointer[_struct.EventRegistrationToken]],
                                           _type.HRESULT]
                remove_RightTapped: _Callable[[_struct.EventRegistrationToken],
                                              _type.HRESULT]
                add_ManipulationStarting: _Callable[[Windows.UI.Xaml.Input.IManipulationStartingEventHandler_impl,
                                                     _Pointer[_struct.EventRegistrationToken]],
                                                    _type.HRESULT]
                remove_ManipulationStarting: _Callable[[_struct.EventRegistrationToken],
                                                       _type.HRESULT]
                add_ManipulationInertiaStarting: _Callable[[Windows.UI.Xaml.Input.IManipulationInertiaStartingEventHandler_impl,
                                                            _Pointer[_struct.EventRegistrationToken]],
                                                           _type.HRESULT]
                remove_ManipulationInertiaStarting: _Callable[[_struct.EventRegistrationToken],
                                                              _type.HRESULT]
                add_ManipulationStarted: _Callable[[Windows.UI.Xaml.Input.IManipulationStartedEventHandler_impl,
                                                    _Pointer[_struct.EventRegistrationToken]],
                                                   _type.HRESULT]
                remove_ManipulationStarted: _Callable[[_struct.EventRegistrationToken],
                                                      _type.HRESULT]
                add_ManipulationDelta: _Callable[[Windows.UI.Xaml.Input.IManipulationDeltaEventHandler_impl,
                                                  _Pointer[_struct.EventRegistrationToken]],
                                                 _type.HRESULT]
                remove_ManipulationDelta: _Callable[[_struct.EventRegistrationToken],
                                                    _type.HRESULT]
                add_ManipulationCompleted: _Callable[[Windows.UI.Xaml.Input.IManipulationCompletedEventHandler_impl,
                                                      _Pointer[_struct.EventRegistrationToken]],
                                                     _type.HRESULT]
                remove_ManipulationCompleted: _Callable[[_struct.EventRegistrationToken],
                                                        _type.HRESULT]
                Measure: _Callable[[_struct.Windows.Foundation.Size],
                                   _type.HRESULT]
                Arrange: _Callable[[_struct.Windows.Foundation.Rect],
                                   _type.HRESULT]
                CapturePointer: _Callable[[Windows.UI.Xaml.Input.IPointer,
                                           _Pointer[_type.boolean]],
                                          _type.HRESULT]
                ReleasePointerCapture: _Callable[[Windows.UI.Xaml.Input.IPointer],
                                                 _type.HRESULT]
                ReleasePointerCaptures: _Callable[[],
                                                  _type.HRESULT]
                AddHandler: _Callable[[Windows.UI.Xaml.IRoutedEvent,
                                       IInspectable,
                                       _type.boolean],
                                      _type.HRESULT]
                RemoveHandler: _Callable[[Windows.UI.Xaml.IRoutedEvent,
                                          IInspectable],
                                         _type.HRESULT]
                TransformToVisual: _Callable[[Windows.UI.Xaml.IUIElement,
                                              _Pointer[Windows.UI.Xaml.Media.IGeneralTransform]],
                                             _type.HRESULT]
                InvalidateMeasure: _Callable[[],
                                             _type.HRESULT]
                InvalidateArrange: _Callable[[],
                                             _type.HRESULT]
                UpdateLayout: _Callable[[],
                                        _type.HRESULT]

            class IUIElement10(IInspectable):
                get_ActualOffset: _Callable
                get_ActualSize: _Callable
                get_XamlRoot: _Callable
                put_XamlRoot: _Callable
                get_UIContext: _Callable
                get_Shadow: _Callable
                put_Shadow: _Callable

            class IUIElement2(IInspectable):
                get_CompositeMode: _Callable
                put_CompositeMode: _Callable
                CancelDirectManipulations: _Callable

            class IUIElement3(IInspectable):
                get_Transform3D: _Callable
                put_Transform3D: _Callable
                get_CanDrag: _Callable
                put_CanDrag: _Callable
                add_DragStarting: _Callable
                remove_DragStarting: _Callable
                add_DropCompleted: _Callable
                remove_DropCompleted: _Callable
                StartDragAsync: _Callable

            class IUIElement4(IInspectable):
                get_ContextFlyout: _Callable
                put_ContextFlyout: _Callable
                get_ExitDisplayModeOnAccessKeyInvoked: _Callable
                put_ExitDisplayModeOnAccessKeyInvoked: _Callable
                get_IsAccessKeyScope: _Callable
                put_IsAccessKeyScope: _Callable
                get_AccessKeyScopeOwner: _Callable
                put_AccessKeyScopeOwner: _Callable
                get_AccessKey: _Callable
                put_AccessKey: _Callable
                add_ContextRequested: _Callable
                remove_ContextRequested: _Callable
                add_ContextCanceled: _Callable
                remove_ContextCanceled: _Callable
                add_AccessKeyDisplayRequested: _Callable
                remove_AccessKeyDisplayRequested: _Callable
                add_AccessKeyDisplayDismissed: _Callable
                remove_AccessKeyDisplayDismissed: _Callable
                add_AccessKeyInvoked: _Callable
                remove_AccessKeyInvoked: _Callable

            class IUIElement5(IInspectable):
                get_Lights: _Callable
                get_KeyTipPlacementMode: _Callable
                put_KeyTipPlacementMode: _Callable
                get_KeyTipHorizontalOffset: _Callable
                put_KeyTipHorizontalOffset: _Callable
                get_KeyTipVerticalOffset: _Callable
                put_KeyTipVerticalOffset: _Callable
                get_XYFocusKeyboardNavigation: _Callable
                put_XYFocusKeyboardNavigation: _Callable
                get_XYFocusUpNavigationStrategy: _Callable
                put_XYFocusUpNavigationStrategy: _Callable
                get_XYFocusDownNavigationStrategy: _Callable
                put_XYFocusDownNavigationStrategy: _Callable
                get_XYFocusLeftNavigationStrategy: _Callable
                put_XYFocusLeftNavigationStrategy: _Callable
                get_XYFocusRightNavigationStrategy: _Callable
                put_XYFocusRightNavigationStrategy: _Callable
                get_HighContrastAdjustment: _Callable
                put_HighContrastAdjustment: _Callable
                get_TabFocusNavigation: _Callable
                put_TabFocusNavigation: _Callable
                add_GettingFocus: _Callable
                remove_GettingFocus: _Callable
                add_LosingFocus: _Callable
                remove_LosingFocus: _Callable
                add_NoFocusCandidateFound: _Callable
                remove_NoFocusCandidateFound: _Callable
                StartBringIntoView: _Callable
                StartBringIntoViewWithOptions: _Callable

            class IUIElement7(IInspectable):
                get_KeyboardAccelerators: _Callable
                add_CharacterReceived: _Callable
                remove_CharacterReceived: _Callable
                add_ProcessKeyboardAccelerators: _Callable
                remove_ProcessKeyboardAccelerators: _Callable
                add_PreviewKeyDown: _Callable
                remove_PreviewKeyDown: _Callable
                add_PreviewKeyUp: _Callable
                remove_PreviewKeyUp: _Callable
                TryInvokeKeyboardAccelerator: _Callable

            class IUIElement8(IInspectable):
                get_KeyTipTarget: _Callable
                put_KeyTipTarget: _Callable
                get_KeyboardAcceleratorPlacementTarget: _Callable
                put_KeyboardAcceleratorPlacementTarget: _Callable
                get_KeyboardAcceleratorPlacementMode: _Callable
                put_KeyboardAcceleratorPlacementMode: _Callable
                add_BringIntoViewRequested: _Callable
                remove_BringIntoViewRequested: _Callable

            class IUIElement9(IInspectable):
                get_CanBeScrollAnchor: _Callable
                put_CanBeScrollAnchor: _Callable
                get_OpacityTransition: _Callable
                put_OpacityTransition: _Callable
                get_Translation: _Callable
                put_Translation: _Callable
                get_TranslationTransition: _Callable
                put_TranslationTransition: _Callable
                get_Rotation: _Callable
                put_Rotation: _Callable
                get_RotationTransition: _Callable
                put_RotationTransition: _Callable
                get_Scale: _Callable
                put_Scale: _Callable
                get_ScaleTransition: _Callable
                put_ScaleTransition: _Callable
                get_TransformMatrix: _Callable
                put_TransformMatrix: _Callable
                get_CenterPoint: _Callable
                put_CenterPoint: _Callable
                get_RotationAxis: _Callable
                put_RotationAxis: _Callable
                StartAnimation: _Callable
                StopAnimation: _Callable

            class IUIElementFactory(IInspectable):
                pass

            class IUIElementOverrides(IInspectable):
                OnCreateAutomationPeer: _Callable
                OnDisconnectVisualChildren: _Callable
                FindSubElementsForTouchTargeting: _Callable

            class IUIElementOverrides7(IInspectable):
                GetChildrenInTabFocusOrder: _Callable
                OnProcessKeyboardAccelerators: _Callable

            class IUIElementOverrides8(IInspectable):
                OnKeyboardAcceleratorInvoked: _Callable
                OnBringIntoViewRequested: _Callable

            class IUIElementOverrides9(IInspectable):
                PopulatePropertyInfoOverride: _Callable

            class IUIElementStatics(IInspectable):
                get_KeyDownEvent: _Callable
                get_KeyUpEvent: _Callable
                get_PointerEnteredEvent: _Callable
                get_PointerPressedEvent: _Callable
                get_PointerMovedEvent: _Callable
                get_PointerReleasedEvent: _Callable
                get_PointerExitedEvent: _Callable
                get_PointerCaptureLostEvent: _Callable
                get_PointerCanceledEvent: _Callable
                get_PointerWheelChangedEvent: _Callable
                get_TappedEvent: _Callable
                get_DoubleTappedEvent: _Callable
                get_HoldingEvent: _Callable
                get_RightTappedEvent: _Callable
                get_ManipulationStartingEvent: _Callable
                get_ManipulationInertiaStartingEvent: _Callable
                get_ManipulationStartedEvent: _Callable
                get_ManipulationDeltaEvent: _Callable
                get_ManipulationCompletedEvent: _Callable
                get_DragEnterEvent: _Callable
                get_DragLeaveEvent: _Callable
                get_DragOverEvent: _Callable
                get_DropEvent: _Callable
                get_AllowDropProperty: _Callable
                get_OpacityProperty: _Callable
                get_ClipProperty: _Callable
                get_RenderTransformProperty: _Callable
                get_ProjectionProperty: _Callable
                get_RenderTransformOriginProperty: _Callable
                get_IsHitTestVisibleProperty: _Callable
                get_VisibilityProperty: _Callable
                get_UseLayoutRoundingProperty: _Callable
                get_TransitionsProperty: _Callable
                get_CacheModeProperty: _Callable
                get_IsTapEnabledProperty: _Callable
                get_IsDoubleTapEnabledProperty: _Callable
                get_IsRightTapEnabledProperty: _Callable
                get_IsHoldingEnabledProperty: _Callable
                get_ManipulationModeProperty: _Callable
                get_PointerCapturesProperty: _Callable

            class IUIElementStatics10(IInspectable):
                get_ShadowProperty: _Callable

            class IUIElementStatics2(IInspectable):
                get_CompositeModeProperty: _Callable

            class IUIElementStatics3(IInspectable):
                get_Transform3DProperty: _Callable
                get_CanDragProperty: _Callable
                TryStartDirectManipulation: _Callable

            class IUIElementStatics4(IInspectable):
                get_ContextFlyoutProperty: _Callable
                get_ExitDisplayModeOnAccessKeyInvokedProperty: _Callable
                get_IsAccessKeyScopeProperty: _Callable
                get_AccessKeyScopeOwnerProperty: _Callable
                get_AccessKeyProperty: _Callable

            class IUIElementStatics5(IInspectable):
                get_LightsProperty: _Callable
                get_KeyTipPlacementModeProperty: _Callable
                get_KeyTipHorizontalOffsetProperty: _Callable
                get_KeyTipVerticalOffsetProperty: _Callable
                get_XYFocusKeyboardNavigationProperty: _Callable
                get_XYFocusUpNavigationStrategyProperty: _Callable
                get_XYFocusDownNavigationStrategyProperty: _Callable
                get_XYFocusLeftNavigationStrategyProperty: _Callable
                get_XYFocusRightNavigationStrategyProperty: _Callable
                get_HighContrastAdjustmentProperty: _Callable
                get_TabFocusNavigationProperty: _Callable

            class IUIElementStatics6(IInspectable):
                get_GettingFocusEvent: _Callable
                get_LosingFocusEvent: _Callable
                get_NoFocusCandidateFoundEvent: _Callable

            class IUIElementStatics7(IInspectable):
                get_PreviewKeyDownEvent: _Callable
                get_CharacterReceivedEvent: _Callable
                get_PreviewKeyUpEvent: _Callable

            class IUIElementStatics8(IInspectable):
                get_BringIntoViewRequestedEvent: _Callable
                get_ContextRequestedEvent: _Callable
                get_KeyTipTargetProperty: _Callable
                get_KeyboardAcceleratorPlacementTargetProperty: _Callable
                get_KeyboardAcceleratorPlacementModeProperty: _Callable
                RegisterAsScrollPort: _Callable

            class IUIElementStatics9(IInspectable):
                get_CanBeScrollAnchorProperty: _Callable

            class IUIElementWeakCollection(IInspectable):
                pass

            class IUIElementWeakCollectionFactory(IInspectable):
                CreateInstance: _Callable

            class IUnhandledExceptionEventArgs(IInspectable):
                get_Exception: _Callable
                get_Message: _Callable
                get_Handled: _Callable
                put_Handled: _Callable

            class IVector3Transition(IInspectable):
                get_Duration: _Callable
                put_Duration: _Callable
                get_Components: _Callable
                put_Components: _Callable

            class IVector3TransitionFactory(IInspectable):
                CreateInstance: _Callable

            class IVisualState(IInspectable):
                get_Name: _Callable
                get_Storyboard: _Callable
                put_Storyboard: _Callable

            class IVisualState2(IInspectable):
                get_Setters: _Callable
                get_StateTriggers: _Callable

            class IVisualStateChangedEventArgs(IInspectable):
                get_OldState: _Callable
                put_OldState: _Callable
                get_NewState: _Callable
                put_NewState: _Callable
                get_Control: _Callable
                put_Control: _Callable

            class IVisualStateGroup(IInspectable):
                get_Name: _Callable
                get_Transitions: _Callable
                get_States: _Callable
                get_CurrentState: _Callable
                add_CurrentStateChanged: _Callable
                remove_CurrentStateChanged: _Callable
                add_CurrentStateChanging: _Callable
                remove_CurrentStateChanging: _Callable

            class IVisualStateManager(IInspectable):
                pass

            class IVisualStateManagerFactory(IInspectable):
                CreateInstance: _Callable

            class IVisualStateManagerOverrides(IInspectable):
                GoToStateCore: _Callable

            class IVisualStateManagerProtected(IInspectable):
                RaiseCurrentStateChanging: _Callable
                RaiseCurrentStateChanged: _Callable

            class IVisualStateManagerStatics(IInspectable):
                GetVisualStateGroups: _Callable
                get_CustomVisualStateManagerProperty: _Callable
                GetCustomVisualStateManager: _Callable
                SetCustomVisualStateManager: _Callable
                GoToState: _Callable

            class IVisualTransition(IInspectable):
                get_GeneratedDuration: _Callable
                put_GeneratedDuration: _Callable
                get_GeneratedEasingFunction: _Callable
                put_GeneratedEasingFunction: _Callable
                get_To: _Callable
                put_To: _Callable
                get_From: _Callable
                put_From: _Callable
                get_Storyboard: _Callable
                put_Storyboard: _Callable

            class IVisualTransitionFactory(IInspectable):
                CreateInstance: _Callable

            class IWindow(IInspectable):
                get_Bounds: _Callable
                get_Visible: _Callable
                get_Content: _Callable
                put_Content: _Callable
                get_CoreWindow: _Callable
                get_Dispatcher: _Callable
                add_Activated: _Callable
                remove_Activated: _Callable
                add_Closed: _Callable
                remove_Closed: _Callable
                add_SizeChanged: _Callable
                remove_SizeChanged: _Callable
                add_VisibilityChanged: _Callable
                remove_VisibilityChanged: _Callable
                Activate: _Callable
                Close: _Callable

            class IWindow2(IInspectable):
                SetTitleBar: _Callable

            class IWindow3(IInspectable):
                get_Compositor: _Callable

            class IWindow4(IInspectable):
                get_UIContext: _Callable

            class IWindowCreatedEventArgs(IInspectable):
                get_Window: _Callable

            class IWindowStatics(IInspectable):
                get_Current: _Callable

            class IXamlRoot(IInspectable):
                get_Content: _Callable
                get_Size: _Callable
                get_RasterizationScale: _Callable
                get_IsHostVisible: _Callable
                get_UIContext: _Callable
                add_Changed: _Callable
                remove_Changed: _Callable

            class IXamlRootChangedEventArgs(IInspectable):
                pass

            class Controls:
                class _IBackClickEventHandler:
                    Invoke: _Callable

                class IBackClickEventHandler(_IBackClickEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IBackClickEventHandler_impl(_IBackClickEventHandler, IUnknown_impl):
                    pass

                class _ICalendarViewDayItemChangingEventHandler:
                    Invoke: _Callable

                class ICalendarViewDayItemChangingEventHandler(_ICalendarViewDayItemChangingEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ICalendarViewDayItemChangingEventHandler_impl(_ICalendarViewDayItemChangingEventHandler, IUnknown_impl):
                    pass

                class _ICleanUpVirtualizedItemEventHandler:
                    Invoke: _Callable

                class ICleanUpVirtualizedItemEventHandler(_ICleanUpVirtualizedItemEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ICleanUpVirtualizedItemEventHandler_impl(_ICleanUpVirtualizedItemEventHandler, IUnknown_impl):
                    pass

                class _IContextMenuOpeningEventHandler:
                    Invoke: _Callable

                class IContextMenuOpeningEventHandler(_IContextMenuOpeningEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IContextMenuOpeningEventHandler_impl(_IContextMenuOpeningEventHandler, IUnknown_impl):
                    pass

                class _IDragItemsStartingEventHandler:
                    Invoke: _Callable

                class IDragItemsStartingEventHandler(_IDragItemsStartingEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IDragItemsStartingEventHandler_impl(_IDragItemsStartingEventHandler, IUnknown_impl):
                    pass

                class _IHubSectionHeaderClickEventHandler:
                    Invoke: _Callable

                class IHubSectionHeaderClickEventHandler(_IHubSectionHeaderClickEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IHubSectionHeaderClickEventHandler_impl(_IHubSectionHeaderClickEventHandler, IUnknown_impl):
                    pass

                class _IItemClickEventHandler:
                    Invoke: _Callable

                class IItemClickEventHandler(_IItemClickEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IItemClickEventHandler_impl(_IItemClickEventHandler, IUnknown_impl):
                    pass

                class _IListViewItemToKeyHandler:
                    Invoke: _Callable

                class IListViewItemToKeyHandler(_IListViewItemToKeyHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IListViewItemToKeyHandler_impl(_IListViewItemToKeyHandler, IUnknown_impl):
                    pass

                class _IListViewKeyToItemHandler:
                    Invoke: _Callable

                class IListViewKeyToItemHandler(_IListViewKeyToItemHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IListViewKeyToItemHandler_impl(_IListViewKeyToItemHandler, IUnknown_impl):
                    pass

                class _INotifyEventHandler:
                    Invoke: _Callable

                class INotifyEventHandler(_INotifyEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class INotifyEventHandler_impl(_INotifyEventHandler, IUnknown_impl):
                    pass

                class _ISectionsInViewChangedEventHandler:
                    Invoke: _Callable

                class ISectionsInViewChangedEventHandler(_ISectionsInViewChangedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ISectionsInViewChangedEventHandler_impl(_ISectionsInViewChangedEventHandler, IUnknown_impl):
                    pass

                class _ISelectionChangedEventHandler:
                    Invoke: _Callable

                class ISelectionChangedEventHandler(_ISelectionChangedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ISelectionChangedEventHandler_impl(_ISelectionChangedEventHandler, IUnknown_impl):
                    pass

                class _ISemanticZoomViewChangedEventHandler:
                    Invoke: _Callable

                class ISemanticZoomViewChangedEventHandler(_ISemanticZoomViewChangedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ISemanticZoomViewChangedEventHandler_impl(_ISemanticZoomViewChangedEventHandler, IUnknown_impl):
                    pass

                class _ITextChangedEventHandler:
                    Invoke: _Callable

                class ITextChangedEventHandler(_ITextChangedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ITextChangedEventHandler_impl(_ITextChangedEventHandler, IUnknown_impl):
                    pass

                class _ITextControlPasteEventHandler:
                    Invoke: _Callable

                class ITextControlPasteEventHandler(_ITextControlPasteEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ITextControlPasteEventHandler_impl(_ITextControlPasteEventHandler, IUnknown_impl):
                    pass

                class _IWebViewNavigationFailedEventHandler:
                    Invoke: _Callable

                class IWebViewNavigationFailedEventHandler(_IWebViewNavigationFailedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IWebViewNavigationFailedEventHandler_impl(_IWebViewNavigationFailedEventHandler, IUnknown_impl):
                    pass

                class IAnchorRequestedEventArgs(IInspectable):
                    get_Anchor: _Callable
                    put_Anchor: _Callable
                    get_AnchorCandidates: _Callable

                class IAppBar(IInspectable):
                    get_IsOpen: _Callable
                    put_IsOpen: _Callable
                    get_IsSticky: _Callable
                    put_IsSticky: _Callable
                    add_Opened: _Callable
                    remove_Opened: _Callable
                    add_Closed: _Callable
                    remove_Closed: _Callable

                class IAppBar2(IInspectable):
                    get_ClosedDisplayMode: _Callable
                    put_ClosedDisplayMode: _Callable

                class IAppBar3(IInspectable):
                    get_TemplateSettings: _Callable
                    add_Opening: _Callable
                    remove_Opening: _Callable
                    add_Closing: _Callable
                    remove_Closing: _Callable

                class IAppBar4(IInspectable):
                    get_LightDismissOverlayMode: _Callable
                    put_LightDismissOverlayMode: _Callable

                class IAppBarButton(IInspectable):
                    get_Label: _Callable
                    put_Label: _Callable
                    get_Icon: _Callable
                    put_Icon: _Callable

                class IAppBarButton3(IInspectable):
                    get_LabelPosition: _Callable
                    put_LabelPosition: _Callable

                class IAppBarButton4(IInspectable):
                    get_KeyboardAcceleratorTextOverride: _Callable
                    put_KeyboardAcceleratorTextOverride: _Callable

                class IAppBarButton5(IInspectable):
                    get_TemplateSettings: _Callable

                class IAppBarButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IAppBarButtonStatics(IInspectable):
                    get_LabelProperty: _Callable
                    get_IconProperty: _Callable
                    get_IsCompactProperty: _Callable

                class IAppBarButtonStatics3(IInspectable):
                    get_LabelPositionProperty: _Callable
                    get_IsInOverflowProperty: _Callable
                    get_DynamicOverflowOrderProperty: _Callable

                class IAppBarButtonStatics4(IInspectable):
                    get_KeyboardAcceleratorTextOverrideProperty: _Callable

                class IAppBarElementContainer(IInspectable):
                    pass

                class IAppBarElementContainerFactory(IInspectable):
                    CreateInstance: _Callable

                class IAppBarElementContainerStatics(IInspectable):
                    get_IsCompactProperty: _Callable
                    get_IsInOverflowProperty: _Callable
                    get_DynamicOverflowOrderProperty: _Callable

                class IAppBarFactory(IInspectable):
                    CreateInstance: _Callable

                class IAppBarOverrides(IInspectable):
                    OnClosed: _Callable
                    OnOpened: _Callable

                class IAppBarOverrides3(IInspectable):
                    OnClosing: _Callable
                    OnOpening: _Callable

                class IAppBarSeparator(IInspectable):
                    pass

                class IAppBarSeparatorFactory(IInspectable):
                    CreateInstance: _Callable

                class IAppBarSeparatorStatics(IInspectable):
                    get_IsCompactProperty: _Callable

                class IAppBarSeparatorStatics3(IInspectable):
                    get_IsInOverflowProperty: _Callable
                    get_DynamicOverflowOrderProperty: _Callable

                class IAppBarStatics(IInspectable):
                    get_IsOpenProperty: _Callable
                    get_IsStickyProperty: _Callable

                class IAppBarStatics2(IInspectable):
                    get_ClosedDisplayModeProperty: _Callable

                class IAppBarStatics4(IInspectable):
                    get_LightDismissOverlayModeProperty: _Callable

                class IAppBarToggleButton(IInspectable):
                    get_Label: _Callable
                    put_Label: _Callable
                    get_Icon: _Callable
                    put_Icon: _Callable

                class IAppBarToggleButton3(IInspectable):
                    get_LabelPosition: _Callable
                    put_LabelPosition: _Callable

                class IAppBarToggleButton4(IInspectable):
                    get_KeyboardAcceleratorTextOverride: _Callable
                    put_KeyboardAcceleratorTextOverride: _Callable

                class IAppBarToggleButton5(IInspectable):
                    get_TemplateSettings: _Callable

                class IAppBarToggleButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IAppBarToggleButtonStatics(IInspectable):
                    get_LabelProperty: _Callable
                    get_IconProperty: _Callable
                    get_IsCompactProperty: _Callable

                class IAppBarToggleButtonStatics3(IInspectable):
                    get_LabelPositionProperty: _Callable
                    get_IsInOverflowProperty: _Callable
                    get_DynamicOverflowOrderProperty: _Callable

                class IAppBarToggleButtonStatics4(IInspectable):
                    get_KeyboardAcceleratorTextOverrideProperty: _Callable

                class IAutoSuggestBox(IInspectable):
                    get_MaxSuggestionListHeight: _Callable
                    put_MaxSuggestionListHeight: _Callable
                    get_IsSuggestionListOpen: _Callable
                    put_IsSuggestionListOpen: _Callable
                    get_TextMemberPath: _Callable
                    put_TextMemberPath: _Callable
                    get_Text: _Callable
                    put_Text: _Callable
                    get_UpdateTextOnSelect: _Callable
                    put_UpdateTextOnSelect: _Callable
                    get_PlaceholderText: _Callable
                    put_PlaceholderText: _Callable
                    get_Header: _Callable
                    put_Header: _Callable
                    get_AutoMaximizeSuggestionArea: _Callable
                    put_AutoMaximizeSuggestionArea: _Callable
                    get_TextBoxStyle: _Callable
                    put_TextBoxStyle: _Callable
                    add_SuggestionChosen: _Callable
                    remove_SuggestionChosen: _Callable
                    add_TextChanged: _Callable
                    remove_TextChanged: _Callable

                class IAutoSuggestBox2(IInspectable):
                    get_QueryIcon: _Callable
                    put_QueryIcon: _Callable
                    add_QuerySubmitted: _Callable
                    remove_QuerySubmitted: _Callable

                class IAutoSuggestBox3(IInspectable):
                    get_LightDismissOverlayMode: _Callable
                    put_LightDismissOverlayMode: _Callable

                class IAutoSuggestBox4(IInspectable):
                    get_Description: _Callable
                    put_Description: _Callable

                class IAutoSuggestBoxQuerySubmittedEventArgs(IInspectable):
                    get_QueryText: _Callable
                    get_ChosenSuggestion: _Callable

                class IAutoSuggestBoxStatics(IInspectable):
                    get_MaxSuggestionListHeightProperty: _Callable
                    get_IsSuggestionListOpenProperty: _Callable
                    get_TextMemberPathProperty: _Callable
                    get_TextProperty: _Callable
                    get_UpdateTextOnSelectProperty: _Callable
                    get_PlaceholderTextProperty: _Callable
                    get_HeaderProperty: _Callable
                    get_AutoMaximizeSuggestionAreaProperty: _Callable
                    get_TextBoxStyleProperty: _Callable

                class IAutoSuggestBoxStatics2(IInspectable):
                    get_QueryIconProperty: _Callable

                class IAutoSuggestBoxStatics3(IInspectable):
                    get_LightDismissOverlayModeProperty: _Callable

                class IAutoSuggestBoxStatics4(IInspectable):
                    get_DescriptionProperty: _Callable

                class IAutoSuggestBoxSuggestionChosenEventArgs(IInspectable):
                    get_SelectedItem: _Callable

                class IAutoSuggestBoxTextChangedEventArgs(IInspectable):
                    get_Reason: _Callable
                    put_Reason: _Callable
                    CheckCurrent: _Callable

                class IAutoSuggestBoxTextChangedEventArgsStatics(IInspectable):
                    get_ReasonProperty: _Callable

                class IBackClickEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IBitmapIcon(IInspectable):
                    get_UriSource: _Callable
                    put_UriSource: _Callable

                class IBitmapIcon2(IInspectable):
                    get_ShowAsMonochrome: _Callable
                    put_ShowAsMonochrome: _Callable

                class IBitmapIconFactory(IInspectable):
                    CreateInstance: _Callable

                class IBitmapIconSource(IInspectable):
                    get_UriSource: _Callable
                    put_UriSource: _Callable
                    get_ShowAsMonochrome: _Callable
                    put_ShowAsMonochrome: _Callable

                class IBitmapIconSourceFactory(IInspectable):
                    CreateInstance: _Callable

                class IBitmapIconSourceStatics(IInspectable):
                    get_UriSourceProperty: _Callable
                    get_ShowAsMonochromeProperty: _Callable

                class IBitmapIconStatics(IInspectable):
                    get_UriSourceProperty: _Callable

                class IBitmapIconStatics2(IInspectable):
                    get_ShowAsMonochromeProperty: _Callable

                class IBorder(IInspectable):
                    get_BorderBrush: _Callable
                    put_BorderBrush: _Callable
                    get_BorderThickness: _Callable
                    put_BorderThickness: _Callable
                    get_Background: _Callable
                    put_Background: _Callable
                    get_CornerRadius: _Callable
                    put_CornerRadius: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable
                    get_Child: _Callable
                    put_Child: _Callable
                    get_ChildTransitions: _Callable
                    put_ChildTransitions: _Callable

                class IBorder2(IInspectable):
                    get_BackgroundSizing: _Callable
                    put_BackgroundSizing: _Callable
                    get_BackgroundTransition: _Callable
                    put_BackgroundTransition: _Callable

                class IBorderStatics(IInspectable):
                    get_BorderBrushProperty: _Callable
                    get_BorderThicknessProperty: _Callable
                    get_BackgroundProperty: _Callable
                    get_CornerRadiusProperty: _Callable
                    get_PaddingProperty: _Callable
                    get_ChildTransitionsProperty: _Callable

                class IBorderStatics2(IInspectable):
                    get_BackgroundSizingProperty: _Callable

                class IButton(IInspectable):
                    pass

                class IButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IButtonStaticsWithFlyout(IInspectable):
                    get_FlyoutProperty: _Callable

                class IButtonWithFlyout(IInspectable):
                    get_Flyout: _Callable
                    put_Flyout: _Callable

                class ICalendarDatePicker(IInspectable):
                    get_Date: _Callable
                    put_Date: _Callable
                    get_IsCalendarOpen: _Callable
                    put_IsCalendarOpen: _Callable
                    get_DateFormat: _Callable
                    put_DateFormat: _Callable
                    get_PlaceholderText: _Callable
                    put_PlaceholderText: _Callable
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_CalendarViewStyle: _Callable
                    put_CalendarViewStyle: _Callable
                    get_MinDate: _Callable
                    put_MinDate: _Callable
                    get_MaxDate: _Callable
                    put_MaxDate: _Callable
                    get_IsTodayHighlighted: _Callable
                    put_IsTodayHighlighted: _Callable
                    get_DisplayMode: _Callable
                    put_DisplayMode: _Callable
                    get_FirstDayOfWeek: _Callable
                    put_FirstDayOfWeek: _Callable
                    get_DayOfWeekFormat: _Callable
                    put_DayOfWeekFormat: _Callable
                    get_CalendarIdentifier: _Callable
                    put_CalendarIdentifier: _Callable
                    get_IsOutOfScopeEnabled: _Callable
                    put_IsOutOfScopeEnabled: _Callable
                    get_IsGroupLabelVisible: _Callable
                    put_IsGroupLabelVisible: _Callable
                    add_CalendarViewDayItemChanging: _Callable
                    remove_CalendarViewDayItemChanging: _Callable
                    add_DateChanged: _Callable
                    remove_DateChanged: _Callable
                    add_Opened: _Callable
                    remove_Opened: _Callable
                    add_Closed: _Callable
                    remove_Closed: _Callable
                    SetDisplayDate: _Callable
                    SetYearDecadeDisplayDimensions: _Callable

                class ICalendarDatePicker2(IInspectable):
                    get_LightDismissOverlayMode: _Callable
                    put_LightDismissOverlayMode: _Callable

                class ICalendarDatePicker3(IInspectable):
                    get_Description: _Callable
                    put_Description: _Callable

                class ICalendarDatePickerDateChangedEventArgs(IInspectable):
                    get_NewDate: _Callable
                    get_OldDate: _Callable

                class ICalendarDatePickerFactory(IInspectable):
                    CreateInstance: _Callable

                class ICalendarDatePickerStatics(IInspectable):
                    get_DateProperty: _Callable
                    get_IsCalendarOpenProperty: _Callable
                    get_DateFormatProperty: _Callable
                    get_PlaceholderTextProperty: _Callable
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_CalendarViewStyleProperty: _Callable
                    get_MinDateProperty: _Callable
                    get_MaxDateProperty: _Callable
                    get_IsTodayHighlightedProperty: _Callable
                    get_DisplayModeProperty: _Callable
                    get_FirstDayOfWeekProperty: _Callable
                    get_DayOfWeekFormatProperty: _Callable
                    get_CalendarIdentifierProperty: _Callable
                    get_IsOutOfScopeEnabledProperty: _Callable
                    get_IsGroupLabelVisibleProperty: _Callable

                class ICalendarDatePickerStatics2(IInspectable):
                    get_LightDismissOverlayModeProperty: _Callable

                class ICalendarDatePickerStatics3(IInspectable):
                    get_DescriptionProperty: _Callable

                class ICalendarView(IInspectable):
                    get_CalendarIdentifier: _Callable
                    put_CalendarIdentifier: _Callable
                    get_DayOfWeekFormat: _Callable
                    put_DayOfWeekFormat: _Callable
                    get_IsGroupLabelVisible: _Callable
                    put_IsGroupLabelVisible: _Callable
                    get_DisplayMode: _Callable
                    put_DisplayMode: _Callable
                    get_FirstDayOfWeek: _Callable
                    put_FirstDayOfWeek: _Callable
                    get_IsOutOfScopeEnabled: _Callable
                    put_IsOutOfScopeEnabled: _Callable
                    get_IsTodayHighlighted: _Callable
                    put_IsTodayHighlighted: _Callable
                    get_MaxDate: _Callable
                    put_MaxDate: _Callable
                    get_MinDate: _Callable
                    put_MinDate: _Callable
                    get_NumberOfWeeksInView: _Callable
                    put_NumberOfWeeksInView: _Callable
                    get_SelectedDates: _Callable
                    get_SelectionMode: _Callable
                    put_SelectionMode: _Callable
                    get_TemplateSettings: _Callable
                    get_FocusBorderBrush: _Callable
                    put_FocusBorderBrush: _Callable
                    get_SelectedHoverBorderBrush: _Callable
                    put_SelectedHoverBorderBrush: _Callable
                    get_SelectedPressedBorderBrush: _Callable
                    put_SelectedPressedBorderBrush: _Callable
                    get_SelectedBorderBrush: _Callable
                    put_SelectedBorderBrush: _Callable
                    get_HoverBorderBrush: _Callable
                    put_HoverBorderBrush: _Callable
                    get_PressedBorderBrush: _Callable
                    put_PressedBorderBrush: _Callable
                    get_CalendarItemBorderBrush: _Callable
                    put_CalendarItemBorderBrush: _Callable
                    get_OutOfScopeBackground: _Callable
                    put_OutOfScopeBackground: _Callable
                    get_CalendarItemBackground: _Callable
                    put_CalendarItemBackground: _Callable
                    get_PressedForeground: _Callable
                    put_PressedForeground: _Callable
                    get_TodayForeground: _Callable
                    put_TodayForeground: _Callable
                    get_BlackoutForeground: _Callable
                    put_BlackoutForeground: _Callable
                    get_SelectedForeground: _Callable
                    put_SelectedForeground: _Callable
                    get_OutOfScopeForeground: _Callable
                    put_OutOfScopeForeground: _Callable
                    get_CalendarItemForeground: _Callable
                    put_CalendarItemForeground: _Callable
                    get_DayItemFontFamily: _Callable
                    put_DayItemFontFamily: _Callable
                    get_DayItemFontSize: _Callable
                    put_DayItemFontSize: _Callable
                    get_DayItemFontStyle: _Callable
                    put_DayItemFontStyle: _Callable
                    get_DayItemFontWeight: _Callable
                    put_DayItemFontWeight: _Callable
                    get_TodayFontWeight: _Callable
                    put_TodayFontWeight: _Callable
                    get_FirstOfMonthLabelFontFamily: _Callable
                    put_FirstOfMonthLabelFontFamily: _Callable
                    get_FirstOfMonthLabelFontSize: _Callable
                    put_FirstOfMonthLabelFontSize: _Callable
                    get_FirstOfMonthLabelFontStyle: _Callable
                    put_FirstOfMonthLabelFontStyle: _Callable
                    get_FirstOfMonthLabelFontWeight: _Callable
                    put_FirstOfMonthLabelFontWeight: _Callable
                    get_MonthYearItemFontFamily: _Callable
                    put_MonthYearItemFontFamily: _Callable
                    get_MonthYearItemFontSize: _Callable
                    put_MonthYearItemFontSize: _Callable
                    get_MonthYearItemFontStyle: _Callable
                    put_MonthYearItemFontStyle: _Callable
                    get_MonthYearItemFontWeight: _Callable
                    put_MonthYearItemFontWeight: _Callable
                    get_FirstOfYearDecadeLabelFontFamily: _Callable
                    put_FirstOfYearDecadeLabelFontFamily: _Callable
                    get_FirstOfYearDecadeLabelFontSize: _Callable
                    put_FirstOfYearDecadeLabelFontSize: _Callable
                    get_FirstOfYearDecadeLabelFontStyle: _Callable
                    put_FirstOfYearDecadeLabelFontStyle: _Callable
                    get_FirstOfYearDecadeLabelFontWeight: _Callable
                    put_FirstOfYearDecadeLabelFontWeight: _Callable
                    get_HorizontalDayItemAlignment: _Callable
                    put_HorizontalDayItemAlignment: _Callable
                    get_VerticalDayItemAlignment: _Callable
                    put_VerticalDayItemAlignment: _Callable
                    get_HorizontalFirstOfMonthLabelAlignment: _Callable
                    put_HorizontalFirstOfMonthLabelAlignment: _Callable
                    get_VerticalFirstOfMonthLabelAlignment: _Callable
                    put_VerticalFirstOfMonthLabelAlignment: _Callable
                    get_CalendarItemBorderThickness: _Callable
                    put_CalendarItemBorderThickness: _Callable
                    get_CalendarViewDayItemStyle: _Callable
                    put_CalendarViewDayItemStyle: _Callable
                    add_CalendarViewDayItemChanging: _Callable
                    remove_CalendarViewDayItemChanging: _Callable
                    add_SelectedDatesChanged: _Callable
                    remove_SelectedDatesChanged: _Callable
                    SetDisplayDate: _Callable
                    SetYearDecadeDisplayDimensions: _Callable

                class ICalendarView2(IInspectable):
                    get_SelectedDisabledBorderBrush: _Callable
                    put_SelectedDisabledBorderBrush: _Callable
                    get_TodaySelectedInnerBorderBrush: _Callable
                    put_TodaySelectedInnerBorderBrush: _Callable
                    get_BlackoutStrikethroughBrush: _Callable
                    put_BlackoutStrikethroughBrush: _Callable
                    get_BlackoutBackground: _Callable
                    put_BlackoutBackground: _Callable
                    get_CalendarItemHoverBackground: _Callable
                    put_CalendarItemHoverBackground: _Callable
                    get_CalendarItemPressedBackground: _Callable
                    put_CalendarItemPressedBackground: _Callable
                    get_CalendarItemDisabledBackground: _Callable
                    put_CalendarItemDisabledBackground: _Callable
                    get_TodayBackground: _Callable
                    put_TodayBackground: _Callable
                    get_TodayBlackoutBackground: _Callable
                    put_TodayBlackoutBackground: _Callable
                    get_TodayHoverBackground: _Callable
                    put_TodayHoverBackground: _Callable
                    get_TodayPressedBackground: _Callable
                    put_TodayPressedBackground: _Callable
                    get_TodayDisabledBackground: _Callable
                    put_TodayDisabledBackground: _Callable
                    get_TodayBlackoutForeground: _Callable
                    put_TodayBlackoutForeground: _Callable
                    get_SelectedHoverForeground: _Callable
                    put_SelectedHoverForeground: _Callable
                    get_SelectedPressedForeground: _Callable
                    put_SelectedPressedForeground: _Callable
                    get_SelectedDisabledForeground: _Callable
                    put_SelectedDisabledForeground: _Callable
                    get_OutOfScopeHoverForeground: _Callable
                    put_OutOfScopeHoverForeground: _Callable
                    get_OutOfScopePressedForeground: _Callable
                    put_OutOfScopePressedForeground: _Callable
                    get_DisabledForeground: _Callable
                    put_DisabledForeground: _Callable
                    get_DayItemMargin: _Callable
                    put_DayItemMargin: _Callable
                    get_MonthYearItemMargin: _Callable
                    put_MonthYearItemMargin: _Callable
                    get_FirstOfMonthLabelMargin: _Callable
                    put_FirstOfMonthLabelMargin: _Callable
                    get_FirstOfYearDecadeLabelMargin: _Callable
                    put_FirstOfYearDecadeLabelMargin: _Callable
                    get_CalendarItemCornerRadius: _Callable
                    put_CalendarItemCornerRadius: _Callable

                class ICalendarViewDayItem(IInspectable):
                    get_IsBlackout: _Callable
                    put_IsBlackout: _Callable
                    get_Date: _Callable
                    SetDensityColors: _Callable

                class ICalendarViewDayItemChangingEventArgs(IInspectable):
                    get_InRecycleQueue: _Callable
                    get_Item: _Callable
                    get_Phase: _Callable
                    RegisterUpdateCallback: _Callable
                    RegisterUpdateCallbackWithPhase: _Callable

                class ICalendarViewDayItemFactory(IInspectable):
                    CreateInstance: _Callable

                class ICalendarViewDayItemStatics(IInspectable):
                    get_IsBlackoutProperty: _Callable
                    get_DateProperty: _Callable

                class ICalendarViewFactory(IInspectable):
                    CreateInstance: _Callable

                class ICalendarViewSelectedDatesChangedEventArgs(IInspectable):
                    get_AddedDates: _Callable
                    get_RemovedDates: _Callable

                class ICalendarViewStatics(IInspectable):
                    get_CalendarIdentifierProperty: _Callable
                    get_DayOfWeekFormatProperty: _Callable
                    get_IsGroupLabelVisibleProperty: _Callable
                    get_DisplayModeProperty: _Callable
                    get_FirstDayOfWeekProperty: _Callable
                    get_IsOutOfScopeEnabledProperty: _Callable
                    get_IsTodayHighlightedProperty: _Callable
                    get_MaxDateProperty: _Callable
                    get_MinDateProperty: _Callable
                    get_NumberOfWeeksInViewProperty: _Callable
                    get_SelectedDatesProperty: _Callable
                    get_SelectionModeProperty: _Callable
                    get_TemplateSettingsProperty: _Callable
                    get_FocusBorderBrushProperty: _Callable
                    get_SelectedHoverBorderBrushProperty: _Callable
                    get_SelectedPressedBorderBrushProperty: _Callable
                    get_SelectedBorderBrushProperty: _Callable
                    get_HoverBorderBrushProperty: _Callable
                    get_PressedBorderBrushProperty: _Callable
                    get_CalendarItemBorderBrushProperty: _Callable
                    get_OutOfScopeBackgroundProperty: _Callable
                    get_CalendarItemBackgroundProperty: _Callable
                    get_PressedForegroundProperty: _Callable
                    get_TodayForegroundProperty: _Callable
                    get_BlackoutForegroundProperty: _Callable
                    get_SelectedForegroundProperty: _Callable
                    get_OutOfScopeForegroundProperty: _Callable
                    get_CalendarItemForegroundProperty: _Callable
                    get_DayItemFontFamilyProperty: _Callable
                    get_DayItemFontSizeProperty: _Callable
                    get_DayItemFontStyleProperty: _Callable
                    get_DayItemFontWeightProperty: _Callable
                    get_TodayFontWeightProperty: _Callable
                    get_FirstOfMonthLabelFontFamilyProperty: _Callable
                    get_FirstOfMonthLabelFontSizeProperty: _Callable
                    get_FirstOfMonthLabelFontStyleProperty: _Callable
                    get_FirstOfMonthLabelFontWeightProperty: _Callable
                    get_MonthYearItemFontFamilyProperty: _Callable
                    get_MonthYearItemFontSizeProperty: _Callable
                    get_MonthYearItemFontStyleProperty: _Callable
                    get_MonthYearItemFontWeightProperty: _Callable
                    get_FirstOfYearDecadeLabelFontFamilyProperty: _Callable
                    get_FirstOfYearDecadeLabelFontSizeProperty: _Callable
                    get_FirstOfYearDecadeLabelFontStyleProperty: _Callable
                    get_FirstOfYearDecadeLabelFontWeightProperty: _Callable
                    get_HorizontalDayItemAlignmentProperty: _Callable
                    get_VerticalDayItemAlignmentProperty: _Callable
                    get_HorizontalFirstOfMonthLabelAlignmentProperty: _Callable
                    get_VerticalFirstOfMonthLabelAlignmentProperty: _Callable
                    get_CalendarItemBorderThicknessProperty: _Callable
                    get_CalendarViewDayItemStyleProperty: _Callable

                class ICalendarViewStatics2(IInspectable):
                    get_SelectedDisabledBorderBrushProperty: _Callable
                    get_TodaySelectedInnerBorderBrushProperty: _Callable
                    get_BlackoutStrikethroughBrushProperty: _Callable
                    get_BlackoutBackgroundProperty: _Callable
                    get_CalendarItemHoverBackgroundProperty: _Callable
                    get_CalendarItemPressedBackgroundProperty: _Callable
                    get_CalendarItemDisabledBackgroundProperty: _Callable
                    get_TodayBackgroundProperty: _Callable
                    get_TodayBlackoutBackgroundProperty: _Callable
                    get_TodayHoverBackgroundProperty: _Callable
                    get_TodayPressedBackgroundProperty: _Callable
                    get_TodayDisabledBackgroundProperty: _Callable
                    get_TodayBlackoutForegroundProperty: _Callable
                    get_SelectedHoverForegroundProperty: _Callable
                    get_SelectedPressedForegroundProperty: _Callable
                    get_SelectedDisabledForegroundProperty: _Callable
                    get_OutOfScopeHoverForegroundProperty: _Callable
                    get_OutOfScopePressedForegroundProperty: _Callable
                    get_DisabledForegroundProperty: _Callable
                    get_DayItemMarginProperty: _Callable
                    get_MonthYearItemMarginProperty: _Callable
                    get_FirstOfMonthLabelMarginProperty: _Callable
                    get_FirstOfYearDecadeLabelMarginProperty: _Callable
                    get_CalendarItemCornerRadiusProperty: _Callable

                class ICandidateWindowBoundsChangedEventArgs(IInspectable):
                    get_Bounds: _Callable

                class ICanvas(IInspectable):
                    pass

                class ICanvasFactory(IInspectable):
                    CreateInstance: _Callable

                class ICanvasStatics(IInspectable):
                    get_LeftProperty: _Callable
                    GetLeft: _Callable
                    SetLeft: _Callable
                    get_TopProperty: _Callable
                    GetTop: _Callable
                    SetTop: _Callable
                    get_ZIndexProperty: _Callable
                    GetZIndex: _Callable
                    SetZIndex: _Callable

                class ICaptureElement(IInspectable):
                    get_Source: _Callable
                    put_Source: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable

                class ICaptureElementStatics(IInspectable):
                    get_SourceProperty: _Callable
                    get_StretchProperty: _Callable

                class ICheckBox(IInspectable):
                    pass

                class ICheckBoxFactory(IInspectable):
                    CreateInstance: _Callable

                class IChoosingGroupHeaderContainerEventArgs(IInspectable):
                    get_GroupHeaderContainer: _Callable
                    put_GroupHeaderContainer: _Callable
                    get_GroupIndex: _Callable
                    get_Group: _Callable

                class IChoosingItemContainerEventArgs(IInspectable):
                    get_ItemIndex: _Callable
                    get_Item: _Callable
                    get_ItemContainer: _Callable
                    put_ItemContainer: _Callable
                    get_IsContainerPrepared: _Callable
                    put_IsContainerPrepared: _Callable

                class ICleanUpVirtualizedItemEventArgs(IInspectable):
                    get_Value: _Callable
                    get_UIElement: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class IColorChangedEventArgs(IInspectable):
                    get_OldColor: _Callable
                    get_NewColor: _Callable

                class IColorPicker(IInspectable):
                    get_Color: _Callable
                    put_Color: _Callable
                    get_PreviousColor: _Callable
                    put_PreviousColor: _Callable
                    get_IsAlphaEnabled: _Callable
                    put_IsAlphaEnabled: _Callable
                    get_IsColorSpectrumVisible: _Callable
                    put_IsColorSpectrumVisible: _Callable
                    get_IsColorPreviewVisible: _Callable
                    put_IsColorPreviewVisible: _Callable
                    get_IsColorSliderVisible: _Callable
                    put_IsColorSliderVisible: _Callable
                    get_IsAlphaSliderVisible: _Callable
                    put_IsAlphaSliderVisible: _Callable
                    get_IsMoreButtonVisible: _Callable
                    put_IsMoreButtonVisible: _Callable
                    get_IsColorChannelTextInputVisible: _Callable
                    put_IsColorChannelTextInputVisible: _Callable
                    get_IsAlphaTextInputVisible: _Callable
                    put_IsAlphaTextInputVisible: _Callable
                    get_IsHexInputVisible: _Callable
                    put_IsHexInputVisible: _Callable
                    get_MinHue: _Callable
                    put_MinHue: _Callable
                    get_MaxHue: _Callable
                    put_MaxHue: _Callable
                    get_MinSaturation: _Callable
                    put_MinSaturation: _Callable
                    get_MaxSaturation: _Callable
                    put_MaxSaturation: _Callable
                    get_MinValue: _Callable
                    put_MinValue: _Callable
                    get_MaxValue: _Callable
                    put_MaxValue: _Callable
                    get_ColorSpectrumShape: _Callable
                    put_ColorSpectrumShape: _Callable
                    get_ColorSpectrumComponents: _Callable
                    put_ColorSpectrumComponents: _Callable
                    add_ColorChanged: _Callable
                    remove_ColorChanged: _Callable

                class IColorPickerFactory(IInspectable):
                    CreateInstance: _Callable

                class IColorPickerStatics(IInspectable):
                    get_ColorProperty: _Callable
                    get_PreviousColorProperty: _Callable
                    get_IsAlphaEnabledProperty: _Callable
                    get_IsColorSpectrumVisibleProperty: _Callable
                    get_IsColorPreviewVisibleProperty: _Callable
                    get_IsColorSliderVisibleProperty: _Callable
                    get_IsAlphaSliderVisibleProperty: _Callable
                    get_IsMoreButtonVisibleProperty: _Callable
                    get_IsColorChannelTextInputVisibleProperty: _Callable
                    get_IsAlphaTextInputVisibleProperty: _Callable
                    get_IsHexInputVisibleProperty: _Callable
                    get_MinHueProperty: _Callable
                    get_MaxHueProperty: _Callable
                    get_MinSaturationProperty: _Callable
                    get_MaxSaturationProperty: _Callable
                    get_MinValueProperty: _Callable
                    get_MaxValueProperty: _Callable
                    get_ColorSpectrumShapeProperty: _Callable
                    get_ColorSpectrumComponentsProperty: _Callable

                class IColumnDefinition(IInspectable):
                    get_Width: _Callable
                    put_Width: _Callable
                    get_MaxWidth: _Callable
                    put_MaxWidth: _Callable
                    get_MinWidth: _Callable
                    put_MinWidth: _Callable
                    get_ActualWidth: _Callable

                class IColumnDefinitionStatics(IInspectable):
                    get_WidthProperty: _Callable
                    get_MaxWidthProperty: _Callable
                    get_MinWidthProperty: _Callable

                class IComboBox(IInspectable):
                    get_IsDropDownOpen: _Callable
                    put_IsDropDownOpen: _Callable
                    get_IsEditable: _Callable
                    get_IsSelectionBoxHighlighted: _Callable
                    get_MaxDropDownHeight: _Callable
                    put_MaxDropDownHeight: _Callable
                    get_SelectionBoxItem: _Callable
                    get_SelectionBoxItemTemplate: _Callable
                    get_TemplateSettings: _Callable
                    add_DropDownClosed: _Callable
                    remove_DropDownClosed: _Callable
                    add_DropDownOpened: _Callable
                    remove_DropDownOpened: _Callable

                class IComboBox2(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_PlaceholderText: _Callable
                    put_PlaceholderText: _Callable

                class IComboBox3(IInspectable):
                    get_LightDismissOverlayMode: _Callable
                    put_LightDismissOverlayMode: _Callable
                    get_IsTextSearchEnabled: _Callable
                    put_IsTextSearchEnabled: _Callable

                class IComboBox4(IInspectable):
                    get_SelectionChangedTrigger: _Callable
                    put_SelectionChangedTrigger: _Callable

                class IComboBox5(IInspectable):
                    get_PlaceholderForeground: _Callable
                    put_PlaceholderForeground: _Callable

                class IComboBox6(IInspectable):
                    put_IsEditable: _Callable
                    get_Text: _Callable
                    put_Text: _Callable
                    get_TextBoxStyle: _Callable
                    put_TextBoxStyle: _Callable
                    get_Description: _Callable
                    put_Description: _Callable
                    add_TextSubmitted: _Callable
                    remove_TextSubmitted: _Callable

                class IComboBoxFactory(IInspectable):
                    CreateInstance: _Callable

                class IComboBoxItem(IInspectable):
                    pass

                class IComboBoxItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IComboBoxOverrides(IInspectable):
                    OnDropDownClosed: _Callable
                    OnDropDownOpened: _Callable

                class IComboBoxStatics(IInspectable):
                    get_IsDropDownOpenProperty: _Callable
                    get_MaxDropDownHeightProperty: _Callable

                class IComboBoxStatics2(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_PlaceholderTextProperty: _Callable

                class IComboBoxStatics3(IInspectable):
                    get_LightDismissOverlayModeProperty: _Callable
                    get_IsTextSearchEnabledProperty: _Callable

                class IComboBoxStatics4(IInspectable):
                    get_SelectionChangedTriggerProperty: _Callable

                class IComboBoxStatics5(IInspectable):
                    get_PlaceholderForegroundProperty: _Callable

                class IComboBoxStatics6(IInspectable):
                    get_IsEditableProperty: _Callable
                    get_TextProperty: _Callable
                    get_TextBoxStyleProperty: _Callable
                    get_DescriptionProperty: _Callable

                class IComboBoxTextSubmittedEventArgs(IInspectable):
                    get_Text: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable

                class ICommandBar(IInspectable):
                    get_PrimaryCommands: _Callable
                    get_SecondaryCommands: _Callable

                class ICommandBar2(IInspectable):
                    get_CommandBarOverflowPresenterStyle: _Callable
                    put_CommandBarOverflowPresenterStyle: _Callable
                    get_CommandBarTemplateSettings: _Callable

                class ICommandBar3(IInspectable):
                    get_DefaultLabelPosition: _Callable
                    put_DefaultLabelPosition: _Callable
                    get_OverflowButtonVisibility: _Callable
                    put_OverflowButtonVisibility: _Callable
                    get_IsDynamicOverflowEnabled: _Callable
                    put_IsDynamicOverflowEnabled: _Callable
                    add_DynamicOverflowItemsChanging: _Callable
                    remove_DynamicOverflowItemsChanging: _Callable

                class ICommandBarElement(IInspectable):
                    get_IsCompact: _Callable
                    put_IsCompact: _Callable

                class ICommandBarElement2(IInspectable):
                    get_IsInOverflow: _Callable
                    get_DynamicOverflowOrder: _Callable
                    put_DynamicOverflowOrder: _Callable

                class ICommandBarFactory(IInspectable):
                    CreateInstance: _Callable

                class ICommandBarFlyout(IInspectable):
                    get_PrimaryCommands: _Callable
                    get_SecondaryCommands: _Callable

                class ICommandBarFlyoutFactory(IInspectable):
                    CreateInstance: _Callable

                class ICommandBarOverflowPresenter(IInspectable):
                    pass

                class ICommandBarOverflowPresenterFactory(IInspectable):
                    CreateInstance: _Callable

                class ICommandBarStatics(IInspectable):
                    get_PrimaryCommandsProperty: _Callable
                    get_SecondaryCommandsProperty: _Callable

                class ICommandBarStatics2(IInspectable):
                    get_CommandBarOverflowPresenterStyleProperty: _Callable

                class ICommandBarStatics3(IInspectable):
                    get_DefaultLabelPositionProperty: _Callable
                    get_OverflowButtonVisibilityProperty: _Callable
                    get_IsDynamicOverflowEnabledProperty: _Callable

                class IContainerContentChangingEventArgs(IInspectable):
                    get_ItemContainer: _Callable
                    get_InRecycleQueue: _Callable
                    get_ItemIndex: _Callable
                    get_Item: _Callable
                    get_Phase: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    RegisterUpdateCallback: _Callable
                    RegisterUpdateCallbackWithPhase: _Callable

                class IContentControl(IInspectable):
                    get_Content: _Callable
                    put_Content: _Callable
                    get_ContentTemplate: _Callable
                    put_ContentTemplate: _Callable
                    get_ContentTemplateSelector: _Callable
                    put_ContentTemplateSelector: _Callable
                    get_ContentTransitions: _Callable
                    put_ContentTransitions: _Callable

                class IContentControl2(IInspectable):
                    get_ContentTemplateRoot: _Callable

                class IContentControlFactory(IInspectable):
                    CreateInstance: _Callable

                class IContentControlOverrides(IInspectable):
                    OnContentChanged: _Callable
                    OnContentTemplateChanged: _Callable
                    OnContentTemplateSelectorChanged: _Callable

                class IContentControlStatics(IInspectable):
                    get_ContentProperty: _Callable
                    get_ContentTemplateProperty: _Callable
                    get_ContentTemplateSelectorProperty: _Callable
                    get_ContentTransitionsProperty: _Callable

                class IContentDialog(IInspectable):
                    get_Title: _Callable
                    put_Title: _Callable
                    get_TitleTemplate: _Callable
                    put_TitleTemplate: _Callable
                    get_FullSizeDesired: _Callable
                    put_FullSizeDesired: _Callable
                    get_PrimaryButtonText: _Callable
                    put_PrimaryButtonText: _Callable
                    get_SecondaryButtonText: _Callable
                    put_SecondaryButtonText: _Callable
                    get_PrimaryButtonCommand: _Callable
                    put_PrimaryButtonCommand: _Callable
                    get_SecondaryButtonCommand: _Callable
                    put_SecondaryButtonCommand: _Callable
                    get_PrimaryButtonCommandParameter: _Callable
                    put_PrimaryButtonCommandParameter: _Callable
                    get_SecondaryButtonCommandParameter: _Callable
                    put_SecondaryButtonCommandParameter: _Callable
                    get_IsPrimaryButtonEnabled: _Callable
                    put_IsPrimaryButtonEnabled: _Callable
                    get_IsSecondaryButtonEnabled: _Callable
                    put_IsSecondaryButtonEnabled: _Callable
                    add_Closing: _Callable
                    remove_Closing: _Callable
                    add_Closed: _Callable
                    remove_Closed: _Callable
                    add_Opened: _Callable
                    remove_Opened: _Callable
                    add_PrimaryButtonClick: _Callable
                    remove_PrimaryButtonClick: _Callable
                    add_SecondaryButtonClick: _Callable
                    remove_SecondaryButtonClick: _Callable
                    Hide: _Callable
                    ShowAsync: _Callable

                class IContentDialog2(IInspectable):
                    get_CloseButtonText: _Callable
                    put_CloseButtonText: _Callable
                    get_CloseButtonCommand: _Callable
                    put_CloseButtonCommand: _Callable
                    get_CloseButtonCommandParameter: _Callable
                    put_CloseButtonCommandParameter: _Callable
                    get_PrimaryButtonStyle: _Callable
                    put_PrimaryButtonStyle: _Callable
                    get_SecondaryButtonStyle: _Callable
                    put_SecondaryButtonStyle: _Callable
                    get_CloseButtonStyle: _Callable
                    put_CloseButtonStyle: _Callable
                    get_DefaultButton: _Callable
                    put_DefaultButton: _Callable
                    add_CloseButtonClick: _Callable
                    remove_CloseButtonClick: _Callable

                class IContentDialog3(IInspectable):
                    ShowAsyncWithPlacement: _Callable

                class IContentDialogButtonClickDeferral(IInspectable):
                    Complete: _Callable

                class IContentDialogButtonClickEventArgs(IInspectable):
                    get_Cancel: _Callable
                    put_Cancel: _Callable
                    GetDeferral: _Callable

                class IContentDialogClosedEventArgs(IInspectable):
                    get_Result: _Callable

                class IContentDialogClosingDeferral(IInspectable):
                    Complete: _Callable

                class IContentDialogClosingEventArgs(IInspectable):
                    get_Result: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable
                    GetDeferral: _Callable

                class IContentDialogFactory(IInspectable):
                    CreateInstance: _Callable

                class IContentDialogOpenedEventArgs(IInspectable):
                    pass

                class IContentDialogStatics(IInspectable):
                    get_TitleProperty: _Callable
                    get_TitleTemplateProperty: _Callable
                    get_FullSizeDesiredProperty: _Callable
                    get_PrimaryButtonTextProperty: _Callable
                    get_SecondaryButtonTextProperty: _Callable
                    get_PrimaryButtonCommandProperty: _Callable
                    get_SecondaryButtonCommandProperty: _Callable
                    get_PrimaryButtonCommandParameterProperty: _Callable
                    get_SecondaryButtonCommandParameterProperty: _Callable
                    get_IsPrimaryButtonEnabledProperty: _Callable
                    get_IsSecondaryButtonEnabledProperty: _Callable

                class IContentDialogStatics2(IInspectable):
                    get_CloseButtonTextProperty: _Callable
                    get_CloseButtonCommandProperty: _Callable
                    get_CloseButtonCommandParameterProperty: _Callable
                    get_PrimaryButtonStyleProperty: _Callable
                    get_SecondaryButtonStyleProperty: _Callable
                    get_CloseButtonStyleProperty: _Callable
                    get_DefaultButtonProperty: _Callable

                class IContentLinkChangedEventArgs(IInspectable):
                    get_ChangeKind: _Callable
                    get_ContentLinkInfo: _Callable
                    get_TextRange: _Callable

                class IContentPresenter(IInspectable):
                    get_Content: _Callable
                    put_Content: _Callable
                    get_ContentTemplate: _Callable
                    put_ContentTemplate: _Callable
                    get_ContentTemplateSelector: _Callable
                    put_ContentTemplateSelector: _Callable
                    get_ContentTransitions: _Callable
                    put_ContentTransitions: _Callable
                    get_FontSize: _Callable
                    put_FontSize: _Callable
                    get_FontFamily: _Callable
                    put_FontFamily: _Callable
                    get_FontWeight: _Callable
                    put_FontWeight: _Callable
                    get_FontStyle: _Callable
                    put_FontStyle: _Callable
                    get_FontStretch: _Callable
                    put_FontStretch: _Callable
                    get_CharacterSpacing: _Callable
                    put_CharacterSpacing: _Callable
                    get_Foreground: _Callable
                    put_Foreground: _Callable

                class IContentPresenter2(IInspectable):
                    get_OpticalMarginAlignment: _Callable
                    put_OpticalMarginAlignment: _Callable
                    get_TextLineBounds: _Callable
                    put_TextLineBounds: _Callable

                class IContentPresenter3(IInspectable):
                    get_IsTextScaleFactorEnabled: _Callable
                    put_IsTextScaleFactorEnabled: _Callable

                class IContentPresenter4(IInspectable):
                    get_TextWrapping: _Callable
                    put_TextWrapping: _Callable
                    get_MaxLines: _Callable
                    put_MaxLines: _Callable
                    get_LineStackingStrategy: _Callable
                    put_LineStackingStrategy: _Callable
                    get_LineHeight: _Callable
                    put_LineHeight: _Callable
                    get_BorderBrush: _Callable
                    put_BorderBrush: _Callable
                    get_BorderThickness: _Callable
                    put_BorderThickness: _Callable
                    get_CornerRadius: _Callable
                    put_CornerRadius: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable
                    get_Background: _Callable
                    put_Background: _Callable
                    get_HorizontalContentAlignment: _Callable
                    put_HorizontalContentAlignment: _Callable
                    get_VerticalContentAlignment: _Callable
                    put_VerticalContentAlignment: _Callable

                class IContentPresenter5(IInspectable):
                    get_BackgroundTransition: _Callable
                    put_BackgroundTransition: _Callable
                    get_BackgroundSizing: _Callable
                    put_BackgroundSizing: _Callable

                class IContentPresenterFactory(IInspectable):
                    CreateInstance: _Callable

                class IContentPresenterOverrides(IInspectable):
                    OnContentTemplateChanged: _Callable
                    OnContentTemplateSelectorChanged: _Callable

                class IContentPresenterStatics(IInspectable):
                    get_ContentProperty: _Callable
                    get_ContentTemplateProperty: _Callable
                    get_ContentTemplateSelectorProperty: _Callable
                    get_ContentTransitionsProperty: _Callable
                    get_FontSizeProperty: _Callable
                    get_FontFamilyProperty: _Callable
                    get_FontWeightProperty: _Callable
                    get_FontStyleProperty: _Callable
                    get_FontStretchProperty: _Callable
                    get_CharacterSpacingProperty: _Callable
                    get_ForegroundProperty: _Callable

                class IContentPresenterStatics2(IInspectable):
                    get_OpticalMarginAlignmentProperty: _Callable
                    get_TextLineBoundsProperty: _Callable

                class IContentPresenterStatics3(IInspectable):
                    get_IsTextScaleFactorEnabledProperty: _Callable

                class IContentPresenterStatics4(IInspectable):
                    get_TextWrappingProperty: _Callable
                    get_MaxLinesProperty: _Callable
                    get_LineStackingStrategyProperty: _Callable
                    get_LineHeightProperty: _Callable
                    get_BorderBrushProperty: _Callable
                    get_BorderThicknessProperty: _Callable
                    get_CornerRadiusProperty: _Callable
                    get_PaddingProperty: _Callable
                    get_BackgroundProperty: _Callable
                    get_HorizontalContentAlignmentProperty: _Callable
                    get_VerticalContentAlignmentProperty: _Callable

                class IContentPresenterStatics5(IInspectable):
                    get_BackgroundSizingProperty: _Callable

                class IContextMenuEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_CursorLeft: _Callable
                    get_CursorTop: _Callable

                class IControl(IInspectable):
                    get_FontSize: _Callable
                    put_FontSize: _Callable
                    get_FontFamily: _Callable
                    put_FontFamily: _Callable
                    get_FontWeight: _Callable
                    put_FontWeight: _Callable
                    get_FontStyle: _Callable
                    put_FontStyle: _Callable
                    get_FontStretch: _Callable
                    put_FontStretch: _Callable
                    get_CharacterSpacing: _Callable
                    put_CharacterSpacing: _Callable
                    get_Foreground: _Callable
                    put_Foreground: _Callable
                    get_IsTabStop: _Callable
                    put_IsTabStop: _Callable
                    get_IsEnabled: _Callable
                    put_IsEnabled: _Callable
                    get_TabIndex: _Callable
                    put_TabIndex: _Callable
                    get_TabNavigation: _Callable
                    put_TabNavigation: _Callable
                    get_Template: _Callable
                    put_Template: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable
                    get_HorizontalContentAlignment: _Callable
                    put_HorizontalContentAlignment: _Callable
                    get_VerticalContentAlignment: _Callable
                    put_VerticalContentAlignment: _Callable
                    get_Background: _Callable
                    put_Background: _Callable
                    get_BorderThickness: _Callable
                    put_BorderThickness: _Callable
                    get_BorderBrush: _Callable
                    put_BorderBrush: _Callable
                    get_FocusState: _Callable
                    add_IsEnabledChanged: _Callable
                    remove_IsEnabledChanged: _Callable
                    ApplyTemplate: _Callable
                    Focus: _Callable

                class IControl2(IInspectable):
                    get_IsTextScaleFactorEnabled: _Callable
                    put_IsTextScaleFactorEnabled: _Callable

                class IControl3(IInspectable):
                    get_UseSystemFocusVisuals: _Callable
                    put_UseSystemFocusVisuals: _Callable

                class IControl4(IInspectable):
                    get_IsFocusEngagementEnabled: _Callable
                    put_IsFocusEngagementEnabled: _Callable
                    get_IsFocusEngaged: _Callable
                    put_IsFocusEngaged: _Callable
                    get_RequiresPointer: _Callable
                    put_RequiresPointer: _Callable
                    get_XYFocusLeft: _Callable
                    put_XYFocusLeft: _Callable
                    get_XYFocusRight: _Callable
                    put_XYFocusRight: _Callable
                    get_XYFocusUp: _Callable
                    put_XYFocusUp: _Callable
                    get_XYFocusDown: _Callable
                    put_XYFocusDown: _Callable
                    get_ElementSoundMode: _Callable
                    put_ElementSoundMode: _Callable
                    add_FocusEngaged: _Callable
                    remove_FocusEngaged: _Callable
                    add_FocusDisengaged: _Callable
                    remove_FocusDisengaged: _Callable
                    RemoveFocusEngagement: _Callable

                class IControl5(IInspectable):
                    get_DefaultStyleResourceUri: _Callable
                    put_DefaultStyleResourceUri: _Callable

                class IControl7(IInspectable):
                    get_BackgroundSizing: _Callable
                    put_BackgroundSizing: _Callable
                    get_CornerRadius: _Callable
                    put_CornerRadius: _Callable

                class IControlFactory(IInspectable):
                    CreateInstance: _Callable

                class IControlOverrides(IInspectable):
                    OnPointerEntered: _Callable
                    OnPointerPressed: _Callable
                    OnPointerMoved: _Callable
                    OnPointerReleased: _Callable
                    OnPointerExited: _Callable
                    OnPointerCaptureLost: _Callable
                    OnPointerCanceled: _Callable
                    OnPointerWheelChanged: _Callable
                    OnTapped: _Callable
                    OnDoubleTapped: _Callable
                    OnHolding: _Callable
                    OnRightTapped: _Callable
                    OnManipulationStarting: _Callable
                    OnManipulationInertiaStarting: _Callable
                    OnManipulationStarted: _Callable
                    OnManipulationDelta: _Callable
                    OnManipulationCompleted: _Callable
                    OnKeyUp: _Callable
                    OnKeyDown: _Callable
                    OnGotFocus: _Callable
                    OnLostFocus: _Callable
                    OnDragEnter: _Callable
                    OnDragLeave: _Callable
                    OnDragOver: _Callable
                    OnDrop: _Callable

                class IControlOverrides6(IInspectable):
                    OnPreviewKeyDown: _Callable
                    OnPreviewKeyUp: _Callable
                    OnCharacterReceived: _Callable

                class IControlProtected(IInspectable):
                    get_DefaultStyleKey: _Callable
                    put_DefaultStyleKey: _Callable
                    GetTemplateChild: _Callable

                class IControlStatics(IInspectable):
                    get_FontSizeProperty: _Callable
                    get_FontFamilyProperty: _Callable
                    get_FontWeightProperty: _Callable
                    get_FontStyleProperty: _Callable
                    get_FontStretchProperty: _Callable
                    get_CharacterSpacingProperty: _Callable
                    get_ForegroundProperty: _Callable
                    get_IsTabStopProperty: _Callable
                    get_IsEnabledProperty: _Callable
                    get_TabIndexProperty: _Callable
                    get_TabNavigationProperty: _Callable
                    get_TemplateProperty: _Callable
                    get_PaddingProperty: _Callable
                    get_HorizontalContentAlignmentProperty: _Callable
                    get_VerticalContentAlignmentProperty: _Callable
                    get_BackgroundProperty: _Callable
                    get_BorderThicknessProperty: _Callable
                    get_BorderBrushProperty: _Callable
                    get_DefaultStyleKeyProperty: _Callable
                    get_FocusStateProperty: _Callable

                class IControlStatics2(IInspectable):
                    get_IsTextScaleFactorEnabledProperty: _Callable

                class IControlStatics3(IInspectable):
                    get_UseSystemFocusVisualsProperty: _Callable
                    get_IsTemplateFocusTargetProperty: _Callable
                    GetIsTemplateFocusTarget: _Callable
                    SetIsTemplateFocusTarget: _Callable

                class IControlStatics4(IInspectable):
                    get_IsFocusEngagementEnabledProperty: _Callable
                    get_IsFocusEngagedProperty: _Callable
                    get_RequiresPointerProperty: _Callable
                    get_XYFocusLeftProperty: _Callable
                    get_XYFocusRightProperty: _Callable
                    get_XYFocusUpProperty: _Callable
                    get_XYFocusDownProperty: _Callable
                    get_ElementSoundModeProperty: _Callable

                class IControlStatics5(IInspectable):
                    get_DefaultStyleResourceUriProperty: _Callable
                    get_IsTemplateKeyTipTargetProperty: _Callable
                    GetIsTemplateKeyTipTarget: _Callable
                    SetIsTemplateKeyTipTarget: _Callable

                class IControlStatics7(IInspectable):
                    get_BackgroundSizingProperty: _Callable
                    get_CornerRadiusProperty: _Callable

                class IControlTemplate(IInspectable):
                    get_TargetType: _Callable
                    put_TargetType: _Callable

                class IDataTemplateSelector(IInspectable):
                    SelectTemplate: _Callable

                class IDataTemplateSelector2(IInspectable):
                    SelectTemplateForItem: _Callable

                class IDataTemplateSelectorFactory(IInspectable):
                    CreateInstance: _Callable

                class IDataTemplateSelectorOverrides(IInspectable):
                    SelectTemplateCore: _Callable

                class IDataTemplateSelectorOverrides2(IInspectable):
                    SelectTemplateForItemCore: _Callable

                class IDatePickedEventArgs(IInspectable):
                    get_OldDate: _Callable
                    get_NewDate: _Callable

                class IDatePicker(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_CalendarIdentifier: _Callable
                    put_CalendarIdentifier: _Callable
                    get_Date: _Callable
                    put_Date: _Callable
                    get_DayVisible: _Callable
                    put_DayVisible: _Callable
                    get_MonthVisible: _Callable
                    put_MonthVisible: _Callable
                    get_YearVisible: _Callable
                    put_YearVisible: _Callable
                    get_DayFormat: _Callable
                    put_DayFormat: _Callable
                    get_MonthFormat: _Callable
                    put_MonthFormat: _Callable
                    get_YearFormat: _Callable
                    put_YearFormat: _Callable
                    get_MinYear: _Callable
                    put_MinYear: _Callable
                    get_MaxYear: _Callable
                    put_MaxYear: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    add_DateChanged: _Callable
                    remove_DateChanged: _Callable

                class IDatePicker2(IInspectable):
                    get_LightDismissOverlayMode: _Callable
                    put_LightDismissOverlayMode: _Callable

                class IDatePicker3(IInspectable):
                    get_SelectedDate: _Callable
                    put_SelectedDate: _Callable
                    add_SelectedDateChanged: _Callable
                    remove_SelectedDateChanged: _Callable

                class IDatePickerFactory(IInspectable):
                    CreateInstance: _Callable

                class IDatePickerFlyout(IInspectable):
                    get_CalendarIdentifier: _Callable
                    put_CalendarIdentifier: _Callable
                    get_Date: _Callable
                    put_Date: _Callable
                    get_DayVisible: _Callable
                    put_DayVisible: _Callable
                    get_MonthVisible: _Callable
                    put_MonthVisible: _Callable
                    get_YearVisible: _Callable
                    put_YearVisible: _Callable
                    get_MinYear: _Callable
                    put_MinYear: _Callable
                    get_MaxYear: _Callable
                    put_MaxYear: _Callable
                    add_DatePicked: _Callable
                    remove_DatePicked: _Callable
                    ShowAtAsync: _Callable

                class IDatePickerFlyout2(IInspectable):
                    get_DayFormat: _Callable
                    put_DayFormat: _Callable
                    get_MonthFormat: _Callable
                    put_MonthFormat: _Callable
                    get_YearFormat: _Callable
                    put_YearFormat: _Callable

                class IDatePickerFlyoutItem(IInspectable):
                    get_PrimaryText: _Callable
                    put_PrimaryText: _Callable
                    get_SecondaryText: _Callable
                    put_SecondaryText: _Callable

                class IDatePickerFlyoutItemStatics(IInspectable):
                    get_PrimaryTextProperty: _Callable
                    get_SecondaryTextProperty: _Callable

                class IDatePickerFlyoutPresenter(IInspectable):
                    pass

                class IDatePickerFlyoutPresenter2(IInspectable):
                    get_IsDefaultShadowEnabled: _Callable
                    put_IsDefaultShadowEnabled: _Callable

                class IDatePickerFlyoutPresenterStatics2(IInspectable):
                    get_IsDefaultShadowEnabledProperty: _Callable

                class IDatePickerFlyoutStatics(IInspectable):
                    get_CalendarIdentifierProperty: _Callable
                    get_DateProperty: _Callable
                    get_DayVisibleProperty: _Callable
                    get_MonthVisibleProperty: _Callable
                    get_YearVisibleProperty: _Callable
                    get_MinYearProperty: _Callable
                    get_MaxYearProperty: _Callable

                class IDatePickerFlyoutStatics2(IInspectable):
                    get_DayFormatProperty: _Callable
                    get_MonthFormatProperty: _Callable
                    get_YearFormatProperty: _Callable

                class IDatePickerSelectedValueChangedEventArgs(IInspectable):
                    get_OldDate: _Callable
                    get_NewDate: _Callable

                class IDatePickerStatics(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_CalendarIdentifierProperty: _Callable
                    get_DateProperty: _Callable
                    get_DayVisibleProperty: _Callable
                    get_MonthVisibleProperty: _Callable
                    get_YearVisibleProperty: _Callable
                    get_DayFormatProperty: _Callable
                    get_MonthFormatProperty: _Callable
                    get_YearFormatProperty: _Callable
                    get_MinYearProperty: _Callable
                    get_MaxYearProperty: _Callable
                    get_OrientationProperty: _Callable

                class IDatePickerStatics2(IInspectable):
                    get_LightDismissOverlayModeProperty: _Callable

                class IDatePickerStatics3(IInspectable):
                    get_SelectedDateProperty: _Callable

                class IDatePickerValueChangedEventArgs(IInspectable):
                    get_OldDate: _Callable
                    get_NewDate: _Callable

                class IDragItemsCompletedEventArgs(IInspectable):
                    get_Items: _Callable
                    get_DropResult: _Callable

                class IDragItemsStartingEventArgs(IInspectable):
                    get_Cancel: _Callable
                    put_Cancel: _Callable
                    get_Items: _Callable
                    get_Data: _Callable

                class IDropDownButton(IInspectable):
                    pass

                class IDropDownButtonAutomationPeer(IInspectable):
                    pass

                class IDropDownButtonAutomationPeerFactory(IInspectable):
                    CreateInstance: _Callable

                class IDropDownButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IDynamicOverflowItemsChangingEventArgs(IInspectable):
                    get_Action: _Callable

                class IFlipView(IInspectable):
                    pass

                class IFlipView2(IInspectable):
                    get_UseTouchAnimationsForAllNavigation: _Callable
                    put_UseTouchAnimationsForAllNavigation: _Callable

                class IFlipViewFactory(IInspectable):
                    CreateInstance: _Callable

                class IFlipViewItem(IInspectable):
                    pass

                class IFlipViewItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IFlipViewStatics2(IInspectable):
                    get_UseTouchAnimationsForAllNavigationProperty: _Callable

                class IFlyout(IInspectable):
                    get_Content: _Callable
                    put_Content: _Callable
                    get_FlyoutPresenterStyle: _Callable
                    put_FlyoutPresenterStyle: _Callable

                class IFlyoutFactory(IInspectable):
                    CreateInstance: _Callable

                class IFlyoutPresenter(IInspectable):
                    pass

                class IFlyoutPresenter2(IInspectable):
                    get_IsDefaultShadowEnabled: _Callable
                    put_IsDefaultShadowEnabled: _Callable

                class IFlyoutPresenterFactory(IInspectable):
                    CreateInstance: _Callable

                class IFlyoutPresenterStatics2(IInspectable):
                    get_IsDefaultShadowEnabledProperty: _Callable

                class IFlyoutStatics(IInspectable):
                    get_ContentProperty: _Callable
                    get_FlyoutPresenterStyleProperty: _Callable

                class IFocusDisengagedEventArgs(IInspectable):
                    pass

                class IFocusEngagedEventArgs(IInspectable):
                    pass

                class IFocusEngagedEventArgs2(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IFontIcon(IInspectable):
                    get_Glyph: _Callable
                    put_Glyph: _Callable
                    get_FontSize: _Callable
                    put_FontSize: _Callable
                    get_FontFamily: _Callable
                    put_FontFamily: _Callable
                    get_FontWeight: _Callable
                    put_FontWeight: _Callable
                    get_FontStyle: _Callable
                    put_FontStyle: _Callable

                class IFontIcon2(IInspectable):
                    get_IsTextScaleFactorEnabled: _Callable
                    put_IsTextScaleFactorEnabled: _Callable

                class IFontIcon3(IInspectable):
                    get_MirroredWhenRightToLeft: _Callable
                    put_MirroredWhenRightToLeft: _Callable

                class IFontIconFactory(IInspectable):
                    CreateInstance: _Callable

                class IFontIconSource(IInspectable):
                    get_Glyph: _Callable
                    put_Glyph: _Callable
                    get_FontSize: _Callable
                    put_FontSize: _Callable
                    get_FontFamily: _Callable
                    put_FontFamily: _Callable
                    get_FontWeight: _Callable
                    put_FontWeight: _Callable
                    get_FontStyle: _Callable
                    put_FontStyle: _Callable
                    get_IsTextScaleFactorEnabled: _Callable
                    put_IsTextScaleFactorEnabled: _Callable
                    get_MirroredWhenRightToLeft: _Callable
                    put_MirroredWhenRightToLeft: _Callable

                class IFontIconSourceFactory(IInspectable):
                    CreateInstance: _Callable

                class IFontIconSourceStatics(IInspectable):
                    get_GlyphProperty: _Callable
                    get_FontSizeProperty: _Callable
                    get_FontFamilyProperty: _Callable
                    get_FontWeightProperty: _Callable
                    get_FontStyleProperty: _Callable
                    get_IsTextScaleFactorEnabledProperty: _Callable
                    get_MirroredWhenRightToLeftProperty: _Callable

                class IFontIconStatics(IInspectable):
                    get_GlyphProperty: _Callable
                    get_FontSizeProperty: _Callable
                    get_FontFamilyProperty: _Callable
                    get_FontWeightProperty: _Callable
                    get_FontStyleProperty: _Callable

                class IFontIconStatics2(IInspectable):
                    get_IsTextScaleFactorEnabledProperty: _Callable

                class IFontIconStatics3(IInspectable):
                    get_MirroredWhenRightToLeftProperty: _Callable

                class IFrame(IInspectable):
                    get_CacheSize: _Callable
                    put_CacheSize: _Callable
                    get_CanGoBack: _Callable
                    get_CanGoForward: _Callable
                    get_CurrentSourcePageType: _Callable
                    get_SourcePageType: _Callable
                    put_SourcePageType: _Callable
                    get_BackStackDepth: _Callable
                    add_Navigated: _Callable
                    remove_Navigated: _Callable
                    add_Navigating: _Callable
                    remove_Navigating: _Callable
                    add_NavigationFailed: _Callable
                    remove_NavigationFailed: _Callable
                    add_NavigationStopped: _Callable
                    remove_NavigationStopped: _Callable
                    GoBack: _Callable
                    GoForward: _Callable
                    Navigate: _Callable
                    GetNavigationState: _Callable
                    SetNavigationState: _Callable

                class IFrame2(IInspectable):
                    get_BackStack: _Callable
                    get_ForwardStack: _Callable
                    Navigate: _Callable

                class IFrame3(IInspectable):
                    GoBack: _Callable

                class IFrame4(IInspectable):
                    SetNavigationStateWithNavigationControl: _Callable

                class IFrame5(IInspectable):
                    get_IsNavigationStackEnabled: _Callable
                    put_IsNavigationStackEnabled: _Callable
                    NavigateToType: _Callable

                class IFrameFactory(IInspectable):
                    CreateInstance: _Callable

                class IFrameStatics(IInspectable):
                    get_CacheSizeProperty: _Callable
                    get_CanGoBackProperty: _Callable
                    get_CanGoForwardProperty: _Callable
                    get_CurrentSourcePageTypeProperty: _Callable
                    get_SourcePageTypeProperty: _Callable
                    get_BackStackDepthProperty: _Callable

                class IFrameStatics2(IInspectable):
                    get_BackStackProperty: _Callable
                    get_ForwardStackProperty: _Callable

                class IFrameStatics5(IInspectable):
                    get_IsNavigationStackEnabledProperty: _Callable

                class IGrid(IInspectable):
                    get_RowDefinitions: _Callable
                    get_ColumnDefinitions: _Callable

                class IGrid2(IInspectable):
                    get_BorderBrush: _Callable
                    put_BorderBrush: _Callable
                    get_BorderThickness: _Callable
                    put_BorderThickness: _Callable
                    get_CornerRadius: _Callable
                    put_CornerRadius: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable

                class IGrid3(IInspectable):
                    get_RowSpacing: _Callable
                    put_RowSpacing: _Callable
                    get_ColumnSpacing: _Callable
                    put_ColumnSpacing: _Callable

                class IGrid4(IInspectable):
                    get_BackgroundSizing: _Callable
                    put_BackgroundSizing: _Callable

                class IGridFactory(IInspectable):
                    CreateInstance: _Callable

                class IGridStatics(IInspectable):
                    get_RowProperty: _Callable
                    GetRow: _Callable
                    SetRow: _Callable
                    get_ColumnProperty: _Callable
                    GetColumn: _Callable
                    SetColumn: _Callable
                    get_RowSpanProperty: _Callable
                    GetRowSpan: _Callable
                    SetRowSpan: _Callable
                    get_ColumnSpanProperty: _Callable
                    GetColumnSpan: _Callable
                    SetColumnSpan: _Callable

                class IGridStatics2(IInspectable):
                    get_BorderBrushProperty: _Callable
                    get_BorderThicknessProperty: _Callable
                    get_CornerRadiusProperty: _Callable
                    get_PaddingProperty: _Callable

                class IGridStatics3(IInspectable):
                    get_RowSpacingProperty: _Callable
                    get_ColumnSpacingProperty: _Callable

                class IGridStatics4(IInspectable):
                    get_BackgroundSizingProperty: _Callable

                class IGridView(IInspectable):
                    pass

                class IGridViewFactory(IInspectable):
                    CreateInstance: _Callable

                class IGridViewHeaderItem(IInspectable):
                    pass

                class IGridViewHeaderItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IGridViewItem(IInspectable):
                    get_TemplateSettings: _Callable

                class IGridViewItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IGroupItem(IInspectable):
                    pass

                class IGroupItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IGroupStyle(IInspectable):
                    get_Panel: _Callable
                    put_Panel: _Callable
                    get_ContainerStyle: _Callable
                    put_ContainerStyle: _Callable
                    get_ContainerStyleSelector: _Callable
                    put_ContainerStyleSelector: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_HeaderTemplateSelector: _Callable
                    put_HeaderTemplateSelector: _Callable
                    get_HidesIfEmpty: _Callable
                    put_HidesIfEmpty: _Callable

                class IGroupStyle2(IInspectable):
                    get_HeaderContainerStyle: _Callable
                    put_HeaderContainerStyle: _Callable

                class IGroupStyleFactory(IInspectable):
                    CreateInstance: _Callable

                class IGroupStyleSelector(IInspectable):
                    SelectGroupStyle: _Callable

                class IGroupStyleSelectorFactory(IInspectable):
                    CreateInstance: _Callable

                class IGroupStyleSelectorOverrides(IInspectable):
                    SelectGroupStyleCore: _Callable

                class IHandwritingPanelClosedEventArgs(IInspectable):
                    pass

                class IHandwritingPanelOpenedEventArgs(IInspectable):
                    pass

                class IHandwritingView(IInspectable):
                    get_PlacementTarget: _Callable
                    put_PlacementTarget: _Callable
                    get_PlacementAlignment: _Callable
                    put_PlacementAlignment: _Callable
                    get_IsOpen: _Callable
                    get_AreCandidatesEnabled: _Callable
                    put_AreCandidatesEnabled: _Callable
                    add_Opened: _Callable
                    remove_Opened: _Callable
                    add_Closed: _Callable
                    remove_Closed: _Callable
                    TryClose: _Callable
                    TryOpen: _Callable

                class IHandwritingView2(IInspectable):
                    get_IsSwitchToKeyboardEnabled: _Callable
                    put_IsSwitchToKeyboardEnabled: _Callable
                    get_IsCommandBarOpen: _Callable
                    put_IsCommandBarOpen: _Callable
                    get_InputDeviceTypes: _Callable
                    put_InputDeviceTypes: _Callable
                    add_CandidatesChanged: _Callable
                    remove_CandidatesChanged: _Callable
                    add_TextSubmitted: _Callable
                    remove_TextSubmitted: _Callable
                    GetCandidates: _Callable
                    SelectCandidate: _Callable

                class IHandwritingViewCandidatesChangedEventArgs(IInspectable):
                    get_CandidatesSessionId: _Callable

                class IHandwritingViewFactory(IInspectable):
                    CreateInstance: _Callable

                class IHandwritingViewStatics(IInspectable):
                    get_PlacementTargetProperty: _Callable
                    get_PlacementAlignmentProperty: _Callable
                    get_IsOpenProperty: _Callable
                    get_AreCandidatesEnabledProperty: _Callable

                class IHandwritingViewStatics2(IInspectable):
                    get_IsSwitchToKeyboardEnabledProperty: _Callable
                    get_IsCommandBarOpenProperty: _Callable

                class IHandwritingViewTextSubmittedEventArgs(IInspectable):
                    pass

                class IHub(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    get_DefaultSectionIndex: _Callable
                    put_DefaultSectionIndex: _Callable
                    get_Sections: _Callable
                    get_SectionsInView: _Callable
                    get_SectionHeaders: _Callable
                    add_SectionHeaderClick: _Callable
                    remove_SectionHeaderClick: _Callable
                    add_SectionsInViewChanged: _Callable
                    remove_SectionsInViewChanged: _Callable
                    ScrollToSection: _Callable

                class IHubFactory(IInspectable):
                    CreateInstance: _Callable

                class IHubSection(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_ContentTemplate: _Callable
                    put_ContentTemplate: _Callable
                    get_IsHeaderInteractive: _Callable
                    put_IsHeaderInteractive: _Callable

                class IHubSectionFactory(IInspectable):
                    CreateInstance: _Callable

                class IHubSectionHeaderClickEventArgs(IInspectable):
                    get_Section: _Callable

                class IHubSectionStatics(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_ContentTemplateProperty: _Callable
                    get_IsHeaderInteractiveProperty: _Callable

                class IHubStatics(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_DefaultSectionIndexProperty: _Callable
                    get_SemanticZoomOwnerProperty: _Callable
                    get_IsActiveViewProperty: _Callable
                    get_IsZoomedInViewProperty: _Callable

                class IHyperlinkButton(IInspectable):
                    get_NavigateUri: _Callable
                    put_NavigateUri: _Callable

                class IHyperlinkButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IHyperlinkButtonStatics(IInspectable):
                    get_NavigateUriProperty: _Callable

                class IIconElement(IInspectable):
                    get_Foreground: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                              _type.HRESULT]
                    put_Foreground: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                              _type.HRESULT]

                class IIconElementFactory(IInspectable):
                    pass

                class IIconElementStatics(IInspectable):
                    get_ForegroundProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]

                class IIconSource(IInspectable):
                    get_Foreground: _Callable
                    put_Foreground: _Callable

                class IIconSourceElement(IInspectable):
                    get_IconSource: _Callable
                    put_IconSource: _Callable

                class IIconSourceElementFactory(IInspectable):
                    CreateInstance: _Callable

                class IIconSourceElementStatics(IInspectable):
                    get_IconSourceProperty: _Callable

                class IIconSourceFactory(IInspectable):
                    pass

                class IIconSourceStatics(IInspectable):
                    get_ForegroundProperty: _Callable

                class IImage(IInspectable):
                    get_Source: _Callable
                    put_Source: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable
                    get_NineGrid: _Callable
                    put_NineGrid: _Callable
                    get_PlayToSource: _Callable
                    add_ImageFailed: _Callable
                    remove_ImageFailed: _Callable
                    add_ImageOpened: _Callable
                    remove_ImageOpened: _Callable

                class IImage2(IInspectable):
                    GetAsCastingSource: _Callable

                class IImage3(IInspectable):
                    GetAlphaMask: _Callable

                class IImageStatics(IInspectable):
                    get_SourceProperty: _Callable
                    get_StretchProperty: _Callable
                    get_NineGridProperty: _Callable
                    get_PlayToSourceProperty: _Callable

                class IInkCanvas(IInspectable):
                    get_InkPresenter: _Callable

                class IInkCanvasFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbar(IInspectable):
                    get_InitialControls: _Callable
                    put_InitialControls: _Callable
                    get_Children: _Callable
                    get_ActiveTool: _Callable
                    put_ActiveTool: _Callable
                    get_InkDrawingAttributes: _Callable
                    get_IsRulerButtonChecked: _Callable
                    put_IsRulerButtonChecked: _Callable
                    get_TargetInkCanvas: _Callable
                    put_TargetInkCanvas: _Callable
                    add_ActiveToolChanged: _Callable
                    remove_ActiveToolChanged: _Callable
                    add_InkDrawingAttributesChanged: _Callable
                    remove_InkDrawingAttributesChanged: _Callable
                    add_EraseAllClicked: _Callable
                    remove_EraseAllClicked: _Callable
                    add_IsRulerButtonCheckedChanged: _Callable
                    remove_IsRulerButtonCheckedChanged: _Callable
                    GetToolButton: _Callable
                    GetToggleButton: _Callable

                class IInkToolbar2(IInspectable):
                    get_IsStencilButtonChecked: _Callable
                    put_IsStencilButtonChecked: _Callable
                    get_ButtonFlyoutPlacement: _Callable
                    put_ButtonFlyoutPlacement: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    add_IsStencilButtonCheckedChanged: _Callable
                    remove_IsStencilButtonCheckedChanged: _Callable
                    GetMenuButton: _Callable

                class IInkToolbar3(IInspectable):
                    get_TargetInkPresenter: _Callable
                    put_TargetInkPresenter: _Callable

                class IInkToolbarBallpointPenButton(IInspectable):
                    pass

                class IInkToolbarBallpointPenButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarCustomPen(IInspectable):
                    CreateInkDrawingAttributes: _Callable

                class IInkToolbarCustomPenButton(IInspectable):
                    get_CustomPen: _Callable
                    put_CustomPen: _Callable
                    get_ConfigurationContent: _Callable
                    put_ConfigurationContent: _Callable

                class IInkToolbarCustomPenButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarCustomPenButtonStatics(IInspectable):
                    get_CustomPenProperty: _Callable
                    get_ConfigurationContentProperty: _Callable

                class IInkToolbarCustomPenFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarCustomPenOverrides(IInspectable):
                    CreateInkDrawingAttributesCore: _Callable

                class IInkToolbarCustomToggleButton(IInspectable):
                    pass

                class IInkToolbarCustomToggleButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarCustomToolButton(IInspectable):
                    get_ConfigurationContent: _Callable
                    put_ConfigurationContent: _Callable

                class IInkToolbarCustomToolButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarCustomToolButtonStatics(IInspectable):
                    get_ConfigurationContentProperty: _Callable

                class IInkToolbarEraserButton(IInspectable):
                    pass

                class IInkToolbarEraserButton2(IInspectable):
                    get_IsClearAllVisible: _Callable
                    put_IsClearAllVisible: _Callable

                class IInkToolbarEraserButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarEraserButtonStatics2(IInspectable):
                    get_IsClearAllVisibleProperty: _Callable

                class IInkToolbarFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarFlyoutItem(IInspectable):
                    get_Kind: _Callable
                    put_Kind: _Callable
                    get_IsChecked: _Callable
                    put_IsChecked: _Callable
                    add_Checked: _Callable
                    remove_Checked: _Callable
                    add_Unchecked: _Callable
                    remove_Unchecked: _Callable

                class IInkToolbarFlyoutItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarFlyoutItemStatics(IInspectable):
                    get_KindProperty: _Callable
                    get_IsCheckedProperty: _Callable

                class IInkToolbarHighlighterButton(IInspectable):
                    pass

                class IInkToolbarHighlighterButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarIsStencilButtonCheckedChangedEventArgs(IInspectable):
                    get_StencilButton: _Callable
                    get_StencilKind: _Callable

                class IInkToolbarMenuButton(IInspectable):
                    get_MenuKind: _Callable
                    get_IsExtensionGlyphShown: _Callable
                    put_IsExtensionGlyphShown: _Callable

                class IInkToolbarMenuButtonFactory(IInspectable):
                    pass

                class IInkToolbarMenuButtonStatics(IInspectable):
                    get_IsExtensionGlyphShownProperty: _Callable

                class IInkToolbarPenButton(IInspectable):
                    get_Palette: _Callable
                    put_Palette: _Callable
                    get_MinStrokeWidth: _Callable
                    put_MinStrokeWidth: _Callable
                    get_MaxStrokeWidth: _Callable
                    put_MaxStrokeWidth: _Callable
                    get_SelectedBrush: _Callable
                    get_SelectedBrushIndex: _Callable
                    put_SelectedBrushIndex: _Callable
                    get_SelectedStrokeWidth: _Callable
                    put_SelectedStrokeWidth: _Callable

                class IInkToolbarPenButtonFactory(IInspectable):
                    pass

                class IInkToolbarPenButtonStatics(IInspectable):
                    get_PaletteProperty: _Callable
                    get_MinStrokeWidthProperty: _Callable
                    get_MaxStrokeWidthProperty: _Callable
                    get_SelectedBrushProperty: _Callable
                    get_SelectedBrushIndexProperty: _Callable
                    get_SelectedStrokeWidthProperty: _Callable

                class IInkToolbarPenConfigurationControl(IInspectable):
                    get_PenButton: _Callable

                class IInkToolbarPenConfigurationControlFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarPenConfigurationControlStatics(IInspectable):
                    get_PenButtonProperty: _Callable

                class IInkToolbarPencilButton(IInspectable):
                    pass

                class IInkToolbarPencilButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarRulerButton(IInspectable):
                    get_Ruler: _Callable

                class IInkToolbarRulerButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarRulerButtonStatics(IInspectable):
                    get_RulerProperty: _Callable

                class IInkToolbarStatics(IInspectable):
                    get_InitialControlsProperty: _Callable
                    get_ChildrenProperty: _Callable
                    get_ActiveToolProperty: _Callable
                    get_InkDrawingAttributesProperty: _Callable
                    get_IsRulerButtonCheckedProperty: _Callable
                    get_TargetInkCanvasProperty: _Callable

                class IInkToolbarStatics2(IInspectable):
                    get_IsStencilButtonCheckedProperty: _Callable
                    get_ButtonFlyoutPlacementProperty: _Callable
                    get_OrientationProperty: _Callable

                class IInkToolbarStatics3(IInspectable):
                    get_TargetInkPresenterProperty: _Callable

                class IInkToolbarStencilButton(IInspectable):
                    get_Ruler: _Callable
                    get_Protractor: _Callable
                    get_SelectedStencil: _Callable
                    put_SelectedStencil: _Callable
                    get_IsRulerItemVisible: _Callable
                    put_IsRulerItemVisible: _Callable
                    get_IsProtractorItemVisible: _Callable
                    put_IsProtractorItemVisible: _Callable

                class IInkToolbarStencilButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IInkToolbarStencilButtonStatics(IInspectable):
                    get_RulerProperty: _Callable
                    get_ProtractorProperty: _Callable
                    get_SelectedStencilProperty: _Callable
                    get_IsRulerItemVisibleProperty: _Callable
                    get_IsProtractorItemVisibleProperty: _Callable

                class IInkToolbarToggleButton(IInspectable):
                    get_ToggleKind: _Callable

                class IInkToolbarToggleButtonFactory(IInspectable):
                    pass

                class IInkToolbarToolButton(IInspectable):
                    get_ToolKind: _Callable
                    get_IsExtensionGlyphShown: _Callable
                    put_IsExtensionGlyphShown: _Callable

                class IInkToolbarToolButtonFactory(IInspectable):
                    pass

                class IInkToolbarToolButtonStatics(IInspectable):
                    get_IsExtensionGlyphShownProperty: _Callable

                class IInsertionPanel(IInspectable):
                    GetInsertionIndexes: _Callable

                class IIsTextTrimmedChangedEventArgs(IInspectable):
                    pass

                class IItemClickEventArgs(IInspectable):
                    get_ClickedItem: _Callable

                class IItemContainerGenerator(IInspectable):
                    add_ItemsChanged: _Callable
                    remove_ItemsChanged: _Callable
                    ItemFromContainer: _Callable
                    ContainerFromItem: _Callable
                    IndexFromContainer: _Callable
                    ContainerFromIndex: _Callable
                    GetItemContainerGeneratorForPanel: _Callable
                    StartAt: _Callable
                    Stop: _Callable
                    GenerateNext: _Callable
                    PrepareItemContainer: _Callable
                    RemoveAll: _Callable
                    Remove: _Callable
                    GeneratorPositionFromIndex: _Callable
                    IndexFromGeneratorPosition: _Callable
                    Recycle: _Callable

                class IItemContainerMapping(IInspectable):
                    ItemFromContainer: _Callable
                    ContainerFromItem: _Callable
                    IndexFromContainer: _Callable
                    ContainerFromIndex: _Callable

                class IItemsControl(IInspectable):
                    get_ItemsSource: _Callable
                    put_ItemsSource: _Callable
                    get_Items: _Callable
                    get_ItemTemplate: _Callable
                    put_ItemTemplate: _Callable
                    get_ItemTemplateSelector: _Callable
                    put_ItemTemplateSelector: _Callable
                    get_ItemsPanel: _Callable
                    put_ItemsPanel: _Callable
                    get_DisplayMemberPath: _Callable
                    put_DisplayMemberPath: _Callable
                    get_ItemContainerStyle: _Callable
                    put_ItemContainerStyle: _Callable
                    get_ItemContainerStyleSelector: _Callable
                    put_ItemContainerStyleSelector: _Callable
                    get_ItemContainerGenerator: _Callable
                    get_ItemContainerTransitions: _Callable
                    put_ItemContainerTransitions: _Callable
                    get_GroupStyle: _Callable
                    get_GroupStyleSelector: _Callable
                    put_GroupStyleSelector: _Callable
                    get_IsGrouping: _Callable

                class IItemsControl2(IInspectable):
                    get_ItemsPanelRoot: _Callable

                class IItemsControl3(IInspectable):
                    GroupHeaderContainerFromItemContainer: _Callable

                class IItemsControlFactory(IInspectable):
                    CreateInstance: _Callable

                class IItemsControlOverrides(IInspectable):
                    IsItemItsOwnContainerOverride: _Callable
                    GetContainerForItemOverride: _Callable
                    ClearContainerForItemOverride: _Callable
                    PrepareContainerForItemOverride: _Callable
                    OnItemsChanged: _Callable
                    OnItemContainerStyleChanged: _Callable
                    OnItemContainerStyleSelectorChanged: _Callable
                    OnItemTemplateChanged: _Callable
                    OnItemTemplateSelectorChanged: _Callable
                    OnGroupStyleSelectorChanged: _Callable

                class IItemsControlStatics(IInspectable):
                    get_ItemsSourceProperty: _Callable
                    get_ItemTemplateProperty: _Callable
                    get_ItemTemplateSelectorProperty: _Callable
                    get_ItemsPanelProperty: _Callable
                    get_DisplayMemberPathProperty: _Callable
                    get_ItemContainerStyleProperty: _Callable
                    get_ItemContainerStyleSelectorProperty: _Callable
                    get_ItemContainerTransitionsProperty: _Callable
                    get_GroupStyleSelectorProperty: _Callable
                    get_IsGroupingProperty: _Callable
                    GetItemsOwner: _Callable
                    ItemsControlFromItemContainer: _Callable

                class IItemsPanelTemplate(IInspectable):
                    pass

                class IItemsPickedEventArgs(IInspectable):
                    get_AddedItems: _Callable
                    get_RemovedItems: _Callable

                class IItemsPresenter(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_HeaderTransitions: _Callable
                    put_HeaderTransitions: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable

                class IItemsPresenter2(IInspectable):
                    get_Footer: _Callable
                    put_Footer: _Callable
                    get_FooterTemplate: _Callable
                    put_FooterTemplate: _Callable
                    get_FooterTransitions: _Callable
                    put_FooterTransitions: _Callable

                class IItemsPresenterStatics(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_HeaderTransitionsProperty: _Callable
                    get_PaddingProperty: _Callable

                class IItemsPresenterStatics2(IInspectable):
                    get_FooterProperty: _Callable
                    get_FooterTemplateProperty: _Callable
                    get_FooterTransitionsProperty: _Callable

                class IItemsStackPanel(IInspectable):
                    get_GroupPadding: _Callable
                    put_GroupPadding: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    get_FirstCacheIndex: _Callable
                    get_FirstVisibleIndex: _Callable
                    get_LastVisibleIndex: _Callable
                    get_LastCacheIndex: _Callable
                    get_ScrollingDirection: _Callable
                    get_GroupHeaderPlacement: _Callable
                    put_GroupHeaderPlacement: _Callable
                    get_ItemsUpdatingScrollMode: _Callable
                    put_ItemsUpdatingScrollMode: _Callable
                    get_CacheLength: _Callable
                    put_CacheLength: _Callable

                class IItemsStackPanel2(IInspectable):
                    get_AreStickyGroupHeadersEnabled: _Callable
                    put_AreStickyGroupHeadersEnabled: _Callable

                class IItemsStackPanelStatics(IInspectable):
                    get_GroupPaddingProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_GroupHeaderPlacementProperty: _Callable
                    get_CacheLengthProperty: _Callable

                class IItemsStackPanelStatics2(IInspectable):
                    get_AreStickyGroupHeadersEnabledProperty: _Callable

                class IItemsWrapGrid(IInspectable):
                    get_GroupPadding: _Callable
                    put_GroupPadding: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    get_MaximumRowsOrColumns: _Callable
                    put_MaximumRowsOrColumns: _Callable
                    get_ItemWidth: _Callable
                    put_ItemWidth: _Callable
                    get_ItemHeight: _Callable
                    put_ItemHeight: _Callable
                    get_FirstCacheIndex: _Callable
                    get_FirstVisibleIndex: _Callable
                    get_LastVisibleIndex: _Callable
                    get_LastCacheIndex: _Callable
                    get_ScrollingDirection: _Callable
                    get_GroupHeaderPlacement: _Callable
                    put_GroupHeaderPlacement: _Callable
                    get_CacheLength: _Callable
                    put_CacheLength: _Callable

                class IItemsWrapGrid2(IInspectable):
                    get_AreStickyGroupHeadersEnabled: _Callable
                    put_AreStickyGroupHeadersEnabled: _Callable

                class IItemsWrapGridStatics(IInspectable):
                    get_GroupPaddingProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_MaximumRowsOrColumnsProperty: _Callable
                    get_ItemWidthProperty: _Callable
                    get_ItemHeightProperty: _Callable
                    get_GroupHeaderPlacementProperty: _Callable
                    get_CacheLengthProperty: _Callable

                class IItemsWrapGridStatics2(IInspectable):
                    get_AreStickyGroupHeadersEnabledProperty: _Callable

                class IListBox(IInspectable):
                    get_SelectedItems: _Callable
                    get_SelectionMode: _Callable
                    put_SelectionMode: _Callable
                    ScrollIntoView: _Callable
                    SelectAll: _Callable

                class IListBox2(IInspectable):
                    get_SingleSelectionFollowsFocus: _Callable
                    put_SingleSelectionFollowsFocus: _Callable

                class IListBoxFactory(IInspectable):
                    CreateInstance: _Callable

                class IListBoxItem(IInspectable):
                    pass

                class IListBoxItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IListBoxStatics(IInspectable):
                    get_SelectionModeProperty: _Callable

                class IListBoxStatics2(IInspectable):
                    get_SingleSelectionFollowsFocusProperty: _Callable

                class IListPickerFlyout(IInspectable):
                    get_ItemsSource: _Callable
                    put_ItemsSource: _Callable
                    get_ItemTemplate: _Callable
                    put_ItemTemplate: _Callable
                    get_DisplayMemberPath: _Callable
                    put_DisplayMemberPath: _Callable
                    get_SelectionMode: _Callable
                    put_SelectionMode: _Callable
                    get_SelectedIndex: _Callable
                    put_SelectedIndex: _Callable
                    get_SelectedItem: _Callable
                    put_SelectedItem: _Callable
                    get_SelectedValue: _Callable
                    put_SelectedValue: _Callable
                    get_SelectedValuePath: _Callable
                    put_SelectedValuePath: _Callable
                    get_SelectedItems: _Callable
                    add_ItemsPicked: _Callable
                    remove_ItemsPicked: _Callable
                    ShowAtAsync: _Callable

                class IListPickerFlyoutPresenter(IInspectable):
                    pass

                class IListPickerFlyoutStatics(IInspectable):
                    get_ItemsSourceProperty: _Callable
                    get_ItemTemplateProperty: _Callable
                    get_DisplayMemberPathProperty: _Callable
                    get_SelectionModeProperty: _Callable
                    get_SelectedIndexProperty: _Callable
                    get_SelectedItemProperty: _Callable
                    get_SelectedValueProperty: _Callable
                    get_SelectedValuePathProperty: _Callable

                class IListView(IInspectable):
                    pass

                class IListViewBase(IInspectable):
                    get_SelectedItems: _Callable
                    get_SelectionMode: _Callable
                    put_SelectionMode: _Callable
                    get_IsSwipeEnabled: _Callable
                    put_IsSwipeEnabled: _Callable
                    get_CanDragItems: _Callable
                    put_CanDragItems: _Callable
                    get_CanReorderItems: _Callable
                    put_CanReorderItems: _Callable
                    get_IsItemClickEnabled: _Callable
                    put_IsItemClickEnabled: _Callable
                    get_DataFetchSize: _Callable
                    put_DataFetchSize: _Callable
                    get_IncrementalLoadingThreshold: _Callable
                    put_IncrementalLoadingThreshold: _Callable
                    get_IncrementalLoadingTrigger: _Callable
                    put_IncrementalLoadingTrigger: _Callable
                    add_ItemClick: _Callable
                    remove_ItemClick: _Callable
                    add_DragItemsStarting: _Callable
                    remove_DragItemsStarting: _Callable
                    ScrollIntoView: _Callable
                    SelectAll: _Callable
                    LoadMoreItemsAsync: _Callable
                    ScrollIntoViewWithAlignment: _Callable
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_HeaderTransitions: _Callable
                    put_HeaderTransitions: _Callable

                class IListViewBase2(IInspectable):
                    get_ShowsScrollingPlaceholders: _Callable
                    put_ShowsScrollingPlaceholders: _Callable
                    add_ContainerContentChanging: _Callable
                    remove_ContainerContentChanging: _Callable
                    SetDesiredContainerUpdateDuration: _Callable
                    get_Footer: _Callable
                    put_Footer: _Callable
                    get_FooterTemplate: _Callable
                    put_FooterTemplate: _Callable
                    get_FooterTransitions: _Callable
                    put_FooterTransitions: _Callable

                class IListViewBase3(IInspectable):
                    get_ReorderMode: _Callable
                    put_ReorderMode: _Callable

                class IListViewBase4(IInspectable):
                    get_SelectedRanges: _Callable
                    get_IsMultiSelectCheckBoxEnabled: _Callable
                    put_IsMultiSelectCheckBoxEnabled: _Callable
                    add_DragItemsCompleted: _Callable
                    remove_DragItemsCompleted: _Callable
                    add_ChoosingItemContainer: _Callable
                    remove_ChoosingItemContainer: _Callable
                    add_ChoosingGroupHeaderContainer: _Callable
                    remove_ChoosingGroupHeaderContainer: _Callable
                    SelectRange: _Callable
                    DeselectRange: _Callable

                class IListViewBase5(IInspectable):
                    get_SingleSelectionFollowsFocus: _Callable
                    put_SingleSelectionFollowsFocus: _Callable
                    IsDragSource: _Callable

                class IListViewBase6(IInspectable):
                    TryStartConnectedAnimationAsync: _Callable
                    PrepareConnectedAnimation: _Callable

                class IListViewBaseFactory(IInspectable):
                    CreateInstance: _Callable

                class IListViewBaseHeaderItem(IInspectable):
                    pass

                class IListViewBaseHeaderItemFactory(IInspectable):
                    pass

                class IListViewBaseStatics(IInspectable):
                    get_SelectionModeProperty: _Callable
                    get_IsSwipeEnabledProperty: _Callable
                    get_CanDragItemsProperty: _Callable
                    get_CanReorderItemsProperty: _Callable
                    get_IsItemClickEnabledProperty: _Callable
                    get_DataFetchSizeProperty: _Callable
                    get_IncrementalLoadingThresholdProperty: _Callable
                    get_IncrementalLoadingTriggerProperty: _Callable
                    get_SemanticZoomOwnerProperty: _Callable
                    get_IsActiveViewProperty: _Callable
                    get_IsZoomedInViewProperty: _Callable
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_HeaderTransitionsProperty: _Callable

                class IListViewBaseStatics2(IInspectable):
                    get_ShowsScrollingPlaceholdersProperty: _Callable
                    get_FooterProperty: _Callable
                    get_FooterTemplateProperty: _Callable
                    get_FooterTransitionsProperty: _Callable

                class IListViewBaseStatics3(IInspectable):
                    get_ReorderModeProperty: _Callable

                class IListViewBaseStatics4(IInspectable):
                    get_IsMultiSelectCheckBoxEnabledProperty: _Callable

                class IListViewBaseStatics5(IInspectable):
                    get_SingleSelectionFollowsFocusProperty: _Callable

                class IListViewFactory(IInspectable):
                    CreateInstance: _Callable

                class IListViewHeaderItem(IInspectable):
                    pass

                class IListViewHeaderItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IListViewItem(IInspectable):
                    get_TemplateSettings: _Callable

                class IListViewItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IListViewPersistenceHelper(IInspectable):
                    pass

                class IListViewPersistenceHelperStatics(IInspectable):
                    GetRelativeScrollPosition: _Callable
                    SetRelativeScrollPositionAsync: _Callable

                class IMediaElement(IInspectable):
                    get_PosterSource: _Callable
                    put_PosterSource: _Callable
                    get_Source: _Callable
                    put_Source: _Callable
                    get_IsMuted: _Callable
                    put_IsMuted: _Callable
                    get_IsAudioOnly: _Callable
                    get_AutoPlay: _Callable
                    put_AutoPlay: _Callable
                    get_Volume: _Callable
                    put_Volume: _Callable
                    get_Balance: _Callable
                    put_Balance: _Callable
                    get_NaturalVideoHeight: _Callable
                    get_NaturalVideoWidth: _Callable
                    get_NaturalDuration: _Callable
                    get_Position: _Callable
                    put_Position: _Callable
                    get_DownloadProgress: _Callable
                    get_BufferingProgress: _Callable
                    get_DownloadProgressOffset: _Callable
                    get_CurrentState: _Callable
                    get_Markers: _Callable
                    get_CanSeek: _Callable
                    get_CanPause: _Callable
                    get_AudioStreamCount: _Callable
                    get_AudioStreamIndex: _Callable
                    put_AudioStreamIndex: _Callable
                    get_PlaybackRate: _Callable
                    put_PlaybackRate: _Callable
                    get_IsLooping: _Callable
                    put_IsLooping: _Callable
                    get_PlayToSource: _Callable
                    get_DefaultPlaybackRate: _Callable
                    put_DefaultPlaybackRate: _Callable
                    get_AspectRatioWidth: _Callable
                    get_AspectRatioHeight: _Callable
                    get_RealTimePlayback: _Callable
                    put_RealTimePlayback: _Callable
                    get_AudioCategory: _Callable
                    put_AudioCategory: _Callable
                    get_AudioDeviceType: _Callable
                    put_AudioDeviceType: _Callable
                    get_ProtectionManager: _Callable
                    put_ProtectionManager: _Callable
                    get_Stereo3DVideoPackingMode: _Callable
                    put_Stereo3DVideoPackingMode: _Callable
                    get_Stereo3DVideoRenderMode: _Callable
                    put_Stereo3DVideoRenderMode: _Callable
                    get_IsStereo3DVideo: _Callable
                    add_MediaOpened: _Callable
                    remove_MediaOpened: _Callable
                    add_MediaEnded: _Callable
                    remove_MediaEnded: _Callable
                    add_MediaFailed: _Callable
                    remove_MediaFailed: _Callable
                    add_DownloadProgressChanged: _Callable
                    remove_DownloadProgressChanged: _Callable
                    add_BufferingProgressChanged: _Callable
                    remove_BufferingProgressChanged: _Callable
                    add_CurrentStateChanged: _Callable
                    remove_CurrentStateChanged: _Callable
                    add_MarkerReached: _Callable
                    remove_MarkerReached: _Callable
                    add_RateChanged: _Callable
                    remove_RateChanged: _Callable
                    add_VolumeChanged: _Callable
                    remove_VolumeChanged: _Callable
                    add_SeekCompleted: _Callable
                    remove_SeekCompleted: _Callable
                    Stop: _Callable
                    Play: _Callable
                    Pause: _Callable
                    CanPlayType: _Callable
                    SetSource: _Callable
                    GetAudioStreamLanguage: _Callable
                    AddAudioEffect: _Callable
                    AddVideoEffect: _Callable
                    RemoveAllEffects: _Callable
                    get_ActualStereo3DVideoPackingMode: _Callable

                class IMediaElement2(IInspectable):
                    get_AreTransportControlsEnabled: _Callable
                    put_AreTransportControlsEnabled: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable
                    get_IsFullWindow: _Callable
                    put_IsFullWindow: _Callable
                    SetMediaStreamSource: _Callable
                    get_PlayToPreferredSourceUri: _Callable
                    put_PlayToPreferredSourceUri: _Callable

                class IMediaElement3(IInspectable):
                    get_TransportControls: _Callable
                    put_TransportControls: _Callable
                    add_PartialMediaFailureDetected: _Callable
                    remove_PartialMediaFailureDetected: _Callable
                    SetPlaybackSource: _Callable
                    GetAsCastingSource: _Callable

                class IMediaElementStatics(IInspectable):
                    get_PosterSourceProperty: _Callable
                    get_SourceProperty: _Callable
                    get_IsMutedProperty: _Callable
                    get_IsAudioOnlyProperty: _Callable
                    get_AutoPlayProperty: _Callable
                    get_VolumeProperty: _Callable
                    get_BalanceProperty: _Callable
                    get_NaturalVideoHeightProperty: _Callable
                    get_NaturalVideoWidthProperty: _Callable
                    get_NaturalDurationProperty: _Callable
                    get_PositionProperty: _Callable
                    get_DownloadProgressProperty: _Callable
                    get_BufferingProgressProperty: _Callable
                    get_DownloadProgressOffsetProperty: _Callable
                    get_CurrentStateProperty: _Callable
                    get_CanSeekProperty: _Callable
                    get_CanPauseProperty: _Callable
                    get_AudioStreamCountProperty: _Callable
                    get_AudioStreamIndexProperty: _Callable
                    get_PlaybackRateProperty: _Callable
                    get_IsLoopingProperty: _Callable
                    get_PlayToSourceProperty: _Callable
                    get_DefaultPlaybackRateProperty: _Callable
                    get_AspectRatioWidthProperty: _Callable
                    get_AspectRatioHeightProperty: _Callable
                    get_RealTimePlaybackProperty: _Callable
                    get_AudioCategoryProperty: _Callable
                    get_AudioDeviceTypeProperty: _Callable
                    get_ProtectionManagerProperty: _Callable
                    get_Stereo3DVideoPackingModeProperty: _Callable
                    get_Stereo3DVideoRenderModeProperty: _Callable
                    get_IsStereo3DVideoProperty: _Callable
                    get_ActualStereo3DVideoPackingModeProperty: _Callable

                class IMediaElementStatics2(IInspectable):
                    get_AreTransportControlsEnabledProperty: _Callable
                    get_StretchProperty: _Callable
                    get_IsFullWindowProperty: _Callable
                    get_PlayToPreferredSourceUriProperty: _Callable

                class IMediaPlayerElement(IInspectable):
                    get_Source: _Callable
                    put_Source: _Callable
                    get_TransportControls: _Callable
                    put_TransportControls: _Callable
                    get_AreTransportControlsEnabled: _Callable
                    put_AreTransportControlsEnabled: _Callable
                    get_PosterSource: _Callable
                    put_PosterSource: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable
                    get_AutoPlay: _Callable
                    put_AutoPlay: _Callable
                    get_IsFullWindow: _Callable
                    put_IsFullWindow: _Callable
                    get_MediaPlayer: _Callable
                    SetMediaPlayer: _Callable

                class IMediaPlayerElementFactory(IInspectable):
                    CreateInstance: _Callable

                class IMediaPlayerElementStatics(IInspectable):
                    get_SourceProperty: _Callable
                    get_AreTransportControlsEnabledProperty: _Callable
                    get_PosterSourceProperty: _Callable
                    get_StretchProperty: _Callable
                    get_AutoPlayProperty: _Callable
                    get_IsFullWindowProperty: _Callable
                    get_MediaPlayerProperty: _Callable

                class IMediaPlayerPresenter(IInspectable):
                    get_MediaPlayer: _Callable
                    put_MediaPlayer: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable
                    get_IsFullWindow: _Callable
                    put_IsFullWindow: _Callable

                class IMediaPlayerPresenterFactory(IInspectable):
                    CreateInstance: _Callable

                class IMediaPlayerPresenterStatics(IInspectable):
                    get_MediaPlayerProperty: _Callable
                    get_StretchProperty: _Callable
                    get_IsFullWindowProperty: _Callable

                class IMediaTransportControls(IInspectable):
                    get_IsFullWindowButtonVisible: _Callable
                    put_IsFullWindowButtonVisible: _Callable
                    get_IsFullWindowEnabled: _Callable
                    put_IsFullWindowEnabled: _Callable
                    get_IsZoomButtonVisible: _Callable
                    put_IsZoomButtonVisible: _Callable
                    get_IsZoomEnabled: _Callable
                    put_IsZoomEnabled: _Callable
                    get_IsFastForwardButtonVisible: _Callable
                    put_IsFastForwardButtonVisible: _Callable
                    get_IsFastForwardEnabled: _Callable
                    put_IsFastForwardEnabled: _Callable
                    get_IsFastRewindButtonVisible: _Callable
                    put_IsFastRewindButtonVisible: _Callable
                    get_IsFastRewindEnabled: _Callable
                    put_IsFastRewindEnabled: _Callable
                    get_IsStopButtonVisible: _Callable
                    put_IsStopButtonVisible: _Callable
                    get_IsStopEnabled: _Callable
                    put_IsStopEnabled: _Callable
                    get_IsVolumeButtonVisible: _Callable
                    put_IsVolumeButtonVisible: _Callable
                    get_IsVolumeEnabled: _Callable
                    put_IsVolumeEnabled: _Callable
                    get_IsPlaybackRateButtonVisible: _Callable
                    put_IsPlaybackRateButtonVisible: _Callable
                    get_IsPlaybackRateEnabled: _Callable
                    put_IsPlaybackRateEnabled: _Callable
                    get_IsSeekBarVisible: _Callable
                    put_IsSeekBarVisible: _Callable
                    get_IsSeekEnabled: _Callable
                    put_IsSeekEnabled: _Callable
                    get_IsCompact: _Callable
                    put_IsCompact: _Callable

                class IMediaTransportControls2(IInspectable):
                    get_IsSkipForwardButtonVisible: _Callable
                    put_IsSkipForwardButtonVisible: _Callable
                    get_IsSkipForwardEnabled: _Callable
                    put_IsSkipForwardEnabled: _Callable
                    get_IsSkipBackwardButtonVisible: _Callable
                    put_IsSkipBackwardButtonVisible: _Callable
                    get_IsSkipBackwardEnabled: _Callable
                    put_IsSkipBackwardEnabled: _Callable
                    get_IsNextTrackButtonVisible: _Callable
                    put_IsNextTrackButtonVisible: _Callable
                    get_IsPreviousTrackButtonVisible: _Callable
                    put_IsPreviousTrackButtonVisible: _Callable
                    get_FastPlayFallbackBehaviour: _Callable
                    put_FastPlayFallbackBehaviour: _Callable
                    add_ThumbnailRequested: _Callable
                    remove_ThumbnailRequested: _Callable

                class IMediaTransportControls3(IInspectable):
                    get_ShowAndHideAutomatically: _Callable
                    put_ShowAndHideAutomatically: _Callable
                    get_IsRepeatEnabled: _Callable
                    put_IsRepeatEnabled: _Callable
                    get_IsRepeatButtonVisible: _Callable
                    put_IsRepeatButtonVisible: _Callable
                    Show: _Callable
                    Hide: _Callable

                class IMediaTransportControls4(IInspectable):
                    get_IsCompactOverlayButtonVisible: _Callable
                    put_IsCompactOverlayButtonVisible: _Callable
                    get_IsCompactOverlayEnabled: _Callable
                    put_IsCompactOverlayEnabled: _Callable

                class IMediaTransportControlsFactory(IInspectable):
                    CreateInstance: _Callable

                class IMediaTransportControlsHelper(IInspectable):
                    pass

                class IMediaTransportControlsHelperStatics(IInspectable):
                    get_DropoutOrderProperty: _Callable
                    GetDropoutOrder: _Callable
                    SetDropoutOrder: _Callable

                class IMediaTransportControlsStatics(IInspectable):
                    get_IsFullWindowButtonVisibleProperty: _Callable
                    get_IsFullWindowEnabledProperty: _Callable
                    get_IsZoomButtonVisibleProperty: _Callable
                    get_IsZoomEnabledProperty: _Callable
                    get_IsFastForwardButtonVisibleProperty: _Callable
                    get_IsFastForwardEnabledProperty: _Callable
                    get_IsFastRewindButtonVisibleProperty: _Callable
                    get_IsFastRewindEnabledProperty: _Callable
                    get_IsStopButtonVisibleProperty: _Callable
                    get_IsStopEnabledProperty: _Callable
                    get_IsVolumeButtonVisibleProperty: _Callable
                    get_IsVolumeEnabledProperty: _Callable
                    get_IsPlaybackRateButtonVisibleProperty: _Callable
                    get_IsPlaybackRateEnabledProperty: _Callable
                    get_IsSeekBarVisibleProperty: _Callable
                    get_IsSeekEnabledProperty: _Callable
                    get_IsCompactProperty: _Callable

                class IMediaTransportControlsStatics2(IInspectable):
                    get_IsSkipForwardButtonVisibleProperty: _Callable
                    get_IsSkipForwardEnabledProperty: _Callable
                    get_IsSkipBackwardButtonVisibleProperty: _Callable
                    get_IsSkipBackwardEnabledProperty: _Callable
                    get_IsNextTrackButtonVisibleProperty: _Callable
                    get_IsPreviousTrackButtonVisibleProperty: _Callable
                    get_FastPlayFallbackBehaviourProperty: _Callable

                class IMediaTransportControlsStatics3(IInspectable):
                    get_ShowAndHideAutomaticallyProperty: _Callable
                    get_IsRepeatEnabledProperty: _Callable
                    get_IsRepeatButtonVisibleProperty: _Callable

                class IMediaTransportControlsStatics4(IInspectable):
                    get_IsCompactOverlayButtonVisibleProperty: _Callable
                    get_IsCompactOverlayEnabledProperty: _Callable

                class IMenuBar(IInspectable):
                    get_Items: _Callable

                class IMenuBarFactory(IInspectable):
                    CreateInstance: _Callable

                class IMenuBarItem(IInspectable):
                    get_Title: _Callable
                    put_Title: _Callable
                    get_Items: _Callable

                class IMenuBarItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IMenuBarItemFlyout(IInspectable):
                    pass

                class IMenuBarItemFlyoutFactory(IInspectable):
                    CreateInstance: _Callable

                class IMenuBarItemStatics(IInspectable):
                    get_TitleProperty: _Callable
                    get_ItemsProperty: _Callable

                class IMenuBarStatics(IInspectable):
                    get_ItemsProperty: _Callable

                class IMenuFlyout(IInspectable):
                    get_Items: _Callable[[_Pointer[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.IMenuFlyoutItemBase]]],
                                         _type.HRESULT]
                    get_MenuFlyoutPresenterStyle: _Callable
                    put_MenuFlyoutPresenterStyle: _Callable

                class IMenuFlyout2(IInspectable):
                    ShowAt: _Callable[[Windows.UI.Xaml.IUIElement,
                                       _struct.Windows.Foundation.Point],
                                      _type.HRESULT]

                class IMenuFlyoutFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IMenuFlyout]],
                                              _type.HRESULT]

                class IMenuFlyoutItem(IInspectable):
                    get_Text: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]
                    put_Text: _Callable[[_type.HSTRING],
                                        _type.HRESULT]
                    get_Command: _Callable
                    put_Command: _Callable
                    get_CommandParameter: _Callable[[_Pointer[IInspectable]],
                                                    _type.HRESULT]
                    put_CommandParameter: _Callable[[IInspectable],
                                                    _type.HRESULT]
                    add_Click: _Callable
                    remove_Click: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]

                class IMenuFlyoutItem2(IInspectable):
                    get_Icon: _Callable[[_Pointer[Windows.UI.Xaml.Controls.IIconElement]],
                                        _type.HRESULT]
                    put_Icon: _Callable[[Windows.UI.Xaml.Controls.IIconElement],
                                        _type.HRESULT]

                class IMenuFlyoutItem3(IInspectable):
                    get_KeyboardAcceleratorTextOverride: _Callable[[_Pointer[_type.HSTRING]],
                                                                   _type.HRESULT]
                    put_KeyboardAcceleratorTextOverride: _Callable[[_type.HSTRING],
                                                                   _type.HRESULT]
                    get_TemplateSettings: _Callable[[_Pointer[Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings]],
                                                    _type.HRESULT]

                class IMenuFlyoutItemBase(IInspectable):
                    pass

                class IMenuFlyoutItemBaseFactory(IInspectable):
                    pass

                class IMenuFlyoutItemFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IMenuFlyoutItem]],
                                              _type.HRESULT]

                class IMenuFlyoutItemStatics(IInspectable):
                    get_TextProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]
                    get_CommandProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                    get_CommandParameterProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]

                class IMenuFlyoutItemStatics2(IInspectable):
                    get_IconProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]

                class IMenuFlyoutItemStatics3(IInspectable):
                    get_KeyboardAcceleratorTextOverrideProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                           _type.HRESULT]

                class IMenuFlyoutPresenter(IInspectable):
                    pass

                class IMenuFlyoutPresenter2(IInspectable):
                    get_TemplateSettings: _Callable[[_Pointer[Windows.UI.Xaml.Controls.Primitives.IMenuFlyoutPresenterTemplateSettings]],
                                                    _type.HRESULT]

                class IMenuFlyoutPresenter3(IInspectable):
                    get_IsDefaultShadowEnabled: _Callable[[_Pointer[_type.boolean]],
                                                          _type.HRESULT]
                    put_IsDefaultShadowEnabled: _Callable[[_type.boolean],
                                                          _type.HRESULT]

                class IMenuFlyoutPresenterFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IMenuFlyoutPresenter]],
                                              _type.HRESULT]

                class IMenuFlyoutPresenterStatics3(IInspectable):
                    get_IsDefaultShadowEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]

                class IMenuFlyoutSeparator(IInspectable):
                    pass

                class IMenuFlyoutSeparatorFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IMenuFlyoutSeparator]],
                                              _type.HRESULT]

                class IMenuFlyoutStatics(IInspectable):
                    get_MenuFlyoutPresenterStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]

                class IMenuFlyoutSubItem(IInspectable):
                    get_Items: _Callable[[_Pointer[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Controls.IMenuFlyoutItem]]],
                                         _type.HRESULT]
                    get_Text: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]
                    put_Text: _Callable[[_type.HSTRING],
                                        _type.HRESULT]

                class IMenuFlyoutSubItem2(IInspectable):
                    get_Icon: _Callable[[_Pointer[Windows.UI.Xaml.Controls.IIconElement]],
                                        _type.HRESULT]
                    put_Icon: _Callable[[Windows.UI.Xaml.Controls.IIconElement],
                                        _type.HRESULT]

                class IMenuFlyoutSubItemStatics(IInspectable):
                    get_TextProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]

                class IMenuFlyoutSubItemStatics2(IInspectable):
                    get_IconProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]

                class INavigate(IInspectable):
                    Navigate: _Callable

                class INavigationView(IInspectable):
                    get_IsPaneOpen: _Callable
                    put_IsPaneOpen: _Callable
                    get_CompactModeThresholdWidth: _Callable
                    put_CompactModeThresholdWidth: _Callable
                    get_ExpandedModeThresholdWidth: _Callable
                    put_ExpandedModeThresholdWidth: _Callable
                    get_PaneFooter: _Callable
                    put_PaneFooter: _Callable
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_DisplayMode: _Callable
                    get_IsSettingsVisible: _Callable
                    put_IsSettingsVisible: _Callable
                    get_IsPaneToggleButtonVisible: _Callable
                    put_IsPaneToggleButtonVisible: _Callable
                    get_AlwaysShowHeader: _Callable
                    put_AlwaysShowHeader: _Callable
                    get_CompactPaneLength: _Callable
                    put_CompactPaneLength: _Callable
                    get_OpenPaneLength: _Callable
                    put_OpenPaneLength: _Callable
                    get_PaneToggleButtonStyle: _Callable
                    put_PaneToggleButtonStyle: _Callable
                    get_SelectedItem: _Callable
                    put_SelectedItem: _Callable
                    get_MenuItems: _Callable
                    get_MenuItemsSource: _Callable
                    put_MenuItemsSource: _Callable
                    get_SettingsItem: _Callable
                    get_AutoSuggestBox: _Callable
                    put_AutoSuggestBox: _Callable
                    get_MenuItemTemplate: _Callable
                    put_MenuItemTemplate: _Callable
                    get_MenuItemTemplateSelector: _Callable
                    put_MenuItemTemplateSelector: _Callable
                    get_MenuItemContainerStyle: _Callable
                    put_MenuItemContainerStyle: _Callable
                    get_MenuItemContainerStyleSelector: _Callable
                    put_MenuItemContainerStyleSelector: _Callable
                    MenuItemFromContainer: _Callable
                    ContainerFromMenuItem: _Callable
                    add_SelectionChanged: _Callable
                    remove_SelectionChanged: _Callable
                    add_ItemInvoked: _Callable
                    remove_ItemInvoked: _Callable
                    add_DisplayModeChanged: _Callable
                    remove_DisplayModeChanged: _Callable

                class INavigationView2(IInspectable):
                    get_IsBackButtonVisible: _Callable
                    put_IsBackButtonVisible: _Callable
                    get_IsBackEnabled: _Callable
                    put_IsBackEnabled: _Callable
                    get_PaneTitle: _Callable
                    put_PaneTitle: _Callable
                    add_BackRequested: _Callable
                    remove_BackRequested: _Callable
                    add_PaneClosed: _Callable
                    remove_PaneClosed: _Callable
                    add_PaneClosing: _Callable
                    remove_PaneClosing: _Callable
                    add_PaneOpened: _Callable
                    remove_PaneOpened: _Callable
                    add_PaneOpening: _Callable
                    remove_PaneOpening: _Callable

                class INavigationView3(IInspectable):
                    get_PaneDisplayMode: _Callable
                    put_PaneDisplayMode: _Callable
                    get_PaneHeader: _Callable
                    put_PaneHeader: _Callable
                    get_PaneCustomContent: _Callable
                    put_PaneCustomContent: _Callable
                    get_ContentOverlay: _Callable
                    put_ContentOverlay: _Callable
                    get_IsPaneVisible: _Callable
                    put_IsPaneVisible: _Callable
                    get_SelectionFollowsFocus: _Callable
                    put_SelectionFollowsFocus: _Callable
                    get_TemplateSettings: _Callable
                    get_ShoulderNavigationEnabled: _Callable
                    put_ShoulderNavigationEnabled: _Callable
                    get_OverflowLabelMode: _Callable
                    put_OverflowLabelMode: _Callable

                class INavigationViewBackRequestedEventArgs(IInspectable):
                    pass

                class INavigationViewDisplayModeChangedEventArgs(IInspectable):
                    get_DisplayMode: _Callable

                class INavigationViewFactory(IInspectable):
                    CreateInstance: _Callable

                class INavigationViewItem(IInspectable):
                    get_Icon: _Callable
                    put_Icon: _Callable
                    get_CompactPaneLength: _Callable

                class INavigationViewItem2(IInspectable):
                    get_SelectsOnInvoked: _Callable
                    put_SelectsOnInvoked: _Callable

                class INavigationViewItemBase(IInspectable):
                    pass

                class INavigationViewItemBaseFactory(IInspectable):
                    pass

                class INavigationViewItemFactory(IInspectable):
                    CreateInstance: _Callable

                class INavigationViewItemHeader(IInspectable):
                    pass

                class INavigationViewItemHeaderFactory(IInspectable):
                    CreateInstance: _Callable

                class INavigationViewItemInvokedEventArgs(IInspectable):
                    get_InvokedItem: _Callable
                    get_IsSettingsInvoked: _Callable

                class INavigationViewItemInvokedEventArgs2(IInspectable):
                    get_InvokedItemContainer: _Callable
                    get_RecommendedNavigationTransitionInfo: _Callable

                class INavigationViewItemSeparator(IInspectable):
                    pass

                class INavigationViewItemSeparatorFactory(IInspectable):
                    CreateInstance: _Callable

                class INavigationViewItemStatics(IInspectable):
                    get_IconProperty: _Callable
                    get_CompactPaneLengthProperty: _Callable

                class INavigationViewItemStatics2(IInspectable):
                    get_SelectsOnInvokedProperty: _Callable

                class INavigationViewList(IInspectable):
                    pass

                class INavigationViewListFactory(IInspectable):
                    CreateInstance: _Callable

                class INavigationViewPaneClosingEventArgs(IInspectable):
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class INavigationViewSelectionChangedEventArgs(IInspectable):
                    get_SelectedItem: _Callable
                    get_IsSettingsSelected: _Callable

                class INavigationViewSelectionChangedEventArgs2(IInspectable):
                    get_SelectedItemContainer: _Callable
                    get_RecommendedNavigationTransitionInfo: _Callable

                class INavigationViewStatics(IInspectable):
                    get_IsPaneOpenProperty: _Callable
                    get_CompactModeThresholdWidthProperty: _Callable
                    get_ExpandedModeThresholdWidthProperty: _Callable
                    get_PaneFooterProperty: _Callable
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_DisplayModeProperty: _Callable
                    get_IsSettingsVisibleProperty: _Callable
                    get_IsPaneToggleButtonVisibleProperty: _Callable
                    get_AlwaysShowHeaderProperty: _Callable
                    get_CompactPaneLengthProperty: _Callable
                    get_OpenPaneLengthProperty: _Callable
                    get_PaneToggleButtonStyleProperty: _Callable
                    get_MenuItemsProperty: _Callable
                    get_MenuItemsSourceProperty: _Callable
                    get_SelectedItemProperty: _Callable
                    get_SettingsItemProperty: _Callable
                    get_AutoSuggestBoxProperty: _Callable
                    get_MenuItemTemplateProperty: _Callable
                    get_MenuItemTemplateSelectorProperty: _Callable
                    get_MenuItemContainerStyleProperty: _Callable
                    get_MenuItemContainerStyleSelectorProperty: _Callable

                class INavigationViewStatics2(IInspectable):
                    get_IsBackButtonVisibleProperty: _Callable
                    get_IsBackEnabledProperty: _Callable
                    get_PaneTitleProperty: _Callable

                class INavigationViewStatics3(IInspectable):
                    get_PaneDisplayModeProperty: _Callable
                    get_PaneHeaderProperty: _Callable
                    get_PaneCustomContentProperty: _Callable
                    get_ContentOverlayProperty: _Callable
                    get_IsPaneVisibleProperty: _Callable
                    get_SelectionFollowsFocusProperty: _Callable
                    get_TemplateSettingsProperty: _Callable
                    get_ShoulderNavigationEnabledProperty: _Callable
                    get_OverflowLabelModeProperty: _Callable

                class INavigationViewTemplateSettings(IInspectable):
                    get_TopPadding: _Callable
                    get_OverflowButtonVisibility: _Callable
                    get_PaneToggleButtonVisibility: _Callable
                    get_BackButtonVisibility: _Callable
                    get_TopPaneVisibility: _Callable
                    get_LeftPaneVisibility: _Callable
                    get_SingleSelectionFollowsFocus: _Callable

                class INavigationViewTemplateSettingsFactory(IInspectable):
                    CreateInstance: _Callable

                class INavigationViewTemplateSettingsStatics(IInspectable):
                    get_TopPaddingProperty: _Callable
                    get_OverflowButtonVisibilityProperty: _Callable
                    get_PaneToggleButtonVisibilityProperty: _Callable
                    get_BackButtonVisibilityProperty: _Callable
                    get_TopPaneVisibilityProperty: _Callable
                    get_LeftPaneVisibilityProperty: _Callable
                    get_SingleSelectionFollowsFocusProperty: _Callable

                class INotifyEventArgs(IInspectable):
                    get_Value: _Callable

                class INotifyEventArgs2(IInspectable):
                    get_CallingUri: _Callable

                class IPage(IInspectable):
                    get_Frame: _Callable
                    get_NavigationCacheMode: _Callable
                    put_NavigationCacheMode: _Callable
                    get_TopAppBar: _Callable
                    put_TopAppBar: _Callable
                    get_BottomAppBar: _Callable
                    put_BottomAppBar: _Callable

                class IPageFactory(IInspectable):
                    CreateInstance: _Callable

                class IPageOverrides(IInspectable):
                    OnNavigatedFrom: _Callable
                    OnNavigatedTo: _Callable
                    OnNavigatingFrom: _Callable

                class IPageStatics(IInspectable):
                    get_FrameProperty: _Callable
                    get_TopAppBarProperty: _Callable
                    get_BottomAppBarProperty: _Callable

                class IPanel(IInspectable):
                    get_Children: _Callable[[_Pointer[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.IUIElement]]],
                                            _type.HRESULT]
                    get_Background: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                              _type.HRESULT]
                    put_Background: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                              _type.HRESULT]
                    get_IsItemsHost: _Callable[[_Pointer[_type.boolean]],
                                               _type.HRESULT]
                    get_ChildrenTransitions: _Callable
                    put_ChildrenTransitions: _Callable

                class IPanel2(IInspectable):
                    get_BackgroundTransition: _Callable
                    put_BackgroundTransition: _Callable

                class IPanelFactory(IInspectable):
                    CreateInstance: _Callable

                class IPanelStatics(IInspectable):
                    get_BackgroundProperty: _Callable
                    get_IsItemsHostProperty: _Callable
                    get_ChildrenTransitionsProperty: _Callable

                class IParallaxView(IInspectable):
                    get_Child: _Callable
                    put_Child: _Callable
                    get_HorizontalShift: _Callable
                    put_HorizontalShift: _Callable
                    get_HorizontalSourceEndOffset: _Callable
                    put_HorizontalSourceEndOffset: _Callable
                    get_HorizontalSourceOffsetKind: _Callable
                    put_HorizontalSourceOffsetKind: _Callable
                    get_HorizontalSourceStartOffset: _Callable
                    put_HorizontalSourceStartOffset: _Callable
                    get_IsHorizontalShiftClamped: _Callable
                    put_IsHorizontalShiftClamped: _Callable
                    get_IsVerticalShiftClamped: _Callable
                    put_IsVerticalShiftClamped: _Callable
                    get_MaxHorizontalShiftRatio: _Callable
                    put_MaxHorizontalShiftRatio: _Callable
                    get_MaxVerticalShiftRatio: _Callable
                    put_MaxVerticalShiftRatio: _Callable
                    get_Source: _Callable
                    put_Source: _Callable
                    get_VerticalShift: _Callable
                    put_VerticalShift: _Callable
                    get_VerticalSourceEndOffset: _Callable
                    put_VerticalSourceEndOffset: _Callable
                    get_VerticalSourceOffsetKind: _Callable
                    put_VerticalSourceOffsetKind: _Callable
                    get_VerticalSourceStartOffset: _Callable
                    put_VerticalSourceStartOffset: _Callable
                    RefreshAutomaticHorizontalOffsets: _Callable
                    RefreshAutomaticVerticalOffsets: _Callable

                class IParallaxViewFactory(IInspectable):
                    CreateInstance: _Callable

                class IParallaxViewStatics(IInspectable):
                    get_ChildProperty: _Callable
                    get_HorizontalSourceEndOffsetProperty: _Callable
                    get_HorizontalSourceOffsetKindProperty: _Callable
                    get_HorizontalSourceStartOffsetProperty: _Callable
                    get_MaxHorizontalShiftRatioProperty: _Callable
                    get_HorizontalShiftProperty: _Callable
                    get_IsHorizontalShiftClampedProperty: _Callable
                    get_IsVerticalShiftClampedProperty: _Callable
                    get_SourceProperty: _Callable
                    get_VerticalSourceEndOffsetProperty: _Callable
                    get_VerticalSourceOffsetKindProperty: _Callable
                    get_VerticalSourceStartOffsetProperty: _Callable
                    get_MaxVerticalShiftRatioProperty: _Callable
                    get_VerticalShiftProperty: _Callable

                class IPasswordBox(IInspectable):
                    get_Password: _Callable
                    put_Password: _Callable
                    get_PasswordChar: _Callable
                    put_PasswordChar: _Callable
                    get_IsPasswordRevealButtonEnabled: _Callable
                    put_IsPasswordRevealButtonEnabled: _Callable
                    get_MaxLength: _Callable
                    put_MaxLength: _Callable
                    add_PasswordChanged: _Callable
                    remove_PasswordChanged: _Callable
                    add_ContextMenuOpening: _Callable
                    remove_ContextMenuOpening: _Callable
                    SelectAll: _Callable

                class IPasswordBox2(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_PlaceholderText: _Callable
                    put_PlaceholderText: _Callable
                    get_SelectionHighlightColor: _Callable
                    put_SelectionHighlightColor: _Callable
                    get_PreventKeyboardDisplayOnProgrammaticFocus: _Callable
                    put_PreventKeyboardDisplayOnProgrammaticFocus: _Callable
                    add_Paste: _Callable
                    remove_Paste: _Callable

                class IPasswordBox3(IInspectable):
                    get_PasswordRevealMode: _Callable
                    put_PasswordRevealMode: _Callable
                    get_TextReadingOrder: _Callable
                    put_TextReadingOrder: _Callable
                    get_InputScope: _Callable
                    put_InputScope: _Callable

                class IPasswordBox4(IInspectable):
                    add_PasswordChanging: _Callable
                    remove_PasswordChanging: _Callable

                class IPasswordBox5(IInspectable):
                    get_CanPasteClipboardContent: _Callable
                    get_SelectionFlyout: _Callable
                    put_SelectionFlyout: _Callable
                    get_Description: _Callable
                    put_Description: _Callable
                    PasteFromClipboard: _Callable

                class IPasswordBoxPasswordChangingEventArgs(IInspectable):
                    get_IsContentChanging: _Callable

                class IPasswordBoxStatics(IInspectable):
                    get_PasswordProperty: _Callable
                    get_PasswordCharProperty: _Callable
                    get_IsPasswordRevealButtonEnabledProperty: _Callable
                    get_MaxLengthProperty: _Callable

                class IPasswordBoxStatics2(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_PlaceholderTextProperty: _Callable
                    get_SelectionHighlightColorProperty: _Callable
                    get_PreventKeyboardDisplayOnProgrammaticFocusProperty: _Callable

                class IPasswordBoxStatics3(IInspectable):
                    get_PasswordRevealModeProperty: _Callable
                    get_TextReadingOrderProperty: _Callable
                    get_InputScopeProperty: _Callable

                class IPasswordBoxStatics5(IInspectable):
                    get_CanPasteClipboardContentProperty: _Callable
                    get_SelectionFlyoutProperty: _Callable
                    get_DescriptionProperty: _Callable

                class IPathIcon(IInspectable):
                    get_Data: _Callable
                    put_Data: _Callable

                class IPathIconFactory(IInspectable):
                    CreateInstance: _Callable

                class IPathIconSource(IInspectable):
                    get_Data: _Callable
                    put_Data: _Callable

                class IPathIconSourceFactory(IInspectable):
                    CreateInstance: _Callable

                class IPathIconSourceStatics(IInspectable):
                    get_DataProperty: _Callable

                class IPathIconStatics(IInspectable):
                    get_DataProperty: _Callable

                class IPersonPicture(IInspectable):
                    get_BadgeNumber: _Callable
                    put_BadgeNumber: _Callable
                    get_BadgeGlyph: _Callable
                    put_BadgeGlyph: _Callable
                    get_BadgeImageSource: _Callable
                    put_BadgeImageSource: _Callable
                    get_BadgeText: _Callable
                    put_BadgeText: _Callable
                    get_IsGroup: _Callable
                    put_IsGroup: _Callable
                    get_Contact: _Callable
                    put_Contact: _Callable
                    get_DisplayName: _Callable
                    put_DisplayName: _Callable
                    get_Initials: _Callable
                    put_Initials: _Callable
                    get_PreferSmallImage: _Callable
                    put_PreferSmallImage: _Callable
                    get_ProfilePicture: _Callable
                    put_ProfilePicture: _Callable

                class IPersonPictureFactory(IInspectable):
                    CreateInstance: _Callable

                class IPersonPictureStatics(IInspectable):
                    get_BadgeNumberProperty: _Callable
                    get_BadgeGlyphProperty: _Callable
                    get_BadgeImageSourceProperty: _Callable
                    get_BadgeTextProperty: _Callable
                    get_IsGroupProperty: _Callable
                    get_ContactProperty: _Callable
                    get_DisplayNameProperty: _Callable
                    get_InitialsProperty: _Callable
                    get_PreferSmallImageProperty: _Callable
                    get_ProfilePictureProperty: _Callable

                class IPickerConfirmedEventArgs(IInspectable):
                    pass

                class IPickerFlyout(IInspectable):
                    get_Content: _Callable
                    put_Content: _Callable
                    get_ConfirmationButtonsVisible: _Callable
                    put_ConfirmationButtonsVisible: _Callable
                    add_Confirmed: _Callable
                    remove_Confirmed: _Callable
                    ShowAtAsync: _Callable

                class IPickerFlyoutPresenter(IInspectable):
                    pass

                class IPickerFlyoutStatics(IInspectable):
                    get_ContentProperty: _Callable
                    get_ConfirmationButtonsVisibleProperty: _Callable

                class IPivot(IInspectable):
                    get_Title: _Callable
                    put_Title: _Callable
                    get_TitleTemplate: _Callable
                    put_TitleTemplate: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_SelectedIndex: _Callable
                    put_SelectedIndex: _Callable
                    get_SelectedItem: _Callable
                    put_SelectedItem: _Callable
                    get_IsLocked: _Callable
                    put_IsLocked: _Callable
                    add_SelectionChanged: _Callable
                    remove_SelectionChanged: _Callable
                    add_PivotItemLoading: _Callable
                    remove_PivotItemLoading: _Callable
                    add_PivotItemLoaded: _Callable
                    remove_PivotItemLoaded: _Callable
                    add_PivotItemUnloading: _Callable
                    remove_PivotItemUnloading: _Callable
                    add_PivotItemUnloaded: _Callable
                    remove_PivotItemUnloaded: _Callable

                class IPivot2(IInspectable):
                    get_LeftHeader: _Callable
                    put_LeftHeader: _Callable
                    get_LeftHeaderTemplate: _Callable
                    put_LeftHeaderTemplate: _Callable
                    get_RightHeader: _Callable
                    put_RightHeader: _Callable
                    get_RightHeaderTemplate: _Callable
                    put_RightHeaderTemplate: _Callable

                class IPivot3(IInspectable):
                    get_HeaderFocusVisualPlacement: _Callable
                    put_HeaderFocusVisualPlacement: _Callable
                    get_IsHeaderItemsCarouselEnabled: _Callable
                    put_IsHeaderItemsCarouselEnabled: _Callable

                class IPivotFactory(IInspectable):
                    CreateInstance: _Callable

                class IPivotItem(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable

                class IPivotItemEventArgs(IInspectable):
                    get_Item: _Callable
                    put_Item: _Callable

                class IPivotItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IPivotItemStatics(IInspectable):
                    get_HeaderProperty: _Callable

                class IPivotStatics(IInspectable):
                    get_TitleProperty: _Callable
                    get_TitleTemplateProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_SelectedIndexProperty: _Callable
                    get_SelectedItemProperty: _Callable
                    get_IsLockedProperty: _Callable
                    get_SlideInAnimationGroupProperty: _Callable
                    GetSlideInAnimationGroup: _Callable
                    SetSlideInAnimationGroup: _Callable

                class IPivotStatics2(IInspectable):
                    get_LeftHeaderProperty: _Callable
                    get_LeftHeaderTemplateProperty: _Callable
                    get_RightHeaderProperty: _Callable
                    get_RightHeaderTemplateProperty: _Callable

                class IPivotStatics3(IInspectable):
                    get_HeaderFocusVisualPlacementProperty: _Callable
                    get_IsHeaderItemsCarouselEnabledProperty: _Callable

                class IProgressBar(IInspectable):
                    get_IsIndeterminate: _Callable
                    put_IsIndeterminate: _Callable
                    get_ShowError: _Callable
                    put_ShowError: _Callable
                    get_ShowPaused: _Callable
                    put_ShowPaused: _Callable
                    get_TemplateSettings: _Callable

                class IProgressBarFactory(IInspectable):
                    CreateInstance: _Callable

                class IProgressBarStatics(IInspectable):
                    get_IsIndeterminateProperty: _Callable
                    get_ShowErrorProperty: _Callable
                    get_ShowPausedProperty: _Callable

                class IProgressRing(IInspectable):
                    get_IsActive: _Callable
                    put_IsActive: _Callable
                    get_TemplateSettings: _Callable

                class IProgressRingStatics(IInspectable):
                    get_IsActiveProperty: _Callable

                class IRadioButton(IInspectable):
                    get_GroupName: _Callable
                    put_GroupName: _Callable

                class IRadioButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IRadioButtonStatics(IInspectable):
                    get_GroupNameProperty: _Callable

                class IRatingControl(IInspectable):
                    get_Caption: _Callable
                    put_Caption: _Callable
                    get_InitialSetValue: _Callable
                    put_InitialSetValue: _Callable
                    get_IsClearEnabled: _Callable
                    put_IsClearEnabled: _Callable
                    get_IsReadOnly: _Callable
                    put_IsReadOnly: _Callable
                    get_MaxRating: _Callable
                    put_MaxRating: _Callable
                    get_PlaceholderValue: _Callable
                    put_PlaceholderValue: _Callable
                    get_ItemInfo: _Callable
                    put_ItemInfo: _Callable
                    get_Value: _Callable
                    put_Value: _Callable
                    add_ValueChanged: _Callable
                    remove_ValueChanged: _Callable

                class IRatingControlFactory(IInspectable):
                    CreateInstance: _Callable

                class IRatingControlStatics(IInspectable):
                    get_CaptionProperty: _Callable
                    get_InitialSetValueProperty: _Callable
                    get_IsClearEnabledProperty: _Callable
                    get_IsReadOnlyProperty: _Callable
                    get_MaxRatingProperty: _Callable
                    get_PlaceholderValueProperty: _Callable
                    get_ItemInfoProperty: _Callable
                    get_ValueProperty: _Callable

                class IRatingItemFontInfo(IInspectable):
                    get_DisabledGlyph: _Callable
                    put_DisabledGlyph: _Callable
                    get_Glyph: _Callable
                    put_Glyph: _Callable
                    get_PointerOverGlyph: _Callable
                    put_PointerOverGlyph: _Callable
                    get_PointerOverPlaceholderGlyph: _Callable
                    put_PointerOverPlaceholderGlyph: _Callable
                    get_PlaceholderGlyph: _Callable
                    put_PlaceholderGlyph: _Callable
                    get_UnsetGlyph: _Callable
                    put_UnsetGlyph: _Callable

                class IRatingItemFontInfoFactory(IInspectable):
                    CreateInstance: _Callable

                class IRatingItemFontInfoStatics(IInspectable):
                    get_DisabledGlyphProperty: _Callable
                    get_GlyphProperty: _Callable
                    get_PlaceholderGlyphProperty: _Callable
                    get_PointerOverGlyphProperty: _Callable
                    get_PointerOverPlaceholderGlyphProperty: _Callable
                    get_UnsetGlyphProperty: _Callable

                class IRatingItemImageInfo(IInspectable):
                    get_DisabledImage: _Callable
                    put_DisabledImage: _Callable
                    get_Image: _Callable
                    put_Image: _Callable
                    get_PlaceholderImage: _Callable
                    put_PlaceholderImage: _Callable
                    get_PointerOverImage: _Callable
                    put_PointerOverImage: _Callable
                    get_PointerOverPlaceholderImage: _Callable
                    put_PointerOverPlaceholderImage: _Callable
                    get_UnsetImage: _Callable
                    put_UnsetImage: _Callable

                class IRatingItemImageInfoFactory(IInspectable):
                    CreateInstance: _Callable

                class IRatingItemImageInfoStatics(IInspectable):
                    get_DisabledImageProperty: _Callable
                    get_ImageProperty: _Callable
                    get_PlaceholderImageProperty: _Callable
                    get_PointerOverImageProperty: _Callable
                    get_PointerOverPlaceholderImageProperty: _Callable
                    get_UnsetImageProperty: _Callable

                class IRatingItemInfo(IInspectable):
                    pass

                class IRatingItemInfoFactory(IInspectable):
                    CreateInstance: _Callable

                class IRefreshContainer(IInspectable):
                    get_Visualizer: _Callable
                    put_Visualizer: _Callable
                    get_PullDirection: _Callable
                    put_PullDirection: _Callable
                    add_RefreshRequested: _Callable
                    remove_RefreshRequested: _Callable
                    RequestRefresh: _Callable

                class IRefreshContainerFactory(IInspectable):
                    CreateInstance: _Callable

                class IRefreshContainerStatics(IInspectable):
                    get_VisualizerProperty: _Callable
                    get_PullDirectionProperty: _Callable

                class IRefreshInteractionRatioChangedEventArgs(IInspectable):
                    get_InteractionRatio: _Callable

                class IRefreshRequestedEventArgs(IInspectable):
                    GetDeferral: _Callable

                class IRefreshStateChangedEventArgs(IInspectable):
                    get_OldState: _Callable
                    get_NewState: _Callable

                class IRefreshVisualizer(IInspectable):
                    RequestRefresh: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    get_Content: _Callable
                    put_Content: _Callable
                    get_State: _Callable
                    add_RefreshRequested: _Callable
                    remove_RefreshRequested: _Callable
                    add_RefreshStateChanged: _Callable
                    remove_RefreshStateChanged: _Callable

                class IRefreshVisualizerFactory(IInspectable):
                    CreateInstance: _Callable

                class IRefreshVisualizerStatics(IInspectable):
                    get_InfoProviderProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_ContentProperty: _Callable
                    get_StateProperty: _Callable

                class IRelativePanel(IInspectable):
                    get_BorderBrush: _Callable
                    put_BorderBrush: _Callable
                    get_BorderThickness: _Callable
                    put_BorderThickness: _Callable
                    get_CornerRadius: _Callable
                    put_CornerRadius: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable

                class IRelativePanel2(IInspectable):
                    get_BackgroundSizing: _Callable
                    put_BackgroundSizing: _Callable

                class IRelativePanelFactory(IInspectable):
                    CreateInstance: _Callable

                class IRelativePanelStatics(IInspectable):
                    get_LeftOfProperty: _Callable
                    GetLeftOf: _Callable
                    SetLeftOf: _Callable
                    get_AboveProperty: _Callable
                    GetAbove: _Callable
                    SetAbove: _Callable
                    get_RightOfProperty: _Callable
                    GetRightOf: _Callable
                    SetRightOf: _Callable
                    get_BelowProperty: _Callable
                    GetBelow: _Callable
                    SetBelow: _Callable
                    get_AlignHorizontalCenterWithProperty: _Callable
                    GetAlignHorizontalCenterWith: _Callable
                    SetAlignHorizontalCenterWith: _Callable
                    get_AlignVerticalCenterWithProperty: _Callable
                    GetAlignVerticalCenterWith: _Callable
                    SetAlignVerticalCenterWith: _Callable
                    get_AlignLeftWithProperty: _Callable
                    GetAlignLeftWith: _Callable
                    SetAlignLeftWith: _Callable
                    get_AlignTopWithProperty: _Callable
                    GetAlignTopWith: _Callable
                    SetAlignTopWith: _Callable
                    get_AlignRightWithProperty: _Callable
                    GetAlignRightWith: _Callable
                    SetAlignRightWith: _Callable
                    get_AlignBottomWithProperty: _Callable
                    GetAlignBottomWith: _Callable
                    SetAlignBottomWith: _Callable
                    get_AlignLeftWithPanelProperty: _Callable
                    GetAlignLeftWithPanel: _Callable
                    SetAlignLeftWithPanel: _Callable
                    get_AlignTopWithPanelProperty: _Callable
                    GetAlignTopWithPanel: _Callable
                    SetAlignTopWithPanel: _Callable
                    get_AlignRightWithPanelProperty: _Callable
                    GetAlignRightWithPanel: _Callable
                    SetAlignRightWithPanel: _Callable
                    get_AlignBottomWithPanelProperty: _Callable
                    GetAlignBottomWithPanel: _Callable
                    SetAlignBottomWithPanel: _Callable
                    get_AlignHorizontalCenterWithPanelProperty: _Callable
                    GetAlignHorizontalCenterWithPanel: _Callable
                    SetAlignHorizontalCenterWithPanel: _Callable
                    get_AlignVerticalCenterWithPanelProperty: _Callable
                    GetAlignVerticalCenterWithPanel: _Callable
                    SetAlignVerticalCenterWithPanel: _Callable
                    get_BorderBrushProperty: _Callable
                    get_BorderThicknessProperty: _Callable
                    get_CornerRadiusProperty: _Callable
                    get_PaddingProperty: _Callable

                class IRelativePanelStatics2(IInspectable):
                    get_BackgroundSizingProperty: _Callable

                class IRichEditBox(IInspectable):
                    get_IsReadOnly: _Callable
                    put_IsReadOnly: _Callable
                    get_AcceptsReturn: _Callable
                    put_AcceptsReturn: _Callable
                    get_TextAlignment: _Callable
                    put_TextAlignment: _Callable
                    get_TextWrapping: _Callable
                    put_TextWrapping: _Callable
                    get_IsSpellCheckEnabled: _Callable
                    put_IsSpellCheckEnabled: _Callable
                    get_IsTextPredictionEnabled: _Callable
                    put_IsTextPredictionEnabled: _Callable
                    get_Document: _Callable
                    get_InputScope: _Callable
                    put_InputScope: _Callable
                    add_TextChanged: _Callable
                    remove_TextChanged: _Callable
                    add_SelectionChanged: _Callable
                    remove_SelectionChanged: _Callable
                    add_ContextMenuOpening: _Callable
                    remove_ContextMenuOpening: _Callable

                class IRichEditBox2(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_PlaceholderText: _Callable
                    put_PlaceholderText: _Callable
                    get_SelectionHighlightColor: _Callable
                    put_SelectionHighlightColor: _Callable
                    get_PreventKeyboardDisplayOnProgrammaticFocus: _Callable
                    put_PreventKeyboardDisplayOnProgrammaticFocus: _Callable
                    get_IsColorFontEnabled: _Callable
                    put_IsColorFontEnabled: _Callable
                    add_Paste: _Callable
                    remove_Paste: _Callable

                class IRichEditBox3(IInspectable):
                    add_TextCompositionStarted: _Callable
                    remove_TextCompositionStarted: _Callable
                    add_TextCompositionChanged: _Callable
                    remove_TextCompositionChanged: _Callable
                    add_TextCompositionEnded: _Callable
                    remove_TextCompositionEnded: _Callable
                    get_TextReadingOrder: _Callable
                    put_TextReadingOrder: _Callable
                    get_DesiredCandidateWindowAlignment: _Callable
                    put_DesiredCandidateWindowAlignment: _Callable
                    add_CandidateWindowBoundsChanged: _Callable
                    remove_CandidateWindowBoundsChanged: _Callable
                    add_TextChanging: _Callable
                    remove_TextChanging: _Callable

                class IRichEditBox4(IInspectable):
                    GetLinguisticAlternativesAsync: _Callable
                    get_ClipboardCopyFormat: _Callable
                    put_ClipboardCopyFormat: _Callable

                class IRichEditBox5(IInspectable):
                    get_SelectionHighlightColorWhenNotFocused: _Callable
                    put_SelectionHighlightColorWhenNotFocused: _Callable
                    get_MaxLength: _Callable
                    put_MaxLength: _Callable

                class IRichEditBox6(IInspectable):
                    get_HorizontalTextAlignment: _Callable
                    put_HorizontalTextAlignment: _Callable
                    get_CharacterCasing: _Callable
                    put_CharacterCasing: _Callable
                    get_DisabledFormattingAccelerators: _Callable
                    put_DisabledFormattingAccelerators: _Callable
                    add_CopyingToClipboard: _Callable
                    remove_CopyingToClipboard: _Callable
                    add_CuttingToClipboard: _Callable
                    remove_CuttingToClipboard: _Callable

                class IRichEditBox7(IInspectable):
                    get_ContentLinkForegroundColor: _Callable
                    put_ContentLinkForegroundColor: _Callable
                    get_ContentLinkBackgroundColor: _Callable
                    put_ContentLinkBackgroundColor: _Callable
                    get_ContentLinkProviders: _Callable
                    put_ContentLinkProviders: _Callable
                    get_HandwritingView: _Callable
                    put_HandwritingView: _Callable
                    get_IsHandwritingViewEnabled: _Callable
                    put_IsHandwritingViewEnabled: _Callable
                    add_ContentLinkChanged: _Callable
                    remove_ContentLinkChanged: _Callable
                    add_ContentLinkInvoked: _Callable
                    remove_ContentLinkInvoked: _Callable

                class IRichEditBox8(IInspectable):
                    get_TextDocument: _Callable
                    get_SelectionFlyout: _Callable
                    put_SelectionFlyout: _Callable
                    get_ProofingMenuFlyout: _Callable
                    get_Description: _Callable
                    put_Description: _Callable
                    add_SelectionChanging: _Callable
                    remove_SelectionChanging: _Callable

                class IRichEditBoxFactory(IInspectable):
                    CreateInstance: _Callable

                class IRichEditBoxSelectionChangingEventArgs(IInspectable):
                    get_SelectionStart: _Callable
                    get_SelectionLength: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class IRichEditBoxStatics(IInspectable):
                    get_IsReadOnlyProperty: _Callable
                    get_AcceptsReturnProperty: _Callable
                    get_TextAlignmentProperty: _Callable
                    get_TextWrappingProperty: _Callable
                    get_IsSpellCheckEnabledProperty: _Callable
                    get_IsTextPredictionEnabledProperty: _Callable
                    get_InputScopeProperty: _Callable

                class IRichEditBoxStatics2(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_PlaceholderTextProperty: _Callable
                    get_SelectionHighlightColorProperty: _Callable
                    get_PreventKeyboardDisplayOnProgrammaticFocusProperty: _Callable
                    get_IsColorFontEnabledProperty: _Callable

                class IRichEditBoxStatics3(IInspectable):
                    get_DesiredCandidateWindowAlignmentProperty: _Callable
                    get_TextReadingOrderProperty: _Callable

                class IRichEditBoxStatics4(IInspectable):
                    get_ClipboardCopyFormatProperty: _Callable

                class IRichEditBoxStatics5(IInspectable):
                    get_SelectionHighlightColorWhenNotFocusedProperty: _Callable
                    get_MaxLengthProperty: _Callable

                class IRichEditBoxStatics6(IInspectable):
                    get_HorizontalTextAlignmentProperty: _Callable
                    get_CharacterCasingProperty: _Callable
                    get_DisabledFormattingAcceleratorsProperty: _Callable

                class IRichEditBoxStatics7(IInspectable):
                    get_ContentLinkForegroundColorProperty: _Callable
                    get_ContentLinkBackgroundColorProperty: _Callable
                    get_ContentLinkProvidersProperty: _Callable
                    get_HandwritingViewProperty: _Callable
                    get_IsHandwritingViewEnabledProperty: _Callable

                class IRichEditBoxStatics8(IInspectable):
                    get_SelectionFlyoutProperty: _Callable
                    get_ProofingMenuFlyoutProperty: _Callable
                    get_DescriptionProperty: _Callable

                class IRichEditBoxTextChangingEventArgs(IInspectable):
                    pass

                class IRichEditBoxTextChangingEventArgs2(IInspectable):
                    get_IsContentChanging: _Callable

                class IRichTextBlock(IInspectable):
                    get_FontSize: _Callable
                    put_FontSize: _Callable
                    get_FontFamily: _Callable
                    put_FontFamily: _Callable
                    get_FontWeight: _Callable
                    put_FontWeight: _Callable
                    get_FontStyle: _Callable
                    put_FontStyle: _Callable
                    get_FontStretch: _Callable
                    put_FontStretch: _Callable
                    get_Foreground: _Callable
                    put_Foreground: _Callable
                    get_TextWrapping: _Callable
                    put_TextWrapping: _Callable
                    get_TextTrimming: _Callable
                    put_TextTrimming: _Callable
                    get_TextAlignment: _Callable
                    put_TextAlignment: _Callable
                    get_Blocks: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable
                    get_LineHeight: _Callable
                    put_LineHeight: _Callable
                    get_LineStackingStrategy: _Callable
                    put_LineStackingStrategy: _Callable
                    get_CharacterSpacing: _Callable
                    put_CharacterSpacing: _Callable
                    get_OverflowContentTarget: _Callable
                    put_OverflowContentTarget: _Callable
                    get_IsTextSelectionEnabled: _Callable
                    put_IsTextSelectionEnabled: _Callable
                    get_HasOverflowContent: _Callable
                    get_SelectedText: _Callable
                    get_ContentStart: _Callable
                    get_ContentEnd: _Callable
                    get_SelectionStart: _Callable
                    get_SelectionEnd: _Callable
                    get_BaselineOffset: _Callable
                    add_SelectionChanged: _Callable
                    remove_SelectionChanged: _Callable
                    add_ContextMenuOpening: _Callable
                    remove_ContextMenuOpening: _Callable
                    SelectAll: _Callable
                    Select: _Callable
                    GetPositionFromPoint: _Callable
                    Focus: _Callable
                    get_TextIndent: _Callable
                    put_TextIndent: _Callable

                class IRichTextBlock2(IInspectable):
                    get_MaxLines: _Callable
                    put_MaxLines: _Callable
                    get_TextLineBounds: _Callable
                    put_TextLineBounds: _Callable
                    get_SelectionHighlightColor: _Callable
                    put_SelectionHighlightColor: _Callable
                    get_OpticalMarginAlignment: _Callable
                    put_OpticalMarginAlignment: _Callable
                    get_IsColorFontEnabled: _Callable
                    put_IsColorFontEnabled: _Callable
                    get_TextReadingOrder: _Callable
                    put_TextReadingOrder: _Callable

                class IRichTextBlock3(IInspectable):
                    get_IsTextScaleFactorEnabled: _Callable
                    put_IsTextScaleFactorEnabled: _Callable

                class IRichTextBlock4(IInspectable):
                    get_TextDecorations: _Callable
                    put_TextDecorations: _Callable

                class IRichTextBlock5(IInspectable):
                    get_IsTextTrimmed: _Callable
                    get_HorizontalTextAlignment: _Callable
                    put_HorizontalTextAlignment: _Callable
                    get_TextHighlighters: _Callable
                    add_IsTextTrimmedChanged: _Callable
                    remove_IsTextTrimmedChanged: _Callable

                class IRichTextBlock6(IInspectable):
                    get_SelectionFlyout: _Callable
                    put_SelectionFlyout: _Callable
                    CopySelectionToClipboard: _Callable

                class IRichTextBlockOverflow(IInspectable):
                    get_OverflowContentTarget: _Callable
                    put_OverflowContentTarget: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable
                    get_ContentSource: _Callable
                    get_HasOverflowContent: _Callable
                    get_ContentStart: _Callable
                    get_ContentEnd: _Callable
                    get_BaselineOffset: _Callable
                    GetPositionFromPoint: _Callable
                    Focus: _Callable

                class IRichTextBlockOverflow2(IInspectable):
                    get_MaxLines: _Callable
                    put_MaxLines: _Callable

                class IRichTextBlockOverflow3(IInspectable):
                    get_IsTextTrimmed: _Callable
                    add_IsTextTrimmedChanged: _Callable
                    remove_IsTextTrimmedChanged: _Callable

                class IRichTextBlockOverflowStatics(IInspectable):
                    get_OverflowContentTargetProperty: _Callable
                    get_PaddingProperty: _Callable
                    get_HasOverflowContentProperty: _Callable

                class IRichTextBlockOverflowStatics2(IInspectable):
                    get_MaxLinesProperty: _Callable

                class IRichTextBlockOverflowStatics3(IInspectable):
                    get_IsTextTrimmedProperty: _Callable

                class IRichTextBlockStatics(IInspectable):
                    get_FontSizeProperty: _Callable
                    get_FontFamilyProperty: _Callable
                    get_FontWeightProperty: _Callable
                    get_FontStyleProperty: _Callable
                    get_FontStretchProperty: _Callable
                    get_ForegroundProperty: _Callable
                    get_TextWrappingProperty: _Callable
                    get_TextTrimmingProperty: _Callable
                    get_TextAlignmentProperty: _Callable
                    get_PaddingProperty: _Callable
                    get_LineHeightProperty: _Callable
                    get_LineStackingStrategyProperty: _Callable
                    get_CharacterSpacingProperty: _Callable
                    get_OverflowContentTargetProperty: _Callable
                    get_IsTextSelectionEnabledProperty: _Callable
                    get_HasOverflowContentProperty: _Callable
                    get_SelectedTextProperty: _Callable
                    get_TextIndentProperty: _Callable

                class IRichTextBlockStatics2(IInspectable):
                    get_MaxLinesProperty: _Callable
                    get_TextLineBoundsProperty: _Callable
                    get_SelectionHighlightColorProperty: _Callable
                    get_OpticalMarginAlignmentProperty: _Callable
                    get_IsColorFontEnabledProperty: _Callable
                    get_TextReadingOrderProperty: _Callable

                class IRichTextBlockStatics3(IInspectable):
                    get_IsTextScaleFactorEnabledProperty: _Callable

                class IRichTextBlockStatics4(IInspectable):
                    get_TextDecorationsProperty: _Callable

                class IRichTextBlockStatics5(IInspectable):
                    get_IsTextTrimmedProperty: _Callable
                    get_HorizontalTextAlignmentProperty: _Callable

                class IRichTextBlockStatics6(IInspectable):
                    get_SelectionFlyoutProperty: _Callable

                class IRowDefinition(IInspectable):
                    get_Height: _Callable
                    put_Height: _Callable
                    get_MaxHeight: _Callable
                    put_MaxHeight: _Callable
                    get_MinHeight: _Callable
                    put_MinHeight: _Callable
                    get_ActualHeight: _Callable

                class IRowDefinitionStatics(IInspectable):
                    get_HeightProperty: _Callable
                    get_MaxHeightProperty: _Callable
                    get_MinHeightProperty: _Callable

                class IScrollAnchorProvider(IInspectable):
                    get_CurrentAnchor: _Callable
                    RegisterAnchorCandidate: _Callable
                    UnregisterAnchorCandidate: _Callable

                class IScrollContentPresenter(IInspectable):
                    get_CanVerticallyScroll: _Callable
                    put_CanVerticallyScroll: _Callable
                    get_CanHorizontallyScroll: _Callable
                    put_CanHorizontallyScroll: _Callable
                    get_ExtentWidth: _Callable
                    get_ExtentHeight: _Callable
                    get_ViewportWidth: _Callable
                    get_ViewportHeight: _Callable
                    get_HorizontalOffset: _Callable
                    get_VerticalOffset: _Callable
                    get_ScrollOwner: _Callable
                    put_ScrollOwner: _Callable
                    LineUp: _Callable
                    LineDown: _Callable
                    LineLeft: _Callable
                    LineRight: _Callable
                    PageUp: _Callable
                    PageDown: _Callable
                    PageLeft: _Callable
                    PageRight: _Callable
                    MouseWheelUp: _Callable
                    MouseWheelDown: _Callable
                    MouseWheelLeft: _Callable
                    MouseWheelRight: _Callable
                    SetHorizontalOffset: _Callable
                    SetVerticalOffset: _Callable
                    MakeVisible: _Callable

                class IScrollContentPresenter2(IInspectable):
                    get_CanContentRenderOutsideBounds: _Callable
                    put_CanContentRenderOutsideBounds: _Callable
                    get_SizesContentToTemplatedParent: _Callable
                    put_SizesContentToTemplatedParent: _Callable

                class IScrollContentPresenterStatics2(IInspectable):
                    get_CanContentRenderOutsideBoundsProperty: _Callable
                    get_SizesContentToTemplatedParentProperty: _Callable

                class IScrollViewer(IInspectable):
                    get_HorizontalScrollBarVisibility: _Callable
                    put_HorizontalScrollBarVisibility: _Callable
                    get_VerticalScrollBarVisibility: _Callable
                    put_VerticalScrollBarVisibility: _Callable
                    get_IsHorizontalRailEnabled: _Callable
                    put_IsHorizontalRailEnabled: _Callable
                    get_IsVerticalRailEnabled: _Callable
                    put_IsVerticalRailEnabled: _Callable
                    get_IsHorizontalScrollChainingEnabled: _Callable
                    put_IsHorizontalScrollChainingEnabled: _Callable
                    get_IsVerticalScrollChainingEnabled: _Callable
                    put_IsVerticalScrollChainingEnabled: _Callable
                    get_IsZoomChainingEnabled: _Callable
                    put_IsZoomChainingEnabled: _Callable
                    get_IsScrollInertiaEnabled: _Callable
                    put_IsScrollInertiaEnabled: _Callable
                    get_IsZoomInertiaEnabled: _Callable
                    put_IsZoomInertiaEnabled: _Callable
                    get_HorizontalScrollMode: _Callable
                    put_HorizontalScrollMode: _Callable
                    get_VerticalScrollMode: _Callable
                    put_VerticalScrollMode: _Callable
                    get_ZoomMode: _Callable
                    put_ZoomMode: _Callable
                    get_HorizontalSnapPointsAlignment: _Callable
                    put_HorizontalSnapPointsAlignment: _Callable
                    get_VerticalSnapPointsAlignment: _Callable
                    put_VerticalSnapPointsAlignment: _Callable
                    get_HorizontalSnapPointsType: _Callable
                    put_HorizontalSnapPointsType: _Callable
                    get_VerticalSnapPointsType: _Callable
                    put_VerticalSnapPointsType: _Callable
                    get_ZoomSnapPointsType: _Callable
                    put_ZoomSnapPointsType: _Callable
                    get_HorizontalOffset: _Callable
                    get_ViewportWidth: _Callable
                    get_ScrollableWidth: _Callable
                    get_ComputedHorizontalScrollBarVisibility: _Callable
                    get_ExtentWidth: _Callable
                    get_VerticalOffset: _Callable
                    get_ViewportHeight: _Callable
                    get_ScrollableHeight: _Callable
                    get_ComputedVerticalScrollBarVisibility: _Callable
                    get_ExtentHeight: _Callable
                    get_MinZoomFactor: _Callable
                    put_MinZoomFactor: _Callable
                    get_MaxZoomFactor: _Callable
                    put_MaxZoomFactor: _Callable
                    get_ZoomFactor: _Callable
                    get_ZoomSnapPoints: _Callable
                    add_ViewChanged: _Callable
                    remove_ViewChanged: _Callable
                    ScrollToHorizontalOffset: _Callable
                    ScrollToVerticalOffset: _Callable
                    ZoomToFactor: _Callable
                    InvalidateScrollInfo: _Callable
                    get_IsDeferredScrollingEnabled: _Callable
                    put_IsDeferredScrollingEnabled: _Callable
                    get_BringIntoViewOnFocusChange: _Callable
                    put_BringIntoViewOnFocusChange: _Callable

                class IScrollViewer2(IInspectable):
                    get_TopLeftHeader: _Callable
                    put_TopLeftHeader: _Callable
                    get_LeftHeader: _Callable
                    put_LeftHeader: _Callable
                    get_TopHeader: _Callable
                    put_TopHeader: _Callable
                    add_ViewChanging: _Callable
                    remove_ViewChanging: _Callable
                    ChangeView: _Callable
                    ChangeViewWithOptionalAnimation: _Callable

                class IScrollViewer3(IInspectable):
                    add_DirectManipulationStarted: _Callable
                    remove_DirectManipulationStarted: _Callable
                    add_DirectManipulationCompleted: _Callable
                    remove_DirectManipulationCompleted: _Callable

                class IScrollViewer4(IInspectable):
                    get_ReduceViewportForCoreInputViewOcclusions: _Callable
                    put_ReduceViewportForCoreInputViewOcclusions: _Callable
                    get_HorizontalAnchorRatio: _Callable
                    put_HorizontalAnchorRatio: _Callable
                    get_VerticalAnchorRatio: _Callable
                    put_VerticalAnchorRatio: _Callable
                    get_CanContentRenderOutsideBounds: _Callable
                    put_CanContentRenderOutsideBounds: _Callable
                    add_AnchorRequested: _Callable
                    remove_AnchorRequested: _Callable

                class IScrollViewerStatics(IInspectable):
                    get_HorizontalSnapPointsAlignmentProperty: _Callable
                    get_VerticalSnapPointsAlignmentProperty: _Callable
                    get_HorizontalSnapPointsTypeProperty: _Callable
                    get_VerticalSnapPointsTypeProperty: _Callable
                    get_ZoomSnapPointsTypeProperty: _Callable
                    get_HorizontalOffsetProperty: _Callable
                    get_ViewportWidthProperty: _Callable
                    get_ScrollableWidthProperty: _Callable
                    get_ComputedHorizontalScrollBarVisibilityProperty: _Callable
                    get_ExtentWidthProperty: _Callable
                    get_VerticalOffsetProperty: _Callable
                    get_ViewportHeightProperty: _Callable
                    get_ScrollableHeightProperty: _Callable
                    get_ComputedVerticalScrollBarVisibilityProperty: _Callable
                    get_ExtentHeightProperty: _Callable
                    get_MinZoomFactorProperty: _Callable
                    get_MaxZoomFactorProperty: _Callable
                    get_ZoomFactorProperty: _Callable
                    get_ZoomSnapPointsProperty: _Callable
                    get_HorizontalScrollBarVisibilityProperty: _Callable
                    GetHorizontalScrollBarVisibility: _Callable
                    SetHorizontalScrollBarVisibility: _Callable
                    get_VerticalScrollBarVisibilityProperty: _Callable
                    GetVerticalScrollBarVisibility: _Callable
                    SetVerticalScrollBarVisibility: _Callable
                    get_IsHorizontalRailEnabledProperty: _Callable
                    GetIsHorizontalRailEnabled: _Callable
                    SetIsHorizontalRailEnabled: _Callable
                    get_IsVerticalRailEnabledProperty: _Callable
                    GetIsVerticalRailEnabled: _Callable
                    SetIsVerticalRailEnabled: _Callable
                    get_IsHorizontalScrollChainingEnabledProperty: _Callable
                    GetIsHorizontalScrollChainingEnabled: _Callable
                    SetIsHorizontalScrollChainingEnabled: _Callable
                    get_IsVerticalScrollChainingEnabledProperty: _Callable
                    GetIsVerticalScrollChainingEnabled: _Callable
                    SetIsVerticalScrollChainingEnabled: _Callable
                    get_IsZoomChainingEnabledProperty: _Callable
                    GetIsZoomChainingEnabled: _Callable
                    SetIsZoomChainingEnabled: _Callable
                    get_IsScrollInertiaEnabledProperty: _Callable
                    GetIsScrollInertiaEnabled: _Callable
                    SetIsScrollInertiaEnabled: _Callable
                    get_IsZoomInertiaEnabledProperty: _Callable
                    GetIsZoomInertiaEnabled: _Callable
                    SetIsZoomInertiaEnabled: _Callable
                    get_HorizontalScrollModeProperty: _Callable
                    GetHorizontalScrollMode: _Callable
                    SetHorizontalScrollMode: _Callable
                    get_VerticalScrollModeProperty: _Callable
                    GetVerticalScrollMode: _Callable
                    SetVerticalScrollMode: _Callable
                    get_ZoomModeProperty: _Callable
                    GetZoomMode: _Callable
                    SetZoomMode: _Callable
                    get_IsDeferredScrollingEnabledProperty: _Callable
                    GetIsDeferredScrollingEnabled: _Callable
                    SetIsDeferredScrollingEnabled: _Callable
                    get_BringIntoViewOnFocusChangeProperty: _Callable
                    GetBringIntoViewOnFocusChange: _Callable
                    SetBringIntoViewOnFocusChange: _Callable

                class IScrollViewerStatics2(IInspectable):
                    get_TopLeftHeaderProperty: _Callable
                    get_LeftHeaderProperty: _Callable
                    get_TopHeaderProperty: _Callable

                class IScrollViewerStatics4(IInspectable):
                    get_ReduceViewportForCoreInputViewOcclusionsProperty: _Callable
                    get_HorizontalAnchorRatioProperty: _Callable
                    get_VerticalAnchorRatioProperty: _Callable
                    get_CanContentRenderOutsideBoundsProperty: _Callable
                    GetCanContentRenderOutsideBounds: _Callable
                    SetCanContentRenderOutsideBounds: _Callable

                class IScrollViewerView(IInspectable):
                    get_HorizontalOffset: _Callable
                    get_VerticalOffset: _Callable
                    get_ZoomFactor: _Callable

                class IScrollViewerViewChangedEventArgs(IInspectable):
                    get_IsIntermediate: _Callable

                class IScrollViewerViewChangingEventArgs(IInspectable):
                    get_NextView: _Callable
                    get_FinalView: _Callable
                    get_IsInertial: _Callable

                class ISearchBox(IInspectable):
                    get_SearchHistoryEnabled: _Callable
                    put_SearchHistoryEnabled: _Callable
                    get_SearchHistoryContext: _Callable
                    put_SearchHistoryContext: _Callable
                    get_PlaceholderText: _Callable
                    put_PlaceholderText: _Callable
                    get_QueryText: _Callable
                    put_QueryText: _Callable
                    get_FocusOnKeyboardInput: _Callable
                    put_FocusOnKeyboardInput: _Callable
                    get_ChooseSuggestionOnEnter: _Callable
                    put_ChooseSuggestionOnEnter: _Callable
                    add_QueryChanged: _Callable
                    remove_QueryChanged: _Callable
                    add_SuggestionsRequested: _Callable
                    remove_SuggestionsRequested: _Callable
                    add_QuerySubmitted: _Callable
                    remove_QuerySubmitted: _Callable
                    add_ResultSuggestionChosen: _Callable
                    remove_ResultSuggestionChosen: _Callable
                    add_PrepareForFocusOnKeyboardInput: _Callable
                    remove_PrepareForFocusOnKeyboardInput: _Callable
                    SetLocalContentSuggestionSettings: _Callable

                class ISearchBoxFactory(IInspectable):
                    CreateInstance: _Callable

                class ISearchBoxQueryChangedEventArgs(IInspectable):
                    get_QueryText: _Callable
                    get_Language: _Callable
                    get_LinguisticDetails: _Callable

                class ISearchBoxQuerySubmittedEventArgs(IInspectable):
                    get_QueryText: _Callable
                    get_Language: _Callable
                    get_LinguisticDetails: _Callable
                    get_KeyModifiers: _Callable

                class ISearchBoxResultSuggestionChosenEventArgs(IInspectable):
                    get_Tag: _Callable
                    get_KeyModifiers: _Callable

                class ISearchBoxStatics(IInspectable):
                    get_SearchHistoryEnabledProperty: _Callable
                    get_SearchHistoryContextProperty: _Callable
                    get_PlaceholderTextProperty: _Callable
                    get_QueryTextProperty: _Callable
                    get_FocusOnKeyboardInputProperty: _Callable
                    get_ChooseSuggestionOnEnterProperty: _Callable

                class ISearchBoxSuggestionsRequestedEventArgs(IInspectable):
                    get_QueryText: _Callable
                    get_Language: _Callable
                    get_LinguisticDetails: _Callable
                    get_Request: _Callable

                class ISectionsInViewChangedEventArgs(IInspectable):
                    get_AddedSections: _Callable
                    get_RemovedSections: _Callable

                class ISectionsInViewChangedEventArgsFactory(IInspectable):
                    pass

                class ISelectionChangedEventArgs(IInspectable):
                    get_AddedItems: _Callable
                    get_RemovedItems: _Callable

                class ISelectionChangedEventArgsFactory(IInspectable):
                    CreateInstanceWithRemovedItemsAndAddedItems: _Callable

                class ISemanticZoom(IInspectable):
                    get_ZoomedInView: _Callable
                    put_ZoomedInView: _Callable
                    get_ZoomedOutView: _Callable
                    put_ZoomedOutView: _Callable
                    get_IsZoomedInViewActive: _Callable
                    put_IsZoomedInViewActive: _Callable
                    get_CanChangeViews: _Callable
                    put_CanChangeViews: _Callable
                    add_ViewChangeStarted: _Callable
                    remove_ViewChangeStarted: _Callable
                    add_ViewChangeCompleted: _Callable
                    remove_ViewChangeCompleted: _Callable
                    ToggleActiveView: _Callable
                    get_IsZoomOutButtonEnabled: _Callable
                    put_IsZoomOutButtonEnabled: _Callable

                class ISemanticZoomInformation(IInspectable):
                    get_SemanticZoomOwner: _Callable
                    put_SemanticZoomOwner: _Callable
                    get_IsActiveView: _Callable
                    put_IsActiveView: _Callable
                    get_IsZoomedInView: _Callable
                    put_IsZoomedInView: _Callable
                    InitializeViewChange: _Callable
                    CompleteViewChange: _Callable
                    MakeVisible: _Callable
                    StartViewChangeFrom: _Callable
                    StartViewChangeTo: _Callable
                    CompleteViewChangeFrom: _Callable
                    CompleteViewChangeTo: _Callable

                class ISemanticZoomLocation(IInspectable):
                    get_Item: _Callable
                    put_Item: _Callable
                    get_Bounds: _Callable
                    put_Bounds: _Callable

                class ISemanticZoomStatics(IInspectable):
                    get_ZoomedInViewProperty: _Callable
                    get_ZoomedOutViewProperty: _Callable
                    get_IsZoomedInViewActiveProperty: _Callable
                    get_CanChangeViewsProperty: _Callable
                    get_IsZoomOutButtonEnabledProperty: _Callable

                class ISemanticZoomViewChangedEventArgs(IInspectable):
                    get_IsSourceZoomedInView: _Callable
                    put_IsSourceZoomedInView: _Callable
                    get_SourceItem: _Callable
                    put_SourceItem: _Callable
                    get_DestinationItem: _Callable
                    put_DestinationItem: _Callable

                class ISettingsFlyout(IInspectable):
                    get_Title: _Callable
                    put_Title: _Callable
                    get_HeaderBackground: _Callable
                    put_HeaderBackground: _Callable
                    get_HeaderForeground: _Callable
                    put_HeaderForeground: _Callable
                    get_IconSource: _Callable
                    put_IconSource: _Callable
                    get_TemplateSettings: _Callable
                    add_BackClick: _Callable
                    remove_BackClick: _Callable
                    Show: _Callable
                    ShowIndependent: _Callable
                    Hide: _Callable

                class ISettingsFlyoutFactory(IInspectable):
                    CreateInstance: _Callable

                class ISettingsFlyoutStatics(IInspectable):
                    get_TitleProperty: _Callable
                    get_HeaderBackgroundProperty: _Callable
                    get_HeaderForegroundProperty: _Callable
                    get_IconSourceProperty: _Callable

                class ISlider(IInspectable):
                    get_IntermediateValue: _Callable
                    put_IntermediateValue: _Callable
                    get_StepFrequency: _Callable
                    put_StepFrequency: _Callable
                    get_SnapsTo: _Callable
                    put_SnapsTo: _Callable
                    get_TickFrequency: _Callable
                    put_TickFrequency: _Callable
                    get_TickPlacement: _Callable
                    put_TickPlacement: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    get_IsDirectionReversed: _Callable
                    put_IsDirectionReversed: _Callable
                    get_IsThumbToolTipEnabled: _Callable
                    put_IsThumbToolTipEnabled: _Callable
                    get_ThumbToolTipValueConverter: _Callable
                    put_ThumbToolTipValueConverter: _Callable

                class ISlider2(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable

                class ISliderFactory(IInspectable):
                    CreateInstance: _Callable

                class ISliderStatics(IInspectable):
                    get_IntermediateValueProperty: _Callable
                    get_StepFrequencyProperty: _Callable
                    get_SnapsToProperty: _Callable
                    get_TickFrequencyProperty: _Callable
                    get_TickPlacementProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_IsDirectionReversedProperty: _Callable
                    get_IsThumbToolTipEnabledProperty: _Callable
                    get_ThumbToolTipValueConverterProperty: _Callable

                class ISliderStatics2(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable

                class ISplitButton(IInspectable):
                    get_Flyout: _Callable
                    put_Flyout: _Callable
                    get_Command: _Callable
                    put_Command: _Callable
                    get_CommandParameter: _Callable
                    put_CommandParameter: _Callable
                    add_Click: _Callable
                    remove_Click: _Callable

                class ISplitButtonAutomationPeer(IInspectable):
                    pass

                class ISplitButtonAutomationPeerFactory(IInspectable):
                    CreateInstance: _Callable

                class ISplitButtonClickEventArgs(IInspectable):
                    pass

                class ISplitButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class ISplitButtonStatics(IInspectable):
                    get_FlyoutProperty: _Callable
                    get_CommandProperty: _Callable
                    get_CommandParameterProperty: _Callable

                class ISplitView(IInspectable):
                    get_Content: _Callable
                    put_Content: _Callable
                    get_Pane: _Callable
                    put_Pane: _Callable
                    get_IsPaneOpen: _Callable
                    put_IsPaneOpen: _Callable
                    get_OpenPaneLength: _Callable
                    put_OpenPaneLength: _Callable
                    get_CompactPaneLength: _Callable
                    put_CompactPaneLength: _Callable
                    get_PanePlacement: _Callable
                    put_PanePlacement: _Callable
                    get_DisplayMode: _Callable
                    put_DisplayMode: _Callable
                    get_TemplateSettings: _Callable
                    get_PaneBackground: _Callable
                    put_PaneBackground: _Callable
                    add_PaneClosing: _Callable
                    remove_PaneClosing: _Callable
                    add_PaneClosed: _Callable
                    remove_PaneClosed: _Callable

                class ISplitView2(IInspectable):
                    get_LightDismissOverlayMode: _Callable
                    put_LightDismissOverlayMode: _Callable

                class ISplitView3(IInspectable):
                    add_PaneOpening: _Callable
                    remove_PaneOpening: _Callable
                    add_PaneOpened: _Callable
                    remove_PaneOpened: _Callable

                class ISplitViewFactory(IInspectable):
                    CreateInstance: _Callable

                class ISplitViewPaneClosingEventArgs(IInspectable):
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class ISplitViewStatics(IInspectable):
                    get_ContentProperty: _Callable
                    get_PaneProperty: _Callable
                    get_IsPaneOpenProperty: _Callable
                    get_OpenPaneLengthProperty: _Callable
                    get_CompactPaneLengthProperty: _Callable
                    get_PanePlacementProperty: _Callable
                    get_DisplayModeProperty: _Callable
                    get_TemplateSettingsProperty: _Callable
                    get_PaneBackgroundProperty: _Callable

                class ISplitViewStatics2(IInspectable):
                    get_LightDismissOverlayModeProperty: _Callable

                class IStackPanel(IInspectable):
                    get_AreScrollSnapPointsRegular: _Callable[[_Pointer[_type.boolean]],
                                                              _type.HRESULT]
                    put_AreScrollSnapPointsRegular: _Callable[[_type.boolean],
                                                              _type.HRESULT]
                    get_Orientation: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Orientation]],
                                               _type.HRESULT]
                    put_Orientation: _Callable[[_enum.Windows.UI.Xaml.Controls.Orientation],
                                               _type.HRESULT]

                class IStackPanel2(IInspectable):
                    get_BorderBrush: _Callable
                    put_BorderBrush: _Callable
                    get_BorderThickness: _Callable
                    put_BorderThickness: _Callable
                    get_CornerRadius: _Callable
                    put_CornerRadius: _Callable
                    get_Padding: _Callable
                    put_Padding: _Callable

                class IStackPanel4(IInspectable):
                    get_Spacing: _Callable
                    put_Spacing: _Callable

                class IStackPanel5(IInspectable):
                    get_BackgroundSizing: _Callable
                    put_BackgroundSizing: _Callable

                class IStackPanelFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IStackPanel]],
                                              _type.HRESULT]

                class IStackPanelStatics(IInspectable):
                    get_AreScrollSnapPointsRegularProperty: _Callable
                    get_OrientationProperty: _Callable

                class IStackPanelStatics2(IInspectable):
                    get_BorderBrushProperty: _Callable
                    get_BorderThicknessProperty: _Callable
                    get_CornerRadiusProperty: _Callable
                    get_PaddingProperty: _Callable

                class IStackPanelStatics4(IInspectable):
                    get_SpacingProperty: _Callable

                class IStackPanelStatics5(IInspectable):
                    get_BackgroundSizingProperty: _Callable

                class IStyleSelector(IInspectable):
                    SelectStyle: _Callable

                class IStyleSelectorFactory(IInspectable):
                    CreateInstance: _Callable

                class IStyleSelectorOverrides(IInspectable):
                    SelectStyleCore: _Callable

                class ISwapChainBackgroundPanel(IInspectable):
                    pass

                class ISwapChainBackgroundPanel2(IInspectable):
                    CreateCoreIndependentInputSource: _Callable

                class ISwapChainBackgroundPanelFactory(IInspectable):
                    CreateInstance: _Callable

                class ISwapChainPanel(IInspectable):
                    get_CompositionScaleX: _Callable
                    get_CompositionScaleY: _Callable
                    add_CompositionScaleChanged: _Callable
                    remove_CompositionScaleChanged: _Callable
                    CreateCoreIndependentInputSource: _Callable

                class ISwapChainPanelFactory(IInspectable):
                    CreateInstance: _Callable

                class ISwapChainPanelStatics(IInspectable):
                    get_CompositionScaleXProperty: _Callable
                    get_CompositionScaleYProperty: _Callable

                class ISwipeControl(IInspectable):
                    get_LeftItems: _Callable
                    put_LeftItems: _Callable
                    get_RightItems: _Callable
                    put_RightItems: _Callable
                    get_TopItems: _Callable
                    put_TopItems: _Callable
                    get_BottomItems: _Callable
                    put_BottomItems: _Callable
                    Close: _Callable

                class ISwipeControlFactory(IInspectable):
                    CreateInstance: _Callable

                class ISwipeControlStatics(IInspectable):
                    get_LeftItemsProperty: _Callable
                    get_RightItemsProperty: _Callable
                    get_TopItemsProperty: _Callable
                    get_BottomItemsProperty: _Callable

                class ISwipeItem(IInspectable):
                    get_Text: _Callable
                    put_Text: _Callable
                    get_IconSource: _Callable
                    put_IconSource: _Callable
                    get_Background: _Callable
                    put_Background: _Callable
                    get_Foreground: _Callable
                    put_Foreground: _Callable
                    get_Command: _Callable
                    put_Command: _Callable
                    get_CommandParameter: _Callable
                    put_CommandParameter: _Callable
                    get_BehaviorOnInvoked: _Callable
                    put_BehaviorOnInvoked: _Callable
                    add_Invoked: _Callable
                    remove_Invoked: _Callable

                class ISwipeItemFactory(IInspectable):
                    CreateInstance: _Callable

                class ISwipeItemInvokedEventArgs(IInspectable):
                    get_SwipeControl: _Callable

                class ISwipeItemStatics(IInspectable):
                    get_IconSourceProperty: _Callable
                    get_TextProperty: _Callable
                    get_BackgroundProperty: _Callable
                    get_ForegroundProperty: _Callable
                    get_CommandProperty: _Callable
                    get_CommandParameterProperty: _Callable
                    get_BehaviorOnInvokedProperty: _Callable

                class ISwipeItems(IInspectable):
                    get_Mode: _Callable
                    put_Mode: _Callable

                class ISwipeItemsFactory(IInspectable):
                    CreateInstance: _Callable

                class ISwipeItemsStatics(IInspectable):
                    get_ModeProperty: _Callable

                class ISymbolIcon(IInspectable):
                    get_Symbol: _Callable
                    put_Symbol: _Callable

                class ISymbolIconFactory(IInspectable):
                    CreateInstanceWithSymbol: _Callable

                class ISymbolIconSource(IInspectable):
                    get_Symbol: _Callable
                    put_Symbol: _Callable

                class ISymbolIconSourceFactory(IInspectable):
                    CreateInstance: _Callable

                class ISymbolIconSourceStatics(IInspectable):
                    get_SymbolProperty: _Callable

                class ISymbolIconStatics(IInspectable):
                    get_SymbolProperty: _Callable

                class ITextBlock(IInspectable):
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
                    get_TextWrapping: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TextWrapping]],
                                                _type.HRESULT]
                    put_TextWrapping: _Callable[[_enum.Windows.UI.Xaml.Controls.TextWrapping],
                                                _type.HRESULT]
                    get_TextTrimming: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TextTrimming]],
                                                _type.HRESULT]
                    put_TextTrimming: _Callable[[_enum.Windows.UI.Xaml.Controls.TextTrimming],
                                                _type.HRESULT]
                    get_TextAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.TextAlignment]],
                                                 _type.HRESULT]
                    put_TextAlignment: _Callable[[_enum.Windows.UI.Xaml.Controls.TextAlignment],
                                                 _type.HRESULT]
                    get_Text: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]
                    put_Text: _Callable[[_type.HSTRING],
                                        _type.HRESULT]
                    get_Inlines: _Callable
                    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],
                                           _type.HRESULT]
                    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],
                                           _type.HRESULT]
                    get_LineHeight: _Callable[[_Pointer[_type.DOUBLE]],
                                              _type.HRESULT]
                    put_LineHeight: _Callable[[_type.DOUBLE],
                                              _type.HRESULT]
                    get_LineStackingStrategy: _Callable[[_Pointer[_enum.Windows.UI.Xaml.LineStackingStrategy]],
                                                        _type.HRESULT]
                    put_LineStackingStrategy: _Callable[[_enum.Windows.UI.Xaml.LineStackingStrategy],
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
                    Focus: _Callable[[_enum.Windows.UI.Xaml.FocusState,
                                      _Pointer[_type.boolean]],
                                     _type.HRESULT]

                class ITextBlock2(IInspectable):
                    get_SelectionHighlightColor: _Callable
                    put_SelectionHighlightColor: _Callable
                    get_MaxLines: _Callable
                    put_MaxLines: _Callable
                    get_TextLineBounds: _Callable
                    put_TextLineBounds: _Callable
                    get_OpticalMarginAlignment: _Callable
                    put_OpticalMarginAlignment: _Callable
                    get_IsColorFontEnabled: _Callable
                    put_IsColorFontEnabled: _Callable
                    get_TextReadingOrder: _Callable
                    put_TextReadingOrder: _Callable

                class ITextBlock3(IInspectable):
                    get_IsTextScaleFactorEnabled: _Callable
                    put_IsTextScaleFactorEnabled: _Callable

                class ITextBlock4(IInspectable):
                    GetAlphaMask: _Callable

                class ITextBlock5(IInspectable):
                    get_TextDecorations: _Callable
                    put_TextDecorations: _Callable

                class ITextBlock6(IInspectable):
                    get_IsTextTrimmed: _Callable
                    get_HorizontalTextAlignment: _Callable
                    put_HorizontalTextAlignment: _Callable
                    get_TextHighlighters: _Callable
                    add_IsTextTrimmedChanged: _Callable
                    remove_IsTextTrimmedChanged: _Callable

                class ITextBlock7(IInspectable):
                    get_SelectionFlyout: _Callable
                    put_SelectionFlyout: _Callable
                    CopySelectionToClipboard: _Callable

                class ITextBlockStatics(IInspectable):
                    get_FontSizeProperty: _Callable
                    get_FontFamilyProperty: _Callable
                    get_FontWeightProperty: _Callable
                    get_FontStyleProperty: _Callable
                    get_FontStretchProperty: _Callable
                    get_CharacterSpacingProperty: _Callable
                    get_ForegroundProperty: _Callable
                    get_TextWrappingProperty: _Callable
                    get_TextTrimmingProperty: _Callable
                    get_TextAlignmentProperty: _Callable
                    get_TextProperty: _Callable
                    get_PaddingProperty: _Callable
                    get_LineHeightProperty: _Callable
                    get_LineStackingStrategyProperty: _Callable
                    get_IsTextSelectionEnabledProperty: _Callable
                    get_SelectedTextProperty: _Callable

                class ITextBlockStatics2(IInspectable):
                    get_SelectionHighlightColorProperty: _Callable
                    get_MaxLinesProperty: _Callable
                    get_TextLineBoundsProperty: _Callable
                    get_OpticalMarginAlignmentProperty: _Callable
                    get_IsColorFontEnabledProperty: _Callable
                    get_TextReadingOrderProperty: _Callable

                class ITextBlockStatics3(IInspectable):
                    get_IsTextScaleFactorEnabledProperty: _Callable

                class ITextBlockStatics5(IInspectable):
                    get_TextDecorationsProperty: _Callable

                class ITextBlockStatics6(IInspectable):
                    get_IsTextTrimmedProperty: _Callable
                    get_HorizontalTextAlignmentProperty: _Callable

                class ITextBlockStatics7(IInspectable):
                    get_SelectionFlyoutProperty: _Callable

                class ITextBox(IInspectable):
                    get_Text: _Callable
                    put_Text: _Callable
                    get_SelectedText: _Callable
                    put_SelectedText: _Callable
                    get_SelectionLength: _Callable
                    put_SelectionLength: _Callable
                    get_SelectionStart: _Callable
                    put_SelectionStart: _Callable
                    get_MaxLength: _Callable
                    put_MaxLength: _Callable
                    get_IsReadOnly: _Callable
                    put_IsReadOnly: _Callable
                    get_AcceptsReturn: _Callable
                    put_AcceptsReturn: _Callable
                    get_TextAlignment: _Callable
                    put_TextAlignment: _Callable
                    get_TextWrapping: _Callable
                    put_TextWrapping: _Callable
                    get_IsSpellCheckEnabled: _Callable
                    put_IsSpellCheckEnabled: _Callable
                    get_IsTextPredictionEnabled: _Callable
                    put_IsTextPredictionEnabled: _Callable
                    get_InputScope: _Callable
                    put_InputScope: _Callable
                    add_TextChanged: _Callable
                    remove_TextChanged: _Callable
                    add_SelectionChanged: _Callable
                    remove_SelectionChanged: _Callable
                    add_ContextMenuOpening: _Callable
                    remove_ContextMenuOpening: _Callable
                    Select: _Callable
                    SelectAll: _Callable
                    GetRectFromCharacterIndex: _Callable

                class ITextBox2(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_PlaceholderText: _Callable
                    put_PlaceholderText: _Callable
                    get_SelectionHighlightColor: _Callable
                    put_SelectionHighlightColor: _Callable
                    get_PreventKeyboardDisplayOnProgrammaticFocus: _Callable
                    put_PreventKeyboardDisplayOnProgrammaticFocus: _Callable
                    get_IsColorFontEnabled: _Callable
                    put_IsColorFontEnabled: _Callable
                    add_Paste: _Callable
                    remove_Paste: _Callable

                class ITextBox3(IInspectable):
                    add_TextCompositionStarted: _Callable
                    remove_TextCompositionStarted: _Callable
                    add_TextCompositionChanged: _Callable
                    remove_TextCompositionChanged: _Callable
                    add_TextCompositionEnded: _Callable
                    remove_TextCompositionEnded: _Callable
                    get_TextReadingOrder: _Callable
                    put_TextReadingOrder: _Callable
                    get_DesiredCandidateWindowAlignment: _Callable
                    put_DesiredCandidateWindowAlignment: _Callable
                    add_CandidateWindowBoundsChanged: _Callable
                    remove_CandidateWindowBoundsChanged: _Callable
                    add_TextChanging: _Callable
                    remove_TextChanging: _Callable

                class ITextBox4(IInspectable):
                    GetLinguisticAlternativesAsync: _Callable

                class ITextBox5(IInspectable):
                    get_SelectionHighlightColorWhenNotFocused: _Callable
                    put_SelectionHighlightColorWhenNotFocused: _Callable

                class ITextBox6(IInspectable):
                    get_HorizontalTextAlignment: _Callable
                    put_HorizontalTextAlignment: _Callable
                    get_CharacterCasing: _Callable
                    put_CharacterCasing: _Callable
                    get_PlaceholderForeground: _Callable
                    put_PlaceholderForeground: _Callable
                    add_CopyingToClipboard: _Callable
                    remove_CopyingToClipboard: _Callable
                    add_CuttingToClipboard: _Callable
                    remove_CuttingToClipboard: _Callable
                    add_BeforeTextChanging: _Callable
                    remove_BeforeTextChanging: _Callable

                class ITextBox7(IInspectable):
                    get_HandwritingView: _Callable
                    put_HandwritingView: _Callable
                    get_IsHandwritingViewEnabled: _Callable
                    put_IsHandwritingViewEnabled: _Callable

                class ITextBox8(IInspectable):
                    get_CanPasteClipboardContent: _Callable
                    get_CanUndo: _Callable
                    get_CanRedo: _Callable
                    get_SelectionFlyout: _Callable
                    put_SelectionFlyout: _Callable
                    get_ProofingMenuFlyout: _Callable
                    get_Description: _Callable
                    put_Description: _Callable
                    add_SelectionChanging: _Callable
                    remove_SelectionChanging: _Callable
                    Undo: _Callable
                    Redo: _Callable
                    PasteFromClipboard: _Callable
                    CopySelectionToClipboard: _Callable
                    CutSelectionToClipboard: _Callable
                    ClearUndoRedoHistory: _Callable

                class ITextBoxBeforeTextChangingEventArgs(IInspectable):
                    get_NewText: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class ITextBoxFactory(IInspectable):
                    CreateInstance: _Callable

                class ITextBoxSelectionChangingEventArgs(IInspectable):
                    get_SelectionStart: _Callable
                    get_SelectionLength: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class ITextBoxStatics(IInspectable):
                    get_TextProperty: _Callable
                    get_MaxLengthProperty: _Callable
                    get_IsReadOnlyProperty: _Callable
                    get_AcceptsReturnProperty: _Callable
                    get_TextAlignmentProperty: _Callable
                    get_TextWrappingProperty: _Callable
                    get_IsSpellCheckEnabledProperty: _Callable
                    get_IsTextPredictionEnabledProperty: _Callable
                    get_InputScopeProperty: _Callable

                class ITextBoxStatics2(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_PlaceholderTextProperty: _Callable
                    get_SelectionHighlightColorProperty: _Callable
                    get_PreventKeyboardDisplayOnProgrammaticFocusProperty: _Callable
                    get_IsColorFontEnabledProperty: _Callable

                class ITextBoxStatics3(IInspectable):
                    get_DesiredCandidateWindowAlignmentProperty: _Callable
                    get_TextReadingOrderProperty: _Callable

                class ITextBoxStatics5(IInspectable):
                    get_SelectionHighlightColorWhenNotFocusedProperty: _Callable

                class ITextBoxStatics6(IInspectable):
                    get_HorizontalTextAlignmentProperty: _Callable
                    get_CharacterCasingProperty: _Callable
                    get_PlaceholderForegroundProperty: _Callable

                class ITextBoxStatics7(IInspectable):
                    get_HandwritingViewProperty: _Callable
                    get_IsHandwritingViewEnabledProperty: _Callable

                class ITextBoxStatics8(IInspectable):
                    get_CanPasteClipboardContentProperty: _Callable
                    get_CanUndoProperty: _Callable
                    get_CanRedoProperty: _Callable
                    get_SelectionFlyoutProperty: _Callable
                    get_ProofingMenuFlyoutProperty: _Callable
                    get_DescriptionProperty: _Callable

                class ITextBoxTextChangingEventArgs(IInspectable):
                    pass

                class ITextBoxTextChangingEventArgs2(IInspectable):
                    get_IsContentChanging: _Callable

                class ITextChangedEventArgs(IInspectable):
                    pass

                class ITextCommandBarFlyout(IInspectable):
                    pass

                class ITextCommandBarFlyoutFactory(IInspectable):
                    CreateInstance: _Callable

                class ITextCompositionChangedEventArgs(IInspectable):
                    get_StartIndex: _Callable
                    get_Length: _Callable

                class ITextCompositionEndedEventArgs(IInspectable):
                    get_StartIndex: _Callable
                    get_Length: _Callable

                class ITextCompositionStartedEventArgs(IInspectable):
                    get_StartIndex: _Callable
                    get_Length: _Callable

                class ITextControlCopyingToClipboardEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable

                class ITextControlCuttingToClipboardEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable

                class ITextControlPasteEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable

                class ITimePickedEventArgs(IInspectable):
                    get_OldTime: _Callable
                    get_NewTime: _Callable

                class ITimePicker(IInspectable):
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_ClockIdentifier: _Callable
                    put_ClockIdentifier: _Callable
                    get_MinuteIncrement: _Callable
                    put_MinuteIncrement: _Callable
                    get_Time: _Callable
                    put_Time: _Callable
                    add_TimeChanged: _Callable
                    remove_TimeChanged: _Callable

                class ITimePicker2(IInspectable):
                    get_LightDismissOverlayMode: _Callable
                    put_LightDismissOverlayMode: _Callable

                class ITimePicker3(IInspectable):
                    get_SelectedTime: _Callable
                    put_SelectedTime: _Callable
                    add_SelectedTimeChanged: _Callable
                    remove_SelectedTimeChanged: _Callable

                class ITimePickerFactory(IInspectable):
                    CreateInstance: _Callable

                class ITimePickerFlyout(IInspectable):
                    get_ClockIdentifier: _Callable
                    put_ClockIdentifier: _Callable
                    get_Time: _Callable
                    put_Time: _Callable
                    get_MinuteIncrement: _Callable
                    put_MinuteIncrement: _Callable
                    add_TimePicked: _Callable
                    remove_TimePicked: _Callable
                    ShowAtAsync: _Callable

                class ITimePickerFlyoutPresenter(IInspectable):
                    pass

                class ITimePickerFlyoutPresenter2(IInspectable):
                    get_IsDefaultShadowEnabled: _Callable
                    put_IsDefaultShadowEnabled: _Callable

                class ITimePickerFlyoutPresenterStatics2(IInspectable):
                    get_IsDefaultShadowEnabledProperty: _Callable

                class ITimePickerFlyoutStatics(IInspectable):
                    get_ClockIdentifierProperty: _Callable
                    get_TimeProperty: _Callable
                    get_MinuteIncrementProperty: _Callable

                class ITimePickerSelectedValueChangedEventArgs(IInspectable):
                    get_OldTime: _Callable
                    get_NewTime: _Callable

                class ITimePickerStatics(IInspectable):
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_ClockIdentifierProperty: _Callable
                    get_MinuteIncrementProperty: _Callable
                    get_TimeProperty: _Callable

                class ITimePickerStatics2(IInspectable):
                    get_LightDismissOverlayModeProperty: _Callable

                class ITimePickerStatics3(IInspectable):
                    get_SelectedTimeProperty: _Callable

                class ITimePickerValueChangedEventArgs(IInspectable):
                    get_OldTime: _Callable
                    get_NewTime: _Callable

                class IToggleMenuFlyoutItem(IInspectable):
                    get_IsChecked: _Callable
                    put_IsChecked: _Callable

                class IToggleMenuFlyoutItemFactory(IInspectable):
                    CreateInstance: _Callable

                class IToggleMenuFlyoutItemStatics(IInspectable):
                    get_IsCheckedProperty: _Callable

                class IToggleSplitButton(IInspectable):
                    get_IsChecked: _Callable
                    put_IsChecked: _Callable
                    add_IsCheckedChanged: _Callable
                    remove_IsCheckedChanged: _Callable

                class IToggleSplitButtonAutomationPeer(IInspectable):
                    pass

                class IToggleSplitButtonAutomationPeerFactory(IInspectable):
                    CreateInstance: _Callable

                class IToggleSplitButtonFactory(IInspectable):
                    CreateInstance: _Callable

                class IToggleSplitButtonIsCheckedChangedEventArgs(IInspectable):
                    pass

                class IToggleSwitch(IInspectable):
                    get_IsOn: _Callable
                    put_IsOn: _Callable
                    get_Header: _Callable
                    put_Header: _Callable
                    get_HeaderTemplate: _Callable
                    put_HeaderTemplate: _Callable
                    get_OnContent: _Callable
                    put_OnContent: _Callable
                    get_OnContentTemplate: _Callable
                    put_OnContentTemplate: _Callable
                    get_OffContent: _Callable
                    put_OffContent: _Callable
                    get_OffContentTemplate: _Callable
                    put_OffContentTemplate: _Callable
                    get_TemplateSettings: _Callable
                    add_Toggled: _Callable
                    remove_Toggled: _Callable

                class IToggleSwitchOverrides(IInspectable):
                    OnToggled: _Callable
                    OnOnContentChanged: _Callable
                    OnOffContentChanged: _Callable
                    OnHeaderChanged: _Callable

                class IToggleSwitchStatics(IInspectable):
                    get_IsOnProperty: _Callable
                    get_HeaderProperty: _Callable
                    get_HeaderTemplateProperty: _Callable
                    get_OnContentProperty: _Callable
                    get_OnContentTemplateProperty: _Callable
                    get_OffContentProperty: _Callable
                    get_OffContentTemplateProperty: _Callable

                class IToolTip(IInspectable):
                    get_HorizontalOffset: _Callable
                    put_HorizontalOffset: _Callable
                    get_IsOpen: _Callable
                    put_IsOpen: _Callable
                    get_Placement: _Callable
                    put_Placement: _Callable
                    get_PlacementTarget: _Callable
                    put_PlacementTarget: _Callable
                    get_VerticalOffset: _Callable
                    put_VerticalOffset: _Callable
                    get_TemplateSettings: _Callable
                    add_Closed: _Callable
                    remove_Closed: _Callable
                    add_Opened: _Callable
                    remove_Opened: _Callable

                class IToolTip2(IInspectable):
                    get_PlacementRect: _Callable
                    put_PlacementRect: _Callable

                class IToolTipFactory(IInspectable):
                    CreateInstance: _Callable

                class IToolTipService(IInspectable):
                    pass

                class IToolTipServiceStatics(IInspectable):
                    get_PlacementProperty: _Callable
                    GetPlacement: _Callable
                    SetPlacement: _Callable
                    get_PlacementTargetProperty: _Callable
                    GetPlacementTarget: _Callable
                    SetPlacementTarget: _Callable
                    get_ToolTipProperty: _Callable
                    GetToolTip: _Callable
                    SetToolTip: _Callable

                class IToolTipStatics(IInspectable):
                    get_HorizontalOffsetProperty: _Callable
                    get_IsOpenProperty: _Callable
                    get_PlacementProperty: _Callable
                    get_PlacementTargetProperty: _Callable
                    get_VerticalOffsetProperty: _Callable

                class IToolTipStatics2(IInspectable):
                    get_PlacementRectProperty: _Callable

                class ITreeView(IInspectable):
                    get_RootNodes: _Callable
                    get_SelectionMode: _Callable
                    put_SelectionMode: _Callable
                    get_SelectedNodes: _Callable
                    Expand: _Callable
                    Collapse: _Callable
                    SelectAll: _Callable
                    add_ItemInvoked: _Callable
                    remove_ItemInvoked: _Callable
                    add_Expanding: _Callable
                    remove_Expanding: _Callable
                    add_Collapsed: _Callable
                    remove_Collapsed: _Callable

                class ITreeView2(IInspectable):
                    NodeFromContainer: _Callable
                    ContainerFromNode: _Callable
                    ItemFromContainer: _Callable
                    ContainerFromItem: _Callable
                    get_CanDragItems: _Callable
                    put_CanDragItems: _Callable
                    get_CanReorderItems: _Callable
                    put_CanReorderItems: _Callable
                    get_ItemTemplate: _Callable
                    put_ItemTemplate: _Callable
                    get_ItemTemplateSelector: _Callable
                    put_ItemTemplateSelector: _Callable
                    get_ItemContainerStyle: _Callable
                    put_ItemContainerStyle: _Callable
                    get_ItemContainerStyleSelector: _Callable
                    put_ItemContainerStyleSelector: _Callable
                    get_ItemContainerTransitions: _Callable
                    put_ItemContainerTransitions: _Callable
                    get_ItemsSource: _Callable
                    put_ItemsSource: _Callable
                    add_DragItemsStarting: _Callable
                    remove_DragItemsStarting: _Callable
                    add_DragItemsCompleted: _Callable
                    remove_DragItemsCompleted: _Callable

                class ITreeViewCollapsedEventArgs(IInspectable):
                    get_Node: _Callable

                class ITreeViewCollapsedEventArgs2(IInspectable):
                    get_Item: _Callable

                class ITreeViewDragItemsCompletedEventArgs(IInspectable):
                    get_DropResult: _Callable
                    get_Items: _Callable

                class ITreeViewDragItemsStartingEventArgs(IInspectable):
                    get_Cancel: _Callable
                    put_Cancel: _Callable
                    get_Data: _Callable
                    get_Items: _Callable

                class ITreeViewExpandingEventArgs(IInspectable):
                    get_Node: _Callable

                class ITreeViewExpandingEventArgs2(IInspectable):
                    get_Item: _Callable

                class ITreeViewFactory(IInspectable):
                    CreateInstance: _Callable

                class ITreeViewItem(IInspectable):
                    get_GlyphOpacity: _Callable
                    put_GlyphOpacity: _Callable
                    get_GlyphBrush: _Callable
                    put_GlyphBrush: _Callable
                    get_ExpandedGlyph: _Callable
                    put_ExpandedGlyph: _Callable
                    get_CollapsedGlyph: _Callable
                    put_CollapsedGlyph: _Callable
                    get_GlyphSize: _Callable
                    put_GlyphSize: _Callable
                    get_IsExpanded: _Callable
                    put_IsExpanded: _Callable
                    get_TreeViewItemTemplateSettings: _Callable

                class ITreeViewItem2(IInspectable):
                    get_HasUnrealizedChildren: _Callable
                    put_HasUnrealizedChildren: _Callable
                    get_ItemsSource: _Callable
                    put_ItemsSource: _Callable

                class ITreeViewItemFactory(IInspectable):
                    CreateInstance: _Callable

                class ITreeViewItemInvokedEventArgs(IInspectable):
                    get_InvokedItem: _Callable
                    put_Handled: _Callable
                    get_Handled: _Callable

                class ITreeViewItemStatics(IInspectable):
                    get_GlyphOpacityProperty: _Callable
                    get_GlyphBrushProperty: _Callable
                    get_ExpandedGlyphProperty: _Callable
                    get_CollapsedGlyphProperty: _Callable
                    get_GlyphSizeProperty: _Callable
                    get_IsExpandedProperty: _Callable
                    get_TreeViewItemTemplateSettingsProperty: _Callable

                class ITreeViewItemStatics2(IInspectable):
                    get_HasUnrealizedChildrenProperty: _Callable
                    get_ItemsSourceProperty: _Callable

                class ITreeViewItemTemplateSettings(IInspectable):
                    get_ExpandedGlyphVisibility: _Callable
                    get_CollapsedGlyphVisibility: _Callable
                    get_Indentation: _Callable
                    get_DragItemsCount: _Callable

                class ITreeViewItemTemplateSettingsFactory(IInspectable):
                    CreateInstance: _Callable

                class ITreeViewItemTemplateSettingsStatics(IInspectable):
                    get_ExpandedGlyphVisibilityProperty: _Callable
                    get_CollapsedGlyphVisibilityProperty: _Callable
                    get_IndentationProperty: _Callable
                    get_DragItemsCountProperty: _Callable

                class ITreeViewList(IInspectable):
                    pass

                class ITreeViewListFactory(IInspectable):
                    CreateInstance: _Callable

                class ITreeViewNode(IInspectable):
                    get_Content: _Callable
                    put_Content: _Callable
                    get_Parent: _Callable
                    get_IsExpanded: _Callable
                    put_IsExpanded: _Callable
                    get_HasChildren: _Callable
                    get_Depth: _Callable
                    get_HasUnrealizedChildren: _Callable
                    put_HasUnrealizedChildren: _Callable
                    get_Children: _Callable

                class ITreeViewNodeFactory(IInspectable):
                    CreateInstance: _Callable

                class ITreeViewNodeStatics(IInspectable):
                    get_ContentProperty: _Callable
                    get_DepthProperty: _Callable
                    get_IsExpandedProperty: _Callable
                    get_HasChildrenProperty: _Callable

                class ITreeViewStatics(IInspectable):
                    get_SelectionModeProperty: _Callable

                class ITreeViewStatics2(IInspectable):
                    get_CanDragItemsProperty: _Callable
                    get_CanReorderItemsProperty: _Callable
                    get_ItemTemplateProperty: _Callable
                    get_ItemTemplateSelectorProperty: _Callable
                    get_ItemContainerStyleProperty: _Callable
                    get_ItemContainerStyleSelectorProperty: _Callable
                    get_ItemContainerTransitionsProperty: _Callable
                    get_ItemsSourceProperty: _Callable

                class ITwoPaneView(IInspectable):
                    get_Pane1: _Callable
                    put_Pane1: _Callable
                    get_Pane2: _Callable
                    put_Pane2: _Callable
                    get_Pane1Length: _Callable
                    put_Pane1Length: _Callable
                    get_Pane2Length: _Callable
                    put_Pane2Length: _Callable
                    get_PanePriority: _Callable
                    put_PanePriority: _Callable
                    get_Mode: _Callable
                    get_WideModeConfiguration: _Callable
                    put_WideModeConfiguration: _Callable
                    get_TallModeConfiguration: _Callable
                    put_TallModeConfiguration: _Callable
                    get_MinWideModeWidth: _Callable
                    put_MinWideModeWidth: _Callable
                    get_MinTallModeHeight: _Callable
                    put_MinTallModeHeight: _Callable
                    add_ModeChanged: _Callable
                    remove_ModeChanged: _Callable

                class ITwoPaneViewFactory(IInspectable):
                    CreateInstance: _Callable

                class ITwoPaneViewStatics(IInspectable):
                    get_Pane1Property: _Callable
                    get_Pane2Property: _Callable
                    get_Pane1LengthProperty: _Callable
                    get_Pane2LengthProperty: _Callable
                    get_PanePriorityProperty: _Callable
                    get_ModeProperty: _Callable
                    get_WideModeConfigurationProperty: _Callable
                    get_TallModeConfigurationProperty: _Callable
                    get_MinWideModeWidthProperty: _Callable
                    get_MinTallModeHeightProperty: _Callable

                class IUIElementCollection(IInspectable):
                    Move: _Callable[[_type.UINT32,
                                     _type.UINT32],
                                    _type.HRESULT]

                class IUserControl(IInspectable):
                    get_Content: _Callable
                    put_Content: _Callable

                class IUserControlFactory(IInspectable):
                    CreateInstance: _Callable

                class IUserControlStatics(IInspectable):
                    get_ContentProperty: _Callable

                class IVariableSizedWrapGrid(IInspectable):
                    get_ItemHeight: _Callable
                    put_ItemHeight: _Callable
                    get_ItemWidth: _Callable
                    put_ItemWidth: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    get_HorizontalChildrenAlignment: _Callable
                    put_HorizontalChildrenAlignment: _Callable
                    get_VerticalChildrenAlignment: _Callable
                    put_VerticalChildrenAlignment: _Callable
                    get_MaximumRowsOrColumns: _Callable
                    put_MaximumRowsOrColumns: _Callable

                class IVariableSizedWrapGridStatics(IInspectable):
                    get_ItemHeightProperty: _Callable
                    get_ItemWidthProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_HorizontalChildrenAlignmentProperty: _Callable
                    get_VerticalChildrenAlignmentProperty: _Callable
                    get_MaximumRowsOrColumnsProperty: _Callable
                    get_RowSpanProperty: _Callable
                    GetRowSpan: _Callable
                    SetRowSpan: _Callable
                    get_ColumnSpanProperty: _Callable
                    GetColumnSpan: _Callable
                    SetColumnSpan: _Callable

                class IViewbox(IInspectable):
                    get_Child: _Callable
                    put_Child: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable
                    get_StretchDirection: _Callable
                    put_StretchDirection: _Callable

                class IViewboxStatics(IInspectable):
                    get_StretchProperty: _Callable
                    get_StretchDirectionProperty: _Callable

                class IVirtualizingPanel(IInspectable):
                    get_ItemContainerGenerator: _Callable

                class IVirtualizingPanelFactory(IInspectable):
                    pass

                class IVirtualizingPanelOverrides(IInspectable):
                    OnItemsChanged: _Callable
                    OnClearChildren: _Callable
                    BringIndexIntoView: _Callable

                class IVirtualizingPanelProtected(IInspectable):
                    AddInternalChild: _Callable
                    InsertInternalChild: _Callable
                    RemoveInternalChildRange: _Callable

                class IVirtualizingStackPanel(IInspectable):
                    get_AreScrollSnapPointsRegular: _Callable
                    put_AreScrollSnapPointsRegular: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    add_CleanUpVirtualizedItemEvent: _Callable
                    remove_CleanUpVirtualizedItemEvent: _Callable

                class IVirtualizingStackPanelOverrides(IInspectable):
                    OnCleanUpVirtualizedItem: _Callable

                class IVirtualizingStackPanelStatics(IInspectable):
                    get_AreScrollSnapPointsRegularProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_VirtualizationModeProperty: _Callable
                    GetVirtualizationMode: _Callable
                    SetVirtualizationMode: _Callable
                    get_IsVirtualizingProperty: _Callable
                    GetIsVirtualizing: _Callable

                class IWebView(IInspectable):
                    get_Source: _Callable
                    put_Source: _Callable
                    get_AllowedScriptNotifyUris: _Callable
                    put_AllowedScriptNotifyUris: _Callable
                    get_DataTransferPackage: _Callable
                    add_LoadCompleted: _Callable
                    remove_LoadCompleted: _Callable
                    add_ScriptNotify: _Callable
                    remove_ScriptNotify: _Callable
                    add_NavigationFailed: _Callable
                    remove_NavigationFailed: _Callable
                    InvokeScript: _Callable
                    Navigate: _Callable
                    NavigateToString: _Callable

                class IWebView2(IInspectable):
                    get_CanGoBack: _Callable
                    get_CanGoForward: _Callable
                    get_DocumentTitle: _Callable
                    add_NavigationStarting: _Callable
                    remove_NavigationStarting: _Callable
                    add_ContentLoading: _Callable
                    remove_ContentLoading: _Callable
                    add_DOMContentLoaded: _Callable
                    remove_DOMContentLoaded: _Callable
                    GoForward: _Callable
                    GoBack: _Callable
                    Refresh: _Callable
                    Stop: _Callable
                    CapturePreviewToStreamAsync: _Callable
                    InvokeScriptAsync: _Callable
                    CaptureSelectedContentToDataPackageAsync: _Callable
                    NavigateToLocalStreamUri: _Callable
                    BuildLocalStreamUri: _Callable
                    get_DefaultBackgroundColor: _Callable
                    put_DefaultBackgroundColor: _Callable
                    add_NavigationCompleted: _Callable
                    remove_NavigationCompleted: _Callable
                    add_FrameNavigationStarting: _Callable
                    remove_FrameNavigationStarting: _Callable
                    add_FrameContentLoading: _Callable
                    remove_FrameContentLoading: _Callable
                    add_FrameDOMContentLoaded: _Callable
                    remove_FrameDOMContentLoaded: _Callable
                    add_FrameNavigationCompleted: _Callable
                    remove_FrameNavigationCompleted: _Callable
                    add_LongRunningScriptDetected: _Callable
                    remove_LongRunningScriptDetected: _Callable
                    add_UnsafeContentWarningDisplaying: _Callable
                    remove_UnsafeContentWarningDisplaying: _Callable
                    add_UnviewableContentIdentified: _Callable
                    remove_UnviewableContentIdentified: _Callable
                    NavigateWithHttpRequestMessage: _Callable
                    Focus: _Callable

                class IWebView3(IInspectable):
                    get_ContainsFullScreenElement: _Callable
                    add_ContainsFullScreenElementChanged: _Callable
                    remove_ContainsFullScreenElementChanged: _Callable

                class IWebView4(IInspectable):
                    get_ExecutionMode: _Callable
                    get_DeferredPermissionRequests: _Callable
                    get_Settings: _Callable
                    add_UnsupportedUriSchemeIdentified: _Callable
                    remove_UnsupportedUriSchemeIdentified: _Callable
                    add_NewWindowRequested: _Callable
                    remove_NewWindowRequested: _Callable
                    add_PermissionRequested: _Callable
                    remove_PermissionRequested: _Callable
                    AddWebAllowedObject: _Callable
                    DeferredPermissionRequestById: _Callable

                class IWebView5(IInspectable):
                    get_XYFocusLeft: _Callable
                    put_XYFocusLeft: _Callable
                    get_XYFocusRight: _Callable
                    put_XYFocusRight: _Callable
                    get_XYFocusUp: _Callable
                    put_XYFocusUp: _Callable
                    get_XYFocusDown: _Callable
                    put_XYFocusDown: _Callable

                class IWebView6(IInspectable):
                    add_SeparateProcessLost: _Callable
                    remove_SeparateProcessLost: _Callable

                class IWebView7(IInspectable):
                    add_WebResourceRequested: _Callable
                    remove_WebResourceRequested: _Callable

                class IWebViewBrush(IInspectable):
                    get_SourceName: _Callable
                    put_SourceName: _Callable
                    Redraw: _Callable
                    SetSource: _Callable

                class IWebViewBrushStatics(IInspectable):
                    get_SourceNameProperty: _Callable

                class IWebViewContentLoadingEventArgs(IInspectable):
                    get_Uri: _Callable

                class IWebViewDOMContentLoadedEventArgs(IInspectable):
                    get_Uri: _Callable

                class IWebViewDeferredPermissionRequest(IInspectable):
                    get_Uri: _Callable
                    get_PermissionType: _Callable
                    get_Id: _Callable
                    Allow: _Callable
                    Deny: _Callable

                class IWebViewFactory4(IInspectable):
                    CreateInstanceWithExecutionMode: _Callable

                class IWebViewLongRunningScriptDetectedEventArgs(IInspectable):
                    get_ExecutionTime: _Callable
                    get_StopPageScriptExecution: _Callable
                    put_StopPageScriptExecution: _Callable

                class IWebViewNavigationCompletedEventArgs(IInspectable):
                    get_Uri: _Callable
                    get_IsSuccess: _Callable
                    get_WebErrorStatus: _Callable

                class IWebViewNavigationFailedEventArgs(IInspectable):
                    get_Uri: _Callable
                    get_WebErrorStatus: _Callable

                class IWebViewNavigationStartingEventArgs(IInspectable):
                    get_Uri: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class IWebViewNewWindowRequestedEventArgs(IInspectable):
                    get_Uri: _Callable
                    get_Referrer: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IWebViewPermissionRequest(IInspectable):
                    get_Uri: _Callable
                    get_PermissionType: _Callable
                    get_Id: _Callable
                    get_State: _Callable
                    Defer: _Callable
                    Allow: _Callable
                    Deny: _Callable

                class IWebViewPermissionRequestedEventArgs(IInspectable):
                    get_PermissionRequest: _Callable

                class IWebViewSeparateProcessLostEventArgs(IInspectable):
                    pass

                class IWebViewSettings(IInspectable):
                    get_IsJavaScriptEnabled: _Callable
                    put_IsJavaScriptEnabled: _Callable
                    get_IsIndexedDBEnabled: _Callable
                    put_IsIndexedDBEnabled: _Callable

                class IWebViewStatics(IInspectable):
                    get_AnyScriptNotifyUri: _Callable
                    get_SourceProperty: _Callable
                    get_AllowedScriptNotifyUrisProperty: _Callable
                    get_DataTransferPackageProperty: _Callable

                class IWebViewStatics2(IInspectable):
                    get_CanGoBackProperty: _Callable
                    get_CanGoForwardProperty: _Callable
                    get_DocumentTitleProperty: _Callable
                    get_DefaultBackgroundColorProperty: _Callable

                class IWebViewStatics3(IInspectable):
                    get_ContainsFullScreenElementProperty: _Callable

                class IWebViewStatics4(IInspectable):
                    get_DefaultExecutionMode: _Callable
                    ClearTemporaryWebDataAsync: _Callable

                class IWebViewStatics5(IInspectable):
                    get_XYFocusLeftProperty: _Callable
                    get_XYFocusRightProperty: _Callable
                    get_XYFocusUpProperty: _Callable
                    get_XYFocusDownProperty: _Callable

                class IWebViewUnsupportedUriSchemeIdentifiedEventArgs(IInspectable):
                    get_Uri: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IWebViewUnviewableContentIdentifiedEventArgs(IInspectable):
                    get_Uri: _Callable
                    get_Referrer: _Callable

                class IWebViewUnviewableContentIdentifiedEventArgs2(IInspectable):
                    get_MediaType: _Callable

                class IWebViewWebResourceRequestedEventArgs(IInspectable):
                    get_Request: _Callable
                    get_Response: _Callable
                    put_Response: _Callable
                    GetDeferral: _Callable

                class IWrapGrid(IInspectable):
                    get_ItemWidth: _Callable
                    put_ItemWidth: _Callable
                    get_ItemHeight: _Callable
                    put_ItemHeight: _Callable
                    get_Orientation: _Callable
                    put_Orientation: _Callable
                    get_HorizontalChildrenAlignment: _Callable
                    put_HorizontalChildrenAlignment: _Callable
                    get_VerticalChildrenAlignment: _Callable
                    put_VerticalChildrenAlignment: _Callable
                    get_MaximumRowsOrColumns: _Callable
                    put_MaximumRowsOrColumns: _Callable

                class IWrapGridStatics(IInspectable):
                    get_ItemWidthProperty: _Callable
                    get_ItemHeightProperty: _Callable
                    get_OrientationProperty: _Callable
                    get_HorizontalChildrenAlignmentProperty: _Callable
                    get_VerticalChildrenAlignmentProperty: _Callable
                    get_MaximumRowsOrColumnsProperty: _Callable

                class Primitives:
                    class _IDragCompletedEventHandler:
                        Invoke: _Callable

                    class IDragCompletedEventHandler(_IDragCompletedEventHandler, IUnknown):
                        pass

                    # noinspection PyPep8Naming
                    class IDragCompletedEventHandler_impl(_IDragCompletedEventHandler, IUnknown_impl):
                        pass

                    class _IDragDeltaEventHandler:
                        Invoke: _Callable

                    class IDragDeltaEventHandler(_IDragDeltaEventHandler, IUnknown):
                        pass

                    # noinspection PyPep8Naming
                    class IDragDeltaEventHandler_impl(_IDragDeltaEventHandler, IUnknown_impl):
                        pass

                    class _IDragStartedEventHandler:
                        Invoke: _Callable

                    class IDragStartedEventHandler(_IDragStartedEventHandler, IUnknown):
                        pass

                    # noinspection PyPep8Naming
                    class IDragStartedEventHandler_impl(_IDragStartedEventHandler, IUnknown_impl):
                        pass

                    class _IItemsChangedEventHandler:
                        Invoke: _Callable

                    class IItemsChangedEventHandler(_IItemsChangedEventHandler, IUnknown):
                        pass

                    # noinspection PyPep8Naming
                    class IItemsChangedEventHandler_impl(_IItemsChangedEventHandler, IUnknown_impl):
                        pass

                    class _IRangeBaseValueChangedEventHandler:
                        Invoke: _Callable

                    class IRangeBaseValueChangedEventHandler(_IRangeBaseValueChangedEventHandler, IUnknown):
                        pass

                    # noinspection PyPep8Naming
                    class IRangeBaseValueChangedEventHandler_impl(_IRangeBaseValueChangedEventHandler, IUnknown_impl):
                        pass

                    class _IScrollEventHandler:
                        Invoke: _Callable

                    class IScrollEventHandler(_IScrollEventHandler, IUnknown):
                        pass

                    # noinspection PyPep8Naming
                    class IScrollEventHandler_impl(_IScrollEventHandler, IUnknown_impl):
                        pass

                    class IAppBarButtonTemplateSettings(IInspectable):
                        get_KeyboardAcceleratorTextMinWidth: _Callable

                    class IAppBarTemplateSettings(IInspectable):
                        get_ClipRect: _Callable
                        get_CompactVerticalDelta: _Callable
                        get_CompactRootMargin: _Callable
                        get_MinimalVerticalDelta: _Callable
                        get_MinimalRootMargin: _Callable
                        get_HiddenVerticalDelta: _Callable
                        get_HiddenRootMargin: _Callable

                    class IAppBarTemplateSettings2(IInspectable):
                        get_NegativeCompactVerticalDelta: _Callable
                        get_NegativeMinimalVerticalDelta: _Callable
                        get_NegativeHiddenVerticalDelta: _Callable

                    class IAppBarToggleButtonTemplateSettings(IInspectable):
                        get_KeyboardAcceleratorTextMinWidth: _Callable

                    class IButtonBase(IInspectable):
                        get_ClickMode: _Callable
                        put_ClickMode: _Callable
                        get_IsPointerOver: _Callable
                        get_IsPressed: _Callable
                        get_Command: _Callable
                        put_Command: _Callable
                        get_CommandParameter: _Callable
                        put_CommandParameter: _Callable
                        add_Click: _Callable
                        remove_Click: _Callable

                    class IButtonBaseFactory(IInspectable):
                        CreateInstance: _Callable

                    class IButtonBaseStatics(IInspectable):
                        get_ClickModeProperty: _Callable
                        get_IsPointerOverProperty: _Callable
                        get_IsPressedProperty: _Callable
                        get_CommandProperty: _Callable
                        get_CommandParameterProperty: _Callable

                    class ICalendarPanel(IInspectable):
                        pass

                    class ICalendarViewTemplateSettings(IInspectable):
                        get_MinViewWidth: _Callable
                        get_HeaderText: _Callable
                        get_WeekDay1: _Callable
                        get_WeekDay2: _Callable
                        get_WeekDay3: _Callable
                        get_WeekDay4: _Callable
                        get_WeekDay5: _Callable
                        get_WeekDay6: _Callable
                        get_WeekDay7: _Callable
                        get_HasMoreContentAfter: _Callable
                        get_HasMoreContentBefore: _Callable
                        get_HasMoreViews: _Callable
                        get_ClipRect: _Callable
                        get_CenterX: _Callable
                        get_CenterY: _Callable

                    class ICarouselPanel(IInspectable):
                        get_CanVerticallyScroll: _Callable
                        put_CanVerticallyScroll: _Callable
                        get_CanHorizontallyScroll: _Callable
                        put_CanHorizontallyScroll: _Callable
                        get_ExtentWidth: _Callable
                        get_ExtentHeight: _Callable
                        get_ViewportWidth: _Callable
                        get_ViewportHeight: _Callable
                        get_HorizontalOffset: _Callable
                        get_VerticalOffset: _Callable
                        get_ScrollOwner: _Callable
                        put_ScrollOwner: _Callable
                        LineUp: _Callable
                        LineDown: _Callable
                        LineLeft: _Callable
                        LineRight: _Callable
                        PageUp: _Callable
                        PageDown: _Callable
                        PageLeft: _Callable
                        PageRight: _Callable
                        MouseWheelUp: _Callable
                        MouseWheelDown: _Callable
                        MouseWheelLeft: _Callable
                        MouseWheelRight: _Callable
                        SetHorizontalOffset: _Callable
                        SetVerticalOffset: _Callable
                        MakeVisible: _Callable

                    class ICarouselPanelFactory(IInspectable):
                        CreateInstance: _Callable

                    class IColorPickerSlider(IInspectable):
                        get_ColorChannel: _Callable
                        put_ColorChannel: _Callable

                    class IColorPickerSliderFactory(IInspectable):
                        CreateInstance: _Callable

                    class IColorPickerSliderStatics(IInspectable):
                        get_ColorChannelProperty: _Callable

                    class IColorSpectrum(IInspectable):
                        get_Color: _Callable
                        put_Color: _Callable
                        get_HsvColor: _Callable
                        put_HsvColor: _Callable
                        get_MinHue: _Callable
                        put_MinHue: _Callable
                        get_MaxHue: _Callable
                        put_MaxHue: _Callable
                        get_MinSaturation: _Callable
                        put_MinSaturation: _Callable
                        get_MaxSaturation: _Callable
                        put_MaxSaturation: _Callable
                        get_MinValue: _Callable
                        put_MinValue: _Callable
                        get_MaxValue: _Callable
                        put_MaxValue: _Callable
                        get_Shape: _Callable
                        put_Shape: _Callable
                        get_Components: _Callable
                        put_Components: _Callable
                        add_ColorChanged: _Callable
                        remove_ColorChanged: _Callable

                    class IColorSpectrumFactory(IInspectable):
                        CreateInstance: _Callable

                    class IColorSpectrumStatics(IInspectable):
                        get_ColorProperty: _Callable
                        get_HsvColorProperty: _Callable
                        get_MinHueProperty: _Callable
                        get_MaxHueProperty: _Callable
                        get_MinSaturationProperty: _Callable
                        get_MaxSaturationProperty: _Callable
                        get_MinValueProperty: _Callable
                        get_MaxValueProperty: _Callable
                        get_ShapeProperty: _Callable
                        get_ComponentsProperty: _Callable

                    class IComboBoxTemplateSettings(IInspectable):
                        get_DropDownOpenedHeight: _Callable
                        get_DropDownClosedHeight: _Callable
                        get_DropDownOffset: _Callable
                        get_SelectedItemDirection: _Callable

                    class IComboBoxTemplateSettings2(IInspectable):
                        get_DropDownContentMinWidth: _Callable

                    class ICommandBarFlyoutCommandBar(IInspectable):
                        get_FlyoutTemplateSettings: _Callable

                    class ICommandBarFlyoutCommandBarFactory(IInspectable):
                        CreateInstance: _Callable

                    class ICommandBarFlyoutCommandBarTemplateSettings(IInspectable):
                        get_OpenAnimationStartPosition: _Callable
                        get_OpenAnimationEndPosition: _Callable
                        get_CloseAnimationEndPosition: _Callable
                        get_CurrentWidth: _Callable
                        get_ExpandedWidth: _Callable
                        get_WidthExpansionDelta: _Callable
                        get_WidthExpansionAnimationStartPosition: _Callable
                        get_WidthExpansionAnimationEndPosition: _Callable
                        get_WidthExpansionMoreButtonAnimationStartPosition: _Callable
                        get_WidthExpansionMoreButtonAnimationEndPosition: _Callable
                        get_ExpandUpOverflowVerticalPosition: _Callable
                        get_ExpandDownOverflowVerticalPosition: _Callable
                        get_ExpandUpAnimationStartPosition: _Callable
                        get_ExpandUpAnimationEndPosition: _Callable
                        get_ExpandUpAnimationHoldPosition: _Callable
                        get_ExpandDownAnimationStartPosition: _Callable
                        get_ExpandDownAnimationEndPosition: _Callable
                        get_ExpandDownAnimationHoldPosition: _Callable
                        get_ContentClipRect: _Callable
                        get_OverflowContentClipRect: _Callable

                    class ICommandBarTemplateSettings(IInspectable):
                        get_ContentHeight: _Callable
                        get_OverflowContentClipRect: _Callable
                        get_OverflowContentMinWidth: _Callable
                        get_OverflowContentMaxHeight: _Callable
                        get_OverflowContentHorizontalOffset: _Callable
                        get_OverflowContentHeight: _Callable
                        get_NegativeOverflowContentHeight: _Callable

                    class ICommandBarTemplateSettings2(IInspectable):
                        get_OverflowContentMaxWidth: _Callable

                    class ICommandBarTemplateSettings3(IInspectable):
                        get_EffectiveOverflowButtonVisibility: _Callable

                    class ICommandBarTemplateSettings4(IInspectable):
                        get_OverflowContentCompactYTranslation: _Callable
                        get_OverflowContentMinimalYTranslation: _Callable
                        get_OverflowContentHiddenYTranslation: _Callable

                    class IDragCompletedEventArgs(IInspectable):
                        get_HorizontalChange: _Callable
                        get_VerticalChange: _Callable
                        get_Canceled: _Callable

                    class IDragCompletedEventArgsFactory(IInspectable):
                        CreateInstanceWithHorizontalChangeVerticalChangeAndCanceled: _Callable

                    class IDragDeltaEventArgs(IInspectable):
                        get_HorizontalChange: _Callable
                        get_VerticalChange: _Callable

                    class IDragDeltaEventArgsFactory(IInspectable):
                        CreateInstanceWithHorizontalChangeAndVerticalChange: _Callable

                    class IDragStartedEventArgs(IInspectable):
                        get_HorizontalOffset: _Callable
                        get_VerticalOffset: _Callable

                    class IDragStartedEventArgsFactory(IInspectable):
                        CreateInstanceWithHorizontalOffsetAndVerticalOffset: _Callable

                    class IFlyoutBase(IInspectable):
                        get_Placement: _Callable
                        put_Placement: _Callable
                        add_Opened: _Callable
                        remove_Opened: _Callable
                        add_Closed: _Callable
                        remove_Closed: _Callable
                        add_Opening: _Callable
                        remove_Opening: _Callable
                        ShowAt: _Callable
                        Hide: _Callable

                    class IFlyoutBase2(IInspectable):
                        get_Target: _Callable
                        get_AllowFocusOnInteraction: _Callable
                        put_AllowFocusOnInteraction: _Callable
                        get_LightDismissOverlayMode: _Callable
                        put_LightDismissOverlayMode: _Callable
                        get_AllowFocusWhenDisabled: _Callable
                        put_AllowFocusWhenDisabled: _Callable
                        get_ElementSoundMode: _Callable
                        put_ElementSoundMode: _Callable
                        add_Closing: _Callable
                        remove_Closing: _Callable

                    class IFlyoutBase3(IInspectable):
                        get_OverlayInputPassThroughElement: _Callable
                        put_OverlayInputPassThroughElement: _Callable

                    class IFlyoutBase4(IInspectable):
                        TryInvokeKeyboardAccelerator: _Callable

                    class IFlyoutBase5(IInspectable):
                        get_ShowMode: _Callable
                        put_ShowMode: _Callable
                        get_InputDevicePrefersPrimaryCommands: _Callable
                        get_AreOpenCloseAnimationsEnabled: _Callable
                        put_AreOpenCloseAnimationsEnabled: _Callable
                        get_IsOpen: _Callable
                        ShowAt: _Callable

                    class IFlyoutBase6(IInspectable):
                        get_ShouldConstrainToRootBounds: _Callable
                        put_ShouldConstrainToRootBounds: _Callable
                        get_IsConstrainedToRootBounds: _Callable
                        get_XamlRoot: _Callable
                        put_XamlRoot: _Callable

                    class IFlyoutBaseClosingEventArgs(IInspectable):
                        get_Cancel: _Callable
                        put_Cancel: _Callable

                    class IFlyoutBaseFactory(IInspectable):
                        CreateInstance: _Callable

                    class IFlyoutBaseOverrides(IInspectable):
                        CreatePresenter: _Callable

                    class IFlyoutBaseOverrides4(IInspectable):
                        OnProcessKeyboardAccelerators: _Callable

                    class IFlyoutBaseStatics(IInspectable):
                        get_PlacementProperty: _Callable
                        get_AttachedFlyoutProperty: _Callable
                        GetAttachedFlyout: _Callable
                        SetAttachedFlyout: _Callable
                        ShowAttachedFlyout: _Callable

                    class IFlyoutBaseStatics2(IInspectable):
                        get_AllowFocusOnInteractionProperty: _Callable
                        get_LightDismissOverlayModeProperty: _Callable
                        get_AllowFocusWhenDisabledProperty: _Callable
                        get_ElementSoundModeProperty: _Callable

                    class IFlyoutBaseStatics3(IInspectable):
                        get_OverlayInputPassThroughElementProperty: _Callable

                    class IFlyoutBaseStatics5(IInspectable):
                        get_TargetProperty: _Callable
                        get_ShowModeProperty: _Callable
                        get_InputDevicePrefersPrimaryCommandsProperty: _Callable
                        get_AreOpenCloseAnimationsEnabledProperty: _Callable
                        get_IsOpenProperty: _Callable

                    class IFlyoutBaseStatics6(IInspectable):
                        get_ShouldConstrainToRootBoundsProperty: _Callable

                    class IFlyoutShowOptions(IInspectable):
                        get_Position: _Callable
                        put_Position: _Callable
                        get_ExclusionRect: _Callable
                        put_ExclusionRect: _Callable
                        get_ShowMode: _Callable
                        put_ShowMode: _Callable
                        get_Placement: _Callable
                        put_Placement: _Callable

                    class IFlyoutShowOptionsFactory(IInspectable):
                        CreateInstance: _Callable

                    class IGeneratorPositionHelper(IInspectable):
                        pass

                    class IGeneratorPositionHelperStatics(IInspectable):
                        FromIndexAndOffset: _Callable

                    class IGridViewItemPresenter(IInspectable):
                        get_SelectionCheckMarkVisualEnabled: _Callable
                        put_SelectionCheckMarkVisualEnabled: _Callable
                        get_CheckHintBrush: _Callable
                        put_CheckHintBrush: _Callable
                        get_CheckSelectingBrush: _Callable
                        put_CheckSelectingBrush: _Callable
                        get_CheckBrush: _Callable
                        put_CheckBrush: _Callable
                        get_DragBackground: _Callable
                        put_DragBackground: _Callable
                        get_DragForeground: _Callable
                        put_DragForeground: _Callable
                        get_FocusBorderBrush: _Callable
                        put_FocusBorderBrush: _Callable
                        get_PlaceholderBackground: _Callable
                        put_PlaceholderBackground: _Callable
                        get_PointerOverBackground: _Callable
                        put_PointerOverBackground: _Callable
                        get_SelectedBackground: _Callable
                        put_SelectedBackground: _Callable
                        get_SelectedForeground: _Callable
                        put_SelectedForeground: _Callable
                        get_SelectedPointerOverBackground: _Callable
                        put_SelectedPointerOverBackground: _Callable
                        get_SelectedPointerOverBorderBrush: _Callable
                        put_SelectedPointerOverBorderBrush: _Callable
                        get_SelectedBorderThickness: _Callable
                        put_SelectedBorderThickness: _Callable
                        get_DisabledOpacity: _Callable
                        put_DisabledOpacity: _Callable
                        get_DragOpacity: _Callable
                        put_DragOpacity: _Callable
                        get_ReorderHintOffset: _Callable
                        put_ReorderHintOffset: _Callable
                        get_GridViewItemPresenterHorizontalContentAlignment: _Callable
                        put_GridViewItemPresenterHorizontalContentAlignment: _Callable
                        get_GridViewItemPresenterVerticalContentAlignment: _Callable
                        put_GridViewItemPresenterVerticalContentAlignment: _Callable
                        get_GridViewItemPresenterPadding: _Callable
                        put_GridViewItemPresenterPadding: _Callable
                        get_PointerOverBackgroundMargin: _Callable
                        put_PointerOverBackgroundMargin: _Callable
                        get_ContentMargin: _Callable
                        put_ContentMargin: _Callable

                    class IGridViewItemPresenterFactory(IInspectable):
                        CreateInstance: _Callable

                    class IGridViewItemPresenterStatics(IInspectable):
                        get_SelectionCheckMarkVisualEnabledProperty: _Callable
                        get_CheckHintBrushProperty: _Callable
                        get_CheckSelectingBrushProperty: _Callable
                        get_CheckBrushProperty: _Callable
                        get_DragBackgroundProperty: _Callable
                        get_DragForegroundProperty: _Callable
                        get_FocusBorderBrushProperty: _Callable
                        get_PlaceholderBackgroundProperty: _Callable
                        get_PointerOverBackgroundProperty: _Callable
                        get_SelectedBackgroundProperty: _Callable
                        get_SelectedForegroundProperty: _Callable
                        get_SelectedPointerOverBackgroundProperty: _Callable
                        get_SelectedPointerOverBorderBrushProperty: _Callable
                        get_SelectedBorderThicknessProperty: _Callable
                        get_DisabledOpacityProperty: _Callable
                        get_DragOpacityProperty: _Callable
                        get_ReorderHintOffsetProperty: _Callable
                        get_GridViewItemPresenterHorizontalContentAlignmentProperty: _Callable
                        get_GridViewItemPresenterVerticalContentAlignmentProperty: _Callable
                        get_GridViewItemPresenterPaddingProperty: _Callable
                        get_PointerOverBackgroundMarginProperty: _Callable
                        get_ContentMarginProperty: _Callable

                    class IGridViewItemTemplateSettings(IInspectable):
                        get_DragItemsCount: _Callable

                    class IItemsChangedEventArgs(IInspectable):
                        get_Action: _Callable
                        get_Position: _Callable
                        get_OldPosition: _Callable
                        get_ItemCount: _Callable
                        get_ItemUICount: _Callable

                    class IJumpListItemBackgroundConverter(IInspectable):
                        get_Enabled: _Callable
                        put_Enabled: _Callable
                        get_Disabled: _Callable
                        put_Disabled: _Callable

                    class IJumpListItemBackgroundConverterStatics(IInspectable):
                        get_EnabledProperty: _Callable
                        get_DisabledProperty: _Callable

                    class IJumpListItemForegroundConverter(IInspectable):
                        get_Enabled: _Callable
                        put_Enabled: _Callable
                        get_Disabled: _Callable
                        put_Disabled: _Callable

                    class IJumpListItemForegroundConverterStatics(IInspectable):
                        get_EnabledProperty: _Callable
                        get_DisabledProperty: _Callable

                    class ILayoutInformation(IInspectable):
                        pass

                    class ILayoutInformationStatics(IInspectable):
                        GetLayoutExceptionElement: _Callable
                        GetLayoutSlot: _Callable

                    class ILayoutInformationStatics2(IInspectable):
                        GetAvailableSize: _Callable

                    class IListViewItemPresenter(IInspectable):
                        get_SelectionCheckMarkVisualEnabled: _Callable
                        put_SelectionCheckMarkVisualEnabled: _Callable
                        get_CheckHintBrush: _Callable
                        put_CheckHintBrush: _Callable
                        get_CheckSelectingBrush: _Callable
                        put_CheckSelectingBrush: _Callable
                        get_CheckBrush: _Callable
                        put_CheckBrush: _Callable
                        get_DragBackground: _Callable
                        put_DragBackground: _Callable
                        get_DragForeground: _Callable
                        put_DragForeground: _Callable
                        get_FocusBorderBrush: _Callable
                        put_FocusBorderBrush: _Callable
                        get_PlaceholderBackground: _Callable
                        put_PlaceholderBackground: _Callable
                        get_PointerOverBackground: _Callable
                        put_PointerOverBackground: _Callable
                        get_SelectedBackground: _Callable
                        put_SelectedBackground: _Callable
                        get_SelectedForeground: _Callable
                        put_SelectedForeground: _Callable
                        get_SelectedPointerOverBackground: _Callable
                        put_SelectedPointerOverBackground: _Callable
                        get_SelectedPointerOverBorderBrush: _Callable
                        put_SelectedPointerOverBorderBrush: _Callable
                        get_SelectedBorderThickness: _Callable
                        put_SelectedBorderThickness: _Callable
                        get_DisabledOpacity: _Callable
                        put_DisabledOpacity: _Callable
                        get_DragOpacity: _Callable
                        put_DragOpacity: _Callable
                        get_ReorderHintOffset: _Callable
                        put_ReorderHintOffset: _Callable
                        get_ListViewItemPresenterHorizontalContentAlignment: _Callable
                        put_ListViewItemPresenterHorizontalContentAlignment: _Callable
                        get_ListViewItemPresenterVerticalContentAlignment: _Callable
                        put_ListViewItemPresenterVerticalContentAlignment: _Callable
                        get_ListViewItemPresenterPadding: _Callable
                        put_ListViewItemPresenterPadding: _Callable
                        get_PointerOverBackgroundMargin: _Callable
                        put_PointerOverBackgroundMargin: _Callable
                        get_ContentMargin: _Callable
                        put_ContentMargin: _Callable

                    class IListViewItemPresenter2(IInspectable):
                        get_SelectedPressedBackground: _Callable
                        put_SelectedPressedBackground: _Callable
                        get_PressedBackground: _Callable
                        put_PressedBackground: _Callable
                        get_CheckBoxBrush: _Callable
                        put_CheckBoxBrush: _Callable
                        get_FocusSecondaryBorderBrush: _Callable
                        put_FocusSecondaryBorderBrush: _Callable
                        get_CheckMode: _Callable
                        put_CheckMode: _Callable
                        get_PointerOverForeground: _Callable
                        put_PointerOverForeground: _Callable

                    class IListViewItemPresenter3(IInspectable):
                        get_RevealBackground: _Callable
                        put_RevealBackground: _Callable
                        get_RevealBorderBrush: _Callable
                        put_RevealBorderBrush: _Callable
                        get_RevealBorderThickness: _Callable
                        put_RevealBorderThickness: _Callable
                        get_RevealBackgroundShowsAboveContent: _Callable
                        put_RevealBackgroundShowsAboveContent: _Callable

                    class IListViewItemPresenter4(IInspectable):
                        get_SelectedDisabledBackground: _Callable
                        put_SelectedDisabledBackground: _Callable
                        get_CheckPressedBrush: _Callable
                        put_CheckPressedBrush: _Callable
                        get_CheckDisabledBrush: _Callable
                        put_CheckDisabledBrush: _Callable
                        get_CheckBoxPointerOverBrush: _Callable
                        put_CheckBoxPointerOverBrush: _Callable
                        get_CheckBoxPressedBrush: _Callable
                        put_CheckBoxPressedBrush: _Callable
                        get_CheckBoxDisabledBrush: _Callable
                        put_CheckBoxDisabledBrush: _Callable
                        get_CheckBoxSelectedBrush: _Callable
                        put_CheckBoxSelectedBrush: _Callable
                        get_CheckBoxSelectedPointerOverBrush: _Callable
                        put_CheckBoxSelectedPointerOverBrush: _Callable
                        get_CheckBoxSelectedPressedBrush: _Callable
                        put_CheckBoxSelectedPressedBrush: _Callable
                        get_CheckBoxSelectedDisabledBrush: _Callable
                        put_CheckBoxSelectedDisabledBrush: _Callable
                        get_CheckBoxBorderBrush: _Callable
                        put_CheckBoxBorderBrush: _Callable
                        get_CheckBoxPointerOverBorderBrush: _Callable
                        put_CheckBoxPointerOverBorderBrush: _Callable
                        get_CheckBoxPressedBorderBrush: _Callable
                        put_CheckBoxPressedBorderBrush: _Callable
                        get_CheckBoxDisabledBorderBrush: _Callable
                        put_CheckBoxDisabledBorderBrush: _Callable
                        get_CheckBoxCornerRadius: _Callable
                        put_CheckBoxCornerRadius: _Callable
                        get_SelectionIndicatorCornerRadius: _Callable
                        put_SelectionIndicatorCornerRadius: _Callable
                        get_SelectionIndicatorVisualEnabled: _Callable
                        put_SelectionIndicatorVisualEnabled: _Callable
                        get_SelectionIndicatorMode: _Callable
                        put_SelectionIndicatorMode: _Callable
                        get_SelectionIndicatorBrush: _Callable
                        put_SelectionIndicatorBrush: _Callable
                        get_SelectionIndicatorPointerOverBrush: _Callable
                        put_SelectionIndicatorPointerOverBrush: _Callable
                        get_SelectionIndicatorPressedBrush: _Callable
                        put_SelectionIndicatorPressedBrush: _Callable
                        get_SelectionIndicatorDisabledBrush: _Callable
                        put_SelectionIndicatorDisabledBrush: _Callable
                        get_SelectedBorderBrush: _Callable
                        put_SelectedBorderBrush: _Callable
                        get_SelectedPressedBorderBrush: _Callable
                        put_SelectedPressedBorderBrush: _Callable
                        get_SelectedDisabledBorderBrush: _Callable
                        put_SelectedDisabledBorderBrush: _Callable
                        get_SelectedInnerBorderBrush: _Callable
                        put_SelectedInnerBorderBrush: _Callable
                        get_PointerOverBorderBrush: _Callable
                        put_PointerOverBorderBrush: _Callable

                    class IListViewItemPresenterFactory(IInspectable):
                        CreateInstance: _Callable

                    class IListViewItemPresenterStatics(IInspectable):
                        get_SelectionCheckMarkVisualEnabledProperty: _Callable
                        get_CheckHintBrushProperty: _Callable
                        get_CheckSelectingBrushProperty: _Callable
                        get_CheckBrushProperty: _Callable
                        get_DragBackgroundProperty: _Callable
                        get_DragForegroundProperty: _Callable
                        get_FocusBorderBrushProperty: _Callable
                        get_PlaceholderBackgroundProperty: _Callable
                        get_PointerOverBackgroundProperty: _Callable
                        get_SelectedBackgroundProperty: _Callable
                        get_SelectedForegroundProperty: _Callable
                        get_SelectedPointerOverBackgroundProperty: _Callable
                        get_SelectedPointerOverBorderBrushProperty: _Callable
                        get_SelectedBorderThicknessProperty: _Callable
                        get_DisabledOpacityProperty: _Callable
                        get_DragOpacityProperty: _Callable
                        get_ReorderHintOffsetProperty: _Callable
                        get_ListViewItemPresenterHorizontalContentAlignmentProperty: _Callable
                        get_ListViewItemPresenterVerticalContentAlignmentProperty: _Callable
                        get_ListViewItemPresenterPaddingProperty: _Callable
                        get_PointerOverBackgroundMarginProperty: _Callable
                        get_ContentMarginProperty: _Callable

                    class IListViewItemPresenterStatics2(IInspectable):
                        get_SelectedPressedBackgroundProperty: _Callable
                        get_PressedBackgroundProperty: _Callable
                        get_CheckBoxBrushProperty: _Callable
                        get_FocusSecondaryBorderBrushProperty: _Callable
                        get_CheckModeProperty: _Callable
                        get_PointerOverForegroundProperty: _Callable

                    class IListViewItemPresenterStatics3(IInspectable):
                        get_RevealBackgroundProperty: _Callable
                        get_RevealBorderBrushProperty: _Callable
                        get_RevealBorderThicknessProperty: _Callable
                        get_RevealBackgroundShowsAboveContentProperty: _Callable

                    class IListViewItemPresenterStatics4(IInspectable):
                        get_SelectedDisabledBackgroundProperty: _Callable
                        get_CheckPressedBrushProperty: _Callable
                        get_CheckDisabledBrushProperty: _Callable
                        get_CheckBoxPointerOverBrushProperty: _Callable
                        get_CheckBoxPressedBrushProperty: _Callable
                        get_CheckBoxDisabledBrushProperty: _Callable
                        get_CheckBoxSelectedBrushProperty: _Callable
                        get_CheckBoxSelectedPointerOverBrushProperty: _Callable
                        get_CheckBoxSelectedPressedBrushProperty: _Callable
                        get_CheckBoxSelectedDisabledBrushProperty: _Callable
                        get_CheckBoxBorderBrushProperty: _Callable
                        get_CheckBoxPointerOverBorderBrushProperty: _Callable
                        get_CheckBoxPressedBorderBrushProperty: _Callable
                        get_CheckBoxDisabledBorderBrushProperty: _Callable
                        get_CheckBoxCornerRadiusProperty: _Callable
                        get_SelectionIndicatorCornerRadiusProperty: _Callable
                        get_SelectionIndicatorVisualEnabledProperty: _Callable
                        get_SelectionIndicatorModeProperty: _Callable
                        get_SelectionIndicatorBrushProperty: _Callable
                        get_SelectionIndicatorPointerOverBrushProperty: _Callable
                        get_SelectionIndicatorPressedBrushProperty: _Callable
                        get_SelectionIndicatorDisabledBrushProperty: _Callable
                        get_SelectedBorderBrushProperty: _Callable
                        get_SelectedPressedBorderBrushProperty: _Callable
                        get_SelectedDisabledBorderBrushProperty: _Callable
                        get_SelectedInnerBorderBrushProperty: _Callable
                        get_PointerOverBorderBrushProperty: _Callable

                    class IListViewItemTemplateSettings(IInspectable):
                        get_DragItemsCount: _Callable

                    class ILoopingSelector(IInspectable):
                        get_ShouldLoop: _Callable
                        put_ShouldLoop: _Callable
                        get_Items: _Callable
                        put_Items: _Callable
                        get_SelectedIndex: _Callable
                        put_SelectedIndex: _Callable
                        get_SelectedItem: _Callable
                        put_SelectedItem: _Callable
                        get_ItemWidth: _Callable
                        put_ItemWidth: _Callable
                        get_ItemHeight: _Callable
                        put_ItemHeight: _Callable
                        get_ItemTemplate: _Callable
                        put_ItemTemplate: _Callable
                        add_SelectionChanged: _Callable
                        remove_SelectionChanged: _Callable

                    class ILoopingSelectorItem(IInspectable):
                        pass

                    class ILoopingSelectorPanel(IInspectable):
                        pass

                    class ILoopingSelectorStatics(IInspectable):
                        get_ShouldLoopProperty: _Callable
                        get_ItemsProperty: _Callable
                        get_SelectedIndexProperty: _Callable
                        get_SelectedItemProperty: _Callable
                        get_ItemWidthProperty: _Callable
                        get_ItemHeightProperty: _Callable
                        get_ItemTemplateProperty: _Callable

                    class IMenuFlyoutItemTemplateSettings(IInspectable):
                        get_KeyboardAcceleratorTextMinWidth: _Callable

                    class IMenuFlyoutPresenterTemplateSettings(IInspectable):
                        get_FlyoutContentMinWidth: _Callable[[_Pointer[_type.DOUBLE]],
                                                             _type.HRESULT]

                    class INavigationViewItemPresenter(IInspectable):
                        get_Icon: _Callable
                        put_Icon: _Callable

                    class INavigationViewItemPresenterFactory(IInspectable):
                        CreateInstance: _Callable

                    class INavigationViewItemPresenterStatics(IInspectable):
                        get_IconProperty: _Callable

                    class IOrientedVirtualizingPanel(IInspectable):
                        get_CanVerticallyScroll: _Callable
                        put_CanVerticallyScroll: _Callable
                        get_CanHorizontallyScroll: _Callable
                        put_CanHorizontallyScroll: _Callable
                        get_ExtentWidth: _Callable
                        get_ExtentHeight: _Callable
                        get_ViewportWidth: _Callable
                        get_ViewportHeight: _Callable
                        get_HorizontalOffset: _Callable
                        get_VerticalOffset: _Callable
                        get_ScrollOwner: _Callable
                        put_ScrollOwner: _Callable
                        LineUp: _Callable
                        LineDown: _Callable
                        LineLeft: _Callable
                        LineRight: _Callable
                        PageUp: _Callable
                        PageDown: _Callable
                        PageLeft: _Callable
                        PageRight: _Callable
                        MouseWheelUp: _Callable
                        MouseWheelDown: _Callable
                        MouseWheelLeft: _Callable
                        MouseWheelRight: _Callable
                        SetHorizontalOffset: _Callable
                        SetVerticalOffset: _Callable
                        MakeVisible: _Callable

                    class IOrientedVirtualizingPanelFactory(IInspectable):
                        pass

                    class IPickerFlyoutBase(IInspectable):
                        pass

                    class IPickerFlyoutBaseFactory(IInspectable):
                        CreateInstance: _Callable

                    class IPickerFlyoutBaseOverrides(IInspectable):
                        OnConfirmed: _Callable
                        ShouldShowConfirmationButtons: _Callable

                    class IPickerFlyoutBaseStatics(IInspectable):
                        get_TitleProperty: _Callable
                        GetTitle: _Callable
                        SetTitle: _Callable

                    class IPivotHeaderItem(IInspectable):
                        pass

                    class IPivotHeaderItemFactory(IInspectable):
                        CreateInstance: _Callable

                    class IPivotHeaderPanel(IInspectable):
                        pass

                    class IPivotPanel(IInspectable):
                        pass

                    class IPopup(IInspectable):
                        get_Child: _Callable
                        put_Child: _Callable
                        get_IsOpen: _Callable
                        put_IsOpen: _Callable
                        get_HorizontalOffset: _Callable
                        put_HorizontalOffset: _Callable
                        get_VerticalOffset: _Callable
                        put_VerticalOffset: _Callable
                        get_ChildTransitions: _Callable
                        put_ChildTransitions: _Callable
                        get_IsLightDismissEnabled: _Callable
                        put_IsLightDismissEnabled: _Callable
                        add_Opened: _Callable
                        remove_Opened: _Callable
                        add_Closed: _Callable
                        remove_Closed: _Callable

                    class IPopup2(IInspectable):
                        get_LightDismissOverlayMode: _Callable
                        put_LightDismissOverlayMode: _Callable

                    class IPopup3(IInspectable):
                        get_ShouldConstrainToRootBounds: _Callable
                        put_ShouldConstrainToRootBounds: _Callable
                        get_IsConstrainedToRootBounds: _Callable

                    class IPopup4(IInspectable):
                        get_PlacementTarget: _Callable
                        put_PlacementTarget: _Callable
                        get_DesiredPlacement: _Callable
                        put_DesiredPlacement: _Callable
                        get_ActualPlacement: _Callable
                        add_ActualPlacementChanged: _Callable
                        remove_ActualPlacementChanged: _Callable

                    class IPopupStatics(IInspectable):
                        get_ChildProperty: _Callable
                        get_IsOpenProperty: _Callable
                        get_HorizontalOffsetProperty: _Callable
                        get_VerticalOffsetProperty: _Callable
                        get_ChildTransitionsProperty: _Callable
                        get_IsLightDismissEnabledProperty: _Callable

                    class IPopupStatics2(IInspectable):
                        get_LightDismissOverlayModeProperty: _Callable

                    class IPopupStatics3(IInspectable):
                        get_ShouldConstrainToRootBoundsProperty: _Callable

                    class IPopupStatics4(IInspectable):
                        get_PlacementTargetProperty: _Callable
                        get_DesiredPlacementProperty: _Callable

                    class IProgressBarTemplateSettings(IInspectable):
                        get_EllipseDiameter: _Callable
                        get_EllipseOffset: _Callable
                        get_EllipseAnimationWellPosition: _Callable
                        get_EllipseAnimationEndPosition: _Callable
                        get_ContainerAnimationStartPosition: _Callable
                        get_ContainerAnimationEndPosition: _Callable
                        get_IndicatorLengthDelta: _Callable

                    class IProgressRingTemplateSettings(IInspectable):
                        get_EllipseDiameter: _Callable
                        get_EllipseOffset: _Callable
                        get_MaxSideLength: _Callable

                    class IRangeBase(IInspectable):
                        get_Minimum: _Callable
                        put_Minimum: _Callable
                        get_Maximum: _Callable
                        put_Maximum: _Callable
                        get_SmallChange: _Callable
                        put_SmallChange: _Callable
                        get_LargeChange: _Callable
                        put_LargeChange: _Callable
                        get_Value: _Callable
                        put_Value: _Callable
                        add_ValueChanged: _Callable
                        remove_ValueChanged: _Callable

                    class IRangeBaseFactory(IInspectable):
                        CreateInstance: _Callable

                    class IRangeBaseOverrides(IInspectable):
                        OnMinimumChanged: _Callable
                        OnMaximumChanged: _Callable
                        OnValueChanged: _Callable

                    class IRangeBaseStatics(IInspectable):
                        get_MinimumProperty: _Callable
                        get_MaximumProperty: _Callable
                        get_SmallChangeProperty: _Callable
                        get_LargeChangeProperty: _Callable
                        get_ValueProperty: _Callable

                    class IRangeBaseValueChangedEventArgs(IInspectable):
                        get_OldValue: _Callable
                        get_NewValue: _Callable

                    class IRepeatButton(IInspectable):
                        get_Delay: _Callable
                        put_Delay: _Callable
                        get_Interval: _Callable
                        put_Interval: _Callable

                    class IRepeatButtonStatics(IInspectable):
                        get_DelayProperty: _Callable
                        get_IntervalProperty: _Callable

                    class IScrollBar(IInspectable):
                        get_Orientation: _Callable
                        put_Orientation: _Callable
                        get_ViewportSize: _Callable
                        put_ViewportSize: _Callable
                        get_IndicatorMode: _Callable
                        put_IndicatorMode: _Callable
                        add_Scroll: _Callable
                        remove_Scroll: _Callable

                    class IScrollBarStatics(IInspectable):
                        get_OrientationProperty: _Callable
                        get_ViewportSizeProperty: _Callable
                        get_IndicatorModeProperty: _Callable

                    class IScrollEventArgs(IInspectable):
                        get_NewValue: _Callable
                        get_ScrollEventType: _Callable

                    class IScrollSnapPointsInfo(IInspectable):
                        get_AreHorizontalSnapPointsRegular: _Callable
                        get_AreVerticalSnapPointsRegular: _Callable
                        add_HorizontalSnapPointsChanged: _Callable
                        remove_HorizontalSnapPointsChanged: _Callable
                        add_VerticalSnapPointsChanged: _Callable
                        remove_VerticalSnapPointsChanged: _Callable
                        GetIrregularSnapPoints: _Callable
                        GetRegularSnapPoints: _Callable

                    class ISelector(IInspectable):
                        get_SelectedIndex: _Callable
                        put_SelectedIndex: _Callable
                        get_SelectedItem: _Callable
                        put_SelectedItem: _Callable
                        get_SelectedValue: _Callable
                        put_SelectedValue: _Callable
                        get_SelectedValuePath: _Callable
                        put_SelectedValuePath: _Callable
                        get_IsSynchronizedWithCurrentItem: _Callable
                        put_IsSynchronizedWithCurrentItem: _Callable
                        add_SelectionChanged: _Callable
                        remove_SelectionChanged: _Callable

                    class ISelectorFactory(IInspectable):
                        pass

                    class ISelectorItem(IInspectable):
                        get_IsSelected: _Callable
                        put_IsSelected: _Callable

                    class ISelectorItemFactory(IInspectable):
                        CreateInstance: _Callable

                    class ISelectorItemStatics(IInspectable):
                        get_IsSelectedProperty: _Callable

                    class ISelectorStatics(IInspectable):
                        get_SelectedIndexProperty: _Callable
                        get_SelectedItemProperty: _Callable
                        get_SelectedValueProperty: _Callable
                        get_SelectedValuePathProperty: _Callable
                        get_IsSynchronizedWithCurrentItemProperty: _Callable
                        GetIsSelectionActive: _Callable

                    class ISettingsFlyoutTemplateSettings(IInspectable):
                        get_HeaderBackground: _Callable
                        get_HeaderForeground: _Callable
                        get_BorderBrush: _Callable
                        get_BorderThickness: _Callable
                        get_IconSource: _Callable
                        get_ContentTransitions: _Callable

                    class ISplitViewTemplateSettings(IInspectable):
                        get_OpenPaneLength: _Callable
                        get_NegativeOpenPaneLength: _Callable
                        get_OpenPaneLengthMinusCompactLength: _Callable
                        get_NegativeOpenPaneLengthMinusCompactLength: _Callable
                        get_OpenPaneGridLength: _Callable
                        get_CompactPaneGridLength: _Callable

                    class IThumb(IInspectable):
                        get_IsDragging: _Callable
                        add_DragStarted: _Callable
                        remove_DragStarted: _Callable
                        add_DragDelta: _Callable
                        remove_DragDelta: _Callable
                        add_DragCompleted: _Callable
                        remove_DragCompleted: _Callable
                        CancelDrag: _Callable

                    class IThumbStatics(IInspectable):
                        get_IsDraggingProperty: _Callable

                    class ITickBar(IInspectable):
                        get_Fill: _Callable
                        put_Fill: _Callable

                    class ITickBarStatics(IInspectable):
                        get_FillProperty: _Callable

                    class IToggleButton(IInspectable):
                        get_IsChecked: _Callable
                        put_IsChecked: _Callable
                        get_IsThreeState: _Callable
                        put_IsThreeState: _Callable
                        add_Checked: _Callable
                        remove_Checked: _Callable
                        add_Unchecked: _Callable
                        remove_Unchecked: _Callable
                        add_Indeterminate: _Callable
                        remove_Indeterminate: _Callable

                    class IToggleButtonFactory(IInspectable):
                        CreateInstance: _Callable

                    class IToggleButtonOverrides(IInspectable):
                        OnToggle: _Callable

                    class IToggleButtonStatics(IInspectable):
                        get_IsCheckedProperty: _Callable
                        get_IsThreeStateProperty: _Callable

                    class IToggleSwitchTemplateSettings(IInspectable):
                        get_KnobCurrentToOnOffset: _Callable
                        get_KnobCurrentToOffOffset: _Callable
                        get_KnobOnToOffOffset: _Callable
                        get_KnobOffToOnOffset: _Callable
                        get_CurtainCurrentToOnOffset: _Callable
                        get_CurtainCurrentToOffOffset: _Callable
                        get_CurtainOnToOffOffset: _Callable
                        get_CurtainOffToOnOffset: _Callable

                    class IToolTipTemplateSettings(IInspectable):
                        get_FromHorizontalOffset: _Callable
                        get_FromVerticalOffset: _Callable

            class Input:
                class _IDoubleTappedEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IDoubleTappedRoutedEventArgs],
                                      _type.HRESULT]

                class IDoubleTappedEventHandler(_IDoubleTappedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IDoubleTappedEventHandler_impl(_IDoubleTappedEventHandler, IUnknown_impl):
                    pass

                class _IHoldingEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IHoldingRoutedEventArgs],
                                      _type.HRESULT]

                class IHoldingEventHandler(_IHoldingEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IHoldingEventHandler_impl(_IHoldingEventHandler, IUnknown_impl):
                    pass

                class _IKeyEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IKeyRoutedEventArgs],
                                      _type.HRESULT]

                class IKeyEventHandler(_IKeyEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IKeyEventHandler_impl(_IKeyEventHandler, IUnknown_impl):
                    pass

                class _IManipulationCompletedEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IManipulationCompletedRoutedEventArgs],
                                      _type.HRESULT]

                class IManipulationCompletedEventHandler(_IManipulationCompletedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IManipulationCompletedEventHandler_impl(_IManipulationCompletedEventHandler, IUnknown_impl):
                    pass

                class _IManipulationDeltaEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IManipulationDeltaRoutedEventArgs],
                                      _type.HRESULT]

                class IManipulationDeltaEventHandler(_IManipulationDeltaEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IManipulationDeltaEventHandler_impl(_IManipulationDeltaEventHandler, IUnknown_impl):
                    pass

                class _IManipulationInertiaStartingEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IManipulationInertiaStartingRoutedEventArgs],
                                      _type.HRESULT]

                class IManipulationInertiaStartingEventHandler(_IManipulationInertiaStartingEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IManipulationInertiaStartingEventHandler_impl(_IManipulationInertiaStartingEventHandler, IUnknown_impl):
                    pass

                class _IManipulationStartedEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IManipulationStartedRoutedEventArgs],
                                      _type.HRESULT]

                class IManipulationStartedEventHandler(_IManipulationStartedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IManipulationStartedEventHandler_impl(_IManipulationStartedEventHandler, IUnknown_impl):
                    pass

                class _IManipulationStartingEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IManipulationStartingRoutedEventArgs],
                                      _type.HRESULT]

                class IManipulationStartingEventHandler(_IManipulationStartingEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IManipulationStartingEventHandler_impl(_IManipulationStartingEventHandler, IUnknown_impl):
                    pass

                class _IPointerEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IPointerRoutedEventArgs],
                                      _type.HRESULT]

                class IPointerEventHandler(_IPointerEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IPointerEventHandler_impl(_IPointerEventHandler, IUnknown_impl):
                    pass

                class _IRightTappedEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.IRightTappedRoutedEventArgs],
                                      _type.HRESULT]

                class IRightTappedEventHandler(_IRightTappedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IRightTappedEventHandler_impl(_IRightTappedEventHandler, IUnknown_impl):
                    pass

                class _ITappedEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Input.ITappedRoutedEventArgs],
                                      _type.HRESULT]

                class ITappedEventHandler(_ITappedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ITappedEventHandler_impl(_ITappedEventHandler, IUnknown_impl):
                    pass

                class IAccessKeyDisplayDismissedEventArgs(IInspectable):
                    pass

                class IAccessKeyDisplayRequestedEventArgs(IInspectable):
                    get_PressedKeys: _Callable

                class IAccessKeyInvokedEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IAccessKeyManager(IInspectable):
                    pass

                class IAccessKeyManagerStatics(IInspectable):
                    get_IsDisplayModeEnabled: _Callable
                    add_IsDisplayModeEnabledChanged: _Callable
                    remove_IsDisplayModeEnabledChanged: _Callable
                    ExitDisplayMode: _Callable

                class IAccessKeyManagerStatics2(IInspectable):
                    get_AreKeyTipsEnabled: _Callable
                    put_AreKeyTipsEnabled: _Callable

                class ICanExecuteRequestedEventArgs(IInspectable):
                    get_Parameter: _Callable
                    get_CanExecute: _Callable
                    put_CanExecute: _Callable

                class ICharacterReceivedRoutedEventArgs(IInspectable):
                    get_Character: _Callable
                    get_KeyStatus: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable

                class ICommand(IInspectable):
                    add_CanExecuteChanged: _Callable[[Windows.Foundation.IEventHandler_impl[IInspectable],
                                                      _Pointer[_struct.EventRegistrationToken]],
                                                     _type.HRESULT]
                    remove_CanExecuteChanged: _Callable[[_struct.EventRegistrationToken],
                                                        _type.HRESULT]
                    CanExecute: _Callable[[IInspectable,
                                           _Pointer[_type.boolean]],
                                          _type.HRESULT]
                    Execute: _Callable[[IInspectable],
                                       _type.HRESULT]

                class IContextRequestedEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable
                    TryGetPosition: _Callable

                class IDoubleTappedRoutedEventArgs(IInspectable):
                    get_PointerDeviceType: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    GetPosition: _Callable

                class IExecuteRequestedEventArgs(IInspectable):
                    get_Parameter: _Callable

                class IFindNextElementOptions(IInspectable):
                    get_SearchRoot: _Callable
                    put_SearchRoot: _Callable
                    get_ExclusionRect: _Callable
                    put_ExclusionRect: _Callable
                    get_HintRect: _Callable
                    put_HintRect: _Callable
                    get_XYFocusNavigationStrategyOverride: _Callable
                    put_XYFocusNavigationStrategyOverride: _Callable

                class IFocusManager(IInspectable):
                    pass

                class IFocusManagerGotFocusEventArgs(IInspectable):
                    get_NewFocusedElement: _Callable
                    get_CorrelationId: _Callable

                class IFocusManagerLostFocusEventArgs(IInspectable):
                    get_OldFocusedElement: _Callable
                    get_CorrelationId: _Callable

                class IFocusManagerStatics(IInspectable):
                    GetFocusedElement: _Callable

                class IFocusManagerStatics2(IInspectable):
                    TryMoveFocus: _Callable

                class IFocusManagerStatics3(IInspectable):
                    FindNextFocusableElement: _Callable
                    FindNextFocusableElementWithHint: _Callable

                class IFocusManagerStatics4(IInspectable):
                    TryMoveFocusWithOptions: _Callable
                    FindNextElement: _Callable
                    FindFirstFocusableElement: _Callable
                    FindLastFocusableElement: _Callable
                    FindNextElementWithOptions: _Callable

                class IFocusManagerStatics5(IInspectable):
                    TryFocusAsync: _Callable
                    TryMoveFocusAsync: _Callable
                    TryMoveFocusWithOptionsAsync: _Callable

                class IFocusManagerStatics6(IInspectable):
                    add_GotFocus: _Callable
                    remove_GotFocus: _Callable
                    add_LostFocus: _Callable
                    remove_LostFocus: _Callable
                    add_GettingFocus: _Callable
                    remove_GettingFocus: _Callable
                    add_LosingFocus: _Callable
                    remove_LosingFocus: _Callable

                class IFocusManagerStatics7(IInspectable):
                    GetFocusedElement: _Callable

                class IFocusMovementResult(IInspectable):
                    get_Succeeded: _Callable

                class IGettingFocusEventArgs(IInspectable):
                    get_OldFocusedElement: _Callable
                    get_NewFocusedElement: _Callable
                    put_NewFocusedElement: _Callable
                    get_FocusState: _Callable
                    get_Direction: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_InputDevice: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class IGettingFocusEventArgs2(IInspectable):
                    TryCancel: _Callable
                    TrySetNewFocusedElement: _Callable

                class IGettingFocusEventArgs3(IInspectable):
                    get_CorrelationId: _Callable

                class IHoldingRoutedEventArgs(IInspectable):
                    get_PointerDeviceType: _Callable
                    get_HoldingState: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    GetPosition: _Callable

                class IInertiaExpansionBehavior(IInspectable):
                    get_DesiredDeceleration: _Callable
                    put_DesiredDeceleration: _Callable
                    get_DesiredExpansion: _Callable
                    put_DesiredExpansion: _Callable

                class IInertiaRotationBehavior(IInspectable):
                    get_DesiredDeceleration: _Callable
                    put_DesiredDeceleration: _Callable
                    get_DesiredRotation: _Callable
                    put_DesiredRotation: _Callable

                class IInertiaTranslationBehavior(IInspectable):
                    get_DesiredDeceleration: _Callable
                    put_DesiredDeceleration: _Callable
                    get_DesiredDisplacement: _Callable
                    put_DesiredDisplacement: _Callable

                class IInputScope(IInspectable):
                    get_Names: _Callable

                class IInputScopeName(IInspectable):
                    get_NameValue: _Callable
                    put_NameValue: _Callable

                class IInputScopeNameFactory(IInspectable):
                    CreateInstance: _Callable

                class IKeyRoutedEventArgs(IInspectable):
                    get_Key: _Callable
                    get_KeyStatus: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IKeyRoutedEventArgs2(IInspectable):
                    get_OriginalKey: _Callable

                class IKeyRoutedEventArgs3(IInspectable):
                    get_DeviceId: _Callable

                class IKeyboardAccelerator(IInspectable):
                    get_Key: _Callable
                    put_Key: _Callable
                    get_Modifiers: _Callable
                    put_Modifiers: _Callable
                    get_IsEnabled: _Callable
                    put_IsEnabled: _Callable
                    get_ScopeOwner: _Callable
                    put_ScopeOwner: _Callable
                    add_Invoked: _Callable
                    remove_Invoked: _Callable

                class IKeyboardAcceleratorFactory(IInspectable):
                    CreateInstance: _Callable

                class IKeyboardAcceleratorInvokedEventArgs(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_Element: _Callable

                class IKeyboardAcceleratorInvokedEventArgs2(IInspectable):
                    get_KeyboardAccelerator: _Callable

                class IKeyboardAcceleratorStatics(IInspectable):
                    get_KeyProperty: _Callable
                    get_ModifiersProperty: _Callable
                    get_IsEnabledProperty: _Callable
                    get_ScopeOwnerProperty: _Callable

                class ILosingFocusEventArgs(IInspectable):
                    get_OldFocusedElement: _Callable
                    get_NewFocusedElement: _Callable
                    put_NewFocusedElement: _Callable
                    get_FocusState: _Callable
                    get_Direction: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_InputDevice: _Callable
                    get_Cancel: _Callable
                    put_Cancel: _Callable

                class ILosingFocusEventArgs2(IInspectable):
                    TryCancel: _Callable
                    TrySetNewFocusedElement: _Callable

                class ILosingFocusEventArgs3(IInspectable):
                    get_CorrelationId: _Callable

                class IManipulationCompletedRoutedEventArgs(IInspectable):
                    get_Container: _Callable
                    get_Position: _Callable
                    get_IsInertial: _Callable
                    get_Cumulative: _Callable
                    get_Velocities: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_PointerDeviceType: _Callable

                class IManipulationDeltaRoutedEventArgs(IInspectable):
                    get_Container: _Callable
                    get_Position: _Callable
                    get_IsInertial: _Callable
                    get_Delta: _Callable
                    get_Cumulative: _Callable
                    get_Velocities: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_PointerDeviceType: _Callable
                    Complete: _Callable

                class IManipulationInertiaStartingRoutedEventArgs(IInspectable):
                    get_Container: _Callable
                    get_ExpansionBehavior: _Callable
                    put_ExpansionBehavior: _Callable
                    get_RotationBehavior: _Callable
                    put_RotationBehavior: _Callable
                    get_TranslationBehavior: _Callable
                    put_TranslationBehavior: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_PointerDeviceType: _Callable
                    get_Delta: _Callable
                    get_Cumulative: _Callable
                    get_Velocities: _Callable

                class IManipulationPivot(IInspectable):
                    get_Center: _Callable
                    put_Center: _Callable
                    get_Radius: _Callable
                    put_Radius: _Callable

                class IManipulationPivotFactory(IInspectable):
                    CreateInstanceWithCenterAndRadius: _Callable

                class IManipulationStartedRoutedEventArgs(IInspectable):
                    get_Container: _Callable
                    get_Position: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_PointerDeviceType: _Callable
                    get_Cumulative: _Callable
                    Complete: _Callable

                class IManipulationStartedRoutedEventArgsFactory(IInspectable):
                    CreateInstance: _Callable

                class IManipulationStartingRoutedEventArgs(IInspectable):
                    get_Mode: _Callable
                    put_Mode: _Callable
                    get_Container: _Callable
                    put_Container: _Callable
                    get_Pivot: _Callable
                    put_Pivot: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable

                class INoFocusCandidateFoundEventArgs(IInspectable):
                    get_Direction: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    get_InputDevice: _Callable

                class IPointer(IInspectable):
                    get_PointerId: _Callable
                    get_PointerDeviceType: _Callable
                    get_IsInContact: _Callable
                    get_IsInRange: _Callable

                class IPointerRoutedEventArgs(IInspectable):
                    get_Pointer: _Callable
                    get_KeyModifiers: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    GetCurrentPoint: _Callable
                    GetIntermediatePoints: _Callable

                class IPointerRoutedEventArgs2(IInspectable):
                    get_IsGenerated: _Callable

                class IProcessKeyboardAcceleratorEventArgs(IInspectable):
                    get_Key: _Callable
                    get_Modifiers: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IRightTappedRoutedEventArgs(IInspectable):
                    get_PointerDeviceType: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    GetPosition: _Callable

                class IStandardUICommand(IInspectable):
                    get_Kind: _Callable

                class IStandardUICommand2(IInspectable):
                    put_Kind: _Callable

                class IStandardUICommandFactory(IInspectable):
                    CreateInstance: _Callable
                    CreateInstanceWithKind: _Callable

                class IStandardUICommandStatics(IInspectable):
                    get_KindProperty: _Callable

                class ITappedRoutedEventArgs(IInspectable):
                    get_PointerDeviceType: _Callable
                    get_Handled: _Callable
                    put_Handled: _Callable
                    GetPosition: _Callable

                class IXamlUICommand(IInspectable):
                    get_Label: _Callable
                    put_Label: _Callable
                    get_IconSource: _Callable
                    put_IconSource: _Callable
                    get_KeyboardAccelerators: _Callable
                    get_AccessKey: _Callable
                    put_AccessKey: _Callable
                    get_Description: _Callable
                    put_Description: _Callable
                    get_Command: _Callable
                    put_Command: _Callable
                    add_ExecuteRequested: _Callable
                    remove_ExecuteRequested: _Callable
                    add_CanExecuteRequested: _Callable
                    remove_CanExecuteRequested: _Callable
                    NotifyCanExecuteChanged: _Callable

                class IXamlUICommandFactory(IInspectable):
                    CreateInstance: _Callable

                class IXamlUICommandStatics(IInspectable):
                    get_LabelProperty: _Callable
                    get_IconSourceProperty: _Callable
                    get_KeyboardAcceleratorsProperty: _Callable
                    get_AccessKeyProperty: _Callable
                    get_DescriptionProperty: _Callable
                    get_CommandProperty: _Callable

            class Hosting:
                class IDesignerAppExitedEventArgs(IInspectable):
                    get_ExitCode: _Callable

                class IDesignerAppManager(IInspectable):
                    get_AppUserModelId: _Callable
                    add_DesignerAppExited: _Callable
                    remove_DesignerAppExited: _Callable
                    CreateNewViewAsync: _Callable
                    LoadObjectIntoAppAsync: _Callable

                class IDesignerAppManagerFactory(IInspectable):
                    Create: _Callable

                class IDesignerAppView(IInspectable):
                    get_ApplicationViewId: _Callable
                    get_AppUserModelId: _Callable
                    get_ViewState: _Callable
                    get_ViewSize: _Callable
                    UpdateViewAsync: _Callable

                class IDesktopWindowXamlSource(IInspectable):
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
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource]],
                                              _type.HRESULT]

                class IDesktopWindowXamlSourceGotFocusEventArgs(IInspectable):
                    get_Request: _Callable

                class IDesktopWindowXamlSourceTakeFocusRequestedEventArgs(IInspectable):
                    get_Request: _Callable[[_Pointer[Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest]],
                                           _type.HRESULT]

                class IElementCompositionPreview(IInspectable):
                    pass

                class IElementCompositionPreviewStatics(IInspectable):
                    GetElementVisual: _Callable
                    GetElementChildVisual: _Callable
                    SetElementChildVisual: _Callable
                    GetScrollViewerManipulationPropertySet: _Callable

                class IElementCompositionPreviewStatics2(IInspectable):
                    SetImplicitShowAnimation: _Callable
                    SetImplicitHideAnimation: _Callable
                    SetIsTranslationEnabled: _Callable
                    GetPointerPositionPropertySet: _Callable

                class IElementCompositionPreviewStatics3(IInspectable):
                    SetAppWindowContent: _Callable
                    GetAppWindowContent: _Callable

                class IWindowsXamlManager(IInspectable):
                    pass

                class IWindowsXamlManagerStatics(IInspectable):
                    InitializeForCurrentThread: _Callable[[_Pointer[Windows.UI.Xaml.Hosting.IWindowsXamlManager]],
                                                          _type.HRESULT]

                class IXamlSourceFocusNavigationRequest(IInspectable):
                    get_Reason: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Hosting.XamlSourceFocusNavigationReason]],
                                          _type.HRESULT]
                    get_HintRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],
                                            _type.HRESULT]
                    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],
                                                 _type.HRESULT]

                class IXamlSourceFocusNavigationRequestFactory(IInspectable):
                    CreateInstance: _Callable
                    CreateInstanceWithHintRect: _Callable
                    CreateInstanceWithHintRectAndCorrelationId: _Callable

                class IXamlSourceFocusNavigationResult(IInspectable):
                    get_WasFocusMoved: _Callable

                class IXamlSourceFocusNavigationResultFactory(IInspectable):
                    CreateInstance: _Callable

                class IXamlUIPresenter(IInspectable):
                    get_RootElement: _Callable
                    put_RootElement: _Callable
                    get_ThemeKey: _Callable
                    put_ThemeKey: _Callable
                    get_ThemeResourcesXaml: _Callable
                    put_ThemeResourcesXaml: _Callable
                    SetSize: _Callable
                    Render: _Callable
                    Present: _Callable

                class IXamlUIPresenterHost(IInspectable):
                    ResolveFileResource: _Callable

                class IXamlUIPresenterHost2(IInspectable):
                    GetGenericXamlFilePath: _Callable

                class IXamlUIPresenterHost3(IInspectable):
                    ResolveDictionaryResource: _Callable

                class IXamlUIPresenterStatics(IInspectable):
                    get_CompleteTimelinesAutomatically: _Callable
                    put_CompleteTimelinesAutomatically: _Callable
                    SetHost: _Callable
                    NotifyWindowSizeChanged: _Callable

                class IXamlUIPresenterStatics2(IInspectable):
                    GetFlyoutPlacementTargetInfo: _Callable
                    GetFlyoutPlacement: _Callable

            class Media:
                class _IRateChangedRoutedEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Media.IRateChangedRoutedEventArgs],
                                      _type.HRESULT]

                class IRateChangedRoutedEventHandler(_IRateChangedRoutedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IRateChangedRoutedEventHandler_impl(_IRateChangedRoutedEventHandler, IUnknown_impl):
                    pass

                class _ITimelineMarkerRoutedEventHandler:
                    Invoke: _Callable[[IInspectable,
                                       Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs],
                                      _type.HRESULT]

                class ITimelineMarkerRoutedEventHandler(_ITimelineMarkerRoutedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ITimelineMarkerRoutedEventHandler_impl(_ITimelineMarkerRoutedEventHandler, IUnknown_impl):
                    pass

                class IAcrylicBrush(IInspectable):
                    get_BackgroundSource: _Callable
                    put_BackgroundSource: _Callable
                    get_TintColor: _Callable
                    put_TintColor: _Callable
                    get_TintOpacity: _Callable
                    put_TintOpacity: _Callable
                    get_TintTransitionDuration: _Callable
                    put_TintTransitionDuration: _Callable
                    get_AlwaysUseFallback: _Callable
                    put_AlwaysUseFallback: _Callable

                class IAcrylicBrush2(IInspectable):
                    get_TintLuminosityOpacity: _Callable
                    put_TintLuminosityOpacity: _Callable

                class IAcrylicBrushFactory(IInspectable):
                    CreateInstance: _Callable

                class IAcrylicBrushStatics(IInspectable):
                    get_BackgroundSourceProperty: _Callable
                    get_TintColorProperty: _Callable
                    get_TintOpacityProperty: _Callable
                    get_TintTransitionDurationProperty: _Callable
                    get_AlwaysUseFallbackProperty: _Callable

                class IAcrylicBrushStatics2(IInspectable):
                    get_TintLuminosityOpacityProperty: _Callable

                class IArcSegment(IInspectable):
                    get_Point: _Callable
                    put_Point: _Callable
                    get_Size: _Callable
                    put_Size: _Callable
                    get_RotationAngle: _Callable
                    put_RotationAngle: _Callable
                    get_IsLargeArc: _Callable
                    put_IsLargeArc: _Callable
                    get_SweepDirection: _Callable
                    put_SweepDirection: _Callable

                class IArcSegmentStatics(IInspectable):
                    get_PointProperty: _Callable
                    get_SizeProperty: _Callable
                    get_RotationAngleProperty: _Callable
                    get_IsLargeArcProperty: _Callable
                    get_SweepDirectionProperty: _Callable

                class IBezierSegment(IInspectable):
                    get_Point1: _Callable
                    put_Point1: _Callable
                    get_Point2: _Callable
                    put_Point2: _Callable
                    get_Point3: _Callable
                    put_Point3: _Callable

                class IBezierSegmentStatics(IInspectable):
                    get_Point1Property: _Callable
                    get_Point2Property: _Callable
                    get_Point3Property: _Callable

                class IBitmapCache(IInspectable):
                    pass

                class IBrush(IInspectable):
                    get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],
                                           _type.HRESULT]
                    put_Opacity: _Callable[[_type.DOUBLE],
                                           _type.HRESULT]
                    get_Transform: _Callable
                    put_Transform: _Callable
                    get_RelativeTransform: _Callable
                    put_RelativeTransform: _Callable

                class IBrushFactory(IInspectable):
                    CreateInstance: _Callable

                class IBrushOverrides2(IInspectable):
                    PopulatePropertyInfoOverride: _Callable

                class IBrushStatics(IInspectable):
                    get_OpacityProperty: _Callable
                    get_TransformProperty: _Callable
                    get_RelativeTransformProperty: _Callable

                class ICacheMode(IInspectable):
                    pass

                class ICacheModeFactory(IInspectable):
                    CreateInstance: _Callable

                class ICompositeTransform(IInspectable):
                    get_CenterX: _Callable
                    put_CenterX: _Callable
                    get_CenterY: _Callable
                    put_CenterY: _Callable
                    get_ScaleX: _Callable
                    put_ScaleX: _Callable
                    get_ScaleY: _Callable
                    put_ScaleY: _Callable
                    get_SkewX: _Callable
                    put_SkewX: _Callable
                    get_SkewY: _Callable
                    put_SkewY: _Callable
                    get_Rotation: _Callable
                    put_Rotation: _Callable
                    get_TranslateX: _Callable
                    put_TranslateX: _Callable
                    get_TranslateY: _Callable
                    put_TranslateY: _Callable

                class ICompositeTransformStatics(IInspectable):
                    get_CenterXProperty: _Callable
                    get_CenterYProperty: _Callable
                    get_ScaleXProperty: _Callable
                    get_ScaleYProperty: _Callable
                    get_SkewXProperty: _Callable
                    get_SkewYProperty: _Callable
                    get_RotationProperty: _Callable
                    get_TranslateXProperty: _Callable
                    get_TranslateYProperty: _Callable

                class ICompositionTarget(IInspectable):
                    pass

                class ICompositionTargetStatics(IInspectable):
                    add_Rendering: _Callable
                    remove_Rendering: _Callable
                    add_SurfaceContentsLost: _Callable
                    remove_SurfaceContentsLost: _Callable

                class ICompositionTargetStatics3(IInspectable):
                    add_Rendered: _Callable
                    remove_Rendered: _Callable

                class IEllipseGeometry(IInspectable):
                    get_Center: _Callable
                    put_Center: _Callable
                    get_RadiusX: _Callable
                    put_RadiusX: _Callable
                    get_RadiusY: _Callable
                    put_RadiusY: _Callable

                class IEllipseGeometryStatics(IInspectable):
                    get_CenterProperty: _Callable
                    get_RadiusXProperty: _Callable
                    get_RadiusYProperty: _Callable

                class IFontFamily(IInspectable):
                    get_Source: _Callable

                class IFontFamilyFactory(IInspectable):
                    CreateInstanceWithName: _Callable

                class IFontFamilyStatics2(IInspectable):
                    get_XamlAutoFontFamily: _Callable

                class IGeneralTransform(IInspectable):
                    get_Inverse: _Callable
                    TransformPoint: _Callable
                    TryTransform: _Callable
                    TransformBounds: _Callable

                class IGeneralTransformFactory(IInspectable):
                    CreateInstance: _Callable

                class IGeneralTransformOverrides(IInspectable):
                    get_InverseCore: _Callable
                    TryTransformCore: _Callable
                    TransformBoundsCore: _Callable

                class IGeometry(IInspectable):
                    get_Transform: _Callable
                    put_Transform: _Callable
                    get_Bounds: _Callable

                class IGeometryFactory(IInspectable):
                    pass

                class IGeometryGroup(IInspectable):
                    get_FillRule: _Callable
                    put_FillRule: _Callable
                    get_Children: _Callable
                    put_Children: _Callable

                class IGeometryGroupStatics(IInspectable):
                    get_FillRuleProperty: _Callable
                    get_ChildrenProperty: _Callable

                class IGeometryStatics(IInspectable):
                    get_Empty: _Callable
                    get_StandardFlatteningTolerance: _Callable
                    get_TransformProperty: _Callable

                class IGradientBrush(IInspectable):
                    get_SpreadMethod: _Callable
                    put_SpreadMethod: _Callable
                    get_MappingMode: _Callable
                    put_MappingMode: _Callable
                    get_ColorInterpolationMode: _Callable
                    put_ColorInterpolationMode: _Callable
                    get_GradientStops: _Callable
                    put_GradientStops: _Callable

                class IGradientBrushFactory(IInspectable):
                    CreateInstance: _Callable

                class IGradientBrushStatics(IInspectable):
                    get_SpreadMethodProperty: _Callable
                    get_MappingModeProperty: _Callable
                    get_ColorInterpolationModeProperty: _Callable
                    get_GradientStopsProperty: _Callable

                class IGradientStop(IInspectable):
                    get_Color: _Callable
                    put_Color: _Callable
                    get_Offset: _Callable
                    put_Offset: _Callable

                class IGradientStopStatics(IInspectable):
                    get_ColorProperty: _Callable
                    get_OffsetProperty: _Callable

                class IImageBrush(IInspectable):
                    get_ImageSource: _Callable
                    put_ImageSource: _Callable
                    add_ImageFailed: _Callable
                    remove_ImageFailed: _Callable
                    add_ImageOpened: _Callable
                    remove_ImageOpened: _Callable

                class IImageBrushStatics(IInspectable):
                    get_ImageSourceProperty: _Callable

                class IImageSource(IInspectable):
                    pass

                class IImageSourceFactory(IInspectable):
                    pass

                class ILineGeometry(IInspectable):
                    get_StartPoint: _Callable
                    put_StartPoint: _Callable
                    get_EndPoint: _Callable
                    put_EndPoint: _Callable

                class ILineGeometryStatics(IInspectable):
                    get_StartPointProperty: _Callable
                    get_EndPointProperty: _Callable

                class ILineSegment(IInspectable):
                    get_Point: _Callable
                    put_Point: _Callable

                class ILineSegmentStatics(IInspectable):
                    get_PointProperty: _Callable

                class ILinearGradientBrush(IInspectable):
                    get_StartPoint: _Callable
                    put_StartPoint: _Callable
                    get_EndPoint: _Callable
                    put_EndPoint: _Callable

                class ILinearGradientBrushFactory(IInspectable):
                    CreateInstanceWithGradientStopCollectionAndAngle: _Callable

                class ILinearGradientBrushStatics(IInspectable):
                    get_StartPointProperty: _Callable
                    get_EndPointProperty: _Callable

                class ILoadedImageSourceLoadCompletedEventArgs(IInspectable):
                    get_Status: _Callable

                class ILoadedImageSurface(IInspectable):
                    get_DecodedPhysicalSize: _Callable
                    get_DecodedSize: _Callable
                    get_NaturalSize: _Callable
                    add_LoadCompleted: _Callable
                    remove_LoadCompleted: _Callable

                class ILoadedImageSurfaceStatics(IInspectable):
                    StartLoadFromUriWithSize: _Callable
                    StartLoadFromUri: _Callable
                    StartLoadFromStreamWithSize: _Callable
                    StartLoadFromStream: _Callable

                class IMatrix3DProjection(IInspectable):
                    get_ProjectionMatrix: _Callable
                    put_ProjectionMatrix: _Callable

                class IMatrix3DProjectionStatics(IInspectable):
                    get_ProjectionMatrixProperty: _Callable

                class IMatrixHelper(IInspectable):
                    pass

                class IMatrixHelperStatics(IInspectable):
                    get_Identity: _Callable
                    FromElements: _Callable
                    GetIsIdentity: _Callable
                    Transform: _Callable

                class IMatrixTransform(IInspectable):
                    get_Matrix: _Callable
                    put_Matrix: _Callable

                class IMatrixTransformStatics(IInspectable):
                    get_MatrixProperty: _Callable

                class IMediaTransportControlsThumbnailRequestedEventArgs(IInspectable):
                    SetThumbnailImage: _Callable
                    GetDeferral: _Callable

                class IPartialMediaFailureDetectedEventArgs(IInspectable):
                    get_StreamKind: _Callable

                class IPartialMediaFailureDetectedEventArgs2(IInspectable):
                    get_ExtendedError: _Callable

                class IPathFigure(IInspectable):
                    get_Segments: _Callable
                    put_Segments: _Callable
                    get_StartPoint: _Callable
                    put_StartPoint: _Callable
                    get_IsClosed: _Callable
                    put_IsClosed: _Callable
                    get_IsFilled: _Callable
                    put_IsFilled: _Callable

                class IPathFigureStatics(IInspectable):
                    get_SegmentsProperty: _Callable
                    get_StartPointProperty: _Callable
                    get_IsClosedProperty: _Callable
                    get_IsFilledProperty: _Callable

                class IPathGeometry(IInspectable):
                    get_FillRule: _Callable
                    put_FillRule: _Callable
                    get_Figures: _Callable
                    put_Figures: _Callable

                class IPathGeometryStatics(IInspectable):
                    get_FillRuleProperty: _Callable
                    get_FiguresProperty: _Callable

                class IPathSegment(IInspectable):
                    pass

                class IPathSegmentFactory(IInspectable):
                    pass

                class IPlaneProjection(IInspectable):
                    get_LocalOffsetX: _Callable
                    put_LocalOffsetX: _Callable
                    get_LocalOffsetY: _Callable
                    put_LocalOffsetY: _Callable
                    get_LocalOffsetZ: _Callable
                    put_LocalOffsetZ: _Callable
                    get_RotationX: _Callable
                    put_RotationX: _Callable
                    get_RotationY: _Callable
                    put_RotationY: _Callable
                    get_RotationZ: _Callable
                    put_RotationZ: _Callable
                    get_CenterOfRotationX: _Callable
                    put_CenterOfRotationX: _Callable
                    get_CenterOfRotationY: _Callable
                    put_CenterOfRotationY: _Callable
                    get_CenterOfRotationZ: _Callable
                    put_CenterOfRotationZ: _Callable
                    get_GlobalOffsetX: _Callable
                    put_GlobalOffsetX: _Callable
                    get_GlobalOffsetY: _Callable
                    put_GlobalOffsetY: _Callable
                    get_GlobalOffsetZ: _Callable
                    put_GlobalOffsetZ: _Callable
                    get_ProjectionMatrix: _Callable

                class IPlaneProjectionStatics(IInspectable):
                    get_LocalOffsetXProperty: _Callable
                    get_LocalOffsetYProperty: _Callable
                    get_LocalOffsetZProperty: _Callable
                    get_RotationXProperty: _Callable
                    get_RotationYProperty: _Callable
                    get_RotationZProperty: _Callable
                    get_CenterOfRotationXProperty: _Callable
                    get_CenterOfRotationYProperty: _Callable
                    get_CenterOfRotationZProperty: _Callable
                    get_GlobalOffsetXProperty: _Callable
                    get_GlobalOffsetYProperty: _Callable
                    get_GlobalOffsetZProperty: _Callable
                    get_ProjectionMatrixProperty: _Callable

                class IPolyBezierSegment(IInspectable):
                    get_Points: _Callable
                    put_Points: _Callable

                class IPolyBezierSegmentStatics(IInspectable):
                    get_PointsProperty: _Callable

                class IPolyLineSegment(IInspectable):
                    get_Points: _Callable
                    put_Points: _Callable

                class IPolyLineSegmentStatics(IInspectable):
                    get_PointsProperty: _Callable

                class IPolyQuadraticBezierSegment(IInspectable):
                    get_Points: _Callable
                    put_Points: _Callable

                class IPolyQuadraticBezierSegmentStatics(IInspectable):
                    get_PointsProperty: _Callable

                class IProjection(IInspectable):
                    pass

                class IProjectionFactory(IInspectable):
                    CreateInstance: _Callable

                class IQuadraticBezierSegment(IInspectable):
                    get_Point1: _Callable
                    put_Point1: _Callable
                    get_Point2: _Callable
                    put_Point2: _Callable

                class IQuadraticBezierSegmentStatics(IInspectable):
                    get_Point1Property: _Callable
                    get_Point2Property: _Callable

                class IRateChangedRoutedEventArgs(IInspectable):
                    pass

                class IRectangleGeometry(IInspectable):
                    get_Rect: _Callable
                    put_Rect: _Callable

                class IRectangleGeometryStatics(IInspectable):
                    get_RectProperty: _Callable

                class IRenderedEventArgs(IInspectable):
                    get_FrameDuration: _Callable

                class IRenderingEventArgs(IInspectable):
                    get_RenderingTime: _Callable

                class IRevealBackgroundBrush(IInspectable):
                    pass

                class IRevealBackgroundBrushFactory(IInspectable):
                    CreateInstance: _Callable

                class IRevealBorderBrush(IInspectable):
                    pass

                class IRevealBorderBrushFactory(IInspectable):
                    CreateInstance: _Callable

                class IRevealBrush(IInspectable):
                    get_Color: _Callable
                    put_Color: _Callable
                    get_TargetTheme: _Callable
                    put_TargetTheme: _Callable
                    get_AlwaysUseFallback: _Callable
                    put_AlwaysUseFallback: _Callable

                class IRevealBrushFactory(IInspectable):
                    CreateInstance: _Callable

                class IRevealBrushStatics(IInspectable):
                    get_ColorProperty: _Callable
                    get_TargetThemeProperty: _Callable
                    get_AlwaysUseFallbackProperty: _Callable
                    get_StateProperty: _Callable
                    SetState: _Callable
                    GetState: _Callable

                class IRotateTransform(IInspectable):
                    get_CenterX: _Callable
                    put_CenterX: _Callable
                    get_CenterY: _Callable
                    put_CenterY: _Callable
                    get_Angle: _Callable
                    put_Angle: _Callable

                class IRotateTransformStatics(IInspectable):
                    get_CenterXProperty: _Callable
                    get_CenterYProperty: _Callable
                    get_AngleProperty: _Callable

                class IScaleTransform(IInspectable):
                    get_CenterX: _Callable
                    put_CenterX: _Callable
                    get_CenterY: _Callable
                    put_CenterY: _Callable
                    get_ScaleX: _Callable
                    put_ScaleX: _Callable
                    get_ScaleY: _Callable
                    put_ScaleY: _Callable

                class IScaleTransformStatics(IInspectable):
                    get_CenterXProperty: _Callable
                    get_CenterYProperty: _Callable
                    get_ScaleXProperty: _Callable
                    get_ScaleYProperty: _Callable

                class IShadow(IInspectable):
                    pass

                class IShadowFactory(IInspectable):
                    pass

                class ISkewTransform(IInspectable):
                    get_CenterX: _Callable
                    put_CenterX: _Callable
                    get_CenterY: _Callable
                    put_CenterY: _Callable
                    get_AngleX: _Callable
                    put_AngleX: _Callable
                    get_AngleY: _Callable
                    put_AngleY: _Callable

                class ISkewTransformStatics(IInspectable):
                    get_CenterXProperty: _Callable
                    get_CenterYProperty: _Callable
                    get_AngleXProperty: _Callable
                    get_AngleYProperty: _Callable

                class ISolidColorBrush(IInspectable):
                    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
                    put_Color: _Callable[[_struct.Windows.UI.Color],
                                         _type.HRESULT]

                class ISolidColorBrushFactory(IInspectable):
                    CreateInstanceWithColor: _Callable[[_struct.Windows.UI.Color,
                                                        _Pointer[Windows.UI.Xaml.Media.ISolidColorBrush]],
                                                       _type.HRESULT]

                class ISolidColorBrushStatics(IInspectable):
                    get_ColorProperty: _Callable

                class IThemeShadow(IInspectable):
                    get_Receivers: _Callable

                class IThemeShadowFactory(IInspectable):
                    CreateInstance: _Callable

                class ITileBrush(IInspectable):
                    get_AlignmentX: _Callable
                    put_AlignmentX: _Callable
                    get_AlignmentY: _Callable
                    put_AlignmentY: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable

                class ITileBrushFactory(IInspectable):
                    CreateInstance: _Callable

                class ITileBrushStatics(IInspectable):
                    get_AlignmentXProperty: _Callable
                    get_AlignmentYProperty: _Callable
                    get_StretchProperty: _Callable

                class ITimelineMarker(IInspectable):
                    get_Time: _Callable
                    put_Time: _Callable
                    get_Type: _Callable
                    put_Type: _Callable
                    get_Text: _Callable
                    put_Text: _Callable

                class ITimelineMarkerRoutedEventArgs(IInspectable):
                    get_Marker: _Callable
                    put_Marker: _Callable

                class ITimelineMarkerStatics(IInspectable):
                    get_TimeProperty: _Callable
                    get_TypeProperty: _Callable
                    get_TextProperty: _Callable

                class ITransform(IInspectable):
                    pass

                class ITransformFactory(IInspectable):
                    pass

                class ITransformGroup(IInspectable):
                    get_Children: _Callable
                    put_Children: _Callable
                    get_Value: _Callable

                class ITransformGroupStatics(IInspectable):
                    get_ChildrenProperty: _Callable

                class ITranslateTransform(IInspectable):
                    get_X: _Callable
                    put_X: _Callable
                    get_Y: _Callable
                    put_Y: _Callable

                class ITranslateTransformStatics(IInspectable):
                    get_XProperty: _Callable
                    get_YProperty: _Callable

                class IVisualTreeHelper(IInspectable):
                    pass

                class IVisualTreeHelperStatics(IInspectable):
                    FindElementsInHostCoordinatesPoint: _Callable
                    FindElementsInHostCoordinatesRect: _Callable
                    FindAllElementsInHostCoordinatesPoint: _Callable
                    FindAllElementsInHostCoordinatesRect: _Callable
                    GetChild: _Callable
                    GetChildrenCount: _Callable
                    GetParent: _Callable
                    DisconnectChildrenRecursive: _Callable

                class IVisualTreeHelperStatics2(IInspectable):
                    GetOpenPopups: _Callable

                class IVisualTreeHelperStatics3(IInspectable):
                    GetOpenPopupsForXamlRoot: _Callable

                class IXamlCompositionBrushBase(IInspectable):
                    get_FallbackColor: _Callable
                    put_FallbackColor: _Callable

                class IXamlCompositionBrushBaseFactory(IInspectable):
                    CreateInstance: _Callable

                class IXamlCompositionBrushBaseOverrides(IInspectable):
                    OnConnected: _Callable
                    OnDisconnected: _Callable

                class IXamlCompositionBrushBaseProtected(IInspectable):
                    get_CompositionBrush: _Callable
                    put_CompositionBrush: _Callable

                class IXamlCompositionBrushBaseStatics(IInspectable):
                    get_FallbackColorProperty: _Callable

                class IXamlLight(IInspectable):
                    pass

                class IXamlLightFactory(IInspectable):
                    CreateInstance: _Callable

                class IXamlLightOverrides(IInspectable):
                    GetId: _Callable
                    OnConnected: _Callable
                    OnDisconnected: _Callable

                class IXamlLightProtected(IInspectable):
                    get_CompositionLight: _Callable
                    put_CompositionLight: _Callable

                class IXamlLightStatics(IInspectable):
                    AddTargetElement: _Callable
                    RemoveTargetElement: _Callable
                    AddTargetBrush: _Callable
                    RemoveTargetBrush: _Callable

                class Animation:
                    class IAddDeleteThemeTransition(IInspectable):
                        pass

                    class IBackEase(IInspectable):
                        get_Amplitude: _Callable
                        put_Amplitude: _Callable

                    class IBackEaseStatics(IInspectable):
                        get_AmplitudeProperty: _Callable

                    class IBasicConnectedAnimationConfiguration(IInspectable):
                        pass

                    class IBasicConnectedAnimationConfigurationFactory(IInspectable):
                        CreateInstance: _Callable

                    class IBeginStoryboard(IInspectable):
                        get_Storyboard: _Callable
                        put_Storyboard: _Callable

                    class IBeginStoryboardStatics(IInspectable):
                        get_StoryboardProperty: _Callable

                    class IBounceEase(IInspectable):
                        get_Bounces: _Callable
                        put_Bounces: _Callable
                        get_Bounciness: _Callable
                        put_Bounciness: _Callable

                    class IBounceEaseStatics(IInspectable):
                        get_BouncesProperty: _Callable
                        get_BouncinessProperty: _Callable

                    class ICircleEase(IInspectable):
                        pass

                    class IColorAnimation(IInspectable):
                        get_From: _Callable
                        put_From: _Callable
                        get_To: _Callable
                        put_To: _Callable
                        get_By: _Callable
                        put_By: _Callable
                        get_EasingFunction: _Callable
                        put_EasingFunction: _Callable
                        get_EnableDependentAnimation: _Callable
                        put_EnableDependentAnimation: _Callable

                    class IColorAnimationStatics(IInspectable):
                        get_FromProperty: _Callable
                        get_ToProperty: _Callable
                        get_ByProperty: _Callable
                        get_EasingFunctionProperty: _Callable
                        get_EnableDependentAnimationProperty: _Callable

                    class IColorAnimationUsingKeyFrames(IInspectable):
                        get_KeyFrames: _Callable
                        get_EnableDependentAnimation: _Callable
                        put_EnableDependentAnimation: _Callable

                    class IColorAnimationUsingKeyFramesStatics(IInspectable):
                        get_EnableDependentAnimationProperty: _Callable

                    class IColorKeyFrame(IInspectable):
                        get_Value: _Callable
                        put_Value: _Callable
                        get_KeyTime: _Callable
                        put_KeyTime: _Callable

                    class IColorKeyFrameFactory(IInspectable):
                        CreateInstance: _Callable

                    class IColorKeyFrameStatics(IInspectable):
                        get_ValueProperty: _Callable
                        get_KeyTimeProperty: _Callable

                    class ICommonNavigationTransitionInfo(IInspectable):
                        get_IsStaggeringEnabled: _Callable
                        put_IsStaggeringEnabled: _Callable

                    class ICommonNavigationTransitionInfoStatics(IInspectable):
                        get_IsStaggeringEnabledProperty: _Callable
                        get_IsStaggerElementProperty: _Callable
                        GetIsStaggerElement: _Callable
                        SetIsStaggerElement: _Callable

                    class IConnectedAnimation(IInspectable):
                        add_Completed: _Callable
                        remove_Completed: _Callable
                        TryStart: _Callable
                        Cancel: _Callable

                    class IConnectedAnimation2(IInspectable):
                        get_IsScaleAnimationEnabled: _Callable
                        put_IsScaleAnimationEnabled: _Callable
                        TryStartWithCoordinatedElements: _Callable
                        SetAnimationComponent: _Callable

                    class IConnectedAnimation3(IInspectable):
                        get_Configuration: _Callable
                        put_Configuration: _Callable

                    class IConnectedAnimationConfiguration(IInspectable):
                        pass

                    class IConnectedAnimationConfigurationFactory(IInspectable):
                        pass

                    class IConnectedAnimationService(IInspectable):
                        get_DefaultDuration: _Callable
                        put_DefaultDuration: _Callable
                        get_DefaultEasingFunction: _Callable
                        put_DefaultEasingFunction: _Callable
                        PrepareToAnimate: _Callable
                        GetAnimation: _Callable

                    class IConnectedAnimationServiceStatics(IInspectable):
                        GetForCurrentView: _Callable

                    class IContentThemeTransition(IInspectable):
                        get_HorizontalOffset: _Callable
                        put_HorizontalOffset: _Callable
                        get_VerticalOffset: _Callable
                        put_VerticalOffset: _Callable

                    class IContentThemeTransitionStatics(IInspectable):
                        get_HorizontalOffsetProperty: _Callable
                        get_VerticalOffsetProperty: _Callable

                    class IContinuumNavigationTransitionInfo(IInspectable):
                        get_ExitElement: _Callable
                        put_ExitElement: _Callable

                    class IContinuumNavigationTransitionInfoStatics(IInspectable):
                        get_ExitElementProperty: _Callable
                        get_IsEntranceElementProperty: _Callable
                        GetIsEntranceElement: _Callable
                        SetIsEntranceElement: _Callable
                        get_IsExitElementProperty: _Callable
                        GetIsExitElement: _Callable
                        SetIsExitElement: _Callable
                        get_ExitElementContainerProperty: _Callable
                        GetExitElementContainer: _Callable
                        SetExitElementContainer: _Callable

                    class ICubicEase(IInspectable):
                        pass

                    class IDirectConnectedAnimationConfiguration(IInspectable):
                        pass

                    class IDirectConnectedAnimationConfigurationFactory(IInspectable):
                        CreateInstance: _Callable

                    class IDiscreteColorKeyFrame(IInspectable):
                        pass

                    class IDiscreteDoubleKeyFrame(IInspectable):
                        pass

                    class IDiscreteObjectKeyFrame(IInspectable):
                        pass

                    class IDiscretePointKeyFrame(IInspectable):
                        pass

                    class IDoubleAnimation(IInspectable):
                        get_From: _Callable
                        put_From: _Callable
                        get_To: _Callable
                        put_To: _Callable
                        get_By: _Callable
                        put_By: _Callable
                        get_EasingFunction: _Callable
                        put_EasingFunction: _Callable
                        get_EnableDependentAnimation: _Callable
                        put_EnableDependentAnimation: _Callable

                    class IDoubleAnimationStatics(IInspectable):
                        get_FromProperty: _Callable
                        get_ToProperty: _Callable
                        get_ByProperty: _Callable
                        get_EasingFunctionProperty: _Callable
                        get_EnableDependentAnimationProperty: _Callable

                    class IDoubleAnimationUsingKeyFrames(IInspectable):
                        get_KeyFrames: _Callable
                        get_EnableDependentAnimation: _Callable
                        put_EnableDependentAnimation: _Callable

                    class IDoubleAnimationUsingKeyFramesStatics(IInspectable):
                        get_EnableDependentAnimationProperty: _Callable

                    class IDoubleKeyFrame(IInspectable):
                        get_Value: _Callable
                        put_Value: _Callable
                        get_KeyTime: _Callable
                        put_KeyTime: _Callable

                    class IDoubleKeyFrameFactory(IInspectable):
                        CreateInstance: _Callable

                    class IDoubleKeyFrameStatics(IInspectable):
                        get_ValueProperty: _Callable
                        get_KeyTimeProperty: _Callable

                    class IDragItemThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable

                    class IDragItemThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable

                    class IDragOverThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable
                        get_ToOffset: _Callable
                        put_ToOffset: _Callable
                        get_Direction: _Callable
                        put_Direction: _Callable

                    class IDragOverThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable
                        get_ToOffsetProperty: _Callable
                        get_DirectionProperty: _Callable

                    class IDrillInNavigationTransitionInfo(IInspectable):
                        pass

                    class IDrillInThemeAnimation(IInspectable):
                        get_EntranceTargetName: _Callable
                        put_EntranceTargetName: _Callable
                        get_EntranceTarget: _Callable
                        put_EntranceTarget: _Callable
                        get_ExitTargetName: _Callable
                        put_ExitTargetName: _Callable
                        get_ExitTarget: _Callable
                        put_ExitTarget: _Callable

                    class IDrillInThemeAnimationStatics(IInspectable):
                        get_EntranceTargetNameProperty: _Callable
                        get_EntranceTargetProperty: _Callable
                        get_ExitTargetNameProperty: _Callable
                        get_ExitTargetProperty: _Callable

                    class IDrillOutThemeAnimation(IInspectable):
                        get_EntranceTargetName: _Callable
                        put_EntranceTargetName: _Callable
                        get_EntranceTarget: _Callable
                        put_EntranceTarget: _Callable
                        get_ExitTargetName: _Callable
                        put_ExitTargetName: _Callable
                        get_ExitTarget: _Callable
                        put_ExitTarget: _Callable

                    class IDrillOutThemeAnimationStatics(IInspectable):
                        get_EntranceTargetNameProperty: _Callable
                        get_EntranceTargetProperty: _Callable
                        get_ExitTargetNameProperty: _Callable
                        get_ExitTargetProperty: _Callable

                    class IDropTargetItemThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable

                    class IDropTargetItemThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable

                    class IEasingColorKeyFrame(IInspectable):
                        get_EasingFunction: _Callable
                        put_EasingFunction: _Callable

                    class IEasingColorKeyFrameStatics(IInspectable):
                        get_EasingFunctionProperty: _Callable

                    class IEasingDoubleKeyFrame(IInspectable):
                        get_EasingFunction: _Callable
                        put_EasingFunction: _Callable

                    class IEasingDoubleKeyFrameStatics(IInspectable):
                        get_EasingFunctionProperty: _Callable

                    class IEasingFunctionBase(IInspectable):
                        get_EasingMode: _Callable
                        put_EasingMode: _Callable
                        Ease: _Callable

                    class IEasingFunctionBaseFactory(IInspectable):
                        pass

                    class IEasingFunctionBaseStatics(IInspectable):
                        get_EasingModeProperty: _Callable

                    class IEasingPointKeyFrame(IInspectable):
                        get_EasingFunction: _Callable
                        put_EasingFunction: _Callable

                    class IEasingPointKeyFrameStatics(IInspectable):
                        get_EasingFunctionProperty: _Callable

                    class IEdgeUIThemeTransition(IInspectable):
                        get_Edge: _Callable
                        put_Edge: _Callable

                    class IEdgeUIThemeTransitionStatics(IInspectable):
                        get_EdgeProperty: _Callable

                    class IElasticEase(IInspectable):
                        get_Oscillations: _Callable
                        put_Oscillations: _Callable
                        get_Springiness: _Callable
                        put_Springiness: _Callable

                    class IElasticEaseStatics(IInspectable):
                        get_OscillationsProperty: _Callable
                        get_SpringinessProperty: _Callable

                    class IEntranceNavigationTransitionInfo(IInspectable):
                        pass

                    class IEntranceNavigationTransitionInfoStatics(IInspectable):
                        get_IsTargetElementProperty: _Callable
                        GetIsTargetElement: _Callable
                        SetIsTargetElement: _Callable

                    class IEntranceThemeTransition(IInspectable):
                        get_FromHorizontalOffset: _Callable
                        put_FromHorizontalOffset: _Callable
                        get_FromVerticalOffset: _Callable
                        put_FromVerticalOffset: _Callable
                        get_IsStaggeringEnabled: _Callable
                        put_IsStaggeringEnabled: _Callable

                    class IEntranceThemeTransitionStatics(IInspectable):
                        get_FromHorizontalOffsetProperty: _Callable
                        get_FromVerticalOffsetProperty: _Callable
                        get_IsStaggeringEnabledProperty: _Callable

                    class IExponentialEase(IInspectable):
                        get_Exponent: _Callable
                        put_Exponent: _Callable

                    class IExponentialEaseStatics(IInspectable):
                        get_ExponentProperty: _Callable

                    class IFadeInThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable

                    class IFadeInThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable

                    class IFadeOutThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable

                    class IFadeOutThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable

                    class IGravityConnectedAnimationConfiguration(IInspectable):
                        pass

                    class IGravityConnectedAnimationConfiguration2(IInspectable):
                        get_IsShadowEnabled: _Callable
                        put_IsShadowEnabled: _Callable

                    class IGravityConnectedAnimationConfigurationFactory(IInspectable):
                        CreateInstance: _Callable

                    class IKeySpline(IInspectable):
                        get_ControlPoint1: _Callable
                        put_ControlPoint1: _Callable
                        get_ControlPoint2: _Callable
                        put_ControlPoint2: _Callable

                    class IKeyTimeHelper(IInspectable):
                        pass

                    class IKeyTimeHelperStatics(IInspectable):
                        FromTimeSpan: _Callable

                    class ILinearColorKeyFrame(IInspectable):
                        pass

                    class ILinearDoubleKeyFrame(IInspectable):
                        pass

                    class ILinearPointKeyFrame(IInspectable):
                        pass

                    class INavigationThemeTransition(IInspectable):
                        get_DefaultNavigationTransitionInfo: _Callable
                        put_DefaultNavigationTransitionInfo: _Callable

                    class INavigationThemeTransitionStatics(IInspectable):
                        get_DefaultNavigationTransitionInfoProperty: _Callable

                    class INavigationTransitionInfo(IInspectable):
                        pass

                    class INavigationTransitionInfoFactory(IInspectable):
                        CreateInstance: _Callable

                    class INavigationTransitionInfoOverrides(IInspectable):
                        GetNavigationStateCore: _Callable
                        SetNavigationStateCore: _Callable

                    class IObjectAnimationUsingKeyFrames(IInspectable):
                        get_KeyFrames: _Callable
                        get_EnableDependentAnimation: _Callable
                        put_EnableDependentAnimation: _Callable

                    class IObjectAnimationUsingKeyFramesStatics(IInspectable):
                        get_EnableDependentAnimationProperty: _Callable

                    class IObjectKeyFrame(IInspectable):
                        get_Value: _Callable
                        put_Value: _Callable
                        get_KeyTime: _Callable
                        put_KeyTime: _Callable

                    class IObjectKeyFrameFactory(IInspectable):
                        CreateInstance: _Callable

                    class IObjectKeyFrameStatics(IInspectable):
                        get_ValueProperty: _Callable
                        get_KeyTimeProperty: _Callable

                    class IPaneThemeTransition(IInspectable):
                        get_Edge: _Callable
                        put_Edge: _Callable

                    class IPaneThemeTransitionStatics(IInspectable):
                        get_EdgeProperty: _Callable

                    class IPointAnimation(IInspectable):
                        get_From: _Callable
                        put_From: _Callable
                        get_To: _Callable
                        put_To: _Callable
                        get_By: _Callable
                        put_By: _Callable
                        get_EasingFunction: _Callable
                        put_EasingFunction: _Callable
                        get_EnableDependentAnimation: _Callable
                        put_EnableDependentAnimation: _Callable

                    class IPointAnimationStatics(IInspectable):
                        get_FromProperty: _Callable
                        get_ToProperty: _Callable
                        get_ByProperty: _Callable
                        get_EasingFunctionProperty: _Callable
                        get_EnableDependentAnimationProperty: _Callable

                    class IPointAnimationUsingKeyFrames(IInspectable):
                        get_KeyFrames: _Callable
                        get_EnableDependentAnimation: _Callable
                        put_EnableDependentAnimation: _Callable

                    class IPointAnimationUsingKeyFramesStatics(IInspectable):
                        get_EnableDependentAnimationProperty: _Callable

                    class IPointKeyFrame(IInspectable):
                        get_Value: _Callable
                        put_Value: _Callable
                        get_KeyTime: _Callable
                        put_KeyTime: _Callable

                    class IPointKeyFrameFactory(IInspectable):
                        CreateInstance: _Callable

                    class IPointKeyFrameStatics(IInspectable):
                        get_ValueProperty: _Callable
                        get_KeyTimeProperty: _Callable

                    class IPointerDownThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable

                    class IPointerDownThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable

                    class IPointerUpThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable

                    class IPointerUpThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable

                    class IPopInThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable
                        get_FromHorizontalOffset: _Callable
                        put_FromHorizontalOffset: _Callable
                        get_FromVerticalOffset: _Callable
                        put_FromVerticalOffset: _Callable

                    class IPopInThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable
                        get_FromHorizontalOffsetProperty: _Callable
                        get_FromVerticalOffsetProperty: _Callable

                    class IPopOutThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable

                    class IPopOutThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable

                    class IPopupThemeTransition(IInspectable):
                        get_FromHorizontalOffset: _Callable
                        put_FromHorizontalOffset: _Callable
                        get_FromVerticalOffset: _Callable
                        put_FromVerticalOffset: _Callable

                    class IPopupThemeTransitionStatics(IInspectable):
                        get_FromHorizontalOffsetProperty: _Callable
                        get_FromVerticalOffsetProperty: _Callable

                    class IPowerEase(IInspectable):
                        get_Power: _Callable
                        put_Power: _Callable

                    class IPowerEaseStatics(IInspectable):
                        get_PowerProperty: _Callable

                    class IQuadraticEase(IInspectable):
                        pass

                    class IQuarticEase(IInspectable):
                        pass

                    class IQuinticEase(IInspectable):
                        pass

                    class IReorderThemeTransition(IInspectable):
                        pass

                    class IRepeatBehaviorHelper(IInspectable):
                        pass

                    class IRepeatBehaviorHelperStatics(IInspectable):
                        get_Forever: _Callable
                        FromCount: _Callable
                        FromDuration: _Callable
                        GetHasCount: _Callable
                        GetHasDuration: _Callable
                        Equals: _Callable

                    class IRepositionThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable
                        get_FromHorizontalOffset: _Callable
                        put_FromHorizontalOffset: _Callable
                        get_FromVerticalOffset: _Callable
                        put_FromVerticalOffset: _Callable

                    class IRepositionThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable
                        get_FromHorizontalOffsetProperty: _Callable
                        get_FromVerticalOffsetProperty: _Callable

                    class IRepositionThemeTransition(IInspectable):
                        pass

                    class IRepositionThemeTransition2(IInspectable):
                        get_IsStaggeringEnabled: _Callable
                        put_IsStaggeringEnabled: _Callable

                    class IRepositionThemeTransitionStatics2(IInspectable):
                        get_IsStaggeringEnabledProperty: _Callable

                    class ISineEase(IInspectable):
                        pass

                    class ISlideNavigationTransitionInfo(IInspectable):
                        pass

                    class ISlideNavigationTransitionInfo2(IInspectable):
                        get_Effect: _Callable
                        put_Effect: _Callable

                    class ISlideNavigationTransitionInfoStatics2(IInspectable):
                        get_EffectProperty: _Callable

                    class ISplineColorKeyFrame(IInspectable):
                        get_KeySpline: _Callable
                        put_KeySpline: _Callable

                    class ISplineColorKeyFrameStatics(IInspectable):
                        get_KeySplineProperty: _Callable

                    class ISplineDoubleKeyFrame(IInspectable):
                        get_KeySpline: _Callable
                        put_KeySpline: _Callable

                    class ISplineDoubleKeyFrameStatics(IInspectable):
                        get_KeySplineProperty: _Callable

                    class ISplinePointKeyFrame(IInspectable):
                        get_KeySpline: _Callable
                        put_KeySpline: _Callable

                    class ISplinePointKeyFrameStatics(IInspectable):
                        get_KeySplineProperty: _Callable

                    class ISplitCloseThemeAnimation(IInspectable):
                        get_OpenedTargetName: _Callable
                        put_OpenedTargetName: _Callable
                        get_OpenedTarget: _Callable
                        put_OpenedTarget: _Callable
                        get_ClosedTargetName: _Callable
                        put_ClosedTargetName: _Callable
                        get_ClosedTarget: _Callable
                        put_ClosedTarget: _Callable
                        get_ContentTargetName: _Callable
                        put_ContentTargetName: _Callable
                        get_ContentTarget: _Callable
                        put_ContentTarget: _Callable
                        get_OpenedLength: _Callable
                        put_OpenedLength: _Callable
                        get_ClosedLength: _Callable
                        put_ClosedLength: _Callable
                        get_OffsetFromCenter: _Callable
                        put_OffsetFromCenter: _Callable
                        get_ContentTranslationDirection: _Callable
                        put_ContentTranslationDirection: _Callable
                        get_ContentTranslationOffset: _Callable
                        put_ContentTranslationOffset: _Callable

                    class ISplitCloseThemeAnimationStatics(IInspectable):
                        get_OpenedTargetNameProperty: _Callable
                        get_OpenedTargetProperty: _Callable
                        get_ClosedTargetNameProperty: _Callable
                        get_ClosedTargetProperty: _Callable
                        get_ContentTargetNameProperty: _Callable
                        get_ContentTargetProperty: _Callable
                        get_OpenedLengthProperty: _Callable
                        get_ClosedLengthProperty: _Callable
                        get_OffsetFromCenterProperty: _Callable
                        get_ContentTranslationDirectionProperty: _Callable
                        get_ContentTranslationOffsetProperty: _Callable

                    class ISplitOpenThemeAnimation(IInspectable):
                        get_OpenedTargetName: _Callable
                        put_OpenedTargetName: _Callable
                        get_OpenedTarget: _Callable
                        put_OpenedTarget: _Callable
                        get_ClosedTargetName: _Callable
                        put_ClosedTargetName: _Callable
                        get_ClosedTarget: _Callable
                        put_ClosedTarget: _Callable
                        get_ContentTargetName: _Callable
                        put_ContentTargetName: _Callable
                        get_ContentTarget: _Callable
                        put_ContentTarget: _Callable
                        get_OpenedLength: _Callable
                        put_OpenedLength: _Callable
                        get_ClosedLength: _Callable
                        put_ClosedLength: _Callable
                        get_OffsetFromCenter: _Callable
                        put_OffsetFromCenter: _Callable
                        get_ContentTranslationDirection: _Callable
                        put_ContentTranslationDirection: _Callable
                        get_ContentTranslationOffset: _Callable
                        put_ContentTranslationOffset: _Callable

                    class ISplitOpenThemeAnimationStatics(IInspectable):
                        get_OpenedTargetNameProperty: _Callable
                        get_OpenedTargetProperty: _Callable
                        get_ClosedTargetNameProperty: _Callable
                        get_ClosedTargetProperty: _Callable
                        get_ContentTargetNameProperty: _Callable
                        get_ContentTargetProperty: _Callable
                        get_OpenedLengthProperty: _Callable
                        get_ClosedLengthProperty: _Callable
                        get_OffsetFromCenterProperty: _Callable
                        get_ContentTranslationDirectionProperty: _Callable
                        get_ContentTranslationOffsetProperty: _Callable

                    class IStoryboard(IInspectable):
                        get_Children: _Callable
                        Seek: _Callable
                        Stop: _Callable
                        Begin: _Callable
                        Pause: _Callable
                        Resume: _Callable
                        GetCurrentState: _Callable
                        GetCurrentTime: _Callable
                        SeekAlignedToLastTick: _Callable
                        SkipToFill: _Callable

                    class IStoryboardStatics(IInspectable):
                        get_TargetPropertyProperty: _Callable
                        GetTargetProperty: _Callable
                        SetTargetProperty: _Callable
                        get_TargetNameProperty: _Callable
                        GetTargetName: _Callable
                        SetTargetName: _Callable
                        SetTarget: _Callable

                    class ISuppressNavigationTransitionInfo(IInspectable):
                        pass

                    class ISwipeBackThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable
                        get_FromHorizontalOffset: _Callable
                        put_FromHorizontalOffset: _Callable
                        get_FromVerticalOffset: _Callable
                        put_FromVerticalOffset: _Callable

                    class ISwipeBackThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable
                        get_FromHorizontalOffsetProperty: _Callable
                        get_FromVerticalOffsetProperty: _Callable

                    class ISwipeHintThemeAnimation(IInspectable):
                        get_TargetName: _Callable
                        put_TargetName: _Callable
                        get_ToHorizontalOffset: _Callable
                        put_ToHorizontalOffset: _Callable
                        get_ToVerticalOffset: _Callable
                        put_ToVerticalOffset: _Callable

                    class ISwipeHintThemeAnimationStatics(IInspectable):
                        get_TargetNameProperty: _Callable
                        get_ToHorizontalOffsetProperty: _Callable
                        get_ToVerticalOffsetProperty: _Callable

                    class ITimeline(IInspectable):
                        get_AutoReverse: _Callable
                        put_AutoReverse: _Callable
                        get_BeginTime: _Callable
                        put_BeginTime: _Callable
                        get_Duration: _Callable
                        put_Duration: _Callable
                        get_SpeedRatio: _Callable
                        put_SpeedRatio: _Callable
                        get_FillBehavior: _Callable
                        put_FillBehavior: _Callable
                        get_RepeatBehavior: _Callable
                        put_RepeatBehavior: _Callable
                        add_Completed: _Callable
                        remove_Completed: _Callable

                    class ITimelineFactory(IInspectable):
                        CreateInstance: _Callable

                    class ITimelineStatics(IInspectable):
                        get_AllowDependentAnimations: _Callable
                        put_AllowDependentAnimations: _Callable
                        get_AutoReverseProperty: _Callable
                        get_BeginTimeProperty: _Callable
                        get_DurationProperty: _Callable
                        get_SpeedRatioProperty: _Callable
                        get_FillBehaviorProperty: _Callable
                        get_RepeatBehaviorProperty: _Callable

                    class ITransition(IInspectable):
                        pass

                    class ITransitionFactory(IInspectable):
                        pass
