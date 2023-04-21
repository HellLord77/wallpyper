from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

Init: _Callable[[],
                _type.RZRESULT]
InitSDK: _Callable[[_Pointer[_struct.ChromaSDK.APPINFOTYPE]],  # pAppInfo
                   _type.RZRESULT]
UnInit: _Callable[[],
                  _type.RZRESULT]
CreateEffect: _Callable[[_struct.RZDEVICEID,  # DeviceId
                         _enum.ChromaSDK.EFFECT_TYPE,  # Effect
                         _type.PRZPARAM,  # pParam
                         _Pointer[_struct.RZEFFECTID]],  # pEffectId
                        _type.RZRESULT]
CreateKeyboardEffect: _Callable[[_enum.ChromaSDK.Keyboard.EFFECT_TYPE,  # Effect
                                 _type.PRZPARAM,  # pParam
                                 _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                _type.RZRESULT]
CreateMouseEffect: _Callable[[_enum.ChromaSDK.Mouse.EFFECT_TYPE,  # Effect
                              _type.PRZPARAM,  # pParam
                              _Pointer[_struct.RZEFFECTID]],  # pEffectId
                             _type.RZRESULT]
CreateHeadsetEffect: _Callable[[_enum.ChromaSDK.Headset.EFFECT_TYPE,  # Effect
                                _type.PRZPARAM,  # pParam
                                _Pointer[_struct.RZEFFECTID]],  # pEffectId
                               _type.RZRESULT]
CreateMousepadEffect: _Callable[[_enum.ChromaSDK.Mousepad.EFFECT_TYPE,  # Effect
                                 _type.PRZPARAM,  # pParam
                                 _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                _type.RZRESULT]
CreateKeypadEffect: _Callable[[_enum.ChromaSDK.Keypad.EFFECT_TYPE,  # Effect
                               _type.PRZPARAM,  # pParam
                               _Pointer[_struct.RZEFFECTID]],  # pEffectId
                              _type.RZRESULT]
CreateChromaLinkEffect: _Callable[[_enum.ChromaSDK.ChromaLink.EFFECT_TYPE,  # Effect
                                   _type.PRZPARAM,  # pParam
                                   _Pointer[_struct.RZEFFECTID]],  # pEffectId
                                  _type.RZRESULT]
DeleteEffect: _Callable[[_struct.RZEFFECTID],  # EffectId
                        _type.RZRESULT]
SetEffect: _Callable[[_struct.RZEFFECTID],  # EffectId
                     _type.RZRESULT]
RegisterEventNotification: _Callable[[_type.HWND],  # hWnd
                                     _type.RZRESULT]
UnregisterEventNotification: _Callable[[],  # hWnd
                                       _type.RZRESULT]
QueryDevice: _Callable[[_struct.RZDEVICEID,  # DeviceId
                        _Pointer[_struct.ChromaSDK.DEVICE_INFO_TYPE]],  # DeviceInfo
                       _type.RZRESULT]

_WinLib(__name__)
