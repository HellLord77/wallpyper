from __future__ import annotations

__version__ = '0.2.1'

import binascii
import dataclasses
import hashlib
import os
import urllib.parse
from typing import Any, Callable, Iterator, Optional, TypedDict, final

import consts
import langs
import win32
from libs import callables, files, request, utils

KEY: Optional[bytes | str] = None
SOURCES: dict[str, type[Source]] = {}


@dataclasses.dataclass
class File:
    request: str | request.Request
    name: str = ''
    size: int = 0
    sha256: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)
    md5: bytes | str = dataclasses.field(default=b'', repr=False, kw_only=True)

    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.__hash__ = cls.__hash__
        cls.__eq__ = cls.__eq__

    def __post_init__(self):
        if isinstance(self.request, str):
            self.request = request.Request(request.Method.GET, self.request)
        if not self.name:
            self.name = urllib.parse.unquote_plus(
                os.path.basename(request.strip_url(self.request.url)))
        self.name = utils.shrink_string_mid(
            win32.sanitize_filename(self.name), consts.MAX_FILENAME_LEN)
        if not self.size:
            self.size = request.sizeof(self.request)
        for algorithm, hash_ in self._iter_hashes():
            if not isinstance(hash_, bytes):
                setattr(self, algorithm, bytes.fromhex(hash_))

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return repr(self).replace(f'request={self.request!r}', f'url={self.request.url}', 1).replace(
            f'size={self.size}', f'size={files.Size(self.size)}' if self.size else '', 1)

    def __eq__(self, other):
        if isinstance(other, File):
            return self.name == other.name
        return NotImplemented

    @classmethod
    def fromdict(cls, data: dict[str, Any]) -> Optional[File]:
        request_ = utils.decrypt(data.pop('request'), KEY)
        if request_ is not utils.DEFAULT:
            return callables.ReducedCallable(cls)(request_, **data)

    def _iter_hashes(self, filled: bool = False) -> Iterator[tuple[str, bytes | str]]:
        for algorithm in hashlib.algorithms_available:
            hash_ = getattr(self, algorithm, None)
            if hash_ is not None and (not filled or hash_):
                yield algorithm, hash_

    def asdict(self) -> dict[str, Any]:
        result: dict = {'request': utils.encrypt(
            self.request, KEY, as_string=True), 'name': self.name}
        if self.size:
            result['size'] = self.size
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
                break
        return False

    def fill(self, path: str) -> bool:
        if not self.size:
            try:
                self.size = os.path.getsize(path)
            except OSError:
                return False
        if not any(self._iter_hashes(True)):
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
        return (self.request.headers is None and self.request.files is None and
                self.request.data is None and self.request.params is None and
                self.request.auth is None and self.request.cookies is None and
                self.request.json is None and self.request.unredirected_hdrs is None)

    def get_url(self) -> str:  # TODO BasicAuth
        return request.encode_params(self.request.url, self.request.params)


@dataclasses.dataclass
class ImageFile(File):
    width: int = 0
    height: int = 0
    sketchy: bool = False
    nsfw: bool = False

    def asdict(self) -> dict[str, Any]:
        result = super().asdict()
        if self.width:
            result['width'] = self.width
        if self.height:
            result['height'] = self.height
        if self.sketchy:
            result['sketchy'] = self.sketchy
        if self.nsfw:
            result['nsfw'] = self.nsfw
        for algorithm, _ in self._iter_hashes(True):
            result[algorithm] = result.pop(algorithm)
        return result

    def is_animated(self) -> bool:  # TODO
        return os.path.splitext(self.name)[1].lower() in ('.gif', '.webp')

    def is_portrait(self) -> bool:
        return self.width < self.height

    def is_landscape(self) -> bool:
        return self.width > self.height

    def is_sfw(self) -> bool:
        return not self.sketchy and not self.nsfw


class Source:
    NAME: str = ''
    VERSION: str = '0.0.0'
    ICON: str = 'ico'
    URL: str = ''
    TCONFIG: type[dict] | type[TypedDict] = dict[str, Any]
    DEFAULT_CONFIG: TCONFIG = None
    CURRENT_CONFIG: TCONFIG = None

    def __init_subclass__(cls):
        uid = cls.__module__.split('.')[-1]
        if not cls.NAME:
            cls.NAME = cls.__name__
        cls.ICON = os.path.join(os.path.dirname(__file__), 'res', f'{uid}.{cls.ICON}')
        if cls.DEFAULT_CONFIG is None:
            cls.DEFAULT_CONFIG = {}
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
    def _text(cls, message: int | str) -> str:
        return langs.to_str(message, langs.DEFAULT) if isinstance(message, int) else getattr(
            langs.DEFAULT, f'{cls.__module__.split(".", 1)[1].upper()}_{message}')

    @classmethod
    def create_menu(cls):
        pass

    @classmethod
    @callables.LastCacheCallable
    def get_image(cls, **params) -> Iterator[Optional[File]]:
        raise NotImplementedError

    @classmethod
    def filter_image(cls, image: File) -> bool:
        return True


from . import (
    bing,
    doesnotexist,
    facets,
    fivehundredpx_legacy,
    folder_local,
    pexels,
    pixabay,
    reddit,
    shutterstock,
    simpledesktops,
    spotlight,
    stocksnap,
    unsplash,
    wallhaven,
    wallhere,
    wallpaperabyss,
    wallpaperflare,
    wallpapersmug,
    yandere,
    zerochan)  # NOQA: E402
