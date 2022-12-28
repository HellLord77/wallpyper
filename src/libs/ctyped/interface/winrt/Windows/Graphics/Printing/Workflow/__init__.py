from __future__ import annotations as _

from typing import Callable as _Callable

from .. import PrintTicket as _Windows_Graphics_Printing_PrintTicket
from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from ....Devices import Printers as _Windows_Devices_Printers
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPrintWorkflowBackgroundSession(_inspectable.IInspectable):
    add_SetupRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowBackgroundSession, IPrintWorkflowBackgroundSetupRequestedEventArgs],  # setupEventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_SetupRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_Submitted: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowBackgroundSession, IPrintWorkflowSubmittedEventArgs],  # submittedEventHandler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Submitted: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus]],  # value
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IPrintWorkflowBackgroundSetupRequestedEventArgs(_inspectable.IInspectable):
    GetUserPrintTicketAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket]]],  # operation
                                       _type.HRESULT]
    get_Configuration: _Callable[[_Pointer[IPrintWorkflowConfiguration]],  # configuration
                                 _type.HRESULT]
    SetRequiresUI: _Callable[[],
                             _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintWorkflowConfiguration(_inspectable.IInspectable):
    get_SourceAppDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_JobTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_SessionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IPrintWorkflowConfiguration2(_inspectable.IInspectable):
    AbortPrintFlow: _Callable[[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowJobAbortReason],  # reason
                              _type.HRESULT]


class IPrintWorkflowForegroundSession(_inspectable.IInspectable):
    add_SetupRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowForegroundSession, IPrintWorkflowForegroundSetupRequestedEventArgs],  # setupEventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_SetupRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_XpsDataAvailable: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowForegroundSession, IPrintWorkflowXpsDataAvailableEventArgs],  # xpsDataAvailableEventHandler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_XpsDataAvailable: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus]],  # value
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IPrintWorkflowForegroundSetupRequestedEventArgs(_inspectable.IInspectable):
    GetUserPrintTicketAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket]]],  # operation
                                       _type.HRESULT]
    get_Configuration: _Callable[[_Pointer[IPrintWorkflowConfiguration]],  # value
                                 _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintWorkflowJobActivatedEventArgs(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IPrintWorkflowJobUISession]],  # value
                           _type.HRESULT]


