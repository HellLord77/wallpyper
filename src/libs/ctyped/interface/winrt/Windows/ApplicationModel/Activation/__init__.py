from __future__ import annotations

from typing import Callable as _Callable

from .. import Background as _Windows_ApplicationModel_Background
from .. import Calls as _Windows_ApplicationModel_Calls
from .. import Contacts as _Windows_ApplicationModel_Contacts
from .. import Search as _Windows_ApplicationModel_Search
from ..Appointments import AppointmentsProvider as _Windows_ApplicationModel_Appointments_AppointmentsProvider
from ..Contacts import Provider as _Windows_ApplicationModel_Contacts_Provider
from ..DataTransfer import ShareTarget as _Windows_ApplicationModel_DataTransfer_ShareTarget
from ..UserDataAccounts import Provider as _Windows_ApplicationModel_UserDataAccounts_Provider
from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ... import System as _Windows_System
from ...Devices import Enumeration as _Windows_Devices_Enumeration
from ...Devices.Printers import Extensions as _Windows_Devices_Printers_Extensions
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Media import SpeechRecognition as _Windows_Media_SpeechRecognition
from ...Security.Authentication import Web as _Windows_Security_Authentication_Web
from ...Security.Authentication.Web import Provider as _Windows_Security_Authentication_Web_Provider
from ...Storage import Provider as _Windows_Storage_Provider
from ...Storage import Search as _Windows_Storage_Search
from ...Storage.Pickers import Provider as _Windows_Storage_Pickers_Provider
from ...UI import Notifications as _Windows_UI_Notifications
from ...UI import ViewManagement as _Windows_UI_ViewManagement
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IActivatedEventArgs(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Activation.ActivationKind]],  # value
                        _type.HRESULT]
    get_PreviousExecutionState: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Activation.ApplicationExecutionState]],  # value
                                          _type.HRESULT]
    get_SplashScreen: _Callable[[_Pointer[ISplashScreen]],  # value
                                _type.HRESULT]


class IActivatedEventArgsWithUser(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IApplicationViewActivatedEventArgs(_inspectable.IInspectable):
    get_CurrentlyShownApplicationViewId: _Callable[[_Pointer[_type.INT32]],  # value
                                                   _type.HRESULT]


class IAppointmentsProviderActivatedEventArgs(_inspectable.IInspectable):
    get_Verb: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IAppointmentsProviderAddAppointmentActivatedEventArgs(_inspectable.IInspectable):
    get_AddAppointmentOperation: _Callable[[_Pointer[_Windows_ApplicationModel_Appointments_AppointmentsProvider.IAddAppointmentOperation]],  # value
                                           _type.HRESULT]


class IAppointmentsProviderRemoveAppointmentActivatedEventArgs(_inspectable.IInspectable):
    get_RemoveAppointmentOperation: _Callable[[_Pointer[_Windows_ApplicationModel_Appointments_AppointmentsProvider.IRemoveAppointmentOperation]],  # value
                                              _type.HRESULT]


class IAppointmentsProviderReplaceAppointmentActivatedEventArgs(_inspectable.IInspectable):
    get_ReplaceAppointmentOperation: _Callable[[_Pointer[_Windows_ApplicationModel_Appointments_AppointmentsProvider.IReplaceAppointmentOperation]],  # value
                                               _type.HRESULT]


class IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs(_inspectable.IInspectable):
    get_InstanceStartDate: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                     _type.HRESULT]
    get_LocalId: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_RoamingId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IAppointmentsProviderShowTimeFrameActivatedEventArgs(_inspectable.IInspectable):
    get_TimeToShow: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                              _type.HRESULT]
    get_Duration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                            _type.HRESULT]


class IBackgroundActivatedEventArgs(_inspectable.IInspectable):
    get_TaskInstance: _Callable[[_Pointer[_Windows_ApplicationModel_Background.IBackgroundTaskInstance]],  # value
                                _type.HRESULT]


class IBarcodeScannerPreviewActivatedEventArgs(_inspectable.IInspectable):
    get_ConnectionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class ICachedFileUpdaterActivatedEventArgs(_inspectable.IInspectable):
    get_CachedFileUpdaterUI: _Callable[[_Pointer[_Windows_Storage_Provider.ICachedFileUpdaterUI]],  # value
                                       _type.HRESULT]


class ICameraSettingsActivatedEventArgs(_inspectable.IInspectable):
    get_VideoDeviceController: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                         _type.HRESULT]
    get_VideoDeviceExtension: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                        _type.HRESULT]


