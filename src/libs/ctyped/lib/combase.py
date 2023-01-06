from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.um import objidl as _objidl
from ..interface.winrt import inspectable as _inspectable

# roapi
RoInitialize: _Callable[[_enum.RO_INIT_TYPE],  # initType
                        _type.HRESULT]
RoUninitialize: _Callable[[],
                          _type.c_void]
RoActivateInstance: _Callable[[_type.HSTRING,  # activatableClassId
                               _Pointer[_inspectable.IInspectable]],  # instance
                              _type.HRESULT]
RoRegisterActivationFactories: _Callable[[_Pointer[_type.HSTRING],  # activatableClassIds
                                          _Pointer[_type.PFNGETACTIVATIONFACTORY],  # activationFactoryCallbacks
                                          _type.UINT32,  # count
                                          _Pointer[_Pointer[_struct.RO_REGISTRATION_COOKIE]]],  # cookie
                                         _type.HRESULT]
RoRevokeActivationFactories: _Callable[[_Pointer[_struct.RO_REGISTRATION_COOKIE]],  # cookie
                                       _type.c_void]
RoGetActivationFactory: _Callable[[_type.HSTRING,  # activatableClassId
                                   _Pointer[_struct.IID],  # iid
                                   _type.c_void_p],  # factory
                                  _type.HRESULT]
RoRegisterForApartmentShutdown: _Callable[[_objidl.IApartmentShutdown,  # callbackObject
                                           _Pointer[_type.UINT64],  # apartmentIdentifier
                                           _Pointer[_type.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE]],  # regCookie
                                          _type.HRESULT]
RoUnregisterForApartmentShutdown: _Callable[[_type.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE],  # regCookie
                                            _type.HRESULT]
RoGetApartmentIdentifier: _Callable[[_Pointer[_type.UINT64]],  # apartmentIdentifier
                                    _type.HRESULT]
Initialize: _Callable[[_enum.RO_INIT_TYPE],  # initType
                      _type.HRESULT]
Uninitialize: _Callable[[],
                        _type.c_void]
RegisterActivationFactories: _Callable[[_Pointer[_type.HSTRING],  # activatableClassIds
                                        _Pointer[_type.PFNGETACTIVATIONFACTORY],  # activationFactoryCallbacks
                                        _type.UINT32,  # count
                                        _Pointer[_Pointer[_struct.RO_REGISTRATION_COOKIE]]],  # cookie
                                       _type.HRESULT]
RevokeActivationFactories: _Callable[[_Pointer[_struct.RO_REGISTRATION_COOKIE]],  # cookie
                                     _type.c_void]
# winstring
WindowsConcatString: _Callable[[_Optional[_type.HSTRING],
                                _Optional[_type.HSTRING],
                                _Pointer[_type.HSTRING]],
                               _type.HRESULT]
WindowsCreateString: _Callable[[_Optional[_type.PCNZWCH],
                                _type.UINT32,
                                _Pointer[_type.HSTRING]],
                               _type.HRESULT]
WindowsDeleteString: _Callable[[_type.HSTRING],
                               _type.HRESULT]
WindowsGetStringLen: _Callable[[_type.HSTRING],
                               _type.UINT32]
WindowsGetStringRawBuffer: _Callable[[_Optional[_type.HSTRING],
                                      _Optional[_Pointer[_type.UINT32]]],
                                     _type.PCWSTR]
WindowsIsStringEmpty: _Callable[[_type.HSTRING],
                                _type.BOOL]
WindowsReplaceString: _Callable[[_Optional[_type.HSTRING],
                                 _Optional[_type.HSTRING],
                                 _Optional[_type.HSTRING],
                                 _Pointer[_type.HSTRING]],
                                _type.HRESULT]
WindowsTrimStringEnd: _Callable[[_Optional[_type.HSTRING],
                                 _Optional[_type.HSTRING],
                                 _Pointer[_type.HSTRING]],
                                _type.HRESULT]
WindowsTrimStringStart: _Callable[[_Optional[_type.HSTRING],
                                   _Optional[_type.HSTRING],
                                   _Pointer[_type.HSTRING]],
                                  _type.HRESULT]

_WinLib(__name__)
