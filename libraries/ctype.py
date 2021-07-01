from __future__ import annotations  # 3.10

import ctypes
import ctypes.wintypes
import dataclasses
import functools
import typing

_CT = typing.TypeVar('_CT')


def _items(cls: type) -> typing.Generator[dict[str, typing.Any], None, None]:
    for var, val in cls.__dict__.items():
        if not var.startswith('__') and not var.endswith('__'):
            yield var, val


def _resolve_type(obj):
    # noinspection PyProtectedMember,PyUnresolvedReferences
    if isinstance(obj, typing._UnionGenericAlias):
        obj = typing.get_args(obj)[0]
    # noinspection PyProtectedMember,PyUnresolvedReferences
    return ctypes.POINTER(typing.get_args(obj)[0]) if isinstance(obj, typing._GenericAlias) else obj


def _init():
    for var, type_ in _items(Type):
        setattr(Type, var, _resolve_type(type_))

    for var, struct in _items(Structure):
        class Wrapper(ctypes.Structure):
            _fields_ = tuple(typing.get_type_hints(struct).items())
            _defaults_ = {field: getattr(struct, field) or type_() for field, type_ in _fields_}

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
        types_ = typing.get_args(types[var])
        func.argtypes = (_resolve_type(type_) for type_ in types_[0])
        func.restype = _resolve_type(types_[1])

    globals()[Pointer.__name__] = ctypes.POINTER


class Constant:
    BI_BITFIELDS = 3
    BI_CMYK = 11
    BI_CMYKRLE4 = 13
    BI_CMYKRLE8 = 12
    BI_JPEG = 4
    BI_PNG = 5
    BI_RGB = 0
    BI_RLE4 = 2
    BI_RLE8 = 1

    CBM_INIT = 4

    CF_BITMAP = 2
    CF_DIB = 8
    CF_DIBV5 = 17
    CF_TEXT = 1
    CF_TIFF = 6
    CF_UNICODETEXT = 13
    CF_WAVE = 12

    CSIDL_APPDATA = 26
    CSIDL_LOCAL_APPDATA = 28
    CSIDL_MYPICTURES = 39

    DIB_PAL_COLORS = 1
    DIB_PAL_INDICES = 2
    DIB_RGB_COLORS = 0

    GHND = 66
    GMEM_FIXED = 0
    GMEM_MOVEABLE = 2
    GMEM_ZEROINIT = 64
    GPTR = 64

    SHGFP_TYPE_CURRENT = 0
    SHGFP_TYPE_DEFAULT = 1

    SPI_GETDESKWALLPAPER = 115
    SPI_SETDESKWALLPAPER = 20

    SPIF_NONE = 0
    SPIF_SENDCHANGE = 2
    SPIF_SENDWININICHANGE = 2
    SPIF_UPDATEINIFILE = 1


class Pointer(typing.Generic[_CT]):
    value = None

    # noinspection PyTypeChecker,PyUnusedLocal
    def __init__(self, type_: typing.Type[_CT]) -> typing.Type[Pointer[_CT]]:
        pass


class Type:
    c_byte = typing.Union[ctypes.c_byte, int]
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

    BYTE = typing.Union[ctypes.wintypes.BYTE, int]
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

    VOID = c_void_p
    PVOID = c_void_p
    LPCWSTR = LPWSTR
    UINT32 = c_uint32
    HBITMAP = HANDLE
    HGDIOBJ = HANDLE
    HGLOBAL = HANDLE
    HINSTANCE = HANDLE
    HDC = HANDLE
    HWND = HANDLE
    ULONG_PTR = c_ulong
    SIZE_T = ULONG_PTR
    ARGB = DWORD
    GpStatus = HRESULT
    Status = GpStatus


