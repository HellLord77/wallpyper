from __future__ import annotations

from typing import Callable as _Callable

from .. import Appointments as _Windows_ApplicationModel_Appointments
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IEmailAttachment(_inspectable.IInspectable):
    get_FileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_FileName: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                        _type.HRESULT]


class IEmailAttachment2(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_ContentId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_ContentId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_ContentLocation: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_ContentLocation: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_DownloadState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailAttachmentDownloadState]],  # value
                                 _type.HRESULT]
    put_DownloadState: _Callable[[_enum.Windows.ApplicationModel.Email.EmailAttachmentDownloadState],  # value
                                 _type.HRESULT]
    get_EstimatedDownloadSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                                _type.HRESULT]
    put_EstimatedDownloadSizeInBytes: _Callable[[_type.UINT64],  # value
                                                _type.HRESULT]
    get_IsFromBaseMessage: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsInline: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsInline: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_MimeType: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_MimeType: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IEmailAttachmentFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # fileName
                       _Windows_Storage_Streams.IRandomAccessStreamReference,  # data
                       _Pointer[IEmailAttachment]],  # result
                      _type.HRESULT]


class IEmailAttachmentFactory2(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # fileName
                       _Windows_Storage_Streams.IRandomAccessStreamReference,  # data
                       _type.HSTRING,  # mimeType
                       _Pointer[IEmailAttachment]],  # result
                      _type.HRESULT]

    _factory = True


class IEmailConversation(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_MailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_FlagState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailFlagState]],  # value
                             _type.HRESULT]
    get_HasAttachment: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_Importance: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailImportance]],  # value
                              _type.HRESULT]
    get_LastEmailResponseKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMessageResponseKind]],  # value
                                         _type.HRESULT]
    get_MessageCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_MostRecentMessageId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_MostRecentMessageTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                         _type.HRESULT]
    get_Preview: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_LatestSender: _Callable[[_Pointer[IEmailRecipient]],  # value
                                _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_UnreadMessageCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    FindMessagesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IEmailMessage]]]],  # result
                                 _type.HRESULT]
    FindMessagesWithCountAsync: _Callable[[_type.UINT32,  # count
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IEmailMessage]]]],  # result
                                          _type.HRESULT]


class IEmailConversationBatch(_inspectable.IInspectable):
    get_Conversations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IEmailConversation]]],  # value
                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailBatchStatus]],  # value
                          _type.HRESULT]


class IEmailConversationReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IEmailConversationBatch]]],  # result
                              _type.HRESULT]


