from __future__ import annotations  # TODO: remove if >= 3.10

__version__ = '0.0.1'

import ctypes
import ctypes.wintypes
import dataclasses
import functools
import typing

_CT = typing.TypeVar('_CT')


def _items(cls: type) -> typing.Generator[dict[str, typing.Any], None, None]:
    for name, val in cls.__dict__.items():
        if not name.startswith('_'):
            yield name, val


def _resolve_type(obj):
    # noinspection PyProtectedMember,PyUnresolvedReferences
    if isinstance(obj, typing._UnionGenericAlias):
        obj = typing.get_args(obj)[0]
    # noinspection PyProtectedMember,PyUnresolvedReferences
    return ctypes.POINTER(typing.get_args(obj)[0]) if isinstance(obj, typing._GenericAlias) else obj


def _init():
    for var, type_ in _items(Type):
        setattr(Type, var, _resolve_type(type_))

    for var, struct in _items(Struct):
        class Wrapper(ctypes.Structure):
            _fields_ = tuple(typing.get_type_hints(struct).items())
            _defaults = {field: getattr(struct, field) or type_() for field, type_ in _fields_}

            def __init__(self, *args, **kwargs):
                for i, var_ in enumerate(self._defaults):
                    if i >= len(args) and var_ not in kwargs:
                        kwargs[var_] = self._defaults[var_]
                super().__init__(*args, **kwargs)

            __repr__ = struct.__repr__

        functools.update_wrapper(Wrapper, struct, updated=())
        setattr(Struct, var, Wrapper)

    # TODO: Vtbl

    types = typing.get_type_hints(Func)
    for var, func in _items(Func):
        types_ = typing.get_args(types[var])
        func.argtypes = (_resolve_type(type_) for type_ in types_[0])
        func.restype = _resolve_type(types_[1])


class Const:
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

    CLSCTX_INPROC_SERVER = 1
    CLSCTX_INPROC_HANDLER = 2
    CLSCTX_LOCAL_SERVER = 4
    CLSCTX_REMOTE_SERVER = 16

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
    c_ubyte = typing.Union[ctypes.c_ubyte, int]
    c_void_p = typing.Union[ctypes.c_void_p, ctypes.c_wchar_p, int, str]
    c_char_p = typing.Union[ctypes.c_char_p, str]
    c_wchar_p = typing.Union[ctypes.c_wchar_p, str]
    c_int = typing.Union[ctypes.c_int, int]
    c_uint = typing.Union[ctypes.c_uint, int]
    c_uint32 = typing.Union[ctypes.c_uint32, int]
    c_short = typing.Union[ctypes.c_short, int]
    c_ushort = typing.Union[ctypes.c_ushort, int]
    c_long = typing.Union[ctypes.c_long, int]
    c_ulong = typing.Union[ctypes.c_ulong, int]
    size_t = typing.Union[ctypes.c_size_t, int]
    c_wchar = typing.Union[ctypes.c_wchar, str]
    HRESULT = typing.Union[ctypes.HRESULT, int]

    c_uchar = c_ubyte

    BOOL = c_long
    BYTE = c_byte
    DWORD = c_ulong
    HANDLE = c_void_p
    INT = c_int
    LONG = c_long
    LPCOLESTR = c_wchar_p
    LPCWSTR = c_wchar_p
    LPVOID = c_void_p
    LPWSTR = c_wchar_p
    UCHAR = c_uchar
    UINT = c_uint
    ULONG = c_ulong
    WCHAR = c_wchar
    WORD = c_ushort

    LPUNKNOWN = c_void_p  # Pointer[IUnknown]
    REFCLSID = c_void_p  # Pointer[CLSID]
    REFGUID = c_void_p  # Pointer[GUID]
    REFIID = c_void_p  # Pointer[IID]

    DebugEventProc = c_void_p  # DebugEventProc
    GpBitmap = c_void_p  # GpBitmap
    GpImage = c_void_p  # GpImage
    IFileDialog = c_void_p  # IFileDialog
    IUnknown = c_void_p  # IUnknown

    VOID = c_void_p
    PVOID = c_void_p
    PCWSTR = c_wchar_p
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
    Status = HRESULT
    GpStatus = Status


class Struct:
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
        bmiHeader: Struct.BITMAPINFOHEADER = None
        # noinspection PyTypeChecker
        bmiColors: Struct.RGBQUAD * 1 = None

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
        dsBm: Struct.BITMAP = None
        dsBmih: Struct.BITMAPINFOHEADER = None
        dsBitfields: Type.DWORD * 3 = None
        dshSection: Type.HANDLE = None
        dsOffset: Type.DWORD = None

    @dataclasses.dataclass
    class GUID:
        Data1: Type.c_ulong = None
        Data2: Type.c_ushort = None
        Data3: Type.c_ushort = None
        Data4: Type.c_uchar * 8 = None

    UUID = GUID
    IID = GUID
    CLSID = GUID


