from typing import Iterator, Optional

from libs import request
from . import GelbooruV02Source
from ... import ImageFile

URL_CDN = 'https://api-cdn.rule34.xxx'


class Rul34(GelbooruV02Source):  # https://rule34.xxx/index.php?page=help&topic=dapi
    NAME = 'Rule34.xxx'
    VERSION = '0.0.2'
    URL = 'https://rule34.xxx'
    URL_API = 'https://api.rule34.xxx'

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        for image in super().get_image(**params):
            image.request.url = request.join_url(
                URL_CDN, *request.split_url(image.request.url)[1:])
            del image.hashes['md5']
            yield image
