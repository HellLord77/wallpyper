from __future__ import annotations as _

from typing import Callable as _Callable, Optional as _Optional

from . import _WinLib
from .. import enum as _enum
from .. import struct as _struct
from .. import type as _type
from .._utils import _Pointer
from ..interface.um import ddraw as _ddraw
from ..interface.um import objidlbase as _objidlbase

# gdipluseffects
GdipCreateEffect: _Callable[[_struct.GUID,  # guid
                             _Pointer[_type.CGpEffect]],  # effect
                            _enum.Status]
GdipDeleteEffect: _Callable[[_type.CGpEffect],  # effect
                            _enum.Status]
GdipGetEffectParameterSize: _Callable[[_type.CGpEffect,  # effect
                                       _Pointer[_type.UINT]],  # size
                                      _enum.Status]
GdipSetEffectParameters: _Callable[[_type.CGpEffect,  # effect
                                    _type.PVOID,  # params
                                    _type.UINT],  # size
                                   _enum.Status]
GdipGetEffectParameters: _Callable[[_type.CGpEffect,  # effect
                                    _type.UINT,  # size
                                    _type.PVOID],  # params
                                   _enum.Status]
# gdiplusflat
GdipCreatePath: _Callable[[_enum.GpFillMode,  # brushMode
                           _Pointer[_type.GpPath]],  # path
                          _enum.GpStatus]
GdipCreatePath2: _Callable[[_Pointer[_struct.GpPointF],  # points
                            _Pointer[_type.BYTE],  # types
                            _type.INT,  # count
                            _enum.GpFillMode,  # fillMode
                            _Pointer[_type.GpPath]],  # path
                           _enum.GpStatus]
GdipCreatePath2I: _Callable[[_Pointer[_struct.GpPoint],  # points
                             _Pointer[_type.BYTE],  # types
                             _type.INT,  # count
                             _enum.GpFillMode,  # fillMode
                             _Pointer[_type.GpPath]],  # path
                            _enum.GpStatus]
GdipClonePath: _Callable[[_type.GpPath,  # path
                          _Pointer[_type.GpPath]],  # clonePath
                         _enum.GpStatus]
GdipDeletePath: _Callable[[_type.GpPath],  # path
                          _enum.GpStatus]
GdipResetPath: _Callable[[_type.GpPath],  # path
                         _enum.GpStatus]
GdipGetPointCount: _Callable[[_type.GpPath,  # path
                              _Pointer[_type.INT]],  # count
                             _enum.GpStatus]
GdipGetPathTypes: _Callable[[_type.GpPath,  # path
                             _Pointer[_type.BYTE],  # types
                             _type.INT],  # count
                            _enum.GpStatus]
GdipGetPathPoints: _Callable[[_type.GpPath,  # GpPath*
                              _Pointer[_struct.GpPointF],  # points
                              _type.INT],  # count
                             _enum.GpStatus]
GdipGetPathPointsI: _Callable[[_type.GpPath,  # GpPath*
                               _Pointer[_struct.GpPoint],  # points
                               _type.INT],  # count
                              _enum.GpStatus]
GdipGetPathFillMode: _Callable[[_type.GpPath,  # path
                                _Pointer[_enum.GpFillMode]],  # fillmode
                               _enum.GpStatus]
GdipSetPathFillMode: _Callable[[_type.GpPath,  # path
                                _enum.GpFillMode],  # fillmode
                               _enum.GpStatus]
GdipGetPathData: _Callable[[_type.GpPath,  # path
                            _Pointer[_struct.GpPathData]],  # pathData
                           _enum.GpStatus]
GdipStartPathFigure: _Callable[[_type.GpPath],  # path
                               _enum.GpStatus]
GdipClosePathFigure: _Callable[[_type.GpPath],  # path
                               _enum.GpStatus]
GdipClosePathFigures: _Callable[[_type.GpPath],  # path
                                _enum.GpStatus]
GdipSetPathMarker: _Callable[[_type.GpPath],  # path
                             _enum.GpStatus]
GdipClearPathMarkers: _Callable[[_type.GpPath],  # path
                                _enum.GpStatus]
GdipReversePath: _Callable[[_type.GpPath],  # path
                           _enum.GpStatus]
GdipGetPathLastPoint: _Callable[[_type.GpPath,  # path
                                 _Pointer[_struct.GpPointF]],  # lastPoint
                                _enum.GpStatus]
GdipAddPathLine: _Callable[[_type.GpPath,  # path
                            _type.REAL,  # x1
                            _type.REAL,  # y1
                            _type.REAL,  # x2
                            _type.REAL],  # y2
                           _enum.GpStatus]
GdipAddPathLine2: _Callable[[_type.GpPath,  # path
                             _Pointer[_struct.GpPointF],  # points
                             _type.INT],  # count
                            _enum.GpStatus]
GdipAddPathArc: _Callable[[_type.GpPath,  # path
                           _type.REAL,  # x
                           _type.REAL,  # y
                           _type.REAL,  # width
                           _type.REAL,  # height
                           _type.REAL,  # startAngle
                           _type.REAL],  # sweepAngle
                          _enum.GpStatus]
GdipAddPathBezier: _Callable[[_type.GpPath,  # path
                              _type.REAL,  # x1
                              _type.REAL,  # y1
                              _type.REAL,  # x2
                              _type.REAL,  # y2
                              _type.REAL,  # x3
                              _type.REAL,  # y3
                              _type.REAL,  # x4
                              _type.REAL],  # y4
                             _enum.GpStatus]
GdipAddPathBeziers: _Callable[[_type.GpPath,  # path
                               _Pointer[_struct.GpPointF],  # points
                               _type.INT],  # count
                              _enum.GpStatus]
GdipAddPathCurve: _Callable[[_type.GpPath,  # path
                             _Pointer[_struct.GpPointF],  # points
                             _type.INT],  # count
                            _enum.GpStatus]
GdipAddPathCurve2: _Callable[[_type.GpPath,  # path
                              _Pointer[_struct.GpPointF],  # points
                              _type.INT,  # count
                              _type.REAL],  # tension
                             _enum.GpStatus]
GdipAddPathCurve3: _Callable[[_type.GpPath,  # path
                              _Pointer[_struct.GpPointF],  # points
                              _type.INT,  # count
                              _type.INT,  # offset
                              _type.INT,  # numberOfSegments
                              _type.REAL],  # tension
                             _enum.GpStatus]
GdipAddPathClosedCurve: _Callable[[_type.GpPath,  # path
                                   _Pointer[_struct.GpPointF],  # points
                                   _type.INT],  # count
                                  _enum.GpStatus]
GdipAddPathClosedCurve2: _Callable[[_type.GpPath,  # path
                                    _Pointer[_struct.GpPointF],  # points
                                    _type.INT,  # count
                                    _type.REAL],  # tension
                                   _enum.GpStatus]
GdipAddPathRectangle: _Callable[[_type.GpPath,  # path
                                 _type.REAL,  # x
                                 _type.REAL,  # y
                                 _type.REAL,  # width
                                 _type.REAL],  # height
                                _enum.GpStatus]
GdipAddPathRectangles: _Callable[[_type.GpPath,  # path
                                  _Pointer[_struct.GpRectF],  # rects
                                  _type.INT],  # count
                                 _enum.GpStatus]
GdipAddPathEllipse: _Callable[[_type.GpPath,  # path
                               _type.REAL,  # x
                               _type.REAL,  # y
                               _type.REAL,  # width
                               _type.REAL],  # height
                              _enum.GpStatus]
GdipAddPathPie: _Callable[[_type.GpPath,  # path
                           _type.REAL,  # x
                           _type.REAL,  # y
                           _type.REAL,  # width
                           _type.REAL,  # height
                           _type.REAL,  # startAngle
                           _type.REAL],  # sweepAngle
                          _enum.GpStatus]
GdipAddPathPolygon: _Callable[[_type.GpPath,  # path
                               _Pointer[_struct.GpPointF],  # points
                               _type.INT],  # count
                              _enum.GpStatus]
GdipAddPathPath: _Callable[[_type.GpPath,  # path
                            _type.GpPath,  # addingPath
                            _type.BOOL],  # connect
                           _enum.GpStatus]
GdipAddPathString: _Callable[[_type.GpPath,  # path
                              _type.LPWSTR,  # string
                              _type.INT,  # length
                              _type.GpFontFamily,  # family
                              _type.INT,  # style
                              _type.REAL,  # emSize
                              _Pointer[_struct.RectF],  # layoutRect
                              _type.GpStringFormat],  # format
                             _enum.GpStatus]
GdipAddPathStringI: _Callable[[_type.GpPath,  # path
                               _type.LPWSTR,  # string
                               _type.INT,  # length
                               _type.GpFontFamily,  # family
                               _type.INT,  # style
                               _type.REAL,  # emSize
                               _Pointer[_struct.Rect],  # layoutRect
                               _type.GpStringFormat],  # format
                              _enum.GpStatus]
GdipAddPathLineI: _Callable[[_type.GpPath,  # path
                             _type.INT,  # x1
                             _type.INT,  # y1
                             _type.INT,  # x2
                             _type.INT],  # y2
                            _enum.GpStatus]
GdipAddPathLine2I: _Callable[[_type.GpPath,  # path
                              _Pointer[_struct.GpPoint],  # points
                              _type.INT],  # count
                             _enum.GpStatus]
GdipAddPathArcI: _Callable[[_type.GpPath,  # path
                            _type.INT,  # x
                            _type.INT,  # y
                            _type.INT,  # width
                            _type.INT,  # height
                            _type.REAL,  # startAngle
                            _type.REAL],  # sweepAngle
                           _enum.GpStatus]
GdipAddPathBezierI: _Callable[[_type.GpPath,  # path
                               _type.INT,  # x1
                               _type.INT,  # y1
                               _type.INT,  # x2
                               _type.INT,  # y2
                               _type.INT,  # x3
                               _type.INT,  # y3
                               _type.INT,  # x4
                               _type.INT],  # y4
                              _enum.GpStatus]
GdipAddPathBeziersI: _Callable[[_type.GpPath,  # path
                                _Pointer[_struct.GpPoint],  # points
                                _type.INT],  # count
                               _enum.GpStatus]
GdipAddPathCurveI: _Callable[[_type.GpPath,  # path
                              _Pointer[_struct.GpPoint],  # points
                              _type.INT],  # count
                             _enum.GpStatus]
GdipAddPathCurve2I: _Callable[[_type.GpPath,  # path
                               _Pointer[_struct.GpPoint],  # points
                               _type.INT,  # count
                               _type.REAL],  # tension
                              _enum.GpStatus]
GdipAddPathCurve3I: _Callable[[_type.GpPath,  # path
                               _Pointer[_struct.GpPoint],  # points
                               _type.INT,  # count
                               _type.INT,  # offset
                               _type.INT,  # numberOfSegments
                               _type.REAL],  # tension
                              _enum.GpStatus]
GdipAddPathClosedCurveI: _Callable[[_type.GpPath,  # path
                                    _Pointer[_struct.GpPoint],  # points
                                    _type.INT],  # count
                                   _enum.GpStatus]
GdipAddPathClosedCurve2I: _Callable[[_type.GpPath,  # path
                                     _Pointer[_struct.GpPoint],  # points
                                     _type.INT,  # count
                                     _type.REAL],  # tension
                                    _enum.GpStatus]
GdipAddPathRectangleI: _Callable[[_type.GpPath,  # path
                                  _type.INT,  # x
                                  _type.INT,  # y
                                  _type.INT,  # width
                                  _type.INT],  # height
                                 _enum.GpStatus]
GdipAddPathRectanglesI: _Callable[[_type.GpPath,  # path
                                   _Pointer[_struct.GpRect],  # rects
                                   _type.INT],  # count
                                  _enum.GpStatus]
GdipAddPathEllipseI: _Callable[[_type.GpPath,  # path
                                _type.INT,  # x
                                _type.INT,  # y
                                _type.INT,  # width
                                _type.INT],  # height
                               _enum.GpStatus]
GdipAddPathPieI: _Callable[[_type.GpPath,  # path
                            _type.INT,  # x
                            _type.INT,  # y
                            _type.INT,  # width
                            _type.INT,  # height
                            _type.REAL,  # startAngle
                            _type.REAL],  # sweepAngle
                           _enum.GpStatus]
GdipAddPathPolygonI: _Callable[[_type.GpPath,  # path
                                _Pointer[_struct.GpPoint],  # points
                                _type.INT],  # count
                               _enum.GpStatus]
GdipFlattenPath: _Callable[[_type.GpPath,  # path
                            _type.GpMatrix,  # matrix
                            _type.REAL],  # flatness
                           _enum.GpStatus]
GdipWindingModeOutline: _Callable[[_type.GpPath,  # path
                                   _type.GpMatrix,  # matrix
                                   _type.REAL],  # flatness
                                  _enum.GpStatus]
GdipWidenPath: _Callable[[_type.GpPath,  # nativePath
                          _type.GpPen,  # pen
                          _type.GpMatrix,  # matrix
                          _type.REAL],  # flatness
                         _enum.GpStatus]
GdipWarpPath: _Callable[[_type.GpPath,  # path
                         _type.GpMatrix,  # matrix
                         _Pointer[_struct.GpPointF],  # points
                         _type.INT,  # count
                         _type.REAL,  # srcx
                         _type.REAL,  # srcy
                         _type.REAL,  # srcwidth
                         _type.REAL,  # srcheight
                         _enum.WarpMode,  # warpMode
                         _type.REAL],  # flatness
                        _enum.GpStatus]
GdipTransformPath: _Callable[[_type.GpPath,  # path
                              _type.GpMatrix],  # matrix
                             _enum.GpStatus]
GdipGetPathWorldBounds: _Callable[[_type.GpPath,  # path
                                   _Pointer[_struct.GpRectF],  # bounds
                                   _type.GpMatrix,  # matrix
                                   _type.GpPen],  # pen
                                  _enum.GpStatus]
GdipGetPathWorldBoundsI: _Callable[[_type.GpPath,  # path
                                    _Pointer[_struct.GpRect],  # bounds
                                    _type.GpMatrix,  # matrix
                                    _type.GpPen],  # pen
                                   _enum.GpStatus]
GdipIsVisiblePathPoint: _Callable[[_type.GpPath,  # path
                                   _type.REAL,  # x
                                   _type.REAL,  # y
                                   _type.GpGraphics,  # graphics
                                   _Pointer[_type.BOOL]],  # result
                                  _enum.GpStatus]
GdipIsVisiblePathPointI: _Callable[[_type.GpPath,  # path
                                    _type.INT,  # x
                                    _type.INT,  # y
                                    _type.GpGraphics,  # graphics
                                    _Pointer[_type.BOOL]],  # result
                                   _enum.GpStatus]
GdipIsOutlineVisiblePathPoint: _Callable[[_type.GpPath,  # path
                                          _type.REAL,  # x
                                          _type.REAL,  # y
                                          _type.GpPen,  # pen
                                          _type.GpGraphics,  # graphics
                                          _Pointer[_type.BOOL]],  # result
                                         _enum.GpStatus]
GdipIsOutlineVisiblePathPointI: _Callable[[_type.GpPath,  # path
                                           _type.INT,  # x
                                           _type.INT,  # y
                                           _type.GpPen,  # pen
                                           _type.GpGraphics,  # graphics
                                           _Pointer[_type.BOOL]],  # result
                                          _enum.GpStatus]
GdipCreatePathIter: _Callable[[_Pointer[_type.GpPathIterator],  # iterator
                               _type.GpPath],  # path
                              _enum.GpStatus]
GdipDeletePathIter: _Callable[[_type.GpPathIterator],  # iterator
                              _enum.GpStatus]
GdipPathIterNextSubpath: _Callable[[_type.GpPathIterator,  # iterator
                                    _Pointer[_type.INT],  # resultCount
                                    _Pointer[_type.INT],  # startIndex
                                    _Pointer[_type.INT],  # endIndex
                                    _Pointer[_type.BOOL]],  # isClosed
                                   _enum.GpStatus]
GdipPathIterNextSubpathPath: _Callable[[_type.GpPathIterator,  # iterator
                                        _Pointer[_type.INT],  # resultCount
                                        _type.GpPath,  # path
                                        _Pointer[_type.BOOL]],  # isClosed
                                       _enum.GpStatus]
GdipPathIterNextPathType: _Callable[[_type.GpPathIterator,  # iterator
                                     _Pointer[_type.INT],  # resultCount
                                     _Pointer[_type.BYTE],  # pathType
                                     _Pointer[_type.INT],  # startIndex
                                     _Pointer[_type.INT]],  # endIndex
                                    _enum.GpStatus]
GdipPathIterNextMarker: _Callable[[_type.GpPathIterator,  # iterator
                                   _Pointer[_type.INT],  # resultCount
                                   _Pointer[_type.INT],  # startIndex
                                   _Pointer[_type.INT]],  # endIndex
                                  _enum.GpStatus]
GdipPathIterNextMarkerPath: _Callable[[_type.GpPathIterator,  # iterator
                                       _Pointer[_type.INT],  # resultCount
                                       _type.GpPath],  # path
                                      _enum.GpStatus]
GdipPathIterGetCount: _Callable[[_type.GpPathIterator,  # iterator
                                 _Pointer[_type.INT]],  # count
                                _enum.GpStatus]
