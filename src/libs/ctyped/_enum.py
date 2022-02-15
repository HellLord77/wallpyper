from __future__ import annotations as _

import enum as _enum
import functools as _functools
from typing import Optional as _Optional
from typing import Union as _Union

from . import _type
from .__head__ import _Globals
from .__head__ import _get_annotations

_ASSIGNED = ('__str__', *(assigned for assigned in _functools.WRAPPER_ASSIGNMENTS))


class _Enum(_enum.IntEnum):
    # noinspection PyUnusedLocal
    def __init__(self, value: _Optional[int] = None):
        pass


# noinspection PyPep8Naming
class DESKTOP_SLIDESHOW_OPTIONS(_Enum):
    DSO_SHUFFLEIMAGES: DESKTOP_SLIDESHOW_OPTIONS = 0x1


class AsyncStatus(_Enum):
    Started: AsyncStatus
    Completed: AsyncStatus
    Canceled: AsyncStatus
    Error: AsyncStatus


def _get_members(enum: _Enum) -> dict[int, str]:
    last = -1
    return {(last := int(getattr(enum, name_, last + 1))): name_ for name_ in _get_annotations(enum)}


def _init(name: str) -> type:
    _globals.check_item(name)

    class Wrapper(_type.c_uint):
        _members = _get_members(_globals.vars_[name])

        # noinspection PyMissingConstructor
        def __init__(self, value: _Optional[int] = None):
            if value is None:
                for val in self._members:
                    value = val
                    break
            _type.c_uint.__init__(self, value)

        @property
        def _name_(self) -> _Union[int, str]:
            return self._members.get(self.value, self.value)

    # TODO docs
    return _functools.update_wrapper(Wrapper, _globals.vars_[name], _ASSIGNED, ())


_globals = _Globals()
