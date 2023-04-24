from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from . import d2d1_1 as _d2d1_1
from . import wincodec as _wincodec
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID2D1VertexBuffer(_Unknwnbase.IUnknown):
    Map: _Callable[[_Pointer[_Pointer[_type.BYTE]],  # data
                    _type.UINT32],  # bufferSize
                   _type.HRESULT]
    Unmap: _Callable[[],
                     _type.HRESULT]


class ID2D1ResourceTexture(_Unknwnbase.IUnknown):
    Update: _Callable[[_Pointer[_type.UINT32],  # minimumExtents
                       _Pointer[_type.UINT32],  # maximimumExtents
                       _Pointer[_type.UINT32],  # strides
                       _type.UINT32,  # dimensions
                       _Pointer[_type.BYTE],  # data
                       _type.UINT32],  # dataCount
                      _type.HRESULT]


class ID2D1RenderInfo(_Unknwnbase.IUnknown):
    SetInputDescription: _Callable[[_type.UINT32,  # inputIndex
                                    _struct.D2D1_INPUT_DESCRIPTION],  # inputDescription
                                   _type.HRESULT]
    SetOutputBuffer: _Callable[[_enum.D2D1_BUFFER_PRECISION,  # bufferPrecision
                                _enum.D2D1_CHANNEL_DEPTH],  # channelDepth
                               _type.HRESULT]
    SetCached: _Callable[[_type.BOOL],  # isCached
                         _type.c_void]
    SetInstructionCountHint: _Callable[[_type.UINT32],  # instructionCount
                                       _type.c_void]


class ID2D1DrawInfo(ID2D1RenderInfo):
    SetPixelShaderConstantBuffer: _Callable[[_Pointer[_type.BYTE],  # buffer
                                             _type.UINT32],  # bufferCount
                                            _type.HRESULT]
    SetResourceTexture: _Callable[[_type.UINT32,  # textureIndex
                                   ID2D1ResourceTexture],  # resourceTexture
                                  _type.HRESULT]
    SetVertexShaderConstantBuffer: _Callable[[_Pointer[_type.BYTE],  # buffer
                                              _type.UINT32],  # bufferCount
                                             _type.HRESULT]
    SetPixelShader: _Callable[[_Pointer[_struct.GUID],  # shaderId
                               _enum.D2D1_PIXEL_OPTIONS],  # pixelOptions
                              _type.HRESULT]
    SetVertexProcessing: _Callable[[ID2D1VertexBuffer,  # vertexBuffer
                                    _enum.D2D1_VERTEX_OPTIONS,  # vertexOptions
                                    _Pointer[_struct.D2D1_BLEND_DESCRIPTION],  # blendDescription
                                    _Pointer[_struct.D2D1_VERTEX_RANGE],  # vertexRange
                                    _Pointer[_struct.GUID]],  # vertexShader
                                   _type.HRESULT]


class ID2D1ComputeInfo(ID2D1RenderInfo):
    SetComputeShaderConstantBuffer: _Callable[[_Pointer[_type.BYTE],  # buffer
                                               _type.UINT32],  # bufferCount
                                              _type.HRESULT]
    SetComputeShader: _Callable[[_Pointer[_struct.GUID]],  # shaderId
                                _type.HRESULT]
    SetResourceTexture: _Callable[[_type.UINT32,  # textureIndex
                                   ID2D1ResourceTexture],  # resourceTexture
                                  _type.HRESULT]


class ID2D1TransformNode(_Unknwnbase.IUnknown):
    GetInputCount: _Callable[[],
                             _type.UINT32]


class ID2D1TransformGraph(_Unknwnbase.IUnknown):
    GetInputCount: _Callable[[],
                             _type.UINT32]
    SetSingleTransformNode: _Callable[[ID2D1TransformNode],  # node
                                      _type.HRESULT]
    AddNode: _Callable[[ID2D1TransformNode],  # node
                       _type.HRESULT]
    RemoveNode: _Callable[[ID2D1TransformNode],  # node
                          _type.HRESULT]
    SetOutputNode: _Callable[[ID2D1TransformNode],  # node
                             _type.HRESULT]
    ConnectNode: _Callable[[ID2D1TransformNode,  # fromNode
                            ID2D1TransformNode,  # toNode
                            _type.UINT32],  # toNodeInputIndex
                           _type.HRESULT]
    ConnectToEffectInput: _Callable[[_type.UINT32,  # toEffectInputIndex
                                     ID2D1TransformNode,  # node
                                     _type.UINT32],  # toNodeInputIndex
                                    _type.HRESULT]
    Clear: _Callable[[],
                     _type.c_void]
    SetPassthroughGraph: _Callable[[_type.UINT32],  # effectInputIndex
                                   _type.HRESULT]


