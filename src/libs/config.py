__version__ = '0.1.2'

import array
import ast
import builtins
import collections
import configparser
import contextlib
import dataclasses
import datetime
import decimal
import enum
import fractions
import inspect
import io
import ipaddress
import itertools
import json
import operator
import os
import pathlib
import re
import sys
import typing
import uuid
from types import NoneType
from typing import Any, AnyStr, BinaryIO, Callable, ContextManager, Iterable, Iterator, Mapping, Optional, TextIO
from xml.etree import ElementTree

_CONFIG = '_'
_MATCH_TYPE = re.compile(r'__[.|\w]+__').fullmatch

_T = typing.TypeVar('_T')
_TIO = BinaryIO | TextIO
_TPath = bytes | int | str | os.PathLike[bytes] | os.PathLike[str]


@contextlib.contextmanager
def _open(path_or_file: _TPath | _TIO, write: bool = False,
          encoding: Optional[str] = None) -> ContextManager[_TIO]:
    if hasattr(path_or_file, 'write' if write else 'read'):
        yield path_or_file
    else:
        with open(path_or_file, 'w' if write else 'r', encoding=encoding) as file:
            yield file


def _is_type(obj) -> bool:
    return isinstance(obj, list) and len(obj) == 2 and isinstance(
        obj[0], str) and _MATCH_TYPE(obj[0]) and type(obj[1]) in (dict, list)


def _dump_type(obj) -> str:
    type_ = type(obj)
    return type_.__qualname__ if inspect.getmodule(
        type_) is builtins else f'{type_.__module__}|{type_.__qualname__}'


def _load_type(name: str) -> type:
    parts = name.split('|')
    type_ = sys.modules['builtins' if len(parts) == 1 else parts[0]]
    for part in parts[-1].split('.'):
        type_ = getattr(type_, part)
    if isinstance(type_, type):
        return type_
    raise TypeError(f"Object '{type_!r}' is not a type")


def _issubclass_namedtuple(type_: type) -> bool:
    bases = type_.__bases__
    fields = getattr(type_, '_fields', None)
    return len(bases) == 1 and bases[0] is tuple and type(
        fields) is tuple and all(type__ is str for type__ in map(type, fields))


def _dumper(data) -> Any:
    if dataclasses.is_dataclass(data):
        return [f'__{_dump_type(data)}__', vars(data)]
    return data


def _loader(data) -> Any:
    if _is_type(data):
        dunder = data[0]
        type_ = _load_type(dunder[2:-2])
        if _issubclass_namedtuple(type_):
            # noinspection PyProtectedMember
            return type_(*map(JSONConfig._load, data[1]))
        elif dataclasses.is_dataclass(type_):
            # noinspection PyProtectedMember
            return type_(**dict(map(JSONConfig._load_mapping, data[1].items())))
    return data


def _dumper_int(data) -> list[int]:
    return [int(data)]


def _dumper_str(data) -> list[str]:
    return [str(data)]


def _dumper_state(data) -> list:
    # noinspection PyProtectedMember
    return JSONConfig._dump(data.__getstate__())


def _loader_arg(cls: type[_T], data: dict | list) -> _T:
    return cls(data)


def _loader_args(cls: type[_T], data: dict | list) -> _T:
    return cls(*data)


def _loader_kwargs(cls: type[_T], data: dict | list) -> _T:
    return cls(**data)


def _loader_state(cls: type[_T], data: dict | list) -> _T:
    self = cls.__new__(cls)
    # noinspection PyProtectedMember
    self.__setstate__(JSONConfig._load(data))
    return self


def _dumper_datetime(data) -> list[str]:
    return [data.isoformat()]


def _loader_datetime(type_: type[_T], data) -> _T:
    return type_.fromisoformat(data[0])


def _configparser() -> configparser.ConfigParser:
    parser = configparser.ConfigParser(allow_no_value=True)
    parser.optionxform = str
    return parser


class _Config(dict[str, Any]):
    def dump(self, path_or_file: _TPath | _TIO):
        with _open(path_or_file, True) as file:
            # noinspection PyTypeChecker
            file.write(self.dumps())

    def dumps(self) -> str:
        stream = io.StringIO()
        self.dump(stream)
        return stream.getvalue()

    def load(self, path_or_file: _TPath | _TIO):
        with _open(path_or_file) as file:
            # noinspection PyTypeChecker
            self.loads(file.read())

    def loads(self, data: str):
        stream = io.StringIO(data)
        self.load(stream)


