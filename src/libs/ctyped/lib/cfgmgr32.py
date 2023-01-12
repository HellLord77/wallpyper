from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# Cfgmgr32
CM_Add_Empty_Log_Conf: _Callable[[_Pointer[_type.LOG_CONF],  # plcLogConf
                                  _type.DEVINST,  # dnDevInst
                                  _type.PRIORITY,  # Priority
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Add_Empty_Log_Conf_Ex: _Callable[[_Pointer[_type.LOG_CONF],  # plcLogConf
                                     _type.DEVINST,  # dnDevInst
                                     _type.PRIORITY,  # Priority
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Add_IDA: _Callable[[_type.DEVINST,  # dnDevInst
                       _type.PSTR,  # pszID
                       _type.ULONG],  # ulFlags
                      _type.CONFIGRET]
CM_Add_IDW: _Callable[[_type.DEVINST,  # dnDevInst
                       _type.PWSTR,  # pszID
                       _type.ULONG],  # ulFlags
                      _type.CONFIGRET]
CM_Add_ID_ExA: _Callable[[_type.DEVINST,  # dnDevInst
                          _type.PSTR,  # pszID
                          _type.ULONG,  # ulFlags
                          _type.HMACHINE],  # hMachine
                         _type.CONFIGRET]
CM_Add_ID_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                          _type.PWSTR,  # pszID
                          _type.ULONG,  # ulFlags
                          _type.HMACHINE],  # hMachine
                         _type.CONFIGRET]
CM_Add_Range: _Callable[[_type.DWORDLONG,  # ullStartValue
                         _type.DWORDLONG,  # ullEndValue
                         _type.RANGE_LIST,  # rlh
                         _type.ULONG],  # ulFlags
                        _type.CONFIGRET]
CM_Add_Res_Des: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                           _type.LOG_CONF,  # lcLogConf
                           _type.RESOURCEID,  # ResourceID
                           _type.PCVOID,  # ResourceData
                           _type.ULONG,  # ResourceLen
                           _type.ULONG],  # ulFlags
                          _type.CONFIGRET]
CM_Add_Res_Des_Ex: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                              _type.LOG_CONF,  # lcLogConf
                              _type.RESOURCEID,  # ResourceID
                              _type.PCVOID,  # ResourceData
                              _type.ULONG,  # ResourceLen
                              _type.ULONG,  # ulFlags
                              _type.HMACHINE],  # hMachine
                             _type.CONFIGRET]
CM_Connect_MachineA: _Callable[[_type.PCSTR,  # UNCServerName
                                _Pointer[_type.HMACHINE]],  # phMachine
                               _type.CONFIGRET]
CM_Connect_MachineW: _Callable[[_type.PCWSTR,  # UNCServerName
                                _Pointer[_type.HMACHINE]],  # phMachine
                               _type.CONFIGRET]
CM_Create_DevNodeA: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                               _type.DEVINSTID_A,  # pDeviceID
                               _type.DEVINST,  # dnParent
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Create_DevNodeW: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                               _type.DEVINSTID_W,  # pDeviceID
                               _type.DEVINST,  # dnParent
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Create_DevNode_ExA: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                                  _type.DEVINSTID_A,  # pDeviceID
                                  _type.DEVINST,  # dnParent
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Create_DevNode_ExW: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                                  _type.DEVINSTID_W,  # pDeviceID
                                  _type.DEVINST,  # dnParent
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Create_Range_List: _Callable[[_Pointer[_type.RANGE_LIST],  # prlh
                                 _type.ULONG],  # ulFlags
                                _type.CONFIGRET]
CM_Delete_Class_Key: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                _type.ULONG],  # ulFlags
                               _type.CONFIGRET]
CM_Delete_Class_Key_Ex: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                   _type.ULONG,  # ulFlags
                                   _type.HMACHINE],  # hMachine
                                  _type.CONFIGRET]
CM_Delete_DevNode_Key: _Callable[[_type.DEVNODE,  # dnDevNode
                                  _type.ULONG,  # ulHardwareProfile
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Delete_DevNode_Key_Ex: _Callable[[_type.DEVNODE,  # dnDevNode
                                     _type.ULONG,  # ulHardwareProfile
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Delete_Range: _Callable[[_type.DWORDLONG,  # ullStartValue
                            _type.DWORDLONG,  # ullEndValue
                            _type.RANGE_LIST,  # rlh
                            _type.ULONG],  # ulFlags
                           _type.CONFIGRET]
CM_Detect_Resource_Conflict: _Callable[[_type.DEVINST,  # dnDevInst
                                        _type.RESOURCEID,  # ResourceID
                                        _type.PCVOID,  # ResourceData
                                        _type.ULONG,  # ResourceLen
                                        _Pointer[_type.BOOL],  # pbConflictDetected
                                        _type.ULONG],  # ulFlags
                                       _type.CONFIGRET]
CM_Detect_Resource_Conflict_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                           _type.RESOURCEID,  # ResourceID
                                           _type.PCVOID,  # ResourceData
                                           _type.ULONG,  # ResourceLen
                                           _Pointer[_type.BOOL],  # pbConflictDetected
                                           _type.ULONG,  # ulFlags
                                           _type.HMACHINE],  # hMachine
                                          _type.CONFIGRET]
CM_Disable_DevNode: _Callable[[_type.DEVINST,  # dnDevInst
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Disable_DevNode_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Disconnect_Machine: _Callable[[_type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Dup_Range_List: _Callable[[_type.RANGE_LIST,  # rlhOld
                              _type.RANGE_LIST,  # rlhNew
                              _type.ULONG],  # ulFlags
                             _type.CONFIGRET]
CM_Enable_DevNode: _Callable[[_type.DEVINST,  # dnDevInst
                              _type.ULONG],  # ulFlags
                             _type.CONFIGRET]
CM_Enable_DevNode_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                 _type.ULONG,  # ulFlags
                                 _type.HMACHINE],  # hMachine
                                _type.CONFIGRET]
CM_Enumerate_Classes: _Callable[[_type.ULONG,  # ulClassIndex
                                 _Pointer[_struct.GUID],  # ClassGuid
                                 _type.ULONG],  # ulFlags
                                _type.CONFIGRET]
CM_Enumerate_Classes_Ex: _Callable[[_type.ULONG,  # ulClassIndex
                                    _Pointer[_struct.GUID],  # ClassGuid
                                    _type.ULONG,  # ulFlags
                                    _type.HMACHINE],  # hMachine
                                   _type.CONFIGRET]
CM_Enumerate_EnumeratorsA: _Callable[[_type.ULONG,  # ulEnumIndex
                                      _type.PSTR,  # Buffer
                                      _Pointer[_type.ULONG],  # pulLength
                                      _type.ULONG],  # ulFlags
                                     _type.CONFIGRET]
CM_Enumerate_EnumeratorsW: _Callable[[_type.ULONG,  # ulEnumIndex
                                      _type.PWSTR,  # Buffer
                                      _Pointer[_type.ULONG],  # pulLength
                                      _type.ULONG],  # ulFlags
                                     _type.CONFIGRET]
CM_Enumerate_Enumerators_ExA: _Callable[[_type.ULONG,  # ulEnumIndex
                                         _type.PSTR,  # Buffer
                                         _Pointer[_type.ULONG],  # pulLength
                                         _type.ULONG,  # ulFlags
                                         _type.HMACHINE],  # hMachine
                                        _type.CONFIGRET]
CM_Enumerate_Enumerators_ExW: _Callable[[_type.ULONG,  # ulEnumIndex
                                         _type.PWSTR,  # Buffer
                                         _Pointer[_type.ULONG],  # pulLength
                                         _type.ULONG,  # ulFlags
                                         _type.HMACHINE],  # hMachine
                                        _type.CONFIGRET]
CM_Find_Range: _Callable[[_Pointer[_type.DWORDLONG],  # pullStart
                          _type.DWORDLONG,  # ullStart
                          _type.ULONG,  # ulLength
                          _type.DWORDLONG,  # ullAlignment
                          _type.DWORDLONG,  # ullEnd
                          _type.RANGE_LIST,  # rlh
                          _type.ULONG],  # ulFlags
                         _type.CONFIGRET]
CM_First_Range: _Callable[[_type.RANGE_LIST,  # rlh
                           _Pointer[_type.DWORDLONG],  # pullStart
                           _Pointer[_type.DWORDLONG],  # pullEnd
                           _Pointer[_type.RANGE_ELEMENT],  # preElement
                           _type.ULONG],  # ulFlags
                          _type.CONFIGRET]
CM_Free_Log_Conf: _Callable[[_type.LOG_CONF,  # lcLogConfToBeFreed
                             _type.ULONG],  # ulFlags
                            _type.CONFIGRET]
CM_Free_Log_Conf_Ex: _Callable[[_type.LOG_CONF,  # lcLogConfToBeFreed
                                _type.ULONG,  # ulFlags
                                _type.HMACHINE],  # hMachine
                               _type.CONFIGRET]
CM_Free_Log_Conf_Handle: _Callable[[_type.LOG_CONF],  # lcLogConf
                                   _type.CONFIGRET]
CM_Free_Range_List: _Callable[[_type.RANGE_LIST,  # rlh
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Free_Res_Des: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                            _type.RES_DES,  # rdResDes
                            _type.ULONG],  # ulFlags
                           _type.CONFIGRET]
CM_Free_Res_Des_Ex: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                               _type.RES_DES,  # rdResDes
                               _type.ULONG,  # ulFlags
                               _type.HMACHINE],  # hMachine
                              _type.CONFIGRET]
CM_Free_Res_Des_Handle: _Callable[[_type.RES_DES],  # rdResDes
                                  _type.CONFIGRET]
CM_Get_Child: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                         _type.DEVINST,  # dnDevInst
                         _type.ULONG],  # ulFlags
                        _type.CONFIGRET]
