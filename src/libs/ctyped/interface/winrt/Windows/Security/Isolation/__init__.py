from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from .....um import Unknwnbase as _Unknwnbase
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class _IHostMessageReceivedCallback:
    Invoke: _Callable[[_struct.GUID,  # receiverId
                       _Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]],  # message
                      _type.HRESULT]


class IHostMessageReceivedCallback(_IHostMessageReceivedCallback, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IHostMessageReceivedCallback_impl(_IHostMessageReceivedCallback, _Unknwnbase.IUnknown_impl):
    pass


class _IMessageReceivedCallback:
    Invoke: _Callable[[_struct.GUID,  # receiverId
                       _Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]],  # message
                      _type.HRESULT]


class IMessageReceivedCallback(_IMessageReceivedCallback, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IMessageReceivedCallback_impl(_IMessageReceivedCallback, _Unknwnbase.IUnknown_impl):
    pass


class IIsolatedWindowsEnvironment(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    StartProcessSilentlyAsync: _Callable[[_type.HSTRING,  # hostExePath
                                          _type.HSTRING,  # arguments
                                          _enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentActivator,  # activator
                                          _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentStartProcessResult]]],  # operation
                                         _type.HRESULT]
    StartProcessSilentlyWithTelemetryAsync: _Callable[[_type.HSTRING,  # hostExePath
                                                       _type.HSTRING,  # arguments
                                                       _enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentActivator,  # activator
                                                       IIsolatedWindowsEnvironmentTelemetryParameters,  # telemetryParameters
                                                       _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentStartProcessResult]]],  # operation
                                                      _type.HRESULT]
    ShareFolderAsync: _Callable[[_type.HSTRING,  # hostFolder
                                 IIsolatedWindowsEnvironmentShareFolderRequestOptions,  # requestOptions
                                 _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentShareFolderResult]]],  # operation
                                _type.HRESULT]
    ShareFolderWithTelemetryAsync: _Callable[[_type.HSTRING,  # hostFolder
                                              IIsolatedWindowsEnvironmentShareFolderRequestOptions,  # requestOptions
                                              IIsolatedWindowsEnvironmentTelemetryParameters,  # telemetryParameters
                                              _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentShareFolderResult]]],  # operation
                                             _type.HRESULT]
    LaunchFileWithUIAsync: _Callable[[_type.HSTRING,  # appExePath
                                      _type.HSTRING,  # argumentsTemplate
                                      _type.HSTRING,  # filePath
                                      _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentLaunchFileResult]]],  # operation
                                     _type.HRESULT]
    LaunchFileWithUIAndTelemetryAsync: _Callable[[_type.HSTRING,  # appExePath
                                                  _type.HSTRING,  # argumentsTemplate
                                                  _type.HSTRING,  # filePath
                                                  IIsolatedWindowsEnvironmentTelemetryParameters,  # telemetryParameters
                                                  _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentLaunchFileResult]]],  # operation
                                                 _type.HRESULT]
    TerminateAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                              _type.HRESULT]
    TerminateWithTelemetryAsync: _Callable[[IIsolatedWindowsEnvironmentTelemetryParameters,  # telemetryParameters
                                            _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                           _type.HRESULT]
    RegisterMessageReceiver: _Callable[[_struct.GUID,  # receiverId
                                        IMessageReceivedCallback],  # messageReceivedCallback
                                       _type.HRESULT]
    UnregisterMessageReceiver: _Callable[[_struct.GUID],  # receiverId
                                         _type.HRESULT]


class IIsolatedWindowsEnvironment2(_inspectable.IInspectable):
    PostMessageToReceiverAsync: _Callable[[_struct.GUID,  # receiverId
                                           _Windows_Foundation_Collections.IIterable[_inspectable.IInspectable],  # message
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentPostMessageResult]]],  # operation
                                          _type.HRESULT]
    PostMessageToReceiverWithTelemetryAsync: _Callable[[_struct.GUID,  # receiverId
                                                        _Windows_Foundation_Collections.IIterable[_inspectable.IInspectable],  # message
                                                        IIsolatedWindowsEnvironmentTelemetryParameters,  # telemetryParameters
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentPostMessageResult]]],  # operation
                                                       _type.HRESULT]


class IIsolatedWindowsEnvironment3(_inspectable.IInspectable):
    GetUserInfo: _Callable[[_Pointer[IIsolatedWindowsEnvironmentUserInfo]],  # result
                           _type.HRESULT]
    ShareFileAsync: _Callable[[_type.HSTRING,  # filePath
                               IIsolatedWindowsEnvironmentShareFileRequestOptions,  # options
                               _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentShareFileResult]]],  # operation
                              _type.HRESULT]
    ShareFileWithTelemetryAsync: _Callable[[_type.HSTRING,  # filePath
                                            IIsolatedWindowsEnvironmentShareFileRequestOptions,  # options
                                            IIsolatedWindowsEnvironmentTelemetryParameters,  # telemetryParameters
                                            _Pointer[_Windows_Foundation.IAsyncOperation[IIsolatedWindowsEnvironmentShareFileResult]]],  # operation
                                           _type.HRESULT]


