from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IWalletBarcode(_inspectable.IInspectable):
    Symbology: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Wallet.WalletBarcodeSymbology]],  # value
                         _type.HRESULT]
    Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                     _type.HRESULT]
    GetImageAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # operation
                             _type.HRESULT]


class IWalletBarcodeFactory(_inspectable.IInspectable, factory=True):
    CreateWalletBarcode: _Callable[[_enum.Windows.ApplicationModel.Wallet.WalletBarcodeSymbology,  # symbology
                                    _type.HSTRING,  # value
                                    _Pointer[IWalletBarcode]],  # barcode
                                   _type.HRESULT]
    CreateCustomWalletBarcode: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # streamToBarcodeImage
                                          _Pointer[IWalletBarcode]],  # barcode
                                         _type.HRESULT]


class IWalletItem(_inspectable.IInspectable):
    DisplayName: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                  _type.HRESULT]
    IsAcknowledged: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    IssuerDisplayName: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    LastUpdated: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Wallet.WalletItemKind]],  # value
                    _type.HRESULT]
    Barcode: _Callable[[IWalletBarcode],  # value
                       _type.HRESULT]
    ExpirationDate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                              _type.HRESULT]
    Logo159x159: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                           _type.HRESULT]
    Logo336x336: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                           _type.HRESULT]
    Logo99x99: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                         _type.HRESULT]
    DisplayMessage: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    IsDisplayMessageLaunchable: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    LogoText: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    HeaderColor: _Callable[[_struct.Windows.UI.Color],  # value
                           _type.HRESULT]
    BodyColor: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    HeaderFontColor: _Callable[[_struct.Windows.UI.Color],  # value
                               _type.HRESULT]
    BodyFontColor: _Callable[[_struct.Windows.UI.Color],  # value
                             _type.HRESULT]
    HeaderBackgroundImage: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                                     _type.HRESULT]
    BodyBackgroundImage: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                                   _type.HRESULT]
    LogoImage: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                         _type.HRESULT]
    PromotionalImage: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                                _type.HRESULT]
    RelevantDate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    RelevantDateDisplayMessage: _Callable[[_type.HSTRING],  # value
                                          _type.HRESULT]
    TransactionHistory: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, IWalletTransaction]]],  # value
                                  _type.HRESULT]
    RelevantLocations: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, IWalletRelevantLocation]]],  # value
                                 _type.HRESULT]
    IsMoreTransactionHistoryLaunchable: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    DisplayProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, IWalletItemCustomProperty]]],  # value
                                 _type.HRESULT]
    Verbs: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, IWalletVerb]]],  # value
                     _type.HRESULT]


class IWalletItemCustomProperty(_inspectable.IInspectable):
    Name: _Callable[[_type.HSTRING],  # value
                    _type.HRESULT]
    Value: _Callable[[_type.HSTRING],  # value
                     _type.HRESULT]
    AutoDetectLinks: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    DetailViewPosition: _Callable[[_enum.Windows.ApplicationModel.Wallet.WalletDetailViewPosition],  # value
                                  _type.HRESULT]
    SummaryViewPosition: _Callable[[_enum.Windows.ApplicationModel.Wallet.WalletSummaryViewPosition],  # value
                                   _type.HRESULT]


class IWalletItemCustomPropertyFactory(_inspectable.IInspectable, factory=True):
    CreateWalletItemCustomProperty: _Callable[[_type.HSTRING,  # name
                                               _type.HSTRING,  # value
                                               _Pointer[IWalletItemCustomProperty]],  # walletItemCustomProperty
                                              _type.HRESULT]


class IWalletItemFactory(_inspectable.IInspectable, factory=True):
    CreateWalletItem: _Callable[[_enum.Windows.ApplicationModel.Wallet.WalletItemKind,  # kind
                                 _type.HSTRING,  # displayName
                                 _Pointer[IWalletItem]],  # walletItem
                                _type.HRESULT]


class IWalletItemStore(_inspectable.IInspectable):
    AddAsync: _Callable[[_type.HSTRING,  # id
                         IWalletItem,  # item
                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                        _type.HRESULT]
    ClearAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    GetWalletItemAsync: _Callable[[_type.HSTRING,  # id
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IWalletItem]]],  # operation
                                  _type.HRESULT]
    GetItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IWalletItem]]]],  # operation
                             _type.HRESULT]
    GetItemsWithKindAsync: _Callable[[_enum.Windows.ApplicationModel.Wallet.WalletItemKind,  # kind
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IWalletItem]]]],  # operation
                                     _type.HRESULT]
    ImportItemAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # stream
                                _Pointer[_Windows_Foundation.IAsyncOperation[IWalletItem]]],  # operation
                               _type.HRESULT]
    DeleteAsync: _Callable[[_type.HSTRING,  # id
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    ShowAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                         _type.HRESULT]
    ShowItemAsync: _Callable[[_type.HSTRING,  # id
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                             _type.HRESULT]
    UpdateAsync: _Callable[[IWalletItem,  # item
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]


class IWalletItemStore2(_inspectable.IInspectable):
    ItemsChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                            _type.HRESULT]


class IWalletManagerStatics(_inspectable.IInspectable, factory=True):
    RequestStoreAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IWalletItemStore]]],  # operation
                                 _type.HRESULT]


class IWalletRelevantLocation(_inspectable.IInspectable):
    Position: _Callable[[_struct.Windows.Devices.Geolocation.BasicGeoposition],  # value
                        _type.HRESULT]
    DisplayMessage: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]


class IWalletTransaction(_inspectable.IInspectable):
    Description: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    DisplayAmount: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    IgnoreTimeOfDay: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    DisplayLocation: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    TransactionDate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                               _type.HRESULT]
    IsLaunchable: _Callable[[_type.boolean],  # value
                            _type.HRESULT]


class IWalletVerb(_inspectable.IInspectable):
    Name: _Callable[[_type.HSTRING],  # value
                    _type.HRESULT]


class IWalletVerbFactory(_inspectable.IInspectable, factory=True):
    CreateWalletVerb: _Callable[[_type.HSTRING,  # name
                                 _Pointer[IWalletVerb]],  # WalletVerb
                                _type.HRESULT]
