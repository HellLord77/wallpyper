from __future__ import annotations

from typing import Callable as _Callable

from ... import Contacts as _Windows_ApplicationModel_Contacts
from ... import DataTransfer as _Windows_ApplicationModel_DataTransfer
from ....Foundation import Collections as _Windows_Foundation_Collections
from ....Storage import Streams as _Windows_Storage_Streams
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IQuickLink(_inspectable.IInspectable):
    get_Title: _Callable[[_Pointer[_type.HSTRING]],  # value
                         _type.HRESULT]
    put_Title: _Callable[[_type.HSTRING],  # value
                         _type.HRESULT]
    get_Thumbnail: _Callable[[_Pointer[_Windows_Storage_Streams.IRandomAccessStreamReference]],  # value
                             _type.HRESULT]
    put_Thumbnail: _Callable[[_Windows_Storage_Streams.IRandomAccessStreamReference],  # value
                             _type.HRESULT]
    get_Id: _Callable[[_Pointer[_type.HSTRING]],  # value
                      _type.HRESULT]
    put_Id: _Callable[[_type.HSTRING],  # value
                      _type.HRESULT]
    get_SupportedDataFormats: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                        _type.HRESULT]
    get_SupportedFileTypes: _Callable[[_Pointer[_Windows_Foundation_Collections.IVector[_type.HSTRING]]],  # value
                                      _type.HRESULT]


class IShareOperation(_inspectable.IInspectable):
    get_Data: _Callable[[_Pointer[_Windows_ApplicationModel_DataTransfer.IDataPackageView]],  # value
                        _type.HRESULT]
    get_QuickLinkId: _Callable[[_Pointer[_type.HSTRING]],  # value
                               _type.HRESULT]
    RemoveThisQuickLink: _Callable[[],
                                   _type.HRESULT]
    ReportStarted: _Callable[[],
                             _type.HRESULT]
    ReportDataRetrieved: _Callable[[],
                                   _type.HRESULT]
    ReportSubmittedBackgroundTask: _Callable[[],
                                             _type.HRESULT]
    ReportCompletedWithQuickLink: _Callable[[IQuickLink],  # quicklink
                                            _type.HRESULT]
    ReportCompleted: _Callable[[],
                               _type.HRESULT]
    ReportError: _Callable[[_type.HSTRING],  # value
                           _type.HRESULT]


class IShareOperation2(_inspectable.IInspectable):
    DismissUI: _Callable[[],
                         _type.HRESULT]


class IShareOperation3(_inspectable.IInspectable):
    get_Contacts: _Callable[[_Pointer[_Windows_Foundation_Collections.IVectorView[_Windows_ApplicationModel_Contacts.IContact]]],  # value
                            _type.HRESULT]
