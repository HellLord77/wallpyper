from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Activation as _Windows_ApplicationModel_Activation
from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Devices import Bluetooth as _Windows_Devices_Bluetooth
from ...Devices import Sensors as _Windows_Devices_Sensors
from ...Devices import Sms as _Windows_Devices_Sms
from ...Devices.Bluetooth import Advertisement as _Windows_Devices_Bluetooth_Advertisement
from ...Devices.Bluetooth import Background as _Windows_Devices_Bluetooth_Background
from ...Devices.Bluetooth import GenericAttributeProfile as _Windows_Devices_Bluetooth_GenericAttributeProfile
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Provider as _Windows_Storage_Provider
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IBackgroundTaskCanceledEventHandler:
    Invoke: _Callable[[IBackgroundTaskInstance,  # sender
                       _enum.Windows.ApplicationModel.Background.BackgroundTaskCancellationReason],  # reason
                      _type.HRESULT]


class IBackgroundTaskCanceledEventHandler(_IBackgroundTaskCanceledEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IBackgroundTaskCanceledEventHandler_impl(_IBackgroundTaskCanceledEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IBackgroundTaskCompletedEventHandler:
    Invoke: _Callable[[IBackgroundTaskRegistration,  # sender
                       IBackgroundTaskCompletedEventArgs],  # args
                      _type.HRESULT]


class IBackgroundTaskCompletedEventHandler(_IBackgroundTaskCompletedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IBackgroundTaskCompletedEventHandler_impl(_IBackgroundTaskCompletedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IBackgroundTaskProgressEventHandler:
    Invoke: _Callable[[IBackgroundTaskRegistration,  # sender
                       IBackgroundTaskProgressEventArgs],  # args
                      _type.HRESULT]


class IBackgroundTaskProgressEventHandler(_IBackgroundTaskProgressEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IBackgroundTaskProgressEventHandler_impl(_IBackgroundTaskProgressEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IActivitySensorTrigger(_inspectable.IInspectable):
    get_SubscribedActivities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Devices.Sensors.ActivityType]]],  # value
                                        _type.HRESULT]
    get_ReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_SupportedActivities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Devices.Sensors.ActivityType]]],  # value
                                       _type.HRESULT]
    get_MinimumReportInterval: _Callable[[_Pointer[_type.UINT32]],  # value
                                         _type.HRESULT]


class IActivitySensorTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # reportIntervalInMilliseconds
                       _Pointer[IActivitySensorTrigger]],  # activityTrigger
                      _type.HRESULT]

    _factory = True


class IAlarmApplicationManagerStatics(_inspectable.IInspectable):
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.AlarmAccessStatus]]],  # operation
                                  _type.HRESULT]
    GetAccessStatus: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.AlarmAccessStatus]],  # status
                               _type.HRESULT]

    _factory = True


class IAppBroadcastTrigger(_inspectable.IInspectable):
    put_ProviderInfo: _Callable[[IAppBroadcastTriggerProviderInfo],  # value
                                _type.HRESULT]
    get_ProviderInfo: _Callable[[_Pointer[IAppBroadcastTriggerProviderInfo]],  # value
                                _type.HRESULT]


class IAppBroadcastTriggerFactory(_inspectable.IInspectable):
    CreateAppBroadcastTrigger: _Callable[[_type.HSTRING,  # providerKey
                                          _Pointer[IAppBroadcastTrigger]],  # broadcastTrigger
                                         _type.HRESULT]

    _factory = True


class IAppBroadcastTriggerProviderInfo(_inspectable.IInspectable):
    put_DisplayNameResource: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_DisplayNameResource: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_LogoResource: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_LogoResource: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_VideoKeyFrameInterval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                         _type.HRESULT]
    get_VideoKeyFrameInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                         _type.HRESULT]
    put_MaxVideoBitrate: _Callable[[_type.UINT32],  # value
                                   _type.HRESULT]
    get_MaxVideoBitrate: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    put_MaxVideoWidth: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]
    get_MaxVideoWidth: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    put_MaxVideoHeight: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]
    get_MaxVideoHeight: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]


