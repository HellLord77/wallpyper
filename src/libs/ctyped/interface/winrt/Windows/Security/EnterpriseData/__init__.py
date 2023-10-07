from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Networking as _Windows_Networking
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBufferProtectUnprotectResult(_inspectable.IInspectable):
    get_Buffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                          _type.HRESULT]
    get_ProtectionInfo: _Callable[[_Pointer[IDataProtectionInfo]],  # value
                                  _type.HRESULT]


class IDataProtectionInfo(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.EnterpriseData.DataProtectionStatus]],  # value
                          _type.HRESULT]
    get_Identity: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IDataProtectionManagerStatics(_inspectable.IInspectable, factory=True):
    ProtectAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                             _type.HSTRING,  # identity
                             _Pointer[_Windows_Foundation.IAsyncOperation[IBufferProtectUnprotectResult]]],  # result
                            _type.HRESULT]
    UnprotectAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # data
                               _Pointer[_Windows_Foundation.IAsyncOperation[IBufferProtectUnprotectResult]]],  # result
                              _type.HRESULT]
    ProtectStreamAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # unprotectedStream
                                   _type.HSTRING,  # identity
                                   _Windows_Storage_Streams.IOutputStream,  # protectedStream
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IDataProtectionInfo]]],  # result
                                  _type.HRESULT]
    UnprotectStreamAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # protectedStream
                                     _Windows_Storage_Streams.IOutputStream,  # unprotectedStream
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IDataProtectionInfo]]],  # result
                                    _type.HRESULT]
    GetProtectionInfoAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # protectedData
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IDataProtectionInfo]]],  # result
                                      _type.HRESULT]
    GetStreamProtectionInfoAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # protectedStream
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IDataProtectionInfo]]],  # result
                                            _type.HRESULT]


class IFileProtectionInfo(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.EnterpriseData.FileProtectionStatus]],  # value
                          _type.HRESULT]
    get_IsRoamable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Identity: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IFileProtectionInfo2(_inspectable.IInspectable):
    get_IsProtectWhileOpenSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]


class IFileProtectionManagerStatics(_inspectable.IInspectable, factory=True):
    ProtectAsync: _Callable[[_Windows_Storage.IStorageItem,  # target
                             _type.HSTRING,  # identity
                             _Pointer[_Windows_Foundation.IAsyncOperation[IFileProtectionInfo]]],  # result
                            _type.HRESULT]
    CopyProtectionAsync: _Callable[[_Windows_Storage.IStorageItem,  # source
                                    _Windows_Storage.IStorageItem,  # target
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                   _type.HRESULT]
    GetProtectionInfoAsync: _Callable[[_Windows_Storage.IStorageItem,  # source
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IFileProtectionInfo]]],  # result
                                      _type.HRESULT]
    SaveFileAsContainerAsync: _Callable[[_Windows_Storage.IStorageFile,  # protectedFile
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IProtectedContainerExportResult]]],  # result
                                        _type.HRESULT]
    LoadFileFromContainerAsync: _Callable[[_Windows_Storage.IStorageFile,  # containerFile
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IProtectedContainerImportResult]]],  # result
                                          _type.HRESULT]
    LoadFileFromContainerWithTargetAsync: _Callable[[_Windows_Storage.IStorageFile,  # containerFile
                                                     _Windows_Storage.IStorageItem,  # target
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[IProtectedContainerImportResult]]],  # result
                                                    _type.HRESULT]
    CreateProtectedAndOpenAsync: _Callable[[_Windows_Storage.IStorageFolder,  # parentFolder
                                            _type.HSTRING,  # desiredName
                                            _type.HSTRING,  # identity
                                            _enum.Windows.Storage.CreationCollisionOption,  # collisionOption
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IProtectedFileCreateResult]]],  # result
                                           _type.HRESULT]


