from __future__ import annotations as _

from typing import Callable as _Callable

from . import Activation as _Windows_ApplicationModel_Activation
from . import Core as _Windows_ApplicationModel_Core
from .. import Foundation as _Windows_Foundation
from .. import Storage as _Windows_Storage
from .. import System as _Windows_System
from ..Foundation import Collections as _Windows_Foundation_Collections
from ..Storage import Streams as _Windows_Storage_Streams
from ... import inspectable as _inspectable
from ..... import enum as _enum
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class IAppDisplayInfo(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    GetLogo: _Callable[[_struct.Windows.Foundation.Size,  # size
                        _Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                       _type.HRESULT]


class IAppInfo(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_DisplayInfo: _Callable[[_Pointer[IAppDisplayInfo]],  # value
                               _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IAppInfo2(_inspectable.IInspectable):
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]


class IAppInfo3(_inspectable.IInspectable):
    get_ExecutionContext: _Callable[[_Pointer[_enum.Windows.ApplicationModel.AppExecutionContext]],  # value
                                    _type.HRESULT]


class IAppInfo4(_inspectable.IInspectable):
    get_SupportedFileExtensions: _Callable[[_Pointer[_type.UINT32],  # __valueSize
                                            _Pointer[_Pointer[_type.HSTRING]]],  # value
                                           _type.HRESULT]


class IAppInfoStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IAppInfo]],  # value
                           _type.HRESULT]
    GetFromAppUserModelId: _Callable[[_type.HSTRING,  # appUserModelId
                                      _Pointer[IAppInfo]],  # result
                                     _type.HRESULT]
    GetFromAppUserModelIdForUser: _Callable[[_Windows_System.IUser,  # user
                                             _type.HSTRING,  # appUserModelId
                                             _Pointer[IAppInfo]],  # result
                                            _type.HRESULT]


class IAppInstallerInfo(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IAppInstallerInfo2(_inspectable.IInspectable):
    get_OnLaunch: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_HoursBetweenUpdateChecks: _Callable[[_Pointer[_type.UINT32]],  # value
                                            _type.HRESULT]
    get_ShowPrompt: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_UpdateBlocksActivation: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_AutomaticBackgroundTask: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_ForceUpdateFromAnyVersion: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_IsAutoRepairEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_Version: _Callable[[_Pointer[_struct.Windows.ApplicationModel.PackageVersion]],  # value
                           _type.HRESULT]
    get_LastChecked: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    get_PausedUntil: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                               _type.HRESULT]
    get_UpdateUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation.IUriRuntimeClass]]],  # value
                              _type.HRESULT]
    get_RepairUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation.IUriRuntimeClass]]],  # value
                              _type.HRESULT]
    get_DependencyPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                         _type.HRESULT]
    get_OptionalPackageUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Foundation.IUriRuntimeClass]]],  # value
                                       _type.HRESULT]
    get_PolicySource: _Callable[[_Pointer[_enum.Windows.ApplicationModel.AppInstallerPolicySource]],  # value
                                _type.HRESULT]


class IAppInstance(_inspectable.IInspectable):
    get_Key: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_IsCurrentInstance: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    RedirectActivationTo: _Callable[[],
                                    _type.HRESULT]


class IAppInstanceStatics(_inspectable.IInspectable, factory=True):
    get_RecommendedInstance: _Callable[[_Pointer[IAppInstance]],  # value
                                       _type.HRESULT]
    GetActivatedEventArgs: _Callable[[_Pointer[_Windows_ApplicationModel_Activation.IActivatedEventArgs]],  # result
                                     _type.HRESULT]
    FindOrRegisterInstanceForKey: _Callable[[_type.HSTRING,  # key
                                             _Pointer[IAppInstance]],  # result
                                            _type.HRESULT]
    Unregister: _Callable[[],
                          _type.HRESULT]
    GetInstances: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAppInstance]]],  # result
                            _type.HRESULT]


