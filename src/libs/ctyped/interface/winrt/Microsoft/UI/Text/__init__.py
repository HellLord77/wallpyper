from __future__ import annotations as _

from typing import Callable as _Callable

from .... import inspectable as _inspectable
from ....Windows.Storage import Streams as _Windows_Storage_Streams
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IFontWeights(_inspectable.IInspectable):
    pass


class IFontWeightsStatics(_inspectable.IInspectable):
    get_Black: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                         _type.HRESULT]
    get_Bold: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                        _type.HRESULT]
    get_ExtraBlack: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    get_ExtraBold: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                             _type.HRESULT]
    get_ExtraLight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                              _type.HRESULT]
    get_Light: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                         _type.HRESULT]
    get_Medium: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                          _type.HRESULT]
    get_Normal: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                          _type.HRESULT]
    get_SemiBold: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                            _type.HRESULT]
    get_SemiLight: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                             _type.HRESULT]
    get_Thin: _Callable[[_Pointer[_struct.Windows.UI.Text.FontWeight]],  # value
                        _type.HRESULT]


class ITextCharacterFormat(_inspectable.IInspectable):
    get_AllCaps: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                           _type.HRESULT]
    put_AllCaps: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                           _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_Bold: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                        _type.HRESULT]
    put_Bold: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                        _type.HRESULT]
    get_FontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # value
                               _type.HRESULT]
    put_FontStretch: _Callable[[_enum.Windows.UI.Text.FontStretch],  # value
                               _type.HRESULT]
    get_FontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                             _type.HRESULT]
    put_FontStyle: _Callable[[_enum.Windows.UI.Text.FontStyle],  # value
                             _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_ForegroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_Hidden: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                          _type.HRESULT]
    put_Hidden: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                          _type.HRESULT]
    get_Italic: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                          _type.HRESULT]
    put_Italic: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                          _type.HRESULT]
    get_Kerning: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    put_Kerning: _Callable[[_type.FLOAT],  # value
                           _type.HRESULT]
    get_LanguageTag: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    put_LanguageTag: _Callable[[_type.HSTRING],  # value
                               _type.HRESULT]
    get_LinkType: _Callable[[_Pointer[_enum.Microsoft.UI.Text.LinkType]],  # value
                            _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Name: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_Outline: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                           _type.HRESULT]
    put_Outline: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                           _type.HRESULT]
    get_Position: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    put_Position: _Callable[[_type.FLOAT],  # value
                            _type.HRESULT]
    get_ProtectedText: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                                 _type.HRESULT]
    put_ProtectedText: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                                 _type.HRESULT]
    get_Size: _Callable[[_Pointer[_type.FLOAT]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_type.FLOAT],  # value
                        _type.HRESULT]
    get_SmallCaps: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                             _type.HRESULT]
    put_SmallCaps: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                             _type.HRESULT]
    get_Spacing: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    put_Spacing: _Callable[[_type.FLOAT],  # value
                           _type.HRESULT]
    get_Strikethrough: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                                 _type.HRESULT]
    put_Strikethrough: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                                 _type.HRESULT]
    get_Subscript: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                             _type.HRESULT]
    put_Subscript: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                             _type.HRESULT]
    get_Superscript: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                               _type.HRESULT]
    put_Superscript: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                               _type.HRESULT]
    get_TextScript: _Callable[[_Pointer[_enum.Microsoft.UI.Text.TextScript]],  # value
                              _type.HRESULT]
    put_TextScript: _Callable[[_enum.Microsoft.UI.Text.TextScript],  # value
                              _type.HRESULT]
    get_Underline: _Callable[[_Pointer[_enum.Microsoft.UI.Text.UnderlineType]],  # value
                             _type.HRESULT]
    put_Underline: _Callable[[_enum.Microsoft.UI.Text.UnderlineType],  # value
                             _type.HRESULT]
    get_Weight: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    put_Weight: _Callable[[_type.INT32],  # value
                          _type.HRESULT]
    SetClone: _Callable[[ITextCharacterFormat],  # value
                        _type.HRESULT]
    GetClone: _Callable[[_Pointer[ITextCharacterFormat]],  # result
                        _type.HRESULT]
    IsEqual: _Callable[[ITextCharacterFormat,  # format
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]


class ITextConstantsStatics(_inspectable.IInspectable):
    get_AutoColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                             _type.HRESULT]
    get_MinUnitCount: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_MaxUnitCount: _Callable[[_Pointer[_type.INT32]],  # value
                                _type.HRESULT]
    get_UndefinedColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                  _type.HRESULT]
    get_UndefinedFloatValue: _Callable[[_Pointer[_type.FLOAT]],  # value
                                       _type.HRESULT]
    get_UndefinedInt32Value: _Callable[[_Pointer[_type.INT32]],  # value
                                       _type.HRESULT]
    get_UndefinedFontStretch: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStretch]],  # value
                                        _type.HRESULT]
    get_UndefinedFontStyle: _Callable[[_Pointer[_enum.Windows.UI.Text.FontStyle]],  # value
                                      _type.HRESULT]


