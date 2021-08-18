from __future__ import annotations  # TODO: remove if >= 3.11

__version__ = '0.0.4'

import contextlib
import ctypes
import dataclasses
import functools
import types
import typing
from typing import Any, Callable, ContextManager, Generator, Generic, Optional, TypeVar, Union

_CT = TypeVar('_CT')


class Const:
    AD_APPLY_SAVE = 1
    AD_APPLY_HTMLGEN = 2
    AD_APPLY_REFRESH = 4
    AD_APPLY_ALL = 7
    AD_APPLY_FORCE = 8
    AD_APPLY_BUFFERED_REFRESH = 16
    AD_APPLY_DYNAMICREFRESH = 32

    AD_GETWP_BMP = 0
    AD_GETWP_IMAGE = 1
    AD_GETWP_LAST_APPLIED = 2

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

    CLSID_ActiveDesktop = '{75048700-EF1F-11D0-9888-006097DEACF9}'
    CLSID_DesktopWallpaper = '{C2CF3110-460E-4fc1-B9D0-8A1C0C9CC4BD}'
    CLSID_FileOpenDialog = '{DC1C5A9C-E88A-4DDE-A5A1-60F82A20AEF7}'

    CSIDL_APPDATA = 26
    CSIDL_LOCAL_APPDATA = 28
    CSIDL_MYPICTURES = 39

    DIB_PAL_COLORS = 1
    DIB_PAL_INDICES = 2
    DIB_RGB_COLORS = 0

    DSD_FORWARD = 0
    DSD_BACKWARD = 1

    DSO_SHUFFLEIMAGES = 1

    DSS_ENABLED = 1
    DSS_SLIDESHOW = 2
    DSS_DISABLED_BY_REMOTE_SESSION = 4

    DWPOS_CENTER = 0
    DWPOS_TILE = 1
    DWPOS_STRETCH = 2
    DWPOS_FIT = 3
    DWPOS_FILL = 4
    DWPOS_SPAN = 5

    GHND = 66
    GMEM_FIXED = 0
    GMEM_MOVEABLE = 2
    GMEM_ZEROINIT = 64
    GPTR = 64

    IID_IUnknown = '{00000000-0000-0000-C000-000000000046}'
    IID_IActiveDesktop = '{F490EB00-1240-11D1-9888-006097DEACF9}'
    IID_IDesktopWallpaper = '{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}'
    IID_IModalWindow = '{B4DB1657-70D7-485E-8E3E-6FCB5A5C1802}'
    IID_IFileDialog = '{42F85136-DB7E-439C-85F1-E4075D135FC8}'
    IID_IFileOpenDialog = '{D57C7288-D4AD-4768-BE02-9D969532D960}'

    IS_NORMAL = 1
    IS_FULLSCREEN = 2
    IS_SPLIT = 4

    SHGFP_TYPE_CURRENT = 0
    SHGFP_TYPE_DEFAULT = 1

    SPI_GETDESKWALLPAPER = 115
    SPI_SETDESKWALLPAPER = 20

    SPIF_NONE = 0
    SPIF_SENDCHANGE = 2
    SPIF_SENDWININICHANGE = 2
    SPIF_UPDATEINIFILE = 1

    WPSTYLE_CENTER = 0
    WPSTYLE_TILE = 1
    WPSTYLE_STRETCH = 2
    WPSTYLE_KEEPASPECT = 3
    WPSTYLE_CROPTOFIT = 4
    WPSTYLE_SPAN = 5


class Pointer(Generic[_CT]):
    value = None

    # noinspection PyTypeChecker,PyUnusedLocal,PyUnresolvedReferences
    def __init__(self, type_: type[_CT]) -> type[Pointer[_CT]]:
        pass


