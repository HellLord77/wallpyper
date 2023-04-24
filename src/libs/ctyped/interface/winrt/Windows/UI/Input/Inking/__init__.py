from __future__ import annotations

from typing import Callable as _Callable

from ... import Core as _Windows_UI_Core
from ... import Input as _Windows_UI_Input
from .... import Foundation as _Windows_Foundation
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IInkDrawingAttributes(_inspectable.IInspectable):
    get_Color: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                         _type.HRESULT]
    put_Color: _Callable[[_struct.Windows.UI.Color],  # value
                         _type.HRESULT]
    get_PenTip: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.PenTipShape]],  # value
                          _type.HRESULT]
    put_PenTip: _Callable[[_enum.Windows.UI.Input.Inking.PenTipShape],  # value
                          _type.HRESULT]
    get_Size: _Callable[[_Pointer[_struct.Windows.Foundation.Size]],  # value
                        _type.HRESULT]
    put_Size: _Callable[[_struct.Windows.Foundation.Size],  # value
                        _type.HRESULT]
    get_IgnorePressure: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IgnorePressure: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_FitToCurve: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_FitToCurve: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class IInkDrawingAttributes2(_inspectable.IInspectable):
    get_PenTipTransform: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                                   _type.HRESULT]
    put_PenTipTransform: _Callable[[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                   _type.HRESULT]
    get_DrawAsHighlighter: _Callable[[_Pointer[_type.boolean]],  # value
                                     _type.HRESULT]
    put_DrawAsHighlighter: _Callable[[_type.boolean],  # value
                                     _type.HRESULT]


class IInkDrawingAttributes3(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.InkDrawingAttributesKind]],  # value
                        _type.HRESULT]
    get_PencilProperties: _Callable[[_Pointer[IInkDrawingAttributesPencilProperties]],  # value
                                    _type.HRESULT]


class IInkDrawingAttributes4(_inspectable.IInspectable):
    get_IgnoreTilt: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    put_IgnoreTilt: _Callable[[_type.boolean],  # value
                              _type.HRESULT]


class IInkDrawingAttributes5(_inspectable.IInspectable):
    get_ModelerAttributes: _Callable[[_Pointer[IInkModelerAttributes]],  # value
                                     _type.HRESULT]


class IInkDrawingAttributesPencilProperties(_inspectable.IInspectable):
    get_Opacity: _Callable[[_Pointer[_type.DOUBLE]],  # value
                           _type.HRESULT]
    put_Opacity: _Callable[[_type.DOUBLE],  # value
                           _type.HRESULT]


class IInkDrawingAttributesStatics(_inspectable.IInspectable):
    CreateForPencil: _Callable[[_Pointer[IInkDrawingAttributes]],  # result
                               _type.HRESULT]

    _factory = True


class IInkInputConfiguration(_inspectable.IInspectable):
    get_IsPrimaryBarrelButtonInputEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                     _type.HRESULT]
    put_IsPrimaryBarrelButtonInputEnabled: _Callable[[_type.boolean],  # value
                                                     _type.HRESULT]
    get_IsEraserInputEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                        _type.HRESULT]
    put_IsEraserInputEnabled: _Callable[[_type.boolean],  # value
                                        _type.HRESULT]


class IInkInputConfiguration2(_inspectable.IInspectable):
    get_IsPenHapticFeedbackEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                              _type.HRESULT]
    put_IsPenHapticFeedbackEnabled: _Callable[[_type.boolean],  # value
                                              _type.HRESULT]


class IInkInputProcessingConfiguration(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.InkInputProcessingMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.UI.Input.Inking.InkInputProcessingMode],  # value
                        _type.HRESULT]
    get_RightDragAction: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.InkInputRightDragAction]],  # value
                                   _type.HRESULT]
    put_RightDragAction: _Callable[[_enum.Windows.UI.Input.Inking.InkInputRightDragAction],  # value
                                   _type.HRESULT]


