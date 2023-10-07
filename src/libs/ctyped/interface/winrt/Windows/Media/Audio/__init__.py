from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Core as _Windows_Media_Core
from .. import Effects as _Windows_Media_Effects
from .. import MediaProperties as _Windows_Media_MediaProperties
from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ... import Storage as _Windows_Storage
from ...Devices import Enumeration as _Windows_Devices_Enumeration
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAudioDeviceInputNode(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                          _type.HRESULT]


class IAudioDeviceOutputNode(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                          _type.HRESULT]


class IAudioFileInputNode(_inspectable.IInspectable):
    put_PlaybackSpeedFactor: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_PlaybackSpeedFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    Seek: _Callable[[_struct.Windows.Foundation.TimeSpan],  # position
                    _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_EndTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                           _type.HRESULT]
    put_EndTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]
    get_LoopCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                             _type.HRESULT]
    put_LoopCount: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_SourceFile: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                              _type.HRESULT]
    add_FileCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioFileInputNode, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_FileCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IAudioFileOutputNode(_inspectable.IInspectable):
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]
    get_FileEncodingProfile: _Callable[[_Pointer[_Windows_Media_MediaProperties.IMediaEncodingProfile]],  # value
                                       _type.HRESULT]
    FinalizeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Media.Transcoding.TranscodeFailureReason]]],  # result
                             _type.HRESULT]


class IAudioFrameCompletedEventArgs(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[_Windows_Media.IAudioFrame]],  # value
                         _type.HRESULT]


class IAudioFrameInputNode(_inspectable.IInspectable):
    put_PlaybackSpeedFactor: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_PlaybackSpeedFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    AddFrame: _Callable[[_Windows_Media.IAudioFrame],  # frame
                        _type.HRESULT]
    DiscardQueuedFrames: _Callable[[],
                                   _type.HRESULT]
    get_QueuedSampleCount: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    add_AudioFrameCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioFrameInputNode, IAudioFrameCompletedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_AudioFrameCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_QuantumStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioFrameInputNode, IFrameInputNodeQuantumStartedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_QuantumStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IAudioFrameOutputNode(_inspectable.IInspectable):
    GetFrame: _Callable[[_Pointer[_Windows_Media.IAudioFrame]],  # audioFrame
                        _type.HRESULT]


class IAudioGraph(_inspectable.IInspectable):
    CreateFrameInputNode: _Callable[[_Pointer[IAudioFrameInputNode]],  # frameInputNode
                                    _type.HRESULT]
    CreateFrameInputNodeWithFormat: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                               _Pointer[IAudioFrameInputNode]],  # frameInputNode
                                              _type.HRESULT]
    CreateDeviceInputNodeAsync: _Callable[[_enum.Windows.Media.Capture.MediaCategory,  # category
                                           _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioDeviceInputNodeResult]]],  # result
                                          _type.HRESULT]
    CreateDeviceInputNodeWithFormatAsync: _Callable[[_enum.Windows.Media.Capture.MediaCategory,  # category
                                                     _Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioDeviceInputNodeResult]]],  # result
                                                    _type.HRESULT]
    CreateDeviceInputNodeWithFormatOnDeviceAsync: _Callable[[_enum.Windows.Media.Capture.MediaCategory,  # category
                                                             _Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                                             _Windows_Devices_Enumeration.IDeviceInformation,  # device
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioDeviceInputNodeResult]]],  # result
                                                            _type.HRESULT]
    CreateFrameOutputNode: _Callable[[_Pointer[IAudioFrameOutputNode]],  # frameOutputNode
                                     _type.HRESULT]
    CreateFrameOutputNodeWithFormat: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                                _Pointer[IAudioFrameOutputNode]],  # frameOutputNode
                                               _type.HRESULT]
    CreateDeviceOutputNodeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioDeviceOutputNodeResult]]],  # result
                                           _type.HRESULT]
    CreateFileInputNodeAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                         _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioFileInputNodeResult]]],  # result
                                        _type.HRESULT]
    CreateFileOutputNodeAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                          _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioFileOutputNodeResult]]],  # result
                                         _type.HRESULT]
    CreateFileOutputNodeWithFileProfileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                                         _Windows_Media_MediaProperties.IMediaEncodingProfile,  # fileEncodingProfile
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioFileOutputNodeResult]]],  # result
                                                        _type.HRESULT]
    CreateSubmixNode: _Callable[[_Pointer[IAudioInputNode]],  # submixNode
                                _type.HRESULT]
    CreateSubmixNodeWithFormat: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                           _Pointer[IAudioInputNode]],  # submixNode
                                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    ResetAllNodes: _Callable[[],
                             _type.HRESULT]
    add_QuantumStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioGraph, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_QuantumStarted: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_QuantumProcessed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioGraph, _inspectable.IInspectable],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_QuantumProcessed: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_UnrecoverableErrorOccurred: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioGraph, IAudioGraphUnrecoverableErrorOccurredEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_UnrecoverableErrorOccurred: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    get_CompletedQuantumCount: _Callable[[_Pointer[_type.UINT64]],  # value
                                         _type.HRESULT]
    get_EncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                      _type.HRESULT]
    get_LatencyInSamples: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    get_PrimaryRenderDevice: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                       _type.HRESULT]
    get_RenderDeviceAudioProcessing: _Callable[[_Pointer[_enum.Windows.Media.AudioProcessing]],  # value
                                               _type.HRESULT]
    get_SamplesPerQuantum: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]


