__version__ = '0.1.2'

import contextlib
import enum
import ntpath
import os
import subprocess
import time
import winreg
from typing import ContextManager, Iterator, Mapping, Optional

from libs import ctyped
from libs.ctyped import winrt
from libs.ctyped.const import error, runtimeclass
from libs.ctyped.interface.um import oaidl, objidl, ocidl, propsys, ShObjIdl, ShObjIdl_core, strmif
from libs.ctyped.interface.winrt.Windows import System as Windows_System
from libs.ctyped.lib import kernel32, user32, uxtheme, shell32, ole32, ntdll, oleaut32, setupapi
from . import _gdiplus, _utils, clipboard, console, dialog, display, gui, window
from ._utils import sanitize_filename

_PIN_TIMEOUT = 3
_APPDATA_DIR = _utils.get_dir(ctyped.const.FOLDERID_RoamingAppData)
_STARTUP_DIR = _utils.get_dir(ctyped.const.FOLDERID_Startup)
_TASKBAR_DIR = ntpath.join(_APPDATA_DIR, 'Microsoft', 'Internet Explorer', 'Quick Launch', 'User Pinned', 'TaskBar')
_STARTUP_KEY = ntpath.join('SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Run')
_SYS_PIN_PATH = ntpath.join(ntpath.dirname(__file__), 'syspin.exe')

LINK_EXT = '.lnk'
SAVE_DIR = _APPDATA_DIR
DESKTOP_DIR = _utils.get_dir(ctyped.const.FOLDERID_Desktop)
PICTURES_DIR = _utils.get_dir(ctyped.const.FOLDERID_Pictures)
START_DIR = _utils.get_dir(ctyped.const.FOLDERID_Programs)

_MESSAGES = None


class ColorMode(enum.IntEnum):
    DEFAULT = ctyped.enum.PreferredAppMode.Default
    AUTO = ctyped.enum.PreferredAppMode.AllowDark
    LIGHT = ctyped.enum.PreferredAppMode.ForceLight
    DARK = ctyped.enum.PreferredAppMode.ForceDark


class FocusAssistState(enum.IntEnum):
    NOT_SUPPORTED = -2
    FAILED = -1
    OFF = 0
    PRIORITY_ONLY = 1
    ALARMS_ONLY = 2


is_valid_image = _gdiplus.image_is_valid


def get_colored_bitmap(r: int, g: int, b: int, width: int = 32, height: int = 32) -> _gdiplus.Bitmap:
    return _gdiplus.bitmap_from_color(_gdiplus.Color.from_rgba(r, g, b), width, height)


def set_color_mode(mode: int | str | ColorMode = ColorMode.DEFAULT, flush: bool = True):
    if isinstance(mode, str):
        mode = ColorMode[mode.upper()]
    if isinstance(mode, ColorMode):
        mode = mode.value
    # noinspection PyTypeChecker
    uxtheme.SetPreferredAppMode(mode)
    if flush:
        uxtheme.FlushMenuThemes()


def get_focus_assist_state() -> FocusAssistState:
    buffer = ctyped.type.DWORD()
    focus_assist = ctyped.struct.WNF_STATE_NAME(ctyped.array(0xA3BF1C75, 0xD83063E, type=ctyped.type.ULONG))
    if ctyped.macro.NT_SUCCESS(ntdll.NtQueryWnfStateData(ctyped.byref(focus_assist), None, None, ctyped.byref(
            ctyped.type.WNF_CHANGE_STAMP()), ctyped.byref(buffer), ctyped.byref(ctyped.type.ULONG(ctyped.sizeof(buffer))))):
        return FocusAssistState(buffer.value)
    else:
        return FocusAssistState.FAILED


def get_short_path(path: str) -> str:
    size = kernel32.GetShortPathNameW(path, None, 0)
    if size:
        with _utils.string_buffer(size) as buff:
            if kernel32.GetShortPathNameW(path, buff, size):
                return buff.value
    return path


