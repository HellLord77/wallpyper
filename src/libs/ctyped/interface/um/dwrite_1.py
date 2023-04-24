from __future__ import annotations

from typing import Callable as _Callable

from . import dwrite as _dwrite
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IDWriteFactory1(_dwrite.IDWriteFactory):
    GetEudcFontCollection: _Callable[[_Pointer[_dwrite.IDWriteFontCollection],  # fontCollection
                                      _type.BOOL],  # checkForUpdates
                                     _type.HRESULT]
    CreateCustomRenderingParams_: _Callable[[_type.FLOAT,  # gamma
                                             _type.FLOAT,  # enhancedContrast
                                             _type.FLOAT,  # enhancedContrastGrayscale
                                             _type.FLOAT,  # clearTypeLevel
                                             _enum.DWRITE_PIXEL_GEOMETRY,  # pixelGeometry
                                             _enum.DWRITE_RENDERING_MODE,  # renderingMode
                                             _Pointer[IDWriteRenderingParams1]],  # renderingParams
                                            _type.HRESULT]


class IDWriteFontFace1(_dwrite.IDWriteFontFace):
    GetMetrics_: _Callable[[_Pointer[_struct.DWRITE_FONT_METRICS1]],  # fontMetrics
                           _type.c_void]
    GetGdiCompatibleMetrics_: _Callable[[_type.FLOAT,  # emSize
                                         _type.FLOAT,  # pixelsPerDip
                                         _Pointer[_struct.DWRITE_MATRIX],  # transform
                                         _Pointer[_struct.DWRITE_FONT_METRICS1]],  # fontMetrics
                                        _type.HRESULT]
    GetCaretMetrics: _Callable[[_Pointer[_struct.DWRITE_CARET_METRICS]],  # caretMetrics
                               _type.c_void]
    GetUnicodeRanges: _Callable[[_type.UINT32,  # maxRangeCount
                                 _Pointer[_struct.DWRITE_UNICODE_RANGE],  # unicodeRanges
                                 _Pointer[_type.UINT32]],  # actualRangeCount
                                _type.HRESULT]
    IsMonospacedFont: _Callable[[],
                                _type.BOOL]
    GetDesignGlyphAdvances: _Callable[[_type.UINT32,  # glyphCount
                                       _Pointer[_type.UINT16],  # glyphIndices
                                       _Pointer[_type.INT32],  # glyphAdvances
                                       _type.BOOL],  # isSideways
                                      _type.HRESULT]
    GetGdiCompatibleGlyphAdvances: _Callable[[_type.FLOAT,  # emSize
                                              _type.FLOAT,  # pixelsPerDip
                                              _Pointer[_struct.DWRITE_MATRIX],  # transform
                                              _type.BOOL,  # useGdiNatural
                                              _type.BOOL,  # isSideways
                                              _type.UINT32,  # glyphCount
                                              _Pointer[_type.UINT16],  # glyphIndices
                                              _Pointer[_type.INT32]],  # glyphAdvances
                                             _type.HRESULT]
    GetKerningPairAdjustments: _Callable[[_type.UINT32,  # glyphCount
                                          _Pointer[_type.UINT16],  # glyphIndices
                                          _Pointer[_type.INT32]],  # glyphAdvanceAdjustments
                                         _type.HRESULT]
    HasKerningPairs: _Callable[[],
                               _type.BOOL]
    GetRecommendedRenderingMode_: _Callable[[_type.FLOAT,  # fontEmSize
                                             _type.FLOAT,  # dpiX
                                             _type.FLOAT,  # dpiY
                                             _Pointer[_struct.DWRITE_MATRIX],  # transform
                                             _type.BOOL,  # isSideways
                                             _enum.DWRITE_OUTLINE_THRESHOLD,  # outlineThreshold
                                             _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                             _Pointer[_enum.DWRITE_RENDERING_MODE]],  # renderingMode
                                            _type.HRESULT]
    GetVerticalGlyphVariants: _Callable[[_type.UINT32,  # glyphCount
                                         _Pointer[_type.UINT16],  # nominalGlyphIndices
                                         _Pointer[_type.UINT16]],  # verticalGlyphIndices
                                        _type.HRESULT]
    HasVerticalGlyphVariants: _Callable[[],
                                        _type.BOOL]


