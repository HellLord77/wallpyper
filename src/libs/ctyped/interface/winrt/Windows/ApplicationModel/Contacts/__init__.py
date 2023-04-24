from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import System as _Windows_System
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IAggregateContactManager(_inspectable.IInspectable):
    FindRawContactsAsync: _Callable[[IContact,  # contact
                                     _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContact]]]],  # value
                                    _type.HRESULT]
    TryLinkContactsAsync: _Callable[[IContact,  # primaryContact
                                     IContact,  # secondaryContact
                                     _Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # contact
                                    _type.HRESULT]
    UnlinkRawContactAsync: _Callable[[IContact,  # contact
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                     _type.HRESULT]
    TrySetPreferredSourceForPictureAsync: _Callable[[IContact,  # aggregateContact
                                                     IContact,  # rawContact
                                                     _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # value
                                                    _type.HRESULT]


class IAggregateContactManager2(_inspectable.IInspectable):
    SetRemoteIdentificationInformationAsync: _Callable[[_type.HSTRING,  # contactListId
                                                        _type.HSTRING,  # remoteSourceId
                                                        _type.HSTRING,  # accountId
                                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                                       _type.HRESULT]


class IContact(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    put_Thumbnail: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    get_Fields: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactField]]],  # value
                          _type.HRESULT]


class IContact2(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_Notes: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Notes: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Phones: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactPhone]]],  # value
                          _type.HRESULT]
    get_Emails: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactEmail]]],  # value
                          _type.HRESULT]
    get_Addresses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactAddress]]],  # value
                             _type.HRESULT]
    get_ConnectedServiceAccounts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactConnectedServiceAccount]]],  # value
                                            _type.HRESULT]
    get_ImportantDates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactDate]]],  # value
                                  _type.HRESULT]
    get_DataSuppliers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                 _type.HRESULT]
    get_JobInfo: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactJobInfo]]],  # value
                           _type.HRESULT]
    get_SignificantOthers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactSignificantOther]]],  # value
                                     _type.HRESULT]
    get_Websites: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IContactWebsite]]],  # value
                            _type.HRESULT]
    get_ProviderProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                      _type.HRESULT]


class IContact3(_inspectable.IInspectable):
    get_ContactListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_DisplayPictureUserUpdateTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                                _type.HRESULT]
    put_DisplayPictureUserUpdateTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                                _type.HRESULT]
    get_IsMe: _Callable[[_Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    get_AggregateId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_RingToneToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_RingToneToken: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_IsDisplayPictureManuallySet: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_LargeDisplayPicture: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                       _type.HRESULT]
    get_SmallDisplayPicture: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                       _type.HRESULT]
    get_SourceDisplayPicture: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                        _type.HRESULT]
    put_SourceDisplayPicture: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                                        _type.HRESULT]
    get_TextToneToken: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_TextToneToken: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_IsAggregate: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_FullName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_DisplayNameOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_DisplayNameOverride: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_Nickname: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Nickname: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_SortName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]


class IContactAddress(_inspectable.IInspectable):
    get_StreetAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_StreetAddress: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_Locality: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Locality: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Region: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Region: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Country: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Country: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_PostalCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_PostalCode: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactAddressKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactAddressKind],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactAnnotation(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_AnnotationListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ContactId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_ContactId: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_RemoteId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RemoteId: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_SupportedOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactAnnotationOperations]],  # value
                                       _type.HRESULT]
    put_SupportedOperations: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactAnnotationOperations],  # value
                                       _type.HRESULT]
    get_IsDisabled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_ProviderProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                      _type.HRESULT]


class IContactAnnotation2(_inspectable.IInspectable):
    get_ContactListId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_ContactListId: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]


