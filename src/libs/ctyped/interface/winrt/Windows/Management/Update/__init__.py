from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IPreviewBuildsManager(_inspectable.IInspectable):
    get_ArePreviewBuildsAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_ArePreviewBuildsAllowed: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    GetCurrentState: _Callable[[_Pointer[IPreviewBuildsState]],  # result
                               _type.HRESULT]
    SyncAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                         _type.HRESULT]


class IPreviewBuildsManagerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IPreviewBuildsManager]],  # value
                          _type.HRESULT]
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]

    _factory = True


class IPreviewBuildsState(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                              _type.HRESULT]


class IWindowsUpdate(_inspectable.IInspectable):
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_UpdateId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsFeatureUpdate: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsMinorImpact: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    get_IsSecurity: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsCritical: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsForOS: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_IsDriver: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsMandatory: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsUrgent: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsSeeker: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_MoreInfoUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_SupportUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                              _type.HRESULT]
    get_IsEulaAccepted: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_EulaText: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                            _type.HRESULT]
    get_AttentionRequiredInfo: _Callable[[_Pointer[IWindowsUpdateAttentionRequiredInfo]],  # value
                                         _type.HRESULT]
    get_ActionResult: _Callable[[_Pointer[IWindowsUpdateActionResult]],  # value
                                _type.HRESULT]
    get_CurrentAction: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ActionProgress: _Callable[[_Pointer[IWindowsUpdateActionProgress]],  # value
                                  _type.HRESULT]
    GetPropertyValue: _Callable[[_type.HSTRING,  # propertyName
                                 _Pointer[_inspectable.IInspectable]],  # result
                                _type.HRESULT]
    AcceptEula: _Callable[[],
                          _type.HRESULT]


class IWindowsUpdateActionCompletedEventArgs(_inspectable.IInspectable):
    get_Update: _Callable[[_Pointer[IWindowsUpdate]],  # value
                          _type.HRESULT]
    get_Action: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IWindowsUpdateActionProgress(_inspectable.IInspectable):
    get_Action: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]


class IWindowsUpdateActionResult(_inspectable.IInspectable):
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Action: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class IWindowsUpdateAdministrator(_inspectable.IInspectable):
    StartAdministratorScan: _Callable[[],
                                      _type.HRESULT]
    ApproveWindowsUpdateAction: _Callable[[_type.HSTRING,  # updateId
                                           _type.HSTRING],  # action
                                          _type.HRESULT]
    RevokeWindowsUpdateActionApproval: _Callable[[_type.HSTRING,  # updateId
                                                  _type.HSTRING],  # action
                                                 _type.HRESULT]
    ApproveWindowsUpdate: _Callable[[_type.HSTRING,  # updateId
                                     IWindowsUpdateApprovalData],  # approvalData
                                    _type.HRESULT]
    RevokeWindowsUpdateApproval: _Callable[[_type.HSTRING],  # updateId
                                           _type.HRESULT]
    GetUpdates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWindowsUpdate]]],  # result
                          _type.HRESULT]


class IWindowsUpdateAdministratorStatics(_inspectable.IInspectable):
    GetRegisteredAdministrator: _Callable[[_type.HSTRING,  # organizationName
                                           _Pointer[IWindowsUpdateGetAdministratorResult]],  # result
                                          _type.HRESULT]
    RegisterForAdministration: _Callable[[_type.HSTRING,  # organizationName
                                          _enum.Windows.Management.Update.WindowsUpdateAdministratorOptions,  # options
                                          _Pointer[_enum.Windows.Management.Update.WindowsUpdateAdministratorStatus]],  # result
                                         _type.HRESULT]
    UnregisterForAdministration: _Callable[[_type.HSTRING,  # organizationName
                                            _Pointer[_enum.Windows.Management.Update.WindowsUpdateAdministratorStatus]],  # result
                                           _type.HRESULT]
    GetRegisteredAdministratorName: _Callable[[_Pointer[_type.HSTRING]],  # result
                                              _type.HRESULT]
    RequestRestart: _Callable[[IWindowsUpdateRestartRequestOptions,  # restartOptions
                               _Pointer[_type.HSTRING]],  # result
                              _type.HRESULT]
    CancelRestartRequest: _Callable[[_type.HSTRING],  # requestRestartToken
                                    _type.HRESULT]

    _factory = True


