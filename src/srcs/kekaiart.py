import random
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from libs import request
from libs import sgml
from . import CONFIG_ORIENTATIONS
from . import ImageFile
from . import Source

# noinspection HttpUrlsUsage
URL_BASE = 'http://www.kekaiart.com'

CONFIG_RANDOM = '_random'
CONFIG_GALLERY = 'gallery'

GALLERIES = 'freelance', 'personal', 'guild-wars-2', 'guild-wars'


class KekaiKotaki(Source):
    NAME = 'KEKAI KOTAKI'
    VERSION = '0.0.1'
    URL = URL_BASE
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[int],
        CONFIG_RANDOM:       bool,
        CONFIG_GALLERY:      str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_ORIENTATIONS: [True, True],
        CONFIG_RANDOM:       False,
        CONFIG_GALLERY:      GALLERIES[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_GALLERY, GALLERIES)
        super().fix_config(saving)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_GALLERY'), {
            gallery: cls._text(f'GALLERY_{gallery}') for gallery in GALLERIES},
                              cls.CURRENT_CONFIG, CONFIG_GALLERY)
        gui.add_separator()
        gui.add_menu_item_check(cls._text('LABEL_RANDOM'), cls.CURRENT_CONFIG, CONFIG_RANDOM)
        super().create_menu()

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        uploads = []
        url = request.join_url(URL_BASE, params.pop(CONFIG_GALLERY) + '.html')
        while True:
            if not uploads:
                response = request.get(url)
                if response:
                    uploads = list(sgml.loads(response.text).find_all(
                        'div', classes='galleryInnerImageHolder'))
                if not uploads:
                    yield
                    continue
            upload = uploads.pop(random.randrange(len(
                uploads)) if cls.CURRENT_CONFIG[CONFIG_RANDOM] else 0)[0]
            image = upload[0]
            yield ImageFile(request.join_url(URL_BASE, upload['href']), request.split_url(
                image['src'])[-1], width=int(image['_width']), height=int(image['_height']))
