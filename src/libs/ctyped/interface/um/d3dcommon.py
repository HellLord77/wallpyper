from __future__ import annotations

from typing import Callable as _Callable

from . import Unknwnbase as _Unknwnbase
from ... import type as _type
from ..._utils import _Pointer


class ID3D10Blob(_Unknwnbase.IUnknown):
    GetBufferPointer: _Callable[[],
                                _type.LPVOID]
    GetBufferSize: _Callable[[],
                             _type.SIZE_T]


class ID3DDestructionNotifier(_Unknwnbase.IUnknown):
    RegisterDestructionCallback: _Callable[[_type.PFN_DESTRUCTION_CALLBACK,  # callbackFn
                                            _type.c_void_p,  # pData
                                            _Pointer[_type.UINT]],  # pCallbackID
                                           _type.HRESULT]
    UnregisterDestructionCallback: _Callable[[_type.UINT],  # callbackID
                                             _type.HRESULT]
