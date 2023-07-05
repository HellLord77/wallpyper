from __future__ import annotations

__version__ = '0.3.1'

import binascii
import copy
import dataclasses
import fractions
import functools
import hashlib
import itertools
import os
import tempfile
import urllib.parse
from typing import Any, Callable, Iterator, Optional, TypedDict, final

import consts
import gui
import langs
import validator
import win32
from libs import callables, files, request, utils

KEY: Optional[bytes | str] = None
SOURCES: dict[str, type[Source]] = {}

CONFIG_ORIENTATIONS = '_orientations_'
CONFIG_RATINGS = '_ratings_'

# noinspection PyUnresolvedReferences
_cache = hashlib.__builtin_constructor_cache
_reduced = functools.cache(callables.ReducedCallable)


class Hash:
    # noinspection PyShadowingBuiltins
    def __init_subclass__(cls, hash: bool = True):
        if hash:
            _cache[cls.name] = cls
            # noinspection PyUnresolvedReferences
            hashlib.algorithms_available.add(cls.name)

    # noinspection PyUnusedLocal
    def __init__(self, data: bytes = b''):
        raise NotImplementedError

    def update(self, data: bytes):
        raise NotImplementedError

    def digest(self) -> bytes:
        return bytes.fromhex(self.hexdigest())

    def hexdigest(self) -> str:
        return binascii.hexlify(self.digest()).decode()

    def copy(self) -> Hash:
        return copy.deepcopy(self)

    @property
    def digest_size(self) -> int:
        raise NotImplementedError

    @property
    def block_size(self) -> int:
        raise NotImplementedError

    # noinspection PyPropertyDefinition
    @classmethod
    @property
    def name(cls) -> str:
        return cls.__name__.lower()


@dataclasses.dataclass
class File:
    request: str | request.Request
    name: str = ''
    # noinspection PyUnresolvedReferences
    size: int = request.RETRIEVE_UNKNOWN_SIZE
    url: Optional[str] = dataclasses.field(default=None, repr=False)
    sha256: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)
    md5: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)
    hash: Optional[dict[str | type[Hash] | Hash, bytes | str]] = \
        dataclasses.field(default=None, repr=False, kw_only=True)

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.__hash__ = cls.__hash__
        cls.__eq__ = cls.__eq__

    def __post_init__(self):
        if isinstance(self.request, str):
            self.request = request.Request(request.Method.GET, self.request)
        if self.request.params is not None:
            self.request.url = request.encode_params(self.request.url, self.request.params)
            self.request.params = None
        # TODO BasicAuth
        if not self.name:
            self.name = urllib.parse.unquote_plus(
                os.path.basename(request.strip_url(self.request.url)))
        name, ext = os.path.splitext(self.name)
        self.name = utils.shrink_string_mid(win32.sanitize_filename(
            name.strip().removesuffix(ext) + ext), consts.MAX_FILENAME_LEN)
        if self.url is None and self.is_simple():
            self.url = self.request.url
        if self.hash is not None:
            for hash_ in tuple(self.hash.keys()):
                if not isinstance(hash_, str):
                    # noinspection PyTypeChecker
                    self.hash[hash_.name] = self.hash.pop(hash_)
            vars(self).update(self.hash)
            self.hash = None
        for algorithm, hash_ in self._iter_hashes():
            if not isinstance(hash_, bytes):
                setattr(self, algorithm, bytes.fromhex(hash_))

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return repr(self).replace(f'request={self.request!r}', f'url={self.request.url}', 1).replace(
            f', size={self.size}', f', size={files.Size(self.size)}' if self.size else '', 1)

    def __eq__(self, other):
        if isinstance(other, File):
            return self.name == other.name
        return NotImplemented

    @classmethod
    def fromdict(cls, data: dict[str, Any]) -> Optional[File]:
        request_ = utils.decrypt(data.pop('request'), KEY, on_error=None)
        if request_ is not None:
            return _reduced(cls)(request_, **data)

    def _iter_hashes(self, filled: bool = False) -> Iterator[tuple[str, bytes | str]]:
        for algorithm in hashlib.algorithms_available:
            hash_ = getattr(self, algorithm, None)
            if hash_ is not None and (not filled or hash_):
                yield algorithm, hash_

    def asdict(self) -> dict[str, Any]:
        result: dict = {'request': utils.encrypt(
            self.request, KEY, as_string=True), 'name': self.name}
        if self.size != request.RETRIEVE_UNKNOWN_SIZE:
            result['size'] = self.size
        if self.url and self.url != self.request.url and self.is_simple():
            result['url'] = self.url
        hashes = {algorith: binascii.hexlify(
            hash_).decode() for algorith, hash_ in self._iter_hashes(True)}
        if hashes:
            result['hash'] = hashes
        return result

    def checksize(self, path: str) -> bool:
        if self.size:
            try:
                return self.size == os.path.getsize(path)
            except OSError:
                pass
        return False

    def checksum(self, path: str) -> bool:
        for algorithm, hash_ in self._iter_hashes(True):
            try:
                return files.checksum(path, hash_, algorithm)
            except OSError:
                return False

    # noinspection PyShadowingBuiltins
    def fill(self, path: str, hash: bool = True) -> bool:
        if not self.size:
            try:
                self.size = os.path.getsize(path)
            except OSError:
                return False
        if hash and not any(self._iter_hashes(True)):
            for algorithm, hash_ in self._iter_hashes():
                if not hash_:
                    try:
                        hash_ = files.get_hash(path, algorithm)
                    except OSError:
                        return False
                    else:
                        setattr(self, algorithm, hash_.digest())
                        break
        return True

    def is_simple(self) -> bool:
        return (self.request.method == request.Method.GET and
                self.request.headers is None and self.request.files is None and
                self.request.data is None and self.request.params is None and
                self.request.auth is None and self.request.cookies is None and
                self.request.json is None and self.request.unredirected_hdrs is None)

    # noinspection PyUnresolvedReferences
    def _response_callback(self, query_callback: Callable[[int, int], bool],
                           response: request.Response) -> bool:
        if self.size == request.RETRIEVE_UNKNOWN_SIZE:
            self.size = request.get_size(response)
        return query_callback(0, self.size) if response else False

    def download(self, path: str, query_callback: Optional[Callable[[int, int], bool]] = None) -> bool:
        return request.retrieve(self.request, path, self.size, chunk_count=100,
                                response_callback=bool if query_callback is None else functools.partial(
                                    self._response_callback, query_callback), query_callback=query_callback)


