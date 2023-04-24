from __future__ import annotations

from typing import Callable as _Callable

from ... import Inking as _Windows_UI_Input_Inking
from ..... import Foundation as _Windows_Foundation
from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class IInkAnalysisInkBullet(_inspectable.IInspectable):
    get_RecognizedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IInkAnalysisInkDrawing(_inspectable.IInspectable):
    get_DrawingKind: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.Analysis.InkAnalysisDrawingKind]],  # value
                               _type.HRESULT]
    get_Center: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                          _type.HRESULT]
    get_Points: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Foundation.Point]]],  # value
                          _type.HRESULT]


class IInkAnalysisInkWord(_inspectable.IInspectable):
    get_RecognizedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_TextAlternates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # value
                                  _type.HRESULT]


class IInkAnalysisLine(_inspectable.IInspectable):
    get_RecognizedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_IndentLevel: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]


class IInkAnalysisListItem(_inspectable.IInspectable):
    get_RecognizedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IInkAnalysisNode(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind]],  # value
                        _type.HRESULT]
    get_BoundingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    get_RotatedBoundingRect: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_struct.Windows.Foundation.Point]]],  # value
                                       _type.HRESULT]
    get_Children: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkAnalysisNode]]],  # value
                            _type.HRESULT]
    get_Parent: _Callable[[_Pointer[IInkAnalysisNode]],  # value
                          _type.HRESULT]
    GetStrokeIds: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # strokeIds
                            _type.HRESULT]


class IInkAnalysisParagraph(_inspectable.IInspectable):
    get_RecognizedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IInkAnalysisResult(_inspectable.IInspectable):
    get_Status: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.Analysis.InkAnalysisStatus]],  # value
                          _type.HRESULT]


class IInkAnalysisRoot(_inspectable.IInspectable):
    get_RecognizedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    FindNodes: _Callable[[_enum.Windows.UI.Input.Inking.Analysis.InkAnalysisNodeKind,  # nodeKind
                          _Pointer[_Windows_Foundation_Collections.IVectorView[IInkAnalysisNode]]],  # result
                         _type.HRESULT]


class IInkAnalysisWritingRegion(_inspectable.IInspectable):
    get_RecognizedText: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]


class IInkAnalyzer(_inspectable.IInspectable):
    get_AnalysisRoot: _Callable[[_Pointer[IInkAnalysisRoot]],  # value
                                _type.HRESULT]
    get_IsAnalyzing: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    AddDataForStroke: _Callable[[_Windows_UI_Input_Inking.IInkStroke],  # stroke
                                _type.HRESULT]
    AddDataForStrokes: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_UI_Input_Inking.IInkStroke]],  # strokes
                                 _type.HRESULT]
    ClearDataForAllStrokes: _Callable[[],
                                      _type.HRESULT]
    RemoveDataForStroke: _Callable[[_type.UINT32],  # strokeId
                                   _type.HRESULT]
    RemoveDataForStrokes: _Callable[[_Windows_Foundation_Collections.IIterable[_type.UINT32]],  # strokeIds
                                    _type.HRESULT]
    ReplaceDataForStroke: _Callable[[_Windows_UI_Input_Inking.IInkStroke],  # stroke
                                    _type.HRESULT]
    SetStrokeDataKind: _Callable[[_type.UINT32,  # strokeId
                                  _enum.Windows.UI.Input.Inking.Analysis.InkAnalysisStrokeKind],  # strokeKind
                                 _type.HRESULT]
    AnalyzeAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[IInkAnalysisResult]]],  # result
                            _type.HRESULT]


class IInkAnalyzerFactory(_inspectable.IInspectable):
    CreateAnalyzer: _Callable[[_Pointer[IInkAnalyzer]],  # result
                              _type.HRESULT]
