from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import d2d1 as _d2d1
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDWriteFontFileLoader(_Unknwnbase.IUnknown):
    CreateStreamFromKey: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                    _type.UINT32,  # fontFileReferenceKeySize
                                    _Pointer[IDWriteFontFileStream]],  # fontFileStream
                                   _type.HRESULT]


class IDWriteLocalFontFileLoader(IDWriteFontFileLoader):
    GetFilePathLengthFromKey: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                         _type.UINT32,  # fontFileReferenceKeySize
                                         _Pointer[_type.UINT32]],  # filePathLength
                                        _type.HRESULT]
    GetFilePathFromKey: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                   _type.UINT32,  # fontFileReferenceKeySize
                                   _type.LPWSTR,  # filePath
                                   _type.UINT32],  # filePathSize
                                  _type.HRESULT]
    GetLastWriteTimeFromKey: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                        _type.UINT32,  # fontFileReferenceKeySize
                                        _Pointer[_struct.FILETIME]],  # lastWriteTime
                                       _type.HRESULT]


class IDWriteFontFileStream(_Unknwnbase.IUnknown):
    ReadFileFragment: _Callable[[_type.c_void_p,  # fragmentStart
                                 _type.UINT64,  # fileOffset
                                 _type.UINT64,  # fragmentSize
                                 _type.c_void_p],  # fragmentContext
                                _type.HRESULT]
    ReleaseFileFragment: _Callable[[_type.c_void_p],  # fragmentContext
                                   _type.c_void]
    GetFileSize: _Callable[[_Pointer[_type.UINT64]],  # fileSize
                           _type.HRESULT]
    GetLastWriteTime: _Callable[[_Pointer[_type.UINT64]],  # lastWriteTime
                                _type.HRESULT]


class IDWriteFontFile(_Unknwnbase.IUnknown):
    GetReferenceKey: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                _Pointer[_type.UINT32]],  # fontFileReferenceKeySize
                               _type.HRESULT]
    GetLoader: _Callable[[_Pointer[IDWriteFontFileLoader]],  # fontFileLoader
                         _type.HRESULT]
    Analyze: _Callable[[_Pointer[_type.BOOL],  # isSupportedFontType
                        _Pointer[_enum.DWRITE_FONT_FILE_TYPE],  # fontFileType
                        _Pointer[_enum.DWRITE_FONT_FACE_TYPE],  # fontFaceType
                        _Pointer[_type.UINT32]],  # numberOfFaces
                       _type.HRESULT]


class IDWriteRenderingParams(_Unknwnbase.IUnknown):
    GetGamma: _Callable[[],
                        _type.FLOAT]
    GetEnhancedContrast: _Callable[[],
                                   _type.FLOAT]
    GetClearTypeLevel: _Callable[[],
                                 _type.FLOAT]
    GetPixelGeometry: _Callable[[],
                                _enum.DWRITE_PIXEL_GEOMETRY]
    GetRenderingMode: _Callable[[],
                                _enum.DWRITE_RENDERING_MODE]


class IDWriteFontFace(_Unknwnbase.IUnknown):
    GetType: _Callable[[],
                       _enum.DWRITE_FONT_FACE_TYPE]
    GetFiles: _Callable[[_Pointer[_type.UINT32],  # numberOfFiles
                         _Pointer[IDWriteFontFile]],  # fontFiles
                        _type.HRESULT]
    GetIndex: _Callable[[],
                        _type.UINT32]
    GetSimulations: _Callable[[],
                              _enum.DWRITE_FONT_SIMULATIONS]
    IsSymbolFont: _Callable[[],
                            _type.BOOL]
    GetMetrics: _Callable[[_Pointer[_struct.DWRITE_FONT_METRICS]],  # fontFaceMetrics
                          _type.c_void]
    GetGlyphCount: _Callable[[],
                             _type.UINT16]
    GetDesignGlyphMetrics: _Callable[[_Pointer[_type.UINT16],  # glyphIndices
                                      _type.UINT32,  # glyphCount
                                      _Pointer[_struct.DWRITE_GLYPH_METRICS],  # glyphMetrics
                                      _type.BOOL],  # isSideways
                                     _type.HRESULT]
    GetGlyphIndices: _Callable[[_Pointer[_type.UINT32],  # codePoints
                                _type.UINT32,  # codePointCount
                                _Pointer[_type.UINT16]],  # glyphIndices
                               _type.HRESULT]
    TryGetFontTable: _Callable[[_type.UINT32,  # openTypeTableTag
                                _type.c_void_p,  # tableData
                                _Pointer[_type.UINT32],  # tableSize
                                _type.c_void_p,  # tableContext
                                _Pointer[_type.BOOL]],  # exists
                               _type.HRESULT]
    ReleaseFontTable: _Callable[[_type.c_void_p],  # tableContext
                                _type.c_void]
    GetGlyphRunOutline: _Callable[[_type.FLOAT,  # emSize
                                   _Pointer[_type.UINT16],  # glyphIndices
                                   _Pointer[_type.FLOAT],  # glyphAdvances
                                   _Pointer[_struct.DWRITE_GLYPH_OFFSET],  # glyphOffsets
                                   _type.UINT32,  # glyphCount
                                   _type.BOOL,  # isSideways
                                   _type.BOOL,  # isRightToLeft
                                   _Pointer[_d2d1.ID2D1SimplifiedGeometrySink]],  # geometrySink
                                  _type.HRESULT]
    GetRecommendedRenderingMode: _Callable[[_type.FLOAT,  # emSize
                                            _type.FLOAT,  # pixelsPerDip
                                            _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                            IDWriteRenderingParams,  # renderingParams
                                            _Pointer[_enum.DWRITE_RENDERING_MODE]],  # renderingMode
                                           _type.HRESULT]
    GetGdiCompatibleMetrics: _Callable[[_type.FLOAT,  # emSize
                                        _type.FLOAT,  # pixelsPerDip
                                        _Pointer[_struct.DWRITE_MATRIX],  # transform
                                        _Pointer[_struct.DWRITE_FONT_METRICS]],  # fontFaceMetrics
                                       _type.HRESULT]
    GetGdiCompatibleGlyphMetrics: _Callable[[_type.FLOAT,  # emSize
                                             _type.FLOAT,  # pixelsPerDip
                                             _Pointer[_struct.DWRITE_MATRIX],  # transform
                                             _type.BOOL,  # useGdiNatural
                                             _Pointer[_type.UINT16],  # glyphIndices
                                             _type.UINT32,  # glyphCount
                                             _Pointer[_struct.DWRITE_GLYPH_METRICS],  # glyphMetrics
                                             _type.BOOL],  # isSideways
                                            _type.HRESULT]


