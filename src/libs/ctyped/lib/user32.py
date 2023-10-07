from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

MessageBoxTimeoutA: _Callable[[_Optional[_type.HWND],  # hWnd
                               _Optional[_type.LPCSTR],  # lpText
                               _Optional[_type.LPCSTR],  # lpCaption
                               _type.UINT,  # uType
                               _type.WORD,  # wLanguageId
                               _type.DWORD],  # dwMilliseconds
                              _type.c_int]
MessageBoxTimeoutW: _Callable[[_Optional[_type.HWND],  # hWnd
                               _Optional[_type.LPCWSTR],  # lpText
                               _Optional[_type.LPCWSTR],  # lpCaption
                               _type.UINT,  # uType
                               _type.WORD,  # wLanguageId
                               _type.DWORD],  # dwMilliseconds
                              _type.c_int]
GetWindowCompositionAttribute: _Callable[[_type.HWND,  # hwnd
                                          _Pointer[_struct.WINDOWCOMPOSITIONATTRIBDATA]],  # pAttrData
                                         _type.BOOL]
SetWindowCompositionAttribute: _Callable[[_type.HWND,  # hwnd
                                          _Pointer[_struct.WINDOWCOMPOSITIONATTRIBDATA]],  # pAttrData
                                         _type.BOOL]
# WinUser
GetWindowTextA: _Callable[[_type.HWND,  # hWnd
                           _type.LPSTR,  # lpString
                           _type.c_int],  # nMaxCount
                          _type.c_int]
GetWindowTextW: _Callable[[_type.HWND,  # hWnd
                           _type.LPWSTR,  # lpString
                           _type.c_int],  # nMaxCount
                          _type.c_int]
GetWindowTextLengthA: _Callable[[_type.HWND],  # hWnd
                                _type.c_int]
GetWindowTextLengthW: _Callable[[_type.HWND],  # hWnd
                                _type.c_int]
MessageBoxA: _Callable[[_Optional[_type.HWND],  # hWnd
                        _Optional[_type.LPCSTR],  # lpText
                        _Optional[_type.LPCSTR],  # lpCaption
                        _type.UINT],
                       _type.c_int]
MessageBoxW: _Callable[[_Optional[_type.HWND],  # hWnd
                        _Optional[_type.LPCWSTR],  # lpText
                        _Optional[_type.LPCWSTR],  # lpCaption
                        _type.UINT],
                       _type.c_int]
GetShellWindow: _Callable[[],
                          _type.HWND]
RegisterShellHookWindow: _Callable[[_type.HWND],  # hwnd
                                   _type.BOOL]
DeregisterShellHookWindow: _Callable[[_type.HWND],  # hwnd
                                     _type.BOOL]
EnumWindows: _Callable[[_type.WNDENUMPROC,  # lpEnumFunc
                        _type.LPARAM],  # lParam
                       _type.BOOL]
EnumThreadWindows: _Callable[[_type.DWORD,  # dwThreadId
                              _type.WNDENUMPROC,  # lpfn
                              _type.LPARAM],  # lParam
                             _type.BOOL]
GetClassNameA: _Callable[[_type.HWND,  # hWnd
                          _type.LPSTR,  # lpClassName
                          _type.c_int],  # nMaxCount
                         _type.c_int]
GetClassNameW: _Callable[[_type.HWND,  # hWnd
                          _type.LPWSTR,  # lpClassName
                          _type.c_int],  # nMaxCount
                         _type.c_int]
GetTopWindow: _Callable[[_Optional[_type.HWND]],  # hWnd
                        _type.HWND]
GetWindowThreadProcessId: _Callable[[_type.HWND,  # hWnd
                                     _Optional[_Pointer[_type.DWORD]]],  # lpdwProcessId
                                    _type.DWORD]
IsGUIThread: _Callable[[_type.BOOL],  # bConvert
                       _type.BOOL]
GetLastActivePopup: _Callable[[_type.HWND],  # hWnd
                              _type.HWND]
GetWindow: _Callable[[_type.HWND,  # hWnd
                      _type.UINT],  # uCmd
                     _type.HWND]
SetWindowsHookA: _Callable[[_type.c_int,  # nFilterType
                            _type.HOOKPROC],  # pfnFilterProc
                           _type.HHOOK]
SetWindowsHookW: _Callable[[_type.c_int,  # nFilterType
                            _type.HOOKPROC],  # pfnFilterProc
                           _type.HHOOK]
UnhookWindowsHook: _Callable[[_type.c_int,  # nCode
                              _type.HOOKPROC],  # pfnFilterProc
                             _type.BOOL]
SetWindowsHookExA: _Callable[[_type.c_int,  # idHook
                              _type.HOOKPROC,  # lpfn
                              _type.HINSTANCE,  # hmod
                              _type.DWORD],  # dwThreadId
                             _type.HHOOK]
SetWindowsHookExW: _Callable[[_type.c_int,  # idHook
                              _type.HOOKPROC,  # lpfn
                              _type.HINSTANCE,  # hmod
                              _type.DWORD],  # dwThreadId
                             _type.HHOOK]
UnhookWindowsHookEx: _Callable[[_type.HHOOK],  # hhk
                               _type.BOOL]
CallNextHookEx: _Callable[[_Optional[_type.HHOOK],  # hhk
                           _type.c_int,  # nCode
                           _type.WPARAM,  # wParam
                           _type.LPARAM],  # lParam
                          _type.LRESULT]
CheckMenuRadioItem: _Callable[[_type.HMENU,  # hmenu
                               _type.UINT,  # first
                               _type.UINT,  # last
                               _type.UINT,  # check
                               _type.UINT],  # flags
                              _type.BOOL]
LoadBitmapA: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                        _type.LPCSTR],  # lpBitmapName
                       _type.HBITMAP]
LoadBitmapW: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                        _type.LPCWSTR],  # lpBitmapName
                       _type.HBITMAP]
LoadCursorA: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                        _type.LPCSTR],  # lpCursorName
                       _type.HCURSOR]