class Type:
    c_byte = Union[ctypes.c_byte, int]
    c_ubyte = Union[ctypes.c_ubyte, int]
    c_void_p = Union[ctypes.c_void_p, Pointer]
    c_char_p = Union[ctypes.c_char_p, str]
    c_wchar_p = Union[ctypes.c_wchar_p, str]
    c_int = Union[ctypes.c_int, int]
    c_uint = Union[ctypes.c_uint, int]
    c_uint32 = Union[ctypes.c_uint32, int]
    c_short = Union[ctypes.c_short, int]
    c_ushort = Union[ctypes.c_ushort, int]
    c_long = Union[ctypes.c_long, int]
    c_ulong = Union[ctypes.c_ulong, int]
    size_t = Union[ctypes.c_size_t, int]
    c_wchar = Union[ctypes.c_wchar, str]
    HRESULT = Union[ctypes.HRESULT, int]

    c_uchar = c_ubyte

    BOOL = c_long
    BYTE = c_byte
    DWORD = c_ulong
    HANDLE = c_void_p
    INT = c_int
    LONG = c_long
    OLESTR = c_wchar_p
    LPOLESTR = c_wchar_p
    LPCOLESTR = c_wchar_p
    LPWSTR = c_wchar_p
    LPCWSTR = c_wchar_p
    LPSTR = c_char_p
    LPCSTR = c_char_p
    LPVOID = c_void_p
    LPCVOID = c_void_p
    UCHAR = c_uchar
    UINT = c_uint
    ULONG = c_ulong
    WCHAR = c_wchar
    WORD = c_ushort

    LPUNKNOWN = c_void_p  # Pointer[IUnknown]
    LPWALLPAPEROPT = c_void_p  # Pointer[WALLPAPEROPT]
    REFCLSID = c_void_p  # Pointer[CLSID]
    REFGUID = c_void_p  # Pointer[GUID]
    REFIID = c_void_p  # Pointer[IID]

    DebugEventProc = c_void_p  # DebugEventProc
    GpBitmap = c_void_p  # GpBitmap
    GpImage = c_void_p  # GpImage
    IActiveDesktop = c_void_p  # IActiveDesktop
    IFileDialog = c_void_p  # IFileDialog
    IUnknown = c_void_p  # IUnknown

    VOID = c_void_p
    PVOID = c_void_p
    PWSTR = c_wchar_p
    PCWSTR = c_wchar_p
    UINT32 = c_uint32
    enum = c_uint  # TODO: Enum type
    DESKTOP_SLIDESHOW_DIRECTION = enum
    DESKTOP_SLIDESHOW_OPTIONS = enum
    DESKTOP_SLIDESHOW_STATE = enum
    DESKTOP_WALLPAPER_POSITION = enum
    HBITMAP = HANDLE
    HDC = HANDLE
    HGDIOBJ = HANDLE
    HGLOBAL = HANDLE
    HINSTANCE = HANDLE
    HWND = HANDLE
    ULONG_PTR = c_ulong
    SIZE_T = ULONG_PTR
    ARGB = DWORD
    COLORREF = DWORD
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

    @dataclasses.dataclass
    class WALLPAPEROPT:
        dwSize: Type.DWORD = None
        dwStyle: Type.DWORD = None

    class UUID(GUID):
        pass

    class IID(GUID):
        pass

    class CLSID(GUID):
        pass

    class RECT:
        left: Type.LONG = None
        top: Type.LONG = None
        right: Type.LONG = None
        bottom: Type.LONG = None


