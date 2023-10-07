from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Contacts as _Windows_ApplicationModel_Contacts
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ICallAnswerEventArgs(_inspectable.IInspectable):
    get_AcceptedMedia: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia]],  # value
                                 _type.HRESULT]


class ICallRejectEventArgs(_inspectable.IInspectable):
    get_RejectReason: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallRejectReason]],  # value
                                _type.HRESULT]


class ICallStateChangeEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallState]],  # value
                         _type.HRESULT]


class ILockScreenCallEndCallDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class ILockScreenCallEndRequestedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[ILockScreenCallEndCallDeferral]],  # value
                           _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]


class ILockScreenCallUI(_inspectable.IInspectable):
    Dismiss: _Callable[[],
                       _type.HRESULT]
    add_EndRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ILockScreenCallUI, ILockScreenCallEndRequestedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_EndRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[ILockScreenCallUI, _inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    get_CallTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_CallTitle: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class IMuteChangeEventArgs(_inspectable.IInspectable):
    get_Muted: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]


class IPhoneCall(_inspectable.IInspectable):
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneCall, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_AudioDeviceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneCall, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_AudioDeviceChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_IsMutedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneCall, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_IsMutedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    get_CallId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_IsMuted: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallStatus]],  # value
                          _type.HRESULT]
    get_AudioDevice: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallAudioDevice]],  # value
                               _type.HRESULT]
    GetPhoneCallInfo: _Callable[[_Pointer[IPhoneCallInfo]],  # result
                                _type.HRESULT]
    GetPhoneCallInfoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPhoneCallInfo]]],  # operation
                                     _type.HRESULT]
    End: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                   _type.HRESULT]
    EndAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                        _type.HRESULT]
    SendDtmfKey: _Callable[[_enum.Windows.ApplicationModel.Calls.DtmfKey,  # key
                            _enum.Windows.ApplicationModel.Calls.DtmfToneAudioPlayback,  # dtmfToneAudioPlayback
                            _Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                           _type.HRESULT]
    SendDtmfKeyAsync: _Callable[[_enum.Windows.ApplicationModel.Calls.DtmfKey,  # key
                                 _enum.Windows.ApplicationModel.Calls.DtmfToneAudioPlayback,  # dtmfToneAudioPlayback
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                                _type.HRESULT]
    AcceptIncoming: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                              _type.HRESULT]
    AcceptIncomingAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                                   _type.HRESULT]
    Hold: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                    _type.HRESULT]
    HoldAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                         _type.HRESULT]
    ResumeFromHold: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                              _type.HRESULT]
    ResumeFromHoldAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                                   _type.HRESULT]
    Mute: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                    _type.HRESULT]
    MuteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                         _type.HRESULT]
    Unmute: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                      _type.HRESULT]
    UnmuteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                           _type.HRESULT]
    RejectIncoming: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                              _type.HRESULT]
    RejectIncomingAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                                   _type.HRESULT]
    ChangeAudioDevice: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallAudioDevice,  # endpoint
                                  _Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # result
                                 _type.HRESULT]
    ChangeAudioDeviceAsync: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallAudioDevice,  # endpoint
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]]],  # operation
                                      _type.HRESULT]


class IPhoneCallBlockingStatics(_inspectable.IInspectable, factory=True):
    get_BlockUnknownNumbers: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_BlockUnknownNumbers: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_BlockPrivateNumbers: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_BlockPrivateNumbers: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    SetCallBlockingListAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # phoneNumberList
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                        _type.HRESULT]


class IPhoneCallHistoryEntry(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Address: _Callable[[_Pointer[IPhoneCallHistoryEntryAddress]],  # value
                           _type.HRESULT]
    put_Address: _Callable[[IPhoneCallHistoryEntryAddress],  # value
                           _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_IsCallerIdBlocked: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsCallerIdBlocked: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IsEmergency: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsEmergency: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_IsIncoming: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsIncoming: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_IsMissed: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsMissed: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_IsRinging: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsRinging: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_IsSeen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_IsSeen: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsSuppressed: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsSuppressed: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_IsVoicemail: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsVoicemail: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_Media: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryMedia]],  # value
                         _type.HRESULT]
    put_Media: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryMedia],  # value
                         _type.HRESULT]
    get_OtherAppReadAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryOtherAppReadAccess]],  # value
                                      _type.HRESULT]
    put_OtherAppReadAccess: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryOtherAppReadAccess],  # value
                                      _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_SourceDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_SourceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_SourceId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_SourceIdKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallHistorySourceIdKind]],  # value
                                _type.HRESULT]
    put_SourceIdKind: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallHistorySourceIdKind],  # value
                                _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                             _type.HRESULT]


