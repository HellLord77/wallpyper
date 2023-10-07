from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

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
                           _Pointer[_type.DWORD],  # lpErrors
                           _Pointer[_struct.COMSTAT]],  # lpStat
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
                          _Pointer[_type.DWORD]],  # lpdwSize
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
                          _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
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
ReadConsoleInputA: _Callable[[_type.HANDLE,  # hConsoleInput
                              _Pointer[_struct.INPUT_RECORD],  # lpBuffer
                              _type.DWORD,  # nLength
                              _Pointer[_type.DWORD]],  # lpNumberOfEventsRead
                             _type.BOOL]
ReadConsoleInputW: _Callable[[_type.HANDLE,  # hConsoleInput
                              _Pointer[_struct.INPUT_RECORD],  # lpBuffer
                              _type.DWORD,  # nLength
                              _Pointer[_type.DWORD]],  # lpNumberOfEventsRead
                             _type.BOOL]
PeekConsoleInputA: _Callable[[_type.HANDLE,  # hConsoleInput
                              _Pointer[_struct.INPUT_RECORD],  # lpBuffer
                              _type.DWORD,  # nLength
                              _Pointer[_type.DWORD]],  # lpNumberOfEventsRead
                             _type.BOOL]
PeekConsoleInputW: _Callable[[_type.HANDLE,  # hConsoleInput
                              _Pointer[_struct.INPUT_RECORD],  # lpBuffer
                              _type.DWORD,  # nLength
                              _Pointer[_type.DWORD]],  # lpNumberOfEventsRead
                             _type.BOOL]
ReadConsoleA: _Callable[[_type.HANDLE,  # hConsoleInput
                         _type.LPVOID,  # lpBuffer
                         _type.DWORD,  # nNumberOfCharsToRead
                         _Pointer[_type.DWORD],  # lpNumberOfCharsRead
                         _Pointer[_struct.CONSOLE_READCONSOLE_CONTROL]],  # pInputControl
                        _type.BOOL]
ReadConsoleW: _Callable[[_type.HANDLE,  # hConsoleInput
                         _type.LPVOID,  # lpBuffer
                         _type.DWORD,  # nNumberOfCharsToRead
                         _Pointer[_type.DWORD],  # lpNumberOfCharsRead
                         _Pointer[_struct.CONSOLE_READCONSOLE_CONTROL]],  # pInputControl
                        _type.BOOL]
WriteConsoleA: _Callable[[_type.HANDLE,  # hConsoleOutput
                          _type.c_void_p,  # lpBuffer
                          _type.DWORD,  # nNumberOfCharsToWrite
                          _Pointer[_type.DWORD],  # lpNumberOfCharsWritten
                          _type.LPVOID],  # lpReserved
                         _type.BOOL]
WriteConsoleW: _Callable[[_type.HANDLE,  # hConsoleOutput
                          _type.c_void_p,  # lpBuffer
                          _type.DWORD,  # nNumberOfCharsToWrite
                          _Pointer[_type.DWORD],  # lpNumberOfCharsWritten
                          _type.LPVOID],  # lpReserved
                         _type.BOOL]
SetConsoleCtrlHandler: _Callable[[_type.PHANDLER_ROUTINE,  # HandlerRoutine
                                  _type.BOOL],  # Add
                                 _type.BOOL]
CreatePseudoConsole: _Callable[[_struct.COORD,  # size
                                _type.HANDLE,  # hInput
                                _type.HANDLE,  # hOutput
                                _type.DWORD,  # dwFlags
                                _Pointer[_type.HPCON]],  # phPC
                               _type.HRESULT]
ResizePseudoConsole: _Callable[[_type.HPCON,  # hPC
                                _struct.COORD],  # size
                               _type.HRESULT]
ClosePseudoConsole: _Callable[[_type.HPCON],  # hPC
                              _type.c_void]
# consoleapi2
FillConsoleOutputCharacterA: _Callable[[_type.HANDLE,  # hConsoleOutput
                                        _type.CHAR,  # cCharacter
                                        _type.DWORD,  # nLength
                                        _struct.COORD,  # dwWriteCoord
                                        _Pointer[_type.DWORD]],  # lpNumberOfCharsWritten
                                       _type.BOOL]
FillConsoleOutputCharacterW: _Callable[[_type.HANDLE,  # hConsoleOutput
                                        _type.WCHAR,  # cCharacter
                                        _type.DWORD,  # nLength
                                        _struct.COORD,  # dwWriteCoord
                                        _Pointer[_type.DWORD]],  # lpNumberOfCharsWritten
                                       _type.BOOL]
FillConsoleOutputAttribute: _Callable[[_type.HANDLE,  # hConsoleOutput
                                       _type.WORD,  # wAttribute
                                       _type.DWORD,  # nLength
                                       _struct.COORD,  # dwWriteCoord
                                       _Pointer[_type.DWORD]],  # lpNumberOfAttrsWritten
                                      _type.BOOL]
GenerateConsoleCtrlEvent: _Callable[[_type.DWORD,  # dwCtrlEvent
                                     _type.DWORD],  # dwProcessGroupId
                                    _type.BOOL]
CreateConsoleScreenBuffer: _Callable[[_type.DWORD,  # dwDesiredAccess
                                      _type.DWORD,  # dwShareMode
                                      _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSecurityAttributes
                                      _type.DWORD,  # dwFlags
                                      _type.LPVOID],  # lpScreenBufferData
                                     _type.HANDLE]
SetConsoleActiveScreenBuffer: _Callable[[_type.HANDLE],  # hConsoleOutput
                                        _type.BOOL]
FlushConsoleInputBuffer: _Callable[[_type.HANDLE],  # hConsoleInput
                                   _type.BOOL]
SetConsoleCP: _Callable[[_type.UINT],  # wCodePageID
                        _type.BOOL]
SetConsoleOutputCP: _Callable[[_type.UINT],  # wCodePageID
                              _type.BOOL]
GetConsoleCursorInfo: _Callable[[_type.HANDLE,  # hConsoleOutput
                                 _Pointer[_struct.CONSOLE_CURSOR_INFO]],  # lpConsoleCursorInfo
                                _type.BOOL]
SetConsoleCursorInfo: _Callable[[_type.HANDLE,  # hConsoleOutput
                                 _Pointer[_struct.CONSOLE_CURSOR_INFO]],  # lpConsoleCursorInfo
                                _type.BOOL]
GetConsoleScreenBufferInfo: _Callable[[_type.HANDLE,  # hConsoleOutput
                                       _Pointer[_struct.CONSOLE_SCREEN_BUFFER_INFO]],  # lpConsoleScreenBufferInfo
                                      _type.BOOL]
GetConsoleScreenBufferInfoEx: _Callable[[_type.HANDLE,  # hConsoleOutput
                                         _Pointer[_struct.CONSOLE_SCREEN_BUFFER_INFOEX]],  # lpConsoleScreenBufferInfoEx
                                        _type.BOOL]
SetConsoleScreenBufferInfoEx: _Callable[[_type.HANDLE,  # hConsoleOutput
                                         _Pointer[_struct.CONSOLE_SCREEN_BUFFER_INFOEX]],  # lpConsoleScreenBufferInfoEx
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
SetConsoleWindowInfo: _Callable[[_type.HANDLE,  # hConsoleOutput
                                 _type.BOOL,  # bAbsolute
                                 _Pointer[_struct.SMALL_RECT]],  # lpConsoleWindow
                                _type.BOOL]
WriteConsoleOutputCharacterA: _Callable[[_type.HANDLE,  # hConsoleOutput
                                         _type.LPCSTR,  # lpCharacter
                                         _type.DWORD,  # nLength
                                         _struct.COORD,  # dwWriteCoord
                                         _Pointer[_type.DWORD]],  # lpNumberOfCharsWritten
                                        _type.BOOL]
WriteConsoleOutputCharacterW: _Callable[[_type.HANDLE,  # hConsoleOutput
                                         _type.LPCWSTR,  # lpCharacter
                                         _type.DWORD,  # nLength
                                         _struct.COORD,  # dwWriteCoord
                                         _Pointer[_type.DWORD]],  # lpNumberOfCharsWritten
                                        _type.BOOL]
WriteConsoleOutputAttribute: _Callable[[_type.HANDLE,  # hConsoleOutput
                                        _Pointer[_type.WORD],  # lpAttribute
                                        _type.DWORD,  # nLength
                                        _struct.COORD,  # dwWriteCoord
                                        _Pointer[_type.DWORD]],  # lpNumberOfAttrsWritten
                                       _type.BOOL]
ReadConsoleOutputCharacterA: _Callable[[_type.HANDLE,  # hConsoleOutput
                                        _type.LPSTR,  # lpCharacter
                                        _type.DWORD,  # nLength
                                        _struct.COORD,  # dwReadCoord
                                        _Pointer[_type.DWORD]],  # lpNumberOfCharsRead
                                       _type.BOOL]
ReadConsoleOutputCharacterW: _Callable[[_type.HANDLE,  # hConsoleOutput
                                        _type.LPWSTR,  # lpCharacter
                                        _type.DWORD,  # nLength
                                        _struct.COORD,  # dwReadCoord
                                        _Pointer[_type.DWORD]],  # lpNumberOfCharsRead
                                       _type.BOOL]
ReadConsoleOutputAttribute: _Callable[[_type.HANDLE,  # hConsoleOutput
                                       _Pointer[_type.WORD],  # lpAttribute
                                       _type.DWORD,  # nLength
                                       _struct.COORD,  # dwReadCoord
                                       _Pointer[_type.DWORD]],  # lpNumberOfAttrsRead
                                      _type.BOOL]
WriteConsoleInputA: _Callable[[_type.HANDLE,  # hConsoleInput
                               _Pointer[_struct.INPUT_RECORD],  # lpBuffer
                               _type.DWORD,  # nLength
                               _Pointer[_type.DWORD]],  # lpNumberOfEventsWritten
                              _type.BOOL]
WriteConsoleInputW: _Callable[[_type.HANDLE,  # hConsoleInput
                               _Pointer[_struct.INPUT_RECORD],  # lpBuffer
                               _type.DWORD,  # nLength
                               _Pointer[_type.DWORD]],  # lpNumberOfEventsWritten
                              _type.BOOL]
ScrollConsoleScreenBufferA: _Callable[[_type.HANDLE,  # hConsoleOutput
                                       _Pointer[_struct.SMALL_RECT],  # lpScrollRectangle
                                       _Pointer[_struct.SMALL_RECT],  # lpClipRectangle
                                       _struct.COORD,  # dwDestinationOrigin
                                       _Pointer[_struct.CHAR_INFO]],  # lpFill
                                      _type.BOOL]
ScrollConsoleScreenBufferW: _Callable[[_type.HANDLE,  # hConsoleOutput
                                       _Pointer[_struct.SMALL_RECT],  # lpScrollRectangle
                                       _Pointer[_struct.SMALL_RECT],  # lpClipRectangle
                                       _struct.COORD,  # dwDestinationOrigin
                                       _Pointer[_struct.CHAR_INFO]],  # lpFill
                                      _type.BOOL]
WriteConsoleOutputA: _Callable[[_type.HANDLE,  # hConsoleOutput
                                _Pointer[_struct.CHAR_INFO],  # lpBuffer
                                _struct.COORD,  # dwBufferSize
                                _struct.COORD,  # dwBufferCoord
                                _Pointer[_struct.SMALL_RECT]],  # lpWriteRegion
                               _type.BOOL]
WriteConsoleOutputW: _Callable[[_type.HANDLE,  # hConsoleOutput
                                _Pointer[_struct.CHAR_INFO],  # lpBuffer
                                _struct.COORD,  # dwBufferSize
                                _struct.COORD,  # dwBufferCoord
                                _Pointer[_struct.SMALL_RECT]],  # lpWriteRegion
                               _type.BOOL]
ReadConsoleOutputA: _Callable[[_type.HANDLE,  # hConsoleOutput
                               _Pointer[_struct.CHAR_INFO],  # lpBuffer
                               _struct.COORD,  # dwBufferSize
                               _struct.COORD,  # dwBufferCoord
                               _Pointer[_struct.SMALL_RECT]],  # lpReadRegion
                              _type.BOOL]
ReadConsoleOutputW: _Callable[[_type.HANDLE,  # hConsoleOutput
                               _Pointer[_struct.CHAR_INFO],  # lpBuffer
                               _struct.COORD,  # dwBufferSize
                               _struct.COORD,  # dwBufferCoord
                               _Pointer[_struct.SMALL_RECT]],  # lpReadRegion
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
                                    _Pointer[_struct.CONSOLE_FONT_INFOEX]],  # lpConsoleCurrentFontEx
                                   _type.BOOL]
