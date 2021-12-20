import ctypes as _ctypes
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _com
from . import _const
from . import _lib
from . import _struct
from . import _type
from .__head__ import _Globals
from .__head__ import _Pointer
from .__head__ import _get_doc
from .__head__ import _resolve_type

SetWindowTheme: _Callable[[_type.HWND, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR]],
                          _type.HRESULT] = _lib.uxtheme

# InitPropVariantFromStringAsVector: _Callable[[_type.PCWSTR, _type.REFPROPVARIANT],
#                                              _type.PSSTDAPI] = _lib.Propsys
# InitPropVariantFromStringVector: _Callable[[_type.PCWSTR, _type.ULONG, _type.REFPROPVARIANT],
#                                            _type.PSSTDAPI] = _lib.Propsys

RoInitialize: _Callable[[_type.RO_INIT_TYPE],
                        _type.HRESULT] = _lib.combase
RoUninitialize: _Callable[[],
                          _type.c_void_p] = _lib.combase
RoActivateInstance: _Callable[[_type.HSTRING, _type.c_void_p],
                              _type.HRESULT] = _lib.combase
WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH], _type.UINT32, _Pointer[_type.HSTRING]],
                               _type.HRESULT] = _lib.combase
WindowsDeleteString: _Callable[[_type.HSTRING],
                               _type.HRESULT] = _lib.combase

GetObjectA: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _lib.gdi32
GetObjectW: _Callable[[_type.HANDLE, _type.c_int, _type.LPVOID],
                      _type.c_int] = _lib.gdi32
DeleteObject: _Callable[[_type.HGDIOBJ],
                        _type.BOOL] = _lib.gdi32
CreateDIBitmap: _Callable[[_type.HDC, _Pointer[_struct.BITMAPINFOHEADER],
                           _type.DWORD, _type.VOID, _Pointer[_struct.BITMAPINFO], _type.UINT],
                          _type.HBITMAP] = _lib.gdi32
GetDIBits: _Callable[[_type.HDC, _type.HBITMAP, _type.UINT, _type.UINT,
                      _Optional[_type.LPVOID], _Pointer[_struct.BITMAPINFO], _type.UINT],
                     _type.c_int] = _lib.gdi32
CreateSolidBrush: _Callable[[_type.COLORREF],
                            _type.HBRUSH] = _lib.gdi32
GetStockObject: _Callable[[_type.c_int],
                          _type.HGDIOBJ] = _lib.gdi32

GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],
                           _Pointer[_struct.GdiplusStartupInput], _Optional[_Pointer[_struct.GdiplusStartupInput]]],
                          _type.Status] = _lib.GdiPlus
GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                           _type.VOID] = _lib.GdiPlus
GdipLoadImageFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpImage]],
                                 _type.GpStatus] = _lib.GdiPlus
GdipDisposeImage: _Callable[[_type.GpImage],
                            _type.GpStatus] = _lib.GdiPlus
GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage, _Pointer[_type.UINT]],
                                            _type.GpStatus] = _lib.GdiPlus
GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                           _type.GpStatus] = _lib.GdiPlus
GdipImageGetFrameCount: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _Pointer[_type.UINT]],
                                  _type.GpStatus] = _lib.GdiPlus
GdipGetPropertyItemSize: _Callable[[_type.GpImage, _type.PROPID, _Pointer[_type.UINT]],
                                   _type.GpStatus] = _lib.GdiPlus
GdipGetPropertyItem: _Callable[[_type.GpImage, _type.PROPID, _type.UINT, _Pointer[_struct.PropertyItem]],
                               _type.GpStatus] = _lib.GdiPlus
GdipImageSelectActiveFrame: _Callable[[_type.GpImage, _Pointer[_struct.GUID], _type.UINT],
                                      _type.GpStatus] = _lib.GdiPlus
GdipCreateBitmapFromFile: _Callable[[_Pointer[_type.WCHAR], _Pointer[_type.GpBitmap]],
                                    _type.GpStatus] = _lib.GdiPlus
GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HBITMAP], _type.ARGB],
                                       _type.GpStatus] = _lib.GdiPlus
GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap, _Pointer[_type.HICON]],
                                     _type.GpStatus] = _lib.GdiPlus

GlobalAlloc: _Callable[[_type.UINT, _type.SIZE_T],
                       _type.HGLOBAL] = _lib.kernel32
