import glob
import io
import os
import re
from typing import Optional

from libs import ctyped

_KITS = os.path.join(os.environ['ProgramFiles(x86)'], 'Windows Kits')
SDK_PATH = os.path.join(_KITS, '10', 'Include', '10.0.22621.0')
NET_PATH = os.path.join(_KITS, 'NETFXSDK', '4.8', 'Include', 'um')


def _format(sec: str, sz: int) -> str:
    return f'{sec[2:].upper():>0{sz}}'


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


def _guid(path: str, prefix: str = 'GUID'):
    with open(path) as file:
        for match in re.finditer(rf'DEFINE_GUID.*({prefix}.*)\);', file.read()):
            guid = match.groups()[0].replace(',', ' ').split()
            guid[1] = guid[1].replace('L', '')
            print(f"{guid[0]} = '{_str(guid[1:12])}'")


def ddraw():
    _guid(os.path.join(SDK_PATH, 'um', f'ddraw.h'), 'CLSID')
    _guid(os.path.join(SDK_PATH, 'um', f'ddraw.h'), 'IID')


def d3d11():
    files = 'd3d11', 'd3d11_1', 'd3d11_2', 'd3d11_3', 'd3d11_4'
    for file in files:
        print(f'# {file}')
        _guid(os.path.join(SDK_PATH, 'um', f'{file}.h'), 'IID')


def dxgi():
    files = 'dxgi', 'dxgi1_2', 'dxgi1_3', 'dxgi1_4', 'dxgi1_5', 'dxgi1_6'
    for file in files:
        print(f'# {file}')
        _guid(os.path.join(SDK_PATH, 'shared', f'{file}.h'), 'IID')


def devguid():
    _guid(os.path.join(SDK_PATH, 'shared', 'devguid.h'))


def gdiplusimaging():
    print('# gdiplusimaging')
    with open(os.path.join(SDK_PATH, 'um', 'gdiplusimaging.h')) as file:
        for match in re.finditer(r'DEFINE_GUID\((.*)\);', file.read()):
            guid = match.groups()[0].replace(',', ' ').split()
            print(f"{guid[0]} = '{_str(guid[1:12])}'")


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
    re_name = re.compile(r'EXTERN_C\sconst\s(CLSID|IID)\s((CLSID|IID)_.*);')
    re_iid = re.compile(r'.*(DECLSPEC_UUID|MIDL_INTERFACE)\("(.*)"\)')
    for line in data.splitlines():
        if match := re_name.match(line):
            name = match.groups()[1]
        elif match := re_iid.match(line):
            print(f"{name} = '{{{match.groups()[1].upper()}}}'")


def wincodec():
    print('# wincodec')
    _clsid_iid(os.path.join(SDK_PATH, 'um', 'wincodec.h'))


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


def _print_iids(interfaces: dict[str, dict] | dict[tuple[str, str] | list[str]], iids: dict[str, str], indent: str = '    '):
    for name in interfaces:
        if isinstance(name, str):
            print(f'{indent}class {name}:')
            _print_iids(interfaces[name], iids, f'{indent}    ')
        else:
            print(f"{indent}IID_{name[0]} = '{{{iids[name[0]]}}}'")


_Namespace = ['Windows']


def _print_interfaces(interfaces: dict[str, dict] | dict[tuple[str, str] | list[str]], indent: str = '    '):
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


def gen_winrt_interface(pattern: str = '*.h'):
    data = ''
    for file in glob.glob(os.path.join(SDK_PATH, 'winrt', pattern)):
        with open(file) as stream:
            data += stream.read()

    re_midl = re.compile(r'MIDL_INTERFACE\(\"(.*)\"\)')
    re_windows = re.compile('namespace Windows {')
    re_namespace = re.compile(r'namespace (.*) {')
    re_interface = re.compile('(I.*) : public (.*)')
    re_func = re.compile(r'virtual HRESULT STDMETHODCALLTYPE (.*)\(')

    interfaces = {}
    iids = {}
    lines = data.splitlines()
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
            for namespace in reversed(namespaces):
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
    with open(path) as file:
        for match in re.finditer(r"IID_(.*) = '(.*)'", file.read()):
            grp = match.groups()
            if grp[1] in iids:
                print(f'IID_{grp[0]}')
            else:
                iids.add(grp[1])


