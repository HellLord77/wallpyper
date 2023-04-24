from __future__ import annotations

from typing import Callable as _Callable

from ... import UserDataTasks as _Windows_ApplicationModel_UserDataTasks
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IUserDataTaskDataProviderConnection(_inspectable.IInspectable):
    add_CreateOrUpdateTaskRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataTaskDataProviderConnection, IUserDataTaskListCreateOrUpdateTaskRequestEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_CreateOrUpdateTaskRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_SyncRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataTaskDataProviderConnection, IUserDataTaskListSyncManagerSyncRequestEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SyncRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_SkipOccurrenceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataTaskDataProviderConnection, IUserDataTaskListSkipOccurrenceRequestEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_SkipOccurrenceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_CompleteTaskRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataTaskDataProviderConnection, IUserDataTaskListCompleteTaskRequestEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_CompleteTaskRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_DeleteTaskRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataTaskDataProviderConnection, IUserDataTaskListDeleteTaskRequestEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_DeleteTaskRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IUserDataTaskDataProviderTriggerDetails(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IUserDataTaskDataProviderConnection]],  # value
                              _type.HRESULT]


class IUserDataTaskListCompleteTaskRequest(_inspectable.IInspectable):
    get_TaskListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_TaskId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    ReportCompletedAsync: _Callable[[_type.HSTRING,  # completedTaskId
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IUserDataTaskListCompleteTaskRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IUserDataTaskListCompleteTaskRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IUserDataTaskListCreateOrUpdateTaskRequest(_inspectable.IInspectable):
    get_TaskListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Task: _Callable[[_Pointer[_Windows_ApplicationModel_UserDataTasks.IUserDataTask]],  # value
                        _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_ApplicationModel_UserDataTasks.IUserDataTask,  # createdOrUpdatedUserDataTask
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IUserDataTaskListCreateOrUpdateTaskRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IUserDataTaskListCreateOrUpdateTaskRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IUserDataTaskListDeleteTaskRequest(_inspectable.IInspectable):
    get_TaskListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_TaskId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IUserDataTaskListDeleteTaskRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IUserDataTaskListDeleteTaskRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IUserDataTaskListSkipOccurrenceRequest(_inspectable.IInspectable):
    get_TaskListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_TaskId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IUserDataTaskListSkipOccurrenceRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IUserDataTaskListSkipOccurrenceRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IUserDataTaskListSyncManagerSyncRequest(_inspectable.IInspectable):
    get_TaskListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IUserDataTaskListSyncManagerSyncRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IUserDataTaskListSyncManagerSyncRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
