from __future__ import annotations

from typing import Callable as _Callable

from ... import Email as _Windows_ApplicationModel_Email
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IEmailDataProviderConnection(_inspectable.IInspectable):
    add_MailboxSyncRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxSyncManagerSyncRequestEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_MailboxSyncRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_DownloadMessageRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxDownloadMessageRequestEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_DownloadMessageRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_DownloadAttachmentRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxDownloadAttachmentRequestEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_DownloadAttachmentRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_CreateFolderRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxCreateFolderRequestEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_CreateFolderRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_DeleteFolderRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxDeleteFolderRequestEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_DeleteFolderRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_EmptyFolderRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxEmptyFolderRequestEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EmptyFolderRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_MoveFolderRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxMoveFolderRequestEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_MoveFolderRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_UpdateMeetingResponseRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxUpdateMeetingResponseRequestEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_UpdateMeetingResponseRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_ForwardMeetingRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxForwardMeetingRequestEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ForwardMeetingRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_ProposeNewTimeForMeetingRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxProposeNewTimeForMeetingRequestEventArgs],  # handler
                                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                                     _type.HRESULT]
    remove_ProposeNewTimeForMeetingRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                        _type.HRESULT]
    add_SetAutoReplySettingsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxSetAutoReplySettingsRequestEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_SetAutoReplySettingsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_GetAutoReplySettingsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxGetAutoReplySettingsRequestEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_GetAutoReplySettingsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_ResolveRecipientsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxResolveRecipientsRequestEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_ResolveRecipientsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    add_ValidateCertificatesRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxValidateCertificatesRequestEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_ValidateCertificatesRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_ServerSearchReadBatchRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailDataProviderConnection, IEmailMailboxServerSearchReadBatchRequestEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_ServerSearchReadBatchRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IEmailDataProviderTriggerDetails(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IEmailDataProviderConnection]],  # value
                              _type.HRESULT]


class IEmailMailboxCreateFolderRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_ParentFolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_ApplicationModel_Email.IEmailFolder,  # folder
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus,  # status
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxCreateFolderRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxCreateFolderRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxDeleteFolderRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailFolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus,  # status
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxDeleteFolderRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxDeleteFolderRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxDownloadAttachmentRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailMessageId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailAttachmentId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxDownloadAttachmentRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxDownloadAttachmentRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxDownloadMessageRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailMessageId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxDownloadMessageRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxDownloadMessageRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxEmptyFolderRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailFolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus,  # status
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxEmptyFolderRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxEmptyFolderRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxForwardMeetingRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailMessageId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Recipients: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Email.IEmailRecipient]]],  # value
                              _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_ForwardHeaderType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMessageBodyKind]],  # value
                                     _type.HRESULT]
    get_ForwardHeader: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxForwardMeetingRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxForwardMeetingRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxGetAutoReplySettingsRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_RequestedFormat: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind]],  # value
                                   _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_ApplicationModel_Email.IEmailMailboxAutoReplySettings,  # autoReplySettings
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxGetAutoReplySettingsRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxGetAutoReplySettingsRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxMoveFolderRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailFolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_NewParentFolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_NewFolderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxMoveFolderRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxMoveFolderRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxProposeNewTimeForMeetingRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailMessageId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_NewStartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    get_NewDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxProposeNewTimeForMeetingRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxProposeNewTimeForMeetingRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxResolveRecipientsRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Recipients: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel_Email.IEmailRecipientResolutionResult],  # resolutionResults
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxResolveRecipientsRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxResolveRecipientsRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxServerSearchReadBatchRequest(_inspectable.IInspectable):
    get_SessionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailFolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Options: _Callable[[_Pointer[_Windows_ApplicationModel_Email.IEmailQueryOptions]],  # value
                           _type.HRESULT]
    get_SuggestedBatchSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    SaveMessageAsync: _Callable[[_Windows_ApplicationModel_Email.IEmailMessage,  # message
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailBatchStatus,  # batchStatus
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxServerSearchReadBatchRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxServerSearchReadBatchRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxSetAutoReplySettingsRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AutoReplySettings: _Callable[[_Pointer[_Windows_ApplicationModel_Email.IEmailMailboxAutoReplySettings]],  # value
                                     _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxSetAutoReplySettingsRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxSetAutoReplySettingsRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxSyncManagerSyncRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxSyncManagerSyncRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxSyncManagerSyncRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxUpdateMeetingResponseRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_EmailMessageId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Response: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMeetingResponseType]],  # response
                            _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_SendUpdate: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxUpdateMeetingResponseRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxUpdateMeetingResponseRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IEmailMailboxValidateCertificatesRequest(_inspectable.IInspectable):
    get_EmailMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Certificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                                _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_enum.Windows.ApplicationModel.Email.EmailCertificateValidationStatus],  # validationStatuses
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IEmailMailboxValidateCertificatesRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IEmailMailboxValidateCertificatesRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
