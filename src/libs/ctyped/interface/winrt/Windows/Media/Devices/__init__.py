from __future__ import annotations

from typing import Callable as _Callable

from . import Core as _Windows_Media_Devices_Core
from .. import MediaProperties as _Windows_Media_MediaProperties
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _ICallControlEventHandler:
    Invoke: _Callable[[ICallControl],  # sender
                      _type.HRESULT]


class ICallControlEventHandler(_ICallControlEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICallControlEventHandler_impl(_ICallControlEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IDialRequestedEventHandler:
    Invoke: _Callable[[ICallControl,  # sender
                       IDialRequestedEventArgs],  # e
                      _type.HRESULT]


class IDialRequestedEventHandler(_IDialRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDialRequestedEventHandler_impl(_IDialRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IKeypadPressedEventHandler:
    Invoke: _Callable[[ICallControl,  # sender
                       IKeypadPressedEventArgs],  # e
                      _type.HRESULT]


class IKeypadPressedEventHandler(_IKeypadPressedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IKeypadPressedEventHandler_impl(_IKeypadPressedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IRedialRequestedEventHandler:
    Invoke: _Callable[[ICallControl,  # sender
                       IRedialRequestedEventArgs],  # e
                      _type.HRESULT]


class IRedialRequestedEventHandler(_IRedialRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IRedialRequestedEventHandler_impl(_IRedialRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAdvancedPhotoCaptureSettings(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.AdvancedPhotoMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Devices.AdvancedPhotoMode],  # value
                        _type.HRESULT]


class IAdvancedPhotoControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_SupportedModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.AdvancedPhotoMode]]],  # value
                                  _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.AdvancedPhotoMode]],  # value
                        _type.HRESULT]
    Configure: _Callable[[IAdvancedPhotoCaptureSettings],  # settings
                         _type.HRESULT]


class IAdvancedVideoCaptureDeviceController(_inspectable.IInspectable):
    SetDeviceProperty: _Callable[[_type.HSTRING,  # propertyId
                                  _inspectable.IInspectable],  # propertyValue
                                 _type.HRESULT]
    GetDeviceProperty: _Callable[[_type.HSTRING,  # propertyId
                                  _Pointer[_inspectable.IInspectable]],  # propertyValue
                                 _type.HRESULT]


class IAdvancedVideoCaptureDeviceController10(_inspectable.IInspectable):
    get_CameraOcclusionInfo: _Callable[[_Pointer[ICameraOcclusionInfo]],  # value
                                       _type.HRESULT]


class IAdvancedVideoCaptureDeviceController11(_inspectable.IInspectable):
    TryAcquireExclusiveControl: _Callable[[_type.HSTRING,  # deviceId
                                           _enum.Windows.Media.Capture.MediaCaptureDeviceExclusiveControlReleaseMode,  # mode
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]


class IAdvancedVideoCaptureDeviceController2(_inspectable.IInspectable):
    get_LowLagPhotoSequence: _Callable[[_Pointer[ILowLagPhotoSequenceControl]],  # value
                                       _type.HRESULT]
    get_LowLagPhoto: _Callable[[_Pointer[ILowLagPhotoControl]],  # value
                               _type.HRESULT]
    get_SceneModeControl: _Callable[[_Pointer[ISceneModeControl]],  # value
                                    _type.HRESULT]
    get_TorchControl: _Callable[[_Pointer[ITorchControl]],  # value
                                _type.HRESULT]
    get_FlashControl: _Callable[[_Pointer[IFlashControl]],  # value
                                _type.HRESULT]
    get_WhiteBalanceControl: _Callable[[_Pointer[IWhiteBalanceControl]],  # value
                                       _type.HRESULT]
    get_ExposureControl: _Callable[[_Pointer[IExposureControl]],  # value
                                   _type.HRESULT]
    get_FocusControl: _Callable[[_Pointer[IFocusControl]],  # value
                                _type.HRESULT]
    get_ExposureCompensationControl: _Callable[[_Pointer[IExposureCompensationControl]],  # value
                                               _type.HRESULT]
    get_IsoSpeedControl: _Callable[[_Pointer[IIsoSpeedControl]],  # value
                                   _type.HRESULT]
    get_RegionsOfInterestControl: _Callable[[_Pointer[IRegionsOfInterestControl]],  # value
                                            _type.HRESULT]
    get_PrimaryUse: _Callable[[_Pointer[_enum.Windows.Media.Devices.CaptureUse]],  # value
                              _type.HRESULT]
    put_PrimaryUse: _Callable[[_enum.Windows.Media.Devices.CaptureUse],  # value
                              _type.HRESULT]


class IAdvancedVideoCaptureDeviceController3(_inspectable.IInspectable):
    get_VariablePhotoSequenceController: _Callable[[_Pointer[_Windows_Media_Devices_Core.IVariablePhotoSequenceController]],  # value
                                                   _type.HRESULT]
    get_PhotoConfirmationControl: _Callable[[_Pointer[IPhotoConfirmationControl]],  # value
                                            _type.HRESULT]
    get_ZoomControl: _Callable[[_Pointer[IZoomControl]],  # value
                               _type.HRESULT]


class IAdvancedVideoCaptureDeviceController4(_inspectable.IInspectable):
    get_ExposurePriorityVideoControl: _Callable[[_Pointer[IExposurePriorityVideoControl]],  # value
                                                _type.HRESULT]
    get_DesiredOptimization: _Callable[[_Pointer[_enum.Windows.Media.Devices.MediaCaptureOptimization]],  # value
                                       _type.HRESULT]
    put_DesiredOptimization: _Callable[[_enum.Windows.Media.Devices.MediaCaptureOptimization],  # value
                                       _type.HRESULT]
    get_HdrVideoControl: _Callable[[_Pointer[IHdrVideoControl]],  # value
                                   _type.HRESULT]
    get_OpticalImageStabilizationControl: _Callable[[_Pointer[IOpticalImageStabilizationControl]],  # value
                                                    _type.HRESULT]
    get_AdvancedPhotoControl: _Callable[[_Pointer[IAdvancedPhotoControl]],  # value
                                        _type.HRESULT]


class IAdvancedVideoCaptureDeviceController5(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    GetDevicePropertyById: _Callable[[_type.HSTRING,  # propertyId
                                      _Windows_Foundation.IReference[_type.UINT32],  # maxPropertyValueSize
                                      _Pointer[IVideoDeviceControllerGetDevicePropertyResult]],  # value
                                     _type.HRESULT]
    SetDevicePropertyById: _Callable[[_type.HSTRING,  # propertyId
                                      _inspectable.IInspectable,  # propertyValue
                                      _Pointer[_enum.Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus]],  # value
                                     _type.HRESULT]
    GetDevicePropertyByExtendedId: _Callable[[_type.UINT32,  # __extendedPropertyIdSize
                                              _Pointer[_type.BYTE],  # extendedPropertyId
                                              _Windows_Foundation.IReference[_type.UINT32],  # maxPropertyValueSize
                                              _Pointer[IVideoDeviceControllerGetDevicePropertyResult]],  # value
                                             _type.HRESULT]
    SetDevicePropertyByExtendedId: _Callable[[_type.UINT32,  # __extendedPropertyIdSize
                                              _Pointer[_type.BYTE],  # extendedPropertyId
                                              _type.UINT32,  # __propertyValueSize
                                              _Pointer[_type.BYTE],  # propertyValue
                                              _Pointer[_enum.Windows.Media.Devices.VideoDeviceControllerSetDevicePropertyStatus]],  # value
                                             _type.HRESULT]


class IAdvancedVideoCaptureDeviceController6(_inspectable.IInspectable):
    get_VideoTemporalDenoisingControl: _Callable[[_Pointer[IVideoTemporalDenoisingControl]],  # value
                                                 _type.HRESULT]


class IAdvancedVideoCaptureDeviceController7(_inspectable.IInspectable):
    get_InfraredTorchControl: _Callable[[_Pointer[IInfraredTorchControl]],  # value
                                        _type.HRESULT]


class IAdvancedVideoCaptureDeviceController8(_inspectable.IInspectable):
    get_PanelBasedOptimizationControl: _Callable[[_Pointer[IPanelBasedOptimizationControl]],  # value
                                                 _type.HRESULT]


class IAdvancedVideoCaptureDeviceController9(_inspectable.IInspectable):
    get_DigitalWindowControl: _Callable[[_Pointer[IDigitalWindowControl]],  # value
                                        _type.HRESULT]


class IAudioDeviceController(_inspectable.IInspectable):
    put_Muted: _Callable[[_type.boolean],  # value
                         _type.HRESULT]
    get_Muted: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]
    put_VolumePercent: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]
    get_VolumePercent: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]


