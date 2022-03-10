from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing
from typing import Callable as _Callable, Optional as _Optional

from . import com as _com, enum as _enum, struct as _struct, type as _type
from ._head import _get_func_doc, _format_annotations, _not_internal, _Pointer, _resolve_type


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
                        self._lib = _ctypes.pythonapi if self is python else getattr(
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


# noinspection PyPep8Naming
class python(_PyFunc):
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


# noinspection PyPep8Naming
class cfgmgr32(_WinFunc):
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


# noinspection PyPep8Naming
class combase(_WinFunc):
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


# noinspection PyPep8Naming
class comdlg32(_WinFunc):
    ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]],
                            _type.BOOL]
    ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]],
                            _type.BOOL]


# noinspection PyPep8Naming
class gdi32(_WinFunc):
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


# noinspection PyPep8Naming
class kernel32(_WinFunc):
    CloseHandle: _Callable[[_type.HANDLE],
                           _type.BOOL]
    DeleteFileA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    DeleteFileW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
    ExitProcess: _Callable[[_type.UINT],
                           _type.VOID]
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
    GetCurrentProcess: _Callable[[],
                                 _type.HANDLE]
    GetCurrentProcessId: _Callable[[],
                                   _type.DWORD]
    GetExitCodeProcess: _Callable[[_type.HANDLE,
                                   _Pointer[_type.DWORD]],
                                  _type.BOOL]
    GetLastError: _Callable[[],
                            _type.DWORD]
    GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                                _type.HMODULE]
    GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                                _type.HMODULE]
    GetSystemDefaultLangID: _Callable[[],
                                      _type.LANGID]
    GetSystemDefaultLCID: _Callable[[],
                                    _type.LCID]
    GetSystemDefaultLocaleName: _Callable[[_type.LPWSTR,
                                           _type.c_int],
                                          _type.c_int]
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
    SetLastError: _Callable[[_type.DWORD],
                            _type.c_void_p]
    SetThreadLocale: _Callable[[_type.LCID],
                               _type.BOOL]
    Sleep: _Callable[[_type.DWORD],
                     _type.VOID]
    SwitchToThread: _Callable[[],
                              _type.BOOL]
    TerminateProcess: _Callable[[_type.HANDLE,
                                 _type.UINT],
                                _type.BOOL]


# noinspection PyPep8Naming
class msimg32(_WinFunc):
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
    free: _Callable[[_type.c_void_p],
                    _type.c_void_p]
    malloc: _Callable[[_type.c_void_p],
                      _type.c_size_t]
    memmove: _Callable[[_type.c_void_p,
                        _type.c_void_p,
                        _type.c_size_t],
                       _type.c_void_p]
    wcslen: _Callable[[_type.c_wchar_p],
                      _type.c_size_t]


# noinspection PyPep8Naming
class ntdll(_WinFunc):
    RtlAreLongPathsEnabled: _Callable[[],
                                      _type.c_ubyte]


