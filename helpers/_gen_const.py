import os
import re
from typing import Union

_KITS = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits')
SDK_PATH = os.path.join(_KITS, '10', 'Include', '10.0.22000.0')
NET_PATH = os.path.join(_KITS, 'NETFXSDK', '4.8', 'Include', 'um')


def _format(sec: str, sz: int) -> str:
    return f'{sec[2:].upper():>0{sz}}'


def _str(guid: list[str]) -> str:
    return '{{{}-{}-{}-{}}}'.format(_format(guid[0], 8), "-".join(_format(guid[i], 4) for i in range(1, 3)), "".join(_format(guid[i], 2) for i in range(3, 5)), "".join(_format(guid[i], 2) for i in range(5, 11)))


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
        for match in re.finditer(rf'DEFINE_GUID.*({prefix}.*)\);', file.read()):
            guid = match.groups()[0].replace(',', ' ').split()
            guid[1] = guid[1].replace('L', '')
            print(f"{guid[0]} = '{_str(guid[1:12])}'")


def devguid():
    _guid(os.path.join(SDK_PATH, 'shared', 'devguid.h'))


def wincodec():
    _guid(os.path.join(SDK_PATH, 'um', 'wincodec.h'), 'CLSID')
    _guid(os.path.join(SDK_PATH, 'um', 'wincodec.h'))


def gdiplusimaging():
    with open(os.path.join(SDK_PATH, 'um', 'gdiplusimaging.h'), 'r') as file:
        for match in re.finditer(r'DEFINE_GUID\((.*)\);', file.read()):
            guid = match.groups()[0].replace(',', ' ').split()
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
    classes = []
    with open(os.path.join(SDK_PATH, 'winrt', file), 'r') as f:
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


def _print_iids(interfaces: Union[dict[str, dict], dict[tuple[str, str], list[str]]], iids: dict[str, str], indent: str = '    '):
    for name in interfaces:
        if isinstance(name, str):
            print(f'{indent}class {name}:')
            _print_iids(interfaces[name], iids, f'{indent}    ')
        else:
            print(f"{indent}IID_{name[0]} = '{{{iids[name[0]]}}}'")


_Namespace = ['Windows']


def _print_interfaces(interfaces: Union[dict[str, dict], dict[tuple[str, str], list[str]]], indent: str = '    '):
    for name in interfaces:
        if not isinstance(name, str):
            if (name[0].endswith('Handler') or name[0].endswith('Callback')) and name[1] == 'IUnknown' and len(interfaces[name]) == 1 and 'Invoke' == interfaces[name][0]:
                print(f'{indent}class _{name[0]}:')
                print(f'{indent}    Invoke: _Callable')
                print(f'{indent}class {name[0]}(_{name[0]}, IUnknown):')
                print(f'{indent}    pass')
                print(f'{indent}# noinspection PyPep8Naming')
                print(f'{indent}class {name[0]}_impl(_{name[0]}, IUnknown_impl):')
                print(f'{indent}    pass')
            else:
                print(f'{indent}class {name[0]}({name[1]}):')
                if interfaces[name]:
                    trunc_name = name[0]
                    while trunc_name[-1].isdigit():
                        trunc_name = trunc_name[:-1]
                    is_static = trunc_name.endswith('Statics')
                    for func in interfaces[name]:
                        if is_static and func.startswith('get_') and func.endswith('Property'):
                            print(f'{indent}    {func}: _Callable[[_Pointer[Windows.UI.Xaml.IDependencyProperty]],')
                            print('_type.HRESULT]')
                        else:
                            print(f'{indent}    {func}: _Callable')
                else:
                    print(f'{indent}    pass')
    for name in interfaces:
        if isinstance(name, str):
            print(f'{indent}class {name}:')
            _Namespace.append(name)
            _print_interfaces(interfaces[name], f'{indent}    ')
            _Namespace.pop()


def gen_winrt_interface(file: str):
    with open(os.path.join(SDK_PATH, 'winrt', file), 'r') as f:
        data = f.read()

    re_midl = re.compile(r'MIDL_INTERFACE\(\"(.*)\"\)')
    re_windows = re.compile('namespace Windows {')
    re_namespace = re.compile(r'namespace (.*) {')
    re_interface = re.compile('(I.*) : public (.*)')
    re_func = re.compile(r'virtual HRESULT STDMETHODCALLTYPE (.*)\(')

    interfaces = {}
    iids = {}
    lines = data.split('\n')
    for index in range(len(lines)):
        line = lines[index].strip()
        if midl := re_midl.findall(line):
            namespaces = []
            index_ = index
            while not re_windows.findall(line_ := lines[index_]):
                if namespace := re_namespace.findall(line_):
                    namespaces.append(namespace[0])
                index_ -= 1
            index_ = index
            while not re_interface.findall(lines[index_]):
                index_ += 1
            interface, base = re_interface.findall(lines[index_])[0]
            iids[interface] = midl[0].upper()
            funcs = []
            while (line_ := lines[index_]).find('};') == -1:
                if func := re_func.findall(line_):
                    funcs.append(func[0])
                index_ += 1
            dict_ = interfaces
            for namespace in namespaces[::-1]:
                dict_[namespace] = dict_.get(namespace, {})
                dict_ = dict_[namespace]
            dict_[interface, base] = funcs
    print('class Windows:')
    _print_iids(interfaces, iids)
    print('class Windows:')
    _print_interfaces(interfaces)


def set_const():
    path = r'D:\Projects\wallpyper\src\libs\ctyped\const.py'
    iids = set()
    with open(path, 'r') as file:
        for match in re.finditer(r"IID_(.*) = '(.*)'", file.read()):
            grp = match.groups()
            if grp[1] in iids:
                print(f'IID_{grp[0]}')
            else:
                iids.add(grp[1])


if __name__ == '__main__':
    gen_winrt_interface('windows.ui.xaml.media.animation.h')
