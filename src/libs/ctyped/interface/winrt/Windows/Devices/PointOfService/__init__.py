from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Imaging as _Windows_Graphics_Imaging
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBarcodeScanner(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[IBarcodeScannerCapabilities]],  # value
                                _type.HRESULT]
    ClaimScannerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IClaimedBarcodeScanner]]],  # operation
                                 _type.HRESULT]
    CheckHealthAsync: _Callable[[_enum.Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel,  # level
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                _type.HRESULT]
    GetSupportedSymbologiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]]],  # operation
                                            _type.HRESULT]
    IsSymbologySupportedAsync: _Callable[[_type.UINT32,  # barcodeSymbology
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    RetrieveStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                                       _type.HRESULT]
    GetSupportedProfiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                    _type.HRESULT]
    IsProfileSupported: _Callable[[_type.HSTRING,  # profile
                                   _Pointer[_type.boolean]],  # isSupported
                                  _type.HRESULT]
    add_StatusUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScanner, IBarcodeScannerStatusUpdatedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IBarcodeScanner2(_inspectable.IInspectable):
    get_VideoDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IBarcodeScannerCapabilities(_inspectable.IInspectable):
    get_PowerReportingType: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.UnifiedPosPowerReportingType]],  # value
                                      _type.HRESULT]
    get_IsStatisticsReportingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_IsStatisticsUpdatingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_IsImagePreviewSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class IBarcodeScannerCapabilities1(_inspectable.IInspectable):
    get_IsSoftwareTriggerSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]


class IBarcodeScannerCapabilities2(_inspectable.IInspectable):
    get_IsVideoPreviewSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class IBarcodeScannerDataReceivedEventArgs(_inspectable.IInspectable):
    get_Report: _Callable[[_Pointer[IBarcodeScannerReport]],  # value
                          _type.HRESULT]


class IBarcodeScannerErrorOccurredEventArgs(_inspectable.IInspectable):
    get_PartialInputData: _Callable[[_Pointer[IBarcodeScannerReport]],  # value
                                    _type.HRESULT]
    get_IsRetriable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_ErrorData: _Callable[[_Pointer[IUnifiedPosErrorData]],  # value
                             _type.HRESULT]


class IBarcodeScannerImagePreviewReceivedEventArgs(_inspectable.IInspectable):
    get_Preview: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                           _type.HRESULT]


class IBarcodeScannerReport(_inspectable.IInspectable):
    get_ScanDataType: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_ScanData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                            _type.HRESULT]
    get_ScanDataLabel: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                 _type.HRESULT]


class IBarcodeScannerReportFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.UINT32,  # scanDataType
                               _Windows_Storage_Streams.IBuffer,  # scanData
                               _Windows_Storage_Streams.IBuffer,  # scanDataLabel
                               _Pointer[IBarcodeScannerReport]],  # result
                              _type.HRESULT]

    _factory = True


class IBarcodeScannerStatics(_inspectable.IInspectable):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IBarcodeScanner]]],  # result
                               _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IBarcodeScanner]]],  # result
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]

    _factory = True


class IBarcodeScannerStatics2(_inspectable.IInspectable):
    GetDeviceSelectorWithConnectionTypes: _Callable[[_enum.Windows.Devices.PointOfService.PosConnectionTypes,  # connectionTypes
                                                     _Pointer[_type.HSTRING]],  # value
                                                    _type.HRESULT]

    _factory = True


class IBarcodeScannerStatusUpdatedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.BarcodeScannerStatus]],  # value
                          _type.HRESULT]
    get_ExtendedStatus: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class IBarcodeSymbologiesStatics(_inspectable.IInspectable):
    get_Unknown: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Ean8: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Ean8Add2: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Ean8Add5: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Eanv: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_EanvAdd2: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_EanvAdd5: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Ean13: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Ean13Add2: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Ean13Add5: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Isbn: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_IsbnAdd5: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Ismn: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_IsmnAdd2: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_IsmnAdd5: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Issn: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_IssnAdd2: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_IssnAdd5: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Ean99: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Ean99Add2: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Ean99Add5: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Upca: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_UpcaAdd2: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_UpcaAdd5: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Upce: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_UpceAdd2: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_UpceAdd5: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_UpcCoupon: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_TfStd: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_TfDis: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_TfInt: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_TfInd: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_TfMat: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_TfIata: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Gs1DatabarType1: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_Gs1DatabarType2: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_Gs1DatabarType3: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_Code39: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Code39Ex: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Trioptic39: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_Code32: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Pzn: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Code93: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Code93Ex: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Code128: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Gs1128: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Gs1128Coupon: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_UccEan128: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Sisac: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Isbt: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Codabar: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Code11: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Msi: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Plessey: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Telepen: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Code16k: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_CodablockA: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_CodablockF: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_Codablock128: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_Code49: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Aztec: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_DataCode: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_DataMatrix: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_HanXin: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Maxicode: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_MicroPdf417: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_MicroQr: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Pdf417: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Qr: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_MsTag: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Ccab: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Ccc: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Tlc39: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_AusPost: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_CanPost: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_ChinaPost: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_DutchKix: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_InfoMail: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_ItalianPost25: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_ItalianPost39: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_JapanPost: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_KoreanPost: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_SwedenPost: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_UkPost: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_UsIntelligent: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_UsIntelligentPkg: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_UsPlanet: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_UsPostNet: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Us4StateFics: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_OcrA: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_OcrB: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Micr: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_ExtendedBase: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    GetName: _Callable[[_type.UINT32,  # scanDataType
                        _Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]

    _factory = True


class IBarcodeSymbologiesStatics2(_inspectable.IInspectable):
    get_Gs1DWCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]

    _factory = True


