from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# wingdi
AddFontResourceA: _Callable[[_type.LPCSTR],
                            _type.c_int]
AddFontResourceW: _Callable[[_type.LPCWSTR],
                            _type.c_int]
AnimatePalette: _Callable[[_type.HPALETTE,  # hPal
                           _type.UINT,  # iStartIndex
                           _type.UINT,  # cEntries
                           _Pointer[_struct.PALETTEENTRY]],  # ppe
                          _type.BOOL]
Arc: _Callable[[_type.HDC,  # hdc
                _type.c_int,  # x1
                _type.c_int,  # y1
                _type.c_int,  # x2
                _type.c_int,  # y2
                _type.c_int,  # x3
                _type.c_int,  # y3
                _type.c_int,  # x4
                _type.c_int],  # y4
               _type.BOOL]
BitBlt: _Callable[[_type.HDC,  # hdc
                   _type.c_int,  # x
                   _type.c_int,  # y
                   _type.c_int,  # cx
                   _type.c_int,  # cy
                   _type.HDC,  # hdcSrc
                   _type.c_int,  # x1
                   _type.c_int,  # y1
                   _type.DWORD],  # rop
                  _type.BOOL]
CancelDC: _Callable[[_type.HDC],  # hdc
                    _type.BOOL]
Chord: _Callable[[_type.HDC,  # hdc
                  _type.c_int,  # x1
                  _type.c_int,  # y1
                  _type.c_int,  # x2
                  _type.c_int,  # y2
                  _type.c_int,  # x3
                  _type.c_int,  # y3
                  _type.c_int,  # x4
                  _type.c_int],  # y4
                 _type.BOOL]
ChoosePixelFormat: _Callable[[_type.HDC,  # hdc
                              _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                             _type.c_int]
CloseMetaFile: _Callable[[_type.HDC],  # hdc
                         _type.HMETAFILE]
CombineRgn: _Callable[[_type.HRGN,  # hrgnDst
                       _type.HRGN,  # hrgnSrc1
                       _type.HRGN,  # hrgnSrc2
                       _type.c_int],  # iMode
                      _type.c_int]
CopyMetaFileA: _Callable[[_type.HMETAFILE,
                          _type.LPCSTR],
                         _type.HMETAFILE]
CopyMetaFileW: _Callable[[_type.HMETAFILE,
                          _type.LPCWSTR],
                         _type.HMETAFILE]
CreateBitmap: _Callable[[_type.c_int,  # nWidth
                         _type.c_int,  # nHeight
                         _type.UINT,  # nPlanes
                         _type.UINT,  # nBitCount
                         _type.c_void_p],  # lpBits
                        _type.HBITMAP]
CreateBitmapIndirect: _Callable[[_Pointer[_struct.BITMAP]],  # pbm
                                _type.HBITMAP]
CreateBrushIndirect: _Callable[[_Pointer[_struct.LOGBRUSH]],  # plbrush
                               _type.HBRUSH]
CreateCompatibleBitmap: _Callable[[_type.HDC,  # hdc
                                   _type.c_int,  # cx
                                   _type.c_int],  # cy
                                  _type.HBITMAP]
CreateDiscardableBitmap: _Callable[[_type.HDC,  # hdc
                                    _type.c_int,  # cx
                                    _type.c_int],  # cy
                                   _type.HBITMAP]
CreateCompatibleDC: _Callable[[_type.HDC],  # hdc
                              _type.HDC]
CreateDCA: _Callable[[_type.LPCSTR,  # pwszDriver
                      _type.LPCSTR,  # pwszDevice
                      _type.LPCSTR,  # pszPort
                      _Pointer[_struct.DEVMODEA]],  # pdm
                     _type.HDC]
CreateDCW: _Callable[[_type.LPCWSTR,  # pwszDriver
                      _type.LPCWSTR,  # pwszDevice
                      _type.LPCWSTR,  # pszPort
                      _Pointer[_struct.DEVMODEW]],  # pdm
                     _type.HDC]
CreateDIBitmap: _Callable[[_type.HDC,  # hdc
                           _Pointer[_struct.BITMAPINFOHEADER],  # pbmih
                           _type.DWORD,  # flInit
                           _type.c_void_p,  # pjBits
                           _Pointer[_struct.BITMAPINFO],  # pbmi
                           _type.UINT],  # iUsage
                          _type.HBITMAP]
CreateDIBPatternBrush: _Callable[[_type.HGLOBAL,  # h
                                  _type.UINT],  # iUsage
                                 _type.HBRUSH]
CreateDIBPatternBrushPt: _Callable[[_type.c_void_p,  # lpPackedDIB
                                    _type.UINT],  # iUsage
                                   _type.HBRUSH]
CreateEllipticRgn: _Callable[[_type.c_int,  # x1
                              _type.c_int,  # y1
                              _type.c_int,  # x2
                              _type.c_int],  # y2
                             _type.HRGN]
CreateEllipticRgnIndirect: _Callable[[_Pointer[_struct.RECT]],  # lprect
                                     _type.HRGN]
CreateFontIndirectA: _Callable[[_Pointer[_struct.LOGFONTA]],  # lplf
                               _type.HFONT]
CreateFontIndirectW: _Callable[[_Pointer[_struct.LOGFONTW]],  # lplf
                               _type.HFONT]
CreateFontA: _Callable[[_type.c_int,  # cHeight
                        _type.c_int,  # cWidth
                        _type.c_int,  # cEscapement
                        _type.c_int,  # cOrientation
                        _type.c_int,  # cWeight
                        _type.DWORD,  # bItalic
                        _type.DWORD,  # bUnderline
                        _type.DWORD,  # bStrikeOut
                        _type.DWORD,  # iCharSet
                        _type.DWORD,  # iOutPrecision
                        _type.DWORD,  # iClipPrecision
                        _type.DWORD,  # iQuality
                        _type.DWORD,  # iPitchAndFamily
                        _type.LPCSTR],  # pszFaceName
                       _type.HFONT]
CreateFontW: _Callable[[_type.c_int,  # cHeight
                        _type.c_int,  # cWidth
                        _type.c_int,  # cEscapement
                        _type.c_int,  # cOrientation
                        _type.c_int,  # cWeight
                        _type.DWORD,  # bItalic
                        _type.DWORD,  # bUnderline
                        _type.DWORD,  # bStrikeOut
                        _type.DWORD,  # iCharSet
                        _type.DWORD,  # iOutPrecision
                        _type.DWORD,  # iClipPrecision
                        _type.DWORD,  # iQuality
                        _type.DWORD,  # iPitchAndFamily
                        _type.LPCWSTR],  # pszFaceName
                       _type.HFONT]
CreateHatchBrush: _Callable[[_type.c_int,  # iHatch
                             _type.COLORREF],  # color
                            _type.HBRUSH]
CreateICA: _Callable[[_type.LPCSTR,  # pszDriver
                      _type.LPCSTR,  # pszDevice
                      _type.LPCSTR,  # pszPort
                      _Pointer[_struct.DEVMODEA]],  # pdm
                     _type.HDC]
CreateICW: _Callable[[_type.LPCWSTR,  # pszDriver
                      _type.LPCWSTR,  # pszDevice
                      _type.LPCWSTR,  # pszPort
                      _Pointer[_struct.DEVMODEW]],  # pdm
                     _type.HDC]
CreateMetaFileA: _Callable[[_type.LPCSTR],  # pszFile
                           _type.HDC]
CreateMetaFileW: _Callable[[_type.LPCWSTR],  # pszFile
                           _type.HDC]
CreatePalette: _Callable[[_Pointer[_struct.LOGPALETTE]],  # plpal
                         _type.HPALETTE]
CreatePen: _Callable[[_type.c_int,  # iStyle
                      _type.c_int,  # cWidth
                      _type.COLORREF],  # color
                     _type.HPEN]
CreatePenIndirect: _Callable[[_Pointer[_struct.LOGPEN]],  # plpen
                             _type.HPEN]
CreatePolyPolygonRgn: _Callable[[_Pointer[_struct.POINT],  # pptl
                                 _Pointer[_type.INT],  # pc
                                 _type.c_int,  # cPoly
                                 _type.c_int],  # iMode
                                _type.HRGN]
CreatePatternBrush: _Callable[[_type.HBITMAP],  # hbm
                              _type.HBRUSH]
CreateRectRgn: _Callable[[_type.c_int,  # x1
                          _type.c_int,  # y1
                          _type.c_int,  # x2
                          _type.c_int],  # y2
                         _type.HRGN]
CreateRectRgnIndirect: _Callable[[_Pointer[_struct.RECT]],  # lprect
                                 _type.HRGN]
CreateRoundRectRgn: _Callable[[_type.c_int,  # x1
                               _type.c_int,  # y1
                               _type.c_int,  # x2
                               _type.c_int,  # y2
                               _type.c_int,  # w
                               _type.c_int],  # h
                              _type.HRGN]
CreateScalableFontResourceA: _Callable[[_type.DWORD,  # fdwHidden
                                        _type.LPCSTR,  # lpszFont
                                        _type.LPCSTR,  # lpszFile
                                        _type.LPCSTR],  # lpszPath
                                       _type.BOOL]
CreateScalableFontResourceW: _Callable[[_type.DWORD,  # fdwHidden
                                        _type.LPCWSTR,  # lpszFont
                                        _type.LPCWSTR,  # lpszFile
                                        _type.LPCWSTR],  # lpszPath
                                       _type.BOOL]
CreateSolidBrush: _Callable[[_type.COLORREF],  # color
                            _type.HBRUSH]
DeleteDC: _Callable[[_type.HDC],  # hdc
                    _type.BOOL]
DeleteMetaFile: _Callable[[_type.HMETAFILE],  # hmf
                          _type.BOOL]
DeleteObject: _Callable[[_type.HGDIOBJ],  # ho
                        _type.BOOL]
DescribePixelFormat: _Callable[[_type.HDC,  # hdc
                                _type.c_int,  # iPixelFormat
                                _type.UINT,  # nBytes
                                _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                               _type.c_int]
DeviceCapabilitiesA: _Callable[[_type.LPCSTR,  # pDevice
                                _type.LPCSTR,  # pPort
                                _type.WORD,  # fwCapability
                                _type.LPSTR,  # pOutput
                                _Pointer[_struct.DEVMODEA]],  # pDevMode
                               _type.c_int]
DeviceCapabilitiesW: _Callable[[_type.LPCWSTR,  # pDevice
                                _type.LPCWSTR,  # pPort
                                _type.WORD,  # fwCapability
                                _type.LPWSTR,  # pOutput
                                _Pointer[_struct.DEVMODEW]],  # pDevMode
                               _type.c_int]
DrawEscape: _Callable[[_type.HDC,  # hdc
                       _type.c_int,  # iEscape
                       _type.c_int,  # cjIn
                       _type.LPCSTR],  # lpIn
                      _type.c_int]
Ellipse: _Callable[[_type.HDC,  # hdc
                    _type.c_int,  # left
                    _type.c_int,  # top
                    _type.c_int,  # right
                    _type.c_int],  # bottom
                   _type.BOOL]
# EnumFontFamiliesExA: _Callable[[_type.HDC,  # hdc
#                                 _Pointer[_struct.LOGFONTA],  # lpLogfont
#                                 FONTENUMPROCA,  # lpProc
#                                 _type.LPARAM,  # lParam
#                                 _type.DWORD],  # dwFlags
#                                _type.c_int]
# EnumFontFamiliesExW: _Callable[[_type.HDC,  # hdc
#                                 _Pointer[_struct.LOGFONTW],  # lpLogfont
#                                 FONTENUMPROCW,  # lpProc
#                                 _type.LPARAM,  # lParam
#                                 _type.DWORD],  # dwFlags
#                                _type.c_int]
# EnumFontFamiliesA: _Callable[[_type.HDC,  # hdc
#                               _type.LPCSTR,  # lpLogfont
#                               FONTENUMPROCA,  # lpProc
#                               _type.LPARAM],  # lParam
#                              _type.c_int]
# EnumFontFamiliesW: _Callable[[_type.HDC,  # hdc
#                               _type.LPCWSTR,  # lpLogfont
#                               FONTENUMPROCW,  # lpProc
#                               _type.LPARAM],  # lParam
#                              _type.c_int]
# EnumFontsA: _Callable[[_type.HDC,  # hdc
#                        _type.LPCSTR,  # lpLogfont
#                        FONTENUMPROCA,  # lpProc
#                        _type.LPARAM],  # lParam
#                       _type.c_int]
# EnumFontsW: _Callable[[_type.HDC,  # hdc
#                        _type.LPCWSTR,  # lpLogfont
#                        FONTENUMPROCW,  # lpProc
#                        _type.LPARAM],  # lParam
#                       _type.c_int]
EnumObjects: _Callable[[_type.HDC,  # hdc
                        _type.c_int,  # nType
                        _type.GOBJENUMPROC,  # lpFunc
                        _type.LPARAM],  # lParam
                       _type.c_int]
EqualRgn: _Callable[[_type.HRGN,  # hrgn1
                     _type.HRGN],  # hrgn2
                    _type.BOOL]
Escape: _Callable[[_type.HDC,  # hdc
                   _type.c_int,  # iEscape
                   _type.c_int,  # cjIn
                   _type.LPCSTR,  # pvIn
                   _type.LPVOID],  # pvOut
                  _type.c_int]
ExtEscape: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # iEscape
                      _type.c_int,  # cjInput
                      _type.LPCSTR,  # lpInData
                      _type.c_int,  # cjOutput
                      _type.LPSTR],  # lpOutData
                     _type.c_int]
