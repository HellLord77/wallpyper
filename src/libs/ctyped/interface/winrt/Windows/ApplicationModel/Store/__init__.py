from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _ILicenseChangedEventHandler:
    Invoke: _Callable[[],
                      _type.HRESULT]


class ILicenseChangedEventHandler(_ILicenseChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ILicenseChangedEventHandler_impl(_ILicenseChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICurrentApp(_inspectable.IInspectable, factory=True):
    get_LicenseInformation: _Callable[[_Pointer[ILicenseInformation]],  # value
                                      _type.HRESULT]
    get_LinkUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    get_AppId: _Callable[[_Pointer[_struct.GUID]],  # value
                         _type.HRESULT]
    RequestAppPurchaseAsync: _Callable[[_type.boolean,  # includeReceipt
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # requestAppPurchaseOperation
                                       _type.HRESULT]
    RequestProductPurchaseAsync: _Callable[[_type.HSTRING,  # productId
                                            _type.boolean,  # includeReceipt
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # requestProductPurchaseOperation
                                           _type.HRESULT]
    LoadListingInformationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IListingInformation]]],  # loadListingOperation
                                           _type.HRESULT]
    GetAppReceiptAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # appReceiptOperation
                                  _type.HRESULT]
    GetProductReceiptAsync: _Callable[[_type.HSTRING,  # productId
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # getProductReceiptOperation
                                      _type.HRESULT]


class ICurrentApp2Statics(_inspectable.IInspectable, factory=True):
    GetCustomerPurchaseIdAsync: _Callable[[_type.HSTRING,  # serviceTicket
                                           _type.HSTRING,  # publisherUserId
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                          _type.HRESULT]
    GetCustomerCollectionsIdAsync: _Callable[[_type.HSTRING,  # serviceTicket
                                              _type.HSTRING,  # publisherUserId
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                             _type.HRESULT]


class ICurrentAppSimulator(_inspectable.IInspectable, factory=True):
    get_LicenseInformation: _Callable[[_Pointer[ILicenseInformation]],  # value
                                      _type.HRESULT]
    get_LinkUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    get_AppId: _Callable[[_Pointer[_struct.GUID]],  # value
                         _type.HRESULT]
    RequestAppPurchaseAsync: _Callable[[_type.boolean,  # includeReceipt
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # requestAppPurchaseOperation
                                       _type.HRESULT]
    RequestProductPurchaseAsync: _Callable[[_type.HSTRING,  # productId
                                            _type.boolean,  # includeReceipt
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # requestProductPurchaseOperation
                                           _type.HRESULT]
    LoadListingInformationAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IListingInformation]]],  # loadListingOperation
                                           _type.HRESULT]
    GetAppReceiptAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # appReceiptOperation
                                  _type.HRESULT]
    GetProductReceiptAsync: _Callable[[_type.HSTRING,  # productId
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # getProductReceiptOperation
                                      _type.HRESULT]
    ReloadSimulatorAsync: _Callable[[_Windows_Storage.IStorageFile,  # simulatorSettingsFile
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # reloadSimulatorOperation
                                    _type.HRESULT]


class ICurrentAppSimulatorStaticsWithFiltering(_inspectable.IInspectable, factory=True):
    LoadListingInformationByProductIdsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productIds
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IListingInformation]]],  # loadListingOperation
                                                       _type.HRESULT]
    LoadListingInformationByKeywordsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # keywords
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IListingInformation]]],  # loadListingOperation
                                                     _type.HRESULT]


class ICurrentAppSimulatorWithCampaignId(_inspectable.IInspectable, factory=True):
    GetAppPurchaseCampaignIdAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                             _type.HRESULT]


class ICurrentAppSimulatorWithConsumables(_inspectable.IInspectable, factory=True):
    ReportConsumableFulfillmentAsync: _Callable[[_type.HSTRING,  # productId
                                                 _struct.GUID,  # transactionId
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Store.FulfillmentResult]]],  # reportConsumableFulfillmentOperation
                                                _type.HRESULT]
    RequestProductPurchaseWithResultsAsync: _Callable[[_type.HSTRING,  # productId
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IPurchaseResults]]],  # requestProductPurchaseWithResultsOperation
                                                      _type.HRESULT]
    RequestProductPurchaseWithDisplayPropertiesAsync: _Callable[[_type.HSTRING,  # productId
                                                                 _type.HSTRING,  # offerId
                                                                 IProductPurchaseDisplayProperties,  # displayProperties
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IPurchaseResults]]],  # requestProductPurchaseWithDisplayPropertiesOperation
                                                                _type.HRESULT]
    GetUnfulfilledConsumablesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUnfulfilledConsumable]]]],  # getUnfulfilledConsumablesOperation
                                              _type.HRESULT]


