from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Input as _Microsoft_UI_Xaml_Input
from .. import Media as _Microsoft_UI_Xaml_Media
from ... import Xaml as _Microsoft_UI_Xaml
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.Foundation import Collections as _Windows_Foundation_Collections
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IBlock(_inspectable.IInspectable):
    get_TextAlignment: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.TextAlignment]],  # value
                                 _type.HRESULT]
    put_TextAlignment: _Callable[[_enum.Microsoft.UI.Xaml.TextAlignment],  # value
                                 _type.HRESULT]
    get_HorizontalTextAlignment: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.TextAlignment]],  # value
                                           _type.HRESULT]
    put_HorizontalTextAlignment: _Callable[[_enum.Microsoft.UI.Xaml.TextAlignment],  # value
                                           _type.HRESULT]
    get_LineHeight: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_LineHeight: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]
    get_LineStackingStrategy: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.LineStackingStrategy]],  # value
                                        _type.HRESULT]
    put_LineStackingStrategy: _Callable[[_enum.Microsoft.UI.Xaml.LineStackingStrategy],  # value
                                        _type.HRESULT]
    get_Margin: _Callable[[_Pointer[_struct.Microsoft.UI.Xaml.Thickness]],  # value
                          _type.HRESULT]
    put_Margin: _Callable[[_struct.Microsoft.UI.Xaml.Thickness],  # value
                          _type.HRESULT]


class IBlockFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IBlock]],  # value
                              _type.HRESULT]


class IBlockStatics(_inspectable.IInspectable, factory=True):
    get_TextAlignmentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_HorizontalTextAlignmentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_LineHeightProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_LineStackingStrategyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    get_MarginProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                  _type.HRESULT]


class IBold(_inspectable.IInspectable):
    pass


class IGlyphs(_inspectable.IInspectable):
    get_UnicodeString: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    put_UnicodeString: _Callable[[_type.HSTRING],  # value
                                 _type.HRESULT]
    get_Indices: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Indices: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_FontUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                           _type.HRESULT]
    put_FontUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                           _type.HRESULT]
    get_StyleSimulations: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Media.StyleSimulations]],  # value
                                    _type.HRESULT]
    put_StyleSimulations: _Callable[[_enum.Microsoft.UI.Xaml.Media.StyleSimulations],  # value
                                    _type.HRESULT]
    get_FontRenderingEmSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                       _type.HRESULT]
    put_FontRenderingEmSize: _Callable[[_type.DOUBLE],  # value
                                       _type.HRESULT]
    get_OriginX: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_OriginX: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_OriginY: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_OriginY: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]
    get_Fill: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                        _type.HRESULT]
    put_Fill: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                        _type.HRESULT]
    get_IsColorFontEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                      _type.HRESULT]
    put_IsColorFontEnabled: _Callable[[_type.boolean],  # value
                                      _type.HRESULT]
    get_ColorFontPaletteIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                         _type.HRESULT]
    put_ColorFontPaletteIndex: _Callable[[_type.INT32],  # value
                                         _type.HRESULT]


class IGlyphsStatics(_inspectable.IInspectable, factory=True):
    get_UnicodeStringProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    get_IndicesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_FontUriProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_StyleSimulationsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_FontRenderingEmSizeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_OriginXProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_OriginYProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    get_FillProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                _type.HRESULT]
    get_IsColorFontEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    get_ColorFontPaletteIndexProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                 _type.HRESULT]


