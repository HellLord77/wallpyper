from __future__ import annotations

from typing import Callable as _Callable

from .. import Core as _Windows_Media_Core
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAudioEncodingProperties(_inspectable.IInspectable):
    put_Bitrate: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_Bitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_ChannelCount: _Callable[[_type.UINT32],  # value
                                _type.HRESULT]
    get_ChannelCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    put_SampleRate: _Callable[[_type.UINT32],  # value
                              _type.HRESULT]
    get_SampleRate: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    put_BitsPerSample: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_BitsPerSample: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]


class IAudioEncodingProperties2(_inspectable.IInspectable):
    get_IsSpatial: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IAudioEncodingProperties3(_inspectable.IInspectable):
    Copy: _Callable[[_Pointer[IAudioEncodingProperties]],  # result
                    _type.HRESULT]


class IAudioEncodingPropertiesStatics(_inspectable.IInspectable, factory=True):
    CreateAac: _Callable[[_type.UINT32,  # sampleRate
                          _type.UINT32,  # channelCount
                          _type.UINT32,  # bitrate
                          _Pointer[IAudioEncodingProperties]],  # value
                         _type.HRESULT]
    CreateAacAdts: _Callable[[_type.UINT32,  # sampleRate
                              _type.UINT32,  # channelCount
                              _type.UINT32,  # bitrate
                              _Pointer[IAudioEncodingProperties]],  # value
                             _type.HRESULT]
    CreateMp3: _Callable[[_type.UINT32,  # sampleRate
                          _type.UINT32,  # channelCount
                          _type.UINT32,  # bitrate
                          _Pointer[IAudioEncodingProperties]],  # value
                         _type.HRESULT]
    CreatePcm: _Callable[[_type.UINT32,  # sampleRate
                          _type.UINT32,  # channelCount
                          _type.UINT32,  # bitsPerSample
                          _Pointer[IAudioEncodingProperties]],  # value
                         _type.HRESULT]
    CreateWma: _Callable[[_type.UINT32,  # sampleRate
                          _type.UINT32,  # channelCount
                          _type.UINT32,  # bitrate
                          _Pointer[IAudioEncodingProperties]],  # value
                         _type.HRESULT]


class IAudioEncodingPropertiesStatics2(_inspectable.IInspectable, factory=True):
    CreateAlac: _Callable[[_type.UINT32,  # sampleRate
                           _type.UINT32,  # channelCount
                           _type.UINT32,  # bitsPerSample
                           _Pointer[IAudioEncodingProperties]],  # value
                          _type.HRESULT]
    CreateFlac: _Callable[[_type.UINT32,  # sampleRate
                           _type.UINT32,  # channelCount
                           _type.UINT32,  # bitsPerSample
                           _Pointer[IAudioEncodingProperties]],  # value
                          _type.HRESULT]


class IAudioEncodingPropertiesWithFormatUserData(_inspectable.IInspectable):
    SetFormatUserData: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    GetFormatUserData: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                  _Pointer[_Pointer[_type.BYTE]]],  # value
                                 _type.HRESULT]


class IContainerEncodingProperties(_inspectable.IInspectable):
    pass


class IContainerEncodingProperties2(_inspectable.IInspectable):
    Copy: _Callable[[_Pointer[IContainerEncodingProperties]],  # result
                    _type.HRESULT]


class IH264ProfileIdsStatics(_inspectable.IInspectable, factory=True):
    get_ConstrainedBaseline: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    get_Baseline: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_Extended: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_Main: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    get_High: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    get_High10: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_High422: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    get_High444: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]
    get_StereoHigh: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_MultiviewHigh: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]


class IImageEncodingProperties(_inspectable.IInspectable):
    put_Width: _Callable[[_type.UINT32],  # value
                         _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    put_Height: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]


class IImageEncodingProperties2(_inspectable.IInspectable):
    Copy: _Callable[[_Pointer[IImageEncodingProperties]],  # result
                    _type.HRESULT]


class IImageEncodingPropertiesStatics(_inspectable.IInspectable, factory=True):
    CreateJpeg: _Callable[[_Pointer[IImageEncodingProperties]],  # value
                          _type.HRESULT]
    CreatePng: _Callable[[_Pointer[IImageEncodingProperties]],  # value
                         _type.HRESULT]
    CreateJpegXR: _Callable[[_Pointer[IImageEncodingProperties]],  # value
                            _type.HRESULT]


class IImageEncodingPropertiesStatics2(_inspectable.IInspectable, factory=True):
    CreateUncompressed: _Callable[[_enum.Windows.Media.MediaProperties.MediaPixelFormat,  # format
                                   _Pointer[IImageEncodingProperties]],  # value
                                  _type.HRESULT]
    CreateBmp: _Callable[[_Pointer[IImageEncodingProperties]],  # value
                         _type.HRESULT]


