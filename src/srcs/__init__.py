from __future__ import annotations as _

__version__ = '0.3.4'

import binascii
import copy
import dataclasses
import fractions
import functools
import hashlib
import itertools
import logging
import os
import tempfile
import urllib.parse
from typing import Any
from typing import Callable
from typing import Container
from typing import Iterator
from typing import Optional
from typing import TypedDict
from typing import final

import consts
import gui
import langs
import validator
import win32
from libs import callables
from libs import files
from libs import mimetype
from libs import request
from libs import utils
from libs.request import har

logger = logging.getLogger(__name__)

SOURCES: dict[str, type[Source]] = {}
CATEGORIES: dict[str, type[Source]] = {}

CONFIG_ORIENTATIONS = '_orientations_'
CONFIG_RATINGS = '_ratings_'

EXT_VIDEO = set(itertools.chain.from_iterable(exts for mime, exts in mimetype.iter_extensions()
                                              if mime.split('/', 1)[0] == 'video'))
EXT_ANIMATED = {'apng', 'avif', 'gif', 'webp'}


class Hash:
    _cache = getattr(hashlib, '__builtin_constructor_cache')

    # noinspection PyShadowingBuiltins
    def __init_subclass__(cls, hash: bool = True):
        if hash:
            cls._cache[cls.name] = cls
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
    request: str | har.TRequest | request.Request
    name: str = ''
    # noinspection PyUnresolvedReferences
    size: int = request.RETRIEVE_UNKNOWN_SIZE
    url: str = dataclasses.field(default='', repr=False)
    md5: Optional[bytes | str] = dataclasses.field(default=None, repr=False, kw_only=True)
    sha1: Optional[bytes | str] = dataclasses.field(default=None, repr=False, kw_only=True)
    sha256: Optional[bytes | str] = dataclasses.field(default=None, repr=False, kw_only=True)
    hashes: dict[str | type[Hash] | Hash, bytes | str] = dataclasses.field(
        default_factory=dict, repr=False, kw_only=True)

    _reduced = functools.cache(callables.ReducedCallable)

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.__hash__ = cls.__hash__
        cls.__eq__ = cls.__eq__

    def __post_init__(self):
        if not isinstance(self.request, request.Request):
            if isinstance(self.request, str):
                self.request = request.Request(request.Method.GET, self.request)
            else:
                self.request = har.decode_request(self.request)
        if self.request.params is not None:
            self.request.url = request.encode_params(
                self.request.url, self.request.params)
            self.request.params = None
        # TODO BasicAuth
        if not self.name:
            self.name = urllib.parse.unquote_plus(
                os.path.basename(request.strip_url(self.request.url)))
        name, ext = os.path.splitext(self.name)
        self.name = utils.shrink_string_mid(win32.sanitize_filename(
            name.strip().removesuffix(ext) + ext), consts.MAX_FILENAME_LEN)
        if not self.url and self.is_simple():
            self.url = self.request.url
        hashes = {}
        for algorithm in hashlib.algorithms_available:
            hash_ = getattr(self, algorithm, None)
            if hash_ is not None:
                self.hashes[algorithm] = hash_
        for algorithm, hash_ in self.hashes.items():
            if not isinstance(algorithm, str):
                algorithm = algorithm.name
            if not isinstance(hash_, bytes):
                hash_ = bytes.fromhex(hash_)
            hashes[algorithm] = hash_
        self.hashes = hashes

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
        try:
            data['request'] = har.decode_request(data['request'])
        except BaseException as exc:
            logger.warning(f'Failed to decode request: %s',
                           data['request'], exc_info=exc)
        else:
            return cls._reduced(cls)(**data)

    def asdict(self) -> dict[str, Any]:
        result = {'request': har.encode_request(self.request), 'name': self.name}
        if self.size != request.RETRIEVE_UNKNOWN_SIZE:
            result['size'] = self.size
        if self.url and self.url != self.request.url and self.is_simple():
            result['url'] = self.url
        hashes = {algorithm: binascii.hexlify(
            hash_).decode() for algorithm, hash_ in self.hashes.items()}
        if hashes:
            result['hashes'] = hashes
        return result

    def checksize(self, path: str) -> Optional[bool]:
        if self.size != request.RETRIEVE_UNKNOWN_SIZE:
            try:
                return self.size == os.path.getsize(path)
            except OSError:
                return False

    def checksum(self, path: str) -> Optional[bool]:
        for algorithm, hash_ in self.hashes.items():
            try:
                return files.checksum(path, hash_, algorithm)
            except OSError:
                return False

    # noinspection PyShadowingBuiltins
    def fill(self, path: str, hash: bool = True) -> bool:
        if self.size == request.RETRIEVE_UNKNOWN_SIZE:
            try:
                self.size = os.path.getsize(path)
            except OSError:
                return False
        if hash and not self.hashes:
            try:
                hash_ = files.get_hash(path)
            except OSError:
                return False
            else:
                self.hashes[hash_.name] = hash_.digest()
        return True

    def is_simple(self) -> bool:
        return (self.request.method == request.Method.GET and
                not self.request.headers and self.request.files is None and
                self.request.data is None and not self.request.params and
                self.request.auth is None and not self.request.cookies and
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

    def is_static(self, includes: Container[str] = (), excludes: Container[str] = ()) -> bool:  # TODO
        ext = files.get_ext(self.name).lower()
        return ext in includes or (ext not in excludes and
                                   ext not in EXT_ANIMATED and
                                   ext not in EXT_VIDEO)

    def is_square(self, tolerance: float = 0.05) -> bool:
        return self.ratio <= tolerance

    def is_sfw(self) -> bool:
        return not self.sketchy and not self.nsfw


class Source:
    NAME: str = ''
    VERSION: str = '0.0.0'
    ICON: str = 'ico'
    URL: str = ''
    URL_API: str = ''
    TCONFIG: type[TypedDict] = TypedDict('TCONFIG', {
        CONFIG_ORIENTATIONS: list[bool],
        CONFIG_RATINGS: list[bool]}, total=False)
    DEFAULT_CONFIG: TCONFIG = {}
    CURRENT_CONFIG: TCONFIG = {}

    _orientations: bool
    _ratings: bool

    def __init_subclass__(cls, source: bool = True):
        uid = cls.__module__.removeprefix(Source.__module__ + '.')
        if source:
            if cls.NAME == cls.__base__.NAME:
                cls.NAME = cls.__name__
            cls.ICON = os.path.join(os.path.dirname(
                __file__), 'res', f'{uid}.{cls.ICON}')
            if not cls.URL_API:
                cls.URL_API = cls.URL
            bases = cls.__mro__
            tconfig = cls.TCONFIG
            default_config = cls.DEFAULT_CONFIG
            for base in bases[bases.index(Source)::-1]:
                tconfig_ = base.TCONFIG
                tconfig.__required_keys__ |= tconfig_.__required_keys__
                tconfig.__optional_keys__ |= tconfig_.__optional_keys__
                default_config.update(base.DEFAULT_CONFIG)
            cls.CURRENT_CONFIG = {}
            cls._orientations = CONFIG_ORIENTATIONS in cls.DEFAULT_CONFIG
            cls._ratings = CONFIG_RATINGS in cls.DEFAULT_CONFIG
            cls.get_image = callables.LastCacheCallable(cls.get_image)
            SOURCES[uid] = cls
        else:
            if cls.NAME == cls.__base__.NAME:
                cls.NAME = cls.__name__.removesuffix(Source.__name__)
            CATEGORIES[uid] = cls

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
                            cls.__module__.split('.', 1)[1], *paths)

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
    heytap,
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
