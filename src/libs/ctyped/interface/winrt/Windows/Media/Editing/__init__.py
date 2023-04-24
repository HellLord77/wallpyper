from __future__ import annotations

from typing import Callable as _Callable

from .. import Core as _Windows_Media_Core
from .. import Effects as _Windows_Media_Effects
from .. import MediaProperties as _Windows_Media_MediaProperties
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBackgroundAudioTrack(_inspectable.IInspectable):
    get_TrimTimeFromStart: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    put_TrimTimeFromStart: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                     _type.HRESULT]
    get_TrimTimeFromEnd: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_TrimTimeFromEnd: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_OriginalDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                    _type.HRESULT]
    get_TrimmedDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    get_UserData: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                            _type.HRESULT]
    put_Delay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                         _type.HRESULT]
    get_Delay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                         _type.HRESULT]
    put_Volume: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_Volume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    Clone: _Callable[[_Pointer[IBackgroundAudioTrack]],  # value
                     _type.HRESULT]
    GetAudioEncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                          _type.HRESULT]
    get_AudioEffectDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Media_Effects.IAudioEffectDefinition]]],  # value
                                          _type.HRESULT]


class IBackgroundAudioTrackStatics(_inspectable.IInspectable):
    CreateFromEmbeddedAudioTrack: _Callable[[IEmbeddedAudioTrack,  # embeddedAudioTrack
                                             _Pointer[IBackgroundAudioTrack]],  # value
                                            _type.HRESULT]
    CreateFromFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IBackgroundAudioTrack]]],  # operation
                                   _type.HRESULT]

    _factory = True


class IEmbeddedAudioTrack(_inspectable.IInspectable):
    GetAudioEncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                          _type.HRESULT]


class IMediaClip(_inspectable.IInspectable):
    get_TrimTimeFromStart: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    put_TrimTimeFromStart: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                     _type.HRESULT]
    get_TrimTimeFromEnd: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_TrimTimeFromEnd: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_OriginalDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                    _type.HRESULT]
    get_TrimmedDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    get_UserData: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                            _type.HRESULT]
    Clone: _Callable[[_Pointer[IMediaClip]],  # result
                     _type.HRESULT]
    get_StartTimeInComposition: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                          _type.HRESULT]
    get_EndTimeInComposition: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                        _type.HRESULT]
    get_EmbeddedAudioTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IEmbeddedAudioTrack]]],  # value
                                       _type.HRESULT]
    get_SelectedEmbeddedAudioTrackIndex: _Callable[[_Pointer[_type.UINT32]],  # value
                                                   _type.HRESULT]
    put_SelectedEmbeddedAudioTrackIndex: _Callable[[_type.UINT32],  # value
                                                   _type.HRESULT]
    put_Volume: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_Volume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    GetVideoEncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IVideoEncodingProperties]],  # value
                                          _type.HRESULT]
    get_AudioEffectDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Media_Effects.IAudioEffectDefinition]]],  # value
                                          _type.HRESULT]
    get_VideoEffectDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Media_Effects.IVideoEffectDefinition]]],  # value
                                          _type.HRESULT]


class IMediaClipStatics(_inspectable.IInspectable):
    CreateFromColor: _Callable[[_struct.Windows.UI.Color,  # color
                                _struct.Windows.Foundation.TimeSpan,  # originalDuration
                                _Pointer[IMediaClip]],  # value
                               _type.HRESULT]
    CreateFromFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IMediaClip]]],  # operation
                                   _type.HRESULT]
    CreateFromImageFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                         _struct.Windows.Foundation.TimeSpan,  # originalDuration
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IMediaClip]]],  # operation
                                        _type.HRESULT]

    _factory = True


class IMediaClipStatics2(_inspectable.IInspectable):
    CreateFromSurface: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # surface
                                  _struct.Windows.Foundation.TimeSpan,  # originalDuration
                                  _Pointer[IMediaClip]],  # value
                                 _type.HRESULT]

    _factory = True


