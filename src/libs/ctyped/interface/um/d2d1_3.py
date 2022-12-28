from __future__ import annotations as _

from typing import Callable as _Callable

from . import d2d1 as _d2d1
from . import d2d1_1 as _d2d1_1
from . import d2d1_2 as _d2d1_2
from . import d2d1svg as _d2d1svg
from . import dwrite as _dwrite
from . import objidlbase as _objidlbase
from . import wincodec as _wincodec
from ..shared import dxgi as _dxgi
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID2D1InkStyle(_d2d1.ID2D1Resource):
    SetNibTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                               _type.c_void]
    GetNibTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                               _type.c_void]
    SetNibShape: _Callable[[_enum.D2D1_INK_NIB_SHAPE],  # nibShape
                           _type.c_void]
    GetNibShape: _Callable[[],
                           _enum.D2D1_INK_NIB_SHAPE]


class ID2D1Ink(_d2d1.ID2D1Resource):
    SetStartPoint: _Callable[[_Pointer[_struct.D2D1_INK_POINT]],  # startPoint
                             _type.c_void]
    GetStartPoint: _Callable[[],
                             _struct.D2D1_INK_POINT]
    AddSegments: _Callable[[_Pointer[_struct.D2D1_INK_BEZIER_SEGMENT],  # segments
                            _type.UINT32],  # segmentsCount
                           _type.HRESULT]
    RemoveSegmentsAtEnd: _Callable[[_type.UINT32],  # segmentsCount
                                   _type.HRESULT]
    SetSegments: _Callable[[_type.UINT32,  # startSegment
                            _Pointer[_struct.D2D1_INK_BEZIER_SEGMENT],  # segments
                            _type.UINT32],  # segmentsCount
                           _type.HRESULT]
    SetSegmentAtEnd: _Callable[[_Pointer[_struct.D2D1_INK_BEZIER_SEGMENT]],  # segment
                               _type.HRESULT]
    GetSegmentCount: _Callable[[],
                               _type.UINT32]
    GetSegments: _Callable[[_type.UINT32,  # startSegment
                            _Pointer[_struct.D2D1_INK_BEZIER_SEGMENT],  # segments
                            _type.UINT32],  # segmentsCount
                           _type.HRESULT]
    StreamAsGeometry: _Callable[[ID2D1InkStyle,  # inkStyle
                                 _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                 _type.FLOAT,  # flatteningTolerance
                                 _d2d1.ID2D1SimplifiedGeometrySink],  # geometrySink
                                _type.HRESULT]
    GetBounds: _Callable[[ID2D1InkStyle,  # inkStyle
                          _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                          _Pointer[_struct.D2D1_RECT_F]],  # bounds
                         _type.HRESULT]


class ID2D1GradientMesh(_d2d1.ID2D1Resource):
    GetPatchCount: _Callable[[],
                             _type.UINT32]
    GetPatches: _Callable[[_type.UINT32,  # startIndex
                           _Pointer[_struct.D2D1_GRADIENT_MESH_PATCH],  # patches
                           _type.UINT32],  # patchesCount
                          _type.HRESULT]


class ID2D1ImageSource(_d2d1.ID2D1Image):
    OfferResources: _Callable[[],
                              _type.HRESULT]
    TryReclaimResources: _Callable[[_Pointer[_type.BOOL]],  # resourcesDiscarded
                                   _type.HRESULT]


class ID2D1ImageSourceFromWic(ID2D1ImageSource):
    EnsureCached: _Callable[[_Pointer[_struct.D2D1_RECT_U]],  # rectangleToFill
                            _type.HRESULT]
    TrimCache: _Callable[[_Pointer[_struct.D2D1_RECT_U]],  # rectangleToPreserve
                         _type.HRESULT]
    GetSource: _Callable[[_Pointer[_Pointer[_wincodec.IWICBitmapSource]]],  # wicBitmapSource
                         _type.c_void]


class ID2D1TransformedImageSource(_d2d1.ID2D1Image):
    GetSource: _Callable[[_Pointer[ID2D1ImageSource]],  # imageSource
                         _type.c_void]
    GetProperties: _Callable[[_Pointer[_struct.D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES]],  # properties
                             _type.c_void]


class ID2D1LookupTable3D(_d2d1.ID2D1Resource):
    pass