class ICommandLineActivatedEventArgs(_inspectable.IInspectable):
    get_Operation: _Callable[[_Pointer[ICommandLineActivationOperation]],  # value
                             _type.HRESULT]


class ICommandLineActivationOperation(_inspectable.IInspectable):
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_CurrentDirectoryPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    put_ExitCode: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_ExitCode: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class IContactActivatedEventArgs(_inspectable.IInspectable):
    get_Verb: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IContactCallActivatedEventArgs(_inspectable.IInspectable):
    get_ServiceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ServiceUserId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]


class IContactMapActivatedEventArgs(_inspectable.IInspectable):
    get_Address: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContactAddress]],  # value
                           _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]


class IContactMessageActivatedEventArgs(_inspectable.IInspectable):
    get_ServiceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ServiceUserId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]


class IContactPanelActivatedEventArgs(_inspectable.IInspectable):
    get_ContactPanel: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContactPanel]],  # value
                                _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]


class IContactPickerActivatedEventArgs(_inspectable.IInspectable):
    get_ContactPickerUI: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts_Provider.IContactPickerUI]],  # value
                                   _type.HRESULT]


class IContactPostActivatedEventArgs(_inspectable.IInspectable):
    get_ServiceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ServiceUserId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]


class IContactVideoCallActivatedEventArgs(_inspectable.IInspectable):
    get_ServiceId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_ServiceUserId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_Contact: _Callable[[_Pointer[_Windows_ApplicationModel_Contacts.IContact]],  # value
                           _type.HRESULT]


class IContactsProviderActivatedEventArgs(_inspectable.IInspectable):
    get_Verb: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IContinuationActivatedEventArgs(_inspectable.IInspectable):
    get_ContinuationData: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                    _type.HRESULT]


class IDeviceActivatedEventArgs(_inspectable.IInspectable):
    get_DeviceInformationId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_Verb: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IDevicePairingActivatedEventArgs(_inspectable.IInspectable):
    get_DeviceInformation: _Callable[[_Pointer[_Windows_Devices_Enumeration.IDeviceInformation]],  # value
                                     _type.HRESULT]


class IDialReceiverActivatedEventArgs(_inspectable.IInspectable):
    get_AppName: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]


class IFileActivatedEventArgs(_inspectable.IInspectable):
    get_Files: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageItem]]],  # value
                         _type.HRESULT]
    get_Verb: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IFileActivatedEventArgsWithCallerPackageFamilyName(_inspectable.IInspectable):
    get_CallerPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]


class IFileActivatedEventArgsWithNeighboringFiles(_inspectable.IInspectable):
    get_NeighboringFilesQuery: _Callable[[_Pointer[_Windows_Storage_Search.IStorageFileQueryResult]],  # value
                                         _type.HRESULT]


class IFileOpenPickerActivatedEventArgs(_inspectable.IInspectable):
    get_FileOpenPickerUI: _Callable[[_Pointer[_Windows_Storage_Pickers_Provider.IFileOpenPickerUI]],  # value
                                    _type.HRESULT]


class IFileOpenPickerActivatedEventArgs2(_inspectable.IInspectable):
    get_CallerPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]


class IFileOpenPickerContinuationEventArgs(_inspectable.IInspectable):
    Files: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageFile]]],  # value
                     _type.HRESULT]


class IFileSavePickerActivatedEventArgs(_inspectable.IInspectable):
    get_FileSavePickerUI: _Callable[[_Pointer[_Windows_Storage_Pickers_Provider.IFileSavePickerUI]],  # value
                                    _type.HRESULT]


class IFileSavePickerActivatedEventArgs2(_inspectable.IInspectable):
    get_CallerPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    get_EnterpriseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IFileSavePickerContinuationEventArgs(_inspectable.IInspectable):
    File: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                    _type.HRESULT]


class IFolderPickerContinuationEventArgs(_inspectable.IInspectable):
    Folder: _Callable[[_Pointer[_Windows_Storage.IStorageFolder]],  # value
                      _type.HRESULT]


class ILaunchActivatedEventArgs(_inspectable.IInspectable):
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_TileId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class ILaunchActivatedEventArgs2(_inspectable.IInspectable):
    get_TileActivatedInfo: _Callable[[_Pointer[ITileActivatedInfo]],  # value
                                     _type.HRESULT]


class ILockScreenActivatedEventArgs(_inspectable.IInspectable):
    get_Info: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                        _type.HRESULT]


