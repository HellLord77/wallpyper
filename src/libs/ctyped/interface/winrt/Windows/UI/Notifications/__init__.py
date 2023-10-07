from __future__ import annotations as _

from typing import Callable as _Callable

from ... import ApplicationModel as _Windows_ApplicationModel
from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Data.Xml import Dom as _Windows_Data_Xml_Dom
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAdaptiveNotificationContent(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.Notifications.AdaptiveNotificationContentKind]],  # value
                        _type.HRESULT]
    get_Hints: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                         _type.HRESULT]


class IAdaptiveNotificationText(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IBadgeNotification(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                           _type.HRESULT]
    put_ExpirationTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]


class IBadgeNotificationFactory(_inspectable.IInspectable, factory=True):
    CreateBadgeNotification: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # content
                                        _Pointer[IBadgeNotification]],  # value
                                       _type.HRESULT]


class IBadgeUpdateManagerForUser(_inspectable.IInspectable):
    CreateBadgeUpdaterForApplication: _Callable[[_Pointer[IBadgeUpdater]],  # result
                                                _type.HRESULT]
    CreateBadgeUpdaterForApplicationWithId: _Callable[[_type.HSTRING,  # applicationId
                                                       _Pointer[IBadgeUpdater]],  # result
                                                      _type.HRESULT]
    CreateBadgeUpdaterForSecondaryTile: _Callable[[_type.HSTRING,  # tileId
                                                   _Pointer[IBadgeUpdater]],  # result
                                                  _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IBadgeUpdateManagerStatics(_inspectable.IInspectable, factory=True):
    CreateBadgeUpdaterForApplication: _Callable[[_Pointer[IBadgeUpdater]],  # result
                                                _type.HRESULT]
    CreateBadgeUpdaterForApplicationWithId: _Callable[[_type.HSTRING,  # applicationId
                                                       _Pointer[IBadgeUpdater]],  # result
                                                      _type.HRESULT]
    CreateBadgeUpdaterForSecondaryTile: _Callable[[_type.HSTRING,  # tileId
                                                   _Pointer[IBadgeUpdater]],  # result
                                                  _type.HRESULT]
    GetTemplateContent: _Callable[[_enum.Windows.UI.Notifications.BadgeTemplateType,  # type
                                   _Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # result
                                  _type.HRESULT]


class IBadgeUpdateManagerStatics2(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IBadgeUpdateManagerForUser]],  # result
                          _type.HRESULT]


class IBadgeUpdater(_inspectable.IInspectable):
    Update: _Callable[[IBadgeNotification],  # notification
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    StartPeriodicUpdate: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # badgeContent
                                    _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                   _type.HRESULT]
    StartPeriodicUpdateAtTime: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # badgeContent
                                          _struct.Windows.Foundation.DateTime,  # startTime
                                          _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                         _type.HRESULT]
    StopPeriodicUpdate: _Callable[[],
                                  _type.HRESULT]


class IKnownAdaptiveNotificationHintsStatics(_inspectable.IInspectable, factory=True):
    get_Style: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Wrap: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_MaxLines: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_MinLines: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_TextStacking: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_Align: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IKnownAdaptiveNotificationTextStylesStatics(_inspectable.IInspectable, factory=True):
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Body: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Base: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Subtitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Subheader: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Header: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_TitleNumeral: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_SubheaderNumeral: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_HeaderNumeral: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_CaptionSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_BodySubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_BaseSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_SubtitleSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_TitleSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_SubheaderSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_SubheaderNumeralSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_HeaderSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    get_HeaderNumeralSubtle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]


class IKnownNotificationBindingsStatics(_inspectable.IInspectable, factory=True):
    get_ToastGeneric: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class INotification(_inspectable.IInspectable):
    get_ExpirationTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]
    put_ExpirationTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_Visual: _Callable[[_Pointer[INotificationVisual]],  # value
                          _type.HRESULT]
    put_Visual: _Callable[[INotificationVisual],  # value
                          _type.HRESULT]


