__version__ = '0.0.12'

import contextlib
import ntpath
import operator
import os
import subprocess
import time
import winreg
from typing import ContextManager, Generator, Mapping, Optional, Union

import libs.ctyped as ctyped


def _get_dir(csidl: int) -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.lib.shell32.SHGetFolderPathW(None, csidl, None, ctyped.const.SHGFP_TYPE_CURRENT, buff)
    return buff.value


_PIN_TIMEOUT = 3
_POLL_TIMEOUT = 0.01
_EMPTY = '\0' * ctyped.const.MAX_PATH
_APPDATA_DIR = _get_dir(ctyped.const.CSIDL_APPDATA)
_STARTUP_DIR = _get_dir(ctyped.const.CSIDL_STARTUP)
_TASKBAR_DIR = ntpath.join(_APPDATA_DIR, 'Microsoft', 'Internet Explorer', 'Quick Launch', 'User Pinned', 'TaskBar')
_STARTUP_KEY = ntpath.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
_SYSPIN_PATH = ntpath.join(ntpath.dirname(__file__), 'syspin.exe')

LINK_EXT = '.lnk'
SAVE_DIR = _APPDATA_DIR
DESKTOP_DIR = _get_dir(ctyped.const.CSIDL_DESKTOP)
PICTURES_DIR = _get_dir(ctyped.const.CSIDL_MYPICTURES)
START_DIR = _get_dir(ctyped.const.CSIDL_PROGRAMS)
WALLPAPER_PATH = ntpath.join(SAVE_DIR, 'Microsoft', 'Windows', 'Themes', 'TranscodedWallpaper')


def get_max_shutdown_time() -> float:
    buff = ctyped.type.c_int()
    ctyped.lib.user32.SystemParametersInfoW(ctyped.const.SPI_GETWAITTOKILLTIMEOUT, 0, ctyped.byref(buff), 0)
    return buff.value / 1000


def get_monitor_count() -> int:
    num = ctyped.type.c_int()
    ctyped.lib.user32.EnumDisplayMonitors(None, None, ctyped.type.MONITORENUMPROC(lambda *_: operator.iadd(num, 1)), 0)
    return num.value


def get_temp_dir() -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.lib.kernel32.GetTempPathW(len(_EMPTY), buff)
    return buff.value


def refresh_dir(dir_: str):
    ctyped.lib.shell32.SHChangeNotify(ctyped.const.SHCNE_UPDATEDIR, ctyped.const.SHCNF_PATHW, dir_, None)


def press_keyboard(key: int) -> bool:
    input_ = ctyped.struct.INPUT(ctyped.const.INPUT_KEYBOARD, ctyped.union.INPUT_u(ki=ctyped.struct.KEYBDINPUT(key)))
    ref = ctyped.byref(input_)
    sz = ctyped.sizeof(ctyped.struct.INPUT)
    down = ctyped.lib.user32.SendInput(1, ref, sz) == 1
    if down:
        input_.u.ki.dwFlags = ctyped.const.KEYEVENTF_KEYUP
        return ctyped.lib.user32.SendInput(1, ref, sz) == 1
    return False


@contextlib.contextmanager
def _clipboard() -> ContextManager[None]:
    ctyped.lib.user32.OpenClipboard(None)
    try:
        yield
    finally:
        ctyped.lib.user32.CloseClipboard()


def paste_text() -> str:
    with _clipboard():
        return ctyped.cast(ctyped.lib.user32.GetClipboardData(
            ctyped.const.CF_UNICODETEXT), ctyped.type.c_wchar_p).value or ''


def _set_clipboard(format_: int, hglobal: ctyped.type.HGLOBAL):
    with _clipboard():
        ctyped.lib.user32.EmptyClipboard()
        ctyped.lib.user32.SetClipboardData(format_, hglobal)


