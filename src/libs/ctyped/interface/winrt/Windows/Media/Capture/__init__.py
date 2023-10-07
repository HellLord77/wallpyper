from __future__ import annotations as _

from typing import Callable as _Callable

from . import Core as _Windows_Media_Capture_Core
from . import Frames as _Windows_Media_Capture_Frames
from .. import Core as _Windows_Media_Core
from .. import Devices as _Windows_Media_Devices
from .. import Effects as _Windows_Media_Effects
from .. import MediaProperties as _Windows_Media_MediaProperties
from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics import Imaging as _Windows_Graphics_Imaging
from ...Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ...Security import Credentials as _Windows_Security_Credentials
from ...Security.Authentication import Web as _Windows_Security_Authentication_Web
from ...Storage import Streams as _Windows_Storage_Streams
from ...UI import WindowManagement as _Windows_UI_WindowManagement
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IMediaCaptureFailedEventHandler:
    Invoke: _Callable[[IMediaCapture,  # sender
                       IMediaCaptureFailedEventArgs],  # errorEventArgs
                      _type.HRESULT]


class IMediaCaptureFailedEventHandler(_IMediaCaptureFailedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IMediaCaptureFailedEventHandler_impl(_IMediaCaptureFailedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IRecordLimitationExceededEventHandler:
    Invoke: _Callable[[IMediaCapture],  # sender
                      _type.HRESULT]


class IRecordLimitationExceededEventHandler(_IRecordLimitationExceededEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRecordLimitationExceededEventHandler_impl(_IRecordLimitationExceededEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAdvancedCapturedPhoto(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[ICapturedFrame]],  # value
                         _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.AdvancedPhotoMode]],  # value
                        _type.HRESULT]
    get_Context: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]


class IAdvancedCapturedPhoto2(_inspectable.IInspectable):
    get_FrameBoundsRelativeToReferencePhoto: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]]],  # value
                                                       _type.HRESULT]


class IAdvancedPhotoCapture(_inspectable.IInspectable):
    CaptureAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAdvancedCapturedPhoto]]],  # operation
                            _type.HRESULT]
    CaptureWithContextAsync: _Callable[[_inspectable.IInspectable,  # context
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IAdvancedCapturedPhoto]]],  # operation
                                       _type.HRESULT]
    add_OptionalReferencePhotoCaptured: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdvancedPhotoCapture, IOptionalReferencePhotoCapturedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_OptionalReferencePhotoCaptured: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_AllPhotosCaptured: _Callable[[_Windows_Foundation.ITypedEventHandler[IAdvancedPhotoCapture, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_AllPhotosCaptured: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    FinishAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class IAppBroadcastBackgroundService(_inspectable.IInspectable):
    put_PlugInState: _Callable[[_enum.Windows.Media.Capture.AppBroadcastPlugInState],  # value
                               _type.HRESULT]
    get_PlugInState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastPlugInState]],  # value
                               _type.HRESULT]
    put_SignInInfo: _Callable[[IAppBroadcastBackgroundServiceSignInInfo],  # value
                              _type.HRESULT]
    get_SignInInfo: _Callable[[_Pointer[IAppBroadcastBackgroundServiceSignInInfo]],  # value
                              _type.HRESULT]
    put_StreamInfo: _Callable[[IAppBroadcastBackgroundServiceStreamInfo],  # value
                              _type.HRESULT]
    get_StreamInfo: _Callable[[_Pointer[IAppBroadcastBackgroundServiceStreamInfo]],  # value
                              _type.HRESULT]
    get_AppId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_BroadcastTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_ViewerCount: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_ViewerCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    TerminateBroadcast: _Callable[[_enum.Windows.Media.Capture.AppBroadcastTerminationReason,  # reason
                                   _type.UINT32],  # providerSpecificReason
                                  _type.HRESULT]
    add_HeartbeatRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundService, IAppBroadcastHeartbeatRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_HeartbeatRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    get_TitleId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IAppBroadcastBackgroundService2(_inspectable.IInspectable):
    put_BroadcastTitle: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_BroadcastLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_BroadcastLanguage: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_BroadcastChannel: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_BroadcastChannel: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    add_BroadcastTitleChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundService, _inspectable.IInspectable],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_BroadcastTitleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_BroadcastLanguageChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundService, _inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_BroadcastLanguageChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_BroadcastChannelChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundService, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_BroadcastChannelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IAppBroadcastBackgroundServiceSignInInfo(_inspectable.IInspectable):
    get_SignInState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastSignInState]],  # value
                               _type.HRESULT]
    put_OAuthRequestUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                   _type.HRESULT]
    get_OAuthRequestUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]
    put_OAuthCallbackUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                    _type.HRESULT]
    get_OAuthCallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                    _type.HRESULT]
    get_AuthenticationResult: _Callable[[_Pointer[_Windows_Security_Authentication_Web.IWebAuthenticationResult]],  # value
                                        _type.HRESULT]
    put_UserName: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    add_SignInStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundServiceSignInInfo, IAppBroadcastSignInStateChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_SignInStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class IAppBroadcastBackgroundServiceSignInInfo2(_inspectable.IInspectable):
    add_UserNameChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundServiceSignInInfo, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_UserNameChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IAppBroadcastBackgroundServiceStreamInfo(_inspectable.IInspectable):
    get_StreamState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastStreamState]],  # value
                               _type.HRESULT]
    put_DesiredVideoEncodingBitrate: _Callable[[_type.UINT64],  # value
                                               _type.HRESULT]
    get_DesiredVideoEncodingBitrate: _Callable[[_Pointer[_type.UINT64]],  # value
                                               _type.HRESULT]
    put_BandwidthTestBitrate: _Callable[[_type.UINT64],  # value
                                        _type.HRESULT]
    get_BandwidthTestBitrate: _Callable[[_Pointer[_type.UINT64]],  # value
                                        _type.HRESULT]
    put_AudioCodec: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_AudioCodec: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_BroadcastStreamReader: _Callable[[_Pointer[IAppBroadcastStreamReader]],  # value
                                         _type.HRESULT]
    add_StreamStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundServiceStreamInfo, IAppBroadcastStreamStateChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_StreamStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_VideoEncodingResolutionChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundServiceStreamInfo, _inspectable.IInspectable],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_VideoEncodingResolutionChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_VideoEncodingBitrateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastBackgroundServiceStreamInfo, _inspectable.IInspectable],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_VideoEncodingBitrateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IAppBroadcastBackgroundServiceStreamInfo2(_inspectable.IInspectable):
    ReportProblemWithStream: _Callable[[],
                                       _type.HRESULT]


class IAppBroadcastCameraCaptureStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastCameraCaptureState]],  # value
                         _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IAppBroadcastGlobalSettings(_inspectable.IInspectable):
    get_IsBroadcastEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsDisabledByPolicy: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsGpuConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_HasHardwareEncoder: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsAudioCaptureEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsAudioCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsMicrophoneCaptureEnabledByDefault: _Callable[[_type.boolean],  # value
                                                       _type.HRESULT]
    get_IsMicrophoneCaptureEnabledByDefault: _Callable[[_Pointer[_type.boolean]],  # value
                                                       _type.HRESULT]
    put_IsEchoCancellationEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsEchoCancellationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_SystemAudioGain: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_SystemAudioGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_MicrophoneGain: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_MicrophoneGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_IsCameraCaptureEnabledByDefault: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_IsCameraCaptureEnabledByDefault: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_SelectedCameraId: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_SelectedCameraId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_CameraOverlayLocation: _Callable[[_enum.Windows.Media.Capture.AppBroadcastCameraOverlayLocation],  # value
                                         _type.HRESULT]
    get_CameraOverlayLocation: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastCameraOverlayLocation]],  # value
                                         _type.HRESULT]
    put_CameraOverlaySize: _Callable[[_enum.Windows.Media.Capture.AppBroadcastCameraOverlaySize],  # value
                                     _type.HRESULT]
    get_CameraOverlaySize: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastCameraOverlaySize]],  # value
                                     _type.HRESULT]
    put_IsCursorImageCaptureEnabled: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsCursorImageCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IAppBroadcastHeartbeatRequestedEventArgs(_inspectable.IInspectable):
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]


