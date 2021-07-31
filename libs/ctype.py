from __future__ import annotations  # TODO: remove if >= 3.10

__version__ = '0.0.3'  # TODO: separate nt

import ctypes
import dataclasses
import functools
import typing


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

    CLSID_ActiveDesktop = 1963230976, 61215, 4560, (152, 136, 0, 96, 151, 222, 172, 249)
    CLSID_FileOpenDialog = 3692845724, 59530, 19934, (165, 161, 96, 248, 42, 32, 174, 247)

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

    IID_IActiveDesktop = 4103138048, 4672, 4561, (152, 136, 0, 96, 151, 222, 172, 249)
    IID_IFileDialog = 1123569974, 56190, 17308, (133, 241, 228, 7, 93, 19, 95, 200)

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


_CT = typing.TypeVar('_CT')


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


class COM:
    class IUnknown:
        QueryInterface: typing.Callable[[Type.IUnknown, Pointer[Struct.IID], Type.c_void_p], Type.HRESULT]
        AddRef: typing.Callable[[Type.IUnknown], Type.ULONG]
        Release: typing.Callable[[Type.IUnknown], Type.ULONG]

    class IActiveDesktop(IUnknown):
        ApplyChanges: typing.Callable[[Type.IActiveDesktop, Type.DWORD], Type.HRESULT]
        GetWallpaper: typing.Callable[[Type.IActiveDesktop, Type.PWSTR, Type.UINT, Type.DWORD], Type.HRESULT]
        SetWallpaper: typing.Callable[[Type.IActiveDesktop, Type.PCWSTR, Type.DWORD], Type.HRESULT]
        GetWallpaperOptions: typing.Callable[[Type.IActiveDesktop, Type.LPWALLPAPEROPT, Type.DWORD], Type.HRESULT]
        SetWallpaperOptions: typing.Callable[[Type.IActiveDesktop, Type.LPWALLPAPEROPT, Type.DWORD], Type.HRESULT]
        GetPattern: typing.Callable[[Type.IActiveDesktop, Type.PWSTR, Type.UINT, Type.DWORD], Type.HRESULT]
        SetPattern: typing.Callable[[Type.IActiveDesktop, Type.PCWSTR, Type.DWORD], Type.HRESULT]
        GetDesktopItemOptions: typing.Callable
        SetDesktopItemOptions: typing.Callable
        AddDesktopItem: typing.Callable
        AddDesktopItemWithUI: typing.Callable
        ModifyDesktopItem: typing.Callable
        RemoveDesktopItem: typing.Callable
        GetDesktopItemCount: typing.Callable[[Type.IActiveDesktop, Pointer[Type.c_int], Type.DWORD], Type.HRESULT]
        GetDesktopItem: typing.Callable
        GetDesktopItemByID: typing.Callable
        GenerateDesktopItemHtml: typing.Callable
        AddUrl: typing.Callable
        GetDesktopItemBySource: typing.Callable

    class IFileDialog(IUnknown):
        Show: typing.Callable[[Type.IFileDialog, Type.HWND], Type.HRESULT]
        SetFileTypes: typing.Callable
        SetFileTypeIndex: typing.Callable[[Type.IFileDialog, Type.UINT], Type.HRESULT]
        GetFileTypeIndex: typing.Callable[[Type.IFileDialog, Type.UINT], Type.HRESULT]
        Advise: typing.Callable
        Unadvise: typing.Callable
        SetOptions: typing.Callable
        GetOptions: typing.Callable
        SetDefaultFolder: typing.Callable
        SetFolder: typing.Callable
        GetFolder: typing.Callable
        GetCurrentSelection: typing.Callable
        SetFileName: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        GetFileName: typing.Callable[[Type.IFileDialog, Type.LPWSTR], Type.HRESULT]
        SetTitle: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        SetOkButtonLabel: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        SetFileNameLabel: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        GetResult: typing.Callable
        AddPlace: typing.Callable
        SetDefaultExtension: typing.Callable[[Type.IFileDialog, Type.LPCWSTR], Type.HRESULT]
        Close: typing.Callable[[Type.IFileDialog, Type.HRESULT], Type.HRESULT]
        SetClientGuid: typing.Callable[[Type.IFileDialog, Pointer[Struct.GUID]], Type.HRESULT]
        ClearClientData: typing.Callable[[Type.IFileDialog], Type.HRESULT]
        SetFilter: typing.Callable


