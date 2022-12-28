from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import Foundation as _Windows_Foundation
from ..... import System as _Windows_System
from .....Foundation import Collections as _Windows_Foundation_Collections
from .....Management import Deployment as _Windows_Management_Deployment
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IAppInstallItem(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_InstallType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallType]],  # value
                               _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    GetCurrentStatus: _Callable[[_Pointer[IAppInstallStatus]],  # result
                                _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Restart: _Callable[[],
                       _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppInstallItem, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppInstallItem, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IAppInstallItem2(_inspectable.IInspectable):
    CancelWithTelemetry: _Callable[[_type.HSTRING],  # correlationVector
                                   _type.HRESULT]
    PauseWithTelemetry: _Callable[[_type.HSTRING],  # correlationVector
                                  _type.HRESULT]
    RestartWithTelemetry: _Callable[[_type.HSTRING],  # correlationVector
                                    _type.HRESULT]


class IAppInstallItem3(_inspectable.IInspectable):
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]],  # value
                            _type.HRESULT]
    get_ItemOperationsMightAffectOtherItems: _Callable[[_Pointer[_type.boolean]],  # value
                                                       _type.HRESULT]


class IAppInstallItem4(_inspectable.IInspectable):
    get_LaunchAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_LaunchAfterInstall: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class IAppInstallItem5(_inspectable.IInspectable):
    get_PinToDesktopAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_PinToDesktopAfterInstall: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_PinToStartAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_PinToStartAfterInstall: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_PinToTaskbarAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_PinToTaskbarAfterInstall: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_CompletedInstallToastNotificationMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode]],  # value
                                                         _type.HRESULT]
    put_CompletedInstallToastNotificationMode: _Callable[[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode],  # value
                                                         _type.HRESULT]
    get_InstallInProgressToastNotificationMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode]],  # value
                                                          _type.HRESULT]
    put_InstallInProgressToastNotificationMode: _Callable[[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode],  # value
                                                          _type.HRESULT]


