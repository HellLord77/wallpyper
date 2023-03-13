from __future__ import annotations as _

import array
import collections.abc
import contextlib
import dataclasses
import datetime
import decimal
import enum
import fractions
import ipaddress
import json
import os
import pathlib
import re
import sys
import time
import typing
import uuid
from types import ModuleType, NoneType
from typing import AnyStr, Callable, ItemsView, Literal, Mapping, Optional, Tuple, TypeVar, TypedDict, List, Dict, Iterator
from xml.etree import ElementTree

import win32
from libs import ctyped, typed, config, soup
from libs.ctyped.const import error
from libs.ctyped.lib import kernel32, oleaut32, user32, python
from win32 import _utils


def _get_context_compatibility(path: Optional[str] = None) -> tuple[ctyped.struct.COMPATIBILITY_CONTEXT_ELEMENT, ...]:
    compatibility = ()
    if path is None:
        handle = ctyped.type.HANDLE()
        kernel32.GetCurrentActCtx(ctyped.byref(handle))
    else:
        ctx = ctyped.struct.ACTCTXW(lpSource=path)
        handle = kernel32.CreateActCtxW(ctyped.byref(ctx))
    flag = ctyped.enum.ACTIVATION_CONTEXT_INFO_CLASS.CompatibilityInformationInActivationContext
    sz = ctyped.type.SIZE_T()
    if not kernel32.QueryActCtxW(
            ctyped.const.QUERY_ACTCTX_FLAG_NO_ADDREF, handle, None, flag, None, 0,
            ctyped.byref(sz)) and kernel32.GetLastError() == error.ERROR_INSUFFICIENT_BUFFER:
        buff = kernel32.HeapAlloc(kernel32.GetProcessHeap(), ctyped.const.HEAP_ZERO_MEMORY, sz)
        if kernel32.QueryActCtxW(
                ctyped.const.QUERY_ACTCTX_FLAG_NO_ADDREF, handle, None, flag, buff, sz, ctyped.byref(sz)):
            info = ctyped.cast(buff, ctyped.struct.ACTIVATION_CONTEXT_COMPATIBILITY_INFORMATION).contents
            compatibility = (*ctyped.resize_array(info.Elements, info.ElementCount),)
        if buff:
            kernel32.HeapFree(kernel32.GetProcessHeap(), 0, buff)
    kernel32.ReleaseActCtx(handle)
    return compatibility


# def _test_font():
#     bitmap = gdiplus.Bitmap.from_dimension(100, 100)
#     with win32._utils.get_d2d1_dc_render_target() as target, ctyped.interface.COM[
#         dwrite.IDWriteFactory]() as factory, ctyped.interface.COM[
#         dwrite.IDWriteTextFormat]() as text_format, ctyped.interface.COM[
#         d2d1.ID2D1SolidColorBrush]() as brush, gdiplus.Graphics.from_image(bitmap).get_managed_hdc() as hdc:
#         if target and ctyped.macro.SUCCEEDED(ctyped.lib.DWrite.DWriteCreateFactory(ctyped.enum.DWRITE_FACTORY_TYPE.ISOLATED, ctyped.byref(
#                 ctyped.get_guid(ctyped.const.IID_IDWriteFactory)), ctyped.byref(factory))):
#             factory.CreateTextFormat("Comic Sans MS", ctyped.NULLPTR, ctyped.enum.DWRITE_FONT_WEIGHT.NORMAL, ctyped.enum.DWRITE_FONT_STYLE.NORMAL,
#                                      ctyped.enum.DWRITE_FONT_STRETCH.NORMAL, 16, "en-US", ctyped.byref(text_format))
#             print(text_format.GetFontSize())
#             col = ctyped.struct.D3DCOLORVALUE(1, 0, 0, 1)
#             print(target.CreateSolidColorBrush(ctyped.byref(col), ctyped.NULLPTR, ctyped.byref(brush)))
#             rect2 = ctyped.struct.RECT(0, 0, 100, 100)
#             rect = ctyped.struct.D2D_RECT_F(0, 0, 100, 100)
#             target.BindDC(hdc, ctyped.byref(rect2))
#             text = 'Hello World!'
#             target.BeginDraw()
#             target.DrawText(text, len(text), text_format, ctyped.byref(rect), brush,
#                             ctyped.enum.D2D1_DRAW_TEXT_OPTIONS.ENABLE_COLOR_FONT, ctyped.enum.DWRITE_MEASURING_MODE.NATURAL)
#             target.EndDraw(ctyped.NULLPTR, ctyped.NULLPTR)
#     gdiplus.image_save(bitmap, 'd:\\test.png')


PageAddress = TypeVar('PageAddress', bound=int)
FunctionAddress = TypeVar('FunctionAddress', bound=int)


class Thread(ctyped.type.HANDLE):
    @classmethod
    def create_remote(cls, proc, target: FunctionAddress,
                      arg: Optional[int] = None, suspended: bool = False) -> Thread:
        return cls(kernel32.CreateRemoteThread(proc, None, 0, ctyped.type.LPTHREAD_START_ROUTINE(target), arg, suspended * ctyped.const.CREATE_SUSPENDED, None))

    def set_priority(self, priority: int) -> bool:
        return bool(kernel32.SetThreadPriority(self, priority))

    def set_priority_boost(self, boost: bool = True) -> bool:
        return bool(kernel32.SetThreadPriorityBoost(self, not boost))

    def get_priority_boost(self) -> Optional[bool]:
        boost = ctyped.type.BOOL()
        if kernel32.GetThreadPriorityBoost(self, ctyped.byref(boost)):
            return not boost.value

    def get_priority(self) -> int:
        return kernel32.GetThreadPriority(self)

    def terminate(self, exit_code: int) -> bool:
        return bool(kernel32.TerminateThread(self, exit_code))

    def get_exit_code(self) -> Optional[int]:
        exit_code = ctyped.type.DWORD()
        if kernel32.GetExitCodeThread(self, ctyped.byref(exit_code)):
            return exit_code.value

    def suspend(self) -> bool:
        return kernel32.SuspendThread(self) != -1

    def resume(self) -> bool:
        return kernel32.ResumeThread(self) != -1

    def join(self, timeout: int = ctyped.const.INFINITE) -> bool:
        return ctyped.const.WAIT_OBJECT_0 == kernel32.WaitForSingleObject(self, timeout)


