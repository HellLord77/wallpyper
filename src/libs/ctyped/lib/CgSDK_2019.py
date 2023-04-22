from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from ..enum import CgSDK as _enum_CgSDK

# CgSDK
CgSdkRequestControl: _Callable[[_enum_CgSDK.CorsairAccessMode],  # accessMode
                               _type.c_bool]
"""
requestes control using specified access mode. By default client has shared
control over lighting so there is no need to call CorsairRequestControl unless
client requires exclusive control
"""
CgSdkPerformProtocolHandshake: _Callable[[],
                                         _struct.CorsairProtocolDetails]
"""
checks file and protocol version of CUE to understand which of SDK functions can
be used with this version of CUE
"""
CgSdkGetLastError: _Callable[[],
                             _enum_CgSDK.CorsairError]
"""
returns last error that occured while using any of Corsair* functions
"""
CgSdkReleaseControl: _Callable[[_enum_CgSDK.CorsairAccessMode],  # accessMode
                               _type.c_bool]
"""
releases previously requested control for specified access mode
"""
CgSdkSetGame: _Callable[[_type.c_char_p],  # gamename
                        _type.c_bool]
CgSdkSetState: _Callable[[_type.c_char_p],  # gamename
                         _type.c_bool]
CgSdkSetStateWithKey: _Callable[[_type.c_char_p],  # gamename
                                _type.c_bool]
CgSdkSetEvent: _Callable[[_type.c_char_p],  # gamename
                         _type.c_bool]
CgSdkSetEventWithKey: _Callable[[_type.c_char_p],  # gamename
                                _type.c_bool]
CgSdkSetProgressBarValue: _Callable[[],
                                    _type.c_bool]
CgSdkShowProgressBar: _Callable[[],
                                _type.c_bool]
CgSdkHideProgressBar: _Callable[[],
                                _type.c_bool]
CgSdkClearState: _Callable[[_type.c_char_p],  # gamename
                           _type.c_bool]
CgSdkClearStateWithKey: _Callable[[_type.c_char_p],  # gamename
                                  _type.c_bool]
CgSdkClearAllStates: _Callable[[],
                               _type.c_bool]
CgSdkClearAllEvents: _Callable[[],
                               _type.c_bool]

_WinLib(__name__, 'CgSDK.x64_2019.dll')