LoadCursorW: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                        _type.LPCWSTR],  # lpCursorName
                       _type.HCURSOR]
LoadCursorFromFileA: _Callable[[_type.LPCSTR],  # lpFileName
                               _type.HCURSOR]
LoadCursorFromFileW: _Callable[[_type.LPCWSTR],  # lpFileName
                               _type.HCURSOR]
DestroyCursor: _Callable[[_type.HCURSOR],  # hCursor
                         _type.BOOL]
SetSystemCursor: _Callable[[_type.HCURSOR,  # hcur
                            _type.DWORD],  # id
                           _type.BOOL]
LoadIconA: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                      _type.UINT],  # lpIconName
                     _type.HICON]
LoadIconW: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                      _type.LPCWSTR],  # lpIconName
                     _type.HICON]
DestroyIcon: _Callable[[_type.HICON],  # hIcon
                       _type.BOOL]
SetThreadCursorCreationScaling: _Callable[[_type.UINT],  # cursorDpi
                                          _type.UINT]
SetLastErrorEx: _Callable[[_type.DWORD,  # dwErrCode
                           _type.DWORD],  # dwType
                          _type.VOID]
CancelShutdown: _Callable[[],
                          _type.BOOL]
MonitorFromPoint: _Callable[[_struct.POINT,  # pt,
                             _type.DWORD],  # dwFlags
                            _type.HMONITOR]
MonitorFromRect: _Callable[[_Pointer[_struct.RECT],  # lprc,
                            _type.DWORD],  # dwFlags
                           _type.HMONITOR]
MonitorFromWindow: _Callable[[_type.HWND,  # hwnd,
                              _type.DWORD],  # dwFlags
                             _type.HMONITOR]
# TODO
wvsprintfA: _Callable[[_type.LPSTR,
                       _type.LPCSTR,
                       _type.va_list],
                      _type.c_int]
wvsprintfW: _Callable[[_type.LPWSTR,
                       _type.LPCWSTR,
                       _type.va_list],
                      _type.c_int]
AdjustWindowRect: _Callable[[_Pointer[_struct.RECT],
                             _type.DWORD,
                             _type.BOOL],
                            _type.BOOL]
AdjustWindowRectEx: _Callable[[_Pointer[_struct.RECT],
                               _type.DWORD,
                               _type.BOOL,
                               _type.DWORD],
                              _type.BOOL]
AllowSetForegroundWindow: _Callable[[_type.DWORD],
                                    _type.BOOL]
AnimateWindow: _Callable[[_type.HWND,
                          _type.DWORD,
                          _type.DWORD],
                         _type.BOOL]
AnyPopup: _Callable[[],
                    _type.BOOL]
AppendMenuA: _Callable[[_type.HMENU,
                        _type.UINT,
                        _type.UINT_PTR,
                        _Optional[_type.LPCSTR]],
                       _type.BOOL]
AppendMenuW: _Callable[[_type.HMENU,
                        _type.UINT,
                        _type.UINT_PTR,
                        _Optional[_type.LPCWSTR]],
                       _type.BOOL]
AttachThreadInput: _Callable[[_type.DWORD,
                              _type.DWORD,
                              _type.BOOL],
                             _type.BOOL]
BeginDeferWindowPos: _Callable[[_type.c_int],
                               _type.BOOL]
BeginPaint: _Callable[[_type.HWND,
                       _Pointer[_struct.PAINTSTRUCT]],
                      _type.HDC]
BlockInput: _Callable[[_type.BOOL],
                      _type.BOOL]
BringWindowToTop: _Callable[[_type.HWND],
                            _type.BOOL]
BroadcastSystemMessageA: _Callable[[_type.DWORD,
                                    _Optional[_Pointer[_type.DWORD]],
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM],
                                   _type.c_long]
BroadcastSystemMessageW: _Callable[[_type.DWORD,
                                    _Optional[_Pointer[_type.DWORD]],
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM],
                                   _type.c_long]
BroadcastSystemMessageExA: _Callable[[_type.DWORD,
                                      _Optional[_Pointer[_type.DWORD]],
                                      _type.UINT,
                                      _type.WPARAM,
                                      _type.LPARAM,
                                      _Optional[_Pointer[_struct.BSMINFO]]],
                                     _type.c_long]
BroadcastSystemMessageExW: _Callable[[_type.DWORD,
                                      _Optional[_Pointer[_type.DWORD]],
                                      _type.UINT,
                                      _type.WPARAM,
                                      _type.LPARAM,
                                      _Optional[_Pointer[_struct.BSMINFO]]],
                                     _type.c_long]
CalculatePopupWindowPosition: _Callable[[_Pointer[_struct.POINT],
                                         _Pointer[_struct.SIZE],
                                         _type.UINT,
                                         _Optional[_Pointer[_struct.RECT]],
                                         _Pointer[_struct.RECT]],
                                        _type.BOOL]
ChangeMenuA: _Callable[[_type.HMENU,
                        _type.UINT,
                        _Optional[_type.LPCSTR],
                        _type.UINT,
                        _type.UINT],
                       _type.BOOL]
ChangeMenuW: _Callable[[_type.HMENU,
                        _type.UINT,
                        _Optional[_type.LPCWSTR],
                        _type.UINT,
                        _type.UINT],
                       _type.BOOL]
CheckDlgButton: _Callable[[_type.HWND,
                           _type.c_int,
                           _type.UINT],
                          _type.BOOL]
CheckMenuItem: _Callable[[_type.HMENU,
                          _type.UINT,
                          _type.UINT],
                         _type.DWORD]
CheckRadioButton: _Callable[[_type.HWND,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int],
                            _type.BOOL]
ClientToScreen: _Callable[[_type.HWND,
                           _Pointer[_struct.POINT]],
                          _type.BOOL]
ScreenToClient: _Callable[[_type.HWND,
                           _Pointer[_struct.POINT]],
                          _type.BOOL]
CloseClipboard: _Callable[[],
                          _type.BOOL]
CloseWindow: _Callable[[_type.HWND],
                       _type.BOOL]