class IAppBroadcastManagerStatics(_inspectable.IInspectable, factory=True):
    GetGlobalSettings: _Callable[[_Pointer[IAppBroadcastGlobalSettings]],  # value
                                 _type.HRESULT]
    ApplyGlobalSettings: _Callable[[IAppBroadcastGlobalSettings],  # value
                                   _type.HRESULT]
    GetProviderSettings: _Callable[[_Pointer[IAppBroadcastProviderSettings]],  # value
                                   _type.HRESULT]
    ApplyProviderSettings: _Callable[[IAppBroadcastProviderSettings],  # value
                                     _type.HRESULT]


class IAppBroadcastMicrophoneCaptureStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastMicrophoneCaptureState]],  # value
                         _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IAppBroadcastPlugIn(_inspectable.IInspectable):
    get_AppId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_ProviderSettings: _Callable[[_Pointer[IAppBroadcastProviderSettings]],  # value
                                    _type.HRESULT]
    get_Logo: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                        _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IAppBroadcastPlugInManager(_inspectable.IInspectable):
    get_IsBroadcastProviderAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_PlugInList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppBroadcastPlugIn]]],  # value
                              _type.HRESULT]
    get_DefaultPlugIn: _Callable[[_Pointer[IAppBroadcastPlugIn]],  # value
                                 _type.HRESULT]
    put_DefaultPlugIn: _Callable[[IAppBroadcastPlugIn],  # value
                                 _type.HRESULT]


class IAppBroadcastPlugInManagerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IAppBroadcastPlugInManager]],  # ppInstance
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IAppBroadcastPlugInManager]],  # ppInstance
                          _type.HRESULT]


class IAppBroadcastPlugInStateChangedEventArgs(_inspectable.IInspectable):
    get_PlugInState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastPlugInState]],  # value
                               _type.HRESULT]


class IAppBroadcastPreview(_inspectable.IInspectable):
    StopPreview: _Callable[[],
                           _type.HRESULT]
    get_PreviewState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastPreviewState]],  # value
                                _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                             _type.HRESULT]
    add_PreviewStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastPreview, IAppBroadcastPreviewStateChangedEventArgs],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PreviewStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    get_PreviewStreamReader: _Callable[[_Pointer[IAppBroadcastPreviewStreamReader]],  # value
                                       _type.HRESULT]


class IAppBroadcastPreviewStateChangedEventArgs(_inspectable.IInspectable):
    get_PreviewState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastPreviewState]],  # value
                                _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IAppBroadcastPreviewStreamReader(_inspectable.IInspectable):
    get_VideoWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_VideoHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_VideoStride: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_VideoBitmapPixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]],  # value
                                          _type.HRESULT]
    get_VideoBitmapAlphaMode: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapAlphaMode]],  # value
                                        _type.HRESULT]
    TryGetNextVideoFrame: _Callable[[_Pointer[IAppBroadcastPreviewStreamVideoFrame]],  # frame
                                    _type.HRESULT]
    add_VideoFrameArrived: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastPreviewStreamReader, _inspectable.IInspectable],  # value
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_VideoFrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IAppBroadcastPreviewStreamVideoFrame(_inspectable.IInspectable):
    get_VideoHeader: _Callable[[_Pointer[IAppBroadcastPreviewStreamVideoHeader]],  # value
                               _type.HRESULT]
    get_VideoBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class IAppBroadcastPreviewStreamVideoHeader(_inspectable.IInspectable):
    get_AbsoluteTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                     _type.HRESULT]
    get_RelativeTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_FrameId: _Callable[[_Pointer[_type.UINT64]],  # value
                           _type.HRESULT]


class IAppBroadcastProviderSettings(_inspectable.IInspectable):
    put_DefaultBroadcastTitle: _Callable[[_type.HSTRING],  # value
                                         _type.HRESULT]
    get_DefaultBroadcastTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    put_AudioEncodingBitrate: _Callable[[_type.UINT32],  # value
                                        _type.HRESULT]
    get_AudioEncodingBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    put_CustomVideoEncodingBitrate: _Callable[[_type.UINT32],  # value
                                              _type.HRESULT]
    get_CustomVideoEncodingBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]
    put_CustomVideoEncodingHeight: _Callable[[_type.UINT32],  # value
                                             _type.HRESULT]
    get_CustomVideoEncodingHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                             _type.HRESULT]
    put_CustomVideoEncodingWidth: _Callable[[_type.UINT32],  # value
                                            _type.HRESULT]
    get_CustomVideoEncodingWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]
    put_VideoEncodingBitrateMode: _Callable[[_enum.Windows.Media.Capture.AppBroadcastVideoEncodingBitrateMode],  # value
                                            _type.HRESULT]
    get_VideoEncodingBitrateMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastVideoEncodingBitrateMode]],  # value
                                            _type.HRESULT]
    put_VideoEncodingResolutionMode: _Callable[[_enum.Windows.Media.Capture.AppBroadcastVideoEncodingResolutionMode],  # value
                                               _type.HRESULT]
    get_VideoEncodingResolutionMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastVideoEncodingResolutionMode]],  # value
                                               _type.HRESULT]


class IAppBroadcastServices(_inspectable.IInspectable):
    get_CaptureTargetType: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastCaptureTargetType]],  # value
                                     _type.HRESULT]
    put_CaptureTargetType: _Callable[[_enum.Windows.Media.Capture.AppBroadcastCaptureTargetType],  # value
                                     _type.HRESULT]
    get_BroadcastTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_BroadcastTitle: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_BroadcastLanguage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_BroadcastLanguage: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_CanCapture: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    EnterBroadcastModeAsync: _Callable[[IAppBroadcastPlugIn,  # plugIn
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                       _type.HRESULT]
    ExitBroadcastMode: _Callable[[_enum.Windows.Media.Capture.AppBroadcastExitBroadcastModeReason],  # reason
                                 _type.HRESULT]
    StartBroadcast: _Callable[[],
                              _type.HRESULT]
    PauseBroadcast: _Callable[[],
                              _type.HRESULT]
    ResumeBroadcast: _Callable[[],
                               _type.HRESULT]
    StartPreview: _Callable[[_struct.Windows.Foundation.Size,  # desiredSize
                             _Pointer[IAppBroadcastPreview]],  # preview
                            _type.HRESULT]
    get_State: _Callable[[_Pointer[IAppBroadcastState]],  # value
                         _type.HRESULT]


class IAppBroadcastSignInStateChangedEventArgs(_inspectable.IInspectable):
    get_SignInState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastSignInState]],  # value
                               _type.HRESULT]
    get_Result: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastSignInResult]],  # value
                          _type.HRESULT]


