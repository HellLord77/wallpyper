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
    buffer = libraries.ctype.ctype.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.func.SHGetFolderPathW(None, csidl, None, libraries.ctype.const.SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(libraries.ctype.const.CSIDL_APPDATA)
PICTURES_DIR = _get_dir(libraries.ctype.const.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(libraries.ctype.const.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


@contextlib.contextmanager
def _clipboard() -> ContextManager[None]:
    libraries.ctype.func.OpenClipboard(None)
    try:
        yield
    finally:
        libraries.ctype.func.CloseClipboard()


def paste_text() -> str:
    with _clipboard():
        return libraries.ctype.cast(libraries.ctype.func.GetClipboardData(libraries.ctype.const.CF_UNICODETEXT),
                                    libraries.ctype.ctype.c_wchar_p).value or ''


def _set_clipboard(format_: int,
                   hglobal: libraries.ctype.ctype.HGLOBAL) -> None:
    with _clipboard():
        libraries.ctype.func.EmptyClipboard()
        libraries.ctype.func.SetClipboardData(format_, hglobal)


def copy_text(text: str) -> bool:
    size = (libraries.ctype.func.wcslen(text) + 1) * libraries.ctype.sizeof(libraries.ctype.ctype.c_wchar)
    handle = libraries.ctype.func.GlobalAlloc(libraries.ctype.const.GMEM_MOVEABLE, size)
    if handle:
        buffer = libraries.ctype.func.GlobalLock(handle)
        if buffer:
            libraries.ctype.func.memmove(buffer, text, size)
            _set_clipboard(libraries.ctype.const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _hbitmap(path: str) -> ContextManager[libraries.ctype.ctype.HBITMAP]:
    hbitmap = libraries.ctype.ctype.HBITMAP()
    token = libraries.ctype.ctype.ULONG_PTR()
    if not libraries.ctype.func.GdiplusStartup(libraries.ctype.byref(token), libraries.ctype.byref(
            libraries.ctype.struct.GdiplusStartupInput()), None):
        bitmap = libraries.ctype.ctype.GpBitmap()
        if not libraries.ctype.func.GdipCreateBitmapFromFile(
                libraries.ctype.array(libraries.ctype.ctype.WCHAR, *path, '\0'),
                libraries.ctype.byref(bitmap)):
            libraries.ctype.func.GdipCreateHBITMAPFromBitmap(bitmap, libraries.ctype.byref(hbitmap), 0)
            libraries.ctype.func.GdipDisposeImage(bitmap)
    libraries.ctype.func.GdiplusShutdown(token)
    try:
        yield hbitmap
    finally:
        if hbitmap:
            libraries.ctype.func.DeleteObject(hbitmap)


def copy_image(path: str) -> bool:
    buffer = 0
    with _hbitmap(path) as hbitmap:
        bm = libraries.ctype.struct.BITMAP()
        if libraries.ctype.sizeof(libraries.ctype.struct.BITMAP) == libraries.ctype.func.GetObjectW(
                hbitmap, libraries.ctype.sizeof(libraries.ctype.struct.BITMAP), libraries.ctype.byref(bm)):
            size_bi = libraries.ctype.sizeof(libraries.ctype.struct.BITMAPINFOHEADER)
            bi = libraries.ctype.struct.BITMAPINFOHEADER(size_bi, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel,
                                                         libraries.ctype.const.BI_RGB)
            size = bm.bmWidthBytes * bm.bmHeight
            data = libraries.ctype.array(libraries.ctype.ctype.BYTE, size=size)
            hdc = libraries.ctype.func.GetDC(None)
            if libraries.ctype.func.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data, libraries.ctype.cast(
                    bi, libraries.ctype.struct.BITMAPINFO), libraries.ctype.const.DIB_RGB_COLORS):
                handle = libraries.ctype.func.GlobalAlloc(libraries.ctype.const.GMEM_MOVEABLE, size_bi + size)
                if handle:
                    buffer = libraries.ctype.func.GlobalLock(handle)
                    if buffer:
                        libraries.ctype.func.memmove(buffer, libraries.ctype.byref(bi), size_bi)
                        libraries.ctype.func.memmove(buffer + size_bi, data, size)
                        _set_clipboard(libraries.ctype.const.CF_DIB, handle)
                    libraries.ctype.func.GlobalUnlock(handle)
            libraries.ctype.func.ReleaseDC(None, hdc)
    return bool(buffer)


def get_wallpaper_path() -> str:
    buffer = libraries.ctype.ctype.LPWSTR(' ' * _MAX_PATH)
    libraries.ctype.func.SystemParametersInfoW(libraries.ctype.const.SPI_GETDESKWALLPAPER, _MAX_PATH, buffer, 0)
    return buffer.value or get_wallpaper_path_ex()


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            libraries.ctype.func.SystemParametersInfoW(libraries.ctype.const.SPI_SETDESKWALLPAPER, 0, path,
                                                       libraries.ctype.const.SPIF_SENDWININICHANGE)
            return True
    return False


def get_wallpaper_path_ex() -> str:
    with libraries.ctype.init_com(libraries.ctype.com.IActiveDesktop) as active_desktop:
        buffer = libraries.ctype.ctype.PWSTR(' ' * _MAX_PATH)
        if not active_desktop.GetWallpaper(buffer, _MAX_PATH, libraries.ctype.const.AD_GETWP_BMP):
            return buffer.value
    return get_wallpaper_path()


def set_wallpaper_ex(*paths: str) -> bool:  # TODO: enable and disable slideshow to ensure fade
    with libraries.ctype.init_com(libraries.ctype.com.IActiveDesktop) as active_desktop:
        if active_desktop:
            for path in paths:
                if os.path.isfile(path):
                    active_desktop.SetWallpaper(path, 0)
                    active_desktop.ApplyChanges(libraries.ctype.const.AD_APPLY_ALL)
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
