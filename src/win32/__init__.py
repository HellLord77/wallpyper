__version__ = '0.0.20'

import contextlib
import ntpath
import os
import subprocess
import time
import winreg
from typing import ContextManager, Generator, Mapping, Optional, Union

import libs.ctyped as ctyped
from . import _gdiplus, _utils, clipboard, wallpaper
from ._utils import sanitize_filename

_PIN_TIMEOUT = 3
_POLL_TIMEOUT = 0.01
_APPDATA_DIR = _utils.get_dir(ctyped.const.FOLDERID_RoamingAppData)
_STARTUP_DIR = _utils.get_dir(ctyped.const.FOLDERID_Startup)
_TASKBAR_DIR = ntpath.join(_APPDATA_DIR, 'Microsoft', 'Internet Explorer', 'Quick Launch', 'User Pinned', 'TaskBar')
_STARTUP_KEY = ntpath.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
_SYSPIN_PATH = ntpath.join(ntpath.dirname(__file__), 'syspin.exe')

LINK_EXT = '.lnk'
SAVE_DIR = _APPDATA_DIR
DESKTOP_DIR = _utils.get_dir(ctyped.const.FOLDERID_Desktop)
PICTURES_DIR = _utils.get_dir(ctyped.const.FOLDERID_Pictures)
START_DIR = _utils.get_dir(ctyped.const.FOLDERID_Programs)
WALLPAPER_PATH = ntpath.join(SAVE_DIR, 'Microsoft', 'Windows', 'Themes', 'TranscodedWallpaper')


@contextlib.contextmanager
def _load_prop(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
               write: bool = False) -> ContextManager[Optional[ctyped.com.IPropertyStore]]:
    if isinstance(path_or_interface, str):
        with ctyped.init_com(ctyped.com.IPropertyStore, False) as prop_store:
            flag = (ctyped.enum.GETPROPERTYSTOREFLAGS.GPS_READWRITE
                    if write else ctyped.enum.GETPROPERTYSTOREFLAGS.GPS_PREFERQUERYPROPERTIES)
            if ctyped.macro.SUCCEEDED(ctyped.func.shell32.SHGetPropertyStoreFromParsingName(
                    path_or_interface, None, flag, *ctyped.macro.IID_PPV_ARGS(prop_store))):
                yield prop_store
                return
    else:
        with ctyped.cast_com(path_or_interface, ctyped.com.IPropertyStore) as prop_store:
            yield prop_store
            return
    yield None


def _get_str_ex_props(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
                      *pkeys: tuple[str, int]) -> tuple[Optional[str], ...]:
    vals = []
    with _load_prop(path_or_interface) as prop_store:
        if prop_store:
            var = ctyped.struct.PROPVARIANT()
            var_ref = ctyped.byref(var)
            for key in pkeys:
                with contextlib.suppress(OSError):
                    prop_store.GetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(ctyped.get_guid(key[0]),
                                                                               key[1])), var_ref)
                vals.append(var.U.S.U.pwszVal)
                ctyped.func.ole32.PropVariantClear(var_ref)
    return tuple(vals)


def _set_str_ex_props(path_or_interface: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW],
                      pkeys: Mapping[tuple[str, int], str]) -> bool:
    with _load_prop(path_or_interface, True) as prop_store:
        if prop_store:
            var = ctyped.struct.PROPVARIANT()
            var.U.S.vt = ctyped.enum.VARENUM.VT_LPWSTR.value
            for key, val in pkeys.items():
                var.U.S.U.pwszVal = val
                with contextlib.suppress(OSError):
                    prop_store.SetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(ctyped.get_guid(key[0]),
                                                                               key[1])), ctyped.byref(var))
            with contextlib.suppress(OSError):
                prop_store.Commit()
        return all(val == val_ for val, val_ in zip(pkeys.values(), _get_str_ex_props(path_or_interface, *pkeys)))


@contextlib.contextmanager
def _load_link(path_or_link: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW]) -> \
        ContextManager[ctyped.com.IShellLinkW]:
    if isinstance(path_or_link, str):
        with ctyped.init_com(ctyped.com.IShellLinkW) as link:
            if link:
                with ctyped.cast_com(link, ctyped.com.IPersistFile) as file:
                    if file and ctyped.macro.SUCCEEDED(file.Load(path_or_link, ctyped.const.STGM_READ)):
                        yield link
                        return
        yield None
    else:
        yield path_or_link


