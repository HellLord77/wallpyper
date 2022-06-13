__version__ = '0.1.14'

import itertools
import multiprocessing
import sys

import consts


def main():
    import main
    main.main()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    counter = itertools.count(1)
    exitcode = consts.EX_TEMPFAIL
    while exitcode == consts.EX_TEMPFAIL:
        process = multiprocessing.Process(target=main, name=f'{consts.NAME}-{__version__}-{next(counter)}', daemon=True)
        process.start()
        process.join()
        exitcode = process.exitcode
    sys.exit(exitcode)
