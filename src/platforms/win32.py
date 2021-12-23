__version__ = '0.0.8'

import atexit
import contextlib
import os
import subprocess
import sys
import winreg
from typing import ContextManager, Optional

import libs.ctyped as ctyped

_EMPTY = '\0' * ctyped.const.MAX_PATH
_RUN_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
_BALLOON = ctyped.struct.NOTIFYICONDATA(ctyped.sizeof(ctyped.struct.NOTIFYICONDATA), uID=hash(object()),
                                        uFlags=ctyped.const.NIF_INFO)
atexit.register(ctyped.func.Shell_NotifyIcon, ctyped.const.NIM_DELETE, ctyped.byref(_BALLOON))


def _get_dir(csidl: int) -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.func.SHGetFolderPath(None, csidl, None, ctyped.const.SHGFP_TYPE_CURRENT, buff)
    return buff.value


APPDATA_DIR = _get_dir(ctyped.const.CSIDL_APPDATA)
DESKTOP_DIR = _get_dir(ctyped.const.CSIDL_DESKTOP)
PICTURES_DIR = _get_dir(ctyped.const.CSIDL_MYPICTURES)
TEMP_DIR = os.path.join(_get_dir(ctyped.const.CSIDL_LOCAL_APPDATA), 'Temp')
WALLPAPER_PATH = os.path.join(APPDATA_DIR, 'Microsoft', 'Windows', 'Themes', 'TranscodedWallpaper')


@contextlib.contextmanager
def _clipboard() -> ContextManager[None]:
    ctyped.func.OpenClipboard(None)
    try:
        yield
    finally:
        ctyped.func.CloseClipboard()


def paste_text() -> str:
    with _clipboard():
        return ctyped.cast(ctyped.func.GetClipboardData(ctyped.const.CF_UNICODETEXT), ctyped.type.c_wchar_p).value or ''


def _set_clipboard(format_: int, hglobal: ctyped.type.HGLOBAL) -> None:
    with _clipboard():
        ctyped.func.EmptyClipboard()
        ctyped.func.SetClipboardData(format_, hglobal)


def copy_text(text: str, quote: Optional[str] = None) -> bool:
    if quote:
        text = f'{quote}{text}{quote}'
    size = (ctyped.func.wcslen(text) + 1) * ctyped.sizeof(ctyped.type.c_wchar)
    handle = ctyped.func.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, size)
    if handle:
        buff = ctyped.func.GlobalLock(handle)
        if buff:
            ctyped.func.memmove(buff, text, size)
            _set_clipboard(ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _global_memory(size: ctyped.type.SIZE_T) -> ContextManager[tuple[ctyped.type.HGLOBAL, ctyped.type.LPVOID]]:
    handle = ctyped.func.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, size)
    buff = None
    if handle:
        buff = ctyped.func.GlobalLock(handle)
    try:
        yield handle, buff
    finally:
        ctyped.func.GlobalUnlock(handle)


@contextlib.contextmanager
def _get_dc(hwnd: Optional[ctyped.type.HWND] = None) -> ContextManager[Optional[ctyped.type.HDC]]:
    hdc = ctyped.func.GetDC(hwnd)
    try:
        yield hdc
    finally:
        ctyped.func.ReleaseDC(None, hdc)


@contextlib.contextmanager
def _open_bitmap(path: str) -> ContextManager[ctyped.type.GpBitmap]:
    bitmap = ctyped.type.GpBitmap()
    token = ctyped.type.ULONG_PTR()
    if ctyped.macro.SUCCEEDED(
            ctyped.func.GdiplusStartup(ctyped.byref(token), ctyped.byref(ctyped.struct.GdiplusStartupInput()), None)):
        ctyped.func.GdipCreateBitmapFromFile(ctyped.char_array(path), ctyped.byref(bitmap))
    try:
        yield bitmap
    finally:
        ctyped.func.GdipDisposeImage(bitmap)
        ctyped.func.GdiplusShutdown(token)


