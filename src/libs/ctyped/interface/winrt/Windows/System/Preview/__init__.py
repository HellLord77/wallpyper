from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ITwoPanelHingedDevicePosturePreview(_inspectable.IInspectable):
    GetCurrentPostureAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ITwoPanelHingedDevicePosturePreviewReading]]],  # value
                                      _type.HRESULT]
    PostureChanged: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class ITwoPanelHingedDevicePosturePreviewReading(_inspectable.IInspectable):
    Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                         _type.HRESULT]
    HingeState: _Callable[[_Pointer[_enum.Windows.System.Preview.HingeState]],  # value
                          _type.HRESULT]
    Panel1Orientation: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.SimpleOrientation]],  # value
                                 _type.HRESULT]
    Panel1Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    Panel2Orientation: _Callable[[_Pointer[_enum.Windows.Devices.Sensors.SimpleOrientation]],  # value
                                 _type.HRESULT]
    Panel2Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ITwoPanelHingedDevicePosturePreviewReadingChangedEventArgs(_inspectable.IInspectable):
    Reading: _Callable[[_Pointer[ITwoPanelHingedDevicePosturePreviewReading]],  # value
                       _type.HRESULT]


class ITwoPanelHingedDevicePosturePreviewStatics(_inspectable.IInspectable, factory=True):
    GetDefaultAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ITwoPanelHingedDevicePosturePreview]]],  # result
                               _type.HRESULT]
