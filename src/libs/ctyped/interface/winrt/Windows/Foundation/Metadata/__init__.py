from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import type as _type
from ......_utils import _Pointer


class IApiInformationStatics(_inspectable.IInspectable):
    IsTypePresent: _Callable[[_type.HSTRING,  # typeName
                              _Pointer[_type.boolean]],  # result
                             _type.HRESULT]
    IsMethodPresent: _Callable[[_type.HSTRING,  # typeName
                                _type.HSTRING,  # methodName
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    IsMethodPresentWithArity: _Callable[[_type.HSTRING,  # typeName
                                         _type.HSTRING,  # methodName
                                         _type.UINT32,  # inputParameterCount
                                         _Pointer[_type.boolean]],  # result
                                        _type.HRESULT]
    IsEventPresent: _Callable[[_type.HSTRING,  # typeName
                               _type.HSTRING,  # eventName
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    IsPropertyPresent: _Callable[[_type.HSTRING,  # typeName
                                  _type.HSTRING,  # propertyName
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    IsReadOnlyPropertyPresent: _Callable[[_type.HSTRING,  # typeName
                                          _type.HSTRING,  # propertyName
                                          _Pointer[_type.boolean]],  # result
                                         _type.HRESULT]
    IsWriteablePropertyPresent: _Callable[[_type.HSTRING,  # typeName
                                           _type.HSTRING,  # propertyName
                                           _Pointer[_type.boolean]],  # result
                                          _type.HRESULT]
    IsEnumNamedValuePresent: _Callable[[_type.HSTRING,  # enumTypeName
                                        _type.HSTRING,  # valueName
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    IsApiContractPresentByMajor: _Callable[[_type.HSTRING,  # contractName
                                            _type.UINT16,  # majorVersion
                                            _Pointer[_type.boolean]],  # result
                                           _type.HRESULT]
    IsApiContractPresentByMajorAndMinor: _Callable[[_type.HSTRING,  # contractName
                                                    _type.UINT16,  # majorVersion
                                                    _type.UINT16,  # minorVersion
                                                    _Pointer[_type.boolean]],  # result
                                                   _type.HRESULT]

    _factory = True
