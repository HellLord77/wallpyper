import ctypes as _ctypes
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _com
from . import _const
from . import _lib
from . import _struct
from . import _type
from .__head__ import Globals as _Globals
from .__head__ import Pointer as _Pointer
from .__head__ import get_doc as _get_doc
from .__head__ import resolve_type as _resolve_type

SetWindowTheme: _Callable[[_type.HWND, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR]],
                          _type.HRESULT] = _lib.uxtheme.SetWindowTheme

RoInitialize: _Callable[[_type.RO_INIT_TYPE],
                        _type.HRESULT] = _lib.combase.RoInitialize
RoUninitialize: _Callable[[],
                          _type.c_void_p] = _lib.combase.RoUninitialize
RoActivateInstance: _Callable[[_type.HSTRING, _type.c_void_p],
                              _type.HRESULT] = _lib.combase.RoActivateInstance
WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH], _type.UINT32, _Pointer[_type.HSTRING]],
                               _type.HRESULT] = _lib.combase.WindowsCreateString
WindowsDeleteString: _Callable[[_type.HSTRING],
                               _type.HRESULT] = _lib.combase.WindowsDeleteString

GetObjectA: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _lib.gdi32.GetObjectA
GetObjectW: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _lib.gdi32.GetObjectW
DeleteObject: _Callable[[_type.HGDIOBJ],
                        _type.BOOL] = _lib.gdi32.DeleteObject
CreateDIBitmap: _Callable[[_type.HDC, _Pointer[_struct.BITMAPINFOHEADER],
                           _type.DWORD, _type.VOID, _Pointer[_struct.BITMAPINFO], _type.UINT],
                          _type.HBITMAP] = _lib.gdi32.CreateDIBitmap
GetDIBits: _Callable[[_type.HDC, _type.HBITMAP, _type.UINT, _type.UINT,
                      _Optional[_type.LPVOID], _Pointer[_struct.BITMAPINFO], _type.UINT],
                     _type.c_int] = _lib.gdi32.GetDIBits
CreateSolidBrush: _Callable[[_type.COLORREF],
                            _type.HBRUSH] = _lib.gdi32.CreateSolidBrush
GetStockObject: _Callable[[_type.c_int],
                          _type.HGDIOBJ] = _lib.gdi32.GetStockObject

GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],
                           _Pointer[_struct.GdiplusStartupInput], _Optional[_Pointer[_struct.GdiplusStartupInput]]],
                          _type.Status] = _lib.GdiPlus.GdiplusStartup
GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                           _type.VOID] = _lib.GdiPlus.GdiplusShutdown
GdipLoadImageFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpImage]],
                                 _type.GpStatus] = _lib.GdiPlus.GdipLoadImageFromFile
GdipDisposeImage: _Callable[[_type.GpImage],
                            _type.GpStatus] = _lib.GdiPlus.GdipDisposeImage
GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage, _Pointer[_type.UINT]],
                                            _type.GpStatus] = _lib.GdiPlus.GdipImageGetFrameDimensionsCount
GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                           _type.GpStatus] = _lib.GdiPlus.GdipImageGetFrameDimensionsList
GdipImageGetFrameCount: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _Pointer[_type.UINT]],
                                  _type.GpStatus] = _lib.GdiPlus.GdipImageGetFrameCount
GdipGetPropertyItemSize: _Callable[[_type.GpImage, _type.PROPID, _Pointer[_type.UINT]],
                                   _type.GpStatus] = _lib.GdiPlus.GdipGetPropertyItemSize
GdipGetPropertyItem: _Callable[[_type.GpImage, _type.PROPID, _type.UINT, _Pointer[_struct.PropertyItem]],
                               _type.GpStatus] = _lib.GdiPlus.GdipGetPropertyItem
GdipImageSelectActiveFrame: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                      _type.GpStatus] = _lib.GdiPlus.GdipImageSelectActiveFrame
GdipCreateBitmapFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpBitmap]],
                                    _type.GpStatus] = _lib.GdiPlus.GdipCreateBitmapFromFile
GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HBITMAP], _type.ARGB],
                                       _type.GpStatus] = _lib.GdiPlus.GdipCreateHBITMAPFromBitmap
GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HICON]],
                                     _type.GpStatus] = _lib.GdiPlus.GdipCreateHICONFromBitmap

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
GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                            _type.HMODULE] = _lib.kernel32.GetModuleHandleA
GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                            _type.HMODULE] = _lib.kernel32.GetModuleHandleW

malloc: _Callable[[_type.c_void_p],
                  _type.c_size_t] = _lib.msvcrt.malloc
