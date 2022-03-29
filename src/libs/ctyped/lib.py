from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing
from typing import Callable as _Callable, Optional as _Optional

from . import com as _com, enum as _enum, struct as _struct, type as _type
from ._utils import _get_func_doc, _format_annotations, _not_internal, _Pointer, _resolve_type


class _CDLL(type):
    def __getattr__(self, name: str):
        if _not_internal(name):
            if self._funcs is None:
                self._funcs = {}
                for var in _typing.get_type_hints(self):
                    try:
                        self._funcs[var] = vars(self)[var]
                    except KeyError:
                        self._funcs[var] = var
                    else:
                        delattr(self, var)
            func = None
            while func is None:
                try:
                    func = self._lib[self._funcs[name]]
                except KeyError:
                    raise AttributeError(f"lib '{self.__name__}' has no function '{name}'") from None
                except TypeError:
                    try:
                        self._lib = _ctypes.pythonapi if self is Python else getattr(
                            getattr(_ctypes, type(self).__name__[1:].lower()), self.__name__)
                    except FileNotFoundError as e:
                        raise e from None
            annot = _format_annotations(self.__annotations__[name])
            func.restype, *func.argtypes = _resolve_type(_typing.get_type_hints(self, globals())[name])
            if self._errcheck is not None:
                func.errcheck = self._errcheck
            func.__name__ = name
            func.__doc__ = _get_func_doc(name, func.restype, func.argtypes, annot)
            setattr(self, name, func)
            return func
        return super().__getattribute__(name)


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


class _PyFunc(_Func, metaclass=_PyDLL):
    pass


class _WinFunc(_Func, metaclass=_WinDLL):
    pass


class Python(_PyFunc):
    # pylifecycle
    Py_Initialize: _Callable[[],
                             _type.c_void_p]
    Py_InitializeEx: _Callable[[_type.c_int],
                               _type.c_void_p]
    Py_IsInitialized: _Callable[[],
                                _type.c_int]
    Py_Finalize: _Callable[[],
                           _type.c_void_p]
    Py_FinalizeEx: _Callable[[],
                             _type.c_int]


class Cfgmgr32(_WinFunc):
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


class Combase(_WinFunc):
    # roapi
    RoActivateInstance: _Callable[[_type.HSTRING,
                                   _Pointer[_com.IInspectable]],
                                  _type.HRESULT]
    RoGetActivationFactory: _Callable[[_type.HSTRING,
                                       _Pointer[_struct.IID],
                                       _Pointer[_com.IActivationFactory]],
                                      _type.HRESULT]
    RoInitialize: _Callable[[_enum.RO_INIT_TYPE],
                            _type.HRESULT]
    RoUninitialize: _Callable[[],
                              _type.c_void_p]
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


class Comctl32(_WinFunc):
    # CommCtrl
    InitCommonControls: _Callable[[],
                                  _type.c_void_p]
    InitCommonControlsEx: _Callable[[_Pointer[_struct.INITCOMMONCONTROLSEX]],
                                    _type.BOOL]


class Comdlg32(_WinFunc):
    # commdlg
    ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]],
                            _type.BOOL]
    ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]],
                            _type.BOOL]


