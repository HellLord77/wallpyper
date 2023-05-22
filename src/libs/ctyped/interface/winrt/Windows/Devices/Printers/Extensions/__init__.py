from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPrint3DWorkflow(_inspectable.IInspectable):
    get_DeviceID: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    GetPrintModelPackage: _Callable[[_Pointer[_inspectable.IInspectable]],  # printModelPackage
                                    _type.HRESULT]
    get_IsPrintReady: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsPrintReady: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    add_PrintRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrint3DWorkflow, IPrint3DWorkflowPrintRequestedEventArgs],  # eventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                  _type.HRESULT]
    remove_PrintRequested: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                     _type.HRESULT]


class IPrint3DWorkflow2(_inspectable.IInspectable):
    add_PrinterChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrint3DWorkflow, IPrint3DWorkflowPrinterChangedEventArgs],  # eventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                  _type.HRESULT]
    remove_PrinterChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                     _type.HRESULT]


class IPrint3DWorkflowPrintRequestedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Devices.Printers.Extensions.Print3DWorkflowStatus]],  # value
                          _type.HRESULT]
    SetExtendedStatus: _Callable[[_enum.Windows.Devices.Printers.Extensions.Print3DWorkflowDetail],  # value
                                 _type.HRESULT]
    SetSource: _Callable[[_inspectable.IInspectable],  # source
                         _type.HRESULT]
    SetSourceChanged: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IPrint3DWorkflowPrinterChangedEventArgs(_inspectable.IInspectable):
    get_NewDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IPrintExtensionContextStatic(_inspectable.IInspectable, factory=True):
    FromDeviceId: _Callable[[_type.HSTRING,  # deviceId
                             _Pointer[_inspectable.IInspectable]],  # context
                            _type.HRESULT]


class IPrintNotificationEventDetails(_inspectable.IInspectable):
    get_PrinterName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_EventData: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_EventData: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class IPrintTaskConfiguration(_inspectable.IInspectable):
    get_PrinterExtensionContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # context
                                           _type.HRESULT]
    add_SaveRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintTaskConfiguration, IPrintTaskConfigurationSaveRequestedEventArgs],  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                 _type.HRESULT]
    remove_SaveRequested: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                    _type.HRESULT]


class IPrintTaskConfigurationSaveRequest(_inspectable.IInspectable):
    Cancel: _Callable[[],
                      _type.HRESULT]
    Save: _Callable[[_inspectable.IInspectable],  # printerExtensionContext
                    _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IPrintTaskConfigurationSaveRequestedDeferral]],  # deferral
                           _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]


class IPrintTaskConfigurationSaveRequestedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IPrintTaskConfigurationSaveRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IPrintTaskConfigurationSaveRequest]],  # context
                           _type.HRESULT]
