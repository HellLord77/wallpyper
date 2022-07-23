from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing
from typing import Callable as _Callable, Optional as _Optional

from . import const as _const, enum as _enum, interface as _interface, struct as _struct, type as _type, union as _union
from ._utils import _Pointer, _format_annotations, _func_doc, _resolve_type


class _CDLL(type):
    pass


def _init(self, name: str):
    if name in self.__annotations__:
        if self._funcs is None:
            self._annots = _typing.get_type_hints(self)
            self._funcs = {}
            for name_ in self.__annotations__:
                try:
                    self._funcs[name_] = vars(self)[name_]
                except KeyError:
                    self._funcs[name_] = name_
                else:
                    delattr(self, name_)
        func = None
        while func is None:
            try:
                func = self._lib[self._funcs[name]]
            except KeyError:
                raise AttributeError(f"Lib '{self.__qualname__}' has no function '{name}'")
            except TypeError:
                if self is Python:
                    self._lib = _ctypes.pythonapi
                else:
                    name_ = self.__qualname__
                    mode = _ctypes.DEFAULT_MODE
                    if isinstance(self, _WinDLL):
                        name_ = f'{name_}.dll'
                        mode = _const.LOAD_LIBRARY_SEARCH_DEFAULT_DIRS
                    self._lib = getattr(_ctypes, type(self).__name__[1:])(name_, mode)
        annot = _format_annotations(self.__annotations__[name])
        func.restype, *func.argtypes = _resolve_type(self._annots[name])
        if self._errcheck is not None:
            func.errcheck = self._errcheck
        func.__name__ = name
        func.__doc__ = _func_doc(name, func.restype, func.argtypes, annot)
        setattr(self, name, func)
        return func
    return super(type(self), self).__getattribute__(name)


_CDLL.__getattr__ = _init


class _OleDLL(_CDLL):
    pass


class _PyDLL(_CDLL):
    pass


class _WinDLL(_CDLL):
    pass


class _Func:
    _lib = None
    _errcheck = None
    _funcs = None


class Python(_Func, metaclass=_PyDLL):
    # pylifecycle
    Py_Initialize: _Callable[[],
                             _type.c_void]
    Py_InitializeEx: _Callable[[_type.c_int],
                               _type.c_void]
    Py_IsInitialized: _Callable[[],
                                _type.c_int]
    Py_Finalize: _Callable[[],
                           _type.c_void]
    Py_FinalizeEx: _Callable[[],
                             _type.c_int]
    # pythread
    PyThread_create_key: _Callable[[],
                                   _type.c_int]
    PyThread_delete_key: _Callable[[_type.c_int],
                                   _type.c_void]
    PyThread_delete_key_value: _Callable[[_type.c_int],
                                         _type.c_void]
    PyThread_exit_thread: _Callable[[],
                                    _type.c_void]
    PyThread_get_key_value: _Callable[[_type.c_int],
                                      _type.c_void_p]
    PyThread_get_stacksize: _Callable[[],
                                      _type.c_size_t]
    PyThread_get_thread_ident: _Callable[[],
                                         _type.c_ulong]
    PyThread_get_thread_native_id: _Callable[[],
                                             _type.c_ulong]
    PyThread_init_thread: _Callable[[],
                                    _type.c_void]
    PyThread_set_key_value: _Callable[[_type.c_int,
                                       _type.c_void_p],
                                      _type.c_int]
    PyThread_set_stacksize: _Callable[[_type.c_size_t],
                                      _type.c_int]
    PyThread_ReInitTLS: _Callable[[],
                                  _type.c_void]


class Advapi32(_Func, metaclass=_WinDLL):
    # winreg
    AbortSystemShutdownA: _Callable[[_type.LPSTR],
                                    _type.BOOL]
    AbortSystemShutdownW: _Callable[[_type.LPWSTR],
                                    _type.BOOL]
    CheckForHiberboot: _Callable[[_Pointer[_type.BOOLEAN],
                                  _type.BOOLEAN],
                                 _type.DWORD]
    InitiateShutdownA: _Callable[[_Optional[_type.LPSTR],
                                  _Optional[_type.LPSTR],
                                  _type.DWORD,
                                  _type.DWORD,
                                  _type.DWORD],
                                 _type.DWORD]
    InitiateShutdownW: _Callable[[_Optional[_type.LPWSTR],
                                  _Optional[_type.LPWSTR],
                                  _type.DWORD,
                                  _type.DWORD,
                                  _type.DWORD],
                                 _type.DWORD]
    InitiateSystemShutdownA: _Callable[[_Optional[_type.LPSTR],
                                        _Optional[_type.LPSTR],
                                        _type.DWORD,
                                        _type.BOOL,
                                        _type.BOOL],
                                       _type.BOOL]
    InitiateSystemShutdownW: _Callable[[_Optional[_type.LPWSTR],
                                        _Optional[_type.LPWSTR],
                                        _type.DWORD,
                                        _type.BOOL,
                                        _type.BOOL],
                                       _type.BOOL]
    InitiateSystemShutdownExA: _Callable[[_Optional[_type.LPSTR],
                                          _Optional[_type.LPSTR],
                                          _type.DWORD,
                                          _type.BOOL,
                                          _type.BOOL,
                                          _type.DWORD],
                                         _type.BOOL]
    InitiateSystemShutdownExW: _Callable[[_Optional[_type.LPWSTR],
                                          _Optional[_type.LPWSTR],
                                          _type.DWORD,
                                          _type.BOOL,
                                          _type.BOOL,
                                          _type.DWORD],
                                         _type.BOOL]
    RegCopyTreeA: _Callable[[_type.HKEY,
                             _Optional[_type.LPCSTR],
                             _type.HKEY],
                            _type.LSTATUS]
    RegCopyTreeW: _Callable[[_type.HKEY,
                             _Optional[_type.LPCWSTR],
                             _type.HKEY],
                            _type.LSTATUS]
    RegDeleteKeyValueA: _Callable[[_type.HKEY,
                                   _Optional[_type.LPCSTR],
                                   _Optional[_type.LPCSTR]],
                                  _type.LSTATUS]
    RegDeleteKeyValueW: _Callable[[_type.HKEY,
                                   _Optional[_type.LPCWSTR],
                                   _Optional[_type.LPCWSTR]],
                                  _type.LSTATUS]
    RegDeleteTreeA: _Callable[[_type.HKEY,
                               _Optional[_type.LPCSTR]],
                              _type.LSTATUS]
    RegDeleteTreeW: _Callable[[_type.HKEY,
                               _Optional[_type.LPCWSTR]],
                              _type.LSTATUS]
    RegLoadAppKeyA: _Callable[[_type.LPCSTR,
                               _Pointer[_type.HKEY],
                               _type.REGSAM,
                               _type.DWORD,
                               _type.DWORD],
                              _type.LSTATUS]
    RegLoadAppKeyW: _Callable[[_type.LPCWSTR,
                               _Pointer[_type.HKEY],
                               _type.REGSAM,
                               _type.DWORD,
                               _type.DWORD],
                              _type.LSTATUS]
    RegLoadMUIStringA: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCSTR],
                                  _Optional[_type.LPSTR],
                                  _type.DWORD,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _type.DWORD,
                                  _Optional[_type.LPCSTR]],
                                 _type.LSTATUS]
    RegLoadMUIStringW: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCWSTR],
                                  _Optional[_type.LPWSTR],
                                  _type.DWORD,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _type.DWORD,
                                  _Optional[_type.LPCWSTR]],
                                 _type.LSTATUS]
    RegReplaceKeyA: _Callable[[_type.HKEY,
                               _Optional[_type.LPCSTR],
                               _type.LPCSTR,
                               _type.LPCSTR],
                              _type.LSTATUS]
    RegReplaceKeyW: _Callable[[_type.HKEY,
                               _Optional[_type.LPCWSTR],
                               _type.LPCWSTR,
                               _type.LPCWSTR],
                              _type.LSTATUS]
    RegRestoreKeyA: _Callable[[_type.HKEY,
                               _type.LPCSTR,
                               _type.DWORD],
                              _type.LSTATUS]
    RegRestoreKeyW: _Callable[[_type.HKEY,
                               _type.LPCWSTR,
                               _type.DWORD],
                              _type.LSTATUS]
    RegSaveKeyExA: _Callable[[_type.HKEY,
                              _type.LPCSTR,
                              _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                              _type.DWORD],
                             _type.LSTATUS]
    RegSaveKeyExW: _Callable[[_type.HKEY,
                              _type.LPCWSTR,
                              _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                              _type.DWORD],
                             _type.LSTATUS]
    RegUnLoadKeyA: _Callable[[_type.HKEY,
                              _Optional[_type.LPCSTR]],
                             _type.LSTATUS]
    RegUnLoadKeyW: _Callable[[_type.HKEY,
                              _Optional[_type.LPCWSTR]],
                             _type.LSTATUS]


class Cfgmgr32(_Func, metaclass=_WinDLL):
    # Cfgmgr32
    CM_Get_DevNode_PropertyW: _Callable[[_type.DEVINST,
                                         _Pointer[_struct.DEVPROPKEY],
                                         _Pointer[_type.DEVPROPTYPE],
                                         _Optional[_type.PBYTE],
                                         _Pointer[_type.ULONG],
                                         _type.ULONG],
                                        _type.CONFIGRET]
    CM_Get_Device_Interface_PropertyW: _Callable[[_type.LPCWSTR,
                                                  _Pointer[_struct.DEVPROPKEY],
                                                  _Pointer[_type.DEVPROPTYPE],
                                                  _Optional[_type.PBYTE],
                                                  _Pointer[_type.ULONG],
                                                  _type.ULONG],
                                                 _type.CONFIGRET]
    CM_Locate_DevNodeA: _Callable[[_Pointer[_type.DEVINST],
                                   _type.PBYTE,
                                   _type.ULONG],
                                  _type.CONFIGRET]
    CM_Locate_DevNodeW: _Callable[[_Pointer[_type.DEVINST],
                                   _type.PWSTR,
                                   _type.ULONG],
                                  _type.CONFIGRET]


class Combase(_Func, metaclass=_WinDLL):
    # roapi
    RoActivateInstance: _Callable[[_type.HSTRING,
                                   _Pointer[_interface.IInspectable]],
                                  _type.HRESULT]
    RoGetActivationFactory: _Callable[[_type.HSTRING,
                                       _Pointer[_struct.IID],
                                       _Pointer[_interface.IActivationFactory]],
                                      _type.HRESULT]
    RoGetApartmentIdentifier: _Callable[[_Pointer[_type.UINT64]],
                                        _type.HRESULT]
    RoInitialize: _Callable[[_enum.RO_INIT_TYPE],
                            _type.HRESULT]
    RoUninitialize: _Callable[[],
                              _type.c_void]
    # winstring
    WindowsConcatString: _Callable[[_Optional[_type.HSTRING],
                                    _Optional[_type.HSTRING],
                                    _Pointer[_type.HSTRING]],
                                   _type.HRESULT]
    WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH],
                                    _type.UINT32,
                                    _Pointer[_type.HSTRING]],
                                   _type.HRESULT]
    WindowsDeleteString: _Callable[[_type.HSTRING],
                                   _type.HRESULT]
    WindowsGetStringLen: _Callable[[_type.HSTRING],
                                   _type.UINT32]
    WindowsGetStringRawBuffer: _Callable[[_Optional[_type.HSTRING],
                                          _Optional[_Pointer[_type.UINT32]]],
                                         _type.PCWSTR]
    WindowsIsStringEmpty: _Callable[[_type.HSTRING],
                                    _type.BOOL]
    WindowsReplaceString: _Callable[[_Optional[_type.HSTRING],
                                     _Optional[_type.HSTRING],
                                     _Optional[_type.HSTRING],
                                     _Pointer[_type.HSTRING]],
                                    _type.HRESULT]
    WindowsTrimStringEnd: _Callable[[_Optional[_type.HSTRING],
                                     _Optional[_type.HSTRING],
                                     _Pointer[_type.HSTRING]],
                                    _type.HRESULT]
    WindowsTrimStringStart: _Callable[[_Optional[_type.HSTRING],
                                       _Optional[_type.HSTRING],
                                       _Pointer[_type.HSTRING]],
                                      _type.HRESULT]


class Comctl32(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    # CommCtrl
    InitCommonControls: _Callable[[],
                                  _type.c_void]
    InitCommonControlsEx: _Callable[[_Pointer[_struct.INITCOMMONCONTROLSEX]],
                                    _type.BOOL]


class Comdlg32(_Func, metaclass=_WinDLL):
    # commdlg
    ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]],
                            _type.BOOL]
    ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]],
                            _type.BOOL]


class ComputeCore(_Func, metaclass=_WinDLL):
    # computecore
    HcsGetServiceProperties: _Callable[[_Optional[_type.PCWSTR],
                                        _Pointer[_type.PWSTR]],
                                       _type.HRESULT]
    HcsModifyServiceSettings: _Callable[[_type.PCWSTR,
                                         _Optional[_Pointer[_type.PWSTR]]],
                                        _type.HRESULT]
    HcsSubmitWerReport: _Callable[[_type.PCWSTR],
                                  _type.HRESULT]
    HcsCreateEmptyGuestStateFile: _Callable[[_type.PCWSTR],
                                            _type.HRESULT]
    HcsCreateEmptyRuntimeStateFile: _Callable[[_type.PCWSTR],
                                              _type.HRESULT]
    HcsGrantVmAccess: _Callable[[_type.PCWSTR,
                                 _type.PCWSTR],
                                _type.HRESULT]
    HcsRevokeVmAccess: _Callable[[_type.PCWSTR,
                                  _type.PCWSTR],
                                 _type.HRESULT]
    HcsGrantVmGroupAccess: _Callable[[_type.PCWSTR],
                                     _type.HRESULT]
    HcsRevokeVmGroupAccess: _Callable[[_type.PCWSTR],
                                      _type.HRESULT]


class Crypt32(_Func, metaclass=_WinDLL):
    # wincrypt
    CryptBinaryToStringA: _Callable[[_Pointer[_type.BYTE],
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Optional[_Pointer[_type.LPSTR]],
                                     _Pointer[_type.DWORD]],
                                    _type.BOOL]
    CryptBinaryToStringW: _Callable[[_Pointer[_type.BYTE],
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Optional[_Pointer[_type.LPWSTR]],
                                     _Pointer[_type.DWORD]],
                                    _type.BOOL]
    CryptStringToBinaryA: _Callable[[_type.LPCSTR,
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Pointer[_type.BYTE],
                                     _Pointer[_type.DWORD],
                                     _Optional[_Pointer[_type.DWORD]],
                                     _Optional[_Pointer[_type.DWORD]]],
                                    _type.BOOL]
    CryptStringToBinaryW: _Callable[[_type.LPCWSTR,
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Pointer[_type.BYTE],
                                     _Pointer[_type.DWORD],
                                     _Optional[_Pointer[_type.DWORD]],
                                     _Optional[_Pointer[_type.DWORD]]],
                                    _type.BOOL]


