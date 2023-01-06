from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.um import Unknwnbase as _Unknwnbase
from ..interface.um import objidlbase as _objidlbase

# combaseapi
CoUninitialize: _Callable[[],
                          _type.VOID]
CoGetCurrentProcess: _Callable[[],
                               _type.DWORD]
CoInitializeEx: _Callable[[_Optional[_type.LPVOID],  # pvReserved
                           _type.DWORD],  # dwCoInit
                          _type.HRESULT]
CoMarshalInterface: _Callable[[_objidlbase.IStream,  # pStm
                               _Pointer[_struct.IID],  # riid
                               _Unknwnbase.IUnknown,  # pUnk
                               _type.DWORD,  # dwDestContext
                               _Optional[_type.DWORD],  # pvDestContext
                               _type.DWORD],  # mshlflags
                              _type.HRESULT]
CoUnmarshalInterface: _Callable[[_objidlbase.IStream,  # pStm
                                 _Pointer[_struct.IID],  # riid
                                 _type.LPVOID],  # ppv
                                _type.HRESULT]
CoMarshalHresult: _Callable[[_objidlbase.IStream,  # pstm
                             _type.HRESULT],  # hresult
                            _type.HRESULT]
CoUnmarshalHresult: _Callable[[_objidlbase.IStream,  # pstm
                               _Pointer[_type.HRESULT]],  # phresult
                              _type.HRESULT]
CoIsHandlerConnected: _Callable[[_Unknwnbase.IUnknown],  # pUnk
                                _type.BOOL]
CoMarshalInterThreadInterfaceInStream: _Callable[[_Pointer[_struct.IID],  # riid
                                                  _Unknwnbase.IUnknown,  # pUnk
                                                  _Pointer[_objidlbase.IStream]],  # ppStm
                                                 _type.HRESULT]
CoGetInterfaceAndReleaseStream: _Callable[[_objidlbase.IStream,  # pStm
                                           _Pointer[_struct.IID],  # riid
                                           _type.LPVOID],  # ppv
                                          _type.HRESULT]
CoCreateFreeThreadedMarshaler: _Callable[[_Unknwnbase.IUnknown,  # punkOuter
                                          _Pointer[_Unknwnbase.IUnknown]],  # ppunkMarshal
                                         _type.HRESULT]
CoFreeUnusedLibraries: _Callable[[],
                                 _type.c_void]
CoFreeUnusedLibrariesEx: _Callable[[_type.DWORD,  # dwUnloadDelay
                                    _type.DWORD],  # dwReserved
                                   _type.c_void]
CoDisconnectContext: _Callable[[_type.DWORD],  # dwTimeout
                               _type.HRESULT]
CoCreateInstance: _Callable[[_Pointer[_struct.CLSID],  # rclsid
                             _Optional[_Pointer[_Unknwnbase.IUnknown]],  # pUnkOuter
                             _type.DWORD,  # dwClsContext
                             _Pointer[_struct.IID],  # riid
                             _type.LPVOID],  # ppv
                            _type.HRESULT]
StringFromCLSID: _Callable[[_Pointer[_struct.CLSID],  # rclsid
                            _Pointer[_type.LPOLESTR]],  # lplpsz
                           _type.HRESULT]
CLSIDFromString: _Callable[[_type.LPCOLESTR,  # lpsz
                            _Pointer[_struct.CLSID]],  # pclsid
                           _type.HRESULT]
StringFromIID: _Callable[[_Pointer[_struct.IID],  # rclsid
                          _Pointer[_type.LPOLESTR]],  # lplpsz
                         _type.HRESULT]
IIDFromString: _Callable[[_type.LPCOLESTR,  # lpsz
                          _Pointer[_struct.IID]],  # lpiid
                         _type.HRESULT]
ProgIDFromCLSID: _Callable[[_Pointer[_struct.CLSID],  # clsid
                            _Pointer[_type.LPOLESTR]],  # lplpszProgID
                           _type.HRESULT]
CLSIDFromProgID: _Callable[[_type.LPCOLESTR,  # lpszProgID
                            _Pointer[_struct.CLSID]],  # lpclsid
                           _type.HRESULT]
StringFromGUID2: _Callable[[_Pointer[_struct.GUID],  # rguid
                            _type.LPOLESTR,  # lpsz
                            _type.c_int],  # cchMax
                           _type.c_int]
CoCreateGuid: _Callable[[_Pointer[_struct.GUID]],  # pguid
                        _type.HRESULT]
DllCanUnloadNow: _Callable[[],
                           _type.HRESULT]
CoTaskMemAlloc: _Callable[[_type.SIZE_T],  # cb
                          _type.LPVOID]
CoTaskMemFree: _Callable[[_Optional[_type.LPVOID]],  # pv
                         _type.c_void]
# guiddef
IsEqualGUID: _Callable[[_Pointer[_struct.GUID],
                        _Pointer[_struct.GUID]],
                       _type.c_int]
# objbase
CoInitialize: _Callable[[_Optional[_type.LPVOID]],
                        _type.HRESULT]
# propidl
FreePropVariantArray: _Callable[[_type.ULONG,
                                 _Pointer[_struct.PROPVARIANT]],
                                _type.HRESULT]
PropVariantClear: _Callable[[_Pointer[_struct.PROPVARIANT]],
                            _type.HRESULT]
PropVariantCopy: _Callable[[_Pointer[_struct.PROPVARIANT],
                            _Pointer[_struct.PROPVARIANT]],
                           _type.HRESULT]

_WinLib(__name__)
