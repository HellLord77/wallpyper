from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAddPackageDependencyOptions(_inspectable.IInspectable):
    get_Rank: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    put_Rank: _Callable[[_type.INT32],  # value
                        _type.HRESULT]
    get_PrependIfRankCollision: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_PrependIfRankCollision: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class ICreatePackageDependencyOptions(_inspectable.IInspectable):
    get_Architectures: _Callable[[_Pointer[_enum.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyProcessorArchitectures]],  # value
                                 _type.HRESULT]
    put_Architectures: _Callable[[_enum.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyProcessorArchitectures],  # value
                                 _type.HRESULT]
    get_VerifyDependencyResolution: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_VerifyDependencyResolution: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_LifetimeArtifactKind: _Callable[[_Pointer[_enum.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyLifetimeArtifactKind]],  # value
                                        _type.HRESULT]
    put_LifetimeArtifactKind: _Callable[[_enum.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyLifetimeArtifactKind],  # value
                                        _type.HRESULT]
    get_LifetimeArtifact: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_LifetimeArtifact: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]


class IPackageDependency(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    Delete: _Callable[[],
                      _type.HRESULT]
    Add: _Callable[[_Pointer[IPackageDependencyContext]],  # result
                   _type.HRESULT]
    Add2: _Callable[[IAddPackageDependencyOptions,  # options
                     _Pointer[IPackageDependencyContext]],  # result
                    _type.HRESULT]


class IPackageDependencyContext(_inspectable.IInspectable):
    get_ContextId: _Callable[[_Pointer[_struct.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContextId]],  # value
                             _type.HRESULT]
    get_PackageDependencyId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_PackageFullName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    Remove: _Callable[[],
                      _type.HRESULT]


class IPackageDependencyContextFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_struct.Microsoft.Windows.ApplicationModel.DynamicDependency.PackageDependencyContextId,  # contextId
                               _Pointer[IPackageDependencyContext]],  # value
                              _type.HRESULT]


class IPackageDependencyRankStatics(_inspectable.IInspectable, factory=True):
    get_Default: _Callable[[_Pointer[_type.INT32]],  # value
                           _type.HRESULT]


class IPackageDependencyStatics(_inspectable.IInspectable, factory=True):
    GetFromId: _Callable[[_type.HSTRING,  # id
                          _Pointer[IPackageDependency]],  # result
                         _type.HRESULT]
    GetFromIdForSystem: _Callable[[_type.HSTRING,  # id
                                   _Pointer[IPackageDependency]],  # result
                                  _type.HRESULT]
    Create: _Callable[[_type.HSTRING,  # packageFamilyName
                       _struct.Windows.ApplicationModel.PackageVersion,  # minVersion
                       _Pointer[IPackageDependency]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_type.HSTRING,  # packageFamilyName
                        _struct.Windows.ApplicationModel.PackageVersion,  # minVersion
                        ICreatePackageDependencyOptions,  # options
                        _Pointer[IPackageDependency]],  # result
                       _type.HRESULT]
    CreateForSystem: _Callable[[_type.HSTRING,  # packageFamilyName
                                _struct.Windows.ApplicationModel.PackageVersion,  # minVersion
                                ICreatePackageDependencyOptions,  # options
                                _Pointer[IPackageDependency]],  # result
                               _type.HRESULT]
    get_GenerationId: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]


class IPackageDependencyStatics2(_inspectable.IInspectable, factory=True):
    get_PackageGraphRevisionId: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
