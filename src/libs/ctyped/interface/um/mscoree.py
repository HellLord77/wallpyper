from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IObjectHandle(_Unknwnbase.IUnknown):
    Unwrap: _Callable[[_Pointer[_struct.VARIANT]],  # ppv
                      _type.HRESULT]


class IAppDomainBinding(_Unknwnbase.IUnknown):
    OnAppDomain: _Callable[[_Unknwnbase.IUnknown],  # pAppdomain
                           _type.HRESULT]


class IGCThreadControl(_Unknwnbase.IUnknown):
    ThreadIsBlockingForSuspension: _Callable[[],
                                             _type.HRESULT]
    SuspensionStarting: _Callable[[],
                                  _type.HRESULT]
    SuspensionEnding: _Callable[[_type.DWORD],  # Generation
                                _type.HRESULT]


class IGCHostControl(_Unknwnbase.IUnknown):
    RequestVirtualMemLimit: _Callable[[_type.SIZE_T,  # sztMaxVirtualMemMB
                                       _Pointer[_type.SIZE_T]],  # psztNewMaxVirtualMemMB
                                      _type.HRESULT]


class ICorThreadpool(_Unknwnbase.IUnknown):
    CorRegisterWaitForSingleObject: _Callable[[_Pointer[_type.HANDLE],  # phNewWaitObject
                                               _type.HANDLE,  # hWaitObject
                                               _type.WAITORTIMERCALLBACK,  # Callback
                                               _type.PVOID,  # Context
                                               _type.ULONG,  # timeout
                                               _type.BOOL,  # executeOnlyOnce
                                               _Pointer[_type.BOOL]],  # result
                                              _type.HRESULT]
    CorUnregisterWait: _Callable[[_type.HANDLE,  # hWaitObject
                                  _type.HANDLE,  # CompletionEvent
                                  _Pointer[_type.BOOL]],  # result
                                 _type.HRESULT]
    CorQueueUserWorkItem: _Callable[[_type.LPTHREAD_START_ROUTINE,  # Function
                                     _type.PVOID,  # Context
                                     _type.BOOL,  # executeOnlyOnce
                                     _Pointer[_type.BOOL]],  # result
                                    _type.HRESULT]
    CorCreateTimer: _Callable[[_Pointer[_type.HANDLE],  # phNewTimer
                               _type.WAITORTIMERCALLBACK,  # Callback
                               _type.PVOID,  # Parameter
                               _type.DWORD,  # DueTime
                               _type.DWORD,  # Period
                               _Pointer[_type.BOOL]],  # result
                              _type.HRESULT]
    CorChangeTimer: _Callable[[_type.HANDLE,  # Timer
                               _type.ULONG,  # DueTime
                               _type.ULONG,  # Period
                               _Pointer[_type.BOOL]],  # result
                              _type.HRESULT]
    CorDeleteTimer: _Callable[[_type.HANDLE,  # Timer
                               _type.HANDLE,  # CompletionEvent
                               _Pointer[_type.BOOL]],  # result
                              _type.HRESULT]
    CorBindIoCompletionCallback: _Callable[[_type.HANDLE,  # fileHandle
                                            _type.LPOVERLAPPED_COMPLETION_ROUTINE],  # callback
                                           _type.HRESULT]
    CorCallOrQueueUserWorkItem: _Callable[[_type.LPTHREAD_START_ROUTINE,  # Function
                                           _type.PVOID,  # Context
                                           _Pointer[_type.BOOL]],  # result
                                          _type.HRESULT]
    CorSetMaxThreads: _Callable[[_type.DWORD,  # MaxWorkerThreads
                                 _type.DWORD],  # MaxIOCompletionThreads
                                _type.HRESULT]
    CorGetMaxThreads: _Callable[[_Pointer[_type.DWORD],  # MaxWorkerThreads
                                 _Pointer[_type.DWORD]],  # MaxIOCompletionThreads
                                _type.HRESULT]
    CorGetAvailableThreads: _Callable[[_Pointer[_type.DWORD],  # AvailableWorkerThreads
                                       _Pointer[_type.DWORD]],  # AvailableIOCompletionThreads
                                      _type.HRESULT]


class IDebuggerThreadControl(_Unknwnbase.IUnknown):
    ThreadIsBlockingForDebugger: _Callable[[],
                                           _type.HRESULT]
    ReleaseAllRuntimeThreads: _Callable[[],
                                        _type.HRESULT]
    StartBlockingForDebugger: _Callable[[_type.DWORD],  # dwUnused
                                        _type.HRESULT]


class IDebuggerInfo(_Unknwnbase.IUnknown):
    IsDebuggerAttached: _Callable[[_Pointer[_type.BOOL]],  # pbAttached
                                  _type.HRESULT]


class ICorConfiguration(_Unknwnbase.IUnknown):
    SetGCThreadControl: _Callable[[IGCThreadControl],  # pGCThreadControl
                                  _type.HRESULT]
    SetGCHostControl: _Callable[[IGCHostControl],  # pGCHostControl
                                _type.HRESULT]
    SetDebuggerThreadControl: _Callable[[IDebuggerThreadControl],  # pDebuggerThreadControl
                                        _type.HRESULT]
    AddDebuggerSpecialThread: _Callable[[_type.DWORD],  # dwSpecialThreadId
                                        _type.HRESULT]


