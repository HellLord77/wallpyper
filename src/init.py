__author__ = 'HellLord'
__copyright__ = ''
__credits__ = ['HellLord']

__license__ = ''
__version__ = '0.2.6'
__maintainer__ = 'HellLord'
__email__ = 'ratul.debnath.year@gmail.com'
__status__ = 'Development'

import ctypes
import itertools
import logging
import multiprocessing
import multiprocessing.managers
import sys
import time

import consts


# noinspection PyUnresolvedReferences
def target(reset: multiprocessing.managers.ListProxy,
           restart: multiprocessing.managers.ValueProxy):
    if not consts.FLAG_FANCY_DEBUG:
        logging.basicConfig()
    start = time.monotonic()
    import main
    main.START = start
    main.RESET = reset
    try:
        main.main()
    except SystemExit:
        restart.value = main.RESTART.get()


def main():
    multiprocessing.freeze_support()
    counter = itertools.count(1)
    manager = multiprocessing.Manager()
    reset = manager.list()
    restart = manager.Value(ctypes.c_bool, True)
    exitcode = -1
    while restart.value:
        restart.value = False
        process = multiprocessing.Process(
            target=target, name=f'{consts.NAME}-{__version__}-{next(counter)}',
            args=(reset, restart), daemon=True)
        process.start()
        process.join()
        exitcode = process.exitcode
    sys.exit(exitcode)


if __name__ == '__main__':
    main()
