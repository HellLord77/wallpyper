from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ... import System as _Windows_System
from ...ApplicationModel import AppService as _Windows_ApplicationModel_AppService
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IKnownRemoteSystemCapabilitiesStatics(_inspectable.IInspectable, factory=True):
    get_AppService: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_LaunchUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_RemoteSession: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_SpatialEntity: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IRemoteSystem(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemStatus]],  # value
                          _type.HRESULT]
    get_IsAvailableByProximity: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IRemoteSystem2(_inspectable.IInspectable):
    get_IsAvailableBySpatialProximity: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    GetCapabilitySupportedAsync: _Callable[[_type.HSTRING,  # capabilityName
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]


class IRemoteSystem3(_inspectable.IInspectable):
    get_ManufacturerDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    get_ModelDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IRemoteSystem4(_inspectable.IInspectable):
    get_Platform: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemPlatform]],  # value
                            _type.HRESULT]


class IRemoteSystem5(_inspectable.IInspectable):
    get_Apps: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IRemoteSystemApp]]],  # value
                        _type.HRESULT]


class IRemoteSystem6(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IRemoteSystemAddedEventArgs(_inspectable.IInspectable):
    get_RemoteSystem: _Callable[[_Pointer[IRemoteSystem]],  # value
                                _type.HRESULT]


class IRemoteSystemApp(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsAvailableByProximity: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_IsAvailableBySpatialProximity: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    get_Attributes: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                              _type.HRESULT]


class IRemoteSystemApp2(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    get_ConnectionToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IRemoteSystemAppRegistration(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    get_Attributes: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                              _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                         _type.HRESULT]


class IRemoteSystemAppRegistrationStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IRemoteSystemAppRegistration]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IRemoteSystemAppRegistration]],  # result
                          _type.HRESULT]


class IRemoteSystemAuthorizationKindFilter(_inspectable.IInspectable):
    get_RemoteSystemAuthorizationKind: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind]],  # value
                                                 _type.HRESULT]


class IRemoteSystemAuthorizationKindFilterFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind,  # remoteSystemAuthorizationKind
                       _Pointer[IRemoteSystemAuthorizationKindFilter]],  # value
                      _type.HRESULT]


class IRemoteSystemConnectionInfo(_inspectable.IInspectable):
    get_IsProximal: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IRemoteSystemConnectionInfoStatics(_inspectable.IInspectable, factory=True):
    TryCreateFromAppServiceConnection: _Callable[[_Windows_ApplicationModel_AppService.IAppServiceConnection,  # connection
                                                  _Pointer[IRemoteSystemConnectionInfo]],  # result
                                                 _type.HRESULT]


class IRemoteSystemConnectionRequest(_inspectable.IInspectable):
    get_RemoteSystem: _Callable[[_Pointer[IRemoteSystem]],  # value
                                _type.HRESULT]


class IRemoteSystemConnectionRequest2(_inspectable.IInspectable):
    get_RemoteSystemApp: _Callable[[_Pointer[IRemoteSystemApp]],  # value
                                   _type.HRESULT]


class IRemoteSystemConnectionRequest3(_inspectable.IInspectable):
    get_ConnectionToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IRemoteSystemConnectionRequestFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IRemoteSystem,  # remoteSystem
                       _Pointer[IRemoteSystemConnectionRequest]],  # value
                      _type.HRESULT]


class IRemoteSystemConnectionRequestStatics(_inspectable.IInspectable, factory=True):
    CreateForApp: _Callable[[IRemoteSystemApp,  # remoteSystemApp
                             _Pointer[IRemoteSystemConnectionRequest]],  # result
                            _type.HRESULT]


class IRemoteSystemConnectionRequestStatics2(_inspectable.IInspectable, factory=True):
    CreateFromConnectionToken: _Callable[[_type.HSTRING,  # connectionToken
                                          _Pointer[IRemoteSystemConnectionRequest]],  # result
                                         _type.HRESULT]
    CreateFromConnectionTokenForUser: _Callable[[_Windows_System.IUser,  # user
                                                 _type.HSTRING,  # connectionToken
                                                 _Pointer[IRemoteSystemConnectionRequest]],  # result
                                                _type.HRESULT]


