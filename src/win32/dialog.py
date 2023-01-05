import os.path
from typing import MutableSequence, Optional

from libs import ctyped
from libs.ctyped.const import error
from libs.ctyped.interface.um import ShObjIdl_core
from . import _gdiplus, _utils


def _set_folder(dialog: ShObjIdl_core.IFileDialog, path: Optional[str] = None) -> bool:
    if path is not None:
        with ctyped.interface.COM[ShObjIdl_core.IShellItem]() as item:
            return ctyped.macro.SUCCEEDED(ctyped.lib.shell32.SHCreateItemFromParsingName(
                path, None, *ctyped.macro.IID_PPV_ARGS(item))) and ctyped.macro.SUCCEEDED(dialog.SetFolder(item))
    return True


def _get_path(dialog: ShObjIdl_core.IFileDialog) -> str:
    with ctyped.interface.COM[ShObjIdl_core.IShellItem]() as item:
        dialog.GetResult(ctyped.byref(item))
        with _utils.string_buffer() as buff:
            item.GetDisplayName(ctyped.enum.SIGDN.FILESYSPATH, ctyped.byref(buff))
            path = buff.value
        return path


def open_folder(path: Optional[str] = None, title: Optional[str] = None) -> Optional[str]:
    with ctyped.interface.COM[ShObjIdl_core.IFileDialog](ctyped.const.CLSID_FileOpenDialog) as dialog:
        if dialog:
            dialog.SetOptions(ctyped.enum.FILEOPENDIALOGOPTIONS.PICKFOLDERS | ctyped.enum.FILEOPENDIALOGOPTIONS.FORCEFILESYSTEM)
            _set_folder(dialog, path)
            if title is not None:
                dialog.SetTitle(title)
            hr = dialog.Show(ctyped.NULLPTR)
            if ctyped.macro.SUCCEEDED(hr):
                return _get_path(dialog)
            elif hr == ctyped.macro.HRESULT_FROM_WIN32(error.ERROR_CANCELLED):
                return path


def _get_ext_name(ext: str) -> str:
    info = ctyped.struct.SHFILEINFOW()
    if ctyped.lib.shell32.SHGetFileInfoW(ext, ctyped.const.FILE_ATTRIBUTE_NORMAL, ctyped.byref(
            info), ctyped.sizeof(info), ctyped.const.SHGFI_TYPENAME | ctyped.const.SHGFI_USEFILEATTRIBUTES):
        return info.szTypeName
    return 'File'


def save_file(path: Optional[str] = None, title: Optional[str] = None,
              types: Optional[dict[str, str]] = None, type_index: Optional[int] = None) -> Optional[str]:
    with ctyped.interface.COM[ShObjIdl_core.IFileSaveDialog](ctyped.const.CLSID_FileSaveDialog) as dialog:
        if dialog:
            ext = os.path.splitext(path)[1]
            if types is None:
                types = {_get_ext_name(ext): f'*{ext}'}
            filters = ctyped.array(type=ctyped.struct.COMDLG_FILTERSPEC, size=len(types))
            for filter_spec, (name, spec) in zip(filters, types.items()):
                filter_spec.pszName = name
                filter_spec.pszSpec = spec
            dialog.SetFileTypes(len(types), filters)
            if type_index is None:
                for index, spec in enumerate(types.values()):
                    if ctyped.lib.shlwapi.PathMatchSpecW(path, spec):
                        type_index = index
                        break
                else:
                    type_index = 0
            dialog.SetFileTypeIndex(type_index + 1)
            dialog.SetOptions(ctyped.enum.FILEOPENDIALOGOPTIONS.FORCEFILESYSTEM)
            dialog.SetFileName(os.path.basename(path))
            dialog.SetDefaultExtension(ext[1:])
            _set_folder(dialog, os.path.dirname(path))
            if title is not None:
                dialog.SetTitle(title)
            hr = dialog.Show(ctyped.NULLPTR)
            if ctyped.macro.SUCCEEDED(hr):
                return _get_path(dialog)
            elif hr == ctyped.macro.HRESULT_FROM_WIN32(error.ERROR_CANCELLED):
                return path


def save_image(path: Optional[str] = None, title: Optional[str] = None) -> Optional[str]:
    with _gdiplus.ImageCodec.get_encoders() as encoders:
        return save_file(path, title, {_get_ext_name(
            f'.{encoder.FormatDescription}'): encoder.FilenameExtension.lower() for encoder in encoders})


def _cchookproc(hwnd: ctyped.type.HWND, message: ctyped.type.UINT,
                _: ctyped.type.WPARAM, lparam: ctyped.type.LPARAM) -> ctyped.type.UINT_PTR:
    if message == ctyped.const.WM_INITDIALOG:
        ctyped.lib.user32.SetWindowPos(hwnd, ctyped.const.HWND_TOPMOST, 0, 0, 0, 0,
                                       ctyped.const.SWP_NOSIZE | ctyped.const.SWP_NOMOVE)
        title_address = ctyped.from_address(lparam, ctyped.struct.CHOOSECOLORW).lCustData
        if title_address:
            ctyped.lib.user32.SetWindowTextW(hwnd, ctyped.from_address(title_address, ctyped.type.LPWSTR))
    return 0


def choose_color(title: Optional[str] = None, color: Optional[int] = None,
                 custom_colors: Optional[MutableSequence[int]] = None) -> Optional[int]:
    data = ctyped.type.LPWSTR(title)
    color_chooser = ctyped.struct.CHOOSECOLORW(
        rgbResult=0 if color is None else color, lpCustColors=ctyped.array(*(
            () if custom_colors is None else custom_colors), type=ctyped.type.COLORREF, size=16),
        Flags=ctyped.const.CC_RGBINIT | ctyped.const.CC_FULLOPEN | ctyped.const.CC_ENABLEHOOK,
        lCustData=0 if title is None else ctyped.addressof(data), lpfnHook=ctyped.type.LPCCHOOKPROC(_cchookproc))
    if ctyped.lib.comdlg32.ChooseColorW(ctyped.byref(color_chooser)):
        color = color_chooser.rgbResult
    if custom_colors is not None:
        custom_colors[:] = color_chooser.lpCustColors[:16]
    return color
