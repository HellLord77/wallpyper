from __future__ import annotations

__version__ = '0.0.9'

import html.parser
import io
import itertools
import re
import shutil
import typing
from typing import Callable, Container, Iterable, Iterator, Mapping, Optional, TextIO

_TPattern = (bool | int | bytes | str | re.Pattern |
             Iterable['_TPattern'] | Container[str] | Callable[[str], bool])

# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE

VOID_HTML4 = {
    'area', 'base', 'basefont', 'br', 'col', 'frame', 'hr',
    'img', 'input', 'isindex', 'link', 'meta', 'param'}
VOID_HTML401 = {
    'area', 'base', 'basefont', 'br', 'col', 'frame', 'hr',
    'img', 'input', 'isindex', 'link', 'meta', 'param'}
VOID_HTML5 = {
    'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
    'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class _Parser(html.parser.HTMLParser):
    def __init__(self, void: Container[str], ignore: Container[str]):
        self.void = void
        self.ignore = ignore
        self.root = None
        self.elems = []
        self.decls = []
        self.handle_decl = self.decls.append
        super().__init__()

    def __del__(self):
        if self.root is not None:
            self.root.decls = tuple(self.decls)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]):
        if tag not in self.ignore:
            elem = Element(tag, {name: '' if value is None else value
                                 for name, value in reversed(attrs)},
                           self.elems[-1] if self.elems else None)
            if self.root is None:
                self.root = elem
            if tag not in self.void:
                self.elems.append(elem)

    def handle_endtag(self, tag: str):
        if tag not in self.void and tag not in self.ignore:
            while self.elems[-1].name != tag:
                del self.elems[-1]
            del self.elems[-1]

    def handle_data(self, data: str):
        if self.elems:
            self.elems[-1].datas.append(data)

    def handle_comment(self, data: str):
        if self.elems:
            self.elems[-1].comments.append(data)


class Element:
    def __init__(self, name: str, attributes: dict[str, str], parent: Optional[Element]):
        self.name = name
        self.attributes = attributes
        self.parent = parent
        self.children = []
        self.datas = []
        self.comments = []
        self.decls = ()
        if parent:
            parent.children.append(self)

    def __str__(self):
        attributes = ''
        for name, value in sorted(self.attributes.items()):
            attributes += f' {name}'
            if value:
                attributes += f'="{value}"'
        start = f'<{self.name}{attributes}'
        inner = self.children or self.datas
        return ''.join(f'<!{decl}>' for decl in self.decls) + (
            f'{start}>{"".join(map(str, inner))}</{self.name}>'
            if inner else f'{start}/>')

    @typing.overload
    def __getitem__(self, item: str) -> str:
        pass

    @typing.overload
    def __getitem__(self, item: int) -> Element:
        pass

    @typing.overload
    def __getitem__(self, item: slice) -> list[Element]:
        pass

    def __getitem__(self, item):
        return (self.attributes if isinstance(item, str) else self.children)[item]

    def get_root(self) -> Element:
        return self if self.parent is None else self.parent.get_root()

    def get_child(self, index: int = 0) -> Optional[Element]:
        try:
            return self.children[index]
        except IndexError:
            pass

    def get_data(self, index: int = 0) -> Optional[str]:
        try:
            return self.datas[index]
        except IndexError:
            pass

    @typing.overload
    def get_class(self) -> list[str]:
        pass

    @typing.overload
    def get_class(self, index: int = 0) -> Optional[str]:
        pass

    @typing.overload
    def get_class(self, index: slice) -> list[str]:
        pass

    def get_class(self, index=None):
        classes = self.attributes.get('class', '').split()
        if index is None:
            return classes
        else:
            try:
                return classes[index]
            except IndexError:
                pass

    @typing.overload
    def get_text(self, stop: Optional[int] = None, /) -> str:
        pass

    @typing.overload
    def get_text(self, start: Optional[int] = None, stop: Optional[int] = None, /) -> str:
        pass

    def get_text(self, start=None, stop=None, /):
        return ''.join(map(str.strip, itertools.islice(self.datas, start, stop)))

    def get_doctype(self) -> Optional[str]:
        for decl in self.get_root().decls:
            if decl[:7].upper() == 'DOCTYPE':
                return decl[7:].strip()

    def iter_all_children(self, depth: int = -1) -> Iterator[Element]:
        if depth:
            for child in self.children:
                yield child
                yield from child.iter_all_children(depth - 1)

    def iter_all_parents(self, height: int = -1) -> Iterator[Element]:
        if height and self.parent:
            yield self.parent
            yield from self.parent.iter_all_parents(height - 1)

    def get_next_sibling(self, index: int = 0) -> Optional[Element]:
        return next(itertools.islice(self.iter_next_siblings(), index, None), None)

    def get_previous_sibling(self, index: int = 0) -> Optional[Element]:
        return next(itertools.islice(self.iter_previous_siblings(), index, None), None)

    def iter_next_siblings(self) -> Iterator[Element]:
        if self.parent:
            yield from itertools.islice(
                self.parent.children, self.parent.children.index(self) + 1, None)

    def iter_previous_siblings(self) -> Iterator[Element]:
        if self.parent:
            yield from itertools.islice(reversed(self.parent.children), len(
                self.parent.children) - self.parent.children.index(self), None)

    # noinspection PyShadowingBuiltins
    def find(self, name: Optional[_TPattern] = None,
             attributes: Optional[Mapping[str, _TPattern]] = None, classes: Optional[_TPattern] = None,
             text: Optional[_TPattern] = None, filter: Optional[Callable[[Element], bool]] = None,
             recursive: bool = True, index: int = 0) -> Optional[Element]:
        return find_element(self.iter_all_children() if recursive
                            else self.children, name, attributes, classes, text, filter, index)

    # noinspection PyShadowingBuiltins
    def find_all(self, name: Optional[_TPattern] = None,
                 attributes: Optional[Mapping[str, _TPattern]] = None, classes: Optional[_TPattern] = None,
                 text: Optional[_TPattern] = None, filter: Optional[Callable[[Element], bool]] = None,
                 recursive: bool = True, count: int = -1) -> Iterator[Element]:
        return find_elements(self.iter_all_children() if recursive
                             else self.children, name, attributes, classes, text, filter, count)