class _Lib:
    def __init_subclass__(cls):
        for var, type_ in typing.get_type_hints(cls).items():
            setattr(cls, var, type_(var))


class Lib(_Lib):
    gdi32: ctypes.WinDLL
    gdiplus: ctypes.WinDLL
    kernel32: ctypes.WinDLL
    msvcrt: ctypes.WinDLL
    ntdll: ctypes.WinDLL
    ole32: ctypes.WinDLL
    shell32: ctypes.WinDLL
    user32: ctypes.WinDLL


class Func:
    RtlAreLongPathsEnabled: typing.Callable[[],
                                            Type.c_ubyte] = Lib.ntdll.RtlAreLongPathsEnabled

    GlobalAlloc: typing.Callable[[Type.UINT, Type.SIZE_T],
                                 Type.HGLOBAL] = Lib.kernel32.GlobalAlloc
    GlobalLock: typing.Callable[[Type.HGLOBAL],
                                Type.LPVOID] = Lib.kernel32.GlobalLock
    GlobalUnlock: typing.Callable[[Type.HGLOBAL],
                                  Type.BOOL] = Lib.kernel32.GlobalUnlock
    CloseHandle: typing.Callable[[Type.HANDLE],
                                 Type.BOOL] = Lib.kernel32.CloseHandle

    GetObject: typing.Callable[[Type.HANDLE, Type.INT, Type.LPVOID],
                               Type.INT] = Lib.gdi32.GetObjectW
    DeleteObject: typing.Callable[[Type.HGDIOBJ],
                                  Type.BOOL] = Lib.gdi32.DeleteObject
    CreateDIBitmap: typing.Callable[[Type.HDC, Pointer[Struct.BITMAPINFOHEADER], Type.DWORD,
                                     Type.VOID, Pointer[Struct.BITMAPINFO], Type.UINT],
                                    Type.HBITMAP] = Lib.gdi32.CreateDIBitmap
    GetDIBits: typing.Callable[[Type.HDC, Type.HBITMAP, Type.UINT, Type.UINT,
                                typing.Optional[Type.LPVOID], Pointer[Struct.BITMAPINFO], Type.UINT],
                               Type.INT] = Lib.gdi32.GetDIBits

    SystemParametersInfo: typing.Callable[[Type.UINT, Type.UINT, Type.PVOID, Type.UINT],
                                          Type.BOOL] = Lib.user32.SystemParametersInfoW
    OpenClipboard: typing.Callable[[typing.Optional[Type.HWND]],
                                   Type.BOOL] = Lib.user32.OpenClipboard
    CloseClipboard: typing.Callable[[],
                                    Type.BOOL] = Lib.user32.CloseClipboard
    EmptyClipboard: typing.Callable[[],
                                    Type.BOOL] = Lib.user32.EmptyClipboard
    GetClipboardData: typing.Callable[[Type.UINT],
                                      Type.HANDLE] = Lib.user32.GetClipboardData
    SetClipboardData: typing.Callable[[Type.UINT, Type.HANDLE],
                                      Type.HANDLE] = Lib.user32.SetClipboardData
    LoadImage: typing.Callable[[Type.HINSTANCE, Type.LPCWSTR, Type.UINT, Type.INT, Type.INT, Type.UINT],
                               Type.HANDLE] = Lib.user32.LoadImageW
    GetDC: typing.Callable[[typing.Optional[Type.HWND]],
                           Type.HDC] = Lib.user32.GetDC
    ReleaseDC: typing.Callable[[typing.Optional[Type.HWND], Type.HDC],
                               Type.INT] = Lib.user32.ReleaseDC

    IIDFromString: typing.Callable[[Type.LPCOLESTR, Pointer[Struct.IID]],
                                   Type.HRESULT] = Lib.ole32.IIDFromString
    CLSIDFromString: typing.Callable[[Type.LPCOLESTR, Pointer[Struct.CLSID]],
                                     Type.HRESULT] = Lib.ole32.CLSIDFromString
    CoInitialize: typing.Callable[[typing.Optional[Type.LPVOID]],
                                  Type.HRESULT] = Lib.ole32.CoInitialize
    CoUninitialize: typing.Callable[[],
                                    Type.VOID] = Lib.ole32.CoUninitialize
    CoCreateInstance: typing.Callable[[Pointer[Struct.CLSID], typing.Optional[Pointer[Type.IUnknown]],
                                       Type.DWORD, Pointer[Struct.IID], Type.LPVOID],
                                      Type.HRESULT] = Lib.ole32.CoCreateInstance

    memmove: typing.Callable[[Type.c_void_p, Type.c_void_p, Type.size_t],
                             Type.c_void_p] = Lib.msvcrt.memmove
    wcslen: typing.Callable[[Type.c_wchar_p],
                            Type.size_t] = Lib.msvcrt.wcslen

    GdiplusStartup: typing.Callable[[Pointer[Type.ULONG_PTR], Pointer[Struct.GdiplusStartupInput],
                                     typing.Optional[Pointer[Struct.GdiplusStartupInput]]],
                                    Type.Status] = Lib.gdiplus.GdiplusStartup
    GdiplusShutdown: typing.Callable[[Type.ULONG_PTR],
                                     Type.VOID] = Lib.gdiplus.GdiplusShutdown
    GdipCreateBitmapFromFile: typing.Callable[[Pointer[Type.WCHAR], Pointer[Type.GpBitmap]],
                                              Type.GpStatus] = Lib.gdiplus.GdipCreateBitmapFromFile
    GdipDisposeImage: typing.Callable[[Type.GpImage],
                                      Type.GpStatus] = Lib.gdiplus.GdipDisposeImage
    GdipCreateHBITMAPFromBitmap: typing.Callable[[Type.GpBitmap, Pointer[Type.HBITMAP], Type.ARGB],
                                                 Type.GpStatus] = Lib.gdiplus.GdipCreateHBITMAPFromBitmap

    SHGetFolderPath: typing.Callable[[typing.Optional[Type.HWND], Type.INT,
                                      typing.Optional[Type.HANDLE], Type.DWORD, Type.LPWSTR],
                                     Type.HRESULT] = Lib.shell32.SHGetFolderPathW


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