class IEmailFolder(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_MailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ParentFolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_IsSyncEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsSyncEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_LastSuccessfulSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                          _type.HRESULT]
    put_LastSuccessfulSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                          _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailSpecialFolderKind]],  # value
                        _type.HRESULT]
    CreateFolderAsync: _Callable[[_type.HSTRING,  # name
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IEmailFolder]]],  # result
                                 _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                           _type.HRESULT]
    FindChildFoldersAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IEmailFolder]]]],  # result
                                     _type.HRESULT]
    GetConversationReader: _Callable[[_Pointer[IEmailConversationReader]],  # result
                                     _type.HRESULT]
    GetConversationReaderWithOptions: _Callable[[IEmailQueryOptions,  # options
                                                 _Pointer[IEmailConversationReader]],  # result
                                                _type.HRESULT]
    GetMessageAsync: _Callable[[_type.HSTRING,  # id
                                _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMessage]]],  # result
                               _type.HRESULT]
    GetMessageReader: _Callable[[_Pointer[IEmailMessageReader]],  # result
                                _type.HRESULT]
    GetMessageReaderWithOptions: _Callable[[IEmailQueryOptions,  # options
                                            _Pointer[IEmailMessageReader]],  # result
                                           _type.HRESULT]
    GetMessageCountsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IEmailItemCounts]]],  # result
                                     _type.HRESULT]
    TryMoveAsync: _Callable[[IEmailFolder,  # newParentFolder
                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                            _type.HRESULT]
    TryMoveWithNewNameAsync: _Callable[[IEmailFolder,  # newParentFolder
                                        _type.HSTRING,  # newFolderName
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                       _type.HRESULT]
    TrySaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                            _type.HRESULT]
    SaveMessageAsync: _Callable[[IEmailMessage,  # message
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                _type.HRESULT]


class IEmailIrmInfo(_inspectable.IInspectable):
    get_CanEdit: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_CanEdit: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_CanExtractData: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_CanExtractData: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_CanForward: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_CanForward: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_CanModifyRecipientsOnResponse: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_CanModifyRecipientsOnResponse: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_CanPrintData: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_CanPrintData: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_CanRemoveIrmOnResponse: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_CanRemoveIrmOnResponse: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_CanReply: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_CanReply: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_CanReplyAll: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_CanReplyAll: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    put_ExpirationDate: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                  _type.HRESULT]
    get_IsIrmOriginator: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsIrmOriginator: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsProgramaticAccessAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsProgramaticAccessAllowed: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_Template: _Callable[[_Pointer[IEmailIrmTemplate]],  # value
                            _type.HRESULT]
    put_Template: _Callable[[IEmailIrmTemplate],  # value
                            _type.HRESULT]


class IEmailIrmInfoFactory(_inspectable.IInspectable):
    Create: _Callable[[_struct.Windows.Foundation.DateTime,  # expiration
                       IEmailIrmTemplate,  # irmTemplate
                       _Pointer[IEmailIrmInfo]],  # result
                      _type.HRESULT]

    _factory = True


class IEmailIrmTemplate(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IEmailIrmTemplateFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # id
                       _type.HSTRING,  # name
                       _type.HSTRING,  # description
                       _Pointer[IEmailIrmTemplate]],  # result
                      _type.HRESULT]

    _factory = True


class IEmailItemCounts(_inspectable.IInspectable):
    get_Flagged: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    get_Important: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Total: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Unread: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]


