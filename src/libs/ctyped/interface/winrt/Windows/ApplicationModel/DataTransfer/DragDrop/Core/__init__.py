from __future__ import annotations

from typing import Callable as _Callable

from .... import DataTransfer as _Windows_ApplicationModel_DataTransfer
from ..... import Foundation as _Windows_Foundation
from .....Graphics import Imaging as _Windows_Graphics_Imaging
from ...... import inspectable as _inspectable
from ........ import enum as _enum
from ........ import struct as _struct
from ........ import type as _type
from ........_utils import _Pointer


class ICoreDragDropManager(_inspectable.IInspectable):
    add_TargetRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[ICoreDragDropManager, ICoreDropOperationTargetRequestedEventArgs],  # value
                                    _Pointer[_struct.EventRegistrationToken]],  # returnValue
                                   _type.HRESULT]
    remove_TargetRequested: _Callable[[_struct.EventRegistrationToken],  # value
                                      _type.HRESULT]
    get_AreConcurrentOperationsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_AreConcurrentOperationsEnabled: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]


class ICoreDragDropManagerStatics(_inspectable.IInspectable):
    GetForCurrentView: _Callable[[_Pointer[ICoreDragDropManager]],  # value
                                 _type.HRESULT]

    _factory = True


class ICoreDragInfo(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackageView]],  # value
                        _type.HRESULT]
    get_Modifiers: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DragDrop.DragDropModifiers]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class ICoreDragInfo2(_inspectable.IInspectable):
    get_AllowedOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                     _type.HRESULT]


class ICoreDragOperation(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackage]],  # value
                        _type.HRESULT]
    SetPointerId: _Callable[[_type.UINT32],  # pointerId
                            _type.HRESULT]
    SetDragUIContentFromSoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # softwareBitmap
                                                  _type.HRESULT]
    SetDragUIContentFromSoftwareBitmapWithAnchorPoint: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # softwareBitmap
                                                                  _struct.Windows.Foundation.Point],  # anchorPoint
                                                                 _type.HRESULT]
    get_DragUIContentMode: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIContentMode]],  # value
                                     _type.HRESULT]
    put_DragUIContentMode: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIContentMode],  # value
                                     _type.HRESULT]
    StartAsync: _Callable[[_Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # value
                          _type.HRESULT]


class ICoreDragOperation2(_inspectable.IInspectable):
    get_AllowedOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                     _type.HRESULT]
    put_AllowedOperations: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation],  # value
                                     _type.HRESULT]


class ICoreDragUIOverride(_inspectable.IInspectable):
    SetContentFromSoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # softwareBitmap
                                            _type.HRESULT]
    SetContentFromSoftwareBitmapWithAnchorPoint: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # softwareBitmap
                                                            _struct.Windows.Foundation.Point],  # anchorPoint
                                                           _type.HRESULT]
    get_IsContentVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsContentVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Caption: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_IsCaptionVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsCaptionVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsGlyphVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsGlyphVisible: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]


class ICoreDropOperationTarget(_inspectable.IInspectable):
    EnterAsync: _Callable[[ICoreDragInfo,  # dragInfo
                           ICoreDragUIOverride,  # dragUIOverride
                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # returnValue
                          _type.HRESULT]
    OverAsync: _Callable[[ICoreDragInfo,  # dragInfo
                          ICoreDragUIOverride,  # dragUIOverride
                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # returnValue
                         _type.HRESULT]
    LeaveAsync: _Callable[[ICoreDragInfo,  # dragInfo
                           _Pointer[_Windows_Foundation.IAsyncAction]],  # returnValue
                          _type.HRESULT]
    DropAsync: _Callable[[ICoreDragInfo,  # dragInfo
                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # returnValue
                         _type.HRESULT]


class ICoreDropOperationTargetRequestedEventArgs(_inspectable.IInspectable):
    SetTarget: _Callable[[ICoreDropOperationTarget],  # target
                         _type.HRESULT]