class INotificationBinding(_inspectable.IInspectable):
    get_Template: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Template: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Hints: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                         _type.HRESULT]
    GetTextElements: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IAdaptiveNotificationText]]],  # result
                               _type.HRESULT]


class INotificationData(_inspectable.IInspectable):
    get_Values: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _type.HSTRING]]],  # value
                          _type.HRESULT]
    get_SequenceNumber: _Callable[[_Pointer[_type.UINT32]],  # value
                                  _type.HRESULT]
    put_SequenceNumber: _Callable[[_type.UINT32],  # value
                                  _type.HRESULT]


class INotificationDataFactory(_inspectable.IInspectable, factory=True):
    CreateNotificationDataWithValuesAndSequenceNumber: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # initialValues
                                                                  _type.UINT32,  # sequenceNumber
                                                                  _Pointer[INotificationData]],  # value
                                                                 _type.HRESULT]
    CreateNotificationDataWithValues: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation_Collections.IKeyValuePair[_type.HSTRING, _type.HSTRING]],  # initialValues
                                                 _Pointer[INotificationData]],  # value
                                                _type.HRESULT]


class INotificationVisual(_inspectable.IInspectable):
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Bindings: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[INotificationBinding]]],  # value
                            _type.HRESULT]
    GetBinding: _Callable[[_type.HSTRING,  # templateName
                           _Pointer[INotificationBinding]],  # result
                          _type.HRESULT]


class IScheduledTileNotification(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                           _type.HRESULT]
    get_DeliveryTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    put_ExpirationTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]
    put_Tag: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]


class IScheduledTileNotificationFactory(_inspectable.IInspectable, factory=True):
    CreateScheduledTileNotification: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # content
                                                _struct.Windows.Foundation.DateTime,  # deliveryTime
                                                _Pointer[IScheduledTileNotification]],  # value
                                               _type.HRESULT]


class IScheduledToastNotification(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                           _type.HRESULT]
    get_DeliveryTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]
    get_SnoozeInterval: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                  _type.HRESULT]
    get_MaximumSnoozeCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]


class IScheduledToastNotification2(_inspectable.IInspectable):
    put_Tag: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    put_Group: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Group: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_SuppressPopup: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SuppressPopup: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IScheduledToastNotification3(_inspectable.IInspectable):
    get_NotificationMirroring: _Callable[[_Pointer[_enum.Windows.UI.Notifications.NotificationMirroring]],  # value
                                         _type.HRESULT]
    put_NotificationMirroring: _Callable[[_enum.Windows.UI.Notifications.NotificationMirroring],  # value
                                         _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IScheduledToastNotification4(_inspectable.IInspectable):
    get_ExpirationTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]
    put_ExpirationTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]


class IScheduledToastNotificationFactory(_inspectable.IInspectable, factory=True):
    CreateScheduledToastNotification: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # content
                                                 _struct.Windows.Foundation.DateTime,  # deliveryTime
                                                 _Pointer[IScheduledToastNotification]],  # value
                                                _type.HRESULT]
    CreateScheduledToastNotificationRecurring: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # content
                                                          _struct.Windows.Foundation.DateTime,  # deliveryTime
                                                          _struct.Windows.Foundation.TimeSpan,  # snoozeInterval
                                                          _type.UINT32,  # maximumSnoozeCount
                                                          _Pointer[IScheduledToastNotification]],  # value
                                                         _type.HRESULT]


class IScheduledToastNotificationShowingEventArgs(_inspectable.IInspectable):
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_ScheduledToastNotification: _Callable[[_Pointer[IScheduledToastNotification]],  # value
                                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IShownTileNotification(_inspectable.IInspectable):
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class ITileFlyoutNotification(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                           _type.HRESULT]
    put_ExpirationTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]


class ITileFlyoutNotificationFactory(_inspectable.IInspectable, factory=True):
    CreateTileFlyoutNotification: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # content
                                             _Pointer[ITileFlyoutNotification]],  # value
                                            _type.HRESULT]


