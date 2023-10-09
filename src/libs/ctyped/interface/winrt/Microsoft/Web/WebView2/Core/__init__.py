from __future__ import annotations as _

from typing import Callable as _Callable

from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.ApplicationModel.DataTransfer.DragDrop import Core as _Windows_ApplicationModel_DataTransfer_DragDrop_Core
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from .....Windows.Security.Cryptography import Certificates as _Windows_Security_Cryptography_Certificates
from .....Windows.Storage import Streams as _Windows_Storage_Streams
from .....Windows.UI import Core as _Windows_UI_Core
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class CoreWebView2Certificate_Manual(_inspectable.IInspectable):
    ToCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # result
                             _type.HRESULT]


class CoreWebView2ClientCertificate_Manual(_inspectable.IInspectable):
    ToCertificate: _Callable[[_Pointer[_Windows_Security_Cryptography_Certificates.ICertificate]],  # result
                             _type.HRESULT]


class CoreWebView2Profile_Manual(_inspectable.IInspectable):
    ClearBrowsingDataAsync: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2BrowsingDataKinds,  # dataKinds
                                       _struct.Windows.Foundation.DateTime,  # startTime
                                       _struct.Windows.Foundation.DateTime,  # endTime
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                      _type.HRESULT]
    ClearBrowsingDataAsync2: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                       _type.HRESULT]


class CoreWebView2Profile_Manual2(_inspectable.IInspectable):
    GetNonDefaultPermissionSettingsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ICoreWebView2PermissionSetting]]]],  # operation
                                                    _type.HRESULT]


class ICoreWebView2(_inspectable.IInspectable):
    get_Settings: _Callable[[_Pointer[ICoreWebView2Settings]],  # value
                            _type.HRESULT]
    get_Source: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_BrowserProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_CanGoBack: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanGoForward: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_DocumentTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ContainsFullScreenElement: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    add_NavigationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2NavigationStartingEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContentLoading: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2ContentLoadingEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_SourceChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2SourceChangedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SourceChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_HistoryChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_HistoryChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_NavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2NavigationCompletedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_FrameNavigationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2NavigationStartingEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_FrameNavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_FrameNavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2NavigationCompletedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_FrameNavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_ScriptDialogOpening: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2ScriptDialogOpeningEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ScriptDialogOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_PermissionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2PermissionRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PermissionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ProcessFailed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2ProcessFailedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ProcessFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_WebMessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2WebMessageReceivedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_WebMessageReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_NewWindowRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2NewWindowRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NewWindowRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_DocumentTitleChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_DocumentTitleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_ContainsFullScreenElementChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                                    _type.HRESULT]
    remove_ContainsFullScreenElementChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                       _type.HRESULT]
    add_WebResourceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2WebResourceRequestedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_WebResourceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_WindowCloseRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_WindowCloseRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    Navigate: _Callable[[_type.HSTRING],  # uri
                        _type.HRESULT]
    NavigateToString: _Callable[[_type.HSTRING],  # htmlContent
                                _type.HRESULT]
    AddScriptToExecuteOnDocumentCreatedAsync: _Callable[[_type.HSTRING,  # javaScript
                                                         _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                                        _type.HRESULT]
    RemoveScriptToExecuteOnDocumentCreated: _Callable[[_type.HSTRING],  # id
                                                      _type.HRESULT]
    ExecuteScriptAsync: _Callable[[_type.HSTRING,  # javaScript
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                  _type.HRESULT]
    CapturePreviewAsync: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2CapturePreviewImageFormat,  # imageFormat
                                    _Windows_Storage_Streams.IRandomAccessStream,  # imageStream
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                   _type.HRESULT]
    Reload: _Callable[[],
                      _type.HRESULT]
    PostWebMessageAsJson: _Callable[[_type.HSTRING],  # webMessageAsJson
                                    _type.HRESULT]
    PostWebMessageAsString: _Callable[[_type.HSTRING],  # webMessageAsString
                                      _type.HRESULT]
    CallDevToolsProtocolMethodAsync: _Callable[[_type.HSTRING,  # methodName
                                                _type.HSTRING,  # parametersAsJson
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                               _type.HRESULT]
    GoBack: _Callable[[],
                      _type.HRESULT]
    GoForward: _Callable[[],
                         _type.HRESULT]
    GetDevToolsProtocolEventReceiver: _Callable[[_type.HSTRING,  # eventName
                                                 _Pointer[ICoreWebView2DevToolsProtocolEventReceiver]],  # result
                                                _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    AddHostObjectToScript: _Callable[[_type.HSTRING,  # name
                                      _inspectable.IInspectable],  # rawObject
                                     _type.HRESULT]
    RemoveHostObjectFromScript: _Callable[[_type.HSTRING],  # name
                                          _type.HRESULT]
    OpenDevToolsWindow: _Callable[[],
                                  _type.HRESULT]
    AddWebResourceRequestedFilter: _Callable[[_type.HSTRING,  # uri
                                              _enum.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext],  # ResourceContext
                                             _type.HRESULT]
    RemoveWebResourceRequestedFilter: _Callable[[_type.HSTRING,  # uri
                                                 _enum.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext],  # ResourceContext
                                                _type.HRESULT]


class ICoreWebView2AcceleratorKeyPressedEventArgs(_inspectable.IInspectable):
    get_KeyEventKind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2KeyEventKind]],  # value
                                _type.HRESULT]
    get_VirtualKey: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    get_KeyEventLParam: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    get_PhysicalKeyStatus: _Callable[[_Pointer[_struct.Microsoft.Web.WebView2.Core.CoreWebView2PhysicalKeyStatus]],  # value
                                     _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICoreWebView2BasicAuthenticationRequestedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Challenge: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Response: _Callable[[_Pointer[ICoreWebView2BasicAuthenticationResponse]],  # value
                            _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2BasicAuthenticationResponse(_inspectable.IInspectable):
    get_UserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_UserName: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_Password: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Password: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]


class ICoreWebView2BrowserProcessExitedEventArgs(_inspectable.IInspectable):
    get_BrowserProcessExitKind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2BrowserProcessExitKind]],  # value
                                          _type.HRESULT]
    get_BrowserProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]


class ICoreWebView2Certificate(_inspectable.IInspectable):
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Issuer: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_ValidFrom: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    get_ValidTo: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_DerEncodedSerialNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PemEncodedIssuerCertificateChain: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                                    _type.HRESULT]
    ToPemEncoding: _Callable[[_Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]


class ICoreWebView2ClientCertificate(_inspectable.IInspectable):
    get_Subject: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_Issuer: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_ValidFrom: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    get_ValidTo: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    get_DerEncodedSerialNumber: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_PemEncodedIssuerCertificateChain: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                                    _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificateKind]],  # value
                        _type.HRESULT]
    ToPemEncoding: _Callable[[_Pointer[_type.HSTRING]],  # result
                             _type.HRESULT]


