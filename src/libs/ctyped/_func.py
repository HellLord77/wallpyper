import ctypes as _ctypes
import typing as _typing
from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _com
from . import _struct
from . import _type
from .__head__ import _DEBUG
from .__head__ import _Pointer
from .__head__ import _get_doc
from .__head__ import _resolve_type

_FUNCS = '_funcs'


class _CDLL(type):
    def __new__(mcs, *args, **kwargs):
        self = super().__new__(mcs, *args, **kwargs)
        funcs = {}
        setattr(self, _FUNCS, funcs)
        for var in _typing.get_type_hints(self):
            if hasattr(self, var):
                funcs[var] = getattr(self, var)
                delattr(self, var)
            else:
                funcs[var] = var
        return self


class _OleDLL(_CDLL):
    pass


class _WinDLL(_CDLL):
    pass


# noinspection PyPep8Naming
class cfgmgr32(metaclass=_WinDLL):
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
class combase(metaclass=_WinDLL):
    RoActivateInstance: _Callable[[_type.HSTRING,
                                   _type.c_void_p],
                                  _type.HRESULT]
    RoInitialize: _Callable[[_type.RO_INIT_TYPE],
                            _type.HRESULT]
    RoUninitialize: _Callable[[],
                              _type.c_void_p]
    WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH],
                                    _type.UINT32,
                                    _Pointer[_type.HSTRING]],
                                   _type.HRESULT]
    WindowsDeleteString: _Callable[[_type.HSTRING],
                                   _type.HRESULT]


# noinspection PyPep8Naming
class comdlg32(metaclass=_WinDLL):
    ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]], _type.BOOL]
    ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]], _type.BOOL]


# noinspection PyPep8Naming
class gdi32(metaclass=_WinDLL):
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


