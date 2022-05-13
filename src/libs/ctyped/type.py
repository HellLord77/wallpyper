import ctypes as _ctypes
import functools as _functools
import numbers as _numbers
import operator as _operator
import typing as _typing
from typing import Callable as _Callable, Union as _Union

import _ctypes as __ctypes

from . import const as _const, struct as _struct
from ._utils import _Globals, _Pointer, _resolve_type

_WIN64 = _ctypes.sizeof(_ctypes.c_void_p) == 8
_CT_BINARY = (
    '__add__', '__sub__', '__mul__', '__matmul__', '__truediv__', '__floordiv__', '__mod__',
    '__divmod__', '__pow__', '__lshift__', '__rshift__', '__and__', '__xor__', '__or__')
_CT_R_BINARY = (
    '__radd__', '__rsub__', '__rmul__', '__rmatmul__', '__rtruediv__', '__rfloordiv__', '__rmod__',
    '__rdivmod__', '__rpow__', '__rlshift__', '__rrshift__', '__rand__', '__rxor__', '__ror__')
_CT_I_BINARY = (
    '__iadd__', '__isub__', '__imul__', '__imatmul__', '__itruediv__', '__ifloordiv__',
    '__imod__', '__ipow__', '__ilshift__', '__irshift__', '__iand__', '__ixor__', '__ior__')
_CT_UNARY = '__neg__', '__pos__', '__abs__', '__invert__', '__round__', '__trunc__', '__floor__', '__ceil__'
_PY_BINARY = '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__'
_PY_UNARY = '__complex__', '__int__', '__float__', '__index__'
_MAGICS = {}

c_byte: type[_ctypes.c_byte] = _Union[_ctypes.c_byte, int]
c_char: type[_ctypes.c_char] = _Union[_ctypes.c_char, bytes]
c_char_p: type[_ctypes.c_char_p] = _Union[_ctypes.c_char_p, _Pointer, bytes]
c_double: type[_ctypes.c_double] = _Union[_ctypes.c_double, float]
c_longdouble: type[_ctypes.c_longdouble] = _Union[_ctypes.c_longdouble, float]
c_float: type[_ctypes.c_float] = _Union[_ctypes.c_float, float]
c_int: type[_ctypes.c_int] = _Union[_ctypes.c_int, int]
c_int8: type[_ctypes.c_int8] = _Union[_ctypes.c_int8, int]
c_int16: type[_ctypes.c_int16] = _Union[_ctypes.c_int16, int]
c_int32: type[_ctypes.c_int32] = _Union[_ctypes.c_int32, int]
c_int64: type[_ctypes.c_int64] = _Union[_ctypes.c_int64, int]
c_long: type[_ctypes.c_long] = _Union[_ctypes.c_long, int]
c_longlong: type[_ctypes.c_longlong] = _Union[_ctypes.c_longlong, int]
c_short: type[_ctypes.c_short] = _Union[_ctypes.c_short, int]
c_size_t: type[_ctypes.c_size_t] = _Union[_ctypes.c_size_t, int]
c_ssize_t: type[_ctypes.c_ssize_t] = _Union[_ctypes.c_ssize_t, int]
c_ubyte: type[_ctypes.c_ubyte] = _Union[_ctypes.c_ubyte, int]
c_uint: type[_ctypes.c_uint] = _Union[_ctypes.c_uint, int]
c_uint8: type[_ctypes.c_uint8] = _Union[_ctypes.c_uint8, int]
c_uint16: type[_ctypes.c_uint16] = _Union[_ctypes.c_uint16, int]
c_uint32: type[_ctypes.c_uint32] = _Union[_ctypes.c_uint32, int]
c_uint64: type[_ctypes.c_uint64] = _Union[_ctypes.c_uint64, int]
c_ulong: type[_ctypes.c_ulong] = _Union[_ctypes.c_ulong, int]
c_ulonglong: type[_ctypes.c_ulonglong] = _Union[_ctypes.c_ulonglong, int]
c_ushort: type[_ctypes.c_ushort] = _Union[_ctypes.c_ushort, int]
c_void_p: type[_ctypes.c_void_p] = _Union[_ctypes.c_void_p, _ctypes.c_char_p, _ctypes.c_wchar_p, _Pointer, int, str]
c_wchar: type[_ctypes.c_wchar] = _Union[_ctypes.c_wchar, str]
c_wchar_p: type[_ctypes.c_wchar_p] = _Union[_ctypes.c_wchar_p, _Pointer, str]
c_bool: type[_ctypes.c_bool] = _Union[_ctypes.c_bool, bool]
HRESULT: type[_ctypes.HRESULT] = _Union[_ctypes.HRESULT, int]
py_object: type[_ctypes.py_object] = _Union[_ctypes.py_object, c_void_p, _Pointer, object]

c_void = c_void_p
c_uchar = c_ubyte
c_wchar_t = c_wchar

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
PCSZ = c_char_p
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
VOID = c_void
rsize_t = c_size_t
va_list = c_char_p

