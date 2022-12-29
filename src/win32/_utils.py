import contextlib
import ntpath
import os
import winreg
from typing import Any, Callable, ContextManager, Iterable, Mapping, Optional

from libs import ctyped
from libs.ctyped import winrt
from libs.ctyped.interface.um import DispEx, d2d1, d2d1svg, oaidl, objidlbase
from libs.ctyped.interface.winrt.Windows import Storage as Windows_Storage
from libs.ctyped.interface.winrt.Windows.Storage import Streams as Windows_Storage_Streams
from libs.ctyped.interface.winrt.Windows.System import UserProfile as Windows_System_UserProfile
from . import _com

POLL_INTERVAL = 0.1


class BSTRGetter(_com.Getter):
    def __get__(self, instance: _com.Unknown, owner: type[_com.Unknown]) -> Optional[str]:
        with get_bstr() as bstr:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._getter)(ctyped.byref(bstr))
            return ctyped.type.c_wchar_p.from_buffer(bstr).value


class BSTRSetter(_com.Setter):
    def __set__(self, instance: _com.Unknown, value: str):
        with get_bstr(value) as value:
            # noinspection PyProtectedMember
            getattr(instance._obj, self._setter)(value)


class BSTRGetterSetter(BSTRSetter, BSTRGetter):
    pass


def get_dir(folderid: str) -> str:
    buff = ctyped.type.PWSTR()
    ctyped.lib.shell32.SHGetKnownFolderPath(ctyped.byref(ctyped.get_guid(
        folderid)), ctyped.enum.KNOWN_FOLDER_FLAG.DEFAULT, None, ctyped.byref(buff))
    try:
        return buff.value
    finally:
        ctyped.lib.ole32.CoTaskMemFree(buff)


@contextlib.contextmanager
def string_buffer(size: Optional[int] = None) -> ContextManager[ctyped.type.LPWSTR]:
    ptr = ctyped.type.LPWSTR(*() if size is None else ('\0' * size,))
    try:
        yield ptr
    finally:
        if size is None and ptr.value:
            ctyped.lib.kernel32.LocalFree(ptr)


@contextlib.contextmanager
def get_itemidlist(*paths: str | ctyped.type.PCWSTR) -> ContextManager[tuple[ctyped.Pointer[ctyped.struct.ITEMIDLIST]]]:
    ids = tuple(ctyped.lib.shell32.ILCreateFromPath(path) for path in paths)
    try:
        yield ids
    finally:
        for id_ in ids:
            ctyped.lib.shell32.ILFree(id_)


def get_str_dev_id_prop(dev_path: str, devpkey: tuple[str, int]) -> str:
    sz = ctyped.type.ULONG()
    type_ref = ctyped.byref(ctyped.type.DEVPROPTYPE())
    prop_key_ref = ctyped.byref(ctyped.struct.DEVPROPKEY(ctyped.get_guid(devpkey[0]), devpkey[1]))
    ctyped.lib.cfgmgr32.CM_Get_Device_Interface_PropertyW(dev_path, prop_key_ref, type_ref, None, ctyped.byref(sz), 0)
    with string_buffer(sz.value) as buff:
        ctyped.lib.cfgmgr32.CM_Get_Device_Interface_PropertyW(
            dev_path, prop_key_ref, type_ref, ctyped.cast(buff, ctyped.type.PBYTE), ctyped.byref(sz), 0)
        return buff.value


def get_str_dev_node_props(dev_id: str, *devpkeys: tuple[str, int]) -> tuple[str, ...]:
    props = []
    dev_int = ctyped.type.DEVINST()
    sz = ctyped.type.ULONG()
    type_ = ctyped.type.DEVPROPTYPE()
    for devpkey in devpkeys:
        prop_key_ref = ctyped.byref(ctyped.struct.DEVPROPKEY(ctyped.get_guid(devpkey[0]), devpkey[1]))
        ctyped.lib.cfgmgr32.CM_Locate_DevNodeW(ctyped.byref(dev_int), dev_id, ctyped.const.CM_LOCATE_DEVNODE_NORMAL)
        ctyped.lib.cfgmgr32.CM_Get_DevNode_PropertyW(
            dev_int, prop_key_ref, ctyped.byref(type_), None, ctyped.byref(sz), 0)
        with string_buffer(sz.value) as buff:
            ctyped.lib.cfgmgr32.CM_Get_DevNode_PropertyW(
                dev_int, prop_key_ref, ctyped.byref(type_), ctyped.cast(buff, ctyped.type.PBYTE), ctyped.byref(sz), 0)
            props.append(buff.value)
    return tuple(props)


