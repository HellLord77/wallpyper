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
import os
import pathlib
import pprint
import re
import sys
import time
import typing
import uuid
from types import ModuleType
from typing import AnyStr, Callable, Optional, TypeVar
from xml.etree import ElementTree

import win32
from libs import ctyped, config, request
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


def _test_load_string_from_lib():
    buff = ctyped.char_array(' ' * ctyped.const.MAX_PATH)
    user32.LoadStringW(kernel32.GetModuleHandleW('shell32.dll'), 5387, buff, ctyped.const.MAX_PATH)
    print(buff.value)


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
    # noinspection PyArgumentList
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


def _test_winrt():
    src = r'D:\MMDs\洛天依  -  倾杯.mp4'
    dst = r'D:\test.mp4'
    try:
        print(_utils.copy_file(src, dst, print))
    finally:
        with contextlib.suppress(BaseException):
            os.remove(dst)


def _test_500px():
    url = 'https://api.500px.com/graphql'
    data = {
        "operationName": "DiscoverQueryRendererQuery",
        "variables": {
            "filters": [
                {
                    "key": "FEATURE_NAME",
                    "value": "popular"
                },
                {
                    "key": "FOLLOWERS_COUNT",
                    "value": "gte:0"
                }
            ],
            "sort": "POPULAR_PULSE"
        },
        "query": "query DiscoverQueryRendererQuery($filters: [PhotoDiscoverSearchFilter!], $sort: PhotoDiscoverSort) {\n"
                 "  ...DiscoverPaginationContainer_query_1OEZSy\n"
                 "}\n"
                 "\n"
                 "fragment DiscoverPaginationContainer_query_1OEZSy on Query {\n"
                 "  photos: photoDiscoverSearch(first: 50, filters: $filters, sort: $sort) {\n"
                 "    edges {\n"
                 "      node {\n"
                 "        id\n"
                 "        legacyId\n"
                 "        canonicalPath\n"
                 "        name\n"
                 "        description\n"
                 "        category\n"
                 "        uploadedAt\n"
                 "        location\n"
                 "        width\n"
                 "        height\n"
                 "        isLikedByMe\n"
                 "        notSafeForWork\n"
                 "        tags\n"
                 "        photographer: uploader {\n"
                 "          id\n"
                 "          legacyId\n"
                 "          username\n"
                 "          displayName\n"
                 "          canonicalPath\n"
                 "          avatar {\n"
                 "            images {\n"
                 "              url\n"
                 "              id\n"
                 "            }\n"
                 "            id\n"
                 "          }\n"
                 "          followedBy {\n"
                 "            totalCount\n"
                 "            isFollowedByMe\n"
                 "          }\n"
                 "        }\n"
                 "        images(sizes: [33, 35]) {\n"
                 "          size\n"
                 "          url\n"
                 "          jpegUrl\n"
                 "          webpUrl\n"
                 "          id\n"
                 "        }\n"
                 "        pulse {\n"
                 "          highest\n"
                 "          id\n"
                 "        }\n"
                 "        __typename\n"
                 "      }\n"
                 "      cursor\n"
                 "    }\n"
                 "    totalCount\n"
                 "    pageInfo {\n"
                 "      endCursor\n"
                 "      hasNextPage\n"
                 "    }\n"
                 "  }\n"
                 "}\n"}
    resp = request.post(url, json=data)
    if resp:
        pprint.pprint(resp.json(), sort_dicts=False)


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
        return self._libs_remote[lib] + kernel32.GetProcAddress(lib_local, func.__name__.encode()) - lib_local

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


py_code = """
import ctypes
# from libs import ctyped
pid = ctypes.windll.kernel32.GetCurrentProcessId()
ctypes.windll.user32.MessageBoxW(0, f'Hello from Python ({pid=})', 'Hello from Python', 0x1000)
"""