class IDWriteFontCollectionLoader(_Unknwnbase.IUnknown):
    CreateEnumeratorFromKey: _Callable[[IDWriteFactory,  # factory
                                        _type.c_void_p,  # collectionKey
                                        _type.UINT32,  # collectionKeySize
                                        _Pointer[IDWriteFontFileEnumerator]],  # fontFileEnumerator
                                       _type.HRESULT]


class IDWriteFontFileEnumerator(_Unknwnbase.IUnknown):
    MoveNext: _Callable[[_Pointer[_type.BOOL]],  # hasCurrentFile
                        _type.HRESULT]
    GetCurrentFontFile: _Callable[[_Pointer[IDWriteFontFile]],  # fontFile
                                  _type.HRESULT]


class IDWriteLocalizedStrings(_Unknwnbase.IUnknown):
    GetCount: _Callable[[],
                        _type.UINT32]
    FindLocaleName: _Callable[[_type.LPWSTR,  # localeName
                               _Pointer[_type.UINT32],  # index
                               _Pointer[_type.BOOL]],  # exists
                              _type.HRESULT]
    GetLocaleNameLength: _Callable[[_type.UINT32,  # index
                                    _Pointer[_type.UINT32]],  # length
                                   _type.HRESULT]
    GetLocaleName: _Callable[[_type.UINT32,  # index
                              _type.LPWSTR,  # localeName
                              _type.UINT32],  # size
                             _type.HRESULT]
    GetStringLength: _Callable[[_type.UINT32,  # index
                                _Pointer[_type.UINT32]],  # length
                               _type.HRESULT]
    GetString: _Callable[[_type.UINT32,  # index
                          _type.LPWSTR,  # stringBuffer
                          _type.UINT32],  # size
                         _type.HRESULT]


class IDWriteFontCollection(_Unknwnbase.IUnknown):
    GetFontFamilyCount: _Callable[[],
                                  _type.UINT32]
    GetFontFamily: _Callable[[_type.UINT32,  # index
                              _Pointer[IDWriteFontFamily]],  # fontFamily
                             _type.HRESULT]
    FindFamilyName: _Callable[[_type.LPWSTR,  # familyName
                               _Pointer[_type.UINT32],  # index
                               _Pointer[_type.BOOL]],  # exists
                              _type.HRESULT]
    GetFontFromFontFace: _Callable[[IDWriteFontFace,  # fontFace
                                    _Pointer[IDWriteFont]],  # font
                                   _type.HRESULT]


class IDWriteFontList(_Unknwnbase.IUnknown):
    GetFontCollection: _Callable[[_Pointer[IDWriteFontCollection]],  # fontCollection
                                 _type.HRESULT]
    GetFontCount: _Callable[[],
                            _type.UINT32]
    GetFont: _Callable[[_type.UINT32,  # index
                        _Pointer[IDWriteFont]],  # font
                       _type.HRESULT]


class IDWriteFontFamily(IDWriteFontList):
    GetFamilyNames: _Callable[[_Pointer[IDWriteLocalizedStrings]],  # names
                              _type.HRESULT]
    GetFirstMatchingFont: _Callable[[_enum.DWRITE_FONT_WEIGHT,  # weight
                                     _enum.DWRITE_FONT_STRETCH,  # stretch
                                     _enum.DWRITE_FONT_STYLE,  # style
                                     _Pointer[IDWriteFont]],  # matchingFont
                                    _type.HRESULT]
    GetMatchingFonts: _Callable[[_enum.DWRITE_FONT_WEIGHT,  # weight
                                 _enum.DWRITE_FONT_STRETCH,  # stretch
                                 _enum.DWRITE_FONT_STYLE,  # style
                                 _Pointer[IDWriteFontList]],  # matchingFonts
                                _type.HRESULT]


