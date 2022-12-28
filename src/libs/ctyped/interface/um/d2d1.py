from __future__ import annotations as _

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import dwrite as _dwrite
from . import wincodec as _wincodec
from ..shared import dxgi as _dxgi
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID2D1Resource(_Unknwnbase.IUnknown):
    GetFactory: _Callable[[_Pointer[ID2D1Factory]],  # factory
                          _type.c_void]


class ID2D1Image(ID2D1Resource):
    pass


class ID2D1Bitmap(ID2D1Image):
    GetSize: _Callable[[],
                       _struct.D2D1_SIZE_F]
    GetPixelSize: _Callable[[],
                            _struct.D2D1_SIZE_U]
    GetPixelFormat: _Callable[[],
                              _struct.D2D1_PIXEL_FORMAT]
    GetDpi: _Callable[[_Pointer[_type.FLOAT],  # dpiX
                       _Pointer[_type.FLOAT]],  # dpiY
                      _type.c_void]
    CopyFromBitmap: _Callable[[_Pointer[_struct.D2D1_POINT_2U],  # destPoint
                               ID2D1Bitmap,  # bitmap
                               _Pointer[_struct.D2D1_RECT_U]],  # srcRect
                              _type.HRESULT]
    CopyFromRenderTarget: _Callable[[_Pointer[_struct.D2D1_POINT_2U],  # destPoint
                                     ID2D1RenderTarget,  # renderTarget
                                     _Pointer[_struct.D2D1_RECT_U]],  # srcRect
                                    _type.HRESULT]
    CopyFromMemory: _Callable[[_Pointer[_struct.D2D1_RECT_U],  # dstRect
                               _type.c_void_p,  # srcData
                               _type.UINT32],  # pitch
                              _type.HRESULT]


class ID2D1GradientStopCollection(ID2D1Resource):
    GetGradientStopCount: _Callable[[],
                                    _type.UINT32]
    GetGradientStops: _Callable[[_Pointer[_struct.D2D1_GRADIENT_STOP],  # gradientStops
                                 _type.UINT32],  # gradientStopsCount
                                _type.c_void]
    GetColorInterpolationGamma: _Callable[[],
                                          _enum.D2D1_GAMMA]
    GetExtendMode: _Callable[[],
                             _enum.D2D1_EXTEND_MODE]


class ID2D1Brush(ID2D1Resource):
    SetOpacity: _Callable[[_type.FLOAT],  # opacity
                          _type.c_void]
    SetTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                            _type.c_void]
    GetOpacity: _Callable[[],
                          _type.FLOAT]
    GetTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                            _type.c_void]


class ID2D1BitmapBrush(ID2D1Brush):
    SetExtendModeX: _Callable[[_enum.D2D1_EXTEND_MODE],  # extendModeX
                              _type.c_void]
    SetExtendModeY: _Callable[[_enum.D2D1_EXTEND_MODE],  # extendModeY
                              _type.c_void]
    SetInterpolationMode: _Callable[[_enum.D2D1_BITMAP_INTERPOLATION_MODE],  # interpolationMode
                                    _type.c_void]
    SetBitmap: _Callable[[ID2D1Bitmap],  # bitmap
                         _type.c_void]
    GetExtendModeX: _Callable[[],
                              _enum.D2D1_EXTEND_MODE]
    GetExtendModeY: _Callable[[],
                              _enum.D2D1_EXTEND_MODE]
    GetInterpolationMode: _Callable[[],
                                    _enum.D2D1_BITMAP_INTERPOLATION_MODE]
    GetBitmap: _Callable[[_Pointer[ID2D1Bitmap]],  # bitmap
                         _type.c_void]


class ID2D1SolidColorBrush(ID2D1Brush):
    SetColor: _Callable[[_Pointer[_struct.D2D1_COLOR_F]],  # color
                        _type.c_void]
    GetColor: _Callable[[],
                        _struct.D2D1_COLOR_F]