BOOL = c_int
BYTE = c_uchar
CCHAR = c_char
CHAR = c_char
DOUBLE = c_double
DWORD = c_ulong
DWORD64 = c_uint64
FLOAT = c_float
INT = c_int
INT16 = c_short
INT32 = c_int
INT64 = c_int32
INT8 = c_char
LONG = c_long
LONGLONG = c_int64
REAL = c_float
RPC_STATUS = c_long
SHORT = c_short
UCHAR = c_uchar
UINT = c_uint
UINT16 = c_ushort
UINT32 = c_uint
UINT64 = c_uint64
UINT8 = c_uchar
ULONG = c_ulong
ULONG64 = c_uint64
ULONGLONG = c_uint64
USHORT = c_ushort
VARTYPE = c_ushort
WCHAR = c_wchar_t
WORD = c_ushort
boolean = c_uchar
byte = c_uchar
cs_byte = byte

_obj_p = c_void_p
Color = _obj_p
GpBitmap = _obj_p
GpBrush = _obj_p
GpCachedBitmap = _obj_p
GpGraphics = _obj_p
GpImage = _obj_p
GpImageAttributes = _obj_p
GpPen = _obj_p
GpSolidFill = _obj_p

_enum = c_uint
DebugEventLevel = _enum

HALF_PTR = c_int if _WIN64 else c_short
INT_PTR = c_int64 if _WIN64 else c_int
LONG_PTR = c_int64 if _WIN64 else c_long
UHALF_PTR = c_uint if _WIN64 else c_ushort
UINT_PTR = c_uint64 if _WIN64 else c_uint
ULONG_PTR = c_uint64 if _WIN64 else c_ulong

ACCESS_MASK = DWORD
ARGB = DWORD
ATOM = WORD
BOOLEAN = BYTE
COLORREF = DWORD
DEVINST = DWORD
DEVNODE = DWORD
DEVPROPID = ULONG
DEVPROPTYPE = ULONG
DLL_DIRECTORY_COOKIE = PVOID
DWORDLONG = ULONGLONG
DWORD_PTR = ULONG_PTR
FARPROC = INT_PTR
HANDLE = PVOID
HDEVINFO = PVOID
HDSKSPC = PVOID
KPRIORITY = LONG
LANGID = WORD
LCID = DWORD
LP = LPWSTR
LPARAM = LONG_PTR
LPOLESTR = LPWSTR
LRESULT = LONG_PTR
LSTATUS = LONG
MENUTEMPLATEA = VOID
MENUTEMPLATEW = VOID
NEARPROC = INT_PTR
NTSTATUS = LONG
OLECHAR = WCHAR
PROC = INT_PTR
PROPID = ULONG
PSSTDAPI = HRESULT
PixelFormat = INT
RETURN_TYPE = DWORD
SCODE = LONG
SFGAOF = ULONG
SICHINTF = DWORD
SIZE_T = ULONG_PTR
STDAPI = HRESULT
WINOLECTLAPI = HRESULT
WPARAM = UINT_PTR

APARTMENT_SHUTDOWN_REGISTRATION_COOKIE = HANDLE
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
HPAINTBUFFER = HANDLE
HPALETTE = HANDLE
HPEN = HANDLE
HRGN = HANDLE
HRSRC = HANDLE
HSTR = HANDLE
HSTRING = HANDLE
HSTRING_BUFFER = HANDLE
HTASK = HANDLE
HTHEME = HANDLE
HTHUMBNAIL = HANDLE
HUMPD = HANDLE
HWINEVENTHOOK = HANDLE
HWINSTA = HANDLE
HWND = HANDLE
SC_HANDLE = HANDLE
SERVICE_STATUS_HANDLE = HANDLE

PROPVAR_PAD1 = BYTE if _const.MIDL_PASS else WORD
PROPVAR_PAD2 = BYTE if _const.MIDL_PASS else WORD
PROPVAR_PAD3 = ULONG if _const.MIDL_PASS else WORD

ARGB64 = DWORDLONG
CONFIGRET = RETURN_TYPE
HCURSOR = HICON
LPCOLESTR = LPOLESTR
REGSAM = DWORD
SHSTDAPI = STDAPI

PDWORD_PTR = _Pointer[DWORD_PTR]

LPCSTR_PROXY = ULONG_PTR
LPCWSTR_PROXY = ULONG_PTR
LPSTR_PROXY = ULONG_PTR
LPWSTR_PROXY = ULONG_PTR

