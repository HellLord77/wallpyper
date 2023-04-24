from __future__ import annotations

from typing import Callable as _Callable

from ... import Xaml as _Windows_UI_Xaml
from ....Graphics import Printing as _Windows_Graphics_Printing
from ..... import inspectable as _inspectable
from ......um import Unknwnbase as _Unknwnbase
from ....... import enum as _enum
from ....... import struct as _struct
from ....... import type as _type
from ......._utils import _Pointer


class _IAddPagesEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IAddPagesEventArgs],  # e
                      _type.HRESULT]


class IAddPagesEventHandler(_IAddPagesEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IAddPagesEventHandler_impl(_IAddPagesEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IGetPreviewPageEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IGetPreviewPageEventArgs],  # e
                      _type.HRESULT]


class IGetPreviewPageEventHandler(_IGetPreviewPageEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IGetPreviewPageEventHandler_impl(_IGetPreviewPageEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class _IPaginateEventHandler:
    Invoke: _Callable[[_inspectable.IInspectable,  # sender
                       IPaginateEventArgs],  # e
                      _type.HRESULT]


class IPaginateEventHandler(_IPaginateEventHandler, _Unknwnbase.IUnknown):
    pass


# noinspection PyPep8Naming
class IPaginateEventHandler_impl(_IPaginateEventHandler, _Unknwnbase.IUnknown_impl):
    pass


class IAddPagesEventArgs(_inspectable.IInspectable):
    get_PrintTaskOptions: _Callable[[_Pointer[_Windows_Graphics_Printing.IPrintTaskOptionsCore]],  # value
                                    _type.HRESULT]


class IGetPreviewPageEventArgs(_inspectable.IInspectable):
    get_PageNumber: _Callable[[_Pointer[_type.INT32]],  # value
                              _type.HRESULT]


class IPaginateEventArgs(_inspectable.IInspectable):
    get_PrintTaskOptions: _Callable[[_Pointer[_Windows_Graphics_Printing.IPrintTaskOptionsCore]],  # value
                                    _type.HRESULT]
    get_CurrentPreviewPageNumber: _Callable[[_Pointer[_type.INT32]],  # value
                                            _type.HRESULT]


class IPrintDocument(_inspectable.IInspectable):
    get_DocumentSource: _Callable[[_Pointer[_Windows_Graphics_Printing.IPrintDocumentSource]],  # value
                                  _type.HRESULT]
    add_Paginate: _Callable[[IPaginateEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_Paginate: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    add_GetPreviewPage: _Callable[[IGetPreviewPageEventHandler,  # handler
                                   _Pointer[_struct.EventRegistrationToken]],  # token
                                  _type.HRESULT]
    remove_GetPreviewPage: _Callable[[_struct.EventRegistrationToken],  # token
                                     _type.HRESULT]
    add_AddPages: _Callable[[IAddPagesEventHandler,  # handler
                             _Pointer[_struct.EventRegistrationToken]],  # token
                            _type.HRESULT]
    remove_AddPages: _Callable[[_struct.EventRegistrationToken],  # token
                               _type.HRESULT]
    AddPage: _Callable[[_Windows_UI_Xaml.IUIElement],  # pageVisual
                       _type.HRESULT]
    AddPagesComplete: _Callable[[],
                                _type.HRESULT]
    SetPreviewPageCount: _Callable[[_type.INT32,  # count
                                    _enum.Windows.UI.Xaml.Printing.PreviewPageCountType],  # type
                                   _type.HRESULT]
    SetPreviewPage: _Callable[[_type.INT32,  # pageNumber
                               _Windows_UI_Xaml.IUIElement],  # pageVisual
                              _type.HRESULT]
    InvalidatePreview: _Callable[[],
                                 _type.HRESULT]


class IPrintDocumentFactory(_inspectable.IInspectable):
    CreateInstance: _Callable[[_inspectable.IInspectable,  # baseInterface
                               _Pointer[_inspectable.IInspectable],  # innerInterface
                               _Pointer[IPrintDocument]],  # value
                              _type.HRESULT]


class IPrintDocumentStatics(_inspectable.IInspectable):
    get_DocumentSourceProperty: _Callable[[_Pointer[_Windows_UI_Xaml.IDependencyProperty]],  # value
                                          _type.HRESULT]

    _factory = True
