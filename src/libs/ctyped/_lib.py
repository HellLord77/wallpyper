import ctypes as _ctypes
import typing as _typing
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _com
from . import _struct
from . import _type
from .__head__ import _DEBUG
from .__head__ import _Pointer
from .__head__ import _get_doc
from .__head__ import _not_internal
from .__head__ import _resolve_type


class _CDLL(type):
    pass


class _OleDLL(_CDLL):
    pass


class _WinDLL(_CDLL):
    pass


# noinspection PyPep8Naming
class uxtheme(metaclass=_WinDLL):
    SetWindowTheme: _Callable[[_type.HWND, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR]],
                              _type.HRESULT]


# noinspection PyPep8Naming
class combase(metaclass=_WinDLL):
    RoActivateInstance: _Callable[[_type.HSTRING, _type.c_void_p],
                                  _type.HRESULT]
    RoInitialize: _Callable[[_type.RO_INIT_TYPE],
                            _type.HRESULT]
    RoUninitialize: _Callable[[],
                              _type.c_void_p]
    WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH], _type.UINT32, _Pointer[_type.HSTRING]],
                                   _type.HRESULT]
    WindowsDeleteString: _Callable[[_type.HSTRING],
                                   _type.HRESULT]


# noinspection PyPep8Naming
class gdi32(metaclass=_WinDLL):
    CreateDIBitmap: _Callable[[_type.HDC, _Pointer[_struct.BITMAPINFOHEADER], _type.DWORD,
                               _type.VOID, _Pointer[_struct.BITMAPINFO], _type.UINT],
                              _type.HBITMAP]
    CreateSolidBrush: _Callable[[_type.COLORREF],
                                _type.HBRUSH]
    DeleteObject: _Callable[[_type.HGDIOBJ],
                            _type.BOOL]
    GetDIBits: _Callable[[_type.HDC, _type.HBITMAP, _type.UINT, _type.UINT,
                          _Optional[_type.LPVOID], _Pointer[_struct.BITMAPINFO], _type.UINT],
                         _type.c_int]
    GetObjectA: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                          _type.c_int]
    GetObjectW: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                          _type.c_int]
    GetStockObject: _Callable[[_type.c_int],
                              _type.HGDIOBJ]


class GdiPlus(metaclass=_WinDLL):
    GdipCreateBitmapFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpBitmap]],
                                        _type.GpStatus]
    GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HBITMAP], _type.ARGB],
                                           _type.GpStatus]
    GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HICON]],
                                         _type.GpStatus]
    GdipDisposeImage: _Callable[[_type.GpImage],
                                _type.GpStatus]
    GdipGetPropertyItem: _Callable[[_type.GpImage, _type.PROPID,
                                    _type.UINT, _Pointer[_struct.PropertyItem]],
                                   _type.GpStatus]
    GdipGetPropertyItemSize: _Callable[[_type.GpImage, _type.PROPID, _Pointer[_type.UINT]],
                                       _type.GpStatus]
    GdipImageGetFrameCount: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _Pointer[_type.UINT]],
                                      _type.GpStatus]
    GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage, _Pointer[_type.UINT]],
                                                _type.GpStatus]
    GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                               _type.GpStatus]
    GdipImageSelectActiveFrame: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                          _type.GpStatus]
    GdipLoadImageFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpImage]],
                                     _type.GpStatus]
    GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                               _type.VOID]
    GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],
                               _Pointer[_struct.GdiplusStartupInput], _Optional[_Pointer[_struct.GdiplusStartupInput]]],
                              _type.Status]


# noinspection PyPep8Naming
class kernel32(metaclass=_WinDLL):
    CloseHandle: _Callable[[_type.HANDLE],
                           _type.BOOL]
    DeleteFileA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    DeleteFileW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
    GetLastError: _Callable[[],
                            _type.DWORD]
    GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                                _type.HMODULE]
    GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                                _type.HMODULE]
    GetTempPathA: _Callable[[_type.DWORD, _type.LPSTR],
                            _type.DWORD]
    GetTempPathW: _Callable[[_type.DWORD, _type.LPWSTR],
                            _type.DWORD]
    GlobalAlloc: _Callable[[_type.UINT, _type.SIZE_T],
                           _type.HGLOBAL]
    GlobalLock: _Callable[[_type.HGLOBAL],
                          _type.LPVOID]
    GlobalUnlock: _Callable[[_type.HGLOBAL],
                            _type.BOOL]


# noinspection PyPep8Naming
class msvcrt(metaclass=_WinDLL):
    free: _Callable[[_type.c_void_p],
                    _type.c_void_p]
    malloc: _Callable[[_type.c_void_p],
                      _type.c_size_t]
    memmove: _Callable[[_type.c_void_p, _type.c_void_p, _type.c_size_t],
                       _type.c_void_p]
    wcslen: _Callable[[_type.c_wchar_p],
                      _type.c_size_t]


# noinspection PyPep8Naming
class ntdll(metaclass=_WinDLL):
    RtlAreLongPathsEnabled: _Callable[[],
                                      _type.c_ubyte]


