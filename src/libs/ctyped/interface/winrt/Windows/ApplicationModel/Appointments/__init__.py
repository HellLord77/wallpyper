from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAppointment(_inspectable.IInspectable):
    get_StartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    put_StartTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    put_Duration: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                            _type.HRESULT]
    get_Location: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Location: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Subject: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Details: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Details: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Reminder: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                            _type.HRESULT]
    put_Reminder: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]
    get_Organizer: _Callable[[_Pointer[IAppointmentParticipant]],  # value
                             _type.HRESULT]
    put_Organizer: _Callable[[IAppointmentParticipant],  # value
                             _type.HRESULT]
    get_Invitees: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IAppointmentInvitee]]],  # value
                            _type.HRESULT]
    get_Recurrence: _Callable[[_Pointer[IAppointmentRecurrence]],  # value
                              _type.HRESULT]
    put_Recurrence: _Callable[[IAppointmentRecurrence],  # value
                              _type.HRESULT]
    get_BusyStatus: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentBusyStatus]],  # value
                              _type.HRESULT]
    put_BusyStatus: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentBusyStatus],  # value
                              _type.HRESULT]
    get_AllDay: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_AllDay: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Sensitivity: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentSensitivity]],  # value
                               _type.HRESULT]
    put_Sensitivity: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentSensitivity],  # value
                               _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]


class IAppointment2(_inspectable.IInspectable):
    get_LocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_CalendarId: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_RoamingId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_RoamingId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_OriginalStartTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                     _type.HRESULT]
    get_IsResponseRequested: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsResponseRequested: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_AllowNewTimeProposal: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_AllowNewTimeProposal: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_OnlineMeetingLink: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_OnlineMeetingLink: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_ReplyTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                             _type.HRESULT]
    put_ReplyTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_UserResponse: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse]],  # value
                                _type.HRESULT]
    put_UserResponse: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse],  # value
                                _type.HRESULT]
    get_HasInvitees: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_IsCanceledMeeting: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsCanceledMeeting: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_IsOrganizedByUser: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsOrganizedByUser: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]


class IAppointment3(_inspectable.IInspectable):
    get_ChangeNumber: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]
    get_RemoteChangeNumber: _Callable[[_Pointer[_type.UINT64]],  # value
                                      _type.HRESULT]
    put_RemoteChangeNumber: _Callable[[_type.UINT64],  # value
                                      _type.HRESULT]
    get_DetailsKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentDetailsKind]],  # value
                               _type.HRESULT]
    put_DetailsKind: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentDetailsKind],  # value
                               _type.HRESULT]


