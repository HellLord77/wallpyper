from __future__ import annotations as _

__version__ = '0.0.3'

import itertools
import logging
import os
from typing import Optional

from libs import ctyped
from libs.ctyped.const import brotli as const_brotli
from libs.ctyped.enum import brotli as enum_brotli
from libs.ctyped.lib import brotlidec
from libs.ctyped.lib import brotlienc

logger = logging.getLogger(__name__)

_BLOCK_SIZES = tuple(size * 1024 for size in (
    32, 64, 256, 1 * 1024, 4 * 1024, 8 * 1024, *(16 * 1024,) * 2,
    *(32 * 1024,) * 2, *(64 * 1024,) * 2, *(128 * 1024,) * 2, 256 * 1024))
_PTR = ctyped.pointer(ctyped.type.uint8_t)
_ALLOC = ctyped.type.brotli_alloc_func()
_FREE = ctyped.type.brotli_free_func()


class Error(Exception):
    def __init__(self, message: str, code: Optional[enum_brotli.BrotliDecoderResult]):
        super().__init__(message)
        self.code = code


class DecompressionError(Error):
    def __init__(self, code: enum_brotli.BrotliDecoderResult):
        super().__init__(f'Error during decompression [{code.name}]', code)


class CompressionError(Error):
    def __init__(self):
        super().__init__('Error during compression', None)


def _version(version: int) -> tuple[int, int, int]:
    return version >> 24, (version >> 12) & 0xFFF, version & 0xFFF


class _Brotli(type):
    _obj: Optional[ctyped.Pointer[ctyped.struct.BrotliDecoderState] |
                   ctyped.Pointer[ctyped.struct.BrotliEncoderState]] = None

    def __bool__(self):
        try:
            self.get_version()
        except BaseException as exc:
            logger.warning(f'Failed loading brotli: %s',
                           self.__name__, exc_info=exc)
            return False
        else:
            return True

    @staticmethod
    def get_version() -> tuple[int, int, int]:
        raise NotImplementedError


class Decompressor(metaclass=_Brotli):
    def __init__(self):
        self._obj = brotlidec.BrotliDecoderCreateInstance(_ALLOC, _FREE, None)
        self.unused_data = b''

    def __del__(self):
        if self:
            brotlidec.BrotliDecoderDestroyInstance(self._obj)
            self._obj = None

    def __bool__(self):
        return bool(self._obj)

    def __enter__(self) -> Decompressor:
        return self

    def __exit__(self, _, __, ___):
        self.__del__()

    def decompress(self, data: bytes) -> bytes:
        ret = b''
        with ctyped.py_buffer(data) as buff_in:
            available = ctyped.type.c_size_t(buff_in.len)
            available_in = ctyped.byref(available)
            next_in = ctyped.cast(ctyped.type.c_void_p(buff_in.buf), _PTR)
            sizes = iter(_BLOCK_SIZES)
            size = next(sizes)
            available_out = ctyped.type.c_size_t(size)
            buff_out = ctyped.array(type=ctyped.type.uint8_t, size=size)
            while True:
                result = brotlidec.BrotliDecoderDecompressStream(
                    self._obj, available_in, next_in, ctyped.byref(
                        available_out), ctyped.cast(buff_out, _PTR), ctyped.Pointer.NULL)
                # noinspection PyTypeChecker
                ret += bytes(itertools.islice(buff_out, None, size - available_out.value))
                if result == enum_brotli.BrotliDecoderResult.NEEDS_MORE_OUTPUT:
                    if not available_out:
                        size = available_out.value = next(sizes, _BLOCK_SIZES[-1])
                        buff_out = ctyped.array(type=ctyped.type.uint8_t, size=size)
                    continue
                break
        self.unused_data = data[-available.value:]
        if result == enum_brotli.BrotliDecoderResult.ERROR or available:
            raise DecompressionError(result)
        return ret

    def has_more_output(self) -> bool:
        return bool(brotlidec.BrotliDecoderHasMoreOutput(self._obj))

    def is_used(self) -> bool:
        return bool(brotlidec.BrotliDecoderIsUsed(self._obj))

    def is_finished(self) -> bool:
        return bool(brotlidec.BrotliDecoderIsFinished(self._obj))

    def get_error_code(self) -> enum_brotli.BrotliDecoderErrorCode:
        return brotlidec.BrotliDecoderGetErrorCode(self._obj)

    @staticmethod
    def get_error_string(error_code: enum_brotli.BrotliDecoderErrorCode) -> str:
        return brotlidec.BrotliDecoderErrorString(error_code).decode()

    @staticmethod
    def get_version() -> tuple[int, int, int]:
        return _version(brotlidec.BrotliDecoderVersion())


