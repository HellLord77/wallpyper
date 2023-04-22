import ntpath
import os
import threading
from typing import Optional

from libs import ctyped
from libs.ctyped.const import iCUESDK as const_iCUESDK
from libs.ctyped.enum import iCUESDK as enum_iCUESDK
from libs.ctyped.lib import iCUESDK_x64_2019

_SUCCESS = enum_iCUESDK.CorsairError.Success
_STATE = enum_iCUESDK.CorsairSessionState.Invalid
_LOCK = threading.Lock()
_CONNECTED = threading.Event()


@ctyped.type.CorsairSessionStateChangedHandler
def _session_changed_handler(_: ctyped.type.c_void_p, changed: ctyped.Pointer[ctyped.struct.CorsairSessionStateChanged]):
    global _STATE
    _STATE = changed.contents.state
    if _STATE != enum_iCUESDK.CorsairSessionState.Connecting:
        _CONNECTED.set()


def connect(timeout: Optional[int] = None) -> bool:
    with _LOCK:
        _CONNECTED.clear()
        if iCUESDK_x64_2019.CorsairConnect(_session_changed_handler, None) == _SUCCESS:
            _CONNECTED.wait(timeout)
    return _STATE == enum_iCUESDK.CorsairSessionState.Connected


def disconnect() -> bool:
    return iCUESDK_x64_2019.CorsairDisconnect() == _SUCCESS


# noinspection PyShadowingBuiltins
def get_devices(filter: enum_iCUESDK.CorsairDeviceType = enum_iCUESDK.CorsairDeviceType.All,
                max: ctyped.type.c_int = const_iCUESDK.CORSAIR_DEVICE_COUNT_MAX) -> Optional[list[ctyped.struct.CorsairDeviceInfo]]:
    devices = ctyped.array(type=ctyped.struct.CorsairDeviceInfo, size=max)
    size = ctyped.type.c_int()
    if iCUESDK_x64_2019.CorsairGetDevices(ctyped.byref(ctyped.struct.CorsairDeviceFilter(
            filter)), max, devices, ctyped.byref(size)) == _SUCCESS:
        return devices[:size.value]


os.add_dll_directory(ntpath.join(ntpath.dirname(__file__)))