class ICoreWebView2ClientCertificateRequestedEventArgs(_inspectable.IInspectable):
    get_Host: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Port: _Callable[[_Pointer[_type.INT32]],  # value
                        _type.HRESULT]
    get_IsProxy: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_AllowedCertificateAuthorities: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                                 _type.HRESULT]
    get_MutuallyTrustedCertificates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreWebView2ClientCertificate]]],  # value
                                               _type.HRESULT]
    get_SelectedCertificate: _Callable[[_Pointer[ICoreWebView2ClientCertificate]],  # value
                                       _type.HRESULT]
    put_SelectedCertificate: _Callable[[ICoreWebView2ClientCertificate],  # value
                                       _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2CompositionController(_inspectable.IInspectable):
    get_RootVisualTarget: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                    _type.HRESULT]
    put_RootVisualTarget: _Callable[[_inspectable.IInspectable],  # value
                                    _type.HRESULT]
    add_CursorChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2CompositionController, _inspectable.IInspectable],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_CursorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    SendMouseInput: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2MouseEventKind,  # eventKind
                               _enum.Microsoft.Web.WebView2.Core.CoreWebView2MouseEventVirtualKeys,  # virtualKeys
                               _type.UINT32,  # mouseData
                               _struct.Windows.Foundation.Point],  # point
                              _type.HRESULT]
    SendPointerInput: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PointerEventKind,  # eventKind
                                 ICoreWebView2PointerInfo],  # pointerInfo
                                _type.HRESULT]
    get_Cursor: _Callable[[_Pointer[_Windows_UI_Core.ICoreCursor]],  # value
                          _type.HRESULT]
    DragEnter: _Callable[[_Windows_ApplicationModel_DataTransfer_DragDrop_Core.ICoreDragInfo,  # dragInfo
                          _Windows_ApplicationModel_DataTransfer_DragDrop_Core.ICoreDragUIOverride,  # dragUIOverride
                          _Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # result
                         _type.HRESULT]
    DragOver: _Callable[[_Windows_ApplicationModel_DataTransfer_DragDrop_Core.ICoreDragInfo,  # dragInfo
                         _Windows_ApplicationModel_DataTransfer_DragDrop_Core.ICoreDragUIOverride,  # dragUIOverride
                         _Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # result
                        _type.HRESULT]
    Drop: _Callable[[_Windows_ApplicationModel_DataTransfer_DragDrop_Core.ICoreDragInfo,  # dragInfo
                     _Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # result
                    _type.HRESULT]


class ICoreWebView2CompositionController2(_inspectable.IInspectable):
    pass


class ICoreWebView2CompositionController3(_inspectable.IInspectable):
    DragLeave: _Callable[[],
                         _type.HRESULT]


class ICoreWebView2CompositionControllerStatics(_inspectable.IInspectable):
    pass


class ICoreWebView2CompositionControllerStatics2_Manual(_inspectable.IInspectable):
    pass


class ICoreWebView2ContentLoadingEventArgs(_inspectable.IInspectable):
    get_IsErrorPage: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]


class ICoreWebView2ContextMenuItem(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Label: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    get_CommandId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_ShortcutKeyDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                          _type.HRESULT]
    get_Icon: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                        _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItemKind]],  # value
                        _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_IsChecked: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsChecked: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICoreWebView2ContextMenuItem]]],  # value
                            _type.HRESULT]
    add_CustomItemSelected: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2ContextMenuItem, _inspectable.IInspectable],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CustomItemSelected: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class ICoreWebView2ContextMenuRequestedEventArgs(_inspectable.IInspectable):
    get_MenuItems: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ICoreWebView2ContextMenuItem]]],  # value
                             _type.HRESULT]
    get_ContextMenuTarget: _Callable[[_Pointer[ICoreWebView2ContextMenuTarget]],  # value
                                     _type.HRESULT]
    get_Location: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_SelectedCommandId: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    put_SelectedCommandId: _Callable[[_type.INT32],  # value
                                     _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2ContextMenuTarget(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuTargetKind]],  # value
                        _type.HRESULT]
    get_IsEditable: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_IsRequestedForMainFrame: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    get_PageUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_FrameUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_HasLinkUri: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_LinkUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_HasLinkText: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_LinkText: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_HasSourceUri: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_SourceUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_HasSelection: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_SelectionText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class ICoreWebView2Controller(_inspectable.IInspectable):
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsVisible: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                          _type.HRESULT]
    put_Bounds: _Callable[[_struct.Windows.Foundation.Rect],  # value
                          _type.HRESULT]
    get_ZoomFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_ZoomFactor: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_ParentWindow: _Callable[[_Pointer[ICoreWebView2ControllerWindowReference]],  # value
                                _type.HRESULT]
    put_ParentWindow: _Callable[[ICoreWebView2ControllerWindowReference],  # value
                                _type.HRESULT]
    get_CoreWebView2: _Callable[[_Pointer[ICoreWebView2]],  # value
                                _type.HRESULT]
    add_ZoomFactorChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Controller, _inspectable.IInspectable],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ZoomFactorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    add_MoveFocusRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Controller, ICoreWebView2MoveFocusRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_MoveFocusRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_GotFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Controller, _inspectable.IInspectable],  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_LostFocus: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Controller, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_AcceleratorKeyPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Controller, ICoreWebView2AcceleratorKeyPressedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_AcceleratorKeyPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    SetBoundsAndZoomFactor: _Callable[[_struct.Windows.Foundation.Rect,  # Bounds
                                       _type.DOUBLE],  # ZoomFactor
                                      _type.HRESULT]
    MoveFocus: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusReason],  # reason
                         _type.HRESULT]
    NotifyParentWindowPositionChanged: _Callable[[],
                                                 _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class ICoreWebView2Controller2(_inspectable.IInspectable):
    get_DefaultBackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                          _type.HRESULT]
    put_DefaultBackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                          _type.HRESULT]


class ICoreWebView2Controller3(_inspectable.IInspectable):
    get_RasterizationScale: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                      _type.HRESULT]
    put_RasterizationScale: _Callable[[_type.DOUBLE],  # value
                                      _type.HRESULT]
    get_ShouldDetectMonitorScaleChanges: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_ShouldDetectMonitorScaleChanges: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]
    get_BoundsMode: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2BoundsMode]],  # value
                              _type.HRESULT]
    put_BoundsMode: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2BoundsMode],  # value
                              _type.HRESULT]
    add_RasterizationScaleChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Controller, _inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_RasterizationScaleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]