class COM:
    class IUnknown:
        _CLSID = ''
        QueryInterface: Callable[[Pointer[Struct.IID], Type.c_void_p], Type.HRESULT]
        AddRef: Callable[[], Type.ULONG]
        Release: Callable[[], Type.ULONG]

    class IActiveDesktop(IUnknown):
        _CLSID = Const.CLSID_ActiveDesktop
        ApplyChanges: Callable[[Type.DWORD], Type.HRESULT]
        GetWallpaper: Callable[[Type.PWSTR, Type.UINT, Type.DWORD], Type.HRESULT]
        SetWallpaper: Callable[[Type.PCWSTR, Type.DWORD], Type.HRESULT]
        GetWallpaperOptions: Callable[[Type.LPWALLPAPEROPT, Type.DWORD], Type.HRESULT]
        SetWallpaperOptions: Callable[[Type.LPWALLPAPEROPT, Type.DWORD], Type.HRESULT]
        GetPattern: Callable[[Type.PWSTR, Type.UINT, Type.DWORD], Type.HRESULT]
        SetPattern: Callable[[Type.PCWSTR, Type.DWORD], Type.HRESULT]
        GetDesktopItemOptions: Callable
        SetDesktopItemOptions: Callable
        AddDesktopItem: Callable
        AddDesktopItemWithUI: Callable
        ModifyDesktopItem: Callable
        RemoveDesktopItem: Callable
        GetDesktopItemCount: Callable[[Pointer[Type.c_int], Type.DWORD], Type.HRESULT]
        GetDesktopItem: Callable
        GetDesktopItemByID: Callable
        GenerateDesktopItemHtml: Callable
        AddUrl: Callable
        GetDesktopItemBySource: Callable

    class IDesktopWallpaper(IUnknown):  # TODO: fix
        _CLSID = Const.CLSID_DesktopWallpaper
        SetWallpaper: Callable[[Type.LPCWSTR, Type.LPCWSTR], Type.HRESULT]
        GetWallpaper: Callable[[Type.LPCWSTR, Pointer[Type.LPWSTR]], Type.HRESULT]
        GetMonitorDevicePathAt: Callable[[Type.UINT, Pointer[Type.LPWSTR]], Type.HRESULT]
        GetMonitorDevicePathCount: Callable[[Pointer[Type.UINT]], Type.HRESULT]
        GetMonitorRECT: Callable[[Type.LPCWSTR, Pointer[Struct.RECT]], Type.HRESULT]
        SetBackgroundColor: Callable[[Type.COLORREF], Type.HRESULT]
        GetBackgroundColor: Callable[[Pointer[Type.COLORREF]], Type.HRESULT]
        SetPosition: Callable[[Type.DESKTOP_WALLPAPER_POSITION], Type.HRESULT]
        GetPosition: Callable[[Pointer[Type.DESKTOP_WALLPAPER_POSITION]], Type.HRESULT]
        SetSlideshow: Callable
        GetSlideshow: Callable
        SetSlideshowOptions: Callable[[Type.DESKTOP_SLIDESHOW_OPTIONS, Type.UINT], Type.HRESULT]
        GetSlideshowOptions: Callable[[Type.DESKTOP_SLIDESHOW_OPTIONS, Pointer[Type.UINT]], Type.HRESULT]
        AdvanceSlideshow: Callable[[Type.LPCWSTR, Type.DESKTOP_SLIDESHOW_DIRECTION], Type.HRESULT]
        GetStatus: Callable[[Pointer[Type.DESKTOP_SLIDESHOW_STATE]], Type.HRESULT]
        Enable: Callable[[Type.BOOL], Type.HRESULT]

    class IModalWindow(IUnknown):
        _CLSID = Const.CLSID_FileOpenDialog
        Show: Callable[[Type.HWND], Type.HRESULT]

    class IFileDialog(IModalWindow):
        SetFileTypes: Callable
        SetFileTypeIndex: Callable[[Type.UINT], Type.HRESULT]
        GetFileTypeIndex: Callable[[Type.UINT], Type.HRESULT]
        Advise: Callable
        Unadvise: Callable
        SetOptions: Callable
        GetOptions: Callable
        SetDefaultFolder: Callable
        SetFolder: Callable
        GetFolder: Callable
        GetCurrentSelection: Callable
        SetFileName: Callable[[Type.LPCWSTR], Type.HRESULT]
        GetFileName: Callable[[Type.LPWSTR], Type.HRESULT]
        SetTitle: Callable[[Type.LPCWSTR], Type.HRESULT]
        SetOkButtonLabel: Callable[[Type.LPCWSTR], Type.HRESULT]
        SetFileNameLabel: Callable[[Type.LPCWSTR], Type.HRESULT]
        GetResult: Callable
        AddPlace: Callable
        SetDefaultExtension: Callable[[Type.LPCWSTR], Type.HRESULT]
        Close: Callable[[Type.HRESULT], Type.HRESULT]
        SetClientGuid: Callable[[Pointer[Struct.GUID]], Type.HRESULT]
        ClearClientData: Callable[[], Type.HRESULT]
        SetFilter: Callable

    class IFileOpenDialog(IFileDialog):
        GetResults: Callable
        GetSelectedItems: Callable


