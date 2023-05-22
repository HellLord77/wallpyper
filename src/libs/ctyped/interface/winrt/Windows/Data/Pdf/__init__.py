from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IPdfDocument(_inspectable.IInspectable):
    GetPage: _Callable[[_type.UINT32,  # pageIndex
                        _Pointer[IPdfPage]],  # pdfPage
                       _type.HRESULT]
    get_PageCount: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_IsPasswordProtected: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]


class IPdfDocumentStatics(_inspectable.IInspectable, factory=True):
    LoadFromFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IPdfDocument]]],  # asyncInfo
                                 _type.HRESULT]
    LoadFromFileWithPasswordAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                              _type.HSTRING,  # password
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IPdfDocument]]],  # asyncInfo
                                             _type.HRESULT]
    LoadFromStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # inputStream
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IPdfDocument]]],  # asyncInfo
                                   _type.HRESULT]
    LoadFromStreamWithPasswordAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # inputStream
                                                _type.HSTRING,  # password
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IPdfDocument]]],  # asyncInfo
                                               _type.HRESULT]


class IPdfPage(_inspectable.IInspectable):
    RenderToStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # outputStream
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                   _type.HRESULT]
    RenderWithOptionsToStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # outputStream
                                               IPdfPageRenderOptions,  # options
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                              _type.HRESULT]
    PreparePageAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                _type.HRESULT]
    get_Index: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]
    get_Dimensions: _Callable[[_Pointer[IPdfPageDimensions]],  # value
                              _type.HRESULT]
    get_Rotation: _Callable[[_Pointer[_enum.Windows.Data.Pdf.PdfPageRotation]],  # value
                            _type.HRESULT]
    get_PreferredZoom: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]


class IPdfPageDimensions(_inspectable.IInspectable):
    get_MediaBox: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    get_CropBox: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                           _type.HRESULT]
    get_BleedBox: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    get_TrimBox: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                           _type.HRESULT]
    get_ArtBox: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]


class IPdfPageRenderOptions(_inspectable.IInspectable):
    get_SourceRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                              _type.HRESULT]
    put_SourceRect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                              _type.HRESULT]
    get_DestinationWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    put_DestinationWidth: _Callable[[_type.UINT32],  # value
                                    _type.HRESULT]
    get_DestinationHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    put_DestinationHeight: _Callable[[_type.UINT32],  # value
                                     _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_IsIgnoringHighContrast: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsIgnoringHighContrast: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_BitmapEncoderId: _Callable[[_Pointer[_struct.GUID]],  # value
                                   _type.HRESULT]
    put_BitmapEncoderId: _Callable[[_struct.GUID],  # value
                                   _type.HRESULT]