class ID2D1LinearGradientBrush(ID2D1Brush):
    SetStartPoint: _Callable[[_struct.D2D1_POINT_2F],  # startPoint
                             _type.c_void]
    SetEndPoint: _Callable[[_struct.D2D1_POINT_2F],  # endPoint
                           _type.c_void]
    GetStartPoint: _Callable[[],
                             _struct.D2D1_POINT_2F]
    GetEndPoint: _Callable[[],
                           _struct.D2D1_POINT_2F]
    GetGradientStopCollection: _Callable[[_Pointer[ID2D1GradientStopCollection]],  # gradientStopCollection
                                         _type.c_void]


class ID2D1RadialGradientBrush(ID2D1Brush):
    SetCenter: _Callable[[_struct.D2D1_POINT_2F],  # center
                         _type.c_void]
    SetGradientOriginOffset: _Callable[[_struct.D2D1_POINT_2F],  # gradientOriginOffset
                                       _type.c_void]
    SetRadiusX: _Callable[[_type.FLOAT],  # radiusX
                          _type.c_void]
    SetRadiusY: _Callable[[_type.FLOAT],  # radiusY
                          _type.c_void]
    GetCenter: _Callable[[],
                         _struct.D2D1_POINT_2F]
    GetGradientOriginOffset: _Callable[[],
                                       _struct.D2D1_POINT_2F]
    GetRadiusX: _Callable[[],
                          _type.FLOAT]
    GetRadiusY: _Callable[[],
                          _type.FLOAT]
    GetGradientStopCollection: _Callable[[_Pointer[ID2D1GradientStopCollection]],  # gradientStopCollection
                                         _type.c_void]


class ID2D1StrokeStyle(ID2D1Resource):
    GetStartCap: _Callable[[],
                           _enum.D2D1_CAP_STYLE]
    GetEndCap: _Callable[[],
                         _enum.D2D1_CAP_STYLE]
    GetDashCap: _Callable[[],
                          _enum.D2D1_CAP_STYLE]
    GetMiterLimit: _Callable[[],
                             _type.FLOAT]
    GetLineJoin: _Callable[[],
                           _enum.D2D1_LINE_JOIN]
    GetDashOffset: _Callable[[],
                             _type.FLOAT]
    GetDashStyle: _Callable[[],
                            _enum.D2D1_DASH_STYLE]
    GetDashesCount: _Callable[[],
                              _type.UINT32]
    GetDashes: _Callable[[_Pointer[_type.FLOAT],  # dashes
                          _type.UINT32],  # dashesCount
                         _type.c_void]


