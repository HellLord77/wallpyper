from __future__ import annotations as _

from typing import Callable as _Callable

from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IPlatformDiagnosticActionsStatics(_inspectable.IInspectable):
    IsScenarioEnabled: _Callable[[_struct.GUID,  # scenarioId
                                  _Pointer[_type.boolean]],  # isActive
                                 _type.HRESULT]
    TryEscalateScenario: _Callable[[_struct.GUID,  # scenarioId
                                    _enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEscalationType,  # escalationType
                                    _type.HSTRING,  # outputDirectory
                                    _type.boolean,  # timestampOutputDirectory
                                    _type.boolean,  # forceEscalationUpload
                                    _Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING],  # triggers
                                    _Pointer[_type.boolean]],  # result
                                   _type.HRESULT]
    DownloadLatestSettingsForNamespace: _Callable[[_type.HSTRING,  # partner
                                                   _type.HSTRING,  # feature
                                                   _type.boolean,  # isScenarioNamespace
                                                   _type.boolean,  # downloadOverCostedNetwork
                                                   _type.boolean,  # downloadOverBattery
                                                   _Pointer[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState]],  # result
                                                  _type.HRESULT]
    GetActiveScenarioList: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.GUID]]],  # scenarioIds
                                     _type.HRESULT]
    ForceUpload: _Callable[[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticEventBufferLatencies,  # latency
                            _type.boolean,  # uploadOverCostedNetwork
                            _type.boolean,  # uploadOverBattery
                            _Pointer[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActionState]],  # result
                           _type.HRESULT]
    IsTraceRunning: _Callable[[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType,  # slotType
                               _struct.GUID,  # scenarioId
                               _type.UINT64,  # traceProfileHash
                               _Pointer[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotState]],  # slotState
                              _type.HRESULT]
    GetActiveTraceRuntime: _Callable[[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType,  # slotType
                                      _Pointer[IPlatformDiagnosticTraceRuntimeInfo]],  # traceRuntimeInfo
                                     _type.HRESULT]
    GetKnownTraceList: _Callable[[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTraceSlotType,  # slotType
                                  _Pointer[_Windows_Foundation_Collections.IVectorView[IPlatformDiagnosticTraceInfo]]],  # traceInfo
                                 _type.HRESULT]

    _factory = True


class IPlatformDiagnosticTraceInfo(_inspectable.IInspectable):
    get_ScenarioId: _Callable[[_Pointer[_struct.GUID]],  # value
                              _type.HRESULT]
    get_ProfileHash: _Callable[[_Pointer[_type.UINT64]],  # value
                               _type.HRESULT]
    get_IsExclusive: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsAutoLogger: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_MaxTraceDurationFileTime: _Callable[[_Pointer[_type.INT64]],  # value
                                            _type.HRESULT]
    get_Priority: _Callable[[_Pointer[_enum.Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticTracePriority]],  # value
                            _type.HRESULT]


class IPlatformDiagnosticTraceRuntimeInfo(_inspectable.IInspectable):
    get_RuntimeFileTime: _Callable[[_Pointer[_type.INT64]],  # value
                                   _type.HRESULT]
    get_EtwRuntimeFileTime: _Callable[[_Pointer[_type.INT64]],  # value
                                      _type.HRESULT]
