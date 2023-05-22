from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _ISmsDeviceStatusChangedEventHandler:
    Invoke: _Callable[[ISmsDevice],  # sender
                      _type.HRESULT]


class ISmsDeviceStatusChangedEventHandler(_ISmsDeviceStatusChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISmsDeviceStatusChangedEventHandler_impl(_ISmsDeviceStatusChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ISmsMessageReceivedEventHandler:
    Invoke: _Callable[[ISmsDevice,  # sender
                       ISmsMessageReceivedEventArgs],  # e
                      _type.HRESULT]


class ISmsMessageReceivedEventHandler(_ISmsMessageReceivedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISmsMessageReceivedEventHandler_impl(_ISmsMessageReceivedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ISmsAppMessage(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_To: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_To: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_From: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Body: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_CallbackNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_CallbackNumber: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_IsDeliveryNotificationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsDeliveryNotificationEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_RetryAttemptCount: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    put_RetryAttemptCount: _Callable[[_type.INT32],  # value
                                     _type.HRESULT]
    get_Encoding: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsEncoding]],  # value
                            _type.HRESULT]
    put_Encoding: _Callable[[_enum.Windows.Devices.Sms.SmsEncoding],  # value
                            _type.HRESULT]
    get_PortNumber: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_PortNumber: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_TeleserviceId: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_TeleserviceId: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_ProtocolId: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_ProtocolId: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_BinaryBody: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                              _type.HRESULT]
    put_BinaryBody: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                              _type.HRESULT]


class ISmsBinaryMessage(_inspectable.IInspectable):
    Format: _Callable[[_enum.Windows.Devices.Sms.SmsDataFormat],  # value
                      _type.HRESULT]
    GetData: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                        _Pointer[_Pointer[_type.BYTE]]],  # value
                       _type.HRESULT]
    SetData: _Callable[[_type.UINT32,  # __valueSize
                        _Pointer[_type.BYTE]],  # value
                       _type.HRESULT]


class ISmsBroadcastMessage(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_To: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Channel: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    get_GeographicalScope: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsGeographicalScope]],  # value
                                     _type.HRESULT]
    get_MessageCode: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_UpdateNumber: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_BroadcastType: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsBroadcastType]],  # value
                                 _type.HRESULT]
    get_IsEmergencyAlert: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsUserPopupRequested: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class ISmsDevice(_inspectable.IInspectable):
    SendMessageAsync: _Callable[[ISmsMessage,  # message
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                _type.HRESULT]
    CalculateLength: _Callable[[ISmsTextMessage,  # message
                                _Pointer[_struct.Windows.Devices.Sms.SmsEncodedLength]],  # encodedLength
                               _type.HRESULT]
    AccountPhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    CellularClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.CellularClass]],  # value
                             _type.HRESULT]
    MessageStore: _Callable[[_Pointer[ISmsDeviceMessageStore]],  # value
                            _type.HRESULT]
    DeviceStatus: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsDeviceStatus]],  # value
                            _type.HRESULT]
    SmsMessageReceived: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                  _type.HRESULT]
    SmsDeviceStatusChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                      _type.HRESULT]


class ISmsDevice2(_inspectable.IInspectable):
    get_SmscAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_SmscAddress: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ParentDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AccountPhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_CellularClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.CellularClass]],  # value
                                 _type.HRESULT]
    get_DeviceStatus: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsDeviceStatus]],  # value
                                _type.HRESULT]
    CalculateLength: _Callable[[ISmsMessageBase,  # message
                                _Pointer[_struct.Windows.Devices.Sms.SmsEncodedLength]],  # value
                               _type.HRESULT]
    SendMessageAndGetResultAsync: _Callable[[ISmsMessageBase,  # message
                                             _Pointer[_Windows_Foundation.IAsyncOperation[ISmsSendMessageResult]]],  # asyncInfo
                                            _type.HRESULT]
    add_DeviceStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISmsDevice2, _inspectable.IInspectable],  # eventHandler
                                        _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                       _type.HRESULT]
    remove_DeviceStatusChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                          _type.HRESULT]


class ISmsDevice2Statics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FromId: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[ISmsDevice2]],  # value
                      _type.HRESULT]
    GetDefault: _Callable[[_Pointer[ISmsDevice2]],  # value
                          _type.HRESULT]
    FromParentId: _Callable[[_type.HSTRING,  # parentDeviceId
                             _Pointer[ISmsDevice2]],  # value
                            _type.HRESULT]


