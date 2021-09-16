from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _const
from . import _struct
from . import _type
from .__head__ import _Globals
from .__head__ import _Pointer
from .__head__ import _get_doc
from .__head__ import _resolve_type

_ASSIGNED = ('__CLSID__', *(assigned for assigned in _functools.WRAPPER_ASSIGNMENTS if assigned != '__doc__'))

'''class _ComBase(_ctypes.c_void_p):
    __IID__: str = _const.IID_IUnknown
    _funcs = None

    def __init_subclass__(cls):  # disable init_subclass
        iid = set()
        fields = []
        cls._funcs = []
        for base in cls._get_base(cls):
            try:
                iid.add(base.__IID__)
            except TypeError:
                iid.union(base.__IID__)
            for key, value in vars(base).items():
                if not key.startswith('_'):
                    types = list(_typing.get_type_hints(value).values())
                    # noinspection PyTypeHints
                    type_ = _ctypes.WINFUNCTYPE(*_resolve_type(_Callable[types, types.pop()]))
                    fields.append((key, type_))
                    cls._funcs.append(type_(value))
        # noinspection PyTypeChecker
        cls.__IID__ = iid
        cls._struct = type(cls.__name__, (_ctypes.Structure,), {'_fields_': fields})
        # print(fields)

    def __init__(self):
        print(self)
        self.s = self._struct(*self._funcs)
        super().__init__(_ctypes.addressof(self.s))

    @staticmethod
    def _get_base(subclass) -> _Generator[type[_ComBase], None, None]:
        bases = subclass.mro()
        for i in range(bases.index(_ComBase), -1, -1):
            yield bases[i]

    # noinspection PyPep8Naming
    def QueryInterface(self: _ComBase, lpMyObj: _Pointer[_ComBase], riid: _Pointer[_struct.IID],
                       lppvObj: _Pointer[_type.LPVOID]) -> _type.HRESULT:
        lppvObj.contents.value = None
        iid = _type.LPOLESTR()
        _func.StringFromIID(riid, _byref(iid))
        if iid.value in self.__IID__:
            lppvObj.contents.value = lpMyObj
            return _const.NOERROR
        return _const.E_NOINTERFACE

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def AddRef(self: _ComBase) -> _type.ULONG:
        return 1

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def Release(self: _ComBase) -> _type.ULONG:
        return 0'''


class IUnknown(_ctypes.c_void_p):
    __CLSID__ = ''
    QueryInterface: _Callable[[_Pointer[_struct.IID], _type.c_void_p], _type.HRESULT]
    AddRef: _Callable[[], _type.ULONG]
    Release: _Callable[[], _type.ULONG]


class IShellItem(IUnknown):
    BindToHandler: _Callable[[_Pointer[_type.IBindCtx], _Pointer[_struct.GUID],
                              _Pointer[_struct.IID], _type.c_void_p], _type.HRESULT]
    GetParent: _Callable[[_Pointer[_type.IShellItem]], _type.HRESULT]
    GetDisplayName: _Callable[[_type.SIGDN, _Pointer[_type.LPWSTR]], _type.HRESULT]
    GetAttributes: _Callable[[_type.SFGAOF, _Pointer[_type.SFGAOF]], _type.HRESULT]
    Compare: _Callable[[_Pointer[_type.IShellItem], _type.SICHINTF, _Pointer[_type.c_int]],
                       _type.HRESULT]


class IShellItemArray(IUnknown):
    BindToHandler: _Callable
    GetPropertyStore: _Callable
    GetPropertyDescriptionList: _Callable
    GetAttributes: _Callable
    GetCount: _Callable[[_Pointer[_type.DWORD]], _type.HRESULT]
    GetItemAt: _Callable
    EnumItems: _Callable