class ITileFlyoutUpdateManagerStatics(_inspectable.IInspectable, factory=True):
    CreateTileFlyoutUpdaterForApplication: _Callable[[_Pointer[ITileFlyoutUpdater]],  # result
                                                     _type.HRESULT]
    CreateTileFlyoutUpdaterForApplicationWithId: _Callable[[_type.HSTRING,  # applicationId
                                                            _Pointer[ITileFlyoutUpdater]],  # result
                                                           _type.HRESULT]
    CreateTileFlyoutUpdaterForSecondaryTile: _Callable[[_type.HSTRING,  # tileId
                                                        _Pointer[ITileFlyoutUpdater]],  # result
                                                       _type.HRESULT]
    GetTemplateContent: _Callable[[_enum.Windows.UI.Notifications.TileFlyoutTemplateType,  # type
                                   _Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # result
                                  _type.HRESULT]


class ITileFlyoutUpdater(_inspectable.IInspectable):
    Update: _Callable[[ITileFlyoutNotification],  # notification
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    StartPeriodicUpdate: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # tileFlyoutContent
                                    _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                   _type.HRESULT]
    StartPeriodicUpdateAtTime: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # tileFlyoutContent
                                          _struct.Windows.Foundation.DateTime,  # startTime
                                          _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                         _type.HRESULT]
    StopPeriodicUpdate: _Callable[[],
                                  _type.HRESULT]
    get_Setting: _Callable[[_Pointer[_enum.Windows.UI.Notifications.NotificationSetting]],  # value
                           _type.HRESULT]


class ITileNotification(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                           _type.HRESULT]
    put_ExpirationTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]
    put_Tag: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]


class ITileNotificationFactory(_inspectable.IInspectable, factory=True):
    CreateTileNotification: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # content
                                       _Pointer[ITileNotification]],  # value
                                      _type.HRESULT]


class ITileUpdateManagerForUser(_inspectable.IInspectable):
    CreateTileUpdaterForApplication: _Callable[[_Pointer[ITileUpdater]],  # result
                                               _type.HRESULT]
    CreateTileUpdaterForApplicationWithId: _Callable[[_type.HSTRING,  # applicationId
                                                      _Pointer[ITileUpdater]],  # result
                                                     _type.HRESULT]
    CreateTileUpdaterForSecondaryTile: _Callable[[_type.HSTRING,  # tileId
                                                  _Pointer[ITileUpdater]],  # result
                                                 _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class ITileUpdateManagerStatics(_inspectable.IInspectable, factory=True):
    CreateTileUpdaterForApplication: _Callable[[_Pointer[ITileUpdater]],  # result
                                               _type.HRESULT]
    CreateTileUpdaterForApplicationWithId: _Callable[[_type.HSTRING,  # applicationId
                                                      _Pointer[ITileUpdater]],  # result
                                                     _type.HRESULT]
    CreateTileUpdaterForSecondaryTile: _Callable[[_type.HSTRING,  # tileId
                                                  _Pointer[ITileUpdater]],  # result
                                                 _type.HRESULT]
    GetTemplateContent: _Callable[[_enum.Windows.UI.Notifications.TileTemplateType,  # type
                                   _Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # result
                                  _type.HRESULT]


class ITileUpdateManagerStatics2(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[ITileUpdateManagerForUser]],  # result
                          _type.HRESULT]


class ITileUpdater(_inspectable.IInspectable):
    Update: _Callable[[ITileNotification],  # notification
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    EnableNotificationQueue: _Callable[[_type.boolean],  # enable
                                       _type.HRESULT]
    get_Setting: _Callable[[_Pointer[_enum.Windows.UI.Notifications.NotificationSetting]],  # value
                           _type.HRESULT]
    AddToSchedule: _Callable[[IScheduledTileNotification],  # scheduledTile
                             _type.HRESULT]
    RemoveFromSchedule: _Callable[[IScheduledTileNotification],  # scheduledTile
                                  _type.HRESULT]
    GetScheduledTileNotifications: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IScheduledTileNotification]]],  # result
                                             _type.HRESULT]
    StartPeriodicUpdate: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # tileContent
                                    _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                   _type.HRESULT]
    StartPeriodicUpdateAtTime: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # tileContent
                                          _struct.Windows.Foundation.DateTime,  # startTime
                                          _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                         _type.HRESULT]
    StopPeriodicUpdate: _Callable[[],
                                  _type.HRESULT]
    StartPeriodicUpdateBatch: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # tileContents
                                         _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                        _type.HRESULT]
    StartPeriodicUpdateBatchAtTime: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Foundation.IUriRuntimeClass],  # tileContents
                                               _struct.Windows.Foundation.DateTime,  # startTime
                                               _enum.Windows.UI.Notifications.PeriodicUpdateRecurrence],  # requestedInterval
                                              _type.HRESULT]


