from __future__ import annotations as _

import ctypes as _ctypes
import typing as _typing
from typing import Callable as _Callable, Optional as _Optional

from . import const as _const, enum as _enum, interface as _interface, struct as _struct, type as _type, union as _union
from ._utils import _Pointer, _format_annotations, _func_doc, _resolve_type


class _CDLL(type):
    pass


def _load(self: _CDLL):
    if self._lib is None:
        if isinstance(self, _PyDLL):
            self._lib = _ctypes.pythonapi
        else:
            name_ = self.__qualname__
            mode = _ctypes.DEFAULT_MODE
            if isinstance(self, _WinDLL):
                name_ = f'{name_}.dll'
                mode = _const.LOAD_LIBRARY_SEARCH_DEFAULT_DIRS
            self._lib = getattr(_ctypes, type(self).__name__[1:])(name_, mode)


def _init(self, name: str):
    if name in self.__annotations__:
        if self._funcs is None:
            self._annots = _typing.get_type_hints(self)
            self._funcs = {}
            for name_ in self.__annotations__:
                try:
                    self._funcs[name_] = vars(self)[name_]
                except KeyError:
                    self._funcs[name_] = name_
                else:
                    delattr(self, name_)
        func = None
        while func is None:
            try:
                func = self._lib[self._funcs[name]]
            except KeyError:
                raise AttributeError(f"Lib '{self.__qualname__}' has no function '{name}'")
            except TypeError:
                _load(self)
        annot = _format_annotations(self.__annotations__[name])
        func.restype, *func.argtypes = _resolve_type(self._annots[name])
        if self._errcheck is not None:
            func.errcheck = self._errcheck
        func.__name__ = name
        func.__doc__ = _func_doc(name, func.restype, func.argtypes, annot)
        setattr(self, name, func)
        return func
    return super(type(self), self).__getattribute__(name)


_CDLL.__getattr__ = _init


class _OleDLL(_CDLL):
    pass


class _PyDLL(_CDLL):
    pass


class _WinDLL(_CDLL):
    pass


class _Func:
    _lib = None
    _errcheck = None
    _funcs = None


# noinspection PyPep8Naming
class msvcrt(_Func, metaclass=_CDLL):
    # corecrt_io
    _access: _Callable[[_type.c_char_p,  # _FileName
                        _type.c_int],  # _AccessMode
                       _type.c_int]
    _access_s: _Callable[[_type.c_char_p,  # _FileName
                          _type.c_int],  # _AccessMode
                         _type.errno_t]
    _chmod: _Callable[[_type.c_char_p,  # _FileName
                       _type.c_int],  # _Mode
                      _type.c_int]
    _chsize: _Callable[[_type.c_int,  # _FileHandle
                        _type.c_long],  # _Size
                       _type.c_int]
    _chsize_s: _Callable[[_type.c_int,  # _FileHandle
                          _type.c_int64],  # _Size
                         _type.errno_t]
    _close: _Callable[[_type.c_int],  # _FileHandle
                      _type.c_int]
    _commit: _Callable[[_type.c_int],  # _FileHandle
                       _type.c_int]
    # corecrt_malloc
    calloc: _Callable[[_type.c_size_t,  # _Count
                       _type.c_size_t],  # _Size
                      _type.c_void_p]
    free: _Callable[[_type.c_void_p],  # _Block
                    _type.c_void]
    malloc: _Callable[[_type.c_size_t],  # _Size
                      _type.c_void_p]
    realloc: _Callable[[_type.c_void_p,  # _Block
                        _type.c_size_t],  # _Size
                       _type.c_void_p]
    # corecrt_wstring
    wcscmp: _Callable[[_type.c_wchar_p,  # _String1
                       _type.c_wchar_p],  # _String2
                      _type.c_int]
    wcscspn: _Callable[[_type.c_wchar_p,  # _String
                        _type.c_wchar_p],  # _Control
                       _type.c_size_t]
    wcslen: _Callable[[_type.c_wchar_p],  # _String
                      _type.c_size_t]
    wcsnlen: _Callable[[_type.c_wchar_p,  # _Source
                        _type.c_size_t],  # _MaxCount
                       _type.c_size_t]
    wcsncmp: _Callable[[_type.c_wchar_p,  # _String1
                        _type.c_wchar_p,  # _String2
                        _type.c_size_t],  # _MaxCount
                       _type.c_int]
    # stdio
    clearerr_s: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                          _type.errno_t]
    clearerr: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                        _type.c_void]
    fclose: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                      _type.c_int]
    _fcloseall: _Callable[[],
                          _type.c_int]
    feof: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                    _type.c_int]
    ferror: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                      _type.c_int]
    fflush: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                      _type.c_int]
    fgetc: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                     _type.c_int]
    _fgetchar: _Callable[[],
                         _type.c_int]
    fgets: _Callable[[_type.c_char_p,  # _Buffer
                      _type.c_int,  # _MaxCount
                      _Pointer[_struct.FILE]],  # _Stream
                     _type.c_char_p]
    _fileno: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                       _type.c_int]
    _flushall: _Callable[[],
                         _type.c_int]
    fopen: _Callable[[_type.c_char_p,  # _FileName
                      _type.c_char_p],  # _Mode
                     _Pointer[_struct.FILE]]
    fputc: _Callable[[_type.c_int,  # _Character
                      _Pointer[_struct.FILE]],  # _Stream
                     _type.c_int]
    _fputchar: _Callable[[_type.c_int],  # _Character
                         _type.c_int]
    fputs: _Callable[[_type.c_char_p,  # _Buffer
                      _Pointer[_struct.FILE]],  # _Stream
                     _type.c_int]
    freopen: _Callable[[_type.c_char_p,  # _FileName
                        _type.c_char_p,  # _Mode
                        _Pointer[_struct.FILE]],  # _Stream
                       _Pointer[_struct.FILE]]
    _fsopen: _Callable[[_type.c_char_p,  # _FileName
                        _type.c_char_p,  # _Mode
                        _type.c_int],  # _ShFlag
                       _Pointer[_struct.FILE]]
    fseek: _Callable[[_Pointer[_struct.FILE],  # _Stream
                      _type.c_long,  # _Offset
                      _type.c_int],  # _Origin
                     _type.c_int]
    _fseeki64: _Callable[[_Pointer[_struct.FILE],  # _Stream
                          _type.c_int64,  # _Offset
                          _type.c_int],  # _Origin
                         _type.c_int]
    ftell: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                     _type.c_long]
    getc: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                    _type.c_int]
    getchar: _Callable[[],
                       _type.c_int]
    _getmaxstdio: _Callable[[],
                            _type.c_int]
    _getw: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                     _type.c_int]
    perror: _Callable[[_Optional[_type.c_char_p]],  # _ErrorMessage
                      _type.c_void]
    _pclose: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                       _type.c_int]
    _popen: _Callable[[_type.c_char_p,  # _Command
                       _type.c_char_p],  # _Mode
                      _Pointer[_struct.FILE]]
    putc: _Callable[[_type.c_int,  # _Character
                     _Pointer[_struct.FILE]],  # _Stream
                    _type.c_int]
    putchar: _Callable[[_type.c_int],  # _Character
                       _type.c_int]
    puts: _Callable[[_type.c_char_p],  # _Buffer
                    _type.c_int]
    _putw: _Callable[[_type.c_int,  # _Word
                      _Pointer[_struct.FILE]],  # _Stream
                     _type.c_int]
    remove: _Callable[[_type.c_char_p],  # _FileName
                      _type.c_int]
    rename: _Callable[[_type.c_char_p,  # _OldFileName
                       _type.c_char_p],  # _NewFileName
                      _type.c_int]
    _unlink: _Callable[[_type.c_char_p],  # _FileName
                       _type.c_int]
    unlink: _Callable[[_type.c_char_p],  # _FileName
                      _type.c_int]
    rewind: _Callable[[_Pointer[_struct.FILE]],  # _Stream
                      _type.c_void]
    _rmtmp: _Callable[[],
                      _type.c_int]
    _setmaxstdio: _Callable[[_type.c_int],  # _Maximum
                            _type.c_int]
    # stdlib
    getenv: _Callable[[_type.c_char_p],  # _VarName
                      _type.c_char_p]
    system: _Callable[[_Optional[_type.c_char_p]],  # _Command
                      _type.c_int]
    _seterrormode: _Callable[[_type.c_int],  # _Mode
                             _type.c_void]
    _beep: _Callable[[_type.c_uint,  # _Frequency
                      _type.c_uint],  # _Duration
                     _type.c_void]
    _sleep: _Callable[[_type.c_ulong],  # _Duration
                      _type.c_void]
    # string
    strcpy_s: _Callable[[_type.c_char_p,  # _Destination
                         _type.rsize_t,  # _SizeInBytes
                         _type.c_char_p],  # _Source
                        _type.errno_t]
    strcat_s: _Callable[[_type.c_char_p,  # _Destination
                         _type.rsize_t,  # _SizeInBytes
                         _type.c_char_p],  # _Source
                        _type.errno_t]
    strerror_s: _Callable[[_type.c_char_p,  # _Buffer
                           _type.rsize_t,  # _SizeInBytes
                           _type.c_int],  # _ErrorNumber
                          _type.errno_t]
    strncat_s: _Callable[[_type.c_char_p,  # _Destination
                          _type.rsize_t,  # _SizeInBytes
                          _type.c_char_p,  # _Source
                          _type.rsize_t],  # _MaxCount
                         _type.errno_t]
    strncpy_s: _Callable[[_type.c_char_p,  # _Destination
                          _type.rsize_t,  # _SizeInBytes
                          _type.c_char_p,  # _Source
                          _type.rsize_t],  # _MaxCount
                         _type.errno_t]
    strtok_s: _Callable[[_type.c_char_p,  # _String
                         _type.c_char_p,  # _Delimiters
                         _Pointer[_type.c_char_p]],  # _Context
                        _type.c_char_p]
    strcat: _Callable[[_type.c_char_p,  # _Destination
                       _type.c_char_p],  # _Source
                      _type.c_char_p]
    strcmp: _Callable[[_type.c_char_p,  # _Str1
                       _type.c_char_p],  # _Str2
                      _type.c_int]
    strcoll: _Callable[[_type.c_char_p,  # _String1
                        _type.c_char_p],  # _String2
                       _type.c_int]
    strcpy: _Callable[[_type.c_char_p,  # _Destination
                       _type.c_char_p],  # _Source
                      _type.c_char_p]
    strcspn: _Callable[[_type.c_char_p,  # _Str
                        _type.c_char_p],  # _Control
                       _type.c_size_t]
    # vcruntime_string
    memchr: _Callable[[_type.c_void_p,  # _Buf
                       _type.c_int,  # _Val
                       _type.c_size_t],  # _MaxCount
                      _type.c_void_p]
    memcmp: _Callable[[_type.c_void_p,  # _Buf1
                       _type.c_void_p,  # _Buf2
                       _type.c_size_t],  # _Size
                      _type.c_int]
    memcpy: _Callable[[_type.c_void_p,  # _Dst
                       _type.c_void_p,  # _Src
                       _type.c_size_t],  # _Size
                      _type.c_void_p]
    memmove: _Callable[[_type.c_void_p,  # _Dst
                        _type.c_void_p,  # _Src
                        _type.c_size_t],  # _Size
                       _type.c_void_p]
    memset: _Callable[[_type.c_void_p,  # _Dst
                       _type.c_int,  # _Val
                       _type.c_size_t],  # _Size
                      _type.c_void_p]
    strchr: _Callable[[_type.c_char_p,  # _Str
                       _type.c_int],  # _Val
                      _type.c_char_p]
    strrchr: _Callable[[_type.c_char_p,  # _Str
                        _type.c_int],  # _Ch
                       _type.c_char_p]
    strstr: _Callable[[_type.c_char_p,  # _Str
                       _type.c_char_p],  # _SubStr
                      _type.c_char_p]
    wcschr: _Callable[[_type.c_wchar_p,  # _Str
                       _type.c_wchar_t],  # _Ch
                      _type.c_wchar_p]
    wcsrchr: _Callable[[_type.c_wchar_p,  # _Str
                        _type.c_wchar_t],  # _Ch
                       _type.c_wchar_p]
    wcsstr: _Callable[[_type.c_wchar_p,  # _Str
                       _type.c_wchar_p],  # _SubStr
                      _type.c_wchar_p]


# noinspection PyPep8Naming
class python(_Func, metaclass=_PyDLL):
    # ceval
    Py_MakePendingCalls: _Callable[[],
                                   _type.c_int]
    Py_SetRecursionLimit: _Callable[[_type.c_int],
                                    _type.c_void]
    Py_GetRecursionLimit: _Callable[[],
                                    _type.c_int]
    Py_EnterRecursiveCall: _Callable[[_type.c_char_p],  # where
                                     _type.c_int]
    Py_LeaveRecursiveCall: _Callable[[],
                                     _type.c_void]
    PyEval_ThreadsInitialized: _Callable[[],
                                         _type.c_int]
    PyEval_InitThreads: _Callable[[],
                                  _type.c_void]
    PyEval_AcquireLock: _Callable[[],
                                  _type.c_void]
    PyEval_ReleaseLock: _Callable[[],
                                  _type.c_void]
    # import
    PyImport_GetMagicNumber: _Callable[[],
                                       _type.c_long]
    PyImport_GetMagicTag: _Callable[[],
                                    _type.c_char_p]
    # pyerrors
    PyErr_Clear: _Callable[[],
                           _type.c_void]
    Py_FatalError: _Callable[[_type.c_char_p],  # message
                             _type.c_void]
    PyErr_BadArgument: _Callable[[],
                                 _type.c_void]
    PyErr_BadInternalCall: _Callable[[],
                                     _type.c_void]
    _PyErr_BadInternalCall: _Callable[[_type.c_char_p,  # filename
                                       _type.c_int],  # lineno
                                      _type.c_void]
    PyErr_CheckSignals: _Callable[[],
                                  _type.c_int]
    PyErr_SetInterrupt: _Callable[[],
                                  _type.c_void]
    PyErr_SyntaxLocation: _Callable[[_type.c_char_p,  # filename
                                     _type.c_int],  # lineno
                                    _type.c_void]
    PyErr_SyntaxLocationEx: _Callable[[_type.c_char_p,  # filename
                                       _type.c_int,  # lineno
                                       _type.c_int],  # col_offset
                                      _type.c_void]
    PyOS_vsnprintf: _Callable[[_type.c_char_p,  # str
                               _type.c_size_t,  # size
                               _type.c_char_p,  # format
                               _type.va_list],  # va
                              _type.c_int]
    # pylifecycle
    Py_Initialize: _Callable[[],
                             _type.c_void]
    Py_InitializeEx: _Callable[[_type.c_int],
                               _type.c_void]
    Py_Finalize: _Callable[[],
                           _type.c_void]
    Py_FinalizeEx: _Callable[[],
                             _type.c_int]
    Py_IsInitialized: _Callable[[],
                                _type.c_int]
    Py_Exit: _Callable[[_type.c_int],
                       _type.c_void]
    Py_Main: _Callable[[_type.c_int,  # argc
                        _Pointer[_type.c_wchar_p]],  # argv
                       _type.c_int]
    Py_FrozenMain: _Callable[[_type.c_int,  # argc
                              _Pointer[_type.c_char_p]],  # argv
                             _type.c_int]
    Py_BytesMain: _Callable[[_type.c_int,  # argc
                             _Pointer[_type.c_char_p]],  # argv
                            _type.c_int]
    Py_GetProgramName: _Callable[[],
                                 _type.c_wchar_p]
    Py_SetPythonHome: _Callable[[_type.c_wchar_p],
                                _type.c_void]
    Py_GetPythonHome: _Callable[[],
                                _type.c_wchar_p]
    Py_GetProgramFullPath: _Callable[[],
                                     _type.c_wchar_p]
    Py_GetPrefix: _Callable[[],
                            _type.c_wchar_p]
    Py_GetExecPrefix: _Callable[[],
                                _type.c_wchar_p]
    Py_GetPath: _Callable[[],
                          _type.c_wchar_p]
    Py_SetPath: _Callable[[_type.c_wchar_p],
                          _type.c_void]
    Py_GetVersion: _Callable[[],
                             _type.c_char_p]
    Py_GetPlatform: _Callable[[],
                              _type.c_char_p]
    Py_GetCopyright: _Callable[[],
                               _type.c_char_p]
    Py_GetCompiler: _Callable[[],
                              _type.c_char_p]
    Py_GetBuildInfo: _Callable[[],
                               _type.c_char_p]
    # pymem
    PyMem_Malloc: _Callable[[_type.c_size_t],  # size
                            _type.c_void_p]
    PyMem_Realloc: _Callable[[_type.c_void_p,  # ptr
                              _type.c_size_t],  # size
                             _type.c_void_p]
    PyMem_Free: _Callable[[_type.c_void_p],  # ptr
                          _type.c_void]
    # pythonrun
    PyErr_Print: _Callable[[],
                           _type.c_void]
    PyErr_PrintEx: _Callable[[_type.c_int],
                             _type.c_void]
    PyRun_SimpleString: _Callable[[_type.c_char_p],  # s
                                  _type.c_int]
    # pythread
    PyThread_init_thread: _Callable[[],
                                    _type.c_void]
    PyThread_exit_thread: _Callable[[],
                                    _type.c_void]
    PyThread_get_thread_ident: _Callable[[],
                                         _type.c_ulong]
    PyThread_get_thread_native_id: _Callable[[],
                                             _type.c_ulong]
    PyThread_get_stacksize: _Callable[[],
                                      _type.c_size_t]
    PyThread_set_stacksize: _Callable[[_type.c_size_t],
                                      _type.c_int]
    PyThread_create_key: _Callable[[],
                                   _type.c_int]
    PyThread_delete_key: _Callable[[_type.c_int],  # key
                                   _type.c_void]
    PyThread_set_key_value: _Callable[[_type.c_int,  # key
                                       _type.c_void_p],  # value
                                      _type.c_int]
    PyThread_get_key_value: _Callable[[_type.c_int],  # key
                                      _type.c_void_p]
    PyThread_delete_key_value: _Callable[[_type.c_int],  # key
                                         _type.c_void]
    PyThread_ReInitTLS: _Callable[[],
                                  _type.c_void]
    # sysmodule
    PySys_SetArgv: _Callable[[_type.c_int,
                              _Pointer[_type.c_wchar_p]],
                             _type.c_void]
    PySys_SetArgvEx: _Callable[[_type.c_int,
                                _Pointer[_type.c_wchar_p],
                                _type.c_int],
                               _type.c_void]
    PySys_SetPath: _Callable[[_type.c_wchar_p],
                             _type.c_void]
    PySys_ResetWarnOptions: _Callable[[],
                                      _type.c_void]
    PySys_AddWarnOption: _Callable[[_type.c_wchar_p],
                                   _type.c_void]
    PySys_HasWarnOptions: _Callable[[],
                                    _type.c_int]
    PySys_AddXOption: _Callable[[_type.c_wchar_p],
                                _type.c_void]


# noinspection PyPep8Naming
class advapi32(_Func, metaclass=_WinDLL):
    # winreg
    AbortSystemShutdownA: _Callable[[_type.LPSTR],
                                    _type.BOOL]
    AbortSystemShutdownW: _Callable[[_type.LPWSTR],
                                    _type.BOOL]
    CheckForHiberboot: _Callable[[_Pointer[_type.BOOLEAN],
                                  _type.BOOLEAN],
                                 _type.DWORD]
    InitiateShutdownA: _Callable[[_Optional[_type.LPSTR],
                                  _Optional[_type.LPSTR],
                                  _type.DWORD,
                                  _type.DWORD,
                                  _type.DWORD],
                                 _type.DWORD]
    InitiateShutdownW: _Callable[[_Optional[_type.LPWSTR],
                                  _Optional[_type.LPWSTR],
                                  _type.DWORD,
                                  _type.DWORD,
                                  _type.DWORD],
                                 _type.DWORD]
    InitiateSystemShutdownA: _Callable[[_Optional[_type.LPSTR],
                                        _Optional[_type.LPSTR],
                                        _type.DWORD,
                                        _type.BOOL,
                                        _type.BOOL],
                                       _type.BOOL]
    InitiateSystemShutdownW: _Callable[[_Optional[_type.LPWSTR],
                                        _Optional[_type.LPWSTR],
                                        _type.DWORD,
                                        _type.BOOL,
                                        _type.BOOL],
                                       _type.BOOL]
    InitiateSystemShutdownExA: _Callable[[_Optional[_type.LPSTR],
                                          _Optional[_type.LPSTR],
                                          _type.DWORD,
                                          _type.BOOL,
                                          _type.BOOL,
                                          _type.DWORD],
                                         _type.BOOL]
    InitiateSystemShutdownExW: _Callable[[_Optional[_type.LPWSTR],
                                          _Optional[_type.LPWSTR],
                                          _type.DWORD,
                                          _type.BOOL,
                                          _type.BOOL,
                                          _type.DWORD],
                                         _type.BOOL]
    RegCopyTreeA: _Callable[[_type.HKEY,
                             _Optional[_type.LPCSTR],
                             _type.HKEY],
                            _type.LSTATUS]
    RegCopyTreeW: _Callable[[_type.HKEY,
                             _Optional[_type.LPCWSTR],
                             _type.HKEY],
                            _type.LSTATUS]
    RegDeleteKeyValueA: _Callable[[_type.HKEY,
                                   _Optional[_type.LPCSTR],
                                   _Optional[_type.LPCSTR]],
                                  _type.LSTATUS]
    RegDeleteKeyValueW: _Callable[[_type.HKEY,
                                   _Optional[_type.LPCWSTR],
                                   _Optional[_type.LPCWSTR]],
                                  _type.LSTATUS]
    RegDeleteTreeA: _Callable[[_type.HKEY,
                               _Optional[_type.LPCSTR]],
                              _type.LSTATUS]
    RegDeleteTreeW: _Callable[[_type.HKEY,
                               _Optional[_type.LPCWSTR]],
                              _type.LSTATUS]
    RegLoadAppKeyA: _Callable[[_type.LPCSTR,
                               _Pointer[_type.HKEY],
                               _type.REGSAM,
                               _type.DWORD,
                               _type.DWORD],
                              _type.LSTATUS]
    RegLoadAppKeyW: _Callable[[_type.LPCWSTR,
                               _Pointer[_type.HKEY],
                               _type.REGSAM,
                               _type.DWORD,
                               _type.DWORD],
                              _type.LSTATUS]
    RegLoadMUIStringA: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCSTR],
                                  _Optional[_type.LPSTR],
                                  _type.DWORD,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _type.DWORD,
                                  _Optional[_type.LPCSTR]],
                                 _type.LSTATUS]
    RegLoadMUIStringW: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCWSTR],
                                  _Optional[_type.LPWSTR],
                                  _type.DWORD,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _type.DWORD,
                                  _Optional[_type.LPCWSTR]],
                                 _type.LSTATUS]
    RegReplaceKeyA: _Callable[[_type.HKEY,
                               _Optional[_type.LPCSTR],
                               _type.LPCSTR,
                               _type.LPCSTR],
                              _type.LSTATUS]
    RegReplaceKeyW: _Callable[[_type.HKEY,
                               _Optional[_type.LPCWSTR],
                               _type.LPCWSTR,
                               _type.LPCWSTR],
                              _type.LSTATUS]
    RegRestoreKeyA: _Callable[[_type.HKEY,
                               _type.LPCSTR,
                               _type.DWORD],
                              _type.LSTATUS]
    RegRestoreKeyW: _Callable[[_type.HKEY,
                               _type.LPCWSTR,
                               _type.DWORD],
                              _type.LSTATUS]
    RegSaveKeyExA: _Callable[[_type.HKEY,
                              _type.LPCSTR,
                              _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                              _type.DWORD],
                             _type.LSTATUS]
    RegSaveKeyExW: _Callable[[_type.HKEY,
                              _type.LPCWSTR,
                              _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                              _type.DWORD],
                             _type.LSTATUS]
    RegUnLoadKeyA: _Callable[[_type.HKEY,
                              _Optional[_type.LPCSTR]],
                             _type.LSTATUS]
    RegUnLoadKeyW: _Callable[[_type.HKEY,
                              _Optional[_type.LPCWSTR]],
                             _type.LSTATUS]


# noinspection PyPep8Naming
class cfgmgr32(_Func, metaclass=_WinDLL):
    # Cfgmgr32
    CM_Get_DevNode_PropertyW: _Callable[[_type.DEVINST,
                                         _Pointer[_struct.DEVPROPKEY],
                                         _Pointer[_type.DEVPROPTYPE],
                                         _Optional[_type.PBYTE],
                                         _Pointer[_type.ULONG],
                                         _type.ULONG],
                                        _type.CONFIGRET]
    CM_Get_Device_Interface_PropertyW: _Callable[[_type.LPCWSTR,
                                                  _Pointer[_struct.DEVPROPKEY],
                                                  _Pointer[_type.DEVPROPTYPE],
                                                  _Optional[_type.PBYTE],
                                                  _Pointer[_type.ULONG],
                                                  _type.ULONG],
                                                 _type.CONFIGRET]
    CM_Locate_DevNodeA: _Callable[[_Pointer[_type.DEVINST],
                                   _type.PBYTE,
                                   _type.ULONG],
                                  _type.CONFIGRET]
    CM_Locate_DevNodeW: _Callable[[_Pointer[_type.DEVINST],
                                   _type.PWSTR,
                                   _type.ULONG],
                                  _type.CONFIGRET]


# noinspection PyPep8Naming
class combase(_Func, metaclass=_WinDLL):
    # roapi
    RoActivateInstance: _Callable[[_type.HSTRING,
                                   _Pointer[_interface.IInspectable]],
                                  _type.HRESULT]
    RoGetActivationFactory: _Callable[[_type.HSTRING,
                                       _Pointer[_struct.IID],
                                       _Pointer[_interface.IActivationFactory]],
                                      _type.HRESULT]
    RoGetApartmentIdentifier: _Callable[[_Pointer[_type.UINT64]],
                                        _type.HRESULT]
    RoInitialize: _Callable[[_enum.RO_INIT_TYPE],
                            _type.HRESULT]
    RoUninitialize: _Callable[[],
                              _type.c_void]
    # winstring
    WindowsConcatString: _Callable[[_Optional[_type.HSTRING],
                                    _Optional[_type.HSTRING],
                                    _Pointer[_type.HSTRING]],
                                   _type.HRESULT]
    WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH],
                                    _type.UINT32,
                                    _Pointer[_type.HSTRING]],
                                   _type.HRESULT]
    WindowsDeleteString: _Callable[[_type.HSTRING],
                                   _type.HRESULT]
    WindowsGetStringLen: _Callable[[_type.HSTRING],
                                   _type.UINT32]
    WindowsGetStringRawBuffer: _Callable[[_Optional[_type.HSTRING],
                                          _Optional[_Pointer[_type.UINT32]]],
                                         _type.PCWSTR]
    WindowsIsStringEmpty: _Callable[[_type.HSTRING],
                                    _type.BOOL]
    WindowsReplaceString: _Callable[[_Optional[_type.HSTRING],
                                     _Optional[_type.HSTRING],
                                     _Optional[_type.HSTRING],
                                     _Pointer[_type.HSTRING]],
                                    _type.HRESULT]
    WindowsTrimStringEnd: _Callable[[_Optional[_type.HSTRING],
                                     _Optional[_type.HSTRING],
                                     _Pointer[_type.HSTRING]],
                                    _type.HRESULT]
    WindowsTrimStringStart: _Callable[[_Optional[_type.HSTRING],
                                       _Optional[_type.HSTRING],
                                       _Pointer[_type.HSTRING]],
                                      _type.HRESULT]


# noinspection PyPep8Naming
class comctl32(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    # CommCtrl
    InitCommonControls: _Callable[[],
                                  _type.c_void]
    InitCommonControlsEx: _Callable[[_Pointer[_struct.INITCOMMONCONTROLSEX]],
                                    _type.BOOL]


# noinspection PyPep8Naming
class comdlg32(_Func, metaclass=_WinDLL):
    # commdlg
    ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]],
                            _type.BOOL]
    ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]],
                            _type.BOOL]


# noinspection PyPep8Naming
class computecore(_Func, metaclass=_WinDLL):
    # computecore
    HcsGetServiceProperties: _Callable[[_Optional[_type.PCWSTR],
                                        _Pointer[_type.PWSTR]],
                                       _type.HRESULT]
    HcsModifyServiceSettings: _Callable[[_type.PCWSTR,
                                         _Optional[_Pointer[_type.PWSTR]]],
                                        _type.HRESULT]
    HcsSubmitWerReport: _Callable[[_type.PCWSTR],
                                  _type.HRESULT]
    HcsCreateEmptyGuestStateFile: _Callable[[_type.PCWSTR],
                                            _type.HRESULT]
    HcsCreateEmptyRuntimeStateFile: _Callable[[_type.PCWSTR],
                                              _type.HRESULT]
    HcsGrantVmAccess: _Callable[[_type.PCWSTR,
                                 _type.PCWSTR],
                                _type.HRESULT]
    HcsRevokeVmAccess: _Callable[[_type.PCWSTR,
                                  _type.PCWSTR],
                                 _type.HRESULT]
    HcsGrantVmGroupAccess: _Callable[[_type.PCWSTR],
                                     _type.HRESULT]
    HcsRevokeVmGroupAccess: _Callable[[_type.PCWSTR],
                                      _type.HRESULT]


# noinspection PyPep8Naming
class crypt32(_Func, metaclass=_WinDLL):
    # wincrypt
    CryptBinaryToStringA: _Callable[[_Pointer[_type.BYTE],
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Optional[_Pointer[_type.LPSTR]],
                                     _Pointer[_type.DWORD]],
                                    _type.BOOL]
    CryptBinaryToStringW: _Callable[[_Pointer[_type.BYTE],
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Optional[_Pointer[_type.LPWSTR]],
                                     _Pointer[_type.DWORD]],
                                    _type.BOOL]
    CryptStringToBinaryA: _Callable[[_type.LPCSTR,
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Pointer[_type.BYTE],
                                     _Pointer[_type.DWORD],
                                     _Optional[_Pointer[_type.DWORD]],
                                     _Optional[_Pointer[_type.DWORD]]],
                                    _type.BOOL]
    CryptStringToBinaryW: _Callable[[_type.LPCWSTR,
                                     _type.DWORD,
                                     _type.DWORD,
                                     _Pointer[_type.BYTE],
                                     _Pointer[_type.DWORD],
                                     _Optional[_Pointer[_type.DWORD]],
                                     _Optional[_Pointer[_type.DWORD]]],
                                    _type.BOOL]


# noinspection PyPep8Naming
class d2d1(_Func, metaclass=_WinDLL):
    # d2d1
    D2D1CreateFactory: _Callable[[_enum.D2D1_FACTORY_TYPE,  # factoryType
                                  _Pointer[_struct.IID],  # riid
                                  _Optional[_Pointer[_struct.D2D1_FACTORY_OPTIONS]],  # pFactoryOptions
                                  _type.c_void_p],  # ppIFactory
                                 _type.HRESULT]
    D2D1MakeRotateMatrix: _Callable[[_type.FLOAT,  # angle
                                     _struct.D2D1_POINT_2F,  # center
                                     _Pointer[_struct.D2D1_POINT_2F]],  # matrix
                                    _type.c_void]
    D2D1MakeSkewMatrix: _Callable[[_type.FLOAT,  # angleX
                                   _type.FLOAT,  # angleY
                                   _struct.D2D1_POINT_2F,  # center
                                   _Pointer[_struct.D2D1_MATRIX_3X2_F]],  # matrix
                                  _type.c_void]
    D2D1IsMatrixInvertible: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # matrix
                                      _type.BOOL]
    D2D1InvertMatrix: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # matrix
                                _type.BOOL]
    # d2d1_1
    D2D1CreateDeviceContext: _Callable[[_interface.IDXGISurface,  # dxgiSurface
                                        _Optional[_Pointer[_struct.D2D1_CREATION_PROPERTIES]],  # creationProperties
                                        _Pointer[_interface.ID2D1DeviceContext]],  # d2dDeviceContext
                                       _type.HRESULT]
    D2D1SinCos: _Callable[[_type.FLOAT,  # angle
                           _Pointer[_type.FLOAT],  # s
                           _Pointer[_type.FLOAT]],  # c
                          _type.c_void]
    D2D1Tan: _Callable[[_type.FLOAT],  # angle
                       _type.FLOAT]
    D2D1Vec3Length: _Callable[[_type.FLOAT,  # x
                               _type.FLOAT,  # y
                               _type.FLOAT],  # z
                              _type.FLOAT]


# noinspection PyPep8Naming
class d3d11(_Func, metaclass=_WinDLL):
    # d3d11
    D3D11CreateDevice: _Callable[[_Optional[_interface.IDXGIAdapter],  # pAdapter
                                  _enum.D3D_DRIVER_TYPE,  # DriverType
                                  _type.HMODULE,  # Software
                                  _type.UINT,  # Flags
                                  _Optional[_Pointer[_enum.D3D_FEATURE_LEVEL]],  # pFeatureLevels
                                  _type.UINT,  # FeatureLevels
                                  _type.UINT,  # SDKVersion
                                  _Optional[_Pointer[_interface.ID3D11Device]],  # ppDevice
                                  _Optional[_Pointer[_enum.D3D_FEATURE_LEVEL]],  # pFeatureLevel,
                                  _Optional[_Pointer[_interface.ID3D11DeviceContext]]],  # ppImmediateContext
                                 _type.HRESULT]


class DWrite(_Func, metaclass=_WinDLL):
    # dwrite
    DWriteCreateFactory: _Callable[[_enum.DWRITE_FACTORY_TYPE,  # factoryType
                                    _Pointer[_struct.IID],  # iid
                                    _Pointer[_interface.IUnknown]],  # factory
                                   _type.HRESULT]


# noinspection PyPep8Naming
class dwmapi(_Func, metaclass=_WinDLL):
    # dwmapi
    DwmDefWindowProc: _Callable[[_type.HWND,
                                 _type.UINT,
                                 _type.WPARAM,
                                 _type.LPARAM,
                                 _Pointer[_type.LRESULT]],
                                _type.BOOL]
    DwmEnableComposition: _Callable[[_type.UINT],
                                    _type.HRESULT]
    DwmEnableMMCSS: _Callable[[_type.BOOL],
                              _type.HRESULT]
    DwmExtendFrameIntoClientArea: _Callable[[_type.HWND,
                                             _Pointer[_struct.MARGINS]],
                                            _type.HRESULT]
    DwmGetColorizationColor: _Callable[[_Pointer[_type.DWORD],
                                        _Pointer[_type.BOOL]],
                                       _type.HRESULT]
    DwmGetWindowAttribute: _Callable[[_type.HWND,
                                      _type.DWORD,
                                      _type.PVOID,
                                      _type.DWORD],
                                     _type.HRESULT]
    DwmIsCompositionEnabled: _Callable[[_Pointer[_type.BOOL]],
                                       _type.HRESULT]
    DwmModifyPreviousDxFrameDuration: _Callable[[_type.HWND,
                                                 _type.INT,
                                                 _type.BOOL],
                                                _type.HRESULT]
    DwmRegisterThumbnail: _Callable[[_type.HWND,
                                     _type.HWND,
                                     _Pointer[_type.HTHUMBNAIL]],
                                    _type.HRESULT]
    DwmSetDxFrameDuration: _Callable[[_type.HWND,
                                      _type.INT],
                                     _type.HRESULT]
    DwmSetWindowAttribute: _Callable[[_type.HWND,
                                      _type.DWORD,
                                      _type.LPCVOID,
                                      _type.DWORD],
                                     _type.HRESULT]
    DwmUnregisterThumbnail: _Callable[[_type.HTHUMBNAIL],
                                      _type.HRESULT]


