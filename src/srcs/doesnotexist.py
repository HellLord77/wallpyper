import uuid
from typing import Iterator, Optional

import gui
from libs import files, request
from . import Source

CONFIG_VARIANT = 'variant'

URL_BASE_TEMPLATE = 'https://this{}doesnotexist.com'

VARIANTS = 'person', 'artwork', 'cat', 'horse'


class ThisDoesNotExist(Source):
    NAME = 'This Does Not Exist'
    VERSION = '0.0.1'
    ICON = 'jpg'
    URL = URL_BASE_TEMPLATE.format(VARIANTS[0])
    DEFAULT_CONFIG = {
        CONFIG_VARIANT: VARIANTS[0]}

    @classmethod
    def fix_config(cls):
        cls._fix_config(CONFIG_VARIANT, VARIANTS)

    @classmethod
    def get_next_image(cls, **params) -> Iterator[Optional[files.File]]:
        url = URL_BASE_TEMPLATE.format(cls.CURRENT_CONFIG[CONFIG_VARIANT])
        if cls.CURRENT_CONFIG[CONFIG_VARIANT] == VARIANTS[0]:
            url = request.join(url, 'image')
        while True:
            yield files.File(url, f'{uuid.uuid4()}.jpg')

    @classmethod
    def create_menu(cls):
        gui.add_mapped_submenu(cls.strings.DOESNOTEXIST_MENU_VARIANT, {variant: getattr(
            cls.strings, f'DOESNOTEXIST_VARIANT_{variant}') for variant in VARIANTS}, cls.CURRENT_CONFIG, CONFIG_VARIANT)
