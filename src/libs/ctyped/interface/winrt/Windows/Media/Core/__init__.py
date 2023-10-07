from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Capture as _Windows_Media_Capture
from .. import Devices as _Windows_Media_Devices
from .. import FaceAnalysis as _Windows_Media_FaceAnalysis
from .. import MediaProperties as _Windows_Media_MediaProperties
from .. import Playback as _Windows_Media_Playback
from .. import Protection as _Windows_Media_Protection
from ..Capture import Frames as _Windows_Media_Capture_Frames
from ..Devices import Core as _Windows_Media_Devices_Core
from ..Streaming import Adaptive as _Windows_Media_Streaming_Adaptive
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...ApplicationModel import AppService as _Windows_ApplicationModel_AppService
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Imaging as _Windows_Graphics_Imaging
from ...Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ...Networking import BackgroundTransfer as _Windows_Networking_BackgroundTransfer
from ...Storage import FileProperties as _Windows_Storage_FileProperties
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAudioStreamDescriptor(_inspectable.IInspectable):
    get_EncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # encodingProperties
                                      _type.HRESULT]


class IAudioStreamDescriptor2(_inspectable.IInspectable):
    put_LeadingEncoderPadding: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                         _type.HRESULT]
    get_LeadingEncoderPadding: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                         _type.HRESULT]
    put_TrailingEncoderPadding: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_TrailingEncoderPadding: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                          _type.HRESULT]


class IAudioStreamDescriptor3(_inspectable.IInspectable):
    Copy: _Callable[[_Pointer[IAudioStreamDescriptor]],  # result
                    _type.HRESULT]


class IAudioStreamDescriptorFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                       _Pointer[IAudioStreamDescriptor]],  # result
                      _type.HRESULT]


class IAudioTrack(_inspectable.IInspectable):
    add_OpenFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaTrack, IAudioTrackOpenFailedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_OpenFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    GetEncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                     _type.HRESULT]
    get_PlaybackItem: _Callable[[_Pointer[_Windows_Media_Playback.IMediaPlaybackItem]],  # value
                                _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_SupportInfo: _Callable[[_Pointer[IAudioTrackSupportInfo]],  # value
                               _type.HRESULT]


class IAudioTrackOpenFailedEventArgs(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IAudioTrackSupportInfo(_inspectable.IInspectable):
    get_DecoderStatus: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaDecoderStatus]],  # value
                                 _type.HRESULT]
    get_Degradation: _Callable[[_Pointer[_enum.Windows.Media.Core.AudioDecoderDegradation]],  # value
                               _type.HRESULT]
    get_DegradationReason: _Callable[[_Pointer[_enum.Windows.Media.Core.AudioDecoderDegradationReason]],  # value
                                     _type.HRESULT]
    get_MediaSourceStatus: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaSourceStatus]],  # value
                                     _type.HRESULT]


class IChapterCue(_inspectable.IInspectable):
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class ICodecInfo(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Media.Core.CodecKind]],  # value
                        _type.HRESULT]
    get_Category: _Callable[[_Pointer[_enum.Windows.Media.Core.CodecCategory]],  # value
                            _type.HRESULT]
    get_Subtypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsTrusted: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class ICodecQuery(_inspectable.IInspectable):
    FindAllAsync: _Callable[[_enum.Windows.Media.Core.CodecKind,  # kind
                             _enum.Windows.Media.Core.CodecCategory,  # category
                             _type.HSTRING,  # subType
                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ICodecInfo]]]],  # value
                            _type.HRESULT]


class ICodecSubtypesStatics(_inspectable.IInspectable, factory=True):
    get_VideoFormatDV25: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatDV50: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatDvc: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_VideoFormatDvh1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatDvhD: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatDvsd: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatDvsl: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatH263: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatH264: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatH265: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatH264ES: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_VideoFormatHevc: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatHevcES: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_VideoFormatM4S2: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMjpg: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMP43: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMP4S: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMP4V: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMpeg2: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_VideoFormatVP80: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatVP90: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMpg1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMss1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatMss2: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatWmv1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatWmv2: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatWmv3: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormatWvc1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_VideoFormat420O: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AudioFormatAac: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AudioFormatAdts: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AudioFormatAlac: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AudioFormatAmrNB: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_AudioFormatAmrWB: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_AudioFormatAmrWP: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_AudioFormatDolbyAC3: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_AudioFormatDolbyAC3Spdif: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    get_AudioFormatDolbyDDPlus: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_AudioFormatDrm: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AudioFormatDts: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AudioFormatFlac: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AudioFormatFloat: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_AudioFormatMP3: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AudioFormatMPeg: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AudioFormatMsp1: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AudioFormatOpus: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_AudioFormatPcm: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_AudioFormatWmaSpdif: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_AudioFormatWMAudioLossless: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_AudioFormatWMAudioV8: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_AudioFormatWMAudioV9: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]


class IDataCue(_inspectable.IInspectable):
    put_Data: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                        _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]


