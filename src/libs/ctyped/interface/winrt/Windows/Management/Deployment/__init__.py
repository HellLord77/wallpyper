from __future__ import annotations

from typing import Callable as _Callable

from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAddPackageOptions(_inspectable.IInspectable):
    get_DependencyPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                         _type.HRESULT]
    get_TargetVolume: _Callable[[_Pointer[IPackageVolume]],  # value
                                _type.HRESULT]
    put_TargetVolume: _Callable[[IPackageVolume],  # value
                                _type.HRESULT]
    get_OptionalPackageFamilyNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                              _type.HRESULT]
    get_OptionalPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                       _type.HRESULT]
    get_RelatedPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                      _type.HRESULT]
    get_ExternalLocationUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                       _type.HRESULT]
    put_ExternalLocationUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                       _type.HRESULT]
    get_StubPackageOption: _Callable[[_Pointer[_enum.Windows.Management.Deployment.StubPackageOption]],  # value
                                     _type.HRESULT]
    put_StubPackageOption: _Callable[[_enum.Windows.Management.Deployment.StubPackageOption],  # value
                                     _type.HRESULT]
    get_DeveloperMode: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_DeveloperMode: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_ForceAppShutdown: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ForceAppShutdown: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ForceTargetAppShutdown: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_ForceTargetAppShutdown: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_ForceUpdateFromAnyVersion: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_ForceUpdateFromAnyVersion: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_InstallAllResources: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_InstallAllResources: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_RequiredContentGroupOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_RequiredContentGroupOnly: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_RetainFilesOnFailure: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_RetainFilesOnFailure: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_StageInPlace: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_StageInPlace: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_AllowUnsigned: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AllowUnsigned: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_DeferRegistrationWhenPackagesAreInUse: _Callable[[_Pointer[_type.boolean]],  # value
                                                         _type.HRESULT]
    put_DeferRegistrationWhenPackagesAreInUse: _Callable[[_type.boolean],  # value
                                                         _type.HRESULT]


class IAddPackageOptions2(_inspectable.IInspectable):
    get_ExpectedDigests: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_Windows_Foundation.IUriRuntimeClass, _type.HSTRING]]],  # value
                                   _type.HRESULT]
    get_LimitToExistingPackages: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_LimitToExistingPackages: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]


class IAppInstallerManager(_inspectable.IInspectable):
    SetAutoUpdateSettings: _Callable[[_type.HSTRING,  # packageFamilyName
                                      IAutoUpdateSettingsOptions],  # appInstallerInfo
                                     _type.HRESULT]
    ClearAutoUpdateSettings: _Callable[[_type.HSTRING],  # packageFamilyName
                                       _type.HRESULT]
    PauseAutoUpdatesUntil: _Callable[[_type.HSTRING,  # packageFamilyName
                                      _struct.Windows.Foundation.DateTime],  # dateTime
                                     _type.HRESULT]


class IAppInstallerManagerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IAppInstallerManager]],  # result
                          _type.HRESULT]
    GetForSystem: _Callable[[_Pointer[IAppInstallerManager]],  # result
                            _type.HRESULT]

    _factory = True


class IAutoUpdateSettingsOptions(_inspectable.IInspectable):
    get_Version: _Callable[[_Pointer[_struct.Windows.ApplicationModel.PackageVersion]],  # value
                           _type.HRESULT]
    put_Version: _Callable[[_struct.Windows.ApplicationModel.PackageVersion],  # value
                           _type.HRESULT]
    get_AppInstallerUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                   _type.HRESULT]
    put_AppInstallerUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                   _type.HRESULT]
    get_OnLaunch: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_OnLaunch: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_HoursBetweenUpdateChecks: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]
    put_HoursBetweenUpdateChecks: _Callable[[_type.UINT32],  # value
                                            _type.HRESULT]
    get_ShowPrompt: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_ShowPrompt: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_UpdateBlocksActivation: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_UpdateBlocksActivation: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_AutomaticBackgroundTask: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_AutomaticBackgroundTask: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_ForceUpdateFromAnyVersion: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_ForceUpdateFromAnyVersion: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsAutoRepairEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsAutoRepairEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_UpdateUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                              _type.HRESULT]
    get_RepairUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                              _type.HRESULT]
    get_DependencyPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                         _type.HRESULT]
    get_OptionalPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                       _type.HRESULT]


