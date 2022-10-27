__version__ = '0.0.1'  # https://github.com/ai/easings.net

import math
from typing import Callable, Optional

_c1 = 1.70158
_c2 = _c1 * 1.525
_c3 = _c1 + 1
_c4 = (2 * math.pi) / 3
_c5 = (2 * math.pi) / 4.5
_n1 = 7.5625
_d1 = 2.75


class Ease:
    SINE = 'sine'
    QUAD = 'quad'
    CUBIC = 'cubic'
    QUART = 'quart'
    QUINT = 'quint'
    EXPO = 'expo'
    CIRC = 'circ'
    BACK = 'back'
    ELASTIC = 'elastic'
    BOUNCE = 'bounce'


def linear(x: float) -> float:
    return x


def in_sine(x: float) -> float:
    return 1 - math.cos((x * math.pi) / 2)


def out_sine(x: float) -> float:
    return math.sin((x * math.pi) / 2)


def in_out_sine(x: float) -> float:
    return -(math.cos(math.pi * x) - 1) / 2


def in_quad(x: float) -> float:
    return x ** 2


def out_quad(x: float) -> float:
    return 1 - (1 - x) ** 2


def in_out_quad(x: float) -> float:
    return 2 * x ** 2 if x < 0.5 else 1 - (-2 * x + 2) ** 2 / 2


def in_cubic(x: float) -> float:
    return x ** 3


def out_cubic(x: float) -> float:
    return 1 - (1 - x) ** 3


def in_out_cubic(x: float) -> float:
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def in_quart(x: float) -> float:
    return x ** 4


def out_quart(x: float) -> float:
    return 1 - (1 - x) ** 4


def in_out_quart(x: float) -> float:
    return 8 * x ** 4 if x < 0.5 else 1 - (-2 * x + 2) ** 4 / 2


def in_quint(x: float) -> float:
    return x ** 5


def out_quint(x: float) -> float:
    return 1 - (1 - x) ** 5


def in_out_quint(x: float) -> float:
    return 16 * x ** 5 if x < 0.5 else 1 - (-2 * x + 2) ** 5 / 2


def in_expo(x: float) -> float:
    return 0 if x == 0 else 2 ** (10 * x - 10)


def out_expo(x: float) -> float:
    return 1 if x == 1 else 1 - 2 ** (-10 * x)


def in_out_expo(x: float) -> float:
    return 0 if x == 0 else 1 if x == 1 else 2 ** (20 * x - 10) / 2 if x < 0.5 else (2 - 2 ** (-20 * x + 10)) / 2


def in_circ(x: float) -> float:
    return 1 - (1 - x ** 2) ** 0.5


def out_circ(x: float) -> float:
    return (1 - (x - 1) ** 2) ** 0.5


def in_out_circ(x: float) -> float:
    return (1 - (1 - (2 * x) ** 2) ** 0.5) / 2 if x < 0.5 else ((1 - (-2 * x + 2) ** 2) ** 0.5 + 1) / 2


def in_back(x: float) -> float:
    return _c3 * x ** 3 - _c1 * x ** 2


def out_back(x: float) -> float:
    return 1 + _c3 * (x - 1) ** 3 + _c1 * (x - 1) ** 2


def in_out_back(x: float) -> float:
    return ((2 * x) ** 2 * ((_c2 + 1) * 2 * x - _c2)) / 2 if x < 0.5 else ((2 * x - 2) ** 2 * ((_c2 + 1) * (x * 2 - 2) + _c2) + 2) / 2


def in_elastic(x: float) -> float:
    return 0 if x == 0 else 1 if x == 1 else -2 ** (10 * x - 10) * math.sin((x * 10 - 10.75) * _c4)


def out_elastic(x: float) -> float:
    return 0 if x == 0 else 1 if x == 1 else 2 ** (-10 * x) * math.sin((x * 10 - 0.75) * _c4) + 1


def in_out_elastic(x: float) -> float:
    return 0 if x == 0 else 1 if x == 1 else -(2 ** (20 * x - 10) * math.sin((20 * x - 11.125) * _c5)) / 2 if x < 0.5 else (2 ** (-20 * x + 10) * math.sin((20 * x - 11.125) * _c5)) / 2 + 1


def in_bounce(x: float) -> float:
    return 1 - out_bounce(1 - x)


def out_bounce(x: float) -> float:
    if x < 1 / _d1:
        return _n1 * x ** 2
    elif x < 2 / _d1:
        x -= 1.5 / _d1
        return _n1 * x ** 2 + 0.75
    elif x < 2.5 / _d1:
        x -= 2.25 / _d1
        return _n1 * x ** 2 + 0.9375
    else:
        x -= 2.625 / _d1
        return _n1 * x ** 2 + 0.984375


def in_out_bounce(x: float) -> float:
    return (1 - out_bounce(1 - 2 * x)) / 2 if x < 0.5 else (1 + out_bounce(2 * x - 1)) / 2


def get(ease: Optional[str] = None, in_: bool = False, out: bool = False) -> Callable[[float], float]:
    easing = []
    if in_:
        easing.append('in')
    if out:
        easing.append('out')
    if ease is None or not easing:
        return linear
    else:
        easing.append(ease)
        return globals()['_'.join(easing)]
