from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Foundation as _Windows_Foundation
from .. import Storage as _Windows_Storage
from ..ApplicationModel import AppService as _Windows_ApplicationModel_AppService
from ..Foundation import Collections as _Windows_Foundation_Collections
from ..Graphics import Imaging as _Windows_Graphics_Imaging
from ..Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ..Storage import Streams as _Windows_Storage_Streams
from ... import inspectable as _inspectable
from ..... import enum as _enum
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class IAudioBuffer(_inspectable.IInspectable):
    get_Capacity: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Length: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]


class IAudioFrame(_inspectable.IInspectable):
    LockBuffer: _Callable[[_enum.Windows.Media.AudioBufferAccessMode,  # mode
                           _Pointer[IAudioBuffer]],  # value
                          _type.HRESULT]


class IAudioFrameFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # capacity
                       _Pointer[IAudioFrame]],  # value
                      _type.HRESULT]

    _factory = True


class IAutoRepeatModeChangeRequestedEventArgs(_inspectable.IInspectable):
    get_RequestedAutoRepeatMode: _Callable[[_Pointer[_enum.Windows.Media.MediaPlaybackAutoRepeatMode]],  # value
                                           _type.HRESULT]


class IImageDisplayProperties(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Subtitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Subtitle: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IMediaControl(_inspectable.IInspectable):
    SoundLevelChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                 _type.HRESULT]
    PlayPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                           _type.HRESULT]
    PausePressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                            _type.HRESULT]
    StopPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                           _type.HRESULT]
    PlayPauseTogglePressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    RecordPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                             _type.HRESULT]
    NextTrackPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                _type.HRESULT]
    PreviousTrackPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    FastForwardPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    RewindPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                             _type.HRESULT]
    ChannelUpPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                _type.HRESULT]
    ChannelDownPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    SoundLevel: _Callable[[_Pointer[_enum.Windows.Media.SoundLevel]],  # value
                          _type.HRESULT]
    TrackName: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    ArtistName: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    IsPlaying: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    AlbumArt: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                        _type.HRESULT]

    _factory = True


class IMediaExtension(_inspectable.IInspectable):
    SetProperties: _Callable[[_Windows_Foundation_Collections.IPropertySet],  # configuration
                             _type.HRESULT]


class IMediaExtensionManager(_inspectable.IInspectable):
    RegisterSchemeHandler: _Callable[[_type.HSTRING,  # activatableClassId
                                      _type.HSTRING],  # scheme
                                     _type.HRESULT]
    RegisterSchemeHandlerWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                                  _type.HSTRING,  # scheme
                                                  _Windows_Foundation_Collections.IPropertySet],  # configuration
                                                 _type.HRESULT]
    RegisterByteStreamHandler: _Callable[[_type.HSTRING,  # activatableClassId
                                          _type.HSTRING,  # fileExtension
                                          _type.HSTRING],  # mimeType
                                         _type.HRESULT]
    RegisterByteStreamHandlerWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                                      _type.HSTRING,  # fileExtension
                                                      _type.HSTRING,  # mimeType
                                                      _Windows_Foundation_Collections.IPropertySet],  # configuration
                                                     _type.HRESULT]
    RegisterAudioDecoder: _Callable[[_type.HSTRING,  # activatableClassId
                                     _struct.GUID,  # inputSubtype
                                     _struct.GUID],  # outputSubtype
                                    _type.HRESULT]
    RegisterAudioDecoderWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                                 _struct.GUID,  # inputSubtype
                                                 _struct.GUID,  # outputSubtype
                                                 _Windows_Foundation_Collections.IPropertySet],  # configuration
                                                _type.HRESULT]
    RegisterAudioEncoder: _Callable[[_type.HSTRING,  # activatableClassId
                                     _struct.GUID,  # inputSubtype
                                     _struct.GUID],  # outputSubtype
                                    _type.HRESULT]
    RegisterAudioEncoderWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                                 _struct.GUID,  # inputSubtype
                                                 _struct.GUID,  # outputSubtype
                                                 _Windows_Foundation_Collections.IPropertySet],  # configuration
                                                _type.HRESULT]
    RegisterVideoDecoder: _Callable[[_type.HSTRING,  # activatableClassId
                                     _struct.GUID,  # inputSubtype
                                     _struct.GUID],  # outputSubtype
                                    _type.HRESULT]
    RegisterVideoDecoderWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                                 _struct.GUID,  # inputSubtype
                                                 _struct.GUID,  # outputSubtype
                                                 _Windows_Foundation_Collections.IPropertySet],  # configuration
                                                _type.HRESULT]
    RegisterVideoEncoder: _Callable[[_type.HSTRING,  # activatableClassId
                                     _struct.GUID,  # inputSubtype
                                     _struct.GUID],  # outputSubtype
                                    _type.HRESULT]
    RegisterVideoEncoderWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                                 _struct.GUID,  # inputSubtype
                                                 _struct.GUID,  # outputSubtype
                                                 _Windows_Foundation_Collections.IPropertySet],  # configuration
                                                _type.HRESULT]