class Gdi32(_WinFunc):
    # wingdi
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
    CreateSolidBrush: _Callable[[_type.COLORREF],
                                _type.HBRUSH]
    DeleteDC: _Callable[[_type.HDC],
                        _type.BOOL]
    DeleteMetaFile: _Callable[[_type.HMETAFILE],
                              _type.BOOL]
    DeleteObject: _Callable[[_type.HGDIOBJ],
                            _type.BOOL]
    GetBitmapDimensionEx: _Callable[[_type.HBITMAP,
                                     _Pointer[_struct.SIZE]],
                                    _type.BOOL]
    GetClipBox: _Callable[[_type.HDC,
                           _Pointer[_struct.RECT]],
                          _type.c_int]
    GetDIBits: _Callable[[_type.HDC,
                          _type.HBITMAP,
                          _type.UINT,
                          _type.UINT,
                          _Optional[_type.LPVOID],
                          _Pointer[_struct.BITMAPINFO],
                          _type.UINT],
                         _type.c_int]
    GetObjectA: _Callable[[_type.HANDLE,
                           _type.c_int,
                           _type.LPVOID],
                          _type.c_int]
    GetObjectW: _Callable[[_type.HANDLE,
                           _type.c_int,
                           _type.LPVOID],
                          _type.c_int]
    GetStockObject: _Callable[[_type.c_int],
                              _type.HGDIOBJ]
    SelectObject: _Callable[[_type.HDC,
                             _type.HGDIOBJ],
                            _type.HGDIOBJ]
    SetBkColor: _Callable[[_type.HDC,
                           _type.COLORREF],
                          _type.COLORREF]
    SetDCBrushColor: _Callable[[_type.HDC,
                                _type.COLORREF],
                               _type.COLORREF]
    SetDCPenColor: _Callable[[_type.HDC,
                              _type.COLORREF],
                             _type.COLORREF]
    SetStretchBltMode: _Callable[[_type.HDC,
                                  _type.c_int],
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


class GdiPlus(_WinFunc):
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
    GdipCreateBitmapFromFile: _Callable[[_type.LPWSTR,
                                         _Pointer[_type.GpBitmap]],
                                        _enum.GpStatus]
    GdipCreateBitmapFromGraphics: _Callable[[_type.INT,
                                             _type.INT,
                                             _type.GpGraphics,
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
    GdipCreateBitmapFromScan0: _Callable[[_type.INT,
                                          _type.INT,
                                          _type.INT,
                                          _type.PixelFormat,
                                          _Optional[_Pointer[_type.BYTE]],
                                          _Pointer[_type.GpBitmap]],
                                         _enum.GpStatus]
    GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap,
                                          _Pointer[_type.HICON]],
                                         _enum.GpStatus]
    GdipCreateImageAttributes: _Callable[[_Pointer[_type.GpImageAttributes]],
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
    GdipGetImageWidth: _Callable[[_type.GpImage,
                                  _Pointer[_type.UINT]],
                                 _enum.GpStatus]
    GdipGetImageGraphicsContext: _Callable[[_type.GpImage,
                                            _Pointer[_type.GpGraphics]],
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
    GdipGetSolidFillColor: _Callable[[_type.GpSolidFill,
                                      _Pointer[_type.ARGB]],
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
    GdipSetSolidFillColor: _Callable[[_type.GpSolidFill,
                                      _type.ARGB],
                                     _enum.GpStatus]
    GdipReleaseDC: _Callable[[_type.GpGraphics,
                              _type.HDC],
                             _enum.GpStatus]
    GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                               _type.VOID]
    GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],
                               _Pointer[_struct.GdiplusStartupInput],
                               _Optional[_Pointer[_struct.GdiplusStartupInput]]],
                              _enum.Status]


class Kernel32(_WinFunc):
    # errhandlingapi
    GetLastError: _Callable[[],
                            _type.DWORD]
    SetLastError: _Callable[[_type.DWORD],
                            _type.c_void_p]
    # fileapi
    DeleteFileA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    DeleteFileW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
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
    # handleapi
    CloseHandle: _Callable[[_type.HANDLE],
                           _type.BOOL]
    # libloaderapi
    GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                                _type.HMODULE]
    GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                                _type.HMODULE]
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
    # synchapi
    Sleep: _Callable[[_type.DWORD],
                     _type.VOID]
    # WinBase
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
    GlobalAlloc: _Callable[[_type.UINT,
                            _type.SIZE_T],
                           _type.HGLOBAL]
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


class MSCorEE(_WinFunc):
    # cor
    CoEEShutDownCOM: _Callable[[],
                               _type.c_void_p]
    CoInitializeCor: _Callable[[_type.DWORD],
                               _type.HRESULT]
    CoInitializeEE: _Callable[[_enum.COINITIEE],
                              _type.HRESULT]
    CoUninitializeCor: _Callable[[],
                                 _type.c_void_p]
    CoUninitializeEE: _Callable[[_type.BOOL],
                                _type.c_void_p]
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