class JSONConfig(_Config):
    DUMPERS: list[Callable[[Any], Any]] = [_dumper]
    LOADERS: list[Callable[[Any], Any]] = [_loader]
    TYPE_DUMPERS: dict[type[_T], Callable[[_T], dict | list]] = {
        complex: lambda data: [data.real, data.imag],
        ElementTree.QName: lambda data: [data.text],
        array.array: lambda data: [data.typecode, *data],
        collections.deque: lambda data: [data.maxlen, *data],
        datetime.date: _dumper_datetime,
        datetime.time: _dumper_datetime,
        datetime.datetime: _dumper_datetime,
        datetime.timedelta: lambda data: [
            data.days, data.seconds, data.microseconds],
        decimal.Decimal: _dumper_str,
        fractions.Fraction: lambda data: [data.numerator, data.denominator],
        ipaddress.IPv4Address: _dumper_int,
        ipaddress.IPv4Interface: _dumper_str,
        ipaddress.IPv4Network: _dumper_str,
        ipaddress.IPv6Address: _dumper_int,
        ipaddress.IPv6Interface: _dumper_str,
        ipaddress.IPv6Network: _dumper_str,
        uuid.UUID: _dumper_state}
    TYPE_LOADERS: dict[type[_T], Callable[[type[_T], dict | list], _T]] = {
        complex: _loader_args,
        ElementTree.QName: _loader_args,
        array.array: lambda _, data: array.array(next(it := iter(data)), it),
        collections.Counter: _loader_arg,
        collections.deque: lambda _, data: collections.deque(
            it := iter(data), next(it)),
        datetime.date: _loader_datetime,
        datetime.time: _loader_datetime,
        datetime.datetime: _loader_datetime,
        datetime.timedelta: _loader_args,
        decimal.Decimal: _loader_args,
        fractions.Fraction: _loader_args,
        ipaddress.IPv4Address: _loader_args,
        ipaddress.IPv4Network: _loader_args,
        ipaddress.IPv4Interface: _loader_args,
        ipaddress.IPv6Address: _loader_args,
        ipaddress.IPv6Interface: _loader_args,
        ipaddress.IPv6Network: _loader_args,
        uuid.UUID: _loader_state}
    TYPES_DUMPERS: dict[type[_T], Callable[[_T], dict | list]] = {
        collections.UserString: lambda data: [data.data],
        enum.Enum: lambda data: [data.value],
        pathlib.PurePath: lambda data: list(data.parts)}
    TYPES_LOADERS: dict[type[_T], Callable[[type[_T], dict | list], _T]] = {
        collections.UserString: _loader_args,
        enum.Enum: _loader_args,
        pathlib.PurePath: _loader_args}

    @classmethod
    def _dump(cls, root) -> Any:
        for dumper_ in reversed(cls.DUMPERS):
            root_ = dumper_(root)
            if root_ is not root:
                return cls._dump(root_)
        type_ = type(root)
        dumper = None
        try:
            dumper = cls.TYPE_DUMPERS[type_]
        except KeyError:
            for base in type_.__mro__:
                try:
                    dumper = cls.TYPES_DUMPERS[base]
                except KeyError:
                    pass
                else:
                    break
        if dumper is not None:
            return f'__{_dump_type(root)}__', cls._dump(dumper(root))
        elif issubclass(type_, (bool, float, int, str, NoneType)):
            return root
        elif issubclass(type_, Iterable):
            child = dict(map(cls._dump_mapping, root.items())) if issubclass(
                type_, Mapping) else list(map(cls._dump, root))
            return child if type_ in (dict, list) else (f'__{_dump_type(root)}__', child)
        else:
            raise TypeError(f"Node '{root!r}' is not JSON serializable")

    @classmethod
    def _load(cls, root) -> Any:
        for loader_ in reversed(cls.LOADERS):
            root_ = loader_(root)
            if root_ is not root:
                return cls._load(root_)
        if _is_type(root):
            type_ = _load_type(root[0][2:-2])
            loader = None
            try:
                loader = cls.TYPE_LOADERS[type_]
            except KeyError:
                for base in type_.__mro__:
                    try:
                        loader = cls.TYPES_LOADERS[base]
                    except KeyError:
                        pass
                    else:
                        break
            if loader is not None:
                return loader(type_, cls._load(root[1]))
            elif issubclass(type_, Mapping):
                return type_(map(cls._load_mapping, root[1].items()))
            elif issubclass(type_, Iterable):
                return type_(map(cls._load, root[1]))
            else:
                raise TypeError(f"Node '{root!r}' is not JSON deserializable")
        elif isinstance(root, dict):
            return dict(map(cls._load_mapping, root.items()))
        elif isinstance(root, list):
            return list(map(cls._load, root))
        else:
            return root

    @classmethod
    def _dump_mapping(cls, item: tuple) -> tuple:
        return item[0], cls._dump(item[1])

    @classmethod
    def _load_mapping(cls, item: tuple) -> tuple:
        return item[0], cls._load(item[1])

    def dump(self, path_or_file: _TPath | TextIO, indent: Optional[int | str] = None):
        with _open(path_or_file, True) as file:
            json.dump(self._dump(self)[1], file, indent=indent)

    def dumps(self, indent: Optional[int | str] = '\t') -> str:
        return json.dumps(self._dump(self)[1], indent=indent)

    def loads(self, data: bytearray | AnyStr):
        self.update(self._load(json.loads(data)))


