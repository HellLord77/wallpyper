from typing import Iterator, Optional, TypedDict

import gui
import validator
from libs import request
from . import CONFIG_ORIENTATIONS, CONFIG_RATINGS, ImageFile, Source

URL_BASE = 'https://yande.re'
URL_POSTS = request.join_url(URL_BASE, 'post.json')
URL_INFO = request.join_url(URL_BASE, 'post', 'show')

CONFIG_RATINGS = CONFIG_RATINGS[:-1]
CONFIG_TAGS = 'tags'

_CONTENT_END = b'[]'


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
        gui.add_submenu_check(cls._text('MENU_ORIENTATIONS'), (cls._text(
            f'ORIENTATION_{orientation}') for orientation in range(2)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_ORIENTATIONS)
        gui.add_submenu_check(cls._text('MENU_RATINGS'), (cls._text(
            f'RATING_{rating}') for rating in range(3)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_RATINGS)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        posts: Optional[list] = None
        page = 1
        while True:
            if not posts:
                params['page'] = str(page)
                response = request.get(URL_POSTS, params)
                if (response.status_code == request.Status.NOT_MODIFIED
                        and response.content == _CONTENT_END):
                    page = 1
                    continue
                if response:
                    posts = response.json()
                    page += 1
                if not posts:
                    yield
                    continue
            post = posts.pop(0)
            yield ImageFile(post['file_url'], size=post['file_size'], url=request.join_url(
                URL_INFO, str(post['id'])), width=post['width'],
                            height=post['height'], sketchy=post['rating'] == 'q',
                            nsfw=post['rating'] == 'e', md5=post['md5'])

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if not cls._filter_ratings(image, CONFIG_RATINGS, sketchy=True):
            return False
        return super().filter_image(image)