CM_Get_Child_Ex: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                            _type.DEVINST,  # dnDevInst
                            _type.ULONG,  # ulFlags
                            _type.HMACHINE],  # hMachine
                           _type.CONFIGRET]
CM_Get_Class_NameA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                               _type.PSTR,  # Buffer
                               _Pointer[_type.ULONG],  # pulLength
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Get_Class_NameW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                               _type.PWSTR,  # Buffer
                               _Pointer[_type.ULONG],  # pulLength
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Get_Class_Name_ExA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                  _type.PSTR,  # Buffer
                                  _Pointer[_type.ULONG],  # pulLength
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Get_Class_Name_ExW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                  _type.PWSTR,  # Buffer
                                  _Pointer[_type.ULONG],  # pulLength
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Get_Class_Key_NameA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                   _type.LPSTR,  # pszKeyName
                                   _Pointer[_type.ULONG],  # pulLength
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Get_Class_Key_NameW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                   _type.LPWSTR,  # pszKeyName
                                   _Pointer[_type.ULONG],  # pulLength
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Get_Class_Key_Name_ExA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                      _type.LPSTR,  # pszKeyName
                                      _Pointer[_type.ULONG],  # pulLength
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Get_Class_Key_Name_ExW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                      _type.LPWSTR,  # pszKeyName
                                      _Pointer[_type.ULONG],  # pulLength
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Get_Depth: _Callable[[_Pointer[_type.ULONG],  # pulDepth
                         _type.DEVINST,  # dnDevInst
                         _type.ULONG],  # ulFlags
                        _type.CONFIGRET]
CM_Get_Depth_Ex: _Callable[[_Pointer[_type.ULONG],  # pulDepth
                            _type.DEVINST,  # dnDevInst
                            _type.ULONG,  # ulFlags
                            _type.HMACHINE],  # hMachine
                           _type.CONFIGRET]
CM_Get_Device_IDA: _Callable[[_type.DEVINST,  # dnDevInst
                              _type.PSTR,  # Buffer
                              _type.ULONG,  # BufferLen
                              _type.ULONG],  # ulFlags
                             _type.CONFIGRET]
CM_Get_Device_IDW: _Callable[[_type.DEVINST,  # dnDevInst
                              _type.PWSTR,  # Buffer
                              _type.ULONG,  # BufferLen
                              _type.ULONG],  # ulFlags
                             _type.CONFIGRET]
CM_Get_Device_ID_ExA: _Callable[[_type.DEVINST,  # dnDevInst
                                 _type.PSTR,  # Buffer
                                 _type.ULONG,  # BufferLen
                                 _type.ULONG,  # ulFlags
                                 _type.HMACHINE],  # hMachine
                                _type.CONFIGRET]
CM_Get_Device_ID_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                 _type.PWSTR,  # Buffer
                                 _type.ULONG,  # BufferLen
                                 _type.ULONG,  # ulFlags
                                 _type.HMACHINE],  # hMachine
                                _type.CONFIGRET]
CM_Get_Device_ID_ListA: _Callable[[_type.PCSTR,  # pszFilter
                                   _type.PZZSTR,  # Buffer
                                   _type.ULONG,  # BufferLen
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Get_Device_ID_ListW: _Callable[[_type.PCWSTR,  # pszFilter
                                   _type.PZZWSTR,  # Buffer
                                   _type.ULONG,  # BufferLen
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Get_Device_ID_List_ExA: _Callable[[_type.PCSTR,  # pszFilter
                                      _type.PZZSTR,  # Buffer
                                      _type.ULONG,  # BufferLen
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Get_Device_ID_List_ExW: _Callable[[_type.PCWSTR,  # pszFilter
                                      _type.PZZWSTR,  # Buffer
                                      _type.ULONG,  # BufferLen
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Get_Device_ID_List_SizeA: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                        _type.PCSTR,  # pszFilter
                                        _type.ULONG],  # ulFlags
                                       _type.CONFIGRET]
CM_Get_Device_ID_List_SizeW: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                        _type.PCWSTR,  # pszFilter
                                        _type.ULONG],  # ulFlags
                                       _type.CONFIGRET]
CM_Get_Device_ID_List_Size_ExA: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                           _type.PCSTR,  # pszFilter
                                           _type.ULONG,  # ulFlags
                                           _type.HMACHINE],  # hMachine
                                          _type.CONFIGRET]
CM_Get_Device_ID_List_Size_ExW: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                           _type.PCWSTR,  # pszFilter
                                           _type.ULONG,  # ulFlags
                                           _type.HMACHINE],  # hMachine
                                          _type.CONFIGRET]
CM_Get_Device_ID_Size: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                  _type.DEVINST,  # dnDevInst
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Get_Device_ID_Size_Ex: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                     _type.DEVINST,  # dnDevInst
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Get_DevNode_PropertyW: _Callable[[_type.DEVINST,  # dnDevInst
                                     _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                     _Pointer[_type.DEVPROPTYPE],  # PropertyType
                                     _type.PBYTE,  # PropertyBuffer
                                     _Pointer[_type.ULONG],  # PropertyBufferSize
                                     _type.ULONG],  # ulFlags
                                    _type.CONFIGRET]
