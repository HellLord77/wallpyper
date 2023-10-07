from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Storage as _Windows_Storage
from ...ApplicationModel import Background as _Windows_ApplicationModel_Background
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Security import Credentials as _Windows_Security_Credentials
from ...Storage import Streams as _Windows_Storage_Streams
from ...UI import Notifications as _Windows_UI_Notifications
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IBackgroundDownloader(_inspectable.IInspectable):
    CreateDownload: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                               _Windows_Storage.IStorageFile,  # resultFile
                               _Pointer[IDownloadOperation]],  # operation
                              _type.HRESULT]
    CreateDownloadFromFile: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                       _Windows_Storage.IStorageFile,  # resultFile
                                       _Windows_Storage.IStorageFile,  # requestBodyFile
                                       _Pointer[IDownloadOperation]],  # operation
                                      _type.HRESULT]
    CreateDownloadAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                    _Windows_Storage.IStorageFile,  # resultFile
                                    _Windows_Storage_Streams.IInputStream,  # requestBodyStream
                                    _Pointer[_Windows_Foundation.IAsyncOperation[IDownloadOperation]]],  # operation
                                   _type.HRESULT]


class IBackgroundDownloader2(_inspectable.IInspectable):
    get_TransferGroup: _Callable[[_Pointer[IBackgroundTransferGroup]],  # value
                                 _type.HRESULT]
    put_TransferGroup: _Callable[[IBackgroundTransferGroup],  # value
                                 _type.HRESULT]
    get_SuccessToastNotification: _Callable[[_Pointer[_Windows_UI_Notifications.IToastNotification]],  # value
                                            _type.HRESULT]
    put_SuccessToastNotification: _Callable[[_Windows_UI_Notifications.IToastNotification],  # value
                                            _type.HRESULT]
    get_FailureToastNotification: _Callable[[_Pointer[_Windows_UI_Notifications.IToastNotification]],  # value
                                            _type.HRESULT]
    put_FailureToastNotification: _Callable[[_Windows_UI_Notifications.IToastNotification],  # value
                                            _type.HRESULT]
    get_SuccessTileNotification: _Callable[[_Pointer[_Windows_UI_Notifications.ITileNotification]],  # value
                                           _type.HRESULT]
    put_SuccessTileNotification: _Callable[[_Windows_UI_Notifications.ITileNotification],  # value
                                           _type.HRESULT]
    get_FailureTileNotification: _Callable[[_Pointer[_Windows_UI_Notifications.ITileNotification]],  # value
                                           _type.HRESULT]
    put_FailureTileNotification: _Callable[[_Windows_UI_Notifications.ITileNotification],  # value
                                           _type.HRESULT]


class IBackgroundDownloader3(_inspectable.IInspectable):
    get_CompletionGroup: _Callable[[_Pointer[IBackgroundTransferCompletionGroup]],  # value
                                   _type.HRESULT]


class IBackgroundDownloaderFactory(_inspectable.IInspectable, factory=True):
    CreateWithCompletionGroup: _Callable[[IBackgroundTransferCompletionGroup,  # completionGroup
                                          _Pointer[IBackgroundDownloader]],  # backgroundDownloader
                                         _type.HRESULT]


class IBackgroundDownloaderStaticMethods(_inspectable.IInspectable, factory=True):
    GetCurrentDownloadsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDownloadOperation]]]],  # operation
                                        _type.HRESULT]
    GetCurrentDownloadsForGroupAsync: _Callable[[_type.HSTRING,  # group
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDownloadOperation]]]],  # operation
                                                _type.HRESULT]


class IBackgroundDownloaderStaticMethods2(_inspectable.IInspectable, factory=True):
    GetCurrentDownloadsForTransferGroupAsync: _Callable[[IBackgroundTransferGroup,  # group
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IDownloadOperation]]]],  # operation
                                                        _type.HRESULT]


class IBackgroundDownloaderUserConsent(_inspectable.IInspectable, factory=True):
    RequestUnconstrainedDownloadsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IDownloadOperation],  # operations
                                                   _Pointer[_Windows_Foundation.IAsyncOperation[IUnconstrainedTransferRequestResult]]],  # operation
                                                  _type.HRESULT]


