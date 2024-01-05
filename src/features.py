import multiprocessing

from win32 import brotli
from win32 import zstd

RESTART_SOFT = bool(multiprocessing.parent_process())

BROTLI_DECODE = bool(brotli.Decompressor)

ZSTD_DECODE = bool(zstd.Decompressor)
