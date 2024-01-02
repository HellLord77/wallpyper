import functools
from typing import Callable
from typing import Iterator
from typing import Optional

from libs import request
from libs.request import cloudflare
from . import GelbooruV02Source
from . import URL_FMT
from ... import ImageFile

URL_API = 'https://api.rule34.xxx'
URL_CDN = 'https://api-cdn.rule34.xxx'


def _session_get(session_get: Callable, url: str, params: dict[str, str]) -> request.Response:
    return session_get(URL_FMT.format(url), params)


class Rul34(GelbooruV02Source):  # https://rule34.xxx/index.php?page=help&topic=dapi
    NAME = '# Rule34.xxx [cloudflare]'
    VERSION = '0.0.3'
    URL = 'https://rule34.xxx'

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        for image in super().get_image(**params):
            if image is not None:
                image.request.url = request.join_url(URL_CDN, *request.split_url(image.request.url)[1:])
                del image.hashes['md5']
            yield image

    @classmethod
    def _get_image_api(cls, post: str, session: cloudflare.Session) -> Optional[ImageFile]:
        session.get = functools.partial(_session_get, session.get)
        return super()._get_image_api(post, session)
