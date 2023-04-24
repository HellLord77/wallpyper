from __future__ import annotations

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from .... import Storage as _Windows_Storage
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import type as _type
from ......._utils import _Pointer


class IImageVariableDescriptorPreview(_inspectable.IInspectable):
    BitmapPixelFormat: _Callable[[_Pointer[_enum.Windows.Graphics.Imaging.BitmapPixelFormat]],  # value
                                 _type.HRESULT]
    Width: _Callable[[_Pointer[_type.UINT32]],  # value
                     _type.HRESULT]
    Height: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]


class IInferencingOptionsPreview(_inspectable.IInspectable):
    PreferredDeviceKind: _Callable[[_enum.Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview],  # value
                                   _type.HRESULT]
    IsTracingEnabled: _Callable[[_type.boolean],  # value
                                _type.HRESULT]
    MaxBatchSize: _Callable[[_type.INT32],  # value
                            _type.HRESULT]
    MinimizeMemoryAllocation: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]
    ReclaimMemoryAfterEvaluation: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class ILearningModelBindingPreview(_inspectable.IInspectable):
    Bind: _Callable[[_type.HSTRING,  # name
                     _inspectable.IInspectable],  # value
                    _type.HRESULT]
    BindWithProperties: _Callable[[_type.HSTRING,  # name
                                   _inspectable.IInspectable,  # value
                                   _Windows_Foundation_Collections.IPropertySet],  # metadata
                                  _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class ILearningModelBindingPreviewFactory(_inspectable.IInspectable):
    CreateFromModel: _Callable[[ILearningModelPreview,  # model
                                _Pointer[ILearningModelBindingPreview]],  # value
                               _type.HRESULT]

    _factory = True


class ILearningModelDescriptionPreview(_inspectable.IInspectable):
    Author: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                    _type.HRESULT]
    Domain: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    Version: _Callable[[_Pointer[_type.INT64]],  # value
                       _type.HRESULT]
    Metadata: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _type.HSTRING]]],  # value
                        _type.HRESULT]
    InputFeatures: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[ILearningModelVariableDescriptorPreview]]],  # value
                             _type.HRESULT]
    OutputFeatures: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[ILearningModelVariableDescriptorPreview]]],  # value
                              _type.HRESULT]


class ILearningModelEvaluationResultPreview(_inspectable.IInspectable):
    CorrelationId: _Callable[[_Pointer[_type.HSTRING]],  # correlationId
                             _type.HRESULT]
    Outputs: _Callable[[_Pointer[_Windows_Foundation_Collections.IMapView[_type.HSTRING, _inspectable.IInspectable]]],  # value
                       _type.HRESULT]


class ILearningModelPreview(_inspectable.IInspectable):
    EvaluateAsync: _Callable[[ILearningModelBindingPreview,  # binding
                              _type.HSTRING,  # correlationId
                              _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModelEvaluationResultPreview]]],  # evalOperation
                             _type.HRESULT]
    EvaluateFeaturesAsync: _Callable[[_Windows_Foundation_Collections.IMap[_type.HSTRING, _inspectable.IInspectable],  # features
                                      _type.HSTRING,  # correlationId
                                      _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModelEvaluationResultPreview]]],  # evalOperation
                                     _type.HRESULT]
    Description: _Callable[[_Pointer[ILearningModelDescriptionPreview]],  # returnValue
                           _type.HRESULT]
    InferencingOptions: _Callable[[IInferencingOptionsPreview],  # value
                                  _type.HRESULT]


class ILearningModelPreviewStatics(_inspectable.IInspectable):
    LoadModelFromStorageFileAsync: _Callable[[_Windows_Storage.IStorageFile,  # modelFile
                                              _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModelPreview]]],  # modelCreationOperation
                                             _type.HRESULT]
    LoadModelFromStreamAsync: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference,  # modelStream
                                         _Pointer[_Windows_Foundation.IAsyncOperation[ILearningModelPreview]]],  # modelCreationOperation
                                        _type.HRESULT]

    _factory = True


class ILearningModelVariableDescriptorPreview(_inspectable.IInspectable):
    Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                    _type.HRESULT]
    Description: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    ModelFeatureKind: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview]],  # value
                                _type.HRESULT]
    IsRequired: _Callable[[_Pointer[_type.boolean]],  # value
                          _type.HRESULT]


class IMapVariableDescriptorPreview(_inspectable.IInspectable):
    KeyKind: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.Preview.FeatureElementKindPreview]],  # value
                       _type.HRESULT]
    ValidStringKeys: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[_type.HSTRING]]],  # value
                               _type.HRESULT]
    ValidIntegerKeys: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[_type.INT64]]],  # value
                                _type.HRESULT]
    Fields: _Callable[[_Pointer[ILearningModelVariableDescriptorPreview]],  # value
                      _type.HRESULT]


class ISequenceVariableDescriptorPreview(_inspectable.IInspectable):
    ElementType: _Callable[[_Pointer[ILearningModelVariableDescriptorPreview]],  # value
                           _type.HRESULT]


class ITensorVariableDescriptorPreview(_inspectable.IInspectable):
    DataType: _Callable[[_Pointer[_enum.Windows.AI.MachineLearning.Preview.FeatureElementKindPreview]],  # value
                        _type.HRESULT]
    Shape: _Callable[[_Pointer[_Windows_Foundation_Collections.IIterable[_type.INT64]]],  # value
                     _type.HRESULT]
