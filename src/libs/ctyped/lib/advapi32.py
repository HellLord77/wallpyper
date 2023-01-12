from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# winreg
RegCloseKey: _Callable[[_type.HKEY],  # hKey
                       _type.LSTATUS]
RegOverridePredefKey: _Callable[[_type.HKEY,  # hKey
                                 _type.HKEY],  # hNewHKey
                                _type.LSTATUS]
RegOpenUserClassesRoot: _Callable[[_type.HANDLE,  # hToken
                                   _type.DWORD,  # dwOptions
                                   _type.REGSAM,  # samDesired
                                   _Pointer[_type.HKEY]],  # phkResult
                                  _type.LSTATUS]
RegOpenCurrentUser: _Callable[[_type.REGSAM,  # samDesired
                               _Pointer[_type.HKEY]],  # phkResult
                              _type.LSTATUS]
RegDisablePredefinedCache: _Callable[[],
                                     _type.LSTATUS]
RegDisablePredefinedCacheEx: _Callable[[],
                                       _type.LSTATUS]
RegConnectRegistryA: _Callable[[_type.LPCSTR,  # lpMachineName
                                _type.HKEY,  # hKey
                                _Pointer[_type.HKEY]],  # phkResult
                               _type.LSTATUS]
RegConnectRegistryW: _Callable[[_type.LPCWSTR,  # lpMachineName
                                _type.HKEY,  # hKey
                                _Pointer[_type.HKEY]],  # phkResult
                               _type.LSTATUS]
RegConnectRegistryExA: _Callable[[_type.LPCSTR,  # lpMachineName
                                  _type.HKEY,  # hKey
                                  _type.ULONG,  # Flags
                                  _Pointer[_type.HKEY]],  # phkResult
                                 _type.LSTATUS]
RegConnectRegistryExW: _Callable[[_type.LPCWSTR,  # lpMachineName
                                  _type.HKEY,  # hKey
                                  _type.ULONG,  # Flags
                                  _Pointer[_type.HKEY]],  # phkResult
                                 _type.LSTATUS]
RegCreateKeyA: _Callable[[_type.HKEY,  # hKey
                          _type.LPCSTR,  # lpSubKey
                          _Pointer[_type.HKEY]],  # phkResult
                         _type.LSTATUS]
RegCreateKeyW: _Callable[[_type.HKEY,  # hKey
                          _type.LPCWSTR,  # lpSubKey
                          _Pointer[_type.HKEY]],  # phkResult
                         _type.LSTATUS]
RegCreateKeyExA: _Callable[[_type.HKEY,  # hKey
                            _type.LPCSTR,  # lpSubKey
                            _type.DWORD,  # Reserved
                            _type.LPSTR,  # lpClass
                            _type.DWORD,  # dwOptions
                            _type.REGSAM,  # samDesired
                            _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                            _Pointer[_type.HKEY],  # phkResult
                            _Pointer[_type.DWORD]],  # lpdwDisposition
                           _type.LSTATUS]
RegCreateKeyExW: _Callable[[_type.HKEY,  # hKey
                            _type.LPCWSTR,  # lpSubKey
                            _type.DWORD,  # Reserved
                            _type.LPWSTR,  # lpClass
                            _type.DWORD,  # dwOptions
                            _type.REGSAM,  # samDesired
                            _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                            _Pointer[_type.HKEY],  # phkResult
                            _Pointer[_type.DWORD]],  # lpdwDisposition
                           _type.LSTATUS]
RegCreateKeyTransactedA: _Callable[[_type.HKEY,  # hKey
                                    _type.LPCSTR,  # lpSubKey
                                    _type.DWORD,  # Reserved
                                    _type.LPSTR,  # lpClass
                                    _type.DWORD,  # dwOptions
                                    _type.REGSAM,  # samDesired
                                    _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                                    _Pointer[_type.HKEY],  # phkResult
                                    _Pointer[_type.DWORD],  # lpdwDisposition
                                    _type.HANDLE,  # hTransaction
                                    _type.PVOID],  # pExtendedParemeter
                                   _type.LSTATUS]