CreateDialogIndirectParamA: _Callable[[_Optional[_type.HINSTANCE],
                                       _Pointer[_struct.DLGTEMPLATE],
                                       _Optional[_type.HWND],
                                       _Optional[_type.DLGPROC],
                                       _type.LPARAM],
                                      _type.HWND]
CreateDialogIndirectParamW: _Callable[[_Optional[_type.HINSTANCE],
                                       _Pointer[_struct.DLGTEMPLATE],
                                       _Optional[_type.HWND],
                                       _Optional[_type.DLGPROC],
                                       _type.LPARAM],
                                      _type.HWND]
CreateDialogParamA: _Callable[[_Optional[_type.HINSTANCE],
                               _type.LPCSTR,
                               _Optional[_type.HWND],
                               _Optional[_type.DLGPROC],
                               _type.LPARAM],
                              _type.HWND]
CreateDialogParamW: _Callable[[_Optional[_type.HINSTANCE],
                               _type.LPCWSTR,
                               _Optional[_type.HWND],
                               _Optional[_type.DLGPROC],
                               _type.LPARAM],
                              _type.HWND]
CreateIconFromResource: _Callable[[_type.PBYTE,
                                   _type.DWORD,
                                   _type.BOOL,
                                   _type.DWORD],
                                  _type.HICON]
CreateIconFromResourceEx: _Callable[[_type.PBYTE,
                                     _type.DWORD,
                                     _type.BOOL,
                                     _type.DWORD,
                                     _type.c_int,
                                     _type.c_int,
                                     _type.UINT],
                                    _type.HICON]
CreateMenu: _Callable[[],
                      _type.HMENU]
CreatePopupMenu: _Callable[[],
                           _type.HMENU]
CreateWindowExA: _Callable[[_type.DWORD,
                            _Optional[_type.LPCSTR],
                            _Optional[_type.LPCSTR],
                            _type.DWORD,
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _Optional[_type.HWND],
                            _Optional[_type.HMENU],
                            _Optional[_type.HINSTANCE],
                            _Optional[_type.LPVOID]],
                           _type.HWND]
CreateWindowExW: _Callable[[_type.DWORD,
                            _Optional[_type.LPCWSTR],
                            _Optional[_type.LPCWSTR],
                            _type.DWORD,
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _Optional[_type.HWND],
                            _Optional[_type.HMENU],
                            _Optional[_type.HINSTANCE],
                            _Optional[_type.LPVOID]],
                           _type.HWND]
DeferWindowPos: _Callable[[_type.HDWP,
                           _type.HWND,
                           _Optional[_type.HWND],
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.UINT],
                          _type.HDWP]
DefDlgProcA: _Callable[[_type.HWND,
                        _type.UINT,
                        _type.WPARAM,
                        _type.LPARAM],
                       _type.LRESULT]
DefDlgProcW: _Callable[[_type.HWND,
                        _type.UINT,
                        _type.WPARAM,
                        _type.LPARAM],
                       _type.LRESULT]
DefWindowProcA: _Callable[[_type.HWND,
                           _type.UINT,
                           _type.WPARAM,
                           _type.LPARAM],
                          _type.LRESULT]
DefWindowProcW: _Callable[[_type.HWND,
                           _type.UINT,
                           _type.WPARAM,
                           _type.LPARAM],
                          _type.LRESULT]
DeleteMenu: _Callable[[_type.HMENU,
                       _type.UINT,
                       _type.UINT],
                      _type.BOOL]
DestroyMenu: _Callable[[_type.HMENU],
                       _type.BOOL]
DestroyWindow: _Callable[[_type.HWND],
                         _type.BOOL]
DialogBoxIndirectParamA: _Callable[[_Optional[_type.HINSTANCE],
                                    _Pointer[_struct.DLGTEMPLATE],
                                    _Optional[_type.HWND],
                                    _Optional[_type.DLGPROC],
                                    _type.LPARAM],
                                   _type.INT_PTR]
DialogBoxIndirectParamW: _Callable[[_Optional[_type.HINSTANCE],
                                    _Pointer[_struct.DLGTEMPLATE],
                                    _Optional[_type.HWND],
                                    _Optional[_type.DLGPROC],
                                    _type.LPARAM],
                                   _type.INT_PTR]
DialogBoxParamA: _Callable[[_Optional[_type.HINSTANCE],
                            _type.LPCSTR,
                            _Optional[_type.HWND],
                            _Optional[_type.DLGPROC],
                            _type.LPARAM],
                           _type.INT_PTR]
DialogBoxParamW: _Callable[[_Optional[_type.HINSTANCE],
                            _type.LPCWSTR,
                            _Optional[_type.HWND],
                            _Optional[_type.DLGPROC],
                            _type.LPARAM],
                           _type.INT_PTR]
DispatchMessageA: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL]
DispatchMessageW: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL]
DisplayConfigGetDeviceInfo: _Callable[[_Pointer[_struct.DISPLAYCONFIG_DEVICE_INFO_HEADER]],
                                      _type.LONG]
DisplayConfigSetDeviceInfo: _Callable[[_Pointer[_struct.DISPLAYCONFIG_DEVICE_INFO_HEADER]],
                                      _type.LONG]
DragDetect: _Callable[[_type.HWND,
                       _struct.POINT],
                      _type.BOOL]
DragObject: _Callable[[_type.HWND,
                       _type.HWND,
                       _type.UINT,
                       _type.ULONG_PTR,
                       _Optional[_type.HCURSOR]],
                      _type.DWORD]
DrawIcon: _Callable[[_type.HDC,
                     _type.c_int,
                     _type.c_int,
                     _type.HICON],
                    _type.BOOL]
DrawMenuBar: _Callable[[_type.HWND],
                       _type.BOOL]
EmptyClipboard: _Callable[[],
                          _type.BOOL]
EnableMenuItem: _Callable[[_type.HMENU,
                           _type.UINT,
                           _type.UINT],
                          _type.BOOL]
EnableNonClientDpiScaling: _Callable[[_type.HWND],
                                     _type.BOOL]
