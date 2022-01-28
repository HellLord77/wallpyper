import os
import re

import src.libs.ctyped as ctyped
# noinspection PyProtectedMember
from src.platforms.win32 import _EMPTY

SDK_PATH = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits', '10', 'Include', '10.0.22000.0')


def propkey():
    path = os.path.join(SDK_PATH, 'um', 'propkey.h')
    with open(path, 'r') as file:
        for match in re.finditer(r'//\s\sName:.*(PKEY_[a-zA-Z_]*)+\n'
                                 r'//\s\sType:.*\n'
                                 r'//\s\sFormatID:.*({[0-9A-Z-]+}),\s([0-9]+)', file.read()):
            group = match.groups()
            print(f"{group[0]} = '{group[1]}', {group[2]}")


def functiondiscoverykeys_devpkey():
    path = os.path.join(SDK_PATH, 'um', 'functiondiscoverykeys_devpkey.h')
    with open(path, 'r') as file:
        buff = ctyped.type.LPOLESTR(_EMPTY)
        for match in re.finditer(r'DEFINE_PROPERTYKEY\((PKEY_.*)\);', file.read()):
            pkey = match.groups()[0].replace(',', '').split()
            # noinspection PyTypeChecker
            ctyped.func.ole32.StringFromGUID2(ctyped.byref(ctyped.struct.GUID(
                *(int(index, 16) for index in pkey[1:4]), ctyped.array(ctyped.type.c_uchar, *(int(
                    index, 16) for index in pkey[4:12])))), buff, len(_EMPTY))
            print(f"{pkey[0]} = '{buff.value}', {pkey[12]}")


def devguid():
    path = os.path.join(SDK_PATH, 'shared', 'devguid.h')
    with open(path, 'r') as file:
        buff = ctyped.type.LPOLESTR(_EMPTY)
        for match in re.finditer(r'DEFINE_GUID\(\s(GUID_.*)\);', file.read()):
            guid = match.groups()[0].replace(',', '').split()
            guid[1] = guid[1][:-1]
            ctyped.func.ole32.StringFromGUID2(ctyped.byref(ctyped.struct.GUID(
                *(int(index, 16) for index in guid[1:4]), ctyped.array(ctyped.type.c_uchar, *(int(
                    index, 16) for index in guid[4:12])))), buff, len(_EMPTY))
            print(f"{guid[0]} = '{buff.value}'")


def devpkey():
    path = os.path.join(SDK_PATH, 'shared', 'devpkey.h')
    with open(path, 'r') as file:
        buff = ctyped.type.LPOLESTR(_EMPTY)
        for match in re.finditer(r'DEFINE_DEVPROPKEY\((DEVPKEY_.*)\);', file.read()):
            guid = match.groups()[0].replace(',', '').split()
            ctyped.func.ole32.StringFromGUID2(ctyped.byref(ctyped.struct.GUID(
                *(int(index, 16) for index in guid[1:4]), ctyped.array(ctyped.type.c_uchar, *(int(
                    index, 16) for index in guid[4:12])))), buff, len(_EMPTY))
            print(f"{guid[0]} = '{buff.value}', {guid[12]}")


def main():
    devpkey()


if __name__ == '__main__':
    main()