class IDWriteFont(_Unknwnbase.IUnknown):
    GetFontFamily: _Callable[[_Pointer[IDWriteFontFamily]],  # fontFamily
                             _type.HRESULT]
    GetWeight: _Callable[[],
                         _enum.DWRITE_FONT_WEIGHT]
    GetStretch: _Callable[[],
                          _enum.DWRITE_FONT_STRETCH]
    GetStyle: _Callable[[],
                        _enum.DWRITE_FONT_STYLE]
    IsSymbolFont: _Callable[[],
                            _type.BOOL]
    GetFaceNames: _Callable[[_Pointer[IDWriteLocalizedStrings]],  # names
                            _type.HRESULT]
    GetInformationalStrings: _Callable[[_enum.DWRITE_INFORMATIONAL_STRING_ID,  # informationalStringID
                                        _Pointer[IDWriteLocalizedStrings],  # informationalStrings
                                        _Pointer[_type.BOOL]],  # exists
                                       _type.HRESULT]
    GetSimulations: _Callable[[],
                              _enum.DWRITE_FONT_SIMULATIONS]
    GetMetrics: _Callable[[_Pointer[_struct.DWRITE_FONT_METRICS]],  # fontMetrics
                          _type.c_void]
    HasCharacter: _Callable[[_type.UINT32,  # unicodeValue
                             _Pointer[_type.BOOL]],  # exists
                            _type.HRESULT]
    CreateFontFace: _Callable[[_Pointer[IDWriteFontFace]],  # fontFace
                              _type.HRESULT]


class IDWriteTextFormat(_Unknwnbase.IUnknown):
    SetTextAlignment: _Callable[[_enum.DWRITE_TEXT_ALIGNMENT],  # textAlignment
                                _type.HRESULT]
    SetParagraphAlignment: _Callable[[_enum.DWRITE_PARAGRAPH_ALIGNMENT],  # paragraphAlignment
                                     _type.HRESULT]
    SetWordWrapping: _Callable[[_enum.DWRITE_WORD_WRAPPING],  # wordWrapping
                               _type.HRESULT]
    SetReadingDirection: _Callable[[_enum.DWRITE_READING_DIRECTION],  # readingDirection
                                   _type.HRESULT]
    SetFlowDirection: _Callable[[_enum.DWRITE_FLOW_DIRECTION],  # flowDirection
                                _type.HRESULT]
    SetIncrementalTabStop: _Callable[[_type.FLOAT],  # incrementalTabStop
                                     _type.HRESULT]
    SetTrimming: _Callable[[_Pointer[_struct.DWRITE_TRIMMING],  # trimmingOptions
                            IDWriteInlineObject],  # trimmingSign
                           _type.HRESULT]
    SetLineSpacing: _Callable[[_enum.DWRITE_LINE_SPACING_METHOD,  # lineSpacingMethod
                               _type.FLOAT,  # lineSpacing
                               _type.FLOAT],  # baseline
                              _type.HRESULT]
    GetTextAlignment: _Callable[[],
                                _enum.DWRITE_TEXT_ALIGNMENT]
    GetParagraphAlignment: _Callable[[],
                                     _enum.DWRITE_PARAGRAPH_ALIGNMENT]
    GetWordWrapping: _Callable[[],
                               _enum.DWRITE_WORD_WRAPPING]
    GetReadingDirection: _Callable[[],
                                   _enum.DWRITE_READING_DIRECTION]
    GetFlowDirection: _Callable[[],
                                _enum.DWRITE_FLOW_DIRECTION]
    GetIncrementalTabStop: _Callable[[],
                                     _type.FLOAT]
    GetTrimming: _Callable[[_Pointer[_struct.DWRITE_TRIMMING],  # trimmingOptions
                            _Pointer[IDWriteInlineObject]],  # trimmingSign
                           _type.HRESULT]
    GetLineSpacing: _Callable[[_Pointer[_enum.DWRITE_LINE_SPACING_METHOD],  # lineSpacingMethod
                               _Pointer[_type.FLOAT],  # lineSpacing
                               _Pointer[_type.FLOAT]],  # baseline
                              _type.HRESULT]
    GetFontCollection: _Callable[[_Pointer[IDWriteFontCollection]],  # fontCollection
                                 _type.HRESULT]
    GetFontFamilyNameLength: _Callable[[],
                                       _type.UINT32]
    GetFontFamilyName: _Callable[[_type.LPWSTR,  # fontFamilyName
                                  _type.UINT32],  # nameSize
                                 _type.HRESULT]
    GetFontWeight: _Callable[[],
                             _enum.DWRITE_FONT_WEIGHT]
    GetFontStyle: _Callable[[],
                            _enum.DWRITE_FONT_STYLE]
    GetFontStretch: _Callable[[],
                              _enum.DWRITE_FONT_STRETCH]
    GetFontSize: _Callable[[],
                           _type.FLOAT]
    GetLocaleNameLength: _Callable[[],
                                   _type.UINT32]
    GetLocaleName: _Callable[[_type.LPWSTR,  # localeName
                              _type.UINT32],  # nameSize
                             _type.HRESULT]


class IDWriteTypography(_Unknwnbase.IUnknown):
    AddFontFeature: _Callable[[_struct.DWRITE_FONT_FEATURE],  # fontFeature
                              _type.HRESULT]
    GetFontFeatureCount: _Callable[[],
                                   _type.UINT32]
    GetFontFeature: _Callable[[_type.UINT32,  # fontFeatureIndex
                               _Pointer[_struct.DWRITE_FONT_FEATURE]],  # fontFeature
                              _type.HRESULT]


class IDWriteNumberSubstitution(_Unknwnbase.IUnknown):
    pass


class IDWriteTextAnalysisSource(_Unknwnbase.IUnknown):
    GetTextAtPosition: _Callable[[_type.UINT32,  # textPosition
                                  _Pointer[_type.LPWSTR],  # textString
                                  _Pointer[_type.UINT32]],  # textLength
                                 _type.HRESULT]
    GetTextBeforePosition: _Callable[[_type.UINT32,  # textPosition
                                      _Pointer[_type.LPWSTR],  # textString
                                      _Pointer[_type.UINT32]],  # textLength
                                     _type.HRESULT]
    GetParagraphReadingDirection: _Callable[[],
                                            _enum.DWRITE_READING_DIRECTION]
    GetLocaleName: _Callable[[_type.UINT32,  # textPosition
                              _Pointer[_type.UINT32],  # textLength
                              _Pointer[_type.LPWSTR]],  # localeName
                             _type.HRESULT]
    GetNumberSubstitution: _Callable[[_type.UINT32,  # textPosition
                                      _Pointer[_type.UINT32],  # textLength
                                      _Pointer[IDWriteNumberSubstitution]],  # numberSubstitution
                                     _type.HRESULT]