class Dwmapi(_Func, metaclass=_WinDLL):
    # dwmapi
    DwmDefWindowProc: _Callable[[_type.HWND,
                                 _type.UINT,
                                 _type.WPARAM,
                                 _type.LPARAM,
                                 _Pointer[_type.LRESULT]],
                                _type.BOOL]
    DwmEnableComposition: _Callable[[_type.UINT],
                                    _type.HRESULT]
    DwmEnableMMCSS: _Callable[[_type.BOOL],
                              _type.HRESULT]
    DwmExtendFrameIntoClientArea: _Callable[[_type.HWND,
                                             _Pointer[_struct.MARGINS]],
                                            _type.HRESULT]
    DwmGetColorizationColor: _Callable[[_Pointer[_type.DWORD],
                                        _Pointer[_type.BOOL]],
                                       _type.HRESULT]
    DwmGetWindowAttribute: _Callable[[_type.HWND,
                                      _type.DWORD,
                                      _type.PVOID,
                                      _type.DWORD],
                                     _type.HRESULT]
    DwmIsCompositionEnabled: _Callable[[_Pointer[_type.BOOL]],
                                       _type.HRESULT]
    DwmModifyPreviousDxFrameDuration: _Callable[[_type.HWND,
                                                 _type.INT,
                                                 _type.BOOL],
                                                _type.HRESULT]
    DwmRegisterThumbnail: _Callable[[_type.HWND,
                                     _type.HWND,
                                     _Pointer[_type.HTHUMBNAIL]],
                                    _type.HRESULT]
    DwmSetDxFrameDuration: _Callable[[_type.HWND,
                                      _type.INT],
                                     _type.HRESULT]
    DwmSetWindowAttribute: _Callable[[_type.HWND,
                                      _type.DWORD,
                                      _type.LPCVOID,
                                      _type.DWORD],
                                     _type.HRESULT]
    DwmUnregisterThumbnail: _Callable[[_type.HTHUMBNAIL],
                                      _type.HRESULT]


class Gdi32(_Func, metaclass=_WinDLL):
    # wingdi
    AbortDoc: _Callable[[_type.HDC],
                        _type.c_int]
    AbortPath: _Callable[[_type.HDC],
                         _type.BOOL]
    ArcTo: _Callable[[_type.HDC,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int],
                     _type.BOOL]
    BeginPath: _Callable[[_type.HDC],
                         _type.BOOL]
    BitBlt: _Callable[[_type.HDC,
                       _type.c_int,
                       _type.c_int,
                       _type.c_int,
                       _type.c_int,
                       _type.HDC,
                       _type.c_int,
                       _type.c_int,
                       _type.DWORD],
                      _type.BOOL]
    CloseFigure: _Callable[[_type.HDC],
                           _type.BOOL]
    CreateBitmap: _Callable[[_type.c_int,
                             _type.c_int,
                             _type.UINT,
                             _type.UINT,
                             _Optional[_type.VOID]],
                            _type.HBITMAP]
    CreateCompatibleBitmap: _Callable[[_type.HDC,
                                       _type.c_int,
                                       _type.c_int],
                                      _type.HBITMAP]
    CreateCompatibleDC: _Callable[[_Optional[_type.HDC]],
                                  _type.HDC]
    CreateDIBitmap: _Callable[[_type.HDC,
                               _Pointer[_struct.BITMAPINFOHEADER],
                               _type.DWORD,
                               _type.VOID,
                               _Pointer[_struct.BITMAPINFO],
                               _type.UINT],
                              _type.HBITMAP]
    CreateDIBSection: _Callable[[_type.HDC,
                                 _Pointer[_struct.BITMAPINFOHEADER],
                                 _type.UINT,
                                 _Optional[_type.VOID],
                                 _Optional[_type.HANDLE],
                                 _type.DWORD],
                                _type.HBITMAP]
    CreateDiscardableBitmap: _Callable[[_type.HDC,
                                        _type.c_int,
                                        _type.c_int],
                                       _type.HBITMAP]
    CreateHalftonePalette: _Callable[[_type.HDC],
                                     _type.HPALETTE]
    CreateSolidBrush: _Callable[[_type.COLORREF],
                                _type.HBRUSH]
    DeleteDC: _Callable[[_type.HDC],
                        _type.BOOL]
    DeleteMetaFile: _Callable[[_type.HMETAFILE],
                              _type.BOOL]
    DeleteObject: _Callable[[_type.HGDIOBJ],
                            _type.BOOL]
    EndDoc: _Callable[[_type.HDC],
                      _type.c_int]
    EndPath: _Callable[[_type.HDC],
                       _type.BOOL]
    EndPage: _Callable[[_type.HDC],
                       _type.c_int]
    ExtCreatePen: _Callable[[_type.DWORD,
                             _type.DWORD,
                             _Pointer[_struct.LOGBRUSH],
                             _type.DWORD,
                             _Optional[_Pointer[_type.DWORD]]],
                            _type.HPEN]
    FillPath: _Callable[[_type.HDC],
                        _type.BOOL]
    FlattenPath: _Callable[[_type.HDC],
                           _type.BOOL]
    GetArcDirection: _Callable[[_type.HDC],
                               _type.c_int]
    GetBitmapDimensionEx: _Callable[[_type.HBITMAP,
                                     _Pointer[_struct.SIZE]],
                                    _type.BOOL]
    GetBkColor: _Callable[[_type.HDC],
                          _type.COLORREF]
    GetBkMode: _Callable[[_type.HDC],
                         _type.c_int]
    GetClipBox: _Callable[[_type.HDC,
                           _Pointer[_struct.RECT]],
                          _type.c_int]
    GetColorAdjustment: _Callable[[_type.HDC,
                                   _Pointer[_struct.COLORADJUSTMENT]],
                                  _type.BOOL]
    GetDCBrushColor: _Callable[[_type.HDC],
                               _type.COLORREF]
    GetDCPenColor: _Callable[[_type.HDC],
                             _type.COLORREF]
    GetDIBits: _Callable[[_type.HDC,
                          _type.HBITMAP,
                          _type.UINT,
                          _type.UINT,
                          _Optional[_type.LPVOID],
                          _Pointer[_struct.BITMAPINFO],
                          _type.UINT],
                         _type.c_int]
    GdiFlush: _Callable[[],
                        _type.BOOL]
    GetGraphicsMode: _Callable[[_type.HDC],
                               _type.c_int]
    GetMapMode: _Callable[[_type.HDC],
                          _type.c_int]
    GetMetaFileA: _Callable[[_type.LPCSTR],
                            _type.HMETAFILE]
    GetMetaFileW: _Callable[[_type.LPCWSTR],
                            _type.HMETAFILE]
    GetMiterLimit: _Callable[[_type.HDC,
                              _Pointer[_type.FLOAT]],
                             _type.BOOL]
    GetObjectA: _Callable[[_type.HANDLE,
                           _type.c_int,
                           _type.LPVOID],
                          _type.c_int]
    GetObjectW: _Callable[[_type.HANDLE,
                           _type.c_int,
                           _type.LPVOID],
                          _type.c_int]
    GetObjectType: _Callable[[_type.HGDIOBJ],
                             _type.DWORD]
    GetPath: _Callable[[_type.HDC,
                        _Pointer[_struct.POINT],
                        _Pointer[_type.BYTE],
                        _type.c_int],
                       _type.c_int]
    GetPixel: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int],
                        _type.COLORREF]
    GetPixelFormat: _Callable[[_type.HDC],
                              _type.c_int]
    GetPolyFillMode: _Callable[[_type.HDC],
                               _type.c_int]
    GetRandomRgn: _Callable[[_type.HDC,
                             _type.HRGN,
                             _type.INT],
                            _type.c_int]
    GetRgnBox: _Callable[[_type.HRGN,
                          _Pointer[_struct.RECT]],
                         _type.c_int]
    GetROP2: _Callable[[_type.HDC],
                       _type.c_int]
    GetStockObject: _Callable[[_type.c_int],
                              _type.HGDIOBJ]
    GetStretchBltMode: _Callable[[_type.HDC],
                                 _type.c_int]
    GdiGetBatchLimit: _Callable[[],
                                _type.DWORD]
    GdiSetBatchLimit: _Callable[[_type.DWORD],
                                _type.DWORD]
    MoveToEx: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int,
                         _Pointer[_struct.POINT]],
                        _type.BOOL]
    PathToRegion: _Callable[[_type.HDC],
                            _type.HRGN]
    PolyDraw: _Callable[[_type.HDC,
                         _Pointer[_struct.POINT],
                         _Pointer[_type.BYTE],
                         _type.c_int],
                        _type.BOOL]
    SelectClipPath: _Callable[[_type.HDC,
                               _type.c_int],
                              _type.BOOL]
    SelectObject: _Callable[[_type.HDC,
                             _type.HGDIOBJ],
                            _type.HGDIOBJ]
    SetAbortProc: _Callable[[_type.HDC,
                             _type.ABORTPROC],
                            _type.c_int]
    SetArcDirection: _Callable[[_type.HDC,
                                _type.c_int],
                               _type.c_int]
    SetBkColor: _Callable[[_type.HDC,
                           _type.COLORREF],
                          _type.COLORREF]
    SetColorAdjustment: _Callable[[_type.HDC,
                                   _Pointer[_struct.COLORADJUSTMENT]],
                                  _type.BOOL]
    SetDCBrushColor: _Callable[[_type.HDC,
                                _type.COLORREF],
                               _type.COLORREF]
    SetDCPenColor: _Callable[[_type.HDC,
                              _type.COLORREF],
                             _type.COLORREF]
    SetMiterLimit: _Callable[[_type.HDC,
                              _type.FLOAT,
                              _Optional[_Pointer[_type.FLOAT]]],
                             _type.BOOL]
    SetStretchBltMode: _Callable[[_type.HDC,
                                  _type.c_int],
                                 _type.c_int]
    StartPage: _Callable[[_type.HDC],
                         _type.c_int]
    StretchBlt: _Callable[[_type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.DWORD],
                          _type.BOOL]
    StrokeAndFillPath: _Callable[[_type.HDC],
                                 _type.BOOL]
    StrokePath: _Callable[[_type.HDC],
                          _type.BOOL]
    WidenPath: _Callable[[_type.HDC],
                         _type.BOOL]
    TextOutA: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int,
                         _type.LPCSTR,
                         _type.c_int],
                        _type.BOOL]
    TextOutW: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int,
                         _type.LPCWSTR,
                         _type.c_int],
                        _type.BOOL]
    TransparentBlt: _Callable[[_type.HDC,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.HDC,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.UINT],
                              _type.BOOL]