GlobalLock: _Callable[[_type.HGLOBAL],
                      _type.LPVOID] = _lib.kernel32
GlobalUnlock: _Callable[[_type.HGLOBAL],
                        _type.BOOL] = _lib.kernel32
CloseHandle: _Callable[[_type.HANDLE],
                       _type.BOOL] = _lib.kernel32
GetLastError: _Callable[[],
                        _type.DWORD] = _lib.kernel32
GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                            _type.HMODULE] = _lib.kernel32
GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                            _type.HMODULE] = _lib.kernel32

malloc: _Callable[[_type.c_void_p],
                  _type.c_size_t] = _lib.msvcrt
free: _Callable[[_type.c_void_p],
                _type.c_void_p] = _lib.msvcrt
memmove: _Callable[[_type.c_void_p, _type.c_void_p, _type.c_size_t],
                   _type.c_void_p] = _lib.msvcrt
wcslen: _Callable[[_type.c_wchar_p],
                  _type.c_size_t] = _lib.msvcrt

RtlAreLongPathsEnabled: _Callable[[],
                                  _type.c_ubyte] = _lib.ntdll

IIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.IID]],
                         _type.HRESULT] = _lib.ole32
CLSIDFromString: _Callable[[_type.LPCOLESTR, _Pointer[_struct.CLSID]],
                           _type.HRESULT] = _lib.ole32
StringFromGUID2: _Callable[[_Pointer[_struct.GUID], _type.LPOLESTR, _type.c_int],
                           _type.c_int] = _lib.ole32
CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                        _type.HRESULT] = _lib.ole32
CoUninitialize: _Callable[[],
                          _type.VOID] = _lib.ole32
CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],
                        _type.HRESULT] = _lib.ole32
CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],
                             _Optional[_Pointer[_type.IUnknown]], _type.DWORD, _Pointer[_struct.IID], _type.LPVOID],
                            _type.HRESULT] = _lib.ole32
StringFromIID: _Callable[[_Pointer[_struct.IID], _Pointer[_type.LPOLESTR]],
                         _type.HRESULT] = _lib.ole32
StringFromCLSID: _Callable[[_Pointer[_struct.CLSID], _Pointer[_type.LPOLESTR]],
                           _type.HRESULT] = _lib.ole32

SHGetFolderPathA: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPSTR],
                            _type.HRESULT] = _lib.shell32
SHGetFolderPathW: _Callable[[_Optional[_type.HWND], _type.c_int,
                             _Optional[_type.HANDLE], _type.DWORD, _type.LPWSTR],
                            _type.HRESULT] = _lib.shell32
ILCreateFromPath: _Callable[[_type.PCTSTR],
                            _Pointer[_struct.ITEMIDLIST]] = _lib.shell32
ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                  _type.c_void_p] = _lib.shell32
SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                              _Pointer[_Pointer[_struct.ITEMIDLIST]], _Pointer[_com.IShellItemArray]],
                                             _type.SHSTDAPI] = _lib.shell32
SHOpenFolderAndSelectItems: _Callable[[_Pointer[_struct.ITEMIDLIST], _type.UINT,
                                       _Optional[_Pointer[_Pointer[_struct.ITEMIDLIST]]], _type.DWORD],
                                      _type.SHSTDAPI] = _lib.shell32
SHParseDisplayName: _Callable[[_type.PCWSTR, _Optional[_Pointer[_type.IBindCtx]],
                               _Pointer[_Pointer[type[_struct.ITEMIDLIST]]], _type.SFGAOF, _Pointer[_type.SFGAOF]],
                              _type.SHSTDAPI] = _lib.shell32
Shell_NotifyIconA: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAA]],
                             _type.BOOL] = _lib.shell32
Shell_NotifyIconW: _Callable[[_type.DWORD, _Pointer[_struct.NOTIFYICONDATAW]],
                             _type.BOOL] = _lib.shell32
ShellExecuteA: _Callable[[_Optional[_type.HWND], _Optional[_type.LPCSTR], _type.LPCSTR,
                          _Optional[_type.LPCSTR], _Optional[_type.LPCSTR], _type.INT],
                         _type.HINSTANCE] = _lib.shell32
ShellExecuteW: _Callable[[_Optional[_type.HWND], _Optional[_type.LPCWSTR], _type.LPCWSTR,
                          _Optional[_type.LPCWSTR], _Optional[_type.LPWSTR], _type.INT],
                         _type.HINSTANCE] = _lib.shell32