class IDWriteTextAnalysisSink(_Unknwnbase.IUnknown):
    SetScriptAnalysis: _Callable[[_type.UINT32,  # textPosition
                                  _type.UINT32,  # textLength
                                  _Pointer[_struct.DWRITE_SCRIPT_ANALYSIS]],  # scriptAnalysis
                                 _type.HRESULT]
    SetLineBreakpoints: _Callable[[_type.UINT32,  # textPosition
                                   _type.UINT32,  # textLength
                                   _Pointer[_struct.DWRITE_LINE_BREAKPOINT]],  # lineBreakpoints
                                  _type.HRESULT]
    SetBidiLevel: _Callable[[_type.UINT32,  # textPosition
                             _type.UINT32,  # textLength
                             _type.UINT8,  # explicitLevel
                             _type.UINT8],  # resolvedLevel
                            _type.HRESULT]
    SetNumberSubstitution: _Callable[[_type.UINT32,  # textPosition
                                      _type.UINT32,  # textLength
                                      IDWriteNumberSubstitution],  # numberSubstitution
                                     _type.HRESULT]


class IDWriteTextAnalyzer(_Unknwnbase.IUnknown):
    AnalyzeScript: _Callable[[IDWriteTextAnalysisSource,  # analysisSource
                              _type.UINT32,  # textPosition
                              _type.UINT32,  # textLength
                              IDWriteTextAnalysisSink],  # analysisSink
                             _type.HRESULT]
    AnalyzeBidi: _Callable[[IDWriteTextAnalysisSource,  # analysisSource
                            _type.UINT32,  # textPosition
                            _type.UINT32,  # textLength
                            IDWriteTextAnalysisSink],  # analysisSink
                           _type.HRESULT]
    AnalyzeNumberSubstitution: _Callable[[IDWriteTextAnalysisSource,  # analysisSource
                                          _type.UINT32,  # textPosition
                                          _type.UINT32,  # textLength
                                          IDWriteTextAnalysisSink],  # analysisSink
                                         _type.HRESULT]
    AnalyzeLineBreakpoints: _Callable[[IDWriteTextAnalysisSource,  # analysisSource
                                       _type.UINT32,  # textPosition
                                       _type.UINT32,  # textLength
                                       IDWriteTextAnalysisSink],  # analysisSink
                                      _type.HRESULT]
    GetGlyphs: _Callable[[_type.LPWSTR,  # textString
                          _type.UINT32,  # textLength
                          IDWriteFontFace,  # fontFace
                          _type.BOOL,  # isSideways
                          _type.BOOL,  # isRightToLeft
                          _Pointer[_struct.DWRITE_SCRIPT_ANALYSIS],  # scriptAnalysis
                          _type.LPWSTR,  # localeName
                          IDWriteNumberSubstitution,  # numberSubstitution
                          _Pointer[_Pointer[_struct.DWRITE_TYPOGRAPHIC_FEATURES]],  # features
                          _Pointer[_type.UINT32],  # featureRangeLengths
                          _type.UINT32,  # featureRanges
                          _type.UINT32,  # maxGlyphCount
                          _Pointer[_type.UINT16],  # clusterMap
                          _Pointer[_struct.DWRITE_SHAPING_TEXT_PROPERTIES],  # textProps
                          _Pointer[_type.UINT16],  # glyphIndices
                          _Pointer[_struct.DWRITE_SHAPING_GLYPH_PROPERTIES],  # glyphProps
                          _Pointer[_type.UINT32]],  # actualGlyphCount
                         _type.HRESULT]
    GetGlyphPlacements: _Callable[[_type.LPWSTR,  # textString
                                   _Pointer[_type.UINT16],  # clusterMap
                                   _Pointer[_struct.DWRITE_SHAPING_TEXT_PROPERTIES],  # textProps
                                   _type.UINT32,  # textLength
                                   _Pointer[_type.UINT16],  # glyphIndices
                                   _Pointer[_struct.DWRITE_SHAPING_GLYPH_PROPERTIES],  # glyphProps
                                   _type.UINT32,  # glyphCount
                                   IDWriteFontFace,  # fontFace
                                   _type.FLOAT,  # fontEmSize
                                   _type.BOOL,  # isSideways
                                   _type.BOOL,  # isRightToLeft
                                   _Pointer[_struct.DWRITE_SCRIPT_ANALYSIS],  # scriptAnalysis
                                   _type.LPWSTR,  # localeName
                                   _Pointer[_Pointer[_struct.DWRITE_TYPOGRAPHIC_FEATURES]],  # features
                                   _Pointer[_type.UINT32],  # featureRangeLengths
                                   _type.UINT32,  # featureRanges
                                   _Pointer[_type.FLOAT],  # glyphAdvances
                                   _Pointer[_struct.DWRITE_GLYPH_OFFSET]],  # glyphOffsets
                                  _type.HRESULT]
    GetGdiCompatibleGlyphPlacements: _Callable[[_type.LPWSTR,  # textString
                                                _Pointer[_type.UINT16],  # clusterMap
                                                _Pointer[_struct.DWRITE_SHAPING_TEXT_PROPERTIES],  # textProps
                                                _type.UINT32,  # textLength
                                                _Pointer[_type.UINT16],  # glyphIndices
                                                _Pointer[_struct.DWRITE_SHAPING_GLYPH_PROPERTIES],  # glyphProps
                                                _type.UINT32,  # glyphCount
                                                IDWriteFontFace,  # fontFace
                                                _type.FLOAT,  # fontEmSize
                                                _type.FLOAT,  # pixelsPerDip
                                                _Pointer[_struct.DWRITE_MATRIX],  # transform
                                                _type.BOOL,  # useGdiNatural
                                                _type.BOOL,  # isSideways
                                                _type.BOOL,  # isRightToLeft
                                                _Pointer[_struct.DWRITE_SCRIPT_ANALYSIS],  # scriptAnalysis
                                                _type.LPWSTR,  # localeName
                                                _Pointer[_Pointer[_struct.DWRITE_TYPOGRAPHIC_FEATURES]],  # features
                                                _Pointer[_type.UINT32],  # featureRangeLengths
                                                _type.UINT32,  # featureRanges
                                                _Pointer[_type.FLOAT],  # glyphAdvances
                                                _Pointer[_struct.DWRITE_GLYPH_OFFSET]],  # glyphOffsets
                                               _type.HRESULT]


