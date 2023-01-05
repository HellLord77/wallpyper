__author__ = 'HellLord'
__copyright__ = ''
__credits__ = ['HellLord']

__license__ = ''
__version__ = '0.2.4'
__maintainer__ = 'HellLord'
__email__ = 'ratul.debnath.year@gmail.com'
__status__ = 'Development'

import ctypes
import itertools
import multiprocessing
import sys

import consts


def target(restart: ctypes.c_bool):
    import main
    try:
        main.main()
    except SystemExit:
        restart.value = main.RESTART.get()


def main():
    multiprocessing.freeze_support()
    restart = multiprocessing.Value(ctypes.c_bool, False)
    restart.value = True
    counter = itertools.count(1)
    exitcode = -1
    while restart.value:
        restart.value = False
        process = multiprocessing.Process(
            target=target, name=f'{consts.NAME}-{__version__}-{next(counter)}',
            args=(restart,), daemon=True)
        process.start()
        process.join()
        exitcode = process.exitcode
    sys.exit(exitcode)


if __name__ == '__main__':
    main()
