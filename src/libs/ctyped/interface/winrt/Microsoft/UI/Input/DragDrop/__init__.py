from __future__ import annotations as _

from typing import Callable as _Callable

from ... import Content as _Microsoft_UI_Content
from ... import Input as _Microsoft_UI_Input
from ..... import inspectable as _inspectable
from .....Windows import Foundation as _Windows_Foundation
from .....Windows.ApplicationModel import DataTransfer as _Windows_ApplicationModel_DataTransfer
from .....Windows.Graphics import Imaging as _Windows_Graphics_Imaging
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class IDragDropManager(_inspectable.IInspectable):
    get_AreConcurrentOperationsEnabled: _Callable[[_Pointer[_type.boolean]],  # value
                                                  _type.HRESULT]
    put_AreConcurrentOperationsEnabled: _Callable[[_type.boolean],  # value
                                                  _type.HRESULT]
    add_TargetRequested: _Callable[[_Windows_Foundation.ITypedEventHandler[IDragDropManager, IDropOperationTargetRequestedEventArgs],  # handler
                                    _Pointer[_struct.EventRegistrationToken]],  # token
                                   _type.HRESULT]
    remove_TargetRequested: _Callable[[_struct.EventRegistrationToken],  # token
                                      _type.HRESULT]


class IDragDropManagerStatics(_inspectable.IInspectable, factory=True):
    GetForIsland: _Callable[[_Microsoft_UI_Content.IContentIsland,  # content
                             _Pointer[IDragDropManager]],  # result
                            _type.HRESULT]


class IDragInfo(_inspectable.IInspectable):
    get_AllowedOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                     _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackageView]],  # value
                        _type.HRESULT]
    get_Modifiers: _Callable[[_Pointer[_enum.Microsoft.UI.Input.DragDrop.DragDropModifiers]],  # value
                             _type.HRESULT]
    get_Position: _Callable[[_Pointer[_struct.Windows.Foundation.Point]],  # value
                            _type.HRESULT]


class IDragOperation(_inspectable.IInspectable):
    get_AllowedOperations: _Callable[[_Pointer[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]],  # value
                                     _type.HRESULT]
    put_AllowedOperations: _Callable[[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation],  # value
                                     _type.HRESULT]
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackage]],  # value
                        _type.HRESULT]
    get_DragUIContentMode: _Callable[[_Pointer[_enum.Microsoft.UI.Input.DragDrop.DragUIContentMode]],  # value
                                     _type.HRESULT]
    put_DragUIContentMode: _Callable[[_enum.Microsoft.UI.Input.DragDrop.DragUIContentMode],  # value
                                     _type.HRESULT]
    SetDragUIContentFromSoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # bitmap
                                                  _type.HRESULT]
    SetDragUIContentFromSoftwareBitmap2: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # bitmap
                                                    _struct.Windows.Foundation.Point],  # anchorPoint
                                                   _type.HRESULT]
    StartAsync: _Callable[[IDragDropManager,  # initialTarget
                           _Microsoft_UI_Input.IPointerPoint,  # initialPointerPoint
                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # operation
                          _type.HRESULT]


class IDragUIOverride(_inspectable.IInspectable):
    get_Caption: _Callable[[_Pointer[_type.HSTRING]],  # value
                           _type.HRESULT]
    put_Caption: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]
    get_IsCaptionVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsCaptionVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsContentVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                    _type.HRESULT]
    put_IsContentVisible: _Callable[[_type.boolean],  # value
                                    _type.HRESULT]
    get_IsGlyphVisible: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    put_IsGlyphVisible: _Callable[[_type.boolean],  # value
                                  _type.HRESULT]
    Clear: _Callable[[],
                     _type.HRESULT]
    SetContentFromSoftwareBitmap: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap],  # bitmap
                                            _type.HRESULT]
    SetContentFromSoftwareBitmap2: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # bitmap
                                              _struct.Windows.Foundation.Point],  # anchorPoint
                                             _type.HRESULT]


class IDropOperationTarget(_inspectable.IInspectable):
    DropAsync: _Callable[[IDragInfo,  # dragInfo
                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # operation
                         _type.HRESULT]
    EnterAsync: _Callable[[IDragInfo,  # dragInfo
                           IDragUIOverride,  # dragUIOverride
                           _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # operation
                          _type.HRESULT]
    LeaveAsync: _Callable[[IDragInfo,  # dragInfo
                           _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                          _type.HRESULT]
    OverAsync: _Callable[[IDragInfo,  # dragInfo
                          IDragUIOverride,  # dragUIOverride
                          _Pointer[_Windows_Foundation.IAsyncOperation[_enum.Windows.ApplicationModel.DataTransfer.DataPackageOperation]]],  # operation
                         _type.HRESULT]


class IDropOperationTargetRequestedEventArgs(_inspectable.IInspectable):
    SetTarget: _Callable[[IDropOperationTarget],  # target
                         _type.HRESULT]