class IMediaExtensionManager2(_inspectable.IInspectable):
    RegisterMediaExtensionForAppService: _Callable[[IMediaExtension,  # extension
                                                    _Windows_ApplicationModel_AppService.IAppServiceConnection],  # connection
                                                   _type.HRESULT]


class IMediaFrame(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_RelativeTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    get_RelativeTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                _type.HRESULT]
    put_SystemRelativeTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    get_SystemRelativeTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                      _type.HRESULT]
    put_Duration: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    put_IsDiscontinuous: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsDiscontinuous: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_ExtendedProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                      _type.HRESULT]


class IMediaMarker(_inspectable.IInspectable):
    get_Time: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]
    get_MediaMarkerType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IMediaMarkerTypesStatics(_inspectable.IInspectable):
    get_Bookmark: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]

    _factory = True


class IMediaMarkers(_inspectable.IInspectable):
    get_Markers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaMarker]]],  # value
                           _type.HRESULT]


class IMediaProcessingTriggerDetails(_inspectable.IInspectable):
    get_Arguments: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                             _type.HRESULT]


class IMediaTimelineController(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_ClockRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_ClockRate: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Media.MediaTimelineControllerState]],  # value
                         _type.HRESULT]
    add_PositionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaTimelineController, _inspectable.IInspectable],  # positionChangedEventHandler
                                    _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                   _type.HRESULT]
    remove_PositionChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                      _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaTimelineController, _inspectable.IInspectable],  # stateChangedEventHandler
                                 _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                   _type.HRESULT]


class IMediaTimelineController2(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_IsLoopingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsLoopingEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    add_Failed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaTimelineController, IMediaTimelineControllerFailedEventArgs],  # eventHandler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Failed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Ended: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaTimelineController, _inspectable.IInspectable],  # eventHandler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Ended: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]


class IMediaTimelineControllerFailedEventArgs(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IMusicDisplayProperties(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_AlbumArtist: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_AlbumArtist: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Artist: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Artist: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]


class IMusicDisplayProperties2(_inspectable.IInspectable):
    get_AlbumTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_AlbumTitle: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_TrackNumber: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_TrackNumber: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_Genres: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                          _type.HRESULT]


class IMusicDisplayProperties3(_inspectable.IInspectable):
    get_AlbumTrackCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    put_AlbumTrackCount: _Callable[[_type.UINT32],  # value
                                   _type.HRESULT]


class IPlaybackPositionChangeRequestedEventArgs(_inspectable.IInspectable):
    get_RequestedPlaybackPosition: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                             _type.HRESULT]


class IPlaybackRateChangeRequestedEventArgs(_inspectable.IInspectable):
    get_RequestedPlaybackRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                         _type.HRESULT]


class IShuffleEnabledChangeRequestedEventArgs(_inspectable.IInspectable):
    get_RequestedShuffleEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class ISystemMediaTransportControls(_inspectable.IInspectable):
    get_PlaybackStatus: _Callable[[_Pointer[_enum.Windows.Media.MediaPlaybackStatus]],  # value
                                  _type.HRESULT]
    put_PlaybackStatus: _Callable[[_enum.Windows.Media.MediaPlaybackStatus],  # value
                                  _type.HRESULT]
    get_DisplayUpdater: _Callable[[_Pointer[ISystemMediaTransportControlsDisplayUpdater]],  # value
                                  _type.HRESULT]
    get_SoundLevel: _Callable[[_Pointer[_enum.Windows.Media.SoundLevel]],  # value
                              _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_IsPlayEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsPlayEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsStopEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsStopEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsPauseEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsPauseEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_IsRecordEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsRecordEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsFastForwardEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsFastForwardEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsRewindEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsRewindEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsPreviousEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsPreviousEnabled: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IsNextEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IsNextEnabled: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_IsChannelUpEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsChannelUpEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_IsChannelDownEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsChannelDownEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    add_ButtonPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemMediaTransportControls, ISystemMediaTransportControlsButtonPressedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ButtonPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_PropertyChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemMediaTransportControls, ISystemMediaTransportControlsPropertyChangedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PropertyChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class ISystemMediaTransportControls2(_inspectable.IInspectable):
    get_AutoRepeatMode: _Callable[[_Pointer[_enum.Windows.Media.MediaPlaybackAutoRepeatMode]],  # value
                                  _type.HRESULT]
    put_AutoRepeatMode: _Callable[[_enum.Windows.Media.MediaPlaybackAutoRepeatMode],  # value
                                  _type.HRESULT]
    get_ShuffleEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_ShuffleEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_PlaybackRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_PlaybackRate: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    UpdateTimelineProperties: _Callable[[ISystemMediaTransportControlsTimelineProperties],  # timelineProperties
                                        _type.HRESULT]
    add_PlaybackPositionChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemMediaTransportControls, IPlaybackPositionChangeRequestedEventArgs],  # handler
                                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                                   _type.HRESULT]
    remove_PlaybackPositionChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                      _type.HRESULT]
    add_PlaybackRateChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemMediaTransportControls, IPlaybackRateChangeRequestedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_PlaybackRateChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_ShuffleEnabledChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemMediaTransportControls, IShuffleEnabledChangeRequestedEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_ShuffleEnabledChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_AutoRepeatModeChangeRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ISystemMediaTransportControls, IAutoRepeatModeChangeRequestedEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_AutoRepeatModeChangeRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]