class ITileUpdater2(_inspectable.IInspectable):
    EnableNotificationQueueForSquare150x150: _Callable[[_type.boolean],  # enable
                                                       _type.HRESULT]
    EnableNotificationQueueForWide310x150: _Callable[[_type.boolean],  # enable
                                                     _type.HRESULT]
    EnableNotificationQueueForSquare310x310: _Callable[[_type.boolean],  # enable
                                                       _type.HRESULT]


class IToastActivatedEventArgs(_inspectable.IInspectable):
    get_Arguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IToastActivatedEventArgs2(_inspectable.IInspectable):
    get_UserInput: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                             _type.HRESULT]


class IToastCollection(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_LaunchArgs: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_LaunchArgs: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_Icon: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                        _type.HRESULT]
    put_Icon: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                        _type.HRESULT]


class IToastCollectionFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_type.HSTRING,  # collectionId
                               _type.HSTRING,  # displayName
                               _type.HSTRING,  # launchArgs
                               _Windows_Foundation.IUriRuntimeClass,  # iconUri
                               _Pointer[IToastCollection]],  # value
                              _type.HRESULT]


class IToastCollectionManager(_inspectable.IInspectable):
    SaveToastCollectionAsync: _Callable[[IToastCollection,  # collection
                                         _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                        _type.HRESULT]
    FindAllToastCollectionsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IToastCollection]]]],  # operation
                                            _type.HRESULT]
    GetToastCollectionAsync: _Callable[[_type.HSTRING,  # collectionId
                                        _Pointer[_Windows_Foundation.IAsyncOperation[IToastCollection]]],  # operation
                                       _type.HRESULT]
    RemoveToastCollectionAsync: _Callable[[_type.HSTRING,  # collectionId
                                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                          _type.HRESULT]
    RemoveAllToastCollectionsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                              _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]
    get_AppId: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IToastDismissedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.UI.Notifications.ToastDismissalReason]],  # value
                          _type.HRESULT]


class IToastFailedEventArgs(_inspectable.IInspectable):
    get_ErrorCode: _Callable[[_Pointer[_type.HRESULT]],  # value
                             _type.HRESULT]