class TextDecompressor(Decompressor):
    def decompress(self, data: bytes) -> str:
        return super().decompress(data).decode()


class _Compressor(metaclass=_Brotli):
    def __init__(self, mode: Optional[enum_brotli.BrotliEncoderMode] = None, quality: Optional[int] = None,
                 lgwin: Optional[int] = None, lgblock: Optional[int] = None):
        self._obj = brotlienc.BrotliEncoderCreateInstance(_ALLOC, _FREE, None)
        if mode is not None:
            self._set_mode(mode)
        if quality is not None:
            self.set_quality(quality)
        if lgwin is not None:
            self.set_lgwin(lgwin)
        if lgblock is not None:
            self.set_lgblock(lgblock)

    def __del__(self):
        if self:
            brotlienc.BrotliEncoderDestroyInstance(self._obj)
            self._obj = None

    def __bool__(self):
        return bool(self._obj)

    def __enter__(self) -> _Compressor:
        return self

    def __exit__(self, _, __, ___):
        self.__del__()

    def _set_parameter(self, param: enum_brotli.BrotliEncoderParameter, value: int) -> bool:
        return bool(brotlienc.BrotliEncoderSetParameter(self._obj, param, value))

    def _set_mode(self, mode: enum_brotli.BrotliEncoderMode) -> bool:
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.MODE, mode.value)

    def set_quality(self, quality: int) -> bool:
        assert const_brotli.BROTLI_MIN_QUALITY <= quality <= const_brotli.BROTLI_MAX_QUALITY
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.QUALITY, quality)

    def set_lgwin(self, lgwin: int) -> bool:
        assert const_brotli.BROTLI_MIN_WINDOW_BITS <= lgwin <= const_brotli.BROTLI_MAX_WINDOW_BITS
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.LGWIN, lgwin)

    def set_lgblock(self, lgblock: int) -> bool:
        assert lgblock == 0 or const_brotli.BROTLI_MIN_INPUT_BLOCK_BITS <= lgblock <= const_brotli.BROTLI_MAX_INPUT_BLOCK_BITS
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.LGBLOCK, lgblock)

    def set_size_hint(self, size_hint: int) -> bool:
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.SIZE_HINT, size_hint)

    def set_large_window(self, large_window: bool) -> bool:
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.LARGE_WINDOW, large_window)

    def set_npostfix(self, npostfix: int) -> bool:
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.NPOSTFIX, npostfix)

    def set_ndirect(self, ndirect: int) -> bool:
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.NDIRECT, ndirect)

    def set_stream_offset(self, stream_offset: int) -> bool:
        return self._set_parameter(enum_brotli.BrotliEncoderParameter.STREAM_OFFSET, stream_offset)

    @staticmethod
    def get_max_compressed_size(input_size: int) -> int:
        return brotlienc.BrotliEncoderMaxCompressedSize(input_size)

    def _process(self, data: bytes, operation: enum_brotli.BrotliEncoderOperation) -> bytes:
        ret = b''
        with ctyped.py_buffer(data) as buff_in:
            available = ctyped.type.c_size_t(buff_in.len)
            available_in = ctyped.byref(available)
            next_in = ctyped.cast(ctyped.type.c_void_p(buff_in.buf), _PTR)
            sizes = iter(_BLOCK_SIZES)
            size_out = next(sizes)
            available_out = ctyped.type.c_size_t(size_out)
            buff_out = ctyped.array(type=ctyped.type.uint8_t, size=size_out)
            while True:
                if not brotlienc.BrotliEncoderCompressStream(
                        self._obj, operation, available_in, next_in, ctyped.byref(
                            available_out), ctyped.cast(buff_out, _PTR), ctyped.Pointer.NULL):
                    raise CompressionError()
                # noinspection PyTypeChecker
                ret += bytes(itertools.islice(buff_out, None, size_out - available_out.value))
                if available or self.has_more_output():
                    if not available_out:
                        size_out = available_out.value = next(sizes, _BLOCK_SIZES[-1])
                        buff_out = ctyped.array(type=ctyped.type.uint8_t, size=size_out)
                    continue
                break
        return ret

    def compress(self, data: bytes) -> bytes:
        return self._process(data, enum_brotli.BrotliEncoderOperation.PROCESS)

    def flush(self, data: bytes = b'') -> bytes:
        return self._process(data, enum_brotli.BrotliEncoderOperation.FLUSH)

    def finish(self, data: bytes = b'') -> bytes:
        return self._process(data, enum_brotli.BrotliEncoderOperation.FINISH)

    def emit_metadata(self, data: bytes = b'') -> bytes:
        return self._process(data, enum_brotli.BrotliEncoderOperation.EMIT_METADATA)

    def is_finished(self) -> bool:
        return bool(brotlienc.BrotliEncoderIsFinished(self._obj))

    def has_more_output(self) -> bool:
        return bool(brotlienc.BrotliEncoderHasMoreOutput(self._obj))

    @staticmethod
    def get_version() -> tuple[int, int, int]:
        return _version(brotlienc.BrotliEncoderVersion())


