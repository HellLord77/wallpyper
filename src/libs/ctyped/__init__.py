__version__ = '0.2.6'

import builtins as _builtins
import contextlib as _contextlib
import threading as _threading
import typing as _typing
from typing import (Any as _Any, Callable as _Callable, ContextManager as _ContextManager,
                    Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union)

from . import __head__
from . import _com as com
from . import _com_impl as com_impl
from . import _const as const
from . import _enum as enum
from . import _func as func
from . import _handle as handle
from . import _macro as macro
from . import _struct as struct
# noinspection PyShadowingBuiltins
from . import _type as type
from . import _union as union
from .__head__ import _CT as CT
from .__head__ import _Pointer as Pointer
from .__head__ import _addressof as addressof
from .__head__ import _byref as byref
from .__head__ import _cast as cast
from .__head__ import _pointer as pointer
from .__head__ import _sizeof as sizeof

THREADED_COM = True


# noinspection PyProtectedMember
def set_error_checker(lib: func._CDLL, callback: _Optional[_Callable[[_Any, _Callable, tuple], _Any]] = None):
    lib._errcheck = callback
    for func_ in lib._funcs:
        if func_ in dir(lib):
            getattr(lib, func_).errcheck = callback


@_contextlib.contextmanager
def buffer(size: int = 0) -> _ContextManager[_Optional[int]]:
    ptr = func.msvcrt.malloc(size)
    try:
        yield None if ptr == 0 else ptr
    finally:
        func.msvcrt.free(ptr)


def array(type_: _builtins.type[CT] = type.c_void_p, *elements: _Any, size: _Optional[int] = None) -> Pointer[CT]:
    return (type_ * (size or len(elements)))(*elements)


@_typing.overload
def char_array(string: bytes) -> Pointer[type.c_char]:
    pass


@_typing.overload
def char_array(string: str) -> Pointer[type.c_wchar]:
    pass


def char_array(string):
    return ((type.c_char if isinstance(string, bytes) else type.c_wchar) * (len(string) + 1))(*string)


def get_guid(string: str) -> struct.GUID:
    guid = struct.GUID()
    func.shell32.GUIDFromStringW(string, byref(guid))
    return guid


@_contextlib.contextmanager
def _prep_com(type_: _builtins.type[CT]) -> _ContextManager[tuple[CT, Pointer[struct.CLSID],
                                                                  tuple[Pointer[struct.IID], Pointer[CT]]]]:
    func.ole32.CoInitializeEx(None,
                              enum.COINIT.COINIT_MULTITHREADED.value) if THREADED_COM else func.ole32.CoInitialize(None)
    obj = type_()
    try:
        yield obj, byref(get_guid(type_.__CLSID__)) if type_.__CLSID__ else None, macro.IID_PPV_ARGS(obj)
    finally:
        if obj:
            obj.Release()
        func.ole32.CoUninitialize()


@_contextlib.contextmanager
def init_com(type_: _builtins.type[CT], init: bool = True) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type_) as (obj, clsid_ref, args):
        yield obj if not init or macro.SUCCEEDED(
            func.ole32.CoCreateInstance(clsid_ref, None, const.CLSCTX_ALL, *args)) else None


# noinspection PyProtectedMember
@_contextlib.contextmanager
def conv_com(obj: com.IUnknown, type_: _builtins.type[CT] = com_impl.IUnknown) -> _ContextManager[_Optional[CT]]:
    with _prep_com(type_) as (obj_, _, args):
        if macro.SUCCEEDED(obj.QueryInterface(*args)):
            yield obj_
        else:
            yield None


@_contextlib.contextmanager
def _prep_winrt(type_: _builtins.type[CT]) -> _ContextManager[tuple[type.HSTRING, Pointer[struct.IID],
                                                                    Pointer[com.IActivationFactory]]]:
    func.combase.RoInitialize(
        enum.RO_INIT_TYPE.RO_INIT_MULTITHREADED if THREADED_COM else enum.RO_INIT_TYPE.RO_INIT_SINGLETHREADED)
    factory = com.IActivationFactory()
    try:
        yield handle.HSTRING.from_string(type_.__RuntimeClass__), macro.__uuidof(type_.__name__), factory
    finally:
        if factory:
            factory.Release()
        func.combase.RoUninitialize()


@_contextlib.contextmanager
def get_winrt(type_: _builtins.type[CT]) -> _ContextManager[_Optional[_builtins.type[CT]]]:  # TODO init: bool = False
    with _prep_winrt(type_) as (*args, factory):
        if macro.SUCCEEDED(func.combase.RoGetActivationFactory(*args, byref(factory))):
            with conv_com(factory, type_) as obj:
                yield obj
        else:
            yield None


