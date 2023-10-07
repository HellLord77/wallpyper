from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Printing as _Windows_Graphics_Printing
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IIppAttributeError(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Devices.Printers.IppAttributeErrorReason]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    GetUnsupportedValues: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IIppAttributeValue]]],  # result
                                    _type.HRESULT]


class IIppAttributeValue(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Devices.Printers.IppAttributeValueKind]],  # value
                        _type.HRESULT]
    GetIntegerArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.INT32]]],  # result
                               _type.HRESULT]
    GetBooleanArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.boolean]]],  # result
                               _type.HRESULT]
    GetEnumArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.INT32]]],  # result
                            _type.HRESULT]
    GetOctetStringArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Storage_Streams.IBuffer]]],  # result
                                   _type.HRESULT]
    GetDateTimeArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Foundation.DateTime]]],  # result
                                _type.HRESULT]
    GetResolutionArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IIppResolution]]],  # result
                                  _type.HRESULT]
    GetRangeOfIntegerArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IIppIntegerRange]]],  # result
                                      _type.HRESULT]
    GetCollectionArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IIppAttributeValue]]]],  # result
                                  _type.HRESULT]
    GetTextWithLanguageArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IIppTextWithLanguage]]],  # result
                                        _type.HRESULT]
    GetNameWithLanguageArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IIppTextWithLanguage]]],  # result
                                        _type.HRESULT]
    GetTextWithoutLanguageArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                           _type.HRESULT]
    GetNameWithoutLanguageArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                           _type.HRESULT]
    GetKeywordArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                               _type.HRESULT]
    GetUriArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # result
                           _type.HRESULT]
    GetUriSchemaArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                 _type.HRESULT]
    GetCharsetArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                               _type.HRESULT]
    GetNaturalLanguageArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                       _type.HRESULT]
    GetMimeMediaTypeArray: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                     _type.HRESULT]