ABORTPROC = _Callable[[HDC, c_int], BOOL]
BFFCALLBACK = _Callable[[HWND, UINT, LPARAM, LPARAM], c_int]
DebugEventProc = _Callable[[DebugEventLevel, PCHAR], VOID]
DLGPROC = _Callable[[HWND, UINT, WPARAM, LPARAM], INT_PTR]
DLLGETVERSIONPROC = _Callable[[_Pointer[_struct.DLLVERSIONINFO]], HRESULT]
DRAWSTATEPROC = _Callable[[HDC, LPARAM, WPARAM, c_int, c_int], BOOL]
ENUMRESNAMEPROCA = _Callable[[HMODULE, LPCSTR_PROXY, LPSTR_PROXY, LONG_PTR], BOOL]
ENUMRESNAMEPROCW = _Callable[[HMODULE, LPCWSTR_PROXY, LPWSTR_PROXY, LONG_PTR], BOOL]
ENUMRESLANGPROCA = _Callable[[HMODULE, LPCSTR_PROXY, LPCSTR_PROXY, WORD, LONG_PTR], BOOL]
ENUMRESLANGPROCW = _Callable[[HMODULE, LPCWSTR_PROXY, LPCWSTR_PROXY, WORD, LONG_PTR], BOOL]
ENUMRESTYPEPROCA = _Callable[[HMODULE, LPCSTR_PROXY, LONG_PTR], BOOL]
ENUMRESTYPEPROCW = _Callable[[HMODULE, LPCWSTR_PROXY, LONG_PTR], BOOL]
GRAYSTRINGPROC = _Callable[[HDC, LPARAM, c_int], BOOL]
HOOKPROC = _Callable[[c_int, WPARAM, LPARAM], LRESULT]
ImageAbort = _Callable[[PVOID], BOOL]
LPCCHOOKPROC = _Callable[[HWND, UINT, WPARAM, LPARAM], UINT_PTR]
MONITORENUMPROC = _Callable[[HMONITOR, HDC, _Pointer[_struct.RECT], LPARAM], BOOL]
PHANDLER_ROUTINE = _Callable[[DWORD], BOOL]
PROPENUMPROCA = _Callable[[HWND, LPCSTR, HANDLE], BOOL]
PROPENUMPROCW = _Callable[[HWND, LPCWSTR, HANDLE], BOOL]
PROPENUMPROCEXA = _Callable[[HWND, LPSTR, HANDLE, ULONG_PTR], BOOL]
PROPENUMPROCEXW = _Callable[[HWND, LPWSTR, HANDLE, ULONG_PTR], BOOL]
PTIMERAPCROUTINE = _Callable[[LPVOID, DWORD, DWORD], VOID]
SENDASYNCPROC = _Callable[[HWND, UINT, ULONG_PTR, LRESULT], VOID]
TIMERPROC = _Callable[[HWND, UINT, UINT_PTR, DWORD], VOID]
WINEVENTPROC = _Callable[[HWINEVENTHOOK, DWORD, HWND, LONG, LONG, DWORD, DWORD], VOID]
WNDENUMPROC = _Callable[[HWND, LPARAM], BOOL]
WNDPROC = _Callable[[HWND, UINT, WPARAM, LPARAM], LRESULT]

DrawImageAbort = ImageAbort
GetThumbnailImageAbort = ImageAbort


def _set_magic(magic: str, func: _Callable):
    _MAGICS[magic] = _functools.update_wrapper(func, getattr(_operator, magic, None) or getattr(
        _operator, magic.replace('r', '', 1), None) or getattr(int, magic, None) or getattr(_numbers.Complex, magic))


def _set_magics():
    for magic in _CT_BINARY:
        _set_magic(magic, lambda self, other, *args, _magic=magic: type(self)(
            getattr(self.value, _magic)(getattr(other, 'value', other), *args)))
    for magic in _CT_R_BINARY:
        _set_magic(magic, lambda self, other, *args, _magic=magic.replace(
            'r', '', 1): type(self)(getattr(getattr(other, 'value', other), _magic)(self.value, *args)))
    for magic in _CT_I_BINARY:
        _set_magic(magic, lambda self, other, *args, _magic=magic.replace('i', '', 1): (setattr(
            self, 'value', getattr(self.value, _magic)(getattr(other, 'value', other), *args)), self)[1])
    for magic in _CT_UNARY:
        _set_magic(magic, lambda self, *args, _magic=magic: type(self)(getattr(self.value, _magic)(*args)))
    for magic in _PY_BINARY:
        _set_magic(magic, lambda self, other, _magic=magic: getattr(self.value, _magic)(getattr(other, 'value', other)))
    for magic in _PY_UNARY:
        _set_magic(magic, (lambda self: complex(
            self.value)) if magic == '__complex__' else (lambda self, _magic=magic: getattr(self.value, _magic)()))


_set_magics()


# noinspection PyUnresolvedReferences,PyProtectedMember
def _init(item: str) -> _Union[type[_ctypes._SimpleCData], type[_ctypes._CFuncPtr]]:
    var = _globals.vars_[item]
    type_ = _resolve_type(var)
    if isinstance(var, _typing._CallableGenericAlias):
        type_ = _ctypes.CFUNCTYPE(*type_)
    for item_ in _MAGICS.items():  # TODO subclass
        setattr(type_, *item_)
    if item != type_.__name__:
        type_ = type(item, type_.__bases__, dict(vars(type_)))
    return type_


_ctypes.cast(id(__ctypes.Array) + type(__ctypes.Array).__dictoffset__, _ctypes.POINTER(
    _ctypes.py_object)).contents.value['__str__'] = lambda self: f'{self._type_.__name__}{self[:]}'
_globals = _Globals(True)
