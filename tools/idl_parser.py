import contextlib
import functools
import glob
import io
import ntpath
import os
import pprint
import re
import shutil
import subprocess
import sys
import tempfile
import warnings
from typing import Any
from typing import Callable
from typing import Optional

import bs4
import markdown

from libs import ctyped

SDK_PATH = r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0'
# SDK_PATH = r'D:\Projects\wallpyper\tools'
DOC_DIR = r'D:\Projects\winrt-api'
# DOC_DIR = r'D:\Projects\winapps-winrt-api'
DOC_LINK_PREFIX = 'https://learn.microsoft.com/en-us/uwp/api/'
# DOC_LINK_PREFIX = 'https://learn.microsoft.com/en-us/windows/windows-app-sdk/api/winrt/'
WINMDIDL_DIR = r'C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64'
TYPE_MAP = {
    'IUnknown':                                               '_Unknwnbase.IUnknown',
    'IInspectable':                                           '_inspectable.IInspectable',
    'Windows.Foundation.Collections.IVectorChangedEventArgs': '_Windows_Foundation_Collections.IVectorChangedEventArgs'}
ABS_IMPORTS = [
    'from __future__ import annotations as _',
    'from typing import Callable as _Callable, Generic as _Generic']
EX_IMPORTS: tuple[str, ...] = (
    '. import inspectable as _inspectable',
    '.. import _K, _V, _T, _TArgs, _TProgress, _TResult, _TSender, _Template',
    '..um import Unknwnbase as _Unknwnbase',
    '... import enum as _enum',
    '... import struct as _struct',
    '... import type as _type',
    '..._utils import _Pointer')
EX_ENUMS = {
    'Windows.Foundation.AsyncStatus':                  {
        'Started':   '0',
        'Completed': '1',
        'Canceled':  '2',
        'Error':     '3'},
    'Windows.Foundation.Collections.CollectionChange': {
        'Reset':        '0',
        'ItemInserted': '1',
        'ItemRemoved':  '2',
        'ItemChanged':  '3'}}