class IHyperlink(_inspectable.IInspectable):
    get_NavigateUri: _Callable[[_Pointer[_Windows_Foundation.IUriRuntimeClass]],  # value
                               _type.HRESULT]
    put_NavigateUri: _Callable[[_Windows_Foundation.IUriRuntimeClass],  # value
                               _type.HRESULT]
    get_UnderlineStyle: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Documents.UnderlineStyle]],  # value
                                  _type.HRESULT]
    put_UnderlineStyle: _Callable[[_enum.Microsoft.UI.Xaml.Documents.UnderlineStyle],  # value
                                  _type.HRESULT]
    get_XYFocusLeft: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                               _type.HRESULT]
    put_XYFocusLeft: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                               _type.HRESULT]
    get_XYFocusRight: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                _type.HRESULT]
    put_XYFocusRight: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                                _type.HRESULT]
    get_XYFocusUp: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                             _type.HRESULT]
    put_XYFocusUp: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                             _type.HRESULT]
    get_XYFocusDown: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                               _type.HRESULT]
    put_XYFocusDown: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                               _type.HRESULT]
    get_ElementSoundMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.ElementSoundMode]],  # value
                                    _type.HRESULT]
    put_ElementSoundMode: _Callable[[_enum.Microsoft.UI.Xaml.ElementSoundMode],  # value
                                    _type.HRESULT]
    get_FocusState: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.FocusState]],  # value
                              _type.HRESULT]
    get_XYFocusUpNavigationStrategy: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                               _type.HRESULT]
    put_XYFocusUpNavigationStrategy: _Callable[[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                               _type.HRESULT]
    get_XYFocusDownNavigationStrategy: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                                 _type.HRESULT]
    put_XYFocusDownNavigationStrategy: _Callable[[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                                 _type.HRESULT]
    get_XYFocusLeftNavigationStrategy: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                                 _type.HRESULT]
    put_XYFocusLeftNavigationStrategy: _Callable[[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                                 _type.HRESULT]
    get_XYFocusRightNavigationStrategy: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy]],  # value
                                                  _type.HRESULT]
    put_XYFocusRightNavigationStrategy: _Callable[[_enum.Microsoft.UI.Xaml.Input.XYFocusNavigationStrategy],  # value
                                                  _type.HRESULT]
    get_IsTabStop: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsTabStop: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_TabIndex: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    put_TabIndex: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    add_Click: _Callable[[_Windows_Foundation.ITypedEventHandler[IHyperlink, IHyperlinkClickEventArgs],  # handler
                          _Pointer[_struct.EventRegistrationToken]],  # token
                         _type.HRESULT]
    remove_Click: _Callable[[_struct.EventRegistrationToken],  # token
                            _type.HRESULT]
    add_GotFocus: _Callable[[_Microsoft_UI_Xaml.IRoutedEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_GotFocus: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_LostFocus: _Callable[[_Microsoft_UI_Xaml.IRoutedEventHandler,  # handler
                              _Pointer[_struct.EventRegistrationToken]],  # token
                             _type.HRESULT]
    remove_LostFocus: _Callable[[_struct.EventRegistrationToken],  # token
                                _type.HRESULT]
    Focus: _Callable[[_enum.Microsoft.UI.Xaml.FocusState,  # value
                      _Pointer[_type.boolean]],  # result
                     _type.HRESULT]


class IHyperlinkClickEventArgs(_inspectable.IInspectable):
    pass


class IHyperlinkStatics(_inspectable.IInspectable, factory=True):
    get_NavigateUriProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_UnderlineStyleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    get_XYFocusLeftProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_XYFocusRightProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    get_XYFocusUpProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_XYFocusDownProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_ElementSoundModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_FocusStateProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_XYFocusUpNavigationStrategyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                       _type.HRESULT]
    get_XYFocusDownNavigationStrategyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_XYFocusLeftNavigationStrategyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                         _type.HRESULT]
    get_XYFocusRightNavigationStrategyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                          _type.HRESULT]
    get_IsTabStopProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_TabIndexProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]


class IInline(_inspectable.IInspectable):
    pass


class IInlineFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IInline]],  # value
                              _type.HRESULT]


class IInlineUIContainer(_inspectable.IInspectable):
    get_Child: _Callable[[_Pointer[_Microsoft_UI_Xaml.IUIElement]],  # value
                         _type.HRESULT]
    put_Child: _Callable[[_Microsoft_UI_Xaml.IUIElement],  # value
                         _type.HRESULT]


class IItalic(_inspectable.IInspectable):
    pass


class ILineBreak(_inspectable.IInspectable):
    pass


