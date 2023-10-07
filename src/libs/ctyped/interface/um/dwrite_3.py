from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import dwrite as _dwrite
from . import dwrite_2 as _dwrite_2
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IDWriteRenderingParams3(_dwrite_2.IDWriteRenderingParams2):
    GetRenderingMode1: _Callable[[],
                                 _enum.DWRITE_RENDERING_MODE1]


class IDWriteFactory3(_dwrite_2.IDWriteFactory2):
    CreateGlyphRunAnalysis__: _Callable[[_Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                         _Pointer[_struct.DWRITE_MATRIX],  # transform
                                         _enum.DWRITE_RENDERING_MODE1,  # renderingMode
                                         _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                         _enum.DWRITE_GRID_FIT_MODE,  # gridFitMode
                                         _enum.DWRITE_TEXT_ANTIALIAS_MODE,  # antialiasMode
                                         _type.FLOAT,  # baselineOriginX
                                         _type.FLOAT,  # baselineOriginY
                                         _Pointer[_dwrite.IDWriteGlyphRunAnalysis]],  # glyphRunAnalysis
                                        _type.HRESULT]
    CreateCustomRenderingParams___: _Callable[[_type.FLOAT,  # gamma
                                               _type.FLOAT,  # enhancedContrast
                                               _type.FLOAT,  # grayscaleEnhancedContrast
                                               _type.FLOAT,  # clearTypeLevel
                                               _enum.DWRITE_PIXEL_GEOMETRY,  # pixelGeometry
                                               _enum.DWRITE_RENDERING_MODE1,  # renderingMode
                                               _enum.DWRITE_GRID_FIT_MODE,  # gridFitMode
                                               _Pointer[IDWriteRenderingParams3]],  # renderingParams
                                              _type.HRESULT]
    CreateFontFaceReference: _Callable[[_dwrite.IDWriteFontFile,  # fontFile
                                        _type.UINT32,  # faceIndex
                                        _enum.DWRITE_FONT_SIMULATIONS,  # fontSimulations
                                        _Pointer[IDWriteFontFaceReference]],  # fontFaceReference
                                       _type.HRESULT]
    GetSystemFontSet: _Callable[[_Pointer[IDWriteFontSet]],  # fontSet
                                _type.HRESULT]
    CreateFontSetBuilder: _Callable[[_Pointer[IDWriteFontSetBuilder]],  # fontSetBuilder
                                    _type.HRESULT]
    CreateFontCollectionFromFontSet: _Callable[[IDWriteFontSet,  # fontSet
                                                _Pointer[IDWriteFontCollection1]],  # fontCollection
                                               _type.HRESULT]
    GetSystemFontCollection_: _Callable[[_type.BOOL,  # includeDownloadableFonts
                                         _Pointer[IDWriteFontCollection1],  # fontCollection
                                         _type.BOOL],  # checkForUpdates
                                        _type.HRESULT]
    GetFontDownloadQueue: _Callable[[_Pointer[IDWriteFontDownloadQueue]],  # fontDownloadQueue
                                    _type.HRESULT]


class IDWriteFontSet(_Unknwnbase.IUnknown):
    GetFontCount: _Callable[[],
                            _type.UINT32]
    GetFontFaceReference: _Callable[[_type.UINT32,  # listIndex
                                     _Pointer[IDWriteFontFaceReference]],  # fontFaceReference
                                    _type.HRESULT]
    FindFontFaceReference: _Callable[[IDWriteFontFaceReference,  # fontFaceReference
                                      _Pointer[_type.UINT32],  # listIndex
                                      _Pointer[_type.BOOL]],  # exists
                                     _type.HRESULT]
    FindFontFace: _Callable[[_dwrite.IDWriteFontFace,  # fontFace
                             _Pointer[_type.UINT32],  # listIndex
                             _Pointer[_type.BOOL]],  # exists
                            _type.HRESULT]
    GetPropertyValues: _Callable[[_enum.DWRITE_FONT_PROPERTY_ID,  # propertyID
                                  _Pointer[IDWriteStringList]],  # values
                                 _type.HRESULT]
    GetPropertyOccurrenceCount: _Callable[[_Pointer[_struct.DWRITE_FONT_PROPERTY],  # property
                                           _Pointer[_type.UINT32]],  # propertyOccurrenceCount
                                          _type.HRESULT]
    GetMatchingFonts: _Callable[[_type.LPWSTR,  # familyName
                                 _enum.DWRITE_FONT_WEIGHT,  # fontWeight
                                 _enum.DWRITE_FONT_STRETCH,  # fontStretch
                                 _enum.DWRITE_FONT_STYLE,  # fontStyle
                                 _Pointer[IDWriteFontSet]],  # filteredSet
                                _type.HRESULT]


