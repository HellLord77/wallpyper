from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import dwrite as _dwrite
from . import dwrite_1 as _dwrite_1
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDWriteTextRenderer1(_dwrite.IDWriteTextRenderer):
    DrawGlyphRun_: _Callable[[_type.c_void_p,  # clientDrawingContext
                              _type.FLOAT,  # baselineOriginX
                              _type.FLOAT,  # baselineOriginY
                              _enum.DWRITE_GLYPH_ORIENTATION_ANGLE,  # orientationAngle
                              _enum.DWRITE_MEASURING_MODE,  # measuringMode
                              _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                              _Pointer[_struct.DWRITE_GLYPH_RUN_DESCRIPTION],  # glyphRunDescription
                              _Unknwnbase.IUnknown],  # clientDrawingEffect
                             _type.HRESULT]
    DrawUnderline_: _Callable[[_type.c_void_p,  # clientDrawingContext
                               _type.FLOAT,  # baselineOriginX
                               _type.FLOAT,  # baselineOriginY
                               _enum.DWRITE_GLYPH_ORIENTATION_ANGLE,  # orientationAngle
                               _Pointer[_struct.DWRITE_UNDERLINE],  # underline
                               _Unknwnbase.IUnknown],  # clientDrawingEffect
                              _type.HRESULT]
    DrawStrikethrough_: _Callable[[_type.c_void_p,  # clientDrawingContext
                                   _type.FLOAT,  # baselineOriginX
                                   _type.FLOAT,  # baselineOriginY
                                   _enum.DWRITE_GLYPH_ORIENTATION_ANGLE,  # orientationAngle
                                   _Pointer[_struct.DWRITE_STRIKETHROUGH],  # strikethrough
                                   _Unknwnbase.IUnknown],  # clientDrawingEffect
                                  _type.HRESULT]
    DrawInlineObject_: _Callable[[_type.c_void_p,  # clientDrawingContext
                                  _type.FLOAT,  # originX
                                  _type.FLOAT,  # originY
                                  _enum.DWRITE_GLYPH_ORIENTATION_ANGLE,  # orientationAngle
                                  _dwrite.IDWriteInlineObject,  # inlineObject
                                  _type.BOOL,  # isSideways
                                  _type.BOOL,  # isRightToLeft
                                  _Unknwnbase.IUnknown],  # clientDrawingEffect
                                 _type.HRESULT]


class IDWriteTextFormat1(_dwrite.IDWriteTextFormat):
    SetVerticalGlyphOrientation: _Callable[[_enum.DWRITE_VERTICAL_GLYPH_ORIENTATION],  # glyphOrientation
                                           _type.HRESULT]
    GetVerticalGlyphOrientation: _Callable[[],
                                           _enum.DWRITE_VERTICAL_GLYPH_ORIENTATION]
    SetLastLineWrapping: _Callable[[_type.BOOL],  # isLastLineWrappingEnabled
                                   _type.HRESULT]
    GetLastLineWrapping: _Callable[[],
                                   _type.BOOL]
    SetOpticalAlignment: _Callable[[_enum.DWRITE_OPTICAL_ALIGNMENT],  # opticalAlignment
                                   _type.HRESULT]
    GetOpticalAlignment: _Callable[[],
                                   _enum.DWRITE_OPTICAL_ALIGNMENT]
    SetFontFallback: _Callable[[IDWriteFontFallback],  # fontFallback
                               _type.HRESULT]
    GetFontFallback: _Callable[[_Pointer[IDWriteFontFallback]],  # fontFallback
                               _type.HRESULT]


