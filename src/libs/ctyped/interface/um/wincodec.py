from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import d2d1 as _d2d1
from . import d2d1_1 as _d2d1_1
from . import objidlbase as _objidlbase
from . import ocidl as _ocidl
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IWICPalette(_Unknwnbase.IUnknown):
    InitializePredefined: _Callable[[_enum.WICBitmapPaletteType,  # ePaletteType
                                     _type.BOOL],  # fAddTransparentColor
                                    _type.HRESULT]
    InitializeCustom: _Callable[[_Pointer[_type.WICColor],  # pColors
                                 _type.UINT],  # cCount
                                _type.HRESULT]
    InitializeFromBitmap: _Callable[[IWICBitmapSource,  # pISurface
                                     _type.UINT,  # cCount
                                     _type.BOOL],  # fAddTransparentColor
                                    _type.HRESULT]
    InitializeFromPalette: _Callable[[IWICPalette],  # pIPalette
                                     _type.HRESULT]
    GetType: _Callable[[_Pointer[_enum.WICBitmapPaletteType]],  # pePaletteType
                       _type.HRESULT]
    GetColorCount: _Callable[[_Pointer[_type.UINT]],  # pcCount
                             _type.HRESULT]
    GetColors: _Callable[[_type.UINT,  # cCount
                          _Pointer[_type.WICColor],  # pColors
                          _Pointer[_type.UINT]],  # pcActualColors
                         _type.HRESULT]
    IsBlackWhite: _Callable[[_Pointer[_type.BOOL]],  # pfIsBlackWhite
                            _type.HRESULT]
    IsGrayscale: _Callable[[_Pointer[_type.BOOL]],  # pfIsGrayscale
                           _type.HRESULT]
    HasAlpha: _Callable[[_Pointer[_type.BOOL]],  # pfHasAlpha
                        _type.HRESULT]


class IWICBitmapSource(_Unknwnbase.IUnknown):
    GetSize: _Callable[[_Pointer[_type.UINT],  # puiWidth
                        _Pointer[_type.UINT]],  # puiHeight
                       _type.HRESULT]
    GetPixelFormat: _Callable[[_Pointer[_struct.WICPixelFormatGUID]],  # pPixelFormat
                              _type.HRESULT]
    GetResolution: _Callable[[_Pointer[_type.c_double],  # pDpiX
                              _Pointer[_type.c_double]],  # pDpiY
                             _type.HRESULT]
    CopyPalette: _Callable[[IWICPalette],  # pIPalette
                           _type.HRESULT]
    CopyPixels: _Callable[[_Pointer[_struct.WICRect],  # prc
                           _type.UINT,  # cbStride
                           _type.UINT,  # cbBufferSize
                           _Pointer[_type.BYTE]],  # pbBuffer
                          _type.HRESULT]


class IWICFormatConverter(IWICBitmapSource):
    Initialize: _Callable[[IWICBitmapSource,  # pISource
                           _Pointer[_struct.GUID],  # dstFormat
                           _enum.WICBitmapDitherType,  # dither
                           IWICPalette,  # pIPalette
                           _type.c_double,  # alphaThresholdPercent
                           _enum.WICBitmapPaletteType],  # paletteTranslate
                          _type.HRESULT]
    CanConvert: _Callable[[_Pointer[_struct.GUID],  # srcPixelFormat
                           _Pointer[_struct.GUID],  # dstPixelFormat
                           _Pointer[_type.BOOL]],  # pfCanConvert
                          _type.HRESULT]


class IWICPlanarFormatConverter(IWICBitmapSource):
    Initialize: _Callable[[_Pointer[IWICBitmapSource],  # ppPlanes
                           _type.UINT,  # cPlanes
                           _Pointer[_struct.GUID],  # dstFormat
                           _enum.WICBitmapDitherType,  # dither
                           IWICPalette,  # pIPalette
                           _type.c_double,  # alphaThresholdPercent
                           _enum.WICBitmapPaletteType],  # paletteTranslate
                          _type.HRESULT]
    CanConvert: _Callable[[_Pointer[_struct.WICPixelFormatGUID],  # pSrcPixelFormats
                           _type.UINT,  # cSrcPlanes
                           _Pointer[_struct.GUID],  # dstPixelFormat
                           _Pointer[_type.BOOL]],  # pfCanConvert
                          _type.HRESULT]


class IWICBitmapScaler(IWICBitmapSource):
    Initialize: _Callable[[IWICBitmapSource,  # pISource
                           _type.UINT,  # uiWidth
                           _type.UINT,  # uiHeight
                           _enum.WICBitmapInterpolationMode],  # mode
                          _type.HRESULT]


class IWICBitmapClipper(IWICBitmapSource):
    Initialize: _Callable[[IWICBitmapSource,  # pISource
                           _Pointer[_struct.WICRect]],  # prc
                          _type.HRESULT]


class IWICBitmapFlipRotator(IWICBitmapSource):
    Initialize: _Callable[[IWICBitmapSource,  # pISource
                           _enum.WICBitmapTransformOptions],  # options
                          _type.HRESULT]


class IWICBitmapLock(_Unknwnbase.IUnknown):
    GetSize: _Callable[[_Pointer[_type.UINT],  # puiWidth
                        _Pointer[_type.UINT]],  # puiHeight
                       _type.HRESULT]
    GetStride: _Callable[[_Pointer[_type.UINT]],  # pcbStride
                         _type.HRESULT]
    GetDataPointer: _Callable[[_Pointer[_type.UINT],  # pcbBufferSize
                               _Pointer[_Pointer[_type.BYTE]]],  # ppbData
                              _type.HRESULT]
    GetPixelFormat: _Callable[[_Pointer[_struct.WICPixelFormatGUID]],  # pPixelFormat
                              _type.HRESULT]


