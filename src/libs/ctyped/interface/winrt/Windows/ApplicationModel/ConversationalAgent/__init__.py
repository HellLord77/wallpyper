from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Media import Audio as _Windows_Media_Audio
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IActivationSignalDetectionConfiguration(_inspectable.IInspectable):
    get_SignalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    SetEnabled: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    SetEnabledAsync: _Callable[[_type.boolean,  # value
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
    get_AvailabilityInfo: _Callable[[_Pointer[IDetectionConfigurationAvailabilityInfo]],  # value
                                    _type.HRESULT]
    add_AvailabilityChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IActivationSignalDetectionConfiguration, IDetectionConfigurationAvailabilityChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_AvailabilityChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    SetModelData: _Callable[[_type.HSTRING,  # dataType
                             _Windows_Storage_Streams.IInputStream],  # data
                            _type.HRESULT]
    SetModelDataAsync: _Callable[[_type.HSTRING,  # dataType
                                  _Windows_Storage_Streams.IInputStream,  # data
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                 _type.HRESULT]
    GetModelDataType: _Callable[[_Pointer[_type.HSTRING]],  # result
                                _type.HRESULT]
    GetModelDataTypeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                     _type.HRESULT]
    GetModelData: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # result
                            _type.HRESULT]
    GetModelDataAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IInputStream]]],  # operation
                                 _type.HRESULT]
    ClearModelData: _Callable[[],
                              _type.HRESULT]
    ClearModelDataAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    get_TrainingStepsCompleted: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_TrainingStepsRemaining: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_TrainingDataFormat: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat]],  # value
                                      _type.HRESULT]
    ApplyTrainingData: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat,  # trainingDataFormat
                                  _Windows_Storage_Streams.IInputStream,  # trainingData
                                  _Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus]],  # result
                                 _type.HRESULT]
    ApplyTrainingDataAsync: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat,  # trainingDataFormat
                                       _Windows_Storage_Streams.IInputStream,  # trainingData
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationTrainingStatus]]],  # operation
                                      _type.HRESULT]
    ClearTrainingData: _Callable[[],
                                 _type.HRESULT]
    ClearTrainingDataAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                      _type.HRESULT]


class IActivationSignalDetectionConfiguration2(_inspectable.IInspectable):
    SetModelDataWithResult: _Callable[[_type.HSTRING,  # dataType
                                       _Windows_Storage_Streams.IInputStream,  # data
                                       _Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult]],  # result
                                      _type.HRESULT]
    SetModelDataWithResultAsync: _Callable[[_type.HSTRING,  # dataType
                                            _Windows_Storage_Streams.IInputStream,  # data
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationSetModelDataResult]]],  # operation
                                           _type.HRESULT]
    SetEnabledWithResultAsync: _Callable[[_type.boolean,  # value
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult]]],  # operation
                                         _type.HRESULT]
    SetEnabledWithResult: _Callable[[_type.boolean,  # value
                                     _Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationStateChangeResult]],  # result
                                    _type.HRESULT]
    get_TrainingStepCompletionMaxAllowedTime: _Callable[[_Pointer[_type.UINT32]],  # value
                                                        _type.HRESULT]


class IActivationSignalDetectionConfigurationCreationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationCreationStatus]],  # value
                          _type.HRESULT]
    get_Configuration: _Callable[[_Pointer[IActivationSignalDetectionConfiguration]],  # value
                                 _type.HRESULT]


