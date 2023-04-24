from __future__ import annotations

from typing import Callable as _Callable

from ... import Search as _Windows_ApplicationModel_Search
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IRequestingFocusOnKeyboardInputEventArgs(_inspectable.IInspectable):
    pass


class ISearchSuggestion(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.ApplicationModel.Search.Core.SearchSuggestionKind]],  # value
                        _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    get_DetailText: _Callable[[_Pointer[_type.HSTRING]],  # value
                              _type.HRESULT]
    get_Image: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                         _type.HRESULT]
    get_ImageAlternateText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                      _type.HRESULT]


class ISearchSuggestionManager(_inspectable.IInspectable):
    get_SearchHistoryEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_SearchHistoryEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    get_SearchHistoryContext: _Callable[[_Pointer[_type.HSTRING]],  # value
                                        _type.HRESULT]
    put_SearchHistoryContext: _Callable[[_type.HSTRING],  # value
                                        _type.HRESULT]
    SetLocalContentSuggestionSettings: _Callable[[_Windows_ApplicationModel_Search.ILocalContentSuggestionSettings],  # settings
                                                 _type.HRESULT]
    SetQuery: _Callable[[_type.HSTRING],  # queryText
                        _type.HRESULT]
    SetQueryWithLanguage: _Callable[[_type.HSTRING,  # queryText
                                     _type.HSTRING],  # language
                                    _type.HRESULT]
    SetQueryWithSearchQueryLinguisticDetails: _Callable[[_type.HSTRING,  # queryText
                                                         _type.HSTRING,  # language
                                                         _Windows_ApplicationModel_Search.ISearchQueryLinguisticDetails],  # linguisticDetails
                                                        _type.HRESULT]
    get_Suggestions: _Callable[[_Pointer[_Windows_Foundation_Collections.IObservableVector[ISearchSuggestion]]],  # value
                               _type.HRESULT]
    AddToHistory: _Callable[[_type.HSTRING],  # queryText
                            _type.HRESULT]
    AddToHistoryWithLanguage: _Callable[[_type.HSTRING,  # queryText
                                         _type.HSTRING],  # language
                                        _type.HRESULT]
    ClearHistory: _Callable[[],
                            _type.HRESULT]
    add_SuggestionsRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ISearchSuggestionManager, ISearchSuggestionsRequestedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_SuggestionsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_RequestingFocusOnKeyboardInput: _Callable[[_Windows_Foundation.ITypedEventHandler[ISearchSuggestionManager, IRequestingFocusOnKeyboardInputEventArgs],  # handler
                                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                                  _type.HRESULT]
    remove_RequestingFocusOnKeyboardInput: _Callable[[_struct.EventRegistrationToken],  # token
                                                     _type.HRESULT]


class ISearchSuggestionsRequestedEventArgs(_inspectable.IInspectable):
    get_QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    get_LinguisticDetails: _Callable[[_Pointer[_Windows_ApplicationModel_Search.ISearchQueryLinguisticDetails]],  # value
                                     _type.HRESULT]
    get_Request: _Callable[[_Pointer[_Windows_ApplicationModel_Search.ISearchSuggestionsRequest]],  # value
                           _type.HRESULT]