GdipPathIterGetSubpathCount: _Callable[[_type.GpPathIterator,  # iterator
                                        _Pointer[_type.INT]],  # count
                                       _enum.GpStatus]
GdipPathIterIsValid: _Callable[[_type.GpPathIterator,  # iterator
                                _Pointer[_type.BOOL]],  # valid
                               _enum.GpStatus]
GdipPathIterHasCurve: _Callable[[_type.GpPathIterator,  # iterator
                                 _Pointer[_type.BOOL]],  # hasCurve
                                _enum.GpStatus]
GdipPathIterRewind: _Callable[[_type.GpPathIterator],  # iterator
                              _enum.GpStatus]
GdipPathIterEnumerate: _Callable[[_type.GpPathIterator,  # iterator
                                  _Pointer[_type.INT],  # resultCount
                                  _Pointer[_struct.GpPointF],  # points
                                  _Pointer[_type.BYTE],  # types
                                  _type.INT],  # count
                                 _enum.GpStatus]
GdipPathIterCopyData: _Callable[[_type.GpPathIterator,  # iterator
                                 _Pointer[_type.INT],  # resultCount
                                 _Pointer[_struct.GpPointF],  # points
                                 _Pointer[_type.BYTE],  # types
                                 _type.INT,  # startIndex
                                 _type.INT],  # endIndex
                                _enum.GpStatus]
GdipCreateMatrix: _Callable[[_Pointer[_type.GpMatrix]],  # matrix
                            _enum.GpStatus]
GdipCreateMatrix2: _Callable[[_type.REAL,  # m11
                              _type.REAL,  # m12
                              _type.REAL,  # m21
                              _type.REAL,  # m22
                              _type.REAL,  # dx
                              _type.REAL,  # dy
                              _Pointer[_type.GpMatrix]],  # matrix
                             _enum.GpStatus]
GdipCreateMatrix3: _Callable[[_Pointer[_struct.GpRectF],  # rect
                              _Pointer[_struct.GpPointF],  # dstplg
                              _Pointer[_type.GpMatrix]],  # matrix
                             _enum.GpStatus]
GdipCreateMatrix3I: _Callable[[_Pointer[_struct.GpRect],  # rect
                               _Pointer[_struct.GpPoint],  # dstplg
                               _Pointer[_type.GpMatrix]],  # matrix
                              _enum.GpStatus]
GdipCloneMatrix: _Callable[[_type.GpMatrix,  # matrix
                            _Pointer[_type.GpMatrix]],  # cloneMatrix
                           _enum.GpStatus]
GdipDeleteMatrix: _Callable[[_type.GpMatrix],  # matrix
                            _enum.GpStatus]
GdipSetMatrixElements: _Callable[[_type.GpMatrix,  # matrix
                                  _type.REAL,  # m11
                                  _type.REAL,  # m12
                                  _type.REAL,  # m21
                                  _type.REAL,  # m22
                                  _type.REAL,  # dx
                                  _type.REAL],  # dy
                                 _enum.GpStatus]
GdipMultiplyMatrix: _Callable[[_type.GpMatrix,  # matrix
                               _type.GpMatrix,  # matrix2
                               _enum.GpMatrixOrder],  # order
                              _enum.GpStatus]
GdipTranslateMatrix: _Callable[[_type.GpMatrix,  # matrix
                                _type.REAL,  # offsetX
                                _type.REAL,  # offsetY
                                _enum.GpMatrixOrder],  # order
                               _enum.GpStatus]
GdipScaleMatrix: _Callable[[_type.GpMatrix,  # matrix
                            _type.REAL,  # scaleX
                            _type.REAL,  # scaleY
                            _enum.GpMatrixOrder],  # order
                           _enum.GpStatus]
GdipRotateMatrix: _Callable[[_type.GpMatrix,  # matrix
                             _type.REAL,  # angle
                             _enum.GpMatrixOrder],  # order
                            _enum.GpStatus]
GdipShearMatrix: _Callable[[_type.GpMatrix,  # matrix
                            _type.REAL,  # shearX
                            _type.REAL,  # shearY
                            _enum.GpMatrixOrder],  # order
                           _enum.GpStatus]
GdipInvertMatrix: _Callable[[_type.GpMatrix],  # matrix
                            _enum.GpStatus]
GdipTransformMatrixPoints: _Callable[[_type.GpMatrix,  # matrix
                                      _Pointer[_struct.GpPointF],  # pts
                                      _type.INT],  # count
                                     _enum.GpStatus]
GdipTransformMatrixPointsI: _Callable[[_type.GpMatrix,  # matrix
                                       _Pointer[_struct.GpPoint],  # pts
                                       _type.INT],  # count
                                      _enum.GpStatus]
GdipVectorTransformMatrixPoints: _Callable[[_type.GpMatrix,  # matrix
                                            _Pointer[_struct.GpPointF],  # pts
                                            _type.INT],  # count
                                           _enum.GpStatus]
GdipVectorTransformMatrixPointsI: _Callable[[_type.GpMatrix,  # matrix
                                             _Pointer[_struct.GpPoint],  # pts
                                             _type.INT],  # count
                                            _enum.GpStatus]
GdipGetMatrixElements: _Callable[[_type.GpMatrix,  # matrix
                                  _Pointer[_type.REAL]],  # matrixOut
                                 _enum.GpStatus]
GdipIsMatrixInvertible: _Callable[[_type.GpMatrix,  # matrix
                                   _Pointer[_type.BOOL]],  # result
                                  _enum.GpStatus]
GdipIsMatrixIdentity: _Callable[[_type.GpMatrix,  # matrix
                                 _Pointer[_type.BOOL]],  # result
                                _enum.GpStatus]
GdipIsMatrixEqual: _Callable[[_type.GpMatrix,  # matrix
                              _type.GpMatrix,  # matrix2
                              _Pointer[_type.BOOL]],  # result
                             _enum.GpStatus]
GdipCreateRegion: _Callable[[_Pointer[_type.GpRegion]],  # region
                            _enum.GpStatus]
GdipCreateRegionRect: _Callable[[_Pointer[_struct.GpRectF],  # rect
                                 _Pointer[_type.GpRegion]],  # region
                                _enum.GpStatus]
GdipCreateRegionRectI: _Callable[[_Pointer[_struct.GpRect],  # rect
                                  _Pointer[_type.GpRegion]],  # region
                                 _enum.GpStatus]
GdipCreateRegionPath: _Callable[[_type.GpPath,  # path
                                 _Pointer[_type.GpRegion]],  # region
                                _enum.GpStatus]
GdipCreateRegionRgnData: _Callable[[_Pointer[_type.BYTE],  # regionData
                                    _type.INT,  # size
                                    _Pointer[_type.GpRegion]],  # region
                                   _enum.GpStatus]
GdipCreateRegionHrgn: _Callable[[_type.HRGN,  # hRgn
                                 _Pointer[_type.GpRegion]],  # region
                                _enum.GpStatus]
GdipCloneRegion: _Callable[[_type.GpRegion,  # region
                            _Pointer[_type.GpRegion]],  # cloneRegion
                           _enum.GpStatus]
GdipDeleteRegion: _Callable[[_type.GpRegion],  # region
                            _enum.GpStatus]
GdipSetInfinite: _Callable[[_type.GpRegion],  # region
                           _enum.GpStatus]
GdipSetEmpty: _Callable[[_type.GpRegion],  # region
                        _enum.GpStatus]
GdipCombineRegionRect: _Callable[[_type.GpRegion,  # region
                                  _Pointer[_struct.GpRectF],  # rect
                                  _enum.CombineMode],  # combineMode
                                 _enum.GpStatus]
GdipCombineRegionRectI: _Callable[[_type.GpRegion,  # region
                                   _Pointer[_struct.GpRect],  # rect
                                   _enum.CombineMode],  # combineMode
                                  _enum.GpStatus]
GdipCombineRegionPath: _Callable[[_type.GpRegion,  # region
                                  _type.GpPath,  # path
                                  _enum.CombineMode],  # combineMode
                                 _enum.GpStatus]
GdipCombineRegionRegion: _Callable[[_type.GpRegion,  # region
                                    _type.GpRegion,  # region2
                                    _enum.CombineMode],  # combineMode
                                   _enum.GpStatus]
GdipTranslateRegion: _Callable[[_type.GpRegion,  # region
                                _type.REAL,  # dx
                                _type.REAL],  # dy
                               _enum.GpStatus]
GdipTranslateRegionI: _Callable[[_type.GpRegion,  # region
                                 _type.INT,  # dx
                                 _type.INT],  # dy
                                _enum.GpStatus]
GdipTransformRegion: _Callable[[_type.GpRegion,  # region
                                _type.GpMatrix],  # matrix
                               _enum.GpStatus]
GdipGetRegionBounds: _Callable[[_type.GpRegion,  # region
                                _type.GpGraphics,  # graphics
                                _Pointer[_struct.GpRectF]],  # rect
                               _enum.GpStatus]
GdipGetRegionBoundsI: _Callable[[_type.GpRegion,  # region
                                 _type.GpGraphics,  # graphics
                                 _Pointer[_struct.GpRect]],  # rect
                                _enum.GpStatus]
GdipGetRegionHRgn: _Callable[[_type.GpRegion,  # region
                              _type.GpGraphics,  # graphics
                              _Pointer[_type.HRGN]],  # hRgn
                             _enum.GpStatus]
GdipIsEmptyRegion: _Callable[[_type.GpRegion,  # region
                              _type.GpGraphics,  # graphics
                              _Pointer[_type.BOOL]],  # result
                             _enum.GpStatus]
GdipIsInfiniteRegion: _Callable[[_type.GpRegion,  # region
                                 _type.GpGraphics,  # graphics
                                 _Pointer[_type.BOOL]],  # result
                                _enum.GpStatus]
GdipIsEqualRegion: _Callable[[_type.GpRegion,  # region
                              _type.GpRegion,  # region2
                              _type.GpGraphics,  # graphics
                              _Pointer[_type.BOOL]],  # result
                             _enum.GpStatus]
GdipGetRegionDataSize: _Callable[[_type.GpRegion,  # region
                                  _Pointer[_type.UINT]],  # bufferSize
                                 _enum.GpStatus]
GdipGetRegionData: _Callable[[_type.GpRegion,  # region
                              _Pointer[_type.BYTE],  # buffer
                              _type.UINT,  # bufferSize
                              _Optional[_Pointer[_type.UINT]]],  # sizeFilled
                             _enum.GpStatus]
GdipIsVisibleRegionPoint: _Callable[[_type.GpRegion,  # region
                                     _type.REAL,  # x
                                     _type.REAL,  # y
                                     _type.GpGraphics,  # graphics
                                     _Pointer[_type.BOOL]],  # result
                                    _enum.GpStatus]
GdipIsVisibleRegionPointI: _Callable[[_type.GpRegion,  # region
                                      _type.INT,  # x
                                      _type.INT,  # y
                                      _type.GpGraphics,  # graphics
                                      _Pointer[_type.BOOL]],  # result
                                     _enum.GpStatus]
GdipIsVisibleRegionRect: _Callable[[_type.GpRegion,  # region
                                    _type.REAL,  # x
                                    _type.REAL,  # y
                                    _type.REAL,  # width
                                    _type.REAL,  # height
                                    _type.GpGraphics,  # graphics
                                    _Pointer[_type.BOOL]],  # result
                                   _enum.GpStatus]
GdipIsVisibleRegionRectI: _Callable[[_type.GpRegion,  # region
                                     _type.INT,  # x
                                     _type.INT,  # y
                                     _type.INT,  # width
                                     _type.INT,  # height
                                     _type.GpGraphics,  # graphics
                                     _Pointer[_type.BOOL]],  # result
                                    _enum.GpStatus]
GdipGetRegionScansCount: _Callable[[_type.GpRegion,  # region
                                    _Pointer[_type.UINT],  # count
                                    _type.GpMatrix],  # matrix
                                   _enum.GpStatus]
GdipGetRegionScans: _Callable[[_type.GpRegion,  # region
                               _Pointer[_struct.GpRectF],  # rects
                               _Pointer[_type.INT],  # count
                               _type.GpMatrix],  # matrix
                              _enum.GpStatus]
GdipGetRegionScansI: _Callable[[_type.GpRegion,  # region
                                _Pointer[_struct.GpRect],  # rects
                                _Pointer[_type.INT],  # count
                                _type.GpMatrix],  # matrix
                               _enum.GpStatus]
GdipCloneBrush: _Callable[[_type.GpBrush,  # brush
                           _Pointer[_type.GpBrush]],  # cloneBrush
                          _enum.GpStatus]
GdipDeleteBrush: _Callable[[_type.GpBrush],  # brush
                           _enum.GpStatus]
GdipGetBrushType: _Callable[[_type.GpBrush,  # brush
                             _Pointer[_enum.GpBrushType]],  # type
                            _enum.GpStatus]
GdipCreateHatchBrush: _Callable[[_enum.GpHatchStyle,  # hatchstyle
                                 _type.ARGB,  # forecol
                                 _type.ARGB,  # backcol
                                 _Pointer[_type.GpHatch]],  # brush
                                _enum.GpStatus]
GdipGetHatchStyle: _Callable[[_type.GpHatch,  # brush
                              _Pointer[_enum.GpHatchStyle]],  # hatchstyle
                             _enum.GpStatus]
GdipGetHatchForegroundColor: _Callable[[_type.GpHatch,  # brush
                                        _Pointer[_type.ARGB]],  # forecol
                                       _enum.GpStatus]
GdipGetHatchBackgroundColor: _Callable[[_type.GpHatch,  # brush
                                        _Pointer[_type.ARGB]],  # backcol
                                       _enum.GpStatus]
GdipCreateTexture: _Callable[[_type.GpImage,  # image
                              _enum.GpWrapMode,  # wrapmode
                              _Pointer[_type.GpTexture]],  # texture
                             _enum.GpStatus]
GdipCreateTexture2: _Callable[[_type.GpImage,  # image
                               _enum.GpWrapMode,  # wrapmode
                               _type.REAL,  # x
                               _type.REAL,  # y
                               _type.REAL,  # width
                               _type.REAL,  # height
                               _Pointer[_type.GpTexture]],  # texture
                              _enum.GpStatus]
GdipCreateTextureIA: _Callable[[_type.GpImage,  # image
                                _type.GpImageAttributes,  # imageAttributes
                                _type.REAL,  # x
                                _type.REAL,  # y
                                _type.REAL,  # width
                                _type.REAL,  # height
                                _Pointer[_type.GpTexture]],  # texture
                               _enum.GpStatus]
GdipCreateTexture2I: _Callable[[_type.GpImage,  # image
                                _enum.GpWrapMode,  # wrapmode
                                _type.INT,  # x
                                _type.INT,  # y
                                _type.INT,  # width
                                _type.INT,  # height
                                _Pointer[_type.GpTexture]],  # texture
                               _enum.GpStatus]
GdipCreateTextureIAI: _Callable[[_type.GpImage,  # image
                                 _type.GpImageAttributes,  # imageAttributes
                                 _type.INT,  # x
                                 _type.INT,  # y
                                 _type.INT,  # width
                                 _type.INT,  # height
                                 _Pointer[_type.GpTexture]],  # texture
                                _enum.GpStatus]
GdipGetTextureTransform: _Callable[[_type.GpTexture,  # brush
                                    _type.GpMatrix],  # matrix
                                   _enum.GpStatus]
GdipSetTextureTransform: _Callable[[_type.GpTexture,  # brush
                                    _type.GpMatrix],  # matrix
                                   _enum.GpStatus]
GdipResetTextureTransform: _Callable[[_type.GpTexture],  # brush
                                     _enum.GpStatus]
GdipMultiplyTextureTransform: _Callable[[_type.GpTexture,  # brush
                                         _type.GpMatrix,  # matrix
                                         _enum.GpMatrixOrder],  # order
                                        _enum.GpStatus]
GdipTranslateTextureTransform: _Callable[[_type.GpTexture,  # brush
                                          _type.REAL,  # dx
                                          _type.REAL,  # dy
                                          _enum.GpMatrixOrder],  # order
                                         _enum.GpStatus]
GdipScaleTextureTransform: _Callable[[_type.GpTexture,  # brush
                                      _type.REAL,  # sx
                                      _type.REAL,  # sy
                                      _enum.GpMatrixOrder],  # order
                                     _enum.GpStatus]
GdipRotateTextureTransform: _Callable[[_type.GpTexture,  # brush
                                       _type.REAL,  # angle
                                       _enum.GpMatrixOrder],  # order
                                      _enum.GpStatus]
GdipSetTextureWrapMode: _Callable[[_type.GpTexture,  # brush
                                   _enum.GpWrapMode],  # wrapmode
                                  _enum.GpStatus]
GdipGetTextureWrapMode: _Callable[[_type.GpTexture,  # brush
                                   _Pointer[_enum.GpWrapMode]],  # wrapmode
                                  _enum.GpStatus]
GdipGetTextureImage: _Callable[[_type.GpTexture,  # brush
                                _Pointer[_type.GpImage]],  # image
                               _enum.GpStatus]
GdipCreateSolidFill: _Callable[[_type.ARGB,  # color
                                _Pointer[_type.GpSolidFill]],  # brush
                               _enum.GpStatus]
