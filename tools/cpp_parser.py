import functools
import itertools
import os
import pathlib
import re
import textwrap
import uuid
from typing import Callable
from typing import Iterable
from typing import Iterator
from typing import Optional

import clang.cindex

from libs import ctyped
from libs.ctyped.enum import libclang as enum_libclang
from libs.ctyped.lib import libclang

SOURCE_PATH = r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\winrt\RoMetadataApi.h'
INCLUDES = ('<Windows.h>',)
INCLUDE_DIRS = ()
CLANG_DIR = r'C:\msys64\mingw64\bin'
DEFINITIONS = {
    '__unaligned': '',
    '__cplusplus': '199711L',
    '__int8': 'signed char',
    '__int16': 'short',
    '__int32': 'int',
    '__int64': 'long long',
    '_UNICODE': 1,
    'UNICODE': 1,
    '_WININET_': 1,
    'DECLSPEC_IMPORT': '__declspec(dllimport)',
    'CALLBACK': '__stdcall',
    'WINAPI': '__stdcall',
    'WINAPIV': '__cdecl',
    'APIENTRY': 'WINAPI',
    'APIPRIVATE': '__stdcall',
    'PASCAL': '__stdcall',
    'WINAPI_INLINE': 'WINAPI',
    'INITGUID': 1,
    'GDIPVER': '0x0110'}
