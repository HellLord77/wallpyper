import typing as _typing

from . import _ctype
from . import _header
from . import _lib
from . import _struct

RtlAreLongPathsEnabled: _typing.Callable[[],
                                         _ctype.c_ubyte] = _lib.ntdll.RtlAreLongPathsEnabled

GlobalAlloc: _typing.Callable[[_ctype.UINT, _ctype.SIZE_T],
                              _ctype.HGLOBAL] = _lib.kernel32.GlobalAlloc
GlobalLock: _typing.Callable[[_ctype.HGLOBAL],
                             _ctype.LPVOID] = _lib.kernel32.GlobalLock
GlobalUnlock: _typing.Callable[[_ctype.HGLOBAL],
                               _ctype.BOOL] = _lib.kernel32.GlobalUnlock
CloseHandle: _typing.Callable[[_ctype.HANDLE],
                              _ctype.BOOL] = _lib.kernel32.CloseHandle
GetLastError: _typing.Callable[[],
                               _ctype.DWORD] = _lib.kernel32.GetLastError

GetObjectA: _typing.Callable[[_ctype.HANDLE, _ctype.c_int, _ctype.LPVOID],
                             _ctype.c_int] = _lib.gdi32.GetObjectA
GetObjectW: _typing.Callable[[_ctype.HANDLE, _ctype.c_int, _ctype.LPVOID],
                             _ctype.c_int] = _lib.gdi32.GetObjectW
DeleteObject: _typing.Callable[[_ctype.HGDIOBJ],
                               _ctype.BOOL] = _lib.gdi32.DeleteObject
CreateDIBitmap: _typing.Callable[[_ctype.HDC, _header.Pointer[_struct.BITMAPINFOHEADER], _ctype.DWORD,
                                  _ctype.VOID, _header.Pointer[_struct.BITMAPINFO], _ctype.UINT],
                                 _ctype.HBITMAP] = _lib.gdi32.CreateDIBitmap
GetDIBits: _typing.Callable[[_ctype.HDC, _ctype.HBITMAP, _ctype.UINT, _ctype.UINT,
                             _typing.Optional[_ctype.LPVOID], _header.Pointer[_struct.BITMAPINFO], _ctype.UINT],
                            _ctype.c_int] = _lib.gdi32.GetDIBits
CreateSolidBrush: _typing.Callable[[_ctype.COLORREF],
                                   _ctype.HBRUSH] = _lib.gdi32.CreateSolidBrush
GetStockObject: _typing.Callable[[_ctype.c_int],
                                 _ctype.HGDIOBJ] = _lib.gdi32.GetStockObject

SystemParametersInfoA: _typing.Callable[[_ctype.UINT, _ctype.UINT, _ctype.PVOID, _ctype.UINT],
                                        _ctype.BOOL] = _lib.user32.SystemParametersInfoA
SystemParametersInfoW: _typing.Callable[[_ctype.UINT, _ctype.UINT, _ctype.PVOID, _ctype.UINT],
                                        _ctype.BOOL] = _lib.user32.SystemParametersInfoW
OpenClipboard: _typing.Callable[[_typing.Optional[_ctype.HWND]],
                                _ctype.BOOL] = _lib.user32.OpenClipboard
CloseClipboard: _typing.Callable[[],
                                 _ctype.BOOL] = _lib.user32.CloseClipboard
EmptyClipboard: _typing.Callable[[],
                                 _ctype.BOOL] = _lib.user32.EmptyClipboard
GetClipboardData: _typing.Callable[[_ctype.UINT],
                                   _ctype.HANDLE] = _lib.user32.GetClipboardData
SetClipboardData: _typing.Callable[[_ctype.UINT, _ctype.HANDLE],
                                   _ctype.HANDLE] = _lib.user32.SetClipboardData
GetSysColor: _typing.Callable[[_ctype.c_int],
                              _ctype.DWORD] = _lib.user32.GetSysColor
SetSysColors: _typing.Callable[[_ctype.c_int, _header.Pointer[_ctype.INT], _header.Pointer[_ctype.COLORREF]],
                               _ctype.BOOL] = _lib.user32.SetSysColors
GetMenu: _typing.Callable[[_ctype.HWND],
                          _ctype.HMENU] = _lib.user32.GetMenu
GetSystemMenu: _typing.Callable[[_ctype.HWND, _ctype.BOOL],
                                _ctype.HMENU] = _lib.user32.GetSystemMenu
GetSubMenu: _typing.Callable[[_ctype.HMENU, _ctype.c_int],
                             _ctype.HMENU] = _lib.user32.GetSubMenu
GetMenuInfo: _typing.Callable[[_ctype.HMENU, _header.Pointer[_struct.MENUINFO]],
                              _ctype.BOOL] = _lib.user32.GetMenuInfo
SetMenuInfo: _typing.Callable[[_ctype.HMENU, _header.Pointer[_struct.MENUINFO]],
                              _ctype.BOOL] = _lib.user32.SetMenuInfo