class IParagraph(_inspectable.IInspectable):
    get_Inlines: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IInline]]],  # value
                           _type.HRESULT]
    get_TextIndent: _Callable[[_Pointer[_type.DOUBLE]],  # value
                              _type.HRESULT]
    put_TextIndent: _Callable[[_type.DOUBLE],  # value
                              _type.HRESULT]


class IParagraphStatics(_inspectable.IInspectable, factory=True):
    get_TextIndentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class IRun(_inspectable.IInspectable):
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_FlowDirection: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.FlowDirection]],  # value
                                 _type.HRESULT]
    put_FlowDirection: _Callable[[_enum.Microsoft.UI.Xaml.FlowDirection],  # value
                                 _type.HRESULT]


class IRunStatics(_inspectable.IInspectable, factory=True):
    get_FlowDirectionProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]


class ISpan(_inspectable.IInspectable):
    get_Inlines: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[IInline]]],  # value
                           _type.HRESULT]
    put_Inlines: _Callable[[_Windows_Foundation_Collections.IVector[IInline]],  # value
                           _type.HRESULT]


class ISpanFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ISpan]],  # value
                              _type.HRESULT]


class ITextElement(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_FontSize: _Callable[[_Pointer[_type.DOUBLE]],  # value
                            _type.HRESULT]
    put_FontSize: _Callable[[_type.DOUBLE],  # value
                            _type.HRESULT]
    get_FontFamily: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IFontFamily]],  # value
                              _type.HRESULT]
    put_FontFamily: _Callable[[_Microsoft_UI_Xaml_Media.IFontFamily],  # value
                              _type.HRESULT]
    get_FontWeight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    put_FontWeight: _Callable[[_struct.Windows.UI.Text.FontWeight],  # value
                              _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]
    get_FontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # value
                               _type.HRESULT]
    put_FontStretch: _Callable[[_enum.Windows.UI.Text.FontStretch],  # value
                               _type.HRESULT]
    get_CharacterSpacing: _Callable[[_Pointer[_type.INT32]],  # value
                                    _type.HRESULT]
    put_CharacterSpacing: _Callable[[_type.INT32],  # value
                                    _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_Language: _Callable[[_Pointer[_type.HSTRING]],  # value
                            _type.HRESULT]
    put_Language: _Callable[[_type.HSTRING],  # value
                            _type.HRESULT]
    get_IsTextScaleFactorEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_IsTextScaleFactorEnabled: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]
    get_TextDecorations: _Callable[[_Pointer[_enum.Windows.UI.Text.TextDecorations]],  # value
                                   _type.HRESULT]
    put_TextDecorations: _Callable[[_enum.Windows.UI.Text.TextDecorations],  # value
                                   _type.HRESULT]
    get_ContentStart: _Callable[[_Pointer[ITextPointer]],  # value
                                _type.HRESULT]
    get_ContentEnd: _Callable[[_Pointer[ITextPointer]],  # value
                              _type.HRESULT]
    get_ElementStart: _Callable[[_Pointer[ITextPointer]],  # value
                                _type.HRESULT]
    get_ElementEnd: _Callable[[_Pointer[ITextPointer]],  # value
                              _type.HRESULT]
    get_AllowFocusOnInteraction: _Callable[[_Pointer[_type.boolean]],  # value
                                           _type.HRESULT]
    put_AllowFocusOnInteraction: _Callable[[_type.boolean],  # value
                                           _type.HRESULT]
    get_AccessKey: _Callable[[_Pointer[_type.HSTRING]],  # value
                             _type.HRESULT]
    put_AccessKey: _Callable[[_type.HSTRING],  # value
                             _type.HRESULT]
    get_ExitDisplayModeOnAccessKeyInvoked: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_ExitDisplayModeOnAccessKeyInvoked: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_IsAccessKeyScope: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsAccessKeyScope: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_AccessKeyScopeOwner: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                                       _type.HRESULT]
    put_AccessKeyScopeOwner: _Callable[[_Microsoft_UI_Xaml.IDependencyObject],  # value
                                       _type.HRESULT]
    get_KeyTipPlacementMode: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Input.KeyTipPlacementMode]],  # value
                                       _type.HRESULT]
    put_KeyTipPlacementMode: _Callable[[_enum.Microsoft.UI.Xaml.Input.KeyTipPlacementMode],  # value
                                       _type.HRESULT]
    get_KeyTipHorizontalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                          _type.HRESULT]
    put_KeyTipHorizontalOffset: _Callable[[_type.DOUBLE],  # value
                                          _type.HRESULT]
    get_KeyTipVerticalOffset: _Callable[[_Pointer[_type.DOUBLE]],  # value
                                        _type.HRESULT]
    put_KeyTipVerticalOffset: _Callable[[_type.DOUBLE],  # value
                                        _type.HRESULT]
    get_XamlRoot: _Callable[[_Pointer[_Microsoft_UI_Xaml.IXamlRoot]],  # value
                            _type.HRESULT]
    put_XamlRoot: _Callable[[_Microsoft_UI_Xaml.IXamlRoot],  # value
                            _type.HRESULT]
    add_AccessKeyDisplayRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextElement, _Microsoft_UI_Xaml_Input.IAccessKeyDisplayRequestedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_AccessKeyDisplayRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_AccessKeyDisplayDismissed: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextElement, _Microsoft_UI_Xaml_Input.IAccessKeyDisplayDismissedEventArgs],  # handler
                                              _Pointer[_struct.EventRegistrationToken]],  # token
                                             _type.HRESULT]
    remove_AccessKeyDisplayDismissed: _Callable[[_struct.EventRegistrationToken],  # token
                                                _type.HRESULT]
    add_AccessKeyInvoked: _Callable[[_Windows_Foundation.ITypedEventHandler[ITextElement, _Microsoft_UI_Xaml_Input.IAccessKeyInvokedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # token
                                    _type.HRESULT]
    remove_AccessKeyInvoked: _Callable[[_struct.EventRegistrationToken],  # token
                                       _type.HRESULT]
    FindName: _Callable[[_type.HSTRING,  # name
                         _Pointer[_inspectable.IInspectable]],  # result
                        _type.HRESULT]


class ITextElementFactory(_inspectable.IInspectable):
    pass


class ITextElementOverrides(_inspectable.IInspectable):
    OnDisconnectVisualChildren: _Callable[[],
                                          _type.HRESULT]


class ITextElementStatics(_inspectable.IInspectable, factory=True):
    get_FontSizeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_FontFamilyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontWeightProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_FontStyleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_FontStretchProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    get_CharacterSpacingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_ForegroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_LanguageProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    get_IsTextScaleFactorEnabledProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                    _type.HRESULT]
    get_TextDecorationsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    get_AllowFocusOnInteractionProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                   _type.HRESULT]
    get_AccessKeyProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                     _type.HRESULT]
    get_ExitDisplayModeOnAccessKeyInvokedProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                             _type.HRESULT]
    get_IsAccessKeyScopeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    get_AccessKeyScopeOwnerProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_KeyTipPlacementModeProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    get_KeyTipHorizontalOffsetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    get_KeyTipVerticalOffsetProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]


