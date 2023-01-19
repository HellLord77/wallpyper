__version__ = '0.0.3'

import ast
import builtins
import contextlib
import io
import os
from typing import Any, Generator, BinaryIO, Iterable, Mapping, Optional, TextIO

_CONFIG = '_'
_TYPE_MAP = '_'

_T = Optional[bool | bytes | complex | float | int | str | Iterable | Mapping]
_TPath = bytes | int | str | os.PathLike[bytes] | os.PathLike[str]
_TIO = BinaryIO | TextIO


@contextlib.contextmanager
def _open(path_or_file: _TPath | _TIO, write: bool = False,
          encoding: Optional[str] = None) -> Generator[_TIO, None, None]:
    if hasattr(path_or_file, 'write' if write else 'read'):
        yield path_or_file
    else:
        with open(path_or_file, 'w' if write else 'r', encoding=encoding) as file:
            yield file


class _Config(dict[str, _T]):
    def dump(self, path_or_file: _TPath | _TIO):
        with _open(path_or_file, True) as file:
            file.write(self.dumps())

    def dumps(self) -> str:
        stream = io.StringIO()
        self.dump(stream)
        return stream.getvalue()

    def load(self, path_or_file: _TPath | _TIO):
        with _open(path_or_file) as file:
            self.loads(file.read())

    def loads(self, data: str):
        stream = io.StringIO(data)
        self.load(stream)


try:
    import json
except ImportError:
    json = None
else:
    class JSONConfig(_Config):
        _builtins = {f'__{type_.__name__}__' for type_ in (
            bytearray, bytes, complex, frozenset, set, tuple)}

        @classmethod
        def _dump(cls, root: Any):
            if isinstance(root, complex):
                return f'__complex__', (root.real, root.imag)
            elif f'__{type(root).__name__}__' in cls._builtins:
                return f'__{type(root).__name__}__', tuple(cls._dump(child) for child in root)
            elif isinstance(root, dict):
                return {key: cls._dump(value) for key, value in root.items()}
            elif isinstance(root, list):
                return [cls._dump(child) for child in root]
            else:
                return root

        @classmethod
        def _load(cls, root: Any):
            if isinstance(root, dict):
                return {key: cls._load(val) for key, val in root.items()}
            elif isinstance(root, list):
                if len(root) == 2 and isinstance(root[0], str) and isinstance(
                        root[1], list) and root[0] in cls._builtins:
                    return complex(*root[1]) if root[0] == '__complex__' else getattr(
                        builtins, root[0][2:-2])(cls._load(child) for child in root[1])
                else:
                    return [cls._load(child) for child in root]
            else:
                return root

        def dump(self, path_or_file: _TPath | TextIO, indent: Optional[int | str] = None):
            with _open(path_or_file, True) as file:
                json.dump(self._dump(self), file, indent=indent)

        def dumps(self, indent: Optional[int | str] = '\t') -> str:
            return json.dumps(self._dump(self), indent=indent)

        def loads(self, data: bytearray | bytes | str):
            self.update(self._load(json.loads(data)))

try:
    from xml.etree import ElementTree
except ImportError:
    ElementTree = None
else:
    class XMLConfig(_Config):
        TAG_ITEM: str = '_'
        KEY_TYPE: str = '_'

        @classmethod
        def _dump(cls, obj: _T, root: ElementTree.Element) -> ElementTree.Element:
            if obj is None:
                pass
            elif isinstance(obj, bool | bytes | complex | float | int | str):
                text = repr(obj)
                root.text = text
            elif isinstance(obj, Mapping):
                root.attrib[cls.KEY_TYPE] = _TYPE_MAP
                for key, val in obj.items():
                    cls._dump(val, ElementTree.SubElement(root, key))
            elif isinstance(obj, Iterable):
                type_ = type(obj).__name__
                try:
                    getattr(builtins, type_)
                except AttributeError:
                    raise TypeError(f'Iterable of type {type_} is not XML serializable')
                else:
                    root.attrib[cls.KEY_TYPE] = type_
                    for val in obj:
                        cls._dump(val, ElementTree.SubElement(root, cls.TAG_ITEM))
            else:
                raise TypeError(f'Object of type {type(obj).__name__} is not XML serializable')
            return root

        @classmethod
        def _load(cls, root: ElementTree.Element) -> _T:
            if (type_ := root.attrib.get(cls.KEY_TYPE)) is None:
                return ast.literal_eval(str(root.text))
            elif type_ == _TYPE_MAP:
                return {child.tag: cls._load(child) for child in root}
            else:
                return getattr(builtins, type_)(cls._load(child) for child in root)

        def dump(self, path_or_file: _TPath | _TIO,
                 indent: Optional[int | str] = None, encoding: Optional[str] = None):
            tree = ElementTree.ElementTree(self._dump(
                self, ElementTree.Element(_CONFIG, {self.KEY_TYPE: _TYPE_MAP})))
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

        def loads(self, data: bytes | str):
            self.update(self._load(ElementTree.fromstring(data)))