class IApplicationTrigger(_inspectable.IInspectable):
    RequestAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.ApplicationTriggerResult]]],  # result
                            _type.HRESULT]
    RequestAsyncWithArguments: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # arguments
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.ApplicationTriggerResult]]],  # result
                                         _type.HRESULT]


class IApplicationTriggerDetails(_inspectable.IInspectable):
    get_Arguments: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                             _type.HRESULT]


class IAppointmentStoreNotificationTrigger(_inspectable.IInspectable):
    pass


class IBackgroundCondition(_inspectable.IInspectable):
    pass


class IBackgroundExecutionManagerStatics(_inspectable.IInspectable):
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.BackgroundAccessStatus]]],  # operation
                                  _type.HRESULT]
    RequestAccessForApplicationAsync: _Callable[[_type.HSTRING,  # applicationId
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.BackgroundAccessStatus]]],  # operation
                                                _type.HRESULT]
    RemoveAccess: _Callable[[],
                            _type.HRESULT]
    RemoveAccessForApplication: _Callable[[_type.HSTRING],  # applicationId
                                          _type.HRESULT]
    GetAccessStatus: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.BackgroundAccessStatus]],  # status
                               _type.HRESULT]
    GetAccessStatusForApplication: _Callable[[_type.HSTRING,  # applicationId
                                              _Pointer[_enum.Windows.ApplicationModel.Background.BackgroundAccessStatus]],  # status
                                             _type.HRESULT]

    _factory = True


class IBackgroundExecutionManagerStatics2(_inspectable.IInspectable):
    RequestAccessKindAsync: _Callable[[_enum.Windows.ApplicationModel.Background.BackgroundAccessRequestKind,  # requestedAccess
                                       _type.HSTRING,  # reason
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]

    _factory = True


class IBackgroundExecutionManagerStatics3(_inspectable.IInspectable):
    RequestAccessKindForModernStandbyAsync: _Callable[[_enum.Windows.ApplicationModel.Background.BackgroundAccessRequestKind,  # requestedAccess
                                                       _type.HSTRING,  # reason
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                      _type.HRESULT]
    GetAccessStatusForModernStandby: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.BackgroundAccessStatus]],  # result
                                               _type.HRESULT]
    GetAccessStatusForModernStandbyForApplication: _Callable[[_type.HSTRING,  # applicationId
                                                              _Pointer[_enum.Windows.ApplicationModel.Background.BackgroundAccessStatus]],  # result
                                                             _type.HRESULT]

    _factory = True


class IBackgroundTask(_inspectable.IInspectable):
    Run: _Callable[[IBackgroundTaskInstance],  # taskInstance
                   _type.HRESULT]


