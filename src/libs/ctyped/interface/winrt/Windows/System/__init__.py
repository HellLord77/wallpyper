from __future__ import annotations as _

from typing import Callable as _Callable

from . import Diagnostics as _Windows_System_Diagnostics
from . import RemoteSystems as _Windows_System_RemoteSystems
from .. import ApplicationModel as _Windows_ApplicationModel
from .. import Foundation as _Windows_Foundation
from .. import Storage as _Windows_Storage
from ..Foundation import Collections as _Windows_Foundation_Collections
from ..Storage import Search as _Windows_Storage_Search
from ..Storage import Streams as _Windows_Storage_Streams
from ... import inspectable as _inspectable
from ....um import Unknwnbase as _Unknwnbase
from ..... import enum as _enum
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class _IDispatcherQueueHandler:
    Invoke: _Callable[[],
                      _type.HRESULT]


class IDispatcherQueueHandler(_IDispatcherQueueHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDispatcherQueueHandler_impl(_IDispatcherQueueHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAppActivationResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_AppResourceGroupInfo: _Callable[[_Pointer[IAppResourceGroupInfo]],  # value
                                        _type.HRESULT]


class IAppDiagnosticInfo(_inspectable.IInspectable):
    get_AppInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppInfo]],  # value
                           _type.HRESULT]


class IAppDiagnosticInfo2(_inspectable.IInspectable):
    GetResourceGroups: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAppResourceGroupInfo]]],  # result
                                 _type.HRESULT]
    CreateResourceGroupWatcher: _Callable[[_Pointer[IAppResourceGroupInfoWatcher]],  # result
                                          _type.HRESULT]


class IAppDiagnosticInfo3(_inspectable.IInspectable):
    LaunchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAppActivationResult]]],  # operation
                           _type.HRESULT]


class IAppDiagnosticInfoStatics(_inspectable.IInspectable, factory=True):
    RequestInfoAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IAppDiagnosticInfo]]]],  # operation
                                _type.HRESULT]


class IAppDiagnosticInfoStatics2(_inspectable.IInspectable, factory=True):
    CreateWatcher: _Callable[[_Pointer[IAppDiagnosticInfoWatcher]],  # watcher
                             _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.DiagnosticAccessStatus]]],  # operation
                                  _type.HRESULT]
    RequestInfoForPackageAsync: _Callable[[_type.HSTRING,  # packageFamilyName
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IAppDiagnosticInfo]]]],  # operation
                                          _type.HRESULT]
    RequestInfoForAppAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IAppDiagnosticInfo]]]],  # operation
                                      _type.HRESULT]
    RequestInfoForAppUserModelId: _Callable[[_type.HSTRING,  # appUserModelId
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IAppDiagnosticInfo]]]],  # operation
                                            _type.HRESULT]


class IAppDiagnosticInfoWatcher(_inspectable.IInspectable):
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppDiagnosticInfoWatcher, IAppDiagnosticInfoWatcherEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppDiagnosticInfoWatcher, IAppDiagnosticInfoWatcherEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppDiagnosticInfoWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppDiagnosticInfoWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.System.AppDiagnosticInfoWatcherStatus]],  # value
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IAppDiagnosticInfoWatcherEventArgs(_inspectable.IInspectable):
    get_AppDiagnosticInfo: _Callable[[_Pointer[IAppDiagnosticInfo]],  # value
                                     _type.HRESULT]


class IAppExecutionStateChangeResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IAppMemoryReport(_inspectable.IInspectable):
    get_PrivateCommitUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                      _type.HRESULT]
    get_PeakPrivateCommitUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                          _type.HRESULT]
    get_TotalCommitUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    get_TotalCommitLimit: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]


class IAppMemoryReport2(_inspectable.IInspectable):
    get_ExpectedTotalCommitLimit: _Callable[[_Pointer[_type.UINT64]],  # value
                                            _type.HRESULT]