class IAutoUpdateSettingsOptionsStatics(_inspectable.IInspectable):
    CreateFromAppInstallerInfo: _Callable[[_Windows_ApplicationModel.IAppInstallerInfo,  # appInstallerInfo
                                           _Pointer[IAutoUpdateSettingsOptions]],  # result
                                          _type.HRESULT]

    _factory = True


class ICreateSharedPackageContainerOptions(_inspectable.IInspectable):
    get_Members: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISharedPackageContainerMember]]],  # value
                           _type.HRESULT]
    get_ForceAppShutdown: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ForceAppShutdown: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_CreateCollisionOption: _Callable[[_Pointer[_enum.Windows.Management.Deployment.SharedPackageContainerCreationCollisionOptions]],  # value
                                         _type.HRESULT]
    put_CreateCollisionOption: _Callable[[_enum.Windows.Management.Deployment.SharedPackageContainerCreationCollisionOptions],  # value
                                         _type.HRESULT]


class ICreateSharedPackageContainerResult(_inspectable.IInspectable):
    get_Container: _Callable[[_Pointer[ISharedPackageContainer]],  # value
                             _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Management.Deployment.SharedPackageContainerOperationStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IDeleteSharedPackageContainerOptions(_inspectable.IInspectable):
    get_ForceAppShutdown: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ForceAppShutdown: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_AllUsers: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_AllUsers: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class IDeleteSharedPackageContainerResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Management.Deployment.SharedPackageContainerOperationStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IDeploymentResult(_inspectable.IInspectable):
    get_ErrorText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_ExtendedErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                                     _type.HRESULT]


class IDeploymentResult2(_inspectable.IInspectable):
    get_IsRegistered: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IFindSharedPackageContainerOptions(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_PackageFamilyName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]


class IPackageAllUserProvisioningOptions(_inspectable.IInspectable):
    get_OptionalPackageFamilyNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                              _type.HRESULT]
    get_ProjectionOrderPackageFamilyNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                                     _type.HRESULT]