class IAudioGraph2(_inspectable.IInspectable):
    CreateFrameInputNodeWithFormatAndEmitter: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                                         IAudioNodeEmitter,  # emitter
                                                         _Pointer[IAudioFrameInputNode]],  # frameInputNode
                                                        _type.HRESULT]
    CreateDeviceInputNodeWithFormatAndEmitterOnDeviceAsync: _Callable[[_enum.Windows.Media.Capture.MediaCategory,  # category
                                                                       _Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                                                       _Windows_Devices_Enumeration.IDeviceInformation,  # device
                                                                       IAudioNodeEmitter,  # emitter
                                                                       _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioDeviceInputNodeResult]]],  # result
                                                                      _type.HRESULT]
    CreateFileInputNodeWithEmitterAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                                    IAudioNodeEmitter,  # emitter
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioFileInputNodeResult]]],  # result
                                                   _type.HRESULT]
    CreateSubmixNodeWithFormatAndEmitter: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties,  # encodingProperties
                                                     IAudioNodeEmitter,  # emitter
                                                     _Pointer[IAudioInputNode]],  # submixNode
                                                    _type.HRESULT]
    CreateBatchUpdater: _Callable[[_Pointer[_Windows_Foundation.IClosable]],  # updater
                                  _type.HRESULT]


class IAudioGraph3(_inspectable.IInspectable):
    CreateMediaSourceAudioInputNodeAsync: _Callable[[_Windows_Media_Core.IMediaSource2,  # mediaSource
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[ICreateMediaSourceAudioInputNodeResult]]],  # operation
                                                    _type.HRESULT]
    CreateMediaSourceAudioInputNodeWithEmitterAsync: _Callable[[_Windows_Media_Core.IMediaSource2,  # mediaSource
                                                                IAudioNodeEmitter,  # emitter
                                                                _Pointer[_Windows_Foundation.IAsyncOperation[ICreateMediaSourceAudioInputNodeResult]]],  # operation
                                                               _type.HRESULT]


class IAudioGraphConnection(_inspectable.IInspectable):
    get_Destination: _Callable[[_Pointer[IAudioNode]],  # value
                               _type.HRESULT]
    put_Gain: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]
    get_Gain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]


