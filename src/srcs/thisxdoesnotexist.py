import uuid
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
from . import File
from . import Source

CONFIG_VARIANT = 'variant'

VARIANTS = 'person',

URL_FMT = 'https://this{}doesnotexist.com'


class ThisXDoesNotExist(Source):
    NAME = 'This X Does Not Exist'
    VERSION = '0.0.3'
    ICON = 'png'
    URL = 'https://thisxdoesnotexist.com'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_VARIANT: str})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_VARIANT: VARIANTS[0]}

    @classmethod
    def load_config(cls):
        cls._fix_config(validator.ensure_contains, CONFIG_VARIANT, VARIANTS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_VARIANT'), {variant: cls._text(
            f'VARIANT_{variant}') for variant in VARIANTS}, cls.CURRENT_CONFIG, CONFIG_VARIANT)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        url = URL_FMT.format(cls.CURRENT_CONFIG[CONFIG_VARIANT])
        while True:
            yield File(url, f'{uuid.uuid4()}.jpg')