@contextlib.contextmanager
def _get_hbitmap(path: str) -> ContextManager[ctyped.type.HBITMAP]:
    hbitmap = ctyped.type.HBITMAP()
    with _open_bitmap(path) as bitmap:
        if bitmap:
            ctyped.func.GdipCreateHBITMAPFromBitmap(bitmap, ctyped.byref(hbitmap), 0)
    try:
        yield hbitmap
    finally:
        ctyped.func.DeleteObject(hbitmap)


@contextlib.contextmanager
def _get_hicon(path: str) -> ContextManager[ctyped.type.HICON]:
    hicon = ctyped.type.HICON()
    with _open_bitmap(path) as bitmap:
        if bitmap:
            ctyped.func.GdipCreateHICONFromBitmap(bitmap, ctyped.byref(hicon))
    try:
        yield hicon
    finally:
        ctyped.func.DeleteObject(hicon)


def copy_image(path: str) -> bool:
    with _get_hbitmap(path) as hbitmap:
        bm = ctyped.struct.BITMAP()
        if ctyped.sizeof(ctyped.struct.BITMAP) == ctyped.func.GetObject(hbitmap, ctyped.sizeof(ctyped.struct.BITMAP),
                                                                        ctyped.byref(bm)):
            sz_bi = ctyped.sizeof(ctyped.struct.BITMAPINFOHEADER)
            bi = ctyped.struct.BITMAPINFOHEADER(sz_bi, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel, ctyped.const.BI_RGB)
            sz = bm.bmWidthBytes * bm.bmHeight
            data = ctyped.array(ctyped.type.BYTE, size=sz)
            with _get_dc() as hdc:
                if hdc:
                    if ctyped.func.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data,
                                             ctyped.cast(bi, ctyped.struct.BITMAPINFO), ctyped.const.DIB_RGB_COLORS):
                        with _global_memory(sz_bi + sz) as handle_buff:
                            if handle_buff[1]:
                                ctyped.func.memmove(handle_buff[1], ctyped.byref(bi), sz_bi)
                                ctyped.func.memmove(handle_buff[1] + sz_bi, data, sz)
                                _set_clipboard(ctyped.const.CF_DIB, handle_buff[0])
                                return True
    return False


@contextlib.contextmanager
def _get_itemidlist(*paths: str) -> ContextManager[tuple[ctyped.Pointer[ctyped.struct.ITEMIDLIST]]]:
    ids = tuple(ctyped.func.ILCreateFromPath(path) for path in paths)
    try:
        yield ids
    finally:
        for id_ in ids:
            ctyped.func.ILFree(id_)


def open_file_path(path: str) -> bool:
    with _get_itemidlist(path) as pidl:
        ctyped.func.SHOpenFolderAndSelectItems(pidl[0], 0, None, 0)
    return True


def open_file(path: str) -> bool:
    return ctyped.func.ShellExecute(None, None, path, None, None, ctyped.const.SW_SHOW) > 32


def get_wallpaper_path() -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.func.SystemParametersInfo(ctyped.const.SPI_GETDESKWALLPAPER, ctyped.const.MAX_PATH, buff, 0)
    return buff.value or get_wallpaper_path_ex()


def set_wallpaper(*paths: str) -> bool:
    for path in paths:
        if os.path.isfile(path):
            ctyped.func.SystemParametersInfo(ctyped.const.SPI_SETDESKWALLPAPER, 0, path,
                                             ctyped.const.SPIF_SENDWININICHANGE)
            return True
    return False


def set_slideshow(*paths: str) -> bool:
    with _get_itemidlist(*paths) as pidl:
        id_arr = ctyped.array(ctyped.pointer(ctyped.struct.ITEMIDLIST), *pidl)
        with ctyped.create_com(ctyped.com.IShellItemArray) as shl_arr:
            ctyped.func.SHCreateShellItemArrayFromIDLists(len(id_arr), ctyped.byref(id_arr[0]), ctyped.byref(shl_arr))
            if shl_arr:
                with ctyped.create_com(ctyped.com.IDesktopWallpaper) as wallpaper:
                    if wallpaper:
                        wallpaper.SetSlideshow(shl_arr)
                        return True
    return False


