__version__ = '0.0.5'

import contextlib
import os
import shlex
import winreg
from typing import ContextManager

import libraries.ctype

_MAX_PATH = 32 * 1024
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


def _get_dir(csidl: int) -> str:
    buffer = libraries.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.Func.SHGetFolderPathW(None, csidl, None, libraries.ctype.Const.SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(libraries.ctype.Const.CSIDL_APPDATA)
PICTURES_DIR = _get_dir(libraries.ctype.Const.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(libraries.ctype.Const.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


@contextlib.contextmanager
def _clipboard() -> ContextManager[None]:
    libraries.ctype.Func.OpenClipboard(None)
    try:
        yield
    finally:
        libraries.ctype.Func.CloseClipboard()


def paste_text() -> str:
    with _clipboard():
        return libraries.ctype.cast(libraries.ctype.Func.GetClipboardData(libraries.ctype.Const.CF_UNICODETEXT),
                                    libraries.ctype.Type.c_wchar_p).value or ''


def _set_clipboard(format_: int,
                   hglobal: int) -> None:
    with _clipboard():
        libraries.ctype.Func.EmptyClipboard()
        libraries.ctype.Func.SetClipboardData(format_, hglobal)


def copy_text(text: str) -> bool:
    size = (libraries.ctype.Func.wcslen(text) + 1) * libraries.ctype.sizeof(libraries.ctype.Type.c_wchar)
    handle = libraries.ctype.Func.GlobalAlloc(libraries.ctype.Const.GMEM_MOVEABLE, size)
    if handle:
        buffer = libraries.ctype.Func.GlobalLock(handle)
        if buffer:
            libraries.ctype.Func.memmove(buffer, text, size)
            _set_clipboard(libraries.ctype.Const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _hbitmap(path: str) -> ContextManager[libraries.ctype.Type.HBITMAP]:
    hbitmap = libraries.ctype.Type.HBITMAP()
    token = libraries.ctype.Type.ULONG_PTR()
    if not libraries.ctype.Func.GdiplusStartup(libraries.ctype.byref(token),
                                               libraries.ctype.byref(libraries.ctype.Struct.GdiplusStartupInput()),
                                               None):
        bitmap = libraries.ctype.Type.GpBitmap()
        if not libraries.ctype.Func.GdipCreateBitmapFromFile(
                libraries.ctype.array(libraries.ctype.Type.WCHAR, *path, '\0'),
                libraries.ctype.byref(bitmap)):
            libraries.ctype.Func.GdipCreateHBITMAPFromBitmap(bitmap, libraries.ctype.byref(hbitmap), 0)
            libraries.ctype.Func.GdipDisposeImage(bitmap)
    libraries.ctype.Func.GdiplusShutdown(token)
    try:
        yield hbitmap
    finally:
        if hbitmap:
            libraries.ctype.Func.DeleteObject(hbitmap)


def copy_image(path: str) -> bool:
    buffer = 0
    with _hbitmap(path) as hbitmap:
        bm = libraries.ctype.Struct.BITMAP()
        if libraries.ctype.sizeof(libraries.ctype.Struct.BITMAP) == libraries.ctype.Func.GetObjectW(
                hbitmap, libraries.ctype.sizeof(libraries.ctype.Struct.BITMAP), libraries.ctype.byref(bm)):
            size_bi = libraries.ctype.sizeof(libraries.ctype.Struct.BITMAPINFOHEADER)
            bi = libraries.ctype.Struct.BITMAPINFOHEADER(size_bi, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel,
                                                         libraries.ctype.Const.BI_RGB)
            size = bm.bmWidthBytes * bm.bmHeight
            data = libraries.ctype.array(libraries.ctype.Type.BYTE, size=size)
            hdc = libraries.ctype.Func.GetDC(None)
            if libraries.ctype.Func.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data, libraries.ctype.cast(
                    bi, libraries.ctype.Struct.BITMAPINFO), libraries.ctype.Const.DIB_RGB_COLORS):
                handle = libraries.ctype.Func.GlobalAlloc(libraries.ctype.Const.GMEM_MOVEABLE, size_bi + size)
                if handle:
                    buffer = libraries.ctype.Func.GlobalLock(handle)
                    if buffer:
                        libraries.ctype.Func.memmove(buffer, libraries.ctype.byref(bi), size_bi)
                        libraries.ctype.Func.memmove(buffer + size_bi, data, size)
                        _set_clipboard(libraries.ctype.Const.CF_DIB, handle)
                    libraries.ctype.Func.GlobalUnlock(handle)
            libraries.ctype.Func.ReleaseDC(None, hdc)
    return bool(buffer)


def get_wallpaper_path() -> str:
    buffer = libraries.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.Func.SystemParametersInfoW(libraries.ctype.Const.SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, 0)
    return buffer.value or get_wallpaper_path_ex()


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            libraries.ctype.Func.SystemParametersInfoW(libraries.ctype.Const.SPI_SETDESKWALLPAPER, 0, path,
                                                       libraries.ctype.Const.SPIF_SENDWININICHANGE)
            return True
    return False


def get_wallpaper_path_ex() -> str:
    with libraries.ctype.com(libraries.ctype.COM.IActiveDesktop) as active_desktop:
        buffer = libraries.ctype.Type.PWSTR(' ' * _MAX_PATH)
        if not active_desktop.GetWallpaper(buffer, _MAX_PATH, libraries.ctype.Const.AD_GETWP_BMP):
            return buffer.value
    return get_wallpaper_path()


def set_wallpaper_ex(*paths: str) -> bool:  # TODO: enable and disable slideshow to ensure fade
    with libraries.ctype.com(libraries.ctype.COM.IActiveDesktop) as active_desktop:
        if active_desktop:
            for path in paths:
                if os.path.isfile(path):
                    active_desktop.SetWallpaper(path, 0)
                    active_desktop.ApplyChanges(libraries.ctype.Const.AD_APPLY_ALL)
                    return True
    return set_wallpaper(*paths)


def _swap_char(string: str,
               a: str,
               b: str) -> str:
    return ''.join(a if char == b else b if char == a else char for char in string)


def register_autorun(name: str,
                     path: str,
                     *args: str) -> bool:
    if os.path.isfile(path):
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY,
                            access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE) as key:
            value = _swap_char(shlex.join((os.path.realpath(path),) + args), '"', "'")
            try:
                winreg.SetValueEx(key, name, None, winreg.REG_SZ, value)
            except PermissionError:
                return False
            winreg.FlushKey(key)
            return (value, winreg.REG_SZ) == winreg.QueryValueEx(key, name)
    return False


def unregister_autorun(name: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY, access=winreg.KEY_SET_VALUE) as key:
        for _ in range(2):
            try:
                winreg.DeleteValue(key, name)
            except FileNotFoundError:
                return True
    return False