ExcludeClipRect: _Callable[[_type.HDC,  # hdc
                            _type.c_int,  # left
                            _type.c_int,  # top
                            _type.c_int,  # right
                            _type.c_int],  # bottom
                           _type.c_int]
ExtCreateRegion: _Callable[[_Pointer[_struct.XFORM],  # lpx
                            _type.DWORD,  # nCount
                            _Pointer[_struct.RGNDATA]],  # lpData
                           _type.HRGN]
ExtFloodFill: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # x
                         _type.c_int,  # y
                         _type.COLORREF,  # color
                         _type.UINT],  # type
                        _type.BOOL]
FillRgn: _Callable[[_type.HDC,  # hdc
                    _type.HRGN,  # hrgn
                    _type.HBRUSH],  # hbr
                   _type.BOOL]
FloodFill: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # x
                      _type.c_int,  # y
                      _type.COLORREF],  # color
                     _type.BOOL]
FrameRgn: _Callable[[_type.HDC,  # hdc
                     _type.HRGN,  # hrgn
                     _type.HBRUSH,  # hbr
                     _type.c_int,  # w
                     _type.c_int],  # h
                    _type.BOOL]
GetROP2: _Callable[[_type.HDC],  # hdc
                   _type.c_int]
GetAspectRatioFilterEx: _Callable[[_type.HDC,  # hdc
                                   _Pointer[_struct.SIZE]],  # lpsize
                                  _type.BOOL]
GetBkColor: _Callable[[_type.HDC],  # hdc
                      _type.COLORREF]
GetDCBrushColor: _Callable[[_type.HDC],  # hdc
                           _type.COLORREF]
GetDCPenColor: _Callable[[_type.HDC],  # hdc
                         _type.COLORREF]
GetBkMode: _Callable[[_type.HDC],  # hdc
                     _type.c_int]
GetBitmapBits: _Callable[[_type.HBITMAP,  # hbit
                          _type.LONG,  # cb
                          _type.LPVOID],  # lpvBits
                         _type.LONG]
GetBitmapDimensionEx: _Callable[[_type.HBITMAP,  # hbit
                                 _Pointer[_struct.SIZE]],  # lpsize
                                _type.BOOL]
GetBoundsRect: _Callable[[_type.HDC,  # hdc
                          _Pointer[_struct.RECT],  # lprect
                          _type.UINT],  # flags
                         _type.UINT]
GetBrushOrgEx: _Callable[[_type.HDC,  # hdc
                          _Pointer[_struct.POINT]],  # lppt
                         _type.BOOL]
GetCharWidthA: _Callable[[_type.HDC,  # hdc
                          _type.UINT,  # iFirst
                          _type.UINT,  # iLast
                          _Pointer[_type.c_int]],  # lpBuffer
                         _type.BOOL]
GetCharWidthW: _Callable[[_type.HDC,  # hdc
                          _type.UINT,  # iFirst
                          _type.UINT,  # iLast
                          _Pointer[_type.c_int]],  # lpBuffer
                         _type.BOOL]
GetCharWidth32A: _Callable[[_type.HDC,  # hdc
                            _type.UINT,  # iFirst
                            _type.UINT,  # iLast
                            _Pointer[_type.c_int]],  # lpBuffer
                           _type.BOOL]
GetCharWidth32W: _Callable[[_type.HDC,  # hdc
                            _type.UINT,  # iFirst
                            _type.UINT,  # iLast
                            _Pointer[_type.c_int]],  # lpBuffer
                           _type.BOOL]
GetCharWidthFloatA: _Callable[[_type.HDC,  # hdc
                               _type.UINT,  # iFirst
                               _type.UINT,  # iLast
                               _Pointer[_type.FLOAT]],  # lpBuffer
                              _type.BOOL]
GetCharWidthFloatW: _Callable[[_type.HDC,  # hdc
                               _type.UINT,  # iFirst
                               _type.UINT,  # iLast
                               _Pointer[_type.FLOAT]],  # lpBuffer
                              _type.BOOL]
GetCharABCWidthsA: _Callable[[_type.HDC,  # hdc
                              _type.UINT,  # wFirst
                              _type.UINT,  # wLast
                              _Pointer[_struct.ABC]],  # lpABC
                             _type.BOOL]