class ICoreWebView2Controller4(_inspectable.IInspectable):
    get_AllowExternalDrop: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_AllowExternalDrop: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]


class ICoreWebView2ControllerFactory(_inspectable.IInspectable):
    pass


class ICoreWebView2ControllerOptions(_inspectable.IInspectable):
    get_ProfileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ProfileName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_IsInPrivateModeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_IsInPrivateModeEnabled: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]


class ICoreWebView2ControllerOptions2(_inspectable.IInspectable):
    get_ScriptLocale: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_ScriptLocale: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]


class ICoreWebView2ControllerWindowReference(_inspectable.IInspectable):
    get_WindowHandle: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]
    get_CoreWindow: _Callable[[_Pointer[_Windows_UI_Core.ICoreWindow]],  # value
                              _type.HRESULT]


class ICoreWebView2ControllerWindowReferenceStatics(_inspectable.IInspectable):
    CreateFromWindowHandle: _Callable[[_type.UINT64,  # windowHandle
                                       _Pointer[ICoreWebView2ControllerWindowReference]],  # result
                                      _type.HRESULT]
    CreateFromCoreWindow: _Callable[[_Windows_UI_Core.ICoreWindow,  # coreWindow
                                     _Pointer[ICoreWebView2ControllerWindowReference]],  # result
                                    _type.HRESULT]


class ICoreWebView2Cookie(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Domain: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Expires: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Expires: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_IsHttpOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsHttpOnly: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_SameSite: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2CookieSameSiteKind]],  # value
                            _type.HRESULT]
    put_SameSite: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2CookieSameSiteKind],  # value
                            _type.HRESULT]
    get_IsSecure: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_IsSecure: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_IsSession: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class ICoreWebView2CookieManager(_inspectable.IInspectable):
    CreateCookie: _Callable[[_type.HSTRING,  # name
                             _type.HSTRING,  # value
                             _type.HSTRING,  # Domain
                             _type.HSTRING,  # Path
                             _Pointer[ICoreWebView2Cookie]],  # result
                            _type.HRESULT]
    CopyCookie: _Callable[[ICoreWebView2Cookie,  # cookieParam
                           _Pointer[ICoreWebView2Cookie]],  # result
                          _type.HRESULT]
    AddOrUpdateCookie: _Callable[[ICoreWebView2Cookie],  # cookie
                                 _type.HRESULT]
    DeleteCookie: _Callable[[ICoreWebView2Cookie],  # cookie
                            _type.HRESULT]
    DeleteCookies: _Callable[[_type.HSTRING,  # name
                              _type.HSTRING],  # uri
                             _type.HRESULT]
    DeleteCookiesWithDomainAndPath: _Callable[[_type.HSTRING,  # name
                                               _type.HSTRING,  # Domain
                                               _type.HSTRING],  # Path
                                              _type.HRESULT]
    DeleteAllCookies: _Callable[[],
                                _type.HRESULT]


class ICoreWebView2CookieManager_Manual(_inspectable.IInspectable):
    GetCookiesAsync: _Callable[[_type.HSTRING,  # uri
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[ICoreWebView2Cookie]]]],  # operation
                               _type.HRESULT]


class ICoreWebView2CustomSchemeRegistration(_inspectable.IInspectable):
    get_TreatAsSecure: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_TreatAsSecure: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_HasAuthorityComponent: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_HasAuthorityComponent: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]


class ICoreWebView2DOMContentLoadedEventArgs(_inspectable.IInspectable):
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]


class ICoreWebView2DevToolsProtocolEventReceivedEventArgs(_inspectable.IInspectable):
    get_ParameterObjectAsJson: _Callable[[_Pointer[_type.HSTRING]],  # value
                                         _type.HRESULT]


class ICoreWebView2DevToolsProtocolEventReceivedEventArgs2(_inspectable.IInspectable):
    get_SessionId: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class ICoreWebView2DevToolsProtocolEventReceiver(_inspectable.IInspectable):
    add_DevToolsProtocolEventReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2DevToolsProtocolEventReceivedEventArgs],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_DevToolsProtocolEventReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]


class ICoreWebView2DispatchAdapter(_inspectable.IInspectable):
    WrapNamedObject: _Callable[[_type.HSTRING,  # name
                                ICoreWebView2DispatchAdapter,  # adapter
                                _Pointer[_inspectable.IInspectable]],  # result
                               _type.HRESULT]
    WrapObject: _Callable[[_inspectable.IInspectable,  # unwrapped
                           ICoreWebView2DispatchAdapter,  # adapter
                           _Pointer[_inspectable.IInspectable]],  # result
                          _type.HRESULT]
    UnwrapObject: _Callable[[_inspectable.IInspectable,  # wrapped
                             _Pointer[_inspectable.IInspectable]],  # result
                            _type.HRESULT]
    Clean: _Callable[[],
                     _type.HRESULT]


class ICoreWebView2DownloadOperation(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_ContentDisposition: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_MimeType: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_TotalBytesToReceive: _Callable[[_Pointer[_type.INT64]],  # value
                                       _type.HRESULT]
    get_BytesReceived: _Callable[[_Pointer[_type.INT64]],  # value
                                 _type.HRESULT]
    get_EstimatedEndTime: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_ResultFilePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2DownloadState]],  # value
                         _type.HRESULT]
    get_InterruptReason: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2DownloadInterruptReason]],  # value
                                   _type.HRESULT]
    get_CanResume: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    add_BytesReceivedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2DownloadOperation, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_BytesReceivedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_EstimatedEndTimeChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2DownloadOperation, _inspectable.IInspectable],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_EstimatedEndTimeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2DownloadOperation, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]


class ICoreWebView2DownloadStartingEventArgs(_inspectable.IInspectable):
    get_DownloadOperation: _Callable[[_Pointer[ICoreWebView2DownloadOperation]],  # value
                                     _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_ResultFilePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_ResultFilePath: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2Environment(_inspectable.IInspectable):
    get_BrowserVersionString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    add_NewBrowserVersionAvailable: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Environment, _inspectable.IInspectable],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_NewBrowserVersionAvailable: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]
    CreateCoreWebView2ControllerAsync: _Callable[[ICoreWebView2ControllerWindowReference,  # ParentWindow
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[ICoreWebView2Controller]]],  # operation
                                                 _type.HRESULT]
    CreateWebResourceResponse: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # Content
                                          _type.INT32,  # StatusCode
                                          _type.HSTRING,  # ReasonPhrase
                                          _type.HSTRING,  # Headers
                                          _Pointer[ICoreWebView2WebResourceResponse]],  # result
                                         _type.HRESULT]