class Compressor(_Compressor):
    def __init__(self, quality: Optional[int] = None,
                 lgwin: Optional[int] = None, lgblock: Optional[int] = None):
        super().__init__(enum_brotli.BrotliEncoderMode.GENERIC, quality, lgwin, lgblock)


class TextCompressor(_Compressor):
    def __init__(self, quality: Optional[int] = None,
                 lgwin: Optional[int] = None, lgblock: Optional[int] = None):
        super().__init__(enum_brotli.BrotliEncoderMode.TEXT, quality, lgwin, lgblock)

    def compress(self, data: str) -> bytes:
        return super().compress(data.encode())

    def flush(self, data: str = '') -> bytes:
        return super().flush(data.encode())

    def finish(self, data: str = '') -> bytes:
        return super().finish(data.encode())

    def emit_metadata(self, data: str = '') -> bytes:
        return super().emit_metadata(data.encode())


class FontCompressor(_Compressor):
    def __init__(self, quality: Optional[int] = None,
                 lgwin: Optional[int] = None, lgblock: Optional[int] = None):
        super().__init__(enum_brotli.BrotliEncoderMode.FONT, quality, lgwin, lgblock)


def decompress(data: bytes) -> bytes:
    with Decompressor() as decompressor:
        ret = decompressor.decompress(data)
        if (error_code := decompressor.get_error_code()) != enum_brotli.BrotliDecoderErrorCode.SUCCESS:
            raise DecompressionError(enum_brotli.BrotliDecoderResult(error_code.value))
        return ret


def decompress_known(data: bytes, max_length: Optional[int] = None) -> bytes:
    if max_length is None:
        for size in _BLOCK_SIZES:
            if _Compressor.get_max_compressed_size(size) >= len(data):
                max_length = size
                break
    ret = b''
    with ctyped.py_buffer(data) as buff_in:
        decoded_size = ctyped.type.c_size_t(max_length)
        decoded_buffer = ctyped.array(type=ctyped.type.uint8_t, size=max_length)
        result = brotlidec.BrotliDecoderDecompress(
            buff_in.len, ctyped.byref(ctyped.type.uint8_t.from_address(
                buff_in.buf)), ctyped.byref(decoded_size), decoded_buffer)
        # noinspection PyTypeChecker
        ret += bytes(itertools.islice(decoded_buffer, None, decoded_size.value))
    if result != enum_brotli.BrotliDecoderResult.SUCCESS:
        raise DecompressionError(result)
    return ret


def compress(data: bytes | str) -> bytes:
    with (TextCompressor if isinstance(data, str) else Compressor)() as compressor:
        return compressor.compress(data) + compressor.finish()


def compress_known(data: bytes | str, max_length: Optional[int] = None,
                   quality: int = const_brotli.BROTLI_DEFAULT_QUALITY,
                   lgwin: int = const_brotli.BROTLI_DEFAULT_WINDOW,
                   mode: Optional[enum_brotli.BrotliEncoderMode] = None) -> bytes:
    if text := isinstance(data, str):
        data = data.encode()
    if mode is None:
        mode = enum_brotli.BrotliEncoderMode.TEXT if text else enum_brotli.BrotliEncoderMode.GENERIC
    if max_length is None:
        max_length = _Compressor.get_max_compressed_size(len(data))
    ret = b''
    with ctyped.py_buffer(data) as buff_in:
        encoded_size = ctyped.type.c_size_t(max_length)
        encoded_buffer = ctyped.array(type=ctyped.type.uint8_t, size=max_length)
        if not brotlienc.BrotliEncoderCompress(
                quality, lgwin, mode, buff_in.len, ctyped.byref(ctyped.type.uint8_t.from_address(
                    buff_in.buf)), ctyped.byref(encoded_size), encoded_buffer):
            raise CompressionError()
        # noinspection PyTypeChecker
        ret += bytes(itertools.islice(encoded_buffer, None, encoded_size.value))
    return ret


ctyped.lib.add_path(os.path.join(os.path.dirname(__file__)))