class IContactAnnotationList(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_ProviderPackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]
    get_UserDataAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                           _type.HRESULT]
    TrySaveAnnotationAsync: _Callable[[IContactAnnotation,  # annotation
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # ppResult
                                      _type.HRESULT]
    GetAnnotationAsync: _Callable[[_type.HSTRING,  # annotationId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[IContactAnnotation]]],  # annotation
                                  _type.HRESULT]
    FindAnnotationsByRemoteIdAsync: _Callable[[_type.HSTRING,  # remoteId
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactAnnotation]]]],  # annotations
                                              _type.HRESULT]
    FindAnnotationsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactAnnotation]]]],  # annotations
                                    _type.HRESULT]
    DeleteAnnotationAsync: _Callable[[IContactAnnotation,  # annotation
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                     _type.HRESULT]


class IContactAnnotationStore(_inspectable.IInspectable):
    FindContactIdsByEmailAsync: _Callable[[_type.HSTRING,  # emailAddress
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # contactIds
                                          _type.HRESULT]
    FindContactIdsByPhoneNumberAsync: _Callable[[_type.HSTRING,  # phoneNumber
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # contactIds
                                                _type.HRESULT]
    FindAnnotationsForContactAsync: _Callable[[IContact,  # contact
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactAnnotation]]]],  # annotations
                                              _type.HRESULT]
    DisableAnnotationAsync: _Callable[[IContactAnnotation,  # annotation
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                      _type.HRESULT]
    CreateAnnotationListAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContactAnnotationList]]],  # value
                                         _type.HRESULT]
    CreateAnnotationListInAccountAsync: _Callable[[_type.HSTRING,  # userDataAccountId
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IContactAnnotationList]]],  # value
                                                  _type.HRESULT]
    GetAnnotationListAsync: _Callable[[_type.HSTRING,  # annotationListId
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IContactAnnotationList]]],  # value
                                      _type.HRESULT]
    FindAnnotationListsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactAnnotationList]]]],  # lists
                                        _type.HRESULT]


class IContactAnnotationStore2(_inspectable.IInspectable):
    FindAnnotationsForContactListAsync: _Callable[[_type.HSTRING,  # contactListId
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactAnnotation]]]],  # annotations
                                                  _type.HRESULT]


class IContactBatch(_inspectable.IInspectable):
    get_Contacts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IContact]]],  # value
                            _type.HRESULT]
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactBatchStatus]],  # value
                          _type.HRESULT]


class IContactCardDelayedDataLoader(_inspectable.IInspectable):
    SetData: _Callable[[IContact],  # contact
                       _type.HRESULT]


class IContactCardOptions(_inspectable.IInspectable):
    get_HeaderKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactCardHeaderKind]],  # value
                              _type.HRESULT]
    put_HeaderKind: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactCardHeaderKind],  # value
                              _type.HRESULT]
    get_InitialTabKind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactCardTabKind]],  # value
                                  _type.HRESULT]
    put_InitialTabKind: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactCardTabKind],  # value
                                  _type.HRESULT]


class IContactCardOptions2(_inspectable.IInspectable):
    get_ServerSearchContactListIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                              _type.HRESULT]


class IContactChange(_inspectable.IInspectable):
    get_ChangeType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactChangeType]],  # value
                              _type.HRESULT]
    get_Contact: _Callable[[_Pointer[IContact]],  # value
                           _type.HRESULT]


class IContactChangeReader(_inspectable.IInspectable):
    AcceptChanges: _Callable[[],
                             _type.HRESULT]
    AcceptChangesThrough: _Callable[[IContactChange],  # lastChangeToAccept
                                    _type.HRESULT]
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactChange]]]],  # value
                              _type.HRESULT]


class IContactChangeTracker(_inspectable.IInspectable):
    Enable: _Callable[[],
                      _type.HRESULT]
    GetChangeReader: _Callable[[_Pointer[IContactChangeReader]],  # value
                               _type.HRESULT]
    Reset: _Callable[[],
                     _type.HRESULT]


class IContactChangeTracker2(_inspectable.IInspectable):
    get_IsTracking: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IContactChangedDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IContactChangedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[IContactChangedDeferral]],  # value
                           _type.HRESULT]


class IContactConnectedServiceAccount(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_ServiceName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ServiceName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactDate(_inspectable.IInspectable):
    get_Day: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                       _type.HRESULT]
    put_Day: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Month: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.UINT32]]],  # value
                         _type.HRESULT]
    put_Month: _Callable[[_Windows_Foundation.IReference[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Year: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                        _type.HRESULT]
    put_Year: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                        _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactDateKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactDateKind],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactEmail(_inspectable.IInspectable):
    get_Address: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Address: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactEmailKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactEmailKind],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactField(_inspectable.IInspectable):
    get_Type: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactFieldType]],  # value
                        _type.HRESULT]
    get_Category: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactFieldCategory]],  # value
                            _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IContactFieldFactory(_inspectable.IInspectable):
    CreateField_Default: _Callable[[_type.HSTRING,  # value
                                    _enum.Windows.ApplicationModel.Contacts.ContactFieldType,  # type
                                    _Pointer[IContactField]],  # field
                                   _type.HRESULT]
    CreateField_Category: _Callable[[_type.HSTRING,  # value
                                     _enum.Windows.ApplicationModel.Contacts.ContactFieldType,  # type
                                     _enum.Windows.ApplicationModel.Contacts.ContactFieldCategory,  # category
                                     _Pointer[IContactField]],  # field
                                    _type.HRESULT]
    CreateField_Custom: _Callable[[_type.HSTRING,  # name
                                   _type.HSTRING,  # value
                                   _enum.Windows.ApplicationModel.Contacts.ContactFieldType,  # type
                                   _enum.Windows.ApplicationModel.Contacts.ContactFieldCategory,  # category
                                   _Pointer[IContactField]],  # field
                                  _type.HRESULT]

    _factory = True


