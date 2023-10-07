from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _CLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

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

_CLib(__name__)