class IImageEncodingPropertiesStatics3(_inspectable.IInspectable, factory=True):
    CreateHeif: _Callable[[_Pointer[IImageEncodingProperties]],  # result
                          _type.HRESULT]


class IMediaEncodingProfile(_inspectable.IInspectable):
    put_Audio: _Callable[[IAudioEncodingProperties],  # value
                         _type.HRESULT]
    get_Audio: _Callable[[_Pointer[IAudioEncodingProperties]],  # value
                         _type.HRESULT]
    put_Video: _Callable[[IVideoEncodingProperties],  # value
                         _type.HRESULT]
    get_Video: _Callable[[_Pointer[IVideoEncodingProperties]],  # value
                         _type.HRESULT]
    put_Container: _Callable[[IContainerEncodingProperties],  # value
                             _type.HRESULT]
    get_Container: _Callable[[_Pointer[IContainerEncodingProperties]],  # value
                             _type.HRESULT]


class IMediaEncodingProfile2(_inspectable.IInspectable):
    SetAudioTracks: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Media_Core.IAudioStreamDescriptor]],  # value
                              _type.HRESULT]
    GetAudioTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Media_Core.IAudioStreamDescriptor]]],  # value
                              _type.HRESULT]
    SetVideoTracks: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Media_Core.IVideoStreamDescriptor]],  # value
                              _type.HRESULT]
    GetVideoTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Media_Core.IVideoStreamDescriptor]]],  # value
                              _type.HRESULT]


class IMediaEncodingProfile3(_inspectable.IInspectable):
    SetTimedMetadataTracks: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Media_Core.IMediaStreamDescriptor]],  # value
                                      _type.HRESULT]
    GetTimedMetadataTracks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Media_Core.IMediaStreamDescriptor]]],  # result
                                      _type.HRESULT]


class IMediaEncodingProfileStatics(_inspectable.IInspectable, factory=True):
    CreateM4a: _Callable[[_enum.Windows.Media.MediaProperties.AudioEncodingQuality,  # quality
                          _Pointer[IMediaEncodingProfile]],  # value
                         _type.HRESULT]
    CreateMp3: _Callable[[_enum.Windows.Media.MediaProperties.AudioEncodingQuality,  # quality
                          _Pointer[IMediaEncodingProfile]],  # value
                         _type.HRESULT]
    CreateWma: _Callable[[_enum.Windows.Media.MediaProperties.AudioEncodingQuality,  # quality
                          _Pointer[IMediaEncodingProfile]],  # value
                         _type.HRESULT]
    CreateMp4: _Callable[[_enum.Windows.Media.MediaProperties.VideoEncodingQuality,  # quality
                          _Pointer[IMediaEncodingProfile]],  # value
                         _type.HRESULT]
    CreateWmv: _Callable[[_enum.Windows.Media.MediaProperties.VideoEncodingQuality,  # quality
                          _Pointer[IMediaEncodingProfile]],  # value
                         _type.HRESULT]
    CreateFromFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IMediaEncodingProfile]]],  # operation
                                   _type.HRESULT]
    CreateFromStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IMediaEncodingProfile]]],  # operation
                                     _type.HRESULT]


class IMediaEncodingProfileStatics2(_inspectable.IInspectable, factory=True):
    CreateWav: _Callable[[_enum.Windows.Media.MediaProperties.AudioEncodingQuality,  # quality
                          _Pointer[IMediaEncodingProfile]],  # value
                         _type.HRESULT]
    CreateAvi: _Callable[[_enum.Windows.Media.MediaProperties.VideoEncodingQuality,  # quality
                          _Pointer[IMediaEncodingProfile]],  # value
                         _type.HRESULT]


class IMediaEncodingProfileStatics3(_inspectable.IInspectable, factory=True):
    CreateAlac: _Callable[[_enum.Windows.Media.MediaProperties.AudioEncodingQuality,  # quality
                           _Pointer[IMediaEncodingProfile]],  # value
                          _type.HRESULT]
    CreateFlac: _Callable[[_enum.Windows.Media.MediaProperties.AudioEncodingQuality,  # quality
                           _Pointer[IMediaEncodingProfile]],  # value
                          _type.HRESULT]
    CreateHevc: _Callable[[_enum.Windows.Media.MediaProperties.VideoEncodingQuality,  # quality
                           _Pointer[IMediaEncodingProfile]],  # value
                          _type.HRESULT]