class IBarcodeSymbologyAttributes(_inspectable.IInspectable):
    get_IsCheckDigitValidationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsCheckDigitValidationEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_IsCheckDigitValidationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    get_IsCheckDigitTransmissionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_IsCheckDigitTransmissionEnabled: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_IsCheckDigitTransmissionSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    get_DecodeLength1: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    put_DecodeLength1: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_DecodeLength2: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    put_DecodeLength2: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_DecodeLengthKind: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.BarcodeSymbologyDecodeLengthKind]],  # value
                                    _type.HRESULT]
    put_DecodeLengthKind: _Callable[[_enum.Windows.Devices.PointOfService.BarcodeSymbologyDecodeLengthKind],  # value
                                    _type.HRESULT]
    get_IsDecodeLengthSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class ICashDrawer(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[ICashDrawerCapabilities]],  # value
                                _type.HRESULT]
    get_Status: _Callable[[_Pointer[ICashDrawerStatus]],  # value
                          _type.HRESULT]
    get_IsDrawerOpen: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_DrawerEventSource: _Callable[[_Pointer[ICashDrawerEventSource]],  # value
                                     _type.HRESULT]
    ClaimDrawerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IClaimedCashDrawer]]],  # operation
                                _type.HRESULT]
    CheckHealthAsync: _Callable[[_enum.Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel,  # level
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                _type.HRESULT]
    GetStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                  _type.HRESULT]
    add_StatusUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[ICashDrawer, ICashDrawerStatusUpdatedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class ICashDrawerCapabilities(_inspectable.IInspectable):
    get_PowerReportingType: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.UnifiedPosPowerReportingType]],  # value
                                      _type.HRESULT]
    get_IsStatisticsReportingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_IsStatisticsUpdatingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_IsStatusReportingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_IsStatusMultiDrawerDetectSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                      _type.HRESULT]
    get_IsDrawerOpenSensorAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class ICashDrawerCloseAlarm(_inspectable.IInspectable):
    put_AlarmTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                _type.HRESULT]
    get_AlarmTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    put_BeepFrequency: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_BeepFrequency: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    put_BeepDuration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                _type.HRESULT]
    get_BeepDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    put_BeepDelay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]
    get_BeepDelay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    add_AlarmTimeoutExpired: _Callable[[_Windows_Foundation.ITypedEventHandler[ICashDrawerCloseAlarm, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_AlarmTimeoutExpired: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                          _type.HRESULT]


class ICashDrawerEventSource(_inspectable.IInspectable):
    add_DrawerClosed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICashDrawerEventSource, ICashDrawerEventSourceEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_DrawerClosed: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_DrawerOpened: _Callable[[_Windows_Foundation.ITypedEventHandler[ICashDrawerEventSource, ICashDrawerEventSourceEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_DrawerOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class ICashDrawerEventSourceEventArgs(_inspectable.IInspectable):
    get_CashDrawer: _Callable[[_Pointer[ICashDrawer]],  # value
                              _type.HRESULT]


class ICashDrawerStatics(_inspectable.IInspectable):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ICashDrawer]]],  # result
                               _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ICashDrawer]]],  # result
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]

    _factory = True


class ICashDrawerStatics2(_inspectable.IInspectable):
    GetDeviceSelectorWithConnectionTypes: _Callable[[_enum.Windows.Devices.PointOfService.PosConnectionTypes,  # connectionTypes
                                                     _Pointer[_type.HSTRING]],  # value
                                                    _type.HRESULT]

    _factory = True


class ICashDrawerStatus(_inspectable.IInspectable):
    get_StatusKind: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.CashDrawerStatusKind]],  # value
                              _type.HRESULT]
    get_ExtendedStatus: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class ICashDrawerStatusUpdatedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[ICashDrawerStatus]],  # value
                          _type.HRESULT]


class IClaimedBarcodeScanner(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsDisabledOnDataReceived: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsDisabledOnDataReceived: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsDecodeDataEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsDecodeDataEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    EnableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                           _type.HRESULT]
    DisableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                            _type.HRESULT]
    RetainDevice: _Callable[[],
                            _type.HRESULT]
    SetActiveSymbologiesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.UINT32],  # symbologies
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                         _type.HRESULT]
    ResetStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    UpdateStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # statistics
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]
    SetActiveProfileAsync: _Callable[[_type.HSTRING,  # profile
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]
    add_DataReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedBarcodeScanner, IBarcodeScannerDataReceivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_DataReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_TriggerPressed: _Callable[[_Windows_Foundation.IEventHandler[IClaimedBarcodeScanner],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_TriggerPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_TriggerReleased: _Callable[[_Windows_Foundation.IEventHandler[IClaimedBarcodeScanner],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_TriggerReleased: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_ReleaseDeviceRequested: _Callable[[_Windows_Foundation.IEventHandler[IClaimedBarcodeScanner],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ReleaseDeviceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_ImagePreviewReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedBarcodeScanner, IBarcodeScannerImagePreviewReceivedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ImagePreviewReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_ErrorOccurred: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedBarcodeScanner, IBarcodeScannerErrorOccurredEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ErrorOccurred: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IClaimedBarcodeScanner1(_inspectable.IInspectable):
    StartSoftwareTriggerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                         _type.HRESULT]
    StopSoftwareTriggerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]


class IClaimedBarcodeScanner2(_inspectable.IInspectable):
    GetSymbologyAttributesAsync: _Callable[[_type.UINT32,  # barcodeSymbology
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IBarcodeSymbologyAttributes]]],  # result
                                           _type.HRESULT]
    SetSymbologyAttributesAsync: _Callable[[_type.UINT32,  # barcodeSymbology
                                            IBarcodeSymbologyAttributes,  # attributes
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                           _type.HRESULT]


class IClaimedBarcodeScanner3(_inspectable.IInspectable):
    ShowVideoPreviewAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    HideVideoPreview: _Callable[[],
                                _type.HRESULT]
    put_IsVideoPreviewShownOnEnable: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsVideoPreviewShownOnEnable: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IClaimedBarcodeScanner4(_inspectable.IInspectable):
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedBarcodeScanner, IClaimedBarcodeScannerClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IClaimedBarcodeScannerClosedEventArgs(_inspectable.IInspectable):
    pass


class IClaimedCashDrawer(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsDrawerOpen: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_CloseAlarm: _Callable[[_Pointer[ICashDrawerCloseAlarm]],  # value
                              _type.HRESULT]
    OpenDrawerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                               _type.HRESULT]
    EnableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                           _type.HRESULT]
    DisableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                            _type.HRESULT]
    RetainDeviceAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                 _type.HRESULT]
    ResetStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                    _type.HRESULT]
    UpdateStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # statistics
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                     _type.HRESULT]
    add_ReleaseDeviceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedCashDrawer, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ReleaseDeviceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IClaimedCashDrawer2(_inspectable.IInspectable):
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedCashDrawer, IClaimedCashDrawerClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IClaimedCashDrawerClosedEventArgs(_inspectable.IInspectable):
    pass