class RemoteProcess(ctyped.type.HANDLE):
    def __init__(self, handle: int):
        super().__init__(handle)
        self._libs_remote = {}
        self._libs_local = {}

    @classmethod
    def open(cls, pid: int, access: int = ctyped.const.PROCESS_ALL_ACCESS) -> RemoteProcess:
        return cls(kernel32.OpenProcess(access, False, pid))

    def alloc_mem(self, size: int, permission: int = ctyped.const.PAGE_READONLY) -> PageAddress:
        return kernel32.VirtualAllocEx(self, None, size, ctyped.const.MEM_COMMIT, permission)

    def free_mem(self, addr: PageAddress) -> bool:
        return bool(kernel32.VirtualFreeEx(self, addr, 0, ctyped.const.MEM_RELEASE))

    def read_mem(self, addr: PageAddress, size: int):
        buff = (ctyped.type.c_byte * size)()
        if kernel32.ReadProcessMemory(self, addr, ctyped.addressof(buff), size, None):
            return buff

    def write_mem(self, addr: PageAddress, data: AnyStr, size: Optional[int] = None) -> bool:
        if size is None:
            size = (ctyped.sizeof(ctyped.type.c_wchar) if isinstance(
                data, str) else ctyped.sizeof(ctyped.type.c_char)) * len(data)
        return bool(kernel32.WriteProcessMemory(self, addr, data, size, None))

    def load_lib(self, lib: ModuleType) -> bool:
        getattr(lib, '_', None)
        lib = getattr(lib, '_module', lib)
        lib_path = ctyped.lib.get_path(lib).encode() + b'\0'
        arg_addr = self.alloc_mem(len(lib_path), ctyped.const.PAGE_EXECUTE_READWRITE)
        if arg_addr:
            if self.write_mem(arg_addr, lib_path):
                # print(ctyped.cast(self.read_mem(arg_addr, len(lib_path)), ctyped.type.LPSTR).value)
                if lib_remote := self.call_func(ctyped.addressof_func(kernel32.LoadLibraryA), arg_addr).get_exit_code():
                    self._libs_remote[lib] = lib_remote
                    self._libs_local[lib] = kernel32.GetModuleHandleA(lib_path)
            self.free_mem(arg_addr)
        return bool(self._libs_remote.get(lib) and self._libs_local.get(lib))

    def free_lib(self, lib) -> bool:
        if (lib_remote := self._libs_remote.get(lib)) and kernel32.FreeLibrary(lib_remote):
            del self._libs_remote[lib]
            return True
        return False

    def get_remote_func(self, func: Callable, lib) -> FunctionAddress:
        lib_local = self._libs_local[lib]
        return self._libs_remote[lib] + kernel32.GetProcAddress(lib_local, func.__name__.extend_param()) - lib_local

    def call_func(self, func: FunctionAddress, arg: Optional[int] = None, wait: bool = True) -> Thread:
        thread = Thread.create_remote(self, func, arg)
        if wait:
            thread.join()
        return thread


class PyRemoteProcess(RemoteProcess):
    def __del__(self):
        self.free_lib(python)

    @classmethod
    def open(cls, pid: int, access: int = ctyped.const.PROCESS_ALL_ACCESS) -> Optional[PyRemoteProcess]:
        self = cls(super().open(pid, access).value)
        if self.load_lib(python):
            return self

    def initialize(self) -> bool:
        self.call_func(self.get_remote_func(python.Py_Initialize, python))
        return self.is_initialized()

    def initialize_ex(self, init: bool = False) -> bool:
        self.call_func(self.get_remote_func(python.Py_InitializeEx, python), init)
        return self.is_initialized()

    def finalize(self) -> bool:
        self.call_func(self.get_remote_func(python.Py_Finalize, python))
        return not self.is_initialized()

    def finalize_ex(self) -> bool:
        return self.call_func(self.get_remote_func(python.Py_FinalizeEx, python)).get_exit_code() == 0

    def is_initialized(self) -> bool:
        return bool(self.call_func(self.get_remote_func(python.Py_IsInitialized, python)).get_exit_code())

    def set_path(self: RemoteProcess, *paths: str):
        arg = ';'.join(paths)
        arg_addr = self.alloc_mem(len(arg) * 2, ctyped.const.PAGE_EXECUTE_READWRITE)
        self.write_mem(arg_addr, arg)
        self.call_func(self.get_remote_func(python.Py_SetPath, python), arg_addr)
        self.free_mem(arg_addr)

    def err_print(self):
        self.call_func(self.get_remote_func(python.PyErr_Print, python)).get_exit_code()

    def err_print_ex(self, set_vars: bool = False):
        self.call_func(self.get_remote_func(python.PyErr_PrintEx, python), set_vars).get_exit_code()

    def run_simple_string(self, string: str) -> bool:
        arg = string.encode() + b'\0'
        arg_addr = self.alloc_mem(len(arg), ctyped.const.PAGE_EXECUTE_READWRITE)
        self.write_mem(arg_addr, arg)
        thread = self.call_func(self.get_remote_func(python.PyRun_SimpleString, python), arg_addr)
        self.free_mem(arg_addr)
        return thread.get_exit_code() == 0


class PyRemoteProcessEx(PyRemoteProcess):
    def alloc_console(self) -> bool:
        return bool(self.call_func(ctyped.addressof_func(kernel32.AllocConsole)).get_exit_code())

    def free_console(self) -> bool:
        return bool(self.call_func(ctyped.addressof_func(kernel32.FreeConsole)).get_exit_code())

    def reopen_console(self) -> bool:
        return self.run_simple_string("import sys; sys.stdin = open('CONIN$', 'r'); sys.stdout = sys.stderr = open('CONOUT$', 'w')")

    def exec_file(self, path: str) -> bool:
        print(path)
        return self.run_simple_string(f"exec(open('{path}').read())")


def _test_load_string_from_lib():
    buff = ctyped.char_array(' ' * ctyped.const.MAX_PATH)
    user32.LoadStringW(kernel32.GetModuleHandleW('shell32.dll'), 5387, buff, ctyped.const.MAX_PATH)
    print(buff.value)


py_code = """
import ctypes
# from libs import ctyped
pid = ctypes.windll.kernel32.GetCurrentProcessId()
ctypes.windll.user32.MessageBoxW(0, f'Hello from Python ({pid=})', 'Hello from Python', 0x1000)
"""


