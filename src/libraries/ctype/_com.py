import ctypes as _ctypes
import functools as _functools
import types as _types
import typing as _typing

from . import _const
from . import _ctype
from . import _header
from . import _struct


class IUnknown:
    _CLSID = ''
    QueryInterface: _typing.Callable[[_header.Pointer[_struct.IID], _ctype.c_void_p], _ctype.HRESULT]
    AddRef: _typing.Callable[[], _ctype.ULONG]
    Release: _typing.Callable[[], _ctype.ULONG]


class IActiveDesktop(IUnknown):
    _CLSID = _const.CLSID_ActiveDesktop
    ApplyChanges: _typing.Callable[[_ctype.DWORD], _ctype.HRESULT]
    GetWallpaper: _typing.Callable[[_ctype.PWSTR, _ctype.UINT, _ctype.DWORD], _ctype.HRESULT]
    SetWallpaper: _typing.Callable[[_ctype.PCWSTR, _ctype.DWORD], _ctype.HRESULT]
    GetWallpaperOptions: _typing.Callable[[_header.Pointer[_struct.WALLPAPEROPT], _ctype.DWORD], _ctype.HRESULT]
    SetWallpaperOptions: _typing.Callable[[_header.Pointer[_struct.WALLPAPEROPT], _ctype.DWORD], _ctype.HRESULT]
    GetPattern: _typing.Callable[[_ctype.PWSTR, _ctype.UINT, _ctype.DWORD], _ctype.HRESULT]
    SetPattern: _typing.Callable[[_ctype.PCWSTR, _ctype.DWORD], _ctype.HRESULT]
    GetDesktopItemOptions: _typing.Callable
    SetDesktopItemOptions: _typing.Callable
    AddDesktopItem: _typing.Callable
    AddDesktopItemWithUI: _typing.Callable
    ModifyDesktopItem: _typing.Callable
    RemoveDesktopItem: _typing.Callable
    GetDesktopItemCount: _typing.Callable[[_header.Pointer[_ctype.c_int], _ctype.DWORD], _ctype.HRESULT]
    GetDesktopItem: _typing.Callable
    GetDesktopItemByID: _typing.Callable
    GenerateDesktopItemHtml: _typing.Callable
    AddUrl: _typing.Callable
    GetDesktopItemBySource: _typing.Callable


class IDesktopWallpaper(IUnknown):
    _CLSID = _const.CLSID_DesktopWallpaper
    SetWallpaper: _typing.Callable[[_ctype.LPCWSTR, _ctype.LPCWSTR], _ctype.HRESULT]
    GetWallpaper: _typing.Callable[[_ctype.LPCWSTR, _header.Pointer[_ctype.LPWSTR]], _ctype.HRESULT]
    GetMonitorDevicePathAt: _typing.Callable[[_ctype.UINT, _header.Pointer[_ctype.LPWSTR]], _ctype.HRESULT]
    GetMonitorDevicePathCount: _typing.Callable[[_header.Pointer[_ctype.UINT]], _ctype.HRESULT]
    GetMonitorRECT: _typing.Callable[[_ctype.LPCWSTR, _header.Pointer[_struct.RECT]], _ctype.HRESULT]
    SetBackgroundColor: _typing.Callable[[_ctype.COLORREF], _ctype.HRESULT]
    GetBackgroundColor: _typing.Callable[[_header.Pointer[_ctype.COLORREF]], _ctype.HRESULT]
    SetPosition: _typing.Callable[[_ctype.DESKTOP_WALLPAPER_POSITION], _ctype.HRESULT]
    GetPosition: _typing.Callable[[_header.Pointer[_ctype.DESKTOP_WALLPAPER_POSITION]], _ctype.HRESULT]
    SetSlideshow: _typing.Callable
    GetSlideshow: _typing.Callable
    SetSlideshowOptions: _typing.Callable[[_ctype.DESKTOP_SLIDESHOW_OPTIONS, _ctype.UINT], _ctype.HRESULT]
    GetSlideshowOptions: _typing.Callable[
        [_ctype.DESKTOP_SLIDESHOW_OPTIONS, _header.Pointer[_ctype.UINT]], _ctype.HRESULT]
    AdvanceSlideshow: _typing.Callable[[_ctype.LPCWSTR, _ctype.DESKTOP_SLIDESHOW_DIRECTION], _ctype.HRESULT]
    GetStatus: _typing.Callable[[_header.Pointer[_ctype.DESKTOP_SLIDESHOW_STATE]], _ctype.HRESULT]
    Enable: _typing.Callable[[_ctype.BOOL], _ctype.HRESULT]


class IModalWindow(IUnknown):
    _CLSID = _const.CLSID_FileOpenDialog
    Show: _typing.Callable[[_ctype.HWND], _ctype.HRESULT]


class IFileDialog(IModalWindow):
    SetFileTypes: _typing.Callable
    SetFileTypeIndex: _typing.Callable[[_ctype.UINT], _ctype.HRESULT]
    GetFileTypeIndex: _typing.Callable[[_ctype.UINT], _ctype.HRESULT]
    Advise: _typing.Callable
    Unadvise: _typing.Callable
    SetOptions: _typing.Callable
    GetOptions: _typing.Callable
    SetDefaultFolder: _typing.Callable
    SetFolder: _typing.Callable
    GetFolder: _typing.Callable
    GetCurrentSelection: _typing.Callable
    SetFileName: _typing.Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    GetFileName: _typing.Callable[[_ctype.LPWSTR], _ctype.HRESULT]
    SetTitle: _typing.Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    SetOkButtonLabel: _typing.Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    SetFileNameLabel: _typing.Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    GetResult: _typing.Callable
    AddPlace: _typing.Callable
    SetDefaultExtension: _typing.Callable[[_ctype.LPCWSTR], _ctype.HRESULT]
    Close: _typing.Callable[[_ctype.HRESULT], _ctype.HRESULT]
    SetClientGuid: _typing.Callable[[_header.Pointer[_struct.GUID]], _ctype.HRESULT]
    ClearClientData: _typing.Callable[[], _ctype.HRESULT]
    SetFilter: _typing.Callable


class IFileOpenDialog(IFileDialog):
    GetResults: _typing.Callable
    GetSelectedItems: _typing.Callable


def _method_type(types_: list) -> list:
    types_.insert(1, _ctypes.c_void_p)
    return types_


def _init():  # TODO: cast to IUnknown (?)
    globals_ = globals()
    for var, com_ in _header.items(globals_):
        class Wrapper(_ctypes.c_void_p):
            # noinspection PyTypeChecker
            _pointer = _ctypes.POINTER(
                type(var, (_ctypes.Structure,), {'_fields_': tuple((func, _ctypes.WINFUNCTYPE(*_method_type(
                    _header.resolve_type(types)))) for func, types in _typing.get_type_hints(com_).items())}))
            # noinspection PyProtectedMember
            _methods = tuple(types for types in dir(_pointer._type_) if not types.startswith('_'))

            def __getattr__(self, name):
                if name in self._methods:
                    funcs = _ctypes.cast(_ctypes.cast(self, _ctypes.POINTER(
                        _ctypes.c_void_p)).contents.value, self._pointer).contents
                    for method in self._methods:
                        setattr(self, method, _types.MethodType(getattr(funcs, method), self))
                return super().__getattribute__(name)

        # noinspection PyUnresolvedReferences
        _functools.update_wrapper(Wrapper, com_, _functools.WRAPPER_ASSIGNMENTS + ('_CLSID',), ())
        globals_[var] = Wrapper


_init()