EndDeferWindowPos: _Callable[[_type.HDWP],
                             _type.BOOL]
EndDialog: _Callable[[_type.HWND,
                      _type.INT_PTR],
                     _type.BOOL]
EndMenu: _Callable[[],
                   _type.BOOL]
EndPaint: _Callable[[_type.HWND,
                     _Pointer[_struct.PAINTSTRUCT]],
                    _type.BOOL]
EnumChildWindows: _Callable[[_Optional[_type.HWND],
                             _type.WNDENUMPROC,
                             _type.LPARAM],
                            _type.BOOL]
EnumDisplayDevicesA: _Callable[[_Optional[_type.LPCSTR],
                                _type.DWORD,
                                _Pointer[_struct.DISPLAY_DEVICEA],
                                _type.DWORD],
                               _type.BOOL]
EnumDisplayDevicesW: _Callable[[_Optional[_type.LPCWSTR],
                                _type.DWORD,
                                _Pointer[_struct.DISPLAY_DEVICEW],
                                _type.DWORD],
                               _type.BOOL]
EnumDisplayMonitors: _Callable[[_Optional[_type.HDC],
                                _Optional[_Pointer[_struct.RECT]],
                                _type.MONITORENUMPROC,
                                _type.LPARAM],
                               _type.BOOL]
EqualRect: _Callable[[_Pointer[_struct.RECT],
                      _Pointer[_struct.RECT]],
                     _type.BOOL]
ExitWindowsEx: _Callable[[_type.UINT,
                          _type.DWORD],
                         _type.BOOL]
FillRect: _Callable[[_type.HDC,
                     _Pointer[_struct.RECT],
                     _type.HBRUSH],
                    _type.c_int]
FindWindowA: _Callable[[_type.LPCSTR,
                        _Optional[_type.LPCSTR]],
                       _type.HWND]
FindWindowW: _Callable[[_type.LPCWSTR,
                        _Optional[_type.LPCWSTR]],
                       _type.HWND]
FindWindowExA: _Callable[[_Optional[_type.HWND],
                          _Optional[_type.HWND],
                          _type.LPCSTR,
                          _Optional[_type.LPCSTR]],
                         _type.HWND]
FindWindowExW: _Callable[[_Optional[_type.HWND],
                          _Optional[_type.HWND],
                          _type.LPCWSTR,
                          _Optional[_type.LPCWSTR]],
                         _type.HWND]
FlashWindow: _Callable[[_type.HWND,
                        _type.BOOL],
                       _type.BOOL]
GetActiveWindow: _Callable[[],
                           _type.HWND]
GetAncestor: _Callable[[_type.HWND,
                        _type.UINT],
                       _type.HWND]
GetAsyncKeyState: _Callable[[_type.c_int],
                            _type.SHORT]
GetAutoRotationState: _Callable[[_Pointer[_enum.AR_STATE]],
                                _type.BOOL]
GetCIMSSM: _Callable[[_Pointer[_struct.INPUT_MESSAGE_SOURCE]],
                     _type.BOOL]
GetClassInfoA: _Callable[[_Optional[_type.HINSTANCE],
                          _type.LPCSTR,
                          _Pointer[_struct.WNDCLASSA]],
                         _type.BOOL]
GetClassInfoW: _Callable[[_Optional[_type.HINSTANCE],
                          _type.LPCWSTR,
                          _Pointer[_struct.WNDCLASSW]],
                         _type.BOOL]
GetClassInfoExA: _Callable[[_Optional[_type.HINSTANCE],
                            _type.LPCSTR,
                            _Pointer[_struct.WNDCLASSEXA]],
                           _type.BOOL]
GetClassInfoExW: _Callable[[_Optional[_type.HINSTANCE],
                            _type.LPCWSTR,
                            _Pointer[_struct.WNDCLASSEXW]],
                           _type.BOOL]
GetClientRect: _Callable[[_type.HWND,
                          _Pointer[_struct.RECT]],
                         _type.BOOL]
GetClipboardData: _Callable[[_type.UINT],
                            _type.HANDLE]
GetCurrentInputMessageSource: _Callable[[_Pointer[_struct.INPUT_MESSAGE_SOURCE]],
                                        _type.BOOL]
GetCursorPos: _Callable[[_Pointer[_struct.POINT]],
                        _type.BOOL]
GetDisplayConfigBufferSizes: _Callable[[_type.UINT32,
                                        _Pointer[_type.UINT32],
                                        _Pointer[_type.UINT32]],
                                       _type.LONG]
GetDesktopWindow: _Callable[[],
                            _type.HWND]
GetDC: _Callable[[_Optional[_type.HWND]],
                 _type.HDC]
GetDCEx: _Callable[[_Optional[_type.HWND],
                    _type.HRGN,
                    _type.DWORD],
                   _type.HDC]
GetDialogBaseUnits: _Callable[[],
                              _type.c_long]
GetDisplayAutoRotationPreferences: _Callable[[_Pointer[_enum.ORIENTATION_PREFERENCE]],
                                             _type.BOOL]
GetDisplayAutoRotationPreferencesByProcessId: _Callable[[_type.DWORD,
                                                         _Pointer[_enum.ORIENTATION_PREFERENCE],
                                                         _Pointer[_type.BOOL]],
                                                        _type.BOOL]
GetDlgCtrlID: _Callable[[_type.HWND],
                        _type.c_int]
GetDlgItem: _Callable[[_Optional[_type.HWND],
                       _type.c_int],
                      _type.HWND]
GetDlgItemInt: _Callable[[_type.HWND,
                          _type.c_int,
                          _Optional[_Pointer[_type.BOOL]],
                          _type.BOOL],
                         _type.UINT]
GetDlgItemTextA: _Callable[[_type.HWND,
                            _type.c_int,
                            _type.LPSTR,
                            _type.c_int],
                           _type.UINT]
GetDlgItemTextW: _Callable[[_type.HWND,
                            _type.c_int,
                            _type.LPWSTR,
                            _type.c_int],
                           _type.UINT]
GetDoubleClickTime: _Callable[[],
                              _type.UINT]
