__author__ = 'HellLord'
__copyright__ = ''
__credits__ = ['HellLord']

__license__ = ''
__version__ = '0.2.4'
__maintainer__ = 'HellLord'
__email__ = 'ratul.debnath.year@gmail.com'
__status__ = 'Development'

import itertools
import multiprocessing
import sys

import consts


def target():
    import main
    main.main()


def main():
    multiprocessing.freeze_support()
    counter = itertools.count(1)
    exitcode = consts.CODE_RESTART
    while exitcode == consts.CODE_RESTART:
        process = multiprocessing.Process(
            target=target, name=f'{consts.NAME}-{__version__}-{next(counter)}', daemon=True)
        process.start()
        process.join()
        exitcode = process.exitcode
    sys.exit(exitcode)


if __name__ == '__main__':
    main()