class IInkManager(_inspectable.IInspectable):
    get_Mode: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.InkManipulationMode]],  # value
                        _type.HRESULT]
    put_Mode: _Callable[[_enum.Windows.UI.Input.Inking.InkManipulationMode],  # value
                        _type.HRESULT]
    ProcessPointerDown: _Callable[[_Windows_UI_Input.IPointerPoint],  # pointerPoint
                                  _type.HRESULT]
    ProcessPointerUpdate: _Callable[[_Windows_UI_Input.IPointerPoint,  # pointerPoint
                                     _Pointer[_inspectable.IInspectable]],  # updateInformation
                                    _type.HRESULT]
    ProcessPointerUp: _Callable[[_Windows_UI_Input.IPointerPoint,  # pointerPoint
                                 _Pointer[_struct.Windows.Foundation.Rect]],  # updateRectangle
                                _type.HRESULT]
    SetDefaultDrawingAttributes: _Callable[[IInkDrawingAttributes],  # drawingAttributes
                                           _type.HRESULT]
    RecognizeAsync2: _Callable[[_enum.Windows.UI.Input.Inking.InkRecognitionTarget,  # recognitionTarget
                                _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IInkRecognitionResult]]]],  # recognitionResults
                               _type.HRESULT]


class IInkModelerAttributes(_inspectable.IInspectable):
    get_PredictionTime: _Callable[[_Pointer[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]
    put_PredictionTime: _Callable[[_struct.Windows.Foundation.TimeSpan],  # value
                                  _type.HRESULT]
    get_ScalingFactor: _Callable[[_Pointer[_type.FLOAT]],  # value
                                 _type.HRESULT]
    put_ScalingFactor: _Callable[[_type.FLOAT],  # value
                                 _type.HRESULT]


class IInkModelerAttributes2(_inspectable.IInspectable):
    get_UseVelocityBasedPressure: _Callable[[_Pointer[_type.boolean]],  # value
                                            _type.HRESULT]
    put_UseVelocityBasedPressure: _Callable[[_type.boolean],  # value
                                            _type.HRESULT]


class IInkPoint(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_Pressure: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]


class IInkPoint2(_inspectable.IInspectable):
    get_TiltX: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_TiltY: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_Timestamp: _Callable[[_Pointer[_type.UINT64]],  # value
                             _type.HRESULT]


class IInkPointFactory(_inspectable.IInspectable):
    CreateInkPoint: _Callable[[_struct.Windows.Foundation.Point,  # position
                               _type.FLOAT,  # pressure
                               _Pointer[IInkPoint]],  # result
                              _type.HRESULT]


class IInkPointFactory2(_inspectable.IInspectable):
    CreateInkPointWithTiltAndTimestamp: _Callable[[_struct.Windows.Foundation.Point,  # position
                                                   _type.FLOAT,  # pressure
                                                   _type.FLOAT,  # tiltX
                                                   _type.FLOAT,  # tiltY
                                                   _type.UINT64,  # timestamp
                                                   _Pointer[IInkPoint]],  # result
                                                  _type.HRESULT]

    _factory = True


class IInkPresenter(_inspectable.IInspectable):
    get_IsInputEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsInputEnabled: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_InputDeviceTypes: _Callable[[_Pointer[_enum.Windows.UI.Core.CoreInputDeviceTypes]],  # value
                                    _type.HRESULT]
    put_InputDeviceTypes: _Callable[[_enum.Windows.UI.Core.CoreInputDeviceTypes],  # value
                                    _type.HRESULT]
    get_UnprocessedInput: _Callable[[_Pointer[IInkUnprocessedInput]],  # value
                                    _type.HRESULT]
    get_StrokeInput: _Callable[[_Pointer[IInkStrokeInput]],  # value
                               _type.HRESULT]
    get_InputProcessingConfiguration: _Callable[[_Pointer[IInkInputProcessingConfiguration]],  # value
                                                _type.HRESULT]
    get_StrokeContainer: _Callable[[_Pointer[IInkStrokeContainer]],  # value
                                   _type.HRESULT]
    put_StrokeContainer: _Callable[[IInkStrokeContainer],  # value
                                   _type.HRESULT]
    CopyDefaultDrawingAttributes: _Callable[[_Pointer[IInkDrawingAttributes]],  # value
                                            _type.HRESULT]
    UpdateDefaultDrawingAttributes: _Callable[[IInkDrawingAttributes],  # value
                                              _type.HRESULT]
    ActivateCustomDrying: _Callable[[_Pointer[IInkSynchronizer]],  # inkSynchronizer
                                    _type.HRESULT]
    SetPredefinedConfiguration: _Callable[[_enum.Windows.UI.Input.Inking.InkPresenterPredefinedConfiguration],  # value
                                          _type.HRESULT]
    add_StrokesCollected: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkPresenter, IInkStrokesCollectedEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # cookie
                                    _type.HRESULT]
    remove_StrokesCollected: _Callable[[_struct.EventRegistrationToken],  # cookie
                                       _type.HRESULT]
    add_StrokesErased: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkPresenter, IInkStrokesErasedEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_StrokesErased: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]