class GdiPlus(metaclass=_WinDLL):
    GdipCreateBitmapFromFile: _Callable[[_type.LPWSTR,
                                         _Pointer[_type.GpBitmap]],
                                        _type.GpStatus]
    GdipCreateCachedBitmap: _Callable[[_type.GpBitmap,
                                       _type.GpGraphics,
                                       _Pointer[_type.GpCachedBitmap]],
                                      _type.GpStatus]
    GdipCreateFromHDC: _Callable[[_type.HDC,
                                  _Pointer[_type.GpGraphics]],
                                 _type.GpStatus]
    GdipCreateFromHWND: _Callable[[_type.HWND,
                                   _Pointer[_type.GpGraphics]],
                                  _type.GpStatus]
    GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap,
                                            _Pointer[_type.HBITMAP],
                                            _type.ARGB],
                                           _type.GpStatus]
    GdipCreateBitmapFromScan0: _Callable[[_type.INT,
                                          _type.INT,
                                          _type.INT,
                                          _type.PixelFormat,
                                          _Optional[_Pointer[_type.BYTE]],
                                          _Pointer[_type.GpBitmap]],
                                         _type.GpStatus]
    GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap,
                                          _Pointer[_type.HICON]],
                                         _type.GpStatus]
    GdipCreateImageAttributes: _Callable[[_Pointer[_type.GpImageAttributes]],
                                         _type.GpStatus]
    GdipCreateSolidFill: _Callable[[_type.ARGB,
                                    _Pointer[_type.GpSolidFill]],
                                   _type.GpStatus]
    GdipDeleteBrush: _Callable[[_type.GpBrush],
                               _type.GpStatus]
    GdipDeleteCachedBitmap: _Callable[[_type.GpCachedBitmap],
                                      _type.GpStatus]
    GdipDeleteGraphics: _Callable[[_type.GpGraphics],
                                  _type.GpStatus]
    GdipDisposeImage: _Callable[[_type.GpImage],
                                _type.GpStatus]
    GdipDisposeImageAttributes: _Callable[[_type.GpImageAttributes],
                                          _type.GpStatus]
    GdipDrawCachedBitmap: _Callable[[_type.GpGraphics,
                                     _type.GpCachedBitmap,
                                     _type.INT,
                                     _type.INT],
                                    _type.GpStatus]
    GdipDrawImage: _Callable[[_type.GpGraphics,
                              _type.GpImage,
                              _type.REAL,
                              _type.REAL],
                             _type.GpStatus]
    GdipDrawImageI: _Callable[[_type.GpGraphics,
                               _type.GpImage,
                               _type.INT,
                               _type.INT],
                              _type.GpStatus]
    GdipDrawImagePointRect: _Callable[[_type.GpGraphics,
                                       _type.GpImage,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.REAL,
                                       _type.GpUnit],
                                      _type.GpStatus]
    GdipDrawImagePointRectI: _Callable[[_type.GpGraphics,
                                        _type.GpImage,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _type.INT,
                                        _type.GpUnit],
                                       _type.GpStatus]
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
                                      _type.GpUnit,
                                      _Optional[_type.GpImageAttributes],
                                      _type.DrawImageAbort,
                                      _Optional[_type.PVOID]],
                                     _type.GpStatus]
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
                                       _type.GpUnit,
                                       _Optional[_type.GpImageAttributes],
                                       _type.DrawImageAbort,
                                       _Optional[_type.PVOID]],
                                      _type.GpStatus]
    GdipFillRectangle: _Callable[[_type.GpGraphics,
                                  _type.GpBrush,
                                  _type.REAL,
                                  _type.REAL,
                                  _type.REAL,
                                  _type.REAL],
                                 _type.GpStatus]
    GdipFillRectangleI: _Callable[[_type.GpGraphics,
                                   _type.GpBrush,
                                   _type.INT,
                                   _type.INT,
                                   _type.INT,
                                   _type.INT],
                                  _type.GpStatus]
    GdipGetDC: _Callable[[_type.GpGraphics,
                          _Pointer[_type.HDC]],
                         _type.GpStatus]
    GdipGetImageEncodersSize: _Callable[[_Pointer[_type.UINT],
                                         _Pointer[_type.UINT]],
                                        _type.GpStatus]
    GdipGetImageDimension: _Callable[[_type.GpImage,
                                      _Pointer[_type.REAL],
                                      _Pointer[_type.REAL]],
                                     _type.GpStatus]
    GdipGetImageHeight: _Callable[[_type.GpImage,
                                   _Pointer[_type.UINT]],
                                  _type.GpStatus]
    GdipGetImageWidth: _Callable[[_type.GpImage,
                                  _Pointer[_type.UINT]],
                                 _type.GpStatus]
    GdipGetImageGraphicsContext: _Callable[[_type.GpImage,
                                            _Pointer[_type.GpGraphics]],
                                           _type.GpStatus]
    GdipGetPropertyItem: _Callable[[_type.GpImage,
                                    _type.PROPID,
                                    _type.UINT,
                                    _Pointer[_struct.PropertyItem]],
                                   _type.GpStatus]
    GdipGetPropertyItemSize: _Callable[[_type.GpImage,
                                        _type.PROPID,
                                        _Pointer[_type.UINT]],
                                       _type.GpStatus]
    GdipGetSolidFillColor: _Callable[[_type.GpSolidFill,
                                      _Pointer[_type.ARGB]],
                                     _type.GpStatus]
    GdipImageGetFrameCount: _Callable[[_type.GpImage,
                                       _Pointer[_struct.GUID],
                                       _Pointer[_type.UINT]],
                                      _type.GpStatus]
    GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage,
                                                 _Pointer[_type.UINT]],
                                                _type.GpStatus]
    GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage,
                                                _Pointer[_struct.GUID],
                                                _type.UINT],
                                               _type.GpStatus]
    GdipImageSelectActiveFrame: _Callable[[_type.GpImage,
                                           _Pointer[_struct.GUID],
                                           _type.UINT],
                                          _type.GpStatus]
    GdipLoadImageFromFile: _Callable[[_type.LPWSTR,
                                      _Pointer[_type.GpImage]],
                                     _type.GpStatus]
    GdipScaleWorldTransform: _Callable[[_type.GpGraphics,
                                        _type.REAL,
                                        _type.REAL,
                                        _type.GpMatrixOrder],
                                       _type.GpStatus]
    GdipSetImageAttributesColorMatrix: _Callable[[_type.GpImageAttributes,
                                                  _type.ColorAdjustType,
                                                  _type.BOOL,
                                                  _Pointer[_struct.ColorMatrix],
                                                  _Optional[_Pointer[_struct.ColorMatrix]],
                                                  _type.ColorMatrixFlags],
                                                 _type.GpStatus]
    GdipSetImageAttributesRemapTable: _Callable[[_type.GpImageAttributes,
                                                 _type.ColorAdjustType,
                                                 _type.BOOL,
                                                 _type.UINT,
                                                 _Pointer[_struct.ColorMap]],
                                                _type.GpStatus]
    GdipSetSolidFillColor: _Callable[[_type.GpSolidFill,
                                      _type.ARGB],
                                     _type.GpStatus]
    GdipReleaseDC: _Callable[[_type.GpGraphics,
                              _type.HDC],
                             _type.GpStatus]
    GdiplusShutdown: _Callable[[_type.ULONG_PTR],
                               _type.VOID]
    GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],
                               _Pointer[_struct.GdiplusStartupInput],
                               _Optional[_Pointer[_struct.GdiplusStartupInput]]],
                              _type.Status]


