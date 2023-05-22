from __future__ import annotations

from typing import Callable as _Callable

from .. import Audio as _Windows_Media_Audio
from .. import Casting as _Windows_Media_Casting
from .. import Core as _Windows_Media_Core
from .. import Protection as _Windows_Media_Protection
from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ... import Storage as _Windows_Storage
from ...Devices import Enumeration as _Windows_Devices_Enumeration
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ...Storage import Streams as _Windows_Storage_Streams
from ...UI import Composition as _Windows_UI_Composition
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBackgroundMediaPlayerStatics(_inspectable.IInspectable, factory=True):
    Current: _Callable[[_Pointer[IMediaPlayer]],  # player
                       _type.HRESULT]
    MessageReceivedFromBackground: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    MessageReceivedFromForeground: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    SendMessageToBackground: _Callable[[_Windows_Foundation_Collections.IPropertySet],  # value
                                       _type.HRESULT]
    SendMessageToForeground: _Callable[[_Windows_Foundation_Collections.IPropertySet],  # value
                                       _type.HRESULT]
    IsMediaPlaying: _Callable[[_Pointer[_type.boolean]],  # isMediaPlaying
                              _type.HRESULT]
    Shutdown: _Callable[[],
                        _type.HRESULT]


class ICurrentMediaPlaybackItemChangedEventArgs(_inspectable.IInspectable):
    get_NewItem: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                           _type.HRESULT]
    get_OldItem: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                           _type.HRESULT]


class ICurrentMediaPlaybackItemChangedEventArgs2(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlaybackItemChangedReason]],  # value
                          _type.HRESULT]


class IMediaBreak(_inspectable.IInspectable):
    get_PlaybackList: _Callable[[_Pointer[IMediaPlaybackList]],  # value
                                _type.HRESULT]
    get_PresentationPosition: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                        _type.HRESULT]
    get_InsertionMethod: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaBreakInsertionMethod]],  # value
                                   _type.HRESULT]
    get_CustomProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                    _type.HRESULT]
    get_CanStart: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_CanStart: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class IMediaBreakEndedEventArgs(_inspectable.IInspectable):
    get_MediaBreak: _Callable[[_Pointer[IMediaBreak]],  # value
                              _type.HRESULT]


class IMediaBreakFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.Media.Playback.MediaBreakInsertionMethod,  # insertionMethod
                       _Pointer[IMediaBreak]],  # result
                      _type.HRESULT]
    CreateWithPresentationPosition: _Callable[[_enum.Windows.Media.Playback.MediaBreakInsertionMethod,  # insertionMethod
                                               _struct.Windows.Foundation.TimeSpan,  # presentationPosition
                                               _Pointer[IMediaBreak]],  # result
                                              _type.HRESULT]


class IMediaBreakManager(_inspectable.IInspectable):
    add_BreaksSeekedOver: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaBreakManager, IMediaBreakSeekedOverEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_BreaksSeekedOver: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_BreakStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaBreakManager, IMediaBreakStartedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_BreakStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_BreakEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaBreakManager, IMediaBreakEndedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_BreakEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_BreakSkipped: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaBreakManager, IMediaBreakSkippedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_BreakSkipped: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    get_CurrentBreak: _Callable[[_Pointer[IMediaBreak]],  # value
                                _type.HRESULT]
    get_PlaybackSession: _Callable[[_Pointer[IMediaPlaybackSession]],  # value
                                   _type.HRESULT]
    PlayBreak: _Callable[[IMediaBreak],  # value
                         _type.HRESULT]
    SkipCurrentBreak: _Callable[[],
                                _type.HRESULT]


class IMediaBreakSchedule(_inspectable.IInspectable):
    add_ScheduleChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaBreakSchedule, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ScheduleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    InsertMidrollBreak: _Callable[[IMediaBreak],  # mediaBreak
                                  _type.HRESULT]
    RemoveMidrollBreak: _Callable[[IMediaBreak],  # mediaBreak
                                  _type.HRESULT]
    get_MidrollBreaks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaBreak]]],  # value
                                 _type.HRESULT]
    put_PrerollBreak: _Callable[[IMediaBreak],  # value
                                _type.HRESULT]
    get_PrerollBreak: _Callable[[_Pointer[IMediaBreak]],  # value
                                _type.HRESULT]
    put_PostrollBreak: _Callable[[IMediaBreak],  # value
                                 _type.HRESULT]
    get_PostrollBreak: _Callable[[_Pointer[IMediaBreak]],  # value
                                 _type.HRESULT]
    get_PlaybackItem: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                                _type.HRESULT]