GetDpiForSystem: _Callable[[],
                           _type.UINT]
GetDpiForWindow: _Callable[[_type.HWND],
                           _type.UINT]
GetFocus: _Callable[[],
                    _type.HWND]
GetForegroundWindow: _Callable[[],
                               _type.HWND]
GetGUIThreadInfo: _Callable[[_type.DWORD,
                             _Pointer[_struct.GUITHREADINFO]],
                            _type.BOOL]
GetKBCodePage: _Callable[[],
                         _type.UINT]
GetKeyboardState: _Callable[[_type.PBYTE],
                            _type.BOOL]
GetKeyState: _Callable[[_type.c_int],
                       _type.SHORT]
GetMenu: _Callable[[_type.HWND],
                   _type.HMENU]
GetMenuCheckMarkDimensions: _Callable[[],
                                      _type.LONG]
GetMenuDefaultItem: _Callable[[_type.HMENU,
                               _type.UINT,
                               _type.UINT],
                              _type.UINT]
GetMenuInfo: _Callable[[_type.HMENU,
                        _Pointer[_struct.MENUINFO]],
                       _type.BOOL]
GetMenuItemCount: _Callable[[_Optional[_type.HMENU]],
                            _type.c_int]
GetMenuItemID: _Callable[[_type.HMENU,
                          _type.c_int],
                         _type.UINT]
GetMenuItemInfoA: _Callable[[_type.HMENU,
                             _type.UINT,
                             _type.BOOL,
                             _Pointer[_struct.MENUITEMINFOA]],
                            _type.BOOL]
GetMenuItemInfoW: _Callable[[_type.HMENU,
                             _type.UINT,
                             _type.BOOL,
                             _Pointer[_struct.MENUITEMINFOW]],
                            _type.BOOL]
GetMenuItemRect: _Callable[[_Optional[_type.HWND],
                            _type.HMENU,
                            _type.UINT,
                            _Pointer[_struct.RECT]],
                           _type.BOOL]
GetMenuState: _Callable[[_type.HMENU,
                         _type.UINT,
                         _type.UINT],
                        _type.UINT]
GetMenuStringA: _Callable[[_type.HMENU,
                           _type.UINT,
                           _Optional[_type.LPSTR],
                           _type.c_int,
                           _type.UINT],
                          _type.c_int]
GetMenuStringW: _Callable[[_type.HMENU,
                           _type.UINT,
                           _Optional[_type.LPWSTR],
                           _type.c_int,
                           _type.UINT],
                          _type.c_int]
GetMessageA: _Callable[[_Pointer[_struct.MSG],
                        _Optional[_type.HWND],
                        _type.UINT,
                        _type.UINT],
                       _type.BOOL]
GetMessageW: _Callable[[_Pointer[_struct.MSG],
                        _Optional[_type.HWND],
                        _type.UINT,
                        _type.UINT],
                       _type.BOOL]
GetMessageExtraInfo: _Callable[[],
                               _type.LPARAM]
GetMessagePos: _Callable[[],
                         _type.DWORD]
GetMessageTime: _Callable[[],
                          _type.LONG]
GetMonitorInfoA: _Callable[[_type.HMONITOR,
                            _Pointer[_struct.MONITORINFO]],
                           _type.BOOL]
GetMonitorInfoW: _Callable[[_type.HMONITOR,
                            _Pointer[_struct.MONITORINFO]],
                           _type.BOOL]
GetNextDlgGroupItem: _Callable[[_type.HWND,
                                _Optional[_type.HWND],
                                _type.BOOL],
                               _type.HWND]
GetNextDlgTabItem: _Callable[[_type.HWND,
                              _Optional[_type.HWND],
                              _type.BOOL],
                             _type.HWND]
GetParent: _Callable[[_type.HWND],
                     _type.HWND]
GetProcessDefaultLayout: _Callable[[_Pointer[_type.DWORD]],
                                   _type.BOOL]
GetSubMenu: _Callable[[_type.HMENU,
                       _type.c_int],
                      _type.HMENU]
GetSysColor: _Callable[[_type.c_int],
                       _type.DWORD]
GetSysColorBrush: _Callable[[_type.c_int],
                            _type.HBRUSH]
GetSystemDpiForProcess: _Callable[[_type.HANDLE],
                                  _type.UINT]
GetSystemMenu: _Callable[[_type.HWND,
                          _type.BOOL],
                         _type.HMENU]
GetSystemMetrics: _Callable[[_type.c_int],
                            _type.c_int]
GetUnpredictedMessagePos: _Callable[[],
                                    _type.DWORD]
GetWindowDC: _Callable[[_Optional[_type.HWND]],
                       _type.HDC]
GetWindowDisplayAffinity: _Callable[[_type.HWND,
                                     _Pointer[_type.DWORD]],
                                    _type.BOOL]
GetWindowPlacement: _Callable[[_type.HWND,
                               _Pointer[_struct.WINDOWPLACEMENT]],
                              _type.BOOL]
GetWindowRect: _Callable[[_type.HWND,
                          _Pointer[_struct.RECT]],
                         _type.BOOL]
HiliteMenuItem: _Callable[[_type.HWND,
                           _type.HMENU,
                           _type.UINT,
                           _type.UINT],
                          _type.BOOL]
InheritWindowMonitor: _Callable[[_type.HWND,
                                 _Optional[_type.HWND]],
                                _type.BOOL]
InsertMenuA: _Callable[[_type.HMENU,
                        _type.UINT,
                        _type.UINT,
                        _type.UINT_PTR,
                        _Optional[_type.LPCSTR]],
                       _type.BOOL]
InsertMenuW: _Callable[[_type.HMENU,
                        _type.UINT,
                        _type.UINT,
                        _type.UINT_PTR,
                        _Optional[_type.LPCWSTR]],
                       _type.BOOL]
InsertMenuItemA: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.BOOL,
                            _Pointer[_struct.MENUITEMINFOA]],
                           _type.BOOL]
InsertMenuItemW: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.BOOL,
                            _Pointer[_struct.MENUITEMINFOW]],
                           _type.BOOL]
