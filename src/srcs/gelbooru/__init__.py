import itertools
from typing import Iterator

from .. import Source


def _tag_rating(ratings: tuple[str, str, str], param: list[bool]) -> Iterator[str]:
    count = sum(param)
    filtered = itertools.compress(ratings, param)
    if count == 1:
        yield 'rating:' + next(filtered)
    elif count == 2:
        filtered = tuple(filtered)
        for rating in ratings:
            if rating not in filtered:
                yield '-rating:' + rating
                break


def _yaml_to_json(yml: str) -> str:
    return '{"' + (yml + '\n').replace(':\n', ': null\n').strip(
    ).replace('\n', '","').replace(': ', '":"') + '"}'


class GelbooruSource(Source, source=False):
    NAME = 'Gelbooru'


from . import (
    v01,
    v02)  # NOQA: E402