class IEmailMailbox(_inspectable.IInspectable):
    get_Capabilities: _Callable[[_Pointer[IEmailMailboxCapabilities]],  # value
                                _type.HRESULT]
    get_ChangeTracker: _Callable[[_Pointer[IEmailMailboxChangeTracker]],  # value
                                 _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_IsOwnedByCurrentApp: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsDataEncryptedUnderLock: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_MailAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_MailAddress: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_MailAddressAliases: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                      _type.HRESULT]
    get_OtherAppReadAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxOtherAppReadAccess]],  # value
                                      _type.HRESULT]
    put_OtherAppReadAccess: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxOtherAppReadAccess],  # value
                                      _type.HRESULT]
    get_OtherAppWriteAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxOtherAppWriteAccess]],  # value
                                       _type.HRESULT]
    put_OtherAppWriteAccess: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxOtherAppWriteAccess],  # value
                                       _type.HRESULT]
    get_Policies: _Callable[[_Pointer[IEmailMailboxPolicies]],  # value
                            _type.HRESULT]
    get_SourceDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_SyncManager: _Callable[[_Pointer[IEmailMailboxSyncManager]],  # value
                               _type.HRESULT]
    get_UserDataAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    GetConversationReader: _Callable[[_Pointer[IEmailConversationReader]],  # result
                                     _type.HRESULT]
    GetConversationReaderWithOptions: _Callable[[IEmailQueryOptions,  # options
                                                 _Pointer[IEmailConversationReader]],  # result
                                                _type.HRESULT]
    GetMessageReader: _Callable[[_Pointer[IEmailMessageReader]],  # result
                                _type.HRESULT]
    GetMessageReaderWithOptions: _Callable[[IEmailQueryOptions,  # options
                                            _Pointer[IEmailMessageReader]],  # result
                                           _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                           _type.HRESULT]
    GetConversationAsync: _Callable[[_type.HSTRING,  # id
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IEmailConversation]]],  # result
                                    _type.HRESULT]
    GetFolderAsync: _Callable[[_type.HSTRING,  # id
                               _Pointer[_Windows_Foundation.IAsyncOperation[IEmailFolder]]],  # result
                              _type.HRESULT]
    GetMessageAsync: _Callable[[_type.HSTRING,  # id
                                _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMessage]]],  # result
                               _type.HRESULT]
    GetSpecialFolderAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailSpecialFolderKind,  # folderType
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IEmailFolder]]],  # result
                                     _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                         _type.HRESULT]
    MarkMessageAsSeenAsync: _Callable[[_type.HSTRING,  # messageId
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                      _type.HRESULT]
    MarkFolderAsSeenAsync: _Callable[[_type.HSTRING,  # folderId
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]
    MarkMessageReadAsync: _Callable[[_type.HSTRING,  # messageId
                                     _type.boolean,  # isRead
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ChangeMessageFlagStateAsync: _Callable[[_type.HSTRING,  # messageId
                                            _enum.Windows.ApplicationModel.Email.EmailFlagState,  # flagState
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                           _type.HRESULT]
    TryMoveMessageAsync: _Callable[[_type.HSTRING,  # messageId
                                    _type.HSTRING,  # newParentFolderId
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                   _type.HRESULT]
    TryMoveFolderAsync: _Callable[[_type.HSTRING,  # folderId
                                   _type.HSTRING,  # newParentFolderId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                  _type.HRESULT]
    TryMoveFolderWithNewNameAsync: _Callable[[_type.HSTRING,  # folderId
                                              _type.HSTRING,  # newParentFolderId
                                              _type.HSTRING,  # newFolderName
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                             _type.HRESULT]
    DeleteMessageAsync: _Callable[[_type.HSTRING,  # messageId
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                  _type.HRESULT]
    MarkFolderSyncEnabledAsync: _Callable[[_type.HSTRING,  # folderId
                                           _type.boolean,  # isSyncEnabled
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                          _type.HRESULT]
    SendMessageAsync: _Callable[[IEmailMessage,  # message
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                _type.HRESULT]
    SaveDraftAsync: _Callable[[IEmailMessage,  # message
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                              _type.HRESULT]
    DownloadMessageAsync: _Callable[[_type.HSTRING,  # messageId
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    DownloadAttachmentAsync: _Callable[[_type.HSTRING,  # attachmentId
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                       _type.HRESULT]
    CreateResponseMessageAsync: _Callable[[_type.HSTRING,  # messageId
                                           _enum.Windows.ApplicationModel.Email.EmailMessageResponseKind,  # responseType
                                           _type.HSTRING,  # subject
                                           _enum.Windows.ApplicationModel.Email.EmailMessageBodyKind,  # responseHeaderType
                                           _type.HSTRING,  # responseHeader
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMessage]]],  # result
                                          _type.HRESULT]
    TryUpdateMeetingResponseAsync: _Callable[[IEmailMessage,  # meeting
                                              _enum.Windows.ApplicationModel.Email.EmailMeetingResponseType,  # response
                                              _type.HSTRING,  # subject
                                              _type.HSTRING,  # comment
                                              _type.boolean,  # sendUpdate
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                             _type.HRESULT]
    TryForwardMeetingAsync: _Callable[[IEmailMessage,  # meeting
                                       _Windows_Foundation_Collections.IIterable[IEmailRecipient],  # recipients
                                       _type.HSTRING,  # subject
                                       _enum.Windows.ApplicationModel.Email.EmailMessageBodyKind,  # forwardHeaderType
                                       _type.HSTRING,  # forwardHeader
                                       _type.HSTRING,  # comment
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                      _type.HRESULT]
    TryProposeNewTimeForMeetingAsync: _Callable[[IEmailMessage,  # meeting
                                                 _struct.Windows.Foundation.DateTime,  # newStartTime
                                                 _struct.Windows.Foundation.TimeSpan,  # newDuration
                                                 _type.HSTRING,  # subject
                                                 _type.HSTRING,  # comment
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                _type.HRESULT]
    add_MailboxChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailMailbox, IEmailMailboxChangedEventArgs],  # pHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # pToken
                                  _type.HRESULT]
    remove_MailboxChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    SmartSendMessageAsync: _Callable[[IEmailMessage,  # message
                                      _type.boolean,  # smartSend
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]
    TrySetAutoReplySettingsAsync: _Callable[[IEmailMailboxAutoReplySettings,  # autoReplySettings
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                            _type.HRESULT]
    TryGetAutoReplySettingsAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind,  # requestedFormat
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMailboxAutoReplySettings]]],  # autoReplySettings
                                            _type.HRESULT]


class IEmailMailbox2(_inspectable.IInspectable):
    get_LinkedMailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_NetworkAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_NetworkId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IEmailMailbox3(_inspectable.IInspectable):
    ResolveRecipientsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # recipients
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IEmailRecipientResolutionResult]]]],  # result
                                      _type.HRESULT]
    ValidateCertificatesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Security_Cryptography_Certificates.ICertificate],  # certificates
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_enum.Windows.ApplicationModel.Email.EmailCertificateValidationStatus]]]],  # result
                                         _type.HRESULT]
    TryEmptyFolderAsync: _Callable[[_type.HSTRING,  # folderId
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Email.EmailMailboxEmptyFolderStatus]]],  # result
                                   _type.HRESULT]
    TryCreateFolderAsync: _Callable[[_type.HSTRING,  # parentFolderId
                                     _type.HSTRING,  # name
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMailboxCreateFolderResult]]],  # result
                                    _type.HRESULT]
    TryDeleteFolderAsync: _Callable[[_type.HSTRING,  # folderId
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Email.EmailMailboxDeleteFolderStatus]]],  # result
                                    _type.HRESULT]