IntersectRect: _Callable[[_Pointer[_struct.RECT],
                          _Pointer[_struct.RECT],
                          _Pointer[_struct.RECT]],
                         _type.BOOL]
InvalidateRect: _Callable[[_type.HWND,
                           _Optional[_Pointer[_struct.RECT]],
                           _type.BOOL],
                          _type.BOOL]
InvalidateRgn: _Callable[[_type.HWND,
                          _Optional[_type.HRGN],
                          _type.BOOL],
                         _type.BOOL]
IsChild: _Callable[[_type.HWND,
                    _type.HWND],
                   _type.BOOL]
IsDlgButtonChecked: _Callable[[_type.HWND,
                               _type.c_int],
                              _type.UINT]
IsIconic: _Callable[[_type.HWND],
                    _type.BOOL]
IsImmersiveProcess: _Callable[[_type.HANDLE],
                              _type.BOOL]
IsMenu: _Callable[[_type.HMENU],
                  _type.BOOL]
IsProcessDPIAware: _Callable[[],
                             _type.BOOL]
IsRectEmpty: _Callable[[_Pointer[_struct.RECT]],
                       _type.BOOL]
IsWindow: _Callable[[_type.HWND],
                    _type.BOOL]
IsWindowVisible: _Callable[[_type.HWND],
                           _type.BOOL]
IsWow64Message: _Callable[[],
                          _type.BOOL]
IsZoomed: _Callable[[_type.HWND],
                    _type.BOOL]
QueryDisplayConfig: _Callable[[_type.UINT32,
                               _Pointer[_type.UINT32],
                               _Pointer[_struct.DISPLAYCONFIG_PATH_INFO],
                               _Pointer[_type.UINT32],
                               _Pointer[_struct.DISPLAYCONFIG_MODE_INFO],
                               _Optional[_Pointer[_enum.DISPLAYCONFIG_TOPOLOGY_ID]]],
                              _type.LONG]
KillTimer: _Callable[[_type.HWND,
                      _type.UINT_PTR],
                     _type.BOOL]
LoadImageA: _Callable[[_Optional[_type.HINSTANCE],
                       _type.LPCSTR,
                       _type.UINT,
                       _type.c_int,
                       _type.c_int,
                       _type.UINT],
                      _type.HANDLE]
LoadImageW: _Callable[[_Optional[_type.HINSTANCE],
                       _type.LPCWSTR,
                       _type.UINT,
                       _type.c_int,
                       _type.c_int,
                       _type.UINT],
                      _type.HANDLE]
LoadMenuA: _Callable[[_Optional[_type.HINSTANCE],
                      _type.LPCSTR],
                     _type.HMENU]
LoadMenuW: _Callable[[_Optional[_type.HINSTANCE],
                      _type.LPCWSTR],
                     _type.HMENU]
LoadMenuIndirectA: _Callable[[_type.MENUTEMPLATEA],
                             _type.HMENU]
LoadMenuIndirectW: _Callable[[_type.MENUTEMPLATEW],
                             _type.HMENU]
LoadStringA: _Callable[[_Optional[_type.HINSTANCE],
                        _type.UINT,
                        _type.LPSTR,
                        _type.c_int],
                       _type.c_int]
LoadStringW: _Callable[[_Optional[_type.HINSTANCE],
                        _type.UINT,
                        _type.LPWSTR,
                        _type.c_int],
                       _type.c_int]
LockSetForegroundWindow: _Callable[[_type.UINT],
                                   _type.BOOL]
LockWorkStation: _Callable[[],
                           _type.BOOL]
MapWindowPoints: _Callable[[_Optional[_type.HWND],
                            _Optional[_type.HWND],
                            _Pointer[_struct.POINT],
                            _type.UINT],
                           _type.c_int]
MenuItemFromPoint: _Callable[[_Optional[_type.HWND],
                              _type.HMENU,
                              _struct.POINT],
                             _type.c_int]
ModifyMenuA: _Callable[[_type.HMENU,
                        _type.UINT,
                        _type.UINT,
                        _type.UINT_PTR,
                        _Optional[_type.LPCSTR]],
                       _type.BOOL]
ModifyMenuW: _Callable[[_type.HMENU,
                        _type.UINT,
                        _type.UINT,
                        _type.UINT_PTR,
                        _Optional[_type.LPCWSTR]],
                       _type.BOOL]
MoveWindow: _Callable[[_type.HWND,
                       _type.c_int,
                       _type.c_int,
                       _type.c_int,
                       _type.c_int,
                       _type.BOOL],
                      _type.BOOL]
NotifyWinEvent: _Callable[[_type.DWORD,
                           _type.HWND,
                           _type.LONG,
                           _type.LONG],
                          _type.VOID]
OffsetRect: _Callable[[_Pointer[_struct.RECT],
                       _Pointer[_struct.RECT],
                       _Pointer[_struct.RECT]],
                      _type.BOOL]
OpenClipboard: _Callable[[_Optional[_type.HWND]],
                         _type.BOOL]
OpenIcon: _Callable[[_type.HWND],
                    _type.BOOL]
PaintDesktop: _Callable[[_type.HDC],
                        _type.BOOL]
PostMessageA: _Callable[[_Optional[_type.HWND],
                         _type.UINT,
                         _type.WPARAM,
                         _type.LPARAM],
                        _type.BOOL]
PostMessageW: _Callable[[_Optional[_type.HWND],
                         _type.UINT,
                         _type.WPARAM,
                         _type.LPARAM],
                        _type.BOOL]
PostQuitMessage: _Callable[[_type.c_int],
                           _type.VOID]
PostThreadMessageA: _Callable[[_type.DWORD,
                               _type.UINT,
                               _type.WPARAM,
                               _type.LPARAM],
                              _type.BOOL]
PostThreadMessageW: _Callable[[_type.DWORD,
                               _type.UINT,
                               _type.WPARAM,
                               _type.LPARAM],
                              _type.BOOL]
PrintWindow: _Callable[[_type.HWND,
                        _type.HDC,
                        _type.UINT],
                       _type.BOOL]