class IAudioDeviceModule(_inspectable.IInspectable):
    get_ClassId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_InstanceId: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_MajorVersion: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_MinorVersion: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    SendCommandAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # Command
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IModuleCommandResult]]],  # operation
                                _type.HRESULT]


class IAudioDeviceModuleNotificationEventArgs(_inspectable.IInspectable):
    get_Module: _Callable[[_Pointer[IAudioDeviceModule]],  # value
                          _type.HRESULT]
    get_NotificationData: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                    _type.HRESULT]


class IAudioDeviceModulesManager(_inspectable.IInspectable):
    add_ModuleNotificationReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioDeviceModulesManager, IAudioDeviceModuleNotificationEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_ModuleNotificationReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    FindAllById: _Callable[[_type.HSTRING,  # moduleId
                            _Pointer[_Windows_Foundation_Collections.IVectorView[IAudioDeviceModule]]],  # modules
                           _type.HRESULT]
    FindAll: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAudioDeviceModule]]],  # modules
                       _type.HRESULT]


class IAudioDeviceModulesManagerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[IAudioDeviceModulesManager]],  # result
                      _type.HRESULT]

    _factory = True


class ICallControl(_inspectable.IInspectable):
    IndicateNewIncomingCall: _Callable[[_type.boolean,  # enableRinger
                                        _type.HSTRING,  # callerId
                                        _Pointer[_type.UINT64]],  # callToken
                                       _type.HRESULT]
    IndicateNewOutgoingCall: _Callable[[_Pointer[_type.UINT64]],  # callToken
                                       _type.HRESULT]
    IndicateActiveCall: _Callable[[_type.UINT64],  # callToken
                                  _type.HRESULT]
    EndCall: _Callable[[_type.UINT64],  # callToken
                       _type.HRESULT]
    get_HasRinger: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    add_AnswerRequested: _Callable[[ICallControlEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_AnswerRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_HangUpRequested: _Callable[[ICallControlEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_HangUpRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_DialRequested: _Callable[[IDialRequestedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_DialRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_RedialRequested: _Callable[[IRedialRequestedEventHandler,  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_RedialRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_KeypadPressed: _Callable[[IKeypadPressedEventHandler,  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_KeypadPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_AudioTransferRequested: _Callable[[ICallControlEventHandler,  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_AudioTransferRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]


class ICallControlStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[ICallControl]],  # callControl
                          _type.HRESULT]
    FromId: _Callable[[_type.HSTRING,  # deviceId
                       _Pointer[ICallControl]],  # callControl
                      _type.HRESULT]

    _factory = True


class ICameraOcclusionInfo(_inspectable.IInspectable):
    GetState: _Callable[[_Pointer[ICameraOcclusionState]],  # result
                        _type.HRESULT]
    IsOcclusionKindSupported: _Callable[[_enum.Windows.Media.Devices.CameraOcclusionKind,  # occlusionKind
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICameraOcclusionInfo, ICameraOcclusionStateChangedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class ICameraOcclusionState(_inspectable.IInspectable):
    get_IsOccluded: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    IsOcclusionKind: _Callable[[_enum.Windows.Media.Devices.CameraOcclusionKind,  # occlusionKind
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]


class ICameraOcclusionStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[ICameraOcclusionState]],  # value
                         _type.HRESULT]


class IDefaultAudioDeviceChangedEventArgs(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Role: _Callable[[_Pointer[_enum.Windows.Media.Devices.AudioDeviceRole]],  # value
                        _type.HRESULT]


class IDialRequestedEventArgs(_inspectable.IInspectable):
    Handled: _Callable[[],
                       _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                           _type.HRESULT]


class IDigitalWindowBounds(_inspectable.IInspectable):
    get_NormalizedOriginTop: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_NormalizedOriginTop: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_NormalizedOriginLeft: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_NormalizedOriginLeft: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_Scale: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Scale: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]


class IDigitalWindowCapability(_inspectable.IInspectable):
    get_Width: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_MinScaleValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_MaxScaleValue: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    get_MinScaleValueWithoutUpsampling: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                                  _type.HRESULT]
    get_NormalizedFieldOfViewLimit: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                              _type.HRESULT]


class IDigitalWindowControl(_inspectable.IInspectable):
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_SupportedModes: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                   _Pointer[_Pointer[_enum.Windows.Media.Devices.DigitalWindowMode]]],  # value
                                  _type.HRESULT]
    get_CurrentMode: _Callable[[_Pointer[_enum.Windows.Media.Devices.DigitalWindowMode]],  # value
                               _type.HRESULT]
    GetBounds: _Callable[[_Pointer[IDigitalWindowBounds]],  # result
                         _type.HRESULT]
    Configure: _Callable[[_enum.Windows.Media.Devices.DigitalWindowMode],  # digitalWindowMode
                         _type.HRESULT]
    ConfigureWithBounds: _Callable[[_enum.Windows.Media.Devices.DigitalWindowMode,  # digitalWindowMode
                                    IDigitalWindowBounds],  # digitalWindowBounds
                                   _type.HRESULT]
    get_SupportedCapabilities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDigitalWindowCapability]]],  # value
                                         _type.HRESULT]
    GetCapabilityForSize: _Callable[[_type.INT32,  # width
                                     _type.INT32,  # height
                                     _Pointer[IDigitalWindowCapability]],  # result
                                    _type.HRESULT]


class IExposureCompensationControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.FLOAT]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    SetValueAsync: _Callable[[_type.FLOAT,  # value
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                             _type.HRESULT]


class IExposureControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Auto: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    SetAutoAsync: _Callable[[_type.boolean,  # value
                             _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                            _type.HRESULT]
    get_Min: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                         _type.HRESULT]
    SetValueAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # shutterDuration
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                             _type.HRESULT]


class IExposurePriorityVideoControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IFlashControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_PowerSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_RedEyeReductionSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Auto: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    put_Auto: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    get_RedEyeReduction: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_RedEyeReduction: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_PowerPercent: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_PowerPercent: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]