@contextlib.contextmanager
def _load_prop(path_or_link: str | ShObjIdl_core.IShellLinkW,
               write: bool = False) -> ContextManager[Optional[propsys.IPropertyStore]]:
    if isinstance(path_or_link, str):
        with ctyped.interface.COM[propsys.IPropertyStore]() as prop_store:
            if ctyped.macro.SUCCEEDED(shell32.SHGetPropertyStoreFromParsingName(
                    path_or_link, None, ctyped.enum.GETPROPERTYSTOREFLAGS.READWRITE
                    if write else ctyped.enum.GETPROPERTYSTOREFLAGS.PREFERQUERYPROPERTIES,
                    *ctyped.macro.IID_PPV_ARGS(prop_store))):
                yield prop_store
                return
    else:
        with ctyped.interface.COM[propsys.IPropertyStore](path_or_link) as prop_store:
            yield prop_store
            return
    yield


def get_shortcut_properties(path_or_link: str | ShObjIdl_core.IShellLinkW,
                            *pkeys: tuple[str, int]) -> tuple[Optional[str], ...]:
    vals = []
    with _load_prop(path_or_link) as prop_store:
        if prop_store:
            var = ctyped.struct.PROPVARIANT()
            var_ref = ctyped.byref(var)
            for key in pkeys:
                prop_store.GetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(
                    ctyped.get_guid(key[0]), key[1])), var_ref)
                vals.append(var.U.S.U.pwszVal)
                ole32.PropVariantClear(var_ref)
    return tuple(vals)


def set_shortcut_properties(path_or_link: str | ShObjIdl_core.IShellLinkW, pkeys: Mapping[tuple[str, int], str]) -> bool:
    with _load_prop(path_or_link, True) as prop_store:
        if prop_store:
            var = ctyped.struct.PROPVARIANT()
            var.U.S.vt = ctyped.enum.VARENUM.LPWSTR.value
            for key, val in pkeys.items():
                var.U.S.U.pwszVal = val
                prop_store.SetValue(ctyped.byref(ctyped.struct.PROPERTYKEY(
                    ctyped.get_guid(key[0]), key[1])), ctyped.byref(var))
            prop_store.Commit()
    return all(val == val_ for val, val_ in zip(pkeys.values(), get_shortcut_properties(path_or_link, *pkeys)))


@contextlib.contextmanager
def _load_link(path_or_link: str | ShObjIdl_core.IShellLinkW) -> ContextManager[ShObjIdl_core.IShellLinkW]:
    if isinstance(path_or_link, str):
        with ctyped.interface.COM[ShObjIdl_core.IShellLinkW](ctyped.const.CLSID_ShellLink) as link:
            if link:
                with ctyped.interface.COM[objidl.IPersistFile](link) as file:
                    if file and ctyped.macro.SUCCEEDED(file.Load(path_or_link, ctyped.const.STGM_READ)):
                        yield link
                        return
        yield
    else:
        yield path_or_link


def _save_link(link: ShObjIdl_core.IShellLinkW, path: str) -> bool:
    with ctyped.interface.COM[objidl.IPersistFile](link) as file:
        file.Save(path, True)
    refresh_dir(ntpath.dirname(path))
    return ntpath.isfile(path)


def _get_link_data(path_or_link: str | ShObjIdl_core.IShellLinkW) -> \
        tuple[str, str, str, str, int, int, tuple[str, int]]:
    data = []
    word = ctyped.type.WORD()
    c_int = ctyped.type.c_int()
    with _utils.string_buffer(ctyped.const.SHRT_MAX) as buff:
        with _load_link(path_or_link) as link:
            link.GetPath(buff, ctyped.const.SHRT_MAX, ctyped.NULLPTR, ctyped.enum.SLGP_FLAGS.RAWPATH.value)
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


