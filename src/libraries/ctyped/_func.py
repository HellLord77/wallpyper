import ctypes as _ctypes
import typing as _typing
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _com
from . import _header
from . import _lib
from . import _struct
from . import _type

SetWindowTheme: _Callable[[_type.HWND, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR]],
                          _type.HRESULT] = _lib.UxTheme.SetWindowTheme

RoInitialize: _Callable[[_type.RO_INIT_TYPE],
                        _type.HRESULT] = _lib.combase.RoInitialize
RoUninitialize: _Callable[[],
                          _type.c_void_p] = _lib.combase.RoUninitialize
RoActivateInstance: _Callable[[_type.HSTRING, _type.c_void_p],
                              _type.HRESULT] = _lib.combase.RoActivateInstance
WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH], _type.UINT32, _header.Pointer[_type.HSTRING]],
                               _type.HRESULT] = _lib.combase.WindowsCreateString
WindowsDeleteString: _Callable[[_type.HSTRING],
                               _type.HRESULT] = _lib.combase.WindowsDeleteString

GetObjectA: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _lib.gdi32.GetObjectA
GetObjectW: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _lib.gdi32.GetObjectW
DeleteObject: _Callable[[_type.HGDIOBJ],
                        _type.BOOL] = _lib.gdi32.DeleteObject
CreateDIBitmap: _Callable[[_type.HDC, _header.Pointer[_struct.BITMAPINFOHEADER], _type.DWORD,
                           _type.VOID, _header.Pointer[_struct.BITMAPINFO], _type.UINT],
                          _type.HBITMAP] = _lib.gdi32.CreateDIBitmap
GetDIBits: _Callable[[_type.HDC, _type.HBITMAP, _type.UINT, _type.UINT,
                      _Optional[_type.LPVOID], _header.Pointer[_struct.BITMAPINFO], _type.UINT],
                     _type.c_int] = _lib.gdi32.GetDIBits
CreateSolidBrush: _Callable[[_type.COLORREF],
                            _type.HBRUSH] = _lib.gdi32.CreateSolidBrush
GetStockObject: _Callable[[_type.c_int],
                          _type.HGDIOBJ] = _lib.gdi32.GetStockObject

GdiplusStartup: _Callable[[_header.Pointer[_type.ULONG_PTR], _header.Pointer[_struct.GdiplusStartupInput],
                           _Optional[_header.Pointer[_struct.GdiplusStartupInput]]],
                          _type.Status] = _lib.gdiplus.GdiplusStartup
GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                           _type.VOID] = _lib.gdiplus.GdiplusShutdown
GdipCreateBitmapFromFile: _Callable[[_header.Pointer[_type.WCHAR], _header.Pointer[_type.GpBitmap]],
                                    _type.GpStatus] = _lib.gdiplus.GdipCreateBitmapFromFile
GdipDisposeImage: _Callable[[_type.GpImage],
                            _type.GpStatus] = _lib.gdiplus.GdipDisposeImage
GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap, _header.Pointer[_type.HBITMAP], _type.ARGB],
                                       _type.GpStatus] = _lib.gdiplus.GdipCreateHBITMAPFromBitmap

GlobalAlloc: _Callable[[_type.UINT, _type.SIZE_T],
                       _type.HGLOBAL] = _lib.kernel32.GlobalAlloc
GlobalLock: _Callable[[_type.HGLOBAL],
                      _type.LPVOID] = _lib.kernel32.GlobalLock
GlobalUnlock: _Callable[[_type.HGLOBAL],
                        _type.BOOL] = _lib.kernel32.GlobalUnlock
CloseHandle: _Callable[[_type.HANDLE],
                       _type.BOOL] = _lib.kernel32.CloseHandle
GetLastError: _Callable[[],
                        _type.DWORD] = _lib.kernel32.GetLastError

memmove: _Callable[[_type.c_void_p, _type.c_void_p, _type.c_size_t],
                   _type.c_void_p] = _lib.msvcrt.memmove
wcslen: _Callable[[_type.c_wchar_p],
                  _type.c_size_t] = _lib.msvcrt.wcslen

RtlAreLongPathsEnabled: _Callable[[],
                                  _type.c_ubyte] = _lib.ntdll.RtlAreLongPathsEnabled

IIDFromString: _Callable[[_type.LPCOLESTR, _header.Pointer[_struct.IID]],
                         _type.HRESULT] = _lib.ole32.IIDFromString
CLSIDFromString: _Callable[[_type.LPCOLESTR, _header.Pointer[_struct.CLSID]],
                           _type.HRESULT] = _lib.ole32.CLSIDFromString
CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                        _type.HRESULT] = _lib.ole32.CoInitialize
CoUninitialize: _Callable[[],
                          _type.VOID] = _lib.ole32.CoUninitialize
CoCreateInstance: _Callable[[_header.Pointer[_struct.CLSID], _Optional[_header.Pointer[_type.IUnknown]],
                             _type.DWORD, _header.Pointer[_struct.IID], _type.LPVOID],
                            _type.HRESULT] = _lib.ole32.CoCreateInstance
StringFromIID: _Callable[[_header.Pointer[_struct.IID], _header.Pointer[_type.LPOLESTR]],
                         _type.HRESULT] = _lib.ole32.StringFromIID
StringFromCLSID: _Callable[[_header.Pointer[_struct.CLSID], _header.Pointer[_type.LPOLESTR]],
                           _type.HRESULT] = _lib.ole32.StringFromCLSID