class IDesignModeStatics(_inspectable.IInspectable, factory=True):
    get_DesignModeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IDesignModeStatics2(_inspectable.IInspectable, factory=True):
    get_DesignMode2Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IEnteredBackgroundEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IFindRelatedPackagesOptions(_inspectable.IInspectable):
    get_Relationship: _Callable[[_Pointer[_enum.Windows.ApplicationModel.PackageRelationship]],  # value
                                _type.HRESULT]
    put_Relationship: _Callable[[_enum.Windows.ApplicationModel.PackageRelationship],  # value
                                _type.HRESULT]
    get_IncludeFrameworks: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IncludeFrameworks: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IncludeHostRuntimes: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IncludeHostRuntimes: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IncludeOptionals: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IncludeOptionals: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IncludeResources: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IncludeResources: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IFindRelatedPackagesOptionsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Windows.ApplicationModel.PackageRelationship,  # Relationship
                               _Pointer[IFindRelatedPackagesOptions]],  # value
                              _type.HRESULT]


class IFullTrustProcessLaunchResult(_inspectable.IInspectable):
    get_LaunchResult: _Callable[[_Pointer[_enum.Windows.ApplicationModel.FullTrustLaunchResult]],  # value
                                _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IFullTrustProcessLauncherStatics(_inspectable.IInspectable, factory=True):
    LaunchFullTrustProcessForCurrentAppAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                                        _type.HRESULT]
    LaunchFullTrustProcessForCurrentAppWithParametersAsync: _Callable[[_type.HSTRING,  # parameterGroupId
                                                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                                                      _type.HRESULT]
    LaunchFullTrustProcessForAppAsync: _Callable[[_type.HSTRING,  # fullTrustPackageRelativeAppId
                                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                                 _type.HRESULT]
    LaunchFullTrustProcessForAppWithParametersAsync: _Callable[[_type.HSTRING,  # fullTrustPackageRelativeAppId
                                                                _type.HSTRING,  # parameterGroupId
                                                                _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                                               _type.HRESULT]


class IFullTrustProcessLauncherStatics2(_inspectable.IInspectable, factory=True):
    LaunchFullTrustProcessForCurrentAppWithArgumentsAsync: _Callable[[_type.HSTRING,  # commandLine
                                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IFullTrustProcessLaunchResult]]],  # operation
                                                                     _type.HRESULT]
    LaunchFullTrustProcessForAppWithArgumentsAsync: _Callable[[_type.HSTRING,  # fullTrustPackageRelativeAppId
                                                               _type.HSTRING,  # commandLine
                                                               _Pointer[_Windows_Foundation.IAsyncOperation[IFullTrustProcessLaunchResult]]],  # operation
                                                              _type.HRESULT]


class ILeavingBackgroundEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ILimitedAccessFeatureRequestResult(_inspectable.IInspectable):
    get_FeatureId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.LimitedAccessFeatureStatus]],  # value
                          _type.HRESULT]
    get_EstimatedRemovalDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                        _type.HRESULT]


class ILimitedAccessFeaturesStatics(_inspectable.IInspectable, factory=True):
    TryUnlockFeature: _Callable[[_type.HSTRING,  # featureId
                                 _type.HSTRING,  # token
                                 _type.HSTRING,  # attestation
                                 _Pointer[ILimitedAccessFeatureRequestResult]],  # result
                                _type.HRESULT]


class IPackage(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[IPackageId]],  # value
                      _type.HRESULT]
    get_InstalledLocation: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                     _type.HRESULT]
    get_IsFramework: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_Dependencies: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPackage]]],  # value
                                _type.HRESULT]


class IPackage2(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PublisherDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Logo: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                        _type.HRESULT]
    get_IsResourcePackage: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    get_IsBundle: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsDevelopmentMode: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IPackage3(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[IPackageStatus]],  # value
                          _type.HRESULT]
    get_InstalledDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                 _type.HRESULT]
    GetAppListEntriesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Core.IAppListEntry]]]],  # operation
                                      _type.HRESULT]


class IPackage4(_inspectable.IInspectable):
    get_SignatureKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.PackageSignatureKind]],  # value
                                 _type.HRESULT]
    get_IsOptional: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    VerifyContentIntegrityAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                           _type.HRESULT]


