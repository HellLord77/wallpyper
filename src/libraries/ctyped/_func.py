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
from .__head__ import replace_object as _replace_object
from .__head__ import resolve_type as _resolve_type


class _Func:
    lib = None
    name = None
    restype = None
    argtypes = None
    func = None

    def __call__(self, *args, **kwargs):
        if not self.func:
            self.func = getattr(getattr(_lib, self.lib), self.name)
            self.func.restype = self.restype
            self.func.argtypes = self.argtypes
            self.func.__doc__ = self.__doc__
            _replace_object(self, self.func)
        return self.func(*args, **kwargs)

    @classmethod
    def init(cls, lib: str) -> _Callable:
        func = cls()
        func.lib = lib
        return func


SetWindowTheme: _Callable[[_type.HWND, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR]],
                          _type.HRESULT] = _Func.init('uxtheme')

RoInitialize: _Callable[[_type.RO_INIT_TYPE],
                        _type.HRESULT] = _Func.init('combase')
RoUninitialize: _Callable[[],
                          _type.c_void_p] = _Func.init('combase')
RoActivateInstance: _Callable[[_type.HSTRING, _type.c_void_p],
                              _type.HRESULT] = _Func.init('combase')
WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH], _type.UINT32, _Pointer[_type.HSTRING]],
                               _type.HRESULT] = _Func.init('combase')
WindowsDeleteString: _Callable[[_type.HSTRING],
                               _type.HRESULT] = _Func.init('combase')

GetObjectA: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _Func.init('gdi32')
GetObjectW: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _Func.init('gdi32')
DeleteObject: _Callable[[_type.HGDIOBJ],
                        _type.BOOL] = _Func.init('gdi32')
CreateDIBitmap: _Callable[[_type.HDC, _Pointer[_struct.BITMAPINFOHEADER],
                           _type.DWORD, _type.VOID, _Pointer[_struct.BITMAPINFO], _type.UINT],
                          _type.HBITMAP] = _Func.init('gdi32')
GetDIBits: _Callable[[_type.HDC, _type.HBITMAP, _type.UINT, _type.UINT,
                      _Optional[_type.LPVOID], _Pointer[_struct.BITMAPINFO], _type.UINT],
                     _type.c_int] = _Func.init('gdi32')
CreateSolidBrush: _Callable[[_type.COLORREF],
                            _type.HBRUSH] = _Func.init('gdi32')
GetStockObject: _Callable[[_type.c_int],
                          _type.HGDIOBJ] = _Func.init('gdi32')

GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],
                           _Pointer[_struct.GdiplusStartupInput], _Optional[_Pointer[_struct.GdiplusStartupInput]]],
                          _type.Status] = _Func.init('GdiPlus')
GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                           _type.VOID] = _Func.init('GdiPlus')
GdipLoadImageFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpImage]],
                                 _type.GpStatus] = _Func.init('GdiPlus')
GdipDisposeImage: _Callable[[_type.GpImage],
                            _type.GpStatus] = _Func.init('GdiPlus')
GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage, _Pointer[_type.UINT]],
                                            _type.GpStatus] = _Func.init('GdiPlus')
GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                           _type.GpStatus] = _Func.init('GdiPlus')
GdipImageGetFrameCount: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _Pointer[_type.UINT]],
                                  _type.GpStatus] = _Func.init('GdiPlus')
GdipGetPropertyItemSize: _Callable[[_type.GpImage, _type.PROPID, _Pointer[_type.UINT]],
                                   _type.GpStatus] = _Func.init('GdiPlus')
GdipGetPropertyItem: _Callable[[_type.GpImage, _type.PROPID, _type.UINT, _Pointer[_struct.PropertyItem]],
                               _type.GpStatus] = _Func.init('GdiPlus')
GdipImageSelectActiveFrame: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                      _type.GpStatus] = _Func.init('GdiPlus')
GdipCreateBitmapFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpBitmap]],
                                    _type.GpStatus] = _Func.init('GdiPlus')
GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HBITMAP], _type.ARGB],
                                       _type.GpStatus] = _Func.init('GdiPlus')
GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HICON]],
                                     _type.GpStatus] = _Func.init('GdiPlus')

GlobalAlloc: _Callable[[_type.UINT, _type.SIZE_T],
                       _type.HGLOBAL] = _Func.init('kernel32')
GlobalLock: _Callable[[_type.HGLOBAL],
                      _type.LPVOID] = _Func.init('kernel32')
GlobalUnlock: _Callable[[_type.HGLOBAL],
                        _type.BOOL] = _Func.init('kernel32')
CloseHandle: _Callable[[_type.HANDLE],
                       _type.BOOL] = _Func.init('kernel32')