def _set_link_data(path_or_link: str | ShObjIdl_core.IShellLinkW,
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


def _get_link_paths(dir_: str, recursive: bool = False) -> Iterator[str]:
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
    if (hdevinfo := setupapi.SetupDiGetClassDevsW(
            guid_ref, None, None, flags)) == ctyped.const.INVALID_HANDLE_VALUE:
        yield
    else:
        try:
            yield hdevinfo
        finally:
            setupapi.SetupDiDestroyDeviceInfoList(hdevinfo)


def _get_str_dev_prop(hdevinfo: ctyped.type.HDEVINFO, dev_info_ref: ctyped.Pointer[ctyped.struct.SP_DEVINFO_DATA],
                      spdrp_or_devpkey: int | tuple[str, int]) -> str:
    if isinstance(spdrp_or_devpkey, int):
        getter = setupapi.SetupDiGetDeviceRegistryPropertyW
        key_ref = spdrp_or_devpkey
        type_ref = None
        flags = ()
    else:
        getter = setupapi.SetupDiGetDevicePropertyW
        key_ref = ctyped.byref(ctyped.struct.DEVPROPKEY(ctyped.get_guid(spdrp_or_devpkey[0]), spdrp_or_devpkey[1]))
        type_ref = ctyped.byref(ctyped.type.DEVPROPTYPE())
        flags = 0,
    sz = ctyped.type.DWORD()
    getter(hdevinfo, dev_info_ref, key_ref, type_ref, None, 0, ctyped.byref(sz), *flags)
    with _utils.string_buffer(sz.value) as buff:
        getter(hdevinfo, dev_info_ref, key_ref, type_ref, ctyped.cast(buff, ctyped.type.PBYTE), sz, None, *flags)
        return buff.value


def _get_str_devs_props(guid: Optional[str] = None, *devpkeys: int | tuple[str, int]) -> tuple[tuple[str, ...]]:
    vals = []
    guid_ref = None
    flags = ctyped.const.DIGCF_ALLCLASSES | ctyped.const.DIGCF_PRESENT
    if guid:
        guid_ref = ctyped.byref(ctyped.get_guid(ctyped.const.GUID_DEVCLASS_MONITOR))
        flags = ctyped.const.DIGCF_PRESENT
    with _get_hdevinfo(guid_ref, flags) as hdevinfo:
        if hdevinfo:
            dev_info = ctyped.struct.SP_DEVINFO_DATA()
            dev_info_ref = ctyped.byref(dev_info)
            index = 0
            while setupapi.SetupDiEnumDeviceInfo(hdevinfo, index, dev_info_ref):
                vals.append(tuple(_get_str_dev_prop(hdevinfo, dev_info_ref, devpkey) for devpkey in devpkeys))
                index += 1
    return tuple(vals)


def get_message(message: int) -> str:
    global _MESSAGES
    if _MESSAGES is None:
        _MESSAGES = {}
        for name, val in vars(ctyped.const).items():
            if name.startswith('WM_'):
                _MESSAGES[val] = name
    try:
        return _MESSAGES[message]
    except KeyError:
        return f'WM_{message}'


def get_error(hresult: Optional[ctyped.type.HRESULT] = None) -> str:
    with _utils.string_buffer() as buff:
        kernel32.FormatMessageW((
                ctyped.const.FORMAT_MESSAGE_ALLOCATE_BUFFER |
                ctyped.const.FORMAT_MESSAGE_FROM_SYSTEM | ctyped.const.FORMAT_MESSAGE_IGNORE_INSERTS),
            None, kernel32.GetLastError() if hresult is None else hresult,
            ctyped.macro.MAKELANGID(ctyped.const.LANG_NEUTRAL, ctyped.const.SUBLANG_DEFAULT),
            ctyped.cast(ctyped.byref(buff), ctyped.type.LPWSTR), 0, None)
        return buff.value.strip()


def alert_error(title: Optional[str | type], text: str) -> bool:
    if isinstance(title, type):
        title = title.__name__
    return user32.MessageBoxW(None, text, title, ctyped.const.MB_OK |
                              ctyped.const.MB_ICONERROR | ctyped.const.MB_SYSTEMMODAL) != 0


def get_max_shutdown_time() -> float:
    buff = ctyped.type.c_int()
    user32.SystemParametersInfoW(ctyped.const.SPI_GETWAITTOKILLTIMEOUT, 0, ctyped.byref(buff), 0)
    return buff.value / 1000


# noinspection PyShadowingBuiltins
def refresh_dir(dir: str):
    shell32.SHChangeNotify(ctyped.const.SHCNE_UPDATEDIR, ctyped.const.SHCNF_PATHW, dir, None)


def press_keyboard(key: int) -> bool:
    input_ = ctyped.struct.INPUT(ctyped.const.INPUT_KEYBOARD, ctyped.union.INPUT_U(ki=ctyped.struct.KEYBDINPUT(key)))
    ref = ctyped.byref(input_)
    sz = ctyped.sizeof(ctyped.struct.INPUT)
    if user32.SendInput(1, ref, sz) == 1:
        input_.U.ki.dwFlags = ctyped.const.KEYEVENTF_KEYUP
        return user32.SendInput(1, ref, sz) == 1
    return False


def open_file(path: str, *args: str) -> bool:
    return shell32.ShellExecuteW(
        None, None, path, subprocess.list2cmdline(args), None, ctyped.const.SW_SHOW) > 32


def open_file_path(path: str) -> bool:
    with _utils.get_itemidlist(path) as pidl:
        return ctyped.macro.SUCCEEDED(shell32.SHOpenFolderAndSelectItems(pidl[0], 0, None, 0))


def open_file_with(path: str) -> bool:
    info_ref = ctyped.byref(ctyped.struct.OPENASINFO(path, oaifInFlags=(
            ctyped.enum.OPEN_AS_INFO_FLAGS.EXEC | ctyped.enum.OPEN_AS_INFO_FLAGS.HIDE_REGISTRATION)))
    hr = shell32.SHOpenWithDialog(None, info_ref)
    return ctyped.macro.SUCCEEDED(hr) or hr == ctyped.macro.HRESULT_FROM_WIN32(error.ERROR_CANCELLED)


def open_file_with_ex(path: str) -> bool:
    p_options = ctyped.interface.WinRT[Windows_System.ILauncherOptions](
        runtimeclass.Windows.System.LauncherOptions)
    with p_options as options:
        if options and ctyped.macro.SUCCEEDED(options.put_DisplayApplicationPicker(True)) and (
                p_launcher := ctyped.interface.WinRT[Windows_System.ILauncherStatics](
                    runtimeclass.Windows.System.Launcher)) and (p_file := _utils.open_file(path)):
            operation = ctyped.winrt.AsyncOperation(ctyped.type.boolean)
            with p_launcher as launcher, p_file as file:
                if ctyped.macro.SUCCEEDED(launcher.LaunchFileWithOptionsAsync(file, options, ~operation)):
                    return bool(operation.get())
    return False


def save_hbitmap(hbitmap: ctyped.type.HBITMAP, path: str) -> bool:
    if hbitmap:
        with ctyped.interface.COM[ocidl.IPicture]() as picture:
            pict_desc = ctyped.struct.PICTDESC(picType=ctyped.const.PICTYPE_BITMAP)
            pict_desc.U.bmp.hbitmap = hbitmap
            args = ctyped.macro.IID_PPV_ARGS(picture)
            oleaut32.OleCreatePictureIndirect(ctyped.byref(pict_desc), args[0], False, args[1])
            with ctyped.interface.COM[ocidl.IPictureDisp](picture) as picture_disp:
                return ctyped.macro.SUCCEEDED(oleaut32.OleSavePictureFile(picture_disp, path))
    return False


def get_direct_show_devices_properties(
        clsid: str, prop_names: tuple[str] = ('DevicePath', 'FriendlyName')) -> tuple[tuple[Optional[str], ...], ...]:
    devices = []
    with ctyped.interface.COM[strmif.ICreateDevEnum](ctyped.const.CLSID_SystemDeviceEnum) as dev_enum:
        if dev_enum:
            with ctyped.interface.COM[objidl.IEnumMoniker]() as monikers:
                dev_enum.CreateClassEnumerator(ctyped.byref(ctyped.get_guid(clsid)), ctyped.byref(monikers), 0)
                with ctyped.interface.COM[objidl.IMoniker]() as moniker:
                    with ctyped.interface.COM[oaidl.IPropertyBag]() as prop_bag:
                        props = []
                        while monikers.Next(1, ctyped.byref(moniker), ctyped.NULLPTR) == ctyped.const.S_OK:
                            if ctyped.macro.SUCCEEDED(moniker.BindToStorage(
                                    ctyped.NULLPTR, ctyped.NULLPTR, *ctyped.macro.IID_PPV_ARGS(prop_bag))):
                                var = ctyped.struct.VARIANT()
                                var_ref = ctyped.byref(var)
                                props.clear()
                                for prop_name in prop_names:
                                    oleaut32.VariantInit(var_ref)
                                    prop_bag.Read(prop_name, var_ref, ctyped.NULLPTR)
                                    props.append(var.U.S.U.bstrVal)
                                    oleaut32.VariantClear(var_ref)
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
    unregister_autorun(name, uid)
    return _register_autorun_link(name, path, *args, show=show, aumi=uid) or _register_autorun_reg(name, path, *args)


def _unregister_autorun_reg(name: str) -> bool:
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, _STARTUP_KEY, access=winreg.KEY_SET_VALUE) as key:
        return _utils.delete_key(key, name)


