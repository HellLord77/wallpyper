__version__ = '0.0.7'  # https://github.com/meodai/color-names

import functools
import importlib.resources
import json
import math
from typing import Literal

_PATH = 'colornames.min.json'


def xyz_to_srgb(x: float, y: float, z: float) -> tuple[float, float, float]:
    r = x * 3.2406 + y * -1.5372 + z * -0.4986
    g = x * -0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 + y * -0.2040 + z * 1.0570
    c = (1 / 2.4)
    # noinspection PyTypeChecker
    return tuple((1.055 * c_ ** c - 0.055 if c_ > 0.0031308 else 12.92 * c_) for c_ in (r, g, b))


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


def xyz_to_lab(x: float, y: float, z: float) -> tuple[float, float, float]:
    c = 1 / 3
    c_ = 16 / 116
    x, y, z = (c__ ** c if c__ > 0.008856 else 7.787 * c__ + c_ for c__ in (x, y, z))
    return 116 * y - 16, 500 * (x - y), 200 * (y - z)


def lab_to_xyz(l: float, a: float, b: float) -> tuple[float, float, float]:  # NOQA: E741
    y = (l + 16) / 116
    c = 16 / 116
    # noinspection PyTypeChecker
    return tuple(c_ ** 3 if c_ > 0.008856 else (c_ - c) / 7.787 for c_ in (a / 500 + y, y, y - b / 200))


def lab_to_lch(l: float, a: float, b: float) -> tuple[float, float, float]:  # NOQA: E741
    return l, (a ** 2 + b ** 2) ** 0.5, math.degrees(math.atan2(b, a)) % 360


def lch_to_lab(l: float, c: float, h: float) -> tuple[float, float, float]:  # NOQA: E741
    h = math.radians(h)
    return l, math.cos(h) * c, math.sin(h) * c


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