def _save_link(link: ctyped.com.IShellLinkW, path: str) -> bool:
    with ctyped.cast_com(link, ctyped.com.IPersistFile) as file:
        try:
            file.Save(path, True)
        except (OSError, PermissionError):
            return False
    refresh_dir(ntpath.dirname(path))
    return ntpath.isfile(path)


def _get_link_data(path_or_link: Union[str, ctyped.com.IShellLinkA, ctyped.com.IShellLinkW]) -> tuple[str, str, str,
                                                                                                      str, int, int,
                                                                                                      tuple[str, int]]:
    data = []
    word = ctyped.type.WORD()
    c_int = ctyped.type.c_int()
    with _utils.string_buffer(ctyped.const.SHRT_MAX) as buff:
        with _load_link(path_or_link) as link:
            link.GetPath(buff, ctyped.const.SHRT_MAX, None, ctyped.enum.SLGP_FLAGS.SLGP_RAWPATH.value)
            data.append(buff.value)
            link.GetDescription(buff, ctyped.const.SHRT_MAX)
            data.append(buff.value)
            link.GetWorkingDirectory(buff, ctyped.const.SHRT_MAX)
            data.append(buff.value)
            link.GetArguments(buff, ctyped.const.SHRT_MAX)
            data.append(buff.value)
            link.GetHotkey(ctyped.byref(word))
            data.append(word.value)
            link.GetShowCmd(ctyped.byref(c_int))
            data.append(c_int.value)
            link.GetIconLocation(buff, ctyped.const.SHRT_MAX, ctyped.byref(c_int))
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


def _get_link_paths(dir_: str, recursive: bool = False) -> Generator[str, None, None]:
    dir_entry: os.DirEntry
    for dir_entry in os.scandir(dir_):
        if recursive and dir_entry.is_dir():
            for path in _get_link_paths(dir_entry.path):
                yield path
        elif ntpath.splitext(path := ntpath.realpath(dir_entry.path))[1] == LINK_EXT:
            yield path


@contextlib.contextmanager
def _get_hdevinfo(guid_ref: Optional[ctyped.Pointer[ctyped.struct.GUID]],
                  flags: ctyped.type.DWORD) -> ContextManager[Optional[ctyped.type.HDEVINFO]]:
    if (hdevinfo := ctyped.func.setupapi.SetupDiGetClassDevsW(guid_ref, None, None,
                                                              flags)) == ctyped.const.INVALID_HANDLE_VALUE:
        yield None
    else:
        try:
            yield hdevinfo
        finally:
            ctyped.func.setupapi.SetupDiDestroyDeviceInfoList(hdevinfo)


def _get_str_dev_prop(hdevinfo: ctyped.type.HDEVINFO, dev_info_ref: ctyped.Pointer[ctyped.struct.SP_DEVINFO_DATA],
                      spdrp_or_devpkey: Union[int, tuple[str, int]]) -> str:
    if isinstance(spdrp_or_devpkey, int):
        getter = ctyped.func.setupapi.SetupDiGetDeviceRegistryPropertyW
        key_ref = spdrp_or_devpkey
        type_ref = None
        flags = ()
    else:
        getter = ctyped.func.setupapi.SetupDiGetDevicePropertyW
        key_ref = ctyped.byref(ctyped.struct.DEVPROPKEY(ctyped.get_guid(spdrp_or_devpkey[0]), spdrp_or_devpkey[1]))
        type_ref = ctyped.byref(ctyped.type.DEVPROPTYPE())
        flags = 0,
    sz = ctyped.type.DWORD()
    getter(hdevinfo, dev_info_ref, key_ref, type_ref, None, 0, ctyped.byref(sz), *flags)
    with _utils.string_buffer(sz.value) as buff:
        getter(hdevinfo, dev_info_ref, key_ref, type_ref, ctyped.cast(buff, ctyped.type.PBYTE), sz, None, *flags)
        return buff.value