class IDataCue2(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class IFaceDetectedEventArgs(_inspectable.IInspectable):
    get_ResultFrame: _Callable[[_Pointer[IFaceDetectionEffectFrame]],  # value
                               _type.HRESULT]


class IFaceDetectionEffect(_inspectable.IInspectable):
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_DesiredDetectionInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                            _type.HRESULT]
    get_DesiredDetectionInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                            _type.HRESULT]
    add_FaceDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[IFaceDetectionEffect, IFaceDetectedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_FaceDetected: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]


class IFaceDetectionEffectDefinition(_inspectable.IInspectable):
    put_DetectionMode: _Callable[[_enum.Windows.Media.Core.FaceDetectionMode],  # value
                                 _type.HRESULT]
    get_DetectionMode: _Callable[[_Pointer[_enum.Windows.Media.Core.FaceDetectionMode]],  # value
                                 _type.HRESULT]
    put_SynchronousDetectionEnabled: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_SynchronousDetectionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IFaceDetectionEffectFrame(_inspectable.IInspectable):
    get_DetectedFaces: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_FaceAnalysis.IDetectedFace]]],  # value
                                 _type.HRESULT]


class IHighDynamicRangeControl(_inspectable.IInspectable):
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]


class IHighDynamicRangeOutput(_inspectable.IInspectable):
    get_Certainty: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    get_FrameControllers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_Devices_Core.IFrameController]]],  # value
                                    _type.HRESULT]


class IImageCue(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextPoint]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Media.Core.TimedTextPoint],  # value
                            _type.HRESULT]
    get_Extent: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextSize]],  # value
                          _type.HRESULT]
    put_Extent: _Callable[[_struct.Windows.Media.Core.TimedTextSize],  # value
                          _type.HRESULT]
    put_SoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # value
                                  _type.HRESULT]
    get_SoftwareBitmap: _Callable[[_Pointer[_Windows_Graphics_Imaging.ISoftwareBitmap]],  # value
                                  _type.HRESULT]


class IInitializeMediaStreamSourceRequestedEventArgs(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[IMediaStreamSource]],  # value
                          _type.HRESULT]
    get_RandomAccessStream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ILowLightFusionResult(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[_Windows_Graphics_Imaging.ISoftwareBitmap]],  # value
                         _type.HRESULT]


class ILowLightFusionStatics(_inspectable.IInspectable, factory=True):
    get_SupportedBitmapPixelFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]]],  # value
                                               _type.HRESULT]
    get_MaxSupportedFrameCount: _Callable[[_Pointer[_type.INT32]],  # value
                                          _type.HRESULT]
    FuseAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Graphics_Imaging.ISoftwareBitmap],  # frameSet
                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[ILowLightFusionResult, _type.DOUBLE]]],  # result
                         _type.HRESULT]


class IMediaBinder(_inspectable.IInspectable):
    add_Binding: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaBinder, IMediaBindingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Binding: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Token: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Token: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Source: _Callable[[_Pointer[IMediaSource2]],  # value
                          _type.HRESULT]


class IMediaBindingEventArgs(_inspectable.IInspectable):
    add_Canceled: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaBindingEventArgs, _inspectable.IInspectable],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Canceled: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    get_MediaBinder: _Callable[[_Pointer[IMediaBinder]],  # value
                               _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # deferral
                           _type.HRESULT]
    SetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # uri
                      _type.HRESULT]
    SetStream: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                          _type.HSTRING],  # contentType
                         _type.HRESULT]
    SetStreamReference: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # stream
                                   _type.HSTRING],  # contentType
                                  _type.HRESULT]


class IMediaBindingEventArgs2(_inspectable.IInspectable):
    SetAdaptiveMediaSource: _Callable[[_Windows_Media_Streaming_Adaptive.IAdaptiveMediaSource],  # mediaSource
                                      _type.HRESULT]
    SetStorageFile: _Callable[[_Windows_Storage.IStorageFile],  # file
                              _type.HRESULT]


class IMediaBindingEventArgs3(_inspectable.IInspectable):
    SetDownloadOperation: _Callable[[_Windows_Networking_BackgroundTransfer.IDownloadOperation],  # downloadOperation
                                    _type.HRESULT]


class IMediaCue(_inspectable.IInspectable):
    put_StartTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]


class IMediaCueEventArgs(_inspectable.IInspectable):
    get_Cue: _Callable[[_Pointer[IMediaCue]],  # value
                       _type.HRESULT]


class IMediaSource(_inspectable.IInspectable):
    pass


class IMediaSource2(_inspectable.IInspectable):
    add_OpenOperationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaSource2, IMediaSourceOpenOperationCompletedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_OpenOperationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    get_CustomProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                    _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    get_IsOpen: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_ExternalTimedTextSources: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[ITimedTextSource]]],  # value
                                            _type.HRESULT]
    get_ExternalTimedMetadataTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[ITimedMetadataTrack]]],  # value
                                               _type.HRESULT]