class IAppointmentCalendar(_inspectable.IInspectable):
    get_DisplayColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_LocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_IsHidden: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    get_OtherAppReadAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentCalendarOtherAppReadAccess]],  # value
                                      _type.HRESULT]
    put_OtherAppReadAccess: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentCalendarOtherAppReadAccess],  # value
                                      _type.HRESULT]
    get_OtherAppWriteAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentCalendarOtherAppWriteAccess]],  # value
                                       _type.HRESULT]
    put_OtherAppWriteAccess: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentCalendarOtherAppWriteAccess],  # value
                                       _type.HRESULT]
    get_SourceDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_SummaryCardView: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentSummaryCardView]],  # value
                                   _type.HRESULT]
    put_SummaryCardView: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentSummaryCardView],  # value
                                   _type.HRESULT]
    FindAppointmentsAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # rangeStart
                                      _struct.Windows.Foundation.TimeSpan,  # rangeLength
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # result
                                     _type.HRESULT]
    FindAppointmentsAsyncWithOptions: _Callable[[_struct.Windows.Foundation.DateTime,  # rangeStart
                                                 _struct.Windows.Foundation.TimeSpan,  # rangeLength
                                                 IFindAppointmentsOptions,  # options
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # result
                                                _type.HRESULT]
    FindExceptionsFromMasterAsync: _Callable[[_type.HSTRING,  # masterLocalId
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointmentException]]]],  # value
                                             _type.HRESULT]
    FindAllInstancesAsync: _Callable[[_type.HSTRING,  # masterLocalId
                                      _struct.Windows.Foundation.DateTime,  # rangeStart
                                      _struct.Windows.Foundation.TimeSpan,  # rangeLength
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # value
                                     _type.HRESULT]
    FindAllInstancesAsyncWithOptions: _Callable[[_type.HSTRING,  # masterLocalId
                                                 _struct.Windows.Foundation.DateTime,  # rangeStart
                                                 _struct.Windows.Foundation.TimeSpan,  # rangeLength
                                                 IFindAppointmentsOptions,  # pOptions
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # value
                                                _type.HRESULT]
    GetAppointmentAsync: _Callable[[_type.HSTRING,  # localId
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IAppointment]]],  # result
                                   _type.HRESULT]
    GetAppointmentInstanceAsync: _Callable[[_type.HSTRING,  # localId
                                            _struct.Windows.Foundation.DateTime,  # instanceStartTime
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IAppointment]]],  # result
                                           _type.HRESULT]
    FindUnexpandedAppointmentsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # result
                                               _type.HRESULT]
    FindUnexpandedAppointmentsAsyncWithOptions: _Callable[[IFindAppointmentsOptions,  # options
                                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # result
                                                          _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                           _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                         _type.HRESULT]
    DeleteAppointmentAsync: _Callable[[_type.HSTRING,  # localId
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                      _type.HRESULT]
    DeleteAppointmentInstanceAsync: _Callable[[_type.HSTRING,  # localId
                                               _struct.Windows.Foundation.DateTime,  # instanceStartTime
                                               _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                              _type.HRESULT]
    SaveAppointmentAsync: _Callable[[IAppointment,  # pAppointment
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                    _type.HRESULT]


class IAppointmentCalendar2(_inspectable.IInspectable):
    get_SyncManager: _Callable[[_Pointer[IAppointmentCalendarSyncManager]],  # value
                               _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    put_DisplayColor: _Callable[[_struct.Windows.UI.Color],  # value
                                _type.HRESULT]
    put_IsHidden: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_UserDataAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_CanCreateOrUpdateAppointments: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_CanCreateOrUpdateAppointments: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_CanCancelMeetings: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_CanCancelMeetings: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_CanForwardMeetings: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_CanForwardMeetings: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_CanProposeNewTimeForMeetings: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_CanProposeNewTimeForMeetings: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]
    get_CanUpdateMeetingResponses: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_CanUpdateMeetingResponses: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_CanNotifyInvitees: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_CanNotifyInvitees: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_MustNofityInvitees: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_MustNofityInvitees: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    TryCreateOrUpdateAppointmentAsync: _Callable[[IAppointment,  # appointment
                                                  _type.boolean,  # notifyInvitees
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                 _type.HRESULT]
    TryCancelMeetingAsync: _Callable[[IAppointment,  # meeting
                                      _type.HSTRING,  # subject
                                      _type.HSTRING,  # comment
                                      _type.boolean,  # notifyInvitees
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                     _type.HRESULT]
    TryForwardMeetingAsync: _Callable[[IAppointment,  # meeting
                                       _Windows_Foundation_Collections.IIterable[IAppointmentInvitee],  # invitees
                                       _type.HSTRING,  # subject
                                       _type.HSTRING,  # forwardHeader
                                       _type.HSTRING,  # comment
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                      _type.HRESULT]
    TryProposeNewTimeForMeetingAsync: _Callable[[IAppointment,  # meeting
                                                 _struct.Windows.Foundation.DateTime,  # newStartTime
                                                 _struct.Windows.Foundation.TimeSpan,  # newDuration
                                                 _type.HSTRING,  # subject
                                                 _type.HSTRING,  # comment
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                _type.HRESULT]
    TryUpdateMeetingResponseAsync: _Callable[[IAppointment,  # meeting
                                              _enum.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse,  # response
                                              _type.HSTRING,  # subject
                                              _type.HSTRING,  # comment
                                              _type.boolean,  # sendUpdate
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                             _type.HRESULT]


class IAppointmentCalendar3(_inspectable.IInspectable):
    RegisterSyncManagerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]


class IAppointmentCalendarSyncManager(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentCalendarSyncStatus]],  # value
                          _type.HRESULT]
    get_LastSuccessfulSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                          _type.HRESULT]
    get_LastAttemptedSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                         _type.HRESULT]
    SyncAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                         _type.HRESULT]
    add_SyncStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentCalendarSyncManager, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SyncStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IAppointmentCalendarSyncManager2(_inspectable.IInspectable):
    put_Status: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentCalendarSyncStatus],  # value
                          _type.HRESULT]
    put_LastSuccessfulSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                          _type.HRESULT]
    put_LastAttemptedSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                         _type.HRESULT]