class GdiPlus(_Func, metaclass=_WinDLL):
    # gdiplusflat
    GdipBitmapGetPixel: _Callable[[_type.GpBitmap,
                                   _type.INT,
                                   _type.INT,
                                   _Pointer[_type.ARGB]],
                                  _enum.GpStatus]
    GdipBitmapSetPixel: _Callable[[_type.GpBitmap,
                                   _type.INT,
                                   _type.INT,
                                   _type.ARGB],
                                  _enum.GpStatus]
    GdipBitmapSetResolution: _Callable[[_type.GpBitmap,
                                        _type.REAL,
                                        _type.REAL],
                                       _enum.GpStatus]
    GdipClonePen: _Callable[[_type.GpPen,
                             _Pointer[_type.GpPen]],
                            _enum.GpStatus]
    GdipCreateBitmapFromFile: _Callable[[_type.LPWSTR,
                                         _Pointer[_type.GpBitmap]],
                                        _enum.GpStatus]
    GdipCreateBitmapFromFileICM: _Callable[[_type.LPWSTR,
                                            _Pointer[_type.GpBitmap]],
                                           _enum.GpStatus]
    GdipCreateBitmapFromGdiDib: _Callable[[_Pointer[_struct.BITMAPINFO],
                                           _type.VOID,
                                           _Pointer[_type.GpBitmap]],
                                          _enum.GpStatus]
    GdipCreateBitmapFromGraphics: _Callable[[_type.INT,
                                             _type.INT,
                                             _type.GpGraphics,
                                             _Pointer[_type.GpBitmap]],
                                            _enum.GpStatus]
    GdipCreateBitmapFromHBITMAP: _Callable[[_type.HBITMAP,
                                            _type.HPALETTE,
                                            _Pointer[_type.GpBitmap]],
                                           _enum.GpStatus]
    GdipCreateBitmapFromHICON: _Callable[[_type.HICON,
                                          _Pointer[_type.GpBitmap]],
                                         _enum.GpStatus]
    GdipCreateBitmapFromResource: _Callable[[_type.HINSTANCE,
                                             _type.LPWSTR,
                                             _Pointer[_type.GpBitmap]],
                                            _enum.GpStatus]
    GdipCreateBitmapFromScan0: _Callable[[_type.INT,
                                          _type.INT,
                                          _type.INT,
                                          _type.PixelFormat,
                                          _Optional[_Pointer[_type.BYTE]],
                                          _Pointer[_type.GpBitmap]],
                                         _enum.GpStatus]
    GdipCreateBitmapFromStream: _Callable[[_interface.IStream,
                                           _Pointer[_type.GpBitmap]],
                                          _enum.GpStatus]
    GdipCreateBitmapFromStreamICM: _Callable[[_interface.IStream,
                                              _Pointer[_type.GpBitmap]],
                                             _enum.GpStatus]
    GdipCreateCachedBitmap: _Callable[[_type.GpBitmap,
                                       _type.GpGraphics,
                                       _Pointer[_type.GpCachedBitmap]],
                                      _enum.GpStatus]
    GdipCreateFromHDC: _Callable[[_type.HDC,
                                  _Pointer[_type.GpGraphics]],
                                 _enum.GpStatus]
    GdipCreateFromHWND: _Callable[[_type.HWND,
                                   _Pointer[_type.GpGraphics]],
                                  _enum.GpStatus]
    GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap,
                                            _Pointer[_type.HBITMAP],
                                            _type.ARGB],
                                           _enum.GpStatus]
    GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap,
                                          _Pointer[_type.HICON]],
                                         _enum.GpStatus]
    GdipCreateImageAttributes: _Callable[[_Pointer[_type.GpImageAttributes]],
                                         _enum.GpStatus]
    GdipCreatePen1: _Callable[[_type.ARGB,
                               _type.REAL,
                               _enum.GpUnit,
                               _Pointer[_type.GpPen]],
                              _enum.GpStatus]
    GdipCreatePen2: _Callable[[_type.GpBrush,
                               _type.REAL,
                               _enum.GpUnit,
                               _Pointer[_type.GpPen]],
                              _enum.GpStatus]
    GdipCreateSolidFill: _Callable[[_type.ARGB,
                                    _Pointer[_type.GpSolidFill]],
                                   _enum.GpStatus]
    GdipDeleteBrush: _Callable[[_type.GpBrush],
                               _enum.GpStatus]
    GdipDeleteCachedBitmap: _Callable[[_type.GpCachedBitmap],
                                      _enum.GpStatus]
    GdipDeleteGraphics: _Callable[[_type.GpGraphics],
                                  _enum.GpStatus]
    GdipDeletePen: _Callable[[_type.GpPen],
                             _enum.GpStatus]
    GdipDisposeImage: _Callable[[_type.GpImage],
                                _enum.GpStatus]
    GdipDisposeImageAttributes: _Callable[[_type.GpImageAttributes],
                                          _enum.GpStatus]
    GdipDrawCachedBitmap: _Callable[[_type.GpGraphics,
                                     _type.GpCachedBitmap,
                                     _type.INT,
                                     _type.INT],
                                    _enum.GpStatus]
    GdipDrawImage: _Callable[[_type.GpGraphics,
                              _type.GpImage,
                              _type.REAL,
                              _type.REAL],
                             _enum.GpStatus]
    GdipDrawImageI: _Callable[[_type.GpGraphics,
                               _type.GpImage,
                               _type.INT,
                               _type.INT],
                              _enum.GpStatus]
    GdipDrawImagePointRect: _Callable[[_type.GpGraphics,
                                       _type.GpImage,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _enum.GpUnit],
                                      _enum.GpStatus]
    GdipDrawImagePointRectI: _Callable[[_type.GpGraphics,
                                        _type.GpImage,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _enum.GpUnit],
                                       _enum.GpStatus]
    GdipDrawImageRectRect: _Callable[[_type.GpGraphics,
                                      _type.GpImage,
                                      _type.REAL,
                                      _type.REAL,
                                      _type.REAL,
                                      _type.REAL,
                                      _type.REAL,
                                      _type.REAL,
                                      _type.REAL,
                                      _type.REAL,
                                      _enum.GpUnit,
                                      _Optional[_type.GpImageAttributes],
                                      _type.DrawImageAbort,
                                      _Optional[_type.PVOID]],
                                     _enum.GpStatus]
    GdipDrawImageRectRectI: _Callable[[_type.GpGraphics,
                                       _Optional[_type.GpImage],
                                       _type.INT,
                                       _type.INT,
                                       _type.INT,
                                       _type.INT,
                                       _type.INT,
                                       _type.INT,
                                       _type.INT,
                                       _type.INT,
                                       _enum.GpUnit,
                                       _Optional[_type.GpImageAttributes],
                                       _type.DrawImageAbort,
                                       _Optional[_type.PVOID]],
                                      _enum.GpStatus]
    GdipFillRectangle: _Callable[[_type.GpGraphics,
                                  _type.GpBrush,
                                  _type.REAL,
                                  _type.REAL,
                                  _type.REAL,
                                  _type.REAL],
                                 _enum.GpStatus]
    GdipFillRectangleI: _Callable[[_type.GpGraphics,
                                   _type.GpBrush,
                                   _type.INT,
                                   _type.INT,
                                   _type.INT,
                                   _type.INT],
                                  _enum.GpStatus]
    GdipGetCompositingQuality: _Callable[[_type.GpGraphics,
                                          _Pointer[_enum.CompositingQuality]],
                                         _enum.GpStatus]
    GdipGetDC: _Callable[[_type.GpGraphics,
                          _Pointer[_type.HDC]],
                         _enum.GpStatus]
    GdipGetDpiX: _Callable[[_type.GpGraphics,
                            _Pointer[_type.REAL]],
                           _enum.GpStatus]
    GdipGetDpiY: _Callable[[_type.GpGraphics,
                            _Pointer[_type.REAL]],
                           _enum.GpStatus]
    GdipGetImageEncoders: _Callable[[_type.UINT,
                                     _type.UINT,
                                     _Pointer[_struct.ImageCodecInfo]],
                                    _enum.GpStatus]
    GdipGetImageEncodersSize: _Callable[[_Pointer[_type.UINT],
                                         _Pointer[_type.UINT]],
                                        _enum.GpStatus]
    GdipGetImageDimension: _Callable[[_type.GpImage,
                                      _Pointer[_type.REAL],
                                      _Pointer[_type.REAL]],
                                     _enum.GpStatus]
    GdipGetImageHeight: _Callable[[_type.GpImage,
                                   _Pointer[_type.UINT]],
                                  _enum.GpStatus]
    GdipGetImagePixelFormat: _Callable[[_type.GpImage,
                                        _Pointer[_type.PixelFormat]],
                                       _enum.GpStatus]
    GdipGetImageWidth: _Callable[[_type.GpImage,
                                  _Pointer[_type.UINT]],
                                 _enum.GpStatus]
    GdipGetImageGraphicsContext: _Callable[[_type.GpImage,
                                            _Pointer[_type.GpGraphics]],
                                           _enum.GpStatus]
    GdipGetInterpolationMode: _Callable[[_type.GpGraphics,
                                         _Pointer[_enum.InterpolationMode]],
                                        _enum.GpStatus]
    GdipGetPenColor: _Callable[[_type.GpPen,
                                _Pointer[_type.ARGB]],
                               _enum.GpStatus]
    GdipGetPenUnit: _Callable[[_type.GpPen,
                               _Pointer[_enum.GpUnit]],
                              _enum.GpStatus]
    GdipGetPenWidth: _Callable[[_type.GpPen,
                                _Pointer[_type.REAL]],
                               _enum.GpStatus]
    GdipGetPixelOffsetMode: _Callable[[_type.GpGraphics,
                                       _Pointer[_enum.PixelOffsetMode]],
                                      _enum.GpStatus]
    GdipGetPropertyItem: _Callable[[_type.GpImage,
                                    _type.PROPID,
                                    _type.UINT,
                                    _Pointer[_struct.PropertyItem]],
                                   _enum.GpStatus]
    GdipGetPropertyItemSize: _Callable[[_type.GpImage,
                                        _type.PROPID,
                                        _Pointer[_type.UINT]],
                                       _enum.GpStatus]
    GdipGetSmoothingMode: _Callable[[_type.GpGraphics,
                                     _Pointer[_enum.SmoothingMode]],
                                    _enum.GpStatus]
    GdipGetSolidFillColor: _Callable[[_type.GpSolidFill,
                                      _Pointer[_type.ARGB]],
                                     _enum.GpStatus]
    GdipGetTextContrast: _Callable[[_type.GpGraphics,
                                    _Pointer[_type.UINT]],
                                   _enum.GpStatus]
    GdipImageGetFrameCount: _Callable[[_type.GpImage,
                                       _Pointer[_struct.GUID],
                                       _Pointer[_type.UINT]],
                                      _enum.GpStatus]
    GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage,
                                                 _Pointer[_type.UINT]],
                                                _enum.GpStatus]
    GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage,
                                                _Pointer[_struct.GUID],
                                                _type.UINT],
                                               _enum.GpStatus]
    GdipImageRotateFlip: _Callable[[_type.GpImage,
                                    _enum.RotateFlipType],
                                   _enum.GpStatus]
    GdipImageSelectActiveFrame: _Callable[[_type.GpImage,
                                           _Pointer[_struct.GUID],
                                           _type.UINT],
                                          _enum.GpStatus]
    GdipLoadImageFromFile: _Callable[[_type.LPWSTR,
                                      _Pointer[_type.GpImage]],
                                     _enum.GpStatus]
    GdipLoadImageFromFileICM: _Callable[[_type.LPWSTR,
                                         _Pointer[_type.GpImage]],
                                        _enum.GpStatus]
    GdipLoadImageFromStream: _Callable[[_interface.IStream,
                                        _Pointer[_type.GpImage]],
                                       _enum.GpStatus]
    GdipLoadImageFromStreamICM: _Callable[[_interface.IStream,
                                           _Pointer[_type.GpImage]],
                                          _enum.GpStatus]
    GdipSaveImageToFile: _Callable[[_type.GpImage,
                                    _type.LPWSTR,
                                    _Pointer[_struct.CLSID],
                                    _Optional[_Pointer[_struct.EncoderParameters]]],
                                   _enum.GpStatus]
    GdipScaleWorldTransform: _Callable[[_type.GpGraphics,
                                        _type.REAL,
                                        _type.REAL,
                                        _enum.GpMatrixOrder],
                                       _enum.GpStatus]
    GdipSetCompositingQuality: _Callable[[_type.GpGraphics,
                                          _enum.CompositingQuality],
                                         _enum.GpStatus]
    GdipSetImageAttributesColorMatrix: _Callable[[_type.GpImageAttributes,
                                                  _enum.ColorAdjustType,
                                                  _type.BOOL,
                                                  _Pointer[_struct.ColorMatrix],
                                                  _Optional[_Pointer[_struct.ColorMatrix]],
                                                  _enum.ColorMatrixFlags],
                                                 _enum.GpStatus]
    GdipSetImageAttributesRemapTable: _Callable[[_type.GpImageAttributes,
                                                 _enum.ColorAdjustType,
                                                 _type.BOOL,
                                                 _type.UINT,
                                                 _Pointer[_struct.ColorMap]],
                                                _enum.GpStatus]
    GdipSetInterpolationMode: _Callable[[_type.GpGraphics,
                                         _enum.InterpolationMode],
                                        _enum.GpStatus]
    GdipSetPenColor: _Callable[[_type.GpPen,
                                _type.ARGB],
                               _enum.GpStatus]
    GdipSetPenUnit: _Callable[[_type.GpPen,
                               _enum.GpUnit],
                              _enum.GpStatus]
    GdipSetPenWidth: _Callable[[_type.GpPen,
                                _type.REAL],
                               _enum.GpStatus]
    GdipSetPixelOffsetMode: _Callable[[_type.GpGraphics,
                                       _enum.PixelOffsetMode],
                                      _enum.GpStatus]
    GdipSetSmoothingMode: _Callable[[_type.GpGraphics,
                                     _enum.SmoothingMode],
                                    _enum.GpStatus]
    GdipSetSolidFillColor: _Callable[[_type.GpSolidFill,
                                      _type.ARGB],
                                     _enum.GpStatus]
    GdipSetTextContrast: _Callable[[_type.GpGraphics,
                                    _type.UINT],
                                   _enum.GpStatus]
    GdipReleaseDC: _Callable[[_type.GpGraphics,
                              _type.HDC],
                             _enum.GpStatus]
    GdipResetWorldTransform: _Callable[[_type.GpGraphics],
                                       _enum.GpStatus]
    GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                               _type.VOID]
    GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],
                               _Pointer[_struct.GdiplusStartupInput],
                               _Optional[_Pointer[_struct.GdiplusStartupInput]]],
                              _enum.Status]