class ICoreWebView2Environment10(_inspectable.IInspectable):
    CreateCoreWebView2ControllerOptions: _Callable[[_Pointer[ICoreWebView2ControllerOptions]],  # result
                                                   _type.HRESULT]


class ICoreWebView2Environment11(_inspectable.IInspectable):
    get_FailureReportFolderPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                           _type.HRESULT]


class ICoreWebView2Environment12(_inspectable.IInspectable):
    CreateSharedBuffer: _Callable[[_type.UINT64,  # Size
                                   _Pointer[ICoreWebView2SharedBuffer]],  # result
                                  _type.HRESULT]


class ICoreWebView2Environment2(_inspectable.IInspectable):
    CreateWebResourceRequest: _Callable[[_type.HSTRING,  # uri
                                         _type.HSTRING,  # Method
                                         _Windows_Storage_Streams.IRandomAccessStream,  # postData
                                         _type.HSTRING,  # Headers
                                         _Pointer[ICoreWebView2WebResourceRequest]],  # result
                                        _type.HRESULT]


class ICoreWebView2Environment3(_inspectable.IInspectable):
    CreateCoreWebView2CompositionControllerAsync: _Callable[[ICoreWebView2ControllerWindowReference,  # ParentWindow
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[ICoreWebView2CompositionController]]],  # operation
                                                            _type.HRESULT]
    CreateCoreWebView2PointerInfo: _Callable[[_Pointer[ICoreWebView2PointerInfo]],  # result
                                             _type.HRESULT]


class ICoreWebView2Environment4(_inspectable.IInspectable):
    pass


class ICoreWebView2Environment5(_inspectable.IInspectable):
    add_BrowserProcessExited: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Environment, ICoreWebView2BrowserProcessExitedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_BrowserProcessExited: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class ICoreWebView2Environment6(_inspectable.IInspectable):
    CreatePrintSettings: _Callable[[_Pointer[ICoreWebView2PrintSettings]],  # result
                                   _type.HRESULT]


class ICoreWebView2Environment7(_inspectable.IInspectable):
    get_UserDataFolder: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class ICoreWebView2Environment8(_inspectable.IInspectable):
    add_ProcessInfosChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Environment, _inspectable.IInspectable],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ProcessInfosChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetProcessInfos: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreWebView2ProcessInfo]]],  # result
                               _type.HRESULT]


class ICoreWebView2Environment9(_inspectable.IInspectable):
    CreateContextMenuItem: _Callable[[_type.HSTRING,  # Label
                                      _Windows_Storage_Streams.IRandomAccessStream,  # iconStream
                                      _enum.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItemKind,  # Kind
                                      _Pointer[ICoreWebView2ContextMenuItem]],  # result
                                     _type.HRESULT]


class ICoreWebView2EnvironmentOptions(_inspectable.IInspectable):
    get_AdditionalBrowserArguments: _Callable[[_Pointer[_type.HSTRING]],  # value
                                              _type.HRESULT]
    put_AdditionalBrowserArguments: _Callable[[_type.HSTRING],  # value
                                              _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_TargetCompatibleBrowserVersion: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                  _type.HRESULT]
    put_TargetCompatibleBrowserVersion: _Callable[[_type.HSTRING],  # value
                                                  _type.HRESULT]
    get_AllowSingleSignOnUsingOSPrimaryAccount: _Callable[[_Pointer[_type.boolean]],  # value
                                                          _type.HRESULT]
    put_AllowSingleSignOnUsingOSPrimaryAccount: _Callable[[_type.boolean],  # value
                                                          _type.HRESULT]


class ICoreWebView2EnvironmentOptions2(_inspectable.IInspectable):
    get_ExclusiveUserDataFolderAccess: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_ExclusiveUserDataFolderAccess: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]


class ICoreWebView2EnvironmentOptions3(_inspectable.IInspectable):
    get_IsCustomCrashReportingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_IsCustomCrashReportingEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]


class ICoreWebView2EnvironmentOptions4(_inspectable.IInspectable):
    pass


class ICoreWebView2EnvironmentOptions5(_inspectable.IInspectable):
    get_EnableTrackingPrevention: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_EnableTrackingPrevention: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class ICoreWebView2EnvironmentOptions_Manual(_inspectable.IInspectable):
    pass


class ICoreWebView2EnvironmentStatics(_inspectable.IInspectable):
    CreateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ICoreWebView2Environment]]],  # operation
                           _type.HRESULT]
    CreateWithOptionsAsync: _Callable[[_type.HSTRING,  # browserExecutableFolder
                                       _type.HSTRING,  # userDataFolder
                                       ICoreWebView2EnvironmentOptions,  # options
                                       _Pointer[_Windows_Foundation.IAsyncOperation[ICoreWebView2Environment]]],  # operation
                                      _type.HRESULT]
    GetAvailableBrowserVersionString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                                _type.HRESULT]
    GetAvailableBrowserVersionString2: _Callable[[_type.HSTRING,  # browserExecutableFolder
                                                  _Pointer[_type.HSTRING]],  # result
                                                 _type.HRESULT]
    CompareBrowserVersionString: _Callable[[_type.HSTRING,  # browserVersionString1
                                            _type.HSTRING,  # browserVersionString2
                                            _Pointer[_type.INT32]],  # result
                                           _type.HRESULT]


class ICoreWebView2Environment_Manual(_inspectable.IInspectable):
    CreateCoreWebView2ControllerAsync: _Callable[[ICoreWebView2ControllerWindowReference,  # ParentWindow
                                                  ICoreWebView2ControllerOptions,  # options
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[ICoreWebView2Controller]]],  # operation
                                                 _type.HRESULT]
    CreateCoreWebView2CompositionControllerAsync: _Callable[[ICoreWebView2ControllerWindowReference,  # ParentWindow
                                                             ICoreWebView2ControllerOptions,  # options
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[ICoreWebView2CompositionController]]],  # operation
                                                            _type.HRESULT]


class ICoreWebView2File(_inspectable.IInspectable):
    get_Path: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ICoreWebView2Frame(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    add_NameChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, _inspectable.IInspectable],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_NameChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    add_Destroyed: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, _inspectable.IInspectable],  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Destroyed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    RemoveHostObjectFromScript: _Callable[[_type.HSTRING],  # name
                                          _type.HRESULT]
    IsDestroyed: _Callable[[_Pointer[_type.INT32]],  # result
                           _type.HRESULT]


