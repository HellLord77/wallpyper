from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .. import union as _union
from .._utils import _Pointer

# commapi
ClearCommBreak: _Callable[[_type.HANDLE],  # hFile
                          _type.BOOL]
ClearCommError: _Callable[[_type.HANDLE,  # hFile
                           _Optional[_Pointer[_type.DWORD]],  # lpErrors
                           _Optional[_Pointer[_struct.COMSTAT]]],  # lpStat
                          _type.BOOL]
SetupComm: _Callable[[_type.HANDLE,  # hFile
                      _type.DWORD,  # dwInQueue
                      _type.DWORD],  # dwOutQueue
                     _type.BOOL]
EscapeCommFunction: _Callable[[_type.HANDLE,  # hFile
                               _type.DWORD],  # dwFunc
                              _type.BOOL]
GetCommConfig: _Callable[[_type.HANDLE,  # hCommDev
                          _Pointer[_struct.COMMCONFIG],  # lpCC
                          _Pointer[_type.WORD]],  # lpdwSize
                         _type.BOOL]
GetCommMask: _Callable[[_type.HANDLE,  # hFile
                        _Pointer[_type.DWORD]],  # lpEvtMask
                       _type.BOOL]
GetCommModemStatus: _Callable[[_type.HANDLE,  # hFile
                               _Pointer[_type.DWORD]],  # lpModemStat
                              _type.BOOL]
GetCommProperties: _Callable[[_type.HANDLE,  # hFile
                              _Pointer[_struct.COMMPROP]],  # lpCommProp
                             _type.BOOL]
GetCommState: _Callable[[_type.HANDLE,  # hFile
                         _Pointer[_struct.DCB]],  # lpDCB
                        _type.BOOL]
GetCommTimeouts: _Callable[[_type.HANDLE,  # hFile
                            _Pointer[_struct.COMMTIMEOUTS]],  # lpCommTimeouts
                           _type.BOOL]
PurgeComm: _Callable[[_type.HANDLE,  # hFile
                      _type.DWORD],  # dwFlags
                     _type.BOOL]
SetCommBreak: _Callable[[_type.HANDLE],  # hFile
                        _type.BOOL]
SetCommConfig: _Callable[[_type.HANDLE,  # hCommDev
                          _Pointer[_struct.COMMCONFIG],  # lpCC
                          _type.DWORD],  # dwSize
                         _type.BOOL]
SetCommMask: _Callable[[_type.HANDLE,  # hFile
                        _type.DWORD],  # dwEvtMask
                       _type.BOOL]
SetCommState: _Callable[[_type.HANDLE,  # hFile
                         _Pointer[_struct.DCB]],  # lpDCB
                        _type.BOOL]
SetCommTimeouts: _Callable[[_type.HANDLE,  # hFile
                            _Pointer[_struct.COMMTIMEOUTS]],  # lpCommTimeouts
                           _type.BOOL]
TransmitCommChar: _Callable[[_type.HANDLE,  # hFile
                             _type.c_char],  # cChar
                            _type.BOOL]
WaitCommEvent: _Callable[[_type.HANDLE,  # hFile
                          _Pointer[_type.DWORD],  # lpEvtMask
                          _Optional[_Pointer[_struct.OVERLAPPED]]],  # lpOverlapped
                         _type.BOOL]
OpenCommPort: _Callable[[_type.ULONG,  # uPortNumber
                         _type.DWORD,  # dwDesiredAccess
                         _type.DWORD],  # dwFlagsAndAttributes
                        _type.HANDLE]
GetCommPorts: _Callable[[_Pointer[_type.ULONG],  # lpPortNumbers
                         _type.ULONG,  # uPortNumbersCount
                         _Pointer[_type.ULONG]],  # puPortNumbersFound
                        _type.ULONG]
# consoleapi
AllocConsole: _Callable[[],
                        _type.BOOL]
FreeConsole: _Callable[[],
                       _type.BOOL]
AttachConsole: _Callable[[_type.DWORD],  # dwProcessId
                         _type.BOOL]
GetConsoleCP: _Callable[[],
                        _type.UINT]
GetConsoleOutputCP: _Callable[[],
                              _type.UINT]
GetConsoleMode: _Callable[[_type.HANDLE,  # hConsoleHandle
                           _Pointer[_type.DWORD]],  # lpMode
                          _type.BOOL]
SetConsoleMode: _Callable[[_type.HANDLE,  # hConsoleHandle
                           _type.DWORD],  # dwMode
                          _type.BOOL]
GetNumberOfConsoleInputEvents: _Callable[[_type.HANDLE,  # hConsoleInput
                                          _Pointer[_type.DWORD]],  # lpNumberOfEvents
                                         _type.BOOL]
ReadConsoleA: _Callable[[_type.HANDLE,  # hConsoleInput
                         _type.LPVOID,  # lpBuffer
                         _type.DWORD,  # nNumberOfCharsToRead
                         _Pointer[_type.DWORD],  # lpNumberOfCharsRead
                         _Optional[_Pointer[_struct.CONSOLE_READCONSOLE_CONTROL]]],  # pInputControl
                        _type.BOOL]
ReadConsoleW: _Callable[[_type.HANDLE,  # hConsoleInput
                         _type.LPVOID,  # lpBuffer
                         _type.DWORD,  # nNumberOfCharsToRead
                         _Pointer[_type.DWORD],  # lpNumberOfCharsRead
                         _Optional[_Pointer[_struct.CONSOLE_READCONSOLE_CONTROL]]],  # pInputControl
                        _type.BOOL]
WriteConsoleA: _Callable[[_type.HANDLE,  # hConsoleOutput
                          _type.PVOID,  # lpBuffer
                          _type.DWORD,  # nNumberOfCharsToWrite
                          _Optional[_Pointer[_type.DWORD]],  # lpNumberOfCharsWritten
                          _type.LPVOID],  # lpReserved
                         _type.BOOL]
WriteConsoleW: _Callable[[_type.HANDLE,  # hConsoleOutput
                          _type.PVOID,  # lpBuffer
                          _type.DWORD,  # nNumberOfCharsToWrite
                          _Optional[_Pointer[_type.DWORD]],  # lpNumberOfCharsWritten
                          _type.LPVOID],  # lpReserved
                         _type.BOOL]
SetConsoleCtrlHandler: _Callable[[_Optional[_type.PHANDLER_ROUTINE],  # HandlerRoutine
                                  _type.BOOL],  # Add
                                 _type.BOOL]
# consoleapi2
GenerateConsoleCtrlEvent: _Callable[[_type.DWORD,  # dwCtrlEvent
                                     _type.DWORD],  # dwProcessGroupId
                                    _type.BOOL]
SetConsoleActiveScreenBuffer: _Callable[[_type.HANDLE],  # hConsoleOutput
                                        _type.BOOL]
FlushConsoleInputBuffer: _Callable[[_type.HANDLE],  # hConsoleInput
                                   _type.BOOL]
SetConsoleCP: _Callable[[_type.UINT],  # wCodePageID
                        _type.BOOL]
SetConsoleOutputCP: _Callable[[_type.UINT],  # wCodePageID
                              _type.BOOL]
SetConsoleScreenBufferSize: _Callable[[_type.HANDLE,  # hConsoleOutput
                                       _struct.COORD],  # dwSize
                                      _type.BOOL]
SetConsoleCursorPosition: _Callable[[_type.HANDLE,  # hConsoleOutput
                                     _struct.COORD],  # dwCursorPosition
                                    _type.BOOL]
GetLargestConsoleWindowSize: _Callable[[_type.HANDLE],  # hConsoleOutput
                                       _struct.COORD]
SetConsoleTextAttribute: _Callable[[_type.HANDLE,  # hConsoleOutput
                                    _type.WORD],  # wAttributes
                                   _type.BOOL]
GetConsoleTitleA: _Callable[[_type.LPSTR,  # lpConsoleTitle
                             _type.DWORD],  # nSize
                            _type.DWORD]
GetConsoleTitleW: _Callable[[_type.LPWSTR,  # lpConsoleTitle
                             _type.DWORD],  # nSize
                            _type.DWORD]
GetConsoleOriginalTitleA: _Callable[[_type.LPSTR,  # lpConsoleTitle
                                     _type.DWORD],  # nSize
                                    _type.DWORD]
GetConsoleOriginalTitleW: _Callable[[_type.LPWSTR,  # lpConsoleTitle
                                     _type.DWORD],  # nSize
                                    _type.DWORD]
SetConsoleTitleA: _Callable[[_type.LPCSTR],  # lpConsoleTitle
                            _type.BOOL]
SetConsoleTitleW: _Callable[[_type.LPCWSTR],  # lpConsoleTitle
                            _type.BOOL]
# consoleapi3
GetNumberOfConsoleMouseButtons: _Callable[[_Pointer[_type.DWORD]],  # lpNumberOfMouseButtons
                                          _type.BOOL]
GetConsoleFontSize: _Callable[[_type.HANDLE,  # hConsoleOutput
                               _type.DWORD],  # nFont
                              _struct.COORD]
GetCurrentConsoleFont: _Callable[[_type.HANDLE,  # hConsoleOutput
                                  _type.BOOL,  # bMaximumWindow
                                  _Pointer[_struct.CONSOLE_FONT_INFO]],  # lpConsoleCurrentFont
                                 _type.BOOL]
GetCurrentConsoleFontEx: _Callable[[_type.HANDLE,  # hConsoleOutput
                                    _type.BOOL,  # bMaximumWindow
                                    _Pointer[_struct.CONSOLE_FONT_INFOEX]],  # lpConsoleCurrentFont
                                   _type.BOOL]
SetCurrentConsoleFontEx: _Callable[[_type.HANDLE,  # hConsoleOutput
                                    _type.BOOL,  # bMaximumWindow
                                    _Pointer[_struct.CONSOLE_FONT_INFOEX]],  # lpConsoleCurrentFont
                                   _type.BOOL]
GetConsoleSelectionInfo: _Callable[[_Pointer[_struct.CONSOLE_SELECTION_INFO]],  # lpConsoleSelectionInfo
                                   _type.BOOL]
GetConsoleHistoryInfo: _Callable[[_Pointer[_struct.CONSOLE_HISTORY_INFO]],  # lpConsoleHistoryInfo
                                 _type.BOOL]
SetConsoleHistoryInfo: _Callable[[_Pointer[_struct.CONSOLE_HISTORY_INFO]],  # lpConsoleHistoryInfo
                                 _type.BOOL]
GetConsoleDisplayMode: _Callable[[_Pointer[_type.DWORD]],  # lpModeFlags
                                 _type.BOOL]
SetConsoleDisplayMode: _Callable[[_type.HANDLE,  # hConsoleOutput
                                  _type.DWORD,  # dwFlags
                                  _Optional[_Pointer[_struct.COORD]]],  # lpNewScreenBufferDimensions
                                 _type.BOOL]
GetConsoleWindow: _Callable[[],
                            _type.HWND]
AddConsoleAliasA: _Callable[[_type.LPSTR,  # Source
                             _type.LPSTR,  # Target
                             _type.LPSTR],  # ExeName
                            _type.BOOL]
AddConsoleAliasW: _Callable[[_type.LPWSTR,  # Source
                             _type.LPWSTR,  # Target
                             _type.LPWSTR],  # ExeName
                            _type.BOOL]
GetConsoleAliasA: _Callable[[_type.LPSTR,  # Source
                             _type.LPSTR,  # TargetBuffer
                             _type.DWORD,  # TargetBufferLength
                             _type.LPSTR],  # ExeName
                            _type.DWORD]
GetConsoleAliasW: _Callable[[_type.LPWSTR,  # Source
                             _type.LPWSTR,  # TargetBuffer
                             _type.DWORD,  # TargetBufferLength
                             _type.LPWSTR],  # ExeName
                            _type.DWORD]
GetConsoleAliasesLengthA: _Callable[[_type.LPSTR],  # ExeName
                                    _type.DWORD]
GetConsoleAliasesLengthW: _Callable[[_type.LPWSTR],  # ExeName
                                    _type.DWORD]
GetConsoleAliasExesLengthA: _Callable[[],
                                      _type.DWORD]
GetConsoleAliasExesLengthW: _Callable[[],
                                      _type.DWORD]
