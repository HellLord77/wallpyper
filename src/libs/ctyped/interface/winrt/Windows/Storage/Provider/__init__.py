from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Streams as _Windows_Storage_Streams
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ICachedFileUpdaterStatics(_inspectable.IInspectable, factory=True):
    SetUpdateInformation: _Callable[[_Windows_Storage.IStorageFile,  # file
                                     _type.HSTRING,  # contentId
                                     _enum.Windows.Storage.Provider.ReadActivationMode,  # readMode
                                     _enum.Windows.Storage.Provider.WriteActivationMode,  # writeMode
                                     _enum.Windows.Storage.Provider.CachedFileOptions],  # options
                                    _type.HRESULT]


class ICachedFileUpdaterUI(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_UpdateTarget: _Callable[[_Pointer[_enum.Windows.Storage.Provider.CachedFileTarget]],  # value
                                _type.HRESULT]
    add_FileUpdateRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICachedFileUpdaterUI, IFileUpdateRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_FileUpdateRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_UIRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICachedFileUpdaterUI, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_UIRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    get_UIStatus: _Callable[[_Pointer[_enum.Windows.Storage.Provider.UIStatus]],  # value
                            _type.HRESULT]


class ICachedFileUpdaterUI2(_inspectable.IInspectable):
    get_UpdateRequest: _Callable[[_Pointer[IFileUpdateRequest]],  # value
                                 _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IFileUpdateRequestDeferral]],  # value
                           _type.HRESULT]


class IFileUpdateRequest(_inspectable.IInspectable):
    get_ContentId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                        _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Storage.Provider.FileUpdateStatus]],  # value
                          _type.HRESULT]
    put_Status: _Callable[[_enum.Windows.Storage.Provider.FileUpdateStatus],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IFileUpdateRequestDeferral]],  # value
                           _type.HRESULT]
    UpdateLocalFile: _Callable[[_Windows_Storage.IStorageFile],  # value
                               _type.HRESULT]


class IFileUpdateRequest2(_inspectable.IInspectable):
    get_UserInputNeededMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    put_UserInputNeededMessage: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]


class IFileUpdateRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IFileUpdateRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IFileUpdateRequest]],  # value
                           _type.HRESULT]


class IStorageProviderFileTypeInfo(_inspectable.IInspectable):
    get_FileExtension: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_IconResource: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IStorageProviderFileTypeInfoFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # fileExtension
                               _type.HSTRING,  # iconResource
                               _Pointer[IStorageProviderFileTypeInfo]],  # value
                              _type.HRESULT]


class IStorageProviderGetContentInfoForPathResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderUriSourceStatus]],  # value
                          _type.HRESULT]
    put_Status: _Callable[[_enum.Windows.Storage.Provider.StorageProviderUriSourceStatus],  # value
                          _type.HRESULT]
    get_ContentUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_ContentUri: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_ContentId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_ContentId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class IStorageProviderGetPathForContentUriResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderUriSourceStatus]],  # value
                          _type.HRESULT]
    put_Status: _Callable[[_enum.Windows.Storage.Provider.StorageProviderUriSourceStatus],  # value
                          _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Path: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]


class IStorageProviderItemPropertiesStatics(_inspectable.IInspectable, factory=True):
    SetAsync: _Callable[[_Windows_Storage.IStorageItem,  # item
                         _Windows_Foundation_Collections.IIterable[IStorageProviderItemProperty],  # itemProperties
                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                        _type.HRESULT]


class IStorageProviderItemProperty(_inspectable.IInspectable):
    put_Id: _Callable[[_type.INT32],  # value
                      _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_IconResource: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_IconResource: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IStorageProviderItemPropertyDefinition(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.INT32]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.INT32],  # value
                      _type.HRESULT]
    get_DisplayNameResource: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_DisplayNameResource: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]


class IStorageProviderItemPropertySource(_inspectable.IInspectable):
    GetItemProperties: _Callable[[_type.HSTRING,  # itemPath
                                  _Pointer[_Windows_Foundation_Collections.IIterable[IStorageProviderItemProperty]]],  # result
                                 _type.HRESULT]


