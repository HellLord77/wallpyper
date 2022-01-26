import os
import re

import src.libs.ctyped as ctyped
# noinspection PyProtectedMember
from src.platforms.win32 import _EMPTY

VERSION = '10.0.22000.0'


def propkey():
    path = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits', '10', 'Include', VERSION, 'um', 'propkey.h')
    with open(path, 'r') as file:
        for match in re.compile(r'//\s\sName:.*(PKEY_[a-zA-Z_]*)+\n'
                                r'//\s\sType:.*\n'
                                r'//\s\sFormatID:.*({[0-9A-Z-]+}),\s([0-9]+)').finditer(file.read()):
            group = match.groups()
            print(f"{group[0]} = '{group[1]}', {group[2]}")


def devpkey():
    path = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits', '10', 'Include', VERSION, 'um',
                        'functiondiscoverykeys_devpkey.h')
    with open(path, 'r') as file:
        buff = ctyped.type.LPOLESTR(_EMPTY)
        for match in re.compile(r'DEFINE_PROPERTYKEY\((PKEY_.*)\);').finditer(file.read()):
            pkey = match.groups()[0].replace(',', '').split()
            # noinspection PyTypeChecker
            ctyped.func.ole32.StringFromGUID2(ctyped.byref(ctyped.struct.GUID(
                *(int(i, 16) for i in pkey[1:4]), ctyped.array(ctyped.type.c_uchar, *(int(
                    i, 16) for i in pkey[4:12])))), buff, len(_EMPTY))
            print(f"{pkey[0]} = '{buff.value}', {pkey[12]}")


def main():
    devpkey()


if __name__ == '__main__':
    main()