class IPackageManager(_inspectable.IInspectable):
    AddPackageAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                               _type.HRESULT]
    UpdatePackageAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                   _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                   _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                  _type.HRESULT]
    RemovePackageAsync: _Callable[[_type.HSTRING,  # packageFullName
                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                  _type.HRESULT]
    StagePackageAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                  _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                 _type.HRESULT]
    RegisterPackageAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # manifestUri
                                     _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                     _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                     _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                    _type.HRESULT]
    FindPackages: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                            _type.HRESULT]
    FindPackagesByUserSecurityId: _Callable[[_type.HSTRING,  # userSecurityId
                                             _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                            _type.HRESULT]
    FindPackagesByNamePublisher: _Callable[[_type.HSTRING,  # packageName
                                            _type.HSTRING,  # packagePublisher
                                            _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                           _type.HRESULT]
    FindPackagesByUserSecurityIdNamePublisher: _Callable[[_type.HSTRING,  # userSecurityId
                                                          _type.HSTRING,  # packageName
                                                          _type.HSTRING,  # packagePublisher
                                                          _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                         _type.HRESULT]
    FindUsers: _Callable[[_type.HSTRING,  # packageFullName
                          _Pointer[_Windows_Foundation_Collections.IIterable[IPackageUserInformation]]],  # users
                         _type.HRESULT]
    SetPackageState: _Callable[[_type.HSTRING,  # packageFullName
                                _enum.Windows.Management.Deployment.PackageState],  # packageState
                               _type.HRESULT]
    FindPackageByPackageFullName: _Callable[[_type.HSTRING,  # packageFullName
                                             _Pointer[_Windows_ApplicationModel.IPackage]],  # packageInformation
                                            _type.HRESULT]
    CleanupPackageForUserAsync: _Callable[[_type.HSTRING,  # packageName
                                           _type.HSTRING,  # userSecurityId
                                           _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                          _type.HRESULT]
    FindPackagesByPackageFamilyName: _Callable[[_type.HSTRING,  # packageFamilyName
                                                _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                               _type.HRESULT]
    FindPackagesByUserSecurityIdPackageFamilyName: _Callable[[_type.HSTRING,  # userSecurityId
                                                              _type.HSTRING,  # packageFamilyName
                                                              _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                             _type.HRESULT]
    FindPackageByUserSecurityIdPackageFullName: _Callable[[_type.HSTRING,  # userSecurityId
                                                           _type.HSTRING,  # packageFullName
                                                           _Pointer[_Windows_ApplicationModel.IPackage]],  # packageInformation
                                                          _type.HRESULT]


class IPackageManager10(_inspectable.IInspectable):
    ProvisionPackageForAllUsersWithOptionsAsync: _Callable[[_type.HSTRING,  # mainPackageFamilyName
                                                            IPackageAllUserProvisioningOptions,  # options
                                                            _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                           _type.HRESULT]


class IPackageManager2(_inspectable.IInspectable):
    RemovePackageWithOptionsAsync: _Callable[[_type.HSTRING,  # packageFullName
                                              _enum.Windows.Management.Deployment.RemovalOptions,  # removalOptions
                                              _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                             _type.HRESULT]
    StagePackageWithOptionsAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                             _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                             _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                             _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                            _type.HRESULT]
    RegisterPackageByFullNameAsync: _Callable[[_type.HSTRING,  # mainPackageFullName
                                               _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # dependencyPackageFullNames
                                               _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                               _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                              _type.HRESULT]
    FindPackagesWithPackageTypes: _Callable[[_enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                             _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                            _type.HRESULT]
    FindPackagesByUserSecurityIdWithPackageTypes: _Callable[[_type.HSTRING,  # userSecurityId
                                                             _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                             _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                            _type.HRESULT]
    FindPackagesByNamePublisherWithPackageTypes: _Callable[[_type.HSTRING,  # packageName
                                                            _type.HSTRING,  # packagePublisher
                                                            _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                            _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                           _type.HRESULT]
    FindPackagesByUserSecurityIdNamePublisherWithPackageTypes: _Callable[[_type.HSTRING,  # userSecurityId
                                                                          _type.HSTRING,  # packageName
                                                                          _type.HSTRING,  # packagePublisher
                                                                          _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                                          _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                                         _type.HRESULT]
    FindPackagesByPackageFamilyNameWithPackageTypes: _Callable[[_type.HSTRING,  # packageFamilyName
                                                                _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                                _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                               _type.HRESULT]
    FindPackagesByUserSecurityIdPackageFamilyNameWithPackageTypes: _Callable[[_type.HSTRING,  # userSecurityId
                                                                              _type.HSTRING,  # packageFamilyName
                                                                              _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                                              _Pointer[_Windows_Foundation_Collections.IIterable[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                                             _type.HRESULT]
    StageUserDataAsync: _Callable[[_type.HSTRING,  # packageFullName
                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                  _type.HRESULT]


class IPackageManager3(_inspectable.IInspectable):
    AddPackageVolumeAsync: _Callable[[_type.HSTRING,  # packageStorePath
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IPackageVolume]]],  # packageVolume
                                     _type.HRESULT]
    AddPackageToVolumeAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                        _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                        _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                        IPackageVolume,  # targetVolume
                                        _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                       _type.HRESULT]
    ClearPackageStatus: _Callable[[_type.HSTRING,  # packageFullName
                                   _enum.Windows.Management.Deployment.PackageStatus],  # status
                                  _type.HRESULT]
    RegisterPackageWithAppDataVolumeAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # manifestUri
                                                      _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                                      _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                                      IPackageVolume,  # appDataVolume
                                                      _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                                     _type.HRESULT]
    FindPackageVolumeByName: _Callable[[_type.HSTRING,  # volumeName
                                        _Pointer[IPackageVolume]],  # volume
                                       _type.HRESULT]
    FindPackageVolumes: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[IPackageVolume]]],  # volumeCollection
                                  _type.HRESULT]
    GetDefaultPackageVolume: _Callable[[_Pointer[IPackageVolume]],  # volume
                                       _type.HRESULT]
    MovePackageToVolumeAsync: _Callable[[_type.HSTRING,  # packageFullName
                                         _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                         IPackageVolume,  # targetVolume
                                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                        _type.HRESULT]
    RemovePackageVolumeAsync: _Callable[[IPackageVolume,  # volume
                                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                        _type.HRESULT]
    SetDefaultPackageVolume: _Callable[[IPackageVolume],  # volume
                                       _type.HRESULT]
    SetPackageStatus: _Callable[[_type.HSTRING,  # packageFullName
                                 _enum.Windows.Management.Deployment.PackageStatus],  # status
                                _type.HRESULT]
    SetPackageVolumeOfflineAsync: _Callable[[IPackageVolume,  # packageVolume
                                             _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                            _type.HRESULT]
    SetPackageVolumeOnlineAsync: _Callable[[IPackageVolume,  # packageVolume
                                            _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                           _type.HRESULT]
    StagePackageToVolumeAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                          _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                          _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                          IPackageVolume,  # targetVolume
                                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                         _type.HRESULT]
    StageUserDataWithOptionsAsync: _Callable[[_type.HSTRING,  # packageFullName
                                              _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                              _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                             _type.HRESULT]


class IPackageManager4(_inspectable.IInspectable):
    GetPackageVolumesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IPackageVolume]]]],  # operation
                                      _type.HRESULT]


class IPackageManager5(_inspectable.IInspectable):
    AddPackageToVolumeAndOptionalPackagesAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                                           _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                                           _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                                           IPackageVolume,  # targetVolume
                                                           _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                                           _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # externalPackageUris
                                                           _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                                          _type.HRESULT]
    StagePackageToVolumeAndOptionalPackagesAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                                             _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                                             _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                                             IPackageVolume,  # targetVolume
                                                             _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                                             _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # externalPackageUris
                                                             _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                                            _type.HRESULT]
    RegisterPackageByFamilyNameAndOptionalPackagesAsync: _Callable[[_type.HSTRING,  # mainPackageFamilyName
                                                                    _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # dependencyPackageFamilyNames
                                                                    _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                                                    IPackageVolume,  # appDataVolume
                                                                    _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                                                   _type.HRESULT]
    get_DebugSettings: _Callable[[_Pointer[IPackageManagerDebugSettings]],  # value
                                 _type.HRESULT]


class IPackageManager6(_inspectable.IInspectable):
    ProvisionPackageForAllUsersAsync: _Callable[[_type.HSTRING,  # packageFamilyName
                                                 _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                _type.HRESULT]
    AddPackageByAppInstallerFileAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # appInstallerFileUri
                                                  _enum.Windows.Management.Deployment.AddPackageByAppInstallerOptions,  # options
                                                  IPackageVolume,  # targetVolume
                                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                 _type.HRESULT]
    RequestAddPackageByAppInstallerFileAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # appInstallerFileUri
                                                         _enum.Windows.Management.Deployment.AddPackageByAppInstallerOptions,  # options
                                                         IPackageVolume,  # targetVolume
                                                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                        _type.HRESULT]
    AddPackageToVolumeAndRelatedSetAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                                     _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                                     _enum.Windows.Management.Deployment.DeploymentOptions,  # options
                                                     IPackageVolume,  # targetVolume
                                                     _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                                     _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # packageUrisToInstall
                                                     _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # relatedPackageUris
                                                     _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                    _type.HRESULT]
    StagePackageToVolumeAndRelatedSetAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                                       _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                                       _enum.Windows.Management.Deployment.DeploymentOptions,  # options
                                                       IPackageVolume,  # targetVolume
                                                       _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                                       _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # packageUrisToInstall
                                                       _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # relatedPackageUris
                                                       _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                      _type.HRESULT]
    RequestAddPackageAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                       _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                       _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                       IPackageVolume,  # targetVolume
                                       _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                       _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # relatedPackageUris
                                       _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                      _type.HRESULT]


class IPackageManager7(_inspectable.IInspectable):
    RequestAddPackageAndRelatedSetAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                                    _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # dependencyPackageUris
                                                    _enum.Windows.Management.Deployment.DeploymentOptions,  # deploymentOptions
                                                    IPackageVolume,  # targetVolume
                                                    _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                                    _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # relatedPackageUris
                                                    _Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # packageUrisToInstall
                                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                   _type.HRESULT]


class IPackageManager8(_inspectable.IInspectable):
    DeprovisionPackageForAllUsersAsync: _Callable[[_type.HSTRING,  # packageFamilyName
                                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # operation
                                                  _type.HRESULT]


class IPackageManager9(_inspectable.IInspectable):
    FindProvisionedPackages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                       _type.HRESULT]
    AddPackageByUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                     IAddPackageOptions,  # options
                                     _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                    _type.HRESULT]
    StagePackageByUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # packageUri
                                       IStagePackageOptions,  # options
                                       _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                      _type.HRESULT]
    RegisterPackageByUriAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # manifestUri
                                          IRegisterPackageOptions,  # options
                                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                         _type.HRESULT]
    RegisterPackagesByFullNameAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # packageFullNames
                                                IRegisterPackageOptions,  # options
                                                _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDeploymentResult, _struct.Windows.Management.Deployment.DeploymentProgress]]],  # deploymentOperation
                                               _type.HRESULT]
    SetPackageStubPreference: _Callable[[_type.HSTRING,  # packageFamilyName
                                         _enum.Windows.Management.Deployment.PackageStubPreference],  # useStub
                                        _type.HRESULT]
    GetPackageStubPreference: _Callable[[_type.HSTRING,  # packageFamilyName
                                         _Pointer[_enum.Windows.Management.Deployment.PackageStubPreference]],  # value
                                        _type.HRESULT]


