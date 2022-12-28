from __future__ import annotations as _

import ctypes as _ctypes
from typing import Any as _Any, Callable as _Callable, Optional as _Optional

from . import const as _const
from . import enum as _enum
from . import struct as _struct
from . import type as _type
from . import union as _union
from ._utils import _Pointer, _format_annotations, _func_doc, _resolve_type
from .interface.package import WebView2 as _WebView2
from .interface.shared import dxgi as _dxgi
from .interface.um import ShObjIdl_core as _ShObjIdl_core
from .interface.um import Unknwnbase as _Unknwnbase
from .interface.um import d2d1_1 as _d2d1_1
from .interface.um import d3d11 as _d3d11
from .interface.um import ddraw as _ddraw
from .interface.um import objidl as _objidl
from .interface.um import objidlbase as _objidlbase
from .interface.um import ocidl as _ocidl
from .interface.um import propsys as _propsys
from .interface.winrt import activation as _activation
from .interface.winrt import inspectable as _inspectable


class _CDLLMeta(type):
    _lib = None
    _errcheck = None

    def __new__(mcs, name: str, bases: tuple, dct: dict[str, _Any]):
        cls = super().__new__(mcs, name, bases, dct)
        cls._funcs = {}
        for func_name in cls.__annotations__:
            try:
                cls._funcs[func_name] = cls.__dict__[func_name]
            except KeyError:
                cls._funcs[func_name] = func_name
            else:
                delattr(cls, func_name)
        return cls

    def __getattr__(cls, func_name: str):
        if func_name in cls._funcs:
            func = None
            while func is None:
                try:
                    func = cls._lib[cls._funcs[func_name]]
                except KeyError:
                    raise AttributeError(f"Lib '{cls.__qualname__}' has no function '{func_name}'")
                except TypeError:
                    if cls._lib is None:
                        lib_name = cls.__qualname__
                        mode = _ctypes.DEFAULT_MODE
                        if isinstance(cls, _WinDLLMeta):
                            lib_name = f'{lib_name}.dll'
                            mode = _const.LOAD_LIBRARY_SEARCH_DEFAULT_DIRS
                        cls._lib = getattr(_ctypes, type(cls).__name__[1:-4])(lib_name, mode)
            annot = cls.__annotations__[func_name]
            func.restype, *func.argtypes = _resolve_type(eval(annot, globals()))
            if cls._errcheck is not None:
                func.errcheck = cls._errcheck
            func.__name__ = func_name
            func.__doc__ = _func_doc(func_name, func.restype, func.argtypes, _format_annotations(annot))
            setattr(cls, func_name, func)
            return func
        return super().__getattribute__(func_name)

    def __dir__(self):
        return *self.__dict__, *self._funcs


class _OleDLLMeta(_CDLLMeta):
    pass


class _WinDLLMeta(_CDLLMeta):
    pass


class _PyDLLMeta(_CDLLMeta):
    _lib = _ctypes.pythonapi


class _CDLL(metaclass=_CDLLMeta):
    pass


class _OleDLL(metaclass=_OleDLLMeta):
    pass


class _WinDLL(metaclass=_WinDLLMeta):
    pass


class _PyDLL(metaclass=_PyDLLMeta):
    pass


