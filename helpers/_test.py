from __future__ import annotations

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
import uuid
from types import ModuleType
from typing import AnyStr, Callable, Optional, TypeVar, NamedTuple
from xml.etree import ElementTree

import win32
from libs import ctyped, config, request
from libs.ctyped.const import error
from libs.ctyped.interface.um import ShObjIdl_core
from libs.ctyped.lib import kernel32, user32, python
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


def _test_load_string_from_lib():
    buff = ctyped.char_array(' ' * ctyped.const.MAX_PATH)
    user32.LoadStringW(kernel32.GetModuleHandleW('shell32.dll'), 5387, buff, ctyped.const.MAX_PATH)
    print(buff.value)


def _test_browser():
    from win32 import _browser
    browser = _browser.Browser()
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
    from win32 import _browser
    browser = _browser._BrowserEx()
    browser._mainloop()
    if browser:
        browser._hwnd.show()
        time.sleep(5)
        res = browser.navigate('https://google.com')
        print(bool(browser._controller))
        if res:
            time.sleep(5)


NT = collections.namedtuple('NT', ('a', 'b', 'c'))


class TNT(NamedTuple):
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


data = """
<div
  class="row pt-2"
  id="ModalWallpaperDetailBody"
  data-page="/anime/ultra-instinct-goku-mastered-for-mobile-db-legends-dt_en-US-100733.html"
  data-photoid="100733"
>
  <div class="col-12 col-md-7 pb-2">
    <img
      src="https://cdn.bhdw.net/im/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-100733_w635.webp"
      class="img-fluid rounded"
      alt="Ultra Instinct Goku Mastered for Mobile [DB Legends] download"
    />
    <div class="row">
      <div class="col-12 pl-4 pr-4 pt-2">
        <a
          href="/anime/ultra-instinct-goku-mastered-db-legends-dt_en-US-100732.html"
          class="np btn btn-secondary float-left"
        >
          <img
            src="https://cdn.bhdw.net/v2.10124/images/Left_Arrow.svg"
            alt="Previous"
            width="8"
            height="12"
          />
          Previous
        </a>
        <a
          href="/movies/eobard-thawne-is-reverse-flash-dt_en-US-100734.html"
          class="np btn btn-secondary float-right"
          >Next
          <img
            src="https://cdn.bhdw.net/v2.10124/images/Right_Arrow.svg"
            alt="Next"
            width="8"
            height="12"
          />
        </a>
      </div>
    </div>
  </div>
  <div class="col-12 col-md-5 pl-3 pr-4">
    <div class="row rounded bg-light p-3">
      <div class="col-12">
        <div class="row p-2">
          <div class="col-3 pt-3">
            <a href="/kamaboko-wallpapers-mw_en-US-13596">
              <img
                src="https://cdn.bhdw.net/v2.10124/images/no-avatar.png"
                class="float-left img-fluid rounded-circle"
                alt=""
              />
            </a>
          </div>
          <div class="col-9 align-self-center">
            <h5><strong>Kamaboko </strong></h5>
            <h4><strong>8557</strong> Downloads</h4>
            <h4><strong>12858 </strong> Views</h4>
          </div>
          <div class="col-12">
            <p class="text-muted">Date of upload : 17 Feb 2023</p>
          </div>
        </div>
      </div>
      <div class="col-12 p-1">
        <select class="custom-select custom-select-lg mb-3" id="CHSize">
          <option value="1" asp-selected="asp-selected">
            Wide & Ultra Wide
          </option>
          <option value="2">HD & UHD</option>
          <option value="3">Standard</option>
          <option value="6">Dual Monitor</option>
          <option value="5">Mobile Brands</option>
        </select>
      </div>
      <div class="col-12 p-1">
        <select
          class="custom-select custom-select-lg mb-3 resolutions"
          id="Resolutions1"
          style="display: none"
        >
          <optgroup label="Wide 16:10">
            <option
              value="1"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-960x600-100733_1.jpg"
              asp-selected="asp-selected"
            >
              960x600
            </option>
            <option
              value="2"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1152x720-100733_2.jpg"
              asp-selected="asp-selected"
            >
              1152x720
            </option>
            <option
              value="3"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1280x800-100733_3.jpg"
              asp-selected="asp-selected"
            >
              1280x800
            </option>
            <option
              value="4"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x900-100733_4.jpg"
              asp-selected="asp-selected"
            >
              1440x900
            </option>
          </optgroup>
          <optgroup label="Wide 5:3">
            <option
              value="12"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-800x480-100733_12.jpg"
              asp-selected="asp-selected"
            >
              800x480
            </option>
            <option
              value="13"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1280x768-100733_13.jpg"
              asp-selected="asp-selected"
            >
              1280x768
            </option>
          </optgroup>
        </select>
        <select
          class="custom-select custom-select-lg mb-3 resolutions"
          id="Resolutions2"
          style="display: none"
        >
          <optgroup label="HD 16:9">
            <option
              value="43"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-960x540-100733_43.jpg"
            >
              960x540
            </option>
            <option
              value="44"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1024x576-100733_44.jpg"
            >
              1024x576
            </option>
            <option
              value="45"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1280x720-100733_45.jpg"
            >
              1280x720
            </option>
            <option
              value="46"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1366x768-100733_46.jpg"
            >
              1366x768
            </option>
            <option
              value="47"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1600x900-100733_47.jpg"
            >
              1600x900
            </option>
          </optgroup>
        </select>
        <select
          class="custom-select custom-select-lg mb-3 resolutions"
          id="Resolutions3"
          style="display: none"
        >
          <optgroup label="Standard 3:2">
            <option
              value="36"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1152x768-100733_36.jpg"
            >
              1152x768
            </option>
            <option
              value="37"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x960-100733_37.jpg"
            >
              1440x960
            </option>
          </optgroup>
          <optgroup label="Standard 4:3">
            <option
              value="17"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-800x600-100733_17.jpg"
            >
              800x600
            </option>
            <option
              value="18"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1024x768-100733_18.jpg"
            >
              1024x768
            </option>
            <option
              value="19"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1152x864-100733_19.jpg"
            >
              1152x864
            </option>
            <option
              value="20"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1280x960-100733_20.jpg"
            >
              1280x960
            </option>
            <option
              value="21"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1400x1050-100733_21.jpg"
            >
              1400x1050
            </option>
            <option
              value="22"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x1080-100733_22.jpg"
            >
              1440x1080
            </option>
            <option
              value="23"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1600x1200-100733_23.jpg"
            >
              1600x1200
            </option>
          </optgroup>
          <optgroup label="Standard 5:4">
            <option
              value="32"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1280x1024-100733_32.jpg"
            >
              1280x1024
            </option>
          </optgroup>
        </select>
        <select
          class="custom-select custom-select-lg mb-3 resolutions"
          id="Resolutions6"
          style="display: none"
        >
          <optgroup label="Dual standard 4:3">
            <option
              value="84"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1600x600-100733_84.jpg"
            >
              1600x600
            </option>
          </optgroup>
          <optgroup label="Dual wide 5:3">
            <option
              value="68"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1600x480-100733_68.jpg"
            >
              1600x480
            </option>
          </optgroup>
        </select>
        <select
          class="custom-select custom-select-lg mb-3 resolutions"
          id="Resolutions5"
          style="display: none"
        >
          <optgroup label="Apple iPad 1, 2 &amp; iPad Mini">
            <option
              value="176"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1024x768-100733_18.jpg"
            >
              1024x768
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 11">
            <option
              value="224"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-828x1792-100733_218.jpg"
            >
              828x1792
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 11 Pro">
            <option
              value="225"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1125x2436-100733_215.jpg"
            >
              1125x2436
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 12">
            <option
              value="226"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1170x2532-100733_226.jpg"
            >
              1170x2532
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 12 Mini">
            <option
              value="229"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x2340-100733_229.jpg"
            >
              1080x2340
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 12 Pro">
            <option
              value="227"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1170x2532-100733_226.jpg"
            >
              1170x2532
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 12 Pro Max">
            <option
              value="228"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1284x2778-100733_228.jpg"
            >
              1284x2778
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 13">
            <option
              value="230"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1170x2532-100733_226.jpg"
            >
              1170x2532
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 13 Mini">
            <option
              value="233"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x2340-100733_229.jpg"
            >
              1080x2340
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 13 Pro">
            <option
              value="231"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1170x2532-100733_226.jpg"
            >
              1170x2532
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 13 Pro Max">
            <option
              value="232"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1284x2778-100733_228.jpg"
            >
              1284x2778
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 14">
            <option
              value="234"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1170x2532-100733_226.jpg"
            >
              1170x2532
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 14 Pro">
            <option
              value="235"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1179x2556-100733_235.jpg"
            >
              1179x2556
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 14 Pro Max">
            <option
              value="236"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1290x2796-100733_236.jpg"
            >
              1290x2796
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 1G, 3GS">
            <option
              value="170"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-320x480-100733_170.jpg"
            >
              320x480
            </option>
          </optgroup>
          <optgroup
            label="Apple iPhone 5, 5C, 5S
"
          >
            <option
              value="168"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-640x1136-100733_163.jpg"
            >
              640x1136
            </option>
          </optgroup>
          <optgroup
            label="Apple iPhone 6 &amp; 6S
"
          >
            <option
              value="166"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-750x1334-100733_164.jpg"
            >
              750x1334
            </option>
          </optgroup>
          <optgroup
            label="Apple iPhone 6 Plus
"
          >
            <option
              value="167"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1242x2208-100733_167.jpg"
            >
              1242x2208
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 7">
            <option
              value="164"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-750x1334-100733_164.jpg"
            >
              750x1334
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 7 Plus">
            <option
              value="165"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x1920-100733_165.jpg"
            >
              1080x1920
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 8">
            <option
              value="213"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-750x1334-100733_164.jpg"
            >
              750x1334
            </option>
          </optgroup>
          <optgroup label="Apple iPhone 8 Plus">
            <option
              value="214"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x1920-100733_165.jpg"
            >
              1080x1920
            </option>
          </optgroup>
          <optgroup label="Apple iPhone Plus">
            <option
              value="237"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1284x2778-100733_228.jpg"
            >
              1284x2778
            </option>
          </optgroup>
          <optgroup label="Apple iPhone Retina 4, 4S">
            <option
              value="169"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-640x960-100733_169.jpg"
            >
              640x960
            </option>
          </optgroup>
          <optgroup label="Apple iPhone SE">
            <option
              value="163"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-640x1136-100733_163.jpg"
            >
              640x1136
            </option>
          </optgroup>
          <optgroup label="Apple iPhone X">
            <option
              value="215"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1125x2436-100733_215.jpg"
            >
              1125x2436
            </option>
          </optgroup>
          <optgroup label="Apple iPhone XR">
            <option
              value="218"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-828x1792-100733_218.jpg"
            >
              828x1792
            </option>
          </optgroup>
          <optgroup label="Apple iPhone XS">
            <option
              value="216"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1125x2436-100733_215.jpg"
            >
              1125x2436
            </option>
          </optgroup>
          <optgroup label="Apple iPhone XS Max">
            <option
              value="217"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1242x2688-100733_217.jpg"
            >
              1242x2688
            </option>
          </optgroup>
          <optgroup label="Apple iPod Classic &amp; iPod Nano 3G">
            <option
              value="180"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-240x320-100733_180.jpg"
            >
              240x320
            </option>
          </optgroup>
          <optgroup label="Apple iPod Touch 1G to 3G">
            <option
              value="179"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-320x480-100733_170.jpg"
            >
              320x480
            </option>
          </optgroup>
          <optgroup label="Apple iPod Touch 4G">
            <option
              value="178"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-640x960-100733_169.jpg"
            >
              640x960
            </option>
          </optgroup>
          <optgroup label="Apple iPod Touch 5G">
            <option
              value="177"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-640x1136-100733_163.jpg"
            >
              640x1136
            </option>
          </optgroup>
          <optgroup label="Google Galaxy Nexus or Galaxy X">
            <option
              value="184"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-720x1280-100733_184.jpg"
            >
              720x1280
            </option>
          </optgroup>
          <optgroup label="Google Nexus 4">
            <option
              value="183"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-768x1280-100733_183.jpg"
            >
              768x1280
            </option>
          </optgroup>
          <optgroup label="Google Nexus 5 &amp; Nexus 5X">
            <option
              value="182"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x1920-100733_165.jpg"
            >
              1080x1920
            </option>
          </optgroup>
          <optgroup label="Google Nexus 6 &amp; Nexus 6P">
            <option
              value="181"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x2560-100733_181.jpg"
            >
              1440x2560
            </option>
          </optgroup>
          <optgroup label="Google Nexus S &amp; Nexus One">
            <option
              value="185"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-480x800-100733_185.jpg"
            >
              480x800
            </option>
          </optgroup>
          <optgroup label="HTC 10">
            <option
              value="209"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x2560-100733_181.jpg"
            >
              1440x2560
            </option>
          </optgroup>
          <optgroup label="Huawei Mate 8">
            <option
              value="211"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x1920-100733_165.jpg"
            >
              1080x1920
            </option>
          </optgroup>
          <optgroup label="LG G5">
            <option
              value="210"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x2560-100733_181.jpg"
            >
              1440x2560
            </option>
          </optgroup>
          <optgroup label="Microsoft Lumia 950">
            <option
              value="212"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x2560-100733_181.jpg"
            >
              1440x2560
            </option>
          </optgroup>
          <optgroup label="Samsung Behold 2, Saturn, Galaxy Spica">
            <option
              value="193"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-320x480-100733_170.jpg"
            >
              320x480
            </option>
          </optgroup>
          <optgroup label="Samsung Diva, Tocco, Omnia Pro, Corby">
            <option
              value="195"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-240x320-100733_180.jpg"
            >
              240x320
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Alpha, Galaxy A5, A3, S5 Mini">
            <option
              value="189"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-720x1280-100733_184.jpg"
            >
              720x1280
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Note 2">
            <option
              value="199"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-720x1280-100733_184.jpg"
            >
              720x1280
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Note 3 &amp; Note 3 Neo">
            <option
              value="197"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x1920-100733_165.jpg"
            >
              1080x1920
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Note 5, Note Edge, Note 4">
            <option
              value="196"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x2560-100733_181.jpg"
            >
              1440x2560
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Note 8.0, Note 10.1">
            <option
              value="201"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1280x800-100733_3.jpg"
            >
              1280x800
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Note, Note LTE">
            <option
              value="198"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-800x1280-100733_198.jpg"
            >
              800x1280
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy S, S Plus, S Advance, S Duos">
            <option
              value="192"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-480x800-100733_185.jpg"
            >
              480x800
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy S3, S2 HD">
            <option
              value="190"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-720x1280-100733_184.jpg"
            >
              720x1280
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy S4 Mini, S4 Zoom">
            <option
              value="191"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-540x960-100733_191.jpg"
            >
              540x960
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy S5, S5 Active, S4, S4 Active, A5">
            <option
              value="188"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x1920-100733_165.jpg"
            >
              1080x1920
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy S7 Edge &amp; S6 Edge">
            <option
              value="186"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x2560-100733_181.jpg"
            >
              1440x2560
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy S7, S6 &amp; S5 LTE">
            <option
              value="187"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1440x2560-100733_181.jpg"
            >
              1440x2560
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Tab 2/3/4 10.1, Tab 8.9, Tab 7.7,">
            <option
              value="204"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-800x1280-100733_198.jpg"
            >
              800x1280
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Tab S2 9.7 &amp; 8.0">
            <option
              value="203"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1536x2048-100733_203.jpg"
            >
              1536x2048
            </option>
          </optgroup>
          <optgroup label="Samsung Galaxy Tab, Tab 7.0 Plus, Tab 2 7.0">
            <option
              value="205"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-600x1024-100733_205.jpg"
            >
              600x1024
            </option>
          </optgroup>
          <optgroup label="Samsung Omnia, Star, Pixon, Solstice, Highlight">
            <option
              value="194"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-240x400-100733_194.jpg"
            >
              240x400
            </option>
          </optgroup>
          <optgroup label="Sony Xperia Z5">
            <option
              value="207"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x1920-100733_165.jpg"
            >
              1080x1920
            </option>
          </optgroup>
          <optgroup label="Sony Xperia Z5 Compact">
            <option
              value="208"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-720x1280-100733_184.jpg"
            >
              720x1280
            </option>
          </optgroup>
          <optgroup label="Xiaomi Redmi 10">
            <option
              value="238"
              data-download="https://a-static.besthdwallpaper.com/ultra-instinct-goku-mastered-for-mobile-db-legends-wallpaper-1080x2400-100733_238.jpg"
            >
              1080x2400
            </option>
          </optgroup>
        </select>
      </div>
      <div class="col-12">
        <a
          href="#"
          download=""
          class="btn btn-primary btn-lg btn-block disabled"
          id="DownloadWP"
          data-loading-text="Downloading..."
          data-photoid="100733"
          data-sizeid=""
        >
          <img
            src="https://cdn.bhdw.net/v2.10124/images/Download.svg"
            alt="Download"
          />
          Download</a
        >
      </div>
      <div class="col-12">
        <ins
          class="adsbygoogle"
          style="display: inline-block; width: 260px; height: 90px"
          data-ad-client="ca-pub-8182672928439076"
          data-ad-slot="5864480243"
        ></ins>
        <script>
          (adsbygoogle = window.adsbygoogle || []).push({});
        </script>
      </div>
      <div class="col-12">
        <div class="d-flex text-center pt-3">
          <div class="p-2 flex-fill">
            <a
              href="https://www.facebook.com/sharer/sharer.php?u=https://www.besthdwallpaper.com/anime/ultra-instinct-goku-mastered-for-mobile-db-legends-dt_en-US-100733.html"
              class="social-share facebook"
              target="_blank"
              rel="nofollow"
              title="Share on Facebook"
              data-id="100733"
              ><img
                src="https://cdn.bhdw.net/v2.10124/images/facebook-black.svg"
                alt="Share on Facebook"
            /></a>
          </div>
          <div class="p-2 flex-fill">
            <a
              href="http://pinterest.com/pin/create/button/?url=https://www.besthdwallpaper.com/anime/ultra-instinct-goku-mastered-for-mobile-db-legends-dt_en-US-100733.html"
              data-title="Ultra Instinct Goku Mastered for Mobile [DB Legends]"
              data-share="https://www.besthdwallpaper.com/anime/ultra-instinct-goku-mastered-for-mobile-db-legends-dt_en-US-100733.html"
              data-node="a"
              data-id="100733"
              class="social-share pinterest"
              target="_blank"
              rel="nofollow"
              title="Share on Pinterest"
              ><img
                src="https://cdn.bhdw.net/v2.10124/images/pinterest-black.svg"
                alt="Share on Pinterest"
            /></a>
          </div>
          <div class="p-2 flex-fill">
            <a
              href="https://twitter.com/share?url=https://www.besthdwallpaper.com/anime/ultra-instinct-goku-mastered-for-mobile-db-legends-dt_en-US-100733.html"
              class="social-share twitter"
              target="_blank"
              rel="nofollow"
              title="Share on Twitter"
              data-id="100733"
              ><img
                src="https://cdn.bhdw.net/v2.10124/images/twitter-black.svg"
                alt="Share on Twitter"
            /></a>
          </div>
          <div class="p-2 flex-fill">
            <a
              href="https://mix.com/add?url=https://www.besthdwallpaper.com/anime/ultra-instinct-goku-mastered-for-mobile-db-legends-dt_en-US-100733.html"
              class="social-share mix"
              target="_blank"
              rel="nofollow"
              title="Share on Mix"
              data-id="100733"
              ><img
                src="https://cdn.bhdw.net/v2.10124/images/Mix.svg"
                alt="Share on Mix"
            /></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
<div class="row">
  <div class="col-12">
    <div class="tags">
      <hr class="m-1" />
      <h6><strong>Tag clouds</strong></h6>
      <a
        href="/most-popular/goku-tg_en-US-573"
        class="btn btn-secondary"
        style="font-size: 14pt"
        rel="tag"
        >Goku</a
      >
      <a
        href="/most-popular/dragon-ball-tg_en-US-578"
        class="btn btn-secondary"
        style="font-size: 21pt"
        rel="tag"
        >Dragon Ball</a
      >
      <a
        href="/most-popular/super-saiyan-tg_en-US-579"
        class="btn btn-secondary"
        style="font-size: 15pt"
        rel="tag"
        >Super Saiyan</a
      >
      <a
        href="/most-popular/dragon-ball-z-tg_en-US-586"
        class="btn btn-secondary"
        style="font-size: 17pt"
        rel="tag"
        >dragon ball z</a
      >
      <a
        href="/most-popular/dragon-ball-super-tg_en-US-3452"
        class="btn btn-secondary"
        style="font-size: 12pt"
        rel="tag"
        >Dragon Ball Super</a
      >
      <a
        href="/most-popular/dragon-ball-legends-tg_en-US-43744"
        class="btn btn-secondary"
        style="font-size: 11pt"
        rel="tag"
        >Dragon Ball Legends</a
      >
      <a
        href="/most-popular/dragon-ball-gt-tg_en-US-43757"
        class="btn btn-secondary"
        style="font-size: 13pt"
        rel="tag"
        >Dragon Ball GT</a
      >
      <a
        href="/most-popular/ui-goku-tg_en-US-62197"
        class="btn btn-secondary"
        style="font-size: 18pt"
        rel="tag"
        >ui goku</a
      >
      <a
        href="/most-popular/ultra-instinct-goku-tg_en-US-62203"
        class="btn btn-secondary"
        style="font-size: 11pt"
        rel="tag"
        >ultra instinct goku</a
      >
    </div>
  </div>
</div>
<script>
  jQuery(function () {
    BHDW.ModalWindow();
  });
</script>
"""