class IDWriteFontSetBuilder(_Unknwnbase.IUnknown):
    AddFontFaceReference: _Callable[[IDWriteFontFaceReference,  # fontFaceReference
                                     _Pointer[_struct.DWRITE_FONT_PROPERTY],  # properties
                                     _type.UINT32],  # propertyCount
                                    _type.HRESULT]
    AddFontSet: _Callable[[IDWriteFontSet],  # fontSet
                          _type.HRESULT]
    CreateFontSet: _Callable[[_Pointer[IDWriteFontSet]],  # fontSet
                             _type.HRESULT]


class IDWriteFontCollection1(_dwrite.IDWriteFontCollection):
    GetFontSet: _Callable[[_Pointer[IDWriteFontSet]],  # fontSet
                          _type.HRESULT]
    GetFontFamily_: _Callable[[_type.UINT32,  # index
                               _Pointer[IDWriteFontFamily1]],  # fontFamily
                              _type.HRESULT]


class IDWriteFontFamily1(_dwrite.IDWriteFontFamily):
    GetFontLocality: _Callable[[_type.UINT32],  # listIndex
                               _enum.DWRITE_LOCALITY]
    GetFont_: _Callable[[_type.UINT32,  # listIndex
                         _Pointer[IDWriteFont3]],  # font
                        _type.HRESULT]
    GetFontFaceReference: _Callable[[_type.UINT32,  # listIndex
                                     _Pointer[IDWriteFontFaceReference]],  # fontFaceReference
                                    _type.HRESULT]


class IDWriteFontList1(_dwrite.IDWriteFontList):
    GetFontLocality: _Callable[[_type.UINT32],  # listIndex
                               _enum.DWRITE_LOCALITY]
    GetFont_: _Callable[[_type.UINT32,  # listIndex
                         _Pointer[IDWriteFont3]],  # font
                        _type.HRESULT]
    GetFontFaceReference: _Callable[[_type.UINT32,  # listIndex
                                     _Pointer[IDWriteFontFaceReference]],  # fontFaceReference
                                    _type.HRESULT]


class IDWriteFontFaceReference(_Unknwnbase.IUnknown):
    CreateFontFace: _Callable[[_Pointer[IDWriteFontFace3]],  # fontFace
                              _type.HRESULT]
    CreateFontFaceWithSimulations: _Callable[[_enum.DWRITE_FONT_SIMULATIONS,  # fontFaceSimulationFlags
                                              _Pointer[IDWriteFontFace3]],  # fontFace
                                             _type.HRESULT]
    Equals: _Callable[[IDWriteFontFaceReference],  # fontFaceReference
                      _type.BOOL]
    GetFontFaceIndex: _Callable[[],
                                _type.UINT32]
    GetSimulations: _Callable[[],
                              _enum.DWRITE_FONT_SIMULATIONS]
    GetFontFile: _Callable[[_Pointer[_dwrite.IDWriteFontFile]],  # fontFile
                           _type.HRESULT]
    GetLocalFileSize: _Callable[[],
                                _type.UINT64]
    GetFileSize: _Callable[[],
                           _type.UINT64]
    GetFileTime: _Callable[[_Pointer[_struct.FILETIME]],  # lastWriteTime
                           _type.HRESULT]
    GetLocality: _Callable[[],
                           _enum.DWRITE_LOCALITY]
    EnqueueFontDownloadRequest: _Callable[[],
                                          _type.HRESULT]
    EnqueueCharacterDownloadRequest: _Callable[[_type.LPWSTR,  # characters
                                                _type.UINT32],  # characterCount
                                               _type.HRESULT]
    EnqueueGlyphDownloadRequest: _Callable[[_Pointer[_type.UINT16],  # glyphIndices
                                            _type.UINT32],  # glyphCount
                                           _type.HRESULT]
    EnqueueFileFragmentDownloadRequest: _Callable[[_type.UINT64,  # fileOffset
                                                   _type.UINT64],  # fragmentSize
                                                  _type.HRESULT]


class IDWriteFont3(_dwrite_2.IDWriteFont2):
    CreateFontFace_: _Callable[[_Pointer[IDWriteFontFace3]],  # fontFace
                               _type.HRESULT]
    Equals: _Callable[[_dwrite.IDWriteFont],  # font
                      _type.BOOL]
    GetFontFaceReference: _Callable[[_Pointer[IDWriteFontFaceReference]],  # fontFaceReference
                                    _type.HRESULT]
    HasCharacter_: _Callable[[_type.UINT32],  # unicodeValue
                             _type.BOOL]
    GetLocality: _Callable[[],
                           _enum.DWRITE_LOCALITY]