GdipSetSolidFillColor: _Callable[[_type.GpSolidFill,  # brush
                                  _type.ARGB],  # color
                                 _enum.GpStatus]
GdipGetSolidFillColor: _Callable[[_type.GpSolidFill,  # brush
                                  _Pointer[_type.ARGB]],  # color
                                 _enum.GpStatus]
GdipCreateLineBrush: _Callable[[_Pointer[_struct.GpPointF],  # point1
                                _Pointer[_struct.GpPointF],  # point2
                                _type.ARGB,  # color1
                                _type.ARGB,  # color2
                                _enum.GpWrapMode,  # wrapMode
                                _Pointer[_type.GpLineGradient]],  # lineGradient
                               _enum.GpStatus]
GdipCreateLineBrushI: _Callable[[_Pointer[_struct.GpPoint],  # point1
                                 _Pointer[_struct.GpPoint],  # point2
                                 _type.ARGB,  # color1
                                 _type.ARGB,  # color2
                                 _enum.GpWrapMode,  # wrapMode
                                 _Pointer[_type.GpLineGradient]],  # lineGradient
                                _enum.GpStatus]
GdipCreateLineBrushFromRect: _Callable[[_Pointer[_struct.GpRectF],  # rect
                                        _type.ARGB,  # color1
                                        _type.ARGB,  # color2
                                        _enum.LinearGradientMode,  # mode
                                        _enum.GpWrapMode,  # wrapMode
                                        _Pointer[_type.GpLineGradient]],  # lineGradient
                                       _enum.GpStatus]
GdipCreateLineBrushFromRectI: _Callable[[_Pointer[_struct.GpRect],  # rect
                                         _type.ARGB,  # color1
                                         _type.ARGB,  # color2
                                         _enum.LinearGradientMode,  # mode
                                         _enum.GpWrapMode,  # wrapMode
                                         _Pointer[_type.GpLineGradient]],  # lineGradient
                                        _enum.GpStatus]
GdipCreateLineBrushFromRectWithAngle: _Callable[[_Pointer[_struct.GpRectF],  # rect
                                                 _type.ARGB,  # color1
                                                 _type.ARGB,  # color2
                                                 _type.REAL,  # angle
                                                 _type.BOOL,  # isAngleScalable
                                                 _enum.GpWrapMode,  # wrapMode
                                                 _Pointer[_type.GpLineGradient]],  # lineGradient
                                                _enum.GpStatus]
GdipCreateLineBrushFromRectWithAngleI: _Callable[[_Pointer[_struct.GpRect],  # rect
                                                  _type.ARGB,  # color1
                                                  _type.ARGB,  # color2
                                                  _type.REAL,  # angle
                                                  _type.BOOL,  # isAngleScalable
                                                  _enum.GpWrapMode,  # wrapMode
                                                  _Pointer[_type.GpLineGradient]],  # lineGradient
                                                 _enum.GpStatus]
GdipSetLineColors: _Callable[[_type.GpLineGradient,  # brush
                              _type.ARGB,  # color1
                              _type.ARGB],  # color2
                             _enum.GpStatus]
GdipGetLineColors: _Callable[[_type.GpLineGradient,  # brush
                              _Pointer[_type.ARGB]],  # colors
                             _enum.GpStatus]
GdipGetLineRect: _Callable[[_type.GpLineGradient,  # brush
                            _Pointer[_struct.GpRectF]],  # rect
                           _enum.GpStatus]
GdipGetLineRectI: _Callable[[_type.GpLineGradient,  # brush
                             _Pointer[_struct.GpRect]],  # rect
                            _enum.GpStatus]
GdipSetLineGammaCorrection: _Callable[[_type.GpLineGradient,  # brush
                                       _type.BOOL],  # useGammaCorrection
                                      _enum.GpStatus]
GdipGetLineGammaCorrection: _Callable[[_type.GpLineGradient,  # brush
                                       _Pointer[_type.BOOL]],  # useGammaCorrection
                                      _enum.GpStatus]
GdipGetLineBlendCount: _Callable[[_type.GpLineGradient,  # brush
                                  _Pointer[_type.INT]],  # count
                                 _enum.GpStatus]
GdipGetLineBlend: _Callable[[_type.GpLineGradient,  # brush
                             _Pointer[_type.REAL],  # blend
                             _Pointer[_type.REAL],  # positions
                             _type.INT],  # count
                            _enum.GpStatus]
GdipSetLineBlend: _Callable[[_type.GpLineGradient,  # brush
                             _Pointer[_type.REAL],  # blend
                             _Pointer[_type.REAL],  # positions
                             _type.INT],  # count
                            _enum.GpStatus]
GdipGetLinePresetBlendCount: _Callable[[_type.GpLineGradient,  # brush
                                        _Pointer[_type.INT]],  # count
                                       _enum.GpStatus]
GdipGetLinePresetBlend: _Callable[[_type.GpLineGradient,  # brush
                                   _Pointer[_type.ARGB],  # blend
                                   _Pointer[_type.REAL],  # positions
                                   _type.INT],  # count
                                  _enum.GpStatus]
GdipSetLinePresetBlend: _Callable[[_type.GpLineGradient,  # brush
                                   _Pointer[_type.ARGB],  # blend
                                   _Pointer[_type.REAL],  # positions
                                   _type.INT],  # count
                                  _enum.GpStatus]
GdipSetLineSigmaBlend: _Callable[[_type.GpLineGradient,  # brush
                                  _type.REAL,  # focus
                                  _type.REAL],  # scale
                                 _enum.GpStatus]
GdipSetLineLinearBlend: _Callable[[_type.GpLineGradient,  # brush
                                   _type.REAL,  # focus
                                   _type.REAL],  # scale
                                  _enum.GpStatus]
GdipSetLineWrapMode: _Callable[[_type.GpLineGradient,  # brush
                                _enum.GpWrapMode],  # wrapmode
                               _enum.GpStatus]
GdipGetLineWrapMode: _Callable[[_type.GpLineGradient,  # brush
                                _Pointer[_enum.GpWrapMode]],  # wrapmode
                               _enum.GpStatus]
GdipGetLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                 _type.GpMatrix],  # matrix
                                _enum.GpStatus]
GdipSetLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                 _type.GpMatrix],  # matrix
                                _enum.GpStatus]
GdipResetLineTransform: _Callable[[_type.GpLineGradient],  # brush
                                  _enum.GpStatus]
GdipMultiplyLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                      _type.GpMatrix,  # matrix
                                      _enum.GpMatrixOrder],  # order
                                     _enum.GpStatus]
GdipTranslateLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                       _type.REAL,  # dx
                                       _type.REAL,  # dy
                                       _enum.GpMatrixOrder],  # order
                                      _enum.GpStatus]
GdipScaleLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                   _type.REAL,  # sx
                                   _type.REAL,  # sy
                                   _enum.GpMatrixOrder],  # order
                                  _enum.GpStatus]
GdipRotateLineTransform: _Callable[[_type.GpLineGradient,  # brush
                                    _type.REAL,  # angle
                                    _enum.GpMatrixOrder],  # order
                                   _enum.GpStatus]
GdipCreatePathGradient: _Callable[[_Pointer[_struct.GpPointF],  # points
                                   _type.INT,  # count
                                   _enum.GpWrapMode,  # wrapMode
                                   _Pointer[_type.GpPathGradient]],  # polyGradient
                                  _enum.GpStatus]
GdipCreatePathGradientI: _Callable[[_Pointer[_struct.GpPoint],  # points
                                    _type.INT,  # count
                                    _enum.GpWrapMode,  # wrapMode
                                    _Pointer[_type.GpPathGradient]],  # polyGradient
                                   _enum.GpStatus]
GdipCreatePathGradientFromPath: _Callable[[_type.GpPath,  # path
                                           _Pointer[_type.GpPathGradient]],  # polyGradient
                                          _enum.GpStatus]
GdipGetPathGradientCenterColor: _Callable[[_type.GpPathGradient,  # brush
                                           _Pointer[_type.ARGB]],  # colors
                                          _enum.GpStatus]
GdipSetPathGradientCenterColor: _Callable[[_type.GpPathGradient,  # brush
                                           _type.ARGB],  # colors
                                          _enum.GpStatus]
GdipGetPathGradientSurroundColorsWithCount: _Callable[[_type.GpPathGradient,  # brush
                                                       _Pointer[_type.ARGB],  # color
                                                       _Pointer[_type.INT]],  # count
                                                      _enum.GpStatus]
GdipSetPathGradientSurroundColorsWithCount: _Callable[[_type.GpPathGradient,  # brush
                                                       _Pointer[_type.ARGB],  # color
                                                       _Pointer[_type.INT]],  # count
                                                      _enum.GpStatus]
GdipGetPathGradientPath: _Callable[[_type.GpPathGradient,  # brush
                                    _type.GpPath],  # path
                                   _enum.GpStatus]
GdipSetPathGradientPath: _Callable[[_type.GpPathGradient,  # brush
                                    _type.GpPath],  # path
                                   _enum.GpStatus]
GdipGetPathGradientCenterPoint: _Callable[[_type.GpPathGradient,  # brush
                                           _Pointer[_struct.GpPointF]],  # points
                                          _enum.GpStatus]
GdipGetPathGradientCenterPointI: _Callable[[_type.GpPathGradient,  # brush
                                            _Pointer[_struct.GpPoint]],  # points
                                           _enum.GpStatus]
GdipSetPathGradientCenterPoint: _Callable[[_type.GpPathGradient,  # brush
                                           _Pointer[_struct.GpPointF]],  # points
                                          _enum.GpStatus]
GdipSetPathGradientCenterPointI: _Callable[[_type.GpPathGradient,  # brush
                                            _Pointer[_struct.GpPoint]],  # points
                                           _enum.GpStatus]
GdipGetPathGradientRect: _Callable[[_type.GpPathGradient,  # brush
                                    _Pointer[_struct.GpRectF]],  # rect
                                   _enum.GpStatus]
GdipGetPathGradientRectI: _Callable[[_type.GpPathGradient,  # brush
                                     _Pointer[_struct.GpRect]],  # rect
                                    _enum.GpStatus]
GdipGetPathGradientPointCount: _Callable[[_type.GpPathGradient,  # brush
                                          _Pointer[_type.INT]],  # count
                                         _enum.GpStatus]
GdipGetPathGradientSurroundColorCount: _Callable[[_type.GpPathGradient,  # brush
                                                  _Pointer[_type.INT]],  # count
                                                 _enum.GpStatus]
GdipSetPathGradientGammaCorrection: _Callable[[_type.GpPathGradient,  # brush
                                               _type.BOOL],  # useGammaCorrection
                                              _enum.GpStatus]
GdipGetPathGradientGammaCorrection: _Callable[[_type.GpPathGradient,  # brush
                                               _Pointer[_type.BOOL]],  # useGammaCorrection
                                              _enum.GpStatus]
GdipGetPathGradientBlendCount: _Callable[[_type.GpPathGradient,  # brush
                                          _Pointer[_type.INT]],  # count
                                         _enum.GpStatus]
GdipGetPathGradientBlend: _Callable[[_type.GpPathGradient,  # brush
                                     _Pointer[_type.REAL],  # blend
                                     _Pointer[_type.REAL],  # positions
                                     _type.INT],  # count
                                    _enum.GpStatus]
GdipSetPathGradientBlend: _Callable[[_type.GpPathGradient,  # brush
                                     _Pointer[_type.REAL],  # blend
                                     _Pointer[_type.REAL],  # positions
                                     _type.INT],  # count
                                    _enum.GpStatus]
GdipGetPathGradientPresetBlendCount: _Callable[[_type.GpPathGradient,  # brush
                                                _Pointer[_type.INT]],  # count
                                               _enum.GpStatus]
GdipGetPathGradientPresetBlend: _Callable[[_type.GpPathGradient,  # brush
                                           _Pointer[_type.ARGB],  # blend
                                           _Pointer[_type.REAL],  # positions
                                           _type.INT],  # count
                                          _enum.GpStatus]
GdipSetPathGradientPresetBlend: _Callable[[_type.GpPathGradient,  # brush
                                           _Pointer[_type.ARGB],  # blend
                                           _Pointer[_type.REAL],  # positions
                                           _type.INT],  # count
                                          _enum.GpStatus]
GdipSetPathGradientSigmaBlend: _Callable[[_type.GpPathGradient,  # brush
                                          _type.REAL,  # focus
                                          _type.REAL],  # scale
                                         _enum.GpStatus]
GdipSetPathGradientLinearBlend: _Callable[[_type.GpPathGradient,  # brush
                                           _type.REAL,  # focus
                                           _type.REAL],  # scale
                                          _enum.GpStatus]
GdipGetPathGradientWrapMode: _Callable[[_type.GpPathGradient,  # brush
                                        _Pointer[_enum.GpWrapMode]],  # wrapmode
                                       _enum.GpStatus]
GdipSetPathGradientWrapMode: _Callable[[_type.GpPathGradient,  # brush
                                        _enum.GpWrapMode],  # wrapmode
                                       _enum.GpStatus]
GdipGetPathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                         _type.GpMatrix],  # matrix
                                        _enum.GpStatus]
GdipSetPathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                         _type.GpMatrix],  # matrix
                                        _enum.GpStatus]
GdipResetPathGradientTransform: _Callable[[_type.GpPathGradient],  # brush
                                          _enum.GpStatus]
GdipMultiplyPathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                              _type.GpMatrix,  # matrix
                                              _enum.GpMatrixOrder],  # order
                                             _enum.GpStatus]
GdipTranslatePathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                               _type.REAL,  # dx
                                               _type.REAL,  # dy
                                               _enum.GpMatrixOrder],  # order
                                              _enum.GpStatus]
GdipScalePathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                           _type.REAL,  # sx
                                           _type.REAL,  # sy
                                           _enum.GpMatrixOrder],  # order
                                          _enum.GpStatus]
GdipRotatePathGradientTransform: _Callable[[_type.GpPathGradient,  # brush
                                            _type.REAL,  # angle
                                            _enum.GpMatrixOrder],  # order
                                           _enum.GpStatus]
GdipGetPathGradientFocusScales: _Callable[[_type.GpPathGradient,  # brush
                                           _Pointer[_type.REAL],  # xScale
                                           _Pointer[_type.REAL]],  # yScale
                                          _enum.GpStatus]
GdipSetPathGradientFocusScales: _Callable[[_type.GpPathGradient,  # brush
                                           _type.REAL,  # xScale
                                           _type.REAL],  # yScale
                                          _enum.GpStatus]
GdipCreatePen1: _Callable[[_type.ARGB,  # color
                           _type.REAL,  # width
                           _enum.GpUnit,  # unit
                           _Pointer[_type.GpPen]],  # pen
                          _enum.GpStatus]
GdipCreatePen2: _Callable[[_type.GpBrush,  # brush
                           _type.REAL,  # width
                           _enum.GpUnit,  # unit
                           _Pointer[_type.GpPen]],  # pen
                          _enum.GpStatus]
GdipClonePen: _Callable[[_type.GpPen,  # pen
                         _Pointer[_type.GpPen]],  # clonepen
                        _enum.GpStatus]
GdipDeletePen: _Callable[[_type.GpPen],  # pen
                         _enum.GpStatus]
GdipSetPenWidth: _Callable[[_type.GpPen,  # pen
                            _type.REAL],  # width
                           _enum.GpStatus]
GdipGetPenWidth: _Callable[[_type.GpPen,  # pen
                            _Pointer[_type.REAL]],  # width
                           _enum.GpStatus]
GdipSetPenUnit: _Callable[[_type.GpPen,  # pen
                           _enum.GpUnit],  # unit
                          _enum.GpStatus]
GdipGetPenUnit: _Callable[[_type.GpPen,  # pen
                           _Pointer[_enum.GpUnit]],  # unit
                          _enum.GpStatus]
GdipSetPenLineCap197819: _Callable[[_type.GpPen,  # pen
                                    _enum.GpLineCap,  # startCap
                                    _enum.GpLineCap,  # endCap
                                    _enum.GpDashCap],  # dashCap
                                   _enum.GpStatus]
GdipSetPenStartCap: _Callable[[_type.GpPen,  # pen
                               _enum.GpLineCap],  # startCap
                              _enum.GpStatus]
GdipSetPenEndCap: _Callable[[_type.GpPen,  # pen
                             _enum.GpLineCap],  # endCap
                            _enum.GpStatus]
GdipSetPenDashCap197819: _Callable[[_type.GpPen,  # pen
                                    _enum.GpDashCap],  # dashCap
                                   _enum.GpStatus]
GdipGetPenStartCap: _Callable[[_type.GpPen,  # pen
                               _Pointer[_enum.GpLineCap]],  # startCap
                              _enum.GpStatus]
GdipGetPenEndCap: _Callable[[_type.GpPen,  # pen
                             _Pointer[_enum.GpLineCap]],  # endCap
                            _enum.GpStatus]
GdipGetPenDashCap197819: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_enum.GpDashCap]],  # dashCap
                                   _enum.GpStatus]
GdipSetPenLineJoin: _Callable[[_type.GpPen,  # pen
                               _enum.GpLineJoin],  # lineJoin
                              _enum.GpStatus]
GdipGetPenLineJoin: _Callable[[_type.GpPen,  # pen
                               _Pointer[_enum.GpLineJoin]],  # lineJoin
                              _enum.GpStatus]