class Kernel32(_Func, metaclass=_WinDLL):
    # consoleapi
    AllocConsole: _Callable[[],
                            _type.BOOL]
    AttachConsole: _Callable[[_type.DWORD],
                             _type.BOOL]
    FreeConsole: _Callable[[],
                           _type.BOOL]
    GetConsoleCP: _Callable[[],
                            _type.UINT]
    GetConsoleMode: _Callable[[_type.HANDLE,
                               _Pointer[_type.DWORD]],
                              _type.BOOL]
    GetConsoleOutputCP: _Callable[[],
                                  _type.UINT]
    GetNumberOfConsoleInputEvents: _Callable[[_type.HANDLE,
                                              _Pointer[_type.DWORD]],
                                             _type.BOOL]
    SetConsoleCtrlHandler: _Callable[[_Optional[_type.PHANDLER_ROUTINE],
                                      _type.BOOL],
                                     _type.BOOL]
    SetConsoleMode: _Callable[[_type.HANDLE,
                               _type.DWORD],
                              _type.BOOL]
    # errhandlingapi
    GetLastError: _Callable[[],
                            _type.DWORD]
    SetLastError: _Callable[[_type.DWORD],
                            _type.VOID]
    # fileapi
    AreShortNamesEnabled: _Callable[[_type.HANDLE,
                                     _Pointer[_type.BOOL]],
                                    _type.BOOL]
    CreateFileA: _Callable[[_type.LPCSTR,
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_type.HANDLE]],
                           _type.HANDLE]
    CreateFileW: _Callable[[_type.LPCWSTR,
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_type.HANDLE]],
                           _type.HANDLE]
    DeleteFileA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    DeleteFileW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
    FindFirstVolumeW: _Callable[[_type.LPWSTR,
                                 _type.DWORD],
                                _type.HANDLE]
    FindNextVolumeW: _Callable[[_type.HANDLE,
                                _type.LPWSTR,
                                _type.DWORD],
                               _type.BOOL]
    FindVolumeClose: _Callable[[_type.HANDLE],
                               _type.BOOL]
    FlushFileBuffers: _Callable[[_type.HANDLE],
                                _type.BOOL]
    GetDiskFreeSpaceA: _Callable[[_type.LPCSTR,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]]],
                                 _type.BOOL]
    GetDiskFreeSpaceW: _Callable[[_type.LPCWSTR,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]]],
                                 _type.BOOL]
    GetDiskFreeSpaceExA: _Callable[[_type.LPCSTR,
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                   _type.BOOL]
    GetDiskFreeSpaceExW: _Callable[[_type.LPCWSTR,
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                   _type.BOOL]
    GetDiskSpaceInformationA: _Callable[[_Optional[_type.LPCSTR],
                                         _Pointer[_struct.DISK_SPACE_INFORMATION]],
                                        _type.BOOL]
    GetDiskSpaceInformationW: _Callable[[_Optional[_type.LPCWSTR],
                                         _Pointer[_struct.DISK_SPACE_INFORMATION]],
                                        _type.BOOL]
    GetDriveTypeA: _Callable[[_type.LPCSTR],
                             _type.UINT]
    GetDriveTypeW: _Callable[[_type.LPCWSTR],
                             _type.UINT]
    GetFileAttributesA: _Callable[[_type.LPCSTR],
                                  _type.DWORD]
    GetFileAttributesW: _Callable[[_type.LPCWSTR],
                                  _type.DWORD]
    GetFileSize: _Callable[[_type.HANDLE,
                            _Optional[_Pointer[_type.DWORD]]],
                           _type.DWORD]
    GetFileSizeEx: _Callable[[_type.HANDLE,
                              _Pointer[_union.LARGE_INTEGER]],
                             _type.BOOL]
    GetFileTime: _Callable[[_type.HANDLE,
                            _Optional[_Pointer[_struct.FILETIME]],
                            _Optional[_Pointer[_struct.FILETIME]],
                            _Optional[_Pointer[_struct.FILETIME]]],
                           _type.BOOL]
    GetFileType: _Callable[[_type.HANDLE],
                           _type.DWORD]
    GetFinalPathNameByHandleA: _Callable[[_type.HANDLE,
                                          _type.LPSTR,
                                          _type.DWORD,
                                          _type.DWORD],
                                         _type.DWORD]
    GetFinalPathNameByHandleW: _Callable[[_type.HANDLE,
                                          _type.LPWSTR,
                                          _type.DWORD,
                                          _type.DWORD],
                                         _type.DWORD]
    GetLogicalDrives: _Callable[[],
                                _type.DWORD]
    GetLogicalDriveStringsA: _Callable[[_type.DWORD,
                                        _Optional[_type.LPSTR]],
                                       _type.DWORD]
    GetLogicalDriveStringsW: _Callable[[_type.DWORD,
                                        _Optional[_type.LPWSTR]],
                                       _type.DWORD]
    GetLongPathNameA: _Callable[[_type.LPCSTR,
                                 _Optional[_type.LPSTR],
                                 _type.DWORD],
                                _type.DWORD]
    GetLongPathNameW: _Callable[[_type.LPCWSTR,
                                 _Optional[_type.LPWSTR],
                                 _type.DWORD],
                                _type.DWORD]
    GetShortPathNameW: _Callable[[_type.LPCWSTR,
                                  _Optional[_type.LPWSTR],
                                  _type.DWORD],
                                 _type.DWORD]
    GetTempFileNameW: _Callable[[_type.LPCWSTR,
                                 _type.LPCWSTR,
                                 _type.UINT,
                                 _type.LPWSTR],
                                _type.UINT]
    GetTempPathA: _Callable[[_type.DWORD,
                             _type.LPSTR],
                            _type.DWORD]
    GetTempPathW: _Callable[[_type.DWORD,
                             _type.LPWSTR],
                            _type.DWORD]
    GetTempPath2A: _Callable[[_type.DWORD,
                              _type.LPSTR],
                             _type.DWORD]
    GetTempPath2W: _Callable[[_type.DWORD,
                              _type.LPWSTR],
                             _type.DWORD]
    GetVolumePathNameW: _Callable[[_type.LPCWSTR,
                                   _type.LPWSTR,
                                   _type.DWORD],
                                  _type.DWORD]
    LocalFileTimeToFileTime: _Callable[[_Pointer[_struct.FILETIME],
                                        _Pointer[_struct.FILETIME]],
                                       _type.BOOL]
    LockFile: _Callable[[_type.HANDLE,
                         _type.DWORD,
                         _type.DWORD,
                         _type.DWORD,
                         _type.DWORD],
                        _type.BOOL]
    QueryDosDeviceW: _Callable[[_type.LPCWSTR,
                                _type.LPWSTR,
                                _type.DWORD],
                               _type.DWORD]
    ReadFile: _Callable[[_type.HANDLE,
                         _Optional[_type.LPVOID],
                         _type.DWORD,
                         _Optional[_Pointer[_type.DWORD]],
                         _Optional[_Pointer[_struct.OVERLAPPED]]],
                        _type.BOOL]
    RemoveDirectoryA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    RemoveDirectoryW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    SetEndOfFile: _Callable[[_type.HANDLE],
                            _type.BOOL]
    SetFileAttributesA: _Callable[[_type.LPCSTR,
                                   _type.DWORD],
                                  _type.BOOL]
    SetFileAttributesW: _Callable[[_type.LPCWSTR,
                                   _type.DWORD],
                                  _type.BOOL]
    SetFileValidData: _Callable[[_type.HANDLE,
                                 _type.LONGLONG],
                                _type.BOOL]
    UnlockFile: _Callable[[_type.HANDLE,
                           _type.DWORD,
                           _type.DWORD,
                           _type.DWORD,
                           _type.DWORD],
                          _type.BOOL]
    # handleapi
    CloseHandle: _Callable[[_type.HANDLE],
                           _type.BOOL]
    # heapapi
    GetProcessHeap: _Callable[[],
                              _type.HANDLE]
    GetProcessHeaps: _Callable[[_type.DWORD,
                                _Pointer[_type.HANDLE]],
                               _type.DWORD]
    HeapAlloc: _Callable[[_type.HANDLE,
                          _type.DWORD,
                          _type.SIZE_T],
                         _type.LPVOID]
    HeapCompact: _Callable[[_type.HANDLE,
                            _type.DWORD],
                           _type.SIZE_T]
    HeapCreate: _Callable[[_type.DWORD,
                           _type.SIZE_T,
                           _type.SIZE_T],
                          _type.HANDLE]
    HeapDestroy: _Callable[[_type.HANDLE],
                           _type.BOOL]
    HeapFree: _Callable[[_type.HANDLE,
                         _type.DWORD,
                         _Optional[_type.LPVOID]],
                        _type.BOOL]
    HeapLock: _Callable[[_type.HANDLE],
                        _type.BOOL]
    HeapQueryInformation: _Callable[[_Optional[_type.HANDLE],
                                     _enum.HEAP_INFORMATION_CLASS,
                                     _Optional[_type.PVOID],
                                     _type.SIZE_T,
                                     _Optional[_Pointer[_type.SIZE_T]]],
                                    _type.BOOL]
    HeapReAlloc: _Callable[[_type.HANDLE,
                            _type.DWORD,
                            _Optional[_type.LPVOID],
                            _type.SIZE_T],
                           _type.LPVOID]
    HeapSetInformation: _Callable[[_Optional[_type.HANDLE],
                                   _enum.HEAP_INFORMATION_CLASS,
                                   _Optional[_type.PVOID],
                                   _type.SIZE_T],
                                  _type.BOOL]
    HeapSize: _Callable[[_type.HANDLE,
                         _type.DWORD,
                         _type.LPCVOID],
                        _type.SIZE_T]
    HeapSummary: _Callable[[_type.HANDLE,
                            _type.DWORD,
                            _struct.HEAP_SUMMARY],
                           _type.BOOL]
    HeapUnlock: _Callable[[_type.HANDLE],
                          _type.BOOL]
    HeapValidate: _Callable[[_type.HANDLE,
                             _type.DWORD,
                             _Optional[_type.LPCVOID]],
                            _type.BOOL]
    HeapWalk: _Callable[[_type.HANDLE,
                         _Pointer[_struct.PROCESS_HEAP_ENTRY]],
                        _type.BOOL]
    # libloaderapi
    AddDllDirectory: _Callable[[_type.LPCWSTR],
                               _type.DLL_DIRECTORY_COOKIE]
    DisableThreadLibraryCalls: _Callable[[_type.HMODULE],
                                         _type.BOOL]
    EnumResourceLanguagesA: _Callable[[_Optional[_type.HMODULE],
                                       _type.LPCSTR,
                                       _type.LPCSTR,
                                       _type.ENUMRESLANGPROCA,
                                       _type.LONG_PTR],
                                      _type.BOOL]
    EnumResourceLanguagesW: _Callable[[_Optional[_type.HMODULE],
                                       _type.LPCWSTR,
                                       _type.LPCWSTR,
                                       _type.ENUMRESLANGPROCW,
                                       _type.LONG_PTR],
                                      _type.BOOL]
    EnumResourceLanguagesExA: _Callable[[_Optional[_type.HMODULE],
                                         _type.LPCSTR,
                                         _type.LPCSTR,
                                         _type.ENUMRESLANGPROCA,
                                         _Optional[_type.LONG_PTR],
                                         _type.DWORD,
                                         _type.LANGID],
                                        _type.BOOL]
    EnumResourceLanguagesExW: _Callable[[_Optional[_type.HMODULE],
                                         _type.LPCWSTR,
                                         _type.LPCWSTR,
                                         _type.ENUMRESLANGPROCW,
                                         _Optional[_type.LONG_PTR],
                                         _type.DWORD,
                                         _type.LANGID],
                                        _type.BOOL]
    EnumResourceNamesA: _Callable[[_Optional[_type.HMODULE],
                                   _type.LPCSTR,
                                   _type.ENUMRESNAMEPROCA,
                                   _type.LONG_PTR],
                                  _type.BOOL]
    EnumResourceNamesW: _Callable[[_Optional[_type.HMODULE],
                                   _type.LPCWSTR,
                                   _type.ENUMRESNAMEPROCW,
                                   _type.LONG_PTR],
                                  _type.BOOL]
    EnumResourceNamesExA: _Callable[[_Optional[_type.HMODULE],
                                     _type.LPCSTR,
                                     _type.ENUMRESNAMEPROCA,
                                     _type.LONG_PTR,
                                     _type.DWORD,
                                     _type.LANGID],
                                    _type.BOOL]
    EnumResourceNamesExW: _Callable[[_Optional[_type.HMODULE],
                                     _type.LPCWSTR,
                                     _type.ENUMRESNAMEPROCW,
                                     _type.LONG_PTR,
                                     _type.DWORD,
                                     _type.LANGID],
                                    _type.BOOL]
    EnumResourceTypesA: _Callable[[_Optional[_type.HMODULE],
                                   _type.ENUMRESTYPEPROCA,
                                   _type.LONG_PTR],
                                  _type.BOOL]
    EnumResourceTypesW: _Callable[[_Optional[_type.HMODULE],
                                   _type.ENUMRESTYPEPROCW,
                                   _type.LONG_PTR],
                                  _type.BOOL]
    EnumResourceTypesExA: _Callable[[_Optional[_type.HMODULE],
                                     _type.ENUMRESTYPEPROCA,
                                     _type.LONG_PTR,
                                     _type.DWORD,
                                     _type.LANGID],
                                    _type.BOOL]
    EnumResourceTypesExW: _Callable[[_Optional[_type.HMODULE],
                                     _type.ENUMRESTYPEPROCW,
                                     _type.LONG_PTR,
                                     _type.DWORD,
                                     _type.LANGID],
                                    _type.BOOL]
    FreeLibrary: _Callable[[_type.HMODULE],
                           _type.BOOL]
    FreeLibraryAndExitThread: _Callable[[_type.HMODULE,
                                         _type.DWORD],
                                        _type.VOID]
    FreeResource: _Callable[[_type.HGLOBAL],
                            _type.BOOL]
    FindResourceW: _Callable[[_Optional[_type.HMODULE],
                              _type.LPCWSTR,
                              _type.LPCWSTR],
                             _type.HRSRC]
    FindResourceExW: _Callable[[_Optional[_type.HMODULE],
                                _type.LPCWSTR,
                                _type.LPCWSTR,
                                _type.WORD],
                               _type.HRSRC]
    FindStringOrdinal: _Callable[[_type.DWORD,
                                  _type.LPCWSTR,
                                  _type.c_int,
                                  _type.LPCWSTR,
                                  _type.c_int,
                                  _type.BOOL],
                                 _type.c_int]
    GetModuleFileNameA: _Callable[[_Optional[_type.HMODULE],
                                   _type.LPSTR,
                                   _type.DWORD],
                                  _type.DWORD]
    GetModuleFileNameW: _Callable[[_Optional[_type.HMODULE],
                                   _type.LPWSTR,
                                   _type.DWORD],
                                  _type.DWORD]
    GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                                _type.HMODULE]
    GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                                _type.HMODULE]
    GetModuleHandleExA: _Callable[[_type.DWORD,
                                   _Optional[_type.LPCSTR],
                                   _Pointer[_type.HMODULE]],
                                  _type.BOOL]
    GetModuleHandleExW: _Callable[[_type.DWORD,
                                   _Optional[_type.LPCWSTR],
                                   _Pointer[_type.HMODULE]],
                                  _type.BOOL]
    GetProcAddress: _Callable[[_type.HMODULE,
                               _type.LPCSTR],
                              _type.FARPROC]
    LoadLibraryA: _Callable[[_type.LPCSTR],
                            _type.HMODULE]
    LoadLibraryW: _Callable[[_type.LPCWSTR],
                            _type.HMODULE]
    LoadLibraryExA: _Callable[[_type.LPCSTR,
                               _type.HANDLE,
                               _type.DWORD],
                              _type.HMODULE]
    LoadLibraryExW: _Callable[[_type.LPCWSTR,
                               _type.HANDLE,
                               _type.DWORD],
                              _type.HMODULE]
    LoadResource: _Callable[[_Optional[_type.HMODULE],
                             _type.HRSRC],
                            _type.HGLOBAL]
    LockResource: _Callable[[_type.HGLOBAL],
                            _type.LPVOID]
    RemoveDllDirectory: _Callable[[_type.DLL_DIRECTORY_COOKIE],
                                  _type.BOOL]
    SetDefaultDllDirectories: _Callable[[_type.DWORD],
                                        _type.BOOL]
    SizeofResource: _Callable[[_Optional[_type.HMODULE],
                               _type.HRSRC],
                              _type.DWORD]
    # processthreadsapi
    ExitProcess: _Callable[[_type.UINT],
                           _type.VOID]
    GetCurrentProcess: _Callable[[],
                                 _type.HANDLE]
    GetCurrentProcessId: _Callable[[],
                                   _type.DWORD]
    GetExitCodeProcess: _Callable[[_type.HANDLE,
                                   _Pointer[_type.DWORD]],
                                  _type.BOOL]
    SwitchToThread: _Callable[[],
                              _type.BOOL]
    TerminateProcess: _Callable[[_type.HANDLE,
                                 _type.UINT],
                                _type.BOOL]
    # profileapi
    QueryPerformanceCounter: _Callable[[_Pointer[_union.LARGE_INTEGER]],
                                       _type.BOOL]
    QueryPerformanceFrequency: _Callable[[_Pointer[_union.LARGE_INTEGER]],
                                         _type.BOOL]
    # synchapi
    CancelWaitableTimer: _Callable[[_type.HANDLE],
                                   _type.BOOL]
    CreateEventA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                             _type.BOOL,
                             _type.BOOL,
                             _Optional[_type.LPCSTR]],
                            _type.HANDLE]
    CreateEventW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                             _type.BOOL,
                             _type.BOOL,
                             _Optional[_type.LPCWSTR]],
                            _type.HANDLE]
    CreateEventExA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                               _Optional[_type.LPCSTR],
                               _type.DWORD,
                               _type.DWORD],
                              _type.HANDLE]
    CreateEventExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                               _Optional[_type.LPCWSTR],
                               _type.DWORD,
                               _type.DWORD],
                              _type.HANDLE]
    CreateMutexA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                             _type.BOOL,
                             _Optional[_type.LPCSTR]],
                            _type.HANDLE]
    CreateMutexW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                             _type.BOOL,
                             _Optional[_type.LPCWSTR]],
                            _type.HANDLE]
    CreateMutexExA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                               _Optional[_type.LPCSTR],
                               _type.DWORD,
                               _type.DWORD],
                              _type.HANDLE]
    CreateMutexExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                               _Optional[_type.LPCWSTR],
                               _type.DWORD,
                               _type.DWORD],
                              _type.HANDLE]
    CreateSemaphoreW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                                 _type.LONG,
                                 _type.LONG,
                                 _Optional[_type.LPCWSTR]],
                                _type.HANDLE]
    CreateSemaphoreExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                                   _type.LONG,
                                   _type.LONG,
                                   _Optional[_type.LPCWSTR],
                                   _type.DWORD,
                                   _type.DWORD],
                                  _type.HANDLE]
    CreateWaitableTimerW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                                     _type.BOOL,
                                     _Optional[_type.LPCWSTR]],
                                    _type.HANDLE]
    CreateWaitableTimerExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                                       _Optional[_type.LPCWSTR],
                                       _type.DWORD,
                                       _type.DWORD],
                                      _type.HANDLE]
    OpenEventA: _Callable[[_type.DWORD,
                           _type.BOOL,
                           _type.LPCSTR],
                          _type.HANDLE]
    OpenEventW: _Callable[[_type.DWORD,
                           _type.BOOL,
                           _type.LPCWSTR],
                          _type.HANDLE]
    OpenMutexA: _Callable[[_type.DWORD,
                           _type.BOOL,
                           _type.LPCSTR],
                          _type.HANDLE]
    OpenMutexW: _Callable[[_type.DWORD,
                           _type.BOOL,
                           _type.LPCWSTR],
                          _type.HANDLE]
    OpenSemaphoreW: _Callable[[_type.DWORD,
                               _type.BOOL,
                               _type.LPCWSTR],
                              _type.HANDLE]
    OpenWaitableTimerW: _Callable[[_type.DWORD,
                                   _type.BOOL,
                                   _type.LPCWSTR],
                                  _type.HANDLE]
    ResetEvent: _Callable[[_type.HANDLE],
                          _type.BOOL]
    ReleaseMutex: _Callable[[_type.HANDLE],
                            _type.BOOL]
    ReleaseSemaphore: _Callable[[_type.HANDLE,
                                 _type.LONG,
                                 _Optional[_Pointer[_type.LONG]]],
                                _type.BOOL]
    SetEvent: _Callable[[_type.HANDLE],
                        _type.BOOL]
    SignalObjectAndWait: _Callable[[_type.HANDLE,
                                    _type.HANDLE,
                                    _type.DWORD,
                                    _type.BOOL],
                                   _type.DWORD]
    Sleep: _Callable[[_type.DWORD],
                     _type.VOID]
    SleepEx: _Callable[[_type.DWORD,
                        _type.BOOL],
                       _type.DWORD]
    WaitForMultipleObjects: _Callable[[_type.DWORD,
                                       _Pointer[_type.HANDLE],
                                       _type.BOOL,
                                       _type.DWORD],
                                      _type.DWORD]
    WakeByAddressAll: _Callable[[_type.PVOID],
                                _type.VOID]
    WakeByAddressSingle: _Callable[[_type.PVOID],
                                   _type.VOID]
    # sysinfoapi
    GetComputerNameExA: _Callable[[_enum.COMPUTER_NAME_FORMAT,
                                   _Optional[_type.LPSTR],
                                   _Pointer[_type.DWORD]],
                                  _type.BOOL]
    GetComputerNameExW: _Callable[[_enum.COMPUTER_NAME_FORMAT,
                                   _Optional[_type.LPWSTR],
                                   _Pointer[_type.DWORD]],
                                  _type.BOOL]
    GetSystemDirectoryA: _Callable[[_Optional[_type.LPSTR],
                                    _type.UINT],
                                   _type.UINT]
    GetSystemDirectoryW: _Callable[[_Optional[_type.LPWSTR],
                                    _type.UINT],
                                   _type.UINT]
    GetSystemWindowsDirectoryA: _Callable[[_Optional[_type.LPSTR],
                                           _type.UINT],
                                          _type.UINT]
    GetSystemWindowsDirectoryW: _Callable[[_Optional[_type.LPWSTR],
                                           _type.UINT],
                                          _type.UINT]
    GetVersionExA: _Callable[[_Pointer[_struct.OSVERSIONINFOA]],
                             _type.BOOL]
    GetVersionExW: _Callable[[_Pointer[_struct.OSVERSIONINFOW]],
                             _type.BOOL]
    GetWindowsDirectoryA: _Callable[[_Optional[_type.LPSTR],
                                     _type.UINT],
                                    _type.UINT]
    GetWindowsDirectoryW: _Callable[[_Optional[_type.LPWSTR],
                                     _type.UINT],
                                    _type.UINT]
    SetComputerNameExW: _Callable[[_enum.COMPUTER_NAME_FORMAT,
                                   _type.LPCWSTR],
                                  _type.BOOL]
    SetSystemTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],
                             _type.BOOL]
    # WinBase
    ActivateActCtx: _Callable[[_Optional[_type.HANDLE],
                               _Pointer[_type.ULONG_PTR]],
                              _type.BOOL]
    AddAtomA: _Callable[[_Optional[_type.LPCSTR]],
                        _type.ATOM]
    AddAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                        _type.ATOM]
    AddRefActCtx: _Callable[[_type.HANDLE],
                            _type.VOID]
    AssignProcessToJobObject: _Callable[[_type.HANDLE,
                                         _type.HANDLE],
                                        _type.BOOL]
    BeginUpdateResourceA: _Callable[[_type.LPCSTR,
                                     _type.BOOL],
                                    _type.HANDLE]
    BeginUpdateResourceW: _Callable[[_type.LPCWSTR,
                                     _type.BOOL],
                                    _type.HANDLE]
    CreateActCtxA: _Callable[[_Pointer[_struct.ACTCTXA]],
                             _type.HANDLE]
    CreateActCtxW: _Callable[[_Pointer[_struct.ACTCTXW]],
                             _type.HANDLE]
    DeactivateActCtx: _Callable[[_type.DWORD,
                                 _type.ULONG_PTR],
                                _type.BOOL]
    EndUpdateResourceA: _Callable[[_type.HANDLE,
                                   _type.BOOL],
                                  _type.BOOL]
    EndUpdateResourceW: _Callable[[_type.HANDLE,
                                   _type.BOOL],
                                  _type.BOOL]
    FindAtomA: _Callable[[_Optional[_type.LPCSTR]],
                         _type.ATOM]
    FindAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                         _type.ATOM]
    FormatMessageA: _Callable[[_type.DWORD,
                               _Optional[_type.LPCVOID],
                               _type.DWORD,
                               _type.DWORD,
                               _type.LPSTR,
                               _type.DWORD,
                               _Optional[_Pointer[_type.va_list]]],
                              _type.DWORD]
    FormatMessageW: _Callable[[_type.DWORD,
                               _Optional[_type.LPCVOID],
                               _type.DWORD,
                               _type.DWORD,
                               _type.LPWSTR,
                               _type.DWORD,
                               _Optional[_Pointer[_type.va_list]]],
                              _type.DWORD]
    GetBinaryTypeA: _Callable[[_type.LPCSTR,
                               _Pointer[_type.DWORD]],
                              _type.BOOL]
    GetBinaryTypeW: _Callable[[_type.LPCWSTR,
                               _Pointer[_type.DWORD]],
                              _type.BOOL]
    GetCurrentActCtx: _Callable[[_Pointer[_type.HANDLE]],
                                _type.BOOL]
    GetProfileIntA: _Callable[[_type.LPCSTR,
                               _type.LPCSTR,
                               _type.INT],
                              _type.UINT]
    GetProfileIntW: _Callable[[_type.LPCWSTR,
                               _type.LPCWSTR,
                               _type.INT],
                              _type.UINT]
    GetSystemPowerStatus: _Callable[[_Pointer[_struct.SYSTEM_POWER_STATUS]],
                                    _type.BOOL]
    GlobalAddAtomA: _Callable[[_Optional[_type.LPCSTR]],
                              _type.ATOM]
    GlobalAddAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                              _type.ATOM]
    GlobalAddAtomExA: _Callable[[_Optional[_type.LPCSTR],
                                 _type.DWORD],
                                _type.ATOM]
    GlobalAddAtomExW: _Callable[[_Optional[_type.LPCWSTR],
                                 _type.DWORD],
                                _type.ATOM]
    GlobalAlloc: _Callable[[_type.UINT,
                            _type.SIZE_T],
                           _type.HGLOBAL]
    GlobalFindAtomA: _Callable[[_Optional[_type.LPCSTR]],
                               _type.ATOM]
    GlobalFindAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                               _type.ATOM]
    GlobalLock: _Callable[[_type.HGLOBAL],
                          _type.LPVOID]
    GlobalUnlock: _Callable[[_type.HGLOBAL],
                            _type.BOOL]
    LocalFree: _Callable[[_type.HLOCAL],
                         _type.HLOCAL]
    MoveFileA: _Callable[[_type.LPCSTR,
                          _type.LPCSTR],
                         _type.BOOL]
    MoveFileW: _Callable[[_type.LPCWSTR,
                          _type.LPCWSTR],
                         _type.BOOL]
    OpenJobObjectA: _Callable[[_type.DWORD,
                               _type.BOOL,
                               _type.LPCSTR],
                              _type.HANDLE]
    OpenJobObjectW: _Callable[[_type.DWORD,
                               _type.BOOL,
                               _type.LPCWSTR],
                              _type.HANDLE]
    QueryActCtxW: _Callable[[_type.DWORD,
                             _type.HANDLE,
                             _Optional[_type.PVOID],
                             _type.ULONG,
                             _Optional[_type.PVOID],
                             _type.SIZE_T,
                             _Optional[_Pointer[_type.SIZE_T]]],
                            _type.BOOL]
    QueryActCtxSettingsW: _Callable[[_Optional[_type.DWORD],
                                     _Optional[_type.HANDLE],
                                     _Optional[_type.PCWSTR],
                                     _type.PCWSTR,
                                     _Optional[_type.PWSTR],
                                     _type.SIZE_T,
                                     _Optional[_Pointer[_type.SIZE_T]]],
                                    _type.BOOL]
    ReleaseActCtx: _Callable[[_type.HANDLE],
                             _type.VOID]
    SetDllDirectoryA: _Callable[[_Optional[_type.LPCSTR]],
                                _type.BOOL]
    SetDllDirectoryW: _Callable[[_Optional[_type.LPCWSTR]],
                                _type.BOOL]
    SetSystemPowerState: _Callable[[_type.BOOL,
                                    _type.BOOL],
                                   _type.BOOL]
    TerminateJobObject: _Callable[[_type.HANDLE,
                                   _type.UINT],
                                  _type.BOOL]
    UpdateResourceA: _Callable[[_type.HANDLE,
                                _type.LPCSTR,
                                _type.LPCSTR,
                                _type.WORD,
                                _Optional[_type.LPVOID],
                                _type.DWORD],
                               _type.BOOL]
    UpdateResourceW: _Callable[[_type.HANDLE,
                                _type.LPCWSTR,
                                _type.LPCWSTR,
                                _type.WORD,
                                _Optional[_type.LPVOID],
                                _type.DWORD],
                               _type.BOOL]
    VerifyVersionInfoA: _Callable[[_Pointer[_struct.OSVERSIONINFOEXA],
                                   _type.DWORD,
                                   _type.DWORDLONG],
                                  _type.BOOL]
    VerifyVersionInfoW: _Callable[[_Pointer[_struct.OSVERSIONINFOEXW],
                                   _type.DWORD,
                                   _type.DWORDLONG],
                                  _type.BOOL]
    WritePrivateProfileSectionA: _Callable[[_Optional[_type.LPCSTR],
                                            _Optional[_type.LPCSTR],
                                            _Optional[_type.LPCSTR]],
                                           _type.BOOL]
    WritePrivateProfileSectionW: _Callable[[_Optional[_type.LPCWSTR],
                                            _Optional[_type.LPCWSTR],
                                            _Optional[_type.LPCWSTR]],
                                           _type.BOOL]
    WritePrivateProfileStringA: _Callable[[_Optional[_type.LPCSTR],
                                           _Optional[_type.LPCSTR],
                                           _Optional[_type.LPCSTR],
                                           _Optional[_type.LPCSTR]],
                                          _type.BOOL]
    WritePrivateProfileStringW: _Callable[[_Optional[_type.LPCWSTR],
                                           _Optional[_type.LPCWSTR],
                                           _Optional[_type.LPCWSTR],
                                           _Optional[_type.LPCWSTR]],
                                          _type.BOOL]
    WriteProfileSectionA: _Callable[[_type.LPCSTR,
                                     _type.LPCSTR],
                                    _type.BOOL]
    WriteProfileSectionW: _Callable[[_type.LPCWSTR,
                                     _type.LPCWSTR],
                                    _type.BOOL]
    WriteProfileStringA: _Callable[[_Optional[_type.LPCSTR],
                                    _Optional[_type.LPCSTR],
                                    _Optional[_type.LPCSTR]],
                                   _type.BOOL]
    WriteProfileStringW: _Callable[[_Optional[_type.LPCWSTR],
                                    _Optional[_type.LPCWSTR],
                                    _Optional[_type.LPCWSTR]],
                                   _type.BOOL]
    ZombifyActCtx: _Callable[[_type.HANDLE],
                             _type.BOOL]
    # WinNls
    GetSystemDefaultLangID: _Callable[[],
                                      _type.LANGID]
    GetSystemDefaultLCID: _Callable[[],
                                    _type.LCID]
    GetSystemDefaultLocaleName: _Callable[[_type.LPWSTR,
                                           _type.c_int],
                                          _type.c_int]
    GetThreadLocale: _Callable[[],
                               _type.LCID]
    GetUserDefaultLangID: _Callable[[],
                                    _type.LANGID]
    GetUserDefaultLCID: _Callable[[],
                                  _type.LCID]
    GetUserDefaultUILanguage: _Callable[[],
                                        _type.LANGID]
    GetUserDefaultLocaleName: _Callable[[_type.LPWSTR,
                                         _type.c_int],
                                        _type.c_int]
    SetThreadLocale: _Callable[[_type.LCID],
                               _type.BOOL]
    # winnt
    RtlGetProductInfo: _Callable[[_type.DWORD,
                                  _type.DWORD,
                                  _type.DWORD,
                                  _type.DWORD,
                                  _Pointer[_type.DWORD]],
                                 _type.BOOLEAN]
    VerSetConditionMask: _Callable[[_type.ULONGLONG,
                                    _type.DWORD,
                                    _type.BYTE],
                                   _type.ULONGLONG]


