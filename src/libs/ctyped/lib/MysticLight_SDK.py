from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# MysticLight_Test(C++)
MLAPI_Initialize: _Callable[[],
                            _type.c_int]
"""
This function initializes the APIs.
"""
MLAPI_Release: _Callable[[],
                         _type.c_int]
"""
This function release the APIs
"""
MLAPI_GetDeviceInfo: _Callable[[_Pointer[_Pointer[_struct.SAFEARRAY]],  # pDevType
                                _Pointer[_Pointer[_struct.SAFEARRAY]]],  # pLedCount
                               _type.c_int]
"""
This function retrieves information of all devices.
"""
MLAPI_GetDeviceName: _Callable[[_type.BSTR,  # type
                                _Pointer[_Pointer[_struct.SAFEARRAY]]],  # pDevName
                               _type.c_int]
"""
This function retrieves the friendly name of specific device.
"""
MLAPI_GetDeviceNameEx: _Callable[[_type.BSTR,  # type
                                  _type.DWORD,  # index
                                  _Pointer[_type.BSTR]],  # pDevName
                                 _type.c_int]
"""
This function retrieves the friendly name of specific device.
"""
MLAPI_GetErrorMessage: _Callable[[_type.c_int,  # ErrorCode
                                  _Pointer[_type.BSTR]],  # pDesc
                                 _type.c_int]
"""
This function converts a MLAPI error code into general string.
"""
MLAPI_GetLedName: _Callable[[_type.BSTR,  # type
                             _Pointer[_Pointer[_struct.SAFEARRAY]]],  # pLedName
                            _type.c_int]
"""
This function retrieves the all LED name of specific device.
"""
MLAPI_GetLedInfo: _Callable[[_type.BSTR,  # type
                             _type.DWORD,  # index
                             _Pointer[_type.BSTR],  # pName
                             _Pointer[_Pointer[_struct.SAFEARRAY]]],  # pLedStyles
                            _type.c_int]
"""
This function retrieves the LED display name and enumerate the LED styles.
"""
MLAPI_GetLedColor: _Callable[[_type.BSTR,  # type
                              _type.DWORD,  # index
                              _Pointer[_type.DWORD],  # R
                              _Pointer[_type.DWORD],  # G
                              _Pointer[_type.DWORD]],  # B
                             _type.c_int]
"""
This function retrieves the specific LED current color.
"""
MLAPI_GetLedStyle: _Callable[[_type.BSTR,  # type
                              _type.DWORD,  # index
                              _Pointer[_type.BSTR]],  # style
                             _type.c_int]
"""
This function retrieves the specific LED current style.
"""
MLAPI_GetLedMaxBright: _Callable[[_type.BSTR,  # type
                                  _type.DWORD,  # index
                                  _Pointer[_type.DWORD]],  # maxLevel
                                 _type.c_int]
"""
This function retrieves a specific LED supports the maximum brightness level.
"""
MLAPI_GetLedBright: _Callable[[_type.BSTR,  # type
                               _type.DWORD,  # index
                               _Pointer[_type.DWORD]],  # currentLevel
                              _type.c_int]
"""
This function retrieves the specific LED current brightness level.
"""
MLAPI_GetLedMaxSpeed: _Callable[[_type.BSTR,  # type
                                 _type.DWORD,  # index
                                 _Pointer[_type.DWORD]],  # maxLevel
                                _type.c_int]
"""
This function retrieves a specific LED supports the maximum speed level.
"""
MLAPI_GetLedSpeed: _Callable[[_type.BSTR,  # type
                              _type.DWORD,  # index
                              _Pointer[_type.DWORD]],  # currentLevel
                             _type.c_int]
"""
This function retrieves the specific LED current speed level.
"""
MLAPI_SetLedColor: _Callable[[_type.BSTR,  # type
                              _type.DWORD,  # index
                              _type.DWORD,  # R
                              _type.DWORD,  # G
                              _type.DWORD],  # B
                             _type.c_int]
"""
This function sets the LED to a specific color.
"""
MLAPI_SetLedColors: _Callable[[_type.BSTR,  # type
                               _type.DWORD,  # AreaIndex
                               _Pointer[_Pointer[_struct.SAFEARRAY]],  # pLedName
                               _type.DWORD,  # R
                               _type.DWORD,  # G
                               _type.DWORD],  # B
                              _type.c_int]
"""
This function sets the colors for each individual LED within LED area by its 
name.
"""
LPMLAPI_SetLedColorEx: _Callable[[_type.BSTR,  # type
                                  _type.DWORD,  # AreaIndex
                                  _type.BSTR,  # pLedName
                                  _type.DWORD,  # R
                                  _type.DWORD,  # G
                                  _type.DWORD,  # B
                                  _type.DWORD],
                                 _type.c_int]
"""
This function sets the colors for each individual LED within LED area by its 
name.
"""
MLAPI_SetLedColorSync: _Callable[[_type.BSTR,  # type
                                  _type.DWORD,  # AreaIndex
                                  _type.BSTR,  # pLedName
                                  _type.DWORD,  # R
                                  _type.DWORD,  # G
                                  _type.DWORD,  # B
                                  _type.DWORD],
                                 _type.c_int]
"""
This function sets the colors for each individual LED within LED area by its 
name.
"""
MLAPI_SetLedStyle: _Callable[[_type.BSTR,  # type
                              _type.DWORD,  # index
                              _type.BSTR],  # style
                             _type.c_int]
"""
This function sets the LED to a specific style.
"""
MLAPI_SetLedBright: _Callable[[_type.BSTR,  # type
                               _type.DWORD,  # index
                               _type.DWORD],  # level
                              _type.c_int]
"""
This function sets the LED brightness to a specific level.
"""
MLAPI_SetLedSpeed: _Callable[[_type.BSTR,  # type
                              _type.DWORD,  # index
                              _type.DWORD],  # level
                             _type.c_int]
"""
This function sets the LED blink speed to a specific level.
"""
MLAPI_MysticLightControlNotify: _Callable[[_type.CallbackDelegate],
                                          _type.c_int]
"""
This function register Mystic Light controlling notification.
"""
MLAPI_SetLedColorsSync: _Callable[[_type.BSTR,  # type
                                   _type.DWORD,  # R
                                   _type.DWORD,  # G
                                   _type.DWORD],  # B
                                  _type.c_int]
"""
This function sets the colors for each individual LED within LED area by its 
name.
"""

_WinLib(__name__, 'MysticLight_SDK{}', arg_64='_x64')