def _get_str_devs_props(guid: Optional[str] = None, *devpkeys: Union[int, tuple[str, int]]) -> tuple[tuple[str, ...]]:
    vals = []
    guid_ref = None
    flags = ctyped.const.DIGCF_ALLCLASSES | ctyped.const.DIGCF_PRESENT
    if guid:
        guid_ref = ctyped.byref(ctyped.get_guid(ctyped.const.GUID_DEVCLASS_MONITOR))
        flags = ctyped.const.DIGCF_PRESENT
    with _get_hdevinfo(guid_ref, flags) as hdevinfo:
        if hdevinfo:
            dev_info = ctyped.struct.SP_DEVINFO_DATA(ctyped.sizeof(ctyped.struct.SP_DEVINFO_DATA))
            dev_info_ref = ctyped.byref(dev_info)
            index = 0
            while ctyped.func.setupapi.SetupDiEnumDeviceInfo(hdevinfo, index, dev_info_ref):
                vals.append(tuple(_get_str_dev_prop(hdevinfo, dev_info_ref, devpkey) for devpkey in devpkeys))
                index += 1
    return tuple(vals)


def get_error(hresult: Optional[ctyped.type.HRESULT] = None) -> str:
    with _utils.string_buffer() as buff:
        ctyped.func.kernel32.FormatMessageW((
                ctyped.const.FORMAT_MESSAGE_ALLOCATE_BUFFER |
                ctyped.const.FORMAT_MESSAGE_FROM_SYSTEM | ctyped.const.FORMAT_MESSAGE_IGNORE_INSERTS),
            None, ctyped.func.kernel32.GetLastError() if hresult is None else hresult,
            ctyped.macro.MAKELANGID(ctyped.const.LANG_NEUTRAL, ctyped.const.SUBLANG_DEFAULT),
            ctyped.cast(ctyped.byref(buff), ctyped.type.LPWSTR), 0, None)
        error = buff.value.strip()
    return error


def show_error(title: str, text: str) -> bool:
    return ctyped.func.user32.MessageBoxW(
        None, text, title, ctyped.const.MB_OK | ctyped.const.MB_ICONERROR | ctyped.const.MB_SYSTEMMODAL) != 0


def get_max_shutdown_time() -> float:
    buff = ctyped.type.c_int()
    ctyped.func.user32.SystemParametersInfoW(ctyped.const.SPI_GETWAITTOKILLTIMEOUT, 0, ctyped.byref(buff), 0)
    return buff.value / 1000


# noinspection PyShadowingBuiltins
def refresh_dir(dir: str):
    ctyped.func.shell32.SHChangeNotify(ctyped.const.SHCNE_UPDATEDIR, ctyped.const.SHCNF_PATHW, dir, None)


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
    with _utils.get_itemidlist(path) as pidl:
        return ctyped.macro.SUCCEEDED(ctyped.func.shell32.SHOpenFolderAndSelectItems(pidl[0], 0, None, 0))


def open_file_with(path: str) -> bool:
    info_ref = ctyped.byref(ctyped.struct.OPENASINFO(path, oaifInFlags=(
            ctyped.enum.OPEN_AS_INFO_FLAGS.OAIF_EXEC | ctyped.enum.OPEN_AS_INFO_FLAGS.OAIF_HIDE_REGISTRATION)))
    try:
        return ctyped.const.S_OK == ctyped.func.shell32.SHOpenWithDialog(None, info_ref)
    except OSError as e:
        return e.winerror == ctyped.macro.HRESULT_FROM_WIN32(ctyped.const.ERROR_CANCELLED)


def open_file_with_ex(path: str) -> bool:
    with ctyped.get_winrt(ctyped.com.ILauncherOptions, True) as options:
        if options and ctyped.macro.SUCCEEDED(options.put_DisplayApplicationPicker(True)):
            with ctyped.get_winrt(ctyped.com.ILauncherStatics) as launcher, _utils.open_file(path) as file:
                if launcher and file:
                    operation = ctyped.Async(ctyped.com.IAsyncOperation)
                    if ctyped.macro.SUCCEEDED(launcher.LaunchFileWithOptionsAsync(file, options, operation.get_ref())):
                        return ctyped.enum.AsyncStatus.Completed == operation.wait_for()
    return False