class IMediaBreakSeekedOverEventArgs(_inspectable.IInspectable):
    get_SeekedOverBreaks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaBreak]]],  # value
                                    _type.HRESULT]
    get_OldPosition: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    get_NewPosition: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]


class IMediaBreakSkippedEventArgs(_inspectable.IInspectable):
    get_MediaBreak: _Callable[[_Pointer[IMediaBreak]],  # value
                              _type.HRESULT]


class IMediaBreakStartedEventArgs(_inspectable.IInspectable):
    get_MediaBreak: _Callable[[_Pointer[IMediaBreak]],  # value
                              _type.HRESULT]


class IMediaEnginePlaybackSource(_inspectable.IInspectable):
    CurrentItem: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                           _type.HRESULT]
    SetPlaybackSource: _Callable[[IMediaPlaybackSource],  # source
                                 _type.HRESULT]


class IMediaItemDisplayProperties(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Media.MediaPlaybackType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.Media.MediaPlaybackType],  # value
                        _type.HRESULT]
    get_MusicProperties: _Callable[[_Pointer[_Windows_Media.IMusicDisplayProperties]],  # value
                                   _type.HRESULT]
    get_VideoProperties: _Callable[[_Pointer[_Windows_Media.IVideoDisplayProperties]],  # value
                                   _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    put_Thumbnail: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    ClearAll: _Callable[[],
                        _type.HRESULT]


class IMediaPlaybackCommandManager(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_MediaPlayer: _Callable[[_Pointer[IMediaPlayer]],  # value
                               _type.HRESULT]
    get_PlayBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                _type.HRESULT]
    get_PauseBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                 _type.HRESULT]
    get_NextBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                _type.HRESULT]
    get_PreviousBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                    _type.HRESULT]
    get_FastForwardBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                       _type.HRESULT]
    get_RewindBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                  _type.HRESULT]
    get_ShuffleBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                   _type.HRESULT]
    get_AutoRepeatModeBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                          _type.HRESULT]
    get_PositionBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                    _type.HRESULT]
    get_RateBehavior: _Callable[[_Pointer[IMediaPlaybackCommandManagerCommandBehavior]],  # value
                                _type.HRESULT]
    add_PlayReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerPlayReceivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_PlayReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_PauseReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerPauseReceivedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PauseReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_NextReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerNextReceivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_NextReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_PreviousReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerPreviousReceivedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_PreviousReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_FastForwardReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerFastForwardReceivedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_FastForwardReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_RewindReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerRewindReceivedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_RewindReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_ShuffleReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerShuffleReceivedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ShuffleReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_AutoRepeatModeReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerAutoRepeatModeReceivedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_AutoRepeatModeReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_PositionReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerPositionReceivedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_PositionReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_RateReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManager, IMediaPlaybackCommandManagerRateReceivedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_RateReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IMediaPlaybackCommandManagerAutoRepeatModeReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_AutoRepeatMode: _Callable[[_Pointer[_enum.Windows.Media.MediaPlaybackAutoRepeatMode]],  # value
                                  _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerCommandBehavior(_inspectable.IInspectable):
    get_CommandManager: _Callable[[_Pointer[IMediaPlaybackCommandManager]],  # value
                                  _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_EnablingRule: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaCommandEnablingRule]],  # value
                                _type.HRESULT]
    put_EnablingRule: _Callable[[_enum.Windows.Media.Playback.MediaCommandEnablingRule],  # value
                                _type.HRESULT]
    add_IsEnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackCommandManagerCommandBehavior, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_IsEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IMediaPlaybackCommandManagerFastForwardReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerNextReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerPauseReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerPlayReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerPositionReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerPreviousReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerRateReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_PlaybackRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerRewindReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackCommandManagerShuffleReceivedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_IsShuffleRequested: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IMediaPlaybackItem(_inspectable.IInspectable):
    add_AudioTracksChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackItem, _Windows_Foundation_Collections.IVectorChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_AudioTracksChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_VideoTracksChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackItem, _Windows_Foundation_Collections.IVectorChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_VideoTracksChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_TimedMetadataTracksChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackItem, _Windows_Foundation_Collections.IVectorChangedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_TimedMetadataTracksChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    get_Source: _Callable[[_Pointer[_Windows_Media_Core.IMediaSource2]],  # value
                          _type.HRESULT]
    get_AudioTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_Core.IMediaTrack]]],  # value
                               _type.HRESULT]
    get_VideoTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_Core.IMediaTrack]]],  # value
                               _type.HRESULT]
    get_TimedMetadataTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_Core.ITimedMetadataTrack]]],  # value
                                       _type.HRESULT]