class IAudioGraphSettings(_inspectable.IInspectable):
    get_EncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                      _type.HRESULT]
    put_EncodingProperties: _Callable[[_Windows_Media_MediaProperties.IAudioEncodingProperties],  # value
                                      _type.HRESULT]
    get_PrimaryRenderDevice: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                       _type.HRESULT]
    put_PrimaryRenderDevice: _Callable[[_Windows_Devices_Enumeration.IDeviceInformation],  # value
                                       _type.HRESULT]
    get_QuantumSizeSelectionMode: _Callable[[_Pointer[_enum.Windows.Media.Audio.QuantumSizeSelectionMode]],  # value
                                            _type.HRESULT]
    put_QuantumSizeSelectionMode: _Callable[[_enum.Windows.Media.Audio.QuantumSizeSelectionMode],  # value
                                            _type.HRESULT]
    get_DesiredSamplesPerQuantum: _Callable[[_Pointer[_type.INT32]],  # value
                                            _type.HRESULT]
    put_DesiredSamplesPerQuantum: _Callable[[_type.INT32],  # value
                                            _type.HRESULT]
    get_AudioRenderCategory: _Callable[[_Pointer[_enum.Windows.Media.Render.AudioRenderCategory]],  # value
                                       _type.HRESULT]
    put_AudioRenderCategory: _Callable[[_enum.Windows.Media.Render.AudioRenderCategory],  # value
                                       _type.HRESULT]
    get_DesiredRenderDeviceAudioProcessing: _Callable[[_Pointer[_enum.Windows.Media.AudioProcessing]],  # value
                                                      _type.HRESULT]
    put_DesiredRenderDeviceAudioProcessing: _Callable[[_enum.Windows.Media.AudioProcessing],  # value
                                                      _type.HRESULT]


class IAudioGraphSettings2(_inspectable.IInspectable):
    put_MaxPlaybackSpeedFactor: _Callable[[_type.DOUBLE],  # value
                                          _type.HRESULT]
    get_MaxPlaybackSpeedFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]


class IAudioGraphSettingsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.Media.Render.AudioRenderCategory,  # audioRenderCategory
                       _Pointer[IAudioGraphSettings]],  # value
                      _type.HRESULT]


class IAudioGraphStatics(_inspectable.IInspectable, factory=True):
    CreateAsync: _Callable[[IAudioGraphSettings,  # settings
                            _Pointer[_Windows_Foundation.IAsyncOperation[ICreateAudioGraphResult]]],  # result
                           _type.HRESULT]


class IAudioGraphUnrecoverableErrorOccurredEventArgs(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioGraphUnrecoverableError]],  # value
                         _type.HRESULT]


class IAudioInputNode(_inspectable.IInspectable):
    get_OutgoingConnections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAudioGraphConnection]]],  # value
                                       _type.HRESULT]
    AddOutgoingConnection: _Callable[[IAudioNode],  # destination
                                     _type.HRESULT]
    AddOutgoingConnectionWithGain: _Callable[[IAudioNode,  # destination
                                              _type.DOUBLE],  # gain
                                             _type.HRESULT]
    RemoveOutgoingConnection: _Callable[[IAudioNode],  # destination
                                        _type.HRESULT]


class IAudioInputNode2(_inspectable.IInspectable):
    get_Emitter: _Callable[[_Pointer[IAudioNodeEmitter]],  # value
                           _type.HRESULT]


class IAudioNode(_inspectable.IInspectable):
    get_EffectDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Media_Effects.IAudioEffectDefinition]]],  # value
                                     _type.HRESULT]
    put_OutgoingGain: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_OutgoingGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    get_EncodingProperties: _Callable[[_Pointer[_Windows_Media_MediaProperties.IAudioEncodingProperties]],  # value
                                      _type.HRESULT]
    get_ConsumeInput: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_ConsumeInput: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    DisableEffectsByDefinition: _Callable[[_Windows_Media_Effects.IAudioEffectDefinition],  # definition
                                          _type.HRESULT]
    EnableEffectsByDefinition: _Callable[[_Windows_Media_Effects.IAudioEffectDefinition],  # definition
                                         _type.HRESULT]


class IAudioNodeEmitter(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                            _type.HRESULT]
    get_Direction: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                             _type.HRESULT]
    put_Direction: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                             _type.HRESULT]
    get_Shape: _Callable[[_Pointer[IAudioNodeEmitterShape]],  # value
                         _type.HRESULT]
    get_DecayModel: _Callable[[_Pointer[IAudioNodeEmitterDecayModel]],  # value
                              _type.HRESULT]
    get_Gain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    put_Gain: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]
    get_DistanceScale: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]
    put_DistanceScale: _Callable[[_type.DOUBLE],  # value
                                 _type.HRESULT]
    get_DopplerScale: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_DopplerScale: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_DopplerVelocity: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                   _type.HRESULT]
    put_DopplerVelocity: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                   _type.HRESULT]
    get_IsDopplerDisabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IAudioNodeEmitter2(_inspectable.IInspectable):
    get_SpatialAudioModel: _Callable[[_Pointer[_enum.Windows.Media.Audio.SpatialAudioModel]],  # value
                                     _type.HRESULT]
    put_SpatialAudioModel: _Callable[[_enum.Windows.Media.Audio.SpatialAudioModel],  # value
                                     _type.HRESULT]


