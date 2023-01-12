from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer

# commdlg
GetOpenFileNameA: _Callable[[_Pointer[_struct.OPENFILENAMEA]],
                            _type.BOOL]
GetOpenFileNameW: _Callable[[_Pointer[_struct.OPENFILENAMEW]],
                            _type.BOOL]
GetSaveFileNameA: _Callable[[_Pointer[_struct.OPENFILENAMEA]],
                            _type.BOOL]
GetSaveFileNameW: _Callable[[_Pointer[_struct.OPENFILENAMEW]],
                            _type.BOOL]
GetFileTitleA: _Callable[[_type.LPCSTR,
                          _type.LPSTR,  # Buf
                          _type.WORD],  # cchSize
                         _type.c_short]
GetFileTitleW: _Callable[[_type.LPCWSTR,
                          _type.LPWSTR,  # Buf
                          _type.WORD],  # cchSize
                         _type.c_short]
ChooseColorA: _Callable[[_Pointer[_struct.CHOOSECOLORA]],
                        _type.BOOL]
ChooseColorW: _Callable[[_Pointer[_struct.CHOOSECOLORW]],
                        _type.BOOL]
FindTextA: _Callable[[_Pointer[_struct.FINDREPLACEA]],
                     _type.HWND]
FindTextW: _Callable[[_Pointer[_struct.FINDREPLACEW]],
                     _type.HWND]
ReplaceTextA: _Callable[[_Pointer[_struct.FINDREPLACEA]],
                        _type.HWND]
ReplaceTextW: _Callable[[_Pointer[_struct.FINDREPLACEW]],
                        _type.HWND]
ChooseFontA: _Callable[[_Pointer[_struct.CHOOSEFONTA]],
                       _type.BOOL]
ChooseFontW: _Callable[[_Pointer[_struct.CHOOSEFONTW]],
                       _type.BOOL]
PrintDlgA: _Callable[[_Pointer[_struct.PRINTDLGA]],  # pPD
                     _type.BOOL]
PrintDlgW: _Callable[[_Pointer[_struct.PRINTDLGW]],  # pPD
                     _type.BOOL]
PrintDlgExA: _Callable[[_Pointer[_struct.PRINTDLGEXA]],  # pPD
                       _type.HRESULT]
PrintDlgExW: _Callable[[_Pointer[_struct.PRINTDLGEXW]],  # pPD
                       _type.HRESULT]
CommDlgExtendedError: _Callable[[],
                                _type.DWORD]
PageSetupDlgA: _Callable[[_Pointer[_struct.PAGESETUPDLGA]],
                         _type.BOOL]
PageSetupDlgW: _Callable[[_Pointer[_struct.PAGESETUPDLGW]],
                         _type.BOOL]

_WinLib(__name__)