CM_Get_DevNode_Property_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                        _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                        _Pointer[_type.DEVPROPTYPE],  # PropertyType
                                        _type.PBYTE,  # PropertyBuffer
                                        _Pointer[_type.ULONG],  # PropertyBufferSize
                                        _type.ULONG,  # ulFlags
                                        _type.HMACHINE],  # hMachine
                                       _type.CONFIGRET]
CM_Get_DevNode_Property_Keys: _Callable[[_type.DEVINST,  # dnDevInst
                                         _Pointer[_struct.DEVPROPKEY],  # PropertyKeyArray
                                         _Pointer[_type.ULONG],  # PropertyKeyCount
                                         _type.ULONG],  # ulFlags
                                        _type.CONFIGRET]
CM_Get_DevNode_Property_Keys_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                            _Pointer[_struct.DEVPROPKEY],  # PropertyKeyArray
                                            _Pointer[_type.ULONG],  # PropertyKeyCount
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CM_Get_DevNode_Registry_PropertyA: _Callable[[_type.DEVINST,  # dnDevInst
                                              _type.ULONG,  # ulProperty
                                              _Pointer[_type.ULONG],  # pulRegDataType
                                              _type.PVOID,  # Buffer
                                              _Pointer[_type.ULONG],  # pulLength
                                              _type.ULONG],  # ulFlags
                                             _type.CONFIGRET]
CM_Get_DevNode_Registry_PropertyW: _Callable[[_type.DEVINST,  # dnDevInst
                                              _type.ULONG,  # ulProperty
                                              _Pointer[_type.ULONG],  # pulRegDataType
                                              _type.PVOID,  # Buffer
                                              _Pointer[_type.ULONG],  # pulLength
                                              _type.ULONG],  # ulFlags
                                             _type.CONFIGRET]
CM_Get_DevNode_Registry_Property_ExA: _Callable[[_type.DEVINST,  # dnDevInst
                                                 _type.ULONG,  # ulProperty
                                                 _Pointer[_type.ULONG],  # pulRegDataType
                                                 _type.PVOID,  # Buffer
                                                 _Pointer[_type.ULONG],  # pulLength
                                                 _type.ULONG,  # ulFlags
                                                 _type.HMACHINE],  # hMachine
                                                _type.CONFIGRET]
CM_Get_DevNode_Registry_Property_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                                 _type.ULONG,  # ulProperty
                                                 _Pointer[_type.ULONG],  # pulRegDataType
                                                 _type.PVOID,  # Buffer
                                                 _Pointer[_type.ULONG],  # pulLength
                                                 _type.ULONG,  # ulFlags
                                                 _type.HMACHINE],  # hMachine
                                                _type.CONFIGRET]
CM_Get_DevNode_Custom_PropertyA: _Callable[[_type.DEVINST,  # dnDevInst
                                            _type.PCSTR,  # pszCustomPropertyName
                                            _Pointer[_type.ULONG],  # pulRegDataType
                                            _type.PVOID,  # Buffer
                                            _Pointer[_type.ULONG],  # pulLength
                                            _type.ULONG],  # ulFlags
                                           _type.CONFIGRET]
CM_Get_DevNode_Custom_PropertyW: _Callable[[_type.DEVINST,  # dnDevInst
                                            _type.PCWSTR,  # pszCustomPropertyName
                                            _Pointer[_type.ULONG],  # pulRegDataType
                                            _type.PVOID,  # Buffer
                                            _Pointer[_type.ULONG],  # pulLength
                                            _type.ULONG],  # ulFlags
                                           _type.CONFIGRET]
CM_Get_DevNode_Custom_Property_ExA: _Callable[[_type.DEVINST,  # dnDevInst
                                               _type.PCSTR,  # pszCustomPropertyName
                                               _Pointer[_type.ULONG],  # pulRegDataType
                                               _type.PVOID,  # Buffer
                                               _Pointer[_type.ULONG],  # pulLength
                                               _type.ULONG,  # ulFlags
                                               _type.HMACHINE],  # hMachine
                                              _type.CONFIGRET]
CM_Get_DevNode_Custom_Property_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                               _type.PCWSTR,  # pszCustomPropertyName
                                               _Pointer[_type.ULONG],  # pulRegDataType
                                               _type.PVOID,  # Buffer
                                               _Pointer[_type.ULONG],  # pulLength
                                               _type.ULONG,  # ulFlags
                                               _type.HMACHINE],  # hMachine
                                              _type.CONFIGRET]