# noinspection PyPep8Naming
class msvcrt(_CDLL):
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
class libclang(_CDLL):
    # BuildSystem
    clang_getBuildSessionTimestamp: _Callable[[],
                                              _type.c_ulonglong]
    clang_VirtualFileOverlay_create: _Callable[[_type.c_uint],  # options
                                               _type.CXVirtualFileOverlay]
    clang_VirtualFileOverlay_addFileMapping: _Callable[[_type.CXVirtualFileOverlay,
                                                        _type.c_char_p,  # virtualPath
                                                        _type.c_char_p],  # realPath
                                                       _enum.CXErrorCode]
    clang_VirtualFileOverlay_setCaseSensitivity: _Callable[[_type.CXVirtualFileOverlay,
                                                            _type.c_int],  # caseSensitive
                                                           _enum.CXErrorCode]
    clang_VirtualFileOverlay_writeToBuffer: _Callable[[_type.CXVirtualFileOverlay,
                                                       _type.c_uint,  # options
                                                       _Pointer[_type.c_char_p],  # out_buffer_ptr
                                                       _Pointer[_type.c_uint]],  # out_buffer_size
                                                      _enum.CXErrorCode]
    clang_free: _Callable[[_type.c_void_p],  # buffer
                          _type.c_void]
    clang_VirtualFileOverlay_dispose: _Callable[[_type.CXVirtualFileOverlay],
                                                _type.c_void]
    clang_ModuleMapDescriptor_create: _Callable[[_type.c_uint],  # options
                                                _type.CXModuleMapDescriptor]
    clang_ModuleMapDescriptor_setFrameworkModuleName: _Callable[[_type.CXModuleMapDescriptor,
                                                                 _type.c_char_p],  # name
                                                                _enum.CXErrorCode]
    clang_ModuleMapDescriptor_setUmbrellaHeader: _Callable[[_type.CXModuleMapDescriptor,
                                                            _type.c_char_p],  # name
                                                           _enum.CXErrorCode]
    clang_ModuleMapDescriptor_writeToBuffer: _Callable[[_type.CXModuleMapDescriptor,
                                                        _type.c_uint,  # options
                                                        _Pointer[_type.c_char_p],  # out_buffer_ptr
                                                        _Pointer[_type.c_uint]],  # out_buffer_size
                                                       _enum.CXErrorCode]
    clang_ModuleMapDescriptor_dispose: _Callable[[_type.CXModuleMapDescriptor],
                                                 _type.c_void]
    # CXCompilationDatabase
    clang_CompilationDatabase_fromDirectory: _Callable[[_type.c_char_p,  # BuildDir
                                                        _Pointer[_enum.CXCompilationDatabase_Error]],  # ErrorCode
                                                       _type.CXCompilationDatabase]
    clang_CompilationDatabase_dispose: _Callable[[_type.CXCompilationDatabase],
                                                 _type.c_void]
    clang_CompilationDatabase_getCompileCommands: _Callable[[_type.CXCompilationDatabase,
                                                             _type.c_char_p],  # CompleteFileName
                                                            _type.CXCompileCommands]
    clang_CompilationDatabase_getAllCompileCommands: _Callable[[_type.CXCompilationDatabase],
                                                               _type.CXCompileCommands]
    clang_CompileCommands_dispose: _Callable[[_type.CXCompileCommands],
                                             _type.c_void]
    clang_CompileCommands_getSize: _Callable[[_type.CXCompileCommands],
                                             _type.c_uint]
    clang_CompileCommands_getCommand: _Callable[[_type.CXCompileCommands,
                                                 _type.c_uint],  # I
                                                _type.CXCompileCommand]
    clang_CompileCommand_getDirectory: _Callable[[_type.CXCompileCommand],
                                                 _struct.CXString]
    clang_CompileCommand_getFilename: _Callable[[_type.CXCompileCommand],
                                                _struct.CXString]
    clang_CompileCommand_getNumArgs: _Callable[[_type.CXCompileCommand],
                                               _type.c_uint]
    clang_CompileCommand_getArg: _Callable[[_type.CXCompileCommand,
                                            _type.c_uint],  # I
                                           _struct.CXString]
    clang_CompileCommand_getNumMappedSources: _Callable[[_type.CXCompileCommand],
                                                        _type.c_uint]
    clang_CompileCommand_getMappedSourcePath: _Callable[[_type.CXCompileCommand,
                                                         _type.c_uint],  # I
                                                        _struct.CXString]
    clang_CompileCommand_getMappedSourceContent: _Callable[[_type.CXCompileCommand,
                                                            _type.c_uint],  # I
                                                           _struct.CXString]
    # CXString
    clang_getCString: _Callable[[_struct.CXString],  # string
                                _type.c_char_p]
    clang_disposeString: _Callable[[_struct.CXString],  # string
                                   _type.c_void]
    clang_disposeStringSet: _Callable[[_Pointer[_struct.CXStringSet]],  # set
                                      _type.c_void]
    # Documentation
    clang_Cursor_getParsedComment: _Callable[[_struct.CXCursor],  # C
                                             _struct.CXComment]
    clang_Comment_getKind: _Callable[[_struct.CXComment],  # Comment
                                     _enum.CXCommentKind]
    clang_Comment_getNumChildren: _Callable[[_struct.CXComment],  # Comment
                                            _type.c_uint]
    clang_Comment_getChild: _Callable[[_struct.CXComment,  # Comment
                                       _type.c_uint],  # ChildIdx
                                      _struct.CXComment]
    clang_Comment_isWhitespace: _Callable[[_struct.CXComment],  # Comment
                                          _type.c_uint]
    clang_InlineContentComment_hasTrailingNewline: _Callable[[_struct.CXComment],  # Comment
                                                             _type.c_uint]
    clang_TextComment_getText: _Callable[[_struct.CXComment],  # Comment
                                         _struct.CXString]
    clang_InlineCommandComment_getCommandName: _Callable[[_struct.CXComment],  # Comment
                                                         _struct.CXString]
    clang_InlineCommandComment_getRenderKind: _Callable[[_struct.CXComment],  # Comment
                                                        _enum.CXCommentInlineCommandRenderKind]
    clang_InlineCommandComment_getNumArgs: _Callable[[_struct.CXComment],  # Comment
                                                     _type.c_uint]
    clang_InlineCommandComment_getArgText: _Callable[[_struct.CXComment,  # Comment
                                                      _type.c_uint],  # ArgIdx
                                                     _struct.CXString]
    clang_HTMLTagComment_getTagName: _Callable[[_struct.CXComment],  # Comment
                                               _struct.CXString]
    clang_HTMLStartTagComment_isSelfClosing: _Callable[[_struct.CXComment],  # Comment
                                                       _type.c_uint]
    clang_HTMLStartTag_getNumAttrs: _Callable[[_struct.CXComment],  # Comment
                                              _type.c_uint]
    clang_HTMLStartTag_getAttrName: _Callable[[_struct.CXComment,  # Comment
                                               _type.c_uint],  # AttrIdx
                                              _struct.CXString]
    clang_HTMLStartTag_getAttrValue: _Callable[[_struct.CXComment,  # Comment
                                                _type.c_uint],  # AttrIdx
                                               _struct.CXString]
    clang_BlockCommandComment_getCommandName: _Callable[[_struct.CXComment],  # Comment
                                                        _struct.CXString]
    clang_BlockCommandComment_getNumArgs: _Callable[[_struct.CXComment],  # Comment
                                                    _type.c_uint]
    clang_BlockCommandComment_getArgText: _Callable[[_struct.CXComment,  # Comment
                                                     _type.c_uint],  # ArgIdx
                                                    _struct.CXString]
    clang_BlockCommandComment_getParagraph: _Callable[[_struct.CXComment],  # Comment
                                                      _struct.CXComment]
    clang_ParamCommandComment_getParamName: _Callable[[_struct.CXComment],  # Comment
                                                      _struct.CXString]
    clang_ParamCommandComment_isParamIndexValid: _Callable[[_struct.CXComment],  # Comment
                                                           _type.c_uint]
    clang_ParamCommandComment_getParamIndex: _Callable[[_struct.CXComment],  # Comment
                                                       _type.c_uint]
    clang_ParamCommandComment_isDirectionExplicit: _Callable[[_struct.CXComment],  # Comment
                                                             _type.c_uint]
    clang_ParamCommandComment_getDirection: _Callable[[_struct.CXComment],  # Comment
                                                      _enum.CXCommentParamPassDirection]
    clang_TParamCommandComment_getParamName: _Callable[[_struct.CXComment],  # Comment
                                                       _struct.CXString]
    clang_TParamCommandComment_isParamPositionValid: _Callable[[_struct.CXComment],  # Comment
                                                               _type.c_uint]
    clang_TParamCommandComment_getDepth: _Callable[[_struct.CXComment],  # Comment
                                                   _type.c_uint]
    clang_TParamCommandComment_getIndex: _Callable[[_struct.CXComment,  # Comment
                                                    _type.c_uint],  # Depth
                                                   _type.c_uint]
    clang_VerbatimBlockLineComment_getText: _Callable[[_struct.CXComment],  # Comment
                                                      _struct.CXString]
    clang_VerbatimLineComment_getText: _Callable[[_struct.CXComment],  # Comment
                                                 _struct.CXString]
    clang_HTMLTagComment_getAsString: _Callable[[_struct.CXComment],  # Comment
                                                _struct.CXString]
    clang_FullComment_getAsHTML: _Callable[[_struct.CXComment],  # Comment
                                           _struct.CXString]
    clang_FullComment_getAsXML: _Callable[[_struct.CXComment],  # Comment
                                          _struct.CXString]
    # FatalErrorHandler
    clang_install_aborting_llvm_fatal_error_handler: _Callable[[],
                                                               _type.c_void]
    clang_uninstall_llvm_fatal_error_handler: _Callable[[],
                                                        _type.c_void]
    # Index
    clang_createIndex: _Callable[[_type.c_int,  # excludeDeclarationsFromPCH
                                  _type.c_int],  # displayDiagnostics
                                 _type.CXIndex]
    clang_disposeIndex: _Callable[[_type.CXIndex],  # index
                                  _type.c_void]
    clang_CXIndex_setGlobalOptions: _Callable[[_type.CXIndex,
                                               _type.c_uint],  # options
                                              _type.c_void]
    clang_CXIndex_getGlobalOptions: _Callable[[_type.CXIndex],
                                              _type.c_uint]
    clang_CXIndex_setInvocationEmissionPathOption: _Callable[[_type.CXIndex,
                                                              _type.c_char_p],  # Path
                                                             _type.c_void]
    clang_getFileName: _Callable[[_type.CXFile],  # SFile
                                 _struct.CXString]
    clang_getFileTime: _Callable[[_type.CXFile],  # SFile
                                 _type.time_t]
    clang_getFileUniqueID: _Callable[[_type.CXFile,  # file
                                      _Pointer[_struct.CXFileUniqueID]],  # outID
                                     _type.c_int]
    clang_isFileMultipleIncludeGuarded: _Callable[[_type.CXTranslationUnit,  # tu
                                                   _type.CXFile],  # file
                                                  _type.c_uint]
    clang_getFile: _Callable[[_type.CXTranslationUnit,  # tu
                              _type.c_char_p],  # file_name
                             _type.CXFile]
    clang_getFileContents: _Callable[[_type.CXTranslationUnit,  # tu
                                      _type.CXFile,  # file
                                      _Pointer[_type.c_size_t]],  # size
                                     _type.c_char_p]
    clang_File_isEqual: _Callable[[_type.CXFile,  # file1
                                   _type.CXFile],  # file2
                                  _type.c_int]
    clang_File_tryGetRealPathName: _Callable[[_type.CXFile],  # file
                                             _struct.CXString]
    clang_getNullLocation: _Callable[[],
                                     _struct.CXSourceLocation]
    clang_equalLocations: _Callable[[_struct.CXSourceLocation,  # loc1
                                     _struct.CXSourceLocation],  # loc2
                                    _type.c_uint]
    clang_getLocation: _Callable[[_type.CXTranslationUnit,  # tu
                                  _type.CXFile,  # file
                                  _type.c_uint,  # line
                                  _type.c_uint],  # column
                                 _struct.CXSourceLocation]
    clang_getLocationForOffset: _Callable[[_type.CXTranslationUnit,  # tu
                                           _type.CXFile,  # file
                                           _type.c_uint],  # offset
                                          _struct.CXSourceLocation]
    clang_Location_isInSystemHeader: _Callable[[_struct.CXSourceLocation],  # location
                                               _type.c_int]
    clang_Location_isFromMainFile: _Callable[[_struct.CXSourceLocation],  # location
                                             _type.c_int]
    clang_getNullRange: _Callable[[],
                                  _struct.CXSourceRange]
    clang_getRange: _Callable[[_struct.CXSourceLocation,  # begin
                               _struct.CXSourceLocation],  # end
                              _struct.CXSourceRange]
    clang_equalRanges: _Callable[[_struct.CXSourceRange,  # range1
                                  _struct.CXSourceRange],  # range2
                                 _type.c_uint]
    clang_Range_isNull: _Callable[[_struct.CXSourceRange],  # range
                                  _type.c_int]
    clang_getExpansionLocation: _Callable[[_struct.CXSourceLocation,  # location
                                           _Pointer[_type.CXFile],  # file
                                           _Pointer[_type.c_uint],  # line
                                           _Pointer[_type.c_uint],  # column
                                           _Pointer[_type.c_uint]],  # offset
                                          _type.c_void]
    clang_getPresumedLocation: _Callable[[_struct.CXSourceLocation,  # location
                                          _Pointer[_struct.CXString],  # filename
                                          _Pointer[_type.c_uint],  # line
                                          _Pointer[_type.c_uint]],  # column
                                         _type.c_void]
    clang_getInstantiationLocation: _Callable[[_struct.CXSourceLocation,  # location
                                               _Pointer[_type.CXFile],  # file
                                               _Pointer[_type.c_uint],  # line
                                               _Pointer[_type.c_uint],  # column
                                               _Pointer[_type.c_uint]],  # offset
                                              _type.c_void]
    clang_getSpellingLocation: _Callable[[_struct.CXSourceLocation,  # location
                                          _Pointer[_type.CXFile],  # file
                                          _Pointer[_type.c_uint],  # line
                                          _Pointer[_type.c_uint],  # column
                                          _Pointer[_type.c_uint]],  # offset
                                         _type.c_void]
    clang_getFileLocation: _Callable[[_struct.CXSourceLocation,  # location
                                      _Pointer[_type.CXFile],  # file
                                      _Pointer[_type.c_uint],  # line
                                      _Pointer[_type.c_uint],  # column
                                      _Pointer[_type.c_uint]],  # offset
                                     _type.c_void]
    clang_getRangeStart: _Callable[[_struct.CXSourceRange],  # range
                                   _struct.CXSourceLocation]
    clang_getRangeEnd: _Callable[[_struct.CXSourceRange],  # range
                                 _struct.CXSourceLocation]
    clang_getSkippedRanges: _Callable[[_type.CXTranslationUnit,  # tu
                                       _type.CXFile],  # file
                                      _Pointer[_struct.CXSourceRangeList]]
    clang_getAllSkippedRanges: _Callable[[_type.CXTranslationUnit],  # tu
                                         _Pointer[_struct.CXSourceRangeList]]
    clang_disposeSourceRangeList: _Callable[[_Pointer[_struct.CXSourceRangeList]],  # ranges
                                            _type.c_void]
    clang_getNumDiagnosticsInSet: _Callable[[_type.CXDiagnosticSet],  # Diags
                                            _type.c_uint]
    clang_getDiagnosticInSet: _Callable[[_type.CXDiagnosticSet,  # Diags
                                         _type.c_uint],  # Index
                                        _type.CXDiagnostic]
    clang_loadDiagnostics: _Callable[[_type.c_char_p,  # file
                                      _Pointer[_enum.CXLoadDiag_Error],  # error
                                      _Pointer[_struct.CXString]],  # errorString
                                     _type.CXDiagnosticSet]
    clang_disposeDiagnosticSet: _Callable[[_type.CXDiagnosticSet],  # Diags
                                          _type.c_void]
    clang_getChildDiagnostics: _Callable[[_type.CXDiagnostic],  # D
                                         _type.CXDiagnosticSet]
    clang_getNumDiagnostics: _Callable[[_type.CXTranslationUnit],  # Unit
                                       _type.c_uint]
    clang_getDiagnostic: _Callable[[_type.CXTranslationUnit,  # Unit
                                    _type.c_uint],  # Index
                                   _type.CXDiagnostic]
    clang_getDiagnosticSetFromTU: _Callable[[_type.CXTranslationUnit],  # Unit
                                            _type.CXDiagnosticSet]
    clang_disposeDiagnostic: _Callable[[_type.CXDiagnostic],  # Diagnostic
                                       _type.c_void]
    clang_formatDiagnostic: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                       _type.c_uint],  # Options
                                      _struct.CXString]
    clang_defaultDiagnosticDisplayOptions: _Callable[[],
                                                     _type.c_uint]
    clang_getDiagnosticSeverity: _Callable[[_type.CXDiagnostic],
                                           _enum.CXDiagnosticSeverity]
    clang_getDiagnosticLocation: _Callable[[_type.CXDiagnostic],
                                           _struct.CXSourceLocation]
    clang_getDiagnosticSpelling: _Callable[[_type.CXDiagnostic],
                                           _struct.CXString]
    clang_getDiagnosticOption: _Callable[[_type.CXDiagnostic,  # Diag
                                          _Pointer[_struct.CXString]],  # Disable
                                         _struct.CXString]
    clang_getDiagnosticCategory: _Callable[[_type.CXDiagnostic],
                                           _type.c_uint]
    clang_getDiagnosticCategoryName: _Callable[[_type.c_uint],  # Category
                                               _struct.CXString]
    clang_getDiagnosticCategoryText: _Callable[[_type.CXDiagnostic],
                                               _struct.CXString]
    clang_getDiagnosticNumRanges: _Callable[[_type.CXDiagnostic],
                                            _type.c_uint]
    clang_getDiagnosticRange: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                         _type.c_uint],  # Range
                                        _struct.CXSourceRange]
    clang_getDiagnosticNumFixIts: _Callable[[_type.CXDiagnostic],  # Diagnostic
                                            _type.c_uint]
    clang_getDiagnosticFixIt: _Callable[[_type.CXDiagnostic,  # Diagnostic
                                         _type.c_uint,  # FixIt
                                         _Pointer[_struct.CXSourceRange]],  # ReplacementRange
                                        _struct.CXString]
    clang_getTranslationUnitSpelling: _Callable[[_type.CXTranslationUnit],  # CTUnit
                                                _struct.CXString]
    clang_createTranslationUnitFromSourceFile: _Callable[[_type.CXIndex,  # CIdx
                                                          _type.c_char_p,  # source_filename
                                                          _type.c_int,  # num_clang_command_line_args
                                                          _Pointer[_type.c_char_p],  # clang_command_line_args
                                                          _type.c_uint,  # num_unsaved_files
                                                          _Pointer[_struct.CXUnsavedFile]],  # unsaved_files
                                                         _type.CXTranslationUnit]
    clang_createTranslationUnit: _Callable[[_type.CXIndex,  # CIdx
                                            _type.c_char_p],  # ast_filename
                                           _type.CXTranslationUnit]
    clang_createTranslationUnit2: _Callable[[_type.CXIndex,  # CIdx
                                             _type.c_char_p,  # ast_filename
                                             _Pointer[_type.CXTranslationUnit]],  # out_TU
                                            _enum.CXErrorCode]
    clang_defaultEditingTranslationUnitOptions: _Callable[[],
                                                          _type.c_uint]
    clang_parseTranslationUnit: _Callable[[_type.CXIndex,  # CIdx
                                           _type.c_char_p,  # source_filename
                                           _Pointer[_type.c_char_p],  # command_line_args
                                           _type.c_int,  # num_command_line_args
                                           _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                           _type.c_uint,  # num_unsaved_files
                                           _type.c_uint],  # options
                                          _type.CXTranslationUnit]
    clang_parseTranslationUnit2: _Callable[[_type.CXIndex,  # CIdx
                                            _type.c_char_p,  # source_filename
                                            _Pointer[_type.c_char_p],  # command_line_args
                                            _type.c_int,  # num_command_line_args
                                            _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                            _type.c_uint,  # num_unsaved_files
                                            _type.c_uint,  # options
                                            _Pointer[_type.CXTranslationUnit]],  # out_TU
                                           _enum.CXErrorCode]
    clang_parseTranslationUnit2FullArgv: _Callable[[_type.CXIndex,  # CIdx
                                                    _type.c_char_p,  # source_filename
                                                    _Pointer[_type.c_char_p],  # command_line_args
                                                    _type.c_int,  # num_command_line_args
                                                    _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                                    _type.c_uint,  # num_unsaved_files
                                                    _type.c_uint,  # options
                                                    _Pointer[_type.CXTranslationUnit]],  # out_TU
                                                   _enum.CXErrorCode]
    clang_defaultSaveOptions: _Callable[[_type.CXTranslationUnit],  # TU
                                        _type.c_uint]
    clang_saveTranslationUnit: _Callable[[_type.CXTranslationUnit,  # TU
                                          _type.c_char_p,  # FileName
                                          _type.c_uint],  # options
                                         _type.c_int]
    clang_suspendTranslationUnit: _Callable[[_type.CXTranslationUnit],
                                            _type.c_uint]
    clang_disposeTranslationUnit: _Callable[[_type.CXTranslationUnit],
                                            _type.c_void]
    clang_defaultReparseOptions: _Callable[[_type.CXTranslationUnit],  # TU
                                           _type.c_uint]
    clang_reparseTranslationUnit: _Callable[[_type.CXTranslationUnit,  # TU
                                             _type.c_uint,  # num_unsaved_files
                                             _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                             _type.c_uint],  # options
                                            _type.c_int]
    clang_getTUResourceUsageName: _Callable[[_enum.CXTUResourceUsageKind],  # kind
                                            _type.c_char_p]
    clang_getCXTUResourceUsage: _Callable[[_type.CXTranslationUnit],  # TU
                                          _struct.CXTUResourceUsage]
    clang_disposeCXTUResourceUsage: _Callable[[_struct.CXTUResourceUsage],  # usage
                                              _type.c_void]
    clang_getTranslationUnitTargetInfo: _Callable[[_type.CXTranslationUnit],  # CTUnit
                                                  _type.CXTargetInfo]
    clang_TargetInfo_dispose: _Callable[[_type.CXTargetInfo],  # Info
                                        _type.c_void]
    clang_TargetInfo_getTriple: _Callable[[_type.CXTargetInfo],  # Info
                                          _struct.CXString]
    clang_TargetInfo_getPointerWidth: _Callable[[_type.CXTargetInfo],  # Info
                                                _type.c_int]
    clang_getNullCursor: _Callable[[],
                                   _struct.CXCursor]
    clang_getTranslationUnitCursor: _Callable[[_type.CXTranslationUnit],
                                              _struct.CXCursor]
    clang_equalCursors: _Callable[[_struct.CXCursor,
                                   _struct.CXCursor],
                                  _type.c_uint]
    clang_Cursor_isNull: _Callable[[_struct.CXCursor],  # cursor
                                   _type.c_int]
    clang_hashCursor: _Callable[[_struct.CXCursor],
                                _type.c_uint]
    clang_getCursorKind: _Callable[[_struct.CXCursor],
                                   _enum.CXCursorKind]
    clang_isDeclaration: _Callable[[_enum.CXCursorKind],
                                   _type.c_uint]
    clang_isInvalidDeclaration: _Callable[[_struct.CXCursor],
                                          _type.c_uint]
    clang_isReference: _Callable[[_enum.CXCursorKind],
                                 _type.c_uint]
    clang_isExpression: _Callable[[_enum.CXCursorKind],
                                  _type.c_uint]
    clang_isStatement: _Callable[[_enum.CXCursorKind],
                                 _type.c_uint]
    clang_isAttribute: _Callable[[_enum.CXCursorKind],
                                 _type.c_uint]
    clang_Cursor_hasAttrs: _Callable[[_struct.CXCursor],  # C
                                     _type.c_uint]
    clang_isInvalid: _Callable[[_enum.CXCursorKind],
                               _type.c_uint]
    clang_isTranslationUnit: _Callable[[_enum.CXCursorKind],
                                       _type.c_uint]
    clang_isPreprocessing: _Callable[[_enum.CXCursorKind],
                                     _type.c_uint]
    clang_isUnexposed: _Callable[[_enum.CXCursorKind],
                                 _type.c_uint]
    clang_getCursorLinkage: _Callable[[_struct.CXCursor],  # cursor
                                      _enum.CXLinkageKind]
    clang_getCursorVisibility: _Callable[[_struct.CXCursor],  # cursor
                                         _enum.CXVisibilityKind]
    clang_getCursorAvailability: _Callable[[_struct.CXCursor],  # cursor
                                           _enum.CXAvailabilityKind]
    clang_getCursorPlatformAvailability: _Callable[[_struct.CXCursor,  # cursor
                                                    _Pointer[_type.c_int],  # always_deprecated
                                                    _Pointer[_struct.CXString],  # deprecated_message
                                                    _Pointer[_type.c_int],  # always_unavailable
                                                    _Pointer[_struct.CXString],  # unavailable_message
                                                    _Pointer[_struct.CXPlatformAvailability],  # availability
                                                    _type.c_int],  # availability_size
                                                   _type.c_int]
    clang_disposeCXPlatformAvailability: _Callable[[_Pointer[_struct.CXPlatformAvailability]],  # availability
                                                   _type.c_void]
    clang_Cursor_getVarDeclInitializer: _Callable[[_struct.CXCursor],  # cursor
                                                  _struct.CXCursor]
    clang_Cursor_hasVarDeclGlobalStorage: _Callable[[_struct.CXCursor],  # cursor
                                                    _type.c_int]
    clang_Cursor_hasVarDeclExternalStorage: _Callable[[_struct.CXCursor],  # cursor
                                                      _type.c_int]
    clang_getCursorLanguage: _Callable[[_struct.CXCursor],  # cursor
                                       _enum.CXLanguageKind]
    clang_getCursorTLSKind: _Callable[[_struct.CXCursor],  # cursor
                                      _enum.CXTLSKind]
    clang_Cursor_getTranslationUnit: _Callable[[_struct.CXCursor],
                                               _type.CXTranslationUnit]
    clang_createCXCursorSet: _Callable[[],
                                       _type.CXCursorSet]
    clang_disposeCXCursorSet: _Callable[[_type.CXCursorSet],  # cset
                                        _type.c_void]
    clang_CXCursorSet_contains: _Callable[[_type.CXCursorSet,  # cset
                                           _struct.CXCursor],  # cursor
                                          _type.c_uint]
    clang_CXCursorSet_insert: _Callable[[_type.CXCursorSet,  # cset
                                         _struct.CXCursor],  # cursor
                                        _type.c_uint]
    clang_getCursorSemanticParent: _Callable[[_struct.CXCursor],  # cursor
                                             _struct.CXCursor]
    clang_getCursorLexicalParent: _Callable[[_struct.CXCursor],  # cursor
                                            _struct.CXCursor]
    clang_getOverriddenCursors: _Callable[[_struct.CXCursor,  # cursor
                                           _Pointer[_Pointer[_struct.CXCursor]],  # overridden
                                           _Pointer[_type.c_uint]],  # num_overridden
                                          _type.c_void]
    clang_disposeOverriddenCursors: _Callable[[_Pointer[_struct.CXCursor]],  # overridden
                                              _type.c_void]
    clang_getIncludedFile: _Callable[[_struct.CXCursor],  # cursor
                                     _type.CXFile]
    clang_getCursor: _Callable[[_type.CXTranslationUnit,
                                _struct.CXSourceLocation],
                               _struct.CXCursor]
    clang_getCursorLocation: _Callable[[_struct.CXCursor],
                                       _struct.CXSourceLocation]
    clang_getCursorExtent: _Callable[[_struct.CXCursor],
                                     _struct.CXSourceRange]
    clang_getCursorType: _Callable[[_struct.CXCursor],  # C
                                   _struct.CXType]
    clang_getTypeSpelling: _Callable[[_struct.CXType],  # CT
                                     _struct.CXString]
    clang_getTypedefDeclUnderlyingType: _Callable[[_struct.CXCursor],  # C
                                                  _struct.CXType]
    clang_getEnumDeclIntegerType: _Callable[[_struct.CXCursor],  # C
                                            _struct.CXType]
    clang_getEnumConstantDeclValue: _Callable[[_struct.CXCursor],  # C
                                              _type.c_longlong]
    clang_getEnumConstantDeclUnsignedValue: _Callable[[_struct.CXCursor],  # C
                                                      _type.c_ulonglong]
    clang_getFieldDeclBitWidth: _Callable[[_struct.CXCursor],  # C
                                          _type.c_int]
    clang_Cursor_getNumArguments: _Callable[[_struct.CXCursor],  # C
                                            _type.c_int]
    clang_Cursor_getArgument: _Callable[[_struct.CXCursor,  # C
                                         _type.c_uint],  # i
                                        _struct.CXCursor]
    clang_Cursor_getNumTemplateArguments: _Callable[[_struct.CXCursor],  # C
                                                    _type.c_int]
    clang_Cursor_getTemplateArgumentKind: _Callable[[_struct.CXCursor,  # C
                                                     _type.c_uint],  # I
                                                    _enum.CXTemplateArgumentKind]
    clang_Cursor_getTemplateArgumentType: _Callable[[_struct.CXCursor,  # C
                                                     _type.c_uint],  # I
                                                    _struct.CXType]
    clang_Cursor_getTemplateArgumentValue: _Callable[[_struct.CXCursor,  # C
                                                      _type.c_uint],  # I
                                                     _type.c_longlong]
    clang_Cursor_getTemplateArgumentUnsignedValue: _Callable[[_struct.CXCursor,  # C
                                                              _type.c_uint],  # I
                                                             _type.c_ulonglong]
    clang_equalTypes: _Callable[[_struct.CXType,  # A
                                 _struct.CXType],  # B
                                _type.c_uint]
    clang_getCanonicalType: _Callable[[_struct.CXType],  # T
                                      _struct.CXType]
    clang_isConstQualifiedType: _Callable[[_struct.CXType],  # T
                                          _type.c_uint]
    clang_Cursor_isMacroFunctionLike: _Callable[[_struct.CXCursor],  # C
                                                _type.c_uint]
    clang_Cursor_isMacroBuiltin: _Callable[[_struct.CXCursor],  # C
                                           _type.c_uint]
    clang_Cursor_isFunctionInlined: _Callable[[_struct.CXCursor],  # C
                                              _type.c_uint]
    clang_isVolatileQualifiedType: _Callable[[_struct.CXType],  # T
                                             _type.c_uint]
    clang_isRestrictQualifiedType: _Callable[[_struct.CXType],  # T
                                             _type.c_uint]
    clang_getAddressSpace: _Callable[[_struct.CXType],  # T
                                     _type.c_uint]
    clang_getTypedefName: _Callable[[_struct.CXType],  # CT
                                    _struct.CXString]
    clang_getPointeeType: _Callable[[_struct.CXType],  # T
                                    _struct.CXType]
    clang_getTypeDeclaration: _Callable[[_struct.CXType],  # T
                                        _struct.CXCursor]
    clang_getDeclObjCTypeEncoding: _Callable[[_struct.CXCursor],  # C
                                             _struct.CXString]
    clang_Type_getObjCEncoding: _Callable[[_struct.CXType],  # type
                                          _struct.CXString]
    clang_getTypeKindSpelling: _Callable[[_enum.CXTypeKind],  # K
                                         _struct.CXString]
    clang_getFunctionTypeCallingConv: _Callable[[_struct.CXType],  # T
                                                _enum.CXCallingConv]
    clang_getResultType: _Callable[[_struct.CXType],  # T
                                   _struct.CXType]
    clang_getExceptionSpecificationType: _Callable[[_struct.CXType],  # T
                                                   _type.c_int]
    clang_getNumArgTypes: _Callable[[_struct.CXType],  # T
                                    _type.c_int]
    clang_getArgType: _Callable[[_struct.CXType,  # T
                                 _type.c_uint],  # i
                                _struct.CXType]
    clang_Type_getObjCObjectBaseType: _Callable[[_struct.CXType],  # T
                                                _struct.CXType]
    clang_Type_getNumObjCProtocolRefs: _Callable[[_struct.CXType],  # T
                                                 _type.c_uint]
    clang_Type_getObjCProtocolDecl: _Callable[[_struct.CXType,  # T
                                               _type.c_uint],  # i
                                              _struct.CXCursor]
    clang_Type_getNumObjCTypeArgs: _Callable[[_struct.CXType],  # T
                                             _type.c_uint]
    clang_Type_getObjCTypeArg: _Callable[[_struct.CXType,  # T
                                          _type.c_uint],  # i
                                         _struct.CXType]
    clang_isFunctionTypeVariadic: _Callable[[_struct.CXType],  # T
                                            _type.c_uint]
    clang_getCursorResultType: _Callable[[_struct.CXCursor],  # C
                                         _struct.CXType]
    clang_getCursorExceptionSpecificationType: _Callable[[_struct.CXCursor],  # C
                                                         _type.c_int]
    clang_isPODType: _Callable[[_struct.CXType],  # T
                               _type.c_uint]
    clang_getElementType: _Callable[[_struct.CXType],  # T
                                    _struct.CXType]
    clang_getNumElements: _Callable[[_struct.CXType],  # T
                                    _type.c_longlong]
    clang_getArrayElementType: _Callable[[_struct.CXType],  # T
                                         _struct.CXType]
    clang_getArraySize: _Callable[[_struct.CXType],  # T
                                  _type.c_longlong]
    clang_Type_getNamedType: _Callable[[_struct.CXType],  # T
                                       _struct.CXType]
    clang_Type_isTransparentTagTypedef: _Callable[[_struct.CXType],  # T
                                                  _type.c_uint]
    clang_Type_getNullability: _Callable[[_struct.CXType],  # T
                                         _enum.CXTypeNullabilityKind]
    clang_Type_getAlignOf: _Callable[[_struct.CXType],  # T
                                     _type.c_longlong]
    clang_Type_getClassType: _Callable[[_struct.CXType],  # T
                                       _struct.CXType]
    clang_Type_getSizeOf: _Callable[[_struct.CXType],  # T
                                    _type.c_longlong]
    clang_Type_getOffsetOf: _Callable[[_struct.CXType,  # T
                                       _type.c_char_p],  # S
                                      _type.c_longlong]
    clang_Type_getModifiedType: _Callable[[_struct.CXType],  # T
                                          _struct.CXType]
    clang_Type_getValueType: _Callable[[_struct.CXType],  # CT
                                       _struct.CXType]
    clang_Cursor_getOffsetOfField: _Callable[[_struct.CXCursor],  # C
                                             _type.c_longlong]
    clang_Cursor_isAnonymous: _Callable[[_struct.CXCursor],  # C
                                        _type.c_uint]
    clang_Cursor_isAnonymousRecordDecl: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_uint]
    clang_Cursor_isInlineNamespace: _Callable[[_struct.CXCursor],  # C
                                              _type.c_uint]
    clang_Type_getNumTemplateArguments: _Callable[[_struct.CXType],  # T
                                                  _type.c_int]
    clang_Type_getTemplateArgumentAsType: _Callable[[_struct.CXType,  # T
                                                     _type.c_uint],  # i
                                                    _struct.CXType]
    clang_Type_getCXXRefQualifier: _Callable[[_struct.CXType],  # T
                                             _enum.CXRefQualifierKind]
    clang_Cursor_isBitField: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
    clang_isVirtualBase: _Callable[[_struct.CXCursor],
                                   _type.c_uint]
    clang_getCXXAccessSpecifier: _Callable[[_struct.CXCursor],
                                           _enum.CX_CXXAccessSpecifier]
    clang_Cursor_getStorageClass: _Callable[[_struct.CXCursor],
                                            _enum.CX_StorageClass]
    clang_getNumOverloadedDecls: _Callable[[_struct.CXCursor],  # cursor
                                           _type.c_uint]
    clang_getOverloadedDecl: _Callable[[_struct.CXCursor,  # cursor
                                        _type.c_uint],  # index
                                       _struct.CXCursor]
    clang_getIBOutletCollectionType: _Callable[[_struct.CXCursor],
                                               _struct.CXType]
    clang_visitChildren: _Callable[[_struct.CXCursor,  # parent
                                    _type.CXCursorVisitor,  # visitor
                                    _type.CXClientData],  # client_data
                                   _type.c_uint]
    clang_getCursorUSR: _Callable[[_struct.CXCursor],
                                  _struct.CXString]
    clang_constructUSR_ObjCClass: _Callable[[_type.c_char_p],  # class_name
                                            _struct.CXString]
    clang_constructUSR_ObjCCategory: _Callable[[_type.c_char_p,  # class_name
                                                _type.c_char_p],  # category_name
                                               _struct.CXString]
    clang_constructUSR_ObjCProtocol: _Callable[[_type.c_char_p],  # protocol_name
                                               _struct.CXString]
    clang_constructUSR_ObjCIvar: _Callable[[_type.c_char_p,  # name
                                            _struct.CXString],  # classUSR
                                           _struct.CXString]
    clang_constructUSR_ObjCMethod: _Callable[[_type.c_char_p,  # name
                                              _type.c_uint,  # isInstanceMethod
                                              _struct.CXString],  # classUSR
                                             _struct.CXString]
    clang_constructUSR_ObjCProperty: _Callable[[_type.c_char_p,  # property
                                                _struct.CXString],  # classUSR
                                               _struct.CXString]
    clang_getCursorSpelling: _Callable[[_struct.CXCursor],
                                       _struct.CXString]
    clang_Cursor_getSpellingNameRange: _Callable[[_struct.CXCursor,
                                                  _type.c_uint,  # pieceIndex
                                                  _type.c_uint],  # options
                                                 _struct.CXSourceRange]
    clang_PrintingPolicy_getProperty: _Callable[[_type.CXPrintingPolicy,  # Policy
                                                 _enum.CXPrintingPolicyProperty],  # Property
                                                _type.c_uint]
    clang_PrintingPolicy_setProperty: _Callable[[_type.CXPrintingPolicy,  # Policy
                                                 _enum.CXPrintingPolicyProperty,  # Property
                                                 _type.c_uint],  # Value
                                                _type.c_void]
    clang_getCursorPrintingPolicy: _Callable[[_struct.CXCursor],
                                             _type.CXPrintingPolicy]
    clang_PrintingPolicy_dispose: _Callable[[_type.CXPrintingPolicy],  # Policy
                                            _type.c_void]
    clang_getCursorPrettyPrinted: _Callable[[_struct.CXCursor,  # Cursor
                                             _type.CXPrintingPolicy],  # Policy
                                            _struct.CXString]
    clang_getCursorDisplayName: _Callable[[_struct.CXCursor],
                                          _struct.CXString]
    clang_getCursorReferenced: _Callable[[_struct.CXCursor],
                                         _struct.CXCursor]
    clang_getCursorDefinition: _Callable[[_struct.CXCursor],
                                         _struct.CXCursor]
    clang_isCursorDefinition: _Callable[[_struct.CXCursor],
                                        _type.c_uint]
    clang_getCanonicalCursor: _Callable[[_struct.CXCursor],
                                        _struct.CXCursor]
    clang_Cursor_getObjCSelectorIndex: _Callable[[_struct.CXCursor],
                                                 _type.c_int]
    clang_Cursor_isDynamicCall: _Callable[[_struct.CXCursor],  # C
                                          _type.c_int]
    clang_Cursor_getReceiverType: _Callable[[_struct.CXCursor],  # C
                                            _struct.CXType]
    clang_Cursor_getObjCPropertyAttributes: _Callable[[_struct.CXCursor,  # C
                                                       _type.c_uint],  # reserved
                                                      _type.c_uint]
    clang_Cursor_getObjCPropertyGetterName: _Callable[[_struct.CXCursor],  # C
                                                      _struct.CXString]
    clang_Cursor_getObjCPropertySetterName: _Callable[[_struct.CXCursor],  # C
                                                      _struct.CXString]
    clang_Cursor_getObjCDeclQualifiers: _Callable[[_struct.CXCursor],  # C
                                                  _type.c_uint]
    clang_Cursor_isObjCOptional: _Callable[[_struct.CXCursor],  # C
                                           _type.c_uint]
    clang_Cursor_isVariadic: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
    clang_Cursor_isExternalSymbol: _Callable[[_struct.CXCursor,  # C
                                              _Pointer[_struct.CXString],  # language
                                              _Pointer[_struct.CXString],  # definedIn
                                              _Pointer[_type.c_uint]],  # isGenerated
                                             _type.c_uint]
    clang_Cursor_getCommentRange: _Callable[[_struct.CXCursor],  # C
                                            _struct.CXSourceRange]
    clang_Cursor_getRawCommentText: _Callable[[_struct.CXCursor],  # C
                                              _struct.CXString]
    clang_Cursor_getBriefCommentText: _Callable[[_struct.CXCursor],  # C
                                                _struct.CXString]
    clang_Cursor_getMangling: _Callable[[_struct.CXCursor],
                                        _struct.CXString]
    clang_Cursor_getCXXManglings: _Callable[[_struct.CXCursor],
                                            _Pointer[_struct.CXStringSet]]
    clang_Cursor_getObjCManglings: _Callable[[_struct.CXCursor],
                                             _Pointer[_struct.CXStringSet]]
    clang_Cursor_getModule: _Callable[[_struct.CXCursor],  # C
                                      _type.CXModule]
    clang_getModuleForFile: _Callable[[_type.CXTranslationUnit,
                                       _type.CXFile],
                                      _type.CXModule]
    clang_Module_getASTFile: _Callable[[_type.CXModule],  # Module
                                       _type.CXFile]
    clang_Module_getParent: _Callable[[_type.CXModule],  # Module
                                      _type.CXModule]
    clang_Module_getName: _Callable[[_type.CXModule],  # Module
                                    _struct.CXString]
    clang_Module_getFullName: _Callable[[_type.CXModule],  # Module
                                        _struct.CXString]
    clang_Module_isSystem: _Callable[[_type.CXModule],  # Module
                                     _type.c_int]
    clang_Module_getNumTopLevelHeaders: _Callable[[_type.CXTranslationUnit,
                                                   _type.CXModule],  # Module
                                                  _type.c_uint]
    clang_Module_getTopLevelHeader: _Callable[[_type.CXTranslationUnit,
                                               _type.CXModule,  # Module
                                               _type.c_uint],  # Index
                                              _type.CXFile]
    clang_CXXConstructor_isConvertingConstructor: _Callable[[_struct.CXCursor],  # C
                                                            _type.c_uint]
    clang_CXXConstructor_isCopyConstructor: _Callable[[_struct.CXCursor],  # C
                                                      _type.c_uint]
    clang_CXXConstructor_isDefaultConstructor: _Callable[[_struct.CXCursor],  # C
                                                         _type.c_uint]
    clang_CXXConstructor_isMoveConstructor: _Callable[[_struct.CXCursor],  # C
                                                      _type.c_uint]
    clang_CXXField_isMutable: _Callable[[_struct.CXCursor],  # C
                                        _type.c_uint]
    clang_CXXMethod_isDefaulted: _Callable[[_struct.CXCursor],  # C
                                           _type.c_uint]
    clang_CXXMethod_isPureVirtual: _Callable[[_struct.CXCursor],  # C
                                             _type.c_uint]
    clang_CXXMethod_isStatic: _Callable[[_struct.CXCursor],  # C
                                        _type.c_uint]
    clang_CXXMethod_isVirtual: _Callable[[_struct.CXCursor],  # C
                                         _type.c_uint]
    clang_CXXRecord_isAbstract: _Callable[[_struct.CXCursor],  # C
                                          _type.c_uint]
    clang_EnumDecl_isScoped: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
    clang_CXXMethod_isConst: _Callable[[_struct.CXCursor],  # C
                                       _type.c_uint]
    clang_getTemplateCursorKind: _Callable[[_struct.CXCursor],  # C
                                           _enum.CXCursorKind]
    clang_getSpecializedCursorTemplate: _Callable[[_struct.CXCursor],  # C
                                                  _struct.CXCursor]
    clang_getCursorReferenceNameRange: _Callable[[_struct.CXCursor,  # C
                                                  _type.c_uint,  # NameFlags
                                                  _type.c_uint],  # PieceIndex
                                                 _struct.CXSourceRange]
    clang_getToken: _Callable[[_type.CXTranslationUnit,  # TU
                               _struct.CXSourceLocation],  # Location
                              _Pointer[_struct.CXToken]]
    clang_getTokenKind: _Callable[[_struct.CXToken],
                                  _enum.CXTokenKind]
    clang_getTokenSpelling: _Callable[[_type.CXTranslationUnit,
                                       _struct.CXToken],
                                      _struct.CXString]
    clang_getTokenLocation: _Callable[[_type.CXTranslationUnit,
                                       _struct.CXToken],
                                      _struct.CXSourceLocation]
    clang_getTokenExtent: _Callable[[_type.CXTranslationUnit,
                                     _struct.CXToken],
                                    _struct.CXSourceRange]
    clang_tokenize: _Callable[[_type.CXTranslationUnit,  # TU
                               _struct.CXSourceRange,  # Range
                               _Pointer[_Pointer[_struct.CXToken]],  # Tokens
                               _Pointer[_type.c_uint]],  # NumTokens
                              _type.c_void]
    clang_annotateTokens: _Callable[[_type.CXTranslationUnit,  # TU
                                     _Pointer[_struct.CXToken],  # Tokens
                                     _type.c_uint,  # NumTokens
                                     _Pointer[_struct.CXCursor]],  # Cursors
                                    _type.c_void]
    clang_disposeTokens: _Callable[[_type.CXTranslationUnit,  # TU
                                    _Pointer[_struct.CXToken],  # Tokens
                                    _type.c_uint],  # NumTokens
                                   _type.c_void]
    clang_getCursorKindSpelling: _Callable[[_enum.CXCursorKind],  # Kind
                                           _struct.CXString]
    clang_getDefinitionSpellingAndExtent: _Callable[[_struct.CXCursor,
                                                     _Pointer[_type.c_char_p],  # startBuf
                                                     _Pointer[_type.c_char_p],  # endBuf
                                                     _Pointer[_type.c_uint],  # startLine
                                                     _Pointer[_type.c_uint],  # startColumn
                                                     _Pointer[_type.c_uint],  # endLine
                                                     _Pointer[_type.c_uint]],  # endColumn
                                                    _type.c_void]
    clang_enableStackTraces: _Callable[[],
                                       _type.c_void]
    clang_executeOnThread: _Callable[[_type.c_void_p,  # fn
                                      _type.c_void_p,  # user_data
                                      _type.c_uint],  # stack_size
                                     _type.c_void]
    clang_getCompletionChunkKind: _Callable[[_type.CXCompletionString,  # completion_string
                                             _type.c_uint],  # chunk_number
                                            _enum.CXCompletionChunkKind]
    clang_getCompletionChunkText: _Callable[[_type.CXCompletionString,  # completion_string
                                             _type.c_uint],  # chunk_number
                                            _struct.CXString]
    clang_getCompletionChunkCompletionString: _Callable[[_type.CXCompletionString,  # completion_string
                                                         _type.c_uint],  # chunk_number
                                                        _type.CXCompletionString]
    clang_getNumCompletionChunks: _Callable[[_type.CXCompletionString],  # completion_string
                                            _type.c_uint]
    clang_getCompletionPriority: _Callable[[_type.CXCompletionString],  # completion_string
                                           _type.c_uint]
    clang_getCompletionAvailability: _Callable[[_type.CXCompletionString],  # completion_string
                                               _enum.CXAvailabilityKind]
    clang_getCompletionNumAnnotations: _Callable[[_type.CXCompletionString],  # completion_string
                                                 _type.c_uint]
    clang_getCompletionAnnotation: _Callable[[_type.CXCompletionString,  # completion_string
                                              _type.c_uint],  # annotation_number
                                             _struct.CXString]
    clang_getCompletionParent: _Callable[[_type.CXCompletionString,  # completion_string
                                          _Pointer[_enum.CXCursorKind]],  # kind
                                         _struct.CXString]
    clang_getCompletionBriefComment: _Callable[[_type.CXCompletionString],  # completion_string
                                               _struct.CXString]
    clang_getCursorCompletionString: _Callable[[_struct.CXCursor],  # cursor
                                               _type.CXCompletionString]
    clang_getCompletionNumFixIts: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # results
                                             _type.c_uint],  # completion_index
                                            _type.c_uint]
    clang_getCompletionFixIt: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # results
                                         _type.c_uint,  # completion_index
                                         _type.c_uint,  # fixit_index
                                         _Pointer[_struct.CXSourceRange]],  # replacement_range
                                        _struct.CXString]
    clang_defaultCodeCompleteOptions: _Callable[[],
                                                _type.c_uint]
    clang_codeCompleteAt: _Callable[[_type.CXTranslationUnit,  # TU
                                     _type.c_char_p,  # complete_filename
                                     _type.c_uint,  # complete_line
                                     _type.c_uint,  # complete_column
                                     _Pointer[_struct.CXUnsavedFile],  # unsaved_files
                                     _type.c_uint,  # num_unsaved_files
                                     _type.c_uint],  # options
                                    _Pointer[_struct.CXCodeCompleteResults]]
    clang_sortCodeCompletionResults: _Callable[[_Pointer[_struct.CXCompletionResult],  # Results
                                                _type.c_uint],  # NumResults
                                               _type.c_void]
    clang_disposeCodeCompleteResults: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                                _type.c_void]
    clang_codeCompleteGetNumDiagnostics: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                                   _type.c_uint]
    clang_codeCompleteGetDiagnostic: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # Results
                                                _type.c_uint],  # Index
                                               _type.CXDiagnostic]
    clang_codeCompleteGetContexts: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                             _type.c_ulonglong]
    clang_codeCompleteGetContainerKind: _Callable[[_Pointer[_struct.CXCodeCompleteResults],  # Results
                                                   _Pointer[_type.c_uint]],  # IsIncomplete
                                                  _enum.CXCursorKind]
    clang_codeCompleteGetContainerUSR: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                                 _struct.CXString]
    clang_codeCompleteGetObjCSelector: _Callable[[_Pointer[_struct.CXCodeCompleteResults]],  # Results
                                                 _struct.CXString]
    clang_getClangVersion: _Callable[[],
                                     _struct.CXString]
    clang_toggleCrashRecovery: _Callable[[_type.c_uint],  # isEnabled
                                         _type.c_void]
    clang_getInclusions: _Callable[[_type.CXTranslationUnit,  # tu
                                    _type.CXInclusionVisitor,  # visitor
                                    _type.CXClientData],  # client_data
                                   _type.c_void]
    clang_Cursor_Evaluate: _Callable[[_struct.CXCursor],  # C
                                     _type.CXEvalResult]
    clang_EvalResult_getKind: _Callable[[_type.CXEvalResult],  # E
                                        _enum.CXEvalResultKind]
    clang_EvalResult_getAsInt: _Callable[[_type.CXEvalResult],  # E
                                         _type.c_int]
    clang_EvalResult_getAsLongLong: _Callable[[_type.CXEvalResult],  # E
                                              _type.c_longlong]
    clang_EvalResult_isUnsignedInt: _Callable[[_type.CXEvalResult],  # E
                                              _type.c_uint]
    clang_EvalResult_getAsUnsigned: _Callable[[_type.CXEvalResult],  # E
                                              _type.c_ulonglong]
    clang_EvalResult_getAsDouble: _Callable[[_type.CXEvalResult],  # E
                                            _type.c_double]
    clang_EvalResult_getAsStr: _Callable[[_type.CXEvalResult],  # E
                                         _type.c_char_p]
    clang_EvalResult_dispose: _Callable[[_type.CXEvalResult],  # E
                                        _type.c_void]
    clang_getRemappings: _Callable[[_type.c_char_p],  # path
                                   _type.CXRemapping]
    clang_getRemappingsFromFileList: _Callable[[_Pointer[_type.c_char_p],  # filePaths
                                                _type.c_uint],  # numFiles
                                               _type.CXRemapping]
    clang_remap_getNumFiles: _Callable[[_type.CXRemapping],
                                       _type.c_uint]
    clang_remap_getFilenames: _Callable[[_type.CXRemapping,
                                         _type.c_uint,  # index
                                         _Pointer[_struct.CXString],  # original
                                         _Pointer[_struct.CXString]],  # transformed
                                        _type.c_void]
    clang_remap_dispose: _Callable[[_type.CXRemapping],
                                   _type.c_void]
    clang_findReferencesInFile: _Callable[[_struct.CXCursor,  # cursor
                                           _type.CXFile,  # file
                                           _struct.CXCursorAndRangeVisitor],  # visitor
                                          _enum.CXResult]
    clang_findIncludesInFile: _Callable[[_type.CXTranslationUnit,  # TU
                                         _type.CXFile,  # file
                                         _struct.CXCursorAndRangeVisitor],  # visitor
                                        _enum.CXResult]
    clang_index_isEntityObjCContainerKind: _Callable[[_enum.CXIdxEntityKind],
                                                     _type.c_int]
    clang_index_getObjCContainerDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                    _Pointer[_struct.CXIdxObjCContainerDeclInfo]]
    clang_index_getObjCInterfaceDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                    _Pointer[_struct.CXIdxObjCInterfaceDeclInfo]]
    clang_index_getObjCCategoryDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                   _Pointer[_struct.CXIdxObjCCategoryDeclInfo]]
    clang_index_getObjCProtocolRefListInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                      _Pointer[_struct.CXIdxObjCProtocolRefListInfo]]
    clang_index_getObjCPropertyDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                                   _Pointer[_struct.CXIdxObjCPropertyDeclInfo]]
    clang_index_getIBOutletCollectionAttrInfo: _Callable[[_Pointer[_struct.CXIdxAttrInfo]],
                                                         _Pointer[_struct.CXIdxIBOutletCollectionAttrInfo]]
    clang_index_getCXXClassDeclInfo: _Callable[[_Pointer[_struct.CXIdxDeclInfo]],
                                               _Pointer[_struct.CXIdxCXXClassDeclInfo]]
    clang_index_getClientContainer: _Callable[[_Pointer[_struct.CXIdxContainerInfo]],
                                              _type.CXIdxClientContainer]
    clang_index_setClientContainer: _Callable[[_Pointer[_struct.CXIdxContainerInfo],
                                               _type.CXIdxClientContainer],
                                              _type.c_void]
    clang_index_getClientEntity: _Callable[[_Pointer[_struct.CXIdxEntityInfo]],
                                           _type.CXIdxClientEntity]
    clang_index_setClientEntity: _Callable[[_Pointer[_struct.CXIdxEntityInfo],
                                            _type.CXIdxClientEntity],
                                           _type.c_void]
    clang_IndexAction_create: _Callable[[_type.CXIndex],  # CIdx
                                        _type.CXIndexAction]
    clang_IndexAction_dispose: _Callable[[_type.CXIndexAction],
                                         _type.c_void]
    clang_indexLoc_getFileLocation: _Callable[[_struct.CXIdxLoc,  # loc
                                               _Pointer[_type.CXIdxClientFile],  # indexFile
                                               _Pointer[_type.CXFile],  # file
                                               _Pointer[_type.c_uint],  # line
                                               _Pointer[_type.c_uint],  # column
                                               _Pointer[_type.c_uint]],  # offset
                                              _type.c_void]
    clang_indexLoc_getCXSourceLocation: _Callable[[_struct.CXIdxLoc],  # loc
                                                  _struct.CXSourceLocation]
    clang_Type_visitFields: _Callable[[_struct.CXType,  # T
                                       _type.CXFieldVisitor,  # visitor
                                       _type.CXClientData],  # client_data
                                      _type.c_uint]
    # Rewrite
    clang_CXRewriter_create: _Callable[[_type.CXTranslationUnit],  # TU
                                       _type.CXRewriter]
    clang_CXRewriter_insertTextBefore: _Callable[[_type.CXRewriter,  # Rew
                                                  _struct.CXSourceLocation,  # Loc
                                                  _type.c_char_p],  # Insert
                                                 _type.c_void]
    clang_CXRewriter_replaceText: _Callable[[_type.CXRewriter,  # Rew
                                             _struct.CXSourceRange,  # ToBeReplaced
                                             _type.c_char_p],  # Replacement
                                            _type.c_void]
    clang_CXRewriter_removeText: _Callable[[_type.CXRewriter,  # Rew
                                            _struct.CXSourceRange],  # ToBeRemoved
                                           _type.c_void]
    clang_CXRewriter_overwriteChangedFiles: _Callable[[_type.CXRewriter],  # Rew
                                                      _type.c_int]
    clang_CXRewriter_writeMainFileToStdOut: _Callable[[_type.CXRewriter],  # Rew
                                                      _type.c_void]
    clang_CXRewriter_dispose: _Callable[[_type.CXRewriter],  # Rew
                                        _type.c_void]