class IMediaSource3(_inspectable.IInspectable):
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaSource2, IMediaSourceStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaSourceState]],  # value
                         _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class IMediaSource4(_inspectable.IInspectable):
    get_AdaptiveMediaSource: _Callable[[_Pointer[_Windows_Media_Streaming_Adaptive.IAdaptiveMediaSource]],  # value
                                       _type.HRESULT]
    get_MediaStreamSource: _Callable[[_Pointer[IMediaStreamSource]],  # value
                                     _type.HRESULT]
    get_MseStreamSource: _Callable[[_Pointer[IMseStreamSource]],  # value
                                   _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    OpenAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]


class IMediaSource5(_inspectable.IInspectable):
    get_DownloadOperation: _Callable[[_Pointer[_Windows_Networking_BackgroundTransfer.IDownloadOperation]],  # value
                                     _type.HRESULT]


class IMediaSourceAppServiceConnection(_inspectable.IInspectable):
    add_InitializeMediaStreamSourceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaSourceAppServiceConnection, IInitializeMediaStreamSourceRequestedEventArgs],  # handler
                                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                                        _type.HRESULT]
    remove_InitializeMediaStreamSourceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                           _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IMediaSourceAppServiceConnectionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_ApplicationModel_AppService.IAppServiceConnection,  # appServiceConnection
                       _Pointer[IMediaSourceAppServiceConnection]],  # result
                      _type.HRESULT]


class IMediaSourceError(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IMediaSourceOpenOperationCompletedEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[IMediaSourceError]],  # value
                         _type.HRESULT]


class IMediaSourceStateChangedEventArgs(_inspectable.IInspectable):
    get_OldState: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaSourceState]],  # value
                            _type.HRESULT]
    get_NewState: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaSourceState]],  # value
                            _type.HRESULT]


class IMediaSourceStatics(_inspectable.IInspectable, factory=True):
    CreateFromAdaptiveMediaSource: _Callable[[_Windows_Media_Streaming_Adaptive.IAdaptiveMediaSource,  # mediaSource
                                              _Pointer[IMediaSource2]],  # result
                                             _type.HRESULT]
    CreateFromMediaStreamSource: _Callable[[IMediaStreamSource,  # mediaSource
                                            _Pointer[IMediaSource2]],  # result
                                           _type.HRESULT]
    CreateFromMseStreamSource: _Callable[[IMseStreamSource,  # mediaSource
                                          _Pointer[IMediaSource2]],  # result
                                         _type.HRESULT]
    CreateFromIMediaSource: _Callable[[IMediaSource,  # mediaSource
                                       _Pointer[IMediaSource2]],  # result
                                      _type.HRESULT]
    CreateFromStorageFile: _Callable[[_Windows_Storage.IStorageFile,  # file
                                      _Pointer[IMediaSource2]],  # result
                                     _type.HRESULT]
    CreateFromStream: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                 _type.HSTRING,  # contentType
                                 _Pointer[IMediaSource2]],  # result
                                _type.HRESULT]
    CreateFromStreamReference: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # stream
                                          _type.HSTRING,  # contentType
                                          _Pointer[IMediaSource2]],  # result
                                         _type.HRESULT]
    CreateFromUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                              _Pointer[IMediaSource2]],  # result
                             _type.HRESULT]


class IMediaSourceStatics2(_inspectable.IInspectable, factory=True):
    CreateFromMediaBinder: _Callable[[IMediaBinder,  # binder
                                      _Pointer[IMediaSource2]],  # result
                                     _type.HRESULT]


class IMediaSourceStatics3(_inspectable.IInspectable, factory=True):
    CreateFromMediaFrameSource: _Callable[[_Windows_Media_Capture_Frames.IMediaFrameSource,  # frameSource
                                           _Pointer[IMediaSource2]],  # result
                                          _type.HRESULT]


class IMediaSourceStatics4(_inspectable.IInspectable, factory=True):
    CreateFromDownloadOperation: _Callable[[_Windows_Networking_BackgroundTransfer.IDownloadOperation,  # downloadOperation
                                            _Pointer[IMediaSource2]],  # result
                                           _type.HRESULT]


class IMediaStreamDescriptor(_inspectable.IInspectable):
    get_IsSelected: _Callable[[_Pointer[_type.boolean]],  # selected
                              _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IMediaStreamDescriptor2(_inspectable.IInspectable):
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IMediaStreamSample(_inspectable.IInspectable):
    add_Processed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaStreamSample, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Processed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    get_Buffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                          _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_ExtendedProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_struct.GUID, _inspectable.IInspectable]]],  # value
                                      _type.HRESULT]
    get_Protection: _Callable[[_Pointer[IMediaStreamSampleProtectionProperties]],  # value
                              _type.HRESULT]
    put_DecodeTimestamp: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_DecodeTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_KeyFrame: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_KeyFrame: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_Discontinuous: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_Discontinuous: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IMediaStreamSample2(_inspectable.IInspectable):
    get_Direct3D11Surface: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface]],  # value
                                     _type.HRESULT]


