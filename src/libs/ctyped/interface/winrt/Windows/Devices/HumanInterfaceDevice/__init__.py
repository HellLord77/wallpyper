from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IHidBooleanControl(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_UsagePage: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_UsageId: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_IsActive: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsActive: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_ControlDescription: _Callable[[_Pointer[IHidBooleanControlDescription]],  # value
                                      _type.HRESULT]


class IHidBooleanControlDescription(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_ReportId: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_ReportType: _Callable[[_Pointer[_enum.Windows.Devices.HumanInterfaceDevice.HidReportType]],  # value
                              _type.HRESULT]
    get_UsagePage: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_UsageId: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_ParentCollections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHidCollection]]],  # value
                                     _type.HRESULT]


class IHidBooleanControlDescription2(_inspectable.IInspectable):
    get_IsAbsolute: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IHidCollection(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Devices.HumanInterfaceDevice.HidCollectionType]],  # value
                        _type.HRESULT]
    get_UsagePage: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_UsageId: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]


class IHidDevice(_inspectable.IInspectable):
    get_VendorId: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_ProductId: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_UsagePage: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_UsageId: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    GetInputReportAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IHidInputReport]]],  # value
                                   _type.HRESULT]
    GetInputReportByIdAsync: _Callable[[_type.UINT16,  # reportId
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IHidInputReport]]],  # value
                                       _type.HRESULT]
    GetFeatureReportAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IHidFeatureReport]]],  # value
                                     _type.HRESULT]
    GetFeatureReportByIdAsync: _Callable[[_type.UINT16,  # reportId
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IHidFeatureReport]]],  # value
                                         _type.HRESULT]
    CreateOutputReport: _Callable[[_Pointer[IHidOutputReport]],  # outputReport
                                  _type.HRESULT]
    CreateOutputReportById: _Callable[[_type.UINT16,  # reportId
                                       _Pointer[IHidOutputReport]],  # outputReport
                                      _type.HRESULT]
    CreateFeatureReport: _Callable[[_Pointer[IHidFeatureReport]],  # featureReport
                                   _type.HRESULT]
    CreateFeatureReportById: _Callable[[_type.UINT16,  # reportId
                                        _Pointer[IHidFeatureReport]],  # featureReport
                                       _type.HRESULT]
    SendOutputReportAsync: _Callable[[IHidOutputReport,  # outputReport
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                     _type.HRESULT]
    SendFeatureReportAsync: _Callable[[IHidFeatureReport,  # featureReport
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.UINT32]]],  # operation
                                      _type.HRESULT]
    GetBooleanControlDescriptions: _Callable[[_enum.Windows.Devices.HumanInterfaceDevice.HidReportType,  # reportType
                                              _type.UINT16,  # usagePage
                                              _type.UINT16,  # usageId
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[IHidBooleanControlDescription]]],  # value
                                             _type.HRESULT]
    GetNumericControlDescriptions: _Callable[[_enum.Windows.Devices.HumanInterfaceDevice.HidReportType,  # reportType
                                              _type.UINT16,  # usagePage
                                              _type.UINT16,  # usageId
                                              _Pointer[_Windows_Foundation_Collections.IVectorView[IHidNumericControlDescription]]],  # value
                                             _type.HRESULT]
    add_InputReportReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[IHidDevice, IHidInputReportReceivedEventArgs],  # reportHandler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_InputReportReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class IHidDeviceStatics(_inspectable.IInspectable, factory=True):
    GetDeviceSelector: _Callable[[_type.UINT16,  # usagePage
                                  _type.UINT16,  # usageId
                                  _Pointer[_type.HSTRING]],  # selector
                                 _type.HRESULT]
    GetDeviceSelectorVidPid: _Callable[[_type.UINT16,  # usagePage
                                        _type.UINT16,  # usageId
                                        _type.UINT16,  # vendorId
                                        _type.UINT16,  # productId
                                        _Pointer[_type.HSTRING]],  # selector
                                       _type.HRESULT]
    FromIdAsync: _Callable[[_type.HSTRING,  # deviceId
                            _enum.Windows.Storage.FileAccessMode,  # accessMode
                            _Pointer[_Windows_Foundation.IAsyncOperation[IHidDevice]]],  # hidDevice
                           _type.HRESULT]


