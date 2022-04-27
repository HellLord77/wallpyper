from __future__ import annotations as _

import ctypes as _ctypes
import types as _types
import typing as _typing
from typing import Callable as _Callable, Optional as _Optional

from . import interface as _com, const as _const, enum as _enum, lib as _lib, struct as _struct, type as _type
from ._utils import _addressof, _byref, _not_internal, _Pointer, _pointer, _resolve_type


class IUnknown(_type.c_void_p):
    __IID__ = {_const.IID_IUnknown}
    _funcs = None
    _vtbl = None
    _refs = {}

    def __init_subclass__(cls):
        cls._vtbl = None
        return super().__init_subclass__()

    def __new__(cls):
        base: type[IUnknown]
        if cls._vtbl is None:
            funcs = {}
            bases = cls.mro()
            for base in bases[bases.index(IUnknown)::-1]:
                cls.__IID__.update(base.__IID__)
                for key, value in vars(base).items():
                    if _not_internal(key) and (key in funcs or __name__ == base.__module__):
                        funcs[key] = value
            fields = []
            cls._funcs = []
            for name, func in funcs.items():
                class_ = isinstance(func, classmethod)
                static = isinstance(func, staticmethod)
                if class_ or static:
                    func = func.__func__
                types = list(_typing.get_type_hints(func).values())
                # noinspection PyTypeHints
                type_ = _ctypes.WINFUNCTYPE(*_resolve_type(_Callable[types, types.pop()]))
                fields.append((name, type_))
                cls._funcs.append(type_(_types.MethodType(func, cls)) if class_ else type_(func) if static else None)
            cls._funcs = tuple(cls._funcs)
            cls._vtbl = type(cls.__name__, (_ctypes.Structure,), {'_fields_': tuple(fields)})
        return super().__new__(cls)

    def __init__(self):  # TODO lazy init from value
        # noinspection PyProtectedMember,PyUnresolvedReferences
        self._ptr = _pointer(self._vtbl(*(type_(getattr(self, name)) if func is None else func
                                          for (name, type_), func in zip(self._vtbl._fields_, self._funcs))))
        super().__init__(_addressof(self._ptr))
        self._refs[self] = 1

    def __hash__(self):
        return self.value

    # noinspection PyPep8Naming,PyUnusedLocal
    def QueryInterface(self, This: _Pointer[IUnknown], riid: _Pointer[_struct.IID],
                       ppvObject: _Pointer[_type.LPVOID]) -> _type.HRESULT:
        if not ppvObject:
            return _const.E_INVALIDARG
        ppvObject.contents.value = None
        iid = _type.LPOLESTR()
        _lib.Ole32.StringFromIID(riid, _byref(iid))
        if iid.value in self.__IID__:
            ppvObject.contents.value = self.value
            self.AddRef()
            return _const.NOERROR
        return _const.E_NOINTERFACE

    # noinspection PyPep8Naming,PyUnusedLocal
    def AddRef(self, This: _Optional[_Pointer[IUnknown]] = None) -> _type.ULONG:
        self._refs[self] += 1
        return self._refs[self]

    # noinspection PyPep8Naming,PyUnusedLocal
    def Release(self, This: _Optional[_Pointer[IUnknown]] = None) -> _type.ULONG:
        self._refs[self] -= 1
        if self._refs[self] == 0:
            return self._refs.pop(self)
        return self._refs[self]


class IQueryContinue(IUnknown):
    __IID__ = {_const.IID_IQueryContinue}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def QueryContinue() -> _type.HRESULT:
        return _const.S_OK


class IUserNotificationCallback(IUnknown):
    __IID__ = {_const.IID_IUserNotificationCallback}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def OnBalloonUserClick(This: _Pointer[IUserNotificationCallback],
                           pt: _Pointer[_struct.POINT]) -> _type.HRESULT:
        return _const.NOERROR

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def OnLeftClick(This: _Pointer[IUserNotificationCallback],
                    pt: _Pointer[_struct.POINT]) -> _type.HRESULT:
        return _const.NOERROR

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def OnContextMenu(This: _Pointer[IUserNotificationCallback],
                      pt: _Pointer[_struct.POINT]) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncActionCompletedHandler(IUnknown):
    __IID__ = {_const.IID_IAsyncActionCompletedHandler}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncActionCompletedHandler, asyncInfo: _com.IAsyncAction,
               asyncStatus: _enum.AsyncStatus) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncActionProgressHandler(IUnknown):
    __IID__ = set()

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncActionProgressHandler, asyncInfo: _com.IAsyncActionWithProgress,
               progressInfo: _type.c_void_p) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncActionWithProgressCompletedHandler(IUnknown):
    __IID__ = set()

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncActionWithProgressCompletedHandler, asyncInfo: _com.IAsyncActionWithProgress,
               asyncStatus: _enum.AsyncStatus) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncOperationCompletedHandler(IUnknown):
    __IID__ = {_const.IID_IAsyncOperationCompletedHandler_bool,
               _const.IID_IAsyncOperationCompletedHandler_IRandomAccessStream,
               _const.IID_IAsyncOperationCompletedHandler_IStorageFile,
               _const.IID_IAsyncOperationCompletedHandler_IStorageFolder,
               _const.IID_IAsyncOperationCompletedHandler_IXmlDocument}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncOperationCompletedHandler, asyncInfo: _com.IAsyncOperation,
               asyncStatus: _enum.AsyncStatus) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncOperationProgressHandler(IUnknown):
    __IID__ = {_const.IID_IAsyncOperationWithProgressHandler_UINT64_UINT64}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncOperationProgressHandler, asyncInfo: _com.IAsyncOperationWithProgress,
               progressInfo: _type.c_void_p) -> _type.HRESULT:
        return _const.NOERROR


class IAsyncOperationWithProgressCompletedHandler(IUnknown):
    __IID__ = {_const.IID_IAsyncOperationWithProgressCompletedHandler_UINT64_UINT64}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: IAsyncOperationWithProgressCompletedHandler, asyncInfo: _com.IAsyncOperationWithProgress,
               asyncStatus: _enum.AsyncStatus) -> _type.HRESULT:
        return _const.NOERROR


class ITypedEventHandler(IUnknown):  # TODO split
    __IID__ = {_const.IID_ITypedEventHandler_IToastNotification_IToastDismissedEventArgs,
               _const.IID_ITypedEventHandler_IToastNotification_IInspectable,
               _const.IID_ITypedEventHandler_IToastNotification_IToastFailedEventArgs}

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def Invoke(This: _Pointer[ITypedEventHandler], sender: _type.c_void_p, args: _type.c_void_p) -> _type.HRESULT:
        return _const.NOERROR
