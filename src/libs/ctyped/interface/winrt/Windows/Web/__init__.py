from __future__ import annotations as _

from typing import Callable as _Callable

from .. import Foundation as _Windows_Foundation
from ..Storage import Streams as _Windows_Storage_Streams
from ... import inspectable as _inspectable
from ..... import enum as _enum
from ..... import type as _type
from ....._utils import _Pointer


class IUriToStreamResolver(_inspectable.IInspectable):
    UriToStreamAsync: _Callable[[_Windows_Foundation.IUriRuntimeClass,  # uri
                                 _Pointer[_Windows_Foundation.IAsyncOperation[_Windows_Storage_Streams.IInputStream]]],  # operation
                                _type.HRESULT]


class IWebErrorStatics(_inspectable.IInspectable):
    GetStatus: _Callable[[_type.INT32,  # hresult
                          _Pointer[_enum.Windows.Web.WebErrorStatus]],  # status
                         _type.HRESULT]

    _factory = True