class IAppBroadcastState(_inspectable.IInspectable):
    get_IsCaptureTargetRunning: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_ViewerCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_ShouldCaptureMicrophone: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_ShouldCaptureMicrophone: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    RestartMicrophoneCapture: _Callable[[],
                                        _type.HRESULT]
    get_ShouldCaptureCamera: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_ShouldCaptureCamera: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    RestartCameraCapture: _Callable[[],
                                    _type.HRESULT]
    get_EncodedVideoSize: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                    _type.HRESULT]
    get_MicrophoneCaptureState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastMicrophoneCaptureState]],  # value
                                          _type.HRESULT]
    get_MicrophoneCaptureError: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_CameraCaptureState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastCameraCaptureState]],  # value
                                      _type.HRESULT]
    get_CameraCaptureError: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    get_StreamState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastStreamState]],  # value
                               _type.HRESULT]
    get_PlugInState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastPlugInState]],  # value
                               _type.HRESULT]
    get_OAuthRequestUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]
    get_OAuthCallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                    _type.HRESULT]
    get_AuthenticationResult: _Callable[[_Pointer[_Windows_Security_Authentication_Web.IWebAuthenticationResult]],  # value
                                        _type.HRESULT]
    put_AuthenticationResult: _Callable[[_Windows_Security_Authentication_Web.IWebAuthenticationResult],  # value
                                        _type.HRESULT]
    put_SignInState: _Callable[[_enum.Windows.Media.Capture.AppBroadcastSignInState],  # value
                               _type.HRESULT]
    get_SignInState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastSignInState]],  # value
                               _type.HRESULT]
    get_TerminationReason: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastTerminationReason]],  # value
                                     _type.HRESULT]
    get_TerminationReasonPlugInSpecific: _Callable[[_Pointer[_type.UINT32]],  # value
                                                   _type.HRESULT]
    add_ViewerCountChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastState, IAppBroadcastViewerCountChangedEventArgs],  # value
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_ViewerCountChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_MicrophoneCaptureStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastState, IAppBroadcastMicrophoneCaptureStateChangedEventArgs],  # value
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_MicrophoneCaptureStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_CameraCaptureStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastState, IAppBroadcastCameraCaptureStateChangedEventArgs],  # value
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_CameraCaptureStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_PlugInStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastState, IAppBroadcastPlugInStateChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_PlugInStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_StreamStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastState, IAppBroadcastStreamStateChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_StreamStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_CaptureTargetClosed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastState, _inspectable.IInspectable],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_CaptureTargetClosed: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IAppBroadcastStreamAudioFrame(_inspectable.IInspectable):
    get_AudioHeader: _Callable[[_Pointer[IAppBroadcastStreamAudioHeader]],  # value
                               _type.HRESULT]
    get_AudioBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class IAppBroadcastStreamAudioHeader(_inspectable.IInspectable):
    get_AbsoluteTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                     _type.HRESULT]
    get_RelativeTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_HasDiscontinuity: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_FrameId: _Callable[[_Pointer[_type.UINT64]],  # value
                           _type.HRESULT]


class IAppBroadcastStreamReader(_inspectable.IInspectable):
    get_AudioChannels: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_AudioSampleRate: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    get_AudioAacSequence: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                    _type.HRESULT]
    get_AudioBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    TryGetNextAudioFrame: _Callable[[_Pointer[IAppBroadcastStreamAudioFrame]],  # frame
                                    _type.HRESULT]
    get_VideoWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_VideoHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_VideoBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    TryGetNextVideoFrame: _Callable[[_Pointer[IAppBroadcastStreamVideoFrame]],  # frame
                                    _type.HRESULT]
    add_AudioFrameArrived: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastStreamReader, _inspectable.IInspectable],  # value
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_AudioFrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_VideoFrameArrived: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppBroadcastStreamReader, _inspectable.IInspectable],  # value
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_VideoFrameArrived: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IAppBroadcastStreamStateChangedEventArgs(_inspectable.IInspectable):
    get_StreamState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppBroadcastStreamState]],  # value
                               _type.HRESULT]


class IAppBroadcastStreamVideoFrame(_inspectable.IInspectable):
    get_VideoHeader: _Callable[[_Pointer[IAppBroadcastStreamVideoHeader]],  # value
                               _type.HRESULT]
    get_VideoBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                               _type.HRESULT]


class IAppBroadcastStreamVideoHeader(_inspectable.IInspectable):
    get_AbsoluteTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                     _type.HRESULT]
    get_RelativeTimestamp: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_IsKeyFrame: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_HasDiscontinuity: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_FrameId: _Callable[[_Pointer[_type.UINT64]],  # value
                           _type.HRESULT]


class IAppBroadcastTriggerDetails(_inspectable.IInspectable):
    get_BackgroundService: _Callable[[_Pointer[IAppBroadcastBackgroundService]],  # value
                                     _type.HRESULT]


class IAppBroadcastViewerCountChangedEventArgs(_inspectable.IInspectable):
    get_ViewerCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]


class IAppCapture(_inspectable.IInspectable):
    get_IsCapturingAudio: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsCapturingVideo: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    add_CapturingChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCapture, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_CapturingChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class IAppCaptureAlternateShortcutKeys(_inspectable.IInspectable):
    put_ToggleGameBarKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                    _type.HRESULT]
    get_ToggleGameBarKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                    _type.HRESULT]
    put_ToggleGameBarKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                             _type.HRESULT]
    get_ToggleGameBarKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                             _type.HRESULT]
    put_SaveHistoricalVideoKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                          _type.HRESULT]
    get_SaveHistoricalVideoKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                          _type.HRESULT]
    put_SaveHistoricalVideoKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                                   _type.HRESULT]
    get_SaveHistoricalVideoKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                                   _type.HRESULT]
    put_ToggleRecordingKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                      _type.HRESULT]
    get_ToggleRecordingKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                      _type.HRESULT]
    put_ToggleRecordingKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                               _type.HRESULT]
    get_ToggleRecordingKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                               _type.HRESULT]
    put_TakeScreenshotKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                     _type.HRESULT]
    get_TakeScreenshotKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                     _type.HRESULT]
    put_TakeScreenshotKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                              _type.HRESULT]
    get_TakeScreenshotKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                              _type.HRESULT]
    put_ToggleRecordingIndicatorKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                               _type.HRESULT]
    get_ToggleRecordingIndicatorKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                               _type.HRESULT]
    put_ToggleRecordingIndicatorKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                                        _type.HRESULT]
    get_ToggleRecordingIndicatorKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                                        _type.HRESULT]


class IAppCaptureAlternateShortcutKeys2(_inspectable.IInspectable):
    put_ToggleMicrophoneCaptureKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                              _type.HRESULT]
    get_ToggleMicrophoneCaptureKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                              _type.HRESULT]
    put_ToggleMicrophoneCaptureKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                                       _type.HRESULT]
    get_ToggleMicrophoneCaptureKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                                       _type.HRESULT]


class IAppCaptureAlternateShortcutKeys3(_inspectable.IInspectable):
    put_ToggleCameraCaptureKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                          _type.HRESULT]
    get_ToggleCameraCaptureKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                          _type.HRESULT]
    put_ToggleCameraCaptureKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                                   _type.HRESULT]
    get_ToggleCameraCaptureKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                                   _type.HRESULT]
    put_ToggleBroadcastKey: _Callable[[_enum.Windows.System.VirtualKey],  # value
                                      _type.HRESULT]
    get_ToggleBroadcastKey: _Callable[[_Pointer[_enum.Windows.System.VirtualKey]],  # value
                                      _type.HRESULT]
    put_ToggleBroadcastKeyModifiers: _Callable[[_enum.Windows.System.VirtualKeyModifiers],  # value
                                               _type.HRESULT]
    get_ToggleBroadcastKeyModifiers: _Callable[[_Pointer[_enum.Windows.System.VirtualKeyModifiers]],  # value
                                               _type.HRESULT]