RegCreateKeyTransactedW: _Callable[[_type.HKEY,  # hKey
                                    _type.LPCWSTR,  # lpSubKey
                                    _type.DWORD,  # Reserved
                                    _type.LPWSTR,  # lpClass
                                    _type.DWORD,  # dwOptions
                                    _type.REGSAM,  # samDesired
                                    _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                                    _Pointer[_type.HKEY],  # phkResult
                                    _Pointer[_type.DWORD],  # lpdwDisposition
                                    _type.HANDLE,  # hTransaction
                                    _type.PVOID],  # pExtendedParemeter
                                   _type.LSTATUS]
RegDeleteKeyA: _Callable[[_type.HKEY,  # hKey
                          _type.LPCSTR],  # lpSubKey
                         _type.LSTATUS]
RegDeleteKeyW: _Callable[[_type.HKEY,  # hKey
                          _type.LPCWSTR],  # lpSubKey
                         _type.LSTATUS]
RegDeleteKeyExA: _Callable[[_type.HKEY,  # hKey
                            _type.LPCSTR,  # lpSubKey
                            _type.REGSAM,  # samDesired
                            _type.DWORD],  # Reserved
                           _type.LSTATUS]
RegDeleteKeyExW: _Callable[[_type.HKEY,  # hKey
                            _type.LPCWSTR,  # lpSubKey
                            _type.REGSAM,  # samDesired
                            _type.DWORD],  # Reserved
                           _type.LSTATUS]
RegDeleteKeyTransactedA: _Callable[[_type.HKEY,  # hKey
                                    _type.LPCSTR,  # lpSubKey
                                    _type.REGSAM,  # samDesired
                                    _type.DWORD,  # Reserved
                                    _type.HANDLE,  # hTransaction
                                    _type.PVOID],  # pExtendedParameter
                                   _type.LSTATUS]
RegDeleteKeyTransactedW: _Callable[[_type.HKEY,  # hKey
                                    _type.LPCWSTR,  # lpSubKey
                                    _type.REGSAM,  # samDesired
                                    _type.DWORD,  # Reserved
                                    _type.HANDLE,  # hTransaction
                                    _type.PVOID],  # pExtendedParameter
                                   _type.LSTATUS]
RegDisableReflectionKey: _Callable[[_type.HKEY],  # hBase
                                   _type.LONG]
RegEnableReflectionKey: _Callable[[_type.HKEY],  # hBase
                                  _type.LONG]
RegQueryReflectionKey: _Callable[[_type.HKEY,  # hBase
                                  _Pointer[_type.BOOL]],  # bIsReflectionDisabled
                                 _type.LONG]
RegDeleteValueA: _Callable[[_type.HKEY,  # hKey
                            _type.LPCSTR],  # lpValueName
                           _type.LSTATUS]
RegDeleteValueW: _Callable[[_type.HKEY,  # hKey
                            _type.LPCWSTR],  # lpValueName
                           _type.LSTATUS]
RegEnumKeyA: _Callable[[_type.HKEY,  # hKey
                        _type.DWORD,  # dwIndex
                        _type.LPSTR,  # lpName
                        _type.DWORD],  # cchName
                       _type.LSTATUS]
RegEnumKeyW: _Callable[[_type.HKEY,  # hKey
                        _type.DWORD,  # dwIndex
                        _type.LPWSTR,  # lpName
                        _type.DWORD],  # cchName
                       _type.LSTATUS]