class IActiveDesktop(IUnknown):
    __CLSID__ = _const.CLSID_ActiveDesktop
    ApplyChanges: _Callable[[_type.DWORD], _type.HRESULT]
    GetWallpaper: _Callable[[_type.PWSTR, _type.UINT, _type.DWORD], _type.HRESULT]
    SetWallpaper: _Callable[[_type.PCWSTR, _type.DWORD], _type.HRESULT]
    GetWallpaperOptions: _Callable[[_Pointer[_struct.WALLPAPEROPT], _type.DWORD], _type.HRESULT]
    SetWallpaperOptions: _Callable[[_Pointer[_struct.WALLPAPEROPT], _type.DWORD], _type.HRESULT]
    GetPattern: _Callable[[_type.PWSTR, _type.UINT, _type.DWORD], _type.HRESULT]
    SetPattern: _Callable[[_type.PCWSTR, _type.DWORD], _type.HRESULT]
    GetDesktopItemOptions: _Callable
    SetDesktopItemOptions: _Callable
    AddDesktopItem: _Callable
    AddDesktopItemWithUI: _Callable
    ModifyDesktopItem: _Callable
    RemoveDesktopItem: _Callable
    GetDesktopItemCount: _Callable[[_Pointer[_type.c_int], _type.DWORD], _type.HRESULT]
    GetDesktopItem: _Callable
    GetDesktopItemByID: _Callable
    GenerateDesktopItemHtml: _Callable
    AddUrl: _Callable
    GetDesktopItemBySource: _Callable


class IDesktopWallpaper(IUnknown):
    __CLSID__ = _const.CLSID_DesktopWallpaper
    SetWallpaper: _Callable[[_type.LPCWSTR, _type.LPCWSTR], _type.HRESULT]
    GetWallpaper: _Callable[[_type.LPCWSTR, _Pointer[_type.LPWSTR]], _type.HRESULT]
    GetMonitorDevicePathAt: _Callable[[_type.UINT, _Pointer[_type.LPWSTR]], _type.HRESULT]
    GetMonitorDevicePathCount: _Callable[[_Pointer[_type.UINT]], _type.HRESULT]
    GetMonitorRECT: _Callable[[_type.LPCWSTR, _Pointer[_struct.RECT]], _type.HRESULT]
    SetBackgroundColor: _Callable[[_type.COLORREF], _type.HRESULT]
    GetBackgroundColor: _Callable[[_Pointer[_type.COLORREF]], _type.HRESULT]
    SetPosition: _Callable[[_type.DESKTOP_WALLPAPER_POSITION], _type.HRESULT]
    GetPosition: _Callable[[_Pointer[_type.DESKTOP_WALLPAPER_POSITION]], _type.HRESULT]
    SetSlideshow: _Callable[[_type.IShellItemArray], _type.HRESULT]
    GetSlideshow: _Callable
    SetSlideshowOptions: _Callable[[_type.DESKTOP_SLIDESHOW_OPTIONS, _type.UINT], _type.HRESULT]
    GetSlideshowOptions: _Callable[[_type.DESKTOP_SLIDESHOW_OPTIONS, _Pointer[_type.UINT]], _type.HRESULT]
    AdvanceSlideshow: _Callable[[_type.LPCWSTR, _type.DESKTOP_SLIDESHOW_DIRECTION], _type.HRESULT]
    GetStatus: _Callable[[_Pointer[_type.DESKTOP_SLIDESHOW_STATE]], _type.HRESULT]
    Enable: _Callable[[_type.BOOL], _type.HRESULT]


class IModalWindow(IUnknown):
    __CLSID__ = _const.CLSID_FileOpenDialog
    Show: _Callable[[_type.HWND], _type.HRESULT]


