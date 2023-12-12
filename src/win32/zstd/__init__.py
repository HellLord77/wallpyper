from __future__ import annotations as _

__version__ = '0.0.2'

import itertools
import logging
import os
from typing import Optional

from libs import ctyped
from libs.ctyped.const import zstd as const_zstd
from libs.ctyped.enum import zstd as enum_zstd
from libs.ctyped.lib import libzstd

logger = logging.getLogger(__name__)

FLAG_STRICT = True


class Error(Exception):
    def __init__(self, code: int, message_fmt: str = 'Error during operation: {}<{}>'):
        super().__init__(message_fmt.format(self.get_name(code), code))
        self.code = code

    @classmethod
    def check(cls, code: int, strict: Optional[bool] = None) -> bool:
        if strict is None:
            strict = FLAG_STRICT
        is_error = libzstd.ZSTD_isError(code)
        if strict and is_error:
            raise cls(code)
        else:
            return is_error

    @staticmethod
    def get_name(code: int) -> str:
        return libzstd.ZSTD_getErrorName(code).decode()


class DecompressionError(Error):
    def __init__(self, code: int):
        super().__init__(code, 'Error during decompression: {}<{}>')


class CompressionError(Error):
    def __init__(self, code: int):
        super().__init__(code, 'Error during compression: {}<{}>')


def get_version() -> tuple[int, int, int]:
    version = libzstd.ZSTD_versionNumber()
    return version // 10000, (version // 100) % 100, version % 100


class _Zstd(type):
    _obj: Optional[ctyped.Pointer[ctyped.struct.ZSTD_DCtx] |
                   ctyped.Pointer[ctyped.struct.ZSTD_CCtx]] = None

    def __bool__(self):
        try:
            get_version()
        except BaseException as exc:
            logger.warning(f'Failed loading zstd: %s',
                           self.__name__, exc_info=exc)
            return False
        else:
            return True


class Decompressor(metaclass=_Zstd):
    def __init__(self, window_log_max: Optional[int] = None, custom_mem: Optional[ctyped.struct.ZSTD_customMem] = None):
        self._obj = libzstd.ZSTD_createDCtx() if custom_mem is None else libzstd.ZSTD_createDCtx_advanced(custom_mem)
        if window_log_max is not None:
            self.window_log_max = window_log_max
        self.unused_data = b''

    def __del__(self):
        if self:
            libzstd.ZSTD_freeDCtx(self._obj)
            self._obj = None

    def __bool__(self):
        return bool(self._obj)

    def __enter__(self) -> Decompressor:
        return self

    def __exit__(self, _, __, ___):
        self.__del__()

    def _set_parameter(self, parameter: enum_zstd.ZSTD_dParameter, value: int) -> bool:
        return not Error.check(libzstd.ZSTD_DCtx_setParameter(self._obj, parameter, value))

    def _get_parameter(self, parameter: enum_zstd.ZSTD_dParameter) -> Optional[int]:
        value = ctyped.type.c_int()
        if not Error.check(libzstd.ZSTD_DCtx_getParameter(self._obj, parameter, ctyped.byref(value))):
            return value.value

    @property
    def window_log_max(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_dParameter.windowLogMax)

    @window_log_max.setter
    def window_log_max(self, value: int):
        self._set_parameter(enum_zstd.ZSTD_dParameter.windowLogMax, value)

    @property
    def memory_size(self) -> int:
        return libzstd.ZSTD_sizeof_DCtx(self._obj)

    @staticmethod
    def get_size_in() -> int:
        return libzstd.ZSTD_DStreamInSize()

    @staticmethod
    def get_size_out() -> int:
        return libzstd.ZSTD_DStreamOutSize()

    def decompress(self, data: bytes) -> bytes:
        ret = b''
        with ctyped.py_buffer(data) as buff_in:
            src = ctyped.struct.ZSTD_inBuffer(buff_in.buf, buff_in.len)
            ref_src = ctyped.byref(src)
            size_dst = self.get_size_out()
            buff_out = ctyped.array(type=ctyped.type.c_uchar, size=size_dst)
            dst = ctyped.struct.ZSTD_outBuffer(ctyped.addressof(buff_out), size_dst)
            ref_dst = ctyped.byref(dst)
            last_src_pos = 0
            while src.pos != src.size:
                try:
                    DecompressionError.check(libzstd.ZSTD_decompressStream(
                        self._obj, ref_dst, ref_src), True)
                except DecompressionError as exc:
                    if 'Unknown frame descriptor' in str(exc):
                        self.unused_data = data[last_src_pos:]
                    raise
                last_src_pos = src.pos
                # noinspection PyTypeChecker
                ret += bytes(itertools.islice(buff_out, None, dst.pos))
                dst.pos = 0
        return ret

    def reset(self, session: bool = True, parameters: bool = False) -> bool:
        if session and parameters:
            reset = enum_zstd.ZSTD_ResetDirective.session_and_parameters
        elif session:
            reset = enum_zstd.ZSTD_ResetDirective.session_only
        elif parameters:
            reset = enum_zstd.ZSTD_ResetDirective.parameters_only
        else:
            return True
        return not Error.check(libzstd.ZSTD_DCtx_reset(self._obj, reset))