class IPackageManagerDebugSettings(_inspectable.IInspectable):
    SetContentGroupStateAsync: _Callable[[_Windows_ApplicationModel.IPackage,  # package
                                          _type.HSTRING,  # contentGroupName
                                          _enum.Windows.ApplicationModel.PackageContentGroupState,  # state
                                          _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                         _type.HRESULT]
    SetContentGroupStateWithPercentageAsync: _Callable[[_Windows_ApplicationModel.IPackage,  # package
                                                        _type.HSTRING,  # contentGroupName
                                                        _enum.Windows.ApplicationModel.PackageContentGroupState,  # state
                                                        _type.DOUBLE,  # completionPercentage
                                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                                       _type.HRESULT]


class IPackageUserInformation(_inspectable.IInspectable):
    get_UserSecurityId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_InstallState: _Callable[[_Pointer[_enum.Windows.Management.Deployment.PackageInstallState]],  # value
                                _type.HRESULT]


class IPackageVolume(_inspectable.IInspectable):
    get_IsOffline: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsSystemVolume: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_MountPoint: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_PackageStorePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_SupportsHardLinks: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    FindPackages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                            _type.HRESULT]
    FindPackagesByNamePublisher: _Callable[[_type.HSTRING,  # packageName
                                            _type.HSTRING,  # packagePublisher
                                            _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                           _type.HRESULT]
    FindPackagesByPackageFamilyName: _Callable[[_type.HSTRING,  # packageFamilyName
                                                _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                               _type.HRESULT]
    FindPackagesWithPackageTypes: _Callable[[_enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                             _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                            _type.HRESULT]
    FindPackagesByNamePublisherWithPackagesTypes: _Callable[[_enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                             _type.HSTRING,  # packageName
                                                             _type.HSTRING,  # packagePublisher
                                                             _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                            _type.HRESULT]
    FindPackagesByPackageFamilyNameWithPackageTypes: _Callable[[_enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                                _type.HSTRING,  # packageFamilyName
                                                                _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                               _type.HRESULT]
    FindPackageByPackageFullName: _Callable[[_type.HSTRING,  # packageFullName
                                             _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                            _type.HRESULT]
    FindPackagesByUserSecurityId: _Callable[[_type.HSTRING,  # userSecurityId
                                             _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                            _type.HRESULT]
    FindPackagesByUserSecurityIdNamePublisher: _Callable[[_type.HSTRING,  # userSecurityId
                                                          _type.HSTRING,  # packageName
                                                          _type.HSTRING,  # packagePublisher
                                                          _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                         _type.HRESULT]
    FindPackagesByUserSecurityIdPackageFamilyName: _Callable[[_type.HSTRING,  # userSecurityId
                                                              _type.HSTRING,  # packageFamilyName
                                                              _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                             _type.HRESULT]
    FindPackagesByUserSecurityIdWithPackageTypes: _Callable[[_type.HSTRING,  # userSecurityId
                                                             _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                             _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                            _type.HRESULT]
    FindPackagesByUserSecurityIdNamePublisherWithPackageTypes: _Callable[[_type.HSTRING,  # userSecurityId
                                                                          _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                                          _type.HSTRING,  # packageName
                                                                          _type.HSTRING,  # packagePublisher
                                                                          _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                                         _type.HRESULT]
    FindPackagesByUserSecurityIdPackageFamilyNameWithPackagesTypes: _Callable[[_type.HSTRING,  # userSecurityId
                                                                               _enum.Windows.Management.Deployment.PackageTypes,  # packageTypes
                                                                               _type.HSTRING,  # packageFamilyName
                                                                               _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                                              _type.HRESULT]
    FindPackageByUserSecurityIdPackageFullName: _Callable[[_type.HSTRING,  # userSecurityId
                                                           _type.HSTRING,  # packageFullName
                                                           _Pointer[_Windows_Foundation_Collections.IVector[_Windows_ApplicationModel.IPackage]]],  # packageCollection
                                                          _type.HRESULT]


class IPackageVolume2(_inspectable.IInspectable):
    get_IsFullTrustPackageSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_IsAppxInstallSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    GetAvailableSpaceAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT64]]],  # operation
                                      _type.HRESULT]


class IRegisterPackageOptions(_inspectable.IInspectable):
    get_DependencyPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                         _type.HRESULT]
    get_AppDataVolume: _Callable[[_Pointer[IPackageVolume]],  # value
                                 _type.HRESULT]
    put_AppDataVolume: _Callable[[IPackageVolume],  # value
                                 _type.HRESULT]
    get_OptionalPackageFamilyNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                              _type.HRESULT]
    get_ExternalLocationUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                       _type.HRESULT]
    put_ExternalLocationUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                       _type.HRESULT]
    get_DeveloperMode: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_DeveloperMode: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_ForceAppShutdown: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ForceAppShutdown: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_ForceTargetAppShutdown: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_ForceTargetAppShutdown: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_ForceUpdateFromAnyVersion: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_ForceUpdateFromAnyVersion: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_InstallAllResources: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_InstallAllResources: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_StageInPlace: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_StageInPlace: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_AllowUnsigned: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AllowUnsigned: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_DeferRegistrationWhenPackagesAreInUse: _Callable[[_Pointer[_type.boolean]],  # value
                                                         _type.HRESULT]
    put_DeferRegistrationWhenPackagesAreInUse: _Callable[[_type.boolean],  # value
                                                         _type.HRESULT]


class IRegisterPackageOptions2(_inspectable.IInspectable):
    get_ExpectedDigests: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_Windows_Foundation.IUriRuntimeClass, _type.HSTRING]]],  # value
                                   _type.HRESULT]


class ISharedPackageContainer(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    GetMembers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISharedPackageContainerMember]]],  # result
                          _type.HRESULT]
    RemovePackageFamily: _Callable[[_type.HSTRING,  # packageFamilyName
                                    IUpdateSharedPackageContainerOptions,  # options
                                    _Pointer[IUpdateSharedPackageContainerResult]],  # result
                                   _type.HRESULT]
    ResetData: _Callable[[_Pointer[IUpdateSharedPackageContainerResult]],  # result
                         _type.HRESULT]