def delete_key(key: winreg.HKEYType, name: str) -> bool:
    for _ in range(2):
        try:
            winreg.DeleteValue(key, name)
        except FileNotFoundError:
            return True
    return False


def sanitize_filename(name: str) -> Optional[str]:
    buff = ctyped.type.PWSTR(name)
    if ctyped.lib.shell32.PathCleanupSpec(None, buff) & ctyped.const.PCS_FATAL != ctyped.const.PCS_FATAL:
        return buff.value


def open_file(path: str) -> Optional[ctyped.interface.WinRT[Windows_Storage.IStorageFile]]:
    operation = winrt.AsyncOperation(Windows_Storage.IStorageFile)
    with ctyped.interface.WinRT[Windows_Storage.IStorageFileStatics](
            ctyped.const.runtimeclass.Windows.Storage.StorageFile) as statics:
        if ctyped.macro.SUCCEEDED(statics.GetFileFromPathAsync(
                ctyped.handle.HSTRING.from_string(path), ~operation)) and (file := operation.get()):
            return ctyped.interface.WinRT[Windows_Storage.IStorageFile](file.value)


def open_file_stream(path: str, mode: int = ctyped.const.STGM_READ) -> Optional[ctyped.interface.COM[objidlbase.IStream]]:
    stream = ctyped.interface.COM[objidlbase.IStream]()
    if ctyped.macro.SUCCEEDED(ctyped.lib.shlwapi.SHCreateStreamOnFileW(path, mode, ~stream)):
        return stream


def get_input_stream(file: Windows_Storage.IStorageFile) -> \
        Optional[ctyped.interface.WinRT[Windows_Storage_Streams.IInputStream]]:
    operation = winrt.AsyncOperation(Windows_Storage_Streams.IRandomAccessStream)
    if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.Windows.Storage.FileAccessMode.Read,
                                             ~operation)) and (stream := operation.get()):
        input_stream = ctyped.interface.WinRT[Windows_Storage_Streams.IInputStream]()
        hr = stream.GetInputStreamAt(0, ~input_stream)
        stream.Release()
        if ctyped.macro.SUCCEEDED(hr):
            return input_stream


def get_output_stream(file: Windows_Storage.IStorageFile) -> \
        Optional[ctyped.interface.WinRT[Windows_Storage_Streams.IOutputStream]]:
    operation = winrt.AsyncOperation(Windows_Storage_Streams.IRandomAccessStream)
    if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.Windows.Storage.FileAccessMode.ReadWrite,
                                             ~operation)) and (stream := operation.get()):
        output_stream = ctyped.interface.WinRT[Windows_Storage_Streams.IOutputStream]()
        hr = stream.GetOutputStreamAt(0, ~output_stream)
        stream.Release()
        if ctyped.macro.SUCCEEDED(hr):
            return output_stream


def get_lock_background_input_stream() -> \
        Optional[ctyped.interface.WinRT[Windows_Storage_Streams.IInputStream]]:
    if p_statics := ctyped.interface.WinRT[Windows_System_UserProfile.ILockScreenStatics](
            ctyped.const.runtimeclass.Windows.System.UserProfile.LockScreen):
        p_random = ctyped.interface.WinRT[Windows_Storage_Streams.IRandomAccessStream]()
        with p_statics as statics:
            if ctyped.macro.SUCCEEDED(statics.GetImageStream(~p_random)):
                input_stream = ctyped.interface.WinRT[Windows_Storage_Streams.IInputStream]()
                with p_random as random:
                    if ctyped.macro.SUCCEEDED(random.GetInputStreamAt(0, ~input_stream)):
                        return input_stream


