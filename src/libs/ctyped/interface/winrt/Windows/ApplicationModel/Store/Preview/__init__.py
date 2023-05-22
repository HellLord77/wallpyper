from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import System as _Windows_System
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Security import Credentials as _Windows_Security_Credentials
from ....Security.Authentication.Web import Core as _Windows_Security_Authentication_Web_Core
from ....Storage import Streams as _Windows_Storage_Streams
from ....UI import Xaml as _Windows_UI_Xaml
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDeliveryOptimizationSettings(_inspectable.IInspectable):
    get_DownloadMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadMode]],  # value
                                _type.HRESULT]
    get_DownloadModeSource: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.DeliveryOptimizationDownloadModeSource]],  # value
                                      _type.HRESULT]


class IDeliveryOptimizationSettingsStatics(_inspectable.IInspectable, factory=True):
    GetCurrentSettings: _Callable[[_Pointer[IDeliveryOptimizationSettings]],  # result
                                  _type.HRESULT]


class IStoreConfigurationStatics(_inspectable.IInspectable, factory=True):
    SetSystemConfiguration: _Callable[[_type.HSTRING,  # catalogHardwareManufacturerId
                                       _type.HSTRING,  # catalogStoreContentModifierId
                                       _struct.Windows.Foundation.DateTime,  # systemConfigurationExpiration
                                       _type.HSTRING],  # catalogHardwareDescriptor
                                      _type.HRESULT]
    SetMobileOperatorConfiguration: _Callable[[_type.HSTRING,  # mobileOperatorId
                                               _type.UINT32,  # appDownloadLimitInMegabytes
                                               _type.UINT32],  # updateDownloadLimitInMegabytes
                                              _type.HRESULT]
    SetStoreWebAccountId: _Callable[[_type.HSTRING],  # webAccountId
                                    _type.HRESULT]
    IsStoreWebAccountId: _Callable[[_type.HSTRING,  # webAccountId
                                    _Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_HardwareManufacturerInfo: _Callable[[_Pointer[IStoreHardwareManufacturerInfo]],  # value
                                            _type.HRESULT]
    FilterUnsupportedSystemFeaturesAsync: _Callable[[_Windows_Foundation_Collections.IIterable[_enum.Windows.ApplicationModel.Store.Preview.StoreSystemFeature],  # systemFeatures
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_enum.Windows.ApplicationModel.Store.Preview.StoreSystemFeature]]]],  # operation
                                                    _type.HRESULT]


class IStoreConfigurationStatics2(_inspectable.IInspectable, factory=True):
    get_PurchasePromptingPolicy: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                           _type.HRESULT]
    put_PurchasePromptingPolicy: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                                           _type.HRESULT]


