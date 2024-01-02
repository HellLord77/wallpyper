from __future__ import annotations as _

import functools
import json
import os
import re
from typing import Callable
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from libs.request import cloudflare
from .. import GelbooruSource
from .. import _tag_rating
from .. import _yaml_to_json
from ... import CONFIG_ORIENTATIONS
from ... import ImageFile

FLAG_RETRY_IMAGE = True

URL_FMT = request.join_url('{}', 'index.php')

CONFIG_STATIC = '_static'
CONFIG_MODE = 'mode'
CONFIG_TAGS = 'tags'
CONFIG_RATING = 'rating'
CONFIG_SORT = 'sort'
CONFIG_ORDER = 'order'
CONFIG_SIZE = 'size'
CONFIG_WIDTH = 'width'
CONFIG_HEIGHT = 'height'
CONFIG_FAVORITE = 'favorite'
CONFIG_POOL = 'pool'

MODES = 'tag', 'favorite', 'pool', 'random'
RATINGS = 'safe', 'questionable', 'explicit'
SORTS = 'id', 'score', 'rating', 'user', 'height', 'width', 'parent', 'source', 'updated'
ORDERS = 'asc', 'desc'
SIZES = 'bigger', 'exact', 'smaller'
WIDTHS = 2560, 1920, 1680, 1600, 1440, 1400, 1280, 1152, 1024, 0
HEIGHTS = 1600, 1200, 1080, 1050, 1024, 960, 900, 864, 800, 768, 0

_PARAMS = dict(zip(MODES, (
    {'page': 'post', 's': 'list'},
    {'page': 'favorites', 's': 'view'},
    {'page': 'pool', 's': 'show'},
    {'page': 'post', 's': 'random'})))
_PARAMS_API = {'page': 'dapi', 's': 'post', 'q': 'index', 'json': '1'}
_PARAMS_POST = {'page': 'post', 's': 'view'}
_ATTRS_PAGE = {'id': 'paginator'}
_ATTRS_CONTAINER = {'id': 'note-container'}
_ATTRS_IMAGE = {'id': 'image'}
_ATTRS_STATS = {'id': 'stats'}
_TRANS_QUOTES = str.maketrans({'"': "'", "'": '"'})
_RE_PID = re.compile(r'pid=(\d+)')
_RE_IMAGE = re.compile('({.*})')


def _tag_dimension(size: str, width: int, height: int) -> Iterator[str]:
    fmt = '{}'
    if size == SIZES[0]:
        fmt = '>={}'
    elif size == SIZES[2]:
        fmt = '<={}'
    if width:
        yield 'width:' + fmt.format(width)
    if height:
        yield 'height:' + fmt.format(height)


def _tag_sort(sort: str, order: str) -> Iterator[str]:
    if (sort != GelbooruV02Source.DEFAULT_CONFIG[CONFIG_SORT] or
            order != GelbooruV02Source.DEFAULT_CONFIG[CONFIG_ORDER]):
        yield f'sort:{sort}:{order}'


