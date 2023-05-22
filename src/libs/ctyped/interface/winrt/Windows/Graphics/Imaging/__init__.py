from __future__ import annotations

from typing import Callable as _Callable

from ..DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBitmapBuffer(_inspectable.IInspectable):
    GetPlaneCount: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    GetPlaneDescription: _Callable[[_type.INT32,  # index
                                    _Pointer[_struct.Windows.Graphics.Imaging.BitmapPlaneDescription]],  # value
                                   _type.HRESULT]


class IBitmapCodecInformation(_inspectable.IInspectable):
    get_CodecId: _Callable[[_Pointer[_struct.GUID]],  # value
                           _type.HRESULT]
    get_FileExtensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_MimeTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]


class IBitmapDecoder(_inspectable.IInspectable):
    get_BitmapContainerProperties: _Callable[[_Pointer[IBitmapPropertiesView]],  # value
                                             _type.HRESULT]
    get_DecoderInformation: _Callable[[_Pointer[IBitmapCodecInformation]],  # value
                                      _type.HRESULT]
    get_FrameCount: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    GetPreviewAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # asyncInfo
                               _type.HRESULT]
    GetFrameAsync: _Callable[[_type.UINT32,  # frameIndex
                              _Pointer[_Windows_Foundation.IAsyncOperation[IBitmapFrame]]],  # asyncInfo
                             _type.HRESULT]


class IBitmapDecoderStatics(_inspectable.IInspectable, factory=True):
    get_BmpDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_JpegDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_PngDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_TiffDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_GifDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_JpegXRDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    get_IcoDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    GetDecoderInformationEnumerator: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IBitmapCodecInformation]]],  # decoderInformationEnumerator
                                               _type.HRESULT]
    CreateAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBitmapDecoder]]],  # asyncInfo
                           _type.HRESULT]
    CreateWithIdAsync: _Callable[[_struct.GUID,  # decoderId
                                  _Windows_Storage_Streams.IRandomAccessStream,  # stream
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IBitmapDecoder]]],  # asyncInfo
                                 _type.HRESULT]


class IBitmapDecoderStatics2(_inspectable.IInspectable, factory=True):
    get_HeifDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_WebpDecoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]


class IBitmapEncoder(_inspectable.IInspectable):
    get_EncoderInformation: _Callable[[_Pointer[IBitmapCodecInformation]],  # value
                                      _type.HRESULT]
    get_BitmapProperties: _Callable[[_Pointer[IBitmapProperties]],  # value
                                    _type.HRESULT]
    get_BitmapContainerProperties: _Callable[[_Pointer[IBitmapProperties]],  # value
                                             _type.HRESULT]
    get_IsThumbnailGenerated: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsThumbnailGenerated: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_GeneratedThumbnailWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]
    put_GeneratedThumbnailWidth: _Callable[[_type.UINT32],  # value
                                           _type.HRESULT]
    get_GeneratedThumbnailHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]
    put_GeneratedThumbnailHeight: _Callable[[_type.UINT32],  # value
                                            _type.HRESULT]
    get_BitmapTransform: _Callable[[_Pointer[IBitmapTransform]],  # value
                                   _type.HRESULT]
    SetPixelData: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # pixelFormat
                             _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alphaMode
                             _type.UINT32,  # width
                             _type.UINT32,  # height
                             _type.DOUBLE,  # dpiX
                             _type.DOUBLE,  # dpiY
                             _type.UINT32,  # __pixelsSize
                             _Pointer[_type.BYTE]],  # pixels
                            _type.HRESULT]
    GoToNextFrameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                  _type.HRESULT]
    GoToNextFrameWithEncodingOptionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IBitmapTypedValue]],  # encodingOptions
                                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                                     _type.HRESULT]
    FlushAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                          _type.HRESULT]


