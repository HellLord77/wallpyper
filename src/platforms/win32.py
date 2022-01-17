__version__ = '0.0.11'

import contextlib
import os
import subprocess
import sys
import winreg
from typing import ContextManager, Optional

import libs.ctyped as ctyped


def _get_dir(csidl: int) -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.lib.shell32.SHGetFolderPathW(None, csidl, None, ctyped.const.SHGFP_TYPE_CURRENT, buff)
    return buff.value


_EMPTY = '\0' * ctyped.const.MAX_PATH
_STARTUP_DIR = _get_dir(ctyped.const.CSIDL_STARTUP)
_STARTUP_KEY = os.path.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')

LINK_EXT = 'lnk'
SAVE_DIR = _get_dir(ctyped.const.CSIDL_APPDATA)
DESKTOP_DIR = _get_dir(ctyped.const.CSIDL_DESKTOP)
PICTURES_DIR = _get_dir(ctyped.const.CSIDL_MYPICTURES)
START_DIR = _get_dir(ctyped.const.CSIDL_PROGRAMS)
WALLPAPER_PATH = os.path.join(SAVE_DIR, 'Microsoft', 'Windows', 'Themes', 'TranscodedWallpaper')


def get_max_shutdown_time() -> float:
    buff = ctyped.type.c_int()
    ctyped.lib.user32.SystemParametersInfoW(ctyped.const.SPI_GETWAITTOKILLTIMEOUT, 0, ctyped.byref(buff), 0)
    return buff.value / 1000


def get_temp_dir() -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.lib.kernel32.GetTempPathW(len(_EMPTY), buff)
    return buff.value


@contextlib.contextmanager
def _clipboard() -> ContextManager[None]:
    ctyped.lib.user32.OpenClipboard(None)
    try:
        yield
    finally:
        ctyped.lib.user32.CloseClipboard()


def paste_text() -> str:
    with _clipboard():
        return ctyped.cast(ctyped.lib.user32.GetClipboardData(ctyped.const.CF_UNICODETEXT),
                           ctyped.type.c_wchar_p).value or ''


def _set_clipboard(format_: int, hglobal: ctyped.type.HGLOBAL):
    with _clipboard():
        ctyped.lib.user32.EmptyClipboard()
        ctyped.lib.user32.SetClipboardData(format_, hglobal)


def copy_text(text: str, quote: Optional[str] = None) -> bool:
    if quote:
        text = f'{quote}{text}{quote}'
    size = (ctyped.lib.msvcrt.wcslen(text) + 1) * ctyped.sizeof(ctyped.type.c_wchar)
    handle = ctyped.lib.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, size)
    if handle:
        buff = ctyped.lib.kernel32.GlobalLock(handle)
        if buff:
            ctyped.lib.msvcrt.memmove(buff, text, size)
            _set_clipboard(ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _global_memory(size: ctyped.type.SIZE_T) -> ContextManager[tuple[ctyped.type.HGLOBAL, ctyped.type.LPVOID]]:
    handle = ctyped.lib.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, size)
    buff = None
    if handle:
        buff = ctyped.lib.kernel32.GlobalLock(handle)
    try:
        yield handle, buff
    finally:
        ctyped.lib.kernel32.GlobalUnlock(handle)


@contextlib.contextmanager
def _get_dc(hwnd: Optional[ctyped.type.HWND] = None) -> ContextManager[Optional[ctyped.type.HDC]]:
    hdc = ctyped.lib.user32.GetDC(hwnd)
    try:
        yield hdc
    finally:
        ctyped.lib.user32.ReleaseDC(None, hdc)


@contextlib.contextmanager
def _open_bitmap(path: str) -> ContextManager[ctyped.type.GpBitmap]:
    bitmap = ctyped.type.GpBitmap()
    token = ctyped.type.ULONG_PTR()
    if ctyped.macro.SUCCEEDED(
            ctyped.lib.GdiPlus.GdiplusStartup(ctyped.byref(token), ctyped.byref(ctyped.struct.GdiplusStartupInput()),
                                              None)):
        ctyped.lib.GdiPlus.GdipCreateBitmapFromFile(ctyped.char_array(path), ctyped.byref(bitmap))
    try:
        yield bitmap
    finally:
        ctyped.lib.GdiPlus.GdipDisposeImage(bitmap)
        ctyped.lib.GdiPlus.GdiplusShutdown(token)


@contextlib.contextmanager
def _get_hbitmap(path: str) -> ContextManager[ctyped.type.HBITMAP]:
    hbitmap = ctyped.type.HBITMAP()
    with _open_bitmap(path) as bitmap:
        if bitmap:
            ctyped.lib.GdiPlus.GdipCreateHBITMAPFromBitmap(bitmap, ctyped.byref(hbitmap), 0)
    try:
        yield hbitmap
    finally:
        ctyped.lib.gdi32.DeleteObject(hbitmap)