class Compressor(metaclass=_Zstd):
    def __init__(self, level: Optional[int] = None, content_size: Optional[bool] = None,
                 checksum: Optional[bool] = None, custom_mem: Optional[ctyped.struct.ZSTD_customMem] = None):
        self._obj = libzstd.ZSTD_createCCtx() if custom_mem is None else libzstd.ZSTD_createCCtx_advanced(custom_mem)
        if level is not None:
            self.compression_level = level
        if content_size is not None:
            self.content_size_flag = content_size
        if checksum is not None:
            self.checksum_flag = checksum

    def __del__(self):
        if self:
            libzstd.ZSTD_freeCCtx(self._obj)
            self._obj = None

    def __bool__(self):
        return bool(self._obj)

    def __enter__(self) -> Compressor:
        return self

    def __exit__(self, _, __, ___):
        self.__del__()

    def _set_parameter(self, parameter: enum_zstd.ZSTD_cParameter, value: int) -> bool:
        return not Error.check(libzstd.ZSTD_CCtx_setParameter(self._obj, parameter, value))

    def _get_parameter(self, parameter: enum_zstd.ZSTD_cParameter) -> Optional[int]:
        value = ctyped.type.c_int()
        if not Error.check(libzstd.ZSTD_CCtx_getParameter(self._obj, parameter, ctyped.byref(value))):
            return value.value

    @property
    def compression_level(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.compressionLevel)

    @compression_level.setter
    def compression_level(self, value: int):
        self._set_parameter(enum_zstd.ZSTD_cParameter.compressionLevel, value)

    @property
    def window_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.windowLog)

    @window_log.setter
    def window_log(self, value: int):
        assert const_zstd.ZSTD_WINDOWLOG_MIN <= value <= const_zstd.ZSTD_WINDOWLOG_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.windowLog, value)

    @property
    def hash_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.hashLog)

    @hash_log.setter
    def hash_log(self, value: int):
        assert const_zstd.ZSTD_HASHLOG_MIN <= value <= const_zstd.ZSTD_HASHLOG_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.hashLog, value)

    @property
    def chain_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.chainLog)

    @chain_log.setter
    def chain_log(self, value: int):
        assert const_zstd.ZSTD_CHAINLOG_MIN <= value <= const_zstd.ZSTD_CHAINLOG_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.chainLog, value)

    @property
    def search_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.searchLog)

    @search_log.setter
    def search_log(self, value: int):
        assert const_zstd.ZSTD_SEARCHLOG_MIN <= value <= const_zstd.ZSTD_SEARCHLOG_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.searchLog, value)

    @property
    def min_match(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.minMatch)

    @min_match.setter
    def min_match(self, value: int):
        assert const_zstd.ZSTD_MINMATCH_MIN <= value <= const_zstd.ZSTD_MINMATCH_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.minMatch, value)

    @property
    def target_length(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.targetLength)

    @target_length.setter
    def target_length(self, value: int):
        assert const_zstd.ZSTD_TARGETLENGTH_MIN <= value <= const_zstd.ZSTD_TARGETLENGTH_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.targetLength, value)

    @property
    def strategy(self) -> Optional[enum_zstd.ZSTD_strategy]:
        strategy = self._get_parameter(enum_zstd.ZSTD_cParameter.strategy)
        if strategy is not None:
            strategy = enum_zstd.ZSTD_strategy(strategy)
        return strategy

    @strategy.setter
    def strategy(self, value: int | enum_zstd.ZSTD_strategy):
        assert const_zstd.ZSTD_STRATEGY_MIN <= value <= const_zstd.ZSTD_STRATEGY_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.strategy, int(value))

    @property
    def enable_long_distance_matching(self) -> Optional[bool]:
        return bool(self._get_parameter(enum_zstd.ZSTD_cParameter.ldmFlag))

    @enable_long_distance_matching.setter
    def enable_long_distance_matching(self, value: bool):
        self._set_parameter(enum_zstd.ZSTD_cParameter.ldmFlag, int(value))

    @property
    def ldm_hash_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.ldmHashLog)

    @ldm_hash_log.setter
    def ldm_hash_log(self, value: int):
        assert const_zstd.ZSTD_LDM_HASHLOG_MIN <= value <= const_zstd.ZSTD_LDM_HASHLOG_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.ldmHashLog, value)

    @property
    def ldm_min_match(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.ldmMinMatch)

    @ldm_min_match.setter
    def ldm_min_match(self, value: int):
        assert const_zstd.ZSTD_LDM_MINMATCH_MIN <= value <= const_zstd.ZSTD_LDM_MINMATCH_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.ldmMinMatch, value)

    @property
    def ldm_bucket_size_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.ldmBucketSizeLog)

    @ldm_bucket_size_log.setter
    def ldm_bucket_size_log(self, value: int):
        assert const_zstd.ZSTD_LDM_BUCKETSIZELOG_MIN <= value <= const_zstd.ZSTD_LDM_BUCKETSIZELOG_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.ldmBucketSizeLog, value)

    @property
    def ldm_hash_rate_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.ldmHashRateLog)

    @ldm_hash_rate_log.setter
    def ldm_hash_rate_log(self, value: int):
        assert const_zstd.ZSTD_LDM_HASHRATELOG_MIN <= value <= const_zstd.ZSTD_LDM_HASHRATELOG_MAX
        self._set_parameter(enum_zstd.ZSTD_cParameter.ldmHashRateLog, value)

    @property
    def content_size_flag(self) -> Optional[bool]:
        return bool(self._get_parameter(enum_zstd.ZSTD_cParameter.contentSizeFlag))

    @content_size_flag.setter
    def content_size_flag(self, value: bool):
        self._set_parameter(enum_zstd.ZSTD_cParameter.contentSizeFlag, int(value))

    @property
    def checksum_flag(self) -> Optional[bool]:
        return bool(self._get_parameter(enum_zstd.ZSTD_cParameter.checksumFlag))

    @checksum_flag.setter
    def checksum_flag(self, value: bool):
        self._set_parameter(enum_zstd.ZSTD_cParameter.checksumFlag, int(value))

    @property
    def dict_id_flag(self) -> Optional[bool]:
        return bool(self._get_parameter(enum_zstd.ZSTD_cParameter.dictIDFlag))

    @dict_id_flag.setter
    def dict_id_flag(self, value: bool):
        self._set_parameter(enum_zstd.ZSTD_cParameter.dictIDFlag, int(value))

    @property
    def nb_workers(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.nbWorkers)

    @nb_workers.setter
    def nb_workers(self, value: int):
        self._set_parameter(enum_zstd.ZSTD_cParameter.nbWorkers, value)

    @property
    def job_size(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.jobSize)

    @job_size.setter
    def job_size(self, value: int):
        self._set_parameter(enum_zstd.ZSTD_cParameter.jobSize, value)

    @property
    def overlap_size_log(self) -> Optional[int]:
        return self._get_parameter(enum_zstd.ZSTD_cParameter.overlapLog)

    @overlap_size_log.setter
    def overlap_size_log(self, value: int):
        self._set_parameter(enum_zstd.ZSTD_cParameter.overlapLog, value)

    @property
    def memory_size(self) -> int:
        return libzstd.ZSTD_sizeof_CCtx(self._obj)

    @staticmethod
    def get_size_in() -> int:
        return libzstd.ZSTD_CStreamInSize()

    @staticmethod
    def get_size_out() -> int:
        return libzstd.ZSTD_CStreamOutSize()

    def _process(self, data: bytes, operation: enum_zstd.ZSTD_EndDirective) -> bytes:
        ret = b''
        with ctyped.py_buffer(data) as buff_in:
            src = ctyped.struct.ZSTD_inBuffer(buff_in.buf, buff_in.len)
            ref_src = ctyped.byref(src)
            size_dst = self.get_size_out()
            buff_out = ctyped.array(type=ctyped.type.c_uchar, size=size_dst)
            dst = ctyped.struct.ZSTD_outBuffer(ctyped.addressof(buff_out), size_dst)
            ref_dst = ctyped.byref(dst)
            while src.pos != src.size:
                CompressionError.check(libzstd.ZSTD_compressStream2(
                    self._obj, ref_dst, ref_src, operation), True)
                # noinspection PyTypeChecker
                ret += bytes(itertools.islice(buff_out, None, dst.pos))
                dst.pos = 0
        return ret

    def compress(self, data: bytes) -> bytes:
        return self._process(data, enum_zstd.ZSTD_EndDirective.continue_)

    def flush(self, data: bytes = b'') -> bytes:
        return self._process(data, enum_zstd.ZSTD_EndDirective.flush)

    def end(self, data: bytes = b'') -> bytes:
        return self._process(data, enum_zstd.ZSTD_EndDirective.end)

    def reset(self, session: bool = True, parameters: bool = False) -> bool:
        if session and parameters:
            reset = enum_zstd.ZSTD_ResetDirective.session_and_parameters
        elif session:
            reset = enum_zstd.ZSTD_ResetDirective.session_only
        elif parameters:
            reset = enum_zstd.ZSTD_ResetDirective.parameters_only
        else:
            return True
        return not Error.check(libzstd.ZSTD_CCtx_reset(self._obj, reset))