class IAppMemoryUsageLimitChangingEventArgs(_inspectable.IInspectable):
    get_OldLimit: _Callable[[_Pointer[_type.UINT64]],  # value
                            _type.HRESULT]
    get_NewLimit: _Callable[[_Pointer[_type.UINT64]],  # value
                            _type.HRESULT]


class IAppResourceGroupBackgroundTaskReport(_inspectable.IInspectable):
    get_TaskId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Trigger: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_EntryPoint: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IAppResourceGroupInfo(_inspectable.IInspectable):
    get_InstanceId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_IsShared: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    GetBackgroundTaskReports: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAppResourceGroupBackgroundTaskReport]]],  # result
                                        _type.HRESULT]
    GetMemoryReport: _Callable[[_Pointer[IAppResourceGroupMemoryReport]],  # result
                               _type.HRESULT]
    GetProcessDiagnosticInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_System_Diagnostics.IProcessDiagnosticInfo]]],  # result
                                         _type.HRESULT]
    GetStateReport: _Callable[[_Pointer[IAppResourceGroupStateReport]],  # result
                              _type.HRESULT]


class IAppResourceGroupInfo2(_inspectable.IInspectable):
    StartSuspendAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAppExecutionStateChangeResult]]],  # operation
                                 _type.HRESULT]
    StartResumeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAppExecutionStateChangeResult]]],  # operation
                                _type.HRESULT]
    StartTerminateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IAppExecutionStateChangeResult]]],  # operation
                                   _type.HRESULT]


class IAppResourceGroupInfoWatcher(_inspectable.IInspectable):
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppResourceGroupInfoWatcher, IAppResourceGroupInfoWatcherEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppResourceGroupInfoWatcher, IAppResourceGroupInfoWatcherEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppResourceGroupInfoWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppResourceGroupInfoWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_ExecutionStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppResourceGroupInfoWatcher, IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_ExecutionStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.System.AppResourceGroupInfoWatcherStatus]],  # status
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]


class IAppResourceGroupInfoWatcherEventArgs(_inspectable.IInspectable):
    get_AppDiagnosticInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppDiagnosticInfo]]],  # value
                                      _type.HRESULT]
    get_AppResourceGroupInfo: _Callable[[_Pointer[IAppResourceGroupInfo]],  # value
                                        _type.HRESULT]


class IAppResourceGroupInfoWatcherExecutionStateChangedEventArgs(_inspectable.IInspectable):
    get_AppDiagnosticInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppDiagnosticInfo]]],  # value
                                      _type.HRESULT]
    get_AppResourceGroupInfo: _Callable[[_Pointer[IAppResourceGroupInfo]],  # value
                                        _type.HRESULT]


class IAppResourceGroupMemoryReport(_inspectable.IInspectable):
    get_CommitUsageLimit: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    get_CommitUsageLevel: _Callable[[_Pointer[_enum.Windows.System.AppMemoryUsageLevel]],  # value
                                    _type.HRESULT]
    get_PrivateCommitUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                      _type.HRESULT]
    get_TotalCommitUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]


class IAppResourceGroupStateReport(_inspectable.IInspectable):
    get_ExecutionState: _Callable[[_Pointer[_enum.Windows.System.AppResourceGroupExecutionState]],  # value
                                  _type.HRESULT]
    get_EnergyQuotaState: _Callable[[_Pointer[_enum.Windows.System.AppResourceGroupEnergyQuotaState]],  # value
                                    _type.HRESULT]


class IAppUriHandlerHost(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IAppUriHandlerHost2(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]


class IAppUriHandlerHostFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # name
                               _Pointer[IAppUriHandlerHost]],  # value
                              _type.HRESULT]


class IAppUriHandlerRegistration(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_User: _Callable[[_Pointer[IUser]],  # value
                        _type.HRESULT]
    GetAppAddedHostsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IAppUriHandlerHost]]]],  # operation
                                     _type.HRESULT]
    SetAppAddedHostsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IAppUriHandlerHost],  # hosts
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                     _type.HRESULT]