@dataclasses.dataclass
class ImageFile(File):
    width: int = 0
    height: int = 0
    ratio: float = 0.0
    sketchy: bool = False
    nsfw: bool = False

    def __post_init__(self):
        super().__post_init__()
        if not self.ratio and self.height:
            self.ratio = self.width / self.height

    def __str__(self):
        ratio = fractions.Fraction(self.ratio).limit_denominator(100)
        return super().__str__().replace(f'ratio={self.ratio}', f'ratio={ratio.numerator}:{ratio.denominator}', 1)

    def asdict(self) -> dict[str, Any]:
        result = super().asdict()
        if self.width:
            result['width'] = self.width
        if self.height:
            result['height'] = self.height
        if self.ratio and (not self.height or
                           self.ratio != self.width / self.height):
            result['ratio'] = self.ratio
        if self.sketchy:
            result['sketchy'] = self.sketchy
        if self.nsfw:
            result['nsfw'] = self.nsfw
        if 'hash' in result:
            result['hash'] = result.pop('hash')
        return result

    # noinspection PyShadowingBuiltins
    def fill(self, path: str, hash: bool = True, dimensions: bool = True) -> bool:
        if super().fill(path, hash):
            if dimensions:
                if (dimensions_ := win32.get_dimensions_image(path)) is None:
                    return False
                else:
                    if not self.width:
                        self.width = dimensions_[0]
                    if not self.height:
                        self.height = dimensions_[1]
        return True

    def is_animated(self) -> bool:  # TODO
        return files.get_ext(self.name).lower() in ('gif', 'webp')

    def is_square(self, tolerance: float = 0.05) -> bool:
        return self.ratio <= tolerance

    def is_sfw(self) -> bool:
        return not self.sketchy and not self.nsfw