class ICoreWebView2Frame2(_inspectable.IInspectable):
    add_NavigationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, ICoreWebView2NavigationStartingEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContentLoading: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, ICoreWebView2ContentLoadingEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_NavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, ICoreWebView2NavigationCompletedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_DOMContentLoaded: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, ICoreWebView2DOMContentLoadedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_WebMessageReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, ICoreWebView2WebMessageReceivedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_WebMessageReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    ExecuteScriptAsync: _Callable[[_type.HSTRING,  # javaScript
                                   _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                  _type.HRESULT]
    PostWebMessageAsJson: _Callable[[_type.HSTRING],  # webMessageAsJson
                                    _type.HRESULT]
    PostWebMessageAsString: _Callable[[_type.HSTRING],  # webMessageAsString
                                      _type.HRESULT]


class ICoreWebView2Frame3(_inspectable.IInspectable):
    add_PermissionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2Frame, ICoreWebView2PermissionRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PermissionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class ICoreWebView2Frame4(_inspectable.IInspectable):
    PostSharedBufferToScript: _Callable[[ICoreWebView2SharedBuffer,  # sharedBuffer
                                         _enum.Microsoft.Web.WebView2.Core.CoreWebView2SharedBufferAccess,  # access
                                         _type.HSTRING],  # additionalDataAsJson
                                        _type.HRESULT]


class ICoreWebView2FrameCreatedEventArgs(_inspectable.IInspectable):
    get_Frame: _Callable[[_Pointer[ICoreWebView2Frame]],  # value
                         _type.HRESULT]


class ICoreWebView2FrameInfo(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Source: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]


class ICoreWebView2HttpHeadersCollectionIterator(_inspectable.IInspectable):
    pass


class ICoreWebView2HttpRequestHeaders(_inspectable.IInspectable):
    GetHeader: _Callable[[_type.HSTRING,  # name
                          _Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]
    GetHeaders: _Callable[[_type.HSTRING,  # name
                           _Pointer[ICoreWebView2HttpHeadersCollectionIterator]],  # result
                          _type.HRESULT]
    Contains: _Callable[[_type.HSTRING,  # name
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    SetHeader: _Callable[[_type.HSTRING,  # name
                          _type.HSTRING],  # value
                         _type.HRESULT]
    RemoveHeader: _Callable[[_type.HSTRING],  # name
                            _type.HRESULT]


class ICoreWebView2HttpResponseHeaders(_inspectable.IInspectable):
    AppendHeader: _Callable[[_type.HSTRING,  # name
                             _type.HSTRING],  # value
                            _type.HRESULT]
    Contains: _Callable[[_type.HSTRING,  # name
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    GetHeader: _Callable[[_type.HSTRING,  # name
                          _Pointer[_type.HSTRING]],  # result
                         _type.HRESULT]
    GetHeaders: _Callable[[_type.HSTRING,  # name
                           _Pointer[ICoreWebView2HttpHeadersCollectionIterator]],  # result
                          _type.HRESULT]


class ICoreWebView2LaunchingExternalUriSchemeEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_InitiatingOrigin: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2MoveFocusRequestedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusReason]],  # value
                          _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICoreWebView2NavigationCompletedEventArgs(_inspectable.IInspectable):
    get_IsSuccess: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_WebErrorStatus: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2WebErrorStatus]],  # value
                                  _type.HRESULT]
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]


class ICoreWebView2NavigationCompletedEventArgs2(_inspectable.IInspectable):
    get_HttpStatusCode: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]


class ICoreWebView2NavigationStartingEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_IsRedirected: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    get_RequestHeaders: _Callable[[_Pointer[ICoreWebView2HttpRequestHeaders]],  # value
                                  _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # value
                                _type.HRESULT]


class ICoreWebView2NavigationStartingEventArgs2(_inspectable.IInspectable):
    get_AdditionalAllowedFrameAncestors: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                   _type.HRESULT]
    put_AdditionalAllowedFrameAncestors: _Callable[[_type.HSTRING],  # value
                                                   _type.HRESULT]


class ICoreWebView2NewWindowRequestedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_NewWindow: _Callable[[_Pointer[ICoreWebView2]],  # value
                             _type.HRESULT]
    put_NewWindow: _Callable[[ICoreWebView2],  # value
                             _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_WindowFeatures: _Callable[[_Pointer[ICoreWebView2WindowFeatures]],  # value
                                  _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2NewWindowRequestedEventArgs2(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ICoreWebView2PermissionRequestedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_PermissionKind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind]],  # value
                                  _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState]],  # value
                         _type.HRESULT]
    put_State: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState],  # value
                         _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2PermissionRequestedEventArgs2(_inspectable.IInspectable):
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class ICoreWebView2PermissionRequestedEventArgs3(_inspectable.IInspectable):
    get_SavesInProfile: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_SavesInProfile: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]


class ICoreWebView2PermissionSetting(_inspectable.IInspectable):
    get_PermissionKind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind]],  # value
                                  _type.HRESULT]
    get_PermissionOrigin: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    get_PermissionState: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState]],  # value
                                   _type.HRESULT]