# noinspection PyPep8Naming
class ole32(metaclass=_WinDLL):
    CLSIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.CLSID]],
                               _type.HRESULT]
    CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],
                            _type.HRESULT]
    CoCreateInstance: _Callable[[_Pointer[_struct.CLSID], _Optional[_Pointer[_type.IUnknown]],
                                 _type.DWORD, _Pointer[_struct.IID], _type.LPVOID],
                                _type.HRESULT]
    CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                            _type.HRESULT]
    CoUninitialize: _Callable[[],
                              _type.VOID]
    IIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.IID]],
                             _type.HRESULT]
    StringFromCLSID: _Callable[[_Pointer[_struct.CLSID], _Pointer[_type.LPOLESTR]],
                               _type.HRESULT]
    StringFromGUID2: _Callable[[_Pointer[_struct.GUID], _type.LPOLESTR, _type.c_int],
                               _type.c_int]
    StringFromIID: _Callable[[_Pointer[_struct.IID], _Pointer[_type.LPOLESTR]],
                             _type.HRESULT]


# noinspection PyPep8Naming
class shell32(metaclass=_WinDLL):
    GUIDFromStringA: _Callable[[_type.LPCSTR, _Pointer[_struct.GUID]],
                               _type.BOOL] = 703
    GUIDFromStringW: _Callable[[_type.LPCTSTR, _Pointer[_struct.GUID]],
                               _type.BOOL] = 704
    ILCreateFromPath: _Callable[[_type.PCTSTR],
                                _Pointer[_struct.ITEMIDLIST]]
    ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                      _type.c_void_p]
    SHChangeNotify: _Callable[[_type.LONG, _type.UINT, _Optional[_type.LPCVOID], _Optional[_type.LPCVOID]],
                              _type.c_void_p]
    SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT, _Pointer[_Pointer[_struct.ITEMIDLIST]],
                                                  _Pointer[_com.IShellItemArray]],
                                                 _type.SHSTDAPI]
    SHGetFolderPathA: _Callable[[_Optional[_type.HWND], _type.c_int, _Optional[_type.HANDLE], _type.DWORD, _type.LPSTR],
                                _type.HRESULT]
    SHGetFolderPathW: _Callable[[_Optional[_type.HWND], _type.c_int,
                                 _Optional[_type.HANDLE], _type.DWORD, _type.LPWSTR],
                                _type.HRESULT]
    SHOpenFolderAndSelectItems: _Callable[[_Pointer[_struct.ITEMIDLIST], _type.UINT,
                                           _Optional[_Pointer[_Pointer[_struct.ITEMIDLIST]]], _type.DWORD],
                                          _type.SHSTDAPI]
    SHParseDisplayName: _Callable[[_type.PCWSTR, _Optional[_Pointer[_type.IBindCtx]],
                                   _Pointer[_Pointer[type[_struct.ITEMIDLIST]]], _type.SFGAOF, _Pointer[_type.SFGAOF]],
                                  _type.SHSTDAPI]
    ShellExecuteA: _Callable[[_Optional[_type.HWND], _Optional[_type.LPCSTR], _type.LPCSTR,
                              _Optional[_type.LPCSTR], _Optional[_type.LPCSTR], _type.INT],
                             _type.HINSTANCE]
    ShellExecuteW: _Callable[[_Optional[_type.HWND], _Optional[_type.LPCWSTR], _type.LPCWSTR,
                              _Optional[_type.LPCWSTR], _Optional[_type.LPWSTR], _type.INT],
                             _type.HINSTANCE]
    Shell_NotifyIconA: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAA]],
                                 _type.BOOL]
    Shell_NotifyIconW: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAW]],
                                 _type.BOOL]


