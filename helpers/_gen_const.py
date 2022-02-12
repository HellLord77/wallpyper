import os
import re

SDK_PATH = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits', '10', 'Include', '10.0.22000.0')


def _format(sec: str, sz: int) -> str:
    return f'{sec[2:].upper():>0{sz}}'


def _str(guid: list[str]) -> str:
    return '{{{}-{}-{}-{}}}'.format(_format(guid[0], 8), "-".join(_format(guid[i], 4) for i in range(1, 3)),
                                    "".join(_format(guid[i], 2) for i in range(3, 5)),
                                    "".join(_format(guid[i], 2) for i in range(5, 11)))


def propkey():
    path = os.path.join(SDK_PATH, 'um', 'propkey.h')
    with open(path, 'r') as file:
        for match in re.finditer(r'DEFINE_PROPERTYKEY\((PKEY_.*)\);', file.read()):
            pkey = match.groups()[0].replace(',', ' ').split()
            print(f"{pkey[0]} = '{_str(pkey[1:12])}', {pkey[12]}")


def functiondiscoverykeys_devpkey():
    path = os.path.join(SDK_PATH, 'um', 'functiondiscoverykeys_devpkey.h')
    with open(path, 'r') as file:
        for match in re.finditer(r'DEFINE_PROPERTYKEY\((PKEY_.*)\);', file.read()):
            pkey = match.groups()[0].replace(',', ' ').split()
            print(f"{pkey[0]} = '{_str(pkey[1:12])}', {pkey[12]}")


def devguid():
    path = os.path.join(SDK_PATH, 'shared', 'devguid.h')
    with open(path, 'r') as file:
        for match in re.finditer(r'DEFINE_GUID\(\s(GUID_.*)\);', file.read()):
            guid = match.groups()[0].replace(',', ' ').split()
            guid[1] = guid[1][:-1]
            print(f"{guid[0]} = '{_str(guid[1:12])}'")


def devpkey():
    path = os.path.join(SDK_PATH, 'shared', 'devpkey.h')
    with open(path, 'r') as file:
        for match in re.finditer(r'DEFINE_DEVPROPKEY\((DEVPKEY_.*)\);', file.read()):
            devpkey_ = match.groups()[0].replace(',', ' ').split()
            print(f"{devpkey_[0]} = '{_str(devpkey_[1:12])}', {devpkey_[12]}")


def knownfolders():
    path = os.path.join(SDK_PATH, 'um', 'KnownFolders.h')
    with open(path, 'r') as file:
        for match in re.finditer(r'DEFINE_KNOWN_FOLDER\((FOLDERID_.*)\);', file.read()):
            folderid = match.groups()[0].replace(',', ' ').split()
            print(f"{folderid[0]} = '{_str(folderid[1:12])}'")


def _runtime_class(file: str):
    path = os.path.join(SDK_PATH, 'winrt', file)
    with open(path, 'r') as file:
        for match in re.finditer(r'(RuntimeClass_.*)\[]\s=\sL"(.*)";', file.read()):
            groups = match.groups()
            print(f"{groups[0]} = '{groups[1]}'")


def windows_storage_streams():
    _runtime_class('windows.storage.streams.h')


def windows_storage():
    _runtime_class('windows.storage.h')


if __name__ == '__main__':
    windows_storage()