GetConsoleAliasesA: _Callable[[_type.LPSTR,  # AliasBuffer
                               _type.DWORD,  # AliasBufferLength
                               _type.LPSTR],  # ExeName
                              _type.DWORD]
GetConsoleAliasesW: _Callable[[_type.LPWSTR,  # AliasBuffer
                               _type.DWORD,  # AliasBufferLength
                               _type.LPWSTR],  # ExeName
                              _type.DWORD]
GetConsoleAliasExesA: _Callable[[_type.LPSTR,  # ExeNameBuffer
                                 _type.DWORD],  # ExeNameBufferLength
                                _type.DWORD]
GetConsoleAliasExesW: _Callable[[_type.LPWSTR,  # ExeNameBuffer
                                 _type.DWORD],  # ExeNameBufferLength
                                _type.DWORD]
ExpungeConsoleCommandHistoryA: _Callable[[_type.LPSTR],  # ExeName
                                         _type.VOID]
ExpungeConsoleCommandHistoryW: _Callable[[_type.LPWSTR],  # ExeName
                                         _type.VOID]
SetConsoleNumberOfCommandsA: _Callable[[_type.DWORD,  # Number
                                        _type.LPSTR],  # ExeName
                                       _type.BOOL]
SetConsoleNumberOfCommandsW: _Callable[[_type.DWORD,  # Number
                                        _type.LPWSTR],  # ExeName
                                       _type.BOOL]
GetConsoleCommandHistoryLengthA: _Callable[[_type.LPSTR],  # ExeName
                                           _type.DWORD]
GetConsoleCommandHistoryLengthW: _Callable[[_type.LPWSTR],  # ExeName
                                           _type.DWORD]
GetConsoleCommandHistoryA: _Callable[[_type.LPSTR,  # Commands
                                      _type.DWORD,  # CommandBufferLength
                                      _type.LPSTR],  # ExeName
                                     _type.DWORD]
GetConsoleCommandHistoryW: _Callable[[_type.LPWSTR,  # Commands
                                      _type.DWORD,  # CommandBufferLength
                                      _type.LPWSTR],  # ExeName
                                     _type.DWORD]
GetConsoleProcessList: _Callable[[_Pointer[_type.DWORD],  # lpdwProcessList
                                  _type.DWORD],  # dwProcessCount
                                 _type.DWORD]
# errhandlingapi
GetLastError: _Callable[[],
                        _type.DWORD]
SetLastError: _Callable[[_type.DWORD],  # dwErrCode
                        _type.VOID]
GetErrorMode: _Callable[[],
                        _type.UINT]
SetErrorMode: _Callable[[_type.UINT],  # uMode
                        _type.UINT]
RemoveVectoredExceptionHandler: _Callable[[_type.PVOID],  # Handle
                                          _type.ULONG]
RemoveVectoredContinueHandler: _Callable[[_type.PVOID],  # Handle
                                         _type.ULONG]
RestoreLastError: _Callable[[_type.DWORD],  # dwErrCode
                            _type.VOID]
FatalAppExitA: _Callable[[_type.UINT,  # uAction
                          _type.LPCSTR],  # lpMessageText
                         _type.VOID]
FatalAppExitW: _Callable[[_type.UINT,  # uAction
                          _type.LPCWSTR],  # lpMessageText
                         _type.VOID]
GetThreadErrorMode: _Callable[[],
                              _type.DWORD]
SetThreadErrorMode: _Callable[[_type.DWORD,  # dwNewMode
                               _Optional[_Pointer[_type.DWORD]]],  # lpOldMode
                              _type.BOOL]
TerminateProcessOnMemoryExhaustion: _Callable[[_type.SIZE_T],  # FailedAllocationSize
                                              _type.VOID]
# fileapi
CompareFileTime: _Callable[[_Pointer[_struct.FILETIME],  # lpFileTime1
                            _Pointer[_struct.FILETIME]],  # lpFileTime2
                           _type.LONG]