class IEmailMailbox4(_inspectable.IInspectable):
    RegisterSyncManagerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]


class IEmailMailbox5(_inspectable.IInspectable):
    GetChangeTracker: _Callable[[_type.HSTRING,  # identity
                                 _Pointer[IEmailMailboxChangeTracker]],  # result
                                _type.HRESULT]


class IEmailMailboxAction(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxActionKind]],  # value
                        _type.HRESULT]
    get_ChangeNumber: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]


class IEmailMailboxAutoReply(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Response: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Response: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IEmailMailboxAutoReplySettings(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_ResponseKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind]],  # value
                                _type.HRESULT]
    put_ResponseKind: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxAutoReplyMessageResponseKind],  # value
                                _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_EndTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]
    put_EndTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_InternalReply: _Callable[[_Pointer[IEmailMailboxAutoReply]],  # value
                                 _type.HRESULT]
    get_KnownExternalReply: _Callable[[_Pointer[IEmailMailboxAutoReply]],  # value
                                      _type.HRESULT]
    get_UnknownExternalReply: _Callable[[_Pointer[IEmailMailboxAutoReply]],  # value
                                        _type.HRESULT]


class IEmailMailboxCapabilities(_inspectable.IInspectable):
    get_CanForwardMeetings: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_CanGetAndSetExternalAutoReplies: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    get_CanGetAndSetInternalAutoReplies: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    get_CanUpdateMeetingResponses: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_CanServerSearchFolders: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_CanServerSearchMailbox: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_CanProposeNewTimeForMeetings: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_CanSmartSend: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IEmailMailboxCapabilities2(_inspectable.IInspectable):
    get_CanResolveRecipients: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_CanValidateCertificates: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_CanEmptyFolder: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_CanCreateFolder: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_CanDeleteFolder: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_CanMoveFolder: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IEmailMailboxCapabilities3(_inspectable.IInspectable):
    put_CanForwardMeetings: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    put_CanGetAndSetExternalAutoReplies: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    put_CanGetAndSetInternalAutoReplies: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    put_CanUpdateMeetingResponses: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    put_CanServerSearchFolders: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    put_CanServerSearchMailbox: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    put_CanProposeNewTimeForMeetings: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    put_CanSmartSend: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    put_CanResolveRecipients: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    put_CanValidateCertificates: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    put_CanEmptyFolder: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    put_CanCreateFolder: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    put_CanDeleteFolder: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    put_CanMoveFolder: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class IEmailMailboxChange(_inspectable.IInspectable):
    get_ChangeType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxChangeType]],  # value
                              _type.HRESULT]
    get_MailboxActions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IEmailMailboxAction]]],  # value
                                  _type.HRESULT]
    get_Message: _Callable[[_Pointer[IEmailMessage]],  # value
                           _type.HRESULT]
    get_Folder: _Callable[[_Pointer[IEmailFolder]],  # value
                          _type.HRESULT]


