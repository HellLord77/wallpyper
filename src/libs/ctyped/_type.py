import ctypes as _ctypes  # TODO _Pointer[_struct.TYPE], better inspect name (?)
import functools as _functools
import numbers as _numbers
import operator as _operator
from typing import Callable as _Callable
from typing import Optional as _Optional
from typing import Union as _Union

from . import _const
from . import _struct
from .__head__ import _Globals
from .__head__ import _Pointer
from .__head__ import _resolve_type

_WIN64 = _ctypes.sizeof(_ctypes.c_void_p) == 8
_CT_BINARY = (
    '__add__', '__sub__', '__mul__', '__matmul__', '__truediv__', '__floordiv__', '__mod__',
    '__divmod__', '__pow__', '__lshift__', '__rshift__', '__and__', '__xor__', '__or__'
)
_CT_R_BINARY = (
    '__radd__', '__rsub__', '__rmul__', '__rmatmul__', '__rtruediv__', '__rfloordiv__', '__rmod__',
    '__rdivmod__', '__rpow__', '__rlshift__', '__rrshift__', '__rand__', '__rxor__', '__ror__'
)
_CT_I_BINARY = (
    '__iadd__', '__isub__', '__imul__', '__imatmul__', '__itruediv__', '__ifloordiv__',
    '__imod__', '__ipow__', '__ilshift__', '__irshift__', '__iand__', '__ixor__', '__ior__'
)
_CT_UNARY = ('__neg__', '__pos__', '__abs__', '__invert__', '__round__', '__trunc__', '__floor__', '__ceil__')
_PY_BINARY = '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__'
_PY_UNARY = '__complex__', '__int__', '__float__', '__index__'
_MAGICS = {}

c_bool: type[_ctypes.c_bool] = _Union[_ctypes.c_bool, bool]
c_byte: type[_ctypes.c_byte] = _Union[_ctypes.c_byte, int]
c_char: type[_ctypes.c_char] = _Union[_ctypes.c_char, bytes]
c_char_p: type[_ctypes.c_char_p] = _Optional[_Union[_ctypes.c_char_p, bytes]]
c_double: type[_ctypes.c_double] = _Union[_ctypes.c_double, float]
c_float: type[_ctypes.c_float] = _Union[_ctypes.c_float, float]
c_int: type[_ctypes.c_int] = _Union[_ctypes.c_int, int]
c_int16: type[_ctypes.c_int16] = _Union[_ctypes.c_int16, int]
c_int32: type[_ctypes.c_int32] = _Union[_ctypes.c_int32, int]
c_int64: type[_ctypes.c_int64] = _Union[_ctypes.c_int64, int]
c_int8: type[_ctypes.c_int8] = _Union[_ctypes.c_int8, int]
c_long: type[_ctypes.c_long] = _Union[_ctypes.c_long, int]
c_longdouble: type[_ctypes.c_longdouble] = _Union[_ctypes.c_longdouble, float]
c_short: type[_ctypes.c_short] = _Union[_ctypes.c_short, int]
c_size_t: type[_ctypes.c_size_t] = _Union[_ctypes.c_size_t, int]
c_ssize_t: type[_ctypes.c_ssize_t] = _Union[_ctypes.c_ssize_t, int]
c_ubyte: type[_ctypes.c_ubyte] = _Union[_ctypes.c_ubyte, int]
c_uint: type[_ctypes.c_uint] = _Union[_ctypes.c_uint, int]
c_uint16: type[_ctypes.c_uint16] = _Union[_ctypes.c_uint16, int]
c_uint32: type[_ctypes.c_uint32] = _Union[_ctypes.c_uint32, int]
c_uint64: type[_ctypes.c_uint64] = _Union[_ctypes.c_uint64, int]
c_uint8: type[_ctypes.c_uint8] = _Union[_ctypes.c_uint8, int]
c_ulong: type[_ctypes.c_ulong] = _Union[_ctypes.c_ulong, int]
c_ushort: type[_ctypes.c_ushort] = _Union[_ctypes.c_ushort, int]
c_void_p: type[_ctypes.c_void_p] = _Optional[_Union[_ctypes.c_void_p, _ctypes.c_wchar_p, _Pointer, int, str]]
c_wchar: type[_ctypes.c_wchar] = _Union[_ctypes.c_wchar, str]
c_wchar_p: type[_ctypes.c_wchar_p] = _Optional[_Union[_ctypes.c_wchar_p, _Pointer, str]]
HRESULT: type[_ctypes.HRESULT] = _Union[_ctypes.HRESULT, int]