class ID2D1Geometry(ID2D1Resource):
    GetBounds: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                          _Pointer[_struct.D2D1_RECT_F]],  # bounds
                         _type.HRESULT]
    GetWidenedBounds: _Callable[[_type.FLOAT,  # strokeWidth
                                 ID2D1StrokeStyle,  # strokeStyle
                                 _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                 _type.FLOAT,  # flatteningTolerance
                                 _Pointer[_struct.D2D1_RECT_F]],  # bounds
                                _type.HRESULT]
    StrokeContainsPoint: _Callable[[_struct.D2D1_POINT_2F,  # point
                                    _type.FLOAT,  # strokeWidth
                                    ID2D1StrokeStyle,  # strokeStyle
                                    _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                    _type.FLOAT,  # flatteningTolerance
                                    _Pointer[_type.BOOL]],  # contains
                                   _type.HRESULT]
    FillContainsPoint: _Callable[[_struct.D2D1_POINT_2F,  # point
                                  _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                  _type.FLOAT,  # flatteningTolerance
                                  _Pointer[_type.BOOL]],  # contains
                                 _type.HRESULT]
    CompareWithGeometry: _Callable[[ID2D1Geometry,  # inputGeometry
                                    _Pointer[_struct.D2D1_MATRIX_3X2_F],  # inputGeometryTransform
                                    _type.FLOAT,  # flatteningTolerance
                                    _Pointer[_enum.D2D1_GEOMETRY_RELATION]],  # relation
                                   _type.HRESULT]
    Simplify: _Callable[[_enum.D2D1_GEOMETRY_SIMPLIFICATION_OPTION,  # simplificationOption
                         _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                         _type.FLOAT,  # flatteningTolerance
                         ID2D1SimplifiedGeometrySink],  # geometrySink
                        _type.HRESULT]
    Tessellate: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                           _type.FLOAT,  # flatteningTolerance
                           ID2D1TessellationSink],  # tessellationSink
                          _type.HRESULT]
    CombineWithGeometry: _Callable[[ID2D1Geometry,  # inputGeometry
                                    _enum.D2D1_COMBINE_MODE,  # combineMode
                                    _Pointer[_struct.D2D1_MATRIX_3X2_F],  # inputGeometryTransform
                                    _type.FLOAT,  # flatteningTolerance
                                    ID2D1SimplifiedGeometrySink],  # geometrySink
                                   _type.HRESULT]
    Outline: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                        _type.FLOAT,  # flatteningTolerance
                        ID2D1SimplifiedGeometrySink],  # geometrySink
                       _type.HRESULT]
    ComputeArea: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                            _type.FLOAT,  # flatteningTolerance
                            _Pointer[_type.FLOAT]],  # area
                           _type.HRESULT]
    ComputeLength: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                              _type.FLOAT,  # flatteningTolerance
                              _Pointer[_type.FLOAT]],  # length
                             _type.HRESULT]
    ComputePointAtLength: _Callable[[_type.FLOAT,  # length
                                     _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                                     _type.FLOAT,  # flatteningTolerance
                                     _Pointer[_struct.D2D1_POINT_2F],  # point
                                     _Pointer[_struct.D2D1_POINT_2F]],  # unitTangentVector
                                    _type.HRESULT]
    Widen: _Callable[[_type.FLOAT,  # strokeWidth
                      ID2D1StrokeStyle,  # strokeStyle
                      _Pointer[_struct.D2D1_MATRIX_3X2_F],  # worldTransform
                      _type.FLOAT,  # flatteningTolerance
                      ID2D1SimplifiedGeometrySink],  # geometrySink
                     _type.HRESULT]


class ID2D1RectangleGeometry(ID2D1Geometry):
    GetRect: _Callable[[_Pointer[_struct.D2D1_RECT_F]],  # rect
                       _type.c_void]


class ID2D1RoundedRectangleGeometry(ID2D1Geometry):
    GetRoundedRect: _Callable[[_Pointer[_struct.D2D1_ROUNDED_RECT]],  # roundedRect
                              _type.c_void]


class ID2D1EllipseGeometry(ID2D1Geometry):
    GetEllipse: _Callable[[_Pointer[_struct.D2D1_ELLIPSE]],  # ellipse
                          _type.c_void]


class ID2D1GeometryGroup(ID2D1Geometry):
    GetFillMode: _Callable[[],
                           _enum.D2D1_FILL_MODE]
    GetSourceGeometryCount: _Callable[[],
                                      _type.UINT32]
    GetSourceGeometries: _Callable[[_Pointer[ID2D1Geometry],  # geometries
                                    _type.UINT32],  # geometriesCount
                                   _type.c_void]


class ID2D1TransformedGeometry(ID2D1Geometry):
    GetSourceGeometry: _Callable[[_Pointer[ID2D1Geometry]],  # sourceGeometry
                                 _type.c_void]
    GetTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                            _type.c_void]


class ID2D1SimplifiedGeometrySink(_Unknwnbase.IUnknown):
    SetFillMode: _Callable[[_enum.D2D1_FILL_MODE],  # fillMode
                           _type.c_void]
    SetSegmentFlags: _Callable[[_enum.D2D1_PATH_SEGMENT],  # vertexFlags
                               _type.c_void]
    BeginFigure: _Callable[[_struct.D2D1_POINT_2F,  # startPoint
                            _enum.D2D1_FIGURE_BEGIN],  # figureBegin
                           _type.c_void]
    AddLines: _Callable[[_Pointer[_struct.D2D1_POINT_2F],  # points
                         _type.UINT32],  # pointsCount
                        _type.c_void]
    AddBeziers: _Callable[[_Pointer[_struct.D2D1_BEZIER_SEGMENT],  # beziers
                           _type.UINT32],  # beziersCount
                          _type.c_void]
    EndFigure: _Callable[[_enum.D2D1_FIGURE_END],  # figureEnd
                         _type.c_void]
    Close: _Callable[[],
                     _type.HRESULT]


