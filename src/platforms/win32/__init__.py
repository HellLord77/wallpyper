__version__ = '0.0.13'

import contextlib
import ntpath
import operator
import os
import subprocess
import time
import winreg
from typing import ContextManager, Generator, Iterable, Mapping, Optional, Union

import libs.ctyped as ctyped


def _get_dir(csidl: int) -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.func.shell32.SHGetFolderPathW(None, csidl, None, ctyped.const.SHGFP_TYPE_CURRENT, buff)
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


def _spawn_workerw():
    ctyped.func.user32.SendMessageW(ctyped.func.user32.FindWindowW('Progman', 'Program Manager'), 0x52C, 0, 0)


def _wnd_enum_proc(hwnd: ctyped.type.HWND, lparam: ctyped.type.LPARAM):
    if ctyped.func.user32.FindWindowExW(hwnd, None, 'SHELLDLL_DefView', None) is not None:
        ctyped.type.LPARAM.from_address(lparam).value = ctyped.func.user32.FindWindowExW(None, hwnd,
                                                                                         'WorkerW', None)
    return True


def _get_workerw_hwnd() -> int:
    workkerw = ctyped.type.LPARAM()
    _spawn_workerw()
    ctyped.func.user32.EnumWindows(ctyped.type.WNDENUMPROC(_wnd_enum_proc), ctyped.addressof(workkerw))
    return workkerw.value


@contextlib.contextmanager
def _access_clipboard() -> ContextManager[None]:
    ctyped.func.user32.OpenClipboard(None)
    try:
        yield
    finally:
        ctyped.func.user32.CloseClipboard()


def _set_clipboard(format_: int, hglobal: ctyped.type.HGLOBAL):
    with _access_clipboard():
        ctyped.func.user32.EmptyClipboard()
        ctyped.func.user32.SetClipboardData(format_, hglobal)


@contextlib.contextmanager
def _get_itemidlist(*paths: str) -> ContextManager[tuple[ctyped.Pointer[ctyped.struct.ITEMIDLIST]]]:
    ids = tuple(ctyped.func.shell32.ILCreateFromPath(path) for path in paths)
    try:
        yield ids
    finally:
        for id_ in ids:
            ctyped.func.shell32.ILFree(id_)


@contextlib.contextmanager
def _global_memory(sz: ctyped.type.SIZE_T) -> ContextManager[tuple[ctyped.type.HGLOBAL, ctyped.type.LPVOID]]:
    handle = ctyped.func.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    buff = None
    if handle:
        buff = ctyped.func.kernel32.GlobalLock(handle)
    try:
        yield handle, buff
    finally:
        ctyped.func.kernel32.GlobalUnlock(handle)


@contextlib.contextmanager
def _get_dc(hwnd: Optional[ctyped.type.HWND] = None) -> ContextManager[Optional[ctyped.type.HDC]]:
    hdc = ctyped.func.user32.GetDC(hwnd)
    try:
        yield hdc
    finally:
        ctyped.func.user32.ReleaseDC(hwnd, hdc)


@contextlib.contextmanager
def _get_gp_bitmap(path: str) -> ContextManager[ctyped.type.GpBitmap]:
    token = ctyped.type.ULONG_PTR()
    bitmap = ctyped.type.GpBitmap()
    if ctyped.macro.SUCCEEDED(ctyped.func.GdiPlus.GdiplusStartup(ctyped.byref(
            token), ctyped.byref(ctyped.struct.GdiplusStartupInput()), None)):
        ctyped.func.GdiPlus.GdipCreateBitmapFromFile(ctyped.char_array(path), ctyped.byref(bitmap))
    try:
        yield bitmap
    finally:
        ctyped.func.GdiPlus.GdipDisposeImage(bitmap)
        ctyped.func.GdiPlus.GdiplusShutdown(token)


@contextlib.contextmanager
def _get_hbitmap(path: str) -> ContextManager[ctyped.type.HBITMAP]:
    hbitmap = ctyped.type.HBITMAP()
    with _get_gp_bitmap(path) as gp_bitmap:
        if gp_bitmap:
            ctyped.func.GdiPlus.GdipCreateHBITMAPFromBitmap(gp_bitmap, ctyped.byref(hbitmap), 0)
    try:
        yield hbitmap
    finally:
        ctyped.func.gdi32.DeleteObject(hbitmap)


