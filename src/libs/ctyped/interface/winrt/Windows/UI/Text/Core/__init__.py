from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Globalization as _Windows_Globalization
from ....Foundation import Collections as _Windows_Foundation_Collections
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class ICoreTextCompositionCompletedEventArgs(_inspectable.IInspectable):
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    get_CompositionSegments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ICoreTextCompositionSegment]]],  # value
                                       _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ICoreTextCompositionSegment(_inspectable.IInspectable):
    get_PreconversionString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                       _type.HRESULT]
    get_Range: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                         _type.HRESULT]


class ICoreTextCompositionStartedEventArgs(_inspectable.IInspectable):
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ICoreTextEditContext(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_InputScope: _Callable[[_Pointer[_enum.Windows.UI.Text.Core.CoreTextInputScope]],  # value
                              _type.HRESULT]
    put_InputScope: _Callable[[_enum.Windows.UI.Text.Core.CoreTextInputScope],  # value
                              _type.HRESULT]
    get_IsReadOnly: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IsReadOnly: _Callable[[_type.boolean],  # value
                              _type.HRESULT]
    get_InputPaneDisplayPolicy: _Callable[[_Pointer[_enum.Windows.UI.Text.Core.CoreTextInputPaneDisplayPolicy]],  # value
                                          _type.HRESULT]
    put_InputPaneDisplayPolicy: _Callable[[_enum.Windows.UI.Text.Core.CoreTextInputPaneDisplayPolicy],  # value
                                          _type.HRESULT]
    add_TextRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextTextRequestedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_TextRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_SelectionRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextSelectionRequestedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # cookie
                                      _type.HRESULT]
    remove_SelectionRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                         _type.HRESULT]
    add_LayoutRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextLayoutRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_LayoutRequested: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_TextUpdating: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextTextUpdatingEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_TextUpdating: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    add_SelectionUpdating: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextSelectionUpdatingEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # cookie
                                     _type.HRESULT]
    remove_SelectionUpdating: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]
    add_FormatUpdating: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextFormatUpdatingEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_FormatUpdating: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_CompositionStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextCompositionStartedEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # cookie
                                      _type.HRESULT]
    remove_CompositionStarted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                         _type.HRESULT]
    add_CompositionCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, ICoreTextCompositionCompletedEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # cookie
                                        _type.HRESULT]
    remove_CompositionCompleted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                           _type.HRESULT]
    add_FocusRemoved: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, _inspectable.IInspectable],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_FocusRemoved: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    NotifyFocusEnter: _Callable[[],
                                _type.HRESULT]
    NotifyFocusLeave: _Callable[[],
                                _type.HRESULT]
    NotifyTextChanged: _Callable[[_struct.Windows.UI.Text.Core.CoreTextRange,  # modifiedRange
                                  _type.INT32,  # newLength
                                  _struct.Windows.UI.Text.Core.CoreTextRange],  # newSelection
                                 _type.HRESULT]
    NotifySelectionChanged: _Callable[[_struct.Windows.UI.Text.Core.CoreTextRange],  # selection
                                      _type.HRESULT]
    NotifyLayoutChanged: _Callable[[],
                                   _type.HRESULT]


class ICoreTextEditContext2(_inspectable.IInspectable):
    add_NotifyFocusLeaveCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextEditContext, _inspectable.IInspectable],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # cookie
                                             _type.HRESULT]
    remove_NotifyFocusLeaveCompleted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                                _type.HRESULT]


class ICoreTextFormatUpdatingEventArgs(_inspectable.IInspectable):
    get_Range: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                         _type.HRESULT]
    get_TextColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.UI.ViewManagement.UIElementType]]],  # value
                             _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.UI.ViewManagement.UIElementType]]],  # value
                                   _type.HRESULT]
    get_UnderlineColor: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.UI.ViewManagement.UIElementType]]],  # value
                                  _type.HRESULT]
    get_UnderlineType: _Callable[[_Pointer[_Windows_Foundation.IReference[_enum.Windows.UI.Text.UnderlineType]]],  # value
                                 _type.HRESULT]
    get_Reason: _Callable[[_Pointer[_enum.Windows.UI.Text.Core.CoreTextFormatUpdatingReason]],  # value
                          _type.HRESULT]
    get_Result: _Callable[[_Pointer[_enum.Windows.UI.Text.Core.CoreTextFormatUpdatingResult]],  # value
                          _type.HRESULT]
    put_Result: _Callable[[_enum.Windows.UI.Text.Core.CoreTextFormatUpdatingResult],  # value
                          _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ICoreTextLayoutBounds(_inspectable.IInspectable):
    get_TextBounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                              _type.HRESULT]
    put_TextBounds: _Callable[[_struct.Windows.Foundation.Rect],  # value
                              _type.HRESULT]
    get_ControlBounds: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                 _type.HRESULT]
    put_ControlBounds: _Callable[[_struct.Windows.Foundation.Rect],  # value
                                 _type.HRESULT]