class IWICBitmap(IWICBitmapSource):
    Lock: _Callable[[_Pointer[_struct.WICRect],  # prcLock
                     _type.DWORD,  # flags
                     _Pointer[IWICBitmapLock]],  # ppILock
                    _type.HRESULT]
    SetPalette: _Callable[[IWICPalette],  # pIPalette
                          _type.HRESULT]
    SetResolution: _Callable[[_type.c_double,  # dpiX
                              _type.c_double],  # dpiY
                             _type.HRESULT]


class IWICColorContext(_Unknwnbase.IUnknown):
    InitializeFromFilename: _Callable[[_type.LPCWSTR],  # wzFilename
                                      _type.HRESULT]
    InitializeFromMemory: _Callable[[_Pointer[_type.BYTE],  # pbBuffer
                                     _type.UINT],  # cbBufferSize
                                    _type.HRESULT]
    InitializeFromExifColorSpace: _Callable[[_type.UINT],  # value
                                            _type.HRESULT]
    GetType: _Callable[[_Pointer[_enum.WICColorContextType]],  # pType
                       _type.HRESULT]
    GetProfileBytes: _Callable[[_type.UINT,  # cbBuffer
                                _Pointer[_type.BYTE],  # pbBuffer
                                _Pointer[_type.UINT]],  # pcbActual
                               _type.HRESULT]
    GetExifColorSpace: _Callable[[_Pointer[_type.UINT]],  # pValue
                                 _type.HRESULT]


class IWICColorTransform(IWICBitmapSource):
    Initialize: _Callable[[IWICBitmapSource,  # pIBitmapSource
                           IWICColorContext,  # pIContextSource
                           IWICColorContext,  # pIContextDest
                           _Pointer[_struct.GUID]],  # pixelFmtDest
                          _type.HRESULT]


class IWICFastMetadataEncoder(_Unknwnbase.IUnknown):
    Commit: _Callable[[],
                      _type.HRESULT]
    GetMetadataQueryWriter: _Callable[[_Pointer[IWICMetadataQueryWriter]],  # ppIMetadataQueryWriter
                                      _type.HRESULT]


class IWICStream(_objidlbase.IStream):
    InitializeFromIStream: _Callable[[_objidlbase.IStream],  # pIStream
                                     _type.HRESULT]
    InitializeFromFilename: _Callable[[_type.LPCWSTR,  # wzFileName
                                       _type.DWORD],  # dwDesiredAccess
                                      _type.HRESULT]
    InitializeFromMemory: _Callable[[_Pointer[_type.BYTE],  # pbBuffer
                                     _type.DWORD],  # cbBufferSize
                                    _type.HRESULT]
    InitializeFromIStreamRegion: _Callable[[_objidlbase.IStream,  # pIStream
                                            _union.ULARGE_INTEGER,  # ulOffset
                                            _union.ULARGE_INTEGER],  # ulMaxSize
                                           _type.HRESULT]


class IWICEnumMetadataItem(_Unknwnbase.IUnknown):
    Next: _Callable[[_type.ULONG,  # celt
                     _Pointer[_struct.PROPVARIANT],  # rgeltSchema
                     _Pointer[_struct.PROPVARIANT],  # rgeltId
                     _Pointer[_struct.PROPVARIANT],  # rgeltValue
                     _Pointer[_type.ULONG]],  # pceltFetched
                    _type.HRESULT]
    Skip: _Callable[[_type.ULONG],  # celt
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Clone: _Callable[[_Pointer[IWICEnumMetadataItem]],  # ppIEnumMetadataItem
                     _type.HRESULT]


class IWICMetadataQueryReader(_Unknwnbase.IUnknown):
    GetContainerFormat: _Callable[[_Pointer[_struct.GUID]],  # pguidContainerFormat
                                  _type.HRESULT]
    GetLocation: _Callable[[_type.UINT,  # cchMaxLength
                            _Pointer[_type.WCHAR],  # wzNamespace
                            _Pointer[_type.UINT]],  # pcchActualLength
                           _type.HRESULT]
    GetMetadataByName: _Callable[[_type.LPCWSTR,  # wzName
                                  _Pointer[_struct.PROPVARIANT]],  # pvarValue
                                 _type.HRESULT]
    GetEnumerator: _Callable[[_Pointer[_objidlbase.IEnumString]],  # ppIEnumString
                             _type.HRESULT]


class IWICMetadataQueryWriter(IWICMetadataQueryReader):
    SetMetadataByName: _Callable[[_type.LPCWSTR,  # wzName
                                  _Pointer[_struct.PROPVARIANT]],  # pvarValue
                                 _type.HRESULT]
    RemoveMetadataByName: _Callable[[_type.LPCWSTR],  # wzName
                                    _type.HRESULT]


class IWICBitmapEncoder(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_objidlbase.IStream,  # pIStream
                           _enum.WICBitmapEncoderCacheOption],  # cacheOption
                          _type.HRESULT]
    GetContainerFormat: _Callable[[_Pointer[_struct.GUID]],  # pguidContainerFormat
                                  _type.HRESULT]
    GetEncoderInfo: _Callable[[_Pointer[IWICBitmapEncoderInfo]],  # ppIEncoderInfo
                              _type.HRESULT]
    SetColorContexts: _Callable[[_type.UINT,  # cCount
                                 _Pointer[IWICColorContext]],  # ppIColorContext
                                _type.HRESULT]
    SetPalette: _Callable[[IWICPalette],  # pIPalette
                          _type.HRESULT]
    SetThumbnail: _Callable[[IWICBitmapSource],  # pIThumbnail
                            _type.HRESULT]
    SetPreview: _Callable[[IWICBitmapSource],  # pIPreview
                          _type.HRESULT]
    CreateNewFrame: _Callable[[_Pointer[IWICBitmapFrameEncode],  # ppIFrameEncode
                               _Pointer[_ocidl.IPropertyBag2]],  # ppIEncoderOptions
                              _type.HRESULT]
    Commit: _Callable[[],
                      _type.HRESULT]
    GetMetadataQueryWriter: _Callable[[_Pointer[IWICMetadataQueryWriter]],  # ppIMetadataQueryWriter
                                      _type.HRESULT]


