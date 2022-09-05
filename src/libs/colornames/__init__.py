from __future__ import annotations as _

__version__ = '0.0.4'  # https://github.com/meodai/color-names/

import functools
import json
import math
import os
from typing import Optional

_COLORS: Optional[dict[str, str]] = None
_RGB_TO_HEX_COLORS: Optional[dict[tuple[int, int, int], str]] = None


def xyz_to_srgb(x: float, y: float, z: float) -> tuple[float, float, float]:
    r = x * 3.2406 + y * -1.5372 + z * -0.4986
    g = x * -0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 + y * -0.2040 + z * 1.0570
    # noinspection PyTypeChecker
    return tuple((1.055 * c ** (1 / 2.4) - 0.055 if c > 0.0031308 else 12.92 * c) for c in (r, g, b))


def srgb_to_xyz(r: float, g: float, b: float) -> tuple[float, float, float]:
    r, g, b = ((((c + 0.055) / 1.055) ** 2.4 if c > 0.04045 else c / 12.92) for c in (r, g, b))
    return r * 0.4124 + g * 0.3576 + b * 0.1805, r * 0.216 + g * 0.7152 + b * 0.0722, r * 0.0193 + g * 0.1192 + b * 0.9505


def xyz_to_argb(x: float, y: float, z: float) -> tuple[float, float, float]:
    c = 1 / 2.19921875
    return (x * 2.04137 + y * -0.56495 + z * -0.34469) ** c, (x * -0.96927 + y * 1.87601 + z * 0.04156) ** c, (x * 0.01345 + y * -0.11839 + z * 1.01541) ** c


def argb_to_xyz(r: float, g: float, b: float) -> tuple[float, float, float]:
    r **= 2.19921875
    g **= 2.19921875
    b **= 2.19921875
    return r * 0.57667 + g * 0.18555 + b * 0.18819, r * 0.29738 + g * 0.62735 + b * 0.07527, r * 0.02703 + g * 0.07069 + b * 0.99110


def xyz_to_yxy(x: float, y: float, z: float) -> tuple[float, float, float]:
    c = x + y + z
    return y, x / c, z / c


def yxy_to_xyz(y: float, x: float, y_: float) -> tuple[float, float, float]:
    c = y / y_
    return x * c, y, (1 - x - y) * c


def srgb_to_cmy(r: float, g: float, b: float) -> tuple[float, float, float]:
    return 1 - r, 1 - g, 1 - b


def cmy_to_srgb(c: float, m: float, y: float) -> tuple[float, float, float]:
    return 1 - c, 1 - m, 1 - y


def cmy_to_cmyk(c: float, m: float, y: float) -> tuple[float, float, float, float]:
    k = min((c, m, y, 1.0))
    c_ = 1 - k
    return (0.0, 0.0, 0.0, k) if k == 1 else ((c - k) / c_, (m - k) / c_, (y - k) / c_, k)


def cmyk_to_cmy(c: float, m: float, y: float, k: float) -> tuple[float, float, float]:
    c_ = 1 - k
    return c * c_ + k, m * c_ + k, y * c_ + k


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f'#{r:02x}{g:02x}{b:02x}'


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip('#')
    return int(h[:2], 16), int(h[2:4], 16), int(h[4:], 16)


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
        return color.upper(), name
    global _RGB_TO_HEX_COLORS
    if _RGB_TO_HEX_COLORS is None:
        _RGB_TO_HEX_COLORS = {hex_to_rgb(hex_color) for hex_color in _COLORS}
    rgb_color = hex_to_rgb(color)
    min_distance = math.inf
    nearest_color = 0, 0, 0
    for cur_color in _RGB_TO_HEX_COLORS:
        distance = sum((rgb_color[i] - cur_color[i]) ** 2 for i in range(3))
        if min_distance > distance:
            min_distance = distance
            nearest_color = cur_color
    nearest_color = rgb_to_hex(*nearest_color)
    return nearest_color.upper(), _COLORS[nearest_color[1:]]
