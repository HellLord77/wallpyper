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

FLAG_IMAGE_EX = True

URL_BASE = 'https://www.pixiv.net'
URL_ARTWORK = request.join_url(URL_BASE, 'artworks')
URL_IMAGE = request.join_url('https://i.pximg.net', 'img-original', 'img')

_HEADERS = {request.Header.REFERER: URL_BASE}
_ATTRS_SLIDESHOW = {'id': 'init-config'}
_ATTRS_DATA = {'id': 'meta-preload-data'}


class PixivSlideshow(Source):
    NAME = 'pixiv Slideshow'
    VERSION = '0.0.2'
    URL = URL_BASE
    if FLAG_IMAGE_EX:
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
            # noinspection PyArgumentList
            image = (cls._get_image_ex if FLAG_IMAGE_EX else cls._get_image)(background)
            if image is None:
                backgrounds.insert(0, background)
                yield
                continue
            yield image

    @classmethod
    def _get_image(cls, background: dict[str, str | dict[str, str]]) -> Optional[ImageFile]:
        id_ = background['illust_id']
        parts = request.split_url(background['url']['medium'])
        ext = os.path.splitext(parts[-1])[1]
        return ImageFile(request.Request(request.Method.GET, request.join_url(
            URL_IMAGE, *parts[-7:-1], f'{id_}_p0{ext}'), headers=_HEADERS),
                         background['illust_title'] + ext, url=request.join_url(URL_ARTWORK, id_))

    @classmethod
    def _get_image_ex(cls, background: dict[str, str | dict[str, str]]) -> Optional[ImageFile]:
        id_ = background['illust_id']
        url_artwork = request.join_url(URL_ARTWORK, id_)
        response_artwork = request.get(url_artwork)
        if not response_artwork:
            return
        illust = json.loads(sgml.loads(response_artwork.text).find(
            'meta', _ATTRS_DATA)['content'])['illust'][id_]
        link = illust['urls']['original']
        rating = illust['xRestrict']
        return ImageFile(request.Request(request.Method.GET, link, headers=_HEADERS), illust[
            'illustTitle'] + os.path.splitext(link)[1], url=url_artwork, width=illust['width'],
                         height=illust['height'], sketchy=rating == 1, nsfw=rating == 2)
