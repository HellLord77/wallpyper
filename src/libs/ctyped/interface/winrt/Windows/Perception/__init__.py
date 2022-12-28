from __future__ import annotations as _

from typing import Callable as _Callable

from ... import inspectable as _inspectable
from ..... import struct as _struct
from ..... import type as _type
from ....._utils import _Pointer


class IPerceptionTimestamp(_inspectable.IInspectable):
    get_TargetTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                              _type.HRESULT]
    get_PredictionAmount: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                    _type.HRESULT]


class IPerceptionTimestamp2(_inspectable.IInspectable):
    get_SystemRelativeTargetTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                            _type.HRESULT]


class IPerceptionTimestampHelperStatics(_inspectable.IInspectable):
    FromHistoricalTargetTime: _Callable[[_struct.Windows.Foundation.DateTime,  # targetTime
                                         _Pointer[IPerceptionTimestamp]],  # value
                                        _type.HRESULT]

    _factory = True


class IPerceptionTimestampHelperStatics2(_inspectable.IInspectable):
    FromSystemRelativeTargetTime: _Callable[[_struct.Windows.Foundation.TimeSpan,  # targetTime
                                             _Pointer[IPerceptionTimestamp]],  # value
                                            _type.HRESULT]

    _factory = True
