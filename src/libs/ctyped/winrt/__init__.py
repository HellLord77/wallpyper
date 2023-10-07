from __future__ import annotations

import functools as _functools
import threading as _threading
from typing import Callable as _Callable
from typing import Generic as _Generic
from typing import Optional as _Optional

from .. import byref as _byref
from .. import const as _const
from .. import enum as _enum
from .. import interface as _interface
from .. import macro as _macro
from .. import type as _type
from .._utils import _Pointer
# noinspection PyProtectedMember
from ..interface import _TProgress
from ..interface import _TResult
from ..interface.winrt import asyncinfo as _asyncinfo
from ..interface.winrt import inspectable as _inspectable
from ..interface.winrt.Windows import Foundation as _Windows_Foundation


class _AsyncInfo:
    def __init__(self, winrt_or_interface, /):
        self._obj = _interface.WinRT[_asyncinfo.IAsyncInfo](winrt_or_interface)

    @property
    def id(self) -> _Optional[_type.c_uint32]:
        prop = _type.c_uint32()
        with self._obj as obj:
            if _macro.SUCCEEDED(obj.get_Id(_byref(prop))):
                return prop

    @property
    def status(self) -> _Optional[_enum.Windows.Foundation.AsyncStatus]:
        prop = _enum.Windows.Foundation.AsyncStatus()
        with self._obj as obj:
            if _macro.SUCCEEDED(obj.get_Status(_byref(prop))):
                return prop

    @property
    def error_code(self) -> _Optional[_type.HRESULT]:
        prop = _type.HRESULT()
        with self._obj as obj:
            if _macro.SUCCEEDED(obj.get_ErrorCode(_byref(prop))):
                return prop

    def cancel(self) -> bool:
        with self._obj as obj:
            return _macro.SUCCEEDED(obj.Cancel())

    def close(self) -> bool:
        with self._obj as obj:
            return _macro.SUCCEEDED(obj.Close())


class _Async:
    _t: type[_inspectable.IInspectable]
    _t_completed: type[_inspectable.IInspectable]
    _completed: _interface.COM

    def __init__(self):
        self._obj = _interface.WinRT[self._t]()

    def __del__(self):
        self.cancel()
        self._info.close()

    def __invert__(self) -> _Pointer:
        return ~self._obj

    def __bool__(self):
        return bool(self._obj)

    @_functools.cached_property
    def _info(self) -> _AsyncInfo:
        with self._obj as obj:
            return _AsyncInfo(obj)

    def get_status(self) -> _Optional[_enum.Windows.Foundation.AsyncStatus]:
        return self._info.status

    def get_error_code(self) -> _Optional[_type.HRESULT]:
        return self._info.error_code

    def cancel(self) -> bool:
        return self._info.cancel()

    def on_completed(self, callback: _Callable[[_Async], _type.HRESULT]) -> bool:
        self._completed = _interface.create_handler(_functools.wraps(
            callback)(_functools.partial(callback, self)), self._t_completed)
        with self._obj as obj, self._completed as handler:
            return _macro.SUCCEEDED(obj.put_Completed(handler))

    def get_results(self):
        with self._obj as obj:
            obj.GetResults()

    def wait(self, timeout: _Optional[float] = None) -> _enum.Windows.Foundation.AsyncStatus:
        event = _threading.Event()

        def handler(*_):
            event.set()
            return _const.NOERROR

        self.on_completed(handler)
        event.wait(timeout)
        self.cancel()
        return self.get_status()

    def get(self) -> _Optional[_TResult]:
        if self.wait() == _enum.Windows.Foundation.AsyncStatus.Completed:
            return self.get_results()


class _AsyncWithProgress(_Async):
    _t_progress: type[_inspectable.IInspectable]
    _progress: _interface.COM

    def on_progress(self, callback: _Callable[[_Async], _type.HRESULT]) -> bool:
        self._progress = _interface.create_handler(_functools.wraps(
            callback)(_functools.partial(callback, self)), self._t_progress)
        with self._obj as obj, self._progress as handler:
            return _macro.SUCCEEDED(obj.put_Progress(handler))


class AsyncAction(_Async):
    _t = _Windows_Foundation.IAsyncAction
    _t_completed = _Windows_Foundation.IAsyncActionCompletedHandler


class AsyncActionWithProgress(_AsyncWithProgress, _Generic[_TProgress]):
    def __init__(self, progress: type[_TProgress]):
        self._t = _Windows_Foundation.IAsyncActionWithProgress[progress]
        self._t_progress = _Windows_Foundation.IAsyncActionProgressHandler[progress]
        self._t_completed = _Windows_Foundation.IAsyncActionWithProgressCompletedHandler[progress]
        super().__init__()


class _AsyncOperation(_Async):
    _t_result: type[_TResult]

    def get_results(self) -> _Optional[_TResult]:
        result = self._t_result()
        with self._obj as obj:
            if _macro.SUCCEEDED(obj.GetResults(_byref(result))):
                return result


class AsyncOperation(_AsyncOperation, _Generic[_TResult]):
    def __init__(self, result: type[_TResult]):
        self._t_result = result
        self._t = _Windows_Foundation.IAsyncOperation[result]
        self._t_completed = _Windows_Foundation.IAsyncOperationCompletedHandler[result]
        super().__init__()


class AsyncOperationWithProgress(_AsyncOperation, _AsyncWithProgress, _Generic[_TResult, _TProgress]):
    def __init__(self, result: type[_TResult], progress: type[_TProgress]):
        self._t_result = result
        self._t = _Windows_Foundation.IAsyncOperationWithProgress[result, progress]
        self._t_progress = _Windows_Foundation.IAsyncOperationProgressHandler[result, progress]
        self._t_completed = _Windows_Foundation.IAsyncOperationWithProgressCompletedHandler[result, progress]
        super().__init__()