# noinspection PyPep8Naming
class python(_PyDLL):
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
class advapi32(_WinDLL):
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
class cfgmgr32(_WinDLL):
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
class combase(_WinDLL):
    # roapi
    RoInitialize: _Callable[[_enum.RO_INIT_TYPE],  # initType
                            _type.HRESULT]
    RoUninitialize: _Callable[[],
                              _type.c_void]
    RoActivateInstance: _Callable[[_type.HSTRING,  # activatableClassId
                                   _Pointer[_inspectable.IInspectable]],  # instance
                                  _type.HRESULT]
    RoRegisterActivationFactories: _Callable[[_Pointer[_type.HSTRING],  # activatableClassIds
                                              _Pointer[_type.PFNGETACTIVATIONFACTORY],  # activationFactoryCallbacks
                                              _type.UINT32,  # count
                                              _Pointer[_Pointer[_struct.RO_REGISTRATION_COOKIE]]],  # cookie
                                             _type.HRESULT]
    RoRevokeActivationFactories: _Callable[[_Pointer[_struct.RO_REGISTRATION_COOKIE]],  # cookie
                                           _type.c_void]
    RoGetActivationFactory: _Callable[[_type.HSTRING,  # activatableClassId
                                       _Pointer[_struct.IID],  # iid
                                       _type.c_void_p],  # factory
                                      _type.HRESULT]
    RoRegisterForApartmentShutdown: _Callable[[_objidl.IApartmentShutdown,  # callbackObject
                                               _Pointer[_type.UINT64],  # apartmentIdentifier
                                               _Pointer[_type.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE]],  # regCookie
                                              _type.HRESULT]
    RoUnregisterForApartmentShutdown: _Callable[[_type.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE],  # regCookie
                                                _type.HRESULT]
    RoGetApartmentIdentifier: _Callable[[_Pointer[_type.UINT64]],  # apartmentIdentifier
                                        _type.HRESULT]
    Initialize: _Callable[[_enum.RO_INIT_TYPE],  # initType
                          _type.HRESULT]
    Uninitialize: _Callable[[],
                            _type.c_void]
    RegisterActivationFactories: _Callable[[_Pointer[_type.HSTRING],  # activatableClassIds
                                            _Pointer[_type.PFNGETACTIVATIONFACTORY],  # activationFactoryCallbacks
                                            _type.UINT32,  # count
                                            _Pointer[_Pointer[_struct.RO_REGISTRATION_COOKIE]]],  # cookie
                                           _type.HRESULT]
    RevokeActivationFactories: _Callable[[_Pointer[_struct.RO_REGISTRATION_COOKIE]],  # cookie
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
class comctl32(_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    # CommCtrl
    InitCommonControls: _Callable[[],
                                  _type.c_void]
    InitCommonControlsEx: _Callable[[_Pointer[_struct.INITCOMMONCONTROLSEX]],
                                    _type.BOOL]


# noinspection PyPep8Naming
class comdlg32(_WinDLL):
    # commdlg
    ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]],
                            _type.BOOL]
    ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]],
                            _type.BOOL]