class IFlashControl2(_inspectable.IInspectable):
    get_AssistantLightSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_AssistantLightEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_AssistantLightEnabled: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IFocusControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_SupportedPresets: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.FocusPreset]]],  # value
                                    _type.HRESULT]
    get_Preset: _Callable[[_Pointer[_enum.Windows.Media.Devices.FocusPreset]],  # value
                          _type.HRESULT]
    SetPresetAsync: _Callable[[_enum.Windows.Media.Devices.FocusPreset,  # preset
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                              _type.HRESULT]
    SetPresetWithCompletionOptionAsync: _Callable[[_enum.Windows.Media.Devices.FocusPreset,  # preset
                                                   _type.boolean,  # completeBeforeFocus
                                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                                  _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    SetValueAsync: _Callable[[_type.UINT32,  # focus
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                             _type.HRESULT]
    FocusAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                          _type.HRESULT]


class IFocusControl2(_inspectable.IInspectable):
    get_FocusChangedSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_WaitForFocusSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_SupportedFocusModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.FocusMode]]],  # value
                                       _type.HRESULT]
    get_SupportedFocusDistances: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.ManualFocusDistance]]],  # value
                                           _type.HRESULT]
    get_SupportedFocusRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.AutoFocusRange]]],  # value
                                        _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.FocusMode]],  # value
                        _type.HRESULT]
    get_FocusState: _Callable[[_Pointer[_enum.Windows.Media.Devices.MediaCaptureFocusState]],  # value
                              _type.HRESULT]
    UnlockAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                           _type.HRESULT]
    LockAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                         _type.HRESULT]
    Configure: _Callable[[IFocusSettings],  # settings
                         _type.HRESULT]


