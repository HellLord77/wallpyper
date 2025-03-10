__version__ = '0.1.1'  # https://github.com/intoli/user-agents

import enum
import functools
import importlib.resources
import json
import random
from typing import Container
from typing import Iterator
from typing import Literal
from typing import MutableMapping
from typing import NamedTuple
from typing import Optional

_PATH = 'user-agents.json'


class EffectiveType(enum.StrEnum):
    ET_3G = '3g'
    ET_4G = '4g'


class Type(enum.StrEnum):
    CELLULAR = 'cellular'
    WIFI = 'wifi'


class Platform(enum.StrEnum):
    IPAD = 'iPad'
    IPHONE = 'iPhone'
    LINUX_AAARCH64 = 'Linux aarch64'
    LINUX_ARMV81 = 'Linux armv81'
    LINUX_ARMV8L = 'Linux armv8l'
    LINUX_X86_64 = 'Linux x86_64'
    MACINTEL = 'MacIntel'
    WIN32 = 'Win32'


class Vendor(enum.StrEnum):
    APPLE = 'Apple Computer, Inc.'
    GOOGLE = 'Google Inc.'
    NONE = ''


class DeviceCategory(enum.StrEnum):
    DESKTOP = 'desktop'
    MOBILE = 'mobile'
    TABLET = 'tablet'


PLATFORM_APPLE = {Platform.IPAD, Platform.IPHONE, Platform.MACINTEL}
PLATFORM_LINUX = {Platform.LINUX_AAARCH64, Platform.LINUX_ARMV81,
                  Platform.LINUX_ARMV8L, Platform.LINUX_X86_64}
PLATFORM_WINDOWS = {Platform.WIN32}


class Connection(NamedTuple):
    downlink: int | float
    effective_type: EffectiveType
    rtt: int
    downlink_max: Optional[int | float]
    type: Optional[Type]


class UserAgent(NamedTuple):
    app_name: Literal['Netscape']
    connection: Optional[Connection]
    language: Optional[str]
    oscpu: Optional[str]
    platform: Platform
    plugins_length: int
    screen_height: int
    screen_width: int
    user_agent: str
    vendor: Vendor
    device_category: DeviceCategory
    viewport_height: int
    viewport_width: int


def _filter(platform: Optional[str | Platform | Container[Platform]], vendor: Optional[str | Vendor | Container[Vendor]],
            device_category: Optional[str | DeviceCategory | Container[DeviceCategory]]) -> Iterator[tuple[float, UserAgent]]:
    if isinstance(platform, (str, Platform)):
        platform = platform,
    if isinstance(vendor, (str, Vendor)):
        vendor = vendor,
    if isinstance(device_category, (str, DeviceCategory)):
        device_category = device_category,
    return ((weight, useragent) for weight, useragent in load() if
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


def _set(mapping: MutableMapping, key: str, new_key: Optional[str] = None):
    mapping[key if new_key is None else new_key] = mapping.pop(key, None)


def _set_enum(mapping: MutableMapping, key: str,
              str_enum: type[enum.StrEnum], new_key: Optional[str] = None):
    if (val := mapping.pop(key, None)) is not None:
        val = str_enum(val)
    mapping[key if new_key is None else new_key] = val


@functools.cache
def load() -> list[tuple[float, UserAgent]]:
    useragents = []
    for useragent in json.load((importlib.resources.files(
            __name__) / _PATH).open(encoding='utf-8')):
        useragent: dict
        _set(useragent, 'appName', 'app_name')
        if (connection := useragent.setdefault('connection')) is not None:
            connection['effective_type'] = EffectiveType(connection.pop('effectiveType'))
            _set(connection, 'downlinkMax', 'downlink_max')
            _set_enum(connection, 'type', Type)
            useragent['connection'] = Connection(**connection)
        _set(useragent, 'language')
        _set(useragent, 'oscpu')
        useragent['platform'] = Platform(useragent['platform'])
        useragent['plugins_length'] = useragent.pop('pluginsLength')
        useragent['screen_height'] = useragent.pop('screenHeight')
        useragent['screen_width'] = useragent.pop('screenWidth')
        useragent['user_agent'] = useragent.pop('userAgent')
        useragent['vendor'] = Vendor(useragent['vendor'])
        useragent['device_category'] = DeviceCategory(useragent.pop('deviceCategory'))
        useragent['viewport_height'] = useragent.pop('viewportHeight')
        useragent['viewport_width'] = useragent.pop('viewportWidth')
        useragents.append((useragent.pop('weight'), UserAgent(**useragent)))
    return useragents


if __debug__:
    def download():
        import gzip
        import os
        import urllib.parse
        import urllib.request
        with open(os.path.join(os.path.dirname(__file__), _PATH), 'wb') as file:
            file.write(gzip.decompress(urllib.request.urlopen(urllib.parse.urljoin(
                'https://github.com/intoli/user-agents/raw/main/src/', f'{_PATH}.gz')).read()))
        load.cache_clear()
        load()