def underscore(word: str) -> str:
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()


def gen_properties(tp):
    template = '''
        @classmethod
        @property
        def {}(cls) -> DependencyProperty:
            obj = interface.Windows.UI.Xaml.IDependencyProperty()
            cls[interface.{}].{}(byref(obj))
            return DependencyProperty(obj)'''
    for static in tp._statics:
        if static not in tp.__base__._statics:
            for annot in static.__annotations__:
                if annot.startswith('get_') and annot.endswith('Property'):
                    print(template.format(underscore(annot[4:]), static.__qualname__, annot))


def _print_generated_files_iid(iids: dict[str, str | dict], intend: str = ''):
    for name in iids:
        if isinstance(iids[name], str):
            print(f"{intend}IID_{name} = '{{{iids[name]}}}'")
        else:
            print(f'{intend}class {name}:')
            _print_generated_files_iid(iids[name], f'{intend}    ')


def gen_generated_files_iid(base: str):
    iid = {}
    for file in os.listdir(base):
        if file.endswith('.h'):
            with open(os.path.join(base, file)) as f:
                for match in re.finditer(r'\s\s\s\stemplate <> inline constexpr guid guid_v<winrt::(.*)>{ .*// (.*)', f.read()):
                    groups = match.groups()
                    dct = iid
                    namespaces = groups[0].split('::')
                    for namespace in namespaces[:-1]:
                        dct[namespace] = dct.get(namespace, {})
                        dct = dct[namespace]
                    dct[namespaces[-1]] = groups[1]
    _print_generated_files_iid(iid)


def get_datas(datas: dict, namespaces: list[str]) -> dict:
    for namespace in namespaces:
        try:
            datas = datas[namespace]
        except KeyError:
            datas[namespace] = datas = {}
    return datas


def find_end(lines: list[str], line_num: int) -> int:
    if lines[line_num + 1].strip().startswith('{'):
        while not lines[line_num].strip().startswith('}'):
            line_num += 1
    else:
        line_num = 0
    return line_num


def sort_enum_struct(datas: dict):
    pops = []
    for name, value in datas.items():
        if isinstance(next(iter(value.values())), dict):
            pops.append(name)
            sort_enum_struct(value)
    pops.sort()
    for name in pops:
        datas[name] = datas.pop(name)


def sort_iids(datas: dict):
    pops = []
    for name, data in datas.items():
        if isinstance(data, dict):
            pops.append(name)
            sort_iids(data)
    pops.sort()
    for name in pops:
        datas[name] = datas.pop(name)


def sort_interface(datas: dict):
    pops = []
    for name, data in datas.items():
        if isinstance(name, str):
            pops.append(name)
            sort_interface(data)
    pops.sort()
    for name in pops:
        datas[name] = datas.pop(name)


def add_ptr(type_: str, count: int) -> str:
    for _ in range(count):
        type_ = f'_Pointer[{type_}]'
    return type_