class IDWriteFontFace3(_dwrite_2.IDWriteFontFace2):
    GetFontFaceReference: _Callable[[_Pointer[IDWriteFontFaceReference]],  # fontFaceReference
                                    _type.HRESULT]
    GetPanose: _Callable[[_Pointer[_union.DWRITE_PANOSE]],  # panose
                         _type.c_void]
    GetWeight: _Callable[[],
                         _enum.DWRITE_FONT_WEIGHT]
    GetStretch: _Callable[[],
                          _enum.DWRITE_FONT_STRETCH]
    GetStyle: _Callable[[],
                        _enum.DWRITE_FONT_STYLE]
    GetFamilyNames: _Callable[[_Pointer[_dwrite.IDWriteLocalizedStrings]],  # names
                              _type.HRESULT]
    GetFaceNames: _Callable[[_Pointer[_dwrite.IDWriteLocalizedStrings]],  # names
                            _type.HRESULT]
    GetInformationalStrings: _Callable[[_enum.DWRITE_INFORMATIONAL_STRING_ID,  # informationalStringID
                                        _Pointer[_dwrite.IDWriteLocalizedStrings],  # informationalStrings
                                        _Pointer[_type.BOOL]],  # exists
                                       _type.HRESULT]
    HasCharacter: _Callable[[_type.UINT32],  # unicodeValue
                            _type.BOOL]
    GetRecommendedRenderingMode___: _Callable[[_type.FLOAT,  # fontEmSize
                                               _type.FLOAT,  # dpiX
                                               _type.FLOAT,  # dpiY
                                               _Pointer[_struct.DWRITE_MATRIX],  # transform
                                               _type.BOOL,  # isSideways
                                               _enum.DWRITE_OUTLINE_THRESHOLD,  # outlineThreshold
                                               _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                               _dwrite.IDWriteRenderingParams,  # renderingParams
                                               _Pointer[_enum.DWRITE_RENDERING_MODE1],  # renderingMode
                                               _Pointer[_enum.DWRITE_GRID_FIT_MODE]],  # gridFitMode
                                              _type.HRESULT]
    IsCharacterLocal: _Callable[[_type.UINT32],  # unicodeValue
                                _type.BOOL]
    IsGlyphLocal: _Callable[[_type.UINT16],  # glyphId
                            _type.BOOL]
    AreCharactersLocal: _Callable[[_type.LPWSTR,  # characters
                                   _type.UINT32,  # characterCount
                                   _type.BOOL,  # enqueueIfNotLocal
                                   _Pointer[_type.BOOL]],  # isLocal
                                  _type.HRESULT]
    AreGlyphsLocal: _Callable[[_Pointer[_type.UINT16],  # glyphIndices
                               _type.UINT32,  # glyphCount
                               _type.BOOL,  # enqueueIfNotLocal
                               _Pointer[_type.BOOL]],  # isLocal
                              _type.HRESULT]


class IDWriteStringList(_Unknwnbase.IUnknown):
    GetCount: _Callable[[],
                        _type.UINT32]
    GetLocaleNameLength: _Callable[[_type.UINT32,  # listIndex
                                    _Pointer[_type.UINT32]],  # length
                                   _type.HRESULT]
    GetLocaleName: _Callable[[_type.UINT32,  # listIndex
                              _type.LPWSTR,  # localeName
                              _type.UINT32],  # size
                             _type.HRESULT]
    GetStringLength: _Callable[[_type.UINT32,  # listIndex
                                _Pointer[_type.UINT32]],  # length
                               _type.HRESULT]
    GetString: _Callable[[_type.UINT32,  # listIndex
                          _type.LPWSTR,  # stringBuffer
                          _type.UINT32],  # stringBufferSize
                         _type.HRESULT]


class IDWriteFontDownloadListener(_Unknwnbase.IUnknown):
    DownloadCompleted: _Callable[[IDWriteFontDownloadQueue,  # downloadQueue
                                  _Unknwnbase.IUnknown,  # context
                                  _type.HRESULT],  # downloadResult
                                 _type.c_void]


class IDWriteFontDownloadQueue(_Unknwnbase.IUnknown):
    AddListener: _Callable[[IDWriteFontDownloadListener,  # listener
                            _Pointer[_type.UINT32]],  # token
                           _type.HRESULT]
    RemoveListener: _Callable[[_type.UINT32],  # token
                              _type.HRESULT]
    IsEmpty: _Callable[[],
                       _type.BOOL]
    BeginDownload: _Callable[[_Unknwnbase.IUnknown],  # context
                             _type.HRESULT]
    CancelDownload: _Callable[[],
                              _type.HRESULT]
    GetGenerationCount: _Callable[[],
                                  _type.UINT64]