GetCursorPos: _Callable[[_Pointer[_struct.POINT]],
                        _type.BOOL] = _lib.user32
SystemParametersInfoA: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                 _type.BOOL] = _lib.user32
SystemParametersInfoW: _Callable[[_type.UINT, _type.UINT, _type.PVOID, _type.UINT],
                                 _type.BOOL] = _lib.user32
OpenClipboard: _Callable[[_Optional[_type.HWND]],
                         _type.BOOL] = _lib.user32
CloseClipboard: _Callable[[],
                          _type.BOOL] = _lib.user32
EmptyClipboard: _Callable[[],
                          _type.BOOL] = _lib.user32
GetClipboardData: _Callable[[_type.UINT],
                            _type.HANDLE] = _lib.user32
SetClipboardData: _Callable[[_type.UINT, _type.HANDLE],
                            _type.HANDLE] = _lib.user32
GetSysColor: _Callable[[_type.c_int],
                       _type.DWORD] = _lib.user32
SetSysColors: _Callable[[_type.c_int, _Pointer[_type.INT], _Pointer[_type.COLORREF]],
                        _type.BOOL] = _lib.user32
GetMenu: _Callable[[_type.HWND],
                   _type.HMENU] = _lib.user32
GetSystemMenu: _Callable[[_type.HWND, _type.BOOL],
                         _type.HMENU] = _lib.user32
GetSubMenu: _Callable[[_type.HMENU, _type.c_int],
                      _type.HMENU] = _lib.user32
GetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _lib.user32
SetMenuInfo: _Callable[[_type.HMENU, _Pointer[_struct.MENUINFO]],
                       _type.BOOL] = _lib.user32
DrawMenuBar: _Callable[[_type.HWND],
                       _type.BOOL] = _lib.user32
LoadImageA: _Callable[[_type.HINSTANCE, _type.LPCSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _lib.user32
LoadImageW: _Callable[[_type.HINSTANCE, _type.LPCWSTR, _type.UINT, _type.c_int, _type.c_int, _type.UINT],
                      _type.HANDLE] = _lib.user32
LoadIconA: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                     _type.HICON] = _lib.user32
LoadIconW: _Callable[[_Optional[_type.HINSTANCE], _type.UINT],
                     _type.HICON] = _lib.user32
DestroyIcon: _Callable[[_type.HICON],
                       _type.BOOL] = _lib.user32
GetDC: _Callable[[_Optional[_type.HWND]],
                 _type.HDC] = _lib.user32
GetWindowDC: _Callable[[_Optional[_type.HWND]],
                       _type.HDC] = _lib.user32
ReleaseDC: _Callable[[_Optional[_type.HWND], _type.HDC],
                     _type.c_int] = _lib.user32
FindWindowA: _Callable[[_type.LPCSTR, _Optional[_type.LPCSTR]],
                       _type.HWND] = _lib.user32
FindWindowW: _Callable[[_type.LPCWSTR, _Optional[_type.LPCWSTR]],
                       _type.HWND] = _lib.user32
SendMessageA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                        _type.LRESULT] = _lib.user32
SendMessageW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                        _type.LRESULT] = _lib.user32
SendMessageTimeoutA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                               _type.LRESULT] = _lib.user32
SendMessageTimeoutW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM,
                                _type.UINT, _type.UINT, _Optional[_type.PDWORD_PTR]],
                               _type.LRESULT] = _lib.user32
GetClassNameA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                         _type.c_int] = _lib.user32
GetClassNameW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                         _type.c_int] = _lib.user32
GetWindowTextA: _Callable[[_type.HWND, _type.LPSTR, _type.c_int],
                          _type.c_int] = _lib.user32
GetWindowTextW: _Callable[[_type.HWND, _type.LPWSTR, _type.c_int],
                          _type.c_int] = _lib.user32
LockWorkStation: _Callable[[],
                           _type.BOOL] = _lib.user32
CreateIconFromResource: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL, _type.DWORD],
                                  _type.HICON] = _lib.user32
CreateIconFromResourceEx: _Callable[[_type.PBYTE, _type.DWORD, _type.BOOL,
                                     _type.DWORD, _type.c_int, _type.c_int, _type.UINT],
                                    _type.HICON] = _lib.user32
