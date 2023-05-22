from __future__ import annotations

from typing import Callable as _Callable

from ... import UserActivities as _Windows_ApplicationModel_UserActivities
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICoreUserActivityManagerStatics(_inspectable.IInspectable, factory=True):
    CreateUserActivitySessionInBackground: _Callable[[_Windows_ApplicationModel_UserActivities.IUserActivity,  # activity
                                                      _Pointer[_Windows_ApplicationModel_UserActivities.IUserActivitySession]],  # result
                                                     _type.HRESULT]
    DeleteUserActivitySessionsInTimeRangeAsync: _Callable[[_Windows_ApplicationModel_UserActivities.IUserActivityChannel,  # channel
                                                           _struct.Windows.Foundation.DateTime,  # startTime
                                                           _struct.Windows.Foundation.DateTime,  # endTime
                                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                          _type.HRESULT]