class IDWriteFont1(_dwrite.IDWriteFont):
    GetMetrics_: _Callable[[_Pointer[_struct.DWRITE_FONT_METRICS1]],  # fontMetrics
                           _type.c_void]
    GetPanose: _Callable[[_Pointer[_union.DWRITE_PANOSE]],  # panose
                         _type.c_void]
    GetUnicodeRanges: _Callable[[_type.UINT32,  # maxRangeCount
                                 _Pointer[_struct.DWRITE_UNICODE_RANGE],  # unicodeRanges
                                 _Pointer[_type.UINT32]],  # actualRangeCount
                                _type.HRESULT]
    IsMonospacedFont: _Callable[[],
                                _type.BOOL]


class IDWriteRenderingParams1(_dwrite.IDWriteRenderingParams):
    GetGrayscaleEnhancedContrast: _Callable[[],
                                            _type.FLOAT]


class IDWriteTextAnalyzer1(_dwrite.IDWriteTextAnalyzer):
    ApplyCharacterSpacing: _Callable[[_type.FLOAT,  # leadingSpacing
                                      _type.FLOAT,  # trailingSpacing
                                      _type.FLOAT,  # minimumAdvanceWidth
                                      _type.UINT32,  # textLength
                                      _type.UINT32,  # glyphCount
                                      _Pointer[_type.UINT16],  # clusterMap
                                      _Pointer[_type.FLOAT],  # glyphAdvances
                                      _Pointer[_struct.DWRITE_GLYPH_OFFSET],  # glyphOffsets
                                      _Pointer[_struct.DWRITE_SHAPING_GLYPH_PROPERTIES],  # glyphProperties
                                      _Pointer[_type.FLOAT],  # modifiedGlyphAdvances
                                      _Pointer[_struct.DWRITE_GLYPH_OFFSET]],  # modifiedGlyphOffsets
                                     _type.HRESULT]
    GetBaseline: _Callable[[_dwrite.IDWriteFontFace,  # fontFace
                            _enum.DWRITE_BASELINE,  # baseline
                            _type.BOOL,  # isVertical
                            _type.BOOL,  # isSimulationAllowed
                            _struct.DWRITE_SCRIPT_ANALYSIS,  # scriptAnalysis
                            _type.LPWSTR,  # localeName
                            _Pointer[_type.INT32],  # baselineCoordinate
                            _Pointer[_type.BOOL]],  # exists
                           _type.HRESULT]
    AnalyzeVerticalGlyphOrientation: _Callable[[IDWriteTextAnalysisSource1,  # analysisSource
                                                _type.UINT32,  # textPosition
                                                _type.UINT32,  # textLength
                                                IDWriteTextAnalysisSink1],  # analysisSink
                                               _type.HRESULT]
    GetGlyphOrientationTransform: _Callable[[_enum.DWRITE_GLYPH_ORIENTATION_ANGLE,  # glyphOrientationAngle
                                             _type.BOOL,  # isSideways
                                             _Pointer[_struct.DWRITE_MATRIX]],  # transform
                                            _type.HRESULT]
    GetScriptProperties: _Callable[[_struct.DWRITE_SCRIPT_ANALYSIS,  # scriptAnalysis
                                    _Pointer[_struct.DWRITE_SCRIPT_PROPERTIES]],  # scriptProperties
                                   _type.HRESULT]
    GetTextComplexity: _Callable[[_type.LPWSTR,  # textString
                                  _type.UINT32,  # textLength
                                  _dwrite.IDWriteFontFace,  # fontFace
                                  _Pointer[_type.BOOL],  # isTextSimple
                                  _Pointer[_type.UINT32],  # textLengthRead
                                  _Pointer[_type.UINT16]],  # glyphIndices
                                 _type.HRESULT]
    GetJustificationOpportunities: _Callable[[_dwrite.IDWriteFontFace,  # fontFace
                                              _type.FLOAT,  # fontEmSize
                                              _struct.DWRITE_SCRIPT_ANALYSIS,  # scriptAnalysis
                                              _type.UINT32,  # textLength
                                              _type.UINT32,  # glyphCount
                                              _type.LPWSTR,  # textString
                                              _Pointer[_type.UINT16],  # clusterMap
                                              _Pointer[_struct.DWRITE_SHAPING_GLYPH_PROPERTIES],  # glyphProperties
                                              _Pointer[_struct.DWRITE_JUSTIFICATION_OPPORTUNITY]],  # justificationOpportunities
                                             _type.HRESULT]
    JustifyGlyphAdvances: _Callable[[_type.FLOAT,  # lineWidth
                                     _type.UINT32,  # glyphCount
                                     _Pointer[_struct.DWRITE_JUSTIFICATION_OPPORTUNITY],  # justificationOpportunities
                                     _Pointer[_type.FLOAT],  # glyphAdvances
                                     _Pointer[_struct.DWRITE_GLYPH_OFFSET],  # glyphOffsets
                                     _Pointer[_type.FLOAT],  # justifiedGlyphAdvances
                                     _Pointer[_struct.DWRITE_GLYPH_OFFSET]],  # justifiedGlyphOffsets
                                    _type.HRESULT]
    GetJustifiedGlyphs: _Callable[[_dwrite.IDWriteFontFace,  # fontFace
                                   _type.FLOAT,  # fontEmSize
                                   _struct.DWRITE_SCRIPT_ANALYSIS,  # scriptAnalysis
                                   _type.UINT32,  # textLength
                                   _type.UINT32,  # glyphCount
                                   _type.UINT32,  # maxGlyphCount
                                   _Pointer[_type.UINT16],  # clusterMap
                                   _Pointer[_type.UINT16],  # glyphIndices
                                   _Pointer[_type.FLOAT],  # glyphAdvances
                                   _Pointer[_type.FLOAT],  # justifiedGlyphAdvances
                                   _Pointer[_struct.DWRITE_GLYPH_OFFSET],  # justifiedGlyphOffsets
                                   _Pointer[_struct.DWRITE_SHAPING_GLYPH_PROPERTIES],  # glyphProperties
                                   _Pointer[_type.UINT32],  # actualGlyphCount
                                   _Pointer[_type.UINT16],  # modifiedClusterMap
                                   _Pointer[_type.UINT16],  # modifiedGlyphIndices
                                   _Pointer[_type.FLOAT],  # modifiedGlyphAdvances
                                   _Pointer[_struct.DWRITE_GLYPH_OFFSET]],  # modifiedGlyphOffsets
                                  _type.HRESULT]