class IBackgroundTaskBuilder(_inspectable.IInspectable):
    put_TaskEntryPoint: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_TaskEntryPoint: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    SetTrigger: _Callable[[IBackgroundTrigger],  # trigger
                          _type.HRESULT]
    AddCondition: _Callable[[IBackgroundCondition],  # condition
                            _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    Register: _Callable[[_Pointer[IBackgroundTaskRegistration]],  # task
                        _type.HRESULT]


class IBackgroundTaskBuilder2(_inspectable.IInspectable):
    put_CancelOnConditionLoss: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_CancelOnConditionLoss: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class IBackgroundTaskBuilder3(_inspectable.IInspectable):
    put_IsNetworkRequested: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_IsNetworkRequested: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IBackgroundTaskBuilder4(_inspectable.IInspectable):
    get_TaskGroup: _Callable[[_Pointer[IBackgroundTaskRegistrationGroup]],  # value
                             _type.HRESULT]
    put_TaskGroup: _Callable[[IBackgroundTaskRegistrationGroup],  # value
                             _type.HRESULT]


class IBackgroundTaskBuilder5(_inspectable.IInspectable):
    SetTaskEntryPointClsid: _Callable[[_struct.GUID],  # TaskEntryPoint
                                      _type.HRESULT]


class IBackgroundTaskCompletedEventArgs(_inspectable.IInspectable):
    get_InstanceId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    CheckResult: _Callable[[],
                           _type.HRESULT]


class IBackgroundTaskDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IBackgroundTaskInstance(_inspectable.IInspectable):
    get_InstanceId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Task: _Callable[[_Pointer[IBackgroundTaskRegistration]],  # task
                        _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    put_Progress: _Callable[[_type.UINT32],  # value
                            _type.HRESULT]
    get_TriggerDetails: _Callable[[_Pointer[_inspectable.IInspectable]],  # triggerDetails
                                  _type.HRESULT]
    add_Canceled: _Callable[[IBackgroundTaskCanceledEventHandler,  # cancelHandler
                             _Pointer[_struct.EventRegistrationToken]],  # cookie
                            _type.HRESULT]
    remove_Canceled: _Callable[[_struct.EventRegistrationToken],  # cookie
                               _type.HRESULT]
    get_SuspendedCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IBackgroundTaskDeferral]],  # deferral
                           _type.HRESULT]


class IBackgroundTaskInstance2(_inspectable.IInspectable):
    GetThrottleCount: _Callable[[_enum.Windows.ApplicationModel.Background.BackgroundTaskThrottleCounter,  # counter
                                 _Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IBackgroundTaskInstance4(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IBackgroundTaskProgressEventArgs(_inspectable.IInspectable):
    get_InstanceId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class IBackgroundTaskRegistration(_inspectable.IInspectable):
    get_TaskId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    add_Progress: _Callable[[IBackgroundTaskProgressEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # cookie
                            _type.HRESULT]
    remove_Progress: _Callable[[_struct.EventRegistrationToken],  # cookie
                               _type.HRESULT]
    add_Completed: _Callable[[IBackgroundTaskCompletedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # cookie
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                _type.HRESULT]
    Unregister: _Callable[[_type.boolean],  # cancelTask
                          _type.HRESULT]


class IBackgroundTaskRegistration2(_inspectable.IInspectable):
    get_Trigger: _Callable[[_Pointer[IBackgroundTrigger]],  # value
                           _type.HRESULT]


class IBackgroundTaskRegistration3(_inspectable.IInspectable):
    get_TaskGroup: _Callable[[_Pointer[IBackgroundTaskRegistrationGroup]],  # value
                             _type.HRESULT]


class IBackgroundTaskRegistrationGroup(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    add_BackgroundActivated: _Callable[[_Windows_Foundation.ITypedEventHandler[IBackgroundTaskRegistrationGroup, _Windows_ApplicationModel_Activation.IBackgroundActivatedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_BackgroundActivated: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    get_AllTasks: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, IBackgroundTaskRegistration]]],  # value
                            _type.HRESULT]


class IBackgroundTaskRegistrationGroupFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # id
                       _Pointer[IBackgroundTaskRegistrationGroup]],  # group
                      _type.HRESULT]
    CreateWithName: _Callable[[_type.HSTRING,  # id
                               _type.HSTRING,  # name
                               _Pointer[IBackgroundTaskRegistrationGroup]],  # group
                              _type.HRESULT]

    _factory = True


class IBackgroundTaskRegistrationStatics(_inspectable.IInspectable):
    get_AllTasks: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_struct.GUID, IBackgroundTaskRegistration]]],  # tasks
                            _type.HRESULT]

    _factory = True