class IIppAttributeValueStatics(_inspectable.IInspectable, factory=True):
    CreateUnsupported: _Callable[[_Pointer[IIppAttributeValue]],  # result
                                 _type.HRESULT]
    CreateUnknown: _Callable[[_Pointer[IIppAttributeValue]],  # result
                             _type.HRESULT]
    CreateNoValue: _Callable[[_Pointer[IIppAttributeValue]],  # result
                             _type.HRESULT]
    CreateInteger: _Callable[[_type.INT32,  # value
                              _Pointer[IIppAttributeValue]],  # result
                             _type.HRESULT]
    CreateIntegerArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT32],  # values
                                   _Pointer[IIppAttributeValue]],  # result
                                  _type.HRESULT]
    CreateBoolean: _Callable[[_type.boolean,  # value
                              _Pointer[IIppAttributeValue]],  # result
                             _type.HRESULT]
    CreateBooleanArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.boolean],  # values
                                   _Pointer[IIppAttributeValue]],  # result
                                  _type.HRESULT]
    CreateEnum: _Callable[[_type.INT32,  # value
                           _Pointer[IIppAttributeValue]],  # result
                          _type.HRESULT]
    CreateEnumArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT32],  # values
                                _Pointer[IIppAttributeValue]],  # result
                               _type.HRESULT]
    CreateOctetString: _Callable[[_Windows_Storage_Streams.IBuffer,  # value
                                  _Pointer[IIppAttributeValue]],  # result
                                 _type.HRESULT]
    CreateOctetStringArray: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage_Streams.IBuffer],  # values
                                       _Pointer[IIppAttributeValue]],  # result
                                      _type.HRESULT]
    CreateDateTime: _Callable[[_struct.Windows.Foundation.DateTime,  # value
                               _Pointer[IIppAttributeValue]],  # result
                              _type.HRESULT]
    CreateDateTimeArray: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Foundation.DateTime],  # values
                                    _Pointer[IIppAttributeValue]],  # result
                                   _type.HRESULT]
    CreateResolution: _Callable[[IIppResolution,  # value
                                 _Pointer[IIppAttributeValue]],  # result
                                _type.HRESULT]
    CreateResolutionArray: _Callable[[_Windows_Foundation_Collections.IIterable[IIppResolution],  # values
                                      _Pointer[IIppAttributeValue]],  # result
                                     _type.HRESULT]
    CreateRangeOfInteger: _Callable[[IIppIntegerRange,  # value
                                     _Pointer[IIppAttributeValue]],  # result
                                    _type.HRESULT]
    CreateRangeOfIntegerArray: _Callable[[_Windows_Foundation_Collections.IIterable[IIppIntegerRange],  # values
                                          _Pointer[IIppAttributeValue]],  # result
                                         _type.HRESULT]
    CreateCollection: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IIppAttributeValue]],  # memberAttributes
                                 _Pointer[IIppAttributeValue]],  # result
                                _type.HRESULT]
    CreateCollectionArray: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IIppAttributeValue]]],  # memberAttributesArray
                                      _Pointer[IIppAttributeValue]],  # result
                                     _type.HRESULT]
    CreateTextWithLanguage: _Callable[[IIppTextWithLanguage,  # value
                                       _Pointer[IIppAttributeValue]],  # result
                                      _type.HRESULT]
    CreateTextWithLanguageArray: _Callable[[_Windows_Foundation_Collections.IIterable[IIppTextWithLanguage],  # values
                                            _Pointer[IIppAttributeValue]],  # result
                                           _type.HRESULT]
    CreateNameWithLanguage: _Callable[[IIppTextWithLanguage,  # value
                                       _Pointer[IIppAttributeValue]],  # result
                                      _type.HRESULT]
    CreateNameWithLanguageArray: _Callable[[_Windows_Foundation_Collections.IIterable[IIppTextWithLanguage],  # values
                                            _Pointer[IIppAttributeValue]],  # result
                                           _type.HRESULT]
    CreateTextWithoutLanguage: _Callable[[_type.HSTRING,  # value
                                          _Pointer[IIppAttributeValue]],  # result
                                         _type.HRESULT]
    CreateTextWithoutLanguageArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # values
                                               _Pointer[IIppAttributeValue]],  # result
                                              _type.HRESULT]
    CreateNameWithoutLanguage: _Callable[[_type.HSTRING,  # value
                                          _Pointer[IIppAttributeValue]],  # result
                                         _type.HRESULT]
    CreateNameWithoutLanguageArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # values
                                               _Pointer[IIppAttributeValue]],  # result
                                              _type.HRESULT]
    CreateKeyword: _Callable[[_type.HSTRING,  # value
                              _Pointer[IIppAttributeValue]],  # result
                             _type.HRESULT]
    CreateKeywordArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # values
                                   _Pointer[IIppAttributeValue]],  # result
                                  _type.HRESULT]
    CreateUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # value
                          _Pointer[IIppAttributeValue]],  # result
                         _type.HRESULT]
    CreateUriArray: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # values
                               _Pointer[IIppAttributeValue]],  # result
                              _type.HRESULT]
    CreateUriSchema: _Callable[[_type.HSTRING,  # value
                                _Pointer[IIppAttributeValue]],  # result
                               _type.HRESULT]
    CreateUriSchemaArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # values
                                     _Pointer[IIppAttributeValue]],  # result
                                    _type.HRESULT]
    CreateCharset: _Callable[[_type.HSTRING,  # value
                              _Pointer[IIppAttributeValue]],  # result
                             _type.HRESULT]
    CreateCharsetArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # values
                                   _Pointer[IIppAttributeValue]],  # result
                                  _type.HRESULT]
    CreateNaturalLanguage: _Callable[[_type.HSTRING,  # value
                                      _Pointer[IIppAttributeValue]],  # result
                                     _type.HRESULT]
    CreateNaturalLanguageArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # values
                                           _Pointer[IIppAttributeValue]],  # result
                                          _type.HRESULT]
    CreateMimeMedia: _Callable[[_type.HSTRING,  # value
                                _Pointer[IIppAttributeValue]],  # result
                               _type.HRESULT]
    CreateMimeMediaArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # values
                                     _Pointer[IIppAttributeValue]],  # result
                                    _type.HRESULT]


class IIppIntegerRange(_inspectable.IInspectable):
    get_Start: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    get_End: _Callable[[_Pointer[_type.INT32]],  # value
                       _type.HRESULT]


class IIppIntegerRangeFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.INT32,  # start
                               _type.INT32,  # end
                               _Pointer[IIppIntegerRange]],  # value
                              _type.HRESULT]


class IIppPrintDevice(_inspectable.IInspectable):
    get_PrinterName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PrinterUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                              _type.HRESULT]
    GetPrinterAttributesAsBuffer: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # attributeNames
                                             _Pointer[_Windows_Storage_Streams.IBuffer]],  # result
                                            _type.HRESULT]
    GetPrinterAttributes: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # attributeNames
                                     _Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, IIppAttributeValue]]],  # result
                                    _type.HRESULT]
    SetPrinterAttributesFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # printerAttributesBuffer
                                               _Pointer[IIppSetAttributesResult]],  # result
                                              _type.HRESULT]
    SetPrinterAttributes: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, IIppAttributeValue]],  # printerAttributes
                                     _Pointer[IIppSetAttributesResult]],  # result
                                    _type.HRESULT]