class IPhoneCallHistoryEntryAddress(_inspectable.IInspectable):
    get_ContactId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_ContactId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_RawAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_RawAddress: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_RawAddressKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind]],  # value
                                  _type.HRESULT]
    put_RawAddressKind: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind],  # value
                                  _type.HRESULT]


class IPhoneCallHistoryEntryAddressFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # rawAddress
                       _enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryRawAddressKind,  # rawAddressKind
                       _Pointer[IPhoneCallHistoryEntryAddress]],  # result
                      _type.HRESULT]


class IPhoneCallHistoryEntryQueryOptions(_inspectable.IInspectable):
    get_DesiredMedia: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryDesiredMedia]],  # value
                                _type.HRESULT]
    put_DesiredMedia: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryEntryQueryDesiredMedia],  # value
                                _type.HRESULT]
    get_SourceIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]


class IPhoneCallHistoryEntryReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPhoneCallHistoryEntry]]]],  # result
                              _type.HRESULT]


class IPhoneCallHistoryManagerForUser(_inspectable.IInspectable):
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryStoreAccessType,  # accessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IPhoneCallHistoryStore]]],  # result
                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IPhoneCallHistoryManagerStatics(_inspectable.IInspectable, factory=True):
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallHistoryStoreAccessType,  # accessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IPhoneCallHistoryStore]]],  # result
                                 _type.HRESULT]


class IPhoneCallHistoryManagerStatics2(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IPhoneCallHistoryManagerForUser]],  # result
                          _type.HRESULT]


class IPhoneCallHistoryStore(_inspectable.IInspectable):
    GetEntryAsync: _Callable[[_type.HSTRING,  # callHistoryEntryId
                              _Pointer[_Windows_Foundation.IAsyncOperation[IPhoneCallHistoryEntry]]],  # result
                             _type.HRESULT]
    GetEntryReader: _Callable[[_Pointer[IPhoneCallHistoryEntryReader]],  # result
                              _type.HRESULT]
    GetEntryReaderWithOptions: _Callable[[IPhoneCallHistoryEntryQueryOptions,  # queryOptions
                                          _Pointer[IPhoneCallHistoryEntryReader]],  # result
                                         _type.HRESULT]
    SaveEntryAsync: _Callable[[IPhoneCallHistoryEntry,  # callHistoryEntry
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                              _type.HRESULT]
    DeleteEntryAsync: _Callable[[IPhoneCallHistoryEntry,  # callHistoryEntry
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                _type.HRESULT]
    DeleteEntriesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IPhoneCallHistoryEntry],  # callHistoryEntries
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                  _type.HRESULT]
    MarkEntryAsSeenAsync: _Callable[[IPhoneCallHistoryEntry,  # callHistoryEntry
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    MarkEntriesAsSeenAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IPhoneCallHistoryEntry],  # callHistoryEntries
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                      _type.HRESULT]
    GetUnseenCountAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # result
                                   _type.HRESULT]
    MarkAllAsSeenAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                  _type.HRESULT]
    GetSourcesUnseenCountAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # sourceIds
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # result
                                          _type.HRESULT]
    MarkSourcesAsSeenAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # sourceIds
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                      _type.HRESULT]


class IPhoneCallInfo(_inspectable.IInspectable):
    get_LineId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_IsHoldSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_CallDirection: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallDirection]],  # value
                                 _type.HRESULT]


class IPhoneCallManagerStatics(_inspectable.IInspectable, factory=True):
    ShowPhoneCallUI: _Callable[[_type.HSTRING,  # phoneNumber
                                _type.HSTRING],  # displayName
                               _type.HRESULT]


class IPhoneCallManagerStatics2(_inspectable.IInspectable, factory=True):
    add_CallStateChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_CallStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    get_IsCallActive: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_IsCallIncoming: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    ShowPhoneCallSettingsUI: _Callable[[],
                                       _type.HRESULT]
    RequestStoreAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPhoneCallStore]]],  # result
                                 _type.HRESULT]


class IPhoneCallStatics(_inspectable.IInspectable, factory=True):
    GetFromId: _Callable[[_type.HSTRING,  # callId
                          _Pointer[IPhoneCall]],  # result
                         _type.HRESULT]