CreateDirectoryA: _Callable[[_type.LPCSTR,  # lpPathName
                             _Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpSecurityAttributes
                            _type.BOOL]
CreateDirectoryW: _Callable[[_type.LPCWSTR,  # lpPathName
                             _Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpSecurityAttributes
                            _type.BOOL]
CreateFileA: _Callable[[_type.LPCSTR,  # lpFileName
                        _type.DWORD,  # dwDesiredAccess
                        _type.DWORD,  # dwShareMode
                        _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                        _type.DWORD,  # dwCreationDisposition
                        _type.DWORD,  # dwFlagsAndAttributes
                        _type.HANDLE],  # hTemplateFile
                       _type.HANDLE]
CreateFileW: _Callable[[_type.LPCWSTR,  # lpFileName
                        _type.DWORD,  # dwDesiredAccess
                        _type.DWORD,  # dwShareMode
                        _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                        _type.DWORD,  # dwCreationDisposition
                        _type.DWORD,  # dwFlagsAndAttributes
                        _type.HANDLE],  # hTemplateFile
                       _type.HANDLE]
DefineDosDeviceW: _Callable[[_type.DWORD,  # dwFlags
                             _type.LPCWSTR,  # lpDeviceName
                             _type.LPCWSTR],  # lpTargetPath
                            _type.BOOL]
DeleteFileA: _Callable[[_type.LPCSTR],  # lpFileName
                       _type.BOOL]
DeleteFileW: _Callable[[_type.LPCWSTR],  # lpFileName
                       _type.BOOL]
DeleteVolumeMountPointW: _Callable[[_type.LPCWSTR],  # lpszVolumeMountPoint
                                   _type.BOOL]
FileTimeToLocalFileTime: _Callable[[_Pointer[_struct.FILETIME],  # lpFileTime
                                    _Pointer[_struct.FILETIME]],  # lpLocalFileTime
                                   _type.BOOL]
FindClose: _Callable[[_type.HANDLE],  # hFindFile
                     _type.BOOL]
FindCloseChangeNotification: _Callable[[_type.HANDLE],  # hChangeHandle
                                       _type.BOOL]
FindFirstChangeNotificationA: _Callable[[_type.LPCSTR,  # lpPathName
                                         _type.BOOL,  # bWatchSubtree
                                         _type.DWORD],  # dwNotifyFilter
                                        _type.HANDLE]
FindFirstChangeNotificationW: _Callable[[_type.LPCWSTR,  # lpPathName
                                         _type.BOOL,  # bWatchSubtree
                                         _type.DWORD],  # dwNotifyFilter
                                        _type.HANDLE]
FindFirstFileA: _Callable[[_type.LPCSTR,  # lpFileName
                           _Pointer[_struct.WIN32_FIND_DATAA]],  # lpFindFileData
                          _type.HANDLE]
FindFirstFileW: _Callable[[_type.LPCWSTR,  # lpFileName
                           _Pointer[_struct.WIN32_FIND_DATAW]],  # lpFindFileData
                          _type.HANDLE]
FindFirstFileExA: _Callable[[_type.LPCSTR,  # lpFileName
                             _enum.FINDEX_INFO_LEVELS,  # fInfoLevelId
                             _type.LPVOID,  # lpFindFileData
                             _enum.FINDEX_SEARCH_OPS,  # fSearchOp
                             _type.LPVOID,  # lpSearchFilter
                             _type.DWORD],  # dwAdditionalFlags
                            _type.HANDLE]
FindFirstFileExW: _Callable[[_type.LPCWSTR,  # lpFileName
                             _enum.FINDEX_INFO_LEVELS,  # fInfoLevelId
                             _type.LPVOID,  # lpFindFileData
                             _enum.FINDEX_SEARCH_OPS,  # fSearchOp
                             _type.LPVOID,  # lpSearchFilter
                             _type.DWORD],  # dwAdditionalFlags
                            _type.HANDLE]
FindFirstVolumeW: _Callable[[_type.LPWSTR,  # lpszVolumeName
                             _type.DWORD],  # cchBufferLength
                            _type.HANDLE]
FindNextChangeNotification: _Callable[[_type.HANDLE],  # hChangeHandle
                                      _type.BOOL]
FindNextFileA: _Callable[[_type.HANDLE,  # hFindFile
                          _Pointer[_struct.WIN32_FIND_DATAA]],  # lpFindFileData
                         _type.BOOL]
FindNextFileW: _Callable[[_type.HANDLE,  # hFindFile
                          _Pointer[_struct.WIN32_FIND_DATAW]],  # lpFindFileData
                         _type.BOOL]
FindNextVolumeW: _Callable[[_type.HANDLE,  # hFindVolume
                            _type.LPWSTR,  # lpszVolumeName
                            _type.DWORD],  # cchBufferLength
                           _type.BOOL]
FindVolumeClose: _Callable[[_type.HANDLE],  # hFindVolume
                           _type.BOOL]
FlushFileBuffers: _Callable[[_type.HANDLE],  # hFile
                            _type.BOOL]
GetDiskFreeSpaceA: _Callable[[_type.LPCSTR,  # lpRootPathName
                              _Pointer[_type.DWORD],  # lpSectorsPerCluster
                              _Pointer[_type.DWORD],  # lpBytesPerSector
                              _Pointer[_type.DWORD],  # lpNumberOfFreeClusters
                              _Pointer[_type.DWORD]],  # lpTotalNumberOfClusters
                             _type.BOOL]
GetDiskFreeSpaceW: _Callable[[_type.LPCWSTR,  # lpRootPathName
                              _Pointer[_type.DWORD],  # lpSectorsPerCluster
                              _Pointer[_type.DWORD],  # lpBytesPerSector
                              _Pointer[_type.DWORD],  # lpNumberOfFreeClusters
                              _Pointer[_type.DWORD]],  # lpTotalNumberOfClusters
                             _type.BOOL]
GetDiskFreeSpaceExA: _Callable[[_type.LPCSTR,  # lpDirectoryName
                                _Pointer[_union.ULARGE_INTEGER],  # lpFreeBytesAvailableToCaller
                                _Pointer[_union.ULARGE_INTEGER],  # lpTotalNumberOfBytes
                                _Pointer[_union.ULARGE_INTEGER]],  # lpTotalNumberOfFreeBytes
                               _type.BOOL]
GetDiskFreeSpaceExW: _Callable[[_type.LPCWSTR,  # lpDirectoryName
                                _Pointer[_union.ULARGE_INTEGER],  # lpFreeBytesAvailableToCaller
                                _Pointer[_union.ULARGE_INTEGER],  # lpTotalNumberOfBytes
                                _Pointer[_union.ULARGE_INTEGER]],  # lpTotalNumberOfFreeBytes
                               _type.BOOL]
GetDiskSpaceInformationA: _Callable[[_type.LPCSTR,  # rootPath
                                     _Pointer[_struct.DISK_SPACE_INFORMATION]],  # diskSpaceInfo
                                    _type.HRESULT]
GetDiskSpaceInformationW: _Callable[[_type.LPCWSTR,  # rootPath
                                     _Pointer[_struct.DISK_SPACE_INFORMATION]],  # diskSpaceInfo
                                    _type.HRESULT]
GetDriveTypeA: _Callable[[_type.LPCSTR],  # lpRootPathName
                         _type.UINT]
GetDriveTypeW: _Callable[[_type.LPCWSTR],  # lpRootPathName
                         _type.UINT]
GetFileAttributesA: _Callable[[_type.LPCSTR],  # lpFileName
                              _type.DWORD]
GetFileAttributesW: _Callable[[_type.LPCWSTR],  # lpFileName
                              _type.DWORD]
GetFileAttributesExA: _Callable[[_type.LPCSTR,  # lpFileName
                                 _enum.GET_FILEEX_INFO_LEVELS,  # fInfoLevelId
                                 _type.LPVOID],  # lpFileInformation
                                _type.BOOL]
GetFileAttributesExW: _Callable[[_type.LPCWSTR,  # lpFileName
                                 _enum.GET_FILEEX_INFO_LEVELS,  # fInfoLevelId
                                 _type.LPVOID],  # lpFileInformation
                                _type.BOOL]
GetFileInformationByHandle: _Callable[[_type.HANDLE,  # hFile
                                       _Pointer[_struct.BY_HANDLE_FILE_INFORMATION]],  # lpFileInformation
                                      _type.BOOL]
GetFileSize: _Callable[[_type.HANDLE,  # hFile
                        _Pointer[_type.DWORD]],  # lpFileSizeHigh
                       _type.DWORD]
GetFileSizeEx: _Callable[[_type.HANDLE,  # hFile
                          _Pointer[_struct.LARGE_INTEGER]],  # lpFileSize
                         _type.BOOL]
GetFileType: _Callable[[_type.HANDLE],  # hFile
                       _type.DWORD]
GetFinalPathNameByHandleA: _Callable[[_type.HANDLE,  # hFile
                                      _type.LPSTR,  # lpszFilePath
                                      _type.DWORD,  # cchFilePath
                                      _type.DWORD],  # dwFlags
                                     _type.DWORD]
GetFinalPathNameByHandleW: _Callable[[_type.HANDLE,  # hFile
                                      _type.LPWSTR,  # lpszFilePath
                                      _type.DWORD,  # cchFilePath
                                      _type.DWORD],  # dwFlags
                                     _type.DWORD]
GetFileTime: _Callable[[_type.HANDLE,  # hFile
                        _Pointer[_struct.FILETIME],  # lpCreationTime
                        _Pointer[_struct.FILETIME],  # lpLastAccessTime
                        _Pointer[_struct.FILETIME]],  # lpLastWriteTime
                       _type.BOOL]
GetFullPathNameW: _Callable[[_type.LPCWSTR,  # lpFileName
                             _type.DWORD,  # nBufferLength
                             _type.LPWSTR,  # lpBuffer
                             _Pointer[_type.LPWSTR]],  # lpFilePart
                            _type.DWORD]
GetFullPathNameA: _Callable[[_type.LPCSTR,  # lpFileName
                             _type.DWORD,  # nBufferLength
                             _type.LPSTR,  # lpBuffer
                             _Pointer[_type.LPSTR]],  # lpFilePart
                            _type.DWORD]
GetLogicalDrives: _Callable[[],
                            _type.DWORD]
GetLogicalDriveStringsW: _Callable[[_type.DWORD,  # nBufferLength
                                    _type.LPWSTR],  # lpBuffer
                                   _type.DWORD]
GetLongPathNameA: _Callable[[_type.LPCSTR,  # lpszShortPath
                             _type.LPSTR,  # lpszLongPath
                             _type.DWORD],  # cchBuffer
                            _type.DWORD]
GetLongPathNameW: _Callable[[_type.LPCWSTR,  # lpszShortPath
                             _type.LPWSTR,  # lpszLongPath
                             _type.DWORD],  # cchBuffer
                            _type.DWORD]
AreShortNamesEnabled: _Callable[[_type.HANDLE,  # Handle
                                 _Pointer[_type.BOOL]],  # Enabled
                                _type.BOOL]
GetShortPathNameW: _Callable[[_type.LPCWSTR,  # lpszLongPath
                              _type.LPWSTR,  # lpszShortPath
                              _type.DWORD],  # cchBuffer
                             _type.DWORD]
GetTempFileNameW: _Callable[[_type.LPCWSTR,  # lpPathName
                             _type.LPCWSTR,  # lpPrefixString
                             _type.UINT,  # uUnique
                             _type.LPWSTR],  # lpTempFileName
                            _type.UINT]
GetVolumeInformationByHandleW: _Callable[[_type.HANDLE,  # hFile
                                          _type.LPWSTR,  # lpVolumeNameBuffer
                                          _type.DWORD,  # nVolumeNameSize
                                          _Pointer[_type.DWORD],  # lpVolumeSerialNumber
                                          _Pointer[_type.DWORD],  # lpMaximumComponentLength
                                          _Pointer[_type.DWORD],  # lpFileSystemFlags
                                          _type.LPWSTR,  # lpFileSystemNameBuffer
                                          _type.DWORD],  # nFileSystemNameSize
                                         _type.BOOL]
GetVolumeInformationW: _Callable[[_type.LPCWSTR,  # lpRootPathName
                                  _type.LPWSTR,  # lpVolumeNameBuffer
                                  _type.DWORD,  # nVolumeNameSize
                                  _Pointer[_type.DWORD],  # lpVolumeSerialNumber
                                  _Pointer[_type.DWORD],  # lpMaximumComponentLength
                                  _Pointer[_type.DWORD],  # lpFileSystemFlags
                                  _type.LPWSTR,  # lpFileSystemNameBuffer
                                  _type.DWORD],  # nFileSystemNameSize
                                 _type.BOOL]
GetVolumePathNameW: _Callable[[_type.LPCWSTR,  # lpszFileName
                               _type.LPWSTR,  # lpszVolumePathName
                               _type.DWORD],  # cchBufferLength
                              _type.BOOL]
LocalFileTimeToFileTime: _Callable[[_Pointer[_struct.FILETIME],  # lpLocalFileTime
                                    _Pointer[_struct.FILETIME]],  # lpFileTime
                                   _type.BOOL]
LockFile: _Callable[[_type.HANDLE,  # hFile
                     _type.DWORD,  # dwFileOffsetLow
                     _type.DWORD,  # dwFileOffsetHigh
                     _type.DWORD,  # nNumberOfBytesToLockLow
                     _type.DWORD],  # nNumberOfBytesToLockHigh
                    _type.BOOL]
LockFileEx: _Callable[[_type.HANDLE,  # hFile
                       _type.DWORD,  # dwFlags
                       _type.DWORD,  # dwReserved
                       _type.DWORD,  # nNumberOfBytesToLockLow
                       _type.DWORD,  # nNumberOfBytesToLockHigh
                       _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                      _type.BOOL]
QueryDosDeviceW: _Callable[[_type.LPCWSTR,  # lpDeviceName
                            _type.LPWSTR,  # lpTargetPath
                            _type.DWORD],  # ucchMax
                           _type.DWORD]
ReadFile: _Callable[[_type.HANDLE,  # hFile
                     _type.LPVOID,  # lpBuffer
                     _type.DWORD,  # nNumberOfBytesToRead
                     _Pointer[_type.DWORD],  # lpNumberOfBytesRead
                     _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                    _type.BOOL]
ReadFileEx: _Callable[[_type.HANDLE,  # hFile
                       _type.LPVOID,  # lpBuffer
                       _type.DWORD,  # nNumberOfBytesToRead
                       _Pointer[_struct.OVERLAPPED],  # lpOverlapped
                       _type.LPOVERLAPPED_COMPLETION_ROUTINE],  # lpCompletionRoutine
                      _type.BOOL]
ReadFileScatter: _Callable[[_type.HANDLE,  # hFile
                            _Pointer[_union.FILE_SEGMENT_ELEMENT],  # aSegmentArray
                            _type.DWORD,  # nNumberOfBytesToRead
                            _Pointer[_type.DWORD],  # lpReserved
                            _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                           _type.BOOL]
RemoveDirectoryA: _Callable[[_type.LPCSTR],  # lpPathName
                            _type.BOOL]
RemoveDirectoryW: _Callable[[_type.LPCWSTR],  # lpPathName
                            _type.BOOL]
SetEndOfFile: _Callable[[_type.HANDLE],  # hFile
                        _type.BOOL]
SetFileAttributesA: _Callable[[_type.LPCSTR,  # lpFileName
                               _type.DWORD],  # dwFileAttributes
                              _type.BOOL]
SetFileAttributesW: _Callable[[_type.LPCWSTR,  # lpFileName
                               _type.DWORD],  # dwFileAttributes
                              _type.BOOL]
SetFileInformationByHandle: _Callable[[_type.HANDLE,  # hFile
                                       _enum.FILE_INFO_BY_HANDLE_CLASS,  # FileInformationClass
                                       _type.LPVOID,  # lpFileInformation
                                       _type.DWORD],  # dwBufferSize
                                      _type.BOOL]
SetFilePointer: _Callable[[_type.HANDLE,  # hFile
                           _type.LONG,  # lDistanceToMove
                           _Pointer[_type.LONG],  # lpDistanceToMoveHigh
                           _type.DWORD],  # dwMoveMethod
                          _type.DWORD]
SetFilePointerEx: _Callable[[_type.HANDLE,  # hFile
                             _union.LARGE_INTEGER,  # liDistanceToMove
                             _Pointer[_union.LARGE_INTEGER],  # lpNewFilePointer
                             _type.DWORD],  # dwMoveMethod
                            _type.BOOL]
SetFileTime: _Callable[[_type.HANDLE,  # hFile
                        _Pointer[_struct.FILETIME],  # lpCreationTime
                        _Pointer[_struct.FILETIME],  # lpLastAccessTime
                        _Pointer[_struct.FILETIME]],  # lpLastWriteTime
                       _type.BOOL]
SetFileValidData: _Callable[[_type.HANDLE,  # hFile
                             _type.LONGLONG],  # ValidDataLength
                            _type.BOOL]
UnlockFile: _Callable[[_type.HANDLE,  # hFile
                       _type.DWORD,  # dwFileOffsetLow
                       _type.DWORD,  # dwFileOffsetHigh
                       _type.DWORD,  # nNumberOfBytesToUnlockLow
                       _type.DWORD],  # nNumberOfBytesToUnlockHigh
                      _type.BOOL]
UnlockFileEx: _Callable[[_type.HANDLE,  # hFile
                         _type.DWORD,  # dwReserved
                         _type.DWORD,  # nNumberOfBytesToUnlockLow
                         _type.DWORD,  # nNumberOfBytesToUnlockHigh
                         _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                        _type.BOOL]
WriteFile: _Callable[[_type.HANDLE,  # hFile
                      _type.LPCVOID,  # lpBuffer
                      _type.DWORD,  # nNumberOfBytesToWrite
                      _Pointer[_type.DWORD],  # lpNumberOfBytesWritten
                      _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                     _type.BOOL]
WriteFileEx: _Callable[[_type.HANDLE,  # hFile
                        _type.LPCVOID,  # lpBuffer
                        _type.DWORD,  # nNumberOfBytesToWrite
                        _Pointer[_struct.OVERLAPPED],  # lpOverlapped
                        _type.LPOVERLAPPED_COMPLETION_ROUTINE],  # lpCompletionRoutine
                       _type.BOOL]
WriteFileGather: _Callable[[_type.HANDLE,  # hFile
                            _Pointer[_union.FILE_SEGMENT_ELEMENT],  # aSegmentArray
                            _type.DWORD,  # nNumberOfBytesToWrite
                            _Pointer[_type.DWORD],  # lpReserved
                            _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                           _type.BOOL]
GetTempPathW: _Callable[[_type.DWORD,  # nBufferLength
                         _type.LPWSTR],  # lpBuffer
                        _type.DWORD]
GetVolumeNameForVolumeMountPointW: _Callable[[_type.LPCWSTR,  # lpszVolumeMountPoint
                                              _type.LPWSTR,  # lpszVolumeName
                                              _type.DWORD],  # cchBufferLength
                                             _type.BOOL]
GetVolumePathNamesForVolumeNameW: _Callable[[_type.LPCWSTR,  # lpszVolumeName
                                             _type.LPWCH,  # lpszVolumePathNames
                                             _type.DWORD,  # cchBufferLength
                                             _Pointer[_type.DWORD]],  # lpcchReturnLength
                                            _type.BOOL]
CreateFile2: _Callable[[_type.LPCWSTR,  # lpFileName
                        _type.DWORD,  # dwDesiredAccess
                        _type.DWORD,  # dwShareMode
                        _type.DWORD,  # dwCreationDisposition
                        _Pointer[_struct.CREATEFILE2_EXTENDED_PARAMETERS]],  # pCreateExParams
                       _type.HANDLE]
SetFileIoOverlappedRange: _Callable[[_type.HANDLE,  # FileHandle
                                     _Pointer[_type.UCHAR],  # OverlappedRangeStart
                                     _type.ULONG],  # Length
                                    _type.BOOL]
GetCompressedFileSizeA: _Callable[[_type.LPCSTR,  # lpFileName
                                   _Pointer[_type.DWORD]],  # lpFileSizeHigh
                                  _type.DWORD]
GetCompressedFileSizeW: _Callable[[_type.LPCWSTR,  # lpFileName
                                   _Pointer[_type.DWORD]],  # lpFileSizeHigh
                                  _type.DWORD]
FindFirstStreamW: _Callable[[_type.LPCWSTR,  # lpFileName
                             _enum.STREAM_INFO_LEVELS,  # InfoLevel
                             _type.LPVOID,  # lpFindStreamData
                             _type.DWORD],  # dwFlags
                            _type.HANDLE]
FindNextStreamW: _Callable[[_type.HANDLE,  # hFindStream
                            _type.LPVOID],  # lpFindStreamData
                           _type.BOOL]
AreFileApisANSI: _Callable[[],
                           _type.BOOL]
GetTempPathA: _Callable[[_type.DWORD,  # nBufferLength
                         _type.LPSTR],  # lpBuffer
                        _type.DWORD]
FindFirstFileNameW: _Callable[[_type.LPCWSTR,  # lpFileName
                               _type.DWORD,  # dwFlags
                               _Pointer[_type.DWORD],  # StringLength
                               _type.PWSTR],  # LinkName
                              _type.HANDLE]
FindNextFileNameW: _Callable[[_type.HANDLE,  # hFindStream
                              _Pointer[_type.DWORD],  # StringLength
                              _type.PWSTR],  # LinkName
                             _type.BOOL]
GetVolumeInformationA: _Callable[[_type.LPCSTR,  # lpRootPathName
                                  _type.LPSTR,  # lpVolumeNameBuffer
                                  _type.DWORD,  # nVolumeNameSize
                                  _Pointer[_type.DWORD],  # lpVolumeSerialNumber
                                  _Pointer[_type.DWORD],  # lpMaximumComponentLength
                                  _Pointer[_type.DWORD],  # lpFileSystemFlags
                                  _type.LPSTR,  # lpFileSystemNameBuffer
                                  _type.DWORD],  # nFileSystemNameSize
                                 _type.BOOL]
GetTempFileNameA: _Callable[[_type.LPCSTR,  # lpPathName
                             _type.LPCSTR,  # lpPrefixString
                             _type.UINT,  # uUnique
                             _type.LPSTR],  # lpTempFileName
                            _type.UINT]
SetFileApisToOEM: _Callable[[],
                            _type.c_void]
SetFileApisToANSI: _Callable[[],
                             _type.c_void]
GetTempPath2W: _Callable[[_type.DWORD,  # BufferLength
                          _type.LPWSTR],  # Buffer
                         _type.DWORD]
GetTempPath2A: _Callable[[_type.DWORD,  # BufferLength
                          _type.LPSTR],  # Buffer
                         _type.DWORD]
# handleapi
CloseHandle: _Callable[[_type.HANDLE],
                       _type.BOOL]
# heapapi
GetProcessHeap: _Callable[[],
                          _type.HANDLE]
GetProcessHeaps: _Callable[[_type.DWORD,
                            _Pointer[_type.HANDLE]],
                           _type.DWORD]
HeapAlloc: _Callable[[_type.HANDLE,
                      _type.DWORD,
                      _type.SIZE_T],
                     _type.LPVOID]
HeapCompact: _Callable[[_type.HANDLE,
                        _type.DWORD],
                       _type.SIZE_T]
HeapCreate: _Callable[[_type.DWORD,
                       _type.SIZE_T,
                       _type.SIZE_T],
                      _type.HANDLE]
HeapDestroy: _Callable[[_type.HANDLE],
                       _type.BOOL]
HeapFree: _Callable[[_type.HANDLE,
                     _type.DWORD,
                     _Optional[_type.LPVOID]],
                    _type.BOOL]
HeapLock: _Callable[[_type.HANDLE],
                    _type.BOOL]
HeapQueryInformation: _Callable[[_Optional[_type.HANDLE],
                                 _enum.HEAP_INFORMATION_CLASS,
                                 _Optional[_type.PVOID],
                                 _type.SIZE_T,
                                 _Optional[_Pointer[_type.SIZE_T]]],
                                _type.BOOL]
HeapReAlloc: _Callable[[_type.HANDLE,
                        _type.DWORD,
                        _Optional[_type.LPVOID],
                        _type.SIZE_T],
                       _type.LPVOID]
HeapSetInformation: _Callable[[_Optional[_type.HANDLE],
                               _enum.HEAP_INFORMATION_CLASS,
                               _Optional[_type.PVOID],
                               _type.SIZE_T],
                              _type.BOOL]
HeapSize: _Callable[[_type.HANDLE,
                     _type.DWORD,
                     _type.LPCVOID],
                    _type.SIZE_T]
HeapSummary: _Callable[[_type.HANDLE,
                        _type.DWORD,
                        _struct.HEAP_SUMMARY],
                       _type.BOOL]
HeapUnlock: _Callable[[_type.HANDLE],
                      _type.BOOL]
HeapValidate: _Callable[[_type.HANDLE,
                         _type.DWORD,
                         _Optional[_type.LPCVOID]],
                        _type.BOOL]
HeapWalk: _Callable[[_type.HANDLE,
                     _Pointer[_struct.PROCESS_HEAP_ENTRY]],
                    _type.BOOL]
# ioapiset
CreateIoCompletionPort: _Callable[[_type.HANDLE,  # FileHandle
                                   _Optional[_type.HANDLE],  # ExistingCompletionPort
                                   _type.ULONG_PTR,  # CompletionKey
                                   _type.DWORD],  # NumberOfConcurrentThreads
                                  _type.HANDLE]
GetQueuedCompletionStatus: _Callable[[_type.HANDLE,  # CompletionPort
                                      _Pointer[_type.DWORD],  # lpNumberOfBytesTransferred
                                      _Pointer[_type.ULONG_PTR],  # lpCompletionKey
                                      _Pointer[_Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                                      _type.DWORD],  # dwMilliseconds
                                     _type.BOOL]
GetQueuedCompletionStatusEx: _Callable[[_type.HANDLE,  # CompletionPort
                                        _Pointer[_struct.OVERLAPPED_ENTRY],  # lpCompletionPortEntries
                                        _type.ULONG,  # ulCount
                                        _Pointer[_type.ULONG],  # ulNumEntriesRemoved
                                        _type.DWORD,  # dwMilliseconds
                                        _type.BOOL],  # fAlertable
                                       _type.BOOL]
PostQueuedCompletionStatus: _Callable[[_type.HANDLE,  # CompletionPort
                                       _type.DWORD,  # dwNumberOfBytesTransferred
                                       _type.ULONG_PTR,  # dwCompletionKey
                                       _Optional[_Pointer[_struct.OVERLAPPED]]],  # lpOverlapped
                                      _type.BOOL]
DeviceIoControl: _Callable[[_type.HANDLE,  # hDevice
                            _type.DWORD,  # dwIoControlCode
                            _Optional[_type.LPVOID],  # lpInBuffer
                            _type.DWORD,  # nInBufferSize
                            _Optional[_type.LPVOID],  # lpOutBuffer
                            _type.DWORD,  # nOutBufferSize
                            _Optional[_Pointer[_type.DWORD]],  # lpBytesReturned
                            _Optional[_Pointer[_struct.OVERLAPPED]]],  # lpOverlapped
                           _type.BOOL]
GetOverlappedResult: _Callable[[_type.HANDLE,  # hFile
                                _Pointer[_struct.OVERLAPPED],  # lpOverlapped
                                _Pointer[_type.DWORD],  # lpNumberOfBytesTransferred
                                _type.BOOL],  # bWait
                               _type.BOOL]
CancelIoEx: _Callable[[_type.HANDLE,  # hFile
                       _Optional[_Pointer[_struct.OVERLAPPED]]],  # lpOverlapped
                      _type.BOOL]
CancelIo: _Callable[[_type.HANDLE],  # hFile
                    _type.BOOL]
GetOverlappedResultEx: _Callable[[_type.HANDLE,  # hFile
                                  _Pointer[_struct.OVERLAPPED],  # lpOverlapped
                                  _Pointer[_type.DWORD],  # lpNumberOfBytesTransferred
                                  _type.DWORD,  # dwMilliseconds
                                  _type.BOOL],  # bWait
                                 _type.BOOL]
CancelSynchronousIo: _Callable[[_type.HANDLE],  # hThread
                               _type.BOOL]
# libloaderapi
AddDllDirectory: _Callable[[_type.LPCWSTR],
                           _type.DLL_DIRECTORY_COOKIE]
DisableThreadLibraryCalls: _Callable[[_type.HMODULE],
                                     _type.BOOL]
EnumResourceLanguagesA: _Callable[[_Optional[_type.HMODULE],
                                   _type.LPCSTR,
                                   _type.LPCSTR,
                                   _type.ENUMRESLANGPROCA,
                                   _type.LONG_PTR],
                                  _type.BOOL]
EnumResourceLanguagesW: _Callable[[_Optional[_type.HMODULE],
                                   _type.LPCWSTR,
                                   _type.LPCWSTR,
                                   _type.ENUMRESLANGPROCW,
                                   _type.LONG_PTR],
                                  _type.BOOL]
EnumResourceLanguagesExA: _Callable[[_Optional[_type.HMODULE],
                                     _type.LPCSTR,
                                     _type.LPCSTR,
                                     _type.ENUMRESLANGPROCA,
                                     _Optional[_type.LONG_PTR],
                                     _type.DWORD,
                                     _type.LANGID],
                                    _type.BOOL]
EnumResourceLanguagesExW: _Callable[[_Optional[_type.HMODULE],
                                     _type.LPCWSTR,
                                     _type.LPCWSTR,
                                     _type.ENUMRESLANGPROCW,
                                     _Optional[_type.LONG_PTR],
                                     _type.DWORD,
                                     _type.LANGID],
                                    _type.BOOL]
EnumResourceNamesA: _Callable[[_Optional[_type.HMODULE],
                               _type.LPCSTR,
                               _type.ENUMRESNAMEPROCA,
                               _type.LONG_PTR],
                              _type.BOOL]
EnumResourceNamesW: _Callable[[_Optional[_type.HMODULE],
                               _type.LPCWSTR,
                               _type.ENUMRESNAMEPROCW,
                               _type.LONG_PTR],
                              _type.BOOL]
EnumResourceNamesExA: _Callable[[_Optional[_type.HMODULE],
                                 _type.LPCSTR,
                                 _type.ENUMRESNAMEPROCA,
                                 _type.LONG_PTR,
                                 _type.DWORD,
                                 _type.LANGID],
                                _type.BOOL]
EnumResourceNamesExW: _Callable[[_Optional[_type.HMODULE],
                                 _type.LPCWSTR,
                                 _type.ENUMRESNAMEPROCW,
                                 _type.LONG_PTR,
                                 _type.DWORD,
                                 _type.LANGID],
                                _type.BOOL]
EnumResourceTypesA: _Callable[[_Optional[_type.HMODULE],
                               _type.ENUMRESTYPEPROCA,
                               _type.LONG_PTR],
                              _type.BOOL]
EnumResourceTypesW: _Callable[[_Optional[_type.HMODULE],
                               _type.ENUMRESTYPEPROCW,
                               _type.LONG_PTR],
                              _type.BOOL]
EnumResourceTypesExA: _Callable[[_Optional[_type.HMODULE],
                                 _type.ENUMRESTYPEPROCA,
                                 _type.LONG_PTR,
                                 _type.DWORD,
                                 _type.LANGID],
                                _type.BOOL]
EnumResourceTypesExW: _Callable[[_Optional[_type.HMODULE],
                                 _type.ENUMRESTYPEPROCW,
                                 _type.LONG_PTR,
                                 _type.DWORD,
                                 _type.LANGID],
                                _type.BOOL]
FreeLibrary: _Callable[[_type.HMODULE],
                       _type.BOOL]
FreeLibraryAndExitThread: _Callable[[_type.HMODULE,
                                     _type.DWORD],
                                    _type.VOID]
FreeResource: _Callable[[_type.HGLOBAL],
                        _type.BOOL]
FindResourceW: _Callable[[_Optional[_type.HMODULE],
                          _type.LPCWSTR,
                          _type.LPCWSTR],
                         _type.HRSRC]
FindResourceExW: _Callable[[_Optional[_type.HMODULE],
                            _type.LPCWSTR,
                            _type.LPCWSTR,
                            _type.WORD],
                           _type.HRSRC]
FindStringOrdinal: _Callable[[_type.DWORD,
                              _type.LPCWSTR,
                              _type.c_int,
                              _type.LPCWSTR,
                              _type.c_int,
                              _type.BOOL],
                             _type.c_int]
GetModuleFileNameA: _Callable[[_Optional[_type.HMODULE],
                               _type.LPSTR,
                               _type.DWORD],
                              _type.DWORD]
GetModuleFileNameW: _Callable[[_Optional[_type.HMODULE],
                               _type.LPWSTR,
                               _type.DWORD],
                              _type.DWORD]
GetModuleHandleA: _Callable[[_Optional[_type.LPCSTR]],
                            _type.HMODULE]
GetModuleHandleW: _Callable[[_Optional[_type.LPCWSTR]],
                            _type.HMODULE]
GetModuleHandleExA: _Callable[[_type.DWORD,
                               _Optional[_type.LPCSTR],
                               _Pointer[_type.HMODULE]],
                              _type.BOOL]
GetModuleHandleExW: _Callable[[_type.DWORD,
                               _Optional[_type.LPCWSTR],
                               _Pointer[_type.HMODULE]],
                              _type.BOOL]
GetProcAddress: _Callable[[_type.HMODULE,
                           _type.LPCSTR],
                          _type.FARPROC]
LoadLibraryA: _Callable[[_type.LPCSTR],
                        _type.HMODULE]
LoadLibraryW: _Callable[[_type.LPCWSTR],
                        _type.HMODULE]
LoadLibraryExA: _Callable[[_type.LPCSTR,
                           _type.HANDLE,
                           _type.DWORD],
                          _type.HMODULE]
LoadLibraryExW: _Callable[[_type.LPCWSTR,
                           _type.HANDLE,
                           _type.DWORD],
                          _type.HMODULE]
LoadResource: _Callable[[_Optional[_type.HMODULE],
                         _type.HRSRC],
                        _type.HGLOBAL]
LockResource: _Callable[[_type.HGLOBAL],
                        _type.LPVOID]
RemoveDllDirectory: _Callable[[_type.DLL_DIRECTORY_COOKIE],
                              _type.BOOL]
SetDefaultDllDirectories: _Callable[[_type.DWORD],
                                    _type.BOOL]
SizeofResource: _Callable[[_Optional[_type.HMODULE],
                           _type.HRSRC],
                          _type.DWORD]
# memoryapi
VirtualFree: _Callable[[_type.LPVOID,  # lpAddress
                        _type.SIZE_T,  # dwSize
                        _type.DWORD],  # dwFreeType
                       _type.BOOL]
VirtualAllocEx: _Callable[[_type.HANDLE,  # hProcess
                           _Optional[_type.LPVOID],  # lpAddress
                           _type.SIZE_T,  # dwSize
                           _type.DWORD,  # flAllocationType
                           _type.DWORD],  # flProtect
                          _type.LPVOID]
VirtualProtectEx: _Callable[[_type.HANDLE,  # hProcess
                             _type.LPVOID,  # lpAddress
                             _type.SIZE_T,  # dwSize
                             _type.DWORD,  # flNewProtect
                             _Pointer[_type.DWORD]],  # lpflOldProtect
                            _type.BOOL]
ReadProcessMemory: _Callable[[_type.HANDLE,  # hProcess
                              _type.LPCVOID,  # lpBaseAddress
                              _type.LPVOID,  # lpBuffer
                              _type.SIZE_T,  # nSize
                              _Optional[_Pointer[_type.SIZE_T]]],  # lpNumberOfBytesRead
                             _type.BOOL]
WriteProcessMemory: _Callable[[_type.HANDLE,  # hProcess
                               _type.LPVOID,  # lpBaseAddress
                               _type.LPCVOID,  # lpBuffer
                               _type.SIZE_T,  # nSize
                               _Optional[_Pointer[_type.SIZE_T]]],  # lpNumberOfBytesWritten
                              _type.BOOL]
OpenFileMappingW: _Callable[[_type.DWORD,  # dwDesiredAccess
                             _type.BOOL,  # bInheritHandle
                             _type.LPCWSTR],  # lpName
                            _type.HANDLE]
MapViewOfFile: _Callable[[_type.HANDLE,  # hFileMappingObject
                          _type.DWORD,  # dwDesiredAccess
                          _type.DWORD,  # dwFileOffsetHigh
                          _type.DWORD,  # dwFileOffsetLow
                          _type.SIZE_T],  # dwNumberOfBytesToMap
                         _type.LPVOID]
MapViewOfFileEx: _Callable[[_type.HANDLE,  # hFileMappingObject
                            _type.DWORD,  # dwDesiredAccess
                            _type.DWORD,  # dwFileOffsetHigh
                            _type.DWORD,  # dwFileOffsetLow
                            _type.SIZE_T,  # dwNumberOfBytesToMap
                            _Optional[_type.LPVOID]],  # lpBaseAddress
                           _type.LPVOID]
VirtualFreeEx: _Callable[[_type.HANDLE,  # hProcess
                          _type.LPVOID,  # lpAddress
                          _type.SIZE_T,  # dwSize
                          _type.DWORD],  # dwFreeType
                         _type.BOOL]
FlushViewOfFile: _Callable[[_type.LPCVOID,  # lpBaseAddress
                            _type.SIZE_T],  # dwNumberOfBytesToFlush
                           _type.BOOL]
UnmapViewOfFile: _Callable[[_type.LPCVOID],  # lpBaseAddress
                           _type.BOOL]
GetLargePageMinimum: _Callable[[],
                               _type.SIZE_T]
VirtualLock: _Callable[[_type.LPVOID,  # lpAddress
                        _type.SIZE_T],  # dwSize
                       _type.BOOL]
VirtualUnlock: _Callable[[_type.LPVOID,  # lpAddress
                          _type.SIZE_T],  # dwSize
                         _type.BOOL]
ResetWriteWatch: _Callable[[_type.LPVOID,  # lpBaseAddress
                            _type.SIZE_T],  # dwRegionSize
                           _type.UINT]
QueryMemoryResourceNotification: _Callable[[_type.HANDLE,  # ResourceNotificationHandle
                                            _Pointer[_type.BOOL]],  # ResourceState
                                           _type.BOOL]
# namedpipeapi
CreatePipe: _Callable[[_Pointer[_type.HANDLE],  # hReadPipe
                       _Pointer[_type.HANDLE],  # hWritePipe
                       _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpPipeAttributes
                       _type.DWORD],  # nSize
                      _type.BOOL]
ConnectNamedPipe: _Callable[[_type.HANDLE,  # hNamedPipe
                             _Optional[_Pointer[_struct.OVERLAPPED]]],  # lpOverlapped
                            _type.BOOL]
DisconnectNamedPipe: _Callable[[_type.HANDLE],  # hNamedPipe
                               _type.BOOL]
SetNamedPipeHandleState: _Callable[[_type.HANDLE,  # hNamedPipe
                                    _Optional[_Pointer[_type.DWORD]],  # lpMode
                                    _Optional[_Pointer[_type.DWORD]],  # lpMaxCollectionCount
                                    _Optional[_Pointer[_type.DWORD]]],  # lpCollectDataTimeout
                                   _type.BOOL]
PeekNamedPipe: _Callable[[_type.HANDLE,  # hNamedPipe
                          _Optional[_type.LPVOID],  # lpBuffer
                          _type.DWORD,  # nBufferSize
                          _Optional[_Pointer[_type.DWORD]],  # lpBytesRead
                          _Optional[_Pointer[_type.DWORD]],  # lpTotalBytesAvail
                          _Optional[_Pointer[_type.DWORD]]],  # lpBytesLeftThisMessage
                         _type.BOOL]
TransactNamedPipe: _Callable[[_type.HANDLE,  # hNamedPipe
                              _Optional[_type.LPVOID],  # lpInBuffer
                              _type.DWORD,  # nInBufferSize
                              _Optional[_type.LPVOID],  # lpOutBuffer
                              _type.DWORD,  # nOutBufferSize
                              _Optional[_Pointer[_type.DWORD]],  # lpBytesRead
                              _Optional[_Pointer[_struct.OVERLAPPED]]],  # lpOverlapped
                             _type.BOOL]
CreateNamedPipeW: _Callable[[_type.LPCWSTR,  # lpName
                             _type.DWORD,  # dwOpenMode
                             _type.DWORD,  # dwPipeMode
                             _type.DWORD,  # nMaxInstances
                             _type.DWORD,  # nOutBufferSize
                             _type.DWORD,  # nInBufferSize
                             _type.DWORD,  # nDefaultTimeOut
                             _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]]],  # lpSecurityAttributes
                            _type.HANDLE]
WaitNamedPipeW: _Callable[[_type.LPCWSTR,  # lpNamedPipeName
                           _type.DWORD],  # nTimeOut
                          _type.BOOL]
GetNamedPipeClientComputerNameW: _Callable[[_type.HANDLE,  # Pipe
                                            _type.LPWSTR,  # ClientComputerName
                                            _type.ULONG],  # ClientComputerNameLength
                                           _type.BOOL]
ImpersonateNamedPipeClient: _Callable[[_type.HANDLE],  # hNamedPipe
                                      _type.BOOL]
GetNamedPipeInfo: _Callable[[_type.HANDLE,  # hNamedPipe
                             _Optional[_Pointer[_type.DWORD]],  # lpFlags
                             _Optional[_Pointer[_type.DWORD]],  # lpOutBufferSize
                             _Optional[_Pointer[_type.DWORD]],  # lpInBufferSize
                             _Optional[_Pointer[_type.DWORD]]],  # lpMaxInstances
                            _type.BOOL]
GetNamedPipeHandleStateW: _Callable[[_type.HANDLE,  # hNamedPipe
                                     _Optional[_Pointer[_type.DWORD]],  # lpState
                                     _Optional[_Pointer[_type.DWORD]],  # lpCurInstances
                                     _Optional[_Pointer[_type.DWORD]],  # lpMaxCollectionCount
                                     _Optional[_Pointer[_type.DWORD]],  # lpCollectDataTimeout
                                     _Optional[_Pointer[_type.LPWSTR]],  # lpUserName
                                     _type.DWORD],  # nMaxUserNameSize
                                    _type.BOOL]
CallNamedPipeW: _Callable[[_type.LPCWSTR,  # lpNamedPipeName
                           _Optional[_type.LPVOID],  # lpInBuffer
                           _type.DWORD,  # nInBufferSize
                           _Optional[_type.LPVOID],  # lpOutBuffer
                           _type.DWORD,  # nOutBufferSize
                           _Pointer[_type.DWORD],  # lpBytesRead
                           _type.DWORD],  # nTimeOut
                          _type.BOOL]
# processenv
SetEnvironmentStringsW: _Callable[[_type.LPWCH],  # NewEnvironment
                                  _type.BOOL]
GetStdHandle: _Callable[[_type.DWORD],  # nStdHandle
                        _type.HANDLE]
SetStdHandle: _Callable[[_type.DWORD,  # nStdHandle
                         _type.HANDLE],  # hHandle
                        _type.BOOL]
SetStdHandleEx: _Callable[[_type.DWORD,  # nStdHandle
                           _type.HANDLE,  # hHandle
                           _Optional[_Pointer[_type.HANDLE]]],  # phPrevValue
                          _type.BOOL]
GetCommandLineA: _Callable[[],
                           _type.LPSTR]
GetCommandLineW: _Callable[[],
                           _type.LPWSTR]
GetEnvironmentStrings: _Callable[[],
                                 _type.LPCH]
GetEnvironmentStringsW: _Callable[[],
                                  _type.LPWCH]
FreeEnvironmentStringsA: _Callable[[_type.LPCH],  # penv
                                   _type.BOOL]
FreeEnvironmentStringsW: _Callable[[_type.LPWCH],  # penv
                                   _type.BOOL]
GetEnvironmentVariableA: _Callable[[_Optional[_type.LPCSTR],  # lpName
                                    _Optional[_type.LPSTR],  # lpBuffer
                                    _type.DWORD],  # nSize
                                   _type.DWORD]
GetEnvironmentVariableW: _Callable[[_Optional[_type.LPCWSTR],  # lpName
                                    _Optional[_type.LPWSTR],  # lpBuffer
                                    _type.DWORD],  # nSize
                                   _type.DWORD]
SetEnvironmentVariableA: _Callable[[_type.LPCSTR,  # lpName
                                    _Optional[_type.LPCSTR]],  # lpValue
                                   _type.BOOL]
SetEnvironmentVariableW: _Callable[[_type.LPCWSTR,  # lpName
                                    _Optional[_type.LPCWSTR]],  # lpValue
                                   _type.BOOL]
SetCurrentDirectoryA: _Callable[[_type.LPCSTR],  # lpPathName
                                _type.BOOL]
SetCurrentDirectoryW: _Callable[[_type.LPCWSTR],  # lpPathName
                                _type.BOOL]
GetCurrentDirectoryA: _Callable[[_type.DWORD,  # nBufferLength
                                 _Optional[_type.LPSTR]],  # lpBuffer
                                _type.DWORD]
GetCurrentDirectoryW: _Callable[[_type.DWORD,  # nBufferLength
                                 _Optional[_type.LPWSTR]],  # lpBuffer
                                _type.DWORD]
NeedCurrentDirectoryForExePathA: _Callable[[_type.LPCSTR],  # ExeName
                                           _type.BOOL]
NeedCurrentDirectoryForExePathW: _Callable[[_type.LPCWSTR],  # ExeName
                                           _type.BOOL]
GetEnvironmentStringsA: _Callable[[],
                                  _type.LPCH]
# processthreadsapi
GetCurrentProcess: _Callable[[],
                             _type.HANDLE]
GetCurrentProcessId: _Callable[[],
                               _type.DWORD]
ExitProcess: _Callable[[_type.UINT],  # uExitCode
                       _type.VOID]
TerminateProcess: _Callable[[_type.HANDLE,  # hProcess
                             _type.UINT],  # uExitCode
                            _type.BOOL]
GetExitCodeProcess: _Callable[[_type.HANDLE,  # hProcess
                               _Pointer[_type.DWORD]],  # lpExitCode
                              _type.BOOL]
SwitchToThread: _Callable[[],
                          _type.BOOL]
CreateThread: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpThreadAttributes
                         _type.SIZE_T,  # dwStackSize
                         _type.LPTHREAD_START_ROUTINE,  # lpStartAddress
                         _Optional[_type.LPVOID],  # lpParameter
                         _type.DWORD,  # dwCreationFlags
                         _Optional[_Pointer[_type.DWORD]]],  # lpThreadId
                        _type.HANDLE]
CreateRemoteThread: _Callable[[_type.HANDLE,  # hProcess
                               _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpThreadAttributes
                               _type.SIZE_T,  # dwStackSize
                               _type.LPTHREAD_START_ROUTINE,  # lpStartAddress
                               _Optional[_type.LPVOID],  # lpParameter
                               _type.DWORD,  # dwCreationFlags
                               _Optional[_Pointer[_type.DWORD]]],  # lpThreadId
                              _type.HANDLE]
GetCurrentThread: _Callable[[],
                            _type.HANDLE]
GetCurrentThreadId: _Callable[[],
                              _type.DWORD]
OpenThread: _Callable[[_type.DWORD,  # dwDesiredAccess
                       _type.BOOL,  # bInheritHandle
                       _type.DWORD],  # dwThreadId
                      _type.HANDLE]
SetThreadPriority: _Callable[[_type.HANDLE,  # hThread
                              _type.c_int],  # nPriority
                             _type.BOOL]
SetThreadPriorityBoost: _Callable[[_type.HANDLE,  # hThread
                                   _type.BOOL],  # DisablePriorityBoost
                                  _type.BOOL]
GetThreadPriorityBoost: _Callable[[_type.HANDLE,  # hThread
                                   _Pointer[_type.BOOL]],  # pDisablePriorityBoost
                                  _type.BOOL]
GetThreadPriority: _Callable[[_type.HANDLE],  # hThread
                             _type.c_int]
ExitThread: _Callable[[_type.DWORD],  # dwExitCode
                      _type.VOID]
TerminateThread: _Callable[[_type.HANDLE,  # hThread
                            _type.DWORD],  # dwExitCode
                           _type.BOOL]
GetExitCodeThread: _Callable[[_type.HANDLE,  # hThread
                              _Pointer[_type.DWORD]],  # lpExitCode
                             _type.BOOL]
SuspendThread: _Callable[[_type.HANDLE],  # hThread
                         _type.DWORD]
ResumeThread: _Callable[[_type.HANDLE],  # hThread
                        _type.DWORD]
TlsAlloc: _Callable[[],
                    _type.DWORD]
TlsGetValue: _Callable[[_type.DWORD],  # dwTlsIndex
                       _type.LPVOID]
TlsSetValue: _Callable[[_type.DWORD,  # dwTlsIndex
                        _Optional[_type.LPVOID]],  # lpTlsValue
                       _type.BOOL]
OpenProcess: _Callable[[_type.DWORD,  # dwDesiredAccess
                        _type.BOOL,  # bInheritHandle
                        _type.DWORD],  # dwProcessId
                       _type.HANDLE]
IsProcessorFeaturePresent: _Callable[[_type.DWORD],  # ProcessorFeature
                                     _type.BOOL]
GetProcessHandleCount: _Callable[[_type.HANDLE,  # hProcess
                                  _Pointer[_type.DWORD]],  # pdwHandleCount
                                 _type.BOOL]
GetCurrentProcessorNumber: _Callable[[],
                                     _type.DWORD]
GetProcessPriorityBoost: _Callable[[_type.HANDLE,  # hProcess
                                    _Pointer[_type.BOOL]],  # pDisablePriorityBoost
                                   _type.BOOL]
SetProcessPriorityBoost: _Callable[[_type.HANDLE,  # hProcess
                                    _type.BOOL],  # bDisablePriorityBoost
                                   _type.BOOL]
# profileapi
QueryPerformanceCounter: _Callable[[_Pointer[_union.LARGE_INTEGER]],  # lpPerformanceCount
                                   _type.BOOL]
QueryPerformanceFrequency: _Callable[[_Pointer[_union.LARGE_INTEGER]],  # lpFrequency
                                     _type.BOOL]
# synchapi
SetEvent: _Callable[[_type.HANDLE],  # hEvent
                    _type.BOOL]
ResetEvent: _Callable[[_type.HANDLE],  # hEvent
                      _type.BOOL]
ReleaseSemaphore: _Callable[[_type.HANDLE,  # hSemaphore
                             _type.LONG,  # lReleaseCount
                             _Optional[_Pointer[_type.LONG]]],  # lpPreviousCount
                            _type.BOOL]
ReleaseMutex: _Callable[[_type.HANDLE],  # hMutex
                        _type.BOOL]
WaitForSingleObject: _Callable[[_type.HANDLE,  # hHandle,
                                _type.DWORD],  # dwMilliseconds
                               _type.DWORD]
SleepEx: _Callable[[_type.DWORD,  # dwMilliseconds
                    _type.BOOL],  # bAlertable
                   _type.DWORD]
WaitForSingleObjectEx: _Callable[[_type.HANDLE,  # hHandle,
                                  _type.DWORD,  # dwMilliseconds
                                  _type.BOOL],  # bAlertable
                                 _type.DWORD]
WaitForMultipleObjectsEx: _Callable[[_type.BOOL,  # nCount
                                     _Pointer[_type.HANDLE],  # lpHandles,
                                     _type.BOOL,  # bWaitAll
                                     _type.DWORD,  # dwMilliseconds
                                     _type.BOOL],  # bAlertable
                                    _type.DWORD]
CreateMutexA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpMutexAttributes
                         _type.BOOL,  # bInitialOwner
                         _Optional[_type.LPCSTR]],  # lpName
                        _type.HANDLE]
CreateMutexW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpMutexAttributes
                         _type.BOOL,  # bInitialOwner
                         _Optional[_type.LPCWSTR]],  # lpName
                        _type.HANDLE]
CreateEventA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpEventAttributes
                         _type.BOOL,  # bManualReset
                         _type.BOOL,  # bInitialState
                         _Optional[_type.LPCSTR]],  # lpName
                        _type.HANDLE]
