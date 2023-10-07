from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IDataProviderHandler:
    Invoke: _Callable[[IDataProviderRequest],  # request
                      _type.HRESULT]


class IDataProviderHandler(_IDataProviderHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IDataProviderHandler_impl(_IDataProviderHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IShareProviderHandler:
    Invoke: _Callable[[IShareProviderOperation],  # operation
                      _type.HRESULT]


class IShareProviderHandler(_IShareProviderHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IShareProviderHandler_impl(_IShareProviderHandler, _Unknwnbase.IUnknown_impl):
    pass


class IClipboardContentOptions(_inspectable.IInspectable):
    get_IsRoamable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsRoamable: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_IsAllowedInHistory: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsAllowedInHistory: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_RoamingFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                  _type.HRESULT]
    get_HistoryFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                  _type.HRESULT]


class IClipboardHistoryChangedEventArgs(_inspectable.IInspectable):
    pass


class IClipboardHistoryItem(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                             _type.HRESULT]
    get_Content: _Callable[[_Pointer[IDataPackageView]],  # value
                           _type.HRESULT]


class IClipboardHistoryItemsResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.ClipboardHistoryItemsResultStatus]],  # value
                          _type.HRESULT]
    get_Items: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IClipboardHistoryItem]]],  # value
                         _type.HRESULT]


class IClipboardStatics(_inspectable.IInspectable, factory=True):
    GetContent: _Callable[[_Pointer[IDataPackageView]],  # result
                          _type.HRESULT]
    SetContent: _Callable[[IDataPackage],  # content
                          _type.HRESULT]
    Flush: _Callable[[],
                     _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    add_ContentChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContentChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IClipboardStatics2(_inspectable.IInspectable, factory=True):
    GetHistoryItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IClipboardHistoryItemsResult]]],  # operation
                                    _type.HRESULT]
    ClearHistory: _Callable[[_Pointer[_type.boolean]],  # result
                            _type.HRESULT]
    DeleteItemFromHistory: _Callable[[IClipboardHistoryItem,  # item
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    SetHistoryItemAsContent: _Callable[[IClipboardHistoryItem,  # item
                                        _Pointer[_enum.Windows.ApplicationModel.DataTransfer.SetHistoryItemAsContentStatus]],  # result
                                       _type.HRESULT]
    IsHistoryEnabled: _Callable[[_Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    IsRoamingEnabled: _Callable[[_Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetContentWithOptions: _Callable[[IDataPackage,  # content
                                      IClipboardContentOptions,  # options
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    add_HistoryChanged: _Callable[[_Windows_Foundation.IEventHandler[IClipboardHistoryChangedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_HistoryChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_RoamingEnabledChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_RoamingEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_HistoryEnabledChanged: _Callable[[_Windows_Foundation.IEventHandler[_inspectable.IInspectable],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_HistoryEnabledChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class IDataPackage(_inspectable.IInspectable):
    GetView: _Callable[[_Pointer[IDataPackageView]],  # result
                       _type.HRESULT]
    get_Properties: _Callable[[_Pointer[IDataPackagePropertySet]],  # value
                              _type.HRESULT]
    get_RequestedOperation: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                      _type.HRESULT]
    put_RequestedOperation: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation],  # value
                                      _type.HRESULT]
    add_OperationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDataPackage, IOperationCompletedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_OperationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_Destroyed: _Callable[[_Windows_Foundation.ITypedEventHandler[IDataPackage, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Destroyed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    SetData: _Callable[[_type.HSTRING,  # formatId
                        _inspectable.IInspectable],  # value
                       _type.HRESULT]
    SetDataProvider: _Callable[[_type.HSTRING,  # formatId
                                IDataProviderHandler],  # delayRenderer
                               _type.HRESULT]
    SetText: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    SetUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                      _type.HRESULT]
    SetHtmlFormat: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_ResourceMap: _Callable[[_Pointer[_Windows_Foundation_Collections.IMap[_type.HSTRING, _Windows_Storage_Streams.IRandomAccessStreamReference]]],  # value
                               _type.HRESULT]
    SetRtf: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    SetBitmap: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                         _type.HRESULT]
    SetStorageItemsReadOnly: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageItem]],  # value
                                       _type.HRESULT]
    SetStorageItems: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_Storage.IStorageItem],  # value
                                _type.boolean],  # readOnly
                               _type.HRESULT]


class IDataPackage2(_inspectable.IInspectable):
    SetApplicationLink: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                  _type.HRESULT]
    SetWebLink: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                          _type.HRESULT]


class IDataPackage3(_inspectable.IInspectable):
    add_ShareCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IDataPackage, IShareCompletedEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ShareCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]


class IDataPackage4(_inspectable.IInspectable):
    add_ShareCanceled: _Callable[[_Windows_Foundation.ITypedEventHandler[IDataPackage, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ShareCanceled: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class IDataPackagePropertySet(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_Description: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    put_Thumbnail: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    get_FileTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_ApplicationName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    put_ApplicationName: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    get_ApplicationListingUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                         _type.HRESULT]
    put_ApplicationListingUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                         _type.HRESULT]


class IDataPackagePropertySet2(_inspectable.IInspectable):
    get_ContentSourceWebLink: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                        _type.HRESULT]
    put_ContentSourceWebLink: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                        _type.HRESULT]
    get_ContentSourceApplicationLink: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                                _type.HRESULT]
    put_ContentSourceApplicationLink: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                                _type.HRESULT]
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_PackageFamilyName: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_Square30x30Logo: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                   _type.HRESULT]
    put_Square30x30Logo: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                                   _type.HRESULT]
    get_LogoBackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                       _type.HRESULT]
    put_LogoBackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                       _type.HRESULT]