# noinspection PyPep8Naming
class gdi32(_Func, metaclass=_WinDLL):
    # wingdi
    CombineRgn: _Callable[[_type.HRGN,  # hrgnDst
                           _type.HRGN,  # hrgnSrc1
                           _type.HRGN,  # hrgnSrc2
                           _type.c_int],  # iMode
                          _type.c_int]
    CreateRectRgn: _Callable[[_type.c_int,  # x1
                              _type.c_int,  # y1
                              _type.c_int,  # x2
                              _type.c_int],  # y2
                             _type.HRGN]
    CreateRectRgnIndirect: _Callable[[_Pointer[_struct.RECT]],  # lprect
                                     _type.HRGN]
    CreateRoundRectRgn: _Callable[[_type.c_int,  # x1
                                   _type.c_int,  # y1
                                   _type.c_int,  # x2
                                   _type.c_int,  # y2
                                   _type.c_int,  # w
                                   _type.c_int],  # h
                                  _type.HRGN]
    EqualRgn: _Callable[[_type.HRGN,  # hrgn1
                         _type.HRGN],  # hrgn2
                        _type.BOOL]
    ExcludeClipRect: _Callable[[_type.HDC,  # hdc
                                _type.c_int,  # left
                                _type.c_int,  # top
                                _type.c_int,  # right
                                _type.c_int],  # bottom
                               _type.c_int]
    ExtFloodFill: _Callable[[_type.HDC,  # hdc
                             _type.c_int,  # x
                             _type.c_int,  # y
                             _type.COLORREF,  # color
                             _type.UINT],  # type
                            _type.BOOL]
    FillRgn: _Callable[[_type.HDC,  # hdc
                        _type.HRGN,  # hrgn
                        _type.HBRUSH],  # hbr
                       _type.BOOL]
    FloodFill: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # x
                          _type.c_int,  # y
                          _type.COLORREF],  # color
                         _type.BOOL]
    FrameRgn: _Callable[[_type.HDC,  # hdc
                         _type.HRGN,  # hrgn
                         _type.HBRUSH,  # hbr
                         _type.c_int,  # w
                         _type.c_int],  # h
                        _type.BOOL]
    GetROP2: _Callable[[_type.HDC],  # hdc
                       _type.c_int]
    GetBkColor: _Callable[[_type.HDC],  # hdc
                          _type.COLORREF]
    GetDCBrushColor: _Callable[[_type.HDC],  # hdc
                               _type.COLORREF]
    GetDCPenColor: _Callable[[_type.HDC],  # hdc
                             _type.COLORREF]
    RectVisible: _Callable[[_type.HDC,  # hdc
                            _Pointer[_struct.RECT]],  # lprect
                           _type.BOOL]
    Rectangle: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # left
                          _type.c_int,  # top
                          _type.c_int,  # right
                          _type.c_int],  # bottom
                         _type.BOOL]
    # TODO
    AbortDoc: _Callable[[_type.HDC],
                        _type.c_int]
    AbortPath: _Callable[[_type.HDC],
                         _type.BOOL]
    ArcTo: _Callable[[_type.HDC,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int,
                      _type.c_int],
                     _type.BOOL]
    BeginPath: _Callable[[_type.HDC],
                         _type.BOOL]
    BitBlt: _Callable[[_type.HDC,
                       _type.c_int,
                       _type.c_int,
                       _type.c_int,
                       _type.c_int,
                       _type.HDC,
                       _type.c_int,
                       _type.c_int,
                       _type.DWORD],
                      _type.BOOL]
    CloseFigure: _Callable[[_type.HDC],
                           _type.BOOL]
    CreateBitmap: _Callable[[_type.c_int,
                             _type.c_int,
                             _type.UINT,
                             _type.UINT,
                             _Optional[_type.VOID]],
                            _type.HBITMAP]
    CreateCompatibleBitmap: _Callable[[_type.HDC,
                                       _type.c_int,
                                       _type.c_int],
                                      _type.HBITMAP]
    CreateCompatibleDC: _Callable[[_Optional[_type.HDC]],
                                  _type.HDC]
    CreateDIBitmap: _Callable[[_type.HDC,
                               _Pointer[_struct.BITMAPINFOHEADER],
                               _type.DWORD,
                               _type.VOID,
                               _Pointer[_struct.BITMAPINFO],
                               _type.UINT],
                              _type.HBITMAP]
    CreateDIBSection: _Callable[[_type.HDC,
                                 _Pointer[_struct.BITMAPINFOHEADER],
                                 _type.UINT,
                                 _Optional[_type.VOID],
                                 _Optional[_type.HANDLE],
                                 _type.DWORD],
                                _type.HBITMAP]
    CreateDiscardableBitmap: _Callable[[_type.HDC,
                                        _type.c_int,
                                        _type.c_int],
                                       _type.HBITMAP]
    CreateHalftonePalette: _Callable[[_type.HDC],
                                     _type.HPALETTE]
    CreateSolidBrush: _Callable[[_type.COLORREF],
                                _type.HBRUSH]
    DeleteDC: _Callable[[_type.HDC],
                        _type.BOOL]
    DeleteMetaFile: _Callable[[_type.HMETAFILE],
                              _type.BOOL]
    DeleteObject: _Callable[[_type.HGDIOBJ],
                            _type.BOOL]
    EndDoc: _Callable[[_type.HDC],
                      _type.c_int]
    EndPath: _Callable[[_type.HDC],
                       _type.BOOL]
    EndPage: _Callable[[_type.HDC],
                       _type.c_int]
    ExtCreatePen: _Callable[[_type.DWORD,
                             _type.DWORD,
                             _Pointer[_struct.LOGBRUSH],
                             _type.DWORD,
                             _Optional[_Pointer[_type.DWORD]]],
                            _type.HPEN]
    FillPath: _Callable[[_type.HDC],
                        _type.BOOL]
    FlattenPath: _Callable[[_type.HDC],
                           _type.BOOL]
    GetArcDirection: _Callable[[_type.HDC],
                               _type.c_int]
    GetBitmapDimensionEx: _Callable[[_type.HBITMAP,
                                     _Pointer[_struct.SIZE]],
                                    _type.BOOL]
    GetBkColor: _Callable[[_type.HDC],
                          _type.COLORREF]
    GetBkMode: _Callable[[_type.HDC],
                         _type.c_int]
    GetClipBox: _Callable[[_type.HDC,
                           _Pointer[_struct.RECT]],
                          _type.c_int]
    GetColorAdjustment: _Callable[[_type.HDC,
                                   _Pointer[_struct.COLORADJUSTMENT]],
                                  _type.BOOL]
    GetDIBits: _Callable[[_type.HDC,
                          _type.HBITMAP,
                          _type.UINT,
                          _type.UINT,
                          _Optional[_type.LPVOID],
                          _Pointer[_struct.BITMAPINFO],
                          _type.UINT],
                         _type.c_int]
    GdiFlush: _Callable[[],
                        _type.BOOL]
    GetGraphicsMode: _Callable[[_type.HDC],
                               _type.c_int]
    GetMapMode: _Callable[[_type.HDC],
                          _type.c_int]
    GetMetaFileA: _Callable[[_type.LPCSTR],
                            _type.HMETAFILE]
    GetMetaFileW: _Callable[[_type.LPCWSTR],
                            _type.HMETAFILE]
    GetMiterLimit: _Callable[[_type.HDC,
                              _Pointer[_type.FLOAT]],
                             _type.BOOL]
    GetObjectA: _Callable[[_type.HANDLE,
                           _type.c_int,
                           _type.LPVOID],
                          _type.c_int]
    GetObjectW: _Callable[[_type.HANDLE,
                           _type.c_int,
                           _type.LPVOID],
                          _type.c_int]
    GetObjectType: _Callable[[_type.HGDIOBJ],
                             _type.DWORD]
    GetPath: _Callable[[_type.HDC,
                        _Pointer[_struct.POINT],
                        _Pointer[_type.BYTE],
                        _type.c_int],
                       _type.c_int]
    GetPixel: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int],
                        _type.COLORREF]
    GetPixelFormat: _Callable[[_type.HDC],
                              _type.c_int]
    GetPolyFillMode: _Callable[[_type.HDC],
                               _type.c_int]
    GetRandomRgn: _Callable[[_type.HDC,
                             _type.HRGN,
                             _type.INT],
                            _type.c_int]
    GetRgnBox: _Callable[[_type.HRGN,
                          _Pointer[_struct.RECT]],
                         _type.c_int]
    GetROP2: _Callable[[_type.HDC],
                       _type.c_int]
    GetStockObject: _Callable[[_type.c_int],
                              _type.HGDIOBJ]
    GetStretchBltMode: _Callable[[_type.HDC],
                                 _type.c_int]
    GdiGetBatchLimit: _Callable[[],
                                _type.DWORD]
    GdiSetBatchLimit: _Callable[[_type.DWORD],
                                _type.DWORD]
    MoveToEx: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int,
                         _Pointer[_struct.POINT]],
                        _type.BOOL]
    PathToRegion: _Callable[[_type.HDC],
                            _type.HRGN]
    PolyDraw: _Callable[[_type.HDC,
                         _Pointer[_struct.POINT],
                         _Pointer[_type.BYTE],
                         _type.c_int],
                        _type.BOOL]
    SelectClipPath: _Callable[[_type.HDC,
                               _type.c_int],
                              _type.BOOL]
    SelectObject: _Callable[[_type.HDC,
                             _type.HGDIOBJ],
                            _type.HGDIOBJ]
    SetAbortProc: _Callable[[_type.HDC,
                             _type.ABORTPROC],
                            _type.c_int]
    SetArcDirection: _Callable[[_type.HDC,
                                _type.c_int],
                               _type.c_int]
    SetBkColor: _Callable[[_type.HDC,
                           _type.COLORREF],
                          _type.COLORREF]
    SetColorAdjustment: _Callable[[_type.HDC,
                                   _Pointer[_struct.COLORADJUSTMENT]],
                                  _type.BOOL]
    SetDCBrushColor: _Callable[[_type.HDC,
                                _type.COLORREF],
                               _type.COLORREF]
    SetDCPenColor: _Callable[[_type.HDC,
                              _type.COLORREF],
                             _type.COLORREF]
    SetMiterLimit: _Callable[[_type.HDC,
                              _type.FLOAT,
                              _Optional[_Pointer[_type.FLOAT]]],
                             _type.BOOL]
    SetStretchBltMode: _Callable[[_type.HDC,
                                  _type.c_int],
                                 _type.c_int]
    StartPage: _Callable[[_type.HDC],
                         _type.c_int]
    StretchBlt: _Callable[[_type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.DWORD],
                          _type.BOOL]
    StrokeAndFillPath: _Callable[[_type.HDC],
                                 _type.BOOL]
    StrokePath: _Callable[[_type.HDC],
                          _type.BOOL]
    WidenPath: _Callable[[_type.HDC],
                         _type.BOOL]
    TextOutA: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int,
                         _type.LPCSTR,
                         _type.c_int],
                        _type.BOOL]
    TextOutW: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int,
                         _type.LPCWSTR,
                         _type.c_int],
                        _type.BOOL]
    TransparentBlt: _Callable[[_type.HDC,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.HDC,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.UINT],
                              _type.BOOL]