class Msimg32(_WinFunc):
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
class msvcrt(_WinFunc):
    # corecrt_malloc
    free: _Callable[[_type.c_void_p],
                    _type.c_void_p]
    malloc: _Callable[[_type.c_void_p],
                      _type.c_size_t]
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
class ntdll(_WinFunc):
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


class Ole32(_WinFunc):
    # combaseapi
    CLSIDFromString: _Callable[[_type.LPCOLESTR,
                                _Pointer[_struct.CLSID]],
                               _type.HRESULT]
    CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],
                            _type.HRESULT]
    CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],
                                 _Optional[_Pointer[_com.IUnknown]],
                                 _type.DWORD,
                                 _Pointer[_struct.IID],
                                 _type.LPVOID],
                                _type.HRESULT]
    CoInitializeEx: _Callable[[_Optional[_type.LPVOID],
                               _type.DWORD],
                              _type.HRESULT]
    CoTaskMemFree: _Callable[[_type.LPVOID],
                             _type.c_void_p]
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


class Oleacc(_WinFunc):
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


class OleAut32(_WinFunc):
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
                           _type.c_void_p]
    # olectl
    OleCreatePictureIndirect: _Callable[[_Pointer[_struct.PICTDESC],
                                         _Pointer[_struct.IID],
                                         _type.BOOL,
                                         _type.LPVOID],
                                        _type.WINOLECTLAPI]
    OleSavePictureFile: _Callable[[_com.IPictureDisp,
                                   _type.BSTR],
                                  _type.WINOLECTLAPI]


class Shell32(_WinFunc):
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 703
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 704
    # shellapi
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
    # ShlObj_core
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
                      _type.c_void_p]
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
    SHBrowseForFolderA: _Callable[[_Pointer[_struct.BROWSEINFOA]],
                                  _Pointer[_Pointer[_struct.ITEMIDLIST]]]
    SHBrowseForFolderW: _Callable[[_Pointer[_struct.BROWSEINFOW]],
                                  _Pointer[_Pointer[_struct.ITEMIDLIST]]]
    SHChangeNotify: _Callable[[_type.LONG,
                               _type.UINT,
                               _Optional[_type.LPCVOID],
                               _Optional[_type.LPCVOID]],
                              _type.c_void_p]
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
                                            _Optional[_Pointer[_com.IBindCtx]],
                                            _Pointer[_struct.IID],
                                            _Pointer[_com.IShellItem]],
                                           _type.SHSTDAPI]
    SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                                  _Pointer[_Pointer[_struct.ITEMIDLIST]],
                                                  _Pointer[_com.IShellItemArray]],
                                                 _type.SHSTDAPI]
    SHGetKnownFolderPath: _Callable[[_Pointer[_struct.KNOWNFOLDERID],
                                     _enum.KNOWN_FOLDER_FLAG,
                                     _Optional[_type.HANDLE],
                                     _Pointer[_type.PWSTR]],
                                    _type.HRESULT]
    SHGetPropertyStoreFromParsingName: _Callable[[_type.PCWSTR,
                                                  _Optional[_Pointer[_com.IBindCtx]],
                                                  _enum.GETPROPERTYSTOREFLAGS,
                                                  _Pointer[_struct.IID],
                                                  _Pointer[_com.IPropertyStore]],
                                                 _type.SHSTDAPI]


class Setupapi(_WinFunc):
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


class Shcore(_WinFunc):
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


class Shlwapi(_WinFunc):
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 269
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 270
    # Shlwapi
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
                              _type.c_void_p]
    PathStripPathW: _Callable[[_type.LPWSTR],
                              _type.c_void_p]
    PathStripToRootA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    PathStripToRootW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    PathUndecorateA: _Callable[[_type.LPSTR],
                               _type.c_void_p]
    PathUndecorateA: _Callable[[_type.LPWSTR],
                               _type.c_void_p]
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