def select_folder(title: Optional[str] = None, path: Optional[str] = None) -> str:  # TODO dark context menu
    with ctyped.init_com(ctyped.com.IFileDialog) as dialog:
        if dialog:
            dialog.SetOptions(ctyped.enum.FILEOPENDIALOGOPTIONS.FOS_PICKFOLDERS)
            if path is not None:
                with ctyped.init_com(ctyped.com.IShellItem, False) as item:
                    try:
                        ctyped.func.shell32.SHCreateItemFromParsingName(path, None, *ctyped.macro.IID_PPV_ARGS(item))
                    except FileNotFoundError:
                        pass
                    except OSError as e:
                        if e.winerror != ctyped.macro.HRESULT_FROM_WIN32(ctyped.const.ERROR_INVALID_PARAMETER):
                            return ''
                    else:
                        dialog.SetFolder(item)
            if title is not None:
                dialog.SetTitle(title)
            try:
                dialog.Show(None)
            except OSError as e:
                if e.winerror == ctyped.macro.HRESULT_FROM_WIN32(ctyped.const.ERROR_CANCELLED):
                    return path
            else:
                with ctyped.init_com(ctyped.com.IShellItem, False) as item:
                    dialog.GetResult(ctyped.byref(item))
                    with _utils.string_buffer() as buff:
                        item.GetDisplayName(ctyped.enum.SIGDN.SIGDN_DESKTOPABSOLUTEPARSING, ctyped.byref(buff))
                        dir_ = buff.value
                    return dir_
    return ''


def _choose_color_hook(hwnd: ctyped.type.HWND, message: ctyped.type.UINT,
                       _: ctyped.type.WPARAM, lparam: ctyped.type.LPARAM) -> ctyped.type.UINT_PTR:
    if message == ctyped.const.WM_INITDIALOG:
        ctyped.func.user32.SetWindowPos(hwnd, ctyped.const.HWND_TOPMOST, 0, 0, 0, 0,
                                        ctyped.const.SWP_NOSIZE | ctyped.const.SWP_NOMOVE)
        title_address = ctyped.struct.CHOOSECOLORW.from_address(lparam).lCustData
        if title_address:
            ctyped.func.user32.SetWindowTextW(hwnd, ctyped.type.LPWSTR.from_address(title_address).value)
    return 0


def choose_color(title: Optional[str] = None, color: Optional[int] = None,
                 custom_colors: Optional[list[int]] = None) -> Optional[int]:
    data = ctyped.type.LPWSTR(title)
    color_chooser = ctyped.struct.CHOOSECOLORW(ctyped.sizeof(
        ctyped.struct.CHOOSECOLORW), rgbResult=0 if color is None else color,
        lpCustColors=ctyped.array(ctyped.type.COLORREF, *(() if custom_colors is None else custom_colors), size=16),
        Flags=ctyped.const.CC_RGBINIT | ctyped.const.CC_FULLOPEN | ctyped.const.CC_ENABLEHOOK,
        lCustData=0 if title is None else ctyped.addressof(data), lpfnHook=ctyped.type.LPCCHOOKPROC(_choose_color_hook))
    if ctyped.func.comdlg32.ChooseColorW(ctyped.byref(color_chooser)):
        color = color_chooser.rgbResult
    if custom_colors is not None:
        custom_colors[:] = color_chooser.lpCustColors[:16]
    return color


def save_hbitmap(hbitmap: ctyped.type.HBITMAP, path: str) -> bool:
    if hbitmap:
        with ctyped.init_com(ctyped.com.IPicture, False) as picture:
            pict_desc = ctyped.struct.PICTDESC(ctyped.sizeof(ctyped.struct.PICTDESC), ctyped.const.PICTYPE_BITMAP)
            pict_desc.U.bmp.hbitmap = hbitmap
            args = ctyped.macro.IID_PPV_ARGS(picture)
            ctyped.func.oleaut32.OleCreatePictureIndirect(ctyped.byref(pict_desc), args[0], False, args[1])
            with ctyped.cast_com(picture, ctyped.com.IPictureDisp) as picture_disp:
                try:
                    ctyped.func.oleaut32.OleSavePictureFile(picture_disp, path)
                except OSError:
                    pass
                else:
                    return True
    return False