class IAppInstallManager(_inspectable.IInspectable):
    get_AppInstallItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]],  # value
                                   _type.HRESULT]
    Cancel: _Callable[[_type.HSTRING],  # productId
                      _type.HRESULT]
    Pause: _Callable[[_type.HSTRING],  # productId
                     _type.HRESULT]
    Restart: _Callable[[_type.HSTRING],  # productId
                       _type.HRESULT]
    add_ItemCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppInstallManager, IAppInstallManagerItemEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ItemCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_ItemStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppInstallManager, IAppInstallManagerItemEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ItemStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    get_AutoUpdateSetting: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AutoUpdateSetting]],  # value
                                     _type.HRESULT]
    put_AutoUpdateSetting: _Callable[[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AutoUpdateSetting],  # value
                                     _type.HRESULT]
    get_AcquisitionIdentity: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_AcquisitionIdentity: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    GetIsApplicableAsync: _Callable[[_type.HSTRING,  # productId
                                     _type.HSTRING,  # skuId
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                    _type.HRESULT]
    StartAppInstallAsync: _Callable[[_type.HSTRING,  # productId
                                     _type.HSTRING,  # skuId
                                     _type.boolean,  # repair
                                     _type.boolean,  # forceUseOfNonRemovableStorage
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                    _type.HRESULT]
    UpdateAppByPackageFamilyNameAsync: _Callable[[_type.HSTRING,  # packageFamilyName
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                                 _type.HRESULT]
    SearchForUpdatesAsync: _Callable[[_type.HSTRING,  # productId
                                      _type.HSTRING,  # skuId
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                     _type.HRESULT]
    SearchForAllUpdatesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                        _type.HRESULT]
    IsStoreBlockedByPolicyAsync: _Callable[[_type.HSTRING,  # storeClientName
                                            _type.HSTRING,  # storeClientPublisher
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]
    GetIsAppAllowedToInstallAsync: _Callable[[_type.HSTRING,  # productId
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                             _type.HRESULT]


class IAppInstallManager2(_inspectable.IInspectable):
    StartAppInstallWithTelemetryAsync: _Callable[[_type.HSTRING,  # productId
                                                  _type.HSTRING,  # skuId
                                                  _type.boolean,  # repair
                                                  _type.boolean,  # forceUseOfNonRemovableStorage
                                                  _type.HSTRING,  # catalogId
                                                  _type.HSTRING,  # bundleId
                                                  _type.HSTRING,  # correlationVector
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                                 _type.HRESULT]
    UpdateAppByPackageFamilyNameWithTelemetryAsync: _Callable[[_type.HSTRING,  # packageFamilyName
                                                               _type.HSTRING,  # correlationVector
                                                               _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                                              _type.HRESULT]
    SearchForUpdatesWithTelemetryAsync: _Callable[[_type.HSTRING,  # productId
                                                   _type.HSTRING,  # skuId
                                                   _type.HSTRING,  # catalogId
                                                   _type.HSTRING,  # correlationVector
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                                  _type.HRESULT]
    SearchForAllUpdatesWithTelemetryAsync: _Callable[[_type.HSTRING,  # correlationVector
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                                     _type.HRESULT]
    GetIsAppAllowedToInstallWithTelemetryAsync: _Callable[[_type.HSTRING,  # productId
                                                           _type.HSTRING,  # skuId
                                                           _type.HSTRING,  # catalogId
                                                           _type.HSTRING,  # correlationVector
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                          _type.HRESULT]
    CancelWithTelemetry: _Callable[[_type.HSTRING,  # productId
                                    _type.HSTRING],  # correlationVector
                                   _type.HRESULT]
    PauseWithTelemetry: _Callable[[_type.HSTRING,  # productId
                                   _type.HSTRING],  # correlationVector
                                  _type.HRESULT]
    RestartWithTelemetry: _Callable[[_type.HSTRING,  # productId
                                     _type.HSTRING],  # correlationVector
                                    _type.HRESULT]


class IAppInstallManager3(_inspectable.IInspectable):
    StartProductInstallAsync: _Callable[[_type.HSTRING,  # productId
                                         _type.HSTRING,  # catalogId
                                         _type.HSTRING,  # flightId
                                         _type.HSTRING,  # clientId
                                         _type.boolean,  # repair
                                         _type.boolean,  # forceUseOfNonRemovableStorage
                                         _type.HSTRING,  # correlationVector
                                         _Windows_Management_Deployment.IPackageVolume,  # targetVolume
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                        _type.HRESULT]
    StartProductInstallForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                _type.HSTRING,  # productId
                                                _type.HSTRING,  # catalogId
                                                _type.HSTRING,  # flightId
                                                _type.HSTRING,  # clientId
                                                _type.boolean,  # repair
                                                _type.boolean,  # forceUseOfNonRemovableStorage
                                                _type.HSTRING,  # correlationVector
                                                _Windows_Management_Deployment.IPackageVolume,  # targetVolume
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                               _type.HRESULT]
    UpdateAppByPackageFamilyNameForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                         _type.HSTRING,  # packageFamilyName
                                                         _type.HSTRING,  # correlationVector
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                                        _type.HRESULT]
    SearchForUpdatesForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                             _type.HSTRING,  # productId
                                             _type.HSTRING,  # skuId
                                             _type.HSTRING,  # catalogId
                                             _type.HSTRING,  # correlationVector
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                            _type.HRESULT]
    SearchForAllUpdatesForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                _type.HSTRING,  # correlationVector
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                               _type.HRESULT]
    GetIsAppAllowedToInstallForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                     _type.HSTRING,  # productId
                                                     _type.HSTRING,  # skuId
                                                     _type.HSTRING,  # catalogId
                                                     _type.HSTRING,  # correlationVector
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                    _type.HRESULT]
    GetIsApplicableForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                            _type.HSTRING,  # productId
                                            _type.HSTRING,  # skuId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]
    MoveToFrontOfDownloadQueue: _Callable[[_type.HSTRING,  # productId
                                           _type.HSTRING],  # correlationVector
                                          _type.HRESULT]


class IAppInstallManager4(_inspectable.IInspectable):
    GetFreeUserEntitlementAsync: _Callable[[_type.HSTRING,  # storeId
                                            _type.HSTRING,  # campaignId
                                            _type.HSTRING,  # correlationVector
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IGetEntitlementResult]]],  # ppAsyncOperation
                                           _type.HRESULT]
    GetFreeUserEntitlementForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                   _type.HSTRING,  # storeId
                                                   _type.HSTRING,  # campaignId
                                                   _type.HSTRING,  # correlationVector
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IGetEntitlementResult]]],  # ppAsyncOperation
                                                  _type.HRESULT]
    GetFreeDeviceEntitlementAsync: _Callable[[_type.HSTRING,  # storeId
                                              _type.HSTRING,  # campaignId
                                              _type.HSTRING,  # correlationVector
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IGetEntitlementResult]]],  # ppAsyncOperation
                                             _type.HRESULT]


class IAppInstallManager5(_inspectable.IInspectable):
    get_AppInstallItemsWithGroupSupport: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]],  # value
                                                   _type.HRESULT]