class ITextDocument(_inspectable.IInspectable):
    get_CaretType: _Callable[[_Pointer[_enum.Microsoft.UI.Text.CaretType]],  # value
                             _type.HRESULT]
    put_CaretType: _Callable[[_enum.Microsoft.UI.Text.CaretType],  # value
                             _type.HRESULT]
    get_DefaultTabStop: _Callable[[_Pointer[_type.FLOAT]],  # value
                                  _type.HRESULT]
    put_DefaultTabStop: _Callable[[_type.FLOAT],  # value
                                  _type.HRESULT]
    get_Selection: _Callable[[_Pointer[ITextSelection]],  # value
                             _type.HRESULT]
    get_UndoLimit: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    put_UndoLimit: _Callable[[_type.UINT32],  # value
                             _type.HRESULT]
    CanCopy: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    CanPaste: _Callable[[_Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    CanRedo: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    CanUndo: _Callable[[_Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    ApplyDisplayUpdates: _Callable[[_Pointer[_type.INT32]],  # result
                                   _type.HRESULT]
    BatchDisplayUpdates: _Callable[[_Pointer[_type.INT32]],  # result
                                   _type.HRESULT]
    BeginUndoGroup: _Callable[[],
                              _type.HRESULT]
    EndUndoGroup: _Callable[[],
                            _type.HRESULT]
    GetDefaultCharacterFormat: _Callable[[_Pointer[ITextCharacterFormat]],  # result
                                         _type.HRESULT]
    GetDefaultParagraphFormat: _Callable[[_Pointer[ITextParagraphFormat]],  # result
                                         _type.HRESULT]
    GetRange: _Callable[[_type.INT32,  # startPosition
                         _type.INT32,  # endPosition
                         _Pointer[ITextRange]],  # result
                        _type.HRESULT]
    GetRangeFromPoint: _Callable[[_struct.Windows.Foundation.Point,  # point
                                  _enum.Microsoft.UI.Text.PointOptions,  # options
                                  _Pointer[ITextRange]],  # result
                                 _type.HRESULT]
    GetText: _Callable[[_enum.Microsoft.UI.Text.TextGetOptions,  # options
                        _Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    LoadFromStream: _Callable[[_enum.Microsoft.UI.Text.TextSetOptions,  # options
                               _Windows_Storage_Streams.IRandomAccessStream],  # value
                              _type.HRESULT]
    Redo: _Callable[[],
                    _type.HRESULT]
    SaveToStream: _Callable[[_enum.Microsoft.UI.Text.TextGetOptions,  # options
                             _Windows_Storage_Streams.IRandomAccessStream],  # value
                            _type.HRESULT]
    SetDefaultCharacterFormat: _Callable[[ITextCharacterFormat],  # value
                                         _type.HRESULT]
    SetDefaultParagraphFormat: _Callable[[ITextParagraphFormat],  # value
                                         _type.HRESULT]
    SetText: _Callable[[_enum.Microsoft.UI.Text.TextSetOptions,  # options
                        _type.HSTRING],  # value
                       _type.HRESULT]
    Undo: _Callable[[],
                    _type.HRESULT]
    get_AlignmentIncludesTrailingWhitespace: _Callable[[_Pointer[_type.boolean]],  # value
                                                       _type.HRESULT]
    put_AlignmentIncludesTrailingWhitespace: _Callable[[_type.boolean],  # value
                                                       _type.HRESULT]
    get_IgnoreTrailingCharacterSpacing: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_IgnoreTrailingCharacterSpacing: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    ClearUndoRedoHistory: _Callable[[],
                                    _type.HRESULT]


class ITextParagraphFormat(_inspectable.IInspectable):
    get_Alignment: _Callable[[_Pointer[_enum.Microsoft.UI.Text.ParagraphAlignment]],  # value
                             _type.HRESULT]
    put_Alignment: _Callable[[_enum.Microsoft.UI.Text.ParagraphAlignment],  # value
                             _type.HRESULT]
    get_FirstLineIndent: _Callable[[_Pointer[_type.FLOAT]],  # value
                                   _type.HRESULT]
    get_KeepTogether: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                                _type.HRESULT]
    put_KeepTogether: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                                _type.HRESULT]
    get_KeepWithNext: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                                _type.HRESULT]
    put_KeepWithNext: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                                _type.HRESULT]
    get_LeftIndent: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    get_LineSpacing: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    get_LineSpacingRule: _Callable[[_Pointer[_enum.Microsoft.UI.Text.LineSpacingRule]],  # value
                                   _type.HRESULT]
    get_ListAlignment: _Callable[[_Pointer[_enum.Microsoft.UI.Text.MarkerAlignment]],  # value
                                 _type.HRESULT]
    put_ListAlignment: _Callable[[_enum.Microsoft.UI.Text.MarkerAlignment],  # value
                                 _type.HRESULT]
    get_ListLevelIndex: _Callable[[_Pointer[_type.INT32]],  # value
                                  _type.HRESULT]
    put_ListLevelIndex: _Callable[[_type.INT32],  # value
                                  _type.HRESULT]
    get_ListStart: _Callable[[_Pointer[_type.INT32]],  # value
                             _type.HRESULT]
    put_ListStart: _Callable[[_type.INT32],  # value
                             _type.HRESULT]
    get_ListStyle: _Callable[[_Pointer[_enum.Microsoft.UI.Text.MarkerStyle]],  # value
                             _type.HRESULT]
    put_ListStyle: _Callable[[_enum.Microsoft.UI.Text.MarkerStyle],  # value
                             _type.HRESULT]
    get_ListTab: _Callable[[_Pointer[_type.FLOAT]],  # value
                           _type.HRESULT]
    put_ListTab: _Callable[[_type.FLOAT],  # value
                           _type.HRESULT]
    get_ListType: _Callable[[_Pointer[_enum.Microsoft.UI.Text.MarkerType]],  # value
                            _type.HRESULT]
    put_ListType: _Callable[[_enum.Microsoft.UI.Text.MarkerType],  # value
                            _type.HRESULT]
    get_NoLineNumber: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                                _type.HRESULT]
    put_NoLineNumber: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                                _type.HRESULT]
    get_PageBreakBefore: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                                   _type.HRESULT]
    put_PageBreakBefore: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                                   _type.HRESULT]
    get_RightIndent: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_RightIndent: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_RightToLeft: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                               _type.HRESULT]
    put_RightToLeft: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                               _type.HRESULT]
    get_Style: _Callable[[_Pointer[_enum.Microsoft.UI.Text.ParagraphStyle]],  # value
                         _type.HRESULT]
    put_Style: _Callable[[_enum.Microsoft.UI.Text.ParagraphStyle],  # value
                         _type.HRESULT]
    get_SpaceAfter: _Callable[[_Pointer[_type.FLOAT]],  # value
                              _type.HRESULT]
    put_SpaceAfter: _Callable[[_type.FLOAT],  # value
                              _type.HRESULT]
    get_SpaceBefore: _Callable[[_Pointer[_type.FLOAT]],  # value
                               _type.HRESULT]
    put_SpaceBefore: _Callable[[_type.FLOAT],  # value
                               _type.HRESULT]
    get_WidowControl: _Callable[[_Pointer[_enum.Microsoft.UI.Text.FormatEffect]],  # value
                                _type.HRESULT]
    put_WidowControl: _Callable[[_enum.Microsoft.UI.Text.FormatEffect],  # value
                                _type.HRESULT]
    get_TabCount: _Callable[[_Pointer[_type.INT32]],  # value
                            _type.HRESULT]
    AddTab: _Callable[[_type.FLOAT,  # position
                       _enum.Microsoft.UI.Text.TabAlignment,  # align
                       _enum.Microsoft.UI.Text.TabLeader],  # leader
                      _type.HRESULT]
    ClearAllTabs: _Callable[[],
                            _type.HRESULT]
    DeleteTab: _Callable[[_type.FLOAT],  # position
                         _type.HRESULT]
    GetClone: _Callable[[_Pointer[ITextParagraphFormat]],  # result
                        _type.HRESULT]
    GetTab: _Callable[[_type.INT32,  # index
                       _Pointer[_type.FLOAT],  # position
                       _Pointer[_enum.Microsoft.UI.Text.TabAlignment],  # align
                       _Pointer[_enum.Microsoft.UI.Text.TabLeader]],  # leader
                      _type.HRESULT]
    IsEqual: _Callable[[ITextParagraphFormat,  # format
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    SetClone: _Callable[[ITextParagraphFormat],  # format
                        _type.HRESULT]
    SetIndents: _Callable[[_type.FLOAT,  # start
                           _type.FLOAT,  # left
                           _type.FLOAT],  # right
                          _type.HRESULT]
    SetLineSpacing: _Callable[[_enum.Microsoft.UI.Text.LineSpacingRule,  # rule
                               _type.FLOAT],  # spacing
                              _type.HRESULT]


class ITextRange(_inspectable.IInspectable):
    get_Character: _Callable[[_Pointer[_type.WCHAR]],  # value
                             _type.HRESULT]
    put_Character: _Callable[[_type.WCHAR],  # value
                             _type.HRESULT]
    get_CharacterFormat: _Callable[[_Pointer[ITextCharacterFormat]],  # value
                                   _type.HRESULT]
    put_CharacterFormat: _Callable[[ITextCharacterFormat],  # value
                                   _type.HRESULT]
    get_FormattedText: _Callable[[_Pointer[ITextRange]],  # value
                                 _type.HRESULT]
    put_FormattedText: _Callable[[ITextRange],  # value
                                 _type.HRESULT]
    get_EndPosition: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    put_EndPosition: _Callable[[_type.INT32],  # value
                               _type.HRESULT]
    get_Gravity: _Callable[[_Pointer[_enum.Microsoft.UI.Text.RangeGravity]],  # value
                           _type.HRESULT]
    put_Gravity: _Callable[[_enum.Microsoft.UI.Text.RangeGravity],  # value
                           _type.HRESULT]
    get_Length: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_Link: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Link: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    get_ParagraphFormat: _Callable[[_Pointer[ITextParagraphFormat]],  # value
                                   _type.HRESULT]
    put_ParagraphFormat: _Callable[[ITextParagraphFormat],  # value
                                   _type.HRESULT]
    get_StartPosition: _Callable[[_Pointer[_type.INT32]],  # value
                                 _type.HRESULT]
    put_StartPosition: _Callable[[_type.INT32],  # value
                                 _type.HRESULT]
    get_StoryLength: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_Text: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    put_Text: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
    CanPaste: _Callable[[_type.INT32,  # format
                         _Pointer[_type.boolean]],  # result
                        _type.HRESULT]
    ChangeCase: _Callable[[_enum.Microsoft.UI.Text.LetterCase],  # value
                          _type.HRESULT]
    Collapse: _Callable[[_type.boolean],  # value
                        _type.HRESULT]
    Copy: _Callable[[],
                    _type.HRESULT]
    Cut: _Callable[[],
                   _type.HRESULT]
    Delete: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                       _type.INT32,  # count
                       _Pointer[_type.INT32]],  # result
                      _type.HRESULT]
    EndOf: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                      _type.boolean,  # extend
                      _Pointer[_type.INT32]],  # result
                     _type.HRESULT]
    Expand: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                       _Pointer[_type.INT32]],  # result
                      _type.HRESULT]
    FindText: _Callable[[_type.HSTRING,  # value
                         _type.INT32,  # scanLength
                         _enum.Microsoft.UI.Text.FindOptions,  # options
                         _Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    GetCharacterUtf32: _Callable[[_Pointer[_type.UINT32],  # value
                                  _type.INT32],  # offset
                                 _type.HRESULT]
    GetClone: _Callable[[_Pointer[ITextRange]],  # result
                        _type.HRESULT]
    GetIndex: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                         _Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    GetPoint: _Callable[[_enum.Microsoft.UI.Text.HorizontalCharacterAlignment,  # horizontalAlign
                         _enum.Microsoft.UI.Text.VerticalCharacterAlignment,  # verticalAlign
                         _enum.Microsoft.UI.Text.PointOptions,  # options
                         _Pointer[_struct.Windows.Foundation.Point]],  # point
                        _type.HRESULT]
    GetRect: _Callable[[_enum.Microsoft.UI.Text.PointOptions,  # options
                        _Pointer[_struct.Windows.Foundation.Rect],  # rect
                        _Pointer[_type.INT32]],  # hit
                       _type.HRESULT]
    GetText: _Callable[[_enum.Microsoft.UI.Text.TextGetOptions,  # options
                        _Pointer[_type.HSTRING]],  # value
                       _type.HRESULT]
    GetTextViaStream: _Callable[[_enum.Microsoft.UI.Text.TextGetOptions,  # options
                                 _Windows_Storage_Streams.IRandomAccessStream],  # value
                                _type.HRESULT]
    InRange: _Callable[[ITextRange,  # range
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    InsertImage: _Callable[[_type.INT32,  # width
                            _type.INT32,  # height
                            _type.INT32,  # ascent
                            _enum.Microsoft.UI.Text.VerticalCharacterAlignment,  # verticalAlign
                            _type.HSTRING,  # alternateText
                            _Windows_Storage_Streams.IRandomAccessStream],  # value
                           _type.HRESULT]
    InStory: _Callable[[ITextRange,  # range
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    IsEqual: _Callable[[ITextRange,  # range
                        _Pointer[_type.boolean]],  # result
                       _type.HRESULT]
    Move: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                     _type.INT32,  # count
                     _Pointer[_type.INT32]],  # result
                    _type.HRESULT]
    MoveEnd: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                        _type.INT32,  # count
                        _Pointer[_type.INT32]],  # result
                       _type.HRESULT]
    MoveStart: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                          _type.INT32,  # count
                          _Pointer[_type.INT32]],  # result
                         _type.HRESULT]
    Paste: _Callable[[_type.INT32],  # format
                     _type.HRESULT]
    ScrollIntoView: _Callable[[_enum.Microsoft.UI.Text.PointOptions],  # value
                              _type.HRESULT]
    MatchSelection: _Callable[[],
                              _type.HRESULT]
    SetIndex: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                         _type.INT32,  # index
                         _type.boolean],  # extend
                        _type.HRESULT]
    SetPoint: _Callable[[_struct.Windows.Foundation.Point,  # point
                         _enum.Microsoft.UI.Text.PointOptions,  # options
                         _type.boolean],  # extend
                        _type.HRESULT]
    SetRange: _Callable[[_type.INT32,  # startPosition
                         _type.INT32],  # endPosition
                        _type.HRESULT]
    SetText: _Callable[[_enum.Microsoft.UI.Text.TextSetOptions,  # options
                        _type.HSTRING],  # value
                       _type.HRESULT]
    SetTextViaStream: _Callable[[_enum.Microsoft.UI.Text.TextSetOptions,  # options
                                 _Windows_Storage_Streams.IRandomAccessStream],  # value
                                _type.HRESULT]
    StartOf: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                        _type.boolean,  # extend
                        _Pointer[_type.INT32]],  # result
                       _type.HRESULT]


