from __future__ import annotations as _

import ctypes as _ctypes
import functools as _functools
from typing import Optional as _Optional

from . import const as _const
from . import struct as _struct
from . import type as _type
from ._utils import _CT, _Pointer, _PyCSimpleType, _cast_int, _byref, _sizeof
from .lib import kernel32 as _kernel32
from .lib import ole32 as _ole32


# noinspection PyPep8Naming,PyShadowingBuiltins
def FIELD_OFFSET(type: type[_ctypes.Structure], field: str, _: _Optional[int] = None) -> int:
    field_ = getattr(type, field)
    offset = field_.offset
    if _ is not None:
        # noinspection PyUnresolvedReferences,PyProtectedMember
        offset += _ * _sizeof(dict(type._fields_)[field]._type_)
    return offset


# noinspection PyPep8Naming
def SUCCEEDED(hr: int) -> bool:
    return hr >= 0


# noinspection PyPep8Naming
def FAILED(hr: int) -> bool:
    return hr < 0


# noinspection PyPep8Naming
def NT_SUCCESS(Status: int) -> bool:
    return Status >= 0


# noinspection PyPep8Naming
def NT_INFORMATION(Status: int) -> bool:
    return (Status >> 30) == 1


# noinspection PyPep8Naming
def NT_WARNING(Status: int) -> bool:
    return (Status >> 30) == 2


# noinspection PyPep8Naming
def NT_ERROR(Status: int) -> bool:
    return (Status >> 30) == 3


# noinspection PyPep8Naming
def HRESULT_FROM_WIN32(x: int) -> int:
    return _type.HRESULT(x if x < 0 else (x & 0x0000FFFF) | _const.FACILITY_WIN32 << 16 | 0x80000000).value


# noinspection PyPep8Naming
def MAKEWORD(a: int, b: int) -> int:
    return (a & 0xff) | (b & 0xff) << 8


# noinspection PyPep8Naming
def MAKELONG(a: int, b: int) -> int:
    return (a & 0xffff) | (b & 0xffff) << 16


# noinspection PyPep8Naming
def MAKEWPARAM(l_: int, h: int) -> int:
    return _cast_int(_cast_int(MAKELONG(l_, h), _type.DWORD), _type.WPARAM)


# noinspection PyPep8Naming
def MAKELPARAM(l_: int, h: int) -> int:
    return _cast_int(_cast_int(MAKELONG(l_, h), _type.DWORD), _type.LPARAM)


# noinspection PyPep8Naming
def MAKELRESULT(l_: int, h: int) -> int:
    return _cast_int(_cast_int(MAKELONG(l_, h), _type.DWORD), _type.LRESULT)


# noinspection PyPep8Naming
def MAKEINTATOMA(i: int) -> _type.LPSTR:
    return _type.LPSTR(_cast_int(_cast_int(i, _type.WORD), _type.ULONG_PTR))


# noinspection PyPep8Naming
def MAKEINTATOMW(i: int) -> _type.LPWSTR:
    return _type.LPWSTR(_cast_int(_cast_int(i, _type.WORD), _type.ULONG_PTR))


# noinspection PyPep8Naming
def LOWORD(l_: int) -> int:
    return l_ & 0xffff


# noinspection PyPep8Naming
def HIWORD(l_: int) -> int:
    return l_ >> 16 & 0xffff


# noinspection PyPep8Naming
def LOBYTE(w: int) -> int:
    return w & 0xff


# noinspection PyPep8Naming
def HIBYTE(w: int) -> int:
    return w >> 8 & 0xff


# noinspection PyPep8Naming
def MAKELANGID(p: int, s: int) -> int:
    return s << 10 | p


# noinspection PyPep8Naming
def PRIMARYLANGID(lgid: int) -> int:
    return lgid & 0x3ff


# noinspection PyPep8Naming
def SUBLANGID(lgid: int) -> int:
    return lgid >> 10


# noinspection PyPep8Naming
def RGB(r: int, g: int, b: int) -> int:
    return r | g << 8 | b << 16


# noinspection PyPep8Naming
def PALETTERGB(r: int, g: int, b: int) -> int:
    return 0x02000000 | RGB(r, g, b)


# noinspection PyPep8Naming
def GetRValue(rgb: int) -> int:
    return LOBYTE(rgb)


# noinspection PyPep8Naming
def GetGValue(rgb: int) -> int:
    return LOBYTE(rgb >> 8)


# noinspection PyPep8Naming
def GetBValue(rgb: int) -> int:
    return LOBYTE(rgb >> 16)


# noinspection PyPep8Naming
def IS_INTRESOURCE(_r: int) -> bool:
    return _cast_int(_r, _type.ULONG_PTR) >> 16 == 0


# noinspection PyPep8Naming
def GET_X_LPARAM(lp: int) -> int:
    return LOWORD(lp)


# noinspection PyPep8Naming
def GET_Y_LPARAM(lp: int) -> int:
    return HIWORD(lp)


# noinspection PyPep8Naming
def GetScode(sc: int) -> int:
    return _cast_int(sc, _type.SCODE)


# noinspection PyPep8Naming
def ResultFromScode(sc: int) -> int:
    return _type.HRESULT(sc).value


# noinspection PyPep8Naming
def MAKEDLLVERULL(major: int, minor: int, build: int, qfe: int) -> int:
    return major << 48 | minor << 32 | build << 16 | qfe


