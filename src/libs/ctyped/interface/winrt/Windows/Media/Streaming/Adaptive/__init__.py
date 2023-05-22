from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ....Web import Http as _Windows_Web_Http
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAdaptiveMediaSource(_inspectable.IInspectable):
    get_IsLive: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_DesiredLiveOffset: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    put_DesiredLiveOffset: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                     _type.HRESULT]
    get_InitialBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    put_InitialBitrate: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_CurrentDownloadBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_CurrentPlaybackBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_AvailableBitrates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # value
                                     _type.HRESULT]
    get_DesiredMinBitrate: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                     _type.HRESULT]
    put_DesiredMinBitrate: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_DesiredMaxBitrate: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                     _type.HRESULT]
    put_DesiredMaxBitrate: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                     _type.HRESULT]
    get_AudioOnlyPlayback: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_InboundBitsPerSecond: _Callable[[_Pointer[_type.UINT64]],  # value
                                        _type.HRESULT]
    get_InboundBitsPerSecondWindow: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                              _type.HRESULT]
    put_InboundBitsPerSecondWindow: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                              _type.HRESULT]
    add_DownloadBitrateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdaptiveMediaSource, IAdaptiveMediaSourceDownloadBitrateChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_DownloadBitrateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_PlaybackBitrateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdaptiveMediaSource, IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_PlaybackBitrateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_DownloadRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdaptiveMediaSource, IAdaptiveMediaSourceDownloadRequestedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_DownloadRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_DownloadCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdaptiveMediaSource, IAdaptiveMediaSourceDownloadCompletedEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_DownloadCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_DownloadFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdaptiveMediaSource, IAdaptiveMediaSourceDownloadFailedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_DownloadFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IAdaptiveMediaSource2(_inspectable.IInspectable):
    get_AdvancedSettings: _Callable[[_Pointer[IAdaptiveMediaSourceAdvancedSettings]],  # value
                                    _type.HRESULT]


class IAdaptiveMediaSource3(_inspectable.IInspectable):
    get_MinLiveOffset: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                 _type.HRESULT]
    get_MaxSeekableWindowSize: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                         _type.HRESULT]
    get_DesiredSeekableWindowSize: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                             _type.HRESULT]
    put_DesiredSeekableWindowSize: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                             _type.HRESULT]
    get_Diagnostics: _Callable[[_Pointer[IAdaptiveMediaSourceDiagnostics]],  # value
                               _type.HRESULT]
    GetCorrelatedTimes: _Callable[[_Pointer[IAdaptiveMediaSourceCorrelatedTimes]],  # value
                                  _type.HRESULT]


class IAdaptiveMediaSourceAdvancedSettings(_inspectable.IInspectable):
    get_AllSegmentsIndependent: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_AllSegmentsIndependent: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_DesiredBitrateHeadroomRatio: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                               _type.HRESULT]
    put_DesiredBitrateHeadroomRatio: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                                               _type.HRESULT]
    get_BitrateDowngradeTriggerRatio: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                                _type.HRESULT]
    put_BitrateDowngradeTriggerRatio: _Callable[[_Windows_Foundation.IReference[_type.DOUBLE]],  # value
                                                _type.HRESULT]


class IAdaptiveMediaSourceCorrelatedTimes(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    get_PresentationTimeStamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                         _type.HRESULT]
    get_ProgramDateTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                   _type.HRESULT]


class IAdaptiveMediaSourceCreationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceCreationStatus]],  # value
                          _type.HRESULT]
    get_MediaSource: _Callable[[_Pointer[IAdaptiveMediaSource]],  # value
                               _type.HRESULT]
    get_HttpResponseMessage: _Callable[[_Pointer[_Windows_Web_Http.IHttpResponseMessage]],  # value
                                       _type.HRESULT]


class IAdaptiveMediaSourceCreationResult2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IAdaptiveMediaSourceDiagnosticAvailableEventArgs(_inspectable.IInspectable):
    get_DiagnosticType: _Callable[[_Pointer[_enum.Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDiagnosticType]],  # value
                                  _type.HRESULT]
    get_RequestId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    get_SegmentId: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                             _type.HRESULT]
    get_ResourceType: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType]]],  # value
                                _type.HRESULT]
    get_ResourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_ResourceByteRangeOffset: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_ResourceByteRangeLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_Bitrate: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                           _type.HRESULT]


class IAdaptiveMediaSourceDiagnosticAvailableEventArgs2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IAdaptiveMediaSourceDiagnosticAvailableEventArgs3(_inspectable.IInspectable):
    get_ResourceDuration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_ResourceContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IAdaptiveMediaSourceDiagnostics(_inspectable.IInspectable):
    add_DiagnosticAvailable: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdaptiveMediaSourceDiagnostics, IAdaptiveMediaSourceDiagnosticAvailableEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_DiagnosticAvailable: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IAdaptiveMediaSourceDownloadBitrateChangedEventArgs(_inspectable.IInspectable):
    get_OldValue: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_NewValue: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class IAdaptiveMediaSourceDownloadBitrateChangedEventArgs2(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceDownloadBitrateChangedReason]],  # value
                          _type.HRESULT]


