__version__ = '0.0.4'

import contextlib
import os
import shlex
import winreg

import libs.ctype

_MAX_PATH = 32 * 1024
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
_CLSID_ActiveDesktop_ref = libs.ctype.byref(libs.ctype.Struct.CLSID(*libs.ctype.Const.CLSID_ActiveDesktop))
_IID_IActiveDesktop_ref = libs.ctype.byref(libs.ctype.Struct.IID(*libs.ctype.Const.IID_IActiveDesktop))


def _get_dir(csidl: int) -> str:
    buffer = libs.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libs.ctype.Func.SHGetFolderPath(None, csidl, None, libs.ctype.Const.SHGFP_TYPE_CURRENT, buffer)
    return buffer.value


APPDATA_DIR = _get_dir(libs.ctype.Const.CSIDL_APPDATA)
PICTURES_DIR = _get_dir(libs.ctype.Const.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(libs.ctype.Const.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_DIR = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'CachedFiles')


@contextlib.contextmanager
def _clipboard() -> None:
    libs.ctype.Func.OpenClipboard(None)
    try:
        yield
    finally:
        libs.ctype.Func.CloseClipboard()


def paste_text() -> str:
    with _clipboard():
        return libs.ctype.cast(libs.ctype.Func.GetClipboardData(libs.ctype.Const.CF_UNICODETEXT),
                               libs.ctype.Type.c_wchar_p).value or ''


def _set_clipboard(format_: int,
                   hglobal: int) -> None:
    with _clipboard():
        libs.ctype.Func.EmptyClipboard()
        libs.ctype.Func.SetClipboardData(format_, hglobal)


def copy_text(text: str) -> bool:
    size = (libs.ctype.Func.wcslen(text) + 1) * libs.ctype.sizeof(libs.ctype.Type.c_wchar)
    handle = libs.ctype.Func.GlobalAlloc(libs.ctype.Const.GMEM_MOVEABLE, size)
    if handle:
        buffer = libs.ctype.Func.GlobalLock(handle)
        if buffer:
            libs.ctype.Func.memmove(buffer, text, size)
            _set_clipboard(libs.ctype.Const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _hbitmap(path: str) -> libs.ctype.Type.HBITMAP:
    hbitmap = libs.ctype.Type.HBITMAP()
    token = libs.ctype.Type.ULONG_PTR()
    if not libs.ctype.Func.GdiplusStartup(libs.ctype.byref(token),
                                          libs.ctype.byref(libs.ctype.Struct.GdiplusStartupInput()), None):
        bitmap = libs.ctype.Type.GpBitmap()
        if not libs.ctype.Func.GdipCreateBitmapFromFile(libs.ctype.array(libs.ctype.Type.WCHAR, *path, '\0'),
                                                        libs.ctype.byref(bitmap)):
            libs.ctype.Func.GdipCreateHBITMAPFromBitmap(bitmap, libs.ctype.byref(hbitmap), 0)
            libs.ctype.Func.GdipDisposeImage(bitmap)
    libs.ctype.Func.GdiplusShutdown(token)
    try:
        yield hbitmap
    finally:
        if hbitmap:
            libs.ctype.Func.DeleteObject(hbitmap)


def copy_image(path: str) -> bool:
    buffer = 0
    with _hbitmap(path) as hbitmap:
        bm = libs.ctype.Struct.BITMAP()
        if libs.ctype.sizeof(libs.ctype.Struct.BITMAP) == libs.ctype.Func.GetObject(hbitmap, libs.ctype.sizeof(
                libs.ctype.Struct.BITMAP), libs.ctype.byref(bm)):
            size_bi = libs.ctype.sizeof(libs.ctype.Struct.BITMAPINFOHEADER)
            bi = libs.ctype.Struct.BITMAPINFOHEADER(size_bi, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel,
                                                    libs.ctype.Const.BI_RGB)
            size = bm.bmWidthBytes * bm.bmHeight
            data = libs.ctype.array(libs.ctype.Type.BYTE, size=size)
            hdc = libs.ctype.Func.GetDC(None)
            if libs.ctype.Func.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data,
                                         libs.ctype.cast(libs.ctype.byref(bi), libs.ctype.Struct.BITMAPINFO),
                                         libs.ctype.Const.DIB_RGB_COLORS):
                handle = libs.ctype.Func.GlobalAlloc(libs.ctype.Const.GMEM_MOVEABLE, size_bi + size)
                if handle:
                    buffer = libs.ctype.Func.GlobalLock(handle)
                    if buffer:
                        libs.ctype.Func.memmove(buffer, libs.ctype.byref(bi), size_bi)
                        libs.ctype.Func.memmove(buffer + size_bi, data, size)
                        _set_clipboard(libs.ctype.Const.CF_DIB, handle)
                    libs.ctype.Func.GlobalUnlock(handle)
            libs.ctype.Func.ReleaseDC(None, hdc)
    return bool(buffer)


def get_wallpaper_path() -> str:
    buffer = libs.ctype.Type.LPWSTR(' ' * _MAX_PATH)
    libs.ctype.Func.SystemParametersInfo(libs.ctype.Const.SPI_GETDESKWALLPAPER, _MAX_PATH, buffer,
                                         libs.ctype.Const.SPIF_NONE)
    return buffer.value or get_wallpaper_path_ex()


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            libs.ctype.Func.SystemParametersInfo(libs.ctype.Const.SPI_SETDESKWALLPAPER, 0, path,
                                                 libs.ctype.Const.SPIF_SENDWININICHANGE)
            return True
    return False


@contextlib.contextmanager
def _active_desktop() -> libs.ctype.COM.IActiveDesktop:
    active_desktop = libs.ctype.COM.IActiveDesktop()
    libs.ctype.Func.CoInitialize(None)
    try:
        libs.ctype.Func.CoCreateInstance(_CLSID_ActiveDesktop_ref, None, libs.ctype.Const.CLSCTX_INPROC_SERVER,
                                         _IID_IActiveDesktop_ref, libs.ctype.byref(active_desktop))
        yield active_desktop
    finally:
        if active_desktop:
            active_desktop.Release()
        libs.ctype.Func.CoUninitialize()


def get_wallpaper_path_ex() -> str:
    with _active_desktop() as active_desktop:
        buffer = libs.ctype.Type.PWSTR(' ' * _MAX_PATH)
        if not active_desktop.GetWallpaper(buffer, _MAX_PATH, libs.ctype.Const.AD_GETWP_BMP):
            return buffer.value
    return get_wallpaper_path()


def set_wallpaper_ex(*paths: str) -> bool:
    with _active_desktop() as active_desktop:
        if active_desktop:
            for path in paths:
                if os.path.isfile(path):
                    active_desktop.SetWallpaper(path, 0)
                    active_desktop.ApplyChanges(libs.ctype.Const.AD_APPLY_ALL)
                    return True
    return set_wallpaper(*paths)


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
        return value == winreg.QueryValueEx(key, name)[0]


def unregister_autorun(name: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY, access=winreg.KEY_SET_VALUE) as key:
        for _ in range(2):
            try:
                winreg.DeleteValue(key, name)
            except FileNotFoundError:
                return True
    return False
