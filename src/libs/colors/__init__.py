__version__ = '0.0.1'

import json
import os
from typing import Union

COLORS: dict[str, str] = {}


def get_name(hex_color: Union[str, tuple[int, int, int]]) -> str:
    if isinstance(hex_color, str):
        hex_color = hex_color.strip().lower()
        hex_color = hex_color[hex_color.startswith('#'):]
    else:
        hex_color = ''.join(f'{hex(color)[2:]:>02}' for color in hex_color)
    try:
        return COLORS[hex_color]
    except KeyError:
        return f'#{hex_color.upper()}'


def _init():
    with open(os.path.join(os.path.dirname(__file__), 'colornames.min.json'), 'r', encoding='utf-8') as file:
        COLORS.update(json.load(file))


_init()
