import os
import shlex
import winreg

import libraries.ctype

_MAX_PATH = 260
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


def _get_dir(csidl: int) -> str:
    buffer = libraries.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.Function.sh_get_folder_path(None, csidl, None, libraries.ctype.Constant.SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


def _get_clipboard(format_: int) -> libraries.ctype.Type.HANDLE:
    libraries.ctype.Function.open_clipboard(None)
    handle = libraries.ctype.Function.get_clipboard_data(format_)
    libraries.ctype.Function.close_clipboard()
    return handle


def _set_clipboard(format_: int,
                   hglobal: int) -> None:
    libraries.ctype.Function.open_clipboard(None)
    libraries.ctype.Function.empty_clipboard()
    libraries.ctype.Function.set_clipboard_data(format_, hglobal)
    libraries.ctype.Function.close_clipboard()


APPDATA_DIR = _get_dir(libraries.ctype.Constant.CSIDL_APPDATA)
PICTURES_DIR = _get_dir(libraries.ctype.Constant.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(libraries.ctype.Constant.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


def paste_text() -> str:
    return libraries.ctype.cast(_get_clipboard(libraries.ctype.Constant.CF_UNICODETEXT),
                                libraries.ctype.Type.c_wchar_p).value or ''


def copy_text(text: str) -> bool:
    size = (libraries.ctype.Function.wcslen(text) + 1) * libraries.ctype.sizeof(libraries.ctype.Type.c_wchar)
    handle = libraries.ctype.Function.global_alloc(libraries.ctype.Constant.GMEM_MOVEABLE, size)
    if handle:
        buffer = libraries.ctype.Function.global_lock(handle)
        if buffer:
            libraries.ctype.Function.memmove(buffer, text, size)
            _set_clipboard(libraries.ctype.Constant.CF_UNICODETEXT, handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    buffer = 0
    token = libraries.ctype.Type.ULONG_PTR()
    if not libraries.ctype.Function.gdiplus_startup(
            libraries.ctype.byref(token), libraries.ctype.byref(libraries.ctype.Structure.GdiplusStartupInput()), None):
        bitmap = libraries.ctype.Type.GpBitmap()
        if not libraries.ctype.Function.gdip_create_bitmap_from_file(
                libraries.ctype.array(libraries.ctype.Type.WCHAR, *path, '\0'), libraries.ctype.byref(bitmap)):
            hbitmap = libraries.ctype.Type.HBITMAP()
            libraries.ctype.Function.gdip_create_HBITMAP_from_bitmap(bitmap, libraries.ctype.byref(hbitmap), 0)
            libraries.ctype.Function.gdip_dispose_image(bitmap)
            if hbitmap:
                bm = libraries.ctype.Structure.BITMAP()
                if libraries.ctype.sizeof(libraries.ctype.Structure.BITMAP) == libraries.ctype.Function.get_object(
                        hbitmap, libraries.ctype.sizeof(libraries.ctype.Structure.BITMAP), libraries.ctype.byref(bm)):
                    size_bi = libraries.ctype.sizeof(libraries.ctype.Structure.BITMAPINFOHEADER)
                    bi = libraries.ctype.Structure.BITMAPINFOHEADER(size_bi, bm.bmWidth, bm.bmHeight, 1,
                                                                    bm.bmBitsPixel, libraries.ctype.Constant.BI_RGB)
                    size = bm.bmWidthBytes * bm.bmHeight
                    data = libraries.ctype.array(libraries.ctype.Type.BYTE, size=size)
                    hdc = libraries.ctype.Function.get_DC(None)
                    if libraries.ctype.Function.get_DI_bits(hdc, hbitmap, 0, bi.biHeight, data, libraries.ctype.cast(
                            libraries.ctype.byref(bi), libraries.ctype.Pointer(libraries.ctype.Structure.BITMAPINFO)),
                                                            libraries.ctype.Constant.DIB_RGB_COLORS):
                        handle = libraries.ctype.Function.global_alloc(libraries.ctype.Constant.GMEM_MOVEABLE,
                                                                       size_bi + size)
                        if handle:
                            buffer = libraries.ctype.Function.global_lock(handle)
                            if buffer:
                                libraries.ctype.Function.memmove(buffer, libraries.ctype.byref(bi), size_bi)
                                libraries.ctype.Function.memmove(buffer + size_bi, data, size)
                                _set_clipboard(libraries.ctype.Constant.CF_DIB, handle)
                            libraries.ctype.Function.global_unlock(handle)
                    libraries.ctype.Function.release_DC(None, hdc)
                libraries.ctype.Function.delete_object(hbitmap)
        libraries.ctype.Function.gdiplus_shutdown(token)
    return bool(buffer)


def get_wallpaper_path() -> str:
    buffer = libraries.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.Function.system_parameters_info(libraries.ctype.Constant.SPI_GETDESKWALLPAPER, _MAX_PATH,
                                                    buffer, libraries.ctype.Constant.SPIF_NONE)
    return buffer.value


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            libraries.ctype.Function.system_parameters_info(libraries.ctype.Constant.SPI_SETDESKWALLPAPER, 0,
                                                            path, libraries.ctype.Constant.SPIF_SENDWININICHANGE)
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