SetCurrentConsoleFontEx: _Callable[[_type.HANDLE,  # hConsoleOutput
                                    _type.BOOL,  # bMaximumWindow
                                    _Pointer[_struct.CONSOLE_FONT_INFOEX]],  # lpConsoleCurrentFontEx
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
                                  _Pointer[_struct.COORD]],  # lpNewScreenBufferDimensions
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
                                         _type.c_void]
ExpungeConsoleCommandHistoryW: _Callable[[_type.LPWSTR],  # ExeName
                                         _type.c_void]
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
RaiseException: _Callable[[_type.DWORD,  # dwExceptionCode
                           _type.DWORD,  # dwExceptionFlags
                           _type.DWORD,  # nNumberOfArguments
                           _Pointer[_type.ULONG_PTR]],  # lpArguments
                          _type.c_void]
UnhandledExceptionFilter: _Callable[[_Pointer[_struct._EXCEPTION_POINTERS]],  # ExceptionInfo
                                    _type.LONG]
SetUnhandledExceptionFilter: _Callable[[_type.LPTOP_LEVEL_EXCEPTION_FILTER],  # lpTopLevelExceptionFilter
                                       _type.LPTOP_LEVEL_EXCEPTION_FILTER]
GetLastError: _Callable[[],
                        _type.DWORD]
SetLastError: _Callable[[_type.DWORD],  # dwErrCode
                        _type.c_void]
GetErrorMode: _Callable[[],
                        _type.UINT]
SetErrorMode: _Callable[[_type.UINT],  # uMode
                        _type.UINT]
AddVectoredExceptionHandler: _Callable[[_type.ULONG,  # First
                                        _type.PVECTORED_EXCEPTION_HANDLER],  # Handler
                                       _type.PVOID]
RemoveVectoredExceptionHandler: _Callable[[_type.PVOID],  # Handle
                                          _type.ULONG]
AddVectoredContinueHandler: _Callable[[_type.ULONG,  # First
                                       _type.PVECTORED_EXCEPTION_HANDLER],  # Handler
                                      _type.PVOID]
RemoveVectoredContinueHandler: _Callable[[_type.PVOID],  # Handle
                                         _type.ULONG]
RaiseFailFastException: _Callable[[_Pointer[_struct.EXCEPTION_RECORD],  # pExceptionRecord
                                   _Pointer[_struct.CONTEXT],  # pContextRecord
                                   _type.DWORD],  # dwFlags
                                  _type.c_void]
FatalAppExitA: _Callable[[_type.UINT,  # uAction
                          _type.LPCSTR],  # lpMessageText
                         _type.c_void]
FatalAppExitW: _Callable[[_type.UINT,  # uAction
                          _type.LPCWSTR],  # lpMessageText
                         _type.c_void]
GetThreadErrorMode: _Callable[[],
                              _type.DWORD]
SetThreadErrorMode: _Callable[[_type.DWORD,  # dwNewMode
                               _Pointer[_type.DWORD]],  # lpOldMode
                              _type.BOOL]
TerminateProcessOnMemoryExhaustion: _Callable[[_type.SIZE_T],  # FailedAllocationSize
                                              _type.c_void]
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
                          _Pointer[_union.LARGE_INTEGER]],  # lpFileSize
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
CloseHandle: _Callable[[_type.HANDLE],  # hObject
                       _type.BOOL]
DuplicateHandle: _Callable[[_type.HANDLE,  # hSourceProcessHandle
                            _type.HANDLE,  # hSourceHandle
                            _type.HANDLE,  # hTargetProcessHandle
                            _Pointer[_type.HANDLE],  # lpTargetHandle
                            _type.DWORD,  # dwDesiredAccess
                            _type.BOOL,  # bInheritHandle
                            _type.DWORD],  # dwOptions
                           _type.BOOL]
CompareObjectHandles: _Callable[[_type.HANDLE,  # hFirstObjectHandle
                                 _type.HANDLE],  # hSecondObjectHandle
                                _type.BOOL]
GetHandleInformation: _Callable[[_type.HANDLE,  # hObject
                                 _Pointer[_type.DWORD]],  # lpdwFlags
                                _type.BOOL]
SetHandleInformation: _Callable[[_type.HANDLE,  # hObject
                                 _type.DWORD,  # dwMask
                                 _type.DWORD],  # dwFlags
                                _type.BOOL]
# heapapi
HeapCreate: _Callable[[_type.DWORD,  # flOptions
                       _type.SIZE_T,  # dwInitialSize
                       _type.SIZE_T],  # dwMaximumSize
                      _type.HANDLE]
HeapDestroy: _Callable[[_type.HANDLE],  # hHeap
                       _type.BOOL]
HeapAlloc: _Callable[[_type.HANDLE,  # hHeap
                      _type.DWORD,  # dwFlags
                      _type.SIZE_T],  # dwBytes
                     _type.LPVOID]
HeapReAlloc: _Callable[[_type.HANDLE,  # hHeap
                        _type.DWORD,  # dwFlags
                        _type.LPVOID,  # lpMem
                        _type.SIZE_T],  # dwBytes
                       _type.LPVOID]
HeapFree: _Callable[[_type.HANDLE,  # hHeap
                     _type.DWORD,  # dwFlags
                     _type.LPVOID],  # lpMem
                    _type.BOOL]
HeapSize: _Callable[[_type.HANDLE,  # hHeap
                     _type.DWORD,  # dwFlags
                     _type.LPCVOID],  # lpMem
                    _type.SIZE_T]
GetProcessHeap: _Callable[[],
                          _type.HANDLE]
HeapCompact: _Callable[[_type.HANDLE,  # hHeap
                        _type.DWORD],  # dwFlags
                       _type.SIZE_T]
HeapSetInformation: _Callable[[_type.HANDLE,  # HeapHandle
                               _enum.HEAP_INFORMATION_CLASS,  # HeapInformationClass
                               _type.PVOID,  # HeapInformation
                               _type.SIZE_T],  # HeapInformationLength
                              _type.BOOL]
HeapValidate: _Callable[[_type.HANDLE,  # hHeap
                         _type.DWORD,  # dwFlags
                         _type.LPCVOID],  # lpMem
                        _type.BOOL]
HeapSummary: _Callable[[_type.HANDLE,  # hHeap
                        _type.DWORD,  # dwFlags
                        _Pointer[_struct.HEAP_SUMMARY]],  # lpSummary
                       _type.BOOL]
GetProcessHeaps: _Callable[[_type.DWORD,  # NumberOfHeaps
                            _Pointer[_type.HANDLE]],  # ProcessHeaps
                           _type.DWORD]
HeapLock: _Callable[[_type.HANDLE],  # hHeap
                    _type.BOOL]
HeapUnlock: _Callable[[_type.HANDLE],  # hHeap
                      _type.BOOL]
HeapWalk: _Callable[[_type.HANDLE,  # hHeap
                     _Pointer[_struct.PROCESS_HEAP_ENTRY]],  # lpEntry
                    _type.BOOL]
HeapQueryInformation: _Callable[[_type.HANDLE,  # HeapHandle
                                 _enum.HEAP_INFORMATION_CLASS,  # HeapInformationClass
                                 _type.PVOID,  # HeapInformation
                                 _type.SIZE_T,  # HeapInformationLength
                                 _Pointer[_type.SIZE_T]],  # ReturnLength
                                _type.BOOL]