def _test_hook():
    # ctyped.lib.Python.PyRun_SimpleString(code.encode())
    name = 'Progman'

    # hwnd = ctyped.lib.User32.FindWindowW(name, None)
    pid = ctyped.type.DWORD(29484)
    # ctyped.lib.User32.GetWindowThreadProcessId(hwnd, ctyped.byref(pid))
    print(pid)
    proc = PyRemoteProcessEx.open(pid.value)

    # multi args doesn't work [only first arg is loaded in register]
    # proc.load_lib(ctyped.lib.Kernel32)
    # class Args(ctypes.Structure):
    #     _pack_ = 1
    #     _fields_ = (('dwFreq', ctyped.type.DWORD),
    #                 ('dwDuration', ctyped.type.DWORD))
    # args = Args()
    # args.dwFreq = 750
    # args.dwDuration = 300
    # arg_addr = proc.alloc_mem(ctyped.sizeof(Args), ctyped.const.PAGE_EXECUTE_READWRITE)
    # if arg_addr:
    #     print(ctyped.lib.Kernel32.WriteProcessMemory(proc, arg_addr, ctyped.addressof(args), ctyped.sizeof(args), None))
    #     obj = ctyped.cast(proc.read_mem(arg_addr, ctyped.sizeof(Args)), Args).contents
    #     print(obj.dwFreq, obj.dwDuration)
    #     # proc.write_mem(arg_addr, b_sys_path)
    #     func_addr = proc.get_remote_func(ctyped.lib.Kernel32.Beep, ctyped.lib.Kernel32)
    #     print(proc.call_func(func_addr, arg_addr).get_exit_code())
    #     proc.free_mem(arg_addr)

    proc.alloc_console()
    time.sleep(3)
    print(proc.set_path(*sys.path))
    print(proc.initialize_ex())
    # proc.reopen_console()
    print(proc.run_simple_string('print("Hello from Python")'))
    # print(proc.exec_file(ntpath.realpath('_test_py.py')))
    print(proc.finalize_ex())
    proc.free_console()


class BSTR(ctyped.type.BSTR):
    # noinspection PyMissingConstructor
    def __init__(self, string: Optional[str] = None, size: Optional[int] = None):
        if size is not None:
            self.value = oleaut32.SysAllocStringLen(string, size)
        elif string is not None:
            self.value = oleaut32.SysAllocString(string)

    def __del__(self):
        if self:
            oleaut32.SysFreeString(self)

    def __str__(self):
        return ctyped.type.c_wchar_p.from_buffer(self).value

    def __len__(self):
        return oleaut32.SysStringLen(self)


def _test_browser():
    browser = win32.browser.Browser()
    browser.navigate('https://google.com')
    browser.wait()
    print(browser._browser.width)
    # browser.navigate('about:blank')
    # browser.wait()
    print(browser.get_static_html())


def _test_dispatch():
    # noinspection PyUnresolvedReferences
    import win32com.client as com
    excel = com.gencache.EnsureDispatch('Excel.Application')
    print(excel, sys.modules[type(excel).__module__])

    from libs.ctyped.interface.um import oaidl
    with ctyped.interface.COM[oaidl.IDispatch]('Excel.Application') as disp:
        print(win32._utils.get_funcs(disp).values())


def _test_browser_ex():
    browser = win32.browser._BrowserEx()
    browser._mainloop()
    if browser:
        browser._hwnd.show()
        time.sleep(5)
        res = browser.navigate('https://google.com')
        print(bool(browser._controller))
        if res:
            time.sleep(5)


NT = collections.namedtuple('NT', ('a', 'b', 'c'))


class TNT(typing.NamedTuple):
    a: int
    b: int
    c: int
    d: NT


class E(enum.Enum):
    A = 1
    B = 2
    C = 3


@dataclasses.dataclass
class DC:
    prop1: int
    prop5: Optional[DC] = None

    not_data = 69


class US(collections.UserString):
    pass


class UL(collections.UserList):
    pass


class UD(collections.UserDict):
    pass


def _test_cfg():
    data = {
        # 'ntt': NT(1, 2, 3),
        'tough': collections.deque([1, (1, 2), '3'], maxlen=3),
        'name': 'A Test \'of\' the "TOML" Parser',
        'e_text': '',
        'od': collections.OrderedDict([('a', 1), ('b', 2)]),
        'num': 123,
        'map': {},
        'boolean': True,
        'null': None,
        't_list': [],
        'e_tup': (),
        't_tuple': (1, 2, '3'),
        'set': {1, '2', 3},
        'barr': bytearray(b'123'),
        'fzst': frozenset({'1', 2, 3}),
        'list2': [1, 2, '3'],
        'bytes': b'\x01\x02\x03\x04',
        'complex': 1 + 2j,
        'things': [{'a': 'thing1', 'b': ('fdsa', 69), 'multiLine': 'Some sample text.'},
                   {'a': 'Something else',
                    'b': 'zxcv',
                    'multiLine': 'Multiline string',
                    'objs': [{'x': 1},
                             {'x': {
                                 'list2': [1, 2, '3'],
                                 'bytes': b'\x01\x02\x03\x04'}},
                             {'morethings': [{'y': [2, 3, 4]}, {'y': 9}], 'x': 7}]},
                   {'a': '3', 'b': 'asdf', 'multiLine': 'thing 3.\nanother line'}]}
    # pprint.pprint(data, sort_dicts=False)
    config_ = config.JSONConfig(data)
    dumped = config_.dumps()
    # print(dumped)
    config__ = config.JSONConfig()
    config__.loads(dumped)
    print('JSON', config_ == config__)
    config_ = config.XMLConfig(data)
    dumped = config_.dumps()
    # print(dumped)
    config__ = config.XMLConfig()
    config__.loads(dumped)
    print('XML', config_ == config__)
    config_ = config.INIConfig(data)
    dumped = config_.dumps()
    # print(dumped)
    config__ = config.INIConfig()
    config__.loads(dumped)
    print('INI', config_ == config__)
    config_ = config.REGConfig(data)
    dumped = config_.dumps()
    # print(dumped)
    config__ = config.REGConfig()
    config__.loads(dumped)
    print('REG', config_ == config__)
    # config_ = config.YAMLConfig(data)
    # dumped = config_.dumps()
    # # print(dumped)
    # config__ = config.YAMLConfig()
    # config__.loads(dumped)
    # print('YAML', config_ == config__)