GdipSetPenCustomStartCap: _Callable[[_type.GpPen,  # pen
                                     _type.GpCustomLineCap],  # customCap
                                    _enum.GpStatus]
GdipGetPenCustomStartCap: _Callable[[_type.GpPen,  # pen
                                     _Pointer[_type.GpCustomLineCap]],  # customCap
                                    _enum.GpStatus]
GdipSetPenCustomEndCap: _Callable[[_type.GpPen,  # pen
                                   _type.GpCustomLineCap],  # customCap
                                  _enum.GpStatus]
GdipGetPenCustomEndCap: _Callable[[_type.GpPen,  # pen
                                   _Pointer[_type.GpCustomLineCap]],  # customCap
                                  _enum.GpStatus]
GdipSetPenMiterLimit: _Callable[[_type.GpPen,  # pen
                                 _type.REAL],  # miterLimit
                                _enum.GpStatus]
GdipGetPenMiterLimit: _Callable[[_type.GpPen,  # pen
                                 _Pointer[_type.REAL]],  # miterLimit
                                _enum.GpStatus]
GdipSetPenMode: _Callable[[_type.GpPen,  # pen
                           _enum.GpPenAlignment],  # penMode
                          _enum.GpStatus]
GdipGetPenMode: _Callable[[_type.GpPen,  # pen
                           _Pointer[_enum.GpPenAlignment]],  # penMode
                          _enum.GpStatus]
GdipSetPenTransform: _Callable[[_type.GpPen,  # pen
                                _type.GpMatrix],  # matrix
                               _enum.GpStatus]
GdipGetPenTransform: _Callable[[_type.GpPen,  # pen
                                _type.GpMatrix],  # matrix
                               _enum.GpStatus]
GdipResetPenTransform: _Callable[[_type.GpPen],  # pen
                                 _enum.GpStatus]
GdipMultiplyPenTransform: _Callable[[_type.GpPen,  # pen
                                     _type.GpMatrix,  # matrix
                                     _enum.GpMatrixOrder],  # order
                                    _enum.GpStatus]
GdipTranslatePenTransform: _Callable[[_type.GpPen,  # pen
                                      _type.REAL,  # dx
                                      _type.REAL,  # dy
                                      _enum.GpMatrixOrder],  # order
                                     _enum.GpStatus]
GdipScalePenTransform: _Callable[[_type.GpPen,  # pen
                                  _type.REAL,  # sx
                                  _type.REAL,  # sy
                                  _enum.GpMatrixOrder],  # order
                                 _enum.GpStatus]
GdipRotatePenTransform: _Callable[[_type.GpPen,  # pen
                                   _type.REAL,  # angle
                                   _enum.GpMatrixOrder],  # order
                                  _enum.GpStatus]
GdipSetPenColor: _Callable[[_type.GpPen,  # pen
                            _type.ARGB],  # argb
                           _enum.GpStatus]
GdipGetPenColor: _Callable[[_type.GpPen,  # pen
                            _Pointer[_type.ARGB]],  # argb
                           _enum.GpStatus]
GdipSetPenBrushFill: _Callable[[_type.GpPen,  # pen
                                _type.GpBrush],  # brush
                               _enum.GpStatus]
GdipGetPenBrushFill: _Callable[[_type.GpPen,  # pen
                                _Pointer[_type.GpBrush]],  # brush
                               _enum.GpStatus]
GdipGetPenFillType: _Callable[[_type.GpPen,  # pen
                               _Pointer[_enum.GpPenType]],  # type
                              _enum.GpStatus]
GdipGetPenDashStyle: _Callable[[_type.GpPen,  # pen
                                _Pointer[_enum.GpDashStyle]],  # dashstyle
                               _enum.GpStatus]
GdipSetPenDashStyle: _Callable[[_type.GpPen,  # pen
                                _enum.GpDashStyle],  # dashstyle
                               _enum.GpStatus]
GdipGetPenDashOffset: _Callable[[_type.GpPen,  # pen
                                 _Pointer[_type.REAL]],  # offset
                                _enum.GpStatus]
GdipSetPenDashOffset: _Callable[[_type.GpPen,  # pen
                                 _type.REAL],  # offset
                                _enum.GpStatus]
GdipGetPenDashCount: _Callable[[_type.GpPen,  # pen
                                _Pointer[_type.INT]],  # count
                               _enum.GpStatus]
GdipSetPenDashArray: _Callable[[_type.GpPen,  # pen
                                _Pointer[_type.REAL],  # dash
                                _type.INT],  # count
                               _enum.GpStatus]
GdipGetPenDashArray: _Callable[[_type.GpPen,  # pen
                                _Pointer[_type.REAL],  # dash
                                _type.INT],  # count
                               _enum.GpStatus]
GdipGetPenCompoundCount: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_type.INT]],  # count
                                   _enum.GpStatus]
GdipSetPenCompoundArray: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_type.REAL],  # dash
                                    _type.INT],  # count
                                   _enum.GpStatus]
GdipGetPenCompoundArray: _Callable[[_type.GpPen,  # pen
                                    _Pointer[_type.REAL],  # dash
                                    _type.INT],  # count
                                   _enum.GpStatus]
GdipCreateCustomLineCap: _Callable[[_type.GpPath,  # fillPath
                                    _type.GpPath,  # strokePath
                                    _enum.GpLineCap,  # baseCap
                                    _type.REAL,  # baseInset
                                    _Pointer[_type.GpCustomLineCap]],  # customCap
                                   _enum.GpStatus]
GdipDeleteCustomLineCap: _Callable[[_type.GpCustomLineCap],  # customCap
                                   _enum.GpStatus]
GdipCloneCustomLineCap: _Callable[[_type.GpCustomLineCap,  # customCap
                                   _Pointer[_type.GpCustomLineCap]],  # clonedCap
                                  _enum.GpStatus]
GdipGetCustomLineCapType: _Callable[[_type.GpCustomLineCap,  # customCap
                                     _Pointer[_enum.CustomLineCapType]],  # capType
                                    _enum.GpStatus]
GdipSetCustomLineCapStrokeCaps: _Callable[[_type.GpCustomLineCap,  # customCap
                                           _enum.GpLineCap,  # startCap
                                           _enum.GpLineCap],  # endCap
                                          _enum.GpStatus]
GdipGetCustomLineCapStrokeCaps: _Callable[[_type.GpCustomLineCap,  # customCap
                                           _Pointer[_enum.GpLineCap],  # startCap
                                           _Pointer[_enum.GpLineCap]],  # endCap
                                          _enum.GpStatus]
GdipSetCustomLineCapStrokeJoin: _Callable[[_type.GpCustomLineCap,  # customCap
                                           _enum.GpLineJoin],  # lineJoin
                                          _enum.GpStatus]
GdipGetCustomLineCapStrokeJoin: _Callable[[_type.GpCustomLineCap,  # customCap
                                           _Pointer[_enum.GpLineJoin]],  # lineJoin
                                          _enum.GpStatus]
GdipSetCustomLineCapBaseCap: _Callable[[_type.GpCustomLineCap,  # customCap
                                        _enum.GpLineCap],  # baseCap
                                       _enum.GpStatus]
GdipGetCustomLineCapBaseCap: _Callable[[_type.GpCustomLineCap,  # customCap
                                        _Pointer[_enum.GpLineCap]],  # baseCap
                                       _enum.GpStatus]
GdipSetCustomLineCapBaseInset: _Callable[[_type.GpCustomLineCap,  # customCap
                                          _type.REAL],  # inset
                                         _enum.GpStatus]
GdipGetCustomLineCapBaseInset: _Callable[[_type.GpCustomLineCap,  # customCap
                                          _Pointer[_type.REAL]],  # inset
                                         _enum.GpStatus]
GdipSetCustomLineCapWidthScale: _Callable[[_type.GpCustomLineCap,  # customCap
                                           _type.REAL],  # widthScale
                                          _enum.GpStatus]
GdipGetCustomLineCapWidthScale: _Callable[[_type.GpCustomLineCap,  # customCap
                                           _Pointer[_type.REAL]],  # widthScale
                                          _enum.GpStatus]
GdipCreateAdjustableArrowCap: _Callable[[_type.REAL,  # height
                                         _type.REAL,  # width
                                         _type.BOOL,  # isFilled
                                         _Pointer[_type.GpAdjustableArrowCap]],  # cap
                                        _enum.GpStatus]
GdipSetAdjustableArrowCapHeight: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                            _type.REAL],  # height
                                           _enum.GpStatus]
GdipGetAdjustableArrowCapHeight: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                            _Pointer[_type.REAL]],  # height
                                           _enum.GpStatus]
GdipSetAdjustableArrowCapWidth: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                           _type.REAL],  # width
                                          _enum.GpStatus]
GdipGetAdjustableArrowCapWidth: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                           _Pointer[_type.REAL]],  # width
                                          _enum.GpStatus]
GdipSetAdjustableArrowCapMiddleInset: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                 _type.REAL],  # middleInset
                                                _enum.GpStatus]
GdipGetAdjustableArrowCapMiddleInset: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                                 _Pointer[_type.REAL]],  # middleInset
                                                _enum.GpStatus]
GdipSetAdjustableArrowCapFillState: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                               _type.BOOL],  # fillState
                                              _enum.GpStatus]
GdipGetAdjustableArrowCapFillState: _Callable[[_type.GpAdjustableArrowCap,  # cap
                                               _Pointer[_type.BOOL]],  # fillState
                                              _enum.GpStatus]
GdipLoadImageFromStream: _Callable[[_objidlbase.IStream,  # stream
                                    _Pointer[_type.GpImage]],  # image
                                   _enum.GpStatus]
GdipLoadImageFromFile: _Callable[[_type.LPWSTR,  # filename
                                  _Pointer[_type.GpImage]],  # image
                                 _enum.GpStatus]
GdipLoadImageFromStreamICM: _Callable[[_objidlbase.IStream,  # stream
                                       _Pointer[_type.GpImage]],  # image
                                      _enum.GpStatus]
GdipLoadImageFromFileICM: _Callable[[_type.LPWSTR,  # filename
                                     _Pointer[_type.GpImage]],  # image
                                    _enum.GpStatus]
GdipCloneImage: _Callable[[_type.GpImage,  # image
                           _Pointer[_type.GpImage]],  # cloneImage
                          _enum.GpStatus]
GdipDisposeImage: _Callable[[_type.GpImage],  # image
                            _enum.GpStatus]
GdipSaveImageToFile: _Callable[[_type.GpImage,  # image
                                _type.LPWSTR,  # filename
                                _Pointer[_struct.CLSID],  # clsidEncoder
                                _Optional[_Pointer[_struct.EncoderParameters]]],  # encoderParams
                               _enum.GpStatus]
GdipSaveImageToStream: _Callable[[_type.GpImage,  # image
                                  _objidlbase.IStream,  # stream
                                  _Pointer[_struct.CLSID],  # clsidEncoder
                                  _Pointer[_struct.EncoderParameters]],  # encoderParams
                                 _enum.GpStatus]
GdipSaveAdd: _Callable[[_type.GpImage,  # image
                        _Pointer[_struct.EncoderParameters]],  # encoderParams
                       _enum.GpStatus]
GdipSaveAddImage: _Callable[[_type.GpImage,  # image
                             _type.GpImage,  # newImage
                             _Pointer[_struct.EncoderParameters]],  # encoderParams
                            _enum.GpStatus]
GdipGetImageGraphicsContext: _Callable[[_type.GpImage,  # image
                                        _Pointer[_type.GpGraphics]],  # graphics
                                       _enum.GpStatus]
GdipGetImageBounds: _Callable[[_type.GpImage,  # image
                               _Pointer[_struct.GpRectF],  # srcRect
                               _Pointer[_enum.GpUnit]],  # srcUnit
                              _enum.GpStatus]
GdipGetImageDimension: _Callable[[_type.GpImage,  # image
                                  _Pointer[_type.REAL],  # width
                                  _Pointer[_type.REAL]],  # height
                                 _enum.GpStatus]
GdipGetImageType: _Callable[[_type.GpImage,  # image
                             _Pointer[_enum.ImageType]],  # type
                            _enum.GpStatus]
GdipGetImageWidth: _Callable[[_type.GpImage,  # image
                              _Pointer[_type.UINT]],  # width
                             _enum.GpStatus]
GdipGetImageHeight: _Callable[[_type.GpImage,  # image
                               _Pointer[_type.UINT]],  # height
                              _enum.GpStatus]
GdipGetImageHorizontalResolution: _Callable[[_type.GpImage,  # image
                                             _Pointer[_type.REAL]],  # resolution
                                            _enum.GpStatus]
GdipGetImageVerticalResolution: _Callable[[_type.GpImage,  # image
                                           _Pointer[_type.REAL]],  # resolution
                                          _enum.GpStatus]
GdipGetImageFlags: _Callable[[_type.GpImage,  # image
                              _Pointer[_type.UINT]],  # flags
                             _enum.GpStatus]
GdipGetImageRawFormat: _Callable[[_type.GpImage,  # image
                                  _Pointer[_struct.GUID]],  # format
                                 _enum.GpStatus]
GdipGetImagePixelFormat: _Callable[[_type.GpImage,  # image
                                    _Pointer[_type.PixelFormat]],  # format
                                   _enum.GpStatus]
GdipGetImageThumbnail: _Callable[[_type.GpImage,  # image
                                  _type.UINT,  # thumbWidth
                                  _type.UINT,  # thumbHeight
                                  _Pointer[_type.GpImage],  # thumbImage
                                  _type.GetThumbnailImageAbort,  # callback
                                  _Optional[_Pointer[_type.VOID]]],  # callbackData
                                 _enum.GpStatus]
GdipGetEncoderParameterListSize: _Callable[[_type.GpImage,  # image
                                            _Pointer[_struct.CLSID],  # clsidEncoder
                                            _Pointer[_type.UINT]],  # size
                                           _enum.GpStatus]
GdipGetEncoderParameterList: _Callable[[_type.GpImage,  # image
                                        _Pointer[_struct.CLSID],  # clsidEncoder
                                        _type.UINT,  # size
                                        _Pointer[_struct.EncoderParameters]],  # buffer
                                       _enum.GpStatus]
GdipImageGetFrameDimensionsCount: _Callable[[_type.GpImage,  # image
                                             _Pointer[_type.UINT]],  # count
                                            _enum.GpStatus]
GdipImageGetFrameDimensionsList: _Callable[[_type.GpImage,  # image
                                            _Pointer[_struct.GUID],  # dimensionIDs
                                            _type.UINT],  # count
                                           _enum.GpStatus]
GdipImageGetFrameCount: _Callable[[_type.GpImage,  # image
                                   _Pointer[_struct.GUID],  # dimensionID
                                   _Pointer[_type.UINT]],  # count
                                  _enum.GpStatus]
GdipImageSelectActiveFrame: _Callable[[_type.GpImage,  # image
                                       _Pointer[_struct.GUID],  # dimensionID
                                       _type.UINT],  # frameIndex
                                      _enum.GpStatus]
GdipImageRotateFlip: _Callable[[_type.GpImage,  # image
                                _enum.RotateFlipType],  # rfType
                               _enum.GpStatus]
GdipGetImagePalette: _Callable[[_type.GpImage,  # image
                                _Pointer[_struct.ColorPalette],  # palette
                                _type.INT],  # size
                               _enum.GpStatus]
GdipSetImagePalette: _Callable[[_type.GpImage,  # image
                                _Pointer[_struct.ColorPalette]],  # palette
                               _enum.GpStatus]
GdipGetImagePaletteSize: _Callable[[_type.GpImage,  # image
                                    _Pointer[_type.INT]],  # size
                                   _enum.GpStatus]
GdipGetPropertyCount: _Callable[[_type.GpImage,  # image
                                 _Pointer[_type.UINT]],  # numOfProperty
                                _enum.GpStatus]
GdipGetPropertyIdList: _Callable[[_type.GpImage,  # image
                                  _type.UINT,  # numOfProperty
                                  _Pointer[_type.PROPID]],  # list
                                 _enum.GpStatus]
GdipGetPropertyItemSize: _Callable[[_type.GpImage,  # image
                                    _type.PROPID,  # propId
                                    _Pointer[_type.UINT]],  # size
                                   _enum.GpStatus]
GdipGetPropertyItem: _Callable[[_type.GpImage,  # image
                                _type.PROPID,  # propId
                                _type.UINT,  # propSize
                                _Pointer[_struct.PropertyItem]],  # buffer
                               _enum.GpStatus]
GdipGetPropertySize: _Callable[[_type.GpImage,  # image
                                _Pointer[_type.UINT],  # totalBufferSize
                                _Pointer[_type.UINT]],  # numProperties
                               _enum.GpStatus]
GdipGetAllPropertyItems: _Callable[[_type.GpImage,  # image
                                    _type.UINT,  # totalBufferSize
                                    _type.UINT,  # numProperties
                                    _Pointer[_struct.PropertyItem]],  # allItems
                                   _enum.GpStatus]
GdipRemovePropertyItem: _Callable[[_type.GpImage,  # image
                                   _type.PROPID],  # propId
                                  _enum.GpStatus]
GdipSetPropertyItem: _Callable[[_type.GpImage,  # image
                                _Pointer[_struct.PropertyItem]],  # item
                               _enum.GpStatus]
