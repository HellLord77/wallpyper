__version__ = '0.0.2'

import json
import os
from typing import Union

COLORS: dict[str, str] = {}


def get_name(color: Union[str, tuple[int, int, int]]) -> str:
    if not COLORS:
        with open(os.path.join(os.path.dirname(__file__), 'res', 'colornames.min.json'), encoding='utf-8') as file:
            COLORS.update(json.load(file))
    if isinstance(color, str):
        color = color.strip().lower()
        color = color[color.startswith('#'):]
    else:
        color = ''.join(f'{hex(color)[2:]:>02}' for color in color)
    try:
        return COLORS[color]
    except KeyError:
        return f'#{color.upper()}'
