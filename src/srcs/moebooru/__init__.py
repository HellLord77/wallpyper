import datetime
import functools
import itertools
import os
import re
import urllib.parse
from typing import Callable, Iterator, Optional, TypedDict

import gui
import validator
from libs import request
from .. import CONFIG_ORIENTATIONS, ImageFile, Source

URL_FMT_TAG = request.join_url('{}', 'post.json')
URL_FMT_INFO = request.join_url('{}', 'post', 'show')
URL_FMT_POOL = request.join_url('{}', 'pool', 'show', '{}.json')
URL_FMT_POPULAR = request.join_url('{}', 'post', 'popular_{}.json')

CONFIG_MODE = 'mode'
CONFIG_TAGS = 'tags'
CONFIG_RATING = 'rating'
CONFIG_ORDER = 'order'
CONFIG_SIZE = 'size'
CONFIG_WIDTH = 'width'
CONFIG_HEIGHT = 'height'
CONFIG_POOL = 'pool'
CONFIG_POPULARITY = 'popularity'
CONFIG_PERIOD = 'period'
CONFIG_DAY = 'day'
CONFIG_MONTH = 'month'
CONFIG_YEAR = 'year'

MODES = 'tag', 'pool', 'popular'
RATINGS = 's', 'q', 'e'
ORDERS = (
    'id', 'id_desc', 'score', 'score_asc', 'mpixels',
    'mpixels_asc', 'landscape', 'portrait', 'random')
SIZES = 'bigger', 'exact', 'smaller'
WIDTHS = 2560, 1920, 1680, 1600, 1440, 1400, 1280, 1152, 1024, 0
HEIGHTS = 1600, 1200, 1080, 1050, 1024, 960, 900, 864, 800, 768, 0
POPULARITIES = 'recent', 'by_day', 'by_week', 'by_month'
PERIODS = '1d', '1w', '1m', '1y'

_CONTENT_END = b'[]'
_RE_PREFIX = re.compile(r'^\D*')


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


def _tag_order(order: str) -> Iterator[str]:
    if order != ORDERS[1]:
        yield 'order:' + order


def _tag_dimension(width: int, height: int, size: str) -> Iterator[str]:
    fmt = '{}'
    if size == SIZES[0]:
        fmt = '{}..'
    elif size == SIZES[2]:
        fmt = '..{}'
    if width:
        yield 'width:' + fmt.format(width)
    if height:
        yield 'height:' + fmt.format(height)


def _param_time(day: int, month: int, year: int) -> Iterator[tuple[str, str]]:
    if day or month or year:
        today = datetime.date.today()
        if not day:
            day = today.day
        yield CONFIG_DAY, str(day)
        if not month:
            month = today.month
        yield CONFIG_MONTH, str(month)
        if not year:
            year = today.year
        yield CONFIG_YEAR, str(year)