class IDWriteTextAnalysisSource1(_dwrite.IDWriteTextAnalysisSource):
    GetVerticalGlyphOrientation: _Callable[[_type.UINT32,  # textPosition
                                            _Pointer[_type.UINT32],  # textLength
                                            _Pointer[_enum.DWRITE_VERTICAL_GLYPH_ORIENTATION],  # glyphOrientation
                                            _Pointer[_type.UINT8]],  # bidiLevel
                                           _type.HRESULT]


class IDWriteTextAnalysisSink1(_dwrite.IDWriteTextAnalysisSink):
    SetGlyphOrientation: _Callable[[_type.UINT32,  # textPosition
                                    _type.UINT32,  # textLength
                                    _enum.DWRITE_GLYPH_ORIENTATION_ANGLE,  # glyphOrientationAngle
                                    _type.UINT8,  # adjustedBidiLevel
                                    _type.BOOL,  # isSideways
                                    _type.BOOL],  # isRightToLeft
                                   _type.HRESULT]


class IDWriteTextLayout1(_dwrite.IDWriteTextLayout):
    SetPairKerning: _Callable[[_type.BOOL,  # isPairKerningEnabled
                               _struct.DWRITE_TEXT_RANGE],  # textRange
                              _type.HRESULT]
    GetPairKerning: _Callable[[_type.UINT32,  # currentPosition
                               _Pointer[_type.BOOL],  # isPairKerningEnabled
                               _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                              _type.HRESULT]
    SetCharacterSpacing: _Callable[[_type.FLOAT,  # leadingSpacing
                                    _type.FLOAT,  # trailingSpacing
                                    _type.FLOAT,  # minimumAdvanceWidth
                                    _struct.DWRITE_TEXT_RANGE],  # textRange
                                   _type.HRESULT]
    GetCharacterSpacing: _Callable[[_type.UINT32,  # currentPosition
                                    _Pointer[_type.FLOAT],  # leadingSpacing
                                    _Pointer[_type.FLOAT],  # trailingSpacing
                                    _Pointer[_type.FLOAT],  # minimumAdvanceWidth
                                    _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                   _type.HRESULT]


class IDWriteBitmapRenderTarget1(_dwrite.IDWriteBitmapRenderTarget):
    GetTextAntialiasMode: _Callable[[],
                                    _enum.DWRITE_TEXT_ANTIALIAS_MODE]
    SetTextAntialiasMode: _Callable[[_enum.DWRITE_TEXT_ANTIALIAS_MODE],  # antialiasMode
                                    _type.HRESULT]