class GdiPlus(_Func, metaclass=_WinDLL):
    # gdipluseffects
    GdipCreateEffect: _Callable[[_struct.GUID,  # guid
                                 _Pointer[_type.CGpEffect]],  # effect
                                _enum.Status]
    GdipDeleteEffect: _Callable[[_type.CGpEffect],  # effect
                                _enum.Status]
    GdipGetEffectParameterSize: _Callable[[_type.CGpEffect,  # effect
                                           _Pointer[_type.UINT]],  # size
                                          _enum.Status]
    GdipSetEffectParameters: _Callable[[_type.CGpEffect,  # effect
                                        _type.PVOID,  # params
                                        _type.UINT],  # size
                                       _enum.Status]
    GdipGetEffectParameters: _Callable[[_type.CGpEffect,  # effect
                                        _type.UINT,  # size
                                        _type.PVOID],  # params
                                       _enum.Status]
    # gdiplusflat
    GdipCreatePath: _Callable[[_enum.GpFillMode,  # brushMode
                               _Pointer[_type.GpPath]],  # path
                              _enum.GpStatus]
    GdipCreatePath2: _Callable[[_Pointer[_struct.GpPointF],  # points
                                _Pointer[_type.BYTE],  # types
                                _type.INT,  # count
                                _enum.GpFillMode,  # fillMode
                                _Pointer[_type.GpPath]],  # path
                               _enum.GpStatus]
    GdipCreatePath2I: _Callable[[_Pointer[_struct.GpPoint],  # points
                                 _Pointer[_type.BYTE],  # types
                                 _type.INT,  # count
                                 _enum.GpFillMode,  # fillMode
                                 _Pointer[_type.GpPath]],  # path
                                _enum.GpStatus]
    GdipClonePath: _Callable[[_type.GpPath,  # path
                              _Pointer[_type.GpPath]],  # clonePath
                             _enum.GpStatus]
    GdipDeletePath: _Callable[[_type.GpPath],  # path
                              _enum.GpStatus]
    GdipResetPath: _Callable[[_type.GpPath],  # path
                             _enum.GpStatus]
    GdipGetPointCount: _Callable[[_type.GpPath,  # path
                                  _Pointer[_type.INT]],  # count
                                 _enum.GpStatus]
    GdipGetPathTypes: _Callable[[_type.GpPath,  # path
                                 _Pointer[_type.BYTE],  # types
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipGetPathPoints: _Callable[[_type.GpPath,  # GpPath*
                                  _Pointer[_struct.GpPointF],  # points
                                  _type.INT],  # count
                                 _enum.GpStatus]
    GdipGetPathPointsI: _Callable[[_type.GpPath,  # GpPath*
                                   _Pointer[_struct.GpPoint],  # points
                                   _type.INT],  # count
                                  _enum.GpStatus]
    GdipGetPathFillMode: _Callable[[_type.GpPath,  # path
                                    _Pointer[_enum.GpFillMode]],  # fillmode
                                   _enum.GpStatus]
    GdipSetPathFillMode: _Callable[[_type.GpPath,  # path
                                    _enum.GpFillMode],  # fillmode
                                   _enum.GpStatus]
    GdipGetPathData: _Callable[[_type.GpPath,  # path
                                _Pointer[_struct.GpPathData]],  # pathData
                               _enum.GpStatus]
    GdipStartPathFigure: _Callable[[_type.GpPath],  # path
                                   _enum.GpStatus]
    GdipClosePathFigure: _Callable[[_type.GpPath],  # path
                                   _enum.GpStatus]
    GdipClosePathFigures: _Callable[[_type.GpPath],  # path
                                    _enum.GpStatus]
    GdipSetPathMarker: _Callable[[_type.GpPath],  # path
                                 _enum.GpStatus]
    GdipClearPathMarkers: _Callable[[_type.GpPath],  # path
                                    _enum.GpStatus]
    GdipReversePath: _Callable[[_type.GpPath],  # path
                               _enum.GpStatus]
    GdipGetPathLastPoint: _Callable[[_type.GpPath,  # path
                                     _Pointer[_struct.GpPointF]],  # lastPoint
                                    _enum.GpStatus]
    GdipAddPathLine: _Callable[[_type.GpPath,  # path
                                _type.REAL,  # x1
                                _type.REAL,  # y1
                                _type.REAL,  # x2
                                _type.REAL],  # y2
                               _enum.GpStatus]
    GdipAddPathLine2: _Callable[[_type.GpPath,  # path
                                 _Pointer[_struct.GpPointF],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipAddPathArc: _Callable[[_type.GpPath,  # path
                               _type.REAL,  # x
                               _type.REAL,  # y
                               _type.REAL,  # width
                               _type.REAL,  # height
                               _type.REAL,  # startAngle
                               _type.REAL],  # sweepAngle
                              _enum.GpStatus]
    GdipAddPathBezier: _Callable[[_type.GpPath,  # path
                                  _type.REAL,  # x1
                                  _type.REAL,  # y1
                                  _type.REAL,  # x2
                                  _type.REAL,  # y2
                                  _type.REAL,  # x3
                                  _type.REAL,  # y3
                                  _type.REAL,  # x4
                                  _type.REAL],  # y4
                                 _enum.GpStatus]
    GdipAddPathBeziers: _Callable[[_type.GpPath,  # path
                                   _Pointer[_struct.GpPointF],  # points
                                   _type.INT],  # count
                                  _enum.GpStatus]
    GdipAddPathCurve: _Callable[[_type.GpPath,  # path
                                 _Pointer[_struct.GpPointF],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipAddPathCurve2: _Callable[[_type.GpPath,  # path
                                  _Pointer[_struct.GpPointF],  # points
                                  _type.INT,  # count
                                  _type.REAL],  # tension
                                 _enum.GpStatus]
    GdipAddPathCurve3: _Callable[[_type.GpPath,  # path
                                  _Pointer[_struct.GpPointF],  # points
                                  _type.INT,  # count
                                  _type.INT,  # offset
                                  _type.INT,  # numberOfSegments
                                  _type.REAL],  # tension
                                 _enum.GpStatus]
    GdipAddPathClosedCurve: _Callable[[_type.GpPath,  # path
                                       _Pointer[_struct.GpPointF],  # points
                                       _type.INT],  # count
                                      _enum.GpStatus]
    GdipAddPathClosedCurve2: _Callable[[_type.GpPath,  # path
                                        _Pointer[_struct.GpPointF],  # points
                                        _type.INT,  # count
                                        _type.REAL],  # tension
                                       _enum.GpStatus]
    GdipAddPathRectangle: _Callable[[_type.GpPath,  # path
                                     _type.REAL,  # x
                                     _type.REAL,  # y
                                     _type.REAL,  # width
                                     _type.REAL],  # height
                                    _enum.GpStatus]
    GdipAddPathRectangles: _Callable[[_type.GpPath,  # path
                                      _Pointer[_struct.GpRectF],  # rects
                                      _type.INT],  # count
                                     _enum.GpStatus]
    GdipAddPathEllipse: _Callable[[_type.GpPath,  # path
                                   _type.REAL,  # x
                                   _type.REAL,  # y
                                   _type.REAL,  # width
                                   _type.REAL],  # height
                                  _enum.GpStatus]
    GdipAddPathPie: _Callable[[_type.GpPath,  # path
                               _type.REAL,  # x
                               _type.REAL,  # y
                               _type.REAL,  # width
                               _type.REAL,  # height
                               _type.REAL,  # startAngle
                               _type.REAL],  # sweepAngle
                              _enum.GpStatus]
    GdipAddPathPolygon: _Callable[[_type.GpPath,  # path
                                   _Pointer[_struct.GpPointF],  # points
                                   _type.INT],  # count
                                  _enum.GpStatus]
    GdipAddPathPath: _Callable[[_type.GpPath,  # path
                                _type.GpPath,  # addingPath
                                _type.BOOL],  # connect
                               _enum.GpStatus]
    GdipAddPathString: _Callable[[_type.GpPath,  # path
                                  _type.LPWSTR,  # string
                                  _type.INT,  # length
                                  _type.GpFontFamily,  # family
                                  _type.INT,  # style
                                  _type.REAL,  # emSize
                                  _Pointer[_struct.RectF],  # layoutRect
                                  _type.GpStringFormat],  # format
                                 _enum.GpStatus]
    GdipAddPathStringI: _Callable[[_type.GpPath,  # path
                                   _type.LPWSTR,  # string
                                   _type.INT,  # length
                                   _type.GpFontFamily,  # family
                                   _type.INT,  # style
                                   _type.REAL,  # emSize
                                   _Pointer[_struct.Rect],  # layoutRect
                                   _type.GpStringFormat],  # format
                                  _enum.GpStatus]
    GdipAddPathLineI: _Callable[[_type.GpPath,  # path
                                 _type.INT,  # x1
                                 _type.INT,  # y1
                                 _type.INT,  # x2
                                 _type.INT],  # y2
                                _enum.GpStatus]
    GdipAddPathLine2I: _Callable[[_type.GpPath,  # path
                                  _Pointer[_struct.GpPoint],  # points
                                  _type.INT],  # count
                                 _enum.GpStatus]
    GdipAddPathArcI: _Callable[[_type.GpPath,  # path
                                _type.INT,  # x
                                _type.INT,  # y
                                _type.INT,  # width
                                _type.INT,  # height
                                _type.REAL,  # startAngle
                                _type.REAL],  # sweepAngle
                               _enum.GpStatus]
    GdipAddPathBezierI: _Callable[[_type.GpPath,  # path
                                   _type.INT,  # x1
                                   _type.INT,  # y1
                                   _type.INT,  # x2
                                   _type.INT,  # y2
                                   _type.INT,  # x3
                                   _type.INT,  # y3
                                   _type.INT,  # x4
                                   _type.INT],  # y4
                                  _enum.GpStatus]
    GdipAddPathBeziersI: _Callable[[_type.GpPath,  # path
                                    _Pointer[_struct.GpPoint],  # points
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipAddPathCurveI: _Callable[[_type.GpPath,  # path
                                  _Pointer[_struct.GpPoint],  # points
                                  _type.INT],  # count
                                 _enum.GpStatus]
    GdipAddPathCurve2I: _Callable[[_type.GpPath,  # path
                                   _Pointer[_struct.GpPoint],  # points
                                   _type.INT,  # count
                                   _type.REAL],  # tension
                                  _enum.GpStatus]
    GdipAddPathCurve3I: _Callable[[_type.GpPath,  # path
                                   _Pointer[_struct.GpPoint],  # points
                                   _type.INT,  # count
                                   _type.INT,  # offset
                                   _type.INT,  # numberOfSegments
                                   _type.REAL],  # tension
                                  _enum.GpStatus]
    GdipAddPathClosedCurveI: _Callable[[_type.GpPath,  # path
                                        _Pointer[_struct.GpPoint],  # points
                                        _type.INT],  # count
                                       _enum.GpStatus]
    GdipAddPathClosedCurve2I: _Callable[[_type.GpPath,  # path
                                         _Pointer[_struct.GpPoint],  # points
                                         _type.INT,  # count
                                         _type.REAL],  # tension
                                        _enum.GpStatus]
    GdipAddPathRectangleI: _Callable[[_type.GpPath,  # path
                                      _type.INT,  # x
                                      _type.INT,  # y
                                      _type.INT,  # width
                                      _type.INT],  # height
                                     _enum.GpStatus]
    GdipAddPathRectanglesI: _Callable[[_type.GpPath,  # path
                                       _Pointer[_struct.GpRect],  # rects
                                       _type.INT],  # count
                                      _enum.GpStatus]
    GdipAddPathEllipseI: _Callable[[_type.GpPath,  # path
                                    _type.INT,  # x
                                    _type.INT,  # y
                                    _type.INT,  # width
                                    _type.INT],  # height
                                   _enum.GpStatus]
    GdipAddPathPieI: _Callable[[_type.GpPath,  # path
                                _type.INT,  # x
                                _type.INT,  # y
                                _type.INT,  # width
                                _type.INT,  # height
                                _type.REAL,  # startAngle
                                _type.REAL],  # sweepAngle
                               _enum.GpStatus]
    GdipAddPathPolygonI: _Callable[[_type.GpPath,  # path
                                    _Pointer[_struct.GpPoint],  # points
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipFlattenPath: _Callable[[_type.GpPath,  # path
                                _type.GpMatrix,  # matrix
                                _type.REAL],  # flatness
                               _enum.GpStatus]
    GdipWindingModeOutline: _Callable[[_type.GpPath,  # path
                                       _type.GpMatrix,  # matrix
                                       _type.REAL],  # flatness
                                      _enum.GpStatus]
    GdipWidenPath: _Callable[[_type.GpPath,  # nativePath
                              _type.GpPen,  # pen
                              _type.GpMatrix,  # matrix
                              _type.REAL],  # flatness
                             _enum.GpStatus]
    GdipWarpPath: _Callable[[_type.GpPath,  # path
                             _type.GpMatrix,  # matrix
                             _Pointer[_struct.GpPointF],  # points
                             _type.INT,  # count
                             _type.REAL,  # srcx
                             _type.REAL,  # srcy
                             _type.REAL,  # srcwidth
                             _type.REAL,  # srcheight
                             _enum.WarpMode,  # warpMode
                             _type.REAL],  # flatness
                            _enum.GpStatus]
    GdipTransformPath: _Callable[[_type.GpPath,  # path
                                  _type.GpMatrix],  # matrix
                                 _enum.GpStatus]
    GdipGetPathWorldBounds: _Callable[[_type.GpPath,  # path
                                       _Pointer[_struct.GpRectF],  # bounds
                                       _type.GpMatrix,  # matrix
                                       _type.GpPen],  # pen
                                      _enum.GpStatus]
    GdipGetPathWorldBoundsI: _Callable[[_type.GpPath,  # path
                                        _Pointer[_struct.GpRect],  # bounds
                                        _type.GpMatrix,  # matrix
                                        _type.GpPen],  # pen
                                       _enum.GpStatus]
    GdipIsVisiblePathPoint: _Callable[[_type.GpPath,  # path
                                       _type.REAL,  # x
                                       _type.REAL,  # y
                                       _type.GpGraphics,  # graphics
                                       _Pointer[_type.BOOL]],  # result
                                      _enum.GpStatus]
    GdipIsVisiblePathPointI: _Callable[[_type.GpPath,  # path
                                        _type.INT,  # x
                                        _type.INT,  # y
                                        _type.GpGraphics,  # graphics
                                        _Pointer[_type.BOOL]],  # result
                                       _enum.GpStatus]
    GdipIsOutlineVisiblePathPoint: _Callable[[_type.GpPath,  # path
                                              _type.REAL,  # x
                                              _type.REAL,  # y
                                              _type.GpPen,  # pen
                                              _type.GpGraphics,  # graphics
                                              _Pointer[_type.BOOL]],  # result
                                             _enum.GpStatus]
    GdipIsOutlineVisiblePathPointI: _Callable[[_type.GpPath,  # path
                                               _type.INT,  # x
                                               _type.INT,  # y
                                               _type.GpPen,  # pen
                                               _type.GpGraphics,  # graphics
                                               _Pointer[_type.BOOL]],  # result
                                              _enum.GpStatus]
    GdipCreatePathIter: _Callable[[_Pointer[_type.GpPathIterator],  # iterator
                                   _type.GpPath],  # path
                                  _enum.GpStatus]
    GdipDeletePathIter: _Callable[[_type.GpPathIterator],  # iterator
                                  _enum.GpStatus]
    GdipPathIterNextSubpath: _Callable[[_type.GpPathIterator,  # iterator
                                        _Pointer[_type.INT],  # resultCount
                                        _Pointer[_type.INT],  # startIndex
                                        _Pointer[_type.INT],  # endIndex
                                        _Pointer[_type.BOOL]],  # isClosed
                                       _enum.GpStatus]
    GdipPathIterNextSubpathPath: _Callable[[_type.GpPathIterator,  # iterator
                                            _Pointer[_type.INT],  # resultCount
                                            _type.GpPath,  # path
                                            _Pointer[_type.BOOL]],  # isClosed
                                           _enum.GpStatus]
    GdipPathIterNextPathType: _Callable[[_type.GpPathIterator,  # iterator
                                         _Pointer[_type.INT],  # resultCount
                                         _Pointer[_type.BYTE],  # pathType
                                         _Pointer[_type.INT],  # startIndex
                                         _Pointer[_type.INT]],  # endIndex
                                        _enum.GpStatus]
    GdipPathIterNextMarker: _Callable[[_type.GpPathIterator,  # iterator
                                       _Pointer[_type.INT],  # resultCount
                                       _Pointer[_type.INT],  # startIndex
                                       _Pointer[_type.INT]],  # endIndex
                                      _enum.GpStatus]
    GdipPathIterNextMarkerPath: _Callable[[_type.GpPathIterator,  # iterator
                                           _Pointer[_type.INT],  # resultCount
                                           _type.GpPath],  # path
                                          _enum.GpStatus]
    GdipPathIterGetCount: _Callable[[_type.GpPathIterator,  # iterator
                                     _Pointer[_type.INT]],  # count
                                    _enum.GpStatus]
    GdipPathIterGetSubpathCount: _Callable[[_type.GpPathIterator,  # iterator
                                            _Pointer[_type.INT]],  # count
                                           _enum.GpStatus]
    GdipPathIterIsValid: _Callable[[_type.GpPathIterator,  # iterator
                                    _Pointer[_type.BOOL]],  # valid
                                   _enum.GpStatus]
    GdipPathIterHasCurve: _Callable[[_type.GpPathIterator,  # iterator
                                     _Pointer[_type.BOOL]],  # hasCurve
                                    _enum.GpStatus]
    GdipPathIterRewind: _Callable[[_type.GpPathIterator],  # iterator
                                  _enum.GpStatus]
    GdipPathIterEnumerate: _Callable[[_type.GpPathIterator,  # iterator
                                      _Pointer[_type.INT],  # resultCount
                                      _Pointer[_struct.GpPointF],  # points
                                      _Pointer[_type.BYTE],  # types
                                      _type.INT],  # count
                                     _enum.GpStatus]
    GdipPathIterCopyData: _Callable[[_type.GpPathIterator,  # iterator
                                     _Pointer[_type.INT],  # resultCount
                                     _Pointer[_struct.GpPointF],  # points
                                     _Pointer[_type.BYTE],  # types
                                     _type.INT,  # startIndex
                                     _type.INT],  # endIndex
                                    _enum.GpStatus]
    GdipCreateMatrix: _Callable[[_Pointer[_type.GpMatrix]],  # matrix
                                _enum.GpStatus]
    GdipCreateMatrix2: _Callable[[_type.REAL,  # m11
                                  _type.REAL,  # m12
                                  _type.REAL,  # m21
                                  _type.REAL,  # m22
                                  _type.REAL,  # dx
                                  _type.REAL,  # dy
                                  _Pointer[_type.GpMatrix]],  # matrix
                                 _enum.GpStatus]
    GdipCreateMatrix3: _Callable[[_Pointer[_struct.GpRectF],  # rect
                                  _Pointer[_struct.GpPointF],  # dstplg
                                  _Pointer[_type.GpMatrix]],  # matrix
                                 _enum.GpStatus]
    GdipCreateMatrix3I: _Callable[[_Pointer[_struct.GpRect],  # rect
                                   _Pointer[_struct.GpPoint],  # dstplg
                                   _Pointer[_type.GpMatrix]],  # matrix
                                  _enum.GpStatus]
    GdipCloneMatrix: _Callable[[_type.GpMatrix,  # matrix
                                _Pointer[_type.GpMatrix]],  # cloneMatrix
                               _enum.GpStatus]
    GdipDeleteMatrix: _Callable[[_type.GpMatrix],  # matrix
                                _enum.GpStatus]
    GdipSetMatrixElements: _Callable[[_type.GpMatrix,  # matrix
                                      _type.REAL,  # m11
                                      _type.REAL,  # m12
                                      _type.REAL,  # m21
                                      _type.REAL,  # m22
                                      _type.REAL,  # dx
                                      _type.REAL],  # dy
                                     _enum.GpStatus]
    GdipMultiplyMatrix: _Callable[[_type.GpMatrix,  # matrix
                                   _type.GpMatrix,  # matrix2
                                   _enum.GpMatrixOrder],  # order
                                  _enum.GpStatus]
    GdipTranslateMatrix: _Callable[[_type.GpMatrix,  # matrix
                                    _type.REAL,  # offsetX
                                    _type.REAL,  # offsetY
                                    _enum.GpMatrixOrder],  # order
                                   _enum.GpStatus]
    GdipScaleMatrix: _Callable[[_type.GpMatrix,  # matrix
                                _type.REAL,  # scaleX
                                _type.REAL,  # scaleY
                                _enum.GpMatrixOrder],  # order
                               _enum.GpStatus]
    GdipRotateMatrix: _Callable[[_type.GpMatrix,  # matrix
                                 _type.REAL,  # angle
                                 _enum.GpMatrixOrder],  # order
                                _enum.GpStatus]
    GdipShearMatrix: _Callable[[_type.GpMatrix,  # matrix
                                _type.REAL,  # shearX
                                _type.REAL,  # shearY
                                _enum.GpMatrixOrder],  # order
                               _enum.GpStatus]
    GdipInvertMatrix: _Callable[[_type.GpMatrix],  # matrix
                                _enum.GpStatus]
    GdipTransformMatrixPoints: _Callable[[_type.GpMatrix,  # matrix
                                          _Pointer[_struct.GpPointF],  # pts
                                          _type.INT],  # count
                                         _enum.GpStatus]
    GdipTransformMatrixPointsI: _Callable[[_type.GpMatrix,  # matrix
                                           _Pointer[_struct.GpPoint],  # pts
                                           _type.INT],  # count
                                          _enum.GpStatus]
    GdipVectorTransformMatrixPoints: _Callable[[_type.GpMatrix,  # matrix
                                                _Pointer[_struct.GpPointF],  # pts
                                                _type.INT],  # count
                                               _enum.GpStatus]
    GdipVectorTransformMatrixPointsI: _Callable[[_type.GpMatrix,  # matrix
                                                 _Pointer[_struct.GpPoint],  # pts
                                                 _type.INT],  # count
                                                _enum.GpStatus]
    GdipGetMatrixElements: _Callable[[_type.GpMatrix,  # matrix
                                      _Pointer[_type.REAL]],  # matrixOut
                                     _enum.GpStatus]
    GdipIsMatrixInvertible: _Callable[[_type.GpMatrix,  # matrix
                                       _Pointer[_type.BOOL]],  # result
                                      _enum.GpStatus]
    GdipIsMatrixIdentity: _Callable[[_type.GpMatrix,  # matrix
                                     _Pointer[_type.BOOL]],  # result
                                    _enum.GpStatus]
    GdipIsMatrixEqual: _Callable[[_type.GpMatrix,  # matrix
                                  _type.GpMatrix,  # matrix2
                                  _Pointer[_type.BOOL]],  # result
                                 _enum.GpStatus]
    GdipCreateRegion: _Callable[[_Pointer[_type.GpRegion]],  # region
                                _enum.GpStatus]
    GdipCreateRegionRect: _Callable[[_Pointer[_struct.GpRectF],  # rect
                                     _Pointer[_type.GpRegion]],  # region
                                    _enum.GpStatus]
    GdipCreateRegionRectI: _Callable[[_Pointer[_struct.GpRect],  # rect
                                      _Pointer[_type.GpRegion]],  # region
                                     _enum.GpStatus]
    GdipCreateRegionPath: _Callable[[_type.GpPath,  # path
                                     _Pointer[_type.GpRegion]],  # region
                                    _enum.GpStatus]
    GdipCreateRegionRgnData: _Callable[[_Pointer[_type.BYTE],  # regionData
                                        _type.INT,  # size
                                        _Pointer[_type.GpRegion]],  # region
                                       _enum.GpStatus]
    GdipCreateRegionHrgn: _Callable[[_type.HRGN,  # hRgn
                                     _Pointer[_type.GpRegion]],  # region
                                    _enum.GpStatus]
    GdipCloneRegion: _Callable[[_type.GpRegion,  # region
                                _Pointer[_type.GpRegion]],  # cloneRegion
                               _enum.GpStatus]
    GdipDeleteRegion: _Callable[[_type.GpRegion],  # region
                                _enum.GpStatus]
    GdipSetInfinite: _Callable[[_type.GpRegion],  # region
                               _enum.GpStatus]
    GdipSetEmpty: _Callable[[_type.GpRegion],  # region
                            _enum.GpStatus]
    GdipCombineRegionRect: _Callable[[_type.GpRegion,  # region
                                      _Pointer[_struct.GpRectF],  # rect
                                      _enum.CombineMode],  # combineMode
                                     _enum.GpStatus]
    GdipCombineRegionRectI: _Callable[[_type.GpRegion,  # region
                                       _Pointer[_struct.GpRect],  # rect
                                       _enum.CombineMode],  # combineMode
                                      _enum.GpStatus]
    GdipCombineRegionPath: _Callable[[_type.GpRegion,  # region
                                      _type.GpPath,  # path
                                      _enum.CombineMode],  # combineMode
                                     _enum.GpStatus]
    GdipCombineRegionRegion: _Callable[[_type.GpRegion,  # region
                                        _type.GpRegion,  # region2
                                        _enum.CombineMode],  # combineMode
                                       _enum.GpStatus]
    GdipTranslateRegion: _Callable[[_type.GpRegion,  # region
                                    _type.REAL,  # dx
                                    _type.REAL],  # dy
                                   _enum.GpStatus]
    GdipTranslateRegionI: _Callable[[_type.GpRegion,  # region
                                     _type.INT,  # dx
                                     _type.INT],  # dy
                                    _enum.GpStatus]
    GdipTransformRegion: _Callable[[_type.GpRegion,  # region
                                    _type.GpMatrix],  # matrix
                                   _enum.GpStatus]
    GdipGetRegionBounds: _Callable[[_type.GpRegion,  # region
                                    _type.GpGraphics,  # graphics
                                    _Pointer[_struct.GpRectF]],  # rect
                                   _enum.GpStatus]
    GdipGetRegionBoundsI: _Callable[[_type.GpRegion,  # region
                                     _type.GpGraphics,  # graphics
                                     _Pointer[_struct.GpRect]],  # rect
                                    _enum.GpStatus]
    GdipGetRegionHRgn: _Callable[[_type.GpRegion,  # region
                                  _type.GpGraphics,  # graphics
                                  _Pointer[_type.HRGN]],  # hRgn
                                 _enum.GpStatus]
    GdipIsEmptyRegion: _Callable[[_type.GpRegion,  # region
                                  _type.GpGraphics,  # graphics
                                  _Pointer[_type.BOOL]],  # result
                                 _enum.GpStatus]
    GdipIsInfiniteRegion: _Callable[[_type.GpRegion,  # region
                                     _type.GpGraphics,  # graphics
                                     _Pointer[_type.BOOL]],  # result
                                    _enum.GpStatus]
    GdipIsEqualRegion: _Callable[[_type.GpRegion,  # region
                                  _type.GpRegion,  # region2
                                  _type.GpGraphics,  # graphics
                                  _Pointer[_type.BOOL]],  # result
                                 _enum.GpStatus]
    GdipGetRegionDataSize: _Callable[[_type.GpRegion,  # region
                                      _Pointer[_type.UINT]],  # bufferSize
                                     _enum.GpStatus]
    GdipGetRegionData: _Callable[[_type.GpRegion,  # region
                                  _Pointer[_type.BYTE],  # buffer
                                  _type.UINT,  # bufferSize
                                  _Optional[_Pointer[_type.UINT]]],  # sizeFilled
                                 _enum.GpStatus]
    GdipIsVisibleRegionPoint: _Callable[[_type.GpRegion,  # region
                                         _type.REAL,  # x
                                         _type.REAL,  # y
                                         _type.GpGraphics,  # graphics
                                         _Pointer[_type.BOOL]],  # result
                                        _enum.GpStatus]
    GdipIsVisibleRegionPointI: _Callable[[_type.GpRegion,  # region
                                          _type.INT,  # x
                                          _type.INT,  # y
                                          _type.GpGraphics,  # graphics
                                          _Pointer[_type.BOOL]],  # result
                                         _enum.GpStatus]
    GdipIsVisibleRegionRect: _Callable[[_type.GpRegion,  # region
                                        _type.REAL,  # x
                                        _type.REAL,  # y
                                        _type.REAL,  # width
                                        _type.REAL,  # height
                                        _type.GpGraphics,  # graphics
                                        _Pointer[_type.BOOL]],  # result
                                       _enum.GpStatus]
    GdipIsVisibleRegionRectI: _Callable[[_type.GpRegion,  # region
                                         _type.INT,  # x
                                         _type.INT,  # y
                                         _type.INT,  # width
                                         _type.INT,  # height
                                         _type.GpGraphics,  # graphics
                                         _Pointer[_type.BOOL]],  # result
                                        _enum.GpStatus]
    GdipGetRegionScansCount: _Callable[[_type.GpRegion,  # region
                                        _Pointer[_type.UINT],  # count
                                        _type.GpMatrix],  # matrix
                                       _enum.GpStatus]
    GdipGetRegionScans: _Callable[[_type.GpRegion,  # region
                                   _Pointer[_struct.GpRectF],  # rects
                                   _Pointer[_type.INT],  # count
                                   _type.GpMatrix],  # matrix
                                  _enum.GpStatus]
    GdipGetRegionScansI: _Callable[[_type.GpRegion,  # region
                                    _Pointer[_struct.GpRect],  # rects
                                    _Pointer[_type.INT],  # count
                                    _type.GpMatrix],  # matrix
                                   _enum.GpStatus]
    GdipCloneBrush: _Callable[[_type.GpBrush,  # brush
                               _Pointer[_type.GpBrush]],  # cloneBrush
                              _enum.GpStatus]
    GdipDeleteBrush: _Callable[[_type.GpBrush],  # brush
                               _enum.GpStatus]
    GdipGetBrushType: _Callable[[_type.GpBrush,  # brush
                                 _Pointer[_enum.GpBrushType]],  # type
                                _enum.GpStatus]
    GdipCreateHatchBrush: _Callable[[_enum.GpHatchStyle,  # hatchstyle
                                     _type.ARGB,  # forecol
                                     _type.ARGB,  # backcol
                                     _Pointer[_type.GpHatch]],  # brush
                                    _enum.GpStatus]
    GdipGetHatchStyle: _Callable[[_type.GpHatch,  # brush
                                  _Pointer[_enum.GpHatchStyle]],  # hatchstyle
                                 _enum.GpStatus]
    GdipGetHatchForegroundColor: _Callable[[_type.GpHatch,  # brush
                                            _Pointer[_type.ARGB]],  # forecol
                                           _enum.GpStatus]
    GdipGetHatchBackgroundColor: _Callable[[_type.GpHatch,  # brush
                                            _Pointer[_type.ARGB]],  # backcol
                                           _enum.GpStatus]
    GdipCreateTexture: _Callable[[_type.GpImage,  # image
                                  _enum.GpWrapMode,  # wrapmode
                                  _Pointer[_type.GpTexture]],  # texture
                                 _enum.GpStatus]
    GdipCreateTexture2: _Callable[[_type.GpImage,  # image
                                   _enum.GpWrapMode,  # wrapmode
                                   _type.REAL,  # x
                                   _type.REAL,  # y
                                   _type.REAL,  # width
                                   _type.REAL,  # height
                                   _Pointer[_type.GpTexture]],  # texture
                                  _enum.GpStatus]
    GdipCreateTextureIA: _Callable[[_type.GpImage,  # image
                                    _type.GpImageAttributes,  # imageAttributes
                                    _type.REAL,  # x
                                    _type.REAL,  # y
                                    _type.REAL,  # width
                                    _type.REAL,  # height
                                    _Pointer[_type.GpTexture]],  # texture
                                   _enum.GpStatus]
    GdipCreateTexture2I: _Callable[[_type.GpImage,  # image
                                    _enum.GpWrapMode,  # wrapmode
                                    _type.INT,  # x
                                    _type.INT,  # y
                                    _type.INT,  # width
                                    _type.INT,  # height
                                    _Pointer[_type.GpTexture]],  # texture
                                   _enum.GpStatus]
    GdipCreateTextureIAI: _Callable[[_type.GpImage,  # image
                                     _type.GpImageAttributes,  # imageAttributes
                                     _type.INT,  # x
                                     _type.INT,  # y
                                     _type.INT,  # width
                                     _type.INT,  # height
                                     _Pointer[_type.GpTexture]],  # texture
                                    _enum.GpStatus]
    GdipGetTextureTransform: _Callable[[_type.GpTexture,  # brush
                                        _type.GpMatrix],  # matrix
                                       _enum.GpStatus]
    GdipSetTextureTransform: _Callable[[_type.GpTexture,  # brush
                                        _type.GpMatrix],  # matrix
                                       _enum.GpStatus]
    GdipResetTextureTransform: _Callable[[_type.GpTexture],  # brush
                                         _enum.GpStatus]
    GdipMultiplyTextureTransform: _Callable[[_type.GpTexture,  # brush
                                             _type.GpMatrix,  # matrix
                                             _enum.GpMatrixOrder],  # order
                                            _enum.GpStatus]
    GdipTranslateTextureTransform: _Callable[[_type.GpTexture,  # brush
                                              _type.REAL,  # dx
                                              _type.REAL,  # dy
                                              _enum.GpMatrixOrder],  # order
                                             _enum.GpStatus]
    GdipScaleTextureTransform: _Callable[[_type.GpTexture,  # brush
                                          _type.REAL,  # sx
                                          _type.REAL,  # sy
                                          _enum.GpMatrixOrder],  # order
                                         _enum.GpStatus]
    GdipRotateTextureTransform: _Callable[[_type.GpTexture,  # brush
                                           _type.REAL,  # angle
                                           _enum.GpMatrixOrder],  # order
                                          _enum.GpStatus]
    GdipSetTextureWrapMode: _Callable[[_type.GpTexture,  # brush
                                       _enum.GpWrapMode],  # wrapmode
                                      _enum.GpStatus]
    GdipGetTextureWrapMode: _Callable[[_type.GpTexture,  # brush
                                       _Pointer[_enum.GpWrapMode]],  # wrapmode
                                      _enum.GpStatus]
    GdipGetTextureImage: _Callable[[_type.GpTexture,  # brush
                                    _Pointer[_type.GpImage]],  # image
                                   _enum.GpStatus]
    GdipCreateSolidFill: _Callable[[_type.ARGB,  # color
                                    _Pointer[_type.GpSolidFill]],  # brush
                                   _enum.GpStatus]
    GdipSetSolidFillColor: _Callable[[_type.GpSolidFill,  # brush
                                      _type.ARGB],  # color
                                     _enum.GpStatus]
    GdipGetSolidFillColor: _Callable[[_type.GpSolidFill,  # brush
                                      _Pointer[_type.ARGB]],  # color
                                     _enum.GpStatus]
    GdipCreateLineBrush: _Callable[[_Pointer[_struct.GpPointF],  # point1
                                    _Pointer[_struct.GpPointF],  # point2
                                    _type.ARGB,  # color1
                                    _type.ARGB,  # color2
                                    _enum.GpWrapMode,  # wrapMode
                                    _Pointer[_type.GpLineGradient]],  # lineGradient
                                   _enum.GpStatus]
    GdipCreateLineBrushI: _Callable[[_Pointer[_struct.GpPoint],  # point1
                                     _Pointer[_struct.GpPoint],  # point2
                                     _type.ARGB,  # color1
                                     _type.ARGB,  # color2
                                     _enum.GpWrapMode,  # wrapMode
                                     _Pointer[_type.GpLineGradient]],  # lineGradient
                                    _enum.GpStatus]
    GdipCreateLineBrushFromRect: _Callable[[_Pointer[_struct.GpRectF],  # rect
                                            _type.ARGB,  # color1
                                            _type.ARGB,  # color2
                                            _enum.LinearGradientMode,  # mode
                                            _enum.GpWrapMode,  # wrapMode
                                            _Pointer[_type.GpLineGradient]],  # lineGradient
                                           _enum.GpStatus]
    GdipCreateLineBrushFromRectI: _Callable[[_Pointer[_struct.GpRect],  # rect
                                             _type.ARGB,  # color1
                                             _type.ARGB,  # color2
                                             _enum.LinearGradientMode,  # mode
                                             _enum.GpWrapMode,  # wrapMode
                                             _Pointer[_type.GpLineGradient]],  # lineGradient
                                            _enum.GpStatus]
    GdipCreateLineBrushFromRectWithAngle: _Callable[[_Pointer[_struct.GpRectF],  # rect
                                                     _type.ARGB,  # color1
                                                     _type.ARGB,  # color2
                                                     _type.REAL,  # angle
                                                     _type.BOOL,  # isAngleScalable
                                                     _enum.GpWrapMode,  # wrapMode
                                                     _Pointer[_type.GpLineGradient]],  # lineGradient
                                                    _enum.GpStatus]
    GdipCreateLineBrushFromRectWithAngleI: _Callable[[_Pointer[_struct.GpRect],  # rect
                                                      _type.ARGB,  # color1
                                                      _type.ARGB,  # color2
                                                      _type.REAL,  # angle
                                                      _type.BOOL,  # isAngleScalable
                                                      _enum.GpWrapMode,  # wrapMode
                                                      _Pointer[_type.GpLineGradient]],  # lineGradient
                                                     _enum.GpStatus]
    GdipSetLineColors: _Callable[[_type.GpLineGradient,  # brush
                                  _type.ARGB,  # color1
                                  _type.ARGB],  # color2
                                 _enum.GpStatus]
    GdipGetLineColors: _Callable[[_type.GpLineGradient,  # brush
                                  _Pointer[_type.ARGB]],  # colors
                                 _enum.GpStatus]
    GdipGetLineRect: _Callable[[_type.GpLineGradient,  # brush
                                _Pointer[_struct.GpRectF]],  # rect
                               _enum.GpStatus]
    GdipGetLineRectI: _Callable[[_type.GpLineGradient,  # brush
                                 _Pointer[_struct.GpRect]],  # rect
                                _enum.GpStatus]
    GdipSetLineGammaCorrection: _Callable[[_type.GpLineGradient,  # brush
                                           _type.BOOL],  # useGammaCorrection
                                          _enum.GpStatus]
    GdipGetLineGammaCorrection: _Callable[[_type.GpLineGradient,  # brush
                                           _Pointer[_type.BOOL]],  # useGammaCorrection
                                          _enum.GpStatus]
    GdipGetLineBlendCount: _Callable[[_type.GpLineGradient,  # brush
                                      _Pointer[_type.INT]],  # count
                                     _enum.GpStatus]
    GdipGetLineBlend: _Callable[[_type.GpLineGradient,  # brush
                                 _Pointer[_type.REAL],  # blend
                                 _Pointer[_type.REAL],  # positions
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipSetLineBlend: _Callable[[_type.GpLineGradient,  # brush
                                 _Pointer[_type.REAL],  # blend
                                 _Pointer[_type.REAL],  # positions
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipGetLinePresetBlendCount: _Callable[[_type.GpLineGradient,  # brush
                                            _Pointer[_type.INT]],  # count
                                           _enum.GpStatus]
    GdipGetLinePresetBlend: _Callable[[_type.GpLineGradient,  # brush
                                       _Pointer[_type.ARGB],  # blend
                                       _Pointer[_type.REAL],  # positions
                                       _type.INT],  # count
                                      _enum.GpStatus]
    GdipSetLinePresetBlend: _Callable[[_type.GpLineGradient,  # brush
                                       _Pointer[_type.ARGB],  # blend
                                       _Pointer[_type.REAL],  # positions
                                       _type.INT],  # count
                                      _enum.GpStatus]
    GdipSetLineSigmaBlend: _Callable[[_type.GpLineGradient,  # brush
                                      _type.REAL,  # focus
                                      _type.REAL],  # scale
                                     _enum.GpStatus]
    GdipSetLineLinearBlend: _Callable[[_type.GpLineGradient,  # brush
                                       _type.REAL,  # focus
                                       _type.REAL],  # scale
                                      _enum.GpStatus]
    GdipSetLineWrapMode: _Callable[[_type.GpLineGradient,  # brush
                                    _enum.GpWrapMode],  # wrapmode
                                   _enum.GpStatus]
    GdipGetLineWrapMode: _Callable[[_type.GpLineGradient,  # brush
                                    _Pointer[_enum.GpWrapMode]],  # wrapmode
                                   _enum.GpStatus]
    GdipGetLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                     _type.GpMatrix],  # matrix
                                    _enum.GpStatus]
    GdipSetLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                     _type.GpMatrix],  # matrix
                                    _enum.GpStatus]
    GdipResetLineTransform: _Callable[[_type.GpLineGradient],  # brush
                                      _enum.GpStatus]
    GdipMultiplyLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                          _type.GpMatrix,  # matrix
                                          _enum.GpMatrixOrder],  # order
                                         _enum.GpStatus]
    GdipTranslateLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                           _type.REAL,  # dx
                                           _type.REAL,  # dy
                                           _enum.GpMatrixOrder],  # order
                                          _enum.GpStatus]
    GdipScaleLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                       _type.REAL,  # sx
                                       _type.REAL,  # sy
                                       _enum.GpMatrixOrder],  # order
                                      _enum.GpStatus]
    GdipRotateLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                        _type.REAL,  # angle
                                        _enum.GpMatrixOrder],  # order
                                       _enum.GpStatus]
    GdipCreatePathGradient: _Callable[[_Pointer[_struct.GpPointF],  # points
                                       _type.INT,  # count
                                       _enum.GpWrapMode,  # wrapMode
                                       _Pointer[_type.GpPathGradient]],  # polyGradient
                                      _enum.GpStatus]
    GdipCreatePathGradientI: _Callable[[_Pointer[_struct.GpPoint],  # points
                                        _type.INT,  # count
                                        _enum.GpWrapMode,  # wrapMode
                                        _Pointer[_type.GpPathGradient]],  # polyGradient
                                       _enum.GpStatus]
    GdipCreatePathGradientFromPath: _Callable[[_type.GpPath,  # path
                                               _Pointer[_type.GpPathGradient]],  # polyGradient
                                              _enum.GpStatus]
    GdipGetPathGradientCenterColor: _Callable[[_type.GpPathGradient,  # brush
                                               _Pointer[_type.ARGB]],  # colors
                                              _enum.GpStatus]
    GdipSetPathGradientCenterColor: _Callable[[_type.GpPathGradient,  # brush
                                               _type.ARGB],  # colors
                                              _enum.GpStatus]
    GdipGetPathGradientSurroundColorsWithCount: _Callable[[_type.GpPathGradient,  # brush
                                                           _Pointer[_type.ARGB],  # color
                                                           _Pointer[_type.INT]],  # count
                                                          _enum.GpStatus]
    GdipSetPathGradientSurroundColorsWithCount: _Callable[[_type.GpPathGradient,  # brush
                                                           _Pointer[_type.ARGB],  # color
                                                           _Pointer[_type.INT]],  # count
                                                          _enum.GpStatus]
    GdipGetPathGradientPath: _Callable[[_type.GpPathGradient,  # brush
                                        _type.GpPath],  # path
                                       _enum.GpStatus]
    GdipSetPathGradientPath: _Callable[[_type.GpPathGradient,  # brush
                                        _type.GpPath],  # path
                                       _enum.GpStatus]
    GdipGetPathGradientCenterPoint: _Callable[[_type.GpPathGradient,  # brush
                                               _Pointer[_struct.GpPointF]],  # points
                                              _enum.GpStatus]
    GdipGetPathGradientCenterPointI: _Callable[[_type.GpPathGradient,  # brush
                                                _Pointer[_struct.GpPoint]],  # points
                                               _enum.GpStatus]
    GdipSetPathGradientCenterPoint: _Callable[[_type.GpPathGradient,  # brush
                                               _Pointer[_struct.GpPointF]],  # points
                                              _enum.GpStatus]
    GdipSetPathGradientCenterPointI: _Callable[[_type.GpPathGradient,  # brush
                                                _Pointer[_struct.GpPoint]],  # points
                                               _enum.GpStatus]
    GdipGetPathGradientRect: _Callable[[_type.GpPathGradient,  # brush
                                        _Pointer[_struct.GpRectF]],  # rect
                                       _enum.GpStatus]
    GdipGetPathGradientRectI: _Callable[[_type.GpPathGradient,  # brush
                                         _Pointer[_struct.GpRect]],  # rect
                                        _enum.GpStatus]
    GdipGetPathGradientPointCount: _Callable[[_type.GpPathGradient,  # brush
                                              _Pointer[_type.INT]],  # count
                                             _enum.GpStatus]
    GdipGetPathGradientSurroundColorCount: _Callable[[_type.GpPathGradient,  # brush
                                                      _Pointer[_type.INT]],  # count
                                                     _enum.GpStatus]
    GdipSetPathGradientGammaCorrection: _Callable[[_type.GpPathGradient,  # brush
                                                   _type.BOOL],  # useGammaCorrection
                                                  _enum.GpStatus]
    GdipGetPathGradientGammaCorrection: _Callable[[_type.GpPathGradient,  # brush
                                                   _Pointer[_type.BOOL]],  # useGammaCorrection
                                                  _enum.GpStatus]
    GdipGetPathGradientBlendCount: _Callable[[_type.GpPathGradient,  # brush
                                              _Pointer[_type.INT]],  # count
                                             _enum.GpStatus]
    GdipGetPathGradientBlend: _Callable[[_type.GpPathGradient,  # brush
                                         _Pointer[_type.REAL],  # blend
                                         _Pointer[_type.REAL],  # positions
                                         _type.INT],  # count
                                        _enum.GpStatus]
    GdipSetPathGradientBlend: _Callable[[_type.GpPathGradient,  # brush
                                         _Pointer[_type.REAL],  # blend
                                         _Pointer[_type.REAL],  # positions
                                         _type.INT],  # count
                                        _enum.GpStatus]
    GdipGetPathGradientPresetBlendCount: _Callable[[_type.GpPathGradient,  # brush
                                                    _Pointer[_type.INT]],  # count
                                                   _enum.GpStatus]
    GdipGetPathGradientPresetBlend: _Callable[[_type.GpPathGradient,  # brush
                                               _Pointer[_type.ARGB],  # blend
                                               _Pointer[_type.REAL],  # positions
                                               _type.INT],  # count
                                              _enum.GpStatus]
    GdipSetPathGradientPresetBlend: _Callable[[_type.GpPathGradient,  # brush
                                               _Pointer[_type.ARGB],  # blend
                                               _Pointer[_type.REAL],  # positions
                                               _type.INT],  # count
                                              _enum.GpStatus]
    GdipSetPathGradientSigmaBlend: _Callable[[_type.GpPathGradient,  # brush
                                              _type.REAL,  # focus
                                              _type.REAL],  # scale
                                             _enum.GpStatus]
    GdipSetPathGradientLinearBlend: _Callable[[_type.GpPathGradient,  # brush
                                               _type.REAL,  # focus
                                               _type.REAL],  # scale
                                              _enum.GpStatus]
    GdipGetPathGradientWrapMode: _Callable[[_type.GpPathGradient,  # brush
                                            _Pointer[_enum.GpWrapMode]],  # wrapmode
                                           _enum.GpStatus]
    GdipSetPathGradientWrapMode: _Callable[[_type.GpPathGradient,  # brush
                                            _enum.GpWrapMode],  # wrapmode
                                           _enum.GpStatus]
    GdipGetPathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                             _type.GpMatrix],  # matrix
                                            _enum.GpStatus]
    GdipSetPathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                             _type.GpMatrix],  # matrix
                                            _enum.GpStatus]
    GdipResetPathGradientTransform: _Callable[[_type.GpPathGradient],  # brush
                                              _enum.GpStatus]
    GdipMultiplyPathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                                  _type.GpMatrix,  # matrix
                                                  _enum.GpMatrixOrder],  # order
                                                 _enum.GpStatus]
    GdipTranslatePathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                                   _type.REAL,  # dx
                                                   _type.REAL,  # dy
                                                   _enum.GpMatrixOrder],  # order
                                                  _enum.GpStatus]
    GdipScalePathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                               _type.REAL,  # sx
                                               _type.REAL,  # sy
                                               _enum.GpMatrixOrder],  # order
                                              _enum.GpStatus]
    GdipRotatePathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                                _type.REAL,  # angle
                                                _enum.GpMatrixOrder],  # order
                                               _enum.GpStatus]
    GdipGetPathGradientFocusScales: _Callable[[_type.GpPathGradient,  # brush
                                               _Pointer[_type.REAL],  # xScale
                                               _Pointer[_type.REAL]],  # yScale
                                              _enum.GpStatus]
    GdipSetPathGradientFocusScales: _Callable[[_type.GpPathGradient,  # brush
                                               _type.REAL,  # xScale
                                               _type.REAL],  # yScale
                                              _enum.GpStatus]
    GdipCreatePen1: _Callable[[_type.ARGB,  # color
                               _type.REAL,  # width
                               _enum.GpUnit,  # unit
                               _Pointer[_type.GpPen]],  # pen
                              _enum.GpStatus]
    GdipCreatePen2: _Callable[[_type.GpBrush,  # brush
                               _type.REAL,  # width
                               _enum.GpUnit,  # unit
                               _Pointer[_type.GpPen]],  # pen
                              _enum.GpStatus]
    GdipClonePen: _Callable[[_type.GpPen,  # pen
                             _Pointer[_type.GpPen]],  # clonepen
                            _enum.GpStatus]
    GdipDeletePen: _Callable[[_type.GpPen],  # pen
                             _enum.GpStatus]
    GdipSetPenWidth: _Callable[[_type.GpPen,  # pen
                                _type.REAL],  # width
                               _enum.GpStatus]
    GdipGetPenWidth: _Callable[[_type.GpPen,  # pen
                                _Pointer[_type.REAL]],  # width
                               _enum.GpStatus]
    GdipSetPenUnit: _Callable[[_type.GpPen,  # pen
                               _enum.GpUnit],  # unit
                              _enum.GpStatus]
    GdipGetPenUnit: _Callable[[_type.GpPen,  # pen
                               _Pointer[_enum.GpUnit]],  # unit
                              _enum.GpStatus]
    GdipSetPenLineCap197819: _Callable[[_type.GpPen,  # pen
                                        _enum.GpLineCap,  # startCap
                                        _enum.GpLineCap,  # endCap
                                        _enum.GpDashCap],  # dashCap
                                       _enum.GpStatus]
    GdipSetPenStartCap: _Callable[[_type.GpPen,  # pen
                                   _enum.GpLineCap],  # startCap
                                  _enum.GpStatus]
    GdipSetPenEndCap: _Callable[[_type.GpPen,  # pen
                                 _enum.GpLineCap],  # endCap
                                _enum.GpStatus]
    GdipSetPenDashCap197819: _Callable[[_type.GpPen,  # pen
                                        _enum.GpDashCap],  # dashCap
                                       _enum.GpStatus]
    GdipGetPenStartCap: _Callable[[_type.GpPen,  # pen
                                   _Pointer[_enum.GpLineCap]],  # startCap
                                  _enum.GpStatus]
    GdipGetPenEndCap: _Callable[[_type.GpPen,  # pen
                                 _Pointer[_enum.GpLineCap]],  # endCap
                                _enum.GpStatus]
    GdipGetPenDashCap197819: _Callable[[_type.GpPen,  # pen
                                        _Pointer[_enum.GpDashCap]],  # dashCap
                                       _enum.GpStatus]
    GdipSetPenLineJoin: _Callable[[_type.GpPen,  # pen
                                   _enum.GpLineJoin],  # lineJoin
                                  _enum.GpStatus]
    GdipGetPenLineJoin: _Callable[[_type.GpPen,  # pen
                                   _Pointer[_enum.GpLineJoin]],  # lineJoin
                                  _enum.GpStatus]
    GdipSetPenCustomStartCap: _Callable[[_type.GpPen,  # pen
                                         _type.GpCustomLineCap],  # customCap
                                        _enum.GpStatus]
    GdipGetPenCustomStartCap: _Callable[[_type.GpPen,  # pen
                                         _Pointer[_type.GpCustomLineCap]],  # customCap
                                        _enum.GpStatus]
    GdipSetPenCustomEndCap: _Callable[[_type.GpPen,  # pen
                                       _type.GpCustomLineCap],  # customCap
                                      _enum.GpStatus]
    GdipGetPenCustomEndCap: _Callable[[_type.GpPen,  # pen
                                       _Pointer[_type.GpCustomLineCap]],  # customCap
                                      _enum.GpStatus]
    GdipSetPenMiterLimit: _Callable[[_type.GpPen,  # pen
                                     _type.REAL],  # miterLimit
                                    _enum.GpStatus]
    GdipGetPenMiterLimit: _Callable[[_type.GpPen,  # pen
                                     _Pointer[_type.REAL]],  # miterLimit
                                    _enum.GpStatus]
    GdipSetPenMode: _Callable[[_type.GpPen,  # pen
                               _enum.GpPenAlignment],  # penMode
                              _enum.GpStatus]
    GdipGetPenMode: _Callable[[_type.GpPen,  # pen
                               _Pointer[_enum.GpPenAlignment]],  # penMode
                              _enum.GpStatus]
    GdipSetPenTransform: _Callable[[_type.GpPen,  # pen
                                    _type.GpMatrix],  # matrix
                                   _enum.GpStatus]
    GdipGetPenTransform: _Callable[[_type.GpPen,  # pen
                                    _type.GpMatrix],  # matrix
                                   _enum.GpStatus]
    GdipResetPenTransform: _Callable[[_type.GpPen],  # pen
                                     _enum.GpStatus]
    GdipMultiplyPenTransform: _Callable[[_type.GpPen,  # pen
                                         _type.GpMatrix,  # matrix
                                         _enum.GpMatrixOrder],  # order
                                        _enum.GpStatus]
    GdipTranslatePenTransform: _Callable[[_type.GpPen,  # pen
                                          _type.REAL,  # dx
                                          _type.REAL,  # dy
                                          _enum.GpMatrixOrder],  # order
                                         _enum.GpStatus]
    GdipScalePenTransform: _Callable[[_type.GpPen,  # pen
                                      _type.REAL,  # sx
                                      _type.REAL,  # sy
                                      _enum.GpMatrixOrder],  # order
                                     _enum.GpStatus]
    GdipRotatePenTransform: _Callable[[_type.GpPen,  # pen
                                       _type.REAL,  # angle
                                       _enum.GpMatrixOrder],  # order
                                      _enum.GpStatus]
    GdipSetPenColor: _Callable[[_type.GpPen,  # pen
                                _type.ARGB],  # argb
                               _enum.GpStatus]
    GdipGetPenColor: _Callable[[_type.GpPen,  # pen
                                _Pointer[_type.ARGB]],  # argb
                               _enum.GpStatus]
    GdipSetPenBrushFill: _Callable[[_type.GpPen,  # pen
                                    _type.GpBrush],  # brush
                                   _enum.GpStatus]
    GdipGetPenBrushFill: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_type.GpBrush]],  # brush
                                   _enum.GpStatus]
    GdipGetPenFillType: _Callable[[_type.GpPen,  # pen
                                   _Pointer[_enum.GpPenType]],  # type
                                  _enum.GpStatus]
    GdipGetPenDashStyle: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_enum.GpDashStyle]],  # dashstyle
                                   _enum.GpStatus]
    GdipSetPenDashStyle: _Callable[[_type.GpPen,  # pen
                                    _enum.GpDashStyle],  # dashstyle
                                   _enum.GpStatus]
    GdipGetPenDashOffset: _Callable[[_type.GpPen,  # pen
                                     _Pointer[_type.REAL]],  # offset
                                    _enum.GpStatus]
    GdipSetPenDashOffset: _Callable[[_type.GpPen,  # pen
                                     _type.REAL],  # offset
                                    _enum.GpStatus]
    GdipGetPenDashCount: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_type.INT]],  # count
                                   _enum.GpStatus]
    GdipSetPenDashArray: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_type.REAL],  # dash
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipGetPenDashArray: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_type.REAL],  # dash
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipGetPenCompoundCount: _Callable[[_type.GpPen,  # pen
                                        _Pointer[_type.INT]],  # count
                                       _enum.GpStatus]
    GdipSetPenCompoundArray: _Callable[[_type.GpPen,  # pen
                                        _Pointer[_type.REAL],  # dash
                                        _type.INT],  # count
                                       _enum.GpStatus]
    GdipGetPenCompoundArray: _Callable[[_type.GpPen,  # pen
                                        _Pointer[_type.REAL],  # dash
                                        _type.INT],  # count
                                       _enum.GpStatus]
    GdipCreateCustomLineCap: _Callable[[_type.GpPath,  # fillPath
                                        _type.GpPath,  # strokePath
                                        _enum.GpLineCap,  # baseCap
                                        _type.REAL,  # baseInset
                                        _Pointer[_type.GpCustomLineCap]],  # customCap
                                       _enum.GpStatus]
    GdipDeleteCustomLineCap: _Callable[[_type.GpCustomLineCap],  # customCap
                                       _enum.GpStatus]
    GdipCloneCustomLineCap: _Callable[[_type.GpCustomLineCap,  # customCap
                                       _Pointer[_type.GpCustomLineCap]],  # clonedCap
                                      _enum.GpStatus]
    GdipGetCustomLineCapType: _Callable[[_type.GpCustomLineCap,  # customCap
                                         _Pointer[_enum.CustomLineCapType]],  # capType
                                        _enum.GpStatus]
    GdipSetCustomLineCapStrokeCaps: _Callable[[_type.GpCustomLineCap,  # customCap
                                               _enum.GpLineCap,  # startCap
                                               _enum.GpLineCap],  # endCap
                                              _enum.GpStatus]
    GdipGetCustomLineCapStrokeCaps: _Callable[[_type.GpCustomLineCap,  # customCap
                                               _Pointer[_enum.GpLineCap],  # startCap
                                               _Pointer[_enum.GpLineCap]],  # endCap
                                              _enum.GpStatus]
    GdipSetCustomLineCapStrokeJoin: _Callable[[_type.GpCustomLineCap,  # customCap
                                               _enum.GpLineJoin],  # lineJoin
                                              _enum.GpStatus]
    GdipGetCustomLineCapStrokeJoin: _Callable[[_type.GpCustomLineCap,  # customCap
                                               _Pointer[_enum.GpLineJoin]],  # lineJoin
                                              _enum.GpStatus]
    GdipSetCustomLineCapBaseCap: _Callable[[_type.GpCustomLineCap,  # customCap
                                            _enum.GpLineCap],  # baseCap
                                           _enum.GpStatus]
    GdipGetCustomLineCapBaseCap: _Callable[[_type.GpCustomLineCap,  # customCap
                                            _Pointer[_enum.GpLineCap]],  # baseCap
                                           _enum.GpStatus]
    GdipSetCustomLineCapBaseInset: _Callable[[_type.GpCustomLineCap,  # customCap
                                              _type.REAL],  # inset
                                             _enum.GpStatus]
    GdipGetCustomLineCapBaseInset: _Callable[[_type.GpCustomLineCap,  # customCap
                                              _Pointer[_type.REAL]],  # inset
                                             _enum.GpStatus]
    GdipSetCustomLineCapWidthScale: _Callable[[_type.GpCustomLineCap,  # customCap
                                               _type.REAL],  # widthScale
                                              _enum.GpStatus]
    GdipGetCustomLineCapWidthScale: _Callable[[_type.GpCustomLineCap,  # customCap
                                               _Pointer[_type.REAL]],  # widthScale
                                              _enum.GpStatus]
    GdipCreateAdjustableArrowCap: _Callable[[_type.REAL,  # height
                                             _type.REAL,  # width
                                             _type.BOOL,  # isFilled
                                             _Pointer[_type.GpAdjustableArrowCap]],  # cap
                                            _enum.GpStatus]
    GdipSetAdjustableArrowCapHeight: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                _type.REAL],  # height
                                               _enum.GpStatus]
    GdipGetAdjustableArrowCapHeight: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                _Pointer[_type.REAL]],  # height
                                               _enum.GpStatus]
    GdipSetAdjustableArrowCapWidth: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                               _type.REAL],  # width
                                              _enum.GpStatus]
    GdipGetAdjustableArrowCapWidth: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                               _Pointer[_type.REAL]],  # width
                                              _enum.GpStatus]
    GdipSetAdjustableArrowCapMiddleInset: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                     _type.REAL],  # middleInset
                                                    _enum.GpStatus]
    GdipGetAdjustableArrowCapMiddleInset: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                     _Pointer[_type.REAL]],  # middleInset
                                                    _enum.GpStatus]
    GdipSetAdjustableArrowCapFillState: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                   _type.BOOL],  # fillState
                                                  _enum.GpStatus]
    GdipGetAdjustableArrowCapFillState: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                   _Pointer[_type.BOOL]],  # fillState
                                                  _enum.GpStatus]
    GdipLoadImageFromStream: _Callable[[_interface.IStream,  # stream
                                        _Pointer[_type.GpImage]],  # image
                                       _enum.GpStatus]
    GdipLoadImageFromFile: _Callable[[_type.LPWSTR,  # filename
                                      _Pointer[_type.GpImage]],  # image
                                     _enum.GpStatus]
    GdipLoadImageFromStreamICM: _Callable[[_interface.IStream,  # stream
                                           _Pointer[_type.GpImage]],  # image
                                          _enum.GpStatus]
    GdipLoadImageFromFileICM: _Callable[[_type.LPWSTR,  # filename
                                         _Pointer[_type.GpImage]],  # image
                                        _enum.GpStatus]
    GdipCloneImage: _Callable[[_type.GpImage,  # image
                               _Pointer[_type.GpImage]],  # cloneImage
                              _enum.GpStatus]
    GdipDisposeImage: _Callable[[_type.GpImage],  # image
                                _enum.GpStatus]
    GdipSaveImageToFile: _Callable[[_type.GpImage,  # image
                                    _type.LPWSTR,  # filename
                                    _Pointer[_struct.CLSID],  # clsidEncoder
                                    _Optional[_Pointer[_struct.EncoderParameters]]],  # encoderParams
                                   _enum.GpStatus]
    GdipSaveImageToStream: _Callable[[_type.GpImage,  # image
                                      _interface.IStream,  # stream
                                      _Pointer[_struct.CLSID],  # clsidEncoder
                                      _Pointer[_struct.EncoderParameters]],  # encoderParams
                                     _enum.GpStatus]
    GdipSaveAdd: _Callable[[_type.GpImage,  # image
                            _Pointer[_struct.EncoderParameters]],  # encoderParams
                           _enum.GpStatus]
    GdipSaveAddImage: _Callable[[_type.GpImage,  # image
                                 _type.GpImage,  # newImage
                                 _Pointer[_struct.EncoderParameters]],  # encoderParams
                                _enum.GpStatus]
    GdipGetImageGraphicsContext: _Callable[[_type.GpImage,  # image
                                            _Pointer[_type.GpGraphics]],  # graphics
                                           _enum.GpStatus]
    GdipGetImageBounds: _Callable[[_type.GpImage,  # image
                                   _Pointer[_struct.GpRectF],  # srcRect
                                   _Pointer[_enum.GpUnit]],  # srcUnit
                                  _enum.GpStatus]
    GdipGetImageDimension: _Callable[[_type.GpImage,  # image
                                      _Pointer[_type.REAL],  # width
                                      _Pointer[_type.REAL]],  # height
                                     _enum.GpStatus]
    GdipGetImageType: _Callable[[_type.GpImage,  # image
                                 _Pointer[_enum.ImageType]],  # type
                                _enum.GpStatus]
    GdipGetImageWidth: _Callable[[_type.GpImage,  # image
                                  _Pointer[_type.UINT]],  # width
                                 _enum.GpStatus]
    GdipGetImageHeight: _Callable[[_type.GpImage,  # image
                                   _Pointer[_type.UINT]],  # height
                                  _enum.GpStatus]
    GdipGetImageHorizontalResolution: _Callable[[_type.GpImage,  # image
                                                 _Pointer[_type.REAL]],  # resolution
                                                _enum.GpStatus]
    GdipGetImageVerticalResolution: _Callable[[_type.GpImage,  # image
                                               _Pointer[_type.REAL]],  # resolution
                                              _enum.GpStatus]
    GdipGetImageFlags: _Callable[[_type.GpImage,  # image
                                  _Pointer[_type.UINT]],  # flags
                                 _enum.GpStatus]
    GdipGetImageRawFormat: _Callable[[_type.GpImage,  # image
                                      _Pointer[_struct.GUID]],  # format
                                     _enum.GpStatus]
    GdipGetImagePixelFormat: _Callable[[_type.GpImage,  # image
                                        _Pointer[_type.PixelFormat]],  # format
                                       _enum.GpStatus]
    GdipGetImageThumbnail: _Callable[[_type.GpImage,  # image
                                      _type.UINT,  # thumbWidth
                                      _type.UINT,  # thumbHeight
                                      _Pointer[_type.GpImage],  # thumbImage
                                      _type.GetThumbnailImageAbort,  # callback
                                      _Optional[_Pointer[_type.VOID]]],  # callbackData
                                     _enum.GpStatus]
    GdipGetEncoderParameterListSize: _Callable[[_type.GpImage,  # image
                                                _Pointer[_struct.CLSID],  # clsidEncoder
                                                _Pointer[_type.UINT]],  # size
                                               _enum.GpStatus]
    GdipGetEncoderParameterList: _Callable[[_type.GpImage,  # image
                                            _Pointer[_struct.CLSID],  # clsidEncoder
                                            _type.UINT,  # size
                                            _Pointer[_struct.EncoderParameters]],  # buffer
                                           _enum.GpStatus]
    GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage,  # image
                                                 _Pointer[_type.UINT]],  # count
                                                _enum.GpStatus]
    GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage,  # image
                                                _Pointer[_struct.GUID],  # dimensionIDs
                                                _type.UINT],  # count
                                               _enum.GpStatus]
    GdipImageGetFrameCount: _Callable[[_type.GpImage,  # image
                                       _Pointer[_struct.GUID],  # dimensionID
                                       _Pointer[_type.UINT]],  # count
                                      _enum.GpStatus]
    GdipImageSelectActiveFrame: _Callable[[_type.GpImage,  # image
                                           _Pointer[_struct.GUID],  # dimensionID
                                           _type.UINT],  # frameIndex
                                          _enum.GpStatus]
    GdipImageRotateFlip: _Callable[[_type.GpImage,  # image
                                    _enum.RotateFlipType],  # rfType
                                   _enum.GpStatus]
    GdipGetImagePalette: _Callable[[_type.GpImage,  # image
                                    _Pointer[_struct.ColorPalette],  # palette
                                    _type.INT],  # size
                                   _enum.GpStatus]
    GdipSetImagePalette: _Callable[[_type.GpImage,  # image
                                    _Pointer[_struct.ColorPalette]],  # palette
                                   _enum.GpStatus]
    GdipGetImagePaletteSize: _Callable[[_type.GpImage,  # image
                                        _Pointer[_type.INT]],  # size
                                       _enum.GpStatus]
    GdipGetPropertyCount: _Callable[[_type.GpImage,  # image
                                     _Pointer[_type.UINT]],  # numOfProperty
                                    _enum.GpStatus]
    GdipGetPropertyIdList: _Callable[[_type.GpImage,  # image
                                      _type.UINT,  # numOfProperty
                                      _Pointer[_type.PROPID]],  # list
                                     _enum.GpStatus]
    GdipGetPropertyItemSize: _Callable[[_type.GpImage,  # image
                                        _type.PROPID,  # propId
                                        _Pointer[_type.UINT]],  # size
                                       _enum.GpStatus]
    GdipGetPropertyItem: _Callable[[_type.GpImage,  # image
                                    _type.PROPID,  # propId
                                    _type.UINT,  # propSize
                                    _Pointer[_struct.PropertyItem]],  # buffer
                                   _enum.GpStatus]
    GdipGetPropertySize: _Callable[[_type.GpImage,  # image
                                    _Pointer[_type.UINT],  # totalBufferSize
                                    _Pointer[_type.UINT]],  # numProperties
                                   _enum.GpStatus]
    GdipGetAllPropertyItems: _Callable[[_type.GpImage,  # image
                                        _type.UINT,  # totalBufferSize
                                        _type.UINT,  # numProperties
                                        _Pointer[_struct.PropertyItem]],  # allItems
                                       _enum.GpStatus]
    GdipRemovePropertyItem: _Callable[[_type.GpImage,  # image
                                       _type.PROPID],  # propId
                                      _enum.GpStatus]
    GdipSetPropertyItem: _Callable[[_type.GpImage,  # image
                                    _Pointer[_struct.PropertyItem]],  # item
                                   _enum.GpStatus]
    GdipFindFirstImageItem: _Callable[[_type.GpImage,  # image
                                       _Pointer[_struct.ImageItemData]],  # item
                                      _enum.GpStatus]
    GdipFindNextImageItem: _Callable[[_type.GpImage,  # image
                                      _Pointer[_struct.ImageItemData]],  # item
                                     _enum.GpStatus]
    GdipGetImageItemData: _Callable[[_type.GpImage,  # image
                                     _Pointer[_struct.ImageItemData]],  # item
                                    _enum.GpStatus]
    GdipImageForceValidation: _Callable[[_type.GpImage],  # image
                                        _enum.GpStatus]
    GdipCreateBitmapFromStream: _Callable[[_interface.IStream,  # stream
                                           _Pointer[_type.GpBitmap]],  # bitmap
                                          _enum.GpStatus]
    GdipCreateBitmapFromFile: _Callable[[_type.LPWSTR,  # filename
                                         _Pointer[_type.GpBitmap]],  # bitmap
                                        _enum.GpStatus]
    GdipCreateBitmapFromStreamICM: _Callable[[_interface.IStream,  # stream
                                              _Pointer[_type.GpBitmap]],  # bitmap
                                             _enum.GpStatus]
    GdipCreateBitmapFromFileICM: _Callable[[_type.LPWSTR,  # filename
                                            _Pointer[_type.GpBitmap]],  # bitmap
                                           _enum.GpStatus]
    GdipCreateBitmapFromScan0: _Callable[[_type.INT,  # width
                                          _type.INT,  # height
                                          _type.INT,  # stride
                                          _type.PixelFormat,  # format
                                          _Optional[_Pointer[_type.BYTE]],  # scan0
                                          _Pointer[_type.GpBitmap]],  # bitmap
                                         _enum.GpStatus]
    GdipCreateBitmapFromGraphics: _Callable[[_type.INT,  # width
                                             _type.INT,  # height
                                             _type.GpGraphics,  # target
                                             _Pointer[_type.GpBitmap]],  # bitmap
                                            _enum.GpStatus]
    GdipCreateBitmapFromDirectDrawSurface: _Callable[[_interface.IDirectDrawSurface7,  # surface
                                                      _Pointer[_type.GpBitmap]],  # bitmap
                                                     _enum.GpStatus]
    GdipCreateBitmapFromGdiDib: _Callable[[_Pointer[_struct.BITMAPINFO],  # gdiBitmapInfo
                                           _Pointer[_type.VOID],  # gdiBitmapData
                                           _Pointer[_type.GpBitmap]],  # bitmap
                                          _enum.GpStatus]
    GdipCreateBitmapFromHBITMAP: _Callable[[_type.HBITMAP,  # hbm
                                            _type.HPALETTE,  # hpal
                                            _Pointer[_type.GpBitmap]],  # bitmap
                                           _enum.GpStatus]
    GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap,  # bitmap
                                            _Pointer[_type.HBITMAP],  # hbmReturn
                                            _type.ARGB],  # background
                                           _enum.GpStatus]
    GdipCreateBitmapFromHICON: _Callable[[_type.HICON,  # hicon
                                          _Pointer[_type.GpBitmap]],  # bitmap
                                         _enum.GpStatus]
    GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap,  # bitmap
                                          _Pointer[_type.HICON]],  # hbmReturn
                                         _enum.GpStatus]
    GdipCreateBitmapFromResource: _Callable[[_type.HINSTANCE,  # hInstance
                                             _type.LPWSTR,  # lpBitmapName
                                             _Pointer[_type.GpBitmap]],  # bitmap
                                            _enum.GpStatus]
    GdipCloneBitmapArea: _Callable[[_type.REAL,  # x
                                    _type.REAL,  # y
                                    _type.REAL,  # width
                                    _type.REAL,  # height
                                    _type.PixelFormat,  # format
                                    _type.GpBitmap,  # srcBitmap
                                    _Pointer[_type.GpBitmap]],  # dstBitmap
                                   _enum.GpStatus]
    GdipCloneBitmapAreaI: _Callable[[_type.INT,  # x
                                     _type.INT,  # y
                                     _type.INT,  # width
                                     _type.INT,  # height
                                     _type.PixelFormat,  # format
                                     _type.GpBitmap,  # srcBitmap
                                     _Pointer[_type.GpBitmap]],  # dstBitmap
                                    _enum.GpStatus]
    GdipBitmapLockBits: _Callable[[_type.GpBitmap,  # bitmap
                                   _Pointer[_struct.GpRect],  # rect
                                   _type.UINT,  # flags
                                   _type.PixelFormat,  # format
                                   _Pointer[_struct.BitmapData]],  # lockedBitmapData
                                  _enum.GpStatus]
    GdipBitmapUnlockBits: _Callable[[_type.GpBitmap,  # bitmap
                                     _Pointer[_struct.BitmapData]],  # lockedBitmapData
                                    _enum.GpStatus]
    GdipBitmapGetPixel: _Callable[[_type.GpBitmap,  # bitmap
                                   _type.INT,  # x
                                   _type.INT,  # y
                                   _Pointer[_type.ARGB]],  # color
                                  _enum.GpStatus]
    GdipBitmapSetPixel: _Callable[[_type.GpBitmap,  # bitmap
                                   _type.INT,  # x
                                   _type.INT,  # y
                                   _type.ARGB],  # color
                                  _enum.GpStatus]
    GdipImageSetAbort: _Callable[[_type.GpImage,  # pImage
                                  _Pointer[_type.GdiplusAbort]],  # pIAbort
                                 _enum.GpStatus]
    GdipGraphicsSetAbort: _Callable[[_type.GpGraphics,  # pGraphics
                                     _Pointer[_type.GdiplusAbort]],  # pIAbort
                                    _enum.GpStatus]
    GdipBitmapConvertFormat: _Callable[[_type.GpBitmap,  # pInputBitmap
                                        _type.PixelFormat,  # format
                                        _enum.DitherType,  # dithertype
                                        _enum.PaletteType,  # palettetype
                                        _Pointer[_struct.ColorPalette],  # palette
                                        _type.REAL],  # alphaThresholdPercent
                                       _enum.GpStatus]
    GdipInitializePalette: _Callable[[_Pointer[_struct.ColorPalette],  # palette
                                      _enum.PaletteType,  # palettetype
                                      _type.INT,  # optimalColors
                                      _type.BOOL,  # useTransparentColor
                                      _type.GpBitmap],  # bitmap
                                     _enum.GpStatus]
    GdipBitmapApplyEffect: _Callable[[_type.GpBitmap,  # bitmap
                                      _Pointer[_type.CGpEffect],  # effect
                                      _Pointer[_struct.RECT],  # roi
                                      _type.BOOL,  # useAuxData
                                      _Pointer[_Pointer[_type.VOID]],  # auxData
                                      _Pointer[_type.INT]],  # auxDataSize
                                     _enum.GpStatus]
    GdipBitmapCreateApplyEffect: _Callable[[_Pointer[_type.GpBitmap],  # inputBitmaps
                                            _type.INT,  # numInputs
                                            _Pointer[_type.CGpEffect],  # effect
                                            _Pointer[_struct.RECT],  # roi
                                            _Pointer[_struct.RECT],  # outputRect
                                            _Pointer[_type.GpBitmap],  # outputBitmap
                                            _type.BOOL,  # useAuxData
                                            _Pointer[_Pointer[_type.VOID]],  # auxData
                                            _Pointer[_type.INT]],  # auxDataSize
                                           _enum.GpStatus]
    GdipBitmapGetHistogram: _Callable[[_type.GpBitmap,  # bitmap
                                       _enum.HistogramFormat,  # format
                                       _type.UINT,  # NumberOfEntries
                                       _Pointer[_type.UINT],  # channel0
                                       _Pointer[_type.UINT],  # channel1
                                       _Pointer[_type.UINT],  # channel2
                                       _Pointer[_type.UINT]],  # channel3
                                      _enum.GpStatus]
    GdipBitmapGetHistogramSize: _Callable[[_enum.HistogramFormat,  # format
                                           _Pointer[_type.UINT]],  # NumberOfEntries
                                          _enum.GpStatus]
    GdipBitmapSetResolution: _Callable[[_type.GpBitmap,  # bitmap
                                        _type.REAL,  # xdpi
                                        _type.REAL],  # ydpi
                                       _enum.GpStatus]
    GdipCreateImageAttributes: _Callable[[_Pointer[_type.GpImageAttributes]],  # imageattr
                                         _enum.GpStatus]
    GdipCloneImageAttributes: _Callable[[_type.GpImageAttributes,  # imageattr
                                         _Pointer[_type.GpImageAttributes]],  # cloneImageattr
                                        _enum.GpStatus]
    GdipDisposeImageAttributes: _Callable[[_type.GpImageAttributes],  # imageattr
                                          _enum.GpStatus]
    GdipSetImageAttributesToIdentity: _Callable[[_type.GpImageAttributes,  # imageattr
                                                 _enum.ColorAdjustType],  # type
                                                _enum.GpStatus]
    GdipResetImageAttributes: _Callable[[_type.GpImageAttributes,  # imageattr
                                         _enum.ColorAdjustType],  # type
                                        _enum.GpStatus]
    GdipSetImageAttributesColorMatrix: _Callable[[_type.GpImageAttributes,  # imageattr
                                                  _enum.ColorAdjustType,  # type
                                                  _type.BOOL,  # enableFlag
                                                  _Optional[_Pointer[_struct.ColorMatrix]],  # colorMatrix
                                                  _Optional[_Pointer[_struct.ColorMatrix]],  # grayMatrix
                                                  _enum.ColorMatrixFlags],  # flags
                                                 _enum.GpStatus]
    GdipSetImageAttributesThreshold: _Callable[[_type.GpImageAttributes,  # imageattr
                                                _enum.ColorAdjustType,  # type
                                                _type.BOOL,  # enableFlag
                                                _type.REAL],  # threshold
                                               _enum.GpStatus]
    GdipSetImageAttributesGamma: _Callable[[_type.GpImageAttributes,  # imageattr
                                            _enum.ColorAdjustType,  # type
                                            _type.BOOL,  # enableFlag
                                            _type.REAL],  # gamma
                                           _enum.GpStatus]
    GdipSetImageAttributesNoOp: _Callable[[_type.GpImageAttributes,  # imageattr
                                           _enum.ColorAdjustType,  # type
                                           _type.BOOL],  # enableFlag
                                          _enum.GpStatus]
    GdipSetImageAttributesColorKeys: _Callable[[_type.GpImageAttributes,  # imageattr
                                                _enum.ColorAdjustType,  # type
                                                _type.BOOL,  # enableFlag
                                                _type.ARGB,  # colorLow
                                                _type.ARGB],  # colorHigh
                                               _enum.GpStatus]
    GdipSetImageAttributesOutputChannel: _Callable[[_type.GpImageAttributes,  # imageattr
                                                    _enum.ColorAdjustType,  # type
                                                    _type.BOOL,  # enableFlag
                                                    _enum.ColorChannelFlags],  # channelFlags
                                                   _enum.GpStatus]
    GdipSetImageAttributesOutputChannelColorProfile: _Callable[[_type.GpImageAttributes,  # imageattr
                                                                _enum.ColorAdjustType,  # type
                                                                _type.BOOL,  # enableFlag
                                                                _Optional[_type.LPWSTR]],  # colorProfileFilename
                                                               _enum.GpStatus]
    GdipSetImageAttributesRemapTable: _Callable[[_type.GpImageAttributes,  # imageattr
                                                 _enum.ColorAdjustType,  # type
                                                 _type.BOOL,  # enableFlag
                                                 _type.UINT,  # mapSize
                                                 _Optional[_Pointer[_struct.ColorMap]]],  # map
                                                _enum.GpStatus]
    GdipSetImageAttributesWrapMode: _Callable[[_type.GpImageAttributes,  # imageAttr
                                               _enum.WrapMode,  # wrap
                                               _type.ARGB,  # argb
                                               _type.BOOL],  # clamp
                                              _enum.GpStatus]
    GdipSetImageAttributesICMMode: _Callable[[_type.GpImageAttributes,  # imageAttr
                                              _type.BOOL],  # on
                                             _enum.GpStatus]
    GdipGetImageAttributesAdjustedPalette: _Callable[[_type.GpImageAttributes,  # imageAttr
                                                      _Pointer[_struct.ColorPalette],  # colorPalette
                                                      _enum.ColorAdjustType],  # colorAdjustType
                                                     _enum.GpStatus]
    GdipFlush: _Callable[[_type.GpGraphics,  # graphics
                          _enum.GpFlushIntention],  # intention
                         _enum.GpStatus]
    GdipCreateFromHDC: _Callable[[_type.HDC,  # hdc
                                  _Pointer[_type.GpGraphics]],  # graphics
                                 _enum.GpStatus]
    GdipCreateFromHDC2: _Callable[[_type.HDC,  # hdc
                                   _type.HANDLE,  # hDevice
                                   _Pointer[_type.GpGraphics]],  # graphics
                                  _enum.GpStatus]
    GdipCreateFromHWND: _Callable[[_type.HWND,  # hwnd
                                   _Pointer[_type.GpGraphics]],  # graphics
                                  _enum.GpStatus]
    GdipCreateFromHWNDICM: _Callable[[_type.HWND,  # hwnd
                                      _Pointer[_type.GpGraphics]],  # graphics
                                     _enum.GpStatus]
    GdipDeleteGraphics: _Callable[[_type.GpGraphics],  # graphics
                                  _enum.GpStatus]
    GdipGetDC: _Callable[[_type.GpGraphics,  # graphics
                          _Pointer[_type.HDC]],  # hdc
                         _enum.GpStatus]
    GdipReleaseDC: _Callable[[_type.GpGraphics,  # graphics
                              _type.HDC],  # hdc
                             _enum.GpStatus]
    GdipSetCompositingMode: _Callable[[_type.GpGraphics,  # graphics
                                       _enum.CompositingMode],  # compositingMode
                                      _enum.GpStatus]
    GdipGetCompositingMode: _Callable[[_type.GpGraphics,  # graphics
                                       _Pointer[_enum.CompositingMode]],  # compositingMode
                                      _enum.GpStatus]
    GdipSetRenderingOrigin: _Callable[[_type.GpGraphics,  # graphics
                                       _type.INT,  # x
                                       _type.INT],  # y
                                      _enum.GpStatus]
    GdipGetRenderingOrigin: _Callable[[_type.GpGraphics,  # graphics
                                       _Pointer[_type.INT],  # x
                                       _Pointer[_type.INT]],  # y
                                      _enum.GpStatus]
    GdipSetCompositingQuality: _Callable[[_type.GpGraphics,  # graphics
                                          _enum.CompositingQuality],  # compositingQuality
                                         _enum.GpStatus]
    GdipGetCompositingQuality: _Callable[[_type.GpGraphics,  # graphics
                                          _Pointer[_enum.CompositingQuality]],  # compositingQuality
                                         _enum.GpStatus]
    GdipSetSmoothingMode: _Callable[[_type.GpGraphics,  # graphics
                                     _enum.SmoothingMode],  # smoothingMode
                                    _enum.GpStatus]
    GdipGetSmoothingMode: _Callable[[_type.GpGraphics,  # graphics
                                     _Pointer[_enum.SmoothingMode]],  # smoothingMode
                                    _enum.GpStatus]
    GdipSetPixelOffsetMode: _Callable[[_type.GpGraphics,  # graphics
                                       _enum.PixelOffsetMode],  # pixelOffsetMode
                                      _enum.GpStatus]
    GdipGetPixelOffsetMode: _Callable[[_type.GpGraphics,  # graphics
                                       _Pointer[_enum.PixelOffsetMode]],  # pixelOffsetMode
                                      _enum.GpStatus]
    GdipSetTextRenderingHint: _Callable[[_type.GpGraphics,  # graphics
                                         _enum.TextRenderingHint],  # mode
                                        _enum.GpStatus]
    GdipGetTextRenderingHint: _Callable[[_type.GpGraphics,  # graphics
                                         _Pointer[_enum.TextRenderingHint]],  # mode
                                        _enum.GpStatus]
    GdipSetTextContrast: _Callable[[_type.GpGraphics,  # graphics
                                    _type.UINT],  # contrast
                                   _enum.GpStatus]
    GdipGetTextContrast: _Callable[[_type.GpGraphics,  # graphics
                                    _Pointer[_type.UINT]],  # contrast
                                   _enum.GpStatus]
    GdipSetInterpolationMode: _Callable[[_type.GpGraphics,  # graphics
                                         _enum.InterpolationMode],  # interpolationMode
                                        _enum.GpStatus]
    GdipGetInterpolationMode: _Callable[[_type.GpGraphics,  # graphics
                                         _Pointer[_enum.InterpolationMode]],  # interpolationMode
                                        _enum.GpStatus]
    GdipSetWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                      _type.GpMatrix],  # matrix
                                     _enum.GpStatus]
    GdipResetWorldTransform: _Callable[[_type.GpGraphics],  # graphics
                                       _enum.GpStatus]
    GdipMultiplyWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                           _type.GpMatrix,  # matrix
                                           _enum.GpMatrixOrder],  # order
                                          _enum.GpStatus]
    GdipTranslateWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                            _type.REAL,  # dx
                                            _type.REAL,  # dy
                                            _enum.GpMatrixOrder],  # order
                                           _enum.GpStatus]
    GdipScaleWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                        _type.REAL,  # sx
                                        _type.REAL,  # sy
                                        _enum.GpMatrixOrder],  # order
                                       _enum.GpStatus]
    GdipRotateWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                         _type.REAL,  # angle
                                         _enum.GpMatrixOrder],  # order
                                        _enum.GpStatus]
    GdipGetWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                      _type.GpMatrix],  # matrix
                                     _enum.GpStatus]
    GdipResetPageTransform: _Callable[[_type.GpGraphics],  # graphics
                                      _enum.GpStatus]
    GdipGetPageUnit: _Callable[[_type.GpGraphics,  # graphics
                                _Pointer[_enum.GpUnit]],  # unit
                               _enum.GpStatus]
    GdipGetPageScale: _Callable[[_type.GpGraphics,  # graphics
                                 _Pointer[_type.REAL]],  # scale
                                _enum.GpStatus]
    GdipSetPageUnit: _Callable[[_type.GpGraphics,  # graphics
                                _enum.GpUnit],  # unit
                               _enum.GpStatus]
    GdipSetPageScale: _Callable[[_type.GpGraphics,  # graphics
                                 _type.REAL],  # scale
                                _enum.GpStatus]
    GdipGetDpiX: _Callable[[_type.GpGraphics,  # graphics
                            _Pointer[_type.REAL]],  # dpi
                           _enum.GpStatus]
    GdipGetDpiY: _Callable[[_type.GpGraphics,  # graphics
                            _Pointer[_type.REAL]],  # dpi
                           _enum.GpStatus]
    GdipTransformPoints: _Callable[[_type.GpGraphics,  # graphics
                                    _enum.GpCoordinateSpace,  # destSpace
                                    _enum.GpCoordinateSpace,  # srcSpace
                                    _Pointer[_struct.GpPointF],  # points
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipTransformPointsI: _Callable[[_type.GpGraphics,  # graphics
                                     _enum.GpCoordinateSpace,  # destSpace
                                     _enum.GpCoordinateSpace,  # srcSpace
                                     _Pointer[_struct.GpPoint],  # points
                                     _type.INT],  # count
                                    _enum.GpStatus]
    GdipGetNearestColor: _Callable[[_type.GpGraphics,  # graphics
                                    _Pointer[_type.ARGB]],  # argb
                                   _enum.GpStatus]
    GdipDrawLine: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpPen,  # pen
                             _type.REAL,  # x1
                             _type.REAL,  # y1
                             _type.REAL,  # x2
                             _type.REAL],  # y2
                            _enum.GpStatus]
    GdipDrawLineI: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpPen,  # pen
                              _type.INT,  # x1
                              _type.INT,  # y1
                              _type.INT,  # x2
                              _type.INT],  # y2
                             _enum.GpStatus]
    GdipDrawLines: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpPen,  # pen
                              _Pointer[_struct.GpPointF],  # points
                              _type.INT],  # count
                             _enum.GpStatus]
    GdipDrawLinesI: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpPen,  # pen
                               _Pointer[_struct.GpPoint],  # points
                               _type.INT],  # count
                              _enum.GpStatus]
    GdipDrawArc: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _type.REAL,  # x
                            _type.REAL,  # y
                            _type.REAL,  # width
                            _type.REAL,  # height
                            _type.REAL,  # startAngle
                            _type.REAL],  # sweepAngle
                           _enum.GpStatus]
    GdipDrawArcI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpPen,  # pen
                             _type.INT,  # x
                             _type.INT,  # y
                             _type.INT,  # width
                             _type.INT,  # height
                             _type.REAL,  # startAngle
                             _type.REAL],  # sweepAngle
                            _enum.GpStatus]
    GdipDrawBezier: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpPen,  # pen
                               _type.REAL,  # x1
                               _type.REAL,  # y1
                               _type.REAL,  # x2
                               _type.REAL,  # y2
                               _type.REAL,  # x3
                               _type.REAL,  # y3
                               _type.REAL,  # x4
                               _type.REAL],  # y4
                              _enum.GpStatus]
    GdipDrawBezierI: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _type.INT,  # x1
                                _type.INT,  # y1
                                _type.INT,  # x2
                                _type.INT,  # y2
                                _type.INT,  # x3
                                _type.INT,  # y3
                                _type.INT,  # x4
                                _type.INT],  # y4
                               _enum.GpStatus]
    GdipDrawBeziers: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _Pointer[_struct.GpPointF],  # points
                                _type.INT],  # count
                               _enum.GpStatus]
    GdipDrawBeziersI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpPen,  # pen
                                 _Pointer[_struct.GpPoint],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipDrawRectangle: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpPen,  # pen
                                  _type.REAL,  # x
                                  _type.REAL,  # y
                                  _type.REAL,  # width
                                  _type.REAL],  # height
                                 _enum.GpStatus]
    GdipDrawRectangleI: _Callable[[_type.GpGraphics,  # graphics
                                   _type.GpPen,  # pen
                                   _type.INT,  # x
                                   _type.INT,  # y
                                   _type.INT,  # width
                                   _type.INT],  # height
                                  _enum.GpStatus]
    GdipDrawRectangles: _Callable[[_type.GpGraphics,  # graphics
                                   _type.GpPen,  # pen
                                   _Pointer[_struct.GpRectF],  # rects
                                   _type.INT],  # count
                                  _enum.GpStatus]
    GdipDrawRectanglesI: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpPen,  # pen
                                    _Pointer[_struct.GpRect],  # rects
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipDrawEllipse: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _type.REAL,  # x
                                _type.REAL,  # y
                                _type.REAL,  # width
                                _type.REAL],  # height
                               _enum.GpStatus]
    GdipDrawEllipseI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpPen,  # pen
                                 _type.INT,  # x
                                 _type.INT,  # y
                                 _type.INT,  # width
                                 _type.INT],  # height
                                _enum.GpStatus]
    GdipDrawPie: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _type.REAL,  # x
                            _type.REAL,  # y
                            _type.REAL,  # width
                            _type.REAL,  # height
                            _type.REAL,  # startAngle
                            _type.REAL],  # sweepAngle
                           _enum.GpStatus]
    GdipDrawPieI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpPen,  # pen
                             _type.INT,  # x
                             _type.INT,  # y
                             _type.INT,  # width
                             _type.INT,  # height
                             _type.REAL,  # startAngle
                             _type.REAL],  # sweepAngle
                            _enum.GpStatus]
    GdipDrawPolygon: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _Pointer[_struct.GpPointF],  # points
                                _type.INT],  # count
                               _enum.GpStatus]
    GdipDrawPolygonI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpPen,  # pen
                                 _Pointer[_struct.GpPoint],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipDrawPath: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpPen,  # pen
                             _type.GpPath],  # path
                            _enum.GpStatus]
    GdipDrawCurve: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpPen,  # pen
                              _Pointer[_struct.GpPointF],  # points
                              _type.INT],  # count
                             _enum.GpStatus]
    GdipDrawCurveI: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpPen,  # pen
                               _Pointer[_struct.GpPoint],  # points
                               _type.INT],  # count
                              _enum.GpStatus]
    GdipDrawCurve2: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpPen,  # pen
                               _Pointer[_struct.GpPointF],  # points
                               _type.INT,  # count
                               _type.REAL],  # tension
                              _enum.GpStatus]
    GdipDrawCurve2I: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _Pointer[_struct.GpPoint],  # points
                                _type.INT,  # count
                                _type.REAL],  # tension
                               _enum.GpStatus]
    GdipDrawCurve3: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpPen,  # pen
                               _Pointer[_struct.GpPointF],  # points
                               _type.INT,  # count
                               _type.INT,  # offset
                               _type.INT,  # numberOfSegments
                               _type.REAL],  # tension
                              _enum.GpStatus]
    GdipDrawCurve3I: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _Pointer[_struct.GpPoint],  # points
                                _type.INT,  # count
                                _type.INT,  # offset
                                _type.INT,  # numberOfSegments
                                _type.REAL],  # tension
                               _enum.GpStatus]
    GdipDrawClosedCurve: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpPen,  # pen
                                    _Pointer[_struct.GpPointF],  # points
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipDrawClosedCurveI: _Callable[[_type.GpGraphics,  # graphics
                                     _type.GpPen,  # pen
                                     _Pointer[_struct.GpPoint],  # points
                                     _type.INT],  # count
                                    _enum.GpStatus]
    GdipDrawClosedCurve2: _Callable[[_type.GpGraphics,  # graphics
                                     _type.GpPen,  # pen
                                     _Pointer[_struct.GpPointF],  # points
                                     _type.INT,  # count
                                     _type.REAL],  # tension
                                    _enum.GpStatus]
    GdipDrawClosedCurve2I: _Callable[[_type.GpGraphics,  # graphics
                                      _type.GpPen,  # pen
                                      _Pointer[_struct.GpPoint],  # points
                                      _type.INT,  # count
                                      _type.REAL],  # tension
                                     _enum.GpStatus]
    GdipGraphicsClear: _Callable[[_type.GpGraphics,  # graphics
                                  _type.ARGB],  # color
                                 _enum.GpStatus]
    GdipFillRectangle: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpBrush,  # brush
                                  _type.REAL,  # x
                                  _type.REAL,  # y
                                  _type.REAL,  # width
                                  _type.REAL],  # height
                                 _enum.GpStatus]
    GdipFillRectangleI: _Callable[[_type.GpGraphics,  # graphics
                                   _type.GpBrush,  # brush
                                   _type.INT,  # x
                                   _type.INT,  # y
                                   _type.INT,  # width
                                   _type.INT],  # height
                                  _enum.GpStatus]
    GdipFillRectangles: _Callable[[_type.GpGraphics,  # graphics
                                   _type.GpBrush,  # brush
                                   _Pointer[_struct.GpRectF],  # rects
                                   _type.INT],  # count
                                  _enum.GpStatus]
    GdipFillRectanglesI: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpBrush,  # brush
                                    _Pointer[_struct.GpRect],  # rects
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipFillPolygon: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpBrush,  # brush
                                _Pointer[_struct.GpPointF],  # points
                                _type.INT,  # count
                                _enum.GpFillMode],  # fillMode
                               _enum.GpStatus]
    GdipFillPolygonI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpBrush,  # brush
                                 _Pointer[_struct.GpPoint],  # points
                                 _type.INT,  # count
                                 _enum.GpFillMode],  # fillMode
                                _enum.GpStatus]
    GdipFillPolygon2: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpBrush,  # brush
                                 _Pointer[_struct.GpPointF],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
    GdipFillPolygon2I: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpBrush,  # brush
                                  _Pointer[_struct.GpPoint],  # points
                                  _type.INT],  # count
                                 _enum.GpStatus]
    GdipFillEllipse: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpBrush,  # brush
                                _type.REAL,  # x
                                _type.REAL,  # y
                                _type.REAL,  # width
                                _type.REAL],  # height
                               _enum.GpStatus]
    GdipFillEllipseI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpBrush,  # brush
                                 _type.INT,  # x
                                 _type.INT,  # y
                                 _type.INT,  # width
                                 _type.INT],  # height
                                _enum.GpStatus]
    GdipFillPie: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpBrush,  # brush
                            _type.REAL,  # x
                            _type.REAL,  # y
                            _type.REAL,  # width
                            _type.REAL,  # height
                            _type.REAL,  # startAngle
                            _type.REAL],  # sweepAngle
                           _enum.GpStatus]
    GdipFillPieI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpBrush,  # brush
                             _type.INT,  # x
                             _type.INT,  # y
                             _type.INT,  # width
                             _type.INT,  # height
                             _type.REAL,  # startAngle
                             _type.REAL],  # sweepAngle
                            _enum.GpStatus]
    GdipFillPath: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpBrush,  # brush
                             _type.GpPath],  # path
                            _enum.GpStatus]
    GdipFillClosedCurve: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpBrush,  # brush
                                    _Pointer[_struct.GpPointF],  # points
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipFillClosedCurveI: _Callable[[_type.GpGraphics,  # graphics
                                     _type.GpBrush,  # brush
                                     _Pointer[_struct.GpPoint],  # points
                                     _type.INT],  # count
                                    _enum.GpStatus]
    GdipFillClosedCurve2: _Callable[[_type.GpGraphics,  # graphics
                                     _type.GpBrush,  # brush
                                     _Pointer[_struct.GpPointF],  # points
                                     _type.INT,  # count
                                     _type.REAL,  # tension
                                     _enum.GpFillMode],  # fillMode
                                    _enum.GpStatus]
    GdipFillClosedCurve2I: _Callable[[_type.GpGraphics,  # graphics
                                      _type.GpBrush,  # brush
                                      _Pointer[_struct.GpPoint],  # points
                                      _type.INT,  # count
                                      _type.REAL,  # tension
                                      _enum.GpFillMode],  # fillMode
                                     _enum.GpStatus]
    GdipFillRegion: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpBrush,  # brush
                               _type.GpRegion],  # region
                              _enum.GpStatus]
    GdipDrawImage: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpImage,  # image
                              _type.REAL,  # x
                              _type.REAL],  # y
                             _enum.GpStatus]
    GdipDrawImageI: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpImage,  # image
                               _type.INT,  # x
                               _type.INT],  # y
                              _enum.GpStatus]
    GdipDrawImageRect: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpImage,  # image
                                  _type.REAL,  # x
                                  _type.REAL,  # y
                                  _type.REAL,  # width
                                  _type.REAL],  # height
                                 _enum.GpStatus]
    GdipDrawImageRectI: _Callable[[_type.GpGraphics,  # graphics
                                   _type.GpImage,  # image
                                   _type.INT,  # x
                                   _type.INT,  # y
                                   _type.INT,  # width
                                   _type.INT],  # height
                                  _enum.GpStatus]
    GdipDrawImagePoints: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpImage,  # image
                                    _Pointer[_struct.GpPointF],  # dstpoints
                                    _type.INT],  # count
                                   _enum.GpStatus]
    GdipDrawImagePointsI: _Callable[[_type.GpGraphics,  # graphics
                                     _type.GpImage,  # image
                                     _Pointer[_struct.GpPoint],  # dstpoints
                                     _type.INT],  # count
                                    _enum.GpStatus]
    GdipDrawImagePointRect: _Callable[[_type.GpGraphics,  # graphics
                                       _type.GpImage,  # image
                                       _type.REAL,  # x
                                       _type.REAL,  # y
                                       _type.REAL,  # srcx
                                       _type.REAL,  # srcy
                                       _type.REAL,  # srcwidth
                                       _type.REAL,  # srcheight
                                       _enum.GpUnit],  # srcUnit
                                      _enum.GpStatus]
    GdipDrawImagePointRectI: _Callable[[_type.GpGraphics,  # graphics
                                        _type.GpImage,  # image
                                        _type.INT,  # x
                                        _type.INT,  # y
                                        _type.INT,  # srcx
                                        _type.INT,  # srcy
                                        _type.INT,  # srcwidth
                                        _type.INT,  # srcheight
                                        _enum.GpUnit],  # srcUnit
                                       _enum.GpStatus]
    GdipDrawImageRectRect: _Callable[[_type.GpGraphics,  # graphics
                                      _type.GpImage,  # image
                                      _type.REAL,  # dstx
                                      _type.REAL,  # dsty
                                      _type.REAL,  # dstwidth
                                      _type.REAL,  # dstheight
                                      _type.REAL,  # srcx
                                      _type.REAL,  # srcy
                                      _type.REAL,  # srcwidth
                                      _type.REAL,  # srcheight
                                      _enum.GpUnit,  # srcUnit
                                      _Optional[_type.GpImageAttributes],  # imageAttributes
                                      _type.DrawImageAbort,  # callback  TODO _Optional _FuncPtr
                                      _Optional[_Pointer[_type.VOID]]],  # callbackData
                                     _enum.GpStatus]
    GdipDrawImageRectRectI: _Callable[[_type.GpGraphics,  # graphics
                                       _type.GpImage,  # image
                                       _type.INT,  # dstx
                                       _type.INT,  # dsty
                                       _type.INT,  # dstwidth
                                       _type.INT,  # dstheight
                                       _type.INT,  # srcx
                                       _type.INT,  # srcy
                                       _type.INT,  # srcwidth
                                       _type.INT,  # srcheight
                                       _enum.GpUnit,  # srcUnit
                                       _Optional[_type.GpImageAttributes],  # imageAttributes
                                       _type.DrawImageAbort,  # callback
                                       _Optional[_Pointer[_type.VOID]]],  # callbackData
                                      _enum.GpStatus]
    GdipDrawImagePointsRect: _Callable[[_type.GpGraphics,  # graphics
                                        _type.GpImage,  # image
                                        _Pointer[_struct.GpPointF],  # points
                                        _type.INT,  # count
                                        _type.REAL,  # srcx
                                        _type.REAL,  # srcy
                                        _type.REAL,  # srcwidth
                                        _type.REAL,  # srcheight
                                        _enum.GpUnit,  # srcUnit
                                        _Optional[_type.GpImageAttributes],  # imageAttributes
                                        _type.DrawImageAbort,  # callback
                                        _Optional[_Pointer[_type.VOID]]],  # callbackData
                                       _enum.GpStatus]
    GdipDrawImagePointsRectI: _Callable[[_type.GpGraphics,  # graphics
                                         _type.GpImage,  # image
                                         _Pointer[_struct.GpPoint],  # points
                                         _type.INT,  # count
                                         _type.INT,  # srcx
                                         _type.INT,  # srcy
                                         _type.INT,  # srcwidth
                                         _type.INT,  # srcheight
                                         _enum.GpUnit,  # srcUnit
                                         _Optional[_type.GpImageAttributes],  # imageAttributes
                                         _type.DrawImageAbort,  # callback
                                         _Optional[_Pointer[_type.VOID]]],  # callbackData
                                        _enum.GpStatus]
    GdipEnumerateMetafileDestPoint: _Callable[[_type.GpGraphics,  # graphics
                                               _type.GpMetafile,  # metafile
                                               _Pointer[_struct.PointF],  # destPoint
                                               _type.EnumerateMetafileProc,  # callback
                                               _Pointer[_type.VOID],  # callbackData
                                               _type.GpImageAttributes],  # imageAttributes
                                              _enum.GpStatus]
    GdipEnumerateMetafileDestPointI: _Callable[[_type.GpGraphics,  # graphics
                                                _type.GpMetafile,  # metafile
                                                _Pointer[_struct.Point],  # destPoint
                                                _type.EnumerateMetafileProc,  # callback
                                                _Pointer[_type.VOID],  # callbackData
                                                _type.GpImageAttributes],  # imageAttributes
                                               _enum.GpStatus]
    GdipEnumerateMetafileDestRect: _Callable[[_type.GpGraphics,  # graphics
                                              _type.GpMetafile,  # metafile
                                              _Pointer[_struct.RectF],  # destRect
                                              _type.EnumerateMetafileProc,  # callback
                                              _Pointer[_type.VOID],  # callbackData
                                              _type.GpImageAttributes],  # imageAttributes
                                             _enum.GpStatus]
    GdipEnumerateMetafileDestRectI: _Callable[[_type.GpGraphics,  # graphics
                                               _type.GpMetafile,  # metafile
                                               _Pointer[_struct.Rect],  # destRect
                                               _type.EnumerateMetafileProc,  # callback
                                               _Pointer[_type.VOID],  # callbackData
                                               _type.GpImageAttributes],  # imageAttributes
                                              _enum.GpStatus]
    GdipEnumerateMetafileDestPoints: _Callable[[_type.GpGraphics,  # graphics
                                                _type.GpMetafile,  # metafile
                                                _Pointer[_struct.PointF],  # destPoints
                                                _type.INT,  # count
                                                _type.EnumerateMetafileProc,  # callback
                                                _Pointer[_type.VOID],  # callbackData
                                                _type.GpImageAttributes],  # imageAttributes
                                               _enum.GpStatus]
    GdipEnumerateMetafileDestPointsI: _Callable[[_type.GpGraphics,  # graphics
                                                 _type.GpMetafile,  # metafile
                                                 _Pointer[_struct.Point],  # destPoints
                                                 _type.INT,  # count
                                                 _type.EnumerateMetafileProc,  # callback
                                                 _Pointer[_type.VOID],  # callbackData
                                                 _type.GpImageAttributes],  # imageAttributes
                                                _enum.GpStatus]
    GdipEnumerateMetafileSrcRectDestPoint: _Callable[[_type.GpGraphics,  # graphics
                                                      _type.GpMetafile,  # metafile
                                                      _Pointer[_struct.PointF],  # destPoint
                                                      _Pointer[_struct.RectF],  # srcRect
                                                      _enum.Unit,  # srcUnit
                                                      _type.EnumerateMetafileProc,  # callback
                                                      _Pointer[_type.VOID],  # callbackData
                                                      _type.GpImageAttributes],  # imageAttributes
                                                     _enum.GpStatus]
    GdipEnumerateMetafileSrcRectDestPointI: _Callable[[_type.GpGraphics,  # graphics
                                                       _type.GpMetafile,  # metafile
                                                       _Pointer[_struct.Point],  # destPoint
                                                       _Pointer[_struct.Rect],  # srcRect
                                                       _enum.Unit,  # srcUnit
                                                       _type.EnumerateMetafileProc,  # callback
                                                       _Pointer[_type.VOID],  # callbackData
                                                       _type.GpImageAttributes],  # imageAttributes
                                                      _enum.GpStatus]
    GdipEnumerateMetafileSrcRectDestRect: _Callable[[_type.GpGraphics,  # graphics
                                                     _type.GpMetafile,  # metafile
                                                     _Pointer[_struct.RectF],  # destRect
                                                     _Pointer[_struct.RectF],  # srcRect
                                                     _enum.Unit,  # srcUnit
                                                     _type.EnumerateMetafileProc,  # callback
                                                     _Pointer[_type.VOID],  # callbackData
                                                     _type.GpImageAttributes],  # imageAttributes
                                                    _enum.GpStatus]
    GdipEnumerateMetafileSrcRectDestRectI: _Callable[[_type.GpGraphics,  # graphics
                                                      _type.GpMetafile,  # metafile
                                                      _Pointer[_struct.Rect],  # destRect
                                                      _Pointer[_struct.Rect],  # srcRect
                                                      _enum.Unit,  # srcUnit
                                                      _type.EnumerateMetafileProc,  # callback
                                                      _Pointer[_type.VOID],  # callbackData
                                                      _type.GpImageAttributes],  # imageAttributes
                                                     _enum.GpStatus]
    GdipEnumerateMetafileSrcRectDestPoints: _Callable[[_type.GpGraphics,  # graphics
                                                       _type.GpMetafile,  # metafile
                                                       _Pointer[_struct.PointF],  # destPoints
                                                       _type.INT,  # count
                                                       _Pointer[_struct.RectF],  # srcRect
                                                       _enum.Unit,  # srcUnit
                                                       _type.EnumerateMetafileProc,  # callback
                                                       _Pointer[_type.VOID],  # callbackData
                                                       _type.GpImageAttributes],  # imageAttributes
                                                      _enum.GpStatus]
    GdipEnumerateMetafileSrcRectDestPointsI: _Callable[[_type.GpGraphics,  # graphics
                                                        _type.GpMetafile,  # metafile
                                                        _Pointer[_struct.Point],  # destPoints
                                                        _type.INT,  # count
                                                        _Pointer[_struct.Rect],  # srcRect
                                                        _enum.Unit,  # srcUnit
                                                        _type.EnumerateMetafileProc,  # callback
                                                        _Pointer[_type.VOID],  # callbackData
                                                        _type.GpImageAttributes],  # imageAttributes
                                                       _enum.GpStatus]
    GdipPlayMetafileRecord: _Callable[[_type.GpMetafile,  # metafile
                                       _type.EmfPlusRecordType,  # recordType
                                       _type.UINT,  # flags
                                       _type.UINT,  # dataSize
                                       _Pointer[_type.BYTE]],  # data
                                      _enum.GpStatus]
    GdipSetClipGraphics: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpGraphics,  # srcgraphics
                                    _enum.CombineMode],  # combineMode
                                   _enum.GpStatus]
    GdipSetClipRect: _Callable[[_type.GpGraphics,  # graphics
                                _type.REAL,  # x
                                _type.REAL,  # y
                                _type.REAL,  # width
                                _type.REAL,  # height
                                _enum.CombineMode],  # combineMode
                               _enum.GpStatus]
    GdipSetClipRectI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.INT,  # x
                                 _type.INT,  # y
                                 _type.INT,  # width
                                 _type.INT,  # height
                                 _enum.CombineMode],  # combineMode
                                _enum.GpStatus]
    GdipSetClipPath: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPath,  # path
                                _enum.CombineMode],  # combineMode
                               _enum.GpStatus]
    GdipSetClipRegion: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpRegion,  # region
                                  _enum.CombineMode],  # combineMode
                                 _enum.GpStatus]
    GdipSetClipHrgn: _Callable[[_type.GpGraphics,  # graphics
                                _type.HRGN,  # hRgn
                                _enum.CombineMode],  # combineMode
                               _enum.GpStatus]
    GdipResetClip: _Callable[[_type.GpGraphics],  # graphics
                             _enum.GpStatus]
    GdipTranslateClip: _Callable[[_type.GpGraphics,  # graphics
                                  _type.REAL,  # dx
                                  _type.REAL],  # dy
                                 _enum.GpStatus]
    GdipTranslateClipI: _Callable[[_type.GpGraphics,  # graphics
                                   _type.INT,  # dx
                                   _type.INT],  # dy
                                  _enum.GpStatus]
    GdipGetClip: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpRegion],  # region
                           _enum.GpStatus]
    GdipGetClipBounds: _Callable[[_type.GpGraphics,  # graphics
                                  _Pointer[_struct.GpRectF]],  # rect
                                 _enum.GpStatus]
    GdipGetClipBoundsI: _Callable[[_type.GpGraphics,  # graphics
                                   _Pointer[_struct.GpRect]],  # rect
                                  _enum.GpStatus]
    GdipIsClipEmpty: _Callable[[_type.GpGraphics,  # graphics
                                _Pointer[_type.BOOL]],  # result
                               _enum.GpStatus]
    GdipGetVisibleClipBounds: _Callable[[_type.GpGraphics,  # graphics
                                         _Pointer[_struct.GpRectF]],  # rect
                                        _enum.GpStatus]
    GdipGetVisibleClipBoundsI: _Callable[[_type.GpGraphics,  # graphics
                                          _Pointer[_struct.GpRect]],  # rect
                                         _enum.GpStatus]
    GdipIsVisibleClipEmpty: _Callable[[_type.GpGraphics,  # graphics
                                       _Pointer[_type.BOOL]],  # result
                                      _enum.GpStatus]
    GdipIsVisiblePoint: _Callable[[_type.GpGraphics,  # graphics
                                   _type.REAL,  # x
                                   _type.REAL,  # y
                                   _Pointer[_type.BOOL]],  # result
                                  _enum.GpStatus]
    GdipIsVisiblePointI: _Callable[[_type.GpGraphics,  # graphics
                                    _type.INT,  # x
                                    _type.INT,  # y
                                    _Pointer[_type.BOOL]],  # result
                                   _enum.GpStatus]
    GdipIsVisibleRect: _Callable[[_type.GpGraphics,  # graphics
                                  _type.REAL,  # x
                                  _type.REAL,  # y
                                  _type.REAL,  # width
                                  _type.REAL,  # height
                                  _Pointer[_type.BOOL]],  # result
                                 _enum.GpStatus]
    GdipIsVisibleRectI: _Callable[[_type.GpGraphics,  # graphics
                                   _type.INT,  # x
                                   _type.INT,  # y
                                   _type.INT,  # width
                                   _type.INT,  # height
                                   _Pointer[_type.BOOL]],  # result
                                  _enum.GpStatus]
    GdipSaveGraphics: _Callable[[_type.GpGraphics,  # graphics
                                 _Pointer[_type.GraphicsState]],  # state
                                _enum.GpStatus]
    GdipRestoreGraphics: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GraphicsState],  # state
                                   _enum.GpStatus]
    GdipBeginContainer: _Callable[[_type.GpGraphics,  # graphics
                                   _Pointer[_struct.GpRectF],  # dstrect
                                   _Pointer[_struct.GpRectF],  # srcrect
                                   _enum.GpUnit,  # unit
                                   _Pointer[_type.GraphicsContainer]],  # state
                                  _enum.GpStatus]
    GdipBeginContainerI: _Callable[[_type.GpGraphics,  # graphics
                                    _Pointer[_struct.GpRect],  # dstrect
                                    _Pointer[_struct.GpRect],  # srcrect
                                    _enum.GpUnit,  # unit
                                    _Pointer[_type.GraphicsContainer]],  # state
                                   _enum.GpStatus]
    GdipBeginContainer2: _Callable[[_type.GpGraphics,  # graphics
                                    _Pointer[_type.GraphicsContainer]],  # state
                                   _enum.GpStatus]
    GdipEndContainer: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GraphicsContainer],  # state
                                _enum.GpStatus]
    GdipCreateStreamOnFile: _Callable[[_type.LPWSTR,  # filename
                                       _type.UINT,  # access
                                       _Pointer[_interface.IStream]],  # stream
                                      _enum.GpStatus]
    GdipCreateMetafileFromWmf: _Callable[[_type.HMETAFILE,  # hWmf
                                          _type.BOOL,  # deleteWmf
                                          _Pointer[_struct.WmfPlaceableFileHeader],  # wmfPlaceableFileHeader
                                          _Pointer[_type.GpMetafile]],  # metafile
                                         _enum.GpStatus]
    GdipCreateMetafileFromEmf: _Callable[[_type.HENHMETAFILE,  # hEmf
                                          _type.BOOL,  # deleteEmf
                                          _Pointer[_type.GpMetafile]],  # metafile
                                         _enum.GpStatus]
    GdipCreateMetafileFromFile: _Callable[[_type.LPWSTR,  # file
                                           _Pointer[_type.GpMetafile]],  # metafile
                                          _enum.GpStatus]
    GdipCreateMetafileFromWmfFile: _Callable[[_type.LPWSTR,  # file
                                              _Pointer[_struct.WmfPlaceableFileHeader],  # wmfPlaceableFileHeader
                                              _Pointer[_type.GpMetafile]],  # metafile
                                             _enum.GpStatus]
    GdipCreateMetafileFromStream: _Callable[[_interface.IStream,  # stream
                                             _Pointer[_type.GpMetafile]],  # metafile
                                            _enum.GpStatus]
    GdipRecordMetafile: _Callable[[_type.HDC,  # referenceHdc
                                   _enum.EmfType,  # type
                                   _Pointer[_struct.GpRectF],  # frameRect
                                   _enum.MetafileFrameUnit,  # frameUnit
                                   _type.LPWSTR,  # description
                                   _Pointer[_type.GpMetafile]],  # metafile
                                  _enum.GpStatus]
    GdipRecordMetafileI: _Callable[[_type.HDC,  # referenceHdc
                                    _enum.EmfType,  # type
                                    _Pointer[_struct.GpRect],  # frameRect
                                    _enum.MetafileFrameUnit,  # frameUnit
                                    _type.LPWSTR,  # description
                                    _Pointer[_type.GpMetafile]],  # metafile
                                   _enum.GpStatus]
    GdipRecordMetafileFileName: _Callable[[_type.LPWSTR,  # fileName
                                           _type.HDC,  # referenceHdc
                                           _enum.EmfType,  # type
                                           _Pointer[_struct.GpRectF],  # frameRect
                                           _enum.MetafileFrameUnit,  # frameUnit
                                           _type.LPWSTR,  # description
                                           _Pointer[_type.GpMetafile]],  # metafile
                                          _enum.GpStatus]
    GdipRecordMetafileFileNameI: _Callable[[_type.LPWSTR,  # fileName
                                            _type.HDC,  # referenceHdc
                                            _enum.EmfType,  # type
                                            _Pointer[_struct.GpRect],  # frameRect
                                            _enum.MetafileFrameUnit,  # frameUnit
                                            _type.LPWSTR,  # description
                                            _Pointer[_type.GpMetafile]],  # metafile
                                           _enum.GpStatus]
    GdipRecordMetafileStream: _Callable[[_interface.IStream,  # stream
                                         _type.HDC,  # referenceHdc
                                         _enum.EmfType,  # type
                                         _Pointer[_struct.GpRectF],  # frameRect
                                         _enum.MetafileFrameUnit,  # frameUnit
                                         _type.LPWSTR,  # description
                                         _Pointer[_type.GpMetafile]],  # metafile
                                        _enum.GpStatus]
    GdipRecordMetafileStreamI: _Callable[[_interface.IStream,  # stream
                                          _type.HDC,  # referenceHdc
                                          _enum.EmfType,  # type
                                          _Pointer[_struct.GpRect],  # frameRect
                                          _enum.MetafileFrameUnit,  # frameUnit
                                          _type.LPWSTR,  # description
                                          _Pointer[_type.GpMetafile]],  # metafile
                                         _enum.GpStatus]
    GdipSetMetafileDownLevelRasterizationLimit: _Callable[[_type.GpMetafile,  # metafile
                                                           _type.UINT],  # metafileRasterizationLimitDpi
                                                          _enum.GpStatus]
    GdipGetMetafileDownLevelRasterizationLimit: _Callable[[_type.GpMetafile,  # metafile
                                                           _Pointer[_type.UINT]],  # metafileRasterizationLimitDpi
                                                          _enum.GpStatus]
    GdipGetImageDecodersSize: _Callable[[_Pointer[_type.UINT],  # numDecoders
                                         _Pointer[_type.UINT]],  # size
                                        _enum.GpStatus]
    GdipGetImageDecoders: _Callable[[_type.UINT,  # numDecoders
                                     _type.UINT,  # size
                                     _Pointer[_struct.ImageCodecInfo]],  # decoders
                                    _enum.GpStatus]
    GdipGetImageEncodersSize: _Callable[[_Pointer[_type.UINT],  # numEncoders
                                         _Pointer[_type.UINT]],  # size
                                        _enum.GpStatus]
    GdipGetImageEncoders: _Callable[[_type.UINT,  # numEncoders
                                     _type.UINT,  # size
                                     _Pointer[_struct.ImageCodecInfo]],  # encoders
                                    _enum.GpStatus]
    GdipComment: _Callable[[_type.GpGraphics,  # graphics
                            _type.UINT,  # sizeData
                            _Pointer[_type.BYTE]],  # data
                           _enum.GpStatus]
    GdipCreateFontFamilyFromName: _Callable[[_type.LPWSTR,  # name
                                             _Optional[_type.GpFontCollection],  # fontCollection
                                             _Pointer[_type.GpFontFamily]],  # fontFamily
                                            _enum.GpStatus]
    GdipDeleteFontFamily: _Callable[[_type.GpFontFamily],  # fontFamily
                                    _enum.GpStatus]
    GdipCloneFontFamily: _Callable[[_type.GpFontFamily,  # fontFamily
                                    _Pointer[_type.GpFontFamily]],  # clonedFontFamily
                                   _enum.GpStatus]
    GdipGetGenericFontFamilySansSerif: _Callable[[_Pointer[_type.GpFontFamily]],  # nativeFamily
                                                 _enum.GpStatus]
    GdipGetGenericFontFamilySerif: _Callable[[_Pointer[_type.GpFontFamily]],  # nativeFamily
                                             _enum.GpStatus]
    GdipGetGenericFontFamilyMonospace: _Callable[[_Pointer[_type.GpFontFamily]],  # nativeFamily
                                                 _enum.GpStatus]
    GdipGetFamilyName: _Callable[[_type.GpFontFamily,  # family
                                  _type.LPWSTR,  # name
                                  _type.LANGID],  # language
                                 _enum.GpStatus]
    GdipIsStyleAvailable: _Callable[[_type.GpFontFamily,  # family
                                     _type.INT,  # style
                                     _Pointer[_type.BOOL]],  # isStyleAvailable
                                    _enum.GpStatus]
    GdipFontCollectionEnumerable: _Callable[[_type.GpFontCollection,  # fontCollection
                                             _type.GpGraphics,  # graphics
                                             _Pointer[_type.INT]],  # numFound
                                            _enum.GpStatus]
    GdipFontCollectionEnumerate: _Callable[[_type.GpFontCollection,  # fontCollection
                                            _type.INT,  # numSought
                                            _type.GpFontFamily,  # gpfamilies[]
                                            _Pointer[_type.INT],  # numFound
                                            _type.GpGraphics],  # graphics
                                           _enum.GpStatus]
    GdipGetEmHeight: _Callable[[_type.GpFontFamily,  # family
                                _type.INT,  # style
                                _Pointer[_type.UINT16]],  # EmHeight
                               _enum.GpStatus]
    GdipGetCellAscent: _Callable[[_type.GpFontFamily,  # family
                                  _type.INT,  # style
                                  _Pointer[_type.UINT16]],  # CellAscent
                                 _enum.GpStatus]
    GdipGetCellDescent: _Callable[[_type.GpFontFamily,  # family
                                   _type.INT,  # style
                                   _Pointer[_type.UINT16]],  # CellDescent
                                  _enum.GpStatus]
    GdipGetLineSpacing: _Callable[[_type.GpFontFamily,  # family
                                   _type.INT,  # style
                                   _Pointer[_type.UINT16]],  # LineSpacing
                                  _enum.GpStatus]
    GdipCreateFontFromDC: _Callable[[_type.HDC,  # hdc
                                     _Pointer[_type.GpFont]],  # font
                                    _enum.GpStatus]
    GdipCreateFontFromLogfontA: _Callable[[_type.HDC,  # hdc
                                           _Pointer[_struct.LOGFONTA],  # logfont
                                           _Pointer[_type.GpFont]],  # font
                                          _enum.GpStatus]
    GdipCreateFontFromLogfontW: _Callable[[_type.HDC,  # hdc
                                           _Pointer[_struct.LOGFONTW],  # logfont
                                           _Pointer[_type.GpFont]],  # font
                                          _enum.GpStatus]
    GdipCreateFont: _Callable[[_type.GpFontFamily,  # fontFamily
                               _type.REAL,  # emSize
                               _type.INT,  # style
                               _enum.Unit,  # unit
                               _Pointer[_type.GpFont]],  # font
                              _enum.GpStatus]
    GdipCloneFont: _Callable[[_type.GpFont,  # font
                              _Pointer[_type.GpFont]],  # cloneFont
                             _enum.GpStatus]
    GdipDeleteFont: _Callable[[_type.GpFont],  # font
                              _enum.GpStatus]
    GdipGetFamily: _Callable[[_type.GpFont,  # font
                              _Pointer[_type.GpFontFamily]],  # family
                             _enum.GpStatus]
    GdipGetFontStyle: _Callable[[_type.GpFont,  # font
                                 _Pointer[_type.INT]],  # style
                                _enum.GpStatus]
    GdipGetFontSize: _Callable[[_type.GpFont,  # font
                                _Pointer[_type.REAL]],  # size
                               _enum.GpStatus]
    GdipGetFontUnit: _Callable[[_type.GpFont,  # font
                                _Pointer[_enum.Unit]],  # unit
                               _enum.GpStatus]
    GdipGetFontHeight: _Callable[[_type.GpFont,  # font
                                  _type.GpGraphics,  # graphics
                                  _Pointer[_type.REAL]],  # height
                                 _enum.GpStatus]
    GdipGetFontHeightGivenDPI: _Callable[[_type.GpFont,  # font
                                          _type.REAL,  # dpi
                                          _Pointer[_type.REAL]],  # height
                                         _enum.GpStatus]
    GdipGetLogFontA: _Callable[[_type.GpFont,  # font
                                _type.GpGraphics,  # graphics
                                _Pointer[_struct.LOGFONTA]],  # logfontA
                               _enum.GpStatus]
    GdipGetLogFontW: _Callable[[_type.GpFont,  # font
                                _type.GpGraphics,  # graphics
                                _Pointer[_struct.LOGFONTW]],  # logfontW
                               _enum.GpStatus]
    GdipNewInstalledFontCollection: _Callable[[_Pointer[_type.GpFontCollection]],  # fontCollection
                                              _enum.GpStatus]
    GdipNewPrivateFontCollection: _Callable[[_Pointer[_type.GpFontCollection]],  # fontCollection
                                            _enum.GpStatus]
    GdipDeletePrivateFontCollection: _Callable[[_Pointer[_type.GpFontCollection]],  # fontCollection
                                               _enum.GpStatus]
    GdipGetFontCollectionFamilyCount: _Callable[[_type.GpFontCollection,  # fontCollection
                                                 _Pointer[_type.INT]],  # numFound
                                                _enum.GpStatus]
    GdipGetFontCollectionFamilyList: _Callable[[_type.GpFontCollection,  # fontCollection
                                                _type.INT,  # numSought
                                                _type.GpFontFamily,  # gpfamilies
                                                _Pointer[_type.INT]],  # numFound
                                               _enum.GpStatus]
    GdipPrivateAddFontFile: _Callable[[_type.GpFontCollection,  # fontCollection
                                       _type.LPWSTR],  # filename
                                      _enum.GpStatus]
    GdipPrivateAddMemoryFont: _Callable[[_type.GpFontCollection,  # fontCollection
                                         _type.c_void_p,  # memory
                                         _type.INT],  # length
                                        _enum.GpStatus]
    GdipDrawString: _Callable[[_type.GpGraphics,  # graphics
                               _type.LPWSTR,  # string
                               _type.INT,  # length
                               _type.GpFont,  # font
                               _Pointer[_struct.RectF],  # layoutRect
                               _Optional[_type.GpStringFormat],  # stringFormat
                               _type.GpBrush],  # brush
                              _enum.GpStatus]
    GdipMeasureString: _Callable[[_type.GpGraphics,  # graphics
                                  _type.LPWSTR,  # string
                                  _type.INT,  # length
                                  _type.GpFont,  # font
                                  _Pointer[_struct.RectF],  # layoutRect
                                  _Optional[_type.GpStringFormat],  # stringFormat
                                  _Pointer[_struct.RectF],  # boundingBox
                                  _Optional[_Pointer[_type.INT]],  # codepointsFitted
                                  _Optional[_Pointer[_type.INT]]],  # linesFilled
                                 _enum.GpStatus]
    GdipMeasureCharacterRanges: _Callable[[_type.GpGraphics,  # graphics
                                           _type.LPWSTR,  # string
                                           _type.INT,  # length
                                           _type.GpFont,  # font
                                           _Pointer[_struct.RectF],  # layoutRect
                                           _type.GpStringFormat,  # stringFormat
                                           _type.INT,  # regionCount
                                           _Pointer[_type.GpRegion]],  # regions
                                          _enum.GpStatus]
    GdipDrawDriverString: _Callable[[_type.GpGraphics,  # graphics
                                     _Pointer[_type.UINT16],  # text
                                     _type.INT,  # length
                                     _type.GpFont,  # font
                                     _type.GpBrush,  # brush
                                     _Pointer[_struct.PointF],  # positions
                                     _type.INT,  # flags
                                     _type.GpMatrix],  # matrix
                                    _enum.GpStatus]
    GdipMeasureDriverString: _Callable[[_type.GpGraphics,  # graphics
                                        _Pointer[_type.UINT16],  # text
                                        _type.INT,  # length
                                        _type.GpFont,  # font
                                        _Pointer[_struct.PointF],  # positions
                                        _type.INT,  # flags
                                        _type.GpMatrix,  # matrix
                                        _Pointer[_struct.RectF]],  # boundingBox
                                       _enum.GpStatus]
    GdipCreateStringFormat: _Callable[[_type.INT,  # formatAttributes
                                       _type.LANGID,  # language
                                       _Pointer[_type.GpStringFormat]],  # format
                                      _enum.GpStatus]
    GdipStringFormatGetGenericDefault: _Callable[[_Pointer[_type.GpStringFormat]],  # format
                                                 _enum.GpStatus]
    GdipStringFormatGetGenericTypographic: _Callable[[_Pointer[_type.GpStringFormat]],  # format
                                                     _enum.GpStatus]
    GdipDeleteStringFormat: _Callable[[_type.GpStringFormat],  # format
                                      _enum.GpStatus]
    GdipCloneStringFormat: _Callable[[_type.GpStringFormat,  # format
                                      _Pointer[_type.GpStringFormat]],  # newFormat
                                     _enum.GpStatus]
    GdipSetStringFormatFlags: _Callable[[_type.GpStringFormat,  # format
                                         _type.INT],  # flags
                                        _enum.GpStatus]
    GdipGetStringFormatFlags: _Callable[[_type.GpStringFormat,  # format
                                         _Pointer[_type.INT]],  # flags
                                        _enum.GpStatus]
    GdipSetStringFormatAlign: _Callable[[_type.GpStringFormat,  # format
                                         _enum.StringAlignment],  # align
                                        _enum.GpStatus]
    GdipGetStringFormatAlign: _Callable[[_type.GpStringFormat,  # format
                                         _Pointer[_enum.StringAlignment]],  # align
                                        _enum.GpStatus]
    GdipSetStringFormatLineAlign: _Callable[[_type.GpStringFormat,  # format
                                             _enum.StringAlignment],  # align
                                            _enum.GpStatus]
    GdipGetStringFormatLineAlign: _Callable[[_type.GpStringFormat,  # format
                                             _Pointer[_enum.StringAlignment]],  # align
                                            _enum.GpStatus]
    GdipSetStringFormatTrimming: _Callable[[_type.GpStringFormat,  # format
                                            _enum.StringTrimming],  # trimming
                                           _enum.GpStatus]
    GdipGetStringFormatTrimming: _Callable[[_type.GpStringFormat,  # format
                                            _Pointer[_enum.StringTrimming]],  # trimming
                                           _enum.GpStatus]
    GdipSetStringFormatHotkeyPrefix: _Callable[[_type.GpStringFormat,  # format
                                                _type.INT],  # hotkeyPrefix
                                               _enum.GpStatus]
    GdipGetStringFormatHotkeyPrefix: _Callable[[_type.GpStringFormat,  # format
                                                _Pointer[_type.INT]],  # hotkeyPrefix
                                               _enum.GpStatus]
    GdipSetStringFormatTabStops: _Callable[[_type.GpStringFormat,  # format
                                            _type.REAL,  # firstTabOffset
                                            _type.INT,  # count
                                            _Pointer[_type.REAL]],  # tabStops
                                           _enum.GpStatus]
    GdipGetStringFormatTabStops: _Callable[[_type.GpStringFormat,  # format
                                            _type.INT,  # count
                                            _Pointer[_type.REAL],  # firstTabOffset
                                            _Pointer[_type.REAL]],  # tabStops
                                           _enum.GpStatus]
    GdipGetStringFormatTabStopCount: _Callable[[_type.GpStringFormat,  # format
                                                _Pointer[_type.INT]],  # count
                                               _enum.GpStatus]
    GdipSetStringFormatDigitSubstitution: _Callable[[_type.GpStringFormat,  # format
                                                     _type.LANGID,  # language
                                                     _enum.StringDigitSubstitute],  # substitute
                                                    _enum.GpStatus]
    GdipGetStringFormatDigitSubstitution: _Callable[[_type.GpStringFormat,  # format
                                                     _Pointer[_type.LANGID],  # language
                                                     _Pointer[_enum.StringDigitSubstitute]],  # substitute
                                                    _enum.GpStatus]
    GdipGetStringFormatMeasurableCharacterRangeCount: _Callable[[_type.GpStringFormat,  # format
                                                                 _Pointer[_type.INT]],  # count
                                                                _enum.GpStatus]
    GdipSetStringFormatMeasurableCharacterRanges: _Callable[[_type.GpStringFormat,  # format
                                                             _type.INT,  # rangeCount
                                                             _Pointer[_struct.CharacterRange]],  # ranges
                                                            _enum.GpStatus]
    GdipCreateCachedBitmap: _Callable[[_type.GpBitmap,  # bitmap
                                       _type.GpGraphics,  # graphics
                                       _Pointer[_type.GpCachedBitmap]],  # cachedBitmap
                                      _enum.GpStatus]
    GdipDeleteCachedBitmap: _Callable[[_type.GpCachedBitmap],  # cachedBitmap
                                      _enum.GpStatus]
    GdipDrawCachedBitmap: _Callable[[_type.GpGraphics,  # graphics
                                     _type.GpCachedBitmap,  # cachedBitmap
                                     _type.INT,  # x
                                     _type.INT],  # y
                                    _enum.GpStatus]
    GdipEmfToWmfBits: _Callable[[_type.HENHMETAFILE,  # hemf
                                 _type.UINT,  # cbData16
                                 _Optional[_Pointer[_type.BYTE]],  # pData16
                                 _type.INT,  # iMapMode
                                 _type.INT],  # eFlags
                                _type.UINT]
    GdipSetImageAttributesCachedBackground: _Callable[[_type.GpImageAttributes,  # imageattr
                                                       _type.BOOL],  # enableFlag
                                                      _enum.GpStatus]
    GdipTestControl: _Callable[[_enum.GpTestControlEnum,  # control
                                _type.c_void_p],  # param
                               _enum.GpStatus]
    GdiplusNotificationHook: _Callable[[_Pointer[_type.ULONG_PTR]],  # token
                                       _enum.GpStatus]
    GdiplusNotificationUnhook: _Callable[[_type.ULONG_PTR],  # token
                                         _type.VOID]
    GdipConvertToEmfPlus: _Callable[[_type.GpGraphics,  # refGraphics
                                     _type.GpMetafile,  # metafile
                                     _Pointer[_type.INT],  # conversionFailureFlag
                                     _enum.EmfType,  # emfType
                                     _type.LPWSTR,  # description
                                     _Pointer[_type.GpMetafile]],  # out_metafile
                                    _enum.GpStatus]
    GdipConvertToEmfPlusToFile: _Callable[[_type.GpGraphics,  # refGraphics
                                           _type.GpMetafile,  # metafile
                                           _Pointer[_type.INT],  # conversionFailureFlag
                                           _type.LPWSTR,  # filename
                                           _enum.EmfType,  # emfType
                                           _type.LPWSTR,  # description
                                           _Pointer[_type.GpMetafile]],  # out_metafile
                                          _enum.GpStatus]
    GdipConvertToEmfPlusToStream: _Callable[[_type.GpGraphics,  # refGraphics
                                             _type.GpMetafile,  # metafile
                                             _Pointer[_type.INT],  # conversionFailureFlag
                                             _interface.IStream,  # stream
                                             _enum.EmfType,  # emfType
                                             _type.LPWSTR,  # description
                                             _Pointer[_type.GpMetafile]],  # out_metafile
                                            _enum.GpStatus]
    # gdiplusinit
    GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],  # token
                               _Pointer[_struct.GdiplusStartupInput],  # input
                               _Optional[_Pointer[_struct.GdiplusStartupInput]]],  # output
                              _enum.Status]
    GdiplusShutdown: _Callable[[_type.ULONG_PTR],  # token
                               _type.VOID]


