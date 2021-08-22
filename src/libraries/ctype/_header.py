from __future__ import annotations

import ctypes as _ctypes
import typing as _typing

CT = _typing.TypeVar('CT')


class Pointer(_typing.Generic[CT]):
    contents: CT
    value: CT

    # noinspection PyUnusedLocal,PyTypeChecker
    def __init__(self, type_: _typing.Type[CT]) -> _typing.Type[Pointer[CT]]:
        pass


# noinspection PyAbstractClass
class Array(Pointer, _typing.Sequence[CT]):
    pass


def byref(obj: CT) -> Pointer[CT]:
    # noinspection PyTypeChecker
    return _ctypes.byref(obj)


def cast(obj: _typing.Any,  # typing.cast
         type_: type[CT]) -> Pointer[CT]:
    try:
        return _ctypes.cast(obj, type_)
    except _ctypes.ArgumentError:
        return cast(_ctypes.byref(obj), type_)
    except TypeError:
        return cast(obj, _ctypes.POINTER(type_))


# noinspection PyPep8Naming
def POINTER(type_: _typing.Union[CT, type[CT]]) -> Pointer[CT]:
    try:
        # noinspection PyTypeChecker
        return _ctypes.POINTER(type_)
    except TypeError:
        # noinspection PyTypeChecker
        return _ctypes.POINTER(type(type_))


def pointer(type_: CT) -> Pointer[CT]:
    try:
        # noinspection PyTypeChecker
        return _ctypes.pointer(type_)
    except TypeError:
        # noinspection PyTypeChecker
        return _ctypes.POINTER(type_())


def sizeof(obj: CT) -> int:
    return _ctypes.sizeof(obj)


def items(vars_: dict[str, _typing.Any]) -> _typing.Generator[tuple[str, _typing.Any], None, None]:
    for var, val in vars_.items():
        if not var.startswith('_'):
            yield var, val


def resolve_type(type_: _typing.Any) -> _typing.Any:
    if isinstance(type_, type(_typing.Callable)):
        type_ = [None]
    elif isinstance(type_, type(_typing.Callable[[], None])):
        types_ = _typing.get_args(type_)
        type_ = [resolve_type(types_[1])]
        type_.extend(resolve_type(type_) for type_ in types_[0])
    else:
        if isinstance(type_, type(_typing.Optional[object])):
            type_ = _typing.get_args(type_)[0]
        if _typing.get_origin(type_) is Pointer:
            type_ = _ctypes.POINTER(resolve_type(_typing.get_args(type_)[0]))
    return type_