class IMediaStreamSampleProtectionProperties(_inspectable.IInspectable):
    SetKeyIdentifier: _Callable[[_type.UINT32,  # __valueSize
                                 _Pointer[_type.BYTE]],  # value
                                _type.HRESULT]
    GetKeyIdentifier: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                 _Pointer[_Pointer[_type.BYTE]]],  # value
                                _type.HRESULT]
    SetInitializationVector: _Callable[[_type.UINT32,  # __valueSize
                                        _Pointer[_type.BYTE]],  # value
                                       _type.HRESULT]
    GetInitializationVector: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                        _Pointer[_Pointer[_type.BYTE]]],  # value
                                       _type.HRESULT]
    SetSubSampleMapping: _Callable[[_type.UINT32,  # __valueSize
                                    _Pointer[_type.BYTE]],  # value
                                   _type.HRESULT]
    GetSubSampleMapping: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                    _Pointer[_Pointer[_type.BYTE]]],  # value
                                   _type.HRESULT]


class IMediaStreamSampleStatics(_inspectable.IInspectable, factory=True):
    CreateFromBuffer: _Callable[[_Windows_Storage_Streams.IBuffer,  # buffer
                                 _struct.Windows.Foundation.TimeSpan,  # timestamp
                                 _Pointer[IMediaStreamSample]],  # value
                                _type.HRESULT]
    CreateFromStreamAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # stream
                                      _type.UINT32,  # count
                                      _struct.Windows.Foundation.TimeSpan,  # timestamp
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IMediaStreamSample]]],  # value
                                     _type.HRESULT]


class IMediaStreamSampleStatics2(_inspectable.IInspectable, factory=True):
    CreateFromDirect3D11Surface: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DSurface,  # surface
                                            _struct.Windows.Foundation.TimeSpan,  # timestamp
                                            _Pointer[IMediaStreamSample]],  # result
                                           _type.HRESULT]


class IMediaStreamSource(_inspectable.IInspectable):
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaStreamSource, IMediaStreamSourceClosedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Starting: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaStreamSource, IMediaStreamSourceStartingEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Starting: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_Paused: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaStreamSource, _inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Paused: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_SampleRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaStreamSource, IMediaStreamSourceSampleRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_SampleRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_SwitchStreamsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaStreamSource, IMediaStreamSourceSwitchStreamsRequestedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_SwitchStreamsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    NotifyError: _Callable[[_enum.Windows.Media.Core.MediaStreamSourceErrorStatus],  # errorStatus
                           _type.HRESULT]
    AddStreamDescriptor: _Callable[[IMediaStreamDescriptor],  # descriptor
                                   _type.HRESULT]
    put_MediaProtectionManager: _Callable[[_Windows_Media_Protection.IMediaProtectionManager],  # value
                                          _type.HRESULT]
    get_MediaProtectionManager: _Callable[[_Pointer[_Windows_Media_Protection.IMediaProtectionManager]],  # value
                                          _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_CanSeek: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_CanSeek: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_BufferTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                              _type.HRESULT]
    get_BufferTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    SetBufferedRange: _Callable[[_struct.Windows.Foundation.TimeSpan,  # startOffset
                                 _struct.Windows.Foundation.TimeSpan],  # endOffset
                                _type.HRESULT]
    get_MusicProperties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IMusicProperties]],  # value
                                   _type.HRESULT]
    get_VideoProperties: _Callable[[_Pointer[_Windows_Storage_FileProperties.IVideoProperties]],  # value
                                   _type.HRESULT]
    put_Thumbnail: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    AddProtectionKey: _Callable[[IMediaStreamDescriptor,  # streamDescriptor
                                 _type.UINT32,  # __keyIdentifierSize
                                 _Pointer[_type.BYTE],  # keyIdentifier
                                 _type.UINT32,  # __licenseDataSize
                                 _Pointer[_type.BYTE]],  # licenseData
                                _type.HRESULT]


class IMediaStreamSource2(_inspectable.IInspectable):
    add_SampleRendered: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaStreamSource, IMediaStreamSourceSampleRenderedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_SampleRendered: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IMediaStreamSource3(_inspectable.IInspectable):
    put_MaxSupportedPlaybackRate: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                                            _type.HRESULT]
    get_MaxSupportedPlaybackRate: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                            _type.HRESULT]


class IMediaStreamSource4(_inspectable.IInspectable):
    put_IsLive: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_IsLive: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]


class IMediaStreamSourceClosedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IMediaStreamSourceClosedRequest]],  # value
                           _type.HRESULT]


class IMediaStreamSourceClosedRequest(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaStreamSourceClosedReason]],  # value
                          _type.HRESULT]


class IMediaStreamSourceFactory(_inspectable.IInspectable, factory=True):
    CreateFromDescriptor: _Callable[[IMediaStreamDescriptor,  # descriptor
                                     _Pointer[IMediaStreamSource]],  # result
                                    _type.HRESULT]
    CreateFromDescriptors: _Callable[[IMediaStreamDescriptor,  # descriptor
                                      IMediaStreamDescriptor,  # descriptor2
                                      _Pointer[IMediaStreamSource]],  # result
                                     _type.HRESULT]


class IMediaStreamSourceSampleRenderedEventArgs(_inspectable.IInspectable):
    get_SampleLag: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]


