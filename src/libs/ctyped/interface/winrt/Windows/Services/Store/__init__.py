from __future__ import annotations as _

from typing import Callable as _Callable

from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IStoreAcquireLicenseResult(_inspectable.IInspectable):
    get_StorePackageLicense: _Callable[[_Pointer[IStorePackageLicense]],  # value
                                       _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IStoreAppLicense(_inspectable.IInspectable):
    get_SkuStoreId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsTrial: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_AddOnLicenses: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IStoreLicense]]],  # value
                                 _type.HRESULT]
    get_TrialTimeRemaining: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    get_IsTrialOwnedByThisUser: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_TrialUniqueId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IStoreAppLicense2(_inspectable.IInspectable):
    get_IsDiscLicense: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IStoreAvailability(_inspectable.IInspectable):
    get_StoreId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_EndDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_Price: _Callable[[_Pointer[IStorePrice]],  # value
                         _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    RequestPurchaseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                    _type.HRESULT]
    RequestPurchaseWithPurchasePropertiesAsync: _Callable[[IStorePurchaseProperties,  # storePurchaseProperties
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                                          _type.HRESULT]


class IStoreCanAcquireLicenseResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_LicensableSku: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreCanLicenseStatus]],  # value
                          _type.HRESULT]


class IStoreCollectionData(_inspectable.IInspectable):
    get_IsTrial: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_CampaignId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_DeveloperOfferId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_AcquiredDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    get_StartDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_EndDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_TrialTimeRemaining: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                      _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IStoreConsumableResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreConsumableStatus]],  # value
                          _type.HRESULT]
    get_TrackingId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_BalanceRemaining: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IStoreContext(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    add_OfflineLicensesChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IStoreContext, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_OfflineLicensesChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    GetCustomerPurchaseIdAsync: _Callable[[_type.HSTRING,  # serviceTicket
                                           _type.HSTRING,  # publisherUserId
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                          _type.HRESULT]
    GetCustomerCollectionsIdAsync: _Callable[[_type.HSTRING,  # serviceTicket
                                              _type.HSTRING,  # publisherUserId
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                             _type.HRESULT]
    GetAppLicenseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStoreAppLicense]]],  # operation
                                  _type.HRESULT]
    GetStoreProductForCurrentAppAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductResult]]],  # operation
                                                 _type.HRESULT]
    GetStoreProductsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                      _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # storeIds
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductQueryResult]]],  # operation
                                     _type.HRESULT]
    GetAssociatedStoreProductsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductQueryResult]]],  # operation
                                               _type.HRESULT]
    GetAssociatedStoreProductsWithPagingAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                                          _type.UINT32,  # maxItemsToRetrievePerPage
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductPagedQueryResult]]],  # operation
                                                         _type.HRESULT]
    GetUserCollectionAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductQueryResult]]],  # operation
                                      _type.HRESULT]
    GetUserCollectionWithPagingAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                                 _type.UINT32,  # maxItemsToRetrievePerPage
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductPagedQueryResult]]],  # operation
                                                _type.HRESULT]
    ReportConsumableFulfillmentAsync: _Callable[[_type.HSTRING,  # productStoreId
                                                 _type.UINT32,  # quantity
                                                 _struct.GUID,  # trackingId
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IStoreConsumableResult]]],  # operation
                                                _type.HRESULT]
    GetConsumableBalanceRemainingAsync: _Callable[[_type.HSTRING,  # productStoreId
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IStoreConsumableResult]]],  # operation
                                                  _type.HRESULT]
    AcquireStoreLicenseForOptionalPackageAsync: _Callable[[_Windows_ApplicationModel.IPackage,  # optionalPackage
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStoreAcquireLicenseResult]]],  # operation
                                                          _type.HRESULT]
    RequestPurchaseAsync: _Callable[[_type.HSTRING,  # storeId
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                    _type.HRESULT]
    RequestPurchaseWithPurchasePropertiesAsync: _Callable[[_type.HSTRING,  # storeId
                                                           IStorePurchaseProperties,  # storePurchaseProperties
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                                          _type.HRESULT]
    GetAppAndOptionalStorePackageUpdatesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorePackageUpdate]]]],  # operation
                                                         _type.HRESULT]
    RequestDownloadStorePackageUpdatesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IStorePackageUpdate],  # storePackageUpdates
                                                        _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IStorePackageUpdateResult, _struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # operation
                                                       _type.HRESULT]
    RequestDownloadAndInstallStorePackageUpdatesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IStorePackageUpdate],  # storePackageUpdates
                                                                  _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IStorePackageUpdateResult, _struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # operation
                                                                 _type.HRESULT]
    RequestDownloadAndInstallStorePackagesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # storeIds
                                                            _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IStorePackageUpdateResult, _struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # operation
                                                           _type.HRESULT]