class IStorageProviderMoreInfoUI(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Message: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Command: _Callable[[_Pointer[IStorageProviderUICommand]],  # value
                           _type.HRESULT]
    put_Command: _Callable[[IStorageProviderUICommand],  # value
                           _type.HRESULT]


class IStorageProviderPropertyCapabilities(_inspectable.IInspectable):
    IsPropertySupported: _Callable[[_type.HSTRING,  # propertyCanonicalName
                                    _Pointer[_type.boolean]],  # isSupported
                                   _type.HRESULT]


class IStorageProviderQuotaUI(_inspectable.IInspectable):
    get_QuotaTotalInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                     _type.HRESULT]
    put_QuotaTotalInBytes: _Callable[[_type.UINT64],  # value
                                     _type.HRESULT]
    get_QuotaUsedInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    put_QuotaUsedInBytes: _Callable[[_type.UINT64],  # value
                                    _type.HRESULT]
    get_QuotaUsedLabel: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_QuotaUsedLabel: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_QuotaUsedColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                                  _type.HRESULT]
    put_QuotaUsedColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]


class IStorageProviderStatusUI(_inspectable.IInspectable):
    get_ProviderState: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderState]],  # value
                                 _type.HRESULT]
    put_ProviderState: _Callable[[_enum.Windows.Storage.Provider.StorageProviderState],  # value
                                 _type.HRESULT]
    get_ProviderStateLabel: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_ProviderStateLabel: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_ProviderStateIcon: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                     _type.HRESULT]
    put_ProviderStateIcon: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                     _type.HRESULT]
    get_SyncStatusCommand: _Callable[[_Pointer[IStorageProviderUICommand]],  # value
                                     _type.HRESULT]
    put_SyncStatusCommand: _Callable[[IStorageProviderUICommand],  # value
                                     _type.HRESULT]
    get_QuotaUI: _Callable[[_Pointer[IStorageProviderQuotaUI]],  # value
                           _type.HRESULT]
    put_QuotaUI: _Callable[[IStorageProviderQuotaUI],  # value
                           _type.HRESULT]
    get_MoreInfoUI: _Callable[[_Pointer[IStorageProviderMoreInfoUI]],  # value
                              _type.HRESULT]
    put_MoreInfoUI: _Callable[[IStorageProviderMoreInfoUI],  # value
                              _type.HRESULT]
    get_ProviderPrimaryCommand: _Callable[[_Pointer[IStorageProviderUICommand]],  # value
                                          _type.HRESULT]
    put_ProviderPrimaryCommand: _Callable[[IStorageProviderUICommand],  # value
                                          _type.HRESULT]
    get_ProviderSecondaryCommands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IStorageProviderUICommand]]],  # value
                                             _type.HRESULT]
    put_ProviderSecondaryCommands: _Callable[[_Windows_Foundation_Collections.IVector[IStorageProviderUICommand]],  # value
                                             _type.HRESULT]


class IStorageProviderStatusUISource(_inspectable.IInspectable):
    GetStatusUI: _Callable[[_Pointer[IStorageProviderStatusUI]],  # result
                           _type.HRESULT]
    add_StatusUIChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorageProviderStatusUISource, _inspectable.IInspectable],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_StatusUIChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IStorageProviderStatusUISourceFactory(_inspectable.IInspectable):
    GetStatusUISource: _Callable[[_type.HSTRING,  # syncRootId
                                  _Pointer[IStorageProviderStatusUISource]],  # result
                                 _type.HRESULT]