class IContactGroup(_inspectable.IInspectable):
    pass


class IContactInformation(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    GetThumbnailAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamWithContentType]]],  # operation
                                 _type.HRESULT]
    get_Emails: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IContactField]]],  # value
                          _type.HRESULT]
    get_PhoneNumbers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IContactField]]],  # value
                                _type.HRESULT]
    get_Locations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IContactLocationField]]],  # value
                             _type.HRESULT]
    get_InstantMessages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IContactInstantMessageField]]],  # value
                                   _type.HRESULT]
    get_CustomFields: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IContactField]]],  # value
                                _type.HRESULT]
    QueryCustomFields: _Callable[[_type.HSTRING,  # customName
                                  _Pointer[_Windows_Foundation_Collections.IVectorView[IContactField]]],  # value
                                 _type.HRESULT]


class IContactInstantMessageField(_inspectable.IInspectable):
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Service: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_DisplayText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_LaunchUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]


class IContactInstantMessageFieldFactory(_inspectable.IInspectable):
    CreateInstantMessage_Default: _Callable[[_type.HSTRING,  # userName
                                             _Pointer[IContactInstantMessageField]],  # field
                                            _type.HRESULT]
    CreateInstantMessage_Category: _Callable[[_type.HSTRING,  # userName
                                              _enum.Windows.ApplicationModel.Contacts.ContactFieldCategory,  # category
                                              _Pointer[IContactInstantMessageField]],  # field
                                             _type.HRESULT]
    CreateInstantMessage_All: _Callable[[_type.HSTRING,  # userName
                                         _enum.Windows.ApplicationModel.Contacts.ContactFieldCategory,  # category
                                         _type.HSTRING,  # service
                                         _type.HSTRING,  # displayText
                                         _Windows_Foundation.IUriRuntimeClass,  # verb
                                         _Pointer[IContactInstantMessageField]],  # field
                                        _type.HRESULT]

    _factory = True


class IContactJobInfo(_inspectable.IInspectable):
    get_CompanyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_CompanyName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_CompanyYomiName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_CompanyYomiName: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_Department: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_Department: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Manager: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Manager: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_Office: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Office: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_CompanyAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_CompanyAddress: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactLaunchActionVerbsStatics(_inspectable.IInspectable):
    get_Call: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Map: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Post: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_VideoCall: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]

    _factory = True