class ICorRuntimeHost(_Unknwnbase.IUnknown):
    CreateLogicalThreadState: _Callable[[],
                                        _type.HRESULT]
    DeleteLogicalThreadState: _Callable[[],
                                        _type.HRESULT]
    SwitchInLogicalThreadState: _Callable[[_Pointer[_type.DWORD]],  # pFiberCookie
                                          _type.HRESULT]
    SwitchOutLogicalThreadState: _Callable[[_Pointer[_Pointer[_type.DWORD]]],  # pFiberCookie
                                           _type.HRESULT]
    LocksHeldByLogicalThread: _Callable[[_Pointer[_type.DWORD]],  # pCount
                                        _type.HRESULT]
    MapFile: _Callable[[_type.HANDLE,  # hFile
                        _Pointer[_type.HMODULE]],  # hMapAddress
                       _type.HRESULT]
    GetConfiguration: _Callable[[_Pointer[ICorConfiguration]],  # pConfiguration
                                _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    CreateDomain: _Callable[[_type.LPCWSTR,  # pwzFriendlyName
                             _Unknwnbase.IUnknown,  # pIdentityArray
                             _Pointer[_Unknwnbase.IUnknown]],  # pAppDomain
                            _type.HRESULT]
    GetDefaultDomain: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # pAppDomain
                                _type.HRESULT]
    EnumDomains: _Callable[[_Pointer[_type.HDOMAINENUM]],  # hEnum
                           _type.HRESULT]
    NextDomain: _Callable[[_type.HDOMAINENUM,  # hEnum
                           _Pointer[_Unknwnbase.IUnknown]],  # pAppDomain
                          _type.HRESULT]
    CloseEnum: _Callable[[_type.HDOMAINENUM],  # hEnum
                         _type.HRESULT]
    CreateDomainEx: _Callable[[_type.LPCWSTR,  # pwzFriendlyName
                               _Unknwnbase.IUnknown,  # pSetup
                               _Unknwnbase.IUnknown,  # pEvidence
                               _Pointer[_Unknwnbase.IUnknown]],  # pAppDomain
                              _type.HRESULT]
    CreateDomainSetup: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # pAppDomainSetup
                                 _type.HRESULT]
    CreateEvidence: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # pEvidence
                              _type.HRESULT]
    UnloadDomain: _Callable[[_Unknwnbase.IUnknown],  # pAppDomain
                            _type.HRESULT]
    CurrentDomain: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # pAppDomain
                             _type.HRESULT]


class ICLRMemoryNotificationCallback(_Unknwnbase.IUnknown):
    OnMemoryNotification: _Callable[[_enum.EMemoryAvailable],  # eMemoryAvailable
                                    _type.HRESULT]


class IHostMalloc(_Unknwnbase.IUnknown):
    Alloc: _Callable[[_type.SIZE_T,  # cbSize
                      _enum.EMemoryCriticalLevel,  # eCriticalLevel
                      _type.c_void_p],  # ppMem
                     _type.HRESULT]
    DebugAlloc: _Callable[[_type.SIZE_T,  # cbSize
                           _enum.EMemoryCriticalLevel,  # eCriticalLevel
                           _type.c_char_p,  # pszFileName
                           _type.c_int,  # iLineNo
                           _type.c_void_p],  # ppMem
                          _type.HRESULT]
    Free: _Callable[[_type.c_void_p],  # pMem
                    _type.HRESULT]


class IHostMemoryManager(_Unknwnbase.IUnknown):
    CreateMalloc: _Callable[[_type.DWORD,  # dwMallocType
                             _Pointer[IHostMalloc]],  # ppMalloc
                            _type.HRESULT]
    VirtualAlloc: _Callable[[_type.c_void_p,  # pAddress
                             _type.SIZE_T,  # dwSize
                             _type.DWORD,  # flAllocationType
                             _type.DWORD,  # flProtect
                             _enum.EMemoryCriticalLevel,  # eCriticalLevel
                             _type.c_void_p],  # ppMem
                            _type.HRESULT]
    VirtualFree: _Callable[[_type.LPVOID,  # lpAddress
                            _type.SIZE_T,  # dwSize
                            _type.DWORD],  # dwFreeType
                           _type.HRESULT]
    VirtualQuery: _Callable[[_type.c_void_p,  # lpAddress
                             _type.c_void_p,  # lpBuffer
                             _type.SIZE_T,  # dwLength
                             _Pointer[_type.SIZE_T]],  # pResult
                            _type.HRESULT]
    VirtualProtect: _Callable[[_type.c_void_p,  # lpAddress
                               _type.SIZE_T,  # dwSize
                               _type.DWORD,  # flNewProtect
                               _Pointer[_type.DWORD]],  # pflOldProtect
                              _type.HRESULT]
    GetMemoryLoad: _Callable[[_Pointer[_type.DWORD],  # pMemoryLoad
                              _Pointer[_type.SIZE_T]],  # pAvailableBytes
                             _type.HRESULT]
    RegisterMemoryNotificationCallback: _Callable[[ICLRMemoryNotificationCallback],  # pCallback
                                                  _type.HRESULT]
    NeedsVirtualAddressSpace: _Callable[[_type.LPVOID,  # startAddress
                                         _type.SIZE_T],  # size
                                        _type.HRESULT]
    AcquiredVirtualAddressSpace: _Callable[[_type.LPVOID,  # startAddress
                                            _type.SIZE_T],  # size
                                           _type.HRESULT]
    ReleasedVirtualAddressSpace: _Callable[[_type.LPVOID],  # startAddress
                                           _type.HRESULT]