CM_Get_DevNode_Status: _Callable[[_Pointer[_type.ULONG],  # pulStatus
                                  _Pointer[_type.ULONG],  # pulProblemNumber
                                  _type.DEVINST,  # dnDevInst
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Get_DevNode_Status_Ex: _Callable[[_Pointer[_type.ULONG],  # pulStatus
                                     _Pointer[_type.ULONG],  # pulProblemNumber
                                     _type.DEVINST,  # dnDevInst
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Get_First_Log_Conf: _Callable[[_Pointer[_type.LOG_CONF],  # plcLogConf
                                  _type.DEVINST,  # dnDevInst
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Get_First_Log_Conf_Ex: _Callable[[_Pointer[_type.LOG_CONF],  # plcLogConf
                                     _type.DEVINST,  # dnDevInst
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Get_Global_State: _Callable[[_Pointer[_type.ULONG],  # pulState
                                _type.ULONG],  # ulFlags
                               _type.CONFIGRET]
CM_Get_Global_State_Ex: _Callable[[_Pointer[_type.ULONG],  # pulState
                                   _type.ULONG,  # ulFlags
                                   _type.HMACHINE],  # hMachine
                                  _type.CONFIGRET]
CM_Get_Hardware_Profile_InfoA: _Callable[[_type.ULONG,  # ulIndex
                                          _Pointer[_struct.HWPROFILEINFO_A],  # pHWProfileInfo
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Get_Hardware_Profile_Info_ExA: _Callable[[_type.ULONG,  # ulIndex
                                             _Pointer[_struct.HWPROFILEINFO_A],  # pHWProfileInfo
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Get_Hardware_Profile_InfoW: _Callable[[_type.ULONG,  # ulIndex
                                          _Pointer[_struct.HWPROFILEINFO_W],  # pHWProfileInfo
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Get_Hardware_Profile_Info_ExW: _Callable[[_type.ULONG,  # ulIndex
                                             _Pointer[_struct.HWPROFILEINFO_W],  # pHWProfileInfo
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Get_HW_Prof_FlagsA: _Callable[[_type.DEVINSTID_A,  # pDeviceID
                                  _type.ULONG,  # ulHardwareProfile
                                  _Pointer[_type.ULONG],  # pulValue
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Get_HW_Prof_FlagsW: _Callable[[_type.DEVINSTID_W,  # pDeviceID
                                  _type.ULONG,  # ulHardwareProfile
                                  _Pointer[_type.ULONG],  # pulValue
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Get_HW_Prof_Flags_ExA: _Callable[[_type.DEVINSTID_A,  # pDeviceID
                                     _type.ULONG,  # ulHardwareProfile
                                     _Pointer[_type.ULONG],  # pulValue
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Get_HW_Prof_Flags_ExW: _Callable[[_type.DEVINSTID_W,  # pDeviceID
                                     _type.ULONG,  # ulHardwareProfile
                                     _Pointer[_type.ULONG],  # pulValue
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Get_Device_Interface_AliasA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                           _Pointer[_struct.GUID],  # AliasInterfaceGuid
                                           _type.LPSTR,  # pszAliasDeviceInterface
                                           _Pointer[_type.ULONG],  # pulLength
                                           _type.ULONG],  # ulFlags
                                          _type.CONFIGRET]
CM_Get_Device_Interface_AliasW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                           _Pointer[_struct.GUID],  # AliasInterfaceGuid
                                           _type.LPWSTR,  # pszAliasDeviceInterface
                                           _Pointer[_type.ULONG],  # pulLength
                                           _type.ULONG],  # ulFlags
                                          _type.CONFIGRET]
CM_Get_Device_Interface_Alias_ExA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                              _Pointer[_struct.GUID],  # AliasInterfaceGuid
                                              _type.LPSTR,  # pszAliasDeviceInterface
                                              _Pointer[_type.ULONG],  # pulLength
                                              _type.ULONG,  # ulFlags
                                              _type.HMACHINE],  # hMachine
                                             _type.CONFIGRET]
CM_Get_Device_Interface_Alias_ExW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                              _Pointer[_struct.GUID],  # AliasInterfaceGuid
                                              _type.LPWSTR,  # pszAliasDeviceInterface
                                              _Pointer[_type.ULONG],  # pulLength
                                              _type.ULONG,  # ulFlags
                                              _type.HMACHINE],  # hMachine
                                             _type.CONFIGRET]
CM_Get_Device_Interface_ListA: _Callable[[_Pointer[_struct.GUID],  # InterfaceClassGuid
                                          _type.DEVINSTID_A,  # pDeviceID
                                          _type.PZZSTR,  # Buffer
                                          _type.ULONG,  # BufferLen
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Get_Device_Interface_ListW: _Callable[[_Pointer[_struct.GUID],  # InterfaceClassGuid
                                          _type.DEVINSTID_W,  # pDeviceID
                                          _type.PZZWSTR,  # Buffer
                                          _type.ULONG,  # BufferLen
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Get_Device_Interface_List_ExA: _Callable[[_Pointer[_struct.GUID],  # InterfaceClassGuid
                                             _type.DEVINSTID_A,  # pDeviceID
                                             _type.PZZSTR,  # Buffer
                                             _type.ULONG,  # BufferLen
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Get_Device_Interface_List_ExW: _Callable[[_Pointer[_struct.GUID],  # InterfaceClassGuid
                                             _type.DEVINSTID_W,  # pDeviceID
                                             _type.PZZWSTR,  # Buffer
                                             _type.ULONG,  # BufferLen
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Get_Device_Interface_List_SizeA: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                               _Pointer[_struct.GUID],  # InterfaceClassGuid
                                               _type.DEVINSTID_A,  # pDeviceID
                                               _type.ULONG],  # ulFlags
                                              _type.CONFIGRET]
CM_Get_Device_Interface_List_SizeW: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                               _Pointer[_struct.GUID],  # InterfaceClassGuid
                                               _type.DEVINSTID_W,  # pDeviceID
                                               _type.ULONG],  # ulFlags
                                              _type.CONFIGRET]
CM_Get_Device_Interface_List_Size_ExA: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                                  _Pointer[_struct.GUID],  # InterfaceClassGuid
                                                  _type.DEVINSTID_A,  # pDeviceID
                                                  _type.ULONG,  # ulFlags
                                                  _type.HMACHINE],  # hMachine
                                                 _type.CONFIGRET]
CM_Get_Device_Interface_List_Size_ExW: _Callable[[_Pointer[_type.ULONG],  # pulLen
                                                  _Pointer[_struct.GUID],  # InterfaceClassGuid
                                                  _type.DEVINSTID_W,  # pDeviceID
                                                  _type.ULONG,  # ulFlags
                                                  _type.HMACHINE],  # hMachine
                                                 _type.CONFIGRET]
CM_Get_Device_Interface_PropertyW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                              _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                              _Pointer[_type.DEVPROPTYPE],  # PropertyType
                                              _type.PBYTE,  # PropertyBuffer
                                              _Pointer[_type.ULONG],  # PropertyBufferSize
                                              _type.ULONG],  # ulFlags
                                             _type.CONFIGRET]
CM_Get_Device_Interface_Property_ExW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                                 _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                                 _Pointer[_type.DEVPROPTYPE],  # PropertyType
                                                 _type.PBYTE,  # PropertyBuffer
                                                 _Pointer[_type.ULONG],  # PropertyBufferSize
                                                 _type.ULONG,  # ulFlags
                                                 _type.HMACHINE],  # hMachine
                                                _type.CONFIGRET]
CM_Get_Device_Interface_Property_KeysW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                                   _Pointer[_struct.DEVPROPKEY],  # PropertyKeyArray
                                                   _Pointer[_type.ULONG],  # PropertyKeyCount
                                                   _type.ULONG],  # ulFlags
                                                  _type.CONFIGRET]
CM_Get_Device_Interface_Property_Keys_ExW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                                      _Pointer[_struct.DEVPROPKEY],  # PropertyKeyArray
                                                      _Pointer[_type.ULONG],  # PropertyKeyCount
                                                      _type.ULONG,  # ulFlags
                                                      _type.HMACHINE],  # hMachine
                                                     _type.CONFIGRET]
CM_Get_Log_Conf_Priority: _Callable[[_type.LOG_CONF,  # lcLogConf
                                     _Pointer[_type.PRIORITY],  # pPriority
                                     _type.ULONG],  # ulFlags
                                    _type.CONFIGRET]
CM_Get_Log_Conf_Priority_Ex: _Callable[[_type.LOG_CONF,  # lcLogConf
                                        _Pointer[_type.PRIORITY],  # pPriority
                                        _type.ULONG,  # ulFlags
                                        _type.HMACHINE],  # hMachine
                                       _type.CONFIGRET]
CM_Get_Next_Log_Conf: _Callable[[_Pointer[_type.LOG_CONF],  # plcLogConf
                                 _type.LOG_CONF,  # lcLogConf
                                 _type.ULONG],  # ulFlags
                                _type.CONFIGRET]
CM_Get_Next_Log_Conf_Ex: _Callable[[_Pointer[_type.LOG_CONF],  # plcLogConf
                                    _type.LOG_CONF,  # lcLogConf
                                    _type.ULONG,  # ulFlags
                                    _type.HMACHINE],  # hMachine
                                   _type.CONFIGRET]
CM_Get_Parent: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                          _type.DEVINST,  # dnDevInst
                          _type.ULONG],  # ulFlags
                         _type.CONFIGRET]
CM_Get_Parent_Ex: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                             _type.DEVINST,  # dnDevInst
                             _type.ULONG,  # ulFlags
                             _type.HMACHINE],  # hMachine
                            _type.CONFIGRET]
CM_Get_Res_Des_Data: _Callable[[_type.RES_DES,  # rdResDes
                                _type.PVOID,  # Buffer
                                _type.ULONG,  # BufferLen
                                _type.ULONG],  # ulFlags
                               _type.CONFIGRET]
CM_Get_Res_Des_Data_Ex: _Callable[[_type.RES_DES,  # rdResDes
                                   _type.PVOID,  # Buffer
                                   _type.ULONG,  # BufferLen
                                   _type.ULONG,  # ulFlags
                                   _type.HMACHINE],  # hMachine
                                  _type.CONFIGRET]
CM_Get_Res_Des_Data_Size: _Callable[[_Pointer[_type.ULONG],  # pulSize
                                     _type.RES_DES,  # rdResDes
                                     _type.ULONG],  # ulFlags
                                    _type.CONFIGRET]
CM_Get_Res_Des_Data_Size_Ex: _Callable[[_Pointer[_type.ULONG],  # pulSize
                                        _type.RES_DES,  # rdResDes
                                        _type.ULONG,  # ulFlags
                                        _type.HMACHINE],  # hMachine
                                       _type.CONFIGRET]
CM_Get_Sibling: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                           _type.DEVINST,  # dnDevInst
                           _type.ULONG],  # ulFlags
                          _type.CONFIGRET]
CM_Get_Sibling_Ex: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                              _type.DEVINST,  # dnDevInst
                              _type.ULONG,  # ulFlags
                              _type.HMACHINE],  # hMachine
                             _type.CONFIGRET]
CM_Get_Version: _Callable[[],
                          _type.WORD]
CM_Get_Version_Ex: _Callable[[_type.HMACHINE],  # hMachine
                             _type.WORD]
CM_Is_Version_Available: _Callable[[_type.WORD],  # wVersion
                                   _type.BOOL]
CM_Is_Version_Available_Ex: _Callable[[_type.WORD,  # wVersion
                                       _type.HMACHINE],  # hMachine
                                      _type.BOOL]
CM_Intersect_Range_List: _Callable[[_type.RANGE_LIST,  # rlhOld1
                                    _type.RANGE_LIST,  # rlhOld2
                                    _type.RANGE_LIST,  # rlhNew
                                    _type.ULONG],  # ulFlags
                                   _type.CONFIGRET]
CM_Invert_Range_List: _Callable[[_type.RANGE_LIST,  # rlhOld
                                 _type.RANGE_LIST,  # rlhNew
                                 _type.DWORDLONG,  # ullMaxValue
                                 _type.ULONG],  # ulFlags
                                _type.CONFIGRET]
CM_Locate_DevNodeA: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                               _type.DEVINSTID_A,  # pDeviceID
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Locate_DevNodeW: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                               _type.DEVINSTID_W,  # pDeviceID
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Locate_DevNode_ExA: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                                  _type.DEVINSTID_A,  # pDeviceID
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Locate_DevNode_ExW: _Callable[[_Pointer[_type.DEVINST],  # pdnDevInst
                                  _type.DEVINSTID_W,  # pDeviceID
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Merge_Range_List: _Callable[[_type.RANGE_LIST,  # rlhOld1
                                _type.RANGE_LIST,  # rlhOld2
                                _type.RANGE_LIST,  # rlhNew
                                _type.ULONG],  # ulFlags
                               _type.CONFIGRET]
CM_Modify_Res_Des: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                              _type.RES_DES,  # rdResDes
                              _type.RESOURCEID,  # ResourceID
                              _type.PCVOID,  # ResourceData
                              _type.ULONG,  # ResourceLen
                              _type.ULONG],  # ulFlags
                             _type.CONFIGRET]
CM_Modify_Res_Des_Ex: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                                 _type.RES_DES,  # rdResDes
                                 _type.RESOURCEID,  # ResourceID
                                 _type.PCVOID,  # ResourceData
                                 _type.ULONG,  # ResourceLen
                                 _type.ULONG,  # ulFlags
                                 _type.HMACHINE],  # hMachine
                                _type.CONFIGRET]