class ICoreWebView2PointerInfo(_inspectable.IInspectable):
    get_PointerKind: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_PointerKind: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_PointerId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_PointerId: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_FrameId: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_FrameId: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_PointerFlags: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    put_PointerFlags: _Callable[[_type.UINT32],  # value
                                _type.HRESULT]
    get_PointerDeviceRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                     _type.HRESULT]
    put_PointerDeviceRect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                     _type.HRESULT]
    get_DisplayRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                               _type.HRESULT]
    put_DisplayRect: _Callable[[_struct.Windows.Foundation.Rect],  # value
                               _type.HRESULT]
    get_PixelLocation: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                 _type.HRESULT]
    put_PixelLocation: _Callable[[_struct.Windows.Foundation.Point],  # value
                                 _type.HRESULT]
    get_HimetricLocation: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                    _type.HRESULT]
    put_HimetricLocation: _Callable[[_struct.Windows.Foundation.Point],  # value
                                    _type.HRESULT]
    get_PixelLocationRaw: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                    _type.HRESULT]
    put_PixelLocationRaw: _Callable[[_struct.Windows.Foundation.Point],  # value
                                    _type.HRESULT]
    get_HimetricLocationRaw: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                       _type.HRESULT]
    put_HimetricLocationRaw: _Callable[[_struct.Windows.Foundation.Point],  # value
                                       _type.HRESULT]
    get_Time: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    put_Time: _Callable[[_type.UINT32],  # value
                        _type.HRESULT]
    get_HistoryCount: _Callable[[_Pointer[_type.UINT32]],  # value
                                _type.HRESULT]
    put_HistoryCount: _Callable[[_type.UINT32],  # value
                                _type.HRESULT]
    get_InputData: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_InputData: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_KeyStates: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_KeyStates: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_PerformanceCount: _Callable[[_Pointer[_type.UINT64]],  # value
                                    _type.HRESULT]
    put_PerformanceCount: _Callable[[_type.UINT64],  # value
                                    _type.HRESULT]
    get_ButtonChangeKind: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_ButtonChangeKind: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_PenFlags: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    put_PenFlags: _Callable[[_type.UINT32],  # value
                            _type.HRESULT]
    get_PenMask: _Callable[[_Pointer[_type.UINT32]],  # value
                           _type.HRESULT]
    put_PenMask: _Callable[[_type.UINT32],  # value
                           _type.HRESULT]
    get_PenPressure: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_PenPressure: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_PenRotation: _Callable[[_Pointer[_type.UINT32]],  # value
                               _type.HRESULT]
    put_PenRotation: _Callable[[_type.UINT32],  # value
                               _type.HRESULT]
    get_PenTiltX: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_PenTiltX: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_PenTiltY: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_PenTiltY: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    get_TouchFlags: _Callable[[_Pointer[_type.UINT32]],  # value
                              _type.HRESULT]
    put_TouchFlags: _Callable[[_type.UINT32],  # value
                              _type.HRESULT]
    get_TouchMask: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_TouchMask: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    get_TouchContact: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    put_TouchContact: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                _type.HRESULT]
    get_TouchContactRaw: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                   _type.HRESULT]
    put_TouchContactRaw: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                   _type.HRESULT]
    get_TouchOrientation: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    put_TouchOrientation: _Callable[[_type.UINT32],  # value
                                    _type.HRESULT]
    get_TouchPressure: _Callable[[_Pointer[_type.UINT32]],  # value
                                 _type.HRESULT]
    put_TouchPressure: _Callable[[_type.UINT32],  # value
                                 _type.HRESULT]


class ICoreWebView2PrintSettings(_inspectable.IInspectable):
    get_Orientation: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintOrientation]],  # value
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintOrientation],  # value
                               _type.HRESULT]
    get_ScaleFactor: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_ScaleFactor: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_PageWidth: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_PageWidth: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_PageHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_PageHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_MarginTop: _Callable[[_Pointer[_type.DOUBLE]],  # value
                             _type.HRESULT]
    put_MarginTop: _Callable[[_type.DOUBLE],  # value
                             _type.HRESULT]
    get_MarginBottom: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_MarginBottom: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_MarginLeft: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_MarginLeft: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_MarginRight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_MarginRight: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_ShouldPrintBackgrounds: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    put_ShouldPrintBackgrounds: _Callable[[_type.boolean],  # value
                                          _type.HRESULT]
    get_ShouldPrintSelectionOnly: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_ShouldPrintSelectionOnly: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_ShouldPrintHeaderAndFooter: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_ShouldPrintHeaderAndFooter: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]
    get_HeaderTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_HeaderTitle: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_FooterUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_FooterUri: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class ICoreWebView2PrintSettings2(_inspectable.IInspectable):
    get_PageRanges: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_PageRanges: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    get_PagesPerSide: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    put_PagesPerSide: _Callable[[_type.INT32],  # value
                                _type.HRESULT]
    get_Copies: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_Copies: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    get_Collation: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintCollation]],  # value
                             _type.HRESULT]
    put_Collation: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintCollation],  # value
                             _type.HRESULT]
    get_ColorMode: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintColorMode]],  # value
                             _type.HRESULT]
    put_ColorMode: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintColorMode],  # value
                             _type.HRESULT]
    get_Duplex: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintDuplex]],  # value
                          _type.HRESULT]
    put_Duplex: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintDuplex],  # value
                          _type.HRESULT]
    get_MediaSize: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintMediaSize]],  # value
                             _type.HRESULT]
    put_MediaSize: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintMediaSize],  # value
                             _type.HRESULT]
    get_PrinterName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_PrinterName: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]


class ICoreWebView2PrivatePartial(_inspectable.IInspectable):
    pass


class ICoreWebView2PrivatePartialController(_inspectable.IInspectable):
    get_IsBrowserHitTransparent: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class ICoreWebView2ProcessFailedEventArgs(_inspectable.IInspectable):
    get_ProcessFailedKind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedKind]],  # value
                                     _type.HRESULT]


class ICoreWebView2ProcessFailedEventArgs2(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedReason]],  # value
                          _type.HRESULT]
    get_ExitCode: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    get_ProcessDescription: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_FrameInfosForFailedProcess: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreWebView2FrameInfo]]],  # value
                                              _type.HRESULT]


class ICoreWebView2ProcessInfo(_inspectable.IInspectable):
    get_ProcessId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ProcessKind]],  # value
                        _type.HRESULT]


class ICoreWebView2Profile(_inspectable.IInspectable):
    get_ProfileName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_IsInPrivateModeEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    get_ProfilePath: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_DefaultDownloadFolderPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                             _type.HRESULT]
    put_DefaultDownloadFolderPath: _Callable[[_type.HSTRING],  # value
                                             _type.HRESULT]
    get_PreferredColorScheme: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PreferredColorScheme]],  # value
                                        _type.HRESULT]
    put_PreferredColorScheme: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PreferredColorScheme],  # value
                                        _type.HRESULT]


class ICoreWebView2Profile2(_inspectable.IInspectable):
    ClearBrowsingDataAsync: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2BrowsingDataKinds,  # dataKinds
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                      _type.HRESULT]


class ICoreWebView2Profile3(_inspectable.IInspectable):
    get_PreferredTrackingPreventionLevel: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2TrackingPreventionLevel]],  # value
                                                    _type.HRESULT]
    put_PreferredTrackingPreventionLevel: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2TrackingPreventionLevel],  # value
                                                    _type.HRESULT]


class ICoreWebView2Profile4(_inspectable.IInspectable):
    SetPermissionStateAsync: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind,  # PermissionKind
                                        _type.HSTRING,  # origin
                                        _enum.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState,  # State
                                        _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                       _type.HRESULT]


class ICoreWebView2Profile5(_inspectable.IInspectable):
    get_CookieManager: _Callable[[_Pointer[ICoreWebView2CookieManager]],  # value
                                 _type.HRESULT]