class IBackgroundTaskRegistrationStatics2(_inspectable.IInspectable):
    get_AllTaskGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IBackgroundTaskRegistrationGroup]]],  # value
                                 _type.HRESULT]
    GetTaskGroup: _Callable[[_type.HSTRING,  # groupId
                             _Pointer[IBackgroundTaskRegistrationGroup]],  # value
                            _type.HRESULT]

    _factory = True


class IBackgroundTrigger(_inspectable.IInspectable):
    pass


class IBackgroundWorkCostStatics(_inspectable.IInspectable):
    get_CurrentBackgroundWorkCost: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.BackgroundWorkCostValue]],  # value
                                             _type.HRESULT]

    _factory = True


class IBluetoothLEAdvertisementPublisherTrigger(_inspectable.IInspectable):
    get_Advertisement: _Callable[[_Pointer[_Windows_Devices_Bluetooth_Advertisement.IBluetoothLEAdvertisement]],  # value
                                 _type.HRESULT]


class IBluetoothLEAdvertisementPublisherTrigger2(_inspectable.IInspectable):
    get_PreferredTransmitPowerLevelInDBm: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT16]]],  # value
                                                    _type.HRESULT]
    put_PreferredTransmitPowerLevelInDBm: _Callable[[_Windows_Foundation.IReference[_type.INT16]],  # value
                                                    _type.HRESULT]
    get_UseExtendedFormat: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_UseExtendedFormat: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IsAnonymous: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsAnonymous: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_IncludeTransmitPowerLevel: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IncludeTransmitPowerLevel: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]


class IBluetoothLEAdvertisementWatcherTrigger(_inspectable.IInspectable):
    get_MinSamplingInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                       _type.HRESULT]
    get_MaxSamplingInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                       _type.HRESULT]
    get_MinOutOfRangeTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                        _type.HRESULT]
    get_MaxOutOfRangeTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                        _type.HRESULT]
    get_SignalStrengthFilter: _Callable[[_Pointer[_Windows_Devices_Bluetooth.IBluetoothSignalStrengthFilter]],  # value
                                        _type.HRESULT]
    put_SignalStrengthFilter: _Callable[[_Windows_Devices_Bluetooth.IBluetoothSignalStrengthFilter],  # value
                                        _type.HRESULT]
    get_AdvertisementFilter: _Callable[[_Pointer[_Windows_Devices_Bluetooth_Advertisement.IBluetoothLEAdvertisementFilter]],  # value
                                       _type.HRESULT]
    put_AdvertisementFilter: _Callable[[_Windows_Devices_Bluetooth_Advertisement.IBluetoothLEAdvertisementFilter],  # value
                                       _type.HRESULT]


class IBluetoothLEAdvertisementWatcherTrigger2(_inspectable.IInspectable):
    get_AllowExtendedAdvertisements: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_AllowExtendedAdvertisements: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]


class ICachedFileUpdaterTrigger(_inspectable.IInspectable):
    pass


class ICachedFileUpdaterTriggerDetails(_inspectable.IInspectable):
    get_UpdateTarget: _Callable[[_Pointer[_enum.Windows.Storage.Provider.CachedFileTarget]],  # value
                                _type.HRESULT]
    get_UpdateRequest: _Callable[[_Pointer[_Windows_Storage_Provider.IFileUpdateRequest]],  # value
                                 _type.HRESULT]
    get_CanRequestUserInput: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]


class IChatMessageNotificationTrigger(_inspectable.IInspectable):
    pass


class IChatMessageReceivedNotificationTrigger(_inspectable.IInspectable):
    pass


class ICommunicationBlockingAppSetAsActiveTrigger(_inspectable.IInspectable):
    pass


class IContactStoreNotificationTrigger(_inspectable.IInspectable):
    pass


class IContentPrefetchTrigger(_inspectable.IInspectable):
    get_WaitInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # waitInterval
                                _type.HRESULT]


class IContentPrefetchTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_struct.Windows.Foundation.TimeSpan,  # waitInterval
                       _Pointer[IContentPrefetchTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class ICustomSystemEventTrigger(_inspectable.IInspectable):
    get_TriggerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Recurrence: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence]],  # value
                              _type.HRESULT]


class ICustomSystemEventTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # triggerId
                       _enum.Windows.ApplicationModel.Background.CustomSystemEventTriggerRecurrence,  # recurrence
                       _Pointer[ICustomSystemEventTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class IDeviceConnectionChangeTrigger(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_CanMaintainConnection: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    get_MaintainConnection: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_MaintainConnection: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class IDeviceConnectionChangeTriggerStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IDeviceConnectionChangeTrigger]]],  # deviceChangeTrigger
                           _type.HRESULT]

    _factory = True


class IDeviceManufacturerNotificationTrigger(_inspectable.IInspectable):
    TriggerQualifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    OneShot: _Callable[[_Pointer[_type.boolean]],  # oneShot
                       _type.HRESULT]


class IDeviceManufacturerNotificationTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # triggerQualifier
                       _type.boolean,  # oneShot
                       _Pointer[IDeviceManufacturerNotificationTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class IDeviceServicingTrigger(_inspectable.IInspectable):
    RequestAsyncSimple: _Callable[[_type.HSTRING,  # deviceId
                                   _struct.Windows.Foundation.TimeSpan,  # expectedDuration
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.DeviceTriggerResult]]],  # result
                                  _type.HRESULT]
    RequestAsyncWithArguments: _Callable[[_type.HSTRING,  # deviceId
                                          _struct.Windows.Foundation.TimeSpan,  # expectedDuration
                                          _type.HSTRING,  # arguments
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.DeviceTriggerResult]]],  # result
                                         _type.HRESULT]


class IDeviceUseTrigger(_inspectable.IInspectable):
    RequestAsyncSimple: _Callable[[_type.HSTRING,  # deviceId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.DeviceTriggerResult]]],  # result
                                  _type.HRESULT]
    RequestAsyncWithArguments: _Callable[[_type.HSTRING,  # deviceId
                                          _type.HSTRING,  # arguments
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.DeviceTriggerResult]]],  # result
                                         _type.HRESULT]


class IDeviceWatcherTrigger(_inspectable.IInspectable):
    pass


class IEmailStoreNotificationTrigger(_inspectable.IInspectable):
    pass


class IGattCharacteristicNotificationTrigger(_inspectable.IInspectable):
    get_Characteristic: _Callable[[_Pointer[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattCharacteristic]],  # value
                                  _type.HRESULT]


class IGattCharacteristicNotificationTrigger2(_inspectable.IInspectable):
    get_EventTriggeringMode: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode]],  # value
                                       _type.HRESULT]


class IGattCharacteristicNotificationTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattCharacteristic,  # characteristic
                       _Pointer[IGattCharacteristicNotificationTrigger]],  # gattCharacteristicNotificationTrigger
                      _type.HRESULT]


class IGattCharacteristicNotificationTriggerFactory2(_inspectable.IInspectable):
    CreateWithEventTriggeringMode: _Callable[[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattCharacteristic,  # characteristic
                                              _enum.Windows.Devices.Bluetooth.Background.BluetoothEventTriggeringMode,  # eventTriggeringMode
                                              _Pointer[IGattCharacteristicNotificationTrigger]],  # result
                                             _type.HRESULT]

    _factory = True


class IGattServiceProviderTrigger(_inspectable.IInspectable):
    get_TriggerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Service: _Callable[[_Pointer[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattLocalService]],  # value
                           _type.HRESULT]
    put_AdvertisingParameters: _Callable[[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattServiceProviderAdvertisingParameters],  # value
                                         _type.HRESULT]
    get_AdvertisingParameters: _Callable[[_Pointer[_Windows_Devices_Bluetooth_GenericAttributeProfile.IGattServiceProviderAdvertisingParameters]],  # value
                                         _type.HRESULT]