class IAppInstallManager6(_inspectable.IInspectable):
    SearchForAllUpdatesWithUpdateOptionsAsync: _Callable[[_type.HSTRING,  # correlationVector
                                                          _type.HSTRING,  # clientId
                                                          IAppUpdateOptions,  # updateOptions
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                                         _type.HRESULT]
    SearchForAllUpdatesWithUpdateOptionsForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                                 _type.HSTRING,  # correlationVector
                                                                 _type.HSTRING,  # clientId
                                                                 IAppUpdateOptions,  # updateOptions
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                                                _type.HRESULT]
    SearchForUpdatesWithUpdateOptionsAsync: _Callable[[_type.HSTRING,  # productId
                                                       _type.HSTRING,  # skuId
                                                       _type.HSTRING,  # correlationVector
                                                       _type.HSTRING,  # clientId
                                                       IAppUpdateOptions,  # updateOptions
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                                      _type.HRESULT]
    SearchForUpdatesWithUpdateOptionsForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                              _type.HSTRING,  # productId
                                                              _type.HSTRING,  # skuId
                                                              _type.HSTRING,  # correlationVector
                                                              _type.HSTRING,  # clientId
                                                              IAppUpdateOptions,  # updateOptions
                                                              _Pointer[_Windows_Foundation.IAsyncOperation[IAppInstallItem]]],  # operation
                                                             _type.HRESULT]
    StartProductInstallWithOptionsAsync: _Callable[[_type.HSTRING,  # productId
                                                    _type.HSTRING,  # flightId
                                                    _type.HSTRING,  # clientId
                                                    _type.HSTRING,  # correlationVector
                                                    IAppInstallOptions,  # installOptions
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                                   _type.HRESULT]
    StartProductInstallWithOptionsForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                           _type.HSTRING,  # productId
                                                           _type.HSTRING,  # flightId
                                                           _type.HSTRING,  # clientId
                                                           _type.HSTRING,  # correlationVector
                                                           IAppInstallOptions,  # installOptions
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppInstallItem]]]],  # operation
                                                          _type.HRESULT]
    GetIsPackageIdentityAllowedToInstallAsync: _Callable[[_type.HSTRING,  # correlationVector
                                                          _type.HSTRING,  # packageIdentityName
                                                          _type.HSTRING,  # publisherCertificateName
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                         _type.HRESULT]
    GetIsPackageIdentityAllowedToInstallForUserAsync: _Callable[[_Windows_System.IUser,  # user
                                                                 _type.HSTRING,  # correlationVector
                                                                 _type.HSTRING,  # packageIdentityName
                                                                 _type.HSTRING,  # publisherCertificateName
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                                _type.HRESULT]


class IAppInstallManager7(_inspectable.IInspectable):
    get_CanInstallForAllUsers: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class IAppInstallManagerItemEventArgs(_inspectable.IInspectable):
    get_Item: _Callable[[_Pointer[IAppInstallItem]],  # value
                        _type.HRESULT]


class IAppInstallOptions(_inspectable.IInspectable):
    get_CatalogId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_CatalogId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_ForceUseOfNonRemovableStorage: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_ForceUseOfNonRemovableStorage: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_AllowForcedAppRestart: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_AllowForcedAppRestart: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_Repair: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Repair: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_TargetVolume: _Callable[[_Pointer[_Windows_Management_Deployment.IPackageVolume]],  # value
                                _type.HRESULT]
    put_TargetVolume: _Callable[[_Windows_Management_Deployment.IPackageVolume],  # value
                                _type.HRESULT]
    get_LaunchAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_LaunchAfterInstall: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class IAppInstallOptions2(_inspectable.IInspectable):
    get_PinToDesktopAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_PinToDesktopAfterInstall: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_PinToStartAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_PinToStartAfterInstall: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_PinToTaskbarAfterInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_PinToTaskbarAfterInstall: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_CompletedInstallToastNotificationMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode]],  # value
                                                         _type.HRESULT]
    put_CompletedInstallToastNotificationMode: _Callable[[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode],  # value
                                                         _type.HRESULT]
    get_InstallInProgressToastNotificationMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode]],  # value
                                                          _type.HRESULT]
    put_InstallInProgressToastNotificationMode: _Callable[[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallationToastNotificationMode],  # value
                                                          _type.HRESULT]
    get_InstallForAllUsers: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_InstallForAllUsers: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_StageButDoNotInstall: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_StageButDoNotInstall: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_CampaignId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_CampaignId: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_ExtendedCampaignId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_ExtendedCampaignId: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]


class IAppInstallStatus(_inspectable.IInspectable):
    get_InstallState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.AppInstallState]],  # value
                                _type.HRESULT]
    get_DownloadSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_BytesDownloaded: _Callable[[_Pointer[_type.UINT64]],  # value
                                   _type.HRESULT]
    get_PercentComplete: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]


class IAppInstallStatus2(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    get_ReadyForLaunch: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]


class IAppInstallStatus3(_inspectable.IInspectable):
    get_IsStaged: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]


class IAppUpdateOptions(_inspectable.IInspectable):
    get_CatalogId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_CatalogId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_AllowForcedAppRestart: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_AllowForcedAppRestart: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IAppUpdateOptions2(_inspectable.IInspectable):
    get_AutomaticallyDownloadAndInstallUpdateIfFound: _Callable[[_Pointer[_type.boolean]],  # value
                                                                _type.HRESULT]
    put_AutomaticallyDownloadAndInstallUpdateIfFound: _Callable[[_type.boolean],  # value
                                                                _type.HRESULT]


class IGetEntitlementResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.InstallControl.GetEntitlementStatus]],  # value
                          _type.HRESULT]
