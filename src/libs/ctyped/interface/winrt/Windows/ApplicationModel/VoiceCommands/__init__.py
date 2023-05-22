from __future__ import annotations

from typing import Callable as _Callable

from .. import AppService as _Windows_ApplicationModel_AppService
from ... import Foundation as _Windows_Foundation
from ... import Globalization as _Windows_Globalization
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Media import SpeechRecognition as _Windows_Media_SpeechRecognition
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IVoiceCommand(_inspectable.IInspectable):
    get_CommandName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # value
                              _type.HRESULT]
    get_SpeechRecognitionResult: _Callable[[_Pointer[_Windows_Media_SpeechRecognition.ISpeechRecognitionResult]],  # value
                                           _type.HRESULT]


class IVoiceCommandCompletedEventArgs(_inspectable.IInspectable):
    get_Reason: _Callable[[_Pointer[_enum.Windows.ApplicationModel.VoiceCommands.VoiceCommandCompletionReason]],  # value
                          _type.HRESULT]


class IVoiceCommandConfirmationResult(_inspectable.IInspectable):
    get_Confirmed: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class IVoiceCommandContentTile(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_TextLine1: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_TextLine1: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_TextLine2: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_TextLine2: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_TextLine3: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_TextLine3: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_Image: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                         _type.HRESULT]
    put_Image: _Callable[[_Windows_Storage.IStorageFile],  # value
                         _type.HRESULT]
    get_AppContext: _Callable[[_Pointer[_inspectable.IInspectable]],  # value
                              _type.HRESULT]
    put_AppContext: _Callable[[_inspectable.IInspectable],  # value
                              _type.HRESULT]
    get_AppLaunchArgument: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_AppLaunchArgument: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_ContentTileType: _Callable[[_Pointer[_enum.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType]],  # value
                                   _type.HRESULT]
    put_ContentTileType: _Callable[[_enum.Windows.ApplicationModel.VoiceCommands.VoiceCommandContentTileType],  # value
                                   _type.HRESULT]


class IVoiceCommandDefinition(_inspectable.IInspectable):
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    SetPhraseListAsync: _Callable[[_type.HSTRING,  # phraseListName
                                   _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # phraseList
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # updateAction
                                  _type.HRESULT]


class IVoiceCommandDefinitionManagerStatics(_inspectable.IInspectable, factory=True):
    InstallCommandDefinitionsFromStorageFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                                              _Pointer[_Windows_Foundation.IAsyncAction]],  # installAction
                                                             _type.HRESULT]
    get_InstalledCommandDefinitions: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IVoiceCommandDefinition]]],  # voiceCommandDefinitions
                                               _type.HRESULT]


class IVoiceCommandDisambiguationResult(_inspectable.IInspectable):
    get_SelectedItem: _Callable[[_Pointer[IVoiceCommandContentTile]],  # value
                                _type.HRESULT]


class IVoiceCommandResponse(_inspectable.IInspectable):
    get_Message: _Callable[[_Pointer[IVoiceCommandUserMessage]],  # value
                           _type.HRESULT]
    put_Message: _Callable[[IVoiceCommandUserMessage],  # value
                           _type.HRESULT]
    get_RepeatMessage: _Callable[[_Pointer[IVoiceCommandUserMessage]],  # value
                                 _type.HRESULT]
    put_RepeatMessage: _Callable[[IVoiceCommandUserMessage],  # value
                                 _type.HRESULT]
    get_AppLaunchArgument: _Callable[[_Pointer[_type.HSTRING]],  # value
                                     _type.HRESULT]
    put_AppLaunchArgument: _Callable[[_type.HSTRING],  # value
                                     _type.HRESULT]
    get_VoiceCommandContentTiles: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IVoiceCommandContentTile]]],  # value
                                            _type.HRESULT]


class IVoiceCommandResponseStatics(_inspectable.IInspectable, factory=True):
    get_MaxSupportedVoiceCommandContentTiles: _Callable[[_Pointer[_type.UINT32]],  # value
                                                        _type.HRESULT]
    CreateResponse: _Callable[[IVoiceCommandUserMessage,  # userMessage
                               _Pointer[IVoiceCommandResponse]],  # response
                              _type.HRESULT]
    CreateResponseWithTiles: _Callable[[IVoiceCommandUserMessage,  # message
                                        _Windows_Foundation_Collections.IIterable[IVoiceCommandContentTile],  # contentTiles
                                        _Pointer[IVoiceCommandResponse]],  # response
                                       _type.HRESULT]
    CreateResponseForPrompt: _Callable[[IVoiceCommandUserMessage,  # message
                                        IVoiceCommandUserMessage,  # repeatMessage
                                        _Pointer[IVoiceCommandResponse]],  # response
                                       _type.HRESULT]
    CreateResponseForPromptWithTiles: _Callable[[IVoiceCommandUserMessage,  # message
                                                 IVoiceCommandUserMessage,  # repeatMessage
                                                 _Windows_Foundation_Collections.IIterable[IVoiceCommandContentTile],  # contentTiles
                                                 _Pointer[IVoiceCommandResponse]],  # response
                                                _type.HRESULT]


class IVoiceCommandServiceConnection(_inspectable.IInspectable):
    GetVoiceCommandAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IVoiceCommand]]],  # operation
                                    _type.HRESULT]
    RequestConfirmationAsync: _Callable[[IVoiceCommandResponse,  # response
                                         _Pointer[_Windows_Foundation.IAsyncOperation[IVoiceCommandConfirmationResult]]],  # operation
                                        _type.HRESULT]
    RequestDisambiguationAsync: _Callable[[IVoiceCommandResponse,  # response
                                           _Pointer[_Windows_Foundation.IAsyncOperation[IVoiceCommandDisambiguationResult]]],  # operation
                                          _type.HRESULT]
    ReportProgressAsync: _Callable[[IVoiceCommandResponse,  # response
                                    _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                   _type.HRESULT]
    ReportSuccessAsync: _Callable[[IVoiceCommandResponse,  # response
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                  _type.HRESULT]
    ReportFailureAsync: _Callable[[IVoiceCommandResponse,  # response
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                  _type.HRESULT]
    RequestAppLaunchAsync: _Callable[[IVoiceCommandResponse,  # response
                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                     _type.HRESULT]
    get_Language: _Callable[[_Pointer[_Windows_Globalization.ILanguage]],  # language
                            _type.HRESULT]
    add_VoiceCommandCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[IVoiceCommandServiceConnection, IVoiceCommandCompletedEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_VoiceCommandCompleted: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class IVoiceCommandServiceConnectionStatics(_inspectable.IInspectable, factory=True):
    FromAppServiceTriggerDetails: _Callable[[_Windows_ApplicationModel_AppService.IAppServiceTriggerDetails,  # triggerDetails
                                             _Pointer[IVoiceCommandServiceConnection]],  # value
                                            _type.HRESULT]


class IVoiceCommandUserMessage(_inspectable.IInspectable):
    get_DisplayMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    put_DisplayMessage: _Callable[[_type.HSTRING],  # value
                                  _type.HRESULT]
    get_SpokenMessage: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_SpokenMessage: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