def copy_stream(input_stream: Windows_Storage_Streams.IInputStream,
                output_stream: Windows_Storage_Streams.IOutputStream,
                progress_callback: Optional[Callable[[int, ...], Any]],
                args: Optional[Iterable], kwargs: Optional[Mapping[str, Any]]) -> bool:
    p_statics = ctyped.interface.WinRT[Windows_Storage_Streams.IRandomAccessStreamStatics](
        ctyped.const.runtimeclass.Windows.Storage.Streams.RandomAccessStream)
    if p_statics:
        operation = winrt.AsyncOperationWithProgress(ctyped.type.UINT64, ctyped.type.UINT64)
        with p_statics as statics:
            if ctyped.macro.SUCCEEDED(statics.CopyAndCloseAsync(input_stream, output_stream, ~operation)):
                if progress_callback is not None:
                    if args is None:
                        args = ()
                    if kwargs is None:
                        kwargs = {}

                    def handler(_, __, progress: int):
                        try:
                            progress_callback(progress, *args, **kwargs)
                        finally:
                            return ctyped.const.NOERROR

                    operation.on_progress(handler)
                return ctyped.enum.Windows.Foundation.AsyncStatus.Completed == operation.wait()
    return False


def copy_file(src: str, dst: str, progress_callback: Optional[Callable[[int, ...], Any]],
              args: Optional[Iterable] = None, kwargs: Optional[Mapping[str, Any]] = None) -> bool:
    p_src = open_file(src)
    if p_src:
        os.makedirs(ntpath.dirname(dst), exist_ok=True)
        open(dst, 'w').close()
        if p_dst := open_file(dst):
            with p_src as f_src, p_dst as f_dst, get_input_stream(
                    f_src) as i_stream, get_output_stream(f_dst) as o_stream:
                return copy_stream(i_stream, o_stream, progress_callback, args, kwargs)
    return False


@contextlib.contextmanager
def get_d2d1_dc_render_target() -> ContextManager[Optional[d2d1.ID2D1DCRenderTarget]]:
    with ctyped.interface.COM[d2d1.ID2D1Factory]() as factory, ctyped.interface.COM[d2d1.ID2D1DCRenderTarget]() as target:
        p_iid, p_factory = ctyped.macro.IID_PPV_ARGS(factory)
        if ctyped.macro.SUCCEEDED(ctyped.lib.d2d1.D2D1CreateFactory(ctyped.enum.D2D1_FACTORY_TYPE.SINGLE_THREADED, p_iid, None, p_factory)) and ctyped.macro.SUCCEEDED(
                factory.CreateDCRenderTarget(ctyped.byref(ctyped.struct.D2D1_RENDER_TARGET_PROPERTIES(pixelFormat=ctyped.struct.D2D1_PIXEL_FORMAT(
                    ctyped.enum.DXGI_FORMAT.DF_B8G8R8A8_UNORM, ctyped.enum.D2D1_ALPHA_MODE.PREMULTIPLIED))), ctyped.byref(target))):
            yield target
            return
    yield


def set_svg_doc_viewport(svg: d2d1svg.ID2D1SvgDocument) -> bool:
    with ctyped.interface.COM[d2d1svg.ID2D1SvgElement]() as root:
        if ctyped.macro.SUCCEEDED(svg.GetRoot(ctyped.byref(root))):
            view_box = ctyped.struct.D2D1_SVG_VIEWBOX()
            if root.IsAttributeSpecified('viewBox', ctyped.NULLPTR):
                root.GetAttributeValue_('viewBox', ctyped.enum.D2D1_SVG_ATTRIBUTE_POD_TYPE.VIEWBOX,
                                        ctyped.byref(view_box), ctyped.sizeof(view_box))
            elif root.IsAttributeSpecified('width', ctyped.NULLPTR) and root.IsAttributeSpecified('height', ctyped.NULLPTR):
                buff = ctyped.type.FLOAT()
                if ctyped.macro.SUCCEEDED(root.GetAttributeValue_('width', ctyped.enum.D2D1_SVG_ATTRIBUTE_POD_TYPE.FLOAT,
                                                                  ctyped.byref(buff), ctyped.sizeof(buff))):
                    view_box.width = buff.value
                if ctyped.macro.SUCCEEDED(root.GetAttributeValue_('height', ctyped.enum.D2D1_SVG_ATTRIBUTE_POD_TYPE.FLOAT,
                                                                  ctyped.byref(buff), ctyped.sizeof(buff))):
                    view_box.height = buff.value
            if view_box.width and view_box.width:
                return ctyped.macro.SUCCEEDED(svg.SetViewportSize(ctyped.struct.D2D_SIZE_F(view_box.width, view_box.height)))
    return False


