from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IUserDataAvailabilityStateChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IUserDataBufferUnprotectResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.DataProtection.UserDataBufferUnprotectStatus]],  # value
                          _type.HRESULT]
    get_UnprotectedBuffer: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                                     _type.HRESULT]


class IUserDataProtectionManager(_inspectable.IInspectable):
    ProtectStorageItemAsync: _Callable[[_Windows_Storage.IStorageItem,  # storageItem
                                        _enum.Windows.Security.DataProtection.UserDataAvailability,  # availability
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.DataProtection.UserDataStorageItemProtectionStatus]]],  # result
                                       _type.HRESULT]
    GetStorageItemProtectionInfoAsync: _Callable[[_Windows_Storage.IStorageItem,  # storageItem
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataStorageItemProtectionInfo]]],  # result
                                                 _type.HRESULT]
    ProtectBufferAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # unprotectedBuffer
                                   _enum.Windows.Security.DataProtection.UserDataAvailability,  # availability
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # result
                                  _type.HRESULT]
    UnprotectBufferAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # protectedBuffer
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataBufferUnprotectResult]]],  # result
                                    _type.HRESULT]
    IsContinuedDataAvailabilityExpected: _Callable[[_enum.Windows.Security.DataProtection.UserDataAvailability,  # availability
                                                    _Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    add_DataAvailabilityStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataProtectionManager, IUserDataAvailabilityStateChangedEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_DataAvailabilityStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]


class IUserDataProtectionManagerStatics(_inspectable.IInspectable, factory=True):
    TryGetDefault: _Callable[[_Pointer[IUserDataProtectionManager]],  # result
                             _type.HRESULT]
    TryGetForUser: _Callable[[_Windows_System.IUser,  # user
                              _Pointer[IUserDataProtectionManager]],  # result
                             _type.HRESULT]


class IUserDataStorageItemProtectionInfo(_inspectable.IInspectable):
    get_Availability: _Callable[[_Pointer[_enum.Windows.Security.DataProtection.UserDataAvailability]],  # value
                                _type.HRESULT]