class IAdaptiveMediaSourceDownloadCompletedEventArgs(_inspectable.IInspectable):
    get_ResourceType: _Callable[[_Pointer[_enum.Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType]],  # value
                                _type.HRESULT]
    get_ResourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_ResourceByteRangeOffset: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_ResourceByteRangeLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_HttpResponseMessage: _Callable[[_Pointer[_Windows_Web_Http.IHttpResponseMessage]],  # value
                                       _type.HRESULT]


class IAdaptiveMediaSourceDownloadCompletedEventArgs2(_inspectable.IInspectable):
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Statistics: _Callable[[_Pointer[IAdaptiveMediaSourceDownloadStatistics]],  # value
                              _type.HRESULT]
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]


class IAdaptiveMediaSourceDownloadCompletedEventArgs3(_inspectable.IInspectable):
    get_ResourceDuration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_ResourceContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IAdaptiveMediaSourceDownloadFailedEventArgs(_inspectable.IInspectable):
    get_ResourceType: _Callable[[_Pointer[_enum.Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType]],  # value
                                _type.HRESULT]
    get_ResourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_ResourceByteRangeOffset: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_ResourceByteRangeLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_HttpResponseMessage: _Callable[[_Pointer[_Windows_Web_Http.IHttpResponseMessage]],  # value
                                       _type.HRESULT]


class IAdaptiveMediaSourceDownloadFailedEventArgs2(_inspectable.IInspectable):
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Statistics: _Callable[[_Pointer[IAdaptiveMediaSourceDownloadStatistics]],  # value
                              _type.HRESULT]
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]


class IAdaptiveMediaSourceDownloadFailedEventArgs3(_inspectable.IInspectable):
    get_ResourceDuration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_ResourceContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IAdaptiveMediaSourceDownloadRequestedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IAdaptiveMediaSourceDownloadRequestedEventArgs(_inspectable.IInspectable):
    get_ResourceType: _Callable[[_Pointer[_enum.Windows.Media.Streaming.Adaptive.AdaptiveMediaSourceResourceType]],  # value
                                _type.HRESULT]
    get_ResourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_ResourceByteRangeOffset: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_ResourceByteRangeLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    get_Result: _Callable[[_Pointer[IAdaptiveMediaSourceDownloadResult]],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IAdaptiveMediaSourceDownloadRequestedDeferral]],  # deferral
                           _type.HRESULT]


class IAdaptiveMediaSourceDownloadRequestedEventArgs2(_inspectable.IInspectable):
    get_RequestId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]


class IAdaptiveMediaSourceDownloadRequestedEventArgs3(_inspectable.IInspectable):
    get_ResourceDuration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                    _type.HRESULT]
    get_ResourceContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IAdaptiveMediaSourceDownloadResult(_inspectable.IInspectable):
    get_ResourceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_ResourceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]
    get_InputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                               _type.HRESULT]
    put_InputStream: _Callable[[_Windows_Storage_Streams.IInputStream],  # value
                               _type.HRESULT]
    get_Buffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                          _type.HRESULT]
    put_Buffer: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                          _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ContentType: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_ExtendedStatus: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    put_ExtendedStatus: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]


class IAdaptiveMediaSourceDownloadResult2(_inspectable.IInspectable):
    get_ResourceByteRangeOffset: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    put_ResourceByteRangeOffset: _Callable[[_Windows_Foundation.IReference[_type.UINT64]],  # value
                                           _type.HRESULT]
    get_ResourceByteRangeLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT64]]],  # value
                                           _type.HRESULT]
    put_ResourceByteRangeLength: _Callable[[_Windows_Foundation.IReference[_type.UINT64]],  # value
                                           _type.HRESULT]


class IAdaptiveMediaSourceDownloadStatistics(_inspectable.IInspectable):
    get_ContentBytesReceivedCount: _Callable[[_Pointer[_type.UINT64]],  # value
                                             _type.HRESULT]
    get_TimeToHeadersReceived: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                         _type.HRESULT]
    get_TimeToFirstByteReceived: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                           _type.HRESULT]
    get_TimeToLastByteReceived: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                          _type.HRESULT]


class IAdaptiveMediaSourcePlaybackBitrateChangedEventArgs(_inspectable.IInspectable):
    get_OldValue: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_NewValue: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    get_AudioOnly: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IAdaptiveMediaSourceStatics(_inspectable.IInspectable, factory=True):
    IsContentTypeSupported: _Callable[[_type.HSTRING,  # contentType
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    CreateFromUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IAdaptiveMediaSourceCreationResult]]],  # result
                                  _type.HRESULT]
    CreateFromUriWithDownloaderAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                                 _Windows_Web_Http.IHttpClient,  # httpClient
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IAdaptiveMediaSourceCreationResult]]],  # result
                                                _type.HRESULT]
    CreateFromStreamAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # stream
                                      _Windows_Foundation.IUriRuntimeClass,  # uri
                                      _type.HSTRING,  # contentType
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IAdaptiveMediaSourceCreationResult]]],  # result
                                     _type.HRESULT]
    CreateFromStreamWithDownloaderAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # stream
                                                    _Windows_Foundation.IUriRuntimeClass,  # uri
                                                    _type.HSTRING,  # contentType
                                                    _Windows_Web_Http.IHttpClient,  # httpClient
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IAdaptiveMediaSourceCreationResult]]],  # result
                                                   _type.HRESULT]