free: _Callable[[_type.c_void_p],
                _type.c_void_p] = _lib.msvcrt.free
memmove: _Callable[[_type.c_void_p, _type.c_void_p, _type.c_size_t],
                   _type.c_void_p] = _lib.msvcrt.memmove
wcslen: _Callable[[_type.c_wchar_p],
                  _type.c_size_t] = _lib.msvcrt.wcslen

RtlAreLongPathsEnabled: _Callable[[],
                                  _type.c_ubyte] = _lib.ntdll.RtlAreLongPathsEnabled

IIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.IID]],
                         _type.HRESULT] = _lib.ole32.IIDFromString
CLSIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.CLSID]],
                           _type.HRESULT] = _lib.ole32.CLSIDFromString
StringFromGUID2: _Callable[[_Pointer[_struct.GUID], _type.LPOLESTR, _type.c_int],
                           _type.c_int] = _lib.ole32.StringFromGUID2
CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                        _type.HRESULT] = _lib.ole32.CoInitialize
CoUninitialize: _Callable[[],
                          _type.VOID] = _lib.ole32.CoUninitialize
CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],
                        _type.HRESULT] = _lib.ole32.CoCreateGuid
CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],
                             _Optional[_Pointer[_type.IUnknown]], _type.DWORD, _Pointer[_struct.IID], _type.LPVOID],
                            _type.HRESULT] = _lib.ole32.CoCreateInstance
StringFromIID: _Callable[[_Pointer[_struct.IID], _Pointer[_type.LPOLESTR]],
                         _type.HRESULT] = _lib.ole32.StringFromIID
StringFromCLSID: _Callable[[_Pointer[_struct.CLSID], _Pointer[_type.LPOLESTR]],
                           _type.HRESULT] = _lib.ole32.StringFromCLSID

SHGetFolderPathA: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPSTR],
                            _type.HRESULT] = _lib.shell32.SHGetFolderPathA
SHGetFolderPathW: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPWSTR],
                            _type.HRESULT] = _lib.shell32.SHGetFolderPathW
ILCreateFromPath: _Callable[[_type.PCTSTR],
                            _Pointer[_struct.ITEMIDLIST]] = _lib.shell32.ILCreateFromPath
ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                  _type.c_void_p] = _lib.shell32.ILFree
SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                              _Pointer[_Pointer[_struct.ITEMIDLIST]], _Pointer[_com.IShellItemArray]],
                                             _type.SHSTDAPI] = _lib.shell32.SHCreateShellItemArrayFromIDLists
SHParseDisplayName: _Callable[[_type.PCWSTR, _Optional[_Pointer[_type.IBindCtx]],
                               _Pointer[_Pointer[type[_struct.ITEMIDLIST]]], _type.SFGAOF, _Pointer[_type.SFGAOF]],
                              _type.SHSTDAPI] = _lib.shell32.SHParseDisplayName
Shell_NotifyIconA: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAA]],
                             _type.BOOL] = _lib.shell32.Shell_NotifyIconA
Shell_NotifyIconW: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAW]],
                             _type.BOOL] = _lib.shell32.Shell_NotifyIconW

GetCursorPos: _Callable[[_Pointer[_struct.POINT]],
                        _type.BOOL] = _lib.user32.GetCursorPos
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
SetSysColors: _Callable[[_type.c_int, _Pointer[_type.INT], _Pointer[_type.COLORREF]],
                        _type.BOOL] = _lib.user32.SetSysColors
GetMenu: _Callable[[_type.HWND],
                   _type.HMENU] = _lib.user32.GetMenu
GetSystemMenu: _Callable[[_type.HWND, _type.BOOL],
                         _type.HMENU] = _lib.user32.GetSystemMenu
GetSubMenu: _Callable[[_type.HMENU, _type.c_int],
                      _type.HMENU] = _lib.user32.GetSubMenu
GetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _lib.user32.GetMenuInfo
SetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _lib.user32.SetMenuInfo
DrawMenuBar: _Callable[[_type.HWND],
                       _type.BOOL] = _lib.user32.DrawMenuBar
LoadImageA: _Callable[[_type.HINSTANCE, _type.LPCSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _lib.user32.LoadImageA
LoadImageW: _Callable[[_type.HINSTANCE, _type.LPCWSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _lib.user32.LoadImageW
LoadIconA: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                     _type.HICON] = _lib.user32.LoadIconA
LoadIconW: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                     _type.HICON] = _lib.user32.LoadIconW
DestroyIcon: _Callable[[_type.HICON],
                       _type.BOOL] = _lib.user32.DestroyIcon
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
LockWorkStation: _Callable[[],
                           _type.BOOL] = _lib.user32.LockWorkStation
CreateIconFromResource: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL, _type.DWORD],
                                  _type.HICON] = _lib.user32.CreateIconFromResource