def copy_text(text: str, quote: Optional[str] = None) -> bool:
    if quote:
        text = f'{quote}{text}{quote}'
    sz = (ctyped.lib.msvcrt.wcslen(text) + 1) * ctyped.sizeof(ctyped.type.c_wchar)
    handle = ctyped.lib.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    if handle:
        buff = ctyped.lib.kernel32.GlobalLock(handle)
        if buff:
            ctyped.lib.msvcrt.memmove(buff, text, sz)
            _set_clipboard(ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


@contextlib.contextmanager
def _global_memory(sz: ctyped.type.SIZE_T) -> ContextManager[tuple[ctyped.type.HGLOBAL, ctyped.type.LPVOID]]:
    handle = ctyped.lib.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
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
        if (sz_bi := ctyped.sizeof(ctyped.struct.BITMAP)) == ctyped.lib.gdi32.GetObjectW(hbitmap, sz_bi,
                                                                                         ctyped.byref(bm)):
            sz_bih = ctyped.sizeof(ctyped.struct.BITMAPINFOHEADER)
            bi = ctyped.struct.BITMAPINFOHEADER(sz_bih, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel, ctyped.const.BI_RGB)
            sz = bm.bmWidthBytes * bm.bmHeight
            data = ctyped.array(ctyped.type.BYTE, size=sz)
            with _get_dc() as hdc:
                if hdc and ctyped.lib.gdi32.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data, ctyped.cast(
                        bi, ctyped.struct.BITMAPINFO), ctyped.const.DIB_RGB_COLORS):
                    with _global_memory(sz_bih + sz) as handle_buff:
                        if handle_buff[1]:
                            ctyped.lib.msvcrt.memmove(handle_buff[1], ctyped.byref(bi), sz_bih)
                            ctyped.lib.msvcrt.memmove(handle_buff[1] + sz_bih, data, sz)
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
    if ctyped.lib.shlwapi.PathFileExistsW(path):
        return bool(ctyped.lib.user32.SystemParametersInfoW(ctyped.const.SPI_SETDESKWALLPAPER, 0, path,
                                                            ctyped.const.SPIF_SENDWININICHANGE))
    return False


def _set_wallpaper_com(path: str) -> bool:
    with ctyped.create_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop and ctyped.lib.shlwapi.PathFileExistsW(path):
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
        with ctyped.create_com(ctyped.com.IDesktopWallpaper) as wallpaper:
            if wallpaper:
                with ctyped.create_com(ctyped.com.IShellItemArray, None) as shl_arr:
                    ctyped.lib.shell32.SHCreateShellItemArrayFromIDLists(
                        len(id_arr), ctyped.byref(id_arr[0]), ctyped.byref(shl_arr))
                    if shl_arr:
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


def _register_autorun_link(name: str, path: str, *args: str, show: bool, aumi: Optional[str] = None) -> bool:
    return create_shortcut(ntpath.join(_STARTUP_DIR, f'{name}.{LINK_EXT}'), path, *args, show=show, uid=aumi)


def register_autorun(name: str, path: str, *args: str, show: bool = True, uid: Optional[str] = None) -> bool:
    return unregister_autorun(name, uid) and (
            _register_autorun_link(name, path, *args, show=show, aumi=uid) or _register_autorun_reg(name, path,
                                                                                                    *args))


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


@contextlib.contextmanager
def _load_prop(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW], write: bool = False) -> \
        ContextManager[Optional[ctyped.com.IPropertyStore]]:
    try:
        with ctyped.create_com(
                ctyped.com.IPropertyStore, ctyped.lib.shell32.SHGetPropertyStoreFromParsingName, path_or_interface,
                ctyped.const.GPS_READWRITE if write else ctyped.const.GPS_PREFERQUERYPROPERTIES) if isinstance(
            path_or_interface, str) else ctyped.convert_com(ctyped.com.IPropertyStore,
                                                            path_or_interface) as prop_store:
            yield prop_store
    except OSError:
        yield None


def _get_ex_str_props(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
                      *keys: tuple[str, int]) -> tuple[Optional[str], ...]:
    vals = []
    with _load_prop(path_or_interface) as prop:
        if prop:
            var = ctyped.struct.PROPVARIANT()
            for key in keys:
                try:
                    prop.GetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(ctyped.init_guid(
                        key[0], ctyped.struct.GUID), key[1])), ctyped.byref(var))
                except OSError:
                    var.u.s.u.pwszVal = None
                vals.append(var.u.s.u.pwszVal)
        else:
            vals = [None] * len(keys)
    return tuple(vals)


