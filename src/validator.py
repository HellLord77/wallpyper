import enum
import os
import re
import sys
from typing import Any
from typing import AnyStr
from typing import Callable
from typing import Hashable
from typing import Iterable
from typing import MutableSequence
from typing import Optional


def ensure_truthy(current: dict, default: dict, key: str,
                  func: Callable[[Any], bool] = bool) -> bool:
    val = current[key]
    if func(val):
        return True
    current[key] = default[key]
    return False


# noinspection PyShadowingBuiltins
def ensure_min_len(current: dict, default: dict, key: str,
                   min: int, keep: bool = True, unique: bool = False) -> bool:
    val: MutableSequence = current[key]
    if min <= len(val):
        return True
    if keep:
        val.extend((set(default[key]) - set(val))
                   if unique else default[key][len(val):min])
    else:
        val[:] = default[key]
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
        val[:] = default[key]
    return False


# noinspection PyShadowingBuiltins
def ensure_len(current: dict, default: dict, key: str,
               len: int, keep: bool = True, right: bool = False) -> bool:
    return (ensure_min_len(current, default, key, len, keep) and
            ensure_max_len(current, default, key, len, keep, right))


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


def ensure_search(current: dict, default: dict, key: str,
                  pattern: re.Pattern, flags: int | re.RegexFlag = re.NOFLAG) -> bool:
    val: AnyStr = current[key]
    if re.search(pattern, val, flags) is not None:
        return True
    current[key] = default[key]
    return False


def ensure_contains(current: dict, default: dict, key: str,
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
    return ensure_contains(current, default, key, range(1, max))


# noinspection PyShadowingBuiltins
def ensure_negative(current: dict, default: dict, key: str,
                    min: int = -sys.maxsize) -> bool:
    return ensure_contains(current, default, key, range(-1, min, -1))


# noinspection PyShadowingNames
def ensure_enum_name(current: dict, default: dict, key: str,
                     enum: type[enum.Enum], casefold: bool = True) -> bool:
    return ensure_contains(current, default, key,
                           (member.name for member in enum), casefold)


# noinspection PyShadowingNames
def ensure_enum_value(current: dict, default: dict, key: str,
                      enum: type[enum.Enum], casefold: bool = True) -> bool:
    return ensure_contains(current, default, key,
                           (member.value for member in enum), casefold)


def ensure_subset(current: dict, _: dict, key: str,
                  iterable: Iterable[str], unique: bool = True, casefold: bool = True) -> bool:
    val: list[str] = current[key]
    iterable = tuple(iterable)
    if casefold:
        val = [item.casefold() for item in val]
        iterable_ = tuple(item.casefold() for item in iterable)
    else:
        iterable_ = iterable
    vals = []
    not_fixed = not unique or ensure_unique(
        current, _, key, str.casefold if casefold else None)
    for item in val:
        try:
            index = iterable_.index(item)
        except ValueError:
            not_fixed = False
        else:
            vals.append(iterable[index])
    current[key] = vals
    return not_fixed


def ensure_unordered(current: dict, default: dict, key: str,
                     unique: bool = True, casefold: bool = True) -> bool:
    not_fixed = ensure_subset(current, default, key, default[key], unique, casefold)
    return ensure_min_len(current, default, key, len(default[key]), unique=unique) or not_fixed


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