class IPhoneCallStore(_inspectable.IInspectable):
    IsEmergencyPhoneNumberAsync: _Callable[[_type.HSTRING,  # number
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                           _type.HRESULT]
    GetDefaultLineAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_struct.GUID]]],  # result
                                   _type.HRESULT]
    RequestLineWatcher: _Callable[[_Pointer[IPhoneLineWatcher]],  # result
                                  _type.HRESULT]


class IPhoneCallVideoCapabilities(_inspectable.IInspectable):
    get_IsVideoCallingCapable: _Callable[[_Pointer[_type.boolean]],  # pValue
                                         _type.HRESULT]


class IPhoneCallVideoCapabilitiesManagerStatics(_inspectable.IInspectable, factory=True):
    GetCapabilitiesAsync: _Callable[[_type.HSTRING,  # phoneNumber
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IPhoneCallVideoCapabilities]]],  # result
                                    _type.HRESULT]


class IPhoneCallsResult(_inspectable.IInspectable):
    get_OperationStatus: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneLineOperationStatus]],  # value
                                   _type.HRESULT]
    get_AllActivePhoneCalls: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPhoneCall]]],  # value
                                       _type.HRESULT]


class IPhoneDialOptions(_inspectable.IInspectable):
    get_Number: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Number: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]
    put_Contact: _Callable[[_Windows_ApplicationModel_Contacts.IContact],  # value
                           _type.HRESULT]
    get_ContactPhone: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContactPhone]],  # value
                                _type.HRESULT]
    put_ContactPhone: _Callable[[_Windows_ApplicationModel_Contacts.IContactPhone],  # value
                                _type.HRESULT]
    get_Media: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallMedia]],  # value
                         _type.HRESULT]
    put_Media: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneCallMedia],  # value
                         _type.HRESULT]
    get_AudioEndpoint: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneAudioRoutingEndpoint]],  # value
                                 _type.HRESULT]
    put_AudioEndpoint: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneAudioRoutingEndpoint],  # value
                                 _type.HRESULT]


class IPhoneLine(_inspectable.IInspectable):
    add_LineChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLine, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_LineChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]
    get_DisplayColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_NetworkState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneNetworkState]],  # value
                                _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Voicemail: _Callable[[_Pointer[IPhoneVoicemail]],  # value
                             _type.HRESULT]
    get_NetworkName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_CellularDetails: _Callable[[_Pointer[IPhoneLineCellularDetails]],  # value
                                   _type.HRESULT]
    get_Transport: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneLineTransport]],  # value
                             _type.HRESULT]
    get_CanDial: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_SupportsTile: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_VideoCallingCapabilities: _Callable[[_Pointer[IPhoneCallVideoCapabilities]],  # value
                                            _type.HRESULT]
    get_LineConfiguration: _Callable[[_Pointer[IPhoneLineConfiguration]],  # value
                                     _type.HRESULT]
    IsImmediateDialNumberAsync: _Callable[[_type.HSTRING,  # number
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                          _type.HRESULT]
    Dial: _Callable[[_type.HSTRING,  # number
                     _type.HSTRING],  # displayName
                    _type.HRESULT]
    DialWithOptions: _Callable[[IPhoneDialOptions],  # options
                               _type.HRESULT]


class IPhoneLine2(_inspectable.IInspectable):
    EnableTextReply: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_TransportDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IPhoneLine3(_inspectable.IInspectable):
    DialWithResult: _Callable[[_type.HSTRING,  # number
                               _type.HSTRING,  # displayName
                               _Pointer[IPhoneLineDialResult]],  # result
                              _type.HRESULT]
    DialWithResultAsync: _Callable[[_type.HSTRING,  # number
                                    _type.HSTRING,  # displayName
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IPhoneLineDialResult]]],  # operation
                                   _type.HRESULT]
    GetAllActivePhoneCalls: _Callable[[_Pointer[IPhoneCallsResult]],  # result
                                      _type.HRESULT]
    GetAllActivePhoneCallsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPhoneCallsResult]]],  # operation
                                           _type.HRESULT]


class IPhoneLineCellularDetails(_inspectable.IInspectable):
    get_SimState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneSimState]],  # value
                            _type.HRESULT]
    get_SimSlotIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_IsModemOn: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_RegistrationRejectCode: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    GetNetworkOperatorDisplayText: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneLineNetworkOperatorDisplayTextLocation,  # location
                                              _Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]


class IPhoneLineConfiguration(_inspectable.IInspectable):
    get_IsVideoCallingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_ExtendedProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                                      _type.HRESULT]