class XMLConfig(_Config):
    TAG_ITEM: str = '_'

    @classmethod
    def _dump(cls, obj, root: ElementTree.Element) -> ElementTree.Element:
        if obj is None:
            pass
        elif isinstance(obj, (bool, bytes, complex, float, int, str)):
            root.text = repr(obj)
        elif isinstance(obj, Iterable):
            root.attrib['_'] = _dump_type(obj)
            for key, val in obj.items() if isinstance(
                    obj, Mapping) else zip(itertools.repeat(cls.TAG_ITEM), obj):
                cls._dump(val, ElementTree.SubElement(root, key))
        else:
            raise TypeError(f"Object of type '{type(obj).__name__}' is not XML serializable")
        return root

    @classmethod
    def _load(cls, root: ElementTree.Element) -> Any:
        if (type_ := root.attrib.get('_')) is None:
            return None if root.text is None else ast.literal_eval(root.text)
        else:
            type_ = _load_type(type_)
            if issubclass(type_, Mapping):
                return type_(map(cls._load_mapping, root))
            elif issubclass(type_, Iterable):
                return type_(map(cls._load, root))
            else:
                raise TypeError(f"Node '{root!r}' is not XML deserializable")

    @classmethod
    def _load_mapping(cls, item: ElementTree.Element) -> tuple:
        return item.tag, cls._load(item)

    def dump(self, path_or_file: _TPath | _TIO,
             indent: Optional[int | str] = None, encoding: Optional[str] = None):
        tree = ElementTree.ElementTree(self._dump(
            self, ElementTree.Element(_CONFIG)))
        if indent is not None:
            ElementTree.indent(tree, indent if isinstance(indent, str) else ' ' * indent)
        tree.write(path_or_file, encoding=encoding)

    def dumps(self, indent: Optional[int | str] = 2) -> str:
        stream = io.StringIO()
        self.dump(stream, indent, 'unicode')
        return stream.getvalue()

    def load(self, path_or_file: _TPath | _TIO):
        with _open(path_or_file) as file:
            self.update(self._load(ElementTree.parse(file).getroot()))

    def loads(self, data: AnyStr):
        self.update(self._load(ElementTree.fromstring(data)))