GetLastError: _Callable[[],
                        _type.DWORD] = _Func.init('kernel32')
GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                            _type.HMODULE] = _Func.init('kernel32')
GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                            _type.HMODULE] = _Func.init('kernel32')

malloc: _Callable[[_type.c_void_p],
                  _type.c_size_t] = _Func.init('msvcrt')
free: _Callable[[_type.c_void_p],
                _type.c_void_p] = _Func.init('msvcrt')
memmove: _Callable[[_type.c_void_p, _type.c_void_p, _type.c_size_t],
                   _type.c_void_p] = _Func.init('msvcrt')
wcslen: _Callable[[_type.c_wchar_p],
                  _type.c_size_t] = _Func.init('msvcrt')

RtlAreLongPathsEnabled: _Callable[[],
                                  _type.c_ubyte] = _lib.ntdll.RtlAreLongPathsEnabled

IIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.IID]],
                         _type.HRESULT] = _Func.init('ole32')
CLSIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.CLSID]],
                           _type.HRESULT] = _Func.init('ole32')
StringFromGUID2: _Callable[[_Pointer[_struct.GUID], _type.LPOLESTR, _type.c_int],
                           _type.c_int] = _Func.init('ole32')
CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                        _type.HRESULT] = _Func.init('ole32')
CoUninitialize: _Callable[[],
                          _type.VOID] = _Func.init('ole32')
CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],
                        _type.HRESULT] = _Func.init('ole32')
CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],
                             _Optional[_Pointer[_type.IUnknown]], _type.DWORD, _Pointer[_struct.IID], _type.LPVOID],
                            _type.HRESULT] = _Func.init('ole32')
StringFromIID: _Callable[[_Pointer[_struct.IID], _Pointer[_type.LPOLESTR]],
                         _type.HRESULT] = _Func.init('ole32')
StringFromCLSID: _Callable[[_Pointer[_struct.CLSID], _Pointer[_type.LPOLESTR]],
                           _type.HRESULT] = _Func.init('ole32')

SHGetFolderPathA: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPSTR],
                            _type.HRESULT] = _Func.init('shell32')
SHGetFolderPathW: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPWSTR],
                            _type.HRESULT] = _Func.init('shell32')
ILCreateFromPath: _Callable[[_type.PCTSTR],
                            _Pointer[_struct.ITEMIDLIST]] = _Func.init('shell32')
ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                  _type.c_void_p] = _Func.init('shell32')
SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                              _Pointer[_Pointer[_struct.ITEMIDLIST]], _Pointer[_com.IShellItemArray]],
                                             _type.SHSTDAPI] = _Func.init('shell32')
SHParseDisplayName: _Callable[[_type.PCWSTR, _Optional[_Pointer[_type.IBindCtx]],
                               _Pointer[_Pointer[type[_struct.ITEMIDLIST]]], _type.SFGAOF, _Pointer[_type.SFGAOF]],
                              _type.SHSTDAPI] = _Func.init('shell32')
Shell_NotifyIconA: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAA]],
                             _type.BOOL] = _Func.init('shell32')
Shell_NotifyIconW: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAW]],
                             _type.BOOL] = _Func.init('shell32')

GetCursorPos: _Callable[[_Pointer[_struct.POINT]],
                        _type.BOOL] = _Func.init('user32')
SystemParametersInfoA: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                 _type.BOOL] = _Func.init('user32')
SystemParametersInfoW: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                 _type.BOOL] = _Func.init('user32')
OpenClipboard: _Callable[[_Optional[_type.HWND]],
                         _type.BOOL] = _Func.init('user32')
CloseClipboard: _Callable[[],
                          _type.BOOL] = _Func.init('user32')
EmptyClipboard: _Callable[[],
                          _type.BOOL] = _Func.init('user32')
GetClipboardData: _Callable[[_type.UINT],
                            _type.HANDLE] = _Func.init('user32')
SetClipboardData: _Callable[[_type.UINT, _type.HANDLE],
                            _type.HANDLE] = _Func.init('user32')
GetSysColor: _Callable[[_type.c_int],
                       _type.DWORD] = _Func.init('user32')
SetSysColors: _Callable[[_type.c_int, _Pointer[_type.INT], _Pointer[_type.COLORREF]],
                        _type.BOOL] = _Func.init('user32')
GetMenu: _Callable[[_type.HWND],
                   _type.HMENU] = _Func.init('user32')
GetSystemMenu: _Callable[[_type.HWND, _type.BOOL],
                         _type.HMENU] = _Func.init('user32')
GetSubMenu: _Callable[[_type.HMENU, _type.c_int],
                      _type.HMENU] = _Func.init('user32')
GetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _Func.init('user32')
SetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _Func.init('user32')
DrawMenuBar: _Callable[[_type.HWND],
                       _type.BOOL] = _Func.init('user32')
LoadImageA: _Callable[[_type.HINSTANCE, _type.LPCSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _Func.init('user32')
LoadImageW: _Callable[[_type.HINSTANCE, _type.LPCWSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _Func.init('user32')
LoadIconA: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                     _type.HICON] = _Func.init('user32')
LoadIconW: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                     _type.HICON] = _Func.init('user32')
DestroyIcon: _Callable[[_type.HICON],
                       _type.BOOL] = _Func.init('user32')
GetDC: _Callable[[_Optional[_type.HWND]],
                 _type.HDC] = _Func.init('user32')
GetWindowDC: _Callable[[_Optional[_type.HWND]],
                       _type.HDC] = _Func.init('user32')
ReleaseDC: _Callable[[_Optional[_type.HWND], _type.HDC],
                     _type.c_int] = _Func.init('user32')
FindWindowA: _Callable[[_type.LPCSTR, _Optional[_type.LPCSTR]],
                       _type.HWND] = _Func.init('user32')
FindWindowW: _Callable[[_type.LPCWSTR, _Optional[_type.LPCWSTR]],
                       _type.HWND] = _Func.init('user32')
SendMessageA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                        _type.LRESULT] = _Func.init('user32')
SendMessageW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                        _type.LRESULT] = _Func.init('user32')
SendMessageTimeoutA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                               _type.LRESULT] = _Func.init('user32')
SendMessageTimeoutW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                               _type.LRESULT] = _Func.init('user32')
GetClassNameA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                         _type.c_int] = _Func.init('user32')
GetClassNameW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                         _type.c_int] = _Func.init('user32')
GetWindowTextA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                          _type.c_int] = _Func.init('user32')
GetWindowTextW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                          _type.c_int] = _Func.init('user32')
LockWorkStation: _Callable[[],
                           _type.BOOL] = _Func.init('user32')
CreateIconFromResource: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL, _type.DWORD],
                                  _type.HICON] = _Func.init('user32')
CreateIconFromResourceEx: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL,
                                     _type.DWORD, _type.c_int, _type.c_int, _type.UINT],
                                    _type.HICON] = _Func.init('user32')
RegisterClassExA: _Callable[[_Pointer[_struct.WNDCLASSEXA]],
                            _type.ATOM] = _Func.init('user32')
RegisterClassExW: _Callable[[_Pointer[_struct.WNDCLASSEXW]],
                            _type.ATOM] = _Func.init('user32')
UnregisterClassA: _Callable[[_type.LPCSTR, _type.HINSTANCE],
                            _type.BOOL] = _Func.init('user32')
UnregisterClassW: _Callable[[_type.LPCWSTR, _type.HINSTANCE],
                            _type.BOOL] = _Func.init('user32')
CreateWindowExA: _Callable[[_type.DWORD, _Optional[_type.LPCSTR], _Optional[_type.LPCSTR], _type.DWORD,
                            _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                            _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                           _type.HWND] = _Func.init('user32')
CreateWindowExW: _Callable[[_type.DWORD, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR], _type.DWORD,
                            _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                            _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                           _type.HWND] = _Func.init('user32')
DestroyWindow: _Callable[[_type.HWND],
                         _type.BOOL] = _Func.init('user32')
DefWindowProcA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                          _type.LRESULT] = _Func.init('user32')
DefWindowProcW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                          _type.LRESULT] = _Func.init('user32')
GetMessageA: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                       _type.BOOL] = _Func.init('user32')
GetMessageW: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                       _type.BOOL] = _Func.init('user32')
TranslateMessage: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _Func.init('user32')
DispatchMessageA: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _Func.init('user32')
DispatchMessageW: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _Func.init('user32')
PostQuitMessage: _Callable[[_type.c_int],
                           _type.c_void_p] = _Func.init('user32')
ShowWindow: _Callable[[_type.HWND, _type.c_int],
                      _type.BOOL] = _Func.init('user32')
SetTimer: _Callable[[_Optional[_type.HWND], _type.UINT_PTR, _type.UINT, _Optional[_type.TIMERPROC]],
                    _type.UINT_PTR] = _Func.init('user32')
KillTimer: _Callable[[_type.HWND, _type.UINT_PTR],
                     _type.BOOL] = _Func.init('user32')

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
    try:
        unicode = _globals.vars_[f'{name}W']
    except KeyError:
        func.name = name
    else:
        func.name = f'{name}{"W" if unicode is func else "A"}'
    func.restype, *func.argtypes = _resolve_type(_globals.get_annotation(name))
    func.__doc__ = _get_doc(name, func.restype, func.argtypes)
    return func


_globals = _Globals()