DATA_INTERFACE: dict[str, str] = {
    'Windows.Foundation':             '''
class _IAsyncOperationProgressHandler(_Template):
    Invoke: _Callable[[IAsyncOperationWithProgress[_TResult, _TProgress],  # asyncInfo
                       _TProgress],  # progressInfo
                      _type.HRESULT]


class IAsyncOperationProgressHandler(_IAsyncOperationProgressHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncOperationProgressHandler_impl(_IAsyncOperationProgressHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown_impl):
    pass


class _IAsyncOperationWithProgressCompletedHandler(_Template):
    Invoke: _Callable[[IAsyncOperationWithProgress[_TResult, _TProgress],  # asyncInfo
                       _enum.Windows.Foundation.AsyncStatus],  # status
                      _type.HRESULT]


class IAsyncOperationWithProgressCompletedHandler(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncOperationWithProgressCompletedHandler_impl(_IAsyncOperationWithProgressCompletedHandler, _Generic[_TResult, _TProgress], _Unknwnbase.IUnknown_impl):
    pass


class _IAsyncOperationCompletedHandler(_Template):
    Invoke: _Callable[[IAsyncOperation[_TResult],  # asyncInfo
                       _enum.Windows.Foundation.AsyncStatus],  # status
                      _type.HRESULT]


class IAsyncOperationCompletedHandler(_IAsyncOperationCompletedHandler, _Generic[_TResult], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncOperationCompletedHandler_impl(_IAsyncOperationCompletedHandler, _Generic[_TResult], _Unknwnbase.IUnknown_impl):
    pass


class IAsyncOperationWithProgress(_Template, _Generic[_TResult, _TProgress], _inspectable.IInspectable):
    put_Progress: _Callable[[IAsyncOperationProgressHandler[_TResult, _TProgress]],  # handler
                            _type.HRESULT]
    get_Progress: _Callable[[_Pointer[IAsyncOperationProgressHandler[_TResult, _TProgress]]],  # handler
                            _type.HRESULT]
    put_Completed: _Callable[[IAsyncOperationWithProgressCompletedHandler[_TResult, _TProgress]],  # handler
                             _type.HRESULT]
    get_Completed: _Callable[[_Pointer[IAsyncOperationWithProgressCompletedHandler[_TResult, _TProgress]]],  # handler
                             _type.HRESULT]
    GetResults: _Callable[[_Pointer[_TResult]],  # results
                          _type.HRESULT]


class IAsyncActionWithProgress(_Template, _Generic[_TProgress], _inspectable.IInspectable):
    put_Progress: _Callable[[IAsyncActionProgressHandler[_TProgress]],  # handler
                            _type.HRESULT]
    get_Progress: _Callable[[_Pointer[IAsyncActionProgressHandler[_TProgress]]],  # handler
                            _type.HRESULT]
    put_Completed: _Callable[[IAsyncActionWithProgressCompletedHandler[_TProgress]],  # handler
                             _type.HRESULT]
    get_Completed: _Callable[[_Pointer[IAsyncActionWithProgressCompletedHandler[_TProgress]]],  # handler
                             _type.HRESULT]
    GetResults: _Callable[[],
                          _type.HRESULT]


class IAsyncOperation(_Template, _Generic[_TResult], _inspectable.IInspectable):
    put_Completed: _Callable[[IAsyncOperationCompletedHandler[_TResult]],  # handler
                             _type.HRESULT]
    get_Completed: _Callable[[_Pointer[IAsyncOperationCompletedHandler[_TResult]]],  # handler
                             _type.HRESULT]
    GetResults: _Callable[[_Pointer[_TResult]],  # results
                          _type.HRESULT]


class _IAsyncActionProgressHandler(_Template):
    Invoke: _Callable[[IAsyncActionWithProgress[_TProgress],  # asyncInfo
                       _TProgress],  # progressInfo
                      _type.HRESULT]


class IAsyncActionProgressHandler(_IAsyncActionProgressHandler, _Generic[_TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncActionProgressHandler_impl(_IAsyncActionProgressHandler, _Generic[_TProgress], _Unknwnbase.IUnknown_impl):
    pass


class _IAsyncActionWithProgressCompletedHandler(_Template):
    Invoke: _Callable[[IAsyncActionWithProgress[_TProgress],  # asyncInfo
                       _enum.Windows.Foundation.AsyncStatus],  # status
                      _type.HRESULT]


class IAsyncActionWithProgressCompletedHandler(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAsyncActionWithProgressCompletedHandler_impl(_IAsyncActionWithProgressCompletedHandler, _Generic[_TProgress], _Unknwnbase.IUnknown_impl):
    pass


class IReference(_Template, _Generic[_T], _inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_T]],  # value
                         _type.HRESULT]


class IReferenceArray(_Template, _Generic[_T], _inspectable.IInspectable):
    get_Value: _Callable[[_Pointer[_type.UINT32],  # length
                          _Pointer[_Pointer[_T]]],  # value
                         _type.HRESULT]


class _IEventHandler(_Template):
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       _T],  # args
                      _type.HRESULT]


class IEventHandler(_IEventHandler, _Generic[_T], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IEventHandler_impl(_IEventHandler, _Generic[_T], _Unknwnbase.IUnknown_impl):
    pass


class _ITypedEventHandler(_Template):
    Invoke: _Callable[[_TSender,  # sender
                       _TArgs],  # args
                      _type.HRESULT]


class ITypedEventHandler(_ITypedEventHandler, _Generic[_TSender, _TArgs], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITypedEventHandler_impl(_ITypedEventHandler, _Generic[_TSender, _TArgs], _Unknwnbase.IUnknown_impl):
    pass
''',
    "Windows.Foundation.Collections": '''
class IIterator(_Template, _Generic[_T], _inspectable.IInspectable):
    get_Current: _Callable[[_Pointer[_T]],  # current
                           _type.HRESULT]
    get_HasCurrent: _Callable[[_Pointer[_type.boolean]],  # hasCurrent
                              _type.HRESULT]
    MoveNext: _Callable[[_Pointer[_type.boolean]],  # hasCurrent
                        _type.HRESULT]
    GetMany: _Callable[[_type.c_uint,  # capacity
                        _Pointer[_T],  # value
                        _Pointer[_type.c_uint]],  # actual
                       _type.HRESULT]


class IIterable(_Template, _Generic[_T], _inspectable.IInspectable):
    First: _Callable[[_Pointer[IIterator[_T]]],  # first
                     _type.HRESULT]


class IVectorView(_Template, _Generic[_T], _inspectable.IInspectable):
    GetAt: _Callable[[_type.c_uint,  # index
                      _Pointer[_T]],  # item
                     _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    IndexOf: _Callable[[_T,  # value
                        _Pointer[_type.c_uint],  # index
                        _Pointer[_type.boolean]],  # found
                       _type.HRESULT]
    GetMany: _Callable[[_type.c_uint,  # startIndex
                        _type.c_uint,  # capacity
                        _Pointer[_T],  # value
                        _Pointer[_type.c_uint]],  # actual
                       _type.HRESULT]


class IVector(_Template, _Generic[_T], _inspectable.IInspectable):
    GetAt: _Callable[[_type.c_uint,  # index
                      _Pointer[_T]],  # item
                     _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    GetView: _Callable[[_Pointer[IVectorView[_T]]],  # view
                       _type.HRESULT]
    IndexOf: _Callable[[_T,  # value
                        _Pointer[_type.c_uint],  # index
                        _Pointer[_type.boolean]],  # found
                       _type.HRESULT]
    SetAt: _Callable[[_type.c_uint,  # index
                      _T],  # item
                     _type.HRESULT]
    InsertAt: _Callable[[_type.c_uint,  # index
                         _T],  # item
                        _type.HRESULT]
    RemoveAt: _Callable[[_type.c_uint],  # index
                        _type.HRESULT]
    Append: _Callable[[_T],  # item
                      _type.HRESULT]
    RemoveAtEnd: _Callable[[],
                           _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    GetMany: _Callable[[_type.c_uint,  # startIndex
                        _type.c_uint,  # capacity
                        _Pointer[_T],  # value
                        _Pointer[_type.c_uint]],  # actual
                       _type.HRESULT]
    ReplaceAll: _Callable[[_type.c_uint,  # count
                           _Pointer[_T]],  # value
                          _type.HRESULT]


class IKeyValuePair(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    get_Key: _Callable[[_Pointer[_K]],  # key
                       _type.HRESULT]
    get_Value: _Callable[[_Pointer[_V]],  # value
                         _type.HRESULT]


class IMapView(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    Lookup: _Callable[[_K,  # key
                       _Pointer[_V]],  # value
                      _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    HasKey: _Callable[[_K,  # key
                       _Pointer[_type.boolean]],  # found
                      _type.HRESULT]
    Split: _Callable[[_Pointer[IMapView[_K, _V]],  # firstPartition
                      _Pointer[IMapView[_K, _V]]],  # secondPartition
                     _type.HRESULT]


class IMap(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    Lookup: _Callable[[_K,  # key
                       _Pointer[_V]],  # value
                      _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.c_uint]],  # size
                        _type.HRESULT]
    HasKey: _Callable[[_K,  # key
                       _Pointer[_type.boolean]],  # found
                      _type.HRESULT]
    GetView: _Callable[[_Pointer[IMapView[_K, _V]]],  # view
                       _type.HRESULT]
    Insert: _Callable[[_K,  # key
                       _V,  # value
                       _Pointer[_type.boolean]],  # replaced
                      _type.HRESULT]
    Remove: _Callable[[_K],  # key
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class _IVectorChangedEventHandler(_Template):
    Invoke: _Callable[[IObservableVector[_T],  # sender
                       IVectorChangedEventArgs],  # e
                      _type.HRESULT]


class IVectorChangedEventHandler(_IVectorChangedEventHandler, _Generic[_T], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IVectorChangedEventHandler_impl(_IVectorChangedEventHandler, _Generic[_T], _Unknwnbase.IUnknown_impl):
    pass


class IObservableVector(_Template, _Generic[_T], _inspectable.IInspectable):
    add_VectorChanged: _Callable[[IVectorChangedEventHandler[_T],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_VectorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IMapChangedEventArgs(_Template, _Generic[_K], _inspectable.IInspectable):
    get_CollectionChange: _Callable[[_Pointer[_enum.Windows.Foundation.Collections.CollectionChange]],  # value
                                    _type.HRESULT]
    get_Key: _Callable[[_Pointer[_K]],  # value
                       _type.HRESULT]


class _IMapChangedEventHandler(_Template):
    Invoke: _Callable[[IObservableMap[_K, _V],  # sender
                       IMapChangedEventArgs[_K]],  # e
                      _type.HRESULT]


class IMapChangedEventHandler(_IMapChangedEventHandler, _Generic[_K, _V], _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IMapChangedEventHandler_impl(_IMapChangedEventHandler, _Generic[_K, _V], _Unknwnbase.IUnknown_impl):
    pass


class IObservableMap(_Template, _Generic[_K, _V], _inspectable.IInspectable):
    add_MapChanged: _Callable[[IMapChangedEventHandler[_K, _V],  # handler
                               _Pointer[_struct.EventRegistrationToken]],  # token
                              _type.HRESULT]
    remove_MapChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]


class IVectorChangedEventArgs(_inspectable.IInspectable):
    get_CollectionChange: _Callable[[_Pointer[_enum.Windows.Foundation.Collections.CollectionChange]],
                                    _type.HRESULT]
    get_Index: _Callable[[_Pointer[_type.c_uint]],
                         _type.HRESULT]
'''}
GEN_DOC = True

