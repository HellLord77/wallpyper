from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import oaidl as _oaidl
from . import servprov as _servprov
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDispatchEx(_oaidl.IDispatch):
    GetDispID: _Callable[[_type.BSTR,  # bstrName
                          _type.DWORD,  # grfdex
                          _Pointer[_type.DISPID]],  # pid
                         _type.HRESULT]
    InvokeEx: _Callable[[_type.DISPID,  # id
                         _type.LCID,  # lcid
                         _type.WORD,  # wFlags
                         _Pointer[_struct.DISPPARAMS],  # pdp
                         _Pointer[_struct.VARIANT],  # pvarRes
                         _Pointer[_struct.EXCEPINFO],  # pei
                         _servprov.IServiceProvider],  # pspCaller
                        _type.HRESULT]
    DeleteMemberByName: _Callable[[_type.BSTR,  # bstrName
                                   _type.DWORD],  # grfdex
                                  _type.HRESULT]
    DeleteMemberByDispID: _Callable[[_type.DISPID],  # id
                                    _type.HRESULT]
    GetMemberProperties: _Callable[[_type.DISPID,  # id
                                    _type.DWORD,  # grfdexFetch
                                    _Pointer[_type.DWORD]],  # pgrfdex
                                   _type.HRESULT]
    GetMemberName: _Callable[[_type.DISPID,  # id
                              _Pointer[_type.BSTR]],  # pbstrName
                             _type.HRESULT]
    GetNextDispID: _Callable[[_type.DWORD,  # grfdex
                              _type.DISPID,  # id
                              _Pointer[_type.DISPID]],  # pid
                             _type.HRESULT]
    GetNameSpaceParent: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # ppunk
                                  _type.HRESULT]


class IDispError(_Unknwnbase.IUnknown):
    QueryErrorInfo: _Callable[[_struct.GUID,  # guidErrorType
                               _Pointer[IDispError]],  # ppde
                              _type.HRESULT]
    GetNext: _Callable[[_Pointer[IDispError]],  # ppde
                       _type.HRESULT]
    GetHresult: _Callable[[_Pointer[_type.HRESULT]],  # phr
                          _type.HRESULT]
    GetSource: _Callable[[_Pointer[_type.BSTR]],  # pbstrSource
                         _type.HRESULT]
    GetHelpInfo: _Callable[[_Pointer[_type.BSTR],  # pbstrFileName
                            _Pointer[_type.DWORD]],  # pdwContext
                           _type.HRESULT]
    GetDescription: _Callable[[_Pointer[_type.BSTR]],  # pbstrDescription
                              _type.HRESULT]


class IVariantChangeType(_Unknwnbase.IUnknown):
    ChangeType: _Callable[[_Pointer[_struct.VARIANT],  # pvarDst
                           _Pointer[_struct.VARIANT],  # pvarSrc
                           _type.LCID,  # lcid
                           _type.VARTYPE],  # vtNew
                          _type.HRESULT]


class IObjectIdentity(_Unknwnbase.IUnknown):
    IsEqualObject: _Callable[[_Unknwnbase.IUnknown],  # punk
                             _type.HRESULT]


class ICanHandleException(_Unknwnbase.IUnknown):
    CanHandleException: _Callable[[_Pointer[_struct.EXCEPINFO],  # pExcepInfo
                                   _Pointer[_struct.VARIANT]],  # pvar
                                  _type.HRESULT]


class IProvideRuntimeContext(_Unknwnbase.IUnknown):
    GetCurrentSourceContext: _Callable[[_Pointer[_type.DWORD_PTR],  # pdwContext
                                        _Pointer[_type.VARIANT_BOOL]],  # pfExecutingGlobalCode
                                       _type.HRESULT]
