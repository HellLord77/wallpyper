import itertools
import os
import random
from typing import Iterator
from typing import Optional
from typing import TypedDict

import gui
import validator
import win32
from libs import colornames
from libs import request
from . import ImageFile
from . import Source

CONFIG_LUMINANCES = '_luminances'
CONFIG_WIDTH = 'width'
CONFIG_HEIGHT = 'height'

LUMINANCES = 'light', 'dark'
WIDTHS = 640, 800, 1024, 1280, 1360, 1366, 1440, 1536, 1600, 1680, 1920, 2048, 2560, 3440, 3840
HEIGHTS = 360, 480, 600, 720, 768, 800, 864, 900, 1024, 1050, 1080, 1152, 1200, 1440, 1536, 1600, 2160


class Color(Source):
    NAME = 'Color [offline]'
    VERSION = '0.0.2'
    ICON = 'png'
    TCONFIG = TypedDict('TCONFIG', {
        CONFIG_LUMINANCES: list[bool, bool],
        CONFIG_WIDTH:      int,
        CONFIG_HEIGHT:     int})
    DEFAULT_CONFIG: TCONFIG = {
        CONFIG_LUMINANCES: [True, True],
        CONFIG_WIDTH:      WIDTHS[10],
        CONFIG_HEIGHT:     HEIGHTS[10]}

    @classmethod
    def fix_config(cls, saving: bool = False):
        cls._fix_config(validator.ensure_len, CONFIG_LUMINANCES, 2)
        cls._fix_config(validator.ensure_truthy, CONFIG_LUMINANCES)
        cls._fix_config(validator.ensure_contains, CONFIG_WIDTH, WIDTHS)
        cls._fix_config(validator.ensure_contains, CONFIG_HEIGHT, HEIGHTS)

    @classmethod
    def create_menu(cls):
        gui.add_submenu_radio(cls._text('MENU_WIDTH'), {width: cls._text(
            width) for width in WIDTHS}, cls.CURRENT_CONFIG, CONFIG_WIDTH)
        gui.add_submenu_radio(cls._text('MENU_HEIGHT'), {height: cls._text(
            height) for height in HEIGHTS}, cls.CURRENT_CONFIG, CONFIG_HEIGHT)
        gui.add_separator()
        gui.add_submenu_check(cls._text('MENU_LUMINANCES'), (cls._text(
            f'LUMINANCE_{luminance}') for luminance in range(2)),
                              (1, None), cls.CURRENT_CONFIG, CONFIG_LUMINANCES)

    @classmethod
    def get_image(cls, **params) -> Iterator[Optional[ImageFile]]:
        width = params.pop(CONFIG_WIDTH)
        height = params.pop(CONFIG_HEIGHT)
        while True:
            file = None
            rgb = random.randrange(256), random.randrange(256), random.randrange(256)
            if bitmap := win32.get_colored_bitmap(*rgb, width, height):
                path = cls._temp(colornames.get_nearest_color_lab(
                    colornames.rgb_to_hex(*rgb))[1] + '.png')
                os.makedirs(os.path.dirname(path), exist_ok=True)
                if win32.save_image(bitmap, path):
                    file = ImageFile(request.from_path(path), width=width, height=height)
                    file._rgb = rgb
            yield file

    @classmethod
    def _filter_luminances(cls, rgb: tuple[int, int, int]) -> bool:
        srgb = [0, 0, 0]
        for i in range(3):
            c = rgb[i] / 255
            srgb[i] = (c / 12.92) if c <= 0.04045 else (((c + 0.055) / 1.055) ** 2.4)
        light = (0.2126 * srgb[0] + 0.7152 * srgb[1] + 0.0722 * srgb[2]) > 0.179
        return any(itertools.compress((
            light, not light), cls.CURRENT_CONFIG[CONFIG_LUMINANCES]))

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if ((rgb := getattr(image, '_rgb', None)) is not None and
                not cls._filter_luminances(rgb)):
            return False
        return True
