from __future__ import annotations

__version__ = '0.0.2'  # https://github.com/intoli/user-agents

import enum
import json
import os
import random
import typing
from typing import Container, Iterator, MutableMapping, Optional

_PATH = 'user-agents.json'
_USERAGENTS: Optional[list[tuple[float, UserAgent]]] = None


class AppName(enum.StrEnum):
    NETSCAPE = 'Netscape'


class EffectiveType(enum.StrEnum):
    ET_3G = '3g'
    ET_4G = '4g'


class Type(enum.StrEnum):
    ETHERNET = 'ethernet'
    CELLULAR = 'cellular'
    WIFI = 'wifi'
    UNKNOWN = 'unknown'


class Platform(enum.StrEnum):
    IPAD = 'iPad'
    IPHONE = 'iPhone'
    LINUX_AAARCH64 = 'Linux aarch64'
    LINUX_ARMV7L = 'Linux armv7l'
    LINUX_ARMV8L = 'Linux armv8l'
    LINUX_ARMV81 = 'Linux armv81'
    LINUX_X86_64 = 'Linux x86_64'
    MACINTEL = 'MacIntel'
    WIN32 = 'Win32'
    WINDOWS = 'Windows'


class Vendor(enum.StrEnum):
    NAVER = 'NAVER Corp.'
    APPLE = 'Apple Computer, Inc.'
    GOOGLE = 'Google Inc.'


class DeviceCategory(enum.StrEnum):
    DESKTOP = 'desktop'
    MOBILE = 'mobile'
    TABLET = 'tablet'


PLATFORM_APPLE = {Platform.IPAD, Platform.IPHONE, Platform.MACINTEL}
PLATFORM_LINUX = {Platform.LINUX_AAARCH64, Platform.LINUX_ARMV7L,
                  Platform.LINUX_ARMV8L, Platform.LINUX_ARMV81, Platform.LINUX_X86_64}
PLATFORM_WINDOWS = {Platform.WIN32, Platform.WINDOWS}


class Connection(typing.NamedTuple):
    downlink: Optional[int | float]
    downlink_max: Optional[int | float]
    effective_type: Optional[EffectiveType]
    rtt: Optional[int]
    type: Optional[Type]


class UserAgent(typing.NamedTuple):
    app_name: AppName
    connection: Optional[Connection]
    platform: Platform
    plugins_length: int
    vendor: Vendor
    user_agent: str
    viewport_height: Optional[int]
    viewport_width: Optional[int]
    device_category: DeviceCategory
    screen_height: int
    screen_width: int


def _set(mapping: MutableMapping, key: str, new_key: Optional[str] = None):
    mapping[key if new_key is None else new_key] = mapping.pop(key, None)


def _set_enum(mapping: MutableMapping, key: str,
              str_enum: type[enum.StrEnum], new_key: Optional[str] = None):
    if (val := mapping.pop(key, None)) is not None:
        val = str_enum(val)
    mapping[key if new_key is None else new_key] = val


def _load() -> list[tuple[float, UserAgent]]:
    global _USERAGENTS
    if _USERAGENTS is None:
        _USERAGENTS = []
        with open(os.path.join(os.path.dirname(__file__), _PATH), encoding='utf-8') as file:
            for useragent in json.load(file):
                _set_enum(useragent, 'appName', AppName, 'app_name')
                if (connection := useragent.get('connection')) is None:
                    useragent['connection'] = None
                else:
                    _set(connection, 'downlink')
                    _set(connection, 'downlinkMax', 'downlink_max')
                    _set_enum(connection, 'effectiveType', EffectiveType, 'effective_type')
                    _set(connection, 'rtt')
                    _set_enum(connection, 'type', Type)
                    useragent['connection'] = Connection(**connection)
                _set_enum(useragent, 'platform', Platform)
                _set(useragent, 'pluginsLength', 'plugins_length')
                _set_enum(useragent, 'vendor', Vendor)
                _set(useragent, 'userAgent', 'user_agent')
                _set(useragent, 'viewportHeight', 'viewport_height')
                _set(useragent, 'viewportWidth', 'viewport_width')
                _set_enum(useragent, 'deviceCategory', DeviceCategory, 'device_category')
                _set(useragent, 'screenHeight', 'screen_height')
                _set(useragent, 'screenWidth', 'screen_width')
                _USERAGENTS.append((useragent.pop('weight'), UserAgent(**useragent)))
    return _USERAGENTS


def _filter(platform: Optional[str | Platform | Container[Platform]], vendor: Optional[str | Vendor | Container[Vendor]],
            device_category: Optional[str | DeviceCategory | Container[DeviceCategory]]) -> Iterator[tuple[float, UserAgent]]:
    useragents = _load()
    if isinstance(platform, (str, Platform)):
        platform = platform,
    if isinstance(vendor, (str, Vendor)):
        vendor = vendor,
    if isinstance(device_category, (str, DeviceCategory)):
        device_category = device_category,
    return ((weight, useragent) for weight, useragent in useragents if
            (platform is None or useragent.platform in platform) and
            (vendor is None or useragent.vendor in vendor) and
            (device_category is None or useragent.device_category in device_category))


def get_max(platform: Optional[str | Platform | Container[Platform]] = None,
            vendor: Optional[str | Vendor | Container[Vendor]] = None,
            device_category: Optional[str | DeviceCategory | Container[DeviceCategory]] = None) -> UserAgent:
    weights, useragents = zip(*_filter(platform, vendor, device_category))
    return useragents[weights.index(max(weights))]


def get_min(platform: Optional[str | Platform | Container[Platform]] = None,
            vendor: Optional[str | Vendor | Container[Vendor]] = None,
            device_category: Optional[str | DeviceCategory | Container[DeviceCategory]] = None) -> UserAgent:
    weights, useragents = zip(*_filter(platform, vendor, device_category))
    return useragents[weights.index(min(weights))]


def get_random(platform: Optional[str | Platform | Container[Platform]] = None,
               vendor: Optional[str | Vendor | Container[Vendor]] = None,
               device_category: Optional[str | DeviceCategory | Container[DeviceCategory]] = None) -> UserAgent:
    weights, useragents = zip(*_filter(platform, vendor, device_category))
    return random.choices(useragents, weights)[0]


if __debug__:
    def _download():
        import urllib.parse
        import urllib.request
        import gzip
        path = os.path.join(os.path.dirname(__file__), _PATH)
        with open(path, 'wb') as file:
            file.write(gzip.decompress(urllib.request.urlopen(urllib.parse.urljoin(
                'https://github.com/intoli/user-agents/raw/master/src/', f'{_PATH}.gz')).read()))
        with open(path, encoding='utf-8') as file:
            json.load(file)
