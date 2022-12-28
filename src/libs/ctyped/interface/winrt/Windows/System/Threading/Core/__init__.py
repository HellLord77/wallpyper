from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Threading as _Windows_System_Threading
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _ISignalHandler:
    Invoke: _Callable[[ISignalNotifier,  # signalNotifier
                       _type.boolean],  # timedOut
                      _type.HRESULT]


class ISignalHandler(_ISignalHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ISignalHandler_impl(_ISignalHandler, _Unknwnbase.IUnknown_impl):
    pass


class IPreallocatedWorkItem(_inspectable.IInspectable):
    RunAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                        _type.HRESULT]


class IPreallocatedWorkItemFactory(_inspectable.IInspectable):
    CreateWorkItem: _Callable[[_Windows_System_Threading.IWorkItemHandler,  # handler
                               _Pointer[IPreallocatedWorkItem]],  # workItem
                              _type.HRESULT]
    CreateWorkItemWithPriority: _Callable[[_Windows_System_Threading.IWorkItemHandler,  # handler
                                           _enum.Windows.System.Threading.WorkItemPriority,  # priority
                                           _Pointer[IPreallocatedWorkItem]],  # WorkItem
                                          _type.HRESULT]
    CreateWorkItemWithPriorityAndOptions: _Callable[[_Windows_System_Threading.IWorkItemHandler,  # handler
                                                     _enum.Windows.System.Threading.WorkItemPriority,  # priority
                                                     _enum.Windows.System.Threading.WorkItemOptions,  # options
                                                     _Pointer[IPreallocatedWorkItem]],  # WorkItem
                                                    _type.HRESULT]

    _factory = True


class ISignalNotifier(_inspectable.IInspectable):
    Enable: _Callable[[],
                      _type.HRESULT]
    Terminate: _Callable[[],
                         _type.HRESULT]


class ISignalNotifierStatics(_inspectable.IInspectable):
    AttachToEvent: _Callable[[_type.HSTRING,  # name
                              ISignalHandler,  # handler
                              _Pointer[ISignalNotifier]],  # signalNotifier
                             _type.HRESULT]
    AttachToEventWithTimeout: _Callable[[_type.HSTRING,  # name
                                         ISignalHandler,  # handler
                                         _struct.Windows.Foundation.TimeSpan,  # timeout
                                         _Pointer[ISignalNotifier]],  # signalNotifier
                                        _type.HRESULT]
    AttachToSemaphore: _Callable[[_type.HSTRING,  # name
                                  ISignalHandler,  # handler
                                  _Pointer[ISignalNotifier]],  # signalNotifier
                                 _type.HRESULT]
    AttachToSemaphoreWithTimeout: _Callable[[_type.HSTRING,  # name
                                             ISignalHandler,  # handler
                                             _struct.Windows.Foundation.TimeSpan,  # timeout
                                             _Pointer[ISignalNotifier]],  # signalNotifier
                                            _type.HRESULT]

    _factory = True
