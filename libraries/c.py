from __future__ import annotations

import ctypes
import ctypes.wintypes
import dataclasses
import functools
import typing

_T = typing.TypeVar('_T')


def _or(val: _T, default: _T) -> _T:
    return default if val is None else val


def _is_union(obj: typing.Any) -> bool:
    # noinspection PyProtectedMember,PyUnresolvedReferences
    return isinstance(obj, typing._UnionGenericAlias)


def _items(cls: type) -> dict[str, typing.Any]:
    for var, val in cls.__dict__.items():
        if not var.startswith('__') and not var.endswith('__'):
            yield var, val


def byref(var) -> ctypes.pointer:
    # noinspection PyTypeChecker
    return ctypes.byref(var)


def pointer(type_):
    return ctypes.POINTER(type_)


def sizeof(type_):
    return ctypes.sizeof(type_)


class Type:
    c_void_p = typing.Union[ctypes.c_void_p, ctypes.c_wchar_p, int, str]
    c_wchar_p = typing.Union[ctypes.c_wchar_p, str]
    c_int = typing.Union[ctypes.c_int, int]
    c_uint = typing.Union[ctypes.c_uint, int]
    c_uint32 = typing.Union[ctypes.c_uint32, int]
    c_short = typing.Union[ctypes.c_short, int]
    c_ushort = typing.Union[ctypes.c_ushort, int]
    c_long = typing.Union[ctypes.c_long, int]
    c_ulong = typing.Union[ctypes.c_ulong, int]
    size_t = typing.Union[ctypes.c_size_t, int]
    HRESULT = typing.Union[ctypes.HRESULT, int]
    c_wchar = typing.Union[ctypes.c_wchar, str]

    HANDLE = typing.Union[ctypes.wintypes.HANDLE, int]
    LPVOID = typing.Union[ctypes.wintypes.LPVOID, int]
    LPWSTR = typing.Union[ctypes.wintypes.LPWSTR, str]
    INT = typing.Union[ctypes.wintypes.INT, int]
    UINT = typing.Union[ctypes.wintypes.UINT, int]
    WORD = typing.Union[ctypes.wintypes.WORD, int]
    BOOL = typing.Union[ctypes.wintypes.BOOL, int]
    LONG = typing.Union[ctypes.wintypes.LONG, int]
    DWORD = typing.Union[ctypes.wintypes.DWORD, int]
    ULONG = typing.Union[ctypes.wintypes.ULONG, int]
    WCHAR = typing.Union[ctypes.wintypes.WCHAR, str]

    DebugEventProc = c_void_p
    GpBitmap = c_void_p
    GpImage = c_void_p
    PVOID = c_void_p
    UINT32 = c_uint32
    HBITMAP = HANDLE
    HGDIOBJ = HANDLE
    HGLOBAL = HANDLE
    HINSTANCE = HANDLE
    HWND = HANDLE
    ULONG_PTR = c_ulong
    SIZE_T = ULONG_PTR
    ARGB = DWORD
    GpStatus = HRESULT


class Structure:
    @dataclasses.dataclass
    class GdiplusStartupInput:
        GdiplusVersion: Type.UINT32 = 1
        DebugEventCallback: Type.DebugEventProc = None
        SuppressBackgroundThread: Type.BOOL = False
        SuppressExternalCodecs: Type.BOOL = False

    @dataclasses.dataclass
    class BITMAPINFOHEADER:
        biSize: Type.DWORD = None
        biWidth: Type.LONG = None
        biHeight: Type.LONG = None
        biPlanes: Type.WORD = None
        biBitCount: Type.WORD = None
        biCompression: Type.DWORD = None
        biSizeImage: Type.DWORD = None
        biXPelsPerMeter: Type.LONG = None
        biYPelsPerMeter: Type.LONG = None
        biClrUsed: Type.DWORD = None
        biClrImportant: Type.DWORD = None

    @dataclasses.dataclass
    class BITMAP:
        bmType: Type.LONG = None
        bmWidth: Type.LONG = None
        bmHeight: Type.LONG = None
        bmWidthBytes: Type.LONG = None
        bmPlanes: Type.WORD = None
        bmBitsPixel: Type.WORD = None
        bmBits: Type.LPVOID = None

    @dataclasses.dataclass
    class DIBSECTION:
        dsBm: Structure.BITMAP = None
        dsBmih: Structure.BITMAPINFOHEADER = None
        dsBitfields: Type.DWORD * 3 = None
        dshSection: Type.HANDLE = None
        dsOffset: Type.DWORD = None


