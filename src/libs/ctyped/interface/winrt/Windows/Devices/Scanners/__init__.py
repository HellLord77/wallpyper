from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IImageScanner(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_DefaultScanSource: _Callable[[_Pointer[_enum.Windows.Devices.Scanners.ImageScannerScanSource]],  # value
                                     _type.HRESULT]
    IsScanSourceSupported: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerScanSource,  # value
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    get_FlatbedConfiguration: _Callable[[_Pointer[IImageScannerFormatConfiguration]],  # value
                                        _type.HRESULT]
    get_FeederConfiguration: _Callable[[_Pointer[IImageScannerFormatConfiguration]],  # value
                                       _type.HRESULT]
    get_AutoConfiguration: _Callable[[_Pointer[IImageScannerFormatConfiguration]],  # value
                                     _type.HRESULT]
    IsPreviewSupported: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerScanSource,  # scanSource
                                   _Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    ScanPreviewToStreamAsync: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerScanSource,  # scanSource
                                         _Windows_Storage_Streams.IRandomAccessStream,  # targetStream
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IImageScannerPreviewResult]]],  # operation
                                        _type.HRESULT]
    ScanFilesToFolderAsync: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerScanSource,  # scanSource
                                       _Windows_Storage.IStorageFolder,  # storageFolder
                                       _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IImageScannerScanResult, _type.UINT32]]],  # operation
                                      _type.HRESULT]


class IImageScannerFeederConfiguration(_inspectable.IInspectable):
    get_CanAutoDetectPageSize: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_AutoDetectPageSize: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_AutoDetectPageSize: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_PageSize: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintMediaSize]],  # value
                            _type.HRESULT]
    put_PageSize: _Callable[[_enum.Windows.Graphics.Printing.PrintMediaSize],  # value
                            _type.HRESULT]
    get_PageOrientation: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintOrientation]],  # value
                                   _type.HRESULT]
    put_PageOrientation: _Callable[[_enum.Windows.Graphics.Printing.PrintOrientation],  # value
                                   _type.HRESULT]
    get_PageSizeDimensions: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                      _type.HRESULT]
    IsPageSizeSupported: _Callable[[_enum.Windows.Graphics.Printing.PrintMediaSize,  # pageSize
                                    _enum.Windows.Graphics.Printing.PrintOrientation,  # pageOrientation
                                    _Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    get_MaxNumberOfPages: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    put_MaxNumberOfPages: _Callable[[_type.UINT32],  # value
                                    _type.HRESULT]
    get_CanScanDuplex: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_Duplex: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Duplex: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_CanScanAhead: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_ScanAhead: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_ScanAhead: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class IImageScannerFormatConfiguration(_inspectable.IInspectable):
    get_DefaultFormat: _Callable[[_Pointer[_enum.Windows.Devices.Scanners.ImageScannerFormat]],  # value
                                 _type.HRESULT]
    get_Format: _Callable[[_Pointer[_enum.Windows.Devices.Scanners.ImageScannerFormat]],  # value
                          _type.HRESULT]
    put_Format: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerFormat],  # value
                          _type.HRESULT]
    IsFormatSupported: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerFormat,  # value
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]


class IImageScannerPreviewResult(_inspectable.IInspectable):
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Format: _Callable[[_Pointer[_enum.Windows.Devices.Scanners.ImageScannerFormat]],  # value
                          _type.HRESULT]


class IImageScannerScanResult(_inspectable.IInspectable):
    get_ScannedFiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFile]]],  # value
                                _type.HRESULT]


class IImageScannerSourceConfiguration(_inspectable.IInspectable):
    get_MinScanArea: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                               _type.HRESULT]
    get_MaxScanArea: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                               _type.HRESULT]
    get_SelectedScanRegion: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                      _type.HRESULT]
    put_SelectedScanRegion: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                      _type.HRESULT]
    get_AutoCroppingMode: _Callable[[_Pointer[_enum.Windows.Devices.Scanners.ImageScannerAutoCroppingMode]],  # value
                                    _type.HRESULT]
    put_AutoCroppingMode: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerAutoCroppingMode],  # value
                                    _type.HRESULT]
    IsAutoCroppingModeSupported: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerAutoCroppingMode,  # value
                                            _Pointer[_type.boolean]],  # result
                                           _type.HRESULT]
    get_MinResolution: _Callable[[_Pointer[_struct.Windows.Devices.Scanners.ImageScannerResolution]],  # value
                                 _type.HRESULT]
    get_MaxResolution: _Callable[[_Pointer[_struct.Windows.Devices.Scanners.ImageScannerResolution]],  # value
                                 _type.HRESULT]
    get_OpticalResolution: _Callable[[_Pointer[_struct.Windows.Devices.Scanners.ImageScannerResolution]],  # value
                                     _type.HRESULT]
    get_DesiredResolution: _Callable[[_Pointer[_struct.Windows.Devices.Scanners.ImageScannerResolution]],  # value
                                     _type.HRESULT]
    put_DesiredResolution: _Callable[[_struct.Windows.Devices.Scanners.ImageScannerResolution],  # value
                                     _type.HRESULT]
    get_ActualResolution: _Callable[[_Pointer[_struct.Windows.Devices.Scanners.ImageScannerResolution]],  # value
                                    _type.HRESULT]
    get_DefaultColorMode: _Callable[[_Pointer[_enum.Windows.Devices.Scanners.ImageScannerColorMode]],  # value
                                    _type.HRESULT]
    get_ColorMode: _Callable[[_Pointer[_enum.Windows.Devices.Scanners.ImageScannerColorMode]],  # value
                             _type.HRESULT]
    put_ColorMode: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerColorMode],  # value
                             _type.HRESULT]
    IsColorModeSupported: _Callable[[_enum.Windows.Devices.Scanners.ImageScannerColorMode,  # value
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    get_MinBrightness: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    get_MaxBrightness: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    get_BrightnessStep: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_DefaultBrightness: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_Brightness: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_Brightness: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_MinContrast: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_MaxContrast: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_ContrastStep: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_DefaultContrast: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_Contrast: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_Contrast: _Callable[[_type.INT32],  # value
                            _type.HRESULT]


class IImageScannerStatics(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IImageScanner]]],  # asyncInfo
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]