class ID2D1GeometrySink(ID2D1SimplifiedGeometrySink):
    AddLine: _Callable[[_struct.D2D1_POINT_2F],  # point
                       _type.c_void]
    AddBezier: _Callable[[_Pointer[_struct.D2D1_BEZIER_SEGMENT]],  # bezier
                         _type.c_void]
    AddQuadraticBezier: _Callable[[_Pointer[_struct.D2D1_QUADRATIC_BEZIER_SEGMENT]],  # bezier
                                  _type.c_void]
    AddQuadraticBeziers: _Callable[[_Pointer[_struct.D2D1_QUADRATIC_BEZIER_SEGMENT],  # beziers
                                    _type.UINT32],  # beziersCount
                                   _type.c_void]
    AddArc: _Callable[[_Pointer[_struct.D2D1_ARC_SEGMENT]],  # arc
                      _type.c_void]


class ID2D1TessellationSink(_Unknwnbase.IUnknown):
    AddTriangles: _Callable[[_Pointer[_struct.D2D1_TRIANGLE],  # triangles
                             _type.UINT32],  # trianglesCount
                            _type.c_void]
    Close: _Callable[[],
                     _type.HRESULT]


class ID2D1PathGeometry(ID2D1Geometry):
    Open: _Callable[[_Pointer[ID2D1GeometrySink]],  # geometrySink
                    _type.HRESULT]
    Stream: _Callable[[ID2D1GeometrySink],  # geometrySink
                      _type.HRESULT]
    GetSegmentCount: _Callable[[_Pointer[_type.UINT32]],  # count
                               _type.HRESULT]
    GetFigureCount: _Callable[[_Pointer[_type.UINT32]],  # count
                              _type.HRESULT]


class ID2D1Mesh(ID2D1Resource):
    Open: _Callable[[_Pointer[ID2D1TessellationSink]],  # tessellationSink
                    _type.HRESULT]


class ID2D1Layer(ID2D1Resource):
    GetSize: _Callable[[],
                       _struct.D2D1_SIZE_F]


class ID2D1DrawingStateBlock(ID2D1Resource):
    GetDescription: _Callable[[_Pointer[_struct.D2D1_DRAWING_STATE_DESCRIPTION]],  # stateDescription
                              _type.c_void]
    SetDescription: _Callable[[_Pointer[_struct.D2D1_DRAWING_STATE_DESCRIPTION]],  # stateDescription
                              _type.c_void]
    SetTextRenderingParams: _Callable[[_dwrite.IDWriteRenderingParams],  # textRenderingParams
                                      _type.c_void]
    GetTextRenderingParams: _Callable[[_Pointer[_dwrite.IDWriteRenderingParams]],  # textRenderingParams
                                      _type.c_void]