_CURRENT: list[str] = []
_FACTORIES: set[str] = set()
_REL_IMPORTS: list[str] = []


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


def _sort(comp: Callable[[str, Any], bool], datas: dict):
    pops = []
    for name, data in datas.items():
        if comp(name, data):
            pops.append(name)
            # _sort(comp, data)
    pops.sort()
    for name in pops:
        datas[name] = datas.pop(name)


sort_enum = functools.partial(_sort, lambda _, data: isinstance(next(iter(data.values())), dict))
sort_struct = sort_enum
sort_iid = functools.partial(_sort, lambda _, data: isinstance(data, dict))
sort_interface = functools.partial(_sort, lambda name, _: isinstance(name, str))
sort_runtimeclass = sort_iid


def add_ptr(type_: str, count: int) -> str:
    return f'{"_Pointer[" * count}{type_}{"]" * count}'


def resolve_type(type_: str, this: str = '', interfaces: Optional[dict] = None,
                 runtimeclasses: Optional[dict] = None, re_bracket=re.compile('<(.*)>')) -> str:
    ptr_c = 0
    while type_.endswith('*'):
        ptr_c += 1
        type_ = type_[:-1]
    try:
        type_ = TYPE_MAP[type_]
    except KeyError:
        pass
    else:
        return add_ptr(type_, ptr_c - 1)
    if type_ == 'AsyncStatus':
        return add_ptr(f'{"_enum." * (this != "enum")}Windows.Foundation.AsyncStatus', ptr_c)
    if runtimeclasses:
        runtimeclass = runtimeclasses
        for namespace in type_.split('.'):
            try:
                runtimeclass = runtimeclass[namespace]
            except KeyError:
                break
        else:
            type_ = runtimeclass[2][runtimeclass[3]]
    for name in ('type', 'enum', 'struct'):
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
            args = [resolve_type(type__, this, interfaces, runtimeclasses) for type__ in get_params(match.groups()[0])]
            if '.'.join(namespaces) == _CURRENT[-1]:
                namespace = ''
            else:
                namespace = f'_{"_".join(namespaces)}.'
            return add_ptr(f'{namespace}{"I" * (1 - name.startswith("I"))}{name}{args}'.replace("'", ''), ptr_c - 1)
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
                    ns, cls = i_type.rsplit('.', 1)
                    if ns == _CURRENT[-1]:
                        i_type = cls
                    else:
                        i_type = f'_{ns.replace(".", "_")}.{cls}'
                    return add_ptr(i_type, ptr_c - 1)
    warnings.warn(type_)
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