SHGetFolderPathA: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPSTR],
                            _type.HRESULT] = _lib.shell32.SHGetFolderPathA
SHGetFolderPathW: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPWSTR],
                            _type.HRESULT] = _lib.shell32.SHGetFolderPathW
ILCreateFromPath: _Callable[[_type.PCTSTR],
                            _header.Pointer[_struct.ITEMIDLIST]] = _lib.shell32.ILCreateFromPath
ILFree: _Callable[[_Optional[_header.Pointer[_struct.ITEMIDLIST]]],
                  _type.c_void_p] = _lib.shell32.ILFree
SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT, _header.Pointer[_header.Pointer[_struct.ITEMIDLIST]],
                                              _header.Pointer[_com.IShellItemArray]],
                                             _type.SHSTDAPI] = _lib.shell32.SHCreateShellItemArrayFromIDLists
SHParseDisplayName: _Callable[[_type.PCWSTR, _Optional[_header.Pointer[_type.IBindCtx]], _header.Pointer[
    _header.Pointer[type[_struct.ITEMIDLIST]]], _type.SFGAOF, _header.Pointer[_type.SFGAOF]],
                              _type.SHSTDAPI] = _lib.shell32.SHParseDisplayName

SystemParametersInfoA: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                 _type.BOOL] = _lib.user32.SystemParametersInfoA
SystemParametersInfoW: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                 _type.BOOL] = _lib.user32.SystemParametersInfoW
OpenClipboard: _Callable[[_Optional[_type.HWND]],
                         _type.BOOL] = _lib.user32.OpenClipboard
CloseClipboard: _Callable[[],
                          _type.BOOL] = _lib.user32.CloseClipboard
EmptyClipboard: _Callable[[],
                          _type.BOOL] = _lib.user32.EmptyClipboard
GetClipboardData: _Callable[[_type.UINT],
                            _type.HANDLE] = _lib.user32.GetClipboardData
SetClipboardData: _Callable[[_type.UINT, _type.HANDLE],
                            _type.HANDLE] = _lib.user32.SetClipboardData
GetSysColor: _Callable[[_type.c_int],
                       _type.DWORD] = _lib.user32.GetSysColor
SetSysColors: _Callable[[_type.c_int, _header.Pointer[_type.INT], _header.Pointer[_type.COLORREF]],
                        _type.BOOL] = _lib.user32.SetSysColors
GetMenu: _Callable[[_type.HWND],
                   _type.HMENU] = _lib.user32.GetMenu
GetSystemMenu: _Callable[[_type.HWND, _type.BOOL],
                         _type.HMENU] = _lib.user32.GetSystemMenu
GetSubMenu: _Callable[[_type.HMENU, _type.c_int],
                      _type.HMENU] = _lib.user32.GetSubMenu
GetMenuInfo: _Callable[[_type.HMENU, _header.Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _lib.user32.GetMenuInfo
SetMenuInfo: _Callable[[_type.HMENU, _header.Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _lib.user32.SetMenuInfo
DrawMenuBar: _Callable[[_type.HWND],
                       _type.BOOL] = _lib.user32.DrawMenuBar
LoadImageA: _Callable[[_type.HINSTANCE, _type.LPCSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _lib.user32.LoadImageA
LoadImageW: _Callable[[_type.HINSTANCE, _type.LPCWSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _lib.user32.LoadImageW
GetDC: _Callable[[_Optional[_type.HWND]],
                 _type.HDC] = _lib.user32.GetDC
GetWindowDC: _Callable[[_Optional[_type.HWND]],
                       _type.HDC] = _lib.user32.GetWindowDC
ReleaseDC: _Callable[[_Optional[_type.HWND], _type.HDC],
                     _type.c_int] = _lib.user32.ReleaseDC
FindWindowA: _Callable[[_type.LPCSTR, _Optional[_type.LPCSTR]],
                       _type.HWND] = _lib.user32.FindWindowA
FindWindowW: _Callable[[_type.LPCWSTR, _Optional[_type.LPCWSTR]],
                       _type.HWND] = _lib.user32.FindWindowW
SendMessageA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                        _type.LRESULT] = _lib.user32.SendMessageA
SendMessageW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                        _type.LRESULT] = _lib.user32.SendMessageW
SendMessageTimeoutA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                               _type.LRESULT] = _lib.user32.SendMessageTimeoutA
SendMessageTimeoutW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                               _type.LRESULT] = _lib.user32.SendMessageTimeoutW
GetClassNameA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                         _type.c_int] = _lib.user32.GetClassNameA
GetClassNameW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                         _type.c_int] = _lib.user32.GetClassNameW
GetWindowTextA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                          _type.c_int] = _lib.user32.GetWindowTextA
GetWindowTextW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                          _type.c_int] = _lib.user32.GetWindowTextW


# noinspection PyUnresolvedReferences,PyProtectedMember
def __getattr__(name: str) -> _ctypes._CFuncPtr:
    # noinspection PyTypeChecker
    _header.Globals.hasattr(_func, name)
    globals_ = globals()
    func = _func[name]
    func.restype, *func.argtypes = _header.resolve_type(_annotations[name])
    func.__doc__ = _header.get_doc(name, func.restype, func.argtypes)
    globals_[name] = func
    return globals_[name]


_func = _header.init(globals())
_annotations = _typing.get_type_hints(type('', (), globals()))
if _header.INIT:
    for _func_ in _func:
        __getattr__(_func_)
