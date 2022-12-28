from __future__ import annotations as _

from typing import Callable as _Callable

from . import dxgi as _dxgi
from ..um import Unknwnbase as _Unknwnbase
from ... import enum as _enum
from ... import struct as _struct
from ... import type as _type
from ..._utils import _Pointer


class IDXGIDisplayControl(_Unknwnbase.IUnknown):
    IsStereoEnabled: _Callable[[],
                               _type.BOOL]
    SetStereoEnabled: _Callable[[_type.BOOL],  # enabled
                                _type.c_void]


class IDXGIOutputDuplication(_dxgi.IDXGIObject):
    GetDesc: _Callable[[_Pointer[_struct.DXGI_OUTDUPL_DESC]],  # pDesc
                       _type.c_void]
    AcquireNextFrame: _Callable[[_type.UINT,  # TimeoutInMilliseconds
                                 _Pointer[_struct.DXGI_OUTDUPL_FRAME_INFO],  # pFrameInfo
                                 _Pointer[_dxgi.IDXGIResource]],  # ppDesktopResource
                                _type.HRESULT]
    GetFrameDirtyRects: _Callable[[_type.UINT,  # DirtyRectsBufferSize
                                   _Pointer[_struct.RECT],  # pDirtyRectsBuffer
                                   _Pointer[_type.UINT]],  # pDirtyRectsBufferSizeRequired
                                  _type.HRESULT]
    GetFrameMoveRects: _Callable[[_type.UINT,  # MoveRectsBufferSize
                                  _Pointer[_struct.DXGI_OUTDUPL_MOVE_RECT],  # pMoveRectBuffer
                                  _Pointer[_type.UINT]],  # pMoveRectsBufferSizeRequired
                                 _type.HRESULT]
    GetFramePointerShape: _Callable[[_type.UINT,  # PointerShapeBufferSize
                                     _type.c_void_p,  # pPointerShapeBuffer
                                     _Pointer[_type.UINT],  # pPointerShapeBufferSizeRequired
                                     _Pointer[_struct.DXGI_OUTDUPL_POINTER_SHAPE_INFO]],  # pPointerShapeInfo
                                    _type.HRESULT]
    MapDesktopSurface: _Callable[[_Pointer[_struct.DXGI_MAPPED_RECT]],  # pLockedRect
                                 _type.HRESULT]
    UnMapDesktopSurface: _Callable[[],
                                   _type.HRESULT]
    ReleaseFrame: _Callable[[],
                            _type.HRESULT]


class IDXGISurface2(_dxgi.IDXGISurface1):
    GetResource: _Callable[[_Pointer[_struct.IID],  # riid
                            _type.c_void_p,  # ppParentResource
                            _Pointer[_type.UINT]],  # pSubresourceIndex
                           _type.HRESULT]


class IDXGIResource1(_dxgi.IDXGIResource):
    CreateSubresourceSurface: _Callable[[_type.UINT,  # index
                                         _Pointer[IDXGISurface2]],  # ppSurface
                                        _type.HRESULT]
    CreateSharedHandle: _Callable[[_Pointer[_struct.SECURITY_ATTRIBUTES],  # pAttributes
                                   _type.DWORD,  # dwAccess
                                   _type.LPCWSTR,  # lpName
                                   _Pointer[_type.HANDLE]],  # pHandle
                                  _type.HRESULT]


class IDXGIDevice2(_dxgi.IDXGIDevice1):
    OfferResources: _Callable[[_type.UINT,  # NumResources
                               _Pointer[_dxgi.IDXGIResource],  # ppResources
                               _enum.DXGI_OFFER_RESOURCE_PRIORITY],  # Priority
                              _type.HRESULT]
    ReclaimResources: _Callable[[_type.UINT,  # NumResources
                                 _Pointer[_dxgi.IDXGIResource],  # ppResources
                                 _Pointer[_type.BOOL]],  # pDiscarded
                                _type.HRESULT]
    EnqueueSetEvent: _Callable[[_type.HANDLE],  # hEvent
                               _type.HRESULT]


