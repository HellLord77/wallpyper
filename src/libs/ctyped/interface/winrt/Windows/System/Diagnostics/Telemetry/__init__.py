from __future__ import annotations

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IPlatformTelemetryClientStatics(_inspectable.IInspectable):
    Register: _Callable[[_type.HSTRING,  # id
                         _Pointer[IPlatformTelemetryRegistrationResult]],  # result
                        _type.HRESULT]
    RegisterWithSettings: _Callable[[_type.HSTRING,  # id
                                     IPlatformTelemetryRegistrationSettings,  # settings
                                     _Pointer[IPlatformTelemetryRegistrationResult]],  # result
                                    _type.HRESULT]

    _factory = True


class IPlatformTelemetryRegistrationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationStatus]],  # value
                          _type.HRESULT]


class IPlatformTelemetryRegistrationSettings(_inspectable.IInspectable):
    get_StorageSize: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_StorageSize: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_UploadQuotaSize: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]
    put_UploadQuotaSize: _Callable[[_type.UINT32],  # value
                                   _type.HRESULT]
