import os
import re

_KITS = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits')
SDK_PATH = os.path.join(_KITS, '10', 'Include', '10.0.22000.0')
NET_PATH = os.path.join(_KITS, 'NETFXSDK', '4.8', 'Include', 'um')


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


def _guid(path: str, prefix: str = 'GUID'):
    with open(path, 'r') as file:
        for match in re.finditer(rf'DEFINE_GUID.*({prefix}_.*)\);', file.read()):
            guid = match.groups()[0].replace(',', ' ').split()
            guid[1] = guid[1].replace('L', '')
            print(f"{guid[0]} = '{_str(guid[1:12])}'")


def devguid():
    _guid(os.path.join(SDK_PATH, 'shared', 'devguid.h'))


def wincodec():
    _guid(os.path.join(SDK_PATH, 'um', 'wincodec.h'), 'CLSID')
    _guid(os.path.join(SDK_PATH, 'um', 'wincodec.h'))


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
    classes = []
    with open(path, 'r') as file:
        for match in re.finditer(r'(RuntimeClass_.*)\[]\s=\sL"(.*)";', file.read()):
            groups = match.groups()
            class_ = f"{groups[0]} = '{groups[1]}'"
            if class_ not in classes:
                classes.append(class_)
    print('\n'.join(classes))


def windows_storage_streams():
    _runtime_class('windows.storage.streams.h')


def windows_storage():
    _runtime_class('windows.storage.h')


def windows_system():
    _runtime_class('windows.system.h')


def winerror():
    path = os.path.join(SDK_PATH, 'shared', 'winerror.h')
    with open(path, 'r') as file:
        for match in re.finditer(r'#define (ERROR_.*)\s(\d*)L', file.read()):
            group = match.groups()
            print(f'{group[0].strip()} = {group[1]}')


def mscoree():
    path = os.path.join(NET_PATH, 'mscoree.h')
    with open(path, 'r') as file:
        for line in file.readlines():
            if line.startswith('EXTERN_GUID('):
                line = line.replace(' ', '')
                guid = line.split(',')[1:]
                guid[-1] = guid[-1][:-3]
                print(f"{line[12:line.find(',')]} = '{_str(guid)}'")


if __name__ == '__main__':
    mscoree()