def _test_cfg_json():
    data = {
        'ElementTree': {
            'QName': ElementTree.QName('ns', 'name')},
        'array': {
            'array': array.array('i', [1, 2, 3])},
        'collections': {
            'ChainMap': collections.ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}),
            'Counter': collections.Counter({'red': 4, 'blue': 2}),
            'OrderedDict': collections.OrderedDict([('b', 420), ('a', 69)]),
            'UserDict': UD({'a': 1, 'b': 2}),
            'UserList': UL([1, 2, 3]),
            'UserString': US('usd'),
            'deque': collections.deque([1, (1, 2), '3'], maxlen=3),
            'namedtuple': NT(1, 2, 3)},
        'dataclasses': {
            'dataclass': DC(69, DC(420))},
        'datetime': {
            'date': datetime.date.today(),
            'time': datetime.time(1, 2, 3, 4),
            'datetime': datetime.datetime.now(),
            'timedelta': datetime.timedelta(1, 2, 3, 4)},
        'decimal': {
            'Decimal': decimal.Decimal('123.456')},
        'enum': {
            'enum': E.A},
        'fractions': {
            'Fraction': fractions.Fraction(1, 2)},
        'ipaddress': {
            'IPv4Address': ipaddress.IPv4Address('192.168.0.1'),
            'IPv4Interface': ipaddress.IPv4Interface('192.0.2.5/24'),
            'IPv4Network': ipaddress.IPv4Network('192.0.2.0/28'),
            'IPv6Address': ipaddress.IPv6Address('2001:db8::1'),
            'IPv6Interface': ipaddress.IPv6Interface('2001:db8::1/64'),
            'IPv6Network': ipaddress.IPv6Network('2001:db8::/32')},
        'pathlib': {
            'PurePath': pathlib.PurePath('c:/temp/test.txt')},
        're': {
            'Pattern': re.compile(r'(?P<first>\w+) (?P<last>\w+)', re.IGNORECASE)},
        'typing': {
            'NamedTuple': TNT(1, 2, 3, NT(4, 5, 6))},
        'uuid': {
            'UUID': uuid.uuid4()},
        'NoneType': None,
        # 'EllipsisType': ...,
        'bytes': b'\x01\x02\x03\x04',
        'bytes_': b'',
        'str': 'A Test \'of\' the "JSONConfig"',
        'str_': '',
        'int': 123,
        'float': 123.456,
        'bool': True,
        'complex': 1 + 2j,
        'bytearray': bytearray(b'123'),
        'frozenset': frozenset({'1', 2, 3}),
        'tuple': (1, 2, '3'),
        'tuple_': (),
        'list': [1, 2, '3'],
        'list_': [],
        'set': {1, '2', 3},
        'set_': set(),
        'dict': {'a': 1, 'b': 2},
        'dict_': {},
        'memoryview': memoryview(b'123'),
        'range': range(1, 10, 2),
        'slice': slice(1, 10, 2),
        'nest': [{'a': 'thing1', 'b': ('fdsa', 69), 'multiLine': 'Some sample text.'},
                 {'objs': [{'x': 1},
                           {'x': {
                               'list2': [1, 2, '3'],
                               'bytes': b'\x01\x02\x03\x04'}},
                           {'morethings': [{'y': [2, 3, 4]}, {'y': 9}], 'x': 7}]},
                 {'a': '3', 'b': 'asdf', 'multiLine': 'thing 3.\nanother line'}]}
    config_ = config.JSONConfig(data)
    dumped = config_.dumps()
    print(dumped)
    config__ = config.JSONConfig()
    config__.loads(dumped)
    print(config__)
    print(config_ == config__)


class TD(typing.TypedDict):
    a: int
    b: str


class TD2(TD, total=False):
    c: str


class CT(tuple):
    pass


def _test_inst():
    lst = [1, 2, 3]
    print(typed.isinstance_ex(lst, list[int]))
    tp = list[tuple[int] | list[str]]
    print(typed.isinstance_ex([(1,), (2,), ['3']], tp))
    ct = CT((1, 2, 3))
    print(typed.isinstance_ex(ct, CT[int, int, int]))
    tp2 = Mapping[str, int]
    print(typed.isinstance_ex({'d': 2}, tp2))
    tp3 = dict[str, int]
    print(typed.isinstance_ex({'d': 6}, tp3))
    tp4 = Tuple[int, str]
    print(typed.isinstance_ex((2, '2'), tp4))
    d: dict[int, str] = {1: '1'}
    i = d.items()
    print('ItemsView', typed.isinstance_ex(i, ItemsView[int, str]))
    tp5 = str | NoneType
    print(typed.isinstance_ex(None, tp5))
    tp6 = Optional[str]
    print(typed.isinstance_ex(None, tp6))
    td = TD(a=1, b='2')
    print(typed.isinstance_ex(td, TD))
    nt = TNT(1, 2, 3, NT(4, 5, 6))
    print(typed.isinstance_ex(nt, TNT))
    nnt = 1, 2, 3
    print('nnt', typed.isinstance_ex(nnt, TNT))
    tp = tuple[int, ...]
    print(typed.isinstance_ex((1, 2, 3), tp))
    ltt = Literal[1, 2, 3]
    print('Literal', typed.isinstance_ex(1, ltt))
    print('Literal', typed.isinstance_ex('2', ltt))
    minitd = TypedDict('minitd', {'a': int, 'b': str})
    print('TypedDict', typed.isinstance_ex(td, minitd))
    print('TypedDict', typed.isinstance_ex({}, minitd))
    print(typed.isinstance_ex(TD2(a=1, b='2'), TD2))
    # print(typed.is_instance(v, Callable[[int], float]))
    print(typed.isinstance_ex([{'x': 3}], List[Dict[str, int]]))
    print(typed.isinstance_ex([{'x': 3}, {'y': 7.5}], List[Dict[str, int]]))
    print(typed.isinstance_ex([{'x': 3}], list[dict[str, int]]))
    print(typed.isinstance_ex([{'x': 3}, {'y': 7.5}], list[dict[str, int]]))
    print(typed.isinstance_ex(iter([1, 2, 3]), Iterator[int]))
    print(typed.isinstance_ex([1, 2, 3], Iterator[int]))


def _test_winrt():
    src = r'D:\MMDs\洛天依  -  倾杯.mp4'
    dst = r'D:\test.mp4'
    try:
        print(_utils.copy_file(src, dst, print))
    finally:
        with contextlib.suppress(BaseException):
            os.remove(dst)