try:
    import configparser
except ImportError:
    configparser = None
else:
    def _configparser() -> configparser.ConfigParser:
        parser = configparser.ConfigParser(allow_no_value=True)
        parser.optionxform = str
        return parser


    class FLATConfig(_Config):
        SEPARATOR = '.'

        @classmethod
        def _dump(cls, obj: _T, root: dict[str, str], __parent: str = ''):
            if obj is None:
                pass
            elif isinstance(obj, bool | bytes | complex | float | int | str):
                return repr(obj)
            elif isinstance(obj, Iterable):
                if __parent:
                    __parent += cls.SEPARATOR
                for key, val in obj.items() if isinstance(obj, Mapping) else enumerate(obj):
                    parent = f'{__parent}{key}'
                    children = {}
                    dumped = cls._dump(val, children, parent)
                    if dumped is children:
                        if isinstance(val, Mapping):
                            type_ = _TYPE_MAP
                        else:
                            type_ = type(val).__name__
                            try:
                                getattr(builtins, type_)
                            except AttributeError:
                                raise TypeError(f'Iterable of type {type_} is not REG serializable')
                        root[parent + cls.SEPARATOR] = type_
                        root.update(children)
                    else:
                        root[parent] = dumped
                return root
            else:
                raise TypeError(f'Object of type {type(obj).__name__} is not REG serializable')

        @classmethod
        def _load(cls, root: list[tuple[str, str]],
                  __parent: str = '') -> Generator[tuple[str, _T], None, None]:
            while root:
                key, val = root.pop()
                is_iterable = key.endswith(cls.SEPARATOR)
                if key.startswith(__parent):
                    flat = key.rsplit(cls.SEPARATOR, 2)[-1 - bool(is_iterable)]
                    if is_iterable:
                        if val == _TYPE_MAP:
                            yield flat, dict(cls._load(root, key))
                        else:
                            yield flat, getattr(builtins, val)(
                                child for _, child in cls._load(root, key))
                    else:
                        yield flat, None if val is None else ast.literal_eval(val)
                else:
                    root.append((key, val))
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
            root = list(flat[_CONFIG].items())
            root.reverse()
            # noinspection PyTypeChecker
            self.__init__(self._load(root))


    class REGConfig(_Config):
        SEPARATOR = os.sep

        @classmethod
        def _dump(cls, obj: Iterable, root: dict[str: str | dict], __parent: str):
            for key, val in obj.items() if isinstance(obj, Mapping) else enumerate(obj):
                if isinstance(val, Optional[bool | bytes | complex | float | int | str]):
                    root[__parent][key] = repr(val)
                elif isinstance(val, Iterable):
                    child = key if __parent == _CONFIG else f'{__parent}{cls.SEPARATOR}{key}'
                    root[__parent][f'{key}{cls.SEPARATOR}'] = _TYPE_MAP if isinstance(
                        val, Mapping) else type(val).__name__
                    root[child] = {}
                    cls._dump(val, root, child)
            return root

        @classmethod
        def _load(cls, obj: configparser.SectionProxy, root: configparser.ConfigParser,
                  __parent: str = '') -> Generator[tuple[str, _T], None, None]:
            for key, val in obj.items():
                if key.endswith(cls.SEPARATOR):
                    parent = __parent + key
                    reg = root[parent[:-1]]
                    if val == _TYPE_MAP:
                        yield key[:-1], dict(cls._load(reg, root, parent))
                    else:
                        yield key[:-1], getattr(builtins, val)(
                            child for _, child in cls._load(reg, root, parent))
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
    import tomlkit
except ImportError:
    tomlkit = None
else:
    class TOMLConfig(_Config):
        def dumps(self) -> str:
            return tomlkit.dumps(self)

        def loads(self, data: bytes | str):
            self.update(tomlkit.loads(data))

try:
    import yaml
except ImportError:
    yaml = None
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

        def loads(self, data: bytes | str):
            self.update(yaml.full_load(data))


    # noinspection PyTypeChecker
    yaml.add_representer(YAMLConfig, yaml.representer.SafeRepresenter.represent_dict)