class IPackage5(_inspectable.IInspectable):
    GetContentGroupsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IPackageContentGroup]]]],  # operation
                                     _type.HRESULT]
    GetContentGroupAsync: _Callable[[_type.HSTRING,  # name
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IPackageContentGroup]]],  # operation
                                    _type.HRESULT]
    StageContentGroupsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # names
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IPackageContentGroup]]]],  # operation
                                       _type.HRESULT]
    StageContentGroupsWithPriorityAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # names
                                                    _type.boolean,  # moveToHeadOfQueue
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IPackageContentGroup]]]],  # operation
                                                   _type.HRESULT]
    SetInUseAsync: _Callable[[_type.boolean,  # inUse
                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                             _type.HRESULT]


class IPackage6(_inspectable.IInspectable):
    GetAppInstallerInfo: _Callable[[_Pointer[IAppInstallerInfo]],  # value
                                   _type.HRESULT]
    CheckUpdateAvailabilityAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPackageUpdateAvailabilityResult]]],  # operation
                                            _type.HRESULT]


class IPackage7(_inspectable.IInspectable):
    get_MutableLocation: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                   _type.HRESULT]
    get_EffectiveLocation: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                     _type.HRESULT]


class IPackage8(_inspectable.IInspectable):
    get_EffectiveExternalLocation: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                             _type.HRESULT]
    get_MachineExternalLocation: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                           _type.HRESULT]
    get_UserExternalLocation: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                                        _type.HRESULT]
    get_InstalledPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_MutablePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_EffectivePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_EffectiveExternalPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_MachineExternalPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_UserExternalPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    GetLogoAsRandomAccessStreamReference: _Callable[[_struct.Windows.Foundation.Size,  # size
                                                     _Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # result
                                                    _type.HRESULT]
    GetAppListEntries: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Core.IAppListEntry]]],  # result
                                 _type.HRESULT]
    get_IsStub: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]


class IPackage9(_inspectable.IInspectable):
    FindRelatedPackages: _Callable[[IFindRelatedPackagesOptions,  # options
                                    _Pointer[_Windows_Foundation_Collections.IVector[IPackage]]],  # result
                                   _type.HRESULT]
    get_SourceUriSchemeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IPackageCatalog(_inspectable.IInspectable):
    add_PackageStaging: _Callable[[_Windows_Foundation.ITypedEventHandler[IPackageCatalog, IPackageStagingEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PackageStaging: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PackageInstalling: _Callable[[_Windows_Foundation.ITypedEventHandler[IPackageCatalog, IPackageInstallingEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_PackageInstalling: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_PackageUpdating: _Callable[[_Windows_Foundation.ITypedEventHandler[IPackageCatalog, IPackageUpdatingEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PackageUpdating: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_PackageUninstalling: _Callable[[_Windows_Foundation.ITypedEventHandler[IPackageCatalog, IPackageUninstallingEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PackageUninstalling: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_PackageStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IPackageCatalog, IPackageStatusChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_PackageStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IPackageCatalog2(_inspectable.IInspectable):
    add_PackageContentGroupStaging: _Callable[[_Windows_Foundation.ITypedEventHandler[IPackageCatalog, IPackageContentGroupStagingEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_PackageContentGroupStaging: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    AddOptionalPackageAsync: _Callable[[_type.HSTRING,  # optionalPackageFamilyName
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IPackageCatalogAddOptionalPackageResult]]],  # operation
                                       _type.HRESULT]


class IPackageCatalog3(_inspectable.IInspectable):
    RemoveOptionalPackagesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # optionalPackageFamilyNames
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IPackageCatalogRemoveOptionalPackagesResult]]],  # operation
                                           _type.HRESULT]


class IPackageCatalog4(_inspectable.IInspectable):
    AddResourcePackageAsync: _Callable[[_type.HSTRING,  # resourcePackageFamilyName
                                        _type.HSTRING,  # resourceID
                                        _enum.Windows.ApplicationModel.AddResourcePackageOptions,  # options
                                        _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IPackageCatalogAddResourcePackageResult, _struct.Windows.ApplicationModel.PackageInstallProgress]]],  # operation
                                       _type.HRESULT]
    RemoveResourcePackagesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IPackage],  # resourcePackages
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IPackageCatalogRemoveResourcePackagesResult]]],  # operation
                                           _type.HRESULT]


class IPackageCatalogAddOptionalPackageResult(_inspectable.IInspectable):
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IPackageCatalogAddResourcePackageResult(_inspectable.IInspectable):
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]
    get_IsComplete: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IPackageCatalogRemoveOptionalPackagesResult(_inspectable.IInspectable):
    get_PackagesRemoved: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPackage]]],  # value
                                   _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IPackageCatalogRemoveResourcePackagesResult(_inspectable.IInspectable):
    get_PackagesRemoved: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IPackage]]],  # value
                                   _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IPackageCatalogStatics(_inspectable.IInspectable, factory=True):
    OpenForCurrentPackage: _Callable[[_Pointer[IPackageCatalog]],  # value
                                     _type.HRESULT]
    OpenForCurrentUser: _Callable[[_Pointer[IPackageCatalog]],  # value
                                  _type.HRESULT]