# noinspection PyPep8Naming
class computecore(_WinDLL):
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
class crypt32(_WinDLL):
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
class d2d1(_WinDLL):
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
    D2D1CreateDeviceContext: _Callable[[_dxgi.IDXGISurface,  # dxgiSurface
                                        _Optional[_Pointer[_struct.D2D1_CREATION_PROPERTIES]],  # creationProperties
                                        _Pointer[_d2d1_1.ID2D1DeviceContext]],  # d2dDeviceContext
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
class d3d11(_WinDLL):
    # d3d11
    D3D11CreateDevice: _Callable[[_Optional[_dxgi.IDXGIAdapter],  # pAdapter
                                  _enum.D3D_DRIVER_TYPE,  # DriverType
                                  _type.HMODULE,  # Software
                                  _type.UINT,  # Flags
                                  _Optional[_Pointer[_enum.D3D_FEATURE_LEVEL]],  # pFeatureLevels
                                  _type.UINT,  # FeatureLevels
                                  _type.UINT,  # SDKVersion
                                  _Optional[_Pointer[_d3d11.ID3D11Device]],  # ppDevice
                                  _Optional[_Pointer[_enum.D3D_FEATURE_LEVEL]],  # pFeatureLevel,
                                  _Optional[_Pointer[_d3d11.ID3D11DeviceContext]]],  # ppImmediateContext
                                 _type.HRESULT]


class DWrite(_WinDLL):
    # dwrite
    DWriteCreateFactory: _Callable[[_enum.DWRITE_FACTORY_TYPE,  # factoryType
                                    _Pointer[_struct.IID],  # iid
                                    _Pointer[_Unknwnbase.IUnknown]],  # factory
                                   _type.HRESULT]


# noinspection PyPep8Naming
class dwmapi(_WinDLL):
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
class gdi32(_WinDLL):
    # wingdi
    AddFontResourceA: _Callable[[_type.LPCSTR],
                                _type.c_int]
    AddFontResourceW: _Callable[[_type.LPCWSTR],
                                _type.c_int]
    AnimatePalette: _Callable[[_type.HPALETTE,  # hPal
                               _type.UINT,  # iStartIndex
                               _type.UINT,  # cEntries
                               _Pointer[_struct.PALETTEENTRY]],  # ppe
                              _type.BOOL]
    Arc: _Callable[[_type.HDC,  # hdc
                    _type.c_int,  # x1
                    _type.c_int,  # y1
                    _type.c_int,  # x2
                    _type.c_int,  # y2
                    _type.c_int,  # x3
                    _type.c_int,  # y3
                    _type.c_int,  # x4
                    _type.c_int],  # y4
                   _type.BOOL]
    BitBlt: _Callable[[_type.HDC,  # hdc
                       _type.c_int,  # x
                       _type.c_int,  # y
                       _type.c_int,  # cx
                       _type.c_int,  # cy
                       _type.HDC,  # hdcSrc
                       _type.c_int,  # x1
                       _type.c_int,  # y1
                       _type.DWORD],  # rop
                      _type.BOOL]
    CancelDC: _Callable[[_type.HDC],  # hdc
                        _type.BOOL]
    Chord: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # x1
                      _type.c_int,  # y1
                      _type.c_int,  # x2
                      _type.c_int,  # y2
                      _type.c_int,  # x3
                      _type.c_int,  # y3
                      _type.c_int,  # x4
                      _type.c_int],  # y4
                     _type.BOOL]
    ChoosePixelFormat: _Callable[[_type.HDC,  # hdc
                                  _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                                 _type.c_int]
    CloseMetaFile: _Callable[[_type.HDC],  # hdc
                             _type.HMETAFILE]
    CombineRgn: _Callable[[_type.HRGN,  # hrgnDst
                           _type.HRGN,  # hrgnSrc1
                           _type.HRGN,  # hrgnSrc2
                           _type.c_int],  # iMode
                          _type.c_int]
    CopyMetaFileA: _Callable[[_type.HMETAFILE,
                              _type.LPCSTR],
                             _type.HMETAFILE]
    CopyMetaFileW: _Callable[[_type.HMETAFILE,
                              _type.LPCWSTR],
                             _type.HMETAFILE]
    CreateBitmap: _Callable[[_type.c_int,  # nWidth
                             _type.c_int,  # nHeight
                             _type.UINT,  # nPlanes
                             _type.UINT,  # nBitCount
                             _type.c_void_p],  # lpBits
                            _type.HBITMAP]
    CreateBitmapIndirect: _Callable[[_Pointer[_struct.BITMAP]],  # pbm
                                    _type.HBITMAP]
    CreateBrushIndirect: _Callable[[_Pointer[_struct.LOGBRUSH]],  # plbrush
                                   _type.HBRUSH]
    CreateCompatibleBitmap: _Callable[[_type.HDC,  # hdc
                                       _type.c_int,  # cx
                                       _type.c_int],  # cy
                                      _type.HBITMAP]
    CreateDiscardableBitmap: _Callable[[_type.HDC,  # hdc
                                        _type.c_int,  # cx
                                        _type.c_int],  # cy
                                       _type.HBITMAP]
    CreateCompatibleDC: _Callable[[_type.HDC],  # hdc
                                  _type.HDC]
    CreateDCA: _Callable[[_type.LPCSTR,  # pwszDriver
                          _type.LPCSTR,  # pwszDevice
                          _type.LPCSTR,  # pszPort
                          _Pointer[_struct.DEVMODEA]],  # pdm
                         _type.HDC]
    CreateDCW: _Callable[[_type.LPCWSTR,  # pwszDriver
                          _type.LPCWSTR,  # pwszDevice
                          _type.LPCWSTR,  # pszPort
                          _Pointer[_struct.DEVMODEW]],  # pdm
                         _type.HDC]
    CreateDIBitmap: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.BITMAPINFOHEADER],  # pbmih
                               _type.DWORD,  # flInit
                               _type.c_void_p,  # pjBits
                               _Pointer[_struct.BITMAPINFO],  # pbmi
                               _type.UINT],  # iUsage
                              _type.HBITMAP]
    CreateDIBPatternBrush: _Callable[[_type.HGLOBAL,  # h
                                      _type.UINT],  # iUsage
                                     _type.HBRUSH]
    CreateDIBPatternBrushPt: _Callable[[_type.c_void_p,  # lpPackedDIB
                                        _type.UINT],  # iUsage
                                       _type.HBRUSH]
    CreateEllipticRgn: _Callable[[_type.c_int,  # x1
                                  _type.c_int,  # y1
                                  _type.c_int,  # x2
                                  _type.c_int],  # y2
                                 _type.HRGN]
    CreateEllipticRgnIndirect: _Callable[[_Pointer[_struct.RECT]],  # lprect
                                         _type.HRGN]
    CreateFontIndirectA: _Callable[[_Pointer[_struct.LOGFONTA]],  # lplf
                                   _type.HFONT]
    CreateFontIndirectW: _Callable[[_Pointer[_struct.LOGFONTW]],  # lplf
                                   _type.HFONT]
    CreateFontA: _Callable[[_type.c_int,  # cHeight
                            _type.c_int,  # cWidth
                            _type.c_int,  # cEscapement
                            _type.c_int,  # cOrientation
                            _type.c_int,  # cWeight
                            _type.DWORD,  # bItalic
                            _type.DWORD,  # bUnderline
                            _type.DWORD,  # bStrikeOut
                            _type.DWORD,  # iCharSet
                            _type.DWORD,  # iOutPrecision
                            _type.DWORD,  # iClipPrecision
                            _type.DWORD,  # iQuality
                            _type.DWORD,  # iPitchAndFamily
                            _type.LPCSTR],  # pszFaceName
                           _type.HFONT]
    CreateFontW: _Callable[[_type.c_int,  # cHeight
                            _type.c_int,  # cWidth
                            _type.c_int,  # cEscapement
                            _type.c_int,  # cOrientation
                            _type.c_int,  # cWeight
                            _type.DWORD,  # bItalic
                            _type.DWORD,  # bUnderline
                            _type.DWORD,  # bStrikeOut
                            _type.DWORD,  # iCharSet
                            _type.DWORD,  # iOutPrecision
                            _type.DWORD,  # iClipPrecision
                            _type.DWORD,  # iQuality
                            _type.DWORD,  # iPitchAndFamily
                            _type.LPCWSTR],  # pszFaceName
                           _type.HFONT]
    CreateHatchBrush: _Callable[[_type.c_int,  # iHatch
                                 _type.COLORREF],  # color
                                _type.HBRUSH]
    CreateICA: _Callable[[_type.LPCSTR,  # pszDriver
                          _type.LPCSTR,  # pszDevice
                          _type.LPCSTR,  # pszPort
                          _Pointer[_struct.DEVMODEA]],  # pdm
                         _type.HDC]
    CreateICW: _Callable[[_type.LPCWSTR,  # pszDriver
                          _type.LPCWSTR,  # pszDevice
                          _type.LPCWSTR,  # pszPort
                          _Pointer[_struct.DEVMODEW]],  # pdm
                         _type.HDC]
    CreateMetaFileA: _Callable[[_type.LPCSTR],  # pszFile
                               _type.HDC]
    CreateMetaFileW: _Callable[[_type.LPCWSTR],  # pszFile
                               _type.HDC]
    CreatePalette: _Callable[[_Pointer[_struct.LOGPALETTE]],  # plpal
                             _type.HPALETTE]
    CreatePen: _Callable[[_type.c_int,  # iStyle
                          _type.c_int,  # cWidth
                          _type.COLORREF],  # color
                         _type.HPEN]
    CreatePenIndirect: _Callable[[_Pointer[_struct.LOGPEN]],  # plpen
                                 _type.HPEN]
    CreatePolyPolygonRgn: _Callable[[_Pointer[_struct.POINT],  # pptl
                                     _Pointer[_type.INT],  # pc
                                     _type.c_int,  # cPoly
                                     _type.c_int],  # iMode
                                    _type.HRGN]
    CreatePatternBrush: _Callable[[_type.HBITMAP],  # hbm
                                  _type.HBRUSH]
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
    CreateScalableFontResourceA: _Callable[[_type.DWORD,  # fdwHidden
                                            _type.LPCSTR,  # lpszFont
                                            _type.LPCSTR,  # lpszFile
                                            _type.LPCSTR],  # lpszPath
                                           _type.BOOL]
    CreateScalableFontResourceW: _Callable[[_type.DWORD,  # fdwHidden
                                            _type.LPCWSTR,  # lpszFont
                                            _type.LPCWSTR,  # lpszFile
                                            _type.LPCWSTR],  # lpszPath
                                           _type.BOOL]
    CreateSolidBrush: _Callable[[_type.COLORREF],  # color
                                _type.HBRUSH]
    DeleteDC: _Callable[[_type.HDC],  # hdc
                        _type.BOOL]
    DeleteMetaFile: _Callable[[_type.HMETAFILE],  # hmf
                              _type.BOOL]
    DeleteObject: _Callable[[_type.HGDIOBJ],  # ho
                            _type.BOOL]
    DescribePixelFormat: _Callable[[_type.HDC,  # hdc
                                    _type.c_int,  # iPixelFormat
                                    _type.UINT,  # nBytes
                                    _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                                   _type.c_int]
    DeviceCapabilitiesA: _Callable[[_type.LPCSTR,  # pDevice
                                    _type.LPCSTR,  # pPort
                                    _type.WORD,  # fwCapability
                                    _type.LPSTR,  # pOutput
                                    _Pointer[_struct.DEVMODEA]],  # pDevMode
                                   _type.c_int]
    DeviceCapabilitiesW: _Callable[[_type.LPCWSTR,  # pDevice
                                    _type.LPCWSTR,  # pPort
                                    _type.WORD,  # fwCapability
                                    _type.LPWSTR,  # pOutput
                                    _Pointer[_struct.DEVMODEW]],  # pDevMode
                                   _type.c_int]
    DrawEscape: _Callable[[_type.HDC,  # hdc
                           _type.c_int,  # iEscape
                           _type.c_int,  # cjIn
                           _type.LPCSTR],  # lpIn
                          _type.c_int]
    Ellipse: _Callable[[_type.HDC,  # hdc
                        _type.c_int,  # left
                        _type.c_int,  # top
                        _type.c_int,  # right
                        _type.c_int],  # bottom
                       _type.BOOL]
    EnumObjects: _Callable[[_type.HDC,  # hdc
                            _type.c_int,  # nType
                            _type.GOBJENUMPROC,  # lpFunc
                            _type.LPARAM],  # lParam
                           _type.c_int]
    EqualRgn: _Callable[[_type.HRGN,  # hrgn1
                         _type.HRGN],  # hrgn2
                        _type.BOOL]
    Escape: _Callable[[_type.HDC,  # hdc
                       _type.c_int,  # iEscape
                       _type.c_int,  # cjIn
                       _type.LPCSTR,  # pvIn
                       _type.LPVOID],  # pvOut
                      _type.c_int]
    ExtEscape: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # iEscape
                          _type.c_int,  # cjInput
                          _type.LPCSTR,  # lpInData
                          _type.c_int,  # cjOutput
                          _type.LPSTR],  # lpOutData
                         _type.c_int]
    ExcludeClipRect: _Callable[[_type.HDC,  # hdc
                                _type.c_int,  # left
                                _type.c_int,  # top
                                _type.c_int,  # right
                                _type.c_int],  # bottom
                               _type.c_int]
    ExtCreateRegion: _Callable[[_Pointer[_struct.XFORM],  # lpx
                                _type.DWORD,  # nCount
                                _Pointer[_struct.RGNDATA]],  # lpData
                               _type.HRGN]
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
    GetAspectRatioFilterEx: _Callable[[_type.HDC,  # hdc
                                       _Pointer[_struct.SIZE]],  # lpsize
                                      _type.BOOL]
    GetBkColor: _Callable[[_type.HDC],  # hdc
                          _type.COLORREF]
    GetDCBrushColor: _Callable[[_type.HDC],  # hdc
                               _type.COLORREF]
    GetDCPenColor: _Callable[[_type.HDC],  # hdc
                             _type.COLORREF]
    GetBkMode: _Callable[[_type.HDC],  # hdc
                         _type.c_int]
    GetBitmapBits: _Callable[[_type.HBITMAP,  # hbit
                              _type.LONG,  # cb
                              _type.LPVOID],  # lpvBits
                             _type.LONG]
    GetBitmapDimensionEx: _Callable[[_type.HBITMAP,  # hbit
                                     _Pointer[_struct.SIZE]],  # lpsize
                                    _type.BOOL]
    GetBoundsRect: _Callable[[_type.HDC,  # hdc
                              _Pointer[_struct.RECT],  # lprect
                              _type.UINT],  # flags
                             _type.UINT]
    GetBrushOrgEx: _Callable[[_type.HDC,  # hdc
                              _Pointer[_struct.POINT]],  # lppt
                             _type.BOOL]
    GetCharWidthA: _Callable[[_type.HDC,  # hdc
                              _type.UINT,  # iFirst
                              _type.UINT,  # iLast
                              _Pointer[_type.c_int]],  # lpBuffer
                             _type.BOOL]
    GetCharWidthW: _Callable[[_type.HDC,  # hdc
                              _type.UINT,  # iFirst
                              _type.UINT,  # iLast
                              _Pointer[_type.c_int]],  # lpBuffer
                             _type.BOOL]
    GetCharWidth32A: _Callable[[_type.HDC,  # hdc
                                _type.UINT,  # iFirst
                                _type.UINT,  # iLast
                                _Pointer[_type.c_int]],  # lpBuffer
                               _type.BOOL]
    GetCharWidth32W: _Callable[[_type.HDC,  # hdc
                                _type.UINT,  # iFirst
                                _type.UINT,  # iLast
                                _Pointer[_type.c_int]],  # lpBuffer
                               _type.BOOL]
    GetCharWidthFloatA: _Callable[[_type.HDC,  # hdc
                                   _type.UINT,  # iFirst
                                   _type.UINT,  # iLast
                                   _Pointer[_type.FLOAT]],  # lpBuffer
                                  _type.BOOL]
    GetCharWidthFloatW: _Callable[[_type.HDC,  # hdc
                                   _type.UINT,  # iFirst
                                   _type.UINT,  # iLast
                                   _Pointer[_type.FLOAT]],  # lpBuffer
                                  _type.BOOL]
    GetCharABCWidthsA: _Callable[[_type.HDC,  # hdc
                                  _type.UINT,  # wFirst
                                  _type.UINT,  # wLast
                                  _Pointer[_struct.ABC]],  # lpABC
                                 _type.BOOL]
    GetCharABCWidthsW: _Callable[[_type.HDC,  # hdc
                                  _type.UINT,  # wFirst
                                  _type.UINT,  # wLast
                                  _Pointer[_struct.ABC]],  # lpABC
                                 _type.BOOL]
    GetCharABCWidthsFloatA: _Callable[[_type.HDC,  # hdc
                                       _type.UINT,  # iFirst
                                       _type.UINT,  # iLast
                                       _Pointer[_struct.ABCFLOAT]],  # lpABC
                                      _type.BOOL]
    GetCharABCWidthsFloatW: _Callable[[_type.HDC,  # hdc
                                       _type.UINT,  # iFirst
                                       _type.UINT,  # iLast
                                       _Pointer[_struct.ABCFLOAT]],  # lpABC
                                      _type.BOOL]
    GetClipBox: _Callable[[_type.HDC,  # hdc
                           _Pointer[_struct.RECT]],  # lprect
                          _type.c_int]
    GetClipRgn: _Callable[[_type.HDC,  # hdc
                           _type.HRGN],  # hrgn
                          _type.c_int]
    GetMetaRgn: _Callable[[_type.HDC,  # hdc
                           _type.HRGN],  # hrgn
                          _type.c_int]
    GetCurrentObject: _Callable[[_type.HDC,  # hdc
                                 _type.UINT],  # type
                                _type.HGDIOBJ]
    GetCurrentPositionEx: _Callable[[_type.HDC,  # hdc
                                     _Pointer[_struct.POINT]],  # lppt
                                    _type.BOOL]
    GetDeviceCaps: _Callable[[_type.HDC,  # hdc
                              _type.c_int],  # index
                             _type.c_int]
    GetDIBits: _Callable[[_type.HDC,  # hdc
                          _type.HBITMAP,  # hbm
                          _type.UINT,  # start
                          _type.UINT,  # cLines
                          _type.LPVOID,  # lpvBits
                          _Pointer[_struct.BITMAPINFO],  # lpbmi
                          _type.UINT],  # usage
                         _type.c_int]
    GetFontData: _Callable[[_type.HDC,  # hdc
                            _type.DWORD,  # dwTable
                            _type.DWORD,  # dwOffset
                            _type.PVOID,  # pvBuffer
                            _type.DWORD],  # cjBuffer
                           _type.DWORD]
    GetGlyphOutlineA: _Callable[[_type.HDC,  # hdc
                                 _type.UINT,  # uChar
                                 _type.UINT,  # fuFormat
                                 _Pointer[_struct.GLYPHMETRICS],  # lpgm
                                 _type.DWORD,  # cjBuffer
                                 _type.LPVOID,  # pvBuffer
                                 _Pointer[_struct.MAT2]],  # lpmat2
                                _type.DWORD]
    GetGlyphOutlineW: _Callable[[_type.HDC,  # hdc
                                 _type.UINT,  # uChar
                                 _type.UINT,  # fuFormat
                                 _Pointer[_struct.GLYPHMETRICS],  # lpgm
                                 _type.DWORD,  # cjBuffer
                                 _type.LPVOID,  # pvBuffer
                                 _Pointer[_struct.MAT2]],  # lpmat2
                                _type.DWORD]
    GetGraphicsMode: _Callable[[_type.HDC],  # hdc
                               _type.c_int]
    GetMapMode: _Callable[[_type.HDC],  # hdc
                          _type.c_int]
    GetMetaFileBitsEx: _Callable[[_type.HMETAFILE,  # hMF
                                  _type.UINT,  # cbBuffer
                                  _type.LPVOID],  # lpData
                                 _type.UINT]
    GetMetaFileA: _Callable[[_type.LPCSTR],  # lpName
                            _type.HMETAFILE]
    GetMetaFileW: _Callable[[_type.LPCWSTR],  # lpName
                            _type.HMETAFILE]
    GetNearestColor: _Callable[[_type.HDC,  # hdc
                                _type.COLORREF],  # color
                               _type.COLORREF]
    GetNearestPaletteIndex: _Callable[[_type.HPALETTE,  # h
                                       _type.COLORREF],  # color
                                      _type.UINT]
    GetObjectType: _Callable[[_type.HGDIOBJ],  # h
                             _type.DWORD]
    GetOutlineTextMetricsA: _Callable[[_type.HDC,  # hdc
                                       _type.UINT,  # cjCopy
                                       _Pointer[_struct.OUTLINETEXTMETRICA]],  # potm
                                      _type.UINT]
    GetOutlineTextMetricsW: _Callable[[_type.HDC,  # hdc
                                       _type.UINT,  # cjCopy
                                       _Pointer[_struct.OUTLINETEXTMETRICW]],  # potm
                                      _type.UINT]
    GetPaletteEntries: _Callable[[_type.HPALETTE,  # hpal
                                  _type.UINT,  # iStart
                                  _type.UINT,  # cEntries
                                  _Pointer[_struct.PALETTEENTRY]],  # pPalEntries
                                 _type.UINT]
    GetPixel: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # x
                         _type.c_int],  # y
                        _type.COLORREF]
    GetPixelFormat: _Callable[[_type.HDC],  # hdc
                              _type.c_int]
    GetPolyFillMode: _Callable[[_type.HDC],  # hdc
                               _type.c_int]
    GetRasterizerCaps: _Callable[[_Pointer[_struct.RASTERIZER_STATUS],  # lpraststat
                                  _type.UINT],  # cjBytes
                                 _type.BOOL]
    GetRandomRgn: _Callable[[_type.HDC,  # hdc
                             _type.HRGN,  # hrgn
                             _type.INT],  # i
                            _type.c_int]
    GetRegionData: _Callable[[_type.HRGN,  # hrgn
                              _type.DWORD,  # nCount
                              _Pointer[_struct.RGNDATA]],  # lpRgnData
                             _type.DWORD]
    GetRgnBox: _Callable[[_type.HRGN,  # hrgn
                          _Pointer[_struct.RECT]],  # lprc
                         _type.c_int]
    GetStockObject: _Callable[[_type.c_int],  # i
                              _type.HGDIOBJ]
    GetStretchBltMode: _Callable[[_type.HDC],  # hdc
                                 _type.c_int]
    GetSystemPaletteEntries: _Callable[[_type.HDC,  # hdc
                                        _type.UINT,  # iStart
                                        _type.UINT,  # cEntries
                                        _Pointer[_struct.PALETTEENTRY]],  # pPalEntries
                                       _type.UINT]
    GetSystemPaletteUse: _Callable[[_type.HDC],  # hdc
                                   _type.UINT]
    GetTextCharacterExtra: _Callable[[_type.HDC],  # hdc
                                     _type.c_int]
    GetTextAlign: _Callable[[_type.HDC],  # hdc
                            _type.UINT]
    GetTextColor: _Callable[[_type.HDC],  # hdc
                            _type.COLORREF]
    GetTextExtentPointA: _Callable[[_type.HDC,  # hdc
                                    _type.LPCSTR,  # lpString
                                    _type.c_int,  # c
                                    _Pointer[_struct.SIZE]],  # lpsz
                                   _type.BOOL]
    GetTextExtentPointW: _Callable[[_type.HDC,  # hdc
                                    _type.LPCWSTR,  # lpString
                                    _type.c_int,  # c
                                    _Pointer[_struct.SIZE]],  # lpsz
                                   _type.BOOL]
    GetTextExtentPoint32A: _Callable[[_type.HDC,  # hdc
                                      _type.LPCSTR,  # lpString
                                      _type.c_int,  # c
                                      _Pointer[_struct.SIZE]],  # psizl
                                     _type.BOOL]
    GetTextExtentPoint32W: _Callable[[_type.HDC,  # hdc
                                      _type.LPCWSTR,  # lpString
                                      _type.c_int,  # c
                                      _Pointer[_struct.SIZE]],  # psizl
                                     _type.BOOL]
    GetTextExtentExPointA: _Callable[[_type.HDC,  # hdc
                                      _type.LPCSTR,  # lpszString
                                      _type.c_int,  # cchString
                                      _type.c_int,  # nMaxExtent
                                      _Pointer[_type.c_int],  # lpnFit
                                      _Pointer[_type.c_int],  # lpnDx
                                      _Pointer[_struct.SIZE]],  # lpSize
                                     _type.BOOL]
    GetTextExtentExPointW: _Callable[[_type.HDC,  # hdc
                                      _type.LPCWSTR,  # lpszString
                                      _type.c_int,  # cchString
                                      _type.c_int,  # nMaxExtent
                                      _Pointer[_type.c_int],  # lpnFit
                                      _Pointer[_type.c_int],  # lpnDx
                                      _Pointer[_struct.SIZE]],  # lpSize
                                     _type.BOOL]
    GetTextCharset: _Callable[[_type.HDC],  # hdc
                              _type.c_int]
    GetTextCharsetInfo: _Callable[[_type.HDC,  # hdc
                                   _Pointer[_struct.FONTSIGNATURE],  # lpSig
                                   _type.DWORD],  # dwFlags
                                  _type.c_int]
    TranslateCharsetInfo: _Callable[[_Pointer[_type.DWORD],  # lpSrc
                                     _Pointer[_struct.CHARSETINFO],  # lpCs
                                     _type.DWORD],  # dwFlags
                                    _type.BOOL]
    GetFontLanguageInfo: _Callable[[_type.HDC],  # hdc
                                   _type.DWORD]
    GetCharacterPlacementA: _Callable[[_type.HDC,  # hdc
                                       _type.LPCSTR,  # lpString
                                       _type.c_int,  # nCount
                                       _type.c_int,  # nMexExtent
                                       _Pointer[_struct.GCP_RESULTSA],  # lpResults
                                       _type.DWORD],  # dwFlags
                                      _type.DWORD]
    GetCharacterPlacementW: _Callable[[_type.HDC,  # hdc
                                       _type.LPCWSTR,  # lpString
                                       _type.c_int,  # nCount
                                       _type.c_int,  # nMexExtent
                                       _Pointer[_struct.GCP_RESULTSW],  # lpResults
                                       _type.DWORD],  # dwFlags
                                      _type.DWORD]
    GetFontUnicodeRanges: _Callable[[_type.HDC,  # hdc
                                     _Pointer[_struct.GLYPHSET]],  # lpgs
                                    _type.DWORD]
    GetGlyphIndicesA: _Callable[[_type.HDC,  # hdc
                                 _type.LPCSTR,  # lpstr
                                 _type.c_int,  # c
                                 _Pointer[_type.WORD],  # pgi
                                 _type.DWORD],  # fl
                                _type.DWORD]
    GetGlyphIndicesW: _Callable[[_type.HDC,  # hdc
                                 _type.LPCWSTR,  # lpstr
                                 _type.c_int,  # c
                                 _Pointer[_type.WORD],  # pgi
                                 _type.DWORD],  # fl
                                _type.DWORD]
    GetTextExtentPointI: _Callable[[_type.HDC,  # hdc
                                    _Pointer[_type.WORD],  # pgiIn
                                    _type.c_int,  # cgi
                                    _Pointer[_struct.SIZE]],  # psize
                                   _type.BOOL]
    GetTextExtentExPointI: _Callable[[_type.HDC,  # hdc
                                      _Pointer[_type.WORD],  # lpwszString
                                      _type.c_int,  # cwchString
                                      _type.c_int,  # nMaxExtent
                                      _Pointer[_type.c_int],  # lpnFit
                                      _Pointer[_type.c_int],  # lpnDx
                                      _Pointer[_struct.SIZE]],  # lpSize
                                     _type.BOOL]
    GetCharWidthI: _Callable[[_type.HDC,  # hdc
                              _type.UINT,  # giFirst
                              _type.UINT,  # cgi
                              _Pointer[_type.WORD],  # pgi
                              _Pointer[_type.c_int]],  # piWidths
                             _type.BOOL]
    GetCharABCWidthsI: _Callable[[_type.HDC,  # hdc
                                  _type.UINT,  # giFirst
                                  _type.UINT,  # cgi
                                  _Pointer[_type.WORD],  # pgi
                                  _Pointer[_struct.ABC]],  # pabc
                                 _type.BOOL]
    AddFontResourceExA: _Callable[[_type.LPCSTR,  # name
                                   _type.DWORD,  # fl
                                   _type.PVOID],  # res
                                  _type.c_int]
    AddFontResourceExW: _Callable[[_type.LPCWSTR,  # name
                                   _type.DWORD,  # fl
                                   _type.PVOID],  # res
                                  _type.c_int]
    RemoveFontResourceExA: _Callable[[_type.LPCSTR,  # name
                                      _type.DWORD,  # fl
                                      _type.PVOID],  # pdv
                                     _type.BOOL]
    RemoveFontResourceExW: _Callable[[_type.LPCWSTR,  # name
                                      _type.DWORD,  # fl
                                      _type.PVOID],  # pdv
                                     _type.BOOL]
    AddFontMemResourceEx: _Callable[[_type.PVOID,  # pFileView
                                     _type.DWORD,  # cjSize
                                     _type.PVOID,  # pvResrved
                                     _Pointer[_type.DWORD]],  # pNumFonts
                                    _type.HANDLE]
    RemoveFontMemResourceEx: _Callable[[_type.HANDLE],  # h
                                       _type.BOOL]
    CreateFontIndirectExA: _Callable[[_Pointer[_struct.ENUMLOGFONTEXDVA]],
                                     _type.HFONT]
    CreateFontIndirectExW: _Callable[[_Pointer[_struct.ENUMLOGFONTEXDVW]],
                                     _type.HFONT]
    GetViewportExtEx: _Callable[[_type.HDC,  # hdc
                                 _Pointer[_struct.SIZE]],  # lpsize
                                _type.BOOL]
    GetViewportOrgEx: _Callable[[_type.HDC,  # hdc
                                 _Pointer[_struct.POINT]],  # lppoint
                                _type.BOOL]
    GetWindowExtEx: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.SIZE]],  # lpsize
                              _type.BOOL]
    GetWindowOrgEx: _Callable[[_type.HDC,  # hdc
                               _Pointer[_struct.POINT]],  # lppoint
                              _type.BOOL]
    IntersectClipRect: _Callable[[_type.HDC,  # hdc
                                  _type.c_int,  # left
                                  _type.c_int,  # top
                                  _type.c_int,  # right
                                  _type.c_int],  # bottom
                                 _type.c_int]
    InvertRgn: _Callable[[_type.HDC,  # hdc
                          _type.HRGN],  # hrgn
                         _type.BOOL]
    LineDDA: _Callable[[_type.c_int,  # xStart
                        _type.c_int,  # yStart
                        _type.c_int,  # xEnd
                        _type.c_int,  # yEnd
                        _type.LINEDDAPROC,  # lpProc
                        _type.LPARAM],  # data
                       _type.BOOL]
    LineTo: _Callable[[_type.HDC,  # hdc
                       _type.c_int,  # x
                       _type.c_int],  # y
                      _type.BOOL]
    MaskBlt: _Callable[[_type.HDC,  # hdcDest
                        _type.c_int,  # xDest
                        _type.c_int,  # yDest
                        _type.c_int,  # width
                        _type.c_int,  # height
                        _type.HDC,  # hdcSrc
                        _type.c_int,  # xSrc
                        _type.c_int,  # ySrc
                        _type.HBITMAP,  # hbmMask
                        _type.c_int,  # xMask
                        _type.c_int,  # yMask
                        _type.DWORD],  # rop
                       _type.BOOL]
    PlgBlt: _Callable[[_type.HDC,  # hdcDest
                       _Pointer[_struct.POINT],  # lpPoint
                       _type.HDC,  # hdcSrc
                       _type.c_int,  # xSrc
                       _type.c_int,  # ySrc
                       _type.c_int,  # width
                       _type.c_int,  # height
                       _type.HBITMAP,  # hbmMask
                       _type.c_int,  # xMask
                       _type.c_int],  # yMask
                      _type.BOOL]
    OffsetClipRgn: _Callable[[_type.HDC,  # hdc
                              _type.c_int,  # x
                              _type.c_int],  # y
                             _type.c_int]
    OffsetRgn: _Callable[[_type.HRGN,  # hrgn
                          _type.c_int,  # x
                          _type.c_int],  # y
                         _type.c_int]
    PatBlt: _Callable[[_type.HDC,  # hdc
                       _type.c_int,  # x
                       _type.c_int,  # y
                       _type.c_int,  # w
                       _type.c_int,  # h
                       _type.DWORD],  # rop
                      _type.BOOL]
    Pie: _Callable[[_type.HDC,  # hdc
                    _type.c_int,  # left
                    _type.c_int,  # top
                    _type.c_int,  # right
                    _type.c_int,  # bottom
                    _type.c_int,  # xr1
                    _type.c_int,  # yr1
                    _type.c_int,  # xr2
                    _type.c_int],  # yr2
                   _type.BOOL]
    PlayMetaFile: _Callable[[_type.HDC,  # hdc
                             _type.HMETAFILE],  # hmf
                            _type.BOOL]
    PaintRgn: _Callable[[_type.HDC,  # hdc
                         _type.HRGN],  # hrgn
                        _type.BOOL]
    PolyPolygon: _Callable[[_type.HDC,  # hdc
                            _Pointer[_struct.POINT],  # apt
                            _Pointer[_type.INT],  # asz
                            _type.c_int],  # csz
                           _type.BOOL]
    PtInRegion: _Callable[[_type.HRGN,  # hrgn
                           _type.c_int,  # x
                           _type.c_int],  # y
                          _type.BOOL]
    PtVisible: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # x
                          _type.c_int],  # y
                         _type.BOOL]
    RectInRegion: _Callable[[_type.HRGN,  # hrgn
                             _Pointer[_struct.RECT]],  # lprect
                            _type.BOOL]
    RectVisible: _Callable[[_type.HDC,  # hdc
                            _Pointer[_struct.RECT]],  # lprect
                           _type.BOOL]
    Rectangle: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # left
                          _type.c_int,  # top
                          _type.c_int,  # right
                          _type.c_int],  # bottom
                         _type.BOOL]
    RestoreDC: _Callable[[_type.HDC,  # hdc
                          _type.c_int],  # nSavedDC
                         _type.BOOL]
    ResetDCA: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.DEVMODEA]],  # lpdm
                        _type.HDC]
    ResetDCW: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.DEVMODEW]],  # lpdm
                        _type.HDC]
    RealizePalette: _Callable[[_type.HDC],  # hdc
                              _type.UINT]
    RemoveFontResourceA: _Callable[[_type.LPCSTR],  # lpFileName
                                   _type.BOOL]
    RemoveFontResourceW: _Callable[[_type.LPCWSTR],  # lpFileName
                                   _type.BOOL]
    RoundRect: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # left
                          _type.c_int,  # top
                          _type.c_int,  # right
                          _type.c_int,  # bottom
                          _type.c_int,  # width
                          _type.c_int],  # height
                         _type.BOOL]
    ResizePalette: _Callable[[_type.HPALETTE,  # hpal
                              _type.UINT],  # n
                             _type.BOOL]
    SaveDC: _Callable[[_type.HDC],  # hdc
                      _type.c_int]
    SelectClipRgn: _Callable[[_type.HDC,  # hdc
                              _type.HRGN],  # hrgn
                             _type.c_int]
    ExtSelectClipRgn: _Callable[[_type.HDC,  # hdc
                                 _type.HRGN,  # hrgn
                                 _type.c_int],  # mode
                                _type.c_int]
    SetMetaRgn: _Callable[[_type.HDC],  # hdc
                          _type.c_int]
    SelectObject: _Callable[[_type.HDC,  # hdc
                             _type.HGDIOBJ],  # h
                            _type.HGDIOBJ]
    SelectPalette: _Callable[[_type.HDC,  # hdc
                              _type.HPALETTE,  # hPal
                              _type.BOOL],  # bForceBkgd
                             _type.HPALETTE]
    SetBkColor: _Callable[[_type.HDC,  # hdc
                           _type.COLORREF],  # color
                          _type.COLORREF]
    SetDCBrushColor: _Callable[[_type.HDC,  # hdc
                                _type.COLORREF],  # color
                               _type.COLORREF]
    SetDCPenColor: _Callable[[_type.HDC,  # hdc
                              _type.COLORREF],  # color
                             _type.COLORREF]
    SetBkMode: _Callable[[_type.HDC,  # hdc
                          _type.c_int],  # mode
                         _type.c_int]
    SetBitmapBits: _Callable[[_type.HBITMAP,  # hbm
                              _type.DWORD,  # cb
                              _type.c_void_p],  # pvBits
                             _type.LONG]
    SetBoundsRect: _Callable[[_type.HDC,  # hdc
                              _Pointer[_struct.RECT],  # lprect
                              _type.UINT],  # flags
                             _type.UINT]
    SetDIBits: _Callable[[_type.HDC,  # hdc
                          _type.HBITMAP,  # hbm
                          _type.UINT,  # start
                          _type.UINT,  # cLines
                          _type.c_void_p,  # lpBits
                          _Pointer[_struct.BITMAPINFO],  # lpbmi
                          _type.UINT],  # ColorUse
                         _type.c_int]
    SetDIBitsToDevice: _Callable[[_type.HDC,  # hdc
                                  _type.c_int,  # xDest
                                  _type.c_int,  # yDest
                                  _type.DWORD,  # w
                                  _type.DWORD,  # h
                                  _type.c_int,  # xSrc
                                  _type.c_int,  # ySrc
                                  _type.UINT,  # StartScan
                                  _type.UINT,  # cLines
                                  _type.c_void_p,  # lpvBits
                                  _Pointer[_struct.BITMAPINFO],  # lpbmi
                                  _type.UINT],  # ColorUse
                                 _type.c_int]
    SetMapperFlags: _Callable[[_type.HDC,  # hdc
                               _type.DWORD],  # flags
                              _type.DWORD]
    SetGraphicsMode: _Callable[[_type.HDC,  # hdc
                                _type.c_int],  # iMode
                               _type.c_int]
    SetMapMode: _Callable[[_type.HDC,  # hdc
                           _type.c_int],  # iMode
                          _type.c_int]
    SetLayout: _Callable[[_type.HDC,  # hdc
                          _type.DWORD],  # l
                         _type.DWORD]
    GetLayout: _Callable[[_type.HDC],  # hdc
                         _type.DWORD]
    SetMetaFileBitsEx: _Callable[[_type.UINT,  # cbBuffer
                                  _Pointer[_type.BYTE]],  # lpData
                                 _type.HMETAFILE]
    SetPaletteEntries: _Callable[[_type.HPALETTE,  # hpal
                                  _type.UINT,  # iStart
                                  _type.UINT,  # cEntries
                                  _Pointer[_struct.PALETTEENTRY]],  # pPalEntries
                                 _type.UINT]
    SetPixel: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # x
                         _type.c_int,  # y
                         _type.COLORREF],  # color
                        _type.COLORREF]
    SetPixelV: _Callable[[_type.HDC,  # hdc
                          _type.c_int,  # x
                          _type.c_int,  # y
                          _type.COLORREF],  # color
                         _type.BOOL]
    SetPixelFormat: _Callable[[_type.HDC,  # hdc
                               _type.c_int,  # format
                               _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                              _type.BOOL]
    SetPolyFillMode: _Callable[[_type.HDC,  # hdc
                                _type.c_int],  # mode
                               _type.c_int]
    StretchBlt: _Callable[[_type.HDC,  # hdcDest
                           _type.c_int,  # xDest
                           _type.c_int,  # yDest
                           _type.c_int,  # wDest
                           _type.c_int,  # hDest
                           _type.HDC,  # hdcSrc
                           _type.c_int,  # xSrc
                           _type.c_int,  # ySrc
                           _type.c_int,  # wSrc
                           _type.c_int,  # hSrc
                           _type.DWORD],  # rop
                          _type.BOOL]
    SetRectRgn: _Callable[[_type.HRGN,  # hrgn
                           _type.c_int,  # left
                           _type.c_int,  # top
                           _type.c_int,  # right
                           _type.c_int],  # bottom
                          _type.BOOL]
    StretchDIBits: _Callable[[_type.HDC,  # hdc
                              _type.c_int,  # xDest
                              _type.c_int,  # yDest
                              _type.c_int,  # DestWidth
                              _type.c_int,  # DestHeight
                              _type.c_int,  # xSrc
                              _type.c_int,  # ySrc
                              _type.c_int,  # SrcWidth
                              _type.c_int,  # SrcHeight
                              _type.c_void_p,  # lpBits
                              _Pointer[_struct.BITMAPINFO],  # lpbmi
                              _type.UINT,  # iUsage
                              _type.DWORD],  # rop
                             _type.c_int]
    SetROP2: _Callable[[_type.HDC,  # hdc
                        _type.c_int],  # rop2
                       _type.c_int]
    SetStretchBltMode: _Callable[[_type.HDC,  # hdc
                                  _type.c_int],  # mode
                                 _type.c_int]
    SetSystemPaletteUse: _Callable[[_type.HDC,  # hdc
                                    _type.UINT],  # use
                                   _type.UINT]
    SetTextCharacterExtra: _Callable[[_type.HDC,  # hdc
                                      _type.c_int],  # extra
                                     _type.c_int]
    SetTextColor: _Callable[[_type.HDC,  # hdc
                             _type.COLORREF],  # color
                            _type.COLORREF]
    SetTextAlign: _Callable[[_type.HDC,  # hdc
                             _type.UINT],  # align
                            _type.UINT]
    SetTextJustification: _Callable[[_type.HDC,  # hdc
                                     _type.c_int,  # extra
                                     _type.c_int],  # count
                                    _type.BOOL]
    UpdateColors: _Callable[[_type.HDC],  # hdc
                            _type.BOOL]
    AlphaBlend: _Callable[[_type.HDC,  # hdcDest
                           _type.c_int,  # xoriginDest
                           _type.c_int,  # yoriginDest
                           _type.c_int,  # wDest
                           _type.c_int,  # hDest
                           _type.HDC,  # hdcSrc
                           _type.c_int,  # xoriginSrc
                           _type.c_int,  # yoriginSrc
                           _type.c_int,  # wSrc
                           _type.c_int,  # hSrc
                           _struct.BLENDFUNCTION],  # ftn
                          _type.BOOL]
    TransparentBlt: _Callable[[_type.HDC,  # hdcDest
                               _type.c_int,  # xoriginDest
                               _type.c_int,  # yoriginDest
                               _type.c_int,  # wDest
                               _type.c_int,  # hDest
                               _type.HDC,  # hdcSrc
                               _type.c_int,  # xoriginSrc
                               _type.c_int,  # yoriginSrc
                               _type.c_int,  # wSrc
                               _type.c_int,  # hSrc
                               _type.UINT],  # crTransparent
                              _type.BOOL]
    GradientFill: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.TRIVERTEX],  # pVertex
                             _type.ULONG,  # nVertex
                             _type.PVOID,  # pMesh
                             _type.ULONG,  # nMesh
                             _type.ULONG],  # ulMode
                            _type.BOOL]
    GdiAlphaBlend: _Callable[[_type.HDC,  # hdcDest
                              _type.c_int,  # xoriginDest
                              _type.c_int,  # yoriginDest
                              _type.c_int,  # wDest
                              _type.c_int,  # hDest
                              _type.HDC,  # hdcSrc
                              _type.c_int,  # xoriginSrc
                              _type.c_int,  # yoriginSrc
                              _type.c_int,  # wSrc
                              _type.c_int,  # hSrc
                              _struct.BLENDFUNCTION],  # ftn
                             _type.BOOL]
    GdiTransparentBlt: _Callable[[_type.HDC,  # hdcDest
                                  _type.c_int,  # xoriginDest
                                  _type.c_int,  # yoriginDest
                                  _type.c_int,  # wDest
                                  _type.c_int,  # hDest
                                  _type.HDC,  # hdcSrc
                                  _type.c_int,  # xoriginSrc
                                  _type.c_int,  # yoriginSrc
                                  _type.c_int,  # wSrc
                                  _type.c_int,  # hSrc
                                  _type.UINT],  # crTransparent
                                 _type.BOOL]
    GdiGradientFill: _Callable[[_type.HDC,  # hdc
                                _Pointer[_struct.TRIVERTEX],  # pVertex
                                _type.ULONG,  # nVertex
                                _type.PVOID,  # pMesh
                                _type.ULONG,  # nCount
                                _type.ULONG],  # ulMode
                               _type.BOOL]
    PlayMetaFileRecord: _Callable[[_type.HDC,  # hdc
                                   _Pointer[_struct.HANDLETABLE],  # lpHandleTable
                                   _Pointer[_struct.METARECORD],  # lpMR
                                   _type.UINT],  # noObjs
                                  _type.BOOL]
    CloseEnhMetaFile: _Callable[[_type.HDC],  # hdc
                                _type.HENHMETAFILE]
    CopyEnhMetaFileA: _Callable[[_type.HENHMETAFILE,  # hEnh
                                 _type.LPCSTR],  # lpFileName
                                _type.HENHMETAFILE]
    CopyEnhMetaFileW: _Callable[[_type.HENHMETAFILE,  # hEnh
                                 _type.LPCWSTR],  # lpFileName
                                _type.HENHMETAFILE]
    CreateEnhMetaFileA: _Callable[[_type.HDC,  # hdc
                                   _type.LPCSTR,  # lpFilename
                                   _Pointer[_struct.RECT],  # lprc
                                   _type.LPCSTR],  # lpDesc
                                  _type.HDC]
    CreateEnhMetaFileW: _Callable[[_type.HDC,  # hdc
                                   _type.LPCWSTR,  # lpFilename
                                   _Pointer[_struct.RECT],  # lprc
                                   _type.LPCWSTR],  # lpDesc
                                  _type.HDC]
    DeleteEnhMetaFile: _Callable[[_type.HENHMETAFILE],  # hmf
                                 _type.BOOL]
    GetEnhMetaFileA: _Callable[[_type.LPCSTR],  # lpName
                               _type.HENHMETAFILE]
    GetEnhMetaFileW: _Callable[[_type.LPCWSTR],  # lpName
                               _type.HENHMETAFILE]
    GetEnhMetaFileBits: _Callable[[_type.HENHMETAFILE,  # hEMF
                                   _type.UINT,  # nSize
                                   _Pointer[_type.BYTE]],  # lpData
                                  _type.UINT]
    GetEnhMetaFileDescriptionA: _Callable[[_type.HENHMETAFILE,  # hemf
                                           _type.UINT,  # cchBuffer
                                           _type.LPSTR],  # lpDescription
                                          _type.UINT]
    GetEnhMetaFileDescriptionW: _Callable[[_type.HENHMETAFILE,  # hemf
                                           _type.UINT,  # cchBuffer
                                           _type.LPWSTR],  # lpDescription
                                          _type.UINT]
    GetEnhMetaFileHeader: _Callable[[_type.HENHMETAFILE,  # hemf
                                     _type.UINT,  # nSize
                                     _Pointer[_struct.ENHMETAHEADER]],  # lpEnhMetaHeader
                                    _type.UINT]
    GetEnhMetaFilePaletteEntries: _Callable[[_type.HENHMETAFILE,  # hemf
                                             _type.UINT,  # nNumEntries
                                             _Pointer[_struct.PALETTEENTRY]],  # lpPaletteEntries
                                            _type.UINT]
    GetEnhMetaFilePixelFormat: _Callable[[_type.HENHMETAFILE,  # hemf
                                          _type.UINT,  # cbBuffer
                                          _Pointer[_struct.PIXELFORMATDESCRIPTOR]],  # ppfd
                                         _type.UINT]
    GetWinMetaFileBits: _Callable[[_type.HENHMETAFILE,  # hemf
                                   _type.UINT,  # cbData16
                                   _Pointer[_type.BYTE],  # pData16
                                   _type.INT,  # iMapMode
                                   _type.HDC],  # hdcRef
                                  _type.UINT]
    PlayEnhMetaFile: _Callable[[_type.HDC,  # hdc
                                _type.HENHMETAFILE,  # hmf
                                _Pointer[_struct.RECT]],  # lprect
                               _type.BOOL]
    PlayEnhMetaFileRecord: _Callable[[_type.HDC,  # hdc
                                      _Pointer[_struct.HANDLETABLE],  # pht
                                      _Pointer[_struct.ENHMETARECORD],  # pmr
                                      _type.UINT],  # cht
                                     _type.BOOL]
    SetEnhMetaFileBits: _Callable[[_type.UINT,  # nSize
                                   _Pointer[_type.BYTE]],  # pb
                                  _type.HENHMETAFILE]
    SetWinMetaFileBits: _Callable[[_type.UINT,  # nSize
                                   _Pointer[_type.BYTE],  # lpMeta16Data
                                   _type.HDC,  # hdcRef
                                   _Pointer[_struct.METAFILEPICT]],  # lpMFP
                                  _type.HENHMETAFILE]
    GdiComment: _Callable[[_type.HDC,  # hdc
                           _type.UINT,  # nSize
                           _Pointer[_type.BYTE]],  # lpData
                          _type.BOOL]
    GetTextMetricsA: _Callable[[_type.HDC,  # hdc
                                _Pointer[_struct.TEXTMETRICA]],  # lptm
                               _type.BOOL]
    GetTextMetricsW: _Callable[[_type.HDC,  # hdc
                                _Pointer[_struct.TEXTMETRICW]],  # lptm
                               _type.BOOL]
    AngleArc: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # x
                         _type.c_int,  # y
                         _type.DWORD,  # r
                         _type.FLOAT,  # StartAngle
                         _type.FLOAT],  # SweepAngle
                        _type.BOOL]
    PolyPolyline: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.POINT],  # apt
                             _Pointer[_type.DWORD],  # asz
                             _type.DWORD],  # csz
                            _type.BOOL]
    GetWorldTransform: _Callable[[_type.HDC,  # hdc
                                  _Pointer[_struct.XFORM]],  # lpxf
                                 _type.BOOL]
    SetWorldTransform: _Callable[[_type.HDC,  # hdc
                                  _Pointer[_struct.XFORM]],  # lpxf
                                 _type.BOOL]
    ModifyWorldTransform: _Callable[[_type.HDC,  # hdc
                                     _Pointer[_struct.XFORM],  # lpxf
                                     _type.DWORD],  # mode
                                    _type.BOOL]
    CombineTransform: _Callable[[_Pointer[_struct.XFORM],  # lpxfOut
                                 _Pointer[_struct.XFORM],  # lpxf1
                                 _Pointer[_struct.XFORM]],  # lpxf2
                                _type.BOOL]
    CreateDIBSection: _Callable[[_type.HDC,  # hdc
                                 _Pointer[_struct.BITMAPINFO],  # pbmi
                                 _type.UINT,  # usage
                                 _type.c_void_p,  # ppvBits
                                 _type.HANDLE,  # hSection
                                 _type.DWORD],  # offset
                                _type.HBITMAP]
    GetDIBColorTable: _Callable[[_type.HDC,  # hdc
                                 _type.UINT,  # iStart
                                 _type.UINT,  # cEntries
                                 _Pointer[_struct.RGBQUAD]],  # prgbq
                                _type.UINT]
    SetDIBColorTable: _Callable[[_type.HDC,  # hdc
                                 _type.UINT,  # iStart
                                 _type.UINT,  # cEntries
                                 _Pointer[_struct.RGBQUAD]],  # prgbq
                                _type.UINT]
    SetColorAdjustment: _Callable[[_type.HDC,  # hdc
                                   _Pointer[_struct.COLORADJUSTMENT]],  # lpca
                                  _type.BOOL]
    GetColorAdjustment: _Callable[[_type.HDC,  # hdc
                                   _Pointer[_struct.COLORADJUSTMENT]],  # lpca
                                  _type.BOOL]
    CreateHalftonePalette: _Callable[[_type.HDC],  # hdc
                                     _type.HPALETTE]
    StartDocA: _Callable[[_type.HDC,  # hdc
                          _Pointer[_struct.DOCINFOA]],  # lpdi
                         _type.c_int]
    StartDocW: _Callable[[_type.HDC,  # hdc
                          _Pointer[_struct.DOCINFOW]],  # lpdi
                         _type.c_int]
    EndDoc: _Callable[[_type.HDC],  # hdc
                      _type.c_int]
    StartPage: _Callable[[_type.HDC],  # hdc
                         _type.c_int]
    EndPage: _Callable[[_type.HDC],  # hdc
                       _type.c_int]
    AbortDoc: _Callable[[_type.HDC],  # hdc
                        _type.c_int]
    SetAbortProc: _Callable[[_type.HDC,  # hdc
                             _type.ABORTPROC],  # proc
                            _type.c_int]
    AbortPath: _Callable[[_type.HDC],  # hdc
                         _type.BOOL]
    ArcTo: _Callable[[_type.HDC,  # hdc
                      _type.c_int,  # left
                      _type.c_int,  # top
                      _type.c_int,  # right
                      _type.c_int,  # bottom
                      _type.c_int,  # xr1
                      _type.c_int,  # yr1
                      _type.c_int,  # xr2
                      _type.c_int],  # yr2
                     _type.BOOL]
    BeginPath: _Callable[[_type.HDC],  # hdc
                         _type.BOOL]
    CloseFigure: _Callable[[_type.HDC],  # hdc
                           _type.BOOL]
    EndPath: _Callable[[_type.HDC],  # hdc
                       _type.BOOL]
    FillPath: _Callable[[_type.HDC],  # hdc
                        _type.BOOL]
    FlattenPath: _Callable[[_type.HDC],  # hdc
                           _type.BOOL]
    GetPath: _Callable[[_type.HDC,  # hdc
                        _Pointer[_struct.POINT],  # apt
                        _Pointer[_type.BYTE],  # aj
                        _type.c_int],  # cpt
                       _type.c_int]
    PathToRegion: _Callable[[_type.HDC],  # hdc
                            _type.HRGN]
    PolyDraw: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.POINT],  # apt
                         _Pointer[_type.BYTE],  # aj
                         _type.c_int],  # cpt
                        _type.BOOL]
    SelectClipPath: _Callable[[_type.HDC,  # hdc
                               _type.c_int],  # mode
                              _type.BOOL]
    SetArcDirection: _Callable[[_type.HDC,  # hdc
                                _type.c_int],  # dir
                               _type.c_int]
    SetMiterLimit: _Callable[[_type.HDC,  # hdc
                              _type.FLOAT,  # limit
                              _Pointer[_type.FLOAT]],  # old
                             _type.BOOL]
    StrokeAndFillPath: _Callable[[_type.HDC],  # hdc
                                 _type.BOOL]
    StrokePath: _Callable[[_type.HDC],  # hdc
                          _type.BOOL]
    WidenPath: _Callable[[_type.HDC],  # hdc
                         _type.BOOL]
    ExtCreatePen: _Callable[[_type.DWORD,  # iPenStyle
                             _type.DWORD,  # cWidth
                             _Pointer[_struct.LOGBRUSH],  # plbrush
                             _type.DWORD,  # cStyle
                             _Pointer[_type.DWORD]],  # pstyle
                            _type.HPEN]
    GetMiterLimit: _Callable[[_type.HDC,  # hdc
                              _Pointer[_type.FLOAT]],  # plimit
                             _type.BOOL]
    GetArcDirection: _Callable[[_type.HDC],  # hdc
                               _type.c_int]
    GetObjectA: _Callable[[_type.HANDLE,  # h
                           _type.c_int,  # c
                           _type.LPVOID],  # pv
                          _type.c_int]
    GetObjectW: _Callable[[_type.HANDLE,  # h
                           _type.c_int,  # c
                           _type.LPVOID],  # pv
                          _type.c_int]
    MoveToEx: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # x
                         _type.c_int,  # y
                         _Pointer[_struct.POINT]],  # lppt
                        _type.BOOL]
    TextOutA: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # x
                         _type.c_int,  # y
                         _type.LPCSTR,  # lpString
                         _type.c_int],  # c
                        _type.BOOL]
    TextOutW: _Callable[[_type.HDC,  # hdc
                         _type.c_int,  # x
                         _type.c_int,  # y
                         _type.LPCWSTR,  # lpString
                         _type.c_int],  # c
                        _type.BOOL]
    ExtTextOutA: _Callable[[_type.HDC,  # hdc
                            _type.c_int,  # x
                            _type.c_int,  # y
                            _type.UINT,  # options
                            _Pointer[_struct.RECT],  # lprect
                            _type.LPCSTR,  # lpString
                            _type.UINT,  # c
                            _Pointer[_type.INT]],  # lpDx
                           _type.BOOL]
    ExtTextOutW: _Callable[[_type.HDC,  # hdc
                            _type.c_int,  # x
                            _type.c_int,  # y
                            _type.UINT,  # options
                            _Pointer[_struct.RECT],  # lprect
                            _type.LPCWSTR,  # lpString
                            _type.UINT,  # c
                            _Pointer[_type.INT]],  # lpDx
                           _type.BOOL]
    PolyTextOutA: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.POLYTEXTA],  # ppt
                             _type.c_int],  # nstrings
                            _type.BOOL]
    PolyTextOutW: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.POLYTEXTW],  # ppt
                             _type.c_int],  # nstrings
                            _type.BOOL]
    CreatePolygonRgn: _Callable[[_Pointer[_struct.POINT],  # pptl
                                 _type.c_int,  # cPoint
                                 _type.c_int],  # iMode
                                _type.HRGN]
    DPtoLP: _Callable[[_type.HDC,  # hdc
                       _Pointer[_struct.POINT],  # lppt
                       _type.c_int],  # c
                      _type.BOOL]
    LPtoDP: _Callable[[_type.HDC,  # hdc
                       _Pointer[_struct.POINT],  # lppt
                       _type.c_int],  # c
                      _type.BOOL]
    Polygon: _Callable[[_type.HDC,  # hdc
                        _Pointer[_struct.POINT],  # apt
                        _type.c_int],  # cpt
                       _type.BOOL]
    Polyline: _Callable[[_type.HDC,  # hdc
                         _Pointer[_struct.POINT],  # apt
                         _type.c_int],  # cpt
                        _type.BOOL]
    PolyBezier: _Callable[[_type.HDC,  # hdc
                           _Pointer[_struct.POINT],  # apt
                           _type.DWORD],  # cpt
                          _type.BOOL]
    PolyBezierTo: _Callable[[_type.HDC,  # hdc
                             _Pointer[_struct.POINT],  # apt
                             _type.DWORD],  # cpt
                            _type.BOOL]
    PolylineTo: _Callable[[_type.HDC,  # hdc
                           _Pointer[_struct.POINT],  # apt
                           _type.DWORD],  # cpt
                          _type.BOOL]
    SetViewportExtEx: _Callable[[_type.HDC,  # hdc
                                 _type.c_int,  # x
                                 _type.c_int,  # y
                                 _Pointer[_struct.SIZE]],  # lpsz
                                _type.BOOL]
    SetViewportOrgEx: _Callable[[_type.HDC,  # hdc
                                 _type.c_int,  # x
                                 _type.c_int,  # y
                                 _Pointer[_struct.POINT]],  # lppt
                                _type.BOOL]
    SetWindowExtEx: _Callable[[_type.HDC,  # hdc
                               _type.c_int,  # x
                               _type.c_int,  # y
                               _Pointer[_struct.SIZE]],  # lpsz
                              _type.BOOL]
    SetWindowOrgEx: _Callable[[_type.HDC,  # hdc
                               _type.c_int,  # x
                               _type.c_int,  # y
                               _Pointer[_struct.POINT]],  # lppt
                              _type.BOOL]
    OffsetViewportOrgEx: _Callable[[_type.HDC,  # hdc
                                    _type.c_int,  # x
                                    _type.c_int,  # y
                                    _Pointer[_struct.POINT]],  # lppt
                                   _type.BOOL]
    OffsetWindowOrgEx: _Callable[[_type.HDC,  # hdc
                                  _type.c_int,  # x
                                  _type.c_int,  # y
                                  _Pointer[_struct.POINT]],  # lppt
                                 _type.BOOL]
    ScaleViewportExtEx: _Callable[[_type.HDC,  # hdc
                                   _type.c_int,  # xn
                                   _type.c_int,  # dx
                                   _type.c_int,  # yn
                                   _type.c_int,  # yd
                                   _Pointer[_struct.SIZE]],  # lpsz
                                  _type.BOOL]
    ScaleWindowExtEx: _Callable[[_type.HDC,  # hdc
                                 _type.c_int,  # xn
                                 _type.c_int,  # xd
                                 _type.c_int,  # yn
                                 _type.c_int,  # yd
                                 _Pointer[_struct.SIZE]],  # lpsz
                                _type.BOOL]
    SetBitmapDimensionEx: _Callable[[_type.HBITMAP,  # hbm
                                     _type.c_int,  # w
                                     _type.c_int,  # h
                                     _Pointer[_struct.SIZE]],  # lpsz
                                    _type.BOOL]
    SetBrushOrgEx: _Callable[[_type.HDC,  # hdc
                              _type.c_int,  # x
                              _type.c_int,  # y
                              _Pointer[_struct.POINT]],  # lppt
                             _type.BOOL]
    GetTextFaceA: _Callable[[_type.HDC,  # hdc
                             _type.c_int,  # c
                             _type.LPSTR],  # lpName
                            _type.c_int]
    GetTextFaceW: _Callable[[_type.HDC,  # hdc
                             _type.c_int,  # c
                             _type.LPWSTR],  # lpName
                            _type.c_int]
    GetKerningPairsA: _Callable[[_type.HDC,  # hdc
                                 _type.DWORD,  # nPairs
                                 _Pointer[_struct.KERNINGPAIR]],  # lpKernPair
                                _type.DWORD]
    GetKerningPairsW: _Callable[[_type.HDC,  # hdc
                                 _type.DWORD,  # nPairs
                                 _Pointer[_struct.KERNINGPAIR]],  # lpKernPair
                                _type.DWORD]
    GetDCOrgEx: _Callable[[_type.HDC,  # hdc
                           _Pointer[_struct.POINT]],  # lppt
                          _type.BOOL]
    FixBrushOrgEx: _Callable[[_type.HDC,  # hdc
                              _type.c_int,  # x
                              _type.c_int,  # y
                              _Pointer[_struct.POINT]],  # ptl
                             _type.BOOL]
    UnrealizeObject: _Callable[[_type.HGDIOBJ],  # h
                               _type.BOOL]
    GdiFlush: _Callable[[],
                        _type.BOOL]
    GdiSetBatchLimit: _Callable[[_type.DWORD],  # dw
                                _type.DWORD]
    GdiGetBatchLimit: _Callable[[],
                                _type.DWORD]
    SetICMMode: _Callable[[_type.HDC,  # hdc
                           _type.c_int],  # mode
                          _type.c_int]
    CheckColorsInGamut: _Callable[[_type.HDC,  # hdc
                                   _Pointer[_struct.RGBTRIPLE],  # lpRGBTriple
                                   _type.LPVOID,  # dlpBuffer
                                   _type.DWORD],  # nCount
                                  _type.BOOL]
    GetColorSpace: _Callable[[_type.HDC],  # hdc
                             _type.HCOLORSPACE]
    GetLogColorSpaceA: _Callable[[_type.HCOLORSPACE,  # hColorSpace
                                  _Pointer[_struct.LOGCOLORSPACEA],  # lpBuffer
                                  _type.DWORD],  # nSize
                                 _type.BOOL]
    GetLogColorSpaceW: _Callable[[_type.HCOLORSPACE,  # hColorSpace
                                  _Pointer[_struct.LOGCOLORSPACEW],  # lpBuffer
                                  _type.DWORD],  # nSize
                                 _type.BOOL]
    CreateColorSpaceA: _Callable[[_Pointer[_struct.LOGCOLORSPACEA]],  # lplcs
                                 _type.HCOLORSPACE]
    CreateColorSpaceW: _Callable[[_Pointer[_struct.LOGCOLORSPACEW]],  # lplcs
                                 _type.HCOLORSPACE]
    SetColorSpace: _Callable[[_type.HDC,  # hdc
                              _type.HCOLORSPACE],  # hcs
                             _type.HCOLORSPACE]
    DeleteColorSpace: _Callable[[_type.HCOLORSPACE],  # hcs
                                _type.BOOL]
    GetICMProfileA: _Callable[[_type.HDC,  # hdc
                               _Pointer[_type.DWORD],  # pBufSize
                               _type.LPSTR],  # pszFilename
                              _type.BOOL]
    GetICMProfileW: _Callable[[_type.HDC,  # hdc
                               _Pointer[_type.DWORD],  # pBufSize
                               _type.LPWSTR],  # pszFilename
                              _type.BOOL]
    SetICMProfileA: _Callable[[_type.HDC,  # hdc
                               _type.LPSTR],  # lpFileName
                              _type.BOOL]
    SetICMProfileW: _Callable[[_type.HDC,  # hdc
                               _type.LPWSTR],  # lpFileName
                              _type.BOOL]
    GetDeviceGammaRamp: _Callable[[_type.HDC,  # hdc
                                   _type.LPVOID],  # lpRamp
                                  _type.BOOL]
    SetDeviceGammaRamp: _Callable[[_type.HDC,  # hdc
                                   _type.LPVOID],  # lpRamp
                                  _type.BOOL]
    ColorMatchToTarget: _Callable[[_type.HDC,  # hdc
                                   _type.HDC,  # hdcTarget
                                   _type.DWORD],  # action
                                  _type.BOOL]
    EnumICMProfilesA: _Callable[[_type.HDC,  # hdc
                                 _type.ICMENUMPROCA,  # proc
                                 _type.LPARAM],  # param
                                _type.c_int]
    EnumICMProfilesW: _Callable[[_type.HDC,  # hdc
                                 _type.ICMENUMPROCW,  # proc
                                 _type.LPARAM],  # param
                                _type.c_int]
    UpdateICMRegKeyA: _Callable[[_type.DWORD,  # reserved
                                 _type.LPSTR,  # lpszCMID
                                 _type.LPSTR,  # lpszFileName
                                 _type.UINT],  # command
                                _type.BOOL]
    UpdateICMRegKeyW: _Callable[[_type.DWORD,  # reserved
                                 _type.LPWSTR,  # lpszCMID
                                 _type.LPWSTR,  # lpszFileName
                                 _type.UINT],  # command
                                _type.BOOL]
    ColorCorrectPalette: _Callable[[_type.HDC,  # hdc
                                    _type.HPALETTE,  # hPal
                                    _type.DWORD,  # deFirst
                                    _type.DWORD],  # num
                                   _type.BOOL]
    wglCopyContext: _Callable[[_type.HGLRC,
                               _type.HGLRC,
                               _type.UINT],
                              _type.BOOL]
    wglCreateContext: _Callable[[_type.HDC],
                                _type.HGLRC]
    wglCreateLayerContext: _Callable[[_type.HDC,
                                      _type.c_int],
                                     _type.HGLRC]
    wglDeleteContext: _Callable[[_type.HGLRC],
                                _type.BOOL]
    wglGetCurrentContext: _Callable[[],
                                    _type.HGLRC]
    wglGetCurrentDC: _Callable[[],
                               _type.HDC]
    wglGetProcAddress: _Callable[[_type.LPCSTR],
                                 _type.PROC]
    wglMakeCurrent: _Callable[[_type.HDC,
                               _type.HGLRC],
                              _type.BOOL]
    wglShareLists: _Callable[[_type.HGLRC,
                              _type.HGLRC],
                             _type.BOOL]
    wglUseFontBitmapsA: _Callable[[_type.HDC,
                                   _type.DWORD,
                                   _type.DWORD,
                                   _type.DWORD],
                                  _type.BOOL]
    wglUseFontBitmapsW: _Callable[[_type.HDC,
                                   _type.DWORD,
                                   _type.DWORD,
                                   _type.DWORD],
                                  _type.BOOL]
    SwapBuffers: _Callable[[_type.HDC],
                           _type.BOOL]
    wglUseFontOutlinesA: _Callable[[_type.HDC,
                                    _type.DWORD,
                                    _type.DWORD,
                                    _type.DWORD,
                                    _type.FLOAT,
                                    _type.FLOAT,
                                    _type.c_int,
                                    _Pointer[_struct.GLYPHMETRICSFLOAT]],
                                   _type.BOOL]
    wglUseFontOutlinesW: _Callable[[_type.HDC,
                                    _type.DWORD,
                                    _type.DWORD,
                                    _type.DWORD,
                                    _type.FLOAT,
                                    _type.FLOAT,
                                    _type.c_int,
                                    _Pointer[_struct.GLYPHMETRICSFLOAT]],
                                   _type.BOOL]
    wglDescribeLayerPlane: _Callable[[_type.HDC,
                                      _type.c_int,
                                      _type.c_int,
                                      _type.UINT,
                                      _Pointer[_struct.LAYERPLANEDESCRIPTOR]],
                                     _type.BOOL]
    wglSetLayerPaletteEntries: _Callable[[_type.HDC,
                                          _type.c_int,
                                          _type.c_int,
                                          _type.c_int,
                                          _Pointer[_type.COLORREF]],
                                         _type.c_int]
    wglGetLayerPaletteEntries: _Callable[[_type.HDC,
                                          _type.c_int,
                                          _type.c_int,
                                          _type.c_int,
                                          _Pointer[_type.COLORREF]],
                                         _type.c_int]
    wglRealizeLayerPalette: _Callable[[_type.HDC,
                                       _type.c_int,
                                       _type.BOOL],
                                      _type.BOOL]
    wglSwapLayerBuffers: _Callable[[_type.HDC,
                                    _type.UINT],
                                   _type.BOOL]
    wglSwapMultipleBuffers: _Callable[[_type.UINT,
                                       _Pointer[_struct.WGLSWAP]],
                                      _type.DWORD]