class IHidFeatureReport(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT16]],  # value
                      _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                        _type.HRESULT]
    GetBooleanControl: _Callable[[_type.UINT16,  # usagePage
                                  _type.UINT16,  # usageId
                                  _Pointer[IHidBooleanControl]],  # value
                                 _type.HRESULT]
    GetBooleanControlByDescription: _Callable[[IHidBooleanControlDescription,  # controlDescription
                                               _Pointer[IHidBooleanControl]],  # value
                                              _type.HRESULT]
    GetNumericControl: _Callable[[_type.UINT16,  # usagePage
                                  _type.UINT16,  # usageId
                                  _Pointer[IHidNumericControl]],  # value
                                 _type.HRESULT]
    GetNumericControlByDescription: _Callable[[IHidNumericControlDescription,  # controlDescription
                                               _Pointer[IHidNumericControl]],  # value
                                              _type.HRESULT]


class IHidInputReport(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT16]],  # value
                      _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    get_ActivatedBooleanControls: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHidBooleanControl]]],  # value
                                            _type.HRESULT]
    get_TransitionedBooleanControls: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHidBooleanControl]]],  # value
                                               _type.HRESULT]
    GetBooleanControl: _Callable[[_type.UINT16,  # usagePage
                                  _type.UINT16,  # usageId
                                  _Pointer[IHidBooleanControl]],  # value
                                 _type.HRESULT]
    GetBooleanControlByDescription: _Callable[[IHidBooleanControlDescription,  # controlDescription
                                               _Pointer[IHidBooleanControl]],  # value
                                              _type.HRESULT]
    GetNumericControl: _Callable[[_type.UINT16,  # usagePage
                                  _type.UINT16,  # usageId
                                  _Pointer[IHidNumericControl]],  # value
                                 _type.HRESULT]
    GetNumericControlByDescription: _Callable[[IHidNumericControlDescription,  # controlDescription
                                               _Pointer[IHidNumericControl]],  # value
                                              _type.HRESULT]


class IHidInputReportReceivedEventArgs(_inspectable.IInspectable):
    get_Report: _Callable[[_Pointer[IHidInputReport]],  # value
                          _type.HRESULT]


class IHidNumericControl(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_IsGrouped: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_UsagePage: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_UsageId: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.INT64]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.INT64],  # value
                         _type.HRESULT]
    get_ScaledValue: _Callable[[_Pointer[_type.INT64]],  # value
                               _type.HRESULT]
    put_ScaledValue: _Callable[[_type.INT64],  # value
                               _type.HRESULT]
    get_ControlDescription: _Callable[[_Pointer[IHidNumericControlDescription]],  # value
                                      _type.HRESULT]


class IHidNumericControlDescription(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_ReportId: _Callable[[_Pointer[_type.UINT16]],  # value
                            _type.HRESULT]
    get_ReportType: _Callable[[_Pointer[_enum.Windows.Devices.HumanInterfaceDevice.HidReportType]],  # value
                              _type.HRESULT]
    get_ReportSize: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_ReportCount: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    get_UsagePage: _Callable[[_Pointer[_type.UINT16]],  # value
                             _type.HRESULT]
    get_UsageId: _Callable[[_Pointer[_type.UINT16]],  # value
                           _type.HRESULT]
    get_LogicalMinimum: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_LogicalMaximum: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_PhysicalMinimum: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_PhysicalMaximum: _Callable[[_Pointer[_type.INT32]],  # value
                                   _type.HRESULT]
    get_UnitExponent: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    get_Unit: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_IsAbsolute: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_HasNull: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_ParentCollections: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IHidCollection]]],  # value
                                     _type.HRESULT]


class IHidOutputReport(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT16]],  # value
                      _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Storage_Streams.IBuffer]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[_Windows_Storage_Streams.IBuffer],  # value
                        _type.HRESULT]
    GetBooleanControl: _Callable[[_type.UINT16,  # usagePage
                                  _type.UINT16,  # usageId
                                  _Pointer[IHidBooleanControl]],  # value
                                 _type.HRESULT]
    GetBooleanControlByDescription: _Callable[[IHidBooleanControlDescription,  # controlDescription
                                               _Pointer[IHidBooleanControl]],  # value
                                              _type.HRESULT]
    GetNumericControl: _Callable[[_type.UINT16,  # usagePage
                                  _type.UINT16,  # usageId
                                  _Pointer[IHidNumericControl]],  # value
                                 _type.HRESULT]
    GetNumericControlByDescription: _Callable[[IHidNumericControlDescription,  # controlDescription
                                               _Pointer[IHidNumericControl]],  # value
                                              _type.HRESULT]