CreateEventW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpEventAttributes
                         _type.BOOL,  # bManualReset
                         _type.BOOL,  # bInitialState
                         _Optional[_type.LPCWSTR]],  # lpName
                        _type.HANDLE]
OpenMutexW: _Callable[[_type.DWORD,  # dwDesiredAccess
                       _type.BOOL,  # bInheritHandle
                       _type.LPCWSTR],  # lpName
                      _type.HANDLE]
OpenEventA: _Callable[[_type.DWORD,  # dwDesiredAccess
                       _type.BOOL,  # bInheritHandle
                       _type.LPCSTR],  # lpName
                      _type.HANDLE]
OpenEventW: _Callable[[_type.DWORD,  # dwDesiredAccess
                       _type.BOOL,  # bInheritHandle
                       _type.LPCWSTR],  # lpName
                      _type.HANDLE]
OpenSemaphoreW: _Callable[[_type.DWORD,  # dwDesiredAccess
                           _type.BOOL,  # bInheritHandle
                           _type.LPCWSTR],  # lpName
                          _type.HANDLE]
OpenWaitableTimerW: _Callable[[_type.DWORD,  # dwDesiredAccess
                               _type.BOOL,  # bInheritHandle
                               _type.LPCWSTR],  # lpTimerName
                              _type.HANDLE]