class ID2D1DeviceContext2(_d2d1_2.ID2D1DeviceContext1):
    CreateInk: _Callable[[_Pointer[_struct.D2D1_INK_POINT],  # startPoint
                          _Pointer[ID2D1Ink]],  # ink
                         _type.HRESULT]
    CreateInkStyle: _Callable[[_Pointer[_struct.D2D1_INK_STYLE_PROPERTIES],  # inkStyleProperties
                               _Pointer[ID2D1InkStyle]],  # inkStyle
                              _type.HRESULT]
    CreateGradientMesh: _Callable[[_Pointer[_struct.D2D1_GRADIENT_MESH_PATCH],  # patches
                                   _type.UINT32,  # patchesCount
                                   _Pointer[ID2D1GradientMesh]],  # gradientMesh
                                  _type.HRESULT]
    CreateImageSourceFromWic: _Callable[[_Pointer[_wincodec.IWICBitmapSource],  # wicBitmapSource
                                         _enum.D2D1_IMAGE_SOURCE_LOADING_OPTIONS,  # loadingOptions
                                         _enum.D2D1_ALPHA_MODE,  # alphaMode
                                         _Pointer[ID2D1ImageSourceFromWic]],  # imageSource
                                        _type.HRESULT]
    CreateLookupTable3D: _Callable[[_enum.D2D1_BUFFER_PRECISION,  # precision
                                    _Pointer[_type.UINT32],  # extents
                                    _Pointer[_type.BYTE],  # data
                                    _type.UINT32,  # dataCount
                                    _Pointer[_type.UINT32],  # strides
                                    _Pointer[ID2D1LookupTable3D]],  # lookupTable
                                   _type.HRESULT]
    CreateImageSourceFromDxgi: _Callable[[_Pointer[_dxgi.IDXGISurface],  # surfaces
                                          _type.UINT32,  # surfaceCount
                                          _enum.DXGI_COLOR_SPACE_TYPE,  # colorSpace
                                          _enum.D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS,  # options
                                          _Pointer[ID2D1ImageSource]],  # imageSource
                                         _type.HRESULT]
    GetGradientMeshWorldBounds: _Callable[[ID2D1GradientMesh,  # gradientMesh
                                           _Pointer[_struct.D2D1_RECT_F]],  # pBounds
                                          _type.HRESULT]
    DrawInk: _Callable[[ID2D1Ink,  # ink
                        _d2d1.ID2D1Brush,  # brush
                        ID2D1InkStyle],  # inkStyle
                       _type.c_void]
    DrawGradientMesh: _Callable[[ID2D1GradientMesh],  # gradientMesh
                                _type.c_void]
    DrawGdiMetafile_: _Callable[[_d2d1_1.ID2D1GdiMetafile,  # gdiMetafile
                                 _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                                 _Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                                _type.c_void]
    CreateTransformedImageSource: _Callable[[ID2D1ImageSource,  # imageSource
                                             _Pointer[_struct.D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES],  # properties
                                             _Pointer[ID2D1TransformedImageSource]],  # transformedImageSource
                                            _type.HRESULT]


class ID2D1Device2(_d2d1_2.ID2D1Device1):
    CreateDeviceContext__: _Callable[[_enum.D2D1_DEVICE_CONTEXT_OPTIONS,  # options
                                      _Pointer[ID2D1DeviceContext2]],  # deviceContext2
                                     _type.HRESULT]
    FlushDeviceContexts: _Callable[[_d2d1.ID2D1Bitmap],  # bitmap
                                   _type.c_void]
    GetDxgiDevice: _Callable[[_Pointer[_dxgi.IDXGIDevice]],  # dxgiDevice
                             _type.HRESULT]


class ID2D1Factory3(_d2d1_2.ID2D1Factory2):
    CreateDevice__: _Callable[[_dxgi.IDXGIDevice,  # dxgiDevice
                               _Pointer[ID2D1Device2]],  # d2dDevice2
                              _type.HRESULT]


class ID2D1CommandSink2(_d2d1_2.ID2D1CommandSink1):
    DrawInk: _Callable[[ID2D1Ink,  # ink
                        _d2d1.ID2D1Brush,  # brush
                        ID2D1InkStyle],  # inkStyle
                       _type.HRESULT]
    DrawGradientMesh: _Callable[[ID2D1GradientMesh],  # gradientMesh
                                _type.HRESULT]
    DrawGdiMetafile_: _Callable[[_d2d1_1.ID2D1GdiMetafile,  # gdiMetafile
                                 _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                                 _Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                                _type.HRESULT]


class ID2D1GdiMetafile1(_d2d1_1.ID2D1GdiMetafile):
    GetDpi: _Callable[[_Pointer[_type.FLOAT],  # dpiX
                       _Pointer[_type.FLOAT]],  # dpiY
                      _type.HRESULT]
    GetSourceBounds: _Callable[[_Pointer[_struct.D2D1_RECT_F]],  # bounds
                               _type.HRESULT]


class ID2D1GdiMetafileSink1(_d2d1_1.ID2D1GdiMetafileSink):
    ProcessRecord_: _Callable[[_type.DWORD,  # recordType
                               _type.c_void_p,  # recordData
                               _type.DWORD,  # recordDataSize
                               _type.UINT32],  # flags
                              _type.HRESULT]


class ID2D1SpriteBatch(_d2d1.ID2D1Resource):
    AddSprites: _Callable[[_type.UINT32,  # spriteCount
                           _Pointer[_struct.D2D1_RECT_F],  # destinationRectangles
                           _Pointer[_struct.D2D1_RECT_U],  # sourceRectangles
                           _Pointer[_struct.D2D1_COLOR_F],  # colors
                           _Pointer[_struct.D2D1_MATRIX_3X2_F],  # transforms
                           _type.UINT32,  # destinationRectanglesStride
                           _type.UINT32,  # sourceRectanglesStride
                           _type.UINT32,  # colorsStride
                           _type.UINT32],  # transformsStride
                          _type.HRESULT]
    SetSprites: _Callable[[_type.UINT32,  # startIndex
                           _type.UINT32,  # spriteCount
                           _Pointer[_struct.D2D1_RECT_F],  # destinationRectangles
                           _Pointer[_struct.D2D1_RECT_U],  # sourceRectangles
                           _Pointer[_struct.D2D1_COLOR_F],  # colors
                           _Pointer[_struct.D2D1_MATRIX_3X2_F],  # transforms
                           _type.UINT32,  # destinationRectanglesStride
                           _type.UINT32,  # sourceRectanglesStride
                           _type.UINT32,  # colorsStride
                           _type.UINT32],  # transformsStride
                          _type.HRESULT]
    GetSprites: _Callable[[_type.UINT32,  # startIndex
                           _type.UINT32,  # spriteCount
                           _Pointer[_struct.D2D1_RECT_F],  # destinationRectangles
                           _Pointer[_struct.D2D1_RECT_U],  # sourceRectangles
                           _Pointer[_struct.D2D1_COLOR_F],  # colors
                           _Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transforms
                          _type.HRESULT]
    GetSpriteCount: _Callable[[],
                              _type.UINT32]
    Clear: _Callable[[],
                     _type.c_void]


class ID2D1DeviceContext3(ID2D1DeviceContext2):
    CreateSpriteBatch: _Callable[[_Pointer[ID2D1SpriteBatch]],  # spriteBatch
                                 _type.HRESULT]
    DrawSpriteBatch: _Callable[[ID2D1SpriteBatch,  # spriteBatch
                                _type.UINT32,  # startIndex
                                _type.UINT32,  # spriteCount
                                _d2d1.ID2D1Bitmap,  # bitmap
                                _enum.D2D1_BITMAP_INTERPOLATION_MODE,  # interpolationMode
                                _enum.D2D1_SPRITE_OPTIONS],  # spriteOptions
                               _type.c_void]


class ID2D1Device3(ID2D1Device2):
    CreateDeviceContext___: _Callable[[_enum.D2D1_DEVICE_CONTEXT_OPTIONS,  # options
                                       _Pointer[ID2D1DeviceContext3]],  # deviceContext3
                                      _type.HRESULT]


class ID2D1Factory4(ID2D1Factory3):
    CreateDevice___: _Callable[[_dxgi.IDXGIDevice,  # dxgiDevice
                                _Pointer[ID2D1Device3]],  # d2dDevice3
                               _type.HRESULT]


class ID2D1CommandSink3(ID2D1CommandSink2):
    DrawSpriteBatch: _Callable[[ID2D1SpriteBatch,  # spriteBatch
                                _type.UINT32,  # startIndex
                                _type.UINT32,  # spriteCount
                                _d2d1.ID2D1Bitmap,  # bitmap
                                _enum.D2D1_BITMAP_INTERPOLATION_MODE,  # interpolationMode
                                _enum.D2D1_SPRITE_OPTIONS],  # spriteOptions
                               _type.HRESULT]


class ID2D1SvgGlyphStyle(_d2d1.ID2D1Resource):
    SetFill: _Callable[[_d2d1.ID2D1Brush],  # brush
                       _type.HRESULT]
    GetFill: _Callable[[_Pointer[_d2d1.ID2D1Brush]],  # brush
                       _type.c_void]
    SetStroke: _Callable[[_d2d1.ID2D1Brush,  # brush
                          _type.FLOAT,  # strokeWidth
                          _Pointer[_type.FLOAT],  # dashes
                          _type.UINT32,  # dashesCount
                          _type.FLOAT],  # dashOffset
                         _type.HRESULT]
    GetStrokeDashesCount: _Callable[[],
                                    _type.UINT32]
    GetStroke: _Callable[[_Pointer[_d2d1.ID2D1Brush],  # brush
                          _Pointer[_type.FLOAT],  # strokeWidth
                          _Pointer[_type.FLOAT],  # dashes
                          _type.UINT32,  # dashesCount
                          _Pointer[_type.FLOAT]],  # dashOffset
                         _type.c_void]


class ID2D1DeviceContext4(ID2D1DeviceContext3):
    CreateSvgGlyphStyle: _Callable[[_Pointer[ID2D1SvgGlyphStyle]],  # svgGlyphStyle
                                   _type.HRESULT]
    DrawText_: _Callable[[_type.LPWSTR,  # string
                          _type.UINT32,  # stringLength
                          _dwrite.IDWriteTextFormat,  # textFormat
                          _Pointer[_struct.D2D1_RECT_F],  # layoutRect
                          _d2d1.ID2D1Brush,  # defaultFillBrush
                          ID2D1SvgGlyphStyle,  # svgGlyphStyle
                          _type.UINT32,  # colorPaletteIndex
                          _enum.D2D1_DRAW_TEXT_OPTIONS,  # options
                          _enum.DWRITE_MEASURING_MODE],  # measuringMode
                         _type.c_void]
    DrawTextLayout_: _Callable[[_struct.D2D1_POINT_2F,  # origin
                                _dwrite.IDWriteTextLayout,  # textLayout
                                _d2d1.ID2D1Brush,  # defaultFillBrush
                                ID2D1SvgGlyphStyle,  # svgGlyphStyle
                                _type.UINT32,  # colorPaletteIndex
                                _enum.D2D1_DRAW_TEXT_OPTIONS],  # options
                               _type.c_void]
    DrawColorBitmapGlyphRun: _Callable[[_enum.DWRITE_GLYPH_IMAGE_FORMATS,  # glyphImageFormat
                                        _struct.D2D1_POINT_2F,  # baselineOrigin
                                        _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                        _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                        _enum.D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION],  # bitmapSnapOption
                                       _type.c_void]
    DrawSvgGlyphRun: _Callable[[_struct.D2D1_POINT_2F,  # baselineOrigin
                                _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                _d2d1.ID2D1Brush,  # defaultFillBrush
                                ID2D1SvgGlyphStyle,  # svgGlyphStyle
                                _type.UINT32,  # colorPaletteIndex
                                _enum.DWRITE_MEASURING_MODE],  # measuringMode
                               _type.c_void]
    GetColorBitmapGlyphImage: _Callable[[_enum.DWRITE_GLYPH_IMAGE_FORMATS,  # glyphImageFormat
                                         _struct.D2D1_POINT_2F,  # glyphOrigin
                                         _dwrite.IDWriteFontFace,  # fontFace
                                         _type.FLOAT,  # fontEmSize
                                         _type.UINT16,  # glyphIndex
                                         _type.BOOL,  # isSideways
                                         _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                         _type.FLOAT,  # dpiX
                                         _type.FLOAT,  # dpiY
                                         _Pointer[_struct.D2D1_MATRIX_3X2_F],  # glyphTransform
                                         _Pointer[_d2d1.ID2D1Image]],  # glyphImage
                                        _type.HRESULT]
    GetSvgGlyphImage: _Callable[[_struct.D2D1_POINT_2F,  # glyphOrigin
                                 _dwrite.IDWriteFontFace,  # fontFace
                                 _type.FLOAT,  # fontEmSize
                                 _type.UINT16,  # glyphIndex
                                 _type.BOOL,  # isSideways
                                 _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                 _d2d1.ID2D1Brush,  # defaultFillBrush
                                 ID2D1SvgGlyphStyle,  # svgGlyphStyle
                                 _type.UINT32,  # colorPaletteIndex
                                 _Pointer[_struct.D2D1_MATRIX_3X2_F],  # glyphTransform
                                 _Pointer[_d2d1_1.ID2D1CommandList]],  # glyphImage
                                _type.HRESULT]


class ID2D1Device4(ID2D1Device3):
    CreateDeviceContext____: _Callable[[_enum.D2D1_DEVICE_CONTEXT_OPTIONS,  # options
                                        _Pointer[ID2D1DeviceContext4]],  # deviceContext4
                                       _type.HRESULT]
    SetMaximumColorGlyphCacheMemory: _Callable[[_type.UINT64],  # maximumInBytes
                                               _type.c_void]
    GetMaximumColorGlyphCacheMemory: _Callable[[],
                                               _type.UINT64]


class ID2D1Factory5(ID2D1Factory4):
    CreateDevice____: _Callable[[_dxgi.IDXGIDevice,  # dxgiDevice
                                 _Pointer[ID2D1Device4]],  # d2dDevice4
                                _type.HRESULT]


class ID2D1CommandSink4(ID2D1CommandSink3):
    SetPrimitiveBlend2: _Callable[[_enum.D2D1_PRIMITIVE_BLEND],  # primitiveBlend
                                  _type.HRESULT]


class ID2D1ColorContext1(_d2d1_1.ID2D1ColorContext):
    GetColorContextType: _Callable[[],
                                   _enum.D2D1_COLOR_CONTEXT_TYPE]
    GetDXGIColorSpace: _Callable[[],
                                 _enum.DXGI_COLOR_SPACE_TYPE]
    GetSimpleColorProfile: _Callable[[_Pointer[_struct.D2D1_SIMPLE_COLOR_PROFILE]],  # simpleProfile
                                     _type.HRESULT]


class ID2D1DeviceContext5(ID2D1DeviceContext4):
    CreateSvgDocument: _Callable[[_objidlbase.IStream,  # inputXmlStream
                                  _struct.D2D1_SIZE_F,  # viewportSize
                                  _Pointer[_d2d1svg.ID2D1SvgDocument]],  # svgDocument
                                 _type.HRESULT]
    DrawSvgDocument: _Callable[[_d2d1svg.ID2D1SvgDocument],  # svgDocument
                               _type.c_void]
    CreateColorContextFromDxgiColorSpace: _Callable[[_enum.DXGI_COLOR_SPACE_TYPE,  # colorSpace
                                                     _Pointer[ID2D1ColorContext1]],  # colorContext
                                                    _type.HRESULT]
    CreateColorContextFromSimpleColorProfile: _Callable[[_Pointer[_struct.D2D1_SIMPLE_COLOR_PROFILE],  # simpleProfile
                                                         _Pointer[ID2D1ColorContext1]],  # colorContext
                                                        _type.HRESULT]


class ID2D1Device5(ID2D1Device4):
    CreateDeviceContext_____: _Callable[[_enum.D2D1_DEVICE_CONTEXT_OPTIONS,  # options
                                         _Pointer[ID2D1DeviceContext5]],  # deviceContext5
                                        _type.HRESULT]


class ID2D1Factory6(ID2D1Factory5):
    CreateDevice_____: _Callable[[_dxgi.IDXGIDevice,  # dxgiDevice
                                  _Pointer[ID2D1Device5]],  # d2dDevice5
                                 _type.HRESULT]


class ID2D1CommandSink5(ID2D1CommandSink4):
    BlendImage: _Callable[[_d2d1.ID2D1Image,  # image
                           _enum.D2D1_BLEND_MODE,  # blendMode
                           _Pointer[_struct.D2D1_POINT_2F],  # targetOffset
                           _Pointer[_struct.D2D1_RECT_F],  # imageRectangle
                           _enum.D2D1_INTERPOLATION_MODE],  # interpolationMode
                          _type.HRESULT]


class ID2D1DeviceContext6(ID2D1DeviceContext5):
    BlendImage: _Callable[[_d2d1.ID2D1Image,  # image
                           _enum.D2D1_BLEND_MODE,  # blendMode
                           _Pointer[_struct.D2D1_POINT_2F],  # targetOffset
                           _Pointer[_struct.D2D1_RECT_F],  # imageRectangle
                           _enum.D2D1_INTERPOLATION_MODE],  # interpolationMode
                          _type.c_void]


class ID2D1Device6(ID2D1Device5):
    CreateDeviceContext______: _Callable[[_enum.D2D1_DEVICE_CONTEXT_OPTIONS,  # options
                                          _Pointer[ID2D1DeviceContext6]],  # deviceContext6
                                         _type.HRESULT]


class ID2D1Factory7(ID2D1Factory6):
    CreateDevice______: _Callable[[_dxgi.IDXGIDevice,  # dxgiDevice
                                   _Pointer[ID2D1Device6]],  # d2dDevice6
                                  _type.HRESULT]
