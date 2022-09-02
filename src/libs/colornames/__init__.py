__version__ = '0.0.2'  # https://github.com/meodai/color-names/

import json
import os
from typing import Optional

_COLORS: Optional[dict[str, str]] = None


def get_name(color: str | tuple[int, int, int]) -> str:
    global _COLORS
    if _COLORS is None:
        with open(os.path.join(os.path.dirname(__file__), 'colornames.min.json'), encoding='utf-8') as file:
            _COLORS = json.load(file)
    if isinstance(color, str):
        color = color.strip().lower()
        color = color[color.startswith('#'):]
    else:
        color = ''.join(f'{hex(color)[2:]:>02}' for color in color)
    try:
        return _COLORS[color]
    except KeyError:
        return f'#{color.upper()}'
