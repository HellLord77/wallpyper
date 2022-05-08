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
_CArgObject = type(_ctypes.byref(_ctypes.c_void_p()))


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
            qualname = f'{cls.__qualname__.removesuffix("_impl")}_{"_".join(type_.__name__ for type_ in args.values())}{"_impl" * cls.__qualname__.endswith("_impl")}'
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
        # noinspection PyUnresolvedReferences,PyProtectedMember
        obj_ref = ppvObject._obj if isinstance(ppvObject, _CArgObject) else _type.LPVOID.from_address(ppvObject)
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
            CreateNewGuid: _Callable[[_Pointer[_struct.GUID]],
                                     _type.HRESULT]
            get_Empty: _Callable[[_Pointer[_struct.GUID]],
                                 _type.HRESULT]
            Equals: _Callable[[_Pointer[_struct.GUID],
                               _Pointer[_struct.GUID],
                               _Pointer[_type.boolean]],
                              _type.HRESULT]

        class IMemoryBuffer(IInspectable):
            CreateReference: _Callable[[_Pointer[Windows.Foundation.IMemoryBufferReference]],
                                       _type.HRESULT]

        class IMemoryBufferFactory(IInspectable):
            Create: _Callable[[_type.UINT32,
                               _Pointer[Windows.Foundation.IMemoryBuffer]],
                              _type.HRESULT]

        class IMemoryBufferReference(IInspectable):
            get_Capacity: _Callable[[_Pointer[_type.UINT32]],
                                    _type.HRESULT]
            add_Closed: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.Foundation.IMemoryBufferReference, IInspectable],
                                   _Pointer[_struct.EventRegistrationToken]],
                                  _type.HRESULT]
            remove_Closed: _Callable[[_struct.EventRegistrationToken],
                                     _type.HRESULT]

        class IPropertyValue(IInspectable):
            get_Type: _Callable[[_Pointer[_enum.Windows.Foundation.PropertyType]],
                                _type.HRESULT]
            get_IsNumericScalar: _Callable[[_Pointer[_type.boolean]],
                                           _type.HRESULT]
            GetUInt8: _Callable[[_Pointer[_type.BYTE]],
                                _type.HRESULT]
            GetInt16: _Callable[[_Pointer[_type.INT16]],
                                _type.HRESULT]
            GetUInt16: _Callable[[_Pointer[_type.UINT16]],
                                 _type.HRESULT]
            GetInt32: _Callable[[_Pointer[_type.INT32]],
                                _type.HRESULT]
            GetUInt32: _Callable[[_Pointer[_type.UINT32]],
                                 _type.HRESULT]
            GetInt64: _Callable[[_Pointer[_type.INT64]],
                                _type.HRESULT]
            GetUInt64: _Callable[[_Pointer[_type.UINT64]],
                                 _type.HRESULT]
            GetSingle: _Callable[[_Pointer[_type.FLOAT]],
                                 _type.HRESULT]
            GetDouble: _Callable[[_Pointer[_type.DOUBLE]],
                                 _type.HRESULT]
            GetChar16: _Callable[[_Pointer[_type.WCHAR]],
                                 _type.HRESULT]
            GetBoolean: _Callable[[_Pointer[_type.boolean]],
                                  _type.HRESULT]
            GetString: _Callable[[_Pointer[_type.HSTRING]],
                                 _type.HRESULT]
            GetGuid: _Callable[[_Pointer[_struct.GUID]],
                               _type.HRESULT]
            GetDateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],
                                   _type.HRESULT]
            GetTimeSpan: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],
                                   _type.HRESULT]
            GetPoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],
                                _type.HRESULT]
            GetSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                               _type.HRESULT]
            GetRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],
                               _type.HRESULT]
            GetUInt8Array: _Callable[[_Pointer[_type.UINT32],
                                      _Pointer[_Pointer[_type.BYTE]]],
                                     _type.HRESULT]
            GetInt16Array: _Callable[[_Pointer[_type.UINT32],
                                      _Pointer[_Pointer[_type.INT16]]],
                                     _type.HRESULT]
            GetUInt16Array: _Callable[[_Pointer[_type.UINT32],
                                       _Pointer[_Pointer[_type.UINT16]]],
                                      _type.HRESULT]
            GetInt32Array: _Callable[[_Pointer[_type.UINT32],
                                      _Pointer[_Pointer[_type.INT32]]],
                                     _type.HRESULT]
            GetUInt32Array: _Callable[[_Pointer[_type.UINT32],
                                       _Pointer[_Pointer[_type.UINT32]]],
                                      _type.HRESULT]
            GetInt64Array: _Callable[[_Pointer[_type.UINT32],
                                      _Pointer[_Pointer[_type.INT64]]],
                                     _type.HRESULT]
            GetUInt64Array: _Callable[[_Pointer[_type.UINT32],
                                       _Pointer[_Pointer[_type.UINT64]]],
                                      _type.HRESULT]
            GetSingleArray: _Callable[[_Pointer[_type.UINT32],
                                       _Pointer[_Pointer[_type.FLOAT]]],
                                      _type.HRESULT]
            GetDoubleArray: _Callable[[_Pointer[_type.UINT32],
                                       _Pointer[_Pointer[_type.DOUBLE]]],
                                      _type.HRESULT]
            GetChar16Array: _Callable[[_Pointer[_type.UINT32],
                                       _Pointer[_Pointer[_type.WCHAR]]],
                                      _type.HRESULT]
            GetBooleanArray: _Callable[[_Pointer[_type.UINT32],
                                        _Pointer[_Pointer[_type.boolean]]],
                                       _type.HRESULT]
            GetStringArray: _Callable[[_Pointer[_type.UINT32],
                                       _Pointer[_Pointer[_type.HSTRING]]],
                                      _type.HRESULT]
            GetInspectableArray: _Callable[[_Pointer[_type.UINT32],
                                            _Pointer[_Pointer[IInspectable]]],
                                           _type.HRESULT]
            GetGuidArray: _Callable[[_Pointer[_type.UINT32],
                                     _Pointer[_Pointer[_struct.GUID]]],
                                    _type.HRESULT]
            GetDateTimeArray: _Callable[[_Pointer[_type.UINT32],
                                         _Pointer[_Pointer[_struct.Windows.Foundation.DateTime]]],
                                        _type.HRESULT]
            GetTimeSpanArray: _Callable[[_Pointer[_type.UINT32],
                                         _Pointer[_Pointer[_struct.Windows.Foundation.TimeSpan]]],
                                        _type.HRESULT]
            GetPointArray: _Callable[[_Pointer[_type.UINT32],
                                      _Pointer[_Pointer[_struct.Windows.Foundation.Point]]],
                                     _type.HRESULT]
            GetSizeArray: _Callable[[_Pointer[_type.UINT32],
                                     _Pointer[_Pointer[_struct.Windows.Foundation.Size]]],
                                    _type.HRESULT]
            GetRectArray: _Callable[[_Pointer[_type.UINT32],
                                     _Pointer[_Pointer[_struct.Windows.Foundation.Rect]]],
                                    _type.HRESULT]

        class IPropertyValueStatics(IInspectable):
            CreateEmpty: _Callable[[_Pointer[IInspectable]],
                                   _type.HRESULT]
            CreateUInt8: _Callable[[_type.BYTE,
                                    _Pointer[IInspectable]],
                                   _type.HRESULT]
            CreateInt16: _Callable[[_type.INT16,
                                    _Pointer[IInspectable]],
                                   _type.HRESULT]
            CreateUInt16: _Callable[[_type.UINT16,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
            CreateInt32: _Callable[[_type.INT32,
                                    _Pointer[IInspectable]],
                                   _type.HRESULT]
            CreateUInt32: _Callable[[_type.UINT32,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
            CreateInt64: _Callable[[_type.INT64,
                                    _Pointer[IInspectable]],
                                   _type.HRESULT]
            CreateUInt64: _Callable[[_type.UINT64,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
            CreateSingle: _Callable[[_type.FLOAT,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
            CreateDouble: _Callable[[_type.DOUBLE,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
            CreateChar16: _Callable[[_type.WCHAR,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
            CreateBoolean: _Callable[[_type.boolean,
                                      _Pointer[IInspectable]],
                                     _type.HRESULT]
            CreateString: _Callable[[_type.HSTRING,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
            CreateInspectable: _Callable[[IInspectable,
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateGuid: _Callable[[_struct.GUID,
                                   _Pointer[IInspectable]],
                                  _type.HRESULT]
            CreateDateTime: _Callable[[_struct.Windows.Foundation.DateTime,
                                       _Pointer[IInspectable]],
                                      _type.HRESULT]
            CreateTimeSpan: _Callable[[_struct.Windows.Foundation.TimeSpan,
                                       _Pointer[IInspectable]],
                                      _type.HRESULT]
            CreatePoint: _Callable[[_struct.Windows.Foundation.Point,
                                    _Pointer[IInspectable]],
                                   _type.HRESULT]
            CreateSize: _Callable[[_struct.Windows.Foundation.Size,
                                   _Pointer[IInspectable]],
                                  _type.HRESULT]
            CreateRect: _Callable[[_struct.Windows.Foundation.Rect,
                                   _Pointer[IInspectable]],
                                  _type.HRESULT]
            CreateUInt8Array: _Callable[[_type.UINT32,
                                         _Pointer[_type.BYTE],
                                         _Pointer[IInspectable]],
                                        _type.HRESULT]
            CreateInt16Array: _Callable[[_type.UINT32,
                                         _Pointer[_type.INT16],
                                         _Pointer[IInspectable]],
                                        _type.HRESULT]
            CreateUInt16Array: _Callable[[_type.UINT32,
                                          _Pointer[_type.UINT16],
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateInt32Array: _Callable[[_type.UINT32,
                                         _Pointer[_type.INT32],
                                         _Pointer[IInspectable]],
                                        _type.HRESULT]
            CreateUInt32Array: _Callable[[_type.UINT32,
                                          _Pointer[_type.UINT32],
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateInt64Array: _Callable[[_type.UINT32,
                                         _Pointer[_type.INT64],
                                         _Pointer[IInspectable]],
                                        _type.HRESULT]
            CreateUInt64Array: _Callable[[_type.UINT32,
                                          _Pointer[_type.UINT64],
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateSingleArray: _Callable[[_type.UINT32,
                                          _Pointer[_type.FLOAT],
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateDoubleArray: _Callable[[_type.UINT32,
                                          _Pointer[_type.DOUBLE],
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateChar16Array: _Callable[[_type.UINT32,
                                          _Pointer[_type.WCHAR],
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateBooleanArray: _Callable[[_type.UINT32,
                                           _Pointer[_type.boolean],
                                           _Pointer[IInspectable]],
                                          _type.HRESULT]
            CreateStringArray: _Callable[[_type.UINT32,
                                          _Pointer[_type.HSTRING],
                                          _Pointer[IInspectable]],
                                         _type.HRESULT]
            CreateInspectableArray: _Callable[[_type.UINT32,
                                               _Pointer[IInspectable],
                                               _Pointer[IInspectable]],
                                              _type.HRESULT]
            CreateGuidArray: _Callable[[_type.UINT32,
                                        _Pointer[_struct.GUID],
                                        _Pointer[IInspectable]],
                                       _type.HRESULT]
            CreateDateTimeArray: _Callable[[_type.UINT32,
                                            _Pointer[_struct.Windows.Foundation.DateTime],
                                            _Pointer[IInspectable]],
                                           _type.HRESULT]
            CreateTimeSpanArray: _Callable[[_type.UINT32,
                                            _Pointer[_struct.Windows.Foundation.TimeSpan],
                                            _Pointer[IInspectable]],
                                           _type.HRESULT]
            CreatePointArray: _Callable[[_type.UINT32,
                                         _Pointer[_struct.Windows.Foundation.Point],
                                         _Pointer[IInspectable]],
                                        _type.HRESULT]
            CreateSizeArray: _Callable[[_type.UINT32,
                                        _Pointer[_struct.Windows.Foundation.Size],
                                        _Pointer[IInspectable]],
                                       _type.HRESULT]
            CreateRectArray: _Callable[[_type.UINT32,
                                        _Pointer[_struct.Windows.Foundation.Rect],
                                        _Pointer[IInspectable]],
                                       _type.HRESULT]

        class IStringable(IInspectable):
            ToString: _Callable[[_Pointer[_type.HSTRING]],
                                _type.HRESULT]

        class IUriEscapeStatics(IInspectable):
            UnescapeComponent: _Callable[[_type.HSTRING,
                                          _Pointer[_type.HSTRING]],
                                         _type.HRESULT]
            EscapeComponent: _Callable[[_type.HSTRING,
                                        _Pointer[_type.HSTRING]],
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

        class IUriRuntimeClassFactory(IInspectable):
            CreateUri: _Callable[[_type.HSTRING,
                                  _Pointer[Windows.Foundation.IUriRuntimeClass]],
                                 _type.HRESULT]
            CreateWithRelativeUri: _Callable[[_type.HSTRING,
                                              _type.HSTRING,
                                              _Pointer[Windows.Foundation.IUriRuntimeClass]],
                                             _type.HRESULT]

        class IUriRuntimeClassWithAbsoluteCanonicalUri(IInspectable):
            get_AbsoluteCanonicalUri: _Callable[[_Pointer[_type.HSTRING]],
                                                _type.HRESULT]
            get_DisplayIri: _Callable[[_Pointer[_type.HSTRING]],
                                      _type.HRESULT]

        class IWwwFormUrlDecoderEntry(IInspectable):
            get_Name: _Callable[[_Pointer[_type.HSTRING]],
                                _type.HRESULT]
            get_Value: _Callable[[_Pointer[_type.HSTRING]],
                                 _type.HRESULT]

        class IWwwFormUrlDecoderRuntimeClass(IInspectable):
            GetFirstValueByName: _Callable[[_type.HSTRING,
                                            _Pointer[_type.HSTRING]],
                                           _type.HRESULT]

        class IWwwFormUrlDecoderRuntimeClassFactory(IInspectable):
            CreateWwwFormUrlDecoder: _Callable[[_type.HSTRING,
                                                _Pointer[Windows.Foundation.IWwwFormUrlDecoderRuntimeClass]],
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

        class IReference(_Template, _Generic[_T], IInspectable):
            get_Value: _Callable[[_Pointer[_T]],
                                 _type.HRESULT]

        class IReferenceArray(_Template, _Generic[_T], IInspectable):
            get_Value: _Callable[[_Pointer[_type.UINT32],
                                  _Pointer[_Pointer[_T]]],
                                 _type.HRESULT]

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

    class Gaming:
        class UI:
            class IGameBarStatics(IInspectable):
                add_VisibilityChanged: _Callable
                remove_VisibilityChanged: _Callable
                add_IsInputRedirectedChanged: _Callable
                remove_IsInputRedirectedChanged: _Callable
                get_Visible: _Callable
                get_IsInputRedirected: _Callable

            class IGameChatMessageReceivedEventArgs(IInspectable):
                get_AppId: _Callable
                get_AppDisplayName: _Callable
                get_SenderName: _Callable
                get_Message: _Callable
                get_Origin: _Callable

            class IGameChatOverlay(IInspectable):
                get_DesiredPosition: _Callable
                put_DesiredPosition: _Callable
                AddMessage: _Callable

            class IGameChatOverlayMessageSource(IInspectable):
                add_MessageReceived: _Callable
                remove_MessageReceived: _Callable
                SetDelayBeforeClosingAfterMessageReceived: _Callable

            class IGameChatOverlayStatics(IInspectable):
                GetDefault: _Callable

            class IGameUIProviderActivatedEventArgs(IInspectable):
                get_GameUIArgs: _Callable
                ReportCompleted: _Callable

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

        class Accessibility:
            class IScreenReaderPositionChangedEventArgs(IInspectable):
                get_ScreenPositionInRawPixels: _Callable
                get_IsReadingText: _Callable

            class IScreenReaderService(IInspectable):
                get_CurrentScreenReaderPosition: _Callable
                add_ScreenReaderPositionChanged: _Callable
                remove_ScreenReaderPositionChanged: _Callable

        class ApplicationSettings:
            class _ICredentialCommandCredentialDeletedHandler:
                Invoke: _Callable

            class ICredentialCommandCredentialDeletedHandler(_ICredentialCommandCredentialDeletedHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class ICredentialCommandCredentialDeletedHandler_impl(_ICredentialCommandCredentialDeletedHandler, IUnknown_impl):
                pass

            class _IWebAccountCommandInvokedHandler:
                Invoke: _Callable

            class IWebAccountCommandInvokedHandler(_IWebAccountCommandInvokedHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IWebAccountCommandInvokedHandler_impl(_IWebAccountCommandInvokedHandler, IUnknown_impl):
                pass

            class _IWebAccountProviderCommandInvokedHandler:
                Invoke: _Callable

            class IWebAccountProviderCommandInvokedHandler(_IWebAccountProviderCommandInvokedHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IWebAccountProviderCommandInvokedHandler_impl(_IWebAccountProviderCommandInvokedHandler, IUnknown_impl):
                pass

            class IAccountsSettingsPane(IInspectable):
                add_AccountCommandsRequested: _Callable
                remove_AccountCommandsRequested: _Callable

            class IAccountsSettingsPaneCommandsRequestedEventArgs(IInspectable):
                get_WebAccountProviderCommands: _Callable
                get_WebAccountCommands: _Callable
                get_CredentialCommands: _Callable
                get_Commands: _Callable
                get_HeaderText: _Callable
                put_HeaderText: _Callable
                GetDeferral: _Callable

            class IAccountsSettingsPaneCommandsRequestedEventArgs2(IInspectable):
                get_User: _Callable

            class IAccountsSettingsPaneEventDeferral(IInspectable):
                Complete: _Callable

            class IAccountsSettingsPaneStatics(IInspectable):
                GetForCurrentView: _Callable
                Show: _Callable

            class IAccountsSettingsPaneStatics2(IInspectable):
                ShowManageAccountsAsync: _Callable
                ShowAddAccountAsync: _Callable

            class IAccountsSettingsPaneStatics3(IInspectable):
                ShowManageAccountsForUserAsync: _Callable
                ShowAddAccountForUserAsync: _Callable

            class ICredentialCommand(IInspectable):
                get_PasswordCredential: _Callable
                get_CredentialDeleted: _Callable

            class ICredentialCommandFactory(IInspectable):
                CreateCredentialCommand: _Callable
                CreateCredentialCommandWithHandler: _Callable

            class ISettingsCommandFactory(IInspectable):
                CreateSettingsCommand: _Callable

            class ISettingsCommandStatics(IInspectable):
                get_AccountsCommand: _Callable

            class ISettingsPane(IInspectable):
                add_CommandsRequested: _Callable
                remove_CommandsRequested: _Callable

            class ISettingsPaneCommandsRequest(IInspectable):
                get_ApplicationCommands: _Callable

            class ISettingsPaneCommandsRequestedEventArgs(IInspectable):
                get_Request: _Callable

            class ISettingsPaneStatics(IInspectable):
                GetForCurrentView: _Callable
                Show: _Callable
                get_Edge: _Callable

            class IWebAccountCommand(IInspectable):
                get_WebAccount: _Callable
                get_Invoked: _Callable
                get_Actions: _Callable

            class IWebAccountCommandFactory(IInspectable):
                CreateWebAccountCommand: _Callable

            class IWebAccountInvokedArgs(IInspectable):
                get_Action: _Callable

            class IWebAccountProviderCommand(IInspectable):
                get_WebAccountProvider: _Callable
                get_Invoked: _Callable

            class IWebAccountProviderCommandFactory(IInspectable):
                CreateWebAccountProviderCommand: _Callable

        class Composition:
            class IAmbientLight(IInspectable):
                get_Color: _Callable
                put_Color: _Callable

            class IAmbientLight2(IInspectable):
                get_Intensity: _Callable
                put_Intensity: _Callable

            class IAnimationController(IInspectable):
                get_PlaybackRate: _Callable
                put_PlaybackRate: _Callable
                get_Progress: _Callable
                put_Progress: _Callable
                get_ProgressBehavior: _Callable
                put_ProgressBehavior: _Callable
                Pause: _Callable
                Resume: _Callable

            class IAnimationControllerStatics(IInspectable):
                get_MaxPlaybackRate: _Callable
                get_MinPlaybackRate: _Callable

            class IAnimationObject(IInspectable):
                PopulatePropertyInfo: _Callable

            class IAnimationPropertyInfo(IInspectable):
                get_AccessMode: _Callable
                put_AccessMode: _Callable

            class IAnimationPropertyInfo2(IInspectable):
                GetResolvedCompositionObject: _Callable
                GetResolvedCompositionObjectProperty: _Callable

            class IBackEasingFunction(IInspectable):
                get_Mode: _Callable
                get_Amplitude: _Callable

            class IBooleanKeyFrameAnimation(IInspectable):
                InsertKeyFrame: _Callable

            class IBounceEasingFunction(IInspectable):
                get_Mode: _Callable
                get_Bounces: _Callable
                get_Bounciness: _Callable

            class IBounceScalarNaturalMotionAnimation(IInspectable):
                get_Acceleration: _Callable
                put_Acceleration: _Callable
                get_Restitution: _Callable
                put_Restitution: _Callable

            class IBounceVector2NaturalMotionAnimation(IInspectable):
                get_Acceleration: _Callable
                put_Acceleration: _Callable
                get_Restitution: _Callable
                put_Restitution: _Callable

            class IBounceVector3NaturalMotionAnimation(IInspectable):
                get_Acceleration: _Callable
                put_Acceleration: _Callable
                get_Restitution: _Callable
                put_Restitution: _Callable

            class ICircleEasingFunction(IInspectable):
                get_Mode: _Callable

            class IColorKeyFrameAnimation(IInspectable):
                get_InterpolationColorSpace: _Callable
                put_InterpolationColorSpace: _Callable
                InsertKeyFrame: _Callable
                InsertKeyFrameWithEasingFunction: _Callable

            class ICompositionAnimation(IInspectable):
                ClearAllParameters: _Callable
                ClearParameter: _Callable
                SetColorParameter: _Callable
                SetMatrix3x2Parameter: _Callable
                SetMatrix4x4Parameter: _Callable
                SetQuaternionParameter: _Callable
                SetReferenceParameter: _Callable
                SetScalarParameter: _Callable
                SetVector2Parameter: _Callable
                SetVector3Parameter: _Callable
                SetVector4Parameter: _Callable

            class ICompositionAnimation2(IInspectable):
                SetBooleanParameter: _Callable
                get_Target: _Callable
                put_Target: _Callable

            class ICompositionAnimation3(IInspectable):
                get_InitialValueExpressions: _Callable

            class ICompositionAnimation4(IInspectable):
                SetExpressionReferenceParameter: _Callable

            class ICompositionAnimationBase(IInspectable):
                pass

            class ICompositionAnimationFactory(IInspectable):
                pass

            class ICompositionAnimationGroup(IInspectable):
                get_Count: _Callable
                Add: _Callable
                Remove: _Callable
                RemoveAll: _Callable

            class ICompositionBackdropBrush(IInspectable):
                pass

            class ICompositionBatchCompletedEventArgs(IInspectable):
                pass

            class ICompositionBrush(IInspectable):
                pass

            class ICompositionBrushFactory(IInspectable):
                pass

            class ICompositionCapabilities(IInspectable):
                AreEffectsSupported: _Callable
                AreEffectsFast: _Callable
                add_Changed: _Callable
                remove_Changed: _Callable

            class ICompositionCapabilitiesStatics(IInspectable):
                GetForCurrentView: _Callable

            class ICompositionClip(IInspectable):
                pass

            class ICompositionClip2(IInspectable):
                get_AnchorPoint: _Callable
                put_AnchorPoint: _Callable
                get_CenterPoint: _Callable
                put_CenterPoint: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_RotationAngle: _Callable
                put_RotationAngle: _Callable
                get_RotationAngleInDegrees: _Callable
                put_RotationAngleInDegrees: _Callable
                get_Scale: _Callable
                put_Scale: _Callable
                get_TransformMatrix: _Callable
                put_TransformMatrix: _Callable

            class ICompositionClipFactory(IInspectable):
                pass

            class ICompositionColorBrush(IInspectable):
                get_Color: _Callable
                put_Color: _Callable

            class ICompositionColorGradientStop(IInspectable):
                get_Color: _Callable
                put_Color: _Callable
                get_Offset: _Callable
                put_Offset: _Callable

            class ICompositionColorGradientStopCollection(IInspectable):
                pass

            class ICompositionCommitBatch(IInspectable):
                get_IsActive: _Callable
                get_IsEnded: _Callable
                add_Completed: _Callable
                remove_Completed: _Callable

            class ICompositionContainerShape(IInspectable):
                get_Shapes: _Callable

            class ICompositionDrawingSurface(IInspectable):
                get_AlphaMode: _Callable
                get_PixelFormat: _Callable
                get_Size: _Callable

            class ICompositionDrawingSurface2(IInspectable):
                get_SizeInt32: _Callable
                Resize: _Callable
                Scroll: _Callable
                ScrollRect: _Callable
                ScrollWithClip: _Callable
                ScrollRectWithClip: _Callable

            class ICompositionDrawingSurfaceFactory(IInspectable):
                pass

            class ICompositionEasingFunction(IInspectable):
                pass

            class ICompositionEasingFunctionFactory(IInspectable):
                pass

            class ICompositionEasingFunctionStatics(IInspectable):
                CreateCubicBezierEasingFunction: _Callable
                CreateLinearEasingFunction: _Callable
                CreateStepEasingFunction: _Callable
                CreateStepEasingFunctionWithStepCount: _Callable
                CreateBackEasingFunction: _Callable
                CreateBounceEasingFunction: _Callable
                CreateCircleEasingFunction: _Callable
                CreateElasticEasingFunction: _Callable
                CreateExponentialEasingFunction: _Callable
                CreatePowerEasingFunction: _Callable
                CreateSineEasingFunction: _Callable

            class ICompositionEffectBrush(IInspectable):
                GetSourceParameter: _Callable
                SetSourceParameter: _Callable

            class ICompositionEffectFactory(IInspectable):
                CreateBrush: _Callable
                get_ExtendedError: _Callable
                get_LoadStatus: _Callable

            class ICompositionEffectSourceParameter(IInspectable):
                get_Name: _Callable

            class ICompositionEffectSourceParameterFactory(IInspectable):
                Create: _Callable

            class ICompositionEllipseGeometry(IInspectable):
                get_Center: _Callable
                put_Center: _Callable
                get_Radius: _Callable
                put_Radius: _Callable

            class ICompositionGeometricClip(IInspectable):
                get_Geometry: _Callable
                put_Geometry: _Callable
                get_ViewBox: _Callable
                put_ViewBox: _Callable

            class ICompositionGeometry(IInspectable):
                get_TrimEnd: _Callable
                put_TrimEnd: _Callable
                get_TrimOffset: _Callable
                put_TrimOffset: _Callable
                get_TrimStart: _Callable
                put_TrimStart: _Callable

            class ICompositionGeometryFactory(IInspectable):
                pass

            class ICompositionGradientBrush(IInspectable):
                get_AnchorPoint: _Callable
                put_AnchorPoint: _Callable
                get_CenterPoint: _Callable
                put_CenterPoint: _Callable
                get_ColorStops: _Callable
                get_ExtendMode: _Callable
                put_ExtendMode: _Callable
                get_InterpolationSpace: _Callable
                put_InterpolationSpace: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_RotationAngle: _Callable
                put_RotationAngle: _Callable
                get_RotationAngleInDegrees: _Callable
                put_RotationAngleInDegrees: _Callable
                get_Scale: _Callable
                put_Scale: _Callable
                get_TransformMatrix: _Callable
                put_TransformMatrix: _Callable

            class ICompositionGradientBrush2(IInspectable):
                get_MappingMode: _Callable
                put_MappingMode: _Callable

            class ICompositionGradientBrushFactory(IInspectable):
                pass

            class ICompositionGraphicsDevice(IInspectable):
                CreateDrawingSurface: _Callable
                add_RenderingDeviceReplaced: _Callable
                remove_RenderingDeviceReplaced: _Callable

            class ICompositionGraphicsDevice2(IInspectable):
                CreateDrawingSurface2: _Callable
                CreateVirtualDrawingSurface: _Callable

            class ICompositionGraphicsDevice3(IInspectable):
                CreateMipmapSurface: _Callable
                Trim: _Callable

            class ICompositionGraphicsDevice4(IInspectable):
                CaptureAsync: _Callable

            class ICompositionLight(IInspectable):
                get_Targets: _Callable

            class ICompositionLight2(IInspectable):
                get_ExclusionsFromTargets: _Callable

            class ICompositionLight3(IInspectable):
                get_IsEnabled: _Callable
                put_IsEnabled: _Callable

            class ICompositionLightFactory(IInspectable):
                pass

            class ICompositionLineGeometry(IInspectable):
                get_Start: _Callable
                put_Start: _Callable
                get_End: _Callable
                put_End: _Callable

            class ICompositionLinearGradientBrush(IInspectable):
                get_EndPoint: _Callable
                put_EndPoint: _Callable
                get_StartPoint: _Callable
                put_StartPoint: _Callable

            class ICompositionMaskBrush(IInspectable):
                get_Mask: _Callable
                put_Mask: _Callable
                get_Source: _Callable
                put_Source: _Callable

            class ICompositionMipmapSurface(IInspectable):
                get_LevelCount: _Callable
                get_AlphaMode: _Callable
                get_PixelFormat: _Callable
                get_SizeInt32: _Callable
                GetDrawingSurfaceForLevel: _Callable

            class ICompositionNineGridBrush(IInspectable):
                get_BottomInset: _Callable
                put_BottomInset: _Callable
                get_BottomInsetScale: _Callable
                put_BottomInsetScale: _Callable
                get_IsCenterHollow: _Callable
                put_IsCenterHollow: _Callable
                get_LeftInset: _Callable
                put_LeftInset: _Callable
                get_LeftInsetScale: _Callable
                put_LeftInsetScale: _Callable
                get_RightInset: _Callable
                put_RightInset: _Callable
                get_RightInsetScale: _Callable
                put_RightInsetScale: _Callable
                get_Source: _Callable
                put_Source: _Callable
                get_TopInset: _Callable
                put_TopInset: _Callable
                get_TopInsetScale: _Callable
                put_TopInsetScale: _Callable
                SetInsets: _Callable
                SetInsetsWithValues: _Callable
                SetInsetScales: _Callable
                SetInsetScalesWithValues: _Callable

            class ICompositionObject(IInspectable):
                get_Compositor: _Callable
                get_Dispatcher: _Callable
                get_Properties: _Callable
                StartAnimation: _Callable
                StopAnimation: _Callable

            class ICompositionObject2(IInspectable):
                get_Comment: _Callable
                put_Comment: _Callable
                get_ImplicitAnimations: _Callable
                put_ImplicitAnimations: _Callable
                StartAnimationGroup: _Callable
                StopAnimationGroup: _Callable

            class ICompositionObject3(IInspectable):
                get_DispatcherQueue: _Callable

            class ICompositionObject4(IInspectable):
                TryGetAnimationController: _Callable

            class ICompositionObjectFactory(IInspectable):
                pass

            class ICompositionObjectStatics(IInspectable):
                StartAnimationWithIAnimationObject: _Callable
                StartAnimationGroupWithIAnimationObject: _Callable

            class ICompositionPath(IInspectable):
                pass

            class ICompositionPathFactory(IInspectable):
                Create: _Callable

            class ICompositionPathGeometry(IInspectable):
                get_Path: _Callable
                put_Path: _Callable

            class ICompositionProjectedShadow(IInspectable):
                get_BlurRadiusMultiplier: _Callable
                put_BlurRadiusMultiplier: _Callable
                get_Casters: _Callable
                get_LightSource: _Callable
                put_LightSource: _Callable
                get_MaxBlurRadius: _Callable
                put_MaxBlurRadius: _Callable
                get_MinBlurRadius: _Callable
                put_MinBlurRadius: _Callable
                get_Receivers: _Callable

            class ICompositionProjectedShadowCaster(IInspectable):
                get_Brush: _Callable
                put_Brush: _Callable
                get_CastingVisual: _Callable
                put_CastingVisual: _Callable

            class ICompositionProjectedShadowCasterCollection(IInspectable):
                get_Count: _Callable
                InsertAbove: _Callable
                InsertAtBottom: _Callable
                InsertAtTop: _Callable
                InsertBelow: _Callable
                Remove: _Callable
                RemoveAll: _Callable

            class ICompositionProjectedShadowCasterCollectionStatics(IInspectable):
                get_MaxRespectedCasters: _Callable

            class ICompositionProjectedShadowReceiver(IInspectable):
                get_ReceivingVisual: _Callable
                put_ReceivingVisual: _Callable

            class ICompositionProjectedShadowReceiverUnorderedCollection(IInspectable):
                Add: _Callable
                get_Count: _Callable
                Remove: _Callable
                RemoveAll: _Callable

            class ICompositionPropertySet(IInspectable):
                InsertColor: _Callable
                InsertMatrix3x2: _Callable
                InsertMatrix4x4: _Callable
                InsertQuaternion: _Callable
                InsertScalar: _Callable
                InsertVector2: _Callable
                InsertVector3: _Callable
                InsertVector4: _Callable
                TryGetColor: _Callable
                TryGetMatrix3x2: _Callable
                TryGetMatrix4x4: _Callable
                TryGetQuaternion: _Callable
                TryGetScalar: _Callable
                TryGetVector2: _Callable
                TryGetVector3: _Callable
                TryGetVector4: _Callable

            class ICompositionPropertySet2(IInspectable):
                InsertBoolean: _Callable
                TryGetBoolean: _Callable

            class ICompositionRadialGradientBrush(IInspectable):
                get_EllipseCenter: _Callable
                put_EllipseCenter: _Callable
                get_EllipseRadius: _Callable
                put_EllipseRadius: _Callable
                get_GradientOriginOffset: _Callable
                put_GradientOriginOffset: _Callable

            class ICompositionRectangleGeometry(IInspectable):
                get_Offset: _Callable
                put_Offset: _Callable
                get_Size: _Callable
                put_Size: _Callable

            class ICompositionRoundedRectangleGeometry(IInspectable):
                get_CornerRadius: _Callable
                put_CornerRadius: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_Size: _Callable
                put_Size: _Callable

            class ICompositionScopedBatch(IInspectable):
                get_IsActive: _Callable
                get_IsEnded: _Callable
                End: _Callable
                Resume: _Callable
                Suspend: _Callable
                add_Completed: _Callable
                remove_Completed: _Callable

            class ICompositionShadow(IInspectable):
                pass

            class ICompositionShadowFactory(IInspectable):
                pass

            class ICompositionShape(IInspectable):
                get_CenterPoint: _Callable
                put_CenterPoint: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_RotationAngle: _Callable
                put_RotationAngle: _Callable
                get_RotationAngleInDegrees: _Callable
                put_RotationAngleInDegrees: _Callable
                get_Scale: _Callable
                put_Scale: _Callable
                get_TransformMatrix: _Callable
                put_TransformMatrix: _Callable

            class ICompositionShapeFactory(IInspectable):
                pass

            class ICompositionSpriteShape(IInspectable):
                get_FillBrush: _Callable
                put_FillBrush: _Callable
                get_Geometry: _Callable
                put_Geometry: _Callable
                get_IsStrokeNonScaling: _Callable
                put_IsStrokeNonScaling: _Callable
                get_StrokeBrush: _Callable
                put_StrokeBrush: _Callable
                get_StrokeDashArray: _Callable
                get_StrokeDashCap: _Callable
                put_StrokeDashCap: _Callable
                get_StrokeDashOffset: _Callable
                put_StrokeDashOffset: _Callable
                get_StrokeEndCap: _Callable
                put_StrokeEndCap: _Callable
                get_StrokeLineJoin: _Callable
                put_StrokeLineJoin: _Callable
                get_StrokeMiterLimit: _Callable
                put_StrokeMiterLimit: _Callable
                get_StrokeStartCap: _Callable
                put_StrokeStartCap: _Callable
                get_StrokeThickness: _Callable
                put_StrokeThickness: _Callable

            class ICompositionSupportsSystemBackdrop(IInspectable):
                get_SystemBackdrop: _Callable
                put_SystemBackdrop: _Callable

            class ICompositionSurface(IInspectable):
                pass

            class ICompositionSurfaceBrush(IInspectable):
                get_BitmapInterpolationMode: _Callable
                put_BitmapInterpolationMode: _Callable
                get_HorizontalAlignmentRatio: _Callable
                put_HorizontalAlignmentRatio: _Callable
                get_Stretch: _Callable
                put_Stretch: _Callable
                get_Surface: _Callable
                put_Surface: _Callable
                get_VerticalAlignmentRatio: _Callable
                put_VerticalAlignmentRatio: _Callable

            class ICompositionSurfaceBrush2(IInspectable):
                get_AnchorPoint: _Callable
                put_AnchorPoint: _Callable
                get_CenterPoint: _Callable
                put_CenterPoint: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_RotationAngle: _Callable
                put_RotationAngle: _Callable
                get_RotationAngleInDegrees: _Callable
                put_RotationAngleInDegrees: _Callable
                get_Scale: _Callable
                put_Scale: _Callable
                get_TransformMatrix: _Callable
                put_TransformMatrix: _Callable

            class ICompositionSurfaceBrush3(IInspectable):
                get_SnapToPixels: _Callable
                put_SnapToPixels: _Callable

            class ICompositionSurfaceFacade(IInspectable):
                GetRealSurface: _Callable

            class ICompositionTarget(IInspectable):
                get_Root: _Callable
                put_Root: _Callable

            class ICompositionTargetFactory(IInspectable):
                pass

            class ICompositionTransform(IInspectable):
                pass

            class ICompositionTransformFactory(IInspectable):
                pass

            class ICompositionViewBox(IInspectable):
                get_HorizontalAlignmentRatio: _Callable
                put_HorizontalAlignmentRatio: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_Size: _Callable
                put_Size: _Callable
                get_Stretch: _Callable
                put_Stretch: _Callable
                get_VerticalAlignmentRatio: _Callable
                put_VerticalAlignmentRatio: _Callable

            class ICompositionVirtualDrawingSurface(IInspectable):
                Trim: _Callable

            class ICompositionVirtualDrawingSurfaceFactory(IInspectable):
                pass

            class ICompositionVisualSurface(IInspectable):
                get_SourceVisual: _Callable
                put_SourceVisual: _Callable
                get_SourceOffset: _Callable
                put_SourceOffset: _Callable
                get_SourceSize: _Callable
                put_SourceSize: _Callable

            class ICompositor(IInspectable):
                CreateColorKeyFrameAnimation: _Callable
                CreateColorBrush: _Callable
                CreateColorBrushWithColor: _Callable
                CreateContainerVisual: _Callable
                CreateCubicBezierEasingFunction: _Callable
                CreateEffectFactory: _Callable
                CreateEffectFactoryWithProperties: _Callable
                CreateExpressionAnimation: _Callable
                CreateExpressionAnimationWithExpression: _Callable
                CreateInsetClip: _Callable
                CreateInsetClipWithInsets: _Callable
                CreateLinearEasingFunction: _Callable
                CreatePropertySet: _Callable
                CreateQuaternionKeyFrameAnimation: _Callable
                CreateScalarKeyFrameAnimation: _Callable
                CreateScopedBatch: _Callable
                CreateSpriteVisual: _Callable
                CreateSurfaceBrush: _Callable
                CreateSurfaceBrushWithSurface: _Callable
                CreateTargetForCurrentView: _Callable
                CreateVector2KeyFrameAnimation: _Callable
                CreateVector3KeyFrameAnimation: _Callable
                CreateVector4KeyFrameAnimation: _Callable
                GetCommitBatch: _Callable

            class ICompositor2(IInspectable):
                CreateAmbientLight: _Callable
                CreateAnimationGroup: _Callable
                CreateBackdropBrush: _Callable
                CreateDistantLight: _Callable
                CreateDropShadow: _Callable
                CreateImplicitAnimationCollection: _Callable
                CreateLayerVisual: _Callable
                CreateMaskBrush: _Callable
                CreateNineGridBrush: _Callable
                CreatePointLight: _Callable
                CreateSpotLight: _Callable
                CreateStepEasingFunction: _Callable
                CreateStepEasingFunctionWithStepCount: _Callable

            class ICompositor3(IInspectable):
                CreateHostBackdropBrush: _Callable

            class ICompositor4(IInspectable):
                CreateColorGradientStop: _Callable
                CreateColorGradientStopWithOffsetAndColor: _Callable
                CreateLinearGradientBrush: _Callable
                CreateSpringScalarAnimation: _Callable
                CreateSpringVector2Animation: _Callable
                CreateSpringVector3Animation: _Callable

            class ICompositor5(IInspectable):
                get_Comment: _Callable
                put_Comment: _Callable
                get_GlobalPlaybackRate: _Callable
                put_GlobalPlaybackRate: _Callable
                CreateBounceScalarAnimation: _Callable
                CreateBounceVector2Animation: _Callable
                CreateBounceVector3Animation: _Callable
                CreateContainerShape: _Callable
                CreateEllipseGeometry: _Callable
                CreateLineGeometry: _Callable
                CreatePathGeometry: _Callable
                CreatePathGeometryWithPath: _Callable
                CreatePathKeyFrameAnimation: _Callable
                CreateRectangleGeometry: _Callable
                CreateRoundedRectangleGeometry: _Callable
                CreateShapeVisual: _Callable
                CreateSpriteShape: _Callable
                CreateSpriteShapeWithGeometry: _Callable
                CreateViewBox: _Callable
                RequestCommitAsync: _Callable

            class ICompositor6(IInspectable):
                CreateGeometricClip: _Callable
                CreateGeometricClipWithGeometry: _Callable
                CreateRedirectVisual: _Callable
                CreateRedirectVisualWithSourceVisual: _Callable
                CreateBooleanKeyFrameAnimation: _Callable

            class ICompositor7(IInspectable):
                get_DispatcherQueue: _Callable
                CreateAnimationPropertyInfo: _Callable
                CreateRectangleClip: _Callable
                CreateRectangleClipWithSides: _Callable
                CreateRectangleClipWithSidesAndRadius: _Callable

            class ICompositorStatics(IInspectable):
                get_MaxGlobalPlaybackRate: _Callable
                get_MinGlobalPlaybackRate: _Callable

            class ICompositorWithBlurredWallpaperBackdropBrush(IInspectable):
                TryCreateBlurredWallpaperBackdropBrush: _Callable

            class ICompositorWithProjectedShadow(IInspectable):
                CreateProjectedShadowCaster: _Callable
                CreateProjectedShadow: _Callable
                CreateProjectedShadowReceiver: _Callable

            class ICompositorWithRadialGradient(IInspectable):
                CreateRadialGradientBrush: _Callable

            class ICompositorWithVisualSurface(IInspectable):
                CreateVisualSurface: _Callable

            class IContainerVisual(IInspectable):
                get_Children: _Callable

            class IContainerVisualFactory(IInspectable):
                pass

            class ICubicBezierEasingFunction(IInspectable):
                get_ControlPoint1: _Callable
                get_ControlPoint2: _Callable

            class IDelegatedInkTrailVisual(IInspectable):
                AddTrailPoints: _Callable
                AddTrailPointsWithPrediction: _Callable
                RemoveTrailPoints: _Callable
                StartNewTrail: _Callable

            class IDelegatedInkTrailVisualStatics(IInspectable):
                Create: _Callable
                CreateForSwapChain: _Callable

            class IDistantLight(IInspectable):
                get_Color: _Callable
                put_Color: _Callable
                get_CoordinateSpace: _Callable
                put_CoordinateSpace: _Callable
                get_Direction: _Callable
                put_Direction: _Callable

            class IDistantLight2(IInspectable):
                get_Intensity: _Callable
                put_Intensity: _Callable

            class IDropShadow(IInspectable):
                get_BlurRadius: _Callable
                put_BlurRadius: _Callable
                get_Color: _Callable
                put_Color: _Callable
                get_Mask: _Callable
                put_Mask: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_Opacity: _Callable
                put_Opacity: _Callable

            class IDropShadow2(IInspectable):
                get_SourcePolicy: _Callable
                put_SourcePolicy: _Callable

            class IElasticEasingFunction(IInspectable):
                get_Mode: _Callable
                get_Oscillations: _Callable
                get_Springiness: _Callable

            class IExponentialEasingFunction(IInspectable):
                get_Mode: _Callable
                get_Exponent: _Callable

            class IExpressionAnimation(IInspectable):
                get_Expression: _Callable
                put_Expression: _Callable

            class IImplicitAnimationCollection(IInspectable):
                pass

            class IInsetClip(IInspectable):
                get_BottomInset: _Callable
                put_BottomInset: _Callable
                get_LeftInset: _Callable
                put_LeftInset: _Callable
                get_RightInset: _Callable
                put_RightInset: _Callable
                get_TopInset: _Callable
                put_TopInset: _Callable

            class IKeyFrameAnimation(IInspectable):
                get_DelayTime: _Callable
                put_DelayTime: _Callable
                get_Duration: _Callable
                put_Duration: _Callable
                get_IterationBehavior: _Callable
                put_IterationBehavior: _Callable
                get_IterationCount: _Callable
                put_IterationCount: _Callable
                get_KeyFrameCount: _Callable
                get_StopBehavior: _Callable
                put_StopBehavior: _Callable
                InsertExpressionKeyFrame: _Callable
                InsertExpressionKeyFrameWithEasingFunction: _Callable

            class IKeyFrameAnimation2(IInspectable):
                get_Direction: _Callable
                put_Direction: _Callable

            class IKeyFrameAnimation3(IInspectable):
                get_DelayBehavior: _Callable
                put_DelayBehavior: _Callable

            class IKeyFrameAnimationFactory(IInspectable):
                pass

            class ILayerVisual(IInspectable):
                get_Effect: _Callable
                put_Effect: _Callable

            class ILayerVisual2(IInspectable):
                get_Shadow: _Callable
                put_Shadow: _Callable

            class ILinearEasingFunction(IInspectable):
                pass

            class INaturalMotionAnimation(IInspectable):
                get_DelayBehavior: _Callable
                put_DelayBehavior: _Callable
                get_DelayTime: _Callable
                put_DelayTime: _Callable
                get_StopBehavior: _Callable
                put_StopBehavior: _Callable

            class INaturalMotionAnimationFactory(IInspectable):
                pass

            class IPathKeyFrameAnimation(IInspectable):
                InsertKeyFrame: _Callable
                InsertKeyFrameWithEasingFunction: _Callable

            class IPointLight(IInspectable):
                get_Color: _Callable
                put_Color: _Callable
                get_ConstantAttenuation: _Callable
                put_ConstantAttenuation: _Callable
                get_CoordinateSpace: _Callable
                put_CoordinateSpace: _Callable
                get_LinearAttenuation: _Callable
                put_LinearAttenuation: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_QuadraticAttenuation: _Callable
                put_QuadraticAttenuation: _Callable

            class IPointLight2(IInspectable):
                get_Intensity: _Callable
                put_Intensity: _Callable

            class IPointLight3(IInspectable):
                get_MinAttenuationCutoff: _Callable
                put_MinAttenuationCutoff: _Callable
                get_MaxAttenuationCutoff: _Callable
                put_MaxAttenuationCutoff: _Callable

            class IPowerEasingFunction(IInspectable):
                get_Mode: _Callable
                get_Power: _Callable

            class IQuaternionKeyFrameAnimation(IInspectable):
                InsertKeyFrame: _Callable
                InsertKeyFrameWithEasingFunction: _Callable

            class IRectangleClip(IInspectable):
                get_Bottom: _Callable
                put_Bottom: _Callable
                get_BottomLeftRadius: _Callable
                put_BottomLeftRadius: _Callable
                get_BottomRightRadius: _Callable
                put_BottomRightRadius: _Callable
                get_Left: _Callable
                put_Left: _Callable
                get_Right: _Callable
                put_Right: _Callable
                get_Top: _Callable
                put_Top: _Callable
                get_TopLeftRadius: _Callable
                put_TopLeftRadius: _Callable
                get_TopRightRadius: _Callable
                put_TopRightRadius: _Callable

            class IRedirectVisual(IInspectable):
                get_Source: _Callable
                put_Source: _Callable

            class IRenderingDeviceReplacedEventArgs(IInspectable):
                get_GraphicsDevice: _Callable

            class IScalarKeyFrameAnimation(IInspectable):
                InsertKeyFrame: _Callable
                InsertKeyFrameWithEasingFunction: _Callable

            class IScalarNaturalMotionAnimation(IInspectable):
                get_FinalValue: _Callable
                put_FinalValue: _Callable
                get_InitialValue: _Callable
                put_InitialValue: _Callable
                get_InitialVelocity: _Callable
                put_InitialVelocity: _Callable

            class IScalarNaturalMotionAnimationFactory(IInspectable):
                pass

            class IShapeVisual(IInspectable):
                get_Shapes: _Callable
                get_ViewBox: _Callable
                put_ViewBox: _Callable

            class ISineEasingFunction(IInspectable):
                get_Mode: _Callable

            class ISpotLight(IInspectable):
                get_ConstantAttenuation: _Callable
                put_ConstantAttenuation: _Callable
                get_CoordinateSpace: _Callable
                put_CoordinateSpace: _Callable
                get_Direction: _Callable
                put_Direction: _Callable
                get_InnerConeAngle: _Callable
                put_InnerConeAngle: _Callable
                get_InnerConeAngleInDegrees: _Callable
                put_InnerConeAngleInDegrees: _Callable
                get_InnerConeColor: _Callable
                put_InnerConeColor: _Callable
                get_LinearAttenuation: _Callable
                put_LinearAttenuation: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_OuterConeAngle: _Callable
                put_OuterConeAngle: _Callable
                get_OuterConeAngleInDegrees: _Callable
                put_OuterConeAngleInDegrees: _Callable
                get_OuterConeColor: _Callable
                put_OuterConeColor: _Callable
                get_QuadraticAttenuation: _Callable
                put_QuadraticAttenuation: _Callable

            class ISpotLight2(IInspectable):
                get_InnerConeIntensity: _Callable
                put_InnerConeIntensity: _Callable
                get_OuterConeIntensity: _Callable
                put_OuterConeIntensity: _Callable

            class ISpotLight3(IInspectable):
                get_MinAttenuationCutoff: _Callable
                put_MinAttenuationCutoff: _Callable
                get_MaxAttenuationCutoff: _Callable
                put_MaxAttenuationCutoff: _Callable

            class ISpringScalarNaturalMotionAnimation(IInspectable):
                get_DampingRatio: _Callable
                put_DampingRatio: _Callable
                get_Period: _Callable
                put_Period: _Callable

            class ISpringVector2NaturalMotionAnimation(IInspectable):
                get_DampingRatio: _Callable
                put_DampingRatio: _Callable
                get_Period: _Callable
                put_Period: _Callable

            class ISpringVector3NaturalMotionAnimation(IInspectable):
                get_DampingRatio: _Callable
                put_DampingRatio: _Callable
                get_Period: _Callable
                put_Period: _Callable

            class ISpriteVisual(IInspectable):
                get_Brush: _Callable
                put_Brush: _Callable

            class ISpriteVisual2(IInspectable):
                get_Shadow: _Callable
                put_Shadow: _Callable

            class IStepEasingFunction(IInspectable):
                get_FinalStep: _Callable
                put_FinalStep: _Callable
                get_InitialStep: _Callable
                put_InitialStep: _Callable
                get_IsFinalStepSingleFrame: _Callable
                put_IsFinalStepSingleFrame: _Callable
                get_IsInitialStepSingleFrame: _Callable
                put_IsInitialStepSingleFrame: _Callable
                get_StepCount: _Callable
                put_StepCount: _Callable

            class IVector2KeyFrameAnimation(IInspectable):
                InsertKeyFrame: _Callable
                InsertKeyFrameWithEasingFunction: _Callable

            class IVector2NaturalMotionAnimation(IInspectable):
                get_FinalValue: _Callable
                put_FinalValue: _Callable
                get_InitialValue: _Callable
                put_InitialValue: _Callable
                get_InitialVelocity: _Callable
                put_InitialVelocity: _Callable

            class IVector2NaturalMotionAnimationFactory(IInspectable):
                pass

            class IVector3KeyFrameAnimation(IInspectable):
                InsertKeyFrame: _Callable
                InsertKeyFrameWithEasingFunction: _Callable

            class IVector3NaturalMotionAnimation(IInspectable):
                get_FinalValue: _Callable
                put_FinalValue: _Callable
                get_InitialValue: _Callable
                put_InitialValue: _Callable
                get_InitialVelocity: _Callable
                put_InitialVelocity: _Callable

            class IVector3NaturalMotionAnimationFactory(IInspectable):
                pass

            class IVector4KeyFrameAnimation(IInspectable):
                InsertKeyFrame: _Callable
                InsertKeyFrameWithEasingFunction: _Callable

            class IVisual(IInspectable):
                get_AnchorPoint: _Callable
                put_AnchorPoint: _Callable
                get_BackfaceVisibility: _Callable
                put_BackfaceVisibility: _Callable
                get_BorderMode: _Callable
                put_BorderMode: _Callable
                get_CenterPoint: _Callable
                put_CenterPoint: _Callable
                get_Clip: _Callable
                put_Clip: _Callable
                get_CompositeMode: _Callable
                put_CompositeMode: _Callable
                get_IsVisible: _Callable
                put_IsVisible: _Callable
                get_Offset: _Callable
                put_Offset: _Callable
                get_Opacity: _Callable
                put_Opacity: _Callable
                get_Orientation: _Callable
                put_Orientation: _Callable
                get_Parent: _Callable
                get_RotationAngle: _Callable
                put_RotationAngle: _Callable
                get_RotationAngleInDegrees: _Callable
                put_RotationAngleInDegrees: _Callable
                get_RotationAxis: _Callable
                put_RotationAxis: _Callable
                get_Scale: _Callable
                put_Scale: _Callable
                get_Size: _Callable
                put_Size: _Callable
                get_TransformMatrix: _Callable
                put_TransformMatrix: _Callable

            class IVisual2(IInspectable):
                get_ParentForTransform: _Callable
                put_ParentForTransform: _Callable
                get_RelativeOffsetAdjustment: _Callable
                put_RelativeOffsetAdjustment: _Callable
                get_RelativeSizeAdjustment: _Callable
                put_RelativeSizeAdjustment: _Callable

            class IVisual3(IInspectable):
                get_IsHitTestVisible: _Callable
                put_IsHitTestVisible: _Callable

            class IVisual4(IInspectable):
                get_IsPixelSnappingEnabled: _Callable
                put_IsPixelSnappingEnabled: _Callable

            class IVisualCollection(IInspectable):
                get_Count: _Callable
                InsertAbove: _Callable
                InsertAtBottom: _Callable
                InsertAtTop: _Callable
                InsertBelow: _Callable
                Remove: _Callable
                RemoveAll: _Callable

            class IVisualElement(IInspectable):
                pass

            class IVisualElement2(IInspectable):
                GetVisualInternal: _Callable

            class IVisualFactory(IInspectable):
                pass

            class IVisualUnorderedCollection(IInspectable):
                get_Count: _Callable
                Add: _Callable
                Remove: _Callable
                RemoveAll: _Callable

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

        class Shell:
            class IAdaptiveCard(IInspectable):
                ToJson: _Callable

            class IAdaptiveCardBuilderStatics(IInspectable):
                CreateAdaptiveCardFromJson: _Callable

            class ISecurityAppManager(IInspectable):
                Register: _Callable
                Unregister: _Callable
                UpdateState: _Callable

            class IShareWindowCommandEventArgs(IInspectable):
                get_WindowId: _Callable
                get_Command: _Callable
                put_Command: _Callable

            class IShareWindowCommandSource(IInspectable):
                Start: _Callable
                Stop: _Callable
                ReportCommandChanged: _Callable
                add_CommandRequested: _Callable
                remove_CommandRequested: _Callable
                add_CommandInvoked: _Callable
                remove_CommandInvoked: _Callable

            class IShareWindowCommandSourceStatics(IInspectable):
                GetForCurrentView: _Callable

            class ITaskbarManager(IInspectable):
                get_IsSupported: _Callable
                get_IsPinningAllowed: _Callable
                IsCurrentAppPinnedAsync: _Callable
                IsAppListEntryPinnedAsync: _Callable
                RequestPinCurrentAppAsync: _Callable
                RequestPinAppListEntryAsync: _Callable

            class ITaskbarManager2(IInspectable):
                IsSecondaryTilePinnedAsync: _Callable
                RequestPinSecondaryTileAsync: _Callable
                TryUnpinSecondaryTileAsync: _Callable

            class ITaskbarManagerStatics(IInspectable):
                GetDefault: _Callable

        class StartScreen:
            class IJumpList(IInspectable):
                get_Items: _Callable
                get_SystemGroupKind: _Callable
                put_SystemGroupKind: _Callable
                SaveAsync: _Callable

            class IJumpListItem(IInspectable):
                get_Kind: _Callable
                get_Arguments: _Callable
                get_RemovedByUser: _Callable
                get_Description: _Callable
                put_Description: _Callable
                get_DisplayName: _Callable
                put_DisplayName: _Callable
                get_GroupName: _Callable
                put_GroupName: _Callable
                get_Logo: _Callable
                put_Logo: _Callable

            class IJumpListItemStatics(IInspectable):
                CreateWithArguments: _Callable
                CreateSeparator: _Callable

            class IJumpListStatics(IInspectable):
                LoadCurrentAsync: _Callable
                IsSupported: _Callable

            class ISecondaryTile(IInspectable):
                put_TileId: _Callable
                get_TileId: _Callable
                put_Arguments: _Callable
                get_Arguments: _Callable
                put_ShortName: _Callable
                get_ShortName: _Callable
                put_DisplayName: _Callable
                get_DisplayName: _Callable
                put_Logo: _Callable
                get_Logo: _Callable
                put_SmallLogo: _Callable
                get_SmallLogo: _Callable
                put_WideLogo: _Callable
                get_WideLogo: _Callable
                put_LockScreenBadgeLogo: _Callable
                get_LockScreenBadgeLogo: _Callable
                put_LockScreenDisplayBadgeAndTileText: _Callable
                get_LockScreenDisplayBadgeAndTileText: _Callable
                put_TileOptions: _Callable
                get_TileOptions: _Callable
                put_ForegroundText: _Callable
                get_ForegroundText: _Callable
                put_BackgroundColor: _Callable
                get_BackgroundColor: _Callable
                RequestCreateAsync: _Callable
                RequestCreateAsyncWithPoint: _Callable
                RequestCreateAsyncWithRect: _Callable
                RequestCreateAsyncWithRectAndPlacement: _Callable
                RequestDeleteAsync: _Callable
                RequestDeleteAsyncWithPoint: _Callable
                RequestDeleteAsyncWithRect: _Callable
                RequestDeleteAsyncWithRectAndPlacement: _Callable
                UpdateAsync: _Callable

            class ISecondaryTile2(IInspectable):
                put_PhoneticName: _Callable
                get_PhoneticName: _Callable
                get_VisualElements: _Callable
                put_RoamingEnabled: _Callable
                get_RoamingEnabled: _Callable
                add_VisualElementsRequested: _Callable
                remove_VisualElementsRequested: _Callable

            class ISecondaryTileFactory(IInspectable):
                CreateTile: _Callable
                CreateWideTile: _Callable
                CreateWithId: _Callable

            class ISecondaryTileFactory2(IInspectable):
                CreateMinimalTile: _Callable

            class ISecondaryTileStatics(IInspectable):
                Exists: _Callable
                FindAllAsync: _Callable
                FindAllForApplicationAsync: _Callable
                FindAllForPackageAsync: _Callable

            class ISecondaryTileVisualElements(IInspectable):
                put_Square30x30Logo: _Callable
                get_Square30x30Logo: _Callable
                put_Square70x70Logo: _Callable
                get_Square70x70Logo: _Callable
                put_Square150x150Logo: _Callable
                get_Square150x150Logo: _Callable
                put_Wide310x150Logo: _Callable
                get_Wide310x150Logo: _Callable
                put_Square310x310Logo: _Callable
                get_Square310x310Logo: _Callable
                put_ForegroundText: _Callable
                get_ForegroundText: _Callable
                put_BackgroundColor: _Callable
                get_BackgroundColor: _Callable
                put_ShowNameOnSquare150x150Logo: _Callable
                get_ShowNameOnSquare150x150Logo: _Callable
                put_ShowNameOnWide310x150Logo: _Callable
                get_ShowNameOnWide310x150Logo: _Callable
                put_ShowNameOnSquare310x310Logo: _Callable
                get_ShowNameOnSquare310x310Logo: _Callable

            class ISecondaryTileVisualElements2(IInspectable):
                put_Square71x71Logo: _Callable
                get_Square71x71Logo: _Callable

            class ISecondaryTileVisualElements3(IInspectable):
                put_Square44x44Logo: _Callable
                get_Square44x44Logo: _Callable

            class ISecondaryTileVisualElements4(IInspectable):
                get_MixedRealityModel: _Callable

            class IStartScreenManager(IInspectable):
                get_User: _Callable
                SupportsAppListEntry: _Callable
                ContainsAppListEntryAsync: _Callable
                RequestAddAppListEntryAsync: _Callable

            class IStartScreenManager2(IInspectable):
                ContainsSecondaryTileAsync: _Callable
                TryRemoveSecondaryTileAsync: _Callable

            class IStartScreenManagerStatics(IInspectable):
                GetDefault: _Callable
                GetForUser: _Callable

            class ITileMixedRealityModel(IInspectable):
                put_Uri: _Callable
                get_Uri: _Callable
                put_BoundingBox: _Callable
                get_BoundingBox: _Callable

            class ITileMixedRealityModel2(IInspectable):
                put_ActivationBehavior: _Callable
                get_ActivationBehavior: _Callable

            class IVisualElementsRequest(IInspectable):
                get_VisualElements: _Callable
                get_AlternateVisualElements: _Callable
                get_Deadline: _Callable
                GetDeferral: _Callable

            class IVisualElementsRequestDeferral(IInspectable):
                Complete: _Callable

            class IVisualElementsRequestedEventArgs(IInspectable):
                get_Request: _Callable

        class Text:
            class IContentLinkInfo(IInspectable):
                get_Id: _Callable
                put_Id: _Callable
                get_DisplayText: _Callable
                put_DisplayText: _Callable
                get_SecondaryText: _Callable
                put_SecondaryText: _Callable
                get_Uri: _Callable
                put_Uri: _Callable
                get_LinkContentKind: _Callable
                put_LinkContentKind: _Callable

            class IFontWeights(IInspectable):
                pass

            class IFontWeightsStatics(IInspectable):
                get_Black: _Callable
                get_Bold: _Callable
                get_ExtraBlack: _Callable
                get_ExtraBold: _Callable
                get_ExtraLight: _Callable
                get_Light: _Callable
                get_Medium: _Callable
                get_Normal: _Callable
                get_SemiBold: _Callable
                get_SemiLight: _Callable
                get_Thin: _Callable

            class IRichEditTextRange(IInspectable):
                get_ContentLinkInfo: _Callable
                put_ContentLinkInfo: _Callable

            class ITextCharacterFormat(IInspectable):
                get_AllCaps: _Callable
                put_AllCaps: _Callable
                get_BackgroundColor: _Callable
                put_BackgroundColor: _Callable
                get_Bold: _Callable
                put_Bold: _Callable
                get_FontStretch: _Callable
                put_FontStretch: _Callable
                get_FontStyle: _Callable
                put_FontStyle: _Callable
                get_ForegroundColor: _Callable
                put_ForegroundColor: _Callable
                get_Hidden: _Callable
                put_Hidden: _Callable
                get_Italic: _Callable
                put_Italic: _Callable
                get_Kerning: _Callable
                put_Kerning: _Callable
                get_LanguageTag: _Callable
                put_LanguageTag: _Callable
                get_LinkType: _Callable
                get_Name: _Callable
                put_Name: _Callable
                get_Outline: _Callable
                put_Outline: _Callable
                get_Position: _Callable
                put_Position: _Callable
                get_ProtectedText: _Callable
                put_ProtectedText: _Callable
                get_Size: _Callable
                put_Size: _Callable
                get_SmallCaps: _Callable
                put_SmallCaps: _Callable
                get_Spacing: _Callable
                put_Spacing: _Callable
                get_Strikethrough: _Callable
                put_Strikethrough: _Callable
                get_Subscript: _Callable
                put_Subscript: _Callable
                get_Superscript: _Callable
                put_Superscript: _Callable
                get_TextScript: _Callable
                put_TextScript: _Callable
                get_Underline: _Callable
                put_Underline: _Callable
                get_Weight: _Callable
                put_Weight: _Callable
                SetClone: _Callable
                GetClone: _Callable
                IsEqual: _Callable

            class ITextConstantsStatics(IInspectable):
                get_AutoColor: _Callable
                get_MinUnitCount: _Callable
                get_MaxUnitCount: _Callable
                get_UndefinedColor: _Callable
                get_UndefinedFloatValue: _Callable
                get_UndefinedInt32Value: _Callable
                get_UndefinedFontStretch: _Callable
                get_UndefinedFontStyle: _Callable

            class ITextDocument(IInspectable):
                get_CaretType: _Callable
                put_CaretType: _Callable
                get_DefaultTabStop: _Callable
                put_DefaultTabStop: _Callable
                get_Selection: _Callable
                get_UndoLimit: _Callable
                put_UndoLimit: _Callable
                CanCopy: _Callable
                CanPaste: _Callable
                CanRedo: _Callable
                CanUndo: _Callable
                ApplyDisplayUpdates: _Callable
                BatchDisplayUpdates: _Callable
                BeginUndoGroup: _Callable
                EndUndoGroup: _Callable
                GetDefaultCharacterFormat: _Callable
                GetDefaultParagraphFormat: _Callable
                GetRange: _Callable
                GetRangeFromPoint: _Callable
                GetText: _Callable
                LoadFromStream: _Callable
                Redo: _Callable
                SaveToStream: _Callable
                SetDefaultCharacterFormat: _Callable
                SetDefaultParagraphFormat: _Callable
                SetText: _Callable
                Undo: _Callable

            class ITextDocument2(IInspectable):
                get_AlignmentIncludesTrailingWhitespace: _Callable
                put_AlignmentIncludesTrailingWhitespace: _Callable
                get_IgnoreTrailingCharacterSpacing: _Callable
                put_IgnoreTrailingCharacterSpacing: _Callable

            class ITextDocument3(IInspectable):
                ClearUndoRedoHistory: _Callable

            class ITextDocument4(IInspectable):
                SetMath: _Callable
                GetMath: _Callable
                SetMathMode: _Callable

            class ITextParagraphFormat(IInspectable):
                get_Alignment: _Callable
                put_Alignment: _Callable
                get_FirstLineIndent: _Callable
                get_KeepTogether: _Callable
                put_KeepTogether: _Callable
                get_KeepWithNext: _Callable
                put_KeepWithNext: _Callable
                get_LeftIndent: _Callable
                get_LineSpacing: _Callable
                get_LineSpacingRule: _Callable
                get_ListAlignment: _Callable
                put_ListAlignment: _Callable
                get_ListLevelIndex: _Callable
                put_ListLevelIndex: _Callable
                get_ListStart: _Callable
                put_ListStart: _Callable
                get_ListStyle: _Callable
                put_ListStyle: _Callable
                get_ListTab: _Callable
                put_ListTab: _Callable
                get_ListType: _Callable
                put_ListType: _Callable
                get_NoLineNumber: _Callable
                put_NoLineNumber: _Callable
                get_PageBreakBefore: _Callable
                put_PageBreakBefore: _Callable
                get_RightIndent: _Callable
                put_RightIndent: _Callable
                get_RightToLeft: _Callable
                put_RightToLeft: _Callable
                get_Style: _Callable
                put_Style: _Callable
                get_SpaceAfter: _Callable
                put_SpaceAfter: _Callable
                get_SpaceBefore: _Callable
                put_SpaceBefore: _Callable
                get_WidowControl: _Callable
                put_WidowControl: _Callable
                get_TabCount: _Callable
                AddTab: _Callable
                ClearAllTabs: _Callable
                DeleteTab: _Callable
                GetClone: _Callable
                GetTab: _Callable
                IsEqual: _Callable
                SetClone: _Callable
                SetIndents: _Callable
                SetLineSpacing: _Callable

            class ITextRange(IInspectable):
                get_Character: _Callable
                put_Character: _Callable
                get_CharacterFormat: _Callable
                put_CharacterFormat: _Callable
                get_FormattedText: _Callable
                put_FormattedText: _Callable
                get_EndPosition: _Callable
                put_EndPosition: _Callable
                get_Gravity: _Callable
                put_Gravity: _Callable
                get_Length: _Callable
                get_Link: _Callable
                put_Link: _Callable
                get_ParagraphFormat: _Callable
                put_ParagraphFormat: _Callable
                get_StartPosition: _Callable
                put_StartPosition: _Callable
                get_StoryLength: _Callable
                get_Text: _Callable
                put_Text: _Callable
                CanPaste: _Callable
                ChangeCase: _Callable
                Collapse: _Callable
                Copy: _Callable
                Cut: _Callable
                Delete: _Callable
                EndOf: _Callable
                Expand: _Callable
                FindText: _Callable
                GetCharacterUtf32: _Callable
                GetClone: _Callable
                GetIndex: _Callable
                GetPoint: _Callable
                GetRect: _Callable
                GetText: _Callable
                GetTextViaStream: _Callable
                InRange: _Callable
                InsertImage: _Callable
                InStory: _Callable
                IsEqual: _Callable
                Move: _Callable
                MoveEnd: _Callable
                MoveStart: _Callable
                Paste: _Callable
                ScrollIntoView: _Callable
                MatchSelection: _Callable
                SetIndex: _Callable
                SetPoint: _Callable
                SetRange: _Callable
                SetText: _Callable
                SetTextViaStream: _Callable
                StartOf: _Callable

            class ITextSelection(IInspectable):
                get_Options: _Callable
                put_Options: _Callable
                get_Type: _Callable
                EndKey: _Callable
                HomeKey: _Callable
                MoveDown: _Callable
                MoveLeft: _Callable
                MoveRight: _Callable
                MoveUp: _Callable
                TypeText: _Callable

        class Popups:
            class _IUICommandInvokedHandler:
                Invoke: _Callable

            class IUICommandInvokedHandler(_IUICommandInvokedHandler, IUnknown):
                pass

            # noinspection PyPep8Naming
            class IUICommandInvokedHandler_impl(_IUICommandInvokedHandler, IUnknown_impl):
                pass

            class IMessageDialog(IInspectable):
                get_Title: _Callable
                put_Title: _Callable
                get_Commands: _Callable
                get_DefaultCommandIndex: _Callable
                put_DefaultCommandIndex: _Callable
                get_CancelCommandIndex: _Callable
                put_CancelCommandIndex: _Callable
                get_Content: _Callable
                put_Content: _Callable
                ShowAsync: _Callable
                get_Options: _Callable
                put_Options: _Callable

            class IMessageDialogFactory(IInspectable):
                Create: _Callable
                CreateWithTitle: _Callable

            class IPopupMenu(IInspectable):
                get_Commands: _Callable
                ShowAsync: _Callable
                ShowAsyncWithRect: _Callable
                ShowAsyncWithRectAndPlacement: _Callable

            class IUICommand(IInspectable):
                get_Label: _Callable
                put_Label: _Callable
                get_Invoked: _Callable
                put_Invoked: _Callable
                get_Id: _Callable
                put_Id: _Callable

            class IUICommandFactory(IInspectable):
                Create: _Callable
                CreateWithHandler: _Callable
                CreateWithHandlerAndId: _Callable

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
                get_TextScaleFactor: _Callable[[_Pointer[_type.DOUBLE]],
                                               _type.HRESULT]
                add_TextScaleFactorChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.ViewManagement.IUISettings, IInspectable],
                                                       _Pointer[_struct.EventRegistrationToken]],
                                                      _type.HRESULT]
                remove_TextScaleFactorChanged: _Callable[[_struct.EventRegistrationToken],
                                                         _type.HRESULT]

            class IUISettings3(IInspectable):
                GetColorValue: _Callable[[_enum.Windows.UI.ViewManagement.UIColorType,
                                          _Pointer[_struct.Windows.UI.Color]],
                                         _type.HRESULT]
                add_ColorValuesChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.ViewManagement.IUISettings, IInspectable],
                                                   _Pointer[_struct.EventRegistrationToken]],
                                                  _type.HRESULT]
                remove_ColorValuesChanged: _Callable[[_struct.EventRegistrationToken],
                                                     _type.HRESULT]

            class IUISettings4(IInspectable):
                get_AdvancedEffectsEnabled: _Callable[[_Pointer[_type.boolean]],
                                                      _type.HRESULT]
                add_AdvancedEffectsEnabledChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.ViewManagement.IUISettings, IInspectable],
                                                              _Pointer[_struct.EventRegistrationToken]],
                                                             _type.HRESULT]
                remove_AdvancedEffectsEnabledChanged: _Callable[[_struct.EventRegistrationToken],
                                                                _type.HRESULT]

            class IUISettings5(IInspectable):
                get_AutoHideScrollBars: _Callable[[_Pointer[_type.boolean]],
                                                  _type.HRESULT]
                add_AutoHideScrollBarsChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.ViewManagement.IUISettings, Windows.UI.ViewManagement.IUISettingsAutoHideScrollBarsChangedEventArgs],
                                                          _Pointer[_struct.EventRegistrationToken]],
                                                         _type.HRESULT]
                remove_AutoHideScrollBarsChanged: _Callable[[_struct.EventRegistrationToken],
                                                            _type.HRESULT]

            class IUISettings6(IInspectable):
                add_AnimationsEnabledChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.ViewManagement.IUISettings, Windows.UI.ViewManagement.IUISettingsAnimationsEnabledChangedEventArgs],
                                                         _Pointer[_struct.EventRegistrationToken]],
                                                        _type.HRESULT]
                remove_AnimationsEnabledChanged: _Callable[[_struct.EventRegistrationToken],
                                                           _type.HRESULT]
                add_MessageDurationChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.ViewManagement.IUISettings, Windows.UI.ViewManagement.IUISettingsMessageDurationChangedEventArgs],
                                                       _Pointer[_struct.EventRegistrationToken]],
                                                      _type.HRESULT]
                remove_MessageDurationChanged: _Callable[[_struct.EventRegistrationToken],
                                                         _type.HRESULT]

            class IUISettingsAnimationsEnabledChangedEventArgs(IInspectable):
                pass

            class IUISettingsAutoHideScrollBarsChangedEventArgs(IInspectable):
                pass

            class IUISettingsMessageDurationChangedEventArgs(IInspectable):
                pass

            class IUIViewSettings(IInspectable):
                get_UserInteractionMode: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.UserInteractionMode]],
                                                   _type.HRESULT]

            class IUIViewSettingsStatics(IInspectable):
                GetForCurrentView: _Callable[[_Pointer[Windows.UI.ViewManagement.IUIViewSettings]],
                                             _type.HRESULT]

            class IViewModePreferences(IInspectable):
                get_ViewSizePreference: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ViewSizePreference]],
                                                  _type.HRESULT]
                put_ViewSizePreference: _Callable[[_enum.Windows.UI.ViewManagement.ViewSizePreference],
                                                  _type.HRESULT]
                get_CustomSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                          _type.HRESULT]
                put_CustomSize: _Callable[[_struct.Windows.Foundation.Size],
                                          _type.HRESULT]

            class IViewModePreferencesStatics(IInspectable):
                CreateDefault: _Callable[[_enum.Windows.UI.ViewManagement.ApplicationViewMode,
                                          _Pointer[Windows.UI.ViewManagement.IViewModePreferences]],
                                         _type.HRESULT]

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
                get_Triggers: _Callable[[_Pointer[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.ITriggerBase]]],
                                        _type.HRESULT]
                get_Resources: _Callable[[_Pointer[Windows.UI.Xaml.IResourceDictionary]],
                                         _type.HRESULT]
                put_Resources: _Callable[[Windows.UI.Xaml.IResourceDictionary],
                                         _type.HRESULT]
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
                SetBinding: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                       Windows.UI.Xaml.Data.IBindingBase],
                                      _type.HRESULT]

            class IFrameworkElement2(IInspectable):
                get_RequestedTheme: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementTheme]],
                                              _type.HRESULT]
                put_RequestedTheme: _Callable[[_enum.Windows.UI.Xaml.ElementTheme],
                                              _type.HRESULT]
                add_DataContextChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.IFrameworkElement, Windows.UI.Xaml.IDataContextChangedEventArgs],
                                                   _Pointer[_struct.EventRegistrationToken]],
                                                  _type.HRESULT]
                remove_DataContextChanged: _Callable[[_struct.EventRegistrationToken],
                                                     _type.HRESULT]
                GetBindingExpression: _Callable[[Windows.UI.Xaml.IDependencyProperty,
                                                 _Pointer[Windows.UI.Xaml.Data.IBindingExpression]],
                                                _type.HRESULT]

            class IFrameworkElement3(IInspectable):
                add_Loading: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.IFrameworkElement, IInspectable],
                                        _Pointer[_struct.EventRegistrationToken]],
                                       _type.HRESULT]
                remove_Loading: _Callable[[_struct.EventRegistrationToken],
                                          _type.HRESULT]

            class IFrameworkElement4(IInspectable):
                get_AllowFocusOnInteraction: _Callable[[_Pointer[_type.boolean]],
                                                       _type.HRESULT]
                put_AllowFocusOnInteraction: _Callable[[_type.boolean],
                                                       _type.HRESULT]
                get_FocusVisualMargin: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],
                                                 _type.HRESULT]
                put_FocusVisualMargin: _Callable[[_struct.Windows.UI.Xaml.Thickness],
                                                 _type.HRESULT]
                get_FocusVisualSecondaryThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],
                                                             _type.HRESULT]
                put_FocusVisualSecondaryThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],
                                                             _type.HRESULT]
                get_FocusVisualPrimaryThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],
                                                           _type.HRESULT]
                put_FocusVisualPrimaryThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],
                                                           _type.HRESULT]
                get_FocusVisualSecondaryBrush: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                                         _type.HRESULT]
                put_FocusVisualSecondaryBrush: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                                         _type.HRESULT]
                get_FocusVisualPrimaryBrush: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                                       _type.HRESULT]
                put_FocusVisualPrimaryBrush: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                                       _type.HRESULT]
                get_AllowFocusWhenDisabled: _Callable[[_Pointer[_type.boolean]],
                                                      _type.HRESULT]
                put_AllowFocusWhenDisabled: _Callable[[_type.boolean],
                                                      _type.HRESULT]

            class IFrameworkElement6(IInspectable):
                get_ActualTheme: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementTheme]],
                                           _type.HRESULT]
                add_ActualThemeChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.IFrameworkElement, IInspectable],
                                                   _Pointer[_struct.EventRegistrationToken]],
                                                  _type.HRESULT]
                remove_ActualThemeChanged: _Callable[[_struct.EventRegistrationToken],
                                                     _type.HRESULT]

            class IFrameworkElement7(IInspectable):
                get_IsLoaded: _Callable[[_Pointer[_type.boolean]],
                                        _type.HRESULT]
                add_EffectiveViewportChanged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.IFrameworkElement, Windows.UI.Xaml.IEffectiveViewportChangedEventArgs],
                                                         _Pointer[_struct.EventRegistrationToken]],
                                                        _type.HRESULT]
                remove_EffectiveViewportChanged: _Callable[[_struct.EventRegistrationToken],
                                                           _type.HRESULT]

            class IFrameworkElementFactory(IInspectable):
                CreateInstance: _Callable[[IInspectable,
                                           _Pointer[IInspectable],
                                           _Pointer[Windows.UI.Xaml.IFrameworkElement]],
                                          _type.HRESULT]

            class IFrameworkElementOverrides(IInspectable):
                MeasureOverride: _Callable[[_struct.Windows.Foundation.Size,
                                            _Pointer[_struct.Windows.Foundation.Size]],
                                           _type.HRESULT]
                ArrangeOverride: _Callable[[_struct.Windows.Foundation.Size,
                                            _Pointer[_struct.Windows.Foundation.Size]],
                                           _type.HRESULT]
                OnApplyTemplate: _Callable[[],
                                           _type.HRESULT]

            class IFrameworkElementOverrides2(IInspectable):
                GoToElementStateCore: _Callable[[_type.HSTRING,
                                                 _type.boolean,
                                                 _Pointer[_type.boolean]],
                                                _type.HRESULT]

            class IFrameworkElementProtected7(IInspectable):
                InvalidateViewport: _Callable[[],
                                              _type.HRESULT]

            class IFrameworkElementStatics(IInspectable):
                get_TagProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                           _type.HRESULT]
                get_LanguageProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]
                get_ActualWidthProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                get_ActualHeightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                get_WidthProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                             _type.HRESULT]
                get_HeightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                              _type.HRESULT]
                get_MinWidthProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]
                get_MaxWidthProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]
                get_MinHeightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                 _type.HRESULT]
                get_MaxHeightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                 _type.HRESULT]
                get_HorizontalAlignmentProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                get_VerticalAlignmentProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                get_MarginProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                              _type.HRESULT]
                get_NameProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                            _type.HRESULT]
                get_DataContextProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                get_StyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                             _type.HRESULT]
                get_FlowDirectionProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]

            class IFrameworkElementStatics2(IInspectable):
                get_RequestedThemeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]

            class IFrameworkElementStatics4(IInspectable):
                get_AllowFocusOnInteractionProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                get_FocusVisualMarginProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                get_FocusVisualSecondaryThicknessProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                     _type.HRESULT]
                get_FocusVisualPrimaryThicknessProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]
                get_FocusVisualSecondaryBrushProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                get_FocusVisualPrimaryBrushProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                get_AllowFocusWhenDisabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]

            class IFrameworkElementStatics5(IInspectable):
                DeferTree: _Callable[[Windows.UI.Xaml.IDependencyObject],
                                     _type.HRESULT]

            class IFrameworkElementStatics6(IInspectable):
                get_ActualThemeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]

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
                get_Target: _Callable[[_Pointer[Windows.UI.Xaml.ITargetPropertyPath]],
                                      _type.HRESULT]
                put_Target: _Callable[[Windows.UI.Xaml.ITargetPropertyPath],
                                      _type.HRESULT]

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
                CreateInstance: _Callable[[IInspectable,
                                           _Pointer[IInspectable],
                                           _Pointer[Windows.UI.Xaml.IVisualTransition]],
                                          _type.HRESULT]

            class IWindow(IInspectable):
                get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],
                                      _type.HRESULT]
                get_Visible: _Callable[[_Pointer[_type.boolean]],
                                       _type.HRESULT]
                get_Content: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                       _type.HRESULT]
                put_Content: _Callable[[Windows.UI.Xaml.IUIElement],
                                       _type.HRESULT]
                get_CoreWindow: _Callable[[_Pointer[Windows.UI.Core.ICoreWindow]],
                                          _type.HRESULT]
                get_Dispatcher: _Callable[[_Pointer[Windows.UI.Core.ICoreDispatcher]],
                                          _type.HRESULT]
                add_Activated: _Callable[[Windows.UI.Xaml.IWindowActivatedEventHandler_impl,
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
                remove_Activated: _Callable[[_struct.EventRegistrationToken],
                                            _type.HRESULT]
                add_Closed: _Callable[[Windows.UI.Xaml.IWindowClosedEventHandler_impl,
                                       _Pointer[_struct.EventRegistrationToken]],
                                      _type.HRESULT]
                remove_Closed: _Callable[[_struct.EventRegistrationToken],
                                         _type.HRESULT]
                add_SizeChanged: _Callable[[Windows.UI.Xaml.IWindowSizeChangedEventHandler_impl,
                                            _Pointer[_struct.EventRegistrationToken]],
                                           _type.HRESULT]
                remove_SizeChanged: _Callable[[_struct.EventRegistrationToken],
                                              _type.HRESULT]
                add_VisibilityChanged: _Callable[[Windows.UI.Xaml.IWindowVisibilityChangedEventHandler_impl,
                                                  _Pointer[_struct.EventRegistrationToken]],
                                                 _type.HRESULT]
                remove_VisibilityChanged: _Callable[[_struct.EventRegistrationToken],
                                                    _type.HRESULT]
                Activate: _Callable[[],
                                    _type.HRESULT]
                Close: _Callable[[],
                                 _type.HRESULT]

            class IWindow2(IInspectable):
                SetTitleBar: _Callable[[Windows.UI.Xaml.IUIElement],
                                       _type.HRESULT]

            class IWindow3(IInspectable):
                get_Compositor: _Callable[[_Pointer[Windows.UI.Composition.ICompositor]],
                                          _type.HRESULT]

            class IWindow4(IInspectable):
                get_UIContext: _Callable[[_Pointer[Windows.UI.IUIContext]],
                                         _type.HRESULT]

            class IWindowCreatedEventArgs(IInspectable):
                get_Window: _Callable[[_Pointer[Windows.UI.Xaml.IWindow]],
                                      _type.HRESULT]

            class IWindowStatics(IInspectable):
                get_Current: _Callable[[_Pointer[Windows.UI.Xaml.IWindow]],
                                       _type.HRESULT]

            class IXamlRoot(IInspectable):
                get_Content: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                       _type.HRESULT]
                get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],
                                    _type.HRESULT]
                get_RasterizationScale: _Callable[[_Pointer[_type.DOUBLE]],
                                                  _type.HRESULT]
                get_IsHostVisible: _Callable[[_Pointer[_type.boolean]],
                                             _type.HRESULT]
                get_UIContext: _Callable[[_Pointer[Windows.UI.IUIContext]],
                                         _type.HRESULT]
                add_Changed: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.IXamlRoot, Windows.UI.Xaml.IXamlRootChangedEventArgs],
                                        _Pointer[_struct.EventRegistrationToken]],
                                       _type.HRESULT]
                remove_Changed: _Callable[[_struct.EventRegistrationToken],
                                          _type.HRESULT]

            class IXamlRootChangedEventArgs(IInspectable):
                pass

            class Automation:
                class Peers:
                    class IAppBarAutomationPeer(IInspectable):
                        pass

                    class IAppBarAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IAppBarButtonAutomationPeer(IInspectable):
                        pass

                    class IAppBarButtonAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IAppBarToggleButtonAutomationPeer(IInspectable):
                        pass

                    class IAppBarToggleButtonAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IAutoSuggestBoxAutomationPeer(IInspectable):
                        pass

                    class IAutoSuggestBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IAutomationPeer(IInspectable):
                        get_EventsSource: _Callable
                        put_EventsSource: _Callable
                        GetPattern: _Callable
                        RaiseAutomationEvent: _Callable
                        RaisePropertyChangedEvent: _Callable
                        GetAcceleratorKey: _Callable
                        GetAccessKey: _Callable
                        GetAutomationControlType: _Callable
                        GetAutomationId: _Callable
                        GetBoundingRectangle: _Callable
                        GetChildren: _Callable
                        GetClassName: _Callable
                        GetClickablePoint: _Callable
                        GetHelpText: _Callable
                        GetItemStatus: _Callable
                        GetItemType: _Callable
                        GetLabeledBy: _Callable
                        GetLocalizedControlType: _Callable
                        GetName: _Callable
                        GetOrientation: _Callable
                        HasKeyboardFocus: _Callable
                        IsContentElement: _Callable
                        IsControlElement: _Callable
                        IsEnabled: _Callable
                        IsKeyboardFocusable: _Callable
                        IsOffscreen: _Callable
                        IsPassword: _Callable
                        IsRequiredForForm: _Callable
                        SetFocus: _Callable
                        GetParent: _Callable
                        InvalidatePeer: _Callable
                        GetPeerFromPoint: _Callable
                        GetLiveSetting: _Callable

                    class IAutomationPeer2(IInspectable):
                        pass

                    class IAutomationPeer3(IInspectable):
                        Navigate: _Callable
                        GetElementFromPoint: _Callable
                        GetFocusedElement: _Callable
                        ShowContextMenu: _Callable
                        GetControlledPeers: _Callable
                        GetAnnotations: _Callable
                        SetParent: _Callable
                        RaiseTextEditTextChangedEvent: _Callable
                        GetPositionInSet: _Callable
                        GetSizeOfSet: _Callable
                        GetLevel: _Callable
                        RaiseStructureChangedEvent: _Callable

                    class IAutomationPeer4(IInspectable):
                        GetLandmarkType: _Callable
                        GetLocalizedLandmarkType: _Callable

                    class IAutomationPeer5(IInspectable):
                        IsPeripheral: _Callable
                        IsDataValidForForm: _Callable
                        GetFullDescription: _Callable

                    class IAutomationPeer6(IInspectable):
                        GetCulture: _Callable

                    class IAutomationPeer7(IInspectable):
                        RaiseNotificationEvent: _Callable

                    class IAutomationPeer8(IInspectable):
                        GetHeadingLevel: _Callable

                    class IAutomationPeer9(IInspectable):
                        IsDialog: _Callable

                    class IAutomationPeerAnnotation(IInspectable):
                        get_Type: _Callable
                        put_Type: _Callable
                        get_Peer: _Callable
                        put_Peer: _Callable

                    class IAutomationPeerAnnotationFactory(IInspectable):
                        CreateInstance: _Callable
                        CreateWithPeerParameter: _Callable

                    class IAutomationPeerAnnotationStatics(IInspectable):
                        get_TypeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                        get_PeerProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]

                    class IAutomationPeerFactory(IInspectable):
                        CreateInstance: _Callable[[IInspectable,
                                                   _Pointer[IInspectable],
                                                   _Pointer[Windows.UI.Xaml.Automation.Peers.IAutomationPeer]],
                                                  _type.HRESULT]

                    class IAutomationPeerOverrides(IInspectable):
                        GetPatternCore: _Callable
                        GetAcceleratorKeyCore: _Callable
                        GetAccessKeyCore: _Callable
                        GetAutomationControlTypeCore: _Callable
                        GetAutomationIdCore: _Callable
                        GetBoundingRectangleCore: _Callable
                        GetChildrenCore: _Callable
                        GetClassNameCore: _Callable
                        GetClickablePointCore: _Callable
                        GetHelpTextCore: _Callable
                        GetItemStatusCore: _Callable
                        GetItemTypeCore: _Callable
                        GetLabeledByCore: _Callable
                        GetLocalizedControlTypeCore: _Callable
                        GetNameCore: _Callable
                        GetOrientationCore: _Callable
                        HasKeyboardFocusCore: _Callable
                        IsContentElementCore: _Callable
                        IsControlElementCore: _Callable
                        IsEnabledCore: _Callable
                        IsKeyboardFocusableCore: _Callable
                        IsOffscreenCore: _Callable
                        IsPasswordCore: _Callable
                        IsRequiredForFormCore: _Callable
                        SetFocusCore: _Callable
                        GetPeerFromPointCore: _Callable
                        GetLiveSettingCore: _Callable

                    class IAutomationPeerOverrides2(IInspectable):
                        ShowContextMenuCore: _Callable
                        GetControlledPeersCore: _Callable

                    class IAutomationPeerOverrides3(IInspectable):
                        NavigateCore: _Callable
                        GetElementFromPointCore: _Callable
                        GetFocusedElementCore: _Callable
                        GetAnnotationsCore: _Callable
                        GetPositionInSetCore: _Callable
                        GetSizeOfSetCore: _Callable
                        GetLevelCore: _Callable

                    class IAutomationPeerOverrides4(IInspectable):
                        GetLandmarkTypeCore: _Callable
                        GetLocalizedLandmarkTypeCore: _Callable

                    class IAutomationPeerOverrides5(IInspectable):
                        IsPeripheralCore: _Callable
                        IsDataValidForFormCore: _Callable
                        GetFullDescriptionCore: _Callable
                        GetDescribedByCore: _Callable
                        GetFlowsToCore: _Callable
                        GetFlowsFromCore: _Callable

                    class IAutomationPeerOverrides6(IInspectable):
                        GetCultureCore: _Callable

                    class IAutomationPeerOverrides8(IInspectable):
                        GetHeadingLevelCore: _Callable

                    class IAutomationPeerOverrides9(IInspectable):
                        IsDialogCore: _Callable

                    class IAutomationPeerProtected(IInspectable):
                        PeerFromProvider: _Callable
                        ProviderFromPeer: _Callable

                    class IAutomationPeerStatics(IInspectable):
                        ListenerExists: _Callable

                    class IAutomationPeerStatics3(IInspectable):
                        GenerateRawElementProviderRuntimeId: _Callable

                    class IButtonAutomationPeer(IInspectable):
                        pass

                    class IButtonAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IButtonBaseAutomationPeer(IInspectable):
                        pass

                    class IButtonBaseAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ICalendarDatePickerAutomationPeer(IInspectable):
                        pass

                    class ICalendarDatePickerAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ICaptureElementAutomationPeer(IInspectable):
                        pass

                    class ICaptureElementAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ICheckBoxAutomationPeer(IInspectable):
                        pass

                    class ICheckBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IColorPickerSliderAutomationPeer(IInspectable):
                        pass

                    class IColorPickerSliderAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IColorSpectrumAutomationPeer(IInspectable):
                        pass

                    class IColorSpectrumAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IComboBoxAutomationPeer(IInspectable):
                        pass

                    class IComboBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IComboBoxItemAutomationPeer(IInspectable):
                        pass

                    class IComboBoxItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IComboBoxItemDataAutomationPeer(IInspectable):
                        pass

                    class IComboBoxItemDataAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class IDatePickerAutomationPeer(IInspectable):
                        pass

                    class IDatePickerAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IDatePickerFlyoutPresenterAutomationPeer(IInspectable):
                        pass

                    class IFlipViewAutomationPeer(IInspectable):
                        pass

                    class IFlipViewAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IFlipViewItemAutomationPeer(IInspectable):
                        pass

                    class IFlipViewItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IFlipViewItemDataAutomationPeer(IInspectable):
                        pass

                    class IFlipViewItemDataAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class IFlyoutPresenterAutomationPeer(IInspectable):
                        pass

                    class IFlyoutPresenterAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IFrameworkElementAutomationPeer(IInspectable):
                        get_Owner: _Callable

                    class IFrameworkElementAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IFrameworkElementAutomationPeerStatics(IInspectable):
                        FromElement: _Callable
                        CreatePeerForElement: _Callable

                    class IGridViewAutomationPeer(IInspectable):
                        pass

                    class IGridViewAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IGridViewHeaderItemAutomationPeer(IInspectable):
                        pass

                    class IGridViewHeaderItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IGridViewItemAutomationPeer(IInspectable):
                        pass

                    class IGridViewItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IGridViewItemDataAutomationPeer(IInspectable):
                        pass

                    class IGridViewItemDataAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class IGroupItemAutomationPeer(IInspectable):
                        pass

                    class IGroupItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IHubAutomationPeer(IInspectable):
                        pass

                    class IHubAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IHubSectionAutomationPeer(IInspectable):
                        pass

                    class IHubSectionAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IHyperlinkButtonAutomationPeer(IInspectable):
                        pass

                    class IHyperlinkButtonAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IImageAutomationPeer(IInspectable):
                        pass

                    class IImageAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IInkToolbarAutomationPeer(IInspectable):
                        pass

                    class IItemAutomationPeer(IInspectable):
                        get_Item: _Callable
                        get_ItemsControlAutomationPeer: _Callable

                    class IItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class IItemsControlAutomationPeer(IInspectable):
                        pass

                    class IItemsControlAutomationPeer2(IInspectable):
                        CreateItemAutomationPeer: _Callable

                    class IItemsControlAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IItemsControlAutomationPeerOverrides2(IInspectable):
                        OnCreateItemAutomationPeer: _Callable

                    class IListBoxAutomationPeer(IInspectable):
                        pass

                    class IListBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IListBoxItemAutomationPeer(IInspectable):
                        pass

                    class IListBoxItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IListBoxItemDataAutomationPeer(IInspectable):
                        pass

                    class IListBoxItemDataAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class IListPickerFlyoutPresenterAutomationPeer(IInspectable):
                        pass

                    class IListViewAutomationPeer(IInspectable):
                        pass

                    class IListViewAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IListViewBaseAutomationPeer(IInspectable):
                        pass

                    class IListViewBaseAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IListViewBaseHeaderItemAutomationPeer(IInspectable):
                        pass

                    class IListViewBaseHeaderItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IListViewHeaderItemAutomationPeer(IInspectable):
                        pass

                    class IListViewHeaderItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IListViewItemAutomationPeer(IInspectable):
                        pass

                    class IListViewItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IListViewItemDataAutomationPeer(IInspectable):
                        pass

                    class IListViewItemDataAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class ILoopingSelectorAutomationPeer(IInspectable):
                        pass

                    class ILoopingSelectorItemAutomationPeer(IInspectable):
                        pass

                    class ILoopingSelectorItemDataAutomationPeer(IInspectable):
                        pass

                    class IMapControlAutomationPeer(IInspectable):
                        pass

                    class IMediaElementAutomationPeer(IInspectable):
                        pass

                    class IMediaElementAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IMediaPlayerElementAutomationPeer(IInspectable):
                        pass

                    class IMediaPlayerElementAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IMediaTransportControlsAutomationPeer(IInspectable):
                        pass

                    class IMediaTransportControlsAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IMenuBarAutomationPeer(IInspectable):
                        pass

                    class IMenuBarAutomationPeerFactory(IInspectable):
                        CreateInstance: _Callable[[Windows.UI.Xaml.Controls.IMenuBar,
                                                   IInspectable,
                                                   _Pointer[IInspectable],
                                                   _Pointer[Windows.UI.Xaml.Automation.Peers.IMenuBarAutomationPeer]],
                                                  _type.HRESULT]

                    class IMenuBarItemAutomationPeer(IInspectable):
                        pass

                    class IMenuBarItemAutomationPeerFactory(IInspectable):
                        CreateInstance: _Callable[[Windows.UI.Xaml.Controls.IMenuBarItem,
                                                   IInspectable,
                                                   _Pointer[IInspectable],
                                                   _Pointer[Windows.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeer]],
                                                  _type.HRESULT]

                    class IMenuFlyoutItemAutomationPeer(IInspectable):
                        pass

                    class IMenuFlyoutItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IMenuFlyoutPresenterAutomationPeer(IInspectable):
                        pass

                    class IMenuFlyoutPresenterAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class INavigationViewItemAutomationPeer(IInspectable):
                        pass

                    class INavigationViewItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IPasswordBoxAutomationPeer(IInspectable):
                        pass

                    class IPasswordBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IPersonPictureAutomationPeer(IInspectable):
                        pass

                    class IPersonPictureAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IPickerFlyoutPresenterAutomationPeer(IInspectable):
                        pass

                    class IPivotAutomationPeer(IInspectable):
                        pass

                    class IPivotAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IPivotItemAutomationPeer(IInspectable):
                        pass

                    class IPivotItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IPivotItemDataAutomationPeer(IInspectable):
                        pass

                    class IPivotItemDataAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class IProgressBarAutomationPeer(IInspectable):
                        pass

                    class IProgressBarAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IProgressRingAutomationPeer(IInspectable):
                        pass

                    class IProgressRingAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IRadioButtonAutomationPeer(IInspectable):
                        pass

                    class IRadioButtonAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IRangeBaseAutomationPeer(IInspectable):
                        pass

                    class IRangeBaseAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IRatingControlAutomationPeer(IInspectable):
                        pass

                    class IRatingControlAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IRepeatButtonAutomationPeer(IInspectable):
                        pass

                    class IRepeatButtonAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IRichEditBoxAutomationPeer(IInspectable):
                        pass

                    class IRichEditBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IRichTextBlockAutomationPeer(IInspectable):
                        pass

                    class IRichTextBlockAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IRichTextBlockOverflowAutomationPeer(IInspectable):
                        pass

                    class IRichTextBlockOverflowAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IScrollBarAutomationPeer(IInspectable):
                        pass

                    class IScrollBarAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IScrollViewerAutomationPeer(IInspectable):
                        pass

                    class IScrollViewerAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ISearchBoxAutomationPeer(IInspectable):
                        pass

                    class ISearchBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ISelectorAutomationPeer(IInspectable):
                        pass

                    class ISelectorAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ISelectorItemAutomationPeer(IInspectable):
                        pass

                    class ISelectorItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithParentAndItem: _Callable

                    class ISemanticZoomAutomationPeer(IInspectable):
                        pass

                    class ISemanticZoomAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ISettingsFlyoutAutomationPeer(IInspectable):
                        pass

                    class ISettingsFlyoutAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ISliderAutomationPeer(IInspectable):
                        pass

                    class ISliderAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ITextBlockAutomationPeer(IInspectable):
                        pass

                    class ITextBlockAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ITextBoxAutomationPeer(IInspectable):
                        pass

                    class ITextBoxAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IThumbAutomationPeer(IInspectable):
                        pass

                    class IThumbAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ITimePickerAutomationPeer(IInspectable):
                        pass

                    class ITimePickerAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ITimePickerFlyoutPresenterAutomationPeer(IInspectable):
                        pass

                    class IToggleButtonAutomationPeer(IInspectable):
                        pass

                    class IToggleButtonAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IToggleMenuFlyoutItemAutomationPeer(IInspectable):
                        pass

                    class IToggleMenuFlyoutItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class IToggleSwitchAutomationPeer(IInspectable):
                        pass

                    class IToggleSwitchAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ITreeViewItemAutomationPeer(IInspectable):
                        pass

                    class ITreeViewItemAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

                    class ITreeViewListAutomationPeer(IInspectable):
                        pass

                    class ITreeViewListAutomationPeerFactory(IInspectable):
                        CreateInstanceWithOwner: _Callable

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
                    get_UriSource: _Callable[[_Pointer[Windows.Foundation.IUriRuntimeClass]],
                                             _type.HRESULT]
                    put_UriSource: _Callable[[Windows.Foundation.IUriRuntimeClass],
                                             _type.HRESULT]

                class IBitmapIcon2(IInspectable):
                    get_ShowAsMonochrome: _Callable[[_Pointer[_type.boolean]],
                                                    _type.HRESULT]
                    put_ShowAsMonochrome: _Callable[[_type.boolean],
                                                    _type.HRESULT]

                class IBitmapIconFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IBitmapIcon]],
                                              _type.HRESULT]

                class IBitmapIconSource(IInspectable):
                    get_UriSource: _Callable[[_Pointer[Windows.Foundation.IUriRuntimeClass]],
                                             _type.HRESULT]
                    put_UriSource: _Callable[[Windows.Foundation.IUriRuntimeClass],
                                             _type.HRESULT]
                    get_ShowAsMonochrome: _Callable[[_Pointer[_type.boolean]],
                                                    _type.HRESULT]
                    put_ShowAsMonochrome: _Callable[[_type.boolean],
                                                    _type.HRESULT]

                class IBitmapIconSourceFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IBitmapIconSource]],
                                              _type.HRESULT]

                class IBitmapIconSourceStatics(IInspectable):
                    get_UriSourceProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_ShowAsMonochromeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]

                class IBitmapIconStatics(IInspectable):
                    get_UriSourceProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]

                class IBitmapIconStatics2(IInspectable):
                    get_ShowAsMonochromeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]

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
                    get_Content: _Callable[[_Pointer[IInspectable]],
                                           _type.HRESULT]
                    put_Content: _Callable[[IInspectable],
                                           _type.HRESULT]
                    get_ContentTemplate: _Callable[[_Pointer[Windows.UI.Xaml.IDataTemplate]],
                                                   _type.HRESULT]
                    put_ContentTemplate: _Callable[[Windows.UI.Xaml.IDataTemplate],
                                                   _type.HRESULT]
                    get_ContentTemplateSelector: _Callable[[_Pointer[Windows.UI.Xaml.Controls.IDataTemplateSelector]],
                                                           _type.HRESULT]
                    put_ContentTemplateSelector: _Callable[[Windows.UI.Xaml.Controls.IDataTemplateSelector],
                                                           _type.HRESULT]
                    get_ContentTransitions: _Callable[[_Pointer[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ITransition]]],
                                                      _type.HRESULT]
                    put_ContentTransitions: _Callable[[Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Animation.ITransition]],
                                                      _type.HRESULT]

                class IContentControl2(IInspectable):
                    get_ContentTemplateRoot: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                                       _type.HRESULT]

                class IContentControlFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IContentControl]],
                                              _type.HRESULT]

                class IContentControlOverrides(IInspectable):
                    OnContentChanged: _Callable[[IInspectable,
                                                 IInspectable],
                                                _type.HRESULT]
                    OnContentTemplateChanged: _Callable[[Windows.UI.Xaml.IDataTemplate,
                                                         Windows.UI.Xaml.IDataTemplate],
                                                        _type.HRESULT]
                    OnContentTemplateSelectorChanged: _Callable[[Windows.UI.Xaml.Controls.IDataTemplateSelector,
                                                                 Windows.UI.Xaml.Controls.IDataTemplateSelector],
                                                                _type.HRESULT]

                class IContentControlStatics(IInspectable):
                    get_ContentProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                    get_ContentTemplateProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_ContentTemplateSelectorProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]
                    get_ContentTransitionsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]

                class IContentDialog(IInspectable):
                    get_Title: _Callable[[_Pointer[IInspectable]],
                                         _type.HRESULT]
                    put_Title: _Callable[[IInspectable],
                                         _type.HRESULT]
                    get_TitleTemplate: _Callable[[_Pointer[Windows.UI.Xaml.IDataTemplate]],
                                                 _type.HRESULT]
                    put_TitleTemplate: _Callable[[Windows.UI.Xaml.IDataTemplate],
                                                 _type.HRESULT]
                    get_FullSizeDesired: _Callable[[_Pointer[_type.boolean]],
                                                   _type.HRESULT]
                    put_FullSizeDesired: _Callable[[_type.boolean],
                                                   _type.HRESULT]
                    get_PrimaryButtonText: _Callable[[_Pointer[_type.HSTRING]],
                                                     _type.HRESULT]
                    put_PrimaryButtonText: _Callable[[_type.HSTRING],
                                                     _type.HRESULT]
                    get_SecondaryButtonText: _Callable[[_Pointer[_type.HSTRING]],
                                                       _type.HRESULT]
                    put_SecondaryButtonText: _Callable[[_type.HSTRING],
                                                       _type.HRESULT]
                    get_PrimaryButtonCommand: _Callable[[_Pointer[Windows.UI.Xaml.Input.ICommand]],
                                                        _type.HRESULT]
                    put_PrimaryButtonCommand: _Callable[[Windows.UI.Xaml.Input.ICommand],
                                                        _type.HRESULT]
                    get_SecondaryButtonCommand: _Callable[[_Pointer[Windows.UI.Xaml.Input.ICommand]],
                                                          _type.HRESULT]
                    put_SecondaryButtonCommand: _Callable[[Windows.UI.Xaml.Input.ICommand],
                                                          _type.HRESULT]
                    get_PrimaryButtonCommandParameter: _Callable[[_Pointer[IInspectable]],
                                                                 _type.HRESULT]
                    put_PrimaryButtonCommandParameter: _Callable[[IInspectable],
                                                                 _type.HRESULT]
                    get_SecondaryButtonCommandParameter: _Callable[[_Pointer[IInspectable]],
                                                                   _type.HRESULT]
                    put_SecondaryButtonCommandParameter: _Callable[[IInspectable],
                                                                   _type.HRESULT]
                    get_IsPrimaryButtonEnabled: _Callable[[_Pointer[_type.boolean]],
                                                          _type.HRESULT]
                    put_IsPrimaryButtonEnabled: _Callable[[_type.boolean],
                                                          _type.HRESULT]
                    get_IsSecondaryButtonEnabled: _Callable[[_Pointer[_type.boolean]],
                                                            _type.HRESULT]
                    put_IsSecondaryButtonEnabled: _Callable[[_type.boolean],
                                                            _type.HRESULT]
                    add_Closing: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IContentDialog, Windows.UI.Xaml.Controls.IContentDialogClosingEventArgs],
                                            _Pointer[_struct.EventRegistrationToken]],
                                           _type.HRESULT]
                    remove_Closing: _Callable[[_struct.EventRegistrationToken],
                                              _type.HRESULT]
                    add_Closed: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IContentDialog, Windows.UI.Xaml.Controls.IContentDialogClosedEventArgs],
                                           _Pointer[_struct.EventRegistrationToken]],
                                          _type.HRESULT]
                    remove_Closed: _Callable[[_struct.EventRegistrationToken],
                                             _type.HRESULT]
                    add_Opened: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IContentDialog, Windows.UI.Xaml.Controls.IContentDialogOpenedEventArgs],
                                           _Pointer[_struct.EventRegistrationToken]],
                                          _type.HRESULT]
                    remove_Opened: _Callable[[_struct.EventRegistrationToken],
                                             _type.HRESULT]
                    add_PrimaryButtonClick: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IContentDialog, Windows.UI.Xaml.Controls.IContentDialogButtonClickEventArgs],
                                                       _Pointer[_struct.EventRegistrationToken]],
                                                      _type.HRESULT]
                    remove_PrimaryButtonClick: _Callable[[_struct.EventRegistrationToken],
                                                         _type.HRESULT]
                    add_SecondaryButtonClick: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IContentDialog, Windows.UI.Xaml.Controls.IContentDialogButtonClickEventArgs],
                                                         _Pointer[_struct.EventRegistrationToken]],
                                                        _type.HRESULT]
                    remove_SecondaryButtonClick: _Callable[[_struct.EventRegistrationToken],
                                                           _type.HRESULT]
                    Hide: _Callable[[],
                                    _type.HRESULT]
                    ShowAsync: _Callable[[_Pointer[Windows.Foundation.IAsyncOperation[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]]],
                                         _type.HRESULT]

                class IContentDialog2(IInspectable):
                    get_CloseButtonText: _Callable[[_Pointer[_type.HSTRING]],
                                                   _type.HRESULT]
                    put_CloseButtonText: _Callable[[_type.HSTRING],
                                                   _type.HRESULT]
                    get_CloseButtonCommand: _Callable[[_Pointer[Windows.UI.Xaml.Input.ICommand]],
                                                      _type.HRESULT]
                    put_CloseButtonCommand: _Callable[[Windows.UI.Xaml.Input.ICommand],
                                                      _type.HRESULT]
                    get_CloseButtonCommandParameter: _Callable[[_Pointer[IInspectable]],
                                                               _type.HRESULT]
                    put_CloseButtonCommandParameter: _Callable[[IInspectable],
                                                               _type.HRESULT]
                    get_PrimaryButtonStyle: _Callable[[_Pointer[Windows.UI.Xaml.IStyle]],
                                                      _type.HRESULT]
                    put_PrimaryButtonStyle: _Callable[[Windows.UI.Xaml.IStyle],
                                                      _type.HRESULT]
                    get_SecondaryButtonStyle: _Callable[[_Pointer[Windows.UI.Xaml.IStyle]],
                                                        _type.HRESULT]
                    put_SecondaryButtonStyle: _Callable[[Windows.UI.Xaml.IStyle],
                                                        _type.HRESULT]
                    get_CloseButtonStyle: _Callable[[_Pointer[Windows.UI.Xaml.IStyle]],
                                                    _type.HRESULT]
                    put_CloseButtonStyle: _Callable[[Windows.UI.Xaml.IStyle],
                                                    _type.HRESULT]
                    get_DefaultButton: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ContentDialogButton]],
                                                 _type.HRESULT]
                    put_DefaultButton: _Callable[[_enum.Windows.UI.Xaml.Controls.ContentDialogButton],
                                                 _type.HRESULT]
                    add_CloseButtonClick: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IContentDialog, Windows.UI.Xaml.Controls.IContentDialogButtonClickEventArgs],
                                                     _Pointer[_struct.EventRegistrationToken]],
                                                    _type.HRESULT]
                    remove_CloseButtonClick: _Callable[[_struct.EventRegistrationToken],
                                                       _type.HRESULT]

                class IContentDialog3(IInspectable):
                    ShowAsyncWithPlacement: _Callable[[_enum.Windows.UI.Xaml.Controls.ContentDialogPlacement,
                                                       _Pointer[Windows.Foundation.IAsyncOperation[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]]],
                                                      _type.HRESULT]

                class IContentDialogButtonClickDeferral(IInspectable):
                    Complete: _Callable[[],
                                        _type.HRESULT]

                class IContentDialogButtonClickEventArgs(IInspectable):
                    get_Cancel: _Callable[[_Pointer[_type.boolean]],
                                          _type.HRESULT]
                    put_Cancel: _Callable[[_type.boolean],
                                          _type.HRESULT]
                    GetDeferral: _Callable[[_Pointer[Windows.UI.Xaml.Controls.IContentDialogButtonClickDeferral]],
                                           _type.HRESULT]

                class IContentDialogClosedEventArgs(IInspectable):
                    get_Result: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]],
                                          _type.HRESULT]

                class IContentDialogClosingDeferral(IInspectable):
                    Complete: _Callable[[],
                                        _type.HRESULT]

                class IContentDialogClosingEventArgs(IInspectable):
                    get_Result: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ContentDialogResult]],
                                          _type.HRESULT]
                    get_Cancel: _Callable[[_Pointer[_type.boolean]],
                                          _type.HRESULT]
                    put_Cancel: _Callable[[_type.boolean],
                                          _type.HRESULT]
                    GetDeferral: _Callable[[_Pointer[Windows.UI.Xaml.Controls.IContentDialogClosingDeferral]],
                                           _type.HRESULT]

                class IContentDialogFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IContentDialog]],
                                              _type.HRESULT]

                class IContentDialogOpenedEventArgs(IInspectable):
                    pass

                class IContentDialogStatics(IInspectable):
                    get_TitleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                 _type.HRESULT]
                    get_TitleTemplateProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                    get_FullSizeDesiredProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_PrimaryButtonTextProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                             _type.HRESULT]
                    get_SecondaryButtonTextProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                    get_PrimaryButtonCommandProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]
                    get_SecondaryButtonCommandProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]
                    get_PrimaryButtonCommandParameterProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                         _type.HRESULT]
                    get_SecondaryButtonCommandParameterProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                           _type.HRESULT]
                    get_IsPrimaryButtonEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]
                    get_IsSecondaryButtonEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]

                class IContentDialogStatics2(IInspectable):
                    get_CloseButtonTextProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_CloseButtonCommandProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]
                    get_CloseButtonCommandParameterProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                       _type.HRESULT]
                    get_PrimaryButtonStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]
                    get_SecondaryButtonStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]
                    get_CloseButtonStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_DefaultButtonProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]

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
                    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],
                                            _type.HRESULT]
                    put_FontSize: _Callable[[_type.DOUBLE],
                                            _type.HRESULT]
                    get_FontFamily: _Callable[[_Pointer[Windows.UI.Xaml.Media.IFontFamily]],
                                              _type.HRESULT]
                    put_FontFamily: _Callable[[Windows.UI.Xaml.Media.IFontFamily],
                                              _type.HRESULT]
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
                    get_IsTabStop: _Callable[[_Pointer[_type.boolean]],
                                             _type.HRESULT]
                    put_IsTabStop: _Callable[[_type.boolean],
                                             _type.HRESULT]
                    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],
                                             _type.HRESULT]
                    put_IsEnabled: _Callable[[_type.boolean],
                                             _type.HRESULT]
                    get_TabIndex: _Callable[[_Pointer[_type.INT32]],
                                            _type.HRESULT]
                    put_TabIndex: _Callable[[_type.INT32],
                                            _type.HRESULT]
                    get_TabNavigation: _Callable
                    put_TabNavigation: _Callable
                    get_Template: _Callable[[_Pointer[Windows.UI.Xaml.Controls.IControlTemplate]],
                                            _type.HRESULT]
                    put_Template: _Callable[[Windows.UI.Xaml.Controls.IControlTemplate],
                                            _type.HRESULT]
                    get_Padding: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],
                                           _type.HRESULT]
                    put_Padding: _Callable[[_struct.Windows.UI.Xaml.Thickness],
                                           _type.HRESULT]
                    get_HorizontalContentAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.HorizontalAlignment]],
                                                              _type.HRESULT]
                    put_HorizontalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.HorizontalAlignment],
                                                              _type.HRESULT]
                    get_VerticalContentAlignment: _Callable[[_Pointer[_enum.Windows.UI.Xaml.VerticalAlignment]],
                                                            _type.HRESULT]
                    put_VerticalContentAlignment: _Callable[[_enum.Windows.UI.Xaml.VerticalAlignment],
                                                            _type.HRESULT]
                    get_Background: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                              _type.HRESULT]
                    put_Background: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                              _type.HRESULT]
                    get_BorderThickness: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Thickness]],
                                                   _type.HRESULT]
                    put_BorderThickness: _Callable[[_struct.Windows.UI.Xaml.Thickness],
                                                   _type.HRESULT]
                    get_BorderBrush: _Callable[[_Pointer[Windows.UI.Xaml.Media.IBrush]],
                                               _type.HRESULT]
                    put_BorderBrush: _Callable[[Windows.UI.Xaml.Media.IBrush],
                                               _type.HRESULT]
                    get_FocusState: _Callable[[_Pointer[_enum.Windows.UI.Xaml.FocusState]],
                                              _type.HRESULT]
                    add_IsEnabledChanged: _Callable[[Windows.UI.Xaml.IDependencyPropertyChangedEventHandler_impl,
                                                     _Pointer[_struct.EventRegistrationToken]],
                                                    _type.HRESULT]
                    remove_IsEnabledChanged: _Callable[[_struct.EventRegistrationToken],
                                                       _type.HRESULT]
                    ApplyTemplate: _Callable[[_Pointer[_type.boolean]],
                                             _type.HRESULT]
                    Focus: _Callable[[_enum.Windows.UI.Xaml.FocusState,
                                      _Pointer[_type.boolean]],
                                     _type.HRESULT]

                class IControl2(IInspectable):
                    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],
                                                            _type.HRESULT]
                    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],
                                                            _type.HRESULT]

                class IControl3(IInspectable):
                    get_UseSystemFocusVisuals: _Callable[[_Pointer[_type.boolean]],
                                                         _type.HRESULT]
                    put_UseSystemFocusVisuals: _Callable[[_type.boolean],
                                                         _type.HRESULT]

                class IControl4(IInspectable):
                    get_IsFocusEngagementEnabled: _Callable[[_Pointer[_type.boolean]],
                                                            _type.HRESULT]
                    put_IsFocusEngagementEnabled: _Callable[[_type.boolean],
                                                            _type.HRESULT]
                    get_IsFocusEngaged: _Callable[[_Pointer[_type.boolean]],
                                                  _type.HRESULT]
                    put_IsFocusEngaged: _Callable[[_type.boolean],
                                                  _type.HRESULT]
                    get_RequiresPointer: _Callable
                    put_RequiresPointer: _Callable
                    get_XYFocusLeft: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyObject]],
                                               _type.HRESULT]
                    put_XYFocusLeft: _Callable[[Windows.UI.Xaml.IDependencyObject],
                                               _type.HRESULT]
                    get_XYFocusRight: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyObject]],
                                                _type.HRESULT]
                    put_XYFocusRight: _Callable[[Windows.UI.Xaml.IDependencyObject],
                                                _type.HRESULT]
                    get_XYFocusUp: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyObject]],
                                             _type.HRESULT]
                    put_XYFocusUp: _Callable[[Windows.UI.Xaml.IDependencyObject],
                                             _type.HRESULT]
                    get_XYFocusDown: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyObject]],
                                               _type.HRESULT]
                    put_XYFocusDown: _Callable[[Windows.UI.Xaml.IDependencyObject],
                                               _type.HRESULT]
                    get_ElementSoundMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementSoundMode]],
                                                    _type.HRESULT]
                    put_ElementSoundMode: _Callable[[_enum.Windows.UI.Xaml.ElementSoundMode],
                                                    _type.HRESULT]
                    add_FocusEngaged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IControl, Windows.UI.Xaml.Controls.IFocusEngagedEventArgs],
                                                 _Pointer[_struct.EventRegistrationToken]],
                                                _type.HRESULT]
                    remove_FocusEngaged: _Callable[[_struct.EventRegistrationToken],
                                                   _type.HRESULT]
                    add_FocusDisengaged: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.IControl, Windows.UI.Xaml.Controls.IFocusDisengagedEventArgs],
                                                    _Pointer[_struct.EventRegistrationToken]],
                                                   _type.HRESULT]
                    remove_FocusDisengaged: _Callable[[_struct.EventRegistrationToken],
                                                      _type.HRESULT]
                    RemoveFocusEngagement: _Callable[[],
                                                     _type.HRESULT]

                class IControl5(IInspectable):
                    get_DefaultStyleResourceUri: _Callable[[_Pointer[Windows.Foundation.IUriRuntimeClass]],
                                                           _type.HRESULT]
                    put_DefaultStyleResourceUri: _Callable[[Windows.Foundation.IUriRuntimeClass],
                                                           _type.HRESULT]

                class IControl7(IInspectable):
                    get_BackgroundSizing: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.BackgroundSizing]],
                                                    _type.HRESULT]
                    put_BackgroundSizing: _Callable[[_enum.Windows.UI.Xaml.Controls.BackgroundSizing],
                                                    _type.HRESULT]
                    get_CornerRadius: _Callable[[_Pointer[_struct.Windows.UI.Xaml.CornerRadius]],
                                                _type.HRESULT]
                    put_CornerRadius: _Callable[[_struct.Windows.UI.Xaml.CornerRadius],
                                                _type.HRESULT]

                class IControlFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IControl]],
                                              _type.HRESULT]

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
                    get_DefaultStyleKey: _Callable[[_Pointer[IInspectable]],
                                                   _type.HRESULT]
                    put_DefaultStyleKey: _Callable[[IInspectable],
                                                   _type.HRESULT]
                    GetTemplateChild: _Callable[[_type.HSTRING,
                                                 _Pointer[Windows.UI.Xaml.IDependencyObject]],
                                                _type.HRESULT]

                class IControlStatics(IInspectable):
                    get_FontSizeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                    get_FontFamilyProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_FontWeightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_FontStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_FontStretchProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                       _type.HRESULT]
                    get_CharacterSpacingProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_ForegroundProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_IsTabStopProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_IsEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_TabIndexProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                    get_TabNavigationProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                    get_TemplateProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                    get_PaddingProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                    get_HorizontalContentAlignmentProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                      _type.HRESULT]
                    get_VerticalContentAlignmentProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]
                    get_BackgroundProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_BorderThicknessProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_BorderBrushProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                       _type.HRESULT]
                    get_DefaultStyleKeyProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_FocusStateProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]

                class IControlStatics2(IInspectable):
                    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]

                class IControlStatics3(IInspectable):
                    get_UseSystemFocusVisualsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                    get_IsTemplateFocusTargetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                    GetIsTemplateFocusTarget: _Callable[[Windows.UI.Xaml.IFrameworkElement,
                                                         _Pointer[_type.boolean]],
                                                        _type.HRESULT]
                    SetIsTemplateFocusTarget: _Callable[[Windows.UI.Xaml.IFrameworkElement,
                                                         _type.boolean],
                                                        _type.HRESULT]

                class IControlStatics4(IInspectable):
                    get_IsFocusEngagementEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]
                    get_IsFocusEngagedProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]
                    get_RequiresPointerProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_XYFocusLeftProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                       _type.HRESULT]
                    get_XYFocusRightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                        _type.HRESULT]
                    get_XYFocusUpProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_XYFocusDownProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                       _type.HRESULT]
                    get_ElementSoundModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]

                class IControlStatics5(IInspectable):
                    get_DefaultStyleResourceUriProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]
                    get_IsTemplateKeyTipTargetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]
                    GetIsTemplateKeyTipTarget: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                                          _Pointer[_type.boolean]],
                                                         _type.HRESULT]
                    SetIsTemplateKeyTipTarget: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                                          _type.boolean],
                                                         _type.HRESULT]

                class IControlStatics7(IInspectable):
                    get_BackgroundSizingProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_CornerRadiusProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                        _type.HRESULT]

                class IControlTemplate(IInspectable):
                    get_TargetType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],
                                              _type.HRESULT]
                    put_TargetType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName],
                                              _type.HRESULT]

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
                    get_Content: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                           _type.HRESULT]
                    put_Content: _Callable[[Windows.UI.Xaml.IUIElement],
                                           _type.HRESULT]
                    get_FlyoutPresenterStyle: _Callable[[_Pointer[Windows.UI.Xaml.IStyle]],
                                                        _type.HRESULT]
                    put_FlyoutPresenterStyle: _Callable[[Windows.UI.Xaml.IStyle],
                                                        _type.HRESULT]

                class IFlyoutFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IFlyout]],
                                              _type.HRESULT]

                class IFlyoutPresenter(IInspectable):
                    pass

                class IFlyoutPresenter2(IInspectable):
                    get_IsDefaultShadowEnabled: _Callable[[_Pointer[_type.boolean]],
                                                          _type.HRESULT]
                    put_IsDefaultShadowEnabled: _Callable[[_type.boolean],
                                                          _type.HRESULT]

                class IFlyoutPresenterFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IFlyoutPresenter]],
                                              _type.HRESULT]

                class IFlyoutPresenterStatics2(IInspectable):
                    get_IsDefaultShadowEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]

                class IFlyoutStatics(IInspectable):
                    get_ContentProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                    get_FlyoutPresenterStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]

                class IFocusDisengagedEventArgs(IInspectable):
                    pass

                class IFocusEngagedEventArgs(IInspectable):
                    pass

                class IFocusEngagedEventArgs2(IInspectable):
                    get_Handled: _Callable
                    put_Handled: _Callable

                class IFontIcon(IInspectable):
                    get_Glyph: _Callable[[_Pointer[_type.HSTRING]],
                                         _type.HRESULT]
                    put_Glyph: _Callable[[_type.HSTRING],
                                         _type.HRESULT]
                    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],
                                            _type.HRESULT]
                    put_FontSize: _Callable[[_type.DOUBLE],
                                            _type.HRESULT]
                    get_FontFamily: _Callable[[_Pointer[Windows.UI.Xaml.Media.IFontFamily]],
                                              _type.HRESULT]
                    put_FontFamily: _Callable[[Windows.UI.Xaml.Media.IFontFamily],
                                              _type.HRESULT]
                    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],
                                              _type.HRESULT]
                    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],
                                              _type.HRESULT]
                    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],
                                             _type.HRESULT]
                    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],
                                             _type.HRESULT]

                class IFontIcon2(IInspectable):
                    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],
                                                            _type.HRESULT]
                    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],
                                                            _type.HRESULT]

                class IFontIcon3(IInspectable):
                    get_MirroredWhenRightToLeft: _Callable[[_Pointer[_type.boolean]],
                                                           _type.HRESULT]
                    put_MirroredWhenRightToLeft: _Callable[[_type.boolean],
                                                           _type.HRESULT]

                class IFontIconFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IFontIcon]],
                                              _type.HRESULT]

                class IFontIconSource(IInspectable):
                    get_Glyph: _Callable[[_Pointer[_type.HSTRING]],
                                         _type.HRESULT]
                    put_Glyph: _Callable[[_type.HSTRING],
                                         _type.HRESULT]
                    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],
                                            _type.HRESULT]
                    put_FontSize: _Callable[[_type.DOUBLE],
                                            _type.HRESULT]
                    get_FontFamily: _Callable[[_Pointer[Windows.UI.Xaml.Media.IFontFamily]],
                                              _type.HRESULT]
                    put_FontFamily: _Callable[[Windows.UI.Xaml.Media.IFontFamily],
                                              _type.HRESULT]
                    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],
                                              _type.HRESULT]
                    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],
                                              _type.HRESULT]
                    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],
                                             _type.HRESULT]
                    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],
                                             _type.HRESULT]
                    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],
                                                            _type.HRESULT]
                    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],
                                                            _type.HRESULT]
                    get_MirroredWhenRightToLeft: _Callable[[_Pointer[_type.boolean]],
                                                           _type.HRESULT]
                    put_MirroredWhenRightToLeft: _Callable[[_type.boolean],
                                                           _type.HRESULT]

                class IFontIconSourceFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IFontIconSource]],
                                              _type.HRESULT]

                class IFontIconSourceStatics(IInspectable):
                    get_GlyphProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                 _type.HRESULT]
                    get_FontSizeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                    get_FontFamilyProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_FontWeightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_FontStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]
                    get_MirroredWhenRightToLeftProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]

                class IFontIconStatics(IInspectable):
                    get_GlyphProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                 _type.HRESULT]
                    get_FontSizeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                    get_FontFamilyProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_FontWeightProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                    get_FontStyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]

                class IFontIconStatics2(IInspectable):
                    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]

                class IFontIconStatics3(IInspectable):
                    get_MirroredWhenRightToLeftProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]

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
                    get_MenuFlyoutPresenterStyle: _Callable[[_Pointer[Windows.UI.Xaml.IStyle]],
                                                            _type.HRESULT]
                    put_MenuFlyoutPresenterStyle: _Callable[[Windows.UI.Xaml.IStyle],
                                                            _type.HRESULT]

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
                    get_Command: _Callable[[_Pointer[Windows.UI.Xaml.Input.ICommand]],
                                           _type.HRESULT]
                    put_Command: _Callable[[Windows.UI.Xaml.Input.ICommand],
                                           _type.HRESULT]
                    get_CommandParameter: _Callable[[_Pointer[IInspectable]],
                                                    _type.HRESULT]
                    put_CommandParameter: _Callable[[IInspectable],
                                                    _type.HRESULT]
                    add_Click: _Callable[[Windows.UI.Xaml.IRoutedEventHandler,
                                          _Pointer[_struct.EventRegistrationToken]],
                                         _type.HRESULT]
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
                    get_Data: _Callable[[_Pointer[Windows.UI.Xaml.Media.IGeometry]],
                                        _type.HRESULT]
                    put_Data: _Callable[[Windows.UI.Xaml.Media.IGeometry],
                                        _type.HRESULT]

                class IPathIconFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IPathIcon]],
                                              _type.HRESULT]

                class IPathIconSource(IInspectable):
                    get_Data: _Callable[[_Pointer[Windows.UI.Xaml.Media.IGeometry]],
                                        _type.HRESULT]
                    put_Data: _Callable[[Windows.UI.Xaml.Media.IGeometry],
                                        _type.HRESULT]

                class IPathIconSourceFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IPathIconSource]],
                                              _type.HRESULT]

                class IPathIconSourceStatics(IInspectable):
                    get_DataProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]

                class IPathIconStatics(IInspectable):
                    get_DataProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]

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
                    get_Symbol: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Symbol]],
                                          _type.HRESULT]
                    put_Symbol: _Callable[[_enum.Windows.UI.Xaml.Controls.Symbol],
                                          _type.HRESULT]

                class ISymbolIconFactory(IInspectable):
                    CreateInstanceWithSymbol: _Callable[[_enum.Windows.UI.Xaml.Controls.Symbol,
                                                         _Pointer[Windows.UI.Xaml.Controls.ISymbolIcon]],
                                                        _type.HRESULT]

                class ISymbolIconSource(IInspectable):
                    get_Symbol: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Symbol]],
                                          _type.HRESULT]
                    put_Symbol: _Callable[[_enum.Windows.UI.Xaml.Controls.Symbol],
                                          _type.HRESULT]

                class ISymbolIconSourceFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.ISymbolIconSource]],
                                              _type.HRESULT]

                class ISymbolIconSourceStatics(IInspectable):
                    get_SymbolProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                  _type.HRESULT]

                class ISymbolIconStatics(IInspectable):
                    get_SymbolProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                  _type.HRESULT]

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
                    get_HorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],
                                                    _type.HRESULT]
                    put_HorizontalOffset: _Callable[[_type.DOUBLE],
                                                    _type.HRESULT]
                    get_IsOpen: _Callable[[_Pointer[_type.boolean]],
                                          _type.HRESULT]
                    put_IsOpen: _Callable[[_type.boolean],
                                          _type.HRESULT]
                    get_Placement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode]],
                                             _type.HRESULT]
                    put_Placement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode],
                                             _type.HRESULT]
                    get_PlacementTarget: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                                   _type.HRESULT]
                    put_PlacementTarget: _Callable[[Windows.UI.Xaml.IUIElement],
                                                   _type.HRESULT]
                    get_VerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],
                                                  _type.HRESULT]
                    put_VerticalOffset: _Callable[[_type.DOUBLE],
                                                  _type.HRESULT]
                    get_TemplateSettings: _Callable[[_Pointer[Windows.UI.Xaml.Controls.Primitives.IToolTipTemplateSettings]],
                                                    _type.HRESULT]
                    add_Closed: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                           _Pointer[_struct.EventRegistrationToken]],
                                          _type.HRESULT]
                    remove_Closed: _Callable[[_struct.EventRegistrationToken],
                                             _type.HRESULT]
                    add_Opened: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                           _Pointer[_struct.EventRegistrationToken]],
                                          _type.HRESULT]
                    remove_Opened: _Callable[[_struct.EventRegistrationToken],
                                             _type.HRESULT]

                class IToolTip2(IInspectable):
                    get_PlacementRect: _Callable[[_Pointer[Windows.Foundation.IReference[_struct.Windows.Foundation.Rect]]],
                                                 _type.HRESULT]
                    put_PlacementRect: _Callable[[Windows.Foundation.IReference[_struct.Windows.Foundation.Rect]],
                                                 _type.HRESULT]

                class IToolTipFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Controls.IToolTip]],
                                              _type.HRESULT]

                class IToolTipService(IInspectable):
                    pass

                class IToolTipServiceStatics(IInspectable):
                    get_PlacementProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    GetPlacement: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                             _Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode]],
                                            _type.HRESULT]
                    SetPlacement: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                             _enum.Windows.UI.Xaml.Controls.Primitives.PlacementMode],
                                            _type.HRESULT]
                    get_PlacementTargetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    GetPlacementTarget: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                                   _Pointer[Windows.UI.Xaml.IUIElement]],
                                                  _type.HRESULT]
                    SetPlacementTarget: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                                   Windows.UI.Xaml.IUIElement],
                                                  _type.HRESULT]
                    get_ToolTipProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                    GetToolTip: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                           _Pointer[IInspectable]],
                                          _type.HRESULT]
                    SetToolTip: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                           IInspectable],
                                          _type.HRESULT]

                class IToolTipStatics(IInspectable):
                    get_HorizontalOffsetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_IsOpenProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                  _type.HRESULT]
                    get_PlacementProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_PlacementTargetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_VerticalOffsetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]

                class IToolTipStatics2(IInspectable):
                    get_PlacementRectProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]

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

                    class Maps:
                        class ICustomMapTileDataSource(IInspectable):
                            add_BitmapRequested: _Callable
                            remove_BitmapRequested: _Callable

                        class ICustomMapTileDataSourceFactory(IInspectable):
                            CreateInstance: _Callable

                        class IHttpMapTileDataSource(IInspectable):
                            get_UriFormatString: _Callable
                            put_UriFormatString: _Callable
                            get_AdditionalRequestHeaders: _Callable
                            get_AllowCaching: _Callable
                            put_AllowCaching: _Callable
                            add_UriRequested: _Callable
                            remove_UriRequested: _Callable

                        class IHttpMapTileDataSourceFactory(IInspectable):
                            CreateInstance: _Callable
                            CreateInstanceWithUriFormatString: _Callable

                        class ILocalMapTileDataSource(IInspectable):
                            get_UriFormatString: _Callable
                            put_UriFormatString: _Callable
                            add_UriRequested: _Callable
                            remove_UriRequested: _Callable

                        class ILocalMapTileDataSourceFactory(IInspectable):
                            CreateInstance: _Callable
                            CreateInstanceWithUriFormatString: _Callable

                        class IMapActualCameraChangedEventArgs(IInspectable):
                            get_Camera: _Callable

                        class IMapActualCameraChangedEventArgs2(IInspectable):
                            get_ChangeReason: _Callable

                        class IMapActualCameraChangingEventArgs(IInspectable):
                            get_Camera: _Callable

                        class IMapActualCameraChangingEventArgs2(IInspectable):
                            get_ChangeReason: _Callable

                        class IMapBillboard(IInspectable):
                            get_Location: _Callable
                            put_Location: _Callable
                            get_NormalizedAnchorPoint: _Callable
                            put_NormalizedAnchorPoint: _Callable
                            get_Image: _Callable
                            put_Image: _Callable
                            get_CollisionBehaviorDesired: _Callable
                            put_CollisionBehaviorDesired: _Callable
                            get_ReferenceCamera: _Callable

                        class IMapBillboardFactory(IInspectable):
                            CreateInstanceFromCamera: _Callable

                        class IMapBillboardStatics(IInspectable):
                            get_LocationProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                            get_NormalizedAnchorPointProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                         _type.HRESULT]
                            get_CollisionBehaviorDesiredProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                            _type.HRESULT]

                        class IMapCamera(IInspectable):
                            get_Location: _Callable
                            put_Location: _Callable
                            get_Heading: _Callable
                            put_Heading: _Callable
                            get_Pitch: _Callable
                            put_Pitch: _Callable
                            get_Roll: _Callable
                            put_Roll: _Callable
                            get_FieldOfView: _Callable
                            put_FieldOfView: _Callable

                        class IMapCameraFactory(IInspectable):
                            CreateInstanceWithLocation: _Callable
                            CreateInstanceWithLocationAndHeading: _Callable
                            CreateInstanceWithLocationHeadingAndPitch: _Callable
                            CreateInstanceWithLocationHeadingPitchRollAndFieldOfView: _Callable

                        class IMapContextRequestedEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElements: _Callable

                        class IMapControl(IInspectable):
                            get_Center: _Callable
                            put_Center: _Callable
                            get_Children: _Callable
                            get_ColorScheme: _Callable
                            put_ColorScheme: _Callable
                            get_DesiredPitch: _Callable
                            put_DesiredPitch: _Callable
                            get_Heading: _Callable
                            put_Heading: _Callable
                            get_LandmarksVisible: _Callable
                            put_LandmarksVisible: _Callable
                            get_LoadingStatus: _Callable
                            get_MapServiceToken: _Callable
                            put_MapServiceToken: _Callable
                            get_MaxZoomLevel: _Callable
                            get_MinZoomLevel: _Callable
                            get_PedestrianFeaturesVisible: _Callable
                            put_PedestrianFeaturesVisible: _Callable
                            get_Pitch: _Callable
                            get_Style: _Callable
                            put_Style: _Callable
                            get_TrafficFlowVisible: _Callable
                            put_TrafficFlowVisible: _Callable
                            get_TransformOrigin: _Callable
                            put_TransformOrigin: _Callable
                            get_WatermarkMode: _Callable
                            put_WatermarkMode: _Callable
                            get_ZoomLevel: _Callable
                            put_ZoomLevel: _Callable
                            get_MapElements: _Callable
                            get_Routes: _Callable
                            get_TileSources: _Callable
                            add_CenterChanged: _Callable
                            remove_CenterChanged: _Callable
                            add_HeadingChanged: _Callable
                            remove_HeadingChanged: _Callable
                            add_LoadingStatusChanged: _Callable
                            remove_LoadingStatusChanged: _Callable
                            add_MapDoubleTapped: _Callable
                            remove_MapDoubleTapped: _Callable
                            add_MapHolding: _Callable
                            remove_MapHolding: _Callable
                            add_MapTapped: _Callable
                            remove_MapTapped: _Callable
                            add_PitchChanged: _Callable
                            remove_PitchChanged: _Callable
                            add_TransformOriginChanged: _Callable
                            remove_TransformOriginChanged: _Callable
                            add_ZoomLevelChanged: _Callable
                            remove_ZoomLevelChanged: _Callable
                            FindMapElementsAtOffset: _Callable
                            GetLocationFromOffset: _Callable
                            GetOffsetFromLocation: _Callable
                            IsLocationInView: _Callable
                            TrySetViewBoundsAsync: _Callable
                            TrySetViewWithCenterAsync: _Callable
                            TrySetViewWithCenterAndZoomAsync: _Callable
                            TrySetViewWithCenterZoomHeadingAndPitchAsync: _Callable
                            TrySetViewWithCenterZoomHeadingPitchAndAnimationAsync: _Callable

                        class IMapControl2(IInspectable):
                            get_BusinessLandmarksVisible: _Callable
                            put_BusinessLandmarksVisible: _Callable
                            get_TransitFeaturesVisible: _Callable
                            put_TransitFeaturesVisible: _Callable
                            get_PanInteractionMode: _Callable
                            put_PanInteractionMode: _Callable
                            get_RotateInteractionMode: _Callable
                            put_RotateInteractionMode: _Callable
                            get_TiltInteractionMode: _Callable
                            put_TiltInteractionMode: _Callable
                            get_ZoomInteractionMode: _Callable
                            put_ZoomInteractionMode: _Callable
                            get_Is3DSupported: _Callable
                            get_IsStreetsideSupported: _Callable
                            get_Scene: _Callable
                            put_Scene: _Callable
                            get_ActualCamera: _Callable
                            get_TargetCamera: _Callable
                            get_CustomExperience: _Callable
                            put_CustomExperience: _Callable
                            add_MapElementClick: _Callable
                            remove_MapElementClick: _Callable
                            add_MapElementPointerEntered: _Callable
                            remove_MapElementPointerEntered: _Callable
                            add_MapElementPointerExited: _Callable
                            remove_MapElementPointerExited: _Callable
                            add_ActualCameraChanged: _Callable
                            remove_ActualCameraChanged: _Callable
                            add_ActualCameraChanging: _Callable
                            remove_ActualCameraChanging: _Callable
                            add_TargetCameraChanged: _Callable
                            remove_TargetCameraChanged: _Callable
                            add_CustomExperienceChanged: _Callable
                            remove_CustomExperienceChanged: _Callable
                            StartContinuousRotate: _Callable
                            StopContinuousRotate: _Callable
                            StartContinuousTilt: _Callable
                            StopContinuousTilt: _Callable
                            StartContinuousZoom: _Callable
                            StopContinuousZoom: _Callable
                            TryRotateAsync: _Callable
                            TryRotateToAsync: _Callable
                            TryTiltAsync: _Callable
                            TryTiltToAsync: _Callable
                            TryZoomInAsync: _Callable
                            TryZoomOutAsync: _Callable
                            TryZoomToAsync: _Callable
                            TrySetSceneAsync: _Callable
                            TrySetSceneWithAnimationAsync: _Callable

                        class IMapControl3(IInspectable):
                            add_MapRightTapped: _Callable
                            remove_MapRightTapped: _Callable

                        class IMapControl4(IInspectable):
                            get_BusinessLandmarksEnabled: _Callable
                            put_BusinessLandmarksEnabled: _Callable
                            get_TransitFeaturesEnabled: _Callable
                            put_TransitFeaturesEnabled: _Callable
                            GetVisibleRegion: _Callable

                        class IMapControl5(IInspectable):
                            get_MapProjection: _Callable
                            put_MapProjection: _Callable
                            get_StyleSheet: _Callable
                            put_StyleSheet: _Callable
                            get_ViewPadding: _Callable
                            put_ViewPadding: _Callable
                            add_MapContextRequested: _Callable
                            remove_MapContextRequested: _Callable
                            FindMapElementsAtOffsetWithRadius: _Callable
                            GetLocationFromOffsetWithReferenceSystem: _Callable
                            StartContinuousPan: _Callable
                            StopContinuousPan: _Callable
                            TryPanAsync: _Callable
                            TryPanToAsync: _Callable

                        class IMapControl6(IInspectable):
                            get_Layers: _Callable
                            put_Layers: _Callable
                            TryGetLocationFromOffset: _Callable
                            TryGetLocationFromOffsetWithReferenceSystem: _Callable

                        class IMapControl7(IInspectable):
                            get_Region: _Callable
                            put_Region: _Callable

                        class IMapControl8(IInspectable):
                            get_CanTiltDown: _Callable
                            get_CanTiltUp: _Callable
                            get_CanZoomIn: _Callable
                            get_CanZoomOut: _Callable

                        class IMapControlBusinessLandmarkClickEventArgs(IInspectable):
                            get_LocalLocations: _Callable

                        class IMapControlBusinessLandmarkPointerEnteredEventArgs(IInspectable):
                            get_LocalLocations: _Callable

                        class IMapControlBusinessLandmarkPointerExitedEventArgs(IInspectable):
                            get_LocalLocations: _Callable

                        class IMapControlBusinessLandmarkRightTappedEventArgs(IInspectable):
                            get_LocalLocations: _Callable

                        class IMapControlDataHelper(IInspectable):
                            add_BusinessLandmarkClick: _Callable
                            remove_BusinessLandmarkClick: _Callable
                            add_TransitFeatureClick: _Callable
                            remove_TransitFeatureClick: _Callable
                            add_BusinessLandmarkRightTapped: _Callable
                            remove_BusinessLandmarkRightTapped: _Callable
                            add_TransitFeatureRightTapped: _Callable
                            remove_TransitFeatureRightTapped: _Callable

                        class IMapControlDataHelper2(IInspectable):
                            add_BusinessLandmarkPointerEntered: _Callable
                            remove_BusinessLandmarkPointerEntered: _Callable
                            add_TransitFeaturePointerEntered: _Callable
                            remove_TransitFeaturePointerEntered: _Callable
                            add_BusinessLandmarkPointerExited: _Callable
                            remove_BusinessLandmarkPointerExited: _Callable
                            add_TransitFeaturePointerExited: _Callable
                            remove_TransitFeaturePointerExited: _Callable

                        class IMapControlDataHelperFactory(IInspectable):
                            CreateInstance: _Callable

                        class IMapControlDataHelperStatics(IInspectable):
                            CreateMapControl: _Callable

                        class IMapControlStatics(IInspectable):
                            get_CenterProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]
                            get_ChildrenProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                            get_ColorSchemeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                            get_DesiredPitchProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]
                            get_HeadingProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                            get_LandmarksVisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]
                            get_LoadingStatusProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                            get_MapServiceTokenProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]
                            get_PedestrianFeaturesVisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                             _type.HRESULT]
                            get_PitchProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                            get_StyleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                            get_TrafficFlowVisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                      _type.HRESULT]
                            get_TransformOriginProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]
                            get_WatermarkModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                            get_ZoomLevelProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                             _type.HRESULT]
                            get_MapElementsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                            get_RoutesProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]
                            get_TileSourcesProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                            get_LocationProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                            GetLocation: _Callable
                            SetLocation: _Callable
                            get_NormalizedAnchorPointProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                         _type.HRESULT]
                            GetNormalizedAnchorPoint: _Callable
                            SetNormalizedAnchorPoint: _Callable

                        class IMapControlStatics2(IInspectable):
                            get_BusinessLandmarksVisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                            _type.HRESULT]
                            get_TransitFeaturesVisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                          _type.HRESULT]
                            get_PanInteractionModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                      _type.HRESULT]
                            get_RotateInteractionModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                         _type.HRESULT]
                            get_TiltInteractionModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                       _type.HRESULT]
                            get_ZoomInteractionModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                       _type.HRESULT]
                            get_Is3DSupportedProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                            get_IsStreetsideSupportedProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                         _type.HRESULT]
                            get_SceneProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]

                        class IMapControlStatics4(IInspectable):
                            get_BusinessLandmarksEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                            _type.HRESULT]
                            get_TransitFeaturesEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                          _type.HRESULT]

                        class IMapControlStatics5(IInspectable):
                            get_MapProjectionProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                            get_StyleSheetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]
                            get_ViewPaddingProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]

                        class IMapControlStatics6(IInspectable):
                            get_LayersProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]

                        class IMapControlStatics7(IInspectable):
                            get_RegionProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]

                        class IMapControlStatics8(IInspectable):
                            get_CanTiltDownProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                            get_CanTiltUpProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                             _type.HRESULT]
                            get_CanZoomInProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                             _type.HRESULT]
                            get_CanZoomOutProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]

                        class IMapControlTransitFeatureClickEventArgs(IInspectable):
                            get_DisplayName: _Callable
                            get_Location: _Callable
                            get_TransitProperties: _Callable

                        class IMapControlTransitFeaturePointerEnteredEventArgs(IInspectable):
                            get_DisplayName: _Callable
                            get_Location: _Callable
                            get_TransitProperties: _Callable

                        class IMapControlTransitFeaturePointerExitedEventArgs(IInspectable):
                            get_DisplayName: _Callable
                            get_Location: _Callable
                            get_TransitProperties: _Callable

                        class IMapControlTransitFeatureRightTappedEventArgs(IInspectable):
                            get_DisplayName: _Callable
                            get_Location: _Callable
                            get_TransitProperties: _Callable

                        class IMapCustomExperience(IInspectable):
                            pass

                        class IMapCustomExperienceChangedEventArgs(IInspectable):
                            pass

                        class IMapCustomExperienceFactory(IInspectable):
                            CreateInstance: _Callable

                        class IMapElement(IInspectable):
                            get_ZIndex: _Callable
                            put_ZIndex: _Callable
                            get_Visible: _Callable
                            put_Visible: _Callable

                        class IMapElement2(IInspectable):
                            get_MapTabIndex: _Callable
                            put_MapTabIndex: _Callable

                        class IMapElement3(IInspectable):
                            get_MapStyleSheetEntry: _Callable
                            put_MapStyleSheetEntry: _Callable
                            get_MapStyleSheetEntryState: _Callable
                            put_MapStyleSheetEntryState: _Callable
                            get_Tag: _Callable
                            put_Tag: _Callable

                        class IMapElement3D(IInspectable):
                            get_Location: _Callable
                            put_Location: _Callable
                            get_Model: _Callable
                            put_Model: _Callable
                            get_Heading: _Callable
                            put_Heading: _Callable
                            get_Pitch: _Callable
                            put_Pitch: _Callable
                            get_Roll: _Callable
                            put_Roll: _Callable
                            get_Scale: _Callable
                            put_Scale: _Callable

                        class IMapElement3DStatics(IInspectable):
                            get_LocationProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                            get_HeadingProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                            get_PitchProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                            get_RollProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                        _type.HRESULT]
                            get_ScaleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]

                        class IMapElement4(IInspectable):
                            get_IsEnabled: _Callable
                            put_IsEnabled: _Callable

                        class IMapElementClickEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElements: _Callable

                        class IMapElementFactory(IInspectable):
                            CreateInstance: _Callable

                        class IMapElementPointerEnteredEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElement: _Callable

                        class IMapElementPointerExitedEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElement: _Callable

                        class IMapElementStatics(IInspectable):
                            get_ZIndexProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]
                            get_VisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]

                        class IMapElementStatics2(IInspectable):
                            get_MapTabIndexProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]

                        class IMapElementStatics3(IInspectable):
                            get_MapStyleSheetEntryProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                      _type.HRESULT]
                            get_MapStyleSheetEntryStateProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                           _type.HRESULT]
                            get_TagProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                       _type.HRESULT]

                        class IMapElementStatics4(IInspectable):
                            get_IsEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                             _type.HRESULT]

                        class IMapElementsLayer(IInspectable):
                            get_MapElements: _Callable
                            put_MapElements: _Callable
                            add_MapElementClick: _Callable
                            remove_MapElementClick: _Callable
                            add_MapElementPointerEntered: _Callable
                            remove_MapElementPointerEntered: _Callable
                            add_MapElementPointerExited: _Callable
                            remove_MapElementPointerExited: _Callable
                            add_MapContextRequested: _Callable
                            remove_MapContextRequested: _Callable

                        class IMapElementsLayerClickEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElements: _Callable

                        class IMapElementsLayerContextRequestedEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElements: _Callable

                        class IMapElementsLayerPointerEnteredEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElement: _Callable

                        class IMapElementsLayerPointerExitedEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable
                            get_MapElement: _Callable

                        class IMapElementsLayerStatics(IInspectable):
                            get_MapElementsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]

                        class IMapIcon(IInspectable):
                            get_Location: _Callable
                            put_Location: _Callable
                            get_Title: _Callable
                            put_Title: _Callable
                            get_NormalizedAnchorPoint: _Callable
                            put_NormalizedAnchorPoint: _Callable
                            get_Image: _Callable
                            put_Image: _Callable

                        class IMapIcon2(IInspectable):
                            get_CollisionBehaviorDesired: _Callable
                            put_CollisionBehaviorDesired: _Callable

                        class IMapIconStatics(IInspectable):
                            get_LocationProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                            get_TitleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                            get_NormalizedAnchorPointProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                         _type.HRESULT]

                        class IMapIconStatics2(IInspectable):
                            get_CollisionBehaviorDesiredProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                            _type.HRESULT]

                        class IMapInputEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable

                        class IMapItemsControl(IInspectable):
                            get_ItemsSource: _Callable
                            put_ItemsSource: _Callable
                            get_Items: _Callable
                            get_ItemTemplate: _Callable
                            put_ItemTemplate: _Callable

                        class IMapItemsControlStatics(IInspectable):
                            get_ItemsSourceProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                            get_ItemsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                            get_ItemTemplateProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]

                        class IMapLayer(IInspectable):
                            get_MapTabIndex: _Callable
                            put_MapTabIndex: _Callable
                            get_Visible: _Callable
                            put_Visible: _Callable
                            get_ZIndex: _Callable
                            put_ZIndex: _Callable

                        class IMapLayerFactory(IInspectable):
                            CreateInstance: _Callable

                        class IMapLayerStatics(IInspectable):
                            get_MapTabIndexProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                               _type.HRESULT]
                            get_VisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                            get_ZIndexProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]

                        class IMapModel3D(IInspectable):
                            pass

                        class IMapModel3DFactory(IInspectable):
                            CreateInstance: _Callable

                        class IMapModel3DStatics(IInspectable):
                            CreateFrom3MFAsync: _Callable
                            CreateFrom3MFWithShadingOptionAsync: _Callable

                        class IMapPolygon(IInspectable):
                            get_Path: _Callable
                            put_Path: _Callable
                            get_StrokeColor: _Callable
                            put_StrokeColor: _Callable
                            get_StrokeThickness: _Callable
                            put_StrokeThickness: _Callable
                            get_StrokeDashed: _Callable
                            put_StrokeDashed: _Callable
                            get_FillColor: _Callable
                            put_FillColor: _Callable

                        class IMapPolygon2(IInspectable):
                            get_Paths: _Callable

                        class IMapPolygonStatics(IInspectable):
                            get_PathProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                        _type.HRESULT]
                            get_StrokeThicknessProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]
                            get_StrokeDashedProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]

                        class IMapPolyline(IInspectable):
                            get_Path: _Callable
                            put_Path: _Callable
                            get_StrokeColor: _Callable
                            put_StrokeColor: _Callable
                            get_StrokeThickness: _Callable
                            put_StrokeThickness: _Callable
                            get_StrokeDashed: _Callable
                            put_StrokeDashed: _Callable

                        class IMapPolylineStatics(IInspectable):
                            get_PathProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                        _type.HRESULT]
                            get_StrokeDashedProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]

                        class IMapRightTappedEventArgs(IInspectable):
                            get_Position: _Callable
                            get_Location: _Callable

                        class IMapRouteView(IInspectable):
                            get_RouteColor: _Callable
                            put_RouteColor: _Callable
                            get_OutlineColor: _Callable
                            put_OutlineColor: _Callable
                            get_Route: _Callable

                        class IMapRouteViewFactory(IInspectable):
                            CreateInstanceWithMapRoute: _Callable

                        class IMapScene(IInspectable):
                            get_TargetCamera: _Callable
                            add_TargetCameraChanged: _Callable
                            remove_TargetCameraChanged: _Callable

                        class IMapSceneStatics(IInspectable):
                            CreateFromBoundingBox: _Callable
                            CreateFromBoundingBoxWithHeadingAndPitch: _Callable
                            CreateFromCamera: _Callable
                            CreateFromLocation: _Callable
                            CreateFromLocationWithHeadingAndPitch: _Callable
                            CreateFromLocationAndRadius: _Callable
                            CreateFromLocationAndRadiusWithHeadingAndPitch: _Callable
                            CreateFromLocations: _Callable
                            CreateFromLocationsWithHeadingAndPitch: _Callable

                        class IMapStyleSheet(IInspectable):
                            pass

                        class IMapStyleSheetEntriesStatics(IInspectable):
                            get_Area: _Callable
                            get_Airport: _Callable
                            get_Cemetery: _Callable
                            get_Continent: _Callable
                            get_Education: _Callable
                            get_IndigenousPeoplesReserve: _Callable
                            get_Island: _Callable
                            get_Medical: _Callable
                            get_Military: _Callable
                            get_Nautical: _Callable
                            get_Neighborhood: _Callable
                            get_Runway: _Callable
                            get_Sand: _Callable
                            get_ShoppingCenter: _Callable
                            get_Stadium: _Callable
                            get_Vegetation: _Callable
                            get_Forest: _Callable
                            get_GolfCourse: _Callable
                            get_Park: _Callable
                            get_PlayingField: _Callable
                            get_Reserve: _Callable
                            get_Point: _Callable
                            get_NaturalPoint: _Callable
                            get_Peak: _Callable
                            get_VolcanicPeak: _Callable
                            get_WaterPoint: _Callable
                            get_PointOfInterest: _Callable
                            get_Business: _Callable
                            get_FoodPoint: _Callable
                            get_PopulatedPlace: _Callable
                            get_Capital: _Callable
                            get_AdminDistrictCapital: _Callable
                            get_CountryRegionCapital: _Callable
                            get_RoadShield: _Callable
                            get_RoadExit: _Callable
                            get_Transit: _Callable
                            get_Political: _Callable
                            get_CountryRegion: _Callable
                            get_AdminDistrict: _Callable
                            get_District: _Callable
                            get_Structure: _Callable
                            get_Building: _Callable
                            get_EducationBuilding: _Callable
                            get_MedicalBuilding: _Callable
                            get_TransitBuilding: _Callable
                            get_Transportation: _Callable
                            get_Road: _Callable
                            get_ControlledAccessHighway: _Callable
                            get_HighSpeedRamp: _Callable
                            get_Highway: _Callable
                            get_MajorRoad: _Callable
                            get_ArterialRoad: _Callable
                            get_Street: _Callable
                            get_Ramp: _Callable
                            get_UnpavedStreet: _Callable
                            get_TollRoad: _Callable
                            get_Railway: _Callable
                            get_Trail: _Callable
                            get_WaterRoute: _Callable
                            get_Water: _Callable
                            get_River: _Callable
                            get_RouteLine: _Callable
                            get_WalkingRoute: _Callable
                            get_DrivingRoute: _Callable

                        class IMapStyleSheetEntryStatesStatics(IInspectable):
                            get_Disabled: _Callable
                            get_Hover: _Callable
                            get_Selected: _Callable

                        class IMapStyleSheetStatics(IInspectable):
                            Aerial: _Callable
                            AerialWithOverlay: _Callable
                            RoadLight: _Callable
                            RoadDark: _Callable
                            RoadHighContrastLight: _Callable
                            RoadHighContrastDark: _Callable
                            Combine: _Callable
                            ParseFromJson: _Callable
                            TryParseFromJson: _Callable

                        class IMapTargetCameraChangedEventArgs(IInspectable):
                            get_Camera: _Callable

                        class IMapTargetCameraChangedEventArgs2(IInspectable):
                            get_ChangeReason: _Callable

                        class IMapTileBitmapRequest(IInspectable):
                            get_PixelData: _Callable
                            put_PixelData: _Callable
                            GetDeferral: _Callable

                        class IMapTileBitmapRequestDeferral(IInspectable):
                            Complete: _Callable

                        class IMapTileBitmapRequestedEventArgs(IInspectable):
                            get_X: _Callable
                            get_Y: _Callable
                            get_ZoomLevel: _Callable
                            get_Request: _Callable

                        class IMapTileBitmapRequestedEventArgs2(IInspectable):
                            get_FrameIndex: _Callable

                        class IMapTileDataSource(IInspectable):
                            pass

                        class IMapTileDataSourceFactory(IInspectable):
                            CreateInstance: _Callable

                        class IMapTileSource(IInspectable):
                            get_DataSource: _Callable
                            put_DataSource: _Callable
                            get_Layer: _Callable
                            put_Layer: _Callable
                            get_ZoomLevelRange: _Callable
                            put_ZoomLevelRange: _Callable
                            get_Bounds: _Callable
                            put_Bounds: _Callable
                            get_AllowOverstretch: _Callable
                            put_AllowOverstretch: _Callable
                            get_IsFadingEnabled: _Callable
                            put_IsFadingEnabled: _Callable
                            get_IsTransparencyEnabled: _Callable
                            put_IsTransparencyEnabled: _Callable
                            get_IsRetryEnabled: _Callable
                            put_IsRetryEnabled: _Callable
                            get_ZIndex: _Callable
                            put_ZIndex: _Callable
                            get_TilePixelSize: _Callable
                            put_TilePixelSize: _Callable
                            get_Visible: _Callable
                            put_Visible: _Callable

                        class IMapTileSource2(IInspectable):
                            get_AnimationState: _Callable
                            get_AutoPlay: _Callable
                            put_AutoPlay: _Callable
                            get_FrameCount: _Callable
                            put_FrameCount: _Callable
                            get_FrameDuration: _Callable
                            put_FrameDuration: _Callable
                            Pause: _Callable
                            Play: _Callable
                            Stop: _Callable

                        class IMapTileSourceFactory(IInspectable):
                            CreateInstance: _Callable
                            CreateInstanceWithDataSource: _Callable
                            CreateInstanceWithDataSourceAndZoomRange: _Callable
                            CreateInstanceWithDataSourceZoomRangeAndBounds: _Callable
                            CreateInstanceWithDataSourceZoomRangeBoundsAndTileSize: _Callable

                        class IMapTileSourceStatics(IInspectable):
                            get_DataSourceProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]
                            get_LayerProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                            get_ZoomLevelRangeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]
                            get_BoundsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]
                            get_AllowOverstretchProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                    _type.HRESULT]
                            get_IsFadingEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                   _type.HRESULT]
                            get_IsTransparencyEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                         _type.HRESULT]
                            get_IsRetryEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]
                            get_ZIndexProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]
                            get_TilePixelSizeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                            get_VisibleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]

                        class IMapTileSourceStatics2(IInspectable):
                            get_AnimationStateProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]
                            get_AutoPlayProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                            get_FrameCountProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]
                            get_FrameDurationProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]

                        class IMapTileUriRequest(IInspectable):
                            get_Uri: _Callable
                            put_Uri: _Callable
                            GetDeferral: _Callable

                        class IMapTileUriRequestDeferral(IInspectable):
                            Complete: _Callable

                        class IMapTileUriRequestedEventArgs(IInspectable):
                            get_X: _Callable
                            get_Y: _Callable
                            get_ZoomLevel: _Callable
                            get_Request: _Callable

                        class IMapTileUriRequestedEventArgs2(IInspectable):
                            get_FrameIndex: _Callable

                        class IStreetsideExperience(IInspectable):
                            get_AddressTextVisible: _Callable
                            put_AddressTextVisible: _Callable
                            get_CursorVisible: _Callable
                            put_CursorVisible: _Callable
                            get_OverviewMapVisible: _Callable
                            put_OverviewMapVisible: _Callable
                            get_StreetLabelsVisible: _Callable
                            put_StreetLabelsVisible: _Callable
                            get_ExitButtonVisible: _Callable
                            put_ExitButtonVisible: _Callable
                            get_ZoomButtonsVisible: _Callable
                            put_ZoomButtonsVisible: _Callable

                        class IStreetsideExperienceFactory(IInspectable):
                            CreateInstanceWithPanorama: _Callable
                            CreateInstanceWithPanoramaHeadingPitchAndFieldOfView: _Callable

                        class IStreetsidePanorama(IInspectable):
                            get_Location: _Callable

                        class IStreetsidePanoramaStatics(IInspectable):
                            FindNearbyWithLocationAsync: _Callable
                            FindNearbyWithLocationAndRadiusAsync: _Callable

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
                        get_ClickMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.ClickMode]],
                                                 _type.HRESULT]
                        put_ClickMode: _Callable[[_enum.Windows.UI.Xaml.Controls.ClickMode],
                                                 _type.HRESULT]
                        get_IsPointerOver: _Callable[[_Pointer[_type.boolean]],
                                                     _type.HRESULT]
                        get_IsPressed: _Callable[[_Pointer[_type.boolean]],
                                                 _type.HRESULT]
                        get_Command: _Callable[[_Pointer[Windows.UI.Xaml.Input.ICommand]],
                                               _type.HRESULT]
                        put_Command: _Callable[[Windows.UI.Xaml.Input.ICommand],
                                               _type.HRESULT]
                        get_CommandParameter: _Callable[[_Pointer[IInspectable]],
                                                        _type.HRESULT]
                        put_CommandParameter: _Callable[[IInspectable],
                                                        _type.HRESULT]
                        add_Click: _Callable[[Windows.UI.Xaml.IRoutedEventHandler_impl,
                                              _Pointer[_struct.EventRegistrationToken]],
                                             _type.HRESULT]
                        remove_Click: _Callable[[_struct.EventRegistrationToken],
                                                _type.HRESULT]

                    class IButtonBaseFactory(IInspectable):
                        CreateInstance: _Callable[[IInspectable,
                                                   _Pointer[IInspectable],
                                                   _Pointer[Windows.UI.Xaml.Controls.Primitives.IButtonBase]],
                                                  _type.HRESULT]

                    class IButtonBaseStatics(IInspectable):
                        get_ClickModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                        get_IsPointerOverProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                             _type.HRESULT]
                        get_IsPressedProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                        get_CommandProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                       _type.HRESULT]
                        get_CommandParameterProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]

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
                        get_Placement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode]],
                                                 _type.HRESULT]
                        put_Placement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],
                                                 _type.HRESULT]
                        add_Opened: _Callable[[Windows.Foundation.ITypedEventHandler_impl[IInspectable],
                                               _Pointer[_struct.EventRegistrationToken]],
                                              _type.HRESULT]
                        remove_Opened: _Callable[[_struct.EventRegistrationToken],
                                                 _type.HRESULT]
                        add_Closed: _Callable[[Windows.Foundation.ITypedEventHandler_impl[IInspectable],
                                               _Pointer[_struct.EventRegistrationToken]],
                                              _type.HRESULT]
                        remove_Closed: _Callable[[_struct.EventRegistrationToken],
                                                 _type.HRESULT]
                        add_Opening: _Callable[[Windows.Foundation.ITypedEventHandler_impl[IInspectable],
                                                _Pointer[_struct.EventRegistrationToken]],
                                               _type.HRESULT]
                        remove_Opening: _Callable[[_struct.EventRegistrationToken],
                                                  _type.HRESULT]
                        ShowAt: _Callable[[Windows.UI.Xaml.IFrameworkElement],
                                          _type.HRESULT]
                        Hide: _Callable[[],
                                        _type.HRESULT]

                    class IFlyoutBase2(IInspectable):
                        get_Target: _Callable[[_Pointer[Windows.UI.Xaml.IFrameworkElement]],
                                              _type.HRESULT]
                        get_AllowFocusOnInteraction: _Callable[[_Pointer[_type.boolean]],
                                                               _type.HRESULT]
                        put_AllowFocusOnInteraction: _Callable[[_type.boolean],
                                                               _type.HRESULT]
                        get_LightDismissOverlayMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode]],
                                                               _type.HRESULT]
                        put_LightDismissOverlayMode: _Callable[[_enum.Windows.UI.Xaml.Controls.LightDismissOverlayMode],
                                                               _type.HRESULT]
                        get_AllowFocusWhenDisabled: _Callable[[_Pointer[_type.boolean]],
                                                              _type.HRESULT]
                        put_AllowFocusWhenDisabled: _Callable[[_type.boolean],
                                                              _type.HRESULT]
                        get_ElementSoundMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.ElementSoundMode]],
                                                        _type.HRESULT]
                        put_ElementSoundMode: _Callable[[_enum.Windows.UI.Xaml.ElementSoundMode],
                                                        _type.HRESULT]
                        add_Closing: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Controls.Primitives.IFlyoutBase, Windows.UI.Xaml.Controls.Primitives.IFlyoutBaseClosingEventArgs],
                                                _Pointer[_struct.EventRegistrationToken]],
                                               _type.HRESULT]
                        remove_Closing: _Callable[[_struct.EventRegistrationToken],
                                                  _type.HRESULT]

                    class IFlyoutBase3(IInspectable):
                        get_OverlayInputPassThroughElement: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyObject]],
                                                                      _type.HRESULT]
                        put_OverlayInputPassThroughElement: _Callable[[Windows.UI.Xaml.IDependencyObject],
                                                                      _type.HRESULT]

                    class IFlyoutBase4(IInspectable):
                        TryInvokeKeyboardAccelerator: _Callable[[Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs],
                                                                _type.HRESULT]

                    class IFlyoutBase5(IInspectable):
                        get_ShowMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode]],
                                                _type.HRESULT]
                        put_ShowMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode],
                                                _type.HRESULT]
                        get_InputDevicePrefersPrimaryCommands: _Callable[[_Pointer[_type.boolean]],
                                                                         _type.HRESULT]
                        get_AreOpenCloseAnimationsEnabled: _Callable[[_Pointer[_type.boolean]],
                                                                     _type.HRESULT]
                        put_AreOpenCloseAnimationsEnabled: _Callable[[_type.boolean],
                                                                     _type.HRESULT]
                        get_IsOpen: _Callable[[_Pointer[_type.boolean]],
                                              _type.HRESULT]
                        ShowAt: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                           Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions],
                                          _type.HRESULT]

                    class IFlyoutBase6(IInspectable):
                        get_ShouldConstrainToRootBounds: _Callable[[_Pointer[_type.boolean]],
                                                                   _type.HRESULT]
                        put_ShouldConstrainToRootBounds: _Callable[[_type.boolean],
                                                                   _type.HRESULT]
                        get_IsConstrainedToRootBounds: _Callable[[_Pointer[_type.boolean]],
                                                                 _type.HRESULT]
                        get_XamlRoot: _Callable[[_Pointer[Windows.UI.Xaml.IXamlRoot]],
                                                _type.HRESULT]
                        put_XamlRoot: _Callable[[Windows.UI.Xaml.IXamlRoot],
                                                _type.HRESULT]

                    class IFlyoutBaseClosingEventArgs(IInspectable):
                        get_Cancel: _Callable[[_Pointer[_type.boolean]],
                                              _type.HRESULT]
                        put_Cancel: _Callable[[_type.boolean],
                                              _type.HRESULT]

                    class IFlyoutBaseFactory(IInspectable):
                        CreateInstance: _Callable[[IInspectable,
                                                   _Pointer[IInspectable],
                                                   _Pointer[Windows.UI.Xaml.Controls.Primitives.IFlyoutBase]],
                                                  _type.HRESULT]

                    class IFlyoutBaseOverrides(IInspectable):
                        CreatePresenter: _Callable[[_Pointer[Windows.UI.Xaml.Controls.IControl]],
                                                   _type.HRESULT]

                    class IFlyoutBaseOverrides4(IInspectable):
                        OnProcessKeyboardAccelerators: _Callable[[Windows.UI.Xaml.Input.IProcessKeyboardAcceleratorEventArgs],
                                                                 _type.HRESULT]

                    class IFlyoutBaseStatics(IInspectable):
                        get_PlacementProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                        get_AttachedFlyoutProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]
                        GetAttachedFlyout: _Callable[[Windows.UI.Xaml.IFrameworkElement,
                                                      _Pointer[Windows.UI.Xaml.Controls.Primitives.IFlyoutBase]],
                                                     _type.HRESULT]
                        SetAttachedFlyout: _Callable[[Windows.UI.Xaml.IFrameworkElement,
                                                      Windows.UI.Xaml.Controls.Primitives.IFlyoutBase],
                                                     _type.HRESULT]
                        ShowAttachedFlyout: _Callable[[Windows.UI.Xaml.IFrameworkElement],
                                                      _type.HRESULT]

                    class IFlyoutBaseStatics2(IInspectable):
                        get_AllowFocusOnInteractionProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                       _type.HRESULT]
                        get_LightDismissOverlayModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                       _type.HRESULT]
                        get_AllowFocusWhenDisabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                      _type.HRESULT]
                        get_ElementSoundModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                _type.HRESULT]

                    class IFlyoutBaseStatics3(IInspectable):
                        get_OverlayInputPassThroughElementProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                              _type.HRESULT]

                    class IFlyoutBaseStatics5(IInspectable):
                        get_TargetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]
                        get_ShowModeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                        _type.HRESULT]
                        get_InputDevicePrefersPrimaryCommandsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                                 _type.HRESULT]
                        get_AreOpenCloseAnimationsEnabledProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                             _type.HRESULT]
                        get_IsOpenProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                      _type.HRESULT]

                    class IFlyoutBaseStatics6(IInspectable):
                        get_ShouldConstrainToRootBoundsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                           _type.HRESULT]

                    class IFlyoutShowOptions(IInspectable):
                        get_Position: _Callable[[_Pointer[Windows.Foundation.IReference[_struct.Windows.Foundation.Point]]],
                                                _type.HRESULT]
                        put_Position: _Callable[[Windows.Foundation.IReference[_struct.Windows.Foundation.Point]],
                                                _type.HRESULT]
                        get_ExclusionRect: _Callable[[_Pointer[Windows.Foundation.IReference[_struct.Windows.Foundation.Rect]]],
                                                     _type.HRESULT]
                        put_ExclusionRect: _Callable[[Windows.Foundation.IReference[_struct.Windows.Foundation.Rect]],
                                                     _type.HRESULT]
                        get_ShowMode: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode]],
                                                _type.HRESULT]
                        put_ShowMode: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutShowMode],
                                                _type.HRESULT]
                        get_Placement: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode]],
                                                 _type.HRESULT]
                        put_Placement: _Callable[[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],
                                                 _type.HRESULT]

                    class IFlyoutShowOptionsFactory(IInspectable):
                        CreateInstance: _Callable[[IInspectable,
                                                   _Pointer[IInspectable],
                                                   _Pointer[Windows.UI.Xaml.Controls.Primitives.IFlyoutShowOptions]],
                                                  _type.HRESULT]

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

            class Data:
                class _ICurrentChangingEventHandler:
                    Invoke: _Callable

                class ICurrentChangingEventHandler(_ICurrentChangingEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class ICurrentChangingEventHandler_impl(_ICurrentChangingEventHandler, IUnknown_impl):
                    pass

                class _IPropertyChangedEventHandler:
                    Invoke: _Callable

                class IPropertyChangedEventHandler(_IPropertyChangedEventHandler, IUnknown):
                    pass

                # noinspection PyPep8Naming
                class IPropertyChangedEventHandler_impl(_IPropertyChangedEventHandler, IUnknown_impl):
                    pass

                class IBinding(IInspectable):
                    get_Path: _Callable
                    put_Path: _Callable
                    get_Mode: _Callable
                    put_Mode: _Callable
                    get_Source: _Callable
                    put_Source: _Callable
                    get_RelativeSource: _Callable
                    put_RelativeSource: _Callable
                    get_ElementName: _Callable
                    put_ElementName: _Callable
                    get_Converter: _Callable
                    put_Converter: _Callable
                    get_ConverterParameter: _Callable
                    put_ConverterParameter: _Callable
                    get_ConverterLanguage: _Callable
                    put_ConverterLanguage: _Callable

                class IBinding2(IInspectable):
                    get_FallbackValue: _Callable
                    put_FallbackValue: _Callable
                    get_TargetNullValue: _Callable
                    put_TargetNullValue: _Callable
                    get_UpdateSourceTrigger: _Callable
                    put_UpdateSourceTrigger: _Callable

                class IBindingBase(IInspectable):
                    pass

                class IBindingBaseFactory(IInspectable):
                    CreateInstance: _Callable

                class IBindingExpression(IInspectable):
                    get_DataItem: _Callable
                    get_ParentBinding: _Callable
                    UpdateSource: _Callable

                class IBindingExpressionBase(IInspectable):
                    pass

                class IBindingExpressionBaseFactory(IInspectable):
                    pass

                class IBindingExpressionFactory(IInspectable):
                    pass

                class IBindingFactory(IInspectable):
                    CreateInstance: _Callable

                class IBindingOperations(IInspectable):
                    pass

                class IBindingOperationsStatics(IInspectable):
                    SetBinding: _Callable

                class ICollectionView(IInspectable):
                    get_CurrentItem: _Callable
                    get_CurrentPosition: _Callable
                    get_IsCurrentAfterLast: _Callable
                    get_IsCurrentBeforeFirst: _Callable
                    get_CollectionGroups: _Callable
                    get_HasMoreItems: _Callable
                    add_CurrentChanged: _Callable
                    remove_CurrentChanged: _Callable
                    add_CurrentChanging: _Callable
                    remove_CurrentChanging: _Callable
                    MoveCurrentTo: _Callable
                    MoveCurrentToPosition: _Callable
                    MoveCurrentToFirst: _Callable
                    MoveCurrentToLast: _Callable
                    MoveCurrentToNext: _Callable
                    MoveCurrentToPrevious: _Callable
                    LoadMoreItemsAsync: _Callable

                class ICollectionViewFactory(IInspectable):
                    CreateView: _Callable

                class ICollectionViewGroup(IInspectable):
                    get_Group: _Callable
                    get_GroupItems: _Callable

                class ICollectionViewSource(IInspectable):
                    get_Source: _Callable
                    put_Source: _Callable
                    get_View: _Callable
                    get_IsSourceGrouped: _Callable
                    put_IsSourceGrouped: _Callable
                    get_ItemsPath: _Callable
                    put_ItemsPath: _Callable

                class ICollectionViewSourceStatics(IInspectable):
                    get_SourceProperty: _Callable
                    get_ViewProperty: _Callable
                    get_IsSourceGroupedProperty: _Callable
                    get_ItemsPathProperty: _Callable

                class ICurrentChangingEventArgs(IInspectable):
                    get_Cancel: _Callable
                    put_Cancel: _Callable
                    get_IsCancelable: _Callable

                class ICurrentChangingEventArgsFactory(IInspectable):
                    CreateInstance: _Callable
                    CreateWithCancelableParameter: _Callable

                class ICustomProperty(IInspectable):
                    get_Type: _Callable
                    get_Name: _Callable
                    GetValue: _Callable
                    SetValue: _Callable
                    GetIndexedValue: _Callable
                    SetIndexedValue: _Callable
                    get_CanWrite: _Callable
                    get_CanRead: _Callable

                class ICustomPropertyProvider(IInspectable):
                    GetCustomProperty: _Callable
                    GetIndexedProperty: _Callable
                    GetStringRepresentation: _Callable
                    get_Type: _Callable

                class IItemIndexRange(IInspectable):
                    get_FirstIndex: _Callable
                    get_Length: _Callable
                    get_LastIndex: _Callable

                class IItemIndexRangeFactory(IInspectable):
                    CreateInstance: _Callable

                class IItemsRangeInfo(IInspectable):
                    RangesChanged: _Callable

                class INotifyPropertyChanged(IInspectable):
                    add_PropertyChanged: _Callable
                    remove_PropertyChanged: _Callable

                class IPropertyChangedEventArgs(IInspectable):
                    get_PropertyName: _Callable

                class IPropertyChangedEventArgsFactory(IInspectable):
                    CreateInstance: _Callable

                class IRelativeSource(IInspectable):
                    get_Mode: _Callable
                    put_Mode: _Callable

                class IRelativeSourceFactory(IInspectable):
                    CreateInstance: _Callable

                class ISelectionInfo(IInspectable):
                    SelectRange: _Callable
                    DeselectRange: _Callable
                    IsSelected: _Callable
                    GetSelectedRanges: _Callable

                class ISupportIncrementalLoading(IInspectable):
                    LoadMoreItemsAsync: _Callable
                    get_HasMoreItems: _Callable

                class IValueConverter(IInspectable):
                    Convert: _Callable
                    ConvertBack: _Callable

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
                    add_TakeFocusRequested: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceTakeFocusRequestedEventArgs],
                                                       _Pointer[_struct.EventRegistrationToken]],
                                                      _type.HRESULT]
                    remove_TakeFocusRequested: _Callable[[_struct.EventRegistrationToken],
                                                         _type.HRESULT]
                    add_GotFocus: _Callable[[Windows.Foundation.ITypedEventHandler_impl[Windows.UI.Xaml.Hosting.IDesktopWindowXamlSource, Windows.UI.Xaml.Hosting.IDesktopWindowXamlSourceGotFocusEventArgs],
                                             _Pointer[_struct.EventRegistrationToken]],
                                            _type.HRESULT]
                    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],
                                               _type.HRESULT]
                    NavigateFocus: _Callable[[Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationRequest,
                                              _Pointer[Windows.UI.Xaml.Hosting.IXamlSourceFocusNavigationResult]],
                                             _type.HRESULT]

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
                    get_RootElement: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                               _type.HRESULT]
                    put_RootElement: _Callable[[_Pointer[Windows.UI.Xaml.IUIElement]],
                                               _type.HRESULT]
                    get_ThemeKey: _Callable[[_Pointer[_type.HSTRING]],
                                            _type.HRESULT]
                    put_ThemeKey: _Callable[[_type.HSTRING],
                                            _type.HRESULT]
                    get_ThemeResourcesXaml: _Callable[[_Pointer[_type.HSTRING]],
                                                      _type.HRESULT]
                    put_ThemeResourcesXaml: _Callable[[_type.HSTRING],
                                                      _type.HRESULT]
                    SetSize: _Callable[[_type.INT32,
                                        _type.INT32],
                                       _type.HSTRING]
                    Render: _Callable[[],
                                      _type.HRESULT]
                    Present: _Callable[[],
                                       _type.HRESULT]

                class IXamlUIPresenterHost(IInspectable):
                    ResolveFileResource: _Callable[[_type.HSTRING,
                                                    _Pointer[_type.HSTRING]],
                                                   _type.HRESULT]

                class IXamlUIPresenterHost2(IInspectable):
                    GetGenericXamlFilePath: _Callable[[_Pointer[_type.HSTRING]],
                                                      _type.HRESULT]

                class IXamlUIPresenterHost3(IInspectable):
                    ResolveDictionaryResource: _Callable[[Windows.UI.Xaml.IResourceDictionary,
                                                          IInspectable,
                                                          IInspectable,
                                                          _Pointer[IInspectable]],
                                                         _type.HRESULT]

                class IXamlUIPresenterStatics(IInspectable):
                    get_CompleteTimelinesAutomatically: _Callable[[_Pointer[_type.boolean]],
                                                                  _type.HRESULT]
                    put_CompleteTimelinesAutomatically: _Callable[[_type.boolean],
                                                                  _type.HRESULT]
                    SetHost: _Callable[[Windows.UI.Xaml.Hosting.IXamlUIPresenterHost],
                                       _type.HRESULT]
                    NotifyWindowSizeChanged: _Callable[[],
                                                       _type.HRESULT]

                class IXamlUIPresenterStatics2(IInspectable):
                    GetFlyoutPlacementTargetInfo: _Callable[[Windows.UI.Xaml.IFrameworkElement,
                                                             _enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode,
                                                             _Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],
                                                             _Pointer[_type.boolean],
                                                             _Pointer[_struct.Windows.Foundation.Rect]],
                                                            _type.HRESULT]
                    GetFlyoutPlacement: _Callable[[_struct.Windows.Foundation.Rect,
                                                   _struct.Windows.Foundation.Size,
                                                   _struct.Windows.Foundation.Size,
                                                   _struct.Windows.Foundation.Rect,
                                                   _enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode,
                                                   _type.boolean,
                                                   _Pointer[_enum.Windows.UI.Xaml.Controls.Primitives.FlyoutPlacementMode],
                                                   _Pointer[_struct.Windows.Foundation.Rect]],
                                                  _type.HRESULT]

            class Markup:
                class IComponentConnector(IInspectable):
                    Connect: _Callable[[_type.INT32,
                                        IInspectable],
                                       _type.HRESULT]

                class IComponentConnector2(IInspectable):
                    GetBindingConnector: _Callable[[_type.INT32,
                                                    IInspectable,
                                                    _Pointer[Windows.UI.Xaml.Markup.IComponentConnector]],
                                                   _type.HRESULT]

                class IDataTemplateComponent(IInspectable):
                    Recycle: _Callable[[],
                                       _type.HRESULT]
                    ProcessBindings: _Callable[[IInspectable,
                                                _type.INT32,
                                                _type.INT32,
                                                _Pointer[_type.INT32]],
                                               _type.HRESULT]

                class IMarkupExtension(IInspectable):
                    pass

                class IMarkupExtensionFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Markup.IMarkupExtension]],
                                              _type.HRESULT]

                class IMarkupExtensionOverrides(IInspectable):
                    ProvideValue: _Callable[[_Pointer[IInspectable]],
                                            _type.HRESULT]

                class IXamlBinaryWriter(IInspectable):
                    pass

                class IXamlBinaryWriterStatics(IInspectable):
                    Write: _Callable[[Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream],
                                      Windows.Foundation.Collections.IVector[Windows.Storage.Streams.IRandomAccessStream],
                                      Windows.UI.Xaml.Markup.IXamlMetadataProvider,
                                      _Pointer[_struct.Windows.UI.Xaml.Markup.XamlBinaryWriterErrorInformation]],
                                     _type.HRESULT]

                class IXamlBindScopeDiagnostics(IInspectable):
                    Disable: _Callable[[_type.INT32,
                                        _type.INT32],
                                       _type.HRESULT]

                class IXamlBindingHelper(IInspectable):
                    pass

                class IXamlBindingHelperStatics(IInspectable):
                    get_DataTemplateComponentProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]
                    GetDataTemplateComponent: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                                         _Pointer[Windows.UI.Xaml.Markup.IDataTemplateComponent]],
                                                        _type.HRESULT]
                    SetDataTemplateComponent: _Callable[[Windows.UI.Xaml.IDependencyObject,
                                                         Windows.UI.Xaml.Markup.IDataTemplateComponent],
                                                        _type.HRESULT]
                    SuspendRendering: _Callable[[Windows.UI.Xaml.IUIElement],
                                                _type.HRESULT]
                    ResumeRendering: _Callable[[Windows.UI.Xaml.IUIElement],
                                               _type.HRESULT]
                    ConvertValue: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,
                                             IInspectable,
                                             _Pointer[IInspectable]],
                                            _type.HRESULT]
                    SetPropertyFromString: _Callable[[IInspectable,
                                                      Windows.UI.Xaml.IDependencyProperty,
                                                      _type.HSTRING],
                                                     _type.HRESULT]
                    SetPropertyFromBoolean: _Callable[[IInspectable,
                                                       Windows.UI.Xaml.IDependencyProperty,
                                                       _type.boolean],
                                                      _type.HRESULT]
                    SetPropertyFromChar16: _Callable[[IInspectable,
                                                      Windows.UI.Xaml.IDependencyProperty,
                                                      _type.WCHAR],
                                                     _type.HRESULT]
                    SetPropertyFromDateTime: _Callable[[IInspectable,
                                                        Windows.UI.Xaml.IDependencyProperty,
                                                        _struct.Windows.Foundation.DateTime],
                                                       _type.HRESULT]
                    SetPropertyFromDouble: _Callable[[IInspectable,
                                                      Windows.UI.Xaml.IDependencyProperty,
                                                      _type.DOUBLE],
                                                     _type.HRESULT]
                    SetPropertyFromInt32: _Callable[[IInspectable,
                                                     Windows.UI.Xaml.IDependencyProperty,
                                                     _type.INT32],
                                                    _type.HRESULT]
                    SetPropertyFromUInt32: _Callable[[IInspectable,
                                                      Windows.UI.Xaml.IDependencyProperty,
                                                      _type.UINT32],
                                                     _type.HRESULT]
                    SetPropertyFromInt64: _Callable[[IInspectable,
                                                     Windows.UI.Xaml.IDependencyProperty,
                                                     _type.INT64],
                                                    _type.HRESULT]
                    SetPropertyFromUInt64: _Callable[[IInspectable,
                                                      Windows.UI.Xaml.IDependencyProperty,
                                                      _type.UINT64],
                                                     _type.HRESULT]
                    SetPropertyFromSingle: _Callable[[IInspectable,
                                                      Windows.UI.Xaml.IDependencyProperty,
                                                      _type.FLOAT],
                                                     _type.HRESULT]
                    SetPropertyFromPoint: _Callable[[IInspectable,
                                                     Windows.UI.Xaml.IDependencyProperty,
                                                     _struct.Windows.Foundation.Point],
                                                    _type.HRESULT]
                    SetPropertyFromRect: _Callable[[IInspectable,
                                                    Windows.UI.Xaml.IDependencyProperty,
                                                    _struct.Windows.Foundation.Rect],
                                                   _type.HRESULT]
                    SetPropertyFromSize: _Callable[[IInspectable,
                                                    Windows.UI.Xaml.IDependencyProperty,
                                                    _struct.Windows.Foundation.Size],
                                                   _type.HRESULT]
                    SetPropertyFromTimeSpan: _Callable[[IInspectable,
                                                        Windows.UI.Xaml.IDependencyProperty,
                                                        _struct.Windows.Foundation.TimeSpan],
                                                       _type.HRESULT]
                    SetPropertyFromByte: _Callable[[IInspectable,
                                                    Windows.UI.Xaml.IDependencyProperty,
                                                    _type.BYTE],
                                                   _type.HRESULT]
                    SetPropertyFromUri: _Callable[[IInspectable,
                                                   Windows.UI.Xaml.IDependencyProperty,
                                                   Windows.Foundation.IUriRuntimeClass],
                                                  _type.HRESULT]
                    SetPropertyFromObject: _Callable[[IInspectable,
                                                      Windows.UI.Xaml.IDependencyProperty,
                                                      IInspectable],
                                                     _type.HRESULT]

                class IXamlMarkupHelper(IInspectable):
                    pass

                class IXamlMarkupHelperStatics(IInspectable):
                    UnloadObject: _Callable[[Windows.UI.Xaml.IDependencyObject],
                                            _type.HRESULT]

                class IXamlMember(IInspectable):
                    get_IsAttachable: _Callable[[_Pointer[_type.boolean]],
                                                _type.HRESULT]
                    get_IsDependencyProperty: _Callable[[_Pointer[_type.boolean]],
                                                        _type.HRESULT]
                    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],
                                              _type.HRESULT]
                    get_Name: _Callable[[_Pointer[_type.HSTRING]],
                                        _type.HRESULT]
                    get_TargetType: _Callable[[_Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                              _type.HRESULT]
                    get_Type: _Callable[[_Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                        _type.HRESULT]
                    GetValue: _Callable[[IInspectable,
                                         _Pointer[IInspectable]],
                                        _type.HRESULT]
                    SetValue: _Callable[[IInspectable,
                                         IInspectable],
                                        _type.HRESULT]

                class IXamlMetadataProvider(IInspectable):
                    GetXamlType: _Callable[[_struct.Windows.UI.Xaml.Interop.TypeName,
                                            _Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                           _type.HRESULT]
                    GetXamlTypeByFullName: _Callable[[_type.HSTRING,
                                                      _Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                                     _type.HRESULT]
                    GetXmlnsDefinitions: _Callable

                class IXamlReader(IInspectable):
                    pass

                class IXamlReaderStatics(IInspectable):
                    Load: _Callable[[_type.HSTRING,
                                     _Pointer[IInspectable]],
                                    _type.HRESULT]
                    LoadWithInitialTemplateValidation: _Callable[[_type.HSTRING,
                                                                  _Pointer[IInspectable]],
                                                                 _type.HRESULT]

                class IXamlType(IInspectable):
                    get_BaseType: _Callable[[_Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                            _type.HRESULT]
                    get_ContentProperty: _Callable[[_Pointer[Windows.UI.Xaml.Markup.IXamlMember]],
                                                   _type.HRESULT]
                    get_FullName: _Callable[[_Pointer[_type.HSTRING]],
                                            _type.HRESULT]
                    get_IsArray: _Callable[[_Pointer[_type.boolean]],
                                           _type.HRESULT]
                    get_IsCollection: _Callable[[_Pointer[_type.boolean]],
                                                _type.HRESULT]
                    get_IsConstructible: _Callable[[_Pointer[_type.boolean]],
                                                   _type.HRESULT]
                    get_IsDictionary: _Callable[[_Pointer[_type.boolean]],
                                                _type.HRESULT]
                    get_IsMarkupExtension: _Callable[[_Pointer[_type.boolean]],
                                                     _type.HRESULT]
                    get_IsBindable: _Callable[[_Pointer[_type.boolean]],
                                              _type.HRESULT]
                    get_ItemType: _Callable[[_Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                            _type.HRESULT]
                    get_KeyType: _Callable[[_Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                           _type.HRESULT]
                    get_UnderlyingType: _Callable[[_Pointer[_struct.Windows.UI.Xaml.Interop.TypeName]],
                                                  _type.HRESULT]
                    ActivateInstance: _Callable[[_Pointer[IInspectable]],
                                                _type.HRESULT]
                    CreateFromString: _Callable[[_type.HSTRING,
                                                 _Pointer[IInspectable]],
                                                _type.HRESULT]
                    GetMember: _Callable[[_type.HSTRING,
                                          _Pointer[Windows.UI.Xaml.Markup.IXamlMember]],
                                         _type.HRESULT]
                    AddToVector: _Callable[[IInspectable,
                                            IInspectable],
                                           _type.HRESULT]
                    AddToMap: _Callable[[IInspectable,
                                         IInspectable,
                                         IInspectable],
                                        _type.HRESULT]
                    RunInitializer: _Callable[[],
                                              _type.HRESULT]

                class IXamlType2(IInspectable):
                    get_BoxedType: _Callable[[_Pointer[Windows.UI.Xaml.Markup.IXamlType]],
                                             _type.HRESULT]

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
                    get_BackgroundSource: _Callable[[_Pointer[_enum.Windows.UI.Xaml.Media.AcrylicBackgroundSource]],
                                                    _type.HRESULT]
                    put_BackgroundSource: _Callable[[_enum.Windows.UI.Xaml.Media.AcrylicBackgroundSource],
                                                    _type.HRESULT]
                    get_TintColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                             _type.HRESULT]
                    put_TintColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],
                                             _type.HRESULT]
                    get_TintOpacity: _Callable[[_Pointer[_type.DOUBLE]],
                                               _type.HRESULT]
                    put_TintOpacity: _Callable[[_type.DOUBLE],
                                               _type.HRESULT]
                    get_TintTransitionDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],
                                                          _type.HRESULT]
                    put_TintTransitionDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],
                                                          _type.HRESULT]
                    get_AlwaysUseFallback: _Callable[[_Pointer[_type.boolean]],
                                                     _type.HRESULT]
                    put_AlwaysUseFallback: _Callable[[_Pointer[_type.boolean]],
                                                     _type.HRESULT]

                class IAcrylicBrush2(IInspectable):
                    get_TintLuminosityOpacity: _Callable[[_Pointer[Windows.Foundation.IReference[_type.DOUBLE]]],
                                                         _type.HRESULT]
                    put_TintLuminosityOpacity: _Callable[[Windows.Foundation.IReference[_type.DOUBLE]],
                                                         _type.HRESULT]

                class IAcrylicBrushFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Media.IAcrylicBrush]],
                                              _type.HRESULT]

                class IAcrylicBrushStatics(IInspectable):
                    get_BackgroundSourceProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_TintColorProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                     _type.HRESULT]
                    get_TintOpacityProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                       _type.HRESULT]
                    get_TintTransitionDurationProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                  _type.HRESULT]
                    get_AlwaysUseFallbackProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                             _type.HRESULT]

                class IAcrylicBrushStatics2(IInspectable):
                    get_TintLuminosityOpacityProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                                 _type.HRESULT]

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

            class Shapes:
                class IEllipse(IInspectable):
                    pass

                class ILine(IInspectable):
                    get_X1: _Callable
                    put_X1: _Callable
                    get_Y1: _Callable
                    put_Y1: _Callable
                    get_X2: _Callable
                    put_X2: _Callable
                    get_Y2: _Callable
                    put_Y2: _Callable

                class ILineStatics(IInspectable):
                    get_X1Property: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                              _type.HRESULT]
                    get_Y1Property: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                              _type.HRESULT]
                    get_X2Property: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                              _type.HRESULT]
                    get_Y2Property: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                              _type.HRESULT]

                class IPath(IInspectable):
                    get_Data: _Callable
                    put_Data: _Callable

                class IPathFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Shapes.IPath]],
                                              _type.HRESULT]

                class IPathStatics(IInspectable):
                    get_DataProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]

                class IPolygon(IInspectable):
                    get_FillRule: _Callable
                    put_FillRule: _Callable
                    get_Points: _Callable
                    put_Points: _Callable

                class IPolygonStatics(IInspectable):
                    get_FillRuleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                    get_PointsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                  _type.HRESULT]

                class IPolyline(IInspectable):
                    get_FillRule: _Callable
                    put_FillRule: _Callable
                    get_Points: _Callable
                    put_Points: _Callable

                class IPolylineStatics(IInspectable):
                    get_FillRuleProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                    _type.HRESULT]
                    get_PointsProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                  _type.HRESULT]

                class IRectangle(IInspectable):
                    get_RadiusX: _Callable
                    put_RadiusX: _Callable
                    get_RadiusY: _Callable
                    put_RadiusY: _Callable

                class IRectangleStatics(IInspectable):
                    get_RadiusXProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
                    get_RadiusYProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]

                class IShape(IInspectable):
                    get_Fill: _Callable
                    put_Fill: _Callable
                    get_Stroke: _Callable
                    put_Stroke: _Callable
                    get_StrokeMiterLimit: _Callable
                    put_StrokeMiterLimit: _Callable
                    get_StrokeThickness: _Callable
                    put_StrokeThickness: _Callable
                    get_StrokeStartLineCap: _Callable
                    put_StrokeStartLineCap: _Callable
                    get_StrokeEndLineCap: _Callable
                    put_StrokeEndLineCap: _Callable
                    get_StrokeLineJoin: _Callable
                    put_StrokeLineJoin: _Callable
                    get_StrokeDashOffset: _Callable
                    put_StrokeDashOffset: _Callable
                    get_StrokeDashCap: _Callable
                    put_StrokeDashCap: _Callable
                    get_StrokeDashArray: _Callable
                    put_StrokeDashArray: _Callable
                    get_Stretch: _Callable
                    put_Stretch: _Callable
                    get_GeometryTransform: _Callable

                class IShape2(IInspectable):
                    GetAlphaMask: _Callable

                class IShapeFactory(IInspectable):
                    CreateInstance: _Callable[[IInspectable,
                                               _Pointer[IInspectable],
                                               _Pointer[Windows.UI.Xaml.Shapes.IShape]],
                                              _type.HRESULT]

                class IShapeStatics(IInspectable):
                    get_FillProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                _type.HRESULT]
                    get_StrokeProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                  _type.HRESULT]
                    get_StrokeMiterLimitProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_StrokeThicknessProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_StrokeStartLineCapProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                              _type.HRESULT]
                    get_StrokeEndLineCapProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_StrokeLineJoinProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                          _type.HRESULT]
                    get_StrokeDashOffsetProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                            _type.HRESULT]
                    get_StrokeDashCapProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                         _type.HRESULT]
                    get_StrokeDashArrayProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                           _type.HRESULT]
                    get_StretchProperty: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],
                                                   _type.HRESULT]