class IFileDialog(IModalWindow):
    SetFileTypes: _Callable
    SetFileTypeIndex: _Callable[[_type.UINT], _type.HRESULT]
    GetFileTypeIndex: _Callable[[_type.UINT], _type.HRESULT]
    Advise: _Callable
    Unadvise: _Callable
    SetOptions: _Callable
    GetOptions: _Callable
    SetDefaultFolder: _Callable
    SetFolder: _Callable
    GetFolder: _Callable
    GetCurrentSelection: _Callable
    SetFileName: _Callable[[_type.LPCWSTR], _type.HRESULT]
    GetFileName: _Callable[[_type.LPWSTR], _type.HRESULT]
    SetTitle: _Callable[[_type.LPCWSTR], _type.HRESULT]
    SetOkButtonLabel: _Callable[[_type.LPCWSTR], _type.HRESULT]
    SetFileNameLabel: _Callable[[_type.LPCWSTR], _type.HRESULT]
    GetResult: _Callable
    AddPlace: _Callable
    SetDefaultExtension: _Callable[[_type.LPCWSTR], _type.HRESULT]
    Close: _Callable[[_type.HRESULT], _type.HRESULT]
    SetClientGuid: _Callable[[_Pointer[_struct.GUID]], _type.HRESULT]
    ClearClientData: _Callable[[], _type.HRESULT]
    SetFilter: _Callable


class IFileOpenDialog(IFileDialog):
    GetResults: _Callable
    GetSelectedItems: _Callable


class IInspectable(IUnknown):
    GetIids: _Callable
    GetRuntimeClassName: _Callable
    GetTrustLevel: _Callable


class IQueryContinue(IUnknown):
    QueryContinue: _Callable[[], _type.HRESULT]


class IUserNotification(IUnknown):
    __CLSID__ = _const.CLSID_UserNotification
    SetBalloonInfo: _Callable[[_type.LPCWSTR, _type.LPCWSTR, _type.DWORD], _type.HRESULT]
    SetBalloonRetry: _Callable[[_type.DWORD, _type.DWORD, _type.UINT], _type.HRESULT]
    SetIconInfo: _Callable[[_type.HICON, _type.LPCWSTR], _type.HRESULT]
    Show: _Callable[[_Optional[_type.IQueryContinue], _type.DWORD], _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR], _type.HRESULT]


class IUserNotificationCallback(IUnknown):
    __CLSID__ = _const.CLSID_UserNotification
    OnBalloonUserClick: _Callable[[_struct.POINT], _type.HRESULT]
    OnLeftClick: _Callable[[_struct.POINT], _type.HRESULT]
    OnContextMenu: _Callable[[_struct.POINT], _type.HRESULT]


class IUserNotification2(IUnknown):
    __CLSID__ = _const.CLSID_UserNotification
    SetBalloonInfo: _Callable[[_type.LPCWSTR, _type.LPCWSTR, _type.DWORD], _type.HRESULT]
    SetBalloonRetry: _Callable[[_type.DWORD, _type.DWORD, _type.UINT], _type.HRESULT]
    SetIconInfo: _Callable[[_type.HICON, _type.LPCWSTR], _type.HRESULT]
    Show: _Callable[[_Optional[_type.IQueryContinue], _type.DWORD,
                     _Optional[_type.IUserNotificationCallback]], _type.HRESULT]
    PlaySound: _Callable[[_type.LPCWSTR], _type.HRESULT]


def _method_type(types: _Callable) -> list:
    types = _resolve_type(types)
    types.insert(1, _ctypes.c_void_p)
    return types


def _init(name: str) -> type[_ctypes.c_void_p]:
    _globals.has_item(name)

    class Wrapper(_ctypes.c_void_p):
        _struct: _ctypes.Structure = type(name, (_ctypes.Structure,), {'_fields_': tuple((name_, _ctypes.WINFUNCTYPE(
            *_method_type(types))) for name_, types in _typing.get_type_hints(_globals.vars_[name], _globals).items())})
        # noinspection PyProtectedMember
        __doc__ = '\n'.join(_get_doc(name_, types._restype_, types._argtypes_) for name_, types in _struct._fields_)

        def __getattr__(self, name_: str):
            if not name_.startswith('_') and name_ in dir(self._struct):
                funcs = self._struct.from_address(_ctypes.c_void_p.from_address(self.value).value)
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