class Structure:
    @dataclasses.dataclass
    class GdiplusStartupInput:
        GdiplusVersion: Type.UINT32 = 1
        DebugEventCallback: Type.DebugEventProc = None
        SuppressBackgroundThread: Type.BOOL = None
        SuppressExternalCodecs: Type.BOOL = None

    @dataclasses.dataclass
    class RGBQUAD:
        rgbBlue: Type.BYTE = None
        rgbGreen: Type.BYTE = None
        rgbRed: Type.BYTE = None
        rgbReserved: Type.BYTE = 0

    @dataclasses.dataclass
    class BITMAPINFOHEADER:
        biSize: Type.DWORD = None
        biWidth: Type.LONG = None
        biHeight: Type.LONG = None
        biPlanes: Type.WORD = 1
        biBitCount: Type.WORD = None
        biCompression: Type.DWORD = None
        biSizeImage: Type.DWORD = None
        biXPelsPerMeter: Type.LONG = None
        biYPelsPerMeter: Type.LONG = None
        biClrUsed: Type.DWORD = None
        biClrImportant: Type.DWORD = None

    @dataclasses.dataclass
    class BITMAPINFO:
        bmiHeader: Structure.BITMAPINFOHEADER = None
        # noinspection PyTypeChecker
        bmiColors: Structure.RGBQUAD * 1 = None

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
    close_handle: typing.Callable[[Type.HANDLE],
                                  Type.BOOL] = ctypes.windll.kernel32.CloseHandle

    delete_object: typing.Callable[[Type.HGDIOBJ],
                                   Type.BOOL] = ctypes.windll.gdi32.DeleteObject
    get_object: typing.Callable[[Type.HANDLE, Type.INT, Type.LPVOID],
                                Type.INT] = ctypes.windll.gdi32.GetObjectW

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
    load_image: typing.Callable[[Type.HINSTANCE, Type.LPCWSTR, Type.UINT, Type.INT, Type.INT, Type.UINT],
                                Type.HANDLE] = ctypes.windll.user32.LoadImageW
    get_DC: typing.Callable[[typing.Optional[Type.HWND]],
                            Type.HDC] = ctypes.windll.user32.GetDC
    release_DC: typing.Callable[[typing.Optional[Type.HWND], Type.HDC],
                                Type.INT] = ctypes.windll.user32.ReleaseDC

    gdiplus_startup: typing.Callable[[Pointer[Type.ULONG_PTR], Pointer[Structure.GdiplusStartupInput],
                                      typing.Optional[Pointer[Structure.GdiplusStartupInput]]],
                                     Type.Status] = ctypes.windll.gdiplus.GdiplusStartup
    gdiplus_shutdown: typing.Callable[[Type.ULONG_PTR],
                                      Type.VOID] = ctypes.windll.gdiplus.GdiplusShutdown
    gdip_create_bitmap_from_file: typing.Callable[[Pointer[Type.WCHAR], Pointer[Type.GpBitmap]],
                                                  Type.GpStatus] = ctypes.windll.gdiplus.GdipCreateBitmapFromFile
    gdip_dispose_image: typing.Callable[[Type.GpImage],
                                        Type.GpStatus] = ctypes.windll.gdiplus.GdipDisposeImage
    gdip_create_HBITMAP_from_bitmap: typing.Callable[[Type.GpBitmap, Pointer[Type.HBITMAP], Type.ARGB],
                                                     Type.GpStatus] = ctypes.windll.gdiplus.GdipCreateHBITMAPFromBitmap

    sh_get_folder_path: typing.Callable[[typing.Optional[Type.HWND], Type.INT,
                                         typing.Optional[Type.HANDLE], Type.DWORD, Type.LPWSTR],
                                        Type.HRESULT] = ctypes.windll.shell32.SHGetFolderPathW

    get_DI_bits: typing.Callable[[Type.HDC, Type.HBITMAP, Type.UINT, Type.UINT,
                                  typing.Optional[Type.LPVOID], Pointer[Structure.BITMAPINFO], Type.UINT],
                                 Type.INT] = ctypes.windll.gdi32.GetDIBits
    create_DI_bitmap: typing.Callable[[Type.HDC, Pointer[Structure.BITMAPINFOHEADER], Type.DWORD,
                                       Type.VOID, Pointer[Structure.BITMAPINFO], Type.UINT],
                                      Type.HBITMAP] = ctypes.windll.gdi32.CreateDIBitmap


def array(type_: _CT = Type.c_void_p,
          *elements: typing.Any,
          size: typing.Optional[int] = None) -> Pointer[_CT]:
    return (type_ * (size or len(elements)))(*elements)


def byref(obj: _CT) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.byref(obj)


def cast(obj: Pointer,
         type_: Pointer[_CT]) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.cast(obj, type_)


def sizeof(obj: _CT) -> int:
    return ctypes.sizeof(obj)


def char_array(obj: str,
               type_: _CT = Type.c_wchar) -> Pointer[_CT]:
    return (type_ * (len(obj) + 1))(*obj)


_init()