class FLATConfig(_Config):
    SEPARATOR = '.'

    @classmethod
    def _dump(cls, obj, root: dict[str, str], __parent: str = '') -> Any:
        if obj is None:
            pass
        elif isinstance(obj, (bool, bytes, complex, float, int, str)):
            return repr(obj)
        elif isinstance(obj, Iterable):
            if __parent:
                __parent += cls.SEPARATOR
            for key, val in obj.items() if isinstance(obj, Mapping) else enumerate(obj):
                parent = f'{__parent}{key}'
                children = {}
                dumped = cls._dump(val, children, parent)
                if dumped is children:
                    root[parent + cls.SEPARATOR] = _dump_type(val)
                    root.update(children)
                else:
                    root[parent] = dumped
            return root
        else:
            raise TypeError(f"Object of type '{type(obj).__name__}' is not REG serializable")

    @classmethod
    def _load(cls, root: collections.deque[tuple[str, str]],
              __parent: str = '') -> Iterator[tuple[str, Any]]:
        while root:
            key, val = root.popleft()
            if key.startswith(__parent):
                flat = key.rsplit(cls.SEPARATOR, 1)[-1]
                if flat:
                    yield flat, None if val is None else ast.literal_eval(val)
                else:
                    flat = key.rsplit(cls.SEPARATOR, 2)[-2]
                    type_ = _load_type(val)
                    if issubclass(type_, Mapping):
                        yield flat, type_(cls._load(root, key))
                    elif issubclass(type_, Iterable):
                        yield flat, type_(map(cls._load_iterable, cls._load(root, key)))
                    else:
                        raise TypeError(f"Node '{root!r}' is not REG deserializable")
            else:
                root.appendleft((key, val))
                break

    _load_iterable = operator.itemgetter(1)

    def dump(self, path_or_file: _TPath | TextIO):
        flat = _configparser()
        flat.read_dict({_CONFIG: self._dump(self, {})})
        with _open(path_or_file, True) as file:
            flat.write(file)

    def load(self, path_or_file: _TPath | TextIO):
        flat = _configparser()
        with _open(path_or_file) as file:
            flat.read_file(file)
        # noinspection PyTypeChecker
        self.__init__(self._load(collections.deque(flat[_CONFIG].items())))


class REGConfig(_Config):
    SEPARATOR = os.sep

    @classmethod
    def _dump(cls, obj: Iterable, root: dict[str, str | dict], __parent: str) -> dict:
        for key, val in obj.items() if isinstance(obj, Mapping) else enumerate(obj):
            if isinstance(val, (bool, bytes, complex, float, int, str, NoneType)):
                root[__parent][key] = repr(val)
            elif isinstance(val, Iterable):
                child = key if __parent == _CONFIG else f'{__parent}{cls.SEPARATOR}{key}'
                root[__parent][f'{key}{cls.SEPARATOR}'] = _dump_type(val)
                root[child] = {}
                cls._dump(val, root, child)
        return root

    @classmethod
    def _load(cls, obj: configparser.SectionProxy, root: configparser.ConfigParser,
              __parent: str = '') -> Iterator[tuple[str, Any]]:
        for key, val in obj.items():
            if key.endswith(cls.SEPARATOR):
                parent = __parent + key
                reg = root[parent[:-1]]
                type_ = _load_type(val)
                if issubclass(type_, Mapping):
                    yield key[:-1], type_(cls._load(reg, root, parent))
                elif issubclass(type_, Iterable):
                    yield key[:-1], type_(map(cls._load_iterable, cls._load(reg, root, parent)))
                else:
                    raise TypeError(f"Node '{root!r}' is not REG deserializable")
            else:
                yield key, None if val is None else ast.literal_eval(val)

    _load_iterable = operator.itemgetter(1)

    def dump(self, path_or_file: _TPath | TextIO):
        reg = _configparser()
        reg.read_dict(self._dump(self, {_CONFIG: {}}, _CONFIG))
        with _open(path_or_file, True) as file:
            reg.write(file)

    def load(self, path_or_file: _TPath | _TIO):
        reg = _configparser()
        with _open(path_or_file) as file:
            reg.read_file(file)
        self.__init__(self._load(reg[_CONFIG], reg))


try:
    # noinspection PyUnresolvedReferences
    import tomlkit
except ImportError:
    pass
else:
    class TOMLConfig(_Config):
        def dumps(self) -> str:
            return tomlkit.dumps(self)

        def loads(self, data: AnyStr):
            self.update(tomlkit.loads(data))

try:
    # noinspection PyUnresolvedReferences
    import yaml
except ImportError:
    pass
else:
    class YAMLConfig(_Config):
        def dump(self, path_or_file: _TPath | _TIO,
                 indent: Optional[int] = None, encoding: Optional[str] = None):
            with _open(path_or_file, True) as file:
                yaml.dump(self, file, indent=indent, encoding=encoding, sort_keys=False)

        def dumps(self, indent: Optional[int] = None) -> str:
            return yaml.dump(self, indent=indent, sort_keys=False)

        def load(self, path_or_file: _TPath | _TIO):
            with _open(path_or_file) as file:
                self.update(yaml.full_load(file))

        def loads(self, data: AnyStr):
            self.update(yaml.full_load(data))


    # noinspection PyTypeChecker
    yaml.add_representer(YAMLConfig, yaml.representer.SafeRepresenter.represent_dict)

Config = JSONConfig