c_uchar = c_ubyte
c_wchar_t = c_wchar

BOOL = c_int
BYTE = c_uchar
CHAR = c_char
DOUBLE = c_double
DWORD = c_ulong
FLOAT = c_float
INT = c_int
INT16 = c_short
INT32 = c_int
INT64 = c_int32
INT8 = c_char
LONG = c_long
LONGLONG = c_int64
RPC_STATUS = c_long
SHORT = c_short
UCHAR = c_uchar
UINT = c_uint
UINT16 = c_ushort
UINT32 = c_uint
UINT64 = c_uint64
UINT8 = c_uchar
ULONG = c_ulong
ULONGLONG = c_uint64
USHORT = c_ushort
WCHAR = c_wchar_t
WORD = c_ushort

BSTR = c_wchar_p
LPCCH = c_char_p
LPCH = c_char_p
LPCSTR = c_char_p
LPCVOID = c_void_p
LPCWCH = c_wchar_p
LPCWSTR = c_wchar_p
LPSTR = c_char_p
LPVOID = c_void_p
LPWCH = c_wchar_p
LPWSTR = c_wchar_p
NPSTR = c_char_p
NWPSTR = c_wchar_p
PBYTE = c_char_p
PCCH = c_char_p
PCH = c_char_p
PCHAR = c_char_p
PCNZCH = c_char_p
PCNZWCH = c_wchar_p
PCSTR = c_char_p
PCWCH = c_wchar_p
PCWSTR = c_wchar_p
PCZZSTR = c_char_p
PNZCH = c_char_p
PSTR = c_char_p
PVOID = c_void_p
PWCH = c_wchar_p
PWCHAR = c_wchar_p
PWSTR = c_wchar_p
PZZSTR = c_char_p
VARTYPE = c_ushort
VOID = c_void_p

_obj_p = c_void_p
GpBitmap = _obj_p
GpImage = _obj_p
HSTRING = _obj_p
IShellItem = _obj_p
IMoniker = _obj_p
LPRECT = _obj_p

_enum = c_uint  # TODO enum.IntEnum
DESKTOP_SLIDESHOW_DIRECTION = _enum
DESKTOP_SLIDESHOW_OPTIONS = _enum
DESKTOP_SLIDESHOW_STATE = _enum
DESKTOP_WALLPAPER_POSITION = _enum
DebugEventLevel = _enum
RO_INIT_TYPE = _enum
SIGDN = _enum
Status = _enum
TrustLevel = _enum
GETPROPERTYSTOREFLAGS = _enum
FILEOPENDIALOGOPTIONS = _enum

HALF_PTR = c_int if _WIN64 else c_short
INT_PTR = c_int64 if _WIN64 else c_int
LONG_PTR = c_int64 if _WIN64 else c_long
UHALF_PTR = c_uint if _WIN64 else c_ushort
UINT_PTR = c_uint64 if _WIN64 else c_uint
ULONG_PTR = c_uint64 if _WIN64 else c_ulong

ARGB = DWORD
ATOM = WORD
BOOLEAN = BYTE
COLORREF = DWORD
DWORD_PTR = ULONG_PTR
HANDLE = PVOID
LP = LPWSTR
LPARAM = LONG_PTR
LPCTCH = LPCWCH
LPCTSTR = LPCWSTR
LPOLESTR = LPWSTR
LPTCH = LPWCH
LPTSTR = LPWSTR
LRESULT = LONG_PTR
OLECHAR = WCHAR
PCTCH = LPCWCH
PCTSTR = LPCWSTR
PROPID = ULONG
PSSTDAPI = HRESULT
PTCH = LPWCH
PTSTR = LPWSTR
SCODE = LONG
SFGAOF = ULONG
SICHINTF = DWORD
SIZE_T = ULONG_PTR
STDAPI = HRESULT
WINOLECTLAPI = HRESULT
WPARAM = UINT_PTR

PROPVAR_PAD1 = BYTE if _const.MIDL_PASS else WORD
PROPVAR_PAD2 = BYTE if _const.MIDL_PASS else WORD
PROPVAR_PAD3 = ULONG if _const.MIDL_PASS else WORD