RegisterClassExA: _Callable[[_Pointer[_struct.WNDCLASSEXA]],
                            _type.ATOM] = _lib.user32
RegisterClassExW: _Callable[[_Pointer[_struct.WNDCLASSEXW]],
                            _type.ATOM] = _lib.user32
UnregisterClassA: _Callable[[_type.LPCSTR, _type.HINSTANCE],
                            _type.BOOL] = _lib.user32
UnregisterClassW: _Callable[[_type.LPCWSTR, _type.HINSTANCE],
                            _type.BOOL] = _lib.user32
CreateWindowExA: _Callable[[_type.DWORD, _Optional[_type.LPCSTR], _Optional[_type.LPCSTR], _type.DWORD,
                            _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                            _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                           _type.HWND] = _lib.user32
CreateWindowExW: _Callable[[_type.DWORD, _Optional[_type.LPCWSTR], _Optional[_type.LPCWSTR], _type.DWORD,
                            _type.c_int, _type.c_int, _type.c_int, _type.c_int, _Optional[_type.HWND],
                            _Optional[_type.HMENU], _Optional[_type.HINSTANCE], _Optional[_type.LPVOID]],
                           _type.HWND] = _lib.user32
DestroyWindow: _Callable[[_type.HWND],
                         _type.BOOL] = _lib.user32
DefWindowProcA: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                          _type.LRESULT] = _lib.user32
DefWindowProcW: _Callable[[_type.HWND, _type.UINT, _type.WPARAM, _type.LPARAM],
                          _type.LRESULT] = _lib.user32
GetMessageA: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                       _type.BOOL] = _lib.user32
GetMessageW: _Callable[[_Pointer[_struct.MSG], _Optional[_type.HWND], _type.UINT, _type.UINT],
                       _type.BOOL] = _lib.user32
TranslateMessage: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _lib.user32
DispatchMessageA: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _lib.user32
DispatchMessageW: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL] = _lib.user32
PostQuitMessage: _Callable[[_type.c_int],
                           _type.c_void_p] = _lib.user32
ShowWindow: _Callable[[_type.HWND, _type.c_int],
                      _type.BOOL] = _lib.user32
SetTimer: _Callable[[_Optional[_type.HWND], _type.UINT_PTR, _type.UINT, _Optional[_type.TIMERPROC]],
                    _type.UINT_PTR] = _lib.user32
KillTimer: _Callable[[_type.HWND, _type.UINT_PTR],
                     _type.BOOL] = _lib.user32

GetObject = GetObjectW or GetObjectA
GetModuleHandle = GetModuleHandleW or GetModuleHandleA
SHGetFolderPath = SHGetFolderPathW or SHGetFolderPathA
Shell_NotifyIcon = Shell_NotifyIconW or Shell_NotifyIconA
ShellExecute = ShellExecuteW or ShellExecuteA
SystemParametersInfo = SystemParametersInfoW or SystemParametersInfoA
LoadImage = LoadImageW or LoadImageA
LoadIcon = LoadIconW or LoadIconA
FindWindow = FindWindowW or FindWindowA
SendMessage = SendMessageW or SendMessageA
SendMessageTimeout = SendMessageTimeoutW or SendMessageTimeoutA
GetClassName = GetClassNameW or GetClassNameA
GetWindowText = GetWindowTextW or GetWindowTextA
RegisterClassEx = RegisterClassExW or RegisterClassExA
UnregisterClass = UnregisterClassW or UnregisterClassA
CreateWindowEx = CreateWindowExW or CreateWindowExA
DefWindowProc = DefWindowProcW or DefWindowProcA
GetMessage = GetMessageW or GetMessageA
DispatchMessage = DispatchMessageW or DispatchMessageA


# noinspection PyUnresolvedReferences,PyProtectedMember
def _init(name: str) -> _ctypes._CFuncPtr:
    _globals.has_item(name)
    try:
        _globals.vars_.__getitem__(f'{name}W')
    except KeyError:
        pass
    else:
        name = f'{name}{"W" if _const.UNICODE else "A"}'
    func = getattr(_globals.vars_[name], name)
    func.restype, *func.argtypes = _resolve_type(_globals.get_annotation(name))
    func.__doc__ = _get_doc(name, func.restype, func.argtypes)
    return func


_globals = _Globals(True)