def resolve_type(type_: str, this: str = '', interfaces: Optional[dict] = None, runtimeclasses: Optional[dict] = None, re_bracket=re.compile('<(.*)>')) -> str:
    names = 'type', 'enum', 'struct'
    ptr_c = 0
    while type_.endswith('*'):
        ptr_c += 1
        type_ = type_[:-1]
    if type_ == 'AsyncStatus':
        return add_ptr(f'{"_enum." * (this != "enum")}Windows.Foundation.AsyncStatus', ptr_c)
    elif type_ == 'IInspectable' or type_ == 'IUnknown':
        return add_ptr(f'{"_interface." * (this != "interface")}{type_}', ptr_c - 1)
    elif type_ == 'Windows.Foundation.Collections.IVectorChangedEventArgs':
        return add_ptr(type_, ptr_c - 1)
    if runtimeclasses:
        *namespaces, name = type_.split('.')
        base = runtimeclasses
        for namespace in namespaces:
            try:
                base = base[namespace]
            except KeyError:
                break
        try:
            type_ = base[name][0]
        except KeyError:
            pass
    for name in names:
        if name != this:
            types = getattr(ctyped, name)
            try:
                for type__ in type_.split('.'):
                    types = getattr(types, type__)
            except AttributeError:
                continue
            else:
                return add_ptr(f'_{name}.{type_}', ptr_c)
    if this == 'interface':
        if match := re_bracket.search(type_):
            *namespaces, name = type_[:match.start()].split('.')
            return add_ptr(f'{".".join(namespaces)}.{"I" * (1 - name.startswith("I"))}{name}{[resolve_type(type__, this, interfaces, runtimeclasses) for type__ in get_params(match.groups()[0])]}'.replace("'", ''), ptr_c - 1)
        else:
            *namespaces, name = type_.split('.')
            for namespace in namespaces:
                try:
                    interfaces = interfaces[namespace]
                except KeyError:
                    break
            i_type = None
            for key in interfaces:
                if key[0] == name:
                    i_type = type_
                elif key[0] == f'I{name}':
                    i_type = f'{".".join(namespaces)}.I{name}'
                if i_type:
                    return add_ptr(i_type, ptr_c - 1)
    print(f'# TODO {type_}')
    return type_


def get_params(line: str) -> list[str]:
    params = []
    start = 0
    bracket = 0
    for index in range(len(line)):
        char = line[index]
        if char == '<':
            bracket += 1
        elif char == '>':
            bracket -= 1
        elif char == ',' and not bracket:
            params.append(line[start:index])
            start = index + 2
    params.append(line[start:])
    if params[0] == '':
        params.clear()
    return params


def get_args(line: str, re_bracket=re.compile(r'\[.*?]')) -> dict[str, str]:
    args = {}
    params = get_params(' '.join(re_bracket.sub('', line).split()))
    for param in params:
        *type_, name = param.removeprefix('const ').rsplit(maxsplit=1)
        args[name] = ''.join(type_)
    return args


def print_enum(enums: dict, intend: str = ''):
    sort_enum_struct(enums)
    for name, value in enums.items():
        if isinstance(next(iter(value.values())), str):
            print(f'{intend}class {name}(_Enum):')
            for name_, value_ in value.items():
                print(f'{intend}    {"None_" if name_ == "None" else name_} = {value_}')
        else:
            print(f'{intend}class {name}:')
            print_enum(value, f'{intend}    ')


def print_struct(structs: dict, indent: str = ''):
    sort_enum_struct(structs)
    for name, value in structs.items():
        if isinstance(next(iter(value.values())), str):
            print(f'{indent}@_struct')
            print(f'{indent}class {name}:')
            for name_, value_ in value.items():
                print(f'{indent}    {name_}: {resolve_type(value_, "struct")} = None')
        else:
            print(f'{indent}class {name}:')
            print_struct(value, f'{indent}    ')


def print_iid(iids: dict, indent: str = ''):
    sort_iids(iids)
    for name, value in iids.items():
        if isinstance(value, dict):
            print(f'{indent}class {name}:')
            print_iid(value, f'{indent}    ')
        else:
            print(f'{indent}IID_{name} = \'{{{value}}}\'')


