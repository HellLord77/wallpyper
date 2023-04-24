from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ISoundLevelBrokerStatics(_inspectable.IInspectable):
    get_SoundLevel: _Callable[[_Pointer[_enum.Windows.Media.SoundLevel]],  # value
                              _type.HRESULT]
    add_SoundLevelChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SoundLevelChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]

    _factory = True