class IPackageCatalogStatics2(_inspectable.IInspectable, factory=True):
    OpenForPackage: _Callable[[IPackage,  # package
                               _Pointer[IPackageCatalog]],  # result
                              _type.HRESULT]


class IPackageContentGroup(_inspectable.IInspectable):
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.ApplicationModel.PackageContentGroupState]],  # value
                         _type.HRESULT]
    get_IsRequired: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IPackageContentGroupStagingEventArgs(_inspectable.IInspectable):
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_IsComplete: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]
    get_ContentGroupName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_IsContentGroupRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IPackageContentGroupStatics(_inspectable.IInspectable, factory=True):
    get_RequiredGroupName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IPackageId(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Version: _Callable[[_Pointer[_struct.Windows.ApplicationModel.PackageVersion]],  # value
                           _type.HRESULT]
    get_Architecture: _Callable[[_Pointer[_enum.Windows.System.ProcessorArchitecture]],  # value
                                _type.HRESULT]
    get_ResourceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Publisher: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_PublisherId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_FullName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_FamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IPackageIdWithMetadata(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Author: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IPackageInstallingEventArgs(_inspectable.IInspectable):
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_IsComplete: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]


class IPackageStagingEventArgs(_inspectable.IInspectable):
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_IsComplete: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]


class IPackageStatics(_inspectable.IInspectable, factory=True):
    get_Current: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]


class IPackageStatus(_inspectable.IInspectable):
    VerifyIsOK: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    get_NotAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_PackageOffline: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_DataOffline: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_Disabled: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_NeedsRemediation: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    get_LicenseIssue: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_Modified: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_Tampered: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_DependencyIssue: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_Servicing: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_DeploymentInProgress: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]


class IPackageStatus2(_inspectable.IInspectable):
    get_IsPartiallyStaged: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IPackageStatusChangedEventArgs(_inspectable.IInspectable):
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]


class IPackageUninstallingEventArgs(_inspectable.IInspectable):
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_Package: _Callable[[_Pointer[IPackage]],  # value
                           _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_IsComplete: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]


class IPackageUpdateAvailabilityResult(_inspectable.IInspectable):
    get_Availability: _Callable[[_Pointer[_enum.Windows.ApplicationModel.PackageUpdateAvailability]],  # value
                                _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IPackageUpdatingEventArgs(_inspectable.IInspectable):
    get_ActivityId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_SourcePackage: _Callable[[_Pointer[IPackage]],  # value
                                 _type.HRESULT]
    get_TargetPackage: _Callable[[_Pointer[IPackage]],  # value
                                 _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    get_IsComplete: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]


class IPackageWithMetadata(_inspectable.IInspectable):
    get_InstallDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    GetThumbnailToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    Launch: _Callable[[_type.HSTRING],  # parameters
                      _type.HRESULT]


class IStartupTask(_inspectable.IInspectable):
    RequestEnableAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.StartupTaskState]]],  # operation
                                  _type.HRESULT]
    Disable: _Callable[[],
                       _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.ApplicationModel.StartupTaskState]],  # value
                         _type.HRESULT]
    get_TaskId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IStartupTaskStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentPackageAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStartupTask]]]],  # operation
                                         _type.HRESULT]
    GetAsync: _Callable[[_type.HSTRING,  # taskId
                         _Pointer[_Windows_Foundation.IAsyncOperation[IStartupTask]]],  # operation
                        _type.HRESULT]


class ISuspendingDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class ISuspendingEventArgs(_inspectable.IInspectable):
    get_SuspendingOperation: _Callable[[_Pointer[ISuspendingOperation]],  # value
                                       _type.HRESULT]


class ISuspendingOperation(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[ISuspendingDeferral]],  # deferral
                           _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
