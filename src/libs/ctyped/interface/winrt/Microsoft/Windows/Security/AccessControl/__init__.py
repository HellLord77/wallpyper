from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISecurityDescriptorHelpersStatics(_inspectable.IInspectable, factory=True):
    GetSddlForAppContainerNames: _Callable[[_type.UINT32,  # __accessRequestsSize
                                            _Pointer[_struct.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess],  # accessRequests
                                            _type.HSTRING,  # principalStringSid
                                            _type.UINT32,  # principalAccessMask
                                            _Pointer[_type.HSTRING]],  # result
                                           _type.HRESULT]
    GetSecurityDescriptorBytesFromAppContainerNames: _Callable[[_type.UINT32,  # __accessRequestsSize
                                                                _Pointer[_struct.Microsoft.Windows.Security.AccessControl.AppContainerNameAndAccess],  # accessRequests
                                                                _type.HSTRING,  # principalStringSid
                                                                _type.UINT32,  # principalAccessMask
                                                                _Pointer[_type.UINT32],  # __resultSize
                                                                _Pointer[_Pointer[_type.BYTE]]],  # result
                                                               _type.HRESULT]