def _test_hook():
    # ctyped.lib.Python.PyRun_SimpleString(code.encode())
    name = 'Notepad'

    hwnd = user32.FindWindowW(name, None)
    pid = ctyped.type.DWORD(32388)
    user32.GetWindowThreadProcessId(hwnd, ctyped.byref(pid))
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
    proc.set_path(*sys.path)
    print(proc.initialize_ex())
    # proc.reopen_console()
    # print(proc.run_simple_string('print("Hello from Python")'))
    # print(proc.exec_file(ntpath.realpath('_test_py.py')))
    print(proc.finalize_ex())
    proc.free_console()


def _test_requests():
    import ssl
    import requests

    from requests.adapters import HTTPAdapter
    from urllib3.poolmanager import PoolManager
    from urllib3.util.ssl_ import create_urllib3_context

    # see "openssl ciphers" command for cipher names
    CIPHERS = "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384"

    class TlsAdapter(HTTPAdapter):
        def __init__(self, ssl_options=0, **kwargs):
            self.ssl_options = ssl_options
            super(TlsAdapter, self).__init__(**kwargs)

        def init_poolmanager(self, *pool_args, **pool_kwargs):
            ctx = create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
            self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)  # prioritize TLS 1.2
    default = requests.get("https://tools.scrapfly.io/api/fp/ja3?extended=1").json()
    session = requests.session()
    session.mount("https://", adapter)
    fixed = session.get("https://tools.scrapfly.io/api/fp/ja3?extended=1").json()
    print('Default:')
    print(default['tls']['ciphers'])
    print(default['ja3'])
    print('Patched:')
    print(fixed['tls']['ciphers'])
    print(fixed['ja3'])
    print(session.get('https://wall.alphacoders.com/by_comments.php').status_code)


def _test_httpx():
    import httpx, ssl

    ssl_ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)  # prefer TLS 1.2
    ssl_ctx.set_alpn_protocols(["h2", "http/1.1"])
    # see "openssl ciphers" command for cipher names
    CIPHERS = "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-ECDSA-AES256-GCM-SHA384"
    ssl_ctx.set_ciphers(CIPHERS)

    default = httpx.get("https://tools.scrapfly.io/api/fp/ja3?extended=1").json()
    fixed = httpx.get("https://tools.scrapfly.io/api/fp/ja3?extended=1", verify=ssl_ctx).json()
    print('Default:')
    print(default['tls']['ciphers'])
    print(default['ja3'])
    print('Patched:')
    print(fixed['tls']['ciphers'])
    print(fixed['ja3'])
    print(httpx.get('https://wall.alphacoders.com/by_comments.php', verify=ssl_ctx).status_code)


def _test():
    import cloudscraper
    url = 'https://wall.alphacoders.com/by_comments.php'
    # url = 'https://tools.scrapfly.io/api/fp/ja3?extended=1'
    cookies = {'ResolutionFilter': '7680x4320',
               'ResolutionEquals': '%3D'}
    sess = cloudscraper.create_scraper()
    adap: cloudscraper.CipherSuiteAdapter = sess.adapters['https://']
    print(adap.ssl_context.wrap_socket)
    ua = sess.user_agent
    headers = ua.headers
    pprint.pprint(headers, sort_dicts=False)
    print(ua.cipherSuite)
    # sess = requests.Session()
    # sess.mount('https://', adap)
    # sess = request.Session(http_debug=True)
    # sess.verify = adap.ssl_context
    resp = sess.get(url, cookies=cookies, headers=headers)
    print(resp.elapsed)
    # print(resp.headers)
    # print(resp.request.headers)
    print(repr(resp.status_code))
    # print(resp.text)

    # bro = win32.browser.Browser(url)
    # bro.wait()
    # print(bro.get_static_html())


if __name__ == '__main__':  # FIXME replace "[tuple(" -> "[*("
    # _test_cfg()
    # _test_cfg_json()
    # _test_winrt()
    # _test_hook()
    # _test_requests()
    # _test_httpx()
    _test()
    sys.exit()