# noinspection PyPep8Naming
class user32(metaclass=_WinDLL):
    CloseClipboard: _Callable[[],
                              _type.BOOL]
    CreateIconFromResource: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL, _type.DWORD],
                                      _type.HICON]
    CreateIconFromResourceEx: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL,
                                         _type.DWORD, _type.c_int, _type.c_int, _type.UINT],
                                        _type.HICON]
    CreateWindowExA: _Callable[[_type.DWORD, _Optional[_type.LPCSTR], _Optional[_type.LPCSTR], _type.DWORD,
                                _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                                _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                               _type.HWND]
    CreateWindowExW: _Callable[[_type.DWORD, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR], _type.DWORD,
                                _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                                _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                               _type.HWND]
    DefWindowProcA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                              _type.LRESULT]
    DefWindowProcW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                              _type.LRESULT]
    DestroyIcon: _Callable[[_type.HICON],
                           _type.BOOL]
    DestroyWindow: _Callable[[_type.HWND],
                             _type.BOOL]
    DispatchMessageA: _Callable[[_Pointer[_struct.MSG]],
                                _type.BOOL]
    DispatchMessageW: _Callable[[_Pointer[_struct.MSG]],
                                _type.BOOL]
    DrawMenuBar: _Callable[[_type.HWND],
                           _type.BOOL]
    EmptyClipboard: _Callable[[],
                              _type.BOOL]
    FindWindowA: _Callable[[_type.LPCSTR, _Optional[_type.LPCSTR]],
                           _type.HWND]
    FindWindowW: _Callable[[_type.LPCWSTR, _Optional[_type.LPCWSTR]],
                           _type.HWND]
    GetClassNameA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                             _type.c_int]
    GetClassNameW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                             _type.c_int]
    GetClipboardData: _Callable[[_type.UINT],
                                _type.HANDLE]
    GetCursorPos: _Callable[[_Pointer[_struct.POINT]],
                            _type.BOOL]
    GetDC: _Callable[[_Optional[_type.HWND]],
                     _type.HDC]
    GetMenu: _Callable[[_type.HWND],
                       _type.HMENU]
    GetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                           _type.BOOL]
    GetMessageA: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                           _type.BOOL]
    GetMessageW: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                           _type.BOOL]
    GetSubMenu: _Callable[[_type.HMENU, _type.c_int],
                          _type.HMENU]
    GetSysColor: _Callable[[_type.c_int],
                           _type.DWORD]
    GetSystemMenu: _Callable[[_type.HWND, _type.BOOL],
                             _type.HMENU]
    GetWindowDC: _Callable[[_Optional[_type.HWND]],
                           _type.HDC]
    GetWindowTextA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                              _type.c_int]
    GetWindowTextW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                              _type.c_int]
    KillTimer: _Callable[[_type.HWND, _type.UINT_PTR],
                         _type.BOOL]
    LoadIconA: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                         _type.HICON]
    LoadIconW: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                         _type.HICON]
    LoadImageA: _Callable[[_type.HINSTANCE, _type.LPCSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                          _type.HANDLE]
    LoadImageW: _Callable[[_type.HINSTANCE, _type.LPCWSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                          _type.HANDLE]
    LockWorkStation: _Callable[[],
                               _type.BOOL]
    OpenClipboard: _Callable[[_Optional[_type.HWND]],
                             _type.BOOL]
    PostQuitMessage: _Callable[[_type.c_int],
                               _type.c_void_p]
    RegisterClassExA: _Callable[[_Pointer[_struct.WNDCLASSEXA]],
                                _type.ATOM]
    RegisterClassExW: _Callable[[_Pointer[_struct.WNDCLASSEXW]],
                                _type.ATOM]
    ReleaseDC: _Callable[[_Optional[_type.HWND], _type.HDC],
                         _type.c_int]
    SendMessageA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                            _type.LRESULT]
    SendMessageTimeoutA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                    _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                                   _type.LRESULT]
    SendMessageTimeoutW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                    _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                                   _type.LRESULT]
    SendMessageW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                            _type.LRESULT]
    SetClipboardData: _Callable[[_type.UINT, _type.HANDLE],
                                _type.HANDLE]
    SetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                           _type.BOOL]
    SetSysColors: _Callable[[_type.c_int, _Pointer[_type.INT], _Pointer[_type.COLORREF]],
                            _type.BOOL]
    SetTimer: _Callable[[_Optional[_type.HWND], _type.UINT_PTR, _type.UINT, _Optional[_type.TIMERPROC]],
                        _type.UINT_PTR]
    ShowWindow: _Callable[[_type.HWND, _type.c_int],
                          _type.BOOL]
    SystemParametersInfoA: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                     _type.BOOL]
    SystemParametersInfoW: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                     _type.BOOL]
    TranslateMessage: _Callable[[_Pointer[_struct.MSG]],
                                _type.BOOL]
    UnregisterClassA: _Callable[[_type.LPCSTR, _type.HINSTANCE],
                                _type.BOOL]
    UnregisterClassW: _Callable[[_type.LPCWSTR, _type.HINSTANCE],
                                _type.BOOL]


class Shlwapi(metaclass=_WinDLL):
    GUIDFromStringA: _Callable[[_type.LPCSTR, _Pointer[_struct.GUID]],
                               _type.BOOL] = 269
    GUIDFromStringW: _Callable[[_type.LPCTSTR, _Pointer[_struct.GUID]],
                               _type.BOOL] = 270
    PathFileExistsA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathFileExistsW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]


_ORDINAL = {lib: {var_: (ord_, delattr(lib, var_))[0] for var_, ord_ in tuple(
    vars(lib).items()) if _not_internal(var_)} for var, lib in globals().items() if _not_internal(var)}


def _init(lib: type[_CDLL], name: str):
    if name == 'lib':
        lib.lib = getattr(_ctypes, lib.__class__.__name__[1:])(lib.__name__, use_last_error=_DEBUG)
        return lib.lib
    try:
        func = lib.lib[_ORDINAL[lib][name]]
    except KeyError:
        func = getattr(lib.lib, name)
    setattr(lib, name, func)
    func.restype, *func.argtypes = _resolve_type(_typing.get_type_hints(lib)[name])
    func.__doc__ = _get_doc(name, func.restype, func.argtypes)
    return func


_CDLL.__getattr__ = _init
