import ctypes
import ctypes.wintypes
import functools
import os
import shlex
import typing
import winreg

_MAX_PATH = ctypes.wintypes.UINT(160)
_CSIDL_APPDATA = ctypes.wintypes.INT(26)
_CSIDL_LOCAL_APPDATA = ctypes.wintypes.INT(28)
_CSIDL_MYPICTURES = ctypes.wintypes.INT(39)
_SHGFP_TYPE_CURRENT = ctypes.wintypes.DWORD(0)
_GMEM_MOVEABLE = ctypes.wintypes.UINT(2)
_CF_UNICODETEXT = ctypes.wintypes.UINT(13)
_SPI_GETDESKWALLPAPER = ctypes.wintypes.UINT(115)
_SPI_SETDESKWALLPAPER = ctypes.wintypes.UINT(20)
_SPIF_SENDWININICHANGE = ctypes.wintypes.UINT(2)
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


class _CtypesTypedFunction:
    def __init_subclass__(cls):
        for var, value in cls.__dict__.items():
            if not var.startswith('__') and not var.endswith('__'):
                *value.argtypes, value.restype = cls.__annotations__[var].__args__


class _Function(_CtypesTypedFunction):
    memmove: typing.Callable[[ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_size_t],
                             ctypes.c_void_p] = ctypes.cdll.msvcrt.memmove
    wcslen: typing.Callable[[ctypes.c_wchar_p],
                            ctypes.c_size_t] = ctypes.cdll.msvcrt.wcslen
    sh_get_folder_path: typing.Callable[[ctypes.wintypes.HWND, ctypes.wintypes.INT, ctypes.wintypes.HANDLE,
                                         ctypes.wintypes.DWORD, ctypes.wintypes.LPWSTR],
                                        ctypes.c_long] = ctypes.windll.shell32.SHGetFolderPathW
    open_clipboard: typing.Callable[[ctypes.wintypes.HWND],
                                    ctypes.wintypes.BOOL] = ctypes.windll.user32.OpenClipboard
    close_clipboard: typing.Callable[[],
                                     ctypes.wintypes.BOOL] = ctypes.windll.user32.CloseClipboard
    empty_clipboard: typing.Callable[[],
                                     ctypes.wintypes.BOOL] = ctypes.windll.user32.EmptyClipboard
    set_clipboard_data: typing.Callable[[ctypes.wintypes.UINT, ctypes.wintypes.HANDLE],
                                        ctypes.wintypes.HANDLE] = ctypes.windll.user32.SetClipboardData
    global_alloc: typing.Callable[[ctypes.wintypes.UINT, ctypes.c_size_t],
                                  ctypes.wintypes.HGLOBAL] = ctypes.windll.kernel32.GlobalAlloc
    global_lock: typing.Callable[[ctypes.wintypes.LPVOID],
                                 ctypes.wintypes.HGLOBAL] = ctypes.windll.kernel32.GlobalLock
    global_unlock: typing.Callable[[ctypes.wintypes.HGLOBAL],
                                   ctypes.wintypes.BOOL] = ctypes.windll.kernel32.GlobalUnlock
    system_parameters_info: typing.Callable[[ctypes.wintypes.UINT, ctypes.wintypes.UINT,
                                             ctypes.c_wchar_p, ctypes.wintypes.UINT],
                                            ctypes.wintypes.BOOL] = ctypes.windll.user32.SystemParametersInfoW


@functools.lru_cache(1)
def _get_buffer(size: int) -> ctypes.wintypes.LPWSTR:
    return ctypes.wintypes.LPWSTR(' ' * size)


def _get_dir(csidl: ctypes.wintypes.INT) -> str:
    buffer = _get_buffer(_MAX_PATH.value)
    _Function.sh_get_folder_path(ctypes.c_void_p(), csidl, ctypes.c_void_p(), _SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(_CSIDL_APPDATA)
PICTURES_DIR = _get_dir(_CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(_CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def copy_text(text: typing.Optional[str] = None) -> bool:
    _Function.open_clipboard(ctypes.wintypes.HWND())
    _Function.empty_clipboard()
    string = ctypes.c_wchar_p(text or '')
    if string:
        # noinspection PyTypeChecker
        size = ctypes.c_size_t((_Function.wcslen(string) + 1) * ctypes.sizeof(ctypes.c_wchar))
        handle = _Function.global_alloc(_GMEM_MOVEABLE, size)
        if handle:
            handle_locked = _Function.global_lock(handle)
            if handle_locked:
                _Function.memmove(handle_locked, string, size)
                _Function.global_unlock(handle)
                _Function.set_clipboard_data(_CF_UNICODETEXT, handle)
    _Function.close_clipboard()
    return False  # TODO: read and verify clipboard


def get_wallpaper_path() -> str:  # TODO: if not exist, check cache/save also
    buffer = _get_buffer(_MAX_PATH.value)
    _Function.system_parameters_info(_SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, ctypes.wintypes.UINT())
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