class IMediaPlaybackItem2(_inspectable.IInspectable):
    get_BreakSchedule: _Callable[[_Pointer[IMediaBreakSchedule]],  # value
                                 _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_DurationLimit: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                 _type.HRESULT]
    get_CanSkip: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_CanSkip: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDisplayProperties: _Callable[[_Pointer[IMediaItemDisplayProperties]],  # value
                                    _type.HRESULT]
    ApplyDisplayProperties: _Callable[[IMediaItemDisplayProperties],  # value
                                      _type.HRESULT]


class IMediaPlaybackItem3(_inspectable.IInspectable):
    get_IsDisabledInPlaybackList: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsDisabledInPlaybackList: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_TotalDownloadProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]
    get_AutoLoadedDisplayProperties: _Callable[[_Pointer[_enum.Windows.Media.Playback.AutoLoadedDisplayPropertyKind]],  # value
                                               _type.HRESULT]
    put_AutoLoadedDisplayProperties: _Callable[[_enum.Windows.Media.Playback.AutoLoadedDisplayPropertyKind],  # value
                                               _type.HRESULT]


class IMediaPlaybackItemError(_inspectable.IInspectable):
    get_ErrorCode: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlaybackItemErrorCode]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IMediaPlaybackItemFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Media_Core.IMediaSource2,  # source
                       _Pointer[IMediaPlaybackItem]],  # value
                      _type.HRESULT]


class IMediaPlaybackItemFactory2(_inspectable.IInspectable, factory=True):
    CreateWithStartTime: _Callable[[_Windows_Media_Core.IMediaSource2,  # source
                                    _struct.Windows.Foundation.TimeSpan,  # startTime
                                    _Pointer[IMediaPlaybackItem]],  # result
                                   _type.HRESULT]
    CreateWithStartTimeAndDurationLimit: _Callable[[_Windows_Media_Core.IMediaSource2,  # source
                                                    _struct.Windows.Foundation.TimeSpan,  # startTime
                                                    _struct.Windows.Foundation.TimeSpan,  # durationLimit
                                                    _Pointer[IMediaPlaybackItem]],  # result
                                                   _type.HRESULT]


class IMediaPlaybackItemFailedEventArgs(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                        _type.HRESULT]
    get_Error: _Callable[[_Pointer[IMediaPlaybackItemError]],  # value
                         _type.HRESULT]


class IMediaPlaybackItemOpenedEventArgs(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                        _type.HRESULT]


class IMediaPlaybackItemStatics(_inspectable.IInspectable, factory=True):
    FindFromMediaSource: _Callable[[_Windows_Media_Core.IMediaSource2,  # source
                                    _Pointer[IMediaPlaybackItem]],  # value
                                   _type.HRESULT]


