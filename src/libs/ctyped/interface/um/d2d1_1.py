from __future__ import annotations as _

from typing import Callable as _Callable

from . import DocumentTarget as _DocumentTarget
from . import Unknwnbase as _Unknwnbase
from . import d2d1 as _d2d1
from . import dwrite as _dwrite
from . import objidlbase as _objidlbase
from . import wincodec as _wincodec
from ..shared import dxgi as _dxgi
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID2D1GdiMetafileSink(_Unknwnbase.IUnknown):
    ProcessRecord: _Callable[[_type.DWORD,  # recordType
                              _type.c_void_p,  # recordData
                              _type.DWORD],  # recordDataSize
                             _type.HRESULT]


class ID2D1GdiMetafile(_d2d1.ID2D1Resource):
    Stream: _Callable[[ID2D1GdiMetafileSink],  # sink
                      _type.HRESULT]
    GetBounds: _Callable[[_Pointer[_struct.D2D1_RECT_F]],  # bounds
                         _type.HRESULT]


class ID2D1CommandSink(_Unknwnbase.IUnknown):
    BeginDraw: _Callable[[],
                         _type.HRESULT]
    EndDraw: _Callable[[],
                       _type.HRESULT]
    SetAntialiasMode: _Callable[[_enum.D2D1_ANTIALIAS_MODE],  # antialiasMode
                                _type.HRESULT]
    SetTags: _Callable[[_type.D2D1_TAG,  # tag1
                        _type.D2D1_TAG],  # tag2
                       _type.HRESULT]
    SetTextAntialiasMode: _Callable[[_enum.D2D1_TEXT_ANTIALIAS_MODE],  # textAntialiasMode
                                    _type.HRESULT]
    SetTextRenderingParams: _Callable[[_dwrite.IDWriteRenderingParams],  # textRenderingParams
                                      _type.HRESULT]
    SetTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                            _type.HRESULT]
    SetPrimitiveBlend: _Callable[[_enum.D2D1_PRIMITIVE_BLEND],  # primitiveBlend
                                 _type.HRESULT]
    SetUnitMode: _Callable[[_enum.D2D1_UNIT_MODE],  # unitMode
                           _type.HRESULT]
    Clear: _Callable[[_Pointer[_struct.D2D1_COLOR_F]],  # color
                     _type.HRESULT]
    DrawGlyphRun: _Callable[[_struct.D2D1_POINT_2F,  # baselineOrigin
                             _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                             _Pointer[_struct.DWRITE_GLYPH_RUN_DESCRIPTION],  # glyphRunDescription
                             _d2d1.ID2D1Brush,  # foregroundBrush
                             _enum.DWRITE_MEASURING_MODE],  # measuringMode
                            _type.HRESULT]
    DrawLine: _Callable[[_struct.D2D1_POINT_2F,  # point0
                         _struct.D2D1_POINT_2F,  # point1
                         _d2d1.ID2D1Brush,  # brush
                         _type.FLOAT,  # strokeWidth
                         _d2d1.ID2D1StrokeStyle],  # strokeStyle
                        _type.HRESULT]
    DrawGeometry: _Callable[[_d2d1.ID2D1Geometry,  # geometry
                             _d2d1.ID2D1Brush,  # brush
                             _type.FLOAT,  # strokeWidth
                             _d2d1.ID2D1StrokeStyle],  # strokeStyle
                            _type.HRESULT]
    DrawRectangle: _Callable[[_Pointer[_struct.D2D1_RECT_F],  # rect
                              _d2d1.ID2D1Brush,  # brush
                              _type.FLOAT,  # strokeWidth
                              _d2d1.ID2D1StrokeStyle],  # strokeStyle
                             _type.HRESULT]
    DrawBitmap: _Callable[[_d2d1.ID2D1Bitmap,  # bitmap
                           _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                           _type.FLOAT,  # opacity
                           _enum.D2D1_INTERPOLATION_MODE,  # interpolationMode
                           _Pointer[_struct.D2D1_RECT_F],  # sourceRectangle
                           _Pointer[_struct.D2D1_MATRIX_4X4_F]],  # perspectiveTransform
                          _type.HRESULT]
    DrawImage: _Callable[[_d2d1.ID2D1Image,  # image
                          _Pointer[_struct.D2D1_POINT_2F],  # targetOffset
                          _Pointer[_struct.D2D1_RECT_F],  # imageRectangle
                          _enum.D2D1_INTERPOLATION_MODE,  # interpolationMode
                          _enum.D2D1_COMPOSITE_MODE],  # compositeMode
                         _type.HRESULT]
    DrawGdiMetafile: _Callable[[ID2D1GdiMetafile,  # gdiMetafile
                                _Pointer[_struct.D2D1_POINT_2F]],  # targetOffset
                               _type.HRESULT]
    FillMesh: _Callable[[_d2d1.ID2D1Mesh,  # mesh
                         _d2d1.ID2D1Brush],  # brush
                        _type.HRESULT]
    FillOpacityMask: _Callable[[_d2d1.ID2D1Bitmap,  # opacityMask
                                _d2d1.ID2D1Brush,  # brush
                                _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                                _Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                               _type.HRESULT]
    FillGeometry: _Callable[[_d2d1.ID2D1Geometry,  # geometry
                             _d2d1.ID2D1Brush,  # brush
                             _d2d1.ID2D1Brush],  # opacityBrush
                            _type.HRESULT]
    FillRectangle: _Callable[[_Pointer[_struct.D2D1_RECT_F],  # rect
                              _d2d1.ID2D1Brush],  # brush
                             _type.HRESULT]
    PushAxisAlignedClip: _Callable[[_Pointer[_struct.D2D1_RECT_F],  # clipRect
                                    _enum.D2D1_ANTIALIAS_MODE],  # antialiasMode
                                   _type.HRESULT]
    PushLayer: _Callable[[_Pointer[_struct.D2D1_LAYER_PARAMETERS1],  # layerParameters1
                          _d2d1.ID2D1Layer],  # layer
                         _type.HRESULT]
    PopAxisAlignedClip: _Callable[[],
                                  _type.HRESULT]
    PopLayer: _Callable[[],
                        _type.HRESULT]


class ID2D1CommandList(_d2d1.ID2D1Image):
    Stream: _Callable[[ID2D1CommandSink],  # sink
                      _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class ID2D1PrintControl(_Unknwnbase.IUnknown):
    AddPage: _Callable[[ID2D1CommandList,  # commandList
                        _struct.D2D_SIZE_F,  # pageSize
                        _objidlbase.IStream,  # pagePrintTicketStream
                        _Pointer[_type.D2D1_TAG],  # tag1
                        _Pointer[_type.D2D1_TAG]],  # tag2
                       _type.HRESULT]
    Close: _Callable[[],
                     _type.HRESULT]


class ID2D1ImageBrush(_d2d1.ID2D1Brush):
    SetImage: _Callable[[_d2d1.ID2D1Image],  # image
                        _type.c_void]
    SetExtendModeX: _Callable[[_enum.D2D1_EXTEND_MODE],  # extendModeX
                              _type.c_void]
    SetExtendModeY: _Callable[[_enum.D2D1_EXTEND_MODE],  # extendModeY
                              _type.c_void]
    SetInterpolationMode: _Callable[[_enum.D2D1_INTERPOLATION_MODE],  # interpolationMode
                                    _type.c_void]
    SetSourceRectangle: _Callable[[_Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                                  _type.c_void]
    GetImage: _Callable[[_Pointer[_d2d1.ID2D1Image]],  # image
                        _type.c_void]
    GetExtendModeX: _Callable[[],
                              _enum.D2D1_EXTEND_MODE]
    GetExtendModeY: _Callable[[],
                              _enum.D2D1_EXTEND_MODE]
    GetInterpolationMode: _Callable[[],
                                    _enum.D2D1_INTERPOLATION_MODE]
    GetSourceRectangle: _Callable[[_Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                                  _type.c_void]


class ID2D1BitmapBrush1(_d2d1.ID2D1BitmapBrush):
    SetInterpolationMode1: _Callable[[_enum.D2D1_INTERPOLATION_MODE],  # interpolationMode
                                     _type.c_void]
    GetInterpolationMode1: _Callable[[],
                                     _enum.D2D1_INTERPOLATION_MODE]


class ID2D1StrokeStyle1(_d2d1.ID2D1StrokeStyle):
    GetStrokeTransformType: _Callable[[],
                                      _enum.D2D1_STROKE_TRANSFORM_TYPE]


class ID2D1PathGeometry1(_d2d1.ID2D1PathGeometry):
    ComputePointAndSegmentAtLength: _Callable[[_type.FLOAT,  # length
                                               _type.UINT32,  # startSegment
                                               _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                               _type.FLOAT,  # flatteningTolerance
                                               _Pointer[_struct.D2D1_POINT_DESCRIPTION]],  # pointDescription
                                              _type.HRESULT]


class ID2D1Properties(_Unknwnbase.IUnknown):
    GetPropertyCount: _Callable[[],
                                _type.UINT32]
    GetPropertyName: _Callable[[_type.UINT32,  # index
                                _type.PWSTR,  # name
                                _type.UINT32],  # nameCount
                               _type.HRESULT]
    GetPropertyNameLength: _Callable[[_type.UINT32],  # index
                                     _type.UINT32]
    GetType: _Callable[[_type.UINT32],  # index
                       _enum.D2D1_PROPERTY_TYPE]
    GetPropertyIndex: _Callable[[_type.PCWSTR],  # name
                                _type.UINT32]
    SetValueByName: _Callable[[_type.PCWSTR,  # name
                               _enum.D2D1_PROPERTY_TYPE,  # type
                               _Pointer[_type.BYTE],  # data
                               _type.UINT32],  # dataSize
                              _type.HRESULT]
    SetValue: _Callable[[_type.UINT32,  # index
                         _enum.D2D1_PROPERTY_TYPE,  # type
                         _Pointer[_type.BYTE],  # data
                         _type.UINT32],  # dataSize
                        _type.HRESULT]
    GetValueByName: _Callable[[_type.PCWSTR,  # name
                               _enum.D2D1_PROPERTY_TYPE,  # type
                               _Pointer[_type.BYTE],  # data
                               _type.UINT32],  # dataSize
                              _type.HRESULT]
    GetValue: _Callable[[_type.UINT32,  # index
                         _enum.D2D1_PROPERTY_TYPE,  # type
                         _Pointer[_type.BYTE],  # data
                         _type.UINT32],  # dataSize
                        _type.HRESULT]
    GetValueSize: _Callable[[_type.UINT32],  # index
                            _type.UINT32]
    GetSubProperties: _Callable[[_type.UINT32,  # index
                                 _Pointer[ID2D1Properties]],  # subProperties
                                _type.HRESULT]


class ID2D1Effect(ID2D1Properties):
    SetInput: _Callable[[_type.UINT32,  # index
                         _d2d1.ID2D1Image,  # input
                         _type.BOOL],  # invalidate
                        _type.c_void]
    SetInputCount: _Callable[[_type.UINT32],  # inputCount
                             _type.HRESULT]
    GetInput: _Callable[[_type.UINT32,  # index
                         _Pointer[_d2d1.ID2D1Image]],  # input
                        _type.c_void]
    GetInputCount: _Callable[[],
                             _type.UINT32]
    GetOutput: _Callable[[_Pointer[_d2d1.ID2D1Image]],  # outputImage
                         _type.c_void]


class ID2D1Bitmap1(_d2d1.ID2D1Bitmap):
    GetColorContext: _Callable[[_Pointer[ID2D1ColorContext]],  # colorContext
                               _type.c_void]
    GetOptions: _Callable[[],
                          _enum.D2D1_BITMAP_OPTIONS]
    GetSurface: _Callable[[_Pointer[_dxgi.IDXGISurface]],  # dxgiSurface
                          _type.HRESULT]
    Map: _Callable[[_enum.D2D1_MAP_OPTIONS,  # options
                    _Pointer[_struct.D2D1_MAPPED_RECT]],  # mappedRect
                   _type.HRESULT]
    Unmap: _Callable[[],
                     _type.HRESULT]


class ID2D1ColorContext(_d2d1.ID2D1Resource):
    GetColorSpace: _Callable[[],
                             _enum.D2D1_COLOR_SPACE]
    GetProfileSize: _Callable[[],
                              _type.UINT32]
    GetProfile: _Callable[[_Pointer[_type.BYTE],  # profile
                           _type.UINT32],  # profileSize
                          _type.HRESULT]


class ID2D1GradientStopCollection1(_d2d1.ID2D1GradientStopCollection):
    GetGradientStops1: _Callable[[_Pointer[_struct.D2D1_GRADIENT_STOP],  # gradientStops
                                  _type.UINT32],  # gradientStopsCount
                                 _type.c_void]
    GetPreInterpolationSpace: _Callable[[],
                                        _enum.D2D1_COLOR_SPACE]
    GetPostInterpolationSpace: _Callable[[],
                                         _enum.D2D1_COLOR_SPACE]
    GetBufferPrecision: _Callable[[],
                                  _enum.D2D1_BUFFER_PRECISION]
    GetColorInterpolationMode: _Callable[[],
                                         _enum.D2D1_COLOR_INTERPOLATION_MODE]


class ID2D1DrawingStateBlock1(_d2d1.ID2D1DrawingStateBlock):
    GetDescription_: _Callable[[_Pointer[_struct.D2D1_DRAWING_STATE_DESCRIPTION1]],  # stateDescription
                               _type.c_void]
    SetDescription_: _Callable[[_Pointer[_struct.D2D1_DRAWING_STATE_DESCRIPTION1]],  # stateDescription
                               _type.c_void]


class ID2D1DeviceContext(_d2d1.ID2D1RenderTarget):
    CreateBitmap_: _Callable[[_struct.D2D1_SIZE_U,  # size
                              _type.c_void_p,  # sourceData
                              _type.UINT32,  # pitch
                              _Pointer[_struct.D2D1_BITMAP_PROPERTIES1],  # bitmapProperties
                              _Pointer[ID2D1Bitmap1]],  # bitmap
                             _type.HRESULT]
    CreateBitmapFromWicBitmap_: _Callable[[_Pointer[_wincodec.IWICBitmapSource],  # wicBitmapSource
                                           _Pointer[_struct.D2D1_BITMAP_PROPERTIES1],  # bitmapProperties
                                           _Pointer[ID2D1Bitmap1]],  # bitmap
                                          _type.HRESULT]
    CreateColorContext: _Callable[[_enum.D2D1_COLOR_SPACE,  # space
                                   _Pointer[_type.BYTE],  # profile
                                   _type.UINT32,  # profileSize
                                   _Pointer[ID2D1ColorContext]],  # colorContext
                                  _type.HRESULT]
    CreateColorContextFromFilename: _Callable[[_type.PCWSTR,  # filename
                                               _Pointer[ID2D1ColorContext]],  # colorContext
                                              _type.HRESULT]
    CreateColorContextFromWicColorContext: _Callable[[_wincodec.IWICColorContext,  # wicColorContext
                                                      _Pointer[ID2D1ColorContext]],  # colorContext
                                                     _type.HRESULT]
    CreateBitmapFromDxgiSurface: _Callable[[_dxgi.IDXGISurface,  # surface
                                            _Pointer[_struct.D2D1_BITMAP_PROPERTIES1],  # bitmapProperties
                                            _Pointer[ID2D1Bitmap1]],  # bitmap
                                           _type.HRESULT]
    CreateEffect: _Callable[[_Pointer[_struct.IID],  # effectId
                             _Pointer[ID2D1Effect]],  # effect
                            _type.HRESULT]
    CreateGradientStopCollection_: _Callable[[_Pointer[_struct.D2D1_GRADIENT_STOP],  # straightAlphaGradientStops
                                              _type.UINT32,  # straightAlphaGradientStopsCount
                                              _enum.D2D1_COLOR_SPACE,  # preInterpolationSpace
                                              _enum.D2D1_COLOR_SPACE,  # postInterpolationSpace
                                              _enum.D2D1_BUFFER_PRECISION,  # bufferPrecision
                                              _enum.D2D1_EXTEND_MODE,  # extendMode
                                              _enum.D2D1_COLOR_INTERPOLATION_MODE,  # colorInterpolationMode
                                              _Pointer[ID2D1GradientStopCollection1]],  # gradientStopCollection1
                                             _type.HRESULT]
    CreateImageBrush: _Callable[[_d2d1.ID2D1Image,  # image
                                 _Pointer[_struct.D2D1_IMAGE_BRUSH_PROPERTIES],  # imageBrushProperties
                                 _Pointer[_struct.D2D1_BRUSH_PROPERTIES],  # brushProperties
                                 _Pointer[ID2D1ImageBrush]],  # imageBrush
                                _type.HRESULT]
    CreateBitmapBrush_: _Callable[[_d2d1.ID2D1Bitmap,  # bitmap
                                   _Pointer[_struct.D2D1_BITMAP_BRUSH_PROPERTIES1],  # bitmapBrushProperties
                                   _Pointer[_struct.D2D1_BRUSH_PROPERTIES],  # brushProperties
                                   _Pointer[ID2D1BitmapBrush1]],  # bitmapBrush
                                  _type.HRESULT]
    CreateCommandList: _Callable[[_Pointer[ID2D1CommandList]],  # commandList
                                 _type.HRESULT]
    IsDxgiFormatSupported: _Callable[[_enum.DXGI_FORMAT],  # format
                                     _type.BOOL]
    IsBufferPrecisionSupported: _Callable[[_enum.D2D1_BUFFER_PRECISION],  # bufferPrecision
                                          _type.BOOL]
    GetImageLocalBounds: _Callable[[_d2d1.ID2D1Image,  # image
                                    _Pointer[_struct.D2D1_RECT_F]],  # localBounds
                                   _type.HRESULT]
    GetImageWorldBounds: _Callable[[_d2d1.ID2D1Image,  # image
                                    _Pointer[_struct.D2D1_RECT_F]],  # worldBounds
                                   _type.HRESULT]
    GetGlyphRunWorldBounds: _Callable[[_struct.D2D1_POINT_2F,  # baselineOrigin
                                       _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                                       _enum.DWRITE_MEASURING_MODE,  # measuringMode
                                       _Pointer[_struct.D2D1_RECT_F]],  # bounds
                                      _type.HRESULT]
    GetDevice: _Callable[[_Pointer[ID2D1Device]],  # device
                         _type.c_void]
    SetTarget: _Callable[[_d2d1.ID2D1Image],  # image
                         _type.c_void]
    GetTarget: _Callable[[_Pointer[_d2d1.ID2D1Image]],  # image
                         _type.c_void]
    SetRenderingControls: _Callable[[_Pointer[_struct.D2D1_RENDERING_CONTROLS]],  # renderingControls
                                    _type.c_void]
    GetRenderingControls: _Callable[[_Pointer[_struct.D2D1_RENDERING_CONTROLS]],  # renderingControls
                                    _type.c_void]
    SetPrimitiveBlend: _Callable[[_enum.D2D1_PRIMITIVE_BLEND],  # primitiveBlend
                                 _type.c_void]
    GetPrimitiveBlend: _Callable[[],
                                 _enum.D2D1_PRIMITIVE_BLEND]
    SetUnitMode: _Callable[[_enum.D2D1_UNIT_MODE],  # unitMode
                           _type.c_void]
    GetUnitMode: _Callable[[],
                           _enum.D2D1_UNIT_MODE]
    DrawGlyphRun_: _Callable[[_struct.D2D1_POINT_2F,  # baselineOrigin
                              _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                              _Pointer[_struct.DWRITE_GLYPH_RUN_DESCRIPTION],  # glyphRunDescription
                              _d2d1.ID2D1Brush,  # foregroundBrush
                              _enum.DWRITE_MEASURING_MODE],  # measuringMode
                             _type.c_void]
    DrawImage: _Callable[[_d2d1.ID2D1Image,  # image
                          _Pointer[_struct.D2D1_POINT_2F],  # targetOffset
                          _Pointer[_struct.D2D1_RECT_F],  # imageRectangle
                          _enum.D2D1_INTERPOLATION_MODE,  # interpolationMode
                          _enum.D2D1_COMPOSITE_MODE],  # compositeMode
                         _type.c_void]
    DrawGdiMetafile: _Callable[[ID2D1GdiMetafile,  # gdiMetafile
                                _Pointer[_struct.D2D1_POINT_2F]],  # targetOffset
                               _type.c_void]
    DrawBitmap_: _Callable[[_d2d1.ID2D1Bitmap,  # bitmap
                            _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                            _type.FLOAT,  # opacity
                            _enum.D2D1_INTERPOLATION_MODE,  # interpolationMode
                            _Pointer[_struct.D2D1_RECT_F],  # sourceRectangle
                            _Pointer[_struct.D2D1_MATRIX_4X4_F]],  # perspectiveTransform
                           _type.c_void]
    PushLayer_: _Callable[[_Pointer[_struct.D2D1_LAYER_PARAMETERS1],  # layerParameters
                           _d2d1.ID2D1Layer],  # layer
                          _type.c_void]
    InvalidateEffectInputRectangle: _Callable[[ID2D1Effect,  # effect
                                               _type.UINT32,  # input
                                               _Pointer[_struct.D2D1_RECT_F]],  # inputRectangle
                                              _type.HRESULT]
    GetEffectInvalidRectangleCount: _Callable[[ID2D1Effect,  # effect
                                               _Pointer[_type.UINT32]],  # rectangleCount
                                              _type.HRESULT]
    GetEffectInvalidRectangles: _Callable[[ID2D1Effect,  # effect
                                           _Pointer[_struct.D2D1_RECT_F],  # rectangles
                                           _type.UINT32],  # rectanglesCount
                                          _type.HRESULT]
    GetEffectRequiredInputRectangles: _Callable[[ID2D1Effect,  # renderEffect
                                                 _Pointer[_struct.D2D1_RECT_F],  # renderImageRectangle
                                                 _Pointer[_struct.D2D1_EFFECT_INPUT_DESCRIPTION],  # inputDescriptions
                                                 _Pointer[_struct.D2D1_RECT_F],  # requiredInputRects
                                                 _type.UINT32],  # inputCount
                                                _type.HRESULT]
    FillOpacityMask_: _Callable[[_d2d1.ID2D1Bitmap,  # opacityMask
                                 _d2d1.ID2D1Brush,  # brush
                                 _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                                 _Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                                _type.c_void]


class ID2D1Device(_d2d1.ID2D1Resource):
    CreateDeviceContext: _Callable[[_enum.D2D1_DEVICE_CONTEXT_OPTIONS,  # options
                                    _Pointer[ID2D1DeviceContext]],  # deviceContext
                                   _type.HRESULT]
    CreatePrintControl: _Callable[[_wincodec.IWICImagingFactory,  # wicFactory
                                   _DocumentTarget.IPrintDocumentPackageTarget,  # documentTarget
                                   _Pointer[_struct.D2D1_PRINT_CONTROL_PROPERTIES],  # printControlProperties
                                   _Pointer[ID2D1PrintControl]],  # printControl
                                  _type.HRESULT]
    SetMaximumTextureMemory: _Callable[[_type.UINT64],  # maximumInBytes
                                       _type.c_void]
    GetMaximumTextureMemory: _Callable[[],
                                       _type.UINT64]
    ClearResources: _Callable[[_type.UINT32],  # millisecondsSinceUse
                              _type.c_void]


class ID2D1Factory1(_d2d1.ID2D1Factory):
    CreateDevice: _Callable[[_dxgi.IDXGIDevice,  # dxgiDevice
                             _Pointer[ID2D1Device]],  # d2dDevice
                            _type.HRESULT]
    CreateStrokeStyle_: _Callable[[_Pointer[_struct.D2D1_STROKE_STYLE_PROPERTIES1],  # strokeStyleProperties
                                   _Pointer[_type.FLOAT],  # dashes
                                   _type.UINT32,  # dashesCount
                                   _Pointer[ID2D1StrokeStyle1]],  # strokeStyle
                                  _type.HRESULT]
    CreatePathGeometry_: _Callable[[_Pointer[ID2D1PathGeometry1]],  # pathGeometry
                                   _type.HRESULT]
    CreateDrawingStateBlock_: _Callable[[_Pointer[_struct.D2D1_DRAWING_STATE_DESCRIPTION1],  # drawingStateDescription
                                         _dwrite.IDWriteRenderingParams,  # textRenderingParams
                                         _Pointer[ID2D1DrawingStateBlock1]],  # drawingStateBlock
                                        _type.HRESULT]
    CreateGdiMetafile: _Callable[[_objidlbase.IStream,  # metafileStream
                                  _Pointer[ID2D1GdiMetafile]],  # metafile
                                 _type.HRESULT]
    RegisterEffectFromStream: _Callable[[_Pointer[_struct.IID],  # classId
                                         _objidlbase.IStream,  # propertyXml
                                         _Pointer[_struct.D2D1_PROPERTY_BINDING],  # bindings
                                         _type.UINT32,  # bindingsCount
                                         _type.PD2D1_EFFECT_FACTORY],  # effectFactory
                                        _type.HRESULT]
    RegisterEffectFromString: _Callable[[_Pointer[_struct.IID],  # classId
                                         _type.PCWSTR,  # propertyXml
                                         _Pointer[_struct.D2D1_PROPERTY_BINDING],  # bindings
                                         _type.UINT32,  # bindingsCount
                                         _type.PD2D1_EFFECT_FACTORY],  # effectFactory
                                        _type.HRESULT]
    UnregisterEffect: _Callable[[_Pointer[_struct.IID]],  # classId
                                _type.HRESULT]
    GetRegisteredEffects: _Callable[[_Pointer[_struct.CLSID],  # effects
                                     _type.UINT32,  # effectsCount
                                     _Pointer[_type.UINT32],  # effectsReturned
                                     _Pointer[_type.UINT32]],  # effectsRegistered
                                    _type.HRESULT]
    GetEffectProperties: _Callable[[_Pointer[_struct.IID],  # effectId
                                    _Pointer[ID2D1Properties]],  # properties
                                   _type.HRESULT]


class ID2D1Multithread(_Unknwnbase.IUnknown):
    GetMultithreadProtected: _Callable[[],
                                       _type.BOOL]
    Enter: _Callable[[],
                     _type.c_void]
    Leave: _Callable[[],
                     _type.c_void]