CancelWaitableTimer: _Callable[[_type.HANDLE],  # hTimer
                               _type.BOOL]
CreateMutexExA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpMutexAttributes
                           _Optional[_type.LPCSTR],  # lpName
                           _type.DWORD,  #
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateMutexExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpMutexAttributes
                           _Optional[_type.LPCWSTR],  # lpName
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateEventExA: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpEventAttributes
                           _Optional[_type.LPCSTR],  # lpName
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateEventExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpEventAttributes
                           _Optional[_type.LPCWSTR],  # lpName
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateSemaphoreExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpSemaphoreAttributes
                               _type.LONG,  # lInitialCount
                               _type.LONG,  # lMaximumCount
                               _Optional[_type.LPCWSTR],  # lpName
                               _type.DWORD,  # dwFlags
                               _type.DWORD],  # dwDesiredAccess
                              _type.HANDLE]
CreateWaitableTimerExW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpTimerAttributes
                                   _Optional[_type.LPCWSTR],  # lpTimerName
                                   _type.DWORD,  # dwFlags
                                   _type.DWORD],  # dwDesiredAccess
                                  _type.HANDLE]
Sleep: _Callable[[_type.DWORD],  # dwMilliseconds
                 _type.VOID]
WakeByAddressSingle: _Callable[[_type.PVOID],  # Address
                               _type.VOID]