class ITextHighlighter(_inspectable.IInspectable):
    get_Ranges: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_struct.Microsoft.UI.Xaml.Documents.TextRange]]],  # value
                          _type.HRESULT]
    get_Foreground: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Foreground: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]
    get_Background: _Callable[[_Pointer[_Microsoft_UI_Xaml_Media.IBrush]],  # value
                              _type.HRESULT]
    put_Background: _Callable[[_Microsoft_UI_Xaml_Media.IBrush],  # value
                              _type.HRESULT]


class ITextHighlighterBase(_inspectable.IInspectable):
    pass


class ITextHighlighterBaseFactory(_inspectable.IInspectable):
    pass


class ITextHighlighterFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[ITextHighlighter]],  # value
                              _type.HRESULT]


class ITextHighlighterStatics(_inspectable.IInspectable, factory=True):
    get_ForegroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]
    get_BackgroundProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                      _type.HRESULT]


class ITextPointer(_inspectable.IInspectable):
    get_Parent: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyObject]],  # value
                          _type.HRESULT]
    get_VisualParent: _Callable[[_Pointer[_Microsoft_UI_Xaml.IFrameworkElement]],  # value
                                _type.HRESULT]
    get_LogicalDirection: _Callable[[_Pointer[_enum.Microsoft.UI.Xaml.Documents.LogicalDirection]],  # value
                                    _type.HRESULT]
    get_Offset: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    GetCharacterRect: _Callable[[_enum.Microsoft.UI.Xaml.Documents.LogicalDirection,  # direction
                                 _Pointer[_struct.Windows.Foundation.Rect]],  # result
                                _type.HRESULT]
    GetPositionAtOffset: _Callable[[_type.INT32,  # offset
                                    _enum.Microsoft.UI.Xaml.Documents.LogicalDirection,  # direction
                                    _Pointer[ITextPointer]],  # result
                                   _type.HRESULT]


