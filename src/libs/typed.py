__version__ = '0.1.1'

import builtins
import copy
import dataclasses
import typing
from types import NoneType, UnionType
from typing import (Any, Callable, ItemsView, Iterable, Literal, Mapping, MutableMapping,
                    MutableSequence, NotRequired, Optional, Sequence, Required, Tuple, TypedDict, Union)


def _type_tuple(obj: tuple) -> builtins.type:
    return tuple[tuple(map(type, obj))]


def _type_dict(obj: dict) -> builtins.type:
    return TypedDict(builtins.type(obj).__name__, {key: type(
        val) for key, val in obj.items()}) if set(
        map(type, obj)) == {str} else _type_mapping(obj)


def _type_union(obj: Iterable) -> builtins.type:
    optional = False
    types = set(map(type, obj))
    if NoneType in types:
        optional = True
        types.remove(NoneType)
    if not types:
        type_ = Any
    elif len(types) == 1:
        type_ = next(iter(types))
    else:
        type_ = Union[tuple(types)]
    if optional:
        type_ = Optional[type_] if types else NoneType
    return type_


def _type_iterable(obj: Iterable) -> builtins.type:
    return builtins.type(obj)[_type_union(obj)]


def _type_mapping(obj: Mapping) -> builtins.type:
    return builtins.type(obj)[_type_union(obj), _type_union(obj.values())]


# noinspection PyShadowingBuiltins
def type(obj) -> builtins.type:
    if builtins.isinstance(obj, (bytes, str)):
        return builtins.type(obj)
    elif builtins.isinstance(obj, tuple):
        return _type_tuple(obj)
    elif builtins.isinstance(obj, dict):
        return _type_dict(obj)
    elif builtins.isinstance(obj, Mapping):
        return _type_mapping(obj)
    elif builtins.isinstance(obj, Iterable):
        return _type_iterable(obj)
    else:
        return builtins.type(obj)


def type_dataclass_asdict(cls):
    type_hints = typing.get_type_hints(cls)
    # noinspection PyUnresolvedReferences,PyProtectedMember
    return TypedDict(cls.__name__, {name: (
        Required if builtins.isinstance(field.default, dataclasses._MISSING_TYPE) else NotRequired)[
        type_hints[name]] for name, field in cls.__dataclass_fields__.items()})


def _issubclass_tuple(cls) -> bool:
    cls = typing.get_origin(cls)
    return cls is not None and issubclass(cls, (tuple, Tuple))


def _issubclass_namedtuple(cls) -> bool:
    bases = getattr(cls, '__bases__', None)
    fields = getattr(cls, '_fields', None)
    return builtins.type(bases) is tuple and len(bases) == 1 and bases[0] is tuple and builtins.type(
        fields) is tuple and all(type_ is str for type_ in map(builtins.type, fields))


def _issubclass_typeddict(cls) -> bool:
    bases = getattr(cls, '__bases__', None)
    required_keys = getattr(cls, '__required_keys__', None)
    optional_keys = getattr(cls, '__optional_keys__', None)
    return builtins.type(bases) is tuple and len(bases) == 1 and bases[0] is dict and builtins.type(
        getattr(cls, '__required_keys__', None)) is frozenset and all(
        type_ is str for type_ in map(builtins.type, required_keys)) and builtins.type(
        getattr(cls, '__optional_keys__', None)) is frozenset and all(
        type_ is str for type_ in map(builtins.type, optional_keys))


def _issubclass_any(cls) -> bool:
    return cls in (..., Any)


def _issubclass_literal(cls) -> bool:
    return typing.get_origin(cls) is Literal


def _issubclass_union(cls) -> bool:
    return typing.get_origin(cls) in (Union, UnionType)


def _issubclass_iterable(cls) -> bool:
    cls = typing.get_origin(cls)
    return cls is not None and issubclass(cls, Iterable)


def _issubclass_callable(cls) -> bool:
    cls = typing.get_origin(cls)
    return cls is not None and issubclass(cls, Callable)


def _issubclass_mapping(cls) -> bool:
    cls = typing.get_origin(cls)
    return cls is not None and issubclass(cls, Mapping)


def _issubclass_itemsview(cls) -> bool:
    cls = typing.get_origin(cls)
    return cls is not None and issubclass(cls, ItemsView)


def _isinstance_tuple(obj, cls) -> bool:
    if builtins.isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            if len(args) == 2 and args[1] is ...:
                type_ele = args[0]
                # noinspection PyTypeHints
                return all(isinstance(ele, type_ele) for ele in obj)
            else:
                return len(obj) == len(args) and all(isinstance(
                    *ele_type_ele) for ele_type_ele in zip(obj, args))
        else:
            return True
    else:
        return False