class IWICBitmapFrameEncode(_Unknwnbase.IUnknown):
    Initialize: _Callable[[_ocidl.IPropertyBag2],  # pIEncoderOptions
                          _type.HRESULT]
    SetSize: _Callable[[_type.UINT,  # uiWidth
                        _type.UINT],  # uiHeight
                       _type.HRESULT]
    SetResolution: _Callable[[_type.c_double,  # dpiX
                              _type.c_double],  # dpiY
                             _type.HRESULT]
    SetPixelFormat: _Callable[[_Pointer[_struct.WICPixelFormatGUID]],  # pPixelFormat
                              _type.HRESULT]
    SetColorContexts: _Callable[[_type.UINT,  # cCount
                                 _Pointer[IWICColorContext]],  # ppIColorContext
                                _type.HRESULT]
    SetPalette: _Callable[[IWICPalette],  # pIPalette
                          _type.HRESULT]
    SetThumbnail: _Callable[[IWICBitmapSource],  # pIThumbnail
                            _type.HRESULT]
    WritePixels: _Callable[[_type.UINT,  # lineCount
                            _type.UINT,  # cbStride
                            _type.UINT,  # cbBufferSize
                            _Pointer[_type.BYTE]],  # pbPixels
                           _type.HRESULT]
    WriteSource: _Callable[[IWICBitmapSource,  # pIBitmapSource
                            _Pointer[_struct.WICRect]],  # prc
                           _type.HRESULT]
    Commit: _Callable[[],
                      _type.HRESULT]
    GetMetadataQueryWriter: _Callable[[_Pointer[IWICMetadataQueryWriter]],  # ppIMetadataQueryWriter
                                      _type.HRESULT]


class IWICPlanarBitmapFrameEncode(_Unknwnbase.IUnknown):
    WritePixels: _Callable[[_type.UINT,  # lineCount
                            _Pointer[_struct.WICBitmapPlane],  # pPlanes
                            _type.UINT],  # cPlanes
                           _type.HRESULT]
    WriteSource: _Callable[[_Pointer[IWICBitmapSource],  # ppPlanes
                            _type.UINT,  # cPlanes
                            _Pointer[_struct.WICRect]],  # prcSource
                           _type.HRESULT]


class IWICImageEncoder(_Unknwnbase.IUnknown):
    WriteFrame: _Callable[[_d2d1.ID2D1Image,  # pImage
                           IWICBitmapFrameEncode,  # pFrameEncode
                           _Pointer[_struct.WICImageParameters]],  # pImageParameters
                          _type.HRESULT]
    WriteFrameThumbnail: _Callable[[_d2d1.ID2D1Image,  # pImage
                                    IWICBitmapFrameEncode,  # pFrameEncode
                                    _Pointer[_struct.WICImageParameters]],  # pImageParameters
                                   _type.HRESULT]
    WriteThumbnail: _Callable[[_d2d1.ID2D1Image,  # pImage
                               IWICBitmapEncoder,  # pEncoder
                               _Pointer[_struct.WICImageParameters]],  # pImageParameters
                              _type.HRESULT]


class IWICBitmapDecoder(_Unknwnbase.IUnknown):
    QueryCapability: _Callable[[_objidlbase.IStream,  # pIStream
                                _Pointer[_type.DWORD]],  # pdwCapability
                               _type.HRESULT]
    Initialize: _Callable[[_objidlbase.IStream,  # pIStream
                           _enum.WICDecodeOptions],  # cacheOptions
                          _type.HRESULT]
    GetContainerFormat: _Callable[[_Pointer[_struct.GUID]],  # pguidContainerFormat
                                  _type.HRESULT]
    GetDecoderInfo: _Callable[[_Pointer[IWICBitmapDecoderInfo]],  # ppIDecoderInfo
                              _type.HRESULT]
    CopyPalette: _Callable[[IWICPalette],  # pIPalette
                           _type.HRESULT]
    GetMetadataQueryReader: _Callable[[_Pointer[IWICMetadataQueryReader]],  # ppIMetadataQueryReader
                                      _type.HRESULT]
    GetPreview: _Callable[[_Pointer[IWICBitmapSource]],  # ppIBitmapSource
                          _type.HRESULT]
    GetColorContexts: _Callable[[_type.UINT,  # cCount
                                 _Pointer[IWICColorContext],  # ppIColorContexts
                                 _Pointer[_type.UINT]],  # pcActualCount
                                _type.HRESULT]
    GetThumbnail: _Callable[[_Pointer[IWICBitmapSource]],  # ppIThumbnail
                            _type.HRESULT]
    GetFrameCount: _Callable[[_Pointer[_type.UINT]],  # pCount
                             _type.HRESULT]
    GetFrame: _Callable[[_type.UINT,  # index
                         _Pointer[IWICBitmapFrameDecode]],  # ppIBitmapFrame
                        _type.HRESULT]