data = '''

<!DOCTYPE html>
<html>
<head>
<title>Lumine  - Genshin Impact - Image by Lunacle #2930194 - Zerochan Anime Image Board</title>
<meta charset="utf-8">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="View and download this 1325x765 Lumine image with 124 favorites, or browse the gallery. ">
<meta name="og:title" content="Lumine  - Genshin Impact - Image by Lunacle #2930194 - Zerochan Anime Image Board">
<meta name="og:image" content="https://static.zerochan.net/Lumine.full.2930194.jpg">
<meta name="og:description" content="View and download this 1325x765 Lumine image with 124 favorites, or browse the gallery. ">
<meta name="og:type" content="website">
<meta name="og:site" content="Zerochan Anime Image Board">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Lumine  - Genshin Impact - Image by Lunacle #2930194 - Zerochan Anime Image Board">
<meta name="twitter:description" content="View and download this 1325x765 Lumine image with 124 favorites, or browse the gallery. ">
<meta name="twitter:image" content="https://static.zerochan.net/Lumine.full.2930194.jpg">
<meta name="google-signin-client_id" content="280853676974-pfa7tcmm6lb529u5b5fkb5aeue4i8j0u.apps.googleusercontent.com">

<link rel="canonical" href="https://www.zerochan.net/2930194" />
<link rel="amphtml" href="https://www.zerochan.net/2930194?amp">
<link href="https://www.zerochan.net/v2.css?69nice" type="text/css" rel="stylesheet" />
<style type="text/css">
#header, #body { background-image: url(https://s1.zerochan.net/header-11.jpg?3); }
body { background-image: url(https://s1.zerochan.net/bg-11.jpg?3); }
#wrapper { min-width: 1280px; }
#body { margin-right: 5px; }
#header ul { margin-right: 0; }


#revert { margin: 10px; }
#revert a { padding: 10px 20px; display: inline-block; position: relative; }
#revert a:before { content: ""; z-index: -1; background: rgba(64,128,192,.3); width: 100%; height: 50%; position: absolute;
	top: 0; left: 0; transform: skew(-40deg, 0); }
#revert a:after { content: ""; z-index: -1; background: rgba(64,128,192,.3); width: 100%; height: 50%; position: absolute;
	bottom: 0; left: 0; transform: skew(40deg, 0); }

a.preview { display: inline-block; }
#large a.preview #dragger { border-color: #f00; transition: none; }

@keyframes gradientProgression {
    0% { background-position: 0px 5000px }
    100% { background-position: 0px -1000px }
}
#large a.preview img {
	background-image: linear-gradient(to bottom,
		rgba(182,166,166,.4) 10%,
		rgba(182,166,166,.6) 30%,
		rgba(182,166,166,.4) 50%
	); 
	background-size: 1000px 6000px;
	animation-duration: 2s;
	animation-fill-mode: forwards;
	animation-iteration-count: infinite;
	animation-name: gradientProgression;
	animation-timing-function: linear;
}

#share-form input[type=text] { width: 95%; }
#large a { position: relative; }
#large a.preview div { position: absolute; border: 2px solid rgba(0,0,0,.5); opacity: 0; transition: all .5s; }
#large a.preview div:before { position: absolute; content: ""; width: 100%; height: 100%; border: 1px solid rgba(255,255,255.5);
	top: 0; left: 0; box-sizing: border-box; }
#large a.preview span { position: absolute; top: 100%; left: -1px; background: rgba(0,0,0,.5); color: #fff; padding: 5px 10px;
	margin-top: 1px; opacity: 0; border-radius: 0 0 10px 10px; transition: all .5s; }
#large a.preview b { position: absolute; top: -10px; right: -10px; display: none; background: #faa; color: #f00; padding: 5px;
	width: 20px; line-height: 20px; font-size: 24px; border-radius: 50%; cursor: pointer; transition: all .5s;
	zoom: .5; }
#large a.preview:hover div { opacity: 1; }
#large a.preview:hover span { opacity: 1; }
#large a.preview:hover b { display: block; }
#large a.preview:hover b:hover { zoom: 1; opacity: 1; }

#large #favorite-notice { position: absolute; background: #000; white-space: nowrap; text-align: left; color: #eee;
	padding: 10px; left: -10px; top: 50px; opacity: .8; opacity: 0; transition: opacity .5s; pointer-events: none; }
#favorite-notice:before { content: ""; background: #000; width: 12px; height: 12px; position: absolute; left: 20px;
	top: -6px; transform: rotate(45deg); }
#fav-button-container:hover #favorite-notice { opacity: 1; }

#action-buttons { background: rgba(0,0,0,.05); display: inline-block; padding: 0 10px; margin: 0 auto; min-height: 30px; }
#fb-button { background: #1877f2; display: inline-block; height: 25px; filter: saturate(0); position: relative; top: -4px;
	padding: 0 0 5px 4px; }
#pinterest-button { background: #f00; display: inline-block; height: 20px; position: relative; top: -6px;
	padding: 5px 20px 5px 20px; filter: saturate(0) invert(1); }
#tweet-button { display: inline-block; background: rgba(128,192,255,.4); padding: 5px 15px; position: relative;
	top: -4px; filter: saturate(0); }
#tweet-button a { color: #fff; }
#tweet-button img { width: 16px; position: relative; top: 2px; }
#fb-button:hover, #pinterest-button:hover, #tweet-button:hover { filter: saturate(.4); }

#fav-button-container { display: inline-block; position: relative; top: 5px; min-width: 100px; }
/*
#fav-link { display: inline-block; background: rgba(0,0,0,.1); border-radius: 50%; padding: 5px; width: 32px; height: 32px; }
*/
#fav-link.active img { filter: none; opacity: 1; }
#fav-link img { width: 32px; height: 32px; filter: grayscale(1); opacity: .5; margin-right: 5px; }
#fav-button-container:hover img { animation: pulse 1s linear infinite; }
#fav-button-container:hover ul { display: inline-block; opacity: 1; }
/*
#fav-button-container:hover #fav-link.active+ul { display: none; }
*/
#fav-button-container ul { display: none; position: absolute; background: #fff; z-index: 2; transition: opacity .5s; opacity: 0;
	min-width: 225px; bottom: 0; border: 1px solid #eee; text-align: left; box-shadow: 1px 1px 3px rgba(0,0,0,.8); }
#fav-button-container ul li { display: block; }
#fav-button-container ul li.active { background: #ccc; font-weight: bold; color: #7b5672; }
#fav-button-container ul a { padding: 10px; display: block; cursor: pointer; }
#fav-button-container ul a:hover { background: #eee; }

/*
#menu dl { display: flex; flex-wrap: wrap; }
#menu dt { width: 40%; padding: 5px; }
#menu dd { width: 55%; padding: 5px; text-align: right; }
*/

#tags .theme.emphasis { border: 1px solid rgba(128,128,128,.6); }
.notice { background: rgba(128,128,128,.15); padding: 5px 5px; margin: 2px; display: inline-block; border-radius: 15px; }
.notice img { width: 16px; margin-bottom: -4px; filter: invert(.5); }




#strip-toggle { position:fixed;display:block;width:20px;height:20px;left:50%;bottom:2px;border-radius:50%;background:#fff;
	transition:all .5s;opacity: .4;cursor:pointer;}
#strip-toggle:hover{opacity:.8;}
#strip-toggle.active { bottom: 160px;}
#strip-toggle:before {content:'';border:3px solid #888;width:6px;height:6px;position:absolute;left:5px;top:5px;
	border-color:#888 transparent transparent #888;transform:rotate(45deg);transition:transform 1s;}
#strip-toggle.active:before { transform:rotate(-135deg);}
#strip-thumbs { overflow: scroll;position: fixed; bottom: 0; width: 100%; background: rgba(0,0,0,.6); height: 155px;
	left: 0;z-index:4;}
#strip-thumbs ul { white-space: nowrap; }
#strip-thumbs li { display: inline-block; padding: 1px; margin: 3px 2px; border: 1px solid transparent; }
#strip-thumbs ul:first-child li { padding: 5px; cursor: pointer; }
#strip-thumbs ul:first-child .active { font-weight: bold; background: rgba(128,128,128,.3); }
#strip-thumbs ul:last-child .active { border: 1px solid #fff; }
#strip-thumbs img { height: 120px; opacity: 0;transition: opacity .5s;}
#strip-thumbs img:hover,#strip-thumbs .active img { opacity: 1;}
#strip-thumbs::-webkit-scrollbar {display: none }
#strip-thumbs a { color: #ddd; }
#strip-thumbs a:hover { color: #fff; }
</style>



<script src="//get.s-onetag.com/c69cb856-edf8-4fcd-b57a-3cb09bbcdc6d/tag.min.js" async defer></script><!-- onScroll -->
</head>
<body>
<div id="wrapper">
<div id="header">
<header><div>
<a href="/"><img src="https://s1.zerochan.net/logo12.png" alt="zerochan"/></a>
<ul>
	<li><a href="/">Browse</a></li>
	<li><a href="/upload">Upload</a></li>
	<li><a href="/subscribed">Subscribed</a></li>
	<li><a href="/login?ref=%2F2930194">Login</a></li>
	<li><a href="/register">Register</a></li>
  <li><a href="/theme?theme=13&amp;url=%2F2930194"><img src="https://s1.zerochan.net/icons/darkmode.png" style="width: 16px; position: relative; top: 4px; opacity: 0.5; "></a></li>
</ul>
</div>
</header>
<a href="/"><img src="https://static.zerochan.net/logo12.png" alt="zerochan"/></a>

	<div id="leaderboard">
      <style>
.Zerochan_MOINSBD_Top { width: 320px; height: 50px; }
@media(min-width: 500px) { .Zerochan_MOINSBD_Top { width: 468px; height: 60px; } }
@media(min-width: 800px) { .Zerochan_MOINSBD_Top { width: 728px; height: 200px; } }
@media(min-width: 1300px) { .Zerochan_MOINSBD_End { width: auto; height: 220px; } }
</style>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3000346950361353" crossorigin="anonymous"></script>
<!-- Zerochan_MOINSBD_Top -->
<ins class="adsbygoogle Zerochan_MOINSBD_Top"
     style="display:inline-block"
     data-ad-client="ca-pub-3000346950361353"
     data-ad-slot="3078685876"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({overlays: {bottom: true}});
</script>    </div>
</div>
<div id="body">
<form id="search" action="/search">
<!--  <span id="social-buttons">
  <a rel="nofollow" target="_blank" href="https://discord.gg/HkGgX6Qs3N"><img src="https://s1.zerochan.net/icons/discord2.png" alt="Discord"></a>
  <a rel="nofollow" target="_blank" href="https://twitter.com/ZerochanAnime"><img src="https://s1.zerochan.net/icons/twitter.svg" alt="Twitter"></a>
  <a rel="nofollow" target="_blank" href="https://www.pinterest.com/ZerochanBot/"><img src="https://s1.zerochan.net/icons/pinterest.svg" alt="Pinterest"></a>
  </span>-->
	<input type="text" id="q" name="q" size="40" tabindex="1" placeholder="Search..." value="" />
	<input type="image" src="https://s1.zerochan.net/search.png" value="Search" />
  <input type="reset" value="&#x2716;" />
</form>
<div id="content">
<ul id="tabs">
<li style="visibility: hidden; "><a>View</a></li></ul>
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "ImageObject",
  "author": "Lunacle",
  "contentUrl": "https://static.zerochan.net/Lumine.full.2930194.jpg",
  "thumbnail": "https://s1.zerochan.net/Lumine.600.2930194.jpg",
  "encodingFormat": "jpg",
  "datePublished": "2020-05-03T19:21:06+00:00",
  "description": "View and download this 1325x765 Lumine image with 124 favorites, or browse the gallery. ",
  "name": "Lumine (Genshin Impact)  by Lunacle",
  "width": "1325 px",
  "height": "765 px",
  "contentSize": "666kB"
}
</script>
<h1>Lumine (Genshin Impact)  by Lunacle #2930194</h1>
<p class="breadcrumbs">
	<a href="/">zerochan</a>
	<span class="game" ><a href="/Genshin+Impact">Genshin Impact</a></span>
	<span class="character"><a href="/Lumine">Lumine</a></span>
</p>
<p>
  Mangaka: <a href="/Lunacle" style="display: inline-block; padding: 5px 8px; background: rgba(128,128,128,.15); border-radius: 15px; ">Lunacle</a>,
	uploaded by <a class="user" href="/user/amlerisa"><img src="https://s1.zerochan.net/avatars/36136.gif">amlerisa</a>  <span>May 03, 2020</span>.
</p>

<p id="revert"></p>

<div id="large">
<a href="/2981982" rel="prev" style="height: 346px; " title="Go to previous Lumine image"><b
	style="margin-top: 163px; "></b></a>

<a class="preview" href="https://static.zerochan.net/Lumine.full.2930194.jpg" style="width: 600px; " tabindex="1"><img
  class="jpg"
	src="https://s1.zerochan.net/Lumine.600.2930194.jpg"
	alt="Tags: Anime, Lunacle, Genshin Impact, Lumine, Lily (Flower), Fanart, Pixiv, Fanart from Pixiv"
	title="Lumine (1325x765 666 kB.)"
	style="width: 600px; height: 346px; " /></a>
<p style="font-size: 10pt; color:#000; ">Lunacle, Genshin Impact, Lumine, Lily (Flower), Fanart, Pixiv, Fanart from Pixiv</p>

<p>1325x765<br /><span>666kB</span> <span style="font-variant: small-caps; font-size: 12px; ">jpg</span></p>
<div id="action-buttons">
<div id="fb-button" style=""><iframe src="https://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.zerochan.net%2F2930194&amp;layout=button_count&amp;show_faces=false&amp;width=80&amp;action=like&amp;colorscheme=light&amp;height=21"
	style="border:none; overflow:hidden; width:80px; height:21px; position: relative; top: 4px; margin-left: 5px; "></iframe></div>
<div id="pinterest-button" style="" ><a href="//www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fwww.zerochan.net%2F2930194&media=https://static.zerochan.net/Lumine.full.2930194.jpg&description=Pinterest"
	data-pin-do="buttonPin" data-pin-config="beside" data-pin-color="grey"><img alt="Save to Pinterest"
	src="//assets.pinterest.com/images/pidgets/pinit_fg_en_rect_red_20.png" /></a></div>
  <div id="tweet-button">
    <a class="twitter-share-button" target="_blank" rel="nofollow"
      href="https://twitter.com/intent/tweet?text=%23Lumine%0A%0Ahttps%3A%2F%2Fwww.zerochan.net%2F2930194">
    <img src="https://s1.zerochan.net/icons/twitter.png"> Tweet</a>
  </div>
</div>

<div style="text-align: center; margin-top: 30px; "><style>
.Zerochan_MOINSBD_End { width: 320px; height: 100px; }
@media(min-width: 500px) { .Zerochan_MOINSBD_End { width: 468px; height: 60px; } }
@media(min-width: 800px) { .Zerochan_MOINSBD_End { width: 728px; height: 90px; } }
@media(min-width: 1300px) { .Zerochan_MOINSBD_End { width: auto; height: 220px; } }
</style>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3000346950361353" crossorigin="anonymous"></script>
<!-- Zerochan_MOINSBD_End -->
<ins class="adsbygoogle Zerochan_MOINSBD_End"
     style="display:inline-block"
     data-ad-client="ca-pub-3000346950361353"
     data-ad-slot="9392689073"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({overlays: {bottom: true}});
</script></div>
</div>

<div id="posts" style="clear: left; "><h2>Comments (English)</h2><ul>
<li style="clear: left; "><!-- coder-fail, needs fix --></li></ul></div>
</div><div id="menu"><h2>Advertisement</h2><div style="padding: 5px; min-height: 300px !important; "><style>
.ZEROCHAN_MOINSBD_SIDEBAR { width: 320px; height: 50px; }
@media(min-width: 500px) { .ZEROCHAN_MOINSBD_SIDEBAR { width: 300px; height: 250px; } }
@media(min-width: 800px) { .ZEROCHAN_MOINSBD_SIDEBAR { width: 300px; height: 600px; } }
</style>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3000346950361353" crossorigin="anonymous"></script>
<!-- ZEROCHAN_MOINSBD_SIDEBAR -->
<ins class="adsbygoogle ZEROCHAN_MOINSBD_SIDEBAR"
   style="display:block"
   data-ad-client="ca-pub-3000346950361353"
   data-ad-slot="5381415589"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({overlays: {bottom: true}});
</script></div><h2>Tags</h2>
<ul id="tags" class="tags">
  <li class="mangaka emphasis">
    <a href="/Lunacle"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/mangaka.svg" alt="Mangaka">
        Lunacle    </a>
  </li>
  <li class="game">
    <a href="/Genshin+Impact"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/game.svg" alt="Game">
        Genshin Impact    </a>
  </li>
  <li class="character emphasis">
    <a href="/Lumine" style="font-weight: bold; " title="Added by SubaruSumeragi">
      <img src="https://s1.zerochan.net/icons/character.svg" alt="Character">
        Lumine    </a>
  </li>
  <li class="theme">
    <a href="/Flower+Background"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/theme.svg" alt="Theme">
        Flower Background    </a>
  </li>
  <li class="theme">
    <a href="/Hand+in+Hair"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/theme.svg" alt="Theme">
        Hand in Hair    </a>
  </li>
  <li class="theme emphasis">
    <a href="/Lily+%28Flower%29"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/theme.svg" alt="Theme">
        Lily (Flower)    </a>
  </li>
  <li class="source">
    <a href="/Fanart"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/source.svg" alt="Source">
        Fanart    </a>
  </li>
  <li class="source">
    <a href="/Fanart+from+Pixiv"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/source.svg" alt="Source">
        Fanart from Pixiv    </a>
  </li>
  <li class="source">
    <a href="/Pixiv"  title="Added by amlerisa">
      <img src="https://s1.zerochan.net/icons/source.svg" alt="Source">
        Pixiv    </a>
  </li>
</ul>
<h2>Share</h2>
<form id="share-form">
<label>Direct Link</label>
<input type="text" readonly="readonly" name="permalink"
	value="https://www.zerochan.net/2930194" />
<label>BBCode/Forum Thumbnail</label>
<input type="text" readonly="readonly" name="bbthumb"
	value="[URL=https://www.zerochan.net/2930194][IMG]https://s3.zerochan.net/Lumine.240.2930194.jpg[/IMG][/URL]" />
<label>HTML Thumbnail</label>
<input type="text" readonly="readonly" name="htmlthumb"
	value="&lt;a href=&quot;https://www.zerochan.net/2930194&quot;&gt;&lt;img src=&quot;https://s3.zerochan.net/Lumine.240.2930194.jpg&quot; alt=&quot;Lumine&quot; /&gt;&lt;/a&gt;" />
</form>
<h2>Stats</h2>
<p>124 favorites. </p>
</div>

<div id="footer">
<form id="language-form" action="/language" method="get">
<input type="hidden" name="url" value="/2930194" />
<select name="language">
	<option value="de" >Deutsch</option>
	<option value="en" selected="selected">English</option>
	<option value="es" >Espa&ntilde;ol</option>
	<option value="fr" >Fran&ccedil;ais</option>
	<option value="it" >Italiano</option>
	<option value="pl" >Polski</option>
	<option value="ru" >&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;</option>
	<option value="ko" >&#xD55C;&#xAD6D;&#xC5B4;</option>
</select>
</form>
<!--<a href="https://www.patreon.com/bePatron?u=6546652" rel="nofollow" style="float: left;"><img src="https://c5.patreon.com/external/logo/become_a_patron_button.png" style="margin: 10px; height: 30px;  "></a>-->
<p>&copy; 2023 Zerochan Anime Images. contact@zerochan.net
	<a href="/about">About</a> |
	<a href="/privacy">Privacy</a> |
	<a href="/api">API</a> |
	<a href="https://kpop.asiachan.com/" rel="nofollow">KPOP Image Board</a>
</p>
<ul id="footer-socials">
	<li><a rel="nofollow" target="_blank" href="https://discord.gg/HkGgX6Qs3N"><img src="https://s1.zerochan.net/icons/discord2.png" alt="Discord"><span>Discord</span></a></li>
	<li><a rel="nofollow" target="_blank" href="https://twitter.com/ZerochanAnime"><img src="https://s1.zerochan.net/icons/twitter.svg" alt="Twitter"><span>Twitter</span></a></li>
	<li><a rel="nofollow" target="_blank" href="https://www.pinterest.com/ZerochanBot/"><img src="https://s1.zerochan.net/icons/pinterest.svg" alt="Pinterest"><span>Pinterest</span></a></li>

</ul>


</div>
</div>
</div>
<div id="loader"></div>
<a id="mode-switch"></a>
<script src="https://s1.zerochan.net/jquery-1.7.min.js?2"></script>
<script src="https://s1.zerochan.net/jquery.autocomplete.js?4"></script>
<script src="https://s1.zerochan.net/lite.js?35"></script>
<script async defer src="https://assets.pinterest.com/js/pinit.js"></script>
<script>

/* <![CDATA[ */

function quotePost(id) {
	var post = $('#edit-post' + id + ' textarea').val();
	var current = $('#comment-form textarea').val();
	var author = $('#post-' + id).attr('data-author');
	post = current + '[quote=' + id + '|' + author + ']' + post + '[/quote]\n';
	$('#comment-form textarea').val(post).focus();
	return false;
}
function editPost(id) {
	$('#edit-post' + id).slideDown(200);
	$('#edit-post' + id + ' + div').slideUp(200);
	return false;
}
$('#posts .edit-post').each(function() {
	$(this).submit(function() {
		id = $('input[name=id]', this).attr('value');
		$('input, textarea', this).attr('readonly', 'readonly');
		$.post('/editpost', $(this).serialize() + '&ajax=1', function(html) {
			$('#edit-post' + id + ' input').removeAttr('readonly');
			$('#edit-post' + id).slideUp(200);
			$('#edit-post' + id + ' + div').slideDown(200);
			$('#edit-post' + id + ' + div').html(html);
		});
		return false;
	});
});

$('.reactions a').click(e => {
	e.preventDefault();
	var reaction = $(e.target).text();
	var id = $(e.target).parent().parent().attr('data-id');
	console.log(id);
	$.post('/react', {id, type: 'post', reaction, ajax: 1}, function(n) {
		console.log($(e.target).parent().find('span').length);
		if (!$(e.target).parent().find('span').length) {
			$(e.target).parent().append('<span/>');
		}
		$(e.target).next().text(n);
		$(e.target).parent().addClass('reacted');
	});
});

$('#fav-link').click(function() {
	//$('#fav-link').html('Working...');
	$.post('/fav', {id: 2930194, ajax: 1}, function(html) {
    console.log(html);
    if (html == 0) $('#fav-link').removeClass('active');
    if (html == 1) $('#fav-link').addClass('active');
	});
	return false;
});

id = 2930194;
level = 0;
thumbX = parseInt('0600');
thumbY = parseInt('0346');
x = 1325;
y = 765;
local1 = 'Click to view image only';
local2 = 'Scaled to fit your screen';
local3 = 'Revert to small';
local4 = 'Entry by';
staticServer = 'https://s1.zerochan.net/';
htmlName = 'amlerisa';
uriName = 'amlerisa';
largeThumbUrl = 'https://s1.zerochan.net/Lumine.600.2930194.jpg';
fullsizeUrl = 'https://static.zerochan.net/Lumine.full.2930194.jpg';
backgroundColor = '182,166,156';
hash = '';
function monitor() {
	if (window.location.hash != hash) {
		if (level == 1 && window.location.hash != '#full') {
			decrease();
		}
		if (level == 0 && window.location.hash == '#full') {
			enlarge();
		}
		hash = window.location.hash;
	}
}
window.setInterval(monitor, 100);
$('#large > a.preview').click(enlarge);

labelX = 0;
labelY = 0;
originalWidth = 1325;
originalHeight = 765;
labelPermissions = false;
$('#large .preview').mousedown(function(e) {
  if (level != 1 && true) return;
  console.log(this, e.pageX, $(this).offset().top);
	if (e.ctrlKey || e.metaKey) {
		labelX = e.pageX - $(this).offset().left;
		labelY = e.pageY - $(this).offset().top;
		$('<div id="dragger" />').insertBefore('#large .preview img').css({left: labelX, top: labelY, display: 'block'});
		return false;
	}
});
$('#large .preview').mousemove(function(e) {
  if (level != 1 && true) return;
	if (e.ctrlKey || e.metaKey) {
    //console.log();
		w = e.pageX - $(this).offset().left - labelX;
		h = e.pageY - $(this).offset().top - labelY;
		$('#dragger').css({width: w, height: h});
	}
});
$('#large .preview').mouseup(function(e) {
  if (level != 1 && true) return;
	if (labelX == 0) return;
  if (!e.ctrlKey && !e.metaKey) return;
	w = e.pageX - $('#large .preview').offset().left - labelX;
	h = e.pageY - $('#large .preview').offset().top - labelY;
	$('#dragger').css({width: w, height: h});
	if (w < 20 || h < 20) {
		alert('Area too small or negative. ');
		return;
	}
  e.preventDefault();
  e.stopPropagation();
  var ratio = x / originalWidth;
  console.log(labelX / ratio, labelY / ratio, w / ratio, h / ratio);
	label = prompt('Label');
	if (label) {
		$.post('./label', {img: 2930194, 'x': labelX / ratio, 'y': labelY / ratio, 'w': w / ratio, 'h': h / ratio, label: label}, function(r) {
			$('<div><b href="#" onclick="return delLabel(' + r + ', this)">×</b><span>' + label + '</span></div>').css({'left': labelX, 'top': labelY, width: w, height: h}).insertBefore('#large .preview img');
			labelX = 0;
			labelY = 0;
		});
	}
	$('#dragger').remove();
});
function delLabel(id, a) {
	$.post('./label', {del: id}, function() {
		$(a).parent().remove();
	});
	return false;
}

$('#share-form').prepend('<p>If you want to share this image on other websites/forums, use the following:</p>');
$('#share-form input').focus(function() {
	this.select();
});
$('#share-form input').mouseup(function(e) {
	e.preventDefault();
});


/* ]]> */
</script>
</body></html>
'''
data2 = r'''
{
  "id": 3906973,
  "small": "https://s1.zerochan.net/75/23/39/3906973.jpg",
  "medium": "https://s3.zerochan.net/240/23/39/3906973.jpg",
  "large": "https://s1.zerochan.net/Lumine.600.3906973.jpg",
  "full": "https://static.zerochan.net/Lumine.full.3906973.jpg",
  "width": 1240,
  "height": 2004,
  "size": 1555456,
  "hash": "5fb5b63fd150dada58d90e88a095a75e",
  "source": "https://www.pixiv.net/en/artworks/105930865",
  "primary": "Lumine",
  "tags": [
    "Female",
    "Ecchi",
    "Fanart",
    "Flower",
    "Dress",
    "White Dress",
    "Clouds",
    "Gloves",
    "See Through Clothes",
    "Shoes",
    "Wedding Dress",
    "Blonde Hair",
    "Sky",
    "Leaves",
    "Gold Eyes",
    "Veil",
    "High Heels",
    "Sunbeam",
    "Hair Flower",
    "Pixiv",
    "Alternate Outfit",
    "Solo",
    "Hair Ornament",
    "White Gloves",
    "Fanart from Pixiv",
    "Long Gloves",
    "Bridal Veil",
    "Cleavage",
    "White Handwear",
    "chabing0802\",
    "Genshin Impact",
    "Lumine",
    "Short Hair with Long Sidelocks"
  ]
}
'''


def _test():
    html = soup.loads(data)
    data3 = data2.replace('\\', '\\\\')
    js = json.loads(data3)
    print(js)


if __name__ == '__main__':  # FIXME replace "[tuple(" -> "[*("
    # _test_cfg()
    # _test_cfg_json()
    # _test_inst()
    # _test_winrt()
    _test()
    sys.exit()