class Source:
    NAME: str = ''
    VERSION: str = '0.0.0'
    ICON: str = 'ico'
    URL: str = ''
    TCONFIG: type[TypedDict] = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_RATINGS: list[bool]}, total=False)
    DEFAULT_CONFIG: TCONFIG = {}
    CURRENT_CONFIG: TCONFIG = {}

    _orientations: bool
    _ratings: bool

    def __init_subclass__(cls, source: bool = True):
        if source:
            uid = cls.__module__.removeprefix(Source.__module__ + '.')
            if not cls.NAME:
                cls.NAME = cls.__name__
            cls.ICON = os.path.join(os.path.dirname(__file__), 'res', f'{uid}.{cls.ICON}')
            tconfig = cls.TCONFIG
            default_config = cls.DEFAULT_CONFIG
            for base in utils.iindex(cls.__mro__[::-1], Source, cls):
                # noinspection PyUnresolvedReferences
                tconfig_ = base.TCONFIG
                tconfig.__required_keys__ |= tconfig_.__required_keys__
                tconfig.__optional_keys__ |= tconfig_.__optional_keys__
                # noinspection PyUnresolvedReferences
                default_config.update(base.DEFAULT_CONFIG)
            cls.CURRENT_CONFIG = {}
            cls._orientations = CONFIG_ORIENTATIONS in cls.DEFAULT_CONFIG
            cls._ratings = CONFIG_RATINGS in cls.DEFAULT_CONFIG
            cls.get_image = callables.LastCacheCallable(cls.get_image)
            SOURCES[uid] = cls

    # noinspection PyShadowingNames
    @classmethod
    @final
    def _fix_config(cls, validator: Callable, key: str, *args, **kwargs) -> bool:
        return validator(cls.CURRENT_CONFIG, cls.DEFAULT_CONFIG, key, *args, **kwargs)

    @classmethod
    def fix_config(cls, saving: bool = False):
        for key in itertools.compress((CONFIG_ORIENTATIONS, CONFIG_RATINGS),
                                      (cls._orientations, cls._ratings)):
            cls._fix_config(validator.ensure_len, key, len(cls.DEFAULT_CONFIG[key]))
            cls._fix_config(validator.ensure_truthy, key, any)

    @classmethod
    @final
    def _text(cls, message: int | str, number: bool = False) -> str:
        return langs.int(message, langs.DEFAULT) if number or isinstance(message, int) else getattr(
            langs.DEFAULT, f'{cls.__module__.split(".", 1)[1].upper()}_{message}')

    @classmethod
    def create_menu(cls):
        if cls._orientations:
            gui.add_submenu_check(cls._text('MENU_ORIENTATIONS'), (cls._text(
                f'ORIENTATION_{orientation}') for orientation in range(
                len(cls.DEFAULT_CONFIG[CONFIG_ORIENTATIONS]))),
                                  (1, None), cls.CURRENT_CONFIG, CONFIG_ORIENTATIONS)
        if cls._ratings:
            gui.add_submenu_check(cls._text('MENU_RATINGS'), (cls._text(
                f'RATING_{rating}') for rating in range(
                len(cls.DEFAULT_CONFIG[CONFIG_RATINGS]))),
                                  (1, None), cls.CURRENT_CONFIG, CONFIG_RATINGS)

    @classmethod
    @final
    def _temp(cls, *paths: str) -> str:
        return os.path.join(tempfile.gettempdir(), consts.NAME,
                            cls.__module__.split(".", 1)[1], *paths)

    @classmethod
    @callables.LastCacheCallable
    def get_image(cls, **params) -> Iterator[Optional[File | ImageFile]]:
        raise NotImplementedError

    @classmethod
    @final
    def _filter_orientations(cls, image: ImageFile, key: str = CONFIG_ORIENTATIONS, *,
                             landscape: bool = True, portrait: bool = True, square: bool = False) -> bool:
        orientations = []
        if landscape:
            orientations.append(image.ratio > 1.0)
        if portrait:
            orientations.append(image.ratio < 1.0)
        if square:
            orientations.append(image.is_square())
        return any(itertools.compress(orientations, cls.CURRENT_CONFIG[key]))

    @classmethod
    @final
    def _filter_ratings(cls, image: ImageFile, key: str = CONFIG_RATINGS, *,
                        sfw: bool = True, sketchy: bool = False, nsfw: bool = True) -> bool:
        ratings = []
        if sfw:
            ratings.append(image.is_sfw())
        if sketchy:
            ratings.append(image.sketchy)
        if nsfw:
            ratings.append(image.nsfw)
        return any(itertools.compress(ratings, cls.CURRENT_CONFIG[key]))

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if cls._orientations and not cls._filter_orientations(image):
            return False
        if cls._ratings and not cls._filter_ratings(image):
            return False
        return True


from . import (
    asiachan,
    backiee,
    besthdwallpaper,
    bing,
    bing_sapphire,
    color,
    deviantart_rss,
    facets,
    fivehundredpx,
    folder,
    fonstola,
    infinitynewtab,
    kekaiart,
    livestartpage,
    lwalpapers,
    pexels,
    pixabay,
    reddit,
    shutterstock,
    simpledesktops,
    spotlight,
    stocksnap,
    thisxdoesnotexist,
    ubuntu,
    unsplash,
    wallha,
    wallhaven,
    wallhere,
    wallpaperabyss,
    wallpaperflare,
    wallpapersmug,
    wallpaperswide,
    wallpapertip,
    wallscloud,
    wallup,
    zerochan,
    gelbooru,
    moebooru)  # NOQA: E402
