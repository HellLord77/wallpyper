from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Inking as _Windows_UI_Input_Inking
from .... import Composition as _Windows_UI_Composition
from .... import Core as _Windows_UI_Core
from ..... import Foundation as _Windows_Foundation
from .....Foundation import Collections as _Windows_Foundation_Collections
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class ICoreIncrementalInkStroke(_inspectable.IInspectable):
    AppendInkPoints: _Callable[[_Windows_Foundation_Collections.IIterable[_Windows_UI_Input_Inking.IInkPoint],  # inkPoints
                                _Pointer[_struct.Windows.Foundation.Rect]],  # result
                               _type.HRESULT]
    CreateInkStroke: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkStroke]],  # result
                               _type.HRESULT]
    get_DrawingAttributes: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkDrawingAttributes]],  # value
                                     _type.HRESULT]
    get_PointTransform: _Callable[[_Pointer[_struct.Windows.Foundation.Numerics.Matrix3x2]],  # value
                                  _type.HRESULT]
    get_BoundingRect: _Callable[[_Pointer[_struct.Windows.Foundation.Rect]],  # value
                                _type.HRESULT]


class ICoreIncrementalInkStrokeFactory(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Input_Inking.IInkDrawingAttributes,  # drawingAttributes
                       _struct.Windows.Foundation.Numerics.Matrix3x2,  # pointTransform
                       _Pointer[ICoreIncrementalInkStroke]],  # result
                      _type.HRESULT]


class ICoreInkIndependentInputSource(_inspectable.IInspectable):
    add_PointerEntering: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInkIndependentInputSource, _Windows_UI_Core.IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_PointerEntering: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_PointerHovering: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInkIndependentInputSource, _Windows_UI_Core.IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_PointerHovering: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_PointerExiting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInkIndependentInputSource, _Windows_UI_Core.IPointerEventArgs],  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # cookie
                                  _type.HRESULT]
    remove_PointerExiting: _Callable[[_struct.EventRegistrationToken],  # cookie
                                     _type.HRESULT]
    add_PointerPressing: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInkIndependentInputSource, _Windows_UI_Core.IPointerEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # cookie
                                   _type.HRESULT]
    remove_PointerPressing: _Callable[[_struct.EventRegistrationToken],  # cookie
                                      _type.HRESULT]
    add_PointerMoving: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInkIndependentInputSource, _Windows_UI_Core.IPointerEventArgs],  # handler
                                  _Pointer[_struct.EventRegistrationToken]],  # cookie
                                 _type.HRESULT]
    remove_PointerMoving: _Callable[[_struct.EventRegistrationToken],  # cookie
                                    _type.HRESULT]
    add_PointerReleasing: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInkIndependentInputSource, _Windows_UI_Core.IPointerEventArgs],  # handler
                                     _Pointer[_struct.EventRegistrationToken]],  # cookie
                                    _type.HRESULT]
    remove_PointerReleasing: _Callable[[_struct.EventRegistrationToken],  # cookie
                                       _type.HRESULT]
    add_PointerLost: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreInkIndependentInputSource, _Windows_UI_Core.IPointerEventArgs],  # handler
                                _Pointer[_struct.EventRegistrationToken]],  # cookie
                               _type.HRESULT]
    remove_PointerLost: _Callable[[_struct.EventRegistrationToken],  # cookie
                                  _type.HRESULT]
    get_InkPresenter: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenter]],  # value
                                _type.HRESULT]


class ICoreInkIndependentInputSource2(_inspectable.IInspectable):
    get_PointerCursor: _Callable[[_Pointer[_Windows_UI_Core.ICoreCursor]],  # value
                                 _type.HRESULT]
    put_PointerCursor: _Callable[[_Windows_UI_Core.ICoreCursor],  # value
                                 _type.HRESULT]


class ICoreInkIndependentInputSourceStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Input_Inking.IInkPresenter,  # inkPresenter
                       _Pointer[ICoreInkIndependentInputSource]],  # inkIndependentInputSource
                      _type.HRESULT]


class ICoreInkPresenterHost(_inspectable.IInspectable):
    get_InkPresenter: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenter]],  # value
                                _type.HRESULT]
    get_RootVisual: _Callable[[_Pointer[_Windows_UI_Composition.IContainerVisual]],  # value
                              _type.HRESULT]
    put_RootVisual: _Callable[[_Windows_UI_Composition.IContainerVisual],  # value
                              _type.HRESULT]


class ICoreWetStrokeUpdateEventArgs(_inspectable.IInspectable):
    get_NewInkPoints: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_Windows_UI_Input_Inking.IInkPoint]]],  # value
                                _type.HRESULT]
    get_PointerId: _Callable[[_Pointer[_type.UINT32]],  # value
                             _type.HRESULT]
    get_Disposition: _Callable[[_Pointer[_enum.Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition]],  # value
                               _type.HRESULT]
    put_Disposition: _Callable[[_enum.Windows.UI.Input.Inking.Core.CoreWetStrokeDisposition],  # value
                               _type.HRESULT]


class ICoreWetStrokeUpdateSource(_inspectable.IInspectable):
    add_WetStrokeStarting: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWetStrokeUpdateSource, ICoreWetStrokeUpdateEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # cookie
                                     _type.HRESULT]
    remove_WetStrokeStarting: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]
    add_WetStrokeContinuing: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWetStrokeUpdateSource, ICoreWetStrokeUpdateEventArgs],  # handler
                                        _Pointer[_struct.EventRegistrationToken]],  # cookie
                                       _type.HRESULT]
    remove_WetStrokeContinuing: _Callable[[_struct.EventRegistrationToken],  # cookie
                                          _type.HRESULT]
    add_WetStrokeStopping: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWetStrokeUpdateSource, ICoreWetStrokeUpdateEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # cookie
                                     _type.HRESULT]
    remove_WetStrokeStopping: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]
    add_WetStrokeCompleted: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWetStrokeUpdateSource, ICoreWetStrokeUpdateEventArgs],  # handler
                                       _Pointer[_struct.EventRegistrationToken]],  # cookie
                                      _type.HRESULT]
    remove_WetStrokeCompleted: _Callable[[_struct.EventRegistrationToken],  # cookie
                                         _type.HRESULT]
    add_WetStrokeCanceled: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreWetStrokeUpdateSource, ICoreWetStrokeUpdateEventArgs],  # handler
                                      _Pointer[_struct.EventRegistrationToken]],  # cookie
                                     _type.HRESULT]
    remove_WetStrokeCanceled: _Callable[[_struct.EventRegistrationToken],  # cookie
                                        _type.HRESULT]
    get_InkPresenter: _Callable[[_Pointer[_Windows_UI_Input_Inking.IInkPresenter]],  # value
                                _type.HRESULT]


class ICoreWetStrokeUpdateSourceStatics(_inspectable.IInspectable, factory=True):
    Create: _Callable[[_Windows_UI_Input_Inking.IInkPresenter,  # inkPresenter
                       _Pointer[ICoreWetStrokeUpdateSource]],  # WetStrokeUpdateSource
                      _type.HRESULT]