class ILockScreenCallActivatedEventArgs(_inspectable.IInspectable):
    get_CallUI: _Callable[[_Pointer[_Windows_ApplicationModel_Calls.ILockScreenCallUI]],  # value
                          _type.HRESULT]


class IPhoneCallActivatedEventArgs(_inspectable.IInspectable):
    get_LineId: _Callable[[_Pointer[_struct.GUID]],  # value
                          _type.HRESULT]


class IPickerReturnedActivatedEventArgs(_inspectable.IInspectable):
    get_PickerOperationId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]


class IPrelaunchActivatedEventArgs(_inspectable.IInspectable):
    get_PrelaunchActivated: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]


class IPrint3DWorkflowActivatedEventArgs(_inspectable.IInspectable):
    get_Workflow: _Callable[[_Pointer[_Windows_Devices_Printers_Extensions.IPrint3DWorkflow]],  # value
                            _type.HRESULT]


class IPrintTaskSettingsActivatedEventArgs(_inspectable.IInspectable):
    get_Configuration: _Callable[[_Pointer[_Windows_Devices_Printers_Extensions.IPrintTaskConfiguration]],  # value
                                 _type.HRESULT]


class IProtocolActivatedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData(_inspectable.IInspectable):
    get_CallerPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                        _type.HRESULT]


class IProtocolForResultsActivatedEventArgs(_inspectable.IInspectable):
    get_ProtocolForResultsOperation: _Callable[[_Pointer[_Windows_System.IProtocolForResultsOperation]],  # value
                                               _type.HRESULT]


class IRestrictedLaunchActivatedEventArgs(_inspectable.IInspectable):
    get_SharedContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                 _type.HRESULT]


class ISearchActivatedEventArgs(_inspectable.IInspectable):
    get_QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class ISearchActivatedEventArgsWithLinguisticDetails(_inspectable.IInspectable):
    get_LinguisticDetails: _Callable[[_Pointer[_Windows_ApplicationModel_Search.ISearchPaneQueryLinguisticDetails]],  # value
                                     _type.HRESULT]


class IShareTargetActivatedEventArgs(_inspectable.IInspectable):
    get_ShareOperation: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer_ShareTarget.IShareOperation]],  # value
                                  _type.HRESULT]


class ISplashScreen(_inspectable.IInspectable):
    get_ImageLocation: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    add_Dismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISplashScreen, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # cookie
                             _type.HRESULT]
    remove_Dismissed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                _type.HRESULT]


class IStartupTaskActivatedEventArgs(_inspectable.IInspectable):
    get_TaskId: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class ITileActivatedInfo(_inspectable.IInspectable):
    get_RecentlyShownNotifications: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_UI_Notifications.IShownTileNotification]]],  # value
                                              _type.HRESULT]


class IToastNotificationActivatedEventArgs(_inspectable.IInspectable):
    get_Argument: _Callable[[_Pointer[_type.HSTRING]],  # argument
                            _type.HRESULT]
    get_UserInput: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                             _type.HRESULT]


class IUserDataAccountProviderActivatedEventArgs(_inspectable.IInspectable):
    get_Operation: _Callable[[_Pointer[_Windows_ApplicationModel_UserDataAccounts_Provider.IUserDataAccountProviderOperation]],  # value
                             _type.HRESULT]


class IViewSwitcherProvider(_inspectable.IInspectable):
    get_ViewSwitcher: _Callable[[_Pointer[_Windows_UI_ViewManagement.IActivationViewSwitcher]],  # value
                                _type.HRESULT]


class IVoiceCommandActivatedEventArgs(_inspectable.IInspectable):
    get_Result: _Callable[[_Pointer[_Windows_Media_SpeechRecognition.ISpeechRecognitionResult]],  # value
                          _type.HRESULT]


class IWalletActionActivatedEventArgs(_inspectable.IInspectable):
    ItemId: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    ActionKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Wallet.WalletActionKind]],  # value
                          _type.HRESULT]
    ActionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IWebAccountProviderActivatedEventArgs(_inspectable.IInspectable):
    get_Operation: _Callable[[_Pointer[_Windows_Security_Authentication_Web_Provider.IWebAccountProviderOperation]],  # value
                             _type.HRESULT]


class IWebAuthenticationBrokerContinuationEventArgs(_inspectable.IInspectable):
    get_WebAuthenticationResult: _Callable[[_Pointer[_Windows_Security_Authentication_Web.IWebAuthenticationResult]],  # result
                                           _type.HRESULT]