class IEmailMailboxChangeReader(_inspectable.IInspectable):
    AcceptChanges: _Callable[[],
                             _type.HRESULT]
    AcceptChangesThrough: _Callable[[IEmailMailboxChange],  # lastChangeToAcknowledge
                                    _type.HRESULT]
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IEmailMailboxChange]]]],  # value
                              _type.HRESULT]


class IEmailMailboxChangeTracker(_inspectable.IInspectable):
    get_IsTracking: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    Enable: _Callable[[],
                      _type.HRESULT]
    GetChangeReader: _Callable[[_Pointer[IEmailMailboxChangeReader]],  # value
                               _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class IEmailMailboxChangedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IEmailMailboxChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IEmailMailboxChangedDeferral]],  # result
                           _type.HRESULT]


class IEmailMailboxCreateFolderResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxCreateFolderStatus]],  # value
                          _type.HRESULT]
    get_Folder: _Callable[[_Pointer[IEmailFolder]],  # value
                          _type.HRESULT]


class IEmailMailboxPolicies(_inspectable.IInspectable):
    get_AllowedSmimeEncryptionAlgorithmNegotiation: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation]],  # value
                                                              _type.HRESULT]
    get_AllowSmimeSoftCertificates: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_RequiredSmimeEncryptionAlgorithm: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.Email.EmailMailboxSmimeEncryptionAlgorithm]]],  # value
                                                    _type.HRESULT]
    get_RequiredSmimeSigningAlgorithm: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.Email.EmailMailboxSmimeSigningAlgorithm]]],  # value
                                                 _type.HRESULT]


class IEmailMailboxPolicies2(_inspectable.IInspectable):
    get_MustEncryptSmimeMessages: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_MustSignSmimeMessages: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class IEmailMailboxPolicies3(_inspectable.IInspectable):
    put_AllowedSmimeEncryptionAlgorithmNegotiation: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxAllowedSmimeEncryptionAlgorithmNegotiation],  # value
                                                              _type.HRESULT]
    put_AllowSmimeSoftCertificates: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    put_RequiredSmimeEncryptionAlgorithm: _Callable[[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.Email.EmailMailboxSmimeEncryptionAlgorithm]],  # value
                                                    _type.HRESULT]
    put_RequiredSmimeSigningAlgorithm: _Callable[[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.Email.EmailMailboxSmimeSigningAlgorithm]],  # value
                                                 _type.HRESULT]
    put_MustEncryptSmimeMessages: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    put_MustSignSmimeMessages: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IEmailMailboxSyncManager(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMailboxSyncStatus]],  # value
                          _type.HRESULT]
    get_LastSuccessfulSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                          _type.HRESULT]
    get_LastAttemptedSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                         _type.HRESULT]
    SyncAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                         _type.HRESULT]
    add_SyncStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IEmailMailboxSyncManager, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SyncStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IEmailMailboxSyncManager2(_inspectable.IInspectable):
    put_Status: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMailboxSyncStatus],  # value
                          _type.HRESULT]
    put_LastSuccessfulSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                          _type.HRESULT]
    put_LastAttemptedSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                         _type.HRESULT]