class ICLRTask(_Unknwnbase.IUnknown):
    SwitchIn: _Callable[[_type.HANDLE],  # threadHandle
                        _type.HRESULT]
    SwitchOut: _Callable[[],
                         _type.HRESULT]
    GetMemStats: _Callable[[_Pointer[_struct.COR_GC_THREAD_STATS]],  # memUsage
                           _type.HRESULT]
    Reset: _Callable[[_type.BOOL],  # fFull
                     _type.HRESULT]
    ExitTask: _Callable[[],
                        _type.HRESULT]
    Abort: _Callable[[],
                     _type.HRESULT]
    RudeAbort: _Callable[[],
                         _type.HRESULT]
    NeedsPriorityScheduling: _Callable[[_Pointer[_type.BOOL]],  # pbNeedsPriorityScheduling
                                       _type.HRESULT]
    YieldTask: _Callable[[],
                         _type.HRESULT]
    LocksHeld: _Callable[[_Pointer[_type.SIZE_T]],  # pLockCount
                         _type.HRESULT]
    SetTaskIdentifier: _Callable[[_type.TASKID],  # asked
                                 _type.HRESULT]


class ICLRTask2(ICLRTask):
    BeginPreventAsyncAbort: _Callable[[],
                                      _type.HRESULT]
    EndPreventAsyncAbort: _Callable[[],
                                    _type.HRESULT]


class IHostTask(_Unknwnbase.IUnknown):
    Start: _Callable[[],
                     _type.HRESULT]
    Alert: _Callable[[],
                     _type.HRESULT]
    Join: _Callable[[_type.DWORD,  # dwMilliseconds
                     _type.DWORD],  # option
                    _type.HRESULT]
    SetPriority: _Callable[[_type.c_int],  # newPriority
                           _type.HRESULT]
    GetPriority: _Callable[[_Pointer[_type.c_int]],  # pPriority
                           _type.HRESULT]
    SetCLRTask: _Callable[[ICLRTask],  # pCLRTask
                          _type.HRESULT]


class ICLRTaskManager(_Unknwnbase.IUnknown):
    CreateTask: _Callable[[_Pointer[ICLRTask]],  # pTask
                          _type.HRESULT]
    GetCurrentTask: _Callable[[_Pointer[ICLRTask]],  # pTask
                              _type.HRESULT]
    SetUILocale: _Callable[[_type.LCID],  # lcid
                           _type.HRESULT]
    SetLocale: _Callable[[_type.LCID],  # lcid
                         _type.HRESULT]
    GetCurrentTaskType: _Callable[[_Pointer[_enum.ETaskType]],  # pTaskType
                                  _type.HRESULT]


class IHostTaskManager(_Unknwnbase.IUnknown):
    GetCurrentTask: _Callable[[_Pointer[IHostTask]],  # pTask
                              _type.HRESULT]
    CreateTask: _Callable[[_type.DWORD,  # dwStackSize
                           _type.LPTHREAD_START_ROUTINE,  # pStartAddress
                           _type.PVOID,  # pParameter
                           _Pointer[IHostTask]],  # ppTask
                          _type.HRESULT]
    Sleep: _Callable[[_type.DWORD,  # dwMilliseconds
                      _type.DWORD],  # option
                     _type.HRESULT]
    SwitchToTask: _Callable[[_type.DWORD],  # option
                            _type.HRESULT]
    SetUILocale: _Callable[[_type.LCID],  # lcid
                           _type.HRESULT]
    SetLocale: _Callable[[_type.LCID],  # lcid
                         _type.HRESULT]
    CallNeedsHostHook: _Callable[[_type.SIZE_T,  # target
                                  _Pointer[_type.BOOL]],  # pbCallNeedsHostHook
                                 _type.HRESULT]
    LeaveRuntime: _Callable[[_type.SIZE_T],  # target
                            _type.HRESULT]
    EnterRuntime: _Callable[[],
                            _type.HRESULT]
    ReverseLeaveRuntime: _Callable[[],
                                   _type.HRESULT]
    ReverseEnterRuntime: _Callable[[],
                                   _type.HRESULT]
    BeginDelayAbort: _Callable[[],
                               _type.HRESULT]
    EndDelayAbort: _Callable[[],
                             _type.HRESULT]
    BeginThreadAffinity: _Callable[[],
                                   _type.HRESULT]
    EndThreadAffinity: _Callable[[],
                                 _type.HRESULT]
    SetStackGuarantee: _Callable[[_type.ULONG],  # guarantee
                                 _type.HRESULT]
    GetStackGuarantee: _Callable[[_Pointer[_type.ULONG]],  # pGuarantee
                                 _type.HRESULT]
    SetCLRTaskManager: _Callable[[ICLRTaskManager],  # ppManager
                                 _type.HRESULT]


