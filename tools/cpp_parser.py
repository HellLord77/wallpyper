import contextlib
import functools
import os
import pathlib
import re
import uuid
from typing import Iterable, Generator, Optional, Callable

import clang.cindex

from libs import ctyped

SOURCE_PATH = r'C:\Program Files (x86)\Windows Kits\10\Include\10.0.22621.0\um\DocObj.h'
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

ENUM = True
FUNCTION = False
INTERFACE = False
GUID = False

CLANG = False
MSVC = True
VCPKG = False

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

_TYPE_KIND = {
    clang.cindex.TypeKind.UINT: 'c_uint',
    clang.cindex.TypeKind.ULONG: 'c_ulong',
    clang.cindex.TypeKind.ULONGLONG: 'c_ulonglong',
    clang.cindex.TypeKind.LONGLONG: 'c_longlong',
    clang.cindex.TypeKind.LONGDOUBLE: 'c_longdouble'}


# noinspection PyShadowingBuiltins
def find_cursor(cursors: Iterable[clang.cindex.Cursor],
                kind: Optional[int | clang.cindex.CursorKind | Callable[[clang.cindex.CursorKind], bool]] = None,
                spelling: Optional[str | re.Pattern | Callable[[str], bool]] = None,
                location: Optional[str | clang.cindex.SourceLocation | Callable[[clang.cindex.SourceLocation], bool]] = None,
                type: Optional[int | clang.cindex.TypeKind | Callable[[clang.cindex.Type], bool]] = None,
                filter: Optional[Callable[[clang.cindex.Cursor], bool]] = None,
                recursive: bool = True) -> Optional[clang.cindex.Cursor]:
    for cursor in find_cursors(cursors, kind, spelling, location, type, filter, recursive):
        return cursor


# noinspection PyShadowingBuiltins
def find_cursors(cursors: Iterable[clang.cindex.Cursor],
                 kind: Optional[int | clang.cindex.CursorKind | Callable[[clang.cindex.CursorKind], bool]] = None,
                 spelling: Optional[str | re.Pattern | Callable[[str], bool]] = None,
                 location: Optional[str | clang.cindex.SourceLocation | Callable[[clang.cindex.SourceLocation], bool]] = None,
                 type: Optional[int | clang.cindex.TypeKind | Callable[[clang.cindex.Type], bool]] = None,
                 filter: Optional[Callable[[clang.cindex.Cursor], bool]] = None,
                 recursive: bool = True) -> Generator[clang.cindex.Cursor, None, None]:
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
    res = ctyped.lib.libclang.clang_Cursor_Evaluate(cursor)
    try:
        kind = ctyped.lib.libclang.clang_EvalResult_getKind(res)
        if kind == ctyped.enum.CXEvalResultKind.Int:
            if ctyped.lib.libclang.clang_EvalResult_isUnsignedInt(res):
                return ctyped.lib.libclang.clang_EvalResult_getAsUnsigned(res)
            else:
                return ctyped.lib.libclang.clang_EvalResult_getAsLongLong(res)
        elif kind == ctyped.enum.CXEvalResultKind.Float:
            return ctyped.lib.libclang.clang_EvalResult_getAsDouble(res)
        elif kind == ctyped.enum.CXEvalResultKind.StrLiteral:
            return ctyped.lib.libclang.clang_EvalResult_getAsStr(res)
    finally:
        if res:
            ctyped.lib.libclang.clang_EvalResult_dispose(res)


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
    if type.kind == clang.cindex.TypeKind.TYPEDEF:
        canon = type.get_canonical()
        if canon.kind == clang.cindex.TypeKind.POINTER:
            pointee = canon.get_pointee()
            if pointee.kind == clang.cindex.TypeKind.RECORD:
                spelling = pointee.spelling
                if spelling.startswith('_'):
                    spelling = spelling[1:]
                elif spelling.startswith('tag'):
                    spelling = spelling[3:]
                else:
                    spelling = ''
                if spelling:
                    return _str_pointer(KIND_STRUCT.format(spelling), count_pointer + 1)
    cursor = type.get_declaration()
    spelling = type.spelling.removeprefix('const ').removeprefix(
        'enum ').removeprefix('struct ').removeprefix('union ')
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
        spelling = _TYPE_KIND[type.kind]
    except KeyError:
        pass
    with contextlib.suppress(AttributeError):
        getattr(ctyped.type, spelling)
        return _str_pointer(f'_type.{spelling}', count_pointer)
    with contextlib.suppress(AttributeError):
        getattr(ctyped.type, f'c_{spelling}')
        return _str_pointer(f'_type.c_{spelling}', count_pointer)
    with contextlib.suppress(AttributeError):
        getattr(ctyped.enum, f'_{spelling}')
        return _str_pointer(KIND_ENUM.format(spelling), count_pointer)
    if type.kind == clang.cindex.TypeKind.CONSTANTARRAY:
        return f'{str_type(type.get_array_element_type())} * {type.get_array_size()}'
    # print(type.kind, type.spelling)
    return f'TODO {_str_pointer(str(spelling), count_pointer)}'