class IMediaStreamSourceSampleRequest(_inspectable.IInspectable):
    get_StreamDescriptor: _Callable[[_Pointer[IMediaStreamDescriptor]],  # value
                                    _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IMediaStreamSourceSampleRequestDeferral]],  # deferral
                           _type.HRESULT]
    put_Sample: _Callable[[IMediaStreamSample],  # value
                          _type.HRESULT]
    get_Sample: _Callable[[_Pointer[IMediaStreamSample]],  # value
                          _type.HRESULT]
    ReportSampleProgress: _Callable[[_type.UINT32],  # progress
                                    _type.HRESULT]


class IMediaStreamSourceSampleRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IMediaStreamSourceSampleRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IMediaStreamSourceSampleRequest]],  # value
                           _type.HRESULT]


class IMediaStreamSourceStartingEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IMediaStreamSourceStartingRequest]],  # value
                           _type.HRESULT]


class IMediaStreamSourceStartingRequest(_inspectable.IInspectable):
    get_StartPosition: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                 _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IMediaStreamSourceStartingRequestDeferral]],  # deferral
                           _type.HRESULT]
    SetActualStartPosition: _Callable[[_struct.Windows.Foundation.TimeSpan],  # position
                                      _type.HRESULT]


class IMediaStreamSourceStartingRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IMediaStreamSourceSwitchStreamsRequest(_inspectable.IInspectable):
    get_OldStreamDescriptor: _Callable[[_Pointer[IMediaStreamDescriptor]],  # value
                                       _type.HRESULT]
    get_NewStreamDescriptor: _Callable[[_Pointer[IMediaStreamDescriptor]],  # value
                                       _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IMediaStreamSourceSwitchStreamsRequestDeferral]],  # deferral
                           _type.HRESULT]


class IMediaStreamSourceSwitchStreamsRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IMediaStreamSourceSwitchStreamsRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IMediaStreamSourceSwitchStreamsRequest]],  # value
                           _type.HRESULT]


class IMediaTrack(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_TrackKind: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaTrackKind]],  # value
                             _type.HRESULT]
    put_Label: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IMseSourceBuffer(_inspectable.IInspectable):
    add_UpdateStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseSourceBuffer, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_UpdateStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseSourceBuffer, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_UpdateEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseSourceBuffer, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_UpdateEnded: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_ErrorOccurred: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseSourceBuffer, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ErrorOccurred: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_Aborted: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseSourceBuffer, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Aborted: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Core.MseAppendMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Core.MseAppendMode],  # value
                        _type.HRESULT]
    get_IsUpdating: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Buffered: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Media.Core.MseTimeRange]]],  # value
                            _type.HRESULT]
    get_TimestampOffset: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    put_TimestampOffset: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                   _type.HRESULT]
    get_AppendWindowStart: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    put_AppendWindowStart: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                     _type.HRESULT]
    get_AppendWindowEnd: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                   _type.HRESULT]
    put_AppendWindowEnd: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                   _type.HRESULT]
    AppendBuffer: _Callable[[_Windows_Storage_Streams.IBuffer],  # buffer
                            _type.HRESULT]
    AppendStream: _Callable[[_Windows_Storage_Streams.IInputStream],  # stream
                            _type.HRESULT]
    AppendStreamMaxSize: _Callable[[_Windows_Storage_Streams.IInputStream,  # stream
                                    _type.UINT64],  # maxSize
                                   _type.HRESULT]
    Abort: _Callable[[],
                     _type.HRESULT]
    Remove: _Callable[[_struct.Windows.Foundation.TimeSpan,  # start
                       _Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # end
                      _type.HRESULT]


class IMseSourceBufferList(_inspectable.IInspectable):
    add_SourceBufferAdded: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseSourceBufferList, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SourceBufferAdded: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_SourceBufferRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseSourceBufferList, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_SourceBufferRemoved: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    get_Buffers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMseSourceBuffer]]],  # value
                           _type.HRESULT]


class IMseStreamSource(_inspectable.IInspectable):
    add_Opened: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseStreamSource, _inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Opened: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    add_Ended: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseStreamSource, _inspectable.IInspectable],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Ended: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Closed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMseStreamSource, _inspectable.IInspectable],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Closed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]
    get_SourceBuffers: _Callable[[_Pointer[IMseSourceBufferList]],  # value
                                 _type.HRESULT]
    get_ActiveSourceBuffers: _Callable[[_Pointer[IMseSourceBufferList]],  # value
                                       _type.HRESULT]
    get_ReadyState: _Callable[[_Pointer[_enum.Windows.Media.Core.MseReadyState]],  # value
                              _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    AddSourceBuffer: _Callable[[_type.HSTRING,  # mimeType
                                _Pointer[IMseSourceBuffer]],  # buffer
                               _type.HRESULT]
    RemoveSourceBuffer: _Callable[[IMseSourceBuffer],  # buffer
                                  _type.HRESULT]
    EndOfStream: _Callable[[_enum.Windows.Media.Core.MseEndOfStreamStatus],  # status
                           _type.HRESULT]


class IMseStreamSource2(_inspectable.IInspectable):
    get_LiveSeekableRange: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Media.Core.MseTimeRange]]],  # value
                                     _type.HRESULT]
    put_LiveSeekableRange: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Media.Core.MseTimeRange]],  # value
                                     _type.HRESULT]