class IFileProtectionManagerStatics2(_inspectable.IInspectable, factory=True):
    IsContainerAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                _type.HRESULT]
    LoadFileFromContainerWithTargetAndNameCollisionOptionAsync: _Callable[[_Windows_Storage.IStorageFile,  # containerFile
                                                                           _Windows_Storage.IStorageItem,  # target
                                                                           _enum.Windows.Storage.NameCollisionOption,  # collisionOption
                                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IProtectedContainerImportResult]]],  # result
                                                                          _type.HRESULT]
    SaveFileAsContainerWithSharingAsync: _Callable[[_Windows_Storage.IStorageFile,  # protectedFile
                                                    _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # sharedWithIdentities
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IProtectedContainerExportResult]]],  # result
                                                   _type.HRESULT]


class IFileProtectionManagerStatics3(_inspectable.IInspectable, factory=True):
    UnprotectAsync: _Callable[[_Windows_Storage.IStorageItem,  # target
                               _Pointer[_Windows_Foundation.IAsyncOperation[IFileProtectionInfo]]],  # result
                              _type.HRESULT]
    UnprotectWithOptionsAsync: _Callable[[_Windows_Storage.IStorageItem,  # target
                                          IFileUnprotectOptions,  # options
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IFileProtectionInfo]]],  # result
                                         _type.HRESULT]


class IFileRevocationManagerStatics(_inspectable.IInspectable, factory=True):
    ProtectAsync: _Callable[[_Windows_Storage.IStorageItem,  # storageItem
                             _type.HSTRING,  # enterpriseIdentity
                             _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.FileProtectionStatus]]],  # result
                            _type.HRESULT]
    CopyProtectionAsync: _Callable[[_Windows_Storage.IStorageItem,  # sourceStorageItem
                                    _Windows_Storage.IStorageItem,  # targetStorageItem
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                   _type.HRESULT]
    Revoke: _Callable[[_type.HSTRING],  # enterpriseIdentity
                      _type.HRESULT]
    GetStatusAsync: _Callable[[_Windows_Storage.IStorageItem,  # storageItem
                               _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.FileProtectionStatus]]],  # result
                              _type.HRESULT]


class IFileUnprotectOptions(_inspectable.IInspectable):
    put_Audit: _Callable[[_type.boolean],  # value
                         _type.HRESULT]
    get_Audit: _Callable[[_Pointer[_type.boolean]],  # value
                         _type.HRESULT]


class IFileUnprotectOptionsFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.boolean,  # audit
                       _Pointer[IFileUnprotectOptions]],  # result
                      _type.HRESULT]


class IProtectedAccessResumedEventArgs(_inspectable.IInspectable):
    get_Identities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]


class IProtectedAccessSuspendingEventArgs(_inspectable.IInspectable):
    get_Identities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IProtectedContainerExportResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.EnterpriseData.ProtectedImportExportStatus]],  # value
                          _type.HRESULT]
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]


class IProtectedContainerImportResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.EnterpriseData.ProtectedImportExportStatus]],  # value
                          _type.HRESULT]
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]


class IProtectedContentRevokedEventArgs(_inspectable.IInspectable):
    get_Identities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                              _type.HRESULT]


class IProtectedFileCreateResult(_inspectable.IInspectable):
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]
    get_Stream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                          _type.HRESULT]
    get_ProtectionInfo: _Callable[[_Pointer[IFileProtectionInfo]],  # value
                                  _type.HRESULT]


