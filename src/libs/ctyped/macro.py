from . import com as _com, const as _const, lib as _lib, struct as _struct, type as _type
from ._utils import _Pointer, _byref, _cast_int


def __uuidof(_: str) -> _Pointer[_struct.IID]:
    iid_ref = _byref(_struct.IID())
    _lib.Ole32.IIDFromString(getattr(_const, f'IID_{_}'), iid_ref)
    return iid_ref


# noinspection PyPep8Naming
def SUCCEEDED(hr: int) -> bool:
    return hr >= 0


# noinspection PyPep8Naming
def FAILED(hr: int) -> bool:
    return hr < 0


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
def MAKEINTRESOURCEA(i: int) -> _type.LPSTR:
    return _type.LPSTR(_cast_int(_cast_int(i, _type.WORD), _type.ULONG_PTR))


# noinspection PyPep8Naming
def MAKEINTRESOURCEW(i: int) -> _type.LPWSTR:
    return _type.LPWSTR(_cast_int(_cast_int(i, _type.WORD), _type.ULONG_PTR))


# noinspection PyPep8Naming
def IID_PPV_ARGS(ppType: _com.IUnknown) -> tuple[_Pointer[_struct.IID], _Pointer[_com.IUnknown]]:
    return __uuidof(type(ppType).__name__), _byref(ppType)
