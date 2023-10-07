from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Data import Json as _Windows_Data_Json
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDiagnosticActionResult(_inspectable.IInspectable):
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Results: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                           _type.HRESULT]


class IDiagnosticInvoker(_inspectable.IInspectable):
    RunDiagnosticActionAsync: _Callable[[_Windows_Data_Json.IJsonObject,  # context
                                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDiagnosticActionResult, _enum.Windows.System.Diagnostics.DiagnosticActionState]]],  # operation
                                        _type.HRESULT]


class IDiagnosticInvoker2(_inspectable.IInspectable):
    RunDiagnosticActionFromStringAsync: _Callable[[_type.HSTRING,  # context
                                                   _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDiagnosticActionResult, _enum.Windows.System.Diagnostics.DiagnosticActionState]]],  # operation
                                                  _type.HRESULT]


class IDiagnosticInvokerStatics(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IDiagnosticInvoker]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IDiagnosticInvoker]],  # result
                          _type.HRESULT]
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class IProcessCpuUsage(_inspectable.IInspectable):
    GetReport: _Callable[[_Pointer[IProcessCpuUsageReport]],  # value
                         _type.HRESULT]


class IProcessCpuUsageReport(_inspectable.IInspectable):
    get_KernelTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    get_UserTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]


class IProcessDiagnosticInfo(_inspectable.IInspectable):
    get_ProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_ExecutableFileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_Parent: _Callable[[_Pointer[IProcessDiagnosticInfo]],  # value
                          _type.HRESULT]
    get_ProcessStartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                    _type.HRESULT]
    get_DiskUsage: _Callable[[_Pointer[IProcessDiskUsage]],  # value
                             _type.HRESULT]
    get_MemoryUsage: _Callable[[_Pointer[IProcessMemoryUsage]],  # value
                               _type.HRESULT]
    get_CpuUsage: _Callable[[_Pointer[IProcessCpuUsage]],  # value
                            _type.HRESULT]


class IProcessDiagnosticInfo2(_inspectable.IInspectable):
    GetAppDiagnosticInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_System.IAppDiagnosticInfo]]],  # result
                                     _type.HRESULT]
    get_IsPackaged: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IProcessDiagnosticInfoStatics(_inspectable.IInspectable, factory=True):
    GetForProcesses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IProcessDiagnosticInfo]]],  # processes
                               _type.HRESULT]
    GetForCurrentProcess: _Callable[[_Pointer[IProcessDiagnosticInfo]],  # processes
                                    _type.HRESULT]


class IProcessDiagnosticInfoStatics2(_inspectable.IInspectable, factory=True):
    TryGetForProcessId: _Callable[[_type.UINT32,  # processId
                                   _Pointer[IProcessDiagnosticInfo]],  # result
                                  _type.HRESULT]


class IProcessDiskUsage(_inspectable.IInspectable):
    GetReport: _Callable[[_Pointer[IProcessDiskUsageReport]],  # value
                         _type.HRESULT]


class IProcessDiskUsageReport(_inspectable.IInspectable):
    get_ReadOperationCount: _Callable[[_Pointer[_type.INT64]],  # value
                                      _type.HRESULT]
    get_WriteOperationCount: _Callable[[_Pointer[_type.INT64]],  # value
                                       _type.HRESULT]
    get_OtherOperationCount: _Callable[[_Pointer[_type.INT64]],  # value
                                       _type.HRESULT]
    get_BytesReadCount: _Callable[[_Pointer[_type.INT64]],  # value
                                  _type.HRESULT]
    get_BytesWrittenCount: _Callable[[_Pointer[_type.INT64]],  # value
                                     _type.HRESULT]
    get_OtherBytesCount: _Callable[[_Pointer[_type.INT64]],  # value
                                   _type.HRESULT]


class IProcessMemoryUsage(_inspectable.IInspectable):
    GetReport: _Callable[[_Pointer[IProcessMemoryUsageReport]],  # value
                         _type.HRESULT]


class IProcessMemoryUsageReport(_inspectable.IInspectable):
    get_NonPagedPoolSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                           _type.HRESULT]
    get_PageFaultCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    get_PageFileSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                       _type.HRESULT]
    get_PagedPoolSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                        _type.HRESULT]
    get_PeakNonPagedPoolSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                               _type.HRESULT]
    get_PeakPageFileSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                           _type.HRESULT]
    get_PeakPagedPoolSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                            _type.HRESULT]
    get_PeakVirtualMemorySizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                                _type.HRESULT]
    get_PeakWorkingSetSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                             _type.HRESULT]
    get_PrivatePageCount: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    get_VirtualMemorySizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                            _type.HRESULT]
    get_WorkingSetSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                         _type.HRESULT]


class ISystemCpuUsage(_inspectable.IInspectable):
    GetReport: _Callable[[_Pointer[ISystemCpuUsageReport]],  # value
                         _type.HRESULT]


class ISystemCpuUsageReport(_inspectable.IInspectable):
    get_KernelTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                              _type.HRESULT]
    get_UserTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_IdleTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]


class ISystemDiagnosticInfo(_inspectable.IInspectable):
    get_MemoryUsage: _Callable[[_Pointer[ISystemMemoryUsage]],  # value
                               _type.HRESULT]
    get_CpuUsage: _Callable[[_Pointer[ISystemCpuUsage]],  # value
                            _type.HRESULT]


class ISystemDiagnosticInfoStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentSystem: _Callable[[_Pointer[ISystemDiagnosticInfo]],  # value
                                   _type.HRESULT]


class ISystemDiagnosticInfoStatics2(_inspectable.IInspectable, factory=True):
    IsArchitectureSupported: _Callable[[_enum.Windows.System.ProcessorArchitecture,  # type
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    get_PreferredArchitecture: _Callable[[_Pointer[_enum.Windows.System.ProcessorArchitecture]],  # value
                                         _type.HRESULT]


class ISystemMemoryUsage(_inspectable.IInspectable):
    GetReport: _Callable[[_Pointer[ISystemMemoryUsageReport]],  # value
                         _type.HRESULT]


class ISystemMemoryUsageReport(_inspectable.IInspectable):
    get_TotalPhysicalSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                            _type.HRESULT]
    get_AvailableSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                        _type.HRESULT]
    get_CommittedSizeInBytes: _Callable[[_Pointer[_type.UINT64]],  # value
                                        _type.HRESULT]