CM_Move_DevNode: _Callable[[_type.DEVINST,  # dnFromDevInst
                            _type.DEVINST,  # dnToDevInst
                            _type.ULONG],  # ulFlags
                           _type.CONFIGRET]
CM_Move_DevNode_Ex: _Callable[[_type.DEVINST,  # dnFromDevInst
                               _type.DEVINST,  # dnToDevInst
                               _type.ULONG,  # ulFlags
                               _type.HMACHINE],  # hMachine
                              _type.CONFIGRET]
CM_Next_Range: _Callable[[_Pointer[_type.RANGE_ELEMENT],  # preElement
                          _Pointer[_type.DWORDLONG],  # pullStart
                          _Pointer[_type.DWORDLONG],  # pullEnd
                          _type.ULONG],  # ulFlags
                         _type.CONFIGRET]
CM_Get_Next_Res_Des: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                                _type.RES_DES,  # rdResDes
                                _type.RESOURCEID,  # ForResource
                                _Pointer[_type.RESOURCEID],  # pResourceID
                                _type.ULONG],  # ulFlags
                               _type.CONFIGRET]
CM_Get_Next_Res_Des_Ex: _Callable[[_Pointer[_type.RES_DES],  # prdResDes
                                   _type.RES_DES,  # rdResDes
                                   _type.RESOURCEID,  # ForResource
                                   _Pointer[_type.RESOURCEID],  # pResourceID
                                   _type.ULONG,  # ulFlags
                                   _type.HMACHINE],  # hMachine
                                  _type.CONFIGRET]
CM_Open_Class_KeyA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                               _type.LPCSTR,  # pszClassName
                               _type.REGSAM,  # samDesired
                               _type.REGDISPOSITION,  # Disposition
                               _Pointer[_type.HKEY],  # phkClass
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Open_Class_KeyW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                               _type.LPCWSTR,  # pszClassName
                               _type.REGSAM,  # samDesired
                               _type.REGDISPOSITION,  # Disposition
                               _Pointer[_type.HKEY],  # phkClass
                               _type.ULONG],  # ulFlags
                              _type.CONFIGRET]
CM_Open_Class_Key_ExA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                  _type.LPCSTR,  # pszClassName
                                  _type.REGSAM,  # samDesired
                                  _type.REGDISPOSITION,  # Disposition
                                  _Pointer[_type.HKEY],  # phkClass
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Open_Class_Key_ExW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                  _type.LPCWSTR,  # pszClassName
                                  _type.REGSAM,  # samDesired
                                  _type.REGDISPOSITION,  # Disposition
                                  _Pointer[_type.HKEY],  # phkClass
                                  _type.ULONG,  # ulFlags
                                  _type.HMACHINE],  # hMachine
                                 _type.CONFIGRET]
CM_Open_DevNode_Key: _Callable[[_type.DEVINST,  # dnDevNode
                                _type.REGSAM,  # samDesired
                                _type.ULONG,  # ulHardwareProfile
                                _type.REGDISPOSITION,  # Disposition
                                _Pointer[_type.HKEY],  # phkDevice
                                _type.ULONG],  # ulFlags
                               _type.CONFIGRET]
CM_Open_DevNode_Key_Ex: _Callable[[_type.DEVINST,  # dnDevNode
                                   _type.REGSAM,  # samDesired
                                   _type.ULONG,  # ulHardwareProfile
                                   _type.REGDISPOSITION,  # Disposition
                                   _Pointer[_type.HKEY],  # phkDevice
                                   _type.ULONG,  # ulFlags
                                   _type.HMACHINE],  # hMachine
                                  _type.CONFIGRET]