class IEmailManagerForUser(_inspectable.IInspectable):
    ShowComposeNewEmailAsync: _Callable[[IEmailMessage,  # message
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailStoreAccessType,  # accessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IEmailStore]]],  # result
                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IEmailManagerStatics(_inspectable.IInspectable):
    ShowComposeNewEmailAsync: _Callable[[IEmailMessage,  # message
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                        _type.HRESULT]

    _factory = True


class IEmailManagerStatics2(_inspectable.IInspectable):
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Email.EmailStoreAccessType,  # accessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IEmailStore]]],  # result
                                 _type.HRESULT]

    _factory = True


class IEmailManagerStatics3(_inspectable.IInspectable):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IEmailManagerForUser]],  # result
                          _type.HRESULT]

    _factory = True


class IEmailMeetingInfo(_inspectable.IInspectable):
    get_AllowNewTimeProposal: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_AllowNewTimeProposal: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_AppointmentRoamingId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    put_AppointmentRoamingId: _Callable[[_type.HSTRING],  # value
                                        _type.HRESULT]
    get_AppointmentOriginalStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    put_AppointmentOriginalStartTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                                _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_IsAllDay: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsAllDay: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_IsResponseRequested: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsResponseRequested: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_Location: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Location: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_ProposedStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # proposedStartTime
                                     _type.HRESULT]
    put_ProposedStartTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # proposedStartTime
                                     _type.HRESULT]
    get_ProposedDuration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # duration
                                    _type.HRESULT]
    put_ProposedDuration: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # duration
                                    _type.HRESULT]
    get_RecurrenceStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                       _type.HRESULT]
    put_RecurrenceStartTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                       _type.HRESULT]
    get_Recurrence: _Callable[[_Pointer[_Windows_ApplicationModel_Appointments.IAppointmentRecurrence]],  # value
                              _type.HRESULT]
    put_Recurrence: _Callable[[_Windows_ApplicationModel_Appointments.IAppointmentRecurrence],  # value
                              _type.HRESULT]
    get_RemoteChangeNumber: _Callable[[_Pointer[_type.UINT64]],  # value
                                      _type.HRESULT]
    put_RemoteChangeNumber: _Callable[[_type.UINT64],  # value
                                      _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                             _type.HRESULT]


class IEmailMeetingInfo2(_inspectable.IInspectable):
    get_IsReportedOutOfDateByServer: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IEmailMessage(_inspectable.IInspectable):
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Subject: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Body: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_To: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IEmailRecipient]]],  # value
                      _type.HRESULT]
    get_CC: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IEmailRecipient]]],  # value
                      _type.HRESULT]
    get_Bcc: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IEmailRecipient]]],  # value
                       _type.HRESULT]
    get_Attachments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IEmailAttachment]]],  # value
                               _type.HRESULT]