def get_text(soup: bs4.BeautifulSoup, text: str, extra='') -> str:
    texts = []
    if h2 := soup.find('h2', string=text):
        for ele in h2.find_next_siblings():
            # noinspection PyUnresolvedReferences
            if ele.name == 'p':
                texts.append(ele.text)
            else:
                break
    return f'{extra}\n\n    {extra}'.join(texts)


def get_enum_text(soup: bs4.BeautifulSoup) -> dict[str, str]:
    texts = {}
    field = ''
    if h2 := soup.find('h2', string='-enum-fields'):
        'h3'
        for ele in h2.find_next_siblings():
            text = ele.text
            # noinspection PyUnresolvedReferences
            if text.startswith('-field'):
                try:
                    end = text.index(':')
                except ValueError:
                    end = None
                field = text[7:end]
                texts[field] = ''
            elif ele.name == 'p':
                if field:
                    texts[field] += f'\n\n    {text}'
            elif ele.name == 'blockquote':
                pass
            else:
                break
    for field, text in texts.items():
        texts[field] = text[6:]
    return texts


def get_doc(path: str) -> Optional[tuple[str, str, dict[str, str]]]:
    output = io.BytesIO()
    try:
        markdown.markdownFromFile(input=path, output=output)
    except FileNotFoundError:
        warnings.warn(path)
    else:
        soup = bs4.BeautifulSoup(output.getvalue().decode(), 'html.parser')
        # print(soup.prettify(), file=sys.stderr)
        return get_text(soup, '-description'), get_text(soup, '-remarks', '*'), get_enum_text(soup)


