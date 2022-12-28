from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IItemRemovedEventArgs(_inspectable.IInspectable):
    get_RemovedEntry: _Callable[[_Pointer[_struct.Windows.Storage.AccessCache.AccessListEntry]],  # value
                                _type.HRESULT]


class IStorageApplicationPermissionsStatics(_inspectable.IInspectable):
    get_FutureAccessList: _Callable[[_Pointer[IStorageItemAccessList]],  # value
                                    _type.HRESULT]
    get_MostRecentlyUsedList: _Callable[[_Pointer[IStorageItemMostRecentlyUsedList]],  # value
                                        _type.HRESULT]

    _factory = True


class IStorageApplicationPermissionsStatics2(_inspectable.IInspectable):
    GetFutureAccessListForUser: _Callable[[_Windows_System.IUser,  # user
                                           _Pointer[IStorageItemAccessList]],  # value
                                          _type.HRESULT]
    GetMostRecentlyUsedListForUser: _Callable[[_Windows_System.IUser,  # user
                                               _Pointer[IStorageItemMostRecentlyUsedList]],  # value
                                              _type.HRESULT]

    _factory = True


class IStorageItemAccessList(_inspectable.IInspectable):
    AddOverloadDefaultMetadata: _Callable[[_Windows_Storage.IStorageItem,  # file
                                           _Pointer[_type.HSTRING]],  # token
                                          _type.HRESULT]
    Add: _Callable[[_Windows_Storage.IStorageItem,  # file
                    _type.HSTRING,  # metadata
                    _Pointer[_type.HSTRING]],  # token
                   _type.HRESULT]
    AddOrReplaceOverloadDefaultMetadata: _Callable[[_type.HSTRING,  # token
                                                    _Windows_Storage.IStorageItem],  # file
                                                   _type.HRESULT]
    AddOrReplace: _Callable[[_type.HSTRING,  # token
                             _Windows_Storage.IStorageItem,  # file
                             _type.HSTRING],  # metadata
                            _type.HRESULT]
    GetItemAsync: _Callable[[_type.HSTRING,  # token
                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageItem]]],  # operation
                            _type.HRESULT]
    GetFileAsync: _Callable[[_type.HSTRING,  # token
                             _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                            _type.HRESULT]
    GetFolderAsync: _Callable[[_type.HSTRING,  # token
                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFolder]]],  # operation
                              _type.HRESULT]
    GetItemWithOptionsAsync: _Callable[[_type.HSTRING,  # token
                                        _enum.Windows.Storage.AccessCache.AccessCacheOptions,  # options
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageItem]]],  # operation
                                       _type.HRESULT]
    GetFileWithOptionsAsync: _Callable[[_type.HSTRING,  # token
                                        _enum.Windows.Storage.AccessCache.AccessCacheOptions,  # options
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                       _type.HRESULT]
    GetFolderWithOptionsAsync: _Callable[[_type.HSTRING,  # token
                                          _enum.Windows.Storage.AccessCache.AccessCacheOptions,  # options
                                          _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFolder]]],  # operation
                                         _type.HRESULT]
    Remove: _Callable[[_type.HSTRING],  # token
                      _type.HRESULT]
    ContainsItem: _Callable[[_type.HSTRING,  # token
                             _Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    CheckAccess: _Callable[[_Windows_Storage.IStorageItem,  # file
                            _Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Entries: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Storage.AccessCache.AccessListEntry]]],  # entries
                           _type.HRESULT]
    get_MaximumItemsAllowed: _Callable[[_Pointer[_type.UINT32]],  # value
                                       _type.HRESULT]


class IStorageItemMostRecentlyUsedList(_inspectable.IInspectable):
    add_ItemRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IStorageItemMostRecentlyUsedList, IItemRemovedEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                               _type.HRESULT]
    remove_ItemRemoved: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                  _type.HRESULT]


class IStorageItemMostRecentlyUsedList2(_inspectable.IInspectable):
    AddWithMetadataAndVisibility: _Callable[[_Windows_Storage.IStorageItem,  # file
                                             _type.HSTRING,  # metadata
                                             _enum.Windows.Storage.AccessCache.RecentStorageItemVisibility,  # visibility
                                             _Pointer[_type.HSTRING]],  # token
                                            _type.HRESULT]
    AddOrReplaceWithMetadataAndVisibility: _Callable[[_type.HSTRING,  # token
                                                      _Windows_Storage.IStorageItem,  # file
                                                      _type.HSTRING,  # metadata
                                                      _enum.Windows.Storage.AccessCache.RecentStorageItemVisibility],  # visibility
                                                     _type.HRESULT]