class IMseStreamSourceStatics(_inspectable.IInspectable, factory=True):
    IsContentTypeSupported: _Callable[[_type.HSTRING,  # contentType
                                       _Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class ISceneAnalysisEffect(_inspectable.IInspectable):
    get_HighDynamicRangeAnalyzer: _Callable[[_Pointer[IHighDynamicRangeControl]],  # value
                                            _type.HRESULT]
    put_DesiredAnalysisInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                           _type.HRESULT]
    get_DesiredAnalysisInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                           _type.HRESULT]
    add_SceneAnalyzed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISceneAnalysisEffect, ISceneAnalyzedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_SceneAnalyzed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]


class ISceneAnalysisEffectFrame(_inspectable.IInspectable):
    get_FrameControlValues: _Callable[[_Pointer[_Windows_Media_Capture.ICapturedFrameControlValues]],  # value
                                      _type.HRESULT]
    get_HighDynamicRange: _Callable[[_Pointer[IHighDynamicRangeOutput]],  # value
                                    _type.HRESULT]


class ISceneAnalysisEffectFrame2(_inspectable.IInspectable):
    get_AnalysisRecommendation: _Callable[[_Pointer[_enum.Windows.Media.Core.SceneAnalysisRecommendation]],  # value
                                          _type.HRESULT]


class ISceneAnalyzedEventArgs(_inspectable.IInspectable):
    get_ResultFrame: _Callable[[_Pointer[ISceneAnalysisEffectFrame]],  # value
                               _type.HRESULT]


class ISingleSelectMediaTrackList(_inspectable.IInspectable):
    add_SelectedIndexChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISingleSelectMediaTrackList, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SelectedIndexChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    put_SelectedIndex: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_SelectedIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]


class ISpeechCue(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_StartPositionInInput: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                        _type.HRESULT]
    put_StartPositionInInput: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                        _type.HRESULT]
    get_EndPositionInInput: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                      _type.HRESULT]
    put_EndPositionInInput: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                      _type.HRESULT]


class ITimedMetadataStreamDescriptor(_inspectable.IInspectable):
    get_EncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaEncodingProperties]],  # value
                                      _type.HRESULT]
    Copy: _Callable[[_Pointer[IMediaStreamDescriptor]],  # result
                    _type.HRESULT]


class ITimedMetadataStreamDescriptorFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProperties,  # encodingProperties
                       _Pointer[IMediaStreamDescriptor]],  # result
                      _type.HRESULT]


class ITimedMetadataTrack(_inspectable.IInspectable):
    add_CueEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[ITimedMetadataTrack, IMediaCueEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_CueEntered: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    add_CueExited: _Callable[[_Windows_Foundation.ITypedEventHandler[ITimedMetadataTrack, IMediaCueEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_CueExited: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_TrackFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[ITimedMetadataTrack, ITimedMetadataTrackFailedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_TrackFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    get_Cues: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCue]]],  # value
                        _type.HRESULT]
    get_ActiveCues: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCue]]],  # value
                              _type.HRESULT]
    get_TimedMetadataKind: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedMetadataKind]],  # value
                                     _type.HRESULT]
    get_DispatchType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    AddCue: _Callable[[IMediaCue],  # cue
                      _type.HRESULT]
    RemoveCue: _Callable[[IMediaCue],  # cue
                         _type.HRESULT]


class ITimedMetadataTrack2(_inspectable.IInspectable):
    get_PlaybackItem: _Callable[[_Pointer[_Windows_Media_Playback.IMediaPlaybackItem]],  # value
                                _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ITimedMetadataTrackError(_inspectable.IInspectable):
    get_ErrorCode: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedMetadataTrackErrorCode]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class ITimedMetadataTrackFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # id
                       _type.HSTRING,  # language
                       _enum.Windows.Media.Core.TimedMetadataKind,  # kind
                       _Pointer[ITimedMetadataTrack]],  # value
                      _type.HRESULT]


class ITimedMetadataTrackFailedEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[ITimedMetadataTrackError]],  # value
                         _type.HRESULT]


class ITimedMetadataTrackProvider(_inspectable.IInspectable):
    get_TimedMetadataTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ITimedMetadataTrack]]],  # value
                                       _type.HRESULT]


class ITimedTextBouten(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextBoutenType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.Media.Core.TimedTextBoutenType],  # value
                        _type.HRESULT]
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_Position: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextBoutenPosition]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_enum.Windows.Media.Core.TimedTextBoutenPosition],  # value
                            _type.HRESULT]