class ID2D1Transform(ID2D1TransformNode):
    MapOutputRectToInputRects: _Callable[[_Pointer[_struct.D2D1_RECT_L],  # outputRect
                                          _Pointer[_struct.D2D1_RECT_L],  # inputRects
                                          _type.UINT32],  # inputRectsCount
                                         _type.HRESULT]
    MapInputRectsToOutputRect: _Callable[[_Pointer[_struct.D2D1_RECT_L],  # inputRects
                                          _Pointer[_struct.D2D1_RECT_L],  # inputOpaqueSubRects
                                          _type.UINT32,  # inputRectCount
                                          _Pointer[_struct.D2D1_RECT_L],  # outputRect
                                          _Pointer[_struct.D2D1_RECT_L]],  # outputOpaqueSubRect
                                         _type.HRESULT]
    MapInvalidRect: _Callable[[_type.UINT32,  # inputIndex
                               _struct.D2D1_RECT_L,  # invalidInputRect
                               _Pointer[_struct.D2D1_RECT_L]],  # invalidOutputRect
                              _type.HRESULT]


class ID2D1DrawTransform(ID2D1Transform):
    SetDrawInfo: _Callable[[ID2D1DrawInfo],  # drawInfo
                           _type.HRESULT]


class ID2D1ComputeTransform(ID2D1Transform):
    SetComputeInfo: _Callable[[ID2D1ComputeInfo],  # computeInfo
                              _type.HRESULT]
    CalculateThreadgroups: _Callable[[_Pointer[_struct.D2D1_RECT_L],  # outputRect
                                      _Pointer[_type.UINT32],  # dimensionX
                                      _Pointer[_type.UINT32],  # dimensionY
                                      _Pointer[_type.UINT32]],  # dimensionZ
                                     _type.HRESULT]


class ID2D1AnalysisTransform(_Unknwnbase.IUnknown):
    ProcessAnalysisResults: _Callable[[_Pointer[_type.BYTE],  # analysisData
                                       _type.UINT32],  # analysisDataCount
                                      _type.HRESULT]


class ID2D1SourceTransform(ID2D1Transform):
    SetRenderInfo: _Callable[[ID2D1RenderInfo],  # renderInfo
                             _type.HRESULT]
    Draw: _Callable[[_d2d1_1.ID2D1Bitmap1,  # target
                     _Pointer[_struct.D2D1_RECT_L],  # drawRect
                     _struct.D2D1_POINT_2U],  # targetOrigin
                    _type.HRESULT]


class ID2D1ConcreteTransform(ID2D1TransformNode):
    SetOutputBuffer: _Callable[[_enum.D2D1_BUFFER_PRECISION,  # bufferPrecision
                                _enum.D2D1_CHANNEL_DEPTH],  # channelDepth
                               _type.HRESULT]
    SetCached: _Callable[[_type.BOOL],  # isCached
                         _type.c_void]


class ID2D1BlendTransform(ID2D1ConcreteTransform):
    SetDescription: _Callable[[_Pointer[_struct.D2D1_BLEND_DESCRIPTION]],  # description
                              _type.c_void]
    GetDescription: _Callable[[_Pointer[_struct.D2D1_BLEND_DESCRIPTION]],  # description
                              _type.c_void]


class ID2D1BorderTransform(ID2D1ConcreteTransform):
    SetExtendModeX: _Callable[[_enum.D2D1_EXTEND_MODE],  # extendMode
                              _type.c_void]
    SetExtendModeY: _Callable[[_enum.D2D1_EXTEND_MODE],  # extendMode
                              _type.c_void]
    GetExtendModeX: _Callable[[],
                              _enum.D2D1_EXTEND_MODE]
    GetExtendModeY: _Callable[[],
                              _enum.D2D1_EXTEND_MODE]


class ID2D1OffsetTransform(ID2D1TransformNode):
    SetOffset: _Callable[[_struct.D2D1_POINT_2L],  # offset
                         _type.c_void]
    GetOffset: _Callable[[],
                         _struct.D2D1_POINT_2L]


class ID2D1BoundsAdjustmentTransform(ID2D1TransformNode):
    SetOutputBounds: _Callable[[_Pointer[_struct.D2D1_RECT_L]],  # outputBounds
                               _type.c_void]
    GetOutputBounds: _Callable[[_Pointer[_struct.D2D1_RECT_L]],  # outputBounds
                               _type.c_void]


class ID2D1EffectImpl(_Unknwnbase.IUnknown):
    Initialize: _Callable[[ID2D1EffectContext,  # effectContext
                           ID2D1TransformGraph],  # transformGraph
                          _type.HRESULT]
    PrepareForRender: _Callable[[_enum.D2D1_CHANGE_TYPE],  # changeType
                                _type.HRESULT]
    SetGraph: _Callable[[ID2D1TransformGraph],  # transformGraph
                        _type.HRESULT]