class IWICBitmapSourceTransform(_Unknwnbase.IUnknown):
    CopyPixels: _Callable[[_Pointer[_struct.WICRect],  # prc
                           _type.UINT,  # uiWidth
                           _type.UINT,  # uiHeight
                           _Pointer[_struct.WICPixelFormatGUID],  # pguidDstFormat
                           _enum.WICBitmapTransformOptions,  # dstTransform
                           _type.UINT,  # nStride
                           _type.UINT,  # cbBufferSize
                           _Pointer[_type.BYTE]],  # pbBuffer
                          _type.HRESULT]
    GetClosestSize: _Callable[[_Pointer[_type.UINT],  # puiWidth
                               _Pointer[_type.UINT]],  # puiHeight
                              _type.HRESULT]
    GetClosestPixelFormat: _Callable[[_Pointer[_struct.WICPixelFormatGUID]],  # pguidDstFormat
                                     _type.HRESULT]
    DoesSupportTransform: _Callable[[_enum.WICBitmapTransformOptions,  # dstTransform
                                     _Pointer[_type.BOOL]],  # pfIsSupported
                                    _type.HRESULT]


class IWICPlanarBitmapSourceTransform(_Unknwnbase.IUnknown):
    DoesSupportTransform: _Callable[[_Pointer[_type.UINT],  # puiWidth
                                     _Pointer[_type.UINT],  # puiHeight
                                     _enum.WICBitmapTransformOptions,  # dstTransform
                                     _enum.WICPlanarOptions,  # dstPlanarOptions
                                     _Pointer[_struct.WICPixelFormatGUID],  # pguidDstFormats
                                     _Pointer[_struct.WICBitmapPlaneDescription],  # pPlaneDescriptions
                                     _type.UINT,  # cPlanes
                                     _Pointer[_type.BOOL]],  # pfIsSupported
                                    _type.HRESULT]
    CopyPixels: _Callable[[_Pointer[_struct.WICRect],  # prcSource
                           _type.UINT,  # uiWidth
                           _type.UINT,  # uiHeight
                           _enum.WICBitmapTransformOptions,  # dstTransform
                           _enum.WICPlanarOptions,  # dstPlanarOptions
                           _Pointer[_struct.WICBitmapPlane],  # pDstPlanes
                           _type.UINT],  # cPlanes
                          _type.HRESULT]


class IWICBitmapFrameDecode(IWICBitmapSource):
    GetMetadataQueryReader: _Callable[[_Pointer[IWICMetadataQueryReader]],  # ppIMetadataQueryReader
                                      _type.HRESULT]
    GetColorContexts: _Callable[[_type.UINT,  # cCount
                                 _Pointer[IWICColorContext],  # ppIColorContexts
                                 _Pointer[_type.UINT]],  # pcActualCount
                                _type.HRESULT]
    GetThumbnail: _Callable[[_Pointer[IWICBitmapSource]],  # ppIThumbnail
                            _type.HRESULT]


class IWICProgressiveLevelControl(_Unknwnbase.IUnknown):
    GetLevelCount: _Callable[[_Pointer[_type.UINT]],  # pcLevels
                             _type.HRESULT]
    GetCurrentLevel: _Callable[[_Pointer[_type.UINT]],  # pnLevel
                               _type.HRESULT]
    SetCurrentLevel: _Callable[[_type.UINT],  # nLevel
                               _type.HRESULT]


class IWICProgressCallback(_Unknwnbase.IUnknown):
    Notify: _Callable[[_type.ULONG,  # uFrameNum
                       _enum.WICProgressOperation,  # operation
                       _type.c_double],  # dblProgress
                      _type.HRESULT]


class IWICBitmapCodecProgressNotification(_Unknwnbase.IUnknown):
    RegisterProgressNotification: _Callable[[_type.PFNProgressNotification,  # pfnProgressNotification
                                             _type.LPVOID,  # pvData
                                             _type.DWORD],  # dwProgressFlags
                                            _type.HRESULT]


class IWICComponentInfo(_Unknwnbase.IUnknown):
    GetComponentType: _Callable[[_Pointer[_enum.WICComponentType]],  # pType
                                _type.HRESULT]
    GetCLSID: _Callable[[_Pointer[_struct.CLSID]],  # pclsid
                        _type.HRESULT]
    GetSigningStatus: _Callable[[_Pointer[_type.DWORD]],  # pStatus
                                _type.HRESULT]
    GetAuthor: _Callable[[_type.UINT,  # cchAuthor
                          _Pointer[_type.WCHAR],  # wzAuthor
                          _Pointer[_type.UINT]],  # pcchActual
                         _type.HRESULT]
    GetVendorGUID: _Callable[[_Pointer[_struct.GUID]],  # pguidVendor
                             _type.HRESULT]
    GetVersion: _Callable[[_type.UINT,  # cchVersion
                           _Pointer[_type.WCHAR],  # wzVersion
                           _Pointer[_type.UINT]],  # pcchActual
                          _type.HRESULT]
    GetSpecVersion: _Callable[[_type.UINT,  # cchSpecVersion
                               _Pointer[_type.WCHAR],  # wzSpecVersion
                               _Pointer[_type.UINT]],  # pcchActual
                              _type.HRESULT]
    GetFriendlyName: _Callable[[_type.UINT,  # cchFriendlyName
                                _Pointer[_type.WCHAR],  # wzFriendlyName
                                _Pointer[_type.UINT]],  # pcchActual
                               _type.HRESULT]