def print_enum(enums: dict, __namespaces: Optional[list[str]] = None):
    sort_enum(enums)
    if __namespaces is None:
        __namespaces = []
    indent = '    ' * len(__namespaces)
    namespace = '.'.join(__namespaces)
    doc_dir = ntpath.join(DOC_DIR, namespace)
    for name, value in enums.items():
        if isinstance(next(iter(value.values())), str):
            docs = None
            print(f'{indent}class {name}(_Enum):')
            if GEN_DOC and (doc_ := get_doc(ntpath.join(doc_dir, f'{name}.md'))):
                doc = ''
                if doc_[0]:
                    doc += f'\n**Description:**\n    {doc_[0]}\n\n'
                if doc_[1]:
                    doc += f'\n**Remarks:**\n    *{doc_[1]}*\n\n'
                docs = doc_[2]
                doc += f'\n**Documentation:**\n    `{namespace}.{name} <{DOC_LINK_PREFIX}{namespace.lower()}.{name.lower()}>`_\n\n'
                print(indent, '    ', f'\n{indent}    '.join(f'"""\n{doc.strip()}\n"""'.splitlines()), sep='')
            for name_, value_ in value.items():
                print(f'{indent}    {"None_" if name_ == "None" else name_} = {value_}')
                if GEN_DOC and docs is not None:
                    try:
                        print(indent, '    ', f'\n{indent}    '.join(f'"""\n{docs[name_]}\n"""'.splitlines()), sep='')
                    except KeyError:
                        print(f'{name}.{name_}', file=sys.stderr)
        else:
            __namespaces.append(name)
            print(f'{indent}class {name}:')
            print_enum(value, __namespaces)
            del __namespaces[-1]


def print_struct(structs: dict, indent: str = ''):
    sort_struct(structs)
    for name, value in structs.items():
        if isinstance(next(iter(value.values())), str):
            print(f'{indent}@_struct')
            print(f'{indent}class {name}:')
            for name_, value_ in value.items():
                print(f'{indent}    {name_}: {resolve_type(value_, "struct")}')
        else:
            print(f'{indent}class {name}:')
            print_struct(value, f'{indent}    ')


def print_iid(iids: dict, indent: str = ''):
    sort_iid(iids)
    for name, value in iids.items():
        if isinstance(value, dict):
            print(f'{indent}class {name}:')
            print_iid(value, f'{indent}    ')
        else:
            print(f'{indent}IID_{name} = \'{{{value}}}\'')


