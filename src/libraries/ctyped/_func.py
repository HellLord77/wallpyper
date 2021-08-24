import typing as _typing
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _ctype
from . import _header
from . import _lib
from . import _struct

# TODO: func help

RoInitialize: _Callable[[_ctype.RO_INIT_TYPE],
                        _ctype.HRESULT] = _lib.combase.RoInitialize
RoUninitialize: _Callable[[],
                          _ctype.c_void_p] = _lib.combase.RoUninitialize

GetObjectA: _Callable[[_ctype.HANDLE, _ctype.c_int, _ctype.LPVOID],
                      _ctype.c_int] = _lib.gdi32.GetObjectA
GetObjectW: _Callable[[_ctype.HANDLE, _ctype.c_int, _ctype.LPVOID],
                      _ctype.c_int] = _lib.gdi32.GetObjectW
DeleteObject: _Callable[[_ctype.HGDIOBJ],
                        _ctype.BOOL] = _lib.gdi32.DeleteObject
CreateDIBitmap: _Callable[[_ctype.HDC, _header.Pointer[_struct.BITMAPINFOHEADER], _ctype.DWORD,
                           _ctype.VOID, _header.Pointer[_struct.BITMAPINFO], _ctype.UINT],
                          _ctype.HBITMAP] = _lib.gdi32.CreateDIBitmap
GetDIBits: _Callable[[_ctype.HDC, _ctype.HBITMAP, _ctype.UINT, _ctype.UINT,
                      _Optional[_ctype.LPVOID], _header.Pointer[_struct.BITMAPINFO], _ctype.UINT],
                     _ctype.c_int] = _lib.gdi32.GetDIBits
CreateSolidBrush: _Callable[[_ctype.COLORREF],
                            _ctype.HBRUSH] = _lib.gdi32.CreateSolidBrush
GetStockObject: _Callable[[_ctype.c_int],
                          _ctype.HGDIOBJ] = _lib.gdi32.GetStockObject

GdiplusStartup: _Callable[[_header.Pointer[_ctype.ULONG_PTR], _header.Pointer[_struct.GdiplusStartupInput],
                           _Optional[_header.Pointer[_struct.GdiplusStartupInput]]],
                          _ctype.Status] = _lib.gdiplus.GdiplusStartup
GdiplusShutdown: _Callable[[_ctype.ULONG_PTR],
                           _ctype.VOID] = _lib.gdiplus.GdiplusShutdown
GdipCreateBitmapFromFile: _Callable[[_header.Pointer[_ctype.WCHAR], _header.Pointer[_ctype.GpBitmap]],
                                    _ctype.GpStatus] = _lib.gdiplus.GdipCreateBitmapFromFile
GdipDisposeImage: _Callable[[_ctype.GpImage],
                            _ctype.GpStatus] = _lib.gdiplus.GdipDisposeImage
GdipCreateHBITMAPFromBitmap: _Callable[[_ctype.GpBitmap, _header.Pointer[_ctype.HBITMAP], _ctype.ARGB],
                                       _ctype.GpStatus] = _lib.gdiplus.GdipCreateHBITMAPFromBitmap

GlobalAlloc: _Callable[[_ctype.UINT, _ctype.SIZE_T],
                       _ctype.HGLOBAL] = _lib.kernel32.GlobalAlloc
GlobalLock: _Callable[[_ctype.HGLOBAL],
                      _ctype.LPVOID] = _lib.kernel32.GlobalLock
GlobalUnlock: _Callable[[_ctype.HGLOBAL],
                        _ctype.BOOL] = _lib.kernel32.GlobalUnlock
CloseHandle: _Callable[[_ctype.HANDLE],
                       _ctype.BOOL] = _lib.kernel32.CloseHandle
GetLastError: _Callable[[],
                        _ctype.DWORD] = _lib.kernel32.GetLastError

memmove: _Callable[[_ctype.c_void_p, _ctype.c_void_p, _ctype.c_size_t],
                   _ctype.c_void_p] = _lib.msvcrt.memmove
wcslen: _Callable[[_ctype.c_wchar_p],
                  _ctype.c_size_t] = _lib.msvcrt.wcslen

RtlAreLongPathsEnabled: _Callable[[],
                                  _ctype.c_ubyte] = _lib.ntdll.RtlAreLongPathsEnabled

IIDFromString: _Callable[[_ctype.LPCOLESTR, _header.Pointer[_struct.IID]],
                         _ctype.HRESULT] = _lib.ole32.IIDFromString
CLSIDFromString: _Callable[[_ctype.LPCOLESTR, _header.Pointer[_struct.CLSID]],
                           _ctype.HRESULT] = _lib.ole32.CLSIDFromString
CoInitialize: _Callable[[_Optional[_ctype.LPVOID]],
                        _ctype.HRESULT] = _lib.ole32.CoInitialize
CoUninitialize: _Callable[[],
                          _ctype.VOID] = _lib.ole32.CoUninitialize
