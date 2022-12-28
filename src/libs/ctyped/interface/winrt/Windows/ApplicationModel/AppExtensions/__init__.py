from __future__ import annotations as _

from typing import Callable as _Callable

from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppExtension(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]
    get_AppInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppInfo]],  # value
                           _type.HRESULT]
    GetExtensionPropertiesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IPropertySet]]],  # operation
                                           _type.HRESULT]
    GetPublicFolderAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFolder]]],  # operation
                                    _type.HRESULT]


class IAppExtension2(_inspectable.IInspectable):
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IAppExtensionCatalog(_inspectable.IInspectable):
    FindAllAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppExtension]]]],  # operation
                            _type.HRESULT]
    RequestRemovePackageAsync: _Callable[[_type.HSTRING,  # packageFullName
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    add_PackageInstalled: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppExtensionCatalog, IAppExtensionPackageInstalledEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_PackageInstalled: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_PackageUpdating: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppExtensionCatalog, IAppExtensionPackageUpdatingEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_PackageUpdating: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    add_PackageUpdated: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppExtensionCatalog, IAppExtensionPackageUpdatedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_PackageUpdated: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_PackageUninstalling: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppExtensionCatalog, IAppExtensionPackageUninstallingEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PackageUninstalling: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_PackageStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppExtensionCatalog, IAppExtensionPackageStatusChangedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_PackageStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IAppExtensionCatalogStatics(_inspectable.IInspectable):
    Open: _Callable[[_type.HSTRING,  # appExtensionName
                     _Pointer[IAppExtensionCatalog]],  # value
                    _type.HRESULT]

    _factory = True


class IAppExtensionPackageInstalledEventArgs(_inspectable.IInspectable):
    get_AppExtensionName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]
    get_Extensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppExtension]]],  # values
                              _type.HRESULT]


class IAppExtensionPackageStatusChangedEventArgs(_inspectable.IInspectable):
    get_AppExtensionName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]


class IAppExtensionPackageUninstallingEventArgs(_inspectable.IInspectable):
    get_AppExtensionName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]


class IAppExtensionPackageUpdatedEventArgs(_inspectable.IInspectable):
    get_AppExtensionName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]
    get_Extensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAppExtension]]],  # values
                              _type.HRESULT]


class IAppExtensionPackageUpdatingEventArgs(_inspectable.IInspectable):
    get_AppExtensionName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]