class IAppCaptureDurationGeneratedEventArgs(_inspectable.IInspectable):
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]


class IAppCaptureFileGeneratedEventArgs(_inspectable.IInspectable):
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]


class IAppCaptureManagerStatics(_inspectable.IInspectable, factory=True):
    GetCurrentSettings: _Callable[[_Pointer[IAppCaptureSettings]],  # value
                                  _type.HRESULT]
    ApplySettings: _Callable[[IAppCaptureSettings],  # appCaptureSettings
                             _type.HRESULT]


class IAppCaptureMetadataWriter(_inspectable.IInspectable):
    AddStringEvent: _Callable[[_type.HSTRING,  # name
                               _type.HSTRING,  # value
                               _enum.Windows.Media.Capture.AppCaptureMetadataPriority],  # priority
                              _type.HRESULT]
    AddInt32Event: _Callable[[_type.HSTRING,  # name
                              _type.INT32,  # value
                              _enum.Windows.Media.Capture.AppCaptureMetadataPriority],  # priority
                             _type.HRESULT]
    AddDoubleEvent: _Callable[[_type.HSTRING,  # name
                               _type.DOUBLE,  # value
                               _enum.Windows.Media.Capture.AppCaptureMetadataPriority],  # priority
                              _type.HRESULT]
    StartStringState: _Callable[[_type.HSTRING,  # name
                                 _type.HSTRING,  # value
                                 _enum.Windows.Media.Capture.AppCaptureMetadataPriority],  # priority
                                _type.HRESULT]
    StartInt32State: _Callable[[_type.HSTRING,  # name
                                _type.INT32,  # value
                                _enum.Windows.Media.Capture.AppCaptureMetadataPriority],  # priority
                               _type.HRESULT]
    StartDoubleState: _Callable[[_type.HSTRING,  # name
                                 _type.DOUBLE,  # value
                                 _enum.Windows.Media.Capture.AppCaptureMetadataPriority],  # priority
                                _type.HRESULT]
    StopState: _Callable[[_type.HSTRING],  # name
                         _type.HRESULT]
    StopAllStates: _Callable[[],
                             _type.HRESULT]
    get_RemainingStorageBytesAvailable: _Callable[[_Pointer[_type.UINT64]],  # value
                                                  _type.HRESULT]
    add_MetadataPurged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCaptureMetadataWriter, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_MetadataPurged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IAppCaptureMicrophoneCaptureStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureMicrophoneCaptureState]],  # value
                         _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IAppCaptureRecordOperation(_inspectable.IInspectable):
    StopRecording: _Callable[[],
                             _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureRecordingState]],  # value
                         _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]
    get_IsFileTruncated: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                   _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCaptureRecordOperation, IAppCaptureRecordingStateChangedEventArgs],  # value
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_DurationGenerated: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCaptureRecordOperation, IAppCaptureDurationGeneratedEventArgs],  # value
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_DurationGenerated: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_FileGenerated: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCaptureRecordOperation, IAppCaptureFileGeneratedEventArgs],  # value
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_FileGenerated: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IAppCaptureRecordingStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureRecordingState]],  # value
                         _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IAppCaptureServices(_inspectable.IInspectable):
    Record: _Callable[[_Pointer[IAppCaptureRecordOperation]],  # operation
                      _type.HRESULT]
    RecordTimeSpan: _Callable[[_struct.Windows.Foundation.DateTime,  # startTime
                               _struct.Windows.Foundation.TimeSpan,  # duration
                               _Pointer[IAppCaptureRecordOperation]],  # operation
                              _type.HRESULT]
    get_CanCapture: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_State: _Callable[[_Pointer[IAppCaptureState]],  # value
                         _type.HRESULT]


class IAppCaptureSettings(_inspectable.IInspectable):
    put_AppCaptureDestinationFolder: _Callable[[_Windows_Storage.IStorageFolder],  # value
                                               _type.HRESULT]
    get_AppCaptureDestinationFolder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                               _type.HRESULT]
    put_AudioEncodingBitrate: _Callable[[_type.UINT32],  # value
                                        _type.HRESULT]
    get_AudioEncodingBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    put_IsAudioCaptureEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsAudioCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_CustomVideoEncodingBitrate: _Callable[[_type.UINT32],  # value
                                              _type.HRESULT]
    get_CustomVideoEncodingBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]
    put_CustomVideoEncodingHeight: _Callable[[_type.UINT32],  # value
                                             _type.HRESULT]
    get_CustomVideoEncodingHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                             _type.HRESULT]
    put_CustomVideoEncodingWidth: _Callable[[_type.UINT32],  # value
                                            _type.HRESULT]
    get_CustomVideoEncodingWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]
    put_HistoricalBufferLength: _Callable[[_type.UINT32],  # value
                                          _type.HRESULT]
    get_HistoricalBufferLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    put_HistoricalBufferLengthUnit: _Callable[[_enum.Windows.Media.Capture.AppCaptureHistoricalBufferLengthUnit],  # value
                                              _type.HRESULT]
    get_HistoricalBufferLengthUnit: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureHistoricalBufferLengthUnit]],  # value
                                              _type.HRESULT]
    put_IsHistoricalCaptureEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_IsHistoricalCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsHistoricalCaptureOnBatteryAllowed: _Callable[[_type.boolean],  # value
                                                       _type.HRESULT]
    get_IsHistoricalCaptureOnBatteryAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                                       _type.HRESULT]
    put_IsHistoricalCaptureOnWirelessDisplayAllowed: _Callable[[_type.boolean],  # value
                                                               _type.HRESULT]
    get_IsHistoricalCaptureOnWirelessDisplayAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                                               _type.HRESULT]
    put_MaximumRecordLength: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                       _type.HRESULT]
    get_MaximumRecordLength: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                       _type.HRESULT]
    put_ScreenshotDestinationFolder: _Callable[[_Windows_Storage.IStorageFolder],  # value
                                               _type.HRESULT]
    get_ScreenshotDestinationFolder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                               _type.HRESULT]
    put_VideoEncodingBitrateMode: _Callable[[_enum.Windows.Media.Capture.AppCaptureVideoEncodingBitrateMode],  # value
                                            _type.HRESULT]
    get_VideoEncodingBitrateMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureVideoEncodingBitrateMode]],  # value
                                            _type.HRESULT]
    put_VideoEncodingResolutionMode: _Callable[[_enum.Windows.Media.Capture.AppCaptureVideoEncodingResolutionMode],  # value
                                               _type.HRESULT]
    get_VideoEncodingResolutionMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureVideoEncodingResolutionMode]],  # value
                                               _type.HRESULT]
    put_IsAppCaptureEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsAppCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsCpuConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_IsDisabledByPolicy: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_IsMemoryConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_HasHardwareEncoder: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IAppCaptureSettings2(_inspectable.IInspectable):
    get_IsGpuConstrained: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_AlternateShortcutKeys: _Callable[[_Pointer[IAppCaptureAlternateShortcutKeys]],  # value
                                         _type.HRESULT]


class IAppCaptureSettings3(_inspectable.IInspectable):
    put_IsMicrophoneCaptureEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_IsMicrophoneCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]


