from __future__ import annotations as _

from typing import Callable as _Callable

from ..um import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ... import union as _union
from ..._utils import _Pointer


class IDXGIObject(_Unknwnbase.IUnknown):
    SetPrivateData: _Callable[[_Pointer[_struct.GUID],  # Name
                               _type.UINT,  # DataSize
                               _type.c_void_p],  # pData
                              _type.HRESULT]
    SetPrivateDataInterface: _Callable[[_Pointer[_struct.GUID],  # Name
                                        _Unknwnbase.IUnknown],  # pUnknown
                                       _type.HRESULT]
    GetPrivateData: _Callable[[_Pointer[_struct.GUID],  # Name
                               _Pointer[_type.UINT],  # pDataSize
                               _type.c_void_p],  # pData
                              _type.HRESULT]
    GetParent: _Callable[[_Pointer[_struct.IID],  # riid
                          _type.c_void_p],  # ppParent
                         _type.HRESULT]


class IDXGIDeviceSubObject(IDXGIObject):
    GetDevice: _Callable[[_Pointer[_struct.IID],  # riid
                          _type.c_void_p],  # ppDevice
                         _type.HRESULT]


class IDXGIResource(IDXGIDeviceSubObject):
    GetSharedHandle: _Callable[[_Pointer[_type.HANDLE]],  # pSharedHandle
                               _type.HRESULT]
    GetUsage: _Callable[[_Pointer[_type.DXGI_USAGE]],  # pUsage
                        _type.HRESULT]
    SetEvictionPriority: _Callable[[_type.UINT],  # EvictionPriority
                                   _type.HRESULT]
    GetEvictionPriority: _Callable[[_Pointer[_type.UINT]],  # pEvictionPriority
                                   _type.HRESULT]


class IDXGIKeyedMutex(IDXGIDeviceSubObject):
    AcquireSync: _Callable[[_type.UINT64,  # Key
                            _type.DWORD],  # dwMilliseconds
                           _type.HRESULT]
    ReleaseSync: _Callable[[_type.UINT64],  # Key
                           _type.HRESULT]


class IDXGISurface(IDXGIDeviceSubObject):
    GetDesc: _Callable[[_Pointer[_struct.DXGI_SURFACE_DESC]],  # pDesc
                       _type.HRESULT]
    Map: _Callable[[_Pointer[_struct.DXGI_MAPPED_RECT],  # pLockedRect
                    _type.UINT],  # MapFlags
                   _type.HRESULT]
    Unmap: _Callable[[],
                     _type.HRESULT]


class IDXGISurface1(IDXGISurface):
    GetDC: _Callable[[_type.BOOL,  # Discard
                      _Pointer[_type.HDC]],  # phdc
                     _type.HRESULT]
    ReleaseDC: _Callable[[_Pointer[_struct.RECT]],  # pDirtyRect
                         _type.HRESULT]


class IDXGIAdapter(IDXGIObject):
    EnumOutputs: _Callable[[_type.UINT,  # Output
                            _Pointer[IDXGIOutput]],  # ppOutput
                           _type.HRESULT]
    GetDesc: _Callable[[_Pointer[_struct.DXGI_ADAPTER_DESC]],  # pDesc
                       _type.HRESULT]
    CheckInterfaceSupport: _Callable[[_Pointer[_struct.GUID],  # InterfaceName
                                      _Pointer[_union.LARGE_INTEGER]],  # pUMDVersion
                                     _type.HRESULT]


class IDXGIOutput(IDXGIObject):
    GetDesc: _Callable[[_Pointer[_struct.DXGI_OUTPUT_DESC]],  # pDesc
                       _type.HRESULT]
    GetDisplayModeList: _Callable[[_enum.DXGI_FORMAT,  # EnumFormat
                                   _type.UINT,  # Flags
                                   _Pointer[_type.UINT],  # pNumModes
                                   _Pointer[_struct.DXGI_MODE_DESC]],  # pDesc
                                  _type.HRESULT]
    FindClosestMatchingMode: _Callable[[_Pointer[_struct.DXGI_MODE_DESC],  # pModeToMatch
                                        _Pointer[_struct.DXGI_MODE_DESC],  # pClosestMatch
                                        _Unknwnbase.IUnknown],  # pConcernedDevice
                                       _type.HRESULT]
    WaitForVBlank: _Callable[[],
                             _type.HRESULT]
    TakeOwnership: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                              _type.BOOL],  # Exclusive
                             _type.HRESULT]
    ReleaseOwnership: _Callable[[],
                                _type.c_void]
    GetGammaControlCapabilities: _Callable[[_Pointer[_struct.DXGI_GAMMA_CONTROL_CAPABILITIES]],  # pGammaCaps
                                           _type.HRESULT]
    SetGammaControl: _Callable[[_Pointer[_struct.DXGI_GAMMA_CONTROL]],  # pArray
                               _type.HRESULT]
    GetGammaControl: _Callable[[_Pointer[_struct.DXGI_GAMMA_CONTROL]],  # pArray
                               _type.HRESULT]
    SetDisplaySurface: _Callable[[IDXGISurface],  # pScanoutSurface
                                 _type.HRESULT]
    GetDisplaySurfaceData: _Callable[[IDXGISurface],  # pDestination
                                     _type.HRESULT]
    GetFrameStatistics: _Callable[[_Pointer[_struct.DXGI_FRAME_STATISTICS]],  # pStats
                                  _type.HRESULT]