class IDataPackagePropertySet3(_inspectable.IInspectable):
    get_EnterpriseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_EnterpriseId: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]


class IDataPackagePropertySet4(_inspectable.IInspectable):
    get_ContentSourceUserActivityJson: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]
    put_ContentSourceUserActivityJson: _Callable[[_type.HSTRING],  # value
                                                 _type.HRESULT]


class IDataPackagePropertySetView(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    get_FileTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                             _type.HRESULT]
    get_ApplicationName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
    get_ApplicationListingUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                         _type.HRESULT]


class IDataPackagePropertySetView2(_inspectable.IInspectable):
    get_PackageFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    get_ContentSourceWebLink: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                        _type.HRESULT]
    get_ContentSourceApplicationLink: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                                _type.HRESULT]
    get_Square30x30Logo: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                                   _type.HRESULT]
    get_LogoBackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                       _type.HRESULT]


class IDataPackagePropertySetView3(_inspectable.IInspectable):
    get_EnterpriseId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IDataPackagePropertySetView4(_inspectable.IInspectable):
    get_ContentSourceUserActivityJson: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]


class IDataPackagePropertySetView5(_inspectable.IInspectable):
    get_IsFromRoamingClipboard: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class IDataPackageView(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[IDataPackagePropertySetView]],  # value
                              _type.HRESULT]
    get_RequestedOperation: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                      _type.HRESULT]
    ReportOperationCompleted: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation],  # value
                                        _type.HRESULT]
    get_AvailableFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # formatIds
                                    _type.HRESULT]
    Contains: _Callable[[_type.HSTRING,  # formatId
                         _Pointer[_type.boolean]],  # value
                        _type.HRESULT]
    GetDataAsync: _Callable[[_type.HSTRING,  # formatId
                             _Pointer[_Windows_Foundation.IAsyncOperation[_inspectable.IInspectable]]],  # operation
                            _type.HRESULT]
    GetTextAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                            _type.HRESULT]
    GetCustomTextAsync: _Callable[[_type.HSTRING,  # formatId
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                  _type.HRESULT]
    GetUriAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation.IUriRuntimeClass]]],  # operation
                           _type.HRESULT]
    GetHtmlFormatAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                  _type.HRESULT]
    GetResourceMapAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _Windows_Storage_Streams.IRandomAccessStreamReference]]]],  # operation
                                   _type.HRESULT]
    GetRtfAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                           _type.HRESULT]
    GetBitmapAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStreamReference]]],  # operation
                              _type.HRESULT]
    GetStorageItemsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[_Windows_Storage.IStorageItem]]]],  # operation
                                    _type.HRESULT]


class IDataPackageView2(_inspectable.IInspectable):
    GetApplicationLinkAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation.IUriRuntimeClass]]],  # operation
                                       _type.HRESULT]
    GetWebLinkAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation.IUriRuntimeClass]]],  # operation
                               _type.HRESULT]


class IDataPackageView3(_inspectable.IInspectable):
    RequestAccessAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # operation
                                  _type.HRESULT]
    RequestAccessWithEnterpriseIdAsync: _Callable[[_type.HSTRING,  # enterpriseId
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]]],  # operation
                                                  _type.HRESULT]
    UnlockAndAssumeEnterpriseIdentity: _Callable[[_Pointer[_enum.Windows.Security.EnterpriseData.ProtectionPolicyEvaluationResult]],  # result
                                                 _type.HRESULT]


class IDataPackageView4(_inspectable.IInspectable):
    SetAcceptedFormatId: _Callable[[_type.HSTRING],  # formatId
                                   _type.HRESULT]


class IDataProviderDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IDataProviderRequest(_inspectable.IInspectable):
    get_FormatId: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IDataProviderDeferral]],  # value
                           _type.HRESULT]
    SetData: _Callable[[_inspectable.IInspectable],  # value
                       _type.HRESULT]


class IDataRequest(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[IDataPackage]],  # value
                        _type.HRESULT]
    put_Data: _Callable[[IDataPackage],  # value
                        _type.HRESULT]
    get_Deadline: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                            _type.HRESULT]
    FailWithDisplayText: _Callable[[_type.HSTRING],  # value
                                   _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[IDataRequestDeferral]],  # result
                           _type.HRESULT]


class IDataRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class IDataRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[IDataRequest]],  # value
                           _type.HRESULT]


class IDataTransferManager(_inspectable.IInspectable):
    add_DataRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IDataTransferManager, IDataRequestedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_DataRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_TargetApplicationChosen: _Callable[[_Windows_Foundation.ITypedEventHandler[IDataTransferManager, ITargetApplicationChosenEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_TargetApplicationChosen: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IDataTransferManager2(_inspectable.IInspectable):
    add_ShareProvidersRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IDataTransferManager, IShareProvidersRequestedEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_ShareProvidersRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]


class IDataTransferManagerStatics(_inspectable.IInspectable, factory=True):
    ShowShareUI: _Callable[[],
                           _type.HRESULT]
    GetForCurrentView: _Callable[[_Pointer[IDataTransferManager]],  # result
                                 _type.HRESULT]


class IDataTransferManagerStatics2(_inspectable.IInspectable, factory=True):
    IsSupported: _Callable[[_Pointer[_type.boolean]],  # result
                           _type.HRESULT]


class IDataTransferManagerStatics3(_inspectable.IInspectable, factory=True):
    ShowShareUIWithOptions: _Callable[[IShareUIOptions],  # options
                                      _type.HRESULT]


class IHtmlFormatHelperStatics(_inspectable.IInspectable, factory=True):
    GetStaticFragment: _Callable[[_type.HSTRING,  # htmlFormat
                                  _Pointer[_type.HSTRING]],  # htmlFragment
                                 _type.HRESULT]
    CreateHtmlFormat: _Callable[[_type.HSTRING,  # htmlFragment
                                 _Pointer[_type.HSTRING]],  # htmlFormat
                                _type.HRESULT]


class IOperationCompletedEventArgs(_inspectable.IInspectable):
    get_Operation: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                             _type.HRESULT]


class IOperationCompletedEventArgs2(_inspectable.IInspectable):
    get_AcceptedFormatId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]


class IShareCompletedEventArgs(_inspectable.IInspectable):
    get_ShareTarget: _Callable[[_Pointer[IShareTargetInfo]],  # value
                               _type.HRESULT]


class IShareProvider(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_DisplayIcon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                               _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                       _type.HRESULT]
    put_Tag: _Callable[[_inspectable.IInspectable],  # value
                       _type.HRESULT]


class IShareProviderFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_type.HSTRING,  # title
                       _Windows_Storage_Streams.IRandomAccessStreamReference,  # displayIcon
                       _struct.Windows.UI.Color,  # backgroundColor
                       IShareProviderHandler,  # handler
                       _Pointer[IShareProvider]],  # result
                      _type.HRESULT]


class IShareProviderOperation(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[IDataPackageView]],  # value
                        _type.HRESULT]
    get_Provider: _Callable[[_Pointer[IShareProvider]],  # value
                            _type.HRESULT]
    ReportCompleted: _Callable[[],
                               _type.HRESULT]


class IShareProvidersRequestedEventArgs(_inspectable.IInspectable):
    get_Providers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IShareProvider]]],  # value
                             _type.HRESULT]
    get_Data: _Callable[[_Pointer[IDataPackageView]],  # value
                        _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IShareTargetInfo(_inspectable.IInspectable):
    get_AppUserModelId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_ShareProvider: _Callable[[_Pointer[IShareProvider]],  # value
                                 _type.HRESULT]


class IShareUIOptions(_inspectable.IInspectable):
    get_Theme: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.ShareUITheme]],  # value
                         _type.HRESULT]
    put_Theme: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.ShareUITheme],  # value
                         _type.HRESULT]
    get_SelectionRect: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]]],  # value
                                 _type.HRESULT]
    put_SelectionRect: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]


class ISharedStorageAccessManagerStatics(_inspectable.IInspectable, factory=True):
    AddFile: _Callable[[_Windows_Storage.IStorageFile,  # file
                        _Pointer[_type.HSTRING]],  # outToken
                       _type.HRESULT]
    RedeemTokenForFileAsync: _Callable[[_type.HSTRING,  # token
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage.IStorageFile]]],  # operation
                                       _type.HRESULT]
    RemoveFile: _Callable[[_type.HSTRING],  # token
                          _type.HRESULT]


class IStandardDataFormatsStatics(_inspectable.IInspectable, factory=True):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                   _type.HRESULT]
    get_Html: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Rtf: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Bitmap: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_StorageItems: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]


class IStandardDataFormatsStatics2(_inspectable.IInspectable, factory=True):
    get_WebLink: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_ApplicationLink: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]


class IStandardDataFormatsStatics3(_inspectable.IInspectable, factory=True):
    get_UserActivityJsonArray: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]


class ITargetApplicationChosenEventArgs(_inspectable.IInspectable):
    get_ApplicationName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                   _type.HRESULT]
