from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class INamedPolicyData(_inspectable.IInspectable):
    get_Area: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Management.Policies.NamedPolicyKind]],  # value
                        _type.HRESULT]
    get_IsManaged: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsUserPolicy: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    GetBoolean: _Callable[[_Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    GetBinary: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # result
                         _type.HRESULT]
    GetInt32: _Callable[[_Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    GetInt64: _Callable[[_Pointer[_type.INT64]],  # result
                        _type.HRESULT]
    GetString: _Callable[[_Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]
    add_Changed: _Callable[[_Windows_Foundation.ITypedEventHandler[INamedPolicyData, _inspectable.IInspectable],  # changedHandler
                            _Pointer[_struct.EventRegistrationToken]],  # cookie
                           _type.HRESULT]
    remove_Changed: _Callable[[_struct.EventRegistrationToken],  # cookie
                              _type.HRESULT]


class INamedPolicyStatics(_inspectable.IInspectable, factory=True):
    GetPolicyFromPath: _Callable[[_type.HSTRING,  # area
                                  _type.HSTRING,  # name
                                  _Pointer[INamedPolicyData]],  # result
                                 _type.HRESULT]
    GetPolicyFromPathForUser: _Callable[[_Windows_System.IUser,  # user
                                         _type.HSTRING,  # area
                                         _type.HSTRING,  # name
                                         _Pointer[INamedPolicyData]],  # result
                                        _type.HRESULT]