# ioapiset
CreateIoCompletionPort: _Callable[[_type.HANDLE,  # FileHandle
                                   _type.HANDLE,  # ExistingCompletionPort
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
                                       _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                                      _type.BOOL]
DeviceIoControl: _Callable[[_type.HANDLE,  # hDevice
                            _type.DWORD,  # dwIoControlCode
                            _type.LPVOID,  # lpInBuffer
                            _type.DWORD,  # nInBufferSize
                            _type.LPVOID,  # lpOutBuffer
                            _type.DWORD,  # nOutBufferSize
                            _Pointer[_type.DWORD],  # lpBytesReturned
                            _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                           _type.BOOL]
GetOverlappedResult: _Callable[[_type.HANDLE,  # hFile
                                _Pointer[_struct.OVERLAPPED],  # lpOverlapped
                                _Pointer[_type.DWORD],  # lpNumberOfBytesTransferred
                                _type.BOOL],  # bWait
                               _type.BOOL]
CancelIoEx: _Callable[[_type.HANDLE,  # hFile
                       _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                      _type.BOOL]
CancelIo: _Callable[[_type.HANDLE],  # hFile
                    _type.BOOL]
GetOverlappedResultEx: _Callable[[_type.HANDLE,  # hFile
                                  _Pointer[_struct.OVERLAPPED],  # lpOverlapped
                                  _Pointer[_type.DWORD],  # lpNumberOfBytesTransferred
                                  _type.DWORD,  # dwMilliseconds
                                  _type.BOOL],  # bAlertable
                                 _type.BOOL]
CancelSynchronousIo: _Callable[[_type.HANDLE],  # hThread
                               _type.BOOL]
# libloaderapi
DisableThreadLibraryCalls: _Callable[[_type.HMODULE],  # hLibModule
                                     _type.BOOL]
FindResourceExW: _Callable[[_type.HMODULE,  # hModule
                            _type.LPCWSTR,  # lpType
                            _type.LPCWSTR,  # lpName
                            _type.WORD],  # wLanguage
                           _type.HRSRC]
FindStringOrdinal: _Callable[[_type.DWORD,  # dwFindStringOrdinalFlags
                              _type.LPCWSTR,  # lpStringSource
                              _type.c_int,  # cchSource
                              _type.LPCWSTR,  # lpStringValue
                              _type.c_int,  # cchValue
                              _type.BOOL],  # bIgnoreCase
                             _type.c_int]
FreeLibrary: _Callable[[_type.HMODULE],  # hLibModule
                       _type.BOOL]
FreeLibraryAndExitThread: _Callable[[_type.HMODULE,  # hLibModule
                                     _type.DWORD],  # dwExitCode
                                    _type.c_void]
FreeResource: _Callable[[_type.HGLOBAL],  # hResData
                        _type.BOOL]
GetModuleFileNameA: _Callable[[_type.HMODULE,  # hModule
                               _type.LPSTR,  # lpFilename
                               _type.DWORD],  # nSize
                              _type.DWORD]
GetModuleFileNameW: _Callable[[_type.HMODULE,  # hModule
                               _type.LPWSTR,  # lpFilename
                               _type.DWORD],  # nSize
                              _type.DWORD]
GetModuleHandleA: _Callable[[_type.LPCSTR],  # lpModuleName
                            _type.HMODULE]
GetModuleHandleW: _Callable[[_type.LPCWSTR],  # lpModuleName
                            _type.HMODULE]
GetModuleHandleExA: _Callable[[_type.DWORD,  # dwFlags
                               _type.LPCSTR,  # lpModuleName
                               _Pointer[_type.HMODULE]],  # phModule
                              _type.BOOL]
GetModuleHandleExW: _Callable[[_type.DWORD,  # dwFlags
                               _type.LPCWSTR,  # lpModuleName
                               _Pointer[_type.HMODULE]],  # phModule
                              _type.BOOL]
GetProcAddress: _Callable[[_type.HMODULE,  # hModule
                           _type.LPCSTR],  # lpProcName
                          _type.FARPROC]
LoadLibraryExA: _Callable[[_type.LPCSTR,  # lpLibFileName
                           _type.HANDLE,  # hFile
                           _type.DWORD],  # dwFlags
                          _type.HMODULE]
LoadLibraryExW: _Callable[[_type.LPCWSTR,  # lpLibFileName
                           _type.HANDLE,  # hFile
                           _type.DWORD],  # dwFlags
                          _type.HMODULE]
LoadResource: _Callable[[_type.HMODULE,  # hModule
                         _type.HRSRC],  # hResInfo
                        _type.HGLOBAL]
LoadStringA: _Callable[[_type.HINSTANCE,  # hInstance
                        _type.UINT,  # uID
                        _type.LPSTR,  # lpBuffer
                        _type.c_int],  # cchBufferMax
                       _type.c_int]
LoadStringW: _Callable[[_type.HINSTANCE,  # hInstance
                        _type.UINT,  # uID
                        _type.LPWSTR,  # lpBuffer
                        _type.c_int],  # cchBufferMax
                       _type.c_int]
LockResource: _Callable[[_type.HGLOBAL],  # hResData
                        _type.LPVOID]
SizeofResource: _Callable[[_type.HMODULE,  # hModule
                           _type.HRSRC],  # hResInfo
                          _type.DWORD]
AddDllDirectory: _Callable[[_type.PCWSTR],  # NewDirectory
                           _type.DLL_DIRECTORY_COOKIE]
RemoveDllDirectory: _Callable[[_type.DLL_DIRECTORY_COOKIE],  # Cookie
                              _type.BOOL]
SetDefaultDllDirectories: _Callable[[_type.DWORD],  # DirectoryFlags
                                    _type.BOOL]
EnumResourceLanguagesExA: _Callable[[_type.HMODULE,  # hModule
                                     _type.LPCSTR,  # lpType
                                     _type.LPCSTR,  # lpName
                                     _type.ENUMRESLANGPROCA,  # lpEnumFunc
                                     _type.LONG_PTR,  # lParam
                                     _type.DWORD,  # dwFlags
                                     _type.LANGID],  # LangId
                                    _type.BOOL]
EnumResourceLanguagesExW: _Callable[[_type.HMODULE,  # hModule
                                     _type.LPCWSTR,  # lpType
                                     _type.LPCWSTR,  # lpName
                                     _type.ENUMRESLANGPROCW,  # lpEnumFunc
                                     _type.LONG_PTR,  # lParam
                                     _type.DWORD,  # dwFlags
                                     _type.LANGID],  # LangId
                                    _type.BOOL]
EnumResourceNamesExA: _Callable[[_type.HMODULE,  # hModule
                                 _type.LPCSTR,  # lpType
                                 _type.ENUMRESNAMEPROCA,  # lpEnumFunc
                                 _type.LONG_PTR,  # lParam
                                 _type.DWORD,  # dwFlags
                                 _type.LANGID],  # LangId
                                _type.BOOL]
EnumResourceNamesExW: _Callable[[_type.HMODULE,  # hModule
                                 _type.LPCWSTR,  # lpType
                                 _type.ENUMRESNAMEPROCW,  # lpEnumFunc
                                 _type.LONG_PTR,  # lParam
                                 _type.DWORD,  # dwFlags
                                 _type.LANGID],  # LangId
                                _type.BOOL]
EnumResourceTypesExA: _Callable[[_type.HMODULE,  # hModule
                                 _type.ENUMRESTYPEPROCA,  # lpEnumFunc
                                 _type.LONG_PTR,  # lParam
                                 _type.DWORD,  # dwFlags
                                 _type.LANGID],  # LangId
                                _type.BOOL]
EnumResourceTypesExW: _Callable[[_type.HMODULE,  # hModule
                                 _type.ENUMRESTYPEPROCW,  # lpEnumFunc
                                 _type.LONG_PTR,  # lParam
                                 _type.DWORD,  # dwFlags
                                 _type.LANGID],  # LangId
                                _type.BOOL]
FindResourceW: _Callable[[_type.HMODULE,  # hModule
                          _type.LPCWSTR,  # lpName
                          _type.LPCWSTR],  # lpType
                         _type.HRSRC]
LoadLibraryA: _Callable[[_type.LPCSTR],  # lpLibFileName
                        _type.HMODULE]
LoadLibraryW: _Callable[[_type.LPCWSTR],  # lpLibFileName
                        _type.HMODULE]
EnumResourceNamesW: _Callable[[_type.HMODULE,  # hModule
                               _type.LPCWSTR,  # lpType
                               _type.ENUMRESNAMEPROCW,  # lpEnumFunc
                               _type.LONG_PTR],  # lParam
                              _type.BOOL]
EnumResourceNamesA: _Callable[[_type.HMODULE,  # hModule
                               _type.LPCSTR,  # lpType
                               _type.ENUMRESNAMEPROCA,  # lpEnumFunc
                               _type.LONG_PTR],  # lParam
                              _type.BOOL]
# memoryapi
VirtualAlloc: _Callable[[_type.LPVOID,  # lpAddress
                         _type.SIZE_T,  # dwSize
                         _type.DWORD,  # flAllocationType
                         _type.DWORD],  # flProtect
                        _type.LPVOID]
VirtualProtect: _Callable[[_type.LPVOID,  # lpAddress
                           _type.SIZE_T,  # dwSize
                           _type.DWORD,  # flNewProtect
                           _Pointer[_type.DWORD]],  # lpflOldProtect
                          _type.BOOL]
VirtualFree: _Callable[[_type.LPVOID,  # lpAddress
                        _type.SIZE_T,  # dwSize
                        _type.DWORD],  # dwFreeType
                       _type.BOOL]
VirtualQuery: _Callable[[_type.LPCVOID,  # lpAddress
                         _Pointer[_struct.MEMORY_BASIC_INFORMATION],  # lpBuffer
                         _type.SIZE_T],  # dwLength
                        _type.SIZE_T]
VirtualAllocEx: _Callable[[_type.HANDLE,  # hProcess
                           _type.LPVOID,  # lpAddress
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
VirtualQueryEx: _Callable[[_type.HANDLE,  # hProcess
                           _type.LPCVOID,  # lpAddress
                           _Pointer[_struct.MEMORY_BASIC_INFORMATION],  # lpBuffer
                           _type.SIZE_T],  # dwLength
                          _type.SIZE_T]
ReadProcessMemory: _Callable[[_type.HANDLE,  # hProcess
                              _type.LPCVOID,  # lpBaseAddress
                              _type.LPVOID,  # lpBuffer
                              _type.SIZE_T,  # nSize
                              _Pointer[_type.SIZE_T]],  # lpNumberOfBytesRead
                             _type.BOOL]
WriteProcessMemory: _Callable[[_type.HANDLE,  # hProcess
                               _type.LPVOID,  # lpBaseAddress
                               _type.LPCVOID,  # lpBuffer
                               _type.SIZE_T,  # nSize
                               _Pointer[_type.SIZE_T]],  # lpNumberOfBytesWritten
                              _type.BOOL]
CreateFileMappingW: _Callable[[_type.HANDLE,  # hFile
                               _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpFileMappingAttributes
                               _type.DWORD,  # flProtect
                               _type.DWORD,  # dwMaximumSizeHigh
                               _type.DWORD,  # dwMaximumSizeLow
                               _type.LPCWSTR],  # lpName
                              _type.HANDLE]
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
                            _type.LPVOID],  # lpBaseAddress
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
GetProcessWorkingSetSize: _Callable[[_type.HANDLE,  # hProcess
                                     _Pointer[_type.SIZE_T],  # lpMinimumWorkingSetSize
                                     _Pointer[_type.SIZE_T]],  # lpMaximumWorkingSetSize
                                    _type.BOOL]
GetProcessWorkingSetSizeEx: _Callable[[_type.HANDLE,  # hProcess
                                       _Pointer[_type.SIZE_T],  # lpMinimumWorkingSetSize
                                       _Pointer[_type.SIZE_T],  # lpMaximumWorkingSetSize
                                       _Pointer[_type.DWORD]],  # Flags
                                      _type.BOOL]
SetProcessWorkingSetSize: _Callable[[_type.HANDLE,  # hProcess
                                     _type.SIZE_T,  # dwMinimumWorkingSetSize
                                     _type.SIZE_T],  # dwMaximumWorkingSetSize
                                    _type.BOOL]
SetProcessWorkingSetSizeEx: _Callable[[_type.HANDLE,  # hProcess
                                       _type.SIZE_T,  # dwMinimumWorkingSetSize
                                       _type.SIZE_T,  # dwMaximumWorkingSetSize
                                       _type.DWORD],  # Flags
                                      _type.BOOL]
VirtualLock: _Callable[[_type.LPVOID,  # lpAddress
                        _type.SIZE_T],  # dwSize
                       _type.BOOL]
VirtualUnlock: _Callable[[_type.LPVOID,  # lpAddress
                          _type.SIZE_T],  # dwSize
                         _type.BOOL]
GetWriteWatch: _Callable[[_type.DWORD,  # dwFlags
                          _type.PVOID,  # lpBaseAddress
                          _type.SIZE_T,  # dwRegionSize
                          _Pointer[_type.PVOID],  # lpAddresses
                          _Pointer[_type.ULONG_PTR],  # lpdwCount
                          _Pointer[_type.DWORD]],  # lpdwGranularity
                         _type.UINT]
ResetWriteWatch: _Callable[[_type.LPVOID,  # lpBaseAddress
                            _type.SIZE_T],  # dwRegionSize
                           _type.UINT]
CreateMemoryResourceNotification: _Callable[[_enum.MEMORY_RESOURCE_NOTIFICATION_TYPE],  # NotificationType
                                            _type.HANDLE]
QueryMemoryResourceNotification: _Callable[[_type.HANDLE,  # ResourceNotificationHandle
                                            _Pointer[_type.BOOL]],  # ResourceState
                                           _type.BOOL]
GetSystemFileCacheSize: _Callable[[_Pointer[_type.SIZE_T],  # lpMinimumFileCacheSize
                                   _Pointer[_type.SIZE_T],  # lpMaximumFileCacheSize
                                   _Pointer[_type.DWORD]],  # lpFlags
                                  _type.BOOL]
SetSystemFileCacheSize: _Callable[[_type.SIZE_T,  # MinimumFileCacheSize
                                   _type.SIZE_T,  # MaximumFileCacheSize
                                   _type.DWORD],  # Flags
                                  _type.BOOL]
CreateFileMappingNumaW: _Callable[[_type.HANDLE,  # hFile
                                   _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpFileMappingAttributes
                                   _type.DWORD,  # flProtect
                                   _type.DWORD,  # dwMaximumSizeHigh
                                   _type.DWORD,  # dwMaximumSizeLow
                                   _type.LPCWSTR,  # lpName
                                   _type.DWORD],  # nndPreferred
                                  _type.HANDLE]
PrefetchVirtualMemory: _Callable[[_type.HANDLE,  # hProcess
                                  _type.ULONG_PTR,  # NumberOfEntries
                                  _Pointer[_struct.WIN32_MEMORY_RANGE_ENTRY],  # VirtualAddresses
                                  _type.ULONG],  # Flags
                                 _type.BOOL]
CreateFileMappingFromApp: _Callable[[_type.HANDLE,  # hFile
                                     _Pointer[_struct.SECURITY_ATTRIBUTES],  # SecurityAttributes
                                     _type.ULONG,  # PageProtection
                                     _type.ULONG64,  # MaximumSize
                                     _type.PCWSTR],  # Name
                                    _type.HANDLE]
MapViewOfFileFromApp: _Callable[[_type.HANDLE,  # hFileMappingObject
                                 _type.ULONG,  # DesiredAccess
                                 _type.ULONG64,  # FileOffset
                                 _type.SIZE_T],  # NumberOfBytesToMap
                                _type.PVOID]
UnmapViewOfFileEx: _Callable[[_type.PVOID,  # BaseAddress
                              _type.ULONG],  # UnmapFlags
                             _type.BOOL]
AllocateUserPhysicalPages: _Callable[[_type.HANDLE,  # hProcess
                                      _Pointer[_type.ULONG_PTR],  # NumberOfPages
                                      _Pointer[_type.ULONG_PTR]],  # PageArray
                                     _type.BOOL]
FreeUserPhysicalPages: _Callable[[_type.HANDLE,  # hProcess
                                  _Pointer[_type.ULONG_PTR],  # NumberOfPages
                                  _Pointer[_type.ULONG_PTR]],  # PageArray
                                 _type.BOOL]
MapUserPhysicalPages: _Callable[[_type.PVOID,  # VirtualAddress
                                 _type.ULONG_PTR,  # NumberOfPages
                                 _Pointer[_type.ULONG_PTR]],  # PageArray
                                _type.BOOL]
AllocateUserPhysicalPagesNuma: _Callable[[_type.HANDLE,  # hProcess
                                          _Pointer[_type.ULONG_PTR],  # NumberOfPages
                                          _Pointer[_type.ULONG_PTR],  # PageArray
                                          _type.DWORD],  # nndPreferred
                                         _type.BOOL]
VirtualAllocExNuma: _Callable[[_type.HANDLE,  # hProcess
                               _type.LPVOID,  # lpAddress
                               _type.SIZE_T,  # dwSize
                               _type.DWORD,  # flAllocationType
                               _type.DWORD,  # flProtect
                               _type.DWORD],  # nndPreferred
                              _type.LPVOID]
GetMemoryErrorHandlingCapabilities: _Callable[[_Pointer[_type.ULONG]],  # Capabilities
                                              _type.BOOL]
RegisterBadMemoryNotification: _Callable[[_type.PBAD_MEMORY_CALLBACK_ROUTINE],  # Callback
                                         _type.PVOID]
UnregisterBadMemoryNotification: _Callable[[_type.PVOID],  # RegistrationHandle
                                           _type.BOOL]
OfferVirtualMemory: _Callable[[_type.PVOID,  # VirtualAddress
                               _type.SIZE_T,  # Size
                               _enum.OFFER_PRIORITY],  # Priority
                              _type.DWORD]
ReclaimVirtualMemory: _Callable[[_type.c_void_p,  # VirtualAddress
                                 _type.SIZE_T],  # Size
                                _type.DWORD]
DiscardVirtualMemory: _Callable[[_type.PVOID,  # VirtualAddress
                                 _type.SIZE_T],  # Size
                                _type.DWORD]
SetProcessValidCallTargets: _Callable[[_type.HANDLE,  # hProcess
                                       _type.PVOID,  # VirtualAddress
                                       _type.SIZE_T,  # RegionSize
                                       _type.ULONG,  # NumberOfOffsets
                                       _Pointer[_struct.CFG_CALL_TARGET_INFO]],  # OffsetInformation
                                      _type.BOOL]
SetProcessValidCallTargetsForMappedView: _Callable[[_type.HANDLE,  # Process
                                                    _type.PVOID,  # VirtualAddress
                                                    _type.SIZE_T,  # RegionSize
                                                    _type.ULONG,  # NumberOfOffsets
                                                    _Pointer[_struct.CFG_CALL_TARGET_INFO],  # OffsetInformation
                                                    _type.HANDLE,  # Section
                                                    _type.ULONG64],  # ExpectedFileOffset
                                                   _type.BOOL]
VirtualAllocFromApp: _Callable[[_type.PVOID,  # BaseAddress
                                _type.SIZE_T,  # Size
                                _type.ULONG,  # AllocationType
                                _type.ULONG],  # Protection
                               _type.PVOID]
VirtualProtectFromApp: _Callable[[_type.PVOID,  # Address
                                  _type.SIZE_T,  # Size
                                  _type.ULONG,  # NewProtection
                                  _Pointer[_type.ULONG]],  # OldProtection
                                 _type.BOOL]
OpenFileMappingFromApp: _Callable[[_type.ULONG,  # DesiredAccess
                                   _type.BOOL,  # InheritHandle
                                   _type.PCWSTR],  # Name
                                  _type.HANDLE]
QueryVirtualMemoryInformation: _Callable[[_type.HANDLE,  # Process
                                          _type.c_void_p,  # VirtualAddress
                                          _enum.WIN32_MEMORY_INFORMATION_CLASS,  # MemoryInformationClass
                                          _type.PVOID,  # MemoryInformation
                                          _type.SIZE_T,  # MemoryInformationSize
                                          _Pointer[_type.SIZE_T]],  # ReturnSize
                                         _type.BOOL]
MapViewOfFileNuma2: _Callable[[_type.HANDLE,  # FileMappingHandle
                               _type.HANDLE,  # ProcessHandle
                               _type.ULONG64,  # Offset
                               _type.PVOID,  # BaseAddress
                               _type.SIZE_T,  # ViewSize
                               _type.ULONG,  # AllocationType
                               _type.ULONG,  # PageProtection
                               _type.ULONG],  # PreferredNode
                              _type.PVOID]
MapViewOfFile2: _Callable[[_type.HANDLE,  # FileMappingHandle
                           _type.HANDLE,  # ProcessHandle
                           _type.ULONG64,  # Offset
                           _type.PVOID,  # BaseAddress
                           _type.SIZE_T,  # ViewSize
                           _type.ULONG,  # AllocationType
                           _type.ULONG],  # PageProtection
                          _type.PVOID]
UnmapViewOfFile2: _Callable[[_type.HANDLE,  # Process
                             _type.PVOID,  # BaseAddress
                             _type.ULONG],  # UnmapFlags
                            _type.BOOL]
VirtualUnlockEx: _Callable[[_type.HANDLE,  # Process
                            _type.LPVOID,  # Address
                            _type.SIZE_T],  # Size
                           _type.BOOL]
VirtualAlloc2: _Callable[[_type.HANDLE,  # Process
                          _type.PVOID,  # BaseAddress
                          _type.SIZE_T,  # Size
                          _type.ULONG,  # AllocationType
                          _type.ULONG,  # PageProtection
                          _Pointer[_struct.MEM_EXTENDED_PARAMETER],  # ExtendedParameters
                          _type.ULONG],  # ParameterCount
                         _type.PVOID]
MapViewOfFile3: _Callable[[_type.HANDLE,  # FileMapping
                           _type.HANDLE,  # Process
                           _type.PVOID,  # BaseAddress
                           _type.ULONG64,  # Offset
                           _type.SIZE_T,  # ViewSize
                           _type.ULONG,  # AllocationType
                           _type.ULONG,  # PageProtection
                           _Pointer[_struct.MEM_EXTENDED_PARAMETER],  # ExtendedParameters
                           _type.ULONG],  # ParameterCount
                          _type.PVOID]
VirtualAlloc2FromApp: _Callable[[_type.HANDLE,  # Process
                                 _type.PVOID,  # BaseAddress
                                 _type.SIZE_T,  # Size
                                 _type.ULONG,  # AllocationType
                                 _type.ULONG,  # PageProtection
                                 _Pointer[_struct.MEM_EXTENDED_PARAMETER],  # ExtendedParameters
                                 _type.ULONG],  # ParameterCount
                                _type.PVOID]
MapViewOfFile3FromApp: _Callable[[_type.HANDLE,  # FileMapping
                                  _type.HANDLE,  # Process
                                  _type.PVOID,  # BaseAddress
                                  _type.ULONG64,  # Offset
                                  _type.SIZE_T,  # ViewSize
                                  _type.ULONG,  # AllocationType
                                  _type.ULONG,  # PageProtection
                                  _Pointer[_struct.MEM_EXTENDED_PARAMETER],  # ExtendedParameters
                                  _type.ULONG],  # ParameterCount
                                 _type.PVOID]
CreateFileMapping2: _Callable[[_type.HANDLE,  # File
                               _Pointer[_struct.SECURITY_ATTRIBUTES],  # SecurityAttributes
                               _type.ULONG,  # DesiredAccess
                               _type.ULONG,  # PageProtection
                               _type.ULONG,  # AllocationAttributes
                               _type.ULONG64,  # MaximumSize
                               _type.PCWSTR,  # Name
                               _Pointer[_struct.MEM_EXTENDED_PARAMETER],  # ExtendedParameters
                               _type.ULONG],  # ParameterCount
                              _type.HANDLE]
AllocateUserPhysicalPages2: _Callable[[_type.HANDLE,  # ObjectHandle
                                       _Pointer[_type.ULONG_PTR],  # NumberOfPages
                                       _Pointer[_type.ULONG_PTR],  # PageArray
                                       _Pointer[_struct.MEM_EXTENDED_PARAMETER],  # ExtendedParameters
                                       _type.ULONG],  # ExtendedParameterCount
                                      _type.BOOL]
OpenDedicatedMemoryPartition: _Callable[[_type.HANDLE,  # Partition
                                         _type.ULONG64,  # DedicatedMemoryTypeId
                                         _type.ACCESS_MASK,  # DesiredAccess
                                         _type.BOOL],  # InheritHandle
                                        _type.HANDLE]
QueryPartitionInformation: _Callable[[_type.HANDLE,  # Partition
                                      _enum.WIN32_MEMORY_PARTITION_INFORMATION_CLASS,  # PartitionInformationClass
                                      _type.PVOID,  # PartitionInformation
                                      _type.ULONG],  # PartitionInformationLength
                                     _type.BOOL]
# namedpipeapi
CreatePipe: _Callable[[_Pointer[_type.HANDLE],  # hReadPipe
                       _Pointer[_type.HANDLE],  # hWritePipe
                       _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpPipeAttributes
                       _type.DWORD],  # nSize
                      _type.BOOL]
ConnectNamedPipe: _Callable[[_type.HANDLE,  # hNamedPipe
                             _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                            _type.BOOL]
DisconnectNamedPipe: _Callable[[_type.HANDLE],  # hNamedPipe
                               _type.BOOL]
SetNamedPipeHandleState: _Callable[[_type.HANDLE,  # hNamedPipe
                                    _Pointer[_type.DWORD],  # lpMode
                                    _Pointer[_type.DWORD],  # lpMaxCollectionCount
                                    _Pointer[_type.DWORD]],  # lpCollectDataTimeout
                                   _type.BOOL]
PeekNamedPipe: _Callable[[_type.HANDLE,  # hNamedPipe
                          _type.LPVOID,  # lpBuffer
                          _type.DWORD,  # nBufferSize
                          _Pointer[_type.DWORD],  # lpBytesRead
                          _Pointer[_type.DWORD],  # lpTotalBytesAvail
                          _Pointer[_type.DWORD]],  # lpBytesLeftThisMessage
                         _type.BOOL]
TransactNamedPipe: _Callable[[_type.HANDLE,  # hNamedPipe
                              _type.LPVOID,  # lpInBuffer
                              _type.DWORD,  # nInBufferSize
                              _type.LPVOID,  # lpOutBuffer
                              _type.DWORD,  # nOutBufferSize
                              _Pointer[_type.DWORD],  # lpBytesRead
                              _Pointer[_struct.OVERLAPPED]],  # lpOverlapped
                             _type.BOOL]
CreateNamedPipeW: _Callable[[_type.LPCWSTR,  # lpName
                             _type.DWORD,  # dwOpenMode
                             _type.DWORD,  # dwPipeMode
                             _type.DWORD,  # nMaxInstances
                             _type.DWORD,  # nOutBufferSize
                             _type.DWORD,  # nInBufferSize
                             _type.DWORD,  # nDefaultTimeOut
                             _Pointer[_struct.SECURITY_ATTRIBUTES]],  # lpSecurityAttributes
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
                             _Pointer[_type.DWORD],  # lpFlags
                             _Pointer[_type.DWORD],  # lpOutBufferSize
                             _Pointer[_type.DWORD],  # lpInBufferSize
                             _Pointer[_type.DWORD]],  # lpMaxInstances
                            _type.BOOL]
GetNamedPipeHandleStateW: _Callable[[_type.HANDLE,  # hNamedPipe
                                     _Pointer[_type.DWORD],  # lpState
                                     _Pointer[_type.DWORD],  # lpCurInstances
                                     _Pointer[_type.DWORD],  # lpMaxCollectionCount
                                     _Pointer[_type.DWORD],  # lpCollectDataTimeout
                                     _type.LPWSTR,  # lpUserName
                                     _type.DWORD],  # nMaxUserNameSize
                                    _type.BOOL]
CallNamedPipeW: _Callable[[_type.LPCWSTR,  # lpNamedPipeName
                           _type.LPVOID,  # lpInBuffer
                           _type.DWORD,  # nInBufferSize
                           _type.LPVOID,  # lpOutBuffer
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
                           _Pointer[_type.HANDLE]],  # phPrevValue
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
GetEnvironmentVariableA: _Callable[[_type.LPCSTR,  # lpName
                                    _type.LPSTR,  # lpBuffer
                                    _type.DWORD],  # nSize
                                   _type.DWORD]
GetEnvironmentVariableW: _Callable[[_type.LPCWSTR,  # lpName
                                    _type.LPWSTR,  # lpBuffer
                                    _type.DWORD],  # nSize
                                   _type.DWORD]
SetEnvironmentVariableA: _Callable[[_type.LPCSTR,  # lpName
                                    _type.LPCSTR],  # lpValue
                                   _type.BOOL]
SetEnvironmentVariableW: _Callable[[_type.LPCWSTR,  # lpName
                                    _type.LPCWSTR],  # lpValue
                                   _type.BOOL]
ExpandEnvironmentStringsA: _Callable[[_type.LPCSTR,  # lpSrc
                                      _type.LPSTR,  # lpDst
                                      _type.DWORD],  # nSize
                                     _type.DWORD]
ExpandEnvironmentStringsW: _Callable[[_type.LPCWSTR,  # lpSrc
                                      _type.LPWSTR,  # lpDst
                                      _type.DWORD],  # nSize
                                     _type.DWORD]
SetCurrentDirectoryA: _Callable[[_type.LPCSTR],  # lpPathName
                                _type.BOOL]
SetCurrentDirectoryW: _Callable[[_type.LPCWSTR],  # lpPathName
                                _type.BOOL]
GetCurrentDirectoryA: _Callable[[_type.DWORD,  # nBufferLength
                                 _type.LPSTR],  # lpBuffer
                                _type.DWORD]
GetCurrentDirectoryW: _Callable[[_type.DWORD,  # nBufferLength
                                 _type.LPWSTR],  # lpBuffer
                                _type.DWORD]
SearchPathW: _Callable[[_type.LPCWSTR,  # lpPath
                        _type.LPCWSTR,  # lpFileName
                        _type.LPCWSTR,  # lpExtension
                        _type.DWORD,  # nBufferLength
                        _type.LPWSTR,  # lpBuffer
                        _Pointer[_type.LPWSTR]],  # lpFilePart
                       _type.DWORD]
SearchPathA: _Callable[[_type.LPCSTR,  # lpPath
                        _type.LPCSTR,  # lpFileName
                        _type.LPCSTR,  # lpExtension
                        _type.DWORD,  # nBufferLength
                        _type.LPSTR,  # lpBuffer
                        _Pointer[_type.LPSTR]],  # lpFilePart
                       _type.DWORD]
NeedCurrentDirectoryForExePathA: _Callable[[_type.LPCSTR],  # ExeName
                                           _type.BOOL]
NeedCurrentDirectoryForExePathW: _Callable[[_type.LPCWSTR],  # ExeName
                                           _type.BOOL]
# processthreadsapi
QueueUserAPC: _Callable[[_type.PAPCFUNC,  # pfnAPC
                         _type.HANDLE,  # hThread
                         _type.ULONG_PTR],  # dwData
                        _type.DWORD]
QueueUserAPC2: _Callable[[_type.PAPCFUNC,  # ApcRoutine
                          _type.HANDLE,  # Thread
                          _type.ULONG_PTR,  # Data
                          _enum.QUEUE_USER_APC_FLAGS],  # Flags
                         _type.BOOL]
GetProcessTimes: _Callable[[_type.HANDLE,  # hProcess
                            _Pointer[_struct.FILETIME],  # lpCreationTime
                            _Pointer[_struct.FILETIME],  # lpExitTime
                            _Pointer[_struct.FILETIME],  # lpKernelTime
                            _Pointer[_struct.FILETIME]],  # lpUserTime
                           _type.BOOL]
GetCurrentProcess: _Callable[[],
                             _type.HANDLE]
GetCurrentProcessId: _Callable[[],
                               _type.DWORD]
ExitProcess: _Callable[[_type.UINT],  # uExitCode
                       _type.c_void]
TerminateProcess: _Callable[[_type.HANDLE,  # hProcess
                             _type.UINT],  # uExitCode
                            _type.BOOL]
GetExitCodeProcess: _Callable[[_type.HANDLE,  # hProcess
                               _Pointer[_type.DWORD]],  # lpExitCode
                              _type.BOOL]
SwitchToThread: _Callable[[],
                          _type.BOOL]
CreateThread: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpThreadAttributes
                         _type.SIZE_T,  # dwStackSize
                         _type.LPTHREAD_START_ROUTINE,  # lpStartAddress
                         _type.LPVOID,  # lpParameter
                         _type.DWORD,  # dwCreationFlags
                         _Pointer[_type.DWORD]],  # lpThreadId
                        _type.HANDLE]
CreateRemoteThread: _Callable[[_type.HANDLE,  # hProcess
                               _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpThreadAttributes
                               _type.SIZE_T,  # dwStackSize
                               _type.LPTHREAD_START_ROUTINE,  # lpStartAddress
                               _type.LPVOID,  # lpParameter
                               _type.DWORD,  # dwCreationFlags
                               _Pointer[_type.DWORD]],  # lpThreadId
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
                                   _type.BOOL],  # bDisablePriorityBoost
                                  _type.BOOL]
GetThreadPriorityBoost: _Callable[[_type.HANDLE,  # hThread
                                   _Pointer[_type.BOOL]],  # pDisablePriorityBoost
                                  _type.BOOL]
GetThreadPriority: _Callable[[_type.HANDLE],  # hThread
                             _type.c_int]
ExitThread: _Callable[[_type.DWORD],  # dwExitCode
                      _type.c_void]
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
                        _type.LPVOID],  # lpTlsValue
                       _type.BOOL]