class IPrintWorkflowJobBackgroundSession(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus]],  # value
                          _type.HRESULT]
    add_JobStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowJobBackgroundSession, IPrintWorkflowJobStartingEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_JobStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_PdlModificationRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowJobBackgroundSession, IPrintWorkflowPdlModificationRequestedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_PdlModificationRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IPrintWorkflowJobNotificationEventArgs(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[IPrintWorkflowConfiguration]],  # value
                                 _type.HRESULT]
    get_PrinterJob: _Callable[[_Pointer[IPrintWorkflowPrinterJob]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintWorkflowJobStartingEventArgs(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[IPrintWorkflowConfiguration]],  # value
                                 _type.HRESULT]
    get_Printer: _Callable[[_Pointer[_Windows_Devices_Printers.IIppPrintDevice]],  # value
                           _type.HRESULT]
    SetSkipSystemRendering: _Callable[[],
                                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintWorkflowJobTriggerDetails(_inspectable.IInspectable):
    get_PrintWorkflowJobSession: _Callable[[_Pointer[IPrintWorkflowJobBackgroundSession]],  # value
                                           _type.HRESULT]


class IPrintWorkflowJobUISession(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowSessionStatus]],  # value
                          _type.HRESULT]
    add_PdlDataAvailable: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowJobUISession, IPrintWorkflowPdlDataAvailableEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_PdlDataAvailable: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_JobNotification: _Callable[[_Windows_Foundation.ITypedEventHandler[IPrintWorkflowJobUISession, IPrintWorkflowJobNotificationEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_JobNotification: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IPrintWorkflowObjectModelSourceFileContent(_inspectable.IInspectable):
    pass


class IPrintWorkflowObjectModelSourceFileContentFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_Windows_Storage_Streams.IInputStream,  # xpsStream
                               _Pointer[IPrintWorkflowObjectModelSourceFileContent]],  # value
                              _type.HRESULT]

    _factory = True


class IPrintWorkflowObjectModelTargetPackage(_inspectable.IInspectable):
    pass


class IPrintWorkflowPdlConverter(_inspectable.IInspectable):
    ConvertPdlAsync: _Callable[[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket,  # printTicket
                                _Windows_Storage_Streams.IInputStream,  # inputStream
                                _Windows_Storage_Streams.IOutputStream,  # outputStream
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]


class IPrintWorkflowPdlConverter2(_inspectable.IInspectable):
    ConvertPdlAsync: _Callable[[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket,  # printTicket
                                _Windows_Storage_Streams.IInputStream,  # inputStream
                                _Windows_Storage_Streams.IOutputStream,  # outputStream
                                _enum.Windows.Graphics.Printing.Workflow.PdlConversionHostBasedProcessingOperations,  # hostBasedProcessingOperations
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]


class IPrintWorkflowPdlDataAvailableEventArgs(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[IPrintWorkflowConfiguration]],  # value
                                 _type.HRESULT]
    get_PrinterJob: _Callable[[_Pointer[IPrintWorkflowPrinterJob]],  # value
                              _type.HRESULT]
    get_SourceContent: _Callable[[_Pointer[IPrintWorkflowPdlSourceContent]],  # value
                                 _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintWorkflowPdlModificationRequestedEventArgs(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[IPrintWorkflowConfiguration]],  # value
                                 _type.HRESULT]
    get_PrinterJob: _Callable[[_Pointer[IPrintWorkflowPrinterJob]],  # value
                              _type.HRESULT]
    get_SourceContent: _Callable[[_Pointer[IPrintWorkflowPdlSourceContent]],  # value
                                 _type.HRESULT]
    get_UILauncher: _Callable[[_Pointer[IPrintWorkflowUILauncher]],  # value
                              _type.HRESULT]
    CreateJobOnPrinter: _Callable[[_type.HSTRING,  # targetContentType
                                   _Pointer[IPrintWorkflowPdlTargetStream]],  # result
                                  _type.HRESULT]
    CreateJobOnPrinterWithAttributes: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _Windows_Devices_Printers.IIppAttributeValue]],  # jobAttributes
                                                 _type.HSTRING,  # targetContentType
                                                 _Pointer[IPrintWorkflowPdlTargetStream]],  # result
                                                _type.HRESULT]
    CreateJobOnPrinterWithAttributesBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # jobAttributesBuffer
                                                       _type.HSTRING,  # targetContentType
                                                       _Pointer[IPrintWorkflowPdlTargetStream]],  # result
                                                      _type.HRESULT]
    GetPdlConverter: _Callable[[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowPdlConversionType,  # conversionType
                                _Pointer[IPrintWorkflowPdlConverter]],  # result
                               _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintWorkflowPdlModificationRequestedEventArgs2(_inspectable.IInspectable):
    CreateJobOnPrinterWithAttributes: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _Windows_Devices_Printers.IIppAttributeValue]],  # jobAttributes
                                                 _type.HSTRING,  # targetContentType
                                                 _Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _Windows_Devices_Printers.IIppAttributeValue]],  # operationAttributes
                                                 _enum.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy,  # jobAttributesMergePolicy
                                                 _enum.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy,  # operationAttributesMergePolicy
                                                 _Pointer[IPrintWorkflowPdlTargetStream]],  # result
                                                _type.HRESULT]
    CreateJobOnPrinterWithAttributesBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # jobAttributesBuffer
                                                       _type.HSTRING,  # targetContentType
                                                       _Windows_Storage_Streams.IBuffer,  # operationAttributesBuffer
                                                       _enum.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy,  # jobAttributesMergePolicy
                                                       _enum.Windows.Graphics.Printing.Workflow.PrintWorkflowAttributesMergePolicy,  # operationAttributesMergePolicy
                                                       _Pointer[IPrintWorkflowPdlTargetStream]],  # result
                                                      _type.HRESULT]


class IPrintWorkflowPdlSourceContent(_inspectable.IInspectable):
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    GetInputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # result
                              _type.HRESULT]
    GetContentFileAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                   _type.HRESULT]


class IPrintWorkflowPdlTargetStream(_inspectable.IInspectable):
    GetOutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # result
                               _type.HRESULT]
    CompleteStreamSubmission: _Callable[[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedStatus],  # status
                                        _type.HRESULT]