class ITypography(_inspectable.IInspectable):
    pass


class ITypographyStatics(_inspectable.IInspectable, factory=True):
    get_AnnotationAlternatesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetAnnotationAlternates: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_type.INT32]],  # result
                                       _type.HRESULT]
    SetAnnotationAlternates: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _type.INT32],  # value
                                       _type.HRESULT]
    get_EastAsianExpertFormsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetEastAsianExpertForms: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    SetEastAsianExpertForms: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _type.boolean],  # value
                                       _type.HRESULT]
    get_EastAsianLanguageProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetEastAsianLanguage: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_enum.Microsoft.UI.Xaml.FontEastAsianLanguage]],  # result
                                    _type.HRESULT]
    SetEastAsianLanguage: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _enum.Microsoft.UI.Xaml.FontEastAsianLanguage],  # value
                                    _type.HRESULT]
    get_EastAsianWidthsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetEastAsianWidths: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                   _Pointer[_enum.Microsoft.UI.Xaml.FontEastAsianWidths]],  # result
                                  _type.HRESULT]
    SetEastAsianWidths: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                   _enum.Microsoft.UI.Xaml.FontEastAsianWidths],  # value
                                  _type.HRESULT]
    get_StandardLigaturesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetStandardLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    SetStandardLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _type.boolean],  # value
                                    _type.HRESULT]
    get_ContextualLigaturesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    GetContextualLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    SetContextualLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                       _type.boolean],  # value
                                      _type.HRESULT]
    get_DiscretionaryLigaturesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                  _type.HRESULT]
    GetDiscretionaryLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                          _Pointer[_type.boolean]],  # result
                                         _type.HRESULT]
    SetDiscretionaryLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                          _type.boolean],  # value
                                         _type.HRESULT]
    get_HistoricalLigaturesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    GetHistoricalLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                       _Pointer[_type.boolean]],  # result
                                      _type.HRESULT]
    SetHistoricalLigatures: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                       _type.boolean],  # value
                                      _type.HRESULT]
    get_StandardSwashesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetStandardSwashes: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                   _Pointer[_type.INT32]],  # result
                                  _type.HRESULT]
    SetStandardSwashes: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                   _type.INT32],  # value
                                  _type.HRESULT]
    get_ContextualSwashesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetContextualSwashes: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_type.INT32]],  # result
                                    _type.HRESULT]
    SetContextualSwashes: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _type.INT32],  # value
                                    _type.HRESULT]
    get_ContextualAlternatesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                                _type.HRESULT]
    GetContextualAlternates: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _Pointer[_type.boolean]],  # result
                                       _type.HRESULT]
    SetContextualAlternates: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                        _type.boolean],  # value
                                       _type.HRESULT]
    get_StylisticAlternatesProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                               _type.HRESULT]
    GetStylisticAlternates: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                       _Pointer[_type.INT32]],  # result
                                      _type.HRESULT]
    SetStylisticAlternates: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                       _type.INT32],  # value
                                      _type.HRESULT]
    get_StylisticSet1Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet1: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet1: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet2Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet2: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet2: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet3Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet3: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet3: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet4Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet4: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet4: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet5Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet5: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet5: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet6Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet6: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet6: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet7Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet7: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet7: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet8Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet8: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet8: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet9Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                         _type.HRESULT]
    GetStylisticSet9: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _Pointer[_type.boolean]],  # result
                                _type.HRESULT]
    SetStylisticSet9: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                 _type.boolean],  # value
                                _type.HRESULT]
    get_StylisticSet10Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet10: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet10: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet11Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet11: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet11: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet12Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet12: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet12: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet13Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet13: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet13: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet14Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet14: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet14: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet15Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet15: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet15: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet16Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet16: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet16: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet17Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet17: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet17: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet18Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet18: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet18: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet19Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet19: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet19: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_StylisticSet20Property: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetStylisticSet20: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetStylisticSet20: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_CapitalsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetCapitals: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_enum.Microsoft.UI.Xaml.FontCapitals]],  # result
                           _type.HRESULT]
    SetCapitals: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                            _enum.Microsoft.UI.Xaml.FontCapitals],  # value
                           _type.HRESULT]
    get_CapitalSpacingProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]
    GetCapitalSpacing: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _Pointer[_type.boolean]],  # result
                                 _type.HRESULT]
    SetCapitalSpacing: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                  _type.boolean],  # value
                                 _type.HRESULT]
    get_KerningProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                   _type.HRESULT]
    GetKerning: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                           _Pointer[_type.boolean]],  # result
                          _type.HRESULT]
    SetKerning: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                           _type.boolean],  # value
                          _type.HRESULT]
    get_CaseSensitiveFormsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                              _type.HRESULT]
    GetCaseSensitiveForms: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                      _Pointer[_type.boolean]],  # result
                                     _type.HRESULT]
    SetCaseSensitiveForms: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                      _type.boolean],  # value
                                     _type.HRESULT]
    get_HistoricalFormsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                           _type.HRESULT]
    GetHistoricalForms: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                   _Pointer[_type.boolean]],  # result
                                  _type.HRESULT]
    SetHistoricalForms: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                   _type.boolean],  # value
                                  _type.HRESULT]
    get_FractionProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetFraction: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_enum.Microsoft.UI.Xaml.FontFraction]],  # result
                           _type.HRESULT]
    SetFraction: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                            _enum.Microsoft.UI.Xaml.FontFraction],  # value
                           _type.HRESULT]
    get_NumeralStyleProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                        _type.HRESULT]
    GetNumeralStyle: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                _Pointer[_enum.Microsoft.UI.Xaml.FontNumeralStyle]],  # result
                               _type.HRESULT]
    SetNumeralStyle: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                _enum.Microsoft.UI.Xaml.FontNumeralStyle],  # value
                               _type.HRESULT]
    get_NumeralAlignmentProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                            _type.HRESULT]
    GetNumeralAlignment: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                    _Pointer[_enum.Microsoft.UI.Xaml.FontNumeralAlignment]],  # result
                                   _type.HRESULT]
    SetNumeralAlignment: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                    _enum.Microsoft.UI.Xaml.FontNumeralAlignment],  # value
                                   _type.HRESULT]
    get_SlashedZeroProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                       _type.HRESULT]
    GetSlashedZero: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                               _Pointer[_type.boolean]],  # result
                              _type.HRESULT]
    SetSlashedZero: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                               _type.boolean],  # value
                              _type.HRESULT]
    get_MathematicalGreekProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                             _type.HRESULT]
    GetMathematicalGreek: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _Pointer[_type.boolean]],  # result
                                    _type.HRESULT]
    SetMathematicalGreek: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                                     _type.boolean],  # value
                                    _type.HRESULT]
    get_VariantsProperty: _Callable[[_Pointer[_Microsoft_UI_Xaml.IDependencyProperty]],  # value
                                    _type.HRESULT]
    GetVariants: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                            _Pointer[_enum.Microsoft.UI.Xaml.FontVariants]],  # result
                           _type.HRESULT]
    SetVariants: _Callable[[_Microsoft_UI_Xaml.IDependencyObject,  # element
                            _enum.Microsoft.UI.Xaml.FontVariants],  # value
                           _type.HRESULT]


class IUnderline(_inspectable.IInspectable):
    pass