class GdiPlus(_WinDLL):
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
    GdipLoadImageFromStream: _Callable[[_objidlbase.IStream,  # stream
                                        _Pointer[_type.GpImage]],  # image
                                       _enum.GpStatus]
    GdipLoadImageFromFile: _Callable[[_type.LPWSTR,  # filename
                                      _Pointer[_type.GpImage]],  # image
                                     _enum.GpStatus]
    GdipLoadImageFromStreamICM: _Callable[[_objidlbase.IStream,  # stream
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
                                      _objidlbase.IStream,  # stream
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
    GdipCreateBitmapFromStream: _Callable[[_objidlbase.IStream,  # stream
                                           _Pointer[_type.GpBitmap]],  # bitmap
                                          _enum.GpStatus]
    GdipCreateBitmapFromFile: _Callable[[_type.LPWSTR,  # filename
                                         _Pointer[_type.GpBitmap]],  # bitmap
                                        _enum.GpStatus]
    GdipCreateBitmapFromStreamICM: _Callable[[_objidlbase.IStream,  # stream
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
    GdipCreateBitmapFromDirectDrawSurface: _Callable[[_ddraw.IDirectDrawSurface7,  # surface
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
                                       _Pointer[_objidlbase.IStream]],  # stream
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
    GdipCreateMetafileFromStream: _Callable[[_objidlbase.IStream,  # stream
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
    GdipRecordMetafileStream: _Callable[[_objidlbase.IStream,  # stream
                                         _type.HDC,  # referenceHdc
                                         _enum.EmfType,  # type
                                         _Pointer[_struct.GpRectF],  # frameRect
                                         _enum.MetafileFrameUnit,  # frameUnit
                                         _type.LPWSTR,  # description
                                         _Pointer[_type.GpMetafile]],  # metafile
                                        _enum.GpStatus]
    GdipRecordMetafileStreamI: _Callable[[_objidlbase.IStream,  # stream
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
                                             _objidlbase.IStream,  # stream
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
class glu32(_WinDLL):
    # GLU
    gluErrorString: _Callable[[_type.GLenum],  # errCode
                              _Pointer[_type.GLubyte]]
    gluErrorUnicodeStringEXT: _Callable[[_type.GLenum],  # errCode
                                        _Pointer[_type.c_wchar_t]]
    gluGetString: _Callable[[_type.GLenum],  # name
                            _Pointer[_type.GLubyte]]
    gluOrtho2D: _Callable[[_type.GLdouble,  # left
                           _type.GLdouble,  # right
                           _type.GLdouble,  # bottom
                           _type.GLdouble],  # top
                          _type.c_void]
    gluPerspective: _Callable[[_type.GLdouble,  # fovy
                               _type.GLdouble,  # aspect
                               _type.GLdouble,  # zNear
                               _type.GLdouble],  # zFar
                              _type.c_void]
    gluPickMatrix: _Callable[[_type.GLdouble,  # x
                              _type.GLdouble,  # y
                              _type.GLdouble,  # width
                              _type.GLdouble,  # height
                              _type.GLint * 4],  # viewport
                             _type.c_void]
    gluLookAt: _Callable[[_type.GLdouble,  # eyex
                          _type.GLdouble,  # eyey
                          _type.GLdouble,  # eyez
                          _type.GLdouble,  # centerx
                          _type.GLdouble,  # centery
                          _type.GLdouble,  # centerz
                          _type.GLdouble,  # upx
                          _type.GLdouble,  # upy
                          _type.GLdouble],  # upz
                         _type.c_void]
    gluProject: _Callable[[_type.GLdouble,  # objx
                           _type.GLdouble,  # objy
                           _type.GLdouble,  # objz
                           _type.GLdouble * 16,  # modelMatrix
                           _type.GLdouble * 16,  # projMatrix
                           _type.GLint * 4,  # viewport
                           _Pointer[_type.GLdouble],  # winx
                           _Pointer[_type.GLdouble],  # winy
                           _Pointer[_type.GLdouble]],  # winz
                          _type.c_int]
    gluUnProject: _Callable[[_type.GLdouble,  # winx
                             _type.GLdouble,  # winy
                             _type.GLdouble,  # winz
                             _type.GLdouble * 16,  # modelMatrix
                             _type.GLdouble * 16,  # projMatrix
                             _type.GLint * 4,  # viewport
                             _Pointer[_type.GLdouble],  # objx
                             _Pointer[_type.GLdouble],  # objy
                             _Pointer[_type.GLdouble]],  # objz
                            _type.c_int]
    gluScaleImage: _Callable[[_type.GLenum,  # format
                              _type.GLint,  # widthin
                              _type.GLint,  # heightin
                              _type.GLenum,  # typein
                              _type.c_void_p,  # datain
                              _type.GLint,  # widthout
                              _type.GLint,  # heightout
                              _type.GLenum,  # typeout
                              _type.c_void_p],  # dataout
                             _type.c_int]
    gluBuild1DMipmaps: _Callable[[_type.GLenum,  # target
                                  _type.GLint,  # components
                                  _type.GLint,  # width
                                  _type.GLenum,  # format
                                  _type.GLenum,  # type
                                  _type.c_void_p],  # data
                                 _type.c_int]
    gluBuild2DMipmaps: _Callable[[_type.GLenum,  # target
                                  _type.GLint,  # components
                                  _type.GLint,  # width
                                  _type.GLint,  # height
                                  _type.GLenum,  # format
                                  _type.GLenum,  # type
                                  _type.c_void_p],  # data
                                 _type.c_int]
    gluNewQuadric: _Callable[[],
                             _Pointer[_type.GLUquadric]]
    gluDeleteQuadric: _Callable[[_Pointer[_type.GLUquadric]],  # state
                                _type.c_void]
    gluQuadricNormals: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                                  _type.GLenum],  # normals
                                 _type.c_void]
    gluQuadricTexture: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                                  _type.GLboolean],  # textureCoords
                                 _type.c_void]
    gluQuadricOrientation: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                                      _type.GLenum],  # orientation
                                     _type.c_void]
    gluQuadricDrawStyle: _Callable[[_Pointer[_type.GLUquadric],  # quadObject
                                    _type.GLenum],  # drawStyle
                                   _type.c_void]
    gluCylinder: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                            _type.GLdouble,  # baseRadius
                            _type.GLdouble,  # topRadius
                            _type.GLdouble,  # height
                            _type.GLint,  # slices
                            _type.GLint],  # stacks
                           _type.c_void]
    gluDisk: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                        _type.GLdouble,  # innerRadius
                        _type.GLdouble,  # outerRadius
                        _type.GLint,  # slices
                        _type.GLint],  # loops
                       _type.c_void]
    gluPartialDisk: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                               _type.GLdouble,  # innerRadius
                               _type.GLdouble,  # outerRadius
                               _type.GLint,  # slices
                               _type.GLint,  # loops
                               _type.GLdouble,  # startAngle
                               _type.GLdouble],  # sweepAngle
                              _type.c_void]
    gluSphere: _Callable[[_Pointer[_type.GLUquadric],  # qobj
                          _type.GLdouble,  # radius
                          _type.GLint,  # slices
                          _type.GLint],  # stacks
                         _type.c_void]
    gluNewTess: _Callable[[],
                          _Pointer[_type.GLUtesselator]]
    gluDeleteTess: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                             _type.c_void]
    gluTessBeginPolygon: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                                    _type.c_void_p],  # polygon_data
                                   _type.c_void]
    gluTessBeginContour: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                                   _type.c_void]
    gluTessVertex: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                              _type.GLdouble * 3,  # coords
                              _type.c_void_p],  # data
                             _type.c_void]
    gluTessEndContour: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                                 _type.c_void]
    gluTessEndPolygon: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                                 _type.c_void]
    gluTessProperty: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                                _type.GLenum,  # which
                                _type.GLdouble],  # value
                               _type.c_void]
    gluTessNormal: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                              _type.GLdouble,  # x
                              _type.GLdouble,  # y
                              _type.GLdouble],  # z
                             _type.c_void]
    gluGetTessProperty: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                                   _type.GLenum,  # which
                                   _Pointer[_type.GLdouble]],  # value
                                  _type.c_void]
    gluNewNurbsRenderer: _Callable[[],
                                   _Pointer[_type.GLUnurbs]]
    gluDeleteNurbsRenderer: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                                      _type.c_void]
    gluBeginSurface: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                               _type.c_void]
    gluBeginCurve: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                             _type.c_void]
    gluEndCurve: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                           _type.c_void]
    gluEndSurface: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                             _type.c_void]
    gluBeginTrim: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                            _type.c_void]
    gluEndTrim: _Callable[[_Pointer[_type.GLUnurbs]],  # nobj
                          _type.c_void]
    gluPwlCurve: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                            _type.GLint,  # count
                            _Pointer[_type.GLfloat],  # array
                            _type.GLint,  # stride
                            _type.GLenum],  # type
                           _type.c_void]
    gluNurbsCurve: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                              _type.GLint,  # nknots
                              _Pointer[_type.GLfloat],  # knot
                              _type.GLint,  # stride
                              _Pointer[_type.GLfloat],  # ctlarray
                              _type.GLint,  # order
                              _type.GLenum],  # type
                             _type.c_void]
    gluNurbsSurface: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                                _type.GLint,  # sknot_count
                                _Pointer[_type.c_float],  # sknot
                                _type.GLint,  # tknot_count
                                _Pointer[_type.GLfloat],  # tknot
                                _type.GLint,  # s_stride
                                _type.GLint,  # t_stride
                                _Pointer[_type.GLfloat],  # ctlarray
                                _type.GLint,  # sorder
                                _type.GLint,  # torder
                                _type.GLenum],  # type
                               _type.c_void]
    gluLoadSamplingMatrices: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                                        _type.GLfloat * 16,  # modelMatrix
                                        _type.GLfloat * 16,  # projMatrix
                                        _type.GLint * 4],  # viewport
                                       _type.c_void]
    gluNurbsProperty: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                                 _type.GLenum,  # property
                                 _type.GLfloat],  # value
                                _type.c_void]
    gluGetNurbsProperty: _Callable[[_Pointer[_type.GLUnurbs],  # nobj
                                    _type.GLenum,  # property
                                    _Pointer[_type.GLfloat]],  # value
                                   _type.c_void]
    gluBeginPolygon: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                               _type.c_void]
    gluNextContour: _Callable[[_Pointer[_type.GLUtesselator],  # tess
                               _type.GLenum],  # type
                              _type.c_void]
    gluEndPolygon: _Callable[[_Pointer[_type.GLUtesselator]],  # tess
                             _type.c_void]


