from __future__ import annotations as _

from typing import Callable as _Callable
from typing import Optional as _Optional

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

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

_WinLib(__name__)
