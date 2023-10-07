from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IUserDataTask(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_ListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_CompletedDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                 _type.HRESULT]
    put_CompletedDate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                 _type.HRESULT]
    get_Details: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Details: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_DetailsKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind]],  # value
                               _type.HRESULT]
    put_DetailsKind: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind],  # value
                               _type.HRESULT]
    get_DueDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                           _type.HRESULT]
    put_DueDate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                           _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskKind]],  # value
                        _type.HRESULT]
    get_Priority: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority]],  # value
                            _type.HRESULT]
    put_Priority: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority],  # value
                            _type.HRESULT]
    get_RecurrenceProperties: _Callable[[_Pointer[IUserDataTaskRecurrenceProperties]],  # value
                                        _type.HRESULT]
    put_RecurrenceProperties: _Callable[[IUserDataTaskRecurrenceProperties],  # value
                                        _type.HRESULT]
    get_RegenerationProperties: _Callable[[_Pointer[IUserDataTaskRegenerationProperties]],  # value
                                          _type.HRESULT]
    put_RegenerationProperties: _Callable[[IUserDataTaskRegenerationProperties],  # value
                                          _type.HRESULT]
    get_Reminder: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                            _type.HRESULT]
    put_Reminder: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    get_Sensitivity: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity]],  # value
                               _type.HRESULT]
    put_Sensitivity: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity],  # value
                               _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Subject: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_StartDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                             _type.HRESULT]
    put_StartDate: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]


class IUserDataTaskBatch(_inspectable.IInspectable):
    get_Tasks: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUserDataTask]]],  # value
                         _type.HRESULT]


class IUserDataTaskList(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_UserDataAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_SourceDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_OtherAppReadAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess]],  # value
                                      _type.HRESULT]
    put_OtherAppReadAccess: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess],  # value
                                      _type.HRESULT]
    get_OtherAppWriteAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess]],  # value
                                       _type.HRESULT]
    put_OtherAppWriteAccess: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess],  # value
                                       _type.HRESULT]
    get_LimitedWriteOperations: _Callable[[_Pointer[IUserDataTaskListLimitedWriteOperations]],  # value
                                          _type.HRESULT]
    get_SyncManager: _Callable[[_Pointer[IUserDataTaskListSyncManager]],  # value
                               _type.HRESULT]
    RegisterSyncManagerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]
    GetTaskReader: _Callable[[_Pointer[IUserDataTaskReader]],  # result
                             _type.HRESULT]
    GetTaskReaderWithOptions: _Callable[[IUserDataTaskQueryOptions,  # options
                                         _Pointer[IUserDataTaskReader]],  # value
                                        _type.HRESULT]
    GetTaskAsync: _Callable[[_type.HSTRING,  # userDataTask
                             _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataTask]]],  # operation
                            _type.HRESULT]
    SaveTaskAsync: _Callable[[IUserDataTask,  # userDataTask
                              _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                             _type.HRESULT]
    DeleteTaskAsync: _Callable[[_type.HSTRING,  # userDataTaskId
                                _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                               _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                           _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                         _type.HRESULT]


class IUserDataTaskListLimitedWriteOperations(_inspectable.IInspectable):
    TryCompleteTaskAsync: _Callable[[_type.HSTRING,  # userDataTaskId
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                    _type.HRESULT]
    TryCreateOrUpdateTaskAsync: _Callable[[IUserDataTask,  # userDataTask
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    TryDeleteTaskAsync: _Callable[[_type.HSTRING,  # userDataTaskId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                  _type.HRESULT]
    TrySkipOccurrenceAsync: _Callable[[_type.HSTRING,  # userDataTaskId
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]


class IUserDataTaskListSyncManager(_inspectable.IInspectable):
    get_LastAttemptedSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                         _type.HRESULT]
    put_LastAttemptedSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                         _type.HRESULT]
    get_LastSuccessfulSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                          _type.HRESULT]
    put_LastSuccessfulSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                          _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus]],  # value
                          _type.HRESULT]
    put_Status: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus],  # value
                          _type.HRESULT]
    SyncAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                         _type.HRESULT]
    add_SyncStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IUserDataTaskListSyncManager, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SyncStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IUserDataTaskManager(_inspectable.IInspectable):
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskStoreAccessType,  # accessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataTaskStore]]],  # operation
                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IUserDataTaskManagerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IUserDataTaskManager]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IUserDataTaskManager]],  # result
                          _type.HRESULT]


class IUserDataTaskQueryOptions(_inspectable.IInspectable):
    get_SortProperty: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty]],  # value
                                _type.HRESULT]
    put_SortProperty: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty],  # value
                                _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind],  # value
                        _type.HRESULT]


class IUserDataTaskReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IUserDataTaskBatch]]],  # result
                              _type.HRESULT]


class IUserDataTaskRecurrenceProperties(_inspectable.IInspectable):
    get_Unit: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit]],  # value
                        _type.HRESULT]
    put_Unit: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit],  # value
                        _type.HRESULT]
    get_Occurrences: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                               _type.HRESULT]
    put_Occurrences: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                               _type.HRESULT]
    get_Until: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                         _type.HRESULT]
    put_Until: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                         _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_Interval: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_DaysOfWeek: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]]],  # value
                              _type.HRESULT]
    put_DaysOfWeek: _Callable[[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]],  # value
                              _type.HRESULT]
    get_WeekOfMonth: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]]],  # value
                               _type.HRESULT]
    put_WeekOfMonth: _Callable[[_Windows_Foundation.IReference[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]],  # value
                               _type.HRESULT]
    get_Month: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                         _type.HRESULT]
    put_Month: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                         _type.HRESULT]
    get_Day: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                       _type.HRESULT]
    put_Day: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                       _type.HRESULT]


class IUserDataTaskRegenerationProperties(_inspectable.IInspectable):
    get_Unit: _Callable[[_Pointer[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit]],  # value
                        _type.HRESULT]
    put_Unit: _Callable[[_enum.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit],  # value
                        _type.HRESULT]
    get_Occurrences: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                               _type.HRESULT]
    put_Occurrences: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                               _type.HRESULT]
    get_Until: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                         _type.HRESULT]
    put_Until: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                         _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_Interval: _Callable[[_type.INT32],  # value
                            _type.HRESULT]


class IUserDataTaskStore(_inspectable.IInspectable):
    CreateListAsync: _Callable[[_type.HSTRING,  # name
                                _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataTaskList]]],  # operation
                               _type.HRESULT]
    CreateListInAccountAsync: _Callable[[_type.HSTRING,  # name
                                         _type.HSTRING,  # userDataAccountId
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataTaskList]]],  # result
                                        _type.HRESULT]
    FindListsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUserDataTaskList]]]],  # operation
                              _type.HRESULT]
    GetListAsync: _Callable[[_type.HSTRING,  # taskListId
                             _Pointer[_Windows_Foundation.IAsyncOperation[IUserDataTaskList]]],  # operation
                            _type.HRESULT]