class IAudioNodeEmitterConeProperties(_inspectable.IInspectable):
    get_InnerAngle: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    get_OuterAngle: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    get_OuterAngleGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]


class IAudioNodeEmitterDecayModel(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioNodeEmitterDecayKind]],  # value
                        _type.HRESULT]
    get_MinGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_MaxGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_NaturalProperties: _Callable[[_Pointer[IAudioNodeEmitterNaturalDecayModelProperties]],  # value
                                     _type.HRESULT]


class IAudioNodeEmitterDecayModelStatics(_inspectable.IInspectable, factory=True):
    CreateNatural: _Callable[[_type.DOUBLE,  # minGain
                              _type.DOUBLE,  # maxGain
                              _type.DOUBLE,  # unityGainDistance
                              _type.DOUBLE,  # cutoffDistance
                              _Pointer[IAudioNodeEmitterDecayModel]],  # decayModel
                             _type.HRESULT]
    CreateCustom: _Callable[[_type.DOUBLE,  # minGain
                             _type.DOUBLE,  # maxGain
                             _Pointer[IAudioNodeEmitterDecayModel]],  # decayModel
                            _type.HRESULT]


class IAudioNodeEmitterFactory(_inspectable.IInspectable, factory=True):
    CreateAudioNodeEmitter: _Callable[[IAudioNodeEmitterShape,  # shape
                                       IAudioNodeEmitterDecayModel,  # decayModel
                                       _enum.Windows.Media.Audio.AudioNodeEmitterSettings,  # settings
                                       _Pointer[IAudioNodeEmitter]],  # emitter
                                      _type.HRESULT]


class IAudioNodeEmitterNaturalDecayModelProperties(_inspectable.IInspectable):
    get_UnityGainDistance: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                     _type.HRESULT]
    get_CutoffDistance: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]


class IAudioNodeEmitterShape(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioNodeEmitterShapeKind]],  # value
                        _type.HRESULT]
    get_ConeProperties: _Callable[[_Pointer[IAudioNodeEmitterConeProperties]],  # value
                                  _type.HRESULT]


class IAudioNodeEmitterShapeStatics(_inspectable.IInspectable, factory=True):
    CreateCone: _Callable[[_type.DOUBLE,  # innerAngle
                           _type.DOUBLE,  # outerAngle
                           _type.DOUBLE,  # outerAngleGain
                           _Pointer[IAudioNodeEmitterShape]],  # shape
                          _type.HRESULT]
    CreateOmnidirectional: _Callable[[_Pointer[IAudioNodeEmitterShape]],  # shape
                                     _type.HRESULT]


class IAudioNodeListener(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                            _type.HRESULT]
    get_Orientation: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Quaternion]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_struct.Windows.Foundation.Numerics.Quaternion],  # value
                               _type.HRESULT]
    get_SpeedOfSound: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_SpeedOfSound: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_DopplerVelocity: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                                   _type.HRESULT]
    put_DopplerVelocity: _Callable[[_struct.Windows.Foundation.Numerics.Vector3],  # value
                                   _type.HRESULT]


class IAudioNodeWithListener(_inspectable.IInspectable):
    put_Listener: _Callable[[IAudioNodeListener],  # value
                            _type.HRESULT]
    get_Listener: _Callable[[_Pointer[IAudioNodeListener]],  # value
                            _type.HRESULT]


class IAudioPlaybackConnection(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioPlaybackConnectionState]],  # value
                         _type.HRESULT]
    Open: _Callable[[_Pointer[IAudioPlaybackConnectionOpenResult]],  # result
                    _type.HRESULT]
    OpenAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAudioPlaybackConnectionOpenResult]]],  # operation
                         _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioPlaybackConnection, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IAudioPlaybackConnectionOpenResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioPlaybackConnectionOpenResultStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IAudioPlaybackConnectionStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    TryCreateFromId: _Callable[[_type.HSTRING,  # id
                                _Pointer[IAudioPlaybackConnection]],  # result
                               _type.HRESULT]