class IInkPresenter2(_inspectable.IInspectable):
    get_HighContrastAdjustment: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.InkHighContrastAdjustment]],  # value
                                          _type.HRESULT]
    put_HighContrastAdjustment: _Callable[[_enum.Windows.UI.Input.Inking.InkHighContrastAdjustment],  # value
                                          _type.HRESULT]


class IInkPresenter3(_inspectable.IInspectable):
    get_InputConfiguration: _Callable[[_Pointer[IInkInputConfiguration]],  # value
                                      _type.HRESULT]


class IInkPresenterProtractor(_inspectable.IInspectable):
    get_AreTickMarksVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_AreTickMarksVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_AreRaysVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_AreRaysVisible: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    get_IsCenterMarkerVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsCenterMarkerVisible: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsAngleReadoutVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                         _type.HRESULT]
    put_IsAngleReadoutVisible: _Callable[[_type.boolean],  # value
                                         _type.HRESULT]
    get_IsResizable: _Callable[[_Pointer[_type.boolean]],  # value
                               _type.HRESULT]
    put_IsResizable: _Callable[[_type.boolean],  # value
                               _type.HRESULT]
    get_Radius: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Radius: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_AccentColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                               _type.HRESULT]
    put_AccentColor: _Callable[[_struct.Windows.UI.Color],  # value
                               _type.HRESULT]


class IInkPresenterProtractorFactory(_inspectable.IInspectable):
    Create: _Callable[[IInkPresenter,  # inkPresenter
                       _Pointer[IInkPresenterProtractor]],  # inkPresenterProtractor
                      _type.HRESULT]

    _factory = True


class IInkPresenterRuler(_inspectable.IInspectable):
    get_Length: _Callable[[_Pointer[_type.DOUBLE]],  # value
                          _type.HRESULT]
    put_Length: _Callable[[_type.DOUBLE],  # value
                          _type.HRESULT]
    get_Width: _Callable[[_Pointer[_type.DOUBLE]],  # value
                         _type.HRESULT]
    put_Width: _Callable[[_type.DOUBLE],  # value
                         _type.HRESULT]


class IInkPresenterRuler2(_inspectable.IInspectable):
    get_AreTickMarksVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                       _type.HRESULT]
    put_AreTickMarksVisible: _Callable[[_type.boolean],  # value
                                       _type.HRESULT]
    get_IsCompassVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsCompassVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]


class IInkPresenterRulerFactory(_inspectable.IInspectable):
    Create: _Callable[[IInkPresenter,  # inkPresenter
                       _Pointer[IInkPresenterRuler]],  # inkPresenterRuler
                      _type.HRESULT]

    _factory = True