class Async:
    _completed = None
    _progress = None
    _info_ = None

    class _AsyncCompletedHandler(com_impl.IAsyncActionCompletedHandler,
                                 com_impl.IAsyncActionWithProgressCompletedHandler,
                                 com_impl.IAsyncOperationCompletedHandler,
                                 com_impl.IAsyncOperationWithProgressCompletedHandler):
        def __init__(self):
            super().__init__()
            self.event = _threading.Event()

        def Invoke(self, _: type.c_void_p, __: type.c_void_p, ___: type.c_void_p) -> type.HRESULT:
            self.event.set()
            return const.NOERROR

    class _AsyncProgressHandler(com_impl.IAsyncActionProgressHandler, com_impl.IAsyncOperationProgressHandler):
        callback = None
        args = None
        kwargs = None

        @classmethod
        def init(cls, type_: _builtins.type[CT], callback: _Callable[[CT, ...], _Any],
                 args: _Iterable, kwargs: _Mapping[str, _Any]):
            cls.Invoke.__annotations__['progress'] = type_
            handler = cls()
            handler.callback = callback
            handler.args = args
            handler.kwargs = kwargs
            return handler

        def Invoke(self, _: type.c_void_p, __: type.c_void_p, progress: type.c_void_p) -> type.HRESULT:
            self.callback(progress, *self.args, **self.kwargs)
            return const.NOERROR

    def __init__(self, type_: _Union[_builtins.type[com.IAsyncAction],
                                     _builtins.type[com.IAsyncActionWithProgress],
                                     _builtins.type[com.IAsyncOperation],
                                     _builtins.type[com.IAsyncOperationWithProgress]] = com.IAsyncAction):
        self._async = type_()

    def __del__(self):
        if self._async:
            if self._completed:
                self._completed.Release()
            if self._progress:
                self._progress.Release()
            if self._info_:
                self._info_.Release()
            self._async.Release()

    @property
    def _info(self):
        if self._info_ is None:
            info = com.IAsyncInfo()
            if macro.SUCCEEDED(self._async.QueryInterface(*macro.IID_PPV_ARGS(info))):
                self._info_ = info
        return self._info_

    def _put(self, putter: _Callable, handler: _Union[_AsyncCompletedHandler, _AsyncProgressHandler]):
        putter(handler) if THREADED_COM else _threading.Thread(
            target=putter, name=f'{__name__}-{__version__}-{_builtins.type(self).__name__}'
                                f'({_builtins.type(self._async).__name__}.{putter.__name__})', args=(handler,)).start()

    def get_ref(self) -> _Union[Pointer[com.IAsyncAction], Pointer[com.IAsyncActionWithProgress],
                                Pointer[com.IAsyncOperation], Pointer[com.IAsyncOperationWithProgress]]:
        return byref(self._async)

    def get_status(self) -> _Optional[int]:
        status = enum.AsyncStatus()
        self._info.get_Status(byref(status))
        return status.value

    def get_error_code(self) -> _Optional[int]:
        hresult = type.HRESULT()
        self._info.get_ErrorCode(byref(hresult))
        return hresult.value

    def cancel(self) -> bool:
        return macro.SUCCEEDED(self._info.Cancel())

    def close(self) -> bool:
        return macro.SUCCEEDED(self._info.Close())

    def put_progress(self, type_: _builtins.type[CT], callback: _Callable[[CT, ...], _Any],
                     args: _Optional[_Iterable] = None, kwargs: _Optional[_Mapping[str, _Any]] = None) -> int:
        self._progress = self._AsyncProgressHandler.init(type_, callback, () if args is None else args,
                                                         {} if kwargs is None else kwargs)
        self._put(self._async.put_Progress, self._progress)
        return self.get_status()

    def get_results(self, obj_ref: _Optional[Pointer[CT]] = None) -> bool:
        try:
            return macro.SUCCEEDED(self._async.GetResults(*() if obj_ref is None else (obj_ref,)))
        except OSError:
            return False

    def get(self, type_: _Optional[_builtins.type[CT]] = None) -> _Optional[CT]:
        obj = None if type_ is None else type_()
        if enum.AsyncStatus.Completed == self.wait_for():
            self.get_results(None if obj is None else byref(obj))
        return obj

    def wait_for(self, timeout: _Optional[float] = None) -> int:
        self._completed = self._AsyncCompletedHandler()
        self._put(self._async.put_Completed, self._completed)
        self._completed.event.wait(timeout)
        self.cancel()
        return self.get_status()