class IBackgroundTransferBase(_inspectable.IInspectable):
    SetRequestHeader: _Callable[[_type.HSTRING,  # headerName
                                 _type.HSTRING],  # headerValue
                                _type.HRESULT]
    get_ServerCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # credential
                                    _type.HRESULT]
    put_ServerCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # credential
                                    _type.HRESULT]
    get_ProxyCredential: _Callable[[_Pointer[_Windows_Security_Credentials.IPasswordCredential]],  # credential
                                   _type.HRESULT]
    put_ProxyCredential: _Callable[[_Windows_Security_Credentials.IPasswordCredential],  # credential
                                   _type.HRESULT]
    get_Method: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Method: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    Group: _Callable[[_type.HSTRING],  # value
                     _type.HRESULT]
    get_CostPolicy: _Callable[[_Pointer[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy]],  # value
                              _type.HRESULT]
    put_CostPolicy: _Callable[[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy],  # value
                              _type.HRESULT]


class IBackgroundTransferCompletionGroup(_inspectable.IInspectable):
    get_Trigger: _Callable[[_Pointer[_Windows_ApplicationModel_Background.IBackgroundTrigger]],  # value
                           _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    Enable: _Callable[[],
                      _type.HRESULT]


class IBackgroundTransferCompletionGroupTriggerDetails(_inspectable.IInspectable):
    get_Downloads: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IDownloadOperation]]],  # value
                             _type.HRESULT]
    get_Uploads: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IUploadOperation]]],  # value
                           _type.HRESULT]


class IBackgroundTransferContentPart(_inspectable.IInspectable):
    SetHeader: _Callable[[_type.HSTRING,  # headerName
                          _type.HSTRING],  # headerValue
                         _type.HRESULT]
    SetText: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    SetFile: _Callable[[_Windows_Storage.IStorageFile],  # value
                       _type.HRESULT]


class IBackgroundTransferContentPartFactory(_inspectable.IInspectable, factory=True):
    CreateWithName: _Callable[[_type.HSTRING,  # name
                               _Pointer[IBackgroundTransferContentPart]],  # value
                              _type.HRESULT]
    CreateWithNameAndFileName: _Callable[[_type.HSTRING,  # name
                                          _type.HSTRING,  # fileName
                                          _Pointer[IBackgroundTransferContentPart]],  # value
                                         _type.HRESULT]


class IBackgroundTransferErrorStaticMethods(_inspectable.IInspectable, factory=True):
    GetStatus: _Callable[[_type.INT32,  # hresult
                          _Pointer[_enum.Windows.Web.WebErrorStatus]],  # status
                         _type.HRESULT]


class IBackgroundTransferGroup(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_TransferBehavior: _Callable[[_Pointer[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior]],  # value
                                    _type.HRESULT]
    put_TransferBehavior: _Callable[[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferBehavior],  # value
                                    _type.HRESULT]


class IBackgroundTransferGroupStatics(_inspectable.IInspectable, factory=True):
    CreateGroup: _Callable[[_type.HSTRING,  # name
                            _Pointer[IBackgroundTransferGroup]],  # value
                           _type.HRESULT]


class IBackgroundTransferOperation(_inspectable.IInspectable):
    get_Guid: _Callable[[_Pointer[_struct.GUID]],  # value
                        _type.HRESULT]
    get_RequestedUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                _type.HRESULT]
    get_Method: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    Group: _Callable[[_Pointer[_type.HSTRING]],  # value
                     _type.HRESULT]
    get_CostPolicy: _Callable[[_Pointer[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy]],  # value
                              _type.HRESULT]
    put_CostPolicy: _Callable[[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferCostPolicy],  # value
                              _type.HRESULT]
    GetResultStreamAt: _Callable[[_type.UINT64,  # position
                                  _Pointer[_Windows_Storage_Streams.IInputStream]],  # value
                                 _type.HRESULT]
    GetResponseInformation: _Callable[[_Pointer[IResponseInformation]],  # value
                                      _type.HRESULT]


class IBackgroundTransferOperationPriority(_inspectable.IInspectable):
    get_Priority: _Callable[[_Pointer[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority]],  # value
                            _type.HRESULT]
    put_Priority: _Callable[[_enum.Windows.Networking.BackgroundTransfer.BackgroundTransferPriority],  # value
                            _type.HRESULT]