class _Lib:
    def __init_subclass__(cls):
        for var, type_ in typing.get_type_hints(cls).items():
            setattr(cls, var, type_(var))


class Lib(_Lib):
    gdi32: ctypes.CDLL
    gdiplus: ctypes.CDLL
    kernel32: ctypes.CDLL
    msvcrt: ctypes.CDLL
    ntdll: ctypes.CDLL
    ole32: ctypes.CDLL
    shell32: ctypes.CDLL
    user32: ctypes.CDLL


class Func:
    RtlAreLongPathsEnabled: Callable[[],
                                     Type.c_ubyte] = Lib.ntdll.RtlAreLongPathsEnabled

    GlobalAlloc: Callable[[Type.UINT, Type.SIZE_T],
                          Type.HGLOBAL] = Lib.kernel32.GlobalAlloc
    GlobalLock: Callable[[Type.HGLOBAL],
                         Type.LPVOID] = Lib.kernel32.GlobalLock
    GlobalUnlock: Callable[[Type.HGLOBAL],
                           Type.BOOL] = Lib.kernel32.GlobalUnlock
    CloseHandle: Callable[[Type.HANDLE],
                          Type.BOOL] = Lib.kernel32.CloseHandle

    GetObject: Callable[[Type.HANDLE, Type.INT, Type.LPVOID],
                        Type.INT] = Lib.gdi32.GetObjectW
    DeleteObject: Callable[[Type.HGDIOBJ],
                           Type.BOOL] = Lib.gdi32.DeleteObject
    CreateDIBitmap: Callable[[Type.HDC, Pointer[Struct.BITMAPINFOHEADER], Type.DWORD,
                              Type.VOID, Pointer[Struct.BITMAPINFO], Type.UINT],
                             Type.HBITMAP] = Lib.gdi32.CreateDIBitmap
    GetDIBits: Callable[[Type.HDC, Type.HBITMAP, Type.UINT, Type.UINT,
                         Optional[Type.LPVOID], Pointer[Struct.BITMAPINFO], Type.UINT],
                        Type.INT] = Lib.gdi32.GetDIBits

    SystemParametersInfo: Callable[[Type.UINT, Type.UINT, Type.PVOID, Type.UINT],
                                   Type.BOOL] = Lib.user32.SystemParametersInfoW
    OpenClipboard: Callable[[Optional[Type.HWND]],
                            Type.BOOL] = Lib.user32.OpenClipboard
    CloseClipboard: Callable[[],
                             Type.BOOL] = Lib.user32.CloseClipboard
    EmptyClipboard: Callable[[],
                             Type.BOOL] = Lib.user32.EmptyClipboard
    GetClipboardData: Callable[[Type.UINT],
                               Type.HANDLE] = Lib.user32.GetClipboardData
    SetClipboardData: Callable[[Type.UINT, Type.HANDLE],
                               Type.HANDLE] = Lib.user32.SetClipboardData
    LoadImage: Callable[[Type.HINSTANCE, Type.LPCWSTR, Type.UINT, Type.INT, Type.INT, Type.UINT],
                        Type.HANDLE] = Lib.user32.LoadImageW
    GetDC: Callable[[Optional[Type.HWND]],
                    Type.HDC] = Lib.user32.GetDC
    ReleaseDC: Callable[[Optional[Type.HWND], Type.HDC],
                        Type.INT] = Lib.user32.ReleaseDC

    IIDFromString: Callable[[Type.LPCOLESTR, Pointer[Struct.IID]],
                            Type.HRESULT] = Lib.ole32.IIDFromString
    CLSIDFromString: Callable[[Type.LPCOLESTR, Pointer[Struct.CLSID]],
                              Type.HRESULT] = Lib.ole32.CLSIDFromString
    CoInitialize: Callable[[Optional[Type.LPVOID]],
                           Type.HRESULT] = Lib.ole32.CoInitialize
    CoUninitialize: Callable[[],
                             Type.VOID] = Lib.ole32.CoUninitialize
    CoCreateInstance: Callable[[Pointer[Struct.CLSID], Optional[Pointer[Type.IUnknown]],
                                Type.DWORD, Pointer[Struct.IID], Type.LPVOID],
                               Type.HRESULT] = Lib.ole32.CoCreateInstance
    StringFromCLSID: Callable[[Type.REFCLSID, Pointer[Type.LPOLESTR]],
                              Type.HRESULT] = Lib.ole32.StringFromCLSID

    memmove: Callable[[Type.c_void_p, Type.c_void_p, Type.size_t],
                      Type.c_void_p] = Lib.msvcrt.memmove
    wcslen: Callable[[Type.c_wchar_p],
                     Type.size_t] = Lib.msvcrt.wcslen

    GdiplusStartup: Callable[[Pointer[Type.ULONG_PTR], Pointer[Struct.GdiplusStartupInput],
                              Optional[Pointer[Struct.GdiplusStartupInput]]],
                             Type.Status] = Lib.gdiplus.GdiplusStartup
    GdiplusShutdown: Callable[[Type.ULONG_PTR],
                              Type.VOID] = Lib.gdiplus.GdiplusShutdown
    GdipCreateBitmapFromFile: Callable[[Pointer[Type.WCHAR], Pointer[Type.GpBitmap]],
                                       Type.GpStatus] = Lib.gdiplus.GdipCreateBitmapFromFile
    GdipDisposeImage: Callable[[Type.GpImage],
                               Type.GpStatus] = Lib.gdiplus.GdipDisposeImage
    GdipCreateHBITMAPFromBitmap: Callable[[Type.GpBitmap, Pointer[Type.HBITMAP], Type.ARGB],
                                          Type.GpStatus] = Lib.gdiplus.GdipCreateHBITMAPFromBitmap

    SHGetFolderPath: Callable[[Optional[Type.HWND], Type.INT,
                               Optional[Type.HANDLE], Type.DWORD, Type.LPWSTR],
                              Type.HRESULT] = Lib.shell32.SHGetFolderPathW