class IStoreConfigurationStatics3(_inspectable.IInspectable, factory=True):
    HasStoreWebAccount: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    HasStoreWebAccountForUser: _Callable[[_Windows_System.IUser,  # user
                                          _Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    GetStoreLogDataAsync: _Callable[[_enum.Windows.ApplicationModel.Store.Preview.StoreLogOptions,  # options
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # operation
                                    _type.HRESULT]
    SetStoreWebAccountIdForUser: _Callable[[_Windows_System.IUser,  # user
                                            _type.HSTRING],  # webAccountId
                                           _type.HRESULT]
    IsStoreWebAccountIdForUser: _Callable[[_Windows_System.IUser,  # user
                                           _type.HSTRING,  # webAccountId
                                           _Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    GetPurchasePromptingPolicyForUser: _Callable[[_Windows_System.IUser,  # user
                                                  _Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                                                 _type.HRESULT]
    SetPurchasePromptingPolicyForUser: _Callable[[_Windows_System.IUser,  # user
                                                  _Windows_Foundation.IReference[_type.UINT32]],  # value
                                                 _type.HRESULT]


class IStoreConfigurationStatics4(_inspectable.IInspectable, factory=True):
    GetStoreWebAccountId: _Callable[[_Pointer[_type.HSTRING]],  # result
                                    _type.HRESULT]
    GetStoreWebAccountIdForUser: _Callable[[_Windows_System.IUser,  # user
                                            _Pointer[_type.HSTRING]],  # result
                                           _type.HRESULT]
    SetEnterpriseStoreWebAccountId: _Callable[[_type.HSTRING],  # webAccountId
                                              _type.HRESULT]
    SetEnterpriseStoreWebAccountIdForUser: _Callable[[_Windows_System.IUser,  # user
                                                      _type.HSTRING],  # webAccountId
                                                     _type.HRESULT]
    GetEnterpriseStoreWebAccountId: _Callable[[_Pointer[_type.HSTRING]],  # result
                                              _type.HRESULT]
    GetEnterpriseStoreWebAccountIdForUser: _Callable[[_Windows_System.IUser,  # user
                                                      _Pointer[_type.HSTRING]],  # result
                                                     _type.HRESULT]
    ShouldRestrictToEnterpriseStoreOnly: _Callable[[_Pointer[_type.boolean]],  # result
                                                   _type.HRESULT]
    ShouldRestrictToEnterpriseStoreOnlyForUser: _Callable[[_Windows_System.IUser,  # user
                                                           _Pointer[_type.boolean]],  # result
                                                          _type.HRESULT]


class IStoreConfigurationStatics5(_inspectable.IInspectable, factory=True):
    IsPinToDesktopSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    IsPinToTaskbarSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    IsPinToStartSupported: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    PinToDesktop: _Callable[[_type.HSTRING],  # appPackageFamilyName
                            _type.HRESULT]
    PinToDesktopForUser: _Callable[[_Windows_System.IUser,  # user
                                    _type.HSTRING],  # appPackageFamilyName
                                   _type.HRESULT]


class IStoreHardwareManufacturerInfo(_inspectable.IInspectable):
    get_HardwareManufacturerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_StoreContentModifierId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_ModelName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ManufacturerName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IStorePreview(_inspectable.IInspectable, factory=True):
    RequestProductPurchaseByProductIdAndSkuIdAsync: _Callable[[_type.HSTRING,  # productId
                                                               _type.HSTRING,  # skuId
                                                               _Pointer[_Windows_Foundation.IAsyncOperation[IStorePreviewPurchaseResults]]],  # requestPurchaseBySkuIdOperation
                                                              _type.HRESULT]
    LoadAddOnProductInfosAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IStorePreviewProductInfo]]]],  # loadAddOnProductInfosOperation
                                          _type.HRESULT]


class IStorePreviewProductInfo(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ProductType: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_SkuInfoList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IStorePreviewSkuInfo]]],  # value
                               _type.HRESULT]


class IStorePreviewPurchaseResults(_inspectable.IInspectable):
    get_ProductPurchaseStatus: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Store.Preview.StorePreviewProductPurchaseStatus]],  # value
                                         _type.HRESULT]


class IStorePreviewSkuInfo(_inspectable.IInspectable):
    get_ProductId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_SkuId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_SkuType: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_CustomDeveloperData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_CurrencyCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_FormattedListPrice: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_ExtendedData: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IWebAuthenticationCoreManagerHelper(_inspectable.IInspectable, factory=True):
    RequestTokenWithUIElementHostingAsync: _Callable[[_Windows_Security_Authentication_Web_Core.IWebTokenRequest,  # request
                                                      _Windows_UI_Xaml.IUIElement,  # uiElement
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Authentication_Web_Core.IWebTokenRequestResult]]],  # asyncInfo
                                                     _type.HRESULT]
    RequestTokenWithUIElementHostingAndWebAccountAsync: _Callable[[_Windows_Security_Authentication_Web_Core.IWebTokenRequest,  # request
                                                                   _Windows_Security_Credentials.IWebAccount,  # webAccount
                                                                   _Windows_UI_Xaml.IUIElement,  # uiElement
                                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Security_Authentication_Web_Core.IWebTokenRequestResult]]],  # asyncInfo
                                                                  _type.HRESULT]
