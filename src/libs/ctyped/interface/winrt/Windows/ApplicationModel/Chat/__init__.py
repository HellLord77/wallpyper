from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Media import MediaProperties as _Windows_Media_MediaProperties
from ...Security import Credentials as _Windows_Security_Credentials
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IChatCapabilities(_inspectable.IInspectable):
    get_IsOnline: _Callable[[_Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    get_IsChatCapable: _Callable[[_Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    get_IsFileTransferCapable: _Callable[[_Pointer[_type.boolean]],  # result
                                         _type.HRESULT]
    get_IsGeoLocationPushCapable: _Callable[[_Pointer[_type.boolean]],  # result
                                            _type.HRESULT]
    get_IsIntegratedMessagingCapable: _Callable[[_Pointer[_type.boolean]],  # result
                                                _type.HRESULT]


class IChatCapabilitiesManagerStatics(_inspectable.IInspectable):
    GetCachedCapabilitiesAsync: _Callable[[_type.HSTRING,  # address
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IChatCapabilities]]],  # result
                                          _type.HRESULT]
    GetCapabilitiesFromNetworkAsync: _Callable[[_type.HSTRING,  # address
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IChatCapabilities]]],  # result
                                               _type.HRESULT]

    _factory = True


class IChatCapabilitiesManagerStatics2(_inspectable.IInspectable):
    GetCachedCapabilitiesForTransportAsync: _Callable[[_type.HSTRING,  # address
                                                       _type.HSTRING,  # transportId
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IChatCapabilities]]],  # operation
                                                      _type.HRESULT]
    GetCapabilitiesFromNetworkForTransportAsync: _Callable[[_type.HSTRING,  # address
                                                            _type.HSTRING,  # transportId
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[IChatCapabilities]]],  # operation
                                                           _type.HRESULT]

    _factory = True


class IChatConversation(_inspectable.IInspectable):
    get_HasUnreadMessages: _Callable[[_Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # result
                           _type.HRESULT]
    put_Subject: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_IsConversationMuted: _Callable[[_Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    put_IsConversationMuted: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_MostRecentMessageId: _Callable[[_Pointer[_type.HSTRING]],  # result
                                       _type.HRESULT]
    get_Participants: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                _type.HRESULT]
    get_ThreadingInfo: _Callable[[_Pointer[IChatConversationThreadingInfo]],  # result
                                 _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                           _type.HRESULT]
    GetMessageReader: _Callable[[_Pointer[IChatMessageReader]],  # result
                                _type.HRESULT]
    MarkAllMessagesAsReadAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                          _type.HRESULT]
    MarkMessagesAsReadAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # value
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                       _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                         _type.HRESULT]
    NotifyLocalParticipantComposing: _Callable[[_type.HSTRING,  # transportId
                                                _type.HSTRING,  # participantAddress
                                                _type.boolean],  # isComposing
                                               _type.HRESULT]
    NotifyRemoteParticipantComposing: _Callable[[_type.HSTRING,  # transportId
                                                 _type.HSTRING,  # participantAddress
                                                 _type.boolean],  # isComposing
                                                _type.HRESULT]
    add_RemoteParticipantComposingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IChatConversation, IRemoteParticipantComposingChangedEventArgs],  # handler
                                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                                     _type.HRESULT]
    remove_RemoteParticipantComposingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                        _type.HRESULT]


class IChatConversation2(_inspectable.IInspectable):
    get_CanModifyParticipants: _Callable[[_Pointer[_type.boolean]],  # result
                                         _type.HRESULT]
    put_CanModifyParticipants: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IChatConversationReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatConversation]]]],  # result
                              _type.HRESULT]
    ReadBatchWithCountAsync: _Callable[[_type.INT32,  # count
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatConversation]]]],  # result
                                       _type.HRESULT]


class IChatConversationThreadingInfo(_inspectable.IInspectable):
    get_ContactId: _Callable[[_Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]
    put_ContactId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Custom: _Callable[[_Pointer[_type.HSTRING]],  # result
                          _type.HRESULT]
    put_Custom: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_ConversationId: _Callable[[_Pointer[_type.HSTRING]],  # result
                                  _type.HRESULT]
    put_ConversationId: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_Participants: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatConversationThreadingKind]],  # result
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.ApplicationModel.Chat.ChatConversationThreadingKind],  # value
                        _type.HRESULT]


class IChatItem(_inspectable.IInspectable):
    get_ItemKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatItemKind]],  # result
                            _type.HRESULT]