class ISharedPackageContainerManager(_inspectable.IInspectable):
    CreateContainer: _Callable[[_type.HSTRING,  # name
                                ICreateSharedPackageContainerOptions,  # options
                                _Pointer[ICreateSharedPackageContainerResult]],  # result
                               _type.HRESULT]
    DeleteContainer: _Callable[[_type.HSTRING,  # id
                                IDeleteSharedPackageContainerOptions,  # options
                                _Pointer[IDeleteSharedPackageContainerResult]],  # result
                               _type.HRESULT]
    GetContainer: _Callable[[_type.HSTRING,  # id
                             _Pointer[ISharedPackageContainer]],  # result
                            _type.HRESULT]
    FindContainers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISharedPackageContainer]]],  # result
                              _type.HRESULT]
    FindContainersWithOptions: _Callable[[IFindSharedPackageContainerOptions,  # options
                                          _Pointer[_Windows_Foundation_Collections.IVector[ISharedPackageContainer]]],  # result
                                         _type.HRESULT]


class ISharedPackageContainerManagerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[ISharedPackageContainerManager]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_type.HSTRING,  # userSid
                           _Pointer[ISharedPackageContainerManager]],  # result
                          _type.HRESULT]
    GetForProvisioning: _Callable[[_Pointer[ISharedPackageContainerManager]],  # result
                                  _type.HRESULT]

    _factory = True


