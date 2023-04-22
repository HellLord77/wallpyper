from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..enum import iCUESDK as _enum_iCUESDK

# iCUESDK
CorsairConnect: _Callable[[_type.CorsairSessionStateChangedHandler,  # onStateChanged
                           _type.c_void_p],  # context
                          _enum_iCUESDK.CorsairError]
"""
sets handler for session state changes, checks versions of SDK client, server
and host (iCUE) to understand which of SDK functions can be used with this
version of iCUE
"""
CorsairGetSessionDetails: _Callable[[_Pointer[_struct.CorsairSessionDetails]],  # details
                                    _enum_iCUESDK.CorsairError]
"""
checks versions of SDK client, server and host (iCUE) to understand which of SDK
functions can be used with this version of iCUE. If there is no active session
or client is not connected to the server, then only client version will be
filled
"""
CorsairDisconnect: _Callable[[],
                             _enum_iCUESDK.CorsairError]
"""
removes handler for session state changes previously set by CorsairConnect
"""
CorsairGetDevices: _Callable[[_Pointer[_struct.CorsairDeviceFilter],  # filter
                              _type.c_int,  # sizeMax
                              _Pointer[_struct.CorsairDeviceInfo],  # devices
                              _Pointer[_type.c_int]],  # size
                             _enum_iCUESDK.CorsairError]
"""
populates the buffer with filtered collection of devices
"""
CorsairGetDeviceInfo: _Callable[[_type.CorsairDeviceId,  # deviceId
                                 _Pointer[_struct.CorsairDeviceInfo]],  # deviceInfo
                                _enum_iCUESDK.CorsairError]
"""
gets information about device specified by deviceId
"""
CorsairGetLedPositions: _Callable[[_type.CorsairDeviceId,  # deviceId
                                   _type.c_int,  # sizeMax
                                   _Pointer[_struct.CorsairLedPosition],  # ledPositions
                                   _Pointer[_type.c_int]],  # size
                                  _enum_iCUESDK.CorsairError]
"""
provides a list of supported device LEDs by its id with their positions.
Position could be either physical (only device-dependent) or logical (depend on
device as well as iCUE settings)
"""
CorsairSubscribeForEvents: _Callable[[_type.CorsairEventHandler,  # onEvent
                                      _type.c_void_p],  # context
                                     _enum_iCUESDK.CorsairError]
"""
registers a callback that will be called by SDK when some event happened. If
client is already subscribed but calls this function again SDK should use only
last callback registered for sending notifications
"""
CorsairUnsubscribeFromEvents: _Callable[[],
                                        _enum_iCUESDK.CorsairError]
"""
unregisters callback previously registered by CorsairSubscribeForEvents call
"""
CorsairConfigureKeyEvent: _Callable[[_type.CorsairDeviceId,  # deviceId
                                     _Pointer[_struct.CorsairKeyEventConfiguration]],  # config
                                    _enum_iCUESDK.CorsairError]
"""
this function gives possibility for a client with ExclusiveKeyEventsListening or
ExclusiveLightingControlAndKeyEventsListening access level to control selected
set of macro keys only and let iCUE to pass some key events to other shared
clients
"""
CorsairGetDevicePropertyInfo: _Callable[[_type.CorsairDeviceId,  # deviceId
                                         _enum_iCUESDK.CorsairDevicePropertyId,  # propertyId
                                         _type.c_uint,  # index
                                         _Pointer[_enum_iCUESDK.CorsairDataType],  # dataType
                                         _Pointer[_type.c_uint]],  # flags
                                        _enum_iCUESDK.CorsairError]
"""
gets information about device property for the device specified by deviceId
"""
CorsairReadDeviceProperty: _Callable[[_type.CorsairDeviceId,  # deviceId
                                      _enum_iCUESDK.CorsairDevicePropertyId,  # propertyId
                                      _type.c_uint,  # index
                                      _Pointer[_struct.CorsairProperty]],  # property
                                     _enum_iCUESDK.CorsairError]