class IHostThreadpoolManager(_Unknwnbase.IUnknown):
    QueueUserWorkItem: _Callable[[_type.LPTHREAD_START_ROUTINE,  # Function
                                  _type.PVOID,  # Context
                                  _type.ULONG],  # Flags
                                 _type.HRESULT]
    SetMaxThreads: _Callable[[_type.DWORD],  # dwMaxWorkerThreads
                             _type.HRESULT]
    GetMaxThreads: _Callable[[_Pointer[_type.DWORD]],  # pdwMaxWorkerThreads
                             _type.HRESULT]
    GetAvailableThreads: _Callable[[_Pointer[_type.DWORD]],  # pdwAvailableWorkerThreads
                                   _type.HRESULT]
    SetMinThreads: _Callable[[_type.DWORD],  # dwMinIOCompletionThreads
                             _type.HRESULT]
    GetMinThreads: _Callable[[_Pointer[_type.DWORD]],  # pdwMinIOCompletionThreads
                             _type.HRESULT]


class ICLRIoCompletionManager(_Unknwnbase.IUnknown):
    OnComplete: _Callable[[_type.DWORD,  # dwErrorCode
                           _type.DWORD,  # NumberOfBytesTransferred
                           _type.c_void_p],  # pvOverlapped
                          _type.HRESULT]


class IHostIoCompletionManager(_Unknwnbase.IUnknown):
    CreateIoCompletionPort: _Callable[[_Pointer[_type.HANDLE]],  # phPort
                                      _type.HRESULT]
    CloseIoCompletionPort: _Callable[[_type.HANDLE],  # hPort
                                     _type.HRESULT]
    SetMaxThreads: _Callable[[_type.DWORD],  # dwMaxIOCompletionThreads
                             _type.HRESULT]
    GetMaxThreads: _Callable[[_Pointer[_type.DWORD]],  # pdwMaxIOCompletionThreads
                             _type.HRESULT]
    GetAvailableThreads: _Callable[[_Pointer[_type.DWORD]],  # pdwAvailableIOCompletionThreads
                                   _type.HRESULT]
    GetHostOverlappedSize: _Callable[[_Pointer[_type.DWORD]],  # pcbSize
                                     _type.HRESULT]
    SetCLRIoCompletionManager: _Callable[[ICLRIoCompletionManager],  # pManager
                                         _type.HRESULT]
    InitializeHostOverlapped: _Callable[[_type.c_void_p],  # pvOverlapped
                                        _type.HRESULT]
    Bind: _Callable[[_type.HANDLE,  # hPort
                     _type.HANDLE],  # hHandle
                    _type.HRESULT]
    SetMinThreads: _Callable[[_type.DWORD],  # dwMinIOCompletionThreads
                             _type.HRESULT]
    GetMinThreads: _Callable[[_Pointer[_type.DWORD]],  # pdwMinIOCompletionThreads
                             _type.HRESULT]


class ICLRDebugManager(_Unknwnbase.IUnknown):
    BeginConnection: _Callable[[_type.CONNID,  # dwConnectionId
                                _Pointer[_type.c_wchar_t]],  # szConnectionName
                               _type.HRESULT]
    SetConnectionTasks: _Callable[[_type.CONNID,  # id
                                   _type.DWORD,  # dwCount
                                   _Pointer[ICLRTask]],  # ppCLRTask
                                  _type.HRESULT]
    EndConnection: _Callable[[_type.CONNID],  # dwConnectionId
                             _type.HRESULT]
    SetDacl: _Callable[[_Pointer[_struct.ACL]],  # pacl
                       _type.HRESULT]
    GetDacl: _Callable[[_Pointer[_Pointer[_struct.ACL]]],  # pacl
                       _type.HRESULT]
    IsDebuggerAttached: _Callable[[_Pointer[_type.BOOL]],  # pbAttached
                                  _type.HRESULT]
    SetSymbolReadingPolicy: _Callable[[_enum.ESymbolReadingPolicy],  # policy
                                      _type.HRESULT]


class ICLRErrorReportingManager(_Unknwnbase.IUnknown):
    GetBucketParametersForCurrentException: _Callable[[_Pointer[_struct.BucketParameters]],  # pParams
                                                      _type.HRESULT]
    BeginCustomDump: _Callable[[_enum.ECustomDumpFlavor,  # dwFlavor
                                _type.DWORD,  # dwNumItems
                                _Pointer[_struct.CustomDumpItem],  # items
                                _type.DWORD],  # dwReserved
                               _type.HRESULT]
    EndCustomDump: _Callable[[],
                             _type.HRESULT]


class IHostCrst(_Unknwnbase.IUnknown):
    Enter: _Callable[[_type.DWORD],  # option
                     _type.HRESULT]
    Leave: _Callable[[],
                     _type.HRESULT]
    TryEnter: _Callable[[_type.DWORD,  # option
                         _Pointer[_type.BOOL]],  # pbSucceeded
                        _type.HRESULT]
    SetSpinCount: _Callable[[_type.DWORD],  # dwSpinCount
                            _type.HRESULT]


class IHostAutoEvent(_Unknwnbase.IUnknown):
    Wait: _Callable[[_type.DWORD,  # dwMilliseconds
                     _type.DWORD],  # option
                    _type.HRESULT]
    Set: _Callable[[],
                   _type.HRESULT]


