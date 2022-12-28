from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Http as _Windows_Web_Http
from ... import Foundation as _Windows_Foundation
from ... import Web as _Windows_Web
from ...ApplicationModel import DataTransfer as _Windows_ApplicationModel_DataTransfer
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IWebViewControl(_inspectable.IInspectable):
    get_Source: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                          _type.HRESULT]
    put_Source: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # source
                          _type.HRESULT]
    get_DocumentTitle: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_CanGoBack: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_CanGoForward: _Callable[[_Pointer[_type.boolean]],  # value
                                _type.HRESULT]
    put_DefaultBackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                          _type.HRESULT]
    get_DefaultBackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                          _type.HRESULT]
    get_ContainsFullScreenElement: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]
    get_Settings: _Callable[[_Pointer[IWebViewControlSettings]],  # value
                            _type.HRESULT]
    get_DeferredPermissionRequests: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IWebViewControlDeferredPermissionRequest]]],  # value
                                              _type.HRESULT]
    GoForward: _Callable[[],
                         _type.HRESULT]
    GoBack: _Callable[[],
                      _type.HRESULT]
    Refresh: _Callable[[],
                       _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    Navigate: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # source
                        _type.HRESULT]
    NavigateToString: _Callable[[_type.HSTRING],  # text
                                _type.HRESULT]
    NavigateToLocalStreamUri: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # source
                                         _Windows_Web.IUriToStreamResolver],  # streamResolver
                                        _type.HRESULT]
    NavigateWithHttpRequestMessage: _Callable[[_Windows_Web_Http.IHttpRequestMessage],  # requestMessage
                                              _type.HRESULT]
    InvokeScriptAsync: _Callable[[_type.HSTRING,  # scriptName
                                  _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # arguments
                                  _Pointer[_Windows_Foundation.IAsyncOperation[_type.HSTRING]]],  # operation
                                 _type.HRESULT]
    CapturePreviewToStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStream,  # stream
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                           _type.HRESULT]
    CaptureSelectedContentToDataPackageAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_Windows_ApplicationModel_DataTransfer.IDataPackage]]],  # operation
                                                        _type.HRESULT]
    BuildLocalStreamUri: _Callable[[_type.HSTRING,  # contentIdentifier
                                    _type.HSTRING,  # relativePath
                                    _Pointer[_Windows_Foundation.IUriRuntimeClass]],  # result
                                   _type.HRESULT]
    GetDeferredPermissionRequestById: _Callable[[_type.UINT32,  # id
                                                 _Pointer[IWebViewControlDeferredPermissionRequest]],  # result
                                                _type.HRESULT]
    add_NavigationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlNavigationStartingEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContentLoading: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlContentLoadingEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_DOMContentLoaded: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlDOMContentLoadedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    add_NavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlNavigationCompletedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_FrameNavigationStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlNavigationStartingEventArgs],  # handler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_FrameNavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_FrameContentLoading: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlContentLoadingEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_FrameContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_FrameDOMContentLoaded: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlDOMContentLoadedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_FrameDOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    add_FrameNavigationCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlNavigationCompletedEventArgs],  # handler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_FrameNavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_ScriptNotify: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlScriptNotifyEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_ScriptNotify: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_LongRunningScriptDetected: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlLongRunningScriptDetectedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_LongRunningScriptDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_UnsafeContentWarningDisplaying: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, _inspectable.IInspectable],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_UnsafeContentWarningDisplaying: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_UnviewableContentIdentified: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlUnviewableContentIdentifiedEventArgs],  # handler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_UnviewableContentIdentified: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    add_PermissionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlPermissionRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PermissionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_UnsupportedUriSchemeIdentified: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_UnsupportedUriSchemeIdentified: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    add_NewWindowRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlNewWindowRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NewWindowRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContainsFullScreenElementChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, _inspectable.IInspectable],  # handler
                                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                                    _type.HRESULT]
    remove_ContainsFullScreenElementChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                       _type.HRESULT]
    add_WebResourceRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IWebViewControl, IWebViewControlWebResourceRequestedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_WebResourceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class IWebViewControl2(_inspectable.IInspectable):
    AddInitializeScript: _Callable[[_type.HSTRING],  # script
                                   _type.HRESULT]


class IWebViewControlContentLoadingEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IWebViewControlDOMContentLoadedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]


class IWebViewControlDeferredPermissionRequest(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_PermissionType: _Callable[[_Pointer[_enum.Windows.Web.UI.WebViewControlPermissionType]],  # value
                                  _type.HRESULT]
    Allow: _Callable[[],
                     _type.HRESULT]
    Deny: _Callable[[],
                    _type.HRESULT]


class IWebViewControlLongRunningScriptDetectedEventArgs(_inspectable.IInspectable):
    get_ExecutionTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]
    get_StopPageScriptExecution: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_StopPageScriptExecution: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]


class IWebViewControlNavigationCompletedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_IsSuccess: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_WebErrorStatus: _Callable[[_Pointer[_enum.Windows.Web.WebErrorStatus]],  # value
                                  _type.HRESULT]


class IWebViewControlNavigationStartingEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.boolean],  # value
                          _type.HRESULT]


class IWebViewControlNewWindowRequestedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Referrer: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IWebViewControlNewWindowRequestedEventArgs2(_inspectable.IInspectable):
    get_NewWindow: _Callable[[_Pointer[IWebViewControl]],  # value
                             _type.HRESULT]
    put_NewWindow: _Callable[[IWebViewControl],  # value
                             _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # deferral
                           _type.HRESULT]


class IWebViewControlPermissionRequest(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_PermissionType: _Callable[[_Pointer[_enum.Windows.Web.UI.WebViewControlPermissionType]],  # value
                                  _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Web.UI.WebViewControlPermissionState]],  # value
                         _type.HRESULT]
    Defer: _Callable[[],
                     _type.HRESULT]
    Allow: _Callable[[],
                     _type.HRESULT]
    Deny: _Callable[[],
                    _type.HRESULT]


class IWebViewControlPermissionRequestedEventArgs(_inspectable.IInspectable):
    get_PermissionRequest: _Callable[[_Pointer[IWebViewControlPermissionRequest]],  # value
                                     _type.HRESULT]


class IWebViewControlScriptNotifyEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]


class IWebViewControlSettings(_inspectable.IInspectable):
    put_IsJavaScriptEnabled: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsJavaScriptEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_IsIndexedDBEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_IsIndexedDBEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsScriptNotifyAllowed: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsScriptNotifyAllowed: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]


class IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]


class IWebViewControlUnviewableContentIdentifiedEventArgs(_inspectable.IInspectable):
    get_Uri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                       _type.HRESULT]
    get_Referrer: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                            _type.HRESULT]
    get_MediaType: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class IWebViewControlWebResourceRequestedEventArgs(_inspectable.IInspectable):
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # deferral
                           _type.HRESULT]
    get_Request: _Callable[[_Pointer[_Windows_Web_Http.IHttpRequestMessage]],  # value
                           _type.HRESULT]
    put_Response: _Callable[[_Windows_Web_Http.IHttpResponseMessage],  # value
                            _type.HRESULT]
    get_Response: _Callable[[_Pointer[_Windows_Web_Http.IHttpResponseMessage]],  # value
                            _type.HRESULT]