CreateIconFromResourceEx: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL,
                                     _type.DWORD, _type.c_int, _type.c_int, _type.UINT],
                                    _type.HICON] = _lib.user32.CreateIconFromResourceEx
RegisterClassExA: _Callable[[_Pointer[_struct.WNDCLASSEXA]],
                            _type.ATOM] = _lib.user32.RegisterClassExA
RegisterClassExW: _Callable[[_Pointer[_struct.WNDCLASSEXW]],
                            _type.ATOM] = _lib.user32.RegisterClassExW
UnregisterClassA: _Callable[[_type.LPCSTR, _type.HINSTANCE],
                            _type.BOOL] = _lib.user32.UnregisterClassA
UnregisterClassW: _Callable[[_type.LPCWSTR, _type.HINSTANCE],
                            _type.BOOL] = _lib.user32.UnregisterClassW
CreateWindowExA: _Callable[[_type.DWORD, _Optional[_type.LPCSTR], _Optional[_type.LPCSTR], _type.DWORD,
                            _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                            _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                           _type.HWND] = _lib.user32.CreateWindowExA
CreateWindowExW: _Callable[[_type.DWORD, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR], _type.DWORD,
                            _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                            _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                           _type.HWND] = _lib.user32.CreateWindowExW
DestroyWindow: _Callable[[_type.HWND],
                         _type.BOOL] = _lib.user32.DestroyWindow
DefWindowProcA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                          _type.LRESULT] = _lib.user32.DefWindowProcA
DefWindowProcW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                          _type.LRESULT] = _lib.user32.DefWindowProcW
GetMessageA: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                       _type.BOOL] = _lib.user32.GetMessageA
GetMessageW: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                       _type.BOOL] = _lib.user32.GetMessageW
TranslateMessage: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _lib.user32.TranslateMessage
DispatchMessageA: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _lib.user32.DispatchMessageA
DispatchMessageW: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _lib.user32.DispatchMessageW
PostQuitMessage: _Callable[[_type.c_int],
                           _type.c_void_p] = _lib.user32.PostQuitMessage
ShowWindow: _Callable[[_type.HWND, _type.c_int],
                      _type.BOOL] = _lib.user32.ShowWindow
SetTimer: _Callable[[_Optional[_type.HWND], _type.UINT_PTR, _type.UINT, _Optional[_type.TIMERPROC]],
                    _type.UINT_PTR] = _lib.user32.SetTimer
KillTimer: _Callable[[_type.HWND, _type.UINT_PTR],
                     _type.BOOL] = _lib.user32.KillTimer

GetObject = GetObjectW if _const.UNICODE else GetObjectA
GetModuleHandle = GetModuleHandleW if _const.UNICODE else GetModuleHandleA
SHGetFolderPath = SHGetFolderPathW if _const.UNICODE else SHGetFolderPathA
Shell_NotifyIcon = Shell_NotifyIconW if _const.UNICODE else Shell_NotifyIconA
SystemParametersInfo = SystemParametersInfoW if _const.UNICODE else SystemParametersInfoA
LoadImage = LoadImageW if _const.UNICODE else LoadImageA
LoadIcon = LoadIconW if _const.UNICODE else LoadIconA
FindWindow = FindWindowW if _const.UNICODE else FindWindowA
SendMessage = SendMessageW if _const.UNICODE else SendMessageA
SendMessageTimeout = SendMessageTimeoutW if _const.UNICODE else SendMessageTimeoutA
GetClassName = GetClassNameW if _const.UNICODE else GetClassNameA
GetWindowText = GetWindowTextW if _const.UNICODE else GetWindowTextA
RegisterClassEx = RegisterClassExW if _const.UNICODE else RegisterClassExA
UnregisterClass = UnregisterClassW if _const.UNICODE else UnregisterClassA
CreateWindowEx = CreateWindowExW if _const.UNICODE else CreateWindowExA
DefWindowProc = DefWindowProcW if _const.UNICODE else DefWindowProcA
GetMessage = GetMessageW if _const.UNICODE else GetMessageA
DispatchMessage = DispatchMessageW if _const.UNICODE else DispatchMessageA


# noinspection PyUnresolvedReferences,PyProtectedMember
def _init(name: str) -> _ctypes._CFuncPtr:
    _globals.has_item(name)
    func = _globals.vars_[name]
    func.restype, *func.argtypes = _resolve_type(_globals.get_annotation(name))
    func.__doc__ = _get_doc(name, func.restype, func.argtypes)
    return func


_globals = _Globals()