class IAppCaptureSettings4(_inspectable.IInspectable):
    put_IsMicrophoneCaptureEnabledByDefault: _Callable[[_type.boolean],  # value
                                                       _type.HRESULT]
    get_IsMicrophoneCaptureEnabledByDefault: _Callable[[_Pointer[_type.boolean]],  # value
                                                       _type.HRESULT]
    put_SystemAudioGain: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_SystemAudioGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_MicrophoneGain: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_MicrophoneGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_VideoEncodingFrameRateMode: _Callable[[_enum.Windows.Media.Capture.AppCaptureVideoEncodingFrameRateMode],  # value
                                              _type.HRESULT]
    get_VideoEncodingFrameRateMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureVideoEncodingFrameRateMode]],  # value
                                              _type.HRESULT]


class IAppCaptureSettings5(_inspectable.IInspectable):
    put_IsEchoCancellationEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsEchoCancellationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsCursorImageCaptureEnabled: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IsCursorImageCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IAppCaptureState(_inspectable.IInspectable):
    get_IsTargetRunning: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsHistoricalCaptureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_ShouldCaptureMicrophone: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_ShouldCaptureMicrophone: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    RestartMicrophoneCapture: _Callable[[],
                                        _type.HRESULT]
    get_MicrophoneCaptureState: _Callable[[_Pointer[_enum.Windows.Media.Capture.AppCaptureMicrophoneCaptureState]],  # value
                                          _type.HRESULT]
    get_MicrophoneCaptureError: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    add_MicrophoneCaptureStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCaptureState, IAppCaptureMicrophoneCaptureStateChangedEventArgs],  # value
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_MicrophoneCaptureStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    add_CaptureTargetClosed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppCaptureState, _inspectable.IInspectable],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_CaptureTargetClosed: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IAppCaptureStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[IAppCapture]],  # value
                                 _type.HRESULT]


class IAppCaptureStatics2(_inspectable.IInspectable, factory=True):
    SetAllowedAsync: _Callable[[_type.boolean,  # allowed
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]


class ICameraCaptureUI(_inspectable.IInspectable):
    get_PhotoSettings: _Callable[[_Pointer[ICameraCaptureUIPhotoCaptureSettings]],  # value
                                 _type.HRESULT]
    get_VideoSettings: _Callable[[_Pointer[ICameraCaptureUIVideoCaptureSettings]],  # value
                                 _type.HRESULT]
    CaptureFileAsync: _Callable[[_enum.Windows.Media.Capture.CameraCaptureUIMode,  # mode
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # asyncInfo
                                _type.HRESULT]


class ICameraCaptureUIPhotoCaptureSettings(_inspectable.IInspectable):
    get_Format: _Callable[[_Pointer[_enum.Windows.Media.Capture.CameraCaptureUIPhotoFormat]],  # value
                          _type.HRESULT]
    put_Format: _Callable[[_enum.Windows.Media.Capture.CameraCaptureUIPhotoFormat],  # value
                          _type.HRESULT]
    get_MaxResolution: _Callable[[_Pointer[_enum.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution]],  # value
                                 _type.HRESULT]
    put_MaxResolution: _Callable[[_enum.Windows.Media.Capture.CameraCaptureUIMaxPhotoResolution],  # value
                                 _type.HRESULT]
    get_CroppedSizeInPixels: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                       _type.HRESULT]
    put_CroppedSizeInPixels: _Callable[[_struct.Windows.Foundation.Size],  # value
                                       _type.HRESULT]
    get_CroppedAspectRatio: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                                      _type.HRESULT]
    put_CroppedAspectRatio: _Callable[[_struct.Windows.Foundation.Size],  # value
                                      _type.HRESULT]
    get_AllowCropping: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AllowCropping: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class ICameraCaptureUIVideoCaptureSettings(_inspectable.IInspectable):
    get_Format: _Callable[[_Pointer[_enum.Windows.Media.Capture.CameraCaptureUIVideoFormat]],  # value
                          _type.HRESULT]
    put_Format: _Callable[[_enum.Windows.Media.Capture.CameraCaptureUIVideoFormat],  # value
                          _type.HRESULT]
    get_MaxResolution: _Callable[[_Pointer[_enum.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution]],  # value
                                 _type.HRESULT]
    put_MaxResolution: _Callable[[_enum.Windows.Media.Capture.CameraCaptureUIMaxVideoResolution],  # value
                                 _type.HRESULT]
    get_MaxDurationInSeconds: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_MaxDurationInSeconds: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    get_AllowTrimming: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AllowTrimming: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class ICameraOptionsUIStatics(_inspectable.IInspectable, factory=True):
    Show: _Callable[[IMediaCapture],  # mediaCapture
                    _type.HRESULT]


class ICapturedFrame(_inspectable.IInspectable):
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]


class ICapturedFrame2(_inspectable.IInspectable):
    get_ControlValues: _Callable[[_Pointer[ICapturedFrameControlValues]],  # value
                                 _type.HRESULT]
    get_BitmapProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _Windows_Graphics_Imaging.IBitmapTypedValue]]],  # value
                                    _type.HRESULT]


class ICapturedFrameControlValues(_inspectable.IInspectable):
    get_Exposure: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    get_ExposureCompensation: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                        _type.HRESULT]
    get_IsoSpeed: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                            _type.HRESULT]
    get_Focus: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                         _type.HRESULT]
    get_SceneMode: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.Devices.CaptureSceneMode]]],  # value
                             _type.HRESULT]
    get_Flashed: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                           _type.HRESULT]
    get_FlashPowerPercent: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                                     _type.HRESULT]
    get_WhiteBalance: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                _type.HRESULT]
    get_ZoomFactor: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.FLOAT]]],  # value
                              _type.HRESULT]


class ICapturedFrameControlValues2(_inspectable.IInspectable):
    get_FocusState: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.Devices.MediaCaptureFocusState]]],  # value
                              _type.HRESULT]
    get_IsoDigitalGain: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                  _type.HRESULT]
    get_IsoAnalogGain: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.DOUBLE]]],  # value
                                 _type.HRESULT]
    get_SensorFrameRate: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                                   _type.HRESULT]
    get_WhiteBalanceGain: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Media.Capture.WhiteBalanceGain]]],  # value
                                    _type.HRESULT]


class ICapturedFrameWithSoftwareBitmap(_inspectable.IInspectable):
    get_SoftwareBitmap: _Callable[[_Pointer[_Windows_Graphics_Imaging.ISoftwareBitmap]],  # value
                                  _type.HRESULT]


class ICapturedPhoto(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[ICapturedFrame]],  # value
                         _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[ICapturedFrame]],  # value
                             _type.HRESULT]


class IGameBarServices(_inspectable.IInspectable):
    get_TargetCapturePolicy: _Callable[[_Pointer[_enum.Windows.Media.Capture.GameBarTargetCapturePolicy]],  # value
                                       _type.HRESULT]
    EnableCapture: _Callable[[],
                             _type.HRESULT]
    DisableCapture: _Callable[[],
                              _type.HRESULT]
    get_TargetInfo: _Callable[[_Pointer[IGameBarServicesTargetInfo]],  # value
                              _type.HRESULT]
    get_SessionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_AppBroadcastServices: _Callable[[_Pointer[IAppBroadcastServices]],  # value
                                        _type.HRESULT]
    get_AppCaptureServices: _Callable[[_Pointer[IAppCaptureServices]],  # value
                                      _type.HRESULT]
    add_CommandReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IGameBarServices, IGameBarServicesCommandEventArgs],  # value
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_CommandReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IGameBarServicesCommandEventArgs(_inspectable.IInspectable):
    get_Command: _Callable[[_Pointer[_enum.Windows.Media.Capture.GameBarCommand]],  # value
                           _type.HRESULT]
    get_Origin: _Callable[[_Pointer[_enum.Windows.Media.Capture.GameBarCommandOrigin]],  # value
                          _type.HRESULT]


