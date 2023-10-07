from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IRadio(_inspectable.IInspectable):
    SetStateAsync: _Callable[[_enum.Windows.Devices.Radios.RadioState,  # value
                              _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Radios.RadioAccessStatus]]],  # retval
                             _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IRadio, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                   _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Devices.Radios.RadioState]],  # value
                         _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.Devices.Radios.RadioKind]],  # value
                        _type.HRESULT]


class IRadioStatics(_inspectable.IInspectable, factory=True):
    GetRadiosAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IRadio]]]],  # value
                              _type.HRESULT]
    GetDeviceSelector: _Callable[[_Pointer[_type.HSTRING]],  # deviceSelector
                                 _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _Pointer[_Windows_Foundation.IAsyncOperation[IRadio]]],  # value
                           _type.HRESULT]
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Devices.Radios.RadioAccessStatus]]],  # value
                                  _type.HRESULT]
