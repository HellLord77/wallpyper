from __future__ import annotations as _

from typing import Callable as _Callable

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
WindowsCreateString: _Callable[[_type.PCNZWCH,  # sourceString
                                _type.UINT32,  # length
                                _Pointer[_type.HSTRING]],  # string
                               _type.HRESULT]
WindowsCreateStringReference: _Callable[[_type.PCWSTR,  # sourceString
                                         _type.UINT32,  # length
                                         _Pointer[_struct.HSTRING_HEADER],  # hstringHeader
                                         _Pointer[_type.HSTRING]],  # string
                                        _type.HRESULT]
WindowsDeleteString: _Callable[[_type.HSTRING],  # string
                               _type.HRESULT]
WindowsDuplicateString: _Callable[[_type.HSTRING,  # string
                                   _Pointer[_type.HSTRING]],  # newString
                                  _type.HRESULT]
WindowsGetStringLen: _Callable[[_type.HSTRING],  # string
                               _type.UINT32]
WindowsGetStringRawBuffer: _Callable[[_type.HSTRING,  # string
                                      _Pointer[_type.UINT32]],  # length
                                     _type.PCWSTR]
WindowsIsStringEmpty: _Callable[[_type.HSTRING],  # string
                                _type.BOOL]
WindowsStringHasEmbeddedNull: _Callable[[_type.HSTRING,  # string
                                         _Pointer[_type.BOOL]],  # hasEmbedNull
                                        _type.HRESULT]
WindowsCompareStringOrdinal: _Callable[[_type.HSTRING,  # string1
                                        _type.HSTRING,  # string2
                                        _Pointer[_type.INT32]],  # result
                                       _type.HRESULT]
WindowsSubstring: _Callable[[_type.HSTRING,  # string
                             _type.UINT32,  # startIndex
                             _Pointer[_type.HSTRING]],  # newString
                            _type.HRESULT]
WindowsSubstringWithSpecifiedLength: _Callable[[_type.HSTRING,  # string
                                                _type.UINT32,  # startIndex
                                                _type.UINT32,  # length
                                                _Pointer[_type.HSTRING]],  # newString
                                               _type.HRESULT]
WindowsConcatString: _Callable[[_type.HSTRING,  # string1
                                _type.HSTRING,  # string2
                                _Pointer[_type.HSTRING]],  # newString
                               _type.HRESULT]
WindowsReplaceString: _Callable[[_type.HSTRING,  # string
                                 _type.HSTRING,  # stringReplaced
                                 _type.HSTRING,  # stringReplaceWith
                                 _Pointer[_type.HSTRING]],  # newString
                                _type.HRESULT]
WindowsTrimStringStart: _Callable[[_type.HSTRING,  # string
                                   _type.HSTRING,  # trimString
                                   _Pointer[_type.HSTRING]],  # newString
                                  _type.HRESULT]
WindowsTrimStringEnd: _Callable[[_type.HSTRING,  # string
                                 _type.HSTRING,  # trimString
                                 _Pointer[_type.HSTRING]],  # newString
                                _type.HRESULT]
WindowsPreallocateStringBuffer: _Callable[[_type.UINT32,  # length
                                           _Pointer[_Pointer[_type.WCHAR]],  # charBuffer
                                           _Pointer[_type.HSTRING_BUFFER]],  # bufferHandle
                                          _type.HRESULT]
WindowsPromoteStringBuffer: _Callable[[_type.HSTRING_BUFFER,  # bufferHandle
                                       _Pointer[_type.HSTRING]],  # string
                                      _type.HRESULT]
WindowsDeleteStringBuffer: _Callable[[_type.HSTRING_BUFFER],  # bufferHandle
                                     _type.HRESULT]
HSTRING_UserSize: _Callable[[_Pointer[_type.ULONG],  # pFlags
                             _type.ULONG,  # StartingSize
                             _Pointer[_type.HSTRING]],  # ppidl
                            _type.ULONG]
HSTRING_UserMarshal: _Callable[[_Pointer[_type.ULONG],  # pFlags
                                _Pointer[_type.UCHAR],  # pBuffer
                                _Pointer[_type.HSTRING]],  # ppidl
                               _Pointer[_type.UCHAR]]
HSTRING_UserUnmarshal: _Callable[[_Pointer[_type.ULONG],  # pFlags
                                  _Pointer[_type.UCHAR],  # pBuffer
                                  _Pointer[_type.HSTRING]],  # ppidl
                                 _Pointer[_type.UCHAR]]
HSTRING_UserFree: _Callable[[_Pointer[_type.ULONG],  # pFlags
                             _Pointer[_type.HSTRING]],  # ppidl
                            _type.c_void]
# WindowsInspectString: _Callable[[_type.UINT_PTR,  # targetHString
#                                  _type.USHORT,  # machine
#                                  PINSPECT_HSTRING_CALLBACK,  # callback
#                                  _type.c_void_p,  # context
#                                  _Pointer[_type.UINT32],  # length
#                                  _Pointer[_type.UINT_PTR]],  # targetStringAddress
#                                 _type.HRESULT]
# WindowsInspectString2: _Callable[[_type.UINT64,  # targetHString
#                                   _type.USHORT,  # machine
#                                   PINSPECT_HSTRING_CALLBACK2,  # callback
#                                   _type.c_void_p,  # context
#                                   _Pointer[_type.UINT32],  # length
#                                   _Pointer[_type.UINT64]],  # targetStringAddress
#                                  _type.HRESULT]

_WinLib(__name__)