class IHostManualEvent(_Unknwnbase.IUnknown):
    Wait: _Callable[[_type.DWORD,  # dwMilliseconds
                     _type.DWORD],  # option
                    _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]
    Set: _Callable[[],
                   _type.HRESULT]


class IHostSemaphore(_Unknwnbase.IUnknown):
    Wait: _Callable[[_type.DWORD,  # dwMilliseconds
                     _type.DWORD],  # option
                    _type.HRESULT]
    ReleaseSemaphore: _Callable[[_type.LONG,  # lReleaseCount
                                 _Pointer[_type.LONG]],  # lpPreviousCount
                                _type.HRESULT]


class ICLRSyncManager(_Unknwnbase.IUnknown):
    GetMonitorOwner: _Callable[[_type.SIZE_T,  # Cookie
                                _Pointer[IHostTask]],  # ppOwnerHostTask
                               _type.HRESULT]
    CreateRWLockOwnerIterator: _Callable[[_type.SIZE_T,  # Cookie
                                          _Pointer[_type.SIZE_T]],  # pIterator
                                         _type.HRESULT]
    GetRWLockOwnerNext: _Callable[[_type.SIZE_T,  # Iterator
                                   _Pointer[IHostTask]],  # ppOwnerHostTask
                                  _type.HRESULT]
    DeleteRWLockOwnerIterator: _Callable[[_type.SIZE_T],  # Iterator
                                         _type.HRESULT]


class IHostSyncManager(_Unknwnbase.IUnknown):
    SetCLRSyncManager: _Callable[[ICLRSyncManager],  # pManager
                                 _type.HRESULT]
    CreateCrst: _Callable[[_Pointer[IHostCrst]],  # ppCrst
                          _type.HRESULT]
    CreateCrstWithSpinCount: _Callable[[_type.DWORD,  # dwSpinCount
                                        _Pointer[IHostCrst]],  # ppCrst
                                       _type.HRESULT]
    CreateAutoEvent: _Callable[[_Pointer[IHostAutoEvent]],  # ppEvent
                               _type.HRESULT]
    CreateManualEvent: _Callable[[_type.BOOL,  # bInitialState
                                  _Pointer[IHostManualEvent]],  # ppEvent
                                 _type.HRESULT]
    CreateMonitorEvent: _Callable[[_type.SIZE_T,  # Cookie
                                   _Pointer[IHostAutoEvent]],  # ppEvent
                                  _type.HRESULT]
    CreateRWLockWriterEvent: _Callable[[_type.SIZE_T,  # Cookie
                                        _Pointer[IHostAutoEvent]],  # ppEvent
                                       _type.HRESULT]
    CreateRWLockReaderEvent: _Callable[[_type.BOOL,  # bInitialState
                                        _type.SIZE_T,  # Cookie
                                        _Pointer[IHostManualEvent]],  # ppEvent
                                       _type.HRESULT]
    CreateSemaphore: _Callable[[_type.DWORD,  # dwInitial
                                _type.DWORD,  # dwMax
                                _Pointer[IHostSemaphore]],  # ppSemaphore
                               _type.HRESULT]


class ICLRPolicyManager(_Unknwnbase.IUnknown):
    SetDefaultAction: _Callable[[_enum.EClrOperation,  # operation
                                 _enum.EPolicyAction],  # action
                                _type.HRESULT]
    SetTimeout: _Callable[[_enum.EClrOperation,  # operation
                           _type.DWORD],  # dwMilliseconds
                          _type.HRESULT]
    SetActionOnTimeout: _Callable[[_enum.EClrOperation,  # operation
                                   _enum.EPolicyAction],  # action
                                  _type.HRESULT]
    SetTimeoutAndAction: _Callable[[_enum.EClrOperation,  # operation
                                    _type.DWORD,  # dwMilliseconds
                                    _enum.EPolicyAction],  # action
                                   _type.HRESULT]
    SetActionOnFailure: _Callable[[_enum.EClrFailure,  # failure
                                   _enum.EPolicyAction],  # action
                                  _type.HRESULT]
    SetUnhandledExceptionPolicy: _Callable[[_enum.EClrUnhandledException],  # policy
                                           _type.HRESULT]


class IHostPolicyManager(_Unknwnbase.IUnknown):
    OnDefaultAction: _Callable[[_enum.EClrOperation,  # operation
                                _enum.EPolicyAction],  # action
                               _type.HRESULT]
    OnTimeout: _Callable[[_enum.EClrOperation,  # operation
                          _enum.EPolicyAction],  # action
                         _type.HRESULT]
    OnFailure: _Callable[[_enum.EClrFailure,  # failure
                          _enum.EPolicyAction],  # action
                         _type.HRESULT]


class IActionOnCLREvent(_Unknwnbase.IUnknown):
    OnEvent: _Callable[[_enum.EClrEvent,  # event
                        _type.PVOID],  # data
                       _type.HRESULT]


class ICLROnEventManager(_Unknwnbase.IUnknown):
    RegisterActionOnEvent: _Callable[[_enum.EClrEvent,  # event
                                      IActionOnCLREvent],  # pAction
                                     _type.HRESULT]
    UnregisterActionOnEvent: _Callable[[_enum.EClrEvent,  # event
                                        IActionOnCLREvent],  # pAction
                                       _type.HRESULT]


