from __future__ import annotations

from typing import Callable as _Callable

from . import dxgi as _dxgi
from . import dxgi1_2 as _dxgi1_2
from . import dxgi1_3 as _dxgi1_3
from . import dxgi1_4 as _dxgi1_4
from ..um import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import type as _type
from ..._utils import _Pointer


class IDXGIOutput5(_dxgi1_4.IDXGIOutput4):
    DuplicateOutput1: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                 _type.UINT,  # Flags
                                 _type.UINT,  # SupportedFormatsCount
                                 _Pointer[_enum.DXGI_FORMAT],  # pSupportedFormats
                                 _Pointer[_dxgi1_2.IDXGIOutputDuplication]],  # ppOutputDuplication
                                _type.HRESULT]


class IDXGISwapChain4(_dxgi1_4.IDXGISwapChain3):
    SetHDRMetaData: _Callable[[_enum.DXGI_HDR_METADATA_TYPE,  # Type
                               _type.UINT,  # Size
                               _type.c_void_p],  # pMetaData
                              _type.HRESULT]


class IDXGIDevice4(_dxgi1_3.IDXGIDevice3):
    OfferResources1: _Callable[[_type.UINT,  # NumResources
                                _Pointer[_dxgi.IDXGIResource],  # ppResources
                                _enum.DXGI_OFFER_RESOURCE_PRIORITY,  # Priority
                                _type.UINT],  # Flags
                               _type.HRESULT]
    ReclaimResources1: _Callable[[_type.UINT,  # NumResources
                                  _Pointer[_dxgi.IDXGIResource],  # ppResources
                                  _Pointer[_enum.DXGI_RECLAIM_RESOURCE_RESULTS]],  # pResults
                                 _type.HRESULT]


class IDXGIFactory5(_dxgi1_4.IDXGIFactory4):
    CheckFeatureSupport: _Callable[[_enum.DXGI_FEATURE,  # Feature
                                    _type.c_void_p,  # pFeatureSupportData
                                    _type.UINT],  # FeatureSupportDataSize
                                   _type.HRESULT]
