__version__ = '0.1.2'

import copy
import dataclasses
import logging
import typing
from types import NoneType
from types import UnionType
from typing import Any
from typing import Callable
from typing import ItemsView
from typing import Iterable
from typing import Literal
from typing import Mapping
from typing import MutableMapping
from typing import MutableSequence
from typing import NotRequired
from typing import Optional
from typing import Required
from typing import Sequence
from typing import Tuple
from typing import TypedDict
from typing import Union

logger = logging.getLogger(__name__)


def _type_tuple(obj: tuple) -> type:
    return tuple[tuple(map(type_ex, obj))]


def _type_dict(obj: dict) -> type:
    return TypedDict(type(obj).__name__, {key: type_ex(
        val) for key, val in obj.items()}) if set(
        map(type_ex, obj)) == {str} else _type_mapping(obj)


def _type_union(obj: Iterable) -> type:
    optional = False
    types = set(map(type_ex, obj))
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


def _type_iterable(obj: Iterable) -> type:
    return type(obj)[_type_union(obj)]


def _type_mapping(obj: Mapping) -> type:
    return type(obj)[_type_union(obj), _type_union(obj.values())]


def type_ex(obj) -> type:
    if isinstance(obj, (bytes, str)):
        return type(obj)
    elif isinstance(obj, tuple):
        return _type_tuple(obj)
    elif isinstance(obj, dict):
        return _type_dict(obj)
    elif isinstance(obj, Mapping):
        return _type_mapping(obj)
    elif isinstance(obj, Iterable):
        return _type_iterable(obj)
    else:
        return type(obj)


def type_dataclass_asdict(cls):
    type_hints = typing.get_type_hints(cls)
    # noinspection PyUnresolvedReferences,PyProtectedMember
    return TypedDict(cls.__name__, {name: (
        Required if isinstance(field.default, dataclasses._MISSING_TYPE) else NotRequired)[
        type_hints[name]] for name, field in cls.__dataclass_fields__.items()})


def _issubclass_tuple(cls) -> bool:
    cls = typing.get_origin(cls)
    return cls is not None and issubclass(cls, (tuple, Tuple))


def _issubclass_namedtuple(cls) -> bool:
    bases = getattr(cls, '__bases__', None)
    fields = getattr(cls, '_fields', None)
    return type(bases) is tuple and len(bases) == 1 and bases[0] is tuple and type(
        fields) is tuple and all(type_ is str for type_ in map(type, fields))


def _issubclass_typeddict(cls) -> bool:
    bases = getattr(cls, '__bases__', None)
    required_keys = getattr(cls, '__required_keys__', None)
    optional_keys = getattr(cls, '__optional_keys__', None)
    return type(bases) is tuple and len(bases) == 1 and bases[0] is dict and type(
        getattr(cls, '__required_keys__', None)) is frozenset and all(
        type_ is str for type_ in map(type, required_keys)) and type(
        getattr(cls, '__optional_keys__', None)) is frozenset and all(
        type_ is str for type_ in map(type, optional_keys))


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
    if isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            if len(args) == 2 and args[1] is ...:
                type_ele = args[0]
                return all(isinstance_ex(ele, type_ele) for ele in obj)
            else:
                return len(obj) == len(args) and all(isinstance_ex(
                    *ele_type_ele) for ele_type_ele in zip(obj, args))
        else:
            return True
    else:
        return False


def _isinstance_namedtuple(obj, cls) -> bool:
    if _issubclass_namedtuple(type(obj)):
        type_hints = typing.get_type_hints(cls)
        for field in cls._fields:
            try:
                val = getattr(obj, field)
            except AttributeError:
                return False
            else:
                if not isinstance_ex(val, type_hints[field]):
                    return False
        return True
    else:
        return False


def _isinstance_typeddict(obj, cls) -> bool:
    if isinstance(obj, dict):
        type_hints = typing.get_type_hints(cls)
        for optional, keys in enumerate((
                cls.__required_keys__, cls.__optional_keys__)):
            for key in keys:
                try:
                    val = obj[key]
                except KeyError:
                    if not optional:
                        return False
                else:
                    if not isinstance_ex(val, type_hints[key]):
                        return False
        return True
    else:
        return False


def _isinstance_literal(obj, cls) -> bool:
    return obj in typing.get_args(cls)


def _isinstance_union(obj, cls) -> bool:
    return any(isinstance_ex(obj, type_) for type_ in typing.get_args(cls))


def _isinstance_iterable(obj, cls) -> bool:
    if isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_ele = args[0]
            return all(isinstance_ex(ele, type_ele) for ele in obj)
        else:
            return True
    else:
        return False


def _isinstance_callable(obj, cls) -> bool:
    logger.warning('Incompletely implemented %r called', _isinstance_callable.__name__)
    if isinstance(obj, typing.get_origin(cls)):
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
    if isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_key, type_val = args
            return all(isinstance_ex(key, type_key) and isinstance_ex(
                val, type_val) for key, val in obj.items())
        else:
            return True
    else:
        return False


def _isinstance_itemsview(obj, cls) -> bool:
    if isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_key, type_val = args
            return all(isinstance_ex(key, type_key) and isinstance_ex(
                val, type_val) for key, val in obj)
        else:
            return True
    else:
        return False


def isinstance_ex(obj, cls) -> bool:
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
        return isinstance(obj, cls)


def is_namedtuple(obj) -> bool:
    if not isinstance(obj, type):
        obj = type(obj)
    return _issubclass_namedtuple(obj)


def is_typeddict(obj) -> bool:
    if not isinstance(obj, type):
        obj = type(obj)
    return _issubclass_typeddict(obj)


def _update_sequence(self: MutableSequence, cls):
    remove = []
    for index, val in enumerate(self):
        if not isinstance_ex(val, cls):
            remove.append(index)
    for index in reversed(remove):
        del self[index]


def _update_mapping(self: MutableMapping, val, cls, callback, key):
    if key in self:
        val_ = self[key]
        if isinstance_ex(val_, cls):
            return
        elif isinstance(val, Mapping):
            if isinstance(val_, MutableMapping):
                intersection_update(val_, val, cls, callback)
                return
        elif isinstance(val, Sequence):
            if isinstance(val_, MutableSequence) and isinstance_ex(
                    val_, typing.get_origin(cls)):
                _update_sequence(val_, typing.get_args(cls)[0])
                return
    self[key] = callback(val)


def intersection_update(self: MutableMapping, other: Mapping, cls,
                        factory: Callable[[Any], Any] = copy.deepcopy):
    if not isinstance_ex(other, cls):
        logger.error('Mismatched type: type(%r) != %r', other, cls)
    if _issubclass_typeddict(cls):
        for key, cls_ in typing.get_type_hints(cls).items():
            if key in other:
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