class IHostGCManager(_Unknwnbase.IUnknown):
    ThreadIsBlockingForSuspension: _Callable[[],
                                             _type.HRESULT]
    SuspensionStarting: _Callable[[],
                                  _type.HRESULT]
    SuspensionEnding: _Callable[[_type.DWORD],  # Generation
                                _type.HRESULT]


class ICLRAssemblyReferenceList(_Unknwnbase.IUnknown):
    IsStringAssemblyReferenceInList: _Callable[[_type.LPCWSTR],  # pwzAssemblyName
                                               _type.HRESULT]
    IsAssemblyReferenceInList: _Callable[[_Unknwnbase.IUnknown],  # pName
                                         _type.HRESULT]


class ICLRReferenceAssemblyEnum(_Unknwnbase.IUnknown):
    Get: _Callable[[_type.DWORD,  # dwIndex
                    _type.LPWSTR,  # pwzBuffer
                    _Pointer[_type.DWORD]],  # pcchBufferSize
                   _type.HRESULT]


class ICLRProbingAssemblyEnum(_Unknwnbase.IUnknown):
    Get: _Callable[[_type.DWORD,  # dwIndex
                    _type.LPWSTR,  # pwzBuffer
                    _Pointer[_type.DWORD]],  # pcchBufferSize
                   _type.HRESULT]


class ICLRAssemblyIdentityManager(_Unknwnbase.IUnknown):
    GetCLRAssemblyReferenceList: _Callable[[_Pointer[_type.LPCWSTR],  # ppwzAssemblyReferences
                                            _type.DWORD,  # dwNumOfReferences
                                            _Pointer[ICLRAssemblyReferenceList]],  # ppReferenceList
                                           _type.HRESULT]
    GetBindingIdentityFromFile: _Callable[[_type.LPCWSTR,  # pwzFilePath
                                           _type.DWORD,  # dwFlags
                                           _type.LPWSTR,  # pwzBuffer
                                           _Pointer[_type.DWORD]],  # pcchBufferSize
                                          _type.HRESULT]
    GetBindingIdentityFromStream: _Callable[[_objidlbase.IStream,  # pStream
                                             _type.DWORD,  # dwFlags
                                             _type.LPWSTR,  # pwzBuffer
                                             _Pointer[_type.DWORD]],  # pcchBufferSize
                                            _type.HRESULT]
    GetReferencedAssembliesFromFile: _Callable[[_type.LPCWSTR,  # pwzFilePath
                                                _type.DWORD,  # dwFlags
                                                ICLRAssemblyReferenceList,  # pExcludeAssembliesList
                                                _Pointer[ICLRReferenceAssemblyEnum]],  # ppReferenceEnum
                                               _type.HRESULT]
    GetReferencedAssembliesFromStream: _Callable[[_objidlbase.IStream,  # pStream
                                                  _type.DWORD,  # dwFlags
                                                  ICLRAssemblyReferenceList,  # pExcludeAssembliesList
                                                  _Pointer[ICLRReferenceAssemblyEnum]],  # ppReferenceEnum
                                                 _type.HRESULT]
    GetProbingAssembliesFromReference: _Callable[[_type.DWORD,  # dwMachineType
                                                  _type.DWORD,  # dwFlags
                                                  _type.LPCWSTR,  # pwzReferenceIdentity
                                                  _Pointer[ICLRProbingAssemblyEnum]],  # ppProbingAssemblyEnum
                                                 _type.HRESULT]
    IsStronglyNamed: _Callable[[_type.LPCWSTR,  # pwzAssemblyIdentity
                                _Pointer[_type.BOOL]],  # pbIsStronglyNamed
                               _type.HRESULT]


class ICLRHostBindingPolicyManager(_Unknwnbase.IUnknown):
    ModifyApplicationPolicy: _Callable[[_type.LPCWSTR,  # pwzSourceAssemblyIdentity
                                        _type.LPCWSTR,  # pwzTargetAssemblyIdentity
                                        _Pointer[_type.BYTE],  # pbApplicationPolicy
                                        _type.DWORD,  # cbAppPolicySize
                                        _type.DWORD,  # dwPolicyModifyFlags
                                        _Pointer[_type.BYTE],  # pbNewApplicationPolicy
                                        _Pointer[_type.DWORD]],  # pcbNewAppPolicySize
                                       _type.HRESULT]
    EvaluatePolicy: _Callable[[_type.LPCWSTR,  # pwzReferenceIdentity
                               _Pointer[_type.BYTE],  # pbApplicationPolicy
                               _type.DWORD,  # cbAppPolicySize
                               _type.LPWSTR,  # pwzPostPolicyReferenceIdentity
                               _Pointer[_type.DWORD],  # pcchPostPolicyReferenceIdentity
                               _Pointer[_type.DWORD]],  # pdwPoliciesApplied
                              _type.HRESULT]


class ICLRGCManager(_Unknwnbase.IUnknown):
    Collect: _Callable[[_type.LONG],  # Generation
                       _type.HRESULT]
    GetStats: _Callable[[_Pointer[_struct.COR_GC_STATS]],  # pStats
                        _type.HRESULT]
    SetGCStartupLimits: _Callable[[_type.DWORD,  # SegmentSize
                                   _type.DWORD],  # MaxGen0Size
                                  _type.HRESULT]