def _unregister_autorun_link(aumi: str) -> bool:
    return remove_shortcuts(_STARTUP_DIR, aumi)


def unregister_autorun(name: Optional[str] = None, uid: Optional[str] = None):
    if name:
        _unregister_autorun_reg(name)
    if uid:
        _unregister_autorun_link(uid)


def create_shortcut(path: str, target: str, *args: str, icon_path: str = '', icon_index: int = 0,
                    comment: Optional[str] = None, start_in: Optional[str] = None, show: bool = True,
                    uid: Optional[str] = None, ext: str = LINK_EXT) -> bool:
    with ctyped.interface.COM[ShObjIdl_core.IShellLinkW](ctyped.const.CLSID_ShellLink) as link:
        created = link and _set_link_data(link, target, comment, ntpath.dirname(
            target) if start_in is None else start_in, subprocess.list2cmdline(
            args), show=ctyped.const.SW_SHOWNORMAL if show else ctyped.const.SW_SHOWMINNOACTIVE,
                                          icon=(icon_path, icon_index)) and _save_link(link, f'{path}{ext}')
    if created and uid is not None:
        created = set_shortcut_properties(f'{path}{ext}', {ctyped.const.PKEY_AppUserModel_ID: uid})
    return created


# noinspection PyShadowingBuiltins
def remove_shortcuts(dir: str, uid: str, rmdir: bool = True) -> bool:
    if uid is None:
        return False
    removed = True
    for path in _get_link_paths(dir, True):
        if uid == get_shortcut_properties(path, ctyped.const.PKEY_AppUserModel_ID)[0]:
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
        if not subprocess.run((_SYS_PIN_PATH, target, '5386' if taskbar else '51201'),
                              creationflags=subprocess.DETACHED_PROCESS).returncode:
            cur_name = ntpath.splitext(ntpath.basename(target))[0]
            if name is None:
                name = cur_name
            if taskbar:
                cur_path = ntpath.join(
                    _TASKBAR_DIR, f'{get_shortcut_properties(target, ctyped.const.PKEY_FileDescription)[0] or cur_name}{LINK_EXT}')
                path = ntpath.join(_TASKBAR_DIR, f'{name}{LINK_EXT}')
            else:
                cur_path = ntpath.join(START_DIR, f'{cur_name}{LINK_EXT}')
                path = ntpath.join(START_DIR, f'{name}{LINK_EXT}')
            end_time = time.monotonic() + _PIN_TIMEOUT
            while end_time > time.monotonic() and not ntpath.isfile(cur_path):
                time.sleep(_utils.POLL_INTERVAL)
            if ntpath.isfile(cur_path):
                os.replace(cur_path, path)
                if args or icon_path or icon_index or not show:
                    with _load_link(path) as link:
                        return _set_link_data(
                            link, args=subprocess.list2cmdline(args),  # FIXME taskbar button requires click to fix (no api)
                            show=ctyped.const.SW_SHOWNORMAL if show else ctyped.const.SW_SHOWMINNOACTIVE,
                            icon=(icon_path, icon_index)) and _save_link(link, path)
                else:
                    return ntpath.isfile(path)
    return False


