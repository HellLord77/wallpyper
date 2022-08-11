__author__ = 'HellLord'
__copyright__ = ''
__credits__ = ['HellLord']

__license__ = ''
__version__ = '0.2.1'
__maintainer__ = 'HellLord'
__email__ = 'ratul.debnath.year@gmail.com'
__status__ = 'Development'

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
