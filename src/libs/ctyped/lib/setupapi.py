from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# SetupAPI
SetupDiCreateDeviceInterfaceA: _Callable[[_type.HDEVINFO,
                                          _Pointer[_struct.SP_DEVINFO_DATA],
                                          _Pointer[_struct.GUID],
                                          _Optional[_type.PCSTR],
                                          _type.DWORD,
                                          _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DATA]]],
                                         _type.BOOL]
SetupDiCreateDeviceInterfaceW: _Callable[[_type.HDEVINFO,
                                          _Pointer[_struct.SP_DEVINFO_DATA],
                                          _Pointer[_struct.GUID],
                                          _Optional[_type.PCWSTR],
                                          _type.DWORD,
                                          _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DATA]]],
                                         _type.BOOL]
SetupDiDestroyDeviceInfoList: _Callable[[_type.HDEVINFO],
                                        _type.BOOL]
SetupDiEnumDeviceInfo: _Callable[[_type.HDEVINFO,
                                  _type.DWORD,
                                  _Pointer[_struct.SP_DEVINFO_DATA]],
                                 _type.BOOL]
SetupDiEnumDeviceInterfaces: _Callable[[_type.HDEVINFO,
                                        _Pointer[_struct.SP_DEVINFO_DATA],
                                        _Optional[_Pointer[_struct.GUID]],
                                        _type.DWORD,
                                        _Pointer[_struct.SP_DEVICE_INTERFACE_DATA]],
                                       _type.BOOL]
SetupDiGetClassDevsA: _Callable[[_Optional[_Pointer[_struct.GUID]],
                                 _Optional[_type.PCSTR],
                                 _Optional[_type.HWND],
                                 _type.DWORD],
                                _type.HDEVINFO]
SetupDiGetClassDevsW: _Callable[[_Optional[_Pointer[_struct.GUID]],
                                 _Optional[_type.PCWSTR],
                                 _Optional[_type.HWND],
                                 _type.DWORD],
                                _type.HDEVINFO]
SetupDiGetDeviceInterfaceDetailA: _Callable[[_type.HDEVINFO,
                                             _Pointer[_struct.SP_DEVICE_INTERFACE_DATA],
                                             _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DETAIL_DATA_A]],
                                             _type.DWORD,
                                             _Optional[_Pointer[_type.DWORD]],
                                             _Optional[_Pointer[_struct.SP_DEVINFO_DATA]]],
                                            _type.BOOL]
SetupDiGetDeviceInterfaceDetailW: _Callable[[_type.HDEVINFO,
                                             _Pointer[_struct.SP_DEVICE_INTERFACE_DATA],
                                             _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DETAIL_DATA_W]],
                                             _type.DWORD,
                                             _Optional[_Pointer[_type.DWORD]],
                                             _Optional[_Pointer[_struct.SP_DEVINFO_DATA]]],
                                            _type.BOOL]
SetupDiGetDevicePropertyW: _Callable[[_type.HDEVINFO,
                                      _Pointer[_struct.SP_DEVINFO_DATA],
                                      _Pointer[_struct.DEVPROPKEY],
                                      _Pointer[_type.DEVPROPTYPE],
                                      _Optional[_type.PBYTE],
                                      _type.DWORD,
                                      _Optional[_Pointer[_type.DWORD]],
                                      _type.DWORD],
                                     _type.BOOL]
SetupDiGetDeviceRegistryPropertyA: _Callable[[_type.HDEVINFO,
                                              _Pointer[_struct.SP_DEVINFO_DATA],
                                              _type.DWORD,
                                              _Optional[_Pointer[_type.DWORD]],
                                              _Optional[_type.PBYTE],
                                              _type.DWORD,
                                              _Optional[_Pointer[_type.DWORD]]],
                                             _type.BOOL]
SetupDiGetDeviceRegistryPropertyW: _Callable[[_type.HDEVINFO,
                                              _Pointer[_struct.SP_DEVINFO_DATA],
                                              _type.DWORD,
                                              _Optional[_Pointer[_type.DWORD]],
                                              _Optional[_type.PBYTE],
                                              _type.DWORD,
                                              _Optional[_Pointer[_type.DWORD]]],
                                             _type.BOOL]

_WinLib(__name__)