class IInkPresenterStencil(_inspectable.IInspectable):
    get_Kind: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.InkPresenterStencilKind]],  # value
                        _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]
    put_IsVisible: _Callable[[_type.boolean],  # value
                             _type.HRESULT]
    get_BackgroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_BackgroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_ForegroundColor: _Callable[[_Pointer[_struct.Windows.UI.Color]],  # value
                                   _type.HRESULT]
    put_ForegroundColor: _Callable[[_struct.Windows.UI.Color],  # value
                                   _type.HRESULT]
    get_Transform: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                             _type.HRESULT]
    put_Transform: _Callable[[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                             _type.HRESULT]


class IInkRecognitionResult(_inspectable.IInspectable):
    get_BoundingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # boundingRect
                                _type.HRESULT]
    GetTextCandidates: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_type.HSTRING]]],  # textCandidates
                                 _type.HRESULT]
    GetStrokes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkStroke]]],  # strokes
                          _type.HRESULT]


class IInkRecognizer(_inspectable.IInspectable):
    get_Name: _Callable[[_Pointer[_type.HSTRING]],  # value
                        _type.HRESULT]


class IInkRecognizerContainer(_inspectable.IInspectable):
    SetDefaultRecognizer: _Callable[[IInkRecognizer],  # recognizer
                                    _type.HRESULT]
    RecognizeAsync: _Callable[[IInkStrokeContainer,  # strokeCollection
                               _enum.Windows.UI.Input.Inking.InkRecognitionTarget,  # recognitionTarget
                               _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Foundation_Collections.IVectorView[IInkRecognitionResult]]]],  # recognitionResults
                              _type.HRESULT]
    GetRecognizers: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkRecognizer]]],  # recognizerView
                              _type.HRESULT]


class IInkStroke(_inspectable.IInspectable):
    get_DrawingAttributes: _Callable[[_Pointer[IInkDrawingAttributes]],  # value
                                     _type.HRESULT]
    put_DrawingAttributes: _Callable[[IInkDrawingAttributes],  # value
                                     _type.HRESULT]
    get_BoundingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    get_Selected: _Callable[[_Pointer[_type.boolean]],  # value
                            _type.HRESULT]
    put_Selected: _Callable[[_type.boolean],  # value
                            _type.HRESULT]
    get_Recognized: _Callable[[_Pointer[_type.boolean]],  # value
                              _type.HRESULT]
    GetRenderingSegments: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkStrokeRenderingSegment]]],  # renderingSegments
                                    _type.HRESULT]
    Clone: _Callable[[_Pointer[IInkStroke]],  # clonedStroke
                     _type.HRESULT]


class IInkStroke2(_inspectable.IInspectable):
    get_PointTransform: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                                  _type.HRESULT]
    put_PointTransform: _Callable[[_struct.Windows.Foundation.Numerics.Matrix3x2],  # value
                                  _type.HRESULT]
    GetInkPoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkPoint]]],  # inkPoints
                            _type.HRESULT]


class IInkStroke3(_inspectable.IInspectable):
    get_Id: _Callable[[_Pointer[_type.UINT32]],  # value
                      _type.HRESULT]
    get_StrokeStartedTime: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]]],  # value
                                     _type.HRESULT]
    put_StrokeStartedTime: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime]],  # value
                                     _type.HRESULT]
    get_StrokeDuration: _Callable[[_Pointer[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]]],  # value
                                  _type.HRESULT]
    put_StrokeDuration: _Callable[[_Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan]],  # value
                                  _type.HRESULT]


class IInkStroke4(_inspectable.IInspectable):
    get_PointerId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]


class IInkStrokeBuilder(_inspectable.IInspectable):
    BeginStroke: _Callable[[_Windows_UI_Input.IPointerPoint],  # pointerPoint
                           _type.HRESULT]
    AppendToStroke: _Callable[[_Windows_UI_Input.IPointerPoint,  # pointerPoint
                               _Pointer[_Windows_UI_Input.IPointerPoint]],  # previousPointerPoint
                              _type.HRESULT]
    EndStroke: _Callable[[_Windows_UI_Input.IPointerPoint,  # pointerPoint
                          _Pointer[IInkStroke]],  # stroke
                         _type.HRESULT]
    CreateStroke: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Foundation.Point],  # points
                             _Pointer[IInkStroke]],  # stroke
                            _type.HRESULT]
    SetDefaultDrawingAttributes: _Callable[[IInkDrawingAttributes],  # drawingAttributes
                                           _type.HRESULT]