def pointer(type_: _CT) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.POINTER(type_)


def byref(obj: _CT) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.byref(obj)


def cast(obj: Pointer,
         type_: Union[Pointer[_CT], type]) -> Pointer[_CT]:
    # noinspection PyTypeChecker
    return ctypes.cast(obj, type_ if not issubclass(
        type_, ctypes.Structure) and hasattr(type_, 'from_param') else ctypes.POINTER(type_))


def sizeof(obj: _CT) -> int:
    return ctypes.sizeof(obj)


def array(type_: _CT = Type.c_void_p,
          *elements: Any,
          size: Optional[int] = None) -> Pointer[_CT]:
    return (type_ * (size or len(elements)))(*elements)


def char_array(obj: str,
               type_: _CT = Type.c_wchar) -> Pointer[_CT]:
    return (type_ * (len(obj) + 1))(*obj)


# noinspection PyUnresolvedReferences
@functools.cache
def _get_refs(type_: type[COM.IUnknown]) -> tuple[Pointer[Struct.CLSID], Pointer[Struct.IID]]:
    clsid_ref = byref(Struct.CLSID())
    # noinspection PyProtectedMember
    Func.CLSIDFromString(type_._CLSID, clsid_ref)
    iid_ref = byref(Struct.IID())
    Func.IIDFromString(getattr(Const, f'IID_{type_.__name__}'), iid_ref)
    return clsid_ref, iid_ref


