import multiprocessing

from plat import brotli
from win32 import zstd

RESTART_SOFT = bool(multiprocessing.parent_process())

BROTLI_DECODE = bool(brotli.Decompressor)
BROTLI_ENCODE = bool(brotli.Compressor)

ZSTD_DECODE = bool(zstd.Decompressor)
