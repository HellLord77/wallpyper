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
            if var in cls.__annotations__:
                *value.argtypes, value.restype = (cls._fix_union(arg) for arg in cls.__annotations__[var].__args__)

    @staticmethod
    def _fix_union(argtype):
        # noinspection PyProtectedMember,PyUnresolvedReferences
        return argtype.__args__[0] if isinstance(argtype, typing._UnionGenericAlias) else argtype


class _Function(_CtypesTypedFunction):
    HRESULT = ctypes.wintypes.LONG
    PVOID = ctypes.c_void_p
    SIZE_T = ctypes.c_ulong

    memmove: typing.Callable[[ctypes.c_void_p, typing.Union[ctypes.c_void_p, ctypes.c_wchar_p],
                              typing.Union[ctypes.c_size_t, int]],
                             ctypes.c_void_p] = ctypes.cdll.msvcrt.memmove
    wcslen: typing.Callable[[ctypes.c_wchar_p],
                            typing.Union[ctypes.c_size_t, int]] = ctypes.cdll.msvcrt.wcslen
    sh_get_folder_path: typing.Callable[[ctypes.wintypes.HWND, ctypes.c_int, ctypes.wintypes.HANDLE,
                                         ctypes.wintypes.DWORD, ctypes.wintypes.LPWSTR],  # TODO: SHGetKnownFolderPath
                                        HRESULT] = ctypes.windll.shell32.SHGetFolderPathW
    global_alloc: typing.Callable[[ctypes.wintypes.UINT, SIZE_T],
                                  ctypes.wintypes.HGLOBAL] = ctypes.windll.kernel32.GlobalAlloc
    global_lock: typing.Callable[[ctypes.wintypes.HGLOBAL],
                                 ctypes.wintypes.LPVOID] = ctypes.windll.kernel32.GlobalLock
    global_unlock: typing.Callable[[ctypes.wintypes.HGLOBAL],
                                   ctypes.wintypes.BOOL] = ctypes.windll.kernel32.GlobalUnlock
    system_parameters_info: typing.Callable[[ctypes.wintypes.UINT, ctypes.wintypes.UINT,
                                             PVOID, ctypes.wintypes.UINT],
                                            ctypes.wintypes.BOOL] = ctypes.windll.user32.SystemParametersInfoW
    open_clipboard: typing.Callable[[ctypes.wintypes.HWND],
                                    ctypes.wintypes.BOOL] = ctypes.windll.user32.OpenClipboard
    close_clipboard: typing.Callable[[],
                                     ctypes.wintypes.BOOL] = ctypes.windll.user32.CloseClipboard
    empty_clipboard: typing.Callable[[],
                                     ctypes.wintypes.BOOL] = ctypes.windll.user32.EmptyClipboard
    get_clipboard_data: typing.Callable[[ctypes.wintypes.UINT],
                                        ctypes.wintypes.HANDLE] = ctypes.windll.user32.GetClipboardData
    set_clipboard_data: typing.Callable[[ctypes.wintypes.UINT, ctypes.wintypes.HANDLE],
                                        ctypes.wintypes.HANDLE] = ctypes.windll.user32.SetClipboardData

    load_image: typing.Callable[[ctypes.wintypes.HINSTANCE, ctypes.wintypes.LPWSTR, ctypes.wintypes.UINT,
                                 ctypes.wintypes.INT, ctypes.wintypes.INT, ctypes.wintypes.UINT],
                                ctypes.wintypes.HANDLE] = ctypes.windll.user32.LoadImageW  # TODO: ctypes.windll.gdi32
    gdiplus_startup: typing.Callable[[ctypes.POINTER(ctypes.wintypes.ULONG),
                                      ctypes.POINTER(_GdiplusStartupInput), ctypes.c_void_p],
                                     ctypes.c_int] = ctypes.windll.gdiplus.GdiplusStartup
    gdiplus_shutdown: typing.Callable[[ctypes.POINTER(ctypes.wintypes.ULONG)],
                                      ctypes.c_void_p] = ctypes.windll.gdiplus.GdiplusShutdown
    gdip_create_bitmap_from_file: typing.Callable[[ctypes.POINTER(ctypes.wintypes.WCHAR), ctypes.wintypes.BOOL],
                                                  ctypes.c_void_p] = ctypes.windll.gdiplus.GdipCreateBitmapFromFile


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


def paste_text() -> str:
    _Function.open_clipboard(ctypes.wintypes.HWND())
    handle = _Function.get_clipboard_data(_CF_UNICODETEXT)
    _Function.close_clipboard()
    # noinspection PyTypeChecker
    return ctypes.c_wchar_p(handle).value or ''


def copy_text(text: str) -> bool:
    _Function.open_clipboard(ctypes.wintypes.HWND())
    _Function.empty_clipboard()
    string = ctypes.c_wchar_p(text)
    size = _Function.SIZE_T((_Function.wcslen(string) + 1) * ctypes.sizeof(ctypes.c_wchar))
    handle = _Function.global_alloc(_GMEM_MOVEABLE, size)
    if handle:
        handle_locked = _Function.global_lock(handle)
        if handle_locked:
            _Function.memmove(handle_locked, string, size.value)
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
    buffer = _get_buffer(_MAX_PATH.value)
    _Function.system_parameters_info(_SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, ctypes.wintypes.UINT())
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            # noinspection PyTypeChecker
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