class GelbooruV02Source(GelbooruSource, source=False):
    NAME = 'Beta 0.2'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_STATIC: bool,
        CONFIG_MODE: str,
        CONFIG_TAGS: list[str],
        CONFIG_RATING: list[bool],
        CONFIG_SORT: str,
        CONFIG_ORDER: str,
        CONFIG_SIZE: str,
        CONFIG_WIDTH: int,
        CONFIG_HEIGHT: int,
        CONFIG_FAVORITE: int,
        CONFIG_POOL: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_STATIC: False,
        CONFIG_MODE: MODES[0],
        CONFIG_TAGS: [],
        CONFIG_RATING: [True, True, True],
        CONFIG_SORT: SORTS[0],
        CONFIG_ORDER: ORDERS[1],
        CONFIG_SIZE: SIZES[0],
        CONFIG_WIDTH: WIDTHS[9],
        CONFIG_HEIGHT: HEIGHTS[10],
        CONFIG_FAVORITE: 0,
        CONFIG_POOL: 0}

    def __init_subclass__(cls, *args, **kwargs):
        cls._text = GelbooruV02Source._text
        super().__init_subclass__(*args, **kwargs)

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_MODE, MODES)
        cls._fix_config(validator.ensure_len, CONFIG_RATING, 3)
        cls._fix_config(validator.ensure_truthy, CONFIG_RATING, any)
        cls._fix_config(validator.ensure_contains, CONFIG_SORT, SORTS)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)
        cls._fix_config(validator.ensure_contains, CONFIG_SIZE, SIZES)
        cls._fix_config(validator.ensure_contains, CONFIG_WIDTH, WIDTHS)
        cls._fix_config(validator.ensure_contains, CONFIG_HEIGHT, HEIGHTS)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        item_post = gui.add_submenu(cls._text('MENU_TAG'))
        with gui.set_menu(item_post):
            gui.add_submenu_check(cls._text('MENU_RATING'), (cls._text(
                f'RATING_{rating}') for rating in range(3)),
                                  (1, None), cls.CURRENT_CONFIG, CONFIG_RATING)
            gui.add_submenu_radio(cls._text('MENU_SORT'), {
                sort: cls._text('SORT_' + sort) for sort in SORTS},
                                  cls.CURRENT_CONFIG, CONFIG_SORT)
            gui.add_submenu_radio(cls._text('MENU_ORDER'), {
                order: cls._text('ORDER_' + order) for order in ORDERS},
                                  cls.CURRENT_CONFIG, CONFIG_ORDER)
            gui.add_separator()
            enable_size = gui.add_submenu_radio(cls._text('MENU_SIZE'), {size: cls._text(
                f'SIZE_{size}') for size in SIZES}, cls.CURRENT_CONFIG, CONFIG_SIZE).enable
            on_dimension = functools.partial(cls._on_dimension, enable_size)
            gui.add_submenu_radio(cls._text('MENU_WIDTH'), {width: cls._text(
                width if width else 'WIDTH_0') for width in WIDTHS}, cls.CURRENT_CONFIG,
                                  CONFIG_WIDTH, on_click=on_dimension, position=-1)
            gui.add_submenu_radio(cls._text('MENU_HEIGHT'), {height: cls._text(
                height if height else 'HEIGHT_0') for height in HEIGHTS}, cls.CURRENT_CONFIG,
                                  CONFIG_HEIGHT, on_click=on_dimension, position=-1)
            on_dimension()
        on_mode = functools.partial(cls._on_mode, item_post.enable)
        gui.add_submenu_radio(cls._text('MENU_MODE'), {mode: cls._text(
            f'MODE_{mode}') for mode in MODES}, cls.CURRENT_CONFIG,
                              CONFIG_MODE, on_click=on_mode, position=0)
        on_mode(cls.CURRENT_CONFIG[CONFIG_MODE])
        gui.add_separator()
        gui.add_menu_item_check(cls._text('LABEL_STATIC'), cls.CURRENT_CONFIG, CONFIG_STATIC)
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        posts = []
        url = URL_FMT.format(cls.URL)
        mode = params[CONFIG_MODE]
        mode_favorite = mode == MODES[1]
        mode_random = mode == MODES[3]
        query = _PARAMS[mode].copy()
        if mode == MODES[0]:
            tags = set(params[CONFIG_TAGS])
            tags.update(_tag_rating(RATINGS, params[CONFIG_RATING]))
            tags.update(_tag_sort(params[CONFIG_SORT], params[CONFIG_ORDER]))
            tags.update(_tag_dimension(
                params[CONFIG_SIZE], params[CONFIG_WIDTH], params[CONFIG_HEIGHT]))
            if tags:
                query[CONFIG_TAGS] = ' '.join(tags)
        elif mode == MODES[1]:
            query['id'] = str(params[CONFIG_FAVORITE])
        elif mode == MODES[2]:
            query['id'] = str(params[CONFIG_POOL])
        session = cloudflare.Session()
        pid = '0'
        while True:
            if not posts:
                query['pid'] = pid
                response = session.get(url, query, allow_redirects=False)
                if response:
                    if mode_random:
                        posts = [request.extract_params(response.next.full_url)['id'][0]]
                    else:
                        html = sgml.loads(response.text)
                        posts = [(thumb[0] if mode_favorite else thumb)['id'][1:]
                                 for thumb in html.find_all(classes='thumb')]
                        paginator = html.find('div', _ATTRS_PAGE)
                        if paginator is not None:
                            paginator = paginator.find('b').get_next_sibling()
                        if paginator is None:
                            pid = '0'
                        else:
                            if mode_favorite:
                                pid = _RE_PID.search(paginator['onclick']).group(1)
                            else:
                                pid = request.extract_params(paginator['href'])['pid'][0]
                if not posts:
                    yield
                    continue
            post = posts.pop(0)
            image = cls._get_image_api(post, session)
            if FLAG_RETRY_IMAGE and image is None:
                image = cls._get_image_scrape(post, session)
            if image is None:
                posts.insert(0, post)
                yield
                continue
            yield image

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if cls.CURRENT_CONFIG[CONFIG_STATIC] and not image.is_static():
            return False
        return super().filter_image(image)

    @classmethod
    def _on_mode(cls, enable_tag: Callable[[bool], bool], mode: str):
        enable_tag(mode == MODES[0])

    @classmethod
    def _on_dimension(cls, enable: Callable[[bool], bool], _: Optional[int] = None):
        enable(bool(cls.CURRENT_CONFIG[CONFIG_WIDTH] or cls.CURRENT_CONFIG[CONFIG_HEIGHT]))

    @classmethod
    def _get_image_api(cls, post: str, session: cloudflare.Session) -> Optional[ImageFile]:
        response_post = session.get(URL_FMT.format(cls.URL), {'id': post, **_PARAMS_API})
        if not response_post:
            return
        try:
            image = response_post.json()[0]
        except (TypeError, json.JSONDecodeError):
            return
        name = image['image']
        rating = image['rating']
        return ImageFile(request.join_url(cls.URL, 'images', str(image['directory']), name),
                         f'{image["id"]} {image["tags"]}{os.path.splitext(name)[1]}',
                         url=request.encode_params(cls.URL, {'id': post, **_PARAMS_POST}),
                         md5=image['hash'], width=image['width'], height=image['height'],
                         sketchy=rating == RATINGS[1], nsfw=rating == RATINGS[2])

    @classmethod
    def _get_image_scrape(cls, post: str, session: cloudflare.Session) -> Optional[ImageFile]:
        url_post = request.encode_params(URL_FMT.format(cls.URL), {'id': post, **_PARAMS_POST})
        response_post = session.get(url_post)
        if not response_post:
            return
        html_post = sgml.loads(response_post.text)
        image = json.loads(_RE_IMAGE.search(html_post.find(
            'div', _ATTRS_CONTAINER).get_next_sibling().get_data(
        )).group(1).translate(_TRANS_QUOTES))
        link = request.join_url(image['domain'], image[
            'base_dir'], str(image['dir']), image['img'])
        hash_, ext = os.path.splitext(image['img'])
        stats = html_post.find('div', _ATTRS_STATS)
        rating = json.loads(_yaml_to_json('\n'.join(text for ele in stats.find_all(
            'li') if (text := ele.get_text()))))['Rating']
        return ImageFile(link, f'{post} {html_post.find("img", _ATTRS_IMAGE)["alt"]}{ext}',
                         url=url_post, md5=hash_, width=image['width'], height=image['height'],
                         sketchy=rating == RATINGS[1], nsfw=rating == RATINGS[2])


from . import (
    furrybooru,
    hypnohub,
    realbooru,
    rule34,
    safebooru,
    thebigimageboard,
    xbooru)  # NOQA: E402