class IClaimedJournalPrinter(_inspectable.IInspectable):
    CreateJob: _Callable[[_Pointer[IPosPrinterJob]],  # value
                         _type.HRESULT]


class IClaimedLineDisplay(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[ILineDisplayCapabilities]],  # value
                                _type.HRESULT]
    get_PhysicalDeviceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_PhysicalDeviceDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]
    get_DeviceControlDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    get_DeviceControlVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_DeviceServiceVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_DefaultWindow: _Callable[[_Pointer[ILineDisplayWindow]],  # value
                                 _type.HRESULT]
    RetainDevice: _Callable[[],
                            _type.HRESULT]
    add_ReleaseDeviceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedLineDisplay, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ReleaseDeviceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IClaimedLineDisplay2(_inspectable.IInspectable):
    GetStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                  _type.HRESULT]
    CheckHealthAsync: _Callable[[_enum.Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel,  # level
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                _type.HRESULT]
    CheckPowerStatusAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.PointOfService.LineDisplayPowerStatus]]],  # result
                                     _type.HRESULT]
    add_StatusUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedLineDisplay, ILineDisplayStatusUpdatedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    get_SupportedScreenSizesInCharacters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Foundation.Size]]],  # value
                                                    _type.HRESULT]
    get_MaxBitmapSizeInPixels: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                         _type.HRESULT]
    get_SupportedCharacterSets: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT32]]],  # value
                                          _type.HRESULT]
    get_CustomGlyphs: _Callable[[_Pointer[ILineDisplayCustomGlyphs]],  # value
                                _type.HRESULT]
    GetAttributes: _Callable[[_Pointer[ILineDisplayAttributes]],  # value
                             _type.HRESULT]
    TryUpdateAttributesAsync: _Callable[[ILineDisplayAttributes,  # attributes
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                        _type.HRESULT]
    TrySetDescriptorAsync: _Callable[[_type.UINT32,  # descriptor
                                      _enum.Windows.Devices.PointOfService.LineDisplayDescriptorState,  # descriptorState
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    TryClearDescriptorsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                        _type.HRESULT]
    TryCreateWindowAsync: _Callable[[_struct.Windows.Foundation.Rect,  # viewport
                                     _struct.Windows.Foundation.Size,  # windowSize
                                     _Pointer[_Windows_Foundation.IAsyncOperation[ILineDisplayWindow]]],  # result
                                    _type.HRESULT]
    TryStoreStorageFileBitmapAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                               _Pointer[_Windows_Foundation.IAsyncOperation[ILineDisplayStoredBitmap]]],  # result
                                              _type.HRESULT]
    TryStoreStorageFileBitmapWithAlignmentAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                                            _enum.Windows.Devices.PointOfService.LineDisplayHorizontalAlignment,  # horizontalAlignment
                                                            _enum.Windows.Devices.PointOfService.LineDisplayVerticalAlignment,  # verticalAlignment
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[ILineDisplayStoredBitmap]]],  # result
                                                           _type.HRESULT]
    TryStoreStorageFileBitmapWithAlignmentAndWidthAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                                                    _enum.Windows.Devices.PointOfService.LineDisplayHorizontalAlignment,  # horizontalAlignment
                                                                    _enum.Windows.Devices.PointOfService.LineDisplayVerticalAlignment,  # verticalAlignment
                                                                    _type.INT32,  # widthInPixels
                                                                    _Pointer[_Windows_Foundation.IAsyncOperation[ILineDisplayStoredBitmap]]],  # result
                                                                   _type.HRESULT]


class IClaimedLineDisplay3(_inspectable.IInspectable):
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedLineDisplay, IClaimedLineDisplayClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IClaimedLineDisplayClosedEventArgs(_inspectable.IInspectable):
    pass


class IClaimedLineDisplayStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IClaimedLineDisplay]]],  # operation
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetDeviceSelectorWithConnectionTypes: _Callable[[_enum.Windows.Devices.PointOfService.PosConnectionTypes,  # connectionTypes
                                                     _Pointer[_type.HSTRING]],  # value
                                                    _type.HRESULT]

    _factory = True


