from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IRemoteDesktopConnectionInfo(_inspectable.IInspectable):
    SetConnectionStatus: _Callable[[_enum.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionStatus],  # value
                                   _type.HRESULT]


class IRemoteDesktopConnectionInfoStatics(_inspectable.IInspectable, factory=True):
    GetForLaunchUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # launchUri
                                _struct.Windows.UI.WindowId,  # windowId
                                _Pointer[IRemoteDesktopConnectionInfo]],  # result
                               _type.HRESULT]