class IActivationSignalDetector(_inspectable.IInspectable):
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind]],  # value
                        _type.HRESULT]
    get_CanCreateConfigurations: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_SupportedModelDataTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                           _type.HRESULT]
    get_SupportedTrainingDataFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionTrainingDataFormat]]],  # value
                                                _type.HRESULT]
    get_SupportedPowerStates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorPowerState]]],  # value
                                        _type.HRESULT]
    GetSupportedModelIdsForSignalId: _Callable[[_type.HSTRING,  # signalId
                                                _Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # result
                                               _type.HRESULT]
    GetSupportedModelIdsForSignalIdAsync: _Callable[[_type.HSTRING,  # signalId
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # operation
                                                    _type.HRESULT]
    CreateConfiguration: _Callable[[_type.HSTRING,  # signalId
                                    _type.HSTRING,  # modelId
                                    _type.HSTRING],  # displayName
                                   _type.HRESULT]
    CreateConfigurationAsync: _Callable[[_type.HSTRING,  # signalId
                                         _type.HSTRING,  # modelId
                                         _type.HSTRING,  # displayName
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                        _type.HRESULT]
    GetConfigurations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IActivationSignalDetectionConfiguration]]],  # result
                                 _type.HRESULT]
    GetConfigurationsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IActivationSignalDetectionConfiguration]]]],  # operation
                                      _type.HRESULT]
    GetConfiguration: _Callable[[_type.HSTRING,  # signalId
                                 _type.HSTRING,  # modelId
                                 _Pointer[IActivationSignalDetectionConfiguration]],  # result
                                _type.HRESULT]
    GetConfigurationAsync: _Callable[[_type.HSTRING,  # signalId
                                      _type.HSTRING,  # modelId
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IActivationSignalDetectionConfiguration]]],  # operation
                                     _type.HRESULT]
    RemoveConfiguration: _Callable[[_type.HSTRING,  # signalId
                                    _type.HSTRING],  # modelId
                                   _type.HRESULT]
    RemoveConfigurationAsync: _Callable[[_type.HSTRING,  # signalId
                                         _type.HSTRING,  # modelId
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                        _type.HRESULT]


class IActivationSignalDetector2(_inspectable.IInspectable):
    GetAvailableModelIdsForSignalIdAsync: _Callable[[_type.HSTRING,  # signalId
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[_type.HSTRING]]]],  # operation
                                                    _type.HRESULT]
    GetAvailableModelIdsForSignalId: _Callable[[_type.HSTRING,  # signalId
                                                _Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # result
                                               _type.HRESULT]
    CreateConfigurationWithResultAsync: _Callable[[_type.HSTRING,  # signalId
                                                   _type.HSTRING,  # modelId
                                                   _type.HSTRING,  # displayName
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IActivationSignalDetectionConfigurationCreationResult]]],  # operation
                                                  _type.HRESULT]
    CreateConfigurationWithResult: _Callable[[_type.HSTRING,  # signalId
                                              _type.HSTRING,  # modelId
                                              _type.HSTRING,  # displayName
                                              _Pointer[IActivationSignalDetectionConfigurationCreationResult]],  # result
                                             _type.HRESULT]
    RemoveConfigurationWithResultAsync: _Callable[[_type.HSTRING,  # signalId
                                                   _type.HSTRING,  # modelId
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult]]],  # operation
                                                  _type.HRESULT]
    RemoveConfigurationWithResult: _Callable[[_type.HSTRING,  # signalId
                                              _type.HSTRING,  # modelId
                                              _Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectionConfigurationRemovalResult]],  # result
                                             _type.HRESULT]
    get_DetectorId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IConversationalAgentDetectorManager(_inspectable.IInspectable):
    GetAllActivationSignalDetectors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IActivationSignalDetector]]],  # result
                                               _type.HRESULT]
    GetAllActivationSignalDetectorsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IActivationSignalDetector]]]],  # operation
                                                    _type.HRESULT]
    GetActivationSignalDetectors: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind,  # kind
                                             _Pointer[_Windows_Foundation_Collections.IVectorView[IActivationSignalDetector]]],  # result
                                            _type.HRESULT]
    GetActivationSignalDetectorsAsync: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind,  # kind
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IActivationSignalDetector]]]],  # operation
                                                 _type.HRESULT]


class IConversationalAgentDetectorManager2(_inspectable.IInspectable):
    GetActivationSignalDetectorFromId: _Callable[[_type.HSTRING,  # detectorId
                                                  _Pointer[IActivationSignalDetector]],  # result
                                                 _type.HRESULT]
    GetActivationSignalDetectorFromIdAsync: _Callable[[_type.HSTRING,  # detectorId
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IActivationSignalDetector]]],  # operation
                                                      _type.HRESULT]


class IConversationalAgentDetectorManagerStatics(_inspectable.IInspectable):
    get_Default: _Callable[[_Pointer[IConversationalAgentDetectorManager]],  # value
                           _type.HRESULT]

    _factory = True