def cie76(l1: float, a1: float, b1: float, l2: float, a2: float, b2: float) -> float:
    return ((l1 - l2) ** 2 + (a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5


def cie94(l1: float, a1: float, b1: float, l2: float, a2: float, b2: float, k: Literal[1, 2] = 1) -> float:
    c1 = (a1 ** 2 + b1 ** 2) ** 0.5
    dc = (a2 ** 2 + b2 ** 2) ** 0.5 - c1
    if k == 1:
        k1 = 0.045
        k2 = 0.015
    else:
        k1 = 0.048
        k2 = 0.014
    return (((l1 - l2) / k) ** 2 + (dc / (1 + k1 * c1)) ** 2 + ((((a1 - a2) ** 2 + (b1 - b2) ** 2 - dc ** 2) ** 0.5) / (1 + k2 * c1)) ** 2) ** 0.5


def ciede2000(l1: float, a1: float, b1: float, l2: float, a2: float, b2: float) -> float:
    cx = ((a1 ** 2 + b1 ** 2) ** 0.5 + (a2 ** 2 + b2 ** 2) ** 0.5) / 2
    gx = 0.5 * (1 - (cx ** 7 / (cx ** 7 + 25 ** 7)) ** 0.5)
    nn = (1 + gx) * a1
    c1 = (nn ** 2 + b1 ** 2) ** 0.5
    h1 = math.degrees(math.atan2(b1, nn)) % 360
    nn = (1 + gx) * a2
    c2 = (nn ** 2 + b2 ** 2) ** 0.5
    h2 = math.degrees(math.atan2(b2, nn)) % 360
    dc = c2 - c1
    if c1 == 0 or c2 == 0:
        dh = 0
    else:
        nn = h2 - h1
        if abs(nn) <= 180:
            dh = h2 - h1
        else:
            dh = h2 - h1 + (-1 if nn > 180 else 1) * 360
    dh = 2 * (c1 * c2) ** 0.5 * math.sin(math.radians(dh / 2))
    lx = (l1 + l2) / 2
    cy = (c1 + c2) / 2
    if c1 == 0 or c2 == 0:
        hx = h1 + h2
    else:
        if abs(h1 - h2) > 180:
            hx = h1 + h2 + (-1 if h2 + h1 > 360 else 1) * 360
        else:
            hx = h1 + h2
        hx /= 2
    tx = 1 - 0.17 * math.cos(math.radians(hx - 30)) + 0.24 * math.cos(math.radians(2 * hx)) + 0.32 * math.cos(math.radians(3 * hx + 6)) - 0.20 * math.cos(math.radians(4 * hx - 63))
    dc /= 1 + 0.045 * cy
    dh /= 1 + 0.015 * cy * tx
    return (((l2 - l1) / (1 + (0.015 * (lx - 50) ** 2) / (20 + (lx - 50) ** 2) ** 0.5)) ** 2 + dc ** 2 + dh ** 2 + (-math.sin(math.radians(2 * (30 * math.e ** (-((hx - 275) / 25) ** 2)))) * (2 * (cy ** 7 / (cy ** 7 + 25 ** 7)) ** 0.5)) * dc * dh) ** 0.5


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f'#{r:02x}{g:02x}{b:02x}'


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip('#')
    return int(h[:2], 16), int(h[2:4], 16), int(h[4:], 16)


def lab_to_hex(l: float, a: float, b: float) -> str:  # NOQA: E741
    return rgb_to_hex(*(round(color * 255) for color in xyz_to_srgb(*lab_to_xyz(l, a, b))))


def format_cmyk(c: float, m: float, y: float, k: float) -> str:
    return f'{"%, ".join(str(round(c_ * 100)) for c_ in (c, m, y, k))}%'


def format_hsv(h: float, s: float, v: float) -> str:
    return f'{round(h * 360)}°, {"%, ".join(str(round(c * 100)) for c in (s, v))}%'


def format_hls(h: float, l: float, s: float) -> str:  # NOQA: E741
    return format_hsv(h, s, l)


def get(color: str) -> str:
    color = color.strip().lstrip('#').lower()
    try:
        return load()[color]
    except KeyError:
        return f'#{color.upper()}'


@functools.cache
def _rgb_to_hex() -> dict[tuple[int, int, int], str]:
    return {hex_to_rgb(hex_color): hex_color for hex_color in load()}


@functools.lru_cache
def get_nearest_color(color: str) -> tuple[str, str]:
    if not (name := get(color)).startswith('#'):
        return color.upper(), name
    rgb_to_hex_ = _rgb_to_hex()
    rgb_color = hex_to_rgb(color)
    min_distance = math.inf
    nearest_color_rgb = 0, 0, 0
    for cur_color in rgb_to_hex_:
        distance = sum((rgb_color[i] - cur_color[i]) ** 2 for i in range(3))
        if min_distance > distance:
            min_distance = distance
            nearest_color_rgb = cur_color
    nearest_color = rgb_to_hex_[nearest_color_rgb]
    return f'#{nearest_color.upper()}', load()[nearest_color]


@functools.cache
def _lab_to_hex() -> dict[tuple[float, float, float], str]:
    return {xyz_to_lab(*srgb_to_xyz(*(color / 255 for color in hex_to_rgb(
        hex_color)))): hex_color for hex_color in load()}


@functools.lru_cache
def get_nearest_color_lab(color: str) -> tuple[str, str]:
    if not (name := get(color)).startswith('#'):
        return color.upper(), name
    lab_to_hex_ = _lab_to_hex()
    lab_color = xyz_to_lab(*srgb_to_xyz(*(color / 255 for color in hex_to_rgb(color))))
    min_distance = math.inf
    nearest_color_rgb = 0.0, 0.0, 0.0
    for cur_color in lab_to_hex_:
        distance = ciede2000(*lab_color, *cur_color)
        if min_distance > distance:
            min_distance = distance
            nearest_color_rgb = cur_color
    nearest_color = lab_to_hex_[nearest_color_rgb]
    return f'#{nearest_color.upper()}', load()[nearest_color]


@functools.cache
def load() -> dict[str, str]:
    return json.load((importlib.resources.files(__name__) / _PATH).open(encoding='utf-8'))


if __debug__:
    def download():
        import urllib.parse
        import urllib.request
        urllib.request.urlretrieve(urllib.parse.urljoin(
            'https://raw.githubusercontent.com/meodai/color-names/master/dist/',
            _PATH), str(importlib.resources.files(__name__) / _PATH))
        load.cache_clear()
        load()
