from __future__ import annotations as _

from typing import Callable as _Callable

from . import _WinLib
from .. import type as _type
from .._utils import _Pointer
from ..interface.package import WebView2 as _WebView2

# WebView2
CreateCoreWebView2EnvironmentWithOptions: _Callable[[_type.PCWSTR,  # browserExecutableFolder
                                                     _type.PCWSTR,  # userDataFolder
                                                     _WebView2.ICoreWebView2EnvironmentOptions,  # environmentOptions
                                                     _WebView2.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler],  # environmentCreatedHandler
                                                    _type.HRESULT]
CreateCoreWebView2Environment: _Callable[[_WebView2.ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler],  # environmentCreatedHandler
                                         _type.HRESULT]
GetAvailableCoreWebView2BrowserVersionString: _Callable[[_type.PCWSTR,  # browserExecutableFolder
                                                         _Pointer[_type.LPWSTR]],  # versionInfo
                                                        _type.HRESULT]
CompareBrowserVersions: _Callable[[_type.PCWSTR,  # version1
                                   _type.PCWSTR,  # version2
                                   _Pointer[_type.c_int]],  # result
                                  _type.HRESULT]

_WinLib(__name__)