WakeByAddressAll: _Callable[[_type.PVOID],  # Address
                            _type.VOID]
SignalObjectAndWait: _Callable[[_type.HANDLE,  # hObjectToSignal
                                _type.HANDLE,  # hObjectToWaitOn
                                _type.DWORD,  # dwMilliseconds
                                _type.BOOL],  # bAlertable
                               _type.DWORD]
WaitForMultipleObjects: _Callable[[_type.DWORD,  # nCount
                                   _Pointer[_type.HANDLE],  # lpHandles
                                   _type.BOOL,  # bWaitAll
                                   _type.DWORD],  # dwMilliseconds
                                  _type.DWORD]
CreateSemaphoreW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpSemaphoreAttributes
                             _type.LONG,  # lInitialCount
                             _type.LONG,  # lMaximumCount
                             _Optional[_type.LPCWSTR]],  # lpName
                            _type.HANDLE]
CreateWaitableTimerW: _Callable[[_Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpTimerAttributes
                                 _type.BOOL,  # bManualReset
                                 _Optional[_type.LPCWSTR]],  # lpTimerName
                                _type.HANDLE]
# sysinfoapi
GetSystemTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                         _type.VOID]
GetSystemTimeAsFileTime: _Callable[[_Pointer[_struct.FILETIME]],  # lpSystemTimeAsFileTime
                                   _type.VOID]
GetLocalTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                        _type.VOID]
IsUserCetAvailableInEnvironment: _Callable[[_type.DWORD],  # UserCetEnvironment
                                           _type.BOOL]
GetSystemLeapSecondInformation: _Callable[[_Pointer[_type.BOOL],  # Enabled
                                           _Pointer[_type.DWORD]],  # _type.BOOL
                                          _type.BOOL]
GetVersion: _Callable[[],
                      _type.DWORD]
GetTickCount: _Callable[[],
                        _type.DWORD]
GetTickCount64: _Callable[[],
                          _type.ULONGLONG]
