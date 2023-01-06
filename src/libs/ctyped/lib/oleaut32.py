from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.um import ocidl as _ocidl

# oleauto
SysAllocString: _Callable[[_Optional[_type.LPCOLESTR]],  # psz
                          _type.BSTR]
SysReAllocString: _Callable[[_Optional[_Pointer[_type.BSTR]],  # pbstr
                             _Optional[_type.LPCOLESTR]],  # psz
                            _type.INT]
SysAllocStringLen: _Callable[[_Optional[_type.LPCOLESTR],  # strIn
                              _type.UINT],  # ui
                             _type.BSTR]
SysReAllocStringLen: _Callable[[_Optional[_Pointer[_type.BSTR]],  # pbstr
                                _Optional[_type.LPCOLESTR],  # psz
                                _type.c_uint],  # len
                               _type.INT]
SysAddRefString: _Callable[[_type.BSTR],  # bstrString
                           _type.HRESULT]
SysReleaseString: _Callable[[_type.BSTR],  # bstrString
                            _type.c_void]
SysFreeString: _Callable[[_Optional[_type.BSTR]],  # pbstr
                         _type.UINT]
SysStringLen: _Callable[[_Optional[_type.BSTR]],  # pbstr
                        _type.UINT]
SysStringByteLen: _Callable[[_Optional[_type.BSTR]],  # pbstr
                            _type.c_void]
SysAllocStringByteLen: _Callable[[_Optional[_type.LPCSTR],  # psz
                                  _type.UINT],  # len
                                 _type.BSTR]
# TODO
VariantChangeType: _Callable[[_Pointer[_struct.VARIANTARG],
                              _Pointer[_struct.VARIANTARG],
                              _type.USHORT,
                              _type.VARTYPE],
                             _type.HRESULT]
VariantChangeTypeEx: _Callable[[_Pointer[_struct.VARIANTARG],
                                _Pointer[_struct.VARIANTARG],
                                _type.LCID,
                                _type.USHORT,
                                _type.VARTYPE],
                               _type.HRESULT]
VariantClear: _Callable[[_Pointer[_struct.VARIANTARG]],
                        _type.HRESULT]
VariantCopy: _Callable[[_Pointer[_struct.VARIANTARG],
                        _Pointer[_struct.VARIANTARG]],
                       _type.HRESULT]
VariantCopyInd: _Callable[[_Pointer[_struct.VARIANTARG],
                           _Pointer[_struct.VARIANTARG]],
                          _type.HRESULT]
VariantInit: _Callable[[_Pointer[_struct.VARIANTARG]],
                       _type.c_void]
# olectl
OleCreatePictureIndirect: _Callable[[_Pointer[_struct.PICTDESC],
                                     _Pointer[_struct.IID],
                                     _type.BOOL,
                                     _type.LPVOID],
                                    _type.WINOLECTLAPI]
OleSavePictureFile: _Callable[[_ocidl.IPictureDisp,
                               _type.BSTR],
                              _type.WINOLECTLAPI]

_WinLib(__name__)
