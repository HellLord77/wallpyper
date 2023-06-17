import uuid
from typing import Iterator, Optional, TypedDict

import gui
import validator
from . import File, Source

CONFIG_VARIANT = 'variant'

VARIANTS = 'person',

_TEMPLATE_URL = 'https://this{}doesnotexist.com'


class ThisXDoesNotExist(Source):
    NAME = 'This X Does Not Exist'
    VERSION = '0.0.3'
    ICON = 'jpg'
    URL = 'https://thisxdoesnotexist.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_VARIANT: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_VARIANT: VARIANTS[0]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_contains, CONFIG_VARIANT, VARIANTS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_VARIANT'), {variant: cls._text(
            f'VARIANT_{variant}') for variant in VARIANTS}, cls.CURRENT_CONFIG, CONFIG_VARIANT)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        url = _TEMPLATE_URL.format(cls.CURRENT_CONFIG[CONFIG_VARIANT])
        while True:
            yield File(url, f'{uuid.uuid4()}.jpg')
