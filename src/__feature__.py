import multiprocessing

try:
    from plat import brotli as _
except ImportError:
    BROTLI = False
else:
    BROTLI = True
RESTART = bool(multiprocessing.parent_process())