def _test_progress():
    with ctyped.interface.COM[ShObjIdl_core.ITaskbarList3](ctyped.const.CLSID_TaskbarList) as taskbar:
        print(taskbar.HrInit())
        hwnd = user32.GetForegroundWindow()
        print(taskbar.SetProgressState(hwnd, ctyped.enum.TBPFLAG.INDETERMINATE))
        time.sleep(3)
        taskbar.SetProgressState(hwnd, ctyped.enum.TBPFLAG.NOPROGRESS)


from libs import minihtml


def key(ele: minihtml.Element) -> int:
    res = map(int, ele[0].datas[0].strip().split('x'))
    return next(res) * next(res)


data2 = """
<html>
<ul id="categories-menu" class="categoryMenu top pt-2">
  <li>
    <a title="Animals" href="/animals-wallpapers-ct_en-US-40">Animals </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li><a title="Birds" href="/birds-wallpapers-ct_en-US-41">Birds</a></li>
        <li><a title="Cats" href="/cats-wallpapers-ct_en-US-156">Cats</a></li>
        <li><a title="Dogs" href="/dogs-wallpapers-ct_en-US-73">Dogs</a></li>
        <li><a title="Frogs" href="/frogs-wallpapers-ct_en-US-46">Frogs</a></li>
        <li>
          <a title="Horses" href="/horses-wallpapers-ct_en-US-42">Horses</a>
        </li>
        <li>
          <a title="Insects" href="/insects-wallpapers-ct_en-US-43">Insects</a>
        </li>
        <li><a title="Pets" href="/pets-wallpapers-ct_en-US-44">Pets</a></li>
        <li>
          <a title="Reptiles" href="/reptiles-wallpapers-ct_en-US-45"
            >Reptiles</a
          >
        </li>
        <li>
          <a title="Sea creature" href="/sea-creature-wallpapers-ct_en-US-47"
            >Sea creature</a
          >
        </li>
        <li><a title="Wild" href="/wild-wallpapers-ct_en-US-48">Wild</a></li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Architecture" href="/architecture-wallpapers-ct_en-US-74"
      >Architecture</a
    >
  </li>
  <li><a title="Army" href="/army-wallpapers-ct_en-US-75">Army</a></li>
  <li>
    <a title="Artistic" href="/artistic-wallpapers-ct_en-US-49">Artistic </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li><a title="3 D" href="/3-d-wallpapers-ct_en-US-150">3 D</a></li>
        <li>
          <a title="Abstract" href="/abstract-wallpapers-ct_en-US-50"
            >Abstract</a
          >
        </li>
        <li><a title="Anime" href="/anime-wallpapers-ct_en-US-51">Anime</a></li>
        <li>
          <a title="Background" href="/background-wallpapers-ct_en-US-153"
            >Background</a
          >
        </li>
        <li>
          <a title="Comics" href="/comics-wallpapers-ct_en-US-165">Comics</a>
        </li>
        <li>
          <a title="Drawings" href="/drawings-wallpapers-ct_en-US-52"
            >Drawings</a
          >
        </li>
        <li>
          <a title="Fantasy" href="/fantasy-wallpapers-ct_en-US-53">Fantasy</a>
        </li>
        <li>
          <a title="Geometric" href="/geometric-wallpapers-ct_en-US-160"
            >Geometric</a
          >
        </li>
        <li>
          <a title="Graffiti" href="/graffiti-wallpapers-ct_en-US-54"
            >Graffiti</a
          >
        </li>
        <li>
          <a title="Grunge" href="/grunge-wallpapers-ct_en-US-55">Grunge</a>
        </li>
        <li>
          <a title="Kaleidoscope" href="/kaleidoscope-wallpapers-ct_en-US-159"
            >Kaleidoscope</a
          >
        </li>
        <li>
          <a title="Sci-fi" href="/sci-fi-wallpapers-ct_en-US-164">Sci-fi</a>
        </li>
        <li>
          <a title="Sculpture" href="/sculpture-wallpapers-ct_en-US-56"
            >Sculpture</a
          >
        </li>
        <li>
          <a title="Typography" href="/typography-wallpapers-ct_en-US-57"
            >Typography</a
          >
        </li>
        <li><a title="Urban" href="/urban-wallpapers-ct_en-US-58">Urban</a></li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Black and White" href="/black-and-white-wallpapers-ct_en-US-76"
      >Black and White</a
    >
  </li>
  <li>
    <a title="Cars" href="/cars-wallpapers-ct_en-US-1">Cars </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li><a title="Audi" href="/audi-wallpapers-ct_en-US-12">Audi</a></li>
        <li>
          <a title="Bentley" href="/bentley-wallpapers-ct_en-US-13">Bentley</a>
        </li>
        <li><a title="BMW" href="/bmw-wallpapers-ct_en-US-14">BMW</a></li>
        <li>
          <a title="Bugatti" href="/bugatti-wallpapers-ct_en-US-186">Bugatti</a>
        </li>
        <li>
          <a title="Chevrolet" href="/chevrolet-wallpapers-ct_en-US-154"
            >Chevrolet</a
          >
        </li>
        <li>
          <a title="Classic cars" href="/classic-cars-wallpapers-ct_en-US-111"
            >Classic cars</a
          >
        </li>
        <li>
          <a title="Ferrari" href="/ferrari-wallpapers-ct_en-US-15">Ferrari</a>
        </li>
        <li><a title="Ford" href="/ford-wallpapers-ct_en-US-16">Ford</a></li>
        <li>
          <a title="Koenigsegg" href="/koenigsegg-wallpapers-ct_en-US-152"
            >Koenigsegg</a
          >
        </li>
        <li>
          <a title="Lamborghini" href="/lamborghini-wallpapers-ct_en-US-59"
            >Lamborghini</a
          >
        </li>
        <li><a title="Lotus" href="/lotus-wallpapers-ct_en-US-17">Lotus</a></li>
        <li>
          <a title="Mercedes" href="/mercedes-wallpapers-ct_en-US-72"
            >Mercedes</a
          >
        </li>
        <li>
          <a title="Mitsubishi" href="/mitsubishi-wallpapers-ct_en-US-18"
            >Mitsubishi</a
          >
        </li>
        <li>
          <a title="Nissan" href="/nissan-wallpapers-ct_en-US-19">Nissan</a>
        </li>
        <li><a title="Other" href="/other-wallpapers-ct_en-US-22">Other</a></li>
        <li>
          <a title="Porsche" href="/porsche-wallpapers-ct_en-US-167">Porsche</a>
        </li>
        <li>
          <a title="Subaru" href="/subaru-wallpapers-ct_en-US-20">Subaru</a>
        </li>
        <li>
          <a title="Toyota" href="/toyota-wallpapers-ct_en-US-21">Toyota</a>
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Cartoons" href="/cartoons-wallpapers-ct_en-US-151">Cartoons</a>
  </li>
  <li>
    <a title="Celebrities" href="/celebrities-wallpapers-ct_en-US-2"
      >Celebrities
    </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a
            title="Angelina Jolie"
            href="/angelina-jolie-wallpapers-ct_en-US-193"
            >Angelina Jolie</a
          >
        </li>
        <li><a title="BTS" href="/bts-wallpapers-ct_en-US-191">BTS</a></li>
        <li>
          <a title="Dua Lipa" href="/dua-lipa-wallpapers-ct_en-US-189"
            >Dua Lipa</a
          >
        </li>
        <li>
          <a title="Gal Gadot" href="/gal-gadot-wallpapers-ct_en-US-190"
            >Gal Gadot</a
          >
        </li>
        <li>
          <a title="Jessica Alba" href="/jessica-alba-wallpapers-ct_en-US-23"
            >Jessica Alba</a
          >
        </li>
        <li>
          <a
            title="Kendall Jenner"
            href="/kendall-jenner-wallpapers-ct_en-US-187"
            >Kendall Jenner</a
          >
        </li>
        <li>
          <a title="Kylie Jenner" href="/kylie-jenner-wallpapers-ct_en-US-155"
            >Kylie Jenner</a
          >
        </li>
        <li>
          <a title="Megan Fox" href="/megan-fox-wallpapers-ct_en-US-24"
            >Megan Fox</a
          >
        </li>
        <li>
          <a title="Models" href="/models-wallpapers-ct_en-US-77">Models</a>
        </li>
        <li>
          <a title="Movies" href="/movies-wallpapers-ct_en-US-78">Movies</a>
        </li>
        <li><a title="Music" href="/music-wallpapers-ct_en-US-79">Music</a></li>
        <li>
          <a title="Olivia wilde" href="/olivia-wilde-wallpapers-ct_en-US-71"
            >Olivia wilde</a
          >
        </li>
        <li>
          <a
            title="Scarlett Johansson"
            href="/scarlett-johansson-wallpapers-ct_en-US-192"
            >Scarlett Johansson</a
          >
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Charity" href="/charity-wallpapers-ct_en-US-143">Charity</a>
  </li>
  <li><a title="City" href="/city-wallpapers-ct_en-US-142">City</a></li>
  <li>
    <a title="Computer" href="/computer-wallpapers-ct_en-US-3">Computer </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Android" href="/android-wallpapers-ct_en-US-136">Android</a>
        </li>
        <li><a title="Apple" href="/apple-wallpapers-ct_en-US-25">Apple</a></li>
        <li>
          <a title="Firefox" href="/firefox-wallpapers-ct_en-US-137">Firefox</a>
        </li>
        <li>
          <a title="Hardware" href="/hardware-wallpapers-ct_en-US-138"
            >Hardware</a
          >
        </li>
        <li>
          <a title="Linux" href="/linux-wallpapers-ct_en-US-139">Linux</a>
        </li>
        <li>
          <a title="nVIDIA" href="/nvidia-wallpapers-ct_en-US-140">nVIDIA</a>
        </li>
        <li><a title="Web" href="/web-wallpapers-ct_en-US-141">Web</a></li>
        <li>
          <a title="Windows" href="/windows-wallpapers-ct_en-US-26">Windows</a>
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Creative" href="/creative-wallpapers-ct_en-US-4">Creative</a>
  </li>
  <li><a title="Cute" href="/cute-wallpapers-ct_en-US-129">Cute</a></li>
  <li>
    <a title="Elements" href="/elements-wallpapers-ct_en-US-130">Elements </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li><a title="Air" href="/air-wallpapers-ct_en-US-134">Air</a></li>
        <li>
          <a title="Earth" href="/earth-wallpapers-ct_en-US-131">Earth</a>
        </li>
        <li><a title="Fire" href="/fire-wallpapers-ct_en-US-132">Fire</a></li>
        <li>
          <a title="Water" href="/water-wallpapers-ct_en-US-133">Water</a>
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Entertainment" href="/entertainment-wallpapers-ct_en-US-5"
      >Entertainment</a
    >
  </li>
  <li>
    <a title="Food and Drink" href="/food-and-drink-wallpapers-ct_en-US-135"
      >Food and Drink</a
    >
  </li>
  <li><a title="Funny" href="/funny-wallpapers-ct_en-US-128">Funny</a></li>
  <li>
    <a title="Games" href="/games-wallpapers-ct_en-US-6">Games </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Apex Legends" href="/apex-legends-wallpapers-ct_en-US-175"
            >Apex Legends</a
          >
        </li>
        <li>
          <a
            title="Assassin's Creed"
            href="/assassin-s-creed-wallpapers-ct_en-US-181"
            >Assassin's Creed</a
          >
        </li>
        <li>
          <a title="Battlefield" href="/battlefield-wallpapers-ct_en-US-172"
            >Battlefield</a
          >
        </li>
        <li>
          <a
            title="Cyberpunk 2077"
            href="/cyberpunk-2077-wallpapers-ct_en-US-174"
            >Cyberpunk 2077</a
          >
        </li>
        <li>
          <a title="Final Fantasy" href="/final-fantasy-wallpapers-ct_en-US-170"
            >Final Fantasy</a
          >
        </li>
        <li>
          <a title="Fortnite" href="/fortnite-wallpapers-ct_en-US-171"
            >Fortnite</a
          >
        </li>
        <li>
          <a title="God of War" href="/god-of-war-wallpapers-ct_en-US-176"
            >God of War</a
          >
        </li>
        <li><a title="LOL" href="/lol-wallpapers-ct_en-US-168">LOL</a></li>
        <li>
          <a
            title="Mobile Legends"
            href="/mobile-legends-wallpapers-ct_en-US-173"
            >Mobile Legends</a
          >
        </li>
        <li>
          <a title="Other Games" href="/other-games-wallpapers-ct_en-US-185"
            >Other Games</a
          >
        </li>
        <li>
          <a title="Overwatch" href="/overwatch-wallpapers-ct_en-US-180"
            >Overwatch</a
          >
        </li>
        <li><a title="PUBG" href="/pubg-wallpapers-ct_en-US-169">PUBG</a></li>
        <li>
          <a title="Spider Man" href="/spider-man-wallpapers-ct_en-US-179"
            >Spider Man</a
          >
        </li>
        <li>
          <a title="The Witcher" href="/the-witcher-wallpapers-ct_en-US-177"
            >The Witcher</a
          >
        </li>
        <li>
          <a
            title="World of Warcraft"
            href="/world-of-warcraft-wallpapers-ct_en-US-178"
            >World of Warcraft</a
          >
        </li>
      </ul>
    </div>
  </li>
  <li><a title="Girls" href="/girls-wallpapers-ct_en-US-127">Girls</a></li>
  <li><a title="Love" href="/love-wallpapers-ct_en-US-114">Love</a></li>
  <li>
    <a title="Motorcycles" href="/motorcycles-wallpapers-ct_en-US-112"
      >Motorcycles</a
    >
  </li>
  <li><a title="Movies" href="/movies-wallpapers-ct_en-US-7">Movies</a></li>
  <li><a title="Music" href="/music-wallpapers-ct_en-US-110">Music</a></li>
  <li>
    <a title="Nature" href="/nature-wallpapers-ct_en-US-8">Nature </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li><a title="Beach" href="/beach-wallpapers-ct_en-US-60">Beach</a></li>
        <li>
          <a title="Desert" href="/desert-wallpapers-ct_en-US-61">Desert</a>
        </li>
        <li>
          <a title="Flowers" href="/flowers-wallpapers-ct_en-US-62">Flowers</a>
        </li>
        <li>
          <a title="Forests" href="/forests-wallpapers-ct_en-US-63">Forests</a>
        </li>
        <li><a title="Lakes" href="/lakes-wallpapers-ct_en-US-64">Lakes</a></li>
        <li>
          <a title="Landscape" href="/landscape-wallpapers-ct_en-US-65"
            >Landscape</a
          >
        </li>
        <li>
          <a title="Mountains" href="/mountains-wallpapers-ct_en-US-66"
            >Mountains</a
          >
        </li>
        <li>
          <a title="Rivers" href="/rivers-wallpapers-ct_en-US-67">Rivers</a>
        </li>
        <li>
          <a title="Sun &amp; Sky" href="/sun-sky-wallpapers-ct_en-US-68"
            >Sun &amp; Sky</a
          >
        </li>
        <li>
          <a title="Waterfalls" href="/waterfalls-wallpapers-ct_en-US-69"
            >Waterfalls</a
          >
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Other" href="/other-wallpapers-ct_en-US-9">Other </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Babies" href="/babies-wallpapers-ct_en-US-162">Babies</a>
        </li>
        <li><a title="Flags" href="/flags-wallpapers-ct_en-US-28">Flags</a></li>
        <li>
          <a title="People" href="/people-wallpapers-ct_en-US-29">People</a>
        </li>
        <li>
          <a title="Quote" href="/quote-wallpapers-ct_en-US-161">Quote</a>
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Seasons" href="/seasons-wallpapers-ct_en-US-144">Seasons </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Autumn" href="/autumn-wallpapers-ct_en-US-145">Autumn</a>
        </li>
        <li>
          <a title="Calendar" href="/calendar-wallpapers-ct_en-US-146"
            >Calendar</a
          >
        </li>
        <li>
          <a title="Spring" href="/spring-wallpapers-ct_en-US-147">Spring</a>
        </li>
        <li>
          <a title="Summer" href="/summer-wallpapers-ct_en-US-148">Summer</a>
        </li>
        <li>
          <a title="Winter" href="/winter-wallpapers-ct_en-US-149">Winter</a>
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Series" href="/series-wallpapers-ct_en-US-10">Series </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Dexter" href="/dexter-wallpapers-ct_en-US-30">Dexter</a>
        </li>
        <li>
          <a
            title="Game of Thrones"
            href="/game-of-thrones-wallpapers-ct_en-US-31"
            >Game of Thrones</a
          >
        </li>
        <li>
          <a title="House MD" href="/house-md-wallpapers-ct_en-US-32"
            >House MD</a
          >
        </li>
        <li>
          <a
            title="How I Met Your Mother"
            href="/how-i-met-your-mother-wallpapers-ct_en-US-33"
            >How I Met Your Mother</a
          >
        </li>
        <li><a title="Lost" href="/lost-wallpapers-ct_en-US-34">Lost</a></li>
        <li>
          <a
            title="My Hero Academia"
            href="/my-hero-academia-wallpapers-ct_en-US-184"
            >My Hero Academia</a
          >
        </li>
        <li>
          <a title="Naruto" href="/naruto-wallpapers-ct_en-US-183">Naruto</a>
        </li>
        <li>
          <a title="One Piece" href="/one-piece-wallpapers-ct_en-US-182"
            >One Piece</a
          >
        </li>
        <li>
          <a title="Other" href="/other-wallpapers-ct_en-US-157">Other</a>
        </li>
        <li>
          <a title="Spartacus" href="/spartacus-wallpapers-ct_en-US-35"
            >Spartacus</a
          >
        </li>
        <li>
          <a title="Squid Game" href="/squid-game-wallpapers-ct_en-US-188"
            >Squid Game</a
          >
        </li>
        <li>
          <a title="Supernatural" href="/supernatural-wallpapers-ct_en-US-36"
            >Supernatural</a
          >
        </li>
        <li>
          <a
            title="The Big Bang Theory"
            href="/the-big-bang-theory-wallpapers-ct_en-US-37"
            >The Big Bang Theory</a
          >
        </li>
      </ul>
    </div>
  </li>
  <li><a title="Space" href="/space-wallpapers-ct_en-US-109">Space</a></li>
  <li>
    <a title="Special days" href="/special-days-wallpapers-ct_en-US-115"
      >Special days
    </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Birthday" href="/birthday-wallpapers-ct_en-US-116"
            >Birthday</a
          >
        </li>
        <li>
          <a
            title="Children's Day"
            href="/children-s-day-wallpapers-ct_en-US-117"
            >Children's Day</a
          >
        </li>
        <li>
          <a title="Christmas" href="/christmas-wallpapers-ct_en-US-118"
            >Christmas</a
          >
        </li>
        <li>
          <a title="Easter" href="/easter-wallpapers-ct_en-US-119">Easter</a>
        </li>
        <li>
          <a title="Father's Day" href="/father-s-day-wallpapers-ct_en-US-120"
            >Father's Day</a
          >
        </li>
        <li>
          <a title="Halloween" href="/halloween-wallpapers-ct_en-US-121"
            >Halloween</a
          >
        </li>
        <li>
          <a title="Holi festival" href="/holi-festival-wallpapers-ct_en-US-166"
            >Holi festival</a
          >
        </li>
        <li>
          <a
            title="Independence Day"
            href="/independence-day-wallpapers-ct_en-US-122"
            >Independence Day</a
          >
        </li>
        <li>
          <a title="Labor day" href="/labor-day-wallpapers-ct_en-US-158"
            >Labor day</a
          >
        </li>
        <li>
          <a title="Mother's Day" href="/mother-s-day-wallpapers-ct_en-US-123"
            >Mother's Day</a
          >
        </li>
        <li>
          <a title="New Year" href="/new-year-wallpapers-ct_en-US-124"
            >New Year</a
          >
        </li>
        <li>
          <a
            title="Saint Patrick's Day"
            href="/saint-patrick-s-day-wallpapers-ct_en-US-125"
            >Saint Patrick's Day</a
          >
        </li>
        <li>
          <a title="Thanksgiving" href="/thanksgiving-wallpapers-ct_en-US-195"
            >Thanksgiving</a
          >
        </li>
        <li>
          <a
            title="Valentine's Day"
            href="/valentine-s-day-wallpapers-ct_en-US-126"
            >Valentine's Day</a
          >
        </li>
        <li>
          <a title="Women's Day" href="/women-s-day-wallpapers-ct_en-US-163"
            >Women's Day</a
          >
        </li>
      </ul>
    </div>
  </li>
  <li>
    <a title="Sport" href="/sport-wallpapers-ct_en-US-11">Sport </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Baseball" href="/baseball-wallpapers-ct_en-US-82"
            >Baseball</a
          >
        </li>
        <li>
          <a title="Basketball" href="/basketball-wallpapers-ct_en-US-39"
            >Basketball</a
          >
        </li>
        <li>
          <a title="Biking" href="/biking-wallpapers-ct_en-US-83">Biking</a>
        </li>
        <li>
          <a title="Boxing" href="/boxing-wallpapers-ct_en-US-84">Boxing</a>
        </li>
        <li>
          <a title="Fitness" href="/fitness-wallpapers-ct_en-US-85">Fitness</a>
        </li>
        <li>
          <a title="Football" href="/football-wallpapers-ct_en-US-38"
            >Football</a
          >
        </li>
        <li>
          <a title="Formula 1" href="/formula-1-wallpapers-ct_en-US-86"
            >Formula 1</a
          >
        </li>
        <li>
          <a title="Free Running" href="/free-running-wallpapers-ct_en-US-87"
            >Free Running</a
          >
        </li>
        <li><a title="Golf" href="/golf-wallpapers-ct_en-US-88">Golf</a></li>
        <li><a title="MMA" href="/mma-wallpapers-ct_en-US-97">MMA</a></li>
        <li>
          <a
            title="Motorcycle Racing"
            href="/motorcycle-racing-wallpapers-ct_en-US-89"
            >Motorcycle Racing</a
          >
        </li>
        <li>
          <a title="Olympics" href="/olympics-wallpapers-ct_en-US-81"
            >Olympics</a
          >
        </li>
        <li>
          <a title="Other Sports" href="/other-sports-wallpapers-ct_en-US-90"
            >Other Sports</a
          >
        </li>
        <li>
          <a title="Parkour" href="/parkour-wallpapers-ct_en-US-91">Parkour</a>
        </li>
        <li>
          <a title="Skateboarding" href="/skateboarding-wallpapers-ct_en-US-92"
            >Skateboarding</a
          >
        </li>
        <li>
          <a title="Skiing" href="/skiing-wallpapers-ct_en-US-93">Skiing</a>
        </li>
        <li>
          <a title="Surfing" href="/surfing-wallpapers-ct_en-US-94">Surfing</a>
        </li>
        <li>
          <a title="Tennis" href="/tennis-wallpapers-ct_en-US-95">Tennis</a>
        </li>
        <li>
          <a title="Winter sport" href="/winter-sport-wallpapers-ct_en-US-96"
            >Winter sport</a
          >
        </li>
      </ul>
    </div>
  </li>
  <li><a title="Trains" href="/trains-wallpapers-ct_en-US-113">Trains</a></li>
  <li>
    <a title="Travel" href="/travel-wallpapers-ct_en-US-98">Travel </a>
    <div class="categoryMenu-Sub">
      <button class="btn">&nbsp;</button>
      <ul>
        <li>
          <a title="Africa" href="/africa-wallpapers-ct_en-US-99">Africa</a>
        </li>
        <li>
          <a title="America" href="/america-wallpapers-ct_en-US-101">America</a>
        </li>
        <li>
          <a title="Antarctica" href="/antarctica-wallpapers-ct_en-US-107"
            >Antarctica</a
          >
        </li>
        <li><a title="Asia" href="/asia-wallpapers-ct_en-US-100">Asia</a></li>
        <li>
          <a title="Caribbean" href="/caribbean-wallpapers-ct_en-US-108"
            >Caribbean</a
          >
        </li>
        <li>
          <a title="Europe" href="/europe-wallpapers-ct_en-US-102">Europe</a>
        </li>
        <li>
          <a title="Islands" href="/islands-wallpapers-ct_en-US-104">Islands</a>
        </li>
        <li><a title="Maps" href="/maps-wallpapers-ct_en-US-105">Maps</a></li>
        <li>
          <a title="Middle east" href="/middle-east-wallpapers-ct_en-US-103"
            >Middle east</a
          >
        </li>
        <li>
          <a title="Oceania" href="/oceania-wallpapers-ct_en-US-106">Oceania</a>
        </li>
      </ul>
    </div>
  </li>
  <li><a title="Vintage" href="/vintage-wallpapers-ct_en-US-80">Vintage</a></li>
  <li><a title="Yacht" href="/yacht-wallpapers-ct_en-US-194">Yacht</a></li>
</ul>
</html>
"""


def _test():
    html = minihtml.loads(data)
    print(max(html.find_all('optgroup'), key=key)[0]['data-download'])
    cats = {}
    for ele in minihtml.loads(data2).find_all('li'):
        link = ele[0]
        id_ = int(link['href'].rsplit('-', 1)[1])
        name = link['title']
        if link.parent.parent.parent.name == 'div':
            name = '    ' + name
        cats[id_] = name
    pprint.pprint(cats, sort_dicts=False)
    print(cats.keys())
    for cat in cats:
        print(f'BESTHDWALLPAPER_CATEGORY_{cat} = {cats[cat]!r}')


if __name__ == '__main__':  # FIXME replace "[tuple(" -> "[*("
    # _test_cfg()
    # _test_cfg_json()
    # _test_winrt()
    # _test_hook()
    _test()
    sys.exit()
