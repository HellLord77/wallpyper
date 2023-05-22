from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ICurrentTimeChangeRequestedEventArgs(_inspectable.IInspectable):
    get_Time: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]


class IMuteChangeRequestedEventArgs(_inspectable.IInspectable):
    get_Mute: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]


class IPlayToConnection(_inspectable.IInspectable):
    State: _Callable[[_Pointer[_enum.Windows.Media.PlayTo.PlayToConnectionState]],  # value
                     _type.HRESULT]
    StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    Transferred: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
    Error: _Callable[[_struct.EventRegistrationToken],  # token
                     _type.HRESULT]


class IPlayToConnectionErrorEventArgs(_inspectable.IInspectable):
    Code: _Callable[[_Pointer[_enum.Windows.Media.PlayTo.PlayToConnectionError]],  # value
                    _type.HRESULT]
    Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]


class IPlayToConnectionStateChangedEventArgs(_inspectable.IInspectable):
    PreviousState: _Callable[[_Pointer[_enum.Windows.Media.PlayTo.PlayToConnectionState]],  # value
                             _type.HRESULT]
    CurrentState: _Callable[[_Pointer[_enum.Windows.Media.PlayTo.PlayToConnectionState]],  # value
                            _type.HRESULT]


class IPlayToConnectionTransferredEventArgs(_inspectable.IInspectable):
    PreviousSource: _Callable[[_Pointer[IPlayToSource]],  # value
                              _type.HRESULT]
    CurrentSource: _Callable[[_Pointer[IPlayToSource]],  # value
                             _type.HRESULT]


class IPlayToManager(_inspectable.IInspectable):
    SourceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    SourceSelected: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    DefaultSourceSelection: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IPlayToManagerStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IPlayToManager]],  # playToManager
                                 _type.HRESULT]
    ShowPlayToUI: _Callable[[],
                            _type.HRESULT]


class IPlayToReceiver(_inspectable.IInspectable):
    add_PlayRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PlayRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PauseRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PauseRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_SourceChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, ISourceChangeRequestedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_SourceChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_PlaybackRateChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, IPlaybackRateChangeRequestedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_PlaybackRateChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_CurrentTimeChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, ICurrentTimeChangeRequestedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_CurrentTimeChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    add_MuteChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, IMuteChangeRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_MuteChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_VolumeChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, IVolumeChangeRequestedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_VolumeChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_TimeUpdateRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_TimeUpdateRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_StopRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IPlayToReceiver, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StopRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    NotifyVolumeChange: _Callable[[_type.DOUBLE,  # volume
                                   _type.boolean],  # mute
                                  _type.HRESULT]
    NotifyRateChange: _Callable[[_type.DOUBLE],  # rate
                                _type.HRESULT]
    NotifyLoadedMetadata: _Callable[[],
                                    _type.HRESULT]
    NotifyTimeUpdate: _Callable[[_struct.Windows.Foundation.TimeSpan],  # currentTime
                                _type.HRESULT]
    NotifyDurationChange: _Callable[[_struct.Windows.Foundation.TimeSpan],  # duration
                                    _type.HRESULT]
    NotifySeeking: _Callable[[],
                             _type.HRESULT]
    NotifySeeked: _Callable[[],
                            _type.HRESULT]
    NotifyPaused: _Callable[[],
                            _type.HRESULT]
    NotifyPlaying: _Callable[[],
                             _type.HRESULT]
    NotifyEnded: _Callable[[],
                           _type.HRESULT]
    NotifyError: _Callable[[],
                           _type.HRESULT]
    NotifyStopped: _Callable[[],
                             _type.HRESULT]
    get_FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_FriendlyName: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    put_SupportsImage: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SupportsImage: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_SupportsAudio: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SupportsAudio: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_SupportsVideo: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SupportsVideo: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                          _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                         _type.HRESULT]


class IPlayToSource(_inspectable.IInspectable):
    Connection: _Callable[[_Pointer[IPlayToConnection]],  # value
                          _type.HRESULT]
    Next: _Callable[[IPlayToSource],  # value
                    _type.HRESULT]
    PlayNext: _Callable[[],
                        _type.HRESULT]


class IPlayToSourceDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IPlayToSourceRequest(_inspectable.IInspectable):
    Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]
    DisplayErrorString: _Callable[[_type.HSTRING],  # errorString
                                  _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IPlayToSourceDeferral]],  # deferral
                           _type.HRESULT]
    SetSource: _Callable[[IPlayToSource],  # value
                         _type.HRESULT]


class IPlayToSourceRequestedEventArgs(_inspectable.IInspectable):
    SourceRequest: _Callable[[_Pointer[IPlayToSourceRequest]],  # value
                             _type.HRESULT]


class IPlayToSourceSelectedEventArgs(_inspectable.IInspectable):
    FriendlyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    Icon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                    _type.HRESULT]
    SupportsImage: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    SupportsAudio: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    SupportsVideo: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IPlayToSourceWithPreferredSourceUri(_inspectable.IInspectable):
    PreferredSourceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                  _type.HRESULT]


class IPlaybackRateChangeRequestedEventArgs(_inspectable.IInspectable):
    get_Rate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]


class ISourceChangeRequestedEventArgs(_inspectable.IInspectable):
    get_Stream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]],  # value
                          _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Author: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Album: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Genre: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Date: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                        _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    get_Rating: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                          _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IVolumeChangeRequestedEventArgs(_inspectable.IInspectable):
    get_Volume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
