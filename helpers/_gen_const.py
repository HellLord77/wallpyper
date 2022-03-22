import os
import re
import urllib.request

# noinspection PyPackageRequirements,PyUnresolvedReferences
from bs4 import BeautifulSoup

import libs.locales._ as locales

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


def _gen_bcp47(lang_str: str, coun_str: str):
    names = [None, None]
    lang = locales.Language[lang_str]
    coun = locales.Country[coun_str]
    for k, v in vars(locales.Language).items():
        if v is lang:
            names[0] = k
            break
    for k, v in vars(locales.Country).items():
        if v is coun:
            names[1] = k
            break
    if all(names):
        print(f"{lang_str}_{coun_str} = _Locale(Language.{names[0]}, Country.{names[1]}, '{lang_str}-{coun_str}')")


def bcp47():
    url = r'https://docs.microsoft.com/en-us/previous-versions/commerce-server/ee825488(v=cs.20)'
    soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url)).read(), 'html.parser')
    table = soup.find(lambda tag: tag.name == 'table')
    body = table.find('tbody')
    for row in body.find_all('tr'):
        row = row.find_all('td')[0].contents[0].split("-")
        if len(row) == 2:
            for s in row:
                if len(s) != 2:
                    break
            else:
                try:
                    _gen_bcp47(row[0], row[1])
                except KeyError:
                    pass


def bcp47_2():
    url = r'https://docs.microsoft.com/en-us/openspecs/office_standards/ms-oe376/6c085406-a698-4e12-9d4d-c3b0ee3dbc4a'
    soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url)).read(), 'html.parser')
    table = soup.find(lambda tag: tag.name == 'table')
    body = table.find('tbody')
    for row in body.find_all('tr')[:-1]:
        row = row.find_all('p')[2].contents[0].split('-')
        if len(row) == 2:
            for s in row:
                if len(s) != 2:
                    break
            else:
                try:
                    _gen_bcp47(row[0], row[1])
                except KeyError:
                    pass


def _get_content(node) -> str:
    while True:
        try:
            node = node.contents[0]
        except AttributeError:
            return node


def iso639():
    url = 'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes'
    soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url)).read(), 'html.parser')
    table = soup.find(id='Table')
    for row in table.find('tbody').find_all('tr')[1:]:
        cells = row.find_all('td')
        try:
            three = f'+{cells[7].contents[2].contents[0]}'
        except IndexError:
            three = ''
        print(f"{cells[0].get('id')} = _Language('{_get_content(cells[1])}', "
              f"'{_get_content(cells[2]).replace(' ', ' ')}', {tuple(_get_content(cells[3]).split(', '))}, "
              f"'{_get_content(cells[4])}', '{_get_content(cells[5])}', '{_get_content(cells[6])}', "
              f"'{_get_content(cells[7])}{three}')")


def iso3166():
    url = 'https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes'
    soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url)).read(), 'html.parser')
    body = soup.find('table', class_='wikitable sortable').find('tbody')
    quote = '\'', "\\'"
    for row in body.find_all('tr')[2:]:
        cells = row.find_all('td')
        id_ = cells[0].get('id')
        if len(cells) == 1:
            name = _get_content(cells[0].contents[2])
            cells = body.find(id=cells[0].contents[4].get('href')[1:]).parent.find_all('td')
        else:
            name = _get_content(cells[0].contents[2])
        cc = []
        for content in cells[7].contents:
            if (c := _get_content(content)).startswith('.'):
                cc.append(c)
        print(f"{id_} = _Country('{name.replace(*quote)}', "
              f"'{_get_content(cells[1]).replace(*quote).replace(' ', ' ')}', '{_get_content(cells[2]).strip()}', "
              f"'{_get_content(cells[3].contents[0].contents[1])}', "
              f"'{_get_content(cells[4].contents[0].contents[1])}', "
              f"'{_get_content(cells[5].contents[0].contents[1])}', {tuple(cc)})")


if __name__ == '__main__':
    mscoree()