class IPrintWorkflowPrinterJob(_inspectable.IInspectable):
    get_JobId: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    get_Printer: _Callable[[_Pointer[_Windows_Devices_Printers.IIppPrintDevice]],  # value
                           _type.HRESULT]
    GetJobStatus: _Callable[[_Pointer[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowPrinterJobStatus]],  # result
                            _type.HRESULT]
    GetJobPrintTicket: _Callable[[_Pointer[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket]],  # result
                                 _type.HRESULT]
    GetJobAttributesAsBuffer: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # attributeNames
                                         _Pointer[_Windows_Storage_Streams.IBuffer]],  # result
                                        _type.HRESULT]
    GetJobAttributes: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # attributeNames
                                 _Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _Windows_Devices_Printers.IIppAttributeValue]]],  # result
                                _type.HRESULT]
    SetJobAttributesFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # jobAttributesBuffer
                                           _Pointer[_Windows_Devices_Printers.IIppSetAttributesResult]],  # result
                                          _type.HRESULT]
    SetJobAttributes: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _Windows_Devices_Printers.IIppAttributeValue]],  # jobAttributes
                                 _Pointer[_Windows_Devices_Printers.IIppSetAttributesResult]],  # result
                                _type.HRESULT]


class IPrintWorkflowSourceContent(_inspectable.IInspectable):
    GetJobPrintTicketAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket]]],  # operation
                                      _type.HRESULT]
    GetSourceSpoolDataAsStreamContent: _Callable[[_Pointer[IPrintWorkflowSpoolStreamContent]],  # result
                                                 _type.HRESULT]
    GetSourceSpoolDataAsXpsObjectModel: _Callable[[_Pointer[IPrintWorkflowObjectModelSourceFileContent]],  # result
                                                  _type.HRESULT]


class IPrintWorkflowSpoolStreamContent(_inspectable.IInspectable):
    GetInputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # result
                              _type.HRESULT]


class IPrintWorkflowStreamTarget(_inspectable.IInspectable):
    GetOutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # result
                               _type.HRESULT]


class IPrintWorkflowSubmittedEventArgs(_inspectable.IInspectable):
    get_Operation: _Callable[[_Pointer[IPrintWorkflowSubmittedOperation]],  # value
                             _type.HRESULT]
    GetTarget: _Callable[[_Windows_Graphics_Printing_PrintTicket.IWorkflowPrintTicket,  # jobPrintTicket
                          _Pointer[IPrintWorkflowTarget]],  # result
                         _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IPrintWorkflowSubmittedOperation(_inspectable.IInspectable):
    Complete: _Callable[[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowSubmittedStatus],  # status
                        _type.HRESULT]
    get_Configuration: _Callable[[_Pointer[IPrintWorkflowConfiguration]],  # value
                                 _type.HRESULT]
    get_XpsContent: _Callable[[_Pointer[IPrintWorkflowSourceContent]],  # value
                              _type.HRESULT]


class IPrintWorkflowTarget(_inspectable.IInspectable):
    get_TargetAsStream: _Callable[[_Pointer[IPrintWorkflowStreamTarget]],  # value
                                  _type.HRESULT]
    get_TargetAsXpsObjectModelPackage: _Callable[[_Pointer[IPrintWorkflowObjectModelTargetPackage]],  # value
                                                 _type.HRESULT]


class IPrintWorkflowTriggerDetails(_inspectable.IInspectable):
    get_PrintWorkflowSession: _Callable[[_Pointer[IPrintWorkflowBackgroundSession]],  # value
                                        _type.HRESULT]


class IPrintWorkflowUIActivatedEventArgs(_inspectable.IInspectable):
    get_PrintWorkflowSession: _Callable[[_Pointer[IPrintWorkflowForegroundSession]],  # value
                                        _type.HRESULT]


class IPrintWorkflowUILauncher(_inspectable.IInspectable):
    IsUILaunchEnabled: _Callable[[_Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    LaunchAndCompleteUIAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Graphics.Printing.Workflow.PrintWorkflowUICompletionStatus]]],  # operation
                                        _type.HRESULT]


class IPrintWorkflowXpsDataAvailableEventArgs(_inspectable.IInspectable):
    get_Operation: _Callable[[_Pointer[IPrintWorkflowSubmittedOperation]],  # value
                             _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]
