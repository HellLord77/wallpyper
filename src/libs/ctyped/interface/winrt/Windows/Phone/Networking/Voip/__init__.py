from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICallAnswerEventArgs(_inspectable.IInspectable):
    get_AcceptedMedia: _Callable[[_Pointer[_enum.Windows.Phone.Networking.Voip.VoipCallMedia]],  # value
                                 _type.HRESULT]


class ICallRejectEventArgs(_inspectable.IInspectable):
    get_RejectReason: _Callable[[_Pointer[_enum.Windows.Phone.Networking.Voip.VoipCallRejectReason]],  # value
                                _type.HRESULT]


class ICallStateChangeEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Phone.Networking.Voip.VoipCallState]],  # value
                         _type.HRESULT]


class IMuteChangeEventArgs(_inspectable.IInspectable):
    get_Muted: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]


class IQuerySeamlessUpgradeSupportOperation(_inspectable.IInspectable):
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    NotifyCompletion: _Callable[[_type.boolean,  # succeeded
                                 _enum.Windows.Phone.Networking.Voip.SeamlessCallUpgradeSupport],  # seamlessCallUpgradeSupport
                                _type.HRESULT]


class IVoipCallCoordinator(_inspectable.IInspectable):
    add_MuteRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipCallCoordinator, IMuteChangeEventArgs],  # muteChangeHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_MuteRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_UnmuteRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoipCallCoordinator, IMuteChangeEventArgs],  # muteChangeHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_UnmuteRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    RequestNewIncomingCall: _Callable[[_type.HSTRING,  # context
                                       _type.HSTRING,  # contactName
                                       _type.HSTRING,  # contactNumber
                                       _Windows_Foundation.IUriRuntimeClass,  # contactImage
                                       _type.HSTRING,  # serviceName
                                       _Windows_Foundation.IUriRuntimeClass,  # brandingImage
                                       _type.HSTRING,  # callDetails
                                       _Windows_Foundation.IUriRuntimeClass,  # ringtone
                                       _enum.Windows.Phone.Networking.Voip.VoipCallMedia,  # media
                                       _struct.Windows.Foundation.TimeSpan,  # ringTimeout
                                       _Pointer[IVoipPhoneCall]],  # call
                                      _type.HRESULT]
    RequestNewOutgoingCall: _Callable[[_type.HSTRING,  # context
                                       _type.HSTRING,  # contactName
                                       _type.HSTRING,  # serviceName
                                       _enum.Windows.Phone.Networking.Voip.VoipCallMedia,  # media
                                       _Pointer[IVoipPhoneCall]],  # call
                                      _type.HRESULT]
    NotifyMuted: _Callable[[],
                           _type.HRESULT]
    NotifyUnmuted: _Callable[[],
                             _type.HRESULT]


class IVoipCallCoordinator2(_inspectable.IInspectable):
    SetupNewAcceptedCall: _Callable[[_type.HSTRING,  # context
                                     _type.HSTRING,  # contactName
                                     _type.HSTRING,  # contactNumber
                                     _type.HSTRING,  # serviceName
                                     _enum.Windows.Phone.Networking.Voip.VoipCallMedia,  # media
                                     _Pointer[IVoipPhoneCall]],  # call
                                    _type.HRESULT]


class IVoipCallCoordinator3(_inspectable.IInspectable):
    RequestNewIncomingCallWithContactRemoteId: _Callable[[_type.HSTRING,  # context
                                                          _type.HSTRING,  # contactName
                                                          _type.HSTRING,  # contactNumber
                                                          _Windows_Foundation.IUriRuntimeClass,  # contactImage
                                                          _type.HSTRING,  # serviceName
                                                          _Windows_Foundation.IUriRuntimeClass,  # brandingImage
                                                          _type.HSTRING,  # callDetails
                                                          _Windows_Foundation.IUriRuntimeClass,  # ringtone
                                                          _enum.Windows.Phone.Networking.Voip.VoipCallMedia,  # media
                                                          _struct.Windows.Foundation.TimeSpan,  # ringTimeout
                                                          _type.HSTRING,  # contactRemoteId
                                                          _Pointer[IVoipPhoneCall]],  # call
                                                         _type.HRESULT]
    RequestNewAppInitiatedCall: _Callable[[_type.HSTRING,  # context
                                           _type.HSTRING,  # contactName
                                           _type.HSTRING,  # contactNumber
                                           _type.HSTRING,  # serviceName
                                           _enum.Windows.Phone.Networking.Voip.VoipCallMedia,  # media
                                           _Pointer[IVoipPhoneCall]],  # call
                                          _type.HRESULT]


class IVoipCallCoordinatorStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IVoipCallCoordinator]],  # coordinator
                          _type.HRESULT]


class IVoipCallCoordinatorWithAppDeterminedUpgrade(_inspectable.IInspectable):
    ConfirmNonSeamlessUpgrade: _Callable[[_struct.GUID],  # callUpgradeGuid
                                         _type.HRESULT]
    CancelUpgrade: _Callable[[_struct.GUID],  # callUpgradeGuid
                             _type.HRESULT]


class IVoipCallCoordinatorWithUpgrade(_inspectable.IInspectable):
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


class IVoipOperation(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # operationId
                      _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Phone.Networking.Voip.VoipOperationType]],  # operationType
                        _type.HRESULT]


class IVoipOperationsManager(_inspectable.IInspectable):
    GetNextOperation: _Callable[[_Pointer[IVoipOperation]],  # voipOperation
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
    get_CallMedia: _Callable[[_Pointer[_enum.Windows.Phone.Networking.Voip.VoipCallMedia]],  # value
                             _type.HRESULT]
    put_CallMedia: _Callable[[_enum.Windows.Phone.Networking.Voip.VoipCallMedia],  # value
                             _type.HRESULT]


class IVoipPhoneCall2(_inspectable.IInspectable):
    TryShowAppUI: _Callable[[],
                            _type.HRESULT]


class IVoipPhoneCall3(_inspectable.IInspectable):
    NotifyCallAccepted: _Callable[[_enum.Windows.Phone.Networking.Voip.VoipCallMedia],  # media
                                  _type.HRESULT]


class IVoipPhoneCallReady(_inspectable.IInspectable):
    NotifyCallReady: _Callable[[],
                               _type.HRESULT]