CM_Open_Device_Interface_KeyA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                          _type.REGSAM,  # samDesired
                                          _type.REGDISPOSITION,  # Disposition
                                          _Pointer[_type.HKEY],  # phkDeviceInterface
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Open_Device_Interface_KeyW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                          _type.REGSAM,  # samDesired
                                          _type.REGDISPOSITION,  # Disposition
                                          _Pointer[_type.HKEY],  # phkDeviceInterface
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Open_Device_Interface_Key_ExA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                             _type.REGSAM,  # samDesired
                                             _type.REGDISPOSITION,  # Disposition
                                             _Pointer[_type.HKEY],  # phkDeviceInterface
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Open_Device_Interface_Key_ExW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                             _type.REGSAM,  # samDesired
                                             _type.REGDISPOSITION,  # Disposition
                                             _Pointer[_type.HKEY],  # phkDeviceInterface
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Delete_Device_Interface_KeyA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                            _type.ULONG],  # ulFlags
                                           _type.CONFIGRET]
CM_Delete_Device_Interface_KeyW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                            _type.ULONG],  # ulFlags
                                           _type.CONFIGRET]
CM_Delete_Device_Interface_Key_ExA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                               _type.ULONG,  # ulFlags
                                               _type.HMACHINE],  # hMachine
                                              _type.CONFIGRET]
CM_Delete_Device_Interface_Key_ExW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                               _type.ULONG,  # ulFlags
                                               _type.HMACHINE],  # hMachine
                                              _type.CONFIGRET]