def _set_ex_str_props(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
                      props: Mapping[tuple[str, int], str]) -> bool:
    with _load_prop(path_or_interface, True) as prop:
        if prop:
            var = ctyped.struct.PROPVARIANT()
            var.u.s.vt = ctyped.const.VT_LPWSTR
            for key, val in props.items():
                var.u.s.u.pwszVal = val
                with contextlib.suppress(OSError):
                    prop.SetValue(
                        ctyped.byref(ctyped.struct.PROPERTYKEY(ctyped.init_guid(key[0], ctyped.struct.GUID), key[1])),
                        ctyped.byref(var))
            with contextlib.suppress(OSError):
                prop.Commit()
        return all(val == val_ for val, val_ in zip(props.values(), _get_ex_str_props(path_or_interface, *props)))


@contextlib.contextmanager
def _load_link(path_or_link: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW]) -> \
        ContextManager[ctyped.com.IShellLinkW]:
    if isinstance(path_or_link, str):
        with ctyped.create_com(ctyped.com.IShellLinkW) as link:
            if link:
                with ctyped.convert_com(ctyped.com.IPersistFile, link) as file:
                    if file:
                        file.Load(path_or_link, ctyped.const.STGM_READ)
            yield link
    else:
        yield path_or_link


def _save_link(link: ctyped.com.IShellLinkW, path: str) -> bool:
    with ctyped.convert_com(ctyped.com.IPersistFile, link) as file:
        try:
            file.Save(path, True)
        except (OSError, PermissionError):
            return False
    refresh_dir(ntpath.dirname(path))
    return ntpath.isfile(path)


def _get_link_data(path_or_link: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW]) -> \
        tuple[str, str, str, str, int, int, tuple[str, int]]:
    data = []
    buff = ctyped.type.LPWSTR(_EMPTY)
    buff_len = len(_EMPTY)
    word = ctyped.type.WORD()
    c_int = ctyped.type.c_int()
    with _load_link(path_or_link) as link:
        link.GetPath(buff, ctyped.const.MAX_PATH, None, ctyped.const.SLGP_RAWPATH)
        data.append(buff.value)
        link.GetDescription(buff, buff_len)
        data.append(buff.value)
        link.GetWorkingDirectory(buff, buff_len)
        data.append(buff.value)
        link.GetArguments(buff, buff_len)
        data.append(buff.value)
        link.GetHotkey(ctyped.byref(word))
        data.append(word.value)
        link.GetShowCmd(ctyped.byref(c_int))
        data.append(c_int.value)
        link.GetIconLocation(buff, buff_len, ctyped.byref(c_int))
        data.append((buff.value, c_int.value))
    # noinspection PyTypeChecker
    return tuple(data)


def _set_link_data(path_or_link: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
                   path: Optional[str] = None, desc: Optional[str] = None, work_dir: Optional[str] = None,
                   args: Optional[str] = None, hotkey: Optional[int] = None,
                   show: Optional[int] = None, icon: Optional[tuple[str, int]] = None) -> bool:
    with _load_link(path_or_link) as link:
        if path is not None:
            link.SetPath(path)
        if desc is not None:
            link.SetDescription(desc)
        if work_dir is not None:
            link.SetWorkingDirectory(work_dir)
        if args is not None:
            link.SetArguments(args)
        if hotkey is not None:
            link.SetHotkey(hotkey)
        if show is not None:
            link.SetShowCmd(show)
        if icon is not None:
            link.SetIconLocation(*icon)
        for data, data_ in zip((path, desc, work_dir, args, hotkey, show, icon), _get_link_data(link)):
            if data is not None and data != data_:
                return False
    return True


def _get_link_paths(dir_: str, recursive: Optional[bool] = None) -> Generator[str, None, None]:
    for dir_entry in os.scandir(dir_):
        if recursive and dir_entry.is_dir():
            for path in _get_link_paths(dir_entry.path):
                yield path
        elif ntpath.splitext(path := ntpath.realpath(dir_entry.path))[1] == LINK_EXT:
            yield path