class IClaimedMagneticStripeReader(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsDisabledOnDataReceived: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_IsDisabledOnDataReceived: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsDecodeDataEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsDecodeDataEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsDeviceAuthenticated: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_DataEncryptionAlgorithm: _Callable[[_type.UINT32],  # value
                                           _type.HRESULT]
    get_DataEncryptionAlgorithm: _Callable[[_Pointer[_type.UINT32]],  # value
                                           _type.HRESULT]
    put_TracksToRead: _Callable[[_enum.Windows.Devices.PointOfService.MagneticStripeReaderTrackIds],  # value
                                _type.HRESULT]
    get_TracksToRead: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderTrackIds]],  # value
                                _type.HRESULT]
    put_IsTransmitSentinelsEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_IsTransmitSentinelsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    EnableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                           _type.HRESULT]
    DisableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                            _type.HRESULT]
    RetainDevice: _Callable[[],
                            _type.HRESULT]
    SetErrorReportingType: _Callable[[_enum.Windows.Devices.PointOfService.MagneticStripeReaderErrorReportingType],  # value
                                     _type.HRESULT]
    RetrieveDeviceAuthenticationDataAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                                                     _type.HRESULT]
    AuthenticateDeviceAsync: _Callable[[_type.UINT32,  # __responseTokenSize
                                        _Pointer[_type.BYTE],  # responseToken
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                       _type.HRESULT]
    DeAuthenticateDeviceAsync: _Callable[[_type.UINT32,  # __responseTokenSize
                                          _Pointer[_type.BYTE],  # responseToken
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                         _type.HRESULT]
    UpdateKeyAsync: _Callable[[_type.HSTRING,  # key
                               _type.HSTRING,  # keyName
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                              _type.HRESULT]
    ResetStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    UpdateStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # statistics
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]
    add_BankCardDataReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedMagneticStripeReader, IMagneticStripeReaderBankCardDataReceivedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_BankCardDataReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_AamvaCardDataReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedMagneticStripeReader, IMagneticStripeReaderAamvaCardDataReceivedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_AamvaCardDataReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_VendorSpecificDataReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedMagneticStripeReader, IMagneticStripeReaderVendorSpecificCardDataReceivedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_VendorSpecificDataReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    add_ReleaseDeviceRequested: _Callable[[_Windows_Foundation.IEventHandler[IClaimedMagneticStripeReader],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ReleaseDeviceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_ErrorOccurred: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedMagneticStripeReader, IMagneticStripeReaderErrorOccurredEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ErrorOccurred: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IClaimedMagneticStripeReader2(_inspectable.IInspectable):
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedMagneticStripeReader, IClaimedMagneticStripeReaderClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IClaimedMagneticStripeReaderClosedEventArgs(_inspectable.IInspectable):
    pass


class IClaimedPosPrinter(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_CharacterSet: _Callable[[_type.UINT32],  # value
                                _type.HRESULT]
    get_CharacterSet: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_IsCoverOpen: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsCharacterSetMappingEnabled: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    get_IsCharacterSetMappingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_MapMode: _Callable[[_enum.Windows.Devices.PointOfService.PosPrinterMapMode],  # value
                           _type.HRESULT]
    get_MapMode: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterMapMode]],  # value
                           _type.HRESULT]
    get_Receipt: _Callable[[_Pointer[IClaimedReceiptPrinter]],  # value
                           _type.HRESULT]
    get_Slip: _Callable[[_Pointer[IClaimedSlipPrinter]],  # value
                        _type.HRESULT]
    get_Journal: _Callable[[_Pointer[IClaimedJournalPrinter]],  # value
                           _type.HRESULT]
    EnableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                           _type.HRESULT]
    DisableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                            _type.HRESULT]
    RetainDeviceAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                 _type.HRESULT]
    ResetStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                    _type.HRESULT]
    UpdateStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # statistics
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                     _type.HRESULT]
    add_ReleaseDeviceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedPosPrinter, IPosPrinterReleaseDeviceRequestedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ReleaseDeviceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IClaimedPosPrinter2(_inspectable.IInspectable):
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IClaimedPosPrinter, IClaimedPosPrinterClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IClaimedPosPrinterClosedEventArgs(_inspectable.IInspectable):
    pass


class IClaimedReceiptPrinter(_inspectable.IInspectable):
    get_SidewaysMaxLines: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_SidewaysMaxChars: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_LinesToPaperCut: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_PageSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                            _type.HRESULT]
    get_PrintArea: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                             _type.HRESULT]
    CreateJob: _Callable[[_Pointer[IReceiptPrintJob]],  # value
                         _type.HRESULT]


class IClaimedSlipPrinter(_inspectable.IInspectable):
    get_SidewaysMaxLines: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_SidewaysMaxChars: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_MaxLines: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_LinesNearEndToEnd: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_PrintSide: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterPrintSide]],  # value
                             _type.HRESULT]
    get_PageSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                            _type.HRESULT]
    get_PrintArea: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                             _type.HRESULT]
    OpenJaws: _Callable[[],
                        _type.HRESULT]
    CloseJaws: _Callable[[],
                         _type.HRESULT]
    InsertSlipAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # timeout
                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                               _type.HRESULT]
    RemoveSlipAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # timeout
                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                               _type.HRESULT]
    ChangePrintSide: _Callable[[_enum.Windows.Devices.PointOfService.PosPrinterPrintSide],  # printSide
                               _type.HRESULT]
    CreateJob: _Callable[[_Pointer[IReceiptOrSlipJob]],  # value
                         _type.HRESULT]


class ICommonClaimedPosPrinterStation(_inspectable.IInspectable):
    put_CharactersPerLine: _Callable[[_type.UINT32],  # value
                                     _type.HRESULT]
    get_CharactersPerLine: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    put_LineHeight: _Callable[[_type.UINT32],  # value
                              _type.HRESULT]
    get_LineHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    put_LineSpacing: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_LineSpacing: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_LineWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_IsLetterQuality: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsLetterQuality: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsPaperNearEnd: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_ColorCartridge: _Callable[[_enum.Windows.Devices.PointOfService.PosPrinterColorCartridge],  # value
                                  _type.HRESULT]
    get_ColorCartridge: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterColorCartridge]],  # value
                                  _type.HRESULT]
    get_IsCoverOpen: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsCartridgeRemoved: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsCartridgeEmpty: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsHeadCleaning: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_IsPaperEmpty: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_IsReadyToPrint: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    ValidateData: _Callable[[_type.HSTRING,  # data
                             _Pointer[_type.boolean]],  # result
                            _type.HRESULT]


class ICommonPosPrintStationCapabilities(_inspectable.IInspectable):
    get_IsPrinterPresent: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsDualColorSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_ColorCartridgeCapabilities: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterColorCapabilities]],  # value
                                              _type.HRESULT]
    get_CartridgeSensors: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterCartridgeSensors]],  # value
                                    _type.HRESULT]
    get_IsBoldSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsItalicSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsUnderlineSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsDoubleHighPrintSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_IsDoubleWidePrintSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_IsDoubleHighDoubleWidePrintSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                        _type.HRESULT]
    get_IsPaperEmptySensorSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_IsPaperNearEndSensorSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_SupportedCharactersPerLine: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                              _type.HRESULT]


class ICommonReceiptSlipCapabilities(_inspectable.IInspectable):
    get_IsBarcodeSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsBitmapSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsLeft90RotationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_IsRight90RotationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_Is180RotationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsPrintAreaSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_RuledLineCapabilities: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterRuledLineCapabilities]],  # value
                                         _type.HRESULT]
    get_SupportedBarcodeRotations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.PointOfService.PosPrinterRotation]]],  # value
                                             _type.HRESULT]
    get_SupportedBitmapRotations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.PointOfService.PosPrinterRotation]]],  # value
                                            _type.HRESULT]


class IJournalPrintJob(_inspectable.IInspectable):
    Print: _Callable[[_type.HSTRING,  # data
                      IPosPrinterPrintOptions],  # printOptions
                     _type.HRESULT]
    FeedPaperByLine: _Callable[[_type.INT32],  # lineCount
                               _type.HRESULT]
    FeedPaperByMapModeUnit: _Callable[[_type.INT32],  # distance
                                      _type.HRESULT]