class IDXGISwapChain(IDXGIDeviceSubObject):
    Present: _Callable[[_type.UINT,  # SyncInterval
                        _type.UINT],  # Flags
                       _type.HRESULT]
    GetBuffer: _Callable[[_type.UINT,  # Buffer
                          _Pointer[_struct.IID],  # riid
                          _type.c_void_p],  # ppSurface
                         _type.HRESULT]
    SetFullscreenState: _Callable[[_type.BOOL,  # Fullscreen
                                   IDXGIOutput],  # pTarget
                                  _type.HRESULT]
    GetFullscreenState: _Callable[[_Pointer[_type.BOOL],  # pFullscreen
                                   _Pointer[IDXGIOutput]],  # ppTarget
                                  _type.HRESULT]
    GetDesc: _Callable[[_Pointer[_struct.DXGI_SWAP_CHAIN_DESC]],  # pDesc
                       _type.HRESULT]
    ResizeBuffers: _Callable[[_type.UINT,  # BufferCount
                              _type.UINT,  # Width
                              _type.UINT,  # Height
                              _enum.DXGI_FORMAT,  # NewFormat
                              _type.UINT],  # SwapChainFlags
                             _type.HRESULT]
    ResizeTarget: _Callable[[_Pointer[_struct.DXGI_MODE_DESC]],  # pNewTargetParameters
                            _type.HRESULT]
    GetContainingOutput: _Callable[[_Pointer[IDXGIOutput]],  # ppOutput
                                   _type.HRESULT]
    GetFrameStatistics: _Callable[[_Pointer[_struct.DXGI_FRAME_STATISTICS]],  # pStats
                                  _type.HRESULT]
    GetLastPresentCount: _Callable[[_Pointer[_type.UINT]],  # pLastPresentCount
                                   _type.HRESULT]


class IDXGIFactory(IDXGIObject):
    EnumAdapters: _Callable[[_type.UINT,  # Adapter
                             _Pointer[IDXGIAdapter]],  # ppAdapter
                            _type.HRESULT]
    MakeWindowAssociation: _Callable[[_type.HWND,  # WindowHandle
                                      _type.UINT],  # Flags
                                     _type.HRESULT]
    GetWindowAssociation: _Callable[[_Pointer[_type.HWND]],  # pWindowHandle
                                    _type.HRESULT]
    CreateSwapChain: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                _Pointer[_struct.DXGI_SWAP_CHAIN_DESC],  # pDesc
                                _Pointer[IDXGISwapChain]],  # ppSwapChain
                               _type.HRESULT]
    CreateSoftwareAdapter: _Callable[[_type.HMODULE,  # Module
                                      _Pointer[IDXGIAdapter]],  # ppAdapter
                                     _type.HRESULT]


class IDXGIDevice(IDXGIObject):
    GetAdapter: _Callable[[_Pointer[IDXGIAdapter]],  # pAdapter
                          _type.HRESULT]
    CreateSurface: _Callable[[_Pointer[_struct.DXGI_SURFACE_DESC],  # pDesc
                              _type.UINT,  # NumSurfaces
                              _type.DXGI_USAGE,  # Usage
                              _Pointer[_struct.DXGI_SHARED_RESOURCE],  # pSharedResource
                              _Pointer[IDXGISurface]],  # ppSurface
                             _type.HRESULT]
    QueryResourceResidency: _Callable[[_Pointer[_Unknwnbase.IUnknown],  # ppResources
                                       _Pointer[_enum.DXGI_RESIDENCY],  # pResidencyStatus
                                       _type.UINT],  # NumResources
                                      _type.HRESULT]
    SetGPUThreadPriority: _Callable[[_type.INT],  # Priority
                                    _type.HRESULT]
    GetGPUThreadPriority: _Callable[[_Pointer[_type.INT]],  # pPriority
                                    _type.HRESULT]


class IDXGIFactory1(IDXGIFactory):
    EnumAdapters1: _Callable[[_type.UINT,  # Adapter
                              _Pointer[IDXGIAdapter1]],  # ppAdapter
                             _type.HRESULT]
    IsCurrent: _Callable[[],
                         _type.BOOL]


class IDXGIAdapter1(IDXGIAdapter):
    GetDesc1: _Callable[[_Pointer[_struct.DXGI_ADAPTER_DESC1]],  # pDesc
                        _type.HRESULT]


class IDXGIDevice1(IDXGIDevice):
    SetMaximumFrameLatency: _Callable[[_type.UINT],  # MaxLatency
                                      _type.HRESULT]
    GetMaximumFrameLatency: _Callable[[_Pointer[_type.UINT]],  # pMaxLatency
                                      _type.HRESULT]
