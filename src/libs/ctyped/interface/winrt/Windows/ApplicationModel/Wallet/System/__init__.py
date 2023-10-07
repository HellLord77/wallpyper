from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Wallet as _Windows_ApplicationModel_Wallet
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IWalletItemSystemStore(_inspectable.IInspectable):
    GetItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Wallet.IWalletItem]]]],  # operation
                             _type.HRESULT]
    DeleteAsync: _Callable[[_Windows_ApplicationModel_Wallet.IWalletItem,  # item
                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                           _type.HRESULT]
    ImportItemAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # stream
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_ApplicationModel_Wallet.IWalletItem]]],  # operation
                               _type.HRESULT]
    GetAppStatusForItem: _Callable[[_Windows_ApplicationModel_Wallet.IWalletItem,  # item
                                    _Pointer[_enum.Windows.ApplicationModel.Wallet.System.WalletItemAppAssociation]],  # result
                                   _type.HRESULT]
    LaunchAppForItemAsync: _Callable[[_Windows_ApplicationModel_Wallet.IWalletItem,  # item
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]


class IWalletItemSystemStore2(_inspectable.IInspectable):
    ItemsChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                            _type.HRESULT]


class IWalletManagerSystemStatics(_inspectable.IInspectable, factory=True):
    RequestStoreAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IWalletItemSystemStore]]],  # operation
                                 _type.HRESULT]