class IJournalPrinterCapabilities(_inspectable.IInspectable):
    pass


class IJournalPrinterCapabilities2(_inspectable.IInspectable):
    get_IsReverseVideoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_IsStrikethroughSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsSuperscriptSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsSubscriptSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsReversePaperFeedByLineSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    get_IsReversePaperFeedByMapModeUnitSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                            _type.HRESULT]


class ILineDisplay(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[ILineDisplayCapabilities]],  # value
                                _type.HRESULT]
    get_PhysicalDeviceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_PhysicalDeviceDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]
    get_DeviceControlDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    get_DeviceControlVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_DeviceServiceVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    ClaimAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IClaimedLineDisplay]]],  # result
                          _type.HRESULT]


class ILineDisplay2(_inspectable.IInspectable):
    CheckPowerStatusAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.PointOfService.LineDisplayPowerStatus]]],  # result
                                     _type.HRESULT]


class ILineDisplayAttributes(_inspectable.IInspectable):
    get_IsPowerNotifyEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsPowerNotifyEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_Brightness: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_Brightness: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_BlinkRate: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    put_BlinkRate: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]
    get_ScreenSizeInCharacters: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                          _type.HRESULT]
    put_ScreenSizeInCharacters: _Callable[[_struct.Windows.Foundation.Size],  # value
                                          _type.HRESULT]
    get_CharacterSet: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    put_CharacterSet: _Callable[[_type.INT32],  # value
                                _type.HRESULT]
    get_IsCharacterSetMappingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_IsCharacterSetMappingEnabled: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    get_CurrentWindow: _Callable[[_Pointer[ILineDisplayWindow]],  # value
                                 _type.HRESULT]
    put_CurrentWindow: _Callable[[ILineDisplayWindow],  # value
                                 _type.HRESULT]


class ILineDisplayCapabilities(_inspectable.IInspectable):
    get_IsStatisticsReportingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_IsStatisticsUpdatingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_PowerReportingType: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.UnifiedPosPowerReportingType]],  # value
                                      _type.HRESULT]
    get_CanChangeScreenSize: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_CanDisplayBitmaps: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_CanReadCharacterAtCursor: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_CanMapCharacterSets: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_CanDisplayCustomGlyphs: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_CanReverse: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.LineDisplayTextAttributeGranularity]],  # value
                              _type.HRESULT]
    get_CanBlink: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.LineDisplayTextAttributeGranularity]],  # value
                            _type.HRESULT]
    get_CanChangeBlinkRate: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsBrightnessSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_IsCursorSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsHorizontalMarqueeSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_IsVerticalMarqueeSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_IsInterCharacterWaitSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_SupportedDescriptors: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    get_SupportedWindows: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]


class ILineDisplayCursor(_inspectable.IInspectable):
    get_CanCustomize: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_IsBlinkSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsBlockSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsHalfBlockSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsUnderlineSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsReverseSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsOtherSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    GetAttributes: _Callable[[_Pointer[ILineDisplayCursorAttributes]],  # result
                             _type.HRESULT]
    TryUpdateAttributesAsync: _Callable[[ILineDisplayCursorAttributes,  # attributes
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                        _type.HRESULT]


class ILineDisplayCursorAttributes(_inspectable.IInspectable):
    get_IsBlinkEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsBlinkEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_CursorType: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.LineDisplayCursorType]],  # value
                              _type.HRESULT]
    put_CursorType: _Callable[[_enum.Windows.Devices.PointOfService.LineDisplayCursorType],  # value
                              _type.HRESULT]
    get_IsAutoAdvanceEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsAutoAdvanceEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.Point],  # value
                            _type.HRESULT]


class ILineDisplayCustomGlyphs(_inspectable.IInspectable):
    get_SizeInPixels: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                _type.HRESULT]
    get_SupportedGlyphCodes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                       _type.HRESULT]
    TryRedefineAsync: _Callable[[_type.UINT32,  # glyphCode
                                 _Windows_Storage_Streams.IBuffer,  # glyphData
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                _type.HRESULT]


class ILineDisplayMarquee(_inspectable.IInspectable):
    get_Format: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.LineDisplayMarqueeFormat]],  # value
                          _type.HRESULT]
    put_Format: _Callable[[_enum.Windows.Devices.PointOfService.LineDisplayMarqueeFormat],  # value
                          _type.HRESULT]
    get_RepeatWaitInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    put_RepeatWaitInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                      _type.HRESULT]
    get_ScrollWaitInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    put_ScrollWaitInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                      _type.HRESULT]
    TryStartScrollingAsync: _Callable[[_enum.Windows.Devices.PointOfService.LineDisplayScrollDirection,  # direction
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]
    TryStopScrollingAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]


class ILineDisplayStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ILineDisplay]]],  # operation
                           _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ILineDisplay]]],  # result
                               _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetDeviceSelectorWithConnectionTypes: _Callable[[_enum.Windows.Devices.PointOfService.PosConnectionTypes,  # connectionTypes
                                                     _Pointer[_type.HSTRING]],  # value
                                                    _type.HRESULT]

    _factory = True


class ILineDisplayStatics2(_inspectable.IInspectable):
    get_StatisticsCategorySelector: _Callable[[_Pointer[ILineDisplayStatisticsCategorySelector]],  # value
                                              _type.HRESULT]

    _factory = True


class ILineDisplayStatisticsCategorySelector(_inspectable.IInspectable):
    get_AllStatistics: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_UnifiedPosStatistics: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_ManufacturerStatistics: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]


class ILineDisplayStatusUpdatedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.LineDisplayPowerStatus]],  # value
                          _type.HRESULT]


class ILineDisplayStoredBitmap(_inspectable.IInspectable):
    get_EscapeSequence: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    TryDeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]