class IChatMessage(_inspectable.IInspectable):
    get_Attachments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IChatMessageAttachment]]],  # value
                               _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Body: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_From: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_IsForwardingDisabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsIncoming: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsRead: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_LocalTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_NetworkTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                    _type.HRESULT]
    get_Recipients: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                              _type.HRESULT]
    get_RecipientSendStatuses: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _enum.Windows.ApplicationModel.Chat.ChatMessageStatus]]],  # value
                                         _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatMessageStatus]],  # value
                          _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_TransportFriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_TransportId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_TransportId: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IChatMessage2(_inspectable.IInspectable):
    get_EstimatedDownloadSize: _Callable[[_Pointer[_type.UINT64]],  # result
                                         _type.HRESULT]
    put_EstimatedDownloadSize: _Callable[[_type.UINT64],  # value
                                         _type.HRESULT]
    put_From: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_IsAutoReply: _Callable[[_Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    put_IsAutoReply: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    put_IsForwardingDisabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsReplyDisabled: _Callable[[_Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    put_IsIncoming: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    put_IsRead: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsSeen: _Callable[[_Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    put_IsSeen: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsSimMessage: _Callable[[_Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    put_LocalTimestamp: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                  _type.HRESULT]
    get_MessageKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatMessageKind]],  # result
                               _type.HRESULT]
    put_MessageKind: _Callable[[_enum.Windows.ApplicationModel.Chat.ChatMessageKind],  # value
                               _type.HRESULT]
    get_MessageOperatorKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatMessageOperatorKind]],  # result
                                       _type.HRESULT]
    put_MessageOperatorKind: _Callable[[_enum.Windows.ApplicationModel.Chat.ChatMessageOperatorKind],  # value
                                       _type.HRESULT]
    put_NetworkTimestamp: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                    _type.HRESULT]
    get_IsReceivedDuringQuietHours: _Callable[[_Pointer[_type.boolean]],  # result
                                              _type.HRESULT]
    put_IsReceivedDuringQuietHours: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    put_Status: _Callable[[_enum.Windows.ApplicationModel.Chat.ChatMessageStatus],  # value
                          _type.HRESULT]
    put_Subject: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_ShouldSuppressNotification: _Callable[[_Pointer[_type.boolean]],  # result
                                              _type.HRESULT]
    put_ShouldSuppressNotification: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_ThreadingInfo: _Callable[[_Pointer[IChatConversationThreadingInfo]],  # result
                                 _type.HRESULT]
    put_ThreadingInfo: _Callable[[IChatConversationThreadingInfo],  # value
                                 _type.HRESULT]
    get_RecipientsDeliveryInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IChatRecipientDeliveryInfo]]],  # result
                                           _type.HRESULT]


class IChatMessage3(_inspectable.IInspectable):
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IChatMessage4(_inspectable.IInspectable):
    get_SyncId: _Callable[[_Pointer[_type.HSTRING]],  # result
                          _type.HRESULT]
    put_SyncId: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]


class IChatMessageAttachment(_inspectable.IInspectable):
    get_DataStreamReference: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                       _type.HRESULT]
    put_DataStreamReference: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                                       _type.HRESULT]
    get_GroupId: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_GroupId: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_MimeType: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_MimeType: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IChatMessageAttachment2(_inspectable.IInspectable):
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # result
                             _type.HRESULT]
    put_Thumbnail: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    get_TransferProgress: _Callable[[_Pointer[_type.DOUBLE]],  # result
                                    _type.HRESULT]
    put_TransferProgress: _Callable[[_type.DOUBLE],  # value
                                    _type.HRESULT]
    get_OriginalFileName: _Callable[[_Pointer[_type.HSTRING]],  # result
                                    _type.HRESULT]
    put_OriginalFileName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]


class IChatMessageAttachmentFactory(_inspectable.IInspectable):
    CreateChatMessageAttachment: _Callable[[_type.HSTRING,  # mimeType
                                            _Windows_Storage_Streams.IRandomAccessStreamReference,  # dataStreamReference
                                            _Pointer[IChatMessageAttachment]],  # value
                                           _type.HRESULT]

    _factory = True


class IChatMessageBlockingStatic(_inspectable.IInspectable):
    MarkMessageAsBlockedAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                          _type.boolean,  # blocked
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                         _type.HRESULT]

    _factory = True


class IChatMessageChange(_inspectable.IInspectable):
    get_ChangeType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatMessageChangeType]],  # value
                              _type.HRESULT]
    get_Message: _Callable[[_Pointer[IChatMessage]],  # value
                           _type.HRESULT]


class IChatMessageChangeReader(_inspectable.IInspectable):
    AcceptChanges: _Callable[[],
                             _type.HRESULT]
    AcceptChangesThrough: _Callable[[IChatMessageChange],  # lastChangeToAcknowledge
                                    _type.HRESULT]
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatMessageChange]]]],  # value
                              _type.HRESULT]