# noinspection PyPep8Naming
class kernel32(metaclass=_WinDLL):
    CloseHandle: _Callable[[_type.HANDLE],
                           _type.BOOL]
    DeleteFileA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    DeleteFileW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
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
    GetLastError: _Callable[[],
                            _type.DWORD]
    GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                                _type.HMODULE]
    GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                                _type.HMODULE]
    GetTempPathA: _Callable[[_type.DWORD,
                             _type.LPSTR],
                            _type.DWORD]
    GetTempPathW: _Callable[[_type.DWORD,
                             _type.LPWSTR],
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
    SetLastError: _Callable[[_type.DWORD],
                            _type.c_void_p]
    Sleep: _Callable[[_type.DWORD],
                     _type.VOID]


# noinspection PyPep8Naming
class msimg32(metaclass=_WinDLL):
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
class msvcrt(metaclass=_WinDLL):
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
class ntdll(metaclass=_WinDLL):
    RtlAreLongPathsEnabled: _Callable[[],
                                      _type.c_ubyte]


# noinspection PyPep8Naming
class ole32(metaclass=_WinDLL):
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
    CoTaskMemFree: _Callable[[_type.LPVOID],
                             _type.c_void_p]
    CoUninitialize: _Callable[[],
                              _type.VOID]
    IIDFromString: _Callable[[_type.LPCOLESTR,
                              _Pointer[_struct.IID]],
                             _type.HRESULT]
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
class oleaut32(metaclass=_WinDLL):
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
class shell32(metaclass=_WinDLL):
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
                                     _type.KNOWN_FOLDER_FLAG,
                                     _Optional[_type.HANDLE],
                                     _Pointer[_type.PWSTR]],
                                    _type.HRESULT]
    SHGetPropertyStoreFromParsingName: _Callable[[_type.PCWSTR,
                                                  _Optional[_Pointer[_com.IBindCtx]],
                                                  _type.GETPROPERTYSTOREFLAGS,
                                                  _Pointer[_struct.IID],
                                                  _Pointer[_com.IPropertyStore]],
                                                 _type.SHSTDAPI]
    SHOpenFolderAndSelectItems: _Callable[[_Pointer[_struct.ITEMIDLIST],
                                           _type.UINT,
                                           _Optional[_Pointer[_Pointer[_struct.ITEMIDLIST]]],
                                           _type.DWORD],
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
    Shell_NotifyIconA: _Callable[[_type.DWORD,
                                  _Pointer[_struct.NOTIFYICONDATAA]],
                                 _type.BOOL]
    Shell_NotifyIconW: _Callable[[_type.DWORD,
                                  _Pointer[_struct.NOTIFYICONDATAW]],
                                 _type.BOOL]


# noinspection PyPep8Naming
class setupapi(metaclass=_WinDLL):
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
class shlwapi(metaclass=_WinDLL):
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


class Taskbar(metaclass=_WinDLL):
    pass


# noinspection PyPep8Naming
class user32(metaclass=_WinDLL):
    BeginPaint: _Callable[[_type.HWND,
                           _Pointer[_struct.PAINTSTRUCT]],
                          _type.HDC]
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
    GetWindowTextA: _Callable[[_type.HWND,
                               _type.LPSTR,
                               _type.c_int],
                              _type.c_int]
    GetWindowTextW: _Callable[[_type.HWND,
                               _type.LPWSTR,
                               _type.c_int],
                              _type.c_int]
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
    OpenClipboard: _Callable[[_Optional[_type.HWND]],
                             _type.BOOL]
    PostQuitMessage: _Callable[[_type.c_int],
                               _type.c_void_p]
    RegisterClassExA: _Callable[[_Pointer[_struct.WNDCLASSEXA]],
                                _type.ATOM]
    RegisterClassExW: _Callable[[_Pointer[_struct.WNDCLASSEXW]],
                                _type.ATOM]
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
    SetWindowPos: _Callable[[_type.HWND,
                             _Optional[_type.HWND],
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int, _type.UINT],
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
    UnhookWindowsHook: _Callable[[_type.c_int,
                                  _type.HOOKPROC],
                                 _type.BOOL]
    UnhookWindowsHookEx: _Callable[[_type.HHOOK],
                                   _type.BOOL]
    UnregisterClassA: _Callable[[_type.LPCSTR,
                                 _type.HINSTANCE],
                                _type.BOOL]
    UnregisterClassW: _Callable[[_type.LPCWSTR,
                                 _type.HINSTANCE],
                                _type.BOOL]


# noinspection PyPep8Naming
class uxtheme(metaclass=_WinDLL):
    SetWindowTheme: _Callable[[_type.HWND,
                               _Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR]],
                              _type.HRESULT]


def _init(lib: type[_CDLL], name: str):
    if name == 'lib':
        lib.lib = getattr(_ctypes, lib.__class__.__name__[1:])(lib.__name__, use_last_error=_DEBUG)
        return lib.lib
    try:
        func = lib.lib[getattr(lib, _FUNCS)[name]]
    except KeyError:
        raise AttributeError(f"lib '{lib.__name__}' has no function '{name}'")
    setattr(lib, name, func)
    func.restype, *func.argtypes = _resolve_type(_typing.get_type_hints(lib)[name])
    func.__doc__ = _get_doc(name, func.restype, func.argtypes)
    return func


_CDLL.__getattr__ = _init