GetCharABCWidthsW: _Callable[[_type.HDC,  # hdc
                              _type.UINT,  # wFirst
                              _type.UINT,  # wLast
                              _Pointer[_struct.ABC]],  # lpABC
                             _type.BOOL]
GetCharABCWidthsFloatA: _Callable[[_type.HDC,  # hdc
                                   _type.UINT,  # iFirst
                                   _type.UINT,  # iLast
                                   _Pointer[_struct.ABCFLOAT]],  # lpABC
                                  _type.BOOL]
GetCharABCWidthsFloatW: _Callable[[_type.HDC,  # hdc
                                   _type.UINT,  # iFirst
                                   _type.UINT,  # iLast
                                   _Pointer[_struct.ABCFLOAT]],  # lpABC
                                  _type.BOOL]
GetClipBox: _Callable[[_type.HDC,  # hdc
                       _Pointer[_struct.RECT]],  # lprect
                      _type.c_int]
GetClipRgn: _Callable[[_type.HDC,  # hdc
                       _type.HRGN],  # hrgn
                      _type.c_int]
GetMetaRgn: _Callable[[_type.HDC,  # hdc
                       _type.HRGN],  # hrgn
                      _type.c_int]
GetCurrentObject: _Callable[[_type.HDC,  # hdc
                             _type.UINT],  # type
                            _type.HGDIOBJ]
GetCurrentPositionEx: _Callable[[_type.HDC,  # hdc
                                 _Pointer[_struct.POINT]],  # lppt
                                _type.BOOL]
GetDeviceCaps: _Callable[[_type.HDC,  # hdc
                          _type.c_int],  # index
                         _type.c_int]
GetDIBits: _Callable[[_type.HDC,  # hdc
                      _type.HBITMAP,  # hbm
                      _type.UINT,  # start
                      _type.UINT,  # cLines
                      _type.LPVOID,  # lpvBits
                      _Pointer[_struct.BITMAPINFO],  # lpbmi
                      _type.UINT],  # usage
                     _type.c_int]
GetFontData: _Callable[[_type.HDC,  # hdc
                        _type.DWORD,  # dwTable
                        _type.DWORD,  # dwOffset
                        _type.PVOID,  # pvBuffer
                        _type.DWORD],  # cjBuffer
                       _type.DWORD]
GetGlyphOutlineA: _Callable[[_type.HDC,  # hdc
                             _type.UINT,  # uChar
                             _type.UINT,  # fuFormat
                             _Pointer[_struct.GLYPHMETRICS],  # lpgm
                             _type.DWORD,  # cjBuffer
                             _type.LPVOID,  # pvBuffer
                             _Pointer[_struct.MAT2]],  # lpmat2
                            _type.DWORD]
GetGlyphOutlineW: _Callable[[_type.HDC,  # hdc
                             _type.UINT,  # uChar
                             _type.UINT,  # fuFormat
                             _Pointer[_struct.GLYPHMETRICS],  # lpgm
                             _type.DWORD,  # cjBuffer
                             _type.LPVOID,  # pvBuffer
                             _Pointer[_struct.MAT2]],  # lpmat2
                            _type.DWORD]
GetGraphicsMode: _Callable[[_type.HDC],  # hdc
                           _type.c_int]
GetMapMode: _Callable[[_type.HDC],  # hdc
                      _type.c_int]
GetMetaFileBitsEx: _Callable[[_type.HMETAFILE,  # hMF
                              _type.UINT,  # cbBuffer
                              _type.LPVOID],  # lpData
                             _type.UINT]
GetMetaFileA: _Callable[[_type.LPCSTR],  # lpName
                        _type.HMETAFILE]
GetMetaFileW: _Callable[[_type.LPCWSTR],  # lpName
                        _type.HMETAFILE]
GetNearestColor: _Callable[[_type.HDC,  # hdc
                            _type.COLORREF],  # color
                           _type.COLORREF]
GetNearestPaletteIndex: _Callable[[_type.HPALETTE,  # h
                                   _type.COLORREF],  # color
                                  _type.UINT]
GetObjectType: _Callable[[_type.HGDIOBJ],  # h
                         _type.DWORD]
GetOutlineTextMetricsA: _Callable[[_type.HDC,  # hdc
                                   _type.UINT,  # cjCopy
                                   _Pointer[_struct.OUTLINETEXTMETRICA]],  # potm
                                  _type.UINT]
GetOutlineTextMetricsW: _Callable[[_type.HDC,  # hdc
                                   _type.UINT,  # cjCopy
                                   _Pointer[_struct.OUTLINETEXTMETRICW]],  # potm
                                  _type.UINT]
GetPaletteEntries: _Callable[[_type.HPALETTE,  # hpal
                              _type.UINT,  # iStart
                              _type.UINT,  # cEntries
                              _Pointer[_struct.PALETTEENTRY]],  # pPalEntries
                             _type.UINT]
GetPixel: _Callable[[_type.HDC,  # hdc
                     _type.c_int,  # x
                     _type.c_int],  # y
                    _type.COLORREF]
GetPixelFormat: _Callable[[_type.HDC],  # hdc
                          _type.c_int]
GetPolyFillMode: _Callable[[_type.HDC],  # hdc
                           _type.c_int]
GetRasterizerCaps: _Callable[[_Pointer[_struct.RASTERIZER_STATUS],  # lpraststat
                              _type.UINT],  # cjBytes
                             _type.BOOL]
GetRandomRgn: _Callable[[_type.HDC,  # hdc
                         _type.HRGN,  # hrgn
                         _type.INT],  # i
                        _type.c_int]
GetRegionData: _Callable[[_type.HRGN,  # hrgn
                          _type.DWORD,  # nCount
                          _Pointer[_struct.RGNDATA]],  # lpRgnData
                         _type.DWORD]
GetRgnBox: _Callable[[_type.HRGN,  # hrgn
                      _Pointer[_struct.RECT]],  # lprc
                     _type.c_int]
GetStockObject: _Callable[[_type.c_int],  # i
                          _type.HGDIOBJ]
GetStretchBltMode: _Callable[[_type.HDC],  # hdc
                             _type.c_int]
GetSystemPaletteEntries: _Callable[[_type.HDC,  # hdc
                                    _type.UINT,  # iStart
                                    _type.UINT,  # cEntries
                                    _Pointer[_struct.PALETTEENTRY]],  # pPalEntries
                                   _type.UINT]
GetSystemPaletteUse: _Callable[[_type.HDC],  # hdc
                               _type.UINT]
GetTextCharacterExtra: _Callable[[_type.HDC],  # hdc
                                 _type.c_int]
GetTextAlign: _Callable[[_type.HDC],  # hdc
                        _type.UINT]
GetTextColor: _Callable[[_type.HDC],  # hdc
                        _type.COLORREF]
GetTextExtentPointA: _Callable[[_type.HDC,  # hdc
                                _type.LPCSTR,  # lpString
                                _type.c_int,  # c
                                _Pointer[_struct.SIZE]],  # lpsz
                               _type.BOOL]
GetTextExtentPointW: _Callable[[_type.HDC,  # hdc
                                _type.LPCWSTR,  # lpString
                                _type.c_int,  # c
                                _Pointer[_struct.SIZE]],  # lpsz
                               _type.BOOL]
GetTextExtentPoint32A: _Callable[[_type.HDC,  # hdc
                                  _type.LPCSTR,  # lpString
                                  _type.c_int,  # c
                                  _Pointer[_struct.SIZE]],  # psizl
                                 _type.BOOL]
GetTextExtentPoint32W: _Callable[[_type.HDC,  # hdc
                                  _type.LPCWSTR,  # lpString
                                  _type.c_int,  # c
                                  _Pointer[_struct.SIZE]],  # psizl
                                 _type.BOOL]
GetTextExtentExPointA: _Callable[[_type.HDC,  # hdc
                                  _type.LPCSTR,  # lpszString
                                  _type.c_int,  # cchString
                                  _type.c_int,  # nMaxExtent
                                  _Pointer[_type.c_int],  # lpnFit
                                  _Pointer[_type.c_int],  # lpnDx
                                  _Pointer[_struct.SIZE]],  # lpSize
                                 _type.BOOL]
GetTextExtentExPointW: _Callable[[_type.HDC,  # hdc
                                  _type.LPCWSTR,  # lpszString
                                  _type.c_int,  # cchString
                                  _type.c_int,  # nMaxExtent
                                  _Pointer[_type.c_int],  # lpnFit
                                  _Pointer[_type.c_int],  # lpnDx
                                  _Pointer[_struct.SIZE]],  # lpSize
                                 _type.BOOL]
GetTextCharset: _Callable[[_type.HDC],  # hdc
                          _type.c_int]
GetTextCharsetInfo: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.FONTSIGNATURE],  # lpSig
                               _type.DWORD],  # dwFlags
                              _type.c_int]