class IDWriteInlineObject(_Unknwnbase.IUnknown):
    Draw: _Callable[[_type.c_void_p,  # clientDrawingContext
                     IDWriteTextRenderer,  # renderer
                     _type.FLOAT,  # originX
                     _type.FLOAT,  # originY
                     _type.BOOL,  # isSideways
                     _type.BOOL,  # isRightToLeft
                     _Unknwnbase.IUnknown],  # clientDrawingEffect
                    _type.HRESULT]
    GetMetrics: _Callable[[_Pointer[_struct.DWRITE_INLINE_OBJECT_METRICS]],  # metrics
                          _type.HRESULT]
    GetOverhangMetrics: _Callable[[_Pointer[_struct.DWRITE_OVERHANG_METRICS]],  # overhangs
                                  _type.HRESULT]
    GetBreakConditions: _Callable[[_Pointer[_enum.DWRITE_BREAK_CONDITION],  # breakConditionBefore
                                   _Pointer[_enum.DWRITE_BREAK_CONDITION]],  # breakConditionAfter
                                  _type.HRESULT]


class IDWritePixelSnapping(_Unknwnbase.IUnknown):
    IsPixelSnappingDisabled: _Callable[[_type.c_void_p,  # clientDrawingContext
                                        _Pointer[_type.BOOL]],  # isDisabled
                                       _type.HRESULT]
    GetCurrentTransform: _Callable[[_type.c_void_p,  # clientDrawingContext
                                    _Pointer[_struct.DWRITE_MATRIX]],  # transform
                                   _type.HRESULT]
    GetPixelsPerDip: _Callable[[_type.c_void_p,  # clientDrawingContext
                                _Pointer[_type.FLOAT]],  # pixelsPerDip
                               _type.HRESULT]


class IDWriteTextRenderer(IDWritePixelSnapping):
    DrawGlyphRun: _Callable[[_type.c_void_p,  # clientDrawingContext
                             _type.FLOAT,  # baselineOriginX
                             _type.FLOAT,  # baselineOriginY
                             _enum.DWRITE_MEASURING_MODE,  # measuringMode
                             _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                             _Pointer[_struct.DWRITE_GLYPH_RUN_DESCRIPTION],  # glyphRunDescription
                             _Unknwnbase.IUnknown],  # clientDrawingEffect
                            _type.HRESULT]
    DrawUnderline: _Callable[[_type.c_void_p,  # clientDrawingContext
                              _type.FLOAT,  # baselineOriginX
                              _type.FLOAT,  # baselineOriginY
                              _Pointer[_struct.DWRITE_UNDERLINE],  # underline
                              _Unknwnbase.IUnknown],  # clientDrawingEffect
                             _type.HRESULT]
    DrawStrikethrough: _Callable[[_type.c_void_p,  # clientDrawingContext
                                  _type.FLOAT,  # baselineOriginX
                                  _type.FLOAT,  # baselineOriginY
                                  _Pointer[_struct.DWRITE_STRIKETHROUGH],  # strikethrough
                                  _Unknwnbase.IUnknown],  # clientDrawingEffect
                                 _type.HRESULT]
    DrawInlineObject: _Callable[[_type.c_void_p,  # clientDrawingContext
                                 _type.FLOAT,  # originX
                                 _type.FLOAT,  # originY
                                 IDWriteInlineObject,  # inlineObject
                                 _type.BOOL,  # isSideways
                                 _type.BOOL,  # isRightToLeft
                                 _Unknwnbase.IUnknown],  # clientDrawingEffect
                                _type.HRESULT]