class ILineDisplayWindow(_inspectable.IInspectable):
    get_SizeInCharacters: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                    _type.HRESULT]
    get_InterCharacterWaitInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                              _type.HRESULT]
    put_InterCharacterWaitInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                              _type.HRESULT]
    TryRefreshAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                               _type.HRESULT]
    TryDisplayTextAsync: _Callable[[_type.HSTRING,  # text
                                    _enum.Windows.Devices.PointOfService.LineDisplayTextAttribute,  # displayAttribute
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                   _type.HRESULT]
    TryDisplayTextAtPositionAsync: _Callable[[_type.HSTRING,  # text
                                              _enum.Windows.Devices.PointOfService.LineDisplayTextAttribute,  # displayAttribute
                                              _struct.Windows.Foundation.Point,  # startPosition
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                             _type.HRESULT]
    TryDisplayTextNormalAsync: _Callable[[_type.HSTRING,  # text
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    TryScrollTextAsync: _Callable[[_enum.Windows.Devices.PointOfService.LineDisplayScrollDirection,  # direction
                                   _type.UINT32,  # numberOfColumnsOrRows
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                  _type.HRESULT]
    TryClearTextAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                 _type.HRESULT]


class ILineDisplayWindow2(_inspectable.IInspectable):
    get_Cursor: _Callable[[_Pointer[ILineDisplayCursor]],  # value
                          _type.HRESULT]
    get_Marquee: _Callable[[_Pointer[ILineDisplayMarquee]],  # value
                           _type.HRESULT]
    ReadCharacterAtCursorAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # result
                                          _type.HRESULT]
    TryDisplayStoredBitmapAtCursorAsync: _Callable[[ILineDisplayStoredBitmap,  # bitmap
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                   _type.HRESULT]
    TryDisplayStorageFileBitmapAtCursorAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                        _type.HRESULT]
    TryDisplayStorageFileBitmapAtCursorWithAlignmentAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                                                      _enum.Windows.Devices.PointOfService.LineDisplayHorizontalAlignment,  # horizontalAlignment
                                                                      _enum.Windows.Devices.PointOfService.LineDisplayVerticalAlignment,  # verticalAlignment
                                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                                     _type.HRESULT]
    TryDisplayStorageFileBitmapAtCursorWithAlignmentAndWidthAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                                                              _enum.Windows.Devices.PointOfService.LineDisplayHorizontalAlignment,  # horizontalAlignment
                                                                              _enum.Windows.Devices.PointOfService.LineDisplayVerticalAlignment,  # verticalAlignment
                                                                              _type.INT32,  # widthInPixels
                                                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                                             _type.HRESULT]
    TryDisplayStorageFileBitmapAtPointAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                                        _struct.Windows.Foundation.Point,  # offsetInPixels
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                       _type.HRESULT]
    TryDisplayStorageFileBitmapAtPointWithWidthAsync: _Callable[[_Windows_Storage.IStorageFile,  # bitmap
                                                                 _struct.Windows.Foundation.Point,  # offsetInPixels
                                                                 _type.INT32,  # widthInPixels
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                                _type.HRESULT]


class IMagneticStripeReader(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[IMagneticStripeReaderCapabilities]],  # value
                                _type.HRESULT]
    get_SupportedCardTypes: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                       _Pointer[_Pointer[_type.UINT32]]],  # value
                                      _type.HRESULT]
    get_DeviceAuthenticationProtocol: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderAuthenticationProtocol]],  # value
                                                _type.HRESULT]
    CheckHealthAsync: _Callable[[_enum.Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel,  # level
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                _type.HRESULT]
    ClaimReaderAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IClaimedMagneticStripeReader]]],  # operation
                                _type.HRESULT]
    RetrieveStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                                       _type.HRESULT]
    GetErrorReportingType: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderErrorReportingType]],  # value
                                     _type.HRESULT]
    add_StatusUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IMagneticStripeReader, IMagneticStripeReaderStatusUpdatedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IMagneticStripeReaderAamvaCardDataReceivedEventArgs(_inspectable.IInspectable):
    get_Report: _Callable[[_Pointer[IMagneticStripeReaderReport]],  # value
                          _type.HRESULT]
    get_LicenseNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Restrictions: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Class: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Endorsements: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_BirthDate: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_FirstName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Surname: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Suffix: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Gender: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_HairColor: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_EyeColor: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Weight: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Address: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_City: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_State: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_PostalCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IMagneticStripeReaderBankCardDataReceivedEventArgs(_inspectable.IInspectable):
    get_Report: _Callable[[_Pointer[IMagneticStripeReaderReport]],  # value
                          _type.HRESULT]
    get_AccountNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_ServiceCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_FirstName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_MiddleInitial: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Surname: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Suffix: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IMagneticStripeReaderCapabilities(_inspectable.IInspectable):
    get_CardAuthentication: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_SupportedEncryptionAlgorithms: _Callable[[_Pointer[_type.UINT32]],  # value
                                                 _type.HRESULT]
    get_AuthenticationLevel: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderAuthenticationLevel]],  # value
                                       _type.HRESULT]
    get_IsIsoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_IsJisOneSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsJisTwoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_PowerReportingType: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.UnifiedPosPowerReportingType]],  # value
                                      _type.HRESULT]
    get_IsStatisticsReportingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_IsStatisticsUpdatingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_IsTrackDataMaskingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_IsTransmitSentinelsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]


class IMagneticStripeReaderCardTypesStatics(_inspectable.IInspectable):
    get_Unknown: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Bank: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Aamva: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_ExtendedBase: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]

    _factory = True


class IMagneticStripeReaderEncryptionAlgorithmsStatics(_inspectable.IInspectable):
    get_None: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_TripleDesDukpt: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_ExtendedBase: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]

    _factory = True


class IMagneticStripeReaderErrorOccurredEventArgs(_inspectable.IInspectable):
    get_Track1Status: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType]],  # value
                                _type.HRESULT]
    get_Track2Status: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType]],  # value
                                _type.HRESULT]
    get_Track3Status: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType]],  # value
                                _type.HRESULT]
    get_Track4Status: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType]],  # value
                                _type.HRESULT]
    get_ErrorData: _Callable[[_Pointer[IUnifiedPosErrorData]],  # value
                             _type.HRESULT]
    get_PartialInputData: _Callable[[_Pointer[IMagneticStripeReaderReport]],  # value
                                    _type.HRESULT]