class IEmailMessage2(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_MailboxId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ConversationId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_FolderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_AllowInternetImages: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_AllowInternetImages: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_ChangeNumber: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]
    get_DownloadState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMessageDownloadState]],  # value
                                 _type.HRESULT]
    put_DownloadState: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMessageDownloadState],  # value
                                 _type.HRESULT]
    get_EstimatedDownloadSizeInBytes: _Callable[[_Pointer[_type.UINT32]],  # value
                                                _type.HRESULT]
    put_EstimatedDownloadSizeInBytes: _Callable[[_type.UINT32],  # value
                                                _type.HRESULT]
    get_FlagState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailFlagState]],  # value
                             _type.HRESULT]
    put_FlagState: _Callable[[_enum.Windows.ApplicationModel.Email.EmailFlagState],  # value
                             _type.HRESULT]
    get_HasPartialBodies: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_Importance: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailImportance]],  # value
                              _type.HRESULT]
    put_Importance: _Callable[[_enum.Windows.ApplicationModel.Email.EmailImportance],  # value
                              _type.HRESULT]
    get_InResponseToMessageId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_IrmInfo: _Callable[[_Pointer[IEmailIrmInfo]],  # value
                           _type.HRESULT]
    put_IrmInfo: _Callable[[IEmailIrmInfo],  # value
                           _type.HRESULT]
    get_IsDraftMessage: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_IsRead: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_IsRead: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsSeen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_IsSeen: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsServerSearchMessage: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_IsSmartSendable: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_MessageClass: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_MessageClass: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_NormalizedSubject: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_OriginalCodePage: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_OriginalCodePage: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_Preview: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Preview: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_LastResponseKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMessageResponseKind]],  # value
                                    _type.HRESULT]
    put_LastResponseKind: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMessageResponseKind],  # value
                                    _type.HRESULT]
    get_Sender: _Callable[[_Pointer[IEmailRecipient]],  # value
                          _type.HRESULT]
    put_Sender: _Callable[[IEmailRecipient],  # value
                          _type.HRESULT]
    get_SentTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                            _type.HRESULT]
    put_SentTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    get_MeetingInfo: _Callable[[_Pointer[IEmailMeetingInfo]],  # value
                               _type.HRESULT]
    put_MeetingInfo: _Callable[[IEmailMeetingInfo],  # value
                               _type.HRESULT]
    GetBodyStream: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMessageBodyKind,  # type
                              _Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # result
                             _type.HRESULT]
    SetBodyStream: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMessageBodyKind,  # type
                              _Windows_Storage_Streams.IRandomAccessStreamReference],  # stream
                             _type.HRESULT]


class IEmailMessage3(_inspectable.IInspectable):
    get_SmimeData: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    put_SmimeData: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    get_SmimeKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailMessageSmimeKind]],  # value
                             _type.HRESULT]
    put_SmimeKind: _Callable[[_enum.Windows.ApplicationModel.Email.EmailMessageSmimeKind],  # value
                             _type.HRESULT]


class IEmailMessage4(_inspectable.IInspectable):
    get_ReplyTo: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IEmailRecipient]]],  # value
                           _type.HRESULT]
    get_SentRepresenting: _Callable[[_Pointer[IEmailRecipient]],  # value
                                    _type.HRESULT]
    put_SentRepresenting: _Callable[[IEmailRecipient],  # value
                                    _type.HRESULT]


class IEmailMessageBatch(_inspectable.IInspectable):
    get_Messages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IEmailMessage]]],  # value
                            _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailBatchStatus]],  # value
                          _type.HRESULT]


class IEmailMessageReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IEmailMessageBatch]]],  # result
                              _type.HRESULT]


class IEmailQueryOptions(_inspectable.IInspectable):
    get_TextSearch: _Callable[[_Pointer[IEmailQueryTextSearch]],  # value
                              _type.HRESULT]
    get_SortDirection: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailQuerySortDirection]],  # value
                                 _type.HRESULT]
    put_SortDirection: _Callable[[_enum.Windows.ApplicationModel.Email.EmailQuerySortDirection],  # value
                                 _type.HRESULT]
    get_SortProperty: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailQuerySortProperty]],  # value
                                _type.HRESULT]
    put_SortProperty: _Callable[[_enum.Windows.ApplicationModel.Email.EmailQuerySortProperty],  # value
                                _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailQueryKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.ApplicationModel.Email.EmailQueryKind],  # value
                        _type.HRESULT]
    get_FolderIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]