class IGameBarServicesManager(_inspectable.IInspectable):
    add_GameBarServicesCreated: _Callable[[_Windows_Foundation.ITypedEventHandler[IGameBarServicesManager, IGameBarServicesManagerGameBarServicesCreatedEventArgs],  # value
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_GameBarServicesCreated: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class IGameBarServicesManagerGameBarServicesCreatedEventArgs(_inspectable.IInspectable):
    get_GameBarServices: _Callable[[_Pointer[IGameBarServices]],  # value
                                   _type.HRESULT]


class IGameBarServicesManagerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IGameBarServicesManager]],  # ppInstance
                          _type.HRESULT]


class IGameBarServicesTargetInfo(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_AppId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_TitleId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_DisplayMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.GameBarServicesDisplayMode]],  # value
                               _type.HRESULT]


class ILowLagMediaRecording(_inspectable.IInspectable):
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    FinishAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class ILowLagMediaRecording2(_inspectable.IInspectable):
    PauseAsync: _Callable[[_enum.Windows.Media.Devices.MediaCapturePauseBehavior,  # behavior
                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    ResumeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class ILowLagMediaRecording3(_inspectable.IInspectable):
    PauseWithResultAsync: _Callable[[_enum.Windows.Media.Devices.MediaCapturePauseBehavior,  # behavior
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IMediaCapturePauseResult]]],  # operation
                                    _type.HRESULT]
    StopWithResultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMediaCaptureStopResult]]],  # operation
                                   _type.HRESULT]


class ILowLagPhotoCapture(_inspectable.IInspectable):
    CaptureAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ICapturedPhoto]]],  # operation
                            _type.HRESULT]
    FinishAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class ILowLagPhotoSequenceCapture(_inspectable.IInspectable):
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    FinishAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    add_PhotoCaptured: _Callable[[_Windows_Foundation.ITypedEventHandler[ILowLagPhotoSequenceCapture, IPhotoCapturedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PhotoCaptured: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IMediaCapture(_inspectable.IInspectable):
    InitializeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                               _type.HRESULT]
    InitializeWithSettingsAsync: _Callable[[IMediaCaptureInitializationSettings,  # mediaCaptureInitializationSettings
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                           _type.HRESULT]
    StartRecordToStorageFileAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                              _Windows_Storage.IStorageFile,  # file
                                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                             _type.HRESULT]
    StartRecordToStreamAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                         _Windows_Storage_Streams.IRandomAccessStream,  # stream
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                        _type.HRESULT]
    StartRecordToCustomSinkAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                             _Windows_Media.IMediaExtension,  # customMediaSink
                                             _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                            _type.HRESULT]
    StartRecordToCustomSinkIdAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                               _type.HSTRING,  # customSinkActivationId
                                               _Windows_Foundation_Collections.IPropertySet,  # customSinkSettings
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                              _type.HRESULT]
    StopRecordAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                               _type.HRESULT]
    CapturePhotoToStorageFileAsync: _Callable[[_Windows_Media_MediaProperties.IImageEncodingProperties,  # type
                                               _Windows_Storage.IStorageFile,  # file
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                              _type.HRESULT]
    CapturePhotoToStreamAsync: _Callable[[_Windows_Media_MediaProperties.IImageEncodingProperties,  # type
                                          _Windows_Storage_Streams.IRandomAccessStream,  # stream
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                         _type.HRESULT]
    AddEffectAsync: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                               _type.HSTRING,  # effectActivationID
                               _Windows_Foundation_Collections.IPropertySet,  # effectSettings
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                              _type.HRESULT]
    ClearEffectsAsync: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                 _type.HRESULT]
    SetEncoderProperty: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                   _struct.GUID,  # propertyId
                                   _inspectable.IInspectable],  # propertyValue
                                  _type.HRESULT]
    GetEncoderProperty: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                   _struct.GUID,  # propertyId
                                   _Pointer[_inspectable.IInspectable]],  # propertyValue
                                  _type.HRESULT]
    add_Failed: _Callable[[IMediaCaptureFailedEventHandler,  # errorEventHandler
                           _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                          _type.HRESULT]
    remove_Failed: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                             _type.HRESULT]
    add_RecordLimitationExceeded: _Callable[[IRecordLimitationExceededEventHandler,  # recordLimitationExceededEventHandler
                                             _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                            _type.HRESULT]
    remove_RecordLimitationExceeded: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                               _type.HRESULT]
    get_MediaCaptureSettings: _Callable[[_Pointer[IMediaCaptureSettings]],  # value
                                        _type.HRESULT]
    get_AudioDeviceController: _Callable[[_Pointer[_Windows_Media_Devices.IAudioDeviceController]],  # value
                                         _type.HRESULT]
    get_VideoDeviceController: _Callable[[_Pointer[_Windows_Media_Devices.IVideoDeviceController]],  # value
                                         _type.HRESULT]
    SetPreviewMirroring: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    GetPreviewMirroring: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    SetPreviewRotation: _Callable[[_enum.Windows.Media.Capture.VideoRotation],  # value
                                  _type.HRESULT]
    GetPreviewRotation: _Callable[[_Pointer[_enum.Windows.Media.Capture.VideoRotation]],  # value
                                  _type.HRESULT]
    SetRecordRotation: _Callable[[_enum.Windows.Media.Capture.VideoRotation],  # value
                                 _type.HRESULT]
    GetRecordRotation: _Callable[[_Pointer[_enum.Windows.Media.Capture.VideoRotation]],  # value
                                 _type.HRESULT]


class IMediaCapture2(_inspectable.IInspectable):
    PrepareLowLagRecordToStorageFileAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                                      _Windows_Storage.IStorageFile,  # file
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[ILowLagMediaRecording]]],  # operation
                                                     _type.HRESULT]
    PrepareLowLagRecordToStreamAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                                 _Windows_Storage_Streams.IRandomAccessStream,  # stream
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[ILowLagMediaRecording]]],  # operation
                                                _type.HRESULT]
    PrepareLowLagRecordToCustomSinkAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                                     _Windows_Media.IMediaExtension,  # customMediaSink
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[ILowLagMediaRecording]]],  # operation
                                                    _type.HRESULT]
    PrepareLowLagRecordToCustomSinkIdAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                                       _type.HSTRING,  # customSinkActivationId
                                                       _Windows_Foundation_Collections.IPropertySet,  # customSinkSettings
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[ILowLagMediaRecording]]],  # operation
                                                      _type.HRESULT]
    PrepareLowLagPhotoCaptureAsync: _Callable[[_Windows_Media_MediaProperties.IImageEncodingProperties,  # type
                                               _Pointer[_Windows_Foundation.IAsyncOperation[ILowLagPhotoCapture]]],  # operation
                                              _type.HRESULT]
    PrepareLowLagPhotoSequenceCaptureAsync: _Callable[[_Windows_Media_MediaProperties.IImageEncodingProperties,  # type
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[ILowLagPhotoSequenceCapture]]],  # operation
                                                      _type.HRESULT]
    SetEncodingPropertiesAsync: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                           _Windows_Media_MediaProperties.IMediaEncodingProperties,  # mediaEncodingProperties
                                           _Windows_Foundation_Collections.IMap[_struct.GUID, _inspectable.IInspectable],  # encoderProperties
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                          _type.HRESULT]