class ICoreWebView2Profile6(_inspectable.IInspectable):
    get_IsPasswordAutosaveEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsPasswordAutosaveEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsGeneralAutofillEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsGeneralAutofillEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class ICoreWebView2ScriptDialogOpeningEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ScriptDialogKind]],  # value
                        _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    get_DefaultText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_ResultText: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    put_ResultText: _Callable[[_type.HSTRING],  # value
                              _type.HRESULT]
    Accept: _Callable[[],
                      _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2ServerCertificateErrorDetectedEventArgs(_inspectable.IInspectable):
    get_ErrorStatus: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2WebErrorStatus]],  # value
                               _type.HRESULT]
    get_RequestUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_ServerCertificate: _Callable[[_Pointer[ICoreWebView2Certificate]],  # value
                                     _type.HRESULT]
    get_Action: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorAction]],  # value
                          _type.HRESULT]
    put_Action: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorAction],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2Settings(_inspectable.IInspectable):
    get_IsScriptEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    put_IsScriptEnabled: _Callable[[_type.boolean],  # value
                                   _type.HRESULT]
    get_IsWebMessageEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsWebMessageEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_AreDefaultScriptDialogsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_AreDefaultScriptDialogsEnabled: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    get_IsStatusBarEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsStatusBarEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_AreDevToolsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_AreDevToolsEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_AreDefaultContextMenusEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                 _type.HRESULT]
    put_AreDefaultContextMenusEnabled: _Callable[[_type.boolean],  # value
                                                 _type.HRESULT]
    get_AreHostObjectsAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_AreHostObjectsAllowed: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsZoomControlEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsZoomControlEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_IsBuiltInErrorPageEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsBuiltInErrorPageEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]


class ICoreWebView2Settings2(_inspectable.IInspectable):
    get_UserAgent: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_UserAgent: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]


class ICoreWebView2Settings3(_inspectable.IInspectable):
    get_AreBrowserAcceleratorKeysEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                    _type.HRESULT]
    put_AreBrowserAcceleratorKeysEnabled: _Callable[[_type.boolean],  # value
                                                    _type.HRESULT]


class ICoreWebView2Settings4(_inspectable.IInspectable):
    get_IsPasswordAutosaveEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    put_IsPasswordAutosaveEnabled: _Callable[[_type.boolean],  # value
                                             _type.HRESULT]
    get_IsGeneralAutofillEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsGeneralAutofillEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class ICoreWebView2Settings5(_inspectable.IInspectable):
    get_IsPinchZoomEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsPinchZoomEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]


class ICoreWebView2Settings6(_inspectable.IInspectable):
    get_IsSwipeNavigationEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsSwipeNavigationEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class ICoreWebView2Settings7(_inspectable.IInspectable):
    get_HiddenPdfToolbarItems: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PdfToolbarItems]],  # value
                                         _type.HRESULT]
    put_HiddenPdfToolbarItems: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PdfToolbarItems],  # value
                                         _type.HRESULT]


class ICoreWebView2Settings8(_inspectable.IInspectable):
    get_IsReputationCheckingRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                                _type.HRESULT]
    put_IsReputationCheckingRequired: _Callable[[_type.boolean],  # value
                                                _type.HRESULT]


class ICoreWebView2Settings_Manual(_inspectable.IInspectable):
    get_HostObjectDispatchAdapter: _Callable[[_Pointer[ICoreWebView2DispatchAdapter]],  # value
                                             _type.HRESULT]
    put_HostObjectDispatchAdapter: _Callable[[ICoreWebView2DispatchAdapter],  # value
                                             _type.HRESULT]


class ICoreWebView2SharedBuffer(_inspectable.IInspectable):
    get_Size: _Callable[[_Pointer[_type.UINT64]],  # value
                        _type.HRESULT]
    OpenStream: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # result
                          _type.HRESULT]


class ICoreWebView2SharedBuffer_Manual(_inspectable.IInspectable):
    get_Buffer: _Callable[[_Pointer[_Windows_Foundation.IMemoryBufferReference]],  # value
                          _type.HRESULT]


class ICoreWebView2SourceChangedEventArgs(_inspectable.IInspectable):
    get_IsNewDocument: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]


class ICoreWebView2WebMessageReceivedEventArgs(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_WebMessageAsJson: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    TryGetWebMessageAsString: _Callable[[_Pointer[_type.HSTRING]],  # result
                                        _type.HRESULT]


class ICoreWebView2WebMessageReceivedEventArgs2(_inspectable.IInspectable):
    get_AdditionalObjects: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]]],  # value
                                     _type.HRESULT]


class ICoreWebView2WebResourceRequest(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    put_Uri: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_Method: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    put_Method: _Callable[[_type.HSTRING],  # value
                          _type.HRESULT]
    get_Content: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_Storage_Streams.IRandomAccessStream],  # value
                           _type.HRESULT]
    get_Headers: _Callable[[_Pointer[ICoreWebView2HttpRequestHeaders]],  # value
                           _type.HRESULT]


class ICoreWebView2WebResourceRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[ICoreWebView2WebResourceRequest]],  # value
                           _type.HRESULT]
    get_Response: _Callable[[_Pointer[ICoreWebView2WebResourceResponse]],  # value
                            _type.HRESULT]
    put_Response: _Callable[[ICoreWebView2WebResourceResponse],  # value
                            _type.HRESULT]
    get_ResourceContext: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext]],  # value
                                   _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # result
                           _type.HRESULT]


class ICoreWebView2WebResourceResponse(_inspectable.IInspectable):
    get_Content: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStream]],  # value
                           _type.HRESULT]
    put_Content: _Callable[[_Windows_Storage_Streams.IRandomAccessStream],  # value
                           _type.HRESULT]
    get_Headers: _Callable[[_Pointer[ICoreWebView2HttpResponseHeaders]],  # value
                           _type.HRESULT]
    get_StatusCode: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    put_StatusCode: _Callable[[_type.INT32],  # value
                              _type.HRESULT]
    get_ReasonPhrase: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    put_ReasonPhrase: _Callable[[_type.HSTRING],  # value
                                _type.HRESULT]


class ICoreWebView2WebResourceResponseReceivedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[ICoreWebView2WebResourceRequest]],  # value
                           _type.HRESULT]
    get_Response: _Callable[[_Pointer[ICoreWebView2WebResourceResponseView]],  # value
                            _type.HRESULT]


class ICoreWebView2WebResourceResponseView(_inspectable.IInspectable):
    get_Headers: _Callable[[_Pointer[ICoreWebView2HttpResponseHeaders]],  # value
                           _type.HRESULT]
    get_StatusCode: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]
    get_ReasonPhrase: _Callable[[_Pointer[_type.HSTRING]],  # value
                                _type.HRESULT]
    GetContentAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                               _type.HRESULT]