def get_wallpaper_path_ex() -> str:
    with ctyped.create_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            buff = ctyped.type.PWSTR(_EMPTY)
            if ctyped.macro.SUCCEEDED(desktop.GetWallpaper(buff, ctyped.const.MAX_PATH, ctyped.const.AD_GETWP_BMP)):
                return buff.value
    return get_wallpaper_path()


def set_wallpaper_ex(*paths: str) -> bool:
    with ctyped.create_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            for path in paths:
                if os.path.isfile(path):
                    ctyped.func.SendMessage(ctyped.func.FindWindow('Progman', 'Program Manager'), 0x52c, 0, 0)
                    desktop.SetWallpaper(path, 0)
                    desktop.ApplyChanges(ctyped.const.AD_APPLY_ALL)
                    return True
    return set_wallpaper(*paths)


def register_autorun(name: str, path: str, *args: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY,
                        access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE) as key:
        command = subprocess.list2cmdline((path,) + args)
        try:
            winreg.SetValueEx(key, name, None, winreg.REG_SZ, command)
        except PermissionError:
            return False
        winreg.FlushKey(key)
        return (command, winreg.REG_SZ) == winreg.QueryValueEx(key, name)


def unregister_autorun(name: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _RUN_KEY, access=winreg.KEY_SET_VALUE) as key:
        for _ in range(2):
            try:
                winreg.DeleteValue(key, name)
            except FileNotFoundError:
                return True
    return False


def _get_link_data(path: str) -> tuple[str, str, str, str, tuple[str, int]]:
    with ctyped.create_com(ctyped.com.IShellLinkW) as link:
        with ctyped.convert_com(link, ctyped.com.IPersistFile) as file:
            file.Load(path, ctyped.const.STGM_READ)
        target = ctyped.type.LPWSTR(_EMPTY)
        args = ctyped.type.LPWSTR(_EMPTY)
        start_in = ctyped.type.LPWSTR(_EMPTY)
        comment = ctyped.type.LPWSTR(_EMPTY)
        icon = ctyped.type.LPWSTR(_EMPTY), ctyped.type.c_int()
        link.GetPath(target, ctyped.const.MAX_PATH, None, ctyped.const.SLGP_SHORTPATH)
        link.GetArguments(args, ctyped.const.MAX_PATH)
        link.GetWorkingDirectory(start_in, ctyped.const.MAX_PATH)
        link.GetDescription(comment, ctyped.const.MAX_PATH)
        link.GetIconLocation(icon[0], ctyped.const.MAX_PATH, ctyped.byref(icon[1]))
        return target.value, args.value, start_in.value, comment.value, (icon[0].value, icon[1].value)


def create_link(path: str, target: str, *args: str, start_in: Optional[str] = None, comment: Optional[str] = None,
                icon_path: Optional[str] = None, icon_index: Optional[int] = None) -> bool:
    args = subprocess.list2cmdline(args)
    start_in = start_in or os.path.dirname(target)
    with ctyped.create_com(ctyped.com.IShellLink) as link:
        link.SetPath(target)
        link.SetArguments(args)
        link.SetWorkingDirectory(start_in)
        if comment:
            link.SetDescription(comment)
        else:
            comment = ''
        if icon_path or icon_index:
            icon = icon_path or sys.executable, icon_index or 0
            link.SetIconLocation(*icon)
        else:
            icon = '', 0
        with ctyped.convert_com(link, ctyped.com.IPersistFile) as file:
            file.Save(path, True)
        return os.path.isfile(path) and (target, args, start_in, comment, icon) == _get_link_data(path)


def show_balloon(title: str, text: str, icon: Optional[str] = None) -> bool:
    _BALLOON.szInfo = text
    _BALLOON.szInfoTitle = title
    _BALLOON.dwInfoFlags = icon or 0
    return ctyped.func.Shell_NotifyIcon(ctyped.const.NIM_MODIFY,
                                        ctyped.byref(_BALLOON)) or ctyped.func.Shell_NotifyIcon(ctyped.const.NIM_ADD,
                                                                                                ctyped.byref(_BALLOON))
