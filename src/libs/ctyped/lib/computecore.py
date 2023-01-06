from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import type as _type
from .._utils import _Pointer

# computecore
HcsGetServiceProperties: _Callable[[_Optional[_type.PCWSTR],
                                    _Pointer[_type.PWSTR]],
                                   _type.HRESULT]
HcsModifyServiceSettings: _Callable[[_type.PCWSTR,
                                     _Optional[_Pointer[_type.PWSTR]]],
                                    _type.HRESULT]
HcsSubmitWerReport: _Callable[[_type.PCWSTR],
                              _type.HRESULT]
HcsCreateEmptyGuestStateFile: _Callable[[_type.PCWSTR],
                                        _type.HRESULT]
HcsCreateEmptyRuntimeStateFile: _Callable[[_type.PCWSTR],
                                          _type.HRESULT]
HcsGrantVmAccess: _Callable[[_type.PCWSTR,
                             _type.PCWSTR],
                            _type.HRESULT]
HcsRevokeVmAccess: _Callable[[_type.PCWSTR,
                              _type.PCWSTR],
                             _type.HRESULT]
HcsGrantVmGroupAccess: _Callable[[_type.PCWSTR],
                                 _type.HRESULT]
HcsRevokeVmGroupAccess: _Callable[[_type.PCWSTR],
                                  _type.HRESULT]

_WinLib(__name__)