def print_interface(interfaces: dict, runtimeclasses: dict, folder: str, depth: int = 0, __interfaces=None):
    sort_interface(interfaces)
    if __interfaces is None:
        __interfaces = interfaces
    for name, value in interfaces.items():
        if isinstance(name, tuple):
            is_delegate = name[1] == 'IUnknown' and len(value) == 1 and 'Invoke' in value
            if is_delegate:
                print(f'class _{name[0]}:')
            else:
                print(f'class {name[0]}({TYPE_MAP[name[1]]}', end='')
                if f'{_CURRENT[-1]}.{name[0]}' in _FACTORIES:
                    print(', factory=True', end='')
                print('):')
            for func, (args, res) in value.items():
                q_final = f'    {func}: _Callable[[' + f',\n        '.join(
                    resolve_type(val, "interface", __interfaces, runtimeclasses) for val in args.values()) + '],'
                s_final = ''
                if args:
                    for line, kwarg in zip(q_final.splitlines(), args):
                        s_final += line + f'  # {kwarg}\n'
                else:
                    s_final += q_final + '\n'
                print(f'{s_final}        {resolve_type(res, "interface", __interfaces, runtimeclasses)}]')
            print()
            if not value:
                print('    pass')
            if is_delegate:
                print(f'class {name[0]}(_{name[0]}, {TYPE_MAP[name[1]]}):')
                print(f'    pass')
                print(f'# noinspection PyPep8Naming')
                print(f'class {name[0]}_impl(_{name[0]}, {TYPE_MAP[name[1]]}_impl):')
                print(f'    pass')
        else:
            n_folder = ntpath.join(folder, name)
            n_depth = depth + 1
            os.makedirs(n_folder, exist_ok=True)
            _CURRENT.append('.'.join(n_folder.rsplit(os.sep, n_depth)[-n_depth:]))
            with contextlib.redirect_stdout(open(ntpath.join(n_folder, '__init__.py'), 'w')):
                try:
                    print(DATA_INTERFACE[_CURRENT[-1]])
                except KeyError:
                    pass
                print_interface(value, runtimeclasses, n_folder, n_depth, __interfaces)
            del _CURRENT[-1]


def gen_rel_imports(interfaces: dict, __interfaces: Optional[list[str]] = None):
    if __interfaces is None:
        __interfaces = []
    else:
        _REL_IMPORTS.append('.'.join(__interfaces))
    for name, value in interfaces.items():
        if not isinstance(name, tuple):
            __interfaces.append(name)
            gen_rel_imports(value, __interfaces)
            del __interfaces[-1]


def patch_imports(folder: str):
    for cur_folder in _REL_IMPORTS:
        cur_ns = cur_folder.split('.')
        cur_dir = ntpath.join(folder, *cur_ns)
        cur_path = ntpath.join(cur_dir, '__init__.py')
        if ntpath.getsize(cur_path):
            imports = ABS_IMPORTS.copy()
            for ex_import in EX_IMPORTS:
                imports.append(f'from {"." * len(cur_ns)}{ex_import}')
            for import_folder in _REL_IMPORTS:
                if cur_folder != import_folder:
                    import_ns = import_folder.split('.')
                    import_as = f'_{"_".join(import_ns)}'
                    with open(cur_path) as cur:
                        if f'{import_as}.' not in cur.read():
                            continue
                    import_dir = ntpath.join(folder, *import_ns)
                    rel_parts = ntpath.relpath(import_dir, cur_path).split(os.sep)
                    if rel_parts[-1] == '..':
                        rel_parts.append('..')
                    else:
                        del rel_parts[-1]
                    rel = ''
                    for rel_part in rel_parts:
                        if rel_part == '..':
                            rel += '.'
                        else:
                            if not rel.endswith('.'):
                                rel += '.'
                            rel += rel_part
                    imports.append(f'from {rel} import {import_ns[-1]} as {import_as}')
            with open(cur_path) as cur:
                data = cur.read()
            with open(cur_path, 'w') as cur:
                for import_ in imports:
                    cur.write(f'{import_}\n')
                cur.write(data)