class ID2D1EffectContext(_Unknwnbase.IUnknown):
    GetDpi: _Callable[[_Pointer[_type.FLOAT],  # dpiX
                       _Pointer[_type.FLOAT]],  # dpiY
                      _type.c_void]
    CreateEffect: _Callable[[_Pointer[_struct.IID],  # effectId
                             _Pointer[_d2d1_1.ID2D1Effect]],  # effect
                            _type.HRESULT]
    GetMaximumSupportedFeatureLevel: _Callable[[_Pointer[_enum.D3D_FEATURE_LEVEL],  # featureLevels
                                                _type.UINT32,  # featureLevelsCount
                                                _Pointer[_enum.D3D_FEATURE_LEVEL]],  # maximumSupportedFeatureLevel
                                               _type.HRESULT]
    CreateTransformNodeFromEffect: _Callable[[_d2d1_1.ID2D1Effect,  # effect
                                              _Pointer[ID2D1TransformNode]],  # transformNode
                                             _type.HRESULT]
    CreateBlendTransform: _Callable[[_type.UINT32,  # numInputs
                                     _Pointer[_struct.D2D1_BLEND_DESCRIPTION],  # blendDescription
                                     _Pointer[ID2D1BlendTransform]],  # transform
                                    _type.HRESULT]
    CreateBorderTransform: _Callable[[_enum.D2D1_EXTEND_MODE,  # extendModeX
                                      _enum.D2D1_EXTEND_MODE,  # extendModeY
                                      _Pointer[ID2D1BorderTransform]],  # transform
                                     _type.HRESULT]
    CreateOffsetTransform: _Callable[[_struct.D2D1_POINT_2L,  # offset
                                      _Pointer[ID2D1OffsetTransform]],  # transform
                                     _type.HRESULT]
    CreateBoundsAdjustmentTransform: _Callable[[_Pointer[_struct.D2D1_RECT_L],  # outputRectangle
                                                _Pointer[ID2D1BoundsAdjustmentTransform]],  # transform
                                               _type.HRESULT]
    LoadPixelShader: _Callable[[_Pointer[_struct.GUID],  # shaderId
                                _Pointer[_type.BYTE],  # shaderBuffer
                                _type.UINT32],  # shaderBufferCount
                               _type.HRESULT]
    LoadVertexShader: _Callable[[_Pointer[_struct.GUID],  # resourceId
                                 _Pointer[_type.BYTE],  # shaderBuffer
                                 _type.UINT32],  # shaderBufferCount
                                _type.HRESULT]
    LoadComputeShader: _Callable[[_Pointer[_struct.GUID],  # resourceId
                                  _Pointer[_type.BYTE],  # shaderBuffer
                                  _type.UINT32],  # shaderBufferCount
                                 _type.HRESULT]
    IsShaderLoaded: _Callable[[_Pointer[_struct.GUID]],  # shaderId
                              _type.BOOL]
    CreateResourceTexture: _Callable[[_Pointer[_struct.GUID],  # resourceId
                                      _Pointer[_struct.D2D1_RESOURCE_TEXTURE_PROPERTIES],  # resourceTextureProperties
                                      _Pointer[_type.BYTE],  # data
                                      _Pointer[_type.UINT32],  # strides
                                      _type.UINT32,  # dataSize
                                      _Pointer[ID2D1ResourceTexture]],  # resourceTexture
                                     _type.HRESULT]
    FindResourceTexture: _Callable[[_Pointer[_struct.GUID],  # resourceId
                                    _Pointer[ID2D1ResourceTexture]],  # resourceTexture
                                   _type.HRESULT]
    CreateVertexBuffer: _Callable[[_Pointer[_struct.D2D1_VERTEX_BUFFER_PROPERTIES],  # vertexBufferProperties
                                   _Pointer[_struct.GUID],  # resourceId
                                   _Pointer[_struct.D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES],  # customVertexBufferProperties
                                   _Pointer[ID2D1VertexBuffer]],  # buffer
                                  _type.HRESULT]
    FindVertexBuffer: _Callable[[_Pointer[_struct.GUID],  # resourceId
                                 _Pointer[ID2D1VertexBuffer]],  # buffer
                                _type.HRESULT]
    CreateColorContext: _Callable[[_enum.D2D1_COLOR_SPACE,  # space
                                   _Pointer[_type.BYTE],  # profile
                                   _type.UINT32,  # profileSize
                                   _Pointer[_d2d1_1.ID2D1ColorContext]],  # colorContext
                                  _type.HRESULT]
    CreateColorContextFromFilename: _Callable[[_type.PCWSTR,  # filename
                                               _Pointer[_d2d1_1.ID2D1ColorContext]],  # colorContext
                                              _type.HRESULT]
    CreateColorContextFromWicColorContext: _Callable[[_wincodec.IWICColorContext,  # wicColorContext
                                                      _Pointer[_d2d1_1.ID2D1ColorContext]],  # colorContext
                                                     _type.HRESULT]
    CheckFeatureSupport: _Callable[[_enum.D2D1_FEATURE,  # feature
                                    _type.c_void_p,  # featureSupportData
                                    _type.UINT32],  # featureSupportDataSize
                                   _type.HRESULT]
    IsBufferPrecisionSupported: _Callable[[_enum.D2D1_BUFFER_PRECISION],  # bufferPrecision
                                          _type.BOOL]