def get_direct_show_devices_properties(
        clsid: str, prop_names: tuple[str] = ('DevicePath', 'FriendlyName')) -> tuple[tuple[Optional[str], ...], ...]:
    devices = []
    with ctyped.init_com(ctyped.com.ICreateDevEnum) as dev_enum:
        if dev_enum:
            with ctyped.init_com(ctyped.com.IEnumMoniker, False) as enum_moniker:
                dev_enum.CreateClassEnumerator(ctyped.byref(ctyped.get_guid(clsid)), ctyped.byref(enum_moniker), 0)
                with ctyped.init_com(ctyped.com.IMoniker, False) as moniker:
                    with ctyped.init_com(ctyped.com.IPropertyBag, False) as prop_bag:
                        props = []
                        while enum_moniker.Next(1, ctyped.byref(moniker), 0) == ctyped.const.S_OK:
                            if ctyped.macro.SUCCEEDED(moniker.BindToStorage(None, None,
                                                                            *ctyped.macro.IID_PPV_ARGS(prop_bag))):
                                var = ctyped.struct.VARIANT()
                                var_ref = ctyped.byref(var)
                                props.clear()
                                for prop_name in prop_names:
                                    ctyped.func.oleaut32.VariantInit(var_ref)
                                    with contextlib.suppress(FileNotFoundError):
                                        prop_bag.Read(prop_name, var_ref, None)
                                    props.append(var.U.S.U.bstrVal)
                                    ctyped.func.oleaut32.VariantClear(var_ref)
                                devices.append(tuple(props))
    return tuple(devices)


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
    return create_shortcut(ntpath.join(_STARTUP_DIR, name), path, *args, show=show, uid=aumi)


def register_autorun(name: str, path: str, *args: str, show: bool = True, uid: Optional[str] = None) -> bool:
    return unregister_autorun(name, uid) and (_register_autorun_link(
        name, path, *args, show=show, aumi=uid) or _register_autorun_reg(name, path, *args))


def _unregister_autorun_reg(name: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _STARTUP_KEY, access=winreg.KEY_SET_VALUE) as key:
        return _utils.delete_key(key, name)


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
                    uid: Optional[str] = None, ext: str = LINK_EXT) -> bool:
    with ctyped.init_com(ctyped.com.IShellLinkW) as link:
        if link:
            set_ = _set_link_data(link, target, comment, ntpath.dirname(
                target) if start_in is None else start_in, subprocess.list2cmdline(
                args), show=ctyped.const.SW_SHOWNORMAL if show else ctyped.const.SW_SHOWMINNOACTIVE,
                                  icon=(icon_path, icon_index))
            return set_ and (uid is None or _set_str_ex_props(link, {
                ctyped.const.PKEY_AppUserModel_ID: uid})) and _save_link(link, f'{path}{ext}')
    return False


# noinspection PyShadowingBuiltins
def remove_shortcuts(dir: str, uid: str, rmdir: bool = True) -> bool:
    if uid is None:
        return False
    removed = True
    for path in _get_link_paths(dir, True):
        if uid == _get_str_ex_props(path, ctyped.const.PKEY_AppUserModel_ID)[0]:
            try:
                os.remove(path)
            except (FileNotFoundError, PermissionError):
                removed = False
            if rmdir and not any(os.scandir(dir_ := ntpath.dirname(path))):
                os.rmdir(dir_)
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
                    f'{_get_str_ex_props(target, ctyped.const.PKEY_FileDescription)[0] or name_}{LINK_EXT}')
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
                with ctyped.init_com(ctyped.com.IStartMenuPinnedList) as pinned:
                    if pinned:
                        with ctyped.init_com(ctyped.com.IShellItem, False) as item:
                            ctyped.func.shell32.SHCreateItemFromParsingName(path, None,
                                                                            *ctyped.macro.IID_PPV_ARGS(item))
                            if item:
                                removed = pinned.RemoveFromList(item) == 0 and removed
            if ntpath.isfile(path):
                removed = ctyped.func.kernel32.DeleteFileW(path) and removed
    return removed