TlsFree: _Callable[[_type.DWORD],  # dwTlsIndex
                   _type.BOOL]
CreateProcessA: _Callable[[_type.LPCSTR,  # lpApplicationName
                           _type.LPSTR,  # lpCommandLine
                           _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpProcessAttributes
                           _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpThreadAttributes
                           _type.BOOL,  # bInheritHandles
                           _type.DWORD,  # dwCreationFlags
                           _type.LPVOID,  # lpEnvironment
                           _type.LPCSTR,  # lpCurrentDirectory
                           _Pointer[_struct.STARTUPINFOA],  # lpStartupInfo
                           _Pointer[_struct.PROCESS_INFORMATION]],  # lpProcessInformation
                          _type.BOOL]
CreateProcessW: _Callable[[_type.LPCWSTR,  # lpApplicationName
                           _type.LPWSTR,  # lpCommandLine
                           _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpProcessAttributes
                           _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpThreadAttributes
                           _type.BOOL,  # bInheritHandles
                           _type.DWORD,  # dwCreationFlags
                           _type.LPVOID,  # lpEnvironment
                           _type.LPCWSTR,  # lpCurrentDirectory
                           _Pointer[_struct.STARTUPINFOW],  # lpStartupInfo
                           _Pointer[_struct.PROCESS_INFORMATION]],  # lpProcessInformation
                          _type.BOOL]