class IEmailQueryOptionsFactory(_inspectable.IInspectable):
    CreateWithText: _Callable[[_type.HSTRING,  # text
                               _Pointer[IEmailQueryOptions]],  # result
                              _type.HRESULT]
    CreateWithTextAndFields: _Callable[[_type.HSTRING,  # text
                                        _enum.Windows.ApplicationModel.Email.EmailQuerySearchFields,  # fields
                                        _Pointer[IEmailQueryOptions]],  # result
                                       _type.HRESULT]

    _factory = True


class IEmailQueryTextSearch(_inspectable.IInspectable):
    get_Fields: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailQuerySearchFields]],  # value
                          _type.HRESULT]
    put_Fields: _Callable[[_enum.Windows.ApplicationModel.Email.EmailQuerySearchFields],  # value
                          _type.HRESULT]
    get_SearchScope: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailQuerySearchScope]],  # value
                               _type.HRESULT]
    put_SearchScope: _Callable[[_enum.Windows.ApplicationModel.Email.EmailQuerySearchScope],  # value
                               _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IEmailRecipient(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Address: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Address: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]


class IEmailRecipientFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # address
                       _Pointer[IEmailRecipient]],  # result
                      _type.HRESULT]
    CreateWithName: _Callable[[_type.HSTRING,  # address
                               _type.HSTRING,  # name
                               _Pointer[IEmailRecipient]],  # result
                              _type.HRESULT]

    _factory = True


class IEmailRecipientResolutionResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Email.EmailRecipientResolutionStatus]],  # value
                          _type.HRESULT]
    get_PublicKeys: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Security_Cryptography_Certificates.ICertificate]]],  # value
                              _type.HRESULT]


class IEmailRecipientResolutionResult2(_inspectable.IInspectable):
    put_Status: _Callable[[_enum.Windows.ApplicationModel.Email.EmailRecipientResolutionStatus],  # value
                          _type.HRESULT]
    SetPublicKeys: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Security_Cryptography_Certificates.ICertificate]],  # value
                             _type.HRESULT]


class IEmailStore(_inspectable.IInspectable):
    FindMailboxesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IEmailMailbox]]]],  # result
                                  _type.HRESULT]
    GetConversationReader: _Callable[[_Pointer[IEmailConversationReader]],  # result
                                     _type.HRESULT]
    GetConversationReaderWithOptions: _Callable[[IEmailQueryOptions,  # options
                                                 _Pointer[IEmailConversationReader]],  # result
                                                _type.HRESULT]
    GetMessageReader: _Callable[[_Pointer[IEmailMessageReader]],  # result
                                _type.HRESULT]
    GetMessageReaderWithOptions: _Callable[[IEmailQueryOptions,  # options
                                            _Pointer[IEmailMessageReader]],  # result
                                           _type.HRESULT]
    GetMailboxAsync: _Callable[[_type.HSTRING,  # id
                                _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMailbox]]],  # result
                               _type.HRESULT]
    GetConversationAsync: _Callable[[_type.HSTRING,  # id
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IEmailConversation]]],  # result
                                    _type.HRESULT]
    GetFolderAsync: _Callable[[_type.HSTRING,  # id
                               _Pointer[_Windows_Foundation.IAsyncOperation[IEmailFolder]]],  # result
                              _type.HRESULT]
    GetMessageAsync: _Callable[[_type.HSTRING,  # id
                                _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMessage]]],  # result
                               _type.HRESULT]
    CreateMailboxAsync: _Callable[[_type.HSTRING,  # accountName
                                   _type.HSTRING,  # accountAddress
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMailbox]]],  # result
                                  _type.HRESULT]
    CreateMailboxInAccountAsync: _Callable[[_type.HSTRING,  # accountName
                                            _type.HSTRING,  # accountAddress
                                            _type.HSTRING,  # userDataAccountId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IEmailMailbox]]],  # result
                                           _type.HRESULT]


class IEmailStoreNotificationTriggerDetails(_inspectable.IInspectable):
    pass