class IProtectionPolicyAuditInfo(_inspectable.IInspectable):
    put_Action: _Callable[[_enum.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction],  # value
                          _type.HRESULT]
    get_Action: _Callable[[_Pointer[_enum.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction]],  # value
                          _type.HRESULT]
    put_DataDescription: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_DataDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_SourceDescription: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_SourceDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_TargetDescription: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_TargetDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IProtectionPolicyAuditInfoFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction,  # action
                       _type.HSTRING,  # dataDescription
                       _type.HSTRING,  # sourceDescription
                       _type.HSTRING,  # targetDescription
                       _Pointer[IProtectionPolicyAuditInfo]],  # result
                      _type.HRESULT]
    CreateWithActionAndDataDescription: _Callable[[_enum.Windows.Security.EnterpriseData.ProtectionPolicyAuditAction,  # action
                                                   _type.HSTRING,  # dataDescription
                                                   _Pointer[IProtectionPolicyAuditInfo]],  # result
                                                  _type.HRESULT]


class IProtectionPolicyManager(_inspectable.IInspectable):
    put_Identity: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Identity: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IProtectionPolicyManager2(_inspectable.IInspectable):
    put_ShowEnterpriseIndicator: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_ShowEnterpriseIndicator: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class IProtectionPolicyManagerStatics(_inspectable.IInspectable, factory=True):
    IsIdentityManaged: _Callable[[_type.HSTRING,  # identity
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    TryApplyProcessUIPolicy: _Callable[[_type.HSTRING,  # identity
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    ClearProcessUIPolicy: _Callable[[],
                                    _type.HRESULT]
    CreateCurrentThreadNetworkContext: _Callable[[_type.HSTRING,  # identity
                                                  _Pointer[IThreadNetworkContext]],  # result
                                                 _type.HRESULT]
    GetPrimaryManagedIdentityForNetworkEndpointAsync: _Callable[[_Windows_Networking.IHostName,  # endpointHost
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                                                _type.HRESULT]
    RevokeContent: _Callable[[_type.HSTRING],  # identity
                             _type.HRESULT]
    GetForCurrentView: _Callable[[_Pointer[IProtectionPolicyManager]],  # result
                                 _type.HRESULT]
    add_ProtectedAccessSuspending: _Callable[[_Windows_Foundation.IEventHandler[IProtectedAccessSuspendingEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_ProtectedAccessSuspending: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_ProtectedAccessResumed: _Callable[[_Windows_Foundation.IEventHandler[IProtectedAccessResumedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_ProtectedAccessResumed: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_ProtectedContentRevoked: _Callable[[_Windows_Foundation.IEventHandler[IProtectedContentRevokedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ProtectedContentRevoked: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    CheckAccess: _Callable[[_type.HSTRING,  # sourceIdentity
                            _type.HSTRING,  # targetIdentity
                            _Pointer[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]],  # result
                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                   _type.HSTRING,  # targetIdentity
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                  _type.HRESULT]


class IProtectionPolicyManagerStatics2(_inspectable.IInspectable, factory=True):
    HasContentBeenRevokedSince: _Callable[[_type.HSTRING,  # identity
                                           _struct.Windows.Foundation.DateTime,  # since
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]
    CheckAccessForApp: _Callable[[_type.HSTRING,  # sourceIdentity
                                  _type.HSTRING,  # appPackageFamilyName
                                  _Pointer[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]],  # result
                                 _type.HRESULT]
    RequestAccessForAppAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                         _type.HSTRING,  # appPackageFamilyName
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                        _type.HRESULT]
    GetEnforcementLevel: _Callable[[_type.HSTRING,  # identity
                                    _Pointer[_enum.Windows.Security.EnterpriseData.EnforcementLevel]],  # value
                                   _type.HRESULT]
    IsUserDecryptionAllowed: _Callable[[_type.HSTRING,  # identity
                                        _Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    IsProtectionUnderLockRequired: _Callable[[_type.HSTRING,  # identity
                                              _Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    add_PolicyChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_PolicyChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    get_IsProtectionEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]


class IProtectionPolicyManagerStatics3(_inspectable.IInspectable, factory=True):
    RequestAccessWithAuditingInfoAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                                   _type.HSTRING,  # targetIdentity
                                                   IProtectionPolicyAuditInfo,  # auditInfo
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                                  _type.HRESULT]
    RequestAccessWithMessageAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                              _type.HSTRING,  # targetIdentity
                                              IProtectionPolicyAuditInfo,  # auditInfo
                                              _type.HSTRING,  # messageFromApp
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                             _type.HRESULT]
    RequestAccessForAppWithAuditingInfoAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                                         _type.HSTRING,  # appPackageFamilyName
                                                         IProtectionPolicyAuditInfo,  # auditInfo
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                                        _type.HRESULT]
    RequestAccessForAppWithMessageAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                                    _type.HSTRING,  # appPackageFamilyName
                                                    IProtectionPolicyAuditInfo,  # auditInfo
                                                    _type.HSTRING,  # messageFromApp
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                                   _type.HRESULT]
    LogAuditEvent: _Callable[[_type.HSTRING,  # sourceIdentity
                              _type.HSTRING,  # targetIdentity
                              IProtectionPolicyAuditInfo],  # auditInfo
                             _type.HRESULT]


class IProtectionPolicyManagerStatics4(_inspectable.IInspectable, factory=True):
    IsRoamableProtectionEnabled: _Callable[[_type.HSTRING,  # identity
                                            _Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    RequestAccessWithBehaviorAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                               _type.HSTRING,  # targetIdentity
                                               IProtectionPolicyAuditInfo,  # auditInfo
                                               _type.HSTRING,  # messageFromApp
                                               _enum.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior,  # behavior
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                              _type.HRESULT]
    RequestAccessForAppWithBehaviorAsync: _Callable[[_type.HSTRING,  # sourceIdentity
                                                     _type.HSTRING,  # appPackageFamilyName
                                                     IProtectionPolicyAuditInfo,  # auditInfo
                                                     _type.HSTRING,  # messageFromApp
                                                     _enum.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior,  # behavior
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                                    _type.HRESULT]
    RequestAccessToFilesForAppAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageItem],  # sourceItemList
                                                _type.HSTRING,  # appPackageFamilyName
                                                IProtectionPolicyAuditInfo,  # auditInfo
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                               _type.HRESULT]
    RequestAccessToFilesForAppWithMessageAndBehaviorAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageItem],  # sourceItemList
                                                                      _type.HSTRING,  # appPackageFamilyName
                                                                      IProtectionPolicyAuditInfo,  # auditInfo
                                                                      _type.HSTRING,  # messageFromApp
                                                                      _enum.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior,  # behavior
                                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                                                     _type.HRESULT]
    RequestAccessToFilesForProcessAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageItem],  # sourceItemList
                                                    _type.UINT32,  # processId
                                                    IProtectionPolicyAuditInfo,  # auditInfo
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                                   _type.HRESULT]
    RequestAccessToFilesForProcessWithMessageAndBehaviorAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageItem],  # sourceItemList
                                                                          _type.UINT32,  # processId
                                                                          IProtectionPolicyAuditInfo,  # auditInfo
                                                                          _type.HSTRING,  # messageFromApp
                                                                          _enum.Windows.Security.EnterpriseData.ProtectionPolicyRequestAccessBehavior,  # behavior
                                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # result
                                                                         _type.HRESULT]
    IsFileProtectionRequiredAsync: _Callable[[_Windows_Storage.IStorageItem,  # target
                                              _type.HSTRING,  # identity
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                             _type.HRESULT]
    IsFileProtectionRequiredForNewFileAsync: _Callable[[_Windows_Storage.IStorageFolder,  # parentFolder
                                                        _type.HSTRING,  # identity
                                                        _type.HSTRING,  # desiredName
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                       _type.HRESULT]
    get_PrimaryManagedIdentity: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    GetPrimaryManagedIdentityForIdentity: _Callable[[_type.HSTRING,  # identity
                                                     _Pointer[_type.HSTRING]],  # value
                                                    _type.HRESULT]


class IThreadNetworkContext(_inspectable.IInspectable):
    pass
