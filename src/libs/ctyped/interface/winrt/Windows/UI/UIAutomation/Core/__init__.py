from __future__ import annotations as _

from typing import Callable as _Callable

from ... import UIAutomation as _Windows_UI_UIAutomation
from .... import Foundation as _Windows_Foundation
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IAutomationRemoteOperationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.UI.UIAutomation.Core.AutomationRemoteOperationStatus]],  # value
                          _type.HRESULT]
    get_ExtendedError: _Callable[[_Pointer[_type.HRESULT]],  # value
                                 _type.HRESULT]
    get_ErrorLocation: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    HasOperand: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # operandId
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    GetOperand: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # operandId
                           _Pointer[_inspectable.IInspectable]],  # result
                          _type.HRESULT]


class ICoreAutomationConnectionBoundObjectProvider(_inspectable.IInspectable):
    get_IsComThreadingRequired: _Callable[[_Pointer[_type.boolean]],  # value
                                          _type.HRESULT]


class ICoreAutomationRegistrarStatics(_inspectable.IInspectable):
    RegisterAnnotationType: _Callable[[_struct.GUID,  # guid
                                       _Pointer[_struct.Windows.UI.UIAutomation.Core.AutomationAnnotationTypeRegistration]],  # result
                                      _type.HRESULT]
    UnregisterAnnotationType: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationAnnotationTypeRegistration],  # registration
                                        _type.HRESULT]

    _factory = True


class ICoreAutomationRemoteOperation(_inspectable.IInspectable):
    IsOpcodeSupported: _Callable[[_type.UINT32,  # opcode
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    ImportElement: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # operandId
                              _Windows_UI_UIAutomation.IAutomationElement],  # element
                             _type.HRESULT]
    ImportTextRange: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # operandId
                                _Windows_UI_UIAutomation.IAutomationTextRange],  # textRange
                               _type.HRESULT]
    AddToResults: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId],  # operandId
                            _type.HRESULT]
    Execute: _Callable[[_type.UINT32,  # __bytecodeBufferSize
                        _Pointer[_type.BYTE],  # bytecodeBuffer
                        _Pointer[IAutomationRemoteOperationResult]],  # result
                       _type.HRESULT]


class ICoreAutomationRemoteOperation2(_inspectable.IInspectable):
    ImportConnectionBoundObject: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # operandId
                                            _Windows_UI_UIAutomation.IAutomationConnectionBoundObject],  # connectionBoundObject
                                           _type.HRESULT]


class ICoreAutomationRemoteOperationContext(_inspectable.IInspectable):
    GetOperand: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # id
                           _Pointer[_inspectable.IInspectable]],  # result
                          _type.HRESULT]
    SetOperand: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # id
                           _inspectable.IInspectable],  # operand
                          _type.HRESULT]
    SetOperand2: _Callable[[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId,  # id
                            _inspectable.IInspectable,  # operand
                            _struct.GUID],  # operandInterfaceId
                           _type.HRESULT]


class ICoreAutomationRemoteOperationExtensionProvider(_inspectable.IInspectable):
    CallExtension: _Callable[[_struct.GUID,  # extensionId
                              ICoreAutomationRemoteOperationContext,  # context
                              _type.UINT32,  # __operandIdsSize
                              _Pointer[_struct.Windows.UI.UIAutomation.Core.AutomationRemoteOperationOperandId]],  # operandIds
                             _type.HRESULT]
    IsExtensionSupported: _Callable[[_struct.GUID,  # extensionId
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]


class IRemoteAutomationClientSession(_inspectable.IInspectable):
    Start: _Callable[[],
                     _type.HRESULT]
    Stop: _Callable[[],
                    _type.HRESULT]
    CreateWindowAsync: _Callable[[_type.UINT64,  # remoteWindowId
                                  _type.UINT32,  # remoteProcessId
                                  _inspectable.IInspectable,  # parentAutomationElement
                                  _Pointer[_Windows_Foundation.IAsyncOperation[IRemoteAutomationWindow]]],  # operation
                                 _type.HRESULT]
    get_SessionId: _Callable[[_Pointer[_struct.GUID]],  # value
                             _type.HRESULT]
    add_ConnectionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteAutomationClientSession, IRemoteAutomationConnectionRequestedEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # token
                                       _type.HRESULT]
    remove_ConnectionRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                          _type.HRESULT]
    add_Disconnected: _Callable[[_Windows_Foundation.ITypedEventHandler[IRemoteAutomationClientSession, IRemoteAutomationDisconnectedEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # token
                                _type.HRESULT]
    remove_Disconnected: _Callable[[_struct.EventRegistrationToken],  # token
                                   _type.HRESULT]


class IRemoteAutomationClientSessionFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_type.HSTRING,  # name
                               _Pointer[IRemoteAutomationClientSession]],  # value
                              _type.HRESULT]
    CreateInstance2: _Callable[[_type.HSTRING,  # name
                                _struct.GUID,  # sessionId
                                _Pointer[IRemoteAutomationClientSession]],  # value
                               _type.HRESULT]

    _factory = True


class IRemoteAutomationConnectionRequestedEventArgs(_inspectable.IInspectable):
    get_LocalPipeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_RemoteProcessId: _Callable[[_Pointer[_type.UINT32]],  # value
                                   _type.HRESULT]


class IRemoteAutomationDisconnectedEventArgs(_inspectable.IInspectable):
    get_LocalPipeName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]


class IRemoteAutomationServerStatics(_inspectable.IInspectable):
    ReportSession: _Callable[[_struct.GUID],  # sessionId
                             _type.HRESULT]

    _factory = True


class IRemoteAutomationWindow(_inspectable.IInspectable):
    get_AutomationProvider: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                                      _type.HRESULT]
    UnregisterAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                               _type.HRESULT]
