__version__ = '0.0.1'

import ast
import builtins
import collections
import configparser
import io
import json
import os
from typing import Any, Generator, IO, Iterable, Mapping, Optional
from xml.etree import ElementTree

_T = Optional[bool | bytes | complex | float | int | str | Iterable | Mapping]
_TYPE_MAP = 'tree'
_TAG_SECTION = '_'


class _Config(dict[str, _T]):
    pass


class JSONConfig(_Config):
    class _Encoder(json.JSONEncoder):
        def default(self, o: Any) -> Any:
            if isinstance(o, Mapping):
                if not isinstance(o, dict):
                    return dict(o)
            elif isinstance(o, Iterable):
                if not isinstance(o, (list, tuple)):
                    return tuple(o)
            return super().default(o)

    def dump(self, file: str | IO, indent: Optional[int] = None):
        if not hasattr(file, 'write'):
            file = open(file, 'w')
        json.dump(self, file, cls=self._Encoder, indent=indent)

    def dumps(self, indent: Optional[int] = 2) -> str:
        return json.dumps(self, cls=self._Encoder, indent=indent)

    def load(self, file: str | IO):
        if not hasattr(file, 'read'):
            file = open(file)
        self.update(json.load(file))

    def loads(self, data: str | bytes):
        self.update(json.loads(data))


# FIXME TOMLConfig
# FIXME YAMLConfig

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

    def dump(self, file: str | IO, indent: Optional[int] = None, encoding: Optional[str] = None):
        tree = ElementTree.ElementTree(self._dump(
            self, ElementTree.Element(_TAG_SECTION, {self._type_key: _TYPE_MAP})))
        if indent is not None:
            ElementTree.indent(tree, ' ' * indent)
        tree.write(file, encoding=encoding)

    def dumps(self, indent: Optional[int] = 2) -> str:
        stream = io.StringIO()
        self.dump(stream, indent, 'unicode')
        return stream.getvalue()

    def load(self, file: str | IO):
        self.update(self._load(ElementTree.parse(file).getroot()))

    def loads(self, data: bytes | str):
        self.update(self._load(ElementTree.fromstring(data)))


class REGConfig(_Config):
    class _Parser(configparser.ConfigParser):
        optionxform = str

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

    def dump(self, file: str | IO):
        if not hasattr(file, 'write'):
            file = open(file, 'w')
        reg = self._Parser()
        reg.read_dict({_TAG_SECTION: self._dump(self, {})})
        reg.write(file)

    def dumps(self) -> str:
        stream = io.StringIO()
        self.dump(stream)
        return stream.getvalue()

    def load(self, file: str | IO, encoding: Optional[str] = None):
        reg = self._Parser()
        reg.read_file(file) if hasattr(file, 'read') else reg.read(file, encoding)
        # noinspection PyTypeChecker
        self.update(dict(self._load(collections.deque(reg[_TAG_SECTION].items()))))

    def loads(self, data: str):
        stream = io.StringIO(data)
        self.load(stream)
