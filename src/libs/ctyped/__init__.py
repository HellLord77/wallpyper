from __future__ import annotations as _

__version__ = '0.2.18'

import builtins as _builtins
import contextlib as _contextlib
import ctypes
import functools as _functools
import threading as _threading
import types as _types
import typing as _typing
from typing import (Any as _Any, Callable as _Callable, ContextManager as _ContextManager, Generic as _Generic,
                    Iterable as _Iterable, Mapping as _Mapping, MutableSequence as _MutableSequence, Optional as _Optional, Union as _Union)

from . import const, enum, handle, interface, lib, macro, struct, type, union
from ._utils import (_get_namespace, _get_winrt_class_name, _CT as CT, _Pointer as Pointer, _addressof as addressof,
                     _byref as byref, _cast as cast, _cast_int as cast_int, _pointer as pointer, _sizeof as sizeof)

_MESSAGES = {}

THREADED_COM = False


# noinspection PyShadowingBuiltins,PyShadowingNames
def from_address(address: int, type: _builtins.type[CT]) -> CT:
    return type.from_address(address)


@_contextlib.contextmanager
def buffer(size: int = 0) -> _ContextManager[_Optional[int]]:
    ptr = lib.msvcrt.malloc(size)
    try:
        yield ptr or None
    finally:
        lib.msvcrt.free(ptr)


# noinspection PyShadowingBuiltins,PyShadowingNames
def array(*elements: _Any, type: _Optional[_builtins.type[CT]] = None, size: _Optional[int] = None) -> _Union[_MutableSequence[CT], Pointer[CT]]:
    return ((_builtins.type(elements[0]) if type is None else type) * (
        len(elements) if size is None else size))(*elements)


@_typing.overload
def char_array(string: bytes = b'', size: _Optional[int] = None) -> Pointer[type.c_char]:
    pass


@_typing.overload
def char_array(string: str = '', size: _Optional[int] = None) -> Pointer[type.c_wchar]:
    pass


def char_array(string='', size=None):
    if size is not None:
        size -= 1
        string = string[:size] + (b'\0' if isinstance(string, bytes) else '\0') * (size - len(string))
    return ((type.c_char if isinstance(string, bytes) else type.c_wchar) * (len(string) + 1))(*string)


# noinspection PyShadowingNames
def resize_array(array: Pointer[CT], size: int) -> Pointer[CT]:
    # noinspection PyProtectedMember
    return (array._type_ * size).from_address(addressof(array))


def get_message(message: int) -> str:
    if not _MESSAGES:
        for name, val in vars(const).items():
            if name.startswith('WM_'):
                _MESSAGES[val] = name
    try:
        return _MESSAGES[message]
    except KeyError:
        return f'WM_{message}'


def get_interface_name(iid: str, base: _Union[type, _types.ModuleType] = const) -> _Optional[str]:
    for var, val in vars(base).items():
        if isinstance(val, _builtins.type):
            if name := get_interface_name(iid, val):
                return name
        elif iid == val:
            return var.removeprefix('IID_')


# noinspection PyProtectedMember,PyShadowingNames
def set_result_checker(lib: lib._CDLL, callback: _Optional[_Callable[[_Any, _Callable, tuple], _Any]] = None,
                       args: _Optional[_Iterable] = None, kwargs: _Optional[_Mapping[str, _Any]] = None):
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}

    @_functools.wraps
    def errcheck(res, *args_):
        callback(res, *args_, *args, **kwargs)
        return res

    lib._errcheck = errcheck
    # noinspection PyUnresolvedReferences
    if lib._funcs:
        # noinspection PyUnresolvedReferences
        for func in set(lib._funcs).intersection(dir(lib)):
            getattr(lib, func).errcheck = errcheck


# noinspection PyShadowingBuiltins,PyShadowingNames
def create_handler(handler: _Callable[[...], type.HRESULT], type: _builtins.type[CT], name: _Optional[str] = None) -> CT:
    args = getattr(type, '_args', None)
    impl_name = type.__name__
    if args is not None:
        impl_name = f'{impl_name.split("_", 1)[0]}_impl'
    impl = getattr(_get_namespace(type), impl_name)
    if args is not None:
        impl = impl[tuple(args.values())]
    return cast(_builtins.type(f'{__name__}-{__version__}-{type.__name__}({handler.__name__})' if name is None else name, (impl,), {'Invoke': handler})(), type)


