from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _ITimerDestroyedHandler:
    Invoke: _Callable[[IThreadPoolTimer],  # timer
                      _type.HRESULT]


class ITimerDestroyedHandler(_ITimerDestroyedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITimerDestroyedHandler_impl(_ITimerDestroyedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ITimerElapsedHandler:
    Invoke: _Callable[[IThreadPoolTimer],  # timer
                      _type.HRESULT]


class ITimerElapsedHandler(_ITimerElapsedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ITimerElapsedHandler_impl(_ITimerElapsedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IWorkItemHandler:
    Invoke: _Callable[[_Windows_Foundation.IAsyncAction],  # operation
                      _type.HRESULT]


class IWorkItemHandler(_IWorkItemHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IWorkItemHandler_impl(_IWorkItemHandler, _Unknwnbase.IUnknown_impl):
    pass


class IThreadPoolStatics(_inspectable.IInspectable):
    RunAsync: _Callable[[IWorkItemHandler,  # handler
                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                        _type.HRESULT]
    RunWithPriorityAsync: _Callable[[IWorkItemHandler,  # handler
                                     _enum.Windows.System.Threading.WorkItemPriority,  # priority
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                    _type.HRESULT]
    RunWithPriorityAndOptionsAsync: _Callable[[IWorkItemHandler,  # handler
                                               _enum.Windows.System.Threading.WorkItemPriority,  # priority
                                               _enum.Windows.System.Threading.WorkItemOptions,  # options
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]

    _factory = True


class IThreadPoolTimer(_inspectable.IInspectable):
    get_Period: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                          _type.HRESULT]
    get_Delay: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                         _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]


class IThreadPoolTimerStatics(_inspectable.IInspectable):
    CreatePeriodicTimer: _Callable[[ITimerElapsedHandler,  # handler
                                    _struct.Windows.Foundation.TimeSpan,  # period
                                    _Pointer[IThreadPoolTimer]],  # timer
                                   _type.HRESULT]
    CreateTimer: _Callable[[ITimerElapsedHandler,  # handler
                            _struct.Windows.Foundation.TimeSpan,  # delay
                            _Pointer[IThreadPoolTimer]],  # timer
                           _type.HRESULT]
    CreatePeriodicTimerWithCompletion: _Callable[[ITimerElapsedHandler,  # handler
                                                  _struct.Windows.Foundation.TimeSpan,  # period
                                                  ITimerDestroyedHandler,  # destroyed
                                                  _Pointer[IThreadPoolTimer]],  # timer
                                                 _type.HRESULT]
    CreateTimerWithCompletion: _Callable[[ITimerElapsedHandler,  # handler
                                          _struct.Windows.Foundation.TimeSpan,  # delay
                                          ITimerDestroyedHandler,  # destroyed
                                          _Pointer[IThreadPoolTimer]],  # timer
                                         _type.HRESULT]

    _factory = True