class IFocusSettings(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.FocusMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Devices.FocusMode],  # value
                        _type.HRESULT]
    get_AutoFocusRange: _Callable[[_Pointer[_enum.Windows.Media.Devices.AutoFocusRange]],  # value
                                  _type.HRESULT]
    put_AutoFocusRange: _Callable[[_enum.Windows.Media.Devices.AutoFocusRange],  # value
                                  _type.HRESULT]
    get_Value: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Distance: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Media.Devices.ManualFocusDistance]]],  # value
                            _type.HRESULT]
    put_Distance: _Callable[[_Windows_Foundation.IReference[_enum.Windows.Media.Devices.ManualFocusDistance]],  # value
                            _type.HRESULT]
    get_WaitForFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_WaitForFocus: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_DisableDriverFallback: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_DisableDriverFallback: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IHdrVideoControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_SupportedModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.HdrVideoMode]]],  # value
                                  _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.HdrVideoMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Devices.HdrVideoMode],  # value
                        _type.HRESULT]


class IInfraredTorchControl(_inspectable.IInspectable):
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_SupportedModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.InfraredTorchMode]]],  # value
                                  _type.HRESULT]
    get_CurrentMode: _Callable[[_Pointer[_enum.Windows.Media.Devices.InfraredTorchMode]],  # value
                               _type.HRESULT]
    put_CurrentMode: _Callable[[_enum.Windows.Media.Devices.InfraredTorchMode],  # value
                               _type.HRESULT]
    get_MinPower: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_MaxPower: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_PowerStep: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Power: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    put_Power: _Callable[[_type.INT32],  # value
                         _type.HRESULT]


class IIsoSpeedControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    SupportedPresets: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.IsoSpeedPreset]]],  # value
                                _type.HRESULT]
    Preset: _Callable[[_Pointer[_enum.Windows.Media.Devices.IsoSpeedPreset]],  # value
                      _type.HRESULT]
    SetPresetAsync: _Callable[[_enum.Windows.Media.Devices.IsoSpeedPreset,  # preset
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                              _type.HRESULT]


class IIsoSpeedControl2(_inspectable.IInspectable):
    get_Min: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    SetValueAsync: _Callable[[_type.UINT32,  # isoSpeed
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                             _type.HRESULT]
    get_Auto: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    SetAutoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                            _type.HRESULT]


class IKeypadPressedEventArgs(_inspectable.IInspectable):
    get_TelephonyKey: _Callable[[_Pointer[_enum.Windows.Media.Devices.TelephonyKey]],  # telephonyKey
                                _type.HRESULT]


class ILowLagPhotoControl(_inspectable.IInspectable):
    GetHighestConcurrentFrameRate: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProperties,  # captureProperties
                                              _Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                                             _type.HRESULT]
    GetCurrentFrameRate: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                                   _type.HRESULT]
    get_ThumbnailEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ThumbnailEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ThumbnailFormat: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.MediaThumbnailFormat]],  # value
                                   _type.HRESULT]
    put_ThumbnailFormat: _Callable[[_enum.Windows.Media.MediaProperties.MediaThumbnailFormat],  # value
                                   _type.HRESULT]
    get_DesiredThumbnailSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    put_DesiredThumbnailSize: _Callable[[_type.UINT32],  # value
                                        _type.HRESULT]
    get_HardwareAcceleratedThumbnailSupported: _Callable[[_Pointer[_type.UINT32]],  # value
                                                         _type.HRESULT]


class ILowLagPhotoSequenceControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_MaxPastPhotos: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_MaxPhotosPerSecond: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_PastPhotoLimit: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    put_PastPhotoLimit: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_PhotosPerSecondLimit: _Callable[[_Pointer[_type.FLOAT]],  # value
                                        _type.HRESULT]
    put_PhotosPerSecondLimit: _Callable[[_type.FLOAT],  # value
                                        _type.HRESULT]
    GetHighestConcurrentFrameRate: _Callable[[_Windows_Media_MediaProperties.IMediaEncodingProperties,  # captureProperties
                                              _Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                                             _type.HRESULT]
    GetCurrentFrameRate: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaRatio]],  # value
                                   _type.HRESULT]
    get_ThumbnailEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ThumbnailEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ThumbnailFormat: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.MediaThumbnailFormat]],  # value
                                   _type.HRESULT]
    put_ThumbnailFormat: _Callable[[_enum.Windows.Media.MediaProperties.MediaThumbnailFormat],  # value
                                   _type.HRESULT]
    get_DesiredThumbnailSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                        _type.HRESULT]
    put_DesiredThumbnailSize: _Callable[[_type.UINT32],  # value
                                        _type.HRESULT]
    get_HardwareAcceleratedThumbnailSupported: _Callable[[_Pointer[_type.UINT32]],  # value
                                                         _type.HRESULT]


