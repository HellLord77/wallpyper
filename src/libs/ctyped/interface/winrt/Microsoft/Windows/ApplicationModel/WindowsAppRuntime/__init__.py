from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IDeploymentInitializeOptions(_inspectable.IInspectable):
    get_ForceDeployment: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_ForceDeployment: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]


class IDeploymentInitializeOptions2(_inspectable.IInspectable):
    get_OnErrorShowUI: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_OnErrorShowUI: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class IDeploymentManagerStatics(_inspectable.IInspectable, factory=True):
    GetStatus: _Callable[[_Pointer[IDeploymentResult]],  # result
                         _type.HRESULT]
    Initialize: _Callable[[_Pointer[IDeploymentResult]],  # result
                          _type.HRESULT]


class IDeploymentManagerStatics2(_inspectable.IInspectable, factory=True):
    Initialize: _Callable[[IDeploymentInitializeOptions,  # deploymentInitializeOptions
                           _Pointer[IDeploymentResult]],  # result
                          _type.HRESULT]


class IDeploymentResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IDeploymentResultFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_enum.Microsoft.Windows.ApplicationModel.WindowsAppRuntime.DeploymentStatus,  # status
                               _type.HRESULT,  # extendedError
                               _Pointer[IDeploymentResult]],  # value
                              _type.HRESULT]
