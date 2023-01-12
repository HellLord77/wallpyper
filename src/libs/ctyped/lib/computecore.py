from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# computecore
HcsEnumerateComputeSystems: _Callable[[_type.PCWSTR,  # query
                                       _type.HCS_OPERATION],  # operation
                                      _type.HRESULT]
HcsEnumerateComputeSystemsInNamespace: _Callable[[_type.PCWSTR,  # idNamespace
                                                  _type.PCWSTR,  # query
                                                  _type.HCS_OPERATION],  # operation
                                                 _type.HRESULT]
# HcsCreateOperation: _Callable[[_type.c_void_p,  # context
#                                HCS_OPERATION_COMPLETION],  # callback
#                               _type.HCS_OPERATION]
# HcsCreateOperationWithNotifications: _Callable[[_enum.HCS_OPERATION_OPTIONS,  # eventTypes
#                                                 _type.c_void_p,  # context
#                                                 HCS_EVENT_CALLBACK],  # callback
#                                                _type.HCS_OPERATION]
HcsCloseOperation: _Callable[[_type.HCS_OPERATION],  # operation
                             _type.c_void]
HcsGetOperationContext: _Callable[[_type.HCS_OPERATION],  # operation
                                  _type.c_void_p]
HcsSetOperationContext: _Callable[[_type.HCS_OPERATION,  # operation
                                   _type.c_void_p],  # context
                                  _type.HRESULT]
HcsGetComputeSystemFromOperation: _Callable[[_type.HCS_OPERATION],  # operation
                                            _type.HCS_SYSTEM]
HcsGetProcessFromOperation: _Callable[[_type.HCS_OPERATION],  # operation
                                      _type.HCS_PROCESS]
HcsGetOperationType: _Callable[[_type.HCS_OPERATION],  # operation
                               _enum.HCS_OPERATION_TYPE]
HcsGetOperationId: _Callable[[_type.HCS_OPERATION],  # operation
                             _type.UINT64]
HcsGetOperationResult: _Callable[[_type.HCS_OPERATION,  # operation
                                  _Pointer[_type.PWSTR]],  # resultDocument
                                 _type.HRESULT]
HcsGetOperationResultAndProcessInfo: _Callable[[_type.HCS_OPERATION,  # operation
                                                _Pointer[_struct.HCS_PROCESS_INFORMATION],  # processInformation
                                                _Pointer[_type.PWSTR]],  # resultDocument
                                               _type.HRESULT]
HcsAddResourceToOperation: _Callable[[_type.HCS_OPERATION,  # operation
                                      _enum.HCS_RESOURCE_TYPE,  # type
                                      _type.PCWSTR,  # uri
                                      _type.HANDLE],  # handle
                                     _type.HRESULT]
HcsGetProcessorCompatibilityFromSavedState: _Callable[[_type.PCWSTR,  # RuntimeFileName
                                                       _Pointer[_type.PCWSTR]],  # ProcessorFeaturesString
                                                      _type.HRESULT]
HcsWaitForOperationResult: _Callable[[_type.HCS_OPERATION,  # operation
                                      _type.DWORD,  # timeoutMs
                                      _Pointer[_type.PWSTR]],  # resultDocument
                                     _type.HRESULT]
HcsWaitForOperationResultAndProcessInfo: _Callable[[_type.HCS_OPERATION,  # operation
                                                    _type.DWORD,  # timeoutMs
                                                    _Pointer[_struct.HCS_PROCESS_INFORMATION],  # processInformation
                                                    _Pointer[_type.PWSTR]],  # resultDocument
                                                   _type.HRESULT]
# HcsSetOperationCallback: _Callable[[_type.HCS_OPERATION,  # operation
#                                     _type.c_void_p,  # context
#                                     HCS_OPERATION_COMPLETION],  # callback
#                                    _type.HRESULT]
HcsCancelOperation: _Callable[[_type.HCS_OPERATION],  # operation
                              _type.HRESULT]
