__version__ = '0.0.2'

import ast
import builtins
import collections
import contextlib
import io
import os
from typing import Any, Generator, IO, Iterable, Mapping, Optional

_T = Optional[bool | bytes | complex | float | int | str | Iterable | Mapping]
_TFile = bytes | str | os.PathLike[bytes] | os.PathLike[str] | IO
_TYPE_MAP = '_'
_TAG_SECTION = '_'


@contextlib.contextmanager
def _open(path_or_file: _TFile, write: bool = False, encoding: Optional[str] = None) -> Generator[IO, None, None]:
    if hasattr(path_or_file, 'write' if write else 'read'):
        yield path_or_file
    else:
        with open(path_or_file, 'w' if write else 'r', encoding=encoding) as file:
            yield file


class _Config(dict[str, _T]):
    pass


try:
    import json
except ImportError:
    json = None
else:
    class JSONConfig(_Config):
        @staticmethod
        def _default(o: Any) -> Any:
            if isinstance(o, Mapping):
                if not isinstance(o, dict):
                    return dict(o)
            elif isinstance(o, Iterable):
                if not isinstance(o, (list, tuple)):
                    return tuple(o)
            raise TypeError(f'Object of type {type(o)} is not JSON serializable')

        def dump(self, path_or_file: _TFile, indent: Optional[int] = None):
            with _open(path_or_file, True) as file:
                json.dump(self, file, indent=indent, default=self._default)

        def dumps(self, indent: Optional[int] = 2) -> str:
            return json.dumps(self, indent=indent, default=self._default)

        def load(self, path_or_file: _TFile):
            with _open(path_or_file, True) as file:
                self.update(json.load(file))

        def loads(self, data: str | bytes):
            self.update(json.loads(data))

# FIXME YAMLConfig

try:
    from xml.etree import ElementTree
except ImportError:
    ElementTree = None
else:
    class XMLConfig(_Config):
        _type_key: str = '_'

        @classmethod
        def _dump(cls, obj: _T, root: ElementTree.Element) -> ElementTree.Element:
            if obj is None:
                pass
            elif isinstance(obj, bool | bytes | complex | float | int | str):
                text = repr(obj)
                if __debug__:
                    ast.literal_eval(text)
                root.text = text
            elif isinstance(obj, Mapping):
                root.attrib[cls._type_key] = _TYPE_MAP
                for key, val in obj.items():
                    cls._dump(val, ElementTree.SubElement(root, key))
            elif isinstance(obj, Iterable):
                type_ = type(obj).__name__
                try:
                    getattr(builtins, type_)
                except AttributeError:
                    raise TypeError(f'Iterable of type {type_} is not XML serializable')
                else:
                    root.attrib[cls._type_key] = type_
                    for val in obj:
                        cls._dump(val, ElementTree.SubElement(root, cls._type_key))
            else:
                raise TypeError(f'Object of type {type(obj).__name__} is not XML serializable')
            return root

        @classmethod
        def _load(cls, root: ElementTree.Element) -> _T:
            if (type_ := root.attrib.get(cls._type_key)) is None:
                return ast.literal_eval(str(root.text))
            elif type_ == _TYPE_MAP:
                return {child.tag: cls._load(child) for child in root}
            else:
                return getattr(builtins, type_)(cls._load(child) for child in root)

        def dump(self, path_or_file: _TFile, indent: Optional[int] = None, encoding: Optional[str] = None):
            tree = ElementTree.ElementTree(self._dump(
                self, ElementTree.Element(_TAG_SECTION, {self._type_key: _TYPE_MAP})))
            if indent is not None:
                ElementTree.indent(tree, ' ' * indent)
            tree.write(path_or_file, encoding=encoding)

        def dumps(self, indent: Optional[int] = 2) -> str:
            stream = io.StringIO()
            self.dump(stream, indent, 'unicode')
            return stream.getvalue()

        def load(self, file: _TFile):
            self.update(self._load(ElementTree.parse(file).getroot()))

        def loads(self, data: bytes | str):
            self.update(self._load(ElementTree.fromstring(data)))

try:
    import configparser
except ImportError:
    configparser = None
else:
    class REGConfig(_Config):
        @staticmethod
        def _configparser() -> configparser.ConfigParser:
            parser = configparser.ConfigParser(allow_no_value=True)
            parser.optionxform = str
            return parser

        @classmethod
        def _dump(cls, obj: _T, root: dict[str, str], __parent: str = ''):
            if obj is None:
                return ''
            elif isinstance(obj, bool | bytes | complex | float | int | str):
                val = repr(obj)
                if __debug__:
                    ast.literal_eval(val)
                return val
            elif isinstance(obj, Iterable):
                if __parent:
                    __parent += os.sep
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
                        root[parent + os.sep] = type_
                        root.update(children)
                    else:
                        root[parent] = dumped
                return root
            else:
                raise TypeError(f'Object of type {type(obj).__name__} is not REG serializable')

        @classmethod
        def _load(cls, root: collections.deque[tuple[str, str]],
                  __parent: str = '') -> Generator[tuple[str, _T], None, None]:
            while root:
                key, val = root.popleft()
                is_iterable = key.endswith(os.sep)
                if key.startswith(__parent):
                    reg = key.rsplit(os.sep, 2)[-1 - bool(is_iterable)]
                    if is_iterable:
                        if val == _TYPE_MAP:
                            yield reg, dict(cls._load(root, key))
                        else:
                            yield reg, getattr(builtins, val)(
                                child for _, child in cls._load(root, key))
                    else:
                        yield reg, ast.literal_eval(val) if val else None
                else:
                    root.appendleft((key, val))
                    break

        def dump(self, path_or_file: _TFile):
            reg = self._configparser()
            reg.read_dict({_TAG_SECTION: self._dump(self, {})})
            with _open(path_or_file, True) as file:
                reg.write(file)

        def dumps(self) -> str:
            stream = io.StringIO()
            self.dump(stream)
            return stream.getvalue()

        def load(self, path_or_file: _TFile, encoding: Optional[str] = None):
            reg = self._configparser()
            with _open(path_or_file, encoding=encoding) as file:
                reg.read_file(file)
            # noinspection PyTypeChecker
            self.update(dict(self._load(collections.deque(reg[_TAG_SECTION].items()))))

        def loads(self, data: str):
            stream = io.StringIO(data)
            self.load(stream)

try:
    import tomlkit
except ImportError:
    tomlkit = None
else:
    pass  # TODO