class ICoreWebView2WindowFeatures(_inspectable.IInspectable):
    get_HasPosition: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    get_HasSize: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Left: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Top: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_ShouldDisplayMenuBar: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_ShouldDisplayStatus: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    get_ShouldDisplayToolbar: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    get_ShouldDisplayScrollBars: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]


class ICoreWebView2_10(_inspectable.IInspectable):
    add_BasicAuthenticationRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2BasicAuthenticationRequestedEventArgs],  # handler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_BasicAuthenticationRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]


class ICoreWebView2_11(_inspectable.IInspectable):
    add_ContextMenuRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2ContextMenuRequestedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ContextMenuRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    CallDevToolsProtocolMethodForSessionAsync: _Callable[[_type.HSTRING,  # sessionId
                                                          _type.HSTRING,  # methodName
                                                          _type.HSTRING,  # parametersAsJson
                                                          _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                                         _type.HRESULT]


class ICoreWebView2_12(_inspectable.IInspectable):
    get_StatusBarText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    add_StatusBarTextChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_StatusBarTextChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class ICoreWebView2_13(_inspectable.IInspectable):
    get_Profile: _Callable[[_Pointer[ICoreWebView2Profile]],  # value
                           _type.HRESULT]


class ICoreWebView2_14(_inspectable.IInspectable):
    add_ServerCertificateErrorDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2ServerCertificateErrorDetectedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_ServerCertificateErrorDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    ClearServerCertificateErrorActionsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                                       _type.HRESULT]


class ICoreWebView2_15(_inspectable.IInspectable):
    get_FaviconUri: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    add_FaviconChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_FaviconChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    GetFaviconAsync: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2FaviconImageFormat,  # format
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                               _type.HRESULT]


class ICoreWebView2_16(_inspectable.IInspectable):
    PrintAsync: _Callable[[ICoreWebView2PrintSettings,  # printSettings
                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintStatus]]],  # operation
                          _type.HRESULT]
    ShowPrintUI: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2PrintDialogKind],  # printDialogKind
                           _type.HRESULT]
    PrintToPdfStreamAsync: _Callable[[ICoreWebView2PrintSettings,  # printSettings
                                      _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IRandomAccessStream]]],  # operation
                                     _type.HRESULT]


class ICoreWebView2_17(_inspectable.IInspectable):
    PostSharedBufferToScript: _Callable[[ICoreWebView2SharedBuffer,  # sharedBuffer
                                         _enum.Microsoft.Web.WebView2.Core.CoreWebView2SharedBufferAccess,  # access
                                         _type.HSTRING],  # additionalDataAsJson
                                        _type.HRESULT]


class ICoreWebView2_18(_inspectable.IInspectable):
    add_LaunchingExternalUriScheme: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2LaunchingExternalUriSchemeEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_LaunchingExternalUriScheme: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


class ICoreWebView2_19(_inspectable.IInspectable):
    get_MemoryUsageTargetLevel: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2MemoryUsageTargetLevel]],  # value
                                          _type.HRESULT]
    put_MemoryUsageTargetLevel: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2MemoryUsageTargetLevel],  # value
                                          _type.HRESULT]


class ICoreWebView2_2(_inspectable.IInspectable):
    get_CookieManager: _Callable[[_Pointer[ICoreWebView2CookieManager]],  # value
                                 _type.HRESULT]
    get_Environment: _Callable[[_Pointer[ICoreWebView2Environment]],  # value
                               _type.HRESULT]
    add_WebResourceResponseReceived: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2WebResourceResponseReceivedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_WebResourceResponseReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_DOMContentLoaded: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2DOMContentLoadedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    NavigateWithWebResourceRequest: _Callable[[ICoreWebView2WebResourceRequest],  # Request
                                              _type.HRESULT]


class ICoreWebView2_3(_inspectable.IInspectable):
    get_IsSuspended: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    TrySuspendAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                               _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    SetVirtualHostNameToFolderMapping: _Callable[[_type.HSTRING,  # hostName
                                                  _type.HSTRING,  # folderPath
                                                  _enum.Microsoft.Web.WebView2.Core.CoreWebView2HostResourceAccessKind],  # accessKind
                                                 _type.HRESULT]
    ClearVirtualHostNameToFolderMapping: _Callable[[_type.HSTRING],  # hostName
                                                   _type.HRESULT]


class ICoreWebView2_4(_inspectable.IInspectable):
    add_FrameCreated: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2FrameCreatedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FrameCreated: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_DownloadStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2DownloadStartingEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DownloadStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


class ICoreWebView2_5(_inspectable.IInspectable):
    add_ClientCertificateRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, ICoreWebView2ClientCertificateRequestedEventArgs],  # handler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_ClientCertificateRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


class ICoreWebView2_6(_inspectable.IInspectable):
    OpenTaskManagerWindow: _Callable[[],
                                     _type.HRESULT]


class ICoreWebView2_7(_inspectable.IInspectable):
    PrintToPdfAsync: _Callable[[_type.HSTRING,  # ResultFilePath
                                ICoreWebView2PrintSettings,  # printSettings
                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                               _type.HRESULT]


class ICoreWebView2_8(_inspectable.IInspectable):
    get_IsMuted: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_IsMuted: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_IsDocumentPlayingAudio: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]
    add_IsMutedChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_IsMutedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_IsDocumentPlayingAudioChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_IsDocumentPlayingAudioChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]


class ICoreWebView2_9(_inspectable.IInspectable):
    get_IsDefaultDownloadDialogOpen: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    get_DefaultDownloadDialogCornerAlignment: _Callable[[_Pointer[_enum.Microsoft.Web.WebView2.Core.CoreWebView2DefaultDownloadDialogCornerAlignment]],  # value
                                                        _type.HRESULT]
    put_DefaultDownloadDialogCornerAlignment: _Callable[[_enum.Microsoft.Web.WebView2.Core.CoreWebView2DefaultDownloadDialogCornerAlignment],  # value
                                                        _type.HRESULT]
    get_DefaultDownloadDialogMargin: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                               _type.HRESULT]
    put_DefaultDownloadDialogMargin: _Callable[[_struct.Windows.Foundation.Point],  # value
                                               _type.HRESULT]
    add_IsDefaultDownloadDialogOpenChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWebView2, _inspectable.IInspectable],  # handler
                                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                                      _type.HRESULT]
    remove_IsDefaultDownloadDialogOpenChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                         _type.HRESULT]
    OpenDefaultDownloadDialog: _Callable[[],
                                         _type.HRESULT]
    CloseDefaultDownloadDialog: _Callable[[],
                                          _type.HRESULT]
