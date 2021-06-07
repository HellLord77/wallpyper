import os
import shlex
import winreg

from libraries import c
from libraries import cache

_MAX_PATH = 260
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


@cache.one_cache
def _get_buffer(size: int) -> c.Type.LPWSTR:
    return c.Type.LPWSTR(' ' * size)


def _get_dir(csidl: int) -> str:
    buffer = _get_buffer(_MAX_PATH)
    c.Function.sh_get_folder_path(None, csidl, None, c.Constant.SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


def _get_clipboard(format_: int) -> c.Type.HANDLE:
    c.Function.open_clipboard(None)
    handle = c.Function.get_clipboard_data(format_)
    c.Function.close_clipboard()
    return handle


def _set_clipboard(format_: int,
                   hglobal: int) -> None:
    c.Function.open_clipboard(None)
    c.Function.empty_clipboard()
    c.Function.set_clipboard_data(format_, hglobal)
    c.Function.close_clipboard()


APPDATA_DIR = _get_dir(c.Constant.CSIDL_APPDATA)
PICTURES_DIR = _get_dir(c.Constant.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(c.Constant.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def paste_text() -> str:
    return c.cast(_get_clipboard(c.Constant.CF_UNICODETEXT), c.Type.c_wchar_p).value or ''


def copy_text(text: str) -> bool:
    size = (c.Function.wcslen(text) + 1) * c.sizeof(c.Type.c_wchar)
    handle = c.Function.global_alloc(c.Constant.GMEM_MOVEABLE, size)
    if handle:
        buffer = c.Function.global_lock(handle)
        if buffer:
            c.Function.memmove(buffer, text, size)
            _set_clipboard(c.Constant.CF_UNICODETEXT, handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    buffer = 0
    token = c.Type.ULONG_PTR()
    if not c.Function.gdiplus_startup(c.byref(token), c.byref(c.Structure.GdiplusStartupInput()), None):
        bitmap = c.Type.GpBitmap()
        if not c.Function.gdip_create_bitmap_from_file(c.array(c.Type.WCHAR, *path, '\0'), c.byref(bitmap)):
            hbitmap = c.Type.HBITMAP()
            c.Function.gdip_create_HBITMAP_from_bitmap(bitmap, c.byref(hbitmap), 0)
            c.Function.gdip_dispose_image(bitmap)
            if hbitmap:
                bm = c.Structure.BITMAP()
                if c.sizeof(c.Structure.BITMAP) == c.Function.get_object(hbitmap, c.sizeof(c.Structure.BITMAP),
                                                                         c.byref(bm)):
                    size_bi = c.sizeof(c.Structure.BITMAPINFOHEADER)
                    bi = c.Structure.BITMAPINFOHEADER(size_bi, bm.bmWidth, bm.bmHeight, 1,
                                                      bm.bmBitsPixel, c.Constant.BI_RGB)
                    size = bm.bmWidthBytes * bm.bmHeight
                    data = c.array(c.Type.BYTE, size=size)
                    hdc = c.Function.get_DC(None)
                    if c.Function.get_DI_bits(hdc, hbitmap, 0, bi.biHeight, data,
                                              c.cast(c.byref(bi), c.Pointer(c.Structure.BITMAPINFO)),
                                              c.Constant.DIB_RGB_COLORS):
                        handle = c.Function.global_alloc(c.Constant.GMEM_MOVEABLE, size_bi + size)
                        if handle:
                            buffer = c.Function.global_lock(handle)
                            if buffer:
                                c.Function.memmove(buffer, c.byref(bi), size_bi)
                                c.Function.memmove(buffer + size_bi, data, size)
                                _set_clipboard(c.Constant.CF_DIB, handle)
                            c.Function.global_unlock(handle)
                    c.Function.release_DC(None, hdc)
                c.Function.delete_object(hbitmap)
        c.Function.gdiplus_shutdown(token)
    return buffer


def get_wallpaper_path() -> str:
    buffer = _get_buffer(_MAX_PATH)
    c.Function.system_parameters_info(c.Constant.SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, c.Constant.SPIF_NONE)
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            c.Function.system_parameters_info(c.Constant.SPI_SETDESKWALLPAPER, 0,
                                              path, c.Constant.SPIF_SENDWININICHANGE)
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