class IInkStrokeBuilder2(_inspectable.IInspectable):
    CreateStrokeFromInkPoints: _Callable[[_Windows_Foundation_Collections.IIterable[IInkPoint],  # inkPoints
                                          _struct.Windows.Foundation.Numerics.Matrix3x2,  # transform
                                          _Pointer[IInkStroke]],  # result
                                         _type.HRESULT]


class IInkStrokeBuilder3(_inspectable.IInspectable):
    CreateStrokeFromInkPoints: _Callable[[_Windows_Foundation_Collections.IIterable[IInkPoint],  # inkPoints
                                          _struct.Windows.Foundation.Numerics.Matrix3x2,  # transform
                                          _Windows_Foundation.IReference[_struct.Windows.Foundation.DateTime],  # strokeStartedTime
                                          _Windows_Foundation.IReference[_struct.Windows.Foundation.TimeSpan],  # strokeDuration
                                          _Pointer[IInkStroke]],  # result
                                         _type.HRESULT]


class IInkStrokeContainer(_inspectable.IInspectable):
    get_BoundingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]
    AddStroke: _Callable[[IInkStroke],  # stroke
                         _type.HRESULT]
    DeleteSelected: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # invalidatedRect
                              _type.HRESULT]
    MoveSelected: _Callable[[_struct.Windows.Foundation.Point,  # translation
                             _Pointer[_struct.Windows.Foundation.Rect]],  # invalidatedRectangle
                            _type.HRESULT]
    SelectWithPolyLine: _Callable[[_Windows_Foundation_Collections.IIterable[_struct.Windows.Foundation.Point],  # polyline
                                   _Pointer[_struct.Windows.Foundation.Rect]],  # invalidatedRectangle
                                  _type.HRESULT]
    SelectWithLine: _Callable[[_struct.Windows.Foundation.Point,  # from
                               _struct.Windows.Foundation.Point,  # to
                               _Pointer[_struct.Windows.Foundation.Rect]],  # invalidatedRectangle
                              _type.HRESULT]
    CopySelectedToClipboard: _Callable[[],
                                       _type.HRESULT]
    PasteFromClipboard: _Callable[[_struct.Windows.Foundation.Point,  # position
                                   _Pointer[_struct.Windows.Foundation.Rect]],  # invalidatedRectangle
                                  _type.HRESULT]
    CanPasteFromClipboard: _Callable[[_Pointer[_type.boolean]],  # canPaste
                                     _type.HRESULT]
    LoadAsync: _Callable[[_Windows_Storage_Streams.IInputStream,  # inputStream
                          _Pointer[_Windows_Foundation.IAsyncActionWithProgress[_type.UINT64]]],  # loadAction
                         _type.HRESULT]
    SaveAsync: _Callable[[_Windows_Storage_Streams.IOutputStream,  # outputStream
                          _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT32, _type.UINT32]]],  # outputStreamOperation
                         _type.HRESULT]
    UpdateRecognitionResults: _Callable[[_Windows_Foundation_Collections.IVectorView[IInkRecognitionResult]],  # recognitionResults
                                        _type.HRESULT]
    GetStrokes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkStroke]]],  # strokeView
                          _type.HRESULT]
    GetRecognitionResults: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkRecognitionResult]]],  # recognitionResults
                                     _type.HRESULT]