class MSCorEE(_Func, metaclass=_WinDLL):
    # cor
    CoEEShutDownCOM: _Callable[[],
                               _type.c_void]
    CoInitializeCor: _Callable[[_type.DWORD],
                               _type.HRESULT]
    CoInitializeEE: _Callable[[_enum.COINITIEE],
                              _type.HRESULT]
    CoUninitializeCor: _Callable[[],
                                 _type.c_void]
    CoUninitializeEE: _Callable[[_type.BOOL],
                                _type.c_void]
    # mscoree
    CorBindToCurrentRuntime: _Callable[[_Optional[_type.LPCWSTR],
                                        _Pointer[_struct.CLSID],
                                        _Pointer[_struct.IID],
                                        _type.LPVOID],
                                       _type.HRESULT]
    CorBindToRuntimeEx: _Callable[[_Optional[_type.LPCWSTR],
                                   _Optional[_type.LPCWSTR],
                                   _enum.STARTUP_FLAGS,
                                   _Pointer[_struct.CLSID],
                                   _Pointer[_struct.IID],
                                   _type.LPVOID],
                                  _type.HRESULT]


class Msimg32(_Func, metaclass=_WinDLL):
    # wingdi
    AlphaBlend: _Callable[[_type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _struct.BLENDFUNCTION],
                          _type.BOOL]


# noinspection PyPep8Naming
class msvcrt(_Func, metaclass=_WinDLL):
    # corecrt_malloc
    calloc: _Callable[[_type.c_size_t,
                       _type.c_size_t],
                      _type.c_void_p]
    free: _Callable[[_type.c_void_p],
                    _type.c_void]
    malloc: _Callable[[_type.c_size_t],
                      _type.c_void_p]
    realloc: _Callable[[_type.c_void_p,
                        _type.c_size_t],
                       _type.c_void_p]
    # corecrt_wstring
    wcscspn: _Callable[[_type.c_wchar_p,
                        _type.c_wchar_p],
                       _type.c_size_t]
    wcscmp: _Callable[[_type.c_wchar_p,
                       _type.c_wchar_p],
                      _type.c_int]
    wcslen: _Callable[[_type.c_wchar_p],
                      _type.c_size_t]
    wcsncmp: _Callable[[_type.c_wchar_p,
                        _type.c_wchar_p,
                        _type.c_size_t],
                       _type.c_int]
    wcsnlen: _Callable[[_type.c_wchar_p,
                        _type.c_size_t],
                       _type.c_size_t]
    # vcruntime_string
    memcpy: _Callable[[_type.c_void_p,
                       _type.c_void_p,
                       _type.c_size_t],
                      _type.c_void_p]
    memmove: _Callable[[_type.c_void_p,
                        _type.c_void_p,
                        _type.c_size_t],
                       _type.c_void_p]
    memset: _Callable[[_type.c_void_p,
                       _type.c_int,
                       _type.c_size_t],
                      _type.c_void_p]


# noinspection PyPep8Naming
class ntdll(_Func, metaclass=_WinDLL):
    RtlAreLongPathsEnabled: _Callable[[],
                                      _type.c_ubyte]
    # winternl
    RtlAnsiStringToUnicodeString: _Callable[[_Pointer[_struct.UNICODE_STRING],
                                             _Pointer[_struct.ANSI_STRING],
                                             _type.BOOLEAN],
                                            _type.NTSTATUS]
    RtlFreeAnsiString: _Callable[[_Pointer[_struct.ANSI_STRING]],
                                 _type.VOID]
    RtlFreeOemString: _Callable[[_Pointer[_struct.OEM_STRING]],
                                _type.VOID]
    RtlFreeUnicodeString: _Callable[[_Pointer[_struct.UNICODE_STRING]],
                                    _type.VOID]
    RtlInitAnsiString: _Callable[[_Pointer[_struct.ANSI_STRING],
                                  _type.PCSZ],
                                 _type.VOID]
    RtlInitAnsiStringEx: _Callable[[_Pointer[_struct.ANSI_STRING],
                                    _type.PCSZ],
                                   _type.NTSTATUS]
    RtlInitString: _Callable[[_Pointer[_struct.STRING],
                              _type.PCSZ],
                             _type.VOID]
    RtlInitStringEx: _Callable[[_Pointer[_struct.STRING],
                                _type.PCSZ],
                               _type.NTSTATUS]
    RtlInitUnicodeString: _Callable[[_Pointer[_struct.UNICODE_STRING],
                                     _type.PCWSTR],
                                    _type.VOID]
    RtlUnicodeStringToAnsiString: _Callable[[_Pointer[_struct.ANSI_STRING],
                                             _Pointer[_struct.UNICODE_STRING],
                                             _type.BOOLEAN],
                                            _type.NTSTATUS]
    RtlUnicodeStringToOemString: _Callable[[_Pointer[_struct.OEM_STRING],
                                            _Pointer[_struct.UNICODE_STRING],
                                            _type.BOOLEAN],
                                           _type.NTSTATUS]