class IAudioStateMonitor(_inspectable.IInspectable):
    add_SoundLevelChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAudioStateMonitor, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SoundLevelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    get_SoundLevel: _Callable[[_Pointer[_enum.Windows.Media.SoundLevel]],  # value
                              _type.HRESULT]


class IAudioStateMonitorStatics(_inspectable.IInspectable, factory=True):
    CreateForRenderMonitoring: _Callable[[_Pointer[IAudioStateMonitor]],  # result
                                         _type.HRESULT]
    CreateForRenderMonitoringWithCategory: _Callable[[_enum.Windows.Media.Render.AudioRenderCategory,  # category
                                                      _Pointer[IAudioStateMonitor]],  # result
                                                     _type.HRESULT]
    CreateForRenderMonitoringWithCategoryAndDeviceRole: _Callable[[_enum.Windows.Media.Render.AudioRenderCategory,  # category
                                                                   _enum.Windows.Media.Devices.AudioDeviceRole,  # role
                                                                   _Pointer[IAudioStateMonitor]],  # result
                                                                  _type.HRESULT]
    CreateForRenderMonitoringWithCategoryAndDeviceId: _Callable[[_enum.Windows.Media.Render.AudioRenderCategory,  # category
                                                                 _type.HSTRING,  # deviceId
                                                                 _Pointer[IAudioStateMonitor]],  # result
                                                                _type.HRESULT]
    CreateForCaptureMonitoring: _Callable[[_Pointer[IAudioStateMonitor]],  # result
                                          _type.HRESULT]
    CreateForCaptureMonitoringWithCategory: _Callable[[_enum.Windows.Media.Capture.MediaCategory,  # category
                                                       _Pointer[IAudioStateMonitor]],  # result
                                                      _type.HRESULT]
    CreateForCaptureMonitoringWithCategoryAndDeviceRole: _Callable[[_enum.Windows.Media.Capture.MediaCategory,  # category
                                                                    _enum.Windows.Media.Devices.AudioDeviceRole,  # role
                                                                    _Pointer[IAudioStateMonitor]],  # result
                                                                   _type.HRESULT]
    CreateForCaptureMonitoringWithCategoryAndDeviceId: _Callable[[_enum.Windows.Media.Capture.MediaCategory,  # category
                                                                  _type.HSTRING,  # deviceId
                                                                  _Pointer[IAudioStateMonitor]],  # result
                                                                 _type.HRESULT]


class ICreateAudioDeviceInputNodeResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioDeviceNodeCreationStatus]],  # value
                          _type.HRESULT]
    get_DeviceInputNode: _Callable[[_Pointer[IAudioDeviceInputNode]],  # value
                                   _type.HRESULT]


class ICreateAudioDeviceInputNodeResult2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class ICreateAudioDeviceOutputNodeResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioDeviceNodeCreationStatus]],  # value
                          _type.HRESULT]
    get_DeviceOutputNode: _Callable[[_Pointer[IAudioDeviceOutputNode]],  # value
                                    _type.HRESULT]


class ICreateAudioDeviceOutputNodeResult2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class ICreateAudioFileInputNodeResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioFileNodeCreationStatus]],  # value
                          _type.HRESULT]
    get_FileInputNode: _Callable[[_Pointer[IAudioFileInputNode]],  # value
                                 _type.HRESULT]


class ICreateAudioFileInputNodeResult2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class ICreateAudioFileOutputNodeResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioFileNodeCreationStatus]],  # value
                          _type.HRESULT]
    get_FileOutputNode: _Callable[[_Pointer[IAudioFileOutputNode]],  # value
                                  _type.HRESULT]


class ICreateAudioFileOutputNodeResult2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class ICreateAudioGraphResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.AudioGraphCreationStatus]],  # value
                          _type.HRESULT]
    get_Graph: _Callable[[_Pointer[IAudioGraph]],  # value
                         _type.HRESULT]