class ID2D1RenderTarget(ID2D1Resource):
    CreateBitmap: _Callable[[_struct.D2D1_SIZE_U,  # size
                             _type.c_void_p,  # srcData
                             _type.UINT32,  # pitch
                             _Pointer[_struct.D2D1_BITMAP_PROPERTIES],  # bitmapProperties
                             _Pointer[ID2D1Bitmap]],  # bitmap
                            _type.HRESULT]
    CreateBitmapFromWicBitmap: _Callable[[_Pointer[_wincodec.IWICBitmapSource],  # wicBitmapSource
                                          _Pointer[_struct.D2D1_BITMAP_PROPERTIES],  # bitmapProperties
                                          _Pointer[ID2D1Bitmap]],  # bitmap
                                         _type.HRESULT]
    CreateSharedBitmap: _Callable[[_Pointer[_struct.IID],  # riid
                                   _type.c_void_p,  # data
                                   _Pointer[_struct.D2D1_BITMAP_PROPERTIES],  # bitmapProperties
                                   _Pointer[ID2D1Bitmap]],  # bitmap
                                  _type.HRESULT]
    CreateBitmapBrush: _Callable[[ID2D1Bitmap,  # bitmap
                                  _Pointer[_struct.D2D1_BITMAP_BRUSH_PROPERTIES],  # bitmapBrushProperties
                                  _Pointer[_struct.D2D1_BRUSH_PROPERTIES],  # brushProperties
                                  _Pointer[ID2D1BitmapBrush]],  # bitmapBrush
                                 _type.HRESULT]
    CreateSolidColorBrush: _Callable[[_Pointer[_struct.D2D1_COLOR_F],  # color
                                      _Pointer[_struct.D2D1_BRUSH_PROPERTIES],  # brushProperties
                                      _Pointer[ID2D1SolidColorBrush]],  # solidColorBrush
                                     _type.HRESULT]
    CreateGradientStopCollection: _Callable[[_Pointer[_struct.D2D1_GRADIENT_STOP],  # gradientStops
                                             _type.UINT32,  # gradientStopsCount
                                             _enum.D2D1_GAMMA,  # colorInterpolationGamma
                                             _enum.D2D1_EXTEND_MODE,  # extendMode
                                             _Pointer[ID2D1GradientStopCollection]],  # gradientStopCollection
                                            _type.HRESULT]
    CreateLinearGradientBrush: _Callable[[_Pointer[_struct.D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES],  # linearGradientBrushProperties
                                          _Pointer[_struct.D2D1_BRUSH_PROPERTIES],  # brushProperties
                                          ID2D1GradientStopCollection,  # gradientStopCollection
                                          _Pointer[ID2D1LinearGradientBrush]],  # linearGradientBrush
                                         _type.HRESULT]
    CreateRadialGradientBrush: _Callable[[_Pointer[_struct.D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES],  # radialGradientBrushProperties
                                          _Pointer[_struct.D2D1_BRUSH_PROPERTIES],  # brushProperties
                                          ID2D1GradientStopCollection,  # gradientStopCollection
                                          _Pointer[ID2D1RadialGradientBrush]],  # radialGradientBrush
                                         _type.HRESULT]
    CreateCompatibleRenderTarget: _Callable[[_Pointer[_struct.D2D1_SIZE_F],  # desiredSize
                                             _Pointer[_struct.D2D1_SIZE_U],  # desiredPixelSize
                                             _Pointer[_struct.D2D1_PIXEL_FORMAT],  # desiredFormat
                                             _enum.D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS,  # options
                                             _Pointer[ID2D1BitmapRenderTarget]],  # bitmapRenderTarget
                                            _type.HRESULT]
    CreateLayer: _Callable[[_Pointer[_struct.D2D1_SIZE_F],  # size
                            _Pointer[ID2D1Layer]],  # layer
                           _type.HRESULT]
    CreateMesh: _Callable[[_Pointer[ID2D1Mesh]],  # mesh
                          _type.HRESULT]
    DrawLine: _Callable[[_struct.D2D1_POINT_2F,  # point0
                         _struct.D2D1_POINT_2F,  # point1
                         ID2D1Brush,  # brush
                         _type.FLOAT,  # strokeWidth
                         ID2D1StrokeStyle],  # strokeStyle
                        _type.c_void]
    DrawRectangle: _Callable[[_Pointer[_struct.D2D1_RECT_F],  # rect
                              ID2D1Brush,  # brush
                              _type.FLOAT,  # strokeWidth
                              ID2D1StrokeStyle],  # strokeStyle
                             _type.c_void]
    FillRectangle: _Callable[[_Pointer[_struct.D2D1_RECT_F],  # rect
                              ID2D1Brush],  # brush
                             _type.c_void]
    DrawRoundedRectangle: _Callable[[_Pointer[_struct.D2D1_ROUNDED_RECT],  # roundedRect
                                     ID2D1Brush,  # brush
                                     _type.FLOAT,  # strokeWidth
                                     ID2D1StrokeStyle],  # strokeStyle
                                    _type.c_void]
    FillRoundedRectangle: _Callable[[_Pointer[_struct.D2D1_ROUNDED_RECT],  # roundedRect
                                     ID2D1Brush],  # brush
                                    _type.c_void]
    DrawEllipse: _Callable[[_Pointer[_struct.D2D1_ELLIPSE],  # ellipse
                            ID2D1Brush,  # brush
                            _type.FLOAT,  # strokeWidth
                            ID2D1StrokeStyle],  # strokeStyle
                           _type.c_void]
    FillEllipse: _Callable[[_Pointer[_struct.D2D1_ELLIPSE],  # ellipse
                            ID2D1Brush],  # brush
                           _type.c_void]
    DrawGeometry: _Callable[[ID2D1Geometry,  # geometry
                             ID2D1Brush,  # brush
                             _type.FLOAT,  # strokeWidth
                             ID2D1StrokeStyle],  # strokeStyle
                            _type.c_void]
    FillGeometry: _Callable[[ID2D1Geometry,  # geometry
                             ID2D1Brush,  # brush
                             ID2D1Brush],  # opacityBrush
                            _type.c_void]
    FillMesh: _Callable[[ID2D1Mesh,  # mesh
                         ID2D1Brush],  # brush
                        _type.c_void]
    FillOpacityMask: _Callable[[ID2D1Bitmap,  # opacityMask
                                ID2D1Brush,  # brush
                                _enum.D2D1_OPACITY_MASK_CONTENT,  # content
                                _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                                _Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                               _type.c_void]
    DrawBitmap: _Callable[[ID2D1Bitmap,  # bitmap
                           _Pointer[_struct.D2D1_RECT_F],  # destinationRectangle
                           _type.FLOAT,  # opacity
                           _enum.D2D1_BITMAP_INTERPOLATION_MODE,  # interpolationMode
                           _Pointer[_struct.D2D1_RECT_F]],  # sourceRectangle
                          _type.c_void]
    DrawText: _Callable[[_type.LPWSTR,  # string
                         _type.UINT32,  # stringLength
                         _dwrite.IDWriteTextFormat,  # textFormat
                         _Pointer[_struct.D2D1_RECT_F],  # layoutRect
                         ID2D1Brush,  # defaultFillBrush
                         _enum.D2D1_DRAW_TEXT_OPTIONS,  # options
                         _enum.DWRITE_MEASURING_MODE],  # measuringMode
                        _type.c_void]
    DrawTextLayout: _Callable[[_struct.D2D1_POINT_2F,  # origin
                               _dwrite.IDWriteTextLayout,  # textLayout
                               ID2D1Brush,  # defaultFillBrush
                               _enum.D2D1_DRAW_TEXT_OPTIONS],  # options
                              _type.c_void]
    DrawGlyphRun: _Callable[[_struct.D2D1_POINT_2F,  # baselineOrigin
                             _Pointer[_struct.DWRITE_GLYPH_RUN],  # glyphRun
                             ID2D1Brush,  # foregroundBrush
                             _enum.DWRITE_MEASURING_MODE],  # measuringMode
                            _type.c_void]
    SetTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                            _type.c_void]
    GetTransform: _Callable[[_Pointer[_struct.D2D1_MATRIX_3X2_F]],  # transform
                            _type.c_void]
    SetAntialiasMode: _Callable[[_enum.D2D1_ANTIALIAS_MODE],  # antialiasMode
                                _type.c_void]
    GetAntialiasMode: _Callable[[],
                                _enum.D2D1_ANTIALIAS_MODE]
    SetTextAntialiasMode: _Callable[[_enum.D2D1_TEXT_ANTIALIAS_MODE],  # textAntialiasMode
                                    _type.c_void]
    GetTextAntialiasMode: _Callable[[],
                                    _enum.D2D1_TEXT_ANTIALIAS_MODE]
    SetTextRenderingParams: _Callable[[_dwrite.IDWriteRenderingParams],  # textRenderingParams
                                      _type.c_void]
    GetTextRenderingParams: _Callable[[_Pointer[_dwrite.IDWriteRenderingParams]],  # textRenderingParams
                                      _type.c_void]
    SetTags: _Callable[[_type.D2D1_TAG,  # tag1
                        _type.D2D1_TAG],  # tag2
                       _type.c_void]
    GetTags: _Callable[[_Pointer[_type.D2D1_TAG],  # tag1
                        _Pointer[_type.D2D1_TAG]],  # tag2
                       _type.c_void]
    PushLayer: _Callable[[_Pointer[_struct.D2D1_LAYER_PARAMETERS],  # layerParameters
                          ID2D1Layer],  # layer
                         _type.c_void]
    PopLayer: _Callable[[],
                        _type.c_void]
    Flush: _Callable[[_Pointer[_type.D2D1_TAG],  # tag1
                      _Pointer[_type.D2D1_TAG]],  # tag2
                     _type.HRESULT]
    SaveDrawingState: _Callable[[ID2D1DrawingStateBlock],  # drawingStateBlock
                                _type.c_void]
    RestoreDrawingState: _Callable[[ID2D1DrawingStateBlock],  # drawingStateBlock
                                   _type.c_void]
    PushAxisAlignedClip: _Callable[[_Pointer[_struct.D2D1_RECT_F],  # clipRect
                                    _enum.D2D1_ANTIALIAS_MODE],  # antialiasMode
                                   _type.c_void]
    PopAxisAlignedClip: _Callable[[],
                                  _type.c_void]
    Clear: _Callable[[_Pointer[_struct.D2D1_COLOR_F]],  # clearColor
                     _type.c_void]
    BeginDraw: _Callable[[],
                         _type.c_void]
    EndDraw: _Callable[[_Pointer[_type.D2D1_TAG],  # tag1
                        _Pointer[_type.D2D1_TAG]],  # tag2
                       _type.HRESULT]
    GetPixelFormat: _Callable[[],
                              _struct.D2D1_PIXEL_FORMAT]
    SetDpi: _Callable[[_type.FLOAT,  # dpiX
                       _type.FLOAT],  # dpiY
                      _type.c_void]
    GetDpi: _Callable[[_Pointer[_type.FLOAT],  # dpiX
                       _Pointer[_type.FLOAT]],  # dpiY
                      _type.c_void]
    GetSize: _Callable[[],
                       _struct.D2D1_SIZE_F]
    GetPixelSize: _Callable[[],
                            _struct.D2D1_SIZE_U]
    GetMaximumBitmapSize: _Callable[[],
                                    _type.UINT32]
    IsSupported: _Callable[[_Pointer[_struct.D2D1_RENDER_TARGET_PROPERTIES]],  # renderTargetProperties
                           _type.BOOL]