def remove_pins(target: str, *args: str, taskbar: bool = True) -> bool:
    removed = True
    args = subprocess.list2cmdline(args)
    for path in _get_link_paths(_TASKBAR_DIR if taskbar else START_DIR):
        data = _get_link_data(path)
        if target == data[0] and args == data[3]:
            if taskbar:
                with ctyped.interface.COM[ShObjIdl.IStartMenuPinnedList](ctyped.const.CLSID_StartMenuPin) as pinned:
                    if pinned:
                        with ctyped.interface.COM[ShObjIdl_core.IShellItem]() as item:
                            shell32.SHCreateItemFromParsingName(
                                path, None, *ctyped.macro.IID_PPV_ARGS(item))
                            if item:
                                removed = ctyped.macro.SUCCEEDED(pinned.RemoveFromList(item)) and removed
            if ntpath.isfile(path):
                removed = kernel32.DeleteFileW(path) and removed
    return removed


@ctyped.type.ENUMRESNAMEPROCW
def _get_manifest_callback(hmodule, lptype, lpname, lparam):
    hrsrc = kernel32.FindResourceW(
        hmodule, ctyped.macro.MAKEINTRESOURCEW(lpname), ctyped.macro.MAKEINTRESOURCEW(lptype))
    string = ctyped.from_address(lparam, ctyped.struct.STRING)
    string.Length = kernel32.SizeofResource(hmodule, hrsrc)
    string.Buffer = kernel32.LockResource(kernel32.LoadResource(hmodule, hrsrc))
    return False


