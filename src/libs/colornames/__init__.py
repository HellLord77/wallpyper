from __future__ import annotations as _

__version__ = '0.0.3'  # https://github.com/meodai/color-names/

import functools
import json
import math
import os
from typing import Optional

_COLORS: Optional[dict[str, str]] = None
_RGB_TO_HEX_COLORS: Optional[dict[tuple[int, int, int], str]] = None


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f'#{r:02x}{g:02x}{b:02x}'


def hex_to_rgb(h: str) -> tuple:
    h = h.lstrip('#')
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def get(color: str) -> str:
    global _COLORS
    if _COLORS is None:
        with open(os.path.join(os.path.dirname(__file__), 'colornames.min.json'), encoding='utf-8') as file:
            _COLORS = json.load(file)
    color = color.strip().lstrip('#').lower()
    try:
        return _COLORS[color]
    except KeyError:
        return f'#{color.upper()}'


@functools.lru_cache
def get_nearest(color: str) -> tuple[str, str]:
    if not (name := get(color)).startswith('#'):
        return color, name
    global _RGB_TO_HEX_COLORS
    if _RGB_TO_HEX_COLORS is None:
        _RGB_TO_HEX_COLORS = {hex_to_rgb(hex_color) for hex_color in _COLORS}
    color = hex_to_rgb(color)
    min_distance = math.inf
    nearest_color = 0, 0, 0
    for rgb_color in _RGB_TO_HEX_COLORS:
        distance = sum((color[i] - rgb_color[i]) ** 2 for i in range(3))
        if min_distance > distance:
            min_distance = distance
            nearest_color = rgb_color
    nearest_color = rgb_to_hex(*nearest_color)
    return nearest_color.upper(), _COLORS[nearest_color[1:]]