class IBackgroundTransferRangesDownloadedEventArgs(_inspectable.IInspectable):
    get_WasDownloadRestarted: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_AddedRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]]],  # value
                               _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class IBackgroundUploader(_inspectable.IInspectable):
    CreateUpload: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                             _Windows_Storage.IStorageFile,  # sourceFile
                             _Pointer[IUploadOperation]],  # operation
                            _type.HRESULT]
    CreateUploadFromStreamAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                            _Windows_Storage_Streams.IInputStream,  # sourceStream
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IUploadOperation]]],  # operation
                                           _type.HRESULT]
    CreateUploadWithFormDataAndAutoBoundaryAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                                             _Windows_Foundation_Collections.IIterable[IBackgroundTransferContentPart],  # parts
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[IUploadOperation]]],  # operation
                                                            _type.HRESULT]
    CreateUploadWithSubTypeAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                             _Windows_Foundation_Collections.IIterable[IBackgroundTransferContentPart],  # parts
                                             _type.HSTRING,  # subType
                                             _Pointer[_Windows_Foundation.IAsyncOperation[IUploadOperation]]],  # operation
                                            _type.HRESULT]
    CreateUploadWithSubTypeAndBoundaryAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                                        _Windows_Foundation_Collections.IIterable[IBackgroundTransferContentPart],  # parts
                                                        _type.HSTRING,  # subType
                                                        _type.HSTRING,  # boundary
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IUploadOperation]]],  # operation
                                                       _type.HRESULT]


class IBackgroundUploader2(_inspectable.IInspectable):
    get_TransferGroup: _Callable[[_Pointer[IBackgroundTransferGroup]],  # value
                                 _type.HRESULT]
    put_TransferGroup: _Callable[[IBackgroundTransferGroup],  # value
                                 _type.HRESULT]
    get_SuccessToastNotification: _Callable[[_Pointer[_Windows_UI_Notifications.IToastNotification]],  # value
                                            _type.HRESULT]
    put_SuccessToastNotification: _Callable[[_Windows_UI_Notifications.IToastNotification],  # value
                                            _type.HRESULT]
    get_FailureToastNotification: _Callable[[_Pointer[_Windows_UI_Notifications.IToastNotification]],  # value
                                            _type.HRESULT]
    put_FailureToastNotification: _Callable[[_Windows_UI_Notifications.IToastNotification],  # value
                                            _type.HRESULT]
    get_SuccessTileNotification: _Callable[[_Pointer[_Windows_UI_Notifications.ITileNotification]],  # value
                                           _type.HRESULT]
    put_SuccessTileNotification: _Callable[[_Windows_UI_Notifications.ITileNotification],  # value
                                           _type.HRESULT]
    get_FailureTileNotification: _Callable[[_Pointer[_Windows_UI_Notifications.ITileNotification]],  # value
                                           _type.HRESULT]
    put_FailureTileNotification: _Callable[[_Windows_UI_Notifications.ITileNotification],  # value
                                           _type.HRESULT]


class IBackgroundUploader3(_inspectable.IInspectable):
    get_CompletionGroup: _Callable[[_Pointer[IBackgroundTransferCompletionGroup]],  # value
                                   _type.HRESULT]


class IBackgroundUploaderFactory(_inspectable.IInspectable, factory=True):
    CreateWithCompletionGroup: _Callable[[IBackgroundTransferCompletionGroup,  # completionGroup
                                          _Pointer[IBackgroundUploader]],  # backgroundUploader
                                         _type.HRESULT]


class IBackgroundUploaderStaticMethods(_inspectable.IInspectable, factory=True):
    GetCurrentUploadsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUploadOperation]]]],  # operation
                                      _type.HRESULT]
    GetCurrentUploadsForGroupAsync: _Callable[[_type.HSTRING,  # group
                                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUploadOperation]]]],  # operation
                                              _type.HRESULT]


class IBackgroundUploaderStaticMethods2(_inspectable.IInspectable, factory=True):
    GetCurrentUploadsForTransferGroupAsync: _Callable[[IBackgroundTransferGroup,  # group
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IUploadOperation]]]],  # operation
                                                      _type.HRESULT]


class IBackgroundUploaderUserConsent(_inspectable.IInspectable, factory=True):
    RequestUnconstrainedUploadsAsync: _Callable[[_Windows_Foundation_Collections.IIterable[IUploadOperation],  # operations
                                                 _Pointer[_Windows_Foundation.IAsyncOperation[IUnconstrainedTransferRequestResult]]],  # operation
                                                _type.HRESULT]


