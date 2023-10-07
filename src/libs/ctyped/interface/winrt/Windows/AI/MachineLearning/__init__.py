from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Foundation as _Windows_Foundation
from ... import Media as _Windows_Media
from ... import Storage as _Windows_Storage
from ...Foundation import Collections as _Windows_Foundation_Collections
from ...Graphics.DirectX import Direct3D11 as _Windows_Graphics_DirectX_Direct3D11
from ...Storage import Streams as _Windows_Storage_Streams
from .... import inspectable as _inspectable
from ...... import enum as _enum
from ...... import struct as _struct
from ...... import type as _type
from ......_utils import _Pointer


class IImageFeatureDescriptor(_inspectable.IInspectable):
    get_BitmapPixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]],  # value
                                     _type.HRESULT]
    get_BitmapAlphaMode: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapAlphaMode]],  # value
                                   _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.UINT32]],  # value
                         _type.HRESULT]
    get_Height: _Callable[[_Pointer[_type.UINT32]],  # value
                          _type.HRESULT]


class IImageFeatureDescriptor2(_inspectable.IInspectable):
    get_PixelRange: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.LearningModelPixelRange]],  # value
                              _type.HRESULT]


class IImageFeatureValue(_inspectable.IInspectable):
    get_VideoFrame: _Callable[[_Pointer[_Windows_Media.IVideoFrame]],  # value
                              _type.HRESULT]


class IImageFeatureValueStatics(_inspectable.IInspectable, factory=True):
    CreateFromVideoFrame: _Callable[[_Windows_Media.IVideoFrame,  # image
                                     _Pointer[IImageFeatureValue]],  # result
                                    _type.HRESULT]


class ILearningModel(_inspectable.IInspectable):
    get_Author: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Domain: _Callable[[_Pointer[_type.HSTRING]],  # value
                          _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Version: _Callable[[_Pointer[_type.INT64]],  # value
                           _type.HRESULT]
    get_Metadata: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                            _type.HRESULT]
    get_InputFeatures: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ILearningModelFeatureDescriptor]]],  # value
                                 _type.HRESULT]
    get_OutputFeatures: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[ILearningModelFeatureDescriptor]]],  # value
                                  _type.HRESULT]


class ILearningModelBinding(_inspectable.IInspectable):
    Bind: _Callable[[_type.HSTRING,  # name
                     _inspectable.IInspectable],  # value
                    _type.HRESULT]
    BindWithProperties: _Callable[[_type.HSTRING,  # name
                                   _inspectable.IInspectable,  # value
                                   _Windows_Foundation_Collections.IPropertySet],  # props
                                  _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class ILearningModelBindingFactory(_inspectable.IInspectable, factory=True):
    CreateFromSession: _Callable[[ILearningModelSession,  # session
                                  _Pointer[ILearningModelBinding]],  # value
                                 _type.HRESULT]


class ILearningModelDevice(_inspectable.IInspectable):
    get_AdapterId: _Callable[[_Pointer[_struct.Windows.Graphics.DisplayAdapterId]],  # value
                             _type.HRESULT]
    get_Direct3D11Device: _Callable[[_Pointer[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice]],  # value
                                    _type.HRESULT]


class ILearningModelDeviceFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_enum.Windows.AI.MachineLearning.LearningModelDeviceKind,  # deviceKind
                       _Pointer[ILearningModelDevice]],  # value
                      _type.HRESULT]


class ILearningModelDeviceStatics(_inspectable.IInspectable, factory=True):
    CreateFromDirect3D11Device: _Callable[[_Windows_Graphics_DirectX_Direct3D11.IDirect3DDevice,  # device
                                           _Pointer[ILearningModelDevice]],  # result
                                          _type.HRESULT]


class ILearningModelEvaluationResult(_inspectable.IInspectable):
    get_CorrelationId: _Callable[[_Pointer[_type.HSTRING]],  # value
                                 _type.HRESULT]
    get_ErrorStatus: _Callable[[_Pointer[_type.INT32]],  # value
                               _type.HRESULT]
    get_Succeeded: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    get_Outputs: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                           _type.HRESULT]


class ILearningModelFeatureDescriptor(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]
    get_Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    get_Kind: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.LearningModelFeatureKind]],  # value
                        _type.HRESULT]
    get_IsRequired: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]


class ILearningModelFeatureValue(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.LearningModelFeatureKind]],  # value
                        _type.HRESULT]


