from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ...... import type as _type
from ......_utils import _Pointer


class IEnvironmentManager(_inspectable.IInspectable):
    GetEnvironmentVariables: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # result
                                       _type.HRESULT]
    GetEnvironmentVariable: _Callable[[_type.HSTRING,  # name
                                       _Pointer[_type.HSTRING]],  # result
                                      _type.HRESULT]
    SetEnvironmentVariable: _Callable[[_type.HSTRING,  # name
                                       _type.HSTRING],  # value
                                      _type.HRESULT]
    AppendToPath: _Callable[[_type.HSTRING],  # path
                            _type.HRESULT]
    RemoveFromPath: _Callable[[_type.HSTRING],  # path
                              _type.HRESULT]
    AddExecutableFileExtension: _Callable[[_type.HSTRING],  # pathExt
                                          _type.HRESULT]
    RemoveExecutableFileExtension: _Callable[[_type.HSTRING],  # pathExt
                                             _type.HRESULT]


class IEnvironmentManager2(_inspectable.IInspectable):
    get_AreChangesTracked: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]


class IEnvironmentManagerStatics(_inspectable.IInspectable, factory=True):
    GetForProcess: _Callable[[_Pointer[IEnvironmentManager]],  # result
                             _type.HRESULT]
    GetForUser: _Callable[[_Pointer[IEnvironmentManager]],  # result
                          _type.HRESULT]
    GetForMachine: _Callable[[_Pointer[IEnvironmentManager]],  # result
                             _type.HRESULT]
    get_IsSupported: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