class IWICFormatConverterInfo(IWICComponentInfo):
    GetPixelFormats: _Callable[[_type.UINT,  # cFormats
                                _Pointer[_struct.WICPixelFormatGUID],  # pPixelFormatGUIDs
                                _Pointer[_type.UINT]],  # pcActual
                               _type.HRESULT]
    CreateInstance: _Callable[[_Pointer[IWICFormatConverter]],  # ppIConverter
                              _type.HRESULT]


class IWICBitmapCodecInfo(IWICComponentInfo):
    GetContainerFormat: _Callable[[_Pointer[_struct.GUID]],  # pguidContainerFormat
                                  _type.HRESULT]
    GetPixelFormats: _Callable[[_type.UINT,  # cFormats
                                _Pointer[_struct.GUID],  # pguidPixelFormats
                                _Pointer[_type.UINT]],  # pcActual
                               _type.HRESULT]
    GetColorManagementVersion: _Callable[[_type.UINT,  # cchColorManagementVersion
                                          _Pointer[_type.WCHAR],  # wzColorManagementVersion
                                          _Pointer[_type.UINT]],  # pcchActual
                                         _type.HRESULT]
    GetDeviceManufacturer: _Callable[[_type.UINT,  # cchDeviceManufacturer
                                      _Pointer[_type.WCHAR],  # wzDeviceManufacturer
                                      _Pointer[_type.UINT]],  # pcchActual
                                     _type.HRESULT]
    GetDeviceModels: _Callable[[_type.UINT,  # cchDeviceModels
                                _Pointer[_type.WCHAR],  # wzDeviceModels
                                _Pointer[_type.UINT]],  # pcchActual
                               _type.HRESULT]
    GetMimeTypes: _Callable[[_type.UINT,  # cchMimeTypes
                             _Pointer[_type.WCHAR],  # wzMimeTypes
                             _Pointer[_type.UINT]],  # pcchActual
                            _type.HRESULT]
    GetFileExtensions: _Callable[[_type.UINT,  # cchFileExtensions
                                  _Pointer[_type.WCHAR],  # wzFileExtensions
                                  _Pointer[_type.UINT]],  # pcchActual
                                 _type.HRESULT]
    DoesSupportAnimation: _Callable[[_Pointer[_type.BOOL]],  # pfSupportAnimation
                                    _type.HRESULT]
    DoesSupportChromakey: _Callable[[_Pointer[_type.BOOL]],  # pfSupportChromakey
                                    _type.HRESULT]
    DoesSupportLossless: _Callable[[_Pointer[_type.BOOL]],  # pfSupportLossless
                                   _type.HRESULT]
    DoesSupportMultiframe: _Callable[[_Pointer[_type.BOOL]],  # pfSupportMultiframe
                                     _type.HRESULT]
    MatchesMimeType: _Callable[[_type.LPCWSTR,  # wzMimeType
                                _Pointer[_type.BOOL]],  # pfMatches
                               _type.HRESULT]


class IWICBitmapEncoderInfo(IWICBitmapCodecInfo):
    CreateInstance: _Callable[[_Pointer[IWICBitmapEncoder]],  # ppIBitmapEncoder
                              _type.HRESULT]


class IWICBitmapDecoderInfo(IWICBitmapCodecInfo):
    GetPatterns: _Callable[[_type.UINT,  # cbSizePatterns
                            _Pointer[_struct.WICBitmapPattern],  # pPatterns
                            _Pointer[_type.UINT],  # pcPatterns
                            _Pointer[_type.UINT]],  # pcbPatternsActual
                           _type.HRESULT]
    MatchesPattern: _Callable[[_objidlbase.IStream,  # pIStream
                               _Pointer[_type.BOOL]],  # pfMatches
                              _type.HRESULT]
    CreateInstance: _Callable[[_Pointer[IWICBitmapDecoder]],  # ppIBitmapDecoder
                              _type.HRESULT]


class IWICPixelFormatInfo(IWICComponentInfo):
    GetFormatGUID: _Callable[[_Pointer[_struct.GUID]],  # pFormat
                             _type.HRESULT]
    GetColorContext: _Callable[[_Pointer[IWICColorContext]],  # ppIColorContext
                               _type.HRESULT]
    GetBitsPerPixel: _Callable[[_Pointer[_type.UINT]],  # puiBitsPerPixel
                               _type.HRESULT]
    GetChannelCount: _Callable[[_Pointer[_type.UINT]],  # puiChannelCount
                               _type.HRESULT]
    GetChannelMask: _Callable[[_type.UINT,  # uiChannelIndex
                               _type.UINT,  # cbMaskBuffer
                               _Pointer[_type.BYTE],  # pbMaskBuffer
                               _Pointer[_type.UINT]],  # pcbActual
                              _type.HRESULT]


class IWICPixelFormatInfo2(IWICPixelFormatInfo):
    SupportsTransparency: _Callable[[_Pointer[_type.BOOL]],  # pfSupportsTransparency
                                    _type.HRESULT]
    GetNumericRepresentation: _Callable[[_Pointer[_enum.WICPixelFormatNumericRepresentation]],  # pNumericRepresentation
                                        _type.HRESULT]