# noinspection PyProtectedMember
def get_lib_path(library: lib._OleDLL | lib._PyDLL | lib._WinDLL) -> str:
    lib._load(library)
    buff = type.LPWSTR('\0' * const.MAX_PATH)
    # noinspection PyUnresolvedReferences
    lib.Kernel32.GetModuleFileNameW(library._lib._handle, buff, const.MAX_PATH)
    return buff.value


def addressof_func(func) -> int:
    return ctypes.cast(func, ctypes.c_void_p).value


def get_guid(string: str) -> struct.GUID:
    guid = struct.GUID()
    lib.Shell32.GUIDFromStringW(string, byref(guid))
    return guid


@_contextlib.contextmanager
def _prep_com(type_: _builtins.type[CT]) -> _ContextManager[CT]:
    lib.Ole32.CoInitializeEx(None, enum.COINIT.MULTITHREADED.value) if THREADED_COM else lib.Ole32.CoInitialize(None)
    obj = type_()
    try:
        yield obj
    finally:
        if obj:
            obj.Release()
        lib.Ole32.CoUninitialize()


# noinspection PyShadowingBuiltins,PyShadowingNames
@_contextlib.contextmanager
def init_com(type: _builtins.type[CT], init: bool = True) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type) as obj:
        if init:
            # noinspection PyProtectedMember
            if macro.FAILED(lib.Ole32.CoCreateInstance(byref(get_guid(
                    type._CLSID_)), None, const.CLSCTX_ALL, *macro.IID_PPV_ARGS(obj))):
                obj = None
        yield obj


# noinspection PyShadowingBuiltins,PyShadowingNames
@_contextlib.contextmanager
def cast_com(obj: _Union[interface.IUnknown, interface.IUnknown_impl], type: _builtins.type[CT] = interface.IUnknown) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type) as obj_:
        yield obj_ if macro.SUCCEEDED(obj.QueryInterface(*macro.IID_PPV_ARGS(obj_))) else None


@_contextlib.contextmanager
def _prep_winrt(type_: _builtins.type[CT], init: bool) -> _ContextManager[tuple[type.HSTRING,
                                                                                _Optional[Pointer[struct.IID]],
                                                                                Pointer[interface.IInspectable]]]:
    lib.Combase.RoInitialize(enum.RO_INIT_TYPE.MULTITHREADED if THREADED_COM else enum.RO_INIT_TYPE.SINGLETHREADED)
    base = (interface.IInspectable if init else interface.IActivationFactory)()
    try:
        yield handle.HSTRING.from_string(_get_winrt_class_name(type_)), None if init else macro.__uuidof(type_), base
    finally:
        if base:
            base.Release()
        lib.Combase.RoUninitialize()


# noinspection PyShadowingBuiltins,PyShadowingNames
@_contextlib.contextmanager
def get_winrt(type: _builtins.type[CT], init: bool = False) -> _ContextManager[_Optional[CT]]:
    with _prep_winrt(type, init) as (*args, base):
        if macro.SUCCEEDED(lib.Combase.RoActivateInstance(args[0], byref(
                base)) if init else lib.Combase.RoGetActivationFactory(*args, byref(base))):
            with cast_com(base, type) as obj:
                yield obj
        else:
            yield