class IMediaPlaybackList(_inspectable.IInspectable):
    add_ItemFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackList, IMediaPlaybackItemFailedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_ItemFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_CurrentItemChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackList, ICurrentMediaPlaybackItemChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CurrentItemChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ItemOpened: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackList, IMediaPlaybackItemOpenedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_ItemOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[IMediaPlaybackItem]]],  # value
                         _type.HRESULT]
    get_AutoRepeatEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_AutoRepeatEnabled: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_ShuffleEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_ShuffleEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_CurrentItem: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                               _type.HRESULT]
    get_CurrentItemIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    MoveNext: _Callable[[_Pointer[IMediaPlaybackItem]],  # item
                        _type.HRESULT]
    MovePrevious: _Callable[[_Pointer[IMediaPlaybackItem]],  # item
                            _type.HRESULT]
    MoveTo: _Callable[[_type.UINT32,  # itemIndex
                       _Pointer[IMediaPlaybackItem]],  # item
                      _type.HRESULT]


class IMediaPlaybackList2(_inspectable.IInspectable):
    get_MaxPrefetchTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                   _type.HRESULT]
    put_MaxPrefetchTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    get_StartingItem: _Callable[[_Pointer[IMediaPlaybackItem]],  # value
                                _type.HRESULT]
    put_StartingItem: _Callable[[IMediaPlaybackItem],  # value
                                _type.HRESULT]
    get_ShuffledItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaPlaybackItem]]],  # value
                                 _type.HRESULT]
    SetShuffledItems: _Callable[[_Windows_Foundation_Collections.IIterable[IMediaPlaybackItem]],  # value
                                _type.HRESULT]


class IMediaPlaybackList3(_inspectable.IInspectable):
    get_MaxPlayedItemsToKeepOpen: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                            _type.HRESULT]
    put_MaxPlayedItemsToKeepOpen: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                            _type.HRESULT]


class IMediaPlaybackSession(_inspectable.IInspectable):
    add_PlaybackStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_PlaybackStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_PlaybackRateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PlaybackRateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_SeekCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SeekCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_BufferingStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_BufferingStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_BufferingEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_BufferingEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_BufferingProgressChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_BufferingProgressChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_DownloadProgressChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_DownloadProgressChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_NaturalDurationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_NaturalDurationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_PositionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PositionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_NaturalVideoSizeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_NaturalVideoSizeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    get_MediaPlayer: _Callable[[_Pointer[IMediaPlayer]],  # value
                               _type.HRESULT]
    get_NaturalDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_PlaybackState: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlaybackState]],  # value
                                 _type.HRESULT]
    get_CanSeek: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_CanPause: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsProtected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_PlaybackRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_PlaybackRate: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_BufferingProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_DownloadProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                    _type.HRESULT]
    get_NaturalVideoHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    get_NaturalVideoWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_NormalizedSourceRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                        _type.HRESULT]
    put_NormalizedSourceRect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                        _type.HRESULT]
    get_StereoscopicVideoPackingMode: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.StereoscopicVideoPackingMode]],  # value
                                                _type.HRESULT]
    put_StereoscopicVideoPackingMode: _Callable[[_enum.Windows.Media.MediaProperties.StereoscopicVideoPackingMode],  # value
                                                _type.HRESULT]


class IMediaPlaybackSession2(_inspectable.IInspectable):
    add_BufferedRangesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_BufferedRangesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_PlayedRangesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PlayedRangesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_SeekableRangesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_SeekableRangesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_SupportedPlaybackRatesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlaybackSession, _inspectable.IInspectable],  # value
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_SupportedPlaybackRatesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    get_SphericalVideoProjection: _Callable[[_Pointer[IMediaPlaybackSphericalVideoProjection]],  # value
                                            _type.HRESULT]
    get_IsMirroring: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsMirroring: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    GetBufferedRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Media.MediaTimeRange]]],  # value
                                 _type.HRESULT]
    GetPlayedRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Media.MediaTimeRange]]],  # value
                               _type.HRESULT]
    GetSeekableRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Media.MediaTimeRange]]],  # value
                                 _type.HRESULT]
    IsSupportedPlaybackRateRange: _Callable[[_type.DOUBLE,  # rate1
                                             _type.DOUBLE,  # rate2
                                             _Pointer[_type.boolean]],  # value
                                            _type.HRESULT]