class IAppointmentConflictResult(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentConflictType]],  # value
                        _type.HRESULT]
    get_Date: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                        _type.HRESULT]


class IAppointmentException(_inspectable.IInspectable):
    get_Appointment: _Callable[[_Pointer[IAppointment]],  # value
                               _type.HRESULT]
    get_ExceptionProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                       _type.HRESULT]
    get_IsDeleted: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IAppointmentInvitee(_inspectable.IInspectable):
    get_Role: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentParticipantRole]],  # value
                        _type.HRESULT]
    put_Role: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentParticipantRole],  # value
                        _type.HRESULT]
    get_Response: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse]],  # value
                            _type.HRESULT]
    put_Response: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse],  # value
                            _type.HRESULT]


class IAppointmentManagerForUser(_inspectable.IInspectable):
    ShowAddAppointmentAsync: _Callable[[IAppointment,  # appointment
                                        _struct.Windows.Foundation.Rect,  # selection
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                       _type.HRESULT]
    ShowAddAppointmentWithPlacementAsync: _Callable[[IAppointment,  # appointment
                                                     _struct.Windows.Foundation.Rect,  # selection
                                                     _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                                    _type.HRESULT]
    ShowReplaceAppointmentAsync: _Callable[[_type.HSTRING,  # appointmentId
                                            IAppointment,  # appointment
                                            _struct.Windows.Foundation.Rect,  # selection
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                           _type.HRESULT]
    ShowReplaceAppointmentWithPlacementAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                         IAppointment,  # appointment
                                                         _struct.Windows.Foundation.Rect,  # selection
                                                         _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                                        _type.HRESULT]
    ShowReplaceAppointmentWithPlacementAndDateAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                                IAppointment,  # appointment
                                                                _struct.Windows.Foundation.Rect,  # selection
                                                                _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                                _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                                               _type.HRESULT]
    ShowRemoveAppointmentAsync: _Callable[[_type.HSTRING,  # appointmentId
                                           _struct.Windows.Foundation.Rect,  # selection
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                          _type.HRESULT]
    ShowRemoveAppointmentWithPlacementAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                        _struct.Windows.Foundation.Rect,  # selection
                                                        _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                       _type.HRESULT]
    ShowRemoveAppointmentWithPlacementAndDateAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                               _struct.Windows.Foundation.Rect,  # selection
                                                               _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                               _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                              _type.HRESULT]
    ShowTimeFrameAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # timeToShow
                                   _struct.Windows.Foundation.TimeSpan,  # duration
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                  _type.HRESULT]
    ShowAppointmentDetailsAsync: _Callable[[_type.HSTRING,  # appointmentId
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                           _type.HRESULT]
    ShowAppointmentDetailsWithDateAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                    _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                                   _type.HRESULT]
    ShowEditNewAppointmentAsync: _Callable[[IAppointment,  # appointment
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # result
                                           _type.HRESULT]
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentStoreAccessType,  # options
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IAppointmentStore]]],  # result
                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IAppointmentManagerStatics(_inspectable.IInspectable, factory=True):
    ShowAddAppointmentAsync: _Callable[[IAppointment,  # appointment
                                        _struct.Windows.Foundation.Rect,  # selection
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                       _type.HRESULT]
    ShowAddAppointmentWithPlacementAsync: _Callable[[IAppointment,  # appointment
                                                     _struct.Windows.Foundation.Rect,  # selection
                                                     _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                                    _type.HRESULT]
    ShowReplaceAppointmentAsync: _Callable[[_type.HSTRING,  # appointmentId
                                            IAppointment,  # appointment
                                            _struct.Windows.Foundation.Rect,  # selection
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                           _type.HRESULT]
    ShowReplaceAppointmentWithPlacementAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                         IAppointment,  # appointment
                                                         _struct.Windows.Foundation.Rect,  # selection
                                                         _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                                        _type.HRESULT]
    ShowReplaceAppointmentWithPlacementAndDateAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                                IAppointment,  # appointment
                                                                _struct.Windows.Foundation.Rect,  # selection
                                                                _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                                _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                                               _type.HRESULT]
    ShowRemoveAppointmentAsync: _Callable[[_type.HSTRING,  # appointmentId
                                           _struct.Windows.Foundation.Rect,  # selection
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    ShowRemoveAppointmentWithPlacementAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                        _struct.Windows.Foundation.Rect,  # selection
                                                        _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                       _type.HRESULT]
    ShowRemoveAppointmentWithPlacementAndDateAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                               _struct.Windows.Foundation.Rect,  # selection
                                                               _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                               _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                              _type.HRESULT]
    ShowTimeFrameAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # timeToShow
                                   _struct.Windows.Foundation.TimeSpan,  # duration
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                  _type.HRESULT]