PtInRect: _Callable[[_Pointer[_struct.RECT],
                     _struct.POINT],
                    _type.BOOL]
RealChildWindowFromPoint: _Callable[[_type.HWND,
                                     _struct.POINT],
                                    _type.HWND]
RealGetWindowClassA: _Callable[[_type.HWND,
                                _type.LPSTR,
                                _type.UINT],
                               _type.UINT]
RealGetWindowClassW: _Callable[[_type.HWND,
                                _type.LPWSTR,
                                _type.UINT],
                               _type.UINT]
RegisterClassA: _Callable[[_Pointer[_struct.WNDCLASSA]],
                          _type.ATOM]
RegisterClassW: _Callable[[_Pointer[_struct.WNDCLASSW]],
                          _type.ATOM]
RegisterClassExA: _Callable[[_Pointer[_struct.WNDCLASSEXA]],
                            _type.ATOM]
RegisterClassExW: _Callable[[_Pointer[_struct.WNDCLASSEXW]],
                            _type.ATOM]
RegisterWindowMessageA: _Callable[[_type.LPCSTR],
                                  _type.UINT]
RegisterWindowMessageW: _Callable[[_type.LPCWSTR],
                                  _type.UINT]
RemoveMenu: _Callable[[_type.HMENU,
                       _type.UINT,
                       _type.UINT],
                      _type.BOOL]
ReleaseDC: _Callable[[_Optional[_type.HWND],
                      _type.HDC],
                     _type.c_int]
ReplyMessage: _Callable[[_type.LRESULT],
                        _type.BOOL]
SendDlgItemMessageA: _Callable[[_type.HWND,
                                _type.c_int,
                                _type.UINT,
                                _type.WPARAM,
                                _type.LPARAM],
                               _type.LRESULT]
SendDlgItemMessageW: _Callable[[_type.HWND,
                                _type.c_int,
                                _type.UINT,
                                _type.WPARAM,
                                _type.LPARAM],
                               _type.LRESULT]
SendInput: _Callable[[_type.UINT,
                      _Pointer[_struct.INPUT],
                      _type.c_int],
                     _type.UINT]
SendMessageA: _Callable[[_type.HWND,
                         _type.UINT,
                         _type.WPARAM,
                         _type.LPARAM],
                        _type.LRESULT]
SendMessageW: _Callable[[_type.HWND,
                         _type.UINT,
                         _type.WPARAM,
                         _type.LPARAM],
                        _type.LRESULT]
SendMessageCallbackA: _Callable[[_type.HWND,
                                 _type.UINT,
                                 _type.WPARAM,
                                 _type.LPARAM,
                                 _type.SENDASYNCPROC,
                                 _type.ULONG_PTR],
                                _type.BOOL]
SendMessageCallbackW: _Callable[[_type.HWND,
                                 _type.UINT,
                                 _type.WPARAM,
                                 _type.LPARAM,
                                 _type.SENDASYNCPROC,
                                 _type.ULONG_PTR],
                                _type.BOOL]
SendMessageTimeoutA: _Callable[[_type.HWND,
                                _type.UINT,
                                _type.WPARAM,
                                _type.LPARAM,
                                _type.UINT,
                                _type.UINT,
                                _Optional[_Pointer[_type.DWORD_PTR]]],
                               _type.LRESULT]
SendMessageTimeoutW: _Callable[[_type.HWND,
                                _type.UINT,
                                _type.WPARAM,
                                _type.LPARAM,
                                _type.UINT,
                                _type.UINT,
                                _Optional[_Pointer[_type.DWORD_PTR]]],
                               _type.LRESULT]
SendNotifyMessageA: _Callable[[_type.HWND,
                               _type.UINT,
                               _type.WPARAM,
                               _type.LPARAM],
                              _type.BOOL]
SendNotifyMessageW: _Callable[[_type.HWND,
                               _type.UINT,
                               _type.WPARAM,
                               _type.LPARAM],
                              _type.BOOL]
SetActiveWindow: _Callable[[_type.HWND],
                           _type.BOOL]
FrameRect: _Callable[[_type.HDC,
                      _Pointer[_struct.RECT],
                      _type.HBRUSH],
                     _type.BOOL]
GetCapture: _Callable[[],
                      _type.HWND]
SetCapture: _Callable[[_type.HWND],
                      _type.HWND]
ReleaseCapture: _Callable[[],
                          _type.BOOL]
SetClipboardData: _Callable[[_type.UINT,
                             _type.HANDLE],
                            _type.HANDLE]
SetCursor: _Callable[[_Optional[_type.HCURSOR]],
                     _type.HCURSOR]
SetDisplayAutoRotationPreferences: _Callable[[_enum.ORIENTATION_PREFERENCE],
                                             _type.BOOL]
SetDisplayConfig: _Callable[[_type.UINT32,
                             _Pointer[_struct.DISPLAYCONFIG_PATH_INFO],
                             _type.UINT32,
                             _Pointer[_struct.DISPLAYCONFIG_MODE_INFO],
                             _type.UINT32],
                            _type.LONG]
SetDlgItemInt: _Callable[[_type.HWND,
                          _type.c_int,
                          _type.UINT,
                          _type.BOOL],
                         _type.BOOL]
SetDlgItemTextA: _Callable[[_type.HWND,
                            _type.c_int,
                            _type.LPCSTR],
                           _type.BOOL]
SetDlgItemTextW: _Callable[[_type.HWND,
                            _type.c_int,
                            _type.LPCWSTR],
                           _type.BOOL]
SetDoubleClickTime: _Callable[[_type.UINT],
                              _type.BOOL]
SetFocus: _Callable[[_type.HWND],
                    _type.HWND]
SetForegroundWindow: _Callable[[_type.HWND],
                               _type.BOOL]
SetKeyboardState: _Callable[[_type.PBYTE],
                            _type.BOOL]
SetMenu: _Callable[[_type.HWND,
                    _Optional[_type.HMENU]],
                   _type.BOOL]
