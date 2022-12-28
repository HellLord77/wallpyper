import csv
import html
import io
import subprocess
import sys
import textwrap
import warnings
from typing import IO

from libs import ctyped

ERR_PATH = r'D:\Apps\Err_6.4.5.exe'


def dump(file: IO = sys.stdout):
    data = subprocess.check_output((ERR_PATH, '/:outputtoCSV'))
    buff = io.StringIO(data.decode())
    last_header = ''
    reader = csv.reader(buff)
    next(reader)
    for code, name, comment, header in reader:
        if last_header != header:
            file.write(f'\n# {header}\n')
            last_header = header
        file.write(f'{name} = {code.upper().replace("X", "x", 1)}\n')
        comment = html.unescape(comment).replace('%0', '').removeprefix(
            '//').removeprefix('/*').removesuffix('*/').strip()
        if comment not in ('N/A', '%0', ''):
            file.write(f'"""\n')
            file.write('\n'.join(textwrap.wrap(comment, 59)))
            file.write('\n"""\n')
        try:
            getattr(ctyped.const, name)
        except AttributeError:
            pass
        else:
            warnings.warn(name)


def main():
    with open('error.py', 'w') as file:
        dump(file)


if __name__ == '__main__':
    main()