class IMediaPlaybackSession3(_inspectable.IInspectable):
    get_PlaybackRotation: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.MediaRotation]],  # value
                                    _type.HRESULT]
    put_PlaybackRotation: _Callable[[_enum.Windows.Media.MediaProperties.MediaRotation],  # value
                                    _type.HRESULT]
    GetOutputDegradationPolicyState: _Callable[[_Pointer[IMediaPlaybackSessionOutputDegradationPolicyState]],  # value
                                               _type.HRESULT]


class IMediaPlaybackSessionBufferingStartedEventArgs(_inspectable.IInspectable):
    get_IsPlaybackInterruption: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IMediaPlaybackSessionOutputDegradationPolicyState(_inspectable.IInspectable):
    get_VideoConstrictionReason: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlaybackSessionVideoConstrictionReason]],  # value
                                           _type.HRESULT]


class IMediaPlaybackSource(_inspectable.IInspectable):
    pass


class IMediaPlaybackSphericalVideoProjection(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_FrameFormat: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.SphericalVideoFrameFormat]],  # value
                               _type.HRESULT]
    put_FrameFormat: _Callable[[_enum.Windows.Media.MediaProperties.SphericalVideoFrameFormat],  # value
                               _type.HRESULT]
    get_HorizontalFieldOfViewInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                  _type.HRESULT]
    put_HorizontalFieldOfViewInDegrees: _Callable[[_type.DOUBLE],  # value
                                                  _type.HRESULT]
    get_ViewOrientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                                   _type.HRESULT]
    put_ViewOrientation: _Callable[[_struct.Windows.Foundation.Numerics.Quaternion],  # value
                                   _type.HRESULT]
    get_ProjectionMode: _Callable[[_Pointer[_enum.Windows.Media.Playback.SphericalVideoProjectionMode]],  # value
                                  _type.HRESULT]
    put_ProjectionMode: _Callable[[_enum.Windows.Media.Playback.SphericalVideoProjectionMode],  # value
                                  _type.HRESULT]


class IMediaPlaybackTimedMetadataTrackList(_inspectable.IInspectable):
    add_PresentationModeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[_Windows_Foundation_Collections.IVectorView[_Windows_Media_Core.ITimedMetadataTrack], ITimedMetadataPresentationModeChangedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_PresentationModeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    GetPresentationMode: _Callable[[_type.UINT32,  # index
                                    _Pointer[_enum.Windows.Media.Playback.TimedMetadataTrackPresentationMode]],  # value
                                   _type.HRESULT]
    SetPresentationMode: _Callable[[_type.UINT32,  # index
                                    _enum.Windows.Media.Playback.TimedMetadataTrackPresentationMode],  # value
                                   _type.HRESULT]


class IMediaPlayer(_inspectable.IInspectable):
    get_AutoPlay: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_AutoPlay: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    NaturalDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    Position: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                        _type.HRESULT]
    BufferingProgress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    CurrentState: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlayerState]],  # value
                            _type.HRESULT]
    CanSeek: _Callable[[_Pointer[_type.boolean]],  # value
                       _type.HRESULT]
    CanPause: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    get_IsLoopingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsLoopingEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    IsProtected: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsMuted: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_IsMuted: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    PlaybackRate: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_Volume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Volume: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    PlaybackMediaMarkers: _Callable[[_Pointer[IPlaybackMediaMarkerSequence]],  # value
                                    _type.HRESULT]
    add_MediaOpened: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, _inspectable.IInspectable],  # value
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_MediaOpened: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_MediaEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, _inspectable.IInspectable],  # value
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_MediaEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_MediaFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, IMediaPlayerFailedEventArgs],  # value
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_MediaFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    CurrentStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    PlaybackMediaMarkerReached: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    MediaPlayerRateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_VolumeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, _inspectable.IInspectable],  # value
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_VolumeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    SeekCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    BufferingStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    BufferingEnded: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    Play: _Callable[[],
                    _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    SetUriSource: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                            _type.HRESULT]