def print_runtimeclass(runtimeclasses: dict, __namespaces: Optional[list[str]] = None):
    sort_runtimeclass(runtimeclasses)
    if __namespaces is None:
        __namespaces = []
    indent = '    ' * len(__namespaces)
    namespace = '.'.join(__namespaces)
    doc_dir = ntpath.join(DOC_DIR, namespace)
    if GEN_DOC and (doc_ := get_doc(ntpath.join(doc_dir, f'{namespace.replace(".", "_")}.md'))):
        doc = ''
        if doc_[0]:
            doc += f'\n**Description:**\n    {doc_[0]}\n\n'
        # if doc_[1]:
        #     doc += f'\n**Remarks:**\n    *{doc_[1]}*\n\n'
        doc += f'\n**Documentation:**\n    `{namespace} <{DOC_LINK_PREFIX}{namespace.lower()}>`_\n\n'
        print(indent, f'\n{indent}'.join(f'"""\n{doc.strip()}\n"""'.splitlines()), sep='')
    for name, value in runtimeclasses.items():
        __namespaces.append(name)
        if isinstance(value, dict):
            print(f'{indent}class {name}:')
            print_runtimeclass(value, __namespaces)
        else:
            runtimeclass = '.'.join(__namespaces)
            print(f"{indent}{name} = '{runtimeclass}'")
            if GEN_DOC:
                doc = ''
                if doc_ := get_doc(ntpath.join(doc_dir, f'{name}.md')):
                    if doc_[0]:
                        doc += f'\n**Description:**\n    {doc_[0]}\n\n'
                    # if doc_[1]:
                    #     doc += f'\n**Remarks:**\n    *{doc_[1]}*\n\n'
                activatable, statics, interfaces, default_index = value
                if activatable:
                    if activatable is True:
                        activatable = runtimeclass
                    doc += f'\n**Activatable:**\n    ``{activatable}``\n\n'
                if statics:
                    doc += f'\n**Statics:**\n'
                    for static in statics:
                        doc += f'    ``{static}``\n\n'
                if interfaces:
                    doc += f'\n**Interfaces:**\n'
                    for index, interface in enumerate(interfaces):
                        doc += f'    ``{interface}``'
                        if index == default_index:
                            doc += ' *****'
                        doc += '\n\n'
                if doc_:
                    doc += f'\n**Documentation:**\n    `{runtimeclass} <{DOC_LINK_PREFIX}{runtimeclass.lower()}>`_\n\n'
                print(indent, f'\n{indent}'.join(f'"""\n{doc.strip()}\n"""'.splitlines()), sep='')
        del __namespaces[-1]