# noinspection PyPep8Naming
class ole32(_WinFunc):
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
    CoInitialize: _Callable[[_Optional[_type.LPVOID]],
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
    IsEqualGUID: _Callable[[_Pointer[_struct.GUID],
                            _Pointer[_struct.GUID]],
                           _type.c_int]
    PropVariantClear: _Callable[[_Pointer[_struct.PROPVARIANT]],
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


# noinspection PyPep8Naming
class oleacc(_WinFunc):
    GetProcessHandleFromHwnd: _Callable[[_type.HWND],
                                        _type.HANDLE]


# noinspection PyPep8Naming
class oleaut32(_WinFunc):
    OleCreatePictureIndirect: _Callable[[_Pointer[_struct.PICTDESC],
                                         _Pointer[_struct.IID],
                                         _type.BOOL,
                                         _type.LPVOID],
                                        _type.WINOLECTLAPI]
    OleSavePictureFile: _Callable[[_com.IPictureDisp,
                                   _type.BSTR],
                                  _type.WINOLECTLAPI]
    VariantClear: _Callable[[_Pointer[_struct.VARIANTARG]],
                            _type.HRESULT]
    VariantInit: _Callable[[_Pointer[_struct.VARIANTARG]],
                           _type.c_void_p]


# noinspection PyPep8Naming
class shell32(_WinFunc):
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 703
    GUIDFromStringW: _Callable[[_type.LPCTSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 704
    ILCreateFromPath: _Callable[[_type.PCTSTR],
                                _Pointer[_struct.ITEMIDLIST]]
    ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                      _type.c_void_p]
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
    SHCreateItemFromParsingName: _Callable[[_type.PCWSTR,
                                            _Optional[_Pointer[_com.IBindCtx]],
                                            _Pointer[_struct.IID],
                                            _Pointer[_com.IShellItem]],
                                           _type.SHSTDAPI]
    SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                                  _Pointer[_Pointer[_struct.ITEMIDLIST]],
                                                  _Pointer[_com.IShellItemArray]],
                                                 _type.SHSTDAPI]
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
    SHOpenFolderAndSelectItems: _Callable[[_Pointer[_struct.ITEMIDLIST],
                                           _type.UINT,
                                           _Optional[_Pointer[_Pointer[_struct.ITEMIDLIST]]],
                                           _type.DWORD],
                                          _type.SHSTDAPI]
    SHOpenWithDialog: _Callable[[_Optional[_type.HWND],
                                 _Pointer[_struct.OPENASINFO]],
                                _type.SHSTDAPI]
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


# noinspection PyPep8Naming
class setupapi(_WinFunc):
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


# noinspection PyPep8Naming
class shcore(_WinFunc):
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


# noinspection PyPep8Naming
class shlwapi(_WinFunc):
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 269
    GUIDFromStringW: _Callable[[_type.LPCTSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 270
    PathFileExistsA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathFileExistsW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathGetDriveNumberA: _Callable[[_type.LPCSTR],
                                   _type.BOOL]
    PathGetDriveNumberW: _Callable[[_type.LPCWSTR],
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
    PathIsNetworkPathA: _Callable[[_type.LPCSTR],
                                  _type.BOOL]
    PathIsNetworkPathW: _Callable[[_type.LPCWSTR],
                                  _type.BOOL]
    PathIsRelativeA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathIsRelativeW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathIsRootA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    PathIsRootW: _Callable[[_type.LPCWSTR],
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


class Taskbar(_WinFunc):
    pass


# noinspection PyPep8Naming
class user32(_WinFunc):
    BeginPaint: _Callable[[_type.HWND,
                           _Pointer[_struct.PAINTSTRUCT]],
                          _type.HDC]
    ClientToScreen: _Callable[[_type.HWND,
                               _Pointer[_struct.POINT]],
                              _type.BOOL]
    CloseClipboard: _Callable[[],
                              _type.BOOL]
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
    GetDpiForSystem: _Callable[[],
                               _type.UINT]
    GetForegroundWindow: _Callable[[],
                                   _type.HWND]
    GetMenu: _Callable[[_type.HWND],
                       _type.HMENU]
    GetMenuInfo: _Callable[[_type.HMENU,
                            _Pointer[_struct.MENUINFO]],
                           _type.BOOL]
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
    GetSubMenu: _Callable[[_type.HMENU,
                           _type.c_int],
                          _type.HMENU]
    GetSysColor: _Callable[[_type.c_int],
                           _type.DWORD]
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
    IntersectRect: _Callable[[_Pointer[_struct.RECT],
                              _Pointer[_struct.RECT],
                              _Pointer[_struct.RECT]],
                             _type.BOOL]
    IsRectEmpty: _Callable[[_Pointer[_struct.RECT]],
                           _type.BOOL]
    KillTimer: _Callable[[_type.HWND,
                          _type.UINT_PTR],
                         _type.BOOL]
    LoadIconA: _Callable[[_Optional[_type.HINSTANCE],
                          _type.UINT],
                         _type.HICON]
    LoadIconW: _Callable[[_Optional[_type.HINSTANCE],
                          _type.UINT],
                         _type.HICON]
    LoadImageA: _Callable[[_type.HINSTANCE,
                           _type.LPCSTR,
                           _type.UINT,
                           _type.c_int,
                           _type.c_int,
                           _type.UINT],
                          _type.HANDLE]
    LoadImageW: _Callable[[_type.HINSTANCE,
                           _type.LPCWSTR,
                           _type.UINT,
                           _type.c_int,
                           _type.c_int,
                           _type.UINT],
                          _type.HANDLE]
    LockWorkStation: _Callable[[],
                               _type.BOOL]
    MapWindowPoints: _Callable[[_Optional[_type.HWND],
                                _Optional[_type.HWND],
                                _Pointer[_struct.POINT],
                                _type.UINT],
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
    PostQuitMessage: _Callable[[_type.c_int],
                               _type.c_void_p]
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
    ReleaseDC: _Callable[[_Optional[_type.HWND],
                          _type.HDC],
                         _type.c_int]
    SendInput: _Callable[[_type.UINT,
                          _Pointer[_struct.INPUT],
                          _type.c_int],
                         _type.UINT]
    SendMessageA: _Callable[[_type.HWND,
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
    SendMessageW: _Callable[[_type.HWND,
                             _type.UINT,
                             _type.WPARAM,
                             _type.LPARAM],
                            _type.LRESULT]
    SetClipboardData: _Callable[[_type.UINT,
                                 _type.HANDLE],
                                _type.HANDLE]
    SetMenuInfo: _Callable[[_type.HMENU,
                            _Pointer[_struct.MENUINFO]],
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
    ShowWindow: _Callable[[_type.HWND,
                           _type.c_int],
                          _type.BOOL]
    SubtractRect: _Callable[[_Pointer[_struct.RECT],
                             _Pointer[_struct.RECT],
                             _Pointer[_struct.RECT]],
                            _type.BOOL]
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


# noinspection PyPep8Naming
class uxtheme(_WinFunc):
    SetWindowTheme: _Callable[[_type.HWND,
                               _Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR]],
                              _type.HRESULT]