class IWICImagingFactory(_Unknwnbase.IUnknown):
    CreateDecoderFromFilename: _Callable[[_type.LPCWSTR,  # wzFilename
                                          _Pointer[_struct.GUID],  # pguidVendor
                                          _type.DWORD,  # dwDesiredAccess
                                          _enum.WICDecodeOptions,  # metadataOptions
                                          _Pointer[IWICBitmapDecoder]],  # ppIDecoder
                                         _type.HRESULT]
    CreateDecoderFromStream: _Callable[[_objidlbase.IStream,  # pIStream
                                        _Pointer[_struct.GUID],  # pguidVendor
                                        _enum.WICDecodeOptions,  # metadataOptions
                                        _Pointer[IWICBitmapDecoder]],  # ppIDecoder
                                       _type.HRESULT]
    CreateDecoderFromFileHandle: _Callable[[_type.ULONG_PTR,  # hFile
                                            _Pointer[_struct.GUID],  # pguidVendor
                                            _enum.WICDecodeOptions,  # metadataOptions
                                            _Pointer[IWICBitmapDecoder]],  # ppIDecoder
                                           _type.HRESULT]
    CreateComponentInfo: _Callable[[_Pointer[_struct.IID],  # clsidComponent
                                    _Pointer[IWICComponentInfo]],  # ppIInfo
                                   _type.HRESULT]
    CreateDecoder: _Callable[[_Pointer[_struct.GUID],  # guidContainerFormat
                              _Pointer[_struct.GUID],  # pguidVendor
                              _Pointer[IWICBitmapDecoder]],  # ppIDecoder
                             _type.HRESULT]
    CreateEncoder: _Callable[[_Pointer[_struct.GUID],  # guidContainerFormat
                              _Pointer[_struct.GUID],  # pguidVendor
                              _Pointer[IWICBitmapEncoder]],  # ppIEncoder
                             _type.HRESULT]
    CreatePalette: _Callable[[_Pointer[IWICPalette]],  # ppIPalette
                             _type.HRESULT]
    CreateFormatConverter: _Callable[[_Pointer[IWICFormatConverter]],  # ppIFormatConverter
                                     _type.HRESULT]
    CreateBitmapScaler: _Callable[[_Pointer[IWICBitmapScaler]],  # ppIBitmapScaler
                                  _type.HRESULT]
    CreateBitmapClipper: _Callable[[_Pointer[IWICBitmapClipper]],  # ppIBitmapClipper
                                   _type.HRESULT]
    CreateBitmapFlipRotator: _Callable[[_Pointer[IWICBitmapFlipRotator]],  # ppIBitmapFlipRotator
                                       _type.HRESULT]
    CreateStream: _Callable[[_Pointer[IWICStream]],  # ppIWICStream
                            _type.HRESULT]
    CreateColorContext: _Callable[[_Pointer[IWICColorContext]],  # ppIWICColorContext
                                  _type.HRESULT]
    CreateColorTransformer: _Callable[[_Pointer[IWICColorTransform]],  # ppIWICColorTransform
                                      _type.HRESULT]
    CreateBitmap: _Callable[[_type.UINT,  # uiWidth
                             _type.UINT,  # uiHeight
                             _Pointer[_struct.GUID],  # pixelFormat
                             _enum.WICBitmapCreateCacheOption,  # option
                             _Pointer[IWICBitmap]],  # ppIBitmap
                            _type.HRESULT]
    CreateBitmapFromSource: _Callable[[IWICBitmapSource,  # pIBitmapSource
                                       _enum.WICBitmapCreateCacheOption,  # option
                                       _Pointer[IWICBitmap]],  # ppIBitmap
                                      _type.HRESULT]
    CreateBitmapFromSourceRect: _Callable[[IWICBitmapSource,  # pIBitmapSource
                                           _type.UINT,  # x
                                           _type.UINT,  # y
                                           _type.UINT,  # width
                                           _type.UINT,  # height
                                           _Pointer[IWICBitmap]],  # ppIBitmap
                                          _type.HRESULT]
    CreateBitmapFromMemory: _Callable[[_type.UINT,  # uiWidth
                                       _type.UINT,  # uiHeight
                                       _Pointer[_struct.GUID],  # pixelFormat
                                       _type.UINT,  # cbStride
                                       _type.UINT,  # cbBufferSize
                                       _Pointer[_type.BYTE],  # pbBuffer
                                       _Pointer[IWICBitmap]],  # ppIBitmap
                                      _type.HRESULT]
    CreateBitmapFromHBITMAP: _Callable[[_type.HBITMAP,  # hBitmap
                                        _type.HPALETTE,  # hPalette
                                        _enum.WICBitmapAlphaChannelOption,  # options
                                        _Pointer[IWICBitmap]],  # ppIBitmap
                                       _type.HRESULT]
    CreateBitmapFromHICON: _Callable[[_type.HICON,  # hIcon
                                      _Pointer[IWICBitmap]],  # ppIBitmap
                                     _type.HRESULT]
    CreateComponentEnumerator: _Callable[[_type.DWORD,  # componentTypes
                                          _type.DWORD,  # options
                                          _Pointer[_objidlbase.IEnumUnknown]],  # ppIEnumUnknown
                                         _type.HRESULT]
    CreateFastMetadataEncoderFromDecoder: _Callable[[IWICBitmapDecoder,  # pIDecoder
                                                     _Pointer[IWICFastMetadataEncoder]],  # ppIFastEncoder
                                                    _type.HRESULT]
    CreateFastMetadataEncoderFromFrameDecode: _Callable[[IWICBitmapFrameDecode,  # pIFrameDecoder
                                                         _Pointer[IWICFastMetadataEncoder]],  # ppIFastEncoder
                                                        _type.HRESULT]
    CreateQueryWriter: _Callable[[_Pointer[_struct.GUID],  # guidMetadataFormat
                                  _Pointer[_struct.GUID],  # pguidVendor
                                  _Pointer[IWICMetadataQueryWriter]],  # ppIQueryWriter
                                 _type.HRESULT]
    CreateQueryWriterFromReader: _Callable[[IWICMetadataQueryReader,  # pIQueryReader
                                            _Pointer[_struct.GUID],  # pguidVendor
                                            _Pointer[IWICMetadataQueryWriter]],  # ppIQueryWriter
                                           _type.HRESULT]