RegEnumKeyExA: _Callable[[_type.HKEY,  # hKey
                          _type.DWORD,  # dwIndex
                          _type.LPSTR,  # lpName
                          _Pointer[_type.DWORD],  # lpcchName
                          _Pointer[_type.DWORD],  # lpReserved
                          _type.LPSTR,  # lpClass
                          _Pointer[_type.DWORD],  # lpcchClass
                          _Pointer[_struct.FILETIME]],  # lpftLastWriteTime
                         _type.LSTATUS]
RegEnumKeyExW: _Callable[[_type.HKEY,  # hKey
                          _type.DWORD,  # dwIndex
                          _type.LPWSTR,  # lpName
                          _Pointer[_type.DWORD],  # lpcchName
                          _Pointer[_type.DWORD],  # lpReserved
                          _type.LPWSTR,  # lpClass
                          _Pointer[_type.DWORD],  # lpcchClass
                          _Pointer[_struct.FILETIME]],  # lpftLastWriteTime
                         _type.LSTATUS]
RegEnumValueA: _Callable[[_type.HKEY,  # hKey
                          _type.DWORD,  # dwIndex
                          _type.LPSTR,  # lpValueName
                          _Pointer[_type.DWORD],  # lpcchValueName
                          _Pointer[_type.DWORD],  # lpReserved
                          _Pointer[_type.DWORD],  # lpType
                          _Pointer[_type.BYTE],  # lpData
                          _Pointer[_type.DWORD]],  # lpcbData
                         _type.LSTATUS]
RegEnumValueW: _Callable[[_type.HKEY,  # hKey
                          _type.DWORD,  # dwIndex
                          _type.LPWSTR,  # lpValueName
                          _Pointer[_type.DWORD],  # lpcchValueName
                          _Pointer[_type.DWORD],  # lpReserved
                          _Pointer[_type.DWORD],  # lpType
                          _Pointer[_type.BYTE],  # lpData
                          _Pointer[_type.DWORD]],  # lpcbData
                         _type.LSTATUS]
RegFlushKey: _Callable[[_type.HKEY],  # hKey
                       _type.LSTATUS]
# RegGetKeySecurity: _Callable[[_type.HKEY,  # hKey
#                               SECURITY_INFORMATION,  # SecurityInformation
#                               PSECURITY_DESCRIPTOR,  # pSecurityDescriptor
#                               _Pointer[_type.DWORD]],  # lpcbSecurityDescriptor
#                              _type.LSTATUS]
RegLoadKeyA: _Callable[[_type.HKEY,  # hKey
                        _type.LPCSTR,  # lpSubKey
                        _type.LPCSTR],  # lpFile
                       _type.LSTATUS]
RegLoadKeyW: _Callable[[_type.HKEY,  # hKey
                        _type.LPCWSTR,  # lpSubKey
                        _type.LPCWSTR],  # lpFile
                       _type.LSTATUS]
RegNotifyChangeKeyValue: _Callable[[_type.HKEY,  # hKey
                                    _type.BOOL,  # bWatchSubtree
                                    _type.DWORD,  # dwNotifyFilter
                                    _type.HANDLE,  # hEvent
                                    _type.BOOL],  # fAsynchronous
                                   _type.LSTATUS]
RegOpenKeyA: _Callable[[_type.HKEY,  # hKey
                        _type.LPCSTR,  # lpSubKey
                        _Pointer[_type.HKEY]],  # phkResult
                       _type.LSTATUS]
RegOpenKeyW: _Callable[[_type.HKEY,  # hKey
                        _type.LPCWSTR,  # lpSubKey
                        _Pointer[_type.HKEY]],  # phkResult
                       _type.LSTATUS]
RegOpenKeyExA: _Callable[[_type.HKEY,  # hKey
                          _type.LPCSTR,  # lpSubKey
                          _type.DWORD,  # ulOptions
                          _type.REGSAM,  # samDesired
                          _Pointer[_type.HKEY]],  # phkResult
                         _type.LSTATUS]