class IConversationalAgentSession(_inspectable.IInspectable):
    add_SessionInterrupted: _Callable[[_Windows_Foundation.ITypedEventHandler[IConversationalAgentSession, IConversationalAgentSessionInterruptedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_SessionInterrupted: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_SignalDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[IConversationalAgentSession, IConversationalAgentSignalDetectedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_SignalDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_SystemStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IConversationalAgentSession, IConversationalAgentSystemStateChangedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_SystemStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    get_AgentState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState]],  # value
                              _type.HRESULT]
    get_Signal: _Callable[[_Pointer[IConversationalAgentSignal]],  # value
                          _type.HRESULT]
    get_IsIndicatorLightAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_IsScreenAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsUserAuthenticated: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_IsVoiceActivationAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    get_IsInterruptible: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsInterrupted: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    RequestInterruptibleAsync: _Callable[[_type.boolean,  # interruptible
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]]],  # operation
                                         _type.HRESULT]
    RequestInterruptible: _Callable[[_type.boolean,  # interruptible
                                     _Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]],  # result
                                    _type.HRESULT]
    RequestAgentStateChangeAsync: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState,  # state
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]]],  # operation
                                            _type.HRESULT]
    RequestAgentStateChange: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentState,  # state
                                        _Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]],  # result
                                       _type.HRESULT]
    RequestForegroundActivationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]]],  # operation
                                                _type.HRESULT]
    RequestForegroundActivation: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSessionUpdateResponse]],  # result
                                           _type.HRESULT]
    GetAudioClientAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_inspectable.IInspectable]]],  # operation
                                   _type.HRESULT]
    GetAudioClient: _Callable[[_Pointer[_inspectable.IInspectable]],  # result
                              _type.HRESULT]
    CreateAudioDeviceInputNodeAsync: _Callable[[_Windows_Media_Audio.IAudioGraph,  # graph
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Media_Audio.IAudioDeviceInputNode]]],  # operation
                                               _type.HRESULT]
    CreateAudioDeviceInputNode: _Callable[[_Windows_Media_Audio.IAudioGraph,  # graph
                                           _Pointer[_Windows_Media_Audio.IAudioDeviceInputNode]],  # result
                                          _type.HRESULT]
    GetAudioCaptureDeviceIdAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                            _type.HRESULT]
    GetAudioCaptureDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # result
                                       _type.HRESULT]
    GetAudioRenderDeviceIdAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                           _type.HRESULT]
    GetAudioRenderDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]
    GetSignalModelIdAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                     _type.HRESULT]
    GetSignalModelId: _Callable[[_Pointer[_type.UINT32]],  # result
                                _type.HRESULT]
    SetSignalModelIdAsync: _Callable[[_type.UINT32,  # signalModelId
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    SetSignalModelId: _Callable[[_type.UINT32,  # signalModelId
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    GetSupportedSignalModelIdsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]]],  # operation
                                               _type.HRESULT]
    GetSupportedSignalModelIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # result
                                          _type.HRESULT]


class IConversationalAgentSession2(_inspectable.IInspectable):
    RequestActivationAsync: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind,  # activationKind
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult]]],  # operation
                                      _type.HRESULT]
    RequestActivation: _Callable[[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationKind,  # activationKind
                                  _Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentActivationResult]],  # result
                                 _type.HRESULT]
    SetSupportLockScreenActivationAsync: _Callable[[_type.boolean,  # lockScreenActivationSupported
                                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                   _type.HRESULT]
    SetSupportLockScreenActivation: _Callable[[_type.boolean],  # lockScreenActivationSupported
                                              _type.HRESULT]
    GetMissingPrerequisites: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]]],  # result
                                       _type.HRESULT]
    GetMissingPrerequisitesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentVoiceActivationPrerequisiteKind]]]],  # operation
                                            _type.HRESULT]


class IConversationalAgentSessionInterruptedEventArgs(_inspectable.IInspectable):
    pass


class IConversationalAgentSessionStatics(_inspectable.IInspectable):
    GetCurrentSessionAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IConversationalAgentSession]]],  # operation
                                      _type.HRESULT]
    GetCurrentSessionSync: _Callable[[_Pointer[IConversationalAgentSession]],  # result
                                     _type.HRESULT]

    _factory = True


class IConversationalAgentSignal(_inspectable.IInspectable):
    get_IsSignalVerificationRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_IsSignalVerificationRequired: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    get_SignalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_SignalId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_SignalName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_SignalName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_SignalContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                 _type.HRESULT]
    put_SignalContext: _Callable[[_inspectable.IInspectable],  # value
                                 _type.HRESULT]
    get_SignalStart: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    put_SignalStart: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                               _type.HRESULT]
    get_SignalEnd: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                             _type.HRESULT]
    put_SignalEnd: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                             _type.HRESULT]


class IConversationalAgentSignal2(_inspectable.IInspectable):
    get_DetectorId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_DetectorKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ActivationSignalDetectorKind]],  # value
                                _type.HRESULT]


class IConversationalAgentSignalDetectedEventArgs(_inspectable.IInspectable):
    pass


class IConversationalAgentSystemStateChangedEventArgs(_inspectable.IInspectable):
    get_SystemStateChangeType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.ConversationalAgentSystemStateChangeType]],  # value
                                         _type.HRESULT]


class IDetectionConfigurationAvailabilityChangedEventArgs(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ConversationalAgent.DetectionConfigurationAvailabilityChangeKind]],  # value
                        _type.HRESULT]


class IDetectionConfigurationAvailabilityInfo(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_HasSystemResourceAccess: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_HasPermission: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_HasLockScreenPermission: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class IDetectionConfigurationAvailabilityInfo2(_inspectable.IInspectable):
    get_UnavailableSystemResources: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.ApplicationModel.ConversationalAgent.SignalDetectorResourceKind]]],  # value
                                              _type.HRESULT]