class IRemoteSystemDiscoveryTypeFilter(_inspectable.IInspectable):
    get_RemoteSystemDiscoveryType: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemDiscoveryType]],  # value
                                             _type.HRESULT]


class IRemoteSystemDiscoveryTypeFilterFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.System.RemoteSystems.RemoteSystemDiscoveryType,  # discoveryType
                       _Pointer[IRemoteSystemDiscoveryTypeFilter]],  # value
                      _type.HRESULT]


class IRemoteSystemEnumerationCompletedEventArgs(_inspectable.IInspectable):
    pass


class IRemoteSystemFilter(_inspectable.IInspectable):
    pass


class IRemoteSystemKindFilter(_inspectable.IInspectable):
    get_RemoteSystemKinds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                     _type.HRESULT]


class IRemoteSystemKindFilterFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # remoteSystemKinds
                       _Pointer[IRemoteSystemKindFilter]],  # value
                      _type.HRESULT]


class IRemoteSystemKindStatics(_inspectable.IInspectable, factory=True):
    get_Phone: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Hub: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Holographic: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Desktop: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Xbox: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IRemoteSystemKindStatics2(_inspectable.IInspectable, factory=True):
    get_Iot: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Tablet: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Laptop: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IRemoteSystemRemovedEventArgs(_inspectable.IInspectable):
    get_RemoteSystemId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IRemoteSystemSession(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ControllerDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    add_Disconnected: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSession, IRemoteSystemSessionDisconnectedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_Disconnected: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    CreateParticipantWatcher: _Callable[[_Pointer[IRemoteSystemSessionParticipantWatcher]],  # result
                                        _type.HRESULT]
    SendInvitationAsync: _Callable[[IRemoteSystem,  # invitee
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                   _type.HRESULT]


class IRemoteSystemSessionAddedEventArgs(_inspectable.IInspectable):
    get_SessionInfo: _Callable[[_Pointer[IRemoteSystemSessionInfo]],  # value
                               _type.HRESULT]


class IRemoteSystemSessionController(_inspectable.IInspectable):
    add_JoinRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionController, IRemoteSystemSessionJoinRequestedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_JoinRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    RemoveParticipantAsync: _Callable[[IRemoteSystemSessionParticipant,  # pParticipant
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]
    CreateSessionAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IRemoteSystemSessionCreationResult]]],  # operation
                                  _type.HRESULT]


class IRemoteSystemSessionControllerFactory(_inspectable.IInspectable, factory=True):
    CreateController: _Callable[[_type.HSTRING,  # displayName
                                 _Pointer[IRemoteSystemSessionController]],  # value
                                _type.HRESULT]
    CreateControllerWithSessionOptions: _Callable[[_type.HSTRING,  # displayName
                                                   IRemoteSystemSessionOptions,  # options
                                                   _Pointer[IRemoteSystemSessionController]],  # value
                                                  _type.HRESULT]


class IRemoteSystemSessionCreationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemSessionCreationStatus]],  # value
                          _type.HRESULT]
    get_Session: _Callable[[_Pointer[IRemoteSystemSession]],  # value
                           _type.HRESULT]


class IRemoteSystemSessionDisconnectedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemSessionDisconnectedReason]],  # value
                          _type.HRESULT]


class IRemoteSystemSessionInfo(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ControllerDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    JoinAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IRemoteSystemSessionJoinResult]]],  # operation
                         _type.HRESULT]


class IRemoteSystemSessionInvitation(_inspectable.IInspectable):
    get_Sender: _Callable[[_Pointer[IRemoteSystem]],  # value
                          _type.HRESULT]
    get_SessionInfo: _Callable[[_Pointer[IRemoteSystemSessionInfo]],  # value
                               _type.HRESULT]