class IInkStrokeContainer2(_inspectable.IInspectable):
    AddStrokes: _Callable[[_Windows_Foundation_Collections.IIterable[IInkStroke]],  # strokes
                          _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class IInkStrokeContainer3(_inspectable.IInspectable):
    SaveWithFormatAsync: _Callable[[_Windows_Storage_Streams.IOutputStream,  # outputStream
                                    _enum.Windows.UI.Input.Inking.InkPersistenceFormat,  # inkPersistenceFormat
                                    _Pointer[_Windows_Foundation.IAsyncOperationWithProgress[_type.UINT32, _type.UINT32]]],  # outputStreamOperation
                                   _type.HRESULT]
    GetStrokeById: _Callable[[_type.UINT32,  # id
                              _Pointer[IInkStroke]],  # stroke
                             _type.HRESULT]


class IInkStrokeInput(_inspectable.IInspectable):
    add_StrokeStarted: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkStrokeInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_StrokeStarted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_StrokeContinued: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkStrokeInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_StrokeContinued: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_StrokeEnded: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkStrokeInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                               _type.HRESULT]
    remove_StrokeEnded: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    add_StrokeCanceled: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkStrokeInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_StrokeCanceled: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    get_InkPresenter: _Callable[[_Pointer[IInkPresenter]],  # value
                                _type.HRESULT]


class IInkStrokeRenderingSegment(_inspectable.IInspectable):
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]
    get_BezierControlPoint1: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                       _type.HRESULT]
    get_BezierControlPoint2: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                                       _type.HRESULT]
    get_Pressure: _Callable[[_Pointer[_type.FLOAT]],  # value
                            _type.HRESULT]
    get_TiltX: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_TiltY: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]
    get_Twist: _Callable[[_Pointer[_type.FLOAT]],  # value
                         _type.HRESULT]


class IInkStrokesCollectedEventArgs(_inspectable.IInspectable):
    get_Strokes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkStroke]]],  # value
                           _type.HRESULT]


class IInkStrokesErasedEventArgs(_inspectable.IInspectable):
    get_Strokes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkStroke]]],  # value
                           _type.HRESULT]


class IInkSynchronizer(_inspectable.IInspectable):
    BeginDry: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[IInkStroke]]],  # inkStrokes
                        _type.HRESULT]
    EndDry: _Callable[[],
                      _type.HRESULT]


class IInkUnprocessedInput(_inspectable.IInspectable):
    add_PointerEntered: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkUnprocessedInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerEntered: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerHovered: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkUnprocessedInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerHovered: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerExited: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkUnprocessedInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_PointerExited: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_PointerPressed: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkUnprocessedInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerPressed: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerMoved: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkUnprocessedInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                 _Pointer[_struct.EventRegistrationToken]],  # cookie
                                _type.HRESULT]
    remove_PointerMoved: _Callable[[_struct.EventRegistrationToken],  # cookie
                                   _type.HRESULT]
    add_PointerReleased: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkUnprocessedInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_PointerReleased: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_PointerLost: _Callable[[_Windows_Foundation.ITypedEventHandler[IInkUnprocessedInput, _Windows_UI_Core.IPointerEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                               _type.HRESULT]
    remove_PointerLost: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    get_InkPresenter: _Callable[[_Pointer[IInkPresenter]],  # value
                                _type.HRESULT]


class IPenAndInkSettings(_inspectable.IInspectable):
    get_IsHandwritingDirectlyIntoTextFieldEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                             _type.HRESULT]
    get_PenHandedness: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.PenHandedness]],  # value
                                 _type.HRESULT]
    get_HandwritingLineHeight: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.HandwritingLineHeight]],  # value
                                         _type.HRESULT]
    get_FontFamilyName: _Callable[[_Pointer[_type.HSTRING]],  # value
                                  _type.HRESULT]
    get_UserConsentsToHandwritingTelemetryCollection: _Callable[[_Pointer[_type.boolean]],  # value
                                                                _type.HRESULT]
    get_IsTouchHandwritingEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                             _type.HRESULT]


class IPenAndInkSettings2(_inspectable.IInspectable):
    SetPenHandedness: _Callable[[_enum.Windows.UI.Input.Inking.PenHandedness],  # value
                                _type.HRESULT]


class IPenAndInkSettingsStatics(_inspectable.IInspectable):
    GetDefault: _Callable[[_Pointer[IPenAndInkSettings]],  # result
                          _type.HRESULT]

    _factory = True