@contextlib.contextmanager
def _get_hicon(path: str) -> ContextManager[ctyped.type.HICON]:
    hicon = ctyped.type.HICON()
    with _open_bitmap(path) as bitmap:
        if bitmap:
            ctyped.lib.GdiPlus.GdipCreateHICONFromBitmap(bitmap, ctyped.byref(hicon))
    try:
        yield hicon
    finally:
        ctyped.lib.gdi32.DeleteObject(hicon)


def copy_image(path: str) -> bool:
    with _get_hbitmap(path) as hbitmap:
        bm = ctyped.struct.BITMAP()
        if ctyped.sizeof(ctyped.struct.BITMAP) == ctyped.lib.gdi32.GetObjectW(hbitmap,
                                                                              ctyped.sizeof(ctyped.struct.BITMAP),
                                                                              ctyped.byref(bm)):
            sz_bi = ctyped.sizeof(ctyped.struct.BITMAPINFOHEADER)
            bi = ctyped.struct.BITMAPINFOHEADER(sz_bi, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel, ctyped.const.BI_RGB)
            sz = bm.bmWidthBytes * bm.bmHeight
            data = ctyped.array(ctyped.type.BYTE, size=sz)
            with _get_dc() as hdc:
                if hdc and ctyped.lib.gdi32.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data,
                                                      ctyped.cast(bi, ctyped.struct.BITMAPINFO),
                                                      ctyped.const.DIB_RGB_COLORS):
                    with _global_memory(sz_bi + sz) as handle_buff:
                        if handle_buff[1]:
                            ctyped.lib.msvcrt.memmove(handle_buff[1], ctyped.byref(bi), sz_bi)
                            ctyped.lib.msvcrt.memmove(handle_buff[1] + sz_bi, data, sz)
                            _set_clipboard(ctyped.const.CF_DIB, handle_buff[0])
                            return True
    return False


@contextlib.contextmanager
def _get_itemidlist(*paths: str) -> ContextManager[tuple[ctyped.Pointer[ctyped.struct.ITEMIDLIST]]]:
    ids = tuple(ctyped.lib.shell32.ILCreateFromPath(path) for path in paths)
    try:
        yield ids
    finally:
        for id_ in ids:
            ctyped.lib.shell32.ILFree(id_)


def open_file_path(path: str) -> bool:
    with _get_itemidlist(path) as pidl:
        ctyped.lib.shell32.SHOpenFolderAndSelectItems(pidl[0], 0, None, 0)
    return True


def open_file(path: str) -> bool:
    return ctyped.lib.shell32.ShellExecuteW(None, None, path, None, None, ctyped.const.SW_SHOW) > 32


def _get_wallpaper_path_param() -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.lib.user32.SystemParametersInfoW(ctyped.const.SPI_GETDESKWALLPAPER, len(_EMPTY), buff, 0)
    return buff.value


def _get_wallpaper_path_com() -> str:
    buff = ctyped.type.PWSTR(_EMPTY)
    with ctyped.create_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            desktop.GetWallpaper(buff, len(_EMPTY), ctyped.const.AD_GETWP_BMP)
    return buff.value


def get_wallpaper_path() -> str:
    return _get_wallpaper_path_param() or _get_wallpaper_path_com()


def _set_wallpaper_param(path: str) -> bool:
    if ctyped.lib.Shlwapi.PathFileExistsW(path):
        ctyped.lib.user32.SystemParametersInfoW(ctyped.const.SPI_SETDESKWALLPAPER, 0, path,
                                                ctyped.const.SPIF_SENDWININICHANGE)
        return True
    return False


def _set_wallpaper_com(path: str) -> bool:
    with ctyped.create_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            if ctyped.lib.Shlwapi.PathFileExistsW(path):
                ctyped.lib.user32.SendMessageW(ctyped.lib.user32.FindWindowW('Progman', 'Program Manager'), 0x52c, 0, 0)
                desktop.SetWallpaper(path, 0)
                desktop.ApplyChanges(ctyped.const.AD_APPLY_ALL)
                return True
    return False


def set_wallpaper(*paths: str, fade: bool = True) -> bool:
    set_ = False
    if fade:
        for path in paths:
            set_ = set_ or _set_wallpaper_com(path)
    if not set_:
        for path in paths:
            set_ = set_ or _set_wallpaper_param(path)
    return set_


def set_slideshow(*paths: str) -> bool:
    with _get_itemidlist(*paths) as pidl:
        id_arr = ctyped.array(ctyped.pointer(ctyped.struct.ITEMIDLIST), *pidl)
        with ctyped.create_com(ctyped.com.IShellItemArray) as shl_arr:
            ctyped.lib.shell32.SHCreateShellItemArrayFromIDLists(len(id_arr), ctyped.byref(id_arr[0]),
                                                                 ctyped.byref(shl_arr))
            if shl_arr:
                with ctyped.create_com(ctyped.com.IDesktopWallpaper) as wallpaper:
                    if wallpaper:
                        wallpaper.SetSlideshow(shl_arr)
                        return True
    return False