# noinspection PyPep8Naming
class kernel32(_Func, metaclass=_WinDLL):
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
    FlushFileBuffers: _Callable[[_type.HANDLE],  # hFile
                                _type.BOOL]
    WriteFile: _Callable[[_type.HANDLE,  # hFile
                          _type.LPCVOID,  # lpBuffer
                          _type.DWORD,  # nNumberOfBytesToWrite
                          _Optional[_Pointer[_type.DWORD]],  # lpNumberOfBytesWritten
                          _Optional[_Pointer[_struct.OVERLAPPED]]],  # lpOverlapped
                         _type.BOOL]
    # TODO
    AreShortNamesEnabled: _Callable[[_type.HANDLE,
                                     _Pointer[_type.BOOL]],
                                    _type.BOOL]
    CreateFileA: _Callable[[_type.LPCSTR,
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_type.HANDLE]],
                           _type.HANDLE]
    CreateFileW: _Callable[[_type.LPCWSTR,
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_Pointer[_struct.SECURITY_ATTRIBUTES]],
                            _type.DWORD,
                            _type.DWORD,
                            _Optional[_type.HANDLE]],
                           _type.HANDLE]
    DeleteFileA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    DeleteFileW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
    FindFirstVolumeW: _Callable[[_type.LPWSTR,
                                 _type.DWORD],
                                _type.HANDLE]
    FindNextVolumeW: _Callable[[_type.HANDLE,
                                _type.LPWSTR,
                                _type.DWORD],
                               _type.BOOL]
    FindVolumeClose: _Callable[[_type.HANDLE],
                               _type.BOOL]
    GetDiskFreeSpaceA: _Callable[[_type.LPCSTR,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]]],
                                 _type.BOOL]
    GetDiskFreeSpaceW: _Callable[[_type.LPCWSTR,
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]],
                                  _Optional[_Pointer[_type.DWORD]]],
                                 _type.BOOL]
    GetDiskFreeSpaceExA: _Callable[[_type.LPCSTR,
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                   _type.BOOL]
    GetDiskFreeSpaceExW: _Callable[[_type.LPCWSTR,
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                    _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                   _type.BOOL]
    GetDiskSpaceInformationA: _Callable[[_Optional[_type.LPCSTR],
                                         _Pointer[_struct.DISK_SPACE_INFORMATION]],
                                        _type.BOOL]
    GetDiskSpaceInformationW: _Callable[[_Optional[_type.LPCWSTR],
                                         _Pointer[_struct.DISK_SPACE_INFORMATION]],
                                        _type.BOOL]
    GetDriveTypeA: _Callable[[_type.LPCSTR],
                             _type.UINT]
    GetDriveTypeW: _Callable[[_type.LPCWSTR],
                             _type.UINT]
    GetFileAttributesA: _Callable[[_type.LPCSTR],
                                  _type.DWORD]
    GetFileAttributesW: _Callable[[_type.LPCWSTR],
                                  _type.DWORD]
    GetFileSize: _Callable[[_type.HANDLE,
                            _Optional[_Pointer[_type.DWORD]]],
                           _type.DWORD]
    GetFileSizeEx: _Callable[[_type.HANDLE,
                              _Pointer[_union.LARGE_INTEGER]],
                             _type.BOOL]
    GetFileTime: _Callable[[_type.HANDLE,
                            _Optional[_Pointer[_struct.FILETIME]],
                            _Optional[_Pointer[_struct.FILETIME]],
                            _Optional[_Pointer[_struct.FILETIME]]],
                           _type.BOOL]
    GetFileType: _Callable[[_type.HANDLE],
                           _type.DWORD]
    GetFinalPathNameByHandleA: _Callable[[_type.HANDLE,
                                          _type.LPSTR,
                                          _type.DWORD,
                                          _type.DWORD],
                                         _type.DWORD]
    GetFinalPathNameByHandleW: _Callable[[_type.HANDLE,
                                          _type.LPWSTR,
                                          _type.DWORD,
                                          _type.DWORD],
                                         _type.DWORD]
    GetLogicalDrives: _Callable[[],
                                _type.DWORD]
    GetLogicalDriveStringsA: _Callable[[_type.DWORD,
                                        _Optional[_type.LPSTR]],
                                       _type.DWORD]
    GetLogicalDriveStringsW: _Callable[[_type.DWORD,
                                        _Optional[_type.LPWSTR]],
                                       _type.DWORD]
    GetLongPathNameA: _Callable[[_type.LPCSTR,
                                 _Optional[_type.LPSTR],
                                 _type.DWORD],
                                _type.DWORD]
    GetLongPathNameW: _Callable[[_type.LPCWSTR,
                                 _Optional[_type.LPWSTR],
                                 _type.DWORD],
                                _type.DWORD]
    GetShortPathNameW: _Callable[[_type.LPCWSTR,
                                  _Optional[_type.LPWSTR],
                                  _type.DWORD],
                                 _type.DWORD]
    GetTempFileNameW: _Callable[[_type.LPCWSTR,
                                 _type.LPCWSTR,
                                 _type.UINT,
                                 _type.LPWSTR],
                                _type.UINT]
    GetTempPathA: _Callable[[_type.DWORD,
                             _type.LPSTR],
                            _type.DWORD]
    GetTempPathW: _Callable[[_type.DWORD,
                             _type.LPWSTR],
                            _type.DWORD]
    GetTempPath2A: _Callable[[_type.DWORD,
                              _type.LPSTR],
                             _type.DWORD]
    GetTempPath2W: _Callable[[_type.DWORD,
                              _type.LPWSTR],
                             _type.DWORD]
    GetVolumePathNameW: _Callable[[_type.LPCWSTR,
                                   _type.LPWSTR,
                                   _type.DWORD],
                                  _type.DWORD]
    LocalFileTimeToFileTime: _Callable[[_Pointer[_struct.FILETIME],
                                        _Pointer[_struct.FILETIME]],
                                       _type.BOOL]
    LockFile: _Callable[[_type.HANDLE,
                         _type.DWORD,
                         _type.DWORD,
                         _type.DWORD,
                         _type.DWORD],
                        _type.BOOL]
    QueryDosDeviceW: _Callable[[_Optional[_type.LPCWSTR],
                                _type.LPWSTR,
                                _type.DWORD],
                               _type.DWORD]
    ReadFile: _Callable[[_type.HANDLE,
                         _Optional[_type.LPVOID],
                         _type.DWORD,
                         _Optional[_Pointer[_type.DWORD]],
                         _Optional[_Pointer[_struct.OVERLAPPED]]],
                        _type.BOOL]
    RemoveDirectoryA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    RemoveDirectoryW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    SetEndOfFile: _Callable[[_type.HANDLE],
                            _type.BOOL]
    SetFileAttributesA: _Callable[[_type.LPCSTR,
                                   _type.DWORD],
                                  _type.BOOL]
    SetFileAttributesW: _Callable[[_type.LPCWSTR,
                                   _type.DWORD],
                                  _type.BOOL]
    SetFileValidData: _Callable[[_type.HANDLE,
                                 _type.LONGLONG],
                                _type.BOOL]
    UnlockFile: _Callable[[_type.HANDLE,
                           _type.DWORD,
                           _type.DWORD,
                           _type.DWORD,
                           _type.DWORD],
                          _type.BOOL]
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


# noinspection PyPep8Naming
class mscoree(_Func, metaclass=_WinDLL):
    # cor
    CoEEShutDownCOM: _Callable[[],
                               _type.c_void]
    CoInitializeCor: _Callable[[_type.DWORD],
                               _type.HRESULT]
    CoInitializeEE: _Callable[[_enum.COINITIEE],
                              _type.HRESULT]
    CoUninitializeCor: _Callable[[],
                                 _type.c_void]
    CoUninitializeEE: _Callable[[_type.BOOL],
                                _type.c_void]
    # mscoree
    CorBindToCurrentRuntime: _Callable[[_Optional[_type.LPCWSTR],
                                        _Pointer[_struct.CLSID],
                                        _Pointer[_struct.IID],
                                        _type.LPVOID],
                                       _type.HRESULT]
    CorBindToRuntimeEx: _Callable[[_Optional[_type.LPCWSTR],
                                   _Optional[_type.LPCWSTR],
                                   _enum.STARTUP_FLAGS,
                                   _Pointer[_struct.CLSID],
                                   _Pointer[_struct.IID],
                                   _type.LPVOID],
                                  _type.HRESULT]


# noinspection PyPep8Naming
class msimg32(_Func, metaclass=_WinDLL):
    # wingdi
    AlphaBlend: _Callable[[_type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.HDC,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _struct.BLENDFUNCTION],
                          _type.BOOL]


# noinspection PyPep8Naming
class ntdll(_Func, metaclass=_WinDLL):
    RtlAreLongPathsEnabled: _Callable[[],
                                      _type.c_ubyte]
    # winnt
    RtlGetProductInfo: _Callable[[_type.DWORD,  # OSMajorVersion
                                  _type.DWORD,  # OSMinorVersion
                                  _type.DWORD,  # SpMajorVersion
                                  _type.DWORD,  # SpMinorVersion
                                  _Pointer[_type.DWORD]],  # ReturnedProductType
                                 _type.BOOLEAN]
    # winternl
    RtlFreeAnsiString: _Callable[[_Pointer[_struct.ANSI_STRING]],  # AnsiString
                                 _type.VOID]
    RtlFreeUnicodeString: _Callable[[_Pointer[_struct.UNICODE_STRING]],  # UnicodeString
                                    _type.VOID]
    RtlFreeOemString: _Callable[[_Pointer[_struct.OEM_STRING]],  # OemString
                                _type.VOID]
    RtlInitString: _Callable[[_Pointer[_struct.STRING],  # DestinationString
                              _type.PCSZ],  # SourceString
                             _type.VOID]
    RtlInitStringEx: _Callable[[_Pointer[_struct.STRING],  # DestinationString
                                _type.PCSZ],  # SourceString
                               _type.NTSTATUS]
    RtlInitAnsiString: _Callable[[_Pointer[_struct.ANSI_STRING],  # DestinationString
                                  _type.PCSZ],  # SourceString
                                 _type.VOID]
    RtlInitAnsiStringEx: _Callable[[_Pointer[_struct.ANSI_STRING],  # DestinationString
                                    _type.PCSZ],  # SourceString
                                   _type.NTSTATUS]
    RtlInitUnicodeString: _Callable[[_Pointer[_struct.UNICODE_STRING],  # DestinationString
                                     _type.PCWSTR],  # SourceString
                                    _type.VOID]
    RtlAnsiStringToUnicodeString: _Callable[[_Pointer[_struct.UNICODE_STRING],  # DestinationString
                                             _Pointer[_struct.ANSI_STRING],  # SourceString
                                             _type.BOOLEAN],  # AllocateDestinationString
                                            _type.NTSTATUS]
    RtlUnicodeStringToAnsiString: _Callable[[_Pointer[_struct.ANSI_STRING],  # DestinationString
                                             _Pointer[_struct.UNICODE_STRING],  # SourceString
                                             _type.BOOLEAN],  # AllocateDestinationString
                                            _type.NTSTATUS]
    RtlUnicodeStringToOemString: _Callable[[_Pointer[_struct.OEM_STRING],  # DestinationString
                                            _Pointer[_struct.UNICODE_STRING],  # SourceString
                                            _type.BOOLEAN],  # AllocateDestinationString
                                           _type.NTSTATUS]


# noinspection PyPep8Naming
class ole32(_Func, metaclass=_WinDLL):
    # combaseapi
    CLSIDFromString: _Callable[[_type.LPCOLESTR,
                                _Pointer[_struct.CLSID]],
                               _type.HRESULT]
    CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],
                            _type.HRESULT]
    CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],
                                 _Optional[_Pointer[_interface.IUnknown]],
                                 _type.DWORD,
                                 _Pointer[_struct.IID],
                                 _type.LPVOID],
                                _type.HRESULT]
    CoInitializeEx: _Callable[[_Optional[_type.LPVOID],
                               _type.DWORD],
                              _type.HRESULT]
    CoTaskMemFree: _Callable[[_Optional[_type.LPVOID]],
                             _type.c_void]
    CoUninitialize: _Callable[[],
                              _type.VOID]
    IIDFromString: _Callable[[_type.LPCOLESTR,
                              _Pointer[_struct.IID]],
                             _type.HRESULT]
    StringFromCLSID: _Callable[[_Pointer[_struct.CLSID],
                                _Pointer[_type.LPOLESTR]],
                               _type.HRESULT]
    StringFromGUID2: _Callable[[_Pointer[_struct.GUID],
                                _type.LPOLESTR,
                                _type.c_int],
                               _type.c_int]
    StringFromIID: _Callable[[_Pointer[_struct.IID],
                              _Pointer[_type.LPOLESTR]],
                             _type.HRESULT]
    # guiddef
    IsEqualGUID: _Callable[[_Pointer[_struct.GUID],
                            _Pointer[_struct.GUID]],
                           _type.c_int]
    # objbase
    CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                            _type.HRESULT]
    # propidl
    FreePropVariantArray: _Callable[[_type.ULONG,
                                     _Pointer[_struct.PROPVARIANT]],
                                    _type.HRESULT]
    PropVariantClear: _Callable[[_Pointer[_struct.PROPVARIANT]],
                                _type.HRESULT]
    PropVariantCopy: _Callable[[_Pointer[_struct.PROPVARIANT],
                                _Pointer[_struct.PROPVARIANT]],
                               _type.HRESULT]


