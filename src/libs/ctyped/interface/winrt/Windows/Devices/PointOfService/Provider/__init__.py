from __future__ import annotations as _

from typing import Callable as _Callable

from ... import PointOfService as _Windows_Devices_PointOfService
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IBarcodeScannerDisableScannerRequest(_inspectable.IInspectable):
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerDisableScannerRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerDisableScannerRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerDisableScannerRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerEnableScannerRequest(_inspectable.IInspectable):
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerEnableScannerRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerEnableScannerRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerEnableScannerRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerFrameReader(_inspectable.IInspectable):
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                          _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    TryAcquireLatestFrameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IBarcodeScannerVideoFrame]]],  # operation
                                          _type.HRESULT]
    get_Connection: _Callable[[_Pointer[IBarcodeScannerProviderConnection]],  # value
                              _type.HRESULT]
    add_FrameArrived: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerFrameReader, IBarcodeScannerFrameReaderFrameArrivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IBarcodeScannerFrameReaderFrameArrivedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerGetSymbologyAttributesRequest(_inspectable.IInspectable):
    get_Symbology: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_Devices_PointOfService.IBarcodeSymbologyAttributes,  # attributes
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerGetSymbologyAttributesRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerGetSymbologyAttributesRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerGetSymbologyAttributesRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerHideVideoPreviewRequest(_inspectable.IInspectable):
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerHideVideoPreviewRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerHideVideoPreviewRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerHideVideoPreviewRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerProviderConnection(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_VideoDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_SupportedSymbologies: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.UINT32]]],  # value
                                        _type.HRESULT]
    get_CompanyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_CompanyName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Version: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    ReportScannedDataAsync: _Callable[[_Windows_Devices_PointOfService.IBarcodeScannerReport,  # report
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                      _type.HRESULT]
    ReportTriggerStateAsync: _Callable[[_enum.Windows.Devices.PointOfService.Provider.BarcodeScannerTriggerState,  # state
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                       _type.HRESULT]
    ReportErrorAsync: _Callable[[_Windows_Devices_PointOfService.IUnifiedPosErrorData,  # errorData
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
    ReportErrorAsyncWithScanReport: _Callable[[_Windows_Devices_PointOfService.IUnifiedPosErrorData,  # errorData
                                               _type.boolean,  # isRetriable
                                               _Windows_Devices_PointOfService.IBarcodeScannerReport,  # scanReport
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]
    add_EnableScannerRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerEnableScannerRequestEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_EnableScannerRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_DisableScannerRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerDisableScannerRequestEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_DisableScannerRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_SetActiveSymbologiesRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerSetActiveSymbologiesRequestEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_SetActiveSymbologiesRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_StartSoftwareTriggerRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerStartSoftwareTriggerRequestEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_StartSoftwareTriggerRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_StopSoftwareTriggerRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerStopSoftwareTriggerRequestEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_StopSoftwareTriggerRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    add_GetBarcodeSymbologyAttributesRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerGetSymbologyAttributesRequestEventArgs],  # handler
                                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                                          _type.HRESULT]
    remove_GetBarcodeSymbologyAttributesRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                             _type.HRESULT]
    add_SetBarcodeSymbologyAttributesRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerSetSymbologyAttributesRequestEventArgs],  # handler
                                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                                          _type.HRESULT]
    remove_SetBarcodeSymbologyAttributesRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                             _type.HRESULT]
    add_HideVideoPreviewRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IBarcodeScannerProviderConnection, IBarcodeScannerHideVideoPreviewRequestEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_HideVideoPreviewRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]


class IBarcodeScannerProviderConnection2(_inspectable.IInspectable):
    CreateFrameReaderAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IBarcodeScannerFrameReader]]],  # operation
                                      _type.HRESULT]
    CreateFrameReaderWithFormatAsync: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # preferredFormat
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IBarcodeScannerFrameReader]]],  # operation
                                                _type.HRESULT]
    CreateFrameReaderWithFormatAndSizeAsync: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # preferredFormat
                                                        _struct.Windows.Graphics.Imaging.BitmapSize,  # preferredSize
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IBarcodeScannerFrameReader]]],  # operation
                                                       _type.HRESULT]


class IBarcodeScannerProviderTriggerDetails(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IBarcodeScannerProviderConnection]],  # value
                              _type.HRESULT]


class IBarcodeScannerSetActiveSymbologiesRequest(_inspectable.IInspectable):
    get_Symbologies: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                               _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerSetActiveSymbologiesRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerSetActiveSymbologiesRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerSetActiveSymbologiesRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerSetSymbologyAttributesRequest(_inspectable.IInspectable):
    get_Symbology: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Attributes: _Callable[[_Pointer[_Windows_Devices_PointOfService.IBarcodeSymbologyAttributes]],  # value
                              _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerSetSymbologyAttributesRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerSetSymbologyAttributesRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerSetSymbologyAttributesRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerStartSoftwareTriggerRequest(_inspectable.IInspectable):
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerStartSoftwareTriggerRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerStartSoftwareTriggerRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerStartSoftwareTriggerRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerStopSoftwareTriggerRequest(_inspectable.IInspectable):
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IBarcodeScannerStopSoftwareTriggerRequest2(_inspectable.IInspectable):
    ReportFailedWithFailedReasonAsync: _Callable[[_type.INT32,  # reason
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                 _type.HRESULT]
    ReportFailedWithFailedReasonAndDescriptionAsync: _Callable[[_type.INT32,  # reason
                                                                _type.HSTRING,  # failedReasonDescription
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                               _type.HRESULT]


class IBarcodeScannerStopSoftwareTriggerRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IBarcodeScannerStopSoftwareTriggerRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBarcodeScannerVideoFrame(_inspectable.IInspectable):
    get_Format: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]],  # value
                          _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_PixelData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                             _type.HRESULT]


class IBarcodeSymbologyAttributesBuilder(_inspectable.IInspectable):
    get_IsCheckDigitValidationSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_IsCheckDigitValidationSupported: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_IsCheckDigitTransmissionSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_IsCheckDigitTransmissionSupported: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_IsDecodeLengthSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsDecodeLengthSupported: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    CreateAttributes: _Callable[[_Pointer[_Windows_Devices_PointOfService.IBarcodeSymbologyAttributes]],  # value
                                _type.HRESULT]