class IIppPrintDevice2(_inspectable.IInspectable):
    GetMaxSupportedPdfSize: _Callable[[_Pointer[_type.UINT64]],  # result
                                      _type.HRESULT]
    GetMaxSupportedPdfVersion: _Callable[[_Pointer[_type.HSTRING]],  # result
                                         _type.HRESULT]
    IsPdlPassthroughSupported: _Callable[[_type.HSTRING,  # pdlContentType
                                          _Pointer[_type.boolean]],  # result
                                         _type.HRESULT]
    GetPdlPassthroughProvider: _Callable[[_Pointer[IPdlPassthroughProvider]],  # result
                                         _type.HRESULT]


class IIppPrintDeviceStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromId: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[IIppPrintDevice]],  # result
                      _type.HRESULT]
    FromPrinterName: _Callable[[_type.HSTRING,  # printerName
                                _Pointer[IIppPrintDevice]],  # result
                               _type.HRESULT]
    IsIppPrinter: _Callable[[_type.HSTRING,  # printerName
                             _Pointer[_type.boolean]],  # result
                            _type.HRESULT]


class IIppResolution(_inspectable.IInspectable):
    get_Width: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_Unit: _Callable[[_Pointer[_enum.Windows.Devices.Printers.IppResolutionUnit]],  # value
                        _type.HRESULT]


class IIppResolutionFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.INT32,  # width
                               _type.INT32,  # height
                               _enum.Windows.Devices.Printers.IppResolutionUnit,  # unit
                               _Pointer[IIppResolution]],  # value
                              _type.HRESULT]


class IIppSetAttributesResult(_inspectable.IInspectable):
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_AttributeErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IIppAttributeError]]],  # value
                                   _type.HRESULT]


class IIppTextWithLanguage(_inspectable.IInspectable):
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IIppTextWithLanguageFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # language
                               _type.HSTRING,  # text
                               _Pointer[IIppTextWithLanguage]],  # value
                              _type.HRESULT]


class IPageConfigurationSettings(_inspectable.IInspectable):
    get_OrientationSource: _Callable[[_Pointer[_enum.Windows.Devices.Printers.PageConfigurationSource]],  # value
                                     _type.HRESULT]
    put_OrientationSource: _Callable[[_enum.Windows.Devices.Printers.PageConfigurationSource],  # value
                                     _type.HRESULT]
    get_SizeSource: _Callable[[_Pointer[_enum.Windows.Devices.Printers.PageConfigurationSource]],  # value
                              _type.HRESULT]
    put_SizeSource: _Callable[[_enum.Windows.Devices.Printers.PageConfigurationSource],  # value
                              _type.HRESULT]


class IPdlPassthroughProvider(_inspectable.IInspectable):
    get_SupportedPdlContentTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                            _type.HRESULT]
    StartPrintJobWithTaskOptions: _Callable[[_type.HSTRING,  # jobName
                                             _type.HSTRING,  # pdlContentType
                                             _Windows_Graphics_Printing.IPrintTaskOptionsCore,  # taskOptions
                                             IPageConfigurationSettings,  # pageConfigurationSettings
                                             _Pointer[IPdlPassthroughTarget]],  # result
                                            _type.HRESULT]
    StartPrintJobWithPrintTicket: _Callable[[_type.HSTRING,  # jobName
                                             _type.HSTRING,  # pdlContentType
                                             _Windows_Storage_Streams.IInputStream,  # printTicket
                                             IPageConfigurationSettings,  # pageConfigurationSettings
                                             _Pointer[IPdlPassthroughTarget]],  # result
                                            _type.HRESULT]


class IPdlPassthroughTarget(_inspectable.IInspectable):
    get_PrintJobId: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    GetOutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # result
                               _type.HRESULT]
    Submit: _Callable[[],
                      _type.HRESULT]


class IPrint3DDevice(_inspectable.IInspectable):
    get_PrintSchema: _Callable[[_Pointer[IPrintSchema]],  # value
                               _type.HRESULT]


class IPrint3DDeviceStatics(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPrint3DDevice]]],  # operation
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]


class IPrintSchema(_inspectable.IInspectable):
    GetDefaultPrintTicketAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                          _type.HRESULT]
    GetCapabilitiesAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamWithContentType,  # constrainTicket
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                    _type.HRESULT]
    MergeAndValidateWithDefaultPrintTicketAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamWithContentType,  # deltaTicket
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                                           _type.HRESULT]