CLANG_INCLUDE_DIRS = r'C:\msys64\mingw64\include',
MSVC_INCLUDE_DIRS = (
    r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\shared',
    r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\ucrt',
    r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\um',
    r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\winrt')
VCPKG_INCLUDE_DIRS = r'D:\Projects\vcpkg\installed\x64-windows\include',

ENUM = False
FUNCTION = False
INTERFACE = False
GUID = True
AST = False

CLANG = False
MSVC = True
VCPKG = False

COMMENT = True
INDENT = ' ' * 4
ENUM_DECL = 'class {}(_Enum):'
ENUM_CONSTANT_DECL = '{} = {}'
FUNCTION_DECL_START = '{}: _Callable[['
FUNCTION_DECL_END = '{}]'
INTERFACE_DECL = 'class {}({}):'
INTERFACE_DECL_DELEGATE = 'class _{}:'
DELEGATE_DECL = f'class {{0}}(_{{0}}, {{1}}):\n{INDENT}pass\n# noinspection PyPep8Naming\nclass {{0}}_impl(_{{0}}, {{1}}_impl):\n{INDENT}pass'
KIND_ENUM = '_enum.{}'
KIND_UNION = '_union.{}'
KIND_STRUCT = '_struct.{}'
KIND_INTERFACE = '_{}.{}'

_TYPE_PTR = {
    'PINT': 'c_int',
    'LPINT': 'c_int',
    'LPLONG': 'c_long',
    'PUINT': 'c_uint',
    'LPUINT': 'UINT',
    'PFLOAT': 'FLOAT',
    'PSHORT': 'SHORT',
    'PUSHORT': 'USHORT',
    'PUCHAR': 'UCHAR',
    'PLONG': 'LONG',
    'PULONG': 'ULONG',
    'LPBYTE': 'BYTE',
    'LPDWORD': 'DWORD',
    'PDWORD': 'DWORD',
    'LPWORD': 'WORD',
    'PWORD': 'WORD',
    'PBOOL': 'BOOL',
    'PBOOLEAN': 'BOOLEAN',
    'PDWORDLONG': 'DWORDLONG',
    'PULONGLONG': 'ULONGLONG',
    'PDWORD64': 'DWORD64',
    'PHKEY': 'HKEY',
    'LPGUID': 'GUID',
    'LPCGUID': 'GUID',
    'LPRECT': 'RECT',
    'LPCRECT': 'RECT',
    'LPRECTL': 'RECTL',
    'LPCRECTL': 'RECTL',
    'LPPOINT': 'POINT',
    'LPCPOINT': 'POINT',
    'LPPOINTL': 'POINTL',
    'LPCPOINTL': 'POINTL',
    'LPSIZE': 'SIZE',
    'LPCSIZE': 'SIZE',
    'LPSIZEL': 'SIZEL',
    'LPCSIZEL': 'SIZEL',
    'PSIZE_T': 'SIZE_T',
    'PHANDLE': 'HANDLE',
    'LPHANDLE': 'HANDLE',
    'PULONG_PTR': 'ULONG_PTR',
    'PLONG_PTR': 'LONG_PTR',
    'PDWORD_PTR': 'DWORD_PTR'}
_TYPE_KIND = {
    clang.cindex.TypeKind.UINT: 'c_uint',
    clang.cindex.TypeKind.ULONG: 'c_ulong',
    clang.cindex.TypeKind.ULONGLONG: 'c_ulonglong',
    clang.cindex.TypeKind.LONGLONG: 'c_longlong',
    clang.cindex.TypeKind.LONGDOUBLE: 'c_longdouble'}

_TFunctionData = tuple[clang.cindex.Type, list[tuple[clang.cindex.Type, str]], Optional[str]]


# noinspection PyShadowingBuiltins
def find_cursor(cursors: clang.cindex.Cursor | Iterable[clang.cindex.Cursor],
                kind: Optional[int | clang.cindex.CursorKind | Callable[[clang.cindex.CursorKind], bool]] = None,
                spelling: Optional[str | re.Pattern | Callable[[str], bool]] = None,
                location: Optional[str | clang.cindex.SourceLocation | Callable[[clang.cindex.SourceLocation], bool]] = None,
                type: Optional[int | clang.cindex.TypeKind | Callable[[clang.cindex.Type], bool]] = None,
                filter: Optional[Callable[[clang.cindex.Cursor], bool]] = None,
                recursive: bool = True) -> Optional[clang.cindex.Cursor]:
    for cursor in find_cursors(cursors, kind, spelling, location, type, filter, recursive):
        return cursor


# noinspection PyShadowingBuiltins
def find_cursors(cursors: clang.cindex.Cursor | Iterable[clang.cindex.Cursor],
                 kind: Optional[int | clang.cindex.CursorKind | Callable[[clang.cindex.CursorKind], bool]] = None,
                 spelling: Optional[str | re.Pattern | Callable[[str], bool]] = None,
                 location: Optional[str | clang.cindex.SourceLocation | Callable[[clang.cindex.SourceLocation], bool]] = None,
                 type: Optional[int | clang.cindex.TypeKind | Callable[[clang.cindex.Type], bool]] = None,
                 filter: Optional[Callable[[clang.cindex.Cursor], bool]] = None,
                 recursive: bool = True) -> Iterator[clang.cindex.Cursor]:
    if isinstance(cursors, clang.cindex.Cursor):
        cursors = cursors.get_children()
    for cursor in cursors:
        skip = False
        if not skip and kind is not None:
            if isinstance(kind, int):
                skip = kind != cursor.kind.value
            elif isinstance(kind, clang.cindex.CursorKind):
                skip = kind != cursor.kind
            else:
                skip = not kind(cursor.kind)
        if not skip and type is not None:
            if isinstance(type, int):
                skip = type != cursor.type.kind.value
            elif isinstance(type, clang.cindex.TypeKind):
                skip = type != cursor.type.kind
            else:
                skip = not type(cursor.type)
        if not skip and spelling is not None:
            if isinstance(spelling, str):
                skip = spelling != cursor.spelling
            elif isinstance(spelling, re.Pattern):
                skip = not bool(spelling.fullmatch(cursor.spelling))
            else:
                skip = not spelling(cursor.spelling)
        if not skip and location is not None:
            if isinstance(location, str):
                skip = cursor.location.file is None or location != cursor.location.file.name
            elif isinstance(location, clang.cindex.SourceLocation):
                skip = location != cursor.location
            else:
                skip = not location(cursor.location)
        if not skip and filter is not None:
            skip = not filter(cursor)
        if not skip:
            yield cursor
        if recursive:
            yield from find_cursors(cursor.get_children(), kind, spelling, location, type, filter, recursive)


def _unpack_typedef(cursor: clang.cindex.Cursor) -> clang.cindex.Cursor:
    while cursor.kind == clang.cindex.CursorKind.TYPEDEF_DECL:
        cursor = cursor.underlying_typedef_type.get_declaration()
    return cursor


def _eval_literal(cursor: ctyped.struct.CXCursor | clang.cindex.Cursor) -> Optional[int | float | str]:
    if not isinstance(cursor, ctyped.struct.CXCursor):
        cursor = ctyped.struct.CXCursor(cursor.kind.value, cursor.xdata, cursor.data)
    res = libclang.clang_Cursor_Evaluate(cursor)
    try:
        kind = libclang.clang_EvalResult_getKind(res)
        if kind == enum_libclang.CXEvalResultKind.Int:
            if libclang.clang_EvalResult_isUnsignedInt(res):
                return libclang.clang_EvalResult_getAsUnsigned(res)
            else:
                return libclang.clang_EvalResult_getAsLongLong(res)
        elif kind == enum_libclang.CXEvalResultKind.Float:
            return libclang.clang_EvalResult_getAsDouble(res)
        elif kind == enum_libclang.CXEvalResultKind.StrLiteral:
            return libclang.clang_EvalResult_getAsStr(res)
    finally:
        if res:
            libclang.clang_EvalResult_dispose(res)


def _same_location(location: str, source_location: clang.cindex.SourceLocation) -> bool:
    return source_location.file is not None and os.path.realpath(location) == os.path.realpath(source_location.file.name)


def is_enum(cursor: clang.cindex.Cursor) -> bool:
    return _unpack_typedef(cursor).kind == clang.cindex.CursorKind.ENUM_DECL


def is_union(cursor: clang.cindex.Cursor) -> bool:
    return _unpack_typedef(cursor).kind == clang.cindex.CursorKind.UNION_DECL


def is_struct(cursor: clang.cindex.Cursor) -> bool:
    return _unpack_typedef(cursor).kind == clang.cindex.CursorKind.STRUCT_DECL


def is_interface(cursor: clang.cindex.Cursor) -> bool:
    if cursor.spelling == 'IUnknown':
        return True
    for cursor_child in _unpack_typedef(cursor).get_children():
        if cursor_child.kind == clang.cindex.CursorKind.CXX_BASE_SPECIFIER:
            return is_interface(cursor_child.type.get_declaration())
        else:
            break
    return False


@functools.lru_cache
def _interface_location(path: str) -> str:
    return pathlib.Path(path).resolve().stem


def get_comment(raw_comment: str | Iterable[str]) -> str:
    if not isinstance(raw_comment, str):
        raw_comment = '\n'.join(raw_comment)
    index = clang.cindex.Index.create()
    unit = index.parse('comment.h', ('-fparse-all-comments',), (
        ('comment.h', f'{raw_comment}\nvoid comment();'),),
                       clang.cindex.TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION)
    return find_cursor(unit.cursor, spelling='comment').brief_comment


def str_comment(comment: str, indent: str = INDENT) -> str:
    return textwrap.indent('"""\n' + '\n'.join(
        textwrap.wrap(comment, 80)) + '\n"""', indent) + '\n'


def _str_pointer(spelling: str, count: int) -> str:
    for _ in range(count):
        spelling = f'_Pointer[{spelling}]'
    return spelling


# noinspection PyShadowingBuiltins
def str_type(type: clang.cindex.Type) -> str:
    count_pointer = 0
    while type.kind in (clang.cindex.TypeKind.POINTER, clang.cindex.TypeKind.LVALUEREFERENCE):
        count_pointer += 1
        type = type.get_pointee()
    while type.kind == clang.cindex.TypeKind.INCOMPLETEARRAY:
        count_pointer += 1
        type = type.get_array_element_type()
    spelling = type.spelling.removeprefix('const ').removeprefix(
        'enum ').removeprefix('struct ').removeprefix('union ')
    if type.kind == clang.cindex.TypeKind.TYPEDEF:
        canon = type.get_canonical()
        if canon.kind == clang.cindex.TypeKind.POINTER:
            pointee = canon.get_pointee()
            if pointee.kind == clang.cindex.TypeKind.RECORD:
                spelling_def = pointee.spelling
                if spelling_def.startswith('_'):
                    spelling_def = spelling_def[1:]
                elif spelling_def.startswith('tag'):
                    spelling_def = spelling_def[3:]
                else:
                    try:
                        spelling_def = _TYPE_PTR[spelling]
                    except KeyError:
                        spelling_def = ''
                if spelling_def:
                    return _str_pointer(KIND_STRUCT.format(spelling_def), count_pointer + 1)
    cursor = type.get_declaration()
    if is_interface(cursor):
        return _str_pointer(KIND_INTERFACE.format(_interface_location(
            type.get_declaration().location.file.name), spelling), count_pointer - 1)
    if is_enum(cursor):
        return _str_pointer(KIND_ENUM.format(spelling), count_pointer)
    if is_union(cursor):
        return _str_pointer(KIND_UNION.format(spelling), count_pointer)
    if is_struct(cursor):
        return _str_pointer(KIND_STRUCT.format(spelling), count_pointer)
    if type.kind == clang.cindex.TypeKind.VOID:
        if count_pointer:
            return f'_type.c_void_p'
        else:
            return f'_type.c_void'
    if count_pointer and spelling in ('char', 'wchar'):
        count_pointer -= 1
        spelling = f'{spelling}_p'
    try:
        spelling = _TYPE_PTR[spelling]
    except KeyError:
        pass
    else:
        count_pointer += 1
    try:
        spelling = _TYPE_KIND[type.kind]
    except KeyError:
        pass
    try:
        getattr(ctyped.type, spelling)
    except AttributeError:
        pass
    else:
        return _str_pointer(f'_type.{spelling}', count_pointer)
    try:
        getattr(ctyped.type, f'c_{spelling}')
    except AttributeError:
        pass
    else:
        return _str_pointer(f'_type.c_{spelling}', count_pointer)
    try:
        getattr(ctyped.enum, f'_{spelling}')
    except AttributeError:
        pass
    else:
        return _str_pointer(KIND_ENUM.format(spelling), count_pointer)
    if type.kind == clang.cindex.TypeKind.CONSTANTARRAY:
        return f'{str_type(type.get_array_element_type())} * {type.get_array_size()}'
    # print(type.kind, type.spelling)
    return f'TODO {_str_pointer(str(spelling), count_pointer)}'


def get_enums(cursor: clang.cindex.Cursor, **kwargs) -> dict[str, tuple[dict[str, tuple[int, Optional[str]]], Optional[str]]]:
    enums = {}
    for cursor in find_cursors(cursor.get_children(), clang.cindex.CursorKind.ENUM_DECL, **kwargs):
        if not cursor.spelling:
            cursor._spelling = f'_{uuid.uuid4().hex}'
        enum = {}
        comment = cursor.brief_comment
        if COMMENT and not comment:
            raw_comment = []
            for token in itertools.islice(cursor.get_tokens(), 2, None):
                if token.kind == clang.cindex.TokenKind.COMMENT:
                    raw_comment.append(token.spelling)
                else:
                    break
            comment = get_comment(raw_comment)
        enums[cursor.spelling] = enum, comment
        for cursor_enum in find_cursors(cursor.get_children(), clang.cindex.CursorKind.ENUM_CONSTANT_DECL, recursive=False):
            enum[cursor_enum.spelling] = cursor_enum.enum_value, cursor_enum.brief_comment
    return enums


def str_enum(spelling: str, data: tuple[dict[str, tuple[int, Optional[str]]], Optional[str]]) -> str:
    prefix = f'{spelling}_'
    formatted = f'{ENUM_DECL.format(spelling)}\n'
    if data[1]:
        formatted += str_comment(data[1])
    if data[0]:
        for enum_spelling, (value, comment) in data[0].items():
            enum_spelling_ = enum_spelling.removeprefix(prefix).removeprefix(spelling)
            if enum_spelling_ == 'None':
                enum_spelling_ += '_'
            formatted += f'{INDENT}{ENUM_CONSTANT_DECL.format(enum_spelling_, value)}\n'
            if comment:
                formatted += str_comment(comment)
    if not any(data):
        formatted += f'{INDENT}pass\n'
    return formatted[:-1]


def print_enums(unit: clang.cindex.TranslationUnit):
    for spelling, data in get_enums(unit.cursor, location=functools.partial(_same_location, SOURCE_PATH)).items():
        print(str_enum(spelling, data))


def _get_function_data(cursor: clang.cindex.Cursor) -> _TFunctionData:
    result, arguments = cursor.result_type, []
    for argument in cursor.get_arguments():
        arguments.append((argument.type, argument.spelling))
    return result, arguments, cursor.brief_comment


def get_functions(cursor: clang.cindex.Cursor, **kwargs) -> dict[str, _TFunctionData]:
    functions = {}
    for cursor in find_cursors(cursor.get_children(), clang.cindex.CursorKind.FUNCTION_DECL, **kwargs):
        functions[cursor.spelling] = _get_function_data(cursor)
    return functions


def str_function(spelling: str, data: _TFunctionData, depth: int = 0) -> str:
    indent = INDENT * depth
    formatted = f'{indent}{FUNCTION_DECL_START.format(spelling)}'
    args = data[1]
    if args:
        formatted_args = f'\n{indent}'.join(
            f'{str_type(arg_type)},{f"  # {arg_name}" if arg_name else ""}' for arg_type, arg_name in args[:-1])
        formatted += formatted_args + '\n' * bool(formatted_args)
        formatted += INDENT * (depth * bool(formatted_args))
        arg_name = args[-1][1]
        formatted += f'{str_type(args[-1][0])}],{f"  # {arg_name}" if arg_name else ""}\n'
    else:
        formatted += '],\n'
    formatted += f'{indent}{FUNCTION_DECL_END.format(str_type(data[0]))}\n'
    if data[2]:
        formatted += str_comment(data[2], indent)
    return formatted[:-1]


def print_functions(unit: clang.cindex.TranslationUnit):
    for spelling, data in get_functions(unit.cursor, location=functools.partial(_same_location, SOURCE_PATH)).items():
        print(str_function(spelling, data))


def get_interfaces(cursor: clang.cindex.Cursor, **kwargs) -> dict[str, tuple[Optional[clang.cindex.Type], dict[str, list[_TFunctionData]]]]:
    interfaces = {}
    for cursor in find_cursors(cursor.get_children(), clang.cindex.CursorKind.STRUCT_DECL, filter=is_interface, **kwargs):
        base = find_cursor(cursor.get_children(), clang.cindex.CursorKind.CXX_BASE_SPECIFIER)
        _, interface = interfaces[cursor.spelling] = (None if base is None else base.type), {}
        for cursor_method in find_cursors(cursor.get_children(), type=clang.cindex.TypeKind.FUNCTIONPROTO,
                                          filter=clang.cindex.Cursor.is_pure_virtual_method):
            interface.setdefault(cursor_method.spelling, []).insert(0, _get_function_data(cursor_method))
    # TODO rename inherited + overloaded
    return interfaces


def str_interface(spelling: str, data: tuple[Optional[clang.cindex.Type], dict[str, list[_TFunctionData]]], depth: int = 0) -> str:
    is_delegate = len(data[1]) == 1 and next(iter(data[1])) == 'Invoke'
    base = data[0]
    if base is None:
        str_base = ''
    else:
        str_base = KIND_INTERFACE.format(_interface_location(base.get_declaration().location.file.name), base.spelling)
    formatted = f'{INDENT * depth}{INTERFACE_DECL_DELEGATE.format(spelling) if is_delegate else INTERFACE_DECL.format(spelling, str_base)}\n'
    depth += 1
    for function_spelling, function_datas in data[1].items():
        spelling_suffix = ''
        for function_data in function_datas:
            formatted += f'{str_function(function_spelling + spelling_suffix, function_data, depth)}\n'
            spelling_suffix += '_'
    if not data[1]:
        formatted += f'{INDENT * depth}pass\n'
    if is_delegate:
        for line in DELEGATE_DECL.format(spelling, str_base).splitlines():
            formatted += f'\n{INDENT * (depth - 1)}{line}'
        formatted += '\n'
    return formatted


def print_interfaces(unit: clang.cindex.TranslationUnit):
    for spelling, data in get_interfaces(unit.cursor, location=functools.partial(_same_location, SOURCE_PATH)).items():
        print(str_interface(spelling, data))


def get_guids(cursor: clang.cindex.Cursor, **kwargs) -> dict[str, ctyped.struct.GUID]:
    guids = {}
    for cursor in find_cursors(cursor.get_children(), clang.cindex.CursorKind.VAR_DECL,
                               type=clang.cindex.TypeKind.TYPEDEF, **kwargs):
        if cursor.type.get_declaration().spelling == 'GUID':
            children = tuple(cursor.get_children())
            assert len(children) == 2
            grandchildren = tuple(children[1].get_children())
            assert len(grandchildren) == 4
            greatgrandchildren = tuple(grandchildren[3].get_children())
            assert len(greatgrandchildren) == 8
            guids[cursor.spelling] = ctyped.struct.GUID(*(_eval_literal(
                grandchildren[index]) for index in range(3)), ctyped.array(
                *(_eval_literal(greatgrandchildren[index]) for index in range(
                    8)), type=ctyped.type.c_uchar))
    return guids


def str_guid(spelling: str, data: ctyped.struct.GUID) -> str:
    return (f"{spelling} = '{{{data.Data1:08X}-{data.Data2:04X}-{data.Data3:04X}-"
            f"{''.join(f'{data.Data4[index]:02X}' for index in range(2))}-"
            f"{''.join(f'{data.Data4[index]:02X}' for index in range(2, 8))}}}'")


def print_guids(unit: clang.cindex.TranslationUnit):
    for spelling, data in get_guids(unit.cursor, location=functools.partial(_same_location, SOURCE_PATH)).items():
        print(str_guid(spelling, data))


def str_ast(cursor: clang.cindex.Cursor, depth: int = 0):
    spelling = cursor.spelling or '<spelling>'
    location = cursor.location
    file = location.file
    name = file.name if file is not None else '<file>'
    return f'{INDENT * depth}{cursor.kind.name} {spelling} {name} [{location.line}:{location.column}]'


def print_ast(cursor: clang.cindex.Cursor, depth: int = 0):
    print(str_ast(cursor, depth))
    for child in find_cursors(cursor.get_children(), location=functools.partial(_same_location, SOURCE_PATH), recursive=False):
        print_ast(child, depth + 1)


def main():
    clang.cindex.Config.set_library_path(CLANG_DIR)
    ctyped.lib.add_path(CLANG_DIR)
    index = clang.cindex.Index.create()
    args = ['-x', 'c++']
    include_dirs = [os.path.dirname(SOURCE_PATH), *INCLUDE_DIRS]
    if CLANG:
        include_dirs += CLANG_INCLUDE_DIRS
    if MSVC:
        include_dirs += MSVC_INCLUDE_DIRS
    if VCPKG:
        include_dirs += VCPKG_INCLUDE_DIRS
    for include_dir in include_dirs:
        args.append(f'-cxx-isystem{include_dir}')
    for macro, value in DEFINITIONS.items():
        args.append(f'-D{macro}={value}')
    if COMMENT:
        args.append('-fparse-all-comments')
    with open(SOURCE_PATH, encoding='utf-8') as file:
        source = file.read()
    for include in INCLUDES:
        source = f'#include {include}\n{source}'
    flags = (clang.cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD |
             clang.cindex.TranslationUnit.PARSE_INCOMPLETE |
             clang.cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
    if COMMENT:
        flags |= clang.cindex.TranslationUnit.PARSE_INCLUDE_BRIEF_COMMENTS_IN_CODE_COMPLETION
    unit = index.parse(SOURCE_PATH, args, ((SOURCE_PATH, source),), flags)
    if ENUM:
        print_enums(unit)
    if FUNCTION:
        print_functions(unit)
    if INTERFACE:
        print_interfaces(unit)
    if GUID:
        print_guids(unit)
    if AST:
        print_ast(unit.cursor)

    # for cursor in find_cursors(unit.cursor.get_children()):
    #     if cursor.spelling == 'MEDIASUBTYPE_None':
    #         print(cursor.kind, cursor.type.kind)
    #         extent = find_cursor(cursor.get_children(), clang.cindex.CursorKind.TYPE_REF).extent
    #         print(extent)
    #         start = extent.start
    #         end = extent.end
    #         with open(start.file.name) as file:
    #             lines = file.read().splitlines()
    #         source = lines[start.line - 2][start.column - 1:]
    #         for line in lines[start.line - 1:end.line - 2]:
    #             source += line
    #         if end.line != start.line:
    #             source += lines[end.line - 2][:end.column - 1]
    #         print(source)


if __name__ == '__main__':
    main()
