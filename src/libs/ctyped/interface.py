from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable, Generic as _Generic, Optional as _Optional

from . import const as _const, enum as _enum, lib as _lib, macro as _macro, struct as _struct, type as _type
from ._utils import _Pointer, _addressof, _byref, _format_annotations, _get_func_doc, _pointer, _resolve_type

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
            cls.__doc__ = '\n\n'.join(_get_func_doc(name, types._restype_, types._argtypes_[1:], _format_annotations(annots[name])) for name, types in cls._vtbl._fields_)
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
            cls._iid_refs = set()
            base = cls
            for base_ in cls.__mro__[cls.__mro__.index(_Interface_impl) - 2::-1]:
                # noinspection PyProtectedMember
                if __name__ == base_.__module__ and not (issubclass(base_, _Template) and base_._args is None):
                    # noinspection PyTypeChecker,PyProtectedMember
                    cls._iid_refs.add(_byref(_macro._uuidof(base_)))
                    base = base_
            cls._iid_refs = frozenset(cls._iid_refs)
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
        obj_ref = _type.LPVOID.from_address(ppvObject)
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


class _IQueryContinueWithStatus(_IQueryContinue):
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
    get_Status: _Callable[[_Pointer[_enum.AsyncStatus]],
                          _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],
                             _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class Windows:
    class Data:
        class Xml:
            class Dom:
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

                class IXmlNodeSerializer(IInspectable):
                    GetXml: _Callable[[_Pointer[_type.HSTRING]],
                                      _type.HRESULT]
                    get_InnerText: _Callable[[_Pointer[_type.HSTRING]],
                                             _type.HRESULT]
                    put_InnerText: _Callable[[_type.HSTRING],
                                             _type.HRESULT]

    class Foundation:
        class _IAsyncActionCompletedHandler(IUnknown):
            Invoke: _Callable[[Windows.Foundation.IAsyncAction,
                               _enum.AsyncStatus],
                              _type.HRESULT]

        class IAsyncActionCompletedHandler(_IAsyncActionCompletedHandler, IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncActionCompletedHandler_impl(_IAsyncActionCompletedHandler, IUnknown_impl):
            pass

        class IDeferralCompletedHandler(IUnknown):
            Invoke: _Callable[[],
                              _type.HRESULT]

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
            Create: _Callable[[Windows.Foundation.IDeferralCompletedHandler,
                               _Pointer[Windows.Foundation.IDeferral]],
                              _type.HRESULT]

        class IGetActivationFactory(IInspectable):
            GetActivationFactory: _Callable[[_type.HSTRING,
                                             _Pointer[IInspectable]],
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
                               _enum.AsyncStatus],
                              _type.HRESULT]

        class IAsyncOperationWithProgressCompletedHandler(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncOperationWithProgressCompletedHandler_impl(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], IUnknown_impl):
            pass

        class _IAsyncOperationCompletedHandler(_Template):
            Invoke: _Callable[[Windows.Foundation.IAsyncOperation[_TResult],
                               _enum.AsyncStatus],
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
                               _enum.AsyncStatus],
                              _type.HRESULT]

        class IAsyncActionWithProgressCompletedHandler(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], IUnknown):
            pass

        # noinspection PyPep8Naming
        class IAsyncActionWithProgressCompletedHandler_impl(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], IUnknown_impl):
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
            class IVector(_Template, _Generic[_T], IInspectable):
                GetAt: _Callable[[_Optional[_type.c_uint],
                                  _Pointer[_T]],
                                 _type.HRESULT]
                get_Size: _Callable[[_Pointer[_type.c_uint]],
                                    _type.HRESULT]
                GetView: _Callable
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

    class Storage:
        class IStorageFile(IInspectable):
            get_FileType: _Callable[[_Pointer[_type.HSTRING]],
                                    _type.HRESULT]
            get_ContentType: _Callable[[_Pointer[_type.HSTRING]],
                                       _type.HRESULT]
            OpenAsync: _Callable[[_enum.FileAccessMode,
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
                                     _enum.NameCollisionOption,
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
                                     _enum.NameCollisionOption,
                                     _Pointer[Windows.Foundation.IAsyncAction]],
                                    _type.HRESULT]
            MoveAndReplaceAsync: _Callable[[Windows.Storage.IStorageFile,
                                            _Pointer[Windows.Foundation.IAsyncAction]],
                                           _type.HRESULT]

        class IStorageFileStatics(IInspectable):
            GetFileFromPathAsync: _Callable[[_type.HSTRING,
                                             _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                            _type.HRESULT]
            GetFileFromApplicationUriAsync: _Callable
            CreateStreamedFileAsync: _Callable
            ReplaceWithStreamedFileAsync: _Callable
            CreateStreamedFileFromUriAsync: _Callable
            ReplaceWithStreamedFileFromUriAsync: _Callable

        class IStorageFolder(IInspectable):
            CreateFileAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                              _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                                             _type.HSTRING]
            CreateFileAsync: _Callable[[_type.HSTRING,
                                        _enum.CreationCollisionOption,
                                        _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFile]]],
                                       _type.HRESULT]
            CreateFolderAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                                _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFolder]]],
                                                               _type.HSTRING]
            CreateFolderAsync: _Callable[[_type.HSTRING,
                                          _enum.CreationCollisionOption,
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

        class IStorageFolderStatics(IInspectable):
            GetFolderFromPathAsync: _Callable[[_type.HSTRING,
                                               _Pointer[Windows.Foundation.IAsyncOperation[Windows.Storage.IStorageFolder]]],
                                              _type.HRESULT]

        class IStorageItem(IInspectable):
            RenameAsyncOverloadDefaultOptions: _Callable[[_type.HSTRING,
                                                          _Pointer[Windows.Foundation.IAsyncAction]],
                                                         _type.HRESULT]
            RenameAsync: _Callable[[_type.HSTRING,
                                    _enum.NameCollisionOption,
                                    _Pointer[Windows.Foundation.IAsyncAction]],
                                   _type.HRESULT]
            DeleteAsyncOverloadDefaultOptions: _Callable[[_Pointer[Windows.Foundation.IAsyncAction]],
                                                         _type.HRESULT]
            DeleteAsync: _Callable[[_enum.StorageDeleteOption,
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
                                      _Pointer[Windows.Foundation.IAsyncOperationWithProgress[Windows.Storage.Streams.IBuffer, _type.UINT32]]],
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

    class System:
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

        class UserProfile:
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

    class UI:
        class IColorsStatics(IInspectable):
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
                get_Argument: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]

            class IToastActivatedEventArgs2(IInspectable):
                get_UserInput: _Callable

            class IToastDismissedEventArgs(IInspectable):
                get_Reason: _Callable[[_Pointer[_enum.ToastDismissalReason]],
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

            class IToastNotificationFactory(IInspectable):
                CreateToastNotification: _Callable[[Windows.Data.Xml.Dom.IXmlDocument,
                                                    _Pointer[Windows.UI.Notifications.IToastNotification]],
                                                   _type.HRESULT]

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
                get_Setting: _Callable[[_Pointer[_enum.NotificationSetting]],
                                       _type.HRESULT]
                AddToSchedule: _Callable
                RemoveFromSchedule: _Callable
                GetScheduledToastNotifications: _Callable

        class ViewManagement:
            class IUISettings(IInspectable):
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

                class IStackPanel(IInspectable):
                    get_AreScrollSnapPointsRegular: _Callable[[_Pointer[_type.boolean]],
                                                              _type.HRESULT]
                    put_AreScrollSnapPointsRegular: _Callable[[_type.boolean],
                                                              _type.HRESULT]
                    get_Orientation: _Callable[[_Pointer[_enum.Orientation]],
                                               _type.HRESULT]
                    put_Orientation: _Callable[[_enum.Orientation],
                                               _type.HRESULT]

                class IStackPanelFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IStackPanel]],
                                              _type.HRESULT]

                class IStackPanelStatics(IInspectable):
                    get_AreScrollSnapPointsRegularProperty: _Callable
                    get_OrientationProperty: _Callable

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
                    Move: _Callable[[_type.UINT32,
                                     _type.UINT32],
                                    _type.HRESULT]

            class Hosting:
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

                class IWindowsXamlManager(IInspectable):
                    pass

                class IWindowsXamlManagerStatics(IInspectable):
                    InitializeForCurrentThread: _Callable[[_Pointer[Windows.UI.Xaml.Hosting.IWindowsXamlManager]],
                                                          _type.HRESULT]

            class Media:
                class IBrush(IInspectable):
                    get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],
                                           _type.HRESULT]
                    put_Opacity: _Callable[[_type.DOUBLE],
                                           _type.HRESULT]
                    get_Transform: _Callable
                    put_Transform: _Callable
                    get_RelativeTransform: _Callable
                    put_RelativeTransform: _Callable

                class ISolidColorBrush(IInspectable):
                    get_Color: _Callable[[_Pointer[_struct.Color]],
                                         _type.HRESULT]
                    put_Color: _Callable[[_struct.Color],
                                         _type.HRESULT]

                class ISolidColorBrushFactory(IInspectable):
                    CreateInstanceWithColor: _Callable[[_struct.Color,
                                                        _Pointer[Windows.UI.Xaml.Media.ISolidColorBrush]],
                                                       _type.HRESULT]