class IMediaPlayer2(_inspectable.IInspectable):
    get_SystemMediaTransportControls: _Callable[[_Pointer[_Windows_Media.ISystemMediaTransportControls]],  # value
                                                _type.HRESULT]
    get_AudioCategory: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlayerAudioCategory]],  # value
                                 _type.HRESULT]
    put_AudioCategory: _Callable[[_enum.Windows.Media.Playback.MediaPlayerAudioCategory],  # value
                                 _type.HRESULT]
    get_AudioDeviceType: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlayerAudioDeviceType]],  # value
                                   _type.HRESULT]
    put_AudioDeviceType: _Callable[[_enum.Windows.Media.Playback.MediaPlayerAudioDeviceType],  # value
                                   _type.HRESULT]


class IMediaPlayer3(_inspectable.IInspectable):
    add_IsMutedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, _inspectable.IInspectable],  # value
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_IsMutedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_SourceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, _inspectable.IInspectable],  # value
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SourceChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    get_AudioBalance: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_AudioBalance: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_RealTimePlayback: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_RealTimePlayback: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_StereoscopicVideoRenderMode: _Callable[[_Pointer[_enum.Windows.Media.Playback.StereoscopicVideoRenderMode]],  # value
                                               _type.HRESULT]
    put_StereoscopicVideoRenderMode: _Callable[[_enum.Windows.Media.Playback.StereoscopicVideoRenderMode],  # value
                                               _type.HRESULT]
    get_BreakManager: _Callable[[_Pointer[IMediaBreakManager]],  # value
                                _type.HRESULT]
    get_CommandManager: _Callable[[_Pointer[IMediaPlaybackCommandManager]],  # value
                                  _type.HRESULT]
    get_AudioDevice: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                               _type.HRESULT]
    put_AudioDevice: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation],  # value
                               _type.HRESULT]
    get_TimelineController: _Callable[[_Pointer[_Windows_Media.IMediaTimelineController]],  # value
                                      _type.HRESULT]
    put_TimelineController: _Callable[[_Windows_Media.IMediaTimelineController],  # value
                                      _type.HRESULT]
    get_TimelineControllerPositionOffset: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                                    _type.HRESULT]
    put_TimelineControllerPositionOffset: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                                    _type.HRESULT]
    get_PlaybackSession: _Callable[[_Pointer[IMediaPlaybackSession]],  # value
                                   _type.HRESULT]
    StepForwardOneFrame: _Callable[[],
                                   _type.HRESULT]
    StepBackwardOneFrame: _Callable[[],
                                    _type.HRESULT]
    GetAsCastingSource: _Callable[[_Pointer[_Windows_Media_Casting.ICastingSource]],  # returnValue
                                  _type.HRESULT]


class IMediaPlayer4(_inspectable.IInspectable):
    SetSurfaceSize: _Callable[[_struct.Windows.Foundation.Size],  # size
                              _type.HRESULT]
    GetSurface: _Callable[[_Windows_UI_Composition.ICompositor,  # compositor
                           _Pointer[IMediaPlayerSurface]],  # result
                          _type.HRESULT]


class IMediaPlayer5(_inspectable.IInspectable):
    add_VideoFrameAvailable: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, _inspectable.IInspectable],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_VideoFrameAvailable: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    get_IsVideoFrameServerEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsVideoFrameServerEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    CopyFrameToVideoSurface: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface],  # destination
                                       _type.HRESULT]
    CopyFrameToVideoSurfaceWithTargetRectangle: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # destination
                                                           _struct.Windows.Foundation.Rect],  # targetRectangle
                                                          _type.HRESULT]
    CopyFrameToStereoscopicVideoSurfaces: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # destinationLeftEye
                                                     _Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface],  # destinationRightEye
                                                    _type.HRESULT]


class IMediaPlayer6(_inspectable.IInspectable):
    add_SubtitleFrameChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaPlayer, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SubtitleFrameChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    RenderSubtitlesToSurface: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # destination
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]
    RenderSubtitlesToSurfaceWithTargetRectangle: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # destination
                                                            _struct.Windows.Foundation.Rect,  # targetRectangle
                                                            _Pointer[_type.boolean]],  # result
                                                           _type.HRESULT]


class IMediaPlayer7(_inspectable.IInspectable):
    get_AudioStateMonitor: _Callable[[_Pointer[_Windows_Media_Audio.IAudioStateMonitor]],  # value
                                     _type.HRESULT]


