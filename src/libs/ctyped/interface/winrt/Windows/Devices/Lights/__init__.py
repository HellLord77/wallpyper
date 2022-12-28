from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ILamp(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_BrightnessLevel: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]
    put_BrightnessLevel: _Callable[[_type.FLOAT],  # value
                                   _type.HRESULT]
    get_IsColorSettable: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    add_AvailabilityChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ILamp, ILampAvailabilityChangedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_AvailabilityChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class ILampArray(_inspectable.IInspectable):
    get_DeviceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_HardwareVendorId: _Callable[[_Pointer[_type.UINT16]],  # value
                                    _type.HRESULT]
    get_HardwareProductId: _Callable[[_Pointer[_type.UINT16]],  # value
                                     _type.HRESULT]
    get_HardwareVersion: _Callable[[_Pointer[_type.UINT16]],  # value
                                   _type.HRESULT]
    get_LampArrayKind: _Callable[[_Pointer[_enum.Windows.Devices.Lights.LampArrayKind]],  # value
                                 _type.HRESULT]
    get_LampCount: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_MinUpdateInterval: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    get_BoundingBox: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                               _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_BrightnessLevel: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                   _type.HRESULT]
    put_BrightnessLevel: _Callable[[_type.DOUBLE],  # value
                                   _type.HRESULT]
    get_IsConnected: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_SupportsVirtualKeys: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    GetLampInfo: _Callable[[_type.INT32,  # lampIndex
                            _Pointer[ILampInfo]],  # result
                           _type.HRESULT]
    GetIndicesForKey: _Callable[[_enum.Windows.System.VirtualKey,  # key
                                 _Pointer[_type.UINT32],  # __resultSize
                                 _Pointer[_Pointer[_type.INT32]]],  # result
                                _type.HRESULT]
    GetIndicesForPurposes: _Callable[[_enum.Windows.Devices.Lights.LampPurposes,  # purposes
                                      _Pointer[_type.UINT32],  # __resultSize
                                      _Pointer[_Pointer[_type.INT32]]],  # result
                                     _type.HRESULT]
    SetColor: _Callable[[_struct.Windows.UI.Color],  # desiredColor
                        _type.HRESULT]
    SetColorForIndex: _Callable[[_type.INT32,  # lampIndex
                                 _struct.Windows.UI.Color],  # desiredColor
                                _type.HRESULT]
    SetSingleColorForIndices: _Callable[[_struct.Windows.UI.Color,  # desiredColor
                                         _type.UINT32,  # __lampIndexesSize
                                         _Pointer[_type.INT32]],  # lampIndexes
                                        _type.HRESULT]
    SetColorsForIndices: _Callable[[_type.UINT32,  # __desiredColorsSize
                                    _Pointer[_struct.Windows.UI.Color],  # desiredColors
                                    _type.UINT32,  # __lampIndexesSize
                                    _Pointer[_type.INT32]],  # lampIndexes
                                   _type.HRESULT]
    SetColorsForKey: _Callable[[_struct.Windows.UI.Color,  # desiredColor
                                _enum.Windows.System.VirtualKey],  # key
                               _type.HRESULT]
    SetColorsForKeys: _Callable[[_type.UINT32,  # __desiredColorsSize
                                 _Pointer[_struct.Windows.UI.Color],  # desiredColors
                                 _type.UINT32,  # __keysSize
                                 _Pointer[_enum.Windows.System.VirtualKey]],  # keys
                                _type.HRESULT]
    SetColorsForPurposes: _Callable[[_struct.Windows.UI.Color,  # desiredColor
                                     _enum.Windows.Devices.Lights.LampPurposes],  # purposes
                                    _type.HRESULT]
    SendMessageAsync: _Callable[[_type.INT32,  # messageId
                                 _Windows_Storage_Streams.IBuffer,  # message
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]
    RequestMessageAsync: _Callable[[_type.INT32,  # messageId
                                    _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IBuffer]]],  # operation
                                   _type.HRESULT]


class ILampArrayStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # result
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ILampArray]]],  # operation
                           _type.HRESULT]

    _factory = True


class ILampAvailabilityChangedEventArgs(_inspectable.IInspectable):
    get_IsAvailable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class ILampInfo(_inspectable.IInspectable):
    get_Index: _Callable[[_Pointer[_type.INT32]],  # value
                         _type.HRESULT]
    get_Purposes: _Callable[[_Pointer[_enum.Windows.Devices.Lights.LampPurposes]],  # value
                            _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Vector3]],  # value
                            _type.HRESULT]
    get_RedLevelCount: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    get_GreenLevelCount: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_BlueLevelCount: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_GainLevelCount: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_FixedColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                              _type.HRESULT]
    GetNearestSupportedColor: _Callable[[_struct.Windows.UI.Color,  # desiredColor
                                         _Pointer[_struct.Windows.UI.Color]],  # result
                                        _type.HRESULT]
    get_UpdateLatency: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]


class ILampStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[ILamp]]],  # operation
                           _type.HRESULT]
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ILamp]]],  # operation
                               _type.HRESULT]

    _factory = True