DrawMenuBar: _typing.Callable[[_ctype.HWND],
                              _ctype.BOOL] = _lib.user32.DrawMenuBar
LoadImageA: _typing.Callable[[_ctype.HINSTANCE, _ctype.LPCSTR, _ctype.UINT, _ctype.c_int, _ctype.c_int, _ctype.UINT],
                             _ctype.HANDLE] = _lib.user32.LoadImageA
LoadImageW: _typing.Callable[[_ctype.HINSTANCE, _ctype.LPCWSTR, _ctype.UINT, _ctype.c_int, _ctype.c_int, _ctype.UINT],
                             _ctype.HANDLE] = _lib.user32.LoadImageW
GetDC: _typing.Callable[[_typing.Optional[_ctype.HWND]],
                        _ctype.HDC] = _lib.user32.GetDC
GetWindowDC: _typing.Callable[[_typing.Optional[_ctype.HWND]],
                              _ctype.HDC] = _lib.user32.GetWindowDC
ReleaseDC: _typing.Callable[[_typing.Optional[_ctype.HWND], _ctype.HDC],
                            _ctype.c_int] = _lib.user32.ReleaseDC

IIDFromString: _typing.Callable[[_ctype.LPCOLESTR, _header.Pointer[_struct.IID]],
                                _ctype.HRESULT] = _lib.ole32.IIDFromString
CLSIDFromString: _typing.Callable[[_ctype.LPCOLESTR, _header.Pointer[_struct.CLSID]],
                                  _ctype.HRESULT] = _lib.ole32.CLSIDFromString
CoInitialize: _typing.Callable[[_typing.Optional[_ctype.LPVOID]],
                               _ctype.HRESULT] = _lib.ole32.CoInitialize
CoUninitialize: _typing.Callable[[],
                                 _ctype.VOID] = _lib.ole32.CoUninitialize
CoCreateInstance: _typing.Callable[[_header.Pointer[_struct.CLSID], _typing.Optional[_header.Pointer[_ctype.IUnknown]],
                                    _ctype.DWORD, _header.Pointer[_struct.IID], _ctype.LPVOID],
                                   _ctype.HRESULT] = _lib.ole32.CoCreateInstance
StringFromIID: _typing.Callable[[_header.Pointer[_struct.IID], _header.Pointer[_ctype.LPOLESTR]],
                                _ctype.HRESULT] = _lib.ole32.StringFromIID
StringFromCLSID: _typing.Callable[[_header.Pointer[_struct.CLSID], _header.Pointer[_ctype.LPOLESTR]],
                                  _ctype.HRESULT] = _lib.ole32.StringFromCLSID

memmove: _typing.Callable[[_ctype.c_void_p, _ctype.c_void_p, _ctype.c_size_t],
                          _ctype.c_void_p] = _lib.msvcrt.memmove
wcslen: _typing.Callable[[_ctype.c_wchar_p],
                         _ctype.c_size_t] = _lib.msvcrt.wcslen

GdiplusStartup: _typing.Callable[[_header.Pointer[_ctype.ULONG_PTR], _header.Pointer[_struct.GdiplusStartupInput],
                                  _typing.Optional[_header.Pointer[_struct.GdiplusStartupInput]]],
                                 _ctype.Status] = _lib.gdiplus.GdiplusStartup
GdiplusShutdown: _typing.Callable[[_ctype.ULONG_PTR],
                                  _ctype.VOID] = _lib.gdiplus.GdiplusShutdown
GdipCreateBitmapFromFile: _typing.Callable[[_header.Pointer[_ctype.WCHAR], _header.Pointer[_ctype.GpBitmap]],
                                           _ctype.GpStatus] = _lib.gdiplus.GdipCreateBitmapFromFile
GdipDisposeImage: _typing.Callable[[_ctype.GpImage],
                                   _ctype.GpStatus] = _lib.gdiplus.GdipDisposeImage
GdipCreateHBITMAPFromBitmap: _typing.Callable[[_ctype.GpBitmap, _header.Pointer[_ctype.HBITMAP], _ctype.ARGB],
                                              _ctype.GpStatus] = _lib.gdiplus.GdipCreateHBITMAPFromBitmap

SHGetFolderPathA: _typing.Callable[[_typing.Optional[_ctype.HWND], _ctype.c_int,
                                    _typing.Optional[_ctype.HANDLE], _ctype.DWORD, _ctype.LPSTR],
                                   _ctype.HRESULT] = _lib.shell32.SHGetFolderPathA
SHGetFolderPathW: _typing.Callable[[_typing.Optional[_ctype.HWND], _ctype.c_int,
                                    _typing.Optional[_ctype.HANDLE], _ctype.DWORD, _ctype.LPWSTR],
                                   _ctype.HRESULT] = _lib.shell32.SHGetFolderPathW


def _init():
    globals_ = globals()
    types_ = _typing.get_type_hints(type('', (), globals_)())
    for var, func in _header.items(globals_):
        func.restype, *func.argtypes = _header.resolve_type(types_[var])


_init()
