from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Appointments as _Windows_ApplicationModel_Appointments
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAppointmentCalendarCancelMeetingRequest(_inspectable.IInspectable):
    get_AppointmentCalendarLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_AppointmentLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_AppointmentOriginalStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_NotifyInvitees: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IAppointmentCalendarCancelMeetingRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IAppointmentCalendarCancelMeetingRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IAppointmentCalendarCreateOrUpdateAppointmentRequest(_inspectable.IInspectable):
    get_AppointmentCalendarLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_Appointment: _Callable[[_Pointer[_Windows_ApplicationModel_Appointments.IAppointment]],  # value
                               _type.HRESULT]
    get_NotifyInvitees: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    get_ChangedProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                     _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Windows_ApplicationModel_Appointments.IAppointment,  # createdOrUpdatedAppointment
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IAppointmentCalendarCreateOrUpdateAppointmentRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IAppointmentCalendarForwardMeetingRequest(_inspectable.IInspectable):
    get_AppointmentCalendarLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_AppointmentLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_AppointmentOriginalStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    get_Invitees: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Appointments.IAppointmentInvitee]]],  # value
                            _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_ForwardHeader: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IAppointmentCalendarForwardMeetingRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IAppointmentCalendarForwardMeetingRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IAppointmentCalendarProposeNewTimeForMeetingRequest(_inspectable.IInspectable):
    get_AppointmentCalendarLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_AppointmentLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_AppointmentOriginalStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    get_NewStartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    get_NewDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                               _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IAppointmentCalendarProposeNewTimeForMeetingRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IAppointmentCalendarSyncManagerSyncRequest(_inspectable.IInspectable):
    get_AppointmentCalendarLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IAppointmentCalendarSyncManagerSyncRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IAppointmentCalendarSyncManagerSyncRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IAppointmentCalendarUpdateMeetingResponseRequest(_inspectable.IInspectable):
    get_AppointmentCalendarLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    get_AppointmentLocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_AppointmentOriginalStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                                _type.HRESULT]
    get_Response: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse]],  # response
                            _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Comment: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_SendUpdate: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    ReportCompletedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                    _type.HRESULT]
    ReportFailedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                 _type.HRESULT]


class IAppointmentCalendarUpdateMeetingResponseRequestEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IAppointmentCalendarUpdateMeetingResponseRequest]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IAppointmentDataProviderConnection(_inspectable.IInspectable):
    add_SyncRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentDataProviderConnection, IAppointmentCalendarSyncManagerSyncRequestEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SyncRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_CreateOrUpdateAppointmentRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentDataProviderConnection, IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs],  # handler
                                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                                      _type.HRESULT]
    remove_CreateOrUpdateAppointmentRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                         _type.HRESULT]
    add_CancelMeetingRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentDataProviderConnection, IAppointmentCalendarCancelMeetingRequestEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_CancelMeetingRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_ForwardMeetingRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentDataProviderConnection, IAppointmentCalendarForwardMeetingRequestEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ForwardMeetingRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_ProposeNewTimeForMeetingRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentDataProviderConnection, IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs],  # handler
                                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                                     _type.HRESULT]
    remove_ProposeNewTimeForMeetingRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                        _type.HRESULT]
    add_UpdateMeetingResponseRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentDataProviderConnection, IAppointmentCalendarUpdateMeetingResponseRequestEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_UpdateMeetingResponseRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    Start: _Callable[[],
                     _type.HRESULT]


class IAppointmentDataProviderTriggerDetails(_inspectable.IInspectable):
    get_Connection: _Callable[[_Pointer[IAppointmentDataProviderConnection]],  # value
                              _type.HRESULT]