class IMediaDeviceControl(_inspectable.IInspectable):
    get_Capabilities: _Callable[[_Pointer[IMediaDeviceControlCapabilities]],  # value
                                _type.HRESULT]
    TryGetValue: _Callable[[_Pointer[_type.DOUBLE],  # value
                            _Pointer[_type.boolean]],  # succeeded
                           _type.HRESULT]
    TrySetValue: _Callable[[_type.DOUBLE,  # value
                            _Pointer[_type.boolean]],  # succeeded
                           _type.HRESULT]
    TryGetAuto: _Callable[[_Pointer[_type.boolean],  # value
                           _Pointer[_type.boolean]],  # succeeded
                          _type.HRESULT]
    TrySetAuto: _Callable[[_type.boolean,  # value
                           _Pointer[_type.boolean]],  # succeeded
                          _type.HRESULT]


class IMediaDeviceControlCapabilities(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.DOUBLE]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.DOUBLE]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    get_Default: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_AutoModeSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IMediaDeviceController(_inspectable.IInspectable):
    GetAvailableMediaStreamProperties: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                                  _Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media_MediaProperties.IMediaEncodingProperties]]],  # value
                                                 _type.HRESULT]
    GetMediaStreamProperties: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                         _Pointer[_Windows_Media_MediaProperties.IMediaEncodingProperties]],  # value
                                        _type.HRESULT]
    SetMediaStreamPropertiesAsync: _Callable[[_enum.Windows.Media.Capture.MediaStreamType,  # mediaStreamType
                                              _Windows_Media_MediaProperties.IMediaEncodingProperties,  # mediaEncodingProperties
                                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                             _type.HRESULT]


class IMediaDeviceStatics(_inspectable.IInspectable):
    GetAudioCaptureSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                       _type.HRESULT]
    GetAudioRenderSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                      _type.HRESULT]
    GetVideoCaptureSelector: _Callable[[_Pointer[_type.HSTRING]],  # selector
                                       _type.HRESULT]
    GetDefaultAudioCaptureId: _Callable[[_enum.Windows.Media.Devices.AudioDeviceRole,  # role
                                         _Pointer[_type.HSTRING]],  # deviceId
                                        _type.HRESULT]
    GetDefaultAudioRenderId: _Callable[[_enum.Windows.Media.Devices.AudioDeviceRole,  # role
                                        _Pointer[_type.HSTRING]],  # deviceId
                                       _type.HRESULT]
    add_DefaultAudioCaptureDeviceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IDefaultAudioDeviceChangedEventArgs],  # handler
                                                     _Pointer[_struct.EventRegistrationToken]],  # cookie
                                                    _type.HRESULT]
    remove_DefaultAudioCaptureDeviceChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                       _type.HRESULT]
    add_DefaultAudioRenderDeviceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IDefaultAudioDeviceChangedEventArgs],  # handler
                                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                                   _type.HRESULT]
    remove_DefaultAudioRenderDeviceChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                      _type.HRESULT]

    _factory = True


class IModuleCommandResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Devices.SendCommandStatus]],  # value
                          _type.HRESULT]
    get_Result: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                          _type.HRESULT]


class IOpticalImageStabilizationControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_SupportedModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.OpticalImageStabilizationMode]]],  # value
                                  _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.OpticalImageStabilizationMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Devices.OpticalImageStabilizationMode],  # value
                        _type.HRESULT]


class IPanelBasedOptimizationControl(_inspectable.IInspectable):
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_Panel: _Callable[[_Pointer[_enum.Windows.Devices.Enumeration.Panel]],  # value
                         _type.HRESULT]
    put_Panel: _Callable[[_enum.Windows.Devices.Enumeration.Panel],  # value
                         _type.HRESULT]


class IPhotoConfirmationControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # pbSupported
                             _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_PixelFormat: _Callable[[_Pointer[_enum.Windows.Media.MediaProperties.MediaPixelFormat]],  # format
                               _type.HRESULT]
    put_PixelFormat: _Callable[[_enum.Windows.Media.MediaProperties.MediaPixelFormat],  # format
                               _type.HRESULT]


class IRedialRequestedEventArgs(_inspectable.IInspectable):
    Handled: _Callable[[],
                       _type.HRESULT]


class IRegionOfInterest(_inspectable.IInspectable):
    get_AutoFocusEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_AutoFocusEnabled: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_AutoWhiteBalanceEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_AutoWhiteBalanceEnabled: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_AutoExposureEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_AutoExposureEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    put_Bounds: _Callable[[_struct.Windows.Foundation.Rect],  # value
                          _type.HRESULT]


