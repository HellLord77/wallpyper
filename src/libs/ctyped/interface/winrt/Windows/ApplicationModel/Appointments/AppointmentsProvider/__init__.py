from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Appointments as _Windows_ApplicationModel_Appointments
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAddAppointmentOperation(_inspectable.IInspectable):
    get_AppointmentInformation: _Callable[[_Pointer[_Windows_ApplicationModel_Appointments.IAppointment]],  # value
                                          _type.HRESULT]
    get_SourcePackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    ReportCompleted: _Callable[[_type.HSTRING],  # itemId
                               _type.HRESULT]
    ReportCanceled: _Callable[[],
                              _type.HRESULT]
    ReportError: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    DismissUI: _Callable[[],
                         _type.HRESULT]


class IAppointmentsProviderLaunchActionVerbsStatics(_inspectable.IInspectable):
    get_AddAppointment: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_ReplaceAppointment: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_RemoveAppointment: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_ShowTimeFrame: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]

    _factory = True


class IAppointmentsProviderLaunchActionVerbsStatics2(_inspectable.IInspectable):
    get_ShowAppointmentDetails: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]

    _factory = True


class IRemoveAppointmentOperation(_inspectable.IInspectable):
    get_AppointmentId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_InstanceStartDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                     _type.HRESULT]
    get_SourcePackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    ReportCompleted: _Callable[[],
                               _type.HRESULT]
    ReportCanceled: _Callable[[],
                              _type.HRESULT]
    ReportError: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    DismissUI: _Callable[[],
                         _type.HRESULT]


class IReplaceAppointmentOperation(_inspectable.IInspectable):
    get_AppointmentId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_AppointmentInformation: _Callable[[_Pointer[_Windows_ApplicationModel_Appointments.IAppointment]],  # value
                                          _type.HRESULT]
    get_InstanceStartDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                     _type.HRESULT]
    get_SourcePackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    ReportCompleted: _Callable[[_type.HSTRING],  # itemId
                               _type.HRESULT]
    ReportCanceled: _Callable[[],
                              _type.HRESULT]
    ReportError: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    DismissUI: _Callable[[],
                         _type.HRESULT]
