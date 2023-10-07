from __future__ import annotations as _

from typing import Callable as _Callable

from . import d2d1 as _d2d1
from . import d2d1_1 as _d2d1_1
from . import objidlbase as _objidlbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID2D1SvgAttribute(_d2d1.ID2D1Resource):
    GetElement: _Callable[[_Pointer[ID2D1SvgElement]],  # element
                          _type.c_void]
    Clone: _Callable[[_Pointer[ID2D1SvgAttribute]],  # attribute
                     _type.HRESULT]


class ID2D1SvgPaint(ID2D1SvgAttribute):
    SetPaintType: _Callable[[_enum.D2D1_SVG_PAINT_TYPE],  # paintType
                            _type.HRESULT]
    GetPaintType: _Callable[[],
                            _enum.D2D1_SVG_PAINT_TYPE]
    SetColor: _Callable[[_Pointer[_struct.D2D1_COLOR_F]],  # color
                        _type.HRESULT]
    GetColor: _Callable[[_Pointer[_struct.D2D1_COLOR_F]],  # color
                        _type.c_void]
    SetId: _Callable[[_type.PCWSTR],  # id
                     _type.HRESULT]
    GetId: _Callable[[_type.PWSTR,  # id
                      _type.UINT32],  # idCount
                     _type.HRESULT]
    GetIdLength: _Callable[[],
                           _type.UINT32]


class ID2D1SvgStrokeDashArray(ID2D1SvgAttribute):
    RemoveDashesAtEnd: _Callable[[_type.UINT32],  # dashesCount
                                 _type.HRESULT]
    UpdateDashes: _Callable[[_Pointer[_struct.D2D1_SVG_LENGTH],  # dashes
                             _type.UINT32,  # dashesCount
                             _type.UINT32],  # startIndex
                            _type.HRESULT]
    GetDashes: _Callable[[_Pointer[_struct.D2D1_SVG_LENGTH],  # dashes
                          _type.UINT32,  # dashesCount
                          _type.UINT32],  # startIndex
                         _type.HRESULT]
    GetDashesCount: _Callable[[],
                              _type.UINT32]


class ID2D1SvgPointCollection(ID2D1SvgAttribute):
    RemovePointsAtEnd: _Callable[[_type.UINT32],  # pointsCount
                                 _type.HRESULT]
    UpdatePoints: _Callable[[_Pointer[_struct.D2D1_POINT_2F],  # points
                             _type.UINT32,  # pointsCount
                             _type.UINT32],  # startIndex
                            _type.HRESULT]
    GetPoints: _Callable[[_Pointer[_struct.D2D1_POINT_2F],  # points
                          _type.UINT32,  # pointsCount
                          _type.UINT32],  # startIndex
                         _type.HRESULT]
    GetPointsCount: _Callable[[],
                              _type.UINT32]


class ID2D1SvgPathData(ID2D1SvgAttribute):
    RemoveSegmentDataAtEnd: _Callable[[_type.UINT32],  # dataCount
                                      _type.HRESULT]
    UpdateSegmentData: _Callable[[_Pointer[_type.FLOAT],  # data
                                  _type.UINT32,  # dataCount
                                  _type.UINT32],  # startIndex
                                 _type.HRESULT]
    GetSegmentData: _Callable[[_Pointer[_type.FLOAT],  # data
                               _type.UINT32,  # dataCount
                               _type.UINT32],  # startIndex
                              _type.HRESULT]
    GetSegmentDataCount: _Callable[[],
                                   _type.UINT32]
    RemoveCommandsAtEnd: _Callable[[_type.UINT32],  # commandsCount
                                   _type.HRESULT]
    UpdateCommands: _Callable[[_Pointer[_enum.D2D1_SVG_PATH_COMMAND],  # commands
                               _type.UINT32,  # commandsCount
                               _type.UINT32],  # startIndex
                              _type.HRESULT]
    GetCommands: _Callable[[_Pointer[_enum.D2D1_SVG_PATH_COMMAND],  # commands
                            _type.UINT32,  # commandsCount
                            _type.UINT32],  # startIndex
                           _type.HRESULT]
    GetCommandsCount: _Callable[[],
                                _type.UINT32]
    CreatePathGeometry: _Callable[[_enum.D2D1_FILL_MODE,  # fillMode
                                   _Pointer[_d2d1_1.ID2D1PathGeometry1]],  # pathGeometry
                                  _type.HRESULT]