class IRegionOfInterest2(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.Media.Devices.RegionOfInterestType]],  # value
                        _type.HRESULT]
    put_Type: _Callable[[_enum.Windows.Media.Devices.RegionOfInterestType],  # value
                        _type.HRESULT]
    get_BoundsNormalized: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_BoundsNormalized: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_Weight: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    put_Weight: _Callable[[_type.UINT32],  # value
                          _type.HRESULT]


class IRegionsOfInterestControl(_inspectable.IInspectable):
    get_MaxRegions: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    SetRegionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IRegionOfInterest],  # regions
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                               _type.HRESULT]
    SetRegionsWithLockAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IRegionOfInterest],  # regions
                                        _type.boolean,  # lockValues
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                       _type.HRESULT]
    ClearRegionsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                                 _type.HRESULT]
    get_AutoFocusSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_AutoWhiteBalanceSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_AutoExposureSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class ISceneModeControl(_inspectable.IInspectable):
    get_SupportedModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.CaptureSceneMode]]],  # value
                                  _type.HRESULT]
    get_Value: _Callable[[_Pointer[_enum.Windows.Media.Devices.CaptureSceneMode]],  # value
                         _type.HRESULT]
    SetValueAsync: _Callable[[_enum.Windows.Media.Devices.CaptureSceneMode,  # sceneMode
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                             _type.HRESULT]


class ITorchControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_PowerSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_PowerPercent: _Callable[[_Pointer[_type.FLOAT]],  # value
                                _type.HRESULT]
    put_PowerPercent: _Callable[[_type.FLOAT],  # value
                                _type.HRESULT]


class IVideoDeviceController(_inspectable.IInspectable):
    get_Brightness: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                              _type.HRESULT]
    get_Contrast: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                            _type.HRESULT]
    get_Hue: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                       _type.HRESULT]
    get_WhiteBalance: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                                _type.HRESULT]
    get_BacklightCompensation: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                                         _type.HRESULT]
    get_Pan: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                       _type.HRESULT]
    get_Tilt: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                        _type.HRESULT]
    get_Zoom: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                        _type.HRESULT]
    get_Roll: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                        _type.HRESULT]
    get_Exposure: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                            _type.HRESULT]
    get_Focus: _Callable[[_Pointer[IMediaDeviceControl]],  # value
                         _type.HRESULT]
    TrySetPowerlineFrequency: _Callable[[_enum.Windows.Media.Capture.PowerlineFrequency,  # value
                                         _Pointer[_type.boolean]],  # succeeded
                                        _type.HRESULT]
    TryGetPowerlineFrequency: _Callable[[_Pointer[_enum.Windows.Media.Capture.PowerlineFrequency],  # value
                                         _Pointer[_type.boolean]],  # succeeded
                                        _type.HRESULT]


class IVideoDeviceControllerGetDevicePropertyResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Devices.VideoDeviceControllerGetDevicePropertyStatus]],  # value
                          _type.HRESULT]
    get_Value: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                         _type.HRESULT]


class IVideoTemporalDenoisingControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_SupportedModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.VideoTemporalDenoisingMode]]],  # value
                                  _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.VideoTemporalDenoisingMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Devices.VideoTemporalDenoisingMode],  # value
                        _type.HRESULT]


class IWhiteBalanceControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Preset: _Callable[[_Pointer[_enum.Windows.Media.Devices.ColorTemperaturePreset]],  # value
                          _type.HRESULT]
    SetPresetAsync: _Callable[[_enum.Windows.Media.Devices.ColorTemperaturePreset,  # preset
                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                              _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    SetValueAsync: _Callable[[_type.UINT32,  # temperature
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncInfo
                             _type.HRESULT]


class IZoomControl(_inspectable.IInspectable):
    get_Supported: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Min: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_Max: _Callable[[_Pointer[_type.FLOAT]],  # value
                       _type.HRESULT]
    get_Step: _Callable[[_Pointer[_type.FLOAT]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.FLOAT],  # value
                         _type.HRESULT]


class IZoomControl2(_inspectable.IInspectable):
    get_SupportedModes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Media.Devices.ZoomTransitionMode]]],  # value
                                  _type.HRESULT]
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.ZoomTransitionMode]],  # value
                        _type.HRESULT]
    Configure: _Callable[[IZoomSettings],  # settings
                         _type.HRESULT]


class IZoomSettings(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.Media.Devices.ZoomTransitionMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.Media.Devices.ZoomTransitionMode],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.FLOAT],  # value
                         _type.HRESULT]
