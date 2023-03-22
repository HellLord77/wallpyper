import http
from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import files, request, utils
from . import Source

_CONTENT_END = b'[]'

URL_BASE = 'https://yande.re'
URL_POSTS = request.join(URL_BASE, 'post.json')

CONFIG_ORIENTATIONS = '_orientations'
CONFIG_RATINGS = '_ratings'
CONFIG_TAGS = 'tags'


class YandeRe(Source):
    NAME = 'yande.re'
    VERSION = '0.0.2'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_RATINGS: list[bool],
        CONFIG_TAGS: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_RATINGS: [True, True, True],
        CONFIG_TAGS: ''}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_ORIENTATIONS, 2)
        cls._fix_config(validator.ensure_truthy, CONFIG_ORIENTATIONS, any)
        cls._fix_config(validator.ensure_len, CONFIG_RATINGS, 3)
        cls._fix_config(validator.ensure_truthy, CONFIG_RATINGS, any)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_check(cls.STRINGS.YANDERE_MENU_ORIENTATIONS, (getattr(
            cls.STRINGS, f'YANDERE_ORIENTATION_{orientation}') for orientation in range(2)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_ORIENTATIONS)
        gui.add_submenu_check(cls.STRINGS.YANDERE_MENU_RATINGS, (getattr(
            cls.STRINGS, f'YANDERE_RATING_{rating}') for rating in range(3)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_RATINGS)

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
        if not any(utils.iter_and(cls.CURRENT_CONFIG[CONFIG_ORIENTATIONS], (
                image.is_landscape(), image.is_portrait()))):
            return False
        if not any(utils.iter_and(cls.CURRENT_CONFIG[CONFIG_RATINGS], (
                image.is_sfw(), image.sketchy, image.nsfw))):
            return False
        return True
