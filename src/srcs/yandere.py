import functools
import http
import itertools
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import files, request
from . import Source

_CONTENT_END = b'[]'

URL_BASE = 'https://yande.re'
URL_POSTS = request.join(URL_BASE, 'post.json')

CONFIG_SAFE = '_safe'
CONFIG_QUESTIONABLE = '_questionable'
CONFIG_EXPLICIT = '_explicit'
CONFIG_ORIENTATION = '_orientation'
CONFIG_TAGS = 'tags'

ORIENTATIONS = 'any', 'landscape', 'portrait'

_CONFIG_RATINGS = CONFIG_SAFE, CONFIG_QUESTIONABLE, CONFIG_EXPLICIT


class YandeRe(Source):
    NAME = 'yande.re'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_SAFE: bool,
        CONFIG_QUESTIONABLE: bool,
        CONFIG_EXPLICIT: bool,
        CONFIG_ORIENTATION: str,
        CONFIG_TAGS: str})
    DEFAULT_CONFIG = {
        CONFIG_SAFE: True,
        CONFIG_QUESTIONABLE: True,
        CONFIG_EXPLICIT: True,
        CONFIG_ORIENTATION: ORIENTATIONS[0],
        CONFIG_TAGS: ''}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_ORIENTATION, ORIENTATIONS)
        if not any(cls.CURRENT_CONFIG[rating] for rating in _CONFIG_RATINGS):
            for rating in _CONFIG_RATINGS:
                cls.CURRENT_CONFIG[rating] = cls.DEFAULT_CONFIG[rating]

    @classmethod
    def create_menu(cls):
        with gui.set_menu(gui.add_submenu(cls.STRINGS.YANDERE_MENU_RATING)) as menu_rating:
            on_rating = functools.partial(cls._on_rating, menu_rating)
            for rating in _CONFIG_RATINGS:
                gui.add_menu_item(getattr(
                    cls.STRINGS, f'YANDERE_RATING_{rating}'), gui.MenuItemType.CHECK,
                    cls.CURRENT_CONFIG[rating], uid=rating, on_click=on_rating)
        on_rating()
        gui.add_mapped_submenu(cls.STRINGS.YANDERE_MENU_ORIENTATION, {
            orientation: getattr(cls.STRINGS, f'YANDERE_ORIENTATION_{orientation}')
            for orientation in ORIENTATIONS}, cls.CURRENT_CONFIG, CONFIG_ORIENTATION)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        posts: Optional[list] = None
        params['page'] = '1'
        params['limit'] = '100'
        while True:
            if not posts:
                response = request.get(URL_POSTS, params=params)
                if (response.status_code == http.HTTPStatus.NOT_MODIFIED
                        and response.content == _CONTENT_END):
                    params['page'] = '1'
                    continue
                if response:
                    posts = response.json()
                    params['page'] = str(int(params['page']) + 1)
            if not posts:
                yield
                continue
            post = posts.pop(0)
            yield files.ImageFile(post['file_url'], size=post['file_size'], width=post[
                'width'], height=post['height'], sketchy=post['rating'] == 'q',
                                  nsfw=post['rating'] == 'e', md5=post['md5'])

    @classmethod
    def filter_image(cls, image: files.ImageFile) -> bool:
        if not any(itertools.starmap(bool.__and__, zip((
                cls.CURRENT_CONFIG[rating] for rating in _CONFIG_RATINGS), (
                image.is_sfw(), image.sketchy, image.nsfw)))):
            return False
        if cls.CURRENT_CONFIG[CONFIG_ORIENTATION] not in (
                ORIENTATIONS[0], ORIENTATIONS[image.is_portrait() + 1]):
            return False
        return True

    @classmethod
    def _on_rating(cls, menu: gui.Menu):
        checked_items = []
        for rating, item in gui.get_menu_items(menu).items():
            item.enable()
            checked = cls.CURRENT_CONFIG[rating] = item.is_checked()
            if checked:
                checked_items.append(item)
        if len(checked_items) == 1:
            checked_items[0].enable(False)