HcsCreateComputeSystem: _Callable[[_type.PCWSTR,  # id
                                   _type.PCWSTR,  # configuration
                                   _type.HCS_OPERATION,  # operation
                                   _Pointer[_struct.SECURITY_DESCRIPTOR],  # securityDescriptor
                                   _Pointer[_type.HCS_SYSTEM]],  # computeSystem
                                  _type.HRESULT]
HcsCreateComputeSystemInNamespace: _Callable[[_type.PCWSTR,  # idNamespace
                                              _type.PCWSTR,  # id
                                              _type.PCWSTR,  # configuration
                                              _type.HCS_OPERATION,  # operation
                                              _Pointer[_enum.HCS_CREATE_OPTIONS],  # options
                                              _Pointer[_type.HCS_SYSTEM]],  # computeSystem
                                             _type.HRESULT]
HcsOpenComputeSystem: _Callable[[_type.PCWSTR,  # id
                                 _type.DWORD,  # requestedAccess
                                 _Pointer[_type.HCS_SYSTEM]],  # computeSystem
                                _type.HRESULT]
HcsOpenComputeSystemInNamespace: _Callable[[_type.PCWSTR,  # idNamespace
                                            _type.PCWSTR,  # id
                                            _type.DWORD,  # requestedAccess
                                            _Pointer[_type.HCS_SYSTEM]],  # computeSystem
                                           _type.HRESULT]
HcsCloseComputeSystem: _Callable[[_type.HCS_SYSTEM],  # computeSystem
                                 _type.c_void]
HcsStartComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                  _type.HCS_OPERATION,  # operation
                                  _type.PCWSTR],  # options
                                 _type.HRESULT]
HcsShutDownComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                     _type.HCS_OPERATION,  # operation
                                     _type.PCWSTR],  # options
                                    _type.HRESULT]
HcsTerminateComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                      _type.HCS_OPERATION,  # operation
                                      _type.PCWSTR],  # options
                                     _type.HRESULT]
HcsCrashComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                  _type.HCS_OPERATION,  # operation
                                  _type.PCWSTR],  # options
                                 _type.HRESULT]
HcsPauseComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                  _type.HCS_OPERATION,  # operation
                                  _type.PCWSTR],  # options
                                 _type.HRESULT]
HcsResumeComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                   _type.HCS_OPERATION,  # operation
                                   _type.PCWSTR],  # options
                                  _type.HRESULT]
HcsSaveComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                 _type.HCS_OPERATION,  # operation
                                 _type.PCWSTR],  # options
                                _type.HRESULT]
HcsGetComputeSystemProperties: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                          _type.HCS_OPERATION,  # operation
                                          _type.PCWSTR],  # propertyQuery
                                         _type.HRESULT]
HcsModifyComputeSystem: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                   _type.HCS_OPERATION,  # operation
                                   _type.PCWSTR,  # configuration
                                   _type.HANDLE],  # identity
                                  _type.HRESULT]
HcsWaitForComputeSystemExit: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                                        _type.DWORD,  # timeoutMs
                                        _Pointer[_type.PWSTR]],  # result
                                       _type.HRESULT]
# HcsSetComputeSystemCallback: _Callable[[_type.HCS_SYSTEM,  # computeSystem
#                                         _enum.HCS_EVENT_OPTIONS,  # callbackOptions
#                                         _type.c_void_p,  # context
#                                         HCS_EVENT_CALLBACK],  # callback
#                                        _type.HRESULT]
HcsCreateProcess: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                             _type.PCWSTR,  # processParameters
                             _type.HCS_OPERATION,  # operation
                             _Pointer[_struct.SECURITY_DESCRIPTOR],  # securityDescriptor
                             _Pointer[_type.HCS_PROCESS]],  # process
                            _type.HRESULT]
HcsOpenProcess: _Callable[[_type.HCS_SYSTEM,  # computeSystem
                           _type.DWORD,  # processId
                           _type.DWORD,  # requestedAccess
                           _Pointer[_type.HCS_PROCESS]],  # process
                          _type.HRESULT]
HcsCloseProcess: _Callable[[_type.HCS_PROCESS],  # process
                           _type.c_void]