class IMediaEncodingProperties(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]
    get_Type: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Subtype: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Subtype: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IMediaEncodingSubtypesStatics(_inspectable.IInspectable, factory=True):
    get_Aac: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AacAdts: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Ac3: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_AmrNb: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_AmrWb: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Argb32: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Asf: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Avi: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Bgra8: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Bmp: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Eac3: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Float: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Gif: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_H263: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_H264: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_H264Es: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Hevc: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_HevcEs: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Iyuv: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Jpeg: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_JpegXr: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Mjpg: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Mpeg: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Mpeg1: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Mpeg2: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Mp3: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Mpeg4: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Nv12: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Pcm: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Png: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Rgb24: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Rgb32: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Tiff: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Wave: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Wma8: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Wma9: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Wmv3: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Wvc1: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Yuy2: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Yv12: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IMediaEncodingSubtypesStatics2(_inspectable.IInspectable, factory=True):
    get_Vp9: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_L8: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_L16: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_D16: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]


class IMediaEncodingSubtypesStatics3(_inspectable.IInspectable, factory=True):
    get_Alac: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Flac: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IMediaEncodingSubtypesStatics4(_inspectable.IInspectable, factory=True):
    get_P010: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IMediaEncodingSubtypesStatics5(_inspectable.IInspectable, factory=True):
    get_Heif: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IMediaEncodingSubtypesStatics6(_inspectable.IInspectable, factory=True):
    get_Pgs: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Srt: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Ssa: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_VobSub: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IMediaRatio(_inspectable.IInspectable):
    put_Numerator: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_Numerator: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_Denominator: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_Denominator: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]


class IMpeg2ProfileIdsStatics(_inspectable.IInspectable, factory=True):
    get_Simple: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_Main: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    get_SignalNoiseRatioScalable: _Callable[[_Pointer[_type.INT32]],  # value
                                            _type.HRESULT]
    get_SpatiallyScalable: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    get_High: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]


class ITimedMetadataEncodingProperties(_inspectable.IInspectable):
    SetFormatUserData: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    GetFormatUserData: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                  _Pointer[_Pointer[_type.BYTE]]],  # value
                                 _type.HRESULT]
    Copy: _Callable[[_Pointer[IMediaEncodingProperties]],  # result
                    _type.HRESULT]


class ITimedMetadataEncodingPropertiesStatics(_inspectable.IInspectable, factory=True):
    CreatePgs: _Callable[[_Pointer[IMediaEncodingProperties]],  # result
                         _type.HRESULT]
    CreateSrt: _Callable[[_Pointer[IMediaEncodingProperties]],  # result
                         _type.HRESULT]
    CreateSsa: _Callable[[_type.UINT32,  # __formatUserDataSize
                          _Pointer[_type.BYTE],  # formatUserData
                          _Pointer[IMediaEncodingProperties]],  # result
                         _type.HRESULT]
    CreateVobSub: _Callable[[_type.UINT32,  # __formatUserDataSize
                             _Pointer[_type.BYTE],  # formatUserData
                             _Pointer[IMediaEncodingProperties]],  # result
                            _type.HRESULT]


class IVideoEncodingProperties(_inspectable.IInspectable):
    put_Bitrate: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_Bitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_Width: _Callable[[_type.UINT32],  # value
                         _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    put_Height: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_FrameRate: _Callable[[_Pointer[IMediaRatio]],  # value
                             _type.HRESULT]
    get_PixelAspectRatio: _Callable[[_Pointer[IMediaRatio]],  # value
                                    _type.HRESULT]


class IVideoEncodingProperties2(_inspectable.IInspectable):
    SetFormatUserData: _Callable[[_type.UINT32,  # __valueSize
                                  _Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    GetFormatUserData: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                  _Pointer[_Pointer[_type.BYTE]]],  # value
                                 _type.HRESULT]
    put_ProfileId: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_ProfileId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]


class IVideoEncodingProperties3(_inspectable.IInspectable):
    get_StereoscopicVideoPackingMode: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.StereoscopicVideoPackingMode]],  # value
                                                _type.HRESULT]


class IVideoEncodingProperties4(_inspectable.IInspectable):
    get_SphericalVideoFrameFormat: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.SphericalVideoFrameFormat]],  # value
                                             _type.HRESULT]


class IVideoEncodingProperties5(_inspectable.IInspectable):
    Copy: _Callable[[_Pointer[IVideoEncodingProperties]],  # result
                    _type.HRESULT]


class IVideoEncodingPropertiesStatics(_inspectable.IInspectable, factory=True):
    CreateH264: _Callable[[_Pointer[IVideoEncodingProperties]],  # value
                          _type.HRESULT]
    CreateMpeg2: _Callable[[_Pointer[IVideoEncodingProperties]],  # value
                           _type.HRESULT]
    CreateUncompressed: _Callable[[_type.HSTRING,  # subtype
                                   _type.UINT32,  # width
                                   _type.UINT32,  # height
                                   _Pointer[IVideoEncodingProperties]],  # value
                                  _type.HRESULT]


class IVideoEncodingPropertiesStatics2(_inspectable.IInspectable, factory=True):
    CreateHevc: _Callable[[_Pointer[IVideoEncodingProperties]],  # value
                          _type.HRESULT]
