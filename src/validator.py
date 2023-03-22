import enum
import os.path
import re
import sys
from typing import Any, AnyStr, Callable, Hashable, Iterable, MutableSequence, Optional


def ensure_truthy(current: dict, default: dict, key: str,
                  func: Callable[[Any], bool] = bool) -> bool:
    val = current[key]
    if func(val):
        return True
    current[key] = default[key]
    return False


# noinspection PyShadowingBuiltins
def ensure_min_len(current: dict, default: dict, key: str,
                   min: int, keep: bool = True) -> bool:
    val: MutableSequence = current[key]
    if min <= len(val):
        return True
    if keep:
        for index in range(len(val), min):
            val.append(default[key][index])
    else:
        val.clear()
        val.extend(default[key])
    return False


# noinspection PyShadowingBuiltins
def ensure_max_len(current: dict, default: dict, key: str,
                   max: int, keep: bool = True, right: bool = False) -> bool:
    val: MutableSequence = current[key]
    if max >= len(val):
        return True
    if keep:
        index = 0 if right else -1
        for _ in range(len(val) - max):
            del val[index]
    else:
        val.clear()
        val.extend(default[key])
    return False


# noinspection PyShadowingBuiltins
def ensure_len(current: dict, default: dict, key: str,
               len: int, keep: bool = True, right: bool = False) -> bool:
    min_len = ensure_min_len(current, default, key, len, keep)
    max_len = ensure_max_len(current, default, key, len, keep, right)
    return min_len and max_len


def ensure_unique(current: dict, _: dict, key: str,
                  func: Optional[Callable[[Any], Hashable]] = None) -> bool:
    val: MutableSequence = current[key]
    keep = {item if func is None else func(item): index
            for index, item in enumerate(val)}.values()
    if len(keep) == len(val):
        return True
    for index in (index for index in reversed(
            range(len(val))) if index not in keep):
        del val[index]
    return False


def ensure_pattern(current: dict, default: dict, key: str,
                   pattern: re.Pattern, flags: int | re.RegexFlag = re.NOFLAG) -> bool:
    val: AnyStr = current[key]
    if re.fullmatch(pattern, val, flags) is not None:
        return True
    current[key] = default[key]
    return False


def ensure_iterable(current: dict, default: dict, key: str,
                    iterable: Iterable, casefold: bool = True) -> bool:
    val = current[key]
    if casefold and isinstance(val, str):
        val = val.casefold()
        for item in iterable:
            if val == item.casefold():
                current[key] = item
                return True
    else:
        if val in iterable:
            return True
    current[key] = default[key]
    return False


# noinspection PyShadowingBuiltins
def ensure_positive(current: dict, default: dict, key: str,
                    max: int = sys.maxsize) -> bool:
    return ensure_iterable(current, default, key, range(1, max))


# noinspection PyShadowingBuiltins
def ensure_negative(current: dict, default: dict, key: str,
                    min: int = -sys.maxsize) -> bool:
    return ensure_iterable(current, default, key, range(-1, min, -1))


# noinspection PyShadowingNames
def ensure_enum_names(current: dict, default: dict, key: str,
                      enum: type[enum.Enum], casefold: bool = True) -> bool:
    return ensure_iterable(current, default, key, (member.name for member in enum), casefold)


def ensure_joined_iterable(current: dict, _: dict, key: str,
                           iterable: Iterable[str], separator: str = ',', casefold: bool = True) -> bool:
    val: str = current[key]
    iterable = tuple(iterable)
    if casefold:
        val = val.casefold()
        iterable_ = tuple(item.casefold() for item in iterable)
    else:
        iterable_ = iterable
    vals = []
    not_fixed = True
    for item in val.split(separator):
        try:
            index = iterable_.index(item)
        except ValueError:
            not_fixed = False
        else:
            vals.append(iterable[index])
    current[key] = separator.join(vals)
    return not_fixed


# noinspection PyShadowingBuiltins
def ensure_disk(current: dict, default: dict, key: str,
                file: bool = True, dir: bool = True) -> bool:
    val: AnyStr = current[key]
    if val:
        val = os.path.realpath(val)
        if file and dir:
            not_fixed = os.path.exists(val)
        elif file:
            not_fixed = os.path.isfile(val)
        elif dir:
            not_fixed = os.path.isdir(val)
        else:
            not_fixed = not os.path.exists(val)
    else:
        not_fixed = False
    current[key] = val if not_fixed else default[key]
    return not_fixed