@contextlib.contextmanager
def _get_hicon(path: str) -> ContextManager[ctyped.type.HICON]:
    hicon = ctyped.type.HICON()
    with _get_gp_bitmap(path) as gp_bitmap:
        if gp_bitmap:
            ctyped.func.GdiPlus.GdipCreateHICONFromBitmap(gp_bitmap, ctyped.byref(hicon))
    try:
        yield hicon
    finally:
        ctyped.func.gdi32.DeleteObject(hicon)


@contextlib.contextmanager
def _load_prop(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
               write: bool = False) -> ContextManager[Optional[ctyped.com.IPropertyStore]]:
    try:
        if isinstance(path_or_interface, str):
            with ctyped.create_com(ctyped.com.IPropertyStore, False) as prop_store:
                ctyped.func.shell32.SHGetPropertyStoreFromParsingName(
                    path_or_interface, None,
                    ctyped.const.GPS_READWRITE if write else ctyped.const.GPS_PREFERQUERYPROPERTIES,
                    *ctyped.macro.IID_PPV_ARGS(prop_store))
                yield prop_store
        else:
            with ctyped.convert_com(ctyped.com.IPropertyStore, path_or_interface) as prop_store:
                yield prop_store
    except OSError:
        yield None


def _get_ex_str_props(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
                      *keys: tuple[str, int]) -> tuple[Optional[str], ...]:
    vals = [None] * len(keys)
    with _load_prop(path_or_interface) as prop:
        if prop:
            var = ctyped.struct.PROPVARIANT()
            for index, key in enumerate(keys):
                var.U.S.U.pwszVal = None
                with contextlib.suppress(OSError):
                    prop.GetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(ctyped.init_guid(
                        key[0], ctyped.struct.GUID), key[1])), ctyped.byref(var))
                vals[index] = var.U.S.U.pwszVal
    return tuple(vals)


def _set_ex_str_props(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
                      props: Mapping[tuple[str, int], str]) -> bool:
    with _load_prop(path_or_interface, True) as prop:
        if prop:
            var = ctyped.struct.PROPVARIANT()
            var.U.S.vt = ctyped.const.VT_LPWSTR
            for key, val in props.items():
                var.U.S.U.pwszVal = val
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


def get_max_shutdown_time() -> float:
    buff = ctyped.type.c_int()
    ctyped.func.user32.SystemParametersInfoW(ctyped.const.SPI_GETWAITTOKILLTIMEOUT, 0, ctyped.byref(buff), 0)
    return buff.value / 1000


def get_monitor_count() -> int:
    num = ctyped.type.c_int()
    ctyped.func.user32.EnumDisplayMonitors(None, None, ctyped.type.MONITORENUMPROC(lambda *_: operator.iadd(num, 1)), 0)
    return num.value


def get_temp_dir() -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.func.kernel32.GetTempPathW(len(_EMPTY), buff)
    return buff.value


def refresh_dir(dir_: str):
    ctyped.func.shell32.SHChangeNotify(ctyped.const.SHCNE_UPDATEDIR, ctyped.const.SHCNF_PATHW, dir_, None)


def press_keyboard(key: int) -> bool:
    input_ = ctyped.struct.INPUT(ctyped.const.INPUT_KEYBOARD, ctyped.union.INPUT_U(ki=ctyped.struct.KEYBDINPUT(key)))
    ref = ctyped.byref(input_)
    sz = ctyped.sizeof(ctyped.struct.INPUT)
    down = ctyped.func.user32.SendInput(1, ref, sz) == 1
    if down:
        input_.U.ki.dwFlags = ctyped.const.KEYEVENTF_KEYUP
        return ctyped.func.user32.SendInput(1, ref, sz) == 1
    return False


def open_file(path: str) -> bool:
    return ctyped.func.shell32.ShellExecuteW(None, None, path, None, None, ctyped.const.SW_SHOW) > 32


def open_file_path(path: str) -> bool:
    with _get_itemidlist(path) as pidl:
        ctyped.func.shell32.SHOpenFolderAndSelectItems(pidl[0], 0, None, 0)
    return True


def select_folder(title: Optional[str] = None, path: Optional[str] = None) -> str:  # TODO dark context menu
    with ctyped.create_com(ctyped.com.IFileDialog) as dialog:
        dialog.SetOptions(ctyped.const.FOS_PICKFOLDERS)
        if path is not None:
            with contextlib.suppress(FileNotFoundError):
                with ctyped.create_com(ctyped.com.IShellItem, False) as item:
                    ctyped.func.shell32.SHCreateItemFromParsingName(path, None, *ctyped.macro.IID_PPV_ARGS(item))
                    dialog.SetFolder(item)
            dialog.SetFileName(path)
        if title is not None:
            dialog.SetTitle(title)
        try:
            dialog.Show(None)
        except OSError:
            return ''
        else:
            buff = ctyped.type.LPWSTR(_EMPTY)
            with ctyped.create_com(ctyped.com.IShellItem, False) as item:
                dialog.GetResult(ctyped.byref(item))
                item.GetDisplayName(ctyped.const.SIGDN_DESKTOPABSOLUTEPARSING, ctyped.byref(buff))
            return buff.value


