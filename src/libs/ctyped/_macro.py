from . import _com
from . import _const
from . import _func
from . import _struct
from . import _type
from .__head__ import _Pointer
from .__head__ import _byref
from .__head__ import _cast


# noinspection PyPep8Naming
def SUCCEEDED(hr: int) -> bool:
    return hr >= 0


# noinspection PyPep8Naming
def FAILED(hr: int) -> bool:
    return hr < 0


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
    return _r >> 16 == 0


# noinspection PyPep8Naming
def MAKEINTRESOURCEA(i: _type.WORD) -> bytes:
    # noinspection PyTypeChecker
    return _cast(_cast(i, _type.ULONG_PTR), _type.LPSTR).value


# noinspection PyPep8Naming
def MAKEINTRESOURCEW(i: _type.WORD) -> str:
    # noinspection PyTypeChecker
    return _cast(_cast(i, _type.ULONG_PTR), _type.LPWSTR).value


# noinspection PyPep8Naming
def GET_X_LPARAM(lp: int) -> int:
    return LOWORD(lp)


# noinspection PyPep8Naming
def GET_Y_LPARAM(lp: int) -> int:
    return HIWORD(lp)


# noinspection PyPep8Naming
def GetScode(sc: int) -> _type.SCODE:
    return _type.SCODE(sc)


# noinspection PyPep8Naming
def ResultFromScode(sc: int) -> _type.HRESULT:
    return _type.HRESULT(sc)


# noinspection PyPep8Naming,PyProtectedMember
def IID_PPV_ARGS(ppType: _com._IUnknown) -> tuple[_Pointer[_struct.IID], _Pointer[_com._IUnknown]]:
    iid_ref = _byref(_struct.IID())
    _func.ole32.IIDFromString(getattr(_const, f'IID_{type(ppType).__name__}'), iid_ref)
    return iid_ref, _byref(ppType)
