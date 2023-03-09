import enum
import os.path
import re
from typing import Iterable


def from_truthy(current: dict, default: dict, key: str) -> bool:
    val = current[key]
    if val:
        return True
    current[key] = default[key]
    return False


def from_pattern(current: dict, default: dict, key: str,
                 pattern: re.Pattern, flags: int | re.RegexFlag = re.NOFLAG) -> bool:
    val = current[key]
    if re.fullmatch(pattern, val, flags) is not None:
        return True
    current[key] = default[key]
    return False


def from_iterable(current: dict, default: dict, key: str,
                  iterable: Iterable, casefold: bool = True) -> bool:
    val = current[key]
    if isinstance(val, str) and casefold:
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


# noinspection PyShadowingNames
def from_enum_names(current: dict, default: dict, key: str,
                    enum: type[enum.Enum], casefold: bool = True) -> bool:
    return from_iterable(current, default, key, (member.name for member in enum), casefold)


# noinspection PyShadowingNames
def from_enum_values(current: dict, default: dict, key: str,
                     enum: type[enum.Enum], casefold: bool = True) -> bool:
    return from_iterable(current, default, key, (member.value for member in enum), casefold)


def from_joined_iterable(current: dict, _: dict, key: str,
                         iterable: Iterable[str], separator: str = ',', casefold: bool = True) -> bool:
    val = current[key]
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
def from_disk(current: dict, default: dict, key: str,
              file: bool = True, dir: bool = True) -> bool:
    val = current[key]
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