# noinspection PyPep8Naming
class kernel32(_WinDLL):
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
class mscoree(_WinDLL):
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
class msimg32(_WinDLL):
    # wingdi
    AlphaBlend: _Callable[[_type.HDC,  # hdcDest
                           _type.c_int,  # xoriginDest
                           _type.c_int,  # yoriginDest
                           _type.c_int,  # wDest
                           _type.c_int,  # hDest
                           _type.HDC,  # hdcSrc
                           _type.c_int,  # xoriginSrc
                           _type.c_int,  # yoriginSrc
                           _type.c_int,  # wSrc
                           _type.c_int,  # hSrc
                           _struct.BLENDFUNCTION],  # ftn
                          _type.BOOL]


# noinspection PyPep8Naming
class ntdll(_WinDLL):
    NtQueryWnfStateData: _Callable[[_Pointer[_struct.WNF_STATE_NAME],  # StateName
                                    _Optional[_Pointer[_struct.WNF_TYPE_ID]],  # TypeId
                                    _Optional[_Pointer[_type.VOID]],  # ExplicitScope
                                    _Pointer[_type.WNF_CHANGE_STAMP],  # ChangeStamp
                                    _type.PVOID,  # Buffer
                                    _Pointer[_type.ULONG]],  # BufferSize
                                   _type.NTSTATUS]
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
class ole32(_WinDLL):
    # combaseapi
    CoUninitialize: _Callable[[],
                              _type.VOID]
    CoGetCurrentProcess: _Callable[[],
                                   _type.DWORD]
    CoInitializeEx: _Callable[[_Optional[_type.LPVOID],  # pvReserved
                               _type.DWORD],  # dwCoInit
                              _type.HRESULT]
    CoMarshalInterface: _Callable[[_objidlbase.IStream,  # pStm
                                   _Pointer[_struct.IID],  # riid
                                   _Unknwnbase.IUnknown,  # pUnk
                                   _type.DWORD,  # dwDestContext
                                   _Optional[_type.DWORD],  # pvDestContext
                                   _type.DWORD],  # mshlflags
                                  _type.HRESULT]
    CoUnmarshalInterface: _Callable[[_objidlbase.IStream,  # pStm
                                     _Pointer[_struct.IID],  # riid
                                     _type.LPVOID],  # ppv
                                    _type.HRESULT]
    CoMarshalHresult: _Callable[[_objidlbase.IStream,  # pstm
                                 _type.HRESULT],  # hresult
                                _type.HRESULT]
    CoUnmarshalHresult: _Callable[[_objidlbase.IStream,  # pstm
                                   _Pointer[_type.HRESULT]],  # phresult
                                  _type.HRESULT]
    CoIsHandlerConnected: _Callable[[_Unknwnbase.IUnknown],  # pUnk
                                    _type.BOOL]
    CoMarshalInterThreadInterfaceInStream: _Callable[[_Pointer[_struct.IID],  # riid
                                                      _Unknwnbase.IUnknown,  # pUnk
                                                      _Pointer[_objidlbase.IStream]],  # ppStm
                                                     _type.HRESULT]
    CoGetInterfaceAndReleaseStream: _Callable[[_objidlbase.IStream,  # pStm
                                               _Pointer[_struct.IID],  # riid
                                               _type.LPVOID],  # ppv
                                              _type.HRESULT]
    CoCreateFreeThreadedMarshaler: _Callable[[_Unknwnbase.IUnknown,  # punkOuter
                                              _Pointer[_Unknwnbase.IUnknown]],  # ppunkMarshal
                                             _type.HRESULT]
    CoFreeUnusedLibraries: _Callable[[],
                                     _type.c_void]
    CoFreeUnusedLibrariesEx: _Callable[[_type.DWORD,  # dwUnloadDelay
                                        _type.DWORD],  # dwReserved
                                       _type.c_void]
    CoDisconnectContext: _Callable[[_type.DWORD],  # dwTimeout
                                   _type.HRESULT]
    CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],  # rclsid
                                 _Optional[_Pointer[_Unknwnbase.IUnknown]],  # pUnkOuter
                                 _type.DWORD,  # dwClsContext
                                 _Pointer[_struct.IID],  # riid
                                 _type.LPVOID],  # ppv
                                _type.HRESULT]
    StringFromCLSID: _Callable[[_Pointer[_struct.CLSID],  # rclsid
                                _Pointer[_type.LPOLESTR]],  # lplpsz
                               _type.HRESULT]
    CLSIDFromString: _Callable[[_type.LPCOLESTR,  # lpsz
                                _Pointer[_struct.CLSID]],  # pclsid
                               _type.HRESULT]
    StringFromIID: _Callable[[_Pointer[_struct.IID],  # rclsid
                              _Pointer[_type.LPOLESTR]],  # lplpsz
                             _type.HRESULT]
    IIDFromString: _Callable[[_type.LPCOLESTR,  # lpsz
                              _Pointer[_struct.IID]],  # lpiid
                             _type.HRESULT]
    ProgIDFromCLSID: _Callable[[_Pointer[_struct.CLSID],  # clsid
                                _Pointer[_type.LPOLESTR]],  # lplpszProgID
                               _type.HRESULT]
    CLSIDFromProgID: _Callable[[_type.LPCOLESTR,  # lpszProgID
                                _Pointer[_struct.CLSID]],  # lpclsid
                               _type.HRESULT]
    StringFromGUID2: _Callable[[_Pointer[_struct.GUID],  # rguid
                                _type.LPOLESTR,  # lpsz
                                _type.c_int],  # cchMax
                               _type.c_int]
    CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],  # pguid
                            _type.HRESULT]
    DllCanUnloadNow: _Callable[[],
                               _type.HRESULT]
    CoTaskMemAlloc: _Callable[[_type.SIZE_T],  # cb
                              _type.LPVOID]
    CoTaskMemFree: _Callable[[_Optional[_type.LPVOID]],  # pv
                             _type.c_void]
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
class oleacc(_WinDLL):
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
class oleaut32(_WinDLL):
    # oleauto
    SysAllocString: _Callable[[_Optional[_type.LPCOLESTR]],  # psz
                              _type.BSTR]
    SysReAllocString: _Callable[[_Optional[_Pointer[_type.BSTR]],  # pbstr
                                 _Optional[_type.LPCOLESTR]],  # psz
                                _type.INT]
    SysAllocStringLen: _Callable[[_Optional[_type.LPCOLESTR],  # strIn
                                  _type.UINT],  # ui
                                 _type.BSTR]
    SysReAllocStringLen: _Callable[[_Optional[_Pointer[_type.BSTR]],  # pbstr
                                    _Optional[_type.LPCOLESTR],  # psz
                                    _type.c_uint],  # len
                                   _type.INT]
    SysAddRefString: _Callable[[_type.BSTR],  # bstrString
                               _type.HRESULT]
    SysReleaseString: _Callable[[_type.BSTR],  # bstrString
                                _type.c_void]
    SysFreeString: _Callable[[_Optional[_type.BSTR]],  # pbstr
                             _type.UINT]
    SysStringLen: _Callable[[_Optional[_type.BSTR]],  # pbstr
                            _type.UINT]
    SysStringByteLen: _Callable[[_Optional[_type.BSTR]],  # pbstr
                                _type.c_void]
    SysAllocStringByteLen: _Callable[[_Optional[_type.LPCSTR],  # psz
                                      _type.UINT],  # len
                                     _type.BSTR]
    # TODO
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
    OleSavePictureFile: _Callable[[_ocidl.IPictureDisp,
                                   _type.BSTR],
                                  _type.WINOLECTLAPI]