class ITimedTextCue(_inspectable.IInspectable):
    get_CueRegion: _Callable[[_Pointer[ITimedTextRegion]],  # value
                             _type.HRESULT]
    put_CueRegion: _Callable[[ITimedTextRegion],  # value
                             _type.HRESULT]
    get_CueStyle: _Callable[[_Pointer[ITimedTextStyle]],  # value
                            _type.HRESULT]
    put_CueStyle: _Callable[[ITimedTextStyle],  # value
                            _type.HRESULT]
    get_Lines: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITimedTextLine]]],  # value
                         _type.HRESULT]


class ITimedTextLine(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Subformats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ITimedTextSubformat]]],  # value
                              _type.HRESULT]


class ITimedTextRegion(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextPoint]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Media.Core.TimedTextPoint],  # value
                            _type.HRESULT]
    get_Extent: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextSize]],  # value
                          _type.HRESULT]
    put_Extent: _Callable[[_struct.Windows.Media.Core.TimedTextSize],  # value
                          _type.HRESULT]
    get_Background: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_struct.Windows.UI.Color],  # value
                              _type.HRESULT]
    get_WritingMode: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextWritingMode]],  # value
                               _type.HRESULT]
    put_WritingMode: _Callable[[_enum.Windows.Media.Core.TimedTextWritingMode],  # value
                               _type.HRESULT]
    get_DisplayAlignment: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextDisplayAlignment]],  # value
                                    _type.HRESULT]
    put_DisplayAlignment: _Callable[[_enum.Windows.Media.Core.TimedTextDisplayAlignment],  # value
                                    _type.HRESULT]
    get_LineHeight: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextDouble]],  # value
                              _type.HRESULT]
    put_LineHeight: _Callable[[_struct.Windows.Media.Core.TimedTextDouble],  # value
                              _type.HRESULT]
    get_IsOverflowClipped: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsOverflowClipped: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_Padding: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextPadding]],  # value
                           _type.HRESULT]
    put_Padding: _Callable[[_struct.Windows.Media.Core.TimedTextPadding],  # value
                           _type.HRESULT]
    get_TextWrapping: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextWrapping]],  # value
                                _type.HRESULT]
    put_TextWrapping: _Callable[[_enum.Windows.Media.Core.TimedTextWrapping],  # value
                                _type.HRESULT]
    get_ZIndex: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_ZIndex: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_ScrollMode: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextScrollMode]],  # value
                              _type.HRESULT]
    put_ScrollMode: _Callable[[_enum.Windows.Media.Core.TimedTextScrollMode],  # value
                              _type.HRESULT]


class ITimedTextRuby(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Position: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextRubyPosition]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_enum.Windows.Media.Core.TimedTextRubyPosition],  # value
                            _type.HRESULT]
    get_Align: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextRubyAlign]],  # value
                         _type.HRESULT]
    put_Align: _Callable[[_enum.Windows.Media.Core.TimedTextRubyAlign],  # value
                         _type.HRESULT]
    get_Reserve: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextRubyReserve]],  # value
                           _type.HRESULT]
    put_Reserve: _Callable[[_enum.Windows.Media.Core.TimedTextRubyReserve],  # value
                           _type.HRESULT]


class ITimedTextSource(_inspectable.IInspectable):
    add_Resolved: _Callable[[_Windows_Foundation.ITypedEventHandler[ITimedTextSource, ITimedTextSourceResolveResultEventArgs],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Resolved: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]


class ITimedTextSourceResolveResultEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[ITimedMetadataTrackError]],  # value
                         _type.HRESULT]
    get_Tracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ITimedMetadataTrack]]],  # value
                          _type.HRESULT]


class ITimedTextSourceStatics(_inspectable.IInspectable, factory=True):
    CreateFromStream: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                 _Pointer[ITimedTextSource]],  # value
                                _type.HRESULT]
    CreateFromUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                              _Pointer[ITimedTextSource]],  # value
                             _type.HRESULT]
    CreateFromStreamWithLanguage: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                             _type.HSTRING,  # defaultLanguage
                                             _Pointer[ITimedTextSource]],  # value
                                            _type.HRESULT]
    CreateFromUriWithLanguage: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                          _type.HSTRING,  # defaultLanguage
                                          _Pointer[ITimedTextSource]],  # value
                                         _type.HRESULT]


class ITimedTextSourceStatics2(_inspectable.IInspectable, factory=True):
    CreateFromStreamWithIndex: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                          _Windows_Storage_Streams.IRandomAccessStream,  # indexStream
                                          _Pointer[ITimedTextSource]],  # result
                                         _type.HRESULT]
    CreateFromUriWithIndex: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                       _Windows_Foundation.IUriRuntimeClass,  # indexUri
                                       _Pointer[ITimedTextSource]],  # result
                                      _type.HRESULT]
    CreateFromStreamWithIndexAndLanguage: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                                     _Windows_Storage_Streams.IRandomAccessStream,  # indexStream
                                                     _type.HSTRING,  # defaultLanguage
                                                     _Pointer[ITimedTextSource]],  # result
                                                    _type.HRESULT]
    CreateFromUriWithIndexAndLanguage: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                                  _Windows_Foundation.IUriRuntimeClass,  # indexUri
                                                  _type.HSTRING,  # defaultLanguage
                                                  _Pointer[ITimedTextSource]],  # result
                                                 _type.HRESULT]