class ISmsDeviceMessageStore(_inspectable.IInspectable):
    DeleteMessageAsync: _Callable[[_type.UINT32,  # messageId
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                  _type.HRESULT]
    DeleteMessagesAsync: _Callable[[_enum.Windows.Devices.Sms.SmsMessageFilter,  # messageFilter
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                   _type.HRESULT]
    GetMessageAsync: _Callable[[_type.UINT32,  # messageId
                                _Pointer[_Windows_Foundation.IAsyncOperation[ISmsMessage]]],  # asyncInfo
                               _type.HRESULT]
    GetMessagesAsync: _Callable[[_enum.Windows.Devices.Sms.SmsMessageFilter,  # messageFilter
                                 _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_Windows_Foundation_Collections.IVectorView[ISmsMessage], _type.INT32]]],  # asyncInfo
                                _type.HRESULT]
    MaxMessages: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]


class ISmsDeviceStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # phstrDeviceClassSelector
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ISmsDevice]]],  # asyncInfo
                           _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISmsDevice]]],  # asyncInfo
                               _type.HRESULT]


class ISmsDeviceStatics2(_inspectable.IInspectable, factory=True):
    FromNetworkAccountIdAsync: _Callable[[_type.HSTRING,  # networkAccountId
                                          _Pointer[_Windows_Foundation.IAsyncOperation[ISmsDevice]]],  # asyncInfo
                                         _type.HRESULT]


class ISmsFilterRule(_inspectable.IInspectable):
    get_MessageType: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsMessageType]],  # value
                               _type.HRESULT]
    get_ImsiPrefixes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                _type.HRESULT]
    get_DeviceIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_SenderNumbers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                 _type.HRESULT]
    get_TextMessagePrefixes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                       _type.HRESULT]
    get_PortNumbers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.INT32]]],  # value
                               _type.HRESULT]
    get_CellularClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.CellularClass]],  # value
                                 _type.HRESULT]
    put_CellularClass: _Callable[[_enum.Windows.Devices.Sms.CellularClass],  # value
                                 _type.HRESULT]
    get_ProtocolIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.INT32]]],  # value
                               _type.HRESULT]
    get_TeleserviceIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.INT32]]],  # value
                                  _type.HRESULT]
    get_WapApplicationIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    get_WapContentTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                   _type.HRESULT]
    get_BroadcastTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.Sms.SmsBroadcastType]]],  # value
                                  _type.HRESULT]
    get_BroadcastChannels: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.INT32]]],  # value
                                     _type.HRESULT]


class ISmsFilterRuleFactory(_inspectable.IInspectable, factory=True):
    CreateFilterRule: _Callable[[_enum.Windows.Devices.Sms.SmsMessageType,  # messageType
                                 _Pointer[ISmsFilterRule]],  # value
                                _type.HRESULT]


class ISmsFilterRules(_inspectable.IInspectable):
    get_ActionType: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsFilterActionType]],  # value
                              _type.HRESULT]
    get_Rules: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISmsFilterRule]]],  # value
                         _type.HRESULT]


class ISmsFilterRulesFactory(_inspectable.IInspectable, factory=True):
    CreateFilterRules: _Callable[[_enum.Windows.Devices.Sms.SmsFilterActionType,  # actionType
                                  _Pointer[ISmsFilterRules]],  # value
                                 _type.HRESULT]


class ISmsMessage(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_MessageClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsMessageClass]],  # value
                                _type.HRESULT]


class ISmsMessageBase(_inspectable.IInspectable):
    get_MessageType: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsMessageType]],  # value
                               _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_CellularClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.CellularClass]],  # value
                                 _type.HRESULT]
    get_MessageClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsMessageClass]],  # value
                                _type.HRESULT]
    get_SimIccId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ISmsMessageReceivedEventArgs(_inspectable.IInspectable):
    TextMessage: _Callable[[_Pointer[ISmsTextMessage]],  # value
                           _type.HRESULT]
    BinaryMessage: _Callable[[_Pointer[ISmsBinaryMessage]],  # value
                             _type.HRESULT]


class ISmsMessageReceivedTriggerDetails(_inspectable.IInspectable):
    get_MessageType: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsMessageType]],  # value
                               _type.HRESULT]
    get_TextMessage: _Callable[[_Pointer[ISmsTextMessage2]],  # value
                               _type.HRESULT]
    get_WapMessage: _Callable[[_Pointer[ISmsWapMessage]],  # value
                              _type.HRESULT]
    get_AppMessage: _Callable[[_Pointer[ISmsAppMessage]],  # value
                              _type.HRESULT]
    get_BroadcastMessage: _Callable[[_Pointer[ISmsBroadcastMessage]],  # value
                                    _type.HRESULT]
    get_VoicemailMessage: _Callable[[_Pointer[ISmsVoicemailMessage]],  # value
                                    _type.HRESULT]
    get_StatusMessage: _Callable[[_Pointer[ISmsStatusMessage]],  # value
                                 _type.HRESULT]
    Drop: _Callable[[],
                    _type.HRESULT]
    Accept: _Callable[[],
                      _type.HRESULT]