class IAppUriHandlerRegistration2(_inspectable.IInspectable):
    GetAllHosts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAppUriHandlerHost]]],  # result
                           _type.HRESULT]
    UpdateHosts: _Callable[[_Windows_Foundation_Collections.IIterable[IAppUriHandlerHost]],  # hosts
                           _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IAppUriHandlerRegistrationManager(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[IUser]],  # value
                        _type.HRESULT]
    TryGetRegistration: _Callable[[_type.HSTRING,  # name
                                   _Pointer[IAppUriHandlerRegistration]],  # result
                                  _type.HRESULT]


class IAppUriHandlerRegistrationManager2(_inspectable.IInspectable):
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IAppUriHandlerRegistrationManagerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IAppUriHandlerRegistrationManager]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[IUser,  # user
                           _Pointer[IAppUriHandlerRegistrationManager]],  # result
                          _type.HRESULT]


class IAppUriHandlerRegistrationManagerStatics2(_inspectable.IInspectable, factory=True):
    GetForPackage: _Callable[[_type.HSTRING,  # packageFamilyName
                              _Pointer[IAppUriHandlerRegistrationManager]],  # result
                             _type.HRESULT]
    GetForPackageForUser: _Callable[[_type.HSTRING,  # packageFamilyName
                                     IUser,  # user
                                     _Pointer[IAppUriHandlerRegistrationManager]],  # result
                                    _type.HRESULT]


class IDateTimeSettingsStatics(_inspectable.IInspectable, factory=True):
    SetSystemDateTime: _Callable[[_struct.Windows.Foundation.DateTime],  # utcDateTime
                                 _type.HRESULT]


class IDispatcherQueue(_inspectable.IInspectable):
    CreateTimer: _Callable[[_Pointer[IDispatcherQueueTimer]],  # result
                           _type.HRESULT]
    TryEnqueue: _Callable[[IDispatcherQueueHandler,  # callback
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    TryEnqueueWithPriority: _Callable[[_enum.Windows.System.DispatcherQueuePriority,  # priority
                                       IDispatcherQueueHandler,  # callback
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    add_ShutdownStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueue, IDispatcherQueueShutdownStartingEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ShutdownStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ShutdownCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueue, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ShutdownCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IDispatcherQueue2(_inspectable.IInspectable):
    get_HasThreadAccess: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IDispatcherQueueController(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[IDispatcherQueue]],  # value
                                   _type.HRESULT]
    ShutdownQueueAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]


class IDispatcherQueueControllerStatics(_inspectable.IInspectable, factory=True):
    CreateOnDedicatedThread: _Callable[[_Pointer[IDispatcherQueueController]],  # result
                                       _type.HRESULT]


class IDispatcherQueueShutdownStartingEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IDispatcherQueueStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentThread: _Callable[[_Pointer[IDispatcherQueue]],  # result
                                   _type.HRESULT]


class IDispatcherQueueTimer(_inspectable.IInspectable):
    get_Interval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Interval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_IsRunning: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsRepeating: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsRepeating: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_Tick: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueueTimer, _inspectable.IInspectable],  # handler
                         _Pointer[_struct.EventRegistrationToken]],  # token
                        _type.HRESULT]
    remove_Tick: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]


class IFolderLauncherOptions(_inspectable.IInspectable):
    get_ItemsToSelect: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Storage.IStorageItem]]],  # value
                                 _type.HRESULT]


class IKnownUserPropertiesStatics(_inspectable.IInspectable, factory=True):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_FirstName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_LastName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ProviderName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_AccountName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_GuestHost: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_PrincipalName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_DomainName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_SessionInitiationProtocolUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                _type.HRESULT]


class IKnownUserPropertiesStatics2(_inspectable.IInspectable, factory=True):
    get_AgeEnforcementRegion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]


class ILaunchUriResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.System.LaunchUriStatus]],  # value
                          _type.HRESULT]
    get_Result: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                          _type.HRESULT]


class ILauncherOptions(_inspectable.IInspectable):
    get_TreatAsUntrusted: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_TreatAsUntrusted: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_DisplayApplicationPicker: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_DisplayApplicationPicker: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_UI: _Callable[[_Pointer[ILauncherUIOptions]],  # value
                      _type.HRESULT]
    get_PreferredApplicationPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                         _type.HRESULT]
    put_PreferredApplicationPackageFamilyName: _Callable[[_type.HSTRING],  # value
                                                         _type.HRESULT]
    get_PreferredApplicationDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                   _type.HRESULT]
    put_PreferredApplicationDisplayName: _Callable[[_type.HSTRING],  # value
                                                   _type.HRESULT]
    get_FallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_FallbackUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]
    get_ContentType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ContentType: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class ILauncherOptions2(_inspectable.IInspectable):
    get_TargetApplicationPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                      _type.HRESULT]
    put_TargetApplicationPackageFamilyName: _Callable[[_type.HSTRING],  # value
                                                      _type.HRESULT]
    get_NeighboringFilesQuery: _Callable[[_Pointer[_Windows_Storage_Search.IStorageFileQueryResult]],  # value
                                         _type.HRESULT]
    put_NeighboringFilesQuery: _Callable[[_Windows_Storage_Search.IStorageFileQueryResult],  # value
                                         _type.HRESULT]


class ILauncherOptions3(_inspectable.IInspectable):
    get_IgnoreAppUriHandlers: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IgnoreAppUriHandlers: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]


class ILauncherOptions4(_inspectable.IInspectable):
    get_LimitPickerToCurrentAppAndAppUriHandlers: _Callable[[_Pointer[_type.boolean]],  # value
                                                            _type.HRESULT]
    put_LimitPickerToCurrentAppAndAppUriHandlers: _Callable[[_type.boolean],  # value
                                                            _type.HRESULT]


class ILauncherStatics(_inspectable.IInspectable, factory=True):
    LaunchFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                               _type.HRESULT]
    LaunchFileWithOptionsAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                           ILauncherOptions,  # options
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    LaunchUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                              _type.HRESULT]
    LaunchUriWithOptionsAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                          ILauncherOptions,  # options
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]


class ILauncherStatics2(_inspectable.IInspectable, factory=True):
    LaunchUriForResultsAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                         ILauncherOptions,  # options
                                         _Pointer[_Windows_Foundation.IAsyncOperation[ILaunchUriResult]]],  # operation
                                        _type.HRESULT]
    LaunchUriForResultsWithDataAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                                 ILauncherOptions,  # options
                                                 _Windows_Foundation_Collections.IPropertySet,  # inputData
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[ILaunchUriResult]]],  # operation
                                                _type.HRESULT]
    LaunchUriWithDataAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                       ILauncherOptions,  # options
                                       _Windows_Foundation_Collections.IPropertySet,  # inputData
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]
    QueryUriSupportAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                     _enum.Windows.System.LaunchQuerySupportType,  # launchQuerySupportType
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchQuerySupportStatus]]],  # operation
                                    _type.HRESULT]
    QueryUriSupportWithPackageFamilyNameAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                                          _enum.Windows.System.LaunchQuerySupportType,  # launchQuerySupportType
                                                          _type.HSTRING,  # packageFamilyName
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchQuerySupportStatus]]],  # operation
                                                         _type.HRESULT]
    QueryFileSupportAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchQuerySupportStatus]]],  # operation
                                     _type.HRESULT]
    QueryFileSupportWithPackageFamilyNameAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                                           _type.HSTRING,  # packageFamilyName
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchQuerySupportStatus]]],  # operation
                                                          _type.HRESULT]
    FindUriSchemeHandlersAsync: _Callable[[_type.HSTRING,  # scheme
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel.IAppInfo]]]],  # operation
                                          _type.HRESULT]
    FindUriSchemeHandlersWithLaunchUriTypeAsync: _Callable[[_type.HSTRING,  # scheme
                                                            _enum.Windows.System.LaunchQuerySupportType,  # launchQuerySupportType
                                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel.IAppInfo]]]],  # operation
                                                           _type.HRESULT]
    FindFileHandlersAsync: _Callable[[_type.HSTRING,  # extension
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel.IAppInfo]]]],  # operation
                                     _type.HRESULT]


