import functools
import os
import shlex
import winreg

from libraries import ctype

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


@functools.lru_cache(1)
def _get_buffer(size: int) -> ctype.Type.LPWSTR:
    return ctype.Type.LPWSTR(' ' * size)


def _get_dir(csidl: int) -> str:
    buffer = _get_buffer(_MAX_PATH)
    ctype.Function.sh_get_folder_path(None, csidl, None, _SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(_CSIDL_APPDATA)
PICTURES_DIR = _get_dir(_CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(_CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def paste_text() -> str:
    ctype.Function.open_clipboard(None)
    handle = ctype.Function.get_clipboard_data(_CF_UNICODETEXT)
    ctype.Function.close_clipboard()
    return ctype.Type.c_wchar_p(handle).value or ''


def copy_text(text: str) -> bool:
    size = (len(text) + 1) * ctype.sizeof(ctype.Type.c_wchar)
    handle = ctype.Function.global_alloc(_GMEM_MOVEABLE, size)
    if handle:
        buffer = ctype.Function.global_lock(handle)
        if buffer:
            ctype.Function.memmove(buffer, text, size)
            ctype.Function.open_clipboard(None)
            ctype.Function.empty_clipboard()
            ctype.Function.set_clipboard_data(_CF_UNICODETEXT, handle)
            ctype.Function.close_clipboard()
        ctype.Function.global_unlock(handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    token = ctype.Type.ULONG_PTR()
    print(ctype.Function.gdiplus_startup(ctype.byref(token), ctype.byref(ctype.Structure.GdiplusStartupInput()), None))
    # ok == 0
    bitmap = ctype.Type.GpBitmap()
    print(ctype.Function.gdip_create_bitmap_from_file(path, ctype.byref(bitmap)))  # ok == 0
    hbitmap = ctype.Type.HBITMAP()
    print(ctype.Function.gdip_create_HBITMAP_from_bitmap(bitmap, ctype.byref(hbitmap), 0))
    print(ctype.Function.gdip_dispose_image(bitmap))
    print(ctype.Function.gdiplus_shutdown(ctype.byref(token)))

    return False


def get_wallpaper_path() -> str:  # TODO: if not exist, check cache/save also
    buffer = _get_buffer(_MAX_PATH)
    ctype.Function.system_parameters_info(_SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, _SPIF_NONE)
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            ctype.Function.system_parameters_info(_SPI_SETDESKWALLPAPER, ctype.Type.UINT(),
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