class IDWriteTextLayout2(_dwrite_1.IDWriteTextLayout1):
    GetMetrics_: _Callable[[_Pointer[_struct.DWRITE_TEXT_METRICS1]],  # textMetrics
                           _type.HRESULT]
    SetVerticalGlyphOrientation: _Callable[[_enum.DWRITE_VERTICAL_GLYPH_ORIENTATION],  # glyphOrientation
                                           _type.HRESULT]
    GetVerticalGlyphOrientation: _Callable[[],
                                           _enum.DWRITE_VERTICAL_GLYPH_ORIENTATION]
    SetLastLineWrapping: _Callable[[_type.BOOL],  # isLastLineWrappingEnabled
                                   _type.HRESULT]
    GetLastLineWrapping: _Callable[[],
                                   _type.BOOL]
    SetOpticalAlignment: _Callable[[_enum.DWRITE_OPTICAL_ALIGNMENT],  # opticalAlignment
                                   _type.HRESULT]
    GetOpticalAlignment: _Callable[[],
                                   _enum.DWRITE_OPTICAL_ALIGNMENT]
    SetFontFallback: _Callable[[IDWriteFontFallback],  # fontFallback
                               _type.HRESULT]
    GetFontFallback: _Callable[[_Pointer[IDWriteFontFallback]],  # fontFallback
                               _type.HRESULT]


class IDWriteTextAnalyzer2(_dwrite_1.IDWriteTextAnalyzer1):
    GetGlyphOrientationTransform_: _Callable[[_enum.DWRITE_GLYPH_ORIENTATION_ANGLE,  # glyphOrientationAngle
                                              _type.BOOL,  # isSideways
                                              _type.FLOAT,  # originX
                                              _type.FLOAT,  # originY
                                              _Pointer[_struct.DWRITE_MATRIX]],  # transform
                                             _type.HRESULT]
    GetTypographicFeatures: _Callable[[_dwrite.IDWriteFontFace,  # fontFace
                                       _struct.DWRITE_SCRIPT_ANALYSIS,  # scriptAnalysis
                                       _type.LPWSTR,  # localeName
                                       _type.UINT32,  # maxTagCount
                                       _Pointer[_type.UINT32],  # actualTagCount
                                       _Pointer[_enum.DWRITE_FONT_FEATURE_TAG]],  # tags
                                      _type.HRESULT]
    CheckTypographicFeature: _Callable[[_dwrite.IDWriteFontFace,  # fontFace
                                        _struct.DWRITE_SCRIPT_ANALYSIS,  # scriptAnalysis
                                        _type.LPWSTR,  # localeName
                                        _enum.DWRITE_FONT_FEATURE_TAG,  # featureTag
                                        _type.UINT32,  # glyphCount
                                        _Pointer[_type.UINT16],  # glyphIndices
                                        _Pointer[_type.UINT8]],  # featureApplies
                                       _type.HRESULT]


class IDWriteFontFallback(_Unknwnbase.IUnknown):
    MapCharacters: _Callable[[_dwrite.IDWriteTextAnalysisSource,  # analysisSource
                              _type.UINT32,  # textPosition
                              _type.UINT32,  # textLength
                              _dwrite.IDWriteFontCollection,  # baseFontCollection
                              _Pointer[_type.c_wchar_t],  # baseFamilyName
                              _enum.DWRITE_FONT_WEIGHT,  # baseWeight
                              _enum.DWRITE_FONT_STYLE,  # baseStyle
                              _enum.DWRITE_FONT_STRETCH,  # baseStretch
                              _Pointer[_type.UINT32],  # mappedLength
                              _Pointer[_dwrite.IDWriteFont],  # mappedFont
                              _Pointer[_type.FLOAT]],  # scale
                             _type.HRESULT]


class IDWriteFontFallbackBuilder(_Unknwnbase.IUnknown):
    AddMapping: _Callable[[_Pointer[_struct.DWRITE_UNICODE_RANGE],  # ranges
                           _type.UINT32,  # rangesCount
                           _Pointer[_type.LPWSTR],  # targetFamilyNames
                           _type.UINT32,  # targetFamilyNamesCount
                           _dwrite.IDWriteFontCollection,  # fontCollection
                           _type.LPWSTR,  # localeName
                           _type.LPWSTR,  # baseFamilyName
                           _type.FLOAT],  # scale
                          _type.HRESULT]
    AddMappings: _Callable[[IDWriteFontFallback],  # fontFallback
                           _type.HRESULT]
    CreateFontFallback: _Callable[[_Pointer[IDWriteFontFallback]],  # fontFallback
                                  _type.HRESULT]


class IDWriteFont2(_dwrite_1.IDWriteFont1):
    IsColorFont: _Callable[[],
                           _type.BOOL]