class IDWriteGdiInterop1(_dwrite.IDWriteGdiInterop):
    CreateFontFromLOGFONT_: _Callable[[_Pointer[_struct.LOGFONTW],  # logFont
                                       _dwrite.IDWriteFontCollection,  # fontCollection
                                       _Pointer[_dwrite.IDWriteFont]],  # font
                                      _type.HRESULT]
    GetFontSignature: _Callable[[_dwrite.IDWriteFontFace,  # fontFace
                                 _Pointer[_struct.FONTSIGNATURE]],  # fontSignature
                                _type.HRESULT]
    GetMatchingFontsByLOGFONT: _Callable[[_Pointer[_struct.LOGFONT],  # logFont
                                          IDWriteFontSet,  # fontSet
                                          _Pointer[IDWriteFontSet]],  # filteredSet
                                         _type.HRESULT]


class IDWriteTextFormat2(_dwrite_2.IDWriteTextFormat1):
    SetLineSpacing_: _Callable[[_Pointer[_struct.DWRITE_LINE_SPACING]],  # lineSpacingOptions
                               _type.HRESULT]
    GetLineSpacing_: _Callable[[_Pointer[_struct.DWRITE_LINE_SPACING]],  # lineSpacingOptions
                               _type.HRESULT]


class IDWriteTextLayout3(_dwrite_2.IDWriteTextLayout2):
    InvalidateLayout: _Callable[[],
                                _type.HRESULT]
    SetLineSpacing_: _Callable[[_Pointer[_struct.DWRITE_LINE_SPACING]],  # lineSpacingOptions
                               _type.HRESULT]
    GetLineSpacing_: _Callable[[_Pointer[_struct.DWRITE_LINE_SPACING]],  # lineSpacingOptions
                               _type.HRESULT]
    GetLineMetrics_: _Callable[[_Pointer[_struct.DWRITE_LINE_METRICS1],  # lineMetrics
                                _type.UINT32,  # maxLineCount
                                _Pointer[_type.UINT32]],  # actualLineCount
                               _type.HRESULT]


class IDWriteColorGlyphRunEnumerator1(_dwrite_2.IDWriteColorGlyphRunEnumerator):
    GetCurrentRun_: _Callable[[_Pointer[_Pointer[_struct.DWRITE_COLOR_GLYPH_RUN1]]],  # colorGlyphRun
                              _type.HRESULT]


class IDWriteFontFace4(IDWriteFontFace3):
    GetGlyphImageFormats: _Callable[[_type.UINT16,  # glyphId
                                     _type.UINT32,  # pixelsPerEmFirst
                                     _type.UINT32,  # pixelsPerEmLast
                                     _Pointer[_enum.DWRITE_GLYPH_IMAGE_FORMATS]],  # glyphImageFormats
                                    _type.HRESULT]
    GetGlyphImageData: _Callable[[_type.UINT16,  # glyphId
                                  _type.UINT32,  # pixelsPerEm
                                  _enum.DWRITE_GLYPH_IMAGE_FORMATS,  # glyphImageFormat
                                  _Pointer[_struct.DWRITE_GLYPH_IMAGE_DATA],  # glyphData
                                  _type.c_void_p],  # glyphDataContext
                                 _type.HRESULT]
    ReleaseGlyphImageData: _Callable[[_type.c_void_p],  # glyphDataContext
                                     _type.c_void]


class IDWriteFactory4(IDWriteFactory3):
    TranslateColorGlyphRun_: _Callable[[_struct.D2D1_POINT_2F,  # baselineOrigin
                                        _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                        _Pointer[_struct.DWRITE_GLYPH_RUN_DESCRIPTION],  # glyphRunDescription
                                        _enum.DWRITE_GLYPH_IMAGE_FORMATS,  # desiredGlyphImageFormats
                                        _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                        _Pointer[_struct.DWRITE_MATRIX],  # worldAndDpiTransform
                                        _type.UINT32,  # colorPaletteIndex
                                        _Pointer[IDWriteColorGlyphRunEnumerator1]],  # colorLayers
                                       _type.HRESULT]
    ComputeGlyphOrigins: _Callable[[_Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                    _struct.D2D1_POINT_2F,  # baselineOrigin
                                    _Pointer[_struct.D2D1_POINT_2F]],  # glyphOrigins
                                   _type.HRESULT]


class IDWriteFontSetBuilder1(IDWriteFontSetBuilder):
    AddFontFile: _Callable[[_dwrite.IDWriteFontFile],  # fontFile
                           _type.HRESULT]


