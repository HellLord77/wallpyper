import os
import shlex
import winreg

from libraries import c
from libraries import cache

_MAX_PATH = 160
_CSIDL_APPDATA = 26
_CSIDL_LOCAL_APPDATA = 28
_CSIDL_MYPICTURES = 39
_SHGFP_TYPE_CURRENT = 0
_GMEM_MOVEABLE = 2
_CF_BITMAP = 2
_CF_UNICODETEXT = 13
_SPI_GETDESKWALLPAPER = 115
_SPI_SETDESKWALLPAPER = 20
_SPIF_NONE = 0
_SPIF_SENDWININICHANGE = 2
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


@cache.one_cache
def _get_buffer(size: int) -> c.Type.LPWSTR:
    return c.Type.LPWSTR(' ' * size)


def _get_dir(csidl: int) -> str:
    buffer = _get_buffer(_MAX_PATH)
    c.Function.sh_get_folder_path(None, csidl, None, _SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(_CSIDL_APPDATA)
PICTURES_DIR = _get_dir(_CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(_CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def paste_text() -> str:
    c.Function.open_clipboard(None)
    handle = c.Function.get_clipboard_data(_CF_UNICODETEXT)
    c.Function.close_clipboard()
    return c.Type.c_wchar_p(handle).value or ''


def copy_text(text: str) -> bool:
    size = (len(text) + 1) * c.sizeof(c.Type.c_wchar)
    handle = c.Function.global_alloc(_GMEM_MOVEABLE, size)
    if handle:
        buffer = c.Function.global_lock(handle)
        if buffer:
            c.Function.memmove(buffer, text, size)
            c.Function.open_clipboard(None)
            c.Function.empty_clipboard()
            c.Function.set_clipboard_data(_CF_UNICODETEXT, handle)
            c.Function.close_clipboard()
        c.Function.global_unlock(handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    token = c.Type.ULONG_PTR()
    print(c.Function.gdiplus_startup(c.byref(token), c.byref(c.Structure.GdiplusStartupInput()), None))
    # ok == 0
    bitmap = c.Type.GpBitmap()
    print(c.Function.gdip_create_bitmap_from_file(path, c.byref(bitmap)))  # ok == 0
    hbitmap = c.Type.HBITMAP()
    print(c.Function.gdip_create_HBITMAP_from_bitmap(bitmap, c.byref(hbitmap), 0))
    print(c.Function.gdip_dispose_image(bitmap))
    print(c.Function.gdiplus_shutdown(c.byref(token)))
    bitmap = c.Structure.BITMAP()
    print(c.Function.get_object(hbitmap, c.sizeof(c.Structure.BITMAP), c.byref(bitmap)))  # ok != 0

    print(bitmap.bmHeight)

    return False


def get_wallpaper_path() -> str:  # TODO: if not exist, check cache/save also
    buffer = _get_buffer(_MAX_PATH)
    c.Function.system_parameters_info(_SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, _SPIF_NONE)
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            c.Function.system_parameters_info(_SPI_SETDESKWALLPAPER, c.Type.UINT(),
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