TranslateCharsetInfo: _Callable[[_Pointer[_type.DWORD],  # lpSrc
                                 _Pointer[_struct.CHARSETINFO],  # lpCs
                                 _type.DWORD],  # dwFlags
                                _type.BOOL]
GetFontLanguageInfo: _Callable[[_type.HDC],  # hdc
                               _type.DWORD]
GetCharacterPlacementA: _Callable[[_type.HDC,  # hdc
                                   _type.LPCSTR,  # lpString
                                   _type.c_int,  # nCount
                                   _type.c_int,  # nMexExtent
                                   _Pointer[_struct.GCP_RESULTSA],  # lpResults
                                   _type.DWORD],  # dwFlags
                                  _type.DWORD]
GetCharacterPlacementW: _Callable[[_type.HDC,  # hdc
                                   _type.LPCWSTR,  # lpString
                                   _type.c_int,  # nCount
                                   _type.c_int,  # nMexExtent
                                   _Pointer[_struct.GCP_RESULTSW],  # lpResults
                                   _type.DWORD],  # dwFlags
                                  _type.DWORD]
GetFontUnicodeRanges: _Callable[[_type.HDC,  # hdc
                                 _Pointer[_struct.GLYPHSET]],  # lpgs
                                _type.DWORD]
GetGlyphIndicesA: _Callable[[_type.HDC,  # hdc
                             _type.LPCSTR,  # lpstr
                             _type.c_int,  # c
                             _Pointer[_type.WORD],  # pgi
                             _type.DWORD],  # fl
                            _type.DWORD]
GetGlyphIndicesW: _Callable[[_type.HDC,  # hdc
                             _type.LPCWSTR,  # lpstr
                             _type.c_int,  # c
                             _Pointer[_type.WORD],  # pgi
                             _type.DWORD],  # fl
                            _type.DWORD]
GetTextExtentPointI: _Callable[[_type.HDC,  # hdc
                                _Pointer[_type.WORD],  # pgiIn
                                _type.c_int,  # cgi
                                _Pointer[_struct.SIZE]],  # psize
                               _type.BOOL]
GetTextExtentExPointI: _Callable[[_type.HDC,  # hdc
                                  _Pointer[_type.WORD],  # lpwszString
                                  _type.c_int,  # cwchString
                                  _type.c_int,  # nMaxExtent
                                  _Pointer[_type.c_int],  # lpnFit
                                  _Pointer[_type.c_int],  # lpnDx
                                  _Pointer[_struct.SIZE]],  # lpSize
                                 _type.BOOL]
GetCharWidthI: _Callable[[_type.HDC,  # hdc
                          _type.UINT,  # giFirst
                          _type.UINT,  # cgi
                          _Pointer[_type.WORD],  # pgi
                          _Pointer[_type.c_int]],  # piWidths
                         _type.BOOL]
GetCharABCWidthsI: _Callable[[_type.HDC,  # hdc
                              _type.UINT,  # giFirst
                              _type.UINT,  # cgi
                              _Pointer[_type.WORD],  # pgi
                              _Pointer[_struct.ABC]],  # pabc
                             _type.BOOL]
AddFontResourceExA: _Callable[[_type.LPCSTR,  # name
                               _type.DWORD,  # fl
                               _type.PVOID],  # res
                              _type.c_int]
AddFontResourceExW: _Callable[[_type.LPCWSTR,  # name
                               _type.DWORD,  # fl
                               _type.PVOID],  # res
                              _type.c_int]
RemoveFontResourceExA: _Callable[[_type.LPCSTR,  # name
                                  _type.DWORD,  # fl
                                  _type.PVOID],  # pdv
                                 _type.BOOL]
RemoveFontResourceExW: _Callable[[_type.LPCWSTR,  # name
                                  _type.DWORD,  # fl
                                  _type.PVOID],  # pdv
                                 _type.BOOL]
AddFontMemResourceEx: _Callable[[_type.PVOID,  # pFileView
                                 _type.DWORD,  # cjSize
                                 _type.PVOID,  # pvResrved
                                 _Pointer[_type.DWORD]],  # pNumFonts
                                _type.HANDLE]
RemoveFontMemResourceEx: _Callable[[_type.HANDLE],  # h
                                   _type.BOOL]
CreateFontIndirectExA: _Callable[[_Pointer[_struct.ENUMLOGFONTEXDVA]],
                                 _type.HFONT]
CreateFontIndirectExW: _Callable[[_Pointer[_struct.ENUMLOGFONTEXDVW]],
                                 _type.HFONT]
GetViewportExtEx: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.SIZE]],  # lpsize
                            _type.BOOL]
GetViewportOrgEx: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.POINT]],  # lppoint
                            _type.BOOL]
GetWindowExtEx: _Callable[[_type.HDC,  # hdc
                           _Pointer[_struct.SIZE]],  # lpsize
                          _type.BOOL]
GetWindowOrgEx: _Callable[[_type.HDC,  # hdc
                           _Pointer[_struct.POINT]],  # lppoint
                          _type.BOOL]
IntersectClipRect: _Callable[[_type.HDC,  # hdc
                              _type.c_int,  # left
                              _type.c_int,  # top
                              _type.c_int,  # right
                              _type.c_int],  # bottom
                             _type.c_int]
InvertRgn: _Callable[[_type.HDC,  # hdc
                      _type.HRGN],  # hrgn
                     _type.BOOL]
LineDDA: _Callable[[_type.c_int,  # xStart
                    _type.c_int,  # yStart
                    _type.c_int,  # xEnd
                    _type.c_int,  # yEnd
                    _type.LINEDDAPROC,  # lpProc
                    _type.LPARAM],  # data
                   _type.BOOL]
LineTo: _Callable[[_type.HDC,  # hdc
                   _type.c_int,  # x
                   _type.c_int],  # y
                  _type.BOOL]
MaskBlt: _Callable[[_type.HDC,  # hdcDest
                    _type.c_int,  # xDest
                    _type.c_int,  # yDest
                    _type.c_int,  # width
                    _type.c_int,  # height
                    _type.HDC,  # hdcSrc
                    _type.c_int,  # xSrc
                    _type.c_int,  # ySrc
                    _type.HBITMAP,  # hbmMask
                    _type.c_int,  # xMask
                    _type.c_int,  # yMask
                    _type.DWORD],  # rop
                   _type.BOOL]
PlgBlt: _Callable[[_type.HDC,  # hdcDest
                   _Pointer[_struct.POINT],  # lpPoint
                   _type.HDC,  # hdcSrc
                   _type.c_int,  # xSrc
                   _type.c_int,  # ySrc
                   _type.c_int,  # width
                   _type.c_int,  # height
                   _type.HBITMAP,  # hbmMask
                   _type.c_int,  # xMask
                   _type.c_int],  # yMask
                  _type.BOOL]
OffsetClipRgn: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # x
                          _type.c_int],  # y
                         _type.c_int]
OffsetRgn: _Callable[[_type.HRGN,  # hrgn
                      _type.c_int,  # x
                      _type.c_int],  # y
                     _type.c_int]
PatBlt: _Callable[[_type.HDC,  # hdc
                   _type.c_int,  # x
                   _type.c_int,  # y
                   _type.c_int,  # w
                   _type.c_int,  # h
                   _type.DWORD],  # rop
                  _type.BOOL]
Pie: _Callable[[_type.HDC,  # hdc
                _type.c_int,  # left
                _type.c_int,  # top
                _type.c_int,  # right
                _type.c_int,  # bottom
                _type.c_int,  # xr1
                _type.c_int,  # yr1
                _type.c_int,  # xr2
                _type.c_int],  # yr2
               _type.BOOL]
PlayMetaFile: _Callable[[_type.HDC,  # hdc
                         _type.HMETAFILE],  # hmf
                        _type.BOOL]
PaintRgn: _Callable[[_type.HDC,  # hdc
                     _type.HRGN],  # hrgn
                    _type.BOOL]
PolyPolygon: _Callable[[_type.HDC,  # hdc
                        _Pointer[_struct.POINT],  # apt
                        _Pointer[_type.INT],  # asz
                        _type.c_int],  # csz
                       _type.BOOL]
PtInRegion: _Callable[[_type.HRGN,  # hrgn
                       _type.c_int,  # x
                       _type.c_int],  # y
                      _type.BOOL]
PtVisible: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # x
                      _type.c_int],  # y
                     _type.BOOL]
RectInRegion: _Callable[[_type.HRGN,  # hrgn
                         _Pointer[_struct.RECT]],  # lprect
                        _type.BOOL]
RectVisible: _Callable[[_type.HDC,  # hdc
                        _Pointer[_struct.RECT]],  # lprect
                       _type.BOOL]
Rectangle: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # left
                      _type.c_int,  # top
                      _type.c_int,  # right
                      _type.c_int],  # bottom
                     _type.BOOL]