class IAppointmentManagerStatics2(_inspectable.IInspectable, factory=True):
    ShowAppointmentDetailsAsync: _Callable[[_type.HSTRING,  # appointmentId
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                           _type.HRESULT]
    ShowAppointmentDetailsWithDateAsync: _Callable[[_type.HSTRING,  # appointmentId
                                                    _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                                   _type.HRESULT]
    ShowEditNewAppointmentAsync: _Callable[[IAppointment,  # appointment
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                           _type.HRESULT]
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentStoreAccessType,  # options
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IAppointmentStore]]],  # operation
                                 _type.HRESULT]


class IAppointmentManagerStatics3(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IAppointmentManagerForUser]],  # result
                          _type.HRESULT]


class IAppointmentParticipant(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Address: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Address: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]


class IAppointmentPropertiesStatics(_inspectable.IInspectable, factory=True):
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Location: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_StartTime: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Reminder: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_BusyStatus: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Sensitivity: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_OriginalStartTime: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_IsResponseRequested: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_AllowNewTimeProposal: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_AllDay: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Details: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_OnlineMeetingLink: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_ReplyTime: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Organizer: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_UserResponse: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_HasInvitees: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsCanceledMeeting: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_IsOrganizedByUser: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_Recurrence: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Invitees: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_DefaultProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]


class IAppointmentPropertiesStatics2(_inspectable.IInspectable, factory=True):
    get_ChangeNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_RemoteChangeNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_DetailsKind: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]