# noinspection PyUnresolvedReferences
@contextlib.contextmanager
def com(type_: type[_CT]) -> ContextManager[_CT]:
    obj = type_()
    Func.CoInitialize(None)
    try:
        refs = _get_refs(type_)
        Func.CoCreateInstance(refs[0], None, Const.CLSCTX_INPROC_SERVER, refs[1], byref(obj))
        yield obj
    finally:
        if obj:
            obj.Release()
        Func.CoUninitialize()


def _items(cls: type) -> Generator[tuple[str, Any], None, None]:
    for var, val in vars(cls).items():
        if not var.startswith('_'):
            yield var, val


def _resolve_type(type_: Any) -> Any:
    if isinstance(type_, type(Callable)):
        type_ = [None]
    elif isinstance(type_, type(Callable[[], None])):
        types_ = typing.get_args(type_)
        type_ = [_resolve_type(types_[1])]
        type_.extend(_resolve_type(type_) for type_ in types_[0])
    else:
        if isinstance(type_, type(Optional[object])):
            type_ = typing.get_args(type_)[0]
        if typing.get_origin(type_) is Pointer:
            type_ = ctypes.POINTER(_resolve_type(typing.get_args(type_)[0]))
    return type_


def _method_type(types_: list) -> list:
    types_.insert(1, ctypes.c_void_p)
    return types_


def _init():
    for var, type_ in _items(Type):
        setattr(Type, var, _resolve_type(type_))

    for var, struct in _items(Struct):
        class Wrapper(ctypes.Structure):
            _fields_ = tuple((field, _resolve_type(type_)) for field, type_ in typing.get_type_hints(struct).items())
            _defaults = tuple((field, getattr(struct, field) or type_) for field, type_ in _fields_)

            def __init__(self, *args, **kwargs):
                for i, field in enumerate(self._defaults):
                    if i >= len(args) and field[0] not in kwargs:
                        kwargs[field[0]] = field[1]() if callable(field[1]) else field[1]
                super().__init__(*args, **kwargs)

        # noinspection PyUnresolvedReferences
        functools.update_wrapper(Wrapper, struct, functools.WRAPPER_ASSIGNMENTS + ('__repr__',), ())
        setattr(Struct, var, Wrapper)

    for var, com_ in _items(COM):
        class Wrapper(ctypes.c_void_p):
            # noinspection PyProtectedMember
            _CLSID = com_._CLSID
            # noinspection PyTypeChecker
            _pointer = ctypes.POINTER(type(var, (ctypes.Structure,), {'_fields_': tuple((func, ctypes.CFUNCTYPE(
                *_method_type(_resolve_type(types)))) for func, types in typing.get_type_hints(com_).items())}))
            # noinspection PyProtectedMember
            _methods = tuple(types[0] for types in _items(_pointer._type_))

            def __getattr__(self, name):
                if name in self._methods:
                    funcs = ctypes.cast(ctypes.cast(self, ctypes.POINTER(
                        ctypes.c_void_p)).contents.value, self._pointer).contents
                    for method in self._methods:
                        setattr(self, method, types.MethodType(getattr(funcs, method), self))
                return super().__getattribute__(name)

        functools.update_wrapper(Wrapper, com_, updated=())
        setattr(COM, var, Wrapper)

    types_ = typing.get_type_hints(Func)
    for var, func in _items(Func):
        func.restype, *func.argtypes = _resolve_type(types_[var])


_init()