# noinspection PyPep8Naming
class oleacc(_Func, metaclass=_WinDLL):
    GetProcessHandleFromHwnd: _Callable[[_type.HWND],
                                        _type.HANDLE]
    # oleacc
    GetRoleTextA: _Callable[[_type.DWORD,
                             _Optional[_type.LPSTR],
                             _type.UINT],
                            _type.UINT]
    GetRoleTextW: _Callable[[_type.DWORD,
                             _Optional[_type.LPWSTR],
                             _type.UINT],
                            _type.UINT]
    GetStateTextA: _Callable[[_type.DWORD,
                              _Optional[_type.LPSTR],
                              _type.UINT],
                             _type.UINT]
    GetStateTextW: _Callable[[_type.DWORD,
                              _Optional[_type.LPWSTR],
                              _type.UINT],
                             _type.UINT]


# noinspection PyPep8Naming
class oleaut32(_Func, metaclass=_WinDLL):
    # oleauto
    VariantChangeType: _Callable[[_Pointer[_struct.VARIANTARG],
                                  _Pointer[_struct.VARIANTARG],
                                  _type.USHORT,
                                  _type.VARTYPE],
                                 _type.HRESULT]
    VariantChangeTypeEx: _Callable[[_Pointer[_struct.VARIANTARG],
                                    _Pointer[_struct.VARIANTARG],
                                    _type.LCID,
                                    _type.USHORT,
                                    _type.VARTYPE],
                                   _type.HRESULT]
    VariantClear: _Callable[[_Pointer[_struct.VARIANTARG]],
                            _type.HRESULT]
    VariantCopy: _Callable[[_Pointer[_struct.VARIANTARG],
                            _Pointer[_struct.VARIANTARG]],
                           _type.HRESULT]
    VariantCopyInd: _Callable[[_Pointer[_struct.VARIANTARG],
                               _Pointer[_struct.VARIANTARG]],
                              _type.HRESULT]
    VariantInit: _Callable[[_Pointer[_struct.VARIANTARG]],
                           _type.c_void]
    # olectl
    OleCreatePictureIndirect: _Callable[[_Pointer[_struct.PICTDESC],
                                         _Pointer[_struct.IID],
                                         _type.BOOL,
                                         _type.LPVOID],
                                        _type.WINOLECTLAPI]
    OleSavePictureFile: _Callable[[_interface.IPictureDisp,
                                   _type.BSTR],
                                  _type.WINOLECTLAPI]


