from typing import Iterator, Optional

from libs import request
from . import GelbooruV02Source
from ... import ImageFile

URL_BASE = 'https://api-cdn.rule34.xxx'


class Rul34(GelbooruV02Source):
    NAME = 'Rule34.xxx'
    VERSION = '0.0.1'
    URL = 'https://rule34.xxx'

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        for image in super().get_image(**params):
            image.request.url = request.join_url(
                URL_BASE, *request.split_url(image.request.url)[1:])
            yield image
