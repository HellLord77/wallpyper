from __future__ import annotations as _

from typing import Callable as _Callable

from . import _PyLib
from .. import type as _type
from .._utils import _Pointer

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

_PyLib(__name__)