def create_shortcut(path: str, target: str, *args: str, icon_path: str = '', icon_index: int = 0,
                    comment: Optional[str] = None, start_in: Optional[str] = None, show: bool = True,
                    uid: Optional[str] = None) -> bool:
    with ctyped.create_com(ctyped.com.IShellLinkW) as link:
        if link:
            set_ = _set_link_data(link, target, comment, ntpath.dirname(
                target) if start_in is None else start_in, subprocess.list2cmdline(
                args), show=ctyped.const.SW_SHOWNORMAL if show else ctyped.const.SW_SHOWMINNOACTIVE,
                                  icon=(icon_path, icon_index))
            return set_ and (uid is None or _set_ex_str_props(link, {
                ctyped.const.PKEY_AppUserModel_ID: uid})) and _save_link(link, path)
    return False


def remove_shortcuts(dir_: str, uid: str, rmdir: bool = True) -> bool:
    if uid is None:
        return False
    removed = True
    for path in _get_link_paths(dir_, True):
        if uid == _get_ex_str_props(path, ctyped.const.PKEY_AppUserModel_ID)[0]:
            try:
                os.remove(path)
            except (FileNotFoundError, PermissionError):
                removed = False
            if rmdir and not any(os.scandir(dir__ := ntpath.dirname(path))):
                os.rmdir(dir__)
    return removed


def add_pin(target: str, *args: str, taskbar: bool = True, name: Optional[str] = None,
            icon_path: str = '', icon_index: int = 0, show: bool = True) -> bool:
    if remove_pins(target, *args, taskbar=taskbar):
        if not subprocess.run((_SYSPIN_PATH, target, '5386' if taskbar else '51201'),
                              creationflags=subprocess.DETACHED_PROCESS).returncode:
            if args and not taskbar:
                time.sleep(_PIN_TIMEOUT)
            name_ = ntpath.splitext(ntpath.basename(target))[0]
            if taskbar:
                path_ = ntpath.join(
                    _TASKBAR_DIR,
                    f'{_get_ex_str_props(target, ctyped.const.PKEY_FileDescription)[0] or name_}{LINK_EXT}')
                path = ntpath.join(_TASKBAR_DIR, f'{name}{LINK_EXT}')
            else:
                path_ = ntpath.join(START_DIR, f'{name_}{LINK_EXT}')
                path = ntpath.join(START_DIR, f'{name}{LINK_EXT}')
            os.replace(path_, path)
            if args or icon_path or icon_index or not show:
                with _load_link(path) as link:
                    return _set_link_data(
                        link, args=subprocess.list2cmdline(args),  # FIXME taskbar button requires click to fix (no api)
                        show=ctyped.const.SW_SHOWNORMAL if show else ctyped.const.SW_SHOWMINNOACTIVE,
                        icon=(icon_path, icon_index)) and _save_link(link, path)
            else:
                end = time.time() + _PIN_TIMEOUT
                while (no_pin := not ntpath.isfile(path)) and end > time.time():
                    time.sleep(_POLL_TIMEOUT)
                return not no_pin
    return False


def remove_pins(target: str, *args: str, taskbar: bool = True) -> bool:
    removed = True
    args = subprocess.list2cmdline(args)
    for path in _get_link_paths(_TASKBAR_DIR if taskbar else START_DIR):
        data = _get_link_data(path)
        if target == data[0] and args == data[3]:
            if taskbar:
                with ctyped.create_com(ctyped.com.IStartMenuPinnedList) as pinned:
                    if pinned:
                        with ctyped.create_com(ctyped.com.IShellItem, ctyped.lib.shell32.SHCreateItemFromParsingName,
                                               path, None) as item:
                            if item:
                                removed = pinned.RemoveFromList(item) == 0 and removed
            if ntpath.isfile(path):
                removed = ctyped.lib.kernel32.DeleteFileW(path) and removed
    return removed
