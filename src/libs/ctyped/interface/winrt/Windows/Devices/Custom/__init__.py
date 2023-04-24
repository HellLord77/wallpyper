from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ICustomDevice(_inspectable.IInspectable):
    get_InputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                               _type.HRESULT]
    get_OutputStream: _Callable[[_Pointer[_Windows_Storage_Streams.IOutputStream]],  # value
                                _type.HRESULT]
    SendIOControlAsync: _Callable[[IIOControlCode,  # ioControlCode
                                   _Windows_Storage_Streams.IBuffer,  # inputBuffer
                                   _Windows_Storage_Streams.IBuffer,  # outputBuffer
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                  _type.HRESULT]
    TrySendIOControlAsync: _Callable[[IIOControlCode,  # ioControlCode
                                      _Windows_Storage_Streams.IBuffer,  # inputBuffer
                                      _Windows_Storage_Streams.IBuffer,  # outputBuffer
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]


class ICustomDeviceStatics(_inspectable.IInspectable):
    GetDeviceSelector: _Callable[[_struct.GUID,  # classGuid
                                  _Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _enum.Windows.Devices.Custom.DeviceAccessMode,  # desiredAccess
                            _enum.Windows.Devices.Custom.DeviceSharingMode,  # sharingMode
                            _Pointer[_Windows_Foundation.IAsyncOperation[ICustomDevice]]],  # operation
                           _type.HRESULT]

    _factory = True


class IIOControlCode(_inspectable.IInspectable):
    get_AccessMode: _Callable[[_Pointer[_enum.Windows.Devices.Custom.IOControlAccessMode]],  # value
                              _type.HRESULT]
    get_BufferingMethod: _Callable[[_Pointer[_enum.Windows.Devices.Custom.IOControlBufferingMethod]],  # value
                                   _type.HRESULT]
    get_Function: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_DeviceType: _Callable[[_Pointer[_type.UINT16]],  # value
                              _type.HRESULT]
    get_ControlCode: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]


class IIOControlCodeFactory(_inspectable.IInspectable):
    CreateIOControlCode: _Callable[[_type.UINT16,  # deviceType
                                    _type.UINT16,  # function
                                    _enum.Windows.Devices.Custom.IOControlAccessMode,  # accessMode
                                    _enum.Windows.Devices.Custom.IOControlBufferingMethod,  # bufferingMethod
                                    _Pointer[IIOControlCode]],  # instance
                                   _type.HRESULT]

    _factory = True


class IKnownDeviceTypesStatics(_inspectable.IInspectable):
    get_Unknown: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]

    _factory = True
