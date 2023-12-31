import itertools
import json
import os.path
from typing import Iterator
from typing import Optional
from typing import TypedDict

from libs import request
from libs import sgml
from . import CONFIG_ORIENTATIONS
from . import CONFIG_RATINGS
from . import ImageFile
from . import Source

URL_BASE = 'https://www.pixiv.net'
URL_ARTWORK = request.join_url(URL_BASE, 'artworks')

_HEADERS = {request.Header.REFERER: URL_BASE}
_ATTRS_SLIDESHOW = {'id': 'init-config'}
_ATTRS_DATA = {'id': 'meta-preload-data'}


class PixivSlideshow(Source):
    NAME = 'pixiv Slideshow'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_RATINGS: list[bool]})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_RATINGS: [True, False, False]}

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        backgrounds = []
        while True:
            if not backgrounds:
                response = request.get(cls.URL)
                if response:
                    backgrounds = list(itertools.chain.from_iterable(json.loads(
                        sgml.loads(response.text).find('input', attributes=_ATTRS_SLIDESHOW)[
                            'value'])['pixivBackgroundSlideshow.illusts'].values()))
                if not backgrounds:
                    yield
                    continue
            background = backgrounds.pop(0)
            id_ = background['illust_id']
            url = request.join_url(URL_ARTWORK, id_)
            response = request.get(url)
            if not response:
                backgrounds.insert(0, background)
                yield
                continue
            illust = json.loads(sgml.loads(response.text).find(
                'meta', _ATTRS_DATA)['content'])['illust'][id_]
            url_illust = illust['urls']['original']
            rating = illust['xRestrict']
            yield ImageFile(request.Request(request.Method.GET, url_illust, headers=_HEADERS), illust[
                'illustTitle'] + os.path.splitext(url_illust)[1], url=url, width=illust['width'],
                            height=illust['height'], sketchy=rating == 1, nsfw=rating == 2)