class Ole32(_Func, metaclass=_WinDLL):
    # combaseapi
    CLSIDFromString: _Callable[[_type.LPCOLESTR,
                                _Pointer[_struct.CLSID]],
                               _type.HRESULT]
    CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],
                            _type.HRESULT]
    CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],
                                 _Optional[_Pointer[_interface.IUnknown]],
                                 _type.DWORD,
                                 _Pointer[_struct.IID],
                                 _type.LPVOID],
                                _type.HRESULT]
    CoInitializeEx: _Callable[[_Optional[_type.LPVOID],
                               _type.DWORD],
                              _type.HRESULT]
    CoTaskMemFree: _Callable[[_Optional[_type.LPVOID]],
                             _type.c_void]
    CoUninitialize: _Callable[[],
                              _type.VOID]
    IIDFromString: _Callable[[_type.LPCOLESTR,
                              _Pointer[_struct.IID]],
                             _type.HRESULT]
    StringFromCLSID: _Callable[[_Pointer[_struct.CLSID],
                                _Pointer[_type.LPOLESTR]],
                               _type.HRESULT]
    StringFromGUID2: _Callable[[_Pointer[_struct.GUID],
                                _type.LPOLESTR,
                                _type.c_int],
                               _type.c_int]
    StringFromIID: _Callable[[_Pointer[_struct.IID],
                              _Pointer[_type.LPOLESTR]],
                             _type.HRESULT]
    # guiddef
    IsEqualGUID: _Callable[[_Pointer[_struct.GUID],
                            _Pointer[_struct.GUID]],
                           _type.c_int]
    # objbase
    CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                            _type.HRESULT]
    # propidl
    FreePropVariantArray: _Callable[[_type.ULONG,
                                     _Pointer[_struct.PROPVARIANT]],
                                    _type.HRESULT]
    PropVariantClear: _Callable[[_Pointer[_struct.PROPVARIANT]],
                                _type.HRESULT]
    PropVariantCopy: _Callable[[_Pointer[_struct.PROPVARIANT],
                                _Pointer[_struct.PROPVARIANT]],
                               _type.HRESULT]


class Oleacc(_Func, metaclass=_WinDLL):
    GetProcessHandleFromHwnd: _Callable[[_type.HWND],
                                        _type.HANDLE]
    # oleacc
    GetRoleTextA: _Callable[[_type.DWORD,
                             _Optional[_type.LPSTR],
                             _type.UINT],
                            _type.UINT]
    GetRoleTextW: _Callable[[_type.DWORD,
                             _Optional[_type.LPWSTR],
                             _type.UINT],
                            _type.UINT]
    GetStateTextA: _Callable[[_type.DWORD,
                              _Optional[_type.LPSTR],
                              _type.UINT],
                             _type.UINT]
    GetStateTextW: _Callable[[_type.DWORD,
                              _Optional[_type.LPWSTR],
                              _type.UINT],
                             _type.UINT]


class OleAut32(_Func, metaclass=_WinDLL):
    # oleauto
    VariantChangeType: _Callable[[_Pointer[_struct.VARIANTARG],
                                  _Pointer[_struct.VARIANTARG],
                                  _type.USHORT,
                                  _type.VARTYPE],
                                 _type.HRESULT]
    VariantChangeTypeEx: _Callable[[_Pointer[_struct.VARIANTARG],
                                    _Pointer[_struct.VARIANTARG],
                                    _type.LCID,
                                    _type.USHORT,
                                    _type.VARTYPE],
                                   _type.HRESULT]
    VariantClear: _Callable[[_Pointer[_struct.VARIANTARG]],
                            _type.HRESULT]
    VariantCopy: _Callable[[_Pointer[_struct.VARIANTARG],
                            _Pointer[_struct.VARIANTARG]],
                           _type.HRESULT]
    VariantCopyInd: _Callable[[_Pointer[_struct.VARIANTARG],
                               _Pointer[_struct.VARIANTARG]],
                              _type.HRESULT]
    VariantInit: _Callable[[_Pointer[_struct.VARIANTARG]],
                           _type.c_void]
    # olectl
    OleCreatePictureIndirect: _Callable[[_Pointer[_struct.PICTDESC],
                                         _Pointer[_struct.IID],
                                         _type.BOOL,
                                         _type.LPVOID],
                                        _type.WINOLECTLAPI]
    OleSavePictureFile: _Callable[[_interface.IPictureDisp,
                                   _type.BSTR],
                                  _type.WINOLECTLAPI]


class Shell32(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 703
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 704
    # shellapi
    InitNetworkAddressControl: _Callable[[],
                                         _type.BOOL]
    ShellExecuteA: _Callable[[_Optional[_type.HWND],
                              _Optional[_type.LPCSTR],
                              _type.LPCSTR,
                              _Optional[_type.LPCSTR],
                              _Optional[_type.LPCSTR],
                              _type.INT],
                             _type.HINSTANCE]
    ShellExecuteW: _Callable[[_Optional[_type.HWND],
                              _Optional[_type.LPCWSTR],
                              _type.LPCWSTR,
                              _Optional[_type.LPCWSTR],
                              _Optional[_type.LPWSTR],
                              _type.INT],
                             _type.HINSTANCE]
    ShellExecuteExA: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOA]],
                               _type.BOOL]
    ShellExecuteExW: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOW]],
                               _type.BOOL]
    Shell_NotifyIconA: _Callable[[_type.DWORD,
                                  _Pointer[_struct.NOTIFYICONDATAA]],
                                 _type.BOOL]
    Shell_NotifyIconW: _Callable[[_type.DWORD,
                                  _Pointer[_struct.NOTIFYICONDATAW]],
                                 _type.BOOL]
    Shell_NotifyIconGetRect: _Callable[[_Pointer[_struct.NOTIFYICONIDENTIFIER],
                                        _Pointer[_struct.RECT]],
                                       _type.BOOL]
    SHEmptyRecycleBinA: _Callable[[_Optional[_type.HWND],
                                   _Optional[_type.LPCSTR],
                                   _type.DWORD],
                                  _type.BOOL]
    SHEmptyRecycleBinW: _Callable[[_Optional[_type.HWND],
                                   _Optional[_type.LPCWSTR],
                                   _type.DWORD],
                                  _type.BOOL]
    SHGetDiskFreeSpaceExA: _Callable[[_type.LPCSTR,
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                     _type.BOOL]
    SHGetDiskFreeSpaceExW: _Callable[[_type.LPCWSTR,
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                     _type.BOOL]
    SHGetDriveMedia: _Callable[[_type.PCWSTR,
                                _Pointer[_type.DWORD]],
                               _type.UINT]
    SHGetStockIconInfo: _Callable[[_enum.SHSTOCKICONID,
                                   _type.UINT,
                                   _Pointer[_struct.SHSTOCKICONINFO]],
                                  _type.HRESULT]
    SHQueryUserNotificationState: _Callable[[_Pointer[_enum.QUERY_USER_NOTIFICATION_STATE]],
                                            _type.HRESULT]
    SHQueryRecycleBinA: _Callable[[_Optional[_type.LPCSTR],
                                   _Pointer[_struct.SHQUERYRBINFO]],
                                  _type.HRESULT]
    SHQueryRecycleBinW: _Callable[[_Optional[_type.LPCWSTR],
                                   _Pointer[_struct.SHQUERYRBINFO]],
                                  _type.HRESULT]
    # ShlObj_core
    GetCurrentProcessExplicitAppUserModelID: _Callable[[_Pointer[_type.PWSTR]],
                                                       _type.HRESULT]
    ILClone: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                       _Pointer[_struct.ITEMIDLIST]]
    ILCloneFirst: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                            _Pointer[_struct.ITEMIDLIST]]
    ILCombine: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]],
                          _Optional[_Pointer[_struct.ITEMIDLIST]]],
                         _Pointer[_struct.ITEMIDLIST]]
    ILCreateFromPath: _Callable[[_type.PCWSTR],
                                _Pointer[_struct.ITEMIDLIST]]
    ILCreateFromPathA: _Callable[[_type.PCSTR],
                                 _Pointer[_struct.ITEMIDLIST]]
    ILCreateFromPathW: _Callable[[_type.PCWSTR],
                                 _Pointer[_struct.ITEMIDLIST]]
    ILFindChild: _Callable[[_Pointer[_struct.ITEMIDLIST],
                            _Pointer[_struct.ITEMIDLIST]],
                           _Pointer[_struct.ITEMIDLIST]]
    ILFindLastID: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                            _Pointer[_struct.ITEMIDLIST]]
    ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                      _type.c_void]
    ILGetNext: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                         _Pointer[_struct.ITEMIDLIST]]
    ILGetSize: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                         _type.UINT]
    ILIsEqual: _Callable[[_Pointer[_struct.ITEMIDLIST],
                          _Pointer[_struct.ITEMIDLIST]],
                         _type.BOOL]
    ILIsParent: _Callable[[_Pointer[_struct.ITEMIDLIST],
                           _Pointer[_struct.ITEMIDLIST],
                           _type.BOOL],
                          _type.BOOL]
    ILRemoveLastID: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                              _type.BOOL]
    PathCleanupSpec: _Callable[[_Optional[_type.PCWSTR],
                                _type.PWSTR],
                               _type.c_int]
    SetCurrentProcessExplicitAppUserModelID: _Callable[[_type.PCWSTR],
                                                       _type.HRESULT]
    SHBrowseForFolderA: _Callable[[_Pointer[_struct.BROWSEINFOA]],
                                  _Pointer[_Pointer[_struct.ITEMIDLIST]]]
    SHBrowseForFolderW: _Callable[[_Pointer[_struct.BROWSEINFOW]],
                                  _Pointer[_Pointer[_struct.ITEMIDLIST]]]
    SHChangeNotify: _Callable[[_type.LONG,
                               _type.UINT,
                               _Optional[_type.LPCVOID],
                               _Optional[_type.LPCVOID]],
                              _type.c_void]
    SHGetFolderPathA: _Callable[[_Optional[_type.HWND],
                                 _type.c_int,
                                 _Optional[_type.HANDLE],
                                 _type.DWORD,
                                 _type.LPSTR],
                                _type.HRESULT]
    SHGetFolderPathW: _Callable[[_Optional[_type.HWND],
                                 _type.c_int,
                                 _Optional[_type.HANDLE],
                                 _type.DWORD,
                                 _type.LPWSTR],
                                _type.HRESULT]
    SHOpenFolderAndSelectItems: _Callable[[_Pointer[_struct.ITEMIDLIST],
                                           _type.UINT,
                                           _Optional[_Pointer[_Pointer[_struct.ITEMIDLIST]]],
                                           _type.DWORD],
                                          _type.SHSTDAPI]
    SHOpenWithDialog: _Callable[[_Optional[_type.HWND],
                                 _Pointer[_struct.OPENASINFO]],
                                _type.SHSTDAPI]
    # ShObjIdl_core
    SHCreateItemFromParsingName: _Callable[[_type.PCWSTR,
                                            _Optional[_Pointer[_interface.IBindCtx]],
                                            _Pointer[_struct.IID],
                                            _Pointer[_interface.IShellItem]],
                                           _type.SHSTDAPI]
    SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                                  _Pointer[_Pointer[_struct.ITEMIDLIST]],
                                                  _Pointer[_interface.IShellItemArray]],
                                                 _type.SHSTDAPI]
    SHGetKnownFolderPath: _Callable[[_Pointer[_struct.KNOWNFOLDERID],
                                     _enum.KNOWN_FOLDER_FLAG,
                                     _Optional[_type.HANDLE],
                                     _Pointer[_type.PWSTR]],
                                    _type.HRESULT]
    SHGetPropertyStoreFromParsingName: _Callable[[_type.PCWSTR,
                                                  _Optional[_Pointer[_interface.IBindCtx]],
                                                  _enum.GETPROPERTYSTOREFLAGS,
                                                  _Pointer[_struct.IID],
                                                  _Pointer[_interface.IPropertyStore]],
                                                 _type.SHSTDAPI]


class Setupapi(_Func, metaclass=_WinDLL):
    # SetupAPI
    SetupDiCreateDeviceInterfaceA: _Callable[[_type.HDEVINFO,
                                              _Pointer[_struct.SP_DEVINFO_DATA],
                                              _Pointer[_struct.GUID],
                                              _Optional[_type.PCSTR],
                                              _type.DWORD,
                                              _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DATA]]],
                                             _type.BOOL]
    SetupDiCreateDeviceInterfaceW: _Callable[[_type.HDEVINFO,
                                              _Pointer[_struct.SP_DEVINFO_DATA],
                                              _Pointer[_struct.GUID],
                                              _Optional[_type.PCWSTR],
                                              _type.DWORD,
                                              _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DATA]]],
                                             _type.BOOL]
    SetupDiDestroyDeviceInfoList: _Callable[[_type.HDEVINFO],
                                            _type.BOOL]
    SetupDiEnumDeviceInfo: _Callable[[_type.HDEVINFO,
                                      _type.DWORD,
                                      _Pointer[_struct.SP_DEVINFO_DATA]],
                                     _type.BOOL]
    SetupDiEnumDeviceInterfaces: _Callable[[_type.HDEVINFO,
                                            _Pointer[_struct.SP_DEVINFO_DATA],
                                            _Optional[_Pointer[_struct.GUID]],
                                            _type.DWORD,
                                            _Pointer[_struct.SP_DEVICE_INTERFACE_DATA]],
                                           _type.BOOL]
    SetupDiGetClassDevsA: _Callable[[_Optional[_Pointer[_struct.GUID]],
                                     _Optional[_type.PCSTR],
                                     _Optional[_type.HWND],
                                     _type.DWORD],
                                    _type.HDEVINFO]
    SetupDiGetClassDevsW: _Callable[[_Optional[_Pointer[_struct.GUID]],
                                     _Optional[_type.PCWSTR],
                                     _Optional[_type.HWND],
                                     _type.DWORD],
                                    _type.HDEVINFO]
    SetupDiGetDeviceInterfaceDetailA: _Callable[[_type.HDEVINFO,
                                                 _Pointer[_struct.SP_DEVICE_INTERFACE_DATA],
                                                 _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DETAIL_DATA_A]],
                                                 _type.DWORD,
                                                 _Optional[_Pointer[_type.DWORD]],
                                                 _Optional[_Pointer[_struct.SP_DEVINFO_DATA]]],
                                                _type.BOOL]
    SetupDiGetDeviceInterfaceDetailW: _Callable[[_type.HDEVINFO,
                                                 _Pointer[_struct.SP_DEVICE_INTERFACE_DATA],
                                                 _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DETAIL_DATA_W]],
                                                 _type.DWORD,
                                                 _Optional[_Pointer[_type.DWORD]],
                                                 _Optional[_Pointer[_struct.SP_DEVINFO_DATA]]],
                                                _type.BOOL]
    SetupDiGetDevicePropertyW: _Callable[[_type.HDEVINFO,
                                          _Pointer[_struct.SP_DEVINFO_DATA],
                                          _Pointer[_struct.DEVPROPKEY],
                                          _Pointer[_type.DEVPROPTYPE],
                                          _Optional[_type.PBYTE],
                                          _type.DWORD,
                                          _Optional[_Pointer[_type.DWORD]],
                                          _type.DWORD],
                                         _type.BOOL]
    SetupDiGetDeviceRegistryPropertyA: _Callable[[_type.HDEVINFO,
                                                  _Pointer[_struct.SP_DEVINFO_DATA],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]],
                                                  _Optional[_type.PBYTE],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]]],
                                                 _type.BOOL]
    SetupDiGetDeviceRegistryPropertyW: _Callable[[_type.HDEVINFO,
                                                  _Pointer[_struct.SP_DEVINFO_DATA],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]],
                                                  _Optional[_type.PBYTE],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]]],
                                                 _type.BOOL]


