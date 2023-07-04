import multiprocessing

from plat import brotli

# noinspection PyBroadException
try:
    brotli.Decompressor()
except BaseException:
    BROTLI = False
else:
    BROTLI = True
RESTART = bool(multiprocessing.parent_process())
