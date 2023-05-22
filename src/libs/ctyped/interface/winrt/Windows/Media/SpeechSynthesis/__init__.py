from __future__ import annotations

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ...Foundation import Collections as _Windows_Foundation_Collections
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import type as _type
from ......_utils import _Pointer


class IInstalledVoicesStatic(_inspectable.IInspectable, factory=True):
    get_AllVoices: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IVoiceInformation]]],  # value
                             _type.HRESULT]
    get_DefaultVoice: _Callable[[_Pointer[IVoiceInformation]],  # value
                                _type.HRESULT]


class IInstalledVoicesStatic2(_inspectable.IInspectable, factory=True):
    TrySetDefaultVoiceAsync: _Callable[[IVoiceInformation,  # voice
                                        _Pointer[_Windows_Foundation.IAsyncOperation[_type.boolean]]],  # result
                                       _type.HRESULT]


class ISpeechSynthesisStream(_inspectable.IInspectable):
    get_Markers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_Media.IMediaMarker]]],  # value
                           _type.HRESULT]


class ISpeechSynthesizer(_inspectable.IInspectable):
    SynthesizeTextToStreamAsync: _Callable[[_type.HSTRING,  # text
                                            _Pointer[_Windows_Foundation.IAsyncOperation[ISpeechSynthesisStream]]],  # operation
                                           _type.HRESULT]
    SynthesizeSsmlToStreamAsync: _Callable[[_type.HSTRING,  # Ssml
                                            _Pointer[_Windows_Foundation.IAsyncOperation[ISpeechSynthesisStream]]],  # operation
                                           _type.HRESULT]
    put_Voice: _Callable[[IVoiceInformation],  # value
                         _type.HRESULT]
    get_Voice: _Callable[[_Pointer[IVoiceInformation]],  # value
                         _type.HRESULT]


class ISpeechSynthesizer2(_inspectable.IInspectable):
    get_Options: _Callable[[_Pointer[ISpeechSynthesizerOptions]],  # value
                           _type.HRESULT]


class ISpeechSynthesizerOptions(_inspectable.IInspectable):
    get_IncludeWordBoundaryMetadata: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_IncludeWordBoundaryMetadata: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]
    get_IncludeSentenceBoundaryMetadata: _Callable[[_Pointer[_type.boolean]],  # value
                                                   _type.HRESULT]
    put_IncludeSentenceBoundaryMetadata: _Callable[[_type.boolean],  # value
                                                   _type.HRESULT]


class ISpeechSynthesizerOptions2(_inspectable.IInspectable):
    get_AudioVolume: _Callable[[_Pointer[_type.DOUBLE]],  # value
                               _type.HRESULT]
    put_AudioVolume: _Callable[[_type.DOUBLE],  # value
                               _type.HRESULT]
    get_SpeakingRate: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                _type.HRESULT]
    put_SpeakingRate: _Callable[[_type.DOUBLE],  # value
                                _type.HRESULT]
    get_AudioPitch: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_AudioPitch: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class ISpeechSynthesizerOptions3(_inspectable.IInspectable):
    get_AppendedSilence: _Callable[[_Pointer[_enum.Windows.Media.SpeechSynthesis.SpeechAppendedSilence]],  # value
                                   _type.HRESULT]
    put_AppendedSilence: _Callable[[_enum.Windows.Media.SpeechSynthesis.SpeechAppendedSilence],  # value
                                   _type.HRESULT]
    get_PunctuationSilence: _Callable[[_Pointer[_enum.Windows.Media.SpeechSynthesis.SpeechPunctuationSilence]],  # value
                                      _type.HRESULT]
    put_PunctuationSilence: _Callable[[_enum.Windows.Media.SpeechSynthesis.SpeechPunctuationSilence],  # value
                                      _type.HRESULT]


class IVoiceInformation(_inspectable.IInspectable):
    get_DisplayName: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Gender: _Callable[[_Pointer[_enum.Windows.Media.SpeechSynthesis.VoiceGender]],  # value
                          _type.HRESULT]