class IDWriteAsyncResult(_Unknwnbase.IUnknown):
    GetWaitHandle: _Callable[[],
                             _type.HANDLE]
    GetResult: _Callable[[],
                         _type.HRESULT]


class IDWriteRemoteFontFileStream(_dwrite.IDWriteFontFileStream):
    GetLocalFileSize: _Callable[[_Pointer[_type.UINT64]],  # localFileSize
                                _type.HRESULT]
    GetFileFragmentLocality: _Callable[[_type.UINT64,  # fileOffset
                                        _type.UINT64,  # fragmentSize
                                        _Pointer[_type.BOOL],  # isLocal
                                        _Pointer[_type.UINT64]],  # partialSize
                                       _type.HRESULT]
    GetLocality: _Callable[[],
                           _enum.DWRITE_LOCALITY]
    BeginDownload: _Callable[[_Pointer[_struct.UUID],  # downloadOperationID
                              _Pointer[_struct.DWRITE_FILE_FRAGMENT],  # fileFragments
                              _type.UINT32,  # fragmentCount
                              _Pointer[IDWriteAsyncResult]],  # asyncResult
                             _type.HRESULT]


class IDWriteRemoteFontFileLoader(_dwrite.IDWriteFontFileLoader):
    CreateRemoteStreamFromKey: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                          _type.UINT32,  # fontFileReferenceKeySize
                                          _Pointer[IDWriteRemoteFontFileStream]],  # fontFileStream
                                         _type.HRESULT]
    GetLocalityFromKey: _Callable[[_type.c_void_p,  # fontFileReferenceKey
                                   _type.UINT32,  # fontFileReferenceKeySize
                                   _Pointer[_enum.DWRITE_LOCALITY]],  # locality
                                  _type.HRESULT]
    CreateFontFileReferenceFromUrl: _Callable[[_dwrite.IDWriteFactory,  # factory
                                               _type.LPWSTR,  # baseUrl
                                               _type.LPWSTR,  # fontFileUrl
                                               _Pointer[_dwrite.IDWriteFontFile]],  # fontFile
                                              _type.HRESULT]


class IDWriteInMemoryFontFileLoader(_dwrite.IDWriteFontFileLoader):
    CreateInMemoryFontFileReference: _Callable[[_dwrite.IDWriteFactory,  # factory
                                                _type.c_void_p,  # fontData
                                                _type.UINT32,  # fontDataSize
                                                _Unknwnbase.IUnknown,  # ownerObject
                                                _Pointer[_dwrite.IDWriteFontFile]],  # fontFile
                                               _type.HRESULT]
    GetFileCount: _Callable[[],
                            _type.UINT32]


class IDWriteFactory5(IDWriteFactory4):
    CreateFontSetBuilder_: _Callable[[_Pointer[IDWriteFontSetBuilder1]],  # fontSetBuilder
                                     _type.HRESULT]
    CreateInMemoryFontFileLoader: _Callable[[_Pointer[IDWriteInMemoryFontFileLoader]],  # newLoader
                                            _type.HRESULT]
    CreateHttpFontFileLoader: _Callable[[_Pointer[_type.c_wchar_t],  # referrerUrl
                                         _Pointer[_type.c_wchar_t],  # extraHeaders
                                         _Pointer[IDWriteRemoteFontFileLoader]],  # newLoader
                                        _type.HRESULT]
    AnalyzeContainerType: _Callable[[_type.c_void_p,  # fileData
                                     _type.UINT32],  # fileDataSize
                                    _enum.DWRITE_CONTAINER_TYPE]
    UnpackFontFile: _Callable[[_enum.DWRITE_CONTAINER_TYPE,  # containerType
                               _type.c_void_p,  # fileData
                               _type.UINT32,  # fileDataSize
                               _Pointer[_dwrite.IDWriteFontFileStream]],  # unpackedFontStream
                              _type.HRESULT]