GdipFindFirstImageItem: _Callable[[_type.GpImage,  # image
                                   _Pointer[_struct.ImageItemData]],  # item
                                  _enum.GpStatus]
GdipFindNextImageItem: _Callable[[_type.GpImage,  # image
                                  _Pointer[_struct.ImageItemData]],  # item
                                 _enum.GpStatus]
GdipGetImageItemData: _Callable[[_type.GpImage,  # image
                                 _Pointer[_struct.ImageItemData]],  # item
                                _enum.GpStatus]
GdipImageForceValidation: _Callable[[_type.GpImage],  # image
                                    _enum.GpStatus]
GdipCreateBitmapFromStream: _Callable[[_objidlbase.IStream,  # stream
                                       _Pointer[_type.GpBitmap]],  # bitmap
                                      _enum.GpStatus]
GdipCreateBitmapFromFile: _Callable[[_type.LPWSTR,  # filename
                                     _Pointer[_type.GpBitmap]],  # bitmap
                                    _enum.GpStatus]
GdipCreateBitmapFromStreamICM: _Callable[[_objidlbase.IStream,  # stream
                                          _Pointer[_type.GpBitmap]],  # bitmap
                                         _enum.GpStatus]
GdipCreateBitmapFromFileICM: _Callable[[_type.LPWSTR,  # filename
                                        _Pointer[_type.GpBitmap]],  # bitmap
                                       _enum.GpStatus]
GdipCreateBitmapFromScan0: _Callable[[_type.INT,  # width
                                      _type.INT,  # height
                                      _type.INT,  # stride
                                      _type.PixelFormat,  # format
                                      _Optional[_Pointer[_type.BYTE]],  # scan0
                                      _Pointer[_type.GpBitmap]],  # bitmap
                                     _enum.GpStatus]
GdipCreateBitmapFromGraphics: _Callable[[_type.INT,  # width
                                         _type.INT,  # height
                                         _type.GpGraphics,  # target
                                         _Pointer[_type.GpBitmap]],  # bitmap
                                        _enum.GpStatus]
GdipCreateBitmapFromDirectDrawSurface: _Callable[[_ddraw.IDirectDrawSurface7,  # surface
                                                  _Pointer[_type.GpBitmap]],  # bitmap
                                                 _enum.GpStatus]
GdipCreateBitmapFromGdiDib: _Callable[[_Pointer[_struct.BITMAPINFO],  # gdiBitmapInfo
                                       _Pointer[_type.VOID],  # gdiBitmapData
                                       _Pointer[_type.GpBitmap]],  # bitmap
                                      _enum.GpStatus]
GdipCreateBitmapFromHBITMAP: _Callable[[_type.HBITMAP,  # hbm
                                        _type.HPALETTE,  # hpal
                                        _Pointer[_type.GpBitmap]],  # bitmap
                                       _enum.GpStatus]
GdipCreateHBITMAPFromBitmap: _Callable[[_type.GpBitmap,  # bitmap
                                        _Pointer[_type.HBITMAP],  # hbmReturn
                                        _type.ARGB],  # background
                                       _enum.GpStatus]
GdipCreateBitmapFromHICON: _Callable[[_type.HICON,  # hicon
                                      _Pointer[_type.GpBitmap]],  # bitmap
                                     _enum.GpStatus]
GdipCreateHICONFromBitmap: _Callable[[_type.GpBitmap,  # bitmap
                                      _Pointer[_type.HICON]],  # hbmReturn
                                     _enum.GpStatus]
GdipCreateBitmapFromResource: _Callable[[_type.HINSTANCE,  # hInstance
                                         _type.LPWSTR,  # lpBitmapName
                                         _Pointer[_type.GpBitmap]],  # bitmap
                                        _enum.GpStatus]
GdipCloneBitmapArea: _Callable[[_type.REAL,  # x
                                _type.REAL,  # y
                                _type.REAL,  # width
                                _type.REAL,  # height
                                _type.PixelFormat,  # format
                                _type.GpBitmap,  # srcBitmap
                                _Pointer[_type.GpBitmap]],  # dstBitmap
                               _enum.GpStatus]
GdipCloneBitmapAreaI: _Callable[[_type.INT,  # x
                                 _type.INT,  # y
                                 _type.INT,  # width
                                 _type.INT,  # height
                                 _type.PixelFormat,  # format
                                 _type.GpBitmap,  # srcBitmap
                                 _Pointer[_type.GpBitmap]],  # dstBitmap
                                _enum.GpStatus]
GdipBitmapLockBits: _Callable[[_type.GpBitmap,  # bitmap
                               _Pointer[_struct.GpRect],  # rect
                               _type.UINT,  # flags
                               _type.PixelFormat,  # format
                               _Pointer[_struct.BitmapData]],  # lockedBitmapData
                              _enum.GpStatus]
GdipBitmapUnlockBits: _Callable[[_type.GpBitmap,  # bitmap
                                 _Pointer[_struct.BitmapData]],  # lockedBitmapData
                                _enum.GpStatus]
GdipBitmapGetPixel: _Callable[[_type.GpBitmap,  # bitmap
                               _type.INT,  # x
                               _type.INT,  # y
                               _Pointer[_type.ARGB]],  # color
                              _enum.GpStatus]
GdipBitmapSetPixel: _Callable[[_type.GpBitmap,  # bitmap
                               _type.INT,  # x
                               _type.INT,  # y
                               _type.ARGB],  # color
                              _enum.GpStatus]
GdipImageSetAbort: _Callable[[_type.GpImage,  # pImage
                              _Pointer[_type.GdiplusAbort]],  # pIAbort
                             _enum.GpStatus]
GdipGraphicsSetAbort: _Callable[[_type.GpGraphics,  # pGraphics
                                 _Pointer[_type.GdiplusAbort]],  # pIAbort
                                _enum.GpStatus]
GdipBitmapConvertFormat: _Callable[[_type.GpBitmap,  # pInputBitmap
                                    _type.PixelFormat,  # format
                                    _enum.DitherType,  # dithertype
                                    _enum.PaletteType,  # palettetype
                                    _Pointer[_struct.ColorPalette],  # palette
                                    _type.REAL],  # alphaThresholdPercent
                                   _enum.GpStatus]
GdipInitializePalette: _Callable[[_Pointer[_struct.ColorPalette],  # palette
                                  _enum.PaletteType,  # palettetype
                                  _type.INT,  # optimalColors
                                  _type.BOOL,  # useTransparentColor
                                  _type.GpBitmap],  # bitmap
                                 _enum.GpStatus]
GdipBitmapApplyEffect: _Callable[[_type.GpBitmap,  # bitmap
                                  _Pointer[_type.CGpEffect],  # effect
                                  _Pointer[_struct.RECT],  # roi
                                  _type.BOOL,  # useAuxData
                                  _Pointer[_Pointer[_type.VOID]],  # auxData
                                  _Pointer[_type.INT]],  # auxDataSize
                                 _enum.GpStatus]
GdipBitmapCreateApplyEffect: _Callable[[_Pointer[_type.GpBitmap],  # inputBitmaps
                                        _type.INT,  # numInputs
                                        _Pointer[_type.CGpEffect],  # effect
                                        _Pointer[_struct.RECT],  # roi
                                        _Pointer[_struct.RECT],  # outputRect
                                        _Pointer[_type.GpBitmap],  # outputBitmap
                                        _type.BOOL,  # useAuxData
                                        _Pointer[_Pointer[_type.VOID]],  # auxData
                                        _Pointer[_type.INT]],  # auxDataSize
                                       _enum.GpStatus]
GdipBitmapGetHistogram: _Callable[[_type.GpBitmap,  # bitmap
                                   _enum.HistogramFormat,  # format
                                   _type.UINT,  # NumberOfEntries
                                   _Pointer[_type.UINT],  # channel0
                                   _Pointer[_type.UINT],  # channel1
                                   _Pointer[_type.UINT],  # channel2
                                   _Pointer[_type.UINT]],  # channel3
                                  _enum.GpStatus]
GdipBitmapGetHistogramSize: _Callable[[_enum.HistogramFormat,  # format
                                       _Pointer[_type.UINT]],  # NumberOfEntries
                                      _enum.GpStatus]
GdipBitmapSetResolution: _Callable[[_type.GpBitmap,  # bitmap
                                    _type.REAL,  # xdpi
                                    _type.REAL],  # ydpi
                                   _enum.GpStatus]
GdipCreateImageAttributes: _Callable[[_Pointer[_type.GpImageAttributes]],  # imageattr
                                     _enum.GpStatus]
GdipCloneImageAttributes: _Callable[[_type.GpImageAttributes,  # imageattr
                                     _Pointer[_type.GpImageAttributes]],  # cloneImageattr
                                    _enum.GpStatus]
GdipDisposeImageAttributes: _Callable[[_type.GpImageAttributes],  # imageattr
                                      _enum.GpStatus]
GdipSetImageAttributesToIdentity: _Callable[[_type.GpImageAttributes,  # imageattr
                                             _enum.ColorAdjustType],  # type
                                            _enum.GpStatus]
GdipResetImageAttributes: _Callable[[_type.GpImageAttributes,  # imageattr
                                     _enum.ColorAdjustType],  # type
                                    _enum.GpStatus]
GdipSetImageAttributesColorMatrix: _Callable[[_type.GpImageAttributes,  # imageattr
                                              _enum.ColorAdjustType,  # type
                                              _type.BOOL,  # enableFlag
                                              _Optional[_Pointer[_struct.ColorMatrix]],  # colorMatrix
                                              _Optional[_Pointer[_struct.ColorMatrix]],  # grayMatrix
                                              _enum.ColorMatrixFlags],  # flags
                                             _enum.GpStatus]
GdipSetImageAttributesThreshold: _Callable[[_type.GpImageAttributes,  # imageattr
                                            _enum.ColorAdjustType,  # type
                                            _type.BOOL,  # enableFlag
                                            _type.REAL],  # threshold
                                           _enum.GpStatus]
GdipSetImageAttributesGamma: _Callable[[_type.GpImageAttributes,  # imageattr
                                        _enum.ColorAdjustType,  # type
                                        _type.BOOL,  # enableFlag
                                        _type.REAL],  # gamma
                                       _enum.GpStatus]
GdipSetImageAttributesNoOp: _Callable[[_type.GpImageAttributes,  # imageattr
                                       _enum.ColorAdjustType,  # type
                                       _type.BOOL],  # enableFlag
                                      _enum.GpStatus]
GdipSetImageAttributesColorKeys: _Callable[[_type.GpImageAttributes,  # imageattr
                                            _enum.ColorAdjustType,  # type
                                            _type.BOOL,  # enableFlag
                                            _type.ARGB,  # colorLow
                                            _type.ARGB],  # colorHigh
                                           _enum.GpStatus]
GdipSetImageAttributesOutputChannel: _Callable[[_type.GpImageAttributes,  # imageattr
                                                _enum.ColorAdjustType,  # type
                                                _type.BOOL,  # enableFlag
                                                _enum.ColorChannelFlags],  # channelFlags
                                               _enum.GpStatus]
GdipSetImageAttributesOutputChannelColorProfile: _Callable[[_type.GpImageAttributes,  # imageattr
                                                            _enum.ColorAdjustType,  # type
                                                            _type.BOOL,  # enableFlag
                                                            _Optional[_type.LPWSTR]],  # colorProfileFilename
                                                           _enum.GpStatus]
GdipSetImageAttributesRemapTable: _Callable[[_type.GpImageAttributes,  # imageattr
                                             _enum.ColorAdjustType,  # type
                                             _type.BOOL,  # enableFlag
                                             _type.UINT,  # mapSize
                                             _Optional[_Pointer[_struct.ColorMap]]],  # map
                                            _enum.GpStatus]
GdipSetImageAttributesWrapMode: _Callable[[_type.GpImageAttributes,  # imageAttr
                                           _enum.WrapMode,  # wrap
                                           _type.ARGB,  # argb
                                           _type.BOOL],  # clamp
                                          _enum.GpStatus]
GdipSetImageAttributesICMMode: _Callable[[_type.GpImageAttributes,  # imageAttr
                                          _type.BOOL],  # on
                                         _enum.GpStatus]
GdipGetImageAttributesAdjustedPalette: _Callable[[_type.GpImageAttributes,  # imageAttr
                                                  _Pointer[_struct.ColorPalette],  # colorPalette
                                                  _enum.ColorAdjustType],  # colorAdjustType
                                                 _enum.GpStatus]
GdipFlush: _Callable[[_type.GpGraphics,  # graphics
                      _enum.GpFlushIntention],  # intention
                     _enum.GpStatus]
GdipCreateFromHDC: _Callable[[_type.HDC,  # hdc
                              _Pointer[_type.GpGraphics]],  # graphics
                             _enum.GpStatus]
GdipCreateFromHDC2: _Callable[[_type.HDC,  # hdc
                               _type.HANDLE,  # hDevice
                               _Pointer[_type.GpGraphics]],  # graphics
                              _enum.GpStatus]
GdipCreateFromHWND: _Callable[[_type.HWND,  # hwnd
                               _Pointer[_type.GpGraphics]],  # graphics
                              _enum.GpStatus]
GdipCreateFromHWNDICM: _Callable[[_type.HWND,  # hwnd
                                  _Pointer[_type.GpGraphics]],  # graphics
                                 _enum.GpStatus]
GdipDeleteGraphics: _Callable[[_type.GpGraphics],  # graphics
                              _enum.GpStatus]
GdipGetDC: _Callable[[_type.GpGraphics,  # graphics
                      _Pointer[_type.HDC]],  # hdc
                     _enum.GpStatus]
GdipReleaseDC: _Callable[[_type.GpGraphics,  # graphics
                          _type.HDC],  # hdc
                         _enum.GpStatus]
GdipSetCompositingMode: _Callable[[_type.GpGraphics,  # graphics
                                   _enum.CompositingMode],  # compositingMode
                                  _enum.GpStatus]
GdipGetCompositingMode: _Callable[[_type.GpGraphics,  # graphics
                                   _Pointer[_enum.CompositingMode]],  # compositingMode
                                  _enum.GpStatus]
GdipSetRenderingOrigin: _Callable[[_type.GpGraphics,  # graphics
                                   _type.INT,  # x
                                   _type.INT],  # y
                                  _enum.GpStatus]
GdipGetRenderingOrigin: _Callable[[_type.GpGraphics,  # graphics
                                   _Pointer[_type.INT],  # x
                                   _Pointer[_type.INT]],  # y
                                  _enum.GpStatus]
GdipSetCompositingQuality: _Callable[[_type.GpGraphics,  # graphics
                                      _enum.CompositingQuality],  # compositingQuality
                                     _enum.GpStatus]
GdipGetCompositingQuality: _Callable[[_type.GpGraphics,  # graphics
                                      _Pointer[_enum.CompositingQuality]],  # compositingQuality
                                     _enum.GpStatus]
GdipSetSmoothingMode: _Callable[[_type.GpGraphics,  # graphics
                                 _enum.SmoothingMode],  # smoothingMode
                                _enum.GpStatus]
GdipGetSmoothingMode: _Callable[[_type.GpGraphics,  # graphics
                                 _Pointer[_enum.SmoothingMode]],  # smoothingMode
                                _enum.GpStatus]
GdipSetPixelOffsetMode: _Callable[[_type.GpGraphics,  # graphics
                                   _enum.PixelOffsetMode],  # pixelOffsetMode
                                  _enum.GpStatus]
GdipGetPixelOffsetMode: _Callable[[_type.GpGraphics,  # graphics
                                   _Pointer[_enum.PixelOffsetMode]],  # pixelOffsetMode
                                  _enum.GpStatus]
GdipSetTextRenderingHint: _Callable[[_type.GpGraphics,  # graphics
                                     _enum.TextRenderingHint],  # mode
                                    _enum.GpStatus]
GdipGetTextRenderingHint: _Callable[[_type.GpGraphics,  # graphics
                                     _Pointer[_enum.TextRenderingHint]],  # mode
                                    _enum.GpStatus]
GdipSetTextContrast: _Callable[[_type.GpGraphics,  # graphics
                                _type.UINT],  # contrast
                               _enum.GpStatus]
GdipGetTextContrast: _Callable[[_type.GpGraphics,  # graphics
                                _Pointer[_type.UINT]],  # contrast
                               _enum.GpStatus]
GdipSetInterpolationMode: _Callable[[_type.GpGraphics,  # graphics
                                     _enum.InterpolationMode],  # interpolationMode
                                    _enum.GpStatus]
GdipGetInterpolationMode: _Callable[[_type.GpGraphics,  # graphics
                                     _Pointer[_enum.InterpolationMode]],  # interpolationMode
                                    _enum.GpStatus]
GdipSetWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpMatrix],  # matrix
                                 _enum.GpStatus]
GdipResetWorldTransform: _Callable[[_type.GpGraphics],  # graphics
                                   _enum.GpStatus]
GdipMultiplyWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                       _type.GpMatrix,  # matrix
                                       _enum.GpMatrixOrder],  # order
                                      _enum.GpStatus]
GdipTranslateWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                        _type.REAL,  # dx
                                        _type.REAL,  # dy
                                        _enum.GpMatrixOrder],  # order
                                       _enum.GpStatus]
GdipScaleWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                    _type.REAL,  # sx
                                    _type.REAL,  # sy
                                    _enum.GpMatrixOrder],  # order
                                   _enum.GpStatus]
GdipRotateWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                     _type.REAL,  # angle
                                     _enum.GpMatrixOrder],  # order
                                    _enum.GpStatus]
GdipGetWorldTransform: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpMatrix],  # matrix
                                 _enum.GpStatus]
GdipResetPageTransform: _Callable[[_type.GpGraphics],  # graphics
                                  _enum.GpStatus]
GdipGetPageUnit: _Callable[[_type.GpGraphics,  # graphics
                            _Pointer[_enum.GpUnit]],  # unit
                           _enum.GpStatus]
GdipGetPageScale: _Callable[[_type.GpGraphics,  # graphics
                             _Pointer[_type.REAL]],  # scale
                            _enum.GpStatus]
GdipSetPageUnit: _Callable[[_type.GpGraphics,  # graphics
                            _enum.GpUnit],  # unit
                           _enum.GpStatus]
GdipSetPageScale: _Callable[[_type.GpGraphics,  # graphics
                             _type.REAL],  # scale
                            _enum.GpStatus]
GdipGetDpiX: _Callable[[_type.GpGraphics,  # graphics
                        _Pointer[_type.REAL]],  # dpi
                       _enum.GpStatus]
GdipGetDpiY: _Callable[[_type.GpGraphics,  # graphics
                        _Pointer[_type.REAL]],  # dpi
                       _enum.GpStatus]
GdipTransformPoints: _Callable[[_type.GpGraphics,  # graphics
                                _enum.GpCoordinateSpace,  # destSpace
                                _enum.GpCoordinateSpace,  # srcSpace
                                _Pointer[_struct.GpPointF],  # points
                                _type.INT],  # count
                               _enum.GpStatus]
GdipTransformPointsI: _Callable[[_type.GpGraphics,  # graphics
                                 _enum.GpCoordinateSpace,  # destSpace
                                 _enum.GpCoordinateSpace,  # srcSpace
                                 _Pointer[_struct.GpPoint],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
GdipGetNearestColor: _Callable[[_type.GpGraphics,  # graphics
                                _Pointer[_type.ARGB]],  # argb
                               _enum.GpStatus]
GdipDrawLine: _Callable[[_type.GpGraphics,  # graphics
                         _type.GpPen,  # pen
                         _type.REAL,  # x1
                         _type.REAL,  # y1
                         _type.REAL,  # x2
                         _type.REAL],  # y2
                        _enum.GpStatus]
GdipDrawLineI: _Callable[[_type.GpGraphics,  # graphics
                          _type.GpPen,  # pen
                          _type.INT,  # x1
                          _type.INT,  # y1
                          _type.INT,  # x2
                          _type.INT],  # y2
                         _enum.GpStatus]
GdipDrawLines: _Callable[[_type.GpGraphics,  # graphics
                          _type.GpPen,  # pen
                          _Pointer[_struct.GpPointF],  # points
                          _type.INT],  # count
                         _enum.GpStatus]
GdipDrawLinesI: _Callable[[_type.GpGraphics,  # graphics
                           _type.GpPen,  # pen
                           _Pointer[_struct.GpPoint],  # points
                           _type.INT],  # count
                          _enum.GpStatus]
GdipDrawArc: _Callable[[_type.GpGraphics,  # graphics
                        _type.GpPen,  # pen
                        _type.REAL,  # x
                        _type.REAL,  # y
                        _type.REAL,  # width
                        _type.REAL,  # height
                        _type.REAL,  # startAngle
                        _type.REAL],  # sweepAngle
                       _enum.GpStatus]
GdipDrawArcI: _Callable[[_type.GpGraphics,  # graphics
                         _type.GpPen,  # pen
                         _type.INT,  # x
                         _type.INT,  # y
                         _type.INT,  # width
                         _type.INT,  # height
                         _type.REAL,  # startAngle
                         _type.REAL],  # sweepAngle
                        _enum.GpStatus]
GdipDrawBezier: _Callable[[_type.GpGraphics,  # graphics
                           _type.GpPen,  # pen
                           _type.REAL,  # x1
                           _type.REAL,  # y1
                           _type.REAL,  # x2
                           _type.REAL,  # y2
                           _type.REAL,  # x3
                           _type.REAL,  # y3
                           _type.REAL,  # x4
                           _type.REAL],  # y4
                          _enum.GpStatus]
GdipDrawBezierI: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _type.INT,  # x1
                            _type.INT,  # y1
                            _type.INT,  # x2
                            _type.INT,  # y2
                            _type.INT,  # x3
                            _type.INT,  # y3
                            _type.INT,  # x4
                            _type.INT],  # y4
                           _enum.GpStatus]
GdipDrawBeziers: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _Pointer[_struct.GpPointF],  # points
                            _type.INT],  # count
                           _enum.GpStatus]
GdipDrawBeziersI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpPen,  # pen
                             _Pointer[_struct.GpPoint],  # points
                             _type.INT],  # count
                            _enum.GpStatus]
GdipDrawRectangle: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpPen,  # pen
                              _type.REAL,  # x
                              _type.REAL,  # y
                              _type.REAL,  # width
                              _type.REAL],  # height
                             _enum.GpStatus]
GdipDrawRectangleI: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpPen,  # pen
                               _type.INT,  # x
                               _type.INT,  # y
                               _type.INT,  # width
                               _type.INT],  # height
                              _enum.GpStatus]
GdipDrawRectangles: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpPen,  # pen
                               _Pointer[_struct.GpRectF],  # rects
                               _type.INT],  # count
                              _enum.GpStatus]
GdipDrawRectanglesI: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _Pointer[_struct.GpRect],  # rects
                                _type.INT],  # count
                               _enum.GpStatus]
GdipDrawEllipse: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _type.REAL,  # x
                            _type.REAL,  # y
                            _type.REAL,  # width
                            _type.REAL],  # height
                           _enum.GpStatus]
GdipDrawEllipseI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpPen,  # pen
                             _type.INT,  # x
                             _type.INT,  # y
                             _type.INT,  # width
                             _type.INT],  # height
                            _enum.GpStatus]
GdipDrawPie: _Callable[[_type.GpGraphics,  # graphics
                        _type.GpPen,  # pen
                        _type.REAL,  # x
                        _type.REAL,  # y
                        _type.REAL,  # width
                        _type.REAL,  # height
                        _type.REAL,  # startAngle
                        _type.REAL],  # sweepAngle
                       _enum.GpStatus]
GdipDrawPieI: _Callable[[_type.GpGraphics,  # graphics
                         _type.GpPen,  # pen
                         _type.INT,  # x
                         _type.INT,  # y
                         _type.INT,  # width
                         _type.INT,  # height
                         _type.REAL,  # startAngle
                         _type.REAL],  # sweepAngle
                        _enum.GpStatus]
GdipDrawPolygon: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _Pointer[_struct.GpPointF],  # points
                            _type.INT],  # count
                           _enum.GpStatus]
GdipDrawPolygonI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpPen,  # pen
                             _Pointer[_struct.GpPoint],  # points
                             _type.INT],  # count
                            _enum.GpStatus]
GdipDrawPath: _Callable[[_type.GpGraphics,  # graphics
                         _type.GpPen,  # pen
                         _type.GpPath],  # path
                        _enum.GpStatus]
GdipDrawCurve: _Callable[[_type.GpGraphics,  # graphics
                          _type.GpPen,  # pen
                          _Pointer[_struct.GpPointF],  # points
                          _type.INT],  # count
                         _enum.GpStatus]
GdipDrawCurveI: _Callable[[_type.GpGraphics,  # graphics
                           _type.GpPen,  # pen
                           _Pointer[_struct.GpPoint],  # points
                           _type.INT],  # count
                          _enum.GpStatus]
GdipDrawCurve2: _Callable[[_type.GpGraphics,  # graphics
                           _type.GpPen,  # pen
                           _Pointer[_struct.GpPointF],  # points
                           _type.INT,  # count
                           _type.REAL],  # tension
                          _enum.GpStatus]
GdipDrawCurve2I: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _Pointer[_struct.GpPoint],  # points
                            _type.INT,  # count
                            _type.REAL],  # tension
                           _enum.GpStatus]
GdipDrawCurve3: _Callable[[_type.GpGraphics,  # graphics
                           _type.GpPen,  # pen
                           _Pointer[_struct.GpPointF],  # points
                           _type.INT,  # count
                           _type.INT,  # offset
                           _type.INT,  # numberOfSegments
                           _type.REAL],  # tension
                          _enum.GpStatus]
GdipDrawCurve3I: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPen,  # pen
                            _Pointer[_struct.GpPoint],  # points
                            _type.INT,  # count
                            _type.INT,  # offset
                            _type.INT,  # numberOfSegments
                            _type.REAL],  # tension
                           _enum.GpStatus]
GdipDrawClosedCurve: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpPen,  # pen
                                _Pointer[_struct.GpPointF],  # points
                                _type.INT],  # count
                               _enum.GpStatus]
GdipDrawClosedCurveI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpPen,  # pen
                                 _Pointer[_struct.GpPoint],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
GdipDrawClosedCurve2: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpPen,  # pen
                                 _Pointer[_struct.GpPointF],  # points
                                 _type.INT,  # count
                                 _type.REAL],  # tension
                                _enum.GpStatus]
GdipDrawClosedCurve2I: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpPen,  # pen
                                  _Pointer[_struct.GpPoint],  # points
                                  _type.INT,  # count
                                  _type.REAL],  # tension
                                 _enum.GpStatus]
GdipGraphicsClear: _Callable[[_type.GpGraphics,  # graphics
                              _type.ARGB],  # color
                             _enum.GpStatus]
GdipFillRectangle: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpBrush,  # brush
                              _type.REAL,  # x
                              _type.REAL,  # y
                              _type.REAL,  # width
                              _type.REAL],  # height
                             _enum.GpStatus]
GdipFillRectangleI: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpBrush,  # brush
                               _type.INT,  # x
                               _type.INT,  # y
                               _type.INT,  # width
                               _type.INT],  # height
                              _enum.GpStatus]
GdipFillRectangles: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpBrush,  # brush
                               _Pointer[_struct.GpRectF],  # rects
                               _type.INT],  # count
                              _enum.GpStatus]
GdipFillRectanglesI: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpBrush,  # brush
                                _Pointer[_struct.GpRect],  # rects
                                _type.INT],  # count
                               _enum.GpStatus]
GdipFillPolygon: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpBrush,  # brush
                            _Pointer[_struct.GpPointF],  # points
                            _type.INT,  # count
                            _enum.GpFillMode],  # fillMode
                           _enum.GpStatus]
GdipFillPolygonI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpBrush,  # brush
                             _Pointer[_struct.GpPoint],  # points
                             _type.INT,  # count
                             _enum.GpFillMode],  # fillMode
                            _enum.GpStatus]
GdipFillPolygon2: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpBrush,  # brush
                             _Pointer[_struct.GpPointF],  # points
                             _type.INT],  # count
                            _enum.GpStatus]
GdipFillPolygon2I: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpBrush,  # brush
                              _Pointer[_struct.GpPoint],  # points
                              _type.INT],  # count
                             _enum.GpStatus]
GdipFillEllipse: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpBrush,  # brush
                            _type.REAL,  # x
                            _type.REAL,  # y
                            _type.REAL,  # width
                            _type.REAL],  # height
                           _enum.GpStatus]
GdipFillEllipseI: _Callable[[_type.GpGraphics,  # graphics
                             _type.GpBrush,  # brush
                             _type.INT,  # x
                             _type.INT,  # y
                             _type.INT,  # width
                             _type.INT],  # height
                            _enum.GpStatus]
GdipFillPie: _Callable[[_type.GpGraphics,  # graphics
                        _type.GpBrush,  # brush
                        _type.REAL,  # x
                        _type.REAL,  # y
                        _type.REAL,  # width
                        _type.REAL,  # height
                        _type.REAL,  # startAngle
                        _type.REAL],  # sweepAngle
                       _enum.GpStatus]
GdipFillPieI: _Callable[[_type.GpGraphics,  # graphics
                         _type.GpBrush,  # brush
                         _type.INT,  # x
                         _type.INT,  # y
                         _type.INT,  # width
                         _type.INT,  # height
                         _type.REAL,  # startAngle
                         _type.REAL],  # sweepAngle
                        _enum.GpStatus]
GdipFillPath: _Callable[[_type.GpGraphics,  # graphics
                         _type.GpBrush,  # brush
                         _type.GpPath],  # path
                        _enum.GpStatus]
GdipFillClosedCurve: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpBrush,  # brush
                                _Pointer[_struct.GpPointF],  # points
                                _type.INT],  # count
                               _enum.GpStatus]
GdipFillClosedCurveI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpBrush,  # brush
                                 _Pointer[_struct.GpPoint],  # points
                                 _type.INT],  # count
                                _enum.GpStatus]
GdipFillClosedCurve2: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpBrush,  # brush
                                 _Pointer[_struct.GpPointF],  # points
                                 _type.INT,  # count
                                 _type.REAL,  # tension
                                 _enum.GpFillMode],  # fillMode
                                _enum.GpStatus]
GdipFillClosedCurve2I: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpBrush,  # brush
                                  _Pointer[_struct.GpPoint],  # points
                                  _type.INT,  # count
                                  _type.REAL,  # tension
                                  _enum.GpFillMode],  # fillMode
                                 _enum.GpStatus]
GdipFillRegion: _Callable[[_type.GpGraphics,  # graphics
                           _type.GpBrush,  # brush
                           _type.GpRegion],  # region
                          _enum.GpStatus]
GdipDrawImage: _Callable[[_type.GpGraphics,  # graphics
                          _type.GpImage,  # image
                          _type.REAL,  # x
                          _type.REAL],  # y
                         _enum.GpStatus]
GdipDrawImageI: _Callable[[_type.GpGraphics,  # graphics
                           _type.GpImage,  # image
                           _type.INT,  # x
                           _type.INT],  # y
                          _enum.GpStatus]
GdipDrawImageRect: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpImage,  # image
                              _type.REAL,  # x
                              _type.REAL,  # y
                              _type.REAL,  # width
                              _type.REAL],  # height
                             _enum.GpStatus]
GdipDrawImageRectI: _Callable[[_type.GpGraphics,  # graphics
                               _type.GpImage,  # image
                               _type.INT,  # x
                               _type.INT,  # y
                               _type.INT,  # width
                               _type.INT],  # height
                              _enum.GpStatus]
GdipDrawImagePoints: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpImage,  # image
                                _Pointer[_struct.GpPointF],  # dstpoints
                                _type.INT],  # count
                               _enum.GpStatus]
GdipDrawImagePointsI: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpImage,  # image
                                 _Pointer[_struct.GpPoint],  # dstpoints
                                 _type.INT],  # count
                                _enum.GpStatus]
GdipDrawImagePointRect: _Callable[[_type.GpGraphics,  # graphics
                                   _type.GpImage,  # image
                                   _type.REAL,  # x
                                   _type.REAL,  # y
                                   _type.REAL,  # srcx
                                   _type.REAL,  # srcy
                                   _type.REAL,  # srcwidth
                                   _type.REAL,  # srcheight
                                   _enum.GpUnit],  # srcUnit
                                  _enum.GpStatus]
GdipDrawImagePointRectI: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpImage,  # image
                                    _type.INT,  # x
                                    _type.INT,  # y
                                    _type.INT,  # srcx
                                    _type.INT,  # srcy
                                    _type.INT,  # srcwidth
                                    _type.INT,  # srcheight
                                    _enum.GpUnit],  # srcUnit
                                   _enum.GpStatus]
GdipDrawImageRectRect: _Callable[[_type.GpGraphics,  # graphics
                                  _type.GpImage,  # image
                                  _type.REAL,  # dstx
                                  _type.REAL,  # dsty
                                  _type.REAL,  # dstwidth
                                  _type.REAL,  # dstheight
                                  _type.REAL,  # srcx
                                  _type.REAL,  # srcy
                                  _type.REAL,  # srcwidth
                                  _type.REAL,  # srcheight
                                  _enum.GpUnit,  # srcUnit
                                  _Optional[_type.GpImageAttributes],  # imageAttributes
                                  _type.DrawImageAbort,  # callback  TODO _Optional _FuncPtr
                                  _Optional[_Pointer[_type.VOID]]],  # callbackData
                                 _enum.GpStatus]
GdipDrawImageRectRectI: _Callable[[_type.GpGraphics,  # graphics
                                   _type.GpImage,  # image
                                   _type.INT,  # dstx
                                   _type.INT,  # dsty
                                   _type.INT,  # dstwidth
                                   _type.INT,  # dstheight
                                   _type.INT,  # srcx
                                   _type.INT,  # srcy
                                   _type.INT,  # srcwidth
                                   _type.INT,  # srcheight
                                   _enum.GpUnit,  # srcUnit
                                   _Optional[_type.GpImageAttributes],  # imageAttributes
                                   _type.DrawImageAbort,  # callback
                                   _Optional[_Pointer[_type.VOID]]],  # callbackData
                                  _enum.GpStatus]