class ID2D1BitmapRenderTarget(ID2D1RenderTarget):
    GetBitmap: _Callable[[_Pointer[ID2D1Bitmap]],  # bitmap
                         _type.HRESULT]


class ID2D1HwndRenderTarget(ID2D1RenderTarget):
    CheckWindowState: _Callable[[],
                                _enum.D2D1_WINDOW_STATE]
    Resize: _Callable[[_Pointer[_struct.D2D1_SIZE_U]],  # pixelSize
                      _type.HRESULT]
    GetHwnd: _Callable[[],
                       _type.HWND]


class ID2D1GdiInteropRenderTarget(_Unknwnbase.IUnknown):
    GetDC: _Callable[[_enum.D2D1_DC_INITIALIZE_MODE,  # mode
                      _Pointer[_type.HDC]],  # hdc
                     _type.HRESULT]
    ReleaseDC: _Callable[[_Pointer[_struct.RECT]],  # update
                         _type.HRESULT]


class ID2D1DCRenderTarget(ID2D1RenderTarget):
    BindDC: _Callable[[_type.HDC,  # hDC
                       _Pointer[_struct.RECT]],  # pSubRect
                      _type.HRESULT]


class ID2D1Factory(_Unknwnbase.IUnknown):
    ReloadSystemMetrics: _Callable[[],
                                   _type.HRESULT]
    GetDesktopDpi: _Callable[[_Pointer[_type.FLOAT],  # dpiX
                              _Pointer[_type.FLOAT]],  # dpiY
                             _type.c_void]
    CreateRectangleGeometry: _Callable[[_Pointer[_struct.D2D1_RECT_F],  # rectangle
                                        _Pointer[ID2D1RectangleGeometry]],  # rectangleGeometry
                                       _type.HRESULT]
    CreateRoundedRectangleGeometry: _Callable[[_Pointer[_struct.D2D1_ROUNDED_RECT],  # roundedRectangle
                                               _Pointer[ID2D1RoundedRectangleGeometry]],  # roundedRectangleGeometry
                                              _type.HRESULT]
    CreateEllipseGeometry: _Callable[[_Pointer[_struct.D2D1_ELLIPSE],  # ellipse
                                      _Pointer[ID2D1EllipseGeometry]],  # ellipseGeometry
                                     _type.HRESULT]
    CreateGeometryGroup: _Callable[[_enum.D2D1_FILL_MODE,  # fillMode
                                    _Pointer[ID2D1Geometry],  # geometries
                                    _type.UINT32,  # geometriesCount
                                    _Pointer[ID2D1GeometryGroup]],  # geometryGroup
                                   _type.HRESULT]
    CreateTransformedGeometry: _Callable[[ID2D1Geometry,  # sourceGeometry
                                          _Pointer[_struct.D2D1_MATRIX_3X2_F],  # transform
                                          _Pointer[ID2D1TransformedGeometry]],  # transformedGeometry
                                         _type.HRESULT]
    CreatePathGeometry: _Callable[[_Pointer[ID2D1PathGeometry]],  # pathGeometry
                                  _type.HRESULT]
    CreateStrokeStyle: _Callable[[_Pointer[_struct.D2D1_STROKE_STYLE_PROPERTIES],  # strokeStyleProperties
                                  _Pointer[_type.FLOAT],  # dashes
                                  _type.UINT32,  # dashesCount
                                  _Pointer[ID2D1StrokeStyle]],  # strokeStyle
                                 _type.HRESULT]
    CreateDrawingStateBlock: _Callable[[_Pointer[_struct.D2D1_DRAWING_STATE_DESCRIPTION],  # drawingStateDescription
                                        _dwrite.IDWriteRenderingParams,  # textRenderingParams
                                        _Pointer[ID2D1DrawingStateBlock]],  # drawingStateBlock
                                       _type.HRESULT]
    CreateWicBitmapRenderTarget: _Callable[[_Pointer[_wincodec.IWICBitmap],  # target
                                            _Pointer[_struct.D2D1_RENDER_TARGET_PROPERTIES],  # renderTargetProperties
                                            _Pointer[ID2D1RenderTarget]],  # renderTarget
                                           _type.HRESULT]
    CreateHwndRenderTarget: _Callable[[_Pointer[_struct.D2D1_RENDER_TARGET_PROPERTIES],  # renderTargetProperties
                                       _Pointer[_struct.D2D1_HWND_RENDER_TARGET_PROPERTIES],  # hwndRenderTargetProperties
                                       _Pointer[ID2D1HwndRenderTarget]],  # hwndRenderTarget
                                      _type.HRESULT]
    CreateDxgiSurfaceRenderTarget: _Callable[[_dxgi.IDXGISurface,  # dxgiSurface
                                              _Pointer[_struct.D2D1_RENDER_TARGET_PROPERTIES],  # renderTargetProperties
                                              _Pointer[ID2D1RenderTarget]],  # renderTarget
                                             _type.HRESULT]
    CreateDCRenderTarget: _Callable[[_Pointer[_struct.D2D1_RENDER_TARGET_PROPERTIES],  # renderTargetProperties
                                     _Pointer[ID2D1DCRenderTarget]],  # dcRenderTarget
                                    _type.HRESULT]
