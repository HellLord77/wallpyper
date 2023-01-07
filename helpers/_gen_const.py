import functools
import io
import os
import re
import sys
from typing import Optional

from libs import ctyped

_KITS = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits')
SDK_PATH = os.path.join(_KITS, '10', 'Include', '10.0.22621.0')
NET_PATH = os.path.join(_KITS, 'NETFXSDK', '4.8', 'Include', 'um')


def _format(sec: str, sz: int) -> str:
    return f'{sec[2:].upper().removesuffix("L"):>0{sz}}'


def _str(guid: list[str]) -> str:
    return '{{{}-{}-{}-{}}}'.format(_format(guid[0], 8), "-".join(_format(guid[i], 4) for i in range(1, 3)), "".join(_format(guid[i], 2) for i in range(3, 5)), "".join(_format(guid[i], 2) for i in range(5, 11)))


def _guid_direct(path: str, macro: str):
    with open(path) as file:
        for match in re.finditer(rf'interface {macro}\("(.*)"\) (\w*)', file.read()):
            groups = match.groups()
            print(f"IID_{groups[1]} = '{{{groups[0].upper()}}}'")


def d2d1():
    files = 'd2d1', 'd2d1_1', 'd2d1_2', 'd2d1_3'
    for file in files:
        print(f'# {file}')
        _guid_direct(os.path.join(SDK_PATH, 'um', f'{file}.h'), 'DX_DECLARE_INTERFACE')


def dwrite():
    files = 'dwrite', 'dwrite_1', 'dwrite_2', 'dwrite_3'
    for file in files:
        print(f'# {file}')
        _guid_direct(os.path.join(SDK_PATH, 'um', f'{file}.h'), 'DWRITE_DECLARE_INTERFACE')


def propkey():
    path = os.path.join(SDK_PATH, 'um', 'propkey.h')
    with open(path) as file:
        for match in re.finditer(r'DEFINE_PROPERTYKEY\((PKEY_.*)\);', file.read()):
            pkey = match.groups()[0].replace(',', ' ').split()
            print(f"{pkey[0]} = '{_str(pkey[1:12])}', {pkey[12]}")


def functiondiscoverykeys_devpkey():
    path = os.path.join(SDK_PATH, 'um', 'functiondiscoverykeys_devpkey.h')
    with open(path) as file:
        for match in re.finditer(r'DEFINE_PROPERTYKEY\((PKEY_.*)\);', file.read()):
            pkey = match.groups()[0].replace(',', ' ').split()
            print(f"{pkey[0]} = '{_str(pkey[1:12])}', {pkey[12]}")


def devpkey():
    path = os.path.join(SDK_PATH, 'shared', 'devpkey.h')
    with open(path) as file:
        for match in re.finditer(r'DEFINE_DEVPROPKEY\((DEVPKEY_.*)\);', file.read()):
            devpkey_ = match.groups()[0].replace(',', ' ').split()
            print(f"{devpkey_[0]} = '{_str(devpkey_[1:12])}', {devpkey_[12]}")


def knownfolders():
    path = os.path.join(SDK_PATH, 'um', 'KnownFolders.h')
    with open(path) as file:
        for match in re.finditer(r'DEFINE_KNOWN_FOLDER\((FOLDERID_.*)\);', file.read()):
            folderid = match.groups()[0].replace(',', ' ').split()
            print(f"{folderid[0]} = '{_str(folderid[1:12])}'")


def _runtime_class(file: str):
    classes = []
    with open(os.path.join(SDK_PATH, 'winrt', file)) as f:
        for match in re.finditer(r'(RuntimeClass_.*)\[]\s=\sL"(.*)";', f.read()):
            groups = match.groups()
            class_ = f"{groups[0]} = '{groups[1]}'"
            if class_ not in classes:
                classes.append(class_)
    for class_ in classes:
        if len(class_) > 120:
            class_ = class_.replace(" = '", " = ('") + ')'
        print(class_)


