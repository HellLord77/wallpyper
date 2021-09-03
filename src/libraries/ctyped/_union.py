import ctypes as _ctypes
import dataclasses as _dataclasses
import functools as _functools
import typing as _typing

from . import __head__
from . import _type


# noinspection PyPep8Naming
@_dataclasses.dataclass
class u:
    uTimeout: _type.UINT = None
    uVersion: _type.UINT = None


def _init(name: str) -> type[_ctypes.Union]:
    _globals.has_item(name)

    class Wrapper(_ctypes.Union):
        _fields_ = tuple((name_, __head__.resolve_type(type_))
                         for name_, type_ in _typing.get_type_hints(_globals.base[name], _globals).items())

        def __repr__(self):
            return f'{type(self).__name__}' \
                   f'({", ".join(f"{item[0]}={getattr(self, item[0])}" for item in self._fields_)})'

    _functools.update_wrapper(Wrapper, _globals.base[name], updated=())
    _globals[name] = Wrapper
    return Wrapper


_globals = __head__.Globals()