class ICreateAudioGraphResult2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class ICreateMediaSourceAudioInputNodeResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.MediaSourceAudioInputNodeCreationStatus]],  # value
                          _type.HRESULT]
    get_Node: _Callable[[_Pointer[IMediaSourceAudioInputNode]],  # value
                        _type.HRESULT]


class ICreateMediaSourceAudioInputNodeResult2(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IEchoEffectDefinition(_inspectable.IInspectable):
    put_WetDryMix: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_WetDryMix: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_Feedback: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_Feedback: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_Delay: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]
    get_Delay: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]


class IEchoEffectDefinitionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IAudioGraph,  # audioGraph
                       _Pointer[IEchoEffectDefinition]],  # value
                      _type.HRESULT]


class IEqualizerBand(_inspectable.IInspectable):
    get_Bandwidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_Bandwidth: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_FrequencyCenter: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_FrequencyCenter: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_Gain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                        _type.HRESULT]
    put_Gain: _Callable[[_type.DOUBLE],  # value
                        _type.HRESULT]


class IEqualizerEffectDefinition(_inspectable.IInspectable):
    get_Bands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IEqualizerBand]]],  # value
                         _type.HRESULT]


class IEqualizerEffectDefinitionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IAudioGraph,  # audioGraph
                       _Pointer[IEqualizerEffectDefinition]],  # value
                      _type.HRESULT]


class IFrameInputNodeQuantumStartedEventArgs(_inspectable.IInspectable):
    get_RequiredSamples: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]


class ILimiterEffectDefinition(_inspectable.IInspectable):
    put_Release: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_Release: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_Loudness: _Callable[[_type.UINT32],  # value
                            _type.HRESULT]
    get_Loudness: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class ILimiterEffectDefinitionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IAudioGraph,  # audioGraph
                       _Pointer[ILimiterEffectDefinition]],  # value
                      _type.HRESULT]


class IMediaSourceAudioInputNode(_inspectable.IInspectable):
    put_PlaybackSpeedFactor: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_PlaybackSpeedFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    Seek: _Callable[[_struct.Windows.Foundation.TimeSpan],  # position
                    _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    get_EndTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                           _type.HRESULT]
    put_EndTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                           _type.HRESULT]
    get_LoopCount: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                             _type.HRESULT]
    put_LoopCount: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_MediaSource: _Callable[[_Pointer[_Windows_Media_Core.IMediaSource2]],  # value
                               _type.HRESULT]
    add_MediaSourceCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IMediaSourceAudioInputNode, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_MediaSourceCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IReverbEffectDefinition(_inspectable.IInspectable):
    put_WetDryMix: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_WetDryMix: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_ReflectionsDelay: _Callable[[_type.UINT32],  # value
                                    _type.HRESULT]
    get_ReflectionsDelay: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    put_ReverbDelay: _Callable[[_type.BYTE],  # value
                               _type.HRESULT]
    get_ReverbDelay: _Callable[[_Pointer[_type.BYTE]],  # value
                               _type.HRESULT]
    put_RearDelay: _Callable[[_type.BYTE],  # value
                             _type.HRESULT]
    get_RearDelay: _Callable[[_Pointer[_type.BYTE]],  # value
                             _type.HRESULT]
    put_PositionLeft: _Callable[[_type.BYTE],  # value
                                _type.HRESULT]
    get_PositionLeft: _Callable[[_Pointer[_type.BYTE]],  # value
                                _type.HRESULT]
    put_PositionRight: _Callable[[_type.BYTE],  # value
                                 _type.HRESULT]
    get_PositionRight: _Callable[[_Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    put_PositionMatrixLeft: _Callable[[_type.BYTE],  # value
                                      _type.HRESULT]
    get_PositionMatrixLeft: _Callable[[_Pointer[_type.BYTE]],  # value
                                      _type.HRESULT]
    put_PositionMatrixRight: _Callable[[_type.BYTE],  # value
                                       _type.HRESULT]
    get_PositionMatrixRight: _Callable[[_Pointer[_type.BYTE]],  # value
                                       _type.HRESULT]
    put_EarlyDiffusion: _Callable[[_type.BYTE],  # value
                                  _type.HRESULT]
    get_EarlyDiffusion: _Callable[[_Pointer[_type.BYTE]],  # value
                                  _type.HRESULT]
    put_LateDiffusion: _Callable[[_type.BYTE],  # value
                                 _type.HRESULT]
    get_LateDiffusion: _Callable[[_Pointer[_type.BYTE]],  # value
                                 _type.HRESULT]
    put_LowEQGain: _Callable[[_type.BYTE],  # value
                             _type.HRESULT]
    get_LowEQGain: _Callable[[_Pointer[_type.BYTE]],  # value
                             _type.HRESULT]
    put_LowEQCutoff: _Callable[[_type.BYTE],  # value
                               _type.HRESULT]
    get_LowEQCutoff: _Callable[[_Pointer[_type.BYTE]],  # value
                               _type.HRESULT]
    put_HighEQGain: _Callable[[_type.BYTE],  # value
                              _type.HRESULT]
    get_HighEQGain: _Callable[[_Pointer[_type.BYTE]],  # value
                              _type.HRESULT]
    put_HighEQCutoff: _Callable[[_type.BYTE],  # value
                                _type.HRESULT]
    get_HighEQCutoff: _Callable[[_Pointer[_type.BYTE]],  # value
                                _type.HRESULT]
    put_RoomFilterFreq: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_RoomFilterFreq: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_RoomFilterMain: _Callable[[_type.DOUBLE],  # value
                                  _type.HRESULT]
    get_RoomFilterMain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                  _type.HRESULT]
    put_RoomFilterHF: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_RoomFilterHF: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_ReflectionsGain: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_ReflectionsGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_ReverbGain: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_ReverbGain: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_DecayTime: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_DecayTime: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_Density: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Density: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_RoomSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_RoomSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_DisableLateField: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_DisableLateField: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]


class IReverbEffectDefinitionFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[IAudioGraph,  # audioGraph
                       _Pointer[IReverbEffectDefinition]],  # value
                      _type.HRESULT]


class ISetDefaultSpatialAudioFormatResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.Audio.SetDefaultSpatialAudioFormatStatus]],  # value
                          _type.HRESULT]


class ISpatialAudioDeviceConfiguration(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsSpatialAudioSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    IsSpatialAudioFormatSupported: _Callable[[_type.HSTRING,  # subtype
                                              _Pointer[_type.boolean]],  # result
                                             _type.HRESULT]
    get_ActiveSpatialAudioFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    get_DefaultSpatialAudioFormat: _Callable[[_Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]
    SetDefaultSpatialAudioFormatAsync: _Callable[[_type.HSTRING,  # subtype
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[ISetDefaultSpatialAudioFormatResult]]],  # operation
                                                 _type.HRESULT]
    add_ConfigurationChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpatialAudioDeviceConfiguration, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ConfigurationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class ISpatialAudioDeviceConfigurationStatics(_inspectable.IInspectable, factory=True):
    GetForDeviceId: _Callable[[_type.HSTRING,  # deviceId
                               _Pointer[ISpatialAudioDeviceConfiguration]],  # result
                              _type.HRESULT]


class ISpatialAudioFormatConfiguration(_inspectable.IInspectable):
    ReportLicenseChangedAsync: _Callable[[_type.HSTRING,  # subtype
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                         _type.HRESULT]
    ReportConfigurationChangedAsync: _Callable[[_type.HSTRING,  # subtype
                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                               _type.HRESULT]
    get_MixedRealityExclusiveModePolicy: _Callable[[_Pointer[_enum.Windows.Media.Audio.MixedRealitySpatialAudioFormatPolicy]],  # value
                                                   _type.HRESULT]
    put_MixedRealityExclusiveModePolicy: _Callable[[_enum.Windows.Media.Audio.MixedRealitySpatialAudioFormatPolicy],  # value
                                                   _type.HRESULT]


class ISpatialAudioFormatConfigurationStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[ISpatialAudioFormatConfiguration]],  # result
                          _type.HRESULT]


class ISpatialAudioFormatSubtypeStatics(_inspectable.IInspectable, factory=True):
    get_WindowsSonic: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_DolbyAtmosForHeadphones: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    get_DolbyAtmosForHomeTheater: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    get_DolbyAtmosForSpeakers: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_DTSHeadphoneX: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_DTSXUltra: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class ISpatialAudioFormatSubtypeStatics2(_inspectable.IInspectable, factory=True):
    get_DTSXForHomeTheater: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