def get_enums(cursor: clang.cindex.Cursor, **kwargs) -> dict[str, dict[str, int]]:
    enums = {}
    for cursor in find_cursors(cursor.get_children(), clang.cindex.CursorKind.ENUM_DECL, **kwargs):
        if not cursor.spelling:
            cursor._spelling = f'_{uuid.uuid4().hex}'
        enum = enums[cursor.spelling] = {}
        for cursor_enum in find_cursors(cursor.get_children(), clang.cindex.CursorKind.ENUM_CONSTANT_DECL, recursive=False):
            enum[cursor_enum.spelling] = cursor_enum.enum_value
    return enums


def str_enum(spelling: str, data: dict[str, int]) -> str:
    prefix = f'{spelling}_'
    formatted = f'{ENUM_DECL.format(spelling)}\n'
    if data:
        for enum_spelling, value in data.items():
            formatted += f'{INDENT}{ENUM_CONSTANT_DECL.format(enum_spelling.removeprefix(prefix).removeprefix(spelling), value)}\n'
    else:
        formatted += f'{INDENT}pass\n'
    return formatted[:-1]


def print_enums(unit: clang.cindex.TranslationUnit):
    for spelling, data in get_enums(unit.cursor, location=functools.partial(_same_location, SOURCE_PATH)).items():
        print(str_enum(spelling, data))


def _get_function_types(cursor: clang.cindex.Cursor) -> tuple[clang.cindex.Type, list[tuple[clang.cindex.Type, str]]]:
    result, arguments = cursor.result_type, []
    for argument in cursor.get_arguments():
        arguments.append((argument.type, argument.spelling))
    return result, arguments


def get_functions(cursor: clang.cindex.Cursor, **kwargs) -> dict[str, tuple[clang.cindex.Type, list[tuple[clang.cindex.Type, str]]]]:
    functions = {}
    for cursor in find_cursors(cursor.get_children(), clang.cindex.CursorKind.FUNCTION_DECL, **kwargs):
        functions[cursor.spelling] = _get_function_types(cursor)
    return functions


def str_function(spelling: str, data: tuple[clang.cindex.Type, list[tuple[clang.cindex.Type, str]]], depth: int = 0) -> str:
    formatted = f'{INDENT * depth}{FUNCTION_DECL_START.format(spelling)}'
    args = data[1]
    if args:
        formatted_args = f'\n{INDENT * depth}'.join(
            f'{str_type(arg_type)},{f"  # {arg_name}" if arg_name else ""}' for arg_type, arg_name in args[:-1])
        formatted += formatted_args + '\n' * bool(formatted_args)
        formatted += INDENT * (depth * bool(formatted_args))
        arg_name = args[-1][1]
        formatted += f'{str_type(args[-1][0])}],{f"  # {arg_name}" if arg_name else ""}\n'
    else:
        formatted += '],\n'
    formatted += f'{INDENT * depth}{FUNCTION_DECL_END.format(str_type(data[0]))}\n'
    return formatted[:-1]


def print_functions(unit: clang.cindex.TranslationUnit):
    for spelling, data in get_functions(unit.cursor, location=functools.partial(_same_location, SOURCE_PATH)).items():
        print(str_function(spelling, data))


def get_interfaces(cursor: clang.cindex.Cursor, **kwargs) -> dict[str, tuple[Optional[clang.cindex.Type], dict[str, tuple[clang.cindex.Type, list[tuple[clang.cindex.Type, str]]]]]]:
    interfaces = {}
    for cursor in find_cursors(cursor.get_children(), clang.cindex.CursorKind.STRUCT_DECL, filter=is_interface, **kwargs):
        base = find_cursor(cursor.get_children(), clang.cindex.CursorKind.CXX_BASE_SPECIFIER)
        _, interface = interfaces[cursor.spelling] = (None if base is None else base.type), {}
        for cursor_method in find_cursors(cursor.get_children(), type=clang.cindex.TypeKind.FUNCTIONPROTO,
                                          filter=clang.cindex.Cursor.is_pure_virtual_method):
            interface[cursor_method.spelling] = _get_function_types(cursor_method)
    return interfaces


def str_interface(spelling: str, data: tuple[Optional[clang.cindex.Type], dict[str, tuple[clang.cindex.Type, list[tuple[clang.cindex.Type, str]]]]], depth: int = 0) -> str:
    is_delegate = len(data[1]) == 1 and next(iter(data[1])) == 'Invoke'
    base = data[0]
    if base is None:
        str_base = ''
    else:
        str_base = KIND_INTERFACE.format(_interface_location(base.get_declaration().location.file.name), base.spelling)
    formatted = f'{INDENT * depth}{INTERFACE_DECL_DELEGATE.format(spelling) if is_delegate else INTERFACE_DECL.format(spelling, str_base)}\n'
    depth += 1
    for function_spelling, function_data in data[1].items():
        formatted += f'{str_function(function_spelling, function_data, depth)}\n'
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


def main():
    os.add_dll_directory(CLANG_DIR)
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
    with open(SOURCE_PATH) as file:
        source = file.read()
    for include in INCLUDES:
        source = f'#include {include}\n{source}'
    flags = (clang.cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD |
             clang.cindex.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
    unit = index.parse(SOURCE_PATH, args, ((SOURCE_PATH, source),), flags)
    if ENUM:
        print_enums(unit)
    if FUNCTION:
        print_functions(unit)
    if INTERFACE:
        print_interfaces(unit)
    if GUID:
        print_guids(unit)

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