class IMediaCapture3(_inspectable.IInspectable):
    PrepareVariablePhotoSequenceCaptureAsync: _Callable[[_Windows_Media_MediaProperties.IImageEncodingProperties,  # type
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Capture_Core.IVariablePhotoSequenceCapture]]],  # operation
                                                        _type.HRESULT]
    add_FocusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaCapture, IMediaCaptureFocusChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FocusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_PhotoConfirmationCaptured: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaCapture, IPhotoConfirmationCapturedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_PhotoConfirmationCaptured: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]


class IMediaCapture4(_inspectable.IInspectable):
    AddAudioEffectAsync: _Callable[[_Windows_Media_Effects.IAudioEffectDefinition,  # definition
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media.IMediaExtension]]],  # op
                                   _type.HRESULT]
    AddVideoEffectAsync: _Callable[[_Windows_Media_Effects.IVideoEffectDefinition,  # definition
                                    _enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media.IMediaExtension]]],  # op
                                   _type.HRESULT]
    PauseRecordAsync: _Callable[[_enum.Windows.Media.Devices.MediaCapturePauseBehavior,  # behavior
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                _type.HRESULT]
    ResumeRecordAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                 _type.HRESULT]
    add_CameraStreamStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaCapture, _inspectable.IInspectable],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_CameraStreamStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    get_CameraStreamState: _Callable[[_Pointer[_enum.Windows.Media.Devices.CameraStreamState]],  # streamState
                                     _type.HRESULT]
    GetPreviewFrameAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media.IVideoFrame]]],  # operation
                                    _type.HRESULT]
    GetPreviewFrameCopyAsync: _Callable[[_Windows_Media.IVideoFrame,  # destination
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media.IVideoFrame]]],  # operation
                                        _type.HRESULT]
    add_ThermalStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaCapture, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ThermalStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_ThermalStatus: _Callable[[_Pointer[_enum.Windows.Media.Capture.MediaCaptureThermalStatus]],  # value
                                 _type.HRESULT]
    PrepareAdvancedPhotoCaptureAsync: _Callable[[_Windows_Media_MediaProperties.IImageEncodingProperties,  # encodingProperties
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IAdvancedPhotoCapture]]],  # operation
                                                _type.HRESULT]


class IMediaCapture5(_inspectable.IInspectable):
    RemoveEffectAsync: _Callable[[_Windows_Media.IMediaExtension,  # effect
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                 _type.HRESULT]
    PauseRecordWithResultAsync: _Callable[[_enum.Windows.Media.Devices.MediaCapturePauseBehavior,  # behavior
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IMediaCapturePauseResult]]],  # operation
                                          _type.HRESULT]
    StopRecordWithResultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IMediaCaptureStopResult]]],  # operation
                                         _type.HRESULT]
    get_FrameSources: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _Windows_Media_Capture_Frames.IMediaFrameSource]]],  # value
                                _type.HRESULT]
    CreateFrameReaderAsync: _Callable[[_Windows_Media_Capture_Frames.IMediaFrameSource,  # inputSource
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Capture_Frames.IMediaFrameReader]]],  # value
                                      _type.HRESULT]
    CreateFrameReaderWithSubtypeAsync: _Callable[[_Windows_Media_Capture_Frames.IMediaFrameSource,  # inputSource
                                                  _type.HSTRING,  # outputSubtype
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Capture_Frames.IMediaFrameReader]]],  # value
                                                 _type.HRESULT]
    CreateFrameReaderWithSubtypeAndSizeAsync: _Callable[[_Windows_Media_Capture_Frames.IMediaFrameSource,  # inputSource
                                                         _type.HSTRING,  # outputSubtype
                                                         _struct.Windows.Graphics.Imaging.BitmapSize,  # outputSize
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Capture_Frames.IMediaFrameReader]]],  # value
                                                        _type.HRESULT]


class IMediaCapture6(_inspectable.IInspectable):
    add_CaptureDeviceExclusiveControlStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaCapture, IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs],  # handler
                                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                                              _type.HRESULT]
    remove_CaptureDeviceExclusiveControlStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                                 _type.HRESULT]
    CreateMultiSourceFrameReaderAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Media_Capture_Frames.IMediaFrameSource],  # inputSources
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Capture_Frames.IMultiSourceMediaFrameReader]]],  # value
                                                 _type.HRESULT]


class IMediaCapture7(_inspectable.IInspectable):
    CreateRelativePanelWatcher: _Callable[[_enum.Windows.Media.Capture.StreamingCaptureMode,  # captureMode
                                           _Windows_UI_WindowManagement.IDisplayRegion,  # displayRegion
                                           _Pointer[IMediaCaptureRelativePanelWatcher]],  # result
                                          _type.HRESULT]


class IMediaCaptureDeviceExclusiveControlStatusChangedEventArgs(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlStatus]],  # value
                          _type.HRESULT]


class IMediaCaptureFailedEventArgs(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Code: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]


class IMediaCaptureFocusChangedEventArgs(_inspectable.IInspectable):
    get_FocusState: _Callable[[_Pointer[_enum.Windows.Media.Devices.MediaCaptureFocusState]],  # value
                              _type.HRESULT]


class IMediaCaptureInitializationSettings(_inspectable.IInspectable):
    put_AudioDeviceId: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_AudioDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_VideoDeviceId: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_VideoDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_StreamingCaptureMode: _Callable[[_enum.Windows.Media.Capture.StreamingCaptureMode],  # value
                                        _type.HRESULT]
    get_StreamingCaptureMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.StreamingCaptureMode]],  # value
                                        _type.HRESULT]
    put_PhotoCaptureSource: _Callable[[_enum.Windows.Media.Capture.PhotoCaptureSource],  # value
                                      _type.HRESULT]
    get_PhotoCaptureSource: _Callable[[_Pointer[_enum.Windows.Media.Capture.PhotoCaptureSource]],  # value
                                      _type.HRESULT]


class IMediaCaptureInitializationSettings2(_inspectable.IInspectable):
    put_MediaCategory: _Callable[[_enum.Windows.Media.Capture.MediaCategory],  # value
                                 _type.HRESULT]
    get_MediaCategory: _Callable[[_Pointer[_enum.Windows.Media.Capture.MediaCategory]],  # value
                                 _type.HRESULT]
    put_AudioProcessing: _Callable[[_enum.Windows.Media.AudioProcessing],  # value
                                   _type.HRESULT]
    get_AudioProcessing: _Callable[[_Pointer[_enum.Windows.Media.AudioProcessing]],  # value
                                   _type.HRESULT]


class IMediaCaptureInitializationSettings3(_inspectable.IInspectable):
    put_AudioSource: _Callable[[_Windows_Media_Core.IMediaSource],  # value
                               _type.HRESULT]
    get_AudioSource: _Callable[[_Pointer[_Windows_Media_Core.IMediaSource]],  # value
                               _type.HRESULT]
    put_VideoSource: _Callable[[_Windows_Media_Core.IMediaSource],  # value
                               _type.HRESULT]
    get_VideoSource: _Callable[[_Pointer[_Windows_Media_Core.IMediaSource]],  # value
                               _type.HRESULT]