RestoreDC: _Callable[[_type.HDC,  # hdc
                      _type.c_int],  # nSavedDC
                     _type.BOOL]
ResetDCA: _Callable[[_type.HDC,  # hdc
                     _Pointer[_struct.DEVMODEA]],  # lpdm
                    _type.HDC]
ResetDCW: _Callable[[_type.HDC,  # hdc
                     _Pointer[_struct.DEVMODEW]],  # lpdm
                    _type.HDC]
RealizePalette: _Callable[[_type.HDC],  # hdc
                          _type.UINT]
RemoveFontResourceA: _Callable[[_type.LPCSTR],  # lpFileName
                               _type.BOOL]
RemoveFontResourceW: _Callable[[_type.LPCWSTR],  # lpFileName
                               _type.BOOL]
RoundRect: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # left
                      _type.c_int,  # top
                      _type.c_int,  # right
                      _type.c_int,  # bottom
                      _type.c_int,  # width
                      _type.c_int],  # height
                     _type.BOOL]
ResizePalette: _Callable[[_type.HPALETTE,  # hpal
                          _type.UINT],  # n
                         _type.BOOL]
SaveDC: _Callable[[_type.HDC],  # hdc
                  _type.c_int]
SelectClipRgn: _Callable[[_type.HDC,  # hdc
                          _type.HRGN],  # hrgn
                         _type.c_int]
ExtSelectClipRgn: _Callable[[_type.HDC,  # hdc
                             _type.HRGN,  # hrgn
                             _type.c_int],  # mode
                            _type.c_int]
SetMetaRgn: _Callable[[_type.HDC],  # hdc
                      _type.c_int]
SelectObject: _Callable[[_type.HDC,  # hdc
                         _type.HGDIOBJ],  # h
                        _type.HGDIOBJ]
SelectPalette: _Callable[[_type.HDC,  # hdc
                          _type.HPALETTE,  # hPal
                          _type.BOOL],  # bForceBkgd
                         _type.HPALETTE]
SetBkColor: _Callable[[_type.HDC,  # hdc
                       _type.COLORREF],  # color
                      _type.COLORREF]
SetDCBrushColor: _Callable[[_type.HDC,  # hdc
                            _type.COLORREF],  # color
                           _type.COLORREF]
SetDCPenColor: _Callable[[_type.HDC,  # hdc
                          _type.COLORREF],  # color
                         _type.COLORREF]
SetBkMode: _Callable[[_type.HDC,  # hdc
                      _type.c_int],  # mode
                     _type.c_int]
SetBitmapBits: _Callable[[_type.HBITMAP,  # hbm
                          _type.DWORD,  # cb
                          _type.c_void_p],  # pvBits
                         _type.LONG]
SetBoundsRect: _Callable[[_type.HDC,  # hdc
                          _Pointer[_struct.RECT],  # lprect
                          _type.UINT],  # flags
                         _type.UINT]
SetDIBits: _Callable[[_type.HDC,  # hdc
                      _type.HBITMAP,  # hbm
                      _type.UINT,  # start
                      _type.UINT,  # cLines
                      _type.c_void_p,  # lpBits
                      _Pointer[_struct.BITMAPINFO],  # lpbmi
                      _type.UINT],  # ColorUse
                     _type.c_int]
SetDIBitsToDevice: _Callable[[_type.HDC,  # hdc
                              _type.c_int,  # xDest
                              _type.c_int,  # yDest
                              _type.DWORD,  # w
                              _type.DWORD,  # h
                              _type.c_int,  # xSrc
                              _type.c_int,  # ySrc
                              _type.UINT,  # StartScan
                              _type.UINT,  # cLines
                              _type.c_void_p,  # lpvBits
                              _Pointer[_struct.BITMAPINFO],  # lpbmi
                              _type.UINT],  # ColorUse
                             _type.c_int]
SetMapperFlags: _Callable[[_type.HDC,  # hdc
                           _type.DWORD],  # flags
                          _type.DWORD]
SetGraphicsMode: _Callable[[_type.HDC,  # hdc
                            _type.c_int],  # iMode
                           _type.c_int]
SetMapMode: _Callable[[_type.HDC,  # hdc
                       _type.c_int],  # iMode
                      _type.c_int]
SetLayout: _Callable[[_type.HDC,  # hdc
                      _type.DWORD],  # l
                     _type.DWORD]
GetLayout: _Callable[[_type.HDC],  # hdc
                     _type.DWORD]
SetMetaFileBitsEx: _Callable[[_type.UINT,  # cbBuffer
                              _Pointer[_type.BYTE]],  # lpData
                             _type.HMETAFILE]
SetPaletteEntries: _Callable[[_type.HPALETTE,  # hpal
                              _type.UINT,  # iStart
                              _type.UINT,  # cEntries
                              _Pointer[_struct.PALETTEENTRY]],  # pPalEntries
                             _type.UINT]
SetPixel: _Callable[[_type.HDC,  # hdc
                     _type.c_int,  # x
                     _type.c_int,  # y
                     _type.COLORREF],  # color
                    _type.COLORREF]
SetPixelV: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # x
                      _type.c_int,  # y
                      _type.COLORREF],  # color
                     _type.BOOL]
SetPixelFormat: _Callable[[_type.HDC,  # hdc
                           _type.c_int,  # format
                           _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                          _type.BOOL]
SetPolyFillMode: _Callable[[_type.HDC,  # hdc
                            _type.c_int],  # mode
                           _type.c_int]
StretchBlt: _Callable[[_type.HDC,  # hdcDest
                       _type.c_int,  # xDest
                       _type.c_int,  # yDest
                       _type.c_int,  # wDest
                       _type.c_int,  # hDest
                       _type.HDC,  # hdcSrc
                       _type.c_int,  # xSrc
                       _type.c_int,  # ySrc
                       _type.c_int,  # wSrc
                       _type.c_int,  # hSrc
                       _type.DWORD],  # rop
                      _type.BOOL]
SetRectRgn: _Callable[[_type.HRGN,  # hrgn
                       _type.c_int,  # left
                       _type.c_int,  # top
                       _type.c_int,  # right
                       _type.c_int],  # bottom
                      _type.BOOL]
StretchDIBits: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # xDest
                          _type.c_int,  # yDest
                          _type.c_int,  # DestWidth
                          _type.c_int,  # DestHeight
                          _type.c_int,  # xSrc
                          _type.c_int,  # ySrc
                          _type.c_int,  # SrcWidth
                          _type.c_int,  # SrcHeight
                          _type.c_void_p,  # lpBits
                          _Pointer[_struct.BITMAPINFO],  # lpbmi
                          _type.UINT,  # iUsage
                          _type.DWORD],  # rop
                         _type.c_int]
SetROP2: _Callable[[_type.HDC,  # hdc
                    _type.c_int],  # rop2
                   _type.c_int]
SetStretchBltMode: _Callable[[_type.HDC,  # hdc
                              _type.c_int],  # mode
                             _type.c_int]
SetSystemPaletteUse: _Callable[[_type.HDC,  # hdc
                                _type.UINT],  # use
                               _type.UINT]
SetTextCharacterExtra: _Callable[[_type.HDC,  # hdc
                                  _type.c_int],  # extra
                                 _type.c_int]
SetTextColor: _Callable[[_type.HDC,  # hdc
                         _type.COLORREF],  # color
                        _type.COLORREF]
SetTextAlign: _Callable[[_type.HDC,  # hdc
                         _type.UINT],  # align
                        _type.UINT]
SetTextJustification: _Callable[[_type.HDC,  # hdc
                                 _type.c_int,  # extra
                                 _type.c_int],  # count
                                _type.BOOL]
UpdateColors: _Callable[[_type.HDC],  # hdc
                        _type.BOOL]
AlphaBlend: _Callable[[_type.HDC,  # hdcDest
                       _type.c_int,  # xoriginDest
                       _type.c_int,  # yoriginDest
                       _type.c_int,  # wDest
                       _type.c_int,  # hDest
                       _type.HDC,  # hdcSrc
                       _type.c_int,  # xoriginSrc
                       _type.c_int,  # yoriginSrc
                       _type.c_int,  # wSrc
                       _type.c_int,  # hSrc
                       _struct.BLENDFUNCTION],  # ftn
                      _type.BOOL]
TransparentBlt: _Callable[[_type.HDC,  # hdcDest
                           _type.c_int,  # xoriginDest
                           _type.c_int,  # yoriginDest
                           _type.c_int,  # wDest
                           _type.c_int,  # hDest
                           _type.HDC,  # hdcSrc
                           _type.c_int,  # xoriginSrc
                           _type.c_int,  # yoriginSrc
                           _type.c_int,  # wSrc
                           _type.c_int,  # hSrc
                           _type.UINT],  # crTransparent
                          _type.BOOL]
GradientFill: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.TRIVERTEX],  # pVertex
                         _type.ULONG,  # nVertex
                         _type.PVOID,  # pMesh
                         _type.ULONG,  # nMesh
                         _type.ULONG],  # ulMode
                        _type.BOOL]
