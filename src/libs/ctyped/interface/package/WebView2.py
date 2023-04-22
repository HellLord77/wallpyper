from __future__ import annotations as _

from typing import Callable as _Callable

from ..um import Unknwnbase as _Unknwnbase
from ..um import objidl as _objidl
from ..um import objidlbase as _objidlbase
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer
from ...enum import WebView2 as _enum_WebView2


class ICoreWebView2AcceleratorKeyPressedEventArgs(_Unknwnbase.IUnknown):
    get_KeyEventKind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_KEY_EVENT_KIND]],  # keyEventKind
                                _type.HRESULT]
    get_VirtualKey: _Callable[[_Pointer[_type.UINT]],  # virtualKey
                              _type.HRESULT]
    get_KeyEventLParam: _Callable[[_Pointer[_type.INT]],  # lParam
                                  _type.HRESULT]
    get_PhysicalKeyStatus: _Callable[[_Pointer[_struct.COREWEBVIEW2_PHYSICAL_KEY_STATUS]],  # physicalKeyStatus
                                     _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.BOOL]],  # handled
                           _type.HRESULT]
    put_Handled: _Callable[[_type.BOOL],  # handled
                           _type.HRESULT]


class _ICoreWebView2AcceleratorKeyPressedEventHandler:
    Invoke: _Callable[[ICoreWebView2Controller,  # sender
                       ICoreWebView2AcceleratorKeyPressedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2AcceleratorKeyPressedEventHandler(_ICoreWebView2AcceleratorKeyPressedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2AcceleratorKeyPressedEventHandler_impl(_ICoreWebView2AcceleratorKeyPressedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       _type.LPCWSTR],  # id
                      _type.HRESULT]


class ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler(_ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler_impl(_ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2CallDevToolsProtocolMethodCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       _type.LPCWSTR],  # returnObjectAsJson
                      _type.HRESULT]


class ICoreWebView2CallDevToolsProtocolMethodCompletedHandler(_ICoreWebView2CallDevToolsProtocolMethodCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2CallDevToolsProtocolMethodCompletedHandler_impl(_ICoreWebView2CallDevToolsProtocolMethodCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2CapturePreviewCompletedHandler:
    Invoke: _Callable[[_type.HRESULT],  # errorCode
                      _type.HRESULT]


class ICoreWebView2CapturePreviewCompletedHandler(_ICoreWebView2CapturePreviewCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2CapturePreviewCompletedHandler_impl(_ICoreWebView2CapturePreviewCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2(_Unknwnbase.IUnknown):
    get_Settings: _Callable[[_Pointer[ICoreWebView2Settings]],  # settings
                            _type.HRESULT]
    get_Source: _Callable[[_Pointer[_type.LPWSTR]],  # uri
                          _type.HRESULT]
    Navigate: _Callable[[_type.LPCWSTR],  # uri
                        _type.HRESULT]
    NavigateToString: _Callable[[_type.LPCWSTR],  # htmlContent
                                _type.HRESULT]
    add_NavigationStarting: _Callable[[ICoreWebView2NavigationStartingEventHandler,  # eventHandler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContentLoading: _Callable[[ICoreWebView2ContentLoadingEventHandler,  # eventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_SourceChanged: _Callable[[ICoreWebView2SourceChangedEventHandler,  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_SourceChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    add_HistoryChanged: _Callable[[ICoreWebView2HistoryChangedEventHandler,  # eventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_HistoryChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_NavigationCompleted: _Callable[[ICoreWebView2NavigationCompletedEventHandler,  # eventHandler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_FrameNavigationStarting: _Callable[[ICoreWebView2NavigationStartingEventHandler,  # eventHandler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_FrameNavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_FrameNavigationCompleted: _Callable[[ICoreWebView2NavigationCompletedEventHandler,  # eventHandler
                                             _Pointer[_struct.EventRegistrationToken]],  # token
                                            _type.HRESULT]
    remove_FrameNavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                               _type.HRESULT]
    add_ScriptDialogOpening: _Callable[[ICoreWebView2ScriptDialogOpeningEventHandler,  # eventHandler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ScriptDialogOpening: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_PermissionRequested: _Callable[[ICoreWebView2PermissionRequestedEventHandler,  # eventHandler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PermissionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_ProcessFailed: _Callable[[ICoreWebView2ProcessFailedEventHandler,  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_ProcessFailed: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    AddScriptToExecuteOnDocumentCreated: _Callable[[_type.LPCWSTR,  # javaScript
                                                    ICoreWebView2AddScriptToExecuteOnDocumentCreatedCompletedHandler],  # handler
                                                   _type.HRESULT]
    RemoveScriptToExecuteOnDocumentCreated: _Callable[[_type.LPCWSTR],  # id
                                                      _type.HRESULT]
    ExecuteScript: _Callable[[_type.LPCWSTR,  # javaScript
                              ICoreWebView2ExecuteScriptCompletedHandler],  # handler
                             _type.HRESULT]
    CapturePreview: _Callable[[_enum_WebView2.COREWEBVIEW2_CAPTURE_PREVIEW_IMAGE_FORMAT,  # imageFormat
                               _objidlbase.IStream,  # imageStream
                               ICoreWebView2CapturePreviewCompletedHandler],  # handler
                              _type.HRESULT]
    Reload: _Callable[[],
                      _type.HRESULT]
    PostWebMessageAsJson: _Callable[[_type.LPCWSTR],  # webMessageAsJson
                                    _type.HRESULT]
    PostWebMessageAsString: _Callable[[_type.LPCWSTR],  # webMessageAsString
                                      _type.HRESULT]
    add_WebMessageReceived: _Callable[[ICoreWebView2WebMessageReceivedEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_WebMessageReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    CallDevToolsProtocolMethod: _Callable[[_type.LPCWSTR,  # methodName
                                           _type.LPCWSTR,  # parametersAsJson
                                           ICoreWebView2CallDevToolsProtocolMethodCompletedHandler],  # handler
                                          _type.HRESULT]
    get_BrowserProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]
    get_CanGoBack: _Callable[[_Pointer[_type.BOOL]],  # canGoBack
                             _type.HRESULT]
    get_CanGoForward: _Callable[[_Pointer[_type.BOOL]],  # canGoForward
                                _type.HRESULT]
    GoBack: _Callable[[],
                      _type.HRESULT]
    GoForward: _Callable[[],
                         _type.HRESULT]
    GetDevToolsProtocolEventReceiver: _Callable[[_type.LPCWSTR,  # eventName
                                                 _Pointer[ICoreWebView2DevToolsProtocolEventReceiver]],  # receiver
                                                _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    add_NewWindowRequested: _Callable[[ICoreWebView2NewWindowRequestedEventHandler,  # eventHandler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NewWindowRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_DocumentTitleChanged: _Callable[[ICoreWebView2DocumentTitleChangedEventHandler,  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_DocumentTitleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_DocumentTitle: _Callable[[_Pointer[_type.LPWSTR]],  # title
                                 _type.HRESULT]
    AddHostObjectToScript: _Callable[[_type.LPCWSTR,  # name
                                      _Pointer[_struct.VARIANT]],  # object
                                     _type.HRESULT]
    RemoveHostObjectFromScript: _Callable[[_type.LPCWSTR],  # name
                                          _type.HRESULT]
    OpenDevToolsWindow: _Callable[[],
                                  _type.HRESULT]
    add_ContainsFullScreenElementChanged: _Callable[[ICoreWebView2ContainsFullScreenElementChangedEventHandler,  # eventHandler
                                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                                    _type.HRESULT]
    remove_ContainsFullScreenElementChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                       _type.HRESULT]
    get_ContainsFullScreenElement: _Callable[[_Pointer[_type.BOOL]],  # containsFullScreenElement
                                             _type.HRESULT]
    add_WebResourceRequested: _Callable[[ICoreWebView2WebResourceRequestedEventHandler,  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_WebResourceRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    AddWebResourceRequestedFilter: _Callable[[_type.LPCWSTR,  # uri
                                              _enum_WebView2.COREWEBVIEW2_WEB_RESOURCE_CONTEXT],  # resourceContext
                                             _type.HRESULT]
    RemoveWebResourceRequestedFilter: _Callable[[_type.LPCWSTR,  # uri
                                                 _enum_WebView2.COREWEBVIEW2_WEB_RESOURCE_CONTEXT],  # resourceContext
                                                _type.HRESULT]
    add_WindowCloseRequested: _Callable[[ICoreWebView2WindowCloseRequestedEventHandler,  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_WindowCloseRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_2(ICoreWebView2):
    add_WebResourceResponseReceived: _Callable[[ICoreWebView2WebResourceResponseReceivedEventHandler,  # eventHandler
                                                _Pointer[_struct.EventRegistrationToken]],  # token
                                               _type.HRESULT]
    remove_WebResourceResponseReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                                  _type.HRESULT]
    NavigateWithWebResourceRequest: _Callable[[ICoreWebView2WebResourceRequest],  # request
                                              _type.HRESULT]
    add_DOMContentLoaded: _Callable[[ICoreWebView2DOMContentLoadedEventHandler,  # eventHandler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    get_CookieManager: _Callable[[_Pointer[ICoreWebView2CookieManager]],  # cookieManager
                                 _type.HRESULT]
    get_Environment: _Callable[[_Pointer[ICoreWebView2Environment]],  # environment
                               _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_3(ICoreWebView2_2):
    TrySuspend: _Callable[[ICoreWebView2TrySuspendCompletedHandler],  # handler
                          _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    get_IsSuspended: _Callable[[_Pointer[_type.BOOL]],  # isSuspended
                               _type.HRESULT]
    SetVirtualHostNameToFolderMapping: _Callable[[_type.LPCWSTR,  # hostName
                                                  _type.LPCWSTR,  # folderPath
                                                  _enum_WebView2.COREWEBVIEW2_HOST_RESOURCE_ACCESS_KIND],  # accessKind
                                                 _type.HRESULT]
    ClearVirtualHostNameToFolderMapping: _Callable[[_type.LPCWSTR],  # hostName
                                                   _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_4(ICoreWebView2_3):
    add_FrameCreated: _Callable[[ICoreWebView2FrameCreatedEventHandler,  # eventHandler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_FrameCreated: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    add_DownloadStarting: _Callable[[ICoreWebView2DownloadStartingEventHandler,  # eventHandler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DownloadStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_5(ICoreWebView2_4):
    add_ClientCertificateRequested: _Callable[[ICoreWebView2ClientCertificateRequestedEventHandler,  # eventHandler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_ClientCertificateRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_6(ICoreWebView2_5):
    OpenTaskManagerWindow: _Callable[[],
                                     _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_7(ICoreWebView2_6):
    PrintToPdf: _Callable[[_type.LPCWSTR,  # resultFilePath
                           ICoreWebView2PrintSettings,  # printSettings
                           ICoreWebView2PrintToPdfCompletedHandler],  # handler
                          _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_8(ICoreWebView2_7):
    add_IsMutedChanged: _Callable[[ICoreWebView2IsMutedChangedEventHandler,  # eventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_IsMutedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    get_IsMuted: _Callable[[_Pointer[_type.BOOL]],  # value
                           _type.HRESULT]
    put_IsMuted: _Callable[[_type.BOOL],  # value
                           _type.HRESULT]
    add_IsDocumentPlayingAudioChanged: _Callable[[ICoreWebView2IsDocumentPlayingAudioChangedEventHandler,  # eventHandler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_IsDocumentPlayingAudioChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]
    get_IsDocumentPlayingAudio: _Callable[[_Pointer[_type.BOOL]],  # value
                                          _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_9(ICoreWebView2_8):
    add_IsDefaultDownloadDialogOpenChanged: _Callable[[ICoreWebView2IsDefaultDownloadDialogOpenChangedEventHandler,  # handler
                                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                                      _type.HRESULT]
    remove_IsDefaultDownloadDialogOpenChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                         _type.HRESULT]
    get_IsDefaultDownloadDialogOpen: _Callable[[_Pointer[_type.BOOL]],  # value
                                               _type.HRESULT]
    OpenDefaultDownloadDialog: _Callable[[],
                                         _type.HRESULT]
    CloseDefaultDownloadDialog: _Callable[[],
                                          _type.HRESULT]
    get_DefaultDownloadDialogCornerAlignment: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_DEFAULT_DOWNLOAD_DIALOG_CORNER_ALIGNMENT]],  # value
                                                        _type.HRESULT]
    put_DefaultDownloadDialogCornerAlignment: _Callable[[_enum_WebView2.COREWEBVIEW2_DEFAULT_DOWNLOAD_DIALOG_CORNER_ALIGNMENT],  # value
                                                        _type.HRESULT]
    get_DefaultDownloadDialogMargin: _Callable[[_Pointer[_struct.POINT]],  # value
                                               _type.HRESULT]
    put_DefaultDownloadDialogMargin: _Callable[[_struct.POINT],  # value
                                               _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_10(ICoreWebView2_9):
    add_BasicAuthenticationRequested: _Callable[[ICoreWebView2BasicAuthenticationRequestedEventHandler,  # eventHandler
                                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                                _type.HRESULT]
    remove_BasicAuthenticationRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                   _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_11(ICoreWebView2_10):
    CallDevToolsProtocolMethodForSession: _Callable[[_type.LPCWSTR,  # sessionId
                                                     _type.LPCWSTR,  # methodName
                                                     _type.LPCWSTR,  # parametersAsJson
                                                     ICoreWebView2CallDevToolsProtocolMethodCompletedHandler],  # handler
                                                    _type.HRESULT]
    add_ContextMenuRequested: _Callable[[ICoreWebView2ContextMenuRequestedEventHandler,  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_ContextMenuRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_12(ICoreWebView2_11):
    add_StatusBarTextChanged: _Callable[[ICoreWebView2StatusBarTextChangedEventHandler,  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_StatusBarTextChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    get_StatusBarText: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                 _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_13(ICoreWebView2_12):
    get_Profile: _Callable[[_Pointer[ICoreWebView2Profile]],  # value
                           _type.HRESULT]


class ICoreWebView2BasicAuthenticationRequestedEventArgs(_Unknwnbase.IUnknown):
    get_Uri: _Callable[[_Pointer[_type.LPWSTR]],  # value
                       _type.HRESULT]
    get_Challenge: _Callable[[_Pointer[_type.LPWSTR]],  # challenge
                             _type.HRESULT]
    get_Response: _Callable[[_Pointer[ICoreWebView2BasicAuthenticationResponse]],  # response
                            _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.BOOL]],  # cancel
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.BOOL],  # cancel
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]


class _ICoreWebView2BasicAuthenticationRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2BasicAuthenticationRequestedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2BasicAuthenticationRequestedEventHandler(_ICoreWebView2BasicAuthenticationRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2BasicAuthenticationRequestedEventHandler_impl(_ICoreWebView2BasicAuthenticationRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2BasicAuthenticationResponse(_Unknwnbase.IUnknown):
    get_UserName: _Callable[[_Pointer[_type.LPWSTR]],  # userName
                            _type.HRESULT]
    put_UserName: _Callable[[_type.LPCWSTR],  # userName
                            _type.HRESULT]
    get_Password: _Callable[[_Pointer[_type.LPWSTR]],  # password
                            _type.HRESULT]
    put_Password: _Callable[[_type.LPCWSTR],  # password
                            _type.HRESULT]


class ICoreWebView2BrowserProcessExitedEventArgs(_Unknwnbase.IUnknown):
    get_BrowserProcessExitKind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_BROWSER_PROCESS_EXIT_KIND]],  # browserProcessExitKind
                                          _type.HRESULT]
    get_BrowserProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                                    _type.HRESULT]


class _ICoreWebView2BrowserProcessExitedEventHandler:
    Invoke: _Callable[[ICoreWebView2Environment,  # sender
                       ICoreWebView2BrowserProcessExitedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2BrowserProcessExitedEventHandler(_ICoreWebView2BrowserProcessExitedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2BrowserProcessExitedEventHandler_impl(_ICoreWebView2BrowserProcessExitedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2BytesReceivedChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2DownloadOperation,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2BytesReceivedChangedEventHandler(_ICoreWebView2BytesReceivedChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2BytesReceivedChangedEventHandler_impl(_ICoreWebView2BytesReceivedChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2CompositionController(_Unknwnbase.IUnknown):
    get_RootVisualTarget: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # target
                                    _type.HRESULT]
    put_RootVisualTarget: _Callable[[_Unknwnbase.IUnknown],  # target
                                    _type.HRESULT]
    SendMouseInput: _Callable[[_enum_WebView2.COREWEBVIEW2_MOUSE_EVENT_KIND,  # eventKind
                               _enum_WebView2.COREWEBVIEW2_MOUSE_EVENT_VIRTUAL_KEYS,  # virtualKeys
                               _type.UINT32,  # mouseData
                               _struct.POINT],  # point
                              _type.HRESULT]
    SendPointerInput: _Callable[[_enum_WebView2.COREWEBVIEW2_POINTER_EVENT_KIND,  # eventKind
                                 ICoreWebView2PointerInfo],  # pointerInfo
                                _type.HRESULT]
    get_Cursor: _Callable[[_Pointer[_type.HCURSOR]],  # cursor
                          _type.HRESULT]
    get_SystemCursorId: _Callable[[_Pointer[_type.UINT32]],  # systemCursorId
                                  _type.HRESULT]
    add_CursorChanged: _Callable[[ICoreWebView2CursorChangedEventHandler,  # eventHandler
                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                 _type.HRESULT]
    remove_CursorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]


class ICoreWebView2CompositionController2(ICoreWebView2CompositionController):
    get_AutomationProvider: _Callable[[_Pointer[_Unknwnbase.IUnknown]],  # provider
                                      _type.HRESULT]


class ICoreWebView2CompositionController3(ICoreWebView2CompositionController2):
    DragEnter: _Callable[[_objidl.IDataObject,  # dataObject
                          _type.DWORD,  # keyState
                          _struct.POINT,  # point
                          _Pointer[_type.DWORD]],  # effect
                         _type.HRESULT]
    DragLeave: _Callable[[],
                         _type.HRESULT]
    DragOver: _Callable[[_type.DWORD,  # keyState
                         _struct.POINT,  # point
                         _Pointer[_type.DWORD]],  # effect
                        _type.HRESULT]
    Drop: _Callable[[_objidl.IDataObject,  # dataObject
                     _type.DWORD,  # keyState
                     _struct.POINT,  # point
                     _Pointer[_type.DWORD]],  # effect
                    _type.HRESULT]


class ICoreWebView2Controller(_Unknwnbase.IUnknown):
    get_IsVisible: _Callable[[_Pointer[_type.BOOL]],  # isVisible
                             _type.HRESULT]
    put_IsVisible: _Callable[[_type.BOOL],  # isVisible
                             _type.HRESULT]
    get_Bounds: _Callable[[_Pointer[_struct.RECT]],  # bounds
                          _type.HRESULT]
    put_Bounds: _Callable[[_struct.RECT],  # bounds
                          _type.HRESULT]
    get_ZoomFactor: _Callable[[_Pointer[_type.c_double]],  # zoomFactor
                              _type.HRESULT]
    put_ZoomFactor: _Callable[[_type.c_double],  # zoomFactor
                              _type.HRESULT]
    add_ZoomFactorChanged: _Callable[[ICoreWebView2ZoomFactorChangedEventHandler,  # eventHandler
                                      _Pointer[_struct.EventRegistrationToken]],  # token
                                     _type.HRESULT]
    remove_ZoomFactorChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                        _type.HRESULT]
    SetBoundsAndZoomFactor: _Callable[[_struct.RECT,  # bounds
                                       _type.c_double],  # zoomFactor
                                      _type.HRESULT]
    MoveFocus: _Callable[[_enum_WebView2.COREWEBVIEW2_MOVE_FOCUS_REASON],  # reason
                         _type.HRESULT]
    add_MoveFocusRequested: _Callable[[ICoreWebView2MoveFocusRequestedEventHandler,  # eventHandler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_MoveFocusRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_GotFocus: _Callable[[ICoreWebView2FocusChangedEventHandler,  # eventHandler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_LostFocus: _Callable[[ICoreWebView2FocusChangedEventHandler,  # eventHandler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    add_AcceleratorKeyPressed: _Callable[[ICoreWebView2AcceleratorKeyPressedEventHandler,  # eventHandler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_AcceleratorKeyPressed: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]
    get_ParentWindow: _Callable[[_Pointer[_type.HWND]],  # parentWindow
                                _type.HRESULT]
    put_ParentWindow: _Callable[[_type.HWND],  # parentWindow
                                _type.HRESULT]
    NotifyParentWindowPositionChanged: _Callable[[],
                                                 _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]
    get_CoreWebView2: _Callable[[_Pointer[ICoreWebView2]],  # coreWebView2
                                _type.HRESULT]


class ICoreWebView2Controller2(ICoreWebView2Controller):
    get_DefaultBackgroundColor: _Callable[[_Pointer[_struct.COREWEBVIEW2_COLOR]],  # backgroundColor
                                          _type.HRESULT]
    put_DefaultBackgroundColor: _Callable[[_struct.COREWEBVIEW2_COLOR],  # backgroundColor
                                          _type.HRESULT]


class ICoreWebView2Controller3(ICoreWebView2Controller2):
    get_RasterizationScale: _Callable[[_Pointer[_type.c_double]],  # scale
                                      _type.HRESULT]
    put_RasterizationScale: _Callable[[_type.c_double],  # scale
                                      _type.HRESULT]
    get_ShouldDetectMonitorScaleChanges: _Callable[[_Pointer[_type.BOOL]],  # value
                                                   _type.HRESULT]
    put_ShouldDetectMonitorScaleChanges: _Callable[[_type.BOOL],  # value
                                                   _type.HRESULT]
    add_RasterizationScaleChanged: _Callable[[ICoreWebView2RasterizationScaleChangedEventHandler,  # eventHandler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_RasterizationScaleChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    get_BoundsMode: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_BOUNDS_MODE]],  # boundsMode
                              _type.HRESULT]
    put_BoundsMode: _Callable[[_enum_WebView2.COREWEBVIEW2_BOUNDS_MODE],  # boundsMode
                              _type.HRESULT]


class ICoreWebView2Controller4(ICoreWebView2Controller3):
    get_AllowExternalDrop: _Callable[[_Pointer[_type.BOOL]],  # value
                                     _type.HRESULT]
    put_AllowExternalDrop: _Callable[[_type.BOOL],  # value
                                     _type.HRESULT]


class ICoreWebView2ControllerOptions(_Unknwnbase.IUnknown):
    get_ProfileName: _Callable[[_Pointer[_type.LPWSTR]],  # value
                               _type.HRESULT]
    put_ProfileName: _Callable[[_type.LPCWSTR],  # value
                               _type.HRESULT]
    get_IsInPrivateModeEnabled: _Callable[[_Pointer[_type.BOOL]],  # value
                                          _type.HRESULT]
    put_IsInPrivateModeEnabled: _Callable[[_type.BOOL],  # value
                                          _type.HRESULT]


class ICoreWebView2ContentLoadingEventArgs(_Unknwnbase.IUnknown):
    get_IsErrorPage: _Callable[[_Pointer[_type.BOOL]],  # isErrorPage
                               _type.HRESULT]
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # navigationId
                                _type.HRESULT]


class _ICoreWebView2ContentLoadingEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2ContentLoadingEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2ContentLoadingEventHandler(_ICoreWebView2ContentLoadingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ContentLoadingEventHandler_impl(_ICoreWebView2ContentLoadingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2ContextMenuRequestedEventArgs(_Unknwnbase.IUnknown):
    get_MenuItems: _Callable[[_Pointer[ICoreWebView2ContextMenuItemCollection]],  # value
                             _type.HRESULT]
    get_ContextMenuTarget: _Callable[[_Pointer[ICoreWebView2ContextMenuTarget]],  # value
                                     _type.HRESULT]
    get_Location: _Callable[[_Pointer[_struct.POINT]],  # value
                            _type.HRESULT]
    put_SelectedCommandId: _Callable[[_type.INT32],  # value
                                     _type.HRESULT]
    get_SelectedCommandId: _Callable[[_Pointer[_type.INT32]],  # value
                                     _type.HRESULT]
    put_Handled: _Callable[[_type.BOOL],  # value
                           _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.BOOL]],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]


class _ICoreWebView2ContextMenuRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2ContextMenuRequestedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2ContextMenuRequestedEventHandler(_ICoreWebView2ContextMenuRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ContextMenuRequestedEventHandler_impl(_ICoreWebView2ContextMenuRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2Cookie(_Unknwnbase.IUnknown):
    get_Name: _Callable[[_Pointer[_type.LPWSTR]],  # name
                        _type.HRESULT]
    get_Value: _Callable[[_Pointer[_type.LPWSTR]],  # value
                         _type.HRESULT]
    put_Value: _Callable[[_type.LPCWSTR],  # value
                         _type.HRESULT]
    get_Domain: _Callable[[_Pointer[_type.LPWSTR]],  # domain
                          _type.HRESULT]
    get_Path: _Callable[[_Pointer[_type.LPWSTR]],  # path
                        _type.HRESULT]
    get_Expires: _Callable[[_Pointer[_type.c_double]],  # expires
                           _type.HRESULT]
    put_Expires: _Callable[[_type.c_double],  # expires
                           _type.HRESULT]
    get_IsHttpOnly: _Callable[[_Pointer[_type.BOOL]],  # isHttpOnly
                              _type.HRESULT]
    put_IsHttpOnly: _Callable[[_type.BOOL],  # isHttpOnly
                              _type.HRESULT]
    get_SameSite: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_COOKIE_SAME_SITE_KIND]],  # sameSite
                            _type.HRESULT]
    put_SameSite: _Callable[[_enum_WebView2.COREWEBVIEW2_COOKIE_SAME_SITE_KIND],  # sameSite
                            _type.HRESULT]
    get_IsSecure: _Callable[[_Pointer[_type.BOOL]],  # isSecure
                            _type.HRESULT]
    put_IsSecure: _Callable[[_type.BOOL],  # isSecure
                            _type.HRESULT]
    get_IsSession: _Callable[[_Pointer[_type.BOOL]],  # isSession
                             _type.HRESULT]


class ICoreWebView2CookieList(_Unknwnbase.IUnknown):
    get_Count: _Callable[[_Pointer[_type.UINT]],  # count
                         _type.HRESULT]
    GetValueAtIndex: _Callable[[_type.UINT,  # index
                                _Pointer[ICoreWebView2Cookie]],  # cookie
                               _type.HRESULT]


class ICoreWebView2CookieManager(_Unknwnbase.IUnknown):
    CreateCookie: _Callable[[_type.LPCWSTR,  # name
                             _type.LPCWSTR,  # value
                             _type.LPCWSTR,  # domain
                             _type.LPCWSTR,  # path
                             _Pointer[ICoreWebView2Cookie]],  # cookie
                            _type.HRESULT]
    CopyCookie: _Callable[[ICoreWebView2Cookie,  # cookieParam
                           _Pointer[ICoreWebView2Cookie]],  # cookie
                          _type.HRESULT]
    GetCookies: _Callable[[_type.LPCWSTR,  # uri
                           ICoreWebView2GetCookiesCompletedHandler],  # handler
                          _type.HRESULT]
    AddOrUpdateCookie: _Callable[[ICoreWebView2Cookie],  # cookie
                                 _type.HRESULT]
    DeleteCookie: _Callable[[ICoreWebView2Cookie],  # cookie
                            _type.HRESULT]
    DeleteCookies: _Callable[[_type.LPCWSTR,  # name
                              _type.LPCWSTR],  # uri
                             _type.HRESULT]
    DeleteCookiesWithDomainAndPath: _Callable[[_type.LPCWSTR,  # name
                                               _type.LPCWSTR,  # domain
                                               _type.LPCWSTR],  # path
                                              _type.HRESULT]
    DeleteAllCookies: _Callable[[],
                                _type.HRESULT]


class ICoreWebView2Certificate(_Unknwnbase.IUnknown):
    get_Subject: _Callable[[_Pointer[_type.LPWSTR]],  # value
                           _type.HRESULT]
    get_Issuer: _Callable[[_Pointer[_type.LPWSTR]],  # value
                          _type.HRESULT]
    get_ValidFrom: _Callable[[_Pointer[_type.c_double]],  # value
                             _type.HRESULT]
    get_ValidTo: _Callable[[_Pointer[_type.c_double]],  # value
                           _type.HRESULT]
    get_DerEncodedSerialNumber: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                          _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.LPWSTR]],  # value
                               _type.HRESULT]
    ToPemEncoding: _Callable[[_Pointer[_type.LPWSTR]],  # pemEncodedData
                             _type.HRESULT]
    get_PemEncodedIssuerCertificateChain: _Callable[[_Pointer[ICoreWebView2StringCollection]],  # value
                                                    _type.HRESULT]


class ICoreWebView2ClientCertificate(_Unknwnbase.IUnknown):
    get_Subject: _Callable[[_Pointer[_type.LPWSTR]],  # value
                           _type.HRESULT]
    get_Issuer: _Callable[[_Pointer[_type.LPWSTR]],  # value
                          _type.HRESULT]
    get_ValidFrom: _Callable[[_Pointer[_type.c_double]],  # value
                             _type.HRESULT]
    get_ValidTo: _Callable[[_Pointer[_type.c_double]],  # value
                           _type.HRESULT]
    get_DerEncodedSerialNumber: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                          _type.HRESULT]
    get_DisplayName: _Callable[[_Pointer[_type.LPWSTR]],  # value
                               _type.HRESULT]
    ToPemEncoding: _Callable[[_Pointer[_type.LPWSTR]],  # pemEncodedData
                             _type.HRESULT]
    get_PemEncodedIssuerCertificateChain: _Callable[[_Pointer[ICoreWebView2StringCollection]],  # value
                                                    _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_CLIENT_CERTIFICATE_KIND]],  # value
                        _type.HRESULT]


class ICoreWebView2StringCollection(_Unknwnbase.IUnknown):
    get_Count: _Callable[[_Pointer[_type.UINT]],  # value
                         _type.HRESULT]
    GetValueAtIndex: _Callable[[_type.UINT,  # index
                                _Pointer[_type.LPWSTR]],  # value
                               _type.HRESULT]


class _ICoreWebView2ClearBrowsingDataCompletedHandler:
    Invoke: _Callable[[_type.HRESULT],  # errorCode
                      _type.HRESULT]


class ICoreWebView2ClearBrowsingDataCompletedHandler(_ICoreWebView2ClearBrowsingDataCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ClearBrowsingDataCompletedHandler_impl(_ICoreWebView2ClearBrowsingDataCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2ClientCertificateCollection(_Unknwnbase.IUnknown):
    get_Count: _Callable[[_Pointer[_type.UINT]],  # value
                         _type.HRESULT]
    GetValueAtIndex: _Callable[[_type.UINT,  # index
                                _Pointer[ICoreWebView2ClientCertificate]],  # certificate
                               _type.HRESULT]


class ICoreWebView2ClientCertificateRequestedEventArgs(_Unknwnbase.IUnknown):
    get_Host: _Callable[[_Pointer[_type.LPWSTR]],  # value
                        _type.HRESULT]
    get_Port: _Callable[[_Pointer[_type.c_int]],  # value
                        _type.HRESULT]
    get_IsProxy: _Callable[[_Pointer[_type.BOOL]],  # value
                           _type.HRESULT]
    get_AllowedCertificateAuthorities: _Callable[[_Pointer[ICoreWebView2StringCollection]],  # value
                                                 _type.HRESULT]
    get_MutuallyTrustedCertificates: _Callable[[_Pointer[ICoreWebView2ClientCertificateCollection]],  # value
                                               _type.HRESULT]
    get_SelectedCertificate: _Callable[[_Pointer[ICoreWebView2ClientCertificate]],  # value
                                       _type.HRESULT]
    put_SelectedCertificate: _Callable[[ICoreWebView2ClientCertificate],  # value
                                       _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.BOOL]],  # value
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.BOOL],  # value
                          _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.BOOL]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.BOOL],  # value
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]


class _ICoreWebView2ClientCertificateRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2ClientCertificateRequestedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2ClientCertificateRequestedEventHandler(_ICoreWebView2ClientCertificateRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ClientCertificateRequestedEventHandler_impl(_ICoreWebView2ClientCertificateRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2ContextMenuItem(_Unknwnbase.IUnknown):
    get_Name: _Callable[[_Pointer[_type.LPWSTR]],  # value
                        _type.HRESULT]
    get_Label: _Callable[[_Pointer[_type.LPWSTR]],  # value
                         _type.HRESULT]
    get_CommandId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_ShortcutKeyDescription: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                          _type.HRESULT]
    get_Icon: _Callable[[_Pointer[_objidlbase.IStream]],  # value
                        _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_CONTEXT_MENU_ITEM_KIND]],  # value
                        _type.HRESULT]
    put_IsEnabled: _Callable[[_type.BOOL],  # value
                             _type.HRESULT]
    get_IsEnabled: _Callable[[_Pointer[_type.BOOL]],  # value
                             _type.HRESULT]
    put_IsChecked: _Callable[[_type.BOOL],  # value
                             _type.HRESULT]
    get_IsChecked: _Callable[[_Pointer[_type.BOOL]],  # value
                             _type.HRESULT]
    get_Children: _Callable[[_Pointer[ICoreWebView2ContextMenuItemCollection]],  # value
                            _type.HRESULT]
    add_CustomItemSelected: _Callable[[ICoreWebView2CustomItemSelectedEventHandler,  # eventHandler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_CustomItemSelected: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class ICoreWebView2ContextMenuItemCollection(_Unknwnbase.IUnknown):
    get_Count: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    GetValueAtIndex: _Callable[[_type.UINT32,  # index
                                _Pointer[ICoreWebView2ContextMenuItem]],  # value
                               _type.HRESULT]
    RemoveValueAtIndex: _Callable[[_type.UINT32],  # index
                                  _type.HRESULT]
    InsertValueAtIndex: _Callable[[_type.UINT32,  # index
                                   ICoreWebView2ContextMenuItem],  # value
                                  _type.HRESULT]


class ICoreWebView2ContextMenuTarget(_Unknwnbase.IUnknown):
    get_Kind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_CONTEXT_MENU_TARGET_KIND]],  # value
                        _type.HRESULT]
    get_IsEditable: _Callable[[_Pointer[_type.BOOL]],  # value
                              _type.HRESULT]
    get_IsRequestedForMainFrame: _Callable[[_Pointer[_type.BOOL]],  # value
                                           _type.HRESULT]
    get_PageUri: _Callable[[_Pointer[_type.LPWSTR]],  # value
                           _type.HRESULT]
    get_FrameUri: _Callable[[_Pointer[_type.LPWSTR]],  # value
                            _type.HRESULT]
    get_HasLinkUri: _Callable[[_Pointer[_type.BOOL]],  # value
                              _type.HRESULT]
    get_LinkUri: _Callable[[_Pointer[_type.LPWSTR]],  # value
                           _type.HRESULT]
    get_HasLinkText: _Callable[[_Pointer[_type.BOOL]],  # value
                               _type.HRESULT]
    get_LinkText: _Callable[[_Pointer[_type.LPWSTR]],  # value
                            _type.HRESULT]
    get_HasSourceUri: _Callable[[_Pointer[_type.BOOL]],  # value
                                _type.HRESULT]
    get_SourceUri: _Callable[[_Pointer[_type.LPWSTR]],  # value
                             _type.HRESULT]
    get_HasSelection: _Callable[[_Pointer[_type.BOOL]],  # value
                                _type.HRESULT]
    get_SelectionText: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                 _type.HRESULT]


class _ICoreWebView2ClearServerCertificateErrorActionsCompletedHandler:
    Invoke: _Callable[[_type.HRESULT],  # errorCode
                      _type.HRESULT]


class ICoreWebView2ClearServerCertificateErrorActionsCompletedHandler(_ICoreWebView2ClearServerCertificateErrorActionsCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ClearServerCertificateErrorActionsCompletedHandler_impl(_ICoreWebView2ClearServerCertificateErrorActionsCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       ICoreWebView2CompositionController],  # webView
                      _type.HRESULT]


class ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler(_ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler_impl(_ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2CreateCoreWebView2ControllerCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       ICoreWebView2Controller],  # createdController
                      _type.HRESULT]


class ICoreWebView2CreateCoreWebView2ControllerCompletedHandler(_ICoreWebView2CreateCoreWebView2ControllerCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2CreateCoreWebView2ControllerCompletedHandler_impl(_ICoreWebView2CreateCoreWebView2ControllerCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       ICoreWebView2Environment],  # createdEnvironment
                      _type.HRESULT]


class ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler(_ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler_impl(_ICoreWebView2CreateCoreWebView2EnvironmentCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2ContainsFullScreenElementChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2ContainsFullScreenElementChangedEventHandler(_ICoreWebView2ContainsFullScreenElementChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ContainsFullScreenElementChangedEventHandler_impl(_ICoreWebView2ContainsFullScreenElementChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2CursorChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2CompositionController,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2CursorChangedEventHandler(_ICoreWebView2CursorChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2CursorChangedEventHandler_impl(_ICoreWebView2CursorChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2CustomItemSelectedEventHandler:
    Invoke: _Callable[[ICoreWebView2ContextMenuItem,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2CustomItemSelectedEventHandler(_ICoreWebView2CustomItemSelectedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2CustomItemSelectedEventHandler_impl(_ICoreWebView2CustomItemSelectedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2DocumentTitleChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2DocumentTitleChangedEventHandler(_ICoreWebView2DocumentTitleChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2DocumentTitleChangedEventHandler_impl(_ICoreWebView2DocumentTitleChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2DOMContentLoadedEventArgs(_Unknwnbase.IUnknown):
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # navigationId
                                _type.HRESULT]


class _ICoreWebView2DOMContentLoadedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2DOMContentLoadedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2DOMContentLoadedEventHandler(_ICoreWebView2DOMContentLoadedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2DOMContentLoadedEventHandler_impl(_ICoreWebView2DOMContentLoadedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2Deferral(_Unknwnbase.IUnknown):
    Complete: _Callable[[],
                        _type.HRESULT]


class ICoreWebView2DevToolsProtocolEventReceivedEventArgs(_Unknwnbase.IUnknown):
    get_ParameterObjectAsJson: _Callable[[_Pointer[_type.LPWSTR]],  # parameterObjectAsJson
                                         _type.HRESULT]


class ICoreWebView2DevToolsProtocolEventReceivedEventArgs2(ICoreWebView2DevToolsProtocolEventReceivedEventArgs):
    get_SessionId: _Callable[[_Pointer[_type.LPWSTR]],  # sessionId
                             _type.HRESULT]


class _ICoreWebView2DevToolsProtocolEventReceivedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2DevToolsProtocolEventReceivedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2DevToolsProtocolEventReceivedEventHandler(_ICoreWebView2DevToolsProtocolEventReceivedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2DevToolsProtocolEventReceivedEventHandler_impl(_ICoreWebView2DevToolsProtocolEventReceivedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2DevToolsProtocolEventReceiver(_Unknwnbase.IUnknown):
    add_DevToolsProtocolEventReceived: _Callable[[ICoreWebView2DevToolsProtocolEventReceivedEventHandler,  # handler
                                                  _Pointer[_struct.EventRegistrationToken]],  # token
                                                 _type.HRESULT]
    remove_DevToolsProtocolEventReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                                    _type.HRESULT]


class ICoreWebView2DownloadOperation(_Unknwnbase.IUnknown):
    add_BytesReceivedChanged: _Callable[[ICoreWebView2BytesReceivedChangedEventHandler,  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_BytesReceivedChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_EstimatedEndTimeChanged: _Callable[[ICoreWebView2EstimatedEndTimeChangedEventHandler,  # eventHandler
                                            _Pointer[_struct.EventRegistrationToken]],  # token
                                           _type.HRESULT]
    remove_EstimatedEndTimeChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                              _type.HRESULT]
    add_StateChanged: _Callable[[ICoreWebView2StateChangedEventHandler,  # eventHandler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]
    get_Uri: _Callable[[_Pointer[_type.LPWSTR]],  # uri
                       _type.HRESULT]
    get_ContentDisposition: _Callable[[_Pointer[_type.LPWSTR]],  # contentDisposition
                                      _type.HRESULT]
    get_MimeType: _Callable[[_Pointer[_type.LPWSTR]],  # mimeType
                            _type.HRESULT]
    get_TotalBytesToReceive: _Callable[[_Pointer[_type.INT64]],  # totalBytesToReceive
                                       _type.HRESULT]
    get_BytesReceived: _Callable[[_Pointer[_type.INT64]],  # bytesReceived
                                 _type.HRESULT]
    get_EstimatedEndTime: _Callable[[_Pointer[_type.LPWSTR]],  # estimatedEndTime
                                    _type.HRESULT]
    get_ResultFilePath: _Callable[[_Pointer[_type.LPWSTR]],  # resultFilePath
                                  _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_DOWNLOAD_STATE]],  # downloadState
                         _type.HRESULT]
    get_InterruptReason: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_DOWNLOAD_INTERRUPT_REASON]],  # interruptReason
                                   _type.HRESULT]
    Cancel: _Callable[[],
                      _type.HRESULT]
    Pause: _Callable[[],
                     _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    get_CanResume: _Callable[[_Pointer[_type.BOOL]],  # canResume
                             _type.HRESULT]


class ICoreWebView2DownloadStartingEventArgs(_Unknwnbase.IUnknown):
    get_DownloadOperation: _Callable[[_Pointer[ICoreWebView2DownloadOperation]],  # downloadOperation
                                     _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.BOOL]],  # cancel
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.BOOL],  # cancel
                          _type.HRESULT]
    get_ResultFilePath: _Callable[[_Pointer[_type.LPWSTR]],  # resultFilePath
                                  _type.HRESULT]
    put_ResultFilePath: _Callable[[_type.LPCWSTR],  # resultFilePath
                                  _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.BOOL]],  # handled
                           _type.HRESULT]
    put_Handled: _Callable[[_type.BOOL],  # handled
                           _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]


class _ICoreWebView2DownloadStartingEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2DownloadStartingEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2DownloadStartingEventHandler(_ICoreWebView2DownloadStartingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2DownloadStartingEventHandler_impl(_ICoreWebView2DownloadStartingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2Environment(_Unknwnbase.IUnknown):
    CreateCoreWebView2Controller: _Callable[[_type.HWND,  # parentWindow
                                             ICoreWebView2CreateCoreWebView2ControllerCompletedHandler],  # handler
                                            _type.HRESULT]
    CreateWebResourceResponse: _Callable[[_objidlbase.IStream,  # content
                                          _type.c_int,  # statusCode
                                          _type.LPCWSTR,  # reasonPhrase
                                          _type.LPCWSTR,  # headers
                                          _Pointer[ICoreWebView2WebResourceResponse]],  # response
                                         _type.HRESULT]
    get_BrowserVersionString: _Callable[[_Pointer[_type.LPWSTR]],  # versionInfo
                                        _type.HRESULT]
    add_NewBrowserVersionAvailable: _Callable[[ICoreWebView2NewBrowserVersionAvailableEventHandler,  # eventHandler
                                               _Pointer[_struct.EventRegistrationToken]],  # token
                                              _type.HRESULT]
    remove_NewBrowserVersionAvailable: _Callable[[_struct.EventRegistrationToken],  # token
                                                 _type.HRESULT]


class ICoreWebView2Environment2(ICoreWebView2Environment):
    CreateWebResourceRequest: _Callable[[_type.LPCWSTR,  # uri
                                         _type.LPCWSTR,  # method
                                         _objidlbase.IStream,  # postData
                                         _type.LPCWSTR,  # headers
                                         _Pointer[ICoreWebView2WebResourceRequest]],  # request
                                        _type.HRESULT]


class ICoreWebView2Environment3(ICoreWebView2Environment2):
    CreateCoreWebView2CompositionController: _Callable[[_type.HWND,  # parentWindow
                                                        ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler],  # handler
                                                       _type.HRESULT]
    CreateCoreWebView2PointerInfo: _Callable[[_Pointer[ICoreWebView2PointerInfo]],  # pointerInfo
                                             _type.HRESULT]


class ICoreWebView2Environment4(ICoreWebView2Environment3):
    GetAutomationProviderForWindow: _Callable[[_type.HWND,  # hwnd
                                               _Pointer[_Unknwnbase.IUnknown]],  # provider
                                              _type.HRESULT]


class ICoreWebView2Environment5(ICoreWebView2Environment4):
    add_BrowserProcessExited: _Callable[[ICoreWebView2BrowserProcessExitedEventHandler,  # eventHandler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_BrowserProcessExited: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]


class ICoreWebView2Environment6(ICoreWebView2Environment5):
    CreatePrintSettings: _Callable[[_Pointer[ICoreWebView2PrintSettings]],  # printSettings
                                   _type.HRESULT]


class ICoreWebView2Environment7(ICoreWebView2Environment6):
    get_UserDataFolder: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                  _type.HRESULT]


class ICoreWebView2Environment8(ICoreWebView2Environment7):
    add_ProcessInfosChanged: _Callable[[ICoreWebView2ProcessInfosChangedEventHandler,  # eventHandler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ProcessInfosChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    GetProcessInfos: _Callable[[_Pointer[ICoreWebView2ProcessInfoCollection]],  # value
                               _type.HRESULT]


class ICoreWebView2Environment9(ICoreWebView2Environment8):
    CreateContextMenuItem: _Callable[[_type.LPCWSTR,  # label
                                      _objidlbase.IStream,  # iconStream
                                      _enum_WebView2.COREWEBVIEW2_CONTEXT_MENU_ITEM_KIND,  # kind
                                      _Pointer[ICoreWebView2ContextMenuItem]],  # item
                                     _type.HRESULT]


class ICoreWebView2Environment10(ICoreWebView2Environment9):
    CreateCoreWebView2ControllerOptions: _Callable[[_Pointer[ICoreWebView2ControllerOptions]],  # options
                                                   _type.HRESULT]
    CreateCoreWebView2ControllerWithOptions: _Callable[[_type.HWND,  # parentWindow
                                                        ICoreWebView2ControllerOptions,  # options
                                                        ICoreWebView2CreateCoreWebView2ControllerCompletedHandler],  # handler
                                                       _type.HRESULT]
    CreateCoreWebView2CompositionControllerWithOptions: _Callable[[_type.HWND,  # parentWindow
                                                                   ICoreWebView2ControllerOptions,  # options
                                                                   ICoreWebView2CreateCoreWebView2CompositionControllerCompletedHandler],  # handler
                                                                  _type.HRESULT]


class ICoreWebView2EnvironmentOptions(_Unknwnbase.IUnknown):
    get_AdditionalBrowserArguments: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                              _type.HRESULT]
    put_AdditionalBrowserArguments: _Callable[[_type.LPCWSTR],  # value
                                              _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.LPWSTR]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.LPCWSTR],  # value
                            _type.HRESULT]
    get_TargetCompatibleBrowserVersion: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                                  _type.HRESULT]
    put_TargetCompatibleBrowserVersion: _Callable[[_type.LPCWSTR],  # value
                                                  _type.HRESULT]
    get_AllowSingleSignOnUsingOSPrimaryAccount: _Callable[[_Pointer[_type.BOOL]],  # allow
                                                          _type.HRESULT]
    put_AllowSingleSignOnUsingOSPrimaryAccount: _Callable[[_type.BOOL],  # allow
                                                          _type.HRESULT]


class ICoreWebView2EnvironmentOptions2(_Unknwnbase.IUnknown):
    get_ExclusiveUserDataFolderAccess: _Callable[[_Pointer[_type.BOOL]],  # value
                                                 _type.HRESULT]
    put_ExclusiveUserDataFolderAccess: _Callable[[_type.BOOL],  # value
                                                 _type.HRESULT]


class _ICoreWebView2EstimatedEndTimeChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2DownloadOperation,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2EstimatedEndTimeChangedEventHandler(_ICoreWebView2EstimatedEndTimeChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2EstimatedEndTimeChangedEventHandler_impl(_ICoreWebView2EstimatedEndTimeChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2ExecuteScriptCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       _type.LPCWSTR],  # resultObjectAsJson
                      _type.HRESULT]


class ICoreWebView2ExecuteScriptCompletedHandler(_ICoreWebView2ExecuteScriptCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ExecuteScriptCompletedHandler_impl(_ICoreWebView2ExecuteScriptCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2Frame(_Unknwnbase.IUnknown):
    get_Name: _Callable[[_Pointer[_type.LPWSTR]],  # name
                        _type.HRESULT]
    add_NameChanged: _Callable[[ICoreWebView2FrameNameChangedEventHandler,  # eventHandler
                                _Pointer[_struct.EventRegistrationToken]],  # token
                               _type.HRESULT]
    remove_NameChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                  _type.HRESULT]
    AddHostObjectToScriptWithOrigins: _Callable[[_type.LPCWSTR,  # name
                                                 _Pointer[_struct.VARIANT],  # object
                                                 _type.UINT32,  # originsCount
                                                 _Pointer[_type.LPCWSTR]],  # origins
                                                _type.HRESULT]
    RemoveHostObjectFromScript: _Callable[[_type.LPCWSTR],  # name
                                          _type.HRESULT]
    add_Destroyed: _Callable[[ICoreWebView2FrameDestroyedEventHandler,  # eventHandler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_Destroyed: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    IsDestroyed: _Callable[[_Pointer[_type.BOOL]],  # destroyed
                           _type.HRESULT]


class ICoreWebView2Frame2(ICoreWebView2Frame):
    add_NavigationStarting: _Callable[[ICoreWebView2FrameNavigationStartingEventHandler,  # eventHandler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_NavigationStarting: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]
    add_ContentLoading: _Callable[[ICoreWebView2FrameContentLoadingEventHandler,  # eventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_ContentLoading: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_NavigationCompleted: _Callable[[ICoreWebView2FrameNavigationCompletedEventHandler,  # eventHandler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_NavigationCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_DOMContentLoaded: _Callable[[ICoreWebView2FrameDOMContentLoadedEventHandler,  # eventHandler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_DOMContentLoaded: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    ExecuteScript: _Callable[[_type.LPCWSTR,  # javaScript
                              ICoreWebView2ExecuteScriptCompletedHandler],  # handler
                             _type.HRESULT]
    PostWebMessageAsJson: _Callable[[_type.LPCWSTR],  # webMessageAsJson
                                    _type.HRESULT]
    PostWebMessageAsString: _Callable[[_type.LPCWSTR],  # webMessageAsString
                                      _type.HRESULT]
    add_WebMessageReceived: _Callable[[ICoreWebView2FrameWebMessageReceivedEventHandler,  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # token
                                      _type.HRESULT]
    remove_WebMessageReceived: _Callable[[_struct.EventRegistrationToken],  # token
                                         _type.HRESULT]


class ICoreWebView2Frame3(ICoreWebView2Frame2):
    add_PermissionRequested: _Callable[[ICoreWebView2FramePermissionRequestedEventHandler,  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_PermissionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]


class _ICoreWebView2FrameContentLoadingEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       ICoreWebView2ContentLoadingEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2FrameContentLoadingEventHandler(_ICoreWebView2FrameContentLoadingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameContentLoadingEventHandler_impl(_ICoreWebView2FrameContentLoadingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2FrameCreatedEventArgs(_Unknwnbase.IUnknown):
    get_Frame: _Callable[[_Pointer[ICoreWebView2Frame]],  # frame
                         _type.HRESULT]


class _ICoreWebView2FrameCreatedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2FrameCreatedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2FrameCreatedEventHandler(_ICoreWebView2FrameCreatedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameCreatedEventHandler_impl(_ICoreWebView2FrameCreatedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FrameDestroyedEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2FrameDestroyedEventHandler(_ICoreWebView2FrameDestroyedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameDestroyedEventHandler_impl(_ICoreWebView2FrameDestroyedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FrameDOMContentLoadedEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       ICoreWebView2DOMContentLoadedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2FrameDOMContentLoadedEventHandler(_ICoreWebView2FrameDOMContentLoadedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameDOMContentLoadedEventHandler_impl(_ICoreWebView2FrameDOMContentLoadedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FrameNameChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2FrameNameChangedEventHandler(_ICoreWebView2FrameNameChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameNameChangedEventHandler_impl(_ICoreWebView2FrameNameChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FrameNavigationCompletedEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       ICoreWebView2NavigationCompletedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2FrameNavigationCompletedEventHandler(_ICoreWebView2FrameNavigationCompletedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameNavigationCompletedEventHandler_impl(_ICoreWebView2FrameNavigationCompletedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FrameNavigationStartingEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       ICoreWebView2NavigationStartingEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2FrameNavigationStartingEventHandler(_ICoreWebView2FrameNavigationStartingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameNavigationStartingEventHandler_impl(_ICoreWebView2FrameNavigationStartingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FramePermissionRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       ICoreWebView2PermissionRequestedEventArgs2],  # args
                      _type.HRESULT]


class ICoreWebView2FramePermissionRequestedEventHandler(_ICoreWebView2FramePermissionRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FramePermissionRequestedEventHandler_impl(_ICoreWebView2FramePermissionRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FrameWebMessageReceivedEventHandler:
    Invoke: _Callable[[ICoreWebView2Frame,  # sender
                       ICoreWebView2WebMessageReceivedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2FrameWebMessageReceivedEventHandler(_ICoreWebView2FrameWebMessageReceivedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FrameWebMessageReceivedEventHandler_impl(_ICoreWebView2FrameWebMessageReceivedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2FrameInfo(_Unknwnbase.IUnknown):
    get_Name: _Callable[[_Pointer[_type.LPWSTR]],  # name
                        _type.HRESULT]
    get_Source: _Callable[[_Pointer[_type.LPWSTR]],  # source
                          _type.HRESULT]


class ICoreWebView2FrameInfoCollection(_Unknwnbase.IUnknown):
    GetIterator: _Callable[[_Pointer[ICoreWebView2FrameInfoCollectionIterator]],  # iterator
                           _type.HRESULT]


class ICoreWebView2FrameInfoCollectionIterator(_Unknwnbase.IUnknown):
    get_HasCurrent: _Callable[[_Pointer[_type.BOOL]],  # hasCurrent
                              _type.HRESULT]
    GetCurrent: _Callable[[_Pointer[ICoreWebView2FrameInfo]],  # frameInfo
                          _type.HRESULT]
    MoveNext: _Callable[[_Pointer[_type.BOOL]],  # hasNext
                        _type.HRESULT]


class _ICoreWebView2FocusChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2Controller,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2FocusChangedEventHandler(_ICoreWebView2FocusChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FocusChangedEventHandler_impl(_ICoreWebView2FocusChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2GetCookiesCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # result
                       ICoreWebView2CookieList],  # cookieList
                      _type.HRESULT]


class ICoreWebView2GetCookiesCompletedHandler(_ICoreWebView2GetCookiesCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2GetCookiesCompletedHandler_impl(_ICoreWebView2GetCookiesCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2HistoryChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2HistoryChangedEventHandler(_ICoreWebView2HistoryChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2HistoryChangedEventHandler_impl(_ICoreWebView2HistoryChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2HttpHeadersCollectionIterator(_Unknwnbase.IUnknown):
    GetCurrentHeader: _Callable[[_Pointer[_type.LPWSTR],  # name
                                 _Pointer[_type.LPWSTR]],  # value
                                _type.HRESULT]
    get_HasCurrentHeader: _Callable[[_Pointer[_type.BOOL]],  # hasCurrent
                                    _type.HRESULT]
    MoveNext: _Callable[[_Pointer[_type.BOOL]],  # hasNext
                        _type.HRESULT]


class ICoreWebView2HttpRequestHeaders(_Unknwnbase.IUnknown):
    GetHeader: _Callable[[_type.LPCWSTR,  # name
                          _Pointer[_type.LPWSTR]],  # value
                         _type.HRESULT]
    GetHeaders: _Callable[[_type.LPCWSTR,  # name
                           _Pointer[ICoreWebView2HttpHeadersCollectionIterator]],  # iterator
                          _type.HRESULT]
    Contains: _Callable[[_type.LPCWSTR,  # name
                         _Pointer[_type.BOOL]],  # contains
                        _type.HRESULT]
    SetHeader: _Callable[[_type.LPCWSTR,  # name
                          _type.LPCWSTR],  # value
                         _type.HRESULT]
    RemoveHeader: _Callable[[_type.LPCWSTR],  # name
                            _type.HRESULT]
    GetIterator: _Callable[[_Pointer[ICoreWebView2HttpHeadersCollectionIterator]],  # iterator
                           _type.HRESULT]


class ICoreWebView2HttpResponseHeaders(_Unknwnbase.IUnknown):
    AppendHeader: _Callable[[_type.LPCWSTR,  # name
                             _type.LPCWSTR],  # value
                            _type.HRESULT]
    Contains: _Callable[[_type.LPCWSTR,  # name
                         _Pointer[_type.BOOL]],  # contains
                        _type.HRESULT]
    GetHeader: _Callable[[_type.LPCWSTR,  # name
                          _Pointer[_type.LPWSTR]],  # value
                         _type.HRESULT]
    GetHeaders: _Callable[[_type.LPCWSTR,  # name
                           _Pointer[ICoreWebView2HttpHeadersCollectionIterator]],  # iterator
                          _type.HRESULT]
    GetIterator: _Callable[[_Pointer[ICoreWebView2HttpHeadersCollectionIterator]],  # iterator
                           _type.HRESULT]


class _ICoreWebView2IsDefaultDownloadDialogOpenChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2IsDefaultDownloadDialogOpenChangedEventHandler(_ICoreWebView2IsDefaultDownloadDialogOpenChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2IsDefaultDownloadDialogOpenChangedEventHandler_impl(_ICoreWebView2IsDefaultDownloadDialogOpenChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2MoveFocusRequestedEventArgs(_Unknwnbase.IUnknown):
    get_Reason: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_MOVE_FOCUS_REASON]],  # reason
                          _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.BOOL]],  # value
                           _type.HRESULT]
    put_Handled: _Callable[[_type.BOOL],  # value
                           _type.HRESULT]


class _ICoreWebView2MoveFocusRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2Controller,  # sender
                       ICoreWebView2MoveFocusRequestedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2MoveFocusRequestedEventHandler(_ICoreWebView2MoveFocusRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2MoveFocusRequestedEventHandler_impl(_ICoreWebView2MoveFocusRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2NavigationCompletedEventArgs(_Unknwnbase.IUnknown):
    get_IsSuccess: _Callable[[_Pointer[_type.BOOL]],  # isSuccess
                             _type.HRESULT]
    get_WebErrorStatus: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_WEB_ERROR_STATUS]],  # webErrorStatus
                                  _type.HRESULT]
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # navigationId
                                _type.HRESULT]


class ICoreWebView2NavigationCompletedEventArgs2(ICoreWebView2NavigationCompletedEventArgs):
    get_HttpStatusCode: _Callable[[_Pointer[_type.c_int]],  # http_status_code
                                  _type.HRESULT]


class _ICoreWebView2NavigationCompletedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2NavigationCompletedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2NavigationCompletedEventHandler(_ICoreWebView2NavigationCompletedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2NavigationCompletedEventHandler_impl(_ICoreWebView2NavigationCompletedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2NavigationStartingEventArgs(_Unknwnbase.IUnknown):
    get_Uri: _Callable[[_Pointer[_type.LPWSTR]],  # uri
                       _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.BOOL]],  # isUserInitiated
                                   _type.HRESULT]
    get_IsRedirected: _Callable[[_Pointer[_type.BOOL]],  # isRedirected
                                _type.HRESULT]
    get_RequestHeaders: _Callable[[_Pointer[ICoreWebView2HttpRequestHeaders]],  # requestHeaders
                                  _type.HRESULT]
    get_Cancel: _Callable[[_Pointer[_type.BOOL]],  # cancel
                          _type.HRESULT]
    put_Cancel: _Callable[[_type.BOOL],  # cancel
                          _type.HRESULT]
    get_NavigationId: _Callable[[_Pointer[_type.UINT64]],  # navigationId
                                _type.HRESULT]


class ICoreWebView2NavigationStartingEventArgs2(ICoreWebView2NavigationStartingEventArgs):
    get_AdditionalAllowedFrameAncestors: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                                   _type.HRESULT]
    put_AdditionalAllowedFrameAncestors: _Callable[[_type.LPCWSTR],  # value
                                                   _type.HRESULT]


class _ICoreWebView2NavigationStartingEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2NavigationStartingEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2NavigationStartingEventHandler(_ICoreWebView2NavigationStartingEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2NavigationStartingEventHandler_impl(_ICoreWebView2NavigationStartingEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2NewBrowserVersionAvailableEventHandler:
    Invoke: _Callable[[ICoreWebView2Environment,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2NewBrowserVersionAvailableEventHandler(_ICoreWebView2NewBrowserVersionAvailableEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2NewBrowserVersionAvailableEventHandler_impl(_ICoreWebView2NewBrowserVersionAvailableEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2NewWindowRequestedEventArgs(_Unknwnbase.IUnknown):
    get_Uri: _Callable[[_Pointer[_type.LPWSTR]],  # uri
                       _type.HRESULT]
    put_NewWindow: _Callable[[ICoreWebView2],  # newWindow
                             _type.HRESULT]
    get_NewWindow: _Callable[[_Pointer[ICoreWebView2]],  # newWindow
                             _type.HRESULT]
    put_Handled: _Callable[[_type.BOOL],  # handled
                           _type.HRESULT]
    get_Handled: _Callable[[_Pointer[_type.BOOL]],  # handled
                           _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.BOOL]],  # isUserInitiated
                                   _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]
    get_WindowFeatures: _Callable[[_Pointer[ICoreWebView2WindowFeatures]],  # value
                                  _type.HRESULT]


class ICoreWebView2NewWindowRequestedEventArgs2(ICoreWebView2NewWindowRequestedEventArgs):
    get_Name: _Callable[[_Pointer[_type.LPWSTR]],  # value
                        _type.HRESULT]


class _ICoreWebView2NewWindowRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2NewWindowRequestedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2NewWindowRequestedEventHandler(_ICoreWebView2NewWindowRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2NewWindowRequestedEventHandler_impl(_ICoreWebView2NewWindowRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2PermissionRequestedEventArgs(_Unknwnbase.IUnknown):
    get_Uri: _Callable[[_Pointer[_type.LPWSTR]],  # uri
                       _type.HRESULT]
    get_PermissionKind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PERMISSION_KIND]],  # permissionKind
                                  _type.HRESULT]
    get_IsUserInitiated: _Callable[[_Pointer[_type.BOOL]],  # isUserInitiated
                                   _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PERMISSION_STATE]],  # state
                         _type.HRESULT]
    put_State: _Callable[[_enum_WebView2.COREWEBVIEW2_PERMISSION_STATE],  # state
                         _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]


class ICoreWebView2PermissionRequestedEventArgs2(ICoreWebView2PermissionRequestedEventArgs):
    get_Handled: _Callable[[_Pointer[_type.BOOL]],  # handled
                           _type.HRESULT]
    put_Handled: _Callable[[_type.BOOL],  # handled
                           _type.HRESULT]


class _ICoreWebView2PermissionRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2PermissionRequestedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2PermissionRequestedEventHandler(_ICoreWebView2PermissionRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2PermissionRequestedEventHandler_impl(_ICoreWebView2PermissionRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2PointerInfo(_Unknwnbase.IUnknown):
    get_PointerKind: _Callable[[_Pointer[_type.DWORD]],  # pointerKind
                               _type.HRESULT]
    put_PointerKind: _Callable[[_type.DWORD],  # pointerKind
                               _type.HRESULT]
    get_PointerId: _Callable[[_Pointer[_type.UINT32]],  # pointerId
                             _type.HRESULT]
    put_PointerId: _Callable[[_type.UINT32],  # pointerId
                             _type.HRESULT]
    get_FrameId: _Callable[[_Pointer[_type.UINT32]],  # frameId
                           _type.HRESULT]
    put_FrameId: _Callable[[_type.UINT32],  # frameId
                           _type.HRESULT]
    get_PointerFlags: _Callable[[_Pointer[_type.UINT32]],  # pointerFlags
                                _type.HRESULT]
    put_PointerFlags: _Callable[[_type.UINT32],  # pointerFlags
                                _type.HRESULT]
    get_PointerDeviceRect: _Callable[[_Pointer[_struct.RECT]],  # pointerDeviceRect
                                     _type.HRESULT]
    put_PointerDeviceRect: _Callable[[_struct.RECT],  # pointerDeviceRect
                                     _type.HRESULT]
    get_DisplayRect: _Callable[[_Pointer[_struct.RECT]],  # displayRect
                               _type.HRESULT]
    put_DisplayRect: _Callable[[_struct.RECT],  # displayRect
                               _type.HRESULT]
    get_PixelLocation: _Callable[[_Pointer[_struct.POINT]],  # pixelLocation
                                 _type.HRESULT]
    put_PixelLocation: _Callable[[_struct.POINT],  # pixelLocation
                                 _type.HRESULT]
    get_HimetricLocation: _Callable[[_Pointer[_struct.POINT]],  # himetricLocation
                                    _type.HRESULT]
    put_HimetricLocation: _Callable[[_struct.POINT],  # himetricLocation
                                    _type.HRESULT]
    get_PixelLocationRaw: _Callable[[_Pointer[_struct.POINT]],  # pixelLocationRaw
                                    _type.HRESULT]
    put_PixelLocationRaw: _Callable[[_struct.POINT],  # pixelLocationRaw
                                    _type.HRESULT]
    get_HimetricLocationRaw: _Callable[[_Pointer[_struct.POINT]],  # himetricLocationRaw
                                       _type.HRESULT]
    put_HimetricLocationRaw: _Callable[[_struct.POINT],  # himetricLocationRaw
                                       _type.HRESULT]
    get_Time: _Callable[[_Pointer[_type.DWORD]],  # time
                        _type.HRESULT]
    put_Time: _Callable[[_type.DWORD],  # time
                        _type.HRESULT]
    get_HistoryCount: _Callable[[_Pointer[_type.UINT32]],  # historyCount
                                _type.HRESULT]
    put_HistoryCount: _Callable[[_type.UINT32],  # historyCount
                                _type.HRESULT]
    get_InputData: _Callable[[_Pointer[_type.INT32]],  # inputData
                             _type.HRESULT]
    put_InputData: _Callable[[_type.INT32],  # inputData
                             _type.HRESULT]
    get_KeyStates: _Callable[[_Pointer[_type.DWORD]],  # keyStates
                             _type.HRESULT]
    put_KeyStates: _Callable[[_type.DWORD],  # keyStates
                             _type.HRESULT]
    get_PerformanceCount: _Callable[[_Pointer[_type.UINT64]],  # performanceCount
                                    _type.HRESULT]
    put_PerformanceCount: _Callable[[_type.UINT64],  # performanceCount
                                    _type.HRESULT]
    get_ButtonChangeKind: _Callable[[_Pointer[_type.INT32]],  # buttonChangeKind
                                    _type.HRESULT]
    put_ButtonChangeKind: _Callable[[_type.INT32],  # buttonChangeKind
                                    _type.HRESULT]
    get_PenFlags: _Callable[[_Pointer[_type.UINT32]],  # penFLags
                            _type.HRESULT]
    put_PenFlags: _Callable[[_type.UINT32],  # penFLags
                            _type.HRESULT]
    get_PenMask: _Callable[[_Pointer[_type.UINT32]],  # penMask
                           _type.HRESULT]
    put_PenMask: _Callable[[_type.UINT32],  # penMask
                           _type.HRESULT]
    get_PenPressure: _Callable[[_Pointer[_type.UINT32]],  # penPressure
                               _type.HRESULT]
    put_PenPressure: _Callable[[_type.UINT32],  # penPressure
                               _type.HRESULT]
    get_PenRotation: _Callable[[_Pointer[_type.UINT32]],  # penRotation
                               _type.HRESULT]
    put_PenRotation: _Callable[[_type.UINT32],  # penRotation
                               _type.HRESULT]
    get_PenTiltX: _Callable[[_Pointer[_type.INT32]],  # penTiltX
                            _type.HRESULT]
    put_PenTiltX: _Callable[[_type.INT32],  # penTiltX
                            _type.HRESULT]
    get_PenTiltY: _Callable[[_Pointer[_type.INT32]],  # penTiltY
                            _type.HRESULT]
    put_PenTiltY: _Callable[[_type.INT32],  # penTiltY
                            _type.HRESULT]
    get_TouchFlags: _Callable[[_Pointer[_type.UINT32]],  # touchFlags
                              _type.HRESULT]
    put_TouchFlags: _Callable[[_type.UINT32],  # touchFlags
                              _type.HRESULT]
    get_TouchMask: _Callable[[_Pointer[_type.UINT32]],  # touchMask
                             _type.HRESULT]
    put_TouchMask: _Callable[[_type.UINT32],  # touchMask
                             _type.HRESULT]
    get_TouchContact: _Callable[[_Pointer[_struct.RECT]],  # touchContact
                                _type.HRESULT]
    put_TouchContact: _Callable[[_struct.RECT],  # touchContact
                                _type.HRESULT]
    get_TouchContactRaw: _Callable[[_Pointer[_struct.RECT]],  # touchContactRaw
                                   _type.HRESULT]
    put_TouchContactRaw: _Callable[[_struct.RECT],  # touchContactRaw
                                   _type.HRESULT]
    get_TouchOrientation: _Callable[[_Pointer[_type.UINT32]],  # touchOrientation
                                    _type.HRESULT]
    put_TouchOrientation: _Callable[[_type.UINT32],  # touchOrientation
                                    _type.HRESULT]
    get_TouchPressure: _Callable[[_Pointer[_type.UINT32]],  # touchPressure
                                 _type.HRESULT]
    put_TouchPressure: _Callable[[_type.UINT32],  # touchPressure
                                 _type.HRESULT]


class ICoreWebView2PrintSettings(_Unknwnbase.IUnknown):
    get_Orientation: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PRINT_ORIENTATION]],  # orientation
                               _type.HRESULT]
    put_Orientation: _Callable[[_enum_WebView2.COREWEBVIEW2_PRINT_ORIENTATION],  # orientation
                               _type.HRESULT]
    get_ScaleFactor: _Callable[[_Pointer[_type.c_double]],  # scaleFactor
                               _type.HRESULT]
    put_ScaleFactor: _Callable[[_type.c_double],  # scaleFactor
                               _type.HRESULT]
    get_PageWidth: _Callable[[_Pointer[_type.c_double]],  # pageWidth
                             _type.HRESULT]
    put_PageWidth: _Callable[[_type.c_double],  # pageWidth
                             _type.HRESULT]
    get_PageHeight: _Callable[[_Pointer[_type.c_double]],  # pageHeight
                              _type.HRESULT]
    put_PageHeight: _Callable[[_type.c_double],  # pageHeight
                              _type.HRESULT]
    get_MarginTop: _Callable[[_Pointer[_type.c_double]],  # marginTop
                             _type.HRESULT]
    put_MarginTop: _Callable[[_type.c_double],  # marginTop
                             _type.HRESULT]
    get_MarginBottom: _Callable[[_Pointer[_type.c_double]],  # marginBottom
                                _type.HRESULT]
    put_MarginBottom: _Callable[[_type.c_double],  # marginBottom
                                _type.HRESULT]
    get_MarginLeft: _Callable[[_Pointer[_type.c_double]],  # marginLeft
                              _type.HRESULT]
    put_MarginLeft: _Callable[[_type.c_double],  # marginLeft
                              _type.HRESULT]
    get_MarginRight: _Callable[[_Pointer[_type.c_double]],  # marginRight
                               _type.HRESULT]
    put_MarginRight: _Callable[[_type.c_double],  # marginRight
                               _type.HRESULT]
    get_ShouldPrintBackgrounds: _Callable[[_Pointer[_type.BOOL]],  # shouldPrintBackgrounds
                                          _type.HRESULT]
    put_ShouldPrintBackgrounds: _Callable[[_type.BOOL],  # shouldPrintBackgrounds
                                          _type.HRESULT]
    get_ShouldPrintSelectionOnly: _Callable[[_Pointer[_type.BOOL]],  # shouldPrintSelectionOnly
                                            _type.HRESULT]
    put_ShouldPrintSelectionOnly: _Callable[[_type.BOOL],  # shouldPrintSelectionOnly
                                            _type.HRESULT]
    get_ShouldPrintHeaderAndFooter: _Callable[[_Pointer[_type.BOOL]],  # shouldPrintHeaderAndFooter
                                              _type.HRESULT]
    put_ShouldPrintHeaderAndFooter: _Callable[[_type.BOOL],  # shouldPrintHeaderAndFooter
                                              _type.HRESULT]
    get_HeaderTitle: _Callable[[_Pointer[_type.LPWSTR]],  # headerTitle
                               _type.HRESULT]
    put_HeaderTitle: _Callable[[_type.LPCWSTR],  # headerTitle
                               _type.HRESULT]
    get_FooterUri: _Callable[[_Pointer[_type.LPWSTR]],  # footerUri
                             _type.HRESULT]
    put_FooterUri: _Callable[[_type.LPCWSTR],  # footerUri
                             _type.HRESULT]


class _ICoreWebView2PrintToPdfCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       _type.BOOL],  # isSuccessful
                      _type.HRESULT]


class ICoreWebView2PrintToPdfCompletedHandler(_ICoreWebView2PrintToPdfCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2PrintToPdfCompletedHandler_impl(_ICoreWebView2PrintToPdfCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2ProcessFailedEventArgs(_Unknwnbase.IUnknown):
    get_ProcessFailedKind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PROCESS_FAILED_KIND]],  # processFailedKind
                                     _type.HRESULT]


class ICoreWebView2ProcessFailedEventArgs2(ICoreWebView2ProcessFailedEventArgs):
    get_Reason: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PROCESS_FAILED_REASON]],  # reason
                          _type.HRESULT]
    get_ExitCode: _Callable[[_Pointer[_type.c_int]],  # exitCode
                            _type.HRESULT]
    get_ProcessDescription: _Callable[[_Pointer[_type.LPWSTR]],  # processDescription
                                      _type.HRESULT]
    get_FrameInfosForFailedProcess: _Callable[[_Pointer[ICoreWebView2FrameInfoCollection]],  # frames
                                              _type.HRESULT]


class _ICoreWebView2ProcessFailedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2ProcessFailedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2ProcessFailedEventHandler(_ICoreWebView2ProcessFailedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ProcessFailedEventHandler_impl(_ICoreWebView2ProcessFailedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2Profile(_Unknwnbase.IUnknown):
    get_ProfileName: _Callable[[_Pointer[_type.LPWSTR]],  # value
                               _type.HRESULT]
    get_IsInPrivateModeEnabled: _Callable[[_Pointer[_type.BOOL]],  # value
                                          _type.HRESULT]
    get_ProfilePath: _Callable[[_Pointer[_type.LPWSTR]],  # value
                               _type.HRESULT]
    get_DefaultDownloadFolderPath: _Callable[[_Pointer[_type.LPWSTR]],  # value
                                             _type.HRESULT]
    put_DefaultDownloadFolderPath: _Callable[[_type.LPCWSTR],  # value
                                             _type.HRESULT]
    get_PreferredColorScheme: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PREFERRED_COLOR_SCHEME]],  # value
                                        _type.HRESULT]
    put_PreferredColorScheme: _Callable[[_enum_WebView2.COREWEBVIEW2_PREFERRED_COLOR_SCHEME],  # value
                                        _type.HRESULT]


class ICoreWebView2Profile2(ICoreWebView2Profile):
    ClearBrowsingData: _Callable[[_enum_WebView2.COREWEBVIEW2_BROWSING_DATA_KINDS,  # dataKinds
                                  ICoreWebView2ClearBrowsingDataCompletedHandler],  # handler
                                 _type.HRESULT]
    ClearBrowsingDataInTimeRange: _Callable[[_enum_WebView2.COREWEBVIEW2_BROWSING_DATA_KINDS,  # dataKinds
                                             _type.c_double,  # startTime
                                             _type.c_double,  # endTime
                                             ICoreWebView2ClearBrowsingDataCompletedHandler],  # handler
                                            _type.HRESULT]
    ClearBrowsingDataAll: _Callable[[ICoreWebView2ClearBrowsingDataCompletedHandler],  # handler
                                    _type.HRESULT]


class _ICoreWebView2RasterizationScaleChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2Controller,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2RasterizationScaleChangedEventHandler(_ICoreWebView2RasterizationScaleChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2RasterizationScaleChangedEventHandler_impl(_ICoreWebView2RasterizationScaleChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2ServerCertificateErrorDetectedEventArgs(_Unknwnbase.IUnknown):
    get_ErrorStatus: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_WEB_ERROR_STATUS]],  # value
                               _type.HRESULT]
    get_RequestUri: _Callable[[_Pointer[_type.LPWSTR]],  # value
                              _type.HRESULT]
    get_ServerCertificate: _Callable[[_Pointer[ICoreWebView2Certificate]],  # value
                                     _type.HRESULT]
    get_Action: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_SERVER_CERTIFICATE_ERROR_ACTION]],  # value
                          _type.HRESULT]
    put_Action: _Callable[[_enum_WebView2.COREWEBVIEW2_SERVER_CERTIFICATE_ERROR_ACTION],  # value
                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]


class _ICoreWebView2ServerCertificateErrorDetectedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2ServerCertificateErrorDetectedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2ServerCertificateErrorDetectedEventHandler(_ICoreWebView2ServerCertificateErrorDetectedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ServerCertificateErrorDetectedEventHandler_impl(_ICoreWebView2ServerCertificateErrorDetectedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2ScriptDialogOpeningEventArgs(_Unknwnbase.IUnknown):
    get_Uri: _Callable[[_Pointer[_type.LPWSTR]],  # uri
                       _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_SCRIPT_DIALOG_KIND]],  # kind
                        _type.HRESULT]
    get_Message: _Callable[[_Pointer[_type.LPWSTR]],  # message
                           _type.HRESULT]
    Accept: _Callable[[],
                      _type.HRESULT]
    get_DefaultText: _Callable[[_Pointer[_type.LPWSTR]],  # defaultText
                               _type.HRESULT]
    get_ResultText: _Callable[[_Pointer[_type.LPWSTR]],  # resultText
                              _type.HRESULT]
    put_ResultText: _Callable[[_type.LPCWSTR],  # resultText
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]


class _ICoreWebView2ScriptDialogOpeningEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2ScriptDialogOpeningEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2ScriptDialogOpeningEventHandler(_ICoreWebView2ScriptDialogOpeningEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ScriptDialogOpeningEventHandler_impl(_ICoreWebView2ScriptDialogOpeningEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2Settings(_Unknwnbase.IUnknown):
    get_IsScriptEnabled: _Callable[[_Pointer[_type.BOOL]],  # isScriptEnabled
                                   _type.HRESULT]
    put_IsScriptEnabled: _Callable[[_type.BOOL],  # isScriptEnabled
                                   _type.HRESULT]
    get_IsWebMessageEnabled: _Callable[[_Pointer[_type.BOOL]],  # isWebMessageEnabled
                                       _type.HRESULT]
    put_IsWebMessageEnabled: _Callable[[_type.BOOL],  # isWebMessageEnabled
                                       _type.HRESULT]
    get_AreDefaultScriptDialogsEnabled: _Callable[[_Pointer[_type.BOOL]],  # areDefaultScriptDialogsEnabled
                                                  _type.HRESULT]
    put_AreDefaultScriptDialogsEnabled: _Callable[[_type.BOOL],  # areDefaultScriptDialogsEnabled
                                                  _type.HRESULT]
    get_IsStatusBarEnabled: _Callable[[_Pointer[_type.BOOL]],  # isStatusBarEnabled
                                      _type.HRESULT]
    put_IsStatusBarEnabled: _Callable[[_type.BOOL],  # isStatusBarEnabled
                                      _type.HRESULT]
    get_AreDevToolsEnabled: _Callable[[_Pointer[_type.BOOL]],  # areDevToolsEnabled
                                      _type.HRESULT]
    put_AreDevToolsEnabled: _Callable[[_type.BOOL],  # areDevToolsEnabled
                                      _type.HRESULT]
    get_AreDefaultContextMenusEnabled: _Callable[[_Pointer[_type.BOOL]],  # enabled
                                                 _type.HRESULT]
    put_AreDefaultContextMenusEnabled: _Callable[[_type.BOOL],  # enabled
                                                 _type.HRESULT]
    get_AreHostObjectsAllowed: _Callable[[_Pointer[_type.BOOL]],  # allowed
                                         _type.HRESULT]
    put_AreHostObjectsAllowed: _Callable[[_type.BOOL],  # allowed
                                         _type.HRESULT]
    get_IsZoomControlEnabled: _Callable[[_Pointer[_type.BOOL]],  # enabled
                                        _type.HRESULT]
    put_IsZoomControlEnabled: _Callable[[_type.BOOL],  # enabled
                                        _type.HRESULT]
    get_IsBuiltInErrorPageEnabled: _Callable[[_Pointer[_type.BOOL]],  # enabled
                                             _type.HRESULT]
    put_IsBuiltInErrorPageEnabled: _Callable[[_type.BOOL],  # enabled
                                             _type.HRESULT]


class ICoreWebView2Settings2(ICoreWebView2Settings):
    get_UserAgent: _Callable[[_Pointer[_type.LPWSTR]],  # userAgent
                             _type.HRESULT]
    put_UserAgent: _Callable[[_type.LPCWSTR],  # userAgent
                             _type.HRESULT]


class ICoreWebView2Settings3(ICoreWebView2Settings2):
    get_AreBrowserAcceleratorKeysEnabled: _Callable[[_Pointer[_type.BOOL]],  # areBrowserAcceleratorKeysEnabled
                                                    _type.HRESULT]
    put_AreBrowserAcceleratorKeysEnabled: _Callable[[_type.BOOL],  # areBrowserAcceleratorKeysEnabled
                                                    _type.HRESULT]


class ICoreWebView2Settings4(ICoreWebView2Settings3):
    get_IsPasswordAutosaveEnabled: _Callable[[_Pointer[_type.BOOL]],  # value
                                             _type.HRESULT]
    put_IsPasswordAutosaveEnabled: _Callable[[_type.BOOL],  # value
                                             _type.HRESULT]
    get_IsGeneralAutofillEnabled: _Callable[[_Pointer[_type.BOOL]],  # value
                                            _type.HRESULT]
    put_IsGeneralAutofillEnabled: _Callable[[_type.BOOL],  # value
                                            _type.HRESULT]


class ICoreWebView2Settings5(ICoreWebView2Settings4):
    get_IsPinchZoomEnabled: _Callable[[_Pointer[_type.BOOL]],  # enabled
                                      _type.HRESULT]
    put_IsPinchZoomEnabled: _Callable[[_type.BOOL],  # enabled
                                      _type.HRESULT]


class ICoreWebView2Settings6(ICoreWebView2Settings5):
    get_IsSwipeNavigationEnabled: _Callable[[_Pointer[_type.BOOL]],  # enabled
                                            _type.HRESULT]
    put_IsSwipeNavigationEnabled: _Callable[[_type.BOOL],  # enabled
                                            _type.HRESULT]


class ICoreWebView2Settings7(ICoreWebView2Settings6):
    get_HiddenPdfToolbarItems: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PDF_TOOLBAR_ITEMS]],  # hidden_pdf_toolbar_items
                                         _type.HRESULT]
    put_HiddenPdfToolbarItems: _Callable[[_enum_WebView2.COREWEBVIEW2_PDF_TOOLBAR_ITEMS],  # hidden_pdf_toolbar_items
                                         _type.HRESULT]


class ICoreWebView2SourceChangedEventArgs(_Unknwnbase.IUnknown):
    get_IsNewDocument: _Callable[[_Pointer[_type.BOOL]],  # isNewDocument
                                 _type.HRESULT]


class _ICoreWebView2SourceChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2SourceChangedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2SourceChangedEventHandler(_ICoreWebView2SourceChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2SourceChangedEventHandler_impl(_ICoreWebView2SourceChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2StateChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2DownloadOperation,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2StateChangedEventHandler(_ICoreWebView2StateChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2StateChangedEventHandler_impl(_ICoreWebView2StateChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2StatusBarTextChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2StatusBarTextChangedEventHandler(_ICoreWebView2StatusBarTextChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2StatusBarTextChangedEventHandler_impl(_ICoreWebView2StatusBarTextChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2TrySuspendCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       _type.BOOL],  # isSuccessful
                      _type.HRESULT]


class ICoreWebView2TrySuspendCompletedHandler(_ICoreWebView2TrySuspendCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2TrySuspendCompletedHandler_impl(_ICoreWebView2TrySuspendCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2WebMessageReceivedEventArgs(_Unknwnbase.IUnknown):
    get_Source: _Callable[[_Pointer[_type.LPWSTR]],  # source
                          _type.HRESULT]
    get_WebMessageAsJson: _Callable[[_Pointer[_type.LPWSTR]],  # webMessageAsJson
                                    _type.HRESULT]
    TryGetWebMessageAsString: _Callable[[_Pointer[_type.LPWSTR]],  # webMessageAsString
                                        _type.HRESULT]


class _ICoreWebView2WebMessageReceivedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2WebMessageReceivedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2WebMessageReceivedEventHandler(_ICoreWebView2WebMessageReceivedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2WebMessageReceivedEventHandler_impl(_ICoreWebView2WebMessageReceivedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2WebResourceRequest(_Unknwnbase.IUnknown):
    get_Uri: _Callable[[_Pointer[_type.LPWSTR]],  # uri
                       _type.HRESULT]
    put_Uri: _Callable[[_type.LPCWSTR],  # uri
                       _type.HRESULT]
    get_Method: _Callable[[_Pointer[_type.LPWSTR]],  # method
                          _type.HRESULT]
    put_Method: _Callable[[_type.LPCWSTR],  # method
                          _type.HRESULT]
    get_Content: _Callable[[_Pointer[_objidlbase.IStream]],  # content
                           _type.HRESULT]
    put_Content: _Callable[[_objidlbase.IStream],  # content
                           _type.HRESULT]
    get_Headers: _Callable[[_Pointer[ICoreWebView2HttpRequestHeaders]],  # headers
                           _type.HRESULT]


class ICoreWebView2WebResourceRequestedEventArgs(_Unknwnbase.IUnknown):
    get_Request: _Callable[[_Pointer[ICoreWebView2WebResourceRequest]],  # request
                           _type.HRESULT]
    get_Response: _Callable[[_Pointer[ICoreWebView2WebResourceResponse]],  # response
                            _type.HRESULT]
    put_Response: _Callable[[ICoreWebView2WebResourceResponse],  # response
                            _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ICoreWebView2Deferral]],  # deferral
                           _type.HRESULT]
    get_ResourceContext: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_WEB_RESOURCE_CONTEXT]],  # context
                                   _type.HRESULT]


class _ICoreWebView2WebResourceRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2WebResourceRequestedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2WebResourceRequestedEventHandler(_ICoreWebView2WebResourceRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2WebResourceRequestedEventHandler_impl(_ICoreWebView2WebResourceRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2WebResourceResponse(_Unknwnbase.IUnknown):
    get_Content: _Callable[[_Pointer[_objidlbase.IStream]],  # content
                           _type.HRESULT]
    put_Content: _Callable[[_objidlbase.IStream],  # content
                           _type.HRESULT]
    get_Headers: _Callable[[_Pointer[ICoreWebView2HttpResponseHeaders]],  # headers
                           _type.HRESULT]
    get_StatusCode: _Callable[[_Pointer[_type.c_int]],  # statusCode
                              _type.HRESULT]
    put_StatusCode: _Callable[[_type.c_int],  # statusCode
                              _type.HRESULT]
    get_ReasonPhrase: _Callable[[_Pointer[_type.LPWSTR]],  # reasonPhrase
                                _type.HRESULT]
    put_ReasonPhrase: _Callable[[_type.LPCWSTR],  # reasonPhrase
                                _type.HRESULT]


class _ICoreWebView2WebResourceResponseReceivedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       ICoreWebView2WebResourceResponseReceivedEventArgs],  # args
                      _type.HRESULT]


class ICoreWebView2WebResourceResponseReceivedEventHandler(_ICoreWebView2WebResourceResponseReceivedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2WebResourceResponseReceivedEventHandler_impl(_ICoreWebView2WebResourceResponseReceivedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2WebResourceResponseReceivedEventArgs(_Unknwnbase.IUnknown):
    get_Request: _Callable[[_Pointer[ICoreWebView2WebResourceRequest]],  # request
                           _type.HRESULT]
    get_Response: _Callable[[_Pointer[ICoreWebView2WebResourceResponseView]],  # response
                            _type.HRESULT]


class ICoreWebView2WebResourceResponseView(_Unknwnbase.IUnknown):
    get_Headers: _Callable[[_Pointer[ICoreWebView2HttpResponseHeaders]],  # headers
                           _type.HRESULT]
    get_StatusCode: _Callable[[_Pointer[_type.c_int]],  # statusCode
                              _type.HRESULT]
    get_ReasonPhrase: _Callable[[_Pointer[_type.LPWSTR]],  # reasonPhrase
                                _type.HRESULT]
    GetContent: _Callable[[ICoreWebView2WebResourceResponseViewGetContentCompletedHandler],  # handler
                          _type.HRESULT]


class _ICoreWebView2WebResourceResponseViewGetContentCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       _objidlbase.IStream],  # content
                      _type.HRESULT]


class ICoreWebView2WebResourceResponseViewGetContentCompletedHandler(_ICoreWebView2WebResourceResponseViewGetContentCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2WebResourceResponseViewGetContentCompletedHandler_impl(_ICoreWebView2WebResourceResponseViewGetContentCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2WindowCloseRequestedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2WindowCloseRequestedEventHandler(_ICoreWebView2WindowCloseRequestedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2WindowCloseRequestedEventHandler_impl(_ICoreWebView2WindowCloseRequestedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2WindowFeatures(_Unknwnbase.IUnknown):
    get_HasPosition: _Callable[[_Pointer[_type.BOOL]],  # value
                               _type.HRESULT]
    get_HasSize: _Callable[[_Pointer[_type.BOOL]],  # value
                           _type.HRESULT]
    get_Left: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    get_Top: _Callable[[_Pointer[_type.UINT32]],  # value
                       _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_ShouldDisplayMenuBar: _Callable[[_Pointer[_type.BOOL]],  # value
                                        _type.HRESULT]
    get_ShouldDisplayStatus: _Callable[[_Pointer[_type.BOOL]],  # value
                                       _type.HRESULT]
    get_ShouldDisplayToolbar: _Callable[[_Pointer[_type.BOOL]],  # value
                                        _type.HRESULT]
    get_ShouldDisplayScrollBars: _Callable[[_Pointer[_type.BOOL]],  # value
                                           _type.HRESULT]


class _ICoreWebView2ZoomFactorChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2Controller,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2ZoomFactorChangedEventHandler(_ICoreWebView2ZoomFactorChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ZoomFactorChangedEventHandler_impl(_ICoreWebView2ZoomFactorChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2IsMutedChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2IsMutedChangedEventHandler(_ICoreWebView2IsMutedChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2IsMutedChangedEventHandler_impl(_ICoreWebView2IsMutedChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2IsDocumentPlayingAudioChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2IsDocumentPlayingAudioChangedEventHandler(_ICoreWebView2IsDocumentPlayingAudioChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2IsDocumentPlayingAudioChangedEventHandler_impl(_ICoreWebView2IsDocumentPlayingAudioChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class ICoreWebView2ProcessInfo(_Unknwnbase.IUnknown):
    get_ProcessId: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum_WebView2.COREWEBVIEW2_PROCESS_KIND]],  # kind
                        _type.HRESULT]


class ICoreWebView2ProcessInfoCollection(_Unknwnbase.IUnknown):
    get_Count: _Callable[[_Pointer[_type.UINT]],  # count
                         _type.HRESULT]
    GetValueAtIndex: _Callable[[_type.UINT32,  # index
                                _Pointer[ICoreWebView2ProcessInfo]],  # processInfo
                               _type.HRESULT]


class _ICoreWebView2ProcessInfosChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2Environment,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2ProcessInfosChangedEventHandler(_ICoreWebView2ProcessInfosChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2ProcessInfosChangedEventHandler_impl(_ICoreWebView2ProcessInfosChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2FaviconChangedEventHandler:
    Invoke: _Callable[[ICoreWebView2,  # sender
                       _Unknwnbase.IUnknown],  # args
                      _type.HRESULT]


class ICoreWebView2FaviconChangedEventHandler(_ICoreWebView2FaviconChangedEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2FaviconChangedEventHandler_impl(_ICoreWebView2FaviconChangedEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _ICoreWebView2GetFaviconCompletedHandler:
    Invoke: _Callable[[_type.HRESULT,  # errorCode
                       _objidlbase.IStream],  # faviconStream
                      _type.HRESULT]


class ICoreWebView2GetFaviconCompletedHandler(_ICoreWebView2GetFaviconCompletedHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class ICoreWebView2GetFaviconCompletedHandler_impl(_ICoreWebView2GetFaviconCompletedHandler, _Unknwnbase.IUnknown_impl):
    pass


# noinspection PyPep8Naming
class ICoreWebView2_14(ICoreWebView2_13):
    add_ServerCertificateErrorDetected: _Callable[[ICoreWebView2ServerCertificateErrorDetectedEventHandler,  # eventHandler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_ServerCertificateErrorDetected: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]
    ClearServerCertificateErrorActions: _Callable[[ICoreWebView2ClearServerCertificateErrorActionsCompletedHandler],  # handler
                                                  _type.HRESULT]


# noinspection PyPep8Naming
class ICoreWebView2_15(ICoreWebView2_14):
    add_FaviconChanged: _Callable[[ICoreWebView2FaviconChangedEventHandler,  # eventHandler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_FaviconChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    get_FaviconUri: _Callable[[_Pointer[_type.LPWSTR]],  # value
                              _type.HRESULT]
    GetFavicon: _Callable[[_enum_WebView2.COREWEBVIEW2_FAVICON_IMAGE_FORMAT,  # format
                           ICoreWebView2GetFaviconCompletedHandler],  # completedHandler
                          _type.HRESULT]