class MoebooruSource(Source, source=False):
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_MODE: str,
        CONFIG_TAGS: list[str],
        CONFIG_RATING: list[bool],
        CONFIG_ORDER: str,
        CONFIG_WIDTH: int,
        CONFIG_HEIGHT: int,
        CONFIG_SIZE: str,
        CONFIG_POOL: int,
        CONFIG_POPULARITY: str,
        CONFIG_PERIOD: str,
        CONFIG_DAY: int,
        CONFIG_MONTH: int,
        CONFIG_YEAR: int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_MODE: MODES[0],
        CONFIG_TAGS: [],
        CONFIG_RATING: [True, True, True],
        CONFIG_ORDER: ORDERS[1],
        CONFIG_WIDTH: WIDTHS[9],
        CONFIG_HEIGHT: HEIGHTS[10],
        CONFIG_SIZE: SIZES[0],
        CONFIG_POOL: 0,
        CONFIG_POPULARITY: POPULARITIES[0],
        CONFIG_PERIOD: PERIODS[0],
        CONFIG_DAY: 0,
        CONFIG_MONTH: 0,
        CONFIG_YEAR: 0}

    def __init_subclass__(cls, *args, **kwargs):
        cls._text = MoebooruSource._text
        super().__init_subclass__(*args, **kwargs)

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_MODE, MODES)
        cls._fix_config(validator.ensure_len, CONFIG_RATING, 3)
        cls._fix_config(validator.ensure_truthy, CONFIG_RATING, any)
        cls._fix_config(validator.ensure_contains, CONFIG_ORDER, ORDERS)
        cls._fix_config(validator.ensure_contains, CONFIG_WIDTH, WIDTHS)
        cls._fix_config(validator.ensure_contains, CONFIG_HEIGHT, HEIGHTS)
        cls._fix_config(validator.ensure_contains, CONFIG_SIZE, SIZES)
        cls._fix_config(validator.ensure_contains, CONFIG_POPULARITY, POPULARITIES)
        cls._fix_config(validator.ensure_contains, CONFIG_PERIOD, PERIODS)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        gui.add_separator()
        item_post = gui.add_submenu(cls._text('MENU_TAG'))
        with gui.set_menu(item_post):
            gui.add_submenu_check(cls._text('MENU_RATING'), (cls._text(
                f'RATING_{rating}') for rating in range(3)),
                                  (1, None), cls.CURRENT_CONFIG, CONFIG_RATING)
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
        item_popular = gui.add_submenu(cls._text('MENU_POPULAR'))
        with gui.set_menu(item_popular):
            gui.add_submenu_radio(cls._text('MENU_POPULARITY'), {
                popular: cls._text(f'POPULARITY_{popular}') for popular in
                POPULARITIES}, cls.CURRENT_CONFIG, CONFIG_POPULARITY)
            gui.add_submenu_radio(cls._text('MENU_PERIOD'), {
                period: cls._text(f'PERIOD_{period}') for period in
                PERIODS}, cls.CURRENT_CONFIG, CONFIG_PERIOD)
        on_mode = functools.partial(cls._on_mode, item_post.enable, item_popular.enable)
        gui.add_submenu_radio(cls._text('MENU_MODE'), {mode: cls._text(
            'MODE_' + mode) for mode in MODES}, cls.CURRENT_CONFIG,
                              CONFIG_MODE, on_click=on_mode, position=0)
        on_mode(cls.CURRENT_CONFIG[CONFIG_MODE])
        gui.add_separator()
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        posts = []
        mode = params[CONFIG_MODE]
        if mode == MODES[0]:
            url = URL_FMT_TAG.format(cls.URL)
            tags = set(params[CONFIG_TAGS])
            tags.update(_tag_rating(params[CONFIG_RATING]))
            tags.update(_tag_order(params[CONFIG_ORDER]))
            tags.update(_tag_dimension(params[CONFIG_WIDTH],
                                       params[CONFIG_HEIGHT], params[CONFIG_SIZE]))
            params = {CONFIG_TAGS: ' '.join(tags)}
        elif mode == MODES[1]:
            url = URL_FMT_POOL.format(cls.URL, params[CONFIG_POOL])
            params.clear()
        else:
            url = URL_FMT_POPULAR.format(cls.URL, params[CONFIG_POPULARITY])
            params = {CONFIG_PERIOD: params[CONFIG_PERIOD]} | dict(_param_time(
                params[CONFIG_DAY], params[CONFIG_MONTH], params[CONFIG_YEAR]))
        page = 1
        while True:
            if not posts:
                params['page'] = str(page)
                response = request.get(url, params)
                if (page != 1 and response.status_code == request.Status.NOT_MODIFIED
                        and response.content == _CONTENT_END):
                    page = 1
                    continue
                if response:
                    posts = response.json()
                    if mode == MODES[1]:
                        posts = posts['posts']
                    page += 1
                if not posts:
                    yield
                    continue
            post = posts.pop(0)
            link = post['file_url']
            rating = post['rating']
            yield ImageFile(link, _RE_PREFIX.sub('', urllib.parse.unquote_plus(
                os.path.basename(request.strip_url(link)))), post['file_size'],
                            request.join_url(URL_FMT_INFO.format(cls.URL), str(post['id'])),
                            width=post['width'], height=post['height'],
                            sketchy=rating == 'q', nsfw=rating == 'e', md5=post['md5'])

    @classmethod
    def _on_mode(cls, enable_post: Callable[[bool], bool],
                 enable_popular: Callable[[bool], bool], mode: str):
        enable_post(mode == MODES[0])
        enable_popular(mode == MODES[2])

    @classmethod
    def _on_dimension(cls, enable: Callable[[bool], bool], _: Optional[int] = None):
        enable(bool(cls.CURRENT_CONFIG[CONFIG_WIDTH] or cls.CURRENT_CONFIG[CONFIG_HEIGHT]))


from . import (
    konachan,
    yandere,
    myimouto)  # NOQA: E402