class IStoreContext2(_inspectable.IInspectable):
    FindStoreProductForPackageAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                                _Windows_ApplicationModel.IPackage,  # package
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductResult]]],  # operation
                                               _type.HRESULT]


class IStoreContext3(_inspectable.IInspectable):
    get_CanSilentlyDownloadStorePackageUpdates: _Callable[[_Pointer[_type.boolean]],  # value
                                                          _type.HRESULT]
    TrySilentDownloadStorePackageUpdatesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IStorePackageUpdate],  # storePackageUpdates
                                                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IStorePackageUpdateResult, _struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # operation
                                                         _type.HRESULT]
    TrySilentDownloadAndInstallStorePackageUpdatesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IStorePackageUpdate],  # storePackageUpdates
                                                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IStorePackageUpdateResult, _struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # operation
                                                                   _type.HRESULT]
    CanAcquireStoreLicenseForOptionalPackageAsync: _Callable[[_Windows_ApplicationModel.IPackage,  # optionalPackage
                                                              _Pointer[_Windows_Foundation.IAsyncOperation[IStoreCanAcquireLicenseResult]]],  # operation
                                                             _type.HRESULT]
    CanAcquireStoreLicenseAsync: _Callable[[_type.HSTRING,  # productStoreId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IStoreCanAcquireLicenseResult]]],  # operation
                                           _type.HRESULT]
    GetStoreProductsWithOptionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                                 _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # storeIds
                                                 IStoreProductOptions,  # storeProductOptions
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductQueryResult]]],  # operation
                                                _type.HRESULT]
    GetAssociatedStoreQueueItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStoreQueueItem]]]],  # operation
                                                 _type.HRESULT]
    GetStoreQueueItemsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # storeIds
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStoreQueueItem]]]],  # operation
                                       _type.HRESULT]
    RequestDownloadAndInstallStorePackagesWithInstallOptionsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # storeIds
                                                                              IStorePackageInstallOptions,  # storePackageInstallOptions
                                                                              _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IStorePackageUpdateResult, _struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # operation
                                                                             _type.HRESULT]
    DownloadAndInstallStorePackagesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # storeIds
                                                     _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IStorePackageUpdateResult, _struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # operation
                                                    _type.HRESULT]
    RequestUninstallStorePackageAsync: _Callable[[_Windows_ApplicationModel.IPackage,  # package
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IStoreUninstallStorePackageResult]]],  # operation
                                                 _type.HRESULT]
    RequestUninstallStorePackageByStoreIdAsync: _Callable[[_type.HSTRING,  # storeId
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStoreUninstallStorePackageResult]]],  # operation
                                                          _type.HRESULT]
    UninstallStorePackageAsync: _Callable[[_Windows_ApplicationModel.IPackage,  # package
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStoreUninstallStorePackageResult]]],  # operation
                                          _type.HRESULT]
    UninstallStorePackageByStoreIdAsync: _Callable[[_type.HSTRING,  # storeId
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IStoreUninstallStorePackageResult]]],  # operation
                                                   _type.HRESULT]