GetSystemTimeAdjustment: _Callable[[_Pointer[_type.DWORD],  # lpTimeAdjustment
                                    _Pointer[_type.DWORD],  # lpTimeIncrement
                                    _Pointer[_type.BOOL]],  # lpTimeAdjustmentDisabled
                                   _type.BOOL]
GetSystemTimeAdjustmentPrecise: _Callable[[_Pointer[_type.DWORD64],  # lpTimeAdjustment
                                           _Pointer[_type.DWORD64],  # lpTimeIncrement
                                           _Pointer[_type.BOOL]],  # lpTimeAdjustmentDisabled
                                          _type.BOOL]
GetSystemDirectoryA: _Callable[[_Optional[_type.LPSTR],  # lpBuffer
                                _type.UINT],  # uSize
                               _type.UINT]
GetSystemDirectoryW: _Callable[[_Optional[_type.LPWSTR],  # lpBuffer
                                _type.UINT],  # uSize
                               _type.UINT]
GetWindowsDirectoryA: _Callable[[_Optional[_type.LPSTR],  # lpBuffer
                                 _type.UINT],  # uSize
                                _type.UINT]
GetWindowsDirectoryW: _Callable[[_Optional[_type.LPWSTR],  # lpBuffer
                                 _type.UINT],  # uSize
                                _type.UINT]
GetSystemWindowsDirectoryA: _Callable[[_Optional[_type.LPSTR],  # lpBuffer
                                       _type.UINT],  # uSize
                                      _type.UINT]
GetSystemWindowsDirectoryW: _Callable[[_Optional[_type.LPWSTR],  # lpBuffer
                                       _type.UINT],  # uSize
                                      _type.UINT]
GetComputerNameExA: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                               _Optional[_type.LPSTR],  # lpBuffer
                               _Pointer[_type.DWORD]],  # nSize
                              _type.BOOL]
GetComputerNameExW: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                               _Optional[_type.LPWSTR],  # lpBuffer
                               _Pointer[_type.DWORD]],  # nSize
                              _type.BOOL]
SetComputerNameExW: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                               _type.LPCWSTR],  # lpBuffer
                              _type.BOOL]
SetSystemTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                         _type.BOOL]
GetVersionExA: _Callable[[_Pointer[_struct.OSVERSIONINFOA]],
                         _type.BOOL]
GetVersionExW: _Callable[[_Pointer[_struct.OSVERSIONINFOW]],
                         _type.BOOL]
GetSystemTimePreciseAsFileTime: _Callable[[_Pointer[_struct.FILETIME]],  # lpSystemTimeAsFileTime
                                          _type.VOID]
GetProductInfo: _Callable[[_type.DWORD,  # dwOSMajorVersion
                           _type.DWORD,  # dwOSMinorVersion
                           _type.DWORD,  # dwSpMajorVersion
                           _type.DWORD,  # dwSpMinorVersion
                           _Pointer[_type.DWORD]],  # pdwReturnedProductType
                          _type.BOOL]
VerSetConditionMask: _Callable[[_type.ULONGLONG,  # ConditionMask
                                _type.ULONG,  # TypeMask
                                _type.UCHAR],  # Condition
                               _type.ULONGLONG]
GetOsSafeBootMode: _Callable[[_Pointer[_type.DWORD]],  # Flags
                             _type.BOOL]
GetPhysicallyInstalledSystemMemory: _Callable[[_Pointer[_type.ULONGLONG]],  # TotalMemoryInKilobytes
                                              _type.BOOL]
SetSystemTimeAdjustment: _Callable[[_type.DWORD,  # dwTimeAdjustment
                                    _type.BOOL],  # bTimeAdjustmentDisabled
                                   _type.BOOL]
SetSystemTimeAdjustmentPrecise: _Callable[[_type.DWORD64,  # dwTimeAdjustment
                                           _type.BOOL],  # bTimeAdjustmentDisabled
                                          _type.BOOL]
InstallELAMCertificateInfo: _Callable[[_type.HANDLE],  # ELAMFile
                                      _type.BOOL]
GetOsManufacturingMode: _Callable[[_Pointer[_type.BOOL]],  # pbEnabled
                                  _type.BOOL]
GetIntegratedDisplaySize: _Callable[[_Pointer[_type.c_double]],  # sizeInInches
                                    _type.HRESULT]
SetComputerNameA: _Callable[[_type.LPCSTR],  # lpComputerName
                            _type.BOOL]
SetComputerNameW: _Callable[[_type.LPCWSTR],  # lpComputerName
                            _type.BOOL]
SetComputerNameExA: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                               _type.LPCSTR],  # lpBuffer
                              _type.BOOL]
# timezoneapi
SystemTimeToTzSpecificLocalTime: _Callable[[_Pointer[_struct.TIME_ZONE_INFORMATION],  # lpTimeZoneInformation
                                            _Pointer[_struct.SYSTEMTIME],  # lpUniversalTime
                                            _Pointer[_struct.SYSTEMTIME]],  # lpLocalTime
                                           _type.BOOL]
TzSpecificLocalTimeToSystemTime: _Callable[[_Pointer[_struct.TIME_ZONE_INFORMATION],  # lpTimeZoneInformation
                                            _Pointer[_struct.SYSTEMTIME],  # lpLocalTime
                                            _Pointer[_struct.SYSTEMTIME]],  # lpUniversalTime
                                           _type.BOOL]
FileTimeToSystemTime: _Callable[[_Pointer[_struct.FILETIME],  # lpFileTime
                                 _Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                                _type.BOOL]
SystemTimeToFileTime: _Callable[[_Pointer[_struct.SYSTEMTIME],  # lpSystemTime
                                 _Pointer[_struct.FILETIME]],  # lpFileTime
                                _type.BOOL]
GetTimeZoneInformation: _Callable[[_Pointer[_struct.TIME_ZONE_INFORMATION]],  # lpTimeZoneInformation
                                  _type.DWORD]
SetTimeZoneInformation: _Callable[[_Pointer[_struct.TIME_ZONE_INFORMATION]],  # lpTimeZoneInformation
                                  _type.BOOL]
SetDynamicTimeZoneInformation: _Callable[[_Pointer[_struct.DYNAMIC_TIME_ZONE_INFORMATION]],  # lpTimeZoneInformation
                                         _type.BOOL]
GetDynamicTimeZoneInformation: _Callable[[_Pointer[_struct.DYNAMIC_TIME_ZONE_INFORMATION]],  # pTimeZoneInformation
                                         _type.DWORD]
GetTimeZoneInformationForYear: _Callable[[_type.USHORT,  # wYear
                                          _Pointer[_struct.DYNAMIC_TIME_ZONE_INFORMATION],  # pdtzi
                                          _Pointer[_struct.TIME_ZONE_INFORMATION]],  # ptzi
                                         _type.BOOL]
EnumDynamicTimeZoneInformation: _Callable[[_type.DWORD,  # dwIndex
                                           _Pointer[_struct.DYNAMIC_TIME_ZONE_INFORMATION]],  # lpTimeZoneInformation
                                          _type.DWORD]
GetDynamicTimeZoneInformationEffectiveYears: _Callable[[_Pointer[_struct.DYNAMIC_TIME_ZONE_INFORMATION],  # lpTimeZoneInformation
                                                        _Pointer[_type.DWORD],  # FirstYear
                                                        _Pointer[_type.DWORD]],  # LastYear
                                                       _type.DWORD]
SystemTimeToTzSpecificLocalTimeEx: _Callable[[_Pointer[_struct.DYNAMIC_TIME_ZONE_INFORMATION],  # lpTimeZoneInformation
                                              _Pointer[_struct.SYSTEMTIME],  # lpUniversalTime
                                              _Pointer[_struct.SYSTEMTIME]],  # lpLocalTime
                                             _type.BOOL]
TzSpecificLocalTimeToSystemTimeEx: _Callable[[_Pointer[_struct.DYNAMIC_TIME_ZONE_INFORMATION],  # lpTimeZoneInformation
                                              _Pointer[_struct.SYSTEMTIME],  # lpLocalTime
                                              _Pointer[_struct.SYSTEMTIME]],  # lpUniversalTime
                                             _type.BOOL]
LocalFileTimeToLocalSystemTime: _Callable[[_Pointer[_struct.TIME_ZONE_INFORMATION],  # timeZoneInformation
                                           _Pointer[_struct.FILETIME],  # localFileTime
                                           _Pointer[_struct.SYSTEMTIME]],  # localSystemTime
                                          _type.BOOL]
LocalSystemTimeToLocalFileTime: _Callable[[_Pointer[_struct.TIME_ZONE_INFORMATION],  # timeZoneInformation
                                           _Pointer[_struct.SYSTEMTIME],  # localSystemTime
                                           _Pointer[_struct.FILETIME]],  # localFileTime
                                          _type.BOOL]
# utilapiset
Beep: _Callable[[_type.DWORD,  # dwFreq
                 _type.DWORD],  # dwDuration
                _type.BOOL]
# WinBase TODO
CreateNamedPipeA: _Callable[[_type.LPCSTR,  # lpName
                             _type.DWORD,  # dwOpenMode
                             _type.DWORD,  # dwPipeMode
                             _type.DWORD,  # nMaxInstances
                             _type.DWORD,  # nOutBufferSize
                             _type.DWORD,  # nInBufferSize
                             _type.DWORD,  # nDefaultTimeOut
                             _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]]],  # lpSecurityAttributes
                            _type.HANDLE]
GetNamedPipeHandleStateA: _Callable[[_type.HANDLE,  # hNamedPipe
                                     _Optional[_Pointer[_type.DWORD]],  # lpState
                                     _Optional[_Pointer[_type.DWORD]],  # lpCurInstances
                                     _Optional[_Pointer[_type.DWORD]],  # lpMaxCollectionCount
                                     _Optional[_Pointer[_type.DWORD]],  # lpCollectDataTimeout
                                     _Optional[_Pointer[_type.LPSTR]],  # lpUserName
                                     _type.DWORD],  # nMaxUserNameSize
                                    _type.BOOL]
CallNamedPipeA: _Callable[[_type.LPCSTR,  # lpNamedPipeName
                           _Optional[_type.LPVOID],  # lpInBuffer
                           _type.DWORD,  # nInBufferSize
                           _Optional[_type.LPVOID],  # lpOutBuffer
                           _type.DWORD,  # nOutBufferSize
                           _Pointer[_type.DWORD],  # lpBytesRead
                           _type.DWORD],  # nTimeOut
                          _type.BOOL]
WaitNamedPipeA: _Callable[[_type.LPCSTR,  # lpNamedPipeName
                           _type.DWORD],  # nTimeOut
                          _type.BOOL]
GetNamedPipeClientComputerNameA: _Callable[[_type.HANDLE,  # Pipe
                                            _type.LPSTR,  # ClientComputerName
                                            _type.ULONG],  # ClientComputerNameLength
                                           _type.BOOL]
GetNamedPipeClientProcessId: _Callable[[_type.HANDLE,  # Pipe
                                        _Pointer[_type.ULONG]],  # ClientProcessId
                                       _type.BOOL]
GetNamedPipeClientSessionId: _Callable[[_type.HANDLE,  # Pipe
                                        _Pointer[_type.ULONG]],  # ClientSessionId
                                       _type.BOOL]
GetNamedPipeServerProcessId: _Callable[[_type.HANDLE,  # Pipe
                                        _Pointer[_type.ULONG]],  # ServerProcessId
                                       _type.BOOL]
GetNamedPipeServerSessionId: _Callable[[_type.HANDLE,  # Pipe
                                        _Pointer[_type.ULONG]],  # ServerSessionId
                                       _type.BOOL]
SetVolumeLabelA: _Callable[[_Optional[_type.LPCSTR],  # lpRootPathName
                            _Optional[_type.LPCSTR]],  # lpVolumeName
                           _type.BOOL]
SetVolumeLabelW: _Callable[[_Optional[_type.LPCWSTR],  # lpRootPathName
                            _Optional[_type.LPCWSTR]],  # lpVolumeName
                           _type.BOOL]
ActivateActCtx: _Callable[[_Optional[_type.HANDLE],
                           _Pointer[_type.ULONG_PTR]],
                          _type.BOOL]
AddAtomA: _Callable[[_Optional[_type.LPCSTR]],
                    _type.ATOM]
AddAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                    _type.ATOM]
AddRefActCtx: _Callable[[_type.HANDLE],
                        _type.VOID]