def print_interface(interfaces: dict, runtimeclasses: dict, indent: str = '', __interfaces=None):
    sort_interface(interfaces)
    if __interfaces is None:
        __interfaces = interfaces
    for name, value in interfaces.items():
        if isinstance(name, tuple):
            is_delegate = name[1] == 'IUnknown' and len(value) == 1 and 'Invoke' in value
            print(f'{indent}class {"_" * is_delegate}{name[0]}{f"({name[1]})" * (not is_delegate)}:')
            if value:
                for func, (args, res) in value.items():
                    q_final = f'{indent}    {func}: _Callable[[' + f',\n{indent}        '.join(resolve_type(val, "interface", __interfaces, runtimeclasses) for val in args.values()) + '],'
                    s_final = ''
                    if args:
                        for line, kwarg in zip(q_final.splitlines(), args):
                            s_final += line + f'  # {kwarg}\n'
                    else:
                        s_final += q_final + '\n'
                    print(f'{s_final}{indent}        {resolve_type(res, "interface", __interfaces, runtimeclasses)}]')
            else:
                print(f'{indent}    pass')
            if is_delegate:
                print(f'{indent}class {name[0]}(_{name[0]}, {name[1]}):')
                print(f'{indent}    pass')
                print(f'{indent}# noinspection PyPep8Naming')
                print(f'{indent}class {name[0]}_impl(_{name[0]}, {name[1]}_impl):')
                print(f'{indent}    pass')
        else:
            print(f'{indent}class {name}:')
            print_interface(value, runtimeclasses, f'{indent}    ', __interfaces)