HcsTerminateProcess: _Callable[[_type.HCS_PROCESS,  # process
                                _type.HCS_OPERATION,  # operation
                                _type.PCWSTR],  # options
                               _type.HRESULT]
HcsSignalProcess: _Callable[[_type.HCS_PROCESS,  # process
                             _type.HCS_OPERATION,  # operation
                             _type.PCWSTR],  # options
                            _type.HRESULT]
HcsGetProcessInfo: _Callable[[_type.HCS_PROCESS,  # process
                              _type.HCS_OPERATION],  # operation
                             _type.HRESULT]
HcsGetProcessProperties: _Callable[[_type.HCS_PROCESS,  # process
                                    _type.HCS_OPERATION,  # operation
                                    _type.PCWSTR],  # propertyQuery
                                   _type.HRESULT]
HcsModifyProcess: _Callable[[_type.HCS_PROCESS,  # process
                             _type.HCS_OPERATION,  # operation
                             _type.PCWSTR],  # settings
                            _type.HRESULT]
# HcsSetProcessCallback: _Callable[[_type.HCS_PROCESS,  # process
#                                   _enum.HCS_EVENT_OPTIONS,  # callbackOptions
#                                   _type.c_void_p,  # context
#                                   HCS_EVENT_CALLBACK],  # callback
#                                  _type.HRESULT]
HcsWaitForProcessExit: _Callable[[_type.HCS_PROCESS,  # computeSystem
                                  _type.DWORD,  # timeoutMs
                                  _Pointer[_type.PWSTR]],  # result
                                 _type.HRESULT]
HcsGetServiceProperties: _Callable[[_type.PCWSTR,  # propertyQuery
                                    _Pointer[_type.PWSTR]],  # result
                                   _type.HRESULT]
HcsModifyServiceSettings: _Callable[[_type.PCWSTR,  # settings
                                     _Pointer[_type.PWSTR]],  # result
                                    _type.HRESULT]
HcsSubmitWerReport: _Callable[[_type.PCWSTR],  # settings
                              _type.HRESULT]
HcsCreateEmptyGuestStateFile: _Callable[[_type.PCWSTR],  # guestStateFilePath
                                        _type.HRESULT]
HcsCreateEmptyRuntimeStateFile: _Callable[[_type.PCWSTR],  # runtimeStateFilePath
                                          _type.HRESULT]
HcsGrantVmAccess: _Callable[[_type.PCWSTR,  # vmId
                             _type.PCWSTR],  # filePath
                            _type.HRESULT]
HcsRevokeVmAccess: _Callable[[_type.PCWSTR,  # vmId
                              _type.PCWSTR],  # filePath
                             _type.HRESULT]
HcsGrantVmGroupAccess: _Callable[[_type.PCWSTR],  # filePath
                                 _type.HRESULT]
HcsRevokeVmGroupAccess: _Callable[[_type.PCWSTR],  # filePath
                                  _type.HRESULT]
IsHcsEnumerateComputeSystemsPresent: _Callable[[],
                                               _type.BOOLEAN]
IsHcsEnumerateComputeSystemsInNamespacePresent: _Callable[[],
                                                          _type.BOOLEAN]
IsHcsCreateOperationPresent: _Callable[[],
                                       _type.BOOLEAN]
IsHcsCreateOperationWithNotificationsPresent: _Callable[[],
                                                        _type.BOOLEAN]
IsHcsCloseOperationPresent: _Callable[[],
                                      _type.BOOLEAN]
IsHcsGetOperationContextPresent: _Callable[[],
                                           _type.BOOLEAN]
IsHcsSetOperationContextPresent: _Callable[[],
                                           _type.BOOLEAN]
IsHcsGetComputeSystemFromOperationPresent: _Callable[[],
                                                     _type.BOOLEAN]
IsHcsGetProcessFromOperationPresent: _Callable[[],
                                               _type.BOOLEAN]
IsHcsGetOperationTypePresent: _Callable[[],
                                        _type.BOOLEAN]
IsHcsGetOperationIdPresent: _Callable[[],
                                      _type.BOOLEAN]
IsHcsGetOperationResultPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsGetOperationResultAndProcessInfoPresent: _Callable[[],
                                                        _type.BOOLEAN]
IsHcsAddResourceToOperationPresent: _Callable[[],
                                              _type.BOOLEAN]
IsHcsGetProcessorCompatibilityFromSavedStatePresent: _Callable[[],
                                                               _type.BOOLEAN]
IsHcsWaitForOperationResultPresent: _Callable[[],
                                              _type.BOOLEAN]
IsHcsWaitForOperationResultAndProcessInfoPresent: _Callable[[],
                                                            _type.BOOLEAN]
IsHcsSetOperationCallbackPresent: _Callable[[],
                                            _type.BOOLEAN]
IsHcsCancelOperationPresent: _Callable[[],
                                       _type.BOOLEAN]
IsHcsCreateComputeSystemPresent: _Callable[[],
                                           _type.BOOLEAN]
IsHcsCreateComputeSystemInNamespacePresent: _Callable[[],
                                                      _type.BOOLEAN]
IsHcsOpenComputeSystemPresent: _Callable[[],
                                         _type.BOOLEAN]
IsHcsOpenComputeSystemInNamespacePresent: _Callable[[],
                                                    _type.BOOLEAN]
IsHcsCloseComputeSystemPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsStartComputeSystemPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsShutDownComputeSystemPresent: _Callable[[],
                                             _type.BOOLEAN]
IsHcsTerminateComputeSystemPresent: _Callable[[],
                                              _type.BOOLEAN]
IsHcsCrashComputeSystemPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsPauseComputeSystemPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsResumeComputeSystemPresent: _Callable[[],
                                           _type.BOOLEAN]
IsHcsSaveComputeSystemPresent: _Callable[[],
                                         _type.BOOLEAN]
IsHcsGetComputeSystemPropertiesPresent: _Callable[[],
                                                  _type.BOOLEAN]
IsHcsModifyComputeSystemPresent: _Callable[[],
                                           _type.BOOLEAN]
IsHcsWaitForComputeSystemExitPresent: _Callable[[],
                                                _type.BOOLEAN]
IsHcsSetComputeSystemCallbackPresent: _Callable[[],
                                                _type.BOOLEAN]
IsHcsCreateProcessPresent: _Callable[[],
                                     _type.BOOLEAN]
IsHcsOpenProcessPresent: _Callable[[],
                                   _type.BOOLEAN]
IsHcsCloseProcessPresent: _Callable[[],
                                    _type.BOOLEAN]
IsHcsTerminateProcessPresent: _Callable[[],
                                        _type.BOOLEAN]
IsHcsSignalProcessPresent: _Callable[[],
                                     _type.BOOLEAN]
IsHcsGetProcessInfoPresent: _Callable[[],
                                      _type.BOOLEAN]
IsHcsGetProcessPropertiesPresent: _Callable[[],
                                            _type.BOOLEAN]
IsHcsModifyProcessPresent: _Callable[[],
                                     _type.BOOLEAN]
IsHcsSetProcessCallbackPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsWaitForProcessExitPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsGetServicePropertiesPresent: _Callable[[],
                                            _type.BOOLEAN]
IsHcsModifyServiceSettingsPresent: _Callable[[],
                                             _type.BOOLEAN]
IsHcsSubmitWerReportPresent: _Callable[[],
                                       _type.BOOLEAN]
IsHcsCreateEmptyGuestStateFilePresent: _Callable[[],
                                                 _type.BOOLEAN]
IsHcsCreateEmptyRuntimeStateFilePresent: _Callable[[],
                                                   _type.BOOLEAN]
IsHcsGrantVmAccessPresent: _Callable[[],
                                     _type.BOOLEAN]
IsHcsRevokeVmAccessPresent: _Callable[[],
                                      _type.BOOLEAN]
IsHcsGrantVmGroupAccessPresent: _Callable[[],
                                          _type.BOOLEAN]
IsHcsRevokeVmGroupAccessPresent: _Callable[[],
                                           _type.BOOLEAN]

_WinLib(__name__)