RegOpenKeyExW: _Callable[[_type.HKEY,  # hKey
                          _type.LPCWSTR,  # lpSubKey
                          _type.DWORD,  # ulOptions
                          _type.REGSAM,  # samDesired
                          _Pointer[_type.HKEY]],  # phkResult
                         _type.LSTATUS]
RegOpenKeyTransactedA: _Callable[[_type.HKEY,  # hKey
                                  _type.LPCSTR,  # lpSubKey
                                  _type.DWORD,  # ulOptions
                                  _type.REGSAM,  # samDesired
                                  _Pointer[_type.HKEY],  # phkResult
                                  _type.HANDLE,  # hTransaction
                                  _type.PVOID],  # pExtendedParemeter
                                 _type.LSTATUS]
RegOpenKeyTransactedW: _Callable[[_type.HKEY,  # hKey
                                  _type.LPCWSTR,  # lpSubKey
                                  _type.DWORD,  # ulOptions
                                  _type.REGSAM,  # samDesired
                                  _Pointer[_type.HKEY],  # phkResult
                                  _type.HANDLE,  # hTransaction
                                  _type.PVOID],  # pExtendedParemeter
                                 _type.LSTATUS]
RegQueryInfoKeyA: _Callable[[_type.HKEY,  # hKey
                             _type.LPSTR,  # lpClass
                             _Pointer[_type.DWORD],  # lpcchClass
                             _Pointer[_type.DWORD],  # lpReserved
                             _Pointer[_type.DWORD],  # lpcSubKeys
                             _Pointer[_type.DWORD],  # lpcbMaxSubKeyLen
                             _Pointer[_type.DWORD],  # lpcbMaxClassLen
                             _Pointer[_type.DWORD],  # lpcValues
                             _Pointer[_type.DWORD],  # lpcbMaxValueNameLen
                             _Pointer[_type.DWORD],  # lpcbMaxValueLen
                             _Pointer[_type.DWORD],  # lpcbSecurityDescriptor
                             _Pointer[_struct.FILETIME]],  # lpftLastWriteTime
                            _type.LSTATUS]
RegQueryInfoKeyW: _Callable[[_type.HKEY,  # hKey
                             _type.LPWSTR,  # lpClass
                             _Pointer[_type.DWORD],  # lpcchClass
                             _Pointer[_type.DWORD],  # lpReserved
                             _Pointer[_type.DWORD],  # lpcSubKeys
                             _Pointer[_type.DWORD],  # lpcbMaxSubKeyLen
                             _Pointer[_type.DWORD],  # lpcbMaxClassLen
                             _Pointer[_type.DWORD],  # lpcValues
                             _Pointer[_type.DWORD],  # lpcbMaxValueNameLen
                             _Pointer[_type.DWORD],  # lpcbMaxValueLen
                             _Pointer[_type.DWORD],  # lpcbSecurityDescriptor
                             _Pointer[_struct.FILETIME]],  # lpftLastWriteTime
                            _type.LSTATUS]
RegQueryValueA: _Callable[[_type.HKEY,  # hKey
                           _type.LPCSTR,  # lpSubKey
                           _type.LPSTR,  # lpData
                           _Pointer[_type.LONG]],  # lpcbData
                          _type.LSTATUS]
RegQueryValueW: _Callable[[_type.HKEY,  # hKey
                           _type.LPCWSTR,  # lpSubKey
                           _type.LPWSTR,  # lpData
                           _Pointer[_type.LONG]],  # lpcbData
                          _type.LSTATUS]
RegQueryMultipleValuesA: _Callable[[_type.HKEY,  # hKey
                                    _Pointer[_struct.VALENTA],  # val_list
                                    _type.DWORD,  # num_vals
                                    _type.LPSTR,  # lpValueBuf
                                    _Pointer[_type.DWORD]],  # ldwTotsize
                                   _type.LSTATUS]