SetProcessShutdownParameters: _Callable[[_type.DWORD,  # dwLevel
                                         _type.DWORD],  # dwFlags
                                        _type.BOOL]
GetProcessVersion: _Callable[[_type.DWORD],  # ProcessId
                             _type.DWORD]
GetStartupInfoW: _Callable[[_Pointer[_struct.STARTUPINFOW]],  # lpStartupInfo
                           _type.c_void]
CreateProcessAsUserW: _Callable[[_type.HANDLE,  # hToken
                                 _type.LPCWSTR,  # lpApplicationName
                                 _type.LPWSTR,  # lpCommandLine
                                 _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpProcessAttributes
                                 _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpThreadAttributes
                                 _type.BOOL,  # bInheritHandles
                                 _type.DWORD,  # dwCreationFlags
                                 _type.LPVOID,  # lpEnvironment
                                 _type.LPCWSTR,  # lpCurrentDirectory
                                 _Pointer[_struct.STARTUPINFOW],  # lpStartupInfo
                                 _Pointer[_struct.PROCESS_INFORMATION]],  # lpProcessInformation
                                _type.BOOL]
GetCurrentProcessToken: _Callable[[],
                                  _type.HANDLE]
GetCurrentThreadToken: _Callable[[],
                                 _type.HANDLE]
