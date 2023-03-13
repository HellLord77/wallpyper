from __future__ import annotations as _

__version__ = '0.0.2'

import html.parser
import itertools
import re
import shutil
from typing import Callable, Container, IO, Iterable, Iterator, Mapping, Optional

_TPattern = str | re.Pattern | Container[str] | Callable[[str], bool]

_VOIDS = (
    'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
    'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr')

# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE


class _Parser(html.parser.HTMLParser):
    def __init__(self):
        self._elems = []
        self.root = None
        self.decls = []
        super().__init__()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]):
        element = Element(tag, dict(reversed(
            attrs)), self._elems[-1] if self._elems else None)
        # if tag not in _VOIDS:
        self._elems.append(element)
        if self.root is None:
            self.root = self._elems[0]
        if self.decls:
            self._elems[-1].decls = tuple(self.decls)
            self.decls.clear()

    def handle_endtag(self, tag: str):
        # if tag not in _VOIDS:
        if self._elems[-1].name == tag:
            del self._elems[-1]

    def handle_data(self, data: str):
        if self._elems:
            self._elems[-1].datas.append(data)

    def handle_comment(self, data: str):
        if self._elems:
            self._elems[-1].comments.append(data)

    def handle_decl(self, decl: str):
        self.decls.append(decl)


class Element:
    def __init__(self, name: str, attributes: dict[str, Optional[str]], parent: Optional[Element]):
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
            attributes += f' {name}="{value}"'
        return f'<{self.name}{attributes}>{"".join(map(str, self.children))}</{self.name}>' \
            if self.children or self.name not in _VOIDS else f'<{self.name}{attributes}/>'

    def get_child(self, index: int = 0) -> Optional[Element]:
        try:
            return self.children[index]
        except IndexError:
            pass

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
