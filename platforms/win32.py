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


def _is_union(arg):
    # noinspection PyProtectedMember,PyUnresolvedReferences
    return isinstance(arg, typing._UnionGenericAlias)


class _CtypesType:
    def __init_subclass__(cls):
        for var, value in cls.__dict__.items():
            if not var.startswith('__') and not var.endswith('__'):
                if _is_union(value):
                    setattr(cls, var, value.__args__[0])

    @staticmethod
    def byref(arg: ctypes) -> ctypes.pointer:
        # noinspection PyTypeChecker
        return ctypes.byref(arg)


class _Type(_CtypesType):
    pointer = ctypes.POINTER

    c_void_p = typing.Union[ctypes.c_void_p, ctypes.c_wchar_p, int, str]
    c_wchar_p = typing.Union[ctypes.c_wchar_p, str]
    c_int = typing.Union[ctypes.c_int, int]
    c_uint = typing.Union[ctypes.c_uint, int]
    c_uint32 = typing.Union[ctypes.c_uint32, int]
    c_long = typing.Union[ctypes.c_long, int]
    c_ulong = typing.Union[ctypes.c_ulong, int]
    size_t = typing.Union[ctypes.c_size_t, int]
    HRESULT = typing.Union[ctypes.HRESULT, int]
    c_wchar = typing.Union[ctypes.c_wchar, str]

    Bitmap = c_void_p
    HANDLE = c_void_p
    LPVOID = c_void_p
    PVOID = c_void_p
    LPWSTR = c_wchar_p
    INT = c_int
    UINT = c_uint
    BOOL = c_long
    DWORD = c_ulong
    ULONG = c_ulong
    ULONG_PTR = c_ulong
    GpStatus = HRESULT
    WCHAR = c_wchar
    HGDIOBJ = HANDLE
    HGLOBAL = HANDLE
    HINSTANCE = HANDLE
    HWND = HANDLE
    SIZE_T = ULONG_PTR


class _GdiplusStartupInput(ctypes.Structure):
    _fields_ = (('GdiplusVersion', _Type.c_uint32),
                ('DebugEventCallback', _Type.c_void_p),
                ('SuppressBackgroundThread', _Type.BOOL),
                ('SuppressExternalCodecs', _Type.BOOL))

    def __init__(self):
        super().__init__(1, None, False, False)


class _CtypesTypedFunction:
    def __init_subclass__(cls):
        for var, value in cls.__dict__.items():
            if var in cls.__annotations__:
                *value.argtypes, value.restype = (cls._resolve_union(arg) for arg in cls.__annotations__[var].__args__)

    @staticmethod
    def _resolve_union(argtype):
        return argtype.__args__[0] if _is_union(argtype) else argtype


class _Function(_CtypesTypedFunction):
    memmove: typing.Callable[[_Type.c_void_p, _Type.c_void_p,
                              _Type.size_t],
                             _Type.c_void_p] = ctypes.cdll.msvcrt.memmove
    wcslen: typing.Callable[[_Type.c_wchar_p],
                            _Type.size_t] = ctypes.cdll.msvcrt.wcslen

    global_alloc: typing.Callable[[_Type.UINT, _Type.SIZE_T],
                                  _Type.HGLOBAL] = ctypes.windll.kernel32.GlobalAlloc
    global_lock: typing.Callable[[_Type.HGLOBAL],
                                 _Type.LPVOID] = ctypes.windll.kernel32.GlobalLock
    global_unlock: typing.Callable[[_Type.HGLOBAL],
                                   _Type.BOOL] = ctypes.windll.kernel32.GlobalUnlock

    system_parameters_info: typing.Callable[[_Type.UINT, _Type.UINT, _Type.PVOID, _Type.UINT],
                                            _Type.BOOL] = ctypes.windll.user32.SystemParametersInfoW
    open_clipboard: typing.Callable[[typing.Optional[_Type.HWND]],
                                    _Type.BOOL] = ctypes.windll.user32.OpenClipboard
    close_clipboard: typing.Callable[[],
                                     _Type.BOOL] = ctypes.windll.user32.CloseClipboard
    empty_clipboard: typing.Callable[[],
                                     _Type.BOOL] = ctypes.windll.user32.EmptyClipboard
    get_clipboard_data: typing.Callable[[_Type.UINT],
                                        _Type.HANDLE] = ctypes.windll.user32.GetClipboardData
    set_clipboard_data: typing.Callable[[_Type.UINT, _Type.HANDLE],
                                        _Type.HANDLE] = ctypes.windll.user32.SetClipboardData

    sh_get_folder_path: typing.Callable[[typing.Optional[_Type.HWND], _Type.c_int,  # TODO: SHGetKnownFolderPath
                                         typing.Optional[_Type.HANDLE], _Type.DWORD, _Type.LPWSTR],
                                        _Type.HRESULT] = ctypes.windll.shell32.SHGetFolderPathW

    load_image: typing.Callable[[_Type.HINSTANCE, _Type.LPWSTR, _Type.UINT, _Type.INT, _Type.INT, _Type.UINT],
                                _Type.HANDLE] = ctypes.windll.user32.LoadImageW
    gdiplus_startup: typing.Callable[[_Type.pointer(_Type.c_ulong), _Type.pointer(_GdiplusStartupInput),
                                      typing.Optional[_Type.pointer(_GdiplusStartupInput)]],
                                     _Type.c_int] = ctypes.windll.gdiplus.GdiplusStartup
    gdiplus_shutdown: typing.Callable[[_Type.pointer(_Type.c_ulong)],
                                      _Type.c_void_p] = ctypes.windll.gdiplus.GdiplusShutdown
    gdip_create_bitmap_from_file: typing.Callable[[_Type.c_wchar_p, _Type.pointer(_Type.Bitmap)],
                                                  _Type.GpStatus] = ctypes.windll.gdiplus.GdipCreateBitmapFromFile
    delete_object: typing.Callable[[_Type.HGDIOBJ],
                                   _Type.BOOL] = ctypes.windll.gdi32.DeleteObject
    close_handle: typing.Callable[[_Type.HANDLE],
                                  _Type.BOOL] = ctypes.windll.kernel32.CloseHandle


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
    _Function.open_clipboard(None)
    _Function.empty_clipboard()
    size = (_Function.wcslen(text) + 1) * ctypes.sizeof(ctypes.c_wchar)
    handle = _Function.global_alloc(_GMEM_MOVEABLE, size)
    if handle:
        handle_locked = _Function.global_lock(handle)
        if handle_locked:
            _Function.memmove(handle_locked, text, size)
            _Function.global_unlock(handle)
            _Function.set_clipboard_data(_CF_UNICODETEXT, handle)
    _Function.close_clipboard()
    return text == paste_text()


def copy_image(path: str) -> bool:
    token = _Type.c_ulong()
    print(_Function.gdiplus_startup(_Type.byref(token), _Type.byref(_GdiplusStartupInput()), None))  # ok == 0
    bitmap = _Type.Bitmap()
    print(_Function.gdip_create_bitmap_from_file(path, _Type.byref(bitmap)))  # ok == 0
    # working upto here
    print(_Function.close_handle(bitmap))  # ok != 0
    print(_Function.gdiplus_shutdown(_Type.byref(token)))
    return False


def get_wallpaper_path() -> str:  # TODO: if not exist, check cache/save also
    buffer = _get_buffer(_MAX_PATH)
    _Function.system_parameters_info(_SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, _SPIF_NONE)
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            _Function.system_parameters_info(_SPI_SETDESKWALLPAPER, ctypes.wintypes.UINT(),
                                             path, _SPIF_SENDWININICHANGE)
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