class Vtbl:
    class IFileDialogVtbl:
        QueryInterface: typing.Callable[[Type.IFileDialog, Pointer[Struct.IID], Type.c_void_p], Type.HRESULT]
        AddRef: typing.Callable[[Type.IFileDialog], Type.ULONG]
        Release: typing.Callable[[Type.IFileDialog], Type.ULONG]
        Show: typing.Callable[[Type.IFileDialog, Type.HWND], Type.HRESULT]
        SetFileTypes: typing.Callable[[], None]
        SetFileTypeIndex: typing.Callable[[Type.IFileDialog, Type.UINT], Type.HRESULT]
        GetFileTypeIndex: typing.Callable[[Type.IFileDialog, Type.UINT], Type.HRESULT]
        Advise: typing.Callable[[], None]
        Unadvise: typing.Callable[[], None]
        SetOptions: typing.Callable[[], None]
        GetOptions: typing.Callable[[], None]
        SetDefaultFolder: typing.Callable[[], None]
        SetFolder: typing.Callable[[], None]
        GetFolder: typing.Callable[[], None]
        GetCurrentSelection: typing.Callable[[], None]
        SetFileName: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        GetFileName: typing.Callable[[Type.IFileDialog, Type.LPWSTR], Type.HRESULT]
        SetTitle: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        SetOkButtonLabel: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        SetFileNameLabel: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        GetResult: typing.Callable[[], None]
        AddPlace: typing.Callable[[], None]
        SetDefaultExtension: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        Close: typing.Callable[[Type.IFileDialog, Type.HRESULT], Type.HRESULT]
        SetClientGuid: typing.Callable[[Type.IFileDialog, Pointer[Struct.GUID]], Type.HRESULT]
        ClearClientData: typing.Callable[[Type.IFileDialog], Type.HRESULT]
        SetFilter: typing.Callable[[], None]


class Func:
    rtl_are_long_paths_enabled: typing.Callable[[],
                                                Type.c_ubyte] = ctypes.windll.ntdll.RtlAreLongPathsEnabled

    global_alloc: typing.Callable[[Type.UINT, Type.SIZE_T],
                                  Type.HGLOBAL] = ctypes.windll.kernel32.GlobalAlloc
    global_lock: typing.Callable[[Type.HGLOBAL],
                                 Type.LPVOID] = ctypes.windll.kernel32.GlobalLock
    global_unlock: typing.Callable[[Type.HGLOBAL],
                                   Type.BOOL] = ctypes.windll.kernel32.GlobalUnlock
    close_handle: typing.Callable[[Type.HANDLE],
                                  Type.BOOL] = ctypes.windll.kernel32.CloseHandle

    get_object: typing.Callable[[Type.HANDLE, Type.INT, Type.LPVOID],
                                Type.INT] = ctypes.windll.gdi32.GetObjectW
    delete_object: typing.Callable[[Type.HGDIOBJ],
                                   Type.BOOL] = ctypes.windll.gdi32.DeleteObject
    create_DI_bitmap: typing.Callable[[Type.HDC, Pointer[Struct.BITMAPINFOHEADER], Type.DWORD,
                                       Type.VOID, Pointer[Struct.BITMAPINFO], Type.UINT],
                                      Type.HBITMAP] = ctypes.windll.gdi32.CreateDIBitmap
    get_DI_bits: typing.Callable[[Type.HDC, Type.HBITMAP, Type.UINT, Type.UINT,
                                  typing.Optional[Type.LPVOID], Pointer[Struct.BITMAPINFO], Type.UINT],
                                 Type.INT] = ctypes.windll.gdi32.GetDIBits

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

    memmove: typing.Callable[[Type.c_void_p, Type.c_void_p, Type.size_t],
                             Type.c_void_p] = ctypes.cdll.msvcrt.memmove
    wcslen: typing.Callable[[Type.c_wchar_p],
                            Type.size_t] = ctypes.cdll.msvcrt.wcslen

    gdiplus_startup: typing.Callable[[Pointer[Type.ULONG_PTR], Pointer[Struct.GdiplusStartupInput],
                                      typing.Optional[Pointer[Struct.GdiplusStartupInput]]],
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

    IID_from_string: typing.Callable[[Type.LPCOLESTR, Pointer[Struct.IID]],
                                     Type.HRESULT] = ctypes.windll.ole32.IIDFromString
    CLSID_from_string: typing.Callable[[Type.LPCOLESTR, Pointer[Struct.CLSID]],
                                       Type.HRESULT] = ctypes.windll.ole32.CLSIDFromString
    co_initialize: typing.Callable[[typing.Optional[Type.LPVOID]],
                                   Type.HRESULT] = ctypes.windll.ole32.CoInitialize
    co_uninitialize: typing.Callable[[],
                                     Type.VOID] = ctypes.windll.ole32.CoUninitialize
    co_create_instance: typing.Callable[[Pointer[Struct.CLSID], typing.Optional[Pointer[Type.IUnknown]],
                                         Type.DWORD, Pointer[Struct.IID], Type.LPVOID],
                                        Type.HRESULT] = ctypes.windll.ole32.CoCreateInstance


def pointer(type_: _CT) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.POINTER(type_)


def byref(obj: _CT) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.byref(obj)


def cast(obj: Pointer,
         type_: typing.Union[Pointer[_CT], type]) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.cast(obj, type_ if not issubclass(
        type_, ctypes.Structure) and hasattr(type_, 'from_param') else ctypes.POINTER(type_))


def sizeof(obj: _CT) -> int:
    return ctypes.sizeof(obj)


def array(type_: _CT = Type.c_void_p,
          *elements: typing.Any,
          size: typing.Optional[int] = None) -> Pointer[_CT]:
    return (type_ * (size or len(elements)))(*elements)


def char_array(obj: str,
               type_: _CT = Type.c_wchar) -> Pointer[_CT]:
    return (type_ * (len(obj) + 1))(*obj)


_init()