class IContactList(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_DisplayName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_SourceDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_IsHidden: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsHidden: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_OtherAppReadAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactListOtherAppReadAccess]],  # value
                                      _type.HRESULT]
    put_OtherAppReadAccess: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactListOtherAppReadAccess],  # value
                                      _type.HRESULT]
    get_OtherAppWriteAccess: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactListOtherAppWriteAccess]],  # value
                                       _type.HRESULT]
    put_OtherAppWriteAccess: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactListOtherAppWriteAccess],  # value
                                       _type.HRESULT]
    get_ChangeTracker: _Callable[[_Pointer[IContactChangeTracker]],  # value
                                 _type.HRESULT]
    get_SyncManager: _Callable[[_Pointer[IContactListSyncManager]],  # value
                               _type.HRESULT]
    get_SupportsServerSearch: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_UserDataAccountId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    add_ContactChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactList, IContactChangedEventArgs],  # value
                                   _Pointer[_struct.EventRegistrationToken]],  # returnValue
                                  _type.HRESULT]
    remove_ContactChanged: _Callable[[_struct.EventRegistrationToken],  # value
                                     _type.HRESULT]
    SaveAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # returnValue
                         _type.HRESULT]
    DeleteAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # returnValue
                           _type.HRESULT]
    GetContactFromRemoteIdAsync: _Callable[[_type.HSTRING,  # remoteId
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # contact
                                           _type.HRESULT]
    GetMeContactAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # meContact
                                 _type.HRESULT]
    GetContactReader: _Callable[[_Pointer[IContactReader]],  # value
                                _type.HRESULT]
    GetContactReaderWithOptions: _Callable[[IContactQueryOptions,  # options
                                            _Pointer[IContactReader]],  # value
                                           _type.HRESULT]
    SaveContactAsync: _Callable[[IContact,  # contact
                                 _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                _type.HRESULT]
    DeleteContactAsync: _Callable[[IContact,  # contact
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                  _type.HRESULT]
    GetContactAsync: _Callable[[_type.HSTRING,  # contactId
                                _Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # contacts
                               _type.HRESULT]


class IContactList2(_inspectable.IInspectable):
    RegisterSyncManagerAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # result
                                        _type.HRESULT]
    put_SupportsServerSearch: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_SyncConstraints: _Callable[[_Pointer[IContactListSyncConstraints]],  # value
                                   _type.HRESULT]


class IContactList3(_inspectable.IInspectable):
    get_LimitedWriteOperations: _Callable[[_Pointer[IContactListLimitedWriteOperations]],  # value
                                          _type.HRESULT]
    GetChangeTracker: _Callable[[_type.HSTRING,  # identity
                                 _Pointer[IContactChangeTracker]],  # result
                                _type.HRESULT]


class IContactListLimitedWriteOperations(_inspectable.IInspectable):
    TryCreateOrUpdateContactAsync: _Callable[[IContact,  # contact
                                              _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                             _type.HRESULT]
    TryDeleteContactAsync: _Callable[[_type.HSTRING,  # contactId
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]


class IContactListSyncConstraints(_inspectable.IInspectable):
    get_CanSyncDescriptions: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_CanSyncDescriptions: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_MaxHomePhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                       _type.HRESULT]
    put_MaxHomePhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                       _type.HRESULT]
    get_MaxMobilePhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                         _type.HRESULT]
    put_MaxMobilePhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                         _type.HRESULT]
    get_MaxWorkPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                       _type.HRESULT]
    put_MaxWorkPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                       _type.HRESULT]
    get_MaxOtherPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                        _type.HRESULT]
    put_MaxOtherPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                        _type.HRESULT]
    get_MaxPagerPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                        _type.HRESULT]
    put_MaxPagerPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                        _type.HRESULT]
    get_MaxBusinessFaxPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                              _type.HRESULT]
    put_MaxBusinessFaxPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                              _type.HRESULT]
    get_MaxHomeFaxPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    put_MaxHomeFaxPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                          _type.HRESULT]
    get_MaxCompanyPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    put_MaxCompanyPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                          _type.HRESULT]
    get_MaxAssistantPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                            _type.HRESULT]
    put_MaxAssistantPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                            _type.HRESULT]
    get_MaxRadioPhoneNumbers: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                        _type.HRESULT]
    put_MaxRadioPhoneNumbers: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                        _type.HRESULT]
    get_MaxPersonalEmailAddresses: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                             _type.HRESULT]
    put_MaxPersonalEmailAddresses: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                             _type.HRESULT]
    get_MaxWorkEmailAddresses: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                         _type.HRESULT]
    put_MaxWorkEmailAddresses: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                         _type.HRESULT]
    get_MaxOtherEmailAddresses: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    put_MaxOtherEmailAddresses: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                          _type.HRESULT]
    get_MaxHomeAddresses: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    put_MaxHomeAddresses: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                    _type.HRESULT]
    get_MaxWorkAddresses: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    put_MaxWorkAddresses: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                    _type.HRESULT]
    get_MaxOtherAddresses: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                     _type.HRESULT]
    put_MaxOtherAddresses: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                     _type.HRESULT]
    get_MaxBirthdayDates: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                    _type.HRESULT]
    put_MaxBirthdayDates: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                    _type.HRESULT]
    get_MaxAnniversaryDates: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                       _type.HRESULT]
    put_MaxAnniversaryDates: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                       _type.HRESULT]
    get_MaxOtherDates: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                 _type.HRESULT]
    put_MaxOtherDates: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                 _type.HRESULT]
    get_MaxOtherRelationships: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                         _type.HRESULT]
    put_MaxOtherRelationships: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                         _type.HRESULT]
    get_MaxSpouseRelationships: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    put_MaxSpouseRelationships: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                          _type.HRESULT]
    get_MaxPartnerRelationships: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                           _type.HRESULT]
    put_MaxPartnerRelationships: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                           _type.HRESULT]
    get_MaxSiblingRelationships: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                           _type.HRESULT]
    put_MaxSiblingRelationships: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                           _type.HRESULT]
    get_MaxParentRelationships: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                          _type.HRESULT]
    put_MaxParentRelationships: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                          _type.HRESULT]
    get_MaxChildRelationships: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                                         _type.HRESULT]
    put_MaxChildRelationships: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                                         _type.HRESULT]
    get_MaxJobInfo: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                              _type.HRESULT]
    put_MaxJobInfo: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                              _type.HRESULT]
    get_MaxWebsites: _Callable[[_Pointer[_Windows_Foundation.IReference[_type.INT32]]],  # value
                               _type.HRESULT]
    put_MaxWebsites: _Callable[[_Windows_Foundation.IReference[_type.INT32]],  # value
                               _type.HRESULT]