class IGattServiceProviderTriggerResult(_inspectable.IInspectable):
    get_Trigger: _Callable[[_Pointer[IGattServiceProviderTrigger]],  # value
                           _type.HRESULT]
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]


class IGattServiceProviderTriggerStatics(_inspectable.IInspectable):
    CreateAsync: _Callable[[_type.HSTRING,  # triggerId
                            _struct.GUID,  # serviceUuid
                            _Pointer[_Windows_Foundation.IAsyncOperation[IGattServiceProviderTriggerResult]]],  # operation
                           _type.HRESULT]

    _factory = True


class IGeovisitTrigger(_inspectable.IInspectable):
    get_MonitoringScope: _Callable[[_Pointer[_enum.Windows.Devices.Geolocation.VisitMonitoringScope]],  # value
                                   _type.HRESULT]
    put_MonitoringScope: _Callable[[_enum.Windows.Devices.Geolocation.VisitMonitoringScope],  # value
                                   _type.HRESULT]


class ILocationTrigger(_inspectable.IInspectable):
    get_TriggerType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.LocationTriggerType]],  # triggerType
                               _type.HRESULT]


class ILocationTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.ApplicationModel.Background.LocationTriggerType,  # triggerType
                       _Pointer[ILocationTrigger]],  # locationTrigger
                      _type.HRESULT]

    _factory = True


class IMaintenanceTrigger(_inspectable.IInspectable):
    get_FreshnessTime: _Callable[[_Pointer[_type.UINT32]],  # freshnessTime
                                 _type.HRESULT]
    get_OneShot: _Callable[[_Pointer[_type.boolean]],  # oneShot
                           _type.HRESULT]


class IMaintenanceTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # freshnessTime
                       _type.boolean,  # oneShot
                       _Pointer[IMaintenanceTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class IMediaProcessingTrigger(_inspectable.IInspectable):
    RequestAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.MediaProcessingTriggerResult]]],  # result
                            _type.HRESULT]
    RequestAsyncWithArguments: _Callable[[_Windows_Foundation_Collections.IPropertySet,  # arguments
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Background.MediaProcessingTriggerResult]]],  # result
                                         _type.HRESULT]


class INetworkOperatorHotspotAuthenticationTrigger(_inspectable.IInspectable):
    pass


class INetworkOperatorNotificationTrigger(_inspectable.IInspectable):
    get_NetworkAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class INetworkOperatorNotificationTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # networkAccountId
                       _Pointer[INetworkOperatorNotificationTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class IPhoneTrigger(_inspectable.IInspectable):
    get_OneShot: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_TriggerType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Calls.Background.PhoneTriggerType]],  # result
                               _type.HRESULT]


class IPhoneTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.ApplicationModel.Calls.Background.PhoneTriggerType,  # type
                       _type.boolean,  # oneShot
                       _Pointer[IPhoneTrigger]],  # result
                      _type.HRESULT]

    _factory = True


class IPushNotificationTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # applicationId
                       _Pointer[IBackgroundTrigger]],  # value
                      _type.HRESULT]

    _factory = True


class IRcsEndUserMessageAvailableTrigger(_inspectable.IInspectable):
    pass


class IRfcommConnectionTrigger(_inspectable.IInspectable):
    get_InboundConnection: _Callable[[_Pointer[_Windows_Devices_Bluetooth_Background.IRfcommInboundConnectionInformation]],  # value
                                     _type.HRESULT]
    get_OutboundConnection: _Callable[[_Pointer[_Windows_Devices_Bluetooth_Background.IRfcommOutboundConnectionInformation]],  # value
                                      _type.HRESULT]
    get_AllowMultipleConnections: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_AllowMultipleConnections: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_ProtectionLevel: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketProtectionLevel]],  # value
                                   _type.HRESULT]
    put_ProtectionLevel: _Callable[[_enum.Windows.Networking.Sockets.SocketProtectionLevel],  # value
                                   _type.HRESULT]
    get_RemoteHostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                  _type.HRESULT]
    put_RemoteHostName: _Callable[[_Windows_Networking.IHostName],  # value
                                  _type.HRESULT]