class IToastNotification(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # value
                           _type.HRESULT]
    put_ExpirationTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                  _type.HRESULT]
    get_ExpirationTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                  _type.HRESULT]
    add_Dismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[IToastNotification, IToastDismissedEventArgs],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Dismissed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Activated: _Callable[[_Windows_Foundation.ITypedEventHandler[IToastNotification, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Activated: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_Failed: _Callable[[_Windows_Foundation.ITypedEventHandler[IToastNotification, IToastFailedEventArgs],  # handler
                           _Pointer[_struct.EventRegistrationToken]],  # token
                          _type.HRESULT]
    remove_Failed: _Callable[[_struct.EventRegistrationToken],  # token
                             _type.HRESULT]


class IToastNotification2(_inspectable.IInspectable):
    put_Tag: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    put_Group: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Group: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_SuppressPopup: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]
    get_SuppressPopup: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class IToastNotification3(_inspectable.IInspectable):
    get_NotificationMirroring: _Callable[[_Pointer[_enum.Windows.UI.Notifications.NotificationMirroring]],  # value
                                         _type.HRESULT]
    put_NotificationMirroring: _Callable[[_enum.Windows.UI.Notifications.NotificationMirroring],  # value
                                         _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IToastNotification4(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[INotificationData]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[INotificationData],  # value
                        _type.HRESULT]
    get_Priority: _Callable[[_Pointer[_enum.Windows.UI.Notifications.ToastNotificationPriority]],  # value
                            _type.HRESULT]
    put_Priority: _Callable[[_enum.Windows.UI.Notifications.ToastNotificationPriority],  # value
                            _type.HRESULT]


class IToastNotification6(_inspectable.IInspectable):
    get_ExpiresOnReboot: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_ExpiresOnReboot: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]


class IToastNotificationActionTriggerDetail(_inspectable.IInspectable):
    get_Argument: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_UserInput: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                             _type.HRESULT]


class IToastNotificationFactory(_inspectable.IInspectable, factory=True):
    CreateToastNotification: _Callable[[_Windows_Data_Xml_Dom.IXmlDocument,  # content
                                        _Pointer[IToastNotification]],  # value
                                       _type.HRESULT]


class IToastNotificationHistory(_inspectable.IInspectable):
    RemoveGroup: _Callable[[_type.HSTRING],  # group
                           _type.HRESULT]
    RemoveGroupWithId: _Callable[[_type.HSTRING,  # group
                                  _type.HSTRING],  # applicationId
                                 _type.HRESULT]
    RemoveGroupedTagWithId: _Callable[[_type.HSTRING,  # tag
                                       _type.HSTRING,  # group
                                       _type.HSTRING],  # applicationId
                                      _type.HRESULT]
    RemoveGroupedTag: _Callable[[_type.HSTRING,  # tag
                                 _type.HSTRING],  # group
                                _type.HRESULT]
    Remove: _Callable[[_type.HSTRING],  # tag
                      _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    ClearWithId: _Callable[[_type.HSTRING],  # applicationId
                           _type.HRESULT]


class IToastNotificationHistory2(_inspectable.IInspectable):
    GetHistory: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IToastNotification]]],  # result
                          _type.HRESULT]
    GetHistoryWithId: _Callable[[_type.HSTRING,  # applicationId
                                 _Pointer[_Windows_Foundation_Collections.IVectorView[IToastNotification]]],  # result
                                _type.HRESULT]


class IToastNotificationHistoryChangedTriggerDetail(_inspectable.IInspectable):
    get_ChangeType: _Callable[[_Pointer[_enum.Windows.UI.Notifications.ToastHistoryChangedType]],  # value
                              _type.HRESULT]


class IToastNotificationHistoryChangedTriggerDetail2(_inspectable.IInspectable):
    get_CollectionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IToastNotificationManagerForUser(_inspectable.IInspectable):
    CreateToastNotifier: _Callable[[_Pointer[IToastNotifier]],  # result
                                   _type.HRESULT]
    CreateToastNotifierWithId: _Callable[[_type.HSTRING,  # applicationId
                                          _Pointer[IToastNotifier]],  # result
                                         _type.HRESULT]
    get_History: _Callable[[_Pointer[IToastNotificationHistory]],  # value
                           _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IToastNotificationManagerForUser2(_inspectable.IInspectable):
    GetToastNotifierForToastCollectionIdAsync: _Callable[[_type.HSTRING,  # collectionId
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[IToastNotifier]]],  # operation
                                                         _type.HRESULT]
    GetHistoryForToastCollectionIdAsync: _Callable[[_type.HSTRING,  # collectionId
                                                    _Pointer[_Windows_Foundation.IAsyncOperation[IToastNotificationHistory]]],  # operation
                                                   _type.HRESULT]
    GetToastCollectionManager: _Callable[[_Pointer[IToastCollectionManager]],  # result
                                         _type.HRESULT]
    GetToastCollectionManagerWithAppId: _Callable[[_type.HSTRING,  # appId
                                                   _Pointer[IToastCollectionManager]],  # result
                                                  _type.HRESULT]


