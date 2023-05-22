from __future__ import annotations

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IMdmAllowPolicyStatics(_inspectable.IInspectable, factory=True):
    IsBrowserAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    IsCameraAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    IsMicrosoftAccountAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    IsStoreAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IMdmPolicyStatics2(_inspectable.IInspectable, factory=True):
    GetMessagingSyncPolicy: _Callable[[_Pointer[_enum.Windows.Management.Workplace.MessagingSyncPolicy]],  # value
                                      _type.HRESULT]


class IWorkplaceSettingsStatics(_inspectable.IInspectable, factory=True):
    get_IsMicrosoftAccountOptional: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