class IMagneticStripeReaderReport(_inspectable.IInspectable):
    get_CardType: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Track1: _Callable[[_Pointer[IMagneticStripeReaderTrackData]],  # value
                          _type.HRESULT]
    get_Track2: _Callable[[_Pointer[IMagneticStripeReaderTrackData]],  # value
                          _type.HRESULT]
    get_Track3: _Callable[[_Pointer[IMagneticStripeReaderTrackData]],  # value
                          _type.HRESULT]
    get_Track4: _Callable[[_Pointer[IMagneticStripeReaderTrackData]],  # value
                          _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                              _type.HRESULT]
    get_CardAuthenticationData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                          _type.HRESULT]
    get_CardAuthenticationDataLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                                _type.HRESULT]
    get_AdditionalSecurityInformation: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                                 _type.HRESULT]


class IMagneticStripeReaderStatics(_inspectable.IInspectable):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMagneticStripeReader]]],  # result
                               _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IMagneticStripeReader]]],  # result
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]

    _factory = True


class IMagneticStripeReaderStatics2(_inspectable.IInspectable):
    GetDeviceSelectorWithConnectionTypes: _Callable[[_enum.Windows.Devices.PointOfService.PosConnectionTypes,  # connectionTypes
                                                     _Pointer[_type.HSTRING]],  # value
                                                    _type.HRESULT]

    _factory = True


class IMagneticStripeReaderStatusUpdatedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.MagneticStripeReaderStatus]],  # value
                          _type.HRESULT]
    get_ExtendedStatus: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class IMagneticStripeReaderTrackData(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    get_DiscretionaryData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                     _type.HRESULT]
    get_EncryptedData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                 _type.HRESULT]


class IMagneticStripeReaderVendorSpecificCardDataReceivedEventArgs(_inspectable.IInspectable):
    get_Report: _Callable[[_Pointer[IMagneticStripeReaderReport]],  # value
                          _type.HRESULT]


class IPosPrinter(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Capabilities: _Callable[[_Pointer[IPosPrinterCapabilities]],  # value
                                _type.HRESULT]
    get_SupportedCharacterSets: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                          _type.HRESULT]
    get_SupportedTypeFaces: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_Status: _Callable[[_Pointer[IPosPrinterStatus]],  # value
                          _type.HRESULT]
    ClaimPrinterAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IClaimedPosPrinter]]],  # operation
                                 _type.HRESULT]
    CheckHealthAsync: _Callable[[_enum.Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel,  # level
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                _type.HRESULT]
    GetStatisticsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # statisticsCategories
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                  _type.HRESULT]
    add_StatusUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IPosPrinter, IPosPrinterStatusUpdatedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IPosPrinter2(_inspectable.IInspectable):
    get_SupportedBarcodeSymbologies: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                               _type.HRESULT]
    GetFontProperty: _Callable[[_type.HSTRING,  # typeface
                                _Pointer[IPosPrinterFontProperty]],  # result
                               _type.HRESULT]


class IPosPrinterCapabilities(_inspectable.IInspectable):
    get_PowerReportingType: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.UnifiedPosPowerReportingType]],  # value
                                      _type.HRESULT]
    get_IsStatisticsReportingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_IsStatisticsUpdatingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_DefaultCharacterSet: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]
    get_HasCoverSensor: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_CanMapCharacterSet: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsTransactionSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_Receipt: _Callable[[_Pointer[IReceiptPrinterCapabilities]],  # value
                           _type.HRESULT]
    get_Slip: _Callable[[_Pointer[ISlipPrinterCapabilities]],  # value
                        _type.HRESULT]
    get_Journal: _Callable[[_Pointer[IJournalPrinterCapabilities]],  # value
                           _type.HRESULT]


class IPosPrinterCharacterSetIdsStatics(_inspectable.IInspectable):
    get_Utf16LE: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Ascii: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Ansi: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]

    _factory = True


class IPosPrinterFontProperty(_inspectable.IInspectable):
    get_TypeFace: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsScalableToAnySize: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_CharacterSizes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Devices.PointOfService.SizeUInt32]]],  # value
                                  _type.HRESULT]


class IPosPrinterJob(_inspectable.IInspectable):
    Print: _Callable[[_type.HSTRING],  # data
                     _type.HRESULT]
    PrintLine: _Callable[[_type.HSTRING],  # data
                         _type.HRESULT]
    PrintNewline: _Callable[[],
                            _type.HRESULT]
    ExecuteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                            _type.HRESULT]


class IPosPrinterPrintOptions(_inspectable.IInspectable):
    get_TypeFace: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_TypeFace: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_CharacterHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    put_CharacterHeight: _Callable[[_type.UINT32],  # value
                                   _type.HRESULT]
    get_Bold: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    put_Bold: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    get_Italic: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Italic: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Underline: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_Underline: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_ReverseVideo: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_ReverseVideo: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_Strikethrough: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_Strikethrough: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_Superscript: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_Superscript: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_Subscript: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_Subscript: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_DoubleWide: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_DoubleWide: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_DoubleHigh: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_DoubleHigh: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_Alignment: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterAlignment]],  # value
                             _type.HRESULT]
    put_Alignment: _Callable[[_enum.Windows.Devices.PointOfService.PosPrinterAlignment],  # value
                             _type.HRESULT]
    get_CharacterSet: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    put_CharacterSet: _Callable[[_type.UINT32],  # value
                                _type.HRESULT]


class IPosPrinterReleaseDeviceRequestedEventArgs(_inspectable.IInspectable):
    pass


class IPosPrinterStatics(_inspectable.IInspectable):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPosPrinter]]],  # result
                               _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPosPrinter]]],  # result
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]

    _factory = True


class IPosPrinterStatics2(_inspectable.IInspectable):
    GetDeviceSelectorWithConnectionTypes: _Callable[[_enum.Windows.Devices.PointOfService.PosConnectionTypes,  # connectionTypes
                                                     _Pointer[_type.HSTRING]],  # value
                                                    _type.HRESULT]

    _factory = True


class IPosPrinterStatus(_inspectable.IInspectable):
    get_StatusKind: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterStatusKind]],  # value
                              _type.HRESULT]
    get_ExtendedStatus: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class IPosPrinterStatusUpdatedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[IPosPrinterStatus]],  # value
                          _type.HRESULT]


