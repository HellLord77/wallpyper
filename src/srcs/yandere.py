import os
import urllib.parse
from typing import Iterator, Optional, TypedDict

from libs import request
from . import CONFIG_ORIENTATIONS, CONFIG_RATINGS, ImageFile, Source

URL_BASE = 'https://yande.re'
URL_POSTS = request.join_url(URL_BASE, 'post.json')
URL_INFO = request.join_url(URL_BASE, 'post', 'show')

CONFIG_RATINGS = CONFIG_RATINGS[:-1]
CONFIG_TAGS = 'tags'

_CONTENT_END = b'[]'


class YandeRe(Source):  # https://yande.re/help/api
    NAME = 'yande.re'
    VERSION = '0.0.3'
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
        cls._fix_ratings(CONFIG_RATINGS)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        super().create_menu()
        cls._create_ratings(CONFIG_RATINGS)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        posts = []
        page = 1
        while True:
            if not posts:
                params['page'] = str(page)
                response = request.get(URL_POSTS, params)
                if (page != 1 and response.status_code == request.Status.NOT_MODIFIED
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
            link = post['file_url']
            yield ImageFile(link, urllib.parse.unquote_plus(os.path.basename(
                request.strip_url(link))).removeprefix('yande.re '), post['file_size'],
                            request.join_url(URL_INFO, str(post['id'])), width=post['width'],
                            height=post['height'], sketchy=post['rating'] == 'q',
                            nsfw=post['rating'] == 'e', md5=post['md5'])

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if not cls._filter_ratings(image, CONFIG_RATINGS, sketchy=True):
            return False
        return super().filter_image(image)
