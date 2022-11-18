from __future__ import annotations as _

__version__ = '0.0.1'

import html.parser
import itertools
import re
import shutil
from typing import Callable, Generator, Iterable, Mapping, Optional, IO

_VOIDS = (
    'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img',
    'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr')

# noinspection PyUnresolvedReferences
MAX_CHUNK = shutil.COPY_BUFSIZE


class _Parser(html.parser.HTMLParser):
    def __init__(self):
        self._elements = []
        self.root = None
        self.decls = []
        super().__init__()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]):
        element = Element(tag, dict(attrs), self._elements[-1] if self._elements else None)
        if tag not in _VOIDS:
            self._elements.append(element)
        if self.root is None:
            self.root = self._elements[0]
        if self.decls:
            self._elements[-1].decls = tuple(self.decls)
            self.decls.clear()

    def handle_endtag(self, tag: str):
        if tag not in _VOIDS:
            del self._elements[-1]

    def handle_data(self, data: str):
        if self._elements:
            self._elements[-1].datas.append(data)

    def handle_comment(self, data: str):
        if self._elements:
            self._elements[-1].comments.append(data)

    def handle_decl(self, decl: str):
        self.decls.append(decl)


class Element:
    def __init__(self, tag: str, attrs: dict[str, Optional[str]], parent: Optional[Element]):
        self.name = tag
        self.attributes = attrs
        self.parent = parent
        self.child = []
        self.datas = []
        self.comments = []
        self.decls = ()
        if parent:
            parent.child.append(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __str__(self):
        if self.attributes:
            attributes = ' ' + ' '.join(f'{name}="{value}"' for name, value in self.attributes.items())
        else:
            attributes = ''
        return f'<{self.name}{attributes}>{"".join(str(children) for children in self.child)}</{self.name}>'

    def iter_all_child(self, depth: int = -1) -> Generator[Element, None, None]:
        if depth:
            for children in self.child:
                yield children
                yield from children.iter_all_child(depth - 1)

    def iter_all_parents(self, height: int = -1) -> Generator[Element, None, None]:
        if height and self.parent:
            yield self.parent
            yield from self.parent.iter_all_parents(height - 1)

    def get_next_sibling(self) -> Optional[Element]:
        for sibling in self.iter_next_siblings():
            return sibling

    def get_previous_sibling(self) -> Optional[Element]:
        for sibling in self.iter_previous_siblings():
            return sibling

    def iter_next_siblings(self) -> Generator[Element, None, None]:
        if self.parent:
            yield from itertools.islice(self.parent.child, self.parent.child.index(self) + 1, None)

    def iter_previous_siblings(self) -> Generator[Element, None, None]:
        if self.parent:
            yield from itertools.islice(self.parent.child, None, self.parent.child.index(self))


def _match(pattern: Optional[str | re.Pattern | Callable[[str, ...], bool]], string: Optional[str]) -> bool:
    if pattern is None:
        return True
    elif string is None:
        return False
    elif isinstance(pattern, str):
        return string == pattern
    elif isinstance(pattern, re.Pattern):
        return bool(pattern.fullmatch(string))
    else:
        return pattern(string)


# noinspection PyShadowingBuiltins
def find_element(elements: Iterable[Element], name: Optional[str | re.Pattern | Callable[[str, ...], bool]] = None,
                 attributes: Optional[Mapping[str, Optional[str | re.Pattern | Callable[[str, ...], bool]]]] = None,
                 filter: Optional[Callable[[Element], bool]] = None) -> Optional[Element]:
    for element in find_elements(elements, name, attributes, filter):
        return element


# noinspection PyShadowingBuiltins
def find_elements(elements: Iterable[Element], name: Optional[str | re.Pattern | Callable[[str, ...], bool]] = None,
                  attributes: Optional[Mapping[str, Optional[str | re.Pattern | Callable[[str, ...], bool]]]] = None,
                  filter: Optional[Callable[[Element], bool]] = None, count: int = -1) -> Generator[Element, None, None]:
    for element in elements:
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
