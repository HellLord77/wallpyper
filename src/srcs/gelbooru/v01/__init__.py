from __future__ import annotations

import functools
import hashlib
import itertools
import json
import os
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import request, sgml
from .. import GelbooruSource
from ... import CONFIG_ORIENTATIONS, Hash, ImageFile

URL_FMT = request.join_url('{}', 'index.php')

CONFIG_MODE = 'mode'
CONFIG_TAGS = 'tags'
CONFIG_RATING = 'rating'
CONFIG_ID = 'id'

MODES = 'tag', 'favorite', 'random'
RATINGS = 'Safe', 'Questionable', 'Explicit'

_IGNORES = 'center',
_PARAMS_TAGS = {'page': 'post', 's': 'list'}
_PARAMS_RANDOM = {'page': 'post', 's': 'random'}
_PARAMS_POST = {'page': 'post', 's': 'view'}
_ATTRS_PAGE = {'id': 'paginator'}
_ATTRS_TAGS = {'id': 'tag_list'}
_ATTRS_IMAGE = {'id': "image"}


def _yml_to_json(yml: str) -> str:
    return '{"' + yml.replace(':\n', ': null\n').replace(
        '\n', '","').replace(': ', '":"') + '"}'


def _tag_rating(ratings: list[bool]) -> Iterator[str]:
    count = sum(ratings)
    filtered = itertools.compress(RATINGS, ratings)
    if count == 1:
        yield 'rating:' + next(filtered)
    elif count == 2:
        filtered = tuple(filtered)
        for rating in RATINGS:
            if rating not in filtered:
                yield '-rating:' + rating
                break


class GelbooruHash(Hash):
    # noinspection PyMissingConstructor
    def __init__(self, data: bytes = b''):
        self._md5 = hashlib.new('md5', data)

    def update(self, data: bytes):
        self._md5.update(data)

    def hexdigest(self):
        return hashlib.sha1(self._md5.hexdigest().encode()).hexdigest()

    def copy(self) -> GelbooruHash:
        other = type(self)()
        other._md5 = self._md5.copy()
        return other

    digest_size = 20

    @property
    def block_size(self) -> int:
        return self._md5.block_size


class GelbooruV01Source(GelbooruSource, source=False):
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_MODE: str,
        CONFIG_TAGS: list[str],
        CONFIG_RATING: list[bool],
        CONFIG_ID: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_MODE: MODES[0],
        CONFIG_TAGS: [],
        CONFIG_RATING: [True, True, True],
        CONFIG_ID: 0}

    def __init_subclass__(cls, *args, **kwargs):
        cls._text = GelbooruV01Source._text
        super().__init_subclass__(*args, **kwargs)

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_MODE, MODES)
        cls._fix_config(validator.ensure_len, CONFIG_RATING, 3)
        cls._fix_config(validator.ensure_truthy, CONFIG_RATING, any)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        enable_rating = gui.add_submenu_check(cls._text(
            'MENU_RATING'), (cls._text(f'RATING_{rating}') for rating in range(3)),
            (1, None), cls.CURRENT_CONFIG, CONFIG_RATING).enable
        on_mode = functools.partial(cls._on_mode, enable_rating)
        gui.add_submenu_radio(cls._text('MENU_MODE'), {mode: cls._text(
            f'MODE_{mode}') for mode in MODES}, cls.CURRENT_CONFIG,
                              CONFIG_MODE, on_click=on_mode, position=0)
        on_mode(cls.CURRENT_CONFIG[CONFIG_MODE])
        gui.add_separator()
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        posts = []
        url = URL_FMT.format(cls.URL)
        mode = params[CONFIG_MODE]
        if mode == MODES[0]:
            tags = set(params[CONFIG_TAGS])
            tags.update(_tag_rating(params[CONFIG_RATING]))
            params = _PARAMS_TAGS.copy()
            if tags:
                params[CONFIG_TAGS] = ' '.join(tags)
        elif mode == MODES[1]:
            params = {
                CONFIG_ID: str(params[CONFIG_ID]),
                'page': 'favorites',
                's': 'view'}
        else:
            params = _PARAMS_RANDOM
        pid = '0'
        while True:
            if not posts:
                params['pid'] = pid
                response = request.get(url, params, allow_redirects=False)
                if response:
                    if mode == MODES[2]:
                        posts = [request.extract_params(response.next.full_url)['id'][0]]
                    else:
                        html = sgml.loads(response.text, ignore=_IGNORES)
                        posts = [thumb[0]['id'][1:] for thumb
                                 in html.find_all('span', classes='thumb')]
                        next_page = html.find('div', _ATTRS_PAGE).find(
                            'b', recursive=False).get_next_sibling()
                        if next_page is None:
                            pid = '0'
                        else:
                            pid = request.extract_params(next_page['href'])['pid'][0]
                if not posts:
                    yield
                    continue
            post = posts.pop(0)
            url_post = request.encode_params(url, {CONFIG_ID: post, **_PARAMS_POST})
            response_post = request.get(url_post)
            if not response_post:
                posts.insert(0, post)
                yield
                continue
            html_post = sgml.loads(response_post.text)
            link = html_post.find('img', _ATTRS_IMAGE)['src']
            tags = html_post.find('div', _ATTRS_TAGS)[1]
            stats = json.loads(_yml_to_json(tags.get_text(sep='\n')))
            name, ext = os.path.splitext(os.path.basename(link))
            width, height = map(int, stats['Size'].split('x'))
            rating = stats['Rating']
            yield ImageFile(link, f'{post} ' + ' '.join(request.get_params(
                tag['href'])['tags'][0] for tag in tags.find_all('a')) + ext, url=url_post,
                            hash={GelbooruHash: name}, width=width, height=height,
                            sketchy=rating == RATINGS[1], nsfw=rating == RATINGS[2])

    @classmethod
    def _on_mode(cls, enable_rating: Callable[[bool], bool], mode: str):
        enable_rating(mode == MODES[0])


from . import (
    allgirl)  # NOQA: E402