class IDWriteFontFace2(_dwrite_1.IDWriteFontFace1):
    IsColorFont: _Callable[[],
                           _type.BOOL]
    GetColorPaletteCount: _Callable[[],
                                    _type.UINT32]
    GetPaletteEntryCount: _Callable[[],
                                    _type.UINT32]
    GetPaletteEntries: _Callable[[_type.UINT32,  # colorPaletteIndex
                                  _type.UINT32,  # firstEntryIndex
                                  _type.UINT32,  # entryCount
                                  _Pointer[_struct.DWRITE_COLOR_F]],  # paletteEntries
                                 _type.HRESULT]
    GetRecommendedRenderingMode__: _Callable[[_type.FLOAT,  # fontEmSize
                                              _type.FLOAT,  # dpiX
                                              _type.FLOAT,  # dpiY
                                              _Pointer[_struct.DWRITE_MATRIX],  # transform
                                              _type.BOOL,  # isSideways
                                              _enum.DWRITE_OUTLINE_THRESHOLD,  # outlineThreshold
                                              _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                              _dwrite.IDWriteRenderingParams,  # renderingParams
                                              _Pointer[_enum.DWRITE_RENDERING_MODE],  # renderingMode
                                              _Pointer[_enum.DWRITE_GRID_FIT_MODE]],  # gridFitMode
                                             _type.HRESULT]


class IDWriteColorGlyphRunEnumerator(_Unknwnbase.IUnknown):
    MoveNext: _Callable[[_Pointer[_type.BOOL]],  # hasRun
                        _type.HRESULT]
    GetCurrentRun: _Callable[[_Pointer[_Pointer[_struct.DWRITE_COLOR_GLYPH_RUN]]],  # colorGlyphRun
                             _type.HRESULT]


class IDWriteRenderingParams2(_dwrite_1.IDWriteRenderingParams1):
    GetGridFitMode: _Callable[[],
                              _enum.DWRITE_GRID_FIT_MODE]


class IDWriteFactory2(_dwrite_1.IDWriteFactory1):
    GetSystemFontFallback: _Callable[[_Pointer[IDWriteFontFallback]],  # fontFallback
                                     _type.HRESULT]
    CreateFontFallbackBuilder: _Callable[[_Pointer[IDWriteFontFallbackBuilder]],  # fontFallbackBuilder
                                         _type.HRESULT]
    TranslateColorGlyphRun: _Callable[[_type.FLOAT,  # baselineOriginX
                                       _type.FLOAT,  # baselineOriginY
                                       _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                       _Pointer[_struct.DWRITE_GLYPH_RUN_DESCRIPTION],  # glyphRunDescription
                                       _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                       _Pointer[_struct.DWRITE_MATRIX],  # worldToDeviceTransform
                                       _type.UINT32,  # colorPaletteIndex
                                       _Pointer[IDWriteColorGlyphRunEnumerator]],  # colorLayers
                                      _type.HRESULT]
    CreateCustomRenderingParams__: _Callable[[_type.FLOAT,  # gamma
                                              _type.FLOAT,  # enhancedContrast
                                              _type.FLOAT,  # grayscaleEnhancedContrast
                                              _type.FLOAT,  # clearTypeLevel
                                              _enum.DWRITE_PIXEL_GEOMETRY,  # pixelGeometry
                                              _enum.DWRITE_RENDERING_MODE,  # renderingMode
                                              _enum.DWRITE_GRID_FIT_MODE,  # gridFitMode
                                              _Pointer[IDWriteRenderingParams2]],  # renderingParams
                                             _type.HRESULT]
    CreateGlyphRunAnalysis_: _Callable[[_Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                        _Pointer[_struct.DWRITE_MATRIX],  # transform
                                        _enum.DWRITE_RENDERING_MODE,  # renderingMode
                                        _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                        _enum.DWRITE_GRID_FIT_MODE,  # gridFitMode
                                        _enum.DWRITE_TEXT_ANTIALIAS_MODE,  # antialiasMode
                                        _type.FLOAT,  # baselineOriginX
                                        _type.FLOAT,  # baselineOriginY
                                        _Pointer[_dwrite.IDWriteGlyphRunAnalysis]],  # glyphRunAnalysis
                                       _type.HRESULT]