GdiAlphaBlend: _Callable[[_type.HDC,  # hdcDest
                          _type.c_int,  # xoriginDest
                          _type.c_int,  # yoriginDest
                          _type.c_int,  # wDest
                          _type.c_int,  # hDest
                          _type.HDC,  # hdcSrc
                          _type.c_int,  # xoriginSrc
                          _type.c_int,  # yoriginSrc
                          _type.c_int,  # wSrc
                          _type.c_int,  # hSrc
                          _struct.BLENDFUNCTION],  # ftn
                         _type.BOOL]
GdiTransparentBlt: _Callable[[_type.HDC,  # hdcDest
                              _type.c_int,  # xoriginDest
                              _type.c_int,  # yoriginDest
                              _type.c_int,  # wDest
                              _type.c_int,  # hDest
                              _type.HDC,  # hdcSrc
                              _type.c_int,  # xoriginSrc
                              _type.c_int,  # yoriginSrc
                              _type.c_int,  # wSrc
                              _type.c_int,  # hSrc
                              _type.UINT],  # crTransparent
                             _type.BOOL]
GdiGradientFill: _Callable[[_type.HDC,  # hdc
                            _Pointer[_struct.TRIVERTEX],  # pVertex
                            _type.ULONG,  # nVertex
                            _type.PVOID,  # pMesh
                            _type.ULONG,  # nCount
                            _type.ULONG],  # ulMode
                           _type.BOOL]
PlayMetaFileRecord: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.HANDLETABLE],  # lpHandleTable
                               _Pointer[_struct.METARECORD],  # lpMR
                               _type.UINT],  # noObjs
                              _type.BOOL]
# EnumMetaFile: _Callable[[_type.HDC,  # hdc
#                          _type.HMETAFILE,  # hmf
#                          MFENUMPROC,  # proc
#                          _type.LPARAM],  # param
#                         _type.BOOL]
CloseEnhMetaFile: _Callable[[_type.HDC],  # hdc
                            _type.HENHMETAFILE]
CopyEnhMetaFileA: _Callable[[_type.HENHMETAFILE,  # hEnh
                             _type.LPCSTR],  # lpFileName
                            _type.HENHMETAFILE]
CopyEnhMetaFileW: _Callable[[_type.HENHMETAFILE,  # hEnh
                             _type.LPCWSTR],  # lpFileName
                            _type.HENHMETAFILE]
CreateEnhMetaFileA: _Callable[[_type.HDC,  # hdc
                               _type.LPCSTR,  # lpFilename
                               _Pointer[_struct.RECT],  # lprc
                               _type.LPCSTR],  # lpDesc
                              _type.HDC]
CreateEnhMetaFileW: _Callable[[_type.HDC,  # hdc
                               _type.LPCWSTR,  # lpFilename
                               _Pointer[_struct.RECT],  # lprc
                               _type.LPCWSTR],  # lpDesc
                              _type.HDC]
DeleteEnhMetaFile: _Callable[[_type.HENHMETAFILE],  # hmf
                             _type.BOOL]
# EnumEnhMetaFile: _Callable[[_type.HDC,  # hdc
#                             _type.HENHMETAFILE,  # hmf
#                             ENHMFENUMPROC,  # proc
#                             _type.LPVOID,  # param
#                             _Pointer[_struct.RECT]],  # lpRect
#                            _type.BOOL]
GetEnhMetaFileA: _Callable[[_type.LPCSTR],  # lpName
                           _type.HENHMETAFILE]
GetEnhMetaFileW: _Callable[[_type.LPCWSTR],  # lpName
                           _type.HENHMETAFILE]
GetEnhMetaFileBits: _Callable[[_type.HENHMETAFILE,  # hEMF
                               _type.UINT,  # nSize
                               _Pointer[_type.BYTE]],  # lpData
                              _type.UINT]
GetEnhMetaFileDescriptionA: _Callable[[_type.HENHMETAFILE,  # hemf
                                       _type.UINT,  # cchBuffer
                                       _type.LPSTR],  # lpDescription
                                      _type.UINT]
GetEnhMetaFileDescriptionW: _Callable[[_type.HENHMETAFILE,  # hemf
                                       _type.UINT,  # cchBuffer
                                       _type.LPWSTR],  # lpDescription
                                      _type.UINT]
GetEnhMetaFileHeader: _Callable[[_type.HENHMETAFILE,  # hemf
                                 _type.UINT,  # nSize
                                 _Pointer[_struct.ENHMETAHEADER]],  # lpEnhMetaHeader
                                _type.UINT]
GetEnhMetaFilePaletteEntries: _Callable[[_type.HENHMETAFILE,  # hemf
                                         _type.UINT,  # nNumEntries
                                         _Pointer[_struct.PALETTEENTRY]],  # lpPaletteEntries
                                        _type.UINT]
GetEnhMetaFilePixelFormat: _Callable[[_type.HENHMETAFILE,  # hemf
                                      _type.UINT,  # cbBuffer
                                      _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                                     _type.UINT]
GetWinMetaFileBits: _Callable[[_type.HENHMETAFILE,  # hemf
                               _type.UINT,  # cbData16
                               _Pointer[_type.BYTE],  # pData16
                               _type.INT,  # iMapMode
                               _type.HDC],  # hdcRef
                              _type.UINT]
PlayEnhMetaFile: _Callable[[_type.HDC,  # hdc
                            _type.HENHMETAFILE,  # hmf
                            _Pointer[_struct.RECT]],  # lprect
                           _type.BOOL]
PlayEnhMetaFileRecord: _Callable[[_type.HDC,  # hdc
                                  _Pointer[_struct.HANDLETABLE],  # pht
                                  _Pointer[_struct.ENHMETARECORD],  # pmr
                                  _type.UINT],  # cht
                                 _type.BOOL]
SetEnhMetaFileBits: _Callable[[_type.UINT,  # nSize
                               _Pointer[_type.BYTE]],  # pb
                              _type.HENHMETAFILE]
SetWinMetaFileBits: _Callable[[_type.UINT,  # nSize
                               _Pointer[_type.BYTE],  # lpMeta16Data
                               _type.HDC,  # hdcRef
                               _Pointer[_struct.METAFILEPICT]],  # lpMFP
                              _type.HENHMETAFILE]
GdiComment: _Callable[[_type.HDC,  # hdc
                       _type.UINT,  # nSize
                       _Pointer[_type.BYTE]],  # lpData
                      _type.BOOL]
GetTextMetricsA: _Callable[[_type.HDC,  # hdc
                            _Pointer[_struct.TEXTMETRICA]],  # lptm
                           _type.BOOL]
GetTextMetricsW: _Callable[[_type.HDC,  # hdc
                            _Pointer[_struct.TEXTMETRICW]],  # lptm
                           _type.BOOL]
AngleArc: _Callable[[_type.HDC,  # hdc
                     _type.c_int,  # x
                     _type.c_int,  # y
                     _type.DWORD,  # r
                     _type.FLOAT,  # StartAngle
                     _type.FLOAT],  # SweepAngle
                    _type.BOOL]
PolyPolyline: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.POINT],  # apt
                         _Pointer[_type.DWORD],  # asz
                         _type.DWORD],  # csz
                        _type.BOOL]
GetWorldTransform: _Callable[[_type.HDC,  # hdc
                              _Pointer[_struct.XFORM]],  # lpxf
                             _type.BOOL]
SetWorldTransform: _Callable[[_type.HDC,  # hdc
                              _Pointer[_struct.XFORM]],  # lpxf
                             _type.BOOL]
ModifyWorldTransform: _Callable[[_type.HDC,  # hdc
                                 _Pointer[_struct.XFORM],  # lpxf
                                 _type.DWORD],  # mode
                                _type.BOOL]
CombineTransform: _Callable[[_Pointer[_struct.XFORM],  # lpxfOut
                             _Pointer[_struct.XFORM],  # lpxf1
                             _Pointer[_struct.XFORM]],  # lpxf2
                            _type.BOOL]
CreateDIBSection: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.BITMAPINFO],  # pbmi
                             _type.UINT,  # usage
                             _type.c_void_p,  # ppvBits
                             _type.HANDLE,  # hSection
                             _type.DWORD],  # offset
                            _type.HBITMAP]
GetDIBColorTable: _Callable[[_type.HDC,  # hdc
                             _type.UINT,  # iStart
                             _type.UINT,  # cEntries
                             _Pointer[_struct.RGBQUAD]],  # prgbq
                            _type.UINT]
SetDIBColorTable: _Callable[[_type.HDC,  # hdc
                             _type.UINT,  # iStart
                             _type.UINT,  # cEntries
                             _Pointer[_struct.RGBQUAD]],  # prgbq
                            _type.UINT]
SetColorAdjustment: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.COLORADJUSTMENT]],  # lpca
                              _type.BOOL]