class IDWriteFactory6(IDWriteFactory5):
    CreateFontFaceReference_: _Callable[[_dwrite.IDWriteFontFile,  # fontFile
                                         _type.UINT32,  # faceIndex
                                         _enum.DWRITE_FONT_SIMULATIONS,  # fontSimulations
                                         _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                         _type.UINT32,  # fontAxisValueCount
                                         _Pointer[IDWriteFontFaceReference1]],  # fontFaceReference
                                        _type.HRESULT]
    CreateFontResource: _Callable[[_dwrite.IDWriteFontFile,  # fontFile
                                   _type.UINT32,  # faceIndex
                                   _Pointer[IDWriteFontResource]],  # fontResource
                                  _type.HRESULT]
    GetSystemFontSet_: _Callable[[_type.BOOL,  # includeDownloadableFonts
                                  _Pointer[IDWriteFontSet1]],  # fontSet
                                 _type.HRESULT]
    GetSystemFontCollection__: _Callable[[_type.BOOL,  # includeDownloadableFonts
                                          _enum.DWRITE_FONT_FAMILY_MODEL,  # fontFamilyModel
                                          _Pointer[IDWriteFontCollection2]],  # fontCollection
                                         _type.HRESULT]
    CreateFontCollectionFromFontSet_: _Callable[[IDWriteFontSet,  # fontSet
                                                 _enum.DWRITE_FONT_FAMILY_MODEL,  # fontFamilyModel
                                                 _Pointer[IDWriteFontCollection2]],  # fontCollection
                                                _type.HRESULT]
    CreateFontSetBuilder__: _Callable[[_Pointer[IDWriteFontSetBuilder2]],  # fontSetBuilder
                                      _type.HRESULT]
    CreateTextFormat_: _Callable[[_type.LPWSTR,  # fontFamilyName
                                  _dwrite.IDWriteFontCollection,  # fontCollection
                                  _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32,  # fontAxisValueCount
                                  _type.FLOAT,  # fontSize
                                  _type.LPWSTR,  # localeName
                                  _Pointer[IDWriteTextFormat3]],  # textFormat
                                 _type.HRESULT]


class IDWriteFontFace5(IDWriteFontFace4):
    GetFontAxisValueCount: _Callable[[],
                                     _type.UINT32]
    GetFontAxisValues: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32],  # fontAxisValueCount
                                 _type.HRESULT]
    HasVariations: _Callable[[],
                             _type.BOOL]
    GetFontResource: _Callable[[_Pointer[IDWriteFontResource]],  # fontResource
                               _type.HRESULT]
    Equals: _Callable[[_dwrite.IDWriteFontFace],  # fontFace
                      _type.BOOL]


class IDWriteFontResource(_Unknwnbase.IUnknown):
    GetFontFile: _Callable[[_Pointer[_dwrite.IDWriteFontFile]],  # fontFile
                           _type.HRESULT]
    GetFontFaceIndex: _Callable[[],
                                _type.UINT32]
    GetFontAxisCount: _Callable[[],
                                _type.UINT32]
    GetDefaultFontAxisValues: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                         _type.UINT32],  # fontAxisValueCount
                                        _type.HRESULT]
    GetFontAxisRanges: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_RANGE],  # fontAxisRanges
                                  _type.UINT32],  # fontAxisRangeCount
                                 _type.HRESULT]
    GetFontAxisAttributes: _Callable[[_type.UINT32],  # axisIndex
                                     _enum.DWRITE_FONT_AXIS_ATTRIBUTES]
    GetAxisNames: _Callable[[_type.UINT32,  # axisIndex
                             _Pointer[_dwrite.IDWriteLocalizedStrings]],  # names
                            _type.HRESULT]
    GetAxisValueNameCount: _Callable[[_type.UINT32],  # axisIndex
                                     _type.UINT32]
    GetAxisValueNames: _Callable[[_type.UINT32,  # axisIndex
                                  _type.UINT32,  # axisValueIndex
                                  _Pointer[_struct.DWRITE_FONT_AXIS_RANGE],  # fontAxisRange
                                  _Pointer[_dwrite.IDWriteLocalizedStrings]],  # names
                                 _type.HRESULT]
    HasVariations: _Callable[[],
                             _type.BOOL]
    CreateFontFace: _Callable[[_enum.DWRITE_FONT_SIMULATIONS,  # fontSimulations
                               _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                               _type.UINT32,  # fontAxisValueCount
                               _Pointer[IDWriteFontFace5]],  # fontFace
                              _type.HRESULT]
    CreateFontFaceReference: _Callable[[_enum.DWRITE_FONT_SIMULATIONS,  # fontSimulations
                                        _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                        _type.UINT32,  # fontAxisValueCount
                                        _Pointer[IDWriteFontFaceReference1]],  # fontFaceReference
                                       _type.HRESULT]


class IDWriteFontFaceReference1(IDWriteFontFaceReference):
    CreateFontFace_: _Callable[[_Pointer[IDWriteFontFace5]],  # fontFace
                               _type.HRESULT]
    GetFontAxisValueCount: _Callable[[],
                                     _type.UINT32]
    GetFontAxisValues: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32],  # fontAxisValueCount
                                 _type.HRESULT]