class Shcore(_Func, metaclass=_WinDLL):
    # ShellScalingApi
    GetDpiForMonitor: _Callable[[_type.HMONITOR,
                                 _enum.MONITOR_DPI_TYPE,
                                 _Pointer[_type.UINT],
                                 _Pointer[_type.UINT]],
                                _type.HRESULT]
    GetProcessDpiAwareness: _Callable[[_type.HANDLE,
                                       _Pointer[_enum.PROCESS_DPI_AWARENESS]],
                                      _type.HRESULT]
    SetProcessDpiAwareness: _Callable[[_enum.PROCESS_DPI_AWARENESS],
                                      _type.HRESULT]


class Shdocvw(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]


class Shlwapi(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 269
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 270
    # Shlwapi
    IsInternetESCEnabled: _Callable[[],
                                    _type.BOOL]
    IStream_Copy: _Callable[[_interface.IStream,
                             _interface.IStream,
                             _type.DWORD],
                            _type.HRESULT]
    IStream_Read: _Callable[[_interface.IStream,
                             _type.c_void_p,
                             _type.ULONG],
                            _type.HRESULT]
    IStream_ReadStr: _Callable[[_interface.IStream,
                                _Pointer[_type.PCWSTR]],
                               _type.HRESULT]
    IStream_Reset: _Callable[[_interface.IStream],
                             _type.HRESULT]
    IStream_Size: _Callable[[_interface.IStream,
                             _Pointer[_union.ULARGE_INTEGER]],
                            _type.HRESULT]
    IStream_Write: _Callable[[_interface.IStream,
                              _type.c_void_p,
                              _type.ULONG],
                             _type.HRESULT]
    IStream_WriteStr: _Callable[[_interface.IStream,
                                 _Pointer[_type.PCWSTR]],
                                _type.HRESULT]
    IUnknown_AtomicRelease: _Callable[[_type.c_void_p],
                                      _type.HRESULT]
    IUnknown_GetSite: _Callable[[_interface.IUnknown,
                                 _Pointer[_struct.IID],
                                 _type.c_void_p],
                                _type.HRESULT]
    IUnknown_GetWindow: _Callable[[_interface.IUnknown,
                                   _Pointer[_type.HWND]],
                                  _type.HRESULT]
    IUnknown_QueryService: _Callable[[_interface.IUnknown,
                                      _Pointer[_struct.GUID],
                                      _Pointer[_struct.IID],
                                      _type.c_void_p],
                                     _type.HRESULT]
    IUnknown_Set: _Callable[[_Pointer[_interface.IUnknown],
                             _Optional[_interface.IUnknown]],
                            _type.HRESULT]
    IUnknown_SetSite: _Callable[[_interface.IUnknown,
                                 _Optional[_interface.IUnknown]],
                                _type.HRESULT]
    PathAddBackslashA: _Callable[[_type.LPSTR],
                                 _type.LPSTR]
    PathAddBackslashW: _Callable[[_type.LPWSTR],
                                 _type.LPWSTR]
    PathAddExtensionA: _Callable[[_type.LPSTR,
                                  _Optional[_type.LPCSTR]],
                                 _type.BOOL]
    PathAddExtensionW: _Callable[[_type.LPWSTR,
                                  _Optional[_type.LPCWSTR]],
                                 _type.BOOL]
    PathAppendA: _Callable[[_type.LPSTR,
                            _type.LPCSTR],
                           _type.BOOL]
    PathAppendW: _Callable[[_type.LPWSTR,
                            _type.LPCWSTR],
                           _type.BOOL]
    PathBuildRootA: _Callable[[_type.LPSTR,
                               _type.c_int],
                              _type.LPSTR]
    PathBuildRootW: _Callable[[_type.LPWSTR,
                               _type.c_int],
                              _type.LPWSTR]
    PathCanonicalizeA: _Callable[[_type.LPSTR,
                                  _type.LPCSTR],
                                 _type.BOOL]
    PathCanonicalizeW: _Callable[[_type.LPWSTR,
                                  _type.LPCWSTR],
                                 _type.BOOL]
    PathCombineA: _Callable[[_type.LPSTR,
                             _Optional[_type.LPCSTR],
                             _Optional[_type.LPCSTR]],
                            _type.BOOL]
    PathCombineW: _Callable[[_type.LPWSTR,
                             _Optional[_type.LPCWSTR],
                             _Optional[_type.LPCWSTR]],
                            _type.BOOL]
    PathCompactPathA: _Callable[[_Optional[_type.HDC],
                                 _type.LPSTR,
                                 _type.UINT],
                                _type.BOOL]
    PathCompactPathW: _Callable[[_Optional[_type.HDC],
                                 _type.LPWSTR,
                                 _type.UINT],
                                _type.BOOL]
    PathCompactPathExA: _Callable[[_type.LPSTR,
                                   _type.LPCSTR,
                                   _type.UINT,
                                   _type.DWORD],
                                  _type.BOOL]
    PathCompactPathExW: _Callable[[_type.LPWSTR,
                                   _type.LPCWSTR,
                                   _type.UINT,
                                   _type.DWORD],
                                  _type.BOOL]
    PathCommonPrefixA: _Callable[[_type.LPCSTR,
                                  _type.LPCSTR,
                                  _type.LPSTR],
                                 _type.c_int]
    PathCommonPrefixW: _Callable[[_type.LPCWSTR,
                                  _type.LPCWSTR,
                                  _type.LPWSTR],
                                 _type.c_int]
    PathFileExistsA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathFileExistsW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathFindExtensionA: _Callable[[_type.LPCSTR],
                                  _type.LPSTR]
    PathFindExtensionW: _Callable[[_type.LPCWSTR],
                                  _type.LPWSTR]
    PathFindFileNameA: _Callable[[_type.LPCSTR],
                                 _type.LPSTR]
    PathFindFileNameW: _Callable[[_type.LPCWSTR],
                                 _type.LPWSTR]
    PathFindNextComponentA: _Callable[[_type.LPCSTR],
                                      _type.LPSTR]
    PathFindNextComponentW: _Callable[[_type.LPCWSTR],
                                      _type.LPWSTR]
    PathFindOnPathA: _Callable[[_type.LPSTR,
                                _Optional[_Pointer[_type.PCSTR]]],
                               _type.BOOL]
    PathFindOnPathW: _Callable[[_type.LPWSTR,
                                _Optional[_Pointer[_type.PCWSTR]]],
                               _type.BOOL]
    PathGetArgsA: _Callable[[_type.LPCSTR],
                            _type.LPSTR]
    PathGetArgsW: _Callable[[_type.LPCWSTR],
                            _type.LPWSTR]
    PathGetCharTypeA: _Callable[[_type.UCHAR],
                                _type.UINT]
    PathGetCharTypeW: _Callable[[_type.WCHAR],
                                _type.UINT]
    PathGetDriveNumberA: _Callable[[_type.LPCSTR],
                                   _type.c_int]
    PathGetDriveNumberW: _Callable[[_type.LPCWSTR],
                                   _type.c_int]
    PathIsContentTypeA: _Callable[[_type.LPCSTR,
                                   _type.LPCSTR],
                                  _type.BOOL]
    PathIsContentTypeW: _Callable[[_type.LPCWSTR,
                                   _type.LPCWSTR],
                                  _type.BOOL]
    PathIsDirectoryA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    PathIsDirectoryW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    PathIsDirectoryEmptyA: _Callable[[_type.LPCSTR],
                                     _type.BOOL]
    PathIsDirectoryEmptyW: _Callable[[_type.LPCWSTR],
                                     _type.BOOL]
    PathIsFileSpecA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathIsFileSpecW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathIsLFNFileSpecA: _Callable[[_type.LPCSTR],
                                  _type.BOOL]
    PathIsLFNFileSpecW: _Callable[[_type.LPCWSTR],
                                  _type.BOOL]
    PathIsNetworkPathA: _Callable[[_type.LPCSTR],
                                  _type.BOOL]
    PathIsNetworkPathW: _Callable[[_type.LPCWSTR],
                                  _type.BOOL]
    PathIsPrefixA: _Callable[[_type.LPCSTR,
                              _type.LPCSTR],
                             _type.BOOL]
    PathIsPrefixW: _Callable[[_type.LPCWSTR,
                              _type.LPCWSTR],
                             _type.BOOL]
    PathIsRelativeA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathIsRelativeW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathIsRootA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    PathIsRootW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
    PathIsSameRootA: _Callable[[_type.LPCSTR,
                                _type.LPCSTR],
                               _type.BOOL]
    PathIsSameRootW: _Callable[[_type.LPCWSTR,
                                _type.LPCWSTR],
                               _type.BOOL]
    PathIsSystemFolderA: _Callable[[_type.LPCSTR,
                                    _type.DWORD],
                                   _type.BOOL]
    PathIsSystemFolderW: _Callable[[_type.LPCWSTR,
                                    _type.DWORD],
                                   _type.BOOL]
    PathIsUNCA: _Callable[[_type.LPCSTR],
                          _type.BOOL]
    PathIsUNCW: _Callable[[_type.LPCWSTR],
                          _type.BOOL]
    PathIsUNCServerA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    PathIsUNCServerW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    PathIsUNCServerShareA: _Callable[[_type.LPCSTR],
                                     _type.BOOL]
    PathIsUNCServerShareW: _Callable[[_type.LPCWSTR],
                                     _type.BOOL]
    PathIsURLA: _Callable[[_type.LPCSTR],
                          _type.BOOL]
    PathIsURLW: _Callable[[_type.LPCWSTR],
                          _type.BOOL]
    PathMakeSystemFolderA: _Callable[[_type.LPCSTR],
                                     _type.BOOL]
    PathMakeSystemFolderW: _Callable[[_type.LPCWSTR],
                                     _type.BOOL]
    PathRemoveFileSpecA: _Callable[[_type.LPSTR],
                                   _type.BOOL]
    PathRemoveFileSpecW: _Callable[[_type.LPWSTR],
                                   _type.BOOL]
    PathRenameExtensionA: _Callable[[_type.LPSTR,
                                     _type.LPCSTR],
                                    _type.BOOL]
    PathRenameExtensionW: _Callable[[_type.LPWSTR,
                                     _type.LPCWSTR],
                                    _type.BOOL]
    PathSearchAndQualifyA: _Callable[[_type.LPCSTR,
                                      _type.LPSTR,
                                      _type.UINT],
                                     _type.BOOL]
    PathSearchAndQualifyW: _Callable[[_type.LPCWSTR,
                                      _type.LPWSTR,
                                      _type.UINT],
                                     _type.BOOL]
    PathSkipRootA: _Callable[[_type.LPCSTR],
                             _type.LPSTR]
    PathSkipRootW: _Callable[[_type.LPCWSTR],
                             _type.LPWSTR]
    PathStripPathA: _Callable[[_type.LPSTR],
                              _type.c_void]
    PathStripPathW: _Callable[[_type.LPWSTR],
                              _type.c_void]
    PathStripToRootA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    PathStripToRootW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    PathUndecorateA: _Callable[[_type.LPSTR],
                               _type.c_void]
    PathUndecorateW: _Callable[[_type.LPWSTR],
                               _type.c_void]
    PathUnExpandEnvStringsA: _Callable[[_type.LPCSTR,
                                        _type.LPSTR,
                                        _type.UINT],
                                       _type.BOOL]
    PathUnExpandEnvStringsW: _Callable[[_type.LPCWSTR,
                                        _type.LPWSTR,
                                        _type.UINT],
                                       _type.BOOL]
    PathUnmakeSystemFolderA: _Callable[[_type.LPCSTR],
                                       _type.BOOL]
    PathUnmakeSystemFolderW: _Callable[[_type.LPCWSTR],
                                       _type.BOOL]
    PathUnquoteSpacesA: _Callable[[_type.LPCSTR],
                                  _type.BOOL]
    PathUnquoteSpacesW: _Callable[[_type.LPCWSTR],
                                  _type.BOOL]
    SHCreateMemStream: _Callable[[_Pointer[_type.BYTE],
                                  _type.UINT],
                                 _interface.IStream]
    SHCreateStreamOnFileA: _Callable[[_type.LPCSTR,
                                      _type.DWORD,
                                      _type.DWORD,
                                      _Pointer[_interface.IStream]],
                                     _type.HRESULT]
    SHCreateStreamOnFileW: _Callable[[_type.LPCWSTR,
                                      _type.DWORD,
                                      _type.DWORD,
                                      _Pointer[_interface.IStream]],
                                     _type.HRESULT]
    SHCreateStreamOnFileEx: _Callable[[_type.LPCWSTR,
                                       _type.DWORD,
                                       _type.DWORD,
                                       _type.BOOL,
                                       _Optional[_interface.IStream],
                                       _Pointer[_interface.IStream]],
                                      _type.HRESULT]
    SHOpenRegStreamA: _Callable[[_type.HKEY,
                                 _Optional[_type.LPCSTR],
                                 _Optional[_type.LPCSTR],
                                 _type.DWORD],
                                _interface.IStream]
    SHOpenRegStreamW: _Callable[[_type.HKEY,
                                 _Optional[_type.LPCWSTR],
                                 _Optional[_type.LPCWSTR],
                                 _type.DWORD],
                                _interface.IStream]
    SHOpenRegStream2A: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCSTR],
                                  _Optional[_type.LPCSTR],
                                  _type.DWORD],
                                 _interface.IStream]
    SHOpenRegStream2W: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCWSTR],
                                  _Optional[_type.LPCWSTR],
                                  _type.DWORD],
                                 _interface.IStream]
    UrlGetLocationA: _Callable[[_type.PCSTR],
                               _type.LPCSTR]
    UrlGetLocationW: _Callable[[_type.PCWSTR],
                               _type.LPCWSTR]
    UrlIsA: _Callable[[_type.PCSTR,
                       _enum.URLIS],
                      _type.BOOL]
    UrlIsW: _Callable[[_type.PCWSTR,
                       _enum.URLIS],
                      _type.BOOL]
    UrlIsOpaqueA: _Callable[[_type.PCSTR],
                            _type.BOOL]
    UrlIsOpaqueW: _Callable[[_type.PCWSTR],
                            _type.BOOL]
    UrlIsNoHistoryA: _Callable[[_type.PCSTR],
                               _type.BOOL]
    UrlIsNoHistoryW: _Callable[[_type.PCWSTR],
                               _type.BOOL]