class ISharedPackageContainerMember(_inspectable.IInspectable):
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class ISharedPackageContainerMemberFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.HSTRING,  # packageFamilyName
                               _Pointer[ISharedPackageContainerMember]],  # value
                              _type.HRESULT]

    _factory = True


class IStagePackageOptions(_inspectable.IInspectable):
    get_DependencyPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                         _type.HRESULT]
    get_TargetVolume: _Callable[[_Pointer[IPackageVolume]],  # value
                                _type.HRESULT]
    put_TargetVolume: _Callable[[IPackageVolume],  # value
                                _type.HRESULT]
    get_OptionalPackageFamilyNames: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                              _type.HRESULT]
    get_OptionalPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                       _type.HRESULT]
    get_RelatedPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                      _type.HRESULT]
    get_ExternalLocationUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                       _type.HRESULT]
    put_ExternalLocationUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                       _type.HRESULT]
    get_StubPackageOption: _Callable[[_Pointer[_enum.Windows.Management.Deployment.StubPackageOption]],  # value
                                     _type.HRESULT]
    put_StubPackageOption: _Callable[[_enum.Windows.Management.Deployment.StubPackageOption],  # value
                                     _type.HRESULT]
    get_DeveloperMode: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_DeveloperMode: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_ForceUpdateFromAnyVersion: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_ForceUpdateFromAnyVersion: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_InstallAllResources: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_InstallAllResources: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_RequiredContentGroupOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_RequiredContentGroupOnly: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_StageInPlace: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_StageInPlace: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_AllowUnsigned: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_AllowUnsigned: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class IStagePackageOptions2(_inspectable.IInspectable):
    get_ExpectedDigests: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_Windows_Foundation.IUriRuntimeClass, _type.HSTRING]]],  # value
                                   _type.HRESULT]


class IUpdateSharedPackageContainerOptions(_inspectable.IInspectable):
    get_ForceAppShutdown: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ForceAppShutdown: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_RequirePackagesPresent: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_RequirePackagesPresent: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class IUpdateSharedPackageContainerResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Management.Deployment.SharedPackageContainerOperationStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