class ILauncherStatics3(_inspectable.IInspectable, factory=True):
    LaunchFolderAsync: _Callable[[_Windows_Storage.IStorageFolder,  # folder
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                 _type.HRESULT]
    LaunchFolderWithOptionsAsync: _Callable[[_Windows_Storage.IStorageFolder,  # folder
                                             IFolderLauncherOptions,  # options
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                            _type.HRESULT]


class ILauncherStatics4(_inspectable.IInspectable, factory=True):
    QueryAppUriSupportAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchQuerySupportStatus]]],  # operation
                                       _type.HRESULT]
    QueryAppUriSupportWithPackageFamilyNameAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                                             _type.HSTRING,  # packageFamilyName
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchQuerySupportStatus]]],  # operation
                                                            _type.HRESULT]
    FindAppUriHandlersAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel.IAppInfo]]]],  # operation
                                       _type.HRESULT]
    LaunchUriForUserAsync: _Callable[[IUser,  # user
                                      _Windows_Foundation.IUriRuntimeClass,  # uri
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchUriStatus]]],  # operation
                                     _type.HRESULT]
    LaunchUriWithOptionsForUserAsync: _Callable[[IUser,  # user
                                                 _Windows_Foundation.IUriRuntimeClass,  # uri
                                                 ILauncherOptions,  # options
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchUriStatus]]],  # operation
                                                _type.HRESULT]
    LaunchUriWithDataForUserAsync: _Callable[[IUser,  # user
                                              _Windows_Foundation.IUriRuntimeClass,  # uri
                                              ILauncherOptions,  # options
                                              _Windows_Foundation_Collections.IPropertySet,  # inputData
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.LaunchUriStatus]]],  # operation
                                             _type.HRESULT]
    LaunchUriForResultsForUserAsync: _Callable[[IUser,  # user
                                                _Windows_Foundation.IUriRuntimeClass,  # uri
                                                ILauncherOptions,  # options
                                                _Pointer[_Windows_Foundation.IAsyncOperation[ILaunchUriResult]]],  # operation
                                               _type.HRESULT]
    LaunchUriForResultsWithDataForUserAsync: _Callable[[IUser,  # user
                                                        _Windows_Foundation.IUriRuntimeClass,  # uri
                                                        ILauncherOptions,  # options
                                                        _Windows_Foundation_Collections.IPropertySet,  # inputData
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[ILaunchUriResult]]],  # operation
                                                       _type.HRESULT]


class ILauncherStatics5(_inspectable.IInspectable, factory=True):
    LaunchFolderPathAsync: _Callable[[_type.HSTRING,  # path
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]
    LaunchFolderPathWithOptionsAsync: _Callable[[_type.HSTRING,  # path
                                                 IFolderLauncherOptions,  # options
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                _type.HRESULT]
    LaunchFolderPathForUserAsync: _Callable[[IUser,  # user
                                             _type.HSTRING,  # path
                                             _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                            _type.HRESULT]
    LaunchFolderPathWithOptionsForUserAsync: _Callable[[IUser,  # user
                                                        _type.HSTRING,  # path
                                                        IFolderLauncherOptions,  # options
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                       _type.HRESULT]


class ILauncherUIOptions(_inspectable.IInspectable):
    get_InvocationPoint: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]]],  # value
                                   _type.HRESULT]
    put_InvocationPoint: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Point]],  # value
                                   _type.HRESULT]
    get_SelectionRect: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]]],  # value
                                 _type.HRESULT]
    put_SelectionRect: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    get_PreferredPlacement: _Callable[[_Pointer[_enum.Windows.UI.Popups.Placement]],  # value
                                      _type.HRESULT]
    put_PreferredPlacement: _Callable[[_enum.Windows.UI.Popups.Placement],  # value
                                      _type.HRESULT]