SetMenuDefaultItem: _Callable[[_type.HMENU,
                               _type.UINT,
                               _type.UINT],
                              _type.BOOL]
SetMenuInfo: _Callable[[_type.HMENU,
                        _Pointer[_struct.MENUINFO]],
                       _type.BOOL]
SetMenuItemBitmaps: _Callable[[_type.HMENU,
                               _type.UINT,
                               _type.UINT,
                               _Optional[_type.HBITMAP],
                               _Optional[_type.HBITMAP]],
                              _type.BOOL]
SetMenuItemInfoA: _Callable[[_type.HMENU,
                             _type.UINT,
                             _type.BOOL,
                             _Pointer[_struct.MENUITEMINFOA]],
                            _type.BOOL]
SetMenuItemInfoW: _Callable[[_type.HMENU,
                             _type.UINT,
                             _type.BOOL,
                             _Pointer[_struct.MENUITEMINFOW]],
                            _type.BOOL]
SetMessageExtraInfo: _Callable[[_type.LPARAM],
                               _type.LPARAM]
SetParent: _Callable[[_type.HWND,
                      _Optional[_type.HWND]],
                     _type.HWND]
SetProcessDefaultLayout: _Callable[[_type.DWORD],
                                   _type.BOOL]
SetProcessDPIAware: _Callable[[],
                              _type.BOOL]
SetProcessRestrictionExemption: _Callable[[_type.BOOL],
                                          _type.BOOL]
SetSysColors: _Callable[[_type.c_int,
                         _Pointer[_type.INT],
                         _Pointer[_type.COLORREF]],
                        _type.BOOL]
SetTimer: _Callable[[_Optional[_type.HWND],
                     _type.UINT_PTR,
                     _type.UINT,
                     _Optional[_type.TIMERPROC]],
                    _type.UINT_PTR]
SetWinEventHook: _Callable[[_type.DWORD,
                            _type.DWORD,
                            _Optional[_type.HMODULE],
                            _type.WINEVENTPROC,
                            _type.DWORD,
                            _type.DWORD,
                            _type.DWORD],
                           _type.HWINEVENTHOOK]
SetWindowDisplayAffinity: _Callable[[_type.HWND,
                                     _type.DWORD],
                                    _type.BOOL]
SetWindowPlacement: _Callable[[_type.HWND,
                               _Pointer[_struct.WINDOWPLACEMENT]],
                              _type.BOOL]
SetWindowPos: _Callable[[_type.HWND,
                         _Optional[_type.HWND],
                         _type.c_int,
                         _type.c_int,
                         _type.c_int,
                         _type.c_int,
                         _type.UINT],
                        _type.BOOL]
SetWindowTextA: _Callable[[_type.HWND,
                           _type.LPCSTR],
                          _type.BOOL]
SetWindowTextW: _Callable[[_type.HWND,
                           _type.LPCWSTR],
                          _type.BOOL]
ShowCursor: _Callable[[_type.BOOL],
                      _type.c_int]
ShowOwnedPopups: _Callable[[_type.HWND,
                            _type.BOOL],
                           _type.BOOL]
ShowWindow: _Callable[[_type.HWND,
                       _type.c_int],
                      _type.BOOL]
ShowWindowAsync: _Callable[[_type.HWND,
                            _type.c_int],
                           _type.BOOL]
ShutdownBlockReasonCreate: _Callable[[_type.HWND,
                                      _type.LPCWSTR],
                                     _type.BOOL]
ShutdownBlockReasonDestroy: _Callable[[_type.HWND],
                                      _type.BOOL]
ShutdownBlockReasonQuery: _Callable[[_type.HWND,
                                     _Optional[_type.LPWSTR],
                                     _Pointer[_type.DWORD]],
                                    _type.BOOL]
SubtractRect: _Callable[[_Pointer[_struct.RECT],
                         _Pointer[_struct.RECT],
                         _Pointer[_struct.RECT]],
                        _type.BOOL]
SwapMouseButton: _Callable[[_type.BOOL],
                           _type.BOOL]
SwitchToThisWindow: _Callable[[_type.HWND,
                               _type.BOOL],
                              _type.VOID]
SystemParametersInfoA: _Callable[[_type.UINT,
                                  _type.UINT,
                                  _type.PVOID,
                                  _type.UINT],
                                 _type.BOOL]
SystemParametersInfoW: _Callable[[_type.UINT,
                                  _type.UINT,
                                  _type.PVOID,
                                  _type.UINT],
                                 _type.BOOL]
TrackMouseEvent: _Callable[[_Pointer[_struct.TRACKMOUSEEVENT]],
                           _type.BOOL]
TrackPopupMenu: _Callable[[_type.HMENU,
                           _type.UINT,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.HWND,
                           _Optional[_Pointer[_struct.RECT]]],
                          _type.BOOL]
TrackPopupMenuEx: _Callable[[_type.HMENU,
                             _type.UINT,
                             _type.c_int,
                             _type.c_int,
                             _type.HWND,
                             _Optional[_Pointer[_struct.TPMPARAMS]]],
                            _type.BOOL]
TranslateMessage: _Callable[[_Pointer[_struct.MSG]],
                            _type.BOOL]
UnhookWinEvent: _Callable[[_type.HWINEVENTHOOK],
                          _type.BOOL]
UnionRect: _Callable[[_Pointer[_struct.RECT],
                      _Pointer[_struct.RECT],
                      _Pointer[_struct.RECT]],
                     _type.BOOL]
UnregisterClassA: _Callable[[_type.LPCSTR,
                             _type.HINSTANCE],
                            _type.BOOL]
UnregisterClassW: _Callable[[_type.LPCWSTR,
                             _type.HINSTANCE],
                            _type.BOOL]
UpdateWindow: _Callable[[_type.HWND],
                        _type.BOOL]
WaitForInputIdle: _Callable[[_type.HANDLE,
                             _type.DWORD],
                            _type.DWORD]
WaitMessage: _Callable[[],
                       _type.BOOL]
WindowFromDC: _Callable[[_type.HDC],
                        _type.HWND]

_WinLib(__name__)
