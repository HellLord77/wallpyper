from __future__ import annotations

from typing import Callable as _Callable

from ... import Core as _Windows_UI_Core
from ... import Input as _Windows_UI_Input
from .... import System as _Windows_System
from ....ApplicationModel import Core as _Windows_ApplicationModel_Core
from ..... import inspectable as _inspectable
from ....... import type as _type
from ......._utils import _Pointer


class IRadialControllerIndependentInputSource(_inspectable.IInspectable):
    get_Controller: _Callable[[_Pointer[_Windows_UI_Input.IRadialController]],  # value
                              _type.HRESULT]
    get_Dispatcher: _Callable[[_Pointer[_Windows_UI_Core.ICoreDispatcher]],  # value
                              _type.HRESULT]


class IRadialControllerIndependentInputSource2(_inspectable.IInspectable):
    get_DispatcherQueue: _Callable[[_Pointer[_Windows_System.IDispatcherQueue]],  # value
                                   _type.HRESULT]


class IRadialControllerIndependentInputSourceStatics(_inspectable.IInspectable, factory=True):
    CreateForView: _Callable[[_Windows_ApplicationModel_Core.ICoreApplicationView,  # view
                              _Pointer[IRadialControllerIndependentInputSource]],  # result
                             _type.HRESULT]