class IAppointmentRecurrence(_inspectable.IInspectable):
    get_Unit: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentRecurrenceUnit]],  # value
                        _type.HRESULT]
    put_Unit: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentRecurrenceUnit],  # value
                        _type.HRESULT]
    get_Occurrences: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                               _type.HRESULT]
    put_Occurrences: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                               _type.HRESULT]
    get_Until: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                         _type.HRESULT]
    put_Until: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                         _type.HRESULT]
    get_Interval: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    put_Interval: _Callable[[_type.UINT32],  # value
                            _type.HRESULT]
    get_DaysOfWeek: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentDaysOfWeek]],  # value
                              _type.HRESULT]
    put_DaysOfWeek: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentDaysOfWeek],  # value
                              _type.HRESULT]
    get_WeekOfMonth: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentWeekOfMonth]],  # value
                               _type.HRESULT]
    put_WeekOfMonth: _Callable[[_enum.Windows.ApplicationModel.Appointments.AppointmentWeekOfMonth],  # value
                               _type.HRESULT]
    get_Month: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    put_Month: _Callable[[_type.UINT32],  # value
                         _type.HRESULT]
    get_Day: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    put_Day: _Callable[[_type.UINT32],  # value
                       _type.HRESULT]


class IAppointmentRecurrence2(_inspectable.IInspectable):
    get_RecurrenceType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.RecurrenceType]],  # value
                                  _type.HRESULT]
    get_TimeZone: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_TimeZone: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IAppointmentRecurrence3(_inspectable.IInspectable):
    get_CalendarIdentifier: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]