class IContentPrefetcher(_inspectable.IInspectable, factory=True):
    get_ContentUris: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Foundation.IUriRuntimeClass]]],  # value
                               _type.HRESULT]
    put_IndirectContentUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                      _type.HRESULT]
    get_IndirectContentUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                                      _type.HRESULT]


class IContentPrefetcherTime(_inspectable.IInspectable, factory=True):
    get_LastSuccessfulPrefetchTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                              _type.HRESULT]


class IDownloadOperation(_inspectable.IInspectable):
    get_ResultFile: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                              _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_struct.Windows.Networking.BackgroundTransfer.BackgroundDownloadProgress]],  # value
                            _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDownloadOperation, IDownloadOperation]]],  # operation
                          _type.HRESULT]
    AttachAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IDownloadOperation, IDownloadOperation]]],  # operation
                           _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]


class IDownloadOperation2(_inspectable.IInspectable):
    get_TransferGroup: _Callable[[_Pointer[IBackgroundTransferGroup]],  # value
                                 _type.HRESULT]


class IDownloadOperation3(_inspectable.IInspectable):
    get_IsRandomAccessRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsRandomAccessRequired: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    GetResultRandomAccessStreamReference: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # stream
                                                    _type.HRESULT]
    GetDownloadedRanges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Windows.Networking.BackgroundTransfer.BackgroundTransferFileRange]]],  # value
                                   _type.HRESULT]
    add_RangesDownloaded: _Callable[[_Windows_Foundation.ITypedEventHandler[IDownloadOperation, IBackgroundTransferRangesDownloadedEventArgs],  # eventHandler
                                     _Pointer[_struct.EventRegistrationToken]],  # eventCookie
                                    _type.HRESULT]
    remove_RangesDownloaded: _Callable[[_struct.EventRegistrationToken],  # eventCookie
                                       _type.HRESULT]
    put_RequestedUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                                _type.HRESULT]
    get_RecoverableWebErrorStatuses: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_enum.Windows.Web.WebErrorStatus]]],  # value
                                               _type.HRESULT]
    get_CurrentWebErrorStatus: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.Web.WebErrorStatus]]],  # value
                                         _type.HRESULT]


class IDownloadOperation4(_inspectable.IInspectable):
    MakeCurrentInTransferGroup: _Callable[[],
                                          _type.HRESULT]


class IDownloadOperation5(_inspectable.IInspectable):
    SetRequestHeader: _Callable[[_type.HSTRING,  # headerName
                                 _type.HSTRING],  # headerValue
                                _type.HRESULT]
    RemoveRequestHeader: _Callable[[_type.HSTRING],  # headerName
                                   _type.HRESULT]


class IResponseInformation(_inspectable.IInspectable):
    get_IsResumable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_ActualUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                             _type.HRESULT]
    get_StatusCode: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_Headers: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                           _type.HRESULT]


class IUnconstrainedTransferRequestResult(_inspectable.IInspectable):
    IsUnconstrained: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]


class IUploadOperation(_inspectable.IInspectable):
    get_SourceFile: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                              _type.HRESULT]
    get_Progress: _Callable[[_Pointer[_struct.Windows.Networking.BackgroundTransfer.BackgroundUploadProgress]],  # value
                            _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IUploadOperation, IUploadOperation]]],  # operation
                          _type.HRESULT]
    AttachAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IUploadOperation, IUploadOperation]]],  # operation
                           _type.HRESULT]


class IUploadOperation2(_inspectable.IInspectable):
    get_TransferGroup: _Callable[[_Pointer[IBackgroundTransferGroup]],  # value
                                 _type.HRESULT]


class IUploadOperation3(_inspectable.IInspectable):
    MakeCurrentInTransferGroup: _Callable[[],
                                          _type.HRESULT]


class IUploadOperation4(_inspectable.IInspectable):
    SetRequestHeader: _Callable[[_type.HSTRING,  # headerName
                                 _type.HSTRING],  # headerValue
                                _type.HRESULT]
    RemoveRequestHeader: _Callable[[_type.HSTRING],  # headerName
                                   _type.HRESULT]
