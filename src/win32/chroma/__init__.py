from __future__ import annotations as _

import enum
from typing import Callable, Iterable, Optional

from libs import ctyped
from libs.ctyped.lib import RzChromaSDK64

_SUCCESS = ctyped.const.RZRESULT_SUCCESS


class AppType(enum.IntEnum):
    UTILITY = 0x01
    GAME = 0x02


class SupportedDevice(enum.IntFlag):
    KEYBOARD = 0x01
    MOUSE = 0x02
    HEADSET = 0x04
    MOUSEPAD = 0x08
    KEYPAD = 0x10
    CHROMALINK = 0x20


def app_info(title: str, description: str, author_name: str, author_contact: str,
             supported_device: int | Iterable[int | SupportedDevice] = SupportedDevice,
             app_type: int | AppType = AppType.UTILITY) -> ctyped.struct.ChromaSDK.APPINFOTYPE:
    info = ctyped.struct.ChromaSDK.APPINFOTYPE()
    info.Title = title
    info.Description = description
    info.Author.Name = author_name
    info.Author.Contact = author_contact
    if not isinstance(supported_device, Iterable):
        supported_device = supported_device,
    for device in supported_device:
        info.SupportedDevice |= int(device)
    info.Category = int(app_type)
    return info


class App:
    def __init__(self, info: Optional[ctyped.struct.ChromaSDK.APPINFOTYPE] = None):
        self._init = RzChromaSDK64.Init() if info is None else RzChromaSDK64.InitSDK(ctyped.byref(info))

    def __bool__(self):
        return self._init == _SUCCESS

    def __del__(self):
        if self:
            RzChromaSDK64.UnInit()
            self._init = ctyped.const.RZRESULT_NOT_VALID_STATE

    def __enter__(self) -> Optional[App]:
        if self:
            return self

    def __exit__(self, _, __, ___):
        self.__del__()


class Effect:
    def __init__(self, device_id: ctyped.struct.RZDEVICEID,
                 effect_type: ctyped.enum.ChromaSDK.EFFECT_TYPE, param=None):
        self._id = ctyped.struct.RZEFFECTID()
        self._init = RzChromaSDK64.CreateEffect(device_id, effect_type, param, ctyped.byref(self._id))

    def __bool__(self):
        return self._init == _SUCCESS

    def __del__(self):
        if self:
            RzChromaSDK64.DeleteEffect(self._id)
            self._init = ctyped.const.RZRESULT_NOT_VALID_STATE

    def __enter__(self) -> Optional[Effect]:
        if self:
            return self

    def __exit__(self, _, __, ___):
        self.__del__()

    def set(self) -> bool:
        return RzChromaSDK64.SetEffect(self._id) == _SUCCESS


class _DeviceEffect(Effect):
    _create: Callable

    # noinspection PyMissingConstructor
    def __init__(self, effect_type: ctyped.enum.ChromaSDK.EFFECT_TYPE, param=None):
        self._id = ctyped.struct.RZEFFECTID()
        self._init = self._create(effect_type, param, ctyped.byref(self._id))


class KeyboardEffect(_DeviceEffect):
    _create = RzChromaSDK64.CreateKeyboardEffect


class MouseEffect(_DeviceEffect):
    _create = RzChromaSDK64.CreateMouseEffect


class HeadsetEffect(_DeviceEffect):
    _create = RzChromaSDK64.CreateHeadsetEffect


class MousepadEffect(_DeviceEffect):
    _create = RzChromaSDK64.CreateMousepadEffect


class KeypadEffect(_DeviceEffect):
    _create = RzChromaSDK64.CreateKeypadEffect


class ChromaLinkEffect(_DeviceEffect):
    _create = RzChromaSDK64.CreateChromaLinkEffect
