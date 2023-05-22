from __future__ import annotations

from typing import Callable as _Callable

from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class ILocalContentSuggestionSettings(_inspectable.IInspectable):
    put_Enabled: _Callable[[_type.boolean],  # value
                           _type.HRESULT]
    get_Enabled: _Callable[[_Pointer[_type.boolean]],  # value
                           _type.HRESULT]
    get_Locations: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_Storage.IStorageFolder]]],  # value
                             _type.HRESULT]
    put_AqsFilter: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_AqsFilter: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    get_PropertiesToMatch: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                     _type.HRESULT]


class ISearchPane(_inspectable.IInspectable):
    SearchHistoryEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    SearchHistoryContext: _Callable[[_Pointer[_type.HSTRING]],  # value
                                    _type.HRESULT]
    PlaceholderText: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    Visible: _Callable[[_Pointer[_type.boolean]],  # value
                       _type.HRESULT]
    VisibilityChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                 _type.HRESULT]
    QueryChanged: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    SuggestionsRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                    _type.HRESULT]
    QuerySubmitted: _Callable[[_struct.EventRegistrationToken],  # token
                              _type.HRESULT]
    ResultSuggestionChosen: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]
    SetLocalContentSuggestionSettings: _Callable[[ILocalContentSuggestionSettings],  # settings
                                                 _type.HRESULT]
    ShowOverloadDefault: _Callable[[],
                                   _type.HRESULT]
    ShowOverloadWithQuery: _Callable[[_type.HSTRING],  # query
                                     _type.HRESULT]
    ShowOnKeyboardInput: _Callable[[_Pointer[_type.boolean]],  # value
                                   _type.HRESULT]
    TrySetQueryText: _Callable[[_type.HSTRING,  # query
                                _Pointer[_type.boolean]],  # succeeded
                               _type.HRESULT]


class ISearchPaneQueryChangedEventArgs(_inspectable.IInspectable):
    QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    LinguisticDetails: _Callable[[_Pointer[ISearchPaneQueryLinguisticDetails]],  # value
                                 _type.HRESULT]


class ISearchPaneQueryLinguisticDetails(_inspectable.IInspectable):
    get_QueryTextAlternatives: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                         _type.HRESULT]
    get_QueryTextCompositionStart: _Callable[[_Pointer[_type.UINT32]],  # value
                                             _type.HRESULT]
    get_QueryTextCompositionLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]


class ISearchPaneQuerySubmittedEventArgs(_inspectable.IInspectable):
    QueryText: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class ISearchPaneQuerySubmittedEventArgsWithLinguisticDetails(_inspectable.IInspectable):
    LinguisticDetails: _Callable[[_Pointer[ISearchPaneQueryLinguisticDetails]],  # value
                                 _type.HRESULT]


class ISearchPaneResultSuggestionChosenEventArgs(_inspectable.IInspectable):
    Tag: _Callable[[_Pointer[_type.HSTRING]],  # value
                   _type.HRESULT]


class ISearchPaneStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[ISearchPane]],  # searchPane
                                 _type.HRESULT]


class ISearchPaneStaticsWithHideThisApplication(_inspectable.IInspectable, factory=True):
    HideThisApplication: _Callable[[],
                                   _type.HRESULT]


class ISearchPaneSuggestionsRequest(_inspectable.IInspectable):
    IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]
    SearchSuggestionCollection: _Callable[[_Pointer[ISearchSuggestionCollection]],  # collection
                                          _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ISearchPaneSuggestionsRequestDeferral]],  # deferral
                           _type.HRESULT]


class ISearchPaneSuggestionsRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]


class ISearchPaneSuggestionsRequestedEventArgs(_inspectable.IInspectable):
    Request: _Callable[[_Pointer[ISearchPaneSuggestionsRequest]],  # value
                       _type.HRESULT]


class ISearchPaneVisibilityChangedEventArgs(_inspectable.IInspectable):
    Visible: _Callable[[_Pointer[_type.boolean]],  # value
                       _type.HRESULT]


class ISearchQueryLinguisticDetails(_inspectable.IInspectable):
    get_QueryTextAlternatives: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                         _type.HRESULT]
    get_QueryTextCompositionStart: _Callable[[_Pointer[_type.UINT32]],  # value
                                             _type.HRESULT]
    get_QueryTextCompositionLength: _Callable[[_Pointer[_type.UINT32]],  # value
                                              _type.HRESULT]


class ISearchQueryLinguisticDetailsFactory(_inspectable.IInspectable, factory=True):
    CreateInstance: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING],  # queryTextAlternatives
                               _type.UINT32,  # queryTextCompositionStart
                               _type.UINT32,  # queryTextCompositionLength
                               _Pointer[ISearchQueryLinguisticDetails]],  # value
                              _type.HRESULT]


class ISearchSuggestionCollection(_inspectable.IInspectable):
    get_Size: _Callable[[_Pointer[_type.UINT32]],  # value
                        _type.HRESULT]
    AppendQuerySuggestion: _Callable[[_type.HSTRING],  # text
                                     _type.HRESULT]
    AppendQuerySuggestions: _Callable[[_Windows_Foundation_Collections.IIterable[_type.HSTRING]],  # suggestions
                                      _type.HRESULT]
    AppendResultSuggestion: _Callable[[_type.HSTRING,  # text
                                       _type.HSTRING,  # detailText
                                       _type.HSTRING,  # tag
                                       _Windows_Storage_Streams.IRandomAccessStreamReference,  # image
                                       _type.HSTRING],  # imageAlternateText
                                      _type.HRESULT]
    AppendSearchSeparator: _Callable[[_type.HSTRING],  # label
                                     _type.HRESULT]


class ISearchSuggestionsRequest(_inspectable.IInspectable):
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_SearchSuggestionCollection: _Callable[[_Pointer[ISearchSuggestionCollection]],  # collection
                                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[ISearchSuggestionsRequestDeferral]],  # deferral
                           _type.HRESULT]


class ISearchSuggestionsRequestDeferral(_inspectable.IInspectable):
    Complete: _Callable[[],
                        _type.HRESULT]
