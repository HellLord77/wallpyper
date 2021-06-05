import ctypes
import ctypes.wintypes
import dataclasses
import typing


def _is_dunder(name: str) -> bool:
    return name.startswith('__') and name.endswith('__')


def _is_union(obj: typing.Any) -> bool:
    # noinspection PyProtectedMember,PyUnresolvedReferences
    return isinstance(obj, typing._UnionGenericAlias)


def byref(var) -> ctypes.pointer:
    # noinspection PyTypeChecker
    return ctypes.byref(var)


def pointer(type_: ctypes):
    return ctypes.POINTER(type_)


class _Type:
    def __init_subclass__(cls):
        for var, value in cls.__dict__.items():
            if not _is_dunder(var) and _is_union(value):
                setattr(cls, var, value.__args__[0])


class Type(_Type):
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

    GpBitmap = c_void_p
    GpImage = c_void_p
    PVOID = c_void_p
    HBITMAP = HANDLE
    HGDIOBJ = HANDLE
    HGLOBAL = HANDLE
    HINSTANCE = HANDLE
    HWND = HANDLE
    ULONG_PTR = c_ulong
    SIZE_T = ULONG_PTR
    ARGB = DWORD
    GpStatus = HRESULT


class _Structure:
    def __init_subclass__(cls):
        for var, value in cls.__dict__.items():
            if not _is_dunder(var):
                class Class(ctypes.Structure):
                    _fields_ = tuple(value.__annotations__.items())
                    _defaults_ = {var_: getattr(value, var_) for var_ in value.__annotations__}

                    def __init__(self, *args, **kwargs):
                        iter_ = iter(self._defaults_)
                        for i in range(len(args)):
                            kwargs[next(iter_)] = args[i]
                        super().__init__(**dict(self._defaults_, **kwargs))

                    def __str__(self):
                        return str({var_: getattr(self, var_) for var_, _ in self._fields_})

                setattr(cls, var, Class)


class Structure(_Structure):
    @dataclasses.dataclass
    class GdiplusStartupInput:
        GdiplusVersion: Type.c_uint32 = 1
        DebugEventCallback: Type.c_void_p = None
        SuppressBackgroundThread: Type.c_void_p = False
        SuppressExternalCodecs: Type.BOOL = False

    @dataclasses.dataclass
    class BITMAPINFOHEADER(ctypes.Structure):
        biSize: Type.DWORD = None
        biWidth: Type.LONG = None
        biHeight: Type.LONG = None
        biPlanes: Type.WORD = None


class _Function:
    def __init_subclass__(cls):
        for var, value in cls.__dict__.items():
            if not _is_dunder(var):
                *value.argtypes, value.restype = (arg.__args__[0] if _is_union(arg) else arg
                                                  for arg in cls.__annotations__[var].__args__)


class Function(_Function):
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