CM_Query_Arbitrator_Free_Data: _Callable[[_type.PVOID,  # pData
                                          _type.ULONG,  # DataLen
                                          _type.DEVINST,  # dnDevInst
                                          _type.RESOURCEID,  # ResourceID
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Query_Arbitrator_Free_Data_Ex: _Callable[[_type.PVOID,  # pData
                                             _type.ULONG,  # DataLen
                                             _type.DEVINST,  # dnDevInst
                                             _type.RESOURCEID,  # ResourceID
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Query_Arbitrator_Free_Size: _Callable[[_Pointer[_type.ULONG],  # pulSize
                                          _type.DEVINST,  # dnDevInst
                                          _type.RESOURCEID,  # ResourceID
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Query_Arbitrator_Free_Size_Ex: _Callable[[_Pointer[_type.ULONG],  # pulSize
                                             _type.DEVINST,  # dnDevInst
                                             _type.RESOURCEID,  # ResourceID
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Query_Remove_SubTree: _Callable[[_type.DEVINST,  # dnAncestor
                                    _type.ULONG],  # ulFlags
                                   _type.CONFIGRET]
CM_Query_Remove_SubTree_Ex: _Callable[[_type.DEVINST,  # dnAncestor
                                       _type.ULONG,  # ulFlags
                                       _type.HMACHINE],  # hMachine
                                      _type.CONFIGRET]
CM_Query_And_Remove_SubTreeA: _Callable[[_type.DEVINST,  # dnAncestor
                                         _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                         _type.LPSTR,  # pszVetoName
                                         _type.ULONG,  # ulNameLength
                                         _type.ULONG],  # ulFlags
                                        _type.CONFIGRET]
CM_Query_And_Remove_SubTreeW: _Callable[[_type.DEVINST,  # dnAncestor
                                         _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                         _type.LPWSTR,  # pszVetoName
                                         _type.ULONG,  # ulNameLength
                                         _type.ULONG],  # ulFlags
                                        _type.CONFIGRET]
CM_Query_And_Remove_SubTree_ExA: _Callable[[_type.DEVINST,  # dnAncestor
                                            _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                            _type.LPSTR,  # pszVetoName
                                            _type.ULONG,  # ulNameLength
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CM_Query_And_Remove_SubTree_ExW: _Callable[[_type.DEVINST,  # dnAncestor
                                            _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                            _type.LPWSTR,  # pszVetoName
                                            _type.ULONG,  # ulNameLength
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CM_Request_Device_EjectA: _Callable[[_type.DEVINST,  # dnDevInst
                                     _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                     _type.LPSTR,  # pszVetoName
                                     _type.ULONG,  # ulNameLength
                                     _type.ULONG],  # ulFlags
                                    _type.CONFIGRET]
CM_Request_Device_Eject_ExA: _Callable[[_type.DEVINST,  # dnDevInst
                                        _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                        _type.LPSTR,  # pszVetoName
                                        _type.ULONG,  # ulNameLength
                                        _type.ULONG,  # ulFlags
                                        _type.HMACHINE],  # hMachine
                                       _type.CONFIGRET]
CM_Request_Device_EjectW: _Callable[[_type.DEVINST,  # dnDevInst
                                     _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                     _type.LPWSTR,  # pszVetoName
                                     _type.ULONG,  # ulNameLength
                                     _type.ULONG],  # ulFlags
                                    _type.CONFIGRET]
CM_Request_Device_Eject_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                        _Pointer[_enum.PNP_VETO_TYPE],  # pVetoType
                                        _type.LPWSTR,  # pszVetoName
                                        _type.ULONG,  # ulNameLength
                                        _type.ULONG,  # ulFlags
                                        _type.HMACHINE],  # hMachine
                                       _type.CONFIGRET]
CM_Reenumerate_DevNode: _Callable[[_type.DEVINST,  # dnDevInst
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Reenumerate_DevNode_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Register_Device_InterfaceA: _Callable[[_type.DEVINST,  # dnDevInst
                                          _Pointer[_struct.GUID],  # InterfaceClassGuid
                                          _type.LPCSTR,  # pszReference
                                          _type.LPSTR,  # pszDeviceInterface
                                          _Pointer[_type.ULONG],  # pulLength
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Register_Device_InterfaceW: _Callable[[_type.DEVINST,  # dnDevInst
                                          _Pointer[_struct.GUID],  # InterfaceClassGuid
                                          _type.LPCWSTR,  # pszReference
                                          _type.LPWSTR,  # pszDeviceInterface
                                          _Pointer[_type.ULONG],  # pulLength
                                          _type.ULONG],  # ulFlags
                                         _type.CONFIGRET]
CM_Register_Device_Interface_ExA: _Callable[[_type.DEVINST,  # dnDevInst
                                             _Pointer[_struct.GUID],  # InterfaceClassGuid
                                             _type.LPCSTR,  # pszReference
                                             _type.LPSTR,  # pszDeviceInterface
                                             _Pointer[_type.ULONG],  # pulLength
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Register_Device_Interface_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                             _Pointer[_struct.GUID],  # InterfaceClassGuid
                                             _type.LPCWSTR,  # pszReference
                                             _type.LPWSTR,  # pszDeviceInterface
                                             _Pointer[_type.ULONG],  # pulLength
                                             _type.ULONG,  # ulFlags
                                             _type.HMACHINE],  # hMachine
                                            _type.CONFIGRET]
CM_Set_DevNode_Problem_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                      _type.ULONG,  # ulProblem
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Set_DevNode_Problem: _Callable[[_type.DEVINST,  # dnDevInst
                                   _type.ULONG,  # ulProblem
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Unregister_Device_InterfaceA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                            _type.ULONG],  # ulFlags
                                           _type.CONFIGRET]
CM_Unregister_Device_InterfaceW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                            _type.ULONG],  # ulFlags
                                           _type.CONFIGRET]
CM_Unregister_Device_Interface_ExA: _Callable[[_type.LPCSTR,  # pszDeviceInterface
                                               _type.ULONG,  # ulFlags
                                               _type.HMACHINE],  # hMachine
                                              _type.CONFIGRET]
CM_Unregister_Device_Interface_ExW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                               _type.ULONG,  # ulFlags
                                               _type.HMACHINE],  # hMachine
                                              _type.CONFIGRET]
CM_Register_Device_Driver: _Callable[[_type.DEVINST,  # dnDevInst
                                      _type.ULONG],  # ulFlags
                                     _type.CONFIGRET]
CM_Register_Device_Driver_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                         _type.ULONG,  # ulFlags
                                         _type.HMACHINE],  # hMachine
                                        _type.CONFIGRET]
CM_Remove_SubTree: _Callable[[_type.DEVINST,  # dnAncestor
                              _type.ULONG],  # ulFlags
                             _type.CONFIGRET]
CM_Remove_SubTree_Ex: _Callable[[_type.DEVINST,  # dnAncestor
                                 _type.ULONG,  # ulFlags
                                 _type.HMACHINE],  # hMachine
                                _type.CONFIGRET]
CM_Set_DevNode_PropertyW: _Callable[[_type.DEVINST,  # dnDevInst
                                     _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                     _type.DEVPROPTYPE,  # PropertyType
                                     _type.PBYTE,  # PropertyBuffer
                                     _type.ULONG,  # PropertyBufferSize
                                     _type.ULONG],  # ulFlags
                                    _type.CONFIGRET]
CM_Set_DevNode_Property_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                        _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                        _type.DEVPROPTYPE,  # PropertyType
                                        _type.PBYTE,  # PropertyBuffer
                                        _type.ULONG,  # PropertyBufferSize
                                        _type.ULONG,  # ulFlags
                                        _type.HMACHINE],  # hMachine
                                       _type.CONFIGRET]
CM_Set_DevNode_Registry_PropertyA: _Callable[[_type.DEVINST,  # dnDevInst
                                              _type.ULONG,  # ulProperty
                                              _type.PCVOID,  # Buffer
                                              _type.ULONG,  # ulLength
                                              _type.ULONG],  # ulFlags
                                             _type.CONFIGRET]
CM_Set_DevNode_Registry_PropertyW: _Callable[[_type.DEVINST,  # dnDevInst
                                              _type.ULONG,  # ulProperty
                                              _type.PCVOID,  # Buffer
                                              _type.ULONG,  # ulLength
                                              _type.ULONG],  # ulFlags
                                             _type.CONFIGRET]
CM_Set_DevNode_Registry_Property_ExA: _Callable[[_type.DEVINST,  # dnDevInst
                                                 _type.ULONG,  # ulProperty
                                                 _type.PCVOID,  # Buffer
                                                 _type.ULONG,  # ulLength
                                                 _type.ULONG,  # ulFlags
                                                 _type.HMACHINE],  # hMachine
                                                _type.CONFIGRET]
CM_Set_DevNode_Registry_Property_ExW: _Callable[[_type.DEVINST,  # dnDevInst
                                                 _type.ULONG,  # ulProperty
                                                 _type.PCVOID,  # Buffer
                                                 _type.ULONG,  # ulLength
                                                 _type.ULONG,  # ulFlags
                                                 _type.HMACHINE],  # hMachine
                                                _type.CONFIGRET]
CM_Set_Device_Interface_PropertyW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                              _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                              _type.DEVPROPTYPE,  # PropertyType
                                              _type.PBYTE,  # PropertyBuffer
                                              _type.ULONG,  # PropertyBufferSize
                                              _type.ULONG],  # ulFlags
                                             _type.CONFIGRET]
CM_Set_Device_Interface_Property_ExW: _Callable[[_type.LPCWSTR,  # pszDeviceInterface
                                                 _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                                 _type.DEVPROPTYPE,  # PropertyType
                                                 _type.PBYTE,  # PropertyBuffer
                                                 _type.ULONG,  # PropertyBufferSize
                                                 _type.ULONG,  # ulFlags
                                                 _type.HMACHINE],  # hMachine
                                                _type.CONFIGRET]
CM_Is_Dock_Station_Present: _Callable[[_Pointer[_type.BOOL]],  # pbPresent
                                      _type.CONFIGRET]
CM_Is_Dock_Station_Present_Ex: _Callable[[_Pointer[_type.BOOL],  # pbPresent
                                          _type.HMACHINE],  # hMachine
                                         _type.CONFIGRET]
CM_Request_Eject_PC: _Callable[[],
                               _type.CONFIGRET]
CM_Request_Eject_PC_Ex: _Callable[[_type.HMACHINE],  # hMachine
                                  _type.CONFIGRET]
CM_Set_HW_Prof_FlagsA: _Callable[[_type.DEVINSTID_A,  # pDeviceID
                                  _type.ULONG,  # ulConfig
                                  _type.ULONG,  # ulValue
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Set_HW_Prof_FlagsW: _Callable[[_type.DEVINSTID_W,  # pDeviceID
                                  _type.ULONG,  # ulConfig
                                  _type.ULONG,  # ulValue
                                  _type.ULONG],  # ulFlags
                                 _type.CONFIGRET]
CM_Set_HW_Prof_Flags_ExA: _Callable[[_type.DEVINSTID_A,  # pDeviceID
                                     _type.ULONG,  # ulConfig
                                     _type.ULONG,  # ulValue
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Set_HW_Prof_Flags_ExW: _Callable[[_type.DEVINSTID_W,  # pDeviceID
                                     _type.ULONG,  # ulConfig
                                     _type.ULONG,  # ulValue
                                     _type.ULONG,  # ulFlags
                                     _type.HMACHINE],  # hMachine
                                    _type.CONFIGRET]
CM_Setup_DevNode: _Callable[[_type.DEVINST,  # dnDevInst
                             _type.ULONG],  # ulFlags
                            _type.CONFIGRET]
CM_Setup_DevNode_Ex: _Callable[[_type.DEVINST,  # dnDevInst
                                _type.ULONG,  # ulFlags
                                _type.HMACHINE],  # hMachine
                               _type.CONFIGRET]
CM_Test_Range_Available: _Callable[[_type.DWORDLONG,  # ullStartValue
                                    _type.DWORDLONG,  # ullEndValue
                                    _type.RANGE_LIST,  # rlh
                                    _type.ULONG],  # ulFlags
                                   _type.CONFIGRET]
CM_Uninstall_DevNode: _Callable[[_type.DEVNODE,  # dnDevInst
                                 _type.ULONG],  # ulFlags
                                _type.CONFIGRET]
CM_Uninstall_DevNode_Ex: _Callable[[_type.DEVNODE,  # dnDevInst
                                    _type.ULONG,  # ulFlags
                                    _type.HMACHINE],  # hMachine
                                   _type.CONFIGRET]
CM_Run_Detection: _Callable[[_type.ULONG],  # ulFlags
                            _type.CONFIGRET]
CM_Run_Detection_Ex: _Callable[[_type.ULONG,  # ulFlags
                                _type.HMACHINE],  # hMachine
                               _type.CONFIGRET]
CM_Apply_PowerScheme: _Callable[[],
                                _type.CONFIGRET]
CM_Write_UserPowerKey: _Callable[[_Pointer[_struct.GUID],  # SchemeGuid
                                  _Pointer[_struct.GUID],  # SubGroupOfPowerSettingsGuid
                                  _Pointer[_struct.GUID],  # PowerSettingGuid
                                  _type.ULONG,  # AccessFlags
                                  _type.ULONG,  # Type
                                  _Pointer[_type.UCHAR],  # Buffer
                                  _type.DWORD,  # BufferSize
                                  _Pointer[_type.DWORD]],  # Error
                                 _type.CONFIGRET]
CM_Set_ActiveScheme: _Callable[[_Pointer[_struct.GUID],  # SchemeGuid
                                _Pointer[_type.DWORD]],  # Error
                               _type.CONFIGRET]
CM_Restore_DefaultPowerScheme: _Callable[[_Pointer[_struct.GUID],  # SchemeGuid
                                          _Pointer[_type.DWORD]],  # Error
                                         _type.CONFIGRET]
CM_RestoreAll_DefaultPowerSchemes: _Callable[[_Pointer[_type.DWORD]],  # Error
                                             _type.CONFIGRET]
CM_Duplicate_PowerScheme: _Callable[[_Pointer[_struct.GUID],  # SourceSchemeGuid
                                     _Pointer[_Pointer[_struct.GUID]],  # DestinationSchemeGuid
                                     _Pointer[_type.DWORD]],  # Error
                                    _type.CONFIGRET]
CM_Delete_PowerScheme: _Callable[[_Pointer[_struct.GUID],  # SchemeGuid
                                  _Pointer[_type.DWORD]],  # Error
                                 _type.CONFIGRET]
CM_Import_PowerScheme: _Callable[[_type.LPCWSTR,  # ImportFileNamePath
                                  _Pointer[_Pointer[_struct.GUID]],  # DestinationSchemeGuid
                                  _Pointer[_type.DWORD]],  # Error
                                 _type.CONFIGRET]
CM_Set_HW_Prof: _Callable[[_type.ULONG,  # ulHardwareProfile
                           _type.ULONG],  # ulFlags
                          _type.CONFIGRET]
CM_Set_HW_Prof_Ex: _Callable[[_type.ULONG,  # ulHardwareProfile
                              _type.ULONG,  # ulFlags
                              _type.HMACHINE],  # hMachine
                             _type.CONFIGRET]
CM_Query_Resource_Conflict_List: _Callable[[_Pointer[_type.CONFLICT_LIST],  # pclConflictList
                                            _type.DEVINST,  # dnDevInst
                                            _type.RESOURCEID,  # ResourceID
                                            _type.PCVOID,  # ResourceData
                                            _type.ULONG,  # ResourceLen
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CM_Free_Resource_Conflict_Handle: _Callable[[_type.CONFLICT_LIST],  # clConflictList
                                            _type.CONFIGRET]
CM_Get_Resource_Conflict_Count: _Callable[[_type.CONFLICT_LIST,  # clConflictList
                                           _Pointer[_type.ULONG]],  # pulCount
                                          _type.CONFIGRET]
CM_Get_Resource_Conflict_DetailsA: _Callable[[_type.CONFLICT_LIST,  # clConflictList
                                              _type.ULONG,  # ulIndex
                                              _Pointer[_struct.CONFLICT_DETAILS_A]],  # pConflictDetails
                                             _type.CONFIGRET]
CM_Get_Resource_Conflict_DetailsW: _Callable[[_type.CONFLICT_LIST,  # clConflictList
                                              _type.ULONG,  # ulIndex
                                              _Pointer[_struct.CONFLICT_DETAILS_W]],  # pConflictDetails
                                             _type.CONFIGRET]
CM_Get_Class_PropertyW: _Callable[[_Pointer[_struct.GUID],  # ClassGUID
                                   _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                   _Pointer[_type.DEVPROPTYPE],  # PropertyType
                                   _type.PBYTE,  # PropertyBuffer
                                   _Pointer[_type.ULONG],  # PropertyBufferSize
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Get_Class_Property_ExW: _Callable[[_Pointer[_struct.GUID],  # ClassGUID
                                      _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                      _Pointer[_type.DEVPROPTYPE],  # PropertyType
                                      _type.PBYTE,  # PropertyBuffer
                                      _Pointer[_type.ULONG],  # PropertyBufferSize
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Get_Class_Property_Keys: _Callable[[_Pointer[_struct.GUID],  # ClassGUID
                                       _Pointer[_struct.DEVPROPKEY],  # PropertyKeyArray
                                       _Pointer[_type.ULONG],  # PropertyKeyCount
                                       _type.ULONG],  # ulFlags
                                      _type.CONFIGRET]
CM_Get_Class_Property_Keys_Ex: _Callable[[_Pointer[_struct.GUID],  # ClassGUID
                                          _Pointer[_struct.DEVPROPKEY],  # PropertyKeyArray
                                          _Pointer[_type.ULONG],  # PropertyKeyCount
                                          _type.ULONG,  # ulFlags
                                          _type.HMACHINE],  # hMachine
                                         _type.CONFIGRET]
CM_Set_Class_PropertyW: _Callable[[_Pointer[_struct.GUID],  # ClassGUID
                                   _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                   _type.DEVPROPTYPE,  # PropertyType
                                   _type.PBYTE,  # PropertyBuffer
                                   _type.ULONG,  # PropertyBufferSize
                                   _type.ULONG],  # ulFlags
                                  _type.CONFIGRET]
CM_Set_Class_Property_ExW: _Callable[[_Pointer[_struct.GUID],  # ClassGUID
                                      _Pointer[_struct.DEVPROPKEY],  # PropertyKey
                                      _type.DEVPROPTYPE,  # PropertyType
                                      _type.PBYTE,  # PropertyBuffer
                                      _type.ULONG,  # PropertyBufferSize
                                      _type.ULONG,  # ulFlags
                                      _type.HMACHINE],  # hMachine
                                     _type.CONFIGRET]
CM_Get_Class_Registry_PropertyA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                            _type.ULONG,  # ulProperty
                                            _Pointer[_type.ULONG],  # pulRegDataType
                                            _type.PVOID,  # Buffer
                                            _Pointer[_type.ULONG],  # pulLength
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CM_Get_Class_Registry_PropertyW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                            _type.ULONG,  # ulProperty
                                            _Pointer[_type.ULONG],  # pulRegDataType
                                            _type.PVOID,  # Buffer
                                            _Pointer[_type.ULONG],  # pulLength
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CM_Set_Class_Registry_PropertyA: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                            _type.ULONG,  # ulProperty
                                            _type.PCVOID,  # Buffer
                                            _type.ULONG,  # ulLength
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CM_Set_Class_Registry_PropertyW: _Callable[[_Pointer[_struct.GUID],  # ClassGuid
                                            _type.ULONG,  # ulProperty
                                            _type.PCVOID,  # Buffer
                                            _type.ULONG,  # ulLength
                                            _type.ULONG,  # ulFlags
                                            _type.HMACHINE],  # hMachine
                                           _type.CONFIGRET]
CMP_WaitNoPendingInstallEvents: _Callable[[_type.DWORD],  # dwTimeout
                                          _type.DWORD]
# CM_Register_Notification: _Callable[[_Pointer[_struct.CM_NOTIFY_FILTER],  # pFilter
#                                      _type.PVOID,  # pContext
#                                      PCM_NOTIFY_CALLBACK,  # pCallback
#                                      PHCMNOTIFICATION],  # pNotifyContext
#                                     _type.CONFIGRET]
CM_Unregister_Notification: _Callable[[_type.HCMNOTIFICATION],  # NotifyContext
                                      _type.CONFIGRET]
CM_MapCrToWin32Err: _Callable[[_type.CONFIGRET,  # CmReturnCode
                               _type.DWORD],  # DefaultErr
                              _type.DWORD]

_WinLib(__name__)
