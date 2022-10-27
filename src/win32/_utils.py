import contextlib
import winreg
from typing import Any, Callable, ContextManager, Iterable, Mapping, Optional

import libs.ctyped as ctyped


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
        if size is None and ptr:
            ctyped.lib.kernel32.LocalFree(ptr)


@contextlib.contextmanager
def get_itemidlist(*paths: str) -> ContextManager[tuple[ctyped.Pointer[ctyped.struct.ITEMIDLIST]]]:
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


@contextlib.contextmanager
def open_file(path: str) -> ContextManager[Optional[ctyped.interface.Windows.Storage.IStorageFile]]:
    with ctyped.get_winrt(ctyped.interface.Windows.Storage.IStorageFileStatics) as file_statics:
        if file_statics:
            with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperation[ctyped.interface.Windows.Storage.IStorageFile]) as operation:
                if ctyped.macro.SUCCEEDED(file_statics.GetFileFromPathAsync(
                        ctyped.handle.HSTRING.from_string(path), operation.get_ref())) and (file := operation.get()):
                    yield file
                    return
    yield


@contextlib.contextmanager
def open_file_stream(path: str, mode: int = ctyped.const.STGM_READ) -> ContextManager[Optional[ctyped.interface.IStream]]:
    with ctyped.init_com(ctyped.interface.IStream, False) as stream:
        if ctyped.macro.SUCCEEDED(ctyped.lib.shlwapi.SHCreateStreamOnFileW(path, mode, ctyped.byref(stream))):
            yield stream
            return
    yield


@contextlib.contextmanager
def get_input_stream(file: ctyped.interface.Windows.Storage.IStorageFile) -> \
        ContextManager[Optional[ctyped.interface.Windows.Storage.Streams.IInputStream]]:
    with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperation[ctyped.interface.Windows.Storage.Streams.IRandomAccessStream]) as operation:
        if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.Windows.Storage.FileAccessMode.Read, operation.get_ref())) and (stream := operation.get()):
            with ctyped.init_com(ctyped.interface.Windows.Storage.Streams.IInputStream, False) as input_stream:
                if ctyped.macro.SUCCEEDED(stream.GetInputStreamAt(0, ctyped.byref(input_stream))):
                    yield input_stream
                    return
    yield


@contextlib.contextmanager
def get_output_stream(file: ctyped.interface.Windows.Storage.IStorageFile) -> \
        ContextManager[Optional[ctyped.interface.Windows.Storage.Streams.IOutputStream]]:
    with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperation[ctyped.interface.Windows.Storage.Streams.IRandomAccessStream]) as operation:
        if ctyped.macro.SUCCEEDED(file.OpenAsync(ctyped.enum.Windows.Storage.FileAccessMode.ReadWrite, operation.get_ref())) and (stream := operation.get()):
            with ctyped.init_com(ctyped.interface.Windows.Storage.Streams.IOutputStream, False) as output_stream:
                if ctyped.macro.SUCCEEDED(stream.GetOutputStreamAt(0, ctyped.byref(output_stream))):
                    yield output_stream
                    return
    yield


@contextlib.contextmanager
def get_wallpaper_lock_input_stream() -> \
        ContextManager[Optional[ctyped.interface.Windows.Storage.Streams.IInputStream]]:
    with ctyped.get_winrt(ctyped.interface.Windows.System.UserProfile.ILockScreenStatics) as lock_statics:
        if lock_statics:
            with ctyped.init_com(ctyped.interface.Windows.Storage.Streams.IRandomAccessStream, False) as stream:
                if ctyped.macro.SUCCEEDED(lock_statics.GetImageStream(ctyped.byref(stream))):
                    with ctyped.init_com(
                            ctyped.interface.Windows.Storage.Streams.IInputStream, False) as input_stream:
                        if ctyped.macro.SUCCEEDED(stream.GetInputStreamAt(0, ctyped.byref(input_stream))):
                            yield input_stream
                            return
    yield


def copy_stream(input_stream: ctyped.interface.Windows.Storage.Streams.IInputStream,
                output_stream: ctyped.interface.Windows.Storage.Streams.IOutputStream,
                progress_callback: Optional[Callable[[int, ...], Any]],
                args: Optional[Iterable], kwargs: Optional[Mapping[str, Any]]) -> bool:
    with ctyped.get_winrt(ctyped.interface.Windows.Storage.Streams.IRandomAccessStreamStatics) as stream_statics:
        if stream_statics:
            with ctyped.Async(ctyped.interface.Windows.Foundation.IAsyncOperationWithProgress[ctyped.type.UINT64, ctyped.type.UINT64]) as operation:
                if ctyped.macro.SUCCEEDED(stream_statics.CopyAndCloseAsync(
                        input_stream, output_stream, operation.get_ref())):
                    if progress_callback is not None:
                        operation.put_progress(progress_callback, args, kwargs)
                    return ctyped.enum.Windows.Foundation.AsyncStatus.Completed == operation.wait_for()
    return False


@contextlib.contextmanager
def get_d2d1_dc_render_target() -> ContextManager[Optional[ctyped.interface.ID2D1DCRenderTarget]]:
    with ctyped.init_com(ctyped.interface.ID2D1Factory, False) as factory, ctyped.init_com(
            ctyped.interface.ID2D1DCRenderTarget, False) as target:
        p_iid, p_factory = ctyped.macro.IID_PPV_ARGS(factory)
        if ctyped.macro.SUCCEEDED(ctyped.lib.d2d1.D2D1CreateFactory(ctyped.enum.D2D1_FACTORY_TYPE.SINGLE_THREADED, p_iid, None, p_factory)) and ctyped.macro.SUCCEEDED(
                factory.CreateDCRenderTarget(ctyped.byref(ctyped.struct.D2D1_RENDER_TARGET_PROPERTIES(pixelFormat=ctyped.struct.D2D1_PIXEL_FORMAT(
                    ctyped.enum.DXGI_FORMAT.DF_B8G8R8A8_UNORM, ctyped.enum.D2D1_ALPHA_MODE.PREMULTIPLIED))), ctyped.byref(target))):
            yield target
            return
    yield


def set_svg_doc_viewport(svg: ctyped.interface.ID2D1SvgDocument) -> bool:
    with ctyped.init_com(ctyped.interface.ID2D1SvgElement, False) as root:
        if ctyped.macro.SUCCEEDED(svg.GetRoot(ctyped.byref(root))):
            view_box = ctyped.struct.D2D1_SVG_VIEWBOX()
            if root.IsAttributeSpecified('viewBox', None):
                root.GetAttributeValue_('viewBox', ctyped.enum.D2D1_SVG_ATTRIBUTE_POD_TYPE.VIEWBOX,
                                        ctyped.byref(view_box), ctyped.sizeof(view_box))
            elif root.IsAttributeSpecified('width', None) and root.IsAttributeSpecified('height', None):
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


def set_svg_doc_dimension(svg: ctyped.interface.ID2D1SvgDocument, width: float = 0, height: float = 0) -> bool:
    with ctyped.init_com(ctyped.interface.ID2D1SvgElement, False) as root:
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