class ICurrentAppStaticsWithFiltering(_inspectable.IInspectable, factory=True):
    LoadListingInformationByProductIdsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # productIds
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IListingInformation]]],  # loadListingOperation
                                                       _type.HRESULT]
    LoadListingInformationByKeywordsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # keywords
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[IListingInformation]]],  # loadListingOperation
                                                     _type.HRESULT]
    ReportProductFulfillment: _Callable[[_type.HSTRING],  # productId
                                        _type.HRESULT]


class ICurrentAppWithCampaignId(_inspectable.IInspectable, factory=True):
    GetAppPurchaseCampaignIdAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                             _type.HRESULT]


class ICurrentAppWithConsumables(_inspectable.IInspectable, factory=True):
    ReportConsumableFulfillmentAsync: _Callable[[_type.HSTRING,  # productId
                                                 _struct.GUID,  # transactionId
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.Store.FulfillmentResult]]],  # reportConsumableFulfillmentOperation
                                                _type.HRESULT]
    RequestProductPurchaseWithResultsAsync: _Callable[[_type.HSTRING,  # productId
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IPurchaseResults]]],  # requestProductPurchaseWithResultsOperation
                                                      _type.HRESULT]
    RequestProductPurchaseWithDisplayPropertiesAsync: _Callable[[_type.HSTRING,  # productId
                                                                 _type.HSTRING,  # offerId
                                                                 IProductPurchaseDisplayProperties,  # displayProperties
                                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IPurchaseResults]]],  # requestProductPurchaseWithDisplayPropertiesOperation
                                                                _type.HRESULT]
    GetUnfulfilledConsumablesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUnfulfilledConsumable]]]],  # getUnfulfilledConsumablesOperation
                                              _type.HRESULT]


class ILicenseInformation(_inspectable.IInspectable):
    get_ProductLicenses: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IProductLicense]]],  # value
                                   _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_IsTrial: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    add_LicenseChanged: _Callable[[ILicenseChangedEventHandler,  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_LicenseChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]


class IListingInformation(_inspectable.IInspectable):
    get_CurrentMarket: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ProductListings: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IProductListing]]],  # value
                                   _type.HRESULT]
    get_FormattedPrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_AgeRating: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IListingInformation2(_inspectable.IInspectable):
    get_FormattedBasePrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_SaleEndDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    get_IsOnSale: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_CurrencyCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IProductLicense(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_ExpirationDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]


class IProductLicenseWithFulfillment(_inspectable.IInspectable):
    get_IsConsumable: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]


class IProductListing(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_FormattedPrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IProductListing2(_inspectable.IInspectable):
    get_FormattedBasePrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_SaleEndDate: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    get_IsOnSale: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_CurrencyCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IProductListingWithConsumables(_inspectable.IInspectable):
    get_ProductType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.ProductType]],  # value
                               _type.HRESULT]


class IProductListingWithMetadata(_inspectable.IInspectable):
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Keywords: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_ProductType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.ProductType]],  # value
                               _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ImageUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]


class IProductPurchaseDisplayProperties(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Image: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                         _type.HRESULT]
    put_Image: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                         _type.HRESULT]


class IProductPurchaseDisplayPropertiesFactory(_inspectable.IInspectable, factory=True):
    CreateProductPurchaseDisplayProperties: _Callable[[_type.HSTRING,  # name
                                                       _Pointer[IProductPurchaseDisplayProperties]],  # displayProperties
                                                      _type.HRESULT]


class IPurchaseResults(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.ProductPurchaseStatus]],  # value
                          _type.HRESULT]
    get_TransactionId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_ReceiptXml: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_OfferId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IUnfulfilledConsumable(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_TransactionId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    get_OfferId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
