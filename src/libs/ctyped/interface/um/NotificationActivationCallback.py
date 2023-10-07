from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class INotificationActivationCallback(_Unknwnbase.IUnknown):
    Activate: _Callable[[_type.LPCWSTR,  # appUserModelId
                         _type.LPCWSTR,  # invokedArgs
                         _Pointer[_struct.NOTIFICATION_USER_INPUT_DATA],  # data
                         _type.ULONG],  # count
                        _type.HRESULT]