class IWindowsUpdateApprovalData(_inspectable.IInspectable):
    get_Seeker: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                          _type.HRESULT]
    put_Seeker: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                          _type.HRESULT]
    get_AllowDownloadOnMetered: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                          _type.HRESULT]
    put_AllowDownloadOnMetered: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                                          _type.HRESULT]
    get_ComplianceDeadlineInDays: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                            _type.HRESULT]
    put_ComplianceDeadlineInDays: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                            _type.HRESULT]
    get_ComplianceGracePeriodInDays: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                               _type.HRESULT]
    put_ComplianceGracePeriodInDays: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                               _type.HRESULT]
    get_OptOutOfAutoReboot: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.boolean]]],  # value
                                      _type.HRESULT]
    put_OptOutOfAutoReboot: _Callable[[_Windows_Foundation.IReference[_type.boolean]],  # value
                                      _type.HRESULT]


class IWindowsUpdateAttentionRequiredInfo(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.Management.Update.WindowsUpdateAttentionRequiredReason]],  # value
                          _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                             _type.HRESULT]


class IWindowsUpdateAttentionRequiredReasonChangedEventArgs(_inspectable.IInspectable):
    get_Update: _Callable[[_Pointer[IWindowsUpdate]],  # value
                          _type.HRESULT]
    get_Reason: _Callable[[_Pointer[_enum.Windows.Management.Update.WindowsUpdateAttentionRequiredReason]],  # value
                          _type.HRESULT]


class IWindowsUpdateGetAdministratorResult(_inspectable.IInspectable):
    get_Administrator: _Callable[[_Pointer[IWindowsUpdateAdministrator]],  # value
                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Management.Update.WindowsUpdateAdministratorStatus]],  # value
                          _type.HRESULT]


class IWindowsUpdateItem(_inspectable.IInspectable):
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_UpdateId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_MoreInfoUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    get_Category: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Operation: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IWindowsUpdateManager(_inspectable.IInspectable):
    add_ScanningStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWindowsUpdateManager, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ScanningStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_WorkingStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWindowsUpdateManager, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_WorkingStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ProgressChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWindowsUpdateManager, IWindowsUpdateProgressChangedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ProgressChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_AttentionRequiredReasonChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWindowsUpdateManager, IWindowsUpdateAttentionRequiredReasonChangedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_AttentionRequiredReasonChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_ActionCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IWindowsUpdateManager, IWindowsUpdateActionCompletedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_ActionCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_ScanCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IWindowsUpdateManager, IWindowsUpdateScanCompletedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ScanCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    get_IsScanning: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsWorking: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_LastSuccessfulScanTimestamp: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                               _type.HRESULT]
    GetApplicableUpdates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWindowsUpdate]]],  # result
                                    _type.HRESULT]
    GetMostRecentCompletedUpdates: _Callable[[_type.INT32,  # count
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[IWindowsUpdateItem]]],  # result
                                             _type.HRESULT]
    GetMostRecentCompletedUpdatesAsync: _Callable[[_type.INT32,  # count
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IWindowsUpdateItem]]]],  # operation
                                                  _type.HRESULT]
    StartScan: _Callable[[_type.boolean],  # userInitiated
                         _type.HRESULT]


class IWindowsUpdateManagerFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.HSTRING,  # clientId
                               _Pointer[IWindowsUpdateManager]],  # value
                              _type.HRESULT]

    _factory = True


class IWindowsUpdateProgressChangedEventArgs(_inspectable.IInspectable):
    get_Update: _Callable[[_Pointer[IWindowsUpdate]],  # value
                          _type.HRESULT]
    get_ActionProgress: _Callable[[_Pointer[IWindowsUpdateActionProgress]],  # value
                                  _type.HRESULT]


class IWindowsUpdateRestartRequestOptions(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_MoreInfoUrl: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_MoreInfoUrl: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]
    get_ComplianceDeadlineInDays: _Callable[[_Pointer[_type.INT32]],  # value
                                            _type.HRESULT]
    put_ComplianceDeadlineInDays: _Callable[[_type.INT32],  # value
                                            _type.HRESULT]
    get_ComplianceGracePeriodInDays: _Callable[[_Pointer[_type.INT32]],  # value
                                               _type.HRESULT]
    put_ComplianceGracePeriodInDays: _Callable[[_type.INT32],  # value
                                               _type.HRESULT]
    get_OrganizationName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_OrganizationName: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_OptOutOfAutoReboot: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_OptOutOfAutoReboot: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class IWindowsUpdateRestartRequestOptionsFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.HSTRING,  # title
                               _type.HSTRING,  # description
                               _Windows_Foundation.IUriRuntimeClass,  # moreInfoUrl
                               _type.INT32,  # complianceDeadlineInDays
                               _type.INT32,  # complianceGracePeriodInDays
                               _Pointer[IWindowsUpdateRestartRequestOptions]],  # value
                              _type.HRESULT]

    _factory = True


class IWindowsUpdateScanCompletedEventArgs(_inspectable.IInspectable):
    get_ProviderId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Updates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWindowsUpdate]]],  # value
                           _type.HRESULT]
