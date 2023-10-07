from __future__ import annotations as _

from typing import Callable as _Callable

from .... import Foundation as _Windows_Foundation
from ....Graphics import Imaging as _Windows_Graphics_Imaging
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IInkWorkspaceHostedAppManager(_inspectable.IInspectable):
    SetThumbnailAsync: _Callable[[_Windows_Graphics_Imaging.ISoftwareBitmap,  # bitmap
                                  _Pointer[_Windows_Foundation.IAsyncAction]],  # action
                                 _type.HRESULT]


class IInkWorkspaceHostedAppManagerStatics(_inspectable.IInspectable, factory=True):
    GetForCurrentApp: _Callable[[_Pointer[IInkWorkspaceHostedAppManager]],  # current
                                _type.HRESULT]