GetColorAdjustment: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.COLORADJUSTMENT]],  # lpca
                              _type.BOOL]
CreateHalftonePalette: _Callable[[_type.HDC],  # hdc
                                 _type.HPALETTE]
StartDocA: _Callable[[_type.HDC,  # hdc
                      _Pointer[_struct.DOCINFOA]],  # lpdi
                     _type.c_int]
StartDocW: _Callable[[_type.HDC,  # hdc
                      _Pointer[_struct.DOCINFOW]],  # lpdi
                     _type.c_int]
EndDoc: _Callable[[_type.HDC],  # hdc
                  _type.c_int]
StartPage: _Callable[[_type.HDC],  # hdc
                     _type.c_int]
EndPage: _Callable[[_type.HDC],  # hdc
                   _type.c_int]
AbortDoc: _Callable[[_type.HDC],  # hdc
                    _type.c_int]
SetAbortProc: _Callable[[_type.HDC,  # hdc
                         _type.ABORTPROC],  # proc
                        _type.c_int]
AbortPath: _Callable[[_type.HDC],  # hdc
                     _type.BOOL]
ArcTo: _Callable[[_type.HDC,  # hdc
                  _type.c_int,  # left
                  _type.c_int,  # top
                  _type.c_int,  # right
                  _type.c_int,  # bottom
                  _type.c_int,  # xr1
                  _type.c_int,  # yr1
                  _type.c_int,  # xr2
                  _type.c_int],  # yr2
                 _type.BOOL]
BeginPath: _Callable[[_type.HDC],  # hdc
                     _type.BOOL]
CloseFigure: _Callable[[_type.HDC],  # hdc
                       _type.BOOL]
EndPath: _Callable[[_type.HDC],  # hdc
                   _type.BOOL]
FillPath: _Callable[[_type.HDC],  # hdc
                    _type.BOOL]
FlattenPath: _Callable[[_type.HDC],  # hdc
                       _type.BOOL]
GetPath: _Callable[[_type.HDC,  # hdc
                    _Pointer[_struct.POINT],  # apt
                    _Pointer[_type.BYTE],  # aj
                    _type.c_int],  # cpt
                   _type.c_int]
PathToRegion: _Callable[[_type.HDC],  # hdc
                        _type.HRGN]
PolyDraw: _Callable[[_type.HDC,  # hdc
                     _Pointer[_struct.POINT],  # apt
                     _Pointer[_type.BYTE],  # aj
                     _type.c_int],  # cpt
                    _type.BOOL]
SelectClipPath: _Callable[[_type.HDC,  # hdc
                           _type.c_int],  # mode
                          _type.BOOL]
SetArcDirection: _Callable[[_type.HDC,  # hdc
                            _type.c_int],  # dir
                           _type.c_int]
SetMiterLimit: _Callable[[_type.HDC,  # hdc
                          _type.FLOAT,  # limit
                          _Pointer[_type.FLOAT]],  # old
                         _type.BOOL]
StrokeAndFillPath: _Callable[[_type.HDC],  # hdc
                             _type.BOOL]
StrokePath: _Callable[[_type.HDC],  # hdc
                      _type.BOOL]
WidenPath: _Callable[[_type.HDC],  # hdc
                     _type.BOOL]
ExtCreatePen: _Callable[[_type.DWORD,  # iPenStyle
                         _type.DWORD,  # cWidth
                         _Pointer[_struct.LOGBRUSH],  # plbrush
                         _type.DWORD,  # cStyle
                         _Pointer[_type.DWORD]],  # pstyle
                        _type.HPEN]
GetMiterLimit: _Callable[[_type.HDC,  # hdc
                          _Pointer[_type.FLOAT]],  # plimit
                         _type.BOOL]
GetArcDirection: _Callable[[_type.HDC],  # hdc
                           _type.c_int]
GetObjectA: _Callable[[_type.HANDLE,  # h
                       _type.c_int,  # c
                       _type.LPVOID],  # pv
                      _type.c_int]
GetObjectW: _Callable[[_type.HANDLE,  # h
                       _type.c_int,  # c
                       _type.LPVOID],  # pv
                      _type.c_int]
MoveToEx: _Callable[[_type.HDC,  # hdc
                     _type.c_int,  # x
                     _type.c_int,  # y
                     _Pointer[_struct.POINT]],  # lppt
                    _type.BOOL]
TextOutA: _Callable[[_type.HDC,  # hdc
                     _type.c_int,  # x
                     _type.c_int,  # y
                     _type.LPCSTR,  # lpString
                     _type.c_int],  # c
                    _type.BOOL]
TextOutW: _Callable[[_type.HDC,  # hdc
                     _type.c_int,  # x
                     _type.c_int,  # y
                     _type.LPCWSTR,  # lpString
                     _type.c_int],  # c
                    _type.BOOL]
ExtTextOutA: _Callable[[_type.HDC,  # hdc
                        _type.c_int,  # x
                        _type.c_int,  # y
                        _type.UINT,  # options
                        _Pointer[_struct.RECT],  # lprect
                        _type.LPCSTR,  # lpString
                        _type.UINT,  # c
                        _Pointer[_type.INT]],  # lpDx
                       _type.BOOL]
ExtTextOutW: _Callable[[_type.HDC,  # hdc
                        _type.c_int,  # x
                        _type.c_int,  # y
                        _type.UINT,  # options
                        _Pointer[_struct.RECT],  # lprect
                        _type.LPCWSTR,  # lpString
                        _type.UINT,  # c
                        _Pointer[_type.INT]],  # lpDx
                       _type.BOOL]
PolyTextOutA: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.POLYTEXTA],  # ppt
                         _type.c_int],  # nstrings
                        _type.BOOL]
PolyTextOutW: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.POLYTEXTW],  # ppt
                         _type.c_int],  # nstrings
                        _type.BOOL]
CreatePolygonRgn: _Callable[[_Pointer[_struct.POINT],  # pptl
                             _type.c_int,  # cPoint
                             _type.c_int],  # iMode
                            _type.HRGN]
DPtoLP: _Callable[[_type.HDC,  # hdc
                   _Pointer[_struct.POINT],  # lppt
                   _type.c_int],  # c
                  _type.BOOL]
LPtoDP: _Callable[[_type.HDC,  # hdc
                   _Pointer[_struct.POINT],  # lppt
                   _type.c_int],  # c
                  _type.BOOL]
Polygon: _Callable[[_type.HDC,  # hdc
                    _Pointer[_struct.POINT],  # apt
                    _type.c_int],  # cpt
                   _type.BOOL]
Polyline: _Callable[[_type.HDC,  # hdc
                     _Pointer[_struct.POINT],  # apt
                     _type.c_int],  # cpt
                    _type.BOOL]
PolyBezier: _Callable[[_type.HDC,  # hdc
                       _Pointer[_struct.POINT],  # apt
                       _type.DWORD],  # cpt
                      _type.BOOL]
PolyBezierTo: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.POINT],  # apt
                         _type.DWORD],  # cpt
                        _type.BOOL]
PolylineTo: _Callable[[_type.HDC,  # hdc
                       _Pointer[_struct.POINT],  # apt
                       _type.DWORD],  # cpt
                      _type.BOOL]
SetViewportExtEx: _Callable[[_type.HDC,  # hdc
                             _type.c_int,  # x
                             _type.c_int,  # y
                             _Pointer[_struct.SIZE]],  # lpsz
                            _type.BOOL]
SetViewportOrgEx: _Callable[[_type.HDC,  # hdc
                             _type.c_int,  # x
                             _type.c_int,  # y
                             _Pointer[_struct.POINT]],  # lppt
                            _type.BOOL]
SetWindowExtEx: _Callable[[_type.HDC,  # hdc
                           _type.c_int,  # x
                           _type.c_int,  # y
                           _Pointer[_struct.SIZE]],  # lpsz
                          _type.BOOL]
SetWindowOrgEx: _Callable[[_type.HDC,  # hdc
                           _type.c_int,  # x
                           _type.c_int,  # y
                           _Pointer[_struct.POINT]],  # lppt
                          _type.BOOL]
OffsetViewportOrgEx: _Callable[[_type.HDC,  # hdc
                                _type.c_int,  # x
                                _type.c_int,  # y
                                _Pointer[_struct.POINT]],  # lppt
                               _type.BOOL]
OffsetWindowOrgEx: _Callable[[_type.HDC,  # hdc
                              _type.c_int,  # x
                              _type.c_int,  # y
                              _Pointer[_struct.POINT]],  # lppt
                             _type.BOOL]
ScaleViewportExtEx: _Callable[[_type.HDC,  # hdc
                               _type.c_int,  # xn
                               _type.c_int,  # dx
                               _type.c_int,  # yn
                               _type.c_int,  # yd
                               _Pointer[_struct.SIZE]],  # lpsz
                              _type.BOOL]