class ISmsMessageRegistration(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    Unregister: _Callable[[],
                          _type.HRESULT]
    add_MessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ISmsMessageRegistration, ISmsMessageReceivedTriggerDetails],  # eventHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                   _type.HRESULT]
    remove_MessageReceived: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                      _type.HRESULT]


class ISmsMessageRegistrationStatics(_inspectable.IInspectable, factory=True):
    get_AllRegistrations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ISmsMessageRegistration]]],  # value
                                    _type.HRESULT]
    Register: _Callable[[_type.HSTRING,  # id
                         ISmsFilterRules,  # filterRules
                         _Pointer[ISmsMessageRegistration]],  # value
                        _type.HRESULT]


class ISmsReceivedEventDetails(_inspectable.IInspectable):
    DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    MessageIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class ISmsReceivedEventDetails2(_inspectable.IInspectable):
    MessageClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsMessageClass]],  # value
                            _type.HRESULT]
    BinaryMessage: _Callable[[_Pointer[ISmsBinaryMessage]],  # value
                             _type.HRESULT]


class ISmsSendMessageResult(_inspectable.IInspectable):
    get_IsSuccessful: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_MessageReferenceNumbers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT32]]],  # value
                                           _type.HRESULT]
    get_CellularClass: _Callable[[_Pointer[_enum.Windows.Devices.Sms.CellularClass]],  # value
                                 _type.HRESULT]
    get_ModemErrorCode: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsModemErrorCode]],  # value
                                  _type.HRESULT]
    get_IsErrorTransient: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_NetworkCauseCode: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_TransportFailureCause: _Callable[[_Pointer[_type.INT32]],  # value
                                         _type.HRESULT]


class ISmsStatusMessage(_inspectable.IInspectable):
    get_To: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_From: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Status: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_MessageReferenceNumber: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    get_ServiceCenterTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                          _type.HRESULT]
    get_DischargeTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                 _type.HRESULT]


class ISmsTextMessage(_inspectable.IInspectable):
    Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                         _type.HRESULT]
    PartReferenceId: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    PartNumber: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    PartCount: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    To: _Callable[[_type.HSTRING],  # value
                  _type.HRESULT]
    From: _Callable[[_type.HSTRING],  # value
                    _type.HRESULT]
    Body: _Callable[[_type.HSTRING],  # value
                    _type.HRESULT]
    Encoding: _Callable[[_enum.Windows.Devices.Sms.SmsEncoding],  # value
                        _type.HRESULT]
    ToBinaryMessages: _Callable[[_enum.Windows.Devices.Sms.SmsDataFormat,  # format
                                 _Pointer[_Windows_Foundation_Collections.IVectorView[ISmsBinaryMessage]]],  # messages
                                _type.HRESULT]


class ISmsTextMessage2(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_To: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_To: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_From: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Body: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Encoding: _Callable[[_Pointer[_enum.Windows.Devices.Sms.SmsEncoding]],  # value
                            _type.HRESULT]
    put_Encoding: _Callable[[_enum.Windows.Devices.Sms.SmsEncoding],  # value
                            _type.HRESULT]
    get_CallbackNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_CallbackNumber: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_IsDeliveryNotificationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsDeliveryNotificationEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_RetryAttemptCount: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    put_RetryAttemptCount: _Callable[[_type.INT32],  # value
                                     _type.HRESULT]
    get_TeleserviceId: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    get_ProtocolId: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]


class ISmsTextMessageStatics(_inspectable.IInspectable, factory=True):
    FromBinaryMessage: _Callable[[ISmsBinaryMessage,  # binaryMessage
                                  _Pointer[ISmsTextMessage]],  # textMessage
                                 _type.HRESULT]
    FromBinaryData: _Callable[[_enum.Windows.Devices.Sms.SmsDataFormat,  # format
                               _type.UINT32,  # __valueSize
                               _Pointer[_type.BYTE],  # value
                               _Pointer[ISmsTextMessage]],  # textMessage
                              _type.HRESULT]


class ISmsVoicemailMessage(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_To: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_MessageCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                _type.HRESULT]


class ISmsWapMessage(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_To: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_From: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_ApplicationId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_BinaryBody: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                              _type.HRESULT]
    get_Headers: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                           _type.HRESULT]