class ILearningModelOperatorProvider(_inspectable.IInspectable):
    pass


class ILearningModelSession(_inspectable.IInspectable):
    get_Model: _Callable[[_Pointer[ILearningModel]],  # value
                         _type.HRESULT]
    get_Device: _Callable[[_Pointer[ILearningModelDevice]],  # value
                          _type.HRESULT]
    get_EvaluationProperties: _Callable[[_Pointer[_Windows_Foundation_Collections.IPropertySet]],  # value
                                        _type.HRESULT]
    EvaluateAsync: _Callable[[ILearningModelBinding,  # bindings
                              _type.HSTRING,  # correlationId
                              _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModelEvaluationResult]]],  # operation
                             _type.HRESULT]
    EvaluateFeaturesAsync: _Callable[[_Windows_Foundation_Collections.IMap[_type.HSTRING, _inspectable.IInspectable],  # features
                                      _type.HSTRING,  # correlationId
                                      _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModelEvaluationResult]]],  # operation
                                     _type.HRESULT]
    Evaluate: _Callable[[ILearningModelBinding,  # bindings
                         _type.HSTRING,  # correlationId
                         _Pointer[ILearningModelEvaluationResult]],  # result
                        _type.HRESULT]
    EvaluateFeatures: _Callable[[_Windows_Foundation_Collections.IMap[_type.HSTRING, _inspectable.IInspectable],  # features
                                 _type.HSTRING,  # correlationId
                                 _Pointer[ILearningModelEvaluationResult]],  # result
                                _type.HRESULT]


class ILearningModelSessionFactory(_inspectable.IInspectable):
    CreateFromModel: _Callable[[ILearningModel,  # model
                                _Pointer[ILearningModelSession]],  # value
                               _type.HRESULT]
    CreateFromModelOnDevice: _Callable[[ILearningModel,  # model
                                        ILearningModelDevice,  # deviceToRunOn
                                        _Pointer[ILearningModelSession]],  # value
                                       _type.HRESULT]


class ILearningModelSessionFactory2(_inspectable.IInspectable, factory=True):
    CreateFromModelOnDeviceWithSessionOptions: _Callable[[ILearningModel,  # model
                                                          ILearningModelDevice,  # deviceToRunOn
                                                          ILearningModelSessionOptions,  # learningModelSessionOptions
                                                          _Pointer[ILearningModelSession]],  # value
                                                         _type.HRESULT]


class ILearningModelSessionOptions(_inspectable.IInspectable):
    get_BatchSizeOverride: _Callable[[_Pointer[_type.UINT32]],  # value
                                     _type.HRESULT]
    put_BatchSizeOverride: _Callable[[_type.UINT32],  # value
                                     _type.HRESULT]


class ILearningModelSessionOptions2(_inspectable.IInspectable):
    get_CloseModelOnSessionCreation: _Callable[[_Pointer[_type.boolean]],  # value
                                               _type.HRESULT]
    put_CloseModelOnSessionCreation: _Callable[[_type.boolean],  # value
                                               _type.HRESULT]


class ILearningModelSessionOptions3(_inspectable.IInspectable):
    OverrideNamedDimension: _Callable[[_type.HSTRING,  # name
                                       _type.UINT32],  # dimension
                                      _type.HRESULT]


class ILearningModelStatics(_inspectable.IInspectable, factory=True):
    LoadFromStorageFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # modelFile
                                         _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModel]]],  # operation
                                        _type.HRESULT]
    LoadFromStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # modelStream
                                    _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModel]]],  # operation
                                   _type.HRESULT]
    LoadFromFilePath: _Callable[[_type.HSTRING,  # filePath
                                 _Pointer[ILearningModel]],  # result
                                _type.HRESULT]
    LoadFromStream: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # modelStream
                               _Pointer[ILearningModel]],  # result
                              _type.HRESULT]
    LoadFromStorageFileWithOperatorProviderAsync: _Callable[[_Windows_Storage.IStorageFile,  # modelFile
                                                             ILearningModelOperatorProvider,  # operatorProvider
                                                             _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModel]]],  # operation
                                                            _type.HRESULT]
    LoadFromStreamWithOperatorProviderAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # modelStream
                                                        ILearningModelOperatorProvider,  # operatorProvider
                                                        _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModel]]],  # operation
                                                       _type.HRESULT]
    LoadFromFilePathWithOperatorProvider: _Callable[[_type.HSTRING,  # filePath
                                                     ILearningModelOperatorProvider,  # operatorProvider
                                                     _Pointer[ILearningModel]],  # result
                                                    _type.HRESULT]
    LoadFromStreamWithOperatorProvider: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # modelStream
                                                   ILearningModelOperatorProvider,  # operatorProvider
                                                   _Pointer[ILearningModel]],  # result
                                                  _type.HRESULT]