GdipDrawImagePointsRect: _Callable[[_type.GpGraphics,  # graphics
                                    _type.GpImage,  # image
                                    _Pointer[_struct.GpPointF],  # points
                                    _type.INT,  # count
                                    _type.REAL,  # srcx
                                    _type.REAL,  # srcy
                                    _type.REAL,  # srcwidth
                                    _type.REAL,  # srcheight
                                    _enum.GpUnit,  # srcUnit
                                    _Optional[_type.GpImageAttributes],  # imageAttributes
                                    _type.DrawImageAbort,  # callback
                                    _Optional[_Pointer[_type.VOID]]],  # callbackData
                                   _enum.GpStatus]
GdipDrawImagePointsRectI: _Callable[[_type.GpGraphics,  # graphics
                                     _type.GpImage,  # image
                                     _Pointer[_struct.GpPoint],  # points
                                     _type.INT,  # count
                                     _type.INT,  # srcx
                                     _type.INT,  # srcy
                                     _type.INT,  # srcwidth
                                     _type.INT,  # srcheight
                                     _enum.GpUnit,  # srcUnit
                                     _Optional[_type.GpImageAttributes],  # imageAttributes
                                     _type.DrawImageAbort,  # callback
                                     _Optional[_Pointer[_type.VOID]]],  # callbackData
                                    _enum.GpStatus]
GdipEnumerateMetafileDestPoint: _Callable[[_type.GpGraphics,  # graphics
                                           _type.GpMetafile,  # metafile
                                           _Pointer[_struct.PointF],  # destPoint
                                           _type.EnumerateMetafileProc,  # callback
                                           _Pointer[_type.VOID],  # callbackData
                                           _type.GpImageAttributes],  # imageAttributes
                                          _enum.GpStatus]
GdipEnumerateMetafileDestPointI: _Callable[[_type.GpGraphics,  # graphics
                                            _type.GpMetafile,  # metafile
                                            _Pointer[_struct.Point],  # destPoint
                                            _type.EnumerateMetafileProc,  # callback
                                            _Pointer[_type.VOID],  # callbackData
                                            _type.GpImageAttributes],  # imageAttributes
                                           _enum.GpStatus]
GdipEnumerateMetafileDestRect: _Callable[[_type.GpGraphics,  # graphics
                                          _type.GpMetafile,  # metafile
                                          _Pointer[_struct.RectF],  # destRect
                                          _type.EnumerateMetafileProc,  # callback
                                          _Pointer[_type.VOID],  # callbackData
                                          _type.GpImageAttributes],  # imageAttributes
                                         _enum.GpStatus]
GdipEnumerateMetafileDestRectI: _Callable[[_type.GpGraphics,  # graphics
                                           _type.GpMetafile,  # metafile
                                           _Pointer[_struct.Rect],  # destRect
                                           _type.EnumerateMetafileProc,  # callback
                                           _Pointer[_type.VOID],  # callbackData
                                           _type.GpImageAttributes],  # imageAttributes
                                          _enum.GpStatus]
GdipEnumerateMetafileDestPoints: _Callable[[_type.GpGraphics,  # graphics
                                            _type.GpMetafile,  # metafile
                                            _Pointer[_struct.PointF],  # destPoints
                                            _type.INT,  # count
                                            _type.EnumerateMetafileProc,  # callback
                                            _Pointer[_type.VOID],  # callbackData
                                            _type.GpImageAttributes],  # imageAttributes
                                           _enum.GpStatus]
GdipEnumerateMetafileDestPointsI: _Callable[[_type.GpGraphics,  # graphics
                                             _type.GpMetafile,  # metafile
                                             _Pointer[_struct.Point],  # destPoints
                                             _type.INT,  # count
                                             _type.EnumerateMetafileProc,  # callback
                                             _Pointer[_type.VOID],  # callbackData
                                             _type.GpImageAttributes],  # imageAttributes
                                            _enum.GpStatus]
GdipEnumerateMetafileSrcRectDestPoint: _Callable[[_type.GpGraphics,  # graphics
                                                  _type.GpMetafile,  # metafile
                                                  _Pointer[_struct.PointF],  # destPoint
                                                  _Pointer[_struct.RectF],  # srcRect
                                                  _enum.Unit,  # srcUnit
                                                  _type.EnumerateMetafileProc,  # callback
                                                  _Pointer[_type.VOID],  # callbackData
                                                  _type.GpImageAttributes],  # imageAttributes
                                                 _enum.GpStatus]
GdipEnumerateMetafileSrcRectDestPointI: _Callable[[_type.GpGraphics,  # graphics
                                                   _type.GpMetafile,  # metafile
                                                   _Pointer[_struct.Point],  # destPoint
                                                   _Pointer[_struct.Rect],  # srcRect
                                                   _enum.Unit,  # srcUnit
                                                   _type.EnumerateMetafileProc,  # callback
                                                   _Pointer[_type.VOID],  # callbackData
                                                   _type.GpImageAttributes],  # imageAttributes
                                                  _enum.GpStatus]
GdipEnumerateMetafileSrcRectDestRect: _Callable[[_type.GpGraphics,  # graphics
                                                 _type.GpMetafile,  # metafile
                                                 _Pointer[_struct.RectF],  # destRect
                                                 _Pointer[_struct.RectF],  # srcRect
                                                 _enum.Unit,  # srcUnit
                                                 _type.EnumerateMetafileProc,  # callback
                                                 _Pointer[_type.VOID],  # callbackData
                                                 _type.GpImageAttributes],  # imageAttributes
                                                _enum.GpStatus]
GdipEnumerateMetafileSrcRectDestRectI: _Callable[[_type.GpGraphics,  # graphics
                                                  _type.GpMetafile,  # metafile
                                                  _Pointer[_struct.Rect],  # destRect
                                                  _Pointer[_struct.Rect],  # srcRect
                                                  _enum.Unit,  # srcUnit
                                                  _type.EnumerateMetafileProc,  # callback
                                                  _Pointer[_type.VOID],  # callbackData
                                                  _type.GpImageAttributes],  # imageAttributes
                                                 _enum.GpStatus]
GdipEnumerateMetafileSrcRectDestPoints: _Callable[[_type.GpGraphics,  # graphics
                                                   _type.GpMetafile,  # metafile
                                                   _Pointer[_struct.PointF],  # destPoints
                                                   _type.INT,  # count
                                                   _Pointer[_struct.RectF],  # srcRect
                                                   _enum.Unit,  # srcUnit
                                                   _type.EnumerateMetafileProc,  # callback
                                                   _Pointer[_type.VOID],  # callbackData
                                                   _type.GpImageAttributes],  # imageAttributes
                                                  _enum.GpStatus]
GdipEnumerateMetafileSrcRectDestPointsI: _Callable[[_type.GpGraphics,  # graphics
                                                    _type.GpMetafile,  # metafile
                                                    _Pointer[_struct.Point],  # destPoints
                                                    _type.INT,  # count
                                                    _Pointer[_struct.Rect],  # srcRect
                                                    _enum.Unit,  # srcUnit
                                                    _type.EnumerateMetafileProc,  # callback
                                                    _Pointer[_type.VOID],  # callbackData
                                                    _type.GpImageAttributes],  # imageAttributes
                                                   _enum.GpStatus]
GdipPlayMetafileRecord: _Callable[[_type.GpMetafile,  # metafile
                                   _enum.EmfPlusRecordType,  # recordType
                                   _type.UINT,  # flags
                                   _type.UINT,  # dataSize
                                   _Pointer[_type.BYTE]],  # data
                                  _enum.GpStatus]
GdipSetClipGraphics: _Callable[[_type.GpGraphics,  # graphics
                                _type.GpGraphics,  # srcgraphics
                                _enum.CombineMode],  # combineMode
                               _enum.GpStatus]
GdipSetClipRect: _Callable[[_type.GpGraphics,  # graphics
                            _type.REAL,  # x
                            _type.REAL,  # y
                            _type.REAL,  # width
                            _type.REAL,  # height
                            _enum.CombineMode],  # combineMode
                           _enum.GpStatus]
GdipSetClipRectI: _Callable[[_type.GpGraphics,  # graphics
                             _type.INT,  # x
                             _type.INT,  # y
                             _type.INT,  # width
                             _type.INT,  # height
                             _enum.CombineMode],  # combineMode
                            _enum.GpStatus]
GdipSetClipPath: _Callable[[_type.GpGraphics,  # graphics
                            _type.GpPath,  # path
                            _enum.CombineMode],  # combineMode
                           _enum.GpStatus]
GdipSetClipRegion: _Callable[[_type.GpGraphics,  # graphics
                              _type.GpRegion,  # region
                              _enum.CombineMode],  # combineMode
                             _enum.GpStatus]
GdipSetClipHrgn: _Callable[[_type.GpGraphics,  # graphics
                            _type.HRGN,  # hRgn
                            _enum.CombineMode],  # combineMode
                           _enum.GpStatus]
GdipResetClip: _Callable[[_type.GpGraphics],  # graphics
                         _enum.GpStatus]
GdipTranslateClip: _Callable[[_type.GpGraphics,  # graphics
                              _type.REAL,  # dx
                              _type.REAL],  # dy
                             _enum.GpStatus]
GdipTranslateClipI: _Callable[[_type.GpGraphics,  # graphics
                               _type.INT,  # dx
                               _type.INT],  # dy
                              _enum.GpStatus]
GdipGetClip: _Callable[[_type.GpGraphics,  # graphics
                        _type.GpRegion],  # region
                       _enum.GpStatus]
GdipGetClipBounds: _Callable[[_type.GpGraphics,  # graphics
                              _Pointer[_struct.GpRectF]],  # rect
                             _enum.GpStatus]
GdipGetClipBoundsI: _Callable[[_type.GpGraphics,  # graphics
                               _Pointer[_struct.GpRect]],  # rect
                              _enum.GpStatus]
GdipIsClipEmpty: _Callable[[_type.GpGraphics,  # graphics
                            _Pointer[_type.BOOL]],  # result
                           _enum.GpStatus]
GdipGetVisibleClipBounds: _Callable[[_type.GpGraphics,  # graphics
                                     _Pointer[_struct.GpRectF]],  # rect
                                    _enum.GpStatus]
GdipGetVisibleClipBoundsI: _Callable[[_type.GpGraphics,  # graphics
                                      _Pointer[_struct.GpRect]],  # rect
                                     _enum.GpStatus]
GdipIsVisibleClipEmpty: _Callable[[_type.GpGraphics,  # graphics
                                   _Pointer[_type.BOOL]],  # result
                                  _enum.GpStatus]
GdipIsVisiblePoint: _Callable[[_type.GpGraphics,  # graphics
                               _type.REAL,  # x
                               _type.REAL,  # y
                               _Pointer[_type.BOOL]],  # result
                              _enum.GpStatus]
GdipIsVisiblePointI: _Callable[[_type.GpGraphics,  # graphics
                                _type.INT,  # x
                                _type.INT,  # y
                                _Pointer[_type.BOOL]],  # result
                               _enum.GpStatus]
GdipIsVisibleRect: _Callable[[_type.GpGraphics,  # graphics
                              _type.REAL,  # x
                              _type.REAL,  # y
                              _type.REAL,  # width
                              _type.REAL,  # height
                              _Pointer[_type.BOOL]],  # result
                             _enum.GpStatus]
GdipIsVisibleRectI: _Callable[[_type.GpGraphics,  # graphics
                               _type.INT,  # x
                               _type.INT,  # y
                               _type.INT,  # width
                               _type.INT,  # height
                               _Pointer[_type.BOOL]],  # result
                              _enum.GpStatus]
GdipSaveGraphics: _Callable[[_type.GpGraphics,  # graphics
                             _Pointer[_type.GraphicsState]],  # state
                            _enum.GpStatus]
GdipRestoreGraphics: _Callable[[_type.GpGraphics,  # graphics
                                _type.GraphicsState],  # state
                               _enum.GpStatus]
GdipBeginContainer: _Callable[[_type.GpGraphics,  # graphics
                               _Pointer[_struct.GpRectF],  # dstrect
                               _Pointer[_struct.GpRectF],  # srcrect
                               _enum.GpUnit,  # unit
                               _Pointer[_type.GraphicsContainer]],  # state
                              _enum.GpStatus]
GdipBeginContainerI: _Callable[[_type.GpGraphics,  # graphics
                                _Pointer[_struct.GpRect],  # dstrect
                                _Pointer[_struct.GpRect],  # srcrect
                                _enum.GpUnit,  # unit
                                _Pointer[_type.GraphicsContainer]],  # state
                               _enum.GpStatus]
GdipBeginContainer2: _Callable[[_type.GpGraphics,  # graphics
                                _Pointer[_type.GraphicsContainer]],  # state
                               _enum.GpStatus]
GdipEndContainer: _Callable[[_type.GpGraphics,  # graphics
                             _type.GraphicsContainer],  # state
                            _enum.GpStatus]
GdipCreateStreamOnFile: _Callable[[_type.LPWSTR,  # filename
                                   _type.UINT,  # access
                                   _Pointer[_objidlbase.IStream]],  # stream
                                  _enum.GpStatus]
GdipCreateMetafileFromWmf: _Callable[[_type.HMETAFILE,  # hWmf
                                      _type.BOOL,  # deleteWmf
                                      _Pointer[_struct.WmfPlaceableFileHeader],  # wmfPlaceableFileHeader
                                      _Pointer[_type.GpMetafile]],  # metafile
                                     _enum.GpStatus]
GdipCreateMetafileFromEmf: _Callable[[_type.HENHMETAFILE,  # hEmf
                                      _type.BOOL,  # deleteEmf
                                      _Pointer[_type.GpMetafile]],  # metafile
                                     _enum.GpStatus]
GdipCreateMetafileFromFile: _Callable[[_type.LPWSTR,  # file
                                       _Pointer[_type.GpMetafile]],  # metafile
                                      _enum.GpStatus]
GdipCreateMetafileFromWmfFile: _Callable[[_type.LPWSTR,  # file
                                          _Pointer[_struct.WmfPlaceableFileHeader],  # wmfPlaceableFileHeader
                                          _Pointer[_type.GpMetafile]],  # metafile
                                         _enum.GpStatus]
GdipCreateMetafileFromStream: _Callable[[_objidlbase.IStream,  # stream
                                         _Pointer[_type.GpMetafile]],  # metafile
                                        _enum.GpStatus]
GdipRecordMetafile: _Callable[[_type.HDC,  # referenceHdc
                               _enum.EmfType,  # type
                               _Pointer[_struct.GpRectF],  # frameRect
                               _enum.MetafileFrameUnit,  # frameUnit
                               _type.LPWSTR,  # description
                               _Pointer[_type.GpMetafile]],  # metafile
                              _enum.GpStatus]
GdipRecordMetafileI: _Callable[[_type.HDC,  # referenceHdc
                                _enum.EmfType,  # type
                                _Pointer[_struct.GpRect],  # frameRect
                                _enum.MetafileFrameUnit,  # frameUnit
                                _type.LPWSTR,  # description
                                _Pointer[_type.GpMetafile]],  # metafile
                               _enum.GpStatus]
GdipRecordMetafileFileName: _Callable[[_type.LPWSTR,  # fileName
                                       _type.HDC,  # referenceHdc
                                       _enum.EmfType,  # type
                                       _Pointer[_struct.GpRectF],  # frameRect
                                       _enum.MetafileFrameUnit,  # frameUnit
                                       _type.LPWSTR,  # description
                                       _Pointer[_type.GpMetafile]],  # metafile
                                      _enum.GpStatus]
GdipRecordMetafileFileNameI: _Callable[[_type.LPWSTR,  # fileName
                                        _type.HDC,  # referenceHdc
                                        _enum.EmfType,  # type
                                        _Pointer[_struct.GpRect],  # frameRect
                                        _enum.MetafileFrameUnit,  # frameUnit
                                        _type.LPWSTR,  # description
                                        _Pointer[_type.GpMetafile]],  # metafile
                                       _enum.GpStatus]
GdipRecordMetafileStream: _Callable[[_objidlbase.IStream,  # stream
                                     _type.HDC,  # referenceHdc
                                     _enum.EmfType,  # type
                                     _Pointer[_struct.GpRectF],  # frameRect
                                     _enum.MetafileFrameUnit,  # frameUnit
                                     _type.LPWSTR,  # description
                                     _Pointer[_type.GpMetafile]],  # metafile
                                    _enum.GpStatus]
GdipRecordMetafileStreamI: _Callable[[_objidlbase.IStream,  # stream
                                      _type.HDC,  # referenceHdc
                                      _enum.EmfType,  # type
                                      _Pointer[_struct.GpRect],  # frameRect
                                      _enum.MetafileFrameUnit,  # frameUnit
                                      _type.LPWSTR,  # description
                                      _Pointer[_type.GpMetafile]],  # metafile
                                     _enum.GpStatus]
GdipSetMetafileDownLevelRasterizationLimit: _Callable[[_type.GpMetafile,  # metafile
                                                       _type.UINT],  # metafileRasterizationLimitDpi
                                                      _enum.GpStatus]
GdipGetMetafileDownLevelRasterizationLimit: _Callable[[_type.GpMetafile,  # metafile
                                                       _Pointer[_type.UINT]],  # metafileRasterizationLimitDpi
                                                      _enum.GpStatus]
GdipGetImageDecodersSize: _Callable[[_Pointer[_type.UINT],  # numDecoders
                                     _Pointer[_type.UINT]],  # size
                                    _enum.GpStatus]
