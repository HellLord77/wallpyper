from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IDisplayMonitor(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ConnectionKind: _Callable[[_Pointer[_enum.Windows.Devices.Display.DisplayMonitorConnectionKind]],  # value
                                  _type.HRESULT]
    get_PhysicalConnector: _Callable[[_Pointer[_enum.Windows.Devices.Display.DisplayMonitorPhysicalConnectorKind]],  # value
                                     _type.HRESULT]
    get_DisplayAdapterDeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_DisplayAdapterId: _Callable[[_Pointer[_struct.Windows.Graphics.DisplayAdapterId]],  # value
                                    _type.HRESULT]
    get_DisplayAdapterTargetId: _Callable[[_Pointer[_type.UINT32]],  # value
                                          _type.HRESULT]
    get_UsageKind: _Callable[[_Pointer[_enum.Windows.Devices.Display.DisplayMonitorUsageKind]],  # value
                             _type.HRESULT]
    get_NativeResolutionInRawPixels: _Callable[[_Pointer[_struct.Windows.Graphics.SizeInt32]],  # value
                                               _type.HRESULT]
    get_PhysicalSizeInInches: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Size]]],  # value
                                        _type.HRESULT]
    get_RawDpiX: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    get_RawDpiY: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    get_RedPrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    get_GreenPrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                _type.HRESULT]
    get_BluePrimary: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                               _type.HRESULT]
    get_WhitePoint: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                              _type.HRESULT]
    get_MaxLuminanceInNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_MinLuminanceInNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                                      _type.HRESULT]
    get_MaxAverageFullFrameLuminanceInNits: _Callable[[_Pointer[_type.FLOAT]],  # value
                                                      _type.HRESULT]
    GetDescriptor: _Callable[[_enum.Windows.Devices.Display.DisplayMonitorDescriptorKind,  # descriptorKind
                              _Pointer[_type.UINT32],  # __resultSize
                              _Pointer[_Pointer[_type.BYTE]]],  # result
                             _type.HRESULT]


class IDisplayMonitor2(_inspectable.IInspectable):
    get_IsDolbyVisionSupportedInHdrMode: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]


class IDisplayMonitorStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IDisplayMonitor]]],  # operation
                           _type.HRESULT]
    FromInterfaceIdAsync: _Callable[[_type.HSTRING,  # deviceInterfaceId
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IDisplayMonitor]]],  # operation
                                    _type.HRESULT]