class IDWriteFontSetBuilder2(IDWriteFontSetBuilder1):
    AddFont: _Callable[[_dwrite.IDWriteFontFile,  # fontFile
                        _type.UINT32,  # fontFaceIndex
                        _enum.DWRITE_FONT_SIMULATIONS,  # fontSimulations
                        _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                        _type.UINT32,  # fontAxisValueCount
                        _Pointer[_struct.DWRITE_FONT_AXIS_RANGE],  # fontAxisRanges
                        _type.UINT32,  # fontAxisRangeCount
                        _Pointer[_struct.DWRITE_FONT_PROPERTY],  # properties
                        _type.UINT32],  # propertyCount
                       _type.HRESULT]
    AddFontFile_: _Callable[[_type.LPWSTR],  # filePath
                            _type.HRESULT]


class IDWriteFontSet1(IDWriteFontSet):
    GetMatchingFonts_: _Callable[[_Pointer[_struct.DWRITE_FONT_PROPERTY],  # fontProperty
                                  _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32,  # fontAxisValueCount
                                  _Pointer[IDWriteFontSet1]],  # matchingFonts
                                 _type.HRESULT]
    GetFirstFontResources: _Callable[[_Pointer[IDWriteFontSet1]],  # filteredFontSet
                                     _type.HRESULT]
    GetFilteredFonts: _Callable[[_Pointer[_type.UINT32],  # indices
                                 _type.UINT32,  # indexCount
                                 _Pointer[IDWriteFontSet1]],  # filteredFontSet
                                _type.HRESULT]
    GetFilteredFontIndices: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_RANGE],  # fontAxisRanges
                                       _type.UINT32,  # fontAxisRangeCount
                                       _type.BOOL,  # selectAnyRange
                                       _Pointer[_type.UINT32],  # indices
                                       _type.UINT32,  # maxIndexCount
                                       _Pointer[_type.UINT32]],  # actualIndexCount
                                      _type.HRESULT]
    GetFontAxisRanges: _Callable[[_type.UINT32,  # listIndex
                                  _Pointer[_struct.DWRITE_FONT_AXIS_RANGE],  # fontAxisRanges
                                  _type.UINT32,  # maxFontAxisRangeCount
                                  _Pointer[_type.UINT32]],  # actualFontAxisRangeCount
                                 _type.HRESULT]
    GetFontFaceReference_: _Callable[[_type.UINT32,  # listIndex
                                      _Pointer[IDWriteFontFaceReference1]],  # fontFaceReference
                                     _type.HRESULT]
    CreateFontResource: _Callable[[_type.UINT32,  # listIndex
                                   _Pointer[IDWriteFontResource]],  # fontResource
                                  _type.HRESULT]
    CreateFontFace: _Callable[[_type.UINT32,  # listIndex
                               _Pointer[IDWriteFontFace5]],  # fontFace
                              _type.HRESULT]
    GetFontLocality: _Callable[[_type.UINT32],  # listIndex
                               _enum.DWRITE_LOCALITY]


class IDWriteFontList2(IDWriteFontList1):
    GetFontSet: _Callable[[_Pointer[IDWriteFontSet1]],  # fontSet
                          _type.HRESULT]


class IDWriteFontFamily2(IDWriteFontFamily1):
    GetMatchingFonts_: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32,  # fontAxisValueCount
                                  _Pointer[IDWriteFontList2]],  # matchingFonts
                                 _type.HRESULT]
    GetFontSet: _Callable[[_Pointer[IDWriteFontSet1]],  # fontSet
                          _type.HRESULT]


class IDWriteFontCollection2(IDWriteFontCollection1):
    GetFontFamily__: _Callable[[_type.UINT32,  # index
                                _Pointer[IDWriteFontFamily2]],  # fontFamily
                               _type.HRESULT]
    GetMatchingFonts: _Callable[[_type.LPWSTR,  # familyName
                                 _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                 _type.UINT32,  # fontAxisValueCount
                                 _Pointer[IDWriteFontList2]],  # fontList
                                _type.HRESULT]
    GetFontFamilyModel: _Callable[[],
                                  _enum.DWRITE_FONT_FAMILY_MODEL]
    GetFontSet_: _Callable[[_Pointer[IDWriteFontSet1]],  # fontSet
                           _type.HRESULT]


class IDWriteTextLayout4(IDWriteTextLayout3):
    SetFontAxisValues: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32,  # fontAxisValueCount
                                  _struct.DWRITE_TEXT_RANGE],  # textRange
                                 _type.HRESULT]
    GetFontAxisValueCount: _Callable[[_type.UINT32],  # currentPosition
                                     _type.UINT32]
    GetFontAxisValues: _Callable[[_type.UINT32,  # currentPosition
                                  _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32,  # fontAxisValueCount
                                  _Pointer[_struct.DWRITE_TEXT_RANGE]],  # textRange
                                 _type.HRESULT]
    GetAutomaticFontAxes: _Callable[[],
                                    _enum.DWRITE_AUTOMATIC_FONT_AXES]
    SetAutomaticFontAxes: _Callable[[_enum.DWRITE_AUTOMATIC_FONT_AXES],  # automaticFontAxes
                                    _type.HRESULT]