class Function:
    memmove: typing.Callable[[Type.c_void_p, Type.c_void_p, Type.size_t],
                             Type.c_void_p] = ctypes.cdll.msvcrt.memmove
    wcslen: typing.Callable[[Type.c_wchar_p],
                            Type.size_t] = ctypes.cdll.msvcrt.wcslen

    global_alloc: typing.Callable[[Type.UINT, Type.SIZE_T],
                                  Type.HGLOBAL] = ctypes.windll.kernel32.GlobalAlloc
    global_lock: typing.Callable[[Type.HGLOBAL],
                                 Type.LPVOID] = ctypes.windll.kernel32.GlobalLock
    global_unlock: typing.Callable[[Type.HGLOBAL],
                                   Type.BOOL] = ctypes.windll.kernel32.GlobalUnlock

    system_parameters_info: typing.Callable[[Type.UINT, Type.UINT, Type.PVOID, Type.UINT],
                                            Type.BOOL] = ctypes.windll.user32.SystemParametersInfoW
    open_clipboard: typing.Callable[[typing.Optional[Type.HWND]],
                                    Type.BOOL] = ctypes.windll.user32.OpenClipboard
    close_clipboard: typing.Callable[[],
                                     Type.BOOL] = ctypes.windll.user32.CloseClipboard
    empty_clipboard: typing.Callable[[],
                                     Type.BOOL] = ctypes.windll.user32.EmptyClipboard
    get_clipboard_data: typing.Callable[[Type.UINT],
                                        Type.HANDLE] = ctypes.windll.user32.GetClipboardData
    set_clipboard_data: typing.Callable[[Type.UINT, Type.HANDLE],
                                        Type.HANDLE] = ctypes.windll.user32.SetClipboardData

    sh_get_folder_path: typing.Callable[[typing.Optional[Type.HWND], Type.c_int,  # TODO: SHGetKnownFolderPath
                                         typing.Optional[Type.HANDLE], Type.DWORD, Type.LPWSTR],
                                        Type.HRESULT] = ctypes.windll.shell32.SHGetFolderPathW

    load_image: typing.Callable[[Type.HINSTANCE, Type.LPWSTR, Type.UINT, Type.INT, Type.INT, Type.UINT],
                                Type.HANDLE] = ctypes.windll.user32.LoadImageW
    gdiplus_startup: typing.Callable[[pointer(Type.ULONG_PTR), pointer(Structure.GdiplusStartupInput),
                                      typing.Optional[pointer(Structure.GdiplusStartupInput)]],
                                     Type.c_int] = ctypes.windll.gdiplus.GdiplusStartup
    gdiplus_shutdown: typing.Callable[[pointer(Type.ULONG_PTR)],
                                      Type.c_void_p] = ctypes.windll.gdiplus.GdiplusShutdown
    gdip_create_bitmap_from_file: typing.Callable[[Type.c_wchar_p, pointer(Type.GpBitmap)],
                                                  Type.GpStatus] = ctypes.windll.gdiplus.GdipCreateBitmapFromFile
    delete_object: typing.Callable[[Type.HGDIOBJ],
                                   Type.BOOL] = ctypes.windll.gdi32.DeleteObject
    close_handle: typing.Callable[[Type.HANDLE],
                                  Type.BOOL] = ctypes.windll.kernel32.CloseHandle
    gdip_dispose_image: typing.Callable[[Type.GpImage],
                                        Type.GpStatus] = ctypes.windll.gdiplus.GdipDisposeImage
    gdip_create_HBITMAP_from_bitmap: typing.Callable[[Type.GpBitmap, pointer(Type.HBITMAP), Type.ARGB],
                                                     Type.GpStatus] = ctypes.windll.gdiplus.GdipCreateHBITMAPFromBitmap
    get_object: typing.Callable[[Type.HANDLE, Type.c_int, Type.LPVOID],
                                Type.c_int] = ctypes.windll.gdi32.GetObjectW


def _init():
    for var, type_ in _items(Type):
        if _is_union(type_):
            setattr(Type, var, type_.__args__[0])

    for var, struct in _items(Structure):
        class Wrapper(ctypes.Structure):
            _fields_ = tuple(typing.get_type_hints(struct).items())
            _defaults_ = {field: _or(getattr(struct, field), type_()) for field, type_ in _fields_}

            def __init__(self, *args, **kwargs):
                for i, var_ in enumerate(self._defaults_):
                    if i >= len(args) and var_ not in kwargs:
                        kwargs[var_] = self._defaults_[var_]
                super().__init__(*args, **kwargs)

            __repr__ = struct.__repr__

        functools.update_wrapper(Wrapper, struct, updated=())
        setattr(Structure, var, Wrapper)

    types = typing.get_type_hints(Function)
    for var, func in _items(Function):
        *func.argtypes, func.restype = (arg.__args__[0] if _is_union(arg) else arg for arg in types[var].__args__)


_init()