class ILauncherViewOptions(_inspectable.IInspectable):
    get_DesiredRemainingView: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ViewSizePreference]],  # value
                                        _type.HRESULT]
    put_DesiredRemainingView: _Callable[[_enum.Windows.UI.ViewManagement.ViewSizePreference],  # value
                                        _type.HRESULT]


class IMemoryManagerStatics(_inspectable.IInspectable, factory=True):
    get_AppMemoryUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                  _type.HRESULT]
    get_AppMemoryUsageLimit: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_AppMemoryUsageLevel: _Callable[[_Pointer[_enum.Windows.System.AppMemoryUsageLevel]],  # value
                                       _type.HRESULT]
    add_AppMemoryUsageIncreased: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_AppMemoryUsageIncreased: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_AppMemoryUsageDecreased: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_AppMemoryUsageDecreased: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_AppMemoryUsageLimitChanging: _Callable[[_Windows_Foundation.IEventHandler[IAppMemoryUsageLimitChangingEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_AppMemoryUsageLimitChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]


class IMemoryManagerStatics2(_inspectable.IInspectable, factory=True):
    GetAppMemoryReport: _Callable[[_Pointer[IAppMemoryReport]],  # memoryReport
                                  _type.HRESULT]
    GetProcessMemoryReport: _Callable[[_Pointer[IProcessMemoryReport]],  # memoryReport
                                      _type.HRESULT]


class IMemoryManagerStatics3(_inspectable.IInspectable, factory=True):
    TrySetAppMemoryUsageLimit: _Callable[[_type.UINT64,  # value
                                          _Pointer[_type.boolean]],  # result
                                         _type.HRESULT]


class IMemoryManagerStatics4(_inspectable.IInspectable, factory=True):
    get_ExpectedAppMemoryUsageLimit: _Callable[[_Pointer[_type.UINT64]],  # value
                                               _type.HRESULT]


class IProcessLauncherOptions(_inspectable.IInspectable):
    get_StandardInput: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                                 _type.HRESULT]
    put_StandardInput: _Callable[[_Windows_Storage_Streams.IInputStream],  # value
                                 _type.HRESULT]
    get_StandardOutput: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                  _type.HRESULT]
    put_StandardOutput: _Callable[[_Windows_Storage_Streams.IOutputStream],  # value
                                  _type.HRESULT]
    get_StandardError: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                 _type.HRESULT]
    put_StandardError: _Callable[[_Windows_Storage_Streams.IOutputStream],  # value
                                 _type.HRESULT]
    get_WorkingDirectory: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_WorkingDirectory: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]


class IProcessLauncherResult(_inspectable.IInspectable):
    get_ExitCode: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]


class IProcessLauncherStatics(_inspectable.IInspectable, factory=True):
    RunToCompletionAsync: _Callable[[_type.HSTRING,  # fileName
                                     _type.HSTRING,  # args
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IProcessLauncherResult]]],  # asyncOperationResult
                                    _type.HRESULT]
    RunToCompletionAsyncWithOptions: _Callable[[_type.HSTRING,  # fileName
                                                _type.HSTRING,  # args
                                                IProcessLauncherOptions,  # options
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IProcessLauncherResult]]],  # asyncOperationResult
                                               _type.HRESULT]


class IProcessMemoryReport(_inspectable.IInspectable):
    get_PrivateWorkingSetUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                          _type.HRESULT]
    get_TotalWorkingSetUsage: _Callable[[_Pointer[_type.UINT64]],  # value
                                        _type.HRESULT]