CoCreateInstance: _Callable[[_header.Pointer[_struct.CLSID], _Optional[_header.Pointer[_ctype.IUnknown]],
                             _ctype.DWORD, _header.Pointer[_struct.IID], _ctype.LPVOID],
                            _ctype.HRESULT] = _lib.ole32.CoCreateInstance
StringFromIID: _Callable[[_header.Pointer[_struct.IID], _header.Pointer[_ctype.LPOLESTR]],
                         _ctype.HRESULT] = _lib.ole32.StringFromIID
StringFromCLSID: _Callable[[_header.Pointer[_struct.CLSID], _header.Pointer[_ctype.LPOLESTR]],
                           _ctype.HRESULT] = _lib.ole32.StringFromCLSID

SHGetFolderPathA: _Callable[[_Optional[_ctype.HWND], _ctype.c_int,
                             _Optional[_ctype.HANDLE], _ctype.DWORD, _ctype.LPSTR],
                            _ctype.HRESULT] = _lib.shell32.SHGetFolderPathA
SHGetFolderPathW: _Callable[[_Optional[_ctype.HWND], _ctype.c_int,
                             _Optional[_ctype.HANDLE], _ctype.DWORD, _ctype.LPWSTR],
                            _ctype.HRESULT] = _lib.shell32.SHGetFolderPathW

SystemParametersInfoA: _Callable[[_ctype.UINT, _ctype.UINT, _ctype.PVOID, _ctype.UINT],
                                 _ctype.BOOL] = _lib.user32.SystemParametersInfoA
SystemParametersInfoW: _Callable[[_ctype.UINT, _ctype.UINT, _ctype.PVOID, _ctype.UINT],
                                 _ctype.BOOL] = _lib.user32.SystemParametersInfoW
OpenClipboard: _Callable[[_Optional[_ctype.HWND]],
                         _ctype.BOOL] = _lib.user32.OpenClipboard
CloseClipboard: _Callable[[],
                          _ctype.BOOL] = _lib.user32.CloseClipboard
EmptyClipboard: _Callable[[],
                          _ctype.BOOL] = _lib.user32.EmptyClipboard
GetClipboardData: _Callable[[_ctype.UINT],
                            _ctype.HANDLE] = _lib.user32.GetClipboardData
SetClipboardData: _Callable[[_ctype.UINT, _ctype.HANDLE],
                            _ctype.HANDLE] = _lib.user32.SetClipboardData
GetSysColor: _Callable[[_ctype.c_int],
                       _ctype.DWORD] = _lib.user32.GetSysColor
SetSysColors: _Callable[[_ctype.c_int, _header.Pointer[_ctype.INT], _header.Pointer[_ctype.COLORREF]],
                        _ctype.BOOL] = _lib.user32.SetSysColors
GetMenu: _Callable[[_ctype.HWND],
                   _ctype.HMENU] = _lib.user32.GetMenu
GetSystemMenu: _Callable[[_ctype.HWND, _ctype.BOOL],
                         _ctype.HMENU] = _lib.user32.GetSystemMenu
GetSubMenu: _Callable[[_ctype.HMENU, _ctype.c_int],
                      _ctype.HMENU] = _lib.user32.GetSubMenu
GetMenuInfo: _Callable[[_ctype.HMENU, _header.Pointer[_struct.MENUINFO]],
                       _ctype.BOOL] = _lib.user32.GetMenuInfo
SetMenuInfo: _Callable[[_ctype.HMENU, _header.Pointer[_struct.MENUINFO]],
                       _ctype.BOOL] = _lib.user32.SetMenuInfo
DrawMenuBar: _Callable[[_ctype.HWND],
                       _ctype.BOOL] = _lib.user32.DrawMenuBar
LoadImageA: _Callable[[_ctype.HINSTANCE, _ctype.LPCSTR, _ctype.UINT, _ctype.c_int, _ctype.c_int, _ctype.UINT],
                      _ctype.HANDLE] = _lib.user32.LoadImageA
LoadImageW: _Callable[[_ctype.HINSTANCE, _ctype.LPCWSTR, _ctype.UINT, _ctype.c_int, _ctype.c_int, _ctype.UINT],
                      _ctype.HANDLE] = _lib.user32.LoadImageW
GetDC: _Callable[[_Optional[_ctype.HWND]],
                 _ctype.HDC] = _lib.user32.GetDC
GetWindowDC: _Callable[[_Optional[_ctype.HWND]],
                       _ctype.HDC] = _lib.user32.GetWindowDC
ReleaseDC: _Callable[[_Optional[_ctype.HWND], _ctype.HDC],
                     _ctype.c_int] = _lib.user32.ReleaseDC


def _init():
    globals_ = globals()
    types_ = _typing.get_type_hints(type('', (), globals_)())
    for var, func in _header.items(globals_):
        func.restype, *func.argtypes = _header.resolve_type(types_[var])


_init()
