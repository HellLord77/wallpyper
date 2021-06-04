import ctypes
import ctypes.wintypes
import functools
import os
import shlex
import typing
import winreg

_MAX_PATH = 160
_CSIDL_APPDATA = 26
_CSIDL_LOCAL_APPDATA = 28
_CSIDL_MYPICTURES = 39
_SHGFP_TYPE_CURRENT = 0
_GMEM_MOVEABLE = 2
_CF_UNICODETEXT = 13
_SPI_GETDESKWALLPAPER = 115
_SPI_SETDESKWALLPAPER = 20
_SPIF_NONE = 0
_SPIF_SENDWININICHANGE = 2
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


class _GdiplusStartupInput(ctypes.Structure):
    _fields_ = (('GdiplusVersion', ctypes.c_uint32),
                ('DebugEventCallback', ctypes.c_void_p),
                ('SuppressBackgroundThread', ctypes.wintypes.BOOL),
                ('SuppressExternalCodecs', ctypes.wintypes.BOOL))

    def __init__(self):
        super().__init__(ctypes.c_uint32(1), ctypes.c_void_p(),
                         ctypes.wintypes.BOOL(False), ctypes.wintypes.BOOL(False))


class _CtypesTypedFunction:
    def __init_subclass__(cls):
        for var, value in cls.__dict__.items():
            if not var.startswith('_'):
                *value.argtypes, value.restype = (cls._resolve_union(arg) for arg in cls.__annotations__[var].__args__)

    @staticmethod
    def _resolve_union(argtype):
        # noinspection PyProtectedMember,PyUnresolvedReferences
        return argtype.__args__[0] if isinstance(argtype, typing._UnionGenericAlias) else argtype


class _Function(_CtypesTypedFunction):
    _c_int = typing.Union[ctypes.c_int, int]
    _c_uint = typing.Union[ctypes.c_uint, int]
    _c_long = typing.Union[ctypes.c_long, int]
    _c_ulong = typing.Union[ctypes.c_ulong, int]
    _size_t = typing.Union[ctypes.c_size_t, int]

    _HANDLE = typing.Union[ctypes.c_void_p, int]
    _LPVOID = ctypes.c_void_p
    _LPWSTR = ctypes.c_wchar_p
    _PVOID = typing.Union[ctypes.c_void_p, ctypes.c_wchar_p]
    _INT = _c_int
    _BOOL = _c_long
    _HRESULT = _c_long
    _DWORD = _c_ulong
    _UINT = _c_uint
    _ULONG_PTR = _c_ulong
    _HGLOBAL = _HANDLE
    _HINSTANCE = _HANDLE
    _HWND = _HANDLE
    _SIZE_T = _ULONG_PTR

    memmove: typing.Callable[[ctypes.c_void_p, typing.Union[ctypes.c_void_p, ctypes.c_wchar_p],
                              _size_t],
                             ctypes.c_void_p] = ctypes.cdll.msvcrt.memmove
    wcslen: typing.Callable[[ctypes.c_wchar_p],
                            _size_t] = ctypes.cdll.msvcrt.wcslen

    global_alloc: typing.Callable[[_UINT, _SIZE_T],
                                  _HGLOBAL] = ctypes.windll.kernel32.GlobalAlloc
    global_lock: typing.Callable[[_HGLOBAL],
                                 _LPVOID] = ctypes.windll.kernel32.GlobalLock
    global_unlock: typing.Callable[[_HGLOBAL],
                                   _BOOL] = ctypes.windll.kernel32.GlobalUnlock

    system_parameters_info: typing.Callable[[_UINT, _UINT, _PVOID, _UINT],
                                            _BOOL] = ctypes.windll.user32.SystemParametersInfoW
    open_clipboard: typing.Callable[[typing.Optional[_HWND]],
                                    _BOOL] = ctypes.windll.user32.OpenClipboard
    close_clipboard: typing.Callable[[],
                                     _BOOL] = ctypes.windll.user32.CloseClipboard
    empty_clipboard: typing.Callable[[],
                                     _BOOL] = ctypes.windll.user32.EmptyClipboard
    get_clipboard_data: typing.Callable[[_UINT],
                                        _HANDLE] = ctypes.windll.user32.GetClipboardData
    set_clipboard_data: typing.Callable[[_UINT, _HANDLE],
                                        _HANDLE] = ctypes.windll.user32.SetClipboardData

    sh_get_folder_path: typing.Callable[[typing.Optional[_HWND], _c_int, typing.Optional[_HANDLE], _DWORD, _LPWSTR],
                                        _HRESULT] = ctypes.windll.shell32.SHGetFolderPathW  # TODO: SHGetKnownFolderPath

    load_image: typing.Callable[[_HINSTANCE, _LPWSTR, _UINT, _INT, _INT, _UINT],
                                _HANDLE] = ctypes.windll.user32.LoadImageW
    gdiplus_startup: typing.Callable[[ctypes.POINTER(ctypes.wintypes.ULONG),
                                      ctypes.POINTER(_GdiplusStartupInput), ctypes.c_void_p],
                                     ctypes.c_int] = ctypes.windll.gdiplus.GdiplusStartup
    gdiplus_shutdown: typing.Callable[[ctypes.POINTER(ctypes.wintypes.ULONG)],
                                      ctypes.c_void_p] = ctypes.windll.gdiplus.GdiplusShutdown
    gdip_create_bitmap_from_file: typing.Callable[[ctypes.POINTER(ctypes.wintypes.WCHAR), _BOOL],
                                                  ctypes.c_void_p] = ctypes.windll.gdiplus.GdipCreateBitmapFromFile