class ICLRGCManager2(ICLRGCManager):
    SetGCStartupLimitsEx: _Callable[[_type.SIZE_T,  # SegmentSize
                                     _type.SIZE_T],  # MaxGen0Size
                                    _type.HRESULT]


class IHostAssemblyStore(_Unknwnbase.IUnknown):
    ProvideAssembly: _Callable[[_Pointer[_struct.AssemblyBindInfo],  # pBindInfo
                                _Pointer[_type.UINT64],  # pAssemblyId
                                _Pointer[_type.UINT64],  # pContext
                                _Pointer[_objidlbase.IStream],  # ppStmAssemblyImage
                                _Pointer[_objidlbase.IStream]],  # ppStmPDB
                               _type.HRESULT]
    ProvideModule: _Callable[[_Pointer[_struct.ModuleBindInfo],  # pBindInfo
                              _Pointer[_type.DWORD],  # pdwModuleId
                              _Pointer[_objidlbase.IStream],  # ppStmModuleImage
                              _Pointer[_objidlbase.IStream]],  # ppStmPDB
                             _type.HRESULT]


class IHostAssemblyManager(_Unknwnbase.IUnknown):
    GetNonHostStoreAssemblies: _Callable[[_Pointer[ICLRAssemblyReferenceList]],  # ppReferenceList
                                         _type.HRESULT]
    GetAssemblyStore: _Callable[[_Pointer[IHostAssemblyStore]],  # ppAssemblyStore
                                _type.HRESULT]


