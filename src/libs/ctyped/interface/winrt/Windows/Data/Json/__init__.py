from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IJsonArray(_inspectable.IInspectable):
    GetObjectAt: _Callable[[_type.UINT32,  # index
                            _Pointer[IJsonObject]],  # returnValue
                           _type.HRESULT]
    GetArrayAt: _Callable[[_type.UINT32,  # index
                           _Pointer[IJsonArray]],  # returnValue
                          _type.HRESULT]
    GetStringAt: _Callable[[_type.UINT32,  # index
                            _Pointer[_type.HSTRING]],  # returnValue
                           _type.HRESULT]
    GetNumberAt: _Callable[[_type.UINT32,  # index
                            _Pointer[_type.DOUBLE]],  # returnValue
                           _type.HRESULT]
    GetBooleanAt: _Callable[[_type.UINT32,  # index
                             _Pointer[_type.boolean]],  # returnValue
                            _type.HRESULT]


class IJsonArrayStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IJsonArray]],  # jsonArray
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IJsonArray],  # result
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IJsonErrorStatics2(_inspectable.IInspectable, factory=True):
    GetJsonStatus: _Callable[[_type.INT32,  # hresult
                              _Pointer[_enum.Windows.Data.Json.JsonErrorStatus]],  # status
                             _type.HRESULT]


class IJsonObject(_inspectable.IInspectable):
    GetNamedValue: _Callable[[_type.HSTRING,  # name
                              _Pointer[IJsonValue]],  # returnValue
                             _type.HRESULT]
    SetNamedValue: _Callable[[_type.HSTRING,  # name
                              IJsonValue],  # value
                             _type.HRESULT]
    GetNamedObject: _Callable[[_type.HSTRING,  # name
                               _Pointer[IJsonObject]],  # returnValue
                              _type.HRESULT]
    GetNamedArray: _Callable[[_type.HSTRING,  # name
                              _Pointer[IJsonArray]],  # returnValue
                             _type.HRESULT]
    GetNamedString: _Callable[[_type.HSTRING,  # name
                               _Pointer[_type.HSTRING]],  # returnValue
                              _type.HRESULT]
    GetNamedNumber: _Callable[[_type.HSTRING,  # name
                               _Pointer[_type.DOUBLE]],  # returnValue
                              _type.HRESULT]
    GetNamedBoolean: _Callable[[_type.HSTRING,  # name
                                _Pointer[_type.boolean]],  # returnValue
                               _type.HRESULT]


class IJsonObjectStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IJsonObject]],  # jsonObject
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IJsonObject],  # result
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]


class IJsonObjectWithDefaultValues(_inspectable.IInspectable):
    GetNamedValueOrDefault: _Callable[[_type.HSTRING,  # name
                                       IJsonValue,  # defaultValue
                                       _Pointer[IJsonValue]],  # returnValue
                                      _type.HRESULT]
    GetNamedObjectOrDefault: _Callable[[_type.HSTRING,  # name
                                        IJsonObject,  # defaultValue
                                        _Pointer[IJsonObject]],  # returnValue
                                       _type.HRESULT]
    GetNamedStringOrDefault: _Callable[[_type.HSTRING,  # name
                                        _type.HSTRING,  # defaultValue
                                        _Pointer[_type.HSTRING]],  # returnValue
                                       _type.HRESULT]
    GetNamedArrayOrDefault: _Callable[[_type.HSTRING,  # name
                                       IJsonArray,  # defaultValue
                                       _Pointer[IJsonArray]],  # returnValue
                                      _type.HRESULT]
    GetNamedNumberOrDefault: _Callable[[_type.HSTRING,  # name
                                        _type.DOUBLE,  # defaultValue
                                        _Pointer[_type.DOUBLE]],  # returnValue
                                       _type.HRESULT]
    GetNamedBooleanOrDefault: _Callable[[_type.HSTRING,  # name
                                         _type.boolean,  # defaultValue
                                         _Pointer[_type.boolean]],  # returnValue
                                        _type.HRESULT]


class IJsonValue(_inspectable.IInspectable):
    get_ValueType: _Callable[[_Pointer[_enum.Windows.Data.Json.JsonValueType]],  # value
                             _type.HRESULT]
    Stringify: _Callable[[_Pointer[_type.HSTRING]],  # returnValue
                         _type.HRESULT]
    GetString: _Callable[[_Pointer[_type.HSTRING]],  # returnValue
                         _type.HRESULT]
    GetNumber: _Callable[[_Pointer[_type.DOUBLE]],  # returnValue
                         _type.HRESULT]
    GetBoolean: _Callable[[_Pointer[_type.boolean]],  # returnValue
                          _type.HRESULT]
    GetArray: _Callable[[_Pointer[IJsonArray]],  # returnValue
                        _type.HRESULT]
    GetObject: _Callable[[_Pointer[IJsonObject]],  # returnValue
                         _type.HRESULT]


class IJsonValueStatics(_inspectable.IInspectable, factory=True):
    Parse: _Callable[[_type.HSTRING,  # input
                      _Pointer[IJsonValue]],  # jsonValue
                     _type.HRESULT]
    TryParse: _Callable[[_type.HSTRING,  # input
                         _Pointer[IJsonValue],  # result
                         _Pointer[_type.boolean]],  # succeeded
                        _type.HRESULT]
    CreateBooleanValue: _Callable[[_type.boolean,  # input
                                   _Pointer[IJsonValue]],  # jsonValue
                                  _type.HRESULT]
    CreateNumberValue: _Callable[[_type.DOUBLE,  # input
                                  _Pointer[IJsonValue]],  # jsonValue
                                 _type.HRESULT]
    CreateStringValue: _Callable[[_type.HSTRING,  # input
                                  _Pointer[IJsonValue]],  # jsonValue
                                 _type.HRESULT]


class IJsonValueStatics2(_inspectable.IInspectable, factory=True):
    CreateNullValue: _Callable[[_Pointer[IJsonValue]],  # jsonValue
                               _type.HRESULT]
