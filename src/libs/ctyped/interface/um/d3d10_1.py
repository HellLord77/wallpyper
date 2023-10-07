from __future__ import annotations as _

from typing import Callable as _Callable

from . import d3d10 as _d3d10
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D10BlendState1(_d3d10.ID3D10BlendState):
    GetDesc1: _Callable[[_Pointer[_struct.D3D10_BLEND_DESC1]],  # pDesc
                        _type.c_void]


class ID3D10ShaderResourceView1(_d3d10.ID3D10ShaderResourceView):
    GetDesc1: _Callable[[_Pointer[_struct.D3D10_SHADER_RESOURCE_VIEW_DESC1]],  # pDesc
                        _type.c_void]


class ID3D10Device1(_d3d10.ID3D10Device):
    CreateShaderResourceView1: _Callable[[_d3d10.ID3D10Resource,  # pResource
                                          _Pointer[_struct.D3D10_SHADER_RESOURCE_VIEW_DESC1],  # pDesc
                                          _Pointer[ID3D10ShaderResourceView1]],  # ppSRView
                                         _type.HRESULT]
    CreateBlendState1: _Callable[[_Pointer[_struct.D3D10_BLEND_DESC1],  # pBlendStateDesc
                                  _Pointer[ID3D10BlendState1]],  # ppBlendState
                                 _type.HRESULT]
    GetFeatureLevel: _Callable[[],
                               _enum.D3D10_FEATURE_LEVEL1]
