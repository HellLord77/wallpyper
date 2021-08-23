__version__ = '0.0.5'

import contextlib
import os
import shlex
import winreg
from typing import ContextManager

import libraries.ctyped

_MAX_PATH = 32 * 1024
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')


def _get_dir(csidl: int) -> str:
    buffer = libraries.ctyped.ctype.LPWSTR(' ' * _MAX_PATH)
    libraries.ctyped.func.SHGetFolderPathW(None, csidl, None, libraries.ctyped.const.SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(libraries.ctyped.const.CSIDL_APPDATA)
PICTURES_DIR = _get_dir(libraries.ctyped.const.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(libraries.ctyped.const.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


@contextlib.contextmanager
def _clipboard() -> ContextManager[None]:
    libraries.ctyped.func.OpenClipboard(None)
    try:
        yield
    finally:
        libraries.ctyped.func.CloseClipboard()


def paste_text() -> str:
    with _clipboard():
        return libraries.ctyped.cast(libraries.ctyped.func.GetClipboardData(libraries.ctyped.const.CF_UNICODETEXT),
                                     libraries.ctyped.ctype.c_wchar_p).value or ''


def _set_clipboard(format_: int,
                   hglobal: libraries.ctyped.ctype.HGLOBAL) -> None:
    with _clipboard():
        libraries.ctyped.func.EmptyClipboard()
        libraries.ctyped.func.SetClipboardData(format_, hglobal)


def copy_text(text: str) -> bool:
    size = (libraries.ctyped.func.wcslen(text) + 1) * libraries.ctyped.sizeof(libraries.ctyped.ctype.c_wchar)
    handle = libraries.ctyped.func.GlobalAlloc(libraries.ctyped.const.GMEM_MOVEABLE, size)
    if handle:
        buffer = libraries.ctyped.func.GlobalLock(handle)
        if buffer:
            libraries.ctyped.func.memmove(buffer, text, size)
            _set_clipboard(libraries.ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _hbitmap(path: str) -> ContextManager[libraries.ctyped.ctype.HBITMAP]:
    hbitmap = libraries.ctyped.ctype.HBITMAP()
    token = libraries.ctyped.ctype.ULONG_PTR()
    if not libraries.ctyped.func.GdiplusStartup(libraries.ctyped.byref(token), libraries.ctyped.byref(
            libraries.ctyped.struct.GdiplusStartupInput()), None):
        bitmap = libraries.ctyped.ctype.GpBitmap()
        if not libraries.ctyped.func.GdipCreateBitmapFromFile(
                libraries.ctyped.array(libraries.ctyped.ctype.WCHAR, *path, '\0'),
                libraries.ctyped.byref(bitmap)):
            libraries.ctyped.func.GdipCreateHBITMAPFromBitmap(bitmap, libraries.ctyped.byref(hbitmap), 0)
            libraries.ctyped.func.GdipDisposeImage(bitmap)
    libraries.ctyped.func.GdiplusShutdown(token)
    try:
        yield hbitmap
    finally:
        if hbitmap:
            libraries.ctyped.func.DeleteObject(hbitmap)


def copy_image(path: str) -> bool:
    buffer = 0
    with _hbitmap(path) as hbitmap:
        bm = libraries.ctyped.struct.BITMAP()
        if libraries.ctyped.sizeof(libraries.ctyped.struct.BITMAP) == libraries.ctyped.func.GetObjectW(
                hbitmap, libraries.ctyped.sizeof(libraries.ctyped.struct.BITMAP), libraries.ctyped.byref(bm)):
            size_bi = libraries.ctyped.sizeof(libraries.ctyped.struct.BITMAPINFOHEADER)
            bi = libraries.ctyped.struct.BITMAPINFOHEADER(size_bi, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel,
                                                          libraries.ctyped.const.BI_RGB)
            size = bm.bmWidthBytes * bm.bmHeight
            data = libraries.ctyped.array(libraries.ctyped.ctype.BYTE, size=size)
            hdc = libraries.ctyped.func.GetDC(None)
            if libraries.ctyped.func.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data, libraries.ctyped.cast(
                    bi, libraries.ctyped.struct.BITMAPINFO), libraries.ctyped.const.DIB_RGB_COLORS):
                handle = libraries.ctyped.func.GlobalAlloc(libraries.ctyped.const.GMEM_MOVEABLE, size_bi + size)
                if handle:
                    buffer = libraries.ctyped.func.GlobalLock(handle)
                    if buffer:
                        libraries.ctyped.func.memmove(buffer, libraries.ctyped.byref(bi), size_bi)
                        libraries.ctyped.func.memmove(buffer + size_bi, data, size)
                        _set_clipboard(libraries.ctyped.const.CF_DIB, handle)
                    libraries.ctyped.func.GlobalUnlock(handle)
            libraries.ctyped.func.ReleaseDC(None, hdc)
    return bool(buffer)


def get_wallpaper_path() -> str:
    buffer = libraries.ctyped.ctype.LPWSTR(' ' * _MAX_PATH)
    libraries.ctyped.func.SystemParametersInfoW(libraries.ctyped.const.SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, 0)
    return buffer.value or get_wallpaper_path_ex()


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            libraries.ctyped.func.SystemParametersInfoW(libraries.ctyped.const.SPI_SETDESKWALLPAPER, 0, path,
                                                        libraries.ctyped.const.SPIF_SENDWININICHANGE)
            return True
    return False


def get_wallpaper_path_ex() -> str:
    with libraries.ctyped.init_com(libraries.ctyped.com.IActiveDesktop) as active_desktop:
        buffer = libraries.ctyped.ctype.PWSTR(' ' * _MAX_PATH)
        if not active_desktop.GetWallpaper(buffer, _MAX_PATH, libraries.ctyped.const.AD_GETWP_BMP):
            return buffer.value
    return get_wallpaper_path()


def set_wallpaper_ex(*paths: str) -> bool:  # TODO: enable and disable slideshow to ensure fade
    with libraries.ctyped.init_com(libraries.ctyped.com.IActiveDesktop) as active_desktop:
        if active_desktop:
            for path in paths:
                if os.path.isfile(path):
                    active_desktop.SetWallpaper(path, 0)
                    active_desktop.ApplyChanges(libraries.ctyped.const.AD_APPLY_ALL)
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