# noinspection PyPep8Naming
class opengl32(_WinDLL):
    # GL
    glAccum: _Callable[[_type.GLenum,  # op
                        _type.GLfloat],  # value
                       _type.c_int]
    glAlphaFunc: _Callable[[_type.GLenum,  # func
                            _type.GLclampf],  # ref
                           _type.c_int]
    glArrayElement: _Callable[[_type.GLint],  # i
                              _type.c_int]
    glBegin: _Callable[[_type.GLenum],  # mode
                       _type.c_int]
    glBindTexture: _Callable[[_type.GLenum,  # target
                              _type.GLuint],  # texture
                             _type.c_int]
    glBitmap: _Callable[[_type.GLsizei,  # width
                         _type.GLsizei,  # height
                         _type.GLfloat,  # xorig
                         _type.GLfloat,  # yorig
                         _type.GLfloat,  # xmove
                         _type.GLfloat,  # ymove
                         _Pointer[_type.GLubyte]],  # bitmap
                        _type.c_int]
    glBlendFunc: _Callable[[_type.GLenum,  # sfactor
                            _type.GLenum],  # dfactor
                           _type.c_int]
    glCallList: _Callable[[_type.GLuint],  # list
                          _type.c_int]
    glCallLists: _Callable[[_type.GLsizei,  # n
                            _type.GLenum,  # type
                            _Pointer[_type.GLvoid]],  # lists
                           _type.c_int]
    glClear: _Callable[[_type.GLbitfield],  # mask
                       _type.c_int]
    glClearAccum: _Callable[[_type.GLfloat,  # red
                             _type.GLfloat,  # green
                             _type.GLfloat,  # blue
                             _type.GLfloat],  # alpha
                            _type.c_int]
    glClearColor: _Callable[[_type.GLclampf,  # red
                             _type.GLclampf,  # green
                             _type.GLclampf,  # blue
                             _type.GLclampf],  # alpha
                            _type.c_int]
    glClearDepth: _Callable[[_type.GLclampd],  # depth
                            _type.c_int]
    glClearIndex: _Callable[[_type.GLfloat],  # c
                            _type.c_int]
    glClearStencil: _Callable[[_type.GLint],  # s
                              _type.c_int]
    glClipPlane: _Callable[[_type.GLenum,  # plane
                            _Pointer[_type.GLdouble]],  # equation
                           _type.c_int]
    glColor3b: _Callable[[_type.GLbyte,  # red
                          _type.GLbyte,  # green
                          _type.GLbyte],  # blue
                         _type.c_int]
    glColor3bv: _Callable[[_Pointer[_type.GLbyte]],  # v
                          _type.c_int]
    glColor3d: _Callable[[_type.GLdouble,  # red
                          _type.GLdouble,  # green
                          _type.GLdouble],  # blue
                         _type.c_int]
    glColor3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                          _type.c_int]
    glColor3f: _Callable[[_type.GLfloat,  # red
                          _type.GLfloat,  # green
                          _type.GLfloat],  # blue
                         _type.c_int]
    glColor3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                          _type.c_int]
    glColor3i: _Callable[[_type.GLint,  # red
                          _type.GLint,  # green
                          _type.GLint],  # blue
                         _type.c_int]
    glColor3iv: _Callable[[_Pointer[_type.GLint]],  # v
                          _type.c_int]
    glColor3s: _Callable[[_type.GLshort,  # red
                          _type.GLshort,  # green
                          _type.GLshort],  # blue
                         _type.c_int]
    glColor3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                          _type.c_int]
    glColor3ub: _Callable[[_type.GLubyte,  # red
                           _type.GLubyte,  # green
                           _type.GLubyte],  # blue
                          _type.c_int]
    glColor3ubv: _Callable[[_Pointer[_type.GLubyte]],  # v
                           _type.c_int]
    glColor3ui: _Callable[[_type.GLuint,  # red
                           _type.GLuint,  # green
                           _type.GLuint],  # blue
                          _type.c_int]
    glColor3uiv: _Callable[[_Pointer[_type.GLuint]],  # v
                           _type.c_int]
    glColor3us: _Callable[[_type.GLushort,  # red
                           _type.GLushort,  # green
                           _type.GLushort],  # blue
                          _type.c_int]
    glColor3usv: _Callable[[_Pointer[_type.GLushort]],  # v
                           _type.c_int]
    glColor4b: _Callable[[_type.GLbyte,  # red
                          _type.GLbyte,  # green
                          _type.GLbyte,  # blue
                          _type.GLbyte],  # alpha
                         _type.c_int]
    glColor4bv: _Callable[[_Pointer[_type.GLbyte]],  # v
                          _type.c_int]
    glColor4d: _Callable[[_type.GLdouble,  # red
                          _type.GLdouble,  # green
                          _type.GLdouble,  # blue
                          _type.GLdouble],  # alpha
                         _type.c_int]
    glColor4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                          _type.c_int]
    glColor4f: _Callable[[_type.GLfloat,  # red
                          _type.GLfloat,  # green
                          _type.GLfloat,  # blue
                          _type.GLfloat],  # alpha
                         _type.c_int]
    glColor4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                          _type.c_int]
    glColor4i: _Callable[[_type.GLint,  # red
                          _type.GLint,  # green
                          _type.GLint,  # blue
                          _type.GLint],  # alpha
                         _type.c_int]
    glColor4iv: _Callable[[_Pointer[_type.GLint]],  # v
                          _type.c_int]
    glColor4s: _Callable[[_type.GLshort,  # red
                          _type.GLshort,  # green
                          _type.GLshort,  # blue
                          _type.GLshort],  # alpha
                         _type.c_int]
    glColor4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                          _type.c_int]
    glColor4ub: _Callable[[_type.GLubyte,  # red
                           _type.GLubyte,  # green
                           _type.GLubyte,  # blue
                           _type.GLubyte],  # alpha
                          _type.c_int]
    glColor4ubv: _Callable[[_Pointer[_type.GLubyte]],  # v
                           _type.c_int]
    glColor4ui: _Callable[[_type.GLuint,  # red
                           _type.GLuint,  # green
                           _type.GLuint,  # blue
                           _type.GLuint],  # alpha
                          _type.c_int]
    glColor4uiv: _Callable[[_Pointer[_type.GLuint]],  # v
                           _type.c_int]
    glColor4us: _Callable[[_type.GLushort,  # red
                           _type.GLushort,  # green
                           _type.GLushort,  # blue
                           _type.GLushort],  # alpha
                          _type.c_int]
    glColor4usv: _Callable[[_Pointer[_type.GLushort]],  # v
                           _type.c_int]
    glColorMask: _Callable[[_type.GLboolean,  # red
                            _type.GLboolean,  # green
                            _type.GLboolean,  # blue
                            _type.GLboolean],  # alpha
                           _type.c_int]
    glColorMaterial: _Callable[[_type.GLenum,  # face
                                _type.GLenum],  # mode
                               _type.c_int]
    glColorPointer: _Callable[[_type.GLint,  # size
                               _type.GLenum,  # type
                               _type.GLsizei,  # stride
                               _Pointer[_type.GLvoid]],  # pointer
                              _type.c_int]
    glCopyPixels: _Callable[[_type.GLint,  # x
                             _type.GLint,  # y
                             _type.GLsizei,  # width
                             _type.GLsizei,  # height
                             _type.GLenum],  # type
                            _type.c_int]
    glCopyTexImage1D: _Callable[[_type.GLenum,  # target
                                 _type.GLint,  # level
                                 _type.GLenum,  # internalFormat
                                 _type.GLint,  # x
                                 _type.GLint,  # y
                                 _type.GLsizei,  # width
                                 _type.GLint],  # border
                                _type.c_int]
    glCopyTexImage2D: _Callable[[_type.GLenum,  # target
                                 _type.GLint,  # level
                                 _type.GLenum,  # internalFormat
                                 _type.GLint,  # x
                                 _type.GLint,  # y
                                 _type.GLsizei,  # width
                                 _type.GLsizei,  # height
                                 _type.GLint],  # border
                                _type.c_int]
    glCopyTexSubImage1D: _Callable[[_type.GLenum,  # target
                                    _type.GLint,  # level
                                    _type.GLint,  # xoffset
                                    _type.GLint,  # x
                                    _type.GLint,  # y
                                    _type.GLsizei],  # width
                                   _type.c_int]
    glCopyTexSubImage2D: _Callable[[_type.GLenum,  # target
                                    _type.GLint,  # level
                                    _type.GLint,  # xoffset
                                    _type.GLint,  # yoffset
                                    _type.GLint,  # x
                                    _type.GLint,  # y
                                    _type.GLsizei,  # width
                                    _type.GLsizei],  # height
                                   _type.c_int]
    glCullFace: _Callable[[_type.GLenum],  # mode
                          _type.c_int]
    glDeleteLists: _Callable[[_type.GLuint,  # list
                              _type.GLsizei],  # range
                             _type.c_int]
    glDeleteTextures: _Callable[[_type.GLsizei,  # n
                                 _Pointer[_type.GLuint]],  # textures
                                _type.c_int]
    glDepthFunc: _Callable[[_type.GLenum],  # func
                           _type.c_int]
    glDepthMask: _Callable[[_type.GLboolean],  # flag
                           _type.c_int]
    glDepthRange: _Callable[[_type.GLclampd,  # zNear
                             _type.GLclampd],  # zFar
                            _type.c_int]
    glDisable: _Callable[[_type.GLenum],  # cap
                         _type.c_int]
    glDisableClientState: _Callable[[_type.GLenum],  # array
                                    _type.c_int]
    glDrawArrays: _Callable[[_type.GLenum,  # mode
                             _type.GLint,  # first
                             _type.GLsizei],  # count
                            _type.c_int]
    glDrawBuffer: _Callable[[_type.GLenum],  # mode
                            _type.c_int]
    glDrawElements: _Callable[[_type.GLenum,  # mode
                               _type.GLsizei,  # count
                               _type.GLenum,  # type
                               _Pointer[_type.GLvoid]],  # indices
                              _type.c_int]
    glDrawPixels: _Callable[[_type.GLsizei,  # width
                             _type.GLsizei,  # height
                             _type.GLenum,  # format
                             _type.GLenum,  # type
                             _Pointer[_type.GLvoid]],  # pixels
                            _type.c_int]
    glEdgeFlag: _Callable[[_type.GLboolean],  # flag
                          _type.c_int]
    glEdgeFlagPointer: _Callable[[_type.GLsizei,  # stride
                                  _Pointer[_type.GLvoid]],  # pointer
                                 _type.c_int]
    glEdgeFlagv: _Callable[[_Pointer[_type.GLboolean]],  # flag
                           _type.c_int]
    glEnable: _Callable[[_type.GLenum],  # cap
                        _type.c_int]
    glEnableClientState: _Callable[[_type.GLenum],  # array
                                   _type.c_int]
    glEnd: _Callable[[],
                     _type.c_int]
    glEndList: _Callable[[],
                         _type.c_int]
    glEvalCoord1d: _Callable[[_type.GLdouble],  # u
                             _type.c_int]
    glEvalCoord1dv: _Callable[[_Pointer[_type.GLdouble]],  # u
                              _type.c_int]
    glEvalCoord1f: _Callable[[_type.GLfloat],  # u
                             _type.c_int]
    glEvalCoord1fv: _Callable[[_Pointer[_type.GLfloat]],  # u
                              _type.c_int]
    glEvalCoord2d: _Callable[[_type.GLdouble,  # u
                              _type.GLdouble],  # v
                             _type.c_int]
    glEvalCoord2dv: _Callable[[_Pointer[_type.GLdouble]],  # u
                              _type.c_int]
    glEvalCoord2f: _Callable[[_type.GLfloat,  # u
                              _type.GLfloat],  # v
                             _type.c_int]
    glEvalCoord2fv: _Callable[[_Pointer[_type.GLfloat]],  # u
                              _type.c_int]
    glEvalMesh1: _Callable[[_type.GLenum,  # mode
                            _type.GLint,  # i1
                            _type.GLint],  # i2
                           _type.c_int]
    glEvalMesh2: _Callable[[_type.GLenum,  # mode
                            _type.GLint,  # i1
                            _type.GLint,  # i2
                            _type.GLint,  # j1
                            _type.GLint],  # j2
                           _type.c_int]
    glEvalPoint1: _Callable[[_type.GLint],  # i
                            _type.c_int]
    glEvalPoint2: _Callable[[_type.GLint,  # i
                             _type.GLint],  # j
                            _type.c_int]
    glFeedbackBuffer: _Callable[[_type.GLsizei,  # size
                                 _type.GLenum,  # type
                                 _Pointer[_type.GLfloat]],  # buffer
                                _type.c_int]
    glFinish: _Callable[[],
                        _type.c_int]
    glFlush: _Callable[[],
                       _type.c_int]
    glFogf: _Callable[[_type.GLenum,  # pname
                       _type.GLfloat],  # param
                      _type.c_int]
    glFogfv: _Callable[[_type.GLenum,  # pname
                        _Pointer[_type.GLfloat]],  # params
                       _type.c_int]
    glFogi: _Callable[[_type.GLenum,  # pname
                       _type.GLint],  # param
                      _type.c_int]
    glFogiv: _Callable[[_type.GLenum,  # pname
                        _Pointer[_type.GLint]],  # params
                       _type.c_int]
    glFrontFace: _Callable[[_type.GLenum],  # mode
                           _type.c_int]
    glFrustum: _Callable[[_type.GLdouble,  # left
                          _type.GLdouble,  # right
                          _type.GLdouble,  # bottom
                          _type.GLdouble,  # top
                          _type.GLdouble,  # zNear
                          _type.GLdouble],  # zFar
                         _type.c_int]
    glGenTextures: _Callable[[_type.GLsizei,  # n
                              _Pointer[_type.GLuint]],  # textures
                             _type.c_int]
    glGetBooleanv: _Callable[[_type.GLenum,  # pname
                              _Pointer[_type.GLboolean]],  # params
                             _type.c_int]
    glGetClipPlane: _Callable[[_type.GLenum,  # plane
                               _Pointer[_type.GLdouble]],  # equation
                              _type.c_int]
    glGetDoublev: _Callable[[_type.GLenum,  # pname
                             _Pointer[_type.GLdouble]],  # params
                            _type.c_int]
    glGetFloatv: _Callable[[_type.GLenum,  # pname
                            _Pointer[_type.GLfloat]],  # params
                           _type.c_int]
    glGetIntegerv: _Callable[[_type.GLenum,  # pname
                              _Pointer[_type.GLint]],  # params
                             _type.c_int]
    glGetLightfv: _Callable[[_type.GLenum,  # light
                             _type.GLenum,  # pname
                             _Pointer[_type.GLfloat]],  # params
                            _type.c_int]
    glGetLightiv: _Callable[[_type.GLenum,  # light
                             _type.GLenum,  # pname
                             _Pointer[_type.GLint]],  # params
                            _type.c_int]
    glGetMapdv: _Callable[[_type.GLenum,  # target
                           _type.GLenum,  # query
                           _Pointer[_type.GLdouble]],  # v
                          _type.c_int]
    glGetMapfv: _Callable[[_type.GLenum,  # target
                           _type.GLenum,  # query
                           _Pointer[_type.GLfloat]],  # v
                          _type.c_int]
    glGetMapiv: _Callable[[_type.GLenum,  # target
                           _type.GLenum,  # query
                           _Pointer[_type.GLint]],  # v
                          _type.c_int]
    glGetMaterialfv: _Callable[[_type.GLenum,  # face
                                _type.GLenum,  # pname
                                _Pointer[_type.GLfloat]],  # params
                               _type.c_int]
    glGetMaterialiv: _Callable[[_type.GLenum,  # face
                                _type.GLenum,  # pname
                                _Pointer[_type.GLint]],  # params
                               _type.c_int]
    glGetPixelMapfv: _Callable[[_type.GLenum,  # map
                                _Pointer[_type.GLfloat]],  # values
                               _type.c_int]
    glGetPixelMapuiv: _Callable[[_type.GLenum,  # map
                                 _Pointer[_type.GLuint]],  # values
                                _type.c_int]
    glGetPixelMapusv: _Callable[[_type.GLenum,  # map
                                 _Pointer[_type.GLushort]],  # values
                                _type.c_int]
    glGetPointerv: _Callable[[_type.GLenum,  # pname
                              _Pointer[_Pointer[_type.GLvoid]]],  # params
                             _type.c_int]
    glGetPolygonStipple: _Callable[[_Pointer[_type.GLubyte]],  # mask
                                   _type.c_int]
    glGetTexEnvfv: _Callable[[_type.GLenum,  # target
                              _type.GLenum,  # pname
                              _Pointer[_type.GLfloat]],  # params
                             _type.c_int]
    glGetTexEnviv: _Callable[[_type.GLenum,  # target
                              _type.GLenum,  # pname
                              _Pointer[_type.GLint]],  # params
                             _type.c_int]
    glGetTexGendv: _Callable[[_type.GLenum,  # coord
                              _type.GLenum,  # pname
                              _Pointer[_type.GLdouble]],  # params
                             _type.c_int]
    glGetTexGenfv: _Callable[[_type.GLenum,  # coord
                              _type.GLenum,  # pname
                              _Pointer[_type.GLfloat]],  # params
                             _type.c_int]
    glGetTexGeniv: _Callable[[_type.GLenum,  # coord
                              _type.GLenum,  # pname
                              _Pointer[_type.GLint]],  # params
                             _type.c_int]
    glGetTexImage: _Callable[[_type.GLenum,  # target
                              _type.GLint,  # level
                              _type.GLenum,  # format
                              _type.GLenum,  # type
                              _Pointer[_type.GLvoid]],  # pixels
                             _type.c_int]
    glGetTexLevelParameterfv: _Callable[[_type.GLenum,  # target
                                         _type.GLint,  # level
                                         _type.GLenum,  # pname
                                         _Pointer[_type.GLfloat]],  # params
                                        _type.c_int]
    glGetTexLevelParameteriv: _Callable[[_type.GLenum,  # target
                                         _type.GLint,  # level
                                         _type.GLenum,  # pname
                                         _Pointer[_type.GLint]],  # params
                                        _type.c_int]
    glGetTexParameterfv: _Callable[[_type.GLenum,  # target
                                    _type.GLenum,  # pname
                                    _Pointer[_type.GLfloat]],  # params
                                   _type.c_int]
    glGetTexParameteriv: _Callable[[_type.GLenum,  # target
                                    _type.GLenum,  # pname
                                    _Pointer[_type.GLint]],  # params
                                   _type.c_int]
    glHint: _Callable[[_type.GLenum,  # target
                       _type.GLenum],  # mode
                      _type.c_int]
    glIndexMask: _Callable[[_type.GLuint],  # mask
                           _type.c_int]
    glIndexPointer: _Callable[[_type.GLenum,  # type
                               _type.GLsizei,  # stride
                               _Pointer[_type.GLvoid]],  # pointer
                              _type.c_int]
    glIndexd: _Callable[[_type.GLdouble],  # c
                        _type.c_int]
    glIndexdv: _Callable[[_Pointer[_type.GLdouble]],  # c
                         _type.c_int]
    glIndexf: _Callable[[_type.GLfloat],  # c
                        _type.c_int]
    glIndexfv: _Callable[[_Pointer[_type.GLfloat]],  # c
                         _type.c_int]
    glIndexi: _Callable[[_type.GLint],  # c
                        _type.c_int]
    glIndexiv: _Callable[[_Pointer[_type.GLint]],  # c
                         _type.c_int]
    glIndexs: _Callable[[_type.GLshort],  # c
                        _type.c_int]
    glIndexsv: _Callable[[_Pointer[_type.GLshort]],  # c
                         _type.c_int]
    glIndexub: _Callable[[_type.GLubyte],  # c
                         _type.c_int]
    glIndexubv: _Callable[[_Pointer[_type.GLubyte]],  # c
                          _type.c_int]
    glInitNames: _Callable[[],
                           _type.c_int]
    glInterleavedArrays: _Callable[[_type.GLenum,  # format
                                    _type.GLsizei,  # stride
                                    _Pointer[_type.GLvoid]],  # pointer
                                   _type.c_int]
    glLightModelf: _Callable[[_type.GLenum,  # pname
                              _type.GLfloat],  # param
                             _type.c_int]
    glLightModelfv: _Callable[[_type.GLenum,  # pname
                               _Pointer[_type.GLfloat]],  # params
                              _type.c_int]
    glLightModeli: _Callable[[_type.GLenum,  # pname
                              _type.GLint],  # param
                             _type.c_int]
    glLightModeliv: _Callable[[_type.GLenum,  # pname
                               _Pointer[_type.GLint]],  # params
                              _type.c_int]
    glLightf: _Callable[[_type.GLenum,  # light
                         _type.GLenum,  # pname
                         _type.GLfloat],  # param
                        _type.c_int]
    glLightfv: _Callable[[_type.GLenum,  # light
                          _type.GLenum,  # pname
                          _Pointer[_type.GLfloat]],  # params
                         _type.c_int]
    glLighti: _Callable[[_type.GLenum,  # light
                         _type.GLenum,  # pname
                         _type.GLint],  # param
                        _type.c_int]
    glLightiv: _Callable[[_type.GLenum,  # light
                          _type.GLenum,  # pname
                          _Pointer[_type.GLint]],  # params
                         _type.c_int]
    glLineStipple: _Callable[[_type.GLint,  # factor
                              _type.GLushort],  # pattern
                             _type.c_int]
    glLineWidth: _Callable[[_type.GLfloat],  # width
                           _type.c_int]
    glListBase: _Callable[[_type.GLuint],  # base
                          _type.c_int]
    glLoadIdentity: _Callable[[],
                              _type.c_int]
    glLoadMatrixd: _Callable[[_Pointer[_type.GLdouble]],  # m
                             _type.c_int]
    glLoadMatrixf: _Callable[[_Pointer[_type.GLfloat]],  # m
                             _type.c_int]
    glLoadName: _Callable[[_type.GLuint],  # name
                          _type.c_int]
    glLogicOp: _Callable[[_type.GLenum],  # opcode
                         _type.c_int]
    glMap1d: _Callable[[_type.GLenum,  # target
                        _type.GLdouble,  # u1
                        _type.GLdouble,  # u2
                        _type.GLint,  # stride
                        _type.GLint,  # order
                        _Pointer[_type.GLdouble]],  # points
                       _type.c_int]
    glMap1f: _Callable[[_type.GLenum,  # target
                        _type.GLfloat,  # u1
                        _type.GLfloat,  # u2
                        _type.GLint,  # stride
                        _type.GLint,  # order
                        _Pointer[_type.GLfloat]],  # points
                       _type.c_int]
    glMap2d: _Callable[[_type.GLenum,  # target
                        _type.GLdouble,  # u1
                        _type.GLdouble,  # u2
                        _type.GLint,  # ustride
                        _type.GLint,  # uorder
                        _type.GLdouble,  # v1
                        _type.GLdouble,  # v2
                        _type.GLint,  # vstride
                        _type.GLint,  # vorder
                        _Pointer[_type.GLdouble]],  # points
                       _type.c_int]
    glMap2f: _Callable[[_type.GLenum,  # target
                        _type.GLfloat,  # u1
                        _type.GLfloat,  # u2
                        _type.GLint,  # ustride
                        _type.GLint,  # uorder
                        _type.GLfloat,  # v1
                        _type.GLfloat,  # v2
                        _type.GLint,  # vstride
                        _type.GLint,  # vorder
                        _Pointer[_type.GLfloat]],  # points
                       _type.c_int]
    glMapGrid1d: _Callable[[_type.GLint,  # un
                            _type.GLdouble,  # u1
                            _type.GLdouble],  # u2
                           _type.c_int]
    glMapGrid1f: _Callable[[_type.GLint,  # un
                            _type.GLfloat,  # u1
                            _type.GLfloat],  # u2
                           _type.c_int]
    glMapGrid2d: _Callable[[_type.GLint,  # un
                            _type.GLdouble,  # u1
                            _type.GLdouble,  # u2
                            _type.GLint,  # vn
                            _type.GLdouble,  # v1
                            _type.GLdouble],  # v2
                           _type.c_int]
    glMapGrid2f: _Callable[[_type.GLint,  # un
                            _type.GLfloat,  # u1
                            _type.GLfloat,  # u2
                            _type.GLint,  # vn
                            _type.GLfloat,  # v1
                            _type.GLfloat],  # v2
                           _type.c_int]
    glMaterialf: _Callable[[_type.GLenum,  # face
                            _type.GLenum,  # pname
                            _type.GLfloat],  # param
                           _type.c_int]
    glMaterialfv: _Callable[[_type.GLenum,  # face
                             _type.GLenum,  # pname
                             _Pointer[_type.GLfloat]],  # params
                            _type.c_int]
    glMateriali: _Callable[[_type.GLenum,  # face
                            _type.GLenum,  # pname
                            _type.GLint],  # param
                           _type.c_int]
    glMaterialiv: _Callable[[_type.GLenum,  # face
                             _type.GLenum,  # pname
                             _Pointer[_type.GLint]],  # params
                            _type.c_int]
    glMatrixMode: _Callable[[_type.GLenum],  # mode
                            _type.c_int]
    glMultMatrixd: _Callable[[_Pointer[_type.GLdouble]],  # m
                             _type.c_int]
    glMultMatrixf: _Callable[[_Pointer[_type.GLfloat]],  # m
                             _type.c_int]
    glNewList: _Callable[[_type.GLuint,  # list
                          _type.GLenum],  # mode
                         _type.c_int]
    glNormal3b: _Callable[[_type.GLbyte,  # nx
                           _type.GLbyte,  # ny
                           _type.GLbyte],  # nz
                          _type.c_int]
    glNormal3bv: _Callable[[_Pointer[_type.GLbyte]],  # v
                           _type.c_int]
    glNormal3d: _Callable[[_type.GLdouble,  # nx
                           _type.GLdouble,  # ny
                           _type.GLdouble],  # nz
                          _type.c_int]
    glNormal3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                           _type.c_int]
    glNormal3f: _Callable[[_type.GLfloat,  # nx
                           _type.GLfloat,  # ny
                           _type.GLfloat],  # nz
                          _type.c_int]
    glNormal3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                           _type.c_int]
    glNormal3i: _Callable[[_type.GLint,  # nx
                           _type.GLint,  # ny
                           _type.GLint],  # nz
                          _type.c_int]
    glNormal3iv: _Callable[[_Pointer[_type.GLint]],  # v
                           _type.c_int]
    glNormal3s: _Callable[[_type.GLshort,  # nx
                           _type.GLshort,  # ny
                           _type.GLshort],  # nz
                          _type.c_int]
    glNormal3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                           _type.c_int]
    glNormalPointer: _Callable[[_type.GLenum,  # type
                                _type.GLsizei,  # stride
                                _Pointer[_type.GLvoid]],  # pointer
                               _type.c_int]
    glOrtho: _Callable[[_type.GLdouble,  # left
                        _type.GLdouble,  # right
                        _type.GLdouble,  # bottom
                        _type.GLdouble,  # top
                        _type.GLdouble,  # zNear
                        _type.GLdouble],  # zFar
                       _type.c_int]
    glPassThrough: _Callable[[_type.GLfloat],  # token
                             _type.c_int]
    glPixelMapfv: _Callable[[_type.GLenum,  # map
                             _type.GLsizei,  # mapsize
                             _Pointer[_type.GLfloat]],  # values
                            _type.c_int]
    glPixelMapuiv: _Callable[[_type.GLenum,  # map
                              _type.GLsizei,  # mapsize
                              _Pointer[_type.GLuint]],  # values
                             _type.c_int]
    glPixelMapusv: _Callable[[_type.GLenum,  # map
                              _type.GLsizei,  # mapsize
                              _Pointer[_type.GLushort]],  # values
                             _type.c_int]
    glPixelStoref: _Callable[[_type.GLenum,  # pname
                              _type.GLfloat],  # param
                             _type.c_int]
    glPixelStorei: _Callable[[_type.GLenum,  # pname
                              _type.GLint],  # param
                             _type.c_int]
    glPixelTransferf: _Callable[[_type.GLenum,  # pname
                                 _type.GLfloat],  # param
                                _type.c_int]
    glPixelTransferi: _Callable[[_type.GLenum,  # pname
                                 _type.GLint],  # param
                                _type.c_int]
    glPixelZoom: _Callable[[_type.GLfloat,  # xfactor
                            _type.GLfloat],  # yfactor
                           _type.c_int]
    glPointSize: _Callable[[_type.GLfloat],  # size
                           _type.c_int]
    glPolygonMode: _Callable[[_type.GLenum,  # face
                              _type.GLenum],  # mode
                             _type.c_int]
    glPolygonOffset: _Callable[[_type.GLfloat,  # factor
                                _type.GLfloat],  # units
                               _type.c_int]
    glPolygonStipple: _Callable[[_Pointer[_type.GLubyte]],  # mask
                                _type.c_int]
    glPopAttrib: _Callable[[],
                           _type.c_int]
    glPopClientAttrib: _Callable[[],
                                 _type.c_int]
    glPopMatrix: _Callable[[],
                           _type.c_int]
    glPopName: _Callable[[],
                         _type.c_int]
    glPrioritizeTextures: _Callable[[_type.GLsizei,  # n
                                     _Pointer[_type.GLuint],  # textures
                                     _Pointer[_type.GLclampf]],  # priorities
                                    _type.c_int]
    glPushAttrib: _Callable[[_type.GLbitfield],  # mask
                            _type.c_int]
    glPushClientAttrib: _Callable[[_type.GLbitfield],  # mask
                                  _type.c_int]
    glPushMatrix: _Callable[[],
                            _type.c_int]
    glPushName: _Callable[[_type.GLuint],  # name
                          _type.c_int]
    glRasterPos2d: _Callable[[_type.GLdouble,  # x
                              _type.GLdouble],  # y
                             _type.c_int]
    glRasterPos2dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                              _type.c_int]
    glRasterPos2f: _Callable[[_type.GLfloat,  # x
                              _type.GLfloat],  # y
                             _type.c_int]
    glRasterPos2fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                              _type.c_int]
    glRasterPos2i: _Callable[[_type.GLint,  # x
                              _type.GLint],  # y
                             _type.c_int]
    glRasterPos2iv: _Callable[[_Pointer[_type.GLint]],  # v
                              _type.c_int]
    glRasterPos2s: _Callable[[_type.GLshort,  # x
                              _type.GLshort],  # y
                             _type.c_int]
    glRasterPos2sv: _Callable[[_Pointer[_type.GLshort]],  # v
                              _type.c_int]
    glRasterPos3d: _Callable[[_type.GLdouble,  # x
                              _type.GLdouble,  # y
                              _type.GLdouble],  # z
                             _type.c_int]
    glRasterPos3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                              _type.c_int]
    glRasterPos3f: _Callable[[_type.GLfloat,  # x
                              _type.GLfloat,  # y
                              _type.GLfloat],  # z
                             _type.c_int]
    glRasterPos3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                              _type.c_int]
    glRasterPos3i: _Callable[[_type.GLint,  # x
                              _type.GLint,  # y
                              _type.GLint],  # z
                             _type.c_int]
    glRasterPos3iv: _Callable[[_Pointer[_type.GLint]],  # v
                              _type.c_int]
    glRasterPos3s: _Callable[[_type.GLshort,  # x
                              _type.GLshort,  # y
                              _type.GLshort],  # z
                             _type.c_int]
    glRasterPos3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                              _type.c_int]
    glRasterPos4d: _Callable[[_type.GLdouble,  # x
                              _type.GLdouble,  # y
                              _type.GLdouble,  # z
                              _type.GLdouble],  # w
                             _type.c_int]
    glRasterPos4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                              _type.c_int]
    glRasterPos4f: _Callable[[_type.GLfloat,  # x
                              _type.GLfloat,  # y
                              _type.GLfloat,  # z
                              _type.GLfloat],  # w
                             _type.c_int]
    glRasterPos4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                              _type.c_int]
    glRasterPos4i: _Callable[[_type.GLint,  # x
                              _type.GLint,  # y
                              _type.GLint,  # z
                              _type.GLint],  # w
                             _type.c_int]
    glRasterPos4iv: _Callable[[_Pointer[_type.GLint]],  # v
                              _type.c_int]
    glRasterPos4s: _Callable[[_type.GLshort,  # x
                              _type.GLshort,  # y
                              _type.GLshort,  # z
                              _type.GLshort],  # w
                             _type.c_int]
    glRasterPos4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                              _type.c_int]
    glReadBuffer: _Callable[[_type.GLenum],  # mode
                            _type.c_int]
    glReadPixels: _Callable[[_type.GLint,  # x
                             _type.GLint,  # y
                             _type.GLsizei,  # width
                             _type.GLsizei,  # height
                             _type.GLenum,  # format
                             _type.GLenum,  # type
                             _Pointer[_type.GLvoid]],  # pixels
                            _type.c_int]
    glRectd: _Callable[[_type.GLdouble,  # x1
                        _type.GLdouble,  # y1
                        _type.GLdouble,  # x2
                        _type.GLdouble],  # y2
                       _type.c_int]
    glRectdv: _Callable[[_Pointer[_type.GLdouble],  # v1
                         _Pointer[_type.GLdouble]],  # v2
                        _type.c_int]
    glRectf: _Callable[[_type.GLfloat,  # x1
                        _type.GLfloat,  # y1
                        _type.GLfloat,  # x2
                        _type.GLfloat],  # y2
                       _type.c_int]
    glRectfv: _Callable[[_Pointer[_type.GLfloat],  # v1
                         _Pointer[_type.GLfloat]],  # v2
                        _type.c_int]
    glRecti: _Callable[[_type.GLint,  # x1
                        _type.GLint,  # y1
                        _type.GLint,  # x2
                        _type.GLint],  # y2
                       _type.c_int]
    glRectiv: _Callable[[_Pointer[_type.GLint],  # v1
                         _Pointer[_type.GLint]],  # v2
                        _type.c_int]
    glRects: _Callable[[_type.GLshort,  # x1
                        _type.GLshort,  # y1
                        _type.GLshort,  # x2
                        _type.GLshort],  # y2
                       _type.c_int]
    glRectsv: _Callable[[_Pointer[_type.GLshort],  # v1
                         _Pointer[_type.GLshort]],  # v2
                        _type.c_int]
    glRotated: _Callable[[_type.GLdouble,  # angle
                          _type.GLdouble,  # x
                          _type.GLdouble,  # y
                          _type.GLdouble],  # z
                         _type.c_int]
    glRotatef: _Callable[[_type.GLfloat,  # angle
                          _type.GLfloat,  # x
                          _type.GLfloat,  # y
                          _type.GLfloat],  # z
                         _type.c_int]
    glScaled: _Callable[[_type.GLdouble,  # x
                         _type.GLdouble,  # y
                         _type.GLdouble],  # z
                        _type.c_int]
    glScalef: _Callable[[_type.GLfloat,  # x
                         _type.GLfloat,  # y
                         _type.GLfloat],  # z
                        _type.c_int]
    glScissor: _Callable[[_type.GLint,  # x
                          _type.GLint,  # y
                          _type.GLsizei,  # width
                          _type.GLsizei],  # height
                         _type.c_int]
    glSelectBuffer: _Callable[[_type.GLsizei,  # size
                               _Pointer[_type.GLuint]],  # buffer
                              _type.c_int]
    glShadeModel: _Callable[[_type.GLenum],  # mode
                            _type.c_int]
    glStencilFunc: _Callable[[_type.GLenum,  # func
                              _type.GLint,  # ref
                              _type.GLuint],  # mask
                             _type.c_int]
    glStencilMask: _Callable[[_type.GLuint],  # mask
                             _type.c_int]
    glStencilOp: _Callable[[_type.GLenum,  # fail
                            _type.GLenum,  # zfail
                            _type.GLenum],  # zpass
                           _type.c_int]
    glTexCoord1d: _Callable[[_type.GLdouble],  # s
                            _type.c_int]
    glTexCoord1dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                             _type.c_int]
    glTexCoord1f: _Callable[[_type.GLfloat],  # s
                            _type.c_int]
    glTexCoord1fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                             _type.c_int]
    glTexCoord1i: _Callable[[_type.GLint],  # s
                            _type.c_int]
    glTexCoord1iv: _Callable[[_Pointer[_type.GLint]],  # v
                             _type.c_int]
    glTexCoord1s: _Callable[[_type.GLshort],  # s
                            _type.c_int]
    glTexCoord1sv: _Callable[[_Pointer[_type.GLshort]],  # v
                             _type.c_int]
    glTexCoord2d: _Callable[[_type.GLdouble,  # s
                             _type.GLdouble],  # t
                            _type.c_int]
    glTexCoord2dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                             _type.c_int]
    glTexCoord2f: _Callable[[_type.GLfloat,  # s
                             _type.GLfloat],  # t
                            _type.c_int]
    glTexCoord2fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                             _type.c_int]
    glTexCoord2i: _Callable[[_type.GLint,  # s
                             _type.GLint],  # t
                            _type.c_int]
    glTexCoord2iv: _Callable[[_Pointer[_type.GLint]],  # v
                             _type.c_int]
    glTexCoord2s: _Callable[[_type.GLshort,  # s
                             _type.GLshort],  # t
                            _type.c_int]
    glTexCoord2sv: _Callable[[_Pointer[_type.GLshort]],  # v
                             _type.c_int]
    glTexCoord3d: _Callable[[_type.GLdouble,  # s
                             _type.GLdouble,  # t
                             _type.GLdouble],  # r
                            _type.c_int]
    glTexCoord3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                             _type.c_int]
    glTexCoord3f: _Callable[[_type.GLfloat,  # s
                             _type.GLfloat,  # t
                             _type.GLfloat],  # r
                            _type.c_int]
    glTexCoord3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                             _type.c_int]
    glTexCoord3i: _Callable[[_type.GLint,  # s
                             _type.GLint,  # t
                             _type.GLint],  # r
                            _type.c_int]
    glTexCoord3iv: _Callable[[_Pointer[_type.GLint]],  # v
                             _type.c_int]
    glTexCoord3s: _Callable[[_type.GLshort,  # s
                             _type.GLshort,  # t
                             _type.GLshort],  # r
                            _type.c_int]
    glTexCoord3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                             _type.c_int]
    glTexCoord4d: _Callable[[_type.GLdouble,  # s
                             _type.GLdouble,  # t
                             _type.GLdouble,  # r
                             _type.GLdouble],  # q
                            _type.c_int]
    glTexCoord4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                             _type.c_int]
    glTexCoord4f: _Callable[[_type.GLfloat,  # s
                             _type.GLfloat,  # t
                             _type.GLfloat,  # r
                             _type.GLfloat],  # q
                            _type.c_int]
    glTexCoord4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                             _type.c_int]
    glTexCoord4i: _Callable[[_type.GLint,  # s
                             _type.GLint,  # t
                             _type.GLint,  # r
                             _type.GLint],  # q
                            _type.c_int]
    glTexCoord4iv: _Callable[[_Pointer[_type.GLint]],  # v
                             _type.c_int]
    glTexCoord4s: _Callable[[_type.GLshort,  # s
                             _type.GLshort,  # t
                             _type.GLshort,  # r
                             _type.GLshort],  # q
                            _type.c_int]
    glTexCoord4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                             _type.c_int]
    glTexCoordPointer: _Callable[[_type.GLint,  # size
                                  _type.GLenum,  # type
                                  _type.GLsizei,  # stride
                                  _Pointer[_type.GLvoid]],  # pointer
                                 _type.c_int]
    glTexEnvf: _Callable[[_type.GLenum,  # target
                          _type.GLenum,  # pname
                          _type.GLfloat],  # param
                         _type.c_int]
    glTexEnvfv: _Callable[[_type.GLenum,  # target
                           _type.GLenum,  # pname
                           _Pointer[_type.GLfloat]],  # params
                          _type.c_int]
    glTexEnvi: _Callable[[_type.GLenum,  # target
                          _type.GLenum,  # pname
                          _type.GLint],  # param
                         _type.c_int]
    glTexEnviv: _Callable[[_type.GLenum,  # target
                           _type.GLenum,  # pname
                           _Pointer[_type.GLint]],  # params
                          _type.c_int]
    glTexGend: _Callable[[_type.GLenum,  # coord
                          _type.GLenum,  # pname
                          _type.GLdouble],  # param
                         _type.c_int]
    glTexGendv: _Callable[[_type.GLenum,  # coord
                           _type.GLenum,  # pname
                           _Pointer[_type.GLdouble]],  # params
                          _type.c_int]
    glTexGenf: _Callable[[_type.GLenum,  # coord
                          _type.GLenum,  # pname
                          _type.GLfloat],  # param
                         _type.c_int]
    glTexGenfv: _Callable[[_type.GLenum,  # coord
                           _type.GLenum,  # pname
                           _Pointer[_type.GLfloat]],  # params
                          _type.c_int]
    glTexGeni: _Callable[[_type.GLenum,  # coord
                          _type.GLenum,  # pname
                          _type.GLint],  # param
                         _type.c_int]
    glTexGeniv: _Callable[[_type.GLenum,  # coord
                           _type.GLenum,  # pname
                           _Pointer[_type.GLint]],  # params
                          _type.c_int]
    glTexImage1D: _Callable[[_type.GLenum,  # target
                             _type.GLint,  # level
                             _type.GLint,  # internalformat
                             _type.GLsizei,  # width
                             _type.GLint,  # border
                             _type.GLenum,  # format
                             _type.GLenum,  # type
                             _Pointer[_type.GLvoid]],  # pixels
                            _type.c_int]
    glTexImage2D: _Callable[[_type.GLenum,  # target
                             _type.GLint,  # level
                             _type.GLint,  # internalformat
                             _type.GLsizei,  # width
                             _type.GLsizei,  # height
                             _type.GLint,  # border
                             _type.GLenum,  # format
                             _type.GLenum,  # type
                             _Pointer[_type.GLvoid]],  # pixels
                            _type.c_int]
    glTexParameterf: _Callable[[_type.GLenum,  # target
                                _type.GLenum,  # pname
                                _type.GLfloat],  # param
                               _type.c_int]
    glTexParameterfv: _Callable[[_type.GLenum,  # target
                                 _type.GLenum,  # pname
                                 _Pointer[_type.GLfloat]],  # params
                                _type.c_int]
    glTexParameteri: _Callable[[_type.GLenum,  # target
                                _type.GLenum,  # pname
                                _type.GLint],  # param
                               _type.c_int]
    glTexParameteriv: _Callable[[_type.GLenum,  # target
                                 _type.GLenum,  # pname
                                 _Pointer[_type.GLint]],  # params
                                _type.c_int]
    glTexSubImage1D: _Callable[[_type.GLenum,  # target
                                _type.GLint,  # level
                                _type.GLint,  # xoffset
                                _type.GLsizei,  # width
                                _type.GLenum,  # format
                                _type.GLenum,  # type
                                _Pointer[_type.GLvoid]],  # pixels
                               _type.c_int]
    glTexSubImage2D: _Callable[[_type.GLenum,  # target
                                _type.GLint,  # level
                                _type.GLint,  # xoffset
                                _type.GLint,  # yoffset
                                _type.GLsizei,  # width
                                _type.GLsizei,  # height
                                _type.GLenum,  # format
                                _type.GLenum,  # type
                                _Pointer[_type.GLvoid]],  # pixels
                               _type.c_int]
    glTranslated: _Callable[[_type.GLdouble,  # x
                             _type.GLdouble,  # y
                             _type.GLdouble],  # z
                            _type.c_int]
    glTranslatef: _Callable[[_type.GLfloat,  # x
                             _type.GLfloat,  # y
                             _type.GLfloat],  # z
                            _type.c_int]
    glVertex2d: _Callable[[_type.GLdouble,  # x
                           _type.GLdouble],  # y
                          _type.c_int]
    glVertex2dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                           _type.c_int]
    glVertex2f: _Callable[[_type.GLfloat,  # x
                           _type.GLfloat],  # y
                          _type.c_int]
    glVertex2fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                           _type.c_int]
    glVertex2i: _Callable[[_type.GLint,  # x
                           _type.GLint],  # y
                          _type.c_int]
    glVertex2iv: _Callable[[_Pointer[_type.GLint]],  # v
                           _type.c_int]
    glVertex2s: _Callable[[_type.GLshort,  # x
                           _type.GLshort],  # y
                          _type.c_int]
    glVertex2sv: _Callable[[_Pointer[_type.GLshort]],  # v
                           _type.c_int]
    glVertex3d: _Callable[[_type.GLdouble,  # x
                           _type.GLdouble,  # y
                           _type.GLdouble],  # z
                          _type.c_int]
    glVertex3dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                           _type.c_int]
    glVertex3f: _Callable[[_type.GLfloat,  # x
                           _type.GLfloat,  # y
                           _type.GLfloat],  # z
                          _type.c_int]
    glVertex3fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                           _type.c_int]
    glVertex3i: _Callable[[_type.GLint,  # x
                           _type.GLint,  # y
                           _type.GLint],  # z
                          _type.c_int]
    glVertex3iv: _Callable[[_Pointer[_type.GLint]],  # v
                           _type.c_int]
    glVertex3s: _Callable[[_type.GLshort,  # x
                           _type.GLshort,  # y
                           _type.GLshort],  # z
                          _type.c_int]
    glVertex3sv: _Callable[[_Pointer[_type.GLshort]],  # v
                           _type.c_int]
    glVertex4d: _Callable[[_type.GLdouble,  # x
                           _type.GLdouble,  # y
                           _type.GLdouble,  # z
                           _type.GLdouble],  # w
                          _type.c_int]
    glVertex4dv: _Callable[[_Pointer[_type.GLdouble]],  # v
                           _type.c_int]
    glVertex4f: _Callable[[_type.GLfloat,  # x
                           _type.GLfloat,  # y
                           _type.GLfloat,  # z
                           _type.GLfloat],  # w
                          _type.c_int]
    glVertex4fv: _Callable[[_Pointer[_type.GLfloat]],  # v
                           _type.c_int]
    glVertex4i: _Callable[[_type.GLint,  # x
                           _type.GLint,  # y
                           _type.GLint,  # z
                           _type.GLint],  # w
                          _type.c_int]
    glVertex4iv: _Callable[[_Pointer[_type.GLint]],  # v
                           _type.c_int]
    glVertex4s: _Callable[[_type.GLshort,  # x
                           _type.GLshort,  # y
                           _type.GLshort,  # z
                           _type.GLshort],  # w
                          _type.c_int]
    glVertex4sv: _Callable[[_Pointer[_type.GLshort]],  # v
                           _type.c_int]
    glVertexPointer: _Callable[[_type.GLint,  # size
                                _type.GLenum,  # type
                                _type.GLsizei,  # stride
                                _Pointer[_type.GLvoid]],  # pointer
                               _type.c_int]
    glViewport: _Callable[[_type.GLint,  # x
                           _type.GLint,  # y
                           _type.GLsizei,  # width
                           _type.GLsizei],  # height
                          _type.c_int]