class IPhoneLineDialResult(_inspectable.IInspectable):
    get_DialCallStatus: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneCallOperationStatus]],  # value
                                  _type.HRESULT]
    get_DialedCall: _Callable[[_Pointer[IPhoneCall]],  # value
                              _type.HRESULT]


class IPhoneLineStatics(_inspectable.IInspectable, factory=True):
    FromIdAsync: _Callable[[_struct.GUID,  # lineId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IPhoneLine]]],  # result
                           _type.HRESULT]


class IPhoneLineTransportDevice(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Transport: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneLineTransport]],  # value
                             _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Enumeration.DeviceAccessStatus]]],  # operation
                                  _type.HRESULT]
    RegisterApp: _Callable[[],
                           _type.HRESULT]
    RegisterAppForUser: _Callable[[_Windows_System.IUser],  # user
                                  _type.HRESULT]
    UnregisterApp: _Callable[[],
                             _type.HRESULT]
    UnregisterAppForUser: _Callable[[_Windows_System.IUser],  # user
                                    _type.HRESULT]
    IsRegistered: _Callable[[_Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    Connect: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    ConnectAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                            _type.HRESULT]


class IPhoneLineTransportDevice2(_inspectable.IInspectable):
    get_AudioRoutingStatus: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.TransportDeviceAudioRoutingStatus]],  # value
                                      _type.HRESULT]
    add_AudioRoutingStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLineTransportDevice, _inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_AudioRoutingStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    get_InBandRingingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    add_InBandRingingEnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLineTransportDevice, _inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_InBandRingingEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IPhoneLineTransportDeviceStatics(_inspectable.IInspectable, factory=True):
    FromId: _Callable[[_type.HSTRING,  # id
                       _Pointer[IPhoneLineTransportDevice]],  # result
                      _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    GetDeviceSelectorForPhoneLineTransport: _Callable[[_enum.Windows.ApplicationModel.Calls.PhoneLineTransport,  # transport
                                                       _Pointer[_type.HSTRING]],  # result
                                                      _type.HRESULT]


class IPhoneLineWatcher(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_LineAdded: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLineWatcher, IPhoneLineWatcherEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LineAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_LineRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLineWatcher, IPhoneLineWatcherEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_LineRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_LineUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLineWatcher, IPhoneLineWatcherEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_LineUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLineWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IPhoneLineWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneLineWatcherStatus]],  # status
                          _type.HRESULT]


class IPhoneLineWatcherEventArgs(_inspectable.IInspectable):
    get_LineId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]


class IPhoneVoicemail(_inspectable.IInspectable):
    get_Number: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_MessageCount: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.PhoneVoicemailType]],  # value
                        _type.HRESULT]
    DialVoicemailAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                  _type.HRESULT]


class IVoipCallCoordinator(_inspectable.IInspectable):
    ReserveCallResourcesAsync: _Callable[[_type.HSTRING,  # taskEntryPoint
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallResourceReservationStatus]]],  # operation
                                         _type.HRESULT]
    add_MuteStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipCallCoordinator, IMuteChangeEventArgs],  # muteChangeHandler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_MuteStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    RequestNewIncomingCall: _Callable[[_type.HSTRING,  # context
                                       _type.HSTRING,  # contactName
                                       _type.HSTRING,  # contactNumber
                                       _Windows_Foundation.IUriRuntimeClass,  # contactImage
                                       _type.HSTRING,  # serviceName
                                       _Windows_Foundation.IUriRuntimeClass,  # brandingImage
                                       _type.HSTRING,  # callDetails
                                       _Windows_Foundation.IUriRuntimeClass,  # ringtone
                                       _enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia,  # media
                                       _struct.Windows.Foundation.TimeSpan,  # ringTimeout
                                       _Pointer[IVoipPhoneCall]],  # call
                                      _type.HRESULT]
    RequestNewOutgoingCall: _Callable[[_type.HSTRING,  # context
                                       _type.HSTRING,  # contactName
                                       _type.HSTRING,  # serviceName
                                       _enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia,  # media
                                       _Pointer[IVoipPhoneCall]],  # call
                                      _type.HRESULT]
    NotifyMuted: _Callable[[],
                           _type.HRESULT]
    NotifyUnmuted: _Callable[[],
                             _type.HRESULT]
    RequestOutgoingUpgradeToVideoCall: _Callable[[_struct.GUID,  # callUpgradeGuid
                                                  _type.HSTRING,  # context
                                                  _type.HSTRING,  # contactName
                                                  _type.HSTRING,  # serviceName
                                                  _Pointer[IVoipPhoneCall]],  # call
                                                 _type.HRESULT]
    RequestIncomingUpgradeToVideoCall: _Callable[[_type.HSTRING,  # context
                                                  _type.HSTRING,  # contactName
                                                  _type.HSTRING,  # contactNumber
                                                  _Windows_Foundation.IUriRuntimeClass,  # contactImage
                                                  _type.HSTRING,  # serviceName
                                                  _Windows_Foundation.IUriRuntimeClass,  # brandingImage
                                                  _type.HSTRING,  # callDetails
                                                  _Windows_Foundation.IUriRuntimeClass,  # ringtone
                                                  _struct.Windows.Foundation.TimeSpan,  # ringTimeout
                                                  _Pointer[IVoipPhoneCall]],  # call
                                                 _type.HRESULT]
    TerminateCellularCall: _Callable[[_struct.GUID],  # callUpgradeGuid
                                     _type.HRESULT]
    CancelUpgrade: _Callable[[_struct.GUID],  # callUpgradeGuid
                             _type.HRESULT]