GdipGetImageDecoders: _Callable[[_type.UINT,  # numDecoders
                                 _type.UINT,  # size
                                 _Pointer[_struct.ImageCodecInfo]],  # decoders
                                _enum.GpStatus]
GdipGetImageEncodersSize: _Callable[[_Pointer[_type.UINT],  # numEncoders
                                     _Pointer[_type.UINT]],  # size
                                    _enum.GpStatus]
GdipGetImageEncoders: _Callable[[_type.UINT,  # numEncoders
                                 _type.UINT,  # size
                                 _Pointer[_struct.ImageCodecInfo]],  # encoders
                                _enum.GpStatus]
GdipComment: _Callable[[_type.GpGraphics,  # graphics
                        _type.UINT,  # sizeData
                        _Pointer[_type.BYTE]],  # data
                       _enum.GpStatus]
GdipCreateFontFamilyFromName: _Callable[[_type.LPWSTR,  # name
                                         _Optional[_type.GpFontCollection],  # fontCollection
                                         _Pointer[_type.GpFontFamily]],  # fontFamily
                                        _enum.GpStatus]
GdipDeleteFontFamily: _Callable[[_type.GpFontFamily],  # fontFamily
                                _enum.GpStatus]
GdipCloneFontFamily: _Callable[[_type.GpFontFamily,  # fontFamily
                                _Pointer[_type.GpFontFamily]],  # clonedFontFamily
                               _enum.GpStatus]
GdipGetGenericFontFamilySansSerif: _Callable[[_Pointer[_type.GpFontFamily]],  # nativeFamily
                                             _enum.GpStatus]
GdipGetGenericFontFamilySerif: _Callable[[_Pointer[_type.GpFontFamily]],  # nativeFamily
                                         _enum.GpStatus]
GdipGetGenericFontFamilyMonospace: _Callable[[_Pointer[_type.GpFontFamily]],  # nativeFamily
                                             _enum.GpStatus]
GdipGetFamilyName: _Callable[[_type.GpFontFamily,  # family
                              _type.LPWSTR,  # name
                              _type.LANGID],  # language
                             _enum.GpStatus]
GdipIsStyleAvailable: _Callable[[_type.GpFontFamily,  # family
                                 _type.INT,  # style
                                 _Pointer[_type.BOOL]],  # isStyleAvailable
                                _enum.GpStatus]
GdipFontCollectionEnumerable: _Callable[[_type.GpFontCollection,  # fontCollection
                                         _type.GpGraphics,  # graphics
                                         _Pointer[_type.INT]],  # numFound
                                        _enum.GpStatus]
GdipFontCollectionEnumerate: _Callable[[_type.GpFontCollection,  # fontCollection
                                        _type.INT,  # numSought
                                        _type.GpFontFamily,  # gpfamilies[]
                                        _Pointer[_type.INT],  # numFound
                                        _type.GpGraphics],  # graphics
                                       _enum.GpStatus]
GdipGetEmHeight: _Callable[[_type.GpFontFamily,  # family
                            _type.INT,  # style
                            _Pointer[_type.UINT16]],  # EmHeight
                           _enum.GpStatus]
GdipGetCellAscent: _Callable[[_type.GpFontFamily,  # family
                              _type.INT,  # style
                              _Pointer[_type.UINT16]],  # CellAscent
                             _enum.GpStatus]
GdipGetCellDescent: _Callable[[_type.GpFontFamily,  # family
                               _type.INT,  # style
                               _Pointer[_type.UINT16]],  # CellDescent
                              _enum.GpStatus]
GdipGetLineSpacing: _Callable[[_type.GpFontFamily,  # family
                               _type.INT,  # style
                               _Pointer[_type.UINT16]],  # LineSpacing
                              _enum.GpStatus]
GdipCreateFontFromDC: _Callable[[_type.HDC,  # hdc
                                 _Pointer[_type.GpFont]],  # font
                                _enum.GpStatus]
GdipCreateFontFromLogfontA: _Callable[[_type.HDC,  # hdc
                                       _Pointer[_struct.LOGFONTA],  # logfont
                                       _Pointer[_type.GpFont]],  # font
                                      _enum.GpStatus]
GdipCreateFontFromLogfontW: _Callable[[_type.HDC,  # hdc
                                       _Pointer[_struct.LOGFONTW],  # logfont
                                       _Pointer[_type.GpFont]],  # font
                                      _enum.GpStatus]
GdipCreateFont: _Callable[[_type.GpFontFamily,  # fontFamily
                           _type.REAL,  # emSize
                           _type.INT,  # style
                           _enum.Unit,  # unit
                           _Pointer[_type.GpFont]],  # font
                          _enum.GpStatus]
GdipCloneFont: _Callable[[_type.GpFont,  # font
                          _Pointer[_type.GpFont]],  # cloneFont
                         _enum.GpStatus]
GdipDeleteFont: _Callable[[_type.GpFont],  # font
                          _enum.GpStatus]
GdipGetFamily: _Callable[[_type.GpFont,  # font
                          _Pointer[_type.GpFontFamily]],  # family
                         _enum.GpStatus]
GdipGetFontStyle: _Callable[[_type.GpFont,  # font
                             _Pointer[_type.INT]],  # style
                            _enum.GpStatus]
GdipGetFontSize: _Callable[[_type.GpFont,  # font
                            _Pointer[_type.REAL]],  # size
                           _enum.GpStatus]
GdipGetFontUnit: _Callable[[_type.GpFont,  # font
                            _Pointer[_enum.Unit]],  # unit
                           _enum.GpStatus]
GdipGetFontHeight: _Callable[[_type.GpFont,  # font
                              _type.GpGraphics,  # graphics
                              _Pointer[_type.REAL]],  # height
                             _enum.GpStatus]
GdipGetFontHeightGivenDPI: _Callable[[_type.GpFont,  # font
                                      _type.REAL,  # dpi
                                      _Pointer[_type.REAL]],  # height
                                     _enum.GpStatus]
GdipGetLogFontA: _Callable[[_type.GpFont,  # font
                            _type.GpGraphics,  # graphics
                            _Pointer[_struct.LOGFONTA]],  # logfontA
                           _enum.GpStatus]
GdipGetLogFontW: _Callable[[_type.GpFont,  # font
                            _type.GpGraphics,  # graphics
                            _Pointer[_struct.LOGFONTW]],  # logfontW
                           _enum.GpStatus]
GdipNewInstalledFontCollection: _Callable[[_Pointer[_type.GpFontCollection]],  # fontCollection
                                          _enum.GpStatus]
GdipNewPrivateFontCollection: _Callable[[_Pointer[_type.GpFontCollection]],  # fontCollection
                                        _enum.GpStatus]
GdipDeletePrivateFontCollection: _Callable[[_Pointer[_type.GpFontCollection]],  # fontCollection
                                           _enum.GpStatus]
GdipGetFontCollectionFamilyCount: _Callable[[_type.GpFontCollection,  # fontCollection
                                             _Pointer[_type.INT]],  # numFound
                                            _enum.GpStatus]
GdipGetFontCollectionFamilyList: _Callable[[_type.GpFontCollection,  # fontCollection
                                            _type.INT,  # numSought
                                            _type.GpFontFamily,  # gpfamilies
                                            _Pointer[_type.INT]],  # numFound
                                           _enum.GpStatus]
GdipPrivateAddFontFile: _Callable[[_type.GpFontCollection,  # fontCollection
                                   _type.LPWSTR],  # filename
                                  _enum.GpStatus]
GdipPrivateAddMemoryFont: _Callable[[_type.GpFontCollection,  # fontCollection
                                     _type.c_void_p,  # memory
                                     _type.INT],  # length
                                    _enum.GpStatus]
GdipDrawString: _Callable[[_type.GpGraphics,  # graphics
                           _type.LPWSTR,  # string
                           _type.INT,  # length
                           _type.GpFont,  # font
                           _Pointer[_struct.RectF],  # layoutRect
                           _Optional[_type.GpStringFormat],  # stringFormat
                           _type.GpBrush],  # brush
                          _enum.GpStatus]
GdipMeasureString: _Callable[[_type.GpGraphics,  # graphics
                              _type.LPWSTR,  # string
                              _type.INT,  # length
                              _type.GpFont,  # font
                              _Pointer[_struct.RectF],  # layoutRect
                              _Optional[_type.GpStringFormat],  # stringFormat
                              _Pointer[_struct.RectF],  # boundingBox
                              _Optional[_Pointer[_type.INT]],  # codepointsFitted
                              _Optional[_Pointer[_type.INT]]],  # linesFilled
                             _enum.GpStatus]
GdipMeasureCharacterRanges: _Callable[[_type.GpGraphics,  # graphics
                                       _type.LPWSTR,  # string
                                       _type.INT,  # length
                                       _type.GpFont,  # font
                                       _Pointer[_struct.RectF],  # layoutRect
                                       _type.GpStringFormat,  # stringFormat
                                       _type.INT,  # regionCount
                                       _Pointer[_type.GpRegion]],  # regions
                                      _enum.GpStatus]
GdipDrawDriverString: _Callable[[_type.GpGraphics,  # graphics
                                 _Pointer[_type.UINT16],  # text
                                 _type.INT,  # length
                                 _type.GpFont,  # font
                                 _type.GpBrush,  # brush
                                 _Pointer[_struct.PointF],  # positions
                                 _type.INT,  # flags
                                 _type.GpMatrix],  # matrix
                                _enum.GpStatus]
GdipMeasureDriverString: _Callable[[_type.GpGraphics,  # graphics
                                    _Pointer[_type.UINT16],  # text
                                    _type.INT,  # length
                                    _type.GpFont,  # font
                                    _Pointer[_struct.PointF],  # positions
                                    _type.INT,  # flags
                                    _type.GpMatrix,  # matrix
                                    _Pointer[_struct.RectF]],  # boundingBox
                                   _enum.GpStatus]
GdipCreateStringFormat: _Callable[[_type.INT,  # formatAttributes
                                   _type.LANGID,  # language
                                   _Pointer[_type.GpStringFormat]],  # format
                                  _enum.GpStatus]
GdipStringFormatGetGenericDefault: _Callable[[_Pointer[_type.GpStringFormat]],  # format
                                             _enum.GpStatus]
GdipStringFormatGetGenericTypographic: _Callable[[_Pointer[_type.GpStringFormat]],  # format
                                                 _enum.GpStatus]
GdipDeleteStringFormat: _Callable[[_type.GpStringFormat],  # format
                                  _enum.GpStatus]
GdipCloneStringFormat: _Callable[[_type.GpStringFormat,  # format
                                  _Pointer[_type.GpStringFormat]],  # newFormat
                                 _enum.GpStatus]
GdipSetStringFormatFlags: _Callable[[_type.GpStringFormat,  # format
                                     _type.INT],  # flags
                                    _enum.GpStatus]
GdipGetStringFormatFlags: _Callable[[_type.GpStringFormat,  # format
                                     _Pointer[_type.INT]],  # flags
                                    _enum.GpStatus]
GdipSetStringFormatAlign: _Callable[[_type.GpStringFormat,  # format
                                     _enum.StringAlignment],  # align
                                    _enum.GpStatus]
GdipGetStringFormatAlign: _Callable[[_type.GpStringFormat,  # format
                                     _Pointer[_enum.StringAlignment]],  # align
                                    _enum.GpStatus]
GdipSetStringFormatLineAlign: _Callable[[_type.GpStringFormat,  # format
                                         _enum.StringAlignment],  # align
                                        _enum.GpStatus]
GdipGetStringFormatLineAlign: _Callable[[_type.GpStringFormat,  # format
                                         _Pointer[_enum.StringAlignment]],  # align
                                        _enum.GpStatus]
GdipSetStringFormatTrimming: _Callable[[_type.GpStringFormat,  # format
                                        _enum.StringTrimming],  # trimming
                                       _enum.GpStatus]
GdipGetStringFormatTrimming: _Callable[[_type.GpStringFormat,  # format
                                        _Pointer[_enum.StringTrimming]],  # trimming
                                       _enum.GpStatus]
GdipSetStringFormatHotkeyPrefix: _Callable[[_type.GpStringFormat,  # format
                                            _type.INT],  # hotkeyPrefix
                                           _enum.GpStatus]
GdipGetStringFormatHotkeyPrefix: _Callable[[_type.GpStringFormat,  # format
                                            _Pointer[_type.INT]],  # hotkeyPrefix
                                           _enum.GpStatus]
GdipSetStringFormatTabStops: _Callable[[_type.GpStringFormat,  # format
                                        _type.REAL,  # firstTabOffset
                                        _type.INT,  # count
                                        _Pointer[_type.REAL]],  # tabStops
                                       _enum.GpStatus]
GdipGetStringFormatTabStops: _Callable[[_type.GpStringFormat,  # format
                                        _type.INT,  # count
                                        _Pointer[_type.REAL],  # firstTabOffset
                                        _Pointer[_type.REAL]],  # tabStops
                                       _enum.GpStatus]
GdipGetStringFormatTabStopCount: _Callable[[_type.GpStringFormat,  # format
                                            _Pointer[_type.INT]],  # count
                                           _enum.GpStatus]
GdipSetStringFormatDigitSubstitution: _Callable[[_type.GpStringFormat,  # format
                                                 _type.LANGID,  # language
                                                 _enum.StringDigitSubstitute],  # substitute
                                                _enum.GpStatus]
GdipGetStringFormatDigitSubstitution: _Callable[[_type.GpStringFormat,  # format
                                                 _Pointer[_type.LANGID],  # language
                                                 _Pointer[_enum.StringDigitSubstitute]],  # substitute
                                                _enum.GpStatus]
GdipGetStringFormatMeasurableCharacterRangeCount: _Callable[[_type.GpStringFormat,  # format
                                                             _Pointer[_type.INT]],  # count
                                                            _enum.GpStatus]
GdipSetStringFormatMeasurableCharacterRanges: _Callable[[_type.GpStringFormat,  # format
                                                         _type.INT,  # rangeCount
                                                         _Pointer[_struct.CharacterRange]],  # ranges
                                                        _enum.GpStatus]
GdipCreateCachedBitmap: _Callable[[_type.GpBitmap,  # bitmap
                                   _type.GpGraphics,  # graphics
                                   _Pointer[_type.GpCachedBitmap]],  # cachedBitmap
                                  _enum.GpStatus]
GdipDeleteCachedBitmap: _Callable[[_type.GpCachedBitmap],  # cachedBitmap
                                  _enum.GpStatus]
GdipDrawCachedBitmap: _Callable[[_type.GpGraphics,  # graphics
                                 _type.GpCachedBitmap,  # cachedBitmap
                                 _type.INT,  # x
                                 _type.INT],  # y
                                _enum.GpStatus]
GdipEmfToWmfBits: _Callable[[_type.HENHMETAFILE,  # hemf
                             _type.UINT,  # cbData16
                             _Optional[_Pointer[_type.BYTE]],  # pData16
                             _type.INT,  # iMapMode
                             _type.INT],  # eFlags
                            _type.UINT]
GdipSetImageAttributesCachedBackground: _Callable[[_type.GpImageAttributes,  # imageattr
                                                   _type.BOOL],  # enableFlag
                                                  _enum.GpStatus]
GdipTestControl: _Callable[[_enum.GpTestControlEnum,  # control
                            _type.c_void_p],  # param
                           _enum.GpStatus]
GdiplusNotificationHook: _Callable[[_Pointer[_type.ULONG_PTR]],  # token
                                   _enum.GpStatus]
GdiplusNotificationUnhook: _Callable[[_type.ULONG_PTR],  # token
                                     _type.VOID]
GdipConvertToEmfPlus: _Callable[[_type.GpGraphics,  # refGraphics
                                 _type.GpMetafile,  # metafile
                                 _Pointer[_type.INT],  # conversionFailureFlag
                                 _enum.EmfType,  # emfType
                                 _type.LPWSTR,  # description
                                 _Pointer[_type.GpMetafile]],  # out_metafile
                                _enum.GpStatus]
GdipConvertToEmfPlusToFile: _Callable[[_type.GpGraphics,  # refGraphics
                                       _type.GpMetafile,  # metafile
                                       _Pointer[_type.INT],  # conversionFailureFlag
                                       _type.LPWSTR,  # filename
                                       _enum.EmfType,  # emfType
                                       _type.LPWSTR,  # description
                                       _Pointer[_type.GpMetafile]],  # out_metafile
                                      _enum.GpStatus]
GdipConvertToEmfPlusToStream: _Callable[[_type.GpGraphics,  # refGraphics
                                         _type.GpMetafile,  # metafile
                                         _Pointer[_type.INT],  # conversionFailureFlag
                                         _objidlbase.IStream,  # stream
                                         _enum.EmfType,  # emfType
                                         _type.LPWSTR,  # description
                                         _Pointer[_type.GpMetafile]],  # out_metafile
                                        _enum.GpStatus]
# gdiplusinit
GdiplusStartup: _Callable[[_Pointer[_type.ULONG_PTR],  # token
                           _Pointer[_struct.GdiplusStartupInput],  # input
                           _Optional[_Pointer[_struct.GdiplusStartupInput]]],  # output
                          _enum.Status]
GdiplusShutdown: _Callable[[_type.ULONG_PTR],  # token
                           _type.VOID]

_WinLib(__name__)