class IChatMessageChangeTracker(_inspectable.IInspectable):
    Enable: _Callable[[],
                      _type.HRESULT]
    GetChangeReader: _Callable[[_Pointer[IChatMessageChangeReader]],  # value
                               _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class IChatMessageChangedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IChatMessageChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IChatMessageChangedDeferral]],  # result
                           _type.HRESULT]


class IChatMessageManager2Statics(_inspectable.IInspectable):
    RegisterTransportAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                      _type.HRESULT]
    GetTransportAsync: _Callable[[_type.HSTRING,  # transportId
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IChatMessageTransport]]],  # result
                                 _type.HRESULT]

    _factory = True


class IChatMessageManagerStatic(_inspectable.IInspectable):
    GetTransportsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatMessageTransport]]]],  # value
                                  _type.HRESULT]
    RequestStoreAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IChatMessageStore]]],  # value
                                 _type.HRESULT]
    ShowComposeSmsMessageAsync: _Callable[[IChatMessage,  # message
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                          _type.HRESULT]
    ShowSmsSettings: _Callable[[],
                               _type.HRESULT]

    _factory = True


class IChatMessageManagerStatics3(_inspectable.IInspectable):
    RequestSyncManagerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IChatSyncManager]]],  # result
                                       _type.HRESULT]

    _factory = True


class IChatMessageNotificationTriggerDetails(_inspectable.IInspectable):
    get_ChatMessage: _Callable[[_Pointer[IChatMessage]],  # value
                               _type.HRESULT]


class IChatMessageNotificationTriggerDetails2(_inspectable.IInspectable):
    get_ShouldDisplayToast: _Callable[[_Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    get_ShouldUpdateDetailText: _Callable[[_Pointer[_type.boolean]],  # result
                                          _type.HRESULT]
    get_ShouldUpdateBadge: _Callable[[_Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    get_ShouldUpdateActionCenter: _Callable[[_Pointer[_type.boolean]],  # result
                                            _type.HRESULT]


class IChatMessageReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatMessage]]]],  # value
                              _type.HRESULT]


class IChatMessageReader2(_inspectable.IInspectable):
    ReadBatchWithCountAsync: _Callable[[_type.INT32,  # count
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatMessage]]]],  # result
                                       _type.HRESULT]


class IChatMessageStore(_inspectable.IInspectable):
    get_ChangeTracker: _Callable[[_Pointer[IChatMessageChangeTracker]],  # value
                                 _type.HRESULT]
    DeleteMessageAsync: _Callable[[_type.HSTRING,  # localMessageId
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                  _type.HRESULT]
    DownloadMessageAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                    _type.HRESULT]
    GetMessageAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                _Pointer[_Windows_Foundation.IAsyncOperation[IChatMessage]]],  # value
                               _type.HRESULT]
    GetMessageReader1: _Callable[[_Pointer[IChatMessageReader]],  # value
                                 _type.HRESULT]
    GetMessageReader2: _Callable[[_struct.Windows.Foundation.TimeSpan,  # recentTimeLimit
                                  _Pointer[IChatMessageReader]],  # value
                                 _type.HRESULT]
    MarkMessageReadAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                    _type.HRESULT]
    RetrySendMessageAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                     _type.HRESULT]
    SendMessageAsync: _Callable[[IChatMessage,  # chatMessage
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                _type.HRESULT]
    ValidateMessage: _Callable[[IChatMessage,  # chatMessage
                                _Pointer[IChatMessageValidationResult]],  # value
                               _type.HRESULT]
    add_MessageChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IChatMessageStore, IChatMessageChangedEventArgs],  # value
                                   _Pointer[_struct.EventRegistrationToken]],  # returnValue
                                  _type.HRESULT]
    remove_MessageChanged: _Callable[[_struct.EventRegistrationToken],  # value
                                     _type.HRESULT]