def decompress(data: bytes, window_log_max: int = const_zstd.ZSTD_WINDOWLOG_LIMIT_DEFAULT) -> bytes:
    with Decompressor(window_log_max) as decompressor:
        return decompressor.decompress(data)


def decompress_known(data: bytes) -> bytes:
    with ctyped.py_buffer(data) as buff_in:
        size_dst = libzstd.ZSTD_getDecompressedSize(buff_in.buf, buff_in.len)
        buff_out = ctyped.array(type=ctyped.type.c_uchar, size=size_dst)
        DecompressionError.check(zr := libzstd.ZSTD_decompress(ctyped.addressof(
            buff_out), size_dst, buff_in.buf, buff_in.len), True)
        # noinspection PyTypeChecker
        return bytes(itertools.islice(buff_out, None, zr))


def compress(data: bytes, level: int = const_zstd.ZSTD_CLEVEL_DEFAULT,
             content_size: bool = True, checksum: bool = True) -> bytes:
    with Compressor(level, content_size, checksum) as compressor:
        return compressor.compress(data) + compressor.end()


def compress_known(data: bytes, level: int = const_zstd.ZSTD_CLEVEL_DEFAULT) -> bytes:
    with ctyped.py_buffer(data) as buff_in:
        size_dst = libzstd.ZSTD_compressBound(buff_in.len)
        buff_out = ctyped.array(type=ctyped.type.c_uchar, size=size_dst)
        CompressionError.check(zr := libzstd.ZSTD_compress(ctyped.addressof(
            buff_out), size_dst, buff_in.buf, buff_in.len, level), True)
        # noinspection PyTypeChecker
        return bytes(itertools.islice(buff_out, None, zr))


ctyped.lib.add_path(os.path.join(os.path.dirname(__file__)))
