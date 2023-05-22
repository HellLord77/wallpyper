from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...ApplicationModel import DataTransfer as _Windows_ApplicationModel_DataTransfer
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IPrintTaskSourceRequestedHandler:
    Invoke: _Callable[[IPrintTaskSourceRequestedArgs],  # args
                      _type.HRESULT]


class IPrintTaskSourceRequestedHandler(_IPrintTaskSourceRequestedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPrintTaskSourceRequestedHandler_impl(_IPrintTaskSourceRequestedHandler, _Unknwnbase.IUnknown_impl):
    pass


class IPrintDocumentSource(_inspectable.IInspectable):
    pass


class IPrintManager(_inspectable.IInspectable):
    add_PrintTaskRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintManager, IPrintTaskRequestedEventArgs],  # eventHandler
                                       _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                      _type.HRESULT]
    remove_PrintTaskRequested: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                         _type.HRESULT]


class IPrintManagerStatic(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IPrintManager]],  # printingManager
                                 _type.HRESULT]
    ShowPrintUIAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                _type.HRESULT]


class IPrintManagerStatic2(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IPrintPageInfo(_inspectable.IInspectable):
    put_MediaSize: _Callable[[_enum.Windows.Graphics.Printing.PrintMediaSize],  # value
                             _type.HRESULT]
    get_MediaSize: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintMediaSize]],  # value
                             _type.HRESULT]
    put_PageSize: _Callable[[_struct.Windows.Foundation.Size],  # value
                            _type.HRESULT]
    get_PageSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                            _type.HRESULT]
    put_DpiX: _Callable[[_type.UINT32],  # value
                        _type.HRESULT]
    get_DpiX: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    put_DpiY: _Callable[[_type.UINT32],  # value
                        _type.HRESULT]
    get_DpiY: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.Graphics.Printing.PrintOrientation],  # value
                               _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintOrientation]],  # value
                               _type.HRESULT]


class IPrintPageRange(_inspectable.IInspectable):
    get_FirstPageNumber: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_LastPageNumber: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]


class IPrintPageRangeFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.INT32,  # firstPage
                       _type.INT32,  # lastPage
                       _Pointer[IPrintPageRange]],  # result
                      _type.HRESULT]
    CreateWithSinglePage: _Callable[[_type.INT32,  # page
                                     _Pointer[IPrintPageRange]],  # result
                                    _type.HRESULT]


class IPrintPageRangeOptions(_inspectable.IInspectable):
    put_AllowAllPages: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_AllowAllPages: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AllowCurrentPage: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_AllowCurrentPage: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_AllowCustomSetOfPages: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_AllowCustomSetOfPages: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class IPrintTask(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackagePropertySet]],  # value
                              _type.HRESULT]
    get_Source: _Callable[[_Pointer[IPrintDocumentSource]],  # value
                          _type.HRESULT]
    get_Options: _Callable[[_Pointer[IPrintTaskOptionsCore]],  # value
                           _type.HRESULT]
    add_Previewing: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintTask, _inspectable.IInspectable],  # eventHandler
                               _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                              _type.HRESULT]
    remove_Previewing: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                 _type.HRESULT]
    add_Submitting: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintTask, _inspectable.IInspectable],  # eventHandler
                               _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                              _type.HRESULT]
    remove_Submitting: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                 _type.HRESULT]
    add_Progressing: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintTask, IPrintTaskProgressingEventArgs],  # eventHandler
                                _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                               _type.HRESULT]
    remove_Progressing: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                  _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintTask, IPrintTaskCompletedEventArgs],  # eventHandler
                              _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                _type.HRESULT]


class IPrintTask2(_inspectable.IInspectable):
    put_IsPreviewEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsPreviewEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]


class IPrintTaskCompletedEventArgs(_inspectable.IInspectable):
    get_Completion: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintTaskCompletion]],  # value
                              _type.HRESULT]


class IPrintTaskOptions(_inspectable.IInspectable):
    put_Bordering: _Callable[[_enum.Windows.Graphics.Printing.PrintBordering],  # value
                             _type.HRESULT]
    get_Bordering: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintBordering]],  # value
                             _type.HRESULT]
    GetPagePrintTicket: _Callable[[IPrintPageInfo,  # printPageInfo
                                   _Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # printTicket
                                  _type.HRESULT]


class IPrintTaskOptions2(_inspectable.IInspectable):
    get_PageRangeOptions: _Callable[[_Pointer[IPrintPageRangeOptions]],  # value
                                    _type.HRESULT]
    get_CustomPageRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IPrintPageRange]]],  # value
                                    _type.HRESULT]


