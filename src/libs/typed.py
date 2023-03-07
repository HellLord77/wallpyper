__version__ = '0.0.1'

import typing
from types import UnionType
from typing import Any, Callable, ItemsView, Iterable, Literal, Mapping, Tuple, Union


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
                return all(is_instance(ele, type_ele) for ele in obj)
            else:
                return len(obj) == len(args) and all(is_instance(
                    *ele_type_ele) for ele_type_ele in zip(obj, args))
        else:
            return True
    else:
        return False


def _isinstance_namedtuple(obj, cls) -> bool:
    if _issubclass_namedtuple(type(obj)):
        type_hints = typing.get_type_hints(cls)
        # noinspection PyUnresolvedReferences
        for field in cls._fields:
            try:
                val = getattr(obj, field)
            except AttributeError:
                return False
            else:
                if not is_instance(val, type_hints[field]):
                    return False
        return True
    else:
        return False


def _isinstance_typeddict(obj, cls) -> bool:
    if isinstance(obj, dict):
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
                    if not is_instance(val, type_hints[key]):
                        return False
        return True
    else:
        return False


def _isinstance_literal(obj, cls) -> bool:
    return obj in typing.get_args(cls)


def _isinstance_union(obj, cls) -> bool:
    return any(is_instance(obj, type_) for type_ in typing.get_args(cls))


def _isinstance_iterable(obj, cls) -> bool:
    if isinstance(obj, typing.get_origin(cls)):
        args = typing.get_args(cls)
        if args:
            type_ele = args[0]
            return all(is_instance(ele, type_ele) for ele in obj)
        else:
            return True
    else:
        return False


def _isinstance_callable(obj, cls) -> bool:
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
            return all(is_instance(key, type_key) and is_instance(
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
            return all(is_instance(key, type_key) and is_instance(
                val, type_val) for key, val in obj)
        else:
            return True
    else:
        return False


def is_instance(obj, cls) -> bool:
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
    # elif _issubclass_callable(cls):
    #     return _isinstance_callable(obj, cls)
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