class IVoipCallCoordinator2(_inspectable.IInspectable):
    SetupNewAcceptedCall: _Callable[[_type.HSTRING,  # context
                                     _type.HSTRING,  # contactName
                                     _type.HSTRING,  # contactNumber
                                     _type.HSTRING,  # serviceName
                                     _enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia,  # media
                                     _Pointer[IVoipPhoneCall]],  # call
                                    _type.HRESULT]


class IVoipCallCoordinator3(_inspectable.IInspectable):
    RequestNewAppInitiatedCall: _Callable[[_type.HSTRING,  # context
                                           _type.HSTRING,  # contactName
                                           _type.HSTRING,  # contactNumber
                                           _type.HSTRING,  # serviceName
                                           _enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia,  # media
                                           _Pointer[IVoipPhoneCall]],  # call
                                          _type.HRESULT]
    RequestNewIncomingCallWithContactRemoteId: _Callable[[_type.HSTRING,  # context
                                                          _type.HSTRING,  # contactName
                                                          _type.HSTRING,  # contactNumber
                                                          _Windows_Foundation.IUriRuntimeClass,  # contactImage
                                                          _type.HSTRING,  # serviceName
                                                          _Windows_Foundation.IUriRuntimeClass,  # brandingImage
                                                          _type.HSTRING,  # callDetails
                                                          _Windows_Foundation.IUriRuntimeClass,  # ringtone
                                                          _enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia,  # media
                                                          _struct.Windows.Foundation.TimeSpan,  # ringTimeout
                                                          _type.HSTRING,  # contactRemoteId
                                                          _Pointer[IVoipPhoneCall]],  # call
                                                         _type.HRESULT]


class IVoipCallCoordinator4(_inspectable.IInspectable):
    ReserveOneProcessCallResourcesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallResourceReservationStatus]]],  # operation
                                                   _type.HRESULT]


class IVoipCallCoordinatorStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IVoipCallCoordinator]],  # coordinator
                          _type.HRESULT]


class IVoipPhoneCall(_inspectable.IInspectable):
    add_EndRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipPhoneCall, ICallStateChangeEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_EndRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_HoldRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipPhoneCall, ICallStateChangeEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_HoldRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_ResumeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipPhoneCall, ICallStateChangeEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ResumeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_AnswerRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipPhoneCall, ICallAnswerEventArgs],  # acceptHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_AnswerRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_RejectRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipPhoneCall, ICallRejectEventArgs],  # rejectHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_RejectRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    NotifyCallHeld: _Callable[[],
                              _type.HRESULT]
    NotifyCallActive: _Callable[[],
                                _type.HRESULT]
    NotifyCallEnded: _Callable[[],
                               _type.HRESULT]
    get_ContactName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ContactName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                             _type.HRESULT]
    get_CallMedia: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia]],  # value
                             _type.HRESULT]
    put_CallMedia: _Callable[[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia],  # value
                             _type.HRESULT]
    NotifyCallReady: _Callable[[],
                               _type.HRESULT]


class IVoipPhoneCall2(_inspectable.IInspectable):
    TryShowAppUI: _Callable[[],
                            _type.HRESULT]


class IVoipPhoneCall3(_inspectable.IInspectable):
    NotifyCallAccepted: _Callable[[_enum.Windows.ApplicationModel.Calls.VoipPhoneCallMedia],  # media
                                  _type.HRESULT]
