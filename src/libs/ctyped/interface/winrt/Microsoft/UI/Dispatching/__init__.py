from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ....Windows import Foundation as _Windows_Foundation
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IDispatcherQueueHandler:
    Invoke: _Callable[[],
                      _type.HRESULT]


class IDispatcherQueueHandler(_IDispatcherQueueHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDispatcherQueueHandler_impl(_IDispatcherQueueHandler, _Unknwnbase.IUnknown_impl):
    pass


class IDispatcherExitDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IDispatcherQueue(_inspectable.IInspectable):
    CreateTimer: _Callable[[_Pointer[IDispatcherQueueTimer]],  # result
                           _type.HRESULT]
    TryEnqueue: _Callable[[IDispatcherQueueHandler,  # callback
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    TryEnqueueWithPriority: _Callable[[_enum.Microsoft.UI.Dispatching.DispatcherQueuePriority,  # priority
                                       IDispatcherQueueHandler,  # callback
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    add_ShutdownStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueue, IDispatcherQueueShutdownStartingEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_ShutdownStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_ShutdownCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueue, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ShutdownCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IDispatcherQueue2(_inspectable.IInspectable):
    get_HasThreadAccess: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]


class IDispatcherQueue3(_inspectable.IInspectable):
    EnqueueEventLoopExit: _Callable[[],
                                    _type.HRESULT]
    EnsureSystemDispatcherQueue: _Callable[[],
                                           _type.HRESULT]
    RunEventLoop: _Callable[[],
                            _type.HRESULT]
    RunEventLoopWithOptions: _Callable[[_enum.Microsoft.UI.Dispatching.DispatcherRunOptions,  # options
                                        IDispatcherExitDeferral],  # deferral
                                       _type.HRESULT]
    add_FrameworkShutdownStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueue, IDispatcherQueueShutdownStartingEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_FrameworkShutdownStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_FrameworkShutdownCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueue, _inspectable.IInspectable],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_FrameworkShutdownCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


class IDispatcherQueueController(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[IDispatcherQueue]],  # value
                                   _type.HRESULT]
    ShutdownQueueAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                  _type.HRESULT]


class IDispatcherQueueController2(_inspectable.IInspectable):
    ShutdownQueue: _Callable[[],
                             _type.HRESULT]


class IDispatcherQueueControllerStatics(_inspectable.IInspectable, factory=True):
    CreateOnDedicatedThread: _Callable[[_Pointer[IDispatcherQueueController]],  # result
                                       _type.HRESULT]
    CreateOnCurrentThread: _Callable[[_Pointer[IDispatcherQueueController]],  # result
                                     _type.HRESULT]


class IDispatcherQueueShutdownStartingEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IDispatcherQueueStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentThread: _Callable[[_Pointer[IDispatcherQueue]],  # result
                                   _type.HRESULT]


class IDispatcherQueueTimer(_inspectable.IInspectable):
    get_Interval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Interval: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_IsRunning: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_IsRepeating: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsRepeating: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_Tick: _Callable[[_Windows_Foundation.ITypedEventHandler[IDispatcherQueueTimer, _inspectable.IInspectable],  # handler
                         _Pointer[_struct.EventRegistrationToken]],  # token
                        _type.HRESULT]
    remove_Tick: _Callable[[_struct.EventRegistrationToken],  # token
                           _type.HRESULT]
