import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable

from . import _const
from . import _header
from . import _struct
from . import _type


class IUnknown(_ctypes.c_void_p):
    __CLSID__ = ''
    QueryInterface: _Callable[[_header.Pointer[_struct.IID], _type.c_void_p], _type.HRESULT]
    AddRef: _Callable[[], _type.ULONG]
    Release: _Callable[[], _type.ULONG]


class IShellItem(IUnknown):
    BindToHandler: _Callable[[_header.Pointer[_type.IBindCtx], _header.Pointer[_struct.GUID],
                              _header.Pointer[_struct.IID], _type.c_void_p], _type.HRESULT]
    GetParent: _Callable[[_header.Pointer[_type.IShellItem]], _type.HRESULT]
    GetDisplayName: _Callable[[_type.SIGDN, _header.Pointer[_type.LPWSTR]], _type.HRESULT]
    GetAttributes: _Callable[[_type.SFGAOF, _header.Pointer[_type.SFGAOF]], _type.HRESULT]
    Compare: _Callable[[_header.Pointer[_type.IShellItem], _type.SICHINTF, _header.Pointer[_type.c_int]], _type.HRESULT]


class IShellItemArray(IUnknown):
    BindToHandler: _Callable
    GetPropertyStore: _Callable
    GetPropertyDescriptionList: _Callable
    GetAttributes: _Callable
    GetCount: _Callable[[_header.Pointer[_type.DWORD]], _type.HRESULT]
    GetItemAt: _Callable
    EnumItems: _Callable


class IActiveDesktop(IUnknown):
    __CLSID__ = _const.CLSID_ActiveDesktop
    ApplyChanges: _Callable[[_type.DWORD], _type.HRESULT]
    GetWallpaper: _Callable[[_type.PWSTR, _type.UINT, _type.DWORD], _type.HRESULT]
    SetWallpaper: _Callable[[_type.PCWSTR, _type.DWORD], _type.HRESULT]
    GetWallpaperOptions: _Callable[[_header.Pointer[_struct.WALLPAPEROPT], _type.DWORD], _type.HRESULT]
    SetWallpaperOptions: _Callable[[_header.Pointer[_struct.WALLPAPEROPT], _type.DWORD], _type.HRESULT]
    GetPattern: _Callable[[_type.PWSTR, _type.UINT, _type.DWORD], _type.HRESULT]
    SetPattern: _Callable[[_type.PCWSTR, _type.DWORD], _type.HRESULT]
    GetDesktopItemOptions: _Callable
    SetDesktopItemOptions: _Callable
    AddDesktopItem: _Callable
    AddDesktopItemWithUI: _Callable
    ModifyDesktopItem: _Callable
    RemoveDesktopItem: _Callable
    GetDesktopItemCount: _Callable[[_header.Pointer[_type.c_int], _type.DWORD], _type.HRESULT]
    GetDesktopItem: _Callable
    GetDesktopItemByID: _Callable
    GenerateDesktopItemHtml: _Callable
    AddUrl: _Callable
    GetDesktopItemBySource: _Callable


class IDesktopWallpaper(IUnknown):
    __CLSID__ = _const.CLSID_DesktopWallpaper
    SetWallpaper: _Callable[[_type.LPCWSTR, _type.LPCWSTR], _type.HRESULT]
    GetWallpaper: _Callable[[_type.LPCWSTR, _header.Pointer[_type.LPWSTR]], _type.HRESULT]
    GetMonitorDevicePathAt: _Callable[[_type.UINT, _header.Pointer[_type.LPWSTR]], _type.HRESULT]
    GetMonitorDevicePathCount: _Callable[[_header.Pointer[_type.UINT]], _type.HRESULT]
    GetMonitorRECT: _Callable[[_type.LPCWSTR, _header.Pointer[_struct.RECT]], _type.HRESULT]
    SetBackgroundColor: _Callable[[_type.COLORREF], _type.HRESULT]
    GetBackgroundColor: _Callable[[_header.Pointer[_type.COLORREF]], _type.HRESULT]
    SetPosition: _Callable[[_type.DESKTOP_WALLPAPER_POSITION], _type.HRESULT]
    GetPosition: _Callable[[_header.Pointer[_type.DESKTOP_WALLPAPER_POSITION]], _type.HRESULT]
    SetSlideshow: _Callable[[_type.IShellItemArray], _type.HRESULT]
    GetSlideshow: _Callable
    SetSlideshowOptions: _Callable[[_type.DESKTOP_SLIDESHOW_OPTIONS, _type.UINT], _type.HRESULT]
    GetSlideshowOptions: _Callable[[_type.DESKTOP_SLIDESHOW_OPTIONS, _header.Pointer[_type.UINT]], _type.HRESULT]
    AdvanceSlideshow: _Callable[[_type.LPCWSTR, _type.DESKTOP_SLIDESHOW_DIRECTION], _type.HRESULT]
    GetStatus: _Callable[[_header.Pointer[_type.DESKTOP_SLIDESHOW_STATE]], _type.HRESULT]
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
    SetClientGuid: _Callable[[_header.Pointer[_struct.GUID]], _type.HRESULT]
    ClearClientData: _Callable[[], _type.HRESULT]
    SetFilter: _Callable


class IFileOpenDialog(IFileDialog):
    GetResults: _Callable
    GetSelectedItems: _Callable


def _method_type(types: _Callable) -> list:
    types_ = _header.resolve_type(types)
    types_.insert(1, _ctypes.c_void_p)
    return types_


def __getattr__(name: str) -> type[_ctypes.c_void_p]:
    _globals.hasattr(name)

    class Wrapper(_ctypes.c_void_p):
        _fields = {name_: _ctypes.WINFUNCTYPE(*_method_type(
            types)) for name_, types in _typing.get_type_hints(_com[name], _globals).items()}
        # noinspection PyTypeChecker
        _pointer = _ctypes.POINTER(type(name, (_ctypes.Structure,), {'_fields_': tuple(_fields.items())}))

        def __getattr__(self, name_):
            if name_ in self._fields:
                funcs = _ctypes.cast(_ctypes.cast(self, _ctypes.POINTER(
                    _ctypes.c_void_p)).contents.value, self._pointer).contents
                for name__, types in self._fields.items():
                    method = getattr(funcs, name__)
                    method.__name__ = name__
                    # noinspection PyProtectedMember
                    method.__doc__ = _header.get_doc(name__, types._restype_, types._argtypes_)
                    setattr(self, name__, _types.MethodType(method, self))
            return super().__getattribute__(name_)

    _globals[name] = _functools.update_wrapper(Wrapper, _com[name], ('__CLSID__', *_functools.WRAPPER_ASSIGNMENTS), ())
    # noinspection PyProtectedMember
    Wrapper.__doc__ = '\n'.join(_header.get_doc(
        name_, types._restype_, types._argtypes_) for name_, types in Wrapper._fields.items())
    return _globals[name]


_com = _header.init(globals())
_globals = _header.Globals(_com, globals(), __getattr__)
if _header.INIT:
    for _com_ in _com:
        __getattr__(_com_)