class IWICImagingFactory2(IWICImagingFactory):
    CreateImageEncoder: _Callable[[_d2d1_1.ID2D1Device,  # pD2DDevice
                                   _Pointer[IWICImageEncoder]],  # ppWICImageEncoder
                                  _type.HRESULT]


class IWICDevelopRawNotificationCallback(_Unknwnbase.IUnknown):
    Notify: _Callable[[_type.UINT],  # NotificationMask
                      _type.HRESULT]


class IWICDevelopRaw(IWICBitmapFrameDecode):
    QueryRawCapabilitiesInfo: _Callable[[_Pointer[_struct.WICRawCapabilitiesInfo]],  # pInfo
                                        _type.HRESULT]
    LoadParameterSet: _Callable[[_enum.WICRawParameterSet],  # ParameterSet
                                _type.HRESULT]
    GetCurrentParameterSet: _Callable[[_Pointer[_ocidl.IPropertyBag2]],  # ppCurrentParameterSet
                                      _type.HRESULT]
    SetExposureCompensation: _Callable[[_type.c_double],  # ev
                                       _type.HRESULT]
    GetExposureCompensation: _Callable[[_Pointer[_type.c_double]],  # pEV
                                       _type.HRESULT]
    SetWhitePointRGB: _Callable[[_type.UINT,  # Red
                                 _type.UINT,  # Green
                                 _type.UINT],  # Blue
                                _type.HRESULT]
    GetWhitePointRGB: _Callable[[_Pointer[_type.UINT],  # pRed
                                 _Pointer[_type.UINT],  # pGreen
                                 _Pointer[_type.UINT]],  # pBlue
                                _type.HRESULT]
    SetNamedWhitePoint: _Callable[[_enum.WICNamedWhitePoint],  # WhitePoint
                                  _type.HRESULT]
    GetNamedWhitePoint: _Callable[[_Pointer[_enum.WICNamedWhitePoint]],  # pWhitePoint
                                  _type.HRESULT]
    SetWhitePointKelvin: _Callable[[_type.UINT],  # WhitePointKelvin
                                   _type.HRESULT]
    GetWhitePointKelvin: _Callable[[_Pointer[_type.UINT]],  # pWhitePointKelvin
                                   _type.HRESULT]
    GetKelvinRangeInfo: _Callable[[_Pointer[_type.UINT],  # pMinKelvinTemp
                                   _Pointer[_type.UINT],  # pMaxKelvinTemp
                                   _Pointer[_type.UINT]],  # pKelvinTempStepValue
                                  _type.HRESULT]
    SetContrast: _Callable[[_type.c_double],  # Contrast
                           _type.HRESULT]
    GetContrast: _Callable[[_Pointer[_type.c_double]],  # pContrast
                           _type.HRESULT]
    SetGamma: _Callable[[_type.c_double],  # Gamma
                        _type.HRESULT]
    GetGamma: _Callable[[_Pointer[_type.c_double]],  # pGamma
                        _type.HRESULT]
    SetSharpness: _Callable[[_type.c_double],  # Sharpness
                            _type.HRESULT]
    GetSharpness: _Callable[[_Pointer[_type.c_double]],  # pSharpness
                            _type.HRESULT]
    SetSaturation: _Callable[[_type.c_double],  # Saturation
                             _type.HRESULT]
    GetSaturation: _Callable[[_Pointer[_type.c_double]],  # pSaturation
                             _type.HRESULT]
    SetTint: _Callable[[_type.c_double],  # Tint
                       _type.HRESULT]
    GetTint: _Callable[[_Pointer[_type.c_double]],  # pTint
                       _type.HRESULT]
    SetNoiseReduction: _Callable[[_type.c_double],  # NoiseReduction
                                 _type.HRESULT]
    GetNoiseReduction: _Callable[[_Pointer[_type.c_double]],  # pNoiseReduction
                                 _type.HRESULT]
    SetDestinationColorContext: _Callable[[IWICColorContext],  # pColorContext
                                          _type.HRESULT]
    SetToneCurve: _Callable[[_type.UINT,  # cbToneCurveSize
                             _Pointer[_struct.WICRawToneCurve]],  # pToneCurve
                            _type.HRESULT]
    GetToneCurve: _Callable[[_type.UINT,  # cbToneCurveBufferSize
                             _Pointer[_struct.WICRawToneCurve],  # pToneCurve
                             _Pointer[_type.UINT]],  # pcbActualToneCurveBufferSize
                            _type.HRESULT]
    SetRotation: _Callable[[_type.c_double],  # Rotation
                           _type.HRESULT]
    GetRotation: _Callable[[_Pointer[_type.c_double]],  # pRotation
                           _type.HRESULT]
    SetRenderMode: _Callable[[_enum.WICRawRenderMode],  # RenderMode
                             _type.HRESULT]
    GetRenderMode: _Callable[[_Pointer[_enum.WICRawRenderMode]],  # pRenderMode
                             _type.HRESULT]
    SetNotificationCallback: _Callable[[IWICDevelopRawNotificationCallback],  # pCallback
                                       _type.HRESULT]


