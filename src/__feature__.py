import multiprocessing

from plat import brotli

RESTART_APP = bool(multiprocessing.parent_process())

BROTLI_DECODE = bool(brotli.Decompressor)
BROTLI_ENCODE = bool(brotli.Compressor)
