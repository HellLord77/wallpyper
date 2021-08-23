import ctypes as _ctypes
import functools as _functools
import numbers as _numbers
import operator as _operator
from typing import Callable as _Callable
from typing import Optional as _Optional
from typing import Union as _Union

from . import _header

_WIN32 = True
_WIN64 = _ctypes.sizeof(_ctypes.c_void_p) == 8
_CT_BINARY = ('__add__', '__sub__', '__mul__', '__matmul__', '__truediv__', '__floordiv__',
              '__mod__', '__divmod__', '__pow__', '__lshift__', '__rshift__', '__and__', '__xor__', '__or__',
              '__radd__', '__rsub__', '__rmul__', '__rmatmul__', '__rtruediv__', '__rfloordiv__',
              '__rmod__', '__rdivmod__', '__rpow__', '__rlshift__', '__rrshift__', '__rand__', '__rxor__', '__ror__')
_CT_I_BINARY = ('__iadd__', '__isub__', '__imul__', '__imatmul__', '__itruediv__', '__ifloordiv__',
                '__imod__', '__ipow__', '__ilshift__', '__irshift__', '__iand__', '__ixor__', '__ior__')
_CT_UNARY = ('__neg__', '__pos__', '__abs__', '__invert__',
             '__round__', '__trunc__', '__floor__', '__ceil__')
_PY_BINARY = '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__'
_PY_UNARY = '__complex__', '__int__', '__float__', '__index__'

HRESULT: type[_ctypes.HRESULT] = _Union[_ctypes.HRESULT, int]
c_bool: type[_ctypes.c_bool] = _Union[_ctypes.c_bool, bool]
c_byte: type[_ctypes.c_byte, int] = _Union[_ctypes.c_byte, int]
c_char: type[_ctypes.c_char, str] = _Union[_ctypes.c_char, str]
c_char_p: type[_ctypes.c_char_p] = _Optional[_Union[_ctypes.c_char_p, str]]
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
c_void_p: type[_ctypes.c_void_p] = _Optional[_Union[_ctypes.c_void_p, _ctypes.c_wchar_p, _header.Pointer, int, str]]
c_wchar: type[_ctypes.c_wchar] = _Union[_ctypes.c_wchar, str]
c_wchar_p: type[_ctypes.c_wchar_p] = _Optional[_Union[_ctypes.c_wchar_p, _header.Pointer, str]]

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
UCHAR = c_uchar
UINT = c_uint
UINT16 = c_ushort
UINT32 = c_uint
UINT64 = c_uint64
UINT8 = c_uchar
ULONG = c_ulong
USHORT = c_ushort
WCHAR = c_wchar_t
WORD = c_ushort

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
PCNZCH = c_char_p
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
VOID = c_void_p

DebugEventProc = c_void_p  # DebugEventProc
GpBitmap = c_void_p  # GpBitmap
GpImage = c_void_p  # GpImage
IUnknown = c_void_p  # IUnknown

enum = c_uint  # TODO: Enum type
DESKTOP_SLIDESHOW_DIRECTION = enum
DESKTOP_SLIDESHOW_OPTIONS = enum
DESKTOP_SLIDESHOW_STATE = enum
DESKTOP_WALLPAPER_POSITION = enum

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
SIZE_T = ULONG_PTR
Status = HRESULT
WPARAM = UINT_PTR

OLECHAR = WCHAR if _WIN32 else c_char
LPOLESTR = _header.Pointer[OLECHAR] if _WIN32 else LPSTR

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
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE

HCURSOR = HICON


def _set_magic(magics: dict[str, _Callable],
               magic: str,
               func: _Callable) -> None:
    magic_ = getattr(_operator, magic, None) or getattr(_operator, magic.replace(
        'r', '', 1), None) or getattr(int, magic, None) or getattr(_numbers.Complex, magic)
    magics[magic] = _functools.update_wrapper(func, magic_)


def _init():
    magics = {}
    for var in _CT_BINARY:
        _set_magic(magics, var, lambda self, other, *args, _magic=var: type(
            self)(getattr(self.value, _magic)(getattr(other, 'value', other), *args)))
    for var in _CT_I_BINARY:
        _set_magic(magics, var, lambda self, other, *args, _magic=var.replace('i', '', 1): (setattr(
            self, 'value', getattr(self.value, _magic)(getattr(other, 'value', other), *args)), self)[1])
    for var in _CT_UNARY:
        _set_magic(magics, var, lambda self, *args, _magic=var: type(self)(getattr(self.value, _magic)(*args)))
    for var in _PY_BINARY:
        _set_magic(magics, var, lambda self, other, _magic=var: getattr(
            self.value, _magic)(getattr(other, 'value', other)))
    for var in _PY_UNARY:
        _set_magic(magics, var, (lambda self: complex(self.value)) if var == '__complex__' else (
            lambda self, _magic=var: getattr(self.value, _magic)()))
    globals_ = globals()
    for var, type_ in _header.items(globals_):
        type_ = _header.resolve_type(type_)
        if type_ not in globals_.values():
            for item in magics.items():
                setattr(type_, *item)
        globals_[var] = type_


_init()