def _isinstance_namedtuple(obj, cls) -> bool:
    if _issubclass_namedtuple(builtins.type(obj)):
        type_hints = typing.get_type_hints(cls)
        # noinspection PyUnresolvedReferences
        for field in cls._fields:
            try:
                val = getattr(obj, field)
            except AttributeError:
                return False
            else:
                # noinspection PyTypeHints
                if not isinstance(val, type_hints[field]):
                    return False
        return True
    else:
        return False


def _isinstance_typeddict(obj, cls) -> bool:
    if builtins.isinstance(obj, dict):
        type_hints = typing.get_type_hints(cls)
        # noinspection PyUnresolvedReferences
        for optional, keys in enumerate((
                cls.__required_keys__, cls.__optional_keys__)):
            for key in keys:
                try:
                    val = obj[key]
                except KeyError:
                    if not optional:
                        return False
                else:
                    # noinspection PyTypeHints
                    if not isinstance(val, type_hints[key]):
                        return False
        return True
    else:
        return False


def _isinstance_literal(obj, cls) -> bool:
    return obj in typing.get_args(cls)


def _isinstance_union(obj, cls) -> bool:
    return any(isinstance(obj, type_) for type_ in typing.get_args(cls))


def _isinstance_iterable(obj, cls) -> bool:
    if builtins.isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_ele = args[0]
            # noinspection PyTypeHints
            return all(isinstance(ele, type_ele) for ele in obj)
        else:
            return True
    else:
        return False


def _isinstance_callable(obj, cls) -> bool:
    if builtins.isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_args, type_ret = args
            type_hints = typing.get_type_hints(obj)
            if type_args is not ... and len(type_args) != len(type_hints) - 1 and not all(
                    issubclass(*ele_type_ele) for ele_type_ele in zip(type_hints.values(), type_args)):
                return False
            elif not issubclass(type_hints['return'], type_ret):
                return False
            return True
        else:
            return True
    else:
        return False


def _isinstance_mapping(obj, cls) -> bool:
    if builtins.isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_key, type_val = args
            return all(isinstance(key, type_key) and isinstance(
                val, type_val) for key, val in obj.items())
        else:
            return True
    else:
        return False


def _isinstance_itemsview(obj, cls) -> bool:
    if builtins.isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_key, type_val = args
            return all(isinstance(key, type_key) and isinstance(
                val, type_val) for key, val in obj)
        else:
            return True
    else:
        return False


# noinspection PyShadowingBuiltins
def isinstance(obj, cls) -> bool:
    if _issubclass_any(cls):
        return True
    elif _issubclass_literal(cls):
        return _isinstance_literal(obj, cls)
    elif _issubclass_union(cls):
        return _isinstance_union(obj, cls)
    elif _issubclass_namedtuple(cls):
        return _isinstance_namedtuple(obj, cls)
    elif _issubclass_typeddict(cls):
        return _isinstance_typeddict(obj, cls)
    elif _issubclass_tuple(cls):
        return _isinstance_tuple(obj, cls)
    elif _issubclass_itemsview(cls):
        return _isinstance_itemsview(obj, cls)
    elif _issubclass_mapping(cls):
        return _isinstance_mapping(obj, cls)
    elif _issubclass_iterable(cls):
        return _isinstance_iterable(obj, cls)
    elif _issubclass_callable(cls):
        return _isinstance_callable(obj, cls)
    else:
        return builtins.isinstance(obj, cls)


def is_namedtuple(obj) -> bool:
    if not builtins.isinstance(obj, builtins.type):
        obj = builtins.type(obj)
    return _issubclass_namedtuple(obj)


def is_typeddict(obj) -> bool:
    if not builtins.isinstance(obj, builtins.type):
        obj = builtins.type(obj)
    return _issubclass_typeddict(obj)


def _update_sequence(self: MutableSequence, cls):
    remove = []
    for index, val in enumerate(self):
        if not isinstance(val, cls):
            remove.append(index)
    for index in reversed(remove):
        del self[index]


def _update_mapping(self: MutableMapping, val, cls, callback, key):
    if key in self:
        val_ = self[key]
        if isinstance(val_, cls):
            return
        elif builtins.isinstance(val, Mapping):
            if builtins.isinstance(val_, MutableMapping):
                intersection_update(val_, val, cls, callback)
                return
        elif builtins.isinstance(val, Sequence):
            if builtins.isinstance(val_, MutableSequence) and isinstance(
                    val_, typing.get_origin(cls)):
                _update_sequence(val_, typing.get_args(cls)[0])
                return
    self[key] = callback(val)


def intersection_update(self: MutableMapping, other: Mapping, cls,
                        factory: Callable[[Any], Any] = copy.deepcopy):
    assert isinstance(other, cls)
    if _issubclass_typeddict(cls):
        for key, cls_ in typing.get_type_hints(cls).items():
            _update_mapping(self, other[key], cls_, factory, key)
    else:
        cls_ = typing.get_args(cls)[1]
        for key, val in other.items():
            _update_mapping(self, val, cls_, factory, key)
    remove = []
    for key in self:
        if key not in other:
            remove.append(key)
    for key in remove:
        del self[key]