class IMediaPlayerDataReceivedEventArgs(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                        _type.HRESULT]


class IMediaPlayerEffects(_inspectable.IInspectable):
    AddAudioEffect: _Callable[[_type.HSTRING,  # activatableClassId
                               _type.boolean,  # effectOptional
                               _Windows_Foundation_Collections.IPropertySet],  # configuration
                              _type.HRESULT]
    RemoveAllEffects: _Callable[[],
                                _type.HRESULT]


class IMediaPlayerEffects2(_inspectable.IInspectable):
    AddVideoEffect: _Callable[[_type.HSTRING,  # activatableClassId
                               _type.boolean,  # effectOptional
                               _Windows_Foundation_Collections.IPropertySet],  # effectConfiguration
                              _type.HRESULT]


class IMediaPlayerFailedEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Media.Playback.MediaPlayerError]],  # value
                         _type.HRESULT]
    get_ExtendedErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                                     _type.HRESULT]
    get_ErrorMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IMediaPlayerRateChangedEventArgs(_inspectable.IInspectable):
    get_NewRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]


class IMediaPlayerSource(_inspectable.IInspectable):
    get_ProtectionManager: _Callable[[_Pointer[_Windows_Media_Protection.IMediaProtectionManager]],  # value
                                     _type.HRESULT]
    put_ProtectionManager: _Callable[[_Windows_Media_Protection.IMediaProtectionManager],  # value
                                     _type.HRESULT]
    SetFileSource: _Callable[[_Windows_Storage.IStorageFile],  # file
                             _type.HRESULT]
    SetStreamSource: _Callable[[_Windows_Storage_Streams.IRandomAccessStream],  # stream
                               _type.HRESULT]
    SetMediaSource: _Callable[[_Windows_Media_Core.IMediaSource],  # source
                              _type.HRESULT]


class IMediaPlayerSource2(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[IMediaPlaybackSource]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[IMediaPlaybackSource],  # value
                          _type.HRESULT]


class IMediaPlayerSurface(_inspectable.IInspectable):
    get_CompositionSurface: _Callable[[_Pointer[_Windows_UI_Composition.ICompositionSurface]],  # value
                                      _type.HRESULT]
    get_Compositor: _Callable[[_Pointer[_Windows_UI_Composition.ICompositor]],  # value
                              _type.HRESULT]
    get_MediaPlayer: _Callable[[_Pointer[IMediaPlayer]],  # value
                               _type.HRESULT]


class IPlaybackMediaMarker(_inspectable.IInspectable):
    get_Time: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]
    get_MediaMarkerType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IPlaybackMediaMarkerFactory(_inspectable.IInspectable, factory=True):
    CreateFromTime: _Callable[[_struct.Windows.Foundation.TimeSpan,  # value
                               _Pointer[IPlaybackMediaMarker]],  # marker
                              _type.HRESULT]
    Create: _Callable[[_struct.Windows.Foundation.TimeSpan,  # value
                       _type.HSTRING,  # mediaMarketType
                       _type.HSTRING,  # text
                       _Pointer[IPlaybackMediaMarker]],  # marker
                      _type.HRESULT]


class IPlaybackMediaMarkerReachedEventArgs(_inspectable.IInspectable):
    get_PlaybackMediaMarker: _Callable[[_Pointer[IPlaybackMediaMarker]],  # value
                                       _type.HRESULT]


class IPlaybackMediaMarkerSequence(_inspectable.IInspectable):
    get_Size: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    Insert: _Callable[[IPlaybackMediaMarker],  # value
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class ITimedMetadataPresentationModeChangedEventArgs(_inspectable.IInspectable):
    get_Track: _Callable[[_Pointer[_Windows_Media_Core.ITimedMetadataTrack]],  # value
                         _type.HRESULT]
    get_OldPresentationMode: _Callable[[_Pointer[_enum.Windows.Media.Playback.TimedMetadataTrackPresentationMode]],  # value
                                       _type.HRESULT]
    get_NewPresentationMode: _Callable[[_Pointer[_enum.Windows.Media.Playback.TimedMetadataTrackPresentationMode]],  # value
                                       _type.HRESULT]