def _register_autorun_reg(name: str, path: str, *args: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _STARTUP_KEY,
                        access=winreg.KEY_QUERY_VALUE | winreg.KEY_SET_VALUE) as key:
        cmd = subprocess.list2cmdline((path,) + args)
        try:
            winreg.SetValueEx(key, name, None, winreg.REG_SZ, cmd)
        except PermissionError:
            return False
        winreg.FlushKey(key)
        return (cmd, winreg.REG_SZ) == winreg.QueryValueEx(key, name)


def _register_autorun_link(name: str, path: str, *args: str, aumi: Optional[str] = None) -> bool:
    return create_shortcut(os.path.join(_STARTUP_DIR, f'{name}.{LINK_EXT}'), path, *args, aumi=aumi)


def register_autorun(name: str, path: str, *args: str, uid: Optional[str] = None) -> bool:
    return _register_autorun_link(name, path, *args, aumi=uid) or _register_autorun_reg(name, path, *args)


def _unregister_autorun_reg(name: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _STARTUP_KEY, access=winreg.KEY_SET_VALUE) as key:
        for _ in range(2):
            try:
                winreg.DeleteValue(key, name)
            except FileNotFoundError:
                return True
    return False


def _unregister_autorun_link(aumi: str) -> bool:
    return remove_shortcuts(_STARTUP_DIR, aumi)


def unregister_autorun(name: Optional[str] = None, uid: Optional[str] = None) -> bool:
    unregistered = False
    if name:
        unregistered = _unregister_autorun_reg(name)
    if uid:
        unregistered = _unregister_autorun_link(uid) and unregistered
    return unregistered


def _get_link_data(path: str) -> tuple[str, str, str, str, tuple[str, int], str]:
    with ctyped.create_com(ctyped.com.IShellLinkW) as link:
        with ctyped.convert_com(link, ctyped.com.IPersistFile) as file:
            file.Load(path, ctyped.const.STGM_READ)
        target = ctyped.type.LPWSTR(_EMPTY)
        args = ctyped.type.LPWSTR(_EMPTY)
        start_in = ctyped.type.LPWSTR(_EMPTY)
        comment = ctyped.type.LPWSTR(_EMPTY)
        icon = ctyped.type.LPWSTR(_EMPTY), ctyped.type.c_int()
        link.GetPath(target, ctyped.const.MAX_PATH, None, ctyped.const.SLGP_RAWPATH)
        link.GetArguments(args, ctyped.const.MAX_PATH)
        link.GetWorkingDirectory(start_in, ctyped.const.MAX_PATH)
        link.GetDescription(comment, ctyped.const.MAX_PATH)
        link.GetIconLocation(icon[0], ctyped.const.MAX_PATH, ctyped.byref(icon[1]))
        with ctyped.convert_com(link, ctyped.com.IPropertyStore) as properties:
            property_ = ctyped.struct.PROPVARIANT()
            properties.GetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(
                ctyped.init_guid(ctyped.const.PKEY_AppUserModel_ID[0], ctyped.struct.GUID),
                ctyped.const.PKEY_AppUserModel_ID[1])), ctyped.byref(property_))
            aumi = property_.u.s.u.pwszVal
        return target.value, args.value, start_in.value, comment.value, (icon[0].value, icon[1].value), aumi


def _refresh_dir(path: str):
    ctyped.lib.shell32.SHChangeNotify(ctyped.const.SHCNE_UPDATEDIR, ctyped.const.SHCNF_PATHW, path, None)


def create_shortcut(path: str, target: str, *args: str, start_in: Optional[str] = None,
                    comment: Optional[str] = None, icon_path: Optional[str] = None,
                    icon_index: Optional[int] = None, aumi: Optional[str] = None) -> bool:
    args = subprocess.list2cmdline(args)
    start_in = start_in or os.path.dirname(target)
    with ctyped.create_com(ctyped.com.IShellLinkW) as link:
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
        if aumi is not None:
            with ctyped.convert_com(link, ctyped.com.IPropertyStore) as properties:
                property_ = ctyped.struct.PROPVARIANT()
                property_.u.s.vt = ctyped.const.VT_LPWSTR
                property_.u.s.u.pwszVal = aumi
                properties.SetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(
                    ctyped.init_guid(ctyped.const.PKEY_AppUserModel_ID[0], ctyped.struct.GUID),
                    ctyped.const.PKEY_AppUserModel_ID[1])), ctyped.byref(property_))
        with ctyped.convert_com(link, ctyped.com.IPersistFile) as file:
            with contextlib.suppress(PermissionError):
                file.Save(path, True)
        _refresh_dir(os.path.dirname(path))
        return ctyped.lib.Shlwapi.PathFileExistsW(path) and (
            target, args, start_in, comment, icon, aumi) == _get_link_data(path)


def remove_shortcuts(dir_: str, uid: str) -> bool:
    removed = True
    for dir__ in os.scandir(dir_):
        # noinspection PyUnresolvedReferences
        path = os.path.realpath(dir__.path)
        if path.endswith(f'.{LINK_EXT}'):
            try:
                aumi = _get_link_data(path)[-1]
            except OSError:
                removed = False
            else:
                if aumi == uid:
                    removed = ctyped.lib.kernel32.DeleteFileW(path) and removed
    return removed