GetCurrentThreadEffectiveToken: _Callable[[],
                                          _type.HANDLE]
SetThreadToken: _Callable[[_Pointer[_type.HANDLE],  # Thread
                           _type.HANDLE],  # Token
                          _type.BOOL]
OpenProcessToken: _Callable[[_type.HANDLE,  # ProcessHandle
                             _type.DWORD,  # DesiredAccess
                             _Pointer[_type.HANDLE]],  # TokenHandle
                            _type.BOOL]
OpenThreadToken: _Callable[[_type.HANDLE,  # ThreadHandle
                            _type.DWORD,  # DesiredAccess
                            _type.BOOL,  # OpenAsSelf
                            _Pointer[_type.HANDLE]],  # TokenHandle
                           _type.BOOL]
SetPriorityClass: _Callable[[_type.HANDLE,  # hProcess
                             _type.DWORD],  # dwPriorityClass
                            _type.BOOL]
GetPriorityClass: _Callable[[_type.HANDLE],  # hProcess
                            _type.DWORD]
SetThreadStackGuarantee: _Callable[[_Pointer[_type.ULONG]],  # StackSizeInBytes
                                   _type.BOOL]
ProcessIdToSessionId: _Callable[[_type.DWORD,  # dwProcessId
                                 _Pointer[_type.DWORD]],  # pSessionId
                                _type.BOOL]
GetProcessId: _Callable[[_type.HANDLE],  # Process
                        _type.DWORD]
GetThreadId: _Callable[[_type.HANDLE],  # Thread
                       _type.DWORD]
FlushProcessWriteBuffers: _Callable[[],
                                    _type.c_void]
GetProcessIdOfThread: _Callable[[_type.HANDLE],  # Thread
                                _type.DWORD]
InitializeProcThreadAttributeList: _Callable[[_Pointer[_struct.PROC_THREAD_ATTRIBUTE_LIST],  # lpAttributeList
                                              _type.DWORD,  # dwAttributeCount
                                              _type.DWORD,  # dwFlags
                                              _Pointer[_type.SIZE_T]],  # lpSize
                                             _type.BOOL]
DeleteProcThreadAttributeList: _Callable[[_Pointer[_struct.PROC_THREAD_ATTRIBUTE_LIST]],  # lpAttributeList
                                         _type.c_void]
UpdateProcThreadAttribute: _Callable[[_Pointer[_struct.PROC_THREAD_ATTRIBUTE_LIST],  # lpAttributeList
                                      _type.DWORD,  # dwFlags
                                      _type.DWORD_PTR,  # Attribute
                                      _type.PVOID,  # lpValue
                                      _type.SIZE_T,  # cbSize
                                      _type.PVOID,  # lpPreviousValue
                                      _Pointer[_type.SIZE_T]],  # lpReturnSize
                                     _type.BOOL]
SetProcessDynamicEHContinuationTargets: _Callable[[_type.HANDLE,  # Process
                                                   _type.USHORT,  # NumberOfTargets
                                                   _Pointer[_struct.PROCESS_DYNAMIC_EH_CONTINUATION_TARGET]],  # Targets
                                                  _type.BOOL]
SetProcessDynamicEnforcedCetCompatibleRanges: _Callable[[_type.HANDLE,  # Process
                                                         _type.USHORT,  # NumberOfRanges
                                                         _Pointer[_struct.PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE]],  # Ranges
                                                        _type.BOOL]
SetProcessAffinityUpdateMode: _Callable[[_type.HANDLE,  # hProcess
                                         _type.DWORD],  # dwFlags
                                        _type.BOOL]
QueryProcessAffinityUpdateMode: _Callable[[_type.HANDLE,  # hProcess
                                           _Pointer[_type.DWORD]],  # lpdwFlags
                                          _type.BOOL]
CreateRemoteThreadEx: _Callable[[_type.HANDLE,  # hProcess
                                 _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpThreadAttributes
                                 _type.SIZE_T,  # dwStackSize
                                 _type.LPTHREAD_START_ROUTINE,  # lpStartAddress
                                 _type.LPVOID,  # lpParameter
                                 _type.DWORD,  # dwCreationFlags
                                 _Pointer[_struct.PROC_THREAD_ATTRIBUTE_LIST],  # lpAttributeList
                                 _Pointer[_type.DWORD]],  # lpThreadId
                                _type.HANDLE]
GetCurrentThreadStackLimits: _Callable[[_Pointer[_type.ULONG_PTR],  # LowLimit
                                        _Pointer[_type.ULONG_PTR]],  # HighLimit
                                       _type.c_void]
GetThreadContext: _Callable[[_type.HANDLE,  # hThread
                             _Pointer[_struct.CONTEXT]],  # lpContext
                            _type.BOOL]
GetProcessMitigationPolicy: _Callable[[_type.HANDLE,  # hProcess
                                       _enum.PROCESS_MITIGATION_POLICY,  # MitigationPolicy
                                       _type.PVOID,  # lpBuffer
                                       _type.SIZE_T],  # dwLength
                                      _type.BOOL]
SetThreadContext: _Callable[[_type.HANDLE,  # hThread
                             _Pointer[_struct.CONTEXT]],  # lpContext
                            _type.BOOL]
SetProcessMitigationPolicy: _Callable[[_enum.PROCESS_MITIGATION_POLICY,  # MitigationPolicy
                                       _type.PVOID,  # lpBuffer
                                       _type.SIZE_T],  # dwLength
                                      _type.BOOL]
FlushInstructionCache: _Callable[[_type.HANDLE,  # hProcess
                                  _type.LPCVOID,  # lpBaseAddress
                                  _type.SIZE_T],  # dwSize
                                 _type.BOOL]
GetThreadTimes: _Callable[[_type.HANDLE,  # hThread
                           _Pointer[_struct.FILETIME],  # lpCreationTime
                           _Pointer[_struct.FILETIME],  # lpExitTime
                           _Pointer[_struct.FILETIME],  # lpKernelTime
                           _Pointer[_struct.FILETIME]],  # lpUserTime
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
SetThreadIdealProcessorEx: _Callable[[_type.HANDLE,  # hThread
                                      _Pointer[_struct.PROCESSOR_NUMBER],  # lpIdealProcessor
                                      _Pointer[_struct.PROCESSOR_NUMBER]],  # lpPreviousIdealProcessor
                                     _type.BOOL]
GetThreadIdealProcessorEx: _Callable[[_type.HANDLE,  # hThread
                                      _Pointer[_struct.PROCESSOR_NUMBER]],  # lpIdealProcessor
                                     _type.BOOL]
GetCurrentProcessorNumberEx: _Callable[[_Pointer[_struct.PROCESSOR_NUMBER]],  # ProcNumber
                                       _type.c_void]
GetProcessPriorityBoost: _Callable[[_type.HANDLE,  # hProcess
                                    _Pointer[_type.BOOL]],  # pDisablePriorityBoost
                                   _type.BOOL]
SetProcessPriorityBoost: _Callable[[_type.HANDLE,  # hProcess
                                    _type.BOOL],  # bDisablePriorityBoost
                                   _type.BOOL]
GetThreadIOPendingFlag: _Callable[[_type.HANDLE,  # hThread
                                   _Pointer[_type.BOOL]],  # lpIOIsPending
                                  _type.BOOL]
GetSystemTimes: _Callable[[_Pointer[_struct.FILETIME],  # lpIdleTime
                           _Pointer[_struct.FILETIME],  # lpKernelTime
                           _Pointer[_struct.FILETIME]],  # lpUserTime
                          _type.BOOL]
GetThreadInformation: _Callable[[_type.HANDLE,  # hThread
                                 _enum.THREAD_INFORMATION_CLASS,  # ThreadInformationClass
                                 _type.LPVOID,  # ThreadInformation
                                 _type.DWORD],  # ThreadInformationSize
                                _type.BOOL]
SetThreadInformation: _Callable[[_type.HANDLE,  # hThread
                                 _enum.THREAD_INFORMATION_CLASS,  # ThreadInformationClass
                                 _type.LPVOID,  # ThreadInformation
                                 _type.DWORD],  # ThreadInformationSize
                                _type.BOOL]
IsProcessCritical: _Callable[[_type.HANDLE,  # hProcess
                              _Pointer[_type.BOOL]],  # Critical
                             _type.BOOL]
SetProtectedPolicy: _Callable[[_Pointer[_struct.GUID],  # PolicyGuid
                               _type.ULONG_PTR,  # PolicyValue
                               _Pointer[_type.ULONG_PTR]],  # OldPolicyValue
                              _type.BOOL]
QueryProtectedPolicy: _Callable[[_Pointer[_struct.GUID],  # PolicyGuid
                                 _Pointer[_type.ULONG_PTR]],  # PolicyValue
                                _type.BOOL]
SetThreadIdealProcessor: _Callable[[_type.HANDLE,  # hThread
                                    _type.DWORD],  # dwIdealProcessor
                                   _type.DWORD]
SetProcessInformation: _Callable[[_type.HANDLE,  # hProcess
                                  _enum.PROCESS_INFORMATION_CLASS,  # ProcessInformationClass
                                  _type.LPVOID,  # ProcessInformation
                                  _type.DWORD],  # ProcessInformationSize
                                 _type.BOOL]
GetProcessInformation: _Callable[[_type.HANDLE,  # hProcess
                                  _enum.PROCESS_INFORMATION_CLASS,  # ProcessInformationClass
                                  _type.LPVOID,  # ProcessInformation
                                  _type.DWORD],  # ProcessInformationSize
                                 _type.BOOL]
GetSystemCpuSetInformation: _Callable[[_Pointer[_struct.SYSTEM_CPU_SET_INFORMATION],  # Information
                                       _type.ULONG,  # BufferLength
                                       _Pointer[_type.ULONG],  # ReturnedLength
                                       _type.HANDLE,  # Process
                                       _type.ULONG],  # Flags
                                      _type.BOOL]
GetProcessDefaultCpuSets: _Callable[[_type.HANDLE,  # Process
                                     _Pointer[_type.ULONG],  # CpuSetIds
                                     _type.ULONG,  # CpuSetIdCount
                                     _Pointer[_type.ULONG]],  # RequiredIdCount
                                    _type.BOOL]
SetProcessDefaultCpuSets: _Callable[[_type.HANDLE,  # Process
                                     _Pointer[_type.ULONG],  # CpuSetIds
                                     _type.ULONG],  # CpuSetIdCount
                                    _type.BOOL]
GetThreadSelectedCpuSets: _Callable[[_type.HANDLE,  # Thread
                                     _Pointer[_type.ULONG],  # CpuSetIds
                                     _type.ULONG,  # CpuSetIdCount
                                     _Pointer[_type.ULONG]],  # RequiredIdCount
                                    _type.BOOL]
SetThreadSelectedCpuSets: _Callable[[_type.HANDLE,  # Thread
                                     _Pointer[_type.ULONG],  # CpuSetIds
                                     _type.ULONG],  # CpuSetIdCount
                                    _type.BOOL]
CreateProcessAsUserA: _Callable[[_type.HANDLE,  # hToken
                                 _type.LPCSTR,  # lpApplicationName
                                 _type.LPSTR,  # lpCommandLine
                                 _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpProcessAttributes
                                 _Pointer[_struct.SECURITY_ATTRIBUTES],  # lpThreadAttributes
                                 _type.BOOL,  # bInheritHandles
                                 _type.DWORD,  # dwCreationFlags
                                 _type.LPVOID,  # lpEnvironment
                                 _type.LPCSTR,  # lpCurrentDirectory
                                 _Pointer[_struct.STARTUPINFOA],  # lpStartupInfo
                                 _Pointer[_struct.PROCESS_INFORMATION]],  # lpProcessInformation
                                _type.BOOL]
GetProcessShutdownParameters: _Callable[[_Pointer[_type.DWORD],  # lpdwLevel
                                         _Pointer[_type.DWORD]],  # lpdwFlags
                                        _type.BOOL]
GetProcessDefaultCpuSetMasks: _Callable[[_type.HANDLE,  # Process
                                         _Pointer[_struct.GROUP_AFFINITY],  # CpuSetMasks
                                         _type.USHORT,  # CpuSetMaskCount
                                         _Pointer[_type.USHORT]],  # RequiredMaskCount
                                        _type.BOOL]
SetProcessDefaultCpuSetMasks: _Callable[[_type.HANDLE,  # Process
                                         _Pointer[_struct.GROUP_AFFINITY],  # CpuSetMasks
                                         _type.USHORT],  # CpuSetMaskCount
                                        _type.BOOL]
GetThreadSelectedCpuSetMasks: _Callable[[_type.HANDLE,  # Thread
                                         _Pointer[_struct.GROUP_AFFINITY],  # CpuSetMasks
                                         _type.USHORT,  # CpuSetMaskCount
                                         _Pointer[_type.USHORT]],  # RequiredMaskCount
                                        _type.BOOL]
SetThreadSelectedCpuSetMasks: _Callable[[_type.HANDLE,  # Thread
                                         _Pointer[_struct.GROUP_AFFINITY],  # CpuSetMasks
                                         _type.USHORT],  # CpuSetMaskCount
                                        _type.BOOL]
GetMachineTypeAttributes: _Callable[[_type.USHORT,  # Machine
                                     _Pointer[_enum.MACHINE_ATTRIBUTES]],  # MachineTypeAttributes
                                    _type.HRESULT]
SetThreadDescription: _Callable[[_type.HANDLE,  # hThread
                                 _type.PCWSTR],  # lpThreadDescription
                                _type.HRESULT]
GetThreadDescription: _Callable[[_type.HANDLE,  # hThread
                                 _Pointer[_type.PWSTR]],  # ppszThreadDescription
                                _type.HRESULT]
# profileapi
QueryPerformanceCounter: _Callable[[_Pointer[_union.LARGE_INTEGER]],  # lpPerformanceCount
                                   _type.BOOL]
QueryPerformanceFrequency: _Callable[[_Pointer[_union.LARGE_INTEGER]],  # lpFrequency
                                     _type.BOOL]
# synchapi
InitializeSRWLock: _Callable[[_Pointer[_struct.RTL_SRWLOCK]],  # SRWLock
                             _type.c_void]
ReleaseSRWLockExclusive: _Callable[[_Pointer[_struct.RTL_SRWLOCK]],  # SRWLock
                                   _type.c_void]
ReleaseSRWLockShared: _Callable[[_Pointer[_struct.RTL_SRWLOCK]],  # SRWLock
                                _type.c_void]
AcquireSRWLockExclusive: _Callable[[_Pointer[_struct.RTL_SRWLOCK]],  # SRWLock
                                   _type.c_void]
AcquireSRWLockShared: _Callable[[_Pointer[_struct.RTL_SRWLOCK]],  # SRWLock
                                _type.c_void]
TryAcquireSRWLockExclusive: _Callable[[_Pointer[_struct.RTL_SRWLOCK]],  # SRWLock
                                      _type.BOOLEAN]
TryAcquireSRWLockShared: _Callable[[_Pointer[_struct.RTL_SRWLOCK]],  # SRWLock
                                   _type.BOOLEAN]
InitializeCriticalSection: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION]],  # lpCriticalSection
                                     _type.c_void]