class IMapFeatureDescriptor(_inspectable.IInspectable):
    get_KeyKind: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.TensorKind]],  # value
                           _type.HRESULT]
    get_ValueDescriptor: _Callable[[_Pointer[ILearningModelFeatureDescriptor]],  # value
                                   _type.HRESULT]


class ISequenceFeatureDescriptor(_inspectable.IInspectable):
    get_ElementDescriptor: _Callable[[_Pointer[ILearningModelFeatureDescriptor]],  # value
                                     _type.HRESULT]


class ITensor(_inspectable.IInspectable):
    get_TensorKind: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.TensorKind]],  # value
                              _type.HRESULT]
    get_Shape: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT64]]],  # value
                         _type.HRESULT]


class ITensorBoolean(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.boolean]]],  # result
                               _type.HRESULT]


class ITensorBooleanStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorBoolean]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorBoolean]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.boolean],  # data
                                _Pointer[ITensorBoolean]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.boolean],  # data
                                   _Pointer[ITensorBoolean]],  # result
                                  _type.HRESULT]


class ITensorBooleanStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.boolean],  # data
                                                 _Pointer[ITensorBoolean]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorBoolean]],  # result
                                _type.HRESULT]


class ITensorDouble(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.DOUBLE]]],  # result
                               _type.HRESULT]


class ITensorDoubleStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorDouble]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorDouble]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.DOUBLE],  # data
                                _Pointer[ITensorDouble]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.DOUBLE],  # data
                                   _Pointer[ITensorDouble]],  # result
                                  _type.HRESULT]


class ITensorDoubleStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.DOUBLE],  # data
                                                 _Pointer[ITensorDouble]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorDouble]],  # result
                                _type.HRESULT]


class ITensorFeatureDescriptor(_inspectable.IInspectable):
    get_TensorKind: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.TensorKind]],  # value
                              _type.HRESULT]
    get_Shape: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT64]]],  # value
                         _type.HRESULT]


class ITensorFloat(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.FLOAT]]],  # result
                               _type.HRESULT]


class ITensorFloat16Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.FLOAT]]],  # result
                               _type.HRESULT]


class ITensorFloat16BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorFloat16Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorFloat16Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.FLOAT],  # data
                                _Pointer[ITensorFloat16Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.FLOAT],  # data
                                   _Pointer[ITensorFloat16Bit]],  # result
                                  _type.HRESULT]


class ITensorFloat16BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.FLOAT],  # data
                                                 _Pointer[ITensorFloat16Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorFloat16Bit]],  # result
                                _type.HRESULT]


class ITensorFloatStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorFloat]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorFloat]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.FLOAT],  # data
                                _Pointer[ITensorFloat]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.FLOAT],  # data
                                   _Pointer[ITensorFloat]],  # result
                                  _type.HRESULT]


class ITensorFloatStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.FLOAT],  # data
                                                 _Pointer[ITensorFloat]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorFloat]],  # result
                                _type.HRESULT]


class ITensorInt16Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT16]]],  # result
                               _type.HRESULT]


class ITensorInt16BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorInt16Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorInt16Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.INT16],  # data
                                _Pointer[ITensorInt16Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.INT16],  # data
                                   _Pointer[ITensorInt16Bit]],  # result
                                  _type.HRESULT]


class ITensorInt16BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.INT16],  # data
                                                 _Pointer[ITensorInt16Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorInt16Bit]],  # result
                                _type.HRESULT]


class ITensorInt32Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT32]]],  # result
                               _type.HRESULT]


class ITensorInt32BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorInt32Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorInt32Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.INT32],  # data
                                _Pointer[ITensorInt32Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.INT32],  # data
                                   _Pointer[ITensorInt32Bit]],  # result
                                  _type.HRESULT]


class ITensorInt32BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.INT32],  # data
                                                 _Pointer[ITensorInt32Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorInt32Bit]],  # result
                                _type.HRESULT]


class ITensorInt64Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.INT64]]],  # result
                               _type.HRESULT]