class IWICDdsDecoder(_Unknwnbase.IUnknown):
    GetParameters: _Callable[[_Pointer[_struct.WICDdsParameters]],  # pParameters
                             _type.HRESULT]
    GetFrame: _Callable[[_type.UINT,  # arrayIndex
                         _type.UINT,  # mipLevel
                         _type.UINT,  # sliceIndex
                         _Pointer[IWICBitmapFrameDecode]],  # ppIBitmapFrame
                        _type.HRESULT]


class IWICDdsEncoder(_Unknwnbase.IUnknown):
    SetParameters: _Callable[[_Pointer[_struct.WICDdsParameters]],  # pParameters
                             _type.HRESULT]
    GetParameters: _Callable[[_Pointer[_struct.WICDdsParameters]],  # pParameters
                             _type.HRESULT]
    CreateNewFrame: _Callable[[_Pointer[IWICBitmapFrameEncode],  # ppIFrameEncode
                               _Pointer[_type.UINT],  # pArrayIndex
                               _Pointer[_type.UINT],  # pMipLevel
                               _Pointer[_type.UINT]],  # pSliceIndex
                              _type.HRESULT]


class IWICDdsFrameDecode(_Unknwnbase.IUnknown):
    GetSizeInBlocks: _Callable[[_Pointer[_type.UINT],  # pWidthInBlocks
                                _Pointer[_type.UINT]],  # pHeightInBlocks
                               _type.HRESULT]
    GetFormatInfo: _Callable[[_Pointer[_struct.WICDdsFormatInfo]],  # pFormatInfo
                             _type.HRESULT]
    CopyBlocks: _Callable[[_Pointer[_struct.WICRect],  # prcBoundsInBlocks
                           _type.UINT,  # cbStride
                           _type.UINT,  # cbBufferSize
                           _Pointer[_type.BYTE]],  # pbBuffer
                          _type.HRESULT]


class IWICJpegFrameDecode(_Unknwnbase.IUnknown):
    DoesSupportIndexing: _Callable[[_Pointer[_type.BOOL]],  # pfIndexingSupported
                                   _type.HRESULT]
    SetIndexing: _Callable[[_enum.WICJpegIndexingOptions,  # options
                            _type.UINT],  # horizontalIntervalSize
                           _type.HRESULT]
    ClearIndexing: _Callable[[],
                             _type.HRESULT]
    GetAcHuffmanTable: _Callable[[_type.UINT,  # scanIndex
                                  _type.UINT,  # tableIndex
                                  _Pointer[_struct.DXGI_JPEG_AC_HUFFMAN_TABLE]],  # pAcHuffmanTable
                                 _type.HRESULT]
    GetDcHuffmanTable: _Callable[[_type.UINT,  # scanIndex
                                  _type.UINT,  # tableIndex
                                  _Pointer[_struct.DXGI_JPEG_DC_HUFFMAN_TABLE]],  # pDcHuffmanTable
                                 _type.HRESULT]
    GetQuantizationTable: _Callable[[_type.UINT,  # scanIndex
                                     _type.UINT,  # tableIndex
                                     _Pointer[_struct.DXGI_JPEG_QUANTIZATION_TABLE]],  # pQuantizationTable
                                    _type.HRESULT]
    GetFrameHeader: _Callable[[_Pointer[_struct.WICJpegFrameHeader]],  # pFrameHeader
                              _type.HRESULT]
    GetScanHeader: _Callable[[_type.UINT,  # scanIndex
                              _Pointer[_struct.WICJpegScanHeader]],  # pScanHeader
                             _type.HRESULT]
    CopyScan: _Callable[[_type.UINT,  # scanIndex
                         _type.UINT,  # scanOffset
                         _type.UINT,  # cbScanData
                         _Pointer[_type.BYTE],  # pbScanData
                         _Pointer[_type.UINT]],  # pcbScanDataActual
                        _type.HRESULT]
    CopyMinimalStream: _Callable[[_type.UINT,  # streamOffset
                                  _type.UINT,  # cbStreamData
                                  _Pointer[_type.BYTE],  # pbStreamData
                                  _Pointer[_type.UINT]],  # pcbStreamDataActual
                                 _type.HRESULT]


class IWICJpegFrameEncode(_Unknwnbase.IUnknown):
    GetAcHuffmanTable: _Callable[[_type.UINT,  # scanIndex
                                  _type.UINT,  # tableIndex
                                  _Pointer[_struct.DXGI_JPEG_AC_HUFFMAN_TABLE]],  # pAcHuffmanTable
                                 _type.HRESULT]
    GetDcHuffmanTable: _Callable[[_type.UINT,  # scanIndex
                                  _type.UINT,  # tableIndex
                                  _Pointer[_struct.DXGI_JPEG_DC_HUFFMAN_TABLE]],  # pDcHuffmanTable
                                 _type.HRESULT]
    GetQuantizationTable: _Callable[[_type.UINT,  # scanIndex
                                     _type.UINT,  # tableIndex
                                     _Pointer[_struct.DXGI_JPEG_QUANTIZATION_TABLE]],  # pQuantizationTable
                                    _type.HRESULT]
    WriteScan: _Callable[[_type.UINT,  # cbScanData
                          _Pointer[_type.BYTE]],  # pbScanData
                         _type.HRESULT]