class ID2D1SvgElement(_d2d1.ID2D1Resource):
    GetDocument: _Callable[[_Pointer[ID2D1SvgDocument]],  # document
                           _type.c_void]
    GetTagName: _Callable[[_type.PWSTR,  # name
                           _type.UINT32],  # nameCount
                          _type.HRESULT]
    GetTagNameLength: _Callable[[],
                                _type.UINT32]
    IsTextContent: _Callable[[],
                             _type.BOOL]
    GetParent: _Callable[[_Pointer[ID2D1SvgElement]],  # parent
                         _type.c_void]
    HasChildren: _Callable[[],
                           _type.BOOL]
    GetFirstChild: _Callable[[_Pointer[ID2D1SvgElement]],  # child
                             _type.c_void]
    GetLastChild: _Callable[[_Pointer[ID2D1SvgElement]],  # child
                            _type.c_void]
    GetPreviousChild: _Callable[[ID2D1SvgElement,  # referenceChild
                                 _Pointer[ID2D1SvgElement]],  # previousChild
                                _type.HRESULT]
    GetNextChild: _Callable[[ID2D1SvgElement,  # referenceChild
                             _Pointer[ID2D1SvgElement]],  # nextChild
                            _type.HRESULT]
    InsertChildBefore: _Callable[[ID2D1SvgElement,  # newChild
                                  ID2D1SvgElement],  # referenceChild
                                 _type.HRESULT]
    AppendChild: _Callable[[ID2D1SvgElement],  # newChild
                           _type.HRESULT]
    ReplaceChild: _Callable[[ID2D1SvgElement,  # newChild
                             ID2D1SvgElement],  # oldChild
                            _type.HRESULT]
    RemoveChild: _Callable[[ID2D1SvgElement],  # oldChild
                           _type.HRESULT]
    CreateChild: _Callable[[_type.PCWSTR,  # tagName
                            _Pointer[ID2D1SvgElement]],  # newChild
                           _type.HRESULT]
    IsAttributeSpecified: _Callable[[_type.PCWSTR,  # name
                                     _Pointer[_type.BOOL]],  # inherited
                                    _type.BOOL]
    GetSpecifiedAttributeCount: _Callable[[],
                                          _type.UINT32]
    GetSpecifiedAttributeName: _Callable[[_type.UINT32,  # index
                                          _type.PWSTR,  # name
                                          _type.UINT32,  # nameCount
                                          _Pointer[_type.BOOL]],  # inherited
                                         _type.HRESULT]
    GetSpecifiedAttributeNameLength: _Callable[[_type.UINT32,  # index
                                                _Pointer[_type.UINT32],  # nameLength
                                                _Pointer[_type.BOOL]],  # inherited
                                               _type.HRESULT]
    RemoveAttribute: _Callable[[_type.PCWSTR],  # name
                               _type.HRESULT]
    SetTextValue: _Callable[[_type.LPWSTR,  # name
                             _type.UINT32],  # nameCount
                            _type.HRESULT]
    GetTextValue: _Callable[[_type.PWSTR,  # name
                             _type.UINT32],  # nameCount
                            _type.HRESULT]
    GetTextValueLength: _Callable[[],
                                  _type.UINT32]
    SetAttributeValue: _Callable[[_type.PCWSTR,  # name
                                  ID2D1SvgAttribute],  # value
                                 _type.HRESULT]
    SetAttributeValue_: _Callable[[_type.PCWSTR,  # name
                                   _enum.D2D1_SVG_ATTRIBUTE_POD_TYPE,  # type
                                   _type.c_void_p,  # value
                                   _type.UINT32],  # valueSizeInBytes
                                  _type.HRESULT]
    SetAttributeValue__: _Callable[[_type.PCWSTR,  # name
                                    _enum.D2D1_SVG_ATTRIBUTE_STRING_TYPE,  # type
                                    _type.PCWSTR],  # value
                                   _type.HRESULT]
    GetAttributeValue: _Callable[[_type.PCWSTR,  # name
                                  _Pointer[_struct.IID],  # riid
                                  _type.c_void_p],  # value
                                 _type.HRESULT]
    GetAttributeValue_: _Callable[[_type.PCWSTR,  # name
                                   _enum.D2D1_SVG_ATTRIBUTE_POD_TYPE,  # type
                                   _type.c_void_p,  # value
                                   _type.UINT32],  # valueSizeInBytes
                                  _type.HRESULT]
    GetAttributeValue__: _Callable[[_type.PCWSTR,  # name
                                    _enum.D2D1_SVG_ATTRIBUTE_STRING_TYPE,  # type
                                    _type.PWSTR,  # value
                                    _type.UINT32],  # valueCount
                                   _type.HRESULT]
    GetAttributeValueLength: _Callable[[_type.PCWSTR,  # name
                                        _enum.D2D1_SVG_ATTRIBUTE_STRING_TYPE,  # type
                                        _Pointer[_type.UINT32]],  # valueLength
                                       _type.HRESULT]