class IReceiptOrSlipJob(_inspectable.IInspectable):
    SetBarcodeRotation: _Callable[[_enum.Windows.Devices.PointOfService.PosPrinterRotation],  # value
                                  _type.HRESULT]
    SetPrintRotation: _Callable[[_enum.Windows.Devices.PointOfService.PosPrinterRotation,  # value
                                 _type.boolean],  # includeBitmaps
                                _type.HRESULT]
    SetPrintArea: _Callable[[_struct.Windows.Foundation.Rect],  # value
                            _type.HRESULT]
    SetBitmap: _Callable[[_type.UINT32,  # bitmapNumber
                          _Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                          _enum.Windows.Devices.PointOfService.PosPrinterAlignment],  # alignment
                         _type.HRESULT]
    SetBitmapCustomWidthStandardAlign: _Callable[[_type.UINT32,  # bitmapNumber
                                                  _Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                                                  _enum.Windows.Devices.PointOfService.PosPrinterAlignment,  # alignment
                                                  _type.UINT32],  # width
                                                 _type.HRESULT]
    SetCustomAlignedBitmap: _Callable[[_type.UINT32,  # bitmapNumber
                                       _Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                                       _type.UINT32],  # alignmentDistance
                                      _type.HRESULT]
    SetBitmapCustomWidthCustomAlign: _Callable[[_type.UINT32,  # bitmapNumber
                                                _Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                                                _type.UINT32,  # alignmentDistance
                                                _type.UINT32],  # width
                                               _type.HRESULT]
    PrintSavedBitmap: _Callable[[_type.UINT32],  # bitmapNumber
                                _type.HRESULT]
    DrawRuledLine: _Callable[[_type.HSTRING,  # positionList
                              _enum.Windows.Devices.PointOfService.PosPrinterLineDirection,  # lineDirection
                              _type.UINT32,  # lineWidth
                              _enum.Windows.Devices.PointOfService.PosPrinterLineStyle,  # lineStyle
                              _type.UINT32],  # lineColor
                             _type.HRESULT]
    PrintBarcode: _Callable[[_type.HSTRING,  # data
                             _type.UINT32,  # symbology
                             _type.UINT32,  # height
                             _type.UINT32,  # width
                             _enum.Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition,  # textPosition
                             _enum.Windows.Devices.PointOfService.PosPrinterAlignment],  # alignment
                            _type.HRESULT]
    PrintBarcodeCustomAlign: _Callable[[_type.HSTRING,  # data
                                        _type.UINT32,  # symbology
                                        _type.UINT32,  # height
                                        _type.UINT32,  # width
                                        _enum.Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition,  # textPosition
                                        _type.UINT32],  # alignmentDistance
                                       _type.HRESULT]
    PrintBitmap: _Callable[[_Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                            _enum.Windows.Devices.PointOfService.PosPrinterAlignment],  # alignment
                           _type.HRESULT]
    PrintBitmapCustomWidthStandardAlign: _Callable[[_Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                                                    _enum.Windows.Devices.PointOfService.PosPrinterAlignment,  # alignment
                                                    _type.UINT32],  # width
                                                   _type.HRESULT]
    PrintCustomAlignedBitmap: _Callable[[_Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                                         _type.UINT32],  # alignmentDistance
                                        _type.HRESULT]
    PrintBitmapCustomWidthCustomAlign: _Callable[[_Windows_Graphics_Imaging.IBitmapFrame,  # bitmap
                                                  _type.UINT32,  # alignmentDistance
                                                  _type.UINT32],  # width
                                                 _type.HRESULT]


class IReceiptPrintJob(_inspectable.IInspectable):
    MarkFeed: _Callable[[_enum.Windows.Devices.PointOfService.PosPrinterMarkFeedKind],  # kind
                        _type.HRESULT]
    CutPaper: _Callable[[_type.DOUBLE],  # percentage
                        _type.HRESULT]
    CutPaperDefault: _Callable[[],
                               _type.HRESULT]


class IReceiptPrintJob2(_inspectable.IInspectable):
    StampPaper: _Callable[[],
                          _type.HRESULT]
    Print: _Callable[[_type.HSTRING,  # data
                      IPosPrinterPrintOptions],  # printOptions
                     _type.HRESULT]
    FeedPaperByLine: _Callable[[_type.INT32],  # lineCount
                               _type.HRESULT]
    FeedPaperByMapModeUnit: _Callable[[_type.INT32],  # distance
                                      _type.HRESULT]


class IReceiptPrinterCapabilities(_inspectable.IInspectable):
    get_CanCutPaper: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsStampSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_MarkFeedCapabilities: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.PosPrinterMarkFeedCapabilities]],  # value
                                        _type.HRESULT]


class IReceiptPrinterCapabilities2(_inspectable.IInspectable):
    get_IsReverseVideoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_IsStrikethroughSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsSuperscriptSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsSubscriptSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsReversePaperFeedByLineSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    get_IsReversePaperFeedByMapModeUnitSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                            _type.HRESULT]


class ISlipPrintJob(_inspectable.IInspectable):
    Print: _Callable[[_type.HSTRING,  # data
                      IPosPrinterPrintOptions],  # printOptions
                     _type.HRESULT]
    FeedPaperByLine: _Callable[[_type.INT32],  # lineCount
                               _type.HRESULT]
    FeedPaperByMapModeUnit: _Callable[[_type.INT32],  # distance
                                      _type.HRESULT]


class ISlipPrinterCapabilities(_inspectable.IInspectable):
    get_IsFullLengthSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_IsBothSidesPrintingSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]


class ISlipPrinterCapabilities2(_inspectable.IInspectable):
    get_IsReverseVideoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_IsStrikethroughSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsSuperscriptSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsSubscriptSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsReversePaperFeedByLineSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    get_IsReversePaperFeedByMapModeUnitSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                            _type.HRESULT]


class IUnifiedPosErrorData(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Severity: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.UnifiedPosErrorSeverity]],  # value
                            _type.HRESULT]
    get_Reason: _Callable[[_Pointer[_enum.Windows.Devices.PointOfService.UnifiedPosErrorReason]],  # value
                          _type.HRESULT]
    get_ExtendedReason: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class IUnifiedPosErrorDataFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.HSTRING,  # message
                               _enum.Windows.Devices.PointOfService.UnifiedPosErrorSeverity,  # severity
                               _enum.Windows.Devices.PointOfService.UnifiedPosErrorReason,  # reason
                               _type.UINT32,  # extendedReason
                               _Pointer[IUnifiedPosErrorData]],  # result
                              _type.HRESULT]

    _factory = True