class IStorageProviderSyncRootInfo(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Context: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                           _type.HRESULT]
    put_Context: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                           _type.HRESULT]
    get_Path: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                        _type.HRESULT]
    put_Path: _Callable[[_Windows_Storage.IStorageFolder],  # value
                        _type.HRESULT]
    get_DisplayNameResource: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_DisplayNameResource: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_IconResource: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_IconResource: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]
    get_HydrationPolicy: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderHydrationPolicy]],  # value
                                   _type.HRESULT]
    put_HydrationPolicy: _Callable[[_enum.Windows.Storage.Provider.StorageProviderHydrationPolicy],  # value
                                   _type.HRESULT]
    get_HydrationPolicyModifier: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderHydrationPolicyModifier]],  # value
                                           _type.HRESULT]
    put_HydrationPolicyModifier: _Callable[[_enum.Windows.Storage.Provider.StorageProviderHydrationPolicyModifier],  # value
                                           _type.HRESULT]
    get_PopulationPolicy: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderPopulationPolicy]],  # value
                                    _type.HRESULT]
    put_PopulationPolicy: _Callable[[_enum.Windows.Storage.Provider.StorageProviderPopulationPolicy],  # value
                                    _type.HRESULT]
    get_InSyncPolicy: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderInSyncPolicy]],  # value
                                _type.HRESULT]
    put_InSyncPolicy: _Callable[[_enum.Windows.Storage.Provider.StorageProviderInSyncPolicy],  # value
                                _type.HRESULT]
    get_HardlinkPolicy: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderHardlinkPolicy]],  # value
                                  _type.HRESULT]
    put_HardlinkPolicy: _Callable[[_enum.Windows.Storage.Provider.StorageProviderHardlinkPolicy],  # value
                                  _type.HRESULT]
    get_ShowSiblingsAsGroup: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_ShowSiblingsAsGroup: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Version: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_ProtectionMode: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderProtectionMode]],  # value
                                  _type.HRESULT]
    put_ProtectionMode: _Callable[[_enum.Windows.Storage.Provider.StorageProviderProtectionMode],  # value
                                  _type.HRESULT]
    get_AllowPinning: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_AllowPinning: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    get_StorageProviderItemPropertyDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IStorageProviderItemPropertyDefinition]]],  # value
                                                          _type.HRESULT]
    get_RecycleBinUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                 _type.HRESULT]
    put_RecycleBinUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                 _type.HRESULT]


class IStorageProviderSyncRootInfo2(_inspectable.IInspectable):
    get_ProviderId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    put_ProviderId: _Callable[[_struct.GUID],  # value
                              _type.HRESULT]


class IStorageProviderSyncRootInfo3(_inspectable.IInspectable):
    get_FallbackFileTypeInfo: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IStorageProviderFileTypeInfo]]],  # value
                                        _type.HRESULT]


class IStorageProviderSyncRootManagerStatics(_inspectable.IInspectable, factory=True):
    Register: _Callable[[IStorageProviderSyncRootInfo],  # syncRootInformation
                        _type.HRESULT]
    Unregister: _Callable[[_type.HSTRING],  # id
                          _type.HRESULT]
    GetSyncRootInformationForFolder: _Callable[[_Windows_Storage.IStorageFolder,  # folder
                                                _Pointer[IStorageProviderSyncRootInfo]],  # result
                                               _type.HRESULT]
    GetSyncRootInformationForId: _Callable[[_type.HSTRING,  # id
                                            _Pointer[IStorageProviderSyncRootInfo]],  # result
                                           _type.HRESULT]
    GetCurrentSyncRoots: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStorageProviderSyncRootInfo]]],  # result
                                   _type.HRESULT]


class IStorageProviderSyncRootManagerStatics2(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IStorageProviderUICommand(_inspectable.IInspectable):
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Icon: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                        _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Storage.Provider.StorageProviderUICommandState]],  # value
                         _type.HRESULT]
    Invoke: _Callable[[],
                      _type.HRESULT]


class IStorageProviderUriSource(_inspectable.IInspectable):
    GetPathForContentUri: _Callable[[_type.HSTRING,  # contentUri
                                     IStorageProviderGetPathForContentUriResult],  # result
                                    _type.HRESULT]
    GetContentInfoForPath: _Callable[[_type.HSTRING,  # path
                                      IStorageProviderGetContentInfoForPathResult],  # result
                                     _type.HRESULT]