class IContactListSyncManager(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactListSyncStatus]],  # value
                          _type.HRESULT]
    get_LastSuccessfulSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                          _type.HRESULT]
    get_LastAttemptedSyncTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                         _type.HRESULT]
    SyncAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                         _type.HRESULT]
    add_SyncStatusChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactListSyncManager, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_SyncStatusChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]


class IContactListSyncManager2(_inspectable.IInspectable):
    put_Status: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactListSyncStatus],  # value
                          _type.HRESULT]
    put_LastSuccessfulSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                          _type.HRESULT]
    put_LastAttemptedSyncTime: _Callable[[_struct.Windows.Foundation.DateTime],  # value
                                         _type.HRESULT]


class IContactLocationField(_inspectable.IInspectable):
    get_UnstructuredAddress: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_Street: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_City: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Region: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Country: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_PostalCode: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]


class IContactLocationFieldFactory(_inspectable.IInspectable):
    CreateLocation_Default: _Callable[[_type.HSTRING,  # unstructuredAddress
                                       _Pointer[IContactLocationField]],  # field
                                      _type.HRESULT]
    CreateLocation_Category: _Callable[[_type.HSTRING,  # unstructuredAddress
                                        _enum.Windows.ApplicationModel.Contacts.ContactFieldCategory,  # category
                                        _Pointer[IContactLocationField]],  # field
                                       _type.HRESULT]
    CreateLocation_All: _Callable[[_type.HSTRING,  # unstructuredAddress
                                   _enum.Windows.ApplicationModel.Contacts.ContactFieldCategory,  # category
                                   _type.HSTRING,  # street
                                   _type.HSTRING,  # city
                                   _type.HSTRING,  # region
                                   _type.HSTRING,  # country
                                   _type.HSTRING,  # postalCode
                                   _Pointer[IContactLocationField]],  # field
                                  _type.HRESULT]

    _factory = True


class IContactManagerForUser(_inspectable.IInspectable):
    ConvertContactToVCardAsync: _Callable[[IContact,  # contact
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # result
                                          _type.HRESULT]
    ConvertContactToVCardAsyncWithMaxBytes: _Callable[[IContact,  # contact
                                                       _type.UINT32,  # maxBytes
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # result
                                                      _type.HRESULT]
    ConvertVCardToContactAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # vCard
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # result
                                          _type.HRESULT]
    RequestStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactStoreAccessType,  # accessType
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IContactStore]]],  # result
                                 _type.HRESULT]
    RequestAnnotationStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactAnnotationStoreAccessType,  # accessType
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IContactAnnotationStore]]],  # result
                                           _type.HRESULT]
    get_SystemDisplayNameOrder: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder]],  # value
                                          _type.HRESULT]
    put_SystemDisplayNameOrder: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder],  # value
                                          _type.HRESULT]
    get_SystemSortOrder: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder]],  # value
                                   _type.HRESULT]
    put_SystemSortOrder: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder],  # value
                                   _type.HRESULT]
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IContactManagerForUser2(_inspectable.IInspectable):
    ShowFullContactCard: _Callable[[IContact,  # contact
                                    IFullContactCardOptions],  # fullContactCardOptions
                                   _type.HRESULT]


class IContactManagerStatics(_inspectable.IInspectable):
    ShowContactCard: _Callable[[IContact,  # contact
                                _struct.Windows.Foundation.Rect],  # selection
                               _type.HRESULT]
    ShowContactCardWithPlacement: _Callable[[IContact,  # contact
                                             _struct.Windows.Foundation.Rect,  # selection
                                             _enum.Windows.UI.Popups.Placement],  # preferredPlacement
                                            _type.HRESULT]
    ShowDelayLoadedContactCard: _Callable[[IContact,  # contact
                                           _struct.Windows.Foundation.Rect,  # selection
                                           _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                           _Pointer[IContactCardDelayedDataLoader]],  # dataLoader
                                          _type.HRESULT]

    _factory = True