class IProtocolForResultsOperation(_inspectable.IInspectable):
    ReportCompleted: _Callable[[_Windows_Foundation_Collections.IPropertySet],  # data
                               _type.HRESULT]


class IRemoteLauncherOptions(_inspectable.IInspectable):
    get_FallbackUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_FallbackUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]
    get_PreferredAppIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                   _type.HRESULT]


class IRemoteLauncherStatics(_inspectable.IInspectable, factory=True):
    LaunchUriAsync: _Callable[[_Windows_System_RemoteSystems.IRemoteSystemConnectionRequest,  # remoteSystemConnectionRequest
                               _Windows_Foundation.IUriRuntimeClass,  # uri
                               _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.RemoteLaunchUriStatus]]],  # operation
                              _type.HRESULT]
    LaunchUriWithOptionsAsync: _Callable[[_Windows_System_RemoteSystems.IRemoteSystemConnectionRequest,  # remoteSystemConnectionRequest
                                          _Windows_Foundation.IUriRuntimeClass,  # uri
                                          IRemoteLauncherOptions,  # options
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.RemoteLaunchUriStatus]]],  # operation
                                         _type.HRESULT]
    LaunchUriWithDataAsync: _Callable[[_Windows_System_RemoteSystems.IRemoteSystemConnectionRequest,  # remoteSystemConnectionRequest
                                       _Windows_Foundation.IUriRuntimeClass,  # uri
                                       IRemoteLauncherOptions,  # options
                                       _Windows_Foundation_Collections.IPropertySet,  # inputData
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.RemoteLaunchUriStatus]]],  # operation
                                      _type.HRESULT]


class IShutdownManagerStatics(_inspectable.IInspectable, factory=True):
    BeginShutdown: _Callable[[_enum.Windows.System.ShutdownKind,  # shutdownKind
                              _struct.Windows.Foundation.TimeSpan],  # timeout
                             _type.HRESULT]
    CancelShutdown: _Callable[[],
                              _type.HRESULT]


class IShutdownManagerStatics2(_inspectable.IInspectable, factory=True):
    IsPowerStateSupported: _Callable[[_enum.Windows.System.PowerState,  # powerState
                                      _Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    EnterPowerState: _Callable[[_enum.Windows.System.PowerState],  # powerState
                               _type.HRESULT]
    EnterPowerStateWithTimeSpan: _Callable[[_enum.Windows.System.PowerState,  # powerState
                                            _struct.Windows.Foundation.TimeSpan],  # wakeUpAfter
                                           _type.HRESULT]


class ITimeZoneSettingsStatics(_inspectable.IInspectable, factory=True):
    get_CurrentTimeZoneDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_SupportedTimeZoneDisplayNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                                 _type.HRESULT]
    get_CanChangeTimeZone: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    ChangeTimeZoneByDisplayName: _Callable[[_type.HSTRING],  # timeZoneDisplayName
                                           _type.HRESULT]


class ITimeZoneSettingsStatics2(_inspectable.IInspectable, factory=True):
    AutoUpdateTimeZoneAsync: _Callable[[_struct.Windows.Foundation.TimeSpan,  # timeout
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.AutoUpdateTimeZoneStatus]]],  # operation
                                       _type.HRESULT]


class IUser(_inspectable.IInspectable):
    get_NonRoamableId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_AuthenticationStatus: _Callable[[_Pointer[_enum.Windows.System.UserAuthenticationStatus]],  # value
                                        _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.System.UserType]],  # value
                        _type.HRESULT]
    GetPropertyAsync: _Callable[[_type.HSTRING,  # value
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_inspectable.IInspectable]]],  # operation
                                _type.HRESULT]
    GetPropertiesAsync: _Callable[[_Windows_Foundation_Collections.IVectorView[_type.HSTRING],  # values
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IPropertySet]]],  # operation
                                  _type.HRESULT]
    GetPictureAsync: _Callable[[_enum.Windows.System.UserPictureSize,  # desiredSize
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # operation
                               _type.HRESULT]


class IUser2(_inspectable.IInspectable):
    CheckUserAgeConsentGroupAsync: _Callable[[_enum.Windows.System.UserAgeConsentGroup,  # consentGroup
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.System.UserAgeConsentResult]]],  # operation
                                             _type.HRESULT]


class IUserAuthenticationStatusChangeDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IUserAuthenticationStatusChangingEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IUserAuthenticationStatusChangeDeferral]],  # result
                           _type.HRESULT]
    get_User: _Callable[[_Pointer[IUser]],  # value
                        _type.HRESULT]
    get_NewStatus: _Callable[[_Pointer[_enum.Windows.System.UserAuthenticationStatus]],  # value
                             _type.HRESULT]
    get_CurrentStatus: _Callable[[_Pointer[_enum.Windows.System.UserAuthenticationStatus]],  # value
                                 _type.HRESULT]


class IUserChangedEventArgs(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[IUser]],  # value
                        _type.HRESULT]


class IUserChangedEventArgs2(_inspectable.IInspectable):
    get_ChangedPropertyKinds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.System.UserWatcherUpdateKind]]],  # value
                                        _type.HRESULT]


class IUserDeviceAssociationChangedEventArgs(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_NewUser: _Callable[[_Pointer[IUser]],  # value
                           _type.HRESULT]
    get_OldUser: _Callable[[_Pointer[IUser]],  # value
                           _type.HRESULT]


class IUserDeviceAssociationStatics(_inspectable.IInspectable, factory=True):
    FindUserFromDeviceId: _Callable[[_type.HSTRING,  # deviceId
                                     _Pointer[IUser]],  # user
                                    _type.HRESULT]
    add_UserDeviceAssociationChanged: _Callable[[_Windows_Foundation.IEventHandler[IUserDeviceAssociationChangedEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_UserDeviceAssociationChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]


class IUserPicker(_inspectable.IInspectable):
    get_AllowGuestAccounts: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_AllowGuestAccounts: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_SuggestedSelectedUser: _Callable[[_Pointer[IUser]],  # value
                                         _type.HRESULT]
    put_SuggestedSelectedUser: _Callable[[IUser],  # value
                                         _type.HRESULT]
    PickSingleUserAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IUser]]],  # operation
                                   _type.HRESULT]


class IUserPickerStatics(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IUserStatics(_inspectable.IInspectable, factory=True):
    CreateWatcher: _Callable[[_Pointer[IUserWatcher]],  # result
                             _type.HRESULT]
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUser]]]],  # operation
                            _type.HRESULT]
    FindAllAsyncByType: _Callable[[_enum.Windows.System.UserType,  # type
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUser]]]],  # operation
                                  _type.HRESULT]
    FindAllAsyncByTypeAndStatus: _Callable[[_enum.Windows.System.UserType,  # type
                                            _enum.Windows.System.UserAuthenticationStatus,  # status
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUser]]]],  # operation
                                           _type.HRESULT]
    GetFromId: _Callable[[_type.HSTRING,  # nonRoamableId
                          _Pointer[IUser]],  # result
                         _type.HRESULT]


class IUserStatics2(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IUser]],  # result
                          _type.HRESULT]


class IUserWatcher(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.System.UserWatcherStatus]],  # value
                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_Added: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserWatcher, IUserChangedEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Added: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_Removed: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserWatcher, IUserChangedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Removed: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_Updated: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserWatcher, IUserChangedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Updated: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    add_AuthenticationStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserWatcher, IUserChangedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_AuthenticationStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_AuthenticationStatusChanging: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserWatcher, IUserAuthenticationStatusChangingEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_AuthenticationStatusChanging: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]
    add_EnumerationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserWatcher, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_EnumerationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_Stopped: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserWatcher, _inspectable.IInspectable],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Stopped: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
