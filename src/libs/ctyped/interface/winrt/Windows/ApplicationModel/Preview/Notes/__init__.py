from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Graphics import Imaging as _Windows_Graphics_Imaging
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class INotePlacementChangedPreviewEventArgs(_inspectable.IInspectable):
    get_ViewId: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]


class INoteVisibilityChangedPreviewEventArgs(_inspectable.IInspectable):
    get_ViewId: _Callable[[_Pointer[_type.INT32]],  # value
                          _type.HRESULT]
    get_IsVisible: _Callable[[_Pointer[_type.boolean]],  # value
                             _type.HRESULT]


class INotesWindowManagerPreview(_inspectable.IInspectable):
    get_IsScreenLocked: _Callable[[_Pointer[_type.boolean]],  # value
                                  _type.HRESULT]
    ShowNote: _Callable[[_type.INT32],  # noteViewId
                        _type.HRESULT]
    ShowNoteRelativeTo: _Callable[[_type.INT32,  # noteViewId
                                   _type.INT32],  # anchorNoteViewId
                                  _type.HRESULT]
    ShowNoteWithPlacement: _Callable[[_type.INT32,  # noteViewId
                                      _Windows_Storage_Streams.IBuffer],  # data
                                     _type.HRESULT]
    HideNote: _Callable[[_type.INT32],  # noteViewId
                        _type.HRESULT]
    GetNotePlacement: _Callable[[_type.INT32,  # noteViewId
                                 _Pointer[_Windows_Storage_Streams.IBuffer]],  # data
                                _type.HRESULT]
    TrySetNoteSize: _Callable[[_type.INT32,  # noteViewId
                               _struct.Windows.Foundation.Size,  # size
                               _Pointer[_type.boolean]],  # succeeded
                              _type.HRESULT]
    SetFocusToNextView: _Callable[[],
                                  _type.HRESULT]
    SetNotesThumbnailAsync: _Callable[[_Windows_Storage_Streams.IBuffer,  # thumbnail
                                       _Pointer[_Windows_Foundation.IAsyncAction]],  # operation
                                      _type.HRESULT]
    add_SystemLockStateChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[INotesWindowManagerPreview, _inspectable.IInspectable],  # handler
                                           _Pointer[_struct.EventRegistrationToken]],  # token
                                          _type.HRESULT]
    remove_SystemLockStateChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                             _type.HRESULT]
    add_NotePlacementChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[INotesWindowManagerPreview, INotePlacementChangedPreviewEventArgs],  # handler
                                         _Pointer[_struct.EventRegistrationToken]],  # token
                                        _type.HRESULT]
    remove_NotePlacementChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                           _type.HRESULT]
    add_NoteVisibilityChanged: _Callable[[_Windows_Foundation.ITypedEventHandler[INotesWindowManagerPreview, INoteVisibilityChangedPreviewEventArgs],  # handler
                                          _Pointer[_struct.EventRegistrationToken]],  # token
                                         _type.HRESULT]
    remove_NoteVisibilityChanged: _Callable[[_struct.EventRegistrationToken],  # token
                                            _type.HRESULT]


class INotesWindowManagerPreview2(_inspectable.IInspectable):
    ShowNoteRelativeToWithOptions: _Callable[[_type.INT32,  # noteViewId
                                              _type.INT32,  # anchorNoteViewId
                                              INotesWindowManagerPreviewShowNoteOptions],  # options
                                             _type.HRESULT]
    ShowNoteWithPlacementWithOptions: _Callable[[_type.INT32,  # noteViewId
                                                 _Windows_Storage_Streams.IBuffer,  # data
                                                 INotesWindowManagerPreviewShowNoteOptions],  # options
                                                _type.HRESULT]
    SetFocusToPreviousView: _Callable[[],
                                      _type.HRESULT]
    SetThumbnailImageForTaskSwitcherAsync: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # bitmap
                                                      _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                                     _type.HRESULT]


class INotesWindowManagerPreviewShowNoteOptions(_inspectable.IInspectable):
    get_ShowWithFocus: _Callable[[_Pointer[_type.boolean]],  # value
                                 _type.HRESULT]
    put_ShowWithFocus: _Callable[[_type.boolean],  # value
                                 _type.HRESULT]


class INotesWindowManagerPreviewStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentApp: _Callable[[_Pointer[INotesWindowManagerPreview]],  # current
                                _type.HRESULT]