class IContactManagerStatics2(_inspectable.IInspectable):
    RequestStoreAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContactStore]]],  # store
                                 _type.HRESULT]

    _factory = True


class IContactManagerStatics3(_inspectable.IInspectable):
    ConvertContactToVCardAsync: _Callable[[IContact,  # contact
                                           _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # vCard
                                          _type.HRESULT]
    ConvertContactToVCardAsyncWithMaxBytes: _Callable[[IContact,  # contact
                                                       _type.UINT32,  # maxBytes
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # vCard
                                                      _type.HRESULT]
    ConvertVCardToContactAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # vCard
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # contact
                                          _type.HRESULT]
    RequestStoreAsyncWithAccessType: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactStoreAccessType,  # accessType
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IContactStore]]],  # store
                                               _type.HRESULT]
    RequestAnnotationStoreAsync: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactAnnotationStoreAccessType,  # accessType
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IContactAnnotationStore]]],  # store
                                           _type.HRESULT]
    IsShowContactCardSupported: _Callable[[_Pointer[_type.boolean]],  # result
                                          _type.HRESULT]
    ShowContactCardWithOptions: _Callable[[IContact,  # contact
                                           _struct.Windows.Foundation.Rect,  # selection
                                           _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                           IContactCardOptions],  # contactCardOptions
                                          _type.HRESULT]
    IsShowDelayLoadedContactCardSupported: _Callable[[_Pointer[_type.boolean]],  # result
                                                     _type.HRESULT]
    ShowDelayLoadedContactCardWithOptions: _Callable[[IContact,  # contact
                                                      _struct.Windows.Foundation.Rect,  # selection
                                                      _enum.Windows.UI.Popups.Placement,  # preferredPlacement
                                                      IContactCardOptions,  # contactCardOptions
                                                      _Pointer[IContactCardDelayedDataLoader]],  # dataLoader
                                                     _type.HRESULT]
    ShowFullContactCard: _Callable[[IContact,  # contact
                                    IFullContactCardOptions],  # fullContactCardOptions
                                   _type.HRESULT]
    get_SystemDisplayNameOrder: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder]],  # value
                                          _type.HRESULT]
    put_SystemDisplayNameOrder: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder],  # value
                                          _type.HRESULT]
    get_SystemSortOrder: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder]],  # value
                                   _type.HRESULT]
    put_SystemSortOrder: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactNameOrder],  # value
                                   _type.HRESULT]

    _factory = True


class IContactManagerStatics4(_inspectable.IInspectable):
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IContactManagerForUser]],  # result
                          _type.HRESULT]

    _factory = True


class IContactManagerStatics5(_inspectable.IInspectable):
    IsShowFullContactCardSupportedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                                   _type.HRESULT]
    get_IncludeMiddleNameInSystemDisplayAndSort: _Callable[[_Pointer[_type.boolean]],  # value
                                                           _type.HRESULT]
    put_IncludeMiddleNameInSystemDisplayAndSort: _Callable[[_type.boolean],  # value
                                                           _type.HRESULT]

    _factory = True


class IContactMatchReason(_inspectable.IInspectable):
    get_Field: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactMatchReasonKind]],  # value
                         _type.HRESULT]
    get_Segments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Data.Text.TextSegment]]],  # value
                            _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IContactName(_inspectable.IInspectable):
    get_FirstName: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_FirstName: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_LastName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_LastName: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_MiddleName: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_MiddleName: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_YomiGivenName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_YomiGivenName: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_YomiFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_YomiFamilyName: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_HonorificNameSuffix: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_HonorificNameSuffix: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_HonorificNamePrefix: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    put_HonorificNamePrefix: _Callable[[_type.HSTRING],  # value
                                       _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_YomiDisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IContactPanel(_inspectable.IInspectable):
    ClosePanel: _Callable[[],
                          _type.HRESULT]
    get_HeaderColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.UI.Color]]],  # value
                               _type.HRESULT]
    put_HeaderColor: _Callable[[_Windows_Foundation.IReference[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    add_LaunchFullAppRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactPanel, IContactPanelLaunchFullAppRequestedEventArgs],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_LaunchFullAppRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_Closing: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactPanel, IContactPanelClosingEventArgs],  # handler
                            _Pointer[_struct.EventRegistrationToken]],  # token
                           _type.HRESULT]
    remove_Closing: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]


class IContactPanelClosingEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # deferral
                           _type.HRESULT]