class IPrintTaskOptionsCore(_inspectable.IInspectable):
    GetPageDescription: _Callable[[_type.UINT32,  # jobPageNumber
                                   _Pointer[_struct.Windows.Graphics.Printing.PrintPageDescription]],  # description
                                  _type.HRESULT]


class IPrintTaskOptionsCoreProperties(_inspectable.IInspectable):
    put_MediaSize: _Callable[[_enum.Windows.Graphics.Printing.PrintMediaSize],  # value
                             _type.HRESULT]
    get_MediaSize: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintMediaSize]],  # value
                             _type.HRESULT]
    put_MediaType: _Callable[[_enum.Windows.Graphics.Printing.PrintMediaType],  # value
                             _type.HRESULT]
    get_MediaType: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintMediaType]],  # value
                             _type.HRESULT]
    put_Orientation: _Callable[[_enum.Windows.Graphics.Printing.PrintOrientation],  # value
                               _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintOrientation]],  # value
                               _type.HRESULT]
    put_PrintQuality: _Callable[[_enum.Windows.Graphics.Printing.PrintQuality],  # value
                                _type.HRESULT]
    get_PrintQuality: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintQuality]],  # value
                                _type.HRESULT]
    put_ColorMode: _Callable[[_enum.Windows.Graphics.Printing.PrintColorMode],  # value
                             _type.HRESULT]
    get_ColorMode: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintColorMode]],  # value
                             _type.HRESULT]
    put_Duplex: _Callable[[_enum.Windows.Graphics.Printing.PrintDuplex],  # value
                          _type.HRESULT]
    get_Duplex: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintDuplex]],  # value
                          _type.HRESULT]
    put_Collation: _Callable[[_enum.Windows.Graphics.Printing.PrintCollation],  # value
                             _type.HRESULT]
    get_Collation: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintCollation]],  # value
                             _type.HRESULT]
    put_Staple: _Callable[[_enum.Windows.Graphics.Printing.PrintStaple],  # value
                          _type.HRESULT]
    get_Staple: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintStaple]],  # value
                          _type.HRESULT]
    put_HolePunch: _Callable[[_enum.Windows.Graphics.Printing.PrintHolePunch],  # value
                             _type.HRESULT]
    get_HolePunch: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintHolePunch]],  # value
                             _type.HRESULT]
    put_Binding: _Callable[[_enum.Windows.Graphics.Printing.PrintBinding],  # value
                           _type.HRESULT]
    get_Binding: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintBinding]],  # value
                           _type.HRESULT]
    get_MinCopies: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_MaxCopies: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_NumberOfCopies: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_NumberOfCopies: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class IPrintTaskOptionsCoreUIConfiguration(_inspectable.IInspectable):
    get_DisplayedOptions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                    _type.HRESULT]


class IPrintTaskProgressingEventArgs(_inspectable.IInspectable):
    get_DocumentPageCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]


class IPrintTaskRequest(_inspectable.IInspectable):
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    CreatePrintTask: _Callable[[_type.HSTRING,  # title
                                IPrintTaskSourceRequestedHandler,  # handler
                                _Pointer[IPrintTask]],  # task
                               _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IPrintTaskRequestedDeferral]],  # deferral
                           _type.HRESULT]


class IPrintTaskRequestedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IPrintTaskRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IPrintTaskRequest]],  # value
                           _type.HRESULT]


class IPrintTaskSourceRequestedArgs(_inspectable.IInspectable):
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    SetSource: _Callable[[IPrintDocumentSource],  # source
                         _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IPrintTaskSourceRequestedDeferral]],  # deferral
                           _type.HRESULT]


class IPrintTaskSourceRequestedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IPrintTaskTargetDeviceSupport(_inspectable.IInspectable):
    put_IsPrinterTargetEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_IsPrinterTargetEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_Is3DManufacturingTargetEnabled: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    get_Is3DManufacturingTargetEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]


class IStandardPrintTaskOptionsStatic(_inspectable.IInspectable, factory=True):
    get_MediaSize: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_MediaType: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PrintQuality: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_ColorMode: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Duplex: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Collation: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Staple: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_HolePunch: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Binding: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Copies: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_NUp: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_InputBin: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IStandardPrintTaskOptionsStatic2(_inspectable.IInspectable, factory=True):
    get_Bordering: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IStandardPrintTaskOptionsStatic3(_inspectable.IInspectable, factory=True):
    get_CustomPageRanges: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