class IDXGISwapChain1(_dxgi.IDXGISwapChain):
    GetDesc1: _Callable[[_Pointer[_struct.DXGI_SWAP_CHAIN_DESC1]],  # pDesc
                        _type.HRESULT]
    GetFullscreenDesc: _Callable[[_Pointer[_struct.DXGI_SWAP_CHAIN_FULLSCREEN_DESC]],  # pDesc
                                 _type.HRESULT]
    GetHwnd: _Callable[[_Pointer[_type.HWND]],  # pHwnd
                       _type.HRESULT]
    GetCoreWindow: _Callable[[_Pointer[_struct.IID],  # refiid
                              _type.c_void_p],  # ppUnk
                             _type.HRESULT]
    Present1: _Callable[[_type.UINT,  # SyncInterval
                         _type.UINT,  # PresentFlags
                         _Pointer[_struct.DXGI_PRESENT_PARAMETERS]],  # pPresentParameters
                        _type.HRESULT]
    IsTemporaryMonoSupported: _Callable[[],
                                        _type.BOOL]
    GetRestrictToOutput: _Callable[[_Pointer[_dxgi.IDXGIOutput]],  # ppRestrictToOutput
                                   _type.HRESULT]
    SetBackgroundColor: _Callable[[_Pointer[_struct.DXGI_RGBA]],  # pColor
                                  _type.HRESULT]
    GetBackgroundColor: _Callable[[_Pointer[_struct.DXGI_RGBA]],  # pColor
                                  _type.HRESULT]
    SetRotation: _Callable[[_enum.DXGI_MODE_ROTATION],  # Rotation
                           _type.HRESULT]
    GetRotation: _Callable[[_Pointer[_enum.DXGI_MODE_ROTATION]],  # pRotation
                           _type.HRESULT]


class IDXGIFactory2(_dxgi.IDXGIFactory1):
    IsWindowedStereoEnabled: _Callable[[],
                                       _type.BOOL]
    CreateSwapChainForHwnd: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                       _type.HWND,  # hWnd
                                       _Pointer[_struct.DXGI_SWAP_CHAIN_DESC1],  # pDesc
                                       _Pointer[_struct.DXGI_SWAP_CHAIN_FULLSCREEN_DESC],  # pFullscreenDesc
                                       _dxgi.IDXGIOutput,  # pRestrictToOutput
                                       _Pointer[IDXGISwapChain1]],  # ppSwapChain
                                      _type.HRESULT]
    CreateSwapChainForCoreWindow: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                             _Unknwnbase.IUnknown,  # pWindow
                                             _Pointer[_struct.DXGI_SWAP_CHAIN_DESC1],  # pDesc
                                             _dxgi.IDXGIOutput,  # pRestrictToOutput
                                             _Pointer[IDXGISwapChain1]],  # ppSwapChain
                                            _type.HRESULT]
    GetSharedResourceAdapterLuid: _Callable[[_type.HANDLE,  # hResource
                                             _Pointer[_struct.LUID]],  # pLuid
                                            _type.HRESULT]
    RegisterStereoStatusWindow: _Callable[[_type.HWND,  # WindowHandle
                                           _type.UINT,  # wMsg
                                           _Pointer[_type.DWORD]],  # pdwCookie
                                          _type.HRESULT]
    RegisterStereoStatusEvent: _Callable[[_type.HANDLE,  # hEvent
                                          _Pointer[_type.DWORD]],  # pdwCookie
                                         _type.HRESULT]
    UnregisterStereoStatus: _Callable[[_type.DWORD],  # dwCookie
                                      _type.c_void]
    RegisterOcclusionStatusWindow: _Callable[[_type.HWND,  # WindowHandle
                                              _type.UINT,  # wMsg
                                              _Pointer[_type.DWORD]],  # pdwCookie
                                             _type.HRESULT]
    RegisterOcclusionStatusEvent: _Callable[[_type.HANDLE,  # hEvent
                                             _Pointer[_type.DWORD]],  # pdwCookie
                                            _type.HRESULT]
    UnregisterOcclusionStatus: _Callable[[_type.DWORD],  # dwCookie
                                         _type.c_void]
    CreateSwapChainForComposition: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                              _Pointer[_struct.DXGI_SWAP_CHAIN_DESC1],  # pDesc
                                              _dxgi.IDXGIOutput,  # pRestrictToOutput
                                              _Pointer[IDXGISwapChain1]],  # ppSwapChain
                                             _type.HRESULT]


class IDXGIAdapter2(_dxgi.IDXGIAdapter1):
    GetDesc2: _Callable[[_Pointer[_struct.DXGI_ADAPTER_DESC2]],  # pDesc
                        _type.HRESULT]


class IDXGIOutput1(_dxgi.IDXGIOutput):
    GetDisplayModeList1: _Callable[[_enum.DXGI_FORMAT,  # EnumFormat
                                    _type.UINT,  # Flags
                                    _Pointer[_type.UINT],  # pNumModes
                                    _Pointer[_struct.DXGI_MODE_DESC1]],  # pDesc
                                   _type.HRESULT]
    FindClosestMatchingMode1: _Callable[[_Pointer[_struct.DXGI_MODE_DESC1],  # pModeToMatch
                                         _Pointer[_struct.DXGI_MODE_DESC1],  # pClosestMatch
                                         _Unknwnbase.IUnknown],  # pConcernedDevice
                                        _type.HRESULT]
    GetDisplaySurfaceData1: _Callable[[_dxgi.IDXGIResource],  # pDestination
                                      _type.HRESULT]
    DuplicateOutput: _Callable[[_Unknwnbase.IUnknown,  # pDevice
                                _Pointer[IDXGIOutputDuplication]],  # ppOutputDuplication
                               _type.HRESULT]