def set_svg_doc_dimension(svg: d2d1svg.ID2D1SvgDocument, width: float = 0, height: float = 0) -> bool:
    with ctyped.interface.COM[d2d1svg.ID2D1SvgElement]() as root:
        if set_ := ctyped.macro.SUCCEEDED(svg.GetRoot(ctyped.byref(root))):
            buff = ctyped.type.FLOAT()
            ref = ctyped.byref(buff)
            size = ctyped.sizeof(buff)
            if width:
                buff.value = width
                set_ = ctyped.macro.SUCCEEDED(root.SetAttributeValue_(
                    'width', ctyped.enum.D2D1_SVG_ATTRIBUTE_POD_TYPE.FLOAT, ref, size))
            if height:
                buff.value = height
                set_ = ctyped.macro.SUCCEEDED(root.SetAttributeValue_(
                    'height', ctyped.enum.D2D1_SVG_ATTRIBUTE_POD_TYPE.FLOAT, ref, size)) and set_
    return set_


def get_variant_value(variant: ctyped.struct.VARIANT) -> Optional[bool | int | float | str | oaidl.IDispatch]:
    var_type = variant.U.S.vt
    if var_type == ctyped.enum.VARENUM.EMPTY:
        return
    elif var_type == ctyped.enum.VARENUM.NULL:
        return
    elif var_type == ctyped.enum.VARENUM.I4:
        return variant.U.S.U.intVal
    elif var_type == ctyped.enum.VARENUM.R8:
        return variant.U.S.U.dblVal
    elif var_type == ctyped.enum.VARENUM.BSTR:
        return ctyped.type.c_wchar_p.from_buffer(variant.U.S.U).value
    elif var_type == ctyped.enum.VARENUM.DISPATCH:
        dispatch = oaidl.IDispatch()
        dispatch.value = variant.U.S.U.pdispVal
        return dispatch
    elif var_type == ctyped.enum.VARENUM.BOOL:
        return bool(variant.U.S.U.VARIANT_BOOL)


@contextlib.contextmanager
def get_bstr(string: Optional[str] = None) -> ContextManager[ctyped.type.BSTR]:
    bstr = ctyped.type.BSTR() if string is None else ctyped.type.BSTR(ctyped.lib.oleaut32.SysAllocString(string))
    try:
        yield bstr
    finally:
        if bstr:
            ctyped.lib.oleaut32.SysFreeString(bstr)


# noinspection PyShadowingBuiltins
def get_members(dispatch_ex: DispEx.IDispatchEx, all: bool = False) -> dict[int, str]:
    members = {}
    disp_id = ctyped.type.DISPID(ctyped.const.DISPID_STARTENUM)
    while ctyped.macro.SUCCEEDED(dispatch_ex.GetNextDispID(ctyped.const.fdexEnumAll if all else ctyped.const.fdexEnumDefault,
                                                           disp_id, ctyped.byref(disp_id))) and disp_id.value > 0:
        with get_bstr() as name:
            dispatch_ex.GetMemberName(disp_id, ctyped.byref(name))
            members[disp_id.value] = ctyped.type.c_wchar_p.from_buffer(name).value
    return members


def get_funcs(dispatch: oaidl.IDispatch) -> dict[int, str]:
    funcs = {}
    with ctyped.interface.COM[oaidl.ITypeInfo]() as type_info:
        if ctyped.macro.SUCCEEDED(dispatch.GetTypeInfo(0, ctyped.const.LOCALE_SYSTEM_DEFAULT, ctyped.byref(type_info))):
            p_type_attr = ctyped.pointer(ctyped.struct.TYPEATTR)()
            if ctyped.macro.SUCCEEDED(type_info.GetTypeAttr(ctyped.byref(p_type_attr))):
                p_func_desc = ctyped.pointer(ctyped.struct.FUNCDESC)()
                for index in range(p_type_attr.contents.cFuncs):
                    if ctyped.macro.SUCCEEDED(type_info.GetFuncDesc(index, ctyped.byref(p_func_desc))):
                        with get_bstr() as name:
                            type_info.GetDocumentation(p_func_desc.contents.memid, ctyped.byref(
                                name), ctyped.NULLPTR, ctyped.NULLPTR, ctyped.NULLPTR)
                            funcs[p_func_desc.contents.memid] = ctyped.type.c_wchar_p.from_buffer(name).value
                        type_info.ReleaseFuncDesc(p_func_desc)
                type_info.ReleaseTypeAttr(p_type_attr)
    return funcs
