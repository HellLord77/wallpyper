from __future__ import annotations as _

__version__ = '0.0.5'

import html.parser
import itertools
import re
import shutil
import typing
from typing import Callable, Container, IO, Iterable, Iterator, Mapping, Optional

_TPattern = str | re.Pattern | Container[str] | Callable[[str], bool]

_VOIDS = (
    'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
    'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr')

# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE


class _Parser(html.parser.HTMLParser):
    def __init__(self):
        self.root = None
        self.elems = []
        self.decls = []
        self.handle_decl = self.decls.append
        super().__init__()

    def __del__(self):
        if self.root is not None:
            self.root.decls = tuple(self.decls)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]):
        elem = Element(tag, {name: '' if value is None else value for name, value in reversed(
            attrs)}, self.elems[-1] if self.elems else None)
        if self.root is None:
            self.root = elem
        if tag not in _VOIDS:
            self.elems.append(elem)

    def handle_endtag(self, tag: str):
        # if tag not in _VOIDS:
        if self.elems[-1].name == tag:
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

    def __eq__(self, other):
        return str(self) == str(other)

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
            if inner or self.name not in _VOIDS else f'{start}/>')

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
    def get_class(self) -> set[str]:
        pass

    @typing.overload
    def get_class(self, index: int = 0) -> Optional[str]:
        pass

    def get_class(self, index=None):
        classes = self.attributes.get('class', '').split()
        if index is None:
            return set(classes)
        else:
            try:
                return classes[index]
            except IndexError:
                pass

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

    def get_next_sibling(self) -> Optional[Element]:
        for sibling in self.iter_next_siblings():
            return sibling

    def get_previous_sibling(self) -> Optional[Element]:
        for sibling in self.iter_previous_siblings():
            return sibling

    def iter_next_siblings(self) -> itertools.islice[Element]:
        if self.parent:
            return itertools.islice(self.parent.children, self.parent.children.index(self) + 1, None)

    def iter_previous_siblings(self) -> itertools.islice[Element]:
        if self.parent:
            return itertools.islice(self.parent.children, None, self.parent.children.index(self))

    # noinspection PyShadowingBuiltins
    def find(self, name: Optional[_TPattern] = None, attributes: Optional[Mapping[str, Optional[_TPattern]]] = None,
             filter: Optional[Callable[[Element], bool]] = None, recursive: bool = True) -> Optional[Element]:
        return find_element(self.iter_all_children() if recursive else self.children, name, attributes, filter)

    # noinspection PyShadowingBuiltins
    def find_all(self, name: Optional[_TPattern] = None, attributes: Optional[Mapping[str, Optional[_TPattern]]] = None,
                 filter: Optional[Callable[[Element], bool]] = None, recursive: bool = True) -> Iterator[Element]:
        return find_elements(self.iter_all_children() if recursive else self.children, name, attributes, filter)


def _match(pattern: Optional[_TPattern], string: Optional[str]) -> bool:
    if pattern is None:
        return True
    elif string is None:
        return False
    elif isinstance(pattern, str):
        return string == pattern
    elif isinstance(pattern, re.Pattern):
        return bool(pattern.fullmatch(string))
    elif isinstance(pattern, Container):
        return string in pattern
    else:
        return pattern(string)


# noinspection PyShadowingBuiltins
def find_element(parent_or_elements: Element | Iterable[Element], name: Optional[_TPattern] = None,
                 attributes: Optional[Mapping[str, Optional[_TPattern]]] = None,
                 filter: Optional[Callable[[Element], bool]] = None) -> Optional[Element]:
    for element in find_elements(parent_or_elements, name, attributes, filter):
        return element


# noinspection PyShadowingBuiltins
def find_elements(parent_or_elements: Element | Iterable[Element], name: Optional[_TPattern] = None,
                  attributes: Optional[Mapping[str, Optional[_TPattern]]] = None,
                  filter: Optional[Callable[[Element], bool]] = None, count: int = -1) -> Iterator[Element]:
    if isinstance(parent_or_elements, Element):
        parent_or_elements = parent_or_elements.children
    for element in parent_or_elements:
        if not count:
            break
        if not _match(name, element.name):
            continue
        if attributes is not None:
            not_match = True
            for name_, value in attributes.items():
                if not _match(value, element.attributes.get(name_)):
                    break
            else:
                not_match = False
            if not_match:
                continue
        if filter is not None and not filter(element):
            continue
        yield element
        count -= 1


def load(file: IO) -> Optional[Element]:
    parser = _Parser()
    while buffer := file.read(MAX_CHUNK):
        parser.feed(buffer)
    return parser.root


def loads(data: str) -> Optional[Element]:
    parser = _Parser()
    parser.feed(data)
    return parser.root
