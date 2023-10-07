from __future__ import annotations as _

from typing import Callable as _Callable

from .. import PrintTicket as _Windows_Graphics_Printing_PrintTicket
from .... import ApplicationModel as _Windows_ApplicationModel
from .... import Foundation as _Windows_Foundation
from ....Data.Xml import Dom as _Windows_Data_Xml_Dom
from ....Devices import Printers as _Windows_Devices_Printers
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....UI import Shell as _Windows_UI_Shell
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPrintSupportExtensionSession(_inspectable.IInspectable):
    get_Printer: _Callable[[_Pointer[_Windows_Devices_Printers.IIppPrintDevice]],  # value
                           _type.HRESULT]
    add_PrintTicketValidationRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintSupportExtensionSession, IPrintSupportPrintTicketValidationRequestedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_PrintTicketValidationRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_PrintDeviceCapabilitiesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintSupportExtensionSession, IPrintSupportPrintDeviceCapabilitiesChangedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_PrintDeviceCapabilitiesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IPrintSupportExtensionSession2(_inspectable.IInspectable):
    add_PrinterSelected: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintSupportExtensionSession, IPrintSupportPrinterSelectedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PrinterSelected: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IPrintSupportExtensionTriggerDetails(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IPrintSupportExtensionSession]],  # value
                           _type.HRESULT]


class IPrintSupportPrintDeviceCapabilitiesChangedEventArgs(_inspectable.IInspectable):
    GetCurrentPrintDeviceCapabilities: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # result
                                                 _type.HRESULT]
    UpdatePrintDeviceCapabilities: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument],  # updatedPdc
                                             _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintSupportPrintDeviceCapabilitiesChangedEventArgs2(_inspectable.IInspectable):
    SetSupportedPdlPassthroughContentTypes: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING]],  # supportedPdlContentTypes
                                                      _type.HRESULT]
    get_ResourceLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    GetCurrentPrintDeviceResources: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # result
                                              _type.HRESULT]
    UpdatePrintDeviceResources: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument],  # updatedPdr
                                          _type.HRESULT]
    SetPrintDeviceCapabilitiesUpdatePolicy: _Callable[[IPrintSupportPrintDeviceCapabilitiesUpdatePolicy],  # updatePolicy
                                                      _type.HRESULT]


class IPrintSupportPrintDeviceCapabilitiesUpdatePolicy(_inspectable.IInspectable):
    pass


class IPrintSupportPrintDeviceCapabilitiesUpdatePolicyStatics(_inspectable.IInspectable, factory=True):
    CreatePeriodicRefresh: _Callable[[_struct.Windows.Foundation.TimeSpan,  # updatePeriod
                                      _Pointer[IPrintSupportPrintDeviceCapabilitiesUpdatePolicy]],  # result
                                     _type.HRESULT]
    CreatePrintJobRefresh: _Callable[[_type.UINT32,  # numberOfJobs
                                      _Pointer[IPrintSupportPrintDeviceCapabilitiesUpdatePolicy]],  # result
                                     _type.HRESULT]


class IPrintSupportPrintTicketElement(_inspectable.IInspectable):
    get_LocalName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_LocalName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_NamespaceUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_NamespaceUri: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]


class IPrintSupportPrintTicketValidationRequestedEventArgs(_inspectable.IInspectable):
    get_PrintTicket: _Callable[[_Pointer[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket]],  # value
                               _type.HRESULT]
    SetPrintTicketValidationStatus: _Callable[[_enum.Windows.Graphics.Printing.PrintSupport.WorkflowPrintTicketValidationStatus],  # status
                                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintSupportPrinterSelectedEventArgs(_inspectable.IInspectable):
    get_SourceAppInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppInfo]],  # value
                                 _type.HRESULT]
    get_PrintTicket: _Callable[[_Pointer[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket]],  # value
                               _type.HRESULT]
    put_PrintTicket: _Callable[[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket],  # value
                               _type.HRESULT]
    SetAdditionalFeatures: _Callable[[_Windows_Foundation_Collections.IIterable[IPrintSupportPrintTicketElement]],  # features
                                     _type.HRESULT]
    SetAdditionalParameters: _Callable[[_Windows_Foundation_Collections.IIterable[IPrintSupportPrintTicketElement]],  # parameters
                                       _type.HRESULT]
    get_AllowedAdditionalFeaturesAndParametersCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                                               _type.HRESULT]
    SetAdaptiveCard: _Callable[[_Windows_UI_Shell.IAdaptiveCard],  # adaptiveCard
                               _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintSupportSessionInfo(_inspectable.IInspectable):
    get_SourceAppInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppInfo]],  # value
                                 _type.HRESULT]
    get_Printer: _Callable[[_Pointer[_Windows_Devices_Printers.IIppPrintDevice]],  # value
                           _type.HRESULT]


class IPrintSupportSettingsActivatedEventArgs(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IPrintSupportSettingsUISession]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintSupportSettingsUISession(_inspectable.IInspectable):
    get_SessionPrintTicket: _Callable[[_Pointer[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket]],  # value
                                      _type.HRESULT]
    get_DocumentTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_LaunchKind: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.PrintSupport.SettingsLaunchKind]],  # value
                              _type.HRESULT]
    UpdatePrintTicket: _Callable[[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket],  # printTicket
                                 _type.HRESULT]
    get_SessionInfo: _Callable[[_Pointer[IPrintSupportSessionInfo]],  # value
                               _type.HRESULT]
