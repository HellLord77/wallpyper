import contextlib
import winreg
from typing import ContextManager, Optional

import libs.ctyped as ctyped


def get_dir(folderid: str) -> str:
    buff = ctyped.type.PWSTR()
    ctyped.func.shell32.SHGetKnownFolderPath(ctyped.byref(ctyped.get_guid(folderid)),
                                             ctyped.enum.KNOWN_FOLDER_FLAG.KF_FLAG_DEFAULT, None, ctyped.byref(buff))
    path = buff.value
    ctyped.func.ole32.CoTaskMemFree(buff)
    return path


@contextlib.contextmanager
def string_buffer(size: Optional[int] = None) -> ContextManager[ctyped.type.LPWSTR]:
    ptr = ctyped.type.LPWSTR(*() if size is None else ('\0' * size,))
    try:
        yield ptr
    finally:
        if size is None and ptr:
            ctyped.func.kernel32.LocalFree(ptr)


@contextlib.contextmanager
def get_itemidlist(*paths: str) -> ContextManager[tuple[ctyped.Pointer[ctyped.struct.ITEMIDLIST]]]:
    ids = tuple(ctyped.func.shell32.ILCreateFromPath(path) for path in paths)
    try:
        yield ids
    finally:
        for id_ in ids:
            ctyped.func.shell32.ILFree(id_)


def get_str_dev_id_prop(dev_path: str, devpkey: tuple[str, int]) -> str:
    sz = ctyped.type.ULONG()
    type_ref = ctyped.byref(ctyped.type.DEVPROPTYPE())
    prop_key_ref = ctyped.byref(ctyped.struct.DEVPROPKEY(ctyped.get_guid(devpkey[0]), devpkey[1]))
    ctyped.func.cfgmgr32.CM_Get_Device_Interface_PropertyW(dev_path, prop_key_ref, type_ref, None, ctyped.byref(sz), 0)
    with string_buffer(sz.value) as buff:
        ctyped.func.cfgmgr32.CM_Get_Device_Interface_PropertyW(
            dev_path, prop_key_ref, type_ref, ctyped.cast(buff, ctyped.type.PBYTE), ctyped.byref(sz), 0)
        return buff.value


def get_str_dev_node_props(dev_id: str, *devpkeys: tuple[str, int]) -> tuple[str, ...]:
    props = []
    dev_int = ctyped.type.DEVINST()
    sz = ctyped.type.ULONG()
    type_ = ctyped.type.DEVPROPTYPE()
    for devpkey in devpkeys:
        prop_key_ref = ctyped.byref(ctyped.struct.DEVPROPKEY(ctyped.get_guid(devpkey[0]), devpkey[1]))
        ctyped.func.cfgmgr32.CM_Locate_DevNodeW(ctyped.byref(dev_int), dev_id, ctyped.const.CM_LOCATE_DEVNODE_NORMAL)
        ctyped.func.cfgmgr32.CM_Get_DevNode_PropertyW(dev_int, prop_key_ref, ctyped.byref(type_),
                                                      None, ctyped.byref(sz), 0)
        with string_buffer(sz.value) as buff:
            ctyped.func.cfgmgr32.CM_Get_DevNode_PropertyW(dev_int, prop_key_ref, ctyped.byref(type_),
                                                          ctyped.cast(buff, ctyped.type.PBYTE), ctyped.byref(sz), 0)
            props.append(buff.value)
    return tuple(props)


@contextlib.contextmanager
def open_file(path: str) -> ContextManager[Optional[ctyped.com.IStorageFile]]:
    with ctyped.get_winrt(ctyped.com.IStorageFileStatics) as file_statics:
        if file_statics:
            operation = ctyped.Async(ctyped.com.IAsyncOperation)
            if ctyped.macro.SUCCEEDED(file_statics.GetFileFromPathAsync(
                    ctyped.handle.HSTRING.from_string(path), operation.get_ref())) and (
                    file := operation.get(ctyped.com.IStorageFile)):
                yield file
                return
    yield None


def delete_key(key: winreg.HKEYType, name: str) -> bool:
    for _ in range(2):
        try:
            winreg.DeleteValue(key, name)
        except FileNotFoundError:
            return True
    return False
