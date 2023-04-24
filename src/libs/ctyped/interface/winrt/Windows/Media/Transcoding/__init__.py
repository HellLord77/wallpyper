from __future__ import annotations

from typing import Callable as _Callable

from .. import Core as _Windows_Media_Core
from .. import MediaProperties as _Windows_Media_MediaProperties
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IMediaTranscoder(_inspectable.IInspectable):
    put_TrimStartTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                 _type.HRESULT]
    get_TrimStartTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]
    put_TrimStopTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                _type.HRESULT]
    get_TrimStopTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                _type.HRESULT]
    put_AlwaysReencode: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_AlwaysReencode: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_HardwareAccelerationEnabled: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_HardwareAccelerationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    AddAudioEffect: _Callable[[_type.HSTRING],  # activatableClassId
                              _type.HRESULT]
    AddAudioEffectWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                           _type.boolean,  # effectRequired
                                           _Windows_Foundation_Collections.IPropertySet],  # configuration
                                          _type.HRESULT]
    AddVideoEffect: _Callable[[_type.HSTRING],  # activatableClassId
                              _type.HRESULT]
    AddVideoEffectWithSettings: _Callable[[_type.HSTRING,  # activatableClassId
                                           _type.boolean,  # effectRequired
                                           _Windows_Foundation_Collections.IPropertySet],  # configuration
                                          _type.HRESULT]
    ClearEffects: _Callable[[],
                            _type.HRESULT]
    PrepareFileTranscodeAsync: _Callable[[_Windows_Storage.IStorageFile,  # source
                                          _Windows_Storage.IStorageFile,  # destination
                                          _Windows_Media_MediaProperties.IMediaEncodingProfile,  # profile
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IPrepareTranscodeResult]]],  # operation
                                         _type.HRESULT]
    PrepareStreamTranscodeAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # source
                                            _Windows_Storage_Streams.IRandomAccessStream,  # destination
                                            _Windows_Media_MediaProperties.IMediaEncodingProfile,  # profile
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IPrepareTranscodeResult]]],  # operation
                                           _type.HRESULT]


class IMediaTranscoder2(_inspectable.IInspectable):
    PrepareMediaStreamSourceTranscodeAsync: _Callable[[_Windows_Media_Core.IMediaSource,  # source
                                                       _Windows_Storage_Streams.IRandomAccessStream,  # destination
                                                       _Windows_Media_MediaProperties.IMediaEncodingProfile,  # profile
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IPrepareTranscodeResult]]],  # operation
                                                      _type.HRESULT]
    put_VideoProcessingAlgorithm: _Callable[[_enum.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm],  # value
                                            _type.HRESULT]
    get_VideoProcessingAlgorithm: _Callable[[_Pointer[_enum.Windows.Media.Transcoding.MediaVideoProcessingAlgorithm]],  # value
                                            _type.HRESULT]


class IPrepareTranscodeResult(_inspectable.IInspectable):
    get_CanTranscode: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_FailureReason: _Callable[[_Pointer[_enum.Windows.Media.Transcoding.TranscodeFailureReason]],  # value
                                 _type.HRESULT]
    TranscodeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncActionWithProgress[_type.DOUBLE]]],  # operation
                              _type.HRESULT]