class IMediaComposition(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Clips: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMediaClip]]],  # value
                         _type.HRESULT]
    get_BackgroundAudioTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IBackgroundAudioTrack]]],  # value
                                         _type.HRESULT]
    get_UserData: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                            _type.HRESULT]
    Clone: _Callable[[_Pointer[IMediaComposition]],  # result
                     _type.HRESULT]
    SaveAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                          _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    GetThumbnailAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # timeFromStart
                                  _type.INT32,  # scaledWidth
                                  _type.INT32,  # scaledHeight
                                  _enum.Windows.Media.Editing.VideoFramePrecision,  # framePrecision
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                 _type.HRESULT]
    GetThumbnailsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Foundation.TimeSpan],  # timesFromStart
                                   _type.INT32,  # scaledWidth
                                   _type.INT32,  # scaledHeight
                                   _enum.Windows.Media.Editing.VideoFramePrecision,  # framePrecision
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]]],  # operation
                                  _type.HRESULT]
    RenderToFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # destination
                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_enum.Windows.Media.Transcoding.TranscodeFailureReason, _type.DOUBLE]]],  # operation
                                 _type.HRESULT]
    RenderToFileWithTrimmingPreferenceAsync: _Callable[[_Windows_Storage.IStorageFile,  # destination
                                                        _enum.Windows.Media.Editing.MediaTrimmingPreference,  # trimmingPreference
                                                        _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_enum.Windows.Media.Transcoding.TranscodeFailureReason, _type.DOUBLE]]],  # operation
                                                       _type.HRESULT]
    RenderToFileWithProfileAsync: _Callable[[_Windows_Storage.IStorageFile,  # destination
                                             _enum.Windows.Media.Editing.MediaTrimmingPreference,  # trimmingPreference
                                             _Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                             _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_enum.Windows.Media.Transcoding.TranscodeFailureReason, _type.DOUBLE]]],  # operation
                                            _type.HRESULT]
    CreateDefaultEncodingProfile: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaEncodingProfile]],  # value
                                            _type.HRESULT]
    GenerateMediaStreamSource: _Callable[[_Pointer[_Windows_Media_Core.IMediaStreamSource]],  # value
                                         _type.HRESULT]
    GenerateMediaStreamSourceWithProfile: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                                     _Pointer[_Windows_Media_Core.IMediaStreamSource]],  # value
                                                    _type.HRESULT]
    GeneratePreviewMediaStreamSource: _Callable[[_type.INT32,  # scaledWidth
                                                 _type.INT32,  # scaledHeight
                                                 _Pointer[_Windows_Media_Core.IMediaStreamSource]],  # value
                                                _type.HRESULT]


class IMediaComposition2(_inspectable.IInspectable):
    get_OverlayLayers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMediaOverlayLayer]]],  # value
                                 _type.HRESULT]


class IMediaCompositionStatics(_inspectable.IInspectable):
    LoadAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                          _Pointer[_Windows_Foundation.IAsyncOperation[IMediaComposition]]],  # operation
                         _type.HRESULT]

    _factory = True


class IMediaOverlay(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.Rect],  # value
                            _type.HRESULT]
    put_Delay: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                         _type.HRESULT]
    get_Delay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                         _type.HRESULT]
    get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Opacity: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    Clone: _Callable[[_Pointer[IMediaOverlay]],  # result
                     _type.HRESULT]
    get_Clip: _Callable[[_Pointer[IMediaClip]],  # value
                        _type.HRESULT]
    get_AudioEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_AudioEnabled: _Callable[[_type.boolean],  # value
                                _type.HRESULT]


class IMediaOverlayFactory(_inspectable.IInspectable):
    Create: _Callable[[IMediaClip,  # clip
                       _Pointer[IMediaOverlay]],  # mediaOverlay
                      _type.HRESULT]
    CreateWithPositionAndOpacity: _Callable[[IMediaClip,  # clip
                                             _struct.Windows.Foundation.Rect,  # position
                                             _type.DOUBLE,  # opacity
                                             _Pointer[IMediaOverlay]],  # mediaOverlay
                                            _type.HRESULT]

    _factory = True


class IMediaOverlayLayer(_inspectable.IInspectable):
    Clone: _Callable[[_Pointer[IMediaOverlayLayer]],  # result
                     _type.HRESULT]
    get_Overlays: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IMediaOverlay]]],  # value
                            _type.HRESULT]
    get_CustomCompositorDefinition: _Callable[[_Pointer[_Windows_Media_Effects.IVideoCompositorDefinition]],  # value
                                              _type.HRESULT]


class IMediaOverlayLayerFactory(_inspectable.IInspectable):
    CreateWithCompositorDefinition: _Callable[[_Windows_Media_Effects.IVideoCompositorDefinition,  # compositorDefinition
                                               _Pointer[IMediaOverlayLayer]],  # mediaOverlayLayer
                                              _type.HRESULT]

    _factory = True