class ISystemMediaTransportControlsButtonPressedEventArgs(_inspectable.IInspectable):
    get_Button: _Callable[[_Pointer[_enum.Windows.Media.SystemMediaTransportControlsButton]],  # value
                          _type.HRESULT]


class ISystemMediaTransportControlsDisplayUpdater(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Media.MediaPlaybackType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.Media.MediaPlaybackType],  # value
                        _type.HRESULT]
    get_AppMediaId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_AppMediaId: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    put_Thumbnail: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    get_MusicProperties: _Callable[[_Pointer[IMusicDisplayProperties]],  # value
                                   _type.HRESULT]
    get_VideoProperties: _Callable[[_Pointer[IVideoDisplayProperties]],  # value
                                   _type.HRESULT]
    get_ImageProperties: _Callable[[_Pointer[IImageDisplayProperties]],  # value
                                   _type.HRESULT]
    CopyFromFileAsync: _Callable[[_enum.Windows.Media.MediaPlaybackType,  # type
                                  _Windows_Storage.IStorageFile,  # source
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                 _type.HRESULT]
    ClearAll: _Callable[[],
                        _type.HRESULT]
    Update: _Callable[[],
                      _type.HRESULT]


class ISystemMediaTransportControlsPropertyChangedEventArgs(_inspectable.IInspectable):
    get_Property: _Callable[[_Pointer[_enum.Windows.Media.SystemMediaTransportControlsProperty]],  # value
                            _type.HRESULT]


class ISystemMediaTransportControlsStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ISystemMediaTransportControls]],  # mediaControl
                                 _type.HRESULT]

    _factory = True


class ISystemMediaTransportControlsTimelineProperties(_inspectable.IInspectable):
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]
    get_EndTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]
    put_EndTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                           _type.HRESULT]
    get_MinSeekTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    put_MinSeekTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                               _type.HRESULT]
    get_MaxSeekTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    put_MaxSeekTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                               _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]


class IVideoDisplayProperties(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Subtitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Subtitle: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IVideoDisplayProperties2(_inspectable.IInspectable):
    get_Genres: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                          _type.HRESULT]


class IVideoEffectsStatics(_inspectable.IInspectable):
    get_VideoStabilization: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]

    _factory = True


class IVideoFrame(_inspectable.IInspectable):
    get_SoftwareBitmap: _Callable[[_Pointer[_Windows_Graphics_Imaging.ISoftwareBitmap]],  # value
                                  _type.HRESULT]
    CopyToAsync: _Callable[[IVideoFrame,  # frame
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                           _type.HRESULT]
    get_Direct3DSurface: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]],  # value
                                   _type.HRESULT]


class IVideoFrame2(_inspectable.IInspectable):
    CopyToWithBoundsAsync: _Callable[[IVideoFrame,  # frame
                                      _Windows_Foundation.IReference[_struct.Windows.Graphics.Imaging.BitmapBounds],  # sourceBounds
                                      _Windows_Foundation.IReference[_struct.Windows.Graphics.Imaging.BitmapBounds],  # destinationBounds
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                     _type.HRESULT]


class IVideoFrameFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                       _type.INT32,  # width
                       _type.INT32,  # height
                       _Pointer[IVideoFrame]],  # value
                      _type.HRESULT]
    CreateWithAlpha: _Callable[[_enum.Windows.Graphics.Imaging.BitmapPixelFormat,  # format
                                _type.INT32,  # width
                                _type.INT32,  # height
                                _enum.Windows.Graphics.Imaging.BitmapAlphaMode,  # alpha
                                _Pointer[IVideoFrame]],  # value
                               _type.HRESULT]

    _factory = True


class IVideoFrameStatics(_inspectable.IInspectable):
    CreateAsDirect3D11SurfaceBacked: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # format
                                                _type.INT32,  # width
                                                _type.INT32,  # height
                                                _Pointer[IVideoFrame]],  # result
                                               _type.HRESULT]
    CreateAsDirect3D11SurfaceBackedWithDevice: _Callable[[_enum.Windows.Graphics.DirectX.DirectXPixelFormat,  # format
                                                          _type.INT32,  # width
                                                          _type.INT32,  # height
                                                          _Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice,  # device
                                                          _Pointer[IVideoFrame]],  # result
                                                         _type.HRESULT]
    CreateWithSoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # bitmap
                                         _Pointer[IVideoFrame]],  # result
                                        _type.HRESULT]
    CreateWithDirect3D11Surface: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # surface
                                            _Pointer[IVideoFrame]],  # result
                                           _type.HRESULT]

    _factory = True