# noinspection PyPep8Naming
class psapi(_Func, metaclass=_WinDLL):
    # Psapi
    GetDeviceDriverBaseNameA: _Callable[[_type.LPVOID,  # ImageBase
                                         _type.LPSTR,  # lpFilename
                                         _type.DWORD],  # nSize
                                        _type.DWORD]
    GetDeviceDriverBaseNameW: _Callable[[_type.LPVOID,  # ImageBase
                                         _type.LPWSTR,  # lpFilename
                                         _type.DWORD],  # nSize
                                        _type.DWORD]
    GetDeviceDriverFileNameA: _Callable[[_type.LPVOID,  # ImageBase
                                         _type.LPSTR,  # lpFilename
                                         _type.DWORD],  # nSize
                                        _type.DWORD]
    GetDeviceDriverFileNameW: _Callable[[_type.LPVOID,  # ImageBase
                                         _type.LPWSTR,  # lpFilename
                                         _type.DWORD],  # nSize
                                        _type.DWORD]
    QueryWorkingSet: _Callable[[_type.HANDLE,  # hProcess
                                _type.PVOID,  # pv
                                _type.DWORD],  # cb
                               _type.BOOL]
    QueryWorkingSetEx: _Callable[[_type.HANDLE,  # hProcess
                                  _type.PVOID,  # pv
                                  _type.DWORD],  # cb
                                 _type.BOOL]
    GetProcessImageFileNameA: _Callable[[_type.HANDLE,  # hProcess
                                         _type.LPSTR,  # lpImageFileName
                                         _type.DWORD],  # nSize
                                        _type.DWORD]
    GetProcessImageFileNameW: _Callable[[_type.HANDLE,  # hProcess
                                         _type.LPWSTR,  # lpImageFileName
                                         _type.DWORD],  # nSize
                                        _type.DWORD]


# noinspection PyPep8Naming
class setupapi(_Func, metaclass=_WinDLL):
    # SetupAPI
    SetupDiCreateDeviceInterfaceA: _Callable[[_type.HDEVINFO,
                                              _Pointer[_struct.SP_DEVINFO_DATA],
                                              _Pointer[_struct.GUID],
                                              _Optional[_type.PCSTR],
                                              _type.DWORD,
                                              _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DATA]]],
                                             _type.BOOL]
    SetupDiCreateDeviceInterfaceW: _Callable[[_type.HDEVINFO,
                                              _Pointer[_struct.SP_DEVINFO_DATA],
                                              _Pointer[_struct.GUID],
                                              _Optional[_type.PCWSTR],
                                              _type.DWORD,
                                              _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DATA]]],
                                             _type.BOOL]
    SetupDiDestroyDeviceInfoList: _Callable[[_type.HDEVINFO],
                                            _type.BOOL]
    SetupDiEnumDeviceInfo: _Callable[[_type.HDEVINFO,
                                      _type.DWORD,
                                      _Pointer[_struct.SP_DEVINFO_DATA]],
                                     _type.BOOL]
    SetupDiEnumDeviceInterfaces: _Callable[[_type.HDEVINFO,
                                            _Pointer[_struct.SP_DEVINFO_DATA],
                                            _Optional[_Pointer[_struct.GUID]],
                                            _type.DWORD,
                                            _Pointer[_struct.SP_DEVICE_INTERFACE_DATA]],
                                           _type.BOOL]
    SetupDiGetClassDevsA: _Callable[[_Optional[_Pointer[_struct.GUID]],
                                     _Optional[_type.PCSTR],
                                     _Optional[_type.HWND],
                                     _type.DWORD],
                                    _type.HDEVINFO]
    SetupDiGetClassDevsW: _Callable[[_Optional[_Pointer[_struct.GUID]],
                                     _Optional[_type.PCWSTR],
                                     _Optional[_type.HWND],
                                     _type.DWORD],
                                    _type.HDEVINFO]
    SetupDiGetDeviceInterfaceDetailA: _Callable[[_type.HDEVINFO,
                                                 _Pointer[_struct.SP_DEVICE_INTERFACE_DATA],
                                                 _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DETAIL_DATA_A]],
                                                 _type.DWORD,
                                                 _Optional[_Pointer[_type.DWORD]],
                                                 _Optional[_Pointer[_struct.SP_DEVINFO_DATA]]],
                                                _type.BOOL]
    SetupDiGetDeviceInterfaceDetailW: _Callable[[_type.HDEVINFO,
                                                 _Pointer[_struct.SP_DEVICE_INTERFACE_DATA],
                                                 _Optional[_Pointer[_struct.SP_DEVICE_INTERFACE_DETAIL_DATA_W]],
                                                 _type.DWORD,
                                                 _Optional[_Pointer[_type.DWORD]],
                                                 _Optional[_Pointer[_struct.SP_DEVINFO_DATA]]],
                                                _type.BOOL]
    SetupDiGetDevicePropertyW: _Callable[[_type.HDEVINFO,
                                          _Pointer[_struct.SP_DEVINFO_DATA],
                                          _Pointer[_struct.DEVPROPKEY],
                                          _Pointer[_type.DEVPROPTYPE],
                                          _Optional[_type.PBYTE],
                                          _type.DWORD,
                                          _Optional[_Pointer[_type.DWORD]],
                                          _type.DWORD],
                                         _type.BOOL]
    SetupDiGetDeviceRegistryPropertyA: _Callable[[_type.HDEVINFO,
                                                  _Pointer[_struct.SP_DEVINFO_DATA],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]],
                                                  _Optional[_type.PBYTE],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]]],
                                                 _type.BOOL]
    SetupDiGetDeviceRegistryPropertyW: _Callable[[_type.HDEVINFO,
                                                  _Pointer[_struct.SP_DEVINFO_DATA],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]],
                                                  _Optional[_type.PBYTE],
                                                  _type.DWORD,
                                                  _Optional[_Pointer[_type.DWORD]]],
                                                 _type.BOOL]


class SHCore(_Func, metaclass=_WinDLL):
    # ShellScalingApi
    GetDpiForMonitor: _Callable[[_type.HMONITOR,
                                 _enum.MONITOR_DPI_TYPE,
                                 _Pointer[_type.UINT],
                                 _Pointer[_type.UINT]],
                                _type.HRESULT]
    GetProcessDpiAwareness: _Callable[[_type.HANDLE,
                                       _Pointer[_enum.PROCESS_DPI_AWARENESS]],
                                      _type.HRESULT]
    SetProcessDpiAwareness: _Callable[[_enum.PROCESS_DPI_AWARENESS],
                                      _type.HRESULT]


# noinspection PyPep8Naming
class shdocvw(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]


# noinspection PyPep8Naming
class shell32(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 703
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 704
    # shellapi
    InitNetworkAddressControl: _Callable[[],
                                         _type.BOOL]
    ShellExecuteA: _Callable[[_Optional[_type.HWND],
                              _Optional[_type.LPCSTR],
                              _type.LPCSTR,
                              _Optional[_type.LPCSTR],
                              _Optional[_type.LPCSTR],
                              _type.INT],
                             _type.HINSTANCE]
    ShellExecuteW: _Callable[[_Optional[_type.HWND],
                              _Optional[_type.LPCWSTR],
                              _type.LPCWSTR,
                              _Optional[_type.LPCWSTR],
                              _Optional[_type.LPWSTR],
                              _type.INT],
                             _type.HINSTANCE]
    ShellExecuteExA: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOA]],
                               _type.BOOL]
    ShellExecuteExW: _Callable[[_Pointer[_struct.SHELLEXECUTEINFOW]],
                               _type.BOOL]
    Shell_NotifyIconA: _Callable[[_type.DWORD,
                                  _Pointer[_struct.NOTIFYICONDATAA]],
                                 _type.BOOL]
    Shell_NotifyIconW: _Callable[[_type.DWORD,
                                  _Pointer[_struct.NOTIFYICONDATAW]],
                                 _type.BOOL]
    Shell_NotifyIconGetRect: _Callable[[_Pointer[_struct.NOTIFYICONIDENTIFIER],
                                        _Pointer[_struct.RECT]],
                                       _type.BOOL]
    SHEmptyRecycleBinA: _Callable[[_Optional[_type.HWND],
                                   _Optional[_type.LPCSTR],
                                   _type.DWORD],
                                  _type.BOOL]
    SHEmptyRecycleBinW: _Callable[[_Optional[_type.HWND],
                                   _Optional[_type.LPCWSTR],
                                   _type.DWORD],
                                  _type.BOOL]
    SHGetDiskFreeSpaceExA: _Callable[[_type.LPCSTR,
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                     _type.BOOL]
    SHGetDiskFreeSpaceExW: _Callable[[_type.LPCWSTR,
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]],
                                      _Optional[_Pointer[_union.ULARGE_INTEGER]]],
                                     _type.BOOL]
    SHGetDriveMedia: _Callable[[_type.PCWSTR,
                                _Pointer[_type.DWORD]],
                               _type.UINT]
    SHGetStockIconInfo: _Callable[[_enum.SHSTOCKICONID,
                                   _type.UINT,
                                   _Pointer[_struct.SHSTOCKICONINFO]],
                                  _type.HRESULT]
    SHQueryUserNotificationState: _Callable[[_Pointer[_enum.QUERY_USER_NOTIFICATION_STATE]],
                                            _type.HRESULT]
    SHQueryRecycleBinA: _Callable[[_Optional[_type.LPCSTR],
                                   _Pointer[_struct.SHQUERYRBINFO]],
                                  _type.HRESULT]
    SHQueryRecycleBinW: _Callable[[_Optional[_type.LPCWSTR],
                                   _Pointer[_struct.SHQUERYRBINFO]],
                                  _type.HRESULT]
    # ShlObj_core
    GetCurrentProcessExplicitAppUserModelID: _Callable[[_Pointer[_type.PWSTR]],
                                                       _type.HRESULT]
    ILClone: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                       _Pointer[_struct.ITEMIDLIST]]
    ILCloneFirst: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                            _Pointer[_struct.ITEMIDLIST]]
    ILCombine: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]],
                          _Optional[_Pointer[_struct.ITEMIDLIST]]],
                         _Pointer[_struct.ITEMIDLIST]]
    ILCreateFromPath: _Callable[[_type.PCWSTR],
                                _Pointer[_struct.ITEMIDLIST]]
    ILCreateFromPathA: _Callable[[_type.PCSTR],
                                 _Pointer[_struct.ITEMIDLIST]]
    ILCreateFromPathW: _Callable[[_type.PCWSTR],
                                 _Pointer[_struct.ITEMIDLIST]]
    ILFindChild: _Callable[[_Pointer[_struct.ITEMIDLIST],
                            _Pointer[_struct.ITEMIDLIST]],
                           _Pointer[_struct.ITEMIDLIST]]
    ILFindLastID: _Callable[[_Pointer[_struct.ITEMIDLIST]],
                            _Pointer[_struct.ITEMIDLIST]]
    ILFree: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                      _type.c_void]
    ILGetNext: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                         _Pointer[_struct.ITEMIDLIST]]
    ILGetSize: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                         _type.UINT]
    ILIsEqual: _Callable[[_Pointer[_struct.ITEMIDLIST],
                          _Pointer[_struct.ITEMIDLIST]],
                         _type.BOOL]
    ILIsParent: _Callable[[_Pointer[_struct.ITEMIDLIST],
                           _Pointer[_struct.ITEMIDLIST],
                           _type.BOOL],
                          _type.BOOL]
    ILRemoveLastID: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]]],
                              _type.BOOL]
    PathCleanupSpec: _Callable[[_Optional[_type.PCWSTR],
                                _type.PWSTR],
                               _type.c_int]
    SetCurrentProcessExplicitAppUserModelID: _Callable[[_type.PCWSTR],
                                                       _type.HRESULT]
    SHBrowseForFolderA: _Callable[[_Pointer[_struct.BROWSEINFOA]],
                                  _Pointer[_Pointer[_struct.ITEMIDLIST]]]
    SHBrowseForFolderW: _Callable[[_Pointer[_struct.BROWSEINFOW]],
                                  _Pointer[_Pointer[_struct.ITEMIDLIST]]]
    SHChangeNotify: _Callable[[_type.LONG,
                               _type.UINT,
                               _Optional[_type.LPCVOID],
                               _Optional[_type.LPCVOID]],
                              _type.c_void]
    SHGetFolderPathA: _Callable[[_Optional[_type.HWND],
                                 _type.c_int,
                                 _Optional[_type.HANDLE],
                                 _type.DWORD,
                                 _type.LPSTR],
                                _type.HRESULT]
    SHGetFolderPathW: _Callable[[_Optional[_type.HWND],
                                 _type.c_int,
                                 _Optional[_type.HANDLE],
                                 _type.DWORD,
                                 _type.LPWSTR],
                                _type.HRESULT]
    SHOpenFolderAndSelectItems: _Callable[[_Pointer[_struct.ITEMIDLIST],
                                           _type.UINT,
                                           _Optional[_Pointer[_Pointer[_struct.ITEMIDLIST]]],
                                           _type.DWORD],
                                          _type.SHSTDAPI]
    SHOpenWithDialog: _Callable[[_Optional[_type.HWND],
                                 _Pointer[_struct.OPENASINFO]],
                                _type.SHSTDAPI]
    # ShObjIdl_core
    SHCreateItemFromParsingName: _Callable[[_type.PCWSTR,
                                            _Optional[_Pointer[_interface.IBindCtx]],
                                            _Pointer[_struct.IID],
                                            _Pointer[_interface.IShellItem]],
                                           _type.SHSTDAPI]
    SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                                  _Pointer[_Pointer[_struct.ITEMIDLIST]],
                                                  _Pointer[_interface.IShellItemArray]],
                                                 _type.SHSTDAPI]
    SHGetKnownFolderPath: _Callable[[_Pointer[_struct.KNOWNFOLDERID],
                                     _enum.KNOWN_FOLDER_FLAG,
                                     _Optional[_type.HANDLE],
                                     _Pointer[_type.PWSTR]],
                                    _type.HRESULT]
    SHGetPropertyStoreFromParsingName: _Callable[[_type.PCWSTR,
                                                  _Optional[_Pointer[_interface.IBindCtx]],
                                                  _enum.GETPROPERTYSTOREFLAGS,
                                                  _Pointer[_struct.IID],
                                                  _Pointer[_interface.IPropertyStore]],
                                                 _type.SHSTDAPI]