class IRemoteSystemSessionInvitationListener(_inspectable.IInspectable):
    add_InvitationReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionInvitationListener, IRemoteSystemSessionInvitationReceivedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_InvitationReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IRemoteSystemSessionInvitationReceivedEventArgs(_inspectable.IInspectable):
    get_Invitation: _Callable[[_Pointer[IRemoteSystemSessionInvitation]],  # value
                              _type.HRESULT]


class IRemoteSystemSessionJoinRequest(_inspectable.IInspectable):
    get_Participant: _Callable[[_Pointer[IRemoteSystemSessionParticipant]],  # value
                               _type.HRESULT]
    Accept: _Callable[[],
                      _type.HRESULT]


class IRemoteSystemSessionJoinRequestedEventArgs(_inspectable.IInspectable):
    get_JoinRequest: _Callable[[_Pointer[IRemoteSystemSessionJoinRequest]],  # value
                               _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IRemoteSystemSessionJoinResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemSessionJoinStatus]],  # value
                          _type.HRESULT]
    get_Session: _Callable[[_Pointer[IRemoteSystemSession]],  # value
                           _type.HRESULT]


class IRemoteSystemSessionMessageChannel(_inspectable.IInspectable):
    get_Session: _Callable[[_Pointer[IRemoteSystemSession]],  # value
                           _type.HRESULT]
    BroadcastValueSetAsync: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # messageData
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]
    SendValueSetAsync: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # messageData
                                  IRemoteSystemSessionParticipant,  # participant
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                 _type.HRESULT]
    SendValueSetToParticipantsAsync: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # messageData
                                                _Windows_Foundation_Collections.IIterable[IRemoteSystemSessionParticipant],  # participants
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                               _type.HRESULT]
    add_ValueSetReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionMessageChannel, IRemoteSystemSessionValueSetReceivedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ValueSetReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IRemoteSystemSessionMessageChannelFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IRemoteSystemSession,  # session
                       _type.HSTRING,  # channelName
                       _Pointer[IRemoteSystemSessionMessageChannel]],  # value
                      _type.HRESULT]
    CreateWithReliability: _Callable[[IRemoteSystemSession,  # session
                                      _type.HSTRING,  # channelName
                                      _enum.Windows.System.RemoteSystems.RemoteSystemSessionMessageChannelReliability,  # reliability
                                      _Pointer[IRemoteSystemSessionMessageChannel]],  # value
                                     _type.HRESULT]


class IRemoteSystemSessionOptions(_inspectable.IInspectable):
    get_IsInviteOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_IsInviteOnly: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IRemoteSystemSessionParticipant(_inspectable.IInspectable):
    get_RemoteSystem: _Callable[[_Pointer[IRemoteSystem]],  # value
                                _type.HRESULT]
    GetHostNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Networking.IHostName]]],  # result
                            _type.HRESULT]


class IRemoteSystemSessionParticipantAddedEventArgs(_inspectable.IInspectable):
    get_Participant: _Callable[[_Pointer[IRemoteSystemSessionParticipant]],  # value
                               _type.HRESULT]


class IRemoteSystemSessionParticipantRemovedEventArgs(_inspectable.IInspectable):
    get_Participant: _Callable[[_Pointer[IRemoteSystemSessionParticipant]],  # value
                               _type.HRESULT]


class IRemoteSystemSessionParticipantWatcher(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemSessionParticipantWatcherStatus]],  # value
                          _type.HRESULT]
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionParticipantWatcher, IRemoteSystemSessionParticipantAddedEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionParticipantWatcher, IRemoteSystemSessionParticipantRemovedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionParticipantWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IRemoteSystemSessionRemovedEventArgs(_inspectable.IInspectable):
    get_SessionInfo: _Callable[[_Pointer[IRemoteSystemSessionInfo]],  # value
                               _type.HRESULT]


class IRemoteSystemSessionStatics(_inspectable.IInspectable, factory=True):
    CreateWatcher: _Callable[[_Pointer[IRemoteSystemSessionWatcher]],  # result
                             _type.HRESULT]


class IRemoteSystemSessionUpdatedEventArgs(_inspectable.IInspectable):
    get_SessionInfo: _Callable[[_Pointer[IRemoteSystemSessionInfo]],  # value
                               _type.HRESULT]