EnterCriticalSection: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION]],  # lpCriticalSection
                                _type.c_void]
LeaveCriticalSection: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION]],  # lpCriticalSection
                                _type.c_void]
InitializeCriticalSectionAndSpinCount: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION],  # lpCriticalSection
                                                  _type.DWORD],  # dwSpinCount
                                                 _type.BOOL]
InitializeCriticalSectionEx: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION],  # lpCriticalSection
                                        _type.DWORD,  # dwSpinCount
                                        _type.DWORD],  # Flags
                                       _type.BOOL]
SetCriticalSectionSpinCount: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION],  # lpCriticalSection
                                        _type.DWORD],  # dwSpinCount
                                       _type.DWORD]
TryEnterCriticalSection: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION]],  # lpCriticalSection
                                   _type.BOOL]
DeleteCriticalSection: _Callable[[_Pointer[_struct.RTL_CRITICAL_SECTION]],  # lpCriticalSection
                                 _type.c_void]
InitOnceInitialize: _Callable[[_Pointer[_struct.RTL_RUN_ONCE]],  # InitOnce
                              _type.c_void]
InitOnceExecuteOnce: _Callable[[_Pointer[_struct.RTL_RUN_ONCE],  # InitOnce
                                _type.PINIT_ONCE_FN,  # InitFn
                                _type.PVOID,  # Parameter
                                _Pointer[_type.LPVOID]],  # Context
                               _type.BOOL]
InitOnceBeginInitialize: _Callable[[_Pointer[_struct.RTL_RUN_ONCE],  # lpInitOnce
                                    _type.DWORD,  # dwFlags
                                    _Pointer[_type.BOOL],  # fPending
                                    _Pointer[_type.LPVOID]],  # lpContext
                                   _type.BOOL]
InitOnceComplete: _Callable[[_Pointer[_struct.RTL_RUN_ONCE],  # lpInitOnce
                             _type.DWORD,  # dwFlags
                             _type.LPVOID],  # lpContext
                            _type.BOOL]
InitializeConditionVariable: _Callable[[_Pointer[_struct.RTL_CONDITION_VARIABLE]],  # ConditionVariable
                                       _type.c_void]
WakeConditionVariable: _Callable[[_Pointer[_struct.RTL_CONDITION_VARIABLE]],  # ConditionVariable
                                 _type.c_void]
WakeAllConditionVariable: _Callable[[_Pointer[_struct.RTL_CONDITION_VARIABLE]],  # ConditionVariable
                                    _type.c_void]
SleepConditionVariableCS: _Callable[[_Pointer[_struct.RTL_CONDITION_VARIABLE],  # ConditionVariable
                                     _Pointer[_struct.RTL_CRITICAL_SECTION],  # CriticalSection
                                     _type.DWORD],  # dwMilliseconds
                                    _type.BOOL]
SleepConditionVariableSRW: _Callable[[_Pointer[_struct.RTL_CONDITION_VARIABLE],  # ConditionVariable
                                      _Pointer[_struct.RTL_SRWLOCK],  # SRWLock
                                      _type.DWORD,  # dwMilliseconds
                                      _type.ULONG],  # Flags
                                     _type.BOOL]
SetEvent: _Callable[[_type.HANDLE],  # hEvent
                    _type.BOOL]
ResetEvent: _Callable[[_type.HANDLE],  # hEvent
                      _type.BOOL]
ReleaseSemaphore: _Callable[[_type.HANDLE,  # hSemaphore
                             _type.LONG,  # lReleaseCount
                             _Pointer[_type.c_long]],  # lpPreviousCount
                            _type.BOOL]
ReleaseMutex: _Callable[[_type.HANDLE],  # hMutex
                        _type.BOOL]
WaitForSingleObject: _Callable[[_type.HANDLE,  # hHandle
                                _type.DWORD],  # dwMilliseconds
                               _type.DWORD]
SleepEx: _Callable[[_type.DWORD,  # dwMilliseconds
                    _type.BOOL],  # bAlertable
                   _type.DWORD]
WaitForSingleObjectEx: _Callable[[_type.HANDLE,  # hHandle
                                  _type.DWORD,  # dwMilliseconds
                                  _type.BOOL],  # bAlertable
                                 _type.DWORD]
WaitForMultipleObjectsEx: _Callable[[_type.DWORD,  # nCount
                                     _Pointer[_type.HANDLE],  # lpHandles
                                     _type.BOOL,  # bWaitAll
                                     _type.DWORD,  # dwMilliseconds
                                     _type.BOOL],  # bAlertable
                                    _type.DWORD]
CreateMutexA: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpMutexAttributes
                         _type.BOOL,  # bInitialOwner
                         _type.LPCSTR],  # lpName
                        _type.HANDLE]
CreateMutexW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpMutexAttributes
                         _type.BOOL,  # bInitialOwner
                         _type.LPCWSTR],  # lpName
                        _type.HANDLE]
OpenMutexW: _Callable[[_type.DWORD,  # dwDesiredAccess
                       _type.BOOL,  # bInheritHandle
                       _type.LPCWSTR],  # lpName
                      _type.HANDLE]
CreateEventA: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpEventAttributes
                         _type.BOOL,  # bManualReset
                         _type.BOOL,  # bInitialState
                         _type.LPCSTR],  # lpName
                        _type.HANDLE]
CreateEventW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpEventAttributes
                         _type.BOOL,  # bManualReset
                         _type.BOOL,  # bInitialState
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
SetWaitableTimerEx: _Callable[[_type.HANDLE,  # hTimer
                               _Pointer[_union.LARGE_INTEGER],  # lpDueTime
                               _type.LONG,  # lPeriod
                               _type.PTIMERAPCROUTINE,  # pfnCompletionRoutine
                               _type.LPVOID,  # lpArgToCompletionRoutine
                               _Pointer[_struct.REASON_CONTEXT],  # WakeContext
                               _type.ULONG],  # TolerableDelay
                              _type.BOOL]
SetWaitableTimer: _Callable[[_type.HANDLE,  # hTimer
                             _Pointer[_union.LARGE_INTEGER],  # lpDueTime
                             _type.LONG,  # lPeriod
                             _type.PTIMERAPCROUTINE,  # pfnCompletionRoutine
                             _type.LPVOID,  # lpArgToCompletionRoutine
                             _type.BOOL],  # fResume
                            _type.BOOL]
CancelWaitableTimer: _Callable[[_type.HANDLE],  # hTimer
                               _type.BOOL]
CreateMutexExA: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpMutexAttributes
                           _type.LPCSTR,  # lpName
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateMutexExW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpMutexAttributes
                           _type.LPCWSTR,  # lpName
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateEventExA: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpEventAttributes
                           _type.LPCSTR,  # lpName
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateEventExW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpEventAttributes
                           _type.LPCWSTR,  # lpName
                           _type.DWORD,  # dwFlags
                           _type.DWORD],  # dwDesiredAccess
                          _type.HANDLE]