class ITimedTextStyle(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_FontSize: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextDouble]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_struct.Windows.Media.Core.TimedTextDouble],  # value
                            _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_enum.Windows.Media.Core.TimedTextWeight],  # value
                              _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_struct.Windows.UI.Color],  # value
                              _type.HRESULT]
    get_Background: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_struct.Windows.UI.Color],  # value
                              _type.HRESULT]
    get_IsBackgroundAlwaysShown: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_IsBackgroundAlwaysShown: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_FlowDirection: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextFlowDirection]],  # value
                                 _type.HRESULT]
    put_FlowDirection: _Callable[[_enum.Windows.Media.Core.TimedTextFlowDirection],  # value
                                 _type.HRESULT]
    get_LineAlignment: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextLineAlignment]],  # value
                                 _type.HRESULT]
    put_LineAlignment: _Callable[[_enum.Windows.Media.Core.TimedTextLineAlignment],  # value
                                 _type.HRESULT]
    get_OutlineColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    put_OutlineColor: _Callable[[_struct.Windows.UI.Color],  # value
                                _type.HRESULT]
    get_OutlineThickness: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextDouble]],  # value
                                    _type.HRESULT]
    put_OutlineThickness: _Callable[[_struct.Windows.Media.Core.TimedTextDouble],  # value
                                    _type.HRESULT]
    get_OutlineRadius: _Callable[[_Pointer[_struct.Windows.Media.Core.TimedTextDouble]],  # value
                                 _type.HRESULT]
    put_OutlineRadius: _Callable[[_struct.Windows.Media.Core.TimedTextDouble],  # value
                                 _type.HRESULT]


class ITimedTextStyle2(_inspectable.IInspectable):
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.Media.Core.TimedTextFontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.Media.Core.TimedTextFontStyle],  # value
                             _type.HRESULT]
    get_IsUnderlineEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsUnderlineEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_IsLineThroughEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsLineThroughEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsOverlineEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsOverlineEnabled: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]


class ITimedTextStyle3(_inspectable.IInspectable):
    get_Ruby: _Callable[[_Pointer[ITimedTextRuby]],  # value
                        _type.HRESULT]
    get_Bouten: _Callable[[_Pointer[ITimedTextBouten]],  # value
                          _type.HRESULT]
    get_IsTextCombined: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsTextCombined: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_FontAngleInDegrees: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_FontAngleInDegrees: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]


class ITimedTextSubformat(_inspectable.IInspectable):
    get_StartIndex: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_StartIndex: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_Length: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_SubformatStyle: _Callable[[_Pointer[ITimedTextStyle]],  # value
                                  _type.HRESULT]
    put_SubformatStyle: _Callable[[ITimedTextStyle],  # value
                                  _type.HRESULT]


class IVideoStabilizationEffect(_inspectable.IInspectable):
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    add_EnabledChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IVideoStabilizationEffect, IVideoStabilizationEffectEnabledChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_EnabledChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    GetRecommendedStreamConfiguration: _Callable[[_Windows_Media_Devices.IVideoDeviceController,  # controller
                                                  _Windows_Media_MediaProperties.IVideoEncodingProperties,  # desiredProperties
                                                  _Pointer[_Windows_Media_Capture.IVideoStreamConfiguration]],  # value
                                                 _type.HRESULT]


class IVideoStabilizationEffectEnabledChangedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Media.Core.VideoStabilizationEffectEnabledChangedReason]],  # value
                          _type.HRESULT]


class IVideoStreamDescriptor(_inspectable.IInspectable):
    get_EncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IVideoEncodingProperties]],  # encodingProperties
                                      _type.HRESULT]


class IVideoStreamDescriptor2(_inspectable.IInspectable):
    Copy: _Callable[[_Pointer[IVideoStreamDescriptor]],  # result
                    _type.HRESULT]


class IVideoStreamDescriptorFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_Media_MediaProperties.IVideoEncodingProperties,  # encodingProperties
                       _Pointer[IVideoStreamDescriptor]],  # result
                      _type.HRESULT]


class IVideoTrack(_inspectable.IInspectable):
    add_OpenFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaTrack, IVideoTrackOpenFailedEventArgs],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_OpenFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    GetEncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IVideoEncodingProperties]],  # value
                                     _type.HRESULT]
    get_PlaybackItem: _Callable[[_Pointer[_Windows_Media_Playback.IMediaPlaybackItem]],  # value
                                _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_SupportInfo: _Callable[[_Pointer[IVideoTrackSupportInfo]],  # value
                               _type.HRESULT]


class IVideoTrackOpenFailedEventArgs(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IVideoTrackSupportInfo(_inspectable.IInspectable):
    get_DecoderStatus: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaDecoderStatus]],  # value
                                 _type.HRESULT]
    get_MediaSourceStatus: _Callable[[_Pointer[_enum.Windows.Media.Core.MediaSourceStatus]],  # value
                                     _type.HRESULT]