RegQueryMultipleValuesW: _Callable[[_type.HKEY,  # hKey
                                    _Pointer[_struct.VALENTW],  # val_list
                                    _type.DWORD,  # num_vals
                                    _type.LPWSTR,  # lpValueBuf
                                    _Pointer[_type.DWORD]],  # ldwTotsize
                                   _type.LSTATUS]
RegQueryValueExA: _Callable[[_type.HKEY,  # hKey
                             _type.LPCSTR,  # lpValueName
                             _Pointer[_type.DWORD],  # lpReserved
                             _Pointer[_type.DWORD],  # lpType
                             _Pointer[_type.BYTE],  # lpData
                             _Pointer[_type.DWORD]],  # lpcbData
                            _type.LSTATUS]
RegQueryValueExW: _Callable[[_type.HKEY,  # hKey
                             _type.LPCWSTR,  # lpValueName
                             _Pointer[_type.DWORD],  # lpReserved
                             _Pointer[_type.DWORD],  # lpType
                             _Pointer[_type.BYTE],  # lpData
                             _Pointer[_type.DWORD]],  # lpcbData
                            _type.LSTATUS]
RegReplaceKeyA: _Callable[[_type.HKEY,  # hKey
                           _type.LPCSTR,  # lpSubKey
                           _type.LPCSTR,  # lpNewFile
                           _type.LPCSTR],  # lpOldFile
                          _type.LSTATUS]
RegReplaceKeyW: _Callable[[_type.HKEY,  # hKey
                           _type.LPCWSTR,  # lpSubKey
                           _type.LPCWSTR,  # lpNewFile
                           _type.LPCWSTR],  # lpOldFile
                          _type.LSTATUS]
RegRestoreKeyA: _Callable[[_type.HKEY,  # hKey
                           _type.LPCSTR,  # lpFile
                           _type.DWORD],  # dwFlags
                          _type.LSTATUS]
RegRestoreKeyW: _Callable[[_type.HKEY,  # hKey
                           _type.LPCWSTR,  # lpFile
                           _type.DWORD],  # dwFlags
                          _type.LSTATUS]
RegRenameKey: _Callable[[_type.HKEY,  # hKey
                         _type.LPCWSTR,  # lpSubKeyName
                         _type.LPCWSTR],  # lpNewKeyName
                        _type.LSTATUS]