ScaleWindowExtEx: _Callable[[_type.HDC,  # hdc
                             _type.c_int,  # xn
                             _type.c_int,  # xd
                             _type.c_int,  # yn
                             _type.c_int,  # yd
                             _Pointer[_struct.SIZE]],  # lpsz
                            _type.BOOL]
SetBitmapDimensionEx: _Callable[[_type.HBITMAP,  # hbm
                                 _type.c_int,  # w
                                 _type.c_int,  # h
                                 _Pointer[_struct.SIZE]],  # lpsz
                                _type.BOOL]
SetBrushOrgEx: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # x
                          _type.c_int,  # y
                          _Pointer[_struct.POINT]],  # lppt
                         _type.BOOL]
GetTextFaceA: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # c
                         _type.LPSTR],  # lpName
                        _type.c_int]
GetTextFaceW: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # c
                         _type.LPWSTR],  # lpName
                        _type.c_int]
GetKerningPairsA: _Callable[[_type.HDC,  # hdc
                             _type.DWORD,  # nPairs
                             _Pointer[_struct.KERNINGPAIR]],  # lpKernPair
                            _type.DWORD]
GetKerningPairsW: _Callable[[_type.HDC,  # hdc
                             _type.DWORD,  # nPairs
                             _Pointer[_struct.KERNINGPAIR]],  # lpKernPair
                            _type.DWORD]
GetDCOrgEx: _Callable[[_type.HDC,  # hdc
                       _Pointer[_struct.POINT]],  # lppt
                      _type.BOOL]
FixBrushOrgEx: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # x
                          _type.c_int,  # y
                          _Pointer[_struct.POINT]],  # ptl
                         _type.BOOL]
UnrealizeObject: _Callable[[_type.HGDIOBJ],  # h
                           _type.BOOL]
GdiFlush: _Callable[[],
                    _type.BOOL]
GdiSetBatchLimit: _Callable[[_type.DWORD],  # dw
                            _type.DWORD]
GdiGetBatchLimit: _Callable[[],
                            _type.DWORD]
SetICMMode: _Callable[[_type.HDC,  # hdc
                       _type.c_int],  # mode
                      _type.c_int]
CheckColorsInGamut: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.RGBTRIPLE],  # lpRGBTriple
                               _type.LPVOID,  # dlpBuffer
                               _type.DWORD],  # nCount
                              _type.BOOL]
GetColorSpace: _Callable[[_type.HDC],  # hdc
                         _type.HCOLORSPACE]
GetLogColorSpaceA: _Callable[[_type.HCOLORSPACE,  # hColorSpace
                              _Pointer[_struct.LOGCOLORSPACEA],  # lpBuffer
                              _type.DWORD],  # nSize
                             _type.BOOL]
GetLogColorSpaceW: _Callable[[_type.HCOLORSPACE,  # hColorSpace
                              _Pointer[_struct.LOGCOLORSPACEW],  # lpBuffer
                              _type.DWORD],  # nSize
                             _type.BOOL]
CreateColorSpaceA: _Callable[[_Pointer[_struct.LOGCOLORSPACEA]],  # lplcs
                             _type.HCOLORSPACE]
CreateColorSpaceW: _Callable[[_Pointer[_struct.LOGCOLORSPACEW]],  # lplcs
                             _type.HCOLORSPACE]
SetColorSpace: _Callable[[_type.HDC,  # hdc
                          _type.HCOLORSPACE],  # hcs
                         _type.HCOLORSPACE]
DeleteColorSpace: _Callable[[_type.HCOLORSPACE],  # hcs
                            _type.BOOL]
GetICMProfileA: _Callable[[_type.HDC,  # hdc
                           _Pointer[_type.DWORD],  # pBufSize
                           _type.LPSTR],  # pszFilename
                          _type.BOOL]
GetICMProfileW: _Callable[[_type.HDC,  # hdc
                           _Pointer[_type.DWORD],  # pBufSize
                           _type.LPWSTR],  # pszFilename
                          _type.BOOL]
SetICMProfileA: _Callable[[_type.HDC,  # hdc
                           _type.LPSTR],  # lpFileName
                          _type.BOOL]
SetICMProfileW: _Callable[[_type.HDC,  # hdc
                           _type.LPWSTR],  # lpFileName
                          _type.BOOL]
GetDeviceGammaRamp: _Callable[[_type.HDC,  # hdc
                               _type.LPVOID],  # lpRamp
                              _type.BOOL]
SetDeviceGammaRamp: _Callable[[_type.HDC,  # hdc
                               _type.LPVOID],  # lpRamp
                              _type.BOOL]
ColorMatchToTarget: _Callable[[_type.HDC,  # hdc
                               _type.HDC,  # hdcTarget
                               _type.DWORD],  # action
                              _type.BOOL]
EnumICMProfilesA: _Callable[[_type.HDC,  # hdc
                             _type.ICMENUMPROCA,  # proc
                             _type.LPARAM],  # param
                            _type.c_int]
EnumICMProfilesW: _Callable[[_type.HDC,  # hdc
                             _type.ICMENUMPROCW,  # proc
                             _type.LPARAM],  # param
                            _type.c_int]
UpdateICMRegKeyA: _Callable[[_type.DWORD,  # reserved
                             _type.LPSTR,  # lpszCMID
                             _type.LPSTR,  # lpszFileName
                             _type.UINT],  # command
                            _type.BOOL]
UpdateICMRegKeyW: _Callable[[_type.DWORD,  # reserved
                             _type.LPWSTR,  # lpszCMID
                             _type.LPWSTR,  # lpszFileName
                             _type.UINT],  # command
                            _type.BOOL]
ColorCorrectPalette: _Callable[[_type.HDC,  # hdc
                                _type.HPALETTE,  # hPal
                                _type.DWORD,  # deFirst
                                _type.DWORD],  # num
                               _type.BOOL]
wglCopyContext: _Callable[[_type.HGLRC,
                           _type.HGLRC,
                           _type.UINT],
                          _type.BOOL]
wglCreateContext: _Callable[[_type.HDC],
                            _type.HGLRC]
wglCreateLayerContext: _Callable[[_type.HDC,
                                  _type.c_int],
                                 _type.HGLRC]
wglDeleteContext: _Callable[[_type.HGLRC],
                            _type.BOOL]
wglGetCurrentContext: _Callable[[],
                                _type.HGLRC]
wglGetCurrentDC: _Callable[[],
                           _type.HDC]
wglGetProcAddress: _Callable[[_type.LPCSTR],
                             _type.PROC]
wglMakeCurrent: _Callable[[_type.HDC,
                           _type.HGLRC],
                          _type.BOOL]
wglShareLists: _Callable[[_type.HGLRC,
                          _type.HGLRC],
                         _type.BOOL]
wglUseFontBitmapsA: _Callable[[_type.HDC,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD],
                              _type.BOOL]
wglUseFontBitmapsW: _Callable[[_type.HDC,
                               _type.DWORD,
                               _type.DWORD,
                               _type.DWORD],
                              _type.BOOL]
SwapBuffers: _Callable[[_type.HDC],
                       _type.BOOL]
wglUseFontOutlinesA: _Callable[[_type.HDC,
                                _type.DWORD,
                                _type.DWORD,
                                _type.DWORD,
                                _type.FLOAT,
                                _type.FLOAT,
                                _type.c_int,
                                _Pointer[_struct.GLYPHMETRICSFLOAT]],
                               _type.BOOL]
wglUseFontOutlinesW: _Callable[[_type.HDC,
                                _type.DWORD,
                                _type.DWORD,
                                _type.DWORD,
                                _type.FLOAT,
                                _type.FLOAT,
                                _type.c_int,
                                _Pointer[_struct.GLYPHMETRICSFLOAT]],
                               _type.BOOL]
wglDescribeLayerPlane: _Callable[[_type.HDC,
                                  _type.c_int,
                                  _type.c_int,
                                  _type.UINT,
                                  _Pointer[_struct.LAYERPLANEDESCRIPTOR]],
                                 _type.BOOL]
wglSetLayerPaletteEntries: _Callable[[_type.HDC,
                                      _type.c_int,
                                      _type.c_int,
                                      _type.c_int,
                                      _Pointer[_type.COLORREF]],
                                     _type.c_int]
wglGetLayerPaletteEntries: _Callable[[_type.HDC,
                                      _type.c_int,
                                      _type.c_int,
                                      _type.c_int,
                                      _Pointer[_type.COLORREF]],
                                     _type.c_int]
wglRealizeLayerPalette: _Callable[[_type.HDC,
                                   _type.c_int,
                                   _type.BOOL],
                                  _type.BOOL]
wglSwapLayerBuffers: _Callable[[_type.HDC,
                                _type.UINT],
                               _type.BOOL]
wglSwapMultipleBuffers: _Callable[[_type.UINT,
                                   _Pointer[_struct.WGLSWAP]],
                                  _type.DWORD]

_WinLib(__name__)