class IMediaCaptureInitializationSettings4(_inspectable.IInspectable):
    get_VideoProfile: _Callable[[_Pointer[IMediaCaptureVideoProfile]],  # value
                                _type.HRESULT]
    put_VideoProfile: _Callable[[IMediaCaptureVideoProfile],  # value
                                _type.HRESULT]
    get_PreviewMediaDescription: _Callable[[_Pointer[IMediaCaptureVideoProfileMediaDescription]],  # value
                                           _type.HRESULT]
    put_PreviewMediaDescription: _Callable[[IMediaCaptureVideoProfileMediaDescription],  # value
                                           _type.HRESULT]
    get_RecordMediaDescription: _Callable[[_Pointer[IMediaCaptureVideoProfileMediaDescription]],  # value
                                          _type.HRESULT]
    put_RecordMediaDescription: _Callable[[IMediaCaptureVideoProfileMediaDescription],  # value
                                          _type.HRESULT]
    get_PhotoMediaDescription: _Callable[[_Pointer[IMediaCaptureVideoProfileMediaDescription]],  # value
                                         _type.HRESULT]
    put_PhotoMediaDescription: _Callable[[IMediaCaptureVideoProfileMediaDescription],  # value
                                         _type.HRESULT]


class IMediaCaptureInitializationSettings5(_inspectable.IInspectable):
    get_SourceGroup: _Callable[[_Pointer[_Windows_Media_Capture_Frames.IMediaFrameSourceGroup]],  # value
                               _type.HRESULT]
    put_SourceGroup: _Callable[[_Windows_Media_Capture_Frames.IMediaFrameSourceGroup],  # value
                               _type.HRESULT]
    get_SharingMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.MediaCaptureSharingMode]],  # value
                               _type.HRESULT]
    put_SharingMode: _Callable[[_enum.Windows.Media.Capture.MediaCaptureSharingMode],  # value
                               _type.HRESULT]
    get_MemoryPreference: _Callable[[_Pointer[_enum.Windows.Media.Capture.MediaCaptureMemoryPreference]],  # value
                                    _type.HRESULT]
    put_MemoryPreference: _Callable[[_enum.Windows.Media.Capture.MediaCaptureMemoryPreference],  # value
                                    _type.HRESULT]


class IMediaCaptureInitializationSettings6(_inspectable.IInspectable):
    get_AlwaysPlaySystemShutterSound: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_AlwaysPlaySystemShutterSound: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]


class IMediaCaptureInitializationSettings7(_inspectable.IInspectable):
    get_DeviceUriPasswordCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # value
                                               _type.HRESULT]
    put_DeviceUriPasswordCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # value
                                               _type.HRESULT]
    get_DeviceUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    put_DeviceUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                             _type.HRESULT]


class IMediaCapturePauseResult(_inspectable.IInspectable):
    get_LastFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                             _type.HRESULT]
    get_RecordDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]


class IMediaCaptureRelativePanelWatcher(_inspectable.IInspectable):
    get_RelativePanel: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.Panel]],  # value
                                 _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaCaptureRelativePanelWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IMediaCaptureSettings(_inspectable.IInspectable):
    get_AudioDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_VideoDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_StreamingCaptureMode: _Callable[[_Pointer[_enum.Windows.Media.Capture.StreamingCaptureMode]],  # value
                                        _type.HRESULT]
    get_PhotoCaptureSource: _Callable[[_Pointer[_enum.Windows.Media.Capture.PhotoCaptureSource]],  # value
                                      _type.HRESULT]
    get_VideoDeviceCharacteristic: _Callable[[_Pointer[_enum.Windows.Media.Capture.VideoDeviceCharacteristic]],  # value
                                             _type.HRESULT]


class IMediaCaptureSettings2(_inspectable.IInspectable):
    get_ConcurrentRecordAndPhotoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    get_ConcurrentRecordAndPhotoSequenceSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    get_CameraSoundRequiredForRegion: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    get_Horizontal35mmEquivalentFocalLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                       _type.HRESULT]
    get_PitchOffsetDegrees: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                      _type.HRESULT]
    get_Vertical35mmEquivalentFocalLength: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                     _type.HRESULT]
    get_MediaCategory: _Callable[[_Pointer[_enum.Windows.Media.Capture.MediaCategory]],  # value
                                 _type.HRESULT]
    get_AudioProcessing: _Callable[[_Pointer[_enum.Windows.Media.AudioProcessing]],  # value
                                   _type.HRESULT]


class IMediaCaptureSettings3(_inspectable.IInspectable):
    get_Direct3D11Device: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice]],  # value
                                    _type.HRESULT]


class IMediaCaptureStatics(_inspectable.IInspectable, factory=True):
    IsVideoProfileSupported: _Callable[[_type.HSTRING,  # videoDeviceId
                                        _Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    FindAllVideoProfiles: _Callable[[_type.HSTRING,  # videoDeviceId
                                     _Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCaptureVideoProfile]]],  # value
                                    _type.HRESULT]
    FindConcurrentProfiles: _Callable[[_type.HSTRING,  # videoDeviceId
                                       _Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCaptureVideoProfile]]],  # value
                                      _type.HRESULT]
    FindKnownVideoProfiles: _Callable[[_type.HSTRING,  # videoDeviceId
                                       _enum.Windows.Media.Capture.KnownVideoProfile,  # name
                                       _Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCaptureVideoProfile]]],  # value
                                      _type.HRESULT]


class IMediaCaptureStopResult(_inspectable.IInspectable):
    get_LastFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                             _type.HRESULT]
    get_RecordDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]


class IMediaCaptureVideoPreview(_inspectable.IInspectable):
    StartPreviewAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                 _type.HRESULT]
    StartPreviewToCustomSinkAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                              _Windows_Media.IMediaExtension,  # customMediaSink
                                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                             _type.HRESULT]
    StartPreviewToCustomSinkIdAsync: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProfile,  # encodingProfile
                                                _type.HSTRING,  # customSinkActivationId
                                                _Windows_Foundation_Collections.IPropertySet,  # customSinkSettings
                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                               _type.HRESULT]
    StopPreviewAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                _type.HRESULT]


class IMediaCaptureVideoProfile(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_VideoDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_SupportedPreviewMediaDescription: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCaptureVideoProfileMediaDescription]]],  # value
                                                    _type.HRESULT]
    get_SupportedRecordMediaDescription: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCaptureVideoProfileMediaDescription]]],  # value
                                                   _type.HRESULT]
    get_SupportedPhotoMediaDescription: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCaptureVideoProfileMediaDescription]]],  # value
                                                  _type.HRESULT]
    GetConcurrency: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IMediaCaptureVideoProfile]]],  # value
                              _type.HRESULT]


class IMediaCaptureVideoProfile2(_inspectable.IInspectable):
    get_FrameSourceInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_Capture_Frames.IMediaFrameSourceInfo]]],  # value
                                    _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IMediaCaptureVideoProfileMediaDescription(_inspectable.IInspectable):
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_FrameRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    IsVariablePhotoSequenceSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    IsHdrVideoSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IMediaCaptureVideoProfileMediaDescription2(_inspectable.IInspectable):
    get_Subtype: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, _inspectable.IInspectable]]],  # value
                              _type.HRESULT]


class IOptionalReferencePhotoCapturedEventArgs(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[ICapturedFrame]],  # value
                         _type.HRESULT]
    get_Context: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]


class IPhotoCapturedEventArgs(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[ICapturedFrame]],  # value
                         _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[ICapturedFrame]],  # value
                             _type.HRESULT]
    get_CaptureTimeOffset: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]


class IPhotoConfirmationCapturedEventArgs(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[ICapturedFrame]],  # value
                         _type.HRESULT]
    get_CaptureTimeOffset: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]


class IVideoStreamConfiguration(_inspectable.IInspectable):
    get_InputProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IVideoEncodingProperties]],  # value
                                   _type.HRESULT]
    get_OutputProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IVideoEncodingProperties]],  # value
                                    _type.HRESULT]