class IHostControl(_Unknwnbase.IUnknown):
    GetHostManager: _Callable[[_Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppObject
                              _type.HRESULT]
    SetAppDomainManager: _Callable[[_type.DWORD,  # dwAppDomainID
                                    _Unknwnbase.IUnknown],  # pUnkAppDomainManager
                                   _type.HRESULT]


class ICLRControl(_Unknwnbase.IUnknown):
    GetCLRManager: _Callable[[_Pointer[_struct.IID],  # riid
                              _type.c_void_p],  # ppObject
                             _type.HRESULT]
    SetAppDomainManagerType: _Callable[[_type.LPCWSTR,  # pwzAppDomainManagerAssembly
                                        _type.LPCWSTR],  # pwzAppDomainManagerType
                                       _type.HRESULT]


class ICLRRuntimeHost(_Unknwnbase.IUnknown):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    SetHostControl: _Callable[[IHostControl],  # pHostControl
                              _type.HRESULT]
    GetCLRControl: _Callable[[_Pointer[ICLRControl]],  # pCLRControl
                             _type.HRESULT]
    UnloadAppDomain: _Callable[[_type.DWORD,  # dwAppDomainId
                                _type.BOOL],  # fWaitUntilDone
                               _type.HRESULT]
    ExecuteInAppDomain: _Callable[[_type.DWORD,  # dwAppDomainId
                                   _type.FExecuteInAppDomainCallback,  # pCallback
                                   _type.c_void_p],  # cookie
                                  _type.HRESULT]
    GetCurrentAppDomainId: _Callable[[_Pointer[_type.DWORD]],  # pdwAppDomainId
                                     _type.HRESULT]
    ExecuteApplication: _Callable[[_type.LPCWSTR,  # pwzAppFullName
                                   _type.DWORD,  # dwManifestPaths
                                   _Pointer[_type.LPCWSTR],  # ppwzManifestPaths
                                   _type.DWORD,  # dwActivationData
                                   _Pointer[_type.LPCWSTR],  # ppwzActivationData
                                   _Pointer[_type.c_int]],  # pReturnValue
                                  _type.HRESULT]
    ExecuteInDefaultAppDomain: _Callable[[_type.LPCWSTR,  # pwzAssemblyPath
                                          _type.LPCWSTR,  # pwzTypeName
                                          _type.LPCWSTR,  # pwzMethodName
                                          _type.LPCWSTR,  # pwzArgument
                                          _Pointer[_type.DWORD]],  # pReturnValue
                                         _type.HRESULT]


class ICLRHostProtectionManager(_Unknwnbase.IUnknown):
    SetProtectedCategories: _Callable[[_enum.EApiCategories],  # categories
                                      _type.HRESULT]
    SetEagerSerializeGrantSets: _Callable[[],
                                          _type.HRESULT]


class ICLRDomainManager(_Unknwnbase.IUnknown):
    SetAppDomainManagerType: _Callable[[_type.LPCWSTR,  # wszAppDomainManagerAssembly
                                        _type.LPCWSTR,  # wszAppDomainManagerType
                                        _enum.EInitializeNewDomainFlags],  # dwInitializeDomainFlags
                                       _type.HRESULT]
    SetPropertiesForDefaultAppDomain: _Callable[[_type.DWORD,  # nProperties
                                                 _Pointer[_type.LPCWSTR],  # pwszPropertyNames
                                                 _Pointer[_type.LPCWSTR]],  # pwszPropertyValues
                                                _type.HRESULT]


class ITypeName(_Unknwnbase.IUnknown):
    GetNameCount: _Callable[[_Pointer[_type.DWORD]],  # pCount
                            _type.HRESULT]
    GetNames: _Callable[[_type.DWORD,  # count
                         _Pointer[_type.BSTR],  # rgbszNames
                         _Pointer[_type.DWORD]],  # pCount
                        _type.HRESULT]
    GetTypeArgumentCount: _Callable[[_Pointer[_type.DWORD]],  # pCount
                                    _type.HRESULT]
    GetTypeArguments: _Callable[[_type.DWORD,  # count
                                 _Pointer[ITypeName],  # rgpArguments
                                 _Pointer[_type.DWORD]],  # pCount
                                _type.HRESULT]
    GetModifierLength: _Callable[[_Pointer[_type.DWORD]],  # pCount
                                 _type.HRESULT]
    GetModifiers: _Callable[[_type.DWORD,  # count
                             _Pointer[_type.DWORD],  # rgModifiers
                             _Pointer[_type.DWORD]],  # pCount
                            _type.HRESULT]
    GetAssemblyName: _Callable[[_Pointer[_type.BSTR]],  # rgbszAssemblyNames
                               _type.HRESULT]


class ITypeNameBuilder(_Unknwnbase.IUnknown):
    OpenGenericArguments: _Callable[[],
                                    _type.HRESULT]
    CloseGenericArguments: _Callable[[],
                                     _type.HRESULT]
    OpenGenericArgument: _Callable[[],
                                   _type.HRESULT]
    CloseGenericArgument: _Callable[[],
                                    _type.HRESULT]
    AddName: _Callable[[_type.LPCWSTR],  # szName
                       _type.HRESULT]
    AddPointer: _Callable[[],
                          _type.HRESULT]
    AddByRef: _Callable[[],
                        _type.HRESULT]
    AddSzArray: _Callable[[],
                          _type.HRESULT]
    AddArray: _Callable[[_type.DWORD],  # rank
                        _type.HRESULT]
    AddAssemblySpec: _Callable[[_type.LPCWSTR],  # szAssemblySpec
                               _type.HRESULT]
    ToString: _Callable[[_Pointer[_type.BSTR]],  # pszStringRepresentation
                        _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class ITypeNameFactory(_Unknwnbase.IUnknown):
    ParseTypeName: _Callable[[_type.LPCWSTR,  # szName
                              _Pointer[_type.DWORD],  # pError
                              _Pointer[ITypeName]],  # ppTypeName
                             _type.HRESULT]
    GetTypeNameBuilder: _Callable[[_Pointer[ITypeNameBuilder]],  # ppTypeBuilder
                                  _type.HRESULT]


class IApartmentCallback(_Unknwnbase.IUnknown):
    DoCallback: _Callable[[_type.SIZE_T,  # pFunc
                           _type.SIZE_T],  # pData
                          _type.HRESULT]


class IManagedObject(_Unknwnbase.IUnknown):
    GetSerializedBuffer: _Callable[[_Pointer[_type.BSTR]],  # pBSTR
                                   _type.HRESULT]
    GetObjectIdentity: _Callable[[_Pointer[_type.BSTR],  # pBSTRGUID
                                  _Pointer[_type.c_int],  # AppDomainID
                                  _Pointer[_type.c_int]],  # pCCW
                                 _type.HRESULT]


class ICatalogServices(_Unknwnbase.IUnknown):
    Autodone: _Callable[[],
                        _type.HRESULT]
    NotAutodone: _Callable[[],
                           _type.HRESULT]


class IHostSecurityContext(_Unknwnbase.IUnknown):
    Capture: _Callable[[_Pointer[IHostSecurityContext]],  # ppClonedContext
                       _type.HRESULT]


class IHostSecurityManager(_Unknwnbase.IUnknown):
    ImpersonateLoggedOnUser: _Callable[[_type.HANDLE],  # hToken
                                       _type.HRESULT]
    RevertToSelf: _Callable[[],
                            _type.HRESULT]
    OpenThreadToken: _Callable[[_type.DWORD,  # dwDesiredAccess
                                _type.BOOL,  # bOpenAsSelf
                                _Pointer[_type.HANDLE]],  # phThreadToken
                               _type.HRESULT]
    SetThreadToken: _Callable[[_type.HANDLE],  # hToken
                              _type.HRESULT]
    GetSecurityContext: _Callable[[_enum.EContextType,  # eContextType
                                   _Pointer[IHostSecurityContext]],  # ppSecurityContext
                                  _type.HRESULT]
    SetSecurityContext: _Callable[[_enum.EContextType,  # eContextType
                                   IHostSecurityContext],  # pSecurityContext
                                  _type.HRESULT]


class ICLRAppDomainResourceMonitor(_Unknwnbase.IUnknown):
    GetCurrentAllocated: _Callable[[_type.DWORD,  # dwAppDomainId
                                    _Pointer[_type.ULONGLONG]],  # pBytesAllocated
                                   _type.HRESULT]
    GetCurrentSurvived: _Callable[[_type.DWORD,  # dwAppDomainId
                                   _Pointer[_type.ULONGLONG],  # pAppDomainBytesSurvived
                                   _Pointer[_type.ULONGLONG]],  # pTotalBytesSurvived
                                  _type.HRESULT]
    GetCurrentCpuTime: _Callable[[_type.DWORD,  # dwAppDomainId
                                  _Pointer[_type.ULONGLONG]],  # pMilliseconds
                                 _type.HRESULT]