class User32(_Func, metaclass=_WinDLL):
    # WinUser
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
    CheckMenuRadioItem: _Callable[[_type.HMENU,
                                   _type.UINT,
                                   _type.UINT,
                                   _type.UINT,
                                   _type.UINT],
                                  _type.BOOL]
    CheckRadioButton: _Callable[[_type.HWND,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.c_int],
                                _type.BOOL]
    ClientToScreen: _Callable[[_type.HWND,
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
    DestroyCursor: _Callable[[_type.HCURSOR],
                             _type.BOOL]
    DestroyIcon: _Callable[[_type.HICON],
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
    EnumThreadWindows: _Callable[[_type.DWORD,
                                  _type.WNDENUMPROC,
                                  _type.LPARAM],
                                 _type.BOOL]
    EnumWindows: _Callable[[_type.WNDENUMPROC,
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
    GetClassNameA: _Callable[[_type.HWND,
                              _type.LPSTR,
                              _type.c_int],
                             _type.c_int]
    GetClassNameW: _Callable[[_type.HWND,
                              _type.LPWSTR,
                              _type.c_int],
                             _type.c_int]
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
    GetLastActivePopup: _Callable[[_type.HWND],
                                  _type.HWND]
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
    GetTopWindow: _Callable[[_Optional[_type.HWND]],
                            _type.HWND]
    GetUnpredictedMessagePos: _Callable[[],
                                        _type.DWORD]
    GetWindow: _Callable[[_type.HWND,
                          _type.UINT],
                         _type.HWND]
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
    GetWindowTextA: _Callable[[_type.HWND,
                               _type.LPSTR,
                               _type.c_int],
                              _type.c_int]
    GetWindowTextW: _Callable[[_type.HWND,
                               _type.LPWSTR,
                               _type.c_int],
                              _type.c_int]
    GetWindowThreadProcessId: _Callable[[_type.HWND,
                                         _Optional[_Pointer[_type.DWORD]]],
                                        _type.DWORD]
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
    IsChild: _Callable[[_type.HWND,
                        _type.HWND],
                       _type.BOOL]
    IsDlgButtonChecked: _Callable[[_type.HWND,
                                   _type.c_int],
                                  _type.UINT]
    IsGUIThread: _Callable[[_type.BOOL],
                           _type.BOOL]
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
    LoadCursorA: _Callable[[_Optional[_type.HINSTANCE],
                            _type.LPCSTR],
                           _type.HCURSOR]
    LoadCursorW: _Callable[[_Optional[_type.HINSTANCE],
                            _type.LPCWSTR],
                           _type.HCURSOR]
    LoadCursorFromFileA: _Callable[[_type.LPCSTR],
                                   _type.HCURSOR]
    LoadCursorFromFileW: _Callable[[_type.LPCWSTR],
                                   _type.HCURSOR]
    LoadIconA: _Callable[[_Optional[_type.HINSTANCE],
                          _type.UINT],
                         _type.HICON]
    LoadIconW: _Callable[[_Optional[_type.HINSTANCE],
                          _type.LPCWSTR],
                         _type.HICON]
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
    MessageBoxA: _Callable[[_Optional[_type.HWND],
                            _Optional[_type.LPCSTR],
                            _Optional[_type.LPCSTR],
                            _type.UINT],
                           _type.c_int]
    MessageBoxW: _Callable[[_Optional[_type.HWND],
                            _Optional[_type.LPCWSTR],
                            _Optional[_type.LPCWSTR],
                            _type.UINT],
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
    MonitorFromPoint: _Callable[[_struct.POINT,
                                 _type.DWORD],
                                _type.HMONITOR]
    MonitorFromRect: _Callable[[_Pointer[_struct.RECT],
                                _type.DWORD],
                               _type.HMONITOR]
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
                                    _Optional[_type.PDWORD_PTR]],
                                   _type.LRESULT]
    SendMessageTimeoutW: _Callable[[_type.HWND,
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM,
                                    _type.UINT,
                                    _type.UINT,
                                    _Optional[_type.PDWORD_PTR]],
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
    SetWindowsHookA: _Callable[[_type.c_int,
                                _type.HOOKPROC],
                               _type.HHOOK]
    SetWindowsHookW: _Callable[[_type.c_int,
                                _type.HOOKPROC],
                               _type.HHOOK]
    SetWindowsHookExA: _Callable[[_type.c_int,
                                  _type.HOOKPROC,
                                  _type.HINSTANCE,
                                  _type.DWORD],
                                 _type.HHOOK]
    SetWindowsHookExW: _Callable[[_type.c_int,
                                  _type.HOOKPROC,
                                  _type.HINSTANCE,
                                  _type.DWORD],
                                 _type.HHOOK]
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
    UnhookWindowsHook: _Callable[[_type.c_int,
                                  _type.HOOKPROC],
                                 _type.BOOL]
    UnhookWindowsHookEx: _Callable[[_type.HHOOK],
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


class UxTheme(_Func, metaclass=_WinDLL):
    # Uxtheme
    BeginPanningFeedback: _Callable[[_type.HWND],
                                    _type.BOOL]
    BufferedPaintInit: _Callable[[],
                                 _type.HRESULT]
    BufferedPaintUnInit: _Callable[[],
                                   _type.HRESULT]
    CloseThemeData: _Callable[[_type.HTHEME],
                              _type.HRESULT]
    DrawThemeBackground: _Callable[[_type.HTHEME,
                                    _type.HDC,
                                    _type.c_int,
                                    _type.c_int,
                                    _Pointer[_struct.RECT],
                                    _Optional[_Pointer[_struct.RECT]]],
                                   _type.HRESULT]
    DrawThemeBackgroundEx: _Callable[[_type.HTHEME,
                                      _type.HDC,
                                      _type.c_int,
                                      _type.c_int,
                                      _Pointer[_struct.RECT],
                                      _Optional[_Pointer[_struct.DTBGOPTS]]],
                                     _type.HRESULT]
    DrawThemeEdge: _Callable[[_type.HTHEME,
                              _type.HDC,
                              _type.c_int,
                              _type.c_int,
                              _Pointer[_struct.RECT],
                              _type.UINT,
                              _type.UINT,
                              _Optional[_Pointer[_struct.RECT]]],
                             _type.HRESULT]
    DrawThemeParentBackground: _Callable[[_type.HWND,
                                          _type.HDC,
                                          _Optional[_Pointer[_struct.RECT]]],
                                         _type.HRESULT]
    DrawThemeParentBackgroundEx: _Callable[[_type.HWND,
                                            _type.HDC,
                                            _type.DWORD,
                                            _Optional[_Pointer[_struct.RECT]]],
                                           _type.HRESULT]
    DrawThemeText: _Callable[[_type.HTHEME,
                              _type.HDC,
                              _type.c_int,
                              _type.c_int,
                              _type.LPCWSTR,
                              _type.c_int,
                              _type.DWORD,
                              _type.DWORD,
                              _Pointer[_struct.RECT]],
                             _type.HRESULT]
    EnableTheming: _Callable[[_type.BOOL],
                             _type.HRESULT]
    EnableThemeDialogTexture: _Callable[[_type.HWND,
                                         _type.DWORD],
                                        _type.HRESULT]
    EndPanningFeedback: _Callable[[_type.HWND,
                                   _type.BOOL],
                                  _type.BOOL]
    GetCurrentThemeName: _Callable[[_type.LPWSTR,
                                    _type.c_int,
                                    _Optional[_type.LPWSTR],
                                    _type.c_int,
                                    _Optional[_type.LPWSTR],
                                    _type.c_int],
                                   _type.HRESULT]
    GetThemeBackgroundExtent: _Callable[[_type.HTHEME,
                                         _Optional[_type.HDC],
                                         _type.c_int,
                                         _type.c_int,
                                         _Pointer[_struct.RECT],
                                         _Pointer[_struct.RECT]],
                                        _type.HRESULT]
    GetThemeBackgroundContentRect: _Callable[[_type.HTHEME,
                                              _Optional[_type.HDC],
                                              _type.c_int,
                                              _type.c_int,
                                              _Pointer[_struct.RECT],
                                              _Pointer[_struct.RECT]],
                                             _type.HRESULT]
    GetThemeBackgroundRegion: _Callable[[_type.HTHEME,
                                         _Optional[_type.HDC],
                                         _type.c_int,
                                         _type.c_int,
                                         _Pointer[_struct.RECT],
                                         _Pointer[_type.HRGN]],
                                        _type.HRESULT]
    GetThemeBool: _Callable[[_type.HTHEME,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _Pointer[_type.BOOL]],
                            _type.HRESULT]
    GetThemeColor: _Callable[[_type.HTHEME,
                              _type.c_int,
                              _type.c_int,
                              _type.c_int,
                              _Pointer[_type.COLORREF]],
                             _type.HRESULT]
    GetThemeEnumValue: _Callable[[_type.HTHEME,
                                  _type.c_int,
                                  _type.c_int,
                                  _type.c_int,
                                  _Pointer[_type.c_int]],
                                 _type.HRESULT]
    GetThemeDocumentationProperty: _Callable[[_type.LPCWSTR,
                                              _type.LPCWSTR,
                                              _type.LPWSTR,
                                              _type.c_int],
                                             _type.HRESULT]
    GetThemeFilename: _Callable[[_type.HTHEME,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.LPWSTR,
                                 _type.c_int],
                                _type.HRESULT]
    GetThemeFont: _Callable[[_type.HTHEME,
                             _Optional[_type.HDC],
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _Pointer[_struct.LOGFONTW]],
                            _type.HRESULT]
    GetThemeInt: _Callable[[_type.HTHEME,
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _Pointer[_type.c_int]],
                           _type.HRESULT]
    GetThemeIntList: _Callable[[_type.HTHEME,
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _Pointer[_struct.INTLIST]],
                               _type.HRESULT]
    GetThemeMargins: _Callable[[_type.HTHEME,
                                _Optional[_type.HDC],
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _Optional[_Pointer[_struct.RECT]],
                                _Pointer[_struct.MARGINS]],
                               _type.HRESULT]
    GetThemeMetric: _Callable[[_type.HTHEME,
                               _Optional[_type.HDC],
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _Pointer[_type.c_int]],
                              _type.HRESULT]
    GetThemePartSize: _Callable[[_type.HTHEME,
                                 _Optional[_type.HDC],
                                 _type.c_int,
                                 _type.c_int,
                                 _Optional[_Pointer[_struct.RECT]],
                                 _enum.THEMESIZE,
                                 _Pointer[_struct.SIZE]],
                                _type.HRESULT]
    GetThemePosition: _Callable[[_type.HTHEME,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.c_int,
                                 _Pointer[_struct.POINT]],
                                _type.HRESULT]
    GetThemeAppProperties: _Callable[[],
                                     _type.DWORD]
    GetThemePropertyOrigin: _Callable[[_type.HTHEME,
                                       _type.c_int,
                                       _type.c_int,
                                       _type.c_int,
                                       _Pointer[_enum.PROPERTYORIGIN]],
                                      _type.HRESULT]
    GetThemeRect: _Callable[[_type.HTHEME,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _Pointer[_struct.RECT]],
                            _type.HRESULT]
    GetThemeString: _Callable[[_type.HTHEME,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.LPWSTR,
                               _type.c_int],
                              _type.HRESULT]
    GetThemeSysBool: _Callable[[_Optional[_type.HTHEME],
                                _type.c_int],
                               _type.BOOL]
    GetThemeSysColor: _Callable[[_Optional[_type.HTHEME],
                                 _type.c_int],
                                _type.COLORREF]
    GetThemeSysColorBrush: _Callable[[_Optional[_type.HTHEME],
                                      _type.c_int],
                                     _type.HBRUSH]
    GetThemeSysFont: _Callable[[_Optional[_type.HTHEME],
                                _type.c_int,
                                _Pointer[_struct.LOGFONTW]],
                               _type.HRESULT]
    GetThemeSysInt: _Callable[[_type.HTHEME,
                               _type.c_int,
                               _Pointer[_type.c_int]],
                              _type.HRESULT]
    GetThemeSysSize: _Callable[[_Optional[_type.HTHEME],
                                _type.c_int],
                               _type.c_int]
    GetThemeSysString: _Callable[[_type.HTHEME,
                                  _type.c_int,
                                  _type.LPWSTR,
                                  _type.c_int],
                                 _type.HRESULT]
    GetThemeTextExtent: _Callable[[_type.HTHEME,
                                   _type.HDC,
                                   _type.c_int,
                                   _type.c_int,
                                   _type.LPCWSTR,
                                   _type.c_int,
                                   _type.DWORD,
                                   _Optional[_Pointer[_struct.RECT]],
                                   _Pointer[_struct.RECT]],
                                  _type.HRESULT]
    GetThemeTextMetrics: _Callable[[_type.HTHEME,
                                    _type.HDC,
                                    _type.c_int,
                                    _type.c_int,
                                    _struct.TEXTMETRICW],
                                   _type.HRESULT]
    HitTestThemeBackground: _Callable[[_type.HTHEME,
                                       _Optional[_type.HDC],
                                       _type.c_int,
                                       _type.c_int,
                                       _type.DWORD,
                                       _Pointer[_struct.RECT],
                                       _Optional[_type.HRGN],
                                       _struct.POINT,
                                       _Pointer[_type.WORD]],
                                      _type.HRESULT]
    IsAppThemed: _Callable[[],
                           _type.BOOL]
    IsCompositionActive: _Callable[[],
                                   _type.BOOL]
    IsThemeActive: _Callable[[],
                             _type.BOOL]
    IsThemeBackgroundPartiallyTransparent: _Callable[[_type.HTHEME,
                                                      _type.c_int,
                                                      _type.c_int],
                                                     _type.BOOL]
    IsThemeDialogTextureEnabled: _Callable[[_type.HWND],
                                           _type.BOOL]
    IsThemePartDefined: _Callable[[_type.HTHEME,
                                   _type.c_int,
                                   _type.c_int],
                                  _type.BOOL]
    OpenThemeData: _Callable[[_Optional[_type.HWND],
                              _type.LPCWSTR],
                             _type.HTHEME]
    OpenThemeDataEx: _Callable[[_Optional[_type.HWND],
                                _type.LPCWSTR,
                                _type.DWORD],
                               _type.HTHEME]
    OpenThemeDataForDpi: _Callable[[_Optional[_type.HWND],
                                    _type.LPCWSTR,
                                    _type.UINT],
                                   _type.HTHEME]
    GetWindowTheme: _Callable[[_type.HWND],
                              _type.HTHEME]
    SetWindowThemeAttribute: _Callable[[_type.HWND,
                                        _enum.WINDOWTHEMEATTRIBUTETYPE,
                                        _type.PVOID,
                                        _type.DWORD],
                                       _type.HRESULT]
    SetThemeAppProperties: _Callable[[_type.DWORD],
                                     _type.c_void]
    SetWindowTheme: _Callable[[_type.HWND,
                               _Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR]],
                              _type.HRESULT]
    UpdatePanningFeedback: _Callable[[_type.HWND,
                                      _type.LONG,
                                      _type.LONG,
                                      _type.BOOL],
                                     _type.BOOL]


class Microsoft:
    class UI:
        class Xaml(_Func, metaclass=_WinDLL):
            DllGetActivationFactory: _Callable[[_type.HSTRING,
                                                _Pointer[_interface.IActivationFactory]],
                                               _type.HRESULT]

    class WindowsAppRuntime:
        class Bootstrap(_Func, metaclass=_WinDLL):
            MddBootstrapInitialize: _Callable[[_type.UINT32,
                                               _type.PCWSTR,
                                               _struct.PACKAGE_VERSION],
                                              _type.HRESULT]
            MddBootstrapShutdown: _Callable[[],
                                            _type.c_void]