class IBitmapEncoderStatics(_inspectable.IInspectable, factory=True):
    get_BmpEncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_JpegEncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_PngEncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_TiffEncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_GifEncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                _type.HRESULT]
    get_JpegXREncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    GetEncoderInformationEnumerator: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IBitmapCodecInformation]]],  # encoderInformationEnumerator
                                               _type.HRESULT]
    CreateAsync: _Callable[[_struct.GUID,  # encoderId
                            _Windows_Storage_Streams.IRandomAccessStream,  # stream
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBitmapEncoder]]],  # asyncInfo
                           _type.HRESULT]
    CreateWithEncodingOptionsAsync: _Callable[[_struct.GUID,  # encoderId
                                               _Windows_Storage_Streams.IRandomAccessStream,  # stream
                                               _Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IBitmapTypedValue]],  # encodingOptions
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IBitmapEncoder]]],  # asyncInfo
                                              _type.HRESULT]
    CreateForTranscodingAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                          IBitmapDecoder,  # bitmapDecoder
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IBitmapEncoder]]],  # asyncInfo
                                         _type.HRESULT]
    CreateForInPlacePropertyEncodingAsync: _Callable[[IBitmapDecoder,  # bitmapDecoder
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IBitmapEncoder]]],  # asyncInfo
                                                     _type.HRESULT]


class IBitmapEncoderStatics2(_inspectable.IInspectable, factory=True):
    get_HeifEncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]


class IBitmapEncoderWithSoftwareBitmap(_inspectable.IInspectable):
    SetSoftwareBitmap: _Callable[[ISoftwareBitmap],  # bitmap
                                 _type.HRESULT]


class IBitmapFrame(_inspectable.IInspectable):
    GetThumbnailAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # asyncInfo
                                 _type.HRESULT]
    get_BitmapProperties: _Callable[[_Pointer[IBitmapPropertiesView]],  # value
                                    _type.HRESULT]
    get_BitmapPixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]],  # value
                                     _type.HRESULT]
    get_BitmapAlphaMode: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapAlphaMode]],  # value
                                   _type.HRESULT]
    get_DpiX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    get_DpiY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    get_PixelWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_PixelHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_OrientedPixelWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    get_OrientedPixelHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    GetPixelDataAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPixelDataProvider]]],  # asyncInfo
                                 _type.HRESULT]
    GetPixelDataTransformedAsync: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # pixelFormat
                                             _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alphaMode
                                             IBitmapTransform,  # transform
                                             _enum.Windows.Graphics.Imaging.ExifOrientationMode,  # exifOrientationMode
                                             _enum.Windows.Graphics.Imaging.ColorManagementMode,  # colorManagementMode
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IPixelDataProvider]]],  # asyncInfo
                                            _type.HRESULT]


class IBitmapFrameWithSoftwareBitmap(_inspectable.IInspectable):
    GetSoftwareBitmapAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISoftwareBitmap]]],  # value
                                      _type.HRESULT]
    GetSoftwareBitmapConvertedAsync: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # pixelFormat
                                                _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alphaMode
                                                _Pointer[_Windows_Foundation.IAsyncOperation[ISoftwareBitmap]]],  # value
                                               _type.HRESULT]
    GetSoftwareBitmapTransformedAsync: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # pixelFormat
                                                  _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alphaMode
                                                  IBitmapTransform,  # transform
                                                  _enum.Windows.Graphics.Imaging.ExifOrientationMode,  # exifOrientationMode
                                                  _enum.Windows.Graphics.Imaging.ColorManagementMode,  # colorManagementMode
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[ISoftwareBitmap]]],  # value
                                                 _type.HRESULT]


class IBitmapProperties(_inspectable.IInspectable):
    SetPropertiesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IBitmapTypedValue]],  # propertiesToSet
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                  _type.HRESULT]


class IBitmapPropertiesView(_inspectable.IInspectable):
    GetPropertiesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # propertiesToRetrieve
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMap[_type.HSTRING, IBitmapTypedValue]]]],  # asyncInfo
                                  _type.HRESULT]