# noinspection PyPep8Naming
def GDIP_WMF_RECORD_TO_EMFPLUS(n: int) -> int:
    return n | _const.GDIP_WMF_RECORD_BASE


# noinspection PyPep8Naming
def GDIP_EMFPLUS_RECORD_TO_WMF(n: int) -> int:
    return n & ~_const.GDIP_WMF_RECORD_BASE


# noinspection PyPep8Naming
def GDIP_IS_WMF_RECORDTYPE(n: int) -> bool:
    return bool(n & _const.GDIP_WMF_RECORD_BASE)


# noinspection PyPep8Naming
def MAKEINTRESOURCEA(i: int) -> _type.LPSTR:
    return _type.LPSTR(_cast_int(_cast_int(i, _type.WORD), _type.ULONG_PTR))


# noinspection PyPep8Naming
def MAKEINTRESOURCEW(i: int) -> _type.LPWSTR:
    return _type.LPWSTR(_cast_int(_cast_int(i, _type.WORD), _type.ULONG_PTR))


@_functools.lru_cache
def __uuidof(_: _PyCSimpleType) -> _Pointer[_struct.IID]:
    # noinspection PyProtectedMember
    base = _._base
    const = _const
    for namespace in base.__module__.split('.'):
        try:  # TODO rework
            const = getattr(const, namespace)
        except AttributeError:
            pass
    iid_ref = _byref(_struct.IID())
    _ole32.IIDFromString(getattr(const, f'IID_{base.__name__}'), iid_ref)
    return iid_ref


# noinspection PyPep8Naming
def IID_PPV_ARGS(ppType: _CT) -> tuple[_Pointer[_struct.IID], _Pointer[_CT]]:
    # noinspection PyProtectedMember
    return __uuidof(ppType._base), _byref(ppType)


# noinspection PyPep8Naming
def IsWindowsVersionOrGreater(wMajorVersion: int, wMinorVersion: int, wServicePackMajor: int) -> bool:
    osvi = _struct.OSVERSIONINFOEXW(
        dwMajorVersion=wMajorVersion, dwMinorVersion=wMinorVersion, wServicePackMajor=wServicePackMajor)
    condition = _kernel32.VerSetConditionMask(_kernel32.VerSetConditionMask(
        _kernel32.VerSetConditionMask(0, _const.VER_MAJORVERSION, _const.VER_GREATER_EQUAL),
        _const.VER_MINORVERSION, _const.VER_GREATER_EQUAL), _const.VER_SERVICEPACKMAJOR, _const.VER_GREATER_EQUAL)
    return bool(_kernel32.VerifyVersionInfoW(_byref(
        osvi), _const.VER_MAJORVERSION | _const.VER_MINORVERSION | _const.VER_SERVICEPACKMAJOR, condition))


# noinspection PyPep8Naming
def IsWindowsXPOrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WINXP), LOBYTE(_const._WIN32_WINNT_WINXP), 0)


# noinspection PyPep8Naming
def IsWindowsXPSP1OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WINXP), LOBYTE(_const._WIN32_WINNT_WINXP), 1)


# noinspection PyPep8Naming
def IsWindowsXPSP2OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WINXP), LOBYTE(_const._WIN32_WINNT_WINXP), 2)


# noinspection PyPep8Naming
def IsWindowsXPSP3OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WINXP), LOBYTE(_const._WIN32_WINNT_WINXP), 3)


# noinspection PyPep8Naming
def IsWindowsVistaOrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_VISTA), LOBYTE(_const._WIN32_WINNT_VISTA), 0)


# noinspection PyPep8Naming
def IsWindowsVistaSP1OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_VISTA), LOBYTE(_const._WIN32_WINNT_VISTA), 1)


# noinspection PyPep8Naming
def IsWindowsVistaSP2OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_VISTA), LOBYTE(_const._WIN32_WINNT_VISTA), 2)


# noinspection PyPep8Naming
def IsWindows7OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WIN7), LOBYTE(_const._WIN32_WINNT_WIN7), 0)


# noinspection PyPep8Naming
def IsWindows7SP1OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WIN7), LOBYTE(_const._WIN32_WINNT_WIN7), 1)


# noinspection PyPep8Naming
def IsWindows8OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WIN8), LOBYTE(_const._WIN32_WINNT_WIN8), 0)


# noinspection PyPep8Naming
def IsWindows8Point1OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WINBLUE), LOBYTE(_const._WIN32_WINNT_WINBLUE), 0)


# noinspection PyPep8Naming
def IsWindowsThresholdOrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(
        _const._WIN32_WINNT_WINTHRESHOLD), LOBYTE(_const._WIN32_WINNT_WINTHRESHOLD), 0)


# noinspection PyPep8Naming
def IsWindows10OrGreater() -> bool:
    # noinspection PyProtectedMember
    return IsWindowsVersionOrGreater(HIBYTE(_const._WIN32_WINNT_WIN10), LOBYTE(_const._WIN32_WINNT_WIN10), 0)


# noinspection PyPep8Naming
def IsWindowsServer() -> bool:
    osvi = _struct.OSVERSIONINFOEXW(wProductType=_const.VER_NT_WORKSTATION)
    condition = _kernel32.VerSetConditionMask(0, _const.VER_PRODUCT_TYPE, _const.VER_EQUAL)
    return not bool(_kernel32.VerifyVersionInfoW(_byref(osvi), _const.VER_PRODUCT_TYPE, condition))


_uuidof = __uuidof