class User32(_WinFunc):
    # WinUser
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
    BeginPaint: _Callable[[_type.HWND,
                           _Pointer[_struct.PAINTSTRUCT]],
                          _type.HDC]
    BlockInput: _Callable[[_type.BOOL],
                          _type.BOOL]
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
    EndDialog: _Callable[[_type.HWND,
                          _type.INT_PTR],
                         _type.BOOL]
    EndPaint: _Callable[[_type.HWND,
                         _Pointer[_struct.PAINTSTRUCT]],
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
    GetCursorPos: _Callable[[_Pointer[_struct.POINT]],
                            _type.BOOL]
    GetDC: _Callable[[_Optional[_type.HWND]],
                     _type.HDC]
    GetDCEx: _Callable[[_Optional[_type.HWND],
                        _type.HRGN,
                        _type.DWORD],
                       _type.HDC]
    GetDialogBaseUnits: _Callable[[],
                                  _type.c_long]
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
    GetDpiForSystem: _Callable[[],
                               _type.UINT]
    GetDpiForWindow: _Callable[[_type.HWND],
                               _type.UINT]
    GetForegroundWindow: _Callable[[],
                                   _type.HWND]
    GetGUIThreadInfo: _Callable[[_type.DWORD,
                                 _Pointer[_struct.GUITHREADINFO]],
                                _type.BOOL]
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
    GetSubMenu: _Callable[[_type.HMENU,
                           _type.c_int],
                          _type.HMENU]
    GetSysColor: _Callable[[_type.c_int],
                           _type.DWORD]
    GetSystemDpiForProcess: _Callable[[_type.HANDLE],
                                      _type.UINT]
    GetSystemMenu: _Callable[[_type.HWND,
                              _type.BOOL],
                             _type.HMENU]
    GetSystemMetrics: _Callable[[_type.c_int],
                                _type.c_int]
    GetWindow: _Callable[[_type.HWND,
                          _type.UINT],
                         _type.HWND]
    GetWindowDC: _Callable[[_Optional[_type.HWND]],
                           _type.HDC]
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
    InsertMenuItemA: _Callable[[_type.HMENU,
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
    IsMenu: _Callable[[_type.HMENU],
                      _type.BOOL]
    IsProcessDPIAware: _Callable[[],
                                 _type.BOOL]
    IsRectEmpty: _Callable[[_Pointer[_struct.RECT]],
                           _type.BOOL]
    IsWindow: _Callable[[_type.HWND],
                        _type.BOOL]
    KillTimer: _Callable[[_type.HWND,
                          _type.UINT_PTR],
                         _type.BOOL]
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
    PostQuitMessage: _Callable[[_type.c_int],
                               _type.c_void_p]
    PrintWindow: _Callable[[_type.HWND,
                            _type.HDC,
                            _type.UINT],
                           _type.BOOL]
    PtInRect: _Callable[[_Pointer[_struct.RECT],
                         _struct.POINT],
                        _type.BOOL]
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
    SetActiveWindow: _Callable[[_type.HWND],
                               _type.BOOL]
    SetClipboardData: _Callable[[_type.UINT,
                                 _type.HANDLE],
                                _type.HANDLE]
    SetCursor: _Callable[[_Optional[_type.HCURSOR]],
                         _type.HCURSOR]
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
    SetForegroundWindow: _Callable[[_type.HWND],
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
    SetProcessDPIAware: _Callable[[],
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
    SubtractRect: _Callable[[_Pointer[_struct.RECT],
                             _Pointer[_struct.RECT],
                             _Pointer[_struct.RECT]],
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
    WindowFromDC: _Callable[[_type.HDC],
                            _type.HWND]


class UxTheme(_WinFunc):
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
                                     _type.c_void_p]
    SetWindowTheme: _Callable[[_type.HWND,
                               _Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR]],
                              _type.HRESULT]
    UpdatePanningFeedback: _Callable[[_type.HWND,
                                      _type.LONG,
                                      _type.LONG,
                                      _type.BOOL],
                                     _type.BOOL]