class ISecondaryAuthenticationFactorAuthenticationTrigger(_inspectable.IInspectable):
    pass


class ISensorDataThresholdTrigger(_inspectable.IInspectable):
    pass


class ISensorDataThresholdTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Devices_Sensors.ISensorDataThreshold,  # threshold
                       _Pointer[ISensorDataThresholdTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class ISmartCardTrigger(_inspectable.IInspectable):
    get_TriggerType: _Callable[[_Pointer[_enum.Windows.Devices.SmartCards.SmartCardTriggerType]],  # triggerType
                               _type.HRESULT]


class ISmartCardTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.Devices.SmartCards.SmartCardTriggerType,  # triggerType
                       _Pointer[ISmartCardTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class ISmsMessageReceivedTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Devices_Sms.ISmsFilterRules,  # filterRules
                       _Pointer[IBackgroundTrigger]],  # value
                      _type.HRESULT]

    _factory = True


class ISocketActivityTrigger(_inspectable.IInspectable):
    get_IsWakeFromLowPowerSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IStorageLibraryChangeTrackerTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Storage.IStorageLibraryChangeTracker,  # tracker
                       _Pointer[IBackgroundTrigger]],  # result
                      _type.HRESULT]

    _factory = True


class IStorageLibraryContentChangedTrigger(_inspectable.IInspectable):
    pass


class IStorageLibraryContentChangedTriggerStatics(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Storage.IStorageLibrary,  # storageLibrary
                       _Pointer[IStorageLibraryContentChangedTrigger]],  # result
                      _type.HRESULT]
    CreateFromLibraries: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageLibrary],  # storageLibraries
                                    _Pointer[IStorageLibraryContentChangedTrigger]],  # result
                                   _type.HRESULT]

    _factory = True


class ISystemCondition(_inspectable.IInspectable):
    get_ConditionType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.SystemConditionType]],  # conditionType
                                 _type.HRESULT]


class ISystemConditionFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.ApplicationModel.Background.SystemConditionType,  # conditionType
                       _Pointer[ISystemCondition]],  # condition
                      _type.HRESULT]

    _factory = True


class ISystemTrigger(_inspectable.IInspectable):
    get_OneShot: _Callable[[_Pointer[_type.boolean]],  # oneShot
                           _type.HRESULT]
    get_TriggerType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Background.SystemTriggerType]],  # triggerType
                               _type.HRESULT]


class ISystemTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.ApplicationModel.Background.SystemTriggerType,  # triggerType
                       _type.boolean,  # oneShot
                       _Pointer[ISystemTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class ITimeTrigger(_inspectable.IInspectable):
    get_FreshnessTime: _Callable[[_Pointer[_type.UINT32]],  # freshnessTime
                                 _type.HRESULT]
    get_OneShot: _Callable[[_Pointer[_type.boolean]],  # oneShot
                           _type.HRESULT]


class ITimeTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.UINT32,  # freshnessTime
                       _type.boolean,  # oneShot
                       _Pointer[ITimeTrigger]],  # trigger
                      _type.HRESULT]

    _factory = True


class IToastNotificationActionTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # applicationId
                       _Pointer[IBackgroundTrigger]],  # value
                      _type.HRESULT]

    _factory = True


class IToastNotificationHistoryChangedTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_type.HSTRING,  # applicationId
                       _Pointer[IBackgroundTrigger]],  # value
                      _type.HRESULT]

    _factory = True


class IUserNotificationChangedTriggerFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.UI.Notifications.NotificationKinds,  # notificationKinds
                       _Pointer[IBackgroundTrigger]],  # value
                      _type.HRESULT]

    _factory = True
