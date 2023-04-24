from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Globalization as _Windows_Globalization
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ISpeechContinuousRecognitionCompletedEventArgs(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus]],  # value
                          _type.HRESULT]


class ISpeechContinuousRecognitionResultGeneratedEventArgs(_inspectable.IInspectable):
    get_Result: _Callable[[_Pointer[ISpeechRecognitionResult]],  # value
                          _type.HRESULT]


class ISpeechContinuousRecognitionSession(_inspectable.IInspectable):
    get_AutoStopSilenceTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                          _type.HRESULT]
    put_AutoStopSilenceTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                          _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                          _type.HRESULT]
    StartWithModeAsync: _Callable[[_enum.Windows.Media.SpeechRecognition.SpeechContinuousRecognitionMode,  # mode
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                  _type.HRESULT]
    StopAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                         _type.HRESULT]
    CancelAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                           _type.HRESULT]
    PauseAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                          _type.HRESULT]
    Resume: _Callable[[],
                      _type.HRESULT]
    add_Completed: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpeechContinuousRecognitionSession, ISpeechContinuousRecognitionCompletedEventArgs],  # value
                              _Pointer[_struct.EventRegistrationToken]],  # returnValue
                             _type.HRESULT]
    remove_Completed: _Callable[[_struct.EventRegistrationToken],  # value
                                _type.HRESULT]
    add_ResultGenerated: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpeechContinuousRecognitionSession, ISpeechContinuousRecognitionResultGeneratedEventArgs],  # value
                                    _Pointer[_struct.EventRegistrationToken]],  # returnValue
                                   _type.HRESULT]
    remove_ResultGenerated: _Callable[[_struct.EventRegistrationToken],  # value
                                      _type.HRESULT]


class ISpeechRecognitionCompilationResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus]],  # value
                          _type.HRESULT]


class ISpeechRecognitionConstraint(_inspectable.IInspectable):
    get_IsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsEnabled: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    put_Tag: _Callable[[_type.HSTRING],  # value
                       _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintType]],  # value
                        _type.HRESULT]
    get_Probability: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability]],  # value
                               _type.HRESULT]
    put_Probability: _Callable[[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionConstraintProbability],  # value
                               _type.HRESULT]


class ISpeechRecognitionGrammarFileConstraint(_inspectable.IInspectable):
    get_GrammarFile: _Callable[[_Pointer[_Windows_Storage.IStorageFile]],  # value
                               _type.HRESULT]


class ISpeechRecognitionGrammarFileConstraintFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Storage.IStorageFile,  # file
                       _Pointer[ISpeechRecognitionGrammarFileConstraint]],  # constraint
                      _type.HRESULT]
    CreateWithTag: _Callable[[_Windows_Storage.IStorageFile,  # file
                              _type.HSTRING,  # tag
                              _Pointer[ISpeechRecognitionGrammarFileConstraint]],  # constraint
                             _type.HRESULT]

    _factory = True


class ISpeechRecognitionHypothesis(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ISpeechRecognitionHypothesisGeneratedEventArgs(_inspectable.IInspectable):
    get_Hypothesis: _Callable[[_Pointer[ISpeechRecognitionHypothesis]],  # value
                              _type.HRESULT]


class ISpeechRecognitionListConstraint(_inspectable.IInspectable):
    get_Commands: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                            _type.HRESULT]


class ISpeechRecognitionListConstraintFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # commands
                       _Pointer[ISpeechRecognitionListConstraint]],  # constraint
                      _type.HRESULT]
    CreateWithTag: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # commands
                              _type.HSTRING,  # tag
                              _Pointer[ISpeechRecognitionListConstraint]],  # constraint
                             _type.HRESULT]

    _factory = True


class ISpeechRecognitionQualityDegradingEventArgs(_inspectable.IInspectable):
    get_Problem: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionAudioProblem]],  # value
                           _type.HRESULT]


class ISpeechRecognitionResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionResultStatus]],  # value
                          _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Confidence: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionConfidence]],  # value
                              _type.HRESULT]
    get_SemanticInterpretation: _Callable[[_Pointer[ISpeechRecognitionSemanticInterpretation]],  # value
                                          _type.HRESULT]
    GetAlternates: _Callable[[_type.UINT32,  # maxAlternates
                              _Pointer[_Windows_Foundation_Collections.IVectorView[ISpeechRecognitionResult]]],  # alternates
                             _type.HRESULT]
    get_Constraint: _Callable[[_Pointer[ISpeechRecognitionConstraint]],  # value
                              _type.HRESULT]
    get_RulePath: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                            _type.HRESULT]
    get_RawConfidence: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                 _type.HRESULT]


class ISpeechRecognitionResult2(_inspectable.IInspectable):
    get_PhraseStartTime: _Callable[[_Pointer[_struct.Windows.Foundation.DateTime]],  # value
                                   _type.HRESULT]
    get_PhraseDuration: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]


class ISpeechRecognitionSemanticInterpretation(_inspectable.IInspectable):
    get_Properties: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _Windows_Foundation_Collections.IVectorView[_type.HSTRING]]]],  # value
                              _type.HRESULT]


class ISpeechRecognitionTopicConstraint(_inspectable.IInspectable):
    get_Scenario: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionScenario]],  # value
                            _type.HRESULT]
    get_TopicHint: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]


