from __future__ import annotations as _

from typing import Callable as _Callable

from . import d3d11 as _d3d11
from . import d3d11_1 as _d3d11_1
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class ID3D11DeviceContext2(_d3d11_1.ID3D11DeviceContext1):
    UpdateTileMappings: _Callable[[_d3d11.ID3D11Resource,  # pTiledResource
                                   _type.UINT,  # NumTiledResourceRegions
                                   _Pointer[_struct.D3D11_TILED_RESOURCE_COORDINATE],  # pTiledResourceRegionStartCoordinates
                                   _Pointer[_struct.D3D11_TILE_REGION_SIZE],  # pTiledResourceRegionSizes
                                   _d3d11.ID3D11Buffer,  # pTilePool
                                   _type.UINT,  # NumRanges
                                   _Pointer[_type.UINT],  # pRangeFlags
                                   _Pointer[_type.UINT],  # pTilePoolStartOffsets
                                   _Pointer[_type.UINT],  # pRangeTileCounts
                                   _type.UINT],  # Flags
                                  _type.HRESULT]
    CopyTileMappings: _Callable[[_d3d11.ID3D11Resource,  # pDestTiledResource
                                 _Pointer[_struct.D3D11_TILED_RESOURCE_COORDINATE],  # pDestRegionStartCoordinate
                                 _d3d11.ID3D11Resource,  # pSourceTiledResource
                                 _Pointer[_struct.D3D11_TILED_RESOURCE_COORDINATE],  # pSourceRegionStartCoordinate
                                 _Pointer[_struct.D3D11_TILE_REGION_SIZE],  # pTileRegionSize
                                 _type.UINT],  # Flags
                                _type.HRESULT]
    CopyTiles: _Callable[[_d3d11.ID3D11Resource,  # pTiledResource
                          _Pointer[_struct.D3D11_TILED_RESOURCE_COORDINATE],  # pTileRegionStartCoordinate
                          _Pointer[_struct.D3D11_TILE_REGION_SIZE],  # pTileRegionSize
                          _d3d11.ID3D11Buffer,  # pBuffer
                          _type.UINT64,  # BufferStartOffsetInBytes
                          _type.UINT],  # Flags
                         _type.c_void]
    UpdateTiles: _Callable[[_d3d11.ID3D11Resource,  # pDestTiledResource
                            _Pointer[_struct.D3D11_TILED_RESOURCE_COORDINATE],  # pDestTileRegionStartCoordinate
                            _Pointer[_struct.D3D11_TILE_REGION_SIZE],  # pDestTileRegionSize
                            _type.c_void_p,  # pSourceTileData
                            _type.UINT],  # Flags
                           _type.c_void]
    ResizeTilePool: _Callable[[_d3d11.ID3D11Buffer,  # pTilePool
                               _type.UINT64],  # NewSizeInBytes
                              _type.HRESULT]
    TiledResourceBarrier: _Callable[[_d3d11.ID3D11DeviceChild,  # pTiledResourceOrViewAccessBeforeBarrier
                                     _d3d11.ID3D11DeviceChild],  # pTiledResourceOrViewAccessAfterBarrier
                                    _type.c_void]
    IsAnnotationEnabled: _Callable[[],
                                   _type.BOOL]
    SetMarkerInt: _Callable[[_type.LPCWSTR,  # pLabel
                             _type.INT],  # Data
                            _type.c_void]
    BeginEventInt: _Callable[[_type.LPCWSTR,  # pLabel
                              _type.INT],  # Data
                             _type.c_void]
    EndEvent: _Callable[[],
                        _type.c_void]


class ID3D11Device2(_d3d11_1.ID3D11Device1):
    GetImmediateContext2: _Callable[[_Pointer[ID3D11DeviceContext2]],  # ppImmediateContext
                                    _type.c_void]
    CreateDeferredContext2: _Callable[[_type.UINT,  # ContextFlags
                                       _Pointer[ID3D11DeviceContext2]],  # ppDeferredContext
                                      _type.HRESULT]
    GetResourceTiling: _Callable[[_d3d11.ID3D11Resource,  # pTiledResource
                                  _Pointer[_type.UINT],  # pNumTilesForEntireResource
                                  _Pointer[_struct.D3D11_PACKED_MIP_DESC],  # pPackedMipDesc
                                  _Pointer[_struct.D3D11_TILE_SHAPE],  # pStandardTileShapeForNonPackedMips
                                  _Pointer[_type.UINT],  # pNumSubresourceTilings
                                  _type.UINT,  # FirstSubresourceTilingToGet
                                  _Pointer[_struct.D3D11_SUBRESOURCE_TILING]],  # pSubresourceTilingsForNonPackedMips
                                 _type.c_void]
    CheckMultisampleQualityLevels1: _Callable[[_enum.DXGI_FORMAT,  # Format
                                               _type.UINT,  # SampleCount
                                               _type.UINT,  # Flags
                                               _Pointer[_type.UINT]],  # pNumQualityLevels
                                              _type.HRESULT]
