import uuid
from typing import Iterator, Optional, TypedDict

import gui
import validator
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
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_VARIANT: str})
    DEFAULT_CONFIG = {
        CONFIG_VARIANT: VARIANTS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_iterable, CONFIG_VARIANT, VARIANTS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls.STRINGS.DOESNOTEXIST_MENU_VARIANT, {variant: getattr(
            cls.STRINGS, f'DOESNOTEXIST_VARIANT_{variant}') for variant in VARIANTS}, cls.CURRENT_CONFIG, CONFIG_VARIANT)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[files.File]]:
        url = URL_BASE_TEMPLATE.format(cls.CURRENT_CONFIG[CONFIG_VARIANT])
        if cls.CURRENT_CONFIG[CONFIG_VARIANT] == VARIANTS[0]:
            url = request.join(url, 'image')
        while True:
            yield files.File(url, f'{uuid.uuid4()}.jpg')
