from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type

MddBootstrapTestInitialize: _Callable[[_type.PCWSTR,  # ddlmPackageNamePrefix
                                       _type.PCWSTR,  # ddlPackagePublisherId
                                       _type.PCWSTR,  # frameworkPackageNamePrefix
                                       _type.PCWSTR],  # mainPackageNamePrefix
                                      _type.HRESULT]

# MddBootstrap
MddBootstrapInitialize: _Callable[[_type.UINT32,  # majorMinorVersion
                                   _type.PCWSTR,  # versionTag
                                   _struct.PACKAGE_VERSION],  # minVersion
                                  _type.HRESULT]
"""
Initialize the calling process to use Windows App Runtime framework package.
"""
MddBootstrapInitialize2: _Callable[[_type.UINT32,  # majorMinorVersion
                                    _type.PCWSTR,  # versionTag
                                    _struct.PACKAGE_VERSION,  # minVersion
                                    _enum.MddBootstrapInitializeOptions],  # options
                                   _type.HRESULT]
"""
Initialize the calling process to use Windows App Runtime framework package.
"""
MddBootstrapShutdown: _Callable[[],
                                _type.c_void]
"""
Undo the changes made by MddBoostrapInitialize().
"""

_WinLib(__name__, 'Microsoft.WindowsAppRuntime.Bootstrap.dll')