class IRemoteSystemSessionValueSetReceivedEventArgs(_inspectable.IInspectable):
    get_Sender: _Callable[[_Pointer[IRemoteSystemSessionParticipant]],  # value
                          _type.HRESULT]
    get_Message: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                           _type.HRESULT]


class IRemoteSystemSessionWatcher(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemSessionWatcherStatus]],  # value
                          _type.HRESULT]
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionWatcher, IRemoteSystemSessionAddedEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionWatcher, IRemoteSystemSessionUpdatedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemSessionWatcher, IRemoteSystemSessionRemovedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IRemoteSystemStatics(_inspectable.IInspectable, factory=True):
    FindByHostNameAsync: _Callable[[_Windows_Networking.IHostName,  # hostName
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IRemoteSystem]]],  # operation
                                   _type.HRESULT]
    CreateWatcher: _Callable[[_Pointer[IRemoteSystemWatcher]],  # result
                             _type.HRESULT]
    CreateWatcherWithFilters: _Callable[[_Windows_Foundation_Collections.IIterable[IRemoteSystemFilter],  # filters
                                         _Pointer[IRemoteSystemWatcher]],  # result
                                        _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.RemoteSystems.RemoteSystemAccessStatus]]],  # operation
                                  _type.HRESULT]


class IRemoteSystemStatics2(_inspectable.IInspectable, factory=True):
    IsAuthorizationKindEnabled: _Callable[[_enum.Windows.System.RemoteSystems.RemoteSystemAuthorizationKind,  # kind
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]


class IRemoteSystemStatics3(_inspectable.IInspectable, factory=True):
    CreateWatcherForUser: _Callable[[_Windows_System.IUser,  # user
                                     _Pointer[IRemoteSystemWatcher]],  # result
                                    _type.HRESULT]
    CreateWatcherWithFiltersForUser: _Callable[[_Windows_System.IUser,  # user
                                                _Windows_Foundation_Collections.IIterable[IRemoteSystemFilter],  # filters
                                                _Pointer[IRemoteSystemWatcher]],  # result
                                               _type.HRESULT]


class IRemoteSystemStatusTypeFilter(_inspectable.IInspectable):
    get_RemoteSystemStatusType: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemStatusType]],  # value
                                          _type.HRESULT]


class IRemoteSystemStatusTypeFilterFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.System.RemoteSystems.RemoteSystemStatusType,  # remoteSystemStatusType
                       _Pointer[IRemoteSystemStatusTypeFilter]],  # value
                      _type.HRESULT]


class IRemoteSystemUpdatedEventArgs(_inspectable.IInspectable):
    get_RemoteSystem: _Callable[[_Pointer[IRemoteSystem]],  # value
                                _type.HRESULT]


class IRemoteSystemWatcher(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_RemoteSystemAdded: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemWatcher, IRemoteSystemAddedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_RemoteSystemAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_RemoteSystemUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemWatcher, IRemoteSystemUpdatedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_RemoteSystemUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_RemoteSystemRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemWatcher, IRemoteSystemRemovedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_RemoteSystemRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IRemoteSystemWatcher2(_inspectable.IInspectable):
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemWatcher, IRemoteSystemEnumerationCompletedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_ErrorOccurred: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteSystemWatcher, IRemoteSystemWatcherErrorOccurredEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ErrorOccurred: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IRemoteSystemWatcher3(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IRemoteSystemWatcherErrorOccurredEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.System.RemoteSystems.RemoteSystemWatcherError]],  # value
                         _type.HRESULT]


class IRemoteSystemWebAccountFilter(_inspectable.IInspectable):
    get_Account: _Callable[[_Pointer[_Windows_Security_Credentials.IWebAccount]],  # value
                           _type.HRESULT]


class IRemoteSystemWebAccountFilterFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Security_Credentials.IWebAccount,  # account
                       _Pointer[IRemoteSystemWebAccountFilter]],  # value
                      _type.HRESULT]