class ICoreTextLayoutRequest(_inspectable.IInspectable):
    get_Range: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                         _type.HRESULT]
    get_LayoutBounds: _Callable[[_Pointer[ICoreTextLayoutBounds]],  # value
                                _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ICoreTextLayoutRequest2(_inspectable.IInspectable):
    get_LayoutBoundsVisualPixels: _Callable[[_Pointer[ICoreTextLayoutBounds]],  # value
                                            _type.HRESULT]


class ICoreTextLayoutRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[ICoreTextLayoutRequest]],  # value
                           _type.HRESULT]


class ICoreTextSelectionRequest(_inspectable.IInspectable):
    get_Selection: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                             _type.HRESULT]
    put_Selection: _Callable[[_struct.Windows.UI.Text.Core.CoreTextRange],  # value
                             _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ICoreTextSelectionRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[ICoreTextSelectionRequest]],  # value
                           _type.HRESULT]


class ICoreTextSelectionUpdatingEventArgs(_inspectable.IInspectable):
    get_Selection: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                             _type.HRESULT]
    get_Result: _Callable[[_Pointer[_enum.Windows.UI.Text.Core.CoreTextSelectionUpdatingResult]],  # value
                          _type.HRESULT]
    put_Result: _Callable[[_enum.Windows.UI.Text.Core.CoreTextSelectionUpdatingResult],  # value
                          _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ICoreTextServicesManager(_inspectable.IInspectable):
    get_InputLanguage: _Callable[[_Pointer[_Windows_Globalization.ILanguage]],  # value
                                 _type.HRESULT]
    add_InputLanguageChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreTextServicesManager, _inspectable.IInspectable],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # cookie
                                        _type.HRESULT]
    remove_InputLanguageChanged: _Callable[[_struct.EventRegistrationToken],  # cookie
                                           _type.HRESULT]
    CreateEditContext: _Callable[[_Pointer[ICoreTextEditContext]],  # value
                                 _type.HRESULT]


class ICoreTextServicesManagerStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentView: _Callable[[_Pointer[ICoreTextServicesManager]],  # value
                                 _type.HRESULT]


class ICoreTextServicesStatics(_inspectable.IInspectable, factory=True):
    get_HiddenCharacter: _Callable[[_Pointer[_type.WCHAR]],  # value
                                   _type.HRESULT]


class ICoreTextTextRequest(_inspectable.IInspectable):
    get_Range: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                         _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]


class ICoreTextTextRequestedEventArgs(_inspectable.IInspectable):
    get_Request: _Callable[[_Pointer[ICoreTextTextRequest]],  # value
                           _type.HRESULT]


class ICoreTextTextUpdatingEventArgs(_inspectable.IInspectable):
    get_Range: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                         _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_NewSelection: _Callable[[_Pointer[_struct.Windows.UI.Text.Core.CoreTextRange]],  # value
                                _type.HRESULT]
    get_InputLanguage: _Callable[[_Pointer[_Windows_Globalization.ILanguage]],  # value
                                 _type.HRESULT]
    get_Result: _Callable[[_Pointer[_enum.Windows.UI.Text.Core.CoreTextTextUpdatingResult]],  # value
                          _type.HRESULT]
    put_Result: _Callable[[_enum.Windows.UI.Text.Core.CoreTextTextUpdatingResult],  # value
                          _type.HRESULT]
    get_IsCanceled: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetDeferral: _Callable[[_Pointer[_Windows_Foundation.IDeferral]],  # value
                           _type.HRESULT]