RegSaveKeyA: _Callable[[_type.HKEY,  # hKey
                        _type.LPCSTR,  # lpFile
                        _Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpSecurityAttributes
                       _type.LSTATUS]
RegSaveKeyW: _Callable[[_type.HKEY,  # hKey
                        _type.LPCWSTR,  # lpFile
                        _Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpSecurityAttributes
                       _type.LSTATUS]
# RegSetKeySecurity: _Callable[[_type.HKEY,  # hKey
#                               SECURITY_INFORMATION,  # SecurityInformation
#                               PSECURITY_DESCRIPTOR],  # pSecurityDescriptor
#                              _type.LSTATUS]
RegSetValueA: _Callable[[_type.HKEY,  # hKey
                         _type.LPCSTR,  # lpSubKey
                         _type.DWORD,  # dwType
                         _type.LPCSTR,  # lpData
                         _type.DWORD],  # cbData
                        _type.LSTATUS]
RegSetValueW: _Callable[[_type.HKEY,  # hKey
                         _type.LPCWSTR,  # lpSubKey
                         _type.DWORD,  # dwType
                         _type.LPCWSTR,  # lpData
                         _type.DWORD],  # cbData
                        _type.LSTATUS]
RegSetValueExA: _Callable[[_type.HKEY,  # hKey
                           _type.LPCSTR,  # lpValueName
                           _type.DWORD,  # Reserved
                           _type.DWORD,  # dwType
                           _Pointer[_type.BYTE],  # lpData
                           _type.DWORD],  # cbData
                          _type.LSTATUS]
RegSetValueExW: _Callable[[_type.HKEY,  # hKey
                           _type.LPCWSTR,  # lpValueName
                           _type.DWORD,  # Reserved
                           _type.DWORD,  # dwType
                           _Pointer[_type.BYTE],  # lpData
                           _type.DWORD],  # cbData
                          _type.LSTATUS]
RegUnLoadKeyA: _Callable[[_type.HKEY,  # hKey
                          _type.LPCSTR],  # lpSubKey
                         _type.LSTATUS]
RegUnLoadKeyW: _Callable[[_type.HKEY,  # hKey
                          _type.LPCWSTR],  # lpSubKey
                         _type.LSTATUS]
RegDeleteKeyValueA: _Callable[[_type.HKEY,  # hKey
                               _type.LPCSTR,  # lpSubKey
                               _type.LPCSTR],  # lpValueName
                              _type.LSTATUS]
RegDeleteKeyValueW: _Callable[[_type.HKEY,  # hKey
                               _type.LPCWSTR,  # lpSubKey
                               _type.LPCWSTR],  # lpValueName
                              _type.LSTATUS]
RegSetKeyValueA: _Callable[[_type.HKEY,  # hKey
                            _type.LPCSTR,  # lpSubKey
                            _type.LPCSTR,  # lpValueName
                            _type.DWORD,  # dwType
                            _type.LPCVOID,  # lpData
                            _type.DWORD],  # cbData
                           _type.LSTATUS]
RegSetKeyValueW: _Callable[[_type.HKEY,  # hKey
                            _type.LPCWSTR,  # lpSubKey
                            _type.LPCWSTR,  # lpValueName
                            _type.DWORD,  # dwType
                            _type.LPCVOID,  # lpData
                            _type.DWORD],  # cbData
                           _type.LSTATUS]
RegDeleteTreeA: _Callable[[_type.HKEY,  # hKey
                           _type.LPCSTR],  # lpSubKey
                          _type.LSTATUS]
RegDeleteTreeW: _Callable[[_type.HKEY,  # hKey
                           _type.LPCWSTR],  # lpSubKey
                          _type.LSTATUS]
RegCopyTreeA: _Callable[[_type.HKEY,  # hKeySrc
                         _type.LPCSTR,  # lpSubKey
                         _type.HKEY],  # hKeyDest
                        _type.LSTATUS]
RegGetValueA: _Callable[[_type.HKEY,  # hkey
                         _type.LPCSTR,  # lpSubKey
                         _type.LPCSTR,  # lpValue
                         _type.DWORD,  # dwFlags
                         _Pointer[_type.DWORD],  # pdwType
                         _type.PVOID,  # pvData
                         _Pointer[_type.DWORD]],  # pcbData
                        _type.LSTATUS]
RegGetValueW: _Callable[[_type.HKEY,  # hkey
                         _type.LPCWSTR,  # lpSubKey
                         _type.LPCWSTR,  # lpValue
                         _type.DWORD,  # dwFlags
                         _Pointer[_type.DWORD],  # pdwType
                         _type.PVOID,  # pvData
                         _Pointer[_type.DWORD]],  # pcbData
                        _type.LSTATUS]
RegCopyTreeW: _Callable[[_type.HKEY,  # hKeySrc
                         _type.LPCWSTR,  # lpSubKey
                         _type.HKEY],  # hKeyDest
                        _type.LSTATUS]
RegLoadMUIStringA: _Callable[[_type.HKEY,  # hKey
                              _type.LPCSTR,  # pszValue
                              _type.LPSTR,  # pszOutBuf
                              _type.DWORD,  # cbOutBuf
                              _Pointer[_type.DWORD],  # pcbData
                              _type.DWORD,  # Flags
                              _type.LPCSTR],  # pszDirectory
                             _type.LSTATUS]
RegLoadMUIStringW: _Callable[[_type.HKEY,  # hKey
                              _type.LPCWSTR,  # pszValue
                              _type.LPWSTR,  # pszOutBuf
                              _type.DWORD,  # cbOutBuf
                              _Pointer[_type.DWORD],  # pcbData
                              _type.DWORD,  # Flags
                              _type.LPCWSTR],  # pszDirectory
                             _type.LSTATUS]
RegLoadAppKeyA: _Callable[[_type.LPCSTR,  # lpFile
                           _Pointer[_type.HKEY],  # phkResult
                           _type.REGSAM,  # samDesired
                           _type.DWORD,  # dwOptions
                           _type.DWORD],  # Reserved
                          _type.LSTATUS]
RegLoadAppKeyW: _Callable[[_type.LPCWSTR,  # lpFile
                           _Pointer[_type.HKEY],  # phkResult
                           _type.REGSAM,  # samDesired
                           _type.DWORD,  # dwOptions
                           _type.DWORD],  # Reserved
                          _type.LSTATUS]
InitiateSystemShutdownA: _Callable[[_type.LPSTR,  # lpMachineName
                                    _type.LPSTR,  # lpMessage
                                    _type.DWORD,  # dwTimeout
                                    _type.BOOL,  # bForceAppsClosed
                                    _type.BOOL],  # bRebootAfterShutdown
                                   _type.BOOL]
InitiateSystemShutdownW: _Callable[[_type.LPWSTR,  # lpMachineName
                                    _type.LPWSTR,  # lpMessage
                                    _type.DWORD,  # dwTimeout
                                    _type.BOOL,  # bForceAppsClosed
                                    _type.BOOL],  # bRebootAfterShutdown
                                   _type.BOOL]
AbortSystemShutdownA: _Callable[[_type.LPSTR],  # lpMachineName
                                _type.BOOL]
AbortSystemShutdownW: _Callable[[_type.LPWSTR],  # lpMachineName
                                _type.BOOL]
InitiateSystemShutdownExA: _Callable[[_type.LPSTR,  # lpMachineName
                                      _type.LPSTR,  # lpMessage
                                      _type.DWORD,  # dwTimeout
                                      _type.BOOL,  # bForceAppsClosed
                                      _type.BOOL,  # bRebootAfterShutdown
                                      _type.DWORD],  # dwReason
                                     _type.BOOL]
InitiateSystemShutdownExW: _Callable[[_type.LPWSTR,  # lpMachineName
                                      _type.LPWSTR,  # lpMessage
                                      _type.DWORD,  # dwTimeout
                                      _type.BOOL,  # bForceAppsClosed
                                      _type.BOOL,  # bRebootAfterShutdown
                                      _type.DWORD],  # dwReason
                                     _type.BOOL]
InitiateShutdownA: _Callable[[_type.LPSTR,  # lpMachineName
                              _type.LPSTR,  # lpMessage
                              _type.DWORD,  # dwGracePeriod
                              _type.DWORD,  # dwShutdownFlags
                              _type.DWORD],  # dwReason
                             _type.DWORD]
InitiateShutdownW: _Callable[[_type.LPWSTR,  # lpMachineName
                              _type.LPWSTR,  # lpMessage
                              _type.DWORD,  # dwGracePeriod
                              _type.DWORD,  # dwShutdownFlags
                              _type.DWORD],  # dwReason
                             _type.DWORD]
CheckForHiberboot: _Callable[[_Pointer[_type.BOOLEAN],  # pHiberboot
                              _type.BOOLEAN],  # bClearFlag
                             _type.DWORD]
RegSaveKeyExA: _Callable[[_type.HKEY,  # hKey
                          _type.LPCSTR,  # lpFile
                          _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                          _type.DWORD],  # Flags
                         _type.LSTATUS]
RegSaveKeyExW: _Callable[[_type.HKEY,  # hKey
                          _type.LPCWSTR,  # lpFile
                          _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                          _type.DWORD],  # Flags
                         _type.LSTATUS]

_WinLib(__name__)