class IIsolatedWindowsEnvironment4(_inspectable.IInspectable):
    ChangePriority: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority],  # Priority
                              _type.HRESULT]


class IIsolatedWindowsEnvironmentCreateResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Environment: _Callable[[_Pointer[IIsolatedWindowsEnvironment]],  # value
                               _type.HRESULT]


class IIsolatedWindowsEnvironmentCreateResult2(_inspectable.IInspectable):
    ChangeCreationPriority: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority],  # priority
                                      _type.HRESULT]


class IIsolatedWindowsEnvironmentFactory(_inspectable.IInspectable, factory=True):
    CreateAsync: _Callable[[IIsolatedWindowsEnvironmentOptions,  # options
                            _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IIsolatedWindowsEnvironmentCreateResult, _struct.Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateProgress]]],  # operation
                           _type.HRESULT]
    CreateWithTelemetryAsync: _Callable[[IIsolatedWindowsEnvironmentOptions,  # options
                                         IIsolatedWindowsEnvironmentTelemetryParameters,  # telemetryParameters
                                         _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[IIsolatedWindowsEnvironmentCreateResult, _struct.Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateProgress]]],  # operation
                                        _type.HRESULT]
    GetById: _Callable[[_type.HSTRING,  # environmentId
                        _Pointer[IIsolatedWindowsEnvironment]],  # result
                       _type.HRESULT]
    FindByOwnerId: _Callable[[_type.HSTRING,  # environmentOwnerId
                              _Pointer[_Windows_Foundation_Collections.IVectorView[IIsolatedWindowsEnvironment]]],  # result
                             _type.HRESULT]


class IIsolatedWindowsEnvironmentFile(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_struct.GUID]],  # value
                      _type.HRESULT]
    get_HostPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class IIsolatedWindowsEnvironmentFile2(_inspectable.IInspectable):
    get_GuestPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class IIsolatedWindowsEnvironmentHostStatics(_inspectable.IInspectable, factory=True):
    get_IsReady: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_HostErrors: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentHostError]]],  # value
                              _type.HRESULT]


class IIsolatedWindowsEnvironmentLaunchFileResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_File: _Callable[[_Pointer[IIsolatedWindowsEnvironmentFile]],  # value
                        _type.HRESULT]


class IIsolatedWindowsEnvironmentOptions(_inspectable.IInspectable):
    get_EnvironmentOwnerId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    put_EnvironmentOwnerId: _Callable[[_type.HSTRING],  # value
                                      _type.HRESULT]
    get_AllowedClipboardFormats: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats]],  # value
                                           _type.HRESULT]
    put_AllowedClipboardFormats: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats],  # value
                                           _type.HRESULT]
    get_ClipboardCopyPasteDirections: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentClipboardCopyPasteDirections]],  # value
                                                _type.HRESULT]
    put_ClipboardCopyPasteDirections: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentClipboardCopyPasteDirections],  # value
                                                _type.HRESULT]
    get_AvailablePrinters: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAvailablePrinters]],  # value
                                     _type.HRESULT]
    put_AvailablePrinters: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAvailablePrinters],  # value
                                     _type.HRESULT]
    get_SharedHostFolderPath: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    get_SharedFolderNameInEnvironment: _Callable[[_Pointer[_type.HSTRING]],  # value
                                                 _type.HRESULT]
    ShareHostFolderForUntrustedItems: _Callable[[_type.HSTRING,  # SharedHostFolderPath
                                                 _type.HSTRING],  # ShareFolderNameInEnvironment
                                                _type.HRESULT]
    get_PersistUserProfile: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_PersistUserProfile: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_AllowGraphicsHardwareAcceleration: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_AllowGraphicsHardwareAcceleration: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_AllowCameraAndMicrophoneAccess: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_AllowCameraAndMicrophoneAccess: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]


class IIsolatedWindowsEnvironmentOptions2(_inspectable.IInspectable):
    get_WindowAnnotationOverride: _Callable[[_Pointer[_type.HSTRING]],  # value
                                            _type.HRESULT]
    put_WindowAnnotationOverride: _Callable[[_type.HSTRING],  # value
                                            _type.HRESULT]


