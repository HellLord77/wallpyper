import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing
from typing import Callable as _Callable

from . import _const
from . import _ctype
from . import _header
from . import _struct


# TODO: winrt, help

class IUnknown:
    __CLSID__ = ''
    QueryInterface: _Callable[[_header.Pointer[_struct.IID], _ctype.c_void_p], _ctype.HRESULT]
    AddRef: _Callable[[], _ctype.ULONG]
    Release: _Callable[[], _ctype.ULONG]


class IActiveDesktop(IUnknown):
    __CLSID__ = _const.CLSID_ActiveDesktop
    ApplyChanges: _Callable[[_ctype.DWORD], _ctype.HRESULT]
    GetWallpaper: _Callable[[_ctype.PWSTR, _ctype.UINT, _ctype.DWORD], _ctype.HRESULT]
    SetWallpaper: _Callable[[_ctype.PCWSTR, _ctype.DWORD], _ctype.HRESULT]
    GetWallpaperOptions: _Callable[[_header.Pointer[_struct.WALLPAPEROPT], _ctype.DWORD], _ctype.HRESULT]
    SetWallpaperOptions: _Callable[[_header.Pointer[_struct.WALLPAPEROPT], _ctype.DWORD], _ctype.HRESULT]
    GetPattern: _Callable[[_ctype.PWSTR, _ctype.UINT, _ctype.DWORD], _ctype.HRESULT]
    SetPattern: _Callable[[_ctype.PCWSTR, _ctype.DWORD], _ctype.HRESULT]
    GetDesktopItemOptions: _Callable
    SetDesktopItemOptions: _Callable
    AddDesktopItem: _Callable
    AddDesktopItemWithUI: _Callable
    ModifyDesktopItem: _Callable
    RemoveDesktopItem: _Callable
    GetDesktopItemCount: _Callable[[_header.Pointer[_ctype.c_int], _ctype.DWORD], _ctype.HRESULT]
    GetDesktopItem: _Callable
    GetDesktopItemByID: _Callable
    GenerateDesktopItemHtml: _Callable
    AddUrl: _Callable
    GetDesktopItemBySource: _Callable


class IDesktopWallpaper(IUnknown):
    __CLSID__ = _const.CLSID_DesktopWallpaper
    SetWallpaper: _Callable[[_ctype.LPCWSTR, _ctype.LPCWSTR], _ctype.HRESULT]
    GetWallpaper: _Callable[[_ctype.LPCWSTR, _header.Pointer[_ctype.LPWSTR]], _ctype.HRESULT]
    GetMonitorDevicePathAt: _Callable[[_ctype.UINT, _header.Pointer[_ctype.LPWSTR]], _ctype.HRESULT]
    GetMonitorDevicePathCount: _Callable[[_header.Pointer[_ctype.UINT]], _ctype.HRESULT]
    GetMonitorRECT: _Callable[[_ctype.LPCWSTR, _header.Pointer[_struct.RECT]], _ctype.HRESULT]
    SetBackgroundColor: _Callable[[_ctype.COLORREF], _ctype.HRESULT]
    GetBackgroundColor: _Callable[[_header.Pointer[_ctype.COLORREF]], _ctype.HRESULT]
    SetPosition: _Callable[[_ctype.DESKTOP_WALLPAPER_POSITION], _ctype.HRESULT]
    GetPosition: _Callable[[_header.Pointer[_ctype.DESKTOP_WALLPAPER_POSITION]], _ctype.HRESULT]
    SetSlideshow: _Callable
    GetSlideshow: _Callable
    SetSlideshowOptions: _Callable[[_ctype.DESKTOP_SLIDESHOW_OPTIONS, _ctype.UINT], _ctype.HRESULT]
    GetSlideshowOptions: _Callable[[_ctype.DESKTOP_SLIDESHOW_OPTIONS, _header.Pointer[_ctype.UINT]], _ctype.HRESULT]
    AdvanceSlideshow: _Callable[[_ctype.LPCWSTR, _ctype.DESKTOP_SLIDESHOW_DIRECTION], _ctype.HRESULT]
    GetStatus: _Callable[[_header.Pointer[_ctype.DESKTOP_SLIDESHOW_STATE]], _ctype.HRESULT]
    Enable: _Callable[[_ctype.BOOL], _ctype.HRESULT]


class IModalWindow(IUnknown):
    __CLSID__ = _const.CLSID_FileOpenDialog
    Show: _Callable[[_ctype.HWND], _ctype.HRESULT]


class IFileDialog(IModalWindow):
    SetFileTypes: _Callable
    SetFileTypeIndex: _Callable[[_ctype.UINT], _ctype.HRESULT]
    GetFileTypeIndex: _Callable[[_ctype.UINT], _ctype.HRESULT]
    Advise: _Callable
    Unadvise: _Callable
    SetOptions: _Callable
    GetOptions: _Callable
    SetDefaultFolder: _Callable
    SetFolder: _Callable
    GetFolder: _Callable
    GetCurrentSelection: _Callable
    SetFileName: _Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    GetFileName: _Callable[[_ctype.LPWSTR], _ctype.HRESULT]
    SetTitle: _Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    SetOkButtonLabel: _Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    SetFileNameLabel: _Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    GetResult: _Callable
    AddPlace: _Callable
    SetDefaultExtension: _Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    Close: _Callable[[_ctype.HRESULT], _ctype.HRESULT]
    SetClientGuid: _Callable[[_header.Pointer[_struct.GUID]], _ctype.HRESULT]
    ClearClientData: _Callable[[], _ctype.HRESULT]
    SetFilter: _Callable


class IFileOpenDialog(IFileDialog):
    GetResults: _Callable
    GetSelectedItems: _Callable


def _method_type(types: _Callable) -> list:
    types_ = _header.resolve_type(types)
    types_.insert(1, _ctypes.c_void_p)
    return types_


def __getattr__(name: str) -> type[_ctypes.c_void_p]:
    class Wrapper(_ctypes.c_void_p):
        # noinspection PyTypeChecker
        _pointer = _ctypes.POINTER(type('', (_ctypes.Structure,), {'_fields_': tuple((func, _ctypes.WINFUNCTYPE(
            *_method_type(types))) for func, types in _typing.get_type_hints(_com[name], _globals).items())}))
        # noinspection PyProtectedMember
        _methods = tuple(types for types in dir(_pointer._type_) if not types.startswith('_'))

        def __getattr__(self, name_):
            if name_ in self._methods:
                funcs = _ctypes.cast(_ctypes.cast(self, _ctypes.POINTER(
                    _ctypes.c_void_p)).contents.value, self._pointer).contents
                for method in self._methods:
                    setattr(self, method, _types.MethodType(getattr(funcs, method), self))
            return super().__getattribute__(name_)

    _globals[name] = _functools.update_wrapper(Wrapper, _com[name], ('__CLSID__', *_functools.WRAPPER_ASSIGNMENTS), ())
    return _globals[name]


_com = _header.init(globals())
_globals = _header.Dict(globals(), __getattr__)
if _header.INIT:
    for _com_ in _com:
        __getattr__(_com_)