class ITensorInt64BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorInt64Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorInt64Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.INT64],  # data
                                _Pointer[ITensorInt64Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.INT64],  # data
                                   _Pointer[ITensorInt64Bit]],  # result
                                  _type.HRESULT]


class ITensorInt64BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.INT64],  # data
                                                 _Pointer[ITensorInt64Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorInt64Bit]],  # result
                                _type.HRESULT]


class ITensorInt8Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.BYTE]]],  # result
                               _type.HRESULT]


class ITensorInt8BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorInt8Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorInt8Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.BYTE],  # data
                                _Pointer[ITensorInt8Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.BYTE],  # data
                                   _Pointer[ITensorInt8Bit]],  # result
                                  _type.HRESULT]


class ITensorInt8BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.BYTE],  # data
                                                 _Pointer[ITensorInt8Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorInt8Bit]],  # result
                                _type.HRESULT]


class ITensorString(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # result
                               _type.HRESULT]


class ITensorStringStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorString]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorString]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.HSTRING],  # data
                                _Pointer[ITensorString]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.HSTRING],  # data
                                   _Pointer[ITensorString]],  # result
                                  _type.HRESULT]


class ITensorStringStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.HSTRING],  # data
                                                 _Pointer[ITensorString]],  # result
                                                _type.HRESULT]


class ITensorUInt16Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT16]]],  # result
                               _type.HRESULT]


class ITensorUInt16BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorUInt16Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorUInt16Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.UINT16],  # data
                                _Pointer[ITensorUInt16Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.UINT16],  # data
                                   _Pointer[ITensorUInt16Bit]],  # result
                                  _type.HRESULT]


class ITensorUInt16BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.UINT16],  # data
                                                 _Pointer[ITensorUInt16Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorUInt16Bit]],  # result
                                _type.HRESULT]


class ITensorUInt32Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT32]]],  # result
                               _type.HRESULT]


class ITensorUInt32BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorUInt32Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorUInt32Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.UINT32],  # data
                                _Pointer[ITensorUInt32Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.UINT32],  # data
                                   _Pointer[ITensorUInt32Bit]],  # result
                                  _type.HRESULT]


class ITensorUInt32BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.UINT32],  # data
                                                 _Pointer[ITensorUInt32Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorUInt32Bit]],  # result
                                _type.HRESULT]


class ITensorUInt64Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.UINT64]]],  # result
                               _type.HRESULT]


class ITensorUInt64BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorUInt64Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorUInt64Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.UINT64],  # data
                                _Pointer[ITensorUInt64Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.UINT64],  # data
                                   _Pointer[ITensorUInt64Bit]],  # result
                                  _type.HRESULT]


class ITensorUInt64BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.UINT64],  # data
                                                 _Pointer[ITensorUInt64Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorUInt64Bit]],  # result
                                _type.HRESULT]


class ITensorUInt8Bit(_inspectable.IInspectable):
    GetAsVectorView: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.BYTE]]],  # result
                               _type.HRESULT]


class ITensorUInt8BitStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Pointer[ITensorUInt8Bit]],  # result
                      _type.HRESULT]
    Create2: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                        _Pointer[ITensorUInt8Bit]],  # result
                       _type.HRESULT]
    CreateFromArray: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                _type.UINT32,  # __dataSize
                                _Pointer[_type.BYTE],  # data
                                _Pointer[ITensorUInt8Bit]],  # result
                               _type.HRESULT]
    CreateFromIterable: _Callable[[_Windows_Foundation_Collections.IIterable[_type.INT64],  # shape
                                   _Windows_Foundation_Collections.IIterable[_type.BYTE],  # data
                                   _Pointer[ITensorUInt8Bit]],  # result
                                  _type.HRESULT]


class ITensorUInt8BitStatics2(_inspectable.IInspectable, factory=True):
    CreateFromShapeArrayAndDataArray: _Callable[[_type.UINT32,  # __shapeSize
                                                 _Pointer[_type.INT64],  # shape
                                                 _type.UINT32,  # __dataSize
                                                 _Pointer[_type.BYTE],  # data
                                                 _Pointer[ITensorUInt8Bit]],  # result
                                                _type.HRESULT]
    CreateFromBuffer: _Callable[[_type.UINT32,  # __shapeSize
                                 _Pointer[_type.INT64],  # shape
                                 _Windows_Storage_Streams.IBuffer,  # buffer
                                 _Pointer[ITensorUInt8Bit]],  # result
                                _type.HRESULT]