# noinspection PyPep8Naming
class shlwapi(_Func, metaclass=_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 269
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 270
    # Shlwapi
    IsInternetESCEnabled: _Callable[[],
                                    _type.BOOL]
    IStream_Copy: _Callable[[_interface.IStream,
                             _interface.IStream,
                             _type.DWORD],
                            _type.HRESULT]
    IStream_Read: _Callable[[_interface.IStream,
                             _type.c_void_p,
                             _type.ULONG],
                            _type.HRESULT]
    IStream_ReadStr: _Callable[[_interface.IStream,
                                _Pointer[_type.PCWSTR]],
                               _type.HRESULT]
    IStream_Reset: _Callable[[_interface.IStream],  # pstm
                             _type.HRESULT]
    IStream_Size: _Callable[[_interface.IStream,  # pstm
                             _Pointer[_union.ULARGE_INTEGER]],  # pui
                            _type.HRESULT]
    IStream_Write: _Callable[[_interface.IStream,
                              _type.c_void_p,
                              _type.ULONG],
                             _type.HRESULT]
    IStream_WriteStr: _Callable[[_interface.IStream,
                                 _Pointer[_type.PCWSTR]],
                                _type.HRESULT]
    IUnknown_AtomicRelease: _Callable[[_type.c_void_p],
                                      _type.HRESULT]
    IUnknown_GetSite: _Callable[[_interface.IUnknown,
                                 _Pointer[_struct.IID],
                                 _type.c_void_p],
                                _type.HRESULT]
    IUnknown_GetWindow: _Callable[[_interface.IUnknown,
                                   _Pointer[_type.HWND]],
                                  _type.HRESULT]
    IUnknown_QueryService: _Callable[[_interface.IUnknown,
                                      _Pointer[_struct.GUID],
                                      _Pointer[_struct.IID],
                                      _type.c_void_p],
                                     _type.HRESULT]
    IUnknown_Set: _Callable[[_Pointer[_interface.IUnknown],
                             _Optional[_interface.IUnknown]],
                            _type.HRESULT]
    IUnknown_SetSite: _Callable[[_interface.IUnknown,
                                 _Optional[_interface.IUnknown]],
                                _type.HRESULT]
    PathAddBackslashA: _Callable[[_type.LPSTR],
                                 _type.LPSTR]
    PathAddBackslashW: _Callable[[_type.LPWSTR],
                                 _type.LPWSTR]
    PathAddExtensionA: _Callable[[_type.LPSTR,
                                  _Optional[_type.LPCSTR]],
                                 _type.BOOL]
    PathAddExtensionW: _Callable[[_type.LPWSTR,
                                  _Optional[_type.LPCWSTR]],
                                 _type.BOOL]
    PathAppendA: _Callable[[_type.LPSTR,
                            _type.LPCSTR],
                           _type.BOOL]
    PathAppendW: _Callable[[_type.LPWSTR,
                            _type.LPCWSTR],
                           _type.BOOL]
    PathBuildRootA: _Callable[[_type.LPSTR,
                               _type.c_int],
                              _type.LPSTR]
    PathBuildRootW: _Callable[[_type.LPWSTR,
                               _type.c_int],
                              _type.LPWSTR]
    PathCanonicalizeA: _Callable[[_type.LPSTR,
                                  _type.LPCSTR],
                                 _type.BOOL]
    PathCanonicalizeW: _Callable[[_type.LPWSTR,
                                  _type.LPCWSTR],
                                 _type.BOOL]
    PathCombineA: _Callable[[_type.LPSTR,
                             _Optional[_type.LPCSTR],
                             _Optional[_type.LPCSTR]],
                            _type.BOOL]
    PathCombineW: _Callable[[_type.LPWSTR,
                             _Optional[_type.LPCWSTR],
                             _Optional[_type.LPCWSTR]],
                            _type.BOOL]
    PathCompactPathA: _Callable[[_Optional[_type.HDC],
                                 _type.LPSTR,
                                 _type.UINT],
                                _type.BOOL]
    PathCompactPathW: _Callable[[_Optional[_type.HDC],
                                 _type.LPWSTR,
                                 _type.UINT],
                                _type.BOOL]
    PathCompactPathExA: _Callable[[_type.LPSTR,
                                   _type.LPCSTR,
                                   _type.UINT,
                                   _type.DWORD],
                                  _type.BOOL]
    PathCompactPathExW: _Callable[[_type.LPWSTR,
                                   _type.LPCWSTR,
                                   _type.UINT,
                                   _type.DWORD],
                                  _type.BOOL]
    PathCommonPrefixA: _Callable[[_type.LPCSTR,
                                  _type.LPCSTR,
                                  _type.LPSTR],
                                 _type.c_int]
    PathCommonPrefixW: _Callable[[_type.LPCWSTR,
                                  _type.LPCWSTR,
                                  _type.LPWSTR],
                                 _type.c_int]
    PathFileExistsA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathFileExistsW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathFindExtensionA: _Callable[[_type.LPCSTR],
                                  _type.LPSTR]
    PathFindExtensionW: _Callable[[_type.LPCWSTR],
                                  _type.LPWSTR]
    PathFindFileNameA: _Callable[[_type.LPCSTR],
                                 _type.LPSTR]
    PathFindFileNameW: _Callable[[_type.LPCWSTR],
                                 _type.LPWSTR]
    PathFindNextComponentA: _Callable[[_type.LPCSTR],
                                      _type.LPSTR]
    PathFindNextComponentW: _Callable[[_type.LPCWSTR],
                                      _type.LPWSTR]
    PathFindOnPathA: _Callable[[_type.LPSTR,
                                _Optional[_Pointer[_type.PCSTR]]],
                               _type.BOOL]
    PathFindOnPathW: _Callable[[_type.LPWSTR,
                                _Optional[_Pointer[_type.PCWSTR]]],
                               _type.BOOL]
    PathGetArgsA: _Callable[[_type.LPCSTR],
                            _type.LPSTR]
    PathGetArgsW: _Callable[[_type.LPCWSTR],
                            _type.LPWSTR]
    PathGetCharTypeA: _Callable[[_type.UCHAR],
                                _type.UINT]
    PathGetCharTypeW: _Callable[[_type.WCHAR],
                                _type.UINT]
    PathGetDriveNumberA: _Callable[[_type.LPCSTR],
                                   _type.c_int]
    PathGetDriveNumberW: _Callable[[_type.LPCWSTR],
                                   _type.c_int]
    PathIsContentTypeA: _Callable[[_type.LPCSTR,
                                   _type.LPCSTR],
                                  _type.BOOL]
    PathIsContentTypeW: _Callable[[_type.LPCWSTR,
                                   _type.LPCWSTR],
                                  _type.BOOL]
    PathIsDirectoryA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    PathIsDirectoryW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    PathIsDirectoryEmptyA: _Callable[[_type.LPCSTR],
                                     _type.BOOL]
    PathIsDirectoryEmptyW: _Callable[[_type.LPCWSTR],
                                     _type.BOOL]
    PathIsFileSpecA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathIsFileSpecW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathIsLFNFileSpecA: _Callable[[_type.LPCSTR],
                                  _type.BOOL]
    PathIsLFNFileSpecW: _Callable[[_type.LPCWSTR],
                                  _type.BOOL]
    PathIsNetworkPathA: _Callable[[_type.LPCSTR],
                                  _type.BOOL]
    PathIsNetworkPathW: _Callable[[_type.LPCWSTR],
                                  _type.BOOL]
    PathIsPrefixA: _Callable[[_type.LPCSTR,
                              _type.LPCSTR],
                             _type.BOOL]
    PathIsPrefixW: _Callable[[_type.LPCWSTR,
                              _type.LPCWSTR],
                             _type.BOOL]
    PathIsRelativeA: _Callable[[_type.LPCSTR],
                               _type.BOOL]
    PathIsRelativeW: _Callable[[_type.LPCWSTR],
                               _type.BOOL]
    PathIsRootA: _Callable[[_type.LPCSTR],
                           _type.BOOL]
    PathIsRootW: _Callable[[_type.LPCWSTR],
                           _type.BOOL]
    PathIsSameRootA: _Callable[[_type.LPCSTR,
                                _type.LPCSTR],
                               _type.BOOL]
    PathIsSameRootW: _Callable[[_type.LPCWSTR,
                                _type.LPCWSTR],
                               _type.BOOL]
    PathIsSystemFolderA: _Callable[[_type.LPCSTR,
                                    _type.DWORD],
                                   _type.BOOL]
    PathIsSystemFolderW: _Callable[[_type.LPCWSTR,
                                    _type.DWORD],
                                   _type.BOOL]
    PathIsUNCA: _Callable[[_type.LPCSTR],
                          _type.BOOL]
    PathIsUNCW: _Callable[[_type.LPCWSTR],
                          _type.BOOL]
    PathIsUNCServerA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    PathIsUNCServerW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    PathIsUNCServerShareA: _Callable[[_type.LPCSTR],
                                     _type.BOOL]
    PathIsUNCServerShareW: _Callable[[_type.LPCWSTR],
                                     _type.BOOL]
    PathIsURLA: _Callable[[_type.LPCSTR],
                          _type.BOOL]
    PathIsURLW: _Callable[[_type.LPCWSTR],
                          _type.BOOL]
    PathMakeSystemFolderA: _Callable[[_type.LPCSTR],
                                     _type.BOOL]
    PathMakeSystemFolderW: _Callable[[_type.LPCWSTR],
                                     _type.BOOL]
    PathRemoveFileSpecA: _Callable[[_type.LPSTR],
                                   _type.BOOL]
    PathRemoveFileSpecW: _Callable[[_type.LPWSTR],
                                   _type.BOOL]
    PathRenameExtensionA: _Callable[[_type.LPSTR,
                                     _type.LPCSTR],
                                    _type.BOOL]
    PathRenameExtensionW: _Callable[[_type.LPWSTR,
                                     _type.LPCWSTR],
                                    _type.BOOL]
    PathSearchAndQualifyA: _Callable[[_type.LPCSTR,
                                      _type.LPSTR,
                                      _type.UINT],
                                     _type.BOOL]
    PathSearchAndQualifyW: _Callable[[_type.LPCWSTR,
                                      _type.LPWSTR,
                                      _type.UINT],
                                     _type.BOOL]
    PathSkipRootA: _Callable[[_type.LPCSTR],
                             _type.LPSTR]
    PathSkipRootW: _Callable[[_type.LPCWSTR],
                             _type.LPWSTR]
    PathStripPathA: _Callable[[_type.LPSTR],
                              _type.c_void]
    PathStripPathW: _Callable[[_type.LPWSTR],
                              _type.c_void]
    PathStripToRootA: _Callable[[_type.LPCSTR],
                                _type.BOOL]
    PathStripToRootW: _Callable[[_type.LPCWSTR],
                                _type.BOOL]
    PathUndecorateA: _Callable[[_type.LPSTR],
                               _type.c_void]
    PathUndecorateW: _Callable[[_type.LPWSTR],
                               _type.c_void]
    PathUnExpandEnvStringsA: _Callable[[_type.LPCSTR,
                                        _type.LPSTR,
                                        _type.UINT],
                                       _type.BOOL]
    PathUnExpandEnvStringsW: _Callable[[_type.LPCWSTR,
                                        _type.LPWSTR,
                                        _type.UINT],
                                       _type.BOOL]
    PathUnmakeSystemFolderA: _Callable[[_type.LPCSTR],
                                       _type.BOOL]
    PathUnmakeSystemFolderW: _Callable[[_type.LPCWSTR],
                                       _type.BOOL]
    PathUnquoteSpacesA: _Callable[[_type.LPCSTR],
                                  _type.BOOL]
    PathUnquoteSpacesW: _Callable[[_type.LPCWSTR],
                                  _type.BOOL]
    SHCreateMemStream: _Callable[[_Pointer[_type.BYTE],
                                  _type.UINT],
                                 _interface.IStream]
    SHCreateStreamOnFileA: _Callable[[_type.LPCSTR,  # pszFile
                                      _type.DWORD,  # grfMode
                                      _Pointer[_interface.IStream]],  # ppstm
                                     _type.HRESULT]
    SHCreateStreamOnFileW: _Callable[[_type.LPCWSTR,  # pszFile
                                      _type.DWORD,  # grfMode
                                      _Pointer[_interface.IStream]],  # ppstm
                                     _type.HRESULT]
    SHCreateStreamOnFileEx: _Callable[[_type.LPCWSTR,
                                       _type.DWORD,
                                       _type.DWORD,
                                       _type.BOOL,
                                       _Optional[_interface.IStream],
                                       _Pointer[_interface.IStream]],
                                      _type.HRESULT]
    SHOpenRegStreamA: _Callable[[_type.HKEY,
                                 _Optional[_type.LPCSTR],
                                 _Optional[_type.LPCSTR],
                                 _type.DWORD],
                                _interface.IStream]
    SHOpenRegStreamW: _Callable[[_type.HKEY,
                                 _Optional[_type.LPCWSTR],
                                 _Optional[_type.LPCWSTR],
                                 _type.DWORD],
                                _interface.IStream]
    SHOpenRegStream2A: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCSTR],
                                  _Optional[_type.LPCSTR],
                                  _type.DWORD],
                                 _interface.IStream]
    SHOpenRegStream2W: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCWSTR],
                                  _Optional[_type.LPCWSTR],
                                  _type.DWORD],
                                 _interface.IStream]
    UrlGetLocationA: _Callable[[_type.PCSTR],
                               _type.LPCSTR]
    UrlGetLocationW: _Callable[[_type.PCWSTR],
                               _type.LPCWSTR]
    UrlIsA: _Callable[[_type.PCSTR,
                       _enum.URLIS],
                      _type.BOOL]
    UrlIsW: _Callable[[_type.PCWSTR,
                       _enum.URLIS],
                      _type.BOOL]
    UrlIsOpaqueA: _Callable[[_type.PCSTR],
                            _type.BOOL]
    UrlIsOpaqueW: _Callable[[_type.PCWSTR],
                            _type.BOOL]
    UrlIsNoHistoryA: _Callable[[_type.PCSTR],
                               _type.BOOL]
    UrlIsNoHistoryW: _Callable[[_type.PCWSTR],
                               _type.BOOL]


