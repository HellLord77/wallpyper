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


class ICurrentSessionChangedEventArgs(_inspectable.IInspectable):
    pass


class IGlobalSystemMediaTransportControlsSession(_inspectable.IInspectable):
    get_SourceAppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    TryGetMediaPropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGlobalSystemMediaTransportControlsSessionMediaProperties]]],  # operation
                                          _type.HRESULT]
    GetTimelineProperties: _Callable[[_Pointer[IGlobalSystemMediaTransportControlsSessionTimelineProperties]],  # result
                                     _type.HRESULT]
    GetPlaybackInfo: _Callable[[_Pointer[IGlobalSystemMediaTransportControlsSessionPlaybackInfo]],  # result
                               _type.HRESULT]
    TryPlayAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                            _type.HRESULT]
    TryPauseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                             _type.HRESULT]
    TryStopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                            _type.HRESULT]
    TryRecordAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    TryFastForwardAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                   _type.HRESULT]
    TryRewindAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    TrySkipNextAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                _type.HRESULT]
    TrySkipPreviousAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                    _type.HRESULT]
    TryChangeChannelUpAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                       _type.HRESULT]
    TryChangeChannelDownAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    TryTogglePlayPauseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                       _type.HRESULT]
    TryChangeAutoRepeatModeAsync: _Callable[[_enum.Windows.Media.MediaPlaybackAutoRepeatMode,  # requestedAutoRepeatMode
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                            _type.HRESULT]
    TryChangePlaybackRateAsync: _Callable[[_type.DOUBLE,  # requestedPlaybackRate
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    TryChangeShuffleActiveAsync: _Callable[[_type.boolean,  # requestedShuffleState
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]
    TryChangePlaybackPositionAsync: _Callable[[_type.INT64,  # requestedPlaybackPosition
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                              _type.HRESULT]
    add_TimelinePropertiesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGlobalSystemMediaTransportControlsSession, ITimelinePropertiesChangedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_TimelinePropertiesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_PlaybackInfoChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGlobalSystemMediaTransportControlsSession, IPlaybackInfoChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PlaybackInfoChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_MediaPropertiesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGlobalSystemMediaTransportControlsSession, IMediaPropertiesChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_MediaPropertiesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IGlobalSystemMediaTransportControlsSessionManager(_inspectable.IInspectable):
    GetCurrentSession: _Callable[[_Pointer[IGlobalSystemMediaTransportControlsSession]],  # result
                                 _type.HRESULT]
    GetSessions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IGlobalSystemMediaTransportControlsSession]]],  # result
                           _type.HRESULT]
    add_CurrentSessionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGlobalSystemMediaTransportControlsSessionManager, ICurrentSessionChangedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_CurrentSessionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_SessionsChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IGlobalSystemMediaTransportControlsSessionManager, ISessionsChangedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_SessionsChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IGlobalSystemMediaTransportControlsSessionManagerStatics(_inspectable.IInspectable):
    RequestAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IGlobalSystemMediaTransportControlsSessionManager]]],  # operation
                            _type.HRESULT]

    _factory = True


class IGlobalSystemMediaTransportControlsSessionMediaProperties(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Subtitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_AlbumArtist: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Artist: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_AlbumTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_TrackNumber: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_Genres: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                          _type.HRESULT]
    get_AlbumTrackCount: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_PlaybackType: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.MediaPlaybackType]]],  # value
                                _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]


class IGlobalSystemMediaTransportControlsSessionPlaybackControls(_inspectable.IInspectable):
    get_IsPlayEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsPauseEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_IsStopEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsRecordEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsFastForwardEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsRewindEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsNextEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsPreviousEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsChannelUpEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsChannelDownEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_IsPlayPauseToggleEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_IsShuffleEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsRepeatEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsPlaybackRateEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_IsPlaybackPositionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]


class IGlobalSystemMediaTransportControlsSessionPlaybackInfo(_inspectable.IInspectable):
    get_Controls: _Callable[[_Pointer[IGlobalSystemMediaTransportControlsSessionPlaybackControls]],  # value
                            _type.HRESULT]
    get_PlaybackStatus: _Callable[[_Pointer[_enum.Windows.Media.Control.GlobalSystemMediaTransportControlsSessionPlaybackStatus]],  # value
                                  _type.HRESULT]
    get_PlaybackType: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.MediaPlaybackType]]],  # value
                                _type.HRESULT]
    get_AutoRepeatMode: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.MediaPlaybackAutoRepeatMode]]],  # value
                                  _type.HRESULT]
    get_PlaybackRate: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                _type.HRESULT]
    get_IsShuffleActive: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                   _type.HRESULT]


class IGlobalSystemMediaTransportControlsSessionTimelineProperties(_inspectable.IInspectable):
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_EndTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]
    get_MinSeekTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    get_MaxSeekTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_LastUpdatedTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                   _type.HRESULT]


class IMediaPropertiesChangedEventArgs(_inspectable.IInspectable):
    pass


class IPlaybackInfoChangedEventArgs(_inspectable.IInspectable):
    pass


class ISessionsChangedEventArgs(_inspectable.IInspectable):
    pass


class ITimelinePropertiesChangedEventArgs(_inspectable.IInspectable):
    pass