def winerror():
    path = os.path.join(SDK_PATH, 'shared', 'winerror.h')
    with open(path) as file:
        for match in re.finditer(r'#define (ERROR_.*)\s(\d*)L', file.read()):
            group = match.groups()
            print(f'{group[0].strip()} = {group[1]}')


def mscoree():
    print('# mscoree')
    path = os.path.join(NET_PATH, 'mscoree.h')
    with open(path) as file:
        for line in file.readlines():
            if line.startswith('EXTERN_GUID('):
                line = line.replace(' ', '')
                guid = line.split(',')[1:]
                guid[-1] = guid[-1][:-3]
                print(f"{line[12:line.find(',')]} = '{_str(guid)}'")


def _clsid_iid(path: str):
    with open(path) as file:
        data = file.read()
    name = ''
    re_name = re.compile(r'EXTERN_C.*const\s(CLSID|IID)\s((CLSID|DIID|IID)_\w*).*;')
    re_iid = re.compile(r'.*(DECLSPEC_UUID|MIDL_INTERFACE)\("(.*)"\)')
    for line in data.splitlines():
        if match := re_name.match(line):
            name = match.groups()[1]
        elif match := re_iid.match(line):
            print(f"{name} = '{{{match.groups()[1].upper()}}}'")


def wincodec():
    print('# wincodec')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'wincodec.h'))


def disp_ex():
    print('# DispEx')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'DispEx.h'))


def ex_disp():
    print('# ExDisp')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'ExDisp.h'))


def ms_html():
    print('# MsHTML')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'MsHTML.h'))


def wincodec_codecs():
    print('# wincodec')
    with open(os.path.join(SDK_PATH, 'um', 'wincodec.h')) as file:
        for match in re.finditer(r'DEFINE_GUID\((\w*),\s*(0x.*)\);', file.read()):
            print(f"{match.groups()[0]} = '{_str(match.groups()[1].split(', '))}'")


def credentialprovider():
    print('# credentialprovider')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'credentialprovider.h'))


def propsys():
    print('# propsys')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'propsys.h'))


def _iid_shlobj(path: str):
    with open(path) as file:
        for match in re.finditer(r'DECLARE_INTERFACE_IID_?\((\w*),.*\s"(.*)"\)', file.read()):
            groups = match.groups()
            print(f"IID_{groups[0]} = '{{{groups[1].upper()}}}'")


def shlobj():
    files = 'ShlObj', 'ShlObj_core'
    for file in files:
        print(f'# {file}')
        _iid_shlobj(os.path.join(SDK_PATH, 'um', f'{file}.h'))


def shlobjidl():
    files = 'ShObjIdl', 'ShObjIdl_core'
    for file in files:
        print(f'# {file}')
        _clsid_iid(os.path.join(SDK_PATH, 'um', f'{file}.h'))


def oaidl():
    print('# oaidl')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'oaidl.h'))


def objidl():
    print('# objidl')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'objidl.h'))


def ocidl():
    print('# ocidl')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'ocidl.h'))


def shldisp():
    print('# ShlDisp')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'shldisp.h'))


def unknwnbase():
    print('# Unknwnbase')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'unknwnbase.h'))


def asyncinfo():
    print('# asyncinfo')
    _clsid_iid(os.path.join(SDK_PATH, 'winrt', 'asyncinfo.h'))


def weakreference():
    print('# WeakReference')
    _clsid_iid(os.path.join(SDK_PATH, 'winrt', 'weakreference.h'))


def desktopwindowxamlhost():
    print('# windows.ui.xaml.hosting.desktopwindowxamlsource')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'windows.ui.xaml.hosting.desktopwindowxamlsource.h'))


def referencetracker():
    print('# windows.ui.xaml.hosting.referencetracker')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'windows.ui.xaml.hosting.referencetracker.h'))


def WebView2():
    print('# WebView2')
    _clsid_iid(r'D:\Projects\WebView2Samples\GettingStartedGuides\Win32_GettingStarted\packages\Microsoft.Web.WebView2.1.0.1418.22\build\native\include\WebView2.h')


