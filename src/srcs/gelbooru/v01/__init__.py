from __future__ import annotations as _

import functools
import hashlib
import json
import os
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from .. import GelbooruSource
from .. import _tag_rating
from .. import _yaml_to_json
from ... import CONFIG_ORIENTATIONS
from ... import Hash
from ... import ImageFile

URL_FMT = request.join_url('{}', 'index.php')

CONFIG_MODE = 'mode'
CONFIG_TAGS = 'tags'
CONFIG_RATING = 'rating'
CONFIG_ID = 'id'

MODES = 'tag', 'favorite', 'random'
RATINGS = 'Safe', 'Questionable', 'Explicit'

_PARAMS = dict(zip(MODES, (
    {'page': 'post', 's': 'list'},
    {'page': 'favorites', 's': 'view'},
    {'page': 'post', 's': 'random'})))
_PARAMS_POST = {'page': 'post', 's': 'view'}
_ATTRS_PAGE = {'id': 'paginator'}
_ATTRS_IMAGE = {'id': 'image'}
_ATTRS_TAGS = {'id': 'tag_list'}


class GelbooruV01Hash(Hash):
    # noinspection PyMissingConstructor
    def __init__(self, data: bytes = b''):
        self._md5 = hashlib.new('md5', data)

    def update(self, data: bytes):
        self._md5.update(data)

    def hexdigest(self):
        return hashlib.sha1(self._md5.hexdigest().encode()).hexdigest()

    def copy(self) -> GelbooruV01Hash:
        other = type(self)()
        other._md5 = self._md5.copy()
        return other

    digest_size = 20

    @property
    def block_size(self) -> int:
        return self._md5.block_size


class GelbooruV01Source(GelbooruSource, source=False):
    NAME = 'Beta 0.1'
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
        mode_random = mode == MODES[2]
        query = _PARAMS[mode].copy()
        if mode == MODES[0]:
            tags = set(params[CONFIG_TAGS])
            tags.update(_tag_rating(RATINGS, params[CONFIG_RATING]))
            if tags:
                query[CONFIG_TAGS] = ' '.join(tags)
        elif mode == MODES[1]:
            query[CONFIG_ID] = str(params[CONFIG_ID])
        pid = '0'
        while True:
            if not posts:
                query['pid'] = pid
                response = request.get(url, query, allow_redirects=False)
                if response:
                    if mode_random:
                        posts = [request.extract_params(response.next.full_url)['id'][0]]
                    else:
                        html = sgml.loads(response.text)
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
            stats = json.loads(_yaml_to_json(tags.get_text(sep='\n')))
            hash_, ext = os.path.splitext(os.path.basename(link))
            width, height = map(int, stats['Size'].split('x'))
            rating = stats['Rating']
            yield ImageFile(link, f'{post} ' + ' '.join(request.get_params(
                tag['href'])['tags'][0] for tag in tags.find_all('a')) + ext, url=url_post,
                            hashes={GelbooruV01Hash: hash_}, width=width, height=height,
                            sketchy=rating == RATINGS[1], nsfw=rating == RATINGS[2])

    @classmethod
    def _on_mode(cls, enable_rating: Callable[[bool], bool], mode: str):
        enable_rating(mode == MODES[0])


from . import (
    allgirl,
    blackedbooru,
    celebbooru,
    drunkenpumken,
    footfetishbooru,
    holobooru,
    myfapbooru,
    steambanners,
    thecollection)  # NOQA: E402