# noinspection PyPep8Naming
class psapi(_WinDLL):
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
class setupapi(_WinDLL):
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


class SHCore(_WinDLL):
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
class shdocvw(_WinDLL):
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]


# noinspection PyPep8Naming
class shell32(_WinDLL):
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 703
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 704
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    # shellapi
    SHGetFileInfoA: _Callable[[_type.LPCSTR,  # pszPath
                               _type.DWORD,  # dwFileAttributes
                               _Pointer[_struct.SHFILEINFOA],  # psfi
                               _type.UINT,  # cbFileInfo
                               _type.UINT],  # uFlags
                              _type.DWORD_PTR]
    SHGetFileInfoW: _Callable[[_type.LPCWSTR,  # pszPath
                               _type.DWORD,  # dwFileAttributes
                               _Pointer[_struct.SHFILEINFOW],  # psfi
                               _type.UINT,  # cbFileInfo
                               _type.UINT],  # uFlags
                              _type.DWORD_PTR]
    # TODO
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
    ILAppendID: _Callable[[_Optional[_Pointer[_struct.ITEMIDLIST]],  # pidl
                           _Pointer[_struct.SHITEMID],  # pmkid
                           _type.BOOL],  # fAppend
                          _Pointer[_struct.ITEMIDLIST]]
    SHGetPathFromIDListEx: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                      _type.PWSTR,  # pszPath
                                      _type.DWORD,  # cchPath
                                      _type.GPFIDL_FLAGS],  # uOpts
                                     _type.BOOL]
    SHGetPathFromIDListA: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                     _type.LPSTR],  # pszPath
                                    _type.BOOL]
    SHGetPathFromIDListW: _Callable[[_Pointer[_struct.ITEMIDLIST],  # pidl
                                     _type.LPWSTR],  # pszPath
                                    _type.BOOL]
    SHCreateDirectory: _Callable[[_Optional[_type.HWND],  # hwnd
                                  _type.PCWSTR],  # pszPath
                                 _type.c_int]
    SHCreateDirectoryExA: _Callable[[_Optional[_type.HWND],  # hwnd
                                     _type.LPCSTR,  # pszPath
                                     _Pointer[_struct.SECURITY_ATTRIBUTES]],  # psa
                                    _type.c_int]
    SHCreateDirectoryExW: _Callable[[_Optional[_type.HWND],  # hwnd
                                     _type.LPCWSTR,  # pszPath
                                     _Pointer[_struct.SECURITY_ATTRIBUTES]],  # psa
                                    _type.c_int]
    SHGetSpecialFolderLocation: _Callable[[_type.HWND,  # hwnd
                                           _type.c_int,  # csidl
                                           _Pointer[_struct.ITEMIDLIST]],  # ppidl
                                          _type.HRESULT]
    SHCloneSpecialIDList: _Callable[[_type.HWND,  # hwnd
                                     _type.c_int,  # csidl
                                     _type.BOOL],  # fCreate
                                    _Pointer[_struct.ITEMIDLIST]]
    SHGetSpecialFolderPathA: _Callable[[_type.HWND,  # hwnd
                                        _type.LPSTR,  # pszPath
                                        _type.c_int,  # csidl
                                        _type.BOOL],  # fCreate
                                       _type.BOOL]
    SHGetSpecialFolderPathW: _Callable[[_type.HWND,  # hwnd
                                        _type.LPWSTR,  # pszPath
                                        _type.c_int,  # csidl
                                        _type.BOOL],  # fCreate
                                       _type.BOOL]
    SHFlushSFCache: _Callable[[],
                              _type.c_void]
    SHGetFolderPathA: _Callable[[_Optional[_type.HWND],  # hwnd
                                 _type.c_int,  # csidl
                                 _Optional[_type.HANDLE],  # hToken
                                 _type.DWORD,  # dwFlags
                                 _type.LPSTR],  # pszPath
                                _type.HRESULT]
    SHGetFolderPathW: _Callable[[_Optional[_type.HWND],  # hwnd
                                 _type.c_int,  # csidl
                                 _Optional[_type.HANDLE],  # hToken
                                 _type.DWORD,  # dwFlags
                                 _type.LPWSTR],  # pszPath
                                _type.HRESULT]
    SHGetFolderLocation: _Callable[[_type.HWND,  # hwnd
                                    _type.c_int,  # csidl
                                    _Optional[_type.HANDLE],  # hToken
                                    _type.DWORD,  # dwFlags
                                    _Pointer[_Pointer[_struct.ITEMIDLIST]]],  # ppidl
                                   _type.HRESULT]
    SHSetFolderPathA: _Callable[[_type.c_int,  # csidl
                                 _Optional[_type.HANDLE],  # hToken
                                 _type.DWORD,  # dwFlags
                                 _type.LPCSTR],  # pszPath
                                _type.HRESULT]
    SHSetFolderPathW: _Callable[[_type.c_int,  # csidl
                                 _Optional[_type.HANDLE],  # hToken
                                 _type.DWORD,  # dwFlags
                                 _type.LPCWSTR],  # pszPath
                                _type.HRESULT]
    SHGetFolderPathAndSubDirA: _Callable[[_type.HWND,  # hwnd
                                          _type.c_int,  # csidl
                                          _Optional[_type.HANDLE],  # hToken
                                          _type.DWORD,  # dwFlags
                                          _Optional[_type.LPCSTR],  # pszSubDir
                                          _type.LPSTR],  # pszPath
                                         _type.HRESULT]
    SHGetFolderPathAndSubDirW: _Callable[[_type.HWND,  # hwnd
                                          _type.c_int,  # csidl
                                          _Optional[_type.HANDLE],  # hToken
                                          _type.DWORD,  # dwFlags
                                          _Optional[_type.LPCWSTR],  # pszSubDir
                                          _type.LPWSTR],  # pszPath
                                         _type.HRESULT]
    SHParseDisplayName: _Callable[[_type.PCWSTR,  # pszName
                                   _Optional[_objidl.IBindCtx],  # pbc
                                   _Pointer[_Pointer[_struct.ITEMIDLIST]],  # ppidl
                                   _type.SFGAOF,  # sfgaoIn
                                   _Optional[_Pointer[_type.SFGAOF]]],  # psfgaoOut
                                  _type.HRESULT]
    # TODO
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
                                            _Optional[_Pointer[_objidl.IBindCtx]],
                                            _Pointer[_struct.IID],
                                            _Pointer[_ShObjIdl_core.IShellItem]],
                                           _type.SHSTDAPI]
    SHCreateShellItemArrayFromIDLists: _Callable[[_type.UINT,
                                                  _Pointer[_Pointer[_struct.ITEMIDLIST]],
                                                  _Pointer[_ShObjIdl_core.IShellItemArray]],
                                                 _type.SHSTDAPI]
    SHGetKnownFolderPath: _Callable[[_Pointer[_struct.KNOWNFOLDERID],
                                     _enum.KNOWN_FOLDER_FLAG,
                                     _Optional[_type.HANDLE],
                                     _Pointer[_type.PWSTR]],
                                    _type.HRESULT]
    SHGetPropertyStoreFromParsingName: _Callable[[_type.PCWSTR,
                                                  _Optional[_Pointer[_objidl.IBindCtx]],
                                                  _enum.GETPROPERTYSTOREFLAGS,
                                                  _Pointer[_struct.IID],
                                                  _Pointer[_propsys.IPropertyStore]],
                                                 _type.SHSTDAPI]


# noinspection PyPep8Naming
class shlwapi(_WinDLL):
    GUIDFromStringA: _Callable[[_type.LPCSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 269
    GUIDFromStringW: _Callable[[_type.LPCWSTR,
                                _Pointer[_struct.GUID]],
                               _type.BOOL] = 270
    DllGetVersion: _Callable[[_Pointer[_struct.DLLVERSIONINFO]],
                             _type.HRESULT]
    # Shlwapi
    PathMakePrettyA: _Callable[[_type.LPCSTR],  # pszPath
                               _type.BOOL]
    PathMakePrettyW: _Callable[[_type.LPCWSTR],  # pszPath
                               _type.BOOL]
    PathMatchSpecA: _Callable[[_type.LPCSTR,  # pszFile
                               _type.LPCSTR],  # pszSpec
                              _type.BOOL]
    PathMatchSpecW: _Callable[[_type.LPCWSTR,  # pszFile
                               _type.LPCWSTR],  # pszSpec
                              _type.BOOL]
    PathMatchSpecExA: _Callable[[_type.LPCSTR,  # pszFile
                                 _type.LPCSTR,  # pszSpec
                                 _type.DWORD],  # dwFlags
                                _type.BOOL]
    PathMatchSpecExW: _Callable[[_type.LPCWSTR,  # pszFile
                                 _type.LPCWSTR,  # pszSpec
                                 _type.DWORD],  # dwFlags
                                _type.BOOL]
    PathSkipRootA: _Callable[[_type.LPCSTR],  # pszPath
                             _type.LPSTR]
    PathSkipRootA: _Callable[[_type.LPCWSTR],  # pszPath
                             _type.LPWSTR]
    PathStripPathA: _Callable[[_type.LPSTR],  # pszPath
                              _type.c_void]
    PathStripPathW: _Callable[[_type.LPWSTR],  # pszPath
                              _type.c_void]
    PathStripToRootA: _Callable[[_type.LPSTR],  # pszPath
                                _type.BOOL]
    PathStripToRootW: _Callable[[_type.LPWSTR],  # pszPath
                                _type.BOOL]
    PathUnmakeSystemFolderA: _Callable[[_type.LPSTR],  # pszPath
                                       _type.BOOL]
    PathUnmakeSystemFolderW: _Callable[[_type.LPWSTR],  # pszPath
                                       _type.BOOL]
    PathUndecorateA: _Callable[[_type.LPSTR],  # pszPath
                               _type.c_void]
    PathUndecorateW: _Callable[[_type.LPWSTR],  # pszPath
                               _type.c_void]
    # TODO
    IsInternetESCEnabled: _Callable[[],
                                    _type.BOOL]
    IStream_Copy: _Callable[[_objidlbase.IStream,
                             _objidlbase.IStream,
                             _type.DWORD],
                            _type.HRESULT]
    IStream_Read: _Callable[[_objidlbase.IStream,
                             _type.c_void_p,
                             _type.ULONG],
                            _type.HRESULT]
    IStream_ReadStr: _Callable[[_objidlbase.IStream,
                                _Pointer[_type.PCWSTR]],
                               _type.HRESULT]
    IStream_Reset: _Callable[[_objidlbase.IStream],  # pstm
                             _type.HRESULT]
    IStream_Size: _Callable[[_objidlbase.IStream,  # pstm
                             _Pointer[_union.ULARGE_INTEGER]],  # pui
                            _type.HRESULT]
    IStream_Write: _Callable[[_objidlbase.IStream,
                              _type.c_void_p,
                              _type.ULONG],
                             _type.HRESULT]
    IStream_WriteStr: _Callable[[_objidlbase.IStream,
                                 _Pointer[_type.PCWSTR]],
                                _type.HRESULT]
    IUnknown_AtomicRelease: _Callable[[_type.c_void_p],
                                      _type.HRESULT]
    IUnknown_GetSite: _Callable[[_Unknwnbase.IUnknown,
                                 _Pointer[_struct.IID],
                                 _type.c_void_p],
                                _type.HRESULT]
    IUnknown_GetWindow: _Callable[[_Unknwnbase.IUnknown,
                                   _Pointer[_type.HWND]],
                                  _type.HRESULT]
    IUnknown_QueryService: _Callable[[_Unknwnbase.IUnknown,
                                      _Pointer[_struct.GUID],
                                      _Pointer[_struct.IID],
                                      _type.c_void_p],
                                     _type.HRESULT]
    IUnknown_Set: _Callable[[_Pointer[_Unknwnbase.IUnknown],
                             _Optional[_Unknwnbase.IUnknown]],
                            _type.HRESULT]
    IUnknown_SetSite: _Callable[[_Unknwnbase.IUnknown,
                                 _Optional[_Unknwnbase.IUnknown]],
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
                                 _objidlbase.IStream]
    SHCreateStreamOnFileA: _Callable[[_type.LPCSTR,  # pszFile
                                      _type.DWORD,  # grfMode
                                      _Pointer[_objidlbase.IStream]],  # ppstm
                                     _type.HRESULT]
    SHCreateStreamOnFileW: _Callable[[_type.LPCWSTR,  # pszFile
                                      _type.DWORD,  # grfMode
                                      _Pointer[_objidlbase.IStream]],  # ppstm
                                     _type.HRESULT]
    SHCreateStreamOnFileEx: _Callable[[_type.LPCWSTR,
                                       _type.DWORD,
                                       _type.DWORD,
                                       _type.BOOL,
                                       _Optional[_objidlbase.IStream],
                                       _Pointer[_objidlbase.IStream]],
                                      _type.HRESULT]
    SHOpenRegStreamA: _Callable[[_type.HKEY,
                                 _Optional[_type.LPCSTR],
                                 _Optional[_type.LPCSTR],
                                 _type.DWORD],
                                _objidlbase.IStream]
    SHOpenRegStreamW: _Callable[[_type.HKEY,
                                 _Optional[_type.LPCWSTR],
                                 _Optional[_type.LPCWSTR],
                                 _type.DWORD],
                                _objidlbase.IStream]
    SHOpenRegStream2A: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCSTR],
                                  _Optional[_type.LPCSTR],
                                  _type.DWORD],
                                 _objidlbase.IStream]
    SHOpenRegStream2W: _Callable[[_type.HKEY,
                                  _Optional[_type.LPCWSTR],
                                  _Optional[_type.LPCWSTR],
                                  _type.DWORD],
                                 _objidlbase.IStream]
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
class user32(_WinDLL):
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
    GetWindowCompositionAttribute: _Callable[[_type.HWND,  # hwnd
                                              _Pointer[_struct.WINDOWCOMPOSITIONATTRIBDATA]],  # pAttrData
                                             _type.BOOL]
    SetWindowCompositionAttribute: _Callable[[_type.HWND,  # hwnd
                                              _Pointer[_struct.WINDOWCOMPOSITIONATTRIBDATA]],  # pAttrData
                                             _type.BOOL]
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
                                    _Optional[_Pointer[_type.DWORD_PTR]]],
                                   _type.LRESULT]
    SendMessageTimeoutW: _Callable[[_type.HWND,
                                    _type.UINT,
                                    _type.WPARAM,
                                    _type.LPARAM,
                                    _type.UINT,
                                    _type.UINT,
                                    _Optional[_Pointer[_type.DWORD_PTR]]],
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
class uxtheme(_WinDLL):
    OpenNcThemeData: _Callable[[_type.HWND,  # hWnd
                                _type.LPCWSTR],  # pszClassList
                               _type.HTHEME] = 49
    RefreshImmersiveColorPolicyState: _Callable[[],
                                                _type.c_void] = 104
    GetIsImmersiveColorUsingHighContrast: _Callable[[_enum.IMMERSIVE_HC_CACHE_MODE],  # mode
                                                    _type.c_bool] = 106
    ShouldAppsUseDarkMode: _Callable[[],
                                     _type.c_bool] = 132
    AllowDarkModeForWindow: _Callable[[_type.HWND,  # hWnd
                                       _type.c_bool],  # allow
                                      _type.c_bool] = 133
    SetPreferredAppMode: _Callable[[_enum.PreferredAppMode],  # appMode
                                   _enum.PreferredAppMode] = 135
    FlushMenuThemes: _Callable[[],
                               _type.c_void] = 136
    IsDarkModeAllowedForWindow: _Callable[[],
                                          _type.c_bool] = 137
    ShouldSystemUseDarkMode: _Callable[[],
                                       _type.c_bool] = 138
    IsDarkModeAllowedForApp: _Callable[[],
                                       _type.c_bool] = 139
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


# noinspection PyPep8Naming
class wininet(_WinDLL):
    # wininet
    InternetCloseHandle: _Callable[[_type.HINTERNET],  # hInternet
                                   _type.BOOLAPI]
    InternetSetOptionA: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                                   _type.DWORD,  # dwOption
                                   _Optional[_type.LPVOID],  # lpBuffer
                                   _type.DWORD],  # dwBufferLength
                                  _type.BOOLAPI]
    InternetSetOptionW: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                                   _type.DWORD,  # dwOption
                                   _Optional[_type.LPVOID],  # lpBuffer
                                   _type.DWORD],  # dwBufferLength
                                  _type.BOOLAPI]
    InternetSetOptionExA: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                                     _type.DWORD,  # dwOption
                                     _Optional[_type.LPVOID],  # lpBuffer
                                     _type.DWORD,  # dwBufferLength
                                     _type.DWORD],  # dwFlags
                                    _type.BOOLAPI]
    InternetSetOptionExW: _Callable[[_Optional[_type.HINTERNET],  # hInternet
                                     _type.DWORD,  # dwOption
                                     _Optional[_type.LPVOID],  # lpBuffer
                                     _type.DWORD,  # dwBufferLength
                                     _type.DWORD],  # dwFlags
                                    _type.BOOLAPI]
    InternetLockRequestFile: _Callable[[_type.HINTERNET,  # hInternet
                                        _Pointer[_type.HANDLE]],  # lphLockRequestInfo
                                       _type.BOOLAPI]
    InternetUnlockRequestFile: _Callable[[_type.HANDLE],  # hLockRequestInfo
                                         _type.BOOLAPI]
    InternetSetCookieA: _Callable[[_type.LPCSTR,  # lpszUrl
                                   _Optional[_type.LPCSTR],  # lpszCookieName
                                   _type.LPCSTR],  # lpszCookieData
                                  _type.BOOLAPI]
    InternetSetCookieW: _Callable[[_type.LPCWSTR,  # lpszUrl
                                   _Optional[_type.LPCWSTR],  # lpszCookieName
                                   _type.LPCWSTR],  # lpszCookieData
                                  _type.BOOLAPI]
    InternetGetCookieA: _Callable[[_type.LPCSTR,  # lpszUrl
                                   _Optional[_type.LPCSTR],  # lpszCookieName
                                   _type.LPSTR,  # lpszCookieData
                                   _Pointer[_type.DWORD]],  # lpdwSize
                                  _type.BOOLAPI]
    InternetGetCookieW: _Callable[[_type.LPCWSTR,  # lpszUrl
                                   _Optional[_type.LPCWSTR],  # lpszCookieName
                                   _type.LPWSTR,  # lpszCookieData
                                   _Pointer[_type.DWORD]],  # lpdwSize
                                  _type.BOOLAPI]
    InternetSetCookieExA: _Callable[[_type.LPCSTR,  # lpszUrl
                                     _Optional[_type.LPCSTR],  # lpszCookieName
                                     _type.LPCSTR,  # lpszCookieData
                                     _type.DWORD,  # dwFlags
                                     _Optional[_type.DWORD_PTR]],  # dwReserved
                                    _type.DWORD]
    InternetSetCookieExW: _Callable[[_type.LPCWSTR,  # lpszUrl
                                     _Optional[_type.LPCWSTR],  # lpszCookieName
                                     _type.LPCWSTR,  # lpszCookieData
                                     _type.DWORD,  # dwFlags
                                     _Optional[_type.DWORD_PTR]],  # dwReserved
                                    _type.DWORD]
    InternetGetCookieExA: _Callable[[_type.LPCSTR,  # lpszUrl
                                     _Optional[_type.LPCSTR],  # lpszCookieName
                                     _type.LPSTR,  # lpszCookieData
                                     _Pointer[_type.DWORD],  # lpdwSize
                                     _type.DWORD,  # dwFlags
                                     _type.LPVOID],  # lpReserved
                                    _type.BOOLAPI]
    InternetGetCookieExW: _Callable[[_type.LPCWSTR,  # lpszUrl
                                     _Optional[_type.LPCWSTR],  # lpszCookieName
                                     _type.LPWSTR,  # lpszCookieData
                                     _Pointer[_type.DWORD],  # lpdwSize
                                     _type.DWORD,  # dwFlags
                                     _type.LPVOID],  # lpReserved
                                    _type.BOOLAPI]


class Microsoft:
    class UI:
        class Xaml(_WinDLL):
            DllGetActivationFactory: _Callable[[_type.HSTRING,
                                                _Pointer[_activation.IActivationFactory]],
                                               _type.HRESULT]

    class WindowsAppRuntime:
        class Bootstrap(_WinDLL):
            MddBootstrapInitialize: _Callable[[_type.UINT32,
                                               _type.PCWSTR,
                                               _struct.PACKAGE_VERSION],
                                              _type.HRESULT]
            MddBootstrapShutdown: _Callable[[],
                                            _type.c_void]


class WebView2Loader(_WinDLL):
    # WebView2
    CreateCoreWebView2EnvironmentWithOptions: _Callable[[_type.PCWSTR,  # browserExecutableFolder
                                                         _type.PCWSTR,  # userDataFolder
                                                         _WebView2.ICoreWebView2EnvironmentOptions,  # environmentOptions
                                                         _WebView2.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler],  # environmentCreatedHandler
                                                        _type.HRESULT]
    CreateCoreWebView2Environment: _Callable[[_WebView2.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler],  # environmentCreatedHandler
                                             _type.HRESULT]
    GetAvailableCoreWebView2BrowserVersionString: _Callable[[_type.PCWSTR,  # browserExecutableFolder
                                                             _Pointer[_type.LPWSTR]],  # versionInfo
                                                            _type.HRESULT]
    CompareBrowserVersions: _Callable[[_type.PCWSTR,  # version1
                                       _type.PCWSTR,  # version2
                                       _Pointer[_type.c_int]],  # result
                                      _type.HRESULT]
