__version__ = '0.1.1'

import ast
import builtins
import collections
import configparser
import contextlib
import dataclasses
import datetime
import enum
import inspect
import io
import itertools
import json
import os
import re
import sys
import types
import typing
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
    return type


def _issubclass_namedtuple(type_: type) -> bool:
    bases = type_.__bases__
    fields = getattr(type_, '_fields', None)
    return len(bases) == 1 and bases[0] is tuple and isinstance(
        fields, tuple) and all(type(name) is str for name in fields)


def _key_dumper(data) -> Any:
    if dataclasses.is_dataclass(data):
        return [f'__{_dump_type(data)}__', vars(data)]
    return data


def _key_loader(data) -> Any:
    if _is_type(data):
        type_ = _load_type(data[0][2:-2])
        if _issubclass_namedtuple(type_):
            # noinspection PyProtectedMember
            return type_(*(JSONConfig._load(val) for val in data[1]))
        elif dataclasses.is_dataclass(type_):
            # noinspection PyProtectedMember
            return type_(**{key: JSONConfig._load(val) for key, val in data[1].items()})
    return data


def _configparser() -> configparser.ConfigParser:
    parser = configparser.ConfigParser(allow_no_value=True)
    parser.optionxform = str
    return parser


class _Config(dict[str, Any]):
    def __str__(self):
        return f'{type(self).__name__}{super().__repr__()}'

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
    KEY_DUMPERS: list[Callable[[Any], Any]] = [_key_dumper]
    KEY_LOADERS: list[Callable[[Any], Any]] = [_key_loader]
    DUMPERS: dict[type[_T], Callable[[_T], dict | list]] = {
        complex: lambda data: [data.real, data.imag],
        collections.deque: lambda data: [data.maxlen, *data],
        datetime.datetime: lambda data: [data.isoformat()],
        datetime.timedelta: lambda data: [data.total_seconds()]}
    DUMPERS[datetime.date] = DUMPERS[datetime.time] = DUMPERS[datetime.datetime]
    LOADERS: dict[type[_T], Callable[[Any], _T]] = {
        complex: lambda data: complex(*data),
        collections.Counter: lambda data: collections.Counter(dict(data)),
        collections.deque: lambda data: collections.deque(
            itertools.islice(data, 1, None), data[0]),
        datetime.date: lambda data: datetime.date.fromisoformat(data[0]),
        datetime.time: lambda data: datetime.time.fromisoformat(data[0]),
        datetime.datetime: lambda data: datetime.datetime.fromisoformat(data[0]),
        datetime.timedelta: lambda data: datetime.timedelta(seconds=data[0])}
    MULTI_DUMPERS: dict[type[_T], Callable[[_T], dict | list]] = {
        enum.Enum: lambda data: [data.name]}
    MULTI_LOADERS: dict[type[_T], Callable[[Any, type[_T]], _T]] = {
        enum.Enum: lambda data, type_: type_[data[0]]}

    @classmethod
    def _dump(cls, root) -> Any:
        for dumper_ in reversed(cls.KEY_DUMPERS):
            root_ = dumper_(root)
            if root_ is not root:
                return cls._dump(root_)
        type_ = type(root)
        dumper = None
        try:
            dumper = cls.DUMPERS[type_]
        except KeyError:
            for base in type_.__mro__:
                try:
                    dumper = cls.MULTI_DUMPERS[base]
                except KeyError:
                    pass
                else:
                    break
        if dumper is None:
            if issubclass(type_, (bool | float | int | str, types.NoneType)):
                return root
            elif issubclass(type_, Iterable):
                child = {key: cls._dump(val) for key, val in root.items()} if issubclass(
                    type_, Mapping) else [cls._dump(val) for val in root]
                return child if type_ in (dict, list) else (f'__{_dump_type(root)}__', child)
            else:
                raise TypeError(f'Node {root} is not JSON serializable')
        else:
            return f'__{_dump_type(root)}__', cls._dump(dumper(root))

    @classmethod
    def _load(cls, root) -> Any:
        for loader_ in reversed(cls.KEY_LOADERS):
            root_ = loader_(root)
            if root_ is not root:
                return cls._load(root_)
        if _is_type(root):
            type_ = _load_type(root[0][2:-2])
            try:
                loader = cls.LOADERS[type_]
            except KeyError:
                for base in type_.__mro__:
                    try:
                        loader = cls.MULTI_LOADERS[base]
                    except KeyError:
                        pass
                    else:
                        return loader(cls._load(root[1]), type_)
                if issubclass(type_, Mapping):
                    return type_((key, cls._load(val)) for key, val in root[1].items())
                elif issubclass(type_, Iterable):
                    return type_(cls._load(val) for val in root[1])
                else:
                    raise TypeError(f'Node {root} is not JSON deserializable')
            else:
                return loader(cls._load(root[1]))
        elif isinstance(root, dict):
            return {key: cls._load(val) for key, val in root.items()}
        elif isinstance(root, list):
            return [cls._load(val) for val in root]
        else:
            return root

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
            raise TypeError(f'Object of type {type(obj).__name__} is not XML serializable')
        return root

    @classmethod
    def _load(cls, root: ElementTree.Element) -> Any:
        if (type_ := root.attrib.get('_')) is None:
            return None if root.text is None else ast.literal_eval(root.text)
        else:
            type_ = _load_type(type_)
            if issubclass(type_, Mapping):
                return type_((child.tag, cls._load(child)) for child in root)
            elif issubclass(type_, Iterable):
                return type_(cls._load(val) for val in root)
            else:
                raise TypeError(f'Node {root} is not XML deserializable')

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
            raise TypeError(f'Object of type {type(obj).__name__} is not REG serializable')

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
                        yield flat, type_(val for _, val in cls._load(root, key))
                    else:
                        raise TypeError(f'Node {root} is not REG deserializable')
            else:
                root.appendleft((key, val))
                break

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
            if isinstance(val, (bool, bytes, complex, float, int, str, types.NoneType)):
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
                    yield key[:-1], type_(val for _, val in cls._load(reg, root, parent))
                else:
                    raise TypeError(f'Node {root} is not REG deserializable')
            else:
                yield key, None if val is None else ast.literal_eval(val)

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