class IChatMessageStore2(_inspectable.IInspectable):
    ForwardMessageAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                    _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # addresses
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IChatMessage]]],  # result
                                   _type.HRESULT]
    GetConversationAsync: _Callable[[_type.HSTRING,  # conversationId
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IChatConversation]]],  # result
                                    _type.HRESULT]
    GetConversationForTransportsAsync: _Callable[[_type.HSTRING,  # conversationId
                                                  _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # transportIds
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IChatConversation]]],  # result
                                                 _type.HRESULT]
    GetConversationFromThreadingInfoAsync: _Callable[[IChatConversationThreadingInfo,  # threadingInfo
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IChatConversation]]],  # result
                                                     _type.HRESULT]
    GetConversationReader: _Callable[[_Pointer[IChatConversationReader]],  # result
                                     _type.HRESULT]
    GetConversationForTransportsReader: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # transportIds
                                                   _Pointer[IChatConversationReader]],  # result
                                                  _type.HRESULT]
    GetMessageByRemoteIdAsync: _Callable[[_type.HSTRING,  # transportId
                                          _type.HSTRING,  # remoteId
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IChatMessage]]],  # result
                                         _type.HRESULT]
    GetUnseenCountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.INT32]]],  # result
                                   _type.HRESULT]
    GetUnseenCountForTransportsReaderAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # transportIds
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.INT32]]],  # result
                                                      _type.HRESULT]
    MarkAsSeenAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                               _type.HRESULT]
    MarkAsSeenForTransportsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # transportIds
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                            _type.HRESULT]
    GetSearchReader: _Callable[[IChatQueryOptions,  # value
                                _Pointer[IChatSearchReader]],  # result
                               _type.HRESULT]
    SaveMessageAsync: _Callable[[IChatMessage,  # chatMessage
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                _type.HRESULT]
    TryCancelDownloadMessageAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                             _type.HRESULT]
    TryCancelSendMessageAsync: _Callable[[_type.HSTRING,  # localChatMessageId
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                         _type.HRESULT]
    add_StoreChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IChatMessageStore, IChatMessageStoreChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StoreChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IChatMessageStore3(_inspectable.IInspectable):
    GetMessageBySyncIdAsync: _Callable[[_type.HSTRING,  # syncId
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IChatMessage]]],  # result
                                       _type.HRESULT]


class IChatMessageStoreChangedEventArgs(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # result
                      _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatStoreChangedEventKind]],  # result
                        _type.HRESULT]


class IChatMessageTransport(_inspectable.IInspectable):
    get_IsAppSetAsNotificationProvider: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_TransportFriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_TransportId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    RequestSetAsNotificationProviderAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                                     _type.HRESULT]


class IChatMessageTransport2(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[IChatMessageTransportConfiguration]],  # result
                                 _type.HRESULT]
    get_TransportKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatMessageTransportKind]],  # result
                                 _type.HRESULT]


class IChatMessageTransportConfiguration(_inspectable.IInspectable):
    get_MaxAttachmentCount: _Callable[[_Pointer[_type.INT32]],  # result
                                      _type.HRESULT]
    get_MaxMessageSizeInKilobytes: _Callable[[_Pointer[_type.INT32]],  # result
                                             _type.HRESULT]
    get_MaxRecipientCount: _Callable[[_Pointer[_type.INT32]],  # result
                                     _type.HRESULT]
    get_SupportedVideoFormat: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaEncodingProfile]],  # result
                                        _type.HRESULT]
    get_ExtendedProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # result
                                      _type.HRESULT]


class IChatMessageValidationResult(_inspectable.IInspectable):
    get_MaxPartCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                _type.HRESULT]
    get_PartCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                             _type.HRESULT]
    get_RemainingCharacterCountInPart: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatMessageValidationStatus]],  # value
                          _type.HRESULT]


class IChatQueryOptions(_inspectable.IInspectable):
    get_SearchString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                _type.HRESULT]
    put_SearchString: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]


class IChatRecipientDeliveryInfo(_inspectable.IInspectable):
    get_TransportAddress: _Callable[[_Pointer[_type.HSTRING]],  # result
                                    _type.HRESULT]
    put_TransportAddress: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_DeliveryTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # result
                                _type.HRESULT]
    put_DeliveryTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    get_ReadTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # result
                            _type.HRESULT]
    put_ReadTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    get_TransportErrorCodeCategory: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatTransportErrorCodeCategory]],  # result
                                              _type.HRESULT]
    get_TransportInterpretedErrorCode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatTransportInterpretedErrorCode]],  # result
                                                 _type.HRESULT]
    get_TransportErrorCode: _Callable[[_Pointer[_type.INT32]],  # result
                                      _type.HRESULT]
    get_IsErrorPermanent: _Callable[[_Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatMessageStatus]],  # result
                          _type.HRESULT]


class IChatSearchReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatItem]]]],  # result
                              _type.HRESULT]
    ReadBatchWithCountAsync: _Callable[[_type.INT32,  # count
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IChatItem]]]],  # result
                                       _type.HRESULT]


class IChatSyncConfiguration(_inspectable.IInspectable):
    get_IsSyncEnabled: _Callable[[_Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    put_IsSyncEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_RestoreHistorySpan: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.ChatRestoreHistorySpan]],  # result
                                      _type.HRESULT]
    put_RestoreHistorySpan: _Callable[[_enum.Windows.ApplicationModel.Chat.ChatRestoreHistorySpan],  # value
                                      _type.HRESULT]