class IAppointmentStore(_inspectable.IInspectable):
    get_ChangeTracker: _Callable[[_Pointer[IAppointmentStoreChangeTracker]],  # value
                                 _type.HRESULT]
    CreateAppointmentCalendarAsync: _Callable[[_type.HSTRING,  # name
                                               _Pointer[_Windows_Foundation.IAsyncOperation[IAppointmentCalendar]]],  # operation
                                              _type.HRESULT]
    GetAppointmentCalendarAsync: _Callable[[_type.HSTRING,  # calendarId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IAppointmentCalendar]]],  # result
                                           _type.HRESULT]
    GetAppointmentAsync: _Callable[[_type.HSTRING,  # localId
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IAppointment]]],  # result
                                   _type.HRESULT]
    GetAppointmentInstanceAsync: _Callable[[_type.HSTRING,  # localId
                                            _struct.Windows.Foundation.DateTime,  # instanceStartTime
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IAppointment]]],  # result
                                           _type.HRESULT]
    FindAppointmentCalendarsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointmentCalendar]]]],  # result
                                             _type.HRESULT]
    FindAppointmentCalendarsAsyncWithOptions: _Callable[[_enum.Windows.ApplicationModel.Appointments.FindAppointmentCalendarsOptions,  # options
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointmentCalendar]]]],  # result
                                                        _type.HRESULT]
    FindAppointmentsAsync: _Callable[[_struct.Windows.Foundation.DateTime,  # rangeStart
                                      _struct.Windows.Foundation.TimeSpan,  # rangeLength
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # result
                                     _type.HRESULT]
    FindAppointmentsAsyncWithOptions: _Callable[[_struct.Windows.Foundation.DateTime,  # rangeStart
                                                 _struct.Windows.Foundation.TimeSpan,  # rangeLength
                                                 IFindAppointmentsOptions,  # options
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointment]]]],  # result
                                                _type.HRESULT]
    FindConflictAsync: _Callable[[IAppointment,  # appointment
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IAppointmentConflictResult]]],  # result
                                 _type.HRESULT]
    FindConflictAsyncWithInstanceStart: _Callable[[IAppointment,  # appointment
                                                   _struct.Windows.Foundation.DateTime,  # instanceStartTime
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IAppointmentConflictResult]]],  # result
                                                  _type.HRESULT]
    MoveAppointmentAsync: _Callable[[IAppointment,  # appointment
                                     IAppointmentCalendar,  # destinationCalendar
                                     _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                    _type.HRESULT]
    ShowAddAppointmentAsync: _Callable[[IAppointment,  # appointment
                                        _struct.Windows.Foundation.Rect,  # selection
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                       _type.HRESULT]
    ShowReplaceAppointmentAsync: _Callable[[_type.HSTRING,  # localId
                                            IAppointment,  # appointment
                                            _struct.Windows.Foundation.Rect,  # selection
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                           _type.HRESULT]
    ShowReplaceAppointmentWithPlacementAndDateAsync: _Callable[[_type.HSTRING,  # localId
                                                                IAppointment,  # appointment
                                                                _struct.Windows.Foundation.Rect,  # selection
                                                                _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                                _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                                               _type.HRESULT]
    ShowRemoveAppointmentAsync: _Callable[[_type.HSTRING,  # localId
                                           _struct.Windows.Foundation.Rect,  # selection
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                          _type.HRESULT]
    ShowRemoveAppointmentWithPlacementAndDateAsync: _Callable[[_type.HSTRING,  # localId
                                                               _struct.Windows.Foundation.Rect,  # selection
                                                               _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                               _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                               _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                                              _type.HRESULT]
    ShowAppointmentDetailsAsync: _Callable[[_type.HSTRING,  # localId
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                           _type.HRESULT]
    ShowAppointmentDetailsWithDateAsync: _Callable[[_type.HSTRING,  # localId
                                                    _struct.Windows.Foundation.DateTime,  # instanceStartDate
                                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # asyncAction
                                                   _type.HRESULT]
    ShowEditNewAppointmentAsync: _Callable[[IAppointment,  # appointment
                                            _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                           _type.HRESULT]
    FindLocalIdsFromRoamingIdAsync: _Callable[[_type.HSTRING,  # roamingId
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # operation
                                              _type.HRESULT]


class IAppointmentStore2(_inspectable.IInspectable):
    add_StoreChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IAppointmentStore, IAppointmentStoreChangedEventArgs],  # pHandler
                                 _Pointer[_struct.EventRegistrationToken]],  # pToken
                                _type.HRESULT]
    remove_StoreChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    CreateAppointmentCalendarInAccountAsync: _Callable[[_type.HSTRING,  # name
                                                        _type.HSTRING,  # userDataAccountId
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IAppointmentCalendar]]],  # operation
                                                       _type.HRESULT]


class IAppointmentStore3(_inspectable.IInspectable):
    GetChangeTracker: _Callable[[_type.HSTRING,  # identity
                                 _Pointer[IAppointmentStoreChangeTracker]],  # result
                                _type.HRESULT]


class IAppointmentStoreChange(_inspectable.IInspectable):
    get_Appointment: _Callable[[_Pointer[IAppointment]],  # value
                               _type.HRESULT]
    get_ChangeType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Appointments.AppointmentStoreChangeType]],  # value
                              _type.HRESULT]


class IAppointmentStoreChange2(_inspectable.IInspectable):
    get_AppointmentCalendar: _Callable[[_Pointer[IAppointmentCalendar]],  # value
                                       _type.HRESULT]


class IAppointmentStoreChangeReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IAppointmentStoreChange]]]],  # result
                              _type.HRESULT]
    AcceptChanges: _Callable[[],
                             _type.HRESULT]
    AcceptChangesThrough: _Callable[[IAppointmentStoreChange],  # lastChangeToAccept
                                    _type.HRESULT]


class IAppointmentStoreChangeTracker(_inspectable.IInspectable):
    GetChangeReader: _Callable[[_Pointer[IAppointmentStoreChangeReader]],  # value
                               _type.HRESULT]
    Enable: _Callable[[],
                      _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class IAppointmentStoreChangeTracker2(_inspectable.IInspectable):
    get_IsTracking: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IAppointmentStoreChangedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IAppointmentStoreChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IAppointmentStoreChangedDeferral]],  # result
                           _type.HRESULT]


class IAppointmentStoreNotificationTriggerDetails(_inspectable.IInspectable):
    pass


class IFindAppointmentsOptions(_inspectable.IInspectable):
    get_CalendarIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                               _type.HRESULT]
    get_FetchProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                   _type.HRESULT]
    get_IncludeHidden: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_IncludeHidden: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_MaxCount: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    put_MaxCount: _Callable[[_type.UINT32],  # value
                            _type.HRESULT]