CreateSemaphoreExW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSemaphoreAttributes
                               _type.LONG,  # lInitialCount
                               _type.LONG,  # lMaximumCount
                               _type.LPCWSTR,  # lpName
                               _type.DWORD,  # dwFlags
                               _type.DWORD],  # dwDesiredAccess
                              _type.HANDLE]
CreateWaitableTimerExW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpTimerAttributes
                                   _type.LPCWSTR,  # lpTimerName
                                   _type.DWORD,  # dwFlags
                                   _type.DWORD],  # dwDesiredAccess
                                  _type.HANDLE]
EnterSynchronizationBarrier: _Callable[[_Pointer[_struct.RTL_BARRIER],  # lpBarrier
                                        _type.DWORD],  # dwFlags
                                       _type.BOOL]
InitializeSynchronizationBarrier: _Callable[[_Pointer[_struct.RTL_BARRIER],  # lpBarrier
                                             _type.LONG,  # lTotalThreads
                                             _type.LONG],  # lSpinCount
                                            _type.BOOL]
DeleteSynchronizationBarrier: _Callable[[_Pointer[_struct.RTL_BARRIER]],  # lpBarrier
                                        _type.BOOL]
Sleep: _Callable[[_type.DWORD],  # dwMilliseconds
                 _type.c_void]
WaitOnAddress: _Callable[[_type.c_void_p,  # Address
                          _type.PVOID,  # CompareAddress
                          _type.SIZE_T,  # AddressSize
                          _type.DWORD],  # dwMilliseconds
                         _type.BOOL]
WakeByAddressSingle: _Callable[[_type.PVOID],  # Address
                               _type.c_void]
WakeByAddressAll: _Callable[[_type.PVOID],  # Address
                            _type.c_void]
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
CreateSemaphoreW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpSemaphoreAttributes
                             _type.LONG,  # lInitialCount
                             _type.LONG,  # lMaximumCount
                             _type.LPCWSTR],  # lpName
                            _type.HANDLE]
CreateWaitableTimerW: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # lpTimerAttributes
                                 _type.BOOL,  # bManualReset
                                 _type.LPCWSTR],  # lpTimerName
                                _type.HANDLE]
# sysinfoapi
GlobalMemoryStatusEx: _Callable[[_Pointer[_struct.MEMORYSTATUSEX]],  # lpBuffer
                                _type.BOOL]
GetSystemInfo: _Callable[[_Pointer[_struct.SYSTEM_INFO]],  # lpSystemInfo
                         _type.c_void]
GetSystemTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                         _type.c_void]
GetSystemTimeAsFileTime: _Callable[[_Pointer[_struct.FILETIME]],  # lpSystemTimeAsFileTime
                                   _type.c_void]
GetLocalTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                        _type.c_void]
IsUserCetAvailableInEnvironment: _Callable[[_type.DWORD],  # UserCetEnvironment
                                           _type.BOOL]
GetSystemLeapSecondInformation: _Callable[[_Pointer[_type.BOOL],  # Enabled
                                           _Pointer[_type.DWORD]],  # Flags
                                          _type.BOOL]
GetVersion: _Callable[[],
                      _type.DWORD]
SetLocalTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                        _type.BOOL]
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
GetSystemDirectoryA: _Callable[[_type.LPSTR,  # lpBuffer
                                _type.UINT],  # uSize
                               _type.UINT]
GetSystemDirectoryW: _Callable[[_type.LPWSTR,  # lpBuffer
                                _type.UINT],  # uSize
                               _type.UINT]
GetWindowsDirectoryA: _Callable[[_type.LPSTR,  # lpBuffer
                                 _type.UINT],  # uSize
                                _type.UINT]
GetWindowsDirectoryW: _Callable[[_type.LPWSTR,  # lpBuffer
                                 _type.UINT],  # uSize
                                _type.UINT]
GetSystemWindowsDirectoryA: _Callable[[_type.LPSTR,  # lpBuffer
                                       _type.UINT],  # uSize
                                      _type.UINT]
GetSystemWindowsDirectoryW: _Callable[[_type.LPWSTR,  # lpBuffer
                                       _type.UINT],  # uSize
                                      _type.UINT]
GetComputerNameExA: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                               _type.LPSTR,  # lpBuffer
                               _Pointer[_type.DWORD]],  # nSize
                              _type.BOOL]
GetComputerNameExW: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                               _type.LPWSTR,  # lpBuffer
                               _Pointer[_type.DWORD]],  # nSize
                              _type.BOOL]
SetComputerNameExW: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                               _type.LPCWSTR],  # lpBuffer
                              _type.BOOL]
SetSystemTime: _Callable[[_Pointer[_struct.SYSTEMTIME]],  # lpSystemTime
                         _type.BOOL]
GetVersionExA: _Callable[[_Pointer[_struct.OSVERSIONINFOA]],  # lpVersionInformation
                         _type.BOOL]
GetVersionExW: _Callable[[_Pointer[_struct.OSVERSIONINFOW]],  # lpVersionInformation
                         _type.BOOL]
GetLogicalProcessorInformation: _Callable[[_Pointer[_struct.SYSTEM_LOGICAL_PROCESSOR_INFORMATION],  # Buffer
                                           _Pointer[_type.DWORD]],  # ReturnedLength
                                          _type.BOOL]
GetLogicalProcessorInformationEx: _Callable[[_enum.LOGICAL_PROCESSOR_RELATIONSHIP,  # RelationshipType
                                             _Pointer[_struct.SYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX],  # Buffer
                                             _Pointer[_type.DWORD]],  # ReturnedLength
                                            _type.BOOL]
GetNativeSystemInfo: _Callable[[_Pointer[_struct.SYSTEM_INFO]],  # lpSystemInfo
                               _type.c_void]
GetSystemTimePreciseAsFileTime: _Callable[[_Pointer[_struct.FILETIME]],  # lpSystemTimeAsFileTime
                                          _type.c_void]
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
EnumSystemFirmwareTables: _Callable[[_type.DWORD,  # FirmwareTableProviderSignature
                                     _type.PVOID,  # pFirmwareTableEnumBuffer
                                     _type.DWORD],  # BufferSize
                                    _type.UINT]
GetSystemFirmwareTable: _Callable[[_type.DWORD,  # FirmwareTableProviderSignature
                                   _type.DWORD,  # FirmwareTableID
                                   _type.PVOID,  # pFirmwareTableBuffer
                                   _type.DWORD],  # BufferSize
                                  _type.UINT]
DnsHostnameToComputerNameExW: _Callable[[_type.LPCWSTR,  # Hostname
                                         _type.LPWSTR,  # ComputerName
                                         _Pointer[_type.DWORD]],  # nSize
                                        _type.BOOL]
GetPhysicallyInstalledSystemMemory: _Callable[[_Pointer[_type.ULONGLONG]],  # TotalMemoryInKilobytes
                                              _type.BOOL]
SetComputerNameEx2W: _Callable[[_enum.COMPUTER_NAME_FORMAT,  # NameType
                                _type.DWORD,  # Flags
                                _type.LPCWSTR],  # lpBuffer
                               _type.BOOL]
SetSystemTimeAdjustment: _Callable[[_type.DWORD,  # dwTimeAdjustment
                                    _type.BOOL],  # bTimeAdjustmentDisabled
                                   _type.BOOL]
SetSystemTimeAdjustmentPrecise: _Callable[[_type.DWORD64,  # dwTimeAdjustment
                                           _type.BOOL],  # bTimeAdjustmentDisabled
                                          _type.BOOL]
InstallELAMCertificateInfo: _Callable[[_type.HANDLE],  # ELAMFile
                                      _type.BOOL]
GetProcessorSystemCycleTime: _Callable[[_type.USHORT,  # Group
                                        _Pointer[_struct.SYSTEM_PROCESSOR_CYCLE_TIME_INFORMATION],  # Buffer
                                        _Pointer[_type.DWORD]],  # ReturnedLength
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
GetDynamicTimeZoneInformation: _Callable[[_Pointer[_struct.TIME_DYNAMIC_ZONE_INFORMATION]],  # pTimeZoneInformation
                                         _type.DWORD]
GetTimeZoneInformationForYear: _Callable[[_type.USHORT,  # wYear
                                          _Pointer[_struct.TIME_DYNAMIC_ZONE_INFORMATION],  # pdtzi
                                          _Pointer[_struct.TIME_ZONE_INFORMATION]],  # ptzi
                                         _type.BOOL]
EnumDynamicTimeZoneInformation: _Callable[[_type.DWORD,  # dwIndex
                                           _Pointer[_struct.TIME_DYNAMIC_ZONE_INFORMATION]],  # lpTimeZoneInformation
                                          _type.DWORD]
GetDynamicTimeZoneInformationEffectiveYears: _Callable[[_Pointer[_struct.TIME_DYNAMIC_ZONE_INFORMATION],  # lpTimeZoneInformation
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
EncodePointer: _Callable[[_type.PVOID],  # Ptr
                         _type.PVOID]
DecodePointer: _Callable[[_type.PVOID],  # Ptr
                         _type.PVOID]
EncodeSystemPointer: _Callable[[_type.PVOID],  # Ptr
                               _type.PVOID]
DecodeSystemPointer: _Callable[[_type.PVOID],  # Ptr
                               _type.PVOID]
EncodeRemotePointer: _Callable[[_type.HANDLE,  # ProcessHandle
                                _type.PVOID,  # Ptr
                                _Pointer[_type.PVOID]],  # EncodedPtr
                               _type.HRESULT]
DecodeRemotePointer: _Callable[[_type.HANDLE,  # ProcessHandle
                                _type.PVOID,  # Ptr
                                _Pointer[_type.PVOID]],  # DecodedPtr
                               _type.HRESULT]
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
# wow64apiset
Wow64EnableWow64FsRedirection: _Callable[[_type.BOOLEAN],  # Wow64FsEnableRedirection
                                         _type.BOOLEAN]
Wow64DisableWow64FsRedirection: _Callable[[_Pointer[_type.PVOID]],  # OldValue
                                          _type.BOOL]
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
                            _Pointer[_type.USHORT]],  # pNativeMachine
                           _type.BOOL]
GetSystemWow64Directory2A: _Callable[[_type.LPSTR,  # lpBuffer
                                      _type.UINT,  # uSize
                                      _type.WORD],  # ImageFileMachineType
                                     _type.UINT]
GetSystemWow64Directory2W: _Callable[[_type.LPWSTR,  # lpBuffer
                                      _type.UINT,  # uSize
                                      _type.WORD],  # ImageFileMachineType
                                     _type.UINT]
IsWow64GuestMachineSupported: _Callable[[_type.USHORT,  # WowGuestMachine
                                         _Pointer[_type.BOOL]],  # MachineIsSupported
                                        _type.HRESULT]
Wow64GetThreadContext: _Callable[[_type.HANDLE,  # hThread
                                  _Pointer[_struct.WOW64_CONTEXT]],  # lpContext
                                 _type.BOOL]
Wow64SetThreadContext: _Callable[[_type.HANDLE,  # hThread
                                  _Pointer[_struct.WOW64_CONTEXT]],  # lpContext
                                 _type.BOOL]
Wow64SuspendThread: _Callable[[_type.HANDLE],  # hThread
                              _type.DWORD]

_WinLib(__name__)