class IChatSyncManager(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[IChatSyncConfiguration]],  # result
                                 _type.HRESULT]
    AssociateAccountAsync: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]
    UnassociateAccountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                       _type.HRESULT]
    IsAccountAssociated: _Callable[[_Windows_Security_Credentials.IWebAccount,  # webAccount
                                    _Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    StartSync: _Callable[[],
                         _type.HRESULT]
    SetConfigurationAsync: _Callable[[IChatSyncConfiguration,  # configuration
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                     _type.HRESULT]


class IRcsEndUserMessage(_inspectable.IInspectable):
    get_TransportId: _Callable[[_Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # result
                        _type.HRESULT]
    get_IsPinRequired: _Callable[[_Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    get_Actions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IRcsEndUserMessageAction]]],  # result
                           _type.HRESULT]
    SendResponseAsync: _Callable[[IRcsEndUserMessageAction,  # action
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]
    SendResponseWithPinAsync: _Callable[[IRcsEndUserMessageAction,  # action
                                         _type.HSTRING,  # pin
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]


class IRcsEndUserMessageAction(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]


class IRcsEndUserMessageAvailableEventArgs(_inspectable.IInspectable):
    get_IsMessageAvailable: _Callable[[_Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    get_Message: _Callable[[_Pointer[IRcsEndUserMessage]],  # result
                           _type.HRESULT]


class IRcsEndUserMessageAvailableTriggerDetails(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IRcsEndUserMessageManager(_inspectable.IInspectable):
    add_MessageAvailableChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRcsEndUserMessageManager, IRcsEndUserMessageAvailableEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_MessageAvailableChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IRcsManagerStatics(_inspectable.IInspectable):
    GetEndUserMessageManager: _Callable[[_Pointer[IRcsEndUserMessageManager]],  # result
                                        _type.HRESULT]
    GetTransportsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IRcsTransport]]]],  # value
                                  _type.HRESULT]
    GetTransportAsync: _Callable[[_type.HSTRING,  # transportId
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IRcsTransport]]],  # result
                                 _type.HRESULT]
    LeaveConversationAsync: _Callable[[IChatConversation,  # conversation
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                      _type.HRESULT]

    _factory = True


class IRcsManagerStatics2(_inspectable.IInspectable):
    add_TransportListChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_TransportListChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]

    _factory = True


class IRcsServiceKindSupportedChangedEventArgs(_inspectable.IInspectable):
    get_ServiceKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Chat.RcsServiceKind]],  # result
                               _type.HRESULT]


class IRcsTransport(_inspectable.IInspectable):
    get_ExtendedProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                                      _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_TransportFriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_TransportId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Configuration: _Callable[[_Pointer[IRcsTransportConfiguration]],  # result
                                 _type.HRESULT]
    IsStoreAndForwardEnabled: _Callable[[_enum.Windows.ApplicationModel.Chat.RcsServiceKind,  # serviceKind
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]
    IsServiceKindSupported: _Callable[[_enum.Windows.ApplicationModel.Chat.RcsServiceKind,  # serviceKind
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    add_ServiceKindSupportedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRcsTransport, IRcsServiceKindSupportedChangedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_ServiceKindSupportedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IRcsTransportConfiguration(_inspectable.IInspectable):
    get_MaxAttachmentCount: _Callable[[_Pointer[_type.INT32]],  # result
                                      _type.HRESULT]
    get_MaxMessageSizeInKilobytes: _Callable[[_Pointer[_type.INT32]],  # result
                                             _type.HRESULT]
    get_MaxGroupMessageSizeInKilobytes: _Callable[[_Pointer[_type.INT32]],  # result
                                                  _type.HRESULT]
    get_MaxRecipientCount: _Callable[[_Pointer[_type.INT32]],  # result
                                     _type.HRESULT]
    get_MaxFileSizeInKilobytes: _Callable[[_Pointer[_type.INT32]],  # result
                                          _type.HRESULT]
    get_WarningFileSizeInKilobytes: _Callable[[_Pointer[_type.INT32]],  # result
                                              _type.HRESULT]


class IRemoteParticipantComposingChangedEventArgs(_inspectable.IInspectable):
    get_TransportId: _Callable[[_Pointer[_type.HSTRING]],  # result
                               _type.HRESULT]
    get_ParticipantAddress: _Callable[[_Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]
    get_IsComposing: _Callable[[_Pointer[_type.boolean]],  # result
                               _type.HRESULT]