class IIsolatedWindowsEnvironmentOptions3(_inspectable.IInspectable):
    get_AllowedClipboardFormatsToEnvironment: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats]],  # value
                                                        _type.HRESULT]
    put_AllowedClipboardFormatsToEnvironment: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats],  # value
                                                        _type.HRESULT]
    get_AllowedClipboardFormatsToHost: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats]],  # value
                                                 _type.HRESULT]
    put_AllowedClipboardFormatsToHost: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats],  # value
                                                 _type.HRESULT]
    get_CreationPriority: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority]],  # value
                                    _type.HRESULT]
    put_CreationPriority: _Callable[[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority],  # value
                                    _type.HRESULT]


class IIsolatedWindowsEnvironmentOwnerRegistrationData(_inspectable.IInspectable):
    get_ShareableFolders: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                    _type.HRESULT]
    get_ProcessesRunnableAsSystem: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                             _type.HRESULT]
    get_ProcessesRunnableAsUser: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                           _type.HRESULT]
    get_ActivationFileExtensions: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                            _type.HRESULT]


class IIsolatedWindowsEnvironmentOwnerRegistrationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IIsolatedWindowsEnvironmentOwnerRegistrationStatics(_inspectable.IInspectable, factory=True):
    Register: _Callable[[_type.HSTRING,  # ownerName
                         IIsolatedWindowsEnvironmentOwnerRegistrationData,  # ownerRegistrationData
                         _Pointer[IIsolatedWindowsEnvironmentOwnerRegistrationResult]],  # result
                        _type.HRESULT]
    Unregister: _Callable[[_type.HSTRING],  # ownerName
                          _type.HRESULT]


class IIsolatedWindowsEnvironmentPostMessageResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IIsolatedWindowsEnvironmentProcess(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentProcessState]],  # value
                         _type.HRESULT]
    get_ExitCode: _Callable[[_Pointer[_type.UINT32]],  # value
                            _type.HRESULT]
    WaitForExit: _Callable[[],
                           _type.HRESULT]
    WaitForExitWithTimeout: _Callable[[_type.UINT32],  # timeoutMilliseconds
                                      _type.HRESULT]
    WaitForExitAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                _type.HRESULT]


class IIsolatedWindowsEnvironmentShareFileRequestOptions(_inspectable.IInspectable):
    get_AllowWrite: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_AllowWrite: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class IIsolatedWindowsEnvironmentShareFileResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_File: _Callable[[_Pointer[IIsolatedWindowsEnvironmentFile]],  # value
                        _type.HRESULT]


class IIsolatedWindowsEnvironmentShareFolderRequestOptions(_inspectable.IInspectable):
    get_AllowWrite: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_AllowWrite: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class IIsolatedWindowsEnvironmentShareFolderResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]


class IIsolatedWindowsEnvironmentStartProcessResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_Process: _Callable[[_Pointer[IIsolatedWindowsEnvironmentProcess]],  # value
                           _type.HRESULT]


class IIsolatedWindowsEnvironmentTelemetryParameters(_inspectable.IInspectable):
    get_CorrelationId: _Callable[[_Pointer[_struct.GUID]],  # value
                                 _type.HRESULT]
    put_CorrelationId: _Callable[[_struct.GUID],  # value
                                 _type.HRESULT]


class IIsolatedWindowsEnvironmentUserInfo(_inspectable.IInspectable):
    get_EnvironmentUserSid: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]
    get_EnvironmentUserName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    TryWaitForSignInAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # operation
                                     _type.HRESULT]


class IIsolatedWindowsEnvironmentUserInfo2(_inspectable.IInspectable):
    TryWaitForSignInWithProgressAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.boolean, _enum.Windows.Security.Isolation.IsolatedWindowsEnvironmentSignInProgress]]],  # operation
                                                 _type.HRESULT]


class IIsolatedWindowsHostMessengerStatics(_inspectable.IInspectable, factory=True):
    PostMessageToReceiver: _Callable[[_struct.GUID,  # receiverId
                                      _Windows_Foundation_Collections.IVectorView[_inspectable.IInspectable]],  # message
                                     _type.HRESULT]
    GetFileId: _Callable[[_type.HSTRING,  # filePath
                          _Pointer[_struct.GUID]],  # result
                         _type.HRESULT]


class IIsolatedWindowsHostMessengerStatics2(_inspectable.IInspectable, factory=True):
    RegisterHostMessageReceiver: _Callable[[_struct.GUID,  # receiverId
                                            IHostMessageReceivedCallback],  # hostMessageReceivedCallback
                                           _type.HRESULT]
    UnregisterHostMessageReceiver: _Callable[[_struct.GUID],  # receiverId
                                             _type.HRESULT]