def dump(*, p_enum: bool = False, p_struct: bool = False, p_iid: bool = False,
         p_interface: bool = False, p_runtimeclass: bool = False, o_interface: str = ''):
    data = ''
    for file in glob.glob(ntpath.join(SDK_PATH, 'winrt', '*.idl')):  # TODO include form import
        if '.' in ntpath.splitext(ntpath.basename(file))[0]:
            with open(file) as stream:
                data += f'\n{stream.read()}'

    re_namespace = re.compile(r'namespace (\S+)')  # namespace Microsoft
    re_enum = re.compile(r'enum (\S+)')  # enum MapRouteOptimization
    re_enum_member = re.compile(r'(\S+)(\s*)=\s((0x)?\d*),?')  # Toll    = 0x1,
    re_struct = re.compile(r'struct (\S+)')
    re_struct_field = re.compile(r'(\S+)\s(.*);')
    re_version = re.compile(r'\[version\((.*)\)]')  # [version(0x00000001)]
    re_iid = re.compile(r'\[uuid\(([\dA-F]{8}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{4}-[\dA-F]{12})\)]')  # [uuid(CC107CDC-558F-5D1A-96A5-A735AC04386B)]
    re_delegate = re.compile(r'delegate')
    re_interface = re.compile(r'interface (\S+) : (\S+)')  # interface ICompositorController : IInspectable
    re_func = re.compile(r'(\S+) (\S+?)\((.*)\);')
    re_template = re.compile(r'declare')
    re_runtimeclass = re.compile(r'runtimeclass (\S+)')  # runtimeclass EnhancedWaypoint
    re_runtimeclass_interface = re.compile(r'interface (.*);')  # interface Windows.Services.Maps.IMapLocation;
    re_attribute = re.compile(r'attribute (\S+)')
    re_contract = re.compile(r'apicontract (\S+)')
    re_activatable = re.compile(r'\[activatable\((\S+), \S+ \d*\.\d*\)]')  # [activatable(Windows.Services.Maps.IEnhancedWaypointFactory, Windows.Foundation.UniversalApiContract, 4.0)]
    re_static = re.compile(r'\[static\((\S+), (\S+) \d*\.\d\)]')

    enums = {}
    structs = {}
    iids = {}
    interfaces = {}
    runtimeclasses = {}

    for enum, value in EX_ENUMS.items():
        *namespaces, name = enum.split('.')
        get_datas(enums, namespaces)[name] = value

    line_num = 0
    namespaces = []
    lines = data.splitlines()
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
                    if match_ := re_enum_member.fullmatch(line_.strip()):
                        enum[match_.groups()[0]] = match_.groups()[2]
                get_datas(enums, namespaces)[match.groups()[0]] = enum
        elif match := re_struct.fullmatch(line):
            struct = {}
            if end := find_end(lines, line_num):
                start = line_num + 2
                line_num = end
                for line_ in lines[start:end]:
                    if match_ := re_struct_field.fullmatch(line_.strip()):
                        struct[match_.groups()[1]] = match_.groups()[0]
                get_datas(structs, namespaces)[match.groups()[0]] = struct
        elif re_delegate.fullmatch(line):
            line_ = lines[line_num + 1].strip()
            match_ = re_func.fullmatch(line_[line_.find('HRESULT'):])
            func = f'I{match_.groups()[1]}'
            get_datas(iids, namespaces)[func] = re_iid.fullmatch(lines[line_num - 1].strip()).groups()[0]
            get_datas(interfaces, namespaces)[(func, 'IUnknown')] = {'Invoke': (get_args(match_.groups()[2]), match_.groups()[0])}
        elif match := re_interface.fullmatch(line):
            line_ = lines[line_num - 1].strip()
            if re_version.fullmatch(line_):
                line_ = lines[line_num - 2].strip()
            get_datas(iids, namespaces)[match.groups()[0]] = re_iid.fullmatch(line_).groups()[0]
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
                line_num = end
        elif match := re_runtimeclass.search(line):
            if not line.endswith(';'):
                line_num_ = line_num - 1
                is_activatable = False
                activatable = None
                statics = []
                interfaces_ = []
                while line_ := lines[line_num_].strip():
                    if line_.startswith('[activatable('):
                        is_activatable = True
                    if activatable is None and (match_ := re_activatable.fullmatch(line_)):
                        activatable = match_.groups()[0]
                    elif match_ := re_static.fullmatch(line_):
                        statics.append(match_.groups()[0])
                    line_num_ -= 1
                if activatable is not None:
                    _FACTORIES.add(activatable)
                else:
                    activatable = is_activatable
                _FACTORIES.update(statics)
                if end := find_end(lines, line_num):
                    start = line_num + 2
                    line_num = end
                    default_index = None
                    for line_ in lines[start:end]:
                        if match_ := re_runtimeclass_interface.search(line_):
                            interfaces_.append(match_.groups()[0])
                            if line_.find('[default]') != -1:
                                default_index = len(interfaces_) - 1
                    get_datas(runtimeclasses, namespaces)[match.groups()[
                        0]] = activatable, tuple(reversed(statics)), tuple(interfaces_), default_index
        elif re_contract.fullmatch(line):
            if end := find_end(lines, line_num):
                line_num = end
        elif re_attribute.fullmatch(line):
            if end := find_end(lines, line_num):
                line_num = end
        elif line.startswith('}'):
            try:
                del namespaces[-1]
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
        o_interface = ntpath.realpath(o_interface)
        gen_rel_imports(interfaces)
        print_interface(interfaces, runtimeclasses, o_interface)
        patch_imports(o_interface)
    if p_runtimeclass:
        print_runtimeclass(runtimeclasses)
    # with open('runtimeclass.json', 'w') as file, contextlib.redirect_stdout(file):
    #     print(json.dumps(runtimeclasses, indent=4))


def dump_idl(pattern: str):
    winmdidl = ntpath.join(WINMDIDL_DIR, 'winmdidl.exe')
    output = f'/outdir:{ntpath.realpath("winrt")}'
    with tempfile.TemporaryDirectory() as temp:
        for winmd in glob.glob(pattern, recursive=True):
            shutil.copy(winmd, ntpath.join(temp, ntpath.basename(winmd)))
        for file in glob.glob(ntpath.join(temp, '*.winmd')):
            args = winmdidl, output, r'/metadata_dir:C:\Windows\System32\WinMetadata', file
            print(args)
            subprocess.run(args)


def main():
    # dump_idl(r'D:\Projects\wallpyper\helpers\microsoft.windowsappsdk.1.4.230913002\**\*.winmd')
    with open('idl.py', 'w', encoding='utf-8') as file, contextlib.redirect_stdout(file):
        pass
        # dump(p_enum=True)
        # dump(p_struct=True)
        # dump(p_iid=True)
        dump(p_runtimeclass=True)
    # dump(p_interface=True, o_interface='output')


if __name__ == '__main__':
    main()