class Async(_Generic[CT]):
    _completed = None
    _progress = None
    _completed_callback = None
    _completed_args = None
    _completed_kwargs = None
    _progress_callback = None
    _progress_args = None
    _progress_kwargs = None

    # noinspection PyProtectedMember,PyShadowingBuiltins,PyShadowingNames
    @staticmethod
    def _get_completed_handler(async_type):
        handler = None
        if issubclass(async_type, interface.Windows.Foundation.IAsyncAction):
            handler = interface.Windows.Foundation.IAsyncActionCompletedHandler
        elif issubclass(async_type, interface.Windows.Foundation.IAsyncActionWithProgress):
            handler = interface.Windows.Foundation.IAsyncActionWithProgressCompletedHandler
        elif issubclass(async_type, interface.Windows.Foundation.IAsyncOperation):
            handler = interface.Windows.Foundation.IAsyncOperationCompletedHandler
        elif issubclass(async_type, interface.Windows.Foundation.IAsyncOperationWithProgress):
            handler = interface.Windows.Foundation.IAsyncOperationWithProgressCompletedHandler
        if getattr(async_type, '_args', None):
            handler = handler[tuple(async_type._args.values())]
        return handler

    @staticmethod
    def _get_progress_handler(async_type):
        handler = None
        if issubclass(async_type, interface.Windows.Foundation.IAsyncActionWithProgress):
            handler = interface.Windows.Foundation.IAsyncActionProgressHandler
        elif issubclass(async_type, interface.Windows.Foundation.IAsyncOperationWithProgress):
            handler = interface.Windows.Foundation.IAsyncOperationProgressHandler
        if getattr(async_type, '_args', None):
            # noinspection PyProtectedMember
            handler = handler[tuple(async_type._args.values())]
        return handler

    # noinspection PyShadowingBuiltins,PyShadowingNames
    def __init__(self, type: _builtins.type[CT] = interface.Windows.Foundation.IAsyncAction):
        self._async: CT = type()
        self._info = interface.IAsyncInfo()
        self._event = _threading.Event()

    def __del__(self):
        if self._async:
            if self._completed:
                self._completed.Release()
                self._completed = None
            if self._progress:
                self._progress.Release()
                self._progress = None
            if self._info:
                self._info.Release()
                self._info = None
            self._async.Release()
            self._async = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__del__()

    def _get_info(self) -> interface.IAsyncInfo:
        if not self._info:
            self._async.QueryInterface(*macro.IID_PPV_ARGS(self._info))
        return self._info

    def _put(self, put: _Callable, handler):
        put(handler) if THREADED_COM else _threading.Thread(
            target=put, name=f'{__name__}-{__version__}-{_builtins.type(self).__name__}'
                             f'({_builtins.type(self._async).__name__}.{put.__name__})', args=(handler,)).start()

    def get_ref(self) -> Pointer[CT]:
        return byref(self._async)

    def get_status(self) -> enum.Windows.Foundation.AsyncStatus:
        status = enum.Windows.Foundation.AsyncStatus()
        self._get_info().get_Status(byref(status))
        return status

    def get_error_code(self) -> _Optional[int]:
        hresult = type.HRESULT()
        self._get_info().get_ErrorCode(byref(hresult))
        return hresult.value

    def cancel(self) -> bool:
        return macro.SUCCEEDED(self._get_info().Cancel())

    def close(self) -> bool:
        return macro.SUCCEEDED(self._get_info().Close())

    def _completed_handler(self, _, __):
        self._completed_callback(self.get_results(), *self._completed_args, **self._completed_kwargs)
        return const.NOERROR

    def _progress_handler(self, _, progress):
        self._progress_callback(progress, *self._progress_args, **self._progress_kwargs)
        return const.NOERROR

    # noinspection PyProtectedMember
    def put_completed(self, callback: _Callable[[CT[interface._TResult], ...], _Any],
                      args: _Optional[_Iterable] = None, kwargs: _Optional[_Mapping[str, _Any]] = None) -> enum.Windows.Foundation.AsyncStatus:
        if self._completed:
            self._completed.Release()
            self._completed = None
        self._completed_callback = callback
        self._completed_args = () if args is None else args
        self._completed_kwargs = {} if kwargs is None else kwargs
        self._completed = create_handler(self._completed_handler, self._get_completed_handler(_builtins.type(self._async)))
        self._put(self._async.put_Completed, self._completed)
        return self.get_status()

    # noinspection PyProtectedMember
    def put_progress(self, callback: _Callable[[CT[interface._TProgress], ...], _Any],
                     args: _Optional[_Iterable] = None, kwargs: _Optional[_Mapping[str, _Any]] = None) -> enum.Windows.Foundation.AsyncStatus:
        if self._progress:
            self._progress.Release()
            self._progress = None
        self._progress_callback = callback
        self._progress_args = () if args is None else args
        self._progress_kwargs = {} if kwargs is None else kwargs
        self._progress = create_handler(self._progress_handler, self._get_progress_handler(_builtins.type(self._async)))
        self._put(self._async.put_Progress, self._progress)
        return self.get_status()

    # noinspection PyProtectedMember
    def get_results(self: Async[CT[interface._TResult]]) -> _Optional[interface._TResult]:
        t_result = self._async._args.get(interface._TResult, None) if isinstance(self._async, interface._Template) else None
        if t_result:
            result = t_result()
            # noinspection PyUnresolvedReferences
            self._async.GetResults(byref(result))
            return result

    # noinspection PyProtectedMember
    def get(self: Async[CT[interface._TResult]]) -> _Optional[interface._TResult]:
        if enum.Windows.Foundation.AsyncStatus.Completed == self.wait_for():
            return self.get_results()

    def wait_for(self, timeout: _Optional[float] = None) -> enum.Windows.Foundation.AsyncStatus:
        self.put_completed(lambda _: self._event.set())
        self._event.wait(timeout)
        self.cancel()
        return self.get_status()