class IToastNotificationManagerForUser3(_inspectable.IInspectable):
    get_NotificationMode: _Callable[[_Pointer[_enum.Windows.UI.Notifications.ToastNotificationMode]],  # value
                                    _type.HRESULT]
    add_NotificationModeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IToastNotificationManagerForUser, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_NotificationModeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IToastNotificationManagerStatics(_inspectable.IInspectable, factory=True):
    CreateToastNotifier: _Callable[[_Pointer[IToastNotifier]],  # result
                                   _type.HRESULT]
    CreateToastNotifierWithId: _Callable[[_type.HSTRING,  # applicationId
                                          _Pointer[IToastNotifier]],  # result
                                         _type.HRESULT]
    GetTemplateContent: _Callable[[_enum.Windows.UI.Notifications.ToastTemplateType,  # type
                                   _Pointer[_Windows_Data_Xml_Dom.IXmlDocument]],  # result
                                  _type.HRESULT]


class IToastNotificationManagerStatics2(_inspectable.IInspectable, factory=True):
    get_History: _Callable[[_Pointer[IToastNotificationHistory]],  # value
                           _type.HRESULT]


class IToastNotificationManagerStatics4(_inspectable.IInspectable, factory=True):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IToastNotificationManagerForUser]],  # result
                          _type.HRESULT]
    ConfigureNotificationMirroring: _Callable[[_enum.Windows.UI.Notifications.NotificationMirroring],  # value
                                              _type.HRESULT]


class IToastNotificationManagerStatics5(_inspectable.IInspectable, factory=True):
    GetDefault: _Callable[[_Pointer[IToastNotificationManagerForUser]],  # result
                          _type.HRESULT]


class IToastNotifier(_inspectable.IInspectable):
    Show: _Callable[[IToastNotification],  # notification
                    _type.HRESULT]
    Hide: _Callable[[IToastNotification],  # notification
                    _type.HRESULT]
    get_Setting: _Callable[[_Pointer[_enum.Windows.UI.Notifications.NotificationSetting]],  # value
                           _type.HRESULT]
    AddToSchedule: _Callable[[IScheduledToastNotification],  # scheduledToast
                             _type.HRESULT]
    RemoveFromSchedule: _Callable[[IScheduledToastNotification],  # scheduledToast
                                  _type.HRESULT]
    GetScheduledToastNotifications: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IScheduledToastNotification]]],  # result
                                              _type.HRESULT]


class IToastNotifier2(_inspectable.IInspectable):
    UpdateWithTagAndGroup: _Callable[[INotificationData,  # data
                                      _type.HSTRING,  # tag
                                      _type.HSTRING,  # group
                                      _Pointer[_enum.Windows.UI.Notifications.NotificationUpdateResult]],  # result
                                     _type.HRESULT]
    UpdateWithTag: _Callable[[INotificationData,  # data
                              _type.HSTRING,  # tag
                              _Pointer[_enum.Windows.UI.Notifications.NotificationUpdateResult]],  # result
                             _type.HRESULT]


class IToastNotifier3(_inspectable.IInspectable):
    add_ScheduledToastNotificationShowing: _Callable[[_Windows_Foundation.ITypedEventHandler[IToastNotifier, IScheduledToastNotificationShowingEventArgs],  # handler
                                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                                     _type.HRESULT]
    remove_ScheduledToastNotificationShowing: _Callable[[_struct.EventRegistrationToken],  # token
                                                        _type.HRESULT]


class IUserNotification(_inspectable.IInspectable):
    get_Notification: _Callable[[_Pointer[INotification]],  # value
                                _type.HRESULT]
    get_AppInfo: _Callable[[_Pointer[_Windows_ApplicationModel.IAppInfo]],  # value
                           _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_CreationTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                _type.HRESULT]


class IUserNotificationChangedEventArgs(_inspectable.IInspectable):
    get_ChangeKind: _Callable[[_Pointer[_enum.Windows.UI.Notifications.UserNotificationChangedKind]],  # value
                              _type.HRESULT]
    get_UserNotificationId: _Callable[[_Pointer[_type.UINT32]],  # value
                                      _type.HRESULT]
