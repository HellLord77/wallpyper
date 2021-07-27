__version__ = '0.0.3'

import contextlib
import os
import shlex
import winreg

import libraries.ctype

_MAX_PATH = 32 * 1024
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


def _get_dir(csidl: int) -> str:
    buffer = libraries.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.Func.sh_get_folder_path(None, csidl, None, libraries.ctype.Const.SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(libraries.ctype.Const.CSIDL_APPDATA)
PICTURES_DIR = _get_dir(libraries.ctype.Const.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(libraries.ctype.Const.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def _get_clipboard(format_: int) -> libraries.ctype.Type.HANDLE:
    libraries.ctype.Func.open_clipboard(None)
    handle = libraries.ctype.Func.get_clipboard_data(format_)
    libraries.ctype.Func.close_clipboard()
    return handle


def paste_text() -> str:
    return libraries.ctype.cast(_get_clipboard(libraries.ctype.Const.CF_UNICODETEXT),
                                libraries.ctype.Type.c_wchar_p).value or ''


def _set_clipboard(format_: int,
                   hglobal: int) -> None:
    libraries.ctype.Func.open_clipboard(None)
    libraries.ctype.Func.empty_clipboard()
    libraries.ctype.Func.set_clipboard_data(format_, hglobal)
    libraries.ctype.Func.close_clipboard()


def copy_text(text: str) -> bool:
    size = (libraries.ctype.Func.wcslen(text) + 1) * libraries.ctype.sizeof(libraries.ctype.Type.c_wchar)
    handle = libraries.ctype.Func.global_alloc(libraries.ctype.Const.GMEM_MOVEABLE, size)
    if handle:
        buffer = libraries.ctype.Func.global_lock(handle)
        if buffer:
            libraries.ctype.Func.memmove(buffer, text, size)
            _set_clipboard(libraries.ctype.Const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _get_hbitmap(path: str) -> libraries.ctype.Type.HBITMAP:
    hbitmap = libraries.ctype.Type.HBITMAP()
    token = libraries.ctype.Type.ULONG_PTR()
    if not libraries.ctype.Func.gdiplus_startup(
            libraries.ctype.byref(token), libraries.ctype.byref(libraries.ctype.Struct.GdiplusStartupInput()), None):
        bitmap = libraries.ctype.Type.GpBitmap()
        if not libraries.ctype.Func.gdip_create_bitmap_from_file(
                libraries.ctype.array(libraries.ctype.Type.WCHAR, *path, '\0'), libraries.ctype.byref(bitmap)):
            libraries.ctype.Func.gdip_create_HBITMAP_from_bitmap(bitmap, libraries.ctype.byref(hbitmap), 0)
            libraries.ctype.Func.gdip_dispose_image(bitmap)
    libraries.ctype.Func.gdiplus_shutdown(token)
    try:
        yield hbitmap
    finally:
        if hbitmap:
            libraries.ctype.Func.delete_object(hbitmap)


def copy_image(path: str) -> bool:
    buffer = 0
    with _get_hbitmap(path) as hbitmap:
        bm = libraries.ctype.Struct.BITMAP()
        if libraries.ctype.sizeof(libraries.ctype.Struct.BITMAP) == libraries.ctype.Func.get_object(
                hbitmap, libraries.ctype.sizeof(libraries.ctype.Struct.BITMAP), libraries.ctype.byref(bm)):
            size_bi = libraries.ctype.sizeof(libraries.ctype.Struct.BITMAPINFOHEADER)
            bi = libraries.ctype.Struct.BITMAPINFOHEADER(size_bi, bm.bmWidth, bm.bmHeight, 1,
                                                         bm.bmBitsPixel, libraries.ctype.Const.BI_RGB)
            size = bm.bmWidthBytes * bm.bmHeight
            data = libraries.ctype.array(libraries.ctype.Type.BYTE, size=size)
            hdc = libraries.ctype.Func.get_DC(None)
            if libraries.ctype.Func.get_DI_bits(hdc, hbitmap, 0, bi.biHeight, data, libraries.ctype.cast(
                    libraries.ctype.byref(bi), libraries.ctype.Pointer(libraries.ctype.Struct.BITMAPINFO)),
                                                libraries.ctype.Const.DIB_RGB_COLORS):
                handle = libraries.ctype.Func.global_alloc(libraries.ctype.Const.GMEM_MOVEABLE, size_bi + size)
                if handle:
                    buffer = libraries.ctype.Func.global_lock(handle)
                    if buffer:
                        libraries.ctype.Func.memmove(buffer, libraries.ctype.byref(bi), size_bi)
                        libraries.ctype.Func.memmove(buffer + size_bi, data, size)
                        _set_clipboard(libraries.ctype.Const.CF_DIB, handle)
                    libraries.ctype.Func.global_unlock(handle)
            libraries.ctype.Func.release_DC(None, hdc)
    return bool(buffer)


def get_wallpaper_path() -> str:
    buffer = libraries.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.Func.system_parameters_info(libraries.ctype.Const.SPI_GETDESKWALLPAPER,
                                                _MAX_PATH, buffer, libraries.ctype.Const.SPIF_NONE)
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            libraries.ctype.Func.system_parameters_info(libraries.ctype.Const.SPI_SETDESKWALLPAPER, 0,
                                                        path, libraries.ctype.Const.SPIF_SENDWININICHANGE)
            return True
    return False


def _swap_char(string: str,
               a: str,
               b: str) -> str:
    return ''.join(a if char == b else b if char == a else char for char in string)


def register_autorun(name: str,
                     path: str,
                     *args: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY,
                        access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE) as key:
        value = _swap_char(shlex.join((path,) + args), '"', "'")
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