@functools.lru_cache(1)
def _get_buffer(size: int) -> ctypes.wintypes.LPWSTR:
    return ctypes.wintypes.LPWSTR(' ' * size)


def _get_dir(csidl: int) -> str:
    buffer = _get_buffer(_MAX_PATH)
    _Function.sh_get_folder_path(None, csidl, None, _SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(_CSIDL_APPDATA)
PICTURES_DIR = _get_dir(_CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(_CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def paste_text() -> str:
    _Function.open_clipboard(None)
    handle = _Function.get_clipboard_data(_CF_UNICODETEXT)
    _Function.close_clipboard()
    return ctypes.c_wchar_p(handle).value or ''


def copy_text(text: str) -> bool:
    _Function.open_clipboard(ctypes.wintypes.HWND())
    _Function.empty_clipboard()
    string = ctypes.c_wchar_p(text)
    size = (_Function.wcslen(string) + 1) * ctypes.sizeof(ctypes.c_wchar)
    handle = _Function.global_alloc(_GMEM_MOVEABLE, size)
    if handle:
        handle_locked = _Function.global_lock(handle)
        if handle_locked:
            _Function.memmove(handle_locked, string, size)
            _Function.global_unlock(handle)
            _Function.set_clipboard_data(_CF_UNICODETEXT, handle)
    _Function.close_clipboard()
    return string.value == paste_text()


def copy_image(path: str) -> bool:
    token = ctypes.c_ulong()
    ret = _Function.gdiplus_startup(token, _GdiplusStartupInput(), ctypes.c_void_p())  # ok = 0
    print(ret)
    ret = _Function.gdiplus_shutdown(token)
    print(ret)
    return False


def get_wallpaper_path() -> str:  # TODO: if not exist, check cache/save also
    buffer = _get_buffer(_MAX_PATH)
    _Function.system_parameters_info(_SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, _SPIF_NONE)
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            _Function.system_parameters_info(_SPI_SETDESKWALLPAPER, ctypes.wintypes.UINT(),
                                             ctypes.c_wchar_p(path), _SPIF_SENDWININICHANGE)
            return True
    return False


def register_autorun(name: str,
                     path: str,
                     *args: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY,
                        access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE) as key:
        value = shlex.join((path,) + args)
        try:
            winreg.SetValueEx(key, name, None, winreg.REG_SZ, value)
        except PermissionError:
            return False
        winreg.FlushKey(key)
        return (value, winreg.REG_SZ) == winreg.QueryValueEx(key, name)


def unregister_autorun(name: str) -> bool:
    if register_autorun(name, ''):
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY, access=winreg.KEY_SET_VALUE) as key:
            winreg.DeleteValue(key, name)
            return True
    return False