ApplicationRecoveryFinished: _Callable[[_type.BOOL],
                                       _type.VOID]
ApplicationRecoveryInProgress: _Callable[[_Pointer[_type.BOOL]],
                                         _type.HRESULT]
AssignProcessToJobObject: _Callable[[_type.HANDLE,
                                     _type.HANDLE],
                                    _type.BOOL]
BeginUpdateResourceA: _Callable[[_type.LPCSTR,
                                 _type.BOOL],
                                _type.HANDLE]
BeginUpdateResourceW: _Callable[[_type.LPCWSTR,
                                 _type.BOOL],
                                _type.HANDLE]
CreateActCtxA: _Callable[[_Pointer[_struct.ACTCTXA]],
                         _type.HANDLE]
CreateActCtxW: _Callable[[_Pointer[_struct.ACTCTXW]],
                         _type.HANDLE]
DeactivateActCtx: _Callable[[_type.DWORD,
                             _type.ULONG_PTR],
                            _type.BOOL]
EndUpdateResourceA: _Callable[[_type.HANDLE,
                               _type.BOOL],
                              _type.BOOL]
EndUpdateResourceW: _Callable[[_type.HANDLE,
                               _type.BOOL],
                              _type.BOOL]
FindAtomA: _Callable[[_Optional[_type.LPCSTR]],
                     _type.ATOM]
FindAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                     _type.ATOM]
FormatMessageA: _Callable[[_type.DWORD,
                           _Optional[_type.LPCVOID],
                           _type.DWORD,
                           _type.DWORD,
                           _type.LPSTR,
                           _type.DWORD,
                           _Optional[_Pointer[_type.va_list]]],
                          _type.DWORD]
FormatMessageW: _Callable[[_type.DWORD,
                           _Optional[_type.LPCVOID],
                           _type.DWORD,
                           _type.DWORD,
                           _type.LPWSTR,
                           _type.DWORD,
                           _Optional[_Pointer[_type.va_list]]],
                          _type.DWORD]
GetBinaryTypeA: _Callable[[_type.LPCSTR,
                           _Pointer[_type.DWORD]],
                          _type.BOOL]
GetBinaryTypeW: _Callable[[_type.LPCWSTR,
                           _Pointer[_type.DWORD]],
                          _type.BOOL]
GetCurrentActCtx: _Callable[[_Pointer[_type.HANDLE]],
                            _type.BOOL]
GetProfileIntA: _Callable[[_type.LPCSTR,
                           _type.LPCSTR,
                           _type.INT],
                          _type.UINT]
GetProfileIntW: _Callable[[_type.LPCWSTR,
                           _type.LPCWSTR,
                           _type.INT],
                          _type.UINT]
GetSystemPowerStatus: _Callable[[_Pointer[_struct.SYSTEM_POWER_STATUS]],
                                _type.BOOL]
GlobalAddAtomA: _Callable[[_Optional[_type.LPCSTR]],
                          _type.ATOM]
GlobalAddAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                          _type.ATOM]
GlobalAddAtomExA: _Callable[[_Optional[_type.LPCSTR],
                             _type.DWORD],
                            _type.ATOM]
GlobalAddAtomExW: _Callable[[_Optional[_type.LPCWSTR],
                             _type.DWORD],
                            _type.ATOM]
GlobalAlloc: _Callable[[_type.UINT,
                        _type.SIZE_T],
                       _type.HGLOBAL]
GlobalFindAtomA: _Callable[[_Optional[_type.LPCSTR]],
                           _type.ATOM]
GlobalFindAtomW: _Callable[[_Optional[_type.LPCWSTR]],
                           _type.ATOM]
GlobalLock: _Callable[[_type.HGLOBAL],
                      _type.LPVOID]
GlobalUnlock: _Callable[[_type.HGLOBAL],
                        _type.BOOL]
LocalFree: _Callable[[_type.HLOCAL],
                     _type.HLOCAL]
MoveFileA: _Callable[[_type.LPCSTR,
                      _type.LPCSTR],
                     _type.BOOL]
MoveFileW: _Callable[[_type.LPCWSTR,
                      _type.LPCWSTR],
                     _type.BOOL]
OpenJobObjectA: _Callable[[_type.DWORD,
                           _type.BOOL,
                           _type.LPCSTR],
                          _type.HANDLE]
OpenJobObjectW: _Callable[[_type.DWORD,
                           _type.BOOL,
                           _type.LPCWSTR],
                          _type.HANDLE]
OpenMutexA: _Callable[[_type.DWORD,
                       _type.BOOL,
                       _type.LPCSTR],
                      _type.HANDLE]
QueryActCtxW: _Callable[[_type.DWORD,
                         _type.HANDLE,
                         _Optional[_type.PVOID],
                         _type.ULONG,
                         _Optional[_type.PVOID],
                         _type.SIZE_T,
                         _Optional[_Pointer[_type.SIZE_T]]],
                        _type.BOOL]
QueryActCtxSettingsW: _Callable[[_Optional[_type.DWORD],
                                 _Optional[_type.HANDLE],
                                 _Optional[_type.PCWSTR],
                                 _type.PCWSTR,
                                 _Optional[_type.PWSTR],
                                 _type.SIZE_T,
                                 _Optional[_Pointer[_type.SIZE_T]]],
                                _type.BOOL]
RegisterApplicationRecoveryCallback: _Callable[[_type.APPLICATION_RECOVERY_CALLBACK,
                                                _Optional[_type.PVOID],
                                                _type.DWORD,
                                                _type.DWORD],
                                               _type.HRESULT]
RegisterApplicationRestart: _Callable[[_Optional[_type.PCWSTR],
                                       _type.DWORD],
                                      _type.HRESULT]
ReleaseActCtx: _Callable[[_type.HANDLE],
                         _type.VOID]
SetDllDirectoryA: _Callable[[_Optional[_type.LPCSTR]],
                            _type.BOOL]
SetDllDirectoryW: _Callable[[_Optional[_type.LPCWSTR]],
                            _type.BOOL]
SetSystemPowerState: _Callable[[_type.BOOL,
                                _type.BOOL],
                               _type.BOOL]
TerminateJobObject: _Callable[[_type.HANDLE,
                               _type.UINT],
                              _type.BOOL]
UnregisterApplicationRecoveryCallback: _Callable[[],
                                                 _type.HRESULT]
UnregisterApplicationRestart: _Callable[[],
                                        _type.HRESULT]
UpdateResourceA: _Callable[[_type.HANDLE,
                            _type.LPCSTR,
                            _type.LPCSTR,
                            _type.WORD,
                            _Optional[_type.LPVOID],
                            _type.DWORD],
                           _type.BOOL]
UpdateResourceW: _Callable[[_type.HANDLE,
                            _type.LPCWSTR,
                            _type.LPCWSTR,
                            _type.WORD,
                            _Optional[_type.LPVOID],
                            _type.DWORD],
                           _type.BOOL]
VerifyVersionInfoA: _Callable[[_Pointer[_struct.OSVERSIONINFOEXA],
                               _type.DWORD,
                               _type.DWORDLONG],
                              _type.BOOL]
VerifyVersionInfoW: _Callable[[_Pointer[_struct.OSVERSIONINFOEXW],
                               _type.DWORD,
                               _type.DWORDLONG],
                              _type.BOOL]
WritePrivateProfileSectionA: _Callable[[_Optional[_type.LPCSTR],
                                        _Optional[_type.LPCSTR],
                                        _Optional[_type.LPCSTR]],
                                       _type.BOOL]
WritePrivateProfileSectionW: _Callable[[_Optional[_type.LPCWSTR],
                                        _Optional[_type.LPCWSTR],
                                        _Optional[_type.LPCWSTR]],
                                       _type.BOOL]
WritePrivateProfileStringA: _Callable[[_Optional[_type.LPCSTR],
                                       _Optional[_type.LPCSTR],
                                       _Optional[_type.LPCSTR],
                                       _Optional[_type.LPCSTR]],
                                      _type.BOOL]
WritePrivateProfileStringW: _Callable[[_Optional[_type.LPCWSTR],
                                       _Optional[_type.LPCWSTR],
                                       _Optional[_type.LPCWSTR],
                                       _Optional[_type.LPCWSTR]],
                                      _type.BOOL]
WriteProfileSectionA: _Callable[[_type.LPCSTR,
                                 _type.LPCSTR],
                                _type.BOOL]
WriteProfileSectionW: _Callable[[_type.LPCWSTR,
                                 _type.LPCWSTR],
                                _type.BOOL]
WriteProfileStringA: _Callable[[_Optional[_type.LPCSTR],
                                _Optional[_type.LPCSTR],
                                _Optional[_type.LPCSTR]],
                               _type.BOOL]
WriteProfileStringW: _Callable[[_Optional[_type.LPCWSTR],
                                _Optional[_type.LPCWSTR],
                                _Optional[_type.LPCWSTR]],
                               _type.BOOL]
ZombifyActCtx: _Callable[[_type.HANDLE],
                         _type.BOOL]
# WinNls
GetSystemDefaultUILanguage: _Callable[[],
                                      _type.LANGID]
GetThreadLocale: _Callable[[],
                           _type.LCID]
SetThreadLocale: _Callable[[_type.LCID],  # Locale
                           _type.BOOL]
GetUserDefaultUILanguage: _Callable[[],
                                    _type.LANGID]
GetUserDefaultLangID: _Callable[[],
                                _type.LANGID]
GetSystemDefaultLangID: _Callable[[],
                                  _type.LANGID]
GetSystemDefaultLCID: _Callable[[],
                                _type.LCID]
GetUserDefaultLCID: _Callable[[],
                              _type.LCID]
SetThreadUILanguage: _Callable[[_type.LANGID],  # LangID
                               _type.LANGID]
GetThreadUILanguage: _Callable[[],
                               _type.LCID]
GetUserDefaultLocaleName: _Callable[[_type.LPWSTR,  # lpLocaleName
                                     _type.c_int],  # cchLocaleName
                                    _type.c_int]
GetSystemDefaultLocaleName: _Callable[[_type.LPWSTR,  # lpLocaleName
                                       _type.c_int],  # cchLocaleName
                                      _type.c_int]
# winnt
VerSetConditionMask: _Callable[[_type.ULONGLONG,  # ConditionMask
                                _type.DWORD,  # TypeMask
                                _type.BYTE],  # Condition
                               _type.ULONGLONG]
# wow64apiset
Wow64EnableWow64FsRedirection: _Callable[[_type.BOOLEAN],  # Wow64FsEnableRedirection
                                         _type.BOOLEAN]
Wow64RevertWow64FsRedirection: _Callable[[_type.PVOID],  # OlValue
                                         _type.BOOL]
IsWow64Process: _Callable[[_type.HANDLE,  # hProcess
                           _Pointer[_type.BOOL]],  # Wow64Process
                          _type.BOOL]
GetSystemWow64DirectoryA: _Callable[[_type.LPSTR,  # lpBuffer
                                     _type.UINT],  # uSize
                                    _type.UINT]
GetSystemWow64DirectoryW: _Callable[[_type.LPWSTR,  # lpBuffer
                                     _type.UINT],  # uSize
                                    _type.UINT]
Wow64SetThreadDefaultGuestMachine: _Callable[[_type.USHORT],  # Machine
                                             _type.USHORT]
IsWow64Process2: _Callable[[_type.HANDLE,  # hProcess
                            _Pointer[_type.USHORT],  # pProcessMachine
                            _Optional[_Pointer[_type.USHORT]]],  # pNativeMachine
                           _type.BOOL]
GetSystemWow64Directory2A: _Callable[[_type.LPSTR,  # lpBuffer
                                      _type.UINT,  # uSize
                                      _type.WORD],  # ImageFileMachineType
                                     _type.UINT]
GetSystemWow64Directory2W: _Callable[[_type.LPWSTR,  # lpBuffer
                                      _type.UINT,  # uSize
                                      _type.WORD],  # ImageFileMachineType
                                     _type.UINT]
IsWow64GuestMachineSupported: _Callable[[[_type.USHORT],  # WowGuestMachine
                                         _Pointer[_type.BOOL]],  # MachineIsSupported
                                        _type.HRESULT]
Wow64SuspendThread: _Callable[[_type.HANDLE],  # hThread
                              _type.DWORD]

_WinLib(__name__)