class IStoreContext4(_inspectable.IInspectable):
    RequestRateAndReviewAppAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStoreRateAndReviewResult]]],  # operation
                                            _type.HRESULT]
    SetInstallOrderForAssociatedStoreQueueItemsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IStoreQueueItem],  # items
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStoreQueueItem]]]],  # operation
                                                                _type.HRESULT]


class IStoreContext5(_inspectable.IInspectable):
    GetUserPurchaseHistoryAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productKinds
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductQueryResult]]],  # operation
                                           _type.HRESULT]
    GetAssociatedStoreProductsByInAppOfferTokenAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # inAppOfferTokens
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductQueryResult]]],  # operation
                                                                _type.HRESULT]
    RequestPurchaseByInAppOfferTokenAsync: _Callable[[_type.HSTRING,  # inAppOfferToken
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                                     _type.HRESULT]


class IStoreContextStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IStoreContext]],  # value
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IStoreContext]],  # value
                          _type.HRESULT]


class IStoreImage(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_ImagePurposeTag: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IStoreLicense(_inspectable.IInspectable):
    get_SkuStoreId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_InAppOfferToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IStorePackageInstallOptions(_inspectable.IInspectable):
    get_AllowForcedAppRestart: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_AllowForcedAppRestart: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class IStorePackageLicense(_inspectable.IInspectable):
    add_LicenseLost: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorePackageLicense, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_LicenseLost: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]
    get_IsValid: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    ReleaseLicense: _Callable[[],
                              _type.HRESULT]


class IStorePackageUpdate(_inspectable.IInspectable):
    get_Package: _Callable[[_Pointer[_Windows_ApplicationModel.IPackage]],  # value
                           _type.HRESULT]
    get_Mandatory: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IStorePackageUpdateResult(_inspectable.IInspectable):
    get_OverallState: _Callable[[_Pointer[_enum.Windows.Services.Store.StorePackageUpdateState]],  # value
                                _type.HRESULT]
    get_StorePackageUpdateStatuses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Services.Store.StorePackageUpdateStatus]]],  # value
                                              _type.HRESULT]


class IStorePackageUpdateResult2(_inspectable.IInspectable):
    get_StoreQueueItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStoreQueueItem]]],  # value
                                   _type.HRESULT]


class IStorePrice(_inspectable.IInspectable):
    get_FormattedBasePrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_FormattedPrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_IsOnSale: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_SaleEndDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    get_CurrencyCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_FormattedRecurrencePrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]


class IStorePrice2(_inspectable.IInspectable):
    get_UnformattedBasePrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_UnformattedPrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_UnformattedRecurrencePrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]


class IStoreProduct(_inspectable.IInspectable):
    get_StoreId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ProductKind: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_HasDigitalDownload: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_Keywords: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_Images: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStoreImage]]],  # value
                          _type.HRESULT]
    get_Videos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStoreVideo]]],  # value
                          _type.HRESULT]
    get_Skus: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStoreSku]]],  # value
                        _type.HRESULT]
    get_IsInUserCollection: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_Price: _Callable[[_Pointer[IStorePrice]],  # value
                         _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_LinkUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    GetIsAnySkuInstalledAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                         _type.HRESULT]
    RequestPurchaseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                    _type.HRESULT]
    RequestPurchaseWithPurchasePropertiesAsync: _Callable[[IStorePurchaseProperties,  # storePurchaseProperties
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                                          _type.HRESULT]
    get_InAppOfferToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IStoreProductOptions(_inspectable.IInspectable):
    get_ActionFilters: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                 _type.HRESULT]


class IStoreProductPagedQueryResult(_inspectable.IInspectable):
    get_Products: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IStoreProduct]]],  # value
                            _type.HRESULT]
    get_HasMoreResults: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    GetNextAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStoreProductPagedQueryResult]]],  # operation
                            _type.HRESULT]


class IStoreProductQueryResult(_inspectable.IInspectable):
    get_Products: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IStoreProduct]]],  # value
                            _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IStoreProductResult(_inspectable.IInspectable):
    get_Product: _Callable[[_Pointer[IStoreProduct]],  # value
                           _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IStorePurchaseProperties(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_ExtendedJsonData: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]


class IStorePurchasePropertiesFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # name
                       _Pointer[IStorePurchaseProperties]],  # storePurchaseProperties
                      _type.HRESULT]


class IStorePurchaseResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Store.StorePurchaseStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IStoreQueueItem(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_InstallKind: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreQueueItemKind]],  # value
                               _type.HRESULT]
    GetCurrentStatus: _Callable[[_Pointer[IStoreQueueItemStatus]],  # result
                                _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[IStoreQueueItem, IStoreQueueItemCompletedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_StatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IStoreQueueItem, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_StatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IStoreQueueItem2(_inspectable.IInspectable):
    CancelInstallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                  _type.HRESULT]
    PauseInstallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                 _type.HRESULT]
    ResumeInstallAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                  _type.HRESULT]


class IStoreQueueItemCompletedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[IStoreQueueItemStatus]],  # value
                          _type.HRESULT]


class IStoreQueueItemStatus(_inspectable.IInspectable):
    get_PackageInstallState: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreQueueItemState]],  # value
                                       _type.HRESULT]
    get_PackageInstallExtendedState: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreQueueItemExtendedState]],  # value
                                               _type.HRESULT]
    get_UpdateStatus: _Callable[[_Pointer[_struct.Windows.Services.Store.StorePackageUpdateStatus]],  # value
                                _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IStoreRateAndReviewResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_WasUpdated: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreRateAndReviewStatus]],  # value
                          _type.HRESULT]


class IStoreRequestHelperStatics(_inspectable.IInspectable, factory=True):
    SendRequestAsync: _Callable[[IStoreContext,  # context
                                 _type.UINT32,  # requestKind
                                 _type.HSTRING,  # parametersAsJson
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IStoreSendRequestResult]]],  # operation
                                _type.HRESULT]


class IStoreSendRequestResult(_inspectable.IInspectable):
    get_Response: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IStoreSendRequestResult2(_inspectable.IInspectable):
    get_HttpStatusCode: _Callable[[_Pointer[_enum.Windows.Web.Http.HttpStatusCode]],  # value
                                  _type.HRESULT]


class IStoreSku(_inspectable.IInspectable):
    get_StoreId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsTrial: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_CustomDeveloperData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_Images: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStoreImage]]],  # value
                          _type.HRESULT]
    get_Videos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStoreVideo]]],  # value
                          _type.HRESULT]
    get_Availabilities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStoreAvailability]]],  # value
                                  _type.HRESULT]
    get_Price: _Callable[[_Pointer[IStorePrice]],  # value
                         _type.HRESULT]
    get_ExtendedJsonData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_IsInUserCollection: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    get_BundledSkus: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                               _type.HRESULT]
    get_CollectionData: _Callable[[_Pointer[IStoreCollectionData]],  # value
                                  _type.HRESULT]
    GetIsInstalledAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                   _type.HRESULT]
    RequestPurchaseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                    _type.HRESULT]
    RequestPurchaseWithPurchasePropertiesAsync: _Callable[[IStorePurchaseProperties,  # storePurchaseProperties
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[IStorePurchaseResult]]],  # operation
                                                          _type.HRESULT]
    get_IsSubscription: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_SubscriptionInfo: _Callable[[_Pointer[IStoreSubscriptionInfo]],  # value
                                    _type.HRESULT]


class IStoreSubscriptionInfo(_inspectable.IInspectable):
    get_BillingPeriod: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    get_BillingPeriodUnit: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreDurationUnit]],  # value
                                     _type.HRESULT]
    get_HasTrialPeriod: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_TrialPeriod: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_TrialPeriodUnit: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreDurationUnit]],  # value
                                   _type.HRESULT]


class IStoreUninstallStorePackageResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.Services.Store.StoreUninstallStorePackageStatus]],  # value
                          _type.HRESULT]


class IStoreVideo(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_VideoPurposeTag: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_PreviewImage: _Callable[[_Pointer[IStoreImage]],  # value
                                _type.HRESULT]