class IBitmapTransform(_inspectable.IInspectable):
    get_ScaledWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_ScaledWidth: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_ScaledHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    put_ScaledHeight: _Callable[[_type.UINT32],  # value
                                _type.HRESULT]
    get_InterpolationMode: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapInterpolationMode]],  # value
                                     _type.HRESULT]
    put_InterpolationMode: _Callable[[_enum.Windows.Graphics.Imaging.BitmapInterpolationMode],  # value
                                     _type.HRESULT]
    get_Flip: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapFlip]],  # value
                        _type.HRESULT]
    put_Flip: _Callable[[_enum.Windows.Graphics.Imaging.BitmapFlip],  # value
                        _type.HRESULT]
    get_Rotation: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapRotation]],  # value
                            _type.HRESULT]
    put_Rotation: _Callable[[_enum.Windows.Graphics.Imaging.BitmapRotation],  # value
                            _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Graphics.Imaging.BitmapBounds]],  # value
                          _type.HRESULT]
    put_Bounds: _Callable[[_struct.Windows.Graphics.Imaging.BitmapBounds],  # value
                          _type.HRESULT]


class IBitmapTypedValue(_inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Foundation.PropertyType]],  # value
                        _type.HRESULT]


class IBitmapTypedValueFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_inspectable.IInspectable,  # value
                       _enum.Windows.Foundation.PropertyType,  # type
                       _Pointer[IBitmapTypedValue]],  # bitmapTypedValue
                      _type.HRESULT]


class IPixelDataProvider(_inspectable.IInspectable):
    DetachPixelData: _Callable[[_Pointer[_type.UINT32],  # __pixelDataSize
                                _Pointer[_Pointer[_type.BYTE]]],  # pixelData
                               _type.HRESULT]


class ISoftwareBitmap(_inspectable.IInspectable):
    get_BitmapPixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]],  # value
                                     _type.HRESULT]
    get_BitmapAlphaMode: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapAlphaMode]],  # value
                                   _type.HRESULT]
    get_PixelWidth: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_PixelHeight: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_DpiX: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]
    get_DpiX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    put_DpiY: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]
    get_DpiY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    LockBuffer: _Callable[[_enum.Windows.Graphics.Imaging.BitmapBufferAccessMode,  # mode
                           _Pointer[IBitmapBuffer]],  # value
                          _type.HRESULT]
    CopyTo: _Callable[[ISoftwareBitmap],  # bitmap
                      _type.HRESULT]
    CopyFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer],  # buffer
                              _type.HRESULT]
    CopyToBuffer: _Callable[[_Windows_Storage_Streams.IBuffer],  # buffer
                            _type.HRESULT]
    GetReadOnlyView: _Callable[[_Pointer[ISoftwareBitmap]],  # value
                               _type.HRESULT]


class ISoftwareBitmapFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                       _type.INT32,  # width
                       _type.INT32,  # height
                       _Pointer[ISoftwareBitmap]],  # value
                      _type.HRESULT]
    CreateWithAlpha: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                                _type.INT32,  # width
                                _type.INT32,  # height
                                _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alpha
                                _Pointer[ISoftwareBitmap]],  # value
                               _type.HRESULT]


class ISoftwareBitmapStatics(_inspectable.IInspectable, factory=True):
    Copy: _Callable[[ISoftwareBitmap,  # source
                     _Pointer[ISoftwareBitmap]],  # value
                    _type.HRESULT]
    Convert: _Callable[[ISoftwareBitmap,  # source
                        _enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                        _Pointer[ISoftwareBitmap]],  # value
                       _type.HRESULT]
    ConvertWithAlpha: _Callable[[ISoftwareBitmap,  # source
                                 _enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                                 _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alpha
                                 _Pointer[ISoftwareBitmap]],  # value
                                _type.HRESULT]
    CreateCopyFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # source
                                     _enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                                     _type.INT32,  # width
                                     _type.INT32,  # height
                                     _Pointer[ISoftwareBitmap]],  # value
                                    _type.HRESULT]
    CreateCopyWithAlphaFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # source
                                              _enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                                              _type.INT32,  # width
                                              _type.INT32,  # height
                                              _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alpha
                                              _Pointer[ISoftwareBitmap]],  # value
                                             _type.HRESULT]
    CreateCopyFromSurfaceAsync: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # surface
                                           _Pointer[_Windows_Foundation.IAsyncOperation[ISoftwareBitmap]]],  # value
                                          _type.HRESULT]
    CreateCopyWithAlphaFromSurfaceAsync: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # surface
                                                    _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alpha
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[ISoftwareBitmap]]],  # value
                                                   _type.HRESULT]
