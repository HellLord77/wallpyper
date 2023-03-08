__version__ = '0.1.4'

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
import sys
import typing
import uuid
from types import NoneType
from typing import Any, AnyStr, BinaryIO, Callable, ContextManager, Iterable, Iterator, Mapping, Optional, TextIO
from xml.etree import ElementTree

_T = typing.TypeVar('_T')
_TIO = BinaryIO | TextIO
_TPath = bytes | int | str | os.PathLike[bytes] | os.PathLike[str]

_CONFIG = '_'


@contextlib.contextmanager
def _open(path_or_file: _TPath | _TIO, write: bool = False, byte: bool = False,
          encoding: Optional[str] = None) -> ContextManager[_TIO]:
    if hasattr(path_or_file, 'write' if write else 'read'):
        yield path_or_file
    else:
        with open(path_or_file, ('w' if write else 'r') + byte * 'b', encoding=encoding) as file:
            yield file


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
        self.load(io.StringIO(data))


def _dump_type(obj) -> str:
    type_ = type(obj)
    name = type_.__qualname__
    if inspect.getmodule(type_) is not builtins:
        name = f'{type_.__module__}|{name}'
    return name


def _load_type(name: str) -> type:
    parts = name.split('|')
    type_ = sys.modules['builtins' if len(parts) == 1 else parts[0]]
    for part in parts[-1].split('.'):
        type_ = getattr(type_, part)
    if not isinstance(type_, type):
        raise TypeError(f"Object '{type_!r}' is not a type")
    return type_


def _issubclass_namedtuple(type_: type) -> bool:
    bases = type_.__bases__
    fields = getattr(type_, '_fields', None)
    return len(bases) == 1 and bases[0] is tuple and type(
        fields) is tuple and all(type__ is str for type__ in map(type, fields))


def _dumper(data) -> Any:
    if dataclasses.is_dataclass(data):
        # noinspection PyProtectedMember
        return {JSONConfig._dump_type(data): data.__getstate__()}
    return data


def _loader(data) -> Any:
    # noinspection PyProtectedMember
    if (type_data := JSONConfig._load_type(data)) is not None:
        type_, root = type_data
        if _issubclass_namedtuple(type_):
            # noinspection PyProtectedMember
            return type_(*map(JSONConfig._load, root))
        elif dataclasses.is_dataclass(type_):
            # noinspection PyProtectedMember
            return type_(**dict(map(JSONConfig._load_mapping, root.items())))
    return data


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


def _loader_datetime(type_: type[_T], data) -> _T:
    return type_.fromisoformat(data)


class JSONConfig(_Config):
    TYPE_PREFIX = '$'
    DUMPERS: list[Callable[[Any], Any]] = [_dumper]
    LOADERS: list[Callable[[Any], Any]] = [_loader]
    # noinspection PyUnresolvedReferences
    TYPE_DUMPERS: dict[type[_T], Callable[[_T], Any]] = {
        complex: lambda data: [data.real, data.imag],
        range: lambda data: [data.start, data.stop, data.step],
        ElementTree.QName: lambda data: data.text,
        array.array: lambda data: [data.typecode, data.tolist()],
        collections.ChainMap: lambda data: data.maps,
        collections.deque: lambda data: [list(data), data.maxlen],
        datetime.date: datetime.date.isoformat,
        datetime.time: datetime.time.isoformat,
        datetime.datetime: datetime.datetime.isoformat,
        datetime.timedelta: lambda data: [
            data.days, data.seconds, data.microseconds],
        decimal.Decimal: decimal.Decimal.__str__,
        fractions.Fraction: lambda data: [data.numerator, data.denominator],
        ipaddress.IPv4Address: ipaddress.IPv4Address.__int__,
        ipaddress.IPv4Interface: ipaddress.IPv4Interface.__str__,
        ipaddress.IPv4Network: ipaddress.IPv4Network.__str__,
        ipaddress.IPv6Address: ipaddress.IPv6Address.__int__,
        ipaddress.IPv6Interface: ipaddress.IPv6Interface.__str__,
        ipaddress.IPv6Network: ipaddress.IPv6Network.__str__,
        uuid.UUID: uuid.UUID.__getstate__}
    TYPE_LOADERS: dict[type[_T], Callable[[type[_T], Any], _T]] = {
        complex: _loader_args,
        range: _loader_args,
        ElementTree.QName: _loader_arg,
        array.array: _loader_args,
        collections.ChainMap: _loader_args,
        collections.Counter: _loader_arg,
        collections.deque: _loader_args,
        datetime.date: _loader_datetime,
        datetime.time: _loader_datetime,
        datetime.datetime: _loader_datetime,
        datetime.timedelta: _loader_args,
        decimal.Decimal: _loader_arg,
        fractions.Fraction: _loader_args,
        ipaddress.IPv4Address: _loader_arg,
        ipaddress.IPv4Network: _loader_arg,
        ipaddress.IPv4Interface: _loader_arg,
        ipaddress.IPv6Address: _loader_arg,
        ipaddress.IPv6Interface: _loader_arg,
        ipaddress.IPv6Network: _loader_arg,
        uuid.UUID: _loader_state}
    TYPES_DUMPERS: dict[type[_T], Callable[[_T], Any]] = {
        collections.UserString: lambda data: data.data,
        enum.Enum: lambda data: data.value,
        pathlib.PurePath: lambda data: list(data.parts)}
    TYPES_LOADERS: dict[type[_T], Callable[[type[_T], Any], _T]] = {
        collections.UserString: _loader_arg,
        enum.Enum: _loader_arg,
        pathlib.PurePath: _loader_args}

    @classmethod
    def _dump_type(cls, obj) -> str:
        return f'{cls.TYPE_PREFIX}{_dump_type(obj)}'

    @classmethod
    def _load_type(cls, data) -> Optional[tuple[type, Any]]:
        # noinspection PyUnboundLocalVariable
        if isinstance(data, dict) and len(data) == 1 and isinstance(
                name := next(iter(data)), str) and name.startswith(cls.TYPE_PREFIX):
            return _load_type(name.removeprefix(cls.TYPE_PREFIX)), data[name]

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
            return {cls._dump_type(root): cls._dump(dumper(root))}
        elif issubclass(type_, (bool, float, int, str, NoneType)):
            return root
        elif issubclass(type_, Iterable):
            child = dict(map(cls._dump_mapping, root.items())) if issubclass(
                type_, Mapping) else list(map(cls._dump, root))
            return child if type_ in (dict, list) else {cls._dump_type(root): child}
        else:
            raise TypeError(f"Node '{root!r}' is not JSON serializable")

    @classmethod
    def _load(cls, root) -> Any:
        for loader_ in reversed(cls.LOADERS):
            root_ = loader_(root)
            if root_ is not root:
                return cls._load(root_)
        if (type_root := cls._load_type(root)) is not None:
            type_, root_ = type_root
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
                return loader(type_, cls._load(root_))
            elif issubclass(type_, Iterable):
                # noinspection PyArgumentList
                return type_(map(*(cls._load_mapping, root_.items()) if issubclass(
                    type_, Mapping) else (cls._load, root_)))
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
            json.dump(self._dump(self)[self._dump_type(self)], file, indent=indent)

    def dumps(self, indent: Optional[int | str] = '\t') -> str:
        return json.dumps(self._dump(self)[self._dump_type(self)], indent=indent)

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
            ElementTree.indent(tree, indent if isinstance(
                indent, str) else ' ' * indent)
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


class INIConfig(_Config):
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