def paste_text() -> str:
    with _access_clipboard():
        return ctyped.cast(ctyped.func.user32.GetClipboardData(
            ctyped.const.CF_UNICODETEXT), ctyped.type.c_wchar_p).value or ''


def copy_text(text: str, quote: Optional[str] = None) -> bool:
    if quote:
        text = f'{quote}{text}{quote}'
    sz = (ctyped.func.msvcrt.wcslen(text) + 1) * ctyped.sizeof(ctyped.type.c_wchar)
    handle = ctyped.func.kernel32.GlobalAlloc(ctyped.const.GMEM_MOVEABLE, sz)
    if handle:
        buff = ctyped.func.kernel32.GlobalLock(handle)
        if buff:
            ctyped.func.msvcrt.memmove(buff, text, sz)
            _set_clipboard(ctyped.const.CF_UNICODETEXT, handle)
    return text == paste_text()


def copy_image(path: str) -> bool:
    with _get_hbitmap(path) as hbitmap:
        bm = ctyped.struct.BITMAP()
        if (sz_bi := ctyped.sizeof(ctyped.struct.BITMAP)) == ctyped.func.gdi32.GetObjectW(
                hbitmap, sz_bi, ctyped.byref(bm)):
            sz_bih = ctyped.sizeof(ctyped.struct.BITMAPINFOHEADER)
            bi = ctyped.struct.BITMAPINFOHEADER(sz_bih, bm.bmWidth, bm.bmHeight, 1, bm.bmBitsPixel, ctyped.const.BI_RGB)
            sz = bm.bmWidthBytes * bm.bmHeight
            data = ctyped.array(ctyped.type.BYTE, size=sz)
            with _get_dc() as hdc:
                if hdc and ctyped.func.gdi32.GetDIBits(hdc, hbitmap, 0, bi.biHeight, data, ctyped.cast(
                        bi, ctyped.struct.BITMAPINFO), ctyped.const.DIB_RGB_COLORS):
                    with _global_memory(sz_bih + sz) as handle_buff:
                        if handle_buff[1]:
                            ctyped.func.msvcrt.memmove(handle_buff[1], ctyped.byref(bi), sz_bih)
                            ctyped.func.msvcrt.memmove(handle_buff[1] + sz_bih, data, sz)
                            _set_clipboard(ctyped.const.CF_DIB, handle_buff[0])
                            return True
    return False


def get_monitors() -> dict[str, str]:
    monitors = {}
    device = ctyped.struct.DISPLAY_DEVICEW()
    device.cb = ctyped.sizeof(ctyped.struct.DISPLAY_DEVICEW)
    device_i = 0
    while ctyped.func.user32.EnumDisplayDevicesW(None, device_i, ctyped.byref(device), 0):
        device_name = device.DeviceName
        monitor_i = 0
        while ctyped.func.user32.EnumDisplayDevicesW(device_name, monitor_i, ctyped.byref(device), 0):
            print(device)
            monitors[device.DeviceID] = device.DeviceName
            monitor_i += 1
        device_i += 1
    return monitors


