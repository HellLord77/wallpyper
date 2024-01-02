import urllib.parse
from typing import Iterator
from typing import Optional

from . import GelbooruV02Source
from ... import ImageFile


class TheBigImageBoard(GelbooruV02Source):  # https://tbib.org/index.php?page=help&topic=dapi
    NAME = 'The Big ImageBoard (TBIB)'
    VERSION = '0.0.3'
    URL = 'https://tbib.org'

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        scheme = urllib.parse.urlsplit(cls.URL).scheme + ':'
        for image in super().get_image(**params):
            if image is not None and not urllib.parse.urlsplit(image.request.url).scheme:
                image.request.url = urllib.parse.urljoin(scheme, image.request.url)
            yield image