class ID2D1SvgDocument(_d2d1.ID2D1Resource):
    SetViewportSize: _Callable[[_struct.D2D1_SIZE_F],  # viewportSize
                               _type.HRESULT]
    GetViewportSize: _Callable[[],
                               _struct.D2D1_SIZE_F]
    SetRoot: _Callable[[ID2D1SvgElement],  # root
                       _type.HRESULT]
    GetRoot: _Callable[[_Pointer[ID2D1SvgElement]],  # root
                       _type.c_void]
    FindElementById: _Callable[[_type.PCWSTR,  # id
                                _Pointer[ID2D1SvgElement]],  # svgElement
                               _type.HRESULT]
    Serialize: _Callable[[_objidlbase.IStream,  # outputXmlStream
                          ID2D1SvgElement],  # subtree
                         _type.HRESULT]
    Deserialize: _Callable[[_objidlbase.IStream,  # inputXmlStream
                            _Pointer[ID2D1SvgElement]],  # subtree
                           _type.HRESULT]
    CreatePaint: _Callable[[_enum.D2D1_SVG_PAINT_TYPE,  # paintType
                            _Pointer[_struct.D2D1_COLOR_F],  # color
                            _type.PCWSTR,  # id
                            _Pointer[ID2D1SvgPaint]],  # paint
                           _type.HRESULT]
    CreateStrokeDashArray: _Callable[[_Pointer[_struct.D2D1_SVG_LENGTH],  # dashes
                                      _type.UINT32,  # dashesCount
                                      _Pointer[ID2D1SvgStrokeDashArray]],  # strokeDashArray
                                     _type.HRESULT]
    CreatePointCollection: _Callable[[_Pointer[_struct.D2D1_POINT_2F],  # points
                                      _type.UINT32,  # pointsCount
                                      _Pointer[ID2D1SvgPointCollection]],  # pointCollection
                                     _type.HRESULT]
    CreatePathData: _Callable[[_Pointer[_type.FLOAT],  # segmentData
                               _type.UINT32,  # segmentDataCount
                               _Pointer[_enum.D2D1_SVG_PATH_COMMAND],  # commands
                               _type.UINT32,  # commandsCount
                               _Pointer[ID2D1SvgPathData]],  # pathData
                              _type.HRESULT]