GpStatus = Status
HACCEL = HANDLE
HBITMAP = HANDLE
HBRUSH = HANDLE
HCOLORSPACE = HANDLE
HDC = HANDLE
HDESK = HANDLE
HDWP = HANDLE
HENHMETAFILE = HANDLE
HFONT = HANDLE
HGDIOBJ = HANDLE
HGLOBAL = HANDLE
HHOOK = HANDLE
HICON = HANDLE
HINSTANCE = HANDLE
HKEY = HANDLE
HKL = HANDLE
HLOCAL = HANDLE
HMENU = HANDLE
HMETAFILE = HANDLE
HMODULE = HANDLE
HMONITOR = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRGN = HANDLE
HRSRC = HANDLE
HSTR = HANDLE
HTASK = HANDLE
HUMPD = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
LPCOLESTR = LPOLESTR
PDWORD_PTR = _Pointer[DWORD_PTR]
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE
SHSTDAPI = STDAPI

HCURSOR = HICON

BFFCALLBACK = _Callable[[HWND, UINT, LPARAM, LPARAM], c_int]
DebugEventProc = _Callable[[DebugEventLevel, PCHAR], VOID]
EDITWORDBREAKPROCA = _Callable[[LPSTR, c_int, c_int, c_int], c_int]
EDITWORDBREAKPROCW = _Callable[[LPWSTR, c_int, c_int, c_int], c_int]
GRAYSTRINGPROC = _Callable[[HDC, LPARAM, c_int], BOOL]
HOOKPROC = _Callable[[c_int, WPARAM, LPARAM], LRESULT]
MONITORENUMPROC = _Callable[[HMONITOR, HDC, _Pointer[_struct.RECT], LPARAM], BOOL]
PROPENUMPROCA = _Callable[[HWND, LPCSTR, HANDLE], BOOL]
PROPENUMPROCEXA = _Callable[[HWND, LPSTR, HANDLE, ULONG_PTR], BOOL]
PROPENUMPROCEXW = _Callable[[HWND, LPWSTR, HANDLE, ULONG_PTR], BOOL]
PROPENUMPROCW = _Callable[[HWND, LPCWSTR, HANDLE], BOOL]
TIMERPROC = _Callable[[HWND, UINT, UINT_PTR, DWORD], VOID]
WNDENUMPROC = _Callable[[HWND, LPARAM], BOOL]
WNDPROC = _Callable[[HWND, UINT, WPARAM, LPARAM], LRESULT]


def _set_magic(magic: str, func: _Callable):
    magic_ = getattr(_operator, magic, None) or getattr(_operator, magic.replace(
        'r', '', 1), None) or getattr(int, magic, None) or getattr(_numbers.Complex, magic)
    _MAGICS[magic] = _functools.update_wrapper(func, magic_)


def _set_magics():
    if not _MAGICS:
        for magic in _CT_BINARY:
            _set_magic(magic, lambda self, other, *args, _magic=magic: type(self)(
                getattr(self.value, _magic)(getattr(other, 'value', other), *args)))
        for magic in _CT_R_BINARY:
            _set_magic(magic, lambda self, other, *args, _magic=magic.replace('r', '', 1): type(self)(
                getattr(getattr(other, 'value', other), _magic)(self.value, *args)))
        for magic in _CT_I_BINARY:
            _set_magic(magic, lambda self, other, *args, _magic=magic.replace('i', '', 1): (setattr(
                self, 'value', getattr(self.value, _magic)(getattr(other, 'value', other), *args)), self)[1])
        for magic in _CT_UNARY:
            _set_magic(magic, lambda self, *args, _magic=magic: type(self)(getattr(self.value, _magic)(*args)))
        for magic in _PY_BINARY:
            _set_magic(magic,
                       lambda self, other, _magic=magic: getattr(self.value, _magic)(getattr(other, 'value', other)))
        for magic in _PY_UNARY:
            _set_magic(magic, (lambda self: complex(self.value)) if magic == '__complex__' else (
                lambda self, _magic=magic: getattr(self.value, _magic)()))


_set_magics()


# noinspection PyUnresolvedReferences,PyProtectedMember
def _init(name: str) -> _Union[type[_ctypes._SimpleCData], type[_ctypes._Pointer]]:
    _globals.has_item(name)
    type_ = _resolve_type(_globals.vars_[name])
    if isinstance(type_, list):
        type_ = _ctypes.WINFUNCTYPE(*type_)
    for item in _MAGICS.items():
        setattr(type_, *item)
    return type_


_globals = _Globals()