class IContactPanelLaunchFullAppRequestedEventArgs(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IContactPhone(_inspectable.IInspectable):
    get_Number: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Number: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactPhoneKind]],  # value
                        _type.HRESULT]
    put_Kind: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactPhoneKind],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactPicker(_inspectable.IInspectable):
    get_CommitButtonText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    put_CommitButtonText: _Callable[[_type.HSTRING],  # value
                                    _type.HRESULT]
    get_SelectionMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactSelectionMode]],  # value
                                 _type.HRESULT]
    put_SelectionMode: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactSelectionMode],  # value
                                 _type.HRESULT]
    get_DesiredFields: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                 _type.HRESULT]
    PickSingleContactAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContactInformation]]],  # result
                                      _type.HRESULT]
    PickMultipleContactsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactInformation]]]],  # result
                                         _type.HRESULT]


class IContactPicker2(_inspectable.IInspectable):
    get_DesiredFieldsWithContactFieldType: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.ApplicationModel.Contacts.ContactFieldType]]],  # value
                                                     _type.HRESULT]
    PickContactAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # result
                                _type.HRESULT]
    PickContactsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVector[IContact]]]],  # result
                                 _type.HRESULT]


class IContactPicker3(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # value
                        _type.HRESULT]


class IContactPickerStatics(_inspectable.IInspectable):
    CreateForUser: _Callable[[_Windows_System.IUser,  # user
                              _Pointer[IContactPicker]],  # result
                             _type.HRESULT]
    IsSupportedAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                _type.HRESULT]

    _factory = True


class IContactQueryOptions(_inspectable.IInspectable):
    get_TextSearch: _Callable[[_Pointer[IContactQueryTextSearch]],  # value
                              _type.HRESULT]
    get_ContactListIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    get_IncludeContactsFromHiddenLists: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_IncludeContactsFromHiddenLists: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    get_DesiredFields: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactQueryDesiredFields]],  # value
                                 _type.HRESULT]
    put_DesiredFields: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactQueryDesiredFields],  # value
                                 _type.HRESULT]
    get_DesiredOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactAnnotationOperations]],  # value
                                     _type.HRESULT]
    put_DesiredOperations: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactAnnotationOperations],  # value
                                     _type.HRESULT]
    get_AnnotationListIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]


class IContactQueryOptionsFactory(_inspectable.IInspectable):
    CreateWithText: _Callable[[_type.HSTRING,  # text
                               _Pointer[IContactQueryOptions]],  # result
                              _type.HRESULT]
    CreateWithTextAndFields: _Callable[[_type.HSTRING,  # text
                                        _enum.Windows.ApplicationModel.Contacts.ContactQuerySearchFields,  # fields
                                        _Pointer[IContactQueryOptions]],  # result
                                       _type.HRESULT]

    _factory = True


class IContactQueryTextSearch(_inspectable.IInspectable):
    get_Fields: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactQuerySearchFields]],  # value
                          _type.HRESULT]
    put_Fields: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactQuerySearchFields],  # value
                          _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_SearchScope: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactQuerySearchScope]],  # value
                               _type.HRESULT]
    put_SearchScope: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactQuerySearchScope],  # value
                               _type.HRESULT]


class IContactReader(_inspectable.IInspectable):
    ReadBatchAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContactBatch]]],  # value
                              _type.HRESULT]
    GetMatchingPropertiesWithMatchReason: _Callable[[IContact,  # contact
                                                     _Pointer[_Windows_Foundation_Collections.IVectorView[IContactMatchReason]]],  # ppRetVal
                                                    _type.HRESULT]


class IContactSignificantOther(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactSignificantOther2(_inspectable.IInspectable):
    get_Relationship: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Contacts.ContactRelationship]],  # value
                                _type.HRESULT]
    put_Relationship: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactRelationship],  # value
                                _type.HRESULT]