class ISpeechRecognitionTopicConstraintFactory(_inspectable.IInspectable):
    Create: _Callable[[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionScenario,  # scenario
                       _type.HSTRING,  # topicHint
                       _Pointer[ISpeechRecognitionTopicConstraint]],  # constraint
                      _type.HRESULT]
    CreateWithTag: _Callable[[_enum.Windows.Media.SpeechRecognition.SpeechRecognitionScenario,  # scenario
                              _type.HSTRING,  # topicHint
                              _type.HSTRING,  # tag
                              _Pointer[ISpeechRecognitionTopicConstraint]],  # constraint
                             _type.HRESULT]

    _factory = True


class ISpeechRecognitionVoiceCommandDefinitionConstraint(_inspectable.IInspectable):
    pass


class ISpeechRecognizer(_inspectable.IInspectable):
    get_CurrentLanguage: _Callable[[_Pointer[_Windows_Globalization.ILanguage]],  # language
                                   _type.HRESULT]
    get_Constraints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[ISpeechRecognitionConstraint]]],  # value
                               _type.HRESULT]
    get_Timeouts: _Callable[[_Pointer[ISpeechRecognizerTimeouts]],  # value
                            _type.HRESULT]
    get_UIOptions: _Callable[[_Pointer[ISpeechRecognizerUIOptions]],  # value
                             _type.HRESULT]
    CompileConstraintsAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISpeechRecognitionCompilationResult]]],  # asyncOperation
                                       _type.HRESULT]
    RecognizeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISpeechRecognitionResult]]],  # asyncOperation
                              _type.HRESULT]
    RecognizeWithUIAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[ISpeechRecognitionResult]]],  # asyncOperation
                                    _type.HRESULT]
    add_RecognitionQualityDegrading: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpeechRecognizer, ISpeechRecognitionQualityDegradingEventArgs],  # speechRecognitionQualityDegradingHandler
                                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                                               _type.HRESULT]
    remove_RecognitionQualityDegrading: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                  _type.HRESULT]
    add_StateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpeechRecognizer, ISpeechRecognizerStateChangedEventArgs],  # stateChangedHandler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_StateChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]


class ISpeechRecognizer2(_inspectable.IInspectable):
    get_ContinuousRecognitionSession: _Callable[[_Pointer[ISpeechContinuousRecognitionSession]],  # value
                                                _type.HRESULT]
    get_State: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognizerState]],  # value
                         _type.HRESULT]
    StopRecognitionAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncAction]],  # value
                                    _type.HRESULT]
    add_HypothesisGenerated: _Callable[[_Windows_Foundation.ITypedEventHandler[ISpeechRecognizer, ISpeechRecognitionHypothesisGeneratedEventArgs],  # value
                                        _Pointer[_struct.EventRegistrationToken]],  # returnValue
                                       _type.HRESULT]
    remove_HypothesisGenerated: _Callable[[_struct.EventRegistrationToken],  # value
                                          _type.HRESULT]


class ISpeechRecognizerFactory(_inspectable.IInspectable):
    Create: _Callable[[_Windows_Globalization.ILanguage,  # language
                       _Pointer[ISpeechRecognizer]],  # recognizer
                      _type.HRESULT]

    _factory = True


class ISpeechRecognizerStateChangedEventArgs(_inspectable.IInspectable):
    get_State: _Callable[[_Pointer[_enum.Windows.Media.SpeechRecognition.SpeechRecognizerState]],  # value
                         _type.HRESULT]


class ISpeechRecognizerStatics(_inspectable.IInspectable):
    get_SystemSpeechLanguage: _Callable[[_Pointer[_Windows_Globalization.ILanguage]],  # language
                                        _type.HRESULT]
    get_SupportedTopicLanguages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Globalization.ILanguage]]],  # languages
                                           _type.HRESULT]
    get_SupportedGrammarLanguages: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Globalization.ILanguage]]],  # languages
                                             _type.HRESULT]

    _factory = True


class ISpeechRecognizerStatics2(_inspectable.IInspectable):
    TrySetSystemSpeechLanguageAsync: _Callable[[_Windows_Globalization.ILanguage,  # speechLanguage
                                                _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                               _type.HRESULT]

    _factory = True


class ISpeechRecognizerTimeouts(_inspectable.IInspectable):
    get_InitialSilenceTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                         _type.HRESULT]
    put_InitialSilenceTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                         _type.HRESULT]
    get_EndSilenceTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                     _type.HRESULT]
    put_EndSilenceTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                     _type.HRESULT]
    get_BabbleTimeout: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                 _type.HRESULT]
    put_BabbleTimeout: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                 _type.HRESULT]


class ISpeechRecognizerUIOptions(_inspectable.IInspectable):
    get_ExampleText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_ExampleText: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_AudiblePrompt: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_AudiblePrompt: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_IsReadBackEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_IsReadBackEnabled: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]
    get_ShowConfirmation: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_ShowConfirmation: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IVoiceCommandManager(_inspectable.IInspectable):
    InstallCommandSetsFromStorageFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # file
                                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # installAction
                                                      _type.HRESULT]
    InstalledCommandSets: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, IVoiceCommandSet]]],  # voiceCommandSets
                                    _type.HRESULT]

    _factory = True


class IVoiceCommandSet(_inspectable.IInspectable):
    Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                    _type.HRESULT]
    SetPhraseListAsync: _Callable[[_type.HSTRING,  # phraseListName
                                   _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # phraseList
                                   _Pointer[_Windows_Foundation.IAsyncAction]],  # updateAction
                                  _type.HRESULT]