def get_manifest(path: Optional[str] = None) -> str:
    hmodule = kernel32.GetModuleHandleW(
        None) if path is None else kernel32.LoadLibraryExW(path, 0, ctyped.const.LOAD_LIBRARY_AS_DATAFILE)
    if hmodule:
        manifest = ctyped.struct.STRING()
        kernel32.EnumResourceNamesW(hmodule, ctyped.macro.MAKEINTRESOURCEW(
            ctyped.const.RT_MANIFEST), _get_manifest_callback, ctyped.addressof(manifest))
        try:
            if manifest.Length:
                return manifest.Buffer[:manifest.Length].decode()
        finally:
            kernel32.FreeLibrary(hmodule)
    return ''


def get_exe_size(path: str) -> int:
    size = 0
    hfile = kernel32.CreateFileW(path, ctyped.const.GENERIC_READ, ctyped.const.FILE_SHARE_READ, None,
                                 ctyped.const.OPEN_EXISTING, ctyped.const.FILE_ATTRIBUTE_NORMAL, None)
    if hfile:
        buff = ctyped.array(type=ctyped.type.BYTE, size=4096)
        kernel32.ReadFile(hfile, buff, ctyped.sizeof(buff), None, None)
        kernel32.CloseHandle(hfile)
        header = ctyped.cast(buff, ctyped.struct.IMAGE_DOS_HEADER).contents
        headers = ctyped.from_address(ctyped.addressof(buff) + header.e_lfanew, ctyped.struct.IMAGE_NT_HEADERS32)
        if headers.FileHeader.Machine == ctyped.const.IMAGE_FILE_MACHINE_AMD64:
            headers = ctyped.cast(headers, ctyped.struct.IMAGE_NT_HEADERS64).contents
        if header.e_magic == ctyped.const.IMAGE_DOS_SIGNATURE and headers.Signature == ctyped.const.IMAGE_NT_SIGNATURE:
            max_ptr = 0
            for section in ctyped.from_address(ctyped.addressof(headers) + ctyped.sizeof(
                    headers), ctyped.struct.IMAGE_SECTION_HEADER * headers.FileHeader.NumberOfSections):
                if section.PointerToRawData > max_ptr:
                    max_ptr = section.PointerToRawData
                    size = max_ptr + section.SizeOfRawData
    return size


ctyped.interface.init_com()