def gen_template_iid(file: str):
    with open(os.path.join(SDK_PATH, 'winrt', file)) as f:
        data = f.read()

    re_iid = re.compile(r'struct __declspec\(uuid\("(.*)"\)\)')
    re_interface = re.compile(r'(I.*)<(ABI::.*::(.*)\*, )?.*::(.*)\*> :')

    lines = data.splitlines()
    for index in range(len(lines)):
        if iid := re_iid.fullmatch(lines[index]):
            if interface := re_interface.match(lines[index + 1]):
                groups = interface.groups()
                print(f'IID_{groups[0]}{f"_I{groups[2]}" if groups[2] else ""}_I{groups[3]} = \'{{{iid.groups()[0].upper()}}}\'')


def underscore(word: str) -> str:
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()


def gen_properties(tp):
    template = """
        @classmethod
        @property
        def {}(cls) -> DependencyProperty:
            obj = interface.Windows.UI.Xaml.IDependencyProperty()
            cls[interface.{}].{}(byref(obj))
            return DependencyProperty(obj)"""
    for static in tp._statics:
        if static not in tp.__base__._statics:
            for annot in static.__annotations__:
                if annot.startswith('get_') and annot.endswith('Property'):
                    print(template.format(underscore(annot[4:]), static.__qualname__, annot))


class GdiPlus:
    def __init__(self, path: Optional[str] = None):
        if path is None:
            path = os.path.join(SDK_PATH, 'um', 'gdiplusflat.h')
        self._path = path

    @functools.cache
    def __str__(self):
        return self.generate()

    @staticmethod
    def _resolve_type(type_: str) -> str:
        ptr = 0
        while type_.endswith('*'):
            ptr += 1
            type_ = type_[:-1]
        names = 'type', 'enum', 'struct', 'interface'
        for name in names:
            try:
                getattr(getattr(ctyped, name), type_)
            except AttributeError:
                pass
            else:
                type_ = f'_{name}.{type_}'
                break
        if type_ == 'void' and ptr == 1:
            type_ = '_type.c_void_p'
        if '.' not in type_:
            type_ = f'# TODO {type_}'
        for i in range(ptr - (type_.startswith('_type.Gp') or type_.startswith('_interface.'))):
            type_ = f'_Pointer[{type_}]'
        return type_

    def generate(self) -> str:
        re_comment = re.compile(r'//.*')
        re_func = re.compile(r'(.*?)\((.*)\);')
        re_star = re.compile(r'\*([^*])')
        file = io.StringIO()

        with open(self._path) as f:
            lines = f.read().splitlines()
        line_num = 0
        while line_num < len(lines):
            line = lines[line_num]
            if line.startswith('GpStatus WINGDIPAPI'):
                if lines[line_num].endswith(');'):
                    buff = lines[line_num]
                else:
                    buff = ''
                    while not (line := re_comment.sub('', lines[line_num])).endswith(');'):
                        buff += line
                        line_num += 1
                    buff += line
                func = re_star.sub(r'* \g<1>', ' '.join(buff.split()).removeprefix(
                    'GpStatus WINGDIPAPI').replace('* ', '*').replace(' *', '*').replace(' &', '*').strip())
                groups = re_func.match(func).groups()
                args = groups[1].split(',')
                params = []
                for arg in args:
                    param = arg.split()[-2:]
                    params.append((self._resolve_type(param[0]), param[-1]))
                print(f'{groups[0]}: _Callable[[', file=file, end='')
                first = True
                for param in params[:-1]:
                    if not first:
                        print(f'\n{" " * (len(groups[0]) + 13)}', file=file, end='')
                    print(f'{param[0]},  # {param[-1]}', file=file, end='')
                    first = False
                if params:
                    param = params[-1]
                    if len(params) > 1:
                        print(f'\n{" " * (len(groups[0]) + 13)}', file=file, end='')
                    print(f'{param[0]}],  # {param[-1]}', file=file)
                print(f'{" " * (len(groups[0]) + 12)}{self._resolve_type("GpStatus")}]', file=file)
            line_num += 1

        return file.getvalue()


def main():
    # cl /d1 reportAllClassLayout testVS.cpp
    sys.exit()


if __name__ == '__main__':
    main()