# noinspection PyPep8Naming
class user32(_Func, metaclass=_WinDLL):
    MessageBoxTimeoutA: _Callable[[_Optional[_type.HWND],  # hWnd
                                   _Optional[_type.LPCSTR],  # lpText
                                   _Optional[_type.LPCSTR],  # lpCaption
                                   _type.UINT,  # uType
                                   _type.WORD,  # wLanguageId
                                   _type.DWORD],  # dwMilliseconds
                                  _type.c_int]
    MessageBoxTimeoutW: _Callable[[_Optional[_type.HWND],  # hWnd
                                   _Optional[_type.LPCWSTR],  # lpText
                                   _Optional[_type.LPCWSTR],  # lpCaption
                                   _type.UINT,  # uType
                                   _type.WORD,  # wLanguageId
                                   _type.DWORD],  # dwMilliseconds
                                  _type.c_int]
    # WinUser
    GetWindowTextA: _Callable[[_type.HWND,  # hWnd
                               _type.LPSTR,  # lpString
                               _type.c_int],  # nMaxCount
                              _type.c_int]
    GetWindowTextW: _Callable[[_type.HWND,  # hWnd
                               _type.LPWSTR,  # lpString
                               _type.c_int],  # nMaxCount
                              _type.c_int]
    GetWindowTextLengthA: _Callable[[_type.HWND],  # hWnd
                                    _type.c_int]
    GetWindowTextLengthW: _Callable[[_type.HWND],  # hWnd
                                    _type.c_int]
    MessageBoxA: _Callable[[_Optional[_type.HWND],  # hWnd
                            _Optional[_type.LPCSTR],  # lpText
                            _Optional[_type.LPCSTR],  # lpCaption
                            _type.UINT],
                           _type.c_int]
    MessageBoxW: _Callable[[_Optional[_type.HWND],  # hWnd
                            _Optional[_type.LPCWSTR],  # lpText
                            _Optional[_type.LPCWSTR],  # lpCaption
                            _type.UINT],
                           _type.c_int]
    GetShellWindow: _Callable[[],
                              _type.HWND]
    RegisterShellHookWindow: _Callable[[_type.HWND],  # hwnd
                                       _type.BOOL]
    DeregisterShellHookWindow: _Callable[[_type.HWND],  # hwnd
                                         _type.BOOL]
    EnumWindows: _Callable[[_type.WNDENUMPROC,  # lpEnumFunc
                            _type.LPARAM],  # lParam
                           _type.BOOL]
    EnumThreadWindows: _Callable[[_type.DWORD,  # dwThreadId
                                  _type.WNDENUMPROC,  # lpfn
                                  _type.LPARAM],  # lParam
                                 _type.BOOL]
    GetClassNameA: _Callable[[_type.HWND,  # hWnd
                              _type.LPSTR,  # lpClassName
                              _type.c_int],  # nMaxCount
                             _type.c_int]
    GetClassNameW: _Callable[[_type.HWND,  # hWnd
                              _type.LPWSTR,  # lpClassName
                              _type.c_int],  # nMaxCount
                             _type.c_int]
    GetTopWindow: _Callable[[_Optional[_type.HWND]],  # hWnd
                            _type.HWND]
    GetWindowThreadProcessId: _Callable[[_type.HWND,  # hWnd
                                         _Optional[_Pointer[_type.DWORD]]],  # lpdwProcessId
                                        _type.DWORD]
    IsGUIThread: _Callable[[_type.BOOL],  # bConvert
                           _type.BOOL]
    GetLastActivePopup: _Callable[[_type.HWND],  # hWnd
                                  _type.HWND]
    GetWindow: _Callable[[_type.HWND,  # hWnd
                          _type.UINT],  # uCmd
                         _type.HWND]
    SetWindowsHookA: _Callable[[_type.c_int,  # nFilterType
                                _type.HOOKPROC],  # pfnFilterProc
                               _type.HHOOK]
    SetWindowsHookW: _Callable[[_type.c_int,  # nFilterType
                                _type.HOOKPROC],  # pfnFilterProc
                               _type.HHOOK]
    UnhookWindowsHook: _Callable[[_type.c_int,  # nCode
                                  _type.HOOKPROC],  # pfnFilterProc
                                 _type.BOOL]
    SetWindowsHookExA: _Callable[[_type.c_int,  # idHook
                                  _type.HOOKPROC,  # lpfn
                                  _type.HINSTANCE,  # hmod
                                  _type.DWORD],  # dwThreadId
                                 _type.HHOOK]
    SetWindowsHookExW: _Callable[[_type.c_int,  # idHook
                                  _type.HOOKPROC,  # lpfn
                                  _type.HINSTANCE,  # hmod
                                  _type.DWORD],  # dwThreadId
                                 _type.HHOOK]
    UnhookWindowsHookEx: _Callable[[_type.HHOOK],  # hhk
                                   _type.BOOL]
    CallNextHookEx: _Callable[[_Optional[_type.HHOOK],  # hhk
                               _type.c_int,  # nCode
                               _type.WPARAM,  # wParam
                               _type.LPARAM],  # lParam
                              _type.LRESULT]
    CheckMenuRadioItem: _Callable[[_type.HMENU,  # hmenu
                                   _type.UINT,  # first
                                   _type.UINT,  # last
                                   _type.UINT,  # check
                                   _type.UINT],  # flags
                                  _type.BOOL]
    LoadBitmapA: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                            _type.LPCSTR],  # lpBitmapName
                           _type.HBITMAP]
    LoadBitmapW: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                            _type.LPCWSTR],  # lpBitmapName
                           _type.HBITMAP]
    LoadCursorA: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                            _type.LPCSTR],  # lpCursorName
                           _type.HCURSOR]
    LoadCursorW: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                            _type.LPCWSTR],  # lpCursorName
                           _type.HCURSOR]
    LoadCursorFromFileA: _Callable[[_type.LPCSTR],  # lpFileName
                                   _type.HCURSOR]
    LoadCursorFromFileW: _Callable[[_type.LPCWSTR],  # lpFileName
                                   _type.HCURSOR]
    DestroyCursor: _Callable[[_type.HCURSOR],  # hCursor
                             _type.BOOL]
    SetSystemCursor: _Callable[[_type.HCURSOR,  # hcur
                                _type.DWORD],  # id
                               _type.BOOL]
    LoadIconA: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                          _type.UINT],  # lpIconName
                         _type.HICON]
    LoadIconW: _Callable[[_Optional[_type.HINSTANCE],  # hInstance
                          _type.LPCWSTR],  # lpIconName
                         _type.HICON]
    DestroyIcon: _Callable[[_type.HICON],  # hIcon
                           _type.BOOL]
    SetThreadCursorCreationScaling: _Callable[[_type.UINT],  # cursorDpi
                                              _type.UINT]
    SetLastErrorEx: _Callable[[_type.DWORD,  # dwErrCode
                               _type.DWORD],  # dwType
                              _type.VOID]
    CancelShutdown: _Callable[[],
                              _type.BOOL]
    MonitorFromPoint: _Callable[[_struct.POINT,  # pt,
                                 _type.DWORD],  # dwFlags
                                _type.HMONITOR]
    MonitorFromRect: _Callable[[_Pointer[_struct.RECT],  # lprc,
                                _type.DWORD],  # dwFlags
                               _type.HMONITOR]
    MonitorFromWindow: _Callable[[_type.HWND,  # hwnd,
                                  _type.DWORD],  # dwFlags
                                 _type.HMONITOR]
    # TODO
    wvsprintfA: _Callable[[_type.LPSTR,
                           _type.LPCSTR,
                           _type.va_list],
                          _type.c_int]
    wvsprintfW: _Callable[[_type.LPWSTR,
                           _type.LPCWSTR,
                           _type.va_list],
                          _type.c_int]
    AdjustWindowRect: _Callable[[_Pointer[_struct.RECT],
                                 _type.DWORD,
                                 _type.BOOL],
                                _type.BOOL]
    AdjustWindowRectEx: _Callable[[_Pointer[_struct.RECT],
                                   _type.DWORD,
                                   _type.BOOL,
                                   _type.DWORD],
                                  _type.BOOL]
    AllowSetForegroundWindow: _Callable[[_type.DWORD],
                                        _type.BOOL]
    AnimateWindow: _Callable[[_type.HWND,
                              _type.DWORD,
                              _type.DWORD],
                             _type.BOOL]
    AnyPopup: _Callable[[],
                        _type.BOOL]
    AppendMenuA: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.UINT_PTR,
                            _Optional[_type.LPCSTR]],
                           _type.BOOL]
    AppendMenuW: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.UINT_PTR,
                            _Optional[_type.LPCWSTR]],
                           _type.BOOL]
    AttachThreadInput: _Callable[[_type.DWORD,
                                  _type.DWORD,
                                  _type.BOOL],
                                 _type.BOOL]
    BeginDeferWindowPos: _Callable[[_type.c_int],
                                   _type.BOOL]
    BeginPaint: _Callable[[_type.HWND,
                           _Pointer[_struct.PAINTSTRUCT]],
                          _type.HDC]
    BlockInput: _Callable[[_type.BOOL],
                          _type.BOOL]
    BringWindowToTop: _Callable[[_type.HWND],
                                _type.BOOL]
    BroadcastSystemMessageA: _Callable[[_type.DWORD,
                                        _Optional[_Pointer[_type.DWORD]],
                                        _type.UINT,
                                        _type.WPARAM,
                                        _type.LPARAM],
                                       _type.c_long]
    BroadcastSystemMessageW: _Callable[[_type.DWORD,
                                        _Optional[_Pointer[_type.DWORD]],
                                        _type.UINT,
                                        _type.WPARAM,
                                        _type.LPARAM],
                                       _type.c_long]
    BroadcastSystemMessageExA: _Callable[[_type.DWORD,
                                          _Optional[_Pointer[_type.DWORD]],
                                          _type.UINT,
                                          _type.WPARAM,
                                          _type.LPARAM,
                                          _Optional[_Pointer[_struct.BSMINFO]]],
                                         _type.c_long]
    BroadcastSystemMessageExW: _Callable[[_type.DWORD,
                                          _Optional[_Pointer[_type.DWORD]],
                                          _type.UINT,
                                          _type.WPARAM,
                                          _type.LPARAM,
                                          _Optional[_Pointer[_struct.BSMINFO]]],
                                         _type.c_long]
    CalculatePopupWindowPosition: _Callable[[_Pointer[_struct.POINT],
                                             _Pointer[_struct.SIZE],
                                             _type.UINT,
                                             _Optional[_Pointer[_struct.RECT]],
                                             _Pointer[_struct.RECT]],
                                            _type.BOOL]
    ChangeMenuA: _Callable[[_type.HMENU,
                            _type.UINT,
                            _Optional[_type.LPCSTR],
                            _type.UINT,
                            _type.UINT],
                           _type.BOOL]
    ChangeMenuW: _Callable[[_type.HMENU,
                            _type.UINT,
                            _Optional[_type.LPCWSTR],
                            _type.UINT,
                            _type.UINT],
                           _type.BOOL]
    CheckDlgButton: _Callable[[_type.HWND,
                               _type.c_int,
                               _type.UINT],
                              _type.BOOL]
    CheckMenuItem: _Callable[[_type.HMENU,
                              _type.UINT,
                              _type.UINT],
                             _type.DWORD]
    CheckRadioButton: _Callable[[_type.HWND,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.c_int],
                                _type.BOOL]
    ClientToScreen: _Callable[[_type.HWND,
                               _Pointer[_struct.POINT]],
                              _type.BOOL]
    CloseClipboard: _Callable[[],
                              _type.BOOL]
    CloseWindow: _Callable[[_type.HWND],
                           _type.BOOL]
    CreateDialogIndirectParamA: _Callable[[_Optional[_type.HINSTANCE],
                                           _Pointer[_struct.DLGTEMPLATE],
                                           _Optional[_type.HWND],
                                           _Optional[_type.DLGPROC],
                                           _type.LPARAM],
                                          _type.HWND]
    CreateDialogIndirectParamW: _Callable[[_Optional[_type.HINSTANCE],
                                           _Pointer[_struct.DLGTEMPLATE],
                                           _Optional[_type.HWND],
                                           _Optional[_type.DLGPROC],
                                           _type.LPARAM],
                                          _type.HWND]
    CreateDialogParamA: _Callable[[_Optional[_type.HINSTANCE],
                                   _type.LPCSTR,
                                   _Optional[_type.HWND],
                                   _Optional[_type.DLGPROC],
                                   _type.LPARAM],
                                  _type.HWND]
    CreateDialogParamW: _Callable[[_Optional[_type.HINSTANCE],
                                   _type.LPCWSTR,
                                   _Optional[_type.HWND],
                                   _Optional[_type.DLGPROC],
                                   _type.LPARAM],
                                  _type.HWND]
    CreateIconFromResource: _Callable[[_type.PBYTE,
                                       _type.DWORD,
                                       _type.BOOL,
                                       _type.DWORD],
                                      _type.HICON]
    CreateIconFromResourceEx: _Callable[[_type.PBYTE,
                                         _type.DWORD,
                                         _type.BOOL,
                                         _type.DWORD,
                                         _type.c_int,
                                         _type.c_int,
                                         _type.UINT],
                                        _type.HICON]
    CreateMenu: _Callable[[],
                          _type.HMENU]
    CreatePopupMenu: _Callable[[],
                               _type.HMENU]
    CreateWindowExA: _Callable[[_type.DWORD,
                                _Optional[_type.LPCSTR],
                                _Optional[_type.LPCSTR],
                                _type.DWORD,
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _Optional[_type.HWND],
                                _Optional[_type.HMENU],
                                _Optional[_type.HINSTANCE],
                                _Optional[_type.LPVOID]],
                               _type.HWND]
    CreateWindowExW: _Callable[[_type.DWORD,
                                _Optional[_type.LPCWSTR],
                                _Optional[_type.LPCWSTR],
                                _type.DWORD,
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _Optional[_type.HWND],
                                _Optional[_type.HMENU],
                                _Optional[_type.HINSTANCE],
                                _Optional[_type.LPVOID]],
                               _type.HWND]
    DeferWindowPos: _Callable[[_type.HDWP,
                               _type.HWND,
                               _Optional[_type.HWND],
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.UINT],
                              _type.HDWP]
    DefDlgProcA: _Callable[[_type.HWND,
                            _type.UINT,
                            _type.WPARAM,
                            _type.LPARAM],
                           _type.LRESULT]
    DefDlgProcW: _Callable[[_type.HWND,
                            _type.UINT,
                            _type.WPARAM,
                            _type.LPARAM],
                           _type.LRESULT]
    DefWindowProcA: _Callable[[_type.HWND,
                               _type.UINT,
                               _type.WPARAM,
                               _type.LPARAM],
                              _type.LRESULT]
    DefWindowProcW: _Callable[[_type.HWND,
                               _type.UINT,
                               _type.WPARAM,
                               _type.LPARAM],
                              _type.LRESULT]
    DeleteMenu: _Callable[[_type.HMENU,
                           _type.UINT,
                           _type.UINT],
                          _type.BOOL]
    DestroyMenu: _Callable[[_type.HMENU],
                           _type.BOOL]
    DestroyWindow: _Callable[[_type.HWND],
                             _type.BOOL]
    DialogBoxIndirectParamA: _Callable[[_Optional[_type.HINSTANCE],
                                        _Pointer[_struct.DLGTEMPLATE],
                                        _Optional[_type.HWND],
                                        _Optional[_type.DLGPROC],
                                        _type.LPARAM],
                                       _type.INT_PTR]
    DialogBoxIndirectParamW: _Callable[[_Optional[_type.HINSTANCE],
                                        _Pointer[_struct.DLGTEMPLATE],
                                        _Optional[_type.HWND],
                                        _Optional[_type.DLGPROC],
                                        _type.LPARAM],
                                       _type.INT_PTR]
    DialogBoxParamA: _Callable[[_Optional[_type.HINSTANCE],
                                _type.LPCSTR,
                                _Optional[_type.HWND],
                                _Optional[_type.DLGPROC],
                                _type.LPARAM],
                               _type.INT_PTR]
    DialogBoxParamW: _Callable[[_Optional[_type.HINSTANCE],
                                _type.LPCWSTR,
                                _Optional[_type.HWND],
                                _Optional[_type.DLGPROC],
                                _type.LPARAM],
                               _type.INT_PTR]
    DispatchMessageA: _Callable[[_Pointer[_struct.MSG]],
                                _type.BOOL]
    DispatchMessageW: _Callable[[_Pointer[_struct.MSG]],
                                _type.BOOL]
    DisplayConfigGetDeviceInfo: _Callable[[_Pointer[_struct.DISPLAYCONFIG_DEVICE_INFO_HEADER]],
                                          _type.LONG]
    DisplayConfigSetDeviceInfo: _Callable[[_Pointer[_struct.DISPLAYCONFIG_DEVICE_INFO_HEADER]],
                                          _type.LONG]
    DragDetect: _Callable[[_type.HWND,
                           _struct.POINT],
                          _type.BOOL]
    DragObject: _Callable[[_type.HWND,
                           _type.HWND,
                           _type.UINT,
                           _type.ULONG_PTR,
                           _Optional[_type.HCURSOR]],
                          _type.DWORD]
    DrawIcon: _Callable[[_type.HDC,
                         _type.c_int,
                         _type.c_int,
                         _type.HICON],
                        _type.BOOL]
    DrawMenuBar: _Callable[[_type.HWND],
                           _type.BOOL]
    EmptyClipboard: _Callable[[],
                              _type.BOOL]
    EnableMenuItem: _Callable[[_type.HMENU,
                               _type.UINT,
                               _type.UINT],
                              _type.BOOL]
    EnableNonClientDpiScaling: _Callable[[_type.HWND],
                                         _type.BOOL]
    EndDeferWindowPos: _Callable[[_type.HDWP],
                                 _type.BOOL]
    EndDialog: _Callable[[_type.HWND,
                          _type.INT_PTR],
                         _type.BOOL]
    EndMenu: _Callable[[],
                       _type.BOOL]
    EndPaint: _Callable[[_type.HWND,
                         _Pointer[_struct.PAINTSTRUCT]],
                        _type.BOOL]
    EnumChildWindows: _Callable[[_Optional[_type.HWND],
                                 _type.WNDENUMPROC,
                                 _type.LPARAM],
                                _type.BOOL]
    EnumDisplayDevicesA: _Callable[[_Optional[_type.LPCSTR],
                                    _type.DWORD,
                                    _Pointer[_struct.DISPLAY_DEVICEA],
                                    _type.DWORD],
                                   _type.BOOL]
    EnumDisplayDevicesW: _Callable[[_Optional[_type.LPCWSTR],
                                    _type.DWORD,
                                    _Pointer[_struct.DISPLAY_DEVICEW],
                                    _type.DWORD],
                                   _type.BOOL]
    EnumDisplayMonitors: _Callable[[_Optional[_type.HDC],
                                    _Optional[_Pointer[_struct.RECT]],
                                    _type.MONITORENUMPROC,
                                    _type.LPARAM],
                                   _type.BOOL]
    EqualRect: _Callable[[_Pointer[_struct.RECT],
                          _Pointer[_struct.RECT]],
                         _type.BOOL]
    ExitWindowsEx: _Callable[[_type.UINT,
                              _type.DWORD],
                             _type.BOOL]
    FillRect: _Callable[[_type.HDC,
                         _Pointer[_struct.RECT],
                         _type.HBRUSH],
                        _type.c_int]
    FindWindowA: _Callable[[_type.LPCSTR,
                            _Optional[_type.LPCSTR]],
                           _type.HWND]
    FindWindowW: _Callable[[_type.LPCWSTR,
                            _Optional[_type.LPCWSTR]],
                           _type.HWND]
    FindWindowExA: _Callable[[_Optional[_type.HWND],
                              _Optional[_type.HWND],
                              _type.LPCSTR,
                              _Optional[_type.LPCSTR]],
                             _type.HWND]
    FindWindowExW: _Callable[[_Optional[_type.HWND],
                              _Optional[_type.HWND],
                              _type.LPCWSTR,
                              _Optional[_type.LPCWSTR]],
                             _type.HWND]
    FlashWindow: _Callable[[_type.HWND,
                            _type.BOOL],
                           _type.BOOL]
    GetActiveWindow: _Callable[[],
                               _type.HWND]
    GetAncestor: _Callable[[_type.HWND,
                            _type.UINT],
                           _type.HWND]
    GetAsyncKeyState: _Callable[[_type.c_int],
                                _type.SHORT]
    GetAutoRotationState: _Callable[[_Pointer[_enum.AR_STATE]],
                                    _type.BOOL]
    GetCIMSSM: _Callable[[_Pointer[_struct.INPUT_MESSAGE_SOURCE]],
                         _type.BOOL]
    GetClassInfoA: _Callable[[_Optional[_type.HINSTANCE],
                              _type.LPCSTR,
                              _Pointer[_struct.WNDCLASSA]],
                             _type.BOOL]
    GetClassInfoW: _Callable[[_Optional[_type.HINSTANCE],
                              _type.LPCWSTR,
                              _Pointer[_struct.WNDCLASSW]],
                             _type.BOOL]
    GetClassInfoExA: _Callable[[_Optional[_type.HINSTANCE],
                                _type.LPCSTR,
                                _Pointer[_struct.WNDCLASSEXA]],
                               _type.BOOL]
    GetClassInfoExW: _Callable[[_Optional[_type.HINSTANCE],
                                _type.LPCWSTR,
                                _Pointer[_struct.WNDCLASSEXW]],
                               _type.BOOL]
    GetClientRect: _Callable[[_type.HWND,
                              _Pointer[_struct.RECT]],
                             _type.BOOL]
    GetClipboardData: _Callable[[_type.UINT],
                                _type.HANDLE]
    GetCurrentInputMessageSource: _Callable[[_Pointer[_struct.INPUT_MESSAGE_SOURCE]],
                                            _type.BOOL]
    GetCursorPos: _Callable[[_Pointer[_struct.POINT]],
                            _type.BOOL]
    GetDisplayConfigBufferSizes: _Callable[[_type.UINT32,
                                            _Pointer[_type.UINT32],
                                            _Pointer[_type.UINT32]],
                                           _type.LONG]
    GetDesktopWindow: _Callable[[],
                                _type.HWND]
    GetDC: _Callable[[_Optional[_type.HWND]],
                     _type.HDC]
    GetDCEx: _Callable[[_Optional[_type.HWND],
                        _type.HRGN,
                        _type.DWORD],
                       _type.HDC]
    GetDialogBaseUnits: _Callable[[],
                                  _type.c_long]
    GetDisplayAutoRotationPreferences: _Callable[[_Pointer[_enum.ORIENTATION_PREFERENCE]],
                                                 _type.BOOL]
    GetDisplayAutoRotationPreferencesByProcessId: _Callable[[_type.DWORD,
                                                             _Pointer[_enum.ORIENTATION_PREFERENCE],
                                                             _Pointer[_type.BOOL]],
                                                            _type.BOOL]
    GetDlgCtrlID: _Callable[[_type.HWND],
                            _type.c_int]
    GetDlgItem: _Callable[[_Optional[_type.HWND],
                           _type.c_int],
                          _type.HWND]
    GetDlgItemInt: _Callable[[_type.HWND,
                              _type.c_int,
                              _Optional[_Pointer[_type.BOOL]],
                              _type.BOOL],
                             _type.UINT]
    GetDlgItemTextA: _Callable[[_type.HWND,
                                _type.c_int,
                                _type.LPSTR,
                                _type.c_int],
                               _type.UINT]
    GetDlgItemTextW: _Callable[[_type.HWND,
                                _type.c_int,
                                _type.LPWSTR,
                                _type.c_int],
                               _type.UINT]
    GetDoubleClickTime: _Callable[[],
                                  _type.UINT]
    GetDpiForSystem: _Callable[[],
                               _type.UINT]
    GetDpiForWindow: _Callable[[_type.HWND],
                               _type.UINT]
    GetFocus: _Callable[[],
                        _type.HWND]
    GetForegroundWindow: _Callable[[],
                                   _type.HWND]
    GetGUIThreadInfo: _Callable[[_type.DWORD,
                                 _Pointer[_struct.GUITHREADINFO]],
                                _type.BOOL]
    GetKBCodePage: _Callable[[],
                             _type.UINT]
    GetKeyboardState: _Callable[[_type.PBYTE],
                                _type.BOOL]
    GetKeyState: _Callable[[_type.c_int],
                           _type.SHORT]
    GetMenu: _Callable[[_type.HWND],
                       _type.HMENU]
    GetMenuCheckMarkDimensions: _Callable[[],
                                          _type.LONG]
    GetMenuDefaultItem: _Callable[[_type.HMENU,
                                   _type.UINT,
                                   _type.UINT],
                                  _type.UINT]
    GetMenuInfo: _Callable[[_type.HMENU,
                            _Pointer[_struct.MENUINFO]],
                           _type.BOOL]
    GetMenuItemCount: _Callable[[_Optional[_type.HMENU]],
                                _type.c_int]
    GetMenuItemID: _Callable[[_type.HMENU,
                              _type.c_int],
                             _type.UINT]
    GetMenuItemInfoA: _Callable[[_type.HMENU,
                                 _type.UINT,
                                 _type.BOOL,
                                 _Pointer[_struct.MENUITEMINFOA]],
                                _type.BOOL]
    GetMenuItemInfoW: _Callable[[_type.HMENU,
                                 _type.UINT,
                                 _type.BOOL,
                                 _Pointer[_struct.MENUITEMINFOW]],
                                _type.BOOL]
    GetMenuItemRect: _Callable[[_Optional[_type.HWND],
                                _type.HMENU,
                                _type.UINT,
                                _Pointer[_struct.RECT]],
                               _type.BOOL]
    GetMenuState: _Callable[[_type.HMENU,
                             _type.UINT,
                             _type.UINT],
                            _type.UINT]
    GetMenuStringA: _Callable[[_type.HMENU,
                               _type.UINT,
                               _Optional[_type.LPSTR],
                               _type.c_int,
                               _type.UINT],
                              _type.c_int]
    GetMenuStringW: _Callable[[_type.HMENU,
                               _type.UINT,
                               _Optional[_type.LPWSTR],
                               _type.c_int,
                               _type.UINT],
                              _type.c_int]
    GetMessageA: _Callable[[_Pointer[_struct.MSG],
                            _Optional[_type.HWND],
                            _type.UINT,
                            _type.UINT],
                           _type.BOOL]
    GetMessageW: _Callable[[_Pointer[_struct.MSG],
                            _Optional[_type.HWND],
                            _type.UINT,
                            _type.UINT],
                           _type.BOOL]
    GetMessageExtraInfo: _Callable[[],
                                   _type.LPARAM]
    GetMessagePos: _Callable[[],
                             _type.DWORD]
    GetMessageTime: _Callable[[],
                              _type.LONG]
    GetMonitorInfoA: _Callable[[_type.HMONITOR,
                                _Pointer[_struct.MONITORINFO]],
                               _type.BOOL]
    GetMonitorInfoW: _Callable[[_type.HMONITOR,
                                _Pointer[_struct.MONITORINFO]],
                               _type.BOOL]
    GetNextDlgGroupItem: _Callable[[_type.HWND,
                                    _Optional[_type.HWND],
                                    _type.BOOL],
                                   _type.HWND]
    GetNextDlgTabItem: _Callable[[_type.HWND,
                                  _Optional[_type.HWND],
                                  _type.BOOL],
                                 _type.HWND]
    GetParent: _Callable[[_type.HWND],
                         _type.HWND]
    GetProcessDefaultLayout: _Callable[[_Pointer[_type.DWORD]],
                                       _type.BOOL]
    GetSubMenu: _Callable[[_type.HMENU,
                           _type.c_int],
                          _type.HMENU]
    GetSysColor: _Callable[[_type.c_int],
                           _type.DWORD]
    GetSysColorBrush: _Callable[[_type.c_int],
                                _type.HBRUSH]
    GetSystemDpiForProcess: _Callable[[_type.HANDLE],
                                      _type.UINT]
    GetSystemMenu: _Callable[[_type.HWND,
                              _type.BOOL],
                             _type.HMENU]
    GetSystemMetrics: _Callable[[_type.c_int],
                                _type.c_int]
    GetUnpredictedMessagePos: _Callable[[],
                                        _type.DWORD]
    GetWindowDC: _Callable[[_Optional[_type.HWND]],
                           _type.HDC]
    GetWindowDisplayAffinity: _Callable[[_type.HWND,
                                         _Pointer[_type.DWORD]],
                                        _type.BOOL]
    GetWindowPlacement: _Callable[[_type.HWND,
                                   _Pointer[_struct.WINDOWPLACEMENT]],
                                  _type.BOOL]
    GetWindowRect: _Callable[[_type.HWND,
                              _Pointer[_struct.RECT]],
                             _type.BOOL]
    HiliteMenuItem: _Callable[[_type.HWND,
                               _type.HMENU,
                               _type.UINT,
                               _type.UINT],
                              _type.BOOL]
    InheritWindowMonitor: _Callable[[_type.HWND,
                                     _Optional[_type.HWND]],
                                    _type.BOOL]
    InsertMenuA: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.UINT,
                            _type.UINT_PTR,
                            _Optional[_type.LPCSTR]],
                           _type.BOOL]
    InsertMenuW: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.UINT,
                            _type.UINT_PTR,
                            _Optional[_type.LPCWSTR]],
                           _type.BOOL]
    InsertMenuItemA: _Callable[[_type.HMENU,
                                _type.UINT,
                                _type.BOOL,
                                _Pointer[_struct.MENUITEMINFOA]],
                               _type.BOOL]
    InsertMenuItemW: _Callable[[_type.HMENU,
                                _type.UINT,
                                _type.BOOL,
                                _Pointer[_struct.MENUITEMINFOW]],
                               _type.BOOL]
    IntersectRect: _Callable[[_Pointer[_struct.RECT],
                              _Pointer[_struct.RECT],
                              _Pointer[_struct.RECT]],
                             _type.BOOL]
    IsChild: _Callable[[_type.HWND,
                        _type.HWND],
                       _type.BOOL]
    IsDlgButtonChecked: _Callable[[_type.HWND,
                                   _type.c_int],
                                  _type.UINT]
    IsIconic: _Callable[[_type.HWND],
                        _type.BOOL]
    IsImmersiveProcess: _Callable[[_type.HANDLE],
                                  _type.BOOL]
    IsMenu: _Callable[[_type.HMENU],
                      _type.BOOL]
    IsProcessDPIAware: _Callable[[],
                                 _type.BOOL]
    IsRectEmpty: _Callable[[_Pointer[_struct.RECT]],
                           _type.BOOL]
    IsWindow: _Callable[[_type.HWND],
                        _type.BOOL]
    IsWindowVisible: _Callable[[_type.HWND],
                               _type.BOOL]
    IsWow64Message: _Callable[[],
                              _type.BOOL]
    IsZoomed: _Callable[[_type.HWND],
                        _type.BOOL]
    QueryDisplayConfig: _Callable[[_type.UINT32,
                                   _Pointer[_type.UINT32],
                                   _Pointer[_struct.DISPLAYCONFIG_PATH_INFO],
                                   _Pointer[_type.UINT32],
                                   _Pointer[_struct.DISPLAYCONFIG_MODE_INFO],
                                   _Optional[_Pointer[_enum.DISPLAYCONFIG_TOPOLOGY_ID]]],
                                  _type.LONG]
    KillTimer: _Callable[[_type.HWND,
                          _type.UINT_PTR],
                         _type.BOOL]
    LoadImageA: _Callable[[_Optional[_type.HINSTANCE],
                           _type.LPCSTR,
                           _type.UINT,
                           _type.c_int,
                           _type.c_int,
                           _type.UINT],
                          _type.HANDLE]
    LoadImageW: _Callable[[_Optional[_type.HINSTANCE],
                           _type.LPCWSTR,
                           _type.UINT,
                           _type.c_int,
                           _type.c_int,
                           _type.UINT],
                          _type.HANDLE]
    LoadMenuA: _Callable[[_Optional[_type.HINSTANCE],
                          _type.LPCSTR],
                         _type.HMENU]
    LoadMenuW: _Callable[[_Optional[_type.HINSTANCE],
                          _type.LPCWSTR],
                         _type.HMENU]
    LoadMenuIndirectA: _Callable[[_type.MENUTEMPLATEA],
                                 _type.HMENU]
    LoadMenuIndirectW: _Callable[[_type.MENUTEMPLATEW],
                                 _type.HMENU]
    LoadStringA: _Callable[[_Optional[_type.HINSTANCE],
                            _type.UINT,
                            _type.LPSTR,
                            _type.c_int],
                           _type.c_int]
    LoadStringW: _Callable[[_Optional[_type.HINSTANCE],
                            _type.UINT,
                            _type.LPWSTR,
                            _type.c_int],
                           _type.c_int]
    LockSetForegroundWindow: _Callable[[_type.UINT],
                                       _type.BOOL]
    LockWorkStation: _Callable[[],
                               _type.BOOL]
    MapWindowPoints: _Callable[[_Optional[_type.HWND],
                                _Optional[_type.HWND],
                                _Pointer[_struct.POINT],
                                _type.UINT],
                               _type.c_int]
    MenuItemFromPoint: _Callable[[_Optional[_type.HWND],
                                  _type.HMENU,
                                  _struct.POINT],
                                 _type.c_int]
    ModifyMenuA: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.UINT,
                            _type.UINT_PTR,
                            _Optional[_type.LPCSTR]],
                           _type.BOOL]
    ModifyMenuW: _Callable[[_type.HMENU,
                            _type.UINT,
                            _type.UINT,
                            _type.UINT_PTR,
                            _Optional[_type.LPCWSTR]],
                           _type.BOOL]
    MoveWindow: _Callable[[_type.HWND,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.c_int,
                           _type.BOOL],
                          _type.BOOL]
    NotifyWinEvent: _Callable[[_type.DWORD,
                               _type.HWND,
                               _type.LONG,
                               _type.LONG],
                              _type.VOID]
    OffsetRect: _Callable[[_Pointer[_struct.RECT],
                           _Pointer[_struct.RECT],
                           _Pointer[_struct.RECT]],
                          _type.BOOL]
    OpenClipboard: _Callable[[_Optional[_type.HWND]],
                             _type.BOOL]
    OpenIcon: _Callable[[_type.HWND],
                        _type.BOOL]
    PaintDesktop: _Callable[[_type.HDC],
                            _type.BOOL]
    PostMessageA: _Callable[[_Optional[_type.HWND],
                             _type.UINT,
                             _type.WPARAM,
                             _type.LPARAM],
                            _type.BOOL]
    PostMessageW: _Callable[[_Optional[_type.HWND],
                             _type.UINT,
                             _type.WPARAM,
                             _type.LPARAM],
                            _type.BOOL]
    PostQuitMessage: _Callable[[_type.c_int],
                               _type.VOID]
    PostThreadMessageA: _Callable[[_type.DWORD,
                                   _type.UINT,
                                   _type.WPARAM,
                                   _type.LPARAM],
                                  _type.BOOL]
    PostThreadMessageW: _Callable[[_type.DWORD,
                                   _type.UINT,
                                   _type.WPARAM,
                                   _type.LPARAM],
                                  _type.BOOL]
    PrintWindow: _Callable[[_type.HWND,
                            _type.HDC,
                            _type.UINT],
                           _type.BOOL]
    PtInRect: _Callable[[_Pointer[_struct.RECT],
                         _struct.POINT],
                        _type.BOOL]
    RealChildWindowFromPoint: _Callable[[_type.HWND,
                                         _struct.POINT],
                                        _type.HWND]
    RealGetWindowClassA: _Callable[[_type.HWND,
                                    _type.LPSTR,
                                    _type.UINT],
                                   _type.UINT]
    RealGetWindowClassW: _Callable[[_type.HWND,
                                    _type.LPWSTR,
                                    _type.UINT],
                                   _type.UINT]
    RegisterClassA: _Callable[[_Pointer[_struct.WNDCLASSA]],
                              _type.ATOM]
    RegisterClassW: _Callable[[_Pointer[_struct.WNDCLASSW]],
                              _type.ATOM]
    RegisterClassExA: _Callable[[_Pointer[_struct.WNDCLASSEXA]],
                                _type.ATOM]
    RegisterClassExW: _Callable[[_Pointer[_struct.WNDCLASSEXW]],
                                _type.ATOM]
    RegisterWindowMessageA: _Callable[[_type.LPCSTR],
                                      _type.UINT]
    RegisterWindowMessageW: _Callable[[_type.LPCWSTR],
                                      _type.UINT]
    RemoveMenu: _Callable[[_type.HMENU,
                           _type.UINT,
                           _type.UINT],
                          _type.BOOL]
    ReleaseDC: _Callable[[_Optional[_type.HWND],
                          _type.HDC],
                         _type.c_int]
    ReplyMessage: _Callable[[_type.LRESULT],
                            _type.BOOL]
    SendDlgItemMessageA: _Callable[[_type.HWND,
                                    _type.c_int,
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM],
                                   _type.LRESULT]
    SendDlgItemMessageW: _Callable[[_type.HWND,
                                    _type.c_int,
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM],
                                   _type.LRESULT]
    SendInput: _Callable[[_type.UINT,
                          _Pointer[_struct.INPUT],
                          _type.c_int],
                         _type.UINT]
    SendMessageA: _Callable[[_type.HWND,
                             _type.UINT,
                             _type.WPARAM,
                             _type.LPARAM],
                            _type.LRESULT]
    SendMessageW: _Callable[[_type.HWND,
                             _type.UINT,
                             _type.WPARAM,
                             _type.LPARAM],
                            _type.LRESULT]
    SendMessageCallbackA: _Callable[[_type.HWND,
                                     _type.UINT,
                                     _type.WPARAM,
                                     _type.LPARAM,
                                     _type.SENDASYNCPROC,
                                     _type.ULONG_PTR],
                                    _type.BOOL]
    SendMessageCallbackW: _Callable[[_type.HWND,
                                     _type.UINT,
                                     _type.WPARAM,
                                     _type.LPARAM,
                                     _type.SENDASYNCPROC,
                                     _type.ULONG_PTR],
                                    _type.BOOL]
    SendMessageTimeoutA: _Callable[[_type.HWND,
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM,
                                    _type.UINT,
                                    _type.UINT,
                                    _Optional[_type.PDWORD_PTR]],
                                   _type.LRESULT]
    SendMessageTimeoutW: _Callable[[_type.HWND,
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM,
                                    _type.UINT,
                                    _type.UINT,
                                    _Optional[_type.PDWORD_PTR]],
                                   _type.LRESULT]
    SendNotifyMessageA: _Callable[[_type.HWND,
                                   _type.UINT,
                                   _type.WPARAM,
                                   _type.LPARAM],
                                  _type.BOOL]
    SendNotifyMessageW: _Callable[[_type.HWND,
                                   _type.UINT,
                                   _type.WPARAM,
                                   _type.LPARAM],
                                  _type.BOOL]
    SetActiveWindow: _Callable[[_type.HWND],
                               _type.BOOL]
    SetClipboardData: _Callable[[_type.UINT,
                                 _type.HANDLE],
                                _type.HANDLE]
    SetCursor: _Callable[[_Optional[_type.HCURSOR]],
                         _type.HCURSOR]
    SetDisplayAutoRotationPreferences: _Callable[[_enum.ORIENTATION_PREFERENCE],
                                                 _type.BOOL]
    SetDisplayConfig: _Callable[[_type.UINT32,
                                 _Pointer[_struct.DISPLAYCONFIG_PATH_INFO],
                                 _type.UINT32,
                                 _Pointer[_struct.DISPLAYCONFIG_MODE_INFO],
                                 _type.UINT32],
                                _type.LONG]
    SetDlgItemInt: _Callable[[_type.HWND,
                              _type.c_int,
                              _type.UINT,
                              _type.BOOL],
                             _type.BOOL]
    SetDlgItemTextA: _Callable[[_type.HWND,
                                _type.c_int,
                                _type.LPCSTR],
                               _type.BOOL]
    SetDlgItemTextW: _Callable[[_type.HWND,
                                _type.c_int,
                                _type.LPCWSTR],
                               _type.BOOL]
    SetDoubleClickTime: _Callable[[_type.UINT],
                                  _type.BOOL]
    SetFocus: _Callable[[_type.HWND],
                        _type.HWND]
    SetForegroundWindow: _Callable[[_type.HWND],
                                   _type.BOOL]
    SetKeyboardState: _Callable[[_type.PBYTE],
                                _type.BOOL]
    SetMenu: _Callable[[_type.HWND,
                        _Optional[_type.HMENU]],
                       _type.BOOL]
    SetMenuDefaultItem: _Callable[[_type.HMENU,
                                   _type.UINT,
                                   _type.UINT],
                                  _type.BOOL]
    SetMenuInfo: _Callable[[_type.HMENU,
                            _Pointer[_struct.MENUINFO]],
                           _type.BOOL]
    SetMenuItemBitmaps: _Callable[[_type.HMENU,
                                   _type.UINT,
                                   _type.UINT,
                                   _Optional[_type.HBITMAP],
                                   _Optional[_type.HBITMAP]],
                                  _type.BOOL]
    SetMenuItemInfoA: _Callable[[_type.HMENU,
                                 _type.UINT,
                                 _type.BOOL,
                                 _Pointer[_struct.MENUITEMINFOA]],
                                _type.BOOL]
    SetMenuItemInfoW: _Callable[[_type.HMENU,
                                 _type.UINT,
                                 _type.BOOL,
                                 _Pointer[_struct.MENUITEMINFOW]],
                                _type.BOOL]
    SetMessageExtraInfo: _Callable[[_type.LPARAM],
                                   _type.LPARAM]
    SetParent: _Callable[[_type.HWND,
                          _Optional[_type.HWND]],
                         _type.HWND]
    SetProcessDefaultLayout: _Callable[[_type.DWORD],
                                       _type.BOOL]
    SetProcessDPIAware: _Callable[[],
                                  _type.BOOL]
    SetProcessRestrictionExemption: _Callable[[_type.BOOL],
                                              _type.BOOL]
    SetSysColors: _Callable[[_type.c_int,
                             _Pointer[_type.INT],
                             _Pointer[_type.COLORREF]],
                            _type.BOOL]
    SetTimer: _Callable[[_Optional[_type.HWND],
                         _type.UINT_PTR,
                         _type.UINT,
                         _Optional[_type.TIMERPROC]],
                        _type.UINT_PTR]
    SetWinEventHook: _Callable[[_type.DWORD,
                                _type.DWORD,
                                _Optional[_type.HMODULE],
                                _type.WINEVENTPROC,
                                _type.DWORD,
                                _type.DWORD,
                                _type.DWORD],
                               _type.HWINEVENTHOOK]
    SetWindowDisplayAffinity: _Callable[[_type.HWND,
                                         _type.DWORD],
                                        _type.BOOL]
    SetWindowPlacement: _Callable[[_type.HWND,
                                   _Pointer[_struct.WINDOWPLACEMENT]],
                                  _type.BOOL]
    SetWindowPos: _Callable[[_type.HWND,
                             _Optional[_type.HWND],
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _type.UINT],
                            _type.BOOL]
    SetWindowTextA: _Callable[[_type.HWND,
                               _type.LPCSTR],
                              _type.BOOL]
    SetWindowTextW: _Callable[[_type.HWND,
                               _type.LPCWSTR],
                              _type.BOOL]
    ShowCursor: _Callable[[_type.BOOL],
                          _type.c_int]
    ShowOwnedPopups: _Callable[[_type.HWND,
                                _type.BOOL],
                               _type.BOOL]
    ShowWindow: _Callable[[_type.HWND,
                           _type.c_int],
                          _type.BOOL]
    ShowWindowAsync: _Callable[[_type.HWND,
                                _type.c_int],
                               _type.BOOL]
    ShutdownBlockReasonCreate: _Callable[[_type.HWND,
                                          _type.LPCWSTR],
                                         _type.BOOL]
    ShutdownBlockReasonDestroy: _Callable[[_type.HWND],
                                          _type.BOOL]
    ShutdownBlockReasonQuery: _Callable[[_type.HWND,
                                         _Optional[_type.LPWSTR],
                                         _Pointer[_type.DWORD]],
                                        _type.BOOL]
    SubtractRect: _Callable[[_Pointer[_struct.RECT],
                             _Pointer[_struct.RECT],
                             _Pointer[_struct.RECT]],
                            _type.BOOL]
    SwapMouseButton: _Callable[[_type.BOOL],
                               _type.BOOL]
    SwitchToThisWindow: _Callable[[_type.HWND,
                                   _type.BOOL],
                                  _type.VOID]
    SystemParametersInfoA: _Callable[[_type.UINT,
                                      _type.UINT,
                                      _type.PVOID,
                                      _type.UINT],
                                     _type.BOOL]
    SystemParametersInfoW: _Callable[[_type.UINT,
                                      _type.UINT,
                                      _type.PVOID,
                                      _type.UINT],
                                     _type.BOOL]
    TrackMouseEvent: _Callable[[_Pointer[_struct.TRACKMOUSEEVENT]],
                               _type.BOOL]
    TrackPopupMenu: _Callable[[_type.HMENU,
                               _type.UINT,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.HWND,
                               _Optional[_Pointer[_struct.RECT]]],
                              _type.BOOL]
    TrackPopupMenuEx: _Callable[[_type.HMENU,
                                 _type.UINT,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.HWND,
                                 _Optional[_Pointer[_struct.TPMPARAMS]]],
                                _type.BOOL]
    TranslateMessage: _Callable[[_Pointer[_struct.MSG]],
                                _type.BOOL]
    UnhookWinEvent: _Callable[[_type.HWINEVENTHOOK],
                              _type.BOOL]
    UnionRect: _Callable[[_Pointer[_struct.RECT],
                          _Pointer[_struct.RECT],
                          _Pointer[_struct.RECT]],
                         _type.BOOL]
    UnregisterClassA: _Callable[[_type.LPCSTR,
                                 _type.HINSTANCE],
                                _type.BOOL]
    UnregisterClassW: _Callable[[_type.LPCWSTR,
                                 _type.HINSTANCE],
                                _type.BOOL]
    UpdateWindow: _Callable[[_type.HWND],
                            _type.BOOL]
    WaitForInputIdle: _Callable[[_type.HANDLE,
                                 _type.DWORD],
                                _type.DWORD]
    WaitMessage: _Callable[[],
                           _type.BOOL]
    WindowFromDC: _Callable[[_type.HDC],
                            _type.HWND]


# noinspection PyPep8Naming
class uxtheme(_Func, metaclass=_WinDLL):
    # Uxtheme
    BeginPanningFeedback: _Callable[[_type.HWND],
                                    _type.BOOL]
    BufferedPaintInit: _Callable[[],
                                 _type.HRESULT]
    BufferedPaintUnInit: _Callable[[],
                                   _type.HRESULT]
    CloseThemeData: _Callable[[_type.HTHEME],
                              _type.HRESULT]
    DrawThemeBackground: _Callable[[_type.HTHEME,
                                    _type.HDC,
                                    _type.c_int,
                                    _type.c_int,
                                    _Pointer[_struct.RECT],
                                    _Optional[_Pointer[_struct.RECT]]],
                                   _type.HRESULT]
    DrawThemeBackgroundEx: _Callable[[_type.HTHEME,
                                      _type.HDC,
                                      _type.c_int,
                                      _type.c_int,
                                      _Pointer[_struct.RECT],
                                      _Optional[_Pointer[_struct.DTBGOPTS]]],
                                     _type.HRESULT]
    DrawThemeEdge: _Callable[[_type.HTHEME,
                              _type.HDC,
                              _type.c_int,
                              _type.c_int,
                              _Pointer[_struct.RECT],
                              _type.UINT,
                              _type.UINT,
                              _Optional[_Pointer[_struct.RECT]]],
                             _type.HRESULT]
    DrawThemeParentBackground: _Callable[[_type.HWND,
                                          _type.HDC,
                                          _Optional[_Pointer[_struct.RECT]]],
                                         _type.HRESULT]
    DrawThemeParentBackgroundEx: _Callable[[_type.HWND,
                                            _type.HDC,
                                            _type.DWORD,
                                            _Optional[_Pointer[_struct.RECT]]],
                                           _type.HRESULT]
    DrawThemeText: _Callable[[_type.HTHEME,
                              _type.HDC,
                              _type.c_int,
                              _type.c_int,
                              _type.LPCWSTR,
                              _type.c_int,
                              _type.DWORD,
                              _type.DWORD,
                              _Pointer[_struct.RECT]],
                             _type.HRESULT]
    EnableTheming: _Callable[[_type.BOOL],
                             _type.HRESULT]
    EnableThemeDialogTexture: _Callable[[_type.HWND,
                                         _type.DWORD],
                                        _type.HRESULT]
    EndPanningFeedback: _Callable[[_type.HWND,
                                   _type.BOOL],
                                  _type.BOOL]
    GetCurrentThemeName: _Callable[[_type.LPWSTR,
                                    _type.c_int,
                                    _Optional[_type.LPWSTR],
                                    _type.c_int,
                                    _Optional[_type.LPWSTR],
                                    _type.c_int],
                                   _type.HRESULT]
    GetThemeBackgroundExtent: _Callable[[_type.HTHEME,
                                         _Optional[_type.HDC],
                                         _type.c_int,
                                         _type.c_int,
                                         _Pointer[_struct.RECT],
                                         _Pointer[_struct.RECT]],
                                        _type.HRESULT]
    GetThemeBackgroundContentRect: _Callable[[_type.HTHEME,
                                              _Optional[_type.HDC],
                                              _type.c_int,
                                              _type.c_int,
                                              _Pointer[_struct.RECT],
                                              _Pointer[_struct.RECT]],
                                             _type.HRESULT]
    GetThemeBackgroundRegion: _Callable[[_type.HTHEME,
                                         _Optional[_type.HDC],
                                         _type.c_int,
                                         _type.c_int,
                                         _Pointer[_struct.RECT],
                                         _Pointer[_type.HRGN]],
                                        _type.HRESULT]
    GetThemeBool: _Callable[[_type.HTHEME,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _Pointer[_type.BOOL]],
                            _type.HRESULT]
    GetThemeColor: _Callable[[_type.HTHEME,
                              _type.c_int,
                              _type.c_int,
                              _type.c_int,
                              _Pointer[_type.COLORREF]],
                             _type.HRESULT]
    GetThemeEnumValue: _Callable[[_type.HTHEME,
                                  _type.c_int,
                                  _type.c_int,
                                  _type.c_int,
                                  _Pointer[_type.c_int]],
                                 _type.HRESULT]
    GetThemeDocumentationProperty: _Callable[[_type.LPCWSTR,
                                              _type.LPCWSTR,
                                              _type.LPWSTR,
                                              _type.c_int],
                                             _type.HRESULT]
    GetThemeFilename: _Callable[[_type.HTHEME,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.LPWSTR,
                                 _type.c_int],
                                _type.HRESULT]
    GetThemeFont: _Callable[[_type.HTHEME,
                             _Optional[_type.HDC],
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _Pointer[_struct.LOGFONTW]],
                            _type.HRESULT]
    GetThemeInt: _Callable[[_type.HTHEME,
                            _type.c_int,
                            _type.c_int,
                            _type.c_int,
                            _Pointer[_type.c_int]],
                           _type.HRESULT]
    GetThemeIntList: _Callable[[_type.HTHEME,
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _Pointer[_struct.INTLIST]],
                               _type.HRESULT]
    GetThemeMargins: _Callable[[_type.HTHEME,
                                _Optional[_type.HDC],
                                _type.c_int,
                                _type.c_int,
                                _type.c_int,
                                _Optional[_Pointer[_struct.RECT]],
                                _Pointer[_struct.MARGINS]],
                               _type.HRESULT]
    GetThemeMetric: _Callable[[_type.HTHEME,
                               _Optional[_type.HDC],
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _Pointer[_type.c_int]],
                              _type.HRESULT]
    GetThemePartSize: _Callable[[_type.HTHEME,
                                 _Optional[_type.HDC],
                                 _type.c_int,
                                 _type.c_int,
                                 _Optional[_Pointer[_struct.RECT]],
                                 _enum.THEMESIZE,
                                 _Pointer[_struct.SIZE]],
                                _type.HRESULT]
    GetThemePosition: _Callable[[_type.HTHEME,
                                 _type.c_int,
                                 _type.c_int,
                                 _type.c_int,
                                 _Pointer[_struct.POINT]],
                                _type.HRESULT]
    GetThemeAppProperties: _Callable[[],
                                     _type.DWORD]
    GetThemePropertyOrigin: _Callable[[_type.HTHEME,
                                       _type.c_int,
                                       _type.c_int,
                                       _type.c_int,
                                       _Pointer[_enum.PROPERTYORIGIN]],
                                      _type.HRESULT]
    GetThemeRect: _Callable[[_type.HTHEME,
                             _type.c_int,
                             _type.c_int,
                             _type.c_int,
                             _Pointer[_struct.RECT]],
                            _type.HRESULT]
    GetThemeString: _Callable[[_type.HTHEME,
                               _type.c_int,
                               _type.c_int,
                               _type.c_int,
                               _type.LPWSTR,
                               _type.c_int],
                              _type.HRESULT]
    GetThemeSysBool: _Callable[[_Optional[_type.HTHEME],
                                _type.c_int],
                               _type.BOOL]
    GetThemeSysColor: _Callable[[_Optional[_type.HTHEME],
                                 _type.c_int],
                                _type.COLORREF]
    GetThemeSysColorBrush: _Callable[[_Optional[_type.HTHEME],
                                      _type.c_int],
                                     _type.HBRUSH]
    GetThemeSysFont: _Callable[[_Optional[_type.HTHEME],
                                _type.c_int,
                                _Pointer[_struct.LOGFONTW]],
                               _type.HRESULT]
    GetThemeSysInt: _Callable[[_type.HTHEME,
                               _type.c_int,
                               _Pointer[_type.c_int]],
                              _type.HRESULT]
    GetThemeSysSize: _Callable[[_Optional[_type.HTHEME],
                                _type.c_int],
                               _type.c_int]
    GetThemeSysString: _Callable[[_type.HTHEME,
                                  _type.c_int,
                                  _type.LPWSTR,
                                  _type.c_int],
                                 _type.HRESULT]
    GetThemeTextExtent: _Callable[[_type.HTHEME,
                                   _type.HDC,
                                   _type.c_int,
                                   _type.c_int,
                                   _type.LPCWSTR,
                                   _type.c_int,
                                   _type.DWORD,
                                   _Optional[_Pointer[_struct.RECT]],
                                   _Pointer[_struct.RECT]],
                                  _type.HRESULT]
    GetThemeTextMetrics: _Callable[[_type.HTHEME,
                                    _type.HDC,
                                    _type.c_int,
                                    _type.c_int,
                                    _struct.TEXTMETRICW],
                                   _type.HRESULT]
    HitTestThemeBackground: _Callable[[_type.HTHEME,
                                       _Optional[_type.HDC],
                                       _type.c_int,
                                       _type.c_int,
                                       _type.DWORD,
                                       _Pointer[_struct.RECT],
                                       _Optional[_type.HRGN],
                                       _struct.POINT,
                                       _Pointer[_type.WORD]],
                                      _type.HRESULT]
    IsAppThemed: _Callable[[],
                           _type.BOOL]
    IsCompositionActive: _Callable[[],
                                   _type.BOOL]
    IsThemeActive: _Callable[[],
                             _type.BOOL]
    IsThemeBackgroundPartiallyTransparent: _Callable[[_type.HTHEME,
                                                      _type.c_int,
                                                      _type.c_int],
                                                     _type.BOOL]
    IsThemeDialogTextureEnabled: _Callable[[_type.HWND],
                                           _type.BOOL]
    IsThemePartDefined: _Callable[[_type.HTHEME,
                                   _type.c_int,
                                   _type.c_int],
                                  _type.BOOL]
    OpenThemeData: _Callable[[_Optional[_type.HWND],
                              _type.LPCWSTR],
                             _type.HTHEME]
    OpenThemeDataEx: _Callable[[_Optional[_type.HWND],
                                _type.LPCWSTR,
                                _type.DWORD],
                               _type.HTHEME]
    OpenThemeDataForDpi: _Callable[[_Optional[_type.HWND],
                                    _type.LPCWSTR,
                                    _type.UINT],
                                   _type.HTHEME]
    GetWindowTheme: _Callable[[_type.HWND],
                              _type.HTHEME]
    SetWindowThemeAttribute: _Callable[[_type.HWND,
                                        _enum.WINDOWTHEMEATTRIBUTETYPE,
                                        _type.PVOID,
                                        _type.DWORD],
                                       _type.HRESULT]
    SetThemeAppProperties: _Callable[[_type.DWORD],
                                     _type.c_void]
    SetWindowTheme: _Callable[[_type.HWND,
                               _Optional[_type.LPCWSTR],
                               _Optional[_type.LPCWSTR]],
                              _type.HRESULT]
    UpdatePanningFeedback: _Callable[[_type.HWND,
                                      _type.LONG,
                                      _type.LONG,
                                      _type.BOOL],
                                     _type.BOOL]


class Microsoft:
    class UI:
        class Xaml(_Func, metaclass=_WinDLL):
            DllGetActivationFactory: _Callable[[_type.HSTRING,
                                                _Pointer[_interface.IActivationFactory]],
                                               _type.HRESULT]

    class WindowsAppRuntime:
        class Bootstrap(_Func, metaclass=_WinDLL):
            MddBootstrapInitialize: _Callable[[_type.UINT32,
                                               _type.PCWSTR,
                                               _struct.PACKAGE_VERSION],
                                              _type.HRESULT]
            MddBootstrapShutdown: _Callable[[],
                                            _type.c_void]