def get_monitor_ids() -> tuple[str, ...]:
    ids = []
    with ctyped.create_com(ctyped.com.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            count = ctyped.type.UINT()
            wallpaper.GetMonitorDevicePathCount(ctyped.byref(count))
            buff = ctyped.type.LPWSTR(_EMPTY)
            for index in range(count.value):
                wallpaper.GetMonitorDevicePathAt(index, ctyped.byref(buff))
                ids.append(buff.value)

                rect = ctyped.struct.RECT()
                wallpaper.GetMonitorRECT(buff.value, ctyped.byref(rect))
                hmonitor = ctyped.func.user32.MonitorFromRect(ctyped.byref(rect), ctyped.const.MONITOR_DEFAULTTONULL)
                print(hmonitor)

    return tuple(ids)


def _get_wallpaper_path_param() -> str:
    buff = ctyped.type.LPWSTR(_EMPTY)
    ctyped.func.user32.SystemParametersInfoW(ctyped.const.SPI_GETDESKWALLPAPER, len(_EMPTY), buff, 0)
    return buff.value


def _get_wallpaper_path_iactivedesktop() -> str:
    buff = ctyped.type.PWSTR(_EMPTY)
    with ctyped.create_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            desktop.GetWallpaper(buff, len(_EMPTY), ctyped.const.AD_GETWP_BMP)
    return buff.value


def _get_wallpaper_path_idesktopwallpaper(*monitors: str) -> tuple[str, ...]:
    paths = []
    with ctyped.create_com(ctyped.com.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            buff = ctyped.type.LPWSTR(_EMPTY)
            for monitor in (monitors or get_monitor_ids()):
                wallpaper.GetWallpaper(monitor, ctyped.byref(buff))
                paths.append(buff.value)
    return tuple(paths)


def get_wallpaper_path() -> str:
    return _get_wallpaper_path_param() or _get_wallpaper_path_iactivedesktop()


def _set_wallpaper_param(path: str) -> bool:
    return bool(ctyped.func.user32.SystemParametersInfoW(ctyped.const.SPI_SETDESKWALLPAPER, 0, path,
                                                         ctyped.const.SPIF_SENDWININICHANGE))


def _set_wallpaper_iactivedesktop(path: str) -> bool:
    with ctyped.create_com(ctyped.com.IActiveDesktop) as desktop:
        if desktop:
            _spawn_workerw()
            desktop.SetWallpaper(path, 0)
            desktop.ApplyChanges(ctyped.const.AD_APPLY_ALL)
            return True
    return False


def _set_wallpaper_idesktopwallpaper(path: str, *monitors: str) -> bool:
    with ctyped.create_com(ctyped.com.IDesktopWallpaper) as wallpaper:
        if wallpaper:
            for monitor in monitors:
                wallpaper.SetWallpaper(monitor, path)
            return True
    return False


def set_wallpaper(*paths: str, fade: bool = True, monitors: Optional[Iterable[str]] = None) -> bool:
    for path in paths:
        if ntpath.isfile(path):
            if _set_wallpaper_idesktopwallpaper(path, *monitors) if monitors else _set_wallpaper_iactivedesktop(
                    path) if fade else _set_wallpaper_param(path):
                return True
    return False


def set_slideshow(*paths: str) -> bool:
    with _get_itemidlist(*paths) as pidl:
        id_arr = ctyped.array(ctyped.pointer(ctyped.struct.ITEMIDLIST), *pidl)
        with ctyped.create_com(ctyped.com.IDesktopWallpaper) as wallpaper:
            if wallpaper:
                with ctyped.create_com(ctyped.com.IShellItemArray, False) as shl_arr:
                    ctyped.func.shell32.SHCreateShellItemArrayFromIDLists(
                        len(id_arr), ctyped.byref(id_arr[0]), ctyped.byref(shl_arr))
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
                        with ctyped.create_com(ctyped.com.IShellItem, False) as item:
                            ctyped.func.shell32.SHCreateItemFromParsingName(path, None,
                                                                            *ctyped.macro.IID_PPV_ARGS(item))
                            if item:
                                removed = pinned.RemoveFromList(item) == 0 and removed
            if ntpath.isfile(path):
                removed = ctyped.func.kernel32.DeleteFileW(path) and removed
    return removed


def get_dimensions(hbitmap: ctyped.type.HBITMAP) -> tuple[int, int]:
    bitmap = ctyped.struct.BITMAP()
    ctyped.func.gdi32.GetObjectW(hbitmap, ctyped.sizeof(ctyped.struct.BITMAP), ctyped.byref(bitmap))
    return bitmap.bmWidth, bitmap.bmHeight


def save_hbitmap(hbitmap: ctyped.type.HBITMAP, path: str):
    if hbitmap:
        with ctyped.create_com(ctyped.com.IPicture, False) as picture:
            pict_desc = ctyped.struct.PICTDESC(ctyped.sizeof(ctyped.struct.PICTDESC), ctyped.const.PICTYPE_BITMAP)
            pict_desc.U.bmp.hbitmap = hbitmap
            args = ctyped.macro.IID_PPV_ARGS(picture)
            ctyped.func.oleaut32.OleCreatePictureIndirect(ctyped.byref(pict_desc), args[0], False, args[1])
            with ctyped.convert_com(ctyped.com.IPictureDisp, picture) as picture_disp:
                try:
                    ctyped.func.oleaut32.OleSavePictureFile(picture_disp, path)
                except OSError:
                    pass
                else:
                    return True
    return False