"""
gets the data of device property by device identifier, property identifier and
property index
"""
CorsairWriteDeviceProperty: _Callable[[_type.CorsairDeviceId,  # deviceId
                                       _enum_iCUESDK.CorsairDevicePropertyId,  # propertyId
                                       _type.c_uint,  # index
                                       _Pointer[_struct.CorsairProperty]],  # property
                                      _enum_iCUESDK.CorsairError]
"""
sets the data of device property by device identifier, property identifier and
property index. Can be called only with writable properties
"""
CorsairFreeProperty: _Callable[[_Pointer[_struct.CorsairProperty]],  # property
                               _enum_iCUESDK.CorsairError]
"""
frees memory occupied by CorsairProperty instance
"""
CorsairSetLedColors: _Callable[[_type.CorsairDeviceId,  # deviceId
                                _type.c_int,  # size
                                _Pointer[_struct.CorsairLedColor]],  # ledColors
                               _enum_iCUESDK.CorsairError]
"""
sets specified LEDs to some colors. The color is retained until changed by
successive calls. This function does not take logical layout into account. This
function executes synchronously, if you are concerned about delays consider
using CorsairSetLedColorsBuffer together with
CorsairSetLedColorsFlushBufferAsync
"""
CorsairSetLedColorsBuffer: _Callable[[_type.CorsairDeviceId,  # deviceId
                                      _type.c_int,  # size
                                      _Pointer[_struct.CorsairLedColor]],  # ledColors
                                     _enum_iCUESDK.CorsairError]
"""
sets specified LEDs to some colors. This function sets LEDs colors in the buffer
which is written to the devices via CorsairSetLedColorsFlushBufferAsync. Typical
usecase is next: CorsairSetLedColorsFlushBufferAsync is called to write LEDs
colors to the device and follows after one or more calls of
CorsairSetLedColorsBuffer to set the LEDs buffer. This function does not take
logical layout into account
"""
CorsairSetLedColorsFlushBufferAsync: _Callable[[_type.CorsairAsyncCallback,  # callback
                                                _type.c_void_p],  # context
                                               _enum_iCUESDK.CorsairError]
"""
writes to the devices LEDs colors buffer which is previously filled by the
CorsairSetLedColorsBuffer function. This function executes asynchronously and
returns control to the caller immediately
"""
CorsairGetLedColors: _Callable[[_type.CorsairDeviceId,  # deviceId
                                _type.c_int,  # size
                                _Pointer[_struct.CorsairLedColor]],  # ledColors
                               _enum_iCUESDK.CorsairError]
"""
get current color for the list of requested LEDs of supported device. The color
should represent the actual state of the hardware LED, which could be a
combination of SDK and/or iCUE input
"""
CorsairSetLayerPriority: _Callable[[_type.c_uint],  # priority
                                   _enum_iCUESDK.CorsairError]
"""
set layer priority for this shared client. By default iCUE has priority of 127
and all shared clients have priority of 128 if they don’t call this function.
Layers with higher priority value are shown on top of layers with lower priority
"""
CorsairGetLedLuidForKeyName: _Callable[[_type.CorsairDeviceId,  # deviceId
                                        _type.c_char,  # keyName
                                        _Pointer[_type.CorsairLedLuid]],  # ledId
                                       _enum_iCUESDK.CorsairError]
"""
retrieves LED luid for key name taking logical layout into account. So on AZERTY
keyboards if user calls CorsairGetLedLuidForKeyName(‘A’, &luid) he gets luid
with CLK_Q code. This luid can be used in CorsairSetLedColors or
CorsairSetLedColorsBuffer function
"""
CorsairRequestControl: _Callable[[_type.CorsairDeviceId,  # deviceId
                                  _enum_iCUESDK.CorsairAccessLevel],  # accessLevel
                                 _enum_iCUESDK.CorsairError]
"""
requests control using specified access level. By default client has shared
control over lighting and events so there is no need to call
CorsairRequestControl() unless client requires exclusive control
"""
CorsairReleaseControl: _Callable[[_type.CorsairDeviceId],  # deviceId
                                 _enum_iCUESDK.CorsairError]
"""
releases previously requested control for specified device. This action resets
access level to default (shared)
"""

_WinLib(__name__, 'iCUESDK{}_2019.dll', arg_64='.x64')
