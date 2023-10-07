from __future__ import annotations as _

from typing import Callable as _Callable

from .. import _Interface
from .. import _Interface_impl
from ... import const as _const
from ... import struct as _struct
from ... import type as _type
from ..._utils import _CArgObject
from ..._utils import _Pointer
from ...const import error as _error
from ...lib import ole32 as _ole32


class _IUnknown:
    QueryInterface: _Callable[[_Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppvObject
                              _type.HRESULT]
    AddRef: _Callable[[],
                      _type.ULONG]
    Release: _Callable[[],
                       _type.ULONG]


class IUnknown(_IUnknown, _Interface):
    pass


# noinspection PyPep8Naming
class IUnknown_impl(_IUnknown, _Interface_impl):
    _c_refs = {}

    def __init__(self):
        super().__init__()
        self._c_refs[self] = 1

    def QueryInterface(self, riid: _Pointer[_struct.IID], ppv_object: _type.LPVOID) -> _type.HRESULT:
        if not ppv_object:
            return _error.E_INVALIDARG
        # noinspection PyProtectedMember
        obj_ref = ppv_object._obj if isinstance(
            ppv_object, _CArgObject) else _type.c_void_p.from_address(ppv_object)
        obj_ref.value = None
        for iid_ref in self._get_iid_refs():
            if _ole32.IsEqualGUID(riid, iid_ref):
                obj_ref.value = self.value
                self.AddRef()
                return _const.NOERROR
        return _error.E_NOINTERFACE

    def AddRef(self) -> _type.ULONG:
        c_ref = self._c_refs[self] = self._c_refs[self] + 1
        return c_ref

    def Release(self) -> _type.ULONG:
        c_ref = self._c_refs[self] = self._c_refs[self] - 1
        if c_ref == 0:
            del self._c_refs[self]
        return c_ref


class AsyncIUnknown(IUnknown):
    Begin_QueryInterface: _Callable[[_Pointer[_struct.IID]],  # riid
                                    _type.HRESULT]
    Finish_QueryInterface: _Callable[[_type.c_void_p],  # ppvObject
                                     _type.HRESULT]
    Begin_AddRef: _Callable[[],
                            _type.HRESULT]
    Finish_AddRef: _Callable[[],
                             _type.ULONG]
    Begin_Release: _Callable[[],
                             _type.HRESULT]
    Finish_Release: _Callable[[],
                              _type.ULONG]


class IClassFactory(IUnknown):
    CreateInstance: _Callable[[IUnknown,  # pUnkOuter
                               _Pointer[_struct.IID],  # riid
                               _type.c_void_p],  # ppvObject
                              _type.HRESULT]
    LockServer: _Callable[[_type.BOOL],  # fLock
                          _type.HRESULT]