class IDWriteTextFormat3(IDWriteTextFormat2):
    SetFontAxisValues: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32],  # fontAxisValueCount
                                 _type.HRESULT]
    GetFontAxisValueCount: _Callable[[],
                                     _type.UINT32]
    GetFontAxisValues: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                  _type.UINT32],  # fontAxisValueCount
                                 _type.HRESULT]
    GetAutomaticFontAxes: _Callable[[],
                                    _enum.DWRITE_AUTOMATIC_FONT_AXES]
    SetAutomaticFontAxes: _Callable[[_enum.DWRITE_AUTOMATIC_FONT_AXES],  # automaticFontAxes
                                    _type.HRESULT]


class IDWriteFontFallback1(_dwrite_2.IDWriteFontFallback):
    MapCharacters_: _Callable[[_dwrite.IDWriteTextAnalysisSource,  # analysisSource
                               _type.UINT32,  # textPosition
                               _type.UINT32,  # textLength
                               _dwrite.IDWriteFontCollection,  # baseFontCollection
                               _type.LPWSTR,  # baseFamilyName
                               _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                               _type.UINT32,  # fontAxisValueCount
                               _Pointer[_type.UINT32],  # mappedLength
                               _Pointer[_type.FLOAT],  # scale
                               _Pointer[IDWriteFontFace5]],  # mappedFontFace
                              _type.HRESULT]


class IDWriteFontSet2(IDWriteFontSet1):
    GetExpirationEvent: _Callable[[],
                                  _type.HANDLE]


class IDWriteFontCollection3(IDWriteFontCollection2):
    GetExpirationEvent: _Callable[[],
                                  _type.HANDLE]


class IDWriteFactory7(IDWriteFactory6):
    GetSystemFontSet__: _Callable[[_type.BOOL,  # includeDownloadableFonts
                                   _Pointer[IDWriteFontSet2]],  # fontSet
                                  _type.HRESULT]
    GetSystemFontCollection___: _Callable[[_type.BOOL,  # includeDownloadableFonts
                                           _enum.DWRITE_FONT_FAMILY_MODEL,  # fontFamilyModel
                                           _Pointer[IDWriteFontCollection3]],  # fontCollection
                                          _type.HRESULT]


class IDWriteFontSet3(IDWriteFontSet2):
    GetFontSourceType: _Callable[[_type.UINT32],  # fontIndex
                                 _enum.DWRITE_FONT_SOURCE_TYPE]
    GetFontSourceNameLength: _Callable[[_type.UINT32],  # listIndex
                                       _type.UINT32]
    GetFontSourceName: _Callable[[_type.UINT32,  # listIndex
                                  _type.LPWSTR,  # stringBuffer
                                  _type.UINT32],  # stringBufferSize
                                 _type.HRESULT]


class IDWriteFontFace6(IDWriteFontFace5):
    GetFamilyNames_: _Callable[[_enum.DWRITE_FONT_FAMILY_MODEL,  # fontFamilyModel
                                _Pointer[_dwrite.IDWriteLocalizedStrings]],  # names
                               _type.HRESULT]
    GetFaceNames_: _Callable[[_enum.DWRITE_FONT_FAMILY_MODEL,  # fontFamilyModel
                              _Pointer[_dwrite.IDWriteLocalizedStrings]],  # names
                             _type.HRESULT]


class IDWriteFontSet4(IDWriteFontSet3):
    ConvertWeightStretchStyleToFontAxisValues: _Callable[[_Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # inputAxisValues
                                                          _type.UINT32,  # inputAxisCount
                                                          _enum.DWRITE_FONT_WEIGHT,  # fontWeight
                                                          _enum.DWRITE_FONT_STRETCH,  # fontStretch
                                                          _enum.DWRITE_FONT_STYLE,  # fontStyle
                                                          _type.c_float,  # fontSize
                                                          _Pointer[_struct.DWRITE_FONT_AXIS_VALUE]],  # outputAxisValues
                                                         _type.UINT32]
    GetMatchingFonts__: _Callable[[_type.LPWSTR,  # familyName
                                   _Pointer[_struct.DWRITE_FONT_AXIS_VALUE],  # fontAxisValues
                                   _type.UINT32,  # fontAxisValueCount
                                   _enum.DWRITE_FONT_SIMULATIONS,  # allowedSimulations
                                   _Pointer[IDWriteFontSet4]],  # matchingFonts
                                  _type.HRESULT]