def gen_winrt(pattern: str = '*.idl', p_enum: bool = False, p_struct: bool = False, p_iid: bool = False, p_interface: bool = False):
    data = ''
    assert pattern.endswith('.idl')
    for file in glob.glob(os.path.join(SDK_PATH, 'winrt', pattern)):
        if '.' in os.path.splitext(os.path.basename(file))[0]:
            with open(file) as stream:
                data += stream.read()

    re_namespace = re.compile(r'namespace (\S+)')
    re_enum = re.compile(r'enum (\S+)')
    re_enum_ = re.compile(r'(\S+)(\s*)=\s((0x)?\d*),?')
    re_struct = re.compile(r'struct (\S+)')
    re_struct_ = re.compile(r'(\S+)\s(.*);')
    re_iid = re.compile(r'\[uuid\(([\dA-F]{8}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{12})\)]')
    re_delegate = re.compile(r'delegate')
    re_interface = re.compile(r'interface (\S+) : (\S+)')
    re_func = re.compile(r'(\S+) (\S+?)\((.*)\);')
    re_template = re.compile(r'declare')
    re_runtimeclass = re.compile(r'runtimeclass (\S+)')
    re_runtimeclass_interface = re.compile(r'interface (.*);')
    re_attribute = re.compile(r'attribute (\S+)')
    re_contract = re.compile(r'apicontract (\S+)')

    lines = data.splitlines()
    namespaces = []
    enums = {}
    structs = {}
    iids = {}
    interfaces = {}
    runtimeclasses = {}
    line_num = 0
    while line_num < len(lines):
        line = lines[line_num].strip()
        if match := re_namespace.fullmatch(line):
            namespaces.append(match.groups()[0])
            line_num += 1
        elif match := re_enum.fullmatch(line):
            enum = {}
            if end := find_end(lines, line_num):
                start = line_num + 2
                line_num = end
                for line_ in lines[start:end]:
                    if match_ := re_enum_.fullmatch(line_.strip()):
                        enum[match_.groups()[0]] = match_.groups()[2]
                get_datas(enums, namespaces)[match.groups()[0]] = enum
        elif match := re_struct.fullmatch(line):
            struct = {}
            if end := find_end(lines, line_num):
                start = line_num + 2
                line_num = end
                for line_ in lines[start:end]:
                    if match_ := re_struct_.fullmatch(line_.strip()):
                        struct[match_.groups()[1]] = match_.groups()[0]
                get_datas(structs, namespaces)[match.groups()[0]] = struct
        elif re_delegate.fullmatch(line):
            line_ = lines[line_num + 1].strip()
            match_ = re_func.fullmatch(line_[line_.find('HRESULT'):])
            func = f'I{match_.groups()[1]}'
            get_datas(iids, namespaces)[func] = re_iid.fullmatch(lines[line_num - 1].strip()).groups()[0]
            get_datas(interfaces, namespaces)[(func, 'IUnknown')] = {'Invoke': (get_args(match_.groups()[2]), match_.groups()[0])}
        elif match := re_interface.fullmatch(line):
            get_datas(iids, namespaces)[match.groups()[0]] = re_iid.fullmatch(lines[line_num - 1].strip()).groups()[0]
            interface = {}
            while not lines[line_num].strip().startswith('{'):
                line_num += 1
            line_num_ = line_num + 1
            while not lines[line_num].strip().startswith('}'):
                line_num += 1
            for line_ in lines[line_num_:line_num]:
                line_ = line_.strip()
                match_ = re_func.fullmatch(line_[line_.find('HRESULT'):])
                func = match_.groups()[1]
                if line_.startswith('[propget]'):
                    func = 'get_' + func
                elif line_.startswith('[propput]'):
                    func = 'put_' + func
                elif line_.startswith('[eventadd]'):
                    func = 'add_' + func
                elif line_.startswith('[eventremove]'):
                    func = 'remove_' + func
                interface[func] = get_args(match_.groups()[2]), match_.groups()[0]
            get_datas(interfaces, namespaces)[match.groups()] = interface
        elif re_template.fullmatch(line):
            if end := find_end(lines, line_num):
                start = line_num + 2
                line_num = end
        elif match := re_runtimeclass.search(line):
            if not line.endswith(';'):
                runtimeclass = []
                if end := find_end(lines, line_num):
                    start = line_num + 2
                    line_num = end
                    default_index = None
                    for line_ in lines[start:end]:
                        if match_ := re_runtimeclass_interface.search(line_):
                            runtimeclass.append(match_.groups()[0])
                            if line_.find('[default]') != -1:
                                default_index = len(runtimeclass) - 1
                    if default_index is not None:
                        runtimeclass.insert(0, runtimeclass.pop(default_index))
                    get_datas(runtimeclasses, namespaces)[match.groups()[0]] = tuple(runtimeclass)
        elif re_contract.fullmatch(line):
            if end := find_end(lines, line_num):
                start = line_num + 2
                line_num = end
        elif re_attribute.fullmatch(line):
            if end := find_end(lines, line_num):
                start = line_num + 2
                line_num = end
        elif line.startswith('}'):
            # print(namespaces, line_num + 1)
            try:
                namespaces.pop()
            except IndexError:
                print(*lines[line_num - 5:line_num], sep='\n')
                raise
        line_num += 1
    assert not namespaces
    if p_enum:
        print_enum(enums)
    if p_struct:
        print_struct(structs)
    if p_iid:
        print_iid(iids)
    if p_interface:
        print_interface(interfaces, runtimeclasses)
    # pprint.pprint(runtimeclasses, width=1, sort_dicts=False)


def clean_and_wrap(typ: str, count: int = 0) -> str:
    typ = typ.replace('const ', '')
    for i in range(count):
        typ = f'_Pointer[{typ}]'
    return typ


class GdiPlus:
    _data = None

    def __init__(self, path: Optional[str] = None):
        if path is None:
            path = os.path.join(SDK_PATH, 'um', 'gdiplusflat.h')
        self._path = path

    def __str__(self):
        if self._data is None:
            self._data = self.generate()
        return self._data

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

        file.seek(0)
        return file.read()


if __name__ == '__main__':
    # TODO cl /d1 reportAllClassLayout testVS.cpp
    shldisp()
    # noinspection PyUnresolvedReferences
    # from libs.ctyped import winrt
    #
    # f = open('gen.py', 'w')
    # sys.stdout = f
    # gen_winrt(p_interface=True)
    # f.close()
    # gen_template_iid('Windows.ui.composition.h')
    # gen_winrt_interface('Windows.foundation.h')
    # gen_properties(winrt._utils.LinearGradientBrush)
    # gen_generated_files_iid(r'D:\Projects\MyDesktopWin32App\x64\Debug\Generated Files\winrt\impl')
    exit()