def _match(pattern: _TPattern, string: Optional[str]) -> bool:
    if pattern is True:
        return True
    elif string is None:
        return pattern is False
    elif isinstance(pattern, int):
        return pattern == len(string)
    elif isinstance(pattern, bytes):
        return pattern == string.encode()
    elif isinstance(pattern, str):
        return pattern == string
    elif isinstance(pattern, re.Pattern):
        return bool(pattern.search(string))
    elif isinstance(pattern, Iterable):
        return any(_match(pattern_, string) for pattern_ in pattern)
    elif isinstance(pattern, Container):
        return string in pattern
    elif callable(pattern):
        return pattern(string)
    else:
        raise TypeError(f'{type(pattern).__name__} is not subclass of {_TPattern}')


# noinspection PyShadowingBuiltins
def find_element(elements: Iterable[Element], name: Optional[_TPattern] = None,
                 attributes: Optional[Mapping[str, _TPattern]] = None,
                 classes: Optional[_TPattern] = None, text: Optional[_TPattern] = None,
                 filter: Optional[Callable[[Element], bool]] = None, index: int = 0) -> Optional[Element]:
    return next(itertools.islice(find_elements(elements, name, attributes, classes, text, filter), index, None), None)


# noinspection PyShadowingBuiltins
def find_elements(elements: Iterable[Element], name: Optional[_TPattern] = None,
                  attributes: Optional[Mapping[str, _TPattern]] = None,
                  classes: Optional[_TPattern] = None, text: Optional[_TPattern] = None,
                  filter: Optional[Callable[[Element], bool]] = None, count: int = -1) -> Iterator[Element]:
    for element in elements:
        if not count:
            break
        if name is not None and not _match(name, element.name):
            continue
        if attributes is not None and not all(_match(value, element.attributes.get(
                attribute)) for attribute, value in attributes.items()):
            continue
        if classes is not None and not any(_match(
                classes, class_) for class_ in element.get_class()):
            continue
        if text is not None and not _match(text, element.get_text() or None):
            continue
        if filter is not None and not filter(element):
            continue
        yield element
        count -= 1


def load(file: TextIO, void: Container[str] = (),
         ignore: Container[str] = ()) -> Optional[Element]:
    parser = _Parser(void, ignore)
    while buffer := file.read(MAX_CHUNK):
        parser.feed(buffer)
    parser.close()
    return parser.root


def loads(data: str, void: Container[str] = (),
          ignore: Container[str] = ()) -> Optional[Element]:
    return load(io.StringIO(data), void, ignore)
