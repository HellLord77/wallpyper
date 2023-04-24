from __future__ import annotations

from typing import Callable as _Callable

from ... import Bluetooth as _Windows_Devices_Bluetooth
from ... import Enumeration as _Windows_Devices_Enumeration
from .... import Foundation as _Windows_Foundation
from .... import Networking as _Windows_Networking
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Networking import Sockets as _Windows_Networking_Sockets
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IRfcommDeviceService(_inspectable.IInspectable):
    get_ConnectionHostName: _Callable[[_Pointer[_Windows_Networking.IHostName]],  # value
                                      _type.HRESULT]
    get_ConnectionServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]
    get_ServiceId: _Callable[[_Pointer[IRfcommServiceId]],  # value
                             _type.HRESULT]
    get_ProtectionLevel: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketProtectionLevel]],  # value
                                   _type.HRESULT]
    get_MaxProtectionLevel: _Callable[[_Pointer[_enum.Windows.Networking.Sockets.SocketProtectionLevel]],  # value
                                      _type.HRESULT]
    GetSdpRawAttributesAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.UINT32, _Windows_Storage_Streams.IBuffer]]]],  # asyncOp
                                        _type.HRESULT]
    GetSdpRawAttributesWithCacheModeAsync: _Callable[[_enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.UINT32, _Windows_Storage_Streams.IBuffer]]]],  # asyncOp
                                                     _type.HRESULT]


class IRfcommDeviceService2(_inspectable.IInspectable):
    get_Device: _Callable[[_Pointer[_Windows_Devices_Bluetooth.IBluetoothDevice]],  # value
                          _type.HRESULT]


class IRfcommDeviceService3(_inspectable.IInspectable):
    get_DeviceAccessInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceAccessInformation]],  # value
                                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Enumeration.DeviceAccessStatus]]],  # value
                                  _type.HRESULT]


class IRfcommDeviceServiceStatics(_inspectable.IInspectable):
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IRfcommDeviceService]]],  # asyncOp
                           _type.HRESULT]
    GetDeviceSelector: _Callable[[IRfcommServiceId,  # serviceId
                                  _Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]

    _factory = True


class IRfcommDeviceServiceStatics2(_inspectable.IInspectable):
    GetDeviceSelectorForBluetoothDevice: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDevice,  # bluetoothDevice
                                                    _Pointer[_type.HSTRING]],  # selector
                                                   _type.HRESULT]
    GetDeviceSelectorForBluetoothDeviceWithCacheMode: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDevice,  # bluetoothDevice
                                                                 _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                                 _Pointer[_type.HSTRING]],  # selector
                                                                _type.HRESULT]
    GetDeviceSelectorForBluetoothDeviceAndServiceId: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDevice,  # bluetoothDevice
                                                                IRfcommServiceId,  # serviceId
                                                                _Pointer[_type.HSTRING]],  # selector
                                                               _type.HRESULT]
    GetDeviceSelectorForBluetoothDeviceAndServiceIdWithCacheMode: _Callable[[_Windows_Devices_Bluetooth.IBluetoothDevice,  # bluetoothDevice
                                                                             IRfcommServiceId,  # serviceId
                                                                             _enum.Windows.Devices.Bluetooth.BluetoothCacheMode,  # cacheMode
                                                                             _Pointer[_type.HSTRING]],  # selector
                                                                            _type.HRESULT]

    _factory = True


class IRfcommDeviceServicesResult(_inspectable.IInspectable):
    get_Error: _Callable[[_Pointer[_enum.Windows.Devices.Bluetooth.BluetoothError]],  # value
                         _type.HRESULT]
    get_Services: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IRfcommDeviceService]]],  # services
                            _type.HRESULT]


class IRfcommServiceId(_inspectable.IInspectable):
    get_Uuid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    AsShortId: _Callable[[_Pointer[_type.UINT32]],  # shortId
                         _type.HRESULT]
    AsString: _Callable[[_Pointer[_type.HSTRING]],  # id
                        _type.HRESULT]


class IRfcommServiceIdStatics(_inspectable.IInspectable):
    FromUuid: _Callable[[_struct.GUID,  # uuid
                         _Pointer[IRfcommServiceId]],  # serviceId
                        _type.HRESULT]
    FromShortId: _Callable[[_type.UINT32,  # shortId
                            _Pointer[IRfcommServiceId]],  # serviceId
                           _type.HRESULT]
    get_SerialPort: _Callable[[_Pointer[IRfcommServiceId]],  # serviceId
                              _type.HRESULT]
    get_ObexObjectPush: _Callable[[_Pointer[IRfcommServiceId]],  # serviceId
                                  _type.HRESULT]
    get_ObexFileTransfer: _Callable[[_Pointer[IRfcommServiceId]],  # serviceId
                                    _type.HRESULT]
    get_PhoneBookAccessPce: _Callable[[_Pointer[IRfcommServiceId]],  # serviceId
                                      _type.HRESULT]
    get_PhoneBookAccessPse: _Callable[[_Pointer[IRfcommServiceId]],  # serviceId
                                      _type.HRESULT]
    get_GenericFileTransfer: _Callable[[_Pointer[IRfcommServiceId]],  # serviceId
                                       _type.HRESULT]

    _factory = True


class IRfcommServiceProvider(_inspectable.IInspectable):
    get_ServiceId: _Callable[[_Pointer[IRfcommServiceId]],  # value
                             _type.HRESULT]
    get_SdpRawAttributes: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.UINT32, _Windows_Storage_Streams.IBuffer]]],  # value
                                    _type.HRESULT]
    StartAdvertising: _Callable[[_Windows_Networking_Sockets.IStreamSocketListener],  # listener
                                _type.HRESULT]
    StopAdvertising: _Callable[[],
                               _type.HRESULT]


class IRfcommServiceProvider2(_inspectable.IInspectable):
    StartAdvertisingWithRadioDiscoverability: _Callable[[_Windows_Networking_Sockets.IStreamSocketListener,  # listener
                                                         _type.boolean],  # radioDiscoverable
                                                        _type.HRESULT]


class IRfcommServiceProviderStatics(_inspectable.IInspectable):
    CreateAsync: _Callable[[IRfcommServiceId,  # serviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IRfcommServiceProvider]]],  # asyncOp
                           _type.HRESULT]

    _factory = True
