from __future__ import annotations

__version__ = '0.2.5'

import binascii
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
import langs
import win32
from libs import callables, files, request, utils

KEY: Optional[bytes | str] = None
SOURCES: dict[str, type[Source]] = {}

CONFIG_ORIENTATIONS = '_orientations_'
CONFIG_RATINGS = '_ratings_'

_reduced = functools.cache(callables.ReducedCallable)


@dataclasses.dataclass
class File:
    request: str | request.Request
    name: str = ''
    # noinspection PyUnresolvedReferences
    size: int = request.RETRIEVE_UNKNOWN_SIZE
    url: Optional[str] = dataclasses.field(default=None, repr=False)
    sha256: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)
    md5: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)

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
        self.name = utils.shrink_string_mid(
            win32.sanitize_filename(self.name), consts.MAX_FILENAME_LEN)
        if self.url is None and self.is_simple():
            self.url = self.request.url
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
        request_ = utils.decrypt(data.pop('request'), KEY)
        if request_ is not utils.DEFAULT:
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
        for algorithm, hash_ in self._iter_hashes(True):
            result[algorithm] = binascii.hexlify(hash_).decode()
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
        for algorithm, _ in self._iter_hashes(True):
            result[algorithm] = result.pop(algorithm)
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
        return os.path.splitext(self.name)[1].lower() in ('.gif', '.webp')

    def is_square(self, tolerance: float = 0.05) -> bool:
        return self.ratio <= tolerance

    def is_sfw(self) -> bool:
        return not self.sketchy and not self.nsfw


class Source:
    NAME: str = ''
    VERSION: str = '0.0.0'
    ICON: str = 'ico'
    URL: Optional[str] = None
    TCONFIG: type[TypedDict] = TypedDict('TCONFIG', {})
    DEFAULT_CONFIG: TCONFIG = {}
    CURRENT_CONFIG: TCONFIG = {}

    def __init_subclass__(cls):
        uid = cls.__module__.split('.')[-1]
        if not cls.NAME:
            cls.NAME = cls.__name__
        cls.ICON = os.path.join(os.path.dirname(__file__), 'res', f'{uid}.{cls.ICON}')
        cls.CURRENT_CONFIG = {}
        cls.get_image = callables.LastCacheCallable(cls.get_image)
        SOURCES[uid] = cls

    @classmethod
    @final
    def _fix_config(cls, validator: Callable, key: str, *args, **kwargs) -> bool:
        return validator(cls.CURRENT_CONFIG, cls.DEFAULT_CONFIG, key, *args, **kwargs)

    @classmethod
    def fix_config(cls, saving: bool = False):
        pass

    @classmethod
    @final
    def _text(cls, message: int | str, number: bool = False) -> str:
        return langs.int(message, langs.DEFAULT) if number or isinstance(message, int) else getattr(
            langs.DEFAULT, f'{cls.__module__.split(".", 1)[1].upper()}_{message}')

    @classmethod
    def create_menu(cls):
        pass

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
        # noinspection PyTypedDict
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
        # noinspection PyTypedDict
        return any(itertools.compress(ratings, cls.CURRENT_CONFIG[key]))

    @classmethod
    def filter_image(cls, image: ImageFile) -> bool:
        if CONFIG_ORIENTATIONS in cls.DEFAULT_CONFIG and not cls._filter_orientations(image):
            return False
        if CONFIG_RATINGS in cls.DEFAULT_CONFIG and not cls._filter_ratings(image):
            return False
        return True


from . import (
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
    yandere,
    zerochan)  # NOQA: E402