class IDWriteTextLayout(IDWriteTextFormat):
    SetMaxWidth: _Callable[[_type.FLOAT],  # maxWidth
                           _type.HRESULT]
    SetMaxHeight: _Callable[[_type.FLOAT],  # maxHeight
                            _type.HRESULT]
    SetFontCollection: _Callable[[IDWriteFontCollection,  # fontCollection
                                  _struct.DWRITE_TEXT_RANGE],  # textRange
                                 _type.HRESULT]
    SetFontFamilyName: _Callable[[_type.LPWSTR,  # fontFamilyName
                                  _struct.DWRITE_TEXT_RANGE],  # textRange
                                 _type.HRESULT]
    SetFontWeight: _Callable[[_enum.DWRITE_FONT_WEIGHT,  # fontWeight
                              _struct.DWRITE_TEXT_RANGE],  # textRange
                             _type.HRESULT]
    SetFontStyle: _Callable[[_enum.DWRITE_FONT_STYLE,  # fontStyle
                             _struct.DWRITE_TEXT_RANGE],  # textRange
                            _type.HRESULT]
    SetFontStretch: _Callable[[_enum.DWRITE_FONT_STRETCH,  # fontStretch
                               _struct.DWRITE_TEXT_RANGE],  # textRange
                              _type.HRESULT]
    SetFontSize: _Callable[[_type.FLOAT,  # fontSize
                            _struct.DWRITE_TEXT_RANGE],  # textRange
                           _type.HRESULT]
    SetUnderline: _Callable[[_type.BOOL,  # hasUnderline
                             _struct.DWRITE_TEXT_RANGE],  # textRange
                            _type.HRESULT]
    SetStrikethrough: _Callable[[_type.BOOL,  # hasStrikethrough
                                 _struct.DWRITE_TEXT_RANGE],  # textRange
                                _type.HRESULT]
    SetDrawingEffect: _Callable[[_Unknwnbase.IUnknown,  # drawingEffect
                                 _struct.DWRITE_TEXT_RANGE],  # textRange
                                _type.HRESULT]
    SetInlineObject: _Callable[[IDWriteInlineObject,  # inlineObject
                                _struct.DWRITE_TEXT_RANGE],  # textRange
                               _type.HRESULT]
    SetTypography: _Callable[[IDWriteTypography,  # typography
                              _struct.DWRITE_TEXT_RANGE],  # textRange
                             _type.HRESULT]
    SetLocaleName: _Callable[[_type.LPWSTR,  # localeName
                              _struct.DWRITE_TEXT_RANGE],  # textRange
                             _type.HRESULT]
    GetMaxWidth: _Callable[[],
                           _type.FLOAT]
    GetMaxHeight: _Callable[[],
                            _type.FLOAT]
    GetFontCollection_: _Callable[[_type.UINT32,  # currentPosition
                                   _Pointer[IDWriteFontCollection],  # fontCollection
                                   _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                  _type.HRESULT]
    GetFontFamilyNameLength_: _Callable[[_type.UINT32,  # currentPosition
                                         _Pointer[_type.UINT32],  # nameLength
                                         _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                        _type.HRESULT]
    GetFontFamilyName_: _Callable[[_type.UINT32,  # currentPosition
                                   _type.LPWSTR,  # fontFamilyName
                                   _type.UINT32,  # nameSize
                                   _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                  _type.HRESULT]
    GetFontWeight_: _Callable[[_type.UINT32,  # currentPosition
                               _Pointer[_enum.DWRITE_FONT_WEIGHT],  # fontWeight
                               _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                              _type.HRESULT]
    GetFontStyle_: _Callable[[_type.UINT32,  # currentPosition
                              _Pointer[_enum.DWRITE_FONT_STYLE],  # fontStyle
                              _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                             _type.HRESULT]
    GetFontStretch_: _Callable[[_type.UINT32,  # currentPosition
                                _Pointer[_enum.DWRITE_FONT_STRETCH],  # fontStretch
                                _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                               _type.HRESULT]
    GetFontSize_: _Callable[[_type.UINT32,  # currentPosition
                             _Pointer[_type.FLOAT],  # fontSize
                             _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                            _type.HRESULT]
    GetUnderline: _Callable[[_type.UINT32,  # currentPosition
                             _Pointer[_type.BOOL],  # hasUnderline
                             _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                            _type.HRESULT]
    GetStrikethrough: _Callable[[_type.UINT32,  # currentPosition
                                 _Pointer[_type.BOOL],  # hasStrikethrough
                                 _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                _type.HRESULT]
    GetDrawingEffect: _Callable[[_type.UINT32,  # currentPosition
                                 _Pointer[_Unknwnbase.IUnknown],  # drawingEffect
                                 _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                _type.HRESULT]
    GetInlineObject: _Callable[[_type.UINT32,  # currentPosition
                                _Pointer[IDWriteInlineObject],  # inlineObject
                                _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                               _type.HRESULT]
    GetTypography: _Callable[[_type.UINT32,  # currentPosition
                              _Pointer[IDWriteTypography],  # typography
                              _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                             _type.HRESULT]
    GetLocaleNameLength_: _Callable[[_type.UINT32,  # currentPosition
                                     _Pointer[_type.UINT32],  # nameLength
                                     _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                    _type.HRESULT]
    GetLocaleName_: _Callable[[_type.UINT32,  # currentPosition
                               _type.LPWSTR,  # localeName
                               _type.UINT32,  # nameSize
                               _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                              _type.HRESULT]
    Draw: _Callable[[_type.c_void_p,  # clientDrawingContext
                     IDWriteTextRenderer,  # renderer
                     _type.FLOAT,  # originX
                     _type.FLOAT],  # originY
                    _type.HRESULT]
    GetLineMetrics: _Callable[[_Pointer[_struct.DWRITE_LINE_METRICS],  # lineMetrics
                               _type.UINT32,  # maxLineCount
                               _Pointer[_type.UINT32]],  # actualLineCount
                              _type.HRESULT]
    GetMetrics: _Callable[[_Pointer[_struct.DWRITE_TEXT_METRICS]],  # textMetrics
                          _type.HRESULT]
    GetOverhangMetrics: _Callable[[_Pointer[_struct.DWRITE_OVERHANG_METRICS]],  # overhangs
                                  _type.HRESULT]
    GetClusterMetrics: _Callable[[_Pointer[_struct.DWRITE_CLUSTER_METRICS],  # clusterMetrics
                                  _type.UINT32,  # maxClusterCount
                                  _Pointer[_type.UINT32]],  # actualClusterCount
                                 _type.HRESULT]
    DetermineMinWidth: _Callable[[_Pointer[_type.FLOAT]],  # minWidth
                                 _type.HRESULT]
    HitTestPoint: _Callable[[_type.FLOAT,  # pointX
                             _type.FLOAT,  # pointY
                             _Pointer[_type.BOOL],  # isTrailingHit
                             _Pointer[_type.BOOL],  # isInside
                             _Pointer[_struct.DWRITE_HIT_TEST_METRICS]],  # hitTestMetrics
                            _type.HRESULT]
    HitTestTextPosition: _Callable[[_type.UINT32,  # textPosition
                                    _type.BOOL,  # isTrailingHit
                                    _Pointer[_type.FLOAT],  # pointX
                                    _Pointer[_type.FLOAT],  # pointY
                                    _Pointer[_struct.DWRITE_HIT_TEST_METRICS]],  # hitTestMetrics
                                   _type.HRESULT]
    HitTestTextRange: _Callable[[_type.UINT32,  # textPosition
                                 _type.UINT32,  # textLength
                                 _type.FLOAT,  # originX
                                 _type.FLOAT,  # originY
                                 _Pointer[_struct.DWRITE_HIT_TEST_METRICS],  # hitTestMetrics
                                 _type.UINT32,  # maxHitTestMetricsCount
                                 _Pointer[_type.UINT32]],  # actualHitTestMetricsCount
                                _type.HRESULT]


class IDWriteBitmapRenderTarget(_Unknwnbase.IUnknown):
    DrawGlyphRun: _Callable[[_type.FLOAT,  # baselineOriginX
                             _type.FLOAT,  # baselineOriginY
                             _enum.DWRITE_MEASURING_MODE,  # measuringMode
                             _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                             IDWriteRenderingParams,  # renderingParams
                             _type.COLORREF,  # textColor
                             _Pointer[_struct.RECT]],  # blackBoxRect
                            _type.HRESULT]
    GetMemoryDC: _Callable[[],
                           _type.HDC]
    GetPixelsPerDip: _Callable[[],
                               _type.FLOAT]
    SetPixelsPerDip: _Callable[[_type.FLOAT],  # pixelsPerDip
                               _type.HRESULT]
    GetCurrentTransform: _Callable[[_Pointer[_struct.DWRITE_MATRIX]],  # transform
                                   _type.HRESULT]
    SetCurrentTransform: _Callable[[_Pointer[_struct.DWRITE_MATRIX]],  # transform
                                   _type.HRESULT]
    GetSize: _Callable[[_Pointer[_struct.SIZE]],  # size
                       _type.HRESULT]
    Resize: _Callable[[_type.UINT32,  # width
                       _type.UINT32],  # height
                      _type.HRESULT]


class IDWriteGdiInterop(_Unknwnbase.IUnknown):
    CreateFontFromLOGFONT: _Callable[[_Pointer[_struct.LOGFONTW],  # logFont
                                      _Pointer[IDWriteFont]],  # font
                                     _type.HRESULT]
    ConvertFontToLOGFONT: _Callable[[IDWriteFont,  # font
                                     _Pointer[_struct.LOGFONTW],  # logFont
                                     _Pointer[_type.BOOL]],  # isSystemFont
                                    _type.HRESULT]
    ConvertFontFaceToLOGFONT: _Callable[[IDWriteFontFace,  # font
                                         _Pointer[_struct.LOGFONTW]],  # logFont
                                        _type.HRESULT]
    CreateFontFaceFromHdc: _Callable[[_type.HDC,  # hdc
                                      _Pointer[IDWriteFontFace]],  # fontFace
                                     _type.HRESULT]
    CreateBitmapRenderTarget: _Callable[[_type.HDC,  # hdc
                                         _type.UINT32,  # width
                                         _type.UINT32,  # height
                                         _Pointer[IDWriteBitmapRenderTarget]],  # renderTarget
                                        _type.HRESULT]


class IDWriteGlyphRunAnalysis(_Unknwnbase.IUnknown):
    GetAlphaTextureBounds: _Callable[[_enum.DWRITE_TEXTURE_TYPE,  # textureType
                                      _Pointer[_struct.RECT]],  # textureBounds
                                     _type.HRESULT]
    CreateAlphaTexture: _Callable[[_enum.DWRITE_TEXTURE_TYPE,  # textureType
                                   _Pointer[_struct.RECT],  # textureBounds
                                   _Pointer[_type.BYTE],  # alphaValues
                                   _type.UINT32],  # bufferSize
                                  _type.HRESULT]
    GetAlphaBlendParams: _Callable[[IDWriteRenderingParams,  # renderingParams
                                    _Pointer[_type.FLOAT],  # blendGamma
                                    _Pointer[_type.FLOAT],  # blendEnhancedContrast
                                    _Pointer[_type.FLOAT]],  # blendClearTypeLevel
                                   _type.HRESULT]


class IDWriteFactory(_Unknwnbase.IUnknown):
    GetSystemFontCollection: _Callable[[_Pointer[IDWriteFontCollection],  # fontCollection
                                        _type.BOOL],  # checkForUpdates
                                       _type.HRESULT]
    CreateCustomFontCollection: _Callable[[IDWriteFontCollectionLoader,  # collectionLoader
                                           _type.c_void_p,  # collectionKey
                                           _type.UINT32,  # collectionKeySize
                                           _Pointer[IDWriteFontCollection]],  # fontCollection
                                          _type.HRESULT]
    RegisterFontCollectionLoader: _Callable[[IDWriteFontCollectionLoader],  # fontCollectionLoader
                                            _type.HRESULT]
    UnregisterFontCollectionLoader: _Callable[[IDWriteFontCollectionLoader],  # fontCollectionLoader
                                              _type.HRESULT]
    CreateFontFileReference: _Callable[[_type.LPWSTR,  # filePath
                                        _Pointer[_struct.FILETIME],  # lastWriteTime
                                        _Pointer[IDWriteFontFile]],  # fontFile
                                       _type.HRESULT]
    CreateCustomFontFileReference: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                              _type.UINT32,  # fontFileReferenceKeySize
                                              IDWriteFontFileLoader,  # fontFileLoader
                                              _Pointer[IDWriteFontFile]],  # fontFile
                                             _type.HRESULT]
    CreateFontFace: _Callable[[_enum.DWRITE_FONT_FACE_TYPE,  # fontFaceType
                               _type.UINT32,  # numberOfFiles
                               _Pointer[IDWriteFontFile],  # fontFiles
                               _type.UINT32,  # faceIndex
                               _enum.DWRITE_FONT_SIMULATIONS,  # fontFaceSimulationFlags
                               _Pointer[IDWriteFontFace]],  # fontFace
                              _type.HRESULT]
    CreateRenderingParams: _Callable[[_Pointer[IDWriteRenderingParams]],  # renderingParams
                                     _type.HRESULT]
    CreateMonitorRenderingParams: _Callable[[_type.HMONITOR,  # monitor
                                             _Pointer[IDWriteRenderingParams]],  # renderingParams
                                            _type.HRESULT]
    CreateCustomRenderingParams: _Callable[[_type.FLOAT,  # gamma
                                            _type.FLOAT,  # enhancedContrast
                                            _type.FLOAT,  # clearTypeLevel
                                            _enum.DWRITE_PIXEL_GEOMETRY,  # pixelGeometry
                                            _enum.DWRITE_RENDERING_MODE,  # renderingMode
                                            _Pointer[IDWriteRenderingParams]],  # renderingParams
                                           _type.HRESULT]
    RegisterFontFileLoader: _Callable[[IDWriteFontFileLoader],  # fontFileLoader
                                      _type.HRESULT]
    UnregisterFontFileLoader: _Callable[[IDWriteFontFileLoader],  # fontFileLoader
                                        _type.HRESULT]
    CreateTextFormat: _Callable[[_type.LPWSTR,  # fontFamilyName
                                 IDWriteFontCollection,  # fontCollection
                                 _enum.DWRITE_FONT_WEIGHT,  # fontWeight
                                 _enum.DWRITE_FONT_STYLE,  # fontStyle
                                 _enum.DWRITE_FONT_STRETCH,  # fontStretch
                                 _type.FLOAT,  # fontSize
                                 _type.LPWSTR,  # localeName
                                 _Pointer[IDWriteTextFormat]],  # textFormat
                                _type.HRESULT]
    CreateTypography: _Callable[[_Pointer[IDWriteTypography]],  # typography
                                _type.HRESULT]
    GetGdiInterop: _Callable[[_Pointer[IDWriteGdiInterop]],  # gdiInterop
                             _type.HRESULT]
    CreateTextLayout: _Callable[[_type.LPWSTR,  # string
                                 _type.UINT32,  # stringLength
                                 IDWriteTextFormat,  # textFormat
                                 _type.FLOAT,  # maxWidth
                                 _type.FLOAT,  # maxHeight
                                 _Pointer[IDWriteTextLayout]],  # textLayout
                                _type.HRESULT]
    CreateGdiCompatibleTextLayout: _Callable[[_type.LPWSTR,  # string
                                              _type.UINT32,  # stringLength
                                              IDWriteTextFormat,  # textFormat
                                              _type.FLOAT,  # layoutWidth
                                              _type.FLOAT,  # layoutHeight
                                              _type.FLOAT,  # pixelsPerDip
                                              _Pointer[_struct.DWRITE_MATRIX],  # transform
                                              _type.BOOL,  # useGdiNatural
                                              _Pointer[IDWriteTextLayout]],  # textLayout
                                             _type.HRESULT]
    CreateEllipsisTrimmingSign: _Callable[[IDWriteTextFormat,  # textFormat
                                           _Pointer[IDWriteInlineObject]],  # trimmingSign
                                          _type.HRESULT]
    CreateTextAnalyzer: _Callable[[_Pointer[IDWriteTextAnalyzer]],  # textAnalyzer
                                  _type.HRESULT]
    CreateNumberSubstitution: _Callable[[_enum.DWRITE_NUMBER_SUBSTITUTION_METHOD,  # substitutionMethod
                                         _type.LPWSTR,  # localeName
                                         _type.BOOL,  # ignoreUserOverride
                                         _Pointer[IDWriteNumberSubstitution]],  # numberSubstitution
                                        _type.HRESULT]
    CreateGlyphRunAnalysis: _Callable[[_Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                       _type.FLOAT,  # pixelsPerDip
                                       _Pointer[_struct.DWRITE_MATRIX],  # transform
                                       _enum.DWRITE_RENDERING_MODE,  # renderingMode
                                       _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                       _type.FLOAT,  # baselineOriginX
                                       _type.FLOAT,  # baselineOriginY
                                       _Pointer[IDWriteGlyphRunAnalysis]],  # glyphRunAnalysis
                                      _type.HRESULT]