def _items(cls: type) -> typing.Generator[dict[str, typing.Any], None, None]:
    for name, val in cls.__dict__.items():
        if not name.startswith('_'):
            yield name, val


def _resolve_type(type_):
    # noinspection PyUnresolvedReferences,PyProtectedMember
    if isinstance(type_, typing._CallableType):
        return None,
    elif isinstance(type_, typing._CallableGenericAlias):
        types = typing.get_args(type_)
        return (_resolve_type(types[1]),) + tuple(_resolve_type(type_) for type_ in types[0])
    # noinspection PyProtectedMember,PyUnresolvedReferences
    if isinstance(type_, typing._UnionGenericAlias):
        type_ = typing.get_args(type_)[0]
    i = 0
    # noinspection PyProtectedMember,PyUnresolvedReferences
    while isinstance(type_, typing._GenericAlias):
        type_ = typing.get_args(type_)[0]
        i += 1
    for _ in range(i):
        type_ = ctypes.POINTER(type_)
    return type_


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

    for var, com in _items(COM):
        class Wrapper(ctypes.c_void_p):
            _base = type('', (ctypes.Structure,), {'_fields_': tuple(
                (func, ctypes.CFUNCTYPE(*_resolve_type(types))) for func, types in typing.get_type_hints(com).items())})
            _funcs = tuple(func for func, _ in _items(_base))

            def __getattr__(self, item):
                if item in self._funcs:
                    # noinspection PyTypeChecker
                    funcs = ctypes.cast(ctypes.cast(self, ctypes.POINTER(ctypes.c_void_p)).contents.value,
                                        ctypes.POINTER(self._base)).contents
                    for func_ in self._funcs:
                        setattr(self, func_, getattr(funcs, func_))
                return getattr(self, item)

        functools.update_wrapper(Wrapper, com, updated=())
        setattr(COM, var, Wrapper)

    types = typing.get_type_hints(Func)
    for var, func in _items(Func):
        func.restype, *func.argtypes = _resolve_type(types[var])


_init()
