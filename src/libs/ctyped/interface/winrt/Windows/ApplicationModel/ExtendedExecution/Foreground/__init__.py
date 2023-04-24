from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IExtendedExecutionForegroundRevokedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundRevokedReason]],  # value
                          _type.HRESULT]


class IExtendedExecutionForegroundSession(_inspectable.IInspectable):
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    add_Revoked: _Callable[[_Windows_Foundation.ITypedEventHandler[_inspectable.IInspectable, IExtendedExecutionForegroundRevokedEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Revoked: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    RequestExtensionAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundResult]]],  # operation
                                     _type.HRESULT]
    get_Reason: _Callable[[_Pointer[_enum.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason]],  # value
                          _type.HRESULT]
    put_Reason: _Callable[[_enum.Windows.ApplicationModel.ExtendedExecution.Foreground.ExtendedExecutionForegroundReason],  # value
                          _type.HRESULT]