class ITextSelection(_inspectable.IInspectable):
    get_Options: _Callable[[_Pointer[_enum.Microsoft.UI.Text.SelectionOptions]],  # value
                           _type.HRESULT]
    put_Options: _Callable[[_enum.Microsoft.UI.Text.SelectionOptions],  # value
                           _type.HRESULT]
    get_Type: _Callable[[_Pointer[_enum.Microsoft.UI.Text.SelectionType]],  # value
                        _type.HRESULT]
    EndKey: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                       _type.boolean,  # extend
                       _Pointer[_type.INT32]],  # result
                      _type.HRESULT]
    HomeKey: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                        _type.boolean,  # extend
                        _Pointer[_type.INT32]],  # result
                       _type.HRESULT]
    MoveDown: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                         _type.INT32,  # count
                         _type.boolean,  # extend
                         _Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    MoveLeft: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                         _type.INT32,  # count
                         _type.boolean,  # extend
                         _Pointer[_type.INT32]],  # result
                        _type.HRESULT]
    MoveRight: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                          _type.INT32,  # count
                          _type.boolean,  # extend
                          _Pointer[_type.INT32]],  # result
                         _type.HRESULT]
    MoveUp: _Callable[[_enum.Microsoft.UI.Text.TextRangeUnit,  # unit
                       _type.INT32,  # count
                       _type.boolean,  # extend
                       _Pointer[_type.INT32]],  # result
                      _type.HRESULT]
    TypeText: _Callable[[_type.HSTRING],  # value
                        _type.HRESULT]