class IContactStore(_inspectable.IInspectable):
    FindContactsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContact]]]],  # contacts
                                 _type.HRESULT]
    FindContactsWithSearchTextAsync: _Callable[[_type.HSTRING,  # searchText
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContact]]]],  # contacts
                                               _type.HRESULT]
    GetContactAsync: _Callable[[_type.HSTRING,  # contactId
                                _Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # contacts
                               _type.HRESULT]


class IContactStore2(_inspectable.IInspectable):
    get_ChangeTracker: _Callable[[_Pointer[IContactChangeTracker]],  # value
                                 _type.HRESULT]
    add_ContactChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IContactStore, IContactChangedEventArgs],  # value
                                   _Pointer[_struct.EventRegistrationToken]],  # returnValue
                                  _type.HRESULT]
    remove_ContactChanged: _Callable[[_struct.EventRegistrationToken],  # value
                                     _type.HRESULT]
    get_AggregateContactManager: _Callable[[_Pointer[IAggregateContactManager]],  # value
                                           _type.HRESULT]
    FindContactListsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IContactList]]]],  # value
                                     _type.HRESULT]
    GetContactListAsync: _Callable[[_type.HSTRING,  # contactListId
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IContactList]]],  # value
                                   _type.HRESULT]
    CreateContactListAsync: _Callable[[_type.HSTRING,  # displayName
                                       _Pointer[_Windows_Foundation.IAsyncOperation[IContactList]]],  # value
                                      _type.HRESULT]
    GetMeContactAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IContact]]],  # meContact
                                 _type.HRESULT]
    GetContactReader: _Callable[[_Pointer[IContactReader]],  # value
                                _type.HRESULT]
    GetContactReaderWithOptions: _Callable[[IContactQueryOptions,  # options
                                            _Pointer[IContactReader]],  # value
                                           _type.HRESULT]
    CreateContactListInAccountAsync: _Callable[[_type.HSTRING,  # displayName
                                                _type.HSTRING,  # userDataAccountId
                                                _Pointer[_Windows_Foundation.IAsyncOperation[IContactList]]],  # value
                                               _type.HRESULT]


class IContactStore3(_inspectable.IInspectable):
    GetChangeTracker: _Callable[[_type.HSTRING,  # identity
                                 _Pointer[IContactChangeTracker]],  # result
                                _type.HRESULT]


class IContactStoreNotificationTriggerDetails(_inspectable.IInspectable):
    pass


class IContactWebsite(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                       _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class IContactWebsite2(_inspectable.IInspectable):
    get_RawValue: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_RawValue: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class IFullContactCardOptions(_inspectable.IInspectable):
    get_DesiredRemainingView: _Callable[[_Pointer[_enum.Windows.UI.ViewManagement.ViewSizePreference]],  # value
                                        _type.HRESULT]
    put_DesiredRemainingView: _Callable[[_enum.Windows.UI.ViewManagement.ViewSizePreference],  # value
                                        _type.HRESULT]


class IKnownContactFieldStatics(_inspectable.IInspectable):
    Email: _Callable[[_Pointer[_type.HSTRING]],  # value
                     _type.HRESULT]
    PhoneNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    Location: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    InstantMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    ConvertNameToType: _Callable[[_type.HSTRING,  # name
                                  _Pointer[_enum.Windows.ApplicationModel.Contacts.ContactFieldType]],  # type
                                 _type.HRESULT]
    ConvertTypeToName: _Callable[[_enum.Windows.ApplicationModel.Contacts.ContactFieldType,  # type
                                  _Pointer[_type.HSTRING]],  # name
                                 _type.HRESULT]

    _factory = True


class IPinnedContactIdsQueryResult(_inspectable.IInspectable):
    get_ContactIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                              _type.HRESULT]


class IPinnedContactManager(_inspectable.IInspectable):
    get_User: _Callable[[_Pointer[_Windows_System.IUser]],  # user
                        _type.HRESULT]
    IsPinSurfaceSupported: _Callable[[_enum.Windows.ApplicationModel.Contacts.PinnedContactSurface,  # surface
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    IsContactPinned: _Callable[[IContact,  # contact
                                _enum.Windows.ApplicationModel.Contacts.PinnedContactSurface,  # surface
                                _Pointer[_type.boolean]],  # result
                               _type.HRESULT]
    RequestPinContactAsync: _Callable[[IContact,  # contact
                                       _enum.Windows.ApplicationModel.Contacts.PinnedContactSurface,  # surface
                                       _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                      _type.HRESULT]
    RequestPinContactsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IContact],  # contacts
                                        _enum.Windows.ApplicationModel.Contacts.PinnedContactSurface,  # surface
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                       _type.HRESULT]
    RequestUnpinContactAsync: _Callable[[IContact,  # contact
                                         _enum.Windows.ApplicationModel.Contacts.PinnedContactSurface,  # surface
                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                        _type.HRESULT]
    SignalContactActivity: _Callable[[IContact],  # contact
                                     _type.HRESULT]
    GetPinnedContactIdsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IPinnedContactIdsQueryResult]]],  # operation
                                        _type.HRESULT]


class IPinnedContactManagerStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IPinnedContactManager]],  # result
                          _type.HRESULT]
    GetForUser: _Callable[[_Windows_System.IUser,  # user
                           _Pointer[IPinnedContactManager]],  # result
                          _type.HRESULT]
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]

    _factory = True
